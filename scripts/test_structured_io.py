"""Protect business values and evidence when switching serialization formats."""
import copy
from pathlib import Path
import unittest
import os
from unittest.mock import patch
from scripts import structured_io
from scripts import parsed_cache

from scripts.structured_io import loads, dumps, read, working_path
from scripts.element_versions import assign_versions
from scripts.test_publish_release import isolated_project


class StructuredIOTests(unittest.TestCase):
    def test_sequence_append_keeps_exact_old_bytes_and_root_fields(self):
        fixtures = [
            '# kept\nschema_version: 1.0.0\nintents:\n- text: café\nsuspensions: []\n',
            'schema_version: 1.0.0\nintents:\n- text: |\n    suspensions:\n    Unicode é\n# kept\nsuspensions: []\n',
            'suspensions: []\nintents:\n- text: "quoted\\nintents:"\n...\n',
            'intents:\n- text: last\n',
        ]
        with isolated_project() as root, patch.object(parsed_cache, 'DIRECTORY', root/'cache'):
            for fixture in fixtures:
                for newline, bom in [('\n', b''), ('\r\n', b'\xef\xbb\xbf')]:
                    before = bom + fixture.replace('\n', newline).encode('utf-8')
                    document, offset = structured_io.load_for_sequence_append(before, 'intents')
                    self.assertIsNotNone(offset)
                    expected = copy.deepcopy(document)
                    items = [{'text': 'new\nsuspensions:\nfin', 'code': '00123'}]
                    expected['intents'].extend(items)
                    result = structured_io.dump_sequence_append(before, expected, 'intents', items, offset)
                    prefix = bom + before.decode('utf-8-sig')[:offset].encode('utf-8')
                    suffix = before.decode('utf-8-sig')[offset:].encode('utf-8')
                    self.assertTrue(result.startswith(prefix))
                    self.assertTrue(result.endswith(suffix))
                    self.assertEqual(loads(result.decode('utf-8-sig')), expected)
                    # The next append reads from the cache seeded by serialization.
                    with patch.object(structured_io, 'ModelLoader', side_effect=AssertionError('Reparsed')):
                        cached, next_offset = structured_io.load_for_sequence_append(result, 'intents')
                    self.assertEqual(cached, expected)
                    more = [{'text': 'third'}]
                    cached['intents'].extend(more)
                    third = structured_io.dump_sequence_append(result, cached, 'intents', more, next_offset)
                    self.assertEqual(loads(third.decode('utf-8-sig')), cached)

    def test_sequence_append_fallback_for_non_block_layouts(self):
        for text in ('intents: []\n', 'intents: [{name: first}]\n',
                     'intents:\n  - name: first\n', 'intents:\n- name: first'):
            before = text.encode()
            doc, offset = structured_io.load_for_sequence_append(before, 'intents')
            self.assertIsNone(offset)
            new = [{'name': 'second'}]
            doc['intents'].extend(new)
            result = structured_io.dump_sequence_append(before, doc, 'intents', new, offset)
            self.assertEqual(loads(result.decode()), doc)

    def test_sequence_append_rejects_invalid_yaml_and_corrupt_cache(self):
        with isolated_project() as root, patch.object(parsed_cache, 'DIRECTORY', root/'cache'):
            before = b'intents:\n- name: valid\n'
            expected = structured_io.load_for_sequence_append(before, 'intents')
            entry = next((root/'cache').glob('*.json'))
            entry.write_bytes(entry.read_bytes().replace(b'valid', b'wrong'))
            self.assertEqual(structured_io.load_for_sequence_append(before, 'intents'), expected)
            changed = before.replace(b'valid', b'other')
            self.assertEqual(structured_io.load_for_sequence_append(changed, 'intents')[0],
                             {'intents': [{'name': 'other'}]})
            for text in ('intents: []\nintents: []', 'intents: &x [*x]',
                         'intents: [!!float .nan]', '1: []', 'intents: []\n---\nintents: []'):
                with self.subTest(text=text), self.assertRaises(ValueError):
                    structured_io.load_for_sequence_append(text.encode(), 'intents')

    def test_oversized_entry_does_not_flush_smaller_working_set(self):
        with isolated_project() as folder, patch.object(structured_io, '_CACHE_LIMIT', 100):
            structured_io.clear_read_cache()
            small = folder/'small.yaml'; small.write_text('a: small', encoding='utf-8')
            large = folder/'large.yaml'; large.write_text('a: ' + 'x'*80, encoding='utf-8')
            read(small); read(large)
            with patch.object(structured_io, 'loads', side_effect=AssertionError('Small entry evicted')):
                self.assertEqual(read(small), {'a':'small'})
            self.assertLessEqual(structured_io._cache_bytes, 100)
        structured_io.clear_read_cache()

    def test_cache_is_content_based_and_does_not_share_mutations(self):
        with isolated_project() as folder:
            path = folder/'cached.yaml'
            path.write_text('items: [first]', encoding='utf-8')
            stamp = path.stat()
            structured_io.clear_read_cache()
            with patch.object(structured_io, 'loads', wraps=loads) as parser:
                read(path)['items'].append('local mutation')
                self.assertEqual(read(path), {'items': ['first']})
                self.assertEqual(parser.call_count, 1)
                path.write_text('items: [other]', encoding='utf-8')
                os.utime(path, ns=(stamp.st_atime_ns, stamp.st_mtime_ns))
                self.assertEqual(read(path), {'items': ['other']})
                self.assertEqual(parser.call_count, 2)
                path.write_text('items: [', encoding='utf-8')
                with self.assertRaises(ValueError):
                    read(path)

    def test_cache_evicts_entries_at_its_memory_bound(self):
        with isolated_project() as folder, patch.object(structured_io, '_CACHE_LIMIT', 16):
            structured_io.clear_read_cache()
            for i in range(5):
                path = folder/(str(i)+'.yaml')
                path.write_text('value: '+str(i), encoding='utf-8')
                self.assertEqual(read(path), {'value': i})
            self.assertLessEqual(structured_io._cache_bytes, 16)
            self.assertLessEqual(len(structured_io._cache), 2)
        structured_io.clear_read_cache()

    def test_identifiers_dates_and_multiline_text_keep_their_types_and_bytes(self):
        document = {'code': '00123', 'flag_word': 'on', 'date': '2026-09-14',
                    'time': '2026-09-14T15:00:00Z', 'empty': '', 'null_word': 'null',
                    'description': 'Consulter le [stock](glossary:TER005).\nDeuxième ligne.\n',
                    'values': [True, False, None, 1, 1.5, 1e20]}
        actual = loads(dumps(document))
        self.assertEqual(actual, document)
        for key in document:
            self.assertIs(type(actual[key]), type(document[key]))
        self.assertEqual(loads('code: 00123\nword: on\ndate: 2026-09-14'),
                         {'code': '00123', 'word': 'on', 'date': '2026-09-14'})

    def test_ambiguous_or_non_json_values_are_rejected(self):
        for text in ('name: first\nname: second', '1: value', 'a: &a [*a]',
                     'a: !!python/object/apply:os.system [echo test]', 'a: !!float .nan',
                     'a: !!timestamp 2026-09-14', 'a: 1\n---\na: 2'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                loads(text)
        with self.assertRaises(ValueError):
            loads('{"name":1,"name":2}', '.json')

    def test_no_competing_live_authority_or_hidden_fallback(self):
        with isolated_project() as folder:
            (folder/'model.json').write_text('{"value": 1}', encoding='utf-8')
            self.assertEqual(working_path(folder).suffix, '.json')
            (folder/'model.yaml').write_text('broken: [', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Competing'):
                working_path(folder)
            with self.assertRaises(ValueError):
                read(folder/'model.yaml')

    def test_yaml_conversion_and_comments_do_not_increment_semantic_revisions(self):
        root = Path(__file__).resolve().parents[1]
        baseline = read(root/'modeles/revisions/2026-09-13.5/backlog.json')
        first = copy.deepcopy(baseline)
        assign_versions(first, baseline, now='2026-09-14T00:00:00Z')
        converted = loads('# Only formatting changed\n' + dumps(first))
        changes = assign_versions(converted, first, now='2026-09-15T00:00:00Z')
        self.assertEqual(changes, [])
        self.assertEqual(converted['revision'], first['revision'])
        self.assertEqual(converted['last_modified'], first['last_modified'])


if __name__ == '__main__':
    unittest.main()

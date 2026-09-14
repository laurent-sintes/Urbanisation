"""Protect business values and evidence when switching serialization formats."""
import copy
from pathlib import Path
import unittest

from scripts.structured_io import loads, dumps, read, working_path
from scripts.element_versions import assign_versions
from scripts.test_publish_release import isolated_project


class StructuredIOTests(unittest.TestCase):
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

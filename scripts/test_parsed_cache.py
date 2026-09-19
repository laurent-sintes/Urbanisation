"""Cross-command acceleration preserves parser and publication contracts."""
from hashlib import sha256
import json
import os
import subprocess
import sys
import unittest
from unittest.mock import patch
from scripts import parsed_cache, structured_io
from scripts.test_publish_release import isolated_project


class ParsedCacheTests(unittest.TestCase):
    def setUp(self):
        structured_io.clear_read_cache()
        self.addCleanup(structured_io.clear_read_cache)

    def test_reuse_after_memory_clear_keeps_values_and_mutation_isolation(self):
        with isolated_project() as root, patch.object(parsed_cache, 'DIRECTORY', root/'cache'), patch.object(structured_io, '_DISK_MIN_BYTES', 0):
            path = root/'source.yaml'
            path.write_text('a: [00123, on, 2026-09-19, true, null, 1.5]', encoding='utf-8')
            expected = structured_io.read(path)
            structured_io.clear_read_cache()
            with patch.object(structured_io, 'loads', side_effect=AssertionError('Reparsed')):
                structured_io.read(path)['a'].append('mutated')
                self.assertEqual(structured_io.read(path), expected)

    def test_same_metadata_changed_bytes_and_changed_parser_cannot_reuse(self):
        with isolated_project() as root, patch.object(parsed_cache, 'DIRECTORY', root/'cache'), patch.object(structured_io, '_DISK_MIN_BYTES', 0):
            path = root/'source.yaml'
            path.write_text('a: first', encoding='utf-8')
            stamp = path.stat()
            structured_io.read(path)
            path.write_text('a: other', encoding='utf-8')
            os.utime(path, ns=(stamp.st_atime_ns, stamp.st_mtime_ns))
            structured_io.clear_read_cache()
            self.assertEqual(structured_io.read(path), {'a': 'other'})
            structured_io.clear_read_cache()
            with patch.object(structured_io, '_PARSER_SIGNATURE', b'new parser'), patch.object(structured_io, 'loads', wraps=structured_io.loads) as parse:
                self.assertEqual(structured_io.read(path), {'a': 'other'})
                self.assertEqual(parse.call_count, 1)

    def test_corrupted_entry_falls_back_and_invalid_sources_never_cache(self):
        with isolated_project() as root, patch.object(parsed_cache, 'DIRECTORY', root/'cache'), patch.object(structured_io, '_DISK_MIN_BYTES', 0):
            path = root/'source.yaml'; path.write_text('a: valid', encoding='utf-8')
            structured_io.read(path)
            entry = next((root/'cache').glob('*.json'))
            entry.write_bytes(entry.read_bytes().replace(b'valid', b'wrong'))
            structured_io.clear_read_cache()
            self.assertEqual(structured_io.read(path), {'a': 'valid'})
            before = set((root/'cache').iterdir())
            for invalid in ('a: 1\na: 2', 'a: &x [*x]', 'a: !!float .nan', '1: value', 'a: ['):
                path.write_text(invalid, encoding='utf-8')
                with self.assertRaises(ValueError): structured_io.read(path)
            self.assertEqual(set((root/'cache').iterdir()), before)

    def test_missing_or_unwritable_cache_cannot_block_reads(self):
        with isolated_project() as root, patch.object(parsed_cache, 'DIRECTORY', root/'not-a-directory'), patch.object(structured_io, '_DISK_MIN_BYTES', 0):
            (root/'not-a-directory').write_text('file', encoding='utf-8')
            path=root/'source.yaml'; path.write_text('a: valid', encoding='utf-8')
            self.assertEqual(structured_io.read(path), {'a':'valid'})

    def test_disk_bound_preserves_unrelated_files(self):
        with isolated_project() as root, patch.object(parsed_cache, 'DIRECTORY', root), patch.object(parsed_cache, 'MAX_ENTRIES', 2):
            unrelated=root/'keep.json'; unrelated.write_text('keep', encoding='utf-8')
            for i in range(4): parsed_cache.put(sha256(str(i).encode()).hexdigest(), {'i':i})
            self.assertEqual(len(list(root.glob('*.json'))), 3)
            self.assertEqual(unrelated.read_text(), 'keep')

    def test_new_process_reads_the_same_cached_value(self):
        with isolated_project() as root, patch.object(parsed_cache, 'DIRECTORY', root/'cache'), patch.object(structured_io, '_DISK_MIN_BYTES', 0):
            path=root/'source.yaml'; path.write_text('a: [one, two]', encoding='utf-8')
            structured_io.read(path)
            program = "from pathlib import Path; from scripts import structured_io as s, parsed_cache as c; import sys,json; c.DIRECTORY=Path(sys.argv[1]); s._DISK_MIN_BYTES=0; s.loads=lambda *a: (_ for _ in ()).throw(AssertionError('Reparsed')); print(json.dumps(s.read(sys.argv[2])))"
            result=subprocess.run([sys.executable,'-c',program,str(root/'cache'),str(path)],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(json.loads(result.stdout),{'a':['one','two']})


if __name__ == '__main__': unittest.main()

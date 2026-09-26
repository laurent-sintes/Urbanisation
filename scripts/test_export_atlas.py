"""Static export boundaries: explicit index, immutable snapshots, atomic activation."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from scripts.export_atlas import export_atlas, encoded


class StaticExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.release = self.root / 'modeles/release'
        self.output = self.root / 'site/data'
        self.release.mkdir(parents=True)
        entries = []
        for version in ('2026-09-25.1', '2026-09-26.1'):
            folder = self.release / version
            folder.mkdir()
            model = encoded({'space': 'release', 'version': version, 'nodes': [], 'relations': [], 'glossary': {'terms': []}})
            (folder / 'model.json').write_bytes(model)
            descriptor = encoded({'version': version, 'path': version + '/model.json', 'sha256': hashlib.sha256(model).hexdigest()})
            name = version + '.json'
            (self.release / name).write_bytes(descriptor)
            entries.append({'descriptor': name, 'sha256': hashlib.sha256(descriptor).hexdigest()})
        # Current is deliberately NOT the highest version.
        (self.release / 'index.json').write_bytes(encoded({'current': entries[0]['descriptor'], 'publications': entries}))

    def test_explicit_pointer_exact_content_and_idempotent_export(self):
        (self.root / 'modeles/backlog').mkdir()
        (self.root / 'modeles/backlog/model.yaml').write_text('invalid live backlog')
        result = export_atlas(self.root, [self.output])
        self.assertEqual(result['current_version'], '2026-09-25.1')
        catalog = json.loads((self.output / 'index.json').read_bytes())
        for entry in catalog['versions']:
            version = entry['version']
            payload = (self.output / version / 'model.json').read_bytes()
            model = json.loads(payload)
            self.assertEqual(model.pop('sourcePath'), f'modeles/release/{version}/model.json')
            self.assertEqual(model, json.loads((self.release / version / 'model.json').read_bytes()))
            self.assertEqual(hashlib.sha256(payload).hexdigest(), entry['model_sha256'])
            guide = json.loads((self.output / version / 'guide.json').read_bytes())
            self.assertEqual(guide['publication_version'], version)
            self.assertEqual(guide['status'], 'unavailable')
        before = {p: p.stat().st_mtime_ns for p in self.output.rglob('*.json')}
        export_atlas(self.root, [self.output])
        self.assertEqual(before, {p: p.stat().st_mtime_ns for p in before})

    def test_corrupt_publication_does_not_activate_partial_export(self):
        export_atlas(self.root, [self.output])
        before = {p: p.read_bytes() for p in self.output.rglob('*.json')}
        (self.release / '2026-09-26.1/model.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            export_atlas(self.root, [self.output])
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_missing_index_is_not_inferred_from_directories(self):
        (self.release / 'index.json').unlink()
        with self.assertRaises(FileNotFoundError):
            export_atlas(self.root, [self.output])
        self.assertFalse(self.output.exists())

    def test_shared_lock_refuses_other_process_and_allows_nested_owner(self):
        import subprocess
        import sys
        from scripts.atlas_lock import atlas_lock
        with atlas_lock(self.root):
            export_atlas(self.root, [self.output])
            child = subprocess.run([sys.executable, '-c',
                'import sys; from pathlib import Path; from scripts.export_atlas import export_atlas; export_atlas(Path(sys.argv[1]))',
                str(self.root)], capture_output=True, text=True)
            self.assertNotEqual(child.returncode, 0)
            self.assertIn('Atlas is being', child.stderr)
        export_atlas(self.root, [self.output])

    def test_pointer_change_during_writes_refuses_old_catalog_activation(self):
        from unittest.mock import patch
        from scripts import export_atlas as module
        original = module.atomic_write
        def changed(path, payload):
            if Path(path).name == 'model.json':
                index_path = self.release / 'index.json'
                index = json.loads(index_path.read_bytes())
                index['current'] = '2026-09-26.1.json'
                index_path.write_bytes(encoded(index))
            original(path, payload)
        with patch.object(module, 'atomic_write', side_effect=changed):
            with self.assertRaisesRegex(ValueError, 'before static activation'):
                export_atlas(self.root, [self.output])
        self.assertFalse((self.output / 'index.json').exists())
        export_atlas(self.root, [self.output])
        self.assertEqual(json.loads((self.output / 'index.json').read_bytes())['current_version'], '2026-09-26.1')

    def test_activation_failure_preserves_served_catalog_and_cleans_temp(self):
        from unittest.mock import patch
        from scripts import export_atlas as module
        export_atlas(self.root, [self.output])
        previous = (self.output / 'index.json').read_bytes()
        index_path = self.release / 'index.json'
        index = json.loads(index_path.read_bytes())
        index['current'] = '2026-09-26.1.json'
        index_path.write_bytes(encoded(index))
        with patch.object(module.os, 'replace', side_effect=OSError('interrupted')):
            with self.assertRaises(OSError):
                export_atlas(self.root, [self.output])
        self.assertEqual((self.output / 'index.json').read_bytes(), previous)
        self.assertEqual(list(self.output.rglob('*.tmp')), [])
        export_atlas(self.root, [self.output])


if __name__ == '__main__':
    unittest.main()

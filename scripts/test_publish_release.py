"""Publication workflow tests; all writes stay in isolated temporary projects."""

from copy import deepcopy
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import shutil
import unittest
from unittest.mock import patch
import uuid

try:
    from . import publish_release as publisher
except ImportError:
    import publish_release as publisher


ROOT = Path(__file__).resolve().parents[1]


@contextmanager
def isolated_project():
    # Plain mkdir inherits workspace ACLs; Windows mkdtemp(mode=0700) can
    # produce an inaccessible directory under the restricted execution token.
    base = (ROOT / '.tmp-model-publication-tests').resolve()
    base.mkdir(exist_ok=True)
    folder = base / uuid.uuid4().hex
    folder.mkdir()
    try:
        yield folder
    finally:
        resolved = folder.resolve()
        if resolved.parent != base or len(resolved.name) != 32:
            raise ValueError('Refusing cleanup outside the isolated test directory')
        shutil.rmtree(resolved)
        try:
            base.rmdir()
        except OSError:
            pass  # Another independent test may still use its own child.


def save(path, document):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def source(identifier, text):
    return {'id': identifier, 'path': 'notes.md', 'anchor': identifier.lower(),
            'captured_text': text, 'content_sha256': hashlib.sha256(text.strip().encode()).hexdigest()}


class PublicationEvidenceTests(unittest.TestCase):
    def test_live_changes_do_not_replace_frozen_proof(self):
        frozen = {'records': [source('U1', 'original proof')]}
        live = {'records': [source('U1', 'later context'), source('U2', 'publish'), source('U3', 'unrelated')]}
        merged = publisher.publication_sources(frozen, live, ['U2'])
        self.assertEqual(merged['records'], [frozen['records'][0], live['records'][1]])
        self.assertEqual(frozen['records'][0]['captured_text'], 'original proof')

    def test_explicit_reuse_of_contradictory_frozen_id_rejected(self):
        frozen = {'records': [source('U1', 'original')]}
        with self.assertRaisesRegex(ValueError, 'contradictory'):
            publisher.publication_sources(frozen, {'records': [source('U1', 'different')]}, ['U1'])

    def test_bad_new_proof_and_unknown_id_rejected(self):
        corrupt = source('U2', 'new')
        corrupt['captured_text'] = 'altered without hash'
        for live, refs in (({'records': [corrupt]}, ['U2']), ({'records': []}, ['U2'])):
            with self.subTest(refs=refs), self.assertRaises(ValueError):
                publisher.publication_sources({'records': []}, live, refs)

    def test_failed_atomic_activation_keeps_old_pointer(self):
        with isolated_project() as folder:
            path = folder / 'current.json'
            save(path, {'version': 'old'})
            before = path.read_bytes()
            with patch.object(publisher.os, 'replace', side_effect=OSError('simulated interruption')):
                with self.assertRaises(OSError):
                    publisher.activate_pointer(path, {'version': 'new'})
            self.assertEqual(path.read_bytes(), before)
            self.assertEqual(list(folder.glob('.current-*.tmp')), [])


class PublicationWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = isolated_project()
        self.root = self.temp.__enter__()
        self.addCleanup(self.temp.__exit__, None, None, None)
        # Copy only inputs used by the publisher, never the live backlog.
        for relative in ('schemas', 'decisions', 'revisions', 'provenance', 'release/2026-09-13.2'):
            shutil.copytree(ROOT / 'modeles' / relative, self.root / 'modeles' / relative)
        save(self.root / 'modeles/release/current.json', {'version': 'unchanged'})
        self.manifest = self.root / 'modeles/release/2026-09-13.2/manifest.json'
        self.version = '2026-09-13.99'
        live_path = self.root / 'modeles/provenance/source-records.json'
        live = publisher.read(live_path)
        live['records'].append(source('PUB-TEST-NEW', 'Authorized next publication'))
        save(live_path, live)

    def test_publication_uses_frozen_inputs_and_activates_last(self):
        original = (self.manifest.parent / 'model.json').read_bytes()
        result = publisher.publish(self.manifest, self.version, ['PUB-TEST-NEW'], activate=True)
        self.assertEqual((result['capability_count'], result['complete_capability_count']), (36, 9))
        current = publisher.read(self.root / 'modeles/release/current.json')
        self.assertEqual(current['version'], self.version)
        self.assertEqual((self.manifest.parent / 'model.json').read_bytes(), original)
        proof = publisher.read(self.root / f'modeles/provenance/{self.version}/source-records.json')
        self.assertIn('PUB-TEST-NEW', {record['id'] for record in proof['records']})
        with self.assertRaisesRegex(ValueError, 'already exists'):
            publisher.publish(self.manifest, self.version, ['PUB-TEST-NEW'])

    def test_validation_failure_creates_no_publication(self):
        with self.assertRaisesRegex(ValueError, 'Unknown publication source'):
            publisher.publish(self.manifest, self.version, ['ABSENT'])
        self.assertFalse((self.root / f'modeles/release/{self.version}').exists())
        self.assertFalse((self.root / f'modeles/provenance/{self.version}').exists())
        self.assertEqual(publisher.read(self.root / 'modeles/release/current.json')['version'], 'unchanged')

    def test_tampered_frozen_provenance_rejected_before_writes(self):
        manifest = publisher.read(self.manifest)
        frozen = (self.manifest.parent / manifest['provenance_path']).resolve()
        frozen.write_text(frozen.read_text(encoding='utf-8') + ' ', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'digest mismatch'):
            publisher.publish(self.manifest, self.version, ['PUB-TEST-NEW'])
        self.assertFalse((self.root / f'modeles/release/{self.version}').exists())

    def test_unsafe_or_ambiguous_versions_rejected(self):
        for version in ('../escape', 'C:escape', 'CON', '2026-09-13.3 ', '2026-09-13.0', '2026-99-99.1'):
            with self.subTest(version=version), self.assertRaises(ValueError):
                publisher.publish(self.manifest, version, ['PUB-TEST-NEW'])


if __name__ == '__main__':
    unittest.main()

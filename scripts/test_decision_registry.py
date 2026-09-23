"""Split storage must preserve agreement semantics and fail closed on corruption."""
from copy import deepcopy
from unittest.mock import patch
from scripts import decision_registry as registry
from scripts import record_decision as recorder
from scripts.structured_io import read, dumps
import unittest
from scripts import test_record_decision as fixtures


class ShardedRegistryTests(unittest.TestCase):
    setUp = fixtures.DecisionIntentTests.setUp
    save = fixtures.DecisionIntentTests.save
    record = fixtures.DecisionIntentTests.record
    snapshot = fixtures.DecisionIntentTests.snapshot
    def document(self):
        return registry.read_registry(self.root / recorder.REGISTRY_PATH, self.sources)

    def split(self):
        self.record()
        self.path = self.root / recorder.REGISTRY_PATH
        original = self.document()
        registry.migrate(self.root, [self.params['intent_id']])
        self.assertEqual(self.document(), original | {'suspensions': []})
        return read(self.path)

    def test_split_roundtrip_and_writes(self):
        index = self.split()
        self.assertIn('/archive/', index['entries'][0]['path'])
        shard = registry.shard_path(self.path, index['entries'][0])
        before = shard.read_bytes()
        self.assertFalse(self.record()['recorded'])
        self.assertTrue(self.record(intent_id='SECOND')['recorded'])
        self.assertEqual(shard.read_bytes(), before)
        self.assertEqual(len(self.document()['intents']), 2)
        self.assertFalse(registry.migrate(self.root)['migrated'])

    def test_corruption_missing_shard_and_path_escape_block_writes(self):
        index = self.split()
        shard = registry.shard_path(self.path, index['entries'][0])
        content = shard.read_bytes()
        shard.write_bytes(content + b'# changed\n')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            self.record(intent_id='SECOND')
        shard.unlink()
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            self.record(intent_id='SECOND')
        shard.write_bytes(content)
        index['entries'][0]['path'] = '../outside.yaml'
        self.path.write_text(dumps(index), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'path'):
            self.record(intent_id='SECOND')

    def test_full_reader_rejects_index_summary_tampering(self):
        index = self.split()
        index['entries'][0]['target']['id'] = 'OTHER'
        self.path.write_text(dumps(index), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'summary mismatch'):
            self.document()

    def test_suspension_and_consumed_history_survive_migration(self):
        original = deepcopy(self.record()['intent'])
        document = read(self.root / recorder.REGISTRY_PATH)
        document['suspensions'] = [{'intent_id': original['id'], 'reviewer': 'Codex',
            'reviewed_at': '2026-09-22', 'source_refs': ['U1'], 'rationale': 'Explicit review'}]
        self.save(recorder.REGISTRY_PATH, document)
        registry.migrate(self.root)
        migrated = self.document()
        self.assertEqual(document, migrated)
        self.assertEqual(recorder.compile_intents(migrated, self.snapshot(), [], self.sources, document)['decisions'], [])

    def test_interrupted_index_write_keeps_old_registry_readable(self):
        self.split()
        before = self.path.read_bytes()
        original_replace = registry.atomic_replace
        def fail_index(path, old, content):
            if path == self.path:
                raise OSError('interrupted')
            return original_replace(path, old, content)
        with patch.object(registry, 'atomic_replace', side_effect=fail_index):
            with self.assertRaises(OSError):
                self.record(intent_id='SECOND')
        self.assertEqual(before, self.path.read_bytes())
        self.assertEqual(len(self.document()['intents']), 1)
        self.assertTrue(self.record(intent_id='SECOND')['recorded'])

    def test_replacement_and_duplicate_batch_contracts(self):
        self.split()
        with self.assertRaisesRegex(ValueError, 'earlier'):
            self.record(intent_id='SECOND', supersedes='absent')
        self.record(intent_id='SECOND', supersedes=self.params['intent_id'], fields=['name'])
        with self.assertRaisesRegex(ValueError, 'unreplaced'):
            self.record(intent_id='THIRD', supersedes=self.params['intent_id'])
        params = self.params | {'intent_id': 'FOURTH'}
        results = recorder.record_intents(self.root, [params, params])
        self.assertEqual([r['recorded'] for r in results], [True, False])

    def check_project(self):
        return registry.validate_project_registry(self.root, self.sources, '2026-09-22.1')

    def test_project_checks_full_captures_even_when_byte_hash_is_updated(self):
        from hashlib import sha256
        index = self.split()
        entry = index['entries'][0]
        intent = registry.load_entry(self.path, entry)
        intent['target']['values']['name'] = 'Changed without semantic hash'
        content = dumps([intent]).encode('utf-8')
        digest = sha256(content).hexdigest()
        entry['path'] = 'decision-intents/archive/' + digest + '.yaml'
        entry['sha256'] = digest
        registry.shard_path(self.path, entry).write_bytes(content)
        self.path.write_text(dumps(index), encoding='utf-8')
        errors, _ = self.check_project()
        self.assertTrue(any('value hash mismatch' in e for e in errors), errors)

    def test_project_checks_frozen_agreements_and_missing_index(self):
        self.split()
        frozen = self.root/'modeles/revisions/2026-09-22.1/deferred/decision-intents.yaml'
        frozen.parent.mkdir(parents=True)
        frozen.write_text(dumps(self.document()), encoding='utf-8')
        index = read(self.path)
        index['entries'] = []
        self.path.write_text(dumps(index), encoding='utf-8')
        errors, _ = self.check_project()
        self.assertTrue(any('removed or changed' in e for e in errors), errors)
        self.path.unlink()
        self.assertTrue(any('index is missing' in e for e in self.check_project()[0]))

    def test_project_preserves_suspensions_and_accepts_pending_context_changes(self):
        self.split()
        index = read(self.path)
        index['suspensions'] = [{'intent_id': self.params['intent_id'], 'reviewer': 'Codex',
            'reviewed_at': '2026-09-22', 'source_refs': ['U1'], 'rationale': 'Reviewed'}]
        self.path.write_text(dumps(index), encoding='utf-8')
        frozen = self.root/'modeles/revisions/2026-09-22.1/deferred/decision-intents.yaml'
        frozen.parent.mkdir(parents=True)
        frozen.write_text(dumps(self.document()), encoding='utf-8')
        self.model['nodes'][1]['fields']['name'] = 'New working name'
        self.save('modeles/backlog/model.yaml', self.model)
        self.assertEqual(self.check_project()[0], [])
        index['suspensions'] = []
        self.path.write_text(dumps(index), encoding='utf-8')
        self.assertTrue(any('suspension was removed' in e for e in self.check_project()[0]))

    def test_project_reports_orphans_without_adopting_or_deleting_them(self):
        self.split()
        orphan = self.path.parent/'decision-intents/archive'/('0'*64 + '.yaml')
        orphan.write_text('not an approval', encoding='utf-8')
        errors, counts = self.check_project()
        self.assertEqual(errors, [])
        self.assertEqual(counts['decision_intents'], 1)
        self.assertEqual(counts['decision_unreferenced_shards'], 1)
        self.assertTrue(orphan.exists())

    def test_project_reports_unknown_sources_and_malformed_index(self):
        original = self.split()
        for change in ({'source_refs': ['missing']}, {'path': []}, {'sha256': 'bad'}):
            index = deepcopy(original)
            index['entries'][0].update(change)
            self.path.write_text(dumps(index), encoding='utf-8')
            self.assertTrue(self.check_project()[0], change)

    def test_project_without_registry_is_compatible_with_legacy_projects(self):
        self.assertEqual(self.check_project(), ([], {'decision_intents': 0}))

    def test_replacement_rejects_desynchronized_predecessor_before_writing(self):
        index = self.split()
        index['entries'][0]['target']['approved_fields'].append('scope')
        self.path.write_text(dumps(index), encoding='utf-8')
        before = self.path.read_bytes()
        files = set(self.path.parent.rglob('*.yaml'))
        with self.assertRaisesRegex(ValueError, 'summary mismatch'):
            self.record(intent_id='REPLACEMENT', fields=['scope'], supersedes=self.params['intent_id'])
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(set(self.path.parent.rglob('*.yaml')), files)

    def test_declared_frozen_registry_cannot_disappear_or_change(self):
        from hashlib import sha256
        self.split()
        frozen = self.root/'modeles/revisions/2026-09-22.1/deferred/decision-intents.yaml'
        frozen.parent.mkdir(parents=True)
        content = dumps(self.document()).encode('utf-8')
        frozen.write_bytes(content)
        manifest = self.root/'modeles/release/2026-09-22.1/manifest.json'
        manifest.parent.mkdir(parents=True)
        manifest.write_text(dumps({'decision_registry_files': {'deferred/decision-intents.yaml': sha256(content).hexdigest()}}, '.json'), encoding='utf-8')
        self.assertEqual(self.check_project()[0], [])
        for changed in (None, content + b'# modified\n'):
            if changed is None:
                frozen.unlink()
            else:
                frozen.write_bytes(changed)
            self.assertTrue(any('artifact missing or changed' in e for e in self.check_project()[0]))
        manifest.write_text(dumps({'decision_registry_files': None}, '.json'), encoding='utf-8')
        self.assertTrue(any('Invalid frozen registry inventory' in e for e in self.check_project()[0]))

    def test_legacy_preparation_hash_authenticates_inventory(self):
        from hashlib import sha256
        self.split()
        frozen = self.root/'modeles/revisions/2026-09-22.1/deferred/decision-intents.yaml'
        frozen.parent.mkdir(parents=True)
        frozen.write_text(dumps(self.document()), encoding='utf-8')
        prepared = self.root/'modeles/staging/2026-09-22.1/manifest.json'
        prepared.parent.mkdir(parents=True)
        prepared.write_text(dumps({'deferred': [{'path': 'deferred/decision-intents.yaml', 'sha256': sha256(frozen.read_bytes()).hexdigest()}]}, '.json'), encoding='utf-8')
        manifest = self.root/'modeles/release/2026-09-22.1/manifest.json'
        manifest.parent.mkdir(parents=True)
        manifest.write_text(dumps({'prepared_manifest_sha256': sha256(prepared.read_bytes()).hexdigest()}, '.json'), encoding='utf-8')
        self.assertEqual(self.check_project()[0], [])
        prepared.write_text('{}', encoding='utf-8')
        self.assertTrue(any('prepared manifest missing or changed' in e for e in self.check_project()[0]))
        prepared.unlink()
        self.assertTrue(any('prepared manifest missing or changed' in e for e in self.check_project()[0]))

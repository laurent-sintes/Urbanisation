"""Backlog publication tests. Every mutation uses an isolated project fixture."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import unittest

try:
    from . import prepare_release as workflow
    from .test_publish_release import isolated_project, save, source
except ImportError:
    import prepare_release as workflow
    from test_publish_release import isolated_project, save, source

ROOT = Path(__file__).resolve().parents[1]


class BacklogPublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = isolated_project()
        self.root = self.temp.__enter__()
        self.addCleanup(self.temp.__exit__, None, None, None)
        for relative in ('schemas', 'backlog', 'decisions', 'revisions', 'provenance', 'release/2026-09-13.2'):
            shutil.copytree(ROOT / 'modeles' / relative, self.root / 'modeles' / relative)
        shutil.copyfile(ROOT / 'modeles/release/current.json', self.root / 'modeles/release/current.json')
        self.version = '2026-09-13.99'
        self.models = self.root / 'modeles'
        self.backlog_path = self.models / 'backlog/model.json'
        path = self.models / 'provenance/source-records.json'
        live = workflow.read(path)
        live['records'].append(source('PUB-TEST-NEW', 'Explicit local publication request'))
        save(path, live)

    def mutate_capability(self, revision=True):
        model = workflow.read(self.backlog_path)
        cap = next(n for n in model['nodes'] if n['id'] == 'D03.a')
        cap['fields']['definition'] += ' New proposed precision.'
        if revision:
            cap['revision'] += 1
        save(self.backlog_path, model)
        return cap

    def prepare(self):
        return workflow.prepare(self.root, self.version, ['PUB-TEST-NEW'])

    def test_read_only_report_identifies_live_changed_field_and_lost_validation(self):
        self.mutate_capability()
        before = (self.models / 'release/current.json').read_bytes()
        bundle = workflow.build_candidate(self.root, self.version)
        report = bundle['report']
        change = next(n for n in report['changes']['nodes']['modified'] if n['id'] == 'D03.a')
        self.assertIn('/fields/definition', {c['path'] for c in change['changes']})
        released = next(n for n in bundle['candidate']['nodes'] if n['id'] == 'D03.a')
        self.assertEqual(released['approved_fields'], [])
        self.assertEqual(released['review']['state'], 'proposed')
        self.assertTrue(released['review']['note'].startswith('Aucune validation antérieure reprise pour cette révision'))
        self.assertIn('Note antérieure, qui ne qualifie pas cette révision', released['review']['note'])
        original_note = next(n for n in workflow.read(self.backlog_path)['nodes'] if n['id'] == 'D03.a')['review']['note']
        self.assertIn(original_note, released['review']['note'])
        self.assertTrue(any(d['target'] == 'D03.a' for d in report['deferred_decisions']))
        self.assertEqual((self.models / 'release/current.json').read_bytes(), before)
        self.assertFalse((self.models / 'staging').exists())

    def test_changed_value_without_revision_is_reported_and_cannot_be_prepared(self):
        self.mutate_capability(revision=False)
        report = workflow.build_candidate(self.root, self.version)['report']
        self.assertTrue(any('new revision' in e for e in report['validation_errors']))
        with self.assertRaisesRegex(ValueError, 'new revision'):
            self.prepare()
        self.assertFalse((self.models / 'staging').exists())

    def test_prepare_freezes_current_backlog_without_changing_release(self):
        self.mutate_capability()
        pointer = (self.models / 'release/current.json').read_bytes()
        result = self.prepare()
        self.assertFalse(result['release_activated'])
        self.assertEqual((self.models / 'release/current.json').read_bytes(), pointer)
        self.assertFalse((self.models / 'release' / self.version).exists())
        candidate = workflow.read(self.models / 'staging' / self.version / 'candidate.json')
        cap = next(n for n in candidate['nodes'] if n['id'] == 'D03.a')
        self.assertIn('New proposed precision.', cap['fields']['definition'])
        self.assertEqual(sum(n['kind'] == 'capability' for n in candidate['nodes']), 36)
        self.assertTrue((self.models / 'staging' / self.version / 'deferred/applicability.json').exists())

    def test_publish_prepared_activates_verified_live_backlog_and_preserves_old_release(self):
        self.mutate_capability()
        old_path = self.models / 'release/2026-09-13.2/model.json'
        old_bytes = old_path.read_bytes()
        self.prepare()
        result = workflow.publish_prepared(self.root, self.version, activate=True)
        self.assertEqual(result['complete_capability_count'], 8)
        self.assertEqual(workflow.read(self.models / 'release/current.json')['version'], self.version)
        self.assertEqual(old_path.read_bytes(), old_bytes)
        self.assertTrue((self.models / f'revisions/{self.version}/backlog.json').exists())
        self.assertTrue((self.models / f'decisions/{self.version}.json').exists())
        # The resulting current release is valid for another report/preparation.
        bundle = workflow.build_candidate(self.root, '2026-09-13.100')
        self.assertFalse(bundle['report']['validation_errors'])
        published_cap = next(n for n in workflow.read(self.models / f'release/{self.version}/model.json')['nodes'] if n['id'] == 'D03.a')
        next_cap = next(n for n in bundle['candidate']['nodes'] if n['id'] == 'D03.a')
        self.assertEqual(next_cap['review']['note'], published_cap['review']['note'])
        self.assertTrue(next_cap['review']['note'].startswith('Aucune validation antérieure reprise pour cette révision'))

    def test_stale_live_backlog_refuses_publication(self):
        self.prepare()
        self.mutate_capability()
        with self.assertRaisesRegex(ValueError, 'Backlog changed'):
            workflow.publish_prepared(self.root, self.version, activate=True)
        self.assertFalse((self.models / 'release' / self.version).exists())

    def test_modified_staged_candidate_is_rejected(self):
        self.prepare()
        path = self.models / 'staging' / self.version / 'candidate.json'
        path.write_text(path.read_text(encoding='utf-8') + ' ', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            workflow.publish_prepared(self.root, self.version)
        self.assertFalse((self.models / 'release' / self.version).exists())

    def test_changed_backlog_context_refuses_publication(self):
        self.prepare()
        path = self.models / 'backlog/modeling-roadmap.json'
        doc = workflow.read(path)
        doc['current_focus'] = ['domain']
        save(path, doc)
        with self.assertRaisesRegex(ValueError, 'context changed'):
            workflow.publish_prepared(self.root, self.version)

    def test_additional_explicit_decision_can_validate_changed_revision(self):
        cap = self.mutate_capability()
        doc = {'schema_version': '1.0.0', 'version': self.version, 'decisions': [{
            'id': 'ADOPT-TEST-NEW', 'decision_state': 'accepted', 'author': 'Laurent',
            'decided_at': '2026-09-13', 'recorded_at': '2026-09-13', 'interpretation': 'explicit',
            'source_refs': ['PUB-TEST-NEW'], 'note': 'Test only: explicit scoped approval.',
            'target': {'collection': 'nodes', 'id': cap['id'], 'revision': cap['revision'],
                       'approved_fields': list(cap['fields']), 'value_sha256': {k: workflow.canonical_sha256(v) for k, v in cap['fields'].items()},
                       'import_version': self.version}}]}
        path = self.root / 'new-decisions.json'
        save(path, doc)
        bundle = workflow.build_candidate(self.root, self.version, ['PUB-TEST-NEW'], path)
        released = next(n for n in bundle['candidate']['nodes'] if n['id'] == cap['id'])
        self.assertEqual(released['review']['state'], 'accepted')
        self.assertEqual(released['adoption_ids'], ['ADOPT-TEST-NEW'])
        self.assertTrue(released['review']['note'].startswith('Seules les décisions applicables à cette version'))
        self.assertEqual(bundle['report']['new_decision_ids'], ['ADOPT-TEST-NEW'])
        self.assertFalse(bundle['report']['validation_errors'])

    def test_lost_validation_note_remains_historical_after_new_partial_approval(self):
        cap = self.mutate_capability()
        snapshot = workflow.read(self.backlog_path)
        decision = {'id': 'ADOPT-TEST-PARTIAL', 'decision_state': 'accepted',
                    'target': {'collection': 'nodes', 'id': cap['id']}}
        workflow.explain_deferred_validations(snapshot, {'decisions': [decision]},
                                             [{'id': 'OLD-APPROVAL', 'target': cap['id']}])
        changed = next(n for n in snapshot['nodes'] if n['id'] == cap['id'])
        self.assertTrue(changed['review']['note'].startswith('Seules les décisions applicables à cette version'))
        self.assertIn('OLD-APPROVAL', changed['review']['note'])
        self.assertIn('Note antérieure, qui ne qualifie pas cette révision', changed['review']['note'])

    def test_relation_qualification_diff_and_new_relation_are_explicit(self):
        model = workflow.read(self.backlog_path)
        relation = {'id': 'REL-TEST', 'revision': 1, 'type': 'relates-to', 'source_id': 'D03.a', 'target_id': 'D03.b',
                    'source_refs': ['PUB-TEST-NEW'], 'review': {'state': 'proposed', 'note': 'Test hypothesis'},
                    'qualification': {'meaning': 'Test relation', 'conditions': [], 'effects': []}}
        model['relations'].append(relation)
        save(self.backlog_path, model)
        report = workflow.build_candidate(self.root, self.version)['report']
        added = report['changes']['relations']['added']
        self.assertEqual(added[0]['qualification']['meaning'], 'Test relation')
        after = deepcopy(added[0])
        after['qualification']['meaning'] = 'Changed meaning'
        delta = workflow.model_diff({'nodes': [], 'relations': added}, {'nodes': [], 'relations': [after]})
        self.assertEqual(delta['relations']['modified'][0]['changes'][0]['path'], '/qualification/meaning')

    def test_deletions_and_status_changes_are_reported(self):
        before = {'nodes': [{'id': 'A', 'review': {'state': 'proposed'}}, {'id': 'B'}], 'relations': [{'id': 'R'}]}
        after = {'nodes': [{'id': 'A', 'review': {'state': 'under_review'}}], 'relations': []}
        report = workflow.model_diff(before, after)
        self.assertEqual(report['nodes']['removed'], [{'id': 'B'}])
        self.assertEqual(report['relations']['removed'], [{'id': 'R'}])
        self.assertEqual(report['nodes']['modified'][0]['changes'][0]['path'], '/review/state')

    def test_version_collision_refuses_to_rewrite_stage(self):
        self.prepare()
        manifest_path = self.models / 'staging' / self.version / 'manifest.json'
        before = manifest_path.read_bytes()
        with self.assertRaisesRegex(ValueError, 'already exists'):
            self.prepare()
        self.assertEqual(manifest_path.read_bytes(), before)

    def test_malformed_new_decision_or_unknown_source_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Unknown publication source'):
            workflow.prepare(self.root, self.version, ['ABSENT'])
        bundle = workflow.build_candidate(self.root, self.version)
        doc = deepcopy(bundle['decisions'])
        doc['decisions'] = [doc['decisions'][0]]
        path = self.root / 'reused-decision.json'
        save(path, doc)
        with self.assertRaisesRegex(ValueError, 'new id'):
            workflow.build_candidate(self.root, self.version, ['PUB-TEST-NEW'], path)


if __name__ == '__main__':
    unittest.main()

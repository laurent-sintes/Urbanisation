"""Release orchestration and guide checks; all publications use disposable fixtures."""
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch
import unittest

from scripts import prepare_release as workflow
from scripts import release
from scripts import test_prepare_release as fixtures
from scripts.test_publish_release import save
from scripts.record_decision import record_intent


class ReleaseRunTests(unittest.TestCase):
    setUpClass = classmethod(fixtures.BacklogPublicationTests.setUpClass.__func__)
    setUp = fixtures.BacklogPublicationTests.setUp
    mutate_capability = fixtures.BacklogPublicationTests.mutate_capability

    def editorial_change(self):
        model = workflow.read(self.backlog_path)
        node = next(n for n in model['nodes'] if n['id'] == 'D03.a')
        node['review']['note'] += ' Editorial clarification for this isolated test.'
        save(self.backlog_path, model)

    def test_final_checks_use_the_real_validator_contract(self):
        with patch.object(release.render_models, 'write_text_if_changed') as write:
            result = release.final_checks(fixtures.ROOT)
        self.assertEqual(result['validation_errors'], 0)
        self.assertGreater(result['counters']['release_capability_count'], 0)
        write.assert_called_once()

    def test_final_checks_surface_validation_errors_without_rendering(self):
        with patch.object(release, 'validate_project', return_value={
                'errors': ['broken publication hash'], 'counters': {}}), \
             patch.object(release.render_models, 'write_text_if_changed') as write:
            with self.assertRaisesRegex(ValueError, 'broken publication hash'):
                release.final_checks(self.root)
        write.assert_not_called()

    def test_editorial_run_builds_once_and_stops_at_preparation_by_default(self):
        self.editorial_change()
        before = (self.models / 'release/index.json').read_bytes()
        with patch.object(workflow, 'build_candidate', wraps=workflow.build_candidate) as builds:
            result = release.run(self.root, self.version, ['PUB-TEST-NEW'])
        self.assertEqual(result['status'], 'prepared', result)
        self.assertEqual(builds.call_count, 1)
        self.assertEqual((self.models / 'release/index.json').read_bytes(), before)
        self.assertGreater(result['summary']['automatically_carried_decisions'], 0)

    def test_semantic_change_returns_review_without_publication(self):
        self.mutate_capability()
        before = (self.models / 'release/index.json').read_bytes()
        result = release.run(self.root, self.version, ['PUB-TEST-NEW'], activate=True)
        self.assertEqual(result['status'], 'needs_review')
        assessment = workflow.read(Path(result['assessment']))
        self.assertTrue(all(i['action'] == 'pending' for i in assessment['items']))
        self.assertEqual((self.models / 'release/index.json').read_bytes(), before)
        self.assertFalse((self.models / 'staging' / self.version).exists())

    def test_resume_publication_checks_without_republishing(self):
        self.editorial_change()
        (self.root / 'JOURNAL.md').write_text('# Journal\n', encoding='utf-8')
        with patch.object(release, 'final_checks', return_value={'validation_errors': 0}), \
             patch.object(release, 'verify_atlas', return_value={'verified': True}), \
             patch.object(workflow, 'publish_prepared', wraps=workflow.publish_prepared) as publish:
            first = release.run(self.root, self.version, ['PUB-TEST-NEW'], activate=True)
            second = release.run(self.root, self.version, ['PUB-TEST-NEW'], activate=True)
        self.assertEqual(first['status'], 'published', first)
        self.assertEqual(second['status'], 'published', second)
        self.assertTrue(second['already_published'])
        self.assertEqual(publish.call_count, 1)
        self.assertEqual((self.root / 'JOURNAL.md').read_text().count('release-run:'), 1)
        with self.assertRaisesRegex(ValueError, 'Published version is frozen'):
            release.run(self.root, self.version, ['PUB-TEST-NEW'], activate=True, guide_path=self.root / 'new-guide.yaml')

    def test_published_site_failure_is_reported_without_claiming_availability(self):
        self.editorial_change()
        with patch.object(release, 'final_checks', return_value={'validation_errors': 0}), \
             patch.object(release, 'verify_atlas', side_effect=OSError('offline')):
            result = release.run(self.root, self.version, ['PUB-TEST-NEW'], activate=True)
        self.assertEqual(result['status'], 'published_checks_failed')
        self.assertTrue(result['release_activated'])
        self.assertFalse(result['atlas']['verified'])
        self.assertEqual(workflow.resolve_release(self.models / 'release')['version'], self.version)

    def test_staged_resume_keeps_integrity_checks(self):
        self.editorial_change()
        prepared = release.run(self.root, self.version, ['PUB-TEST-NEW'])
        self.assertEqual(prepared['status'], 'prepared')
        self.mutate_capability()
        with self.assertRaisesRegex(ValueError, 'Backlog changed'):
            release.run(self.root, self.version, ['PUB-TEST-NEW'], activate=True)
        self.assertFalse((self.models / 'release' / self.version).exists())

    def guide(self):
        guide = deepcopy(workflow.read(fixtures.ROOT / 'modeles/modeling-guides/versions/2026-09-19.4.yaml'))
        guide['version'] = '2099-09-13.1'
        path = self.root / 'guide-candidate.yaml'
        save(path, guide)
        return path

    def test_new_guide_is_frozen_and_associated_before_activation(self):
        path = self.guide()
        self.editorial_change()
        workflow.prepare(self.root, self.version, ['PUB-TEST-NEW'], guide_path=path)
        staged = workflow.read(self.models / 'staging' / self.version / 'manifest.json')
        self.assertEqual(staged['new_modeling_guide']['version'], '2099-09-13.1')
        workflow.publish_prepared(self.root, self.version, activate=True)
        index = workflow.read(self.models / 'modeling-guides/index.yaml')
        self.assertEqual(index['associations'][0]['publication_version'], self.version)
        self.assertEqual((self.models / 'modeling-guides/versions/2099-09-13.1.yaml').read_bytes(), path.read_bytes())

    def test_guide_tamper_refuses_before_writing_any_publication(self):
        path = self.guide()
        workflow.prepare(self.root, self.version, ['PUB-TEST-NEW'], guide_path=path)
        path.write_bytes(path.read_bytes() + b'\n')
        with self.assertRaisesRegex(ValueError, 'Guide candidate changed'):
            workflow.publish_prepared(self.root, self.version, activate=True)
        self.assertFalse((self.models / 'release' / self.version).exists())

    def test_in_memory_candidate_cannot_bypass_fresh_input_check(self):
        bundle = workflow.build_candidate(self.root, self.version, ['PUB-TEST-NEW'])
        self.mutate_capability()
        with self.assertRaisesRegex(ValueError, 'Inputs changed'):
            workflow.stage_candidate(self.root, bundle)
        self.assertFalse((self.models / 'staging' / self.version).exists())

    def test_atlas_verification_rejects_nonlocal_service_before_network(self):
        with patch.object(release, 'urlopen') as network:
            with self.assertRaisesRegex(ValueError, 'local HTTP'):
                release.verify_atlas(self.root, self.version, 'https://example.com')
        network.assert_not_called()

    def test_new_approval_without_business_edit_is_not_discarded_as_unchanged(self):
        self.editorial_change()
        with patch.object(release, 'final_checks', return_value={'validation_errors': 0}):
            first = release.run(self.root, self.version, ['PUB-TEST-NEW'], activate=True, verify_site=False)
        self.assertEqual(first['status'], 'published', first)
        record_intent(self.root, intent_id='ADOPT-RECORDED-ONLY', collection='nodes', target_id='D03.a',
            fields=['name'], source_refs=['PUB-TEST-NEW'], author='Laurent', decided_at='2026-09-19',
            interpretation='explicit', note='Explicit fixture agreement only.', reviewer='Test')
        result = release.run(self.root, '2099-09-13.100', ['PUB-TEST-NEW'], verify_site=False)
        self.assertEqual(result['status'], 'prepared', result)
        self.assertIn('ADOPT-RECORDED-ONLY', workflow.read(self.models / 'staging/2099-09-13.100/report.json')['new_decision_ids'])
        workflow.publish_prepared(self.root, '2099-09-13.100', activate=True)
        (self.models / 'backlog/decision-intents.yaml').unlink()
        removed = workflow.build_candidate(self.root, '2099-09-13.101', ['PUB-TEST-NEW'])
        self.assertTrue(any('previously published registry was removed' in e for e in removed['report']['validation_errors']))

    def test_wrong_additional_version_is_not_hidden_by_intent_registry(self):
        record_intent(self.root, intent_id='ADOPT-RECORDED-VERSION', collection='nodes', target_id='D03.a',
            fields=['name'], source_refs=['PUB-TEST-NEW'], author='Laurent', decided_at='2026-09-19',
            interpretation='explicit', note='Explicit fixture agreement only.', reviewer='Test')
        additional = self.root / 'additional.json'
        save(additional, {'schema_version': '1.0.0', 'version': '2099-09-13.3', 'decisions': []})
        with self.assertRaisesRegex(ValueError, 'prepared version'):
            workflow.build_candidate(self.root, self.version, ['PUB-TEST-NEW'], additional)

    def test_partial_write_is_reported_and_never_blindly_retried(self):
        self.editorial_change()
        def partial(*args, **kwargs):
            (self.models / 'release' / self.version).mkdir()
            raise OSError('simulated interruption')
        with patch.object(workflow, 'publish_prepared', side_effect=partial) as publish:
            first = release.run(self.root, self.version, ['PUB-TEST-NEW'], activate=True)
            second = release.run(self.root, self.version, ['PUB-TEST-NEW'], activate=True)
        self.assertEqual(first['status'], 'publication_incomplete')
        self.assertEqual(second['status'], 'publication_incomplete')
        self.assertEqual(publish.call_count, 1)
        self.assertNotEqual(workflow.resolve_release(self.models / 'release')['version'], self.version)


if __name__ == '__main__':
    unittest.main()

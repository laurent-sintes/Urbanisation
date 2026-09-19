"""Partial reassessment preserves the original approval and excludes changed values."""
from copy import deepcopy
import unittest

from scripts import decision_review as review
from scripts.structured_io import read
from scripts.test_decision_carry import fixture
from scripts.test_publish_release import isolated_project, save as write
from scripts.validate_models import canonical_sha256


class PartialDecisionReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = isolated_project()
        self.folder = self.temp.__enter__() / 'review'
        self.addCleanup(self.temp.__exit__, None, None, None)
        self.decision, self.before = fixture()
        self.decision.update(author='Laurent', decided_at='2026-09-19', recorded_at='2026-09-19',
                             source_refs=['U-ORIGINAL'], interpretation='explicit', note='Original scope.')
        self.decision['target']['import_version'] = 'before'
        self.after = deepcopy(self.before)
        self.after['version'] = '2026-09-20.1'
        self.after['nodes'][2]['revision'] = 2
        self.after['nodes'][2]['fields']['name'] = 'Changed name'

    def dossier(self, reason='approved_value_changed'):
        self.current = review.make_review(
            self.after, self.before, self.before, {'decisions': [self.decision]},
            [{'id': self.decision['id'], 'reason': reason}], {'version': 'before'},
            'manifest', {}, ['PUB'], lambda before, after: [] if before == after else [{'changed': True}],
        )
        review.save_review(self.folder, self.current, {})
        return self.current['items'][0]

    def assess(self, action='retain_partial', fields=('definition',)):
        assessment = read(self.folder / 'assessment.yaml')
        assessment['reviewer'] = 'Reviewer'
        assessment['items'][0].update(action=action, rationale='Definition and its meaning remain unchanged.')
        if action == 'retain_partial':
            assessment['items'][0]['approved_fields'] = list(fields) if fields is not None else None
        write(self.folder / 'assessment.yaml', assessment)
        return assessment

    def test_partial_reassessment_preserves_authority_and_only_unchanged_scope(self):
        item = self.dossier()
        self.assertEqual(item['unchanged_fields'], ['definition'])
        self.assertEqual(item['changed_fields'], ['name'])
        self.assertFalse(item['eligible_for_reassessment'])
        self.assertTrue(item['eligible_for_partial_reassessment'])
        self.assess()
        decisions, evidence = review.apply_assessment(self.folder, self.current)
        decision = decisions['decisions'][0]
        for field in ('author', 'decided_at', 'interpretation', 'decision_state', 'source_refs'):
            self.assertEqual(decision[field], self.decision[field])
        self.assertEqual(decision['target']['approved_fields'], ['definition'])
        self.assertEqual(decision['target']['value_sha256'], {'definition': self.decision['target']['value_sha256']['definition']})
        self.assertEqual(decision['target']['revision'], 2)
        self.assertNotEqual(decision['id'], self.decision['id'])
        self.assertEqual(evidence['transcriptions.json']['items'][0]['approved_fields'], ['definition'])
        self.assertEqual(self.decision['target']['approved_fields'], ['name', 'definition'])

    def test_partial_selection_must_be_explicit_unique_and_unchanged(self):
        self.dossier()
        for fields in ((), ('name',), ('definition', 'name'), ('definition', 'definition'), ('unknown',), None):
            with self.subTest(fields=fields):
                self.assess(fields=fields)
                with self.assertRaisesRegex(ValueError, 'explicit nonempty unchanged scope'):
                    review.apply_assessment(self.folder, self.current)
        assessment = self.assess()
        assessment['items'][0].pop('approved_fields')
        write(self.folder / 'assessment.yaml', assessment)
        with self.assertRaises(ValueError):
            review.apply_assessment(self.folder, self.current)

    def test_full_retain_still_rejects_changed_composite_approval(self):
        self.dossier()
        self.assess(action='retain')
        with self.assertRaisesRegex(ValueError, 'cannot be transcribed'):
            review.apply_assessment(self.folder, self.current)

    def test_legacy_assessment_shape_and_full_scope_remain_compatible(self):
        self.after['nodes'][2]['fields']['name'] = self.before['nodes'][2]['fields']['name']
        self.dossier(reason='revision_changed_requires_explicit_reassessment')
        # Archived review shape before partial reassessment existed.
        for key in ('unchanged_fields', 'changed_fields', 'eligible_for_partial_reassessment'):
            self.current['items'][0].pop(key)
        write(self.folder / 'review.json', self.current)
        assessment = self.assess(action='retain')
        assessment['review_sha256'] = canonical_sha256(self.current)
        write(self.folder / 'assessment.yaml', assessment)
        decisions, _ = review.apply_assessment(self.folder, self.current)
        self.assertEqual(decisions['decisions'][0]['target']['approved_fields'], ['name', 'definition'])

    def test_context_only_change_can_be_reassessed_even_without_target_revision_change(self):
        self.after = deepcopy(self.before)
        self.after['version'] = '2026-09-20.1'
        self.after['nodes'][3]['fields']['scope'] = 'Different neighbor context'
        item = self.dossier(reason='context_changed_requires_explicit_reassessment')
        self.assertTrue(item['eligible_for_reassessment'])
        self.assertTrue(item['eligible_for_partial_reassessment'])
        self.assess(action='retain')
        decisions, _ = review.apply_assessment(self.folder, self.current)
        self.assertEqual(decisions['decisions'][0]['target']['revision'], 1)

    def test_forged_dossier_is_rejected_even_with_updated_assessment_hash(self):
        self.dossier()
        assessment = self.assess()
        altered = deepcopy(self.current)
        altered['items'][0]['unchanged_fields'].append('name')
        write(self.folder / 'review.json', altered)
        assessment['review_sha256'] = canonical_sha256(altered)
        write(self.folder / 'assessment.yaml', assessment)
        with self.assertRaisesRegex(ValueError, 'stale or altered'):
            review.apply_assessment(self.folder, self.current)

    def test_partial_cannot_trust_a_forged_unchanged_flag(self):
        self.dossier()
        self.current['items'][0]['unchanged_fields'].append('name')
        write(self.folder / 'review.json', self.current)
        assessment = self.assess(fields=('name',))
        assessment['review_sha256'] = canonical_sha256(self.current)
        write(self.folder / 'assessment.yaml', assessment)
        with self.assertRaisesRegex(ValueError, 'explicit nonempty unchanged scope'):
            review.apply_assessment(self.folder, self.current)


if __name__ == '__main__':
    unittest.main()

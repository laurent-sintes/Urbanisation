"""Conservative context boundaries for automatic decision transcription."""
from copy import deepcopy
import unittest

from scripts.decision_carry import classify_context
from scripts.validate_models import canonical_sha256


def fixture():
    snapshot = {
        'version': 'before', 'principles': [{'id': 'P', 'text': 'Keep commitments explicit.'}],
        'nodes': [
            {'id': 'root', 'kind': 'domain', 'revision': 1, 'fields': {'name': 'Supply'}},
            {'id': 'area', 'kind': 'area', 'revision': 1, 'fields': {'name': 'Requests'}},
            {'id': 'cap', 'kind': 'capability', 'revision': 1,
             'fields': {'name': 'Request', 'definition': 'Handle [requests](glossary:T1).', 'scope': 'An explicit need.'}},
            {'id': 'peer', 'kind': 'capability', 'revision': 1, 'fields': {'name': 'Planning', 'definition': 'Compare plans.'}},
        ],
        'relations': [
            {'id': 'root-area', 'type': 'presents', 'source_id': 'root', 'target_id': 'area'},
            {'id': 'area-cap', 'type': 'contains', 'source_id': 'area', 'target_id': 'cap'},
            {'id': 'cap-peer', 'type': 'relates-to', 'source_id': 'cap', 'target_id': 'peer',
             'qualification': {'meaning': 'Uses plans.'}, 'fields': {'label': 'Needs planning'}},
        ],
        'glossary': {'version': 'before', 'terms': [
            {'id': 'T1', 'name': 'Request', 'definition': 'An [objective](glossary:T2).'},
            {'id': 'T2', 'name': 'Objective', 'definition': 'An expected result.'},
            {'id': 'OTHER', 'name': 'Unrelated', 'definition': 'Other topic.'},
        ]},
    }
    fields = snapshot['nodes'][2]['fields']
    decision = {
        'id': 'ADOPT-TEST', 'decision_state': 'accepted', 'author': 'Laurent',
        'target': {'collection': 'nodes', 'id': 'cap', 'revision': 1, 'approved_fields': ['name', 'definition'],
                   'value_sha256': {field: canonical_sha256(fields[field]) for field in ('name', 'definition')}},
    }
    return decision, snapshot


class DecisionCarryTests(unittest.TestCase):
    def setUp(self):
        self.decision, self.before = fixture()
        self.after = deepcopy(self.before)
        self.after['version'] = 'after'
        self.after['nodes'][2]['revision'] = 2

    def classify(self):
        return classify_context(self.decision, self.before, self.after)

    def test_known_editorial_metadata_and_market_changes_are_safe(self):
        cap = self.after['nodes'][2]
        cap.update(source_refs=['NEW-SOURCE'], review={'state': 'partial'}, editorial_basis='Editorial clarification',
                   lifecycle={'state': 'urbanist_validated'}, last_modified='new')
        cap['fields']['market_comparisons'] = [{'source_url': 'https://example.test/new'}]
        cap['fields']['market_inspiration'] = {'choice': 'Explain the documented comparison.'}
        self.after['relations'][2]['qualification']['source_refs'] = ['NEW-SOURCE']
        self.after['principles'][0]['review'] = {'state': 'partial'}
        self.after['glossary']['terms'][1]['market_comparisons'] = [{'source_url': 'https://example.test/new'}]
        untouched = deepcopy((self.decision, self.before, self.after))
        self.assertTrue(self.classify()['safe'])
        self.assertEqual((self.decision, self.before, self.after), untouched)

    def test_all_business_and_unknown_fields_remain_significant(self):
        for field in ('name', 'definition', 'scope', 'nature', 'request_origins', 'behavior_aspect', 'new_unknown_field'):
            with self.subTest(field=field):
                self.after = deepcopy(self.before)
                self.after['nodes'][2]['fields'][field] = 'Changed'
                self.assertFalse(self.classify()['safe'])
        self.after = deepcopy(self.before)
        self.after['nodes'][2]['unknown_context'] = 'Changed'
        self.assertFalse(self.classify()['safe'])

    def test_parent_and_ancestor_moves_require_review(self):
        self.after['relations'][1]['source_id'] = 'root'
        self.assertIn('incident_or_membership_relation_changed', self.classify()['reasons'])
        self.after = deepcopy(self.before)
        self.after['nodes'].append({'id': 'new-root', 'kind': 'domain', 'fields': {'name': 'Other'}})
        self.after['relations'][0]['source_id'] = 'new-root'
        self.assertFalse(self.classify()['safe'])

    def test_neighbor_and_ancestor_semantics_require_review(self):
        for index in (0, 1, 3):
            with self.subTest(index=index):
                self.after = deepcopy(self.before)
                self.after['nodes'][index]['fields']['scope'] = 'Different business responsibility'
                self.assertIn('neighbor_or_ancestor_business_changed', self.classify()['reasons'])

    def test_relation_qualifications_and_labels_are_business_content(self):
        self.after['relations'][2]['qualification']['meaning'] = 'Replaces plans.'
        self.assertFalse(self.classify()['safe'])
        self.after = deepcopy(self.before)
        self.after['relations'][2]['fields']['label'] = 'Overrides planning'
        self.assertFalse(self.classify()['safe'])

    def test_principles_and_transitively_referenced_terms_require_review(self):
        self.after['principles'][0]['text'] = 'Automatically override commitments.'
        self.assertIn('principles_changed', self.classify()['reasons'])
        self.after = deepcopy(self.before)
        self.after['glossary']['terms'][1]['definition'] = 'A different meaning.'
        self.assertIn('referenced_glossary_changed', self.classify()['reasons'])

    def test_unrelated_node_and_term_changes_do_not_expand_context(self):
        self.after['nodes'].append({'id': 'unrelated', 'kind': 'capability', 'fields': {'name': 'Other'}})
        self.after['glossary']['terms'][2]['definition'] = 'New unrelated topic.'
        self.assertTrue(self.classify()['safe'])

    def test_first_glossary_without_references_does_not_suspend_approval(self):
        self.before['nodes'][2]['fields']['definition'] = 'Handle requests.'
        self.decision['target']['value_sha256']['definition'] = canonical_sha256('Handle requests.')
        self.after = deepcopy(self.before)
        self.before.pop('glossary')
        self.after['glossary']['definition'] = 'New catalogue unrelated to this approval.'
        self.assertTrue(self.classify()['safe'])
        self.decision, self.before = fixture()
        self.after = deepcopy(self.before)
        self.after['glossary']['definition'] = 'New catalogue context affecting referenced terms.'
        self.assertIn('glossary_context_changed', self.classify()['reasons'])

    def test_unknown_global_context_requires_review(self):
        self.after['unknown_policy'] = 'Never implicitly ignored'
        self.assertIn('global_business_context_changed', self.classify()['reasons'])

    def test_approved_market_values_are_never_carried_when_changed(self):
        self.before['nodes'][2]['fields']['market_comparisons'] = ['before']
        self.after = deepcopy(self.before)
        self.after['nodes'][2]['fields']['market_comparisons'] = ['after']
        target = self.decision['target']
        target['approved_fields'].append('market_comparisons')
        target['value_sha256']['market_comparisons'] = canonical_sha256(['before'])
        self.assertIn('approved_values_changed_or_unverified', self.classify()['reasons'])

    def test_unverified_previous_values_and_missing_context_fail_closed(self):
        self.decision['target']['value_sha256']['name'] = canonical_sha256('Forged')
        self.assertFalse(self.classify()['safe'])
        self.decision, self.before = fixture()
        self.after = deepcopy(self.before)
        self.after['nodes'].pop()
        self.assertFalse(self.classify()['safe'])
        self.after = deepcopy(self.before)
        self.after['glossary']['terms'].pop(1)
        self.assertFalse(self.classify()['safe'])

    def test_relation_decision_checks_both_endpoint_contexts(self):
        relation = self.before['relations'][2]
        relation['revision'] = 1
        self.after = deepcopy(self.before)
        self.decision['target'] = {'collection': 'relations', 'id': relation['id'], 'revision': 1,
                                   'approved_fields': ['type', 'source_id', 'target_id'],
                                   'value_sha256': {field: canonical_sha256(relation[field])
                                                    for field in ('type', 'source_id', 'target_id')}}
        self.assertTrue(self.classify()['safe'])
        self.after['nodes'][3]['fields']['scope'] = 'Changed'
        self.assertFalse(self.classify()['safe'])


if __name__ == '__main__':
    unittest.main()

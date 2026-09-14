"""Terminology integrity and publication isolation; never publish the live project."""
from copy import deepcopy
import unittest
from scripts.glossary import validate, references, reference_impacts
from scripts.element_versions import assign_versions


def catalog():
    return {'id': 'glossary', 'terms': [{'id': 'TER1', 'name': 'Product',
            'short_description': 'Reference.', 'definition': 'Definition.',
            'review': {'state': 'proposed'}, 'source_refs': []}]}


class GlossaryTests(unittest.TestCase):
    def model(self):
        return {'model_id': 'test', 'nodes': [{'id': 'D01', 'fields': {'definition':
                'The [reference](glossary:TER1) in [Inventory](model:D01#definition).'}}],
                'relations': [], 'glossary': catalog()}

    def test_explicit_links_only_and_missing_targets(self):
        model = self.model()
        self.assertEqual(validate(model), [])
        self.assertEqual(list(references(r'\[literal](glossary:missing) [web](https://example.com) Product')), [])
        model['nodes'][0]['fields']['definition'] += ' [missing](glossary:TER0)'
        self.assertIn('glossary: unresolved published link TER0', validate(model))
        model['nodes'][0]['fields']['definition'] = '[wrong](glossary:TER1#missing)'
        self.assertIn('glossary: unresolved section TER1#missing', validate(model))

    def test_duplicate_and_malformed_ids_return_errors(self):
        model = self.model()
        model['glossary']['terms'].append(deepcopy(model['glossary']['terms'][0]))
        self.assertTrue(validate(model))
        model['glossary']['terms'][1]['id'] = []
        self.assertTrue(validate(model))

    def test_term_change_flags_unchanged_linked_statements(self):
        before = self.model()
        after = deepcopy(before)
        after['glossary']['terms'][0]['definition'] += ' Revised.'
        result = reference_impacts(before, after)
        self.assertEqual(result[0]['id'], 'D01')
        self.assertEqual(result[0]['changed_terms'], ['TER1'])
        self.assertEqual(reference_impacts(before, before), [])

    def test_version_and_time_track_definition_not_serialization(self):
        first = self.model()
        assign_versions(first, {}, now='2026-09-14T10:00:00Z')
        stable = self.model()
        assign_versions(stable, first, now='2026-09-14T11:00:00Z')
        self.assertEqual(stable['glossary'], first['glossary'])
        self.assertEqual(stable['revision'], first['revision'])
        changed = self.model()
        changed['glossary']['terms'][0]['definition'] += ' Precision.'
        assign_versions(changed, stable, now='2026-09-14T12:00:00Z')
        self.assertEqual(changed['revision'], first['revision'] + 1)
        self.assertEqual(changed['nodes'], stable['nodes'])
        self.assertEqual(changed['glossary']['terms'][0]['revision'], 2)
        self.assertEqual(changed['glossary']['terms'][0]['last_modified'], '2026-09-14T12:00:00Z')


if __name__ == '__main__':
    unittest.main()

"""Data governance is optional, explicit and independent of capability nature."""
from copy import deepcopy
import unittest
from scripts.test_request_metadata import model, node, ROOT
from scripts.structured_io import read
from scripts.json_contract import validate
from scripts.validate_models import validate_urbanism
from scripts.publish_release import compile_snapshot
from scripts.render_models import render


class DataGovernanceTests(unittest.TestCase):
    def test_each_governance_preserves_type_and_publication_scope(self):
        for governance in ('Domain-managed', 'Projection', 'Domain-View'):
            current = model()
            current['nodes'][1]['fields']['data_governance'] = governance
            original = deepcopy(current)
            self.assertEqual(validate_urbanism(current, {}), [])
            published = compile_snapshot(current, {'decisions': []}, '2026-09-22.99', ['U615'])
            self.assertEqual(current, original)
            self.assertEqual(published['nodes'][1]['fields']['nature'], 'action')
            self.assertEqual(published['nodes'][1]['fields']['data_governance'], governance)
            self.assertIn('data_governance', published['nodes'][1]['proposed_fields'])
            self.assertNotIn('data_governance', published['nodes'][0]['fields'])

    def test_unknown_values_and_wrong_levels_are_rejected(self):
        schema = read(ROOT/'modeles/schemas/urbanism.schema.json')
        for value in ('policy', '', None, ['Projection']):
            current = model()
            current['nodes'][1]['fields']['data_governance'] = value
            self.assertTrue(validate(current['nodes'][1], {'$ref': '#/$defs/node', '$defs': schema['$defs']}))
            self.assertTrue(any('data_governance' in e for e in validate_urbanism(current, {})))
        current = model()
        current['nodes'][0]['fields']['data_governance'] = 'Projection'
        self.assertTrue(any('belongs to' in e for e in validate_urbanism(current, {})))

    def test_reference_and_view_have_distinct_governance_in_rendering(self):
        current = model()
        current['nodes'][0]['kind'] = 'reference'
        current['nodes'][0]['fields']['data_governance'] = 'Projection'
        current['nodes'][1]['fields']['data_governance'] = 'Domain-View'
        self.assertEqual(validate_urbanism(current, {}), [])
        text = render(current, 'Backlog')
        self.assertIn('Gouvernance des données', text)
        self.assertIn('Projection', text)
        self.assertIn('Domain-View', text)

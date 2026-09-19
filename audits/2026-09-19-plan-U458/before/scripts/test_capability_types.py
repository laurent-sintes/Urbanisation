"""U449 typing contract: mandatory in opted-in models, historical snapshots preserved."""
import unittest
from scripts.validate_models import validate_urbanism, CAPABILITY_NATURES
from scripts.structured_io import read


class CapabilityTypeTests(unittest.TestCase):
    def model(self, nature='action', policy=True):
        return {'nodes': [{'id': 'cap', 'kind': 'capability', 'fields': {'nature': nature}}],
                'relations': [], 'principles': [{'id': 'PRINCIPLE-CAPABILITY-NATURE'}] if policy else []}

    def test_six_supported_types(self):
        for nature in CAPABILITY_NATURES:
            self.assertEqual(validate_urbanism(self.model(nature), {}), [])

    def test_missing_or_invalid_type_rejected(self):
        for nature in (None, '', 'calculation', 'Decision'):
            self.assertTrue(any('capability nature' in e for e in validate_urbanism(self.model(nature), {})))

    def test_legacy_models_do_not_gain_a_typing_requirement(self):
        self.assertEqual(validate_urbanism(self.model(None, False), {}), [])

    def test_live_completeness_order_and_typology(self):
        model = read('modeles/backlog/model.yaml')
        nodes = {n['id']: n for n in model['nodes']}
        for node in nodes.values():
            if node['kind'] == 'capability':
                self.assertIn(node['fields'].get('nature'), CAPABILITY_NATURES)
            if node['kind'] in ('domain', 'reference'):
                decisions = [nodes[r['target_id']]['fields']['nature'] == 'decision' for r in model['relations']
                             if r['source_id'] == node['id'] and r['type'] == 'contains']
                self.assertEqual(decisions, sorted(decisions))
        annex = read('modeles/backlog/capability-types-U449.yaml')
        self.assertEqual({item['id'] for item in annex['types']}, CAPABILITY_NATURES)

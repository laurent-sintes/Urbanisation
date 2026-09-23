"""U449/U586 typing contract: opted-in models, historical snapshots preserved."""
from copy import deepcopy
import unittest
from scripts.validate_models import validate_urbanism, CAPABILITY_NATURES
from scripts.structured_io import read


class CapabilityTypeTests(unittest.TestCase):
    def model(self, nature='action', typing_required=True):
        # This fixture keeps the historical layer contract while isolating typing.
        return {'nodes': [{'id': 'cap', 'kind': 'capability', 'layer': 'transactional', 'fields': {'nature': nature}}],
                'relations': [], 'principles': [{'id': 'PRINCIPLE-CAPABILITY-NATURE'}] if typing_required else []}

    def test_seven_supported_types_include_policy(self):
        expected = {'action', 'management', 'knowledge', 'orchestration', 'planning', 'policy', 'decision'}
        self.assertEqual(CAPABILITY_NATURES, expected)
        for nature in expected:
            with self.subTest(nature=nature):
                self.assertEqual(validate_urbanism(self.model(nature), {}), [])

    def test_missing_or_invalid_type_rejected(self):
        for nature in (None, '', 'calculation', 'Decision', 'Policy', 'policy_strategy'):
            self.assertTrue(any('capability nature' in e for e in validate_urbanism(self.model(nature), {})))

    def test_legacy_models_do_not_gain_a_typing_requirement(self):
        self.assertEqual(validate_urbanism(self.model(None, False), {}), [])
        model = self.model(typing_required=False)
        model['nodes'][0]['fields'] = {'name': 'Supply Policy'}
        before = deepcopy(model)
        self.assertEqual(validate_urbanism(model, {}), [])
        self.assertEqual(model, before)

    def test_live_completeness_order_and_typology(self):
        model = read('modeles/backlog/model.yaml')
        nodes = {n['id']: n for n in model['nodes']}
        for node in nodes.values():
            if node['kind'] == 'capability':
                self.assertIn(node['fields'].get('nature'), CAPABILITY_NATURES)
            if node['kind'] in ('domain', 'area', 'reference'):
                decisions = [nodes[r['target_id']]['fields']['nature'] == 'decision' for r in model['relations']
                             if r['source_id'] == node['id'] and r['type'] == 'contains']
                self.assertEqual(decisions, sorted(decisions))
        annex = read('modeles/backlog/capability-types-U449.yaml')
        self.assertEqual({item['id'] for item in annex['types']}, CAPABILITY_NATURES)

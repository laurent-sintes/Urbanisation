from copy import deepcopy
import unittest
from scripts.business_scenarios import scenarios_for_node, validate_scenarios
from scripts.json_contract import validate
from scripts.structured_io import read
from scripts.publish_release import compile_snapshot
from scripts.test_request_metadata import model


class BusinessScenariosTests(unittest.TestCase):
    def setUp(self):
        self.snapshot = model()
        self.owner, self.consumer = self.snapshot['nodes'][:2]
        self.owner['fields']['examples'] = [{'id': 's', 'title': 'Cas', 'situation': 'Illustration FLOW.',
            'options': [{'title': 'Regrouper', 'description': 'Une seule expédition.'}],
            'contributions': [{'node_id': 'request', 'role': 'Comparer les options.'}], 'source_refs': ['U764']}]
        self.consumer['fields']['scenario_refs'] = [{'node_id': 'area', 'scenario_id': 's', 'contribution': 'Éclairer le choix.'}]
        self.nodes = {n['id']: n for n in self.snapshot['nodes']}

    def test_multiple_scenarios_and_shared_reference_survive_publication_without_mutation(self):
        self.owner['fields']['examples'].append({**self.owner['fields']['examples'][0], 'id': 's2'})
        before = deepcopy(self.snapshot)
        self.assertEqual(validate_scenarios(self.nodes), [])
        published = compile_snapshot(self.snapshot, {'decisions': []}, '2026-09-25.99', ['U764'])
        self.assertEqual(published['nodes'][0]['fields']['examples'], self.owner['fields']['examples'])
        self.assertEqual(published['nodes'][1]['fields']['scenario_refs'], self.consumer['fields']['scenario_refs'])
        self.assertEqual(self.snapshot, before)
        rendered = scenarios_for_node(self.consumer, self.nodes)
        rendered[0]['options'][0]['title'] = 'Changed'
        self.assertEqual(self.snapshot, before)

    def test_missing_duplicate_self_and_indirect_references_are_rejected(self):
        ref = self.consumer['fields']['scenario_refs'][0]
        ref['scenario_id'] = 'missing'
        self.assertTrue(validate_scenarios(self.nodes))
        ref['scenario_id'] = 's'
        self.consumer['fields']['scenario_refs'].append(deepcopy(ref))
        self.assertTrue(validate_scenarios(self.nodes))
        self.consumer['fields']['scenario_refs'].pop()
        self.owner['fields']['scenario_refs'] = [deepcopy(ref)]
        self.assertTrue(validate_scenarios(self.nodes))
        self.owner['fields'].pop('scenario_refs')
        self.owner['fields'].pop('examples')
        self.assertTrue(validate_scenarios(self.nodes))
        self.assertEqual(scenarios_for_node(self.consumer, self.nodes), [])

    def test_duplicate_local_ids_and_invalid_contributors_are_rejected(self):
        example = self.owner['fields']['examples'][0]
        self.owner['fields']['examples'].append(deepcopy(example))
        self.assertTrue(validate_scenarios(self.nodes))
        self.owner['fields']['examples'].pop()
        example['contributions'][0]['node_id'] = 'reaction'
        self.assertTrue(validate_scenarios(self.nodes))

    def test_optional_fields_have_a_strict_contract(self):
        schema = read('modeles/schemas/urbanism.schema.json')
        contract = schema['$defs']['businessExamples']
        examples = self.owner['fields']['examples']
        self.assertEqual(validate(examples, contract), [])
        examples[0]['options'][0]['description'] = ''
        self.assertTrue(validate(examples, contract))
        ref_contract = schema['$defs']['node']['properties']['fields']['properties']['scenario_refs']
        refs = self.consumer['fields']['scenario_refs']
        self.assertEqual(validate(refs, ref_contract), [])
        refs[0].pop('contribution')
        self.assertTrue(validate(refs, ref_contract))

    def test_render_exposes_options_and_local_contribution(self):
        from scripts.render_models import render
        output = render(self.snapshot, 'Test')
        self.assertIn('Scénarios métier', output)
        self.assertIn('Une seule expédition.', output)
        self.assertIn('Éclairer le choix.', output)


if __name__ == '__main__':
    unittest.main()

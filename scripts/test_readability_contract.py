from copy import deepcopy
from pathlib import Path
import unittest
from scripts.structured_io import read
from scripts.validate_models import validate_urbanism
from scripts.json_contract import validate

ROOT = Path(__file__).resolve().parents[1]

class ReadabilityContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = read(ROOT / 'modeles/backlog/model.yaml')
        cls.sources = {s['id']: s for s in read(ROOT / 'modeles/provenance/source-records.json')['records']}

    def test_single_behavior_rejected_only_under_new_principle(self):
        model = deepcopy(self.model)
        children = [r['target_id'] for r in model['relations'] if r['type'] == 'contains' and r['source_id'] == 'service-order-transport']
        self.assertGreaterEqual(len(children), 2)
        removed = set(children[1:])
        model['nodes'] = [n for n in model['nodes'] if n['id'] not in removed]
        model['relations'] = [r for r in model['relations'] if r['source_id'] not in removed and r['target_id'] not in removed]
        marker = 'requires zero or at least two'
        self.assertTrue(any(marker in e for e in validate_urbanism(model, self.sources)))
        model['principles'] = [p for p in model['principles'] if p['id'] != 'PRINCIPLE-DIFFERENTIATING-BEHAVIORS']
        self.assertFalse(any(marker in e for e in validate_urbanism(model, self.sources)))

    def test_role_is_optional_but_not_a_capability_type(self):
        schema = read(ROOT / 'modeles/schemas/urbanism.schema.json')['$defs']['node']['properties']['fields']
        self.assertNotIn('dominant_role', schema.get('required', []))
        role = schema['properties']['dominant_role']
        self.assertTrue(validate({'id': 'data-state'}, role))
        model = deepcopy(self.model)
        next(n for n in model['nodes'] if n['kind'] == 'capability')['fields']['dominant_role'] = {'id': 'data-state', 'display_name': 'Données'}
        self.assertTrue(any('dominant role belongs to a subdomain' in e for e in validate_urbanism(model, self.sources)))

    def test_removed_nodes_leave_no_dangling_relations(self):
        ids = {n['id'] for n in self.model['nodes']}
        self.assertFalse(ids & {'D07.b', 'vas-repacking', 'vas-labeling-relabeling'})
        self.assertTrue(all(r['source_id'] in ids and r['target_id'] in ids for r in self.model['relations']))

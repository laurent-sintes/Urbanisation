"""Current layer-free models and immutable historical contracts both remain readable."""
from copy import deepcopy
from pathlib import Path
import unittest
from scripts.structured_io import read
from scripts.validate_models import validate_urbanism
from scripts.element_versions import assign_versions

ROOT = Path(__file__).resolve().parents[1]


class LayerRetirementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = read(ROOT / 'modeles/backlog/model.yaml')
        cls.model['glossary'] = read(ROOT / 'modeles/backlog/glossary.yaml')
        cls.sources = {s['id']: s for s in read(ROOT / 'modeles/provenance/source-records.json')['records']}
        cls.schema = read(ROOT / 'modeles/schemas/urbanism.schema.json')

    def test_current_contract_rejects_reintroduced_layer(self):
        self.assertTrue(all('layer' not in n for n in self.model['nodes']))
        model = deepcopy(self.model)
        model['nodes'][0]['layer'] = 'process'
        errors = validate_urbanism(model, self.sources, self.schema)
        self.assertTrue(any('layer is retired' in error for error in errors), errors)

    def test_historical_publication_contract_is_preserved(self):
        release = ROOT / 'modeles/release'
        descriptor = read(release / read(release / 'index.json')['current'])
        model = read(release / descriptor['path'])
        self.assertEqual(validate_urbanism(model, self.sources, self.schema), [])

    def test_layer_removal_revises_content_without_erasing_its_history(self):
        previous = {'model_id': 'fixture', 'nodes': [{'id': 'A', 'kind': 'capability', 'layer': 'transactional', 'fields': {'name': 'A'}}]}
        assign_versions(previous, {}, now='2026-09-19T00:00:00Z')
        current = deepcopy(previous)
        current['nodes'][0].pop('layer')
        changes = assign_versions(current, previous, now='2026-09-19T01:00:00Z')
        self.assertEqual(current['nodes'][0]['revision'], 2)
        self.assertEqual(previous['nodes'][0]['layer'], 'transactional')
        self.assertTrue(any(c['id'] == 'A' and c['reason'] == 'changed' for c in changes))

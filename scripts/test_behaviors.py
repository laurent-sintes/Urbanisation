"""Behavior contract: real backlog, invalid hierarchies and preserved definitions."""
from copy import deepcopy
from pathlib import Path
import unittest
from scripts.structured_io import read
from scripts.validate_models import validate_urbanism
from scripts.lifecycle import value_hash

ROOT = Path(__file__).resolve().parents[1]

class BehaviorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = read(ROOT / 'modeles/backlog/model.yaml')
        cls.model['glossary'] = read(ROOT / 'modeles/backlog/glossary.yaml')
        cls.schema = read(ROOT / 'modeles/schemas/urbanism.schema.json')
        cls.sources = {s['id']: s for s in read(ROOT / 'modeles/provenance/source-records.json')['records']}

    def check_model(self, model):
        return validate_urbanism(model, self.sources, self.schema)

    def test_adopted_definitions_and_parentage(self):
        self.assertEqual(self.check_model(self.model), [])
        adopted = read(ROOT / 'modeles/backlog/d03-review.yaml')['atp_behaviors_U263']['behaviors']
        for entry in adopted:
            node = next(n for n in self.model['nodes'] if n['id'] == entry['node_id'])
            self.assertEqual(value_hash(node['fields']['definition']), entry['definition_sha256'])
            self.assertEqual(node['lifecycle']['validated_fields'], ['definition'])
            parents = [r for r in self.model['relations'] if r['target_id'] == node['id'] and r['type'] == 'contains']
            self.assertEqual([r['source_id'] for r in parents], ['D03.i'])

    def test_invalid_hierarchies_rejected(self):
        for case in ('orphan', 'two_parents', 'domain_parent', 'behavior_child', 'empty_definition'):
            with self.subTest(case=case):
                model = deepcopy(self.model)
                rel = next(r for r in model['relations'] if r['id'] == 'REL-ATP-BHV001')
                node = next(n for n in model['nodes'] if n['id'] == 'BHV001')
                if case == 'orphan': model['relations'].remove(rel)
                if case == 'two_parents':
                    other = deepcopy(rel); other['id'] += '-SECOND'; other.pop('lifecycle'); model['relations'].append(other)
                if case == 'domain_parent': rel['source_id'] = 'D03'
                if case == 'behavior_child': rel['source_id'] = 'BHV002'
                if case == 'empty_definition': node['fields']['definition'] = ' '
                errors = self.check_model(model)
                self.assertTrue(any('behavior/' in e for e in errors), errors)

    def test_planning_adoption_and_decision_boundaries(self):
        # U269/U271 approvals belong to the preserved pre-refactoring state.
        historical = read(ROOT / 'audits/2026-09-17-refonte-appliquee/model-before.yaml')
        registry = read(ROOT / 'modeles/backlog/d05-refactoring.yaml')
        agreement = registry['scenario_behaviors_U269']
        self.assertEqual(len(agreement['behaviors']), 5)
        updates = registry['scenario_impact_U271']
        revised = {e['node_id']: e for e in updates['revised_behaviors']}
        entries = [revised.get(e['node_id'], e) for e in agreement['behaviors']] + [updates['new_behavior']]
        self.assertEqual(len(entries), 6)
        for entry in entries:
            node = next(n for n in historical['nodes'] if n['id'] == entry['node_id'])
            self.assertEqual(node['lifecycle']['validated_fields'], ['name', 'definition'])
            for field in ('name', 'definition'):
                self.assertEqual(value_hash(node['fields'][field]), entry['value_sha256'][field])
            self.assertNotIn('scope', node['lifecycle']['validated_fields'])
            parents = [r['source_id'] for r in historical['relations'] if r['type'] == 'contains' and r['target_id'] == node['id']]
            self.assertEqual(parents, ['D05.f'])
        for identifier in ('D05.a', 'D05.d', 'D05.e', 'D05.c'):
            parents = [r['source_id'] for r in self.model['relations'] if r['type'] == 'contains' and r['target_id'] == identifier]
            self.assertEqual(parents, ['D05'])
        planning = next(n for n in historical['nodes'] if n['id'] == 'D05.f')
        self.assertNotIn('definition', planning['lifecycle']['validated_fields'])
        self.assertEqual(value_hash(planning['fields']['decomposition_rationale']), agreement['decomposition_rationale_sha256'])

    def test_impact_boundary_updates_preserve_historical_agreement(self):
        registry = read(ROOT / 'modeles/backlog/d05-refactoring.yaml')
        old = read(ROOT / registry['scenario_impact_U271']['historical_capture'])
        for identifier in ('BHV006', 'BHV007'):
            earlier = next(n for n in old['nodes'] if n['id'] == identifier)
            before_refactoring = read(ROOT / 'audits/2026-09-17-refonte-appliquee/model-before.yaml')
            current = next(n for n in before_refactoring['nodes'] if n['id'] == identifier)
            prior = next(e for e in registry['scenario_behaviors_U269']['behaviors'] if e['node_id'] == identifier)
            self.assertEqual(value_hash(earlier['fields']['definition']), prior['value_sha256']['definition'])
            self.assertNotEqual(current['fields']['definition'], earlier['fields']['definition'])
            self.assertIn('U271', current['lifecycle']['source_refs'])

    def test_refactored_behaviors_keep_one_parent_and_concrete_responsibilities(self):
        nodes = {n['id']: n for n in self.model['nodes']}
        for parent, expected in {'D05.f': ['BHV005','BHV006','BHV016'],
                                 'D02.b': ['BHV017','BHV018','BHV019','BHV020'],
                                 'D03.n': ['BHV021','BHV022','BHV023']}.items():
            children = [r['target_id'] for r in self.model['relations'] if r['type']=='contains' and r['source_id']==parent]
            self.assertEqual(set(children), set(expected))
            self.assertTrue(nodes[parent]['fields']['decomposition_rationale'])
        registry = read(ROOT / 'modeles/backlog/refactoring-implementation.yaml')
        for old, target in registry['retired_node_redirects'].items():
            self.assertNotIn(old, nodes)
            self.assertIn(target, nodes)
        # Product operations remain discoverable after their hierarchy nodes retire.
        scope = nodes['D02.b']['fields']['scope'].lower()
        for operation in ('réallocation', 'libération', 'consommation', 'consultation'):
            self.assertIn(operation, scope)
        # A promise merge does not drop illustrative object/document/event links.
        for identifier in ('REL-ILL-001','REL-ILL-002','REL-ILL-003'):
            rel = next(r for r in self.model['relations'] if r['id']==identifier)
            self.assertEqual(rel['source_id'], 'D03.n')

    def test_historical_publication_still_valid(self):
        old = read(ROOT / 'modeles/release/2026-09-16.2/model.yaml')
        self.assertEqual(self.check_model(old), [])
        self.assertFalse(any(n['kind'] == 'behavior' for n in old['nodes']))

    def test_justification_required_without_forcing_every_capability_to_decompose(self):
        for value in (None, '', '   '):
            model = deepcopy(self.model)
            fields = next(n['fields'] for n in model['nodes'] if n['id'] == 'D03.i')
            if value is None: fields.pop('decomposition_rationale')
            else: fields['decomposition_rationale'] = value
            self.assertTrue(any('decomposition requires' in e for e in self.check_model(model)))
        model = deepcopy(self.model)
        fields = next(n['fields'] for n in model['nodes'] if n['id'] == 'D03.i')
        fields['decomposition_rationale'] = 'Bénéfice ciblé : expliquer les délais de mobilisation.'
        self.assertEqual(self.check_model(model), [])

    def test_pre_convention_snapshot_does_not_gain_new_requirements(self):
        model = deepcopy(self.model)
        model['principles'] = [p for p in model['principles'] if p['id'] != 'PRINCIPLE-JUSTIFIED-BEHAVIOR']
        next(n['fields'] for n in model['nodes'] if n['id'] == 'D03.i').pop('decomposition_rationale')
        self.assertEqual(self.check_model(model), [])

if __name__ == '__main__': unittest.main()

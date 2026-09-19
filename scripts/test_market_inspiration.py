"""Editorial inspiration stays optional, complete, sourced and snapshot-compatible."""
from copy import deepcopy
import unittest

from scripts.glossary import validate as validate_glossary
from scripts.json_contract import validate
from scripts.market_comparison import validate_comparisons, validate_inspiration
from scripts.render_models import render
from scripts.structured_io import read
from scripts.validate_models import validate_urbanism


class MarketInspirationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = read('modeles/schemas/urbanism.schema.json')
        cls.entry = {
            'vendor': 'Example Consortium', 'product': 'Reference model',
            'element_name': 'Coordinate supply', 'element_type': 'Reference process',
            'relationship': 'Concept proche', 'similarities': 'Coordonner les acteurs.',
            'differences': 'La stratégie est incluse.', 'flow_position': 'Responsabilités métier.',
            'source_title': 'Coordination reference', 'source_url': 'https://example.org/reference',
            'source_version': '1', 'consulted_on': '2026-09-19', 'source_locator': 'Section 2',
            'evidence_limits': 'Aucune preuve de réalisation.', 'status': 'proposed', 'source_refs': ['ELM1'],
            'concept_name': 'Coordination', 'scope_summary': 'Coopération et stratégie.',
            'approach_summary': 'Organiser les rôles.'}
        cls.inspiration = {
            'choice': 'Nous retenons Orchestration pour coordonner les réponses aux demandes.',
            'flow_scope': 'Commandes et engagements.', 'flow_approach': 'Responsabilités métier.',
            'synthesis': ['Le référentiel inclut la stratégie ; FLOW décrit la réponse aux demandes.'],
            'examples': [{'title': 'Livraison partielle', 'situation': '75 pièces sur 100.',
                          'outcome': 'Chercher les 25 pièces restantes.',
                          'lesson': 'Relier les ressources aux engagements.', 'source_refs': ['ELM1'],
                          'source_title': 'Coordination example', 'source_url': 'https://example.org/example'}]}

    def model(self):
        return {'space': 'backlog', 'version': 'test', 'as_of': '2026-09-19',
                'nodes': [{'id': 'SUPPLY', 'kind': 'group', 'layer': 'transactional',
                           'fields': {'name': 'Supply Chain Orchestration',
                                      'market_comparisons': [deepcopy(self.entry)],
                                      'market_inspiration': deepcopy(self.inspiration)},
                           'review': {'state': 'proposed'}, 'source_refs': ['ELM1']}],
                'relations': [], 'principles': []}

    def term(self):
        return {'id': 'TER1', 'name': 'Coordination', 'short_description': 'Coordonner.',
                'definition': 'Relier les réponses aux demandes.', 'source_refs': ['ELM1'],
                'review': {'state': 'proposed'}, 'market_comparisons': [deepcopy(self.entry)],
                'market_inspiration': deepcopy(self.inspiration)}

    def test_old_comparisons_need_no_editorial_summaries(self):
        entry = deepcopy(self.entry)
        for field in ('concept_name', 'scope_summary', 'approach_summary'):
            entry.pop(field)
        self.assertEqual(validate_comparisons([entry], 'legacy'), [])
        model = self.model()
        model['nodes'][0]['fields'] = {'name': 'Old model', 'market_comparisons': [entry]}
        self.assertEqual(validate_urbanism(model, {'ELM1': {}}), [])
        output = render(model, 'Legacy')
        self.assertIn('Points communs.', output)
        self.assertNotIn('| Source et nom employé |', output)

    def test_current_frozen_publication_remains_valid(self):
        root = 'modeles/release/'
        descriptor = read(root + read(root + 'index.json')['current'])
        self.assertEqual(validate(read(root + descriptor['path']), self.schema), [])

    def test_complete_inspiration_passes_node_and_glossary_validation(self):
        model = self.model()
        model['glossary'] = {'terms': [self.term()]}
        self.assertEqual(validate_urbanism(model, {'ELM1': {}}), [])
        self.assertEqual(validate_glossary(model), [])
        fields_schema = {'$defs': self.schema['$defs'],
                         **self.schema['$defs']['node']['properties']['fields']}
        term_schema = {'$defs': self.schema['$defs'],
                       **self.schema['properties']['glossary']['properties']['terms']['items']}
        self.assertEqual(validate(model['nodes'][0]['fields'], fields_schema), [])
        self.assertEqual(validate(self.term(), term_schema), [])
        invalid_term = self.term()
        invalid_term['market_inspiration']['examples'][0]['source_url'] = 'file:///local.txt'
        self.assertTrue(validate(invalid_term, term_schema))

    def test_incomplete_table_is_rejected_by_node_and_glossary_paths(self):
        for field in ('concept_name', 'scope_summary', 'approach_summary'):
            model = self.model()
            del model['nodes'][0]['fields']['market_comparisons'][0][field]
            self.assertTrue(any(field in error for error in validate_urbanism(model, {'ELM1': {}})))
            term = self.term()
            del term['market_comparisons'][0][field]
            self.assertTrue(any(field in error for error in validate_glossary({'glossary': {'terms': [term]}})))
        self.assertTrue(validate_inspiration(self.inspiration, [], 'empty'))

    def test_optional_summaries_are_nonblank_strings(self):
        for field in ('concept_name', 'scope_summary', 'approach_summary'):
            for value in ('', '   ', 42, None):
                entry = deepcopy(self.entry)
                entry[field] = value
                self.assertTrue(validate_comparisons([entry], 'bad'), (field, value))

    def test_inspiration_requires_choice_table_synthesis_and_example(self):
        for field in ('choice', 'flow_scope', 'flow_approach', 'synthesis', 'examples'):
            value = deepcopy(self.inspiration)
            value.pop(field)
            self.assertTrue(validate_inspiration(value, [self.entry], 'missing'), field)
        for field, invalid in [('choice', ' '), ('synthesis', []), ('synthesis', [' ']), ('examples', [])]:
            value = deepcopy(self.inspiration)
            value[field] = invalid
            self.assertTrue(validate_inspiration(value, [self.entry], 'invalid'), field)

    def test_example_requires_attribution_and_http_source(self):
        for field in ('title', 'situation', 'source_refs', 'source_title', 'source_url'):
            value = deepcopy(self.inspiration)
            value['examples'][0].pop(field)
            self.assertTrue(validate_inspiration(value, [self.entry], 'missing'), field)
        for url in ('javascript:alert(1)', 'file:///C:/local.txt', 'https://', 'https://example.org/has space'):
            value = deepcopy(self.inspiration)
            value['examples'][0]['source_url'] = url
            self.assertTrue(validate_inspiration(value, [self.entry], 'invalid'), url)

    def test_example_provenance_uses_the_existing_source_registry(self):
        model = self.model()
        model['nodes'][0]['fields']['market_inspiration']['examples'][0]['source_refs'] = ['MISSING']
        self.assertTrue(any('market_inspiration/examples/0/source_refs: unknown source MISSING' in error
                            for error in validate_urbanism(model, {'ELM1': {}})))

    def test_glossary_inspiration_links_must_resolve(self):
        term = self.term()
        term['market_inspiration']['choice'] += ' [Terme absent](glossary:MISSING).'
        self.assertIn('glossary: unresolved published link MISSING',
                      validate_glossary({'glossary': {'terms': [term]}}))

    def test_render_orders_choice_table_synthesis_example_and_original_detail(self):
        model = self.model()
        model['glossary'] = {'terms': [self.term()]}
        output = render(model, 'Inspiration')
        positions = [output.index(value) for value in [self.inspiration['choice'],
                     '| Source et nom employé |', self.inspiration['synthesis'][0],
                     '75 pièces sur 100.', '### Détails des références']]
        self.assertEqual(positions, sorted(positions))
        self.assertIn('[Coordination example](https://example.org/example)', output)
        self.assertIn('Références : ELM1.', output)
        self.assertIn('**Limite de preuve.** Aucune preuve de réalisation.', output)
        self.assertEqual(output.count('| Source et nom employé |'), 2)


if __name__ == '__main__':
    unittest.main()

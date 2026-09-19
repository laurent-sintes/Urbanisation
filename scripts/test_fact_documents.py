"""The U461 convention requires a document link without inventing a 1:1 rule."""
from copy import deepcopy
import unittest

from scripts.validate_models import validate_urbanism


class FactDocumentTests(unittest.TestCase):
    def setUp(self):
        self.model = {
            'nodes': [
                {'id': 'DOC', 'kind': 'document', 'fields': {'name': 'Receipt document'}},
                {'id': 'FACT', 'kind': 'event', 'fields': {'name': 'Goods received'}},
            ],
            'relations': [{'id': 'LINK', 'type': 'records', 'source_id': 'DOC', 'target_id': 'FACT'}],
            'principles': [
                {'id': 'PRINCIPLE-DOMAIN-INTERACTIONS'},
                {'id': 'PRINCIPLE-MANAGEMENT-FACT-DOCUMENT'},
            ],
        }

    def errors(self, model=None):
        return validate_urbanism(self.model if model is None else model, {})

    def test_identified_structured_document_needs_no_file(self):
        self.assertEqual(self.errors(), [])

    def test_fact_without_document_is_rejected(self):
        self.model['relations'] = []
        self.assertTrue(any('identified document via records' in e for e in self.errors()))

    def test_all_facts_need_their_link(self):
        self.model['nodes'].append({'id': 'SECOND', 'kind': 'event', 'fields': {'name': 'Second fact'}})
        self.assertTrue(any('nodes/SECOND: management fact' in e for e in self.errors()))

    def test_multiple_documents_and_multiple_facts_remain_possible(self):
        self.model['nodes'] += [
            {'id': 'DOC2', 'kind': 'document', 'fields': {'name': 'Second document'}},
            {'id': 'FACT2', 'kind': 'event', 'fields': {'name': 'Second fact'}},
        ]
        self.model['relations'] += [
            {'id': 'LINK2', 'type': 'records', 'source_id': 'DOC2', 'target_id': 'FACT'},
            {'id': 'LINK3', 'type': 'records', 'source_id': 'DOC', 'target_id': 'FACT2'},
        ]
        self.assertEqual(self.errors(), [])

    def test_invalid_endpoint_cannot_satisfy_the_requirement(self):
        for source in ['MISSING', 'FACT']:
            with self.subTest(source=source):
                model = deepcopy(self.model)
                model['relations'][0]['source_id'] = source
                self.assertTrue(any('identified document via records' in e for e in self.errors(model)))

    def test_another_relation_is_not_a_document_link(self):
        self.model['relations'][0]['type'] = 'represents'
        self.assertTrue(any('identified document via records' in e for e in self.errors()))

    def test_models_without_the_convention_keep_their_contract(self):
        self.model['principles'].pop()
        self.model['relations'] = []
        self.assertEqual(self.errors(), [])


if __name__ == '__main__':
    unittest.main()

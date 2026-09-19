import unittest
from copy import deepcopy
from scripts.market_comparison import validate_reference_policy
from scripts.element_versions import assign_versions


class ReferencePolicyTests(unittest.TestCase):
    def model(self, *urls):
        return {'market_reference_policy': 'two_primary_sources', 'nodes': [
            {'id': 'CAP', 'fields': {'market_comparisons': [{'source_url': u} for u in urls]}}
        ], 'relations': []}

    def test_historical_publication_keeps_its_contract(self):
        model = self.model('https://example.org/one')
        del model['market_reference_policy']
        self.assertEqual(validate_reference_policy(model), [])

    def test_missing_reference_is_not_padded_and_single_reference_fails(self):
        self.assertEqual(validate_reference_policy(self.model()), [])
        self.assertEqual(len(validate_reference_policy(self.model('https://example.org/one'))), 1)

    def test_anchor_and_query_cannot_manufacture_another_document(self):
        self.assertEqual(len(validate_reference_policy(self.model(
            'https://example.org/one#first', 'http://EXAMPLE.ORG/one/?tracking=x#second'))), 1)
        self.assertEqual(validate_reference_policy(self.model(
            'https://example.org/one', 'https://example.org/two')), [])

    def test_glossary_and_relations_are_checked(self):
        model = self.model()
        model['glossary'] = {'terms': [{'id': 'TER', 'market_comparisons': [{'source_url':'https://example.org/one'}]}]}
        model['relations'] = [{'id':'R', 'fields': {'market_comparisons': [{'source_url':'https://example.org/two'}]}}]
        self.assertEqual(len(validate_reference_policy(model)), 2)

    def test_policy_participates_in_new_snapshot_fingerprint(self):
        previous={'model_id':'test', 'nodes':[], 'relations':[]}
        assign_versions(previous, {}, '2099-01-01T00:00:00Z')
        candidate=deepcopy(previous)
        candidate['market_reference_policy']='two_primary_sources'
        assign_versions(candidate, previous, '2099-01-02T00:00:00Z')
        self.assertNotEqual(candidate['content_sha256'], previous['content_sha256'])
        self.assertEqual(candidate['revision'], previous['revision']+1)


if __name__ == '__main__': unittest.main()

import copy
import unittest
from scripts.structured_io import read
from scripts.market_comparison import validate_comparisons
from scripts.glossary import validate as validate_glossary

class MarketComparisonsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = read('modeles/backlog/model.yaml')
        cls.glossary = read('modeles/backlog/glossary.yaml')
        cls.entries = next(n for n in cls.model['nodes'] if n['id']=='D05.e')['fields']['market_comparisons']

    def test_documented_sources_and_differences_required(self):
        self.assertEqual(validate_comparisons(self.entries, 'test'), [])
        for field in ['differences', 'source_url', 'source_version', 'consulted_on', 'evidence_limits']:
            bad = copy.deepcopy(self.entries)
            del bad[0][field]
            self.assertTrue(validate_comparisons(bad, 'test'), field)

    def test_invalid_link_and_date_rejected(self):
        for field,value in [('source_url','javascript:alert(1)'), ('consulted_on','2026-02-30')]:
            bad=copy.deepcopy(self.entries)
            bad[0][field]=value
            self.assertTrue(validate_comparisons(bad,'test'))

    def test_glossary_uses_same_contract_and_old_terms_remain_valid(self):
        model=copy.deepcopy(self.model)
        model['glossary']=copy.deepcopy(self.glossary)
        self.assertEqual(validate_glossary(model), [])
        term=next(t for t in model['glossary']['terms'] if t['id']=='TER079')
        del term['market_comparisons'][0]['similarities']
        self.assertTrue(validate_glossary(model))
        for t in model['glossary']['terms']:
            t.pop('market_comparisons', None)
            t.pop('market_inspiration', None)
        self.assertEqual(validate_glossary(model), [])

if __name__=='__main__':
    unittest.main()

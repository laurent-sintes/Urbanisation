"""Reader content additions stay optional and sourced; old snapshots remain valid."""
from copy import deepcopy
import unittest
from scripts.structured_io import read
from scripts.json_contract import validate
from scripts.market_comparison import validate_comparisons


class BusinessExamplesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = read('modeles/schemas/urbanism.schema.json')
        cls.contract = cls.schema['$defs']['businessExamples']
        cls.example = {'title':'Réception partielle','situation':'60 reçues sur 100.', 'outcome':'40 restantes.', 'source_refs':['U391']}

    def test_structured_example_keeps_its_internal_provenance(self):
        self.assertEqual(validate([self.example], self.contract), [])
        for key in ['title','situation','source_refs']:
            value=deepcopy(self.example);value.pop(key)
            self.assertTrue(validate([value],self.contract),key)

    def test_unknown_metadata_and_invalid_examples_are_rejected(self):
        for field,value in [('situation',''),('source_refs',[]),('outcome',42),('invented_validation',True)]:
            item=deepcopy(self.example);item[field]=value
            self.assertTrue(validate([item],self.contract),(field,value))

    def test_choice_explanations_are_optional_but_typed(self):
        model=read('modeles/backlog/model.yaml')
        entry=deepcopy(next(n for n in model['nodes'] if n['id']=='D03.n')['fields']['market_comparisons'][-1])
        self.assertEqual(validate_comparisons([entry],'test'),[])
        for field in ['term_choice','definition_choice']:
            invalid=deepcopy(entry);invalid[field]=''
            self.assertTrue(validate_comparisons([invalid],'test'))
        entry.pop('term_choice');entry.pop('definition_choice')
        self.assertEqual(validate_comparisons([entry],'test'),[])

    def test_published_nodes_without_examples_keep_their_contract(self):
        root='modeles/release/'
        descriptor=read(root+read(root+'index.json')['current'])
        published=read(root+descriptor['path'])
        self.assertEqual(validate(published,self.schema),[])

    def test_backlog_reading_contains_the_new_content_with_its_provenance(self):
        from scripts.render_models import render
        model=read('modeles/backlog/model.yaml')
        output=render(model,'Fixture de restitution')
        self.assertIn('Pourquoi ce terme',output)
        self.assertIn('Répartir une pénurie sans scinder les commandes',output)
        self.assertIn('U462',output)


if __name__=='__main__':
    unittest.main()

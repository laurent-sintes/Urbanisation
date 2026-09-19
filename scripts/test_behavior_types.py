import unittest
from scripts.structured_io import read
from scripts.validate_models import validate_urbanism, BEHAVIOR_NATURES

class BehaviorTypeTests(unittest.TestCase):
    def test_all_live_behaviors_have_a_supported_form(self):
        model=read('modeles/backlog/model.yaml')
        behaviors=[node for node in model['nodes'] if node['kind']=='behavior']
        self.assertTrue(behaviors, 'The live model must contain behaviors to verify their forms')
        self.assertTrue(all(node['fields'].get('nature') in BEHAVIOR_NATURES for node in behaviors))
        forms=next(term for term in read('modeles/backlog/modeling-glossary.yaml')['terms'] if term['id']=='MOD006')['concrete_forms']
        self.assertEqual({item['key'] for item in forms},BEHAVIOR_NATURES)

    def test_typing_requirement_is_opt_in_and_uses_behavior_forms(self):
        # Keep both historical layers valid so this test isolates behavior typing.
        model={'nodes':[{'id':'cap','kind':'capability','layer':'transactional','fields':{}},{'id':'behavior','kind':'behavior','layer':'transactional','fields':{'name':'Test','definition':'Test','nature':'decision'}}],
               'relations':[{'id':'edge','type':'contains','source_id':'cap','target_id':'behavior'}],
               'principles':[{'id':'PRINCIPLE-BEHAVIOR-NATURE'}]}
        self.assertTrue(any('behavior nature' in error for error in validate_urbanism(model,{})))
        model['nodes'][1]['fields']['nature']='process_variant'
        self.assertEqual(validate_urbanism(model,{}),[])
        model['principles']=[];model['nodes'][1]['fields'].pop('nature')
        self.assertEqual(validate_urbanism(model,{}),[])

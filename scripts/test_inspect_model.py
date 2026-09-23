import json
import unittest
from scripts.inspect_model import inspect
from scripts.test_publish_release import isolated_project


class InspectModelTests(unittest.TestCase):
    def test_cli_emits_utf8_under_restrictive_windows_pipe_encoding(self):
        import os
        import subprocess
        import sys
        code = "from scripts import inspect_model as m; m.inspect = lambda **kw: {'text': '\\u2192 \\u00e9'}; m.main()"
        result = subprocess.run([sys.executable, '-c', code], env=os.environ | {'PYTHONIOENCODING': 'ascii:strict'}, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout.decode('utf-8')), {'text': '→ é'})

    def fixture(self, root):
        folder=root/'modeles/backlog'; folder.mkdir(parents=True)
        model={'version':'work', 'nodes':[
            {'id':'P','kind':'domain','fields':{'name':'Parent'}},
            {'id':'C','kind':'capability','fields':{'name':'Child','definition':'Exact\ntext','market_comparisons':[{'vendor':'Example'}]}}],
            'relations':[{'id':'R','type':'contains','source_id':'P','target_id':'C','fields':{'name':'Contains'}}]}
        (folder/'model.json').write_text(json.dumps(model),encoding='utf-8')
        (folder/'glossary.json').write_text(json.dumps({'terms':[{'id':'TER001','name':'Term','definition':'Exact term'}]}),encoding='utf-8')

    def test_targeted_values_and_explicit_relations_preserve_source(self):
        with isolated_project() as root:
            self.fixture(root)
            path=root/'modeles/backlog/model.json'; before=path.read_bytes()
            result=inspect(root,ids=['C'],fields=['definition'],relations=True)['items'][0]
            self.assertEqual(result['fields'],{'definition':'Exact\ntext'})
            self.assertEqual(result['parents'],[{'id':'P','relation_id':'R','type':'contains'}])
            self.assertEqual(result['relations'][0]['target_id'],'C')
            edge=inspect(root,collection='relations',ids=['R'])['items'][0]
            self.assertEqual(edge['fields']['source_id'],'P')
            self.assertEqual(edge['fields']['fields'],{'name':'Contains'})
            self.assertEqual(path.read_bytes(),before)

    def test_discovery_is_paginated_and_explicit_ids_are_not_truncated(self):
        with isolated_project() as root:
            self.fixture(root)
            self.assertEqual(inspect(root,limit=1)['next_offset'],1)
            self.assertEqual(inspect(root,offset=1,limit=1)['items'][0]['id'],'C')
            self.assertEqual(inspect(root,ids=['C','P'],limit=1)['returned'],2)
            self.assertEqual(inspect(root,query='child')['items'][0]['id'],'C')

    def test_glossary_and_missing_identity_do_not_fall_back(self):
        with isolated_project() as root:
            self.fixture(root)
            self.assertEqual(inspect(root,collection='terms',ids=['TER001'])['items'][0]['fields']['definition'],'Exact term')
            with self.assertRaises(ValueError): inspect(root,ids=['TER001'])
            with self.assertRaises(ValueError): inspect(root,version='historical')
            with self.assertRaises((ValueError,OSError)): inspect(root,space='release',ids=['C'])


if __name__ == '__main__': unittest.main()

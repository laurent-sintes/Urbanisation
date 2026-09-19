"""Contract, publication isolation and revision tests for transverse information."""
from copy import deepcopy
from pathlib import Path
import unittest
from unittest.mock import patch
from scripts.structured_io import read
from scripts.information_catalog import validate_information
from scripts.element_versions import assign_versions
from scripts.validate_models import validate_urbanism, validate_release
from scripts.publish_release import compile_snapshot
from scripts.prepare_release import model_diff

ROOT = Path(__file__).resolve().parents[1]

class InformationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.live = read(ROOT/'modeles/backlog/model.yaml')
        cls.live['glossary'] = read(ROOT/'modeles/backlog/glossary.yaml')
        cls.catalogue = cls.live['information_catalog']
        cls.schema = read(ROOT/'modeles/schemas/urbanism.schema.json')
        cls.sources = {r['id']:r for r in read(ROOT/'modeles/provenance/source-records.json')['records']}

    def model(self):
        return deepcopy(self.live)

    def test_complete_pilot_and_legacy_absence(self):
        model=self.model()
        self.assertEqual(validate_information(model),[])
        self.assertEqual(validate_urbanism(model,self.sources,self.schema),[])
        model.pop('information_catalog')
        self.assertEqual(validate_information(model),[])

    def test_orphan_noncapability_duplicate_and_illustration_roles(self):
        for target in ('ABSENT',next(n['id'] for n in self.live['nodes'] if n['kind']=='behavior')):
            model=self.model();model['information_catalog']['items'][0]['capability_roles'][0]['capability_ref']=target
            self.assertTrue(any('capability' in e for e in validate_information(model)))
        model=self.model(); roles=model['information_catalog']['items'][0]['capability_roles'];roles.append(deepcopy(roles[0]))
        self.assertTrue(any('repeated' in e for e in validate_information(model)))
        target=roles[0]['capability_ref'];next(n for n in model['nodes'] if n['id']==target)['review']['state']='illustration'
        self.assertTrue(any('nonpublishable' in e for e in validate_information(model)))

    def test_identity_collisions_and_invalid_endpoints(self):
        for identifier in (self.live['nodes'][0]['id'],self.catalogue['items'][1]['id'],self.catalogue['id']):
            model=self.model();model['information_catalog']['items'][0]['id']=identifier
            self.assertTrue(any('identity' in e for e in validate_information(model)))
        for target in ('ABSENT',self.catalogue['links'][0]['from_ref']):
            model=self.model();model['information_catalog']['links'][0]['to_ref']=target
            self.assertTrue(validate_information(model))

    def test_required_business_content_and_no_implicit_adoption(self):
        for field in ('essential_elements','examples','market_comparisons','definition'):
            model=self.model();del model['information_catalog']['items'][0][field]
            self.assertTrue(validate_urbanism(model,self.sources,self.schema),field)
        model=self.model();model['information_catalog']['items'][0]['review']['state']='accepted'
        self.assertTrue(validate_urbanism(model,self.sources,self.schema))

    def test_compile_copies_information_from_frozen_input_and_keeps_tree(self):
        snapshot=self.model()
        result=compile_snapshot(snapshot,{'decisions':[]},'2099-01-01.1',['U468'])
        self.assertEqual(result['information_catalog'],snapshot['information_catalog'])
        self.assertEqual({n['id'] for n in result['nodes']},
                         {n['id'] for n in snapshot['nodes'] if n['review']['state']!='illustration'})
        snapshot['information_catalog']['items'][0]['definition']='Changed later'
        self.assertNotEqual(result['information_catalog'],snapshot['information_catalog'])

    def test_release_rejects_dropped_or_tampered_frozen_information(self):
        snapshot=self.model()
        for change in ('drop','definition'):
            release=deepcopy(snapshot)
            if change=='drop': release.pop('information_catalog')
            else: release['information_catalog']['items'][0]['definition']='Tampered'
            # Isolate the release/snapshot equality invariant from unrelated decisions.
            with patch('scripts.validate_models.validate_urbanism',return_value=[]):
                errors=validate_release(release,{},snapshot,self.sources)
            self.assertIn('release: information catalogue differs from frozen input',errors)

    def test_versions_track_only_changed_information_and_root(self):
        base={'model_id':'fixture','nodes':[{'id':'CAP','fields':{'name':'Capability'}}], 'relations':[],
              'information_catalog':deepcopy(self.catalogue)}
        assign_versions(base,{},now='2099-01-01T00:00:00Z')
        unchanged=deepcopy(base)
        self.assertEqual(assign_versions(unchanged,base,now='2099-01-02T00:00:00Z'),[])
        self.assertEqual(unchanged,base)
        revised=deepcopy(base);revised['information_catalog']['items'][0]['definition']+=' Clarification.'
        changes=assign_versions(revised,base,now='2099-01-02T00:00:00Z')
        self.assertEqual([(c['collection'],c['id']) for c in changes],[('information_items',self.catalogue['items'][0]['id'])])
        self.assertEqual(revised['nodes'],base['nodes'])
        self.assertEqual(revised['revision'],base['revision']+1)
        self.assertEqual(revised['information_catalog']['revision'],2)
        removed=deepcopy(base);removed.pop('information_catalog');assign_versions(removed,base,now='2099-01-02T00:00:00Z')
        self.assertEqual(removed['revision'],base['revision']+1)

    def test_release_diff_includes_information_additions_edits_and_removals(self):
        legacy={'nodes':[],'relations':[]};current=deepcopy(legacy);current['information_catalog']=deepcopy(self.catalogue)
        delta=model_diff(legacy,current)
        self.assertEqual(len(delta['information_items']['added']),14)
        self.assertEqual(len(delta['information_links']['added']),15)
        changed=deepcopy(current);changed['information_catalog']['items'][0]['definition']='Changed'
        changed['information_catalog']['links'].pop()
        delta=model_diff(current,changed)
        self.assertEqual(len(delta['information_items']['modified']),1)
        self.assertEqual(len(delta['information_links']['removed']),1)

if __name__=='__main__': unittest.main()

from copy import deepcopy
import unittest
from lifecycle import validate_lifecycle, value_hash
from prepare_release import reconcile_decisions
from validate_models import validate_urbanism


class LifecycleTests(unittest.TestCase):
    def setUp(self):
        self.old = {'id':'CAP','revision':1,'fields':{'name':'Name','definition':'Definition'},'review':{'state':'partial'}}
        self.item = deepcopy(self.old)
        self.item['revision'] = 2
        self.item['lifecycle'] = {'state':'urbanist_validated','recorded_at':'2026-09-13T16:00:00Z',
            'source_refs':['U131','U129'],'validated_fields':['name'],'value_sha256':{'name':value_hash('Name')}}
        self.doc = {'schema_version':'1.0.0','version':'old','decisions':[{'id':'ADOPT-1',
            'author':'Laurent','decided_at':'2026-09-11','recorded_at':'2026-09-11','source_refs':['U129'],
            'decision_state':'accepted','interpretation':'explicit','note':'Name only',
            'target':{'collection':'nodes','id':'CAP','revision':1,'approved_fields':['name'],
                'value_sha256':{'name':value_hash('Name')},'import_version':'old'}}]}

    def reconcile(self):
        return reconcile_decisions(self.doc, {'version':'new','as_of':'2026-09-13','nodes':[self.item],'relations':[]},
                                   previous_snapshot={'nodes':[self.old],'relations':[]})

    def test_name_only_validation_does_not_claim_definition(self):
        self.assertEqual(validate_lifecycle(self.item), [])
        result, deferred = self.reconcile()
        self.assertEqual(deferred, [])
        d=result['decisions'][0]
        self.assertEqual(d['target']['approved_fields'], ['name'])
        self.assertEqual(d['author'], 'Laurent')
        self.assertEqual(d['decided_at'], '2026-09-11')
        self.assertEqual(d['target']['revision'], 2)
        self.assertNotEqual(d['id'], 'ADOPT-1')
        self.assertEqual(self.doc['decisions'][0]['target']['revision'], 1)

    def test_changed_name_rejected_as_stale_validation(self):
        self.item['fields']['name']='Other'
        self.assertTrue(validate_lifecycle(self.item))
        result,deferred=self.reconcile()
        self.assertFalse(result['decisions'])
        self.assertTrue(deferred)

    def test_other_business_edit_cannot_hide_in_cycle_migration(self):
        self.item['fields']['definition']='Other'
        result,deferred=self.reconcile()
        self.assertFalse(result['decisions'])
        self.assertTrue(deferred)

    def test_metadata_only_cycle_change_preserves_the_original_scope(self):
        self.old['lifecycle']=deepcopy(self.item['lifecycle'])
        decisions, deferred = self.reconcile()
        self.assertEqual(deferred, [])
        self.assertEqual(decisions['decisions'][0]['target']['approved_fields'], ['name'])
        self.assertEqual(decisions['decisions'][0]['source_refs'], ['U129'])
        self.assertEqual(decisions['decisions'][0]['author'], 'Laurent')

    def test_validated_state_requires_scope(self):
        self.item['lifecycle'].update(validated_fields=[],value_sha256={})
        self.assertTrue(validate_lifecycle(self.item))

    def test_ai_cannot_claim_validation_and_legacy_is_supported(self):
        self.item['lifecycle']['state']='ai_proposed'
        self.assertTrue(validate_lifecycle(self.item))
        self.assertEqual(validate_lifecycle(self.old), [])

    def test_policy_requires_cycle_on_new_elements(self):
        model = {'lifecycle_policy':1,'nodes':[self.old],'relations':[]}
        self.assertTrue(any('required by lifecycle_policy' in e for e in validate_urbanism(model, {})))

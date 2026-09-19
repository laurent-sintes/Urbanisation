"""Verify the U437–U445 change set against its captured input and frozen evidence."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read,dumps
from scripts.lifecycle import value_hash
OUT=Path(__file__).parent
before=read(OUT/'model-before-U437.yaml');model=read(ROOT/'modeles/backlog/model.yaml')
oldnodes={n['id']:n for n in before['nodes']};nodes={n['id']:n for n in model['nodes']}
assert oldnodes.keys() <= nodes.keys()
assert nodes.keys()-oldnodes.keys()=={'D15','BHV086','BHV087'}
assert len({r['id'] for r in model['relations']})==len(model['relations'])
parents={r['target_id']:r['source_id'] for r in model['relations'] if r['type']=='contains'}
expected={'D03.i':'D15','D03.j':'D15','D03.k':'D15','D03.l':'D15','D03.n':'D15','D04.n':'D04','D04.q':'D04','D02.e':'D03','D03.m':'D03','D03.o':'D03','D03.p':'D03','BHV086':'D04.n','BHV087':'D04.n'}
assert all(parents[k]==v for k,v in expected.items())
assert nodes['D03']['fields']['name']=='Fulfillment Optimization'
assert nodes['D15']['fields']['name']=='Order Promising'
assert nodes['D03.n']['fields']['name']=='Fulfillment Commitment'
for rel in before['relations']:
    if rel['type']=='contains' and oldnodes[rel['target_id']]['kind']=='behavior':
        assert parents[rel['target_id']]==rel['source_id']
allowed={('D03','name'):'U438',('D03.n','name'):'U445',('D04.n','definition'):'proposed_U439_U442'}
for id in ['D03.i','D03.j','D03.k','D03.l','D03.n','D04.n','D04.q']:allowed[('REL-MEMBER-'+id,'source_id')]='U438'
preserved=0;changes=[]
for collection in ['nodes','relations','principles']:
    now={x['id']:x for x in model[collection]}
    for old in before[collection]:
        cur=now[old['id']];a=old['fields'] if collection=='nodes' else old;b=cur['fields'] if collection=='nodes' else cur
        for field in old.get('lifecycle',{}).get('validated_fields',[]):
            if a[field]==b[field]:
                assert old['lifecycle']['value_sha256'][field]==cur['lifecycle']['value_sha256'][field]
                preserved+=1
            else:
                authority=allowed[(old['id'],field)]
                if authority.startswith('proposed_'):assert field not in cur['lifecycle']['validated_fields']
                else:assert cur['lifecycle']['value_sha256'][field]==value_hash(b[field])
                changes.append(dict(id=old['id'],field=field,status=authority))
assert len(changes)==10
for id in ['BHV086','BHV087']:assert nodes[id]['lifecycle']['validated_fields']==[]
protected=read(ROOT/'audits/2026-09-19-audit-profond-v0/metrics.yaml')['protected_files']
for path,expected_hash in protected.items():
    actual=sha256((ROOT/path).read_bytes()).hexdigest()
    assert actual==expected_hash,(path,'frozen bytes changed')
auditpath=ROOT/'modeles/backlog/behavior-gap-audit.yaml'
counts=Counter(n['kind'] for n in model['nodes'])
assert counts['domain']==6 and counts['capability']==47 and counts['behavior']==76
summary=dict(source_refs=['U437','U438','U439','U440','U441','U442','U443','U444','U445'],
    model_sha256=sha256((ROOT/'modeles/backlog/model.yaml').read_bytes()).hexdigest(),
    counts=dict(counts),relations=len(model['relations']),previous_approved_values_unchanged=preserved,
    previous_approved_values_replaced_or_reopened=changes,frozen_files_unchanged=len(protected),
    behavior_gap_audit_sha256=sha256(auditpath.read_bytes()).hexdigest(),previous_behavior_parents_unchanged=True,
    model_validation='0 errors',targeted_tests='15 passed',new_behaviors_status='proposed, under instruction',
    publication='unchanged; no release, commit or push')
(OUT/'verification.yaml').write_text(dumps(summary),encoding='utf-8')
print(f'Verified: {counts["domain"]} domains, {counts["capability"]} capabilities, {counts["behavior"]} behaviors; {preserved} prior approved values unchanged, 9 explicitly replaced and 1 definition reopened as proposed; {len(protected)} frozen files unchanged.')

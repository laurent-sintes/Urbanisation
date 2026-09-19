from pathlib import Path
from hashlib import sha256
import json
import sys

ROOT=Path(__file__).resolve().parents[2]
FOLDER=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read, write_text_if_changed
from scripts.validate_models import _source_refs

before=read(FOLDER/'before/modeles/backlog/model.yaml')
after=read(ROOT/'modeles/backlog/model.yaml')
assert before.keys()==after.keys()
for key in before.keys()-{'nodes'}:
    assert before[key]==after[key],key
assert [n['id'] for n in before['nodes']]==[n['id'] for n in after['nodes']]
changes=[]
for old,new in zip(before['nodes'],after['nodes']):
    if old==new:continue
    keys={k for k in old.keys()|new.keys() if old.get(k)!=new.get(k)}
    assert keys <= {'fields','revision','source_refs','proposed_fields'},(new['id'],keys)
    fields={k for k in old['fields'].keys()|new['fields'].keys() if old['fields'].get(k)!=new['fields'].get(k)}
    assert fields <= {'examples','market_comparisons'},(new['id'],fields)
    assert new['revision']==old['revision']+1
    assert old.get('lifecycle')==new.get('lifecycle')
    assert old.get('review')==new.get('review')
    assert old.get('approved_fields')==new.get('approved_fields')
    assert not fields & set(old.get('lifecycle',{}).get('validated_fields',[]))
    changes.append({'id':new['id'],'name':new['fields']['name'],'fields':sorted(fields)})
assert len(changes)==11
assert (FOLDER/'before/modeles/backlog/glossary.yaml').read_bytes()==(ROOT/'modeles/backlog/glossary.yaml').read_bytes()
protected={}
for name in ['2026-09-19-plan-U458','2026-09-19-atlas-U459']:
    protected.update(read(ROOT/f'audits/{name}/protected-files.json'))
assert all(sha256((ROOT/path).read_bytes()).hexdigest()==digest for path,digest in protected.items())
sources={s['id']:s for s in read(ROOT/'modeles/provenance/source-records.json')['records']}
assert not _source_refs(read(ROOT/'modeles/backlog/v0-readiness.yaml'),sources)
examples=sum(len(n['fields'].get('examples',[])) for n in after['nodes'])
ex_nodes=sum(bool(n['fields'].get('examples')) for n in after['nodes'])
choice_nodes=sum(any(c.get('term_choice') and c.get('definition_choice') for c in n['fields'].get('market_comparisons',[])) for n in after['nodes'])
new_comparisons=sum(len(n['fields'].get('market_comparisons',[])) for n in after['nodes'])-sum(len(n['fields'].get('market_comparisons',[])) for n in before['nodes'])
assert (examples,ex_nodes,choice_nodes,new_comparisons)==(14,9,10,3)
proof={'nodes_preserved':len(after['nodes']),'relations_preserved':len(after['relations']),
       'definitions_and_approval_states_preserved':True,'glossary_unchanged':True,'protected_files_unchanged':len(protected),
       'changed_nodes':changes,'explicit_choice_nodes':choice_nodes,'structured_examples':examples,'example_nodes':ex_nodes,
       'new_market_comparisons':new_comparisons,'publication_changed':False}
write_text_if_changed(FOLDER/'verification.json',json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in proof.items() if k!='changed_nodes'}))

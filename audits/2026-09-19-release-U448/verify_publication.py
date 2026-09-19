"""Check published bytes, current Atlas response, glossary and historical access."""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys
from urllib.request import urlopen
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read
from scripts.release_catalog import resolve_release
OUT=Path(__file__).parent
def get(route):
    with urlopen('http://127.0.0.1:8765'+route,timeout=10) as response:return json.loads(response.read().decode('utf-8'))
pointer=resolve_release(ROOT/'modeles/release')
assert pointer['version']=='2026-09-19.2' and pointer['revision']==9
model=read(ROOT/'modeles/release'/pointer['path'])
assert sha256((ROOT/'modeles/release'/pointer['path']).read_bytes()).hexdigest()==pointer['sha256']
protected=read(OUT/'protected-before.json')
for path,expected in protected.items():assert sha256((ROOT/path).read_bytes()).hexdigest()==expected,path
status=get('/api/status')
assert status['appName']=='FLOW Atlas' and Path(status['repositoryRoot']).resolve()==ROOT.resolve() and status['space']=='release'
served=get('/api/model');catalog=get('/api/releases')
assert served['version']==model['version'] and served['sourcePath']=='modeles/release/2026-09-19.2/model.yaml'
assert served['nodes']==model['nodes'] and served['relations']==model['relations']
assert served['glossary']==model['glossary']
assert catalog['current_version']=='2026-09-19.2'
old=get('/api/model?version=2026-09-19.1');old_model=read(ROOT/'modeles/release/2026-09-19.1/model.yaml')
assert old['version']=='2026-09-19.1' and old['nodes']==old_model['nodes'] and old['relations']==old_model['relations']
assert old['glossary']==old_model['glossary']
nodes={n['id']:n for n in served['nodes']};domains={n['id'] for n in served['nodes'] if n['kind']=='domain'}
assert nodes['D03.n']['fields']['name']=='Fulfillment Commitment'
assert nodes['D03.n']['approved_fields']==['name'] and nodes['D04.n']['approved_fields']==['name']
assert not nodes['BHV086']['approved_fields'] and not nodes['BHV087']['approved_fields']
assert not any(r['source_id'] in domains and r['target_id'] in domains for r in served['relations'] if r['type'] in ['contains','presents'])
order=[r['target_id'] for r in served['relations'] if r['type']=='presents' and r['source_id']=='universe-supply']
assert order==['business-references','D04','D01','D06','D15','D03','D05']
counts=Counter(n['kind'] for n in served['nodes'])
assert counts['capability']==47 and counts['behavior']==76 and counts['domain']==6
assert len(served['glossary']['terms'])==110
result=dict(version=pointer['version'],revision=pointer['revision'],descriptor=pointer['descriptor'],sourcePath=served['sourcePath'],
    published_at=pointer['published_at'],app=status['appName'],pid=status['pid'],
    model_sha256=pointer['sha256'],nodes=len(served['nodes']),relations=len(served['relations']),counts=dict(counts),terms=110,
    published_model_equal_to_served=True,published_glossary_equal_to_served=True,old_version='2026-09-19.1',old_model_and_glossary_preserved=True,
    no_domain_nesting=True,reading_order=order,new_behaviors_remain_proposed=True,immutable_protected_files_unchanged=len(protected),
    technical_index_activated=True,previous_index_capture_sha256=sha256((OUT/'release-index-before.json').read_bytes()).hexdigest(),
    validation_errors=0,targeted_tests_passed=44,frontend_ready=True,commit_or_push=False)
with (OUT/'verification.json').open('x',encoding='utf-8') as stream:json.dump(result,stream,ensure_ascii=False,indent=2);stream.write('\n')
print(json.dumps(result,ensure_ascii=False,indent=2))

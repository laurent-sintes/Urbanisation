"""Verify U452 activation, old evidence and the exact Atlas snapshot."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
import sys
import urllib.request
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read
from scripts.release_catalog import resolve_release
OUT = Path(__file__).parent
VERSION = '2026-09-19.3'
protected = read(OUT / 'protected-before.json')
for relative, fingerprint in protected.items():
    assert sha256((ROOT / relative).read_bytes()).hexdigest() == fingerprint, relative
def api(path):
    with urllib.request.urlopen('http://127.0.0.1:8765' + path, timeout=5) as response:
        return json.load(response)
status = api('/api/status')
assert status['appName'] == 'FLOW Atlas' and status['space'] == 'release'
assert Path(status['repositoryRoot']).resolve() == ROOT
pointer = resolve_release(ROOT / 'modeles/release')
assert pointer['version'] == VERSION
model_path = ROOT / 'modeles/release' / pointer['path']
model = read(model_path)
live = api('/api/model')
assert live['version'] == VERSION
assert live['sourcePath'].replace('\\','/').endswith('release/' + VERSION + '/model.yaml')
for field in ('nodes', 'relations', 'glossary'):
    assert live[field] == model[field], field
assert model == read(ROOT / 'modeles/staging' / VERSION / 'candidate.yaml')
old = read(ROOT / 'modeles/release/2026-09-19.2/model.yaml')
assert model['glossary'] == old['glossary']
assert {r['id']:r for r in model['relations']} == {r['id']:r for r in old['relations']}
prior_nodes = {n['id']:n for n in old['nodes']}
assert set(prior_nodes) == {n['id'] for n in model['nodes']}
for node in model['nodes']:
    assert {k:v for k,v in node['fields'].items() if k!='nature'} == {k:v for k,v in prior_nodes[node['id']]['fields'].items() if k!='nature'}
    if 'nature' not in prior_nodes[node['id']]['fields'] and 'nature' in node['fields']:
        assert 'nature' in node['proposed_fields'] and 'nature' not in node['approved_fields']
old_live = api('/api/model?version=2026-09-19.2')
assert old_live['nodes'] == old['nodes'] and old_live['glossary'] == old['glossary']
guide = api('/api/modeling-guide?version=' + VERSION)
assert guide['status'] == 'available' and guide['guide']['version'] == '2026-09-19.1'
previous_guide_index = read(OUT / 'guide-index-before.yaml')
current_guide_index = read(ROOT / 'modeles/modeling-guides/index.yaml')
assert current_guide_index['guides'] == previous_guide_index['guides']
assert current_guide_index['associations'][:-1] == previous_guide_index['associations']
assert current_guide_index['associations'][-1]['publication_version'] == VERSION
catalog = api('/api/releases')
capabilities = [n for n in model['nodes'] if n['kind']=='capability']
behaviors = [n for n in model['nodes'] if n['kind']=='behavior']
assert len(capabilities)==47 and len(behaviors)==76
summary = {'version':VERSION,'revision':model['revision'],'source_path':live['sourcePath'],
    'descriptor':read(ROOT/'modeles/release/index.json')['current'],
    'model_sha256':sha256(model_path.read_bytes()).hexdigest(),
    'protected_files_unchanged':len(protected), 'api_matches_frozen_candidate':True,
    'prior_names_definitions_relations_glossary_unchanged':True,
    'new_types_remain_proposed':True,'previous_publication_accessible':True,
    'guide_version':guide['guide']['version'], 'guide_association_preserved':True,
    'capability_types':dict(Counter(n['fields']['nature'] for n in capabilities)),
    'behavior_types':dict(Counter(n['fields']['nature'] for n in behaviors)),
    'server_pid':status['pid']}
(OUT/'verification.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'release-catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False))

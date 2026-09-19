"""Verify the U450 presentation change and preserve prior business evidence."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
import sys
import urllib.request
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read
out = Path(__file__).parent
protected = read(out / 'protected-before.json')
for relative, fingerprint in protected.items():
    assert sha256((ROOT / relative).read_bytes()).hexdigest() == fingerprint, relative
before = read(out / 'model-before.yaml')
after = read(ROOT / 'modeles/backlog/model.yaml')
assert before['relations'] == after['relations']
old_nodes = {n['id']: n for n in before['nodes']}
assert old_nodes.keys() == {n['id'] for n in after['nodes']}
changed = []
for node in after['nodes']:
    old = old_nodes[node['id']]
    if node == old:
        continue
    assert node['kind'] == 'behavior'
    assert 'nature' not in old['fields']
    restored = json.loads(json.dumps(node))
    restored['fields'].pop('nature')
    assert restored['source_refs'] == list(dict.fromkeys(old['source_refs'] + ['U450', 'U451']))
    restored['source_refs'] = old['source_refs']
    assert restored['proposed_fields'] == list(dict.fromkeys(old.get('proposed_fields', []) + ['nature']))
    if 'proposed_fields' in old:
        restored['proposed_fields'] = old['proposed_fields']
    else:
        restored.pop('proposed_fields')
    assert restored == old, node['id']
    changed.append(node['id'])
assert len(changed) == 76
def api(path):
    with urllib.request.urlopen('http://127.0.0.1:8765' + path, timeout=5) as response:
        return json.load(response)
status = api('/api/status')
assert status['appName'] == 'FLOW Atlas' and status['space'] == 'release'
assert Path(status['repositoryRoot']).resolve() == ROOT
model = api('/api/model')
frozen = read(ROOT / 'modeles/release' / model['version'] / 'model.yaml')
for field in ('nodes', 'relations', 'glossary'):
    assert model[field] == frozen[field], field
guide = api('/api/modeling-guide?version=' + model['version'])
assert guide['status'] == 'available'
result = {'protected_files_unchanged': len(protected), 'behavior_types_added': len(changed),
    'counts':dict(Counter(n['fields']['nature'] for n in after['nodes'] if n['kind']=='behavior')),
    'previous_fields_and_approvals_unchanged':True,'relations_unchanged':True,
    'business_release_unchanged':model['version'], 'api_matches_frozen_snapshot':True,
    'guide_version':guide['guide']['version'],'guide_available':True,'server_pid':status['pid']}
(out / 'verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False))

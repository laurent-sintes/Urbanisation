"""Check the actual served publication and immutable historical inputs."""
from pathlib import Path
from hashlib import sha256
from urllib.request import urlopen
import json,sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read
folder=Path(__file__).resolve().parent
version='2026-09-19.5'
def api(path):
    with urlopen('http://127.0.0.1:8765'+path,timeout=10) as r:return json.load(r)
status=api('/api/status')
assert status['appName']=='FLOW Atlas' and status['space']=='release'
assert Path(status['repositoryRoot']).resolve()==ROOT.resolve()
index=read(ROOT/'modeles/release/index.json')
descriptor=read(ROOT/'modeles/release'/index['current'])
assert descriptor['version']==version and descriptor['revision']==12
frozen=read(ROOT/'modeles/release'/descriptor['path'])
model=api('/api/model')
assert model['version']==version
assert model['sourcePath']=='modeles/release/'+descriptor['path']
for key,value in frozen.items():assert model[key]==value,key
catalog=api('/api/releases')
assert catalog['current_version']==version
guide=api('/api/modeling-guide?version='+version)
assert guide['status']=='available' and guide['guide']['version']=='2026-09-19.2'
old=api('/api/model?version=2026-09-19.4')
assert old['version']=='2026-09-19.4' and 'information_catalog' not in old
protected=read(folder/'protected-files.json')
changed=[p for p,digest in protected.items() if sha256((ROOT/p).read_bytes()).hexdigest()!=digest]
assert not changed,changed
old_index=read(folder/'before/modeles/release/index.json')
assert all(p in index['publications'] for p in old_index['publications'])
old_guide=read(folder/'before/modeles/modeling-guides/index.yaml')
new_guide=read(ROOT/'modeles/modeling-guides/index.yaml')
assert old_guide['guides']==new_guide['guides']
assert all(a in new_guide['associations'] for a in old_guide['associations'])
assert (folder/'before/modeles/backlog/model.yaml').read_bytes()==(ROOT/'modeles/backlog/model.yaml').read_bytes()
result={'status':'passed','version':version,'revision':descriptor['revision'],'published_at':descriptor['published_at'],
 'descriptor':index['current'],'sourcePath':model['sourcePath'],'model_equals_frozen_snapshot':True,
 'nodes':len(model['nodes']),'relations':len(model['relations']),'information':len(model['information_catalog']['items']),
 'information_links':len(model['information_catalog']['links']),'glossary_terms':len(model['glossary']['terms']),
 'guide':guide['guide']['version'],'historical_files_unchanged':len(protected),'backlog_model_unchanged':True,'server_pid':status['pid']}
(folder/'api-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=True))

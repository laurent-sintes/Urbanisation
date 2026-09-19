from pathlib import Path
from hashlib import sha256
import sys,json
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from scripts.structured_io import read
folder=Path(__file__).resolve().parent
assert not (folder/'protected-files.json').exists()
protected={}
for name in ('release','revisions','decisions','provenance','modeling-guides'):
 for p in (ROOT/'modeles'/name).rglob('*'):
  if p.is_file() and p.relative_to(ROOT).as_posix()!='modeles/provenance/source-records.json':protected[p.relative_to(ROOT).as_posix()]=sha256(p.read_bytes()).hexdigest()
(folder/'protected-files.json').write_text(json.dumps(protected,indent=2)+'\n',encoding='utf-8')
for relative in ('modeles/backlog/model.yaml','modeles/backlog/glossary.yaml','modeles/backlog/v0-readiness.yaml'):
 p=folder/'before'/relative;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/relative).read_bytes())
m=read(ROOT/'modeles/backlog/model.yaml');g=read(ROOT/'modeles/backlog/glossary.yaml')
single=[]
for n in m['nodes']:
 c=n['fields'].get('market_comparisons',[])
 if n['review']['state']!='illustration' and len({x['source_url'] for x in c})==1:single.append({'id':n['id'],'name':n['fields']['name'],'definition':n['fields'].get('definition'),'entries':c})
for t in g['terms']:
 c=t.get('market_comparisons',[])
 if len({x['source_url'] for x in c})==1:single.append({'id':t['id'],'name':t['name'],'definition':t['definition'],'entries':c})
(folder/'single-references.json').write_text(json.dumps(single,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(len(protected),'historical files;',len(single),'single-reference records')

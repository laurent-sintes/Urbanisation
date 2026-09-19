"""Record the review priority and preserve a pre-publication integrity baseline."""
from pathlib import Path
from hashlib import sha256
import json, sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read,dumps,write_text_if_changed
folder=Path(__file__).resolve().parent
baseline=folder/'protected-files.json'
assert not baseline.exists(), 'One-shot baseline: never overwrite'
paths=[]
for name in ('release','revisions','decisions','provenance','modeling-guides'):
    paths += [p for p in (ROOT/'modeles'/name).rglob('*') if p.is_file()]
mutable={'modeles/release/index.json','modeles/modeling-guides/index.yaml','modeles/provenance/source-records.json'}
protected={p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths if p.relative_to(ROOT).as_posix() not in mutable}
baseline.write_text(json.dumps(protected,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for path in ('modeles/release/index.json','modeles/modeling-guides/index.yaml','modeles/backlog/model.yaml'):
    out=folder/'before'/path
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_bytes((ROOT/path).read_bytes())
p=ROOT/'modeles/backlog/v0-readiness.yaml'
s=read(p)
s['source_refs']=list(dict.fromkeys([*s['source_refs'],'U469']))
s['status']='base_consolidation_step_by_step_review_U469'
s['execution_U458']['follow_up_U469']={
    'priority':'Consolider la base à partir de la revue pas à pas de Laurent.',
    'information_scope':'Conserver les travaux U468 existants ; extension et généralisation data/information en attente.',
    'release':'Publication locale de l’état courant demandée pour la revue ; aucune validation globale implicite.',
    'next':'Traiter les retours successifs, sans lancer automatiquement les lots de généralisation.',
    'report':'audits/2026-09-19-release-U469/rapport.md'}
write_text_if_changed(p,dumps(s))
print(f'{len(protected)} historical files protected; model content preserved.')

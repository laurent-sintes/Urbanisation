"""Update the execution ledger and check the unchanged publication baseline."""
from pathlib import Path
import sys, json, hashlib
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read,dumps,write_text_if_changed
folder=Path(__file__).resolve().parent
p=ROOT/'modeles/backlog/v0-readiness.yaml'
state=read(p)
state['status']='plan_U458_lot_4_information_contract_and_reader_implemented_pending_release'
state['source_refs']=list(dict.fromkeys([*state['source_refs'],'U468']))
lot=next(x for x in state['execution_U458']['lots'] if x['lot']==4)
lot.update(status='implemented_pending_publication_and_business_review',
           remaining='Contrat canonique et vue transverse implémentés pour les 14 informations pilotes ; intégration à la prochaine release demandée et relecture PO/expert. Aucun accord étendu aux définitions ou règles encore ouvertes.')
state['execution_U458']['follow_up_U468']={
 'report':'audits/2026-09-19-informations-atlas-U468/rapport.md',
 'catalogue':'modeles/backlog/model.yaml#information_catalog',
 'pilot_evidence':'modeles/backlog/information-cards-U465.yaml',
 'status':'implemented_tested_not_published',
 'remaining':'Recette humaine des sens et découpages, autorités et règles métier ouvertes. Généralisation après les pilotes ; pas de réouverture de l’audit U431.'}
write_text_if_changed(p,dumps(state))
protected=json.loads((folder/'protected-files.json').read_text(encoding='utf-8'))
changed=[path for path,digest in protected.items() if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest]
assert not changed,changed
before=read(folder/'before/modeles/backlog/model.yaml')
after=read(ROOT/'modeles/backlog/model.yaml')
assert {k:v for k,v in after.items() if k!='information_catalog'}==before
catalogue=after['information_catalog']
result={'protected_files_unchanged':len(protected),'existing_model_content_unchanged':True,
        'information_count':len(catalogue['items']),'link_count':len(catalogue['links']),
        'capability_roles':sum(len(i['capability_roles']) for i in catalogue['items']),
        'market_references':sum(len(i['market_comparisons']) for i in catalogue['items']),
        'current_descriptor':read(ROOT/'modeles/release/index.json')['current'], 'published':False}
write_text_if_changed(folder/'integrity.json',json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=True))

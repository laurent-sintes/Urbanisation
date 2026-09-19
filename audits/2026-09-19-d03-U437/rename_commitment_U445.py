"""Adopt only the name explicitly accepted in U445 and repair current references."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read,dumps
from scripts.element_versions import content_hash
from scripts.lifecycle import value_hash
path=ROOT/'modeles/backlog/model.yaml';out=Path(__file__).parent/'model-before-U445.yaml'
assert not out.exists();out.write_bytes(path.read_bytes())
before=read(path);model=deepcopy(before);nd={n['id']:n for n in model['nodes']}
stamp=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
cap=nd['D03.n'];cap['fields']['name']='Fulfillment Commitment'
cap['fields']['definition']='Proposer, confirmer et réviser les engagements de satisfaction d’une commande, en quantités, dates et conditions.'
parts=cap['fields']['scope'].split('\n\n')
cap['fields']['scope']='\n\n'.join('U445 adopte le nom Fulfillment Commitment, en remplacement de Promise Management. La définition développée et les contrats restent proposés ; aucun effet de réservation ni réalisation physique déduit du mot Commitment.' if p.startswith('U444 :') else p for p in parts)
cap['lifecycle']['value_sha256']['name']=value_hash(cap['fields']['name'])
cap['lifecycle']['recorded_at']=stamp
cap['lifecycle']['source_refs']=list(dict.fromkeys(cap['lifecycle']['source_refs']+['U445']))
cap['lifecycle']['note']='U445 adopte le nom Fulfillment Commitment ; descriptions et détails restent éditoriaux. L’ancien nom et son accord sont conservés dans audits/2026-09-19-d03-U437/model-before-U445.yaml.'
cap['review']['note']+=' U445 adopte le nouveau nom ; aucune validation globale déduite.'
for n in model['nodes']:
    for field,value in n['fields'].items():
        if isinstance(value,str) and field not in n.get('lifecycle',{}).get('validated_fields',[]):
            if n['id']=='D03.n' and field=='scope':
                value=value.replace('Promise Management répond','Fulfillment Commitment répond')
            else:value=value.replace('Promise Management','Fulfillment Commitment')
            n['fields'][field]=value
nd['D15']['fields']['scope']=nd['D15']['fields']['scope'].replace('L’utilité et la clarté de Fulfillment Commitment font l’objet de U441, sans suppression adoptée.', 'U441/U443 précisent sa distinction d’avec l’affectation ; U445 adopte son nom Fulfillment Commitment.')
nd['BHV043']['fields']['scope']=nd['BHV043']['fields']['scope'].replace('Order Archiving reste en D03','Order Archiving relève de D04 depuis U438')
for cmp in nd['D05.e']['fields'].get('market_comparisons',[]):
    if 'promesse D03' in cmp.get('differences',''):
        cmp['differences']=cmp['differences'].replace('promesse D03','promesse D15')
        cmp['source_refs']=list(dict.fromkeys(cmp.get('source_refs',[])+['U438']))
for r in model['relations']:
    for key,value in r.get('qualification',{}).items():
        if isinstance(value,str):r['qualification'][key]=value.replace('Promise Management','Fulfillment Commitment')
changed=[]
for collection in ['nodes','relations']:
    old={x['id']:x for x in before[collection]}
    for item in model[collection]:
        original=old[item['id']]
        a=original['fields'] if collection=='nodes' else original
        b=item['fields'] if collection=='nodes' else item
        for field in original.get('lifecycle',{}).get('validated_fields',[]):
            if a[field]!=b[field]:assert item['id']=='D03.n' and field=='name',(item['id'],field)
        if item!=original:
            item['revision']+=1;item['last_modified']=stamp
            item['source_refs']=list(dict.fromkeys(item['source_refs']+['U445']))
            if 'content_sha256' in item:item['content_sha256']=content_hash(item)
            changed.append(item['id'])
model['source_version']+=' + U445 Fulfillment Commitment'
for e in model['source_files']:e['sha256']=sha256((ROOT/e['path']).read_bytes()).hexdigest()
path.write_text(dumps(model),encoding='utf-8')
mgp=ROOT/'modeles/backlog/modeling-glossary.yaml';mg=read(mgp)
mod=next(t for t in mg['terms'] if t['id']=='MOD006')
for f in mod['concrete_forms']:f['examples']=[s.replace('Promise Management','Fulfillment Commitment') for s in f['examples']]
mod['source_refs']=list(dict.fromkeys(mod['source_refs']+['U445']));mgp.write_text(dumps(mg),encoding='utf-8')
conv=ROOT/'CONVENTIONS-MODELE.md';text=conv.read_text(encoding='utf-8').replace('Promise Management','Fulfillment Commitment').replace('**Fulfillment Commitment (U288)**','**Fulfillment Commitment (U288/U445)**')
text=text.replace('Depuis U438, Fulfillment Commitment relève de D15 Order Promising ; son identifiant D03.n reste inchangé.', 'Depuis U438, cette capacité relève de D15 Order Promising ; U445 adopte Fulfillment Commitment en remplacement de Promise Management. Son identifiant D03.n et les trois comportements restent inchangés ; le choix de nom ne valide pas les descriptions par extension.')
conv.write_text(text,encoding='utf-8')
p=ROOT/'modeles/backlog/promise-assignment-review-U441.yaml';r=read(p)
r.update(status='clarification_recorded_name_adopted_U445',name='Fulfillment Commitment',name_status='adopted_U445')
r['source_refs'].append('U445');r['naming_U444']['status']='recommended_name_adopted_U445'
r['adoption_U445']=dict(name='Fulfillment Commitment',name_sha256=value_hash('Fulfillment Commitment'),source_refs=['U445'],scope='name only',previous_name='Promise Management',historical_model=out.relative_to(ROOT).as_posix())
p.write_text(dumps(r),encoding='utf-8')
(Path(__file__).parent/'commitment-name-U445.yaml').write_text(dumps(dict(source_refs=['U445'],name_sha256=value_hash('Fulfillment Commitment'),changed=changed,approved_value_replaced='D03.n.name')),encoding='utf-8')
print('Fulfillment Commitment adopted U445; identity D03.n and behaviors preserved.')

"""Finish the reviewed U626 batch and record final deltas against its capture."""
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read,dumps,write_text_if_changed
from scripts.lifecycle import value_hash

model=read(ROOT/'modeles/backlog/model.yaml')
glossary=read(ROOT/'modeles/backlog/glossary.yaml')
meta=read(ROOT/'modeles/backlog/modeling-glossary.yaml')
annex=read(ROOT/'modeles/backlog/model-consolidation-U626.yaml')
nodes={n['id']:n for n in model['nodes']};terms={t['id']:t for t in glossary['terms']}
stamp=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
oracle=deepcopy(terms['TER092']['market_comparisons'][1])
oracle.update(vendor='Oracle',product='Fusion Cloud SCM',source_title='Examples of Consigned Inventory Returns',
    source_url='https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/famml/examples-of-consigned-inventory-returns.html',
    source_version='25D',source_locator='Material Received and Put Away ; Material Consumed',consulted_on='2026-09-22',
    element_name='Consigned inventory returns',concept_name='Consigned inventory returns',
    similarities='La reprise est possible pour des biens reçus non consommés ; les suites diffèrent après consommation et selon l’état de propriété.',
    differences='Oracle regroupe plusieurs cas sous return to supplier ; il ne prescrit pas le nom Pick-up ni les familles de demandes FLOW.',
    evidence_limits='Perspective de consignation fournisseur ; les effets documentés dépendent du statut de consommation. Aucun consensus de terminologie ni installation Beaumanoir déduit.',
    flow_position='Distinguer l’intention de reprise de biens restés consignés du traitement d’un retour après cession.',
    scope_summary='Reprise de stock consigné avant ou après consommation, selon son état.',
    approach_summary='Identifier la situation de propriété avant de déterminer les suites du retour.',source_refs=['ELM624','U600','U611','U626'])
terms['TER092']['market_comparisons'][1]=oracle
terms['TER092']['market_inspiration']['synthesis']=[c['similarities']+' '+c['differences'] for c in terms['TER092']['market_comparisons']]
terms['TER091']['notes']='[Consignment Fill-up Order](model:D04.r) porte la mise en consignation initiale ou complémentaire. Le sens SAP de consignation client et l’apport fournisseur Microsoft éclairent deux perspectives du régime. Le nom et l’extension détaillée de la capacité sont proposés U626 ; aucun achat par le détenteur ne découle de la seule réception.'
terms['TER091']['market_inspiration']['examples'][0]['outcome']=terms['TER091']['notes']
nodes['D04.r']['fields'].update(name='Consignment Fill-up Order',
    definition='Demander et suivre la mise en consignation initiale ou complémentaire de marchandises : produits, quantités, destinations, échéances et reste à apporter, conformément à l’accord applicable.',
    finality='Constituer ou alimenter le stock consigné sans confondre mise à disposition et acquisition par le détenteur.',
    scope='La demande peut porter des biens d’un fournisseur ou donneur d’ordre détenus chez nous, ou nos biens mis à disposition chez un tiers. [Agreement](model:D11) précise propriété, détention, mandat de vente et conditions ; la réception ne suffit pas à transférer la propriété. L’extension aux deux perspectives est une formulation de couverture U626.\n\n[Initial Stocking](model:BHV061) constitue le stock de départ ; [Continuous Replenishment](model:BHV062) alimente le stock pendant l’activité. Les décisions déterminent les besoins, l’Order porte les exigences et son avancement, Supply connaît les apports attendus, Inventory le régime et les positions, Fulfillment les prestations. Les comportements demeurent terminaux.\n\nLe nom Fill-up est attesté chez SAP ; Microsoft emploie Consignment Replenishment Order dans la perspective fournisseur. FLOW qualifie ainsi l’intention de mise en consignation. Vente avec Consignment Issue, reprise par Consignment Pick-up et Return Order après cession gardent des intentions distinctes. Exemple fictif : demander un apport de cinq cents pièces pour une ouverture, suivre les livraisons partielles et conserver le mandat après la fin de la demande d’apport.',
    market_comparisons=deepcopy(terms['TER091']['market_comparisons']))
nodes['D04.r']['fields']['market_inspiration']=deepcopy(terms['TER091']['market_inspiration'])
nodes['BHV061']['fields']['scope']=nodes['BHV061']['fields']['scope'].replace('la demande fournisseur et son suivi','la demande de mise en consignation et son suivi')
if 'D04.t' not in nodes:
    node={'id':'D04.t','revision':1,'kind':'capability','fields':{
        'name':'Consignment Pick-up Order','nature':'management',
        'definition':'Demander et suivre la reprise ou la restitution au propriétaire de marchandises restées consignées, avec les quantités, lieux, échéances et conditions applicables.',
        'finality':'Mettre fin à la mise à disposition des biens concernés sous consignation et rendre leur restitution vérifiable.',
        'scope':'L’intention est de reprendre des biens restés consignés, dans l’une ou l’autre perspective propriétaire/détenteur. Un retour après cession ou consommation reconnue relève du traitement de retour applicable ; le seul trajet entre sites ne transforme pas la demande en Transfer Order.\n\nAgreement porte les conditions, Consigned Inventory Management qualifie les biens et droits, Demand suit la demande et ses engagements, Fulfillment les Tasks de collecte et transport. Les quantités reprises peuvent être partielles ; la clôture de la demande ne prouve pas à elle seule la fin de tous les accords de consignation. Les documents et effets de propriété dépendent du régime applicable. Exemple fictif : restituer cent invendus au propriétaire en deux collectes, sans créer un achat ni traiter ces biens comme un retour après vente.',
        'market_comparisons':deepcopy(terms['TER092']['market_comparisons']),
        'market_inspiration':deepcopy(terms['TER092']['market_inspiration'])},
        'source_refs':['U600','U611','U612','U626'],'source_locator':{'path':'connaissance/01-contributions-utilisateur.md','anchor':'u626'},
        'review':{'state':'proposed','note':'Intention distincte demandée ; nom complet, rédaction et rattachement matérialisés comme proposition U626.'},
        'lifecycle':{'state':'ai_proposed','recorded_at':stamp,'recorded_by':'Codex','source_refs':['U626']},'last_modified':stamp,'adoption_ids':[]}
    model['nodes'].append(node);nodes['D04.t']=node
    model['relations'].append({'id':'REL-MEMBER-D04.t','revision':1,'type':'contains','source_id':'D04','target_id':'D04.t',
        'source_refs':['U611','U626'],'review':{'state':'proposed','note':'Demande distincte de reprise du stock consigné.'},
        'lifecycle':{'state':'ai_proposed','recorded_at':stamp,'recorded_by':'Codex','source_refs':['U626']}})
nodes['D03.p']['fields']['scope']=nodes['D03.p']['fields']['scope'].replace('il ne reconstruit pas le plan amont qui produit les Planned Orders.',
    'il coordonne ses propositions avec les ajustements et apports du plan commun. Une proposition d’achat, de transfert ou de révision de policy est rendue effective par son responsable, sans double création d’Order.')

def live_text(x):
    if isinstance(x,str):
        x=x.replace('Backing Service Order','Service Order').replace('Consignment Replenishment Order','Consignment Fill-up Order')
        for old,new in [('D15','D04'),('D17','D04'),('D05','D03')]:
            x=re.sub(r'\b'+old+r'\b(?!\.[A-Za-z0-9])',new,x)
        return x.replace('proposition d’transfert','proposition de transfert').replace('proposition de achat','proposition d’achat')
    if isinstance(x,list):return [live_text(v) for v in x]
    if isinstance(x,dict):return {k:live_text(v) for k,v in x.items()}
    return x
for n in model['nodes']:
    for key in ['definition','finality','scope','mastership','market_inspiration']:
        if key in n['fields']:n['fields'][key]=live_text(n['fields'][key])
    # FLOW conclusions change; native publisher names in comparison fields do not.
    for c in n['fields'].get('market_comparisons',[]):c['flow_position']=live_text(c['flow_position'])
for t in glossary['terms']:
    for key in ['definition','short_description','notes','context','market_inspiration']:
        if key in t:t[key]=live_text(t[key])
for p in model['principles']:
    if p['id']=='PRINCIPLE-DOMAIN-PURPOSE':
        p['statement']='Domain → Purpose → Capability → Behavior : un Purpose exprime une finalité métier durable ; les référentiels organisent les sujets sans niveau descriptif supplémentaire. Chaque capacité possède un Purpose de rattachement ; les coopérations ne créent pas de second parent. Le code technique area reste compatible ; le libellé de ce niveau est Purpose.'
for t in meta['terms']:
    for key in ['definition','role','notes']:
        if isinstance(t.get(key),str):t[key]=re.sub(r'\bArea\b','Purpose',t[key])
        elif isinstance(t.get(key),list):t[key]=[re.sub(r'\bArea\b','Purpose',v) if isinstance(v,str) else v for v in t[key]]

original=read(HERE/'before/model.yaml')
changes={k:[] for k in ['nodes','relations','terms','metamodel_terms']}
for collection in ['nodes','relations']:
    before={x['id']:x for x in original[collection]}
    for item in model[collection]:
        old=before.get(item['id'])
        if old==item:continue
        values=item if collection=='relations' else item['fields']
        cycle=item.get('lifecycle',{})
        kept=[k for k in cycle.get('validated_fields',[]) if k in values and value_hash(values[k])==cycle.get('value_sha256',{}).get(k)]
        cycle.update(validated_fields=kept,value_sha256={k:cycle['value_sha256'][k] for k in kept})
        if old and cycle.get('state')=='urbanist_validated':cycle['state']='under_instruction'
        item['lifecycle']=cycle;item['last_modified']=stamp
        item['revision']=old.get('revision',0)+1 if old else 1
        item['source_refs']=list(dict.fromkeys(item.get('source_refs',[])+['U626']))
        changed_fields=sorted(k for k in set(values) if k in item.get('fields',{}) and (old or {}).get('fields',{}).get(k)!=item.get('fields',{}).get(k))
        if old:item['proposed_fields']=list(dict.fromkeys(item.get('proposed_fields',[])+changed_fields))
        changes[collection].append({'id':item['id'],'status':'updated' if old else 'created','changed_fields':changed_fields})
for filename,doc,key in [('glossary.yaml',glossary,'terms'),('modeling-glossary.yaml',meta,'metamodel_terms')]:
    before={x['id']:x for x in read(HERE/'before'/filename)['terms']}
    changes[key]=[{'id':t['id'],'status':'updated' if t['id'] in before else 'created'} for t in doc['terms'] if t!=before.get(t['id'])]
annex['changes']=changes
annex['proposed_materializations'] += ['Consignment Fill-up Order : nom qualifié et couverture des deux perspectives','Consignment Pick-up Order : capacité distincte proposée']
annex['preserved_open_points']=['Formulations et rattachements nouveaux : qualification champ par champ avant publication',
    'Évolution détaillée des capacités et comportements de gestion du plan commun',
    'Signal et maille du début d’exécution partielle']
for filename,doc in [('model.yaml',model),('glossary.yaml',glossary),('modeling-glossary.yaml',meta),('model-consolidation-U626.yaml',annex)]:
    write_text_if_changed(ROOT/'modeles/backlog'/filename,dumps(doc))
(HERE/'changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print({key:len(value) for key,value in changes.items()})

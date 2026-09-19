"""Migration explicite des pilotes vers le catalogue métier ; exécution unique."""
from copy import deepcopy
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps, write_text_if_changed

model_path = ROOT/'modeles/backlog/model.yaml'
model = read(model_path)
assert 'information_catalog' not in model
pilot = read(ROOT/'modeles/backlog/information-cards-U465.yaml')
supports = {s['id']:s for s in pilot['market_support']}
vendors = {'MS-PURCHASE':('Microsoft','Dynamics 365 Supply Chain Management'),
           'MS-RECEIPT':('Microsoft','Dynamics 365 Supply Chain Management'),
           'MS-PRODUCT':('Microsoft','Dynamics 365 Supply Chain Management'),
           'GS1-IDENTITY':('GS1','GS1 identification'),
           'FLOW-PROJECTION':('The Open Group','TOGAF Information Mapping'),
           'MARKET-PROMISE':('Microsoft / Oracle','Delivery schedules / Order Management'),
           'MS-ASSIGNMENT':('Microsoft','Dynamics 365 Planning Optimization'),
           'MS-RESERVATION':('Microsoft','Dynamics 365 Inventory Visibility')}
items = []
for card in pilot['cards']:
    support = supports[card['market_comparison']['support_ref']]
    item = {key:deepcopy(card[key]) for key in ['id','name','label_fr','question','definition','context','essential_elements','granularity_rationale','document_and_fact_boundary']}
    item['boundaries'] = deepcopy(card['separate_meanings'])
    item['capability_roles'] = [dict(capability_ref=r['capability_ref'], role=r['role'], meaning=r['meaning'],
                                   source_refs=r['source_refs']) for r in card['capability_roles']]
    item['examples'] = [dict(title='Exemple illustratif', situation=card['example']['text'], source_refs=card['example']['source_refs'])]
    item['source_refs'] = list(dict.fromkeys([*card['source_refs'], 'U468']))
    item['review'] = dict(state='proposed', note='Fiche issue du pilote U465. Définition, granularité, rôles et rapprochements proposés ; exemple illustratif, pas une observation installée.')
    if 'adopted_scope' in card['review']:
        item['review']['note'] += ' U466 adopte seulement la distinction de deux informations reliées, proposition et engagement, avec coexistence possible ; noms, rédaction, versions, cardinalités et autorisations ne sont pas adoptés par extension.'
    item['market_comparisons'] = []
    for src in support['sources']:
        vendor, product = vendors[support['id']]
        if support['id']=='MARKET-PROMISE':
            vendor = 'Oracle' if 'oracle.com' in src['url'] else 'Microsoft'
            product = 'Order Management 26B' if vendor=='Oracle' else 'Dynamics 365 Delivery schedules'
        item['market_comparisons'].append(dict(
            vendor=vendor, product=product, element_name=src['title'], element_type='Concept ou exemple documentaire',
            relationship='Appui méthodologique' if support['id']=='FLOW-PROJECTION' else 'Appui sémantique',
            similarities=support['common_ground'], differences=support['flow_difference'],
            flow_position=card['market_comparison']['definition_choice'],
            term_choice=card['market_comparison']['term_choice'], definition_choice=card['market_comparison']['definition_choice'],
            source_title=src['title'], source_url=src['url'], source_version='Document et passages datés dans le localisateur',
            consulted_on=src['consulted_on'], source_locator=src['locator'], evidence_limits=src['limit'],
            status='proposed', source_refs=list(dict.fromkeys([*support['source_refs'],'CMP184','U468']))))
    items.append(item)
links = []
for link in pilot['links']:
    item = {k:deepcopy(link[k]) for k in ['id','from_ref','to_ref','meaning','condition','effect','source_refs']}
    item['review'] = dict(state='proposed', note='Expression, conditions et effet issus du pilote U465 ; aucune nouvelle règle ou cardinalité implicite.')
    if link['review'].startswith('principle_adopted'):
        item['review']['note'] += ' Le principe de distinction et coexistence est adopté U466, sans adoption des règles détaillées de confirmation.'
    links.append(item)
model['information_catalog'] = dict(id='flow-business-information',
    source_refs=['U464','U465','U466','U468'], items=items, links=links)
write_text_if_changed(model_path, dumps(model))

schema_path = ROOT/'modeles/schemas/urbanism.schema.json'
schema = read(schema_path)
string = {'type':'string','minLength':1}
strings = {'type':'array','minItems':1,'items':string}
refs = dict(strings, uniqueItems=True)
review = {'type':'object','properties':{'state':{'enum':['proposed','under_review']},'note':string},
          'required':['state','note'],'additionalProperties':False}
version_fields = {k:deepcopy(schema['properties'][k]) for k in ['revision','last_modified','content_sha256']}
role = {'type':'object','properties':{'capability_ref':string,'role':string,'meaning':string,'source_refs':refs},
        'required':['capability_ref','role','meaning','source_refs'],'additionalProperties':False}
props = {k:string for k in ['id','name','label_fr','question','definition','context','granularity_rationale','document_and_fact_boundary']}
props.update(essential_elements=strings, boundaries=strings, capability_roles={'type':'array','minItems':1,'items':role},
             examples={'$ref':'#/$defs/businessExamples'}, market_comparisons={'$ref':'#/$defs/marketComparisons'},
             review=review, source_refs=refs)
item_schema = {'type':'object','properties':dict(props,**version_fields),'required':list(props),'additionalProperties':False}
link_props = {k:string for k in ['id','from_ref','to_ref','meaning','condition','effect']}
link_props.update(review=review,source_refs=refs)
link_schema = {'type':'object','properties':dict(link_props,**version_fields),'required':list(link_props),'additionalProperties':False}
schema['$defs']['informationCatalog'] = {'type':'object', 'properties':dict(
    id=string, source_refs=refs, items={'type':'array','items':item_schema}, links={'type':'array','items':link_schema}, **version_fields),
    'required':['id','source_refs','items','links'],'additionalProperties':False}
schema['properties']['information_catalog'] = {'$ref':'#/$defs/informationCatalog'}
write_text_if_changed(schema_path, dumps(schema, '.json'))
print(f'Integrated {len(items)} information cards and {len(links)} links; existing nodes and relations untouched.')

"""U450/U451: preserve snapshots, type behaviors and prepare a new methodology edition."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
from copy import deepcopy
import json
from scripts.structured_io import read, dumps

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent
def write(path, value):
    path.write_text(dumps(value), encoding='utf-8')
def capture(path, name):
    with (AUDIT / name).open('xb') as stream: stream.write(path.read_bytes())

model_path = ROOT / 'modeles/backlog/model.yaml'
method_path = ROOT / 'modeles/backlog/modeling-glossary.yaml'
guide_index_path = ROOT / 'modeles/modeling-guides/index.yaml'
for path, name in [(model_path, 'model-before.yaml'), (method_path, 'modeling-glossary-before.yaml'), (guide_index_path, 'guide-index-before.yaml')]:
    capture(path, name)
protected = {}
for folder in ('release', 'revisions', 'decisions', 'provenance', 'modeling-guides/versions'):
    for path in (ROOT / 'modeles' / folder).rglob('*'):
        if path.is_file() and path.name != 'source-records.json':
            protected[path.relative_to(ROOT).as_posix()] = sha256(path.read_bytes()).hexdigest()
(AUDIT / 'protected-before.json').write_text(json.dumps(protected, indent=2), encoding='utf-8')
model = read(model_path)
before = deepcopy(model)
groups = {
    'decision_dimension': [1,2,3,4,75,76,77],
    'planning_practice': [5,6,16],
    'intervention_mechanism': [17,18,19,20,24,25,44,45,46,47,85,86,87],
    'business_effect': [21,22,23,36,37,38,39,40,43,63,64,65,78],
    'policy_strategy': [29,30,31,32,33,34,35,48,49,83,84],
    'process_variant': list(range(50,63)) + list(range(66,75)),
    'business_scope': [26,27,28,79,80,81,82],
}
by_id = {f'BHV{number:03d}': nature for nature, numbers in groups.items() for number in numbers}
assert sum(map(len, groups.values())) == len(by_id) == 76
assert set(by_id) == {node['id'] for node in model['nodes'] if node['kind'] == 'behavior'}
for node in model['nodes']:
    if node['kind'] != 'behavior': continue
    assert 'nature' not in node['fields']
    node['fields']['nature'] = by_id[node['id']]
    node['source_refs'] += ['U450', 'U451']
    node.setdefault('proposed_fields', []).append('nature')
model['principles'].append({'id': 'PRINCIPLE-BEHAVIOR-NATURE',
    'statement': 'Chaque comportement porte une forme principale explicite dans fields.nature, parmi les formes propres aux comportements de MOD006. Cette forme pilote son icône ; elle n’interdit pas des dimensions complémentaires et ne crée ni niveau supplémentaire ni comportement supplémentaire.',
    'source_refs': ['U450', 'U451']})
for old, new in zip(before['nodes'], model['nodes']):
    assert old.get('lifecycle') == new.get('lifecycle')
    assert old.get('approved_fields') == new.get('approved_fields')
    assert all(new['fields'][key] == value for key, value in old['fields'].items())
assert before['relations'] == model['relations']
write(model_path, model)
write(ROOT / 'modeles/backlog/behavior-types-U451.yaml', {
    'id': 'flow-behavior-types-U451', 'source_refs': ['U450','U451','U435','ELM052','ELM234','CMP170'],
    'definition_ref': 'modeling-glossary.yaml#MOD006', 'field': 'fields.nature',
    'scope': '76 formes principales proposées ; les formes peuvent se combiner. Aucun changement de noms, définitions, parents, comportements ou audit clos U431.',
    'review': {'state':'partial','adopted_scope':'Grille des formes propres aux comportements U451.','proposed_scope':'Qualifications individuelles par Codex, à partir des résultats et exemples de MOD006.'},
    'classification': [{'id': node['id'], 'nature': by_id[node['id']], 'rationale': node['fields']['definition']} for node in model['nodes'] if node['kind']=='behavior'],
    'market_comparison': {'common':'BIZBOK définit le comportement comme une façon d’agir selon les circonstances ; Microsoft illustre des politiques de comptage.',
        'difference':'Les sept formes et les 76 classifications sont une convention FLOW, pas une taxonomie prescrite par ces sources.',
        'consulted_on':'2026-09-19','source_refs':['ELM052','ELM234','CMP170']}})

method = read(method_path)
method['source_refs'] += ['U450','U451']
method['boundary']['links'] = 'Les identifiants MOD appartiennent au méta modèle. Atlas sépare les deux glossaires selon une association méthodologique figée ; les liens TER historiques restent résolus dans leur publication.'
new_terms = [
    ('MOD008','Universe','Univers','Grand périmètre d’urbanisation qui présente des domaines et des groupes de référentiels.','Situer les domaines sans les imbriquer.', ['U141','U446']),
    ('MOD009','Business Reference','Référentiel métier','Ensemble cohérent de données de référence nécessaires aux capacités métier ; dans Supply, projection de sources maîtresses externes.','Distinguer les références des commandes, décisions et réalisations.', ['U450']),
    ('MOD010','Model Relationship','Relation du modèle','Lien explicite décrivant une appartenance, une présentation ou une interaction métier entre éléments.','Distinguer la structure de lecture des échanges et dépendances métier.', ['U450']),
    ('MOD011','Behavior Nature','Type de comportement','Forme qui explique ce qui distingue une manière d’agir au sein d’une capacité.','Rendre lisible la différence entre politique, parcours, mécanisme, périmètre, raisonnement, effet et pratique de planification.', ['U451']),
]
assert not any(t['id'] in {item[0] for item in new_terms} for t in method['terms'])
for identifier, name, label, definition, role, refs in new_terms:
    method['terms'].append({'id':identifier,'name':name,'label_fr':label,'definition':definition,'role':role,'source_refs':refs,
                           'review':{'state':'proposed','proposed_scope':'Formulation méthodologique de présentation ; aucun accord individuel déduit.'}})
write(method_path, method)

partition = ['TER001','TER002','TER024','TER025','TER026','TER027','TER028','TER029','TER030','TER031']
write(ROOT / 'modeles/backlog/glossary-partition-U450.yaml', {
    'id':'glossary-presentation-U450','source_refs':['U450'],'model_term_ids_in_metamodel':partition,
    'rule':'Classement de présentation : identités TER et définitions du snapshot métier conservées ; termes MOD distincts. Aucun déplacement destructif ni fusion des registres.',
    'rationale':'Concepts de structure, réalisation, opérations et coordination du modèle ; les notions Supply restent dans le glossaire métier.'})
guide = read(ROOT / 'modeles/modeling-guides/versions/2026-09-18.1.yaml')
guide['version'] = '2026-09-19.1'; guide['as_of'] = '2026-09-19'
guide['title'] = 'Comprendre le méta modèle'
guide['subtitle'] = 'Six repères pour comprendre la structure du modèle et son vocabulaire.'
guide['source_refs'] += ['U450','U451']
for identifier, excerpt in [('U450','Présenter séparément le glossaire du méta modèle et le glossaire métier ; Comprendre le méta modèle doit être accessible dans Atlas.'),('U451','Les formes propres aux comportements')]:
    guide['sources'].append({'id':identifier,'title':'Présentation Atlas et types de comportements','excerpt':excerpt,
                            'scope':'U450 : synthèse de la demande, pas un verbatim intégral ; U451 : réponse exacte. Sources internes conservées, non affichées dans Atlas.'})
for lesson in guide['lessons']:
    if lesson['id'] == 'useful-detail': lesson['scene']['parent'] = 'Fulfillment Commitment · capacité'
    for link in lesson['model_links']:
        target = next((node for node in model['nodes'] if node['id'] == link['id']), None)
        if target: link['label'] = target['fields']['name']
guide['lessons'][-1] = {
    'id':'two-vocabularies','label':'Deux vocabulaires','title':'Distinguer le méta modèle du modèle métier',
    'rule':'Le méta modèle décrit comment la carte est construite. Le modèle métier décrit les notions et responsabilités de l’entreprise.',
    'established_at':'2026-09-19',
    'scene':{'kind':'objects','caption':'Deux vocabulaires complémentaires, consultables séparément.',
             'items':[{'label':'Méta modèle','text':'Domaine · Capacité · Comportement · Relation'},{'label':'Modèle métier','text':'Stock · Commande · Réservation · Promesse'}]},
    'question':'Où chercher la différence entre une capacité et un comportement ?',
    'choices':[{'label':'Dans le glossaire du méta modèle','feedback':'Il définit les éléments de la carte et leurs relations.'},
               {'label':'Dans le glossaire métier','feedback':'Le glossaire métier explique les notions de l’entreprise, par exemple un stock ou une commande.'}],
    'explanation':'Utilise le glossaire du méta modèle pour comprendre la structure ; utilise le glossaire métier pour comprendre les responsabilités Supply.',
    'contributor':{'criterion':'Décris une notion métier dans le glossaire métier et une règle de construction dans le méta modèle.',
                   'boundary':'Une relation métier ne crée pas une décomposition ; un terme du méta modèle ne devient pas une capacité.',
                   'scope':'Présentation demandée U450 ; formulation pédagogique proposée.', 'source_refs':['U450','U451']},
    'model_links':[]}
terms=[]
forms=next(t for t in method['terms'] if t['id']=='MOD006')['concrete_forms']
for term in method['terms']:
    projected={key:term[key] for key in ('id','name','label_fr','definition','role') if key in term}
    if term['id'] in ('MOD006','MOD011'): projected['examples']=[item['label']+' : '+item['explanation'] for item in forms]
    if term['id']=='MOD007': projected['examples']=[item['label_fr']+' : '+item['definition'] for item in read(ROOT/'modeles/backlog/capability-types-U449.yaml')['types']]
    terms.append(projected)
guide['glossary']={'terms':terms,'model_term_ids':partition}
write(AUDIT/'guide-candidate.yaml',guide)
(AUDIT/'preparation.json').write_text(json.dumps({'behaviors_typed':len(by_id),'counts':dict(Counter(by_id.values())),
 'metamodel_terms':len(terms),'classified_published_terms':len(partition),'protected_files':len(protected),
 'guide_version':guide['version'],'business_release_unchanged':True},indent=2),encoding='utf-8')
print(json.dumps({'behaviors':len(by_id),'counts':dict(Counter(by_id.values())),'glossary':len(terms)+len(partition)}))

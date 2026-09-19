"""Clarify existing promise responsibilities without adopting a replacement name."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read,dumps
from scripts.element_versions import content_hash
path=ROOT/'modeles/backlog/model.yaml'
before=read(path);model=deepcopy(before);nodes={n['id']:n for n in model['nodes']}
out=Path(__file__).parent/'model-before-promise-clarification-U441.yaml'
assert not out.exists();out.write_bytes(path.read_bytes())
stamp=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
promise=nodes['D03.n']
promise['fields']['definition']='Établir et tenir à jour ce que la Supply propose ou s’engage à fournir pour une commande : quelles quantités, à quelles dates et sous quelles conditions, en distinguant la proposition de la promesse confirmée.'
promise['fields']['scope']+='''

U441/U443 : une demande de 100 pièces vendredi peut recevoir une promesse de 60 vendredi et 40 lundi ; la demande et l’engagement de satisfaction restent lisibles séparément. ATP/CTP établissent les possibilités, Delivery Schedule Decision choisit l’échéancier et Fulfillment Plan Decision la cohérence du plan. Promise Proposal formalise les résultats pertinents sans refaire ces arbitrages ; Promise Confirmation établit l’engagement ; Promise Revision tient ses modifications autorisées.

Supply Assignment maintient les liens entre ressources et commandes. Exemple fictif : remplacer l’affectation à l’arrivage A par B, avec mêmes quantités et mêmes conditions de satisfaction, peut préserver la promesse. Inversement, un retard de transport peut imposer de réexaminer la date promise sans changer les ressources affectées. Aucun de ces constats n’autorise à modifier automatiquement l’engagement ; selon U436, seul Reservation bloque les usages concurrents.

Order Firming rend une intention ferme ; il ne confirme pas automatiquement les quantités et dates de satisfaction. Order Preparation & Revision tient le contenu demandé et ses versions ; la présente capacité tient la proposition et l’engagement de satisfaction. Elle ne possède ni un second choix d’échéancier ni l’autorité générale de modifier les Orders. Les conditions d’autorisation et de synchronisation restent à préciser.

U444 : le terme Management est contesté pour sa lisibilité. Le nom actuel reste adopté historiquement en attendant un choix explicite ; des alternatives de nommage sont examinées, sans fusion avec Supply Assignment ni modification de l’accord de domaines U438.'''
nodes['BHV021']['fields']['definition']='Formaliser les quantités, dates et conditions proposées pour satisfaire une commande, à partir des possibilités et arbitrages établis, sans confirmer encore l’engagement.'
nodes['BHV021']['fields']['scope']+='\n\nU441/U443 : ce comportement présente une solution issue des décisions responsables ; il ne recalcule pas un autre plan d’affectation ni un autre échéancier. Une proposition n’est ni un lien d’affectation ni une réservation.'
nodes['D02.e']['fields']['scope']+='\n\nU443 : l’affectation répond à « quelles ressources sont retenues pour cette commande ? » ; Promise Management répond à « quelles quantités et dates sont proposées ou engagées ? ». Une réaffectation peut conserver la promesse, et une révision de date promise peut conserver l’affectation. La compatibilité des deux résultats reste nécessaire, sans identité de responsabilité ni réservation implicite.'
nodes['D01']['fields']['definition']=nodes['D01']['fields']['definition'].replace('mobilisé par Order Backlog Management','mobilisé par Order Promising et Fulfillment Optimization')
for n in model['nodes']:
    original=next(x for x in before['nodes'] if x['id']==n['id'])
    for field in original.get('lifecycle',{}).get('validated_fields',[]):assert original['fields'][field]==n['fields'][field],(n['id'],field)
    if original!=n:
        n['revision']+=1;n['last_modified']=stamp
        n['source_refs']=list(dict.fromkeys(n['source_refs']+(['U438'] if n['id']=='D01' else ['U435','U441','U443','U444'])))
        if 'content_sha256' in n:n['content_sha256']=content_hash(n)
        n['review']['note']+=' Clarification éditoriale ; noms et champs validés conservés.'
for entry in model['source_files']:entry['sha256']=sha256((ROOT/entry['path']).read_bytes()).hexdigest()
path.write_text(dumps(model),encoding='utf-8')
mgpath=ROOT/'modeles/backlog/modeling-glossary.yaml';mg=read(mgpath)
mod=next(t for t in mg['terms'] if t['id']=='MOD006')
for form in mod['concrete_forms']:
    form['examples']=[s.replace('Order Splitting BHV044 relève d’Order Structuring dans D04 (U417).','Order Splitting BHV044 relève d’Order Structuring, déplacée dans D04 en U438 ; son parent de capacité est conservé depuis U417.') for s in form['examples']]
mgpath.write_text(dumps(mg),encoding='utf-8')
review=dict(source_refs=['U441','U443','U444','U435','U436'],status='editorial_clarification_name_open',
    capability_id='D03.n',domain_id='D15',name='Promise Management',name_status='historically_adopted_reexamined_U444',
    responsibility='Proposer, confirmer et réviser l’engagement de satisfaction en quantités, dates et conditions.',
    comparison=[dict(capability='Supply Assignment',result='Liens de ressources retenues pour la commande'),
        dict(capability='Promise Management',result='Proposition et engagement de satisfaction'),dict(capability='Reservation',result='Blocage des usages concurrents selon U436')],
    independence_cases=['Réaffectation A vers B sans changer les quantités et dates promises.', 'Révision autorisée de date promise après retard de transport, avec les mêmes ressources affectées.'],
    boundaries='Ne pas recalculer un second échéancier, choisir un second plan, tenir le contenu demandé à la place des Orders ni créer une réservation implicite.',
    market_support=[dict(vendor='SAP',source_title='Exploring Backorder Processing',source_url='https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe',consulted_on='2026-09-19',finding='La réévaluation des confirmations et des priorités éclaire la responsabilité de révision ; elle ne fixe pas une capacité FLOW ni son nom.'),
        dict(vendor='Oracle',source_title='Key Actions on Orders',source_url='https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faubm/key-actions-on-orders.html',consulted_on='2026-09-19',source_version='25D',source_locator='Attribute Data Simulation Actions ; Release Actions',finding='Les simulations de planning restent distinctes des informations de scheduling visibles au client ; appui à la distinction scénario/engagement, sans équivalence à Supply Assignment.'),
        dict(vendor='Microsoft',source_title='Firm planned orders',source_url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming',consulted_on='2026-09-19',finding='Le firming transforme des ordres planifiés en ordres effectifs. Il ne constitue pas en lui-même une confirmation de satisfaction au sens proposé pour FLOW.')],
    approval_scope='Aucune adoption nouvelle de définition ni de nom ; clarifications éditoriales autorisées U435 et comparaison explicitée à la demande U441/U443/U444.')
(ROOT/'modeles/backlog/promise-assignment-review-U441.yaml').write_text(dumps(review),encoding='utf-8')
print('Promise responsibility clarified; no approved name or value changed; naming choice remains open.')

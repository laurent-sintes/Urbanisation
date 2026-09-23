"""Apply the U626 editorial consolidation once; preserve the exact prior inputs.

Run from the repository root. This is a dated migration, not a second model.
"""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps, write_text_if_changed

HERE = Path(__file__).resolve().parent
BEFORE = HERE / 'before'
if (HERE/'changes.json').exists():
    raise SystemExit('U626 already applied; do not replay a completed migration.')
BEFORE.mkdir(exist_ok=True)
paths = {name: ROOT / 'modeles/backlog' / name for name in (
    'model.yaml', 'glossary.yaml', 'modeling-glossary.yaml', 'modeling-guide-U458.yaml')}
for name, path in paths.items():
    saved = BEFORE / name
    if saved.exists() and saved.read_bytes() != path.read_bytes():
        raise SystemExit('Source changed since capture: '+name)
    if not saved.exists():
        saved.write_bytes(path.read_bytes())
original = {name: read(path) for name, path in paths.items()}
model, glossary, meta, guide = [deepcopy(original[k]) for k in paths]
nodes = {n['id']: n for n in model['nodes']}
terms = {t['id']: t for t in glossary['terms']}
methods = {t['id']: t for t in meta['terms']}
stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
annex = read(ROOT / 'modeles/backlog/orchestration-areas-review-U584.yaml')
consignment = read(ROOT / 'modeles/backlog/consignment-orders-market-review-U595.yaml')
study = read(ROOT / 'modeles/backlog/area-level-market-study-U620.yaml')

def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)

pool = {}
for doc in [model, glossary, annex, consignment, meta]:
    for entry in walk(doc):
        if entry.get('source_url') and entry.get('vendor') and entry.get('similarities'):
            pool.setdefault(entry['source_url'], deepcopy(entry))

def comparison(url, *, common, difference, position, title=None, vendor=None, locator=None, refs=()):
    c = deepcopy(pool.get(url, {}))
    c.update(source_url=url, similarities=common, differences=difference, flow_position=position,
             relationship='Recouvrement partiel', status='proposed')
    c.setdefault('vendor', vendor or 'Source primaire')
    c.setdefault('product', title or c['vendor'])
    c.setdefault('source_title', title or c['product'])
    c.setdefault('source_version', 'Documentation consultée le 22 septembre 2026 ; édition non précisée')
    c.setdefault('source_locator', locator or 'Passage ciblé documenté dans l’audit U625')
    c.setdefault('consulted_on', '2026-09-22')
    c.setdefault('element_name', c['source_title'])
    c.setdefault('element_type', 'Concept documenté par une source primaire')
    c['concept_name'] = c['element_name']
    c['scope_summary'] = common
    c['approach_summary'] = common
    c['evidence_limits'] = difference + ' Aucune réalisation installée Beaumanoir ni équivalence universelle déduite.'
    c['source_refs'] = list(dict.fromkeys(c.get('source_refs', []) + list(refs) + ['U625', 'U626']))
    return c

MS_PO = 'https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-creation'
MS_RETURN = 'https://learn.microsoft.com/en-us/dynamics-gp/distribution/returnsmanagement'
MS_INV = 'https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-on-hand-list'
MS_PLAN = 'https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans'
MS_ALLOC = 'https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation'
ORACLE_ORCH = 'https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauco/overview-of-supply-orchestration.html'
CMMN = 'https://www.omg.org/spec/CMMN/1.1/PDF'
WORKERS = 'https://docs.camunda.io/docs/components/concepts/job-workers/'
FMS = 'https://help.sap.com/docs/SAP_FASHION_MANAGEMENT/3d09d3032a1649f4abf6eea0a8f3ed11/a620215320ce9254e10000000a4450e5.html'
FMS_SOURCE = next(s for s in consignment['sources'] if s['id'] == 'ELM615')
pool.setdefault(FMS, {'vendor':'SAP', 'product':'Fashion Management', 'source_title':FMS_SOURCE['title'],
    'source_version':FMS_SOURCE['edition'], 'source_locator':FMS_SOURCE['locator'], 'consulted_on':'2026-09-22',
    'element_name':'Consignment Orders', 'element_type':'Fonctions de produit', 'source_refs':['ELM615','CMP259']})
consignment_sources = nodes['D04.r']['fields']['market_comparisons']
MS_CONSIGN = next(c['source_url'] for c in consignment_sources if c['vendor']=='Microsoft')
ORACLE_PROVIDER = 'https://docs.oracle.com/en/cloud/saas/readiness/logistics/24a/otm24a/24A-otm-wn-f29771.htm'
provider_proposal = next(x for x in walk(annex) if x.get('name')=='Service Provider Policy' and x.get('market_comparisons'))

def refs(item, values):
    item['source_refs'] = list(dict.fromkeys(item.get('source_refs', []) + list(values) + ['U626']))

def inspiration(fields, situation, outcome):
    cs = fields['market_comparisons']
    fields['market_inspiration'] = {
        'choice': fields.get('finality', fields['definition']),
        'flow_scope': fields['definition'],
        'flow_approach': cs[0]['flow_position'],
        'synthesis': [c['similarities'] + ' ' + c['differences'] for c in cs[:3]],
        'examples': [{'title':'Illustration FLOW', 'situation':situation, 'outcome':outcome,
            'lesson':'Les responsabilités coopèrent ; cet exemple ne décrit pas une installation Beaumanoir.',
            'source_title':cs[0]['source_title'], 'source_url':cs[0]['source_url'], 'source_refs':['U626']}],
    }

def update_term(identifier, *, name=None, definition=None, notes=None, comparisons=None, sources=()):
    t = terms[identifier]
    if name: t['name'] = name
    if definition:
        t['definition'] = definition
        t['short_description'] = definition
    if notes is not None: t['notes'] = notes
    if comparisons is not None: t['market_comparisons'] = comparisons
    t['context'] = 'Supply Chain Orchestration ; distinguer intention, engagement, pilotage, résultat et document.'
    refs(t, sources)
    t['review'] = {'state':'partial', 'note':'Principes issus des décisions citées ; rédaction et comparaisons consolidées U626, sans accord global supplémentaire.'}
    if comparisons is not None:
        inspiration(t, t['definition'], t['notes'])

def add_term(identifier, name, definition, notes, comparisons, sources=()):
    assert identifier not in terms
    t = {'id':identifier, 'name':name, 'short_description':definition, 'definition':definition,
        'context':'Supply Chain Orchestration', 'notes':notes,
        'source_refs':list(sources)+['U626'],
        'source_locator':{'path':'connaissance/01-contributions-utilisateur.md','anchor':'u626'},
        'review':{'state':'proposed','note':'Définition et rapprochements proposés pour transcrire les principes cités ; aucun nouveau type de demande implicite.'},
        'market_comparisons':comparisons}
    inspiration(t, definition, notes)
    glossary['terms'].append(t); terms[identifier]=t

task_position = 'La Task FLOW gouverne la sollicitation et vérifie l’achèvement du service ; le document de commande reste optionnel.'
task_market = [
    comparison(CMMN, title='Case Management Model and Notation 1.1', vendor='OMG', locator='§5.4.10 ; table 5.39, isBlocking',
        common='CMMN distingue le travail associé et la Task qui peut attendre sa fin.',
        difference='Le standard autorise aussi des Tasks non bloquantes ; il ne prescrit pas tout le contrat de pilotage FLOW.',position=task_position,refs=['U617']),
    comparison(WORKERS,title='Job workers',vendor='Camunda',locator='Completing or failing jobs ; retry back off',
        common='Les jobs disposent de tentatives, d’un délai de reprise et d’une complétion explicite.',
        difference='Fin du job et fin de la prestation métier ne sont pas automatiquement identiques ; service de secours à gouverner explicitement.',position=task_position,refs=['U617']),
]
add_term('TER089','Task',
    'Objet de gouvernance qui pilote la sollicitation d’un [Service](glossary:TER075), son suivi et la vérification de son achèvement.',
    'La Task déclenche la sollicitation immédiatement, à une échéance ou sur événement ; elle peut relancer ou mobiliser un service de secours selon les conditions applicables. Elle se termine lorsque la fin du service est vérifiée. Un acquittement technique ne prouve pas cette fin. Elle peut émettre un [Service Order](glossary:TER066) et reste distincte de la demande initiale, du service et de son document.',task_market,['U616','U617'])

service_order_market = deepcopy(terms['TER066']['market_comparisons'])
for c in service_order_market:
    c['flow_position']='Service Order désigne dans FLOW le document éventuel formalisant une sollicitation pilotée par une Task ; le cycle complet de Task ne se déduit pas du document.'
    c['differences'] += ' U616 restreint ici Service Order au document, sans reprendre intégralement le cycle de l’objet de commande du produit.'
update_term('TER066',name='Service Order',
    definition='Document métier qui formalise et qualifie une demande de [Service](glossary:TER075) adressée à un [Service Provider](glossary:TER088), lorsqu’une telle formalisation est nécessaire.',
    notes='La [Task](glossary:TER089) peut produire et transmettre ce document, par exemple un message EDI. Elle porte le pilotage, les reprises et la vérification de fin. Une sollicitation numérique peut être gouvernée sans Service Order. [Purchase Order](glossary:TER070) porte un acte d’achat ; tout Service Order n’en est pas un. Logistic Order est un cas logistique de Service Order.',
    comparisons=service_order_market,sources=['U616','U617'])

update_term('TER072',name='Return Order',
    definition='Demande portant le retour de marchandises et le résultat attendu de leur prise en charge, avec leurs quantités et conditions, indépendamment d’un contexte B2C ou B2B.',
    notes='L’intention de retour peut conduire à remise en stock, réparation, renvoi fournisseur, restitution ou rebut selon l’accord. Un retour après cession de biens consignés peut être pris en charge ici ; la reprise de biens encore consignés relève de [Consignment Pick-up](glossary:TER092). Les parcours ne deviennent pas des familles d’Orders par seul effet juridique.',
    comparisons=deepcopy(nodes['D04.l']['fields']['market_comparisons']),sources=['U612'])
update_term('TER071',definition='Demande de déplacement de marchandises entre sites pour rééquilibrer leur répartition, avec quantités, échéances et contraintes, sans que la propriété du stock détermine à elle seule son type.',
    notes='L’intention prime : mettre en consignation, reprendre du stock encore consigné ou traiter un retour ne deviennent pas Transfer Order du seul fait d’un déplacement. Frontoffice et Backoffice désignent les origines de la demande. Le sens natif de Transfer Order peut être plus large dans les produits.',sources=['U595','U608','U610'])

def consign_comparisons(position, meaning):
    return [comparison(FMS,common=meaning,difference='SAP décrit la consignation client et ses documents. Lecture primaire indexée U600 ; pas de correspondance universelle ni de quatre capacités FLOW imposées.',position=position,refs=['U600','U601','ELM615']),
        comparison(MS_CONSIGN,common='Microsoft distingue l’apport de stock fournisseur consigné et le changement de propriété.',difference='Perspective fournisseur chez le détenteur ; le nom Fill-up ou Pick-up et les effets exacts ne sont pas communs à tous les produits.',position=position,refs=['U595','U600'])]

add_term('TER090','Consignment',
    'Régime dans lequel des marchandises sont détenues chez une autre partie tandis que leur propriété et les droits de vente ou de consommation restent déterminés par l’accord applicable.',
    'Distinguer propriétaire et détenteur. Le modèle couvre nos biens chez un tiers et des biens appartenant à un tiers dans nos entrepôts, avec mandat de vente lorsque l’accord le prévoit. Mise en place, vente, consommation, reprise et retour après cession ne portent pas la même intention ; aucune règle contractuelle universelle n’est déduite.',
    consign_comparisons('Décrire propriété, détention et mandat sans déduire la famille de demande du seul mouvement.','SAP documente la mise à disposition, la cession et la reprise du stock en consignation.'),['U595','U596','U602','U607'])
add_term('TER091','Consignment Fill-up',
    'Mise en consignation initiale ou complémentaire de marchandises conformément à un accord, sans acquisition par le détenteur du seul fait de leur réception.',
    'Nom proposé pour préciser l’intention de D04.r, encore nommé Consignment Replenishment Order dans le catalogue. Le sens SAP de consignation client est rapproché de l’apport fournisseur Microsoft avec leurs perspectives respectives. La formulation détaillée et l’extension bidirectionnelle de la capacité restent proposées.',
    consign_comparisons('Fill-up qualifie la mise en consignation ; ni achat ni simple transfert par défaut.','SAP utilise Consignment Fill-up pour constituer ou compléter le stock consigné chez le client.'),['U600','U601'])
add_term('TER092','Consignment Pick-up',
    'Reprise ou restitution au propriétaire de marchandises restées sous régime de consignation, sans l’assimiler au retour après une vente ou consommation déjà reconnue.',
    'L’intention reste distincte de [Return Order](glossary:TER072) et de [Transfer Order](glossary:TER071). Les prestations de collecte ou de transport passent par les Tasks ; ce terme ne crée pas à lui seul une nouvelle capacité ou un achat de stock.',
    [comparison(FMS,common='SAP distingue Consignment Pick-up de Consignment Return.',difference='Le parcours SAP est celui de la consignation client ; ne pas généraliser ses types de documents à tous les contrats.',position='Distinguer reprise de biens restés consignés et retour après cession.',refs=['U600','U611']),
     comparison(MS_RETURN,common='Les retours ont des suites différentes selon le résultat attendu.',difference='Les RMA/RTV Microsoft ne constituent pas une définition de Pick-up ; appui à la distinction d’intentions seulement.',position='Le rapprochement avec les retours explique la frontière, sans équivalence de vocabulaire.',refs=['U612'])],['U600','U611','U612'])
add_term('TER093','Consignment Issue',
    'Manière de satisfaire une vente en mobilisant du stock consigné avec les effets de cession ou de consommation prévus par l’accord.',
    'Dans FLOW, c’est un comportement de [Sales Order](model:D04.i), identifié par BHV096. L’intention première reste vendre ; l’effet de propriété ne crée pas un Order autonome. Un mandat de vente sur des biens de tiers peut rendre ce comportement pertinent sans achat automatique par le détenteur.',
    consign_comparisons('Consignment Issue précise Sales Order ; aucun Consignment Issue Order autonome.','SAP distingue l’Issue qui constate la cession/consommation de la mise à disposition du stock.'),['U602','U606','U607'])
add_term('TER094','Service Catalog',
    'Référentiel de l’offre de services mobilisables : prestations proposées, fournisseurs, conditions et engagements de service de référence.',
    'Le catalogue décrit l’offre. La [Service Provider Policy](glossary:TER095) précise les règles locales de recours. La capacité opérationnelle contextualisée et les engagements d’une prestation particulière restent distincts des conditions générales annoncées.',
    deepcopy(nodes['D14']['fields']['market_comparisons']),['U590','U616'])
add_term('TER095','Service Provider Policy',
    'Cadre de règles dont le domaine porte la maîtrise pour autoriser, exclure ou limiter le recours à des fournisseurs de services selon le contexte et leur situation opérationnelle.',
    'Exclure un fournisseur ou plafonner de nouvelles sollicitations ne supprime ni son offre au catalogue ni ses engagements déjà acceptés. Une difficulté observée peut justifier une révision selon les autorités prévues ; elle ne constitue pas automatiquement une interdiction. La policy ne modifie pas la capacité physique du fournisseur.',
    deepcopy(provider_proposal['market_comparisons']),['U585','U587','U590'])
resourcing_market = annex['plan_fulfillment_boundary_U592']['market_comparisons']
resourcing_cs=[]
for c in resourcing_market:
    resourcing_cs.append(comparison(c['source_url'],title=c['source_title'],vendor='Fluent Commerce' if 'fluent' in c['source_url'] else 'Oracle',
        locator=c['source_locator'],common=c['similarities'],difference=c['differences']+' '+c['evidence_limits'],
        position='Rechercher une autre source de réalisation pour tout ou partie du besoin ; le contexte distingue arbitrage et reprise en exécution.',refs=['U592','U593']))
add_term('TER096','Re-sourcing',
    'Recherche d’une autre source de réalisation pour tout ou partie d’un besoin, notamment lorsqu’un site ou un service ne peut plus assurer ce qui était prévu.',
    'En cours d’exécution, Fulfillment peut reprendre le seul article manquant depuis un autre entrepôt et suivre les prestations issues du split en lien avec la demande initiale. Le mot ne désigne pas à lui seul une capacité autonome et n’impose pas de recommencer la totalité du plan.',resourcing_cs,['U592','U593'])

for identifier, other in [('TER007','TER055'),('TER055','TER007'),('TER004','TER060'),('TER060','TER004')]:
    terms[identifier]['notes'] = terms[identifier].get('notes','')+'\n\nRepère associé : ['+terms[other]['name']+'](glossary:'+other+'). Le premier libellé conserve son contexte ; ce renvoi ne fusionne pas les notions ni leurs unités.'
    refs(terms[identifier],['U626'])

methods['MOD013']['analysis_ref']='modeles/backlog/area-level-market-study-U620.yaml'
methods['MOD013']['market_comparison']={
    'comparison_ref':'CMP265', 'common':'Les approches étudiées distinguent périmètres, capacités et contribution à des résultats.',
    'difference':'Les neuf approches ne prescrivent pas une même hiérarchie. BMM distingue Goal/Objective, Guild distingue Outcome et Capability ; aucun ne définit le niveau Purpose FLOW.',
    'flow_position':'Purpose / Finalité est la convention FLOW explicitement adoptée U624, sans surcharge de Subdomain DDD.',
    'sources':deepcopy(study['naming_review_U623']['market_sources']),
    'source_refs':['U620','U621','U622','U623','U624','CMP265','U626']}
refs(methods['MOD013'],['U620','U621','U624','CMP265'])
methods['MOD013']['notes'].append('Purpose est un niveau de regroupement ; finality est le champ exprimant le service ou bénéfice attendu d’un élément, y compris à un autre niveau. Une même capacité peut contribuer à plusieurs résultats sans avoir plusieurs parents.')
refs(methods['MOD008'],['U624'])
methods['MOD007']['notes']=[n.replace('Le nom Policy Management peut désigner une Area contenant plusieurs capacités de type Policy ; Area et type de capacité sont deux dimensions distinctes.',
    'Un même Purpose réunit références et policies U618 ; le type Policy qualifie des capacités distinctes des projections et des vues. Purpose, type de capacité et gouvernance des données sont des dimensions distinctes.') for n in methods['MOD007']['notes']]
refs(methods['MOD007'],['U618','U624'])
capability = {'id':'MOD015','name':'Capability','label_fr':'Capacité',
    'definition':'Ce que sait faire durablement l’entreprise, indépendamment de son organisation et de ses outils.',
    'role':'Décrire une aptitude métier au sein d’un Purpose ; ses comportements en précisent les manières d’agir.',
    'notes':['Un produit peut contribuer à plusieurs capacités ; une fonctionnalité ne suffit pas à définir une capacité.',
             'Le glossaire métier TER001 conserve un renvoi historique vers cette autorité méthodologique.'],
    'source_refs':['U33','U624','U626'], 'review':{'state':'partial','note':'Définition U33 conservée ; matérialisation méthodologique et renvois U626 proposés.'},
    'market_comparisons':deepcopy(terms['TER001']['market_comparisons'])}
meta['terms'].append(capability)
for source, identifier, name in [('TER026','MOD016','Capability Realization'),('TER027','MOD017','Function'),('TER028','MOD018','Product Functionality'),('TER029','MOD019','Capability Grouping')]:
    t=terms[source]
    meta['terms'].append({'id':identifier,'name':name,'definition':t['definition'],
        'role':'Autorité méthodologique de la notion ; le terme métier historique conserve son identifiant et un renvoi.',
        'source_refs':t['source_refs']+['U626'], 'market_comparisons':deepcopy(t['market_comparisons']),
        'review':{'state':'proposed','note':'Organisation méthodologique U626 ; sens antérieur conservé.'}})
for identifier, destination in [('TER001','MOD015'),('TER026','MOD016'),('TER027','MOD017'),('TER028','MOD018'),('TER029','MOD019'),('TER030','MOD008')]:
    terms[identifier]['notes'] = terms[identifier].get('notes','')+'\n\nRepère méthodologique : ['+destination+'](modeling:'+destination+'). Cette entrée conserve le vocabulaire historique ; les règles de construction du modèle font autorité dans le glossaire méthodologique.'
    refs(terms[identifier],['U624'])

# Canonical responsibilities and relationships are applied below.
retired = {'D05':'D03', 'D15':'D04', 'D17':'D04'}
names = {'business-references':'Reference & Policy Management', 'D04':'Demand Management',
         'D01':'Inventory Management', 'D03':'Demand & Supply Optimization', 'D06':'Fulfillment Orchestration', 'D18':'Supply Management'}

def new_node(identifier, kind, fields, sources):
    assert identifier not in nodes
    n={'id':identifier,'revision':1,'kind':kind,'fields':fields,'source_refs':list(sources)+['U626'],
       'source_locator':{'path':'connaissance/01-contributions-utilisateur.md','anchor':'u626'},
       'review':{'state':'proposed','note':'Transcription U626 des responsabilités discutées ; formulation et rattachement proposés.'},
       'lifecycle':{'state':'ai_proposed','recorded_at':stamp,'recorded_by':'Codex','source_refs':['U626']},
       'last_modified':stamp,'adoption_ids':[]}
    model['nodes'].append(n);nodes[identifier]=n
    return n

supply_position='Supply Management connaît les apports attendus, leurs quantités, échéances et incertitudes ; Demand conserve les Orders et le plan détermine les adaptations.'
supply_market=[comparison(ORACLE_ORCH,common='Oracle suit les demandes et apports liés aux achats, transferts et autres modes d’approvisionnement.',
    difference='Le produit couvre aussi création et exécution de supply orders ; FLOW sépare connaissance des apports, demande initiale et orchestration.',position=supply_position),
    comparison(MS_INV,common='Microsoft distingue les quantités physiques des réceptions attendues et de la disponibilité calculée.',
    difference='La vue du produit réunit ces mesures ; elle ne définit pas les frontières des Purposes FLOW.',position=supply_position)]
new_node('D18','area',{'name':names['D18'],'market_comparisons':deepcopy(supply_market)},['U584','U595'])
new_node('D18.a','capability',{
    'name':'Supply Visibility','nature':'knowledge','data_governance':'Domain-View',
    'definition':'Rendre visibles les ressources attendues, leurs quantités, lieux, échéances, engagements et incertitudes, en reliant chaque apport à son origine et à son avancement.',
    'finality':'Permettre de planifier la couverture des besoins avec une connaissance fiable des apports à venir.',
    'scope':'Rapprocher achats, transferts entrants, retours et apports sous consignation sans compter plusieurs fois le même flux. Distinguer proposition, apport engagé, expédition et réception ; conserver provenance et fraîcheur. Les Orders restent gérés par Demand ; la réception reconnue alimente Inventory. Une prévision d’arrivée ne crée ni stock physique ni disponibilité certaine. Exemple fictif : un achat de cent pièces expédié à quatre-vingts laisse vingt pièces à confirmer ; la visibilité expose cet écart et les échéances des deux parts.',
    'market_comparisons':deepcopy(supply_market)},['U584','U595','U614'])

provider_fields={k:deepcopy(v) for k,v in provider_proposal.items() if k in ['name','nature','definition','mastership','scope','market_comparisons']}
provider_fields.update(finality='Protéger la réalisation des demandes contre des sollicitations de prestataires inadaptées à leur situation.',data_governance='Domain-managed')
provider_fields['scope']+='\n\nLe [Service Catalog](model:D14) décrit l’offre ; les faits de capacité et de réalisation ne sont pas eux-mêmes des interdictions. Les nouvelles sollicitations respectent les règles retenues ; les engagements déjà acceptés demandent une adaptation explicite. Exemple fictif : limiter temporairement les nouvelles préparations confiées à un prestataire en retard sans effacer ses travaux en cours.'
new_node('D19.a','capability',provider_fields,['U585','U586','U587','U590','U618'])
demand_policy_market=[comparison(MS_ALLOC,common='La protection des groupes peut encadrer les droits de consommation des demandes.',
    difference='Exemple centré sur le stock ; ne couvre pas toutes les politiques de priorité ou de protection des demandes.',position='Séparer les règles de protection des demandes de la décision de priorité et du résultat d’affectation.'),
    deepcopy(nodes['D03.m']['fields']['market_comparisons'][0])]
demand_policy_market[1]['flow_position']='Les critères et protections applicables aux demandes sont gouvernés séparément de leur classement effectif.'
new_node('D19.b','capability',{
    'name':'Demand Protection Policy','nature':'policy','data_governance':'Domain-managed',
    'definition':'Définir, maintenir et rendre applicables les règles qui protègent ou priorisent certaines demandes dans les arbitrages de couverture et de révision.',
    'finality':'Préserver les exigences et engagements des demandes selon le cadre métier applicable.',
    'scope':'Décrire les critères d’éligibilité, protections contre réoptimisation et priorités applicables avec leur portée et validité. [Order Prioritization](model:D03.m) détermine le classement dans la situation considérée. Le plan peut proposer une révision de policy ; sa mise en vigueur respecte l’autorité prévue. Une protection ne réserve pas du stock et ne garantit pas la satisfaction. Exemple fictif : préserver les commandes déjà promises lors d’une campagne, sauf dérogation autorisée avant leur début d’exécution.',
    'market_comparisons':demand_policy_market},['U585','U586','U592','U618'])

purpose_text={
 'business-references':(
    'Fournir les références et les politiques applicables pour interpréter les demandes, connaître les ressources et encadrer les arbitrages et les sollicitations de services.',
    'Disposer d’un contexte commun fiable et d’un cadre de décision applicable à la Supply Chain.',
    'Ce Purpose réunit les sept référentiels existants et les policies du domaine. Les données projetées gardent une vérité externe ; Domain-managed signifie que le domaine porte leur CRUD ; Domain-View qualifie une vue construite et rafraîchie par le domaine. Type de capacité et gouvernance sont indépendants.\n\nLes référentiels Product Reference, Party / Role, Product Catalog, Assortment, Agreement, Fulfillment Network et Service Catalog restent distincts. Les policies gouvernent protection du stock, protection des demandes et recours aux prestataires ; elles ne deviennent pas des référentiels maîtres d’entreprise. Les décisions utilisent ce cadre ou recommandent sa révision ; une simulation ne change pas la version active.\n\nExemple fictif : un prestataire figure au catalogue mais sa policy plafonne les nouvelles sollicitations pendant une difficulté. Son offre de référence, sa capacité opérationnelle et les engagements de prestations déjà acceptés restent distingués.'),
 'D04':(
    'Prendre en charge les besoins et leurs exigences, porter les demandes selon l’intention de leur initiateur et gouverner leur promesse de satisfaction jusqu’à leur conclusion.',
    'Maintenir une réponse explicite aux besoins, avec leurs exigences et engagements de satisfaction.',
    'Ventes, achats, transferts, retours et mise en consignation portent des intentions distinctes, qu’ils proviennent du commerce ou d’un plan Supply. [Demand Planning](model:D17.a) rapproche besoins prévisionnels et demandes connues ; la prévision restante ne double pas les commandes. [Fulfillment Commitment](model:D03.n) porte proposition, confirmation et révision des engagements.\n\n[Demand & Supply Optimization](model:D03) propose les arbitrages et ajustements du contenu des demandes avant leur début d’exécution, y compris pour une demande ferme. Demand gouverne les mutations et leurs effets sur la promesse. Order Release autorise une prise en charge ; sa présence ne prouve pas à elle seule le début effectif des prestations.\n\n[Supply Management](model:D18) suit les apports résultant des demandes ; [Fulfillment Orchestration](model:D06) pilote leur réalisation par des Tasks qui peuvent émettre des Service Orders. Purchase Order reste l’acte d’achat à un fournisseur, y compris de services ; toute sollicitation n’est pas un achat.\n\nExemple fictif : une demande de transfert issue du plan porte un besoin entre deux sites. Le même Order suit les quantités et le résultat attendu ; l’entrée attendue à destination relève de Supply et le déplacement est réalisé par les services mobilisés.'),
 'D18':(
    'Connaître et actualiser les apports de ressources attendus, avec leurs quantités, lieux, dates et degré d’engagement, pour rendre la couverture des besoins planifiable.',
    'Disposer d’une vision fiable des ressources à venir et de leurs incertitudes.',
    'Achats attendus, transferts entrants, retours et mises en consignation peuvent produire des apports. Les Orders restent des demandes gérées par [Demand Management](model:D04), quelle que soit leur origine. Supply relie leurs effets d’apport sans créer un second Order.\n\nUne proposition du plan, une ressource engagée, un flux expédié et une réception ne sont pas équivalents. La réception reconnue alimente [Inventory Management](model:D01), qui construit ses positions et projections à partir des faits et des apports attendus. La maîtrise du calcul de cette vue ne transfère pas celle des faits externes.\n\nExemple fictif : un retour de dix pièces est annoncé ; deux doivent être expertisées. Supply distingue arrivée attendue et ressource potentiellement utilisable. La confirmation du retour ne crée pas dix pièces disponibles en stock.'),
 'D01':(
    'Connaître et fiabiliser les quantités de stock, leurs lieux, états et régimes de détention dans le temps, puis rendre explicites les ressources réservées et les variations reconnues.',
    'Disposer d’une représentation fiable du stock pour décider et exécuter sans double compte.',
    'Mouvements, tracking, inventaires, positions de stock, réservations et régime du stock consigné restent distincts. Propriétaire et détenteur ne se confondent pas. Inventory construit aussi une position projetée à partir des faits et des apports attendus fournis par [Supply Management](model:D18) ; il ne transforme pas une prévision en stock physique.\n\n[Supply Protection](model:D02.b) fournit le cadre de protection depuis Reference & Policy Management ; les arbitrages d’enveloppes ou de couverture relèvent de Demand & Supply Optimization. Seule la réservation bloque les usages concurrents ; une affectation ne la remplace pas.\n\nExemple fictif : soixante pièces sont présentes, quarante annoncées et vingt réservées. La vue distingue chaque mesure, son horizon et sa fraîcheur ; la somme des apports annoncés ne prouve pas une réception.'),
 'D03':(
    'Construire et actualiser un plan commun de couverture des besoins et d’ajustement des ressources, en mobilisant les décisions spécialisées et en faisant appliquer les changements autorisés.',
    'Concilier satisfaction des demandes, disponibilité des ressources et valeur multidimensionnelle dans un plan cohérent.',
    'Les décisions de priorité, affectation, faisabilité, valeur, échéancier, stocks cibles, protections, réassort, redistribution et devenir des retours contribuent au plan commun. ATP, CTP et PTP restent des repères de résultats documentés, sans imposer leur découpage commercial comme architecture. CTP peut examiner de nouveaux apports et des révisions de demandes ou de policies.\n\n[Order Backlog Planning](model:D03.p) et [Inventory Optimization Planning](model:D05.f) apportent leurs travaux complémentaires à ce plan : les affectations retenues et les ajustements de stock doivent rester compatibles. Ils ne maintiennent pas deux plans finaux concurrents. [Demand Planning](model:D17.a) fournit la demande à couvrir, sans se substituer à ce plan de couverture.\n\nL’arbitrage peut modifier le contenu d’une demande tant qu’elle n’est pas en cours d’exécution ; une demande ferme peut être désaffermie selon les conditions applicables. Demand porte les mutations et engagements ; les policies portent la mise en vigueur des règles ; les achats restent des actes de Purchase Order. En cours d’exécution, Fulfillment adapte les prestations et peut effectuer un re-sourcing ciblé. La maille d’un début partiel et son signal doivent être explicités dans le contexte de prise en charge.\n\nExemple fictif : une campagne eCommerce conduit à comparer un apport supplémentaire, une redistribution et une révision de protection B2B. Le plan propose leurs effets conjoints sans rendre automatiquement actives les nouvelles protections ni confirmer une promesse non couverte.'),
 'D06':(
    'Conduire la réalisation des demandes en orchestrant les services requis, leur sollicitation, leurs dépendances, leur suivi et les adaptations nécessaires jusqu’au résultat attendu.',
    'Obtenir la réalisation attendue malgré les aléas, avec une progression et un résultat vérifiables.',
    'Les [Services](glossary:TER075) peuvent être physiques, humains ou numériques. Chaque sollicitation est pilotée par une [Task](glossary:TER089) : activation immédiate, différée ou événementielle, suivi, relance, recours de secours et vérification de fin. Elle peut produire un [Service Order](glossary:TER066), par exemple EDI ; ce document n’est pas obligatoire pour toute sollicitation.\n\nService Catalog fournit l’offre, Service Provider Policy les règles de recours, Service Capacity Visibility la situation opérationnelle. Le choix et l’adaptation des prestations restent distincts de leur coordination. Les exécutants réalisent les opérations physiques ; un acquittement ou un job technique terminé ne suffit pas à constater la fin d’une prestation.\n\nDès le début d’exécution, Fulfillment peut adapter le plan de réalisation. Si un article manque, le re-sourcing peut retenir un autre entrepôt pour ce seul article, répartir les Tasks et les Service Orders nécessaires et conserver le suivi commun de la demande initiale. Si l’engagement devient impossible, Demand gouverne la révision de promesse ; aucun retour automatique de toute adaptation locale au plan global.\n\nExemples fictifs : une Task sollicite une API documentaire sans commande formalisée ; une autre transmet un Service Order de préparation et suit la prestation jusqu’à sa fin vérifiée. Après un manque partiel, seules les quantités concernées font l’objet d’une nouvelle sollicitation.'),
}
for identifier,(definition,finality,scope) in purpose_text.items():
    f=nodes[identifier]['fields'];f.update(name=names[identifier],definition=definition,finality=finality,scope=scope)
    refs(nodes[identifier],['U584','U585','U592','U595','U616','U617','U618','U619','U624'])

# Curate evidence at the finality's own level, then refresh its FLOW interpretation.
nodes['business-references']['fields']['market_comparisons'] = [deepcopy(nodes['business-references']['fields']['market_comparisons'][i]) for i in [0,1,2,3]] + [deepcopy(pool[MS_ALLOC]),deepcopy(provider_proposal['market_comparisons'][0])]
nodes['D04']['fields']['market_comparisons'] = [deepcopy(terms['TER070']['market_comparisons'][0]),deepcopy(terms['TER072']['market_comparisons'][0]),deepcopy(nodes['D15']['fields']['market_comparisons'][1]),deepcopy(nodes['D04']['fields']['market_comparisons'][2])]
nodes['D03']['fields']['market_comparisons'] = deepcopy(nodes['D03']['fields']['market_comparisons']) + deepcopy(nodes['D17']['fields']['market_comparisons'][2:])
nodes['D06']['fields']['market_comparisons'] += deepcopy(task_market)
for identifier in purpose_text:
    f=nodes[identifier]['fields']
    for c in f['market_comparisons']:
        c['flow_position']=f['definition']+' Ce rapprochement soutient une partie de la finalité ; il ne prescrit ni les frontières ni les capacités FLOW.'
        c['status']='proposed';refs(c,['U626'])
    inspiration(f,'Les besoins, les ressources ou les conditions d’exécution évoluent.', f['finality'])

domain=nodes['universe-supply']['fields']
domain['definition']='Organiser la satisfaction des demandes Supply en rapprochant besoins, ressources présentes ou attendues et règles applicables, puis piloter les services nécessaires à leur réalisation et adapter les choix lorsque la situation change.'
domain['finality']='Satisfaire les besoins de la chaîne d’approvisionnement avec des engagements explicites et une utilisation cohérente des ressources.'
domain['scope']='Le Domain articule six finalités : références et policies, demandes, apports attendus, stock, arbitrage du plan et réalisation. Elles coopèrent ; elles ne forment pas six étapes rigides.\n\nDemand porte besoins, exigences et promesses ; Supply connaît les apports à venir ; Inventory représente le stock et ses projections ; Demand & Supply Optimization construit le plan commun ; Fulfillment sollicite et suit les Services au moyen de Tasks. Références et policies partagent un Purpose tout en distinguant vérité externe, CRUD local et vues construites.\n\nLe Domain orchestre les prestations physiques, humaines ou numériques utiles à la Supply ; il ne devient pas un domaine générique de tous les services de l’entreprise. Les exécutants conservent leurs opérations internes, les maîtres externes leurs références d’entreprise et les fonctions commerciales leur périmètre propre. Les processus peuvent traverser ces frontières sans créer de nouveaux niveaux.\n\nExemple fictif : une campagne augmente les demandes. Le domaine compare les ressources et ajustements possibles, fait porter les engagements par les demandes, puis suit leur réalisation, y compris une reprise depuis un autre site pour les seules quantités manquantes.'
for c in domain['market_comparisons']:
    c['flow_position']='FLOW retient la coordination de besoins, ressources, engagements et partenaires au sein du périmètre Supply, sans absorber leurs opérations internes ni imposer le découpage d’un produit.'
inspiration(domain,'Une campagne augmente les besoins tandis qu’un prestataire prend du retard.','Le plan et les réalisations sont adaptés en gardant explicites les engagements et les responsabilités.')
refs(nodes['universe-supply'],['U584','U595','U616','U618','U624'])

nodes['D02.b']['fields']['nature']='policy'
nodes['D07.b']['fields'].update(name='Service Task Management',
    definition='Gouverner les Tasks qui sollicitent des services, depuis leurs conditions d’activation jusqu’à la vérification de leur fin, en tenant les demandes adressées, les réponses et les reprises nécessaires.',
    finality='Assurer une sollicitation robuste et traçable des services jusqu’au résultat attendu.',
    scope='Chaque Task porte la sollicitation d’un service, ses conditions d’activation immédiate, différée ou événementielle, ses réponses et son suivi. Elle peut produire un Service Order pour formaliser la demande. La gestion de ce document et de ses évolutions reste incluse, sans rendre le document obligatoire.\n\nLa Task peut relancer et mobiliser un service de secours dans le cadre applicable. [Process Orchestration](model:D06.d) coordonne les Tasks et leurs dépendances ; [Process Adaptation Decision](model:D06.f) choisit les adaptations ; le tracking fournit les constats. Une relance technique ne doit pas être assimilée à une nouvelle prestation indépendante sans tenir compte du travail déjà accepté ou réalisé.\n\nLa Task se termine lorsque l’achèvement du service est vérifié ; une réponse d’API ou un acquittement EDI ne prouve pas automatiquement la préparation physique. Demand conserve la demande initiale et ses engagements. Exemple fictif : attendre la preuve de fin d’une préparation, constater un manque, puis suivre la sollicitation complémentaire autorisée depuis un autre site.',
    market_comparisons=deepcopy(task_market))
inspiration(nodes['D07.b']['fields'],'Un service de préparation ne répond pas à l’échéance attendue.','La Task suit la reprise autorisée et vérifie le résultat sans confondre réponse technique et prestation achevée.')
refs(nodes['D07.b'],['U616','U617'])
nodes['D01.c']['fields']['definition']='Fournir une lecture cohérente des positions de stock physiques, logiques et projetées, dans les différents lieux et périmètres, avec provenance et fraîcheur, en intégrant les apports attendus sans double compte.'
nodes['D01.c']['fields']['scope']+='\n\n[Supply Visibility](model:D18.a) fournit les apports attendus et leur qualification. Inventory Visibility construit les positions et projections de stock ; les deux vues se relient sans dupliquer la tenue des demandes ni reconnaître une réception avant le fait correspondant.'
for identifier in ['D03.p','D05.f']:
    nodes[identifier]['fields']['scope']+='\n\nCe travail contribue au plan commun de Demand & Supply Optimization. Les scénarios d’affectation et d’ajustement de stock se réconcilient avant leur application ; ils ne constituent pas deux plans finaux indépendants. Le plan peut proposer des apports et des modifications de demandes ou de policies. Leurs responsables rendent les changements autorisés effectifs. Une demande ferme reste révisable avant son début d’exécution ; en cours d’exécution, Fulfillment pilote l’adaptation des prestations.'
nodes['D17.a']['fields']['scope']=nodes['D17.a']['fields']['scope'].replace('Il ne reconstruit pas le plan amont à l’origine des Planned Orders.','Il produit la demande à couvrir pour le plan commun de Demand & Supply Optimization ; la construction des apports et leur arbitrage ne sont pas sa responsabilité.')

new_parents={'D03.n':'D04','D17.a':'D04','D02.b':'business-references',
    **{k:'D03' for k in ['D03.i','D03.j','D03.k','D03.l','D05.f','D05.a','D05.d','D05.e','D05.c','D05.g','D05.h','D05.i']}}
retired_relations=[]
for r in list(model['relations']):
    if r['type']=='presents' and r['target_id'] in retired:
        retired_relations.append(deepcopy(r)); model['relations'].remove(r);continue
    if r['type']=='contains' and r['target_id'] in new_parents:
        r['source_id']=new_parents[r['target_id']]
    if r['source_id'] in retired:r['source_id']=retired[r['source_id']]
    if r['target_id'] in retired:r['target_id']=retired[r['target_id']]

def add_relation(identifier, source, target, kind, meaning=None):
    assert not any(r['id']==identifier for r in model['relations'])
    r={'id':identifier,'revision':1,'type':kind,'source_id':source,'target_id':target,
       'source_refs':['U626'],'review':{'state':'proposed','note':'Rattachement ou coopération explicité U626.'},
       'lifecycle':{'state':'ai_proposed','recorded_at':stamp,'recorded_by':'Codex','source_refs':['U626']},'last_modified':stamp}
    if meaning:r['qualification']={'meaning':meaning,'conditions':['Données disponibles et qualification connue.'],'effects':['Le consommateur conserve la responsabilité de son résultat.'],'source_refs':['U626']}
    model['relations'].append(r)
add_relation('REL-UNIVERSE-SUPPLY-D18','universe-supply','D18','presents')
for identifier,parent in [('D18.a','D18'),('D19.a','business-references'),('D19.b','business-references')]:
    add_relation('REL-MEMBER-'+identifier,parent,identifier,'contains')
add_relation('REL-SUPPLY-INVENTORY-VISIBILITY','D18','D01','provides-knowledge','Fournit les apports attendus pour construire les positions projetées du stock.')
add_relation('REL-SUPPLY-PLAN-VISIBILITY','D18','D03','provides-knowledge','Fournit les ressources attendues, échéances et incertitudes au plan de couverture.')
retired_nodes=[deepcopy(nodes[i]) for i in retired]
model['nodes']=[n for n in model['nodes'] if n['id'] not in retired]

principle_updates={
 'PRINCIPLE-CASE-SUPPLY-ORDERS':'Un Case gouverne le traitement d’une demande ou d’un problème. Dans Fulfillment, une Task pilote chaque sollicitation de Service et peut produire un document Service Order ; demande initiale, Task, prestation et document restent distincts.',
 'PRINCIPLE-TO-PROMISE':'Les décisions ATP, CTP et PTP contribuent au plan dans Demand & Supply Optimization. Demand porte les propositions et engagements de satisfaction. Leur découpage courant n’impose pas une taxonomie commerciale aux Purposes ; CTP peut mobiliser adaptations des apports, demandes et politiques.',
 'PRINCIPLE-EXECUTION-ORCHESTRATION':'Fulfillment orchestre les Services par des Tasks, vérifie leur fin et adapte la réalisation, y compris par re-sourcing. Demand gouverne la promesse ; les exécutants gardent leurs opérations internes. Le début d’exécution distingue modification du contenu de demande par le plan et adaptation des prestations en cours.',
 'PRINCIPLE-EXECUTION-DECISION-AND-COORDINATION':'Visibilité de capacité, choix des prestations, adaptation et coordination restent distincts. Service Task Management gouverne les sollicitations et leurs documents éventuels ; les Tasks peuvent être immédiates, différées ou événementielles, relancées ou orientées vers un service de secours.',
 'PRINCIPLE-CAPABILITY-NATURE':'Chaque capacité porte un type explicite dans fields.nature, indépendant de sa gouvernance. Dans chaque Purpose, les capacités sont regroupées par type avec séparation visuelle ; les décisions sont présentées après les autres types. Cet ordre ne décrit pas une séquence.',
}
for p in model['principles']:
    if p['id'] in principle_updates:p['statement']=principle_updates[p['id']];refs(p,['U592','U616','U617','U624'])
model['principles'].append({'id':'PRINCIPLE-DOMAIN-PURPOSE',
    'statement':'Domain → Purpose → Capability → Behavior : un Purpose exprime une finalité métier durable ; ses références éventuelles organisent les sujets sans ajouter un niveau descriptif. Les capacités ont un Purpose de rattachement ; leurs interactions peuvent contribuer à plusieurs finalités. Le code historique area reste compatible, le libellé courant est Purpose.',
    'source_refs':['U624','U626']})

current_names={n['id']:n['fields']['name'] for n in model['nodes']}
name_changes={nodes[i]['fields']['name']:names[target] for i,target in retired.items()}
name_changes.update({'Authoritative Data':names['business-references'],'Service Requests':names['D04'],
    'Process Management':names['D06'],'Fulfillment Optimization':names['D03'],
    'Backing Service Orders':'Service Task Management'})

def prose(value):
    if not isinstance(value,str):return value
    value=re.sub(r'\[[^\]]+\]\(model:([^)]+)\)',lambda m:'['+current_names.get(retired.get(m[1],m[1]),m[1])+'](model:'+retired.get(m[1],m[1])+')',value)
    value=re.sub(r'\[[^\]]+\]\(glossary:(TER066|TER072)\)',lambda m:'['+terms[m[1]]['name']+'](glossary:'+m[1]+')',value)
    for old,new in name_changes.items():value=value.replace(old,new)
    for old,new in retired.items():value=re.sub(r'\b'+old+r'\b(?!\.)',new,value)
    value=re.sub(r'\bAreas\b','Purposes',value);value=re.sub(r'\bareas\b','purposes',value)
    value=re.sub(r'\bArea\b','Purpose',value);value=re.sub(r'\barea\b','purpose',value)
    value=value.replace('Customer Return Order','Return Order').replace('Customer Return','Return Order')
    return value

def update_flow_text(value):
    if isinstance(value,list):return [update_flow_text(x) for x in value]
    if isinstance(value,dict):
        native={'vendor','product','source_title','source_url','source_version','source_locator','element_name','concept_name','similarities','differences','scope_summary','approach_summary','evidence_limits','term_choice','definition_choice','source_refs','source_locator'}
        return {k:(v if k in native else update_flow_text(v)) for k,v in value.items()}
    return prose(value)

for n in model['nodes']:
    n['fields']=update_flow_text(n['fields'])
for r in model['relations']:
    for key in ['fields','qualification']:
        if key in r:r[key]=update_flow_text(r[key])
for p in model['principles']:p['statement']=prose(p['statement'])
for t in glossary['terms']:
    for key in ['definition','short_description','notes','context']:
        if key in t:t[key]=prose(t[key])
    if 'market_inspiration' in t:t['market_inspiration']=update_flow_text(t['market_inspiration'])
    for c in t.get('market_comparisons',[]):c['flow_position']=prose(c['flow_position'])

# Guide sources preserve verbatim history; only the live lessons and vocabulary move.
guide['lessons']=update_flow_text(guide['lessons'])
for value in walk(guide['lessons']):
    if value.get('id') in retired:value['id']=retired[value['id']]
    if value.get('id') in current_names and 'label' in value:value['label']=current_names[value['id']]
    for key in ['text','label']:
        if value.get(key)=='Inventory Planning':value[key]='Inventory Optimization Planning'
guide['glossary']=update_flow_text(guide.get('glossary',[]))
guide['version']='2026-09-22.2';refs(guide,['U624','U626'])

# Preserve previous approvals as evidence; only unchanged field claims survive.
changes={'nodes':[],'relations':[],'terms':[],'metamodel_terms':[]}
for collection in ['nodes','relations']:
    old_by_id={x['id']:x for x in original['model.yaml'][collection]}
    for item in model[collection]:
        old=old_by_id.get(item['id'])
        if old is None:changes[collection].append({'id':item['id'],'status':'created'});continue
        if item==old:continue
        fields = sorted(k for k in set(old.get('fields',{}))|set(item.get('fields',{})) if old.get('fields',{}).get(k)!=item.get('fields',{}).get(k))
        endpoints=any(old.get(k)!=item.get(k) for k in ['source_id','target_id','type'])
        cycle=deepcopy(old.get('lifecycle',{}));values=item if collection=='relations' else item['fields']
        kept=[k for k in cycle.get('validated_fields',[]) if not endpoints and (old if collection=='relations' else old['fields']).get(k)==values.get(k)]
        cycle.update(state='under_instruction',recorded_at=stamp,recorded_by='Codex',validated_fields=kept,
            value_sha256={k:cycle.get('value_sha256',{})[k] for k in kept},source_refs=list(dict.fromkeys(cycle.get('source_refs',[])+['U626'])),
            note='Consolidation U626 : anciennes preuves conservées dans le registre et la capture avant modification ; seuls champs inchangés rappelés ici. Nouveaux textes et contextes à qualifier.')
        item['lifecycle']=cycle;item['revision']=old.get('revision',0)+1;item['last_modified']=stamp
        refs(item,['U626']);item['review']={'state':'partial','note':'Décisions antérieures transcrites ; nouvelles formulations et contextes proposés U626, sans accord global.'}
        item['proposed_fields']=list(dict.fromkeys(item.get('proposed_fields',[])+fields))
        changes[collection].append({'id':item['id'],'changed_fields':fields,'endpoints_changed':endpoints,'historical_validated_fields_retained':kept})
for name,key in [('glossary.yaml','terms'),('modeling-glossary.yaml','metamodel_terms')]:
    doc=glossary if key=='terms' else meta
    old={x['id']:x for x in original[name]['terms']}
    for t in doc['terms']:
        if t!=old.get(t['id']):changes[key].append({'id':t['id'],'status':'updated' if t['id'] in old else 'created'})
model['as_of']='2026-09-22';model['source_version']+=' + U626 consolidation Domain/Purpose, gouvernance des services et glossaires'
for doc in [glossary,meta]:doc['as_of']='2026-09-22';refs(doc,['U624','U626'])

review={'id':'model-consolidation-U626','date':'2026-09-22','source_refs':['U625','U626'],
    'status':'canonical_draft_updated_detailed_wording_and_context_not_globally_adopted',
    'authorization':'U626 autorise les corrections et compléments ; pas de release ni d’accord sur tous les champs.',
    'applied_principles':['U581 nom Demand & Supply Optimization','U592 frontière début exécution','U595 Demand porte promesse','U616 Service Order document optionnel','U617 Task gouvernance','U618 références/policies ensemble','U619 achat fournisseur','U624 Purpose'],
    'proposed_materializations':['Six Purposes et rattachements détaillés','Supply Visibility','Service Provider Policy : rédaction et rattachement','Demand Protection Policy','Service Task Management : nom de capacité et rédaction','Policy pour Supply Protection','Nouvelles définitions de glossaire'],
    'preserved_open_points':['Consignment Fill-up : nom qualifié documenté, renommage D04.r et extension bidirectionnelle à qualifier','Consignment Pick-up : notion distincte définie, capacité à matérialiser dans le lot Orders','Évolution détaillée des capacités et comportements de gestion du plan commun','Signal et maille du début d’exécution partielle'],
    'retired_purpose_successors':retired,'retired_nodes':retired_nodes,'retired_relations':retired_relations,
    'changes':changes,'before_evidence':'audits/2026-09-22-model-update-U626/before/',
    'market_basis':['audits/2026-09-22-model-scope-U625/marche.md','modeles/backlog/orchestration-areas-review-U584.yaml','modeles/backlog/consignment-orders-market-review-U595.yaml','modeles/backlog/area-level-market-study-U620.yaml']}
write_text_if_changed(ROOT/'modeles/backlog/model-consolidation-U626.yaml',dumps(review))
for name,doc in zip(paths,[model,glossary,meta,guide]):write_text_if_changed(paths[name],dumps(doc))
(HERE/'changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(HERE/'inputs.json').write_text(json.dumps({name:hashlib.sha256((BEFORE/name).read_bytes()).hexdigest() for name in paths},indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:len(v) for k,v in changes.items()}))

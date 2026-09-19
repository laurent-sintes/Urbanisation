"""Compléments éditoriaux ciblés ; aucun renommage ou nouvel accord implicite."""
from pathlib import Path
from copy import deepcopy
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps, write_text_if_changed

schema_path = ROOT / 'modeles/schemas/urbanism.schema.json'
schema = read(schema_path)
for field in ['term_choice', 'definition_choice']:
    schema['$defs']['marketComparisons']['items']['properties'][field] = {'type':'string','minLength':1}
schema['$defs']['businessExamples'] = {
    'type':'array','minItems':1,'items':{'type':'object','properties':{
        **{key:{'type':'string','minLength':1} for key in ['title','situation','outcome','lesson']},
        'source_refs':{'type':'array','minItems':1,'uniqueItems':True,'items':{'type':'string','minLength':1}}},
        'required':['title','situation','source_refs'],'additionalProperties':False}}
schema['$defs']['node']['properties']['fields']['properties']['examples'] = {'$ref':'#/$defs/businessExamples'}
write_text_if_changed(schema_path,dumps(schema,'.json'))

path = ROOT / 'modeles/backlog/model.yaml'
model=read(path)
before=deepcopy(model)
nodes={n['id']:n for n in model['nodes']}

def example(title,situation,outcome,lesson,*refs):
    return dict(title=title,situation=situation,outcome=outcome,lesson=lesson,source_refs=list(refs)+['U462'])

examples={
 'D04.o':[
  example('Réviser une partie sans effacer la version applicable','Une commande de 100 pièces est ferme et 60 pièces sont libérées. Une révision prépare le report de la date demandée des 40 autres pièces.','Tant que cette révision n’est pas applicable, la version en vigueur demeure la référence ; aucune suspension des 60 pièces n’est implicite.','Préparation, engagement ferme, autorisation de traitement et suspension sont des dimensions distinctes. Les réalisations acquises ne sont pas réécrites.','U424')],
 'D03.n':[
  example('Demander 100 vendredi, promettre en deux temps','Une commande demande 100 pièces vendredi.','La proposition porte sur 60 vendredi et 40 lundi ; la confirmation établit les quantités et dates engagées selon les autorisations applicables.','La demande, la proposition et l’engagement restent lisibles séparément. Confirmer ne réserve pas automatiquement les ressources.','U441','U443','U436'),
  example('Même promesse, autre ressource','40 pièces étaient affectées à l’arrivage A ; l’arrivage B offre les mêmes conditions de satisfaction.','L’affectation peut passer de A à B sans changer l’engagement. Inversement, un retard de transport peut conduire à réexaminer la date promise avec la même ressource.','Fulfillment Commitment et Supply Assignment répondent à deux questions distinctes.','U443')],
 'D02.e':[
  example('Répartir une pénurie sans scinder les commandes','Deux commandes demandent 100 et 200 pièces ; 150 pièces sont disponibles.','Un scénario de prorata donne 50 et 100 pièces affectées. Les demandes restent de 100 et 200.','Cet exemple de Spread ne scinde pas les commandes et ne prescrit pas le prorata : priorités, quotas et engagements peuvent conduire à un autre résultat.','U362','U363'),
  example('Affecter ne réserve pas','40 pièces d’un arrivage sont affectées à une commande.','Le lien indique la ressource retenue ; il ne bloque pas, à lui seul, les usages concurrents.','Seule Reservation porte cet effet opposable dans FLOW.','U436','U443')],
 'D02.c':[
  example('Réserver avant de choisir le lot','Un besoin identifié obtient un droit exclusif sur 40 pièces d’un périmètre de ressource.','Les usages concurrents doivent en tenir compte, même si le lot précis est affecté plus tard.','Réservation, affectation du lot et mouvement physique restent distincts.','U436','U460')],
 'D04.j':[
  example('Réception partielle : rendre visible le reliquat','100 pièces sont attendues ; 60 sont réellement reçues.','Le rapprochement explique les 40 restantes. Le fait de réception est associé à un document identifié, qui peut être structuré sans PDF.','Une confirmation fournisseur ne prouve pas la réalisation.','U391','U461'),
  example('Le fournisseur propose un autre échéancier','100 pièces sont demandées vendredi ; le fournisseur propose 60 vendredi et 40 mardi.','Sa réponse doit être distinguée de la demande et des conditions acceptées.','Accepter sa réponse ne modifie pas automatiquement notre promesse client ; refuser son report ne restaure pas sa capacité.','U403','U443')],
 'D04.n':[
  example('Scinder','100 pièces doivent être traitées en deux parties.','La structure peut distinguer 60 et 40 en préservant la filiation et les quantités.','Cela ne présume pas deux commandes commerciales autonomes.','U362','U363','U439'),
  example('Regrouper en conservant les identités','Deux transferts contribuent à l’ouverture d’un magasin.','Ils sont reliés pour un traitement coordonné, tout en restant deux commandes distinctes.','Regrouper ne signifie pas fusionner.','U440','U442'),
  example('Fusionner des demandes compatibles','Deux achats encore modifiables portent sur 30 et 20 pièces.','Sous les conditions de compatibilité et d’autorisation applicables, une demande résultante peut porter les 50 pièces.','La fusion n’est pas applicable par défaut à tous les états et types de commandes.','U442')],
 'D05.a':[
  example('Choisir où porter le stock de sécurité','Un même réseau comprend un entrepôt et plusieurs magasins.','La décision compare une sécurité davantage portée par l’entrepôt à une sécurité répartie en magasins selon le réassort et le service attendu.','L’objectif est un ensemble cohérent de cibles, sans centralisation systématique ni baisse garantie du stock total.','U331','U332')],
 'D08':[
  example('Une variante, plusieurs offres et plusieurs exemplaires','Un tee-shirt bleu taille M est proposé dans deux catalogues ; deux pièces physiques de cette variante sont présentes.','Les catalogues peuvent partager la référence de variante. Les deux pièces restent deux Product Units.','La référence, l’offre et l’exemplaire physique ne sont pas la même chose.','U191','U193','U202','U460')],
 'D08.d':[
  example('Recevoir une variante avant sa mise au catalogue','Les caractéristiques taille et couleur d’une variante sont reçues depuis leur source externe.','Supply actualise sa projection, même si la variante n’est pas encore proposée dans un catalogue.','Recevoir l’information ne transfère pas à Supply l’administration du maître produit.','U202','U290','U460')]
}
for identifier,items in examples.items():
    assert 'examples' not in nodes[identifier]['fields']
    nodes[identifier]['fields']['examples']=items

def comparison(name,url,locator,similarities,differences,position,version,refs,vendor='Microsoft',product='Dynamics 365 Supply Chain Management'):
    return dict(vendor=vendor,product=product,element_name=name,element_type='Concept ou fonction produit',relationship='Appui lexical et recouvrement partiel',
        similarities=similarities,differences=differences,flow_position=position,source_title=name,source_url=url,source_version=version,
        source_locator=locator,consulted_on='2026-09-19',evidence_limits='Source primaire consultée ; aucune équivalence complète de taxonomie ni réalisation installée déduite.',status='proposed',source_refs=refs+['U462'])

nodes['D03.n']['fields']['market_comparisons'].append(comparison(
 'Confirm sales orders','https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/tasks/confirm-sales-orders',
 'Confirm a single sales order ; Confirm multiple sales orders','Une confirmation est formalisée et peut donner lieu à un document.',
 'La confirmation de commande décrite ne couvre pas à elle seule la proposition et la révision de satisfaction FLOW.',
 'Le nom Fulfillment Commitment exprime l’engagement de satisfaction ; il ne désigne pas une simple confirmation documentaire.',
 'Documentation évolutive ; mise à jour affichée le 1er juillet 2026',['U444','U445','ELM286','CMP179']))
nodes['D02.e']['fields']['market_comparisons'].append(comparison(
 'Explaining Supply Assignment','https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4',
 'Supply Assignment (ARun) ; Supply Assignment Scenarios','Le terme relie explicitement ressources et demandes de commandes.',
 'Le scénario SAP crée aussi un lien qui empêche la satisfaction d’une autre demande. FLOW sépare cet effet dans Reservation.',
 'Reprise du vocabulaire Supply Assignment avec une frontière FLOW propre : l’affectation seule ne bloque pas les usages concurrents.',
 'Cours SAP S/4HANA Fashion évolutif ; édition unique non affichée',['U289','U290','U436','ELM287','CMP180'],vendor='SAP',product='S/4HANA Fashion — Supply Assignment (ARun)'))
nodes['D04.j']['fields']['market_comparisons'].append(comparison(
 'Purchase order overview','https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-overview',
 'Introduction ; Purchase order status','Purchase Order est employé pour un achat de biens ou de services.',
 'La source décrit notamment un document et ses états ; FLOW nomme aussi une capacité métier, distincte de cet objet.',
 'Le nom court Purchase Order désigne ici la prise en charge métier des achats ; il ne transforme pas le document en capacité.',
 'Documentation évolutive ; édition produit non figée',['U384','U391','ELM288','CMP181']))

# Explication des arbitrages déjà discutés, rattachée à la comparaison qui l’éclaire.
choices={
 'D03':('Distributed order management (DOM)',
  'Fulfillment Optimization nomme le problème métier : arbitrer la satisfaction des commandes. Backlog désigne le carnet travaillé, mais ne suffit pas à délimiter cette responsabilité.',
  'Le domaine regroupe priorités, plan, Planning et affectations. Order Promising conserve possibilités et engagements ; Order Management conserve structure, cycle et archivage. Le découpage FLOW n’est pas celui du produit DOM.', ['U437','U438']),
 'D15':('Order promising',
  'Order Promising reprend un terme établi pour la promesse de satisfaction, également documenté chez Microsoft ; il évite de nommer le domaine par le seul objet Backlog.',
  'FLOW distingue possibilités ATP/CTP/PTP, échéancier et engagement de satisfaction. L’optimisation collective et les affectations relèvent du domaine voisin Fulfillment Optimization.', ['U437','U438']),
 'D03.n':('Confirm sales orders',
  'Fulfillment Commitment rend explicite l’engagement de satisfaction. Promise Management était trop vague ; Promise Confirmation trop étroit pour inclure proposition et révision. Order Confirmation peut désigner la confirmation documentaire. Aucun terme unique de marché couvrant exactement cette responsabilité n’est établi ici.',
  'La définition rassemble proposer, confirmer et réviser les quantités, dates et conditions. Elle laisse les calculs de faisabilité, le choix d’échéancier, l’affectation et la réservation à leurs responsabilités.', ['U441','U443','U444','U445']),
 'D02.e':('Explaining Supply Assignment',
  'Supply Assignment rend explicite l’affectation des ressources aux commandes. Le terme Allocation seul est ambigu entre affectation et droits de groupes ; les appellations éditeurs restent qualifiées.',
  'FLOW maintient les liens ressources–commandes et sépare le blocage concurrent dans Reservation. Le vocabulaire commun avec SAP ne signifie donc pas identité d’effet métier.', ['U275','U289','U290','U436']),
 'D02.c':('Inventory Visibility reservations',
  'Reservation désigne l’engagement de ressource dont les autres demandes doivent tenir compte ; le nom permet de le distinguer de l’affectation et de la promesse.',
  'FLOW retient explicitement l’effet opposable sur les usages concurrents. Les types Microsoft et leurs mécanismes techniques ne deviennent pas automatiquement des types FLOW.', ['U436']),
 'D04.n':('What’s a Split Order Line',
  'Order Splitting suffirait pour la seule scission. Order Structuring couvre aussi le regroupement qui conserve les identités et la fusion de demandes compatibles ; ce regroupement de responsabilités est un choix FLOW.',
  'Scission, regroupement et fusion ont des effets distincts. Le cas Oracle éclaire la scission ; il ne prouve pas à lui seul un standard couvrant les trois comportements.', ['U439','U440','U442']),
 'D05.a':('Safety stock journals — Calculate a proposal',
  'Inventory Target Decision nomme le résultat métier : déterminer les cibles et seuils de stock. Decision inclut les calculs nécessaires ; un niveau Calculation séparé n’apporterait pas une responsabilité supplémentaire.',
  'FLOW décrit la détermination des cibles, indépendamment des journaux et paramètres d’un produit. Apports, redistribution et affectation restent des décisions ou actions distinctes.', ['U328','U329']),
 'D04.j':('Purchase order overview',
  'Purchase Order reprend le vocabulaire établi de la commande d’achat. Le nom court a été retenu pour cette capacité d’action, tout en conservant un objet métier homonyme distinct.',
  'La capacité maintient les attentes de biens ou prestations et rapproche leurs réalisations. La définition dépasse le document seul sans absorber négociation contractuelle, facturation ou exécution physique.', ['U384','U391']),
 'D08':('Product information overview',
  'Product Reference met l’accent sur des références partagées, distinctes des offres de catalogue et des exemplaires physiques.',
  'Le choix FLOW est une projection des maîtres externes. Le vocabulaire produit/variante est éclairé par Microsoft ; l’administration des maîtres reste hors de cette responsabilité.', ['U134','U191','U193','U202']),
 'D08.d':('Exchange data between systems',
  'Ingestion précise l’action attendue : recevoir les informations de référence et leurs évolutions.',
  'Recevoir une information et l’administrer comme maître sont deux responsabilités différentes. L’autorité métier ne se déduit pas du seul émetteur.', ['U134','U290','U460'])
}
for identifier,(name,term,definition,refs) in choices.items():
    entries=nodes[identifier]['fields']['market_comparisons']
    entry=next(e for e in entries if e['element_name']==name)
    entry['term_choice']=term
    entry['definition_choice']=definition
    for ref in refs+['U462']:
        if ref not in entry['source_refs']: entry['source_refs'].append(ref)
for old in before['nodes']:
    node=nodes[old['id']]
    changed=[key for key in node['fields'] if old['fields'].get(key)!=node['fields'][key]]
    if not changed:continue
    assert not set(changed)&set(node.get('lifecycle',{}).get('validated_fields',[]))
    assert not set(changed)&set(node.get('approved_fields',[]))
    node['revision']+=1
    node['source_refs'].append('U462')
    for field in changed:
        if 'proposed_fields' in node and field not in node['proposed_fields']: node['proposed_fields'].append(field)
write_text_if_changed(path,dumps(model))
print(f'{len(choices)} choix de terme/définition, {sum(map(len,examples.values()))} exemples sur {len(examples)} fiches ; 3 comparaisons ajoutées.')

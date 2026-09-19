"""Record the D03 review and only apply already-established editorial boundaries."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps
from scripts.element_versions import content_hash

OUT = Path(__file__).parent
PATH = ROOT / 'modeles/backlog/model.yaml'
BASE = OUT / 'model-before-U437.yaml'
assert not BASE.exists(), 'This recording must only run once.'
BASE.write_bytes(PATH.read_bytes())
model = read(PATH)
before = deepcopy(model)
nodes = {n['id']: n for n in model['nodes']}
stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

domain = nodes['D03']
domain['fields']['definition'] = ('Travailler collectivement le carnet d’Orders Supply pour prioriser les demandes, '
    'évaluer leurs possibilités de satisfaction, construire les scénarios d’affectation et préparer la satisfaction '
    'retenue, en mobilisant les capacités responsables des engagements et de l’autorisation de prise en charge '
    'par les processus, et en préservant le sens des demandes.')
old = 'préparer les découpages et regroupements utiles et autoriser la prise en charge retenue.'
new = ('préparer les découpages et regroupements utiles et mobiliser Order Lifecycle Management '
       'pour autoriser la prise en charge retenue.')
assert old in domain['fields']['scope']
domain['fields']['scope'] = domain['fields']['scope'].replace(old, new, 1)
domain['review']['note'] = ('Nom adopté U413 ; rattachements actuels issus de U417/U420. U437 réexamine la structuration '
    'et les recouvrements : proposition à deux domaines dans d03-domain-review-U437.yaml, sans adoption ni déplacement. '
    'Correction éditoriale sous U435 : l’autorisation de prise en charge reste à Lifecycle D04.o conformément à U420. '
    'Définition développée et comparaisons restent proposées.')

assignment = nodes['D02.e']
assignment['fields']['definition'] = ('Matérialiser et maintenir les affectations des ressources Supply présentes ou futures '
    'aux commandes identifiées, en mobilisant les décisions responsables des choix retenus et en respectant les '
    'priorités, les engagements et les contraintes applicables.')
assignment['fields']['finality'] = ('Maintenir des liens d’affectation cohérents entre ressources et commandes pour '
    'concrétiser les choix de satisfaction retenus.')
assignment['review']['note'] += (' U437 sous autorisation U435 : définition et finalité alignées sur l’application '
    'des choix ; l’optimisation collective reste à Fulfillment Plan Decision selon U378. Aucun changement de parent '
    'ni des effets de réservation U436.')

source_limits = ('Page primaire consultée le 19 septembre 2026 ; comparaison documentaire proposée, '
    'sans taxonomie de capacités adoptée ni preuve de réalisation installée. Les Orders FLOW ont un périmètre plus large '
    'que les cas de vente et de transfert documentés. Synthèse originale, sans reproduction du contenu éditeur.')
def comparison(vendor, product, title, url, version, locator, similarities, differences, position):
    return dict(vendor=vendor, product=product, element_name=title, element_type='Fonction et périmètre produit',
        relationship='Recouvrement partiel', similarities=similarities, differences=differences,
        source_title=title, source_url=url, source_version=version, source_locator=locator,
        flow_position=position, consulted_on='2026-09-19', evidence_limits=source_limits,
        status='proposed', source_refs=['U437'])

comparisons = [
    comparison('SAP', 'SAP S/4HANA Cloud Public Edition', 'Exploring Backorder Processing',
        'https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe',
        'Leçon évolutive, édition précise non affichée', 'Discovering Order Promising ; Introduction ; Backorder Processing Overview',
        'Réexaminer disponibilités, priorités et confirmations après un changement de ressources ou de demandes.',
        'BOP réunit plusieurs responsabilités FLOW ; sa leçon cible ventes et transferts. Order Promising ne se limite donc pas à une demande isolée.',
        'Appui à la lecture promesse et à son articulation avec l’optimisation ; ne démontre pas une séparation obligatoire en deux domaines.'),
    comparison('Microsoft', 'Dynamics 365 Commerce', 'Distributed order management (DOM)',
        'https://learn.microsoft.com/en-us/dynamics365/commerce/dom',
        'Documentation évolutive, mise à jour affichée 2026-06-03', 'In this article ; présentation de DOM',
        'Choisir les sources de satisfaction sous contraintes et objectifs de coût et de service, pour une commande ou un ensemble.',
        'Solution omnicanale ; son périmètre logiciel ne fixe ni les parents FLOW ni toutes les responsabilités de tenue des engagements.',
        'Fulfillment Optimization est un candidat de nom pour la responsabilité de choix de satisfaction. La frontière individuel/collectif ne définit pas les domaines.'),
    comparison('Microsoft', 'Dynamics 365 Supply Chain Management', 'Order promising',
        'https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations',
        'Documentation évolutive, mise à jour affichée 2026-04-21', 'In this article ; ATP calculations ; CTP calculations',
        'Établir les dates possibles et la disponibilité soutenant une promesse, notamment par ATP et CTP.',
        'Le CTP Microsoft décrit notamment la capacité de production ; FLOW examine plus largement les adaptations. Cette page ne définit pas toute la gestion de promesse FLOW.',
        'Order Promising constitue un angle métier pertinent, également présent chez Microsoft ; le domaine proposé inclurait la tenue des engagements par choix FLOW explicite.')
]
domain['fields']['market_comparisons'].extend(comparisons)
for n in (domain, assignment):
    n['source_refs'] = list(dict.fromkeys(n['source_refs'] + ['U435', 'U437']))
    n['revision'] += 1
    n['last_modified'] = stamp
    if 'content_sha256' in n:
        n['content_sha256'] = content_hash(n)

model['source_version'] += ' + U437 revue des frontières de D03, structure proposée non adoptée'
for entry in model['source_files']:
    entry['sha256'] = sha256((ROOT / entry['path']).read_bytes()).hexdigest()

preserved = 0
for collection in ('nodes', 'relations', 'principles'):
    current = {n['id']: n for n in model[collection]}
    for original in before[collection]:
        item = current[original['id']]
        a = original['fields'] if collection == 'nodes' else original
        b = item['fields'] if collection == 'nodes' else item
        for field in original.get('lifecycle', {}).get('validated_fields', []):
            assert a[field] == b[field], (original['id'], field)
            assert original['lifecycle']['value_sha256'][field] == item['lifecycle']['value_sha256'][field]
            preserved += 1
assert model['relations'] == before['relations']
assert model['principles'] == before['principles']
PATH.write_text(dumps(model), encoding='utf-8')

review = dict(
    source_refs=['U437', 'U435', 'U436', 'U328', 'U329', 'U378', 'U417', 'U420'],
    status='proposed_pending_domain_arbitration',
    recorded_at=stamp,
    authority='Le catalogue courant reste model.yaml. Ce document propose des choix ; aucun nom, parent ou champ validé n’est remplacé.',
    model_before_sha256=sha256(BASE.read_bytes()).hexdigest(),
    model_after_editorial_fixes_sha256=sha256(PATH.read_bytes()).hexdigest(),
    diagnosis=[
        'Backlog désigne le carnet travaillé ; il ne suffit pas à délimiter le problème métier du domaine.',
        'D03 regroupe possibilités et engagements de promesse, arbitrage de satisfaction, structure et conservation des Orders.',
        'Les recouvrements de sélection doivent être clarifiés par résultat et autorité ; changer les parents ne suffit pas.'
    ],
    recommendation=dict(
        status='proposed',
        option='two_domains',
        justification='Distinguer la responsabilité des promesses de celle des choix de satisfaction, pour rendre les revues PO et métier plus lisibles.',
        domains=[
            dict(proposed_name='Order Promising', identifier='À attribuer après arbitrage, sans réutiliser un identifiant retiré',
                 responsibility='Établir ce qui peut être promis et sous quelles conditions, puis maintenir les propositions et engagements de quantités et de dates.',
                 capability_ids=['D03.i', 'D03.j', 'D03.k', 'D03.l', 'D03.n']),
            dict(proposed_name='Fulfillment Optimization', identifier='D03 conservé proposé',
                 responsibility='Arbitrer la satisfaction des Orders sous contraintes, déterminer un plan cohérent et matérialiser les affectations retenues.',
                 capability_ids=['D03.m', 'D03.o', 'D03.p', 'D02.e'])
        ],
        proposed_other_moves=[dict(capability_id=k, current_domain='D03', proposed_domain='D04',
            reason=reason) for k, reason in [
                ('D04.n', 'Structurer les Orders relève de leur tenue ; une optimisation mobilise cette capacité sans posséder toute la structure.'),
                ('D04.q', 'La conservation historique ne détermine ni une promesse ni un choix de satisfaction.')]],
        planning_name_candidate='Fulfillment Planning',
        planning_name_status='Piste lexicale proposée, pas de renommage automatique ni de terme universel établi par les sources retenues',
        benefit='Deux responsabilités directrices identifiables, sans supprimer les décisions fines ni créer une capacité par fonction éditeur.',
        tradeoff='Interfaces dans les deux sens et dépendances fortes ; les choix économiques, temporels et collectifs doivent rester compatibles.'
    ),
    alternative=dict(option='one_domain', proposed_name='Fulfillment Optimization',
        capability_ids=['D03.i', 'D03.j', 'D03.k', 'D03.l', 'D03.n', 'D03.m', 'D03.o', 'D03.p', 'D02.e'],
        same_proposed_moves_to_D04=['D04.n', 'D04.q'],
        benefit='Un seul domaine autour de la satisfaction des Orders ; moins de frontières de domaine.',
        tradeoff='La tenue des engagements reste sous une bannière Optimization ; les deux responsabilités sont moins visibles.'),
    boundaries_to_arbitrate=[
        dict(elements=['D03.i','D03.j','D03.l'], proposal='ATP/CTP établissent des possibilités réalisables ; Delivery Schedule Decision choisit un échéancier compatible avec les arbitrages applicables.', risk='Ne pas attribuer le même choix définitif de quantités et de dates à trois décisions.'),
        dict(elements=['D03.k','D03.o'], proposal='PTP porte le choix économique contextualisé ; Fulfillment Plan Decision compose le compromis final de satisfaction multidimensionnelle.', risk='Une préférence économique ne doit pas devenir un veto implicite ni un second plan final indépendant ; règles de compatibilité à préciser.'),
        dict(elements=['D03.p','D03.o'], proposal='Planning organise hypothèses, simulations, comparaison et maintien des scénarios en mobilisant les décisions ; Fulfillment Plan Decision détermine la cohérence des choix d’affectation.', risk='Ne pas créer deux optimiseurs ou réduire Planning à un calcul.'),
        dict(elements=['D03.o','D03.n'], proposal='Le plan ressources-commandes soutient une proposition de promesse ; confirmer ou réviser l’engagement reste à Promise Management.', risk='Une possibilité ou un plan retenu ne vaut pas engagement confirmé ; leur actualité doit être vérifiable.')
    ],
    invariants=[
        'La scission ne repose pas sur individuel/collectif : ATP couvre plusieurs demandes ; une optimisation peut en traiter une seule.',
        'Seule Reservation bloque les usages concurrents, conformément à U436 ; priorité, plan, affectation et promesse restent distincts.',
        'D04 conserve les Orders et leur autorisation de prise en charge ; D06 conserve la coordination des services ; D05 optimise le stock.',
        'Les correspondances SAP/Microsoft sont des appuis partiels, pas une taxonomie d’entreprise adoptée.',
        'Aucune fusion ni suppression de capacité ou de comportement proposée dans ce premier choix de domaines.'
    ],
    review_scenarios=[
        dict(case='Deux commandes de 60 pour 80 disponibles, avec une réservation existante.',
             check='Établir les possibilités, arbitrer les priorités et le plan, appliquer les affectations, puis gérer les engagements autorisés sans lever la réservation par priorité seule.'),
        dict(case='Un fournisseur retarde 40 pièces soutenant plusieurs commandes.',
             check='Examiner les alternatives et leurs conséquences, recomposer le plan retenu et traiter les révisions de promesse autorisées ; aucune modification automatique des engagements.'),
        dict(case='Une demande de 100 satisfaite par 60 vendredi et 40 lundi.',
             check='Distinguer possibilités, échéancier retenu, promesse, liens d’affectation et éventuel découpage des Orders ; deux échéances ne créent pas automatiquement deux commandes.')
    ],
    market_comparisons=deepcopy(comparisons),
    applied_editorial_fixes=[
        dict(element='D03', fields=['definition','scope','review','market_comparisons'], reason='Alignement de l’autorisation sur Lifecycle U420 ; comparaison marché et revue proposée.'),
        dict(element='D02.e', fields=['definition','finality','review'], reason='Alignement sur la matérialisation des choix ; optimisation collective déjà portée par D03.o U378.')
    ],
    previous_validated_values_preserved=preserved,
    decision_required='Choisir entre la scission proposée en deux domaines et un domaine unique resserré, ainsi que les deux déplacements proposés vers D04 ; choix de périmètre complexe demandé à Laurent sous U435.'
)
(ROOT / 'modeles/backlog/d03-domain-review-U437.yaml').write_text(dumps(review), encoding='utf-8')
print('Recorded D03 review; two nodes edited; no parent, name, approved value, relation or principle changed.')
print('Approved values preserved:', preserved)

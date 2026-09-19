"""Apply U435 editorial scopes and the exact U436 reservation boundary.

Run once, after the other U435 patches. No publication or historical edit.
"""
from copy import deepcopy
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps

OUT = Path(__file__).parent

SCOPES = {
    'D03.k': '''Comparer les conséquences économiques des scénarios de promesse réalisables : coûts pertinents de transport, de préparation, de fractionnement ou d'adaptation et effets économiques connus. Les valeurs, leur provenance, leur période de validité et les hypothèses sont des entrées à identifier ; cette capacité n'administre ni tarifs, ni comptabilité, ni politique de prix.

Prendre en compte les quantités et échéances possibles, les conditions contractuelles et les contraintes de service. Distinguer les contraintes impératives des préférences économiques. Une information de coût manquante ou incertaine doit rester visible ; elle ne vaut pas un coût nul. Aucun critère ni pondération universelle n'est imposé.

Le résultat explique les scénarios retenus ou écartés et leurs conséquences économiques, avec les hypothèses utilisées. Si aucun scénario admissible n'existe, expliciter cette limite. ATP et CTP conservent l'établissement des possibilités ; Order Prioritization détermine les priorités ; Delivery Schedule Decision choisit l'échéancier. Fulfillment Plan Decision compose un compromis collectif multidimensionnel. La sélection économique ne confirme pas à elle seule une promesse et ne déclenche pas une prestation.

Exemple fictif : comparer une livraison accélérée coûtant 120 et deux livraisons coûtant 80, si les deux respectent les conditions du client. Un scénario moins cher mais hors délai contractuel ne devient pas admissible par son seul gain. Les montants illustrent le raisonnement ; ils ne définissent aucun seuil métier.''',
    'D03.l': '''Choisir la répartition des quantités promises entre les échéances réalisables, en tenant compte des possibilités fournies par ATP/CTP, des conditions de la commande et des décisions économiques et de priorité utiles au cas. Distinguer date demandée, date proposée, date engagée, expédition et réception.

Les possibilités temporelles doivent expliciter les calendriers applicables, jours d'ouverture, heures limites et fuseaux pertinents, ainsi que les délais et dates de connaissance des informations. Ces références proviennent des responsables externes ou des projections applicables ; leur maître précis reste à identifier. Aucun calcul universel par simple ajout de jours ni calendrier administré implicitement par cette capacité.

Le résultat indique quantités et échéances retenues, conditions, hypothèses et reste non couvert. Une préférence pour une livraison unique ou des livraisons fractionnées s'applique selon les conditions connues ; elle n'est pas présumée universelle. Si l'échéance demandée est impossible, exposer les options et la partie non satisfaite sans modifier silencieusement la demande.

Exemple fictif : retenir 60 vendredi et 40 lundi parmi les options autorisées. Si la collecte de vendredi est fermée ou si lundi est non ouvré, réexaminer les options avant de les annoncer. Deux échéances ne signifient pas deux Sales Orders : Order Structuring conserve le découpage, Promise Management la proposition/confirmation/révision et Order Lifecycle Management les changements autorisés.''',
    'D03.m': '''Établir un ordre de priorité entre les commandes ou fractions pertinentes lorsqu'elles sollicitent des ressources concurrentes. Mobiliser les engagements, dates demandées ou promises, accords et critères de priorité applicables ; distinguer obligations impératives, préférences et éventuelles dérogations autorisées.

Le résultat rend explicites les priorités relatives, leur périmètre, leur justification et les égalités ou conflits restant à arbitrer. Une priorité ne crée ni stock, ni faisabilité, ni droit de lever une réservation ou un gel. Réviser les priorités lorsque les faits ou règles changent sans effacer la justification de la décision antérieure.

Fulfillment Plan Decision utilise ces priorités avec les autres décisions pour examiner le carnet ; PTP conserve l'arbitrage économique et Delivery Schedule Decision le choix d'échéancier. Supply Assignment matérialise les affectations retenues et Reservation porte le blocage des usages concurrents. Aucun classement automatique par chiffre d'affaires, canal ou date seule n'est adopté.

Exemple fictif : deux commandes demandent chacune 60 pièces pour 80 admissibles. Une obligation contractuelle peut donner priorité à la première ; cette priorité ne détermine pas à elle seule la répartition des 20 restantes, une dérogation ni une promesse au second client.''',
}

BOUNDARY = ('U436 : seule la réservation bloque les usages concurrents ; l’affectation seule ne les bloque pas. '
            'Créer, conserver ou réviser un lien d’affectation ne crée donc pas implicitement une réservation. '
            'Les protections de groupe conservent leurs règles d’admissibilité, et un gel d’affectation sa restriction de modification. '
            'Expiration, consommation, libération et déclenchement automatique éventuel d’une réservation restent à préciser ; '
            'aucun mécanisme technique de concurrence n’est déduit de cette frontière.')


def add_refs(item, *refs):
    item['source_refs'] = list(dict.fromkeys(item.get('source_refs', []) + list(refs)))


def main():
    assert not (OUT / 'scope-fixes-applied.yaml').exists(), 'Already applied'
    model_path = ROOT / 'modeles/backlog/model.yaml'
    model = read(model_path)
    before = deepcopy(model)
    nodes = {n['id']: n for n in model['nodes']}
    for identifier, scope in SCOPES.items():
        nodes[identifier]['fields']['scope'] = scope
        add_refs(nodes[identifier], 'U435')
    for identifier in ('D02.c', 'D02.e', 'BHV045', 'BHV046', 'BHV047'):
        node = nodes[identifier]
        node['fields']['scope'] += '\n\n' + BOUNDARY
        if identifier == 'D02.e':
            node['fields']['scope'] = node['fields']['scope'].replace(
                'La décision collective et les contrats d’engagement restent à préciser dans A01/A02.',
                'Fulfillment Plan Decision porte la décision collective depuis U378 ; U436 précise le blocage des usages concurrents. Les autres contrats d’engagement restent à instruire.')
        add_refs(node, 'U436')
    nodes['BHV003']['fields']['scope'] += ('\n\nPrécision éditoriale U435 : les délais utilisables tiennent compte des calendriers, jours ouvrés, heures limites et fuseaux pertinents. '
        'Conserver origine et validité des informations ; si une contrainte temporelle est inconnue, ne pas présenter la date comme certaine. '
        'Exemple fictif : un stock présent après la dernière collecte ne permet pas de promettre un départ avant la prochaine ouverture applicable. '
        'Cette lecture des délais ne gère pas les calendriers maîtres et ne choisit pas à elle seule l’échéancier engagé.')
    add_refs(nodes['BHV003'], 'U435')
    nodes['D06.b']['fields']['scope'] += ('\n\nPrécision éditoriale U435 : contextualiser les créneaux et dates communiqués avec leur calendrier applicable, fuseau et éventuelle heure limite. '
        'Une fermeture ou une information périmée doit rester visible aux décisions consommatrices ; aucun disponible ni engagement de capacité n’est déduit d’un plafond communiqué.')
    add_refs(nodes['D06.b'], 'U435')
    stock_scopes = {
        'D01.g': ('Précision éditoriale U435 : conserver la date du fait, sa date de connaissance, son origine et une référence rapprochant une correction du fait antérieur. '
            'Un même fait reçu plusieurs fois ne produit pas plusieurs mouvements. La correction reconnue reste traçable sans effacer le fait initial. '
            'Exemple fictif : une réception déclarée à 100 est corrigée à 80 ; conserver le lien explicatif entre les faits, puis fournir le résultat à Inventory Tracking. '
            'Identifiants techniques, dédoublonnage et propagation restent à concevoir ; aucune architecture événementielle imposée.'),
        'D01.f': ('Précision éditoriale U435 : intégrer les mouvements reconnus et leurs corrections sans décompter plusieurs fois le même effet. '
            'Distinguer quantité physique, état logique et ressource future ; un fait tardif peut corriger leur représentation à la date pertinente. '
            'Exemple fictif : une réception de 100 reçue deux fois puis corrigée à 80 ne représente pas 180 ou 200 unités présentes. '
            'Record Inventory Movements conserve les faits et leurs justifications ; Inventory Tracking en établit les quantités et états.'),
        'D01.c': ('Précision éditoriale U435 : exposer les états corrigés et leur fraîcheur, avec la provenance permettant au consommateur de comprendre une variation. '
            'Une donnée absente ou périmée n’équivaut pas à une quantité nulle ou certaine. Les décisions de disponibilité ou de promesse doivent pouvoir identifier cette limite. '
            'Cette lecture ne corrige pas elle-même les mouvements et ne confirme pas une nouvelle promesse.'),
    }
    for identifier, scope in stock_scopes.items():
        node = nodes[identifier]
        node['fields']['scope'] += '\n\n' + scope
        comparison = dict(vendor='GS1', product='EPCIS / CBV', element_name='Visibility data and erroneous events',
            element_type='Standard de données et guide d’implémentation', relationship='Appui sémantique',
            similarities='Contexte des faits de visibilité, distinction des dates et correction traçable d’un fait antérieur.',
            differences='EPCIS décrit des événements et échanges ; il ne définit pas la capacité FLOW, ses états de stock ou la politique d’engagement des ressources futures.',
            flow_position='U435 : étayer la lecture et la correction des faits de stock, sans imposer EPCIS ni déduire une réalisation installée.',
            source_title='EPCIS and CBV Implementation Guideline', source_url='https://ref.gs1.org/guidelines/epcis-cbv/2.0.0/',
            source_version='Release 2.0, ratifiée mars 2023', source_locator='Dimensions de visibilité ; §5.9 Erroneous events',
            consulted_on='2026-09-19', evidence_limits='Passages du guide officiel lus ; standard de données distinct d’une taxonomie de capacités. STD-V0-04 dans l’audit U434.',
            status='proposed', source_refs=['U434', 'U435'])
        if identifier == 'D01.g':
            node['fields'].setdefault('market_comparisons', []).append(comparison)
        add_refs(node, 'U435')
    for relation in model['relations']:
        if relation['id'] not in ('REL-NEEDS-U290-018', 'REL-NEEDS-U290-019', 'REL-NEEDS-U290-025', 'REL-NEEDS-U290-029', 'REL-NEEDS-U290-030'):
            continue
        reserved = relation['target_id'] == 'D02.c'
        relation['fields'] = {'label': 'Tient compte des réservations opposables' if reserved else 'Utilise les affectations, distinctes des réservations'}
        relation['qualification']['meaning'] = ('Le consommateur tient compte des quantités réservées et des conditions de cet engagement pour ses possibilités ou décisions ; Reservation porte le blocage des usages concurrents.' if reserved else
            'Le consommateur utilise les liens entre ressources et commandes pour connaître leur affectation ; ces liens seuls ne bloquent pas les usages concurrents.')
        relation['qualification']['conditions'] = ['Lorsque les ressources ou commandes du périmètre sont concernées ; U436 distingue affectation et réservation.',
            'Préserver la référence des quantités afin de ne pas les décompter plusieurs fois ; les règles de consommation et de libération restent à préciser.']
        relation['qualification']['effects'] = ['La réservation porte le blocage concurrent ; aucune réservation automatique n’est créée par la simple affectation.',
            'Le consommateur conserve sa responsabilité et respecte les protections et restrictions applicables.']
        relation['qualification']['scope'] = 'Frontière U436 adoptée ; formulation détaillée du contrat proposée. Dépendance consommateur vers fournisseur de résultat, sans appel technique imposé.'
        add_refs(relation, 'U436')
        relation['review']['note'] += ' U436 précise la frontière ; qualification détaillée éditoriale, sans adoption globale du lien.'
    model['principles'].append(dict(id='PRINCIPLE-RESERVATION-CONCURRENCY',
        statement='Seule la réservation bloque les usages concurrents ; l’affectation seule ne les bloque pas.', source_refs=['U436']))
    principle = next(p for p in model['principles'] if p['id'] == 'PRINCIPLE-SUPPLY-DOCUMENTS')
    principle['statement'] = ('Supply porte les Orders selon leur intention métier, les parties, les engagements et le résultat attendu. '
        'Les documents d’autorisation contribuent à leur traitement sans dicter le découpage des responsabilités. '
        'Les parcours transverses de Business Services gardent leur modèle processus distinct.')
    add_refs(principle, 'U393', 'U394', 'U435')
    changes = []
    for collection in ('nodes', 'relations'):
        prior = {i['id']: i for i in before[collection]}
        for item in model[collection]:
            old = prior[item['id']]
            if item == old:
                continue
            values_old = old['fields'] if collection == 'nodes' else old
            values_new = item['fields'] if collection == 'nodes' else item
            for field in old.get('lifecycle', {}).get('validated_fields', []):
                assert values_old[field] == values_new[field], (item['id'], field)
            item['revision'] = old.get('revision', 1) + 1
            changes.append({'id': item['id'], 'collection': collection})
    model['as_of'] = '2026-09-19'
    model_path.write_text(dumps(model), encoding='utf-8')
    glossary_path = ROOT / 'modeles/backlog/glossary.yaml'
    glossary = read(glossary_path)
    for term in glossary['terms']:
        if term['id'] in ('TER016', 'TER017', 'TER078'):
            term['notes'] += '\n\n' + BOUNDARY
            add_refs(term, 'U436')
            term['review'] = dict(state='partial', note=term['review'].get('note', '') + ' U436 adopte uniquement la frontière réservation / affectation sur le blocage concurrent. Définitions et autres compléments conservent leur portée antérieure ; aucun accord global sur le terme.')
    glossary['as_of'] = '2026-09-19'
    add_refs(glossary, 'U436')
    glossary_path.write_text(dumps(glossary), encoding='utf-8')
    (OUT / 'scope-fixes-applied.yaml').write_text(dumps({'source_refs': ['U435', 'U436'], 'changes': changes,
        'principles_changed': ['PRINCIPLE-SUPPLY-DOCUMENTS'], 'principles_added': ['PRINCIPLE-RESERVATION-CONCURRENCY'],
        'glossary_notes_changed': ['TER016', 'TER017', 'TER078'], 'previous_validated_values_preserved': True}), encoding='utf-8')
    print(f'Applied scope and reservation clarifications to {len(changes)} existing elements.')


if __name__ == '__main__':
    main()

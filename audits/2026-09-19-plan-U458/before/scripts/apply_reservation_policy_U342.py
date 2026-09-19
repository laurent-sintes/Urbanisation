"""Integrate the scoped U342 agreement and document proposed policy mechanisms."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

from scripts.lifecycle import value_hash
from scripts.structured_io import read, dumps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-18-reservation-policy'


def append(path, text):
    with (ROOT / path).open('a', encoding='utf-8') as stream:
        stream.write('\n\n' + text.strip() + '\n')


def main():
    assert not OUT.exists(), 'U342 already applied; do not overwrite evidence.'
    assert '## U342\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    OUT.mkdir()
    for name in ['model', 'behavior-gap-audit', 'assignment-reservation-review']:
        (OUT / (name + '-before.yaml')).write_bytes((ROOT / ('modeles/backlog/' + name + '.yaml')).read_bytes())
    append('connaissance/01-contributions-utilisateur.md', '''## U342

**id**

U342

**date**

2026-09-18

**titre**

Adoption de Reservation Policy Decision et demande de documentation des comportements

**texte**

Je valide Reservation Policy Decision. Mais il faut lister tous les comportements possibles et les documenter

**contexte et portée**

Accord sur la capacité proposée après U341, son nom et sa définition présentée : « Déterminer dans quelles situations, à quel moment et pour quelle durée réserver des ressources afin de sécuriser la promesse, selon le risque de pénurie et le coût d’indisponibilité pour les autres demandes. » Demande de recensement et de documentation des comportements possibles. Le rattachement de domaine, la liste nouvelle de comportements, leurs noms/définitions, les contrats détaillés et les comparaisons marché restent proposés. Autorisation d’intégration au backlog, sans publication implicite.''')
    m = read(ROOT / 'modeles/backlog/model.yaml')
    before = deepcopy(m)
    review = read(ROOT / 'modeles/backlog/assignment-reservation-review.yaml')
    ids = {n['id'] for n in m['nodes']}
    assert not ids & {'D05.h', 'BHV032', 'BHV033', 'BHV034', 'BHV035'}
    now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    refs = ['U341', 'U342', 'ELM212', 'CMP120', 'ELM213', 'CMP121']

    def cycle(values, approved=()):
        return dict(state='urbanist_validated' if approved else 'ai_proposed', recorded_at=now,
                    recorded_by='Codex', source_refs=['U342'], validated_fields=list(approved),
                    value_sha256={f: value_hash(values[f]) for f in approved},
                    note='U342 adopte le nom et la définition de la capacité ; les comportements et rattachements nouvellement documentés restent proposés.')

    comparisons = deepcopy(review['policy_decision_U341']['market_comparisons'])
    for c in comparisons:
        c['source_refs'] += ['U342']
        c['flow_position'] = 'Reservation Policy Decision adoptée U342 ; décomposition et parent proposés. Appui au résultat métier, sans prétendre à une équivalence de catalogue ni à un moteur adaptatif standard.'
    additional = [
        ('Oracle', 'E-Business Suite Order Management', 'Reservation Time Fence',
         'https://docs.oracle.com/cd/E26401_01/doc.122/e48842/T373258T377249.htm', '12.2',
         'Reservation Time Fence ; Reserve Orders Concurrent Program ; Reservation Modes',
         'Une fenêtre avant la date planifiée conditionne la réservation automatique. Le programme Reserve Orders peut reprendre les lignes concernées.',
         'Référence EBS, pas Fusion Cloud. Les modes Fair Share/Percentage/Partial du même chapitre mêlent arbitrage des quantités et réservation ; FLOW conserve leurs frontières. Texte primaire ouvert.'),
        ('IBM', 'Sterling Order Management', 'Handling inventory reservation',
         'https://www.ibm.com/docs/en/order-management?topic=2-handling-inventory-reservation', 'Documentation évolutive',
         'Introduction ; Creating reservations',
         'La réservation peut servir des clients prioritaires ou un ordre premier arrivé, premier servi.',
         'Appui à des politiques différenciées ; ne prouve pas une optimisation automatique de la durée par catégorie. Texte primaire indexé consulté.'),
        ('IBM', 'Sterling Intelligent Promising', 'Reservations',
         'https://www.ibm.com/docs/en/sip?topic=data-reservations', 'Documentation évolutive',
         'Creating reservation for node or network ; Updating reservation quantity ; Defining expiration times',
         'Réservations par site ou réseau, expiration configurable et réservation partielle documentées.',
         'Options de réalisation ; le réseau est décomposé en sites selon les priorités IBM. Ne prouve pas une réservation sans affectation sous-jacente. Texte indexé consulté ; ouverture directe indisponible.'),
        ('Shopify', 'Checkout', 'Shopify Checkout',
         'https://help.shopify.com/en/manual/checkout-settings', 'Documentation évolutive',
         'Introduction, contrôle du stock au checkout',
         'Stock retenu à la soumission des informations de paiement, avec libération en cas d’échec.',
         'Jalon produit spécifique, distinct de l’ouverture de page et de l’encaissement effectif ; aucun déclencheur FLOW imposé.'),
    ]
    for vendor, product, name, url, edition, locator, fact, limit in additional:
        comparisons.append(dict(vendor=vendor, product=product, element_name=name,
            element_type='Mécanisme ou règle fonctionnelle produit', relationship='Recouvrement partiel',
            similarities=fact, differences=limit, source_title=name, source_url=url,
            source_version=edition, source_locator=locator, consulted_on='2026-09-18',
            evidence_limits='Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.',
            flow_position='U342 : capacité adoptée ; mécanismes, périmètres et correspondances proposés. Aucun alignement automatique des niveaux produit et FLOW.',
            status='proposed', source_refs=['U342', 'ELM213', 'CMP121']))

    # Every behavior is a business policy mechanism, not a screen, parameter or CRUD operation.
    entries = [
        dict(node_id='BHV032', name='Milestone-Based Reservation Policy',
             definition='Déterminer les événements du parcours métier à partir desquels la ressource doit être réservée, puis les conditions de maintien de cette protection au fil du parcours.',
             criterion='Politique de déclenchement par engagement ou événement métier',
             benefit='Rendre cohérent ce que le client croit garanti avec le stade atteint dans la vente, tout en limitant les immobilisations prématurées.',
             mechanism='Choisir un jalon significatif : ajout au panier, demande explicite de mise de côté, soumission du paiement, acceptation de la commande ou autre engagement convenu. Définir les conditions de passage d’une protection provisoire à celle qui accompagne la commande. Un écran n’est pas le jalon métier.',
             inputs=['États et événements du parcours', 'Nature de l’engagement client', 'Conditions de paiement et d’annulation', 'Objectifs de service'],
             outputs=['Jalon déclencheur', 'Conditions de maintien, d’expiration et de libération', 'Règle de continuité lors de la confirmation'],
             example='Exemple fictif : une pièce reste vendable pendant la consultation du panier ; la soumission du paiement déclenche une réservation de dix minutes. Un paiement accepté prolonge l’engagement pour servir la commande, sans libération intermédiaire de la pièce.',
             boundary='Choisir le jalon et les conditions ne pilote pas le parcours : les processus les mobilisent ; Reservation établit et maintient les engagements. Panier, paiement et commande sont des options de politique, pas trois comportements.',
             market_indices=[0, 1, 7], evidence='Mécanismes de déclenchement directement documentés ; nom de regroupement FLOW proposé.'),
        dict(node_id='BHV033', name='Time-Fenced Reservation Policy',
             definition='Déterminer à quelle distance de la date de besoin commencer à réserver, afin de sécuriser l’échéance sans immobiliser trop tôt les ressources.',
             criterion='Mécanisme de fenêtre temporelle avant le besoin',
             benefit='Conserver de la flexibilité pour les demandes proches tout en organisant la sécurisation progressive des échéances futures.',
             mechanism='Définir une fenêtre de réservation relative à la date de besoin ou d’expédition. Une demande déjà acceptée peut rester hors de cette fenêtre ; l’entrée dans la fenêtre déclenche une nouvelle appréciation selon les conditions applicables. Distinguer cet horizon du délai d’expiration d’une réservation déjà accordée.',
             inputs=['Date de besoin ou d’expédition', 'Délais de préparation', 'Engagements déjà pris', 'Disponibilité présente et future admissible'],
             outputs=['Fenêtre avant le besoin', 'Conditions de réexamen à l’entrée dans la fenêtre', 'Traitement d’un changement d’échéance'],
             example='Exemple fictif : pour une livraison dans trente jours, décider de commencer la réservation à J-7. Cela ne signifie ni ignorer la demande dans l’ATP avant J-7, ni autoriser une promesse sans ressources crédibles.',
             boundary='La date réalisable reste du ressort des décisions de promesse ; ce comportement choisit quand sécuriser les ressources par réservation. Il ne programme pas les opérations logistiques et ne recalcule pas la promesse.',
             market_indices=[4], evidence='Reservation Time Fence est un terme et un mécanisme explicites chez Oracle EBS.'),
        dict(node_id='BHV034', name='Demand-Differentiated Reservation Policy',
             definition='Déterminer des conditions de réservation différentes selon les engagements de service attachés aux demandes, aux clients ou aux canaux, en respectant les priorités et droits d’usage établis.',
             criterion='Politique différenciée de service',
             benefit='Rendre possibles des engagements commerciaux distincts sans appliquer une immobilisation maximale à toutes les demandes.',
             mechanism='Distinguer des régimes de réservation lorsque les conditions de service le justifient : mise de côté convenue pour un client professionnel, protection au paiement pour une vente en ligne, réservation dès acceptation d’une demande urgente. La différence doit modifier la garantie ou le processus ; un simple filtre client ne suffit pas.',
             inputs=['Conditions commerciales et de service', 'Typologie du besoin', 'Priorités déjà décidées', 'Droits et protections applicables'],
             outputs=['Régimes par contexte de demande', 'Jalons et durées différenciés', 'Conditions explicites de dérogation'],
             example='Exemple fictif : un accord professionnel prévoit une mise de côté dès acceptation pendant quarante-huit heures, tandis que la vente web standard réserve au paiement. Ces durées illustrent des engagements différents et ne constituent pas des règles Beaumanoir constatées.',
             boundary='Order Prioritization garde le classement des Orders ; Group Protection Decision garde les enveloppes des groupes. Ce comportement ne choisit ni les commandes gagnantes ni les quantités affectées : il décide du régime de réservation applicable à la demande.',
             market_indices=[0, 5], evidence='Besoins de réservation différenciés attestés ; leur regroupement comme comportement décisionnel est une interprétation FLOW.'),
        dict(node_id='BHV035', name='Risk-Adaptive Reservation Policy',
             definition='Adapter les conditions de déclenchement et de durée de réservation à la tension sur les ressources et au risque d’immobilisation inutile, dans les limites des engagements déjà accordés.',
             criterion='Mécanisme de décision contextuelle selon le risque',
             benefit='Réagir aux évolutions de demande et de disponibilité en arbitrant entre perte de promesse et indisponibilité du stock pour d’autres ventes.',
             mechanism='Appliquer des règles conditionnelles, réestimer les paramètres ou sélectionner une politique selon la situation. Examiner les stocks libres, les engagements concurrents, leur vitesse et variabilité, les entrées attendues et leur fiabilité. La probabilité de conversion et les abandons peuvent éclairer le coût d’une réservation précoce. Une politique conditionnelle peut être définie à l’avance ; adaptation ne signifie ni apprentissage obligatoire ni réécriture permanente des règles.',
             inputs=['Disponibilité après engagements et protections', 'Vitesse des demandes et réservations concurrentes', 'Fiabilité des entrées et du stock', 'Durée du parcours et conversion, si connues', 'Objectifs et limites de service'],
             outputs=['Politique sélectionnée ou paramètres recommandés', 'Motif métier du choix et horizon de validité', 'Conditions de réexamen et solution de repli si les informations sont insuffisantes'],
             example='Exemple fictif : une capsule dispose de huit pièces alors que les demandes s’accélèrent. Pour sécuriser le paiement, proposer une protection plus précoce et courte ; si les paniers sont surtout abandonnés, retenir au contraire une protection plus tardive. Le risque de pénurie seul ne détermine pas le sens de l’adaptation.',
             boundary='Ne pas déduire deux fois les mêmes engagements ; ne pas assimiler sorties physiques et demandes nouvelles. ATP reste fournisseur de possibilités, PTP de l’arbitrage économique de satisfaction des Orders. Une révision de politique ne révoque pas implicitement les réservations existantes ; leurs modifications suivent les conditions accordées.',
             market_indices=[1, 2, 3], evidence='Leviers commercetools et adaptations voisines IBM/SAP ; aucun moteur standard de sélection du jalon par risque démontré. Proposition FLOW issue de U341, sans revendication d’innovation exclusive.'),
    ]
    rationale = ('Le jalon du parcours, la proximité du besoin, la différenciation des engagements de service et l’adaptation au risque '
                 'changent chacun la façon de sécuriser une promesse et le coût d’immobilisation. Quatre mécanismes combinables sont proposés ; '
                 'durées, seuils, canaux et interfaces restent des paramètres ou des contextes. La complexité visée est l’arbitrage de ces mécanismes sans retirer implicitement les garanties existantes.')
    scope = '''La décision produit les conditions dans lesquelles réserver : événements déclencheurs, horizon avant le besoin, durée de protection, conditions de maintien et de réexamen. Une politique peut être définie à l’avance et contenir des règles conditionnelles ; sa sélection contextuelle et la révision de ses paramètres ne sont pas confondues.

Les quatre comportements proposés se combinent sans constituer une séquence. Les variables de sortie sont communes : elles ne donnent pas lieu à un comportement par seuil, durée, écran ou opération. Les règles doivent expliciter le résultat lorsque les conditions se contredisent ou que les données sont insuffisantes ; aucun ordre de priorité universel n’est imposé.

[Inventory Visibility](model:D01.c) fournit les états de stock ; [ATP](model:D03.i) établit les possibilités en tenant compte des engagements. Les flux de demandes et de réservations sont distincts des sorties physiques. Les estimations de conversion peuvent être utilisées si elles existent ; aucune capacité de scoring client ou architecture IA n’est présumée.

[Reservation](model:D02.c) réalise et maintient les engagements individuels. [Supply Assignment](model:D02.e) garde les liens ressources-commandes, [Order Prioritization](model:D03.m) les priorités, [Group Protection Decision](model:D05.d) les enveloppes et [Inventory Target Decision](model:D05.a) les cibles de stock. La gouvernance et la mise en vigueur des politiques restent une responsabilité de management ; leur porteur précis est à arbitrer. Aucun transfert implicite de cette gouvernance vers Reservation Policy Decision.

Exemple fictif : conserver une réservation au paiement en fonctionnement normal, puis examiner une protection plus précoce et plus courte pour une capsule sous tension. La décision compare aussi le risque de paniers abandonnés ; elle ne suppose pas que tout stock rare doit être réservé plus tôt. Les garanties existantes restent applicables selon leurs conditions.

Rattachement proposé à Inventory Optimization : optimiser le compromis entre disponibilité pour les ventes, immobilisation et risque. Le résultat peut être mobilisé lors d’une promesse ou d’un parcours de vente sans transférer à D05 la satisfaction des Orders. Ce parent n’a pas été présenté lors de la validation U342 et reste proposé.'''
    fields = dict(name='Reservation Policy Decision', definition=review['policy_decision_U341']['candidate_definition'],
                  finality='Choisir comment sécuriser les ressources d’une promesse tout en maîtrisant leur indisponibilité pour les autres demandes.',
                  nature='decision', scope=scope, decomposition_rationale=rationale, market_comparisons=comparisons)
    cap = dict(id='D05.h', revision=1, kind='capability', layer='transactional', fields=fields,
               source_refs=refs, source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u342'),
               adoption_ids=[], review=dict(state='partial', note='Nom et définition présentés adoptés U342 ; parent, détails et quatre comportements proposés.'),
               editorial_basis='Accord U342 sur la proposition U341. Recensement mécanismes/paramètres/frontières documenté dans reservation-policy-review.yaml.',
               lifecycle=cycle(fields, ['name', 'definition']))
    m['nodes'].append(cap)

    def relation(identifier, source, target, meaning=None):
        r = dict(id=identifier, revision=1, type='relates-to' if meaning else 'contains', source_id=source,
                 target_id=target, source_refs=['U342'], review=dict(state='proposed', note='Rattachement ou contrat proposé lors du recensement U342.'))
        if meaning:
            r['qualification'] = dict(role='needs', meaning=meaning,
                conditions=['Selon le contexte utile à la décision ou à son application ; aucun appel systématique ni ordre d’exécution imposé.'],
                effects=['Utiliser les informations ou conditions sans transférer la responsabilité métier du fournisseur.'])
        r['lifecycle'] = cycle(r)
        m['relations'].append(r)

    relation('REL-MEMBER-D05.h', 'D05', 'D05.h')
    for e in entries:
        cs = [deepcopy(comparisons[i]) for i in e['market_indices']]
        for c in cs:
            c['flow_position'] = e['evidence'] + ' Proposition ' + e['name'] + ' sous Reservation Policy Decision ; aucune validation implicite du comportement.'
        f = dict(name=e['name'], definition=e['definition'], finality=e['benefit'],
                 scope='\n\n'.join([e['mechanism'], 'Entrées : ' + '; '.join(e['inputs']) + '.',
                     'Résultat : ' + '; '.join(e['outputs']) + '.', e['example'], 'Frontières : ' + e['boundary'],
                     'Justification : ' + e['criterion'] + '. ' + e['benefit'], 'Comparaison : ' + e['evidence']]), market_comparisons=cs)
        m['nodes'].append(dict(id=e['node_id'], revision=1, kind='behavior', layer='transactional', fields=f,
            source_refs=refs, source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u342'),
            adoption_ids=[], review=dict(state='proposed', note='Nouveau comportement proposé pour instruction ; U342 valide la capacité et demande le recensement, pas cette liste.'),
            editorial_basis='Mécanisme terminal, combinable avec les autres ; pas une fonction produit ni un niveau de maturité.', lifecycle=cycle(f)))
        relation('REL-BEHAVIOR-' + e['node_id'], 'D05.h', e['node_id'])
    for suffix, target, meaning in [
        ('INVENTORY', 'D01.c', 'A besoin des quantités, états, engagements connus et de leur fraîcheur pour apprécier la tension sans double compte.'),
        ('ATP', 'D03.i', 'A besoin des possibilités de disponibilité présentes et futures dans le contexte, sans recalculer l’ATP.'),
        ('PRIORITY', 'D03.m', 'A besoin des priorités décidées lorsque les régimes de réservation sont différenciés ; ne reclasse pas les Orders.'),
        ('PROTECTION', 'D02.b', 'A besoin des droits et restrictions actifs qui encadrent les réservations possibles.'),
        ('AGREEMENT', 'D11.a', 'A besoin des conditions de service disponibles dans la projection des Agreements lorsqu’elles encadrent les régimes de réservation.')]:
        relation('REL-RESERVATION-POLICY-' + suffix, 'D05.h', target, meaning)
    relation('REL-RESERVATION-POLICY-APPLICATION', 'D02.c', 'D05.h', 'A besoin des conditions de réservation retenues et mises en vigueur par le management responsable pour établir et maintenir les engagements ; une recommandation non activée ne s’applique pas implicitement.')
    relation('REL-INVENTORY-PLANNING-D05.h', 'D05.f', 'D05.h', 'A besoin des politiques de réservation alternatives et de leurs effets pour les scénarios où cet arbitrage modifie disponibilité, immobilisation et risque.')

    coverage = [
        ('Panier, paiement, commande, demande explicite de mise de côté', 'BHV032', 'Options de jalon métier ; aucun comportement par écran.'),
        ('Réservation progressive au fil des engagements', 'BHV032', 'Conditions de continuité dans le même mécanisme ; ne pas créer une fonction de conversion de statut comme comportement.'),
        ('Réservation à l’approche de la date de besoin', 'BHV033', 'Fenêtre avant le besoin distincte de l’expiration après réservation.'),
        ('Clients, canaux, types de besoin ou engagements contractuels', 'BHV034', 'Justifié seulement si la garantie ou le processus diffère ; un simple filtre ne suffit pas.'),
        ('Stock faible, pic de demande, accélération des engagements', 'BHV035', 'Signaux d’une même décision de risque, pas trois comportements.'),
        ('Entrée fournisseur incertaine, stock peu fiable, retards', 'BHV035', 'Autres facteurs de risque ; utiliser les constats et estimations disponibles sans absorber le tracking.'),
        ('Probabilité de conversion, abandon, durée du parcours', 'BHV035', 'Hypothèse décisionnelle FLOW ; aucun moteur standard attesté. Pas de scoring obligatoire ni nouveau comportement par indicateur.'),
        ('Durée fixe, expiration événementielle, prolongation conditionnelle', 'Paramètres communs', 'Le mécanisme choisit les conditions ; Reservation réalise maintien et libération. Une durée chiffrée ne justifie pas un comportement.'),
        ('Manuel, règles déterministes, optimisation, IA', 'Modes de réalisation', 'Ne différencient pas à eux seuls le résultat métier ni la capacité.'),
        ('Politique structurelle versus décision contextuelle', 'Modalités combinables', 'Une règle conditionnelle fixée à l’avance peut produire une décision adaptée au contexte.'),
        ('Réservation partielle, complète ou coordonnée d’un ensemble', 'Candidat de frontière à instruire', 'Effet métier possible sur les ensembles indissociables. Oracle et IBM documentent des modalités partielles ; le choix quantitatif ou la cohérence de promesse peut relever de D03. Pas ajouté à la capacité sans élargissement explicite de son résultat.'),
        ('Réseau versus site, quantité générique versus lot ou unité', 'Reservation / Supply Assignment', 'Portée de l’engagement et affectation des ressources ; ne pas confondre avec choix du moment de réservation. IBM réseau décompose déjà en sites.'),
        ('Stock actuel versus ressources futures', 'ATP / Reservation', 'Admissibilité et portée de l’engagement ; conserver les comportements ATP déjà adoptés.'),
        ('FIFO/FEFO, priorité, partage équitable, pourcentage entre Orders', 'D03 / Supply Assignment', 'Choix des ressources ou des bénéficiaires ; les modes éditeurs ne sont pas recopiés dans la décision de politique temporelle.'),
        ('Reprise d’une réservation au profit d’une autre demande', 'Arbitrage des engagements existants', 'Ne pas présenter la préemption comme un simple paramètre adaptatif. Conditions de révision, Promise Management et processus de compensation à mobiliser selon le cas.'),
        ('Enveloppes par groupe et stock tampon', 'Supply Protection / décisions D05 existantes', 'Protection préalable des usages, distincte d’un engagement de réservation au bénéfice d’un besoin.'),
        ('Créer, modifier, libérer, prolonger, rechercher', 'Fonctions de Reservation', 'Opérations produit à documenter dans les descriptions, pas comportements de décision.'),
        ('Tester plusieurs politiques et mesurer leurs effets', 'Inventory Planning', 'Simulation & analyse reste le comportement de Planning ; mobilise cette décision sans duplication.'),
        ('Vente sans réservation, backorder ou survente autorisée', 'Option et frontière', 'La décision peut conclure à différer ou ne pas réserver avant un jalon. Autoriser une vente sans ressource et modifier la promesse ne sont pas des pouvoirs implicites de cette capacité.'),
    ]
    registry = dict(id='RESERVATION-POLICY-U342', source_refs=refs, status='capability_adopted_behaviors_proposed',
        capability_id='D05.h', adopted_fields=['name','definition'], value_sha256=cap['lifecycle']['value_sha256'],
        proposed_parent=dict(id='D05', rationale='Compromis disponibilité, immobilisation et risque ; le choix de politique reste distinct de la satisfaction des Orders D03.'),
        scope_limit='Recensement des mécanismes pertinents dans le périmètre adopté et les sources consultées ; pas de prétention à toutes les politiques imaginables ni à une couverture installée.',
        decomposition_rationale=rationale, behaviors=entries,
        coverage=[dict(topic=t, disposition=d, rationale=r) for t,d,r in coverage],
        combination_example='Un régime professionnel différencié peut réserver à l’acceptation, seulement dans une fenêtre de sept jours avant le besoin, avec une durée adaptée au risque. Ces mécanismes se combinent ; ni niveaux de maturité ni séquence obligatoire.',
        open_questions=['Valider les quatre comportements, leurs noms et leurs frontières.', 'Arbitrer D05 comme parent et le porteur de gouvernance des politiques.', 'Qualifier les réservations coordonnées/partielles avant tout élargissement de la capacité.'],
        market_comparisons=comparisons)
    (ROOT/'modeles/backlog/reservation-policy-review.yaml').write_text(dumps(registry), encoding='utf-8')
    review['source_refs'] = list(dict.fromkeys(review['source_refs'] + ['U342', 'ELM213', 'CMP121']))
    review['policy_decision_U341']['status'] = 'capability_adopted_U342_details_proposed'
    review['adoption_U342'] = dict(capability_id='D05.h', adopted_fields=['name','definition'],
                                 registry='modeles/backlog/reservation-policy-review.yaml',
                                 scope='Quatre comportements proposés documentés ; rattachement D05 proposé. A01 affectation/réservation reste ouvert hors cette décision.')
    (ROOT/'modeles/backlog/assignment-reservation-review.yaml').write_text(dumps(review), encoding='utf-8')
    (ROOT/'modeles/backlog/model.yaml').write_text(dumps(m), encoding='utf-8')

    append('marche/elements.md', '### ELM213\n\nSources primaires consultées le 18 septembre 2026 pour U342 ; compléments à ELM211/ELM212. Nature : règles et mécanismes produit, pas catalogues de capacités.\n\n' + '\n\n'.join(
        f"- {c['vendor']} — {c['product']} — {c['element_name']} ({c['source_version']}).\n  Source : {c['source_url']}\n  Passage : {c['source_locator']}.\n  Constat reformulé : {c['similarities']}\n  Limites : {c['differences']}" for c in comparisons[4:]))
    append('marche/comparaisons.md', '''## CMP121

- Codex ; 18 septembre 2026 ; U342 ; ELM211–ELM213 ; D05.h Reservation Policy Decision, backlog courant.
- Nom et définition de la capacité adoptés ; D05 et BHV032–BHV035 proposés. Quatre mécanismes : jalon métier, fenêtre avant besoin, régime de service différencié, adaptation au risque. La décomposition vise des garanties et des pratiques distinctes ; mécanismes combinables.
- Appuis directs sur les jalons commerce et l’horizon Oracle EBS ; appui partiel Microsoft/IBM aux régimes différenciés. Comportement adaptatif FLOW : moyens configurables et adaptations voisines documentés, moteur standard de choix du jalon selon risque non démontré.
- Les paramètres de durée, les opérations de gestion, les interfaces et l’emploi d’IA ne sont pas des comportements. Modes Fair Share/Percentage, priorités, lots, réservations réseau ou partielles : périmètres examinés et frontières explicités, sans recopier les regroupements produits.
- Registre structuré : modeles/backlog/reservation-policy-review.yaml. Synthèse dérivée : audits/2026-09-18-reservation-policy/README.md. Absence de preuve d’implémentation Beaumanoir ; aucune exhaustivité absolue revendiquée.''')

    migration = dict(source_refs=['U342'], model_before=str((OUT/'model-before.yaml').relative_to(ROOT)).replace('\\','/'),
        model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(), delta={}, behaviors=[],
        capability=dict(node_id='D05.h', adopted_fields=['name','definition'], value_sha256=cap['lifecycle']['value_sha256']),
        proposed_behaviors=[e['node_id'] for e in entries], proposed_parent_id='D05',
        scope='Capacité adoptée, quatre comportements documentés et proposés ; aucun ancien nœud modifié, aucune publication.')
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]}; new={x['id']:x for x in m[key]}
        migration['delta'][key]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
                                    changed={i:value_hash(new[i]) for i in sorted(new.keys() & old.keys()) if new[i]!=old[i]}, removed=sorted(old.keys()-new.keys()))
    assert not migration['delta']['nodes']['changed'] and not migration['delta']['relations']['changed']
    (OUT/'implementation.yaml').write_text(dumps(migration), encoding='utf-8')
    audit = read(ROOT/'modeles/backlog/behavior-gap-audit.yaml')
    audit['source_refs'] = list(dict.fromkeys(audit['source_refs'] + ['U342']))
    audit['implementation_U342'] = migration
    for index,c in enumerate(comparisons):
        audit['sources'].append(dict(id='S'+str(55+index).zfill(2), vendor=c['vendor'], native_label=c['element_name'], native_id=None,
            url=c['source_url'], edition=c['source_version'], consulted_on=c['consulted_on'], locator=c['source_locator'],
            nature='documentation', access=c['evidence_limits'], observed_fact=c['similarities'], limits=c['differences'], reuse='Synthèse sélective et lien ; aucune importation substantielle.'))
    audit['assessments'].append(dict(capability_id='D05.h', name=fields['name'], existing_behaviors=[e['node_id'] for e in entries],
        candidate_ids=[], verdict='capacité adoptée ; quatre comportements proposés U342',
        diagnosis=rationale, recommendation='Valider les mécanismes et leurs frontières avant de qualifier leur adoption ; D05 reste proposé.', market_sources=['S'+str(55+i).zfill(2) for i in range(len(comparisons))]))
    for e in entries:
        audit['existing_behavior_review'].append(dict(behavior_id=e['node_id'], status='proposed_U342',
            recommendation=e['evidence']+' '+e['boundary'], market_sources=['S'+str(55+i).zfill(2) for i in e['market_indices']]))
    audit['baseline'].update(sha256=sha256((ROOT/'modeles/backlog/model.yaml').read_bytes()).hexdigest(),
        nodes=len(m['nodes']), relations=len(m['relations']), capabilities=sum(n['kind']=='capability' for n in m['nodes']),
        behaviors=sum(n['kind']=='behavior' for n in m['nodes']))
    (ROOT/'modeles/backlog/behavior-gap-audit.yaml').write_text(dumps(audit), encoding='utf-8')
    append('AGENTS.md', '''## Précision Reservation — U339–U342

Reservation sécurise les ressources d’une promesse ; transaction et lock sont des moyens informatiques. Reservation Policy Decision (D05.h) est adoptée en nom/définition U342. D05 comme parent et les quatre comportements BHV032–BHV035 restent proposés ; voir `modeles/backlog/reservation-policy-review.yaml`. Les règles peuvent être conditionnelles dès leur conception ; adaptation ne signifie pas IA. Préserver les frontières ATP, priorités, affectation et protections de groupe ; un changement de politique ne retire pas implicitement les garanties déjà accordées.''')
    append('JOURNAL.md', '''## 2026-09-18 — U342 : Reservation Policy Decision

Nom et définition intégrés ; D05 proposé comme parent. Quatre mécanismes documentés et proposés avec comparaisons marché, exemples, résultats, limites et inventaire des alternatives. Aucun ancien nœud changé ; preuve différentielle dans audits/2026-09-18-reservation-policy/implementation.yaml. Publications inchangées ; Atlas reste sur la release publiée.''')
    print('U342 integrated: 41 capabilities, 26 behaviors including 4 new proposals.')


if __name__ == '__main__':
    main()

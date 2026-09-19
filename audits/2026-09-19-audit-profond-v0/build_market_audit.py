"""Reproduce the audit annex from reviewed evidence; does not modify the model."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps

OUT = Path(__file__).resolve().parent
DATE = '2026-09-19'
model_path = ROOT / 'modeles/backlog/model.yaml'
EXPECTED_MODEL_SHA256 = '2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2'
if hashlib.sha256(model_path.read_bytes()).hexdigest() != EXPECTED_MODEL_SHA256:
    raise RuntimeError('Le modèle a changé depuis la revue : réexaminer les constats avant de régénérer cet audit.')
model = read(model_path)
nodes = {n['id']: n for n in model['nodes']}
baseline = {
    'path': 'modeles/backlog/model.yaml', 'version': model['version'], 'as_of': model['as_of'],
    'sha256_bytes': hashlib.sha256(model_path.read_bytes()).hexdigest(),
    'state': 'backlog courant, non publié par cet audit',
}

vendors = [
    ('SAP', 'SAP S/4HANA aATP / Retail / Fashion', 'S/4HANA ; éditions détaillées par source', 'Promesse, protection, réexamen collectif et release B2B/fashion'),
    ('Oracle', 'Oracle Fusion Cloud SCM / Order Management / Global Order Promising', '26A, 26B et 26C selon document', 'Sourcing, coûts de promesse, retours et compensation'),
    ('Microsoft', 'Dynamics 365 SCM / Commerce / Intelligent Order Management', 'Documentation évolutive ; versions détaillées par source', 'DOM, réservation, calendrier, consignation et intercompany'),
    ('IBM', 'IBM Sterling Order Management', 'Documentation SaaS évolutive ; édition exacte non établie pour les passages retenus', 'Scheduling, règles de fulfillment et alertes'),
    ('Manhattan', 'Manhattan Active Order Management', 'Page produit évolutive, sans édition affichée', 'Sourcing, arbitrage des coûts et retours omnicanaux'),
    ('Blue Yonder', 'Order Promising & Optimization / Smart Disposition / Allocation & Replenishment', 'Pages produit et FAQ évolutives, sans édition affichée', 'Promesse, routage retour et cycle de stock retail'),
    ('RELEX', 'Retail forecasting, replenishment and merchandising planning', 'Pages explicatives évolutives, sans édition logicielle affichée', 'Prévisions externes, implantation, réassort et fin de vie'),
    ('o9', 'Multi-Echelon Inventory Optimization', 'Page solution évolutive sans édition affichée', 'Cibles réseau, risque et scénarios de stock'),
]
references = []
for idx, (org, name, version, role) in enumerate(vendors, 1):
    references.append(dict(id=f'MKT-V0-{idx:02}', name=name, organization=org,
        nature='documentation et présentation de produits, pas catalogue universel de capacités',
        intended_role=role, version=version, consulted_on=DATE,
        access_and_reuse='Synthèses originales et liens uniquement ; aucun droit de redistribution intégrale établi.',
        status='consulted_not_adopted'))
ref_by_vendor = {r['organization']: r['id'] for r in references}
elements = []
comparisons = []

def evidence(vendor, title, url, locator, version, summary, ids, common, diff, adaptation,
             level='passage_consulte', nature='fonction ou mécanisme produit', native=None,
             limit='Documentation officielle consultée ; aucune preuve de déploiement Beaumanoir ni équivalence de taxonomie.'):
    idx = len(elements) + 1
    eid = f'ELM-V0-{idx:02}'
    elements.append(dict(id=eid, reference_id=ref_by_vendor[vendor], native_id=native,
        native_label=title, nature=nature, definition_consulted='Contenu paraphrasé dans reformulation ; aucune définition normative de capacité attribuée.',
        reformulation=summary, source=dict(title=title, url=url, version=version, locator=locator,
        consulted_on=DATE, content_actually_consulted=summary, evidence_level=level,
        access_limit=limit, reuse='Paraphrase courte, lien vers la source ; pas de reproduction substantielle.')))
    cid = f'CMP-V0-{idx:02}'
    comparisons.append(dict(id=cid, external_element_id=eid, flow_element_ids=ids,
        compared_state=baseline, relation='recouvrement_partiel' if ids else 'non_compare',
        context='Contrôle de cohérence et préparation V0 pour PO, experts et architectes solution',
        similarities=common, differences=diff, adaptation_proposed=adaptation,
        justification='Éprouver les résultats métier et interfaces ; conserver les frontières et la maille FLOW.',
        evidence_limit=limit, status='proposed_not_validated', author='Codex', date=DATE,
        validator=None, validated_on=None))
    return eid

sap_bop = 'https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe'
sap_aatp = 'https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5'
evidence('SAP', 'Exploring Backorder Processing', sap_bop,
    'Backorder Processing Overview ; Confirmation Strategies ; Implementing Backorder Processing',
    'Cours S/4HANA Cloud Public Edition évolutif ; pas de numéro de release affiché',
    'BOP réexamine confirmations, priorités et quantités des commandes de vente et de transfert ; les stratégies autorisent différentes dégradations ou améliorations.',
    ['D03.m','D03.n','D03.o','D03.p','D02.e','D04.o','BHV037','BHV047','BHV077'],
    'Réexamen collectif, priorités et engagements protégés sont représentables.',
    'Le processus SAP traverse plusieurs capacités FLOW ; ses stratégies ne sont pas autant de capacités ou de comportements obligatoires.',
    'Éprouver un cas de pénurie avec promesse gelée, nouvelle commande prioritaire et justification des demandes non servies.')
evidence('SAP', 'Using Advanced Available-To-Promise (aATP) in SAP S/4HANA', sap_aatp,
    'Product Availability Check ; Alternative-Based Confirmation ; Release for Delivery',
    'Cours S/4HANA évolutif, plusieurs générations présentées',
    'PAC calcule quantité/date ; ABC étudie sites et produits alternatifs ; Release for Delivery intervient avant livraison.',
    ['D03.i','D03.j','D03.n','D04.o','D04.n','BHV003','BHV039','BHV044','BHV076'],
    'Possibilités, alternatives et autorisation de livraison trouvent des responsables FLOW.',
    'SAP place ABC dans aATP ; FLOW distingue référence admissible et adaptation. La confirmation produit ne dicte pas la séparation FLOW calcul/engagement.',
    'Afficher cette différence sémantique dans les fiches ATP/CTP ; préciser admissibilité des substitutions.')
evidence('SAP', 'Backorder Processing — Supply Assignment',
    'https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html',
    'Requirement Selection ; Requirement Sorting ; Release rule for supply assignment',
    '2025 FPS01 (Feb 2026), version affichée dans le passage indexé',
    'Le passage indexé cite ventes, contrats fashion et transferts, tri des besoins, affectation/désaffectation/réaffectation et contrôle de release.',
    ['D02.e','D03.m','D04.o','BHV039','BHV045','BHV047'],
    'Affecter, réaffecter et autoriser sont couverts.',
    'Les documents et statuts SAP ne définissent pas la maille métier FLOW.',
    'Éprouver une livraison B2B par ensemble assorti ; conserver les critères de complétude à instruire.',
    level='passage_indexe_consulte_ouverture_sans_texte',
    limit='Portail ouvert sans texte extractible ; seuls passages officiels indexés consultés. Pas de validation du paramétrage complet.')
evidence('Oracle', 'Set Up Promising Rules and Sourcing Rules for Order Management',
    'https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/set-up-promising-rules-and-sourcing-rules-for-order-management.html',
    'Introduction ; Create Your Sourcing Rule ; Assign Your Sourcing Rule', 'Oracle Cloud SCM 26A',
    'ATP rules déterminent les ressources considérées ; sourcing rules et assignment sets déterminent les sources, rangs et répartitions applicables.',
    ['D03.i','D03.j','D03.o','D13.a','D11.a'],
    'Admissibilité, provenance, dates de validité et sources sont pertinentes pour FLOW.',
    'Allocation Percent distribue ici les demandes entre sources ; ce n’est pas automatiquement Group Protection ou Supply Assignment.',
    'Documenter la source des règles d’admissibilité et leur validité sans administrer implicitement un maître externe.')
evidence('Oracle', 'Create Alternative Fulfillment Scenarios to Reduce Cost',
    'https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26c/fascp/create-alternative-fulfillment-scenarios-to-reduce-cost.html',
    'Introduction ; cost table ; Promise According to Arrival Date', 'Oracle Cloud SCM 26C',
    'Le PTP décrit recherche un scénario de moindre coût en intégrant coûts article, ressources et transport selon le contexte de promesse.',
    ['D03.k','D03.l','D03.o','D06.e'],
    'Arbitrage économique parmi possibilités et échéances réalisables.',
    'Le moindre coût Oracle est un objectif produit ; FLOW maintient une valeur multidimensionnelle sans poids implicites.',
    'Préciser coûts pertinents, données disponibles, horizon et articulation PTP/décision collective ; ne pas adopter une fonction objectif unique.')
evidence('Oracle', 'Compensate Sales Orders That Change',
    'https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html',
    'Introduction ; example Create Shipment Redo ; compensation pattern', 'Oracle Cloud SCM 26B',
    'Les changements de commande peuvent conduire à mettre à jour, annuler, refaire ou ne pas modifier une étape déjà engagée.',
    ['D04.o','D06.f','D06.d','D07.b','D07.c'],
    'Mutation autorisée, adaptation, orchestration et suivi du réalisé sont séparés dans FLOW.',
    'Les patterns techniques de compensation ne deviennent pas des comportements métier automatiques.',
    'Éprouver annulation après expédition partielle et échec de révocation de prestation ; expliciter effets irréversibles et suites correctrices.')
evidence('Oracle', "Don't Refund Lines That You Return to Your Customer",
    'https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/don-t-refund-lines-that-you-return-to-your-customer.html',
    'Return flows ; orchestration rule for Create Billing Lines', 'Oracle Cloud SCM 26B',
    'Inspection et destination du retour peuvent conditionner le déclenchement de l’avoir ; le document décrit le cas renvoyé au client sans crédit.',
    ['D04.l','D05.i','D07.c','D06.d','BHV053'],
    'Réception, état accepté, disponibilité et suite financière doivent rester distingués.',
    'FLOW exclut le remboursement de ces capacités ; le produit Oracle englobe un traitement financier.',
    'Rendre visible le contrat sortant vers la responsabilité financière/commerciale, sans ajouter Finance au domaine Supply.')
evidence('Oracle', 'Database Promising',
    'https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/fascp/overview-of-database-centric-order-promising.html',
    'Promising Horizon and Other Order Promising Options ; Suppliers and Supplier Capacity', 'Oracle Cloud SCM 26A',
    'Les options de promesse distinguent recherches concurrentes, fuseaux et hypothèse de capacité fournisseur infinie.',
    ['D03.i','D03.j','D06.b','D03.n'],
    'Les hypothèses de capacité et de temps modifient la faisabilité.',
    'FLOW ne présume ni capacité infinie, ni algorithme ou moteur Oracle.',
    'Rendre les hypothèses de capacité, fraîcheur et concurrence explicites dans les exemples V0.')
evidence('Microsoft', 'Order promising',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations',
    'Delivery date control methods ; ATP calculations', 'Documentation évolutive SCM, édition logicielle non unique',
    'ATP cumulé à anticipation considère stock non engagé, réceptions et sorties ; le document distingue délais simples, ATP et CTP.',
    ['D03.i','D03.j','D03.l','BHV001','BHV003','BHV004'],
    'Quantités futures, engagements et délais sont couverts.',
    'Une formule et des limites produit ne prescrivent pas le calcul FLOW ; le CTP FLOW est plus large que la production.',
    'Ajouter une comparaison visible à ATP, en explicitant absence de formule canonique imposée.')
evidence('Microsoft', 'DOM rules', 'https://learn.microsoft.com/en-us/dynamics365/commerce/dom-rules',
    'Common attributes ; Partial orders rule ; Maximum rejects rule ; Offline fulfillment location rule',
    'Documentation mise à jour 2026-01-22 ; paramètres dépendant des versions Commerce',
    'DOM différencie contraintes strictes, partiel/split, indisponibilité des sites et arrêt après rejets répétés.',
    ['D03.o','D03.k','D03.m','D04.n','D04.o','D06.f','BHV039','BHV044','BHV047'],
    'Arbitrer, découper et replanifier après refus sont représentables.',
    'Le moteur DOM implémente ses propres relaxations ; FLOW doit préserver les autorisations sans les copier.',
    'Décrire contraintes impératives/préférences, critères d’arrêt et escalade ; tester absence de solution et rejets multiples.')
evidence('Microsoft', 'Inventory Visibility reservations',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations',
    'Sample use case for soft reservation ; Integrate soft reservations and offsets',
    'SCM 10.0.33+ pour soft reservations sales orders ; dépendances de versions décrites dans la page',
    'La réservation souple coordonne plusieurs canaux ; l’offset lors de réservation physique ou consommation évite un double décompte.',
    ['D02.c','D01.c','D01.f','D01.g','D03.i','D03.n','D05.h'],
    'Engagement de quantité, disponibilité et consommation conservent des effets distincts.',
    'La soft reservation Microsoft n’impose pas une ontologie FLOW soft/hard ni une API particulière.',
    'Éprouver deux demandes concurrentes et une consommation partielle ; rendre explicites reprise/libération, expiration et décompte unique.')
evidence('Microsoft', 'Inventory Visibility inventory allocation',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation',
    'Allocation workflow ; Consume as a soft reservation', 'Documentation évolutive ; UI versions 1 et 2 distinguées',
    'Des enveloppes par groupe et leur consommation sont distinctes des réservations individuelles ; le passage décrit leur articulation.',
    ['D02.b','D05.d','D02.c','BHV017','BHV018'],
    'Protection de groupes, plafonds et engagements individuels sont séparables.',
    'Allocation désigne ici une enveloppe, pas l’affectation FLOW ressources-commandes.',
    'Illustrer un même stock soumis à quota de canal et réservation sans double soustraction.')
evidence('Microsoft', 'Set up consignment',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment',
    'Consignment replenishment orders ; Inventory ownership change journal', 'Documentation évolutive SCM',
    'L’apport fournisseur conserve sa propriété ; un journal de changement de propriété déclenche le traitement d’achat applicable.',
    ['D04.r','D01.h','D04.j','D01.g','BHV061','BHV062','BHV063'],
    'Apport sans achat, propriété et acquisition sont déjà explicitement séparés.',
    'Le scénario Microsoft concerne notamment matières de production ; ni régime fournisseur Beaumanoir ni implémentation imposés.',
    'Conserver le découpage adopté ; éprouver refus, sur-réception, consommation partielle et sortie de consignation.')
evidence('Microsoft', 'Set up a fulfillment source working calendar',
    'https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/setup-fulfillment-source-calendar',
    'Working hours ; time zone ; Using a calendar for Fulfillment optimization ; carrier pickup times',
    'Documentation mise à jour 2026-01-30',
    'Le calendrier décrit ouverture, fermeture, congés et fuseau ; il contraint sélection de source et créneau de collecte.',
    ['D03.i','D03.l','BHV003','D06.b','D06.e','D14.a','D13.a'],
    'Délais réels et possibilités des services relèvent de capacités déjà présentes.',
    'Aucune capacité Calendar Management interne à créer par analogie ; le référentiel peut rester externe.',
    'Établir un contrat temporel : calendriers, cut-off applicable, fuseau, départ/arrivée et repli si donnée inconnue.')
evidence('Microsoft', 'Calculate requested ship dates for purchase orders',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/supplier-requested-confirmed-dates',
    'Key terms and concepts ; calculation logic ; recalculations for updated orders',
    'SCM 10.0.40+ et Planning Optimization, prérequis explicités',
    'Le document distingue dates demandées/confirmées de départ/réception, délais et calendriers fournisseur/entrepôt.',
    ['D04.j','BHV078','D03.l','D05.e','D07.d'],
    'Supplier Confirmation et suivi des ressources attendues permettent cette distinction.',
    'Ne pas généraliser les formules ou automatismes Microsoft à FLOW.',
    'Éprouver une confirmation de départ déplacée avec date de réception inchangée et tracer l’incohérence à arbitrer.')
evidence('Microsoft', 'Cross-Legal-Entity Fulfillment in Dynamics 365 | Preview',
    'https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/08/19/cross-legal-entity-fulfillment-dynamics-365/',
    'What we are releasing ; How it works ; initial release supports retail orders',
    'Annonce officielle du 2026-08-19, Preview ; périmètre initial retail',
    'Le scénario orchestre la vente originale et les achat/vente intercompany en conservant synchronisation et règles par entité.',
    ['D04.i','D04.j','D04.n','D03.o','D09.d','D11.a','BHV069'],
    'Intercompany Sales et liens de composition sont déjà représentables.',
    'Annonce Preview limitée au retail ; aucune disponibilité générale B2B ni promesse de roadmap utilisée comme preuve.',
    'Éprouver la chaîne d’engagements et le changement partiel dans deux entités sans fusionner les Orders.')
ibm_limit = 'Ouverture directe renvoie 403 ; seuls passages indexés officiels consultés. Couverture détaillée et configuration non vérifiées.'
evidence('IBM', 'Scheduling shipment of an order or order line',
    'https://www.ibm.com/docs/en/order-management?topic=shipped-scheduling-shipment-order-order-line',
    'Status control ; Earliest schedule date', 'Documentation SaaS évolutive, release non établie',
    'Le scheduling dépend de l’état de ligne et d’une date minimale évitant de bloquer trop tôt le stock des demandes futures.',
    ['D03.l','D04.o','D05.h','BHV033','BHV039'],
    'Date d’éligibilité, autorisation et horizon de réservation sont distinguables.',
    'Le scheduling Sterling ne correspond pas à une unique capacité FLOW.',
    'Conserver comme corroboration limitée ; approfondir avant équivalence ou sélection produit.',
    level='passage_indexe_consulte_ouverture_403', limit=ibm_limit)
evidence('IBM', 'Defining fulfillment rules',
    'https://www.ibm.com/docs/en/order-management?topic=components-defining-fulfillment-rules',
    'Split partially backordered or unscheduled lines ; use node from work order',
    'Documentation SaaS évolutive, release non établie',
    'Les règles peuvent séparer un reliquat pour chercher une autre source et tenir compte du site associé à une prestation.',
    ['D04.n','D03.o','D06.e','BHV044'],
    'Le découpage préserve lien de demande et recherche de satisfaction.',
    'Règles produit et objets work order ne définissent pas les frontières FLOW.',
    'Tester conservation de quantités/engagements après split ; corroboration limitée.',
    level='passage_indexe_consulte_ouverture_403', limit=ibm_limit)
evidence('IBM', 'Order Hub', 'https://www.ibm.com/docs/en/order-management?topic=features-order-hub',
    'Manage alerts ; Managing exceptions ; sourcing and scheduling rules',
    'Documentation SaaS évolutive, release non établie',
    'Order Hub expose les risques de retard et les erreurs bloquant le fulfillment à traiter par les opérateurs.',
    ['D07.d','D06.f','D06.d','D04.o','BHV082'],
    'Suivi, décision de variation et suspension sont couverts.',
    'Une console et ses alertes ne prouvent pas une capacité autonome Exception Management manquante.',
    'Préciser propriétaire du traitement, criticité, délai, escalade et clôture sans créer une capacité générique par défaut.',
    level='passage_indexe_consulte_ouverture_403', limit=ibm_limit)
commercial_limit = 'Présentation officielle de solution, pas manuel de configuration ni essai ; aucune preuve de performance ou de déploiement Beaumanoir.'
evidence('Manhattan', 'Optimized Fulfillment Sourcing',
    'https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing',
    'Fulfillment Sourcing Optimization ; Improving Profitability ; Ensuring Promises',
    'Page produit évolutive sans numéro de version',
    'Le sourcing annoncé combine promesse, coûts, capacité, risque de rejet et stock ; il recherche aussi moins de splits et des regroupements.',
    ['D03.o','D03.k','D04.n','D06.b','D06.e','D06.f'],
    'Optimisation collective et contraintes opérationnelles sont représentées.',
    'La page mêle décisions et exécution ; sa terminologie optimisation ne dicte ni frontière ni objectif unique FLOW.',
    'Éprouver arbitrage coût/service/stock et regroupement de livraisons ; exposer les raisons de choix et de rejet.',
    level='presentation_consultee', limit=commercial_limit)
evidence('Manhattan', 'Returns Management',
    'https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/returns-management',
    'Returns Done Right ; Maximize Returns Profitability', 'Page produit évolutive sans numéro de version',
    'La destination de retour peut être choisie dynamiquement pour remettre le produit en vente plus vite.',
    ['D05.i','D05.c','D04.l','D06.e','BHV049','BHV050'],
    'Devenir, destination et récupération de valeur sont représentables.',
    'Cette page ne démontre pas toutes les filières réparation/rebut ; ne pas lui attribuer cette couverture.',
    'Tester orientation logistique versus destination et prise en charge de service.',
    level='presentation_consultee', limit=commercial_limit)
evidence('Blue Yonder', 'Order Promising & Optimization',
    'https://blueyonder.com/solutions/order-management-and-commerce/order-promising-and-optimization',
    'Accuracy in delivery dates ; Lower cost to serve ; Smart resource allocation',
    'Page produit évolutive sans numéro de version',
    'La promesse annoncée combine disponibilité, sources, coût, temps de traitement et ressources de livraison.',
    ['D03.i','D03.k','D03.o','D06.b','D06.e'],
    'Les décisions FLOW couvrent les résultats recherchés.',
    'Une promesse de solution ne prouve ni algorithme ni conditions de faisabilité précises.',
    'Exiger des exemples de données et de contraintes pour transformer le rapprochement en conception.',
    level='presentation_consultee', limit=commercial_limit)
evidence('Blue Yonder', 'Smart Disposition',
    'https://blueyonder.com/solutions/returns-management/smart-disposition',
    'Intelligent routing ; Configure and enforce policy ; Customizable reason codes and rules',
    'Page produit évolutive sans numéro de version',
    'Le routage décrit mobilise état, produit et contexte ; l’offre inclut aussi admission et déclenchement du remboursement.',
    ['D05.i','D04.l','D06.e','BHV048','BHV049'],
    'Politique et récupération de valeur se retrouvent dans les deux comportements existants.',
    'Le produit est plus large que le devenir logistique FLOW ; admission et remboursement sont des interfaces distinctes.',
    'Ne pas ajouter les parcours déjà couverts ; préciser les entrées et sorties vers acteurs commerciaux/financiers.',
    level='presentation_consultee', limit=commercial_limit)
evidence('Blue Yonder', 'What is Blue Yonder Allocation & Replenishment?',
    'https://info.blueyonder.com/retail-planning-category-management/what-is-blue-yonder-allocation-replenishment',
    'Key Capabilities 1–4 ; Push vs Pull ; lifecycle', 'FAQ produit 2026, édition logicielle non indiquée',
    'L’offre décrit apports initiaux et continus, tailles/conditionnements, contraintes de place et lissage des réceptions.',
    ['D05.a','D05.g','D05.e','D05.c','D05.f','D08.d','D06.b'],
    'Implantation, réassort, redistribution et variantes existent dans FLOW.',
    'Une offre intégrée n’exige pas leur fusion ; courbes de tailles et lissage sont des contraintes à instruire.',
    'Tester le résultat par taille/couleur/magasin et le partage de capacité entre implantation et réassort.',
    level='presentation_consultee', limit=commercial_limit)
evidence('RELEX', 'AI-driven forecasting & replenishment for retail profitability',
    'https://www.relexsolutions.com/resources/ai-driven-retail-forecasting-and-replenishment/',
    'How RELEX helps ; 6 keys ; seasonal planning', 'Article évolutif, édition logicielle non indiquée',
    'Prévisions, saisonnalité, promotions, stock, contraintes opérationnelles et scénarios alimentent les décisions retail.',
    ['D05.a','D05.e','D05.g','D05.f','D06.b'],
    'Les décisions de stock consomment besoins et contraintes.',
    'Prévision, prix et planification commerciale dépassent le périmètre Supply transactionnel retenu.',
    'Rendre le contrat entrant prévisions/assortiments visible, sans ajouter implicitement Demand Planning ou Pricing.',
    level='presentation_consultee', limit=commercial_limit)
evidence('RELEX', 'Capabilities to prioritize when implementing merchandising systems',
    'https://www.relexsolutions.com/resources/which-capabilities-to-prioritize-when-implementing-merchandising-systems/',
    'Traditional processes ; initial allocation ; final allocation ; evolution of merchandising',
    'Article expert officiel, pas catalogue normatif de capacités ni version logicielle',
    'L’article distingue assortiment, apports initiaux, réassort et distribution finale ; la prévision peut contribuer à plusieurs décisions.',
    ['D05.g','D05.e','D05.c','D05.f','BHV025'],
    'Finalités initiales, continues et consolidation sont déjà différenciées.',
    'Les systèmes éditeurs agrègent des responsabilités ; la distribution finale n’est pas automatiquement Stock Consolidation.',
    'Éprouver une fin de saison : pousser un reliquat entrepôt, regrouper des tailles et arrêter le réassort selon leurs finalités.',
    level='passage_consulte_article_expert', limit=commercial_limit)
evidence('o9', 'How o9’s Multi-Echelon Inventory Optimization (MEIO) Software Works',
    'https://o9solutions.com/solutions/supply-chain-planning/multi-echelon-inventory-optimization-docs',
    'Optimal Inventory Targets and Network Rebalancing ; Postponement ; Scenario Planning for Inventory Risk',
    'Page solution évolutive, sans édition logicielle malgré le suffixe docs',
    'L’offre décrit cibles réseau, rééquilibrage, report de l’engagement, risques de délai et scénarios.',
    ['D05.a','D05.c','D05.f','D05.h','BHV028','BHV033','BHV035'],
    'MEIO et arbitrage disponibilité/immobilisation/risque existent déjà.',
    'Le périmètre produit mêle cible, action et promesse ; aucune preuve de formulation mathématique détaillée.',
    'Tester cohérence de cibles multi-échelons et incertitudes sans créer un nouveau domaine MEIO.',
    level='presentation_consultee', limit=commercial_limit)

for ref in references:
    owned = [e for e in elements if e['reference_id'] == ref['id']]
    ref['official_sources'] = [e['source']['url'] for e in owned]
    ref['content_actually_consulted'] = [e['id'] for e in owned]

findings = [
    dict(id='MKT-F01', priority='P1', title='Contrat temporel de promesse et de service insuffisamment explicite',
        category='insuffisance_description_interface', nodes=['D03.i','D03.l','BHV003','D06.b','D06.e','D14.a','D13.a'], evidence=['ELM-V0-14','ELM-V0-15','ELM-V0-08'],
        observation='Aucune occurrence de calendrier, calendar, cut-off ou fuseau dans les champs definition/scope/finality des nœuds. BHV003 couvre les délais réels, mais pas le contrat de calcul du temps.',
        recommendation='Préciser source des calendriers, jours fermés, heure limite, fuseau, date départ/réception, fraîcheur et conduite sur donnée inconnue ; consommer un maître externe.',
        acceptance='Un exemple vendredi après cut-off avec fermeture lundi aboutit à une promesse expliquée ; les lecteurs identifient responsable et données sans supposer un simple ajout de jours.',
        boundary='Aucune nouvelle capacité Calendar Management proposée ; absence de mot ne suffit pas à conclure absence fonctionnelle.'),
    dict(id='MKT-F02', priority='P1', title='PTP, priorités et échéancier restent trop peu définis pour une revue solution',
        category='insuffisance_description', nodes=['D03.k','D03.l','D03.m','D03.o'], evidence=['ELM-V0-01','ELM-V0-05','ELM-V0-10','ELM-V0-20'],
        observation='D03.l et D03.m ont un scope limité à un exemple fictif. D03.k expose une frontière et un exemple, sans inputs, résultat argumenté, coûts ni gestion des préférences incompatibles.',
        recommendation='Expliciter question, entrées, contraintes impératives, préférences, résultat, justification et absence de solution. Séparer choix économique PTP et compromis collectif multidimensionnel.',
        acceptance='Un même jeu de demandes permet de distinguer priorité, échéancier et arbitrage économique, sans fixer de pondération métier par défaut.',
        boundary='Le marché justifie les responsabilités, pas une formule unique ni de nouveaux comportements par critère.'),
    dict(id='MKT-F03', priority='P1', title='Réservation, affectation, promesse et consommation : contrat commun à rendre éprouvable',
        category='contrat_transverse_a_preciser', nodes=['D02.c','D02.e','D01.c','D01.g','D03.i','D03.n'], evidence=['ELM-V0-11','ELM-V0-12','ELM-V0-08'],
        observation='Les responsabilités sont distinctes ; plusieurs relations gardent la formulation engagements opposables selon frontière à arbitrer. Le contrat quantitatif de passage vers consommation reste un point V0 à expliciter.',
        recommendation='Fixer pour chaque quantité l’effet sur disponibilité, son identité, libération/expiration, consommation partielle et échec de confirmation ; distinguer engagement logique et ressources physiques.',
        acceptance='Deux canaux promettant la dernière quantité, puis une expédition partielle, ne la comptent ni deux fois disponible ni deux fois indisponible.',
        boundary='Pas de réservation obligatoire ou taxonomie soft/hard imposée ; tester les mécanismes choisis et leurs limites.'),
    dict(id='MKT-F04', priority='P1', title='Changements en cours d’exécution et exceptions : fermer la boucle de responsabilité',
        category='contrat_transverse_a_preciser', nodes=['D04.o','D06.f','D06.d','D07.b','D07.c','D07.d'], evidence=['ELM-V0-06','ELM-V0-10','ELM-V0-19'],
        observation='Tracking, adaptation et orchestration sont présents et reliés. Les textes ne forment pas encore un cas de preuve complet sur refus répétés, annulation trop tardive et réalisé irréversible.',
        recommendation='Éprouver seuil d’arrêt, acteur de résolution, latitude de dérogation, prestation déjà exécutée, correction/compensation et révision de promesse.',
        acceptance='Un rejet répété n’entraîne pas une boucle indéfinie ; une demande annulée après sortie physique conserve les faits et identifie la suite responsable.',
        boundary='Pas de nouveau domaine générique Exception Management déduit d’une console éditeur ; les seuils restent à arbitrer.'),
    dict(id='MKT-F05', priority='P1', title='Prévisions, assortiment, saison et coûts externes : entrées à rendre visibles',
        category='interface_externe_manquante_ou_peu_valorisee', nodes=['D05.a','D05.g','D05.e','D05.f','D03.k','D08','D12','D11'], evidence=['ELM-V0-25','ELM-V0-26','ELM-V0-05'],
        observation='D05.g consomme un assortiment retenu et D05.f les hypothèses/prévisions ; aucun élément explicitement nommé Demand Forecast ou Assortment Plan dans le catalogue. Le coût consommé par PTP n’a pas de contrat dédié lisible.',
        recommendation='Décrire dans une vue de contexte les producteurs externes à identifier, version/horizon/maille, données absentes et retours vers eux ; ne pas attribuer de maître sans preuve.',
        acceptance='Un expert peut dire d’où viennent besoins, assortiment et coûts, et distinguer prévision, engagement fournisseur et demande ferme sans ajouter Demand Planning à FLOW.',
        boundary='Finance, prévision commerciale, assortiment et saison ne deviennent pas de nouveaux domaines par comparaison éditeur.'),
    dict(id='MKT-F06', priority='P1', title='Retours : interface admission/remboursement/remplacement à expliquer',
        category='interface_externe_peu_valorisee', nodes=['D04.l','D04.m','D05.i','D07.c','D06.d','BHV053','BHV055','BHV056'], evidence=['ELM-V0-07','ELM-V0-21','ELM-V0-23'],
        observation='Les parcours et décisions logistiques sont riches ; les textes excluent explicitement autorisation commerciale, remboursement et remplacement client. Ces exclusions doivent déboucher sur des interfaces expliquées.',
        recommendation='Présenter l’origine de l’autorisation et les faits/quantités transmis aux responsables des suites commerciales/financières ; distinguer réparation même bien et remplacement.',
        acceptance='Un retour partiellement accepté puis partiellement renvoyé au client ne vaut pas remboursement total ; responsable et événement justificatif sont identifiés.',
        boundary='Aucun domaine Finance ni remboursement ajouté à Return Disposition Decision ; aucune pratique Sarenza supposée.'),
    dict(id='MKT-F07', priority='P2', title='Fashion et B2B : compléter les cas de preuve, pas multiplier les capacités',
        category='scenario_de_completude', nodes=['D05.g','D05.e','D05.c','D04.n','D04.o','D04.i','D04.j','BHV039','BHV069'], evidence=['ELM-V0-03','ELM-V0-16','ELM-V0-24','ELM-V0-26'],
        observation='Tailles, couleurs, conditionnements, assortiment utile, intercompany et complétude sont déjà mentionnés. La fin de saison et la synchronisation de la chaîne B2B nécessitent une démonstration transversale.',
        recommendation='Éprouver pack indivisible, assortiment incomplet, reliquat de fin de saison, livraisons groupées et changement d’Order intercompany ; préciser intention de chaque apport.',
        acceptance='Le cas distingue implantation, réassort, redistribution et affectation ; il identifie la demande non satisfaite à la maille taille/ligne sans accord implicite sur les règles.',
        boundary='La final allocation éditeur n’est pas automatiquement la Stock Consolidation FLOW ; la frontière doit être décidée au cas métier.'),
    dict(id='MKT-F08', priority='P2', title='Capacité opérationnelle disponible et concurrence à éprouver',
        category='contrat_transverse_a_preciser', nodes=['D06.b','D06.e','D07.b','D03.i','D03.o','D05.f'], evidence=['ELM-V0-08','ELM-V0-20','ELM-V0-22','ELM-V0-24'],
        observation='D06.b distingue correctement plafond, charge et disponible communiqué et exclut une réservation implicite ; la concurrence de plans utilisant un même créneau reste à démontrer.',
        recommendation='Préciser qui atteste et engage la capacité, avec unité, créneau, fraîcheur et réponse de prise en charge ; signaler conditionnel ou inconnu.',
        acceptance='Deux décisions consommant simultanément un créneau limité ne confondent pas information de capacité et engagement confirmé.',
        boundary='Ne pas inventer Capacity Reservation dans FLOW si l’engagement reste chez l’exécutant ; identifier cette dépendance externe.'),
    dict(id='MKT-F09', priority='P1', title='Comparaisons marché des fiches trop inégales pour la V0',
        category='valorisation_preuve', nodes=['D03.i','D03.k','D03.l','D03.m','D03.n','D02.b','D02.c','D05.d','D06.b'], evidence=['ELM-V0-01','ELM-V0-05','ELM-V0-09','ELM-V0-11','ELM-V0-12','ELM-V0-14'],
        observation='Ces capacités n’ont pas de fields.market_comparisons dans le modèle lu alors que l’audit dispose de rapprochements précis. Cela mesure une documentation locale, jamais une absence marché.',
        recommendation='Après revue, reporter les rapprochements utiles et leurs limites dans les fiches selon U311 ; conserver les correspondances proposées tant qu’elles ne sont pas validées.',
        acceptance='Chaque fiche prioritaire montre au moins un appui pertinent, sa différence avec FLOW et sa date ; aucune étiquette validée ou réalisée déduite.',
        boundary='Cet audit écrit une annexe isolée ; il ne modifie pas les champs modèle ni les registres MKT/ELM/CMP existants.'),
]

axes = [
 ('Promesse de référence et future', ['D03.i','D03.n','D01.c'], [2,4,9,11], 'couvert au niveau des responsabilités ; contrat temporel à préciser'),
 ('Adaptations et alternatives de satisfaction', ['D03.j','D06.e','D06.f'], [2,8,10], 'couvert ; ABC SAP traverse la frontière ATP/CTP FLOW'),
 ('Arbitrage économique et priorités', ['D03.k','D03.l','D03.m','D03.o'], [1,5,10,20,22], 'couvert ; descriptions D03.k/l/m trop brèves'),
 ('Protection, plafonds, réservations', ['D02.b','D02.c','D05.d','D05.h'], [11,12,17,27], 'couvert ; contrat de décompte et validité à éprouver'),
 ('Backlog collectif et réaffectation', ['D03.p','D03.o','D02.e','D04.o'], [1,3,10], 'couvert ; scénario de pénurie/gels à éprouver'),
 ('Cibles locales et multi-échelons', ['D05.a','BHV026','BHV027','BHV028'], [25,27], 'couvert ; entrée prévision et hypothèses à expliciter'),
 ('Implantation et réassort', ['D05.g','D05.e','D05.f'], [24,25,26], 'couvert ; contraintes tailles/capacité et articulation à tester'),
 ('Redistribution et fin de saison', ['D05.c','BHV024','BHV025'], [24,26,27], 'couvert partiellement ; qualification des apports finaux à instruire'),
 ('Consignation et propriété', ['D01.h','D04.r','D04.j','D01.g'], [13], 'couvert ; pas de manque de capacité établi'),
 ('Orders, composition et intercompany', ['D04.i','D04.j','D04.k','D04.n','D04.o'], [3,10,15,16,18], 'responsabilités représentées ; Transfer Order non re-comparé finement ; synchronisation et partiel à tester'),
 ('Retours et récupération de valeur', ['D04.l','D04.m','D05.i'], [7,21,23], 'retour client et disposition rapprochés ; Supplier Return non re-comparé ; interfaces externes à représenter'),
 ('Exécution, services et exceptions', ['D06.d','D06.e','D06.f','D07.b','D07.c','D07.d'], [6,10,19,20], 'couvert ; scénarios de compensation/escalade à expliciter'),
 ('Temps et capacité opérationnelle', ['D06.b','D13.a','D14.a','BHV003'], [8,14,15,20,22], 'responsables présents ; contrats sources/dates/capacité insuffisamment précis'),
 ('Prévisions, assortiment et coûts', ['D05.a','D05.g','D05.e','D03.k'], [5,25,26], 'interfaces externes à expliciter ; nouveaux domaines non justifiés'),
 ('Maîtres et projections référentielles', ['D08.d','D09.d','D11.a','D12.a','D13.a','D14.a'], [4,13,14,16,24], 'appuis partiels sur usages ; ingestion/mastering non comparés finement'),
 ('Comptage, archivage et traçabilité des mouvements', ['D01.d','D04.q','D01.g'], [], 'non comparé à nouveau dans ce volet ; comparaisons existantes non revalidées ici'),
]
axis_records = [dict(id=f'AX-V0-{idx:02}', name=name, flow_element_ids=ids,
                    evidence_ids=[f'ELM-V0-{x:02}' for x in es], assessment=assessment)
                for idx,(name,ids,es,assessment) in enumerate(axes,1)]
cap_matrix = []
for node in model['nodes']:
    if node['kind'] != 'capability':
        continue
    nid = node['id']
    hits = [c['id'] for c in comparisons if nid in c['flow_element_ids']]
    existing = node['fields'].get('market_comparisons', [])
    cap_matrix.append(dict(id=nid, name=node['fields']['name'], revision=node.get('revision'),
        fields_sha256_canonical=hashlib.sha256(json.dumps(node['fields'], ensure_ascii=False, sort_keys=True, separators=(',',':')).encode('utf-8')).hexdigest(),
        existing_market_comparisons=len(existing), existing_vendors=sorted({x.get('vendor','') for x in existing}),
        audit_comparison_ids=hits,
        audit_status='rapprochement_propose' if hits else 'non_recompare_dans_ce_volet',
        limit='Une correspondance multi-capacités ne prouve pas tous les champs, comportements ou réalisations.'))

doc = dict(audit_id='AUDIT-MARCHE-EDITEURS-V0-20260919', date=DATE, status='proposed_not_validated',
    authority='Annexe de preuve pour audit ; aucun catalogue modèle concurrent et aucune adoption implicite.',
    scope='8 éditeurs, 27 éléments officiels et 16 axes ; diversité de rôles, pas exhaustivité produit ou du marché.',
    compared_model=baseline,
    evidence_counts=dict(vendors=8, unique_urls_attempted=27, full_text_opened=23,
        documentation_course_or_technical_announcement=15, solution_presentation=7,
        expert_article=1, indexed_passages_only=4, comparisons=27,
        axes=16, capabilities_in_matrix=47, capabilities_with_proposed_comparison=41),
    methodology=['marche/methode.md','CONVENTIONS-MODELE.md sections 2–5','AGENTS.md'],
    limitations=[
        'Le volet couvre fonctions documentées et frontières du backlog ; il ne prouve aucune réalisation Beaumanoir.',
        'Sarenza reste non évalué ; les scénarios proposés sont fictifs.',
        'IBM et un passage SAP sont limités aux extraits officiels indexés après échec de lecture complète.',
        'Manhattan, Blue Yonder, RELEX et o9 apportent surtout présentations et articles officiels ; aucun algorithme ni résultat installé confirmé.',
        'Ce volet ne revalide pas exhaustivement chaque comparaison historique ni chaque condition contractuelle éditeur.',
        'L’absence d’un nom ou d’un champ ne prouve pas un manque fonctionnel ; les écarts distinguent description, interface et responsabilité.',
        'Aucun P0 ni nouveau domaine nécessaire établi par ce volet marché. Les P1 concernent la préparation de la présentation V0.',
        'La clôture historique U431 reste préservée ; ceci répond à une nouvelle demande d’audit, sans modifier son registre.',
    ], references=references, external_elements=elements, comparisons=comparisons,
    coverage_axes=axis_records, capability_matrix=cap_matrix, findings=findings)

OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'marche-editeurs.yaml').write_text(dumps(doc), encoding='utf-8')

def source_link(eid):
    e = next(e for e in elements if e['id'] == eid)
    return f"[{eid} — {e['source']['title']}]({e['source']['url']})"

empty = [n for n in cap_matrix if n['existing_market_comparisons'] == 0]
covered = [n for n in cap_matrix if n['audit_comparison_ids']]
md = [
 '# Audit V0 — comparaison large des éditeurs', '',
 f"État comparé : backlog `{baseline['version']}` (`as_of: {baseline['as_of']}`), lu le {DATE}. Empreinte des octets : `{baseline['sha256_bytes']}`.", '',
 'Dans le périmètre Supply retenu et les sources consultées, les grandes responsabilités étudiées trouvent des correspondances dans FLOW. Ce volet ne démontre aucun grand manque de domaine ni anomalie P0 ; il ne prouve pas la complétude du modèle ou du marché. Pour une V0 présentable, le travail prioritaire porte sur les contrats entre responsabilités, quelques définitions trop courtes et les interfaces avec les activités exclues.', '',
 f"**8 éditeurs, {len(elements)} éléments officiels consultés, {len(axes)} axes et les {len(cap_matrix)} capacités passées en matrice.** {len(covered)} capacités ont un nouveau rapprochement proposé dans ce volet ; les autres sont explicitement non re-comparées. {len(empty)} fiches capacité n’ont actuellement aucun `fields.market_comparisons` : c’est une mesure de documentation locale, pas de couverture marché.", '',
 'Sur les 27 URL uniques ayant fait l’objet d’une tentative d’ouverture, **23 textes ont effectivement été lus** (15 documentations, cours ou annonce technique, 7 présentations de solution et 1 article expert) ; **4 preuves restent limitées aux passages officiels indexés** (SAP Help sans texte extractible et 3 pages IBM en erreur 403).', '',
 'La preuve détaillée et les correspondances audit-locales MKT-V0/ELM-V0/CMP-V0 sont dans [marche-editeurs.yaml](marche-editeurs.yaml). Ce document explique les résultats ; le modèle demeure `modeles/backlog/model.yaml`. Aucun champ du catalogue, accord historique, publication ou registre marché partagé n’est modifié.', '',
 '## Portée et qualité des preuves', '',
 '| Éditeur | Rôle dans le contrôle | Nature de preuve |', '| --- | --- | --- |',
]
for r in references:
    level = 'Cours et documentation ; un extrait Help limité' if r['organization']=='SAP' else 'Documentation technique officielle' if r['organization'] in ['Oracle','Microsoft'] else 'Extraits officiels indexés ; ouverture 403' if r['organization']=='IBM' else 'Présentation produit / article officiel, sans test'
    md.append(f"| {r['organization']} | {r['intended_role']} | {level} |")
md += ['', 'Une fonctionnalité produit peut traverser plusieurs capacités FLOW. La comparaison porte sur résultat, responsabilité et contexte, jamais sur une équivalence de niveaux. Les pages commerciales corroborent une finalité, sans prouver un algorithme, un paramétrage ni une performance. L’annonce Microsoft intercompany reste une **Preview** limitée initialement aux commandes retail. Les passages IBM ne permettent pas une conclusion sur la totalité du produit. Les versions et localisateurs sont conservés par source.', '',
       '## Matrice de couverture par axe', '', '| Axe | Éléments FLOW | Appréciation | Preuves |', '| --- | --- | --- | --- |']
for a in axis_records:
    md.append(f"| {a['name']} | {', '.join(a['flow_element_ids'])} | {a['assessment']} | {', '.join(a['evidence_ids']) or 'Non re-comparé'} |")
md += ['', '## Écarts à traiter ou arbitrer', '']
for f in findings:
    md += [f"### {f['id']} — {f['priority']} — {f['title']}", '',
           f"**Constat FLOW.** {f['observation']}", '',
           f"**Recommandation proposée.** {f['recommendation']}", '',
           f"**Preuve attendue pour la V0.** {f['acceptance']}", '',
           f"**Frontière.** {f['boundary']}", '',
           'Appuis consultés : '+ '; '.join(source_link(e) for e in f['evidence'])+'.', '']
md += ['## Ce que le marché ne justifie pas d’ajouter', '',
       '- Un domaine ATP avancé : SAP aATP est un regroupement produit ; ATP, CTP, protections, priorités, affectation et promesse ont des frontières explicites dans FLOW.',
       '- De nouveaux comportements de retours par code éditeur : D04.l, D04.m et D05.i couvrent déjà parcours, politiques et récupération de valeur.',
       '- Un domaine MEIO : BHV028 est déjà rattaché à Inventory Target Decision ; o9 ne justifie pas d’en faire une nouvelle hiérarchie.',
       '- Forecasting, Pricing, Finance, atelier de production ou WMS internes : les interfaces peuvent être nécessaires, leur réalisation demeure hors périmètre retenu.',
       '- Une capacité par écran, algorithme, taille, seuil, canal ou type d’erreur. Démontrer d’abord une responsabilité durable ou un bénéfice de décomposition.', '',
       '## Compléments non couverts par cette comparaison', '',
       'La matrice n’est ni un benchmark de sélection produit ni une preuve d’exhaustivité du marché. Les six capacités sans nouvelle correspondance sont Stocktaking (D01.d), Transfer Order (D04.k), Supplier Return (D04.m), Service Requirements Decision (D07.a), Catalog Ingestion (D12.a) et Order Archiving (D04.q). Leur présence dans un axe apporte le contexte FLOW, sans nouvelle validation marché détaillée. Les comparaisons déjà inscrites sur leurs fiches restent dans leur état antérieur. Les rapprochements sur les autres ingestions portent surtout sur les informations utilisées, pas sur le mastering. Les interfaces retail/B2B et les scénarios de retour sont à éprouver avec les experts ; aucun existant Sarenza ou déploiement Beaumanoir n’est inféré.', '',
       '## Index des passages effectivement consultés', '',
       '| ID | Source et passage | Édition / accès |', '| --- | --- | --- |']
for e in elements:
    s=e['source']
    md.append(f"| {e['id']} | [{s['title']}]({s['url']}) — {s['locator']} | {s['version']} ; {s['evidence_level']} |")
md += ['', f"Consultation de chaque source : {DATE}. Les synthèses sont originales et courtes ; aucun droit de redistribution intégrale du contenu tiers n’est présumé.", '']
(OUT / 'marche-editeurs.md').write_text('\n'.join(md), encoding='utf-8')
print(json.dumps({'references':len(references),'elements':len(elements),'comparisons':len(comparisons),
 'axes':len(axes),'capabilities':len(cap_matrix),'new_comparison_capabilities':len(covered),
 'capabilities_without_existing_market_comparisons':len(empty),'findings':len(findings),
 'model_sha256':baseline['sha256_bytes']},ensure_ascii=False))

# Frontières, contrats et cas d’épreuve

**Audit clos U431.** Tous les candidats sont intégrés, couverts par l’existant ou retirés. P04/P10/P12 ne créent aucun comportement supplémentaire. Frontière commerciale et financière externe à Supply ; règles et contrats détaillés conservés comme travaux ultérieurs non bloquants. [Bilan de clôture](cloture-U431.md). Les états et propositions antérieurs ci-dessous conservent leur portée historique.

**État courant U427 :** Replenishment Decision porte Requirement-based Replenishment (BHV083), Target-based Replenishment (BHV084) et Replenishment Adjustment (BHV085). Deux politiques et un mécanisme combinable ; noms, définitions présentées et rattachements adoptés. Exemples, justifications et comparaison Microsoft documentés avec leur portée éditoriale. P01–P03 sont intégrés : le point réassort est clos. Les autres arbitrages de l’audit restent distincts ; les conclusions antérieures de non-décomposition et de réouverture ci-dessous sont historiques.

**État courant U424 :** Lifecycle unique en D04 avec six dimensions et leurs états explicites. Rescheduling BHV041 est intégré à Preparation & Revision BHV038 ; Cancellation BHV042 est intégré à Termination BHV043, avec distinction entre annulation et clôture. Les anciens identifiants sont conservés dans les preuves et ne sont pas réutilisés. D03 mobilise Lifecycle ; D06 garde orchestration et réalisations. Nouvelles formulations et listes détaillées éditoriales. Les décompositions antérieures ci-dessous sont historiques.

**État courant U420 :** Order Archiving appartient à D03 ; Order Lifecycle Management appartient à D04, avec Order Release. Structuring et Split restent dans D03. Identifiants, définitions et parents des comportements conservés. Les mentions U417/U418 ci-dessous sont historiques et remplacées sur ces rattachements. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml).

**État courant U417/U418 :** dans D03 Order Backlog Management, Structuring porte Order Splitting et Lifecycle porte Order Release. Les capacités D04.n/D04.o conservent leurs identifiants historiques. Planning prépare les scénarios ; Lifecycle autorise ; Process Orchestration coordonne les services. Gel et suspension sont combinables, sans séquence universelle. Aucun ajout de nœud ou comportement ; arbitrage de placement du carnet résolu. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml). Les anciens rattachements ci-dessous sont historiques.

**État courant U414 :** Order Backlog Planning (D03.p) est créé dans D03. Order Release BHV039 y est déplacé, identité et définition conservées. Lifecycle conserve huit comportements ; Split et Structuring restent en D04 pour le prochain arbitrage. Planning mobilise les décisions et prépare la prise en charge ; affectation, promesse et orchestration gardent leurs responsabilités. Aucun comportement supplémentaire : 47 capacités et 73 comportements. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml). Les anciens rattachements ci-dessous restent historiques.

**État courant U413 :** D03 devient Order Backlog Management. Le travail collectif du carnet prépare son engagement vers les processus, en mobilisant les décisions spécialisées. D04 conserve la demande par intention. Réexamen ciblé de Lifecycle/Structuring : parents inchangés, aucune nouvelle capacité ou comportement. P11 demeure intégré à Order Release ; son placement côté carnet reste à concrétiser. [Mandat, comparaison et réexamen](../../modeles/backlog/order-backlog-review.yaml). Les noms et positions des états précédents sont historiques.

**État courant U410 :** P11 est résolu par enrichissement d’Order Release (BHV039) : conditions individuelles et collectives, complétude, éléments indispensables et traitement partiel. Aucun comportement ajouté ; autorisation distincte de l’affectation et de Process Orchestration. Autoriser ensemble ne signifie pas démarrer simultanément. Les mentions antérieures de P11 ouvert sont historiques. [Accord et comparaison](../../modeles/backlog/order-lifecycle-behaviors.yaml).

**État courant U409 :** le Process orchestre des Services. D06 devient Process Management ; Process Orchestration et Process Adaptation Decision restent distincts. Operations Tracking porte les trois visibilités physiques et Process Tracking. Neuf noms adoptés ; Service Catalog Ingestion et Service Reconciliation sont deux intitulés dérivés proposés. Aucun ajout de comportement ni changement de responsabilité. Les intitulés des états datés ci-dessous restent historiques. [Convention et comparaison](../../modeles/backlog/execution-services-review.yaml).

**État courant U406 :** 47 capacités et 74 comportements. Warehouse Visibility, Transportation Visibility, Store Visibility et Business Process Tracking intégrés sous Execution Tracking (BHV079–082). Tasks et appels sont des objets suivis, pas des niveaux de comportement. Digital Service Visibility est remplacé ; le besoin numérique demeure couvert. [Portées et comparaison](../../modeles/backlog/execution-services-review.yaml). Les propositions et mentions de non-intégration ci-dessous sont historiques.

**État courant U403 :** 47 capacités et 74 comportements. Supplier Confirmation (BHV078) complète Purchase Order et résout A06 sur le catalogue : demande, réponse fournisseur et engagement accepté distincts ; impacts, mutations et promesse client gardent leurs responsables. Refuser un report ne supprime pas le risque annoncé. [Explication et comparaison](../../modeles/backlog/purchase-order-behaviors.yaml). Les mentions antérieures d’un point A06 ouvert restent historiques.

**État courant U402 :** 47 capacités et 74 comportements. Les trois mécanismes CTP BHV075–077 sont intégrés : ressources supplémentaires, alternatives de satisfaction et réexamen d’engagements. P14–P16 ne sont plus conditionnels ; A05 est résolu sur la frontière de catalogue, les règles détaillées restant distinctes. Fulfillment Plan Decision conserve le choix collectif. [Portée et comparaison](../../modeles/backlog/d03-review.yaml). Les états datés ci-dessous conservent leur valeur historique.

**État courant U391 :** Purchase Order porte Stock Procurement, Direct Delivery et Service Procurement (BHV058–060). Consignation instruite séparément dans la gestion du stock. [Accord et intégration](../2026-09-18-purchase-order-U391/README.md).

**État courant U388 :** Return for Repair (BHV057) complète Supplier Return : restitution attendue du même bien réparé, distincte du remplacement. L’ajout n’est plus conditionnel ; achats de prestation et exécution conservent leurs responsabilités. [Portée de l’ajout](../2026-09-18-supplier-repair-U388/README.md).

**État courant U387 :** Supplier Return porte Return for Credit et Return for Replacement (BHV055–056), distingués par l’apport de remplacement attendu. Finance, achat et exécution restent distincts. [Accord et intégration](../2026-09-18-supplier-return-U387/README.md).

**État courant U385 :** définition élargie de Customer Return et cinq parcours combinables adoptés : Return to Stock, Repair and Refurbishment, Return to Supplier, Return to Customer et Scrapping (BHV050–054). Les axes commerciaux et les autres filières restent à instruire. [Accord et intégration](../2026-09-18-customer-return-U385/README.md).

**État courant U384 :** noms courts Sales Order, Purchase Order, Transfer Order, Customer Return et Supplier Return adoptés. Cinq parcours Customer Return détaillés en proposition dans `modeles/backlog/customer-return-behaviors.yaml`, sans ajout au catalogue à ce stade. [Nommage et étude](../2026-09-18-customer-return-U384/README.md).

**État courant U383 :** cinq capacités par type d’Order sont rétablies sous D04 ; Order Type D04.p est retiré. Lifecycle, Structuring et Archiving restent transverses. Return Disposition Decision porte Policy-based Disposition et Value Recovery Optimization (BHV048–049). Les prises en charge des retours restent à détailler. Les états datés ci-dessous sont historiques. [Portée et comparaison](../2026-09-18-orders-disposition-U383/README.md).

**État courant U380 :** Return Disposition Decision (D05.i) est adoptée sous Inventory Optimization, sans comportement. A04 est résolue sur le devenir logistique du bien ; autorisation commerciale, remboursement et remplacement client restent distincts. [Accord et intégration](../2026-09-18-return-disposition-U380/README.md).

**État courant U378 :** Fulfillment Plan Decision (D03.o) produit le scénario collectif ; D03 porte le nom adopté Fulfillment Optimization. A02 est résolue sur la responsabilité ; les contrats détaillés restent proposés. Aucun sous-niveau ou comportement ajouté. Les états U364 et antérieurs ci-dessous sont historiques. [Accord et intégration](../2026-09-18-fulfillment-plan-U378/README.md).

**État courant U364 :** Supply Assignment porte application d’un plan, complément préservant les affectations et réaffectation des liens modifiables (BHV045–BHV047). La distinction stabilité/adaptation est adoptée ; les décisions spécialisées et Freezing gardent leurs responsabilités. A01/A02 restent ouverts. [Portée et comparaison](../2026-09-18-supply-assignment-U364/README.md).

**État courant U363 :** D04 comporte Order Type (cinq variantes), Order Lifecycle Management (neuf comportements), Order Structuring et Order Archiving. Split est une mutation avec filiation ; Spread concerne l’affectation des ressources entre Orders. Les états datés ci-dessous sont historiques. [Refonte et portée](../2026-09-18-d04-U363/README.md).

**Validation U350 :** Order Freezing est le nom adopté pour BHV037. Le principe et le parent U349 sont conservés ; les détails et contrats restent proposés.

**État courant U349 :** Order Lifecycle Management porte Order Firming (BHV036) et la protection contre les réoptimisations (BHV037, nom éditorial Order Freezing). Affermissement, gel et mise en attente sont distincts. Accord et limites dans `modeles/backlog/order-lifecycle-behaviors.yaml` ; P11 reste ouvert. Catalogue : 41 capacités et 28 comportements.

**Clarification U345 / C99 :** Supply Assignment porte l’application des affectations d’un plan ; D04 garde ses effets sur les Orders. Trois mécanismes documentés en proposition dans `modeles/backlog/supply-assignment-mechanisms-review.yaml`. Simulation & Analysis explicite les recommandations ; compensation logicielle hors de cette décomposition métier. Aucun nouveau nœud.

**État courant U343 :** les quatre comportements BHV032–BHV035 et le parent D05 sont adoptés, dans la portée des noms et responsabilités présentées. Modalités détaillées, contrats et comparaisons restent proposés. Les mentions U342 ci-dessous décrivent l’état antérieur. [Portée de validation](../2026-09-18-reservation-policy-adoption/README.md).

**État courant U342 :** Reservation Policy Decision (D05.h), nom et définition adoptés. Quatre comportements BHV032–BHV035 documentés et proposés ; parent D05 proposé. Catalogue : 41 capacités et 26 comportements, dont ces quatre nouvelles propositions. [Recensement et frontières](../2026-09-18-reservation-policy/README.md). A01 reste ouvert au-delà de cette décision.

**État courant U334 :** Stocktaking porte politique et demandes de vérification, ainsi que Periodic Physical Inventory (BHV029), Cycle Counting (BHV030) et Spot Counting (BHV031). P08/P09 intégrés ; traitement des écarts commun et réalisation physique par les exécutants. Catalogue : 40 capacités, 22 comportements. Les sections datées conservent leurs états historiques. [Portée de la validation](../2026-09-18-stocktaking-behaviors/README.md).

**État courant U332 :** Inventory Target Decision porte trois comportements frères : Store Inventory Optimization (BHV026), Distribution Center Inventory Optimization (BHV027) et Multi-Echelon Inventory Optimization (BHV028). P13 est intégré ; P12 reste sans création recommandée. Catalogue : 40 capacités et 19 comportements. Les sections datées ci-dessous conservent leurs états historiques. [Portée de la validation](../2026-09-18-inventory-target-behaviors/README.md).

**État courant U318 :** deux comportements intégrés sous Stock Redistribution Decision : rééquilibrage entre sites (BHV024) et consolidation des stocks dispersés (BHV025), dont assortiments de tailles et reliquats. Définitions françaises et rattachements adoptés ; noms anglais éditoriaux. Catalogue : 40 capacités, 16 comportements. [Portée de l’accord](../2026-09-18-redistribution-behaviors/README.md). P01–P03 sur le réassort restent ouverts. Les textes datés ci-dessous conservent leur portée historique.

**Réexamen U324 / C98 :** les min/max peuvent dépendre des besoins et varier par période. Coverage Target Decision détermine les valeurs ; Supply Protection gouverne leur application ; Replenishment Decision détermine les apports. La création des comportements proposés U323 est suspendue faute de bénéfice différenciant établi. [Comparaison CMP111](../../marche/comparaisons.md#cmp111).

Ajouter un comportement ne résout pas une responsabilité absente, deux résultats confondus ou un contrat de données incomplet. Les arbitrages suivants précèdent les décompositions concernées.

## A01 — Reservation / Supply Assignment

Quel effet un lien d’affectation produit-il sur les usages concurrents, et à quel moment existe un engagement opposable ?

**Proposition.** Conserver les deux capacités. Décrire affectation ressource-demande, réservation opposable et granularité physique/logique. Ne pas déduire temporaire de soft.

**Limite.** Les règles et contrats de réservation restent à préciser. U402 adopte P16 sans libération implicite des garanties ; sa création n’est plus conditionnelle à ces règles détaillées.

**Capacités.** D02.c Reservation, D02.e Supply Assignment.

**Marché.** [S02 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), [S03 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities), [S04 — SAP](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4)

## A02 — Cohérence de la décision collective

Qui garantit qu’un ensemble de choix locaux forme un plan réalisable maximisant la valeur multidimensionnelle ?

**Proposition.** Fulfillment Plan Decision D03.o produit le scénario collectif ; Supply Assignment applique le plan retenu. Décisions spécialisées conservées.

**Limite.** Responsabilité adoptée U378 ; détails de dépendances, critères et règles restent à préciser selon les cas, sans bloquer le catalogue.

**Capacités.** D02.e Supply Assignment, D03.j Capable-to-Promise (CTP), D03.k Profitable-to-Promise (PTP), D03.m Order Prioritization, D03.l Delivery Schedule Decision, D03.o Fulfillment Plan Decision.

**Marché.** [S04 — SAP](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4), [S06 — SAP](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe), [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing), [S16 — Blue Yonder](https://blueyonder.com/solutions/order-management-and-commerce/order-promising-and-optimization)

## A03 — Application d’un plan aux Orders

Le plan change-t-il les liens d’affectation, le contenu/structure des Orders, leur état, ou plusieurs de ces objets ?

**Proposition.** Supply Assignment porte application du plan, complément préservant et réaffectation. D04 garde les mutations des Orders ; D06 garde l’exécution.

**Limite.** Principes et rattachements intégrés U345/U364 ; contrats entre capacités et détails éditoriaux ne sont pas validés globalement.

**Capacités.** D04.o Order Lifecycle Management, D04.n Order Structuring, D02.e Supply Assignment, D05.f Inventory Planning.

**Marché.** [S09 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages), [S17 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html)

## A04 — Devenir des retours

Qui décide remise en vente, remplacement, retour fournisseur ou sortie définitive, et sur quelle preuve ?

**Proposition.** D05.i choisit le devenir du bien ; Customer Return porte les parcours de retour ; D04 prend en charge les demandes liées, D06 les prestations et D01 les stocks. Responsabilités commerciales et financières externes à Supply ; aucune capacité manquante ajoutée pour facturer ou encaisser.

**Limite.** Exclusion Supply acquise U429 et clôture U431. Attribution externe Commerce/Finance et détails des interactions restent séparés ; les propositions CMP165/CMP166 ne sont pas validées en bloc. Aucun constat d’exhaustivité des filières.

**Capacités.** D04.l Customer Return, D04.m Supplier Return, D05.c Stock Redistribution Decision, D06.f Process Adaptation Decision, D05.i Return Disposition Decision.

**Marché.** [S23 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns), [S27 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/create-purchase-return-order)

## A05 — Alternatives et admissibilité

Quelles options sont dans la référence ATP, lesquelles nécessitent une adaptation autorisée, et qui fournit les équivalences ?

**Proposition.** Référence ATP et adaptation CTP distinguées U402 ; BHV076 décrit la faisabilité sous adaptation. Les listes d’options, équivalences autorisées et paramètres relèvent des règles à préciser.

**Limite.** La frontière de catalogue est adoptée ; aucune substitution de taille/couleur ni administration des équivalences attribuée implicitement au Product Reference.

**Capacités.** D03.i Available-to-Promise (ATP), D03.j Capable-to-Promise (CTP), D08.d Product Reference Ingestion, D06.e Service Selection Decision.

**Marché.** [S05 — SAP](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5), [S21 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking), [S22 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-statuses)

## A06 — Engagement reçu du fournisseur

La reconfirmation d’un achat et ses effets aval relèvent-ils du contenu Order, de Lifecycle ou d’un processus de négociation ?

**Proposition.** Supplier Confirmation BHV078 porte l’engagement reçu sur Purchase Order, distinct de Promise Management. Fulfillment Optimization examine les impacts et alternatives ; Lifecycle applique les mutations autorisées. Refuser un report ne rétablit pas la capacité fournisseur.

**Limite.** Tolérances, autorités et règles d’acceptation restent à préciser. La négociation générale des accords n’est pas absorbée ; aucune extension automatique à la consignation ou à tous les Orders.

**Capacités.** D04.j Purchase Order, D03.n Promise Management, D05.e Replenishment Decision.

**Marché.** [S26 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-changes-after-confirmation)

## A07 — Disponibilité et capacité opposables

Quels états, unités, horizons et dates d’effet rendent une ressource réellement engageable ?

**Proposition.** Contractualiser donné physique, indisponible, réservé, attendu et capacité engagée avec leurs producteurs.

**Limite.** Ni SLA global = capacité contextuelle, ni nominal moins charge = disponible sans règle établie. Aucun maître externe précis inventé.

**Capacités.** D01.c Inventory Visibility, D06.b Service Capacity Visibility, D14.a Service Catalog Ingestion, D02.c Reservation.

**Marché.** [S02 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), [S21 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking), [S22 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-statuses), [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing)

## Contrats entre capacités à éprouver

Ces contrats ne constituent pas une nouvelle architecture d’intégration. Le catalogue possède déjà des relations ; une flèche ne suffit pas à prouver la sémantique du résultat échangé.

| Consommateur | Fournisseur / contrat attendu | Invariant proposé | Traçabilité |
| --- | --- | --- | --- |
| D03.i | D01.c : Quantités par état, lieu et date avec provenance et fraîcheur. | Les exclusions qui se recouvrent ne sont pas soustraites deux fois. | REL-NEEDS-U290-027 |
| D03.i | D02.c : Engagements opposables et périmètre de leur consommation. | Une réservation logique ne réduit pas physiquement le stock. | REL-NEEDS-U290-029 |
| D03.j | D06.e : Options de service admissibles et conditions. | CTP mobilise le choix de service, sans le redéfinir. | REL-CTP-EXECUTION-SERVICE |
| D03.j | D06.b : Capacité contextuelle disponible avec unité et horizon. | Un SLA configuré ne prouve pas cette disponibilité. | Lien non établi ; à instruire |
| D03.j | D03.n : Confirmations et latitude de révision. | Tester une alternative ne modifie pas les engagements. | Lien non établi ; à instruire |
| D02.e | D03.m : Priorités relatives des demandes. | Priorité ne signifie pas autorisation de dégrader toute confirmation. | REL-NEEDS-U290-026 |
| D02.e | D03.k : Arbitrage économique et hypothèses. | La valeur multidimensionnelle ne se réduit pas à la seule marge. | Lien non établi ; à instruire |
| D05.e | D04.j : Apports attendus, degré de fermeté et changements admissibles. | Une recommandation ne réécrit pas un achat confirmé. | REL-NEEDS-U290-089 |
| D05.c | D05.a : Cibles des lieux donneurs et receveurs. | Couvrir un manque ne crée pas une pénurie cachée au donneur. | Lien non établi ; à instruire |
| D02.b | D05.d : Droits de groupes et limites recommandés. | La décision de valeur et la configuration transactionnelle sont distinctes. | REL-NEEDS-U290-009 |
| D06.f | D07.d : Faits, estimations et absences de retour qualifiées. | Absence de feedback et échec physique ne sont pas synonymes. | REL-NEEDS-U290-113 |
| D06.d | D06.f : Variation retenue, préconditions et effets admissibles. | Coordination et décision d’adaptation restent séparées. | REL-NEEDS-U290-119 |
| D04.o | D04.n : Groupes et liens dont le lancement doit rester cohérent. | La libération ne modifie pas implicitement une structure imposée. | Lien non établi ; à instruire |

## Cas fictifs de validation

Ces exemples servent à discuter le modèle ; ils ne sont pas des faits observés chez GBM, Boardriders ou Sarenza. Sarenza demeure non évalué.

### C01 — Pénurie entre deux commandes

100 disponibles, demande A=80 et B=60 ; B plus prioritaire mais A possède une confirmation protégée.

Résultat attendu : Le classement ne suffit pas à retirer A. Produire options et valeur, vérifier révisabilité et cohérence des engagements.

Éprouve : A01, A02, P16.

### C02 — Réassort sans nouvelle commande client

Position 45, seuil 50, cible 120 ; apports attendus déjà inclus dans la position.

Résultat attendu : Proposition brute 75 ; ne pas compter deux fois les attendus ni assimiler ce besoin au reliquat d’une commande précise.

Éprouve : P02.

### C03 — Traitement d’un excédent

Besoin baissé, achat ferme de 500 pour besoin restant 300 ; fournisseur autorise report mais pas réduction.

Résultat attendu : D05.e étudie le report ; D04 applique seulement le changement admissible, sans effacer l’engagement.

Éprouve : P03, A06.

### C04 — Excédent sans magasin en rupture

Reliquats dispersés, destination centrale sans besoin de vente immédiat.

Résultat attendu : Évaluer intérêt/coût du regroupement, sans imposer un faux manque au lieu receveur.

Éprouve : P07.

### C05 — Commande partiellement préparée

Changement de service alors que la préparation est achevée et que le transport précédent est sollicité.

Résultat attendu : D06.f décide, D06.d coordonne les compensations réalisables ; ne pas annuler fictivement le fait physique.

Éprouve : P04, P05.

### C06 — Silence opérationnel

Feedback attendu à 13 h, absent à 14 h ; état physique inconnu.

Résultat attendu : Signaler un retour manquant, chercher une preuve ; distinguer estimation de retard et retard confirmé.

Éprouve : P10, A07.

### C07 — Stock théorique non utilisable

100 présents dont 20 bloqués, 30 réservés ; recouvrement éventuel des deux populations non établi.

Résultat attendu : Ne pas conclure mécaniquement 50 libres sans règles de dimensions et de non-double-décompte.

Éprouve : A01, A05, A07.

### C08 — Lancement cohérent

Un ensemble de lignes a un engagement de livraison commune, mais une ligne est indisponible.

Résultat attendu : Vérifier le groupe avant lancement ; fractionner nécessite une décision autorisée, pas seulement un clic Split.

Éprouve : P11.

### C09 — Retour remis en vente

Un retour est reçu mais son état et son admissibilité à la revente ne sont pas encore établis.

Résultat attendu : La réception ne décide ni la remise en disponible ni le remboursement ; localiser le propriétaire de la disposition.

Éprouve : A04.

### C10 — Produit alternatif

Produit demandé indisponible ; autre produit techniquement proche en stock.

Résultat attendu : Équivalence autorisée et acceptation utiles avant la proposition ; aucune substitution automatique taille/couleur.

Éprouve : P15, A05.


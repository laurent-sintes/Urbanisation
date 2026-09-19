# Revue des 47 capacités et des 74 comportements

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

Revue exhaustive du catalogue FLOW au périmètre capturé ; profondeur documentaire marché variable et explicitée. Une absence de comportement n’est pas une absence de couverture. Le verdict porte sur la lisibilité du modèle, pas sur la couverture d’un SI installé.

| Capacité | Verdict | Comportements existants | Candidats proposés |
| --- | --- | --- | --- |
| D01.f Inventory Tracking | préciser | — | — |
| D01.g Record Inventory Movements | conserver | — | — |
| D01.c Inventory Visibility | préciser | — | — |
| D01.d Stocktaking | trois comportements intégrés U334 | BHV029, BHV030, BHV031 | P08, P09 |
| D02.b Supply Protection | enrichir l’existant | BHV017, BHV018, BHV019, BHV020 | — |
| D02.c Reservation | contrat préalable | — | — |
| D02.e Supply Assignment | trois mécanismes intégrés U364 | BHV045, BHV046, BHV047 | — |
| D03.i Available-to-Promise (ATP) | enrichir l’existant | BHV001, BHV002, BHV003, BHV004 | — |
| D03.j Capable-to-Promise (CTP) | mécanismes intégrés U402 | BHV075, BHV076, BHV077 | P14, P15, P16 |
| D03.k Profitable-to-Promise (PTP) | préciser | — | — |
| D03.l Delivery Schedule Decision | préciser | — | — |
| D03.m Order Prioritization | préciser | — | — |
| D03.n Promise Management | enrichir l’existant | BHV021, BHV022, BHV023 | — |
| D04.n Order Structuring | rattachements révisés U417 | BHV044 | — |
| D04.o Order Lifecycle Management | six dimensions intégrées U424 | BHV038, BHV036, BHV037, BHV039, BHV040, BHV043 | P11 |
| D05.a Inventory Target Decision | couverture existante confirmée U431 | BHV026, BHV027, BHV028 | P12, P13 |
| D05.d Group Protection Decision | préciser | — | — |
| D05.e Replenishment Decision | trois comportements intégrés U427 | BHV083, BHV084, BHV085 | P01, P02, P03 |
| D05.c Stock Redistribution Decision | deux mécanismes intégrés U318 | BHV024, BHV025 | — |
| D05.f Inventory Planning | enrichir l’existant | BHV005, BHV006, BHV016 | — |
| D06.b Service Capacity Visibility | contrat préalable | — | — |
| D07.a Service Requirements Decision | conserver | — | — |
| D07.b Service Order Management | conserver | — | — |
| D07.c Service Reconciliation | préciser | — | — |
| D07.d Operations Tracking | couverture existante confirmée U431 | BHV079, BHV080, BHV081, BHV082 | P10 |
| D06.d Process Orchestration | couverture existante confirmée U431 | — | P04, P05 |
| D06.e Service Selection Decision | conserver | — | — |
| D06.f Process Adaptation Decision | préciser | — | — |
| D09.d Party / Role Ingestion | contrat de référence | — | — |
| D11.a Agreement Ingestion | contrat de référence | — | — |
| D08.d Product Reference Ingestion | contrat de référence | — | — |
| D12.a Catalog Ingestion | contrat de référence | — | — |
| D13.a Fulfillment Network Ingestion | contrat de référence | — | — |
| D14.a Service Catalog Ingestion | contrat de référence | — | — |
| D05.g Initial Stocking Decision | ne pas décomposer systématiquement | — | — |
| D05.h Reservation Policy Decision | quatre comportements et parent D05 adoptés U343 | BHV032, BHV033, BHV034, BHV035 | — |
| D04.q Order Archiving | capacité séparée U363 | — | — |
| D03.o Fulfillment Plan Decision | conserver | — | — |
| D05.i Return Disposition Decision | stratégies intégrées U383 | BHV048, BHV049 | — |
| D04.i Sales Order | lot intégré U401 | BHV066, BHV067, BHV068, BHV069 | — |
| D04.j Purchase Order | trois parcours et engagement fournisseur intégrés U403 | BHV058, BHV059, BHV060, BHV078 | — |
| D04.k Transfer Order | lot intégré U401 | BHV070, BHV071, BHV072, BHV073, BHV074 | — |
| D04.l Customer Return | parcours intégrés U385 | BHV050, BHV051, BHV052, BHV053, BHV054 | — |
| D04.m Supplier Return | trois parcours intégrés U388 | BHV055, BHV056, BHV057 | — |
| D04.r Consignment Replenishment Order | deux parcours intégrés U398 | BHV061, BHV062 | — |
| D01.h Consigned Inventory Management | lot intégré U401 | BHV063, BHV064, BHV065 | — |
| D03.p Order Backlog Planning | rattachements révisés U417 | — | — |

## D01.f Inventory Tracking

**Diagnostic.** La traçabilité et les faits tardifs sont des exigences d’état ; pas un mécanisme distinct démontré.

**Proposition.** Préciser physique/logique, date d’effet et provenance ; ne pas ajouter Correction comme comportement.

**Appuis.** [S21 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking), [S22 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-statuses)

## D01.g Record Inventory Movements

**Diagnostic.** Enregistrer, corriger et tracer restent les opérations d’une même responsabilité.

**Proposition.** Expliciter mouvement et changement de statut sans déplacement ; aucune décomposition automatique.

**Appuis.** [S22 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-statuses), [S27 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/create-purchase-return-order)

## D01.c Inventory Visibility

**Diagnostic.** Une vue multi-sites ou future existe déjà ; le risque est la qualité des dimensions et de la fraîcheur.

**Proposition.** Contrat de disponibilité opposable : stock présent, bloqué, attendu, engagé et daté ; pas un comportement par site.

**Appuis.** [S02 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), [S21 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking), [S22 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-statuses)

## D01.d Stocktaking

**Diagnostic.** Campagne complète, inventaire tournant et contrôle ponctuel adoptés ; politique et demande de vérification incluses dans le mandat métier.

**Proposition.** Préciser les contrats et règles de traitement des écarts sans ajouter de niveau ni absorber les opérations physiques.

**Appuis.** [S01 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting), [S53 — SAP](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/ae735d9f76024645ad4f5b1a0e6e3387.html), [S54 — Oracle](https://docs.oracle.com/cd/E26401_01/doc.122/e48826/T256582T257763.htm)

## D02.b Supply Protection

**Diagnostic.** Quatre mécanismes couvrent déjà les principales familles ; la configuration de fraîcheur/validité reste à expliquer.

**Proposition.** Préciser protection relative, plafond absolu et durée de validité dans les comportements existants. Aucun ajout CRUD.

**Appuis.** [S08 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification), [S10 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-journal), [S24 — SAP](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-), [S28 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation)

## D02.c Reservation

**Diagnostic.** Le grain et l’effet opposable ne sont pas assez distingués des liens d’affectation.

**Proposition.** Résoudre A01 avant de proposer Soft/Hard/Temporary comme comportements.

**Appuis.** [S02 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), [S03 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities), [S04 — SAP](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4)

## D02.e Supply Assignment

**Diagnostic.** Trois mécanismes combinables apportent des bénéfices distincts : application traçable d’un plan retenu, stabilité en complétant sans remettre en jeu les liens existants, adaptation collective en révisant les liens autorisés. Le choix de préserver ou réviser change les pratiques de préparation et les engagements à coordonner ; il ne se réduit pas à une opération CRUD ou une optimisation technique de calcul. L’application d’un plan peut mobiliser l’une ou l’autre politique.

**Proposition.** Conserver les décisions spécialisées et les protections ; A01/A02 restent ouverts pour les contrats et la cohérence collective.

**Appuis.** [S04 — SAP](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4), [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing), [S16 — Blue Yonder](https://blueyonder.com/solutions/order-management-and-commerce/order-promising-and-optimization), [S67 — SAP](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html), [S65 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand)

## D03.i Available-to-Promise (ATP)

**Diagnostic.** Les quatre comportements couvrent engagements, réseau, temps opérationnel et futur.

**Proposition.** Préciser exclusions, dates de référence et niveaux de confiance. Ne pas ajouter Multi-site ATP ou Future ATP en doublon.

**Appuis.** [S02 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), [S05 — SAP](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5), [S21 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking), [S22 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-statuses)

## D03.j Capable-to-Promise (CTP)

**Diagnostic.** Distinguer trois leviers métier : obtenir davantage de ressources, changer la solution de satisfaction, ou réexaminer des engagements existants. Les conditions, les parties concernées et les conséquences diffèrent réellement. La décomposition rend explicite ce qui doit changer pour rendre une commande satisfaisable, sans confondre faisabilité, choix collectif et application. Plusieurs leviers peuvent se combiner.

**Proposition.** Trois mécanismes combinables de faisabilité ; Fulfillment Plan Decision choisit le scénario collectif. Paramètres et autorisations détaillés ne bloquent pas le catalogue adopté.

**Appuis.** [S05 — SAP](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5), [S06 — SAP](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe), [S07 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp)

## D03.k Profitable-to-Promise (PTP)

**Diagnostic.** Les critères économiques et leur articulation avec les autres dimensions de valeur manquent de contrat.

**Proposition.** Un coût, une marge ou une pénalité sont des critères. Pas de comportement par indicateur ni d’absorption de toute décision dans PTP.

**Appuis.** [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing), [S16 — Blue Yonder](https://blueyonder.com/solutions/order-management-and-commerce/order-promising-and-optimization)

## D03.l Delivery Schedule Decision

**Diagnostic.** L’échelonnement doit respecter les contraintes communes aux lignes.

**Proposition.** Expliquer livraison complète, fractionnement autorisé et synchronisation. Une date ou plusieurs dates ne justifient pas seules un découpage.

**Appuis.** [S18 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/guidelines-for-managing-shipment-sets.html), [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing)

## D03.m Order Prioritization

**Diagnostic.** Priorité métier ne signifie pas autorisation de dégrader une promesse.

**Proposition.** Séparer classement, fermeté et révisabilité. Garder la décision fine ; pas de comportement par segment client.

**Appuis.** [S06 — SAP](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe), [S11 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/priority-based-planning)

## D03.n Promise Management

**Diagnostic.** Les trois comportements sont suffisants ; la révision mérite des politiques plus explicites.

**Proposition.** Enrichir BHV023 avec révisabilité, préservation et effets sur les autres engagements ; aucune copie de stratégies BOP en nouveaux enfants.

**Appuis.** [S06 — SAP](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe)

## D04.n Order Structuring

**Diagnostic.** La scission permet à des parties d’une demande de devenir traitables distinctement tout en préservant filiation, quantités et engagements. Cette complexité et ce bénéfice justifient Order Splitting comme comportement de Structuring. La composition persistante demeure dans la responsabilité large de la capacité, sans comportement créé pour chaque opération de regroupement.

**Proposition.** U420 : Order Archiving appartient à D03 Order Backlog Management ; Order Lifecycle Management appartient à D04 Order Management. Structuring reste dans D03. Les comportements restent sous leurs capacités : Order Release suit Lifecycle dans D04 ; Split reste sous Structuring dans D03. Aucun identifiant ni définition de comportement modifié.

**Appuis.** [S18 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/guidelines-for-managing-shipment-sets.html), [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing)

## D04.o Order Lifecycle Management

**Diagnostic.** Une commande peut être ferme, partiellement libérée, gelée sur certains éléments et suspendue sur une progression, tandis qu’une modification reste en brouillon. Ces effets distincts et leurs contraintes de combinaison justifient six mécanismes métier, sans comportement par état ni cycle linéaire universel. Préparation/révision distingue contenu applicable et proposé ; fin de la demande préserve la différence entre retrait du besoin et clôture.

**Proposition.** Lire les états dans chaque comportement ; détails éditoriaux, sans statut global ni niveau supplémentaire.

**Appuis.** [S63 — SAP](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/413e5cf1373142a784f6c04b2caf3fc0.html), [S64 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming), [S65 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand), [S66 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans), [S04 — SAP](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4), [S18 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/guidelines-for-managing-shipment-sets.html)

## D05.a Inventory Target Decision

**Diagnostic.** Variantes magasin et centre de distribution, coordination multi-échelon adoptées. Risque/service demeure dans la capacité ; P12 ne doit pas dupliquer ce mandat.

**Proposition.** Inventory Target Decision détermine déjà objectifs et seuils selon besoins, service, délais et risques. Ses comportements magasin, centre de distribution et multi-échelon intègrent ces critères ; aucun bénéfice distinct établi pour le candidat. Candidat P12 clos sans ajout.

**Appuis.** [S10 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-journal), [S13 — Kinaxis](https://www.kinaxis.com/en/solutions/applications/probabilistic-meio-wahupa), [S14 — RELEX](https://www.relexsolutions.com/resources/inventory-planning-software/)

## D05.d Group Protection Decision

**Diagnostic.** Quantité protégée minimale et consommation maximale ont des effets différents.

**Proposition.** Décrire deux résultats distincts dans la décision avant de créer deux comportements symétriques de ceux de management.

**Appuis.** [S24 — SAP](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-), [S28 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation)

## D05.e Replenishment Decision

**Diagnostic.** Deux politiques produisent des apports selon des logiques métier distinctes : satisfaire des besoins datés ou rétablir une cible de stock. L’ajustement des apports existants ajoute un mécanisme combinable qui évite de répondre à tout changement par une commande supplémentaire et traite pénuries, excédents ou décalages sous engagements. Cette différence et ce bénéfice justifient les trois comportements ; seuils, périodes et tailles de lot restent des paramètres. Détermination des cibles, décision d’apports, application aux Orders et réalisation restent distinctes.

**Proposition.** Point réassort traité : deux politiques et un mécanisme d’ajustement combinable ; paramètres, cibles et mise en action gardent leurs frontières.

**Appuis.** [S08 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification), [S09 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages), [S11 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/priority-based-planning), [S26 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-changes-after-confirmation), [S51 — SAP](https://help.sap.com/docs/CARAB/00197153997746b4bec2020d00e66ea9/e99798c39a3f4956bd5ce509b39382f7.html?locale=en-US&state=PRODUCTION&version=5.0.2), [S52 — RELEX](https://www.relexsolutions.com/solutions/automatic-replenishment-system/)

## D05.c Stock Redistribution Decision

**Diagnostic.** Rééquilibrage et consolidation intersites adoptés ; cette dernière couvre assortiments de tailles et reliquats.

**Proposition.** Éprouver les critères de bénéfice, coûts, protection du donneur et disponibilité à destination. Ne pas créer un troisième niveau ni réduire la consolidation aux excédents.

**Appuis.** [S12 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html)

## D05.f Inventory Planning

**Diagnostic.** Construction, simulation/analyse et adaptation suffisent ; impacts et critères restent à détailler.

**Proposition.** Conserver trois comportements ; validation, publication, application et modes de simulation ne deviennent pas de nouveaux niveaux.

**Appuis.** [S13 — Kinaxis](https://www.kinaxis.com/en/solutions/applications/probabilistic-meio-wahupa), [S14 — RELEX](https://www.relexsolutions.com/resources/inventory-planning-software/)

## D06.b Service Capacity Visibility

**Diagnostic.** Une capacité nominale ou un SLA configuré ne prouve pas un disponible opérationnel.

**Proposition.** A07 : unités, horizon, fraîcheur, engagements et titulaire de la capacité. Aucun calcul ou booking implicitement ajouté à Visibility.

**Appuis.** [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing)

## D07.a Service Requirements Decision

**Diagnostic.** Exiger emballage, document ou transport sont des variantes de besoin de prestation.

**Proposition.** Illustrer sans créer un comportement par service. Comparaison directe du découpage non établie dans cette passe.

**Appuis.** Comparaison directe non établie ; raisonnement sur le modèle FLOW.

## D07.b Service Order Management

**Diagnostic.** Solliciter, accepter, modifier et annuler sont les opérations du Service Order.

**Proposition.** Décrire idempotence métier, accusé et irréversibilité dans le contrat ; pas quatre comportements CRUD.

**Appuis.** [S17 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html)

## D07.c Service Reconciliation

**Diagnostic.** Un écart de quantité et une absence de preuve peuvent conduire à des suites distinctes, sans imposer deux comportements.

**Proposition.** Rapprocher prévu, accepté, réalisé et preuves ; la décision de suite relève de D06.f. Correspondance marché seulement partielle.

**Appuis.** [S17 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html), [S19 — SAP](https://help.sap.com/docs/SAP_EVENT_MANAGEMENT/1d2d343a67074058a30cd9ffd093ab50/bebccb53ad377114e10000000a174cb4.html)

## D07.d Operations Tracking

**Diagnostic.** Les trois périmètres physiques rendent lisibles les situations et opérations propres à l’entrepôt, au transport et au magasin ; livré ne signifie pas mis en rayon. Le suivi transversal des processus explique les résultats, attentes et blocages métier en reliant Tasks et appels sous-jacents. Ce sont des perspectives combinables aux bénéfices distincts, sans sous-comportements ni découpage par bouton, interface ou fournisseur.

**Proposition.** Operations Tracking et ses quatre comportements rendent visibles progression, écarts, attentes et échecs physiques ou numériques. La détection transverse des exceptions ne justifie pas un doublon. Candidat P10 clos sans ajout.

**Appuis.** [S35 — project44](https://www.project44.com/blog/enhancing-automotive-finished-vehicle-logistics-with-real-time-visibility/), [S42 — Microsoft](https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing), [S43 — Camunda](https://docs.camunda.io/docs/components/audit-log/overview/), [S44 — SAP](https://learning.sap.com/courses/cloud-onboarding-for-sap-ewm-for-sap-s-4hana-cloud-private-edition-extra-stack/learning-about-the-sap-ewm-solution), [S45 — Oracle](https://www.oracle.com/scm/logistics/warehouse-management/), [S48 — Microsoft](https://learn.microsoft.com/en-us/azure/logic-apps/view-workflow-status-run-history), [S49 — Microsoft](https://learn.microsoft.com/en-us/azure/business-process-tracking/overview), [S50 — Camunda](https://camunda.com/platform/observability/)

## D06.d Process Orchestration

**Diagnostic.** La compensation proposée U292 relève de l’adaptabilité du processus ; elle ne justifie pas un comportement Supply autonome.

**Proposition.** La coordination des prestations et de leurs dépendances appartient à la définition de Process Orchestration. Aucun mécanisme distinct justifiant un comportement supplémentaire. Candidat P04 clos sans ajout.

**Appuis.** [S17 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html), [S25 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/add-branches-to-orchestration-processes.html)

## D06.e Service Selection Decision

**Diagnostic.** Admissibilité et choix de service sont déjà réunis à une maille de décision fine.

**Proposition.** Maintenir critères, contraintes et résultat ; pas un comportement par transporteur ni par algorithme.

**Appuis.** [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing)

## D06.f Process Adaptation Decision

**Diagnostic.** Des adaptations de lieu, service et date existent, mais risquent de recopier toutes les décisions mobilisées.

**Proposition.** Décrire limites d’autonomie, point de non-retour et escalade vers D03.n ; pas de nouvelle promesse Supply.

**Appuis.** [S17 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html), [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing)

## D09.d Party / Role Ingestion

**Diagnostic.** Identité et rôles reçus, validité et références aux parties.

**Proposition.** Pas de comportement Ingestion batch/Streaming/Recherche. Documenter contrat de projection et fraîcheur. Aucune comparaison exhaustive des produits MDM dans cette passe.

**Appuis.** Comparaison directe non établie ; raisonnement sur le modèle FLOW.

## D11.a Agreement Ingestion

**Diagnostic.** Conditions d’Agreement et période de validité utilisables ; aucun contrat négocié localement présumé.

**Proposition.** Pas de comportement Ingestion batch/Streaming/Recherche. Documenter contrat de projection et fraîcheur. Aucune comparaison exhaustive des produits MDM dans cette passe.

**Appuis.** Comparaison directe non établie ; raisonnement sur le modèle FLOW.

## D08.d Product Reference Ingestion

**Diagnostic.** Identité produit/variant ; équivalences autorisées à sourcer si substitution retenue.

**Proposition.** Pas de comportement Ingestion batch/Streaming/Recherche. Documenter contrat de projection et fraîcheur. Aucune comparaison exhaustive des produits MDM dans cette passe.

**Appuis.** [S05 — SAP](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5)

## D12.a Catalog Ingestion

**Diagnostic.** Offre et conditions du catalogue reçues ; aucune administration de maître implicite.

**Proposition.** Pas de comportement Ingestion batch/Streaming/Recherche. Documenter contrat de projection et fraîcheur. Aucune comparaison exhaustive des produits MDM dans cette passe.

**Appuis.** Comparaison directe non établie ; raisonnement sur le modèle FLOW.

## D13.a Fulfillment Network Ingestion

**Diagnostic.** Lieux, liens et contraintes du réseau, avec dates d’effet.

**Proposition.** Pas de comportement Ingestion batch/Streaming/Recherche. Documenter contrat de projection et fraîcheur. Aucune comparaison exhaustive des produits MDM dans cette passe.

**Appuis.** Comparaison directe non établie ; raisonnement sur le modèle FLOW.

## D14.a Service Catalog Ingestion

**Diagnostic.** Services sollicitables, retours attendus, SLA configurés et version du contrat de service.

**Proposition.** Pas de comportement Ingestion batch/Streaming/Recherche. Documenter contrat de projection et fraîcheur. Aucune comparaison exhaustive des produits MDM dans cette passe.

**Appuis.** Comparaison directe non établie ; raisonnement sur le modèle FLOW.

## D05.g Initial Stocking Decision

**Diagnostic.** Décision distincte adoptée U316 pour les apports du lancement ; aucun comportement supplémentaire adopté.

**Proposition.** Éprouver le périmètre avec cibles, apports déjà engagés et ressources contraintes avant de proposer des mécanismes différenciants. Ne pas transformer quantités, dates, tailles ou conditionnements en comportements.

**Appuis.** [S51 — SAP](https://help.sap.com/docs/CARAB/00197153997746b4bec2020d00e66ea9/e99798c39a3f4956bd5ce509b39382f7.html?locale=en-US&state=PRODUCTION&version=5.0.2), [S52 — RELEX](https://www.relexsolutions.com/solutions/automatic-replenishment-system/)

## D05.h Reservation Policy Decision

**Diagnostic.** Le jalon du parcours, la proximité du besoin, la différenciation des engagements de service et l’adaptation au risque changent chacun la façon de sécuriser une promesse et le coût d’immobilisation. Quatre mécanismes combinables sont retenus U343 ; durées, seuils, canaux et interfaces restent des paramètres ou des contextes. La complexité visée est l’arbitrage de ces mécanismes sans retirer implicitement les garanties existantes.

**Proposition.** Préciser gouvernance des politiques et contrats détaillés ; conserver les comparaisons avec leurs limites de preuve.

**Appuis.** [S55 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities), [S56 — commercetools](https://docs.commercetools.com/api/inventory-overview), [S57 — IBM](https://www.ibm.com/docs/en/sip?topic=stock-rules-based-safety), [S58 — SAP](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/62d58baf16434bf1a6ad16e55e4cd0f4.html), [S59 — Oracle](https://docs.oracle.com/cd/E26401_01/doc.122/e48842/T373258T377249.htm), [S60 — IBM](https://www.ibm.com/docs/en/order-management?topic=2-handling-inventory-reservation), [S61 — IBM](https://www.ibm.com/docs/en/sip?topic=data-reservations), [S62 — Shopify](https://help.shopify.com/en/manual/checkout-settings)

## D04.q Order Archiving

**Diagnostic.** Permettre la recherche et l’explication d’anciens engagements sans maintenir indéfiniment les commandes dans le traitement courant ; maîtriser ce qui reste consultable.

**Proposition.** U420 : Order Archiving appartient à D03 Order Backlog Management ; Order Lifecycle Management appartient à D04 Order Management. Structuring reste dans D03. Les comportements restent sous leurs capacités : Order Release suit Lifecycle dans D04 ; Split reste sous Structuring dans D03. Aucun identifiant ni définition de comportement modifié.

**Appuis.** Comparaison directe non établie ; raisonnement sur le modèle FLOW.

## D03.o Fulfillment Plan Decision

**Diagnostic.** Décision de cohérence collective adoptée U378 ; aucune décomposition descriptive nécessaire.

**Proposition.** Conserver les décisions spécialisées comme capacités sœurs ; liens de dépendance proposés, pas sous-capacités.

**Appuis.** Comparaison directe non établie ; raisonnement sur le modèle FLOW.

## D05.i Return Disposition Decision

**Diagnostic.** Distinguer les cas dont la disposition est déterminée par une politique connue des cas nécessitant un arbitrage contextuel entre plusieurs devenirs autorisés ; rendre visibles la standardisation des prises en charge et la récupération de valeur, sans imposer une technologie de décision.

**Proposition.** Conserver stratégies de décision et prises en charge distinctes ; mécanismes combinables, pas de comportement par issue.

**Appuis.** [S23 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns)

## D04.i Sales Order

**Diagnostic.** Livraison, retrait, livraison fournisseur et relation intersociétés changent la prise en charge de la commande, la preuve de satisfaction et les engagements à coordonner. Ces parcours doivent se lire dans la capacité.

**Proposition.** Noms, responsabilités présentées et parents adoptés ; décisions, régime de stock et exécution distincts. Compléments éditoriaux et comparaison : consignment-sales-transfer-review.yaml.

**Appuis.** [S18 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/guidelines-for-managing-shipment-sets.html), [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing)

## D04.j Purchase Order

**Diagnostic.** Les parcours changent la nature de l’attendu, la destination, les dépendances entre commandes et les preuves de réalisation : apport en stock, livraison directe au client, prestation. Cette différence métier justifie la décomposition sans recopier le cycle de vie commun. Supplier Confirmation ajoute le mécanisme de construction d’un engagement avec une autre partie, qui peut répondre autrement que demandé : cette différence change le pilotage de l’achat et la fiabilité des ressources attendues. Il se combine avec les trois parcours ; les opérations accepter, refuser et reconfirmer ne sont pas des comportements séparés.

**Proposition.** Supplier Confirmation distingue demande, réponse et engagement accepté, ainsi que risque et promesse client. Consignation reste distincte dans D01.h et D04.r ; aucune extension du comportement par analogie.

**Appuis.** [S26 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-changes-after-confirmation)

## D04.k Transfer Order

**Diagnostic.** Les transferts servent des intentions distinctes : démarrer un stock, l’alimenter, le rééquilibrer, le regrouper ou satisfaire une commande identifiée. L’attendu et la justification doivent rester lisibles même lorsque le transport ou l’outil est commun.

**Proposition.** Noms, responsabilités présentées et parents adoptés ; décisions, régime de stock et exécution distincts. Compléments éditoriaux et comparaison : consignment-sales-transfer-review.yaml.

**Appuis.** [S12 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html)

## D04.l Customer Return

**Diagnostic.** Les parcours diffèrent par le devenir attendu, les responsabilités sollicitées, les immobilisations et les preuves nécessaires pour considérer le retour traité. Cette complexité justifie des comportements métier ; les étapes de saisie, inspection, validation et clôture ne constituent pas chacune un comportement.

**Proposition.** Préserver parcours combinables et frontières décision/exécution/stocks. Remplacement client et règlement sans retour restent des axes distincts à instruire.

**Appuis.** [S23 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns)

## D04.m Supplier Return

**Diagnostic.** Le retour sans remplacement éteint l’attente de marchandises au titre des quantités reprises ; le retour avec remplacement conserve un apport attendu. Cette différence change le suivi des quantités, des dates et des engagements aval. Elle justifie deux parcours métier, indépendamment des motifs du retour et des interfaces. Le retour pour réparation ajoute un attendu distinct : récupérer le même bien remis en état, avec sa traçabilité et son immobilisation, plutôt que recevoir un autre produit.

**Proposition.** Distinguer absence de remplacement, remplacement et restitution du bien réparé ; achat de prestation et exécution restent distincts.

**Appuis.** [S27 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/create-purchase-return-order)

## D04.r Consignment Replenishment Order

**Diagnostic.** Rendre lisibles les deux intentions d’apport : établir le stock de départ à une échéance de lancement, puis entretenir son alimentation pendant l’activité. La différence de finalité et de résultat attendu est utile même si le traitement est commun.

**Proposition.** Implantation et alimentation continue explicites ; décisions mobilisées et fonctions communes documentées. Les nouvelles règles sur les interactions sont consignées pour la suite U399, sans révision des liens existants.

**Appuis.** Comparaison directe non établie ; raisonnement sur le modèle FLOW.

## D01.h Consigned Inventory Management

**Diagnostic.** Les obligations sur le stock diffèrent selon consommation, durée contractuelle ou sortie sans acquisition ; expliciter ce qui change la propriété et ce qui met fin à la détention évite de confondre mouvement et achat.

**Proposition.** Noms, responsabilités présentées et parents adoptés ; décisions, régime de stock et exécution distincts. Compléments éditoriaux et comparaison : consignment-sales-transfer-review.yaml.

**Appuis.** Comparaison directe non établie ; raisonnement sur le modèle FLOW.

## D03.p Order Backlog Planning

**Diagnostic.** Planning sans comportement direct après U417 ; mandat de préparation conservé.

**Proposition.** U420 : Order Archiving appartient à D03 Order Backlog Management ; Order Lifecycle Management appartient à D04 Order Management. Structuring reste dans D03. Les comportements restent sous leurs capacités : Order Release suit Lifecycle dans D04 ; Split reste sous Structuring dans D03. Aucun identifiant ni définition de comportement modifié.

**Appuis.** [S68 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspc/start-backlog-planning.html), [S69 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faubm/key-actions-on-orders.html), [S70 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-orders-simplified)

## Réexamen des comportements existants

Aucun remplacement proposé. Les précisions ci-dessous restent éditoriales et à valider ; elles ne réécrivent pas les accords antérieurs.

| Comportement | Précision utile | Appui |
| --- | --- | --- |
| BHV001 Existing Commitment Consideration | Décrire la non-double-imputation et les engagements effectivement opposables ; ne pas confondre priorité et droit de révision. | [S02 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), [S06 — SAP](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe) |
| BHV002 Network Stock Availability | Conserver tous les lieux admissibles ; préciser états exclus et granularité, sans un comportement par type de lieu. | [S05 — SAP](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5), [S21 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking), [S22 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-statuses) |
| BHV003 Operational Availability Timing | Distinguer disponibilité physique et délai de mobilisation ; capacité nominale et disponibilité contextuelle ne sont pas interchangeables. | [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing) |
| BHV004 Future Supply Projection | Qualifier date, quantité et confiance de la ressource future ; un arrivage prévu ne vaut pas fait reçu. | [S07 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp), [S09 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages) |
| BHV005 Scenario Construction | Construire des alternatives cohérentes avec hypothèses partagées ; ne pas ajouter un comportement par outil de scénario. | [S13 — Kinaxis](https://www.kinaxis.com/en/solutions/applications/probabilistic-meio-wahupa) |
| BHV006 Simulation & Analysis | Associer résultats de simulation, indicateurs, hypothèses et incertitude dans le comportement déjà adopté. | [S13 — Kinaxis](https://www.kinaxis.com/en/solutions/applications/probabilistic-meio-wahupa), [S14 — RELEX](https://www.relexsolutions.com/resources/inventory-planning-software/) |
| BHV016 Scenario Execution Adaptation | Adapter le scénario depuis les résultats de mise en action, sans absorber les mutations d’Orders ou la coordination D06. | [S09 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages), [S17 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html) |
| BHV017 Group Supply Protection | Expliquer les protections entre groupes et selon priorité comme politiques internes combinables, sans étage supplémentaire. | [S24 — SAP](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-), [S28 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation) |
| BHV018 Consumption Capping | Préciser plafond opposable et imputation de consommation ; une priorité élevée ne supprime pas un plafond explicitement applicable. | [S28 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation) |
| BHV019 Safety Stock Policy | Distinguer politique de buffer, cible décidée et éventuelle indisponibilité d’usage ; un safety stock n’est pas universellement un blocage. | [S10 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-journal), [S21 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking) |
| BHV020 Replenishment Regulation | Clarifier seuil de déclenchement, cible, validité et contraintes ; aucune liste de comportements par paramètre. | [S08 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification) |
| BHV021 Promise Proposal | Une proposition de satisfaction n’est pas une confirmation ; conserver hypothèses et durée de validité utile. | [S05 — SAP](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5) |
| BHV022 Promise Confirmation | Rendre explicite ce qui est engagé et les protections de cet engagement ; ne pas copier un état technique éditeur. | [S04 — SAP](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4), [S06 — SAP](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe) |
| BHV023 Promise Revision | Documenter engagements préservés/révisables, améliorations et dégradations autorisées, et effets sur les autres demandes. | [S06 — SAP](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe) |
| BHV024 Inventory Rebalancing | Mécanisme et définition française adoptés U318 ; nom anglais et contrats détaillés proposés. Préserver les besoins du donneur et comparer coûts/risques. | [S12 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html) |
| BHV025 Stock Consolidation | Mécanisme et définition française adoptés U318 ; nom anglais et contrats détaillés proposés. Distinguer les deux cas validés sans sous-comportement ni confusion avec la consolidation interne EWM. | [S12 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html) |
| BHV026 Store Inventory Optimization | U332 : nom, question métier, particularités présentées et parent adoptés ; définition détaillée locale, périmètre et comparaisons éditoriaux. | [S13 — Kinaxis](https://www.kinaxis.com/en/solutions/applications/probabilistic-meio-wahupa) |
| BHV027 Distribution Center Inventory Optimization | U332 : nom, question métier, particularités présentées et parent adoptés ; définition détaillée locale, périmètre et comparaisons éditoriaux. | [S13 — Kinaxis](https://www.kinaxis.com/en/solutions/applications/probabilistic-meio-wahupa) |
| BHV028 Multi-Echelon Inventory Optimization | U331/U332 : nom, définition multi-échelon présentée et parent adoptés ; périmètre détaillé et comparaisons éditoriaux. | [S13 — Kinaxis](https://www.kinaxis.com/en/solutions/applications/probabilistic-meio-wahupa) |
| BHV029 Periodic Physical Inventory | Nom, définition et parent adoptés U334 ; descriptions détaillées et correspondances restent éditoriales. Traitement des écarts commun au parent. | [S53 — SAP](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/ae735d9f76024645ad4f5b1a0e6e3387.html), [S54 — Oracle](https://docs.oracle.com/cd/E26401_01/doc.122/e48826/T256582T257763.htm) |
| BHV030 Cycle Counting | Nom, définition et parent adoptés U334 ; descriptions détaillées et correspondances restent éditoriales. Traitement des écarts commun au parent. | [S01 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting) |
| BHV031 Spot Counting | Nom, définition et parent adoptés U334 ; descriptions détaillées et correspondances restent éditoriales. Traitement des écarts commun au parent. | [S01 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting) |
| BHV032 Milestone-Based Reservation Policy | U343 : nom, responsabilité présentée et parent adoptés ; définitions développées, modalités et correspondances proposées. | [S55 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities), [S56 — commercetools](https://docs.commercetools.com/api/inventory-overview), [S62 — Shopify](https://help.shopify.com/en/manual/checkout-settings) |
| BHV033 Time-Fenced Reservation Policy | U343 : nom, responsabilité présentée et parent adoptés ; définitions développées, modalités et correspondances proposées. | [S59 — Oracle](https://docs.oracle.com/cd/E26401_01/doc.122/e48842/T373258T377249.htm) |
| BHV034 Demand-Differentiated Reservation Policy | U343 : nom, responsabilité présentée et parent adoptés ; définitions développées, modalités et correspondances proposées. | [S55 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities), [S60 — IBM](https://www.ibm.com/docs/en/order-management?topic=2-handling-inventory-reservation) |
| BHV035 Risk-Adaptive Reservation Policy | U343 : nom, responsabilité présentée et parent adoptés ; définitions développées, modalités et correspondances proposées. | [S56 — commercetools](https://docs.commercetools.com/api/inventory-overview), [S57 — IBM](https://www.ibm.com/docs/en/sip?topic=stock-rules-based-safety), [S58 — SAP](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/62d58baf16434bf1a6ad16e55e4cd0f4.html) |
| BHV036 Order Firming | U424 : dimension et états explicites ; mécanismes regroupés avec succession et preuves conservées. Listes détaillées éditoriales. | [S64 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming) |
| BHV037 Order Freezing | U424 : dimension et états explicites ; mécanismes regroupés avec succession et preuves conservées. Listes détaillées éditoriales. | [S63 — SAP](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/413e5cf1373142a784f6c04b2caf3fc0.html), [S65 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand), [S66 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans) |
| BHV038 Order Preparation & Revision | U424 : dimension et états explicites ; mécanismes regroupés avec succession et preuves conservées. Listes détaillées éditoriales. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV039 Order Release | U424 : dimension et états explicites ; mécanismes regroupés avec succession et preuves conservées. Listes détaillées éditoriales. | [S04 — SAP](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4), [S18 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/guidelines-for-managing-shipment-sets.html) |
| BHV040 Order Hold & Resume | U424 : dimension et états explicites ; mécanismes regroupés avec succession et preuves conservées. Listes détaillées éditoriales. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV043 Order Termination | U424 : dimension et états explicites ; mécanismes regroupés avec succession et preuves conservées. Listes détaillées éditoriales. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV044 Order Splitting | U420 : Order Archiving appartient à D03 Order Backlog Management ; Order Lifecycle Management appartient à D04 Order Management. Structuring reste dans D03. Les comportements restent sous leurs capacités : Order Release suit Lifecycle dans D04 ; Split reste sous Structuring dans D03. Aucun identifiant ni définition de comportement modifié. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV045 Supply Assignment Plan Application | Principe et parent acquis ; pas de confusion entre stabilité métier, gel et stratégie de recalcul. Détails et contrats à éprouver. | [S67 — SAP](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html), [S65 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand) |
| BHV046 Incremental Supply Assignment | Principe et parent acquis ; pas de confusion entre stabilité métier, gel et stratégie de recalcul. Détails et contrats à éprouver. | [S67 — SAP](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html), [S65 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand) |
| BHV047 Supply Reassignment | Principe et parent acquis ; pas de confusion entre stabilité métier, gel et stratégie de recalcul. Détails et contrats à éprouver. | [S67 — SAP](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html), [S65 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand) |
| BHV048 Policy-based Disposition | Nom, responsabilité et parent adoptés ; stratégie distincte du traitement physique et des effets commerciaux. | [S23 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns) |
| BHV049 Value Recovery Optimization | Nom, responsabilité et parent adoptés ; stratégie distincte du traitement physique et des effets commerciaux. | [S23 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns) |
| BHV050 Return to Stock | Nom, responsabilité et parent adoptés ; pas de sous-comportement, de décision de disposition dupliquée ni de réalisation physique absorbée. | [S23 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns) |
| BHV051 Repair and Refurbishment | Nom, responsabilité et parent adoptés ; pas de sous-comportement, de décision de disposition dupliquée ni de réalisation physique absorbée. | [S23 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns) |
| BHV052 Return to Supplier | Nom, responsabilité et parent adoptés ; pas de sous-comportement, de décision de disposition dupliquée ni de réalisation physique absorbée. | [S23 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns) |
| BHV053 Return to Customer | Nom, responsabilité et parent adoptés ; pas de sous-comportement, de décision de disposition dupliquée ni de réalisation physique absorbée. | [S23 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns) |
| BHV054 Scrapping | Nom, responsabilité et parent adoptés ; pas de sous-comportement, de décision de disposition dupliquée ni de réalisation physique absorbée. | [S23 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns) |
| BHV055 Return for Credit | Nom, responsabilité et parent adoptés ; correspondances détaillées dans la fiche. Aucun règlement financier ou troisième parcours absorbé. | [S27 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/create-purchase-return-order) |
| BHV056 Return for Replacement | Nom, responsabilité et parent adoptés ; correspondances détaillées dans la fiche. Aucun règlement financier ou troisième parcours absorbé. | [S27 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/create-purchase-return-order) |
| BHV057 Return for Repair | Nom, principe et parent acquis U388 ; rapprochement Oracle EBS et limites dans la fiche via ELM233/CMP144. Contrats détaillés proposés. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV058 Stock Procurement | Nom, responsabilité et parent adoptés U391 ; Microsoft/SAP ELM235/CMP146 dans les fiches ; contrats proposés. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV059 Direct Delivery | Nom, responsabilité et parent adoptés U391 ; Microsoft/SAP ELM235/CMP146 dans les fiches ; contrats proposés. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV060 Service Procurement | Nom, responsabilité et parent adoptés U391 ; Microsoft/SAP ELM235/CMP146 dans les fiches ; contrats proposés. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV061 Initial Stocking | Nom, définition présentée et parent adoptés U398 ; bénéfice de lisibilité métier ; comparaison Microsoft qualifiée dans la fiche. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV062 Continuous Replenishment | Nom, définition présentée et parent adoptés U398 ; bénéfice de lisibilité métier ; comparaison Microsoft qualifiée dans la fiche. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV063 Consumption-Based Ownership Transfer | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV064 Aging-Based Ownership Transfer | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV065 Consignment Exit | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV066 Ship to Customer | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV067 Customer Pickup | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV068 Direct Delivery | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV069 Intercompany Sales | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV070 Initial Stocking | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV071 Continuous Replenishment | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV072 Inventory Rebalancing | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV073 Stock Consolidation | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV074 Order-Driven Transfer | Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée. | Comparaison directe non établie ; raisonnement sur le modèle FLOW. |
| BHV075 Additional Supply Feasibility | Mécanisme CTP adopté ; comparaison datée ELM241/CMP152 dans la fiche. Aucune modification transactionnelle implicite. | [S07 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp) |
| BHV076 Fulfillment Alternative Feasibility | Mécanisme CTP adopté ; comparaison datée ELM241/CMP152 dans la fiche. Aucune modification transactionnelle implicite. | [S05 — SAP](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5) |
| BHV077 Commitment Rebalancing Feasibility | Mécanisme CTP adopté ; comparaison datée ELM241/CMP152 dans la fiche. Aucune modification transactionnelle implicite. | [S06 — SAP](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe) |
| BHV078 Supplier Confirmation | Confirmation et révision reçues du fournisseur sous Purchase Order ; explication détaillée, sources Microsoft/SAP et limites dans la fiche et purchase-order-behaviors.yaml (ELM242/CMP153). | [S26 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-changes-after-confirmation) |
| BHV079 Warehouse Visibility | Nom, périmètre et parent intégrés selon les accords ; compléments éditoriaux et comparaisons ELM243/CMP154 dans la fiche. | [S44 — SAP](https://learning.sap.com/courses/cloud-onboarding-for-sap-ewm-for-sap-s-4hana-cloud-private-edition-extra-stack/learning-about-the-sap-ewm-solution) |
| BHV080 Transportation Visibility | Nom, périmètre et parent intégrés selon les accords ; compléments éditoriaux et comparaisons ELM243/CMP154 dans la fiche. | [S35 — project44](https://www.project44.com/blog/enhancing-automotive-finished-vehicle-logistics-with-real-time-visibility/) |
| BHV081 Store Visibility | Nom, périmètre et parent intégrés selon les accords ; compléments éditoriaux et comparaisons ELM243/CMP154 dans la fiche. | [S46 — Blue Yonder](https://info.blueyonder.com/order-management-commerce/what-is-blue-yonder-store-execution-inventory-management) |
| BHV082 Process Tracking | Nom, périmètre et parent intégrés selon les accords ; compléments éditoriaux et comparaisons ELM243/CMP154 dans la fiche. | [S49 — Microsoft](https://learn.microsoft.com/en-us/azure/business-process-tracking/overview), [S48 — Microsoft](https://learn.microsoft.com/en-us/azure/logic-apps/view-workflow-status-run-history), [S50 — Camunda](https://camunda.com/platform/observability/) |
| BHV083 Requirement-based Replenishment | Nom, définition et parent adoptés. Exemples et comparaisons éditoriaux ; ni calcul des cibles ni mise à jour des Orders absorbés. | [S08 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification) |
| BHV084 Target-based Replenishment | Nom, définition et parent adoptés. Exemples et comparaisons éditoriaux ; ni calcul des cibles ni mise à jour des Orders absorbés. | [S08 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification) |
| BHV085 Replenishment Adjustment | Nom, définition et parent adoptés. Exemples et comparaisons éditoriaux ; ni calcul des cibles ni mise à jour des Orders absorbés. | [S09 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages) |

# Suivi des mécanismes candidats et des intégrations

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

Les fiches conservent les formulations initiales pour traçabilité. Leur statut courant et leur note de réexamen indiquent les intégrations et les propositions restantes ; les identifiants P ne sont pas des BHV. Une intégration ne valide pas par extension les anciens contrats ou dépendances proposés.

**Statuts courants.** implemented_U427 : 3, covered_by_existing_U431 : 3, withdrawn_U293 : 1, implemented_U318 : 2, implemented_U334 : 2, implemented_U410 : 1, implemented_U332 : 1, implemented_U402 : 3.

## P01 — Demand-linked Replenishment

Parent initialement proposé : **D05.e Replenishment Decision**. Priorité initiale : P1. Statut courant : **implemented_U427**. U427 : intégré sous Replenishment Decision avec nom et définition présentés après U426. Les formulations et questions initiales restent historiques ; la clôture sans comportement U425 est remplacée.

**Résultat.** Déterminer les apports nécessaires pour couvrir des besoins datés nets des ressources déjà utilisables.

**Critère : mécanisme.** Distinguer une couverture des besoins identifiés d’une remontée systématique à un niveau cible.

**Cas fictif.** À J+7, 120 unités sont nécessaires ; 70 utilisables et 20 attendues laissent un besoin net de 30, sous contraintes de lot.

**Frontières et non-doublon.** Requirement et regroupement par fenêtre sont des variantes internes ; aucune création d’Order par la décision.

**Appuis marché.** [S08 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification)

**A besoin de.** D01.c Inventory Visibility, D02.c Reservation, D02.e Supply Assignment.

**Arbitrage.** Les besoins identifiés et leur agrégation suffisent-ils comme premier mécanisme, sans comportement séparé par cadence ?

## P02 — Target-restoring Replenishment

Parent initialement proposé : **D05.e Replenishment Decision**. Priorité initiale : P1. Statut courant : **implemented_U427**. U427 : intégré sous Replenishment Decision avec nom et définition présentés après U426. Les formulations et questions initiales restent historiques ; la clôture sans comportement U425 est remplacée.

**Résultat.** Déterminer les apports qui ramènent une position de stock vers la cible selon une règle de déclenchement.

**Critère : politique.** Le motif est le rétablissement d’un niveau voulu ; le besoin n’est pas nécessairement relié à une commande individuelle.

**Cas fictif.** Position projetée 45, seuil 50, cible 120 : proposer 75 avant contraintes ; ne pas ignorer les apports déjà confirmés.

**Frontières et non-doublon.** D05.a détermine les cibles ; D02.b applique leur configuration. Min/max ne signifie pas immobiliser physiquement la différence.

**Appuis marché.** [S08 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification), [S11 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/priority-based-planning)

**A besoin de.** D05.a Inventory Target Decision, D02.b Supply Protection, D01.c Inventory Visibility.

**Arbitrage.** Valider la restauration de cible comme mécanisme distinct, en conservant les formules et paramètres dans la description ?

## P03 — Committed Supply Adjustment

Parent initialement proposé : **D05.e Replenishment Decision**. Priorité initiale : P1. Statut courant : **implemented_U427**. U427 : intégré sous Replenishment Decision avec nom et définition présentés après U426. Les formulations et questions initiales restent historiques ; la clôture sans comportement U425 est remplacée.

**Résultat.** Décider des ajustements d’apports déjà prévus lorsque les besoins ou cibles changent, en respectant les engagements et contraintes de modification.

**Critère : mécanisme.** Éviter de traiter toute optimisation par une commande supplémentaire ; protéger aussi des excédents et des arrivages mal datés.

**Cas fictif.** Un arrivage de 500 est prévu, mais le besoin tombe à 300 : proposer une réduction de 200 ou un report, selon ce que le fournisseur accepte.

**Frontières et non-doublon.** Avancer, reporter, augmenter et réduire sont des opérations de ce mécanisme. D04 applique les changements autorisés ; un accord ferme ne disparaît pas par recalcul.

**Appuis marché.** [S09 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages), [S26 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-changes-after-confirmation)

**A besoin de.** D04.j Purchase Order, D04.k Transfer Order, D04.o Order Lifecycle Management, D05.a Inventory Target Decision.

**Arbitrage.** Le mot Committed doit-il couvrir tout apport planifié avec des degrés de fermeté explicites ? Le périmètre proposé inclut ces degrés.

## P04 — Dependency-driven Execution

Parent initialement proposé : **D06.d Process Orchestration**. Priorité initiale : P1. Statut courant : **covered_by_existing_U431**. U431 : clôture adoptée. La coordination des prestations et de leurs dépendances appartient à la définition de Process Orchestration. Aucun mécanisme distinct justifiant un comportement supplémentaire. La fiche initiale ci-dessous reste historique.

**Résultat.** Coordonner les prestations selon leurs prérequis et conditions de progression, à partir de résultats et engagements connus.

**Critère : mécanisme.** Faire apparaître les dépendances métier au-delà d’une simple émission de Service Orders.

**Cas fictif.** La remise au transport dépend de la préparation et des documents requis ; un retour documentaire reçu ne vaut pas préparation physique achevée.

**Frontières et non-doublon.** Les tâches internes de l’entrepôt restent chez l’exécutant. Conditions de synchronisation proposées par FLOW, pas norme Oracle recopiée.

**Appuis marché.** [S17 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html), [S25 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/add-branches-to-orchestration-processes.html)

**A besoin de.** D07.a Service Requirements Decision, D07.b Service Order Management, D07.d Operations Tracking.

**Arbitrage.** Valider la coordination des prérequis de prestations comme comportement d’orchestration ?

## P05 — Execution Compensation

Parent initialement proposé : **D06.d Process Orchestration**. Priorité initiale : P1. Statut courant : **withdrawn_U293**. Retiré comme comportement métier autonome ; mécanisme d’adaptabilité du processus/Case. Voir feedback U293.

**Résultat.** Coordonner les effets correctifs rendus nécessaires par un plan d’exécution modifié, en tenant compte des prestations déjà demandées ou réalisées.

**Critère : mécanisme.** Une adaptation en cours d’exécution doit traiter les effets du plan précédent, pas seulement émettre un nouveau plan.

**Cas fictif.** Après changement de transporteur, retirer la sollicitation précédente et obtenir un nouveau document ; si le colis est déjà parti, traiter cette réalité au lieu de rejouer une annulation.

**Frontières et non-doublon.** D06.f choisit la variation ; D06.d la coordonne ; D07.b porte les demandes. Aucun rollback physique ni transaction atomique globale promis.

**Appuis marché.** [S17 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html)

**A besoin de.** D06.f Process Adaptation Decision, D07.b Service Order Management, D07.c Service Reconciliation, D07.d Operations Tracking.

**Arbitrage.** Valider le mécanisme, puis définir les irréversibilités et effets compensables service par service ?

## P06 — Shortage-driven Rebalancing

Parent initialement proposé : **D05.c Stock Redistribution Decision**. Priorité initiale : P1. Statut courant : **implemented_U318**. U318 : mécanisme adopté dans la portée U317 et intégré ; définition initiale ci-dessus conservée comme historique. Lire le comportement courant et sa qualification champ par champ.

**Résultat.** Décider des transferts de ressources existantes qui couvrent des manques en préservant la situation des lieux donneurs.

**Critère : mécanisme.** Rendre explicite l’arbitrage donneur-receveur, distinct d’un réapprovisionnement externe.

**Cas fictif.** A dispose de 100 mais doit en garder 70 ; B manque de 40. Un transfert de 30 laisse un manque de 10 à traiter autrement.

**Frontières et non-doublon.** Le déplacement commun ne fusionne pas les finalités D03 et D05 ; D04.k puis D06 portent la mise en action.

**Appuis marché.** [S12 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html)

**A besoin de.** D05.a Inventory Target Decision, D01.c Inventory Visibility, D02.b Supply Protection, D06.b Service Capacity Visibility.

**Arbitrage.** Le respect du stock utile au donneur est-il le bon invariant à rendre visible ?

## P07 — Excess Consolidation

Parent initialement proposé : **D05.c Stock Redistribution Decision**. Priorité initiale : P1. Statut courant : **implemented_U318**. U318 : mécanisme adopté dans la portée U317 et intégré ; définition initiale ci-dessus conservée comme historique. Lire le comportement courant et sa qualification champ par champ.

**Résultat.** Décider du regroupement de stocks excédentaires dans des lieux adaptés, même sans manque immédiat dans le lieu de destination.

**Critère : bénéfice ciblé.** Adresser les excédents dispersé et les possibilités futures de réutilisation, au-delà de la réponse à une pénurie présente.

**Cas fictif.** Des magasins détiennent des reliquats dispersés ; les regrouper dans un lieu de redistribution permet de libérer de la place et de préparer un futur usage.

**Frontières et non-doublon.** Ni liquidation commerciale, ni destruction, ni remise de prix introduites. Le coût et la valeur du regroupement doivent être éprouvés.

**Appuis marché.** [S12 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html)

**A besoin de.** D05.a Inventory Target Decision, D01.c Inventory Visibility, D13.a Fulfillment Network Ingestion, D06.b Service Capacity Visibility.

**Arbitrage.** Cette collecte d’excédents est-elle un mécanisme utile au périmètre FLOW, distinct d’un transfert pour manque ?

## P08 — Recurring Stock Verification

Parent initialement proposé : **D01.d Stocktaking**. Priorité initiale : P2. Statut courant : **implemented_U334**. U334 : intégré selon la proposition U333, avec traitement des écarts commun au parent. Le seuil Microsoft ne se confond pas avec un signal d’anomalie. Ancienne formulation conservée pour provenance.

**Résultat.** Fiabiliser le stock par une vérification organisée et récurrente des quantités sur un périmètre défini.

**Critère : politique.** La récurrence assure une couverture de contrôle indépendamment des incidents visibles.

**Cas fictif.** Vérifier régulièrement les articles à enjeu, rapprocher les quantités constatées et instruire les écarts.

**Frontières et non-doublon.** Programme et mandat à préciser ; FLOW ne récupère pas automatiquement le comptage physique du WMS.

**Appuis marché.** [S01 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting)

**A besoin de.** D01.c Inventory Visibility, D01.f Inventory Tracking, D01.g Record Inventory Movements.

**Arbitrage.** FLOW porte-t-il la politique de fiabilisation ou seulement le traitement des constats fournis par l’exécutant ?

## P09 — Triggered Stock Verification

Parent initialement proposé : **D01.d Stocktaking**. Priorité initiale : P2. Statut courant : **implemented_U334**. U334 : intégré selon la proposition U333, avec traitement des écarts commun au parent. Le seuil Microsoft ne se confond pas avec un signal d’anomalie. Ancienne formulation conservée pour provenance.

**Résultat.** Fiabiliser une quantité lorsque des signaux rendent sa crédibilité insuffisante pour les usages métier.

**Critère : mécanisme.** Concentrer un contrôle sur une situation à risque et non seulement sur un calendrier.

**Cas fictif.** Un picking échoue alors que le stock est annoncé disponible : solliciter un constat, puis traiter l’écart établi.

**Frontières et non-doublon.** Microsoft documente le seuil ; l’échec de picking est notre cas proposé. Détecter le signal ne donne pas autorité de correction automatique.

**Appuis marché.** [S01 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting), [S21 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking)

**A besoin de.** D07.d Operations Tracking, D01.c Inventory Visibility, D01.g Record Inventory Movements.

**Arbitrage.** Quels signaux autorisent une demande de vérification et qui peut faire corriger la quantité ?

## P10 — Execution Exception Detection

Parent initialement proposé : **D07.d Operations Tracking**. Priorité initiale : P2. Statut courant : **covered_by_existing_U431**. U431 : clôture adoptée. Operations Tracking et ses quatre comportements rendent visibles progression, écarts, attentes et échecs physiques ou numériques. La détection transverse des exceptions ne justifie pas un doublon. La fiche initiale ci-dessous reste historique.

**Résultat.** Identifier les écarts de progression et l’absence de retours attendus afin d’alimenter la réaction opérationnelle.

**Critère : bénéfice ciblé.** Un tracking qui enregistre uniquement les événements reçus ne révèle pas les silences qui mettent le plan en risque.

**Cas fictif.** À 14 h, aucun retour de préparation attendu à 13 h : signaler un manque d’information ; confirmer le retard physique séparément.

**Frontières et non-doublon.** Pas de nouvelle promesse ni de décision d’adaptation. Le catalogue de services doit préciser retours attendus et tolérances. U293 : ce comportement ne résume pas Execution Tracking ; la visibilité normale du transit reste essentielle.

**Appuis marché.** [S19 — SAP](https://help.sap.com/docs/SAP_EVENT_MANAGEMENT/1d2d343a67074058a30cd9ffd093ab50/bebccb53ad377114e10000000a174cb4.html), [S20 — Oracle](https://docs.oracle.com/en/cloud/saas/readiness/scm/26b/order26b/26B-order-mgmt-wn-t72535.htm)

**A besoin de.** D07.b Service Order Management, D14.a Service Catalog Ingestion, D06.b Service Capacity Visibility.

**Arbitrage.** Valider la détection ; préciser ensuite les signaux probants, estimés et absents ? Source SAP historique, validation métier particulièrement importante.

## P11 — Coordinated Order Release

Parent initialement proposé : **D04.o Order Lifecycle Management**. Priorité initiale : P2. Statut courant : **implemented_U410**. P11 intégré BHV039 U410. Release reste sous Lifecycle, déplacé en D04 U420 ; définition et parent de comportement conservés.

**Résultat.** Autoriser la progression d’Orders ou de lignes liés en respectant une condition de cohérence commune.

**Critère : politique.** Des lignes correctement affectées une à une peuvent rester collectivement impropres à être lancées.

**Cas fictif.** Un lot destiné à une ouverture magasin doit atteindre la complétude convenue avant lancement, malgré la disponibilité de certaines lignes.

**Frontières et non-doublon.** La condition de groupe est le mécanisme ; Hold/Release restent des opérations. D03.l décide l’échéancier, D04.n porte la structure, D06 orchestre après lancement.

**Appuis marché.** [S04 — SAP](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4), [S18 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/guidelines-for-managing-shipment-sets.html)

**A besoin de.** D02.e Supply Assignment, D03.l Delivery Schedule Decision, D04.n Order Structuring.

**Arbitrage.** Le lancement coordonné de groupes existe-t-il dans le périmètre FLOW et avec quelle règle métier de complétude ?

## P12 — Service-risk Coverage Targeting

Parent initialement proposé : **D05.a Inventory Target Decision**. Priorité initiale : conditionnel. Statut courant : **covered_by_existing_U431**. U431 : clôture adoptée. Inventory Target Decision détermine déjà objectifs et seuils selon besoins, service, délais et risques. Ses comportements magasin, centre de distribution et multi-échelon intègrent ces critères ; aucun bénéfice distinct établi pour le candidat. La fiche initiale ci-dessous reste historique.

**Résultat.** Déterminer des cibles de couverture différenciées selon l’incertitude et le niveau de service attendu.

**Critère : politique.** Utile si les décisions de cible doivent expliciter un arbitrage de risque distinct d’une simple norme de couverture.

**Cas fictif.** Deux articles à même demande moyenne reçoivent des cibles différentes parce que leurs délais et aléas diffèrent.

**Frontières et non-doublon.** Déjà proche du mandat de D05.a : enrichir d’abord la définition ; ne créer le comportement que si la distinction apporte un usage concret.

**Appuis marché.** [S10 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-journal), [S13 — Kinaxis](https://www.kinaxis.com/en/solutions/applications/probabilistic-meio-wahupa), [S14 — RELEX](https://www.relexsolutions.com/resources/inventory-planning-software/)

**A besoin de.** D01.c Inventory Visibility, D08.d Product Reference Ingestion, D13.a Fulfillment Network Ingestion.

**Arbitrage.** Ce mécanisme apporte-t-il assez par rapport à la définition actuelle pour justifier un nœud ?

## P13 — Network-coordinated Coverage Targeting

Parent initialement proposé : **D05.a Inventory Target Decision**. Priorité initiale : conditionnel. Statut courant : **implemented_U332**. U331/U332 : intégré sous le nom Multi-Echelon Inventory Optimization, avec les variantes locales BHV026/BHV027. Formulation initiale conservée pour provenance.

**Résultat.** Déterminer conjointement les cibles de plusieurs lieux ou échelons en tenant compte de leurs dépendances.

**Critère : mécanisme.** Éviter de cumuler partout des buffers optimisés indépendamment et de surprotéger le réseau.

**Cas fictif.** Comparer un buffer central et des buffers magasins en tenant compte des délais de transfert et du service réellement attendu.

**Frontières et non-doublon.** Décider des cibles n’est pas exécuter des transferts ; le marché consulté apporte un principe produit, pas un algorithme vérifié.

**Appuis marché.** [S13 — Kinaxis](https://www.kinaxis.com/en/solutions/applications/probabilistic-meio-wahupa)

**A besoin de.** D13.a Fulfillment Network Ingestion, D01.c Inventory Visibility, D06.b Service Capacity Visibility.

**Arbitrage.** Le couplage des cibles réseau est-il une ambition FLOW suffisamment explicite ?

## P14 — Additional Supply Feasibility

Parent initialement proposé : **D03.j Capable-to-Promise (CTP)**. Priorité initiale : conditionnel. Statut courant : **implemented_U402**. U402 : nom, responsabilité présentée et parent CTP adoptés ; formulation initiale conservée pour provenance. Frontière avec Fulfillment Plan Decision explicitée dans d03-review.yaml.

**Résultat.** Établir si des ressources supplémentaires peuvent rendre une demande satisfaisable dans les contraintes retenues.

**Critère : mécanisme.** Faire apparaître l’origine de la faisabilité sous adaptation, sans faire de CTP une seconde optimisation du stock.

**Cas fictif.** Une commande ne peut être couverte par les ressources admissibles ; une fourniture additionnelle pourrait la rendre réalisable à J+10.

**Frontières et non-doublon.** D05.e intervient pour l’objectif de stock, pas obligatoirement pour tout achat à la demande. La capacité qui fournit l’option achat ponctuel reste à contractualiser.

**Appuis marché.** [S07 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp)

**A besoin de.** D14.a Service Catalog Ingestion, D06.b Service Capacity Visibility, D06.e Service Selection Decision.

**Arbitrage.** Quelles adaptations de ressources sont effectivement dans CTP FLOW et qui sait en établir la faisabilité ?

## P15 — Fulfillment Alternative Feasibility

Parent initialement proposé : **D03.j Capable-to-Promise (CTP)**. Priorité initiale : conditionnel. Statut courant : **implemented_U402**. U402 : nom, responsabilité présentée et parent CTP adoptés ; formulation initiale conservée pour provenance. Frontière avec Fulfillment Plan Decision explicitée dans d03-review.yaml.

**Résultat.** Établir la faisabilité d’une satisfaction qui nécessite de modifier les modalités admissibles de fulfillment.

**Critère : variante.** Distinguer une adaptation autorisée de la simple lecture des alternatives déjà admissibles par ATP.

**Cas fictif.** Une autre prestation rend la date possible ; elle doit être autorisée et réalisable avant d’être proposée.

**Frontières et non-doublon.** Tous les lieux déjà admissibles restent dans ATP. Une substitution de produit nécessite un contrat d’équivalence ; D06.e garde la décision de service.

**Appuis marché.** [S05 — SAP](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5), [S15 — Manhattan](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing)

**A besoin de.** D03.i Available-to-Promise (ATP), D06.e Service Selection Decision, D06.b Service Capacity Visibility, D08.d Product Reference Ingestion.

**Arbitrage.** Quelle modification marque le passage de la référence ATP à une adaptation CTP ?

## P16 — Commitment Rebalancing Feasibility

Parent initialement proposé : **D03.j Capable-to-Promise (CTP)**. Priorité initiale : conditionnel. Statut courant : **implemented_U402**. U402 : nom, responsabilité présentée et parent CTP adoptés ; formulation initiale conservée pour provenance. Frontière avec Fulfillment Plan Decision explicitée dans d03-review.yaml.

**Résultat.** Établir les possibilités de satisfaction obtenues par une redistribution autorisée d’engagements existants.

**Critère : mécanisme.** Rendre visibles les gagnants, perdants et engagements protégés avant une révision de promesse.

**Cas fictif.** Étudier si une demande prioritaire peut être satisfaite en décalant une demande révisable, sans toucher une confirmation protégée.

**Frontières et non-doublon.** BOP est un appui partiel. D03.m fixe les priorités, D03.n révise les promesses et D02.e applique les affectations ; un scénario candidat ne les modifie pas.

**Appuis marché.** [S06 — SAP](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe), [S04 — SAP](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4)

**A besoin de.** D03.m Order Prioritization, D03.k Profitable-to-Promise (PTP), D03.n Promise Management, D02.c Reservation, D02.e Supply Assignment.

**Arbitrage.** CTP doit-il établir cette faisabilité collective, et avec quel contrat pour les effets croisés ?


# Couverture métier face au marché — U775

**Application U777 — 26 septembre 2026 :** lot corrigé validé et appliqué dans le backlog. Transport Plan Decision et ses deux comportements, Scrapping Order, traçabilité répartie entre Tracking/Ledger/Visibility et Inventory Disposition Decision (D05.i, deux stratégies conservées). Trois scénarios concrets ajoutés avec contributions explicites des capacités ; scénarios de retour et de correspondance transport enrichis. Glossaire aligné. GAP-01 à GAP-05 sont traités selon ces arbitrages ; GAP-06 à GAP-08 restent à arbitrer. Aucune release déclenchée. Les paragraphes antérieurs ci-dessous conservent l’histoire de la proposition et ne décrivent pas tous la cible retenue.

**Point d’arbitrage U776, 26 septembre 2026 :** Transport Plan Decision et Scrapping Order sont acceptés, avec application canonique en attente. Inventory Traceability et Inventory Usage Decision sont en réexamen. Les développements ci-dessous restituent la proposition initiale U775 ; ils ne valent pas approbation globale. La réponse proposée privilégie une traçabilité répartie entre Tracking, Ledger et Visibility, et examine le regroupement de la décision d’usage avec la disposition élargie. Ces deux révisions restent à discuter.

Le modèle couvre déjà une grande partie des responsabilités attendues. La recherche fait ressortir **quatre capacités candidates**, **une extension**, **une décomposition de comportements** et **une clarification de référentiel**. Une famille de comptage confié reste conditionnelle.

Ce sont des propositions : le catalogue canonique conserve ses 72 capacités et 75 comportements. Les neuf sous-domaines ont été balayés à partir du modèle et des sources Dynamics / S/4HANA ; les écarts ont fait l’objet de lectures ciblées. Ce balayage ne prétend pas certifier l’exhaustivité du marché.

## GAP-01 — Inventory Usage Decision

Les faits et statuts sont tenus ; Inspection Order fournit un constat et Return Disposition Decision ne traite que les retours. La décision de restreindre ou réautoriser l’usage d’un stock hors retour n’a pas de responsabilité explicite.

**Proposition.** Ajouter Inventory Usage Decision dans Inventory Management, type decision, catégorie Inventory Foundation : déterminer les usages autorisés ou interdits, quantités, portée et conditions de levée à partir des constats et autorisations applicables. Zéro comportement initial ; bloquer puis libérer constitue un cycle, pas deux variantes artificielles.

**Frontière.** La décision peut être prise par un responsable qualité externe : le modèle métier reste indépendant de son implantation. Inventory Tracking capte les faits ; le Ledger tient l’état reconnu. Ni réservation pour une demande, ni affectation Matching, ni inspection physique. Clarifier U436 : l’exclusivité de réservation concerne les usages concurrents, pas toute interdiction qualité ou réglementaire.

**Cas fictif.** Des boutons présentent un défaut sur 500 vestes déjà reçues : interdire leur usage, faire contrôler le lot, puis libérer uniquement les quantités autorisées sans modifier leur présence physique.

**Appuis marché :** [Microsoft Dynamics 365 — Inventory blocking](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking), [SAP S/4HANA — Performing Internal Inspections in the Warehouse](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-warehouse-management/performing-internal-inspections-in-the-warehouse_a8dd0fcf-85c3-47d5-9da2-0058a81ebed5). Les différences et limites sont consignées dans l’annexe.

## GAP-02 — Inventory Traceability

Les positions, mouvements et progressions existent. Reconstituer la chaîne des origines, transformations et destinations pour identifier les biens et demandes touchés n’est pas explicite ; un journal seul ne produit pas cette réponse.

**Proposition.** Ajouter Inventory Traceability dans Inventory Management, type knowledge, catégorie Inventory Visibility. Produire une connaissance de provenance et de propagation à partir des faits tracés, sans nouvelle source de vérité concurrente.

**Frontière.** Tracking reste de type integration. Les identifiants de lots/unités, liens de transformation et limites de couverture sont indispensables ; ne pas inventer une généalogie à partir d’un solde. Les données de production peuvent venir d’un exécutant externe ; la production n’entre pas dans le domaine.

**Cas fictif.** Retrouver les kits contenant un accessoire défectueux, les magasins livrés et les commandes encore ouvertes, puis remonter au lot fournisseur.

**Comportements proposés :**

- **Backward Traceability** : Reconstituer les origines et transformations ayant contribué aux biens concernés, avec preuves et lacunes.
- **Forward Traceability** : Identifier les biens dérivés, destinations, livraisons et demandes exposées à partir d’une origine identifiée.

**Appuis marché :** [Microsoft Dynamics 365 — Item and raw material tracing in inventory, production, and sales](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/trace-items-raw-materials-inventory-production-sales), [SAP S/4HANA — Batch Management & Traceability in SAP S/4HANA Cloud](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-manufacturing-execution/batch-management-traceability-in-sap-s-4hana-cloud_d396525c-87eb-4af9-a718-041af5cba51c). Les différences et limites sont consignées dans l’annexe.

## GAP-03 — Transport Plan Decision

Le modèle conserve la demande de trajet, sélectionne les prestataires et libère des lots d’ordres. Le choix d’un ensemble cohérent de chargements, arrêts et acheminements est seulement renvoyé à la coordination, sans capacité explicite.

**Proposition.** Ajouter Transport Plan Decision dans Fulfilment Orchestration, type decision, catégorie Définir et choisir les prestations : déterminer le plan de transport demandé, ses regroupements et acheminements compatibles. Le nom est une adaptation FLOW des fonctions Transportation/Load Planning.

**Frontière.** Préserver promesses et affectations Matching. Service Selection Decision garde le choix de services/exécutants ; Release Decision garde le moment de sollicitation. Les Transport Orders portent le plan confié. Placement 3D, conduite et tournées internes non commandées restent chez le prestataire. Ne pas créer un second master plan de matching.

**Cas fictif.** Six magasins doivent recevoir vendredi : regrouper les expéditions en deux chargements compatibles et déterminer les arrêts, plutôt que seulement envoyer six ordres au même moment.

**Comportements proposés :**

- **Load Consolidation** : Constituer des chargements compatibles selon marchandises, capacités, destinations et échéances.
- **Routing & Scheduling** : Déterminer les étapes, arrêts et échéances du plan confié selon les trajets et contraintes admissibles.

**Appuis marché :** [Microsoft Dynamics 365 — Load building workbench](https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/tasks/load-building-workbench), [SAP S/4HANA — Planning Loads](https://learning.sap.com/courses/business-processes-in-sap-s-4hana-transportation-management/planning-loads_e752a3f5-f4a9-4957-9f4d-e6e550c15409), [Microsoft Dynamics 365 — Plan freight transportation routes with multiple stops](https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/plan-freight-transportation-routes-multiple-stops). Les différences et limites sont consignées dans l’annexe.

## GAP-04 — Scrapping Order

Scrapping est un comportement de Return Order qui conserve la suite du retour. Il ne constitue pas la demande de mise au rebut confiée à un exécutant, notamment pour un stock détérioré sans retour.

**Proposition.** Ajouter Scrapping Order dans Service Order Management, type action, catégorie Prestations d’entrepôt : tenir la prestation autorisée de mise au rebut, les quantités, consignes, justificatifs et reliquats. Zéro comportement initial.

**Frontière.** La décision d’orientation reste distincte. Une écriture comptable ou une sortie de stock ne prouve pas la réalisation physique. Le nom de famille est un choix FLOW, non un ordre natif commun aux deux éditeurs. Ne pas étendre automatiquement aux dons, ventes de déstockage ou à toutes les filières de recyclage.

**Cas fictif.** Des articles abîmés sur site sont orientés vers une filière autorisée ; confier le traitement et attendre la preuve portant sur les quantités effectivement traitées.

**Appuis marché :** [Microsoft Dynamics 365 — Quarantine orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quarantine-orders), [SAP S/4HANA — Carrying out Warehouse Ad Hoc Goods Issue](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-warehouse-management/carrying-out-warehouse-ad-hoc-goods-issue_e15b00c8-2b28-4341-9cdc-7da58ded5b89). Les différences et limites sont consignées dans l’annexe.

## GAP-05 — Étendre Return Disposition Decision

Le choix du devenir logistique est limité aux produits retournés. Un stock endommagé pendant le stockage ou refusé au contrôle peut nécessiter les mêmes arbitrages sans Return Order.

**Proposition.** Généraliser D05.i en Inventory Disposition Decision, dans Fulfilment Orchestration, en conservant son identité et ses deux stratégies Policy-based Disposition et Value Recovery Optimization. Ne pas ajouter une seconde capacité presque identique.

**Frontière.** GAP-01 décide les droits d’usage ; cette décision choisit réparation, reconditionnement, retour fournisseur ou sortie définitive autorisée. Matching conserve les déplacements et affectations ; Commerce et Finance conservent leurs décisions. Marché : blocage et orientation sont parfois combinés, leur séparation est un choix de responsabilité FLOW.

**Cas fictif.** Un dégât des eaux touche des manteaux en réserve : comparer nettoyage, réparation et sortie autorisée, même sans retour client.

**Appuis marché :** [Microsoft Dynamics 365 — Inventory blocking](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking), [SAP S/4HANA — Performing Internal Inspections in the Warehouse](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-warehouse-management/performing-internal-inspections-in-the-warehouse_a8dd0fcf-85c3-47d5-9da2-0058a81ebed5), [Microsoft Dynamics 365 — Quarantine orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quarantine-orders), [SAP S/4HANA — Carrying out Warehouse Ad Hoc Goods Issue](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-warehouse-management/carrying-out-warehouse-ad-hoc-goods-issue_e15b00c8-2b28-4341-9cdc-7da58ded5b89). Les différences et limites sont consignées dans l’annexe.

## GAP-06 — Deux variantes de prestation d’inspection

Inspection Order décrit le résultat attendu de façon générique. Il ne distingue pas preuve individuelle et conclusion portant sur un lot à partir d’un échantillon.

**Proposition.** Ajouter deux comportements si cette distinction contractuelle est retenue : Unit-by-Unit Inspection et Sampling-Based Inspection. Décrire obligations, portée du résultat et conditions de clôture, plutôt que les techniques de prélèvement.

**Frontière.** Un taux, une quantité fixe, un écran ou une méthode de test restent des paramètres. L’intérêt de la décomposition est la nature de la preuve attendue ; sinon conserver ces précisions dans le protocole de l’Order. La conclusion d’inspection ne remplace pas la décision d’usage ou de disposition.

**Cas fictif.** Contrôler individuellement 50 vestes réparées exige un résultat pour chacune ; apprécier un lot neuf de 2 000 pièces par échantillon exige le protocole, l’échantillon et la portée de la conclusion.

**Comportements proposés :**

- **Unit-by-Unit Inspection** : Tenir la demande d’un contrôle de chaque unité du périmètre convenu et rapprocher les résultats individuels attendus.
- **Sampling-Based Inspection** : Tenir la demande d’une appréciation de lot à partir d’un échantillon convenu, avec protocole, preuves et limites de représentativité.

**Appuis marché :** [SAP S/4HANA — Setting up Sample Determination](https://learning.sap.com/courses/implementing-sap-s-4hana-quality-management/setting-up-sample-determination_c29dda80-ff64-443e-bead-dc36904a7463), [Microsoft Dynamics 365 — Acceptance sampling](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-acceptance-sampling), [Microsoft Dynamics 365 — Quality management item sampling](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-item-sampling). Les différences et limites sont consignées dans l’annexe.

## GAP-07 — Alternatives autorisées : expliciter leur provenance

Les substitutions autorisées sont supposées par CTP, PTP, Matching et un scénario, mais leur provenance, validité et conditions de consommation ne sont pas clairement attribuées au référentiel local.

**Proposition.** Expliciter dans Product Reference et son ingestion/Visibility les relations d’alternative reçues, leur sens, validité et autorité. Les conditions commerciales restent auprès de leur source ; aucune capacité de substitution supplémentaire proposée.

**Frontière.** La similarité produit n’autorise pas une substitution. Les commandes préservent le demandé et l’accepté ; ATP/CTP évaluent les options, Promise Selection choisit une proposition. Source SAP lue surtout sur alternatives de site : correspondance partielle, pas preuve complète d’équivalences produit.

**Cas fictif.** Une référence remplacée par sa nouvelle version est autorisée pour une période ; une couleur seulement ressemblante ne devient pas substituable sans accord.

**Appuis marché :** [Microsoft Dynamics 365 — Manual order orchestration in Intelligent Order Management | Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/manual-order-orchestration), [SAP S/4HANA — Outlining Alternative-based Confirmation](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-alternative-based-confirmation). Les différences et limites sont consignées dans l’annexe.

## GAP-08 — Stocktaking Order : famille conditionnelle

Stocktaking couvre déjà la politique, la demande de contrôle et le rapprochement. Il n’existe pas de famille distincte pour le comptage confié avec un engagement de prestation autonome.

**Proposition.** Ne pas créer par défaut. Si FLOW commande et suit le comptage comme prestation distincte, envisager Stocktaking Order dans Service Order Management ; Stocktaking conserverait politique, rapprochement et corrections.

**Frontière.** Les work/document éditeurs prouvent des travaux demandés, pas un besoin d’Order autonome dans tous les contextes. Sans engagement propre, la capacité existante suffit ; ne pas dupliquer ses trois comportements.

**Cas fictif.** Un prestataire accepte d’inventorier quatre magasins à une date, livre des résultats partiels puis un solde ; cet engagement pourrait justifier la famille.

**Appuis marché :** [Microsoft Dynamics 365 — Cycle counting](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting), [SAP S/4HANA — Performing a Physical Inventory](https://learning.sap.com/courses/processes-in-sap-s-4hana-ewm-br/performing-a-physical-inventory). Les différences et limites sont consignées dans l’annexe.

## Faux manques et sujets conditionnels

- **Order Lifecycle / Order Hold Management** : Suspension, reprise, gel, annulation, reliquat et engagements sont explicitement communs aux familles Order. Ne pas recréer une capacité retirée.
- **Nouvelles variantes ATP par site, transport ou substitution** : Options déjà évaluables ; les comportements retenus distinguent la profondeur. Une alternative n’est pas automatiquement du CTP.
- **Comptage sur seuil ou anomalie** : BHV030 prévoit déjà un seuil ; BHV031 couvre la sollicitation ponctuelle. Aucun manque démontré.
- **Recall Management autonome** : Le rappel est d’abord un scénario transverse : retrouver les biens concernés, interdire les usages, suspendre les Orders, organiser les retours et leur traitement. La décision de rappel et la communication réglementaire/commerciale restent sous leur autorité externe ; ne pas importer tout le Quality Management.
- **Putaway / Storage Order systématiques** : Le rangement interne appartient à l’exécutant et Receiving Order ne crée pas implicitement une prestation autonome. Une garde avec engagements de durée, conditions et restitution mériterait une famille seulement si elle est réellement confiée. Pas de double appui primaire assez précis établi sur ce contrat de service dans cette recherche ; piste conditionnelle, non recommandation ferme.
- **Inventaire statistique** : SAP mentionne une voie externe de sample-based inventory ; l’acceptance sampling Dynamics vérifie la qualité, pas une extrapolation des quantités de stock. Ne pas fabriquer une équivalence ni un comportement sur cette preuve.
- **Fonctions ERP/WMS/TMS internes** : Comptabilité de stock, paie et charge du personnel, slotting, pilotage machines, conduite et placement 3D ne sont pas ajoutés. Leurs contraintes et résultats peuvent alimenter l’orchestration sans absorber leur réalisation.

## Proposition de priorité

Traiter d’abord la décision d’usage, la traçabilité, la disposition hors retours et la mise au rebut confiée : elles composent un parcours cohérent de traitement d’un lot défectueux. Expliciter ensuite le plan de transport et les variantes contractuelles d’inspection. Les relations d’alternatives doivent être attribuées au référentiel existant ; elles ne justifient pas une nouvelle capacité de décision.

Exemple de confrontation future : un accessoire défectueux est retrouvé dans plusieurs kits ; identifier les stocks et livraisons affectés, suspendre les usages concernés, faire contrôler les biens, orienter leur devenir et suivre les prestations confiées. Le rappel complet reste un scénario transverse ; chaque étape devra être reliée aux capacités retenues dans le modèle.

La seule liste de suivi est [l’annexe du backlog](../modeles/backlog/market-coverage-audit-U775.yaml). Elle contient la matrice des neuf sous-domaines, les constats, les références précises, les limites et les impacts sur le glossaire. L’audit historique U431 reste clos ; l’étude de conformité documentaire U773/U774 reste distincte de cet audit de couverture métier.

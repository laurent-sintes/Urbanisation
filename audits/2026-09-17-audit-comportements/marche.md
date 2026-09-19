# Marché : niveaux, responsabilités et comportements

Consultation du 17 septembre 2026, pour U265/U266. Sources primaires. Les rapprochements FLOW sont des **propositions de Codex**, pas des équivalences validées ni des preuves de couverture des SI. Le catalogue complet SAP retail/fashion et les réalisations Beaumanoir ne sont pas audités ici. Les versions explicitement citées sont celles consultées, pas une affirmation de dernière version disponible.

## Le problème d’alignement n’est pas seulement un niveau manquant

| Référence | Structure native consultée | Usage pour FLOW |
| --- | --- | --- |
| Microsoft Business Process Catalog | Six niveaux : end-to-end, process area, business process, scenario, system process, test case | Les derniers niveaux décrivent aussi configuration, écrans et tests. Un scénario peut éprouver plusieurs capacités et comportements ; ne pas recopier six niveaux de capacités. |
| SAP Reference Business Architecture | Enterprise Domain → Business Domain → Business Area → Business Capability ; liens vers solution capabilities et composants | Comparer les résultats et périmètres avant le rang. Une fonctionnalité S/4 n’est pas nécessairement un nœud du catalogue métier. |
| BIZBOK | Capability Behavior, Capability Instance et Capability Level sont distingués dans le glossaire | Le comportement est une notion reconnue ; son caractère terminal et son rattachement unique sont nos conventions FLOW. |
| TM Forum | TMFC007 relie activités eTOM, informations SID, fonctions et API | Un composant Service Order Management couvre plusieurs responsabilités FLOW ; le recopier ferait disparaître les distinctions orchestration/décision/tracking. |
| LeanIX | Recommandation de profondeur limitée, généralement deux ou trois niveaux | Appui à une carte utile et maintenable, pas prescription du nombre de niveaux de notre modèle. |

Sources : [S1 Microsoft, sections What’s in the catalog / Catalog IDs](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/about), [S2 SAP, Reference Architecture Content Example / Business Capability Model Example](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), [S3 BIZBOK 15.0, pages imprimées 456–457](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_glossary.pdf), [S4 TMFC007 1.2.1, sections 1–3](https://oda-production.s3.eu-west-2.amazonaws.com/v1.0.0/TMFC007_Service_Order_Management_v1.2.1.pdf), [S5 LeanIX, section 6 Don’t go too deep](https://www.leanix.net/en/wiki/ea/best-practices-to-define-business-capabilities).

**Conclusion d’audit :** Comportement rend la comparaison plus précise, sans rendre les arbres équivalents. Maintenir une correspondance plusieurs-à-plusieurs : élément natif et nature → responsabilité FLOW → comportement éventuellement concerné → périmètre couvert et écart. Les opérations détaillées, règles et tests restent des descriptions ou des preuves, pas un troisième niveau sous Comportement.

## Confrontation fonctionnelle

### Stock, protection et réservation

Microsoft distingue une allocation à des groupes avant la vente et une réservation souple liée à une transaction. Il décrit aussi consommation et ajustement des quantités allouées. Cela soutient la distinction entre **Supply Protection**, **Reservation** et la décision de quota ; cela ne tranche pas notre frontière Reservation / Supply Assignment. Proposition FLOW : expliciter validité, application et modification des protections ; tester sur une affectation future qui ne réserve pas immédiatement le stock physique. [S6 Inventory Visibility inventory allocation, Business background / Difference between inventory allocation and soft reservation / Terminology](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation).

### Planning, décisions et mise en action

Microsoft décrit plusieurs plans pour comparer des stratégies et des messages suggérant d’avancer, reporter ou ajuster les quantités des ordres. C’est un appui à la simulation et à la séparation entre résultat recommandé et application ; le module produit réunit des fonctions que FLOW répartit entre D05 et les capacités opérationnelles. [S7 Master plans overview, Using master plans / Action message](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans).

L’affermissement Microsoft dispose de modes manuels, automatiques et par requête/lot. Proposition FLOW : comportement d’affermissement dans le cycle des Orders, avec périmètre sélectionné et résultat explicable ; aucun besoin de créer une capacité Batch Firming. [S8 Firm planned orders, sections de firming](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming).

SAP IBP distingue versions, scénarios et simulations pour explorer d’autres situations. Proposition FLOW : **reconfigurer les hypothèses**, **simuler/comparer**, **valider un scénario** sous Inventory Planning ; les décisions D05 gardent leurs responsabilités de résultat. Le détail des versions SAP ne devient pas un niveau métier FLOW. [S9 Versions and Scenarios, sections Versions / Scénarios / Simulations](https://learning.sap.com/courses/mastering-sap-ibp-for-response-and-supply-order-based-planning-fr/versions-and-scenarios_d42f03ea-be09-49b7-9256-dc93207edee0_fr-FR).

### Promesse

SAP aATP réunit notamment contrôles de disponibilité, allocation, retraitement des confirmations et recherche d’alternatives. BOP réexamine les confirmations quand l’offre ou la demande change ; ABC examine lieux et articles de substitution. **Notre interprétation** répartit ces fonctions entre comportements ATP, Promise Revision, priorisation, affectation et éventuellement CTP selon l’adaptation requise. ABC n’est pas automatiquement CTP : un lieu déjà admissible peut relever de la situation de référence. La nouvelle maille aide précisément à documenter cet écart. [S10 Using aATP, PAC / PAL / BOP / ABC](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5).

### Orders et traitements collectifs

Microsoft décrit la mise en attente et sa levée avec leurs restrictions. Cela conforte des comportements du cycle de vie, sans transformer un motif d’attente en capacité. Les restrictions financières illustrées dans le produit ne réintroduisent pas la finance dans FLOW. [S11 Manage order holds, Place order on hold / Manage orders on hold](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/tasks/manage-order-holds).

La libération partielle de transferts en lot dépend de critères de satisfaction et distingue quantités totales ou réservées. Le **bénéfice du comportement collectif** est de rendre compréhensibles sélection, traitement partiel et reliquats ; « via batch » seul ne le justifie pas. La frontière entre autoriser l’Order et solliciter la logistique doit être décidée dans FLOW. [S12 Batch release of partially reserved transfer orders, fulfillment policies / Allow release in a batch](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/batch-release-of-partially-reserved-transfer-orders).

Microsoft décrit également des décisions de disposition des retours : réintégration, rebut, renvoi ou remplacement. C’est une question de responsabilité à instruire : ordre de retour en D04, décision Supply, demande du Case ou décision de l’exécutant ? Le comportement de rapprochement des réceptions ne suffit pas à attribuer cette responsabilité. Crédit/remboursement restent hors du périmètre Supply retenu. [S13 Sales returns, Disposition codes and disposition actions](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns).

### Exécution et adaptation

Oracle Supply Chain Orchestration organise la création de documents de fourniture, la transmission aux systèmes d’exécution et le retour des évolutions. Appui au pilotage transverse ; ce périmètre Oracle déborde notre D06 et mobiliserait aussi D04/D03. [S14 How Supply Chain Orchestration Works, tableau du déroulement](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/fauco/how-supply-orchestration-works.html).

Oracle Order Management décrit les changements en cours d’exécution et leurs compensations. Proposition FLOW : distinguer **décider une variation** (D06.f), **coordonner son application et les dépendances** (D06.d), **modifier les Service Orders** (D07.b), puis observer et rapprocher. Une annulation/recréation est une possibilité, pas une règle universelle ; les effets physiques déjà réalisés peuvent empêcher un retour arrière. [S15 Overview of Managing Change…, 25C, compensation](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/faiom/overview-of-managing-change-that-occurs-during-order-fulfillment.html).

TMF633 couvre le cycle du catalogue de services. **Écart volontaire :** D14 ingère une projection externe, il n’administre pas le catalogue maître. Les API et composants TM Forum servent à éprouver nos contrats, pas à imposer leur modèle télécom. [S16 TMF633 v4.0, Overview](https://www.tmforum.org/open-digital-architecture/open-apis/service-catalog-management-api-TMF633/v4.0).

## Ce que cette comparaison ne démontre pas

Elle ne prouve ni l’exhaustivité du catalogue local, ni la couverture fonctionnelle d’un produit par FLOW, ni une implémentation dans les trois SI. La maille behavior facilite l’analyse de simulation, masse, exceptions et temporalité. Elle ne résout pas une responsabilité absente ou deux capacités qui modifient le même engagement. Aucun alignement direct L3/L4 n’est proposé. Les correspondances restent proposées (CMP089) ; les pages évolutives n’ont pas une édition métier commune.

Deux URL anciennes ont échoué à l’ouverture : Microsoft `planned-orders-manual-firming` et `sales-marketing/order-holds`. Les pages officielles S8/S11 ont été trouvées et consultées en remplacement. La page répertoire TMFC007 n’était pas accessible ; S4 est la spécification officielle effectivement lue.

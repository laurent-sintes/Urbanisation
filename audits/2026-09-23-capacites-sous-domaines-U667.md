# Audit des capacités — proposition de rattachement aux huit sous-domaines

23 septembre 2026 — U667, actualisé par U668–U672. **Proposition non appliquée au modèle canonique.**

[Source YAML de cette vue](../modeles/backlog/capability-subdomain-audit-U667.yaml). Vue dérivée, sans catalogue autonome. Les noms et identifiants ci-dessous sont ceux des capacités existantes.

**58 capacités examinées : 57 proposées dans les huit sous-domaines et 1 hors périmètre, sans parent cible. Plans reçoit Supply et Demand Plans par ingestion (U669).** Le total cible serait 59 capacités internes, sous réserve des arbitrages signalés.

| Sous-domaine | Existantes proposées | Ajouts proposés |
| --- | ---: | ---: |
| Master Data | 14 | 0 |
| Policies | 3 | 0 |
| Plans | 0 | 2 |
| Order Management | 11 | 0 |
| Inventory Management | 6 | 0 |
| Order Promising | 5 | 0 |
| Demand & Supply Matching | 9 | 0 |
| Fulfilment Orchestration | 9 | 0 |


**Accord U672 : Order Promising** remplace le nom Supply Availability. Sa responsabilité est de déterminer et recommander ce qu’on peut promettre en quantité, date et conditions. Il peut être sollicité avant création ou confirmation d’une commande, ainsi que par Matching.

| Sous-domaine | Responsabilité validée U672 |
| --- | --- |
| Order Promising | Déterminer et recommander ce qu’on peut promettre. |
| Demand & Supply Matching | Arbitrer les affectations dans le master plan de matching. |
| Order Management | Confirmer, porter et réviser l’engagement de la commande. |

Les rattachements et arbitrages de capacités ci-dessous conservent leurs statuts propres ; la validation du nom et de ces frontières ne les adopte pas globalement.

## Conclusions

- U668 : Supply Plan porte les prévisions d’entrées ou de sorties de stock hors achats. Le master plan de matching porte les affectations et reste entièrement géré dans Matching. Aucun lien d’identité entre les deux objets ; les achats projetés APS évoqués en U656 ne sont pas reclassés en Supply Plan.
- 57 capacités existantes ont un rattachement proposé dans les huit sous-domaines ; Demand Planning est hors périmètre, sans parent cible. Aucun sous-domaine externe ni retrait exécuté.
- Plans : responsabilité d’ingestion des Supply et Demand Plans confirmée U669 ; visibilité proposée séparément, non adoptée. Total cible envisagé : 59 capacités internes si toutes les propositions sont retenues.
- Les sept référentiels et leurs quatorze capacités restent distincts sous Master Data. Corriger les formulations de simple copie passive incompatibles avec U479, sans reprendre la maîtrise d’entreprise.
- Les décisions Inventory Target, Initial Stocking et Replenishment sont conservées provisoirement dans Matching pour l’arbitrage opérationnel. Leur périmètre doit être borné face aux calculs APS externes ; l’accord sur les sous-domaines ne tranche pas ce détail.
- Return Disposition Decision est proposé dans Fulfilment : choisir le traitement du bien retourné ne constitue pas par nature un arbitrage de couverture. Une conséquence collective mobilise Matching. Ce déplacement reste à discuter.
- Reservation Policy Decision et Group Protection Decision restent dans Matching pour leur résultat calculé ; Policies porte les règles actives. Reservation reste dans Inventory. Aucun déplacement fondé uniquement sur le mot Policy.
- Service Capacity Visibility reste chez Fulfilment ; Supply Visibility consolide les attendus dans Availability ; Inventory Visibility expose les positions et projections de stock. Leurs consommateurs ne deviennent pas leurs propriétaires.
- ATP, CTP, PTP et Delivery Schedule Decision couvrent déjà faisabilité et recommandation ; Fulfillment Commitment porte l’engagement dans Order Management. Aucun ajout automatique d’une capacité générique de promesse.
- Fulfillment Plan Decision désigne actuellement le choix du plan de couverture dans Matching ; Process Adaptation Decision désigne les adaptations d’exécution dans Fulfilment. Leurs noms/définitions doivent éviter le même mot plan sans qualification.
- Apply Plan, Simulation & Analysis et les commandes de planning sont déjà des comportements de D05.f. L’audit ne les recrée pas en capacités, ne ressuscite aucun identifiant retiré et ne rouvre pas U431.
- Le décompte porte sur la couverture du catalogue existant, pas sur une preuve d’exhaustivité de toutes les responsabilités possibles du domaine ni sur des fonctionnalités installées chez Beaumanoir.

## Placement capacité par capacité

« Direct » qualifie le rattachement proposé, jamais un nouvel accord sur la fiche. Les notes de frontière ne créent pas de règles détaillées.

### Master Data

Tenir les références locales Supply sur les sept sujets existants.

| ID | Capacité actuelle | Parent actuel | Conclusion | Motif et frontière |
| --- | --- | --- | --- | --- |
| D08.d | Product Reference Ingestion | Product Reference | Direct ; rédaction à harmoniser | Intégrer les références et leurs évolutions pour Product Reference ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D08.e | Product Reference Visibility | Product Reference | Direct ; rédaction à harmoniser | Construire et exposer la vue de référence pour Product Reference ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D09.d | Party / Role Ingestion | Party / Role | Direct ; rédaction à harmoniser | Intégrer les références et leurs évolutions pour Party / Role ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D09.e | Party / Role Visibility | Party / Role | Direct ; rédaction à harmoniser | Construire et exposer la vue de référence pour Party / Role ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D11.a | Agreement Ingestion | Agreement | Direct ; rédaction à harmoniser | Intégrer les références et leurs évolutions pour Agreement ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D11.b | Agreement Visibility | Agreement | Direct ; rédaction à harmoniser | Construire et exposer la vue de référence pour Agreement ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D12.a | Product Catalog Ingestion | Product Catalog | Direct ; rédaction à harmoniser | Intégrer les références et leurs évolutions pour Product Catalog ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D12.b | Product Catalog Visibility | Product Catalog | Direct ; rédaction à harmoniser | Construire et exposer la vue de référence pour Product Catalog ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D13.a | Fulfillment Network Ingestion | Fulfillment Network | Direct ; rédaction à harmoniser | Intégrer les références et leurs évolutions pour Fulfillment Network ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D13.b | Fulfillment Network Visibility | Fulfillment Network | Direct ; rédaction à harmoniser | Construire et exposer la vue de référence pour Fulfillment Network ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D14.a | Service Catalog Ingestion | Service Catalog | Direct ; rédaction à harmoniser | Intégrer les références et leurs évolutions pour Service Catalog ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D14.b | Service Catalog Visibility | Service Catalog | Direct ; rédaction à harmoniser | Construire et exposer la vue de référence pour Service Catalog ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D16.a | Assortment Ingestion | Assortment | Direct ; rédaction à harmoniser | Intégrer les références et leurs évolutions pour Assortment ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |
| D16.b | Assortment Visibility | Assortment | Direct ; rédaction à harmoniser | Construire et exposer la vue de référence pour Assortment ; conserver ce sujet et son identité. Harmoniser les formulations « pas de maître local » avec U479 : autorité locale Supply, maîtrise d’entreprise externe. Ne pas transformer l’ingestion en conception du référentiel d’entreprise. |

Appui marché et limite : Les produits documentent des références consommées par les Orders ; les sept regroupements sont un choix FLOW. La maîtrise locale U479 doit être distinguée de la maîtrise d’entreprise externe. Sources : [ELM522](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/data-management), [ELM652](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/how-order-to-cash-works-in-order-management.html).

### Policies

Gouverner les règles applicables, leur validité et leur activation.

| ID | Capacité actuelle | Parent actuel | Conclusion | Motif et frontière |
| --- | --- | --- | --- | --- |
| D02.b | Supply Protection | Reference & Policy Management | Direct | Règles actives de protection, réservation et renouvellement des ressources. Conserver la gouvernance des paramètres applicables ; les recommandations de valeurs issues du Matching ne les activent pas implicitement. |
| D19.a | Service Provider Policy | Reference & Policy Management | Direct | Règles actives d’admissibilité et de sollicitation des prestataires. Ne pas confondre conditions de référence du service, capacité communiquée et choix effectif du prestataire. |
| D19.b | Demand Protection Policy | Reference & Policy Management | Direct | Règles de protection et de priorité de la demande. Demand garde ici son sens large ; Order Prioritization applique ces règles aux commandes en concurrence. |

Appui marché et limite : Les règles DOM et protections SAP étayent l’encadrement des décisions. Ces produits ne prescrivent pas un sous-domaine autonome Policies. Sources : [ELM394](https://learn.microsoft.com/en-us/dynamics365/commerce/dom-rules), [ELM452](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4).

### Plans

Tenir et exposer les données prévisionnelles calculées hors du domaine.

| ID | Capacité actuelle | Parent actuel | Conclusion | Motif et frontière |
| --- | --- | --- | --- | --- |

Aucune capacité existante ne couvre exactement cette responsabilité. L’ingestion des Supply et Demand Plans est confirmée U669 ; son libellé et sa description détaillée restent proposés. La visibilité reste une proposition distincte :

- **Plan Ingestion** (responsabilité confirmée U669) : Recevoir et intégrer les Supply et Demand Plans fournis par l’APS externe, avec leur origine, horizon, version et statut. Supply Plan désigne les prévisions d’entrées ou de sorties de stock hors achats. Distinguer remplacement d’une projection et modification d’un Order déjà pris en charge ; conserver les liens utiles au rapprochement prévision-commandes, sans calculer la prévision ni effacer un engagement. Exemple fictif : Une prévision d’entrée de stock hors achat passe de 100 à 80 pièces : conserver sa révision sans la transformer en réception constatée.
- **Plan Visibility** : Rendre consultables les projections de demande et de mouvements de stock hors achats, leurs versions, dates, conditions et fraîcheur pour éclairer la promesse et le Matching. Ne construit ni prévisions ni master plan de matching. Une projection consultable ne devient pas un approvisionnement ferme. La consommation de prévision par les Orders doit être portée par le calcul de couverture du Matching en s’appuyant sur ces liens. Exemple fictif : Présenter une sortie de stock hors achat prévue à J+3 avec son origine et son incertitude, distincte d’un mouvement réalisé.

Appui marché et limite : Les plans externes et besoins prévisionnels sont documentés ; leur ingestion dans un sous-domaine autonome est une frontière FLOW. Le sens Supply Plan hors achats vient de U668 ; ces sources ne prouvent pas une équivalence avec Supply Planning éditeur. Sources : [ELM415](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans), [ELM649](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-manufacturing-production-planning/outlining-program-planning_be612648-050c-4353-a60a-808b38c67c5a).

### Order Management

Tenir les Orders, leurs évolutions et les engagements qu’ils portent.

| ID | Capacité actuelle | Parent actuel | Conclusion | Motif et frontière |
| --- | --- | --- | --- | --- |
| D04.i | Sales Order | Demand Management | Frontière à réécrire | Contenu, évolutions et reste à servir des commandes clients. Corriger les renvois qui attribuent encore les possibilités de promesse à Demand Management. |
| D04.j | Purchase Order | Demand Management | Frontière à réécrire | Commandes d’achat de biens ou prestations et propositions adressées au domaine. L’APS conserve sa projection d’achat ; l’Order porte la proposition adressée au domaine puis son éventuel affermissement. U668 exclut les achats de Supply Plan. Aucune création automatique ni double comptage. |
| D04.k | Transfer Order | Demand Management | Frontière à réécrire | Ordres de transfert et suivi des départs et arrivées attendus. Une proposition APS reste une donnée de plan avant sa prise en charge comme Order ; ne pas dupliquer les mêmes quantités. |
| D04.l | Return Order | Demand Management | Direct | Demande de retour, quantités et suites attendues. Conserver les parcours spécifiques ; le choix du devenir et les prestations sont mobilisés auprès de Fulfilment, pas exécutés par l’Order. |
| D04.m | Supplier Return | Demand Management | Direct | Renvois fournisseur et attentes de crédit, remplacement ou réparation. Préserver le lien avec les achats de remplacement ; ni comptabilité de l’avoir ni réalisation physique dans cette capacité. |
| D04.n | Order Structuring | Demand Management | Direct | Structure, filiation et cohérence des commandes composées ou scindées. Une scission des prestations ne provoque pas nécessairement une scission documentaire ; préserver les statuts proposés de Grouping et Merging. |
| D04.o | Order Lifecycle Management | Demand Management | Direct | Transitions autorisées du contenu et des engagements des Orders. Le retrait d’une projection APS ne supprime pas un Order engagé ; appliquer les suites autorisées en tenant compte du réalisé. |
| D04.q | Order Archiving | Demand Management | Direct | Conservation et consultation historique des Orders.  |
| D04.r | Consignment Fill-up Order | Demand Management | Direct | Demandes d’apport de biens restant consignés. Ne pas absorber la gestion durable du stock consigné ni la décision d’implantation. |
| D04.t | Consignment Pick-up Order | Demand Management | Direct | Demandes de reprise de biens restés consignés. Conserver l’intention distincte d’un retour après vente ou d’un transfert interne. |
| D03.n | Fulfillment Commitment | Demand Management | Frontière à réécrire | Proposition, confirmation et révision de l’engagement porté par l’Order. Distinguer formalisation de la proposition et choix de la réponse recommandée par Availability. Ne pas recalculer ici le plan ou la promesse. |

Appui marché et limite : Les types d’Orders et leur traitement sont attestés ; FLOW sépare recommandation de promesse et orchestration de réalisation, souvent réunies dans les offres OMS. Sources : [ELM112](https://www.ibm.com/docs/en/order-management?topic=configuration-document-types), [ELM652](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/how-order-to-cash-works-in-order-management.html).

### Inventory Management

Tenir faits, positions, régimes et réservations de stock.

| ID | Capacité actuelle | Parent actuel | Conclusion | Motif et frontière |
| --- | --- | --- | --- | --- |
| D01.f | Inventory Tracking | Inventory Management | Frontière à réécrire | Quantités et états de stock établis à partir des faits reconnus. Resserrer la phrase sur le suivi des ressources futures : consommer Supply Visibility pour les projections, sans reprendre la tenue des attendus. |
| D01.g | Record Inventory Movements | Inventory Management | Direct | Faits de mouvements, corrections et justifications de stock.  |
| D01.c | Inventory Visibility | Inventory Management | Direct | Lecture des positions physiques, logiques et projetées. Une projection de stock utilise Plans et Supply Visibility ; elle ne prouve pas qu’une quantité est promettable. |
| D01.d | Stocktaking | Inventory Management | Direct | Comptages, écarts et corrections justifiées. Le protocole de comptage reste partie de la capacité. Si une règle devient partagée, Policies la gouverne ; aucune scission systématique par règle. |
| D02.c | Reservation | Inventory Management | Direct | Tenue des engagements de quantité opposables aux usages concurrents. Matching demande une réservation mais ne la possède pas. Une affectation du plan ne réserve pas implicitement la ressource (U436). |
| D01.h | Consigned Inventory Management | Inventory Management | Direct | Application du régime et des droits du stock consigné. La fin de l’Order d’apport ne met pas fin à cette responsabilité. |

Appui marché et limite : Les distinctions physiques, attendues et réservées sont étayées. La valorisation financière de certains ERP est hors du périmètre retenu. Sources : [ELM408](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-on-hand-list), [ELM449](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-inventory-management_d2aad6e6-a57e-4f64-9ac0-3b27f613776a).

### Order Promising

Établir les réponses possibles et sélectionner la promesse recommandée.

| ID | Capacité actuelle | Parent actuel | Conclusion | Motif et frontière |
| --- | --- | --- | --- | --- |
| D18.a | Supply Visibility | Supply Management | Frontière à réécrire | Vue qualifiée des apports attendus, de leurs dates et de leur fermeté. Consolider les attendus issus des Orders, des opérations et des Plans sans reprendre leurs autorités ni assimiler projection APS, engagement et réception. |
| D03.i | Available-to-Promise (ATP) | Demand & Supply Optimization | Direct | Réponses quantité/date possibles sur les ressources admissibles. Consommer les ressources futures qualifiées ; un calcul ATP ne confirme ni ne réserve. |
| D03.j | Capable-to-Promise (CTP) | Demand & Supply Optimization | Frontière à réécrire | Réponses possibles nécessitant une adaptation et conditions associées. Une alternative calculée ne vaut ni réaffectation de ressources partagées ni décision locale d’exécution. Mobiliser Matching ou Fulfilment selon l’effet recherché. |
| D03.k | Profitable-to-Promise (PTP) | Demand & Supply Optimization | Direct | Comparaison économique et choix recommandé parmi les réponses faisables. Conserver la dimension économique sans en faire l’objectif unique ; sélection de promesse sous réserve des arbitrages Matching. |
| D03.l | Delivery Schedule Decision | Demand & Supply Optimization | Direct | Sélection des quantités et dates de la réponse recommandée. Conserver la décision de calendrier dans Availability ; confirmation et révision de l’engagement restent dans Order Management. |

Appui marché et limite : GOP et aATP examinent des alternatives ; la séparation FLOW d’avec Matching et l’engagement confirmé n’est pas une frontière uniforme du marché. Sources : [ELM352](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/fascp/overview-of-global-order-promising.html), [ELM653](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-aatp_a1595e13-8923-4514-b889-ec4f63ef1ad5).

### Demand & Supply Matching

Construire et maintenir un master plan de matching cohérent de couverture de la demande.

| ID | Capacité actuelle | Parent actuel | Conclusion | Motif et frontière |
| --- | --- | --- | --- | --- |
| D03.m | Order Prioritization | Demand & Supply Optimization | Direct | Priorités relatives des commandes en concurrence pour les ressources. Les règles sont dans Policies ; leur application contextualisée participe à l’arbitrage du plan. |
| D03.o | Fulfillment Plan Decision | Demand & Supply Optimization | Frontière à réécrire | Choix du scénario de couverture et des affectations de ressources. Le résultat est le master plan de matching, pas le plan des prestations malgré le mot Fulfillment du nom actuel. Inclure commandes et prévision résiduelle sans double compte. |
| D05.a | Inventory Target Decision | Demand & Supply Optimization | Périmètre / placement à arbitrer | Décision sur les cibles de stock utiles aux scénarios de couverture. Proposition à borner : conserver les arbitrages de cibles nécessaires au Matching ; consommer les cibles APS reçues sans reconstruire sa planification. Policies gouverne les valeurs activées. |
| D05.d | Group Protection Decision | Demand & Supply Optimization | Direct | Arbitrage des quantités protégées ou plafonnées par groupe. Le calcul est une décision du Matching ; la règle active et ses périodes sont gouvernées par Policies. Ce n’est pas une réservation individuelle. |
| D05.g | Initial Stocking Decision | Demand & Supply Optimization | Périmètre / placement à arbitrer | Choix des apports opérationnels pour constituer le stock initial. Conserver sous réserve de borner la frontière APS : exécuter et ajuster la couverture du lancement, sans recalculer l’assortiment ni le plan prévisionnel amont. |
| D05.e | Replenishment Decision | Demand & Supply Optimization | Périmètre / placement à arbitrer | Choix des apports et ajustements nécessaires à la couverture courante. Le périmètre actuel inclut des compléments fournisseur : à resserrer pour ne pas dupliquer les achats projetés par l’APS. Garder les arbitrages opérationnels de couverture et remonter les besoins de révision du plan externe. |
| D05.c | Stock Redistribution Decision | Demand & Supply Optimization | Direct | Rééquilibrage du stock existant entre lieux. Coordonner les effets avec le réassort ; les Orders matérialisent les demandes de transfert et Fulfilment les réalise. |
| D05.f | Demand & Supply Optimization Planning | Demand & Supply Optimization | Frontière à réécrire | Construction, comparaison, maintien et application du master plan de matching. Remplacer la dépendance au calcul interne de Demand Planning par les données Plans. Maintenir les neuf comportements, dont Apply Plan et Simulation & Analysis ; ne pas recréer Order Backlog Planning. |
| D05.h | Reservation Policy Decision | Demand & Supply Optimization | Direct | Décision contextualisée sur les conditions de réservation à recommander. Conserver dans Matching car la fiche recommande des conditions selon les tensions ; Policies les active et Inventory tient les réservations. Le mot Policy ne suffit pas à changer le propriétaire. |

Appui marché et limite : Planifier, simuler et appliquer des affectations sont documentés. Le périmètre FLOW inclut aussi la demande prévisionnelle résiduelle, au-delà des seuls portefeuilles de commandes de ces exemples. Sources : [ELM650](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faubm/overview-of-backlog-management-processes.html), [ELM654](https://learn.microsoft.com/en-us/dynamics365/commerce/dom-runs-results).

### Fulfilment Orchestration

Obtenir les prestations et adapter leur réalisation en préservant les engagements.

| ID | Capacité actuelle | Parent actuel | Conclusion | Motif et frontière |
| --- | --- | --- | --- | --- |
| D06.b | Service Capacity Visibility | Fulfillment Orchestration | Direct | Connaissance des capacités opérationnelles communiquées par les exécutants. Conserver chez Fulfilment, responsable du dialogue avec les exécutants ; Availability et Matching la consomment. Un plafond communiqué n’est pas un disponible calculé. |
| D07.a | Service Requirements Decision | Fulfillment Orchestration | Direct | Détermination des prestations et résultats nécessaires. Peut être mobilisée en préparation de la promesse ; la consommation par Availability ne change pas son propriétaire. |
| D07.b | Service Task Management | Fulfillment Orchestration | Direct | Tenue des sollicitations de services, réponses et reprises. Task et Order restent distincts ; un acquittement technique ne prouve pas l’achèvement physique. |
| D07.c | Service Reconciliation | Fulfillment Orchestration | Direct | Rapprochement du réalisé et de l’attendu des prestations. Fournir les écarts aux Orders et les faits à Inventory ; ne pas tenir à leur place le reliquat commande ou le stock. |
| D07.d | Operations Tracking | Fulfillment Orchestration | Frontière à réécrire | Suivi des faits, jalons et estimations pendant les prestations. Alimenter Supply Visibility pour les attendus consolidés ; supprimer toute lecture comme seconde tenue des mêmes ressources futures. |
| D06.d | Process Orchestration | Fulfillment Orchestration | Direct | Coordination des prestations et de leurs dépendances. Distinguer le plan d’exécution coordonné du master plan de matching arbitré dans Matching. |
| D06.e | Service Selection Decision | Fulfillment Orchestration | Direct | Choix des services et exécutants permettant la réalisation. Choisir les moyens initiaux ou alternatifs en préservant promesse et grands équilibres. Consulter cette décision pendant une étude de faisabilité reste possible. |
| D06.f | Process Adaptation Decision | Fulfillment Orchestration | Frontière à réécrire | Choix des adaptations locales de réalisation face aux aléas. Réécrire « variations du plan » en « adaptations du plan d’exécution ». Préserver promesse et grands équilibres ; transmettre les impacts non absorbables à Matching et Order Management, sans seuils à définir ici. |
| D05.i | Return Disposition Decision | Demand & Supply Optimization | Périmètre / placement à arbitrer | Choix du devenir logistique des biens retournés selon leur état et la valeur récupérable. Rattachement proposé à discuter : décision de traitement du retour dans Fulfilment ; demander l’arbitrage Matching si l’orientation affecte les ressources partagées. Ne pas absorber remboursement, inspection physique ou mouvements de stock. |

Appui marché et limite : La coordination des services et retours d’exécution est étayée ; l’autonomie locale respectant Matching est un choix explicite FLOW U664. Sources : [ELM651](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/orchestration-processes.html), [ELM405](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview).

## Capacité actuelle hors périmètre

D17.a **Demand Planning**, actuellement dans Demand Management, calcule les prévisions. Elle est inventoriée pour préparer sa sortie du domaine avec BHV095, en conservant leur histoire. **Aucun parent cible externe ni sous-domaine supplémentaire** n’est créé (U669).

## Cas du devenir des retours

Proposer Fulfilment pour le choix du traitement du retour ; conserver le recours à Matching pour les effets sur les ressources partagées. Éviter de faire de Matching le propriétaire de toute décision comportant un critère économique. Expliciter la transmission des effets de disponibilité au Matching et à Availability.

Ce placement est une recommandation FLOW. Les deux sources documentent le choix du devenir, sans prescrire cette frontière de sous-domaines :

- [Specify how to dispose of returned items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items) — Le devenir du bien retourné est distingué de son motif ; les actions produit peuvent également porter des effets financiers.

- [Smart Disposition](https://blueyonder.com/solutions/returns-management/smart-disposition) — L’état, la destination et la valeur de revente contribuent au choix du devenir du retour.

## Passage au modèle

- Matérialiser les nouveaux sous-domaines et parents seulement après examen de cette proposition ; ne pas recycler les identifiants retirés.
- Conserver identités, comportements et provenance des capacités ; le déplacement d’une fiche n’adopte pas ses champs proposés.
- Borner les trois décisions de stock face à l’APS et examiner le rattachement du devenir des retours.
- Réviser les renvois Demand/Order, plan APS/plan Matching/plan d’exécution et l’autorité locale Master Data.
- Capturer les accords sur les valeurs finales exactement présentées ; une publication reste une opération distincte.

Vérification de couverture : chaque capacité active figure une fois ; parents et enfants sont conservés dans le YAML. Aucun comportement promu en capacité, aucun retrait ou rattachement exécuté dans le modèle.


## Réexamen Order Promising — U670

Responsabilité et usages confirmés en U672 : Order Promising alimente directement **Order Management** (réponse de promesse recommandée) et **Matching** (possibilités et alternatives de couverture). Matching fournit en retour les affectations et contraintes de son master plan ; Order Management porte et transmet les engagements. Une consultation n’impose pas un nouvel arbitrage collectif.

Les lignes ATP/CTP/PTP du tableau conservent les noms du catalogue audité, sans les réadopter. ATP trouve une place claire dans Availability. CTP doit être borné à l’évaluation des ressources/capacités mobilisables : reprendre une affectation à une autre commande relève de Matching. PTP apporte une dimension économique aux réponses possibles ; ce n’est pas une troisième catégorie exclusive de disponibilité. Réexaminer la maille avant d’entériner trois capacités parallèles.

Le cas B2C envisage moins de 200 ms pour répondre sur la promettabilité, sans performance mesurée ni garantie. Une réponse fondée sur les données disponibles et les arbitrages existants peut éviter un recalcul collectif ; une demande nécessitant un nouvel arbitrage doit rester conditionnelle jusqu’à sa résolution. Consultation et confirmation restent distinctes : deux lectures favorables de la dernière pièce ne créent pas deux droits sur cette pièce. La réservation reste dans Inventory Management.

Appuis : [Oracle Promising](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/fascp/overview-of-global-order-promising.html), [SAP aATP](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-aatp_a1595e13-8923-4514-b889-ec4f63ef1ad5), [Microsoft reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations). Les frontières des produits ne sont pas celles des sous-domaines FLOW. Détails et limites : `availability_discussion_U670` dans l’annexe YAML.

# Audit de maturité — confrontation à Microsoft

**Audit U249, 16 septembre 2026.** Auteur : Codex. Objet comparé : FLOW **v007**, publication `2026-09-16.2`, lue dans `modeles/release/2026-09-16.2/model.yaml` : 41 capacités, leurs descriptions et leurs frontières. Les rapprochements ci-dessous sont **proposés**, sans modification du modèle ni validation des formulations publiées.

## Conclusion

Le découpage FLOW est cohérent avec plusieurs distinctions opérationnelles de Microsoft : connaissance du stock / allocation / réservation, promesse / commande, choix de réalisation / orchestration, ordre métier / ordre adressé à l'entrepôt. Il ne reproduit pas une suite ERP : c'est un avantage dans un environnement à maîtres et exécutants externes.

Les trois travaux les plus utiles sont : **fermer la boucle entre optimisation et commandes**, **expliquer le passage des faits d'exécution vers le stock et les reliquats**, et **préciser les décisions autour des retours**. Ils demandent d'abord des responsabilités et des relations explicites ; pas nécessairement de nouvelles capacités.

Le principal écart de vocabulaire reste **CTP** : Microsoft raisonne sur matières, capacité de production et délais de transport ; FLOW lui attribue aussi des variantes de protections et d'engagements. Cette extension locale est assumable, mais elle doit rester visible. [MS04](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp)

## Périmètre et nature de la preuve

La comparaison emploie la documentation fonctionnelle de Dynamics 365 Supply Chain Management, Inventory Visibility et Intelligent Order Management. Ce sont des **fonctionnalités, objets et composants de produits**, pas un catalogue homogène de capacités métier. Aucun rapport un pour un n'est présumé ; aucune installation dans les SI Beaumanoir, Boardriders ou Sarenza n'est inférée.

Les opérations internes des entrepôts et du transport ne deviennent pas des capacités FLOW. Finance, conformité, conception produit et planification de saison restent hors périmètre. Les données utiles venant de ces contextes peuvent néanmoins constituer des entrées.

La page officielle de cycle de vie affiche Intelligent Order Management **« In Support »** à la consultation. Ce constat ne prouve ni une feuille de route particulière ni la disponibilité de toutes ses fonctionnalités dans chaque région. Aucune retraite du produit n'est établie ici. [MS12](https://learn.microsoft.com/en-us/lifecycle/products/dynamics-365-intelligent-order-management)

## Matrice des capacités et frontières

Les 41 capacités sont toutes représentées dans les lignes suivantes. « Non établi » signifie que les passages consultés ne suffisent pas à démontrer le rapprochement, pas que Microsoft ignore le sujet. Les références D02/D07 désignent les identités conservées, avec leurs rattachements actuels à D01/D03/D06.

| Capacités FLOW | Élément Microsoft consulté et relation proposée | Conclusion pour FLOW |
| --- | --- | --- |
| **D01.f Inventory Tracking ; D01.g Record Inventory Movements ; D01.c Inventory Visibility** | Inventory Visibility consolide des états provenant de plusieurs systèmes, reçoit leurs variations et expose les disponibilités. Recouvrement partiel : ce service regroupe des fonctions que FLOW sépare. MS01. | Conserver les trois résultats : état actualisé, historique explicatif, lecture consommable. Décrire un même fait reçu tardivement et sa prise en compte sans double compte. Ne pas créer trois autorités sur la même quantité. |
| **D01.d Stocktaking** | Le mode Warehouse-only expose ajustements de comptage et rapprochement des stocks entre systèmes. Appui méthodologique, pas équivalence entre les deux opérations. MS07. | Le comptage physique est présent. Le rapprochement des représentations numériques reste à attribuer explicitement : ce n'est ni un nouveau comptage obligatoire ni le rapprochement de prestations D07.c. |
| **D02.b Supply Protection ; D02.c Reservation** | Inventory allocation protège des quantités pour des groupes ; soft reservation engage une quantité pour une demande et gère son annulation/consommation. Recouvrement partiel. MS02–MS03. | Frontière convaincante. Étendre les descriptions courtes avec validité, consommation, libération et effets d'une annulation. Le nom Supply Protection n'est pas renommé par cet audit. |
| **D03.i Available-to-Promise (ATP)** | ATP utilise stock non engagé, réceptions, sorties et délais ; ATP + Issue margin distingue une marge de préparation. Recouvrement partiel. MS04. | Bonne maille de décision. Expliciter les protections admissibles, l'horizon et les dates de disponibilité, expédition et réception. Une marge forfaitaire ne prouve pas une capacité logistique restante. |
| **D03.j Capable-to-Promise (CTP)** | CTP incorpore capacité et besoins de réalisation. MS04. | FLOW est plus large sur la modification des engagements et des protections. Garder une note d'écart et un exemple de variante autorisable ; ne pas présenter cette portée comme la définition Microsoft. |
| **D03.k Profitable-to-Promise (PTP)** | Fulfillment and Returns Optimization choisit des sources sous contraintes de service et objectifs économiques. Recouvrement partiel, aucun élément Microsoft nommé PTP démontré ici. MS10. | Bonne responsabilité économique ; préciser les coûts et contraintes reçus, sans absorber comptabilité ni tarification. |
| **D03.l Delivery Schedule Decision ; D03.m Order Prioritization** | Les contraintes de fulfillment abordent notamment réalisation partielle, nombre de sources et horaires. Le détail d'une priorisation métier équivalente n'est pas établi. MS10. | L'échéancier et la priorité restent deux résultats distincts. Ne pas confondre limite de fractionnement et priorité entre Orders. Une règle « jamais scinder » est un paramètre, pas une capacité. |
| **D03.a Promise Proposal ; D03.b Promise Confirmation ; D03.c Promise Revision** | CTP renseigne et recalcule des dates confirmées ; la documentation produit n'expose pas la même séparation de trois capacités. MS04. | Distinction sémantique utile entre proposition et engagement. **Maille des actions à challenger** : pourquoi trois capacités ici alors que le cycle du Service Order est regroupé ? Garder la séparation si chaque responsabilité possède un résultat durable distinct ; sinon envisager une gestion du cycle de la promesse, sans fusion automatique. |
| **D02.e Supply Assignment** | Réservation et plan d'affectation aux sources apportent des appuis partiels ; aucune équivalence complète au périmètre FLOW, qui inclut ressources futures et besoins prévisionnels. MS03, MS10. | Décrire le résultat d'affectation et sa différence avec l'engagement de réservation. Le lecteur doit comprendre si une couverture proposée, retenue ou engagée est manipulée. |
| **D04.i Sales Order Management ; D04.j Purchase Order Management ; D04.k Transfer Order Management ; D04.m Supplier Return Management** | Les documents de commande, types d'achat/retour et origines d'achats automatiques sont documentés ; les shipment orders Warehouse-only restent distincts des Orders ERP. Recouvrement partiel. MS11, MS07. | Maille par type adaptée. Le détail complet des ventes et transferts n'a pas été reconstitué avec ces seules pages. Aucun type supplémentaire obligatoire déduit des objets techniques. |
| **D04.l Customer Return Management** | Sales returns inclut motifs, disposition des biens et interactions avec remplacement ou crédit. Périmètre produit plus large. MS06. | Manque de responsabilité explicite sur le **sort du produit retourné** : remise en stock vendable, autre état, renvoi, rebut. Finance et inspection physique restent externes ; il faut préciser qui décide et qui enregistre le résultat. |
| **D04.n Order Structuring ; D04.o Order Lifecycle Management** | Les achats peuvent provenir d'intentions planifiées ; la documentation distingue retard de traitement, changement et conversion en ordre. MS11, MS05. | Garder ces gestions transversales larges. D04.o est actuellement `nature: decision` : préciser s’il décide des transitions ou tient le cycle lui-même, sans en faire autant de capacités que de verbes. |
| **D05.a Coverage Target Decision ; D05.d Stock Allocation Decision** | Les paramètres de couverture et les allocations fournissent des appuis, mais n'établissent pas une fonction unique calculant un optimum de niveau de service/risque. MS05, MS02. | Séparation décision / tenue des protections pertinente. Ne pas assimiler une fonctionnalité d'édition de quotas à une décision d'optimisation. Les données d'entrée et le résultat recommandable doivent être concrets. |
| **D05.e Replenishment Decision ; D05.c Stock Redistribution Decision** | Les plans suggèrent des Orders et des variations de dates/quantités ; ils distinguent suggestion et affermissement. Recouvrement partiel, la redistribution FLOW n'est pas démontrée comme fonction native unique ici. MS05. | Les décisions sont présentes. Le relais qui transforme le scénario retenu en commandes ou en modifications est encore insuffisamment attribué. Couvrir également diminution/report d'apports devenus excessifs, pas seulement création d'apports. |
| **D05.f Inventory Planning** | Plusieurs plans servent aux simulations, prévisions et stratégies différentes. Appui méthodologique. MS05. | Le regroupement « reconfigurer, simuler, valider » est cohérent. Rendre explicites hypothèses, résultat comparé et scénario retenu. « Planning Optimization » est un produit/moteur, pas l'équivalent de cette capacité. |
| **D07.a Execution Requirements Decision ; D06.e Execution Service Decision** | Les sources de fulfillment et services transport donnent des appuis pour choisir lieu et service. Pas de fonction unique démontrée pour déterminer tous les besoins logistiques et documentaires. MS10, MS08. | Séparer le résultat requis du service choisi est pertinent. Clarifier la frontière : D03 choisit comment honorer l'Order ; D06 décide des prestations et exécutants compatibles avec cette solution. |
| **D06.b Execution Capacity Visibility** | CTP traite une capacité de production ; la configuration de fulfillment comporte des horaires et contraintes. MS04, MS10. | **Pas de preuve d'équivalence** avec un service générique de capacité logistique contextualisée. FLOW porte une responsabilité utile ; préciser plafond, charge, disponible communiqué, unité et fraîcheur avant exploitation. |
| **D07.b Service Order Management ; D06.d Execution Orchestration** | Warehouse-only reçoit des shipment orders ; IOM distingue orchestration et optimisation mobilisée par le parcours. Recouvrement partiel. MS07, MS09. | Bonne séparation entre tenue des demandes et coordination. Les demandes documentaires étendent le périmètre au-delà du seul shipment order. Ne pas importer une dépendance à Dataverse ou à un workflow. |
| **D07.d Execution Tracking ; D07.c Execution Reconciliation ; D06.f Execution Adaptation Decision** | Les retours d'entrepôt et l'orchestration réagissant aux contraintes apportent des appuis ; la trilogie exacte FLOW n'est pas un catalogue natif Microsoft démontré. MS07, MS09. | Trois résultats intelligibles : connaître l'avancement, expliquer les écarts, choisir la variante. Le point faible est le contrat de passage vers D01/D04/D03, plus que l'absence d'une capacité « exception ». |
| **D09.d Party / Role Ingestion ; D11.a Agreement Ingestion ; D08.d Product Reference Ingestion ; D12.a Catalog Ingestion ; D13.a Fulfillment Network Ingestion ; D14.a Execution Service Catalog Ingestion** | Fournisseurs, accords, variantes, lieux et services sont utilisés dans MS11/MS10/MS08. Appui sémantique seulement ; les six ingestions comme capacités et leur maîtrise externe ne sont pas démontrées par ces pages. | La projection externe FLOW est un choix d'architecture métier, pas un manque vis-à-vis d'un ERP qui administre ses données. Auditer réception, validité, rejet et rapprochement d'identifiants ; ne pas ajouter six fonctions d'administration. |

## Manques et écarts à traiter, par priorité

### P1 — Boucle analytique → mise en action

Le modèle dit explicitement que D05 ne lance pas les Orders et que le porteur du déclenchement reste à instruire. Microsoft distingue des suggestions de plan et leur affermissement ; cette séparation étaye le problème, sans dicter son organisation. [MS05](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans)

**Proposition locale :** tester un scénario complet : D05 recommande 200 pièces, le scénario en retient 150 ; une commande d'achat est créée, puis le besoin tombe à 90. Qui met à jour les quantités et dates autorisées ? D04 sait tenir et faire évoluer ces Orders : commencer par expliciter ce relais et les relations. Créer une nouvelle capacité seulement si une responsabilité durable distincte reste sans porteur après cette attribution.

### P1 — Cohérence des stocks représentés

Microsoft documente une réconciliation entre stock ERP et entrepôt ainsi que le risque de compter deux fois des mises à jour. Le sujet complète le comptage physique. [MS07](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-external-erp)

**Proposition locale :** attribuer dans D01 l'explication et le traitement d'un écart entre représentations. Exemple fictif : un entrepôt déclare 100 pièces, FLOW en présente 90, alors qu'une réception de 10 est en transit documentaire. Il faut identifier la cause avant correction. Ne pas rabattre systématiquement ce besoin sur D01.d Stocktaking ni créer une nouvelle capacité avant d'avoir éprouvé D01.f/g/c.

### P1 — Retour et devenir du bien

Le périmètre D04.l laisse déjà plusieurs décisions « à délimiter ». La documentation des retours relie réception, disposition du bien et éventuel remplacement. [MS06](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns)

**Proposition locale :** affecter explicitement la décision de destination/état du retour et la prise en compte de son résultat. Exemple : six pièces reçues, quatre revendables et deux endommagées. D04 tient le retour ; D01 tient le stock qualifié ; l'exécutant rapporte l'inspection. Le choix de disposition reste à attribuer, potentiellement par une décision spécialisée si sa portée le justifie. Avoir financier et contrôle physique ne sont pas absorbés.

### P2 — Entrées de demande, coûts et contraintes

Prévisions et scénarios sont des entrées reconnues dans D05, sans capacité de prévision adoptée. Les sources de fulfillment utilisent des contraintes explicites. [MS05](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans), [MS10](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/fulfillment-returns-optimization)

**Proposition locale :** définir provenance, date de validité et usages des prévisions, coûts, contraintes horaires et paramètres de service. Il s'agit d'abord de **contrats d'entrée manquants**, pas d'un nouveau domaine Demand Planning, de tarification ou de planification de saison. Séparer la qualité attendue de l'information des outils qui la transmettent.

### P2 — Grain des actions et décisions

D04.o présente une ambiguïté de responsabilité : `decision` est défendable pour les autorisations de transition ; une lecture gestion/action convient davantage s’il tient le cycle lui-même. Le nom Management ne tranche pas cette question. La question plus ouverte concerne les trois actions du cycle de promesse face au cycle regroupé des Service Orders. À l'inverse, D05 possède quatre décisions dont les sorties diffèrent réellement ; les éclater selon algorithme, canal, mode de lancement ou interface dégraderait le modèle.

**Règle d'audit proposée :** une décision choisit un résultat métier précis ; un management maintient l'objet et son cycle ; une visibilité restitue un état avec sa fraîcheur ; une orchestration coordonne des prestations. Une action peut contenir plusieurs opérations sans devenir un domaine fourre-tout. Le catalogue Microsoft ne doit pas imposer le nombre de capacités.

### P3 — Mesure de performance

IOM expose des métriques de commande et de fulfillment. [MS09](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview) Cela invite à préciser quels résultats permettent d'apprécier promesses tenues, écarts, disponibilité et immobilisation. La présence de tableaux de bord ne justifie pas automatiquement une capacité Analytics supplémentaire : commencer par les indicateurs et leurs propriétaires dans les domaines existants.

## Relations « a besoin de » à éprouver

Ces lignes sont des **contrats métier candidats**, pas des ordres d'exécution techniques. Le consommateur est à gauche ; les paramètres et événements détaillés restent à définir.

| Consommateur | Fournisseur / résultat requis | Cas qui justifie le besoin |
| --- | --- | --- |
| D03.i ATP | D01.c disponibilité contextualisée ; D02.b protections ; D02.c engagements concurrents | Ne pas promettre deux fois les dernières pièces. Appuis MS01–MS03. |
| D02.c Reservation | D02.b limites applicables et D01.c ressource admissible | Engager une quantité dans le bon périmètre et expliciter sa libération. Appui MS03. |
| D03.a/b/c, selon leur portée | D03.i/j/k/l/m résultats de décision | Distinguer proposition calculée et engagement confirmé ; dépendances locales à expliciter, pas automatisme Microsoft. |
| D02.b Supply Protection | D05.a/d paramètres retenus, avec validité et portée | Une recommandation de quota ne vaut pas mise à jour transactionnelle. |
| D04.j/k/o | D05.e/c/f ajustements retenus et autorisés | Passer de l'optimisation aux achats/transferts/modifications, sans logistique physique dans D05. Appui MS05. |
| D01.f/g ; D04.i–m | D07.d/c faits d'exécution qualifiés | Réception, écart ou correction : actualiser état et reliquat au bon moment sans doublon. Appui MS07. |
| D06.e Execution Service Decision | D14 offre ; D13 réseau ; D06.b capacité communiquée | Choisir un service compatible avec marchandises, lieu et fenêtre. Appuis MS08/MS10. |
| D06.f Execution Adaptation Decision | D07.d faits et estimations ; D07.b prise en charge ; D06.e variantes admissibles | Un retard de préparation conduit à réexaminer une collecte. |
| D03.c Promise Revision | D06.f variante proposée et conséquence sur la promesse | Le changement d'exécutant ne doit pas créer une seconde autorité de promesse. |

Le catalogue publié possède déjà certaines de ces relations, parfois au niveau domaine. Le rapport consolidé doit contrôler leur présence et leur sens exact avant d'en déclarer l'absence. Aucune cardinalité ni passage transactionnel atomique n'est déduit du tableau.

## Qualité des descriptions : ce que la comparaison apporte

L'intérêt de la documentation Microsoft est surtout d'expliquer **une situation, une opération et son effet observable**. Cette forme est plus utile qu'un alignement de noms. Proposition locale de gabarit : résultat métier en une phrase ; entrées et périmètre ; exemple chiffré ; ce qui change et ce qui reste à faire par les autres capacités.

- **Reservation :** expliquer qu'un engagement pour une demande réduit les usages concurrents sans constituer une sortie physique. Montrer annulation partielle et consommation, sans confondre engagement de stock et affectation de ressource. Appui MS03.
- **Execution Capacity Visibility :** indiquer explicitement « plafond de 1 000 préparations », puis distinguer une charge annoncée de 800 d'un disponible de 200 qui ne peut être déduit sans règle. Le modèle contient déjà cet exemple : le rendre accessible dans la définition courte, sans ajouter une capacité de calcul.
- **Supply Protection :** montrer un quota B2B de 300 sur 1 000 pièces et sa validité ; expliquer qui propose ce quota, qui l'applique et quelles demandes peuvent le consommer. Appui partiel MS02 ; les chiffres sont une illustration FLOW.
- **Order Lifecycle Management :** garder le cas 60 autorisées/40 en attente ; expliciter que reporter les 40 ne lève pas le blocage. Ce contenu concret est déjà présent et constitue un bon standard éditorial.

Corriger également les mentions textuelles de « D07 » comme domaine d'exécution dans plusieurs périmètres D04/D05 : v007 l'a retiré comme domaine, même si des identifiants D07.x restent légitimes. Il s'agit d'une obsolescence interne, pas d'un écart au marché.

## Sources officielles consultées

Consultation commune : **16 septembre 2026**. Documentation publique Microsoft Learn évolutive, sans version documentaire figée sauf indication. Les identifiants MS sont locaux à cet audit ; aucun identifiant de capacité natif Microsoft n'est inventé. Résumés et localisateurs seulement, sans reprise intégrale. Les bannières génériques « authorization required » n'ont pas empêché la lecture des passages cités. Les dates ci-dessous sont celles affichées lors de l'ouverture, qui peuvent différer du cache de recherche.

| Clé | Source / édition et date affichée | Passages réellement consultés ; limite |
| --- | --- | --- |
| MS01 | [Inventory Visibility Add-in overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility), 2025-08-14 ; version générale non précisée | Vue globale, ajustements, ATP, états et dimensions. La section historique WMS évoquant une future vague 2022 n'est pas utilisée pour une promesse actuelle de compatibilité. |
| MS02 | [Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), 2025-08-13 ; UI v1/v2 décrites | Business background ; virtual pool ; différence allocation/réservation ; réallocation. Fonction produit, pas décision d'optimisation attestée. |
| MS03 | [Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), 2026-07-27 ; réservations depuis ventes à partir de SCM 10.0.33 | Cas multicanal ; réservation, offset, annulation. Ne pas généraliser une configuration technique à tous les engagements FLOW. |
| MS04 | [Calculate sales order delivery dates using CTP](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp), 2026-07-27 ; Near real-time CTP ≥ 10.0.41 | Comparaison ATP/CTP ; capacité/délais ; méthodes de contrôle ; dates confirmées. Capacité de production, pas preuve de capacité logistique restante. |
| MS05 | [Master plans overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans), 2026-03-25 ; page évolutive | Simulations ; coverage/freeze/firming/forecast/capacity/action messages ; dates et quantités. Plusieurs mécanismes produit ; pas équivalence avec les cinq capacités D05. |
| MS06 | [Sales returns](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns), 2026-04-20 ; version non précisée | Motifs ; disposition ; retour/remplacement ; réception. Les effets financiers documentés restent hors comparaison fonctionnelle FLOW. |
| MS07 | [Warehouse management only mode with external ERP systems](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-external-erp), 2026-05-22 ; version non précisée | Inbound/outbound ; résultats et événements ; on-hand reconciliation ; update logs. Cas d'intégration, pas preuve du SI C-Log. |
| MS08 | [Set up shipping carriers](https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/tasks/set-up-shipping-carriers), 2025-08-05 ; version non précisée | Services, contraintes de charge, tender manuel/EDI, tarification et transit. Appui transport seulement ; pas catalogue universel de prestations. |
| MS09 | [Intelligent Order Management overview](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview), 2026-01-30 ; version non précisée | Components ; orchestration ; providers ; optimization ; insights. Composants logiciels et principe de coopération, pas catalogue métier natif. |
| MS10 | [Fulfillment and Returns Optimization provider overview](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/fulfillment-returns-optimization), 2026-01-28 ; version non précisée | Sources ; contraintes ; strategies ; fulfillment plans. Pas d'équivalence établie avec les décisions d'optimisation du stock D05. |
| MS11 | [Create purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-creation), 2025-08-13 ; version non précisée | Origines des achats ; types ; lignes ; actions et retards. Ne démontre pas tout le catalogue des ventes et transferts. |
| MS12 | [Dynamics 365 Intelligent Order Management — Lifecycle](https://learn.microsoft.com/en-us/lifecycle/products/dynamics-365-intelligent-order-management), état consulté sans date de mise à jour affichée | Support Dates : Modern Lifecycle, début 2021-08-01, In Support. Pas de calendrier futur déduit. |

## Limites et suites

Le contrôle est une confrontation documentée des responsabilités, pas une étude de choix logiciel ni un test d'exécution des produits. PTP, priorisation détaillée et projection des six référentiels restent seulement partiellement rapprochés. La granularité exacte des opérations physiques n'est volontairement pas importée dans FLOW.

Les recommandations sont à croiser avec SAP/Oracle/TM Forum et l'audit interne des relations. Elles ne doivent pas recevoir un statut adopté depuis leur seule présence dans ce document.

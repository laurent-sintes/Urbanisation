# Atlas — rendre les choix et les exemples lisibles

19 septembre 2026 · U462.

L’interface dispose d’un onglet **Marché & choix** et d’une rubrique **Exemples concrets** près de la définition. Le backlog explicite dix choix de vocabulaire/définition et conserve quatorze exemples structurés sur neuf fiches. Les exemples plus anciens, déjà présents dans les périmètres, deviennent également visibles.

## Ce qui est visible après rechargement

- **Marché & choix**, à côté de Carte, Fiche et Relations : position FLOW et lien primaire daté directement visibles. Les points communs, différences, passages consultés et limites de la preuve se déplient. Les explications du terme et de la définition passent en tête lorsqu’elles sont documentées.
- **Exemples concrets**, après la définition : les passages explicitement signalés comme exemples dans la publication sont mis en valeur. Les formats historiques « Exemple discuté », « Exemple métier fictif » et « Exemple illustratif FLOW » sont reconnus. Aucune illustration n’est fabriquée depuis la définition.
- Sources du glossaire également accessibles sans double dépliage ; recherche étendue aux exemples et aux raisons de vocabulaire. Navigation clavier, lien partageable et anciennes ancres marché conservés.

Les statuts de revue et sources internes restent privés. Les liens externes concernent les références de comparaison, sans devenir un catalogue de solutions. Une absence de comparaison reste affichée comme non documentée, sans qualification automatique d’innovation ou de standardisation.

## Contenu renforcé dans le backlog

Les dix fiches concernées par les raisons lexicales sont Fulfillment Optimization, Order Promising, Fulfillment Commitment, Supply Assignment, Reservation, Order Structuring, Inventory Target Decision, Purchase Order, Product Reference et Product Reference Ingestion.

Les choix sont expliqués concrètement : pourquoi Backlog ne suffit pas à nommer un domaine ; pourquoi Commitment précise le résultat attendu ; pourquoi Split est trop étroit lorsque regroupement et fusion sont aussi couverts ; pourquoi Assignment est préféré à Allocation sans complément ; pourquoi une projection ne porte pas l’administration du maître.

Trois rapprochements sourcés sont ajoutés :

- **Fulfillment Commitment / Microsoft Confirm sales orders** : la confirmation documentaire éclaire l’alternative Order Confirmation, sans couvrir à elle seule proposition et révision de satisfaction. [Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/tasks/confirm-sales-orders).
- **Supply Assignment / SAP ARun** : vocabulaire repris, effet différent. Le scénario SAP décrit un lien qui empêche l’usage par une autre demande ; FLOW attribue cet effet à Reservation selon U436. Cette différence est désormais explicite. [Source primaire, Supply Assignment Scenarios](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4).
- **Purchase Order / Microsoft** : appui au terme d’achat de biens ou services ; distinction entre document et capacité métier FLOW. [Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-overview).

Les raisons ajoutées aux autres fiches s’appuient sur les décisions déjà enregistrées, les comparaisons existantes et les passages relus : [Microsoft DOM](https://learn.microsoft.com/en-us/dynamics365/commerce/dom), [Order promising](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations), [minimums de stock](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-journal), [réservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations) et [Oracle Split Order Line](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/fulfillment-line-splits.html). Les appuis Product Reference conservent leur provenance U460. Aucun consensus lexical complet ni nouvelle validation métier déduits.

## Exemples repris

Quatorze illustrations structurées sont portées par neuf fiches :

- **Order Lifecycle Management** : 100 pièces fermes, 60 libérées, révision de l’échéance demandée des 40 restantes sans effacer la version applicable.
- **Fulfillment Commitment** : demander 100 vendredi, proposer 60 vendredi et 40 lundi ; changer de ressource sans changer la promesse.
- **Supply Assignment** : 150 disponibles face à des demandes de 100 et 200 ; le prorata illustratif 50/100 n’est ni une scission ni une politique universelle. Affecter 40 ne les réserve pas.
- **Reservation** : engager 40 pièces avant d’affecter un lot précis.
- **Purchase Order** : 60 reçues sur 100 ; réponse fournisseur en deux échéances et distinction avec notre promesse client.
- **Order Structuring** : scinder 100 en 60/40 ; regrouper deux transferts en conservant leurs identités ; fusionner deux achats compatibles de 30 et 20.
- **Inventory Target Decision** : comparer où porter la sécurité entre entrepôt et magasins.
- **Product Reference et son ingestion** : une variante dans plusieurs catalogues et plusieurs exemplaires physiques ; réception d’une variante avant sa mise au catalogue.

Chaque exemple conserve ses références internes. Ils sont pédagogiques et ne deviennent ni règles universelles ni preuves d’un fonctionnement installé. Les formulations issues des dossiers de discussion restent proposées selon leur portée réelle d’accord.

## Couverture et lacunes restantes

Comptage du contenu directement porté par chaque élément, sans héritage automatique de son parent :

| Niveau | Exemples visibles dans v010 | Exemples dans le backlog | Marché dans v010 | Marché dans le backlog |
| --- | --- | --- | --- | --- |
| Capacités | 46/47 | **47/47** | 39/47 | **40/47** |
| Comportements | 73/76 | 73/76 | 63/76 | 63/76 |
| Domaines | 4/6 | 4/6 | 3/6 | 3/6 |
| Référentiels | 1/6 | 2/6 | 1/6 | 2/6 |

Les dix explications dédiées de terme et définition concernent sept capacités, deux domaines et un référentiel. Les autres comparaisons conservent leurs positions FLOW existantes ; leur présence ne signifie pas que tous les arbitrages lexicaux sont expliqués au même niveau de détail.

Sept capacités restent sans rapprochement marché propre : Service Requirements Decision, Service Reconciliation, Party / Role Ingestion, Agreement Ingestion, Catalog Ingestion, Fulfillment Network Ingestion et Service Catalog Ingestion. Leur étude demande des sources correspondant réellement à leur responsabilité, sans transformer l’import d’un produit en capacité par simple analogie.

Trois comportements ATP restent sans exemple explicite : Existing Commitment Consideration, Network Stock Availability et Future Supply Projection. Order Management et Inventory Management restent à illustrer au niveau du domaine. Party / Role, Catalog, Agreement et Fulfillment Network restent à illustrer et à comparer au niveau du référentiel. Les treize comportements sans comparaison propre et toutes les lacunes sont recensés dans la [preuve navigateur](browser/2026-09-19T10-06-49-336Z/verification.json). Ce relevé de contenu ne rouvre pas l’audit des comportements U431.

## Contrôles et publication

**77 tests frontend et 15 tests Python réussis**, validation du modèle sans erreur et compilation réussie. Restitution backlog actualisée avec les explications et exemples structurés. Contrôles navigateur sur la publication réelle, une publication historique et une fixture isolée du futur contenu : sources, clavier, recherche, 390 px et surface de 720 px équivalente à un repli à 200 %. Cette dernière vérification ne constitue pas une certification d’accessibilité complète.

Les 142 nœuds, 346 relations, définitions, rattachements, états de revue et empreintes d’accord sont préservés. Seuls les champs exemples et comparaisons de onze fiches changent ; le glossaire est intact. **303 fichiers historiques et de publication vérifiés identiques.** [Contrôle de données](verification.json).

La présentation fonctionne déjà avec v010. **Les dix nouvelles explications et quatorze exemples structurés attendent une nouvelle release** ; aucun contenu backlog ne complète silencieusement la publication. Pas de release, commit, push ou opération serveur dans cette intervention.

Captures : [exemples publiés](browser/2026-09-19T10-06-49-336Z/published-examples.png), [marché sur mobile](browser/2026-09-19T10-06-49-336Z/mobile-market.png), [explication de vocabulaire en fixture](browser/2026-09-19T10-06-49-336Z/fixture-terminology.png).

# Inventory Optimization — TM Forum, Microsoft et SAP

Étude U222 du 15 septembre 2026, par Codex. TM est interprété comme TM Forum dans la continuité des échanges. Comparaison du backlog après U219–U221, et non de la release v005. Les correspondances et pistes ci-dessous restent proposées ; aucune capacité ni définition du modèle n'est modifiée par cette étude.

## Conclusion pour D05

Le nom Inventory Optimization est cohérent avec la finalité choisie : décider du stock souhaitable et des ajustements nécessaires. Pour le rendre concret, il faut expliciter **quel compromis est recherché**, puis distinguer le besoin calculé de la décision de réapprovisionnement. Le premier peut être de 50 unités ; la seconde tient compte des lots, dates, capacités de réception et demandes déjà lancées.

L'apport SAP est particulièrement précis sur les objectifs de stock et les arbitrages ; Microsoft fournit des exemples lisibles de règles de couverture et de réapprovisionnement. Le corpus public TM Forum apporte surtout un vocabulaire d'information et d'interfaces. Il ne suffit pas à établir une équivalence de domaine. Ce constat ne prétend pas auditer tous les catalogues de capacités des trois organismes.

## Éléments effectivement consultés

| Élément externe | Constat reformulé | Source et portée |
| --- | --- | --- |
| ELM115 — TMF687, Product Stock et opérations associées | Le stock porte quantités présente, minimum, maximum et seuil de réapprovisionnement. Consultation, ajustement et réservation figurent parmi les opérations. La présence d'un seuil n'explique pas comment l'optimiser. | S1, résumé public du guide ; modèle d'API, pas catalogue de capacités. |
| ELM116 — TMFC032 Supply Chain Management | Composant ODA couvrant notamment planification, approvisionnement, inventaires, production et logistique. Sa spécification est affichée Planned dans la page indexée. | S2 ; composant plus large, sans détail démontrant notre D05. |
| ELM117 — Coverage settings | Dynamics 365 configure des méthodes par besoin, période ou min/max ; la couverture peut produire des ordres planifiés d'achat, transfert ou production. Le mode Priority utilise des seuils et priorités de réapprovisionnement. | S3 ; fonctions de planification du produit, non rangs de capacités métier. |
| ELM118 — DDMRP | Positionner les buffers, déterminer leurs niveaux, les ajuster, planifier les apports et suivre l'exécution sont distingués. La méthode s'applique aussi à la distribution et au retail. | S4 ; étapes méthodologiques, pas cinq capacités à recopier. |
| ELM119 — Inventory Optimization | SAP IBP recommande des objectifs de stock, localement et à plusieurs échelons, selon coûts, service et incertitudes. Il expose aussi composants du stock, quantité économique, niveau de service cible et budget. | S5 ; fonctions IBP 2605. |
| ELM120 — Replenishment Planning / Forecasting and Replenishment | Le cours SAP Retail distingue calcul des besoins, optimisation des quantités et propositions d'ordres. Dans F&R, les propositions sans exception peuvent être libérées et transférées automatiquement ; les exceptions appellent un traitement humain. | S6 ; plusieurs solutions SAP sont présentées séparément, ces fonctions ne sont pas toutes attribuées à IBP. |
| ELM121 — Warehouse replenishment | Le réapprovisionnement Microsoft peut aussi désigner du travail interne à l'entrepôt, notamment pour les emplacements de picking. | S7 ; exécution WMS à distinguer de notre décision de stock. |

## Correspondances avec le backlog

État de référence : [empreintes de lecture](etudes/2026-09-15-inventory-optimization/verification.yaml). Auteur Codex, 2026-09-15 ; toutes les correspondances sont proposées, sans valideur ni date de validation. Aucun déploiement Beaumanoir ou FLOW n'a été évalué.

| Correspondance | Cible locale | Relation et justification | Limite / adaptation proposée |
| --- | --- | --- | --- |
| CMP067 | D05 Inventory Optimization | Recouvrement partiel avec ELM119 ; appui méthodologique ELM118 et fonctionnel ELM120. | Notre périmètre inclut des décisions opérationnelles de réapprovisionnement et redistribution ; il déborde donc les seuls objectifs de stock d'IBP Inventory Optimization. TMFC032 est trop large pour établir une équivalence. |
| CMP068 | D05.a Coverage Target Decision | Recouvrement partiel ELM119 ; appui méthodologique ELM118 ; appui sémantique ELM115. | Préciser service attendu, coût, incertitude, horizon et maille. Des minimums saisis ne démontrent pas une optimisation de ces valeurs. Leur révision dynamique peut enrichir la capacité existante. |
| CMP069 | D05.b Net Requirements Calculation | Recouvrement partiel ELM117 et ELM120 : calcul du manque avant proposition d'apport. | Les fonctions externes dépassent ce calcul. Vérifier stocks admissibles, entrées attendues, demandes en cours et absence de double comptage ; ne pas importer un algorithme MRP complet. |
| CMP070 | D05.c Stock Redistribution Decision | Appui partiel ELM118 pour les apports par transfert ; voisinage avec le positionnement des objectifs ELM119. | Une cible multi-échelon ou un ordre de transfert ne prouve pas une décision de redistribution d'excédents existants. Équivalence détaillée non établie ; conserver ce point à instruire. |
| CMP071 | Périmètre envisagé U221, sans nouveau nœud | Recouvrement fonctionnel partiel ELM117/ELM120, appui méthodologique ELM118. | Examiner Replenishment Decision comme aptitude à décider quantité, date et déclenchement. Automatique décrit un mode, pas la raison de créer une capacité. ELM121 rappelle la frontière avec l'exécution. |

## Piste de décomposition locale, à discuter

Je conserverais les trois capacités actuelles et examinerais une quatrième, **Replenishment Decision**, en définissant des résultats distincts :

1. **Coverage Target Decision** : quel stock viser, où, sur quel horizon et selon quel compromis ? La politique et la révision des paramètres peuvent rester dans cette capacité tant qu'un résultat distinct ne justifie pas de séparation.
2. **Net Requirements Calculation** : quel manque ou excédent subsiste après prise en compte des ressources et besoins pertinents ?
3. **Replenishment Decision**, candidate : quelle quantité demander, pour quand, et quand déclencher ou réviser la demande ? Une décision peut être automatique, soumise à validation ou traitée par exception.
4. **Stock Redistribution Decision** : comment rééquilibrer le stock déjà présent entre lieux ? L'articulation avec Replenishment Decision devra éviter deux décisions concurrentes pour un même transfert.

Il reste possible de garder trois capacités en absorbant une partie du calcul net dans Replenishment Decision. Cette étude ne tranche pas cette granularité. Le besoin net mérite une capacité autonome s'il possède une utilité et un résultat réutilisables, indépendants d'un seul enchaînement de traitement.

L'évaluation des résultats — ruptures, surstocks, immobilisation, respect des objectifs — serait d'abord un aspect transversal à préciser. Je ne créerais pas automatiquement une capacité de plus pour chaque indicateur, règle ou algorithme.

## Exemple fictif : d'une cible au déclenchement

Une variante dans un magasin a une cible de 100 unités, 30 présentes et 20 attendues à temps. En supposant toutes ces quantités admissibles, aucune autre demande à déduire et aucune restriction, le complément net est de 50.

- La cible 100 doit avoir une justification : service attendu, demande prévisionnelle, délai, risque, coût. « Optimiser » peut conduire à la réviser.
- Le besoin net 50 ne décide pas de commander 50 aujourd'hui : un lot de 12 pourrait conduire à proposer 60, sous réserve des autres contraintes.
- Un surplus ailleurs peut justifier une redistribution. Il faut coordonner cette décision et le réapprovisionnement pour éviter de couvrir deux fois le même manque.
- Une demande ou un Order déjà en cours doit être pris en compte avant un nouveau déclenchement automatique.

Dans notre modèle, D05 cherche le bon stock ; D04 gère les Orders correspondants ; D03 décide comment les satisfaire ; les exécutants réalisent les prestations ; D01 tient la représentation du stock et ses protections/réservations. C'est une proposition d'articulation, pas un processus obligatoire ou un partage de moteurs logiciels imposé. La prévision peut être une entrée sans ajouter la planification de saison au périmètre actuel.

## Sources, versions et limites d'accès

Consultation : 2026-09-15. Sources officielles seulement, synthèses courtes et liens ; aucun catalogue propriétaire ou document membre reproduit. Conditions Microsoft/SAP de redistribution intégrale non examinées. Les formulations françaises sont nos reformulations, pas des traductions officielles de capacités.

| Source | Référence, édition et localisateur | Accès réel et limites |
| --- | --- | --- |
| S1 | MKT19 — [TMF687 Stock Management API User Guide v4.0.0](https://www.tmforum.org/resources/specification/tmf687-stock-management-api-user-guide-v4-0-0/), résumé Product Stock / opérations ; approuvé 18 janvier 2021 | Résumé public lu dans le résultat indexé ; ouverture directe 403. Guide complet non consulté. Notice RAND ; ne pas confondre avec la licence d'autres artefacts d'API. |
| S2 | MKT19 — [TMFC032 Supply Chain Management](https://www.tmforum.org/oda/directory/components-map/production/TMFC032), description et Component specification status | Texte indexé lu ; ouverture directe 403. Version et date de publication non renseignées ; pas de spécification détaillée examinée. |
| S3 | MKT14 — [Coverage settings](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/coverage-settings), Coverage codes, mise à jour 25 mars 2026 | Corps de documentation lu ; page évolutive Dynamics 365 SCM. |
| S4 | MKT14 — [DDMRP overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/ddmrp-overview), The five components, mise à jour 25 mars 2026 | Corps de documentation lu ; aucune equivalence entre étapes de méthode et capacités locales. |
| S5 | MKT24 — [SAP IBP Inventory Optimization](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/252c83bbf8184915a56d4cdd0917ef06/cdbbdf46dc8d4212b97d0255f0af93a9.html), Business Background et Key Features, version 2605 | Texte indexé des sections lu ; ouverture directe sans corps exploitable. Pas d'accès à un catalogue RBA de capacités. |
| S6 | MKT13 — [Running Replenishment Planning](https://learning.sap.com/courses/discovering-retail-functions-and-business-processes-in-sap-s-4hana-retail/running-replenishment-planning_e456b0ed-3094-4056-9ba8-aa56cf6833ed), SAP Forecasting and Replenishment Solutions for Retail | Cours public lu, édition logicielle unique non indiquée. Il juxtapose plusieurs solutions et des informations historiques ; aucune annonce de roadmap Q1 2023 utilisée comme état actuel de Predictive Replenishment. |
| S7 | MKT14 — [Replenishment overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/replenishment), méthodes de réapprovisionnement WMS, mise à jour 20 novembre 2025 | Documentation publique consultée ; ne démontre aucune réalisation logistique FLOW. |

Les limites d'accès empêchent de prétendre à une comparaison exhaustive. Elles n'empêchent pas les rapprochements ciblés ci-dessus. D01 et D03 ne font pas l'objet d'un nouvel audit de leurs capacités dans cette étude. La release v005 et Atlas restent inchangés.


## Clarification locale U224, après l'étude

Laurent précise Inventory Optimization comme domaine analytique, distinct de l'application des paramètres et du déclenchement des Orders. La candidate Replenishment Decision présentée ci-dessus n'est donc pas retenue telle quelle comme capacité D05 combinant calcul et déclenchement. Les propositions analytiques et leur statut figurent dans modeles/backlog/stock-order-boundary.yaml, analytics_execution_boundary_U224. Les correspondances U222 gardent leur état daté : elles ne démontrent pas la couverture des nouvelles formulations proposées. Aucune nouvelle consultation externe dans cette clarification.

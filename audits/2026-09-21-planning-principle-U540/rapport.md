# Audit du principe Planning — U537 à U541

Le principe tient dans le modèle : **le Planning porte l’application de son plan ; les décisions et la configuration qu’il consomme restent distinctes.** Cela ne transforme pas toute capacité sollicitée en comportement du Planning.

La revue porte sur 58 capacités, 82 comportements et la structure de 369 relations. Toutes les définitions ont été examinées ; les scopes et sources ont été approfondis sur les frontières concernées. [Matrice et preuves](../../modeles/backlog/planning-principle-audit-U540.yaml). Aucun rejeu de l’audit historique U431, aucune affirmation de réalisation installée.

## Changement intégré

**Order Backlog Planning → Supply Assignment.** L’affectation devient un comportement terminal du planning opérationnel du carnet. Son identifiant D02.e et ses liens métier sont conservés. Les mécanismes historiques d’application, complément en préservant l’existant et réaffectation sont réunis comme modalités descriptives : pas de sous-comportements. BHV045–047 et leurs anciens rattachements restent intégralement conservés dans la [baseline](baseline.yaml), avec succession explicite.

Ce rattachement est l’interprétation contextuelle de la réponse U541 à la question sur le parent ; le niveau comportement est demandé en U539. Les formulations détaillées ne sont pas adoptées par extension.

## Où le principe s’applique

| Périmètre | Conclusion |
| --- | --- |
| Order Backlog Planning | Porte l’application des affectations via Supply Assignment. |
| Inventory Planning | Porte l’application de son scénario ; les protections et les Orders mobilisés gardent leur responsable. Décomposition précise encore à compléter. |
| Demand Planning | Rendre la demande retenue applicable aux consommateurs est à décrire ; ce n’est pas créer les ventes futures ni modifier les commandes connues. |
| Capacité de couverture actuellement nommée Supply Planning | Porter la mise en œuvre des apports retenus, sans absorber Purchase Order ou leur réalisation. Le nom et la largeur restent ouverts. |
| Supply Protection et référentiels | Restent extérieurs : fournissent et maintiennent politiques, paramètres et références consommés. |
| Reservation, Fulfillment Commitment, Orders, consignation | Restent des capacités partenaires : leurs engagements ou responsabilités durables ne se réduisent pas à appliquer un plan. |
| Process Orchestration | Reste une capacité de coordination continue, avec dépendances, attentes et impondérables ; aucune nouvelle capacité Process Planning par analogie. |

## Points à poursuivre

1. **Supply Planning est trop englobant pour nommer sans ambiguïté le seul plan de couverture.** Conserver Planning comme Area et Order Backlog Planning comme capacité claire. Définir le résultat propre de D17.b avant son nom ; ne pas lui transférer les affectations sous prétexte du mot Supply.
2. **Order Backlog Optimization Request et Planning :** les scopes distinguent la demande et le travail de planification, mais Simulation & Analysis et Plan Activation Follow-up peuvent laisser lire un doublon. Clarifier la responsabilité de demande et de suivi ; aucun retrait automatique des comportements U501.
3. **Inventory Rebalancing / Stock Consolidation :** les verbes courts Déplacer et Regrouper suggèrent une exécution, alors que les scopes décrivent des décisions de transfert. Correction éditoriale recommandée, sans déplacement de responsabilité.
4. **Application des autres plans :** préciser leur résultat applicable à la maille capacité avant une décomposition détaillée. Pas de comportement générique ajouté partout.

## Appuis marché et limites

Oracle inclut la mise en application dans le parcours du [backlog](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faubm/overview-of-backlog-management-processes.html), distingue la [release des recommandations](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faupc/manually-release-plan-recommendations.html) et les [règles de protection utilisées par le calcul](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faubm/overview-of-supply-allocation-rules.html). SAP documente [Supply Assignment](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4), avec un périmètre plus large que l’affectation FLOW, notamment sur les usages concurrents.

[Microsoft Reservation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations) étaye l’effet propre de la réservation ; [Oracle Order Management](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/order-management-statuses.html) les états persistants des Orders ; [Camunda](https://camunda.com/process-orchestration/) la coordination continue. Ces sources soutiennent les distinctions fonctionnelles. La hiérarchie Capability → Behavior reste une convention FLOW, pas un consensus éditeur ni une innovation revendiquée.

Les fiches modifiées portent leurs comparaisons marché ; les recommandations ouvertes restent dans l’audit. Aucun changement de publication Atlas.

## Vérification

Modèle validé sans erreur ; 23 tests existants sur les comparaisons marché et les références d’information réussis. Restitution backlog générée. Les 16 décisions, Supply Protection, D17.b et tous les liens métier sont préservés. Deux rôles du catalogue Informations interne ont été alignés sur la capacité parente, sans ajout d’information ni changement de visibilité.


**Approfondissement du premier point — U542 :** [propositions d’application par Planning](../../modeles/backlog/planning-application-options-U542.yaml). Demand Planning rend une demande applicable, Inventory Planning met en effet les actions du scénario de stock, le plan de couverture porte les apports retenus à engager/réviser. Capacités partenaires extérieures ; frontière stock/couverture à préciser pour éviter une double application. Noms candidats et décompositions proposés, sans modification du catalogue.


**Réorientation U543 :** Laurent remet en cause Inventory Planning comme agrégat. [Étude par intentions](../../modeles/backlog/inventory-planning-intentions-U543.yaml) : réassort, rééquilibrage, implantation ; consolidation à éprouver. Cette direction remplace la poursuite d’un comportement générique Inventory Plan Application sous D05.f. Les capacités candidates, leurs parents et leurs comportements restent proposés.


**Alternative U544 :** [Inventory Optimization Planning](../../modeles/backlog/inventory-optimization-planning-option-U544.yaml) explicite un compromis commun entre service, stock immobilisé, coûts et risques. Option à privilégier si un plan arbitre réellement entre les ajustements ; scission U543 à réserver à des plans autonomes. Aucun renommage ou changement structurel adopté.


**Accord U545 :** Inventory Optimization Planning est intégré dans D05.f avec le nom et la définition présentés. La scission par levier U543 n’est pas retenue dans ce changement. Le principe de plan et d’application est cadré pour le stock ; le comportement détaillé et les propositions d’application de Demand Planning / couverture restent ouverts. Les mentions antérieures du rapport sont historiques.


**Deuxième point, approfondissement U546 :** [frontière demande / Planning](../../modeles/backlog/backlog-request-planning-boundary-U546.yaml). Les scopes distinguent déjà les responsabilités ; certaines définitions courtes prêtent à confusion. Clarification proposée pour conserver le cadrage et le suivi dans la demande, l’étude et l’application dans Planning. L’accord U501 est préservé ; aucun déplacement ou retrait intégré.


**Option U547 :** [gestion de demande comme premier comportement de Planning](../../modeles/backlog/planning-request-behavior-option-U547.yaml). La demande d’optimisation reste suivie comme les Orders ; son traitement peut relever du Planning. Cette option est désormais préférée au maintien systématique de deux capacités proposé U546. La redistribution des mécanismes U501 reste à adopter ; aucune migration appliquée.


**Point suivant — U550 :** [Clarification des décisions de redistribution](../../modeles/backlog/stock-redistribution-wording-U550.yaml). Définitions courtes de BHV024/025 proposées avec « Déterminer » ; noms et parents préservés. Les variantes homonymes de Transfer Order portent les Orders, pas le calcul. Oracle/Nextail reconsultés, CMP228 ; aucune modification canonique.


**Accord U551 :** définitions proposées de BHV024 Inventory Rebalancing et BHV025 Stock Consolidation intégrées. Le troisième point est résolu : les décisions sont lisibles dès leur définition courte. Noms, parents et périmètres conservés ; aucune adoption de la migration Request ou des autres applications de Planning par extension.


**Refacto U552 :** [résultat et limites](../2026-09-21-planning-refactor-U552/rapport.md). Gestion de demande, étude, autorisation et affectation réunies comme comportements de Order Backlog Planning ; application stock et publication de demande explicitées. Principes appliqués ; D17.b retirée U555 car le planning amont est déjà pris en charge, Supply Planning devient le nom de l’Area U553. Frontières métier explicitées U556 ; aucune validation globale ni publication déduite.

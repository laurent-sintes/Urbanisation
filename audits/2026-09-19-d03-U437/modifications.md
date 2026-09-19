# Modifications D03, Structuring et Fulfillment Commitment — U437 à U447

Les choix de structure U438 et de nom U445 sont appliqués dans le backlog. **Les six domaines sont frères sous Supply** : aucun domaine ne contient un autre domaine. Le modèle conserve 47 capacités et comporte désormais 76 comportements, dont deux nouveaux proposés.

## Ordre de lecture appliqué — U447

1. **Business References** : Product Reference, Party / Role, Catalog, Agreement, Fulfillment Network, Service Catalog.
2. **Order Management** : les demandes, leur contenu, leur structure et leur cycle de vie.
3. **Inventory Management** : les ressources, faits de stock, protections et réservations.
4. **Process Management** : les prestations et leur réalisation.
5. **Order Promising** : les possibilités et engagements de satisfaction.
6. **Fulfillment Optimization** : les arbitrages et plans de satisfaction des commandes.
7. **Inventory Optimization** : les objectifs et ajustements de stock.

Business References reste un groupe de présentation ; les six éléments suivants sont les domaines frères. L’ordre des relations de présentation et celui des nœuds de la restitution sont alignés. Aucun contenu d’élément ni de relation n’est modifié par cette permutation. C’est un ordre de lecture, pas une séquence d’exécution. [Convention structurée de présentation](../../modeles/backlog/reading-order-U447.yaml). Atlas conserve la publication courante ; cet ordre y sera repris lors d’une prochaine release demandée.

## Répartition adoptée

| Domaine | Capacités après modification |
| --- | --- |
| **D03 Fulfillment Optimization** | Order Prioritization, Fulfillment Plan Decision, Order Backlog Planning, Supply Assignment |
| **D15 Order Promising** | ATP, CTP, PTP, Delivery Schedule Decision, Fulfillment Commitment |
| **D04 Order Management** | Ses sept capacités antérieures, plus Order Structuring et Order Archiving |

Inventory Management, Inventory Optimization et Process Management restent les trois autres domaines. Les identifiants des capacités sont conservés : par exemple D03.n appartient désormais à D15. Les relations explicites déterminent les parents ; les préfixes historiques ne forment pas une hiérarchie.

## Changements opérés

- Nom D03 et répartition des onze capacités appliqués selon U438 ; D15 créé avec un identifiant auparavant inutilisé. Sept relations de rattachement changent de domaine ; les comportements existants gardent tous leur capacité parente.
- **Fulfillment Commitment** remplace Promise Management sur la même capacité D03.n, selon U445. La formulation proposée est : « Proposer, confirmer et réviser les engagements de satisfaction d’une commande, en quantités, dates et conditions. » Les noms des trois comportements existants sont conservés.
- Distinction entre engagement et affectation rendue explicite : changer d’arrivage peut préserver la promesse ; un retard de transport peut faire réviser sa date sans changer les ressources affectées. L’affectation concrétise les choix ; elle ne porte plus une seconde optimisation dans sa définition. La réservation conserve seule le blocage concurrent (U436).
- **Order Structuring** reçoit une définition plus concrète, proposée : « Scinder, regrouper ou fusionner des commandes et leurs éléments, en préservant la traçabilité des demandes, les quantités et les engagements. » Son ancienne définition et son accord sont conservés dans la capture préalable ; l’ancienne validation n’est pas transférée à la nouvelle rédaction.
- **Order Grouping — BHV086** est proposé pour relier des demandes qui restent distinctes. **Order Merging — BHV087** est proposé pour remplacer des demandes compatibles par une demande résultante. Ils sont frères de Split sous Structuring, sans sous-comportement ni nouvel objet imposé.
- Deux relations métier explicitement consacrées à la promesse sont réorientées de D03 vers D15 ; les liens entre capacités restent conservés. Les descriptions, principes, glossaires et conventions sont actualisés sur les nouvelles frontières. La restitution backlog est régénérée.

## Appuis et limites du marché

SAP documente la réévaluation des confirmations dans Order Promising ; Microsoft distingue optimisation de fulfillment et calculs de promesse. Ces périmètres logiciels étayent la lecture, sans imposer la partition FLOW. Les rapprochements sont visibles dans les fiches et dans [l’annexe de structuration](../../modeles/backlog/d03-domain-review-U437.yaml).

Pour les nouveaux comportements, Oracle documente des ensembles de lignes **dans une même commande** ; SAP apporte le regroupement de besoins pour calcul et contrôle, sans prouver un ensemble transactionnel permanent multi-commandes. La portée persistante de Grouping reste donc une proposition FLOW. Infor documente une véritable fusion de commandes d’achat avant approbation ; elle ne démontre pas une fusion universelle de tout type d’Order. Les sources, éditions, passages consultés et correspondances ELM256–258 / CMP167–168 sont consignés dans [la revue Structuring](../../modeles/backlog/order-structuring-review-U439.yaml).

Fulfillment Commitment est un choix lexical FLOW accepté par Laurent, sans consensus marché revendiqué. Order Confirmation a été écarté comme recommandation en raison de son ambiguïté avec la confirmation documentaire. [Étude de la frontière et du nom](../../modeles/backlog/promise-assignment-review-U441.yaml).

## Ce qui reste à préciser

- Autorité respective de PTP, Delivery Schedule Decision et Fulfillment Plan Decision sur le compromis final ; la scission ne résout pas ce contrat à elle seule.
- Types et états de commandes compatibles avec Grouping et Merging, droits de modification, quantités déjà réalisées et traitement des engagements, affectations et réservations.
- Conditions détaillées de confirmation et de révision d’un engagement de satisfaction.

Les questions complexes déjà ouvertes dans l’audit V0 restent tracées, dont le devenir des invendus consignés. Aucune couverture installée Beaumanoir n’est déduite de ces modifications.

## Vérifications

- Validation du modèle : **zéro erreur** ; **15 tests ciblés réussis** sur comportements, glossaire et comparaisons marché.
- **142 nœuds, 6 domaines, 47 capacités, 76 comportements et 346 relations**. Les trois domaines concernés portent respectivement 4, 5 et 9 capacités.
- **560 valeurs antérieurement validées inchangées** ; neuf valeurs remplacées selon les accords explicites U438/U445 ; une définition Structuring reformulée avec statut proposé et preuve de l’ancien accord conservée.
- Les **175 fichiers protégés** de la référence d’audit restent identiques ; publications et audit historique U431 inchangés. Les deux nouveaux comportements ne rouvrent pas cet audit clos.
- Contrôle direct de `contains` et `presents` : **aucune relation de domaine vers un domaine** ; la restitution présente D03, D15 et D04 au même niveau de titre.
- U447 : référentiels en premier puis D04, D01, D06, D15, D03, D05 ; contenu de chaque nœud et relation strictement identique avant/après réordonnancement.

[Preuves de vérification](verification.yaml). Aucun commit, push ou nouvelle publication Atlas effectué.

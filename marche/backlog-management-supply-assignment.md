# Backlog Management et Supply Assignment

14 septembre 2026 — U157. Objet : comparer les résultats métier, sans adopter les frontières de produits ni présumer une fusion de capacités.

## Preuves consultées

| Source | Constat et limite |
| --- | --- |
| [SAP Learning — Explaining Supply Assignment](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4), cours S/4HANA Fashion, édition précise non établie ; texte consulté le 14 septembre 2026 | Lien fixé entre ressource et besoin ; modes normal, preview et simulation. Les outils associés permettent désaffectation et traitement des reliquats. Périmètre produit dépassant la seule écriture d’un lien. Aucune équivalence complète avec Oracle ni configuration Boardriders attestée. |
| [Oracle Cloud SCM 25D — Key Actions on Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faubm/key-actions-on-orders.html), texte consulté le 14 septembre 2026 | Priorisation du carnet, comparaison demandé/planifié/programmé, simulation et ajustement des allocations, puis transmission des résultats à Order Management. La page n’établit pas une affectation ferme de même granularité que SAP ni le traitement de tous types de commandes. |

## Analyse locale

U157 exprime une aptitude durable : travailler un ensemble d’Orders pour décider de leur réalisation, prioriser, évaluer, fractionner et engager. Le carnet n’est pas une simple liste passive. Cela reste une aptitude Supply ; aucune application Case Management ou organisation prescrite. Ce backlog opérationnel est distinct du dossier `modeles/backlog/` qui sert à concevoir la cartographie.

La définition locale D02.e porte affectation/réaffectation/libération de ressources. Le Backlog Management entendu largement recouvre aussi des aptitudes D03 de proposition, révision et échéancement et des aptitudes D04 de connaissance et évolution des Orders. Le traiter comme un synonyme exact de D02.e élargirait silencieusement cette définition et ferait doublon ailleurs.

Inversement, la capacité peut être reformulée à une maille plus large autour de l’arbitrage et de la mise en œuvre de la couverture du carnet, en qualifiant les autres capacités mobilisées. Piste à instruire, pas nouvelle capacité active. La frontière commune prioritaire est le résultat : plan proposé, promesse confirmée, lien d’affectation effectif et modification de contenu d’Order restent distinguables, même s’ils appartiennent à une même aptitude plus large.

**Correction d’analyse :** l’opposition produit simpliste « Backlog Management décide, Supply Assignment ne fait qu’appliquer » n’est pas soutenue par les sources. Elle exprimait la séparation des responsabilités envisagée localement ; ne pas la présenter comme une propriété générale de SAP. Les fonctions SAP de preview/simulation ne sont pas des affectations fermes utilisées par la logistique.

Conclusion : forte communauté de problèmes, équivalence exacte non établie. Backlog Management est plus englobant que notre définition actuelle de Supply Assignment ; leur coexistence comme deux capacités de même niveau, sans frontières explicites, serait contestable. Aucun besoin de fusionner D03/D04, d’étendre la maîtrise des référentiels ou de renommer les capacités par déduction.


## Réorientation U158 — un domaine plutôt qu’une capacité englobante

Laurent propose Backlog Management comme nom de D03. Cela fournit un espace de problèmes cohérent autour de l’arbitrage du carnet et de ses engagements ; la promesse en est un résultat parmi d’autres. L’alternative `D03-BACKLOG-DOMAIN-U158` propose le nom, la définition et la finalité sans changer les valeurs actives.

Frontière proposée : D04 maintient l’Order et son état applicable ; D03 arbitre la réalisation du carnet. La priorité, l’échéancier retenu ou l’affectation sont des décisions/résultats de D03 ; une modification autorisée du contenu d’Order est intégrée par D04. Aucun propriétaire d’objet exclusif, service, API ou bounded context n’est fixé. Le domaine garde aussi la faculté d’évaluer une commande isolée dans le contexte du carnet.

La simulation est une aptitude métier possible si son résultat est défini comme l’évaluation des effets d’hypothèses sur le carnet. Le mode Simulation de SAP ne prouve pas ce rang. Avant d’en faire une capacité distincte, examiner le recouvrement avec ATP/CTP/PTP ; ne pas créer un doublon générique de leurs évaluations. Supply Assignment peut faire émerger plusieurs résultats, mais modifier/libérer un lien existant ne suffit pas automatiquement à justifier des capacités différentes.

Cette réorientation remplace la recommandation précédente d’une simple capacité Backlog Management englobante. Aucune nouvelle source éditeur consultée ; les appuis U157 restent qualifiés comme périmètres de produits, pas comme domaines de notre carte.


## Clarification U159 — résultat propre de la simulation

Laurent distingue ATP/CTP/PTP, qui calculent des solutions, et la simulation, qui en mesure les impacts globaux. Cela répond à la réserve de doublon formulée en U158 : les aptitudes peuvent partager des calculs tout en produisant des résultats différents. Une définition de travail est proposée dans l’annexe JSON : mesurer les conséquences globales d’un scénario par rapport à une situation de référence, sans l’appliquer. Exemples d’impacts à valider : commandes améliorées/dégradées, reliquats, mobilisation de ressources et coûts. Aucune liste d’indicateurs ni nouvelle capacité validée implicitement ; aucune nouvelle comparaison de marché revendiquée.


## Direction courante U413 — Order Backlog Management

D03 est renommé Order Backlog Management. Le mandat adopté comprend le travail collectif du carnet et la préparation de son engagement vers les processus ; les décisions spécialisées le nourrissent. D04 conserve la demande selon son intention. Réexamen ciblé de Lifecycle/Structuring dans modeles/backlog/order-backlog-review.yaml ; aucun déplacement en bloc ni parent de comportement adopté. Les réserves et propositions U157–U159 ci-dessus restent historiques. Comparaison actualisée CMP157.

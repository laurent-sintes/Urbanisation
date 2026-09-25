# Refactoring du Matching — cible validée U749

> Vue de lecture générée depuis [matching-refactoring-U747.yaml](matching-refactoring-U747.yaml). La cible à trois capacités est remplacée par trois catégories et dix capacités. Structure validée U749 et appliquée au modèle canonique U750.

Un master plan commun mobilise plusieurs capacités métier autonomes. Les stratégies sont leurs comportements ; elles ne justifient pas de réduire toutes les décisions à une capacité unique. Microsoft reste l’inspiration principale.

## Master Plan Management

- **Master Planning**. Cadrer, maintenir et réviser le master plan commun en mobilisant les capacités de matching, de simulation et d’application. Comportements : Scope Planning, Schedule Planning, Run Planning, Stop Planning, Rerun Planning, Monitor Plan, Adjust Plan.
- **Simulation & Analysis**. Construire des alternatives de plan, projeter leurs conséquences et comparer leurs effets sur le service, les engagements, les stocks, les coûts et les risques pour éclairer les choix.
- **Plan Application**. Faire appliquer les recommandations autorisées et constater leur prise en compte.

## Supply Matching

- **Demand Prioritization**. Établir et réviser les priorités relatives des besoins à couvrir, selon les engagements et les politiques applicables.
- **Supply Assignment**. Déterminer les affectations cohérentes des ressources aux besoins et leurs révisions autorisées dans le master plan commun. Comportements : Commitment-Preserving Assignment, Supply Reassignment.
- **Replenishment**. Déterminer les apports successifs et leurs ajustements en quantité et en date pour entretenir la disponibilité pendant la commercialisation, selon les besoins, les objectifs de stock, les apports engagés et les contraintes applicables. Comportements : Requirement-based Replenishment, Target-based Replenishment, Replenishment Adjustment.
- **Stock Redistribution**. Déterminer les transferts de stock existant entre sites pour mieux répondre aux besoins, reconstituer des assortiments utiles ou regrouper des stocks dispersés, en tenant compte des coûts et risques. Comportements : Inventory Rebalancing, Stock Consolidation.

## Policy Optimization

- **Inventory Target Optimization**. Déterminer les objectifs de stock et les seuils associés, par produit, lieu et période, selon les besoins, le niveau de service recherché, les délais et les risques. Comportements : Store Demand & Supply Optimization, Distribution Center Demand & Supply Optimization, Multi-Echelon Demand & Supply Optimization.
- **Group Protection Optimization**. Déterminer les quantités à protéger ou les limites d’usage par canal ou groupe de bénéficiaires.
- **Reservation Policy Optimization**. Déterminer dans quelles situations, à quel moment et pour quelle durée réserver des ressources afin de sécuriser la promesse, selon le risque de pénurie et le coût d’indisponibilité pour les autres demandes. Comportements : Milestone-Based Reservation Policy, Time-Fenced Reservation Policy, Demand-Differentiated Reservation Policy, Risk-Adaptive Reservation Policy.

## Portée de l’accord

U749 valide ensemble les trois catégories, les dix capacités nommées, le master plan commun et les familles de stratégies présentées pour Supply Assignment, Replenishment et Stock Redistribution. Les types, descriptions détaillées et choix de migration non présentés restent proposés ; le YAML distingue ces portées et conserve l’empreinte des valeurs approuvées.

Les capacités existantes d’optimisation des cibles, protections et conditions de réservation sont conservées. Policies porte les règles actives ; les capacités de décision en recommandent les évolutions. Disponibilité et réexamen des promesses restent dans Inventory ; confirmation dans Orders ; exécution dans Fulfilment.

## Correspondances appliquées

| Existant | Cible | Traitement |
| --- | --- | --- |
| D05.f Demand & Supply Optimization Planning | Master Planning | Responsabilité conservée comme capacité autonome dans la catégorie Master Plan Management. |
| D05.a Inventory Target Decision | Inventory Target Optimization | Responsabilité conservée comme capacité autonome dans la catégorie Policy Optimization. |
| D05.d Group Protection Decision | Group Protection Optimization | Responsabilité conservée comme capacité autonome dans la catégorie Policy Optimization. |
| D05.e Replenishment Decision | Replenishment | Responsabilité conservée comme capacité autonome dans la catégorie Supply Matching. |
| D05.c Stock Redistribution Decision | Stock Redistribution | Responsabilité conservée comme capacité autonome dans la catégorie Supply Matching. |
| D05.g Initial Stocking Decision | D05.e | Proposition de migration : conserver explicitement l’implantation, les assortiments, quantités par site et dates de lancement dans Replenishment. Le détail de cette absorption n’a pas été présenté en U749. |
| D05.h Reservation Policy Decision | Reservation Policy Optimization | Responsabilité conservée comme capacité autonome dans la catégorie Policy Optimization. |
| D03.m Order Prioritization | Demand Prioritization | Responsabilité conservée comme capacité autonome dans la catégorie Supply Matching. |
| D03.o Fulfillment Plan Decision | Supply Assignment | Responsabilité conservée comme capacité autonome dans la catégorie Supply Matching. |
| D02.e Apply Plan | Plan Application | Responsabilité conservée comme capacité autonome dans la catégorie Master Plan Management. |
| BHV006 Simulation & Analysis | Simulation & Analysis | Responsabilité conservée comme capacité autonome dans la catégorie Master Plan Management. |
| BHV016 Adjust Plan | BHV016 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV024 Inventory Rebalancing | BHV024 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV025 Stock Consolidation | BHV025 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV026 Store Demand & Supply Optimization | BHV026 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV027 Distribution Center Demand & Supply Optimization | BHV027 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV028 Multi-Echelon Demand & Supply Optimization | BHV028 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV032 Milestone-Based Reservation Policy | BHV032 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV033 Time-Fenced Reservation Policy | BHV033 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV034 Demand-Differentiated Reservation Policy | BHV034 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV035 Risk-Adaptive Reservation Policy | BHV035 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV077 Order Rescheduling | BHV016 | Pilotage de révision dans Adjust Plan ; étude des impacts dans Simulation & Analysis ; choix de réaffectation dans Supply Assignment. Aucun BOP absorbé. Répartition détaillée proposée. |
| BHV083 Requirement-based Replenishment | BHV083 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV084 Target-based Replenishment | BHV084 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV085 Replenishment Adjustment | BHV085 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| D04.s Scope Planning | D04.s | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV097 Schedule Planning | BHV097 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV098 Run Planning | BHV098 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV099 Stop Planning | BHV099 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV100 Rerun Planning | BHV100 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |
| BHV101 Monitor Plan | BHV101 | Conserver le comportement, son parent et ses descriptions ; requalifier seulement les références touchées. |

## Précisions de mise en œuvre

- Détail du maintien de l’implantation initiale dans Replenishment : assortiment, quantités par site et date de lancement.
- Répartition des responsabilités d’Order Rescheduling entre révision du plan, simulation et réaffectation, sans absorber le BOP.
- Portée exacte du nouveau nom Demand Prioritization vis-à-vis des besoins prévisionnels.
- Promotion de Simulation & Analysis et Plan Application en capacités, types et requalification des relations. La position en capacité est validée ; les détails techniques et descriptions nouvelles restent proposés.

Ces précisions ne remettent pas en attente l’accord sur la structure. Les 31 éléments existants possèdent une destination appliquée et les 98 relations concernées sont inventoriées dans le YAML.

## Appuis marché

[Master plans Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans), [couverture](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/coverage-settings), [pegging et marking](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/marking), [sélection des ressources](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/make-to-order-supply-automation). Ces sources appuient les mécanismes et le plan commun ; le découpage en dix capacités est une décision de modélisation FLOW. Les sources complémentaires fashion sont conservées dans le YAML et les fiches existantes.


Application U750 : les identifiants BHV006 et D02.e sont conservés lors de leur promotion en capacités ; BHV102 et BHV103 décrivent les deux stratégies de Supply Assignment. D05.g et BHV077 sont retirés avec succession conservée dans le YAML. Les trois catégories et dix capacités sont présentes dans model.yaml ; aucune release effectuée.

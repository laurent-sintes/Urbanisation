# Analyse d’impact du scénario — U270

**Actualisation U271 :** le sixième comportement, sa définition, son rattachement, son bénéfice et les frontières présentées avec Simulation/Evaluation sont adoptés et intégrés. Le corps ci-dessous conserve l’étude U270 avant accord ; voir [les descriptions courantes](../../connaissance/35-comportements-inventory-planning.md). Les compléments éditoriaux et équivalences marché ne deviennent pas adoptés par extension.

17 septembre 2026. Reconnaissance utilisateur d’un comportement complémentaire ; proposition détaillée de Codex ci-dessous. Aucun sixième nœud ajouté à ce stade ; noms et définitions U269 préservés.

## Comparaison au marché

SAP IBP décrit le recalcul des key figures dépendantes lors d’une simulation. Il s’agit de mesures de planification, pas toutes de KPI de pilotage. Ce constat soutient la production de conséquences chiffrées, sans démontrer un comportement métier indépendant nommé Impact Analysis. [S1 — Simulations, IBP 2605](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/36d4c34e3dd04622a4486c0f1360d1c6.html), texte indexé consulté ; ouverture directe sans corps exploitable.

Le cours SAP Inventory Analysis décrit l’impact des scénarios relativement à une référence ou à d’autres scénarios et la sensibilité des résultats aux variables d’entrée. La Scorecard présente des KPI pour apprécier plusieurs options. Ces fonctions sont liées dans le produit ; elles ne prouvent pas un découpage obligatoire en trois capacités ou comportements. [S2 — Inventory Analysis App, Purpose / Key Features](https://learning.sap.com/courses/mastering-sap-ibp-for-inventory-planning-and-optimization/inventory-analysis-app-1) ; [S3 — Inventory Analysis Features, Using the Scenario Scorecard](https://learning.sap.com/courses/mastering-sap-ibp-for-inventory-planning-and-optimization/inventory-analysis-features_f85e091e-ede0-434d-8927-a227bbd673fb). Cours publics sans édition précise affichée ; S3 lu via texte indexé, ouverture directe échouée.

Limite d’accès S2 : texte indexé consulté, ouverture directe retournant 404. S4 est ouvert et lu directement ; les constats sur la prédiction du niveau de service ne dépendent pas de S2/S3.

SAP décrit également Service Level Prediction : estimer le niveau de service atteignable pour un plan de stock donné, notamment après ajustement. Cela fournit un exemple concret d’indicateur de conséquence, distinct d’une simple quantité de stock. [S4 — Calculate Predicted Service Levels](https://learning.sap.com/courses/mastering-sap-ibp-for-inventory-planning-and-optimization/calculate-predicted-service-levels_b60c8b87-3a1d-44f3-a136-c90d2f30098d), cours public sans édition précise affichée.

Oracle compare les plans par indicateurs agrégés et différences d’Orders : autre appui à la distinction entre résultats opérationnels détaillés et appréciation à partir d’indicateurs, sans isoler normativement notre comportement. [S5 — How You Compare Supply Plans and Orders, Oracle 26B](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fausp/how-you-compare-supply-plans-and-orders.html), reconsultation ELM174. Toutes les consultations : 17 septembre 2026 ; appuis fonctionnels, pas preuves de déploiement Beaumanoir.

## Proposition FLOW : Scenario Impact Analysis

**Définition proposée :** Quantifier et expliquer les effets attendus d’un scénario sur les indicateurs métier, par rapport à une situation de référence, pour un périmètre et un horizon donnés.

Les explications doivent s’appuyer sur les hypothèses et résultats disponibles ; aucune attribution causale non établie n’est présumée. Périmètre/horizon/référence évitent de comparer des valeurs incompatibles. Le choix des indicateurs reste à préciser ; ne pas créer une capacité de gestion des KPI par cette seule discussion.

| Comportement | Résultat proposé pour préciser les frontières | Exemple fictif |
| --- | --- | --- |
| Scenario Simulation | Situation opérationnelle projetée sous les hypothèses du scénario, mobilisant les décisions spécialisées | Apports, transferts, stocks et demandes restant insatisfaites par période |
| Scenario Impact Analysis | Indicateurs de conséquence, écarts à la référence et explications disponibles | Service projeté 94 % → 97 %, stock moyen +120 k€, transferts +15 % |
| Scenario Evaluation | Appréciation du compromis selon objectifs, contraintes et comparaison éventuelle entre options | Déterminer si le gain de service justifie l’immobilisation et les contraintes supplémentaires |

**Justification de la décomposition :** rendre visibles les conséquences métier et leur répartition, avant de juger le compromis. Un résultat global peut masquer des dégradations par magasin ou horizon. L’analyse d’impact peut être utile sur un seul scénario, sans classement de plusieurs options. Le comportement reste à la même profondeur que les cinq autres ; pas de sous-comportement ni de nouveau niveau.

**Point de vigilance sur les doublons :** la définition U269 de Simulation (« Produire les conséquences projetées… ») couvre déjà une partie de ce sens ; Evaluation apprécie déjà les résultats. Ajouter une fiche sans préciser ces frontières produirait un recouvrement. La recommandation consiste à détailler les responsabilités de production de la situation projetée, quantification/explication en indicateurs, puis appréciation du compromis. Cela décrit des résultats distincts, pas nécessairement des calculs exécutés successivement ni des logiciels séparés.

La simulation peut déjà produire certains indicateurs ; Impact Analysis peut les exploiter, les agréger et en expliquer les écarts sans les recalculer. Les coûts retenus sont des critères Supply, sans création d’un domaine Finance dans FLOW. Une même représentation logicielle peut combiner les trois comportements.

Si ce découpage est retenu, Inventory Planning possédera six comportements : Construction, Simulation, Impact Analysis, Evaluation, Validation, Application. Cette recommandation et ses formulations sont proposées ; U270 ne leur transfère pas la validation des cinq descriptions U269. Aucun changement du catalogue ni publication.

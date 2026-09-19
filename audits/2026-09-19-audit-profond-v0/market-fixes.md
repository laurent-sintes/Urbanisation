# Lot marché U435 — préparé pour application séquentielle

Le script [apply_market_fixes.py](apply_market_fixes.py) est préparé, **non exécuté par le sous-agent**. Le plan exact est [market-fixes.yaml](market-fixes.yaml). Le modèle partagé n’a pas été modifié par ce sous-agent ; empreinte constatée après préparation : `2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2`.

## Portée exacte

- **15 comparaisons proposées ajoutées** sur des capacités sans rubrique : D01.f, D01.g, D01.c, D02.b, D02.c, D03.i, D03.k, D03.l, D03.m, D03.n, D05.d, D06.b, D06.e, D07.b et D05.f.
- **5 positions FLOW périmées actualisées** : trois dans D03 (préparation/release encore marquées en réexamen alors que U420/U424 fixent les parents) et deux dans BHV060 (ancienne mention de Purchase Order limitée aux biens, déjà remplacée par U391).
- **17 éléments touchés au total**. Aucun nom, définition, parent, comportement, relation, champ validé ou publication modifié.
- Chaque nouvelle entrée reste `status: proposed` et porte uniquement `U435` en `source_refs`. Les identifiants ELM-V0 restent dans l’annexe de preuve ; ils ne deviennent pas des références indexées artificiellement.
- Le script ajoute U435 aux sources des nœuds concernés, sans modifier leurs accords historiques. Révisions, empreintes, `source_files`, refresh et validations finales restent à traiter par le parent.

## Preuves et limites

Les entrées proviennent uniquement de documentations et cours officiels effectivement ouverts : SAP Learning, Oracle et Microsoft. Aucun passage IBM limité par erreur 403 ni fonction extrapolée depuis une présentation commerciale n’est reporté.

Une **28e URL** a été lue après le volet initial pour étayer Inventory Planning avec une documentation technique : [Oracle 26B — Overview of Simulations for Replenishment Plans](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-simulations-for-replenishment-plans.html), sections *Types of Simulations* et paragraphes de mise en action après simulation, consultée le 19 septembre 2026. Elle distingue scénarios portant sur politiques, apports/besoins, coûts et délais, puis utilisation du résultat. FLOW conserve la séparation entre Planning, décisions spécialisées et responsables de la mise en action.

Les correspondances D06.b, D06.e et D07.b sont volontairement limitées : capacité fournisseur communiquée, admissibilité temporelle d’une source et mécanisme de modification de demande. Elles ne prouvent pas la totalité du catalogue de services ou des Service Orders FLOW. Leurs différences sont explicites dans les fiches proposées.

Huit capacités restent sans comparaison faute de preuve suffisamment directe dans ce lot : D07.a, D07.c et les six ingestions D08.d, D09.d, D11.a, D12.a, D13.a, D14.a. Le résultat attendu serait donc **8/47 fiches sans comparaison**, après application, contre 23/47 avant ; cela mesure la documentation, pas la couverture marché.

## Contrôles réalisés

Le plan a été lu et validé avec `scripts.market_comparison.validate_comparisons` : zéro erreur de contrat. Les éléments ciblés existent et aucun ne qualifie `market_comparisons` comme champ validé. Le script vérifie de nouveau cette protection et l’empreinte de la seule rubrique marché avant mutation, ce qui autorise les corrections indépendantes de scope par le parent mais bloque un écrasement concurrent de rubrique marché. L’application est idempotente et nécessite `--apply` ainsi que la présence préalable de U435 dans les contributions.

Le script d’application n’a pas été exécuté, même en simulation. Pas de build ni publication dans ce sous-lot de préparation.

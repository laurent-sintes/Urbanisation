# Comportements d’Inventory Planning — U269/U271

## Inventory Planning

Les six comportements sont adoptés le 17 septembre 2026 : U269 pour les cinq premiers, U271 pour Scenario Impact Analysis et les frontières précisées de Simulation/Evaluation. Les noms, définitions courtes et rattachements ont des portées explicites ; les périmètres et exemples ajoutés restent proposés. L’ancienne définition U235 de la capacité est historisée ; sa nouvelle synthèse ne reprend pas automatiquement cette validation.

**Bénéfice du découpage :** Distinguer ce qu’on envisage, ses conséquences, son intérêt, ce qu’on retient et ce qu’on met effectivement en action.

U271 précise le bénéfice de l’analyse d’impact : rendre les conséquences métier explicites avant appréciation, y compris les dégradations locales éventuellement masquées par une amélioration globale.

## BHV005

**Scenario Construction** — Définir périmètre, hypothèses, objectifs et contraintes.

**Périmètre et exemple proposés :** Construire un premier scénario, le copier ou modifier ses hypothèses. Exemple fictif : préparer deux scénarios de couverture magasin à 10 et 15 jours pour une promotion, avec le même périmètre de comparaison. La construction explicite ce qui sera exploré ; elle ne change pas à elle seule les protections ou Orders opérationnels.

## BHV006

**Scenario Simulation** — Une situation opérationnelle projetée : stocks, apports, transferts, demandes satisfaites ou restantes.

**Périmètre et exemple proposés :** Mobiliser les décisions pertinentes de cibles de couverture, allocations, réapprovisionnement et redistribution. Exemple fictif : établir les apports et transferts proposés et leurs conséquences pour chaque scénario. Les calculs restent dans les décisions spécialisées ; les résultats simulés ne sont pas des mouvements de stock réalisés.

## BHV010

**Scenario Impact Analysis** — Quantifier et expliquer les effets attendus d’un scénario sur les indicateurs métier, par rapport à une situation de référence, pour un périmètre et un horizon donnés.

**Frontière adoptée U271 :** la simulation peut déjà produire les indicateurs ; l’analyse d’impact les exploite et les explique, sans imposer de les recalculer. Evaluation apprécie le compromis à partir de ces conséquences.

**Exemple fictif :** service projeté de 94 % à 97 %, stock moyen supplémentaire de 120 k€, transferts en hausse de 15 %. Examiner les écarts par magasin et période permet de repérer des dégradations locales. Les indicateurs et règles d’explication détaillés restent à instruire, sans présumer de causalité non démontrée.

## BHV007

**Scenario Evaluation** — Une appréciation du compromis selon les objectifs et contraintes.

**Périmètre et exemple proposés :** Apprécier disponibilité, immobilisation et risque selon des critères explicites ; comparer si utile à une référence ou à plusieurs scénarios. Exemple fictif : examiner si le service attendu justifie davantage de stock et signaler les contraintes non satisfaites. Les critères détaillés, pondérations et règles d’arbitrage restent à préciser.

## BHV008

**Scenario Validation** — Retenir et autoriser un scénario, avec ses conditions et réserves.

**Périmètre et exemple proposés :** Identifier le scénario autorisé pour application et les conditions de cet accord. Exemple fictif : retenir le scénario de couverture à 10 jours sur certains magasins, sous réserve des ressources admissibles. Une validation peut être automatique selon les règles ; elle ne prouve pas l’application effective et ne valide pas les définitions du modèle d’urbanisme.

## BHV009

**Scenario Application** — Déclencher les actions retenues et connaître leur prise en compte, via les capacités opérationnelles responsables.

**Périmètre et exemple proposés :** Solliciter [Supply Protection](model:D02.b) pour les protections applicables, les capacités d’[Order Management](model:D04) pour les Orders concernés, puis [Execution Management](model:D06) pour les prestations. Ces capacités conservent leurs responsabilités transactionnelles et opérationnelles. Exemple fictif : demander l’application des seuils retenus et la création des Orders nécessaires, puis distinguer les actions prises en compte, refusées ou restant à traiter. Ne pas confondre scénario retenu, actions engagées et prestations physiquement réalisées. Le détail des dépendances, reprises et conditions de traitement partiel reste proposé ; aucun lot atomique ni séquence technique universelle imposé.

## Sources et portée

U267 propose le découpage ; U268 exige sa justification ; U269 valide les cinq comportements. U270/U271 ajoutent l’analyse d’impact et précisent les frontières. [Comparaison CMP090](../audits/2026-09-17-audit-comportements/scenario-planning-proposition.md) et [analyse d’impact CMP091](../audits/2026-09-17-planning-comportements/impact-analysis.md) : appuis fonctionnels, sans équivalence normative. Les anciennes définitions BHV006/BHV007 sont conservées dans le registre U269 et la capture pré-U271 ; le registre U271 porte leurs nouvelles valeurs. Les quatre décisions D05 restent directement rattachées au domaine. Aucune release implicite.

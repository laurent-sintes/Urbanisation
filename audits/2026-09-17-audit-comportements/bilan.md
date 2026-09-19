# Bilan de réalisation — U265/U266

17 septembre 2026. [Rapport et plan en deux parties](rapport.md), [matrice des 41 capacités](matrice.md), [comparaison et sources](marche.md).

## Livré

- Audit de toutes les capacités et des quatre comportements ATP ; suffisance de la profondeur évaluée sur six familles de cas. Recommandation de niveau terminal maintenue ; complétude métier non présumée.
- Plan A autonome appliqué et plan B conjoint proposé. Aucun déplacement, fusion, nouvelle capacité ou nouvelle dépendance injecté dans le catalogue actif.
- AGENTS.md réduit de **695 à 88 lignes**, et de **142 388 à 14 098 octets**, avec ordre de priorité et liens de lecture ciblés. Capture complète conservée dans AGENTS-before.md ; les récits datés ne sont plus des instructions concurrentes.
- Principe explicite U265 et MOD006, champ `decomposition_rationale` dans le schéma, justification ATP proposée. Contrôle non vide activé par le principe, sans exigence rétroactive sur les publications historiques ; la pertinence reste un jugement métier.
- Six mentions textuelles obsolètes du domaine D07 corrigées en D06, dans des scopes non adoptés. Les identités D07.* restent intactes. Limitations historiques du modèle conservées dans model-before.yaml et remplacées dans le modèle actif par cinq réserves courantes.
- Libellé français du champ dans Atlas ; la restitution Markdown affiche la justification présente. Construction frontend actualisée ; elle affichera ces données lorsqu’elles appartiendront à une publication consultée.
- Comparaison CMP089 et ELM166–172 enregistrés ; références marché existantes réutilisées. Proposition structurée `behavior-audit.yaml` : 41 évaluations, aucune autorité concurrente sur les définitions des capacités.

## Contrôles réellement exécutés

| Contrôle | Résultat |
| --- | --- |
| `python scripts/refresh_sources.py` | 1 224 sources ; seulement index courant modifié |
| `python scripts/validate_models.py` | 0 erreur |
| `python scripts/render_models.py` | Restitutions régénérées |
| `python -m unittest scripts.test_behaviors scripts.test_models scripts.test_publish_release` | 37 tests réussis |
| `pnpm --dir app test` | 35 tests réussis |
| `pnpm --dir app build` | Compilation TypeScript et Vite réussie ; avertissement existant de taille du bundle ELK |
| Comparaison avant/après de ce tour | 92 valeurs de champs validés et tous les lifecycle inchangés ; mêmes identités/types ; 92 relations inchangées |
| Empreintes des publications et preuves | 134 fichiers protégés inchangés |
| Liens locaux du rapport, de la matrice et des instructions | Cibles présentes |
| `git diff --check` | Réussi |

Les nouveaux tests contrôlent la justification absente/vide, l’absence d’obligation de décomposer toutes les capacités et la compatibilité d’un modèle antérieur à cette convention. Les tests existants contrôlent hiérarchie terminale, parent unique, définitions ATP adoptées et release historique. Un texte non vide n’est pas une preuve automatique de bonne justification.

Les preuves chiffrées sont dans `integrity.json`, les empreintes protégées dans `before.json`. `model-before.yaml` capture le backlog réellement audité avant corrections. Scripts ponctuels : `scripts/audit_behaviors_U265.py` et `build_audit.py` ; ils refusent une seconde application. Leurs sorties initiales précèdent quelques compléments éditoriaux explicités dans ce bilan ; ils ne constituent pas un générateur permanent du modèle.

Pas de nouvelle vérification visuelle navigateur dans ce tour : changement d’interface limité au libellé d’un champ déjà rendu génériquement ; compilation et tests de projection/navigation exécutés. Le parcours des comportements a été vérifié au tour U264.

La release courante **v007 / 2026-09-16.2** reste intacte. Les nouvelles données sont dans le backlog, pas dans la publication affichée par défaut dans Atlas. Aucune release, aucun commit ou push.

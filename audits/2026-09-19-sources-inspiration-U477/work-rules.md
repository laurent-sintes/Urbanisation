# Travail éditorial U477 — règles communes

Laurent demande de reprendre toutes les Sources d’inspiration, y compris les fiches sans référence. Le format C publié pour Supply Chain Orchestration est l’exemple accepté. Le périmètre comprend 137 nœuds non illustratifs et 110 termes ; l’univers déjà traité reste inchangé. Pas de release, de commit, d’audit des comportements ou d’extension du catalogue Informations métier dans cette intervention.

Chaque lot dispose d’un `*-input.yaml` extrait des deux captures `before/`. Lire les fiches et leurs sources avant de rédiger. Les sources d’autorité sont toujours `modeles/backlog/model.yaml` et `glossary.yaml`. Les lots sont des deltas de travail, pas des catalogues concurrents. Ne modifier directement aucun fichier d’autorité : le parent intégrera les lots ensemble.

## Résultat attendu

Écrire `BATCH-output.yaml` avec `source: U477`, `nodes` et `terms`, chaque liste contenant les mêmes identifiants que le lot d’entrée. Une entrée comporte `id`, `market_comparisons` (tableau complet), `market_inspiration` et facultativement `editorial_notes` (notes internes d’intégration). Utiliser `scripts.structured_io` pour YAML. Pas de modification des noms, définitions, responsabilités, exemples généraux, rattachements ou accords.

`market_inspiration` est un objet avec :

- `choice` : une ou deux phrases qui commencent par le service ou le sens concret retenu et expliquent le nom ou sa frontière.
- `flow_scope`, `flow_approach` : une courte phrase chacune, adaptées à la maille de la fiche.
- `synthesis` : deux ou trois courts paragraphes nommant les sources, comparant leurs différences et points communs entre elles ET avec FLOW. Éviter les formulations génériques interchangeables.
- `examples` : au moins un objet `{title, situation, outcome, lesson, source_title, source_url, source_refs}`. `lesson` porte la lecture FLOW. Attribuer précisément les exemples effectivement tirés d’une source. Un cas construit doit dire explicitement « Illustration FLOW » dans le titre ou la situation et citer le document qui en soutient le mécanisme, sans le faire passer pour un exemple éditeur ni une observation Beaumanoir.

Chaque `market_comparisons` contient au moins deux documents primaires distincts effectivement consultés et pertinents, à la bonne maille. Trois ou quatre suffisent souvent ; ne pas multiplier les références de remplissage. Une référence scientifique n’est pas obligatoire si elle n’apporte rien de précis.

Chaque entrée de comparaison conserve le contrat : `vendor`, `product`, `element_name`, `element_type`, `relationship`, `similarities`, `differences`, `flow_position`, `source_title`, `source_url`, `source_version`, `source_locator`, `consulted_on`, `status`, `source_refs`, `evidence_limits`. Ajouter `concept_name`, `scope_summary`, `approach_summary`, courts et lisibles. Les champs `term_choice`, `definition_choice` restent optionnels. Le concept et son nom natif diffèrent du titre documentaire. Ne pas qualifier de standard ou consensus sans preuve. Les références nouvelles sont `status: proposed` et comportent `U477` dans leurs sources. Les références existantes conservent leur provenance.

Réexaminer la pertinence et la fidélité de chaque ancienne référence, en consultant les passages mobilisés. Une entrée redondante ou trompeuse peut être remplacée ou regroupée avec une justification dans `editorial_notes` ; ses preuves demeurent dans la capture avant et le relevé des sources. Ne jamais falsifier une consultation inaccessible. Indiquer ses limites et rechercher une autre preuve si elle ne permet pas d’étayer la comparaison. Deux ancres de la même page comptent pour un document.

## Rédaction

Public : métiers, experts de domaine et PO. Français simple, droit au but, cas concret. Ne pas utiliser le mot « transactionnel » comme frontière. Distinguer information, décision, application et exécution physique. Les projections Supply n’administrent pas les maîtres. Pour les commandes, montrer les variantes métier propres, pas une mutualisation logicielle. Les verbes de glossaire sont des conventions locales : comparer des usages proches, pas inventer une définition normative de chaque verbe. Respecter les termes historiques/en réexamen. Aucune preuve d’installation déduite d’une documentation.

Liens glossaire utiles avec `[mot](glossary:TERxxx)` si l’identifiant et le sens sont vérifiés. La reprise ne vaut pas adoption des nouveaux textes.

## Traçabilité

Écrire `BATCH-sources.yaml` : sources effectivement consultées, URL/titre/date/édition/passage, constat utile, exemple réellement présent ou illustration produite, limites, IDs des fiches soutenues. Utiliser les identifiants MKT/ELM/CMP existants quand ils sont établis. Ne pas inventer ni allouer de nouveaux identifiants globaux : le parent enregistrera les nouvelles correspondances du lot. Les refs `[U477]` suffisent provisoirement sur de nouvelles comparaisons avec URL et passage complets.

Exécuter uniquement des contrôles ciblés du lot avant remise (IDs, au moins deux URL distinctes, contrats des entrées, absence de champ manquant). Ne pas lancer refresh_sources, validation globale, rendu global ou build ; le parent les exécutera une fois sur l’état final.

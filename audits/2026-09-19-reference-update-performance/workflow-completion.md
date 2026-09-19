# Mise en œuvre des suites de l’audit de performance

19 septembre 2026 — Laurent a demandé de réaliser la totalité des suites proposées. Ce chantier porte sur les outils et la méthode de mise à jour du référentiel. Aucun contenu métier, accord réel ou pointeur de publication n’est modifié.

## Réexamen des accords

`scripts/decision_review.py` produit un dossier depuis le même candidat que le diagnostic. Il réunit les décisions antérieures, les valeurs avant/après et leurs empreintes, les changements de fiche, de relations incidentes, de contexte global et les impacts du glossaire. `assessment.yaml` est le seul document à compléter ; les autres sont des preuves figées.

Chaque décision commence à `pending`. Un auteur de réexamen, un choix explicite `retain` ou `defer` et une justification de portée sont nécessaires. Une égalité de valeurs n’autorise jamais une reprise automatique. Les valeurs approuvées modifiées, absentes ou retirées sont exclues des transcriptions ; aucune reprise partielle d’un accord n’est fabriquée. Une nouvelle décision métier reste un apport séparé, réellement sourcé.

Une transcription conserve l’auteur, la date, les sources, les champs et les empreintes de l’accord original. Elle reçoit un nouvel identifiant stable, cible la nouvelle révision et cite la preuve de réexamen. Le manifeste fige les preuves ; la publication les archive et leurs empreintes sont contrôlées lors de la validation et de la lecture d’une publication comme base d’une préparation.

Les entrées courantes et leur inventaire, les contrats, le code, le runtime Python, la publication de départ et les paramètres lient le dossier au contexte examiné. Toute différence impose un nouveau dossier. Une modification pendant la construction ou la préparation empêche de figer un mélange d’états.

## Préparation et lecture des résultats

Le parcours maintenu est : **diagnostic avec dossier → réexamen explicite → préparation finale → lecture des artefacts préparés**. Deux constructions sont nécessaires lorsqu’un accord doit être réexaminé ; aucune troisième construction pour relire ou prévalider le même état avant `prepare`.

`prepare` renvoie directement sa synthèse et les chemins des preuves complètes. `prepare_release.py inspect` lit les rapports existants, avec filtres par identifiant, section, pagination et aperçus bornés. `--full` donne les valeurs complètes d’un détail demandé. La lecture n’est jamais présentée comme une nouvelle validation.

Les procédures sont intégrées à `AGENTS.md`, `modeles/README.md` et au skill `release`, synchronisé avec sa copie personnelle. Elles remplacent les scripts ponctuels de transcription et les relances destinées à contourner une sortie tronquée. Les anciens scripts d’opération restent des archives, sans modification ni rejeu.

## Mesure reproductible

`scripts/benchmark_reference_update.py` utilise des copies isolées des seules entrées nécessaires du référentiel actuel, sous `.runtime/reference-benchmark/`. Il simule une précision de note éditoriale sur Purchase Order : nouvelle révision, valeurs approuvées inchangées. Les réexamens automatiques de ce benchmark sont explicitement synthétiques et ne concernent que ces copies. Aucune publication n’est appelée.

Les deux parcours produisent le même candidat, vérifié par empreinte après exclusion des seuls horodatages de génération. Les fichiers réels copiés sont contrôlés inchangés. Le benchmark alterne l’ordre des parcours sur trois répétitions et compare leurs médianes. La copie initiale des fichiers est exclue des temps ; les caches sont réutilisés.

Le premier essai, `workflow-results.json`, a servi à vérifier le protocole et a partagé une partie de son exécution avec la suite de tests. Il ne sert pas de référence de performance. La mesure finale est dans `workflow-final.json`, exécutée seule après les tests.

| Parcours, médiane de trois passages | Temps | Constructions du candidat |
| --- | ---: | ---: |
| Ancien enchaînement avec reconstructions intermédiaires | 18,332 s | 4 |
| Diagnostic avec dossier, inspection, préparation finale | 14,531 s | 2 |

Réduction mesurée : **20,7 %**, soit environ **3,8 secondes** supplémentaires gagnées sur ce scénario, après les optimisations du premier audit. Ces gains ne s’additionnent pas aux pourcentages du cache. Les 147 fichiers nécessaires, soit 12,23 Mo, sont copiés pour chaque essai ; tous les fichiers sources réels sont restés inchangés. Les trois paires de candidats ont des empreintes identiques hors horodatages de génération.

Ces mesures couvrent la chaîne Python de diagnostic, dossier et préparation. Elles ne mesurent ni la génération du LLM ni la durée d’un véritable examen de sens et de portée. Il n’existe pas de mesure avant/après comparable permettant d’annoncer un facteur global sur une intervention humaine/LLM entière.

## Vérifications

- 52 tests ciblés réussis ; 40 tests des parcours affectés rejoués avec succès après le dernier renforcement des contrôles.
- Neuf tests de réexamen : absence d’accord automatique, portée historique conservée, une seule construction finale, dossiers périmés ou falsifiés, choix incomplets ou dupliqués, valeurs modifiées, preuves préparées et archivées altérées, inspection sans reconstruction et changement d’entrées en cours de calcul.
- Inspection CLI d’un rapport réel v013 : sortie paginée, sans nouvelle préparation.
- Validation finale du référentiel réel : zéro erreur ; `git diff --check` sans anomalie.
- Les tests de publication travaillent uniquement dans des projets temporaires. Le benchmark ne publie pas et vérifie les entrées réelles inchangées.
- Aucun build frontend nécessaire ; aucun changement Atlas, de serveur ou de publication pour ce chantier. Aucun commit ni push implicite.

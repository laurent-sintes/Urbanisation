# Intégration U269 — Inventory Planning

Accord utilisateur transcrit dans le backlog le 17 septembre 2026. Aucun changement des publications, commit ou push.

- Cinq comportements BHV005–BHV009 : Scenario Construction, Scenario Simulation, Scenario Evaluation, Scenario Validation, Scenario Application. Noms anglais et descriptions courtes présentés adoptés ; périmètres et exemples ajoutés proposés.
- Cinq relations contains adoptées depuis D05.f. Les quatre décisions D05.a/d/e/c restent directement sous D05, avec leurs relations de mobilisation inchangées.
- Justification du découpage adoptée sur D05.f. Application via les capacités opérationnelles responsables adoptée ; aucune attribution de la réalisation physique à Planning.
- Synthèse de la capacité actualisée et proposée : la validation U235 de l’ancienne définition est conservée dans la capture, sans transfert sur la nouvelle formulation. Nom Inventory Planning conservé. Les trois champs adoptés du domaine D05 sont inchangés.
- AGENTS, MOD002, revue D05, suivi d’audit, connaissance et CMP090 alignés. La généralisation de ces cinq comportements à toutes les capacités Planning reste proposée.

## Contrôles

- Provenance actualisée : 1 230 sources. `validate_models.py` : 0 erreur. Restitutions régénérées.
- `python -m unittest scripts.test_behaviors scripts.test_models` : **30 tests réussis**, dont noms/définitions adoptés, parent unique, décisions conservées au domaine et synthèse parent non validée par héritage.
- `integrity.json` : **41 capacités, 9 comportements**, cinq nouvelles relations structurelles ; les 92 anciennes relations sont inchangées. Seuls D05 et D05.f ont changé parmi les nœuds existants. Les 134 fichiers protégés de publication et preuve sont inchangés.
- `git diff --check` réussi.
- Test navigateur `node app/verify-behaviors.mjs` étendu pour Planning, mais **non exécuté jusqu’aux assertions UI** : connexion refusée sur `127.0.0.1:8765`, serveur Atlas indisponible lors de la tentative. Aucune affirmation de vérification visuelle de cette intégration. Le serveur n’a pas été démarré pour cette validation métier.

La release courante reste **v007 / 2026-09-16.2**. Atlas présente les publications ; les nouveaux comportements Planning deviendront visibles dans ses données courantes lors d’une release. La prise en charge générique des comportements existe déjà dans l’interface.

Les captures avant changement sont les fichiers `*-before.yaml` de ce dossier ; le script ponctuel `scripts/apply_planning_U269.py` refuse une deuxième application. Les sources adoptées sont dans `connaissance/01-contributions-utilisateur.md` (U269) et les portées/hashes dans `modeles/backlog/d05-refactoring.yaml.scenario_behaviors_U269`.

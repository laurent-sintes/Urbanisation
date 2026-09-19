# FLOW — instructions de travail

## Priorités et sources d’autorité

Échanger en français et tutoyer Laurent. Lire les éléments concernés avant de les modifier. Préserver le travail existant. Une instruction récente prime dans sa portée ; un historique ne réactive pas une règle remplacée.

| Besoin | Autorité |
| --- | --- |
| Construire ou discuter le modèle | `modeles/backlog/model.yaml` ; annexes YAML pour propositions et arbitrages |
| Modèle publié / Atlas | `modeles/release/index.json` → descripteur → snapshot ; aucun choix par tri ni complément backlog |
| Vocabulaire métier | `modeles/backlog/glossary.yaml` |
| Vocabulaire méthodologique, dont comportement | `modeles/backlog/modeling-glossary.yaml` ; distinct du glossaire métier |
| Existant | `modeles/panorama-as-is/current.json` ; trois SI et contexte partagé |
| Preuves et corrections | `connaissance/01-contributions-utilisateur.md`, `connaissance/04-corrections.md`, décisions et provenance |
| Contrats et publication | `modeles/README.md`, `modeles/schemas/`, `scripts/validate_models.py` |

Le YAML fait autorité pour le backlog et les nouvelles publications. Utiliser `scripts/structured_io.py` ; aucun modèle JSON concurrent. Index et fichiers techniques JSON restent légitimes. Le Markdown explique sans devenir un deuxième catalogue.

## Invariants de modélisation

Une capacité décrit ce que sait faire durablement l’entreprise, indépendamment de son organisation et de ses outils. Un domaine regroupe des problèmes métier cohérents. Actions à maille large, décisions éventuellement plus fines. Une fonction de produit ne suffit pas à définir une capacité.

Capacité → Comportement est la décomposition descriptive terminale : un parent explicite, aucun sous-comportement. Justifier chaque décomposition par une complexité ou un bénéfice ciblé dans `fields.decomposition_rationale`. Les comportements distinguent mécanisme, politique, variante ou bénéfice ; ne pas créer un comportement par bouton, interface ou paramètre. Étayer les formes concrètes par MOD006 et `behavior-typology.yaml`, sans découpage systématique. Décrire les variantes pour le métier de chaque Order, pas pour une mutualisation logicielle (U389/U398/U399).

Decision inclut ses calculs ; Planning mobilise des décisions distinctes. Simulation & analyse constitue un comportement. Application transactionnelle, déclenchement et réalisation physique restent distincts. Objets, documents et événements ne sont pas des sous-niveaux de comportement. U455 retire les couches transactionnelle/processus : univers et domaines coopèrent par des responsabilités, informations et engagements explicites. Les processus peuvent traverser ces périmètres. Le champ `layer` est absent du backlog courant ; sa présence reste lisible et contrôlée dans les publications historiques figées. Il ne justifie plus une frontière métier.

U456 : Atlas reste strictement métier. Objets, structures d’information métier, documents, faits, règles, autorités et sources d’alimentation métier peuvent y figurer. Applications, produits logiciels, schémas techniques et liens vers leurs réalisations restent hors d’Atlas. L’architecture de solution utilise la référence métier sans devenir une vue d’Atlas. Voir `modeles/backlog/domain-interactions-U455-U456.yaml`.

Construire l’arbre par relations explicites. `contains`, `presents` et liens métier diffèrent ; Business References est un groupe de présentation. Conserver les identifiants, même historiques ; ne jamais réutiliser un identifiant retiré. Qualifier les liens transversaux avec une expression métier, leurs conditions, effets et sources disponibles, afin de rendre leur logique lisible. Une dépendance n’est pas une décomposition.

Noms anglais, définitions françaises, exemples concrets. À notion et périmètre équivalents, préférer les termes établis du marché ; aucune invention de consensus ni renommage automatique. Supply Assignment désigne l’affectation des ressources aux commandes ; préciser les sens d’Allocation lorsqu’un éditeur est cité. L’objectif est une valeur multidimensionnelle, sans pondération implicite.

Pour une modification métier, consulter les sections utiles de [CONVENTIONS-MODELE.md](CONVENTIONS-MODELE.md) : frontières, conventions et renvois spécialisés y sont conservés. Les noms et parents courants du YAML priment sur les repères datés. Ne pas charger ce document entier pour une intervention technique.

## Accords, marché et traçabilité

Enregistrer d’abord les apports métier de Laurent, puis les interpréter. Préserver verbatims, sources, réserves, archives et corrections. Employer les noms canoniques dans le texte rédigé, notamment Boardriders.

Un Go porte sur le contenu présenté et sa portée explicite. Publier ne vaut pas valider ; ne pas étendre un accord aux compléments, descendants ou nouvelles valeurs. Préserver empreintes et accords historiques. `lifecycle`, `review` et décisions ADOPT ne remplacent pas la qualification champ par champ.

À chaque discussion métier (U268), comparer les propositions de Laurent aux références pertinentes effectivement consultées : points communs, différences et limites. Justifier les propositions de Codex par le marché ou la cohérence du modèle, avec bénéfice, frontières et compromis. Suivre `marche/methode.md` ; consigner les correspondances dans les champs du modèle et les réexaminer si le périmètre change. Distinguer constat sourcé, interprétation et recommandation ; une fonctionnalité éditeur n’est pas automatiquement une capacité.

Distinguer cible, applicabilité, couverture documentée et preuve de réalisation installée. Sarenza reste non évalué sans étude. Ne pas inventer de flux, maîtres, observations ni déploiements Beaumanoir. Les référentiels Supply sont des projections de maîtres externes. Aucune administration implicite de données maîtresses.

L’audit des comportements est clos U431 : `modeles/backlog/behavior-gap-audit.yaml`. P04/P10/P12 sont couverts ; `closure_U431.future_work` conserve les précisions futures. Les nouvelles règles enrichissent les prochaines améliorations, sans réouvrir ni lancer automatiquement un audit. Aucun accord global implicite sur les descriptions ou la réalisation installée.

## Contrôles proportionnés

Lire uniquement les sources utiles ; exécuter les contrôles une fois sur l’état final concerné. Rejouer après modification pertinente, échec ou doute restant. Un changement technique n’impose pas une recherche marché métier, une actualisation de provenance ou un audit historique.

| Changement | Vérification et restitution |
| --- | --- |
| Documentation / instructions seules | Relire les liens et la cohérence ; pas de build ni d’audit métier |
| Contributions ou sources indexées | `python scripts/refresh_sources.py` |
| Backlog, glossaires, schémas ou validation | `python scripts/validate_models.py` + tests concernés ; `python scripts/render_models.py --space backlog` si la vue change |
| Panorama As Is | Validation concernée et `python scripts/render_models.py --space panorama-as-is` |
| Audit des comportements ou ses preuves | `python -m scripts.render_behavior_gap_audit` ; `--full` pour forcer le rejeu historique |
| Code Python / publication / lecture structurée | Tests des contrats et parcours touchés ; vérifier l’intégrité, pas publier |
| Frontend | Tests concernés puis `pnpm --dir app build` |
| Release demandée | Skill release ; rapport synthétique `python scripts/prepare_release.py report`, détails `--full` ou `--output CHEMIN_NOUVEAU` |

Le checkpoint local d’audit vérifie les empreintes des fichiers et du code avant réutilisation ; il ne donne aucun accord et ne remplace aucun contrôle de publication. `render_models.py` sans filtre conserve la génération complète. Ne pas réimporter le Markdown historique avec les scripts de migration.

## Atlas et opérations

Release, commit, push et administration serveur sont distincts : utiliser leurs skills seulement pour la demande correspondante. Pas de déclenchement implicite ni confirmation répétée pour une action autorisée. `push` cible Urbanisation ; `flow-push` concerne FLOW-Program. Ne pas changer l’identité Git globale.

Préserver les octets des publications, révisions, preuves et archives ; aucune normalisation implicite. Une correction publiée exige une nouvelle version. Une release part d’une préparation figée contrôlée du backlog courant. Les caches ne dispensent jamais des contrôles d’intégrité.

Atlas présente exclusivement les publications sous Urbanisation : historique sélectionné fixe, courant suivi automatiquement, glossaire et liens du même snapshot. Aucun repli backlog ni glossaire méthodologique présenté comme métier. React/TypeScript, structure React Flow, relations Cytoscape ; conserver les relations publiées et leurs qualifications. Arbre gauche, fiche centrale, recherche, comportements et liens directs ; aucun historique de visites. Identité : `app/BRANDING.md`.

Python sert `app/dist/`, sans Node permanent. Serveur local en lecture seule, port 8765, lanceur `Lancer-FLOW-Atlas.ps1` : vérifier l’identité avant arrêt/redémarrage, redémarrer après modification Python si nécessaire, pas après simple changement de données. Aucun navigateur sans demande. Les procédures détaillées sont dans `app/README.md`, `modeles/README.md` et les skills ; répercuter une modification de skill dans sa copie personnelle sans écraser un skill tiers.

Les conventions détaillées et références ciblées sont dans `CONVENTIONS-MODELE.md`. La [capture antérieure](audits/2026-09-19-performance/AGENTS-before-optimization.md) conserve intégralement les instructions remplacées ; elle sert de preuve, pas de deuxième jeu de règles actives.

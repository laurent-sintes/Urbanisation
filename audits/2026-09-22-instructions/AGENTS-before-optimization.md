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

La hiérarchie courante est **Domain → Area → Capability → Behavior** (U482). Domain désigne le grand périmètre métier, comme Supply Chain Orchestration ; Area regroupe des responsabilités et capacités cohérentes à l’intérieur de ce domaine. Le niveau Domain remplace l’ancien Universe ; les anciens domaines opérationnels deviennent des Areas. Une capacité décrit ce que sait faire durablement l’entreprise, indépendamment de son organisation et de ses outils. Actions à maille large, décisions éventuellement plus fines. Une fonction de produit ne suffit pas à définir une capacité.

Capacité → Comportement est la décomposition descriptive terminale : un parent explicite, aucun sous-comportement. Justifier chaque décomposition par une complexité ou un bénéfice ciblé dans `fields.decomposition_rationale`. Les comportements distinguent mécanisme, politique, variante ou bénéfice ; ne pas créer un comportement par bouton, interface ou paramètre. Étayer les formes concrètes par MOD006 et `behavior-typology.yaml`, sans découpage systématique. Décrire les variantes pour le métier de chaque Order, pas pour une mutualisation logicielle (U389/U398/U399).

Decision inclut ses calculs ; Planning mobilise des décisions distinctes. Simulation & analyse constitue un comportement. Application transactionnelle, déclenchement et réalisation physique restent distincts. Objets, documents et événements ne sont pas des sous-niveaux de comportement. U455 retire les couches transactionnelle/processus : Domains et Areas coopèrent par des responsabilités, informations et engagements explicites. Les processus peuvent traverser ces périmètres. Le champ `layer` est absent du backlog courant ; sa présence reste lisible et contrôlée dans les publications historiques figées. Il ne justifie plus une frontière métier.

Atlas reste strictement métier (U456), avec comparaisons marché visibles et sourcées ; produits et solutions ne deviennent pas des réalisations du modèle. Priorité à la consolidation Supply (U469/U472) : Business Services et TER067 sont retirés, commerce différé. Le catalogue Information existant reste interne, masqué et sans extension ; proposition et engagement restent distincts (U466/U470). Les contrats, limites et sources de ces décisions sont conservés dans [le cadrage courant](CONVENTIONS-MODELE.md#cadrage-courant-u456-u472), à lire seulement pour une modification concernée.

Construire l’arbre par relations explicites. `contains`, `presents` et liens métier diffèrent. U507 fait d’Authoritative Data une Area de Supply Chain Orchestration : elle présente sept référentiels distincts depuis l’ajout d’Assortment (U509), chacun contenant ses capacités d’ingestion et de visibilité. Les références organisent la lecture par sujet, sans nouveau niveau d’Area ni fusion de données. Conserver les identifiants, même historiques ; ne jamais réutiliser un identifiant retiré. Qualifier les liens transversaux avec une expression métier, leurs conditions, effets et sources disponibles, afin de rendre leur logique lisible. Une dépendance n’est pas une décomposition.

Noms anglais, définitions françaises, exemples concrets. À notion et périmètre équivalents, préférer les termes établis du marché ; aucune invention de consensus ni renommage automatique. Supply Assignment désigne l’affectation des ressources aux commandes ; préciser les sens d’Allocation lorsqu’un éditeur est cité. L’objectif est une valeur multidimensionnelle, sans pondération implicite.

Pour une modification métier, consulter les sections utiles de [CONVENTIONS-MODELE.md](CONVENTIONS-MODELE.md) : frontières, conventions et renvois spécialisés y sont conservés. Les noms et parents courants du YAML priment sur les repères datés. Ne pas charger ce document entier pour une intervention technique.

## Accords, marché et traçabilité

Enregistrer d’abord les apports métier de Laurent, puis les interpréter. Préserver verbatims, sources, réserves, archives et corrections. Employer les noms canoniques dans le texte rédigé, notamment Boardriders.

Un Go porte sur le contenu présenté et sa portée explicite. Publier ne vaut pas valider ; ne pas étendre un accord aux compléments, descendants ou nouvelles valeurs. Préserver empreintes et accords historiques. `lifecycle`, `review` et décisions ADOPT ne remplacent pas la qualification champ par champ.

À chaque discussion métier (U268), comparer les propositions de Laurent aux références pertinentes effectivement consultées : points communs, différences et limites. Justifier les propositions de Codex par le marché ou la cohérence du modèle, avec bénéfice, frontières et compromis. Suivre `marche/methode.md` ; consigner les correspondances dans les champs du modèle et les réexaminer si le périmètre change. Distinguer constat sourcé, interprétation et recommandation ; une fonctionnalité éditeur n’est pas automatiquement une capacité. Restituer les comparaisons documentées dans Atlas (U311/U459), y compris leur positionnement et leurs appuis particuliers. Ne qualifier standard ou innovant que sur un constat explicite étayé ; absence de comparaison signifie non documenté. Statuts de revue, réserves internes et liens backlog restent internes.

U472 retire l’ancien univers Business Services (`universe-case`) et son entrée de glossaire `TER067` du modèle courant. Le commerce sera étudié après la Supply Chain : ne pas créer de Domain de remplacement ni développer ce chantier par anticipation. Les identifiants retirés et l’accord U173 restent historiques ; les capacités Supply existantes conservent leurs responsabilités.

Distinguer cible, applicabilité, couverture documentée et preuve de réalisation installée. Sarenza reste non évalué sans étude. Ne pas inventer de flux, maîtres, observations ni déploiements Beaumanoir. U479 : les référentiels Supply gèrent et portent la source de vérité locale du Domain Supply Chain Orchestration ; les sources de vérité à l’échelle de l’entreprise restent externes. L’autorité locale ne se réduit pas à une copie passive et ne transfère pas implicitement la maîtrise d’entreprise.

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
| Release demandée | Skill release ; `python scripts/release.py --source SOURCE --activate`, réexamen ciblé si demandé par le parcours |

Le checkpoint local d’audit vérifie les empreintes des fichiers et du code avant réutilisation ; il ne donne aucun accord et ne remplace aucun contrôle de publication. `render_models.py` sans filtre conserve la génération complète. Ne pas réimporter le Markdown historique avec les scripts de migration.

## Atlas et opérations

Release, commit, push et administration serveur sont distincts : utiliser leurs skills seulement pour la demande correspondante. Pas de déclenchement implicite ni confirmation répétée pour une action autorisée. `push` cible Urbanisation ; `flow-push` concerne FLOW-Program. Ne pas changer l’identité Git globale.

Préserver les octets des publications, révisions, preuves et archives ; aucune normalisation implicite. Une correction publiée exige une nouvelle version. Une release part d’une préparation figée contrôlée du backlog courant. Les caches ne dispensent jamais des contrôles d’intégrité.

Atlas présente exclusivement les publications sous Urbanisation : historique sélectionné fixe, courant suivi automatiquement, glossaire et liens du même snapshot. Aucun repli backlog ni glossaire méthodologique présenté comme métier. React/TypeScript, structure React Flow, relations Cytoscape ; conserver les relations publiées et leurs qualifications. Arbre gauche, fiche centrale, recherche, comportements et liens directs ; aucun historique de visites. Identité : `app/BRANDING.md`.

Python sert `app/dist/`, sans Node permanent. Serveur local en lecture seule, port 8765, lanceur `Lancer-FLOW-Atlas.ps1` : vérifier l’identité avant arrêt/redémarrage, redémarrer après modification Python si nécessaire, pas après simple changement de données. Aucun navigateur sans demande. Les procédures détaillées sont dans `app/README.md`, `modeles/README.md` et les skills ; répercuter une modification de skill dans sa copie personnelle sans écraser un skill tiers.

Les conventions détaillées et références ciblées sont dans `CONVENTIONS-MODELE.md`. La [capture antérieure](audits/2026-09-19-performance/AGENTS-before-optimization.md) conserve intégralement les instructions remplacées ; elle sert de preuve, pas de deuxième jeu de règles actives.


## Lecture et références — U470/U471

Commencer les fiches par le service concret rendu, compréhensible sans connaissance du domaine. Expliquer le jargon utile, illustrer par un cas et relier les mots clés au glossaire avec infobulle. Consigner et appliquer les règles éditoriales de `CONVENTIONS-MODELE.md`.

Dès qu’une fiche présente des rapprochements marché, l’étayer par au moins deux documents primaires distincts et pertinents, conformément à `marche/methode.md`. Justifier le nom et le périmètre de la fiche à son propre niveau ; pour un Domain, ne pas résumer les choix de ses capacités. Deux documents d’un éditeur ne prouvent pas un consensus.

U470 : masquer temporairement le catalogue Informations métier dans Atlas (navigation, fiches, recherche et liens directs), sans supprimer le travail interne ni modifier les publications historiques. La consolidation de la base reste prioritaire ; ne pas étendre ce catalogue.

## Efficacité des mises à jour par l’agent

Lire le périmètre utile avec `python scripts/inspect_model.py D04.j --fields name definition scope` ; ajouter `--relations` si les liens sont concernés, `--collection terms` pour le glossaire, `--space release --version VERSION` pour un état publié. Sans identifiant : recherche `--query` et pagination. Le résultat provient directement du YAML désigné, sans catalogue concurrent. Les champs non sélectionnés ne sont pas réputés absents.

Regrouper les éditions d’un même retour, puis contrôler une fois leur état final. Réutiliser un résultat réussi tant que ses entrées, son code et le contexte restent identiques. Ne pas ajouter de build, recette navigateur ou audit historique à une correction métier seule. Réduire les sorties aux compteurs, champs et erreurs concernés ; écrire les détails volumineux dans un artefact seulement si utile. Après troncature, filtrer cet artefact au lieu de relancer le calcul.

Release U504 : privilégier `scripts/release.py --source SOURCE --activate`, qui construit une fois le candidat puis prépare, publie et vérifie Atlas. Aucun rapport préalable systématique. Les durées et le compte rendu sont générés. Si un examen métier reste nécessaire, le parcours fournit un dossier puis construit une seule préparation finale après résolution. Lire son `report.json` et son candidat figé ; ne pas reconstruire le même candidat uniquement pour le relire avant `prepare`. Les contrôles de publication restent obligatoires. Pour une petite intervention, utiliser Git comme état antérieur lorsqu’il couvre exactement cet état ; sinon capturer les seuls fichiers utiles. Préserver toutes les preuves existantes.

Accords : consigner d’abord l’apport utilisateur et sa portée, puis finaliser les modifications concernées avant de capturer l’accord avec `scripts/record_decision.py`, en amont de toute publication et avec des champs nommés ; ne jamais le déduire de lifecycle. Pour un même retour, regrouper les accords via `record_intents` sur un seul état final et une seule écriture du registre. Ne pas lancer des écritures concurrentes du registre ni modifier le contexte capturé pendant son enregistrement. Vérifier les arguments avant lancement : répéter `--fields` pour plusieurs champs ; pour un nœud, `kind` appartient au contexte et n’est pas un champ sélectionnable. Attendre la fin de l’enregistrement avant les contrôles finaux ; rejouer uniquement après échec ou modification pertinente. Le registre YAML conserve valeurs et contexte, sans version de release imposée. Les reprises automatiques exigent valeurs et contexte métier inchangés ; seules les métadonnées et références éditoriales identifiées peuvent varier. Les champs inconnus restent significatifs.

Accords suspendus : utiliser `prepare_release.py report --version VERSION --source SOURCE --review-output DOSSIER`, puis `inspect DOSSIER --section review --id ID`. Renseigner le réexamen de portée dans `assessment.yaml` avant la reprise avec `release.py --review DOSSIER` ; `retain_partial` permet de reprendre une liste explicite `approved_fields` de valeurs historiques intactes. Les champs modifiés et nouveaux restent exclus ; ne jamais convertir automatiquement « éligible » en « accord repris ». Le [parcours maintenu](modeles/README.md#parcours-maintenu-de-réexamen-des-accords) remplace les scripts ponctuels de transcription. `inspect CHEMIN` lit les rapports enregistrés sans recalcul ; sorties bornées, `--full` seulement pour un détail demandé. Ne pas refaire un diagnostic quand le rapport préparé répond déjà à la question.

Le cache technique `.runtime/parsed-models/` accélère les commandes successives par empreinte du contenu et du parseur. Il ne remplace ni la lecture des octets sources, ni la vérification d’intégrité, ni une validation ou un accord. Ne pas le versionner ni en faire une source de modèle.

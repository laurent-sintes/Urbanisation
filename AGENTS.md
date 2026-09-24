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

## Parcours court par défaut

1. Lire uniquement les éléments concernés et les règles applicables. Utiliser `inspect_model.py` avec des champs ciblés ; ne demander les relations que si elles sont nécessaires.
2. Pour un apport métier, enregistrer le verbatim et sa portée avant interprétation. Pour une intervention technique ou documentaire seule, ne pas créer de dossier métier ni lancer de recherche marché.
3. Finaliser le lot avant les opérations coûteuses : champs requis, références, comparaisons et contexte des accords compris. Un renommage ne déclenche pas une réécriture générale des fiches ou annexes.
4. Si les sources indexées ont changé, actualiser leur index ; capturer ensuite les accords en une seule écriture sur l’état final, sans écriture concurrente ni modification pendant la capture.
5. Appliquer une fois les contrôles du tableau ci-dessous, puis restituer le résultat. Rejouer seulement après échec, modification pertinente ou doute restant. Ne pas confondre accord métier, modification du backlog et publication.

Réutiliser les lectures, sources marché et contrôles déjà valables dans la session tant que leur contenu et leur périmètre restent pertinents. Un acquiescement ou une précision rédactionnelle n’impose pas une nouvelle étude. Conserver les preuves existantes ; capturer seulement les éléments modifiés si Git ne représente pas exactement l’état antérieur.

## Invariants de modélisation

La hiérarchie courante est **Domain → Subdomain → Capability → Behavior** (U655/U673). Domain désigne le grand périmètre métier, comme Supply Chain Orchestration. Subdomain (Sous-domaine) regroupe des responsabilités métier cohérentes au sein du Domain. Il remplace Purpose dans le backlog ; conserver les identifiants et le vocabulaire des publications historiques. Le code technique `area` reste compatible avec le schéma existant ; le principe `PRINCIPLE-DOMAIN-SUBDOMAIN` active le libellé courant. Une capacité décrit ce que sait faire durablement l’entreprise, indépendamment de son organisation et de ses outils. Actions à maille large, décisions éventuellement plus fines. Une fonction de produit ne suffit pas à définir une capacité.

U711 : zéro ou au moins deux comportements différenciants par capacité ; intégrer un comportement isolé à sa capacité, sans en inventer un second. Le rôle dominant du sous-domaine et les catégories de capacités sont des attributs de présentation, sans niveau supplémentaire. Service Order Lifecycle est retiré ; chaque famille conserve son cycle et les invariants communs sont décrits dans le sous-domaine.

Capacité → Comportement est la décomposition descriptive terminale : un parent explicite, aucun sous-comportement. Justifier chaque décomposition par une complexité ou un bénéfice ciblé dans `fields.decomposition_rationale`. Les comportements distinguent mécanisme, politique, variante ou bénéfice ; ne pas créer un comportement par bouton, interface ou paramètre. Étayer les formes concrètes par MOD006 et `behavior-typology.yaml`, sans découpage systématique. Décrire les variantes pour le métier de chaque Order, pas pour une mutualisation logicielle (U389/U398/U399).

Decision inclut ses calculs ; Planning mobilise des décisions distinctes. Simulation & analyse constitue un comportement. Application transactionnelle, déclenchement et réalisation physique restent distincts. Objets, documents et événements ne sont pas des sous-niveaux de comportement. U455 retire les couches transactionnelle/processus : Domains et sous-domaines coopèrent par des responsabilités, informations et engagements explicites. Les processus peuvent traverser ces périmètres. Le champ `layer` est absent du backlog courant ; sa présence reste lisible et contrôlée dans les publications historiques figées. Il ne justifie plus une frontière métier.

Atlas reste strictement métier (U456) ; produits et solutions ne deviennent pas des réalisations du modèle. Priorité Supply (U469/U472) : Business Services (`universe-case`) et TER067 sont retirés, sans Domain de remplacement ni chantier Commerce anticipé. Identifiants retirés et accord U173 restent historiques ; les capacités Supply conservent leurs responsabilités. Le catalogue Informations métier reste interne, masqué dans navigation, fiches, recherche et liens directs, sans suppression ni extension (U470). Proposition et engagement restent distincts (U466). Limites et sources : [cadrage courant](CONVENTIONS-MODELE.md#cadrage-courant-u456-u472), à lire seulement pour une modification concernée.

Construire l’arbre par relations explicites. `contains`, `presents` et liens métier diffèrent. U673 puis U682 appliquent neuf sous-domaines ; voir [l’audit initial](modeles/backlog/capability-subdomain-audit-U667.yaml) et [les ordres de services](modeles/backlog/logistics-execution-audit-U674.yaml) : Master Data, Policies, Plans, Order Management, Inventory Management, Order Promising, Demand & Supply Matching, Service Order Management et Fulfilment Orchestration. Service Order Management porte les exigences et engagements des prestations confiées ; Fulfilment compose, coordonne et adapte leur réalisation. Les familles d’ordres de services sont des capacités sans suffixe Management ; U707 applique les dix familles fashion, retire Value-Added Service Order et intègre Repacking dans Packing Order ; Kitting Order inclut Dekitting. Les preuves restent en annexe, le modèle canonique porte le découpage appliqué. Master Data conserve `business-references` et présente les sept référentiels distincts U509 et Price Book U723, avec leurs vues distinctes et une Master Data Ingestion commune (U717). Policies porte les règles actives ; Plans reçoit les Supply et Demand Plans, sans sous-domaine APS. Supply Plan (prévisions de mouvements de stock hors achats) et master plan de matching (affectations internes) restent distincts. Les références organisent les sujets sans niveau descriptif supplémentaire ni fusion de données. Les Purposes retirés D05/D15/D17 restent tracés, leurs capacités conservant leurs identifiants. Ne jamais réutiliser un identifiant retiré. Qualifier les liens transversaux avec une expression métier, leurs conditions, effets et sources disponibles. Une dépendance n’est pas une décomposition.

Noms anglais, définitions françaises, exemples concrets. À notion et périmètre équivalents, préférer les termes établis du marché ; aucune invention de consensus ni renommage automatique. Supply Assignment désigne l’affectation des ressources aux commandes ; préciser les sens d’Allocation lorsqu’un éditeur est cité. L’objectif est une valeur multidimensionnelle, sans pondération implicite.

Pour une modification métier, consulter les sections utiles de [CONVENTIONS-MODELE.md](CONVENTIONS-MODELE.md) : frontières, conventions et renvois spécialisés y sont conservés. Les noms et parents courants du YAML priment sur les repères datés. Ne pas charger ce document entier pour une intervention technique.

Dans Demand, partir de l’intention de l’acteur déclencheur, du résultat attendu et des engagements (U608–U610). Un document ERP ou un effet juridique ne définit pas automatiquement une demande autonome.

## Accords, marché et traçabilité

Enregistrer d’abord les apports métier de Laurent, puis les interpréter. Préserver verbatims, sources, réserves, archives et corrections. Employer les noms canoniques dans le texte rédigé, notamment Boardriders.

U709 : « je valide » ou un Go porte sur la proposition complète construite au fil de la discussion, avec ses corrections et conditions, pas seulement sur le dernier échange. Reconstituer le lot cohérent avant capture ; exclure les pistes abandonnées et les compléments rédigés ensuite. Appliquer le lot dans model.yaml avant d’annoncer son intégration ; une annexe de preuves ne remplace pas l’application canonique. Les lots suivis portent publication_delivery dans leur annexe : identifiants, champs et rattachements attendus, retraits explicites ; le parcours release vérifie ces déclarations et expose les lots encore pending. Publier ne vaut pas valider ; ne pas étendre un accord aux compléments, descendants ou nouvelles valeurs. Préserver empreintes et accords historiques. `lifecycle`, `review` et décisions ADOPT ne remplacent pas la qualification champ par champ.

À chaque discussion métier (U268), comparer les propositions aux références pertinentes effectivement consultées : points communs, différences, limites. Justifier les choix de Codex par le marché ou la cohérence du modèle, avec bénéfice, frontières et compromis. Distinguer constat, interprétation et recommandation ; ne qualifier standard ou innovant que sur preuve explicite. Absence de comparaison signifie non documenté. Suivre `marche/methode.md` ; conserver les correspondances dans les fiches et les réexaminer si le périmètre change. Chaque fiche comparée exige deux documents primaires distincts et pertinents (U470/U471) ; deux sources d’un éditeur ne prouvent pas un consensus. Justifier nom et périmètre au niveau de la fiche, sans résumer un Domain par ses capacités. Atlas expose positionnement et appuis marché (U311/U459), mais garde statuts de revue, réserves et liens backlog internes.

Commencer les fiches par le service concret rendu, expliquer le jargon utile, illustrer par un cas et relier les mots clés au glossaire avec infobulle. Règles éditoriales : `CONVENTIONS-MODELE.md`.

Distinguer cible, applicabilité, couverture documentée et preuve de réalisation installée. Sarenza reste non évalué sans étude. Ne pas inventer de flux, maîtres, observations ni déploiements Beaumanoir. U479 : les référentiels Supply gèrent et portent la source de vérité locale du Domain Supply Chain Orchestration ; les sources de vérité à l’échelle de l’entreprise restent externes. L’autorité locale ne se réduit pas à une copie passive et ne transfère pas implicitement la maîtrise d’entreprise.

L’audit des comportements est clos U431 : `modeles/backlog/behavior-gap-audit.yaml`. P04/P10/P12 sont couverts ; `closure_U431.future_work` conserve les précisions futures. Les nouvelles règles enrichissent les prochaines améliorations, sans réouvrir ni lancer automatiquement un audit. Aucun accord global implicite sur les descriptions ou la réalisation installée.

## Contrôles proportionnés

Choisir les contrôles selon les fichiers effectivement modifiés ; les lignes applicables se cumulent, sans audit historique automatique.

| Changement | Vérification et restitution |
| --- | --- |
| Documentation / instructions seules | Relire les liens et la cohérence ; pas de build ni d’audit métier |
| Contributions ou sources indexées | `python scripts/refresh_sources.py` |
| Backlog, glossaires, schémas ou validation | `python scripts/validate_models.py` + tests concernés ; `python scripts/render_models.py --space backlog` si la vue change |
| Panorama As Is | Validation concernée et `python scripts/render_models.py --space panorama-as-is` |
| Audit des comportements ou ses preuves | `python -m scripts.render_behavior_gap_audit` lit le résultat clos dans Git ; tout rejeu historique exige un checkout isolé de son ancien état |
| Code Python / publication / lecture structurée | Tests des contrats et parcours touchés ; vérifier l’intégrité, pas publier |
| Frontend | Tests concernés puis `pnpm --dir app build` |
| Release demandée | Skill release ; `python scripts/release.py --source SOURCE --activate`, réexamen ciblé si demandé par le parcours |

Le checkpoint local d’audit vérifie les empreintes des fichiers et du code avant réutilisation ; il ne donne aucun accord et ne remplace aucun contrôle de publication. `render_models.py` sans filtre conserve la génération complète. Ne pas réimporter le Markdown historique avec les scripts de migration.

## Atlas et opérations

Release, commit, push et administration serveur sont distincts : utiliser leurs skills seulement pour la demande correspondante. Pas de déclenchement implicite ni confirmation répétée pour une action autorisée. `push` cible Urbanisation ; `flow-push` concerne FLOW-Program. Ne pas changer l’identité Git globale.

Préserver le contenu des publications et les portées d’accord. Git conserve leurs états historiques ; les copies retirées de l’arbre sont référencées dans `modeles/git-history.json`. Une correction métier publiée exige une nouvelle version. Une release part d’une préparation figée contrôlée du backlog courant. Les caches ne dispensent jamais des contrôles d’intégrité.

Atlas présente exclusivement les publications sous Urbanisation : historique sélectionné fixe, courant suivi automatiquement, glossaire et liens du même snapshot. Aucun repli backlog ni glossaire méthodologique présenté comme métier. React/TypeScript, structure React Flow, relations Cytoscape ; conserver les relations publiées et leurs qualifications. Arbre gauche, fiche centrale, recherche, comportements et liens directs ; aucun historique de visites. Identité : `app/BRANDING.md`.

Python sert `app/dist/`, sans Node permanent. Serveur local en lecture seule, port 8765, lanceur `Lancer-FLOW-Atlas.ps1` : vérifier l’identité avant arrêt/redémarrage, redémarrer après modification Python si nécessaire, pas après simple changement de données. Aucun navigateur sans demande. Les procédures détaillées sont dans `app/README.md`, `modeles/README.md` et les skills ; répercuter une modification de skill dans sa copie personnelle sans écraser un skill tiers.

## Efficacité des mises à jour par l’agent

Lire le périmètre utile avec `python scripts/inspect_model.py D04.j --fields name definition scope` ; ajouter `--relations` si les liens sont concernés, `--collection terms` pour le glossaire, `--space release --version VERSION` pour un état publié. Sans identifiant : recherche `--query` et pagination. Le résultat provient directement du YAML désigné, sans catalogue concurrent. Les champs non sélectionnés ne sont pas réputés absents.

Réduire les sorties aux compteurs, champs et erreurs concernés. Après troncature, filtrer les données utiles plutôt que relancer une lecture ou un calcul complet. Conserver un artefact détaillé seulement s’il sert à la tâche. Pour une opération longue, attendre son résultat avec un délai adapté ; ne pas lancer une seconde écriture pour vérifier ou accélérer la première.

Publication : `scripts/release.py --source SOURCE --activate` utilise le parcours léger (`lean_release.py`). Une construction et une validation du candidat ; préparation temporaire sous `.runtime/publication/`, contrôle des empreintes avant activation, puis vérification Atlas. Aucun rejeu historique ni validation globale du projet dans ce parcours. `validate_models.py` reste le contrôle complet explicite. Les anciennes commandes de publication servent uniquement aux fixtures et à la compatibilité historique ; ne pas les utiliser sur le dépôt migré.

Accords : utiliser `scripts/record_decision.py` sur le lot final ; `record_intents` pour une capture groupée. `decision-intents.yaml` contient seulement les accords en attente, avec leurs valeurs et empreintes de contexte. Les accords publiés figurent dans les décisions de la publication courante. Après publication, les captures consommées quittent le registre actif ; Git conserve leur passé. Une modification de contexte métier exige un réexamen explicite ; un accord inchangé garde son identifiant, sans nouveau récit de report.

Réexamen : `needs_review` fournit le dossier ciblé. Lire `prepare_release.py inspect DOSSIER --section review --id ID`, renseigner `assessment.yaml`, puis reprendre `release.py --review DOSSIER`. `retain_partial` ne conserve que les champs historiques explicitement sélectionnés et inchangés. Publier ne vaut jamais approuver.

Historique : `modeles/release/index.json` conserve le catalogue. Le lecteur `scripts/git_history.py` résout les artefacts retirés par commit exact et chemin, sans recréer une arborescence parallèle. La publication courante et son état source restent autonomes. Avant de retirer une ancienne publication, le parcours exige que ses octets soient déjà conservés dans Git. Il ne crée pas de commit implicitement. Le modèle de travail peut être modifié ; les sources et le code sont liés à la préparation par empreinte et revérifiés avant activation.

Les recherches marché, les contributions utiles et les arbitrages courants restent suivis. Ne pas créer de copie « avant », de journal cumulatif des réflexions ni de rapport historique permanent. Les caches et préparations sont temporaires et ignorés. Le cache de parsing ne remplace ni contrôle d’intégrité ni accord métier.

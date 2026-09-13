# FLOW Atlas — application locale

13 septembre 2026 — réalisation après l’accord contextuel [U105](../connaissance/01-contributions-utilisateur.md#u105), dans le prolongement de [U104](../connaissance/01-contributions-utilisateur.md#u104).

FLOW Atlas permet de parcourir le modèle, de comprendre une capacité dans son contexte et d’explorer ses liens. Les modèles structurés JSON sont l’autorité de la cartographie. Le Markdown conserve les récits, analyses, décisions et restitutions. L’application lit un espace à la fois et distingue les validations, les propositions et les illustrations.

## Lancer l’application

Depuis PowerShell, à la racine du projet :

```powershell
.\Lancer-FLOW-Atlas.ps1
```

Le lanceur cherche un Python 3.10 ou supérieur fonctionnel dans `PATH`, puis dans le runtime Codex de l’utilisateur. Aucun paquet Python ou npm n’est nécessaire. Il démarre le serveur local en arrière-plan et ouvre une fenêtre d’application Edge si Edge est disponible, sinon le navigateur par défaut. Le Python fourni par Codex peut être utilisé sans installation globale.

L’adresse par défaut est [http://127.0.0.1:8765/](http://127.0.0.1:8765/). Un second lancement réutilise le serveur seulement si son identité et la racine du projet correspondent. Si le port est déjà utilisé par un autre service, choisir un autre port :

```powershell
.\Lancer-FLOW-Atlas.ps1 -Port 8766
```

L’option `-Browser` ouvre un onglet classique et `-NoBrowser` démarre ou vérifie le serveur sans ouvrir de fenêtre. Pour arrêter le serveur suivi par le lanceur :

```powershell
.\Lancer-FLOW-Atlas.ps1 -Stop
```

Reprendre `-Port 8766` si ce port a servi au lancement. L’arrêt vérifie l’identité FLOW Atlas, la racine du projet, le port, le PID enregistré et la date de démarrage du processus. Un serveur indisponible ou différent n’est pas arrêté sur la seule base d’un ancien PID. Fermer la fenêtre de l’application laisse le serveur local disponible.

Les journaux et le fichier de suivi du processus sont enregistrés dans `app/.runtime/`. Un échec au démarrage indique le journal à consulter. Si PowerShell interdit l’exécution des scripts selon la politique du poste, le serveur peut aussi être lancé directement depuis un terminal avec un Python disponible :

```powershell
python app/server.py --port 8765
```

Ouvrir ensuite l’adresse locale ci-dessus ; `Ctrl+C` arrête ce serveur exécuté au premier plan. Ce lancement direct ne modifie aucune politique PowerShell.

## Trois espaces distincts

Le sélecteur **Espace de travail** choisit :

| Espace | Fichier faisant autorité | Lecture dans l’application |
| --- | --- | --- |
| **Release** | [current.json](../modeles/release/current.json), qui désigne une version publiée | Dernier modèle publié avec les 36 capacités et leurs statuts explicites. Une publication n’est pas une validation métier de toutes ses entrées. |
| **Backlog** | [model.json](../modeles/backlog/model.json) | Réflexion, propositions, réexamens et exemples. Le parcours illustratif de promesse est réservé à cette vue. |
| **Panorama As Is** | [current.json](../modeles/panorama-as-is/current.json), qui désigne trois fiches de SI | Périmètre historique de Beaumanoir, Boardriders et Sarenza. Sarenza reste explicitement non traité. Le contexte partagé C-Log est présenté séparément, sans en faire un quatrième SI. |

Le **Backlog est la vue initiale** pour explorer et construire le modèle. Un lien qui désigne explicitement la Release ou le Panorama As Is conserve cet espace ; un lien sans espace ouvre le Backlog. Dans la Release, les neuf capacités d’Order Promising validées restent distinguées des validations partielles et des capacités non validées. L’inspecteur affiche les champs adoptés et ceux qui restent proposés. Les derniers rattachements remis en discussion conservent leur historique et leur réserve, notamment Reservation.

Aucun champ de Release n’est complété à partir du Backlog, d’un prototype ou d’une synthèse Markdown. Si un champ manque dans le JSON sélectionné, l’application le signale. Les variantes de conception, dont P82, restent dans le Backlog ; elles ne sont pas transformées en nouvelles capacités de la carte courante. Leurs fiches alternatives sont encore consultables dans le JSON et dans les sources documentaires, sans éditeur ni vue de comparaison dédiée dans l’application.

Le panorama décrit l’état de connaissance des SI actuels. Sa date de publication ne prouve pas une observation récente des déploiements. Les déclarations, réserves, corrections et sources restent accessibles pour chaque fiche. Les listes de composants, flux, autorités d’information et responsabilités de décision ne sont pas fusionnées avec la capability map.

## Explorer et comprendre

- Ouvrir un domaine, un groupe ou un référentiel, puis une capacité. Le fil d’Ariane conserve le contexte.
- Dans le Backlog, suivre les relations métier et le parcours illustratif d’une promesse. Les objets, documents et événements ne deviennent pas des sous-capacités.
- Rechercher par nom, identifiant ou texte. Les alias de recherche français sont réservés au Backlog ; ils ne renomment pas les éléments publiés.
- Ouvrir une source pour retrouver sa formulation et ses réserves. Le lecteur Markdown ne modifie aucun document.
- Copier le lien d’une vue : son fragment conserve l’espace choisi, l’élément, les filtres et la source. Le destinataire doit disposer de cette application locale.
- Actualiser après une modification des fichiers JSON. Une modification du Markdown seule ne change plus le modèle affiché.

## Lecture JSON et maintenance

[atlas_data.py](atlas_data.py) lit les fichiers JSON et le pointeur de Release. Le lecteur refuse les structures invalides et ne revient jamais silencieusement au Markdown ou au Backlog. La révision de l’espace est calculée à partir de ses fichiers JSON et de la configuration de présentation. Les autres espaces restent indépendants.

[model.js](model.js) construit la navigation depuis les nœuds et relations explicites. Les préfixes d’identifiants ne déterminent pas les parents. La hiérarchie reste de profondeur variable et sans cycle ; le graphe des relations métier reste distinct. Les enveloppes Atlas, Socle transactionnel et Processus sont de simples entrées de navigation.

[exploration.json](exploration.json) ne contient plus d’objets ou de relations métier : uniquement libellés de types, icônes, alias et étapes de visite. [model-metadata.json](model-metadata.json) et [legacy/exploration-before-json.json](legacy/exploration-before-json.json) sont des entrées historiques conservées pour la traçabilité de la migration. Le lecteur courant ne les utilise pas comme modèle.

Le serveur utilise la bibliothèque standard Python, écoute sur `127.0.0.1` et n’expose qu’une liste autorisée de fichiers. Les API sont :

- `/api/model?space=release` ou `space=backlog` : un modèle JSON et les liens de ses sources ; Backlog par défaut.
- `/api/panorama` : l’index et les trois fiches de SI avec le contexte partagé.
- `/api/status?space=release`, `backlog` ou `panorama-as-is` : identité du serveur et révision de l’espace ; Backlog par défaut.
- `/api/source?path=…&anchor=…` : un document Markdown autorisé.

Le Markdown n’est analysé que pour ouvrir et localiser les sources. Il n’alimente plus les noms, définitions, finalités ou rattachements du modèle. Les contenus affichés sont échappés, sans exécution de HTML contenu dans les documents.

Cette application reste locale, en lecture seule, sans comptes, édition ni publication sur Internet. Le serveur doit être relancé après une modification du code Python ; un simple rechargement suffit après une modification des fichiers JSON ou de l’interface.

## Vérifier l’application

```powershell
python app/server.py --check
python -m unittest discover -s app -p test_data.py
node --test --test-isolation=none app/test-model.mjs
node app/verify-browser.mjs
```

Les tests couvrent le Backlog par défaut, les liens explicites vers la Release, l’isolation Release/Backlog/As Is, les neuf validations d’Order Promising, les 36 capacités publiées avec statuts, les champs partiellement validés, le maintien des identifiants déplacés, l’absence d’effet des modifications Markdown, les erreurs sans repli automatique et les protections du lecteur de sources.

Le test navigateur utilise Playwright pour le développement, sans dépendance de production. `ATLAS_URL` choisit un autre serveur local et `ATLAS_PLAYWRIGHT_PATH` peut préciser son module. Les captures sont produites dans `app/.runtime/qa-json/`. Le script vérifie les trois espaces, les sources, la recherche, les relations du Backlog, les liens partagés, l’historique et plusieurs largeurs d’écran. Un lien symbolique ne peut être testé sur les postes où sa création n’est pas autorisée.

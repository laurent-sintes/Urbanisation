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

## Urbanisation publiée

Atlas affiche uniquement les modèles publiés, sous le nom **Urbanisation**. La liste **Version publiée** présente la plus récente en premier. Par défaut, la vue suit la dernière publication ; sélectionner une version historique fixe cette consultation. Les liens conservent la version choisie. Les anciens liens contenant un espace backlog ou panorama reviennent à l’urbanisation publiée.

Le serveur lit directement [l’index des publications](../modeles/release/index.json), le descripteur daté qu’il désigne, puis le modèle JSON de cette publication. Atlas n’a pas de référentiel parallèle. Le backlog et le panorama As Is restent des fichiers de travail dans le projet et ne sont pas exposés dans cette interface.

Le modèle et ses éléments portent une révision entière et `last_modified` en UTC. La section **Sources et validation**, ouvrable dans chaque fiche, présente ces métadonnées et les preuves. Les versions historiques sans horodatage précis le signalent. Les notes de release et les détails de changements sont conservés avec chaque nouvelle publication. Les statuts métier restent distincts de la publication.

L’application vérifie automatiquement la révision toutes les cinq secondes quand elle est visible et à son retour au premier plan. Elle recharge les nouvelles données sans action manuelle lorsque la consultation suit la dernière version. Elle conserve le domaine ou la capacité consulté si son identifiant existe encore. Une ancienne version choisie ne bascule pas vers la nouvelle. Après changement du code de l’interface, recharger une fois la page ; les publications de données ultérieures sont automatiques.

## Explorer et lire — U135

L’arbre gauche suit les relations explicites de la publication. Déplier une branche et ouvrir sa fiche sont deux actions distinctes. Les groupes de présentation restent signalés ; les relations vers objets métier, documents et événements ne deviennent pas des enfants hiérarchiques. La sélection et les branches ouvertes sont conservées ; recherche, liens directs et retours révèlent les ancêtres de la fiche. Les visites récentes ont été supprimées.

La séparation entre l’arbre et la fiche se déplace à la souris ou avec les flèches gauche/droite lorsqu’elle a le focus. La largeur choisie et les branches ouvertes sont mémorisées localement, sans enregistrer un historique de visites. Sous 1000 px, le bouton **Arbre** ouvre un tiroir ; Échap le ferme et restitue le focus. Dans l’arbre : flèches pour parcourir et déplier, Home/End pour atteindre le premier/dernier élément visible, Entrée pour ouvrir une fiche. Le focus clavier reste distinct de la sélection.

La fiche présente une seule fois la Finalité, puis la Définition, le Périmètre et les réserves renseignées. Les éléments enfants viennent ensuite. Une vue Relations apparaît lorsque des liens métier sont publiés. Les sources et métadonnées se consultent à la demande ; le statut et la portée synthétique restent visibles en tête.

La recherche porte sur les noms, identifiants et textes publiés, avec filtres selon les types et statuts présents. Ctrl+K place le focus dans la recherche ; flèche bas entre dans les résultats, Entrée ouvre le résultat ciblé. Les synonymes français non présents dans la publication ne sont pas inventés ; les anciennes suggestions sans résultat ont été retirées. La fermeture d’une source retrouve son déclencheur.

## API et contrôles

- `/api/releases` : publications disponibles et identifiant de la publication courante.
- `/api/model` : urbanisation courante ; `?version=2026-09-13.2` pour une publication précise.
- `/api/status` : identité du serveur et révision des données ; même paramètre `version` facultatif.
- `/api/source?path=…&anchor=…` : source documentaire autorisée.

Les demandes d’espace backlog sont refusées, et `/api/panorama` n’est plus exposé. Une publication absente ou invalide provoque une erreur, sans repli vers un autre modèle. Les modèles publiés et descripteurs sont vérifiés par empreintes. Le champ API `dataRevision` sert au rafraîchissement ; `revision` conserve la version entière du modèle.

```powershell
python app/server.py --check
python -m unittest discover -s app -p test_data.py
node --test --test-isolation=none app/test-model.mjs
node app/verify-browser.mjs
node app/verify-tree.mjs
```

Les tests navigateur vérifient les douze domaines et références contre le JSON publié, les anciens liens, la recherche, les sources, les versions historiques, le rafraîchissement automatique et les petits écrans. Le test de publication suivante intercepte les réponses HTTP dans un navigateur de test et ne modifie aucun fichier publié. Captures dans `app/.runtime/qa-urbanisation/`. Playwright est utilisé uniquement pour le développement ; `ATLAS_URL` et `ATLAS_PLAYWRIGHT_PATH` permettent de préciser le serveur et le module.

`verify-tree.mjs` contrôle les rattachements déplacés, l’expansion persistante, le focus, les sources repliées, les filtres, le redimensionnement et le tiroir mobile. Une fixture HTTP synthétique éprouve quatre niveaux supplémentaires et un objet relié sans parent hiérarchique ; aucune donnée de test n’entre dans le modèle. Captures dans `app/.runtime/qa-tree/`.

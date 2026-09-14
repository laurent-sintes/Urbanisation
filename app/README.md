# FLOW Atlas — application locale

14 septembre 2026 — application React avec React Flow et interface sur mesure, selon le choix [U150](../connaissance/01-contributions-utilisateur.md#u150). La première réalisation U105 et l’essai comparatif U146 restent conservés dans les historiques.

FLOW Atlas permet de parcourir l’urbanisation publiée, de comprendre une capacité dans son contexte et d’explorer ses liens. L’arbre gauche, la fiche centrale et la recherche accompagnent les cartes React Flow. Les modèles publiés en YAML, ou en JSON pour les versions historiques, sont l’autorité de cette consultation ; le Markdown conserve les récits, analyses, décisions et restitutions. Une publication ne vaut pas validation métier.

## Compiler l’interface

Depuis PowerShell, à la racine du projet, avec Node.js et pnpm disponibles :

```powershell
pnpm --dir app install --frozen-lockfile
pnpm --dir app build
```

La compilation vérifie TypeScript puis produit `app/dist/index.html` et ses ressources dans `app/dist/assets/`. Le fichier de verrouillage pnpm fixe les dépendances. Après une modification du code React, recompiler puis recharger la page. La compilation de l’interface ne publie aucun modèle métier et ne copie pas le modèle dans le bundle.

Node.js et pnpm servent à la compilation et au développement. L’application compilée utilise ensuite le serveur Python local avec PyYAML, sans serveur Node permanent. Installer le lecteur YAML depuis la racine avec `python -m pip install --target .tools/yaml-runtime -r requirements.txt`. Un dossier `dist` absent produit un diagnostic explicite ; aucune ancienne interface n’est servie en remplacement.

## Lancer l’application

Depuis PowerShell, à la racine du projet :

```powershell
.\Lancer-FLOW-Atlas.ps1
```

Le lanceur vérifie la présence de l’interface compilée et cherche un Python 3.10 ou supérieur fonctionnel dans `PATH`, puis dans le runtime Codex de l’utilisateur. Il démarre le serveur local en arrière-plan et ouvre une fenêtre d’application Edge si Edge est disponible, sinon le navigateur par défaut. Le Python fourni par Codex peut être utilisé sans installation globale.

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

## Développer l’interface

Le serveur Python conserve l’autorité sur la lecture des publications. Dans un premier terminal, le lancer sans navigateur :

```powershell
python app/server.py --port 8765
```

Dans un second terminal :

```powershell
pnpm --dir app dev
```

Vite sert l’interface de développement sur [http://127.0.0.1:5173/](http://127.0.0.1:5173/) et transmet les requêtes `/api` au serveur Python sur 8765. Le rechargement de développement concerne le code ; la sélection de publication et les règles de lecture restent les mêmes. Pour vérifier la livraison locale, recompiler puis consulter le serveur Python sur 8765.

## Urbanisation publiée

Atlas affiche uniquement les modèles publiés, sous le nom **Urbanisation**. La liste **Version publiée** présente la plus récente en premier. Par défaut, la vue suit la dernière publication ; sélectionner une version historique fixe cette consultation. Les liens conservent la version choisie. Les anciens liens contenant un espace backlog ou panorama reviennent à l’urbanisation publiée.

Le serveur lit directement [l’index des publications](../modeles/release/index.json), le descripteur daté qu’il désigne, puis le modèle YAML (ou JSON historique) de cette publication. Atlas n’a pas de référentiel parallèle. Le backlog et le panorama As Is restent des fichiers de travail dans le projet et ne sont pas exposés dans cette interface.

Le modèle et ses éléments portent une révision entière et `last_modified` en UTC. La section **Sources, révision et portée détaillée**, ouvrable dans chaque fiche, présente ces métadonnées et les preuves. Les versions historiques sans horodatage précis le signalent. Les notes de release et les détails de changements sont conservés avec chaque nouvelle publication. Les statuts métier restent distincts de la publication.

L’application vérifie automatiquement la révision toutes les cinq secondes quand elle est visible et à son retour au premier plan. Elle recharge les nouvelles données sans action manuelle lorsque la consultation suit la dernière version. Elle conserve le domaine ou la capacité consulté si son identifiant existe encore. Une ancienne version choisie ne bascule pas vers la nouvelle. Après changement du code de l’interface, recharger une fois la page ; les publications de données ultérieures sont automatiques.

## Explorer et lire

L’arbre gauche suit les relations explicites de la publication. Déplier une branche et ouvrir sa fiche sont deux actions distinctes. Les groupes de présentation restent signalés ; les relations vers objets métier, documents et événements ne deviennent pas des enfants hiérarchiques. La sélection et les branches ouvertes sont conservées ; recherche, liens directs et retours révèlent les ancêtres de la fiche. Les visites récentes ont été supprimées.

La séparation entre l’arbre et la fiche se déplace à la souris ou avec les flèches gauche/droite lorsqu’elle a le focus. La largeur choisie et les branches ouvertes sont mémorisées localement, sans enregistrer un historique de visites. Sous 1000 px, le bouton **Arbre** ouvre un tiroir ; Échap le ferme et restitue le focus. Dans l’arbre : flèches pour parcourir et déplier, Home/End pour atteindre le premier/dernier élément visible, Entrée pour ouvrir une fiche. Le focus clavier reste distinct de la sélection.

La fiche présente une seule fois la Finalité, puis la Définition, le Périmètre et les réserves renseignées. Les éléments enfants viennent ensuite. La vue Relations présente les liens métier publiés et signale les voisinages vides. Les sources et métadonnées se consultent à la demande ; le statut et la portée synthétique restent visibles en tête.

Les cartes React Flow permettent de déplacer et cadrer la vue, puis d’ouvrir les éléments dans leur contexte. Les cartes hiérarchiques utilisent les enfants explicites ; les graphes de relations conservent le sens et la qualification des liens publiés. Un placement visuel ou un cadre de contexte ne crée aucun domaine ni rattachement supplémentaire. Les contrôles de navigation et de carte emploient la même bibliothèque d’icônes.

La recherche porte sur les noms, identifiants et textes publiés, avec filtres selon les types et statuts présents. Ctrl+K place le focus dans la recherche ; flèche bas entre dans les résultats, Entrée ouvre le résultat ciblé. Les synonymes français non présents dans la publication ne sont pas inventés ; les anciennes suggestions sans résultat ont été retirées. La fermeture d’une source retrouve son déclencheur.

## API et contrôles

- `/api/releases` : publications disponibles et identifiant de la publication courante.
- `/api/model` : urbanisation courante ; `?version=2026-09-13.2` pour une publication précise.
- `/api/status` : identité du serveur et révision des données ; même paramètre `version` facultatif.
- `/api/source?path=…&anchor=…` : source documentaire autorisée.

Les demandes d’espace backlog sont refusées, et `/api/panorama` n’est plus exposé. Une publication absente ou invalide provoque une erreur, sans repli vers un autre modèle. Les modèles publiés et descripteurs sont vérifiés par empreintes. Le suivi du catalogue `/api/releases` détecte le changement de publication courante ; `revision` conserve la version entière du modèle.

```powershell
python app/server.py --check
python -m unittest discover -s app -p test_data.py
pnpm --dir app test
pnpm --dir app build
pnpm --dir app verify
```

Les tests navigateur vérifient les domaines et références contre le modèle publié, les anciens liens, la recherche, les sources, les versions historiques, le rafraîchissement automatique et les petits écrans. Le test de publication suivante intercepte les réponses HTTP dans un navigateur de test et ne modifie aucun fichier publié. Captures dans `app/.runtime/qa-react/`. Playwright est utilisé uniquement pour le développement ; `ATLAS_URL` et `ATLAS_PLAYWRIGHT_PATH` permettent de préciser le serveur et le module.

`verify-tree.mjs` contrôle les rattachements déplacés, l’expansion persistante, le focus, les sources repliées, les filtres, le redimensionnement et le tiroir mobile. Une fixture HTTP synthétique éprouve quatre niveaux supplémentaires et un objet relié sans parent hiérarchique ; aucune donnée de test n’entre dans le modèle. Captures dans `app/.runtime/qa-tree/`.

Le serveur de production sert exclusivement l’entrée et les ressources autorisées dans `app/dist/`. Les anciens scripts de l’interface, les sources TypeScript, les dépendances, les source maps et les copies JSON ne sont pas accessibles comme fichiers statiques. Les API restent limitées à la lecture locale, avec vérification de l’hôte et de l’origine, absence de cache et types de contenu explicites. La politique CSP limite scripts et feuilles de style aux fichiers locaux ; seuls les attributs de style nécessaires au placement React Flow sont autorisés en ligne. Elle n’autorise ni scripts en ligne ni évaluation dynamique.

## Structure du frontend

- `src/App.tsx` : composition des vues et navigation ; `navigation.ts` encode les liens et les préférences locales.
- `src/model.ts`, `types.ts` : projection immuable et parcours des relations explicites.
- `src/publication.ts`, `usePublication.ts` : API, catalogue, annulation des requêtes et suivi courant/historique.
- `src/components/Sidebar.tsx` : arbre accessible, recherche et filtres de la publication.
- `src/components/BusinessSheet.tsx`, `SourceDialog.tsx` : lecture métier, preuves et document complet.
- `src/ReactFlowPane.tsx` : cartes et relations ; ELK est chargé seulement lorsqu’un graphe de liens nécessite un placement.
- `src/icons.tsx` : pictogrammes [Lucide React](https://lucide.dev/guide/react), importés individuellement. Les noms connus ont un pictogramme ; les nouveaux éléments utilisent celui de leur type. Cette table décrit uniquement la présentation.

Les anciennes sources `app.js`, `model.js` et `styles.css` ont été remplacées par ces modules. `exploration.json`, `model-metadata.json` et `legacy/` restent des archives de présentation non chargées par la nouvelle interface. Le prototype comparatif dans `prototypes/atlas-exploration/` reste séparé ; aucune dépendance LikeC4 n’est embarquée dans Atlas.

Les cartes et leurs styles sont chargés à la demande. Le fichier ELK reste volumineux (environ 1,43 Mo, 442 ko compressés) mais n’est pas demandé pour une fiche ou une carte hiérarchique ; le serveur Python local sert les ressources sans compression. Le build signale ce chunk différé. Aucune promesse de performance sur des milliers d’éléments n’est déduite du modèle actuel.

## Lecture YAML — U202

Installer `requirements.txt` depuis la racine : `python -m pip install --target .tools/yaml-runtime -r requirements.txt`. Le lecteur commun accepte le modèle YAML publié et les anciens JSON ; les API gardent `application/json`. Aucun changement de contrat HTTP ni de modèle copié dans le navigateur. Après modification du lecteur Python, redémarrer avec le lanceur. Les outils Node qui lisent les fichiers publiés utilisent le même lecteur via `scripts/load-publication.mjs` ; `ATLAS_PYTHON` peut préciser l’interpréteur.
## Glossaire et infobulles — U203

L’accès **Glossaire** est placé dans la navigation, en dehors de la hiérarchie métier. Il présente uniquement `glossary.terms` de la publication consultée, avec recherche par nom, description ou définition. Une ancienne publication sans catalogue affiche un état explicite ; le serveur ne lit pas le glossaire vivant pour la compléter.

Les chaînes `[libellé](glossary:TER059)` et `[libellé](model:D01.f#definition)` sont rendues par `ModelText`. Elles restent des chaînes YAML/JSON ; aucun HTML ni liaison automatique par mot. `ReferenceLink` ajoute une vraie URL, un aperçu au survol/focus et le passage à la fiche. Échap ferme l’aperçu, le pointeur peut passer sur celui-ci ; Entrée, clic, ouverture dans un nouvel onglet et rechargement d’un lien profond conservent la publication. Une cible absente produit un repère explicite, sans redirection vers un autre sens. Les liens de fiches existants utilisent aussi ce composant.

Compiler avec `pnpm --dir app build`, puis recharger la page. Vérifications complémentaires : `node --test --test-isolation=none app/test-glossary.mjs` et `node app/verify-glossary.mjs`. Ce dernier contrôle v003 réelle, puis injecte des données de test uniquement dans son navigateur ; il ne crée pas de release. Captures de contrôle dans `app/.runtime/qa-glossary/` ; captures initiales U203 conservées dans `audits/2026-09-14-glossaire-atlas/`. Le test vérifie aussi le glossaire de la publication courante lorsqu’il existe.

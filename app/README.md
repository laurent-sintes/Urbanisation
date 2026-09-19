# FLOW Atlas — application locale

## Bandeau permanent et défilement

Le fil d’Ariane, le titre, la description et les onglets **Carte / Fiche / Relations / Marché & choix** restent visibles. Seule la zone de contenu sous ce bandeau défile ; l’arbre conserve son propre défilement. Cette règle est commune à l’accueil, aux univers, domaines, capacités et comportements, ainsi qu’aux glossaires et au guide du méta modèle. Sur les écrans de faible hauteur, le bandeau est plus compact.

Sur grand écran, le fil d’Ariane et la copie du lien occupent la barre FLOW de 52 px : ils ne consomment plus une rangée au-dessus du titre. Sur mobile, le bouton d’ouverture de l’arbre rejoint FLOW, tandis que le fil d’Ariane garde sa propre ligne. Beaumanoir devient une signature de 76 px dans le pied de l’arbre, près des statistiques. Les noms longs du fil d’Ariane restent nommés intégralement pour les lecteurs d’écran ; sur grand écran, l’ellipse visuelle conserve leur accès et le titre au survol. [Identité et repères de design](BRANDING.md).

Un changement de vue ou de périmètre remet le contenu en haut ; un lien vers une section affiche directement cette section. La sélection d’une carte dans un même périmètre conserve la position de lecture. L’onglet **Fiche** permanent remplace le bouton « Ouvrir la fiche » en bas de la carte. L’ouverture de la fiche d’un autre élément depuis l’inspecteur de relations reste disponible.

Recette sur le serveur local compilé : `node app/verify-fixed-header.mjs`. Elle contrôle le défilement, les sélections, les liens de section, le clavier et les petits écrans.

`node app/verify-shell.mjs` contrôle la répartition de la barre, les cinq tailles d’écran, la largeur variable de l’arbre, le logo, la copie de lien et l’accès clavier. L’option `--baseline` mesure une version avant modification pour comparer la hauteur réellement gagnée.

## Informations métier — réalisation U468, masquée depuis U470

**État courant :** le catalogue est masqué dans Atlas à la demande de Laurent. Les paragraphes ci-dessous décrivent le fonctionnement conservé en interne et la recette antérieure ; les règles actuelles figurent dans « Allègement de la revue — U470 » en fin de document.

La navigation propose **Informations métier**, avec index filtrable et fiche de lecture. Chaque fiche expose sa question, sa définition, un exemple, sa composition sémantique, ses limites, ses usages par les capacités et les informations liées. L’onglet **Marché & choix** donne les raisons du terme et du périmètre, les différences et les liens directs vers les sources consultées. Les qualifications de travail et identifiants de preuve ne sont pas affichés ni indexés.

Les fiches de capacités, domaines et univers proposent les informations qui concernent leurs capacités explicitement rattachées. Aucun rôle n’est déduit pour un comportement ni propagé par une dépendance. La recherche générale inclut les informations, avec un filtre dédié. Les liens `#version=…&view=information&information=PINFO-…` conservent la publication ; `node=…` ajoute un périmètre de lecture facultatif. Une information absente ou une ancienne publication sans catalogue est signalée sans repli.

Sur écran large, liste et fiche défilent indépendamment ; changer d’information remet la fiche en haut. Sur petit écran, la liste reste compacte et la fiche suit le défilement de la page. Les onglets acceptent les flèches, Home et End. Les références viennent exclusivement de `information_catalog` dans le snapshot métier.

Les 14 fiches U468 sont publiées dans v012 / `2026-09-19.5` ; v011 reste sans catalogue. U469 met l’extension data/information en attente et donne priorité à la revue de la base. Tests : `app/test-information.mjs`, `scripts/test_information_catalog.py` et le parcours de préparation dans `scripts/test_prepare_release.py`. Recette de la publication réelle : `node audits/2026-09-19-release-U469/verify-browser.mjs`. La [recette initiale U468](../audits/2026-09-19-informations-atlas-U468/rapport.md) reste une preuve isolée ; [rapport de publication](../audits/2026-09-19-release-U469/rapport.md).

## Présentation et historique

14 septembre 2026 — application React avec React Flow et interface sur mesure, selon le choix [U150](../connaissance/01-contributions-utilisateur.md#u150). La première réalisation U105 et l’essai comparatif U146 restent conservés dans les historiques.

FLOW Atlas permet de parcourir l’urbanisation publiée, de comprendre une capacité dans son contexte et d’explorer ses liens. L’arbre gauche, la fiche centrale et la recherche accompagnent les cartes React Flow. Les modèles publiés en YAML, ou en JSON pour les versions historiques, sont l’autorité de cette consultation ; le Markdown conserve les récits, analyses, décisions et restitutions. Une publication ne vaut pas validation métier.

## Exploration des dépendances — U415/U419

Le 19 septembre 2026, Laurent a [validé Cytoscape.js](../connaissance/01-contributions-utilisateur.md#u415), puis [autorisé son intégration](../connaissance/01-contributions-utilisateur.md#u419). L’onglet **Relations**, disponible dès l’accueil ou depuis une fiche, utilise Cytoscape pour explorer les liens aux niveaux capacité, domaine et univers. Les cartes de structure conservent React Flow.

Le prototype comparatif utilisait une capture figée du backlog de 46 capacités et 186 relations. L’application lit exclusivement la publication consultée, sans cette capture ni complément depuis le backlog. La profondeur propose un, deux ou trois pas, ou toute la publication. Les filtres portent sur le sens du parcours et le rôle explicitement publié ; une qualification en texte libre ne devient pas automatiquement « a besoin de ». Les changements de niveau regroupent les extrémités selon les rattachements explicites, avec les liens internes et les relations d’origine accessibles dans l’inspecteur. Les comportements sont projetés sur leur capacité parente ; les objets, documents et événements restent distincts. Le parcours ne crée aucune relation transitive.

Les réglages de niveau, profondeur, parcours, qualification, disposition et libellés figurent dans les liens partageables et sont restaurés au retour ou au rechargement. Une sélection de nœud permet de recentrer l’exploration ou d’ouvrir sa fiche ; une sélection de lien ouvre les qualifications, conditions, effets, sources et portées de validation d’origine. Une liste et des contrôles natifs permettent le même parcours au clavier. Les dispositions fCoSE et Dagre sont des réglages d’interface ; les groupes repliables natifs et les performances à grande échelle restent à évaluer. Le moteur graphique ne prescrit aucun découpage logiciel du modèle métier.

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

Atlas affiche uniquement les modèles publiés, sous le nom **Urbanisation**, sans sélecteur de release. Par défaut, la vue suit la publication courante désignée par l’index. Les liens directs contenant une version restent fixes sur cette publication. Les anciens liens contenant un espace backlog ou panorama reviennent à l’urbanisation publiée.

Le serveur lit directement [l’index des publications](../modeles/release/index.json), le descripteur daté qu’il désigne, puis le modèle YAML (ou JSON historique) de cette publication. Atlas n’a pas de référentiel parallèle. Le backlog et le panorama As Is restent des fichiers de travail dans le projet et ne sont pas exposés dans cette interface.

Le modèle et ses éléments portent une révision entière et `last_modified` en UTC. La section **Sources, révision et portée détaillée**, ouvrable dans chaque fiche, présente ces métadonnées et les preuves. Les versions historiques sans horodatage précis le signalent. Les notes de release et les détails de changements sont conservés avec chaque nouvelle publication. Les statuts métier restent distincts de la publication.

L’application vérifie automatiquement la révision toutes les cinq secondes quand elle est visible et à son retour au premier plan. Elle recharge les nouvelles données sans action manuelle lorsque la consultation suit la publication courante. Elle conserve le domaine ou la capacité consulté si son identifiant existe encore. Une version ouverte par lien direct ne bascule pas vers la nouvelle. Après changement du code de l’interface, recharger une fois la page ; les publications de données ultérieures sont automatiques.

## Explorer et lire

L’arbre gauche suit les relations explicites de la publication. Déplier une branche et ouvrir sa fiche sont deux actions distinctes. Les groupes de présentation restent signalés ; les relations vers objets métier, documents et événements ne deviennent pas des enfants hiérarchiques. La sélection et les branches ouvertes sont conservées ; recherche, liens directs et retours révèlent les ancêtres de la fiche. Les visites récentes ont été supprimées.

Les icônes des capacités correspondent à leur `fields.nature` publié : action, gestion, connaissance/visibilité, orchestration, planification ou décision. Les décisions suivent les autres capacités de chaque domaine, avec une ligne légère entre les deux groupes lorsqu’ils existent, dans l’arbre, les cartes et les fiches. L’ordre relatif est conservé dans chaque groupe. Les comportements gardent leur ordre ; une ancienne publication sans type reste explicitement non renseignée, sans déduction du nom ni lecture du backlog.

La séparation entre l’arbre et la fiche se déplace à la souris ou avec les flèches gauche/droite lorsqu’elle a le focus. La largeur choisie et les branches ouvertes sont mémorisées localement, sans enregistrer un historique de visites. Sous 1000 px, le bouton **Arbre** ouvre un tiroir ; Échap le ferme et restitue le focus. Dans l’arbre : flèches pour parcourir et déplier, Home/End pour atteindre le premier/dernier élément visible, Entrée pour ouvrir une fiche. Le focus clavier reste distinct de la sélection.

La fiche présente la Finalité, la Définition, les comportements, le Périmètre et les types renseignés. La vue Relations conserve les qualifications, conditions et effets métier. Depuis U450, les réserves, validations, métadonnées éditoriales et liens vers les sources internes ne sont plus affichés. Ils restent conservés dans les fichiers et preuves internes ; cette présentation ne modifie aucun accord.

Les cartes React Flow permettent de déplacer et cadrer la vue, puis d’ouvrir les éléments dans leur contexte. Les cartes hiérarchiques utilisent les enfants explicites ; la vue Relations utilise Cytoscape et conserve le sens et la qualification des liens publiés. Un placement visuel ou un cadre de contexte ne crée aucun domaine ni rattachement supplémentaire. Les contrôles de navigation et de carte emploient la même bibliothèque d’icônes.

Dans la carte d’un univers, chaque domaine liste ses capacités avec leurs icônes. Le survol ou le focus d’un lien affiche son aperçu ; le clic ou Entrée ouvre directement sa fiche dans la même publication. Le retour du navigateur retrouve la vue Univers. Les listes suivent les rattachements publiés, y compris lorsqu’un identifiant conserve le préfixe d’un autre domaine. La hauteur des cartes suit leur contenu, sur une grille de une à trois colonnes ; la molette fait défiler la page et les boutons de zoom restent disponibles.

La carte **Business References** offre le même parcours : chaque référentiel affiche les liens de ses capacités, avec les mêmes icônes, infobulles et accès direct aux fiches. Cette présentation suit les types et relations publiés, sans transformer le groupe de présentation en univers.

La recherche porte sur les noms, identifiants et textes publiés, avec un filtre par type d’élément. Ctrl+K place le focus dans la recherche ; flèche bas entre dans les résultats, Entrée ouvre le résultat ciblé. Les synonymes français non présents dans la publication ne sont pas inventés. Les anciens paramètres d’URL relatifs au statut ou aux sources internes ne réactivent pas leur affichage.

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

`verify-universe.mjs` contrôle les liens de capacité des cartes de domaines et les cinq référentiels de la carte Business References dans Supply, contre les publications courante et v003. Il vérifie l’ouverture directe des fiches au clic/clavier, les infobulles, le retour navigateur, les univers vides et les listes sur petit écran. Captures dans `app/.runtime/qa-universe/`.

`verify-references.mjs` vérifie les mêmes liens dans les cinq cartes de référentiels : rattachements explicites, clic et clavier, publication historique et affichage desktop/mobile. Captures dans `app/.runtime/qa-references/`.

Le serveur de production sert exclusivement l’entrée et les ressources autorisées dans `app/dist/`. Les anciens scripts de l’interface, les sources TypeScript, les dépendances, les source maps et les copies JSON ne sont pas accessibles comme fichiers statiques. Les API restent limitées à la lecture locale, avec vérification de l’hôte et de l’origine, absence de cache et types de contenu explicites. La politique CSP limite scripts et feuilles de style aux fichiers locaux ; seuls les attributs de style nécessaires au placement React Flow sont autorisés en ligne. Elle n’autorise ni scripts en ligne ni évaluation dynamique.

## Structure du frontend

- `src/brand.css`, `public/assets/` : identité FLOW adoptée en U208, logos originaux et palette du template ; sources et maintenance dans [BRANDING.md](BRANDING.md).
- `src/App.tsx` : composition des vues et navigation ; `navigation.ts` encode les liens et les préférences locales.
- `src/model.ts`, `types.ts` : projection immuable et parcours des relations explicites.
- `src/publication.ts`, `usePublication.ts` : API, catalogue, annulation des requêtes et suivi courant/historique.
- `src/components/Sidebar.tsx` : arbre accessible, recherche et filtres de la publication.
- `src/components/BusinessSheet.tsx`, `SourceDialog.tsx` : lecture métier, preuves et document complet.
- `src/ReactFlowPane.tsx` : cartes de structure et listes de capacités ; placement en grille.
- `src/dependencyGraph.ts` : projection pure des relations publiées et de leurs regroupements, conservant les liens originaux.
- `src/DependenciesPane.tsx`, `CytoscapeCanvas.tsx`, `dependencies.css` : contrôles, inspecteur accessible et rendu Cytoscape avec fCoSE/Dagre.
- `src/icons.tsx` : pictogrammes [Lucide React](https://lucide.dev/guide/react), importés individuellement. Les noms connus ont un pictogramme ; les nouveaux éléments utilisent celui de leur type. Cette table décrit uniquement la présentation.

Les anciennes sources `app.js`, `model.js` et `styles.css` ont été remplacées par ces modules. `exploration.json`, `model-metadata.json` et `legacy/` restent des archives de présentation non chargées par la nouvelle interface. Le prototype comparatif dans `prototypes/atlas-exploration/` reste séparé ; aucune dépendance LikeC4 n’est embarquée dans Atlas.

Les cartes et leurs styles sont chargés à la demande. Cytoscape et ses dispositions ne sont chargés que pour la vue Relations ; les dépendances sont intégrées au build et verrouillées dans pnpm, sans CDN ni changement de CSP. L’ancien moteur ELK n’est plus nécessaire. Le chunk Cytoscape reste volumineux et déclenche l’avertissement de taille de Vite ; les calculs de placement s’exécutent sur le fil principal. Aucune promesse de performance sur des milliers d’éléments n’est déduite du modèle actuel.

Contrôles des dépendances : `pnpm --dir app test` et `pnpm --dir app verify:dependencies`. Ce dernier utilise les publications courante et v003 ainsi qu’une fixture HTTP synthétique isolée, sans lecture du backlog ni modification des publications. Il couvre sens, qualifications, comportements, agrégations, source documentaire, liens directs et mobile. Avec `ATLAS_URL`, il vérifie aussi le serveur réel et sa CSP dans un contexte sans interception. Résultats dans `audits/2026-09-19-atlas-dependencies/browser/` ; [bilan d’intégration](../audits/2026-09-19-atlas-dependencies/README.md).

## Lecture YAML — U202

Installer `requirements.txt` depuis la racine : `python -m pip install --target .tools/yaml-runtime -r requirements.txt`. Le lecteur commun accepte le modèle YAML publié et les anciens JSON ; les API gardent `application/json`. Aucun changement de contrat HTTP ni de modèle copié dans le navigateur. Après modification du lecteur Python, redémarrer avec le lanceur. Les outils Node qui lisent les fichiers publiés utilisent le même lecteur via `scripts/load-publication.mjs` ; `ATLAS_PYTHON` peut préciser l’interpréteur.
## Glossaire et infobulles — U203

Deux accès sont placés hors de l’arbre métier : **Glossaire métier** et **Glossaire du méta modèle**. Le premier lit les termes métier du snapshot ; le second combine les termes méthodologiques figés du guide explicitement associé et les termes TER classés comme méthodologiques par ce guide. Les anciens liens TER gardent leur identité et ouvrent le bon glossaire. Une publication sans guide associé ne récupère aucun complément du backlog. La liste et la définition disposent de panneaux de défilement indépendants ; sélectionner un terme remet sa définition en haut. Sur mobile, les panneaux sont empilés et bornés.

Les chaînes `[libellé](glossary:TER059)` et `[libellé](model:D01.f#definition)` sont rendues par `ModelText`. Elles restent des chaînes YAML/JSON ; aucun HTML ni liaison automatique par mot. `ReferenceLink` ajoute une vraie URL, un aperçu au survol/focus et le passage à la fiche. Échap ferme l’aperçu, le pointeur peut passer sur celui-ci ; Entrée, clic, ouverture dans un nouvel onglet et rechargement d’un lien profond conservent la publication. Une cible absente produit un repère explicite, sans redirection vers un autre sens. Les liens de fiches existants utilisent aussi ce composant.

Compiler avec `pnpm --dir app build`, puis recharger la page. Vérifications complémentaires : `node --test --test-isolation=none app/test-glossary.mjs` et `node app/verify-glossary.mjs`. Ce dernier contrôle v003 réelle, puis injecte des données de test uniquement dans son navigateur ; il ne crée pas de release. Captures de contrôle dans `app/.runtime/qa-glossary/` ; captures initiales U203 conservées dans `audits/2026-09-14-glossaire-atlas/`. Le test vérifie aussi le glossaire de la publication courante lorsqu’il existe.


## Comportements de capacités — U264

Atlas reconnaît les nœuds `behavior` et leur rattachement explicite à une capacité. Arbre terminal et navigation clavier, filtre Comportement et recherche par contenu/ascendance, icône distincte, liste des descriptions dans la fiche de capacité, fiche individuelle avec retour au parent, liens sur les cartes de capacités. Les nombres de comportements et de capacités restent distincts. L’adaptateur refuse les comportements orphelins, rattachés à un autre type ou possédant des enfants. Le champ historique layer n’est plus un critère de parenté depuis U455/U458.

`pnpm --dir app verify:behaviors` vérifie les parcours bureau/mobile dans Edge headless contre le serveur local. Le test intercepte les API **dans son seul navigateur** pour afficher une fixture issue du backlog sous une identité de test. Il ne publie aucune version et contrôle que la publication réelle reste inchangée. Captures et résultats : audits/2026-09-17-comportements-atlas/browser/. Les anciennes publications n’obtiennent aucun contenu du backlog.


## Comparaison par rapport au marché — U311

Les fiches métier et du glossaire affichent les comparaisons structurées du snapshot sélectionné : points communs, différences et références externes consultables. Les statuts, réserves et sources internes restent dans les données. Les termes éditeurs sont recherchables. Les publications historiques sans comparaison ne récupèrent aucune donnée du backlog. La compilation active l’affichage ; la présence de nouvelles données demande une publication métier distincte.

## Comprendre le méta modèle — U319–U322, U450

L’entrée **Comprendre le méta modèle**, à côté des deux glossaires et hors de l’arbre métier, présente six repères visuels. Chaque repère associe un principe, un exemple, deux choix avec explication et un volet **Pour contribuer** : critères et frontières. Les preuves éditoriales restent internes. Le modèle métier ne prescrit aucun découpage de solution ni correspondance un pour un (U322).

Les réponses et les variantes restent éphémères, sans score ni historique de parcours. Le lien direct `#view=principles&principle=ID&version=PUBLICATION` conserve la clé et la publication ; le bouton Copier le lien fixe la publication affichée. Les liens de fiches sont résolus uniquement dans son snapshot.

Le contenu pédagogique est distinct du glossaire métier et du catalogue de capacités. `modeles/modeling-guides/index.yaml` associe explicitement une publication à une version de guide et à son empreinte. `app/modeling_guide.py` lit uniquement cette association et le document YAML figé via `structured_io.py`. `/api/modeling-guide?version=…` renvoie le guide associé ou un état d’absence ; il ne complète jamais une ancienne publication depuis le backlog ni depuis un autre guide. La disponibilité du guide n’altère pas `/api/model`.

Le premier guide du 18 septembre est associé rétrospectivement à v007 (publication du 16 septembre). Sa date et sa portée sont indiquées ; les principes adoptés plus tard et les illustrations sont distingués du contenu du snapshot. L’accord de réalisation U321 ne transforme pas les formulations pédagogiques ou les généralisations proposées en nouveaux accords métier. Les extraits de sources sont figés avec le guide, sans ouvrir une version courante différente à leur place.

Pour une évolution, créer une nouvelle version de guide puis actualiser volontairement les associations et empreintes ; ne pas réécrire une version déjà livrée. U450 associe l’édition méthodologique `2026-09-19.1` à v009, en conservant v007 et son guide. La préparation d’une release capture désormais l’association explicite de sa publication de départ. La publication vérifie son intégrité et la reporte explicitement vers la nouvelle version. Un changement d’index ou de guide après préparation bloque cette reprise ; une base sans association n’en invente aucune. Ce circuit ne complète jamais le modèle métier depuis le backlog.

Depuis U451, les comportements portent une forme principale dans `fields.nature` : politique/stratégie, variante de parcours, mécanisme, périmètre métier, dimension de raisonnement, effet métier ou pratique de planification. Chaque forme possède son pictogramme ; les types inconnus restent neutres. Les capacités contenues par les six référentiels conservent une icône propre au référentiel, déterminée par leur parent explicite. Les décisions restent en fin de liste avec leur séparation légère.

Contrôle U450 : `node app/verify-atlas-presentation.mjs` sur le serveur local compilé. Il vérifie guide, glossaires, anciens liens, défilement, mobile, sources internes masquées et icônes. Les sept formes sont également éprouvées avec une fixture de publication isolée dans le navigateur. Aucun fichier publié n’est modifié par ce contrôle.

Contrôles : `python -m unittest discover -s app -p test_modeling_guide.py`, `pnpm --dir app test`, `pnpm --dir app build`, puis `pnpm --dir app verify:principles`. La vérification navigateur sert les fichiers compilés dans son contexte de test et utilise les publications réelles en lecture seule ; elle ne nécessite pas de démarrer le serveur utilisateur.


## Lectures et actualisation

Les documents structurés déjà analysés sont réutilisés via le cache borné de `scripts/structured_io.py`. Les octets et signatures sont revérifiés à chaque lecture, et les résultats sont copiés pour isoler les requêtes. Le cache disparaît au redémarrage ; une modification de contenu l’invalide même si la date et la taille sont conservées. Il n’existe aucun repli vers le backlog.

La surveillance des publications conserve l’état React lorsque le catalogue et la publication n’ont pas changé. Les changements de publication, erreurs et reprises de connexion restent notifiés. Après modification Python, redémarrer le serveur avec le lanceur et ses contrôles d’identité. Après modification du frontend, reconstruire `app/dist` puis actualiser la page.


### Consultation U458

La recherche classe noms exacts et identifiants en tête, puis les expressions du contenu métier et les termes du glossaire du snapshot. Les champs internes ne sont pas indexés. U459 rétablit les comparaisons visibles et la recherche sur leurs informations métier ; les statuts et sources internes restent exclus. Les résultats indiquent leur nature et un extrait ; les termes ouvrent leur glossaire puis leurs liens métier. Un terme absent du snapshot ne peut être trouvé par repli vers le backlog.

Les fiches présentent finalité, définition, parent et périmètre avant les interactions et comportements repliables ; leurs conditions et effets restent consultables. Les graphes partent des relations directes à la maille choisie ; les relations des comportements sont regroupées avec leur capacité. Les liens entre voisins sont une option avancée conservée dans le lien partagé. Les noms métier restent visibles au dézoom.

Le guide conserve son association versionnée ; le simulateur de réalisations logicielles est retiré. U467 publie la révision pédagogique issue de U458, enrichie jusqu’à U466, comme édition `2026-09-19.2` associée à v011. Aucun repli de lecture vers le brouillon. Recette de la release réelle : `node audits/2026-09-19-release-U467/verify-browser.mjs` ; Information et son exemple, deux glossaires, guide, définition Supply, marché et maintien de v010. La recette initiale `node audits/2026-09-19-plan-U458/verify-reader.mjs` reste celle du brouillon testé en fixture, sans publication.


### Vue d’ensemble et repères marché U459

Les liens de capacités des cartes affichent leur définition et la liste à puces de leurs comportements explicites, au survol comme au focus clavier. Le glossaire n’affiche plus de résumé redondant ; le champ historique reste dans les données et les anciens liens conduisent à la définition.

Les fiches proposent un accès « Marché » et des comparaisons dépliables : nature du rapprochement, appui externe, points communs, différences, choix FLOW et source primaire. Les fiches sans comparaison indiquent un positionnement non documenté ; aucun badge standard ou innovation n’est inventé. Les limites de portée de la preuve restent utiles à la comparaison, distinctes des statuts de revue et réserves internes.

### Marché, choix de vocabulaire et exemples U462

L’onglet **Marché & choix** est voisin de Carte, Fiche et Relations sur chaque élément sélectionné. Il affiche directement la position FLOW et la source primaire datée ; les explications de terme/définition passent en tête lorsqu’elles sont documentées. Les différences, passages et limites documentaires se déplient. Le glossaire utilise la même présentation. Les liens `view=market` sont partageables avec leur publication ; les anciens liens de fiche vers `market_comparisons` sont redirigés.

La fiche place **Exemples concrets** après la définition. `fields.examples` permet situation, résultat et leçon métier. Les anciens périmètres restent lisibles par extraction des passages explicitement signalés comme exemples, y compris les exemples discutés et les marqueurs Markdown historiques. Sources internes et statuts restent privés. La recherche indexe seulement le contenu public des exemples et des raisons de vocabulaire.

Contrôle courant : `node audits/2026-09-19-contenu-U462/verify-ui.mjs`, puis lecture des captures dans le sous-dossier horodaté annoncé. Lecture du serveur local, puis fixture isolée pour les contenus encore non publiés ; aucune mutation de la publication.


## Allègement de la revue — U470

Le catalogue Informations métier est temporairement masqué : pas de bouton de navigation, de section dans les fiches, de résultat ni de filtre de recherche. Un ancien lien `view=information` revient à la fiche de son nœud, ou à la carte, dans la même version. Les données publiées et le travail interne sont conservés ; ce masquage n’est pas un contrôle d’accès à l’API locale. Les composants internes sont conservés sans point d’entrée public.

Les mots clés explicitement reliés au glossaire ouvrent une infobulle au survol et au focus clavier. Elle donne priorité à la définition complète, plutôt qu’au résumé court. U470 ajoute ces liens dans l’univers Supply ; leur disponibilité publique dépend du snapshot publié, sans repli backlog.

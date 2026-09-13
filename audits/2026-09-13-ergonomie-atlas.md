# Audit ergonomique de FLOW Atlas — 13 septembre 2026

**Demande :** U132, complétée par U133 pour la suppression des visites récentes. **Statut :** audit réalisé ; réorganisation proposée, sans modification de l’application ni publication du modèle.

**Suite U135 :** Laurent a autorisé la réalisation par un Go contextuel. L’état audité ci-dessous est conservé ; les changements réalisés et leur vérification figurent à la fin de ce document.

L’interface actuelle ne donne pas assez de place à la lecture du modèle. La navigation gauche ne représente pas son arbre, tandis que le contenu métier des fiches est concentré dans un inspecteur droit. Le centre conserve des cartes, des répétitions et des états vides. La correction prioritaire est donc une réorganisation : **arbre à gauche, fiche métier au centre, preuves consultables à la demande**. Élargir seulement le panneau droit ne résoudrait pas cette répartition.

## Périmètre et méthode

- Application locale identifiée par `/api/status` : FLOW Atlas, dépôt `C:\Dev\Beaumanoir Cartographie`, port 8765, espace `release`.
- Publication effectivement lue : **v002 / `2026-09-13.4`**, depuis `modeles/release/index.json`. Elle contient 49 nœuds, dont 36 capacités ; 36 relations `contains` et 5 relations `presents`. Aucune relation métier transversale n’est publiée dans cette version.
- Inspection du HTML, des styles, du rendu des fiches et de la construction du modèle de navigation. Parcours dans Edge sans interface, avec captures à 1366 × 900, 1920 × 1080, 1024 × 768, 980 × 900 et 390 × 844, en pixels CSS.
- Écrans examinés : carte Urbanisation, Inventory Management, Record Inventory Movements, racine « Modèles », relations et recherche. Essais clavier sur une carte et un résultat ; vérification du retour à la recherche.
- Les [observations brutes](2026-09-13-ergonomie-atlas/observations.json) conservent mesures, résultats, date et empreintes des fichiers examinés. La capture commence le 13 septembre 2026 à 16:49:41 UTC. Les tests utilisent une session de navigateur isolée.

Il s’agit d’un audit expert appuyé sur des parcours réels, pas d’une étude avec utilisateurs ni d’une certification d’accessibilité. Le backlog et les futurs états de cycle de vie U131 ne sont pas utilisés pour enrichir ou requalifier la publication examinée. Les réserves métier restent celles de v002.

## Constats prioritaires

P1 désigne un problème à traiter dans la prochaine réorganisation, car il touche directement l’exploration ou la compréhension. P2 désigne un défaut complémentaire de parcours ou de présentation. Ces priorités ne sont pas des niveaux de gravité de sécurité.

### 1. P1 — La colonne gauche ne montre pas la structure

Elle contient la version, un bouton Urbanisation et les visites récentes. Aucun domaine ni capacité n’y apparaît comme branche. Le fil d’Ariane permet de remonter, mais ne montre pas les branches voisines. Ouvrir une fiche retire donc la vue de ses voisins et oblige à revenir aux cartes pour les retrouver.

Preuves : [structure du rail](../app/index.html), lignes 21–26 ; [rendu de la navigation](../app/app.js), lignes 237–238 ; [capture du domaine](2026-09-13-ergonomie-atlas/02-domaine-1366.png).

**Correction :** remplacer les raccourcis par un arbre dépliable et persistant. La sélection doit rester visible, y compris après une recherche ou l’ouverture d’un lien direct. **Supprimer les visites récentes**, conformément à U133, sans les déplacer dans un autre menu. Les boutons précédent/suivant restent utiles : ils restituent un parcours, sans occuper la colonne avec une liste de visites.

### 2. P1 — La définition occupe une fraction trop faible de la page

Tout le contenu Finalité, Définition, Périmètre, statut et provenance est produit dans `.fa-inspector`. Sa largeur fixe est de 275 px, dont 22 px de retrait et bordure ; elle passe seulement à 320 px au-delà de 1500 px de fenêtre. Le texte métier est composé en 13 px.

Mesures de la fiche **Record Inventory Movements** :

| Fenêtre | Zone centrale | Texte dans l’inspecteur | Début du titre « Définition » |
| --- | ---: | ---: | ---: |
| 1366 × 900 | 818 px | **253 px** | y ≈ 415 px, à droite |
| 1920 × 1080 | 1303 px | **298 px** | y ≈ 419 px, à droite |
| 1024 × 768 | 476 px | **253 px** | y ≈ 415 px, à droite |
| 980 × 900 | 750 px | 750 px, sous la zone centrale | y ≈ 676 px |
| 390 × 844 | 362 px | 362 px, sous la zone centrale | **y ≈ 947 px** |

À 1366 px, la zone centrale est plus de trois fois plus large que le texte métier. À 1920 px, elle est plus de quatre fois plus large. Sur mobile, le contenu devient plus large mais la définition arrive après le premier écran, sous les répétitions et le message d’incomplétude. Aucune largeur testée ne présentait de débordement horizontal ; le problème est l’allocation de l’espace et l’ordre de lecture.

Preuves : [rendu de l’inspecteur](../app/app.js), ligne 153 ; [styles](../app/styles.css), lignes 8, 35–38 et 63–65 ; [fiche à 1366 px](2026-09-13-ergonomie-atlas/03-capacite-1366.png), [fiche à 1920 px](2026-09-13-ergonomie-atlas/04-capacite-1920.png), [fiche mobile complète](2026-09-13-ergonomie-atlas/07-capacite-mobile.png).

**Correction :** mettre la fiche métier dans la zone centrale. Viser initialement un corps de 16 px et une largeur de lecture d’environ 65–85 caractères, à éprouver sur les vraies définitions. Conserver l’espace supplémentaire pour les enfants et les relations, sans étirer chaque paragraphe sur toute la largeur d’un grand écran. Ces valeurs sont des points de départ de conception, pas des seuils normatifs.

### 3. P1 — La page répète la finalité et donne l’impression que la fiche est vide

Sur une capacité sans enfant, le nom est affiché dans le titre puis dans une carte centrale. La finalité apparaît sous le titre, dans cette carte et dans l’inspecteur : **trois occurrences**. La zone centrale affiche ensuite « Le détail reste à enrichir », alors qu’une définition existe dans la colonne droite. L’interface accentue ainsi l’incomplétude au lieu de rendre immédiatement lisible ce qui est connu.

Preuves : [rendu de la fiche](../app/app.js), lignes 153, 170 et 243–246 ; [capture](2026-09-13-ergonomie-atlas/03-capacite-1366.png).

**Correction :** une seule identité de fiche, suivie de la finalité, de la définition et du périmètre. Pour un domaine ou une capacité composée, présenter ensuite les enfants. Pour une feuille, commencer directement par son contenu métier. Réserver les états vides à la rubrique effectivement absente.

### 4. P1 — La recherche ne répond pas à certaines suggestions qu’elle affiche

Essais réels dans v002 :

| Requête | Résultat observé |
| --- | --- |
| `inventaire` | **0 résultat** ; l’écran conseille pourtant d’essayer « inventaire ». |
| `affectation` | 1 résultat : Adjust resource commitments ; Supply Assignment n’apparaît pas. |
| `D03.b` | Promise Confirmation est correctement retrouvé, avec son chemin et son statut. |

Le rendu promet des noms, descriptions et du « vocabulaire français associé », mais les alias de configuration sont désactivés en release. La recherche fait donc une promesse plus large que son index actuel. Les filtres proposent également des catégories absentes de cette publication, notamment Composants SI et Flux SI, et des statuts sans résultat possible dans cette vue. Le filtre « Hypothèses » n’est pas accepté lors de la relecture du lien.

Preuves : [recherche « inventaire »](2026-09-13-ergonomie-atlas/09-recherche-inventaire.png) ; [recherche et filtres](../app/app.js), lignes 92–94 et 213–225 ; [construction des alias](../app/model.js), ligne 45.

**Correction :** ajuster immédiatement les suggestions aux possibilités réelles ; préparer un vocabulaire de recherche publié et traçable pour les usages français. Ne pas réactiver implicitement un enrichissement provenant du backlog. Proposer les types et statuts pertinents dans la publication sélectionnée. À l’ouverture d’un résultat, révéler son chemin dans l’arbre ; conserver le retour à la requête, qui fonctionne déjà dans l’essai effectué.

### 5. P2 — La structure et les relations donnent accès à des impasses répétées

L’onglet Relations est affiché pour tous les éléments. Dans v002, seules les relations hiérarchiques et de présentation existent ; elles sont retirées de l’index des liens métier. Toutes les fiches affichent donc zéro relation dans cette vue. Sur une feuille, Structure ne montre elle-même aucun enfant.

Autre parcours confirmé : cliquer sur « Modèles » dans le fil d’Ariane ouvre une racine Atlas proposant Urbanisation et **Modèle processus**, alors que ce dernier est une coquille de navigation vide. Masquer son bouton gauche ne suffit pas à retirer cette destination.

Preuves : [racine « Modèles »](2026-09-13-ergonomie-atlas/08-racine-modeles.png) ; [construction des coquilles et relations](../app/model.js), lignes 23–25 et 65–69 ; [vues et fil d’Ariane](../app/app.js), lignes 157, 169–170 et 237–246.

**Correction :** une racine visible Urbanisation, avec les branches réellement publiées. Faire de la fiche la vue initiale. Présenter les enfants lorsqu’ils existent et les liens caractérisés lorsqu’ils sont renseignés ; sinon, un état compact « Aucune relation documentée » suffit. Les futures relations restent un parcours important, sans inventer des liens pour remplir l’écran courant.

### 6. P2 — Les preuves détaillées concurrencent la lecture métier

Version, date brute ISO, portée de validation, rattachement, adoptions, sources, chemin Markdown et chemin JSON sont déroulés dans la même colonne que la définition. La fiche D01 atteint environ **1647 px de haut** à 1366 × 900 ; ses sources commencent vers y = 1329 px. Les identifiants et chemins sont utiles pour vérifier une assertion, mais leur affichage systématique impose un volume de lecture important.

**Correction :** conserver près du nom et des champs un statut synthétique et sa portée essentielle. Par exemple, pour D01.g : « Nom adopté ; définition et finalité proposées ». Mettre les preuves complètes dans une section ou un panneau « Sources et validation », ouvert à la demande. Le rattachement contesté et les frontières métier ne doivent pas être masqués parmi les informations techniques. Présenter les dates sous une forme lisible ; garder l’horodatage exact accessible.

Preuves : [inspector](../app/app.js), lignes 138–153 ; [capture du domaine](2026-09-13-ergonomie-atlas/02-domaine-1366.png) et [mesures](2026-09-13-ergonomie-atlas/observations.json).

### 7. P2 — Le défilement et le clavier font perdre le contexte de navigation

Après un défilement de 747 px dans D01, la recherche et les boutons du rail sont sortis de l’écran. Leur positionnement est dans le flux de la page. Après activation au clavier de la carte D01.g ou du résultat D03.b, le focus revient au `body`, car l’élément qui le portait a été remplacé. Une annonce du nom existe, mais le focus de lecture n’est pas établi. Dans l’essai carte, Tab atteint ensuite « Copier le lien ».

Preuves : [observations clavier et défilement](2026-09-13-ergonomie-atlas/observations.json) ; [navigation](../app/app.js), lignes 113–124 ; [structure du rail et du bandeau](../app/styles.css).

**Correction :** conserver la recherche et l’arbre accessibles pendant la lecture, avec un défilement propre à l’arbre. Définir explicitement le focus après navigation, le retour depuis les sources et un accès direct à la fiche. Le futur arbre doit intégrer le clavier dès sa réalisation, sans attendre une phase de finition.

## Organisation recommandée

Schéma de disposition, et non nouvelle hiérarchie métier :

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ FLOW ATLAS     Recherche dans le modèle                 Version publiée │
├────────────────────────┬────────────────────────────────────────────────┤
│ ARBRE                  │ Chemin de l’élément                            │
│                        │                                                │
│ Urbanisation           │ Nom · type · identifiant                       │
│  ▾ Inventory Management│ Statut et portée synthétique                   │
│    Inventory Tracking  │                                                │
│  ● Record Inventory…   │ Finalité                                       │
│    Inventory Visibility│ Définition                                     │
│    Stocktaking         │ Périmètre et frontières                        │
│    Supply Protection   │                                                │
│    Reservation         │ Enfants, si l’élément en possède               │
│  ▸ Order Promising     │ Relations documentées, selon le contenu        │
│  …                     │                                                │
│  ▸ Business References │                  [Sources et validation]       │
└────────────────────────┴────────────────────────────────────────────────┘
```

Le symbole ● désigne la sélection. Business References conserve son indication de groupe de présentation. La liste ci-dessus est un extrait des branches de v002, pas un catalogue supplémentaire.

- **Gauche :** environ 300 px au départ, largeur réglable dans des limites adaptées à l’écran. Déplier une branche et ouvrir une fiche sont deux actions distinctes. L’arbre conserve ses branches ouvertes et révèle la sélection après toute navigation. Aucune rubrique de visites récentes.
- **Centre :** la fiche occupe l’espace principal. Sur un domaine, description puis liste de ses enfants ; sur une capacité feuille, définition immédiatement lisible. Les cartes peuvent rester une vue d’ensemble, sans être obligatoires à chaque profondeur.
- **Preuves :** section repliable ou panneau temporaire. Pas de colonne droite permanente imposée à toutes les fiches. L’ouverture d’une preuve et sa fermeture restituent le contexte.
- **Petits écrans :** accès « Arbre » ouvrant un tiroir ; sélection et expansion conservées. La fiche métier reste prioritaire dans l’ordre vertical. Le passage au tiroir doit dépendre de la largeur disponible pour lire, pas seulement d’un seuil de téléphone.

## Règles de construction de l’arbre

L’arbre de navigation doit être dérivé des relations explicites de la publication : **D02.b et D02.c sous D01 ; D02.e sous D03**. Les préfixes d’identifiants ne sont pas des parents.

`contains` et `presents` n’ont pas le même sens. Business References doit rester reconnaissable comme groupe de présentation. La navigation accepte une profondeur variable ; elle utilisera `group_role` et `level_ref` lorsque de vrais niveaux d’urbanisme seront publiés, sans en créer maintenant. Les objets métier, documents et événements liés ne deviennent pas automatiquement des enfants de capacités.

Pour le clavier, prévoir flèches haut/bas entre les nœuds visibles, droite/gauche pour ouvrir, fermer ou atteindre enfant/parent, Home/End et Entrée pour activer. Distinguer la sélection de la fiche et le focus clavier, exposer les états d’expansion et conserver un indicateur visible. Référence de conception consultée le 13 septembre 2026 : [W3C WAI-ARIA APG — Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/). Ce guide oriente l’interaction ; l’audit ne prétend pas établir une conformité complète.

## Ordre de réalisation proposé et critères de réception

1. **Réorganiser l’exploration et la lecture ensemble.** Arbre gauche, suppression des visites récentes, fiche centrale, clavier et tiroir pour écrans étroits. La sélection reste visible après recherche ou lien direct ; le premier écran d’une fiche contient son sens métier sans carte doublon ni panneau vide préalable.
2. **Rendre les parcours cohérents avec les données publiées.** Racine Urbanisation unique, rubriques adaptées aux enfants et relations disponibles, preuves à la demande, suggestions et filtres de recherche exacts. La simplification conserve toutes les réserves essentielles.
3. **Vérifier la continuité à mesure que le modèle s’enrichit.** Épreuve avec plusieurs niveaux synthétiques dans une fixture de test, libellés longs et branches nombreuses, sans publication de ces données. Les liens métier restent distincts des parents. Une version historique reste fixe ; changement de version, précédent/suivant et actualisation préservent la sélection et l’expansion quand les identifiants existent, avec un message explicite sinon.

Scénarios concrets pour la réception : retrouver Stocktaking avec « inventaire » une fois le vocabulaire publié ; ouvrir Supply Assignment sous Order Promising malgré son identifiant D02.e ; passer d’une capacité à sa voisine sans remonter à la carte ; consulter une réserve de validation puis revenir à la fiche ; retrouver au clavier sa place après navigation ; lire D01.g à 1366 px et sur mobile sans définition reléguée dans un inspecteur.

## Éléments à conserver

La palette calme, les libellés de type, les identifiants stables, les chemins dans les résultats et l’accès aux sources constituent une base utile. Le retour à la requête précédente a fonctionné dans l’essai. La distinction entre publication et validation est essentielle : sa présentation doit devenir plus lisible, sans supprimer sa portée. Aucun changement de bibliothèque ou de serveur n’est nécessaire pour corriger les défauts de répartition et de navigation identifiés ; ils se situent dans le rendu de l’interface.

## Livrables et traçabilité

- Demande et préférence : [U132](../connaissance/01-contributions-utilisateur.md#u132) ; suppression des visites récentes : [U133](../connaissance/01-contributions-utilisateur.md#u133).
- [Mesures, essais et empreintes](2026-09-13-ergonomie-atlas/observations.json), accompagnés de neuf captures dans le même dossier. Les valeurs décrivent les fenêtres et parcours indiqués ; les positions verticales peuvent varier avec les messages de session et le contenu.
- Consignes dans [AGENTS.md](../AGENTS.md) ; réalisation de l’audit consignée au [journal](../JOURNAL.md).

L’application, le backlog, les descripteurs de publication et les instantanés publiés ne sont pas modifiés par cet audit. Les orientations proposées restent à réaliser dans une évolution de l’interface.

## Réalisation U135 — 13 septembre 2026

La réorganisation est réalisée dans `app/index.html`, `app/app.js`, `app/styles.css` et la restitution des métadonnées de groupe dans `app/model.js`.

- Arbre gauche permanent, largeur réglable de 240 à 420 px (300 px par défaut), défilement indépendant, ouverture des ancêtres depuis recherche ou lien direct. La sélection et l’expansion sont distinctes ; les branches ouvertes et la largeur sont mémorisées. Visites récentes supprimées.
- Fiche métier centrale, avec une seule Finalité et une seule Définition. Les réserves de statut et de rattachement restent visibles. Les enfants apparaissent après la description de leur parent. Les métadonnées et sources sont dans une section ouvrable.
- Racine visible Urbanisation ; anciens liens vers les coquilles Atlas/Processus vide ramenés à cette racine. Pas d’onglet Relations vide. Les liens transversaux documentés conservent leur vue distincte de la structure.
- Recherche sur les champs publiés, filtres limités aux types et statuts disponibles, suggestions exactes. Le vocabulaire français absent de la publication reste un enrichissement documentaire ultérieur ; aucune reprise silencieuse d’alias du backlog.
- Navigation clavier de l’arbre et des résultats, focus restauré depuis une source, accès direct au contenu, redimensionnement au clavier. Sous 1000 px, tiroir Arbre avec focus contenu dans le tiroir, Échap et retour à la fiche après sélection.

### Résultats de vérification

Dix tests JavaScript du modèle réussis. Les deux parcours navigateur `verify-browser.mjs` et `verify-tree.mjs` vérifient domaines, versions historiques, actualisation automatique, sources, recherche, arbre, clavier, mobile et profondeur variable ; aucune erreur JavaScript observée. Les scénarios de publication et de profondeur supplémentaire utilisent des réponses HTTP de test, sans modifier les modèles publiés.

| Largeur de fenêtre | Texte métier après correction | Début de la Définition |
| --- | ---: | ---: |
| 1920 px | 673 px | y ≈ 378 px |
| 1366 px | **673 px**, contre 253 px dans l’audit | y ≈ 378 px |
| 1024 px | 663 px | y ≈ 374 px |
| 980 px | 673 px | y ≈ 374 px |
| 390 px | 354 px | **y ≈ 563 px**, contre 947 px |
| 320 px | 284 px | y ≈ 640 px |

Mesures sur Record Inventory Movements, hauteur de fenêtre 844 px dans cette série. Aucun débordement horizontal observé. Le texte métier conserve une largeur de lecture limitée sur les grands écrans.

Captures après réalisation : [fiche centrale](2026-09-13-ergonomie-atlas/apres/fiche-1366.png), [domaine et capacités](2026-09-13-ergonomie-atlas/apres/domaine.png), [fiche mobile](2026-09-13-ergonomie-atlas/apres/fiche-mobile.png), [tiroir Arbre](2026-09-13-ergonomie-atlas/apres/arbre-mobile.png).

La publication reste v002 / `2026-09-13.4`. Aucune release, aucun changement de contenu métier et aucun redémarrage du serveur ne sont nécessaires pour cette évolution du rendu ; une page rechargée utilise le nouveau code.

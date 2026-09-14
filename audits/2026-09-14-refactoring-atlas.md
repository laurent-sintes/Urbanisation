# Atlas — refactoring React Flow et iconographie

14 septembre 2026 — réalisation U152/U153, après le choix U150.

## Résultat

L’application courante sur `127.0.0.1:8765` utilise React, TypeScript et React Flow. Le serveur Python local conserve les API et sert les fichiers compilés. Le prototype comparatif est conservé dans son dossier historique ; LikeC4 n’entre pas dans les dépendances de l’application.

La consultation reste limitée à la publication désignée par l’index, son descripteur et son JSON. La release examinée est v003, `2026-09-13.5`, à 51 nœuds et 36 capacités. Les travaux simultanés du backlog ne sont pas ajoutés à cette consultation. Les empreintes de l’index, du descripteur et du modèle publié sont comparées à l’état figé de l’étude U143.

## Parcours

- **Arbre gauche** : relations explicites, profondeur libre, expansion et sélection distinctes, largeur réglable de 240 à 420 px, préférences conservées. L’arbre révèle l’élément choisi sans déplacer la page centrale. Le clavier conserve un point d’entrée après repli d’une branche ou sélection d’un objet transversal.
- **Carte** : grille de cartes avec contexte stable, zoom, déplacement, centrage et plein écran. Sélectionner un élément met à jour son repère dans l’arbre et le bandeau sous la carte. Explorer ouvre un niveau ; double-cliquer une capacité sans enfant ouvre sa fiche. Un périmètre vide est annoncé explicitement.
- **Fiche** : lecture centrale, finalité non répétée, définition, périmètre, champs complémentaires et réserves. Champs adoptés, compléments proposés et cycle d’instruction sont distincts. La provenance détaillée s’ouvre à la demande.
- **Relations** : voisins directs ou à deux pas, sens entrant/sortant, liens publiés orientés, liste accessible et inspection du sens métier, des conditions, des effets, du périmètre et des preuves. Un lien ne devient jamais un enfant hiérarchique par déduction.
- **Recherche** : noms, repères et textes de la publication consultée, filtres de type, qualification et cycle. Aucun complément lexical provenant du backlog. Ctrl+K et flèches donnent accès aux résultats.
- **Publications et liens** : suivi du catalogue toutes les cinq secondes lorsque l’app est visible et au retour au premier plan ; historiques fixes ; requêtes obsolètes annulées. Un rafraîchissement échoué garde la dernière publication affichée avec un message, puis réessaie. Changer explicitement vers une publication indisponible n’affiche pas les données d’une autre version. Copier le lien épingle la publication consultée. Les anciens liens et les contextes absents sont normalisés.
- **Sources** : document complet, ancres, recherche interne, tableaux, liens documentaires, retour à la source précédente et restitution du focus à la fermeture. Rendu React sûr, sans injection de HTML documentaire.
- **Mobile** : tiroir avec focus contenu, arrière-plan inactif, fermeture par Échap. Aucun historique de visites récentes.

## Iconographie

[Lucide React](https://lucide.dev/guide/react) fournit les SVG importés individuellement. Le [catalogue officiel](https://lucide.dev/icons/) a été consulté le 14 septembre 2026. Les licences des bibliothèques restent celles de leurs paquets : Lucide ISC, React et React Flow MIT, elkjs EPL-2.0.

`app/src/icons.tsx` centralise les correspondances graphiques des 51 éléments actuels. Exemples : entrepôt pour Inventory Management, poignée de main pour Order Promising, registre pour Order Management, balance pour Operational Resource Balancing, itinéraire pour Execution Options, camion pour Execution Commitments and Facts. Les capacités ont des pictogrammes d’action ; les références emploient personnes, contrat, produit, catalogue et réseau. Les univers et groupes de présentation restent différenciés.

Les nouveaux éléments possèdent un repli par type : boîte pour objet métier, feuille pour document, éclair pour événement. Il s’agit uniquement d’une présentation ; aucune icône n’ajoute un sens, une validation ou une relation au JSON. Ces trois types futurs sont vérifiés avec une fixture HTTP, sans les introduire dans la release.

## Code et exploitation

Les modules séparent publication, projection, navigation, arbre, fiches, sources, icônes et rendu graphique. Les anciens `app.js`, `model.js` et `styles.css` sont remplacés ; les archives de présentation ne sont plus lues. Les versions de dépendances sont verrouillées dans `app/pnpm-lock.yaml`.

`pnpm --dir app install --frozen-lockfile`, puis `pnpm --dir app build` produisent `app/dist`. Ce dossier généré n’est pas versionné. Python est le seul processus nécessaire à l’exécution de la livraison compilée ; le lanceur explique une compilation absente. Après modification React, compiler puis recharger la page. Un nouveau JSON publié est lu automatiquement, sans compilation.

Les scripts, CSS et icônes viennent du serveur local. Les attributs de style nécessaires au placement React Flow sont autorisés par une directive CSP dédiée ; les scripts en ligne et l’évaluation dynamique restent interdits. Les sources TypeScript, dépendances, source maps et JSON ne sont pas servis comme fichiers statiques. Les API continuent de contrôler l’hôte, l’origine, les chemins et les empreintes.

Le JavaScript principal fait environ 293 ko, le module React Flow différé 184 ko. ELK, environ 1,43 Mo, n’est chargé que pour disposer des liens ; il explique l’avertissement de taille du build. Le serveur local ne compresse pas ces réponses. Aucun benchmark à très grande échelle n’est revendiqué à partir des 51 éléments actuels.

## Vérification

Les tests de projection utilisent v003 comme référence historique explicite et vérifient séparément le pointeur courant. Les tests de chargement couvrent erreurs, courses entre requêtes, publication historique et suivi automatique. Les tests serveur contrôlent aussi les ressources compilées et les refus d’accès. Le lecteur backlog est comparé au JSON effectivement lu, sans nombre métier figé.

La recette navigateur couvre toutes les cartes des domaines et références publiés, les sources P82/U141/U129, les filtres, les liens historiques, les changements de publication et un échec temporaire simulé. Les scénarios futurs utilisent uniquement des réponses HTTP de test : quatre niveaux supplémentaires et objets/documents/événements transversaux. Les écrans vont de 1920 à 320 px, avec vérification de l’absence de débordement et de la définition visible dans la fiche à 844 px de hauteur.

Commandes reproductibles et organisation du code dans [le README](../app/README.md). Rapports et captures durables dans [le dossier de recette](2026-09-14-atlas-react/verification.json). Les captures illustrent la release consultée, sans publier de contenu métier supplémentaire.

Aucun commit ni push réalisé dans ce refactoring.

Résultat final : **30 tests frontend**, **19 tests Python réussis** et **2 tests de liens symboliques ignorés sur cet hôte** ; **10 groupes de contrôles navigateur** et **17 contrôles d’arbre et de petits écrans** réussis. Aucune exception navigateur, erreur console/CSP ou requête réseau inattendue. Le contrôle `validate_models.py` conclut à zéro erreur.

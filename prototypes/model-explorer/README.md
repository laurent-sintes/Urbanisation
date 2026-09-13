# FLOW Atlas — proposition d’application d’exploration

13 septembre 2026 — réponse à [U104](../../connaissance/01-contributions-utilisateur.md#u104). Proposition produit et prototype d’expérience ; aucune nouvelle structure métier adoptée.

**FLOW Atlas permettrait de comprendre le modèle en changeant progressivement d’échelle, puis en parcourant les liens autour d’une notion.** La recherche offrirait un accès direct à un domaine, une capacité ou une autre notion, tout en conservant le chemin qui permet de la situer. Le nom FLOW Atlas est proposé.

Le modèle évolue dans les registres du projet. L’application en présente une lecture navigable : elle doit exposer ce qui est connu, proposé ou encore ouvert et permettre de retrouver les sources.

## Une expérience d’exploration

| Vue ou interaction | Usage proposé |
| --- | --- |
| **Carte** | Partir de l’ensemble, ouvrir un groupe ou un domaine et découvrir ses éléments. Le zoom est sémantique : le contenu change selon le contexte exploré, avec une vue lisible à chaque étape. |
| **Fil d’Ariane et retour** | Situer l’élément courant, remonter au niveau utile et retrouver le contexte précédent après une recherche ou une traversée de relation. |
| **Liens** | Montrer le voisinage typé de l’élément sélectionné : concepts concernés, informations reçues, objets, documents, faits ou autres capacités liés, selon ce qui est documenté. Ouvrir un voisin recentre l’exploration. |
| **Recherche directe** | Chercher dans les noms, identifiants, définitions, finalités et alias français. Chaque résultat indique son type et son contexte ; le sélectionner mène à sa fiche et à sa place dans la carte. |
| **Fiche de lecture** | Expliquer la Finalité, l’aptitude ou le sens métier, son statut, ses limites et les sources. Les décisions de nom, de rattachement et de liste peuvent avoir des portées différentes. |

Un parcours démonstratif consiste à ouvrir **Order Promising**, sélectionner **Promise Confirmation**, lire sa Finalité puis explorer les liens vers l’engagement, le fait de confirmation et le document associé. Ce dernier voisinage reprend l’[exemple proposé dans la note 24](../../connaissance/24-capacites-objets-et-faits.md#exemple-proposé-confirmer-une-promesse-de-fourniture). Il reste une **illustration**, avec objets, identités, cardinalités et contenus à définir ; la validation de la capacité ne valide pas cet exemple de modèle.

La recherche doit aussi permettre de partir d’un mot français, par exemple « promesse » ou « inventaire », ou d’un identifiant comme D02.e. L’identifiant historique reste attaché à son élément après un changement de rattachement : D02.e ouvre Supply Assignment dans Order Promising.

## Accueillir l’enrichissement du modèle

L’application doit dissocier trois dimensions :

- **Les niveaux de regroupement** servent à organiser la lecture et peuvent s’approfondir sans limite fixée dans le composant de navigation. Leur nom, leur sens et leur adoption viennent du modèle documenté.
- **Les couches d’urbanisation** situent les modèles transactionnel et processus, qui gardent chacun leurs objets et leurs autorités. Le nombre de niveaux visibles dans une carte ne décrit pas le nombre de couches d’architecture.
- **Les relations métier** relient capacités, objets, documents et faits ou événements selon leur sens explicite. Un document ou un événement ne devient pas automatiquement un enfant de capacité. Une notion partagée doit pouvoir être atteinte depuis plusieurs contextes sans dupliquer son identité.

La distinction demandée par Laurent entre objet métier, fait de gestion et document est conservée, ainsi que ses limites détaillées en [U61/U62 et note 24](../../connaissance/24-capacites-objets-et-faits.md). Aucun objet universel, agrégat, séquence capacité → objet → document → événement ou modèle de persistance n’est déduit de cette navigation.

## Périmètre de la démonstration

Le prototype interactif présenté dans la conversation utilise un instantané du 13 septembre 2026, dérivé de la [carte P81 version 0.9](../../connaissance/25-domaines-coeur-et-epreuve-recits.md), état métier du 11 septembre 2026 après U103. Les données sont conservées dans `model-snapshot.json` à côté de cette note. Elles constituent une projection de démonstration ; les registres Markdown restent l’autorité de connaissance.

La lecture d’ensemble présente **sept domaines transactionnels de travail et le groupe Business References**, qui contient cinq références distinctes. Elle conserve les douze repères détaillés et les **36 aptitudes** de P81, avec leurs identifiants historiques. Les cinq références portent cinq ingestions distinctes ; le regroupement n’en fait ni une capacité mère ni un domaine fusionné.

Les **neuf capacités d’Order Promising sont validées en U95**. Les autres éléments conservent leurs statuts particuliers : nom adopté, orientation de rattachement, proposition, réexamen ou frontière ouverte. En particulier, D02 demeure en réexamen, D04/D07 sont à reprendre selon U100, et les attributs ou maîtres du réseau restent ouverts. Le prototype ne doit pas présenter ces statuts comme une validation générale de la carte.

La vue Liens permet d’éprouver une expérience qui s’enrichira au fil du modèle. Sa couverture est partielle ; elle ne constitue pas un inventaire exhaustif des relations. Toute relation illustrative doit être signalée et reliée à sa source. Les faits logistiques reçus gardent leur provenance et leurs autorités ; leur affichage n’étend pas les développements FLOW et ne modifie pas l’autonomie de C-Log.

## Une réalisation simple et évolutive

La recommandation de conception est un **lecteur local utilisable dans un navigateur**, avec une présentation d’application et la possibilité d’étudier son installation ultérieure. À ce stade, l’exploration et la recherche peuvent fonctionner sur un jeu de données local. Une base graphe sur serveur n’est pas nécessaire pour réaliser cette première expérience.

Le moteur de lecture séparerait :

| Élément | Rôle |
| --- | --- |
| Nœuds | Identifiant stable, type, libellé, alias, définition, Finalité, statut et périmètre de modèle. |
| Relations | Origine, destination, type de lien, sens, statut et provenance ; liens de navigation distingués des relations métier. |
| Sources | Registre, identifiant de contribution ou proposition, localisateur, date et portée de la preuve. |
| Vues | Regroupements de navigation acycliques, d’une profondeur libre, sans imposer la même arborescence à tous les usages. |
| Index de recherche | Texte et identifiants indexés localement, avec résultats situés dans leur contexte. |

Un contrôle de cohérence devrait prévenir les références absentes, identifiants dupliqués, cycles dans une hiérarchie de navigation et promotions de statut sans source. Les liens métier peuvent former un graphe ; cette contrainte d’absence de cycle concerne les seules hiérarchies de navigation.

Les futures extractions automatisées depuis les registres, l’édition du modèle, la collaboration et les liens partageables persistants sont des prolongements proposés. Ils ne sont pas réalisés par cette démonstration. Leur conception devra maintenir une autorité de connaissance claire, l’historique et la distinction entre proposition et validation.

## Statut de cette proposition

La demande U104 justifie l’exploration d’une expérience applicative. Elle ne choisit ni technologie, ni produit, ni hébergement, et n’autorise aucune publication implicite. La navigation, le nom FLOW Atlas et l’architecture décrite ici sont proposés à Laurent pour discussion. Les contrôles du prototype sont consignés dans le [journal](../../JOURNAL.md).

## Réalisation de l’aperçu au 13 septembre 2026

Le prototype fonctionne en lecture : navigation de la structure, fil d’Ariane, historique précédent/suivant, visites récentes, voisinage de relations, parcours guidé en quatre étapes et recherche globale. La recherche propose des filtres par type et statut ; « affectation » retrouve Supply Assignment dans Order Promising, et « inventaire » retrouve Stocktaking. La touche Entrée ouvre le premier résultat, Échap ferme la recherche et Ctrl/Cmd+K place le curseur dans le champ lorsque l’aperçu a le focus.

Les relations de démonstration sont limitées : l’exemple de promesse et trois liens de lecture entre domaines/références, avec leurs sources. Un voisinage vide signifie « à documenter dans cet aperçu ». Les objets illustratifs utilisent des repères ILL propres au prototype ; ils ne créent pas d’identifiants canoniques. Les alias de recherche sont des aides lexicales proposées, sans renommage du modèle.

| Fichier | Rôle |
| --- | --- |
| [model-snapshot.json](model-snapshot.json) | Projection datée des douze repères et 36 aptitudes de P81 0.9. |
| [explorer.fragment.html](explorer.fragment.html) | Source de l’interface ; données du snapshot injectées à la génération. |
| [build-preview.py](build-preview.py) | Assemble l’aperçu avec l’instantané ; argument : chemin de destination. |
| [verify-preview.cjs](verify-preview.cjs) | Vérification avec Playwright et un navigateur Edge isolé ; chemin de dépendances adapté à l’environnement local utilisé. |
| `preview.html`, captures PNG | Rendu temporaire de contrôle visuel, sans déploiement. |

Contrôles réalisés : 12 repères, 36 identifiants de capacités uniques et neuf capacités validées ; navigation jusqu’aux ingestions des références ; liens réciproques et historique ; recherche par terme français et identifiant historique ; filtres, clavier et parcours guidé. Quatre largeurs testées, dont une surface d’aperçu de 320 px, avec repli en une colonne ; thèmes clair et sombre inspectés. Aucune erreur JavaScript relevée dans le navigateur de test.

La démonstration n’actualise pas automatiquement son instantané : une évolution des registres exige de régénérer et de contrôler les données. L’écran de provenance expose les repères, le chemin source et les réserves ; l’ouverture des registres depuis une application autonome reste à réaliser.

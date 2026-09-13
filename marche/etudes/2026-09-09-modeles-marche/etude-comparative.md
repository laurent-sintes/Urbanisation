# Comparaison des modèles de référence pour le commerce

Les références de marché convergent sur de grands sujets métier, mais elles ne proposent ni une taxonomie unique ni des niveaux interchangeables. La gestion des articles, l’approvisionnement, le stock, les commandes et les retours réapparaissent dans les contenus retail examinés. Leur place, leur granularité et leur sens changent selon que la référence décrit des capacités, des processus, des composants métier ou des données.

**La conclusion principale est de comparer d’abord des résultats métier et leurs frontières, puis de rapprocher les structures.** Un nom commun constitue un point d’entrée. Une équivalence exige aussi un même objet, une même finalité et un périmètre compatible. Cette étude établit des proximités conceptuelles et des recouvrements argumentés ; elle ne démontre pas d’équivalence générale entre catalogues, ni de conformité de Beaumanoir à l’un d’eux.

## 1. Périmètre et lecture des résultats

La comparaison porte sur dix références : TOGAF, ArchiMate, BIZBOK/Business Architecture Guild, SAP RBA, IBM Component Business Model, Oracle Retail Reference Model, APQC PCF Retail, ARTS ODM, une carte historique de capacités retail Microsoft et le catalogue public de processus Dynamics 365. Les deux références Microsoft sont distinguées car elles n’ont ni la même nature ni la même période. Des documentations fonctionnelles SAP et Microsoft éclairent le cas de l’allocation ; elles ne remplacent pas leurs modèles métier.

Le périmètre d’application est le cœur commerce : référentiels opérationnels, achats, ventes, stocks, allocation, réassort et retours/SAV, avec interfaces logistiques. Les contenus financiers, de planification de saison, de conception produit et de gouvernance sont examinés pour comprendre les frontières des modèles ; leur présence chez un éditeur ne les réintroduit pas dans le périmètre Beaumanoir. L’autonomie du SI C-Log reste une contrainte locale.

Trois degrés de conclusion sont utilisés :

| Conclusion | Ce qu’elle signifie | Ce qu’elle permet |
| --- | --- | --- |
| Proximité de notion | Les définitions portent sur le même type de chose, par exemple une aptitude métier. | Employer un vocabulaire de comparaison commun. |
| Recouvrement de contenu | Des éléments partagent une partie de leur objet ou de leur résultat ; les différences restent explicites. | Construire un rapprochement plusieurs-à-plusieurs et rechercher ses frontières. |
| Équivalence d’éléments | Objet, résultat, inclusions, exclusions et granularité sont compatibles, sur des définitions identifiées. | Substituer un élément à l’autre dans le périmètre déclaré. Aucune équivalence de ce niveau n’est validée ici. |

Une source ne montrant pas un thème ne prouve pas son absence du modèle. Une présentation de 2012 ou 2015 apporte une preuve historique, sans établir le contenu d’une édition actuelle. L’accès à un guide de méthode ne fournit pas, à lui seul, un catalogue de capacités retail.

## 2. Des références de natures différentes

| Référence | Objet principal | Apport réel à la comparaison | Limite structurante |
| --- | --- | --- | --- |
| TOGAF, guide des capacités | Méthode de construction et d’usage des capacités | Définition, décomposition, analyse de l’entreprise | Ne donne pas une nomenclature commerce obligatoire. |
| ArchiMate | Langage et métamodèle d’architecture | Types d’éléments et relations, notamment capacité, comportement et réalisation | Une grammaire ne fournit pas le contenu sectoriel à dessiner. |
| BIZBOK / Guild | Pratiques d’architecture métier et modèles de référence | Objets métier, frontières, décomposition et articulation aux processus | Le guide actuel et un catalogue retail complet n’ont pas été examinés. |
| SAP RBA | Modèles métier de capacités et de processus reliés aux solutions | Une hiérarchie explicite et des éléments sectoriels | Le catalogue complet versionné et ses définitions restent partiellement accessibles. |
| IBM CBM | Composants métier croisés avec des responsabilités | Lecture des compétences, de la gouvernance et de l’exécution | Un composant regroupe des moyens et responsabilités ; il n’est pas automatiquement une capacité élémentaire. |
| Microsoft retail historique | Carte sectorielle présentée comme modèle de capacités | Autre regroupement des sujets retail, utile pour tester les récurrences | Carte historique et libellés, pas catalogue actuel de définitions. |
| Oracle RRM | Modèles de processus métier et techniques, glossaire | Parcours, exceptions, interfaces et liens aux solutions retail | La navigation documentaire n’est pas une pure arborescence de capacités. |
| APQC PCF Retail | Classification sectorielle de processus | Taxonomie de contrôle de couverture et de comparaison des activités | Le contenu détaillé Retail 7.2.1 reste inaccessible dans l’étude. |
| Microsoft Dynamics, catalogue de processus | Parcours métier puis scénarios, réalisation et tests | Contrôle opérationnel détaillé, accessible sur le web | Les niveaux inférieurs décrivent Dynamics ; les aires peuvent refléter des fonctions organisationnelles. |
| ARTS ODM | Modèle de données opérationnelles retail | Sémantique des objets, associations et états | Une entité ou un état ne prescrit pas une capacité ni un service. |

Les distinctions méthode/langage sont explicites chez Open Group. SAP sépare architecture métier et architecture de solution ; Microsoft relie son catalogue à la configuration et aux tests de ses produits. Oracle, IBM et ARTS poursuivent des finalités différentes, que leurs documents décrivent directement.[^1][^2][^3][^4][^5][^6]

## 3. Structure et niveaux : ce qui se compare réellement

### Une profondeur n’est pas une catégorie ni une responsabilité

Quatre coordonnées doivent rester séparées : **le type d’élément**, **sa profondeur de décomposition**, **son classement transversal** et **sa réalisation**. Une capacité peut être de niveau 2, classée dans le cœur métier, mobilisée par plusieurs processus et réalisée par plusieurs composants. Ces propriétés ne sont pas quatre marches d’une même arborescence.

L’atelier Guild distingue ainsi catégorie stratégique/cœur/support et profondeur. Le guide historique TOGAF sépare également classement et décomposition. ArchiMate permet de représenter composition et spécialisation : décomposer une aptitude en parties et distinguer ses variantes sont deux opérations différentes.[^7][^8][^9]

| Référence | Structure et niveaux observés | Interprétation correcte |
| --- | --- | --- |
| SAP RBA — capacités | Enterprise Domain → Business Domain → Business Area → Business Capability | Quatre niveaux visibles, dont un regroupement supérieur d’entreprise ; les feuilles décrivent des capacités. |
| SAP RBA — processus | Processus de bout en bout → module → segment → activité ; regroupements d’entreprise également présents | Une autre structure, reliée aux capacités, pas leur décomposition automatique. |
| TOGAF — G189 historique | Capacités décomposables ; profondeur adaptée au besoin ; classement stratégique/cœur/support distinct | Les trois à six niveaux évoqués sont une pratique, pas une profondeur universelle obligatoire. |
| BIZBOK/Guild — atelier 2019 | Deux axes : catégorie (Tier) et profondeur (Level). Gabarit de niveaux 1 à 6 | Le niveau dépend du détail recherché ; les enfants restent bornés par l’objet du parent dans la méthode présentée. |
| ArchiMate — édition historique examinée | Éléments composables, agrégeables et spécialisables ; vues et domaines d’architecture | Pas de série native de niveaux commerce identiques à ceux de SAP. Les couches d’architecture ne sont pas des profondeurs de capacités. |
| IBM CBM — exemple retail 2005 | Matrice : compétences métier × responsabilités de direction, contrôle et exécution | Les trois lignes sont un axe de responsabilité, pas trois niveaux parent/enfant. |
| Oracle RRM — guide 14.1.1 | L0 secteur retail ; L1 aires de processus ; L2 parcours organisationnels ; L3 parcours métier/système | Niveaux d’information : liens L1 vers L1 possibles ; L3 offre une perspective parallèle à L2. La mention L2.5/3 n’ajoute pas un étage homogène. |
| APQC PCF — convention générale | Catégorie → groupe de processus → processus → activité → tâche | Cinq niveaux de classification ; leur population précise doit être vérifiée dans l’édition sectorielle. |
| Microsoft Dynamics — catalogue public | Processus de bout en bout → aire → processus → scénario → processus système → cas de test | Six niveaux de contenus hétérogènes, du parcours à la mise en œuvre et à la validation. |
| ARTS ODM | Organisation en sujets et vues de données, avec entités, associations, attributs et états | Organisation sémantique et structure relationnelle ; pas une profondeur de capacités. |

La structure propre à la carte Microsoft retail historique est détaillée dans son annexe de preuves ; aucun nombre de niveaux obligatoire n’en est déduit. Les exemples Oracle et APQC doivent être lus avec les éditions et limites d’accès précisées en section 9.[^1][^2][^3][^4][^5][^7][^8][^9][^10][^11]

### Exemple complet chez SAP

| Coordonnée | Stock | Sens |
| --- | --- | --- |
| Enterprise Domain | Supply – Fulfill Demand | Grand regroupement d’entreprise. |
| Business Domain | Supply Chain Execution | Domaine métier. |
| Business Area | Inventory Management | Aire regroupant plusieurs capacités. |
| Business Capability | Physical Inventory | Une aptitude identifiée dans l’extrait. |

La promesse de commande et la gestion d’entrepôt sont des aires voisines de la gestion des stocks. Dans une carte locale, « Gestion des stocks » pourrait recevoir le nom de domaine ; ce serait une convention locale reliée à l’aire SAP. Le changement de vocabulaire ne démontre ni une différence de métier ni une équivalence de contenu.[^1]

### Exemple de changement de niveau sans disparition du métier

Microsoft documente en février 2025 le déplacement des processus de rappel/retour depuis le traitement des dossiers vers la commande/encaissement. Des regroupements relatifs aux prix et coûts produit passent aussi à un niveau inférieur. Un comparateur fondé seulement sur le numéro de niveau signalerait à tort une disparition ou une nouveauté métier. Il faut conserver le type de relation, la version et la raison du déplacement.[^12]

## 4. Équivalences, recouvrements et faux amis

| Rapprochement | Conclusion de l’étude | Frontière à conserver |
| --- | --- | --- |
| Capacité dans TOGAF, Guild, SAP et ArchiMate | Proximité de notion : une aptitude, distincte de son déroulement et de sa réalisation. | ArchiMate peut aussi représenter l’aptitude d’une personne ou d’un système ; le périmètre n’est pas nécessairement le seul métier de l’entreprise. |
| Domaine local / aire SAP / capacité de haut niveau Guild | Comparaison possible de périmètre, aucune équivalence par position. | Un regroupement thématique et une capacité composite doivent être qualifiés séparément. |
| Capacité SAP / composant IBM | Recouvrement possible de fonction ou de résultat. | IBM embarque une lecture des responsabilités et des moyens ; le même thème peut se répartir dans sa matrice. |
| Capacité / élément de classification APQC | Proximité fonctionnelle possible, selon la définition. | Le PCF est une taxonomie : sa hiérarchie ne décrit pas à elle seule l’ordre d’exécution. |
| Capacité / parcours Oracle ou Microsoft | Relation d’utilisation à établir ; parfois proximité aux niveaux les plus agrégés. | Les parcours ajoutent déroulement, événements et passages de responsabilité ; leurs étapes ne deviennent pas automatiquement des capacités. |
| Modèle de capacités / ARTS | Correspondance entre une aptitude et les objets ou faits qu’elle utilise. | L’objet « stock » ne décide pas s’il faut une ou plusieurs capacités pour sa tenue, sa disponibilité ou ses engagements. |
| Inventaire physique SAP / comptage et ajustement Microsoft | Recouvrement de résultat : rapprocher constat et quantité enregistrée. | Le périmètre du comptage, les autorisations, corrections et effets sur les engagements restent à comparer. |
| Protection SAP / allocation Inventory Visibility Microsoft | Recouvrement de finalité : préserver une quantité pour un groupe de demandes. | Fonctionnalités de produits ; critères, horizons, formules et consommation ne sont pas déclarés identiques. |
| Retours / service client / logistique inverse | Sujets reliés, avec intersections. | Dossier de réclamation, droit au retour, réception physique et conséquence commerciale sont des responsabilités différentes. |

Le papier Guild sur l’articulation métier/processus documente des relations plusieurs-à-plusieurs et observe que certains niveaux agrégés de classifications de processus peuvent ressembler à des regroupements fonctionnels. Cela justifie une comparaison par définition, sans requalifier globalement un catalogue de processus en catalogue de capacités.[^13]

Le cas de l’allocation est particulièrement trompeur : un seul nom peut couvrir répartition vers les magasins, protection d’un groupe, plafond de confirmation ou affectation à une commande. Les libellés de cartes sont insuffisants pour conclure à une équivalence de mécanisme.[^14][^15]

## 5. Contenu commerce : les récurrences effectivement observées

Les tableaux utilisent les mêmes thèmes de comparaison, construits pour l’étude. Ils ne constituent pas un nouveau catalogue de capacités Beaumanoir. Les cellules montrent une présence documentaire ; elles ne mesurent ni une couverture complète ni la qualité d’un modèle. « Non établi » signifie que la sélection consultée ne fournit pas la preuve nécessaire.

### Cartes de capacités et de composants métier

Dans ce tableau, les entrées IBM et Microsoft 2012 sont principalement des **libellés sans définitions détaillées**. SAP offre une preuve directe de rattachement pour le stock ; les mentions « domaine » et « extrait indexé » indiquent une preuve moins fine. Les traductions françaises servent au repérage.[^1][^2][^11][^17]

| Thème | SAP RBA | IBM CBM 2005 | Microsoft retail 2012 |
| --- | --- | --- | --- |
| Articles et produits | Domaine de gestion des produits ; référentiel article détaillé non établi | Articles et produits | Référentiel produit |
| Fournisseurs et achats | Domaine achats/approvisionnement ; parcours de sourcing en complément | Sourcing et commandes d’achat | Sourcing et collaboration fournisseur |
| Stock et inventaire | Réceptions, mouvements, sorties, inventaire physique | Gestion des stocks, selon plusieurs positions de la matrice | Stocks entreprise et magasin |
| Disponibilité et allocation | Contrôles de disponibilité et d’allocation, sous la promesse de commande | Allocation ; disponibilité détaillée non établie | Plan d’allocation ; promesse non définie |
| Réassort | Feuille non établie dans la sélection | Réassort | Réassort magasins et centres d’exécution |
| Commande client | Gestion et suivi de commande : définitions citées dans un extrait indexé | Gestion des commandes | Vente/encaissement et exécution repérés ; cycle complet de commande non établi |
| Exécution logistique | Entrepôt et transport, aires distinctes | Entrepôt et transport | Préparation et expédition |
| Retours physiques | Retours mentionnés dans le support client ; traitement physique non établi | Logistique inverse | Non établi |
| SAV et réclamations | Support/demandes de service : extrait indexé | Service client | Service client magasin et centre d’appels |

Les occurrences IBM relatives aux stocks et commandes apparaissent dans plusieurs contextes de sa matrice. Leurs libellés ne suffisent pas à conclure qu’il s’agit du même objet, d’un doublon ou de stocks à tenir séparément. Les annexes conservent les positions et les limites de définition.

### Contrôle par les processus et les données

Les contenus Oracle ci-dessous sont ceux du **guide historique 14.1.1**. Les pages Microsoft mêlent description de parcours et liens vers des fonctions de produit, signalés dans les cellules. Pour ARTS, une vue repérée au sommaire donne une preuve de thème ; seuls les passages indiqués comme lus autorisent une analyse sémantique détaillée.[^3][^5][^16][^18]

| Thème | Oracle RRM — processus | Microsoft Dynamics — processus et réalisation | ARTS ODM — données |
| --- | --- | --- | --- |
| Articles et produits | Non qualifié dans l’extrait sélectionné | Cycle de vie, enrichissement et catégories produit | Vues 01000 articles et 01015 habillement repérées |
| Fournisseurs et achats | Achats, fournisseurs et accords | Fournisseurs, contrats, demandes et commandes d’achat | Vues 01500 article/fournisseur, 02120 commandes, 02130 réception repérées |
| Stock et inventaire | Stock et réception entrepôt | Mouvements, ajustements et comptage tournant | Vue 02010 lue : comptage et ajustements |
| Disponibilité et allocation | Allocation ; définition ATP non établie | Dates/promesse et fonction d’allocation de quantités | Vue 07620 lue : effets sur stock physique/disponible ; pas définition d’un moteur ATP |
| Réassort | Réassort | Plans de réapprovisionnement | Documents d’approvisionnement repérés ; calcul du besoin non établi |
| Commande client | Exemple de vente B2B | Commandes multicanales, B2B et B2C | Vue 07600 commande et effets dans 07620 |
| Exécution logistique | Réception et circuits de traitement | Entrées, préparation, sorties et transport | Vues livraison, commande distribuée et expédition repérées |
| Retours physiques | Exemple de retour marchandise | Retours clients dans les entrées ; fournisseurs dans les sorties et achats | Couverture détaillée non examinée |
| SAV et réclamations | Non qualifié dans l’extrait sélectionné | Dossiers clients/salariés, traitement et résolution | Couverture détaillée non examinée |

TOGAF et ArchiMate ne sont pas renseignés dans ces matrices de contenu, car ils apportent une méthode et une grammaire. Les pratiques publiques Guild ne prouvent pas le contenu de son catalogue retail. Le fichier sectoriel APQC Retail 7.2.1 n’a pas été consulté ; la carte Microsoft hébergée par APQC ne peut pas lui être substituée.

### Ce qui revient, et ce que « partout » voudrait dire

Le **stock et ses changements**, les **articles/produits**, les **approvisionnements**, la **vente/commande** et l’**exécution** forment le faisceau de récurrences le plus visible. Les retours et le service client sont également récurrents, mais davantage dispersés et inégalement documentés. Ce sont des thèmes communs à plusieurs références, avec des niveaux de preuve variables ; aucune liste complète de capacités présente dans toutes les références n’est démontrée.

L’analyse suggère trois constantes utiles : des objets métier durables, des aptitudes qui produisent ou modifient leur état, et des comportements qui articulent ces aptitudes pour obtenir un résultat. Les modèles mettent l’accent sur des composantes différentes de cet ensemble. Cette lecture constitue une synthèse analytique ; elle n’est pas une taxonomie commune publiée par les organismes.

On ne peut pas conclure que tous les modèles distinguent explicitement **protection**, **disponibilité**, **réservation** et **promesse**. On ne peut pas davantage déduire qu’une même capacité « gérer les retours » couvre partout la décision commerciale, la manutention et le dossier de réclamation. Les écarts observés portent souvent sur le découpage d’un besoin partagé, plutôt que sur sa présence ou son absence.

## 6. Trois cas qui expliquent les différences fondamentales

### Stock, disponibilité et engagement

SAP RBA distingue tenue/mouvements/inventaire, promesse de commande et entrepôt. Le catalogue Microsoft rapproche au sein d’une aire le maintien des niveaux, les politiques, le réassort, les mouvements et les ajustements. ARTS décrit les objets et les effets : dans la vue 07620, la commande modifie la disponibilité tandis que l’expédition affecte le stock physique. Ces références se recouvrent sur le sujet, mais elles répondent à des questions différentes.[^1][^16][^18]

Une comparaison utile distingue donc : la quantité enregistrée ; la preuve d’un changement ; le constat physique et l’écart ; la quantité mobilisable selon un contexte ; l’engagement pris envers une demande. Ce sont des axes d’analyse proposés. Ils permettent de comprendre pourquoi un regroupement Microsoft peut couvrir plusieurs aptitudes de notre socle, tandis qu’une vue ARTS décrit des faits utilisés par plusieurs d’entre elles.

La séparation stock physique/disponible chez ARTS apporte une sémantique concrète. Elle ne doit pas être transformée en constat sur Storeland, UR ou les mécanismes de réservation de GBM. L’autorité sur chaque état, son délai de mise à jour et l’effet d’une commande restent à établir localement. Le schéma de données externe ne tranche pas la frontière entre les deux urbanisations.

### Allocation et protection

SAP documente la protection de quantités destinées à des groupes et, séparément, un contrôle de limites d’allocation sur la confirmation. Microsoft Inventory Visibility documente une allocation virtuelle à des groupes, distincte des réservations liées aux transactions. La finalité de protection d’un groupe est comparable ; les deux réalisations ne sont pas déclarées substituables.[^14][^15]

| Question discriminante | Pourquoi elle change le rapprochement |
| --- | --- |
| À qui la quantité est-elle destinée ? | Un magasin, un canal, un groupe de clients et une ligne de commande ne sont pas la même maille. |
| Quel résultat est tenu ? | Un plan de distribution, une protection, un plafond et une réservation ont des effets différents. |
| Quelles ressources sont prises en compte ? | Stock présent, entrées attendues et ressources alternatives ne permettent pas la même promesse. |
| Quand la règle prend-elle effet ? | Calcul amont, contrôle de demande, confirmation et consommation sont des moments distincts. |
| Que provoque une révision ? | Modifier les paramètres n’implique pas nécessairement de réaffecter les commandes déjà engagées. |

Pour Beaumanoir, ces questions éclairent MAP, les protections marque/canal et l’allocation Boardriders. Elles ne prouvent ni le fonctionnement d’ARun ni une repriorisation commerciale dans GBM. La présence d’une fonction chez un éditeur ne lève aucune réserve sur les objets republiés par MAP ou les engagements déjà pris.

### Retour physique, retour commercial et dossier SAV

IBM sépare service client et logistique inverse. Oracle présente un parcours de retour. Microsoft répartit les retours entre commande, réception et achat ; son catalogue distingue aussi les dossiers de réclamation. Le besoin partagé traverse donc plusieurs regroupements, même lorsqu’un intitulé paraît global.[^2][^3][^12][^16]

L’aptitude à **autoriser un retour** n’est pas équivalente à celle de **constater sa réception**, ni à celle de **résoudre une réclamation**. Un processus peut les mobiliser successivement ou seulement en partie. Un échange commercial peut aussi produire plusieurs faits : autorisation, entrée de marchandise, nouvelle demande, ajustement des engagements. Cette décomposition sert à tester les frontières ; elle ne constitue pas un parcours Sarenza confirmé.

Le changement de classement documenté chez Microsoft illustre un point central pour la base évolutive : conserver l’identité du besoin et la justification du lien permet de suivre un déplacement dans le modèle externe. Copier le chemin hiérarchique dans l’identifiant local rendrait ce suivi plus fragile.

## 7. Conséquences pour l’urbanisation Beaumanoir

Les modèles de marché appuient la distinction entre aptitudes, déroulements et réalisations. Ils ne prescrivent pas deux couches autonomes ayant chacune leur modèle, leurs objets et leur persistance. Cette architecture reste une orientation propre à Beaumanoir ; la comparaison doit l’éclairer sans lui substituer les couches d’un langage ou les modules d’un produit.

Le terme marché « capacité » est généralement plus large que la sélection transactionnelle recherchée : il peut couvrir stratégie, pilotage, service ou organisation. La carte du socle doit donc être explicitement une **sélection de capacités métier génériques du commerce**, avec liens vers les besoins de la couche processus et les responsabilités externes.

| Besoin de la cartographie | Référence la plus directement utile pour ce besoin dans le corpus | Usage proposé |
| --- | --- | --- |
| Définir une capacité et sa décomposition | TOGAF et pratiques Guild | Décrire objet, résultat, inclusions/exclusions et capacités enfants. |
| Représenter les relations | ArchiMate, si une notation est retenue | Distinguer composition, spécialisation, mobilisation et réalisation. |
| Éprouver une structure explicite de capacités | SAP RBA | Comparer les quatre niveaux et des éléments définis ; compléter les définitions avant adoption. |
| Tester un autre regroupement retail | IBM et Microsoft retail historique | Rechercher thèmes oubliés, responsabilités et différences de maille ; tenir compte des dates. |
| Éprouver les parcours et exceptions | Oracle RRM et Microsoft Dynamics | Relier les activités aux aptitudes nécessaires ; conserver les variantes organisationnelles et applicatives. |
| Contrôler une taxonomie de processus | APQC | Utiliser la convention générale ; acquérir le contenu sectoriel avant d’en prétendre la couverture. |
| Préciser les objets et effets du stock | ARTS ODM | Comparer données et faits de gestion sans dériver mécaniquement les capacités des entités. |

Aucun classement global des références n’est calculé : elles n’ont pas le même objet et les profondeurs d’accès diffèrent. La proposition est d’utiliser une grammaire commune de comparaison, puis de tester les mêmes scénarios sur plusieurs références.

## 8. Proposition de fonctionnement pour la base évolutive

**Conserver les capacités locales indépendamment des chemins externes.** Pour chaque rapprochement, tenir l’identifiant local, la version externe, le type de l’élément, son chemin, sa définition ou son absence, le résultat partagé, les différences et le statut de preuve. Le chemin est une propriété versionnée ; il ne constitue pas l’identité métier locale.

**Comparer au moins quatre dimensions avant de conclure :** objet traité, résultat obtenu, périmètre couvert et granularité. Ajouter les règles, états, autorités et exceptions lorsque l’on veut dépasser une piste de libellé. Un élément externe peut couvrir plusieurs aptitudes locales ; une aptitude locale peut être éclairée par plusieurs sources de natures différentes.

**Éprouver trois scénarios communs** : comptage avec écart de stock, concurrence de demandes sur un stock protégé, retour nécessitant une décision commerciale puis une réception. Ces scénarios sont proposés pour tester les modèles. Ils devront être précisés avec les pratiques GBM, Boardriders et Sarenza avant tout arbitrage local.

**Distinguer les décisions à venir.** Choisir le nom des niveaux, choisir le contenu des capacités et choisir leur réalisation sont trois décisions séparées. L’étude suffit pour écarter un alignement automatique des niveaux ; elle ne suffit pas pour déclarer une hiérarchie principale ou figer les frontières des 36 candidats.

Les résultats sont reliés au [catalogue des références](../../catalogue.md), aux [éléments examinés](../../elements.md) et aux [comparaisons avec Beaumanoir](../../comparaisons.md). Les notes de preuves détaillent les passages retenus : [cadres de capacités](notes-cadres-capacites.md), [SAP/IBM](notes-sap-ibm.md), [Oracle/APQC/ARTS et Microsoft historique](notes-oracle-apqc-arts.md), [Microsoft Dynamics](notes-microsoft.md).

## 9. Versions, accès et portée de l’étude

État documentaire du 9 septembre 2026. Les dates ci-dessous qualifient la preuve ; elles ne forment pas un classement de maturité des modèles.

| Référence | Édition ou état réellement examiné | Limite déterminante |
| --- | --- | --- |
| TOGAF | Guide G189 de 2018, document primaire sur miroir tiers ; édition G211/version 2 identifiée sur page officielle | Copie historique non comparée au fichier actuellement distribué ; guide version 2 non lu. |
| ArchiMate | Spécification 3.1 de 2019 sur miroir tiers ; tutoriel communautaire hébergé par Open Group | Ne démontre pas la rédaction normative actuelle de la spécification 3.2. |
| BIZBOK/Guild | Atelier officiel 2019 et papier de position 2014 ; notice des ressources BIZBOK 15.0 | Le guide 15.0 complet et un catalogue retail actuel ne sont pas examinés. |
| SAP RBA | Cours publics sans édition de catalogue ; exemples visuels ; compléments éditoriaux 2024–2026 | Certains compléments ne sont accessibles que sous forme d’extraits indexés ; aucune exhaustivité retail/fashion. |
| IBM CBM | Publication G510-6163-00 de 2005, figure retail | Exemple historique ; définitions détaillées des cases absentes. |
| Microsoft retail | Carte marquée V1 du 15 septembre 2012, dans une présentation Microsoft hébergée par APQC | Texte extrait ; emboîtement visuel exact et définitions non établis. |
| Oracle RRM | Guide public 14.1.1 de juin 2015 ; fiche publique actuelle hétérogène | Fiche : 24.2.402.0/2024 en page 1, 26.1.202.0/2026 en page 2. Ne pas attribuer les exemples 2015 à la bibliothèque actuelle. |
| APQC | Convention générale ©2018 ; notice Retail 7.2.1 du 28 avril 2023 | Fichier Retail derrière formulaire, non consulté. Aucun identifiant sectoriel reconstitué. |
| ARTS ODM | Introduction, sommaire et vues 02010/07620 de l’édition 7.3 | Les autres vues sont surtout repérées au sommaire ; date de publication non établie. |
| Microsoft Dynamics | Pages publiques portant diverses dates 2024–2026 ; schéma de six niveaux ; changements de février 2025 | La vue générale annonce des titres alignés sur juillet 2026 avec des schémas parfois antérieurs ; aucun export homogène complet examiné. |

Les limites les plus susceptibles de changer une conclusion de contenu sont les définitions natives SAP, les modèles détaillés Oracle actuels, le fichier APQC Retail et un modèle Guild retail accessible. Leur consultation pourrait affiner ou invalider des rapprochements de maille. Elle ne devrait pas être remplacée par une ressemblance de noms.[^19][^20][^21][^22]

## 10. Sources

Les appels numérotés relient les constats aux sources. Toutes ont été consultées ou recontrôlées pour l’état documentaire indiqué ; les accès limités, miroirs et simples repérages sont signalés. Les traductions et les tableaux comparatifs sont des synthèses, non des reproductions de catalogues.

[^1]: SAP Learning, [Discovering the Reference Architecture Content](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), sections sur les modèles de capacités/processus et leurs exemples ; [Defining Business Architecture](https://learning.sap.com/courses/intelligent-enterprise-architecture-fundamentals/defining-business-architecture), carte générale. Cours sans édition de catalogue identifiée ; texte et images sélectionnées consultés.
[^2]: IBM Business Consulting Services, [Component business models: Making specialization real](https://public.dhe.ibm.com/software/emea/dk/frontlines/g510-6163-component-business-models.pdf), G510-6163-00, 2005, pages PDF 7–11, figure 6 page PDF 11/page imprimée 9. Document public, figure contrôlée visuellement.
[^3]: Oracle, [Retail Reference Model User Guide](https://docs.oracle.com/cd/E64536_01/rrl/pdf/1411/rrm-1411-ug.pdf), release 14.1.1, juin 2015 ; pages imprimées 5–7 et 12–19 pour les niveaux, 12–14 et 18–21 pour achats/stock/exécution, 26 pour le retour. Guide historique public.
[^4]: Microsoft, [Introduction to the business process catalog for Dynamics 365 apps and services](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/about), sections sur les six niveaux et les identifiants ; mise à jour affichée 8 janvier 2026.
[^5]: OMG/ARTS, [Introduction and overview, ODM 7.3](https://www.omg.org/retail-depository/arts-odm-73/introduction_and_overview.htm) et [sommaire des vues](https://www.omg.org/retail-depository/arts-odm-73/hmcontent.htm). Structure et repérage des objets, sans lecture exhaustive des vues.
[^6]: The Open Group, [How the ArchiMate Language and the TOGAF Standard Complement Each Other](https://help.opengroup.org/hc/en-us/articles/32115987894930-How-the-ArchiMate-Language-and-the-TOGAF-Standard-Complement-Each-Other), §§1–3, page d’assistance officielle ; distinction méthode/langage.
[^7]: The Open Group, [Business Capabilities, G189 — copie sur hébergement tiers](https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf), juin 2018, §§2.1, 3 et 3.2, pages imprimées 2–3 et 6–10. Document primaire historique ; identité avec le fichier actuellement distribué non contrôlée.
[^8]: Business Architecture Guild, [Reference Model Workshop](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf), 20 juin 2019, pages PDF 15–21. Atelier officiel : objets/actions, frontières, catégories et profondeurs ; pas le guide actuel intégral.
[^9]: The Open Group, [ArchiMate 3.1 Specification, C197 — copie sur hébergement tiers](https://governance.foundation/assets/frameworks/archimate/ARCHIMATE_v3_1_specifikacia.pdf), novembre 2019, §§7.1, 7.3 et 7.6 ; [tutoriel communautaire ArchiMate 101](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/), vues, domaines et métamodèle. La norme historique et le tutoriel communautaire ont des statuts distincts.
[^10]: APQC, [Introduction to the Process Classification Framework](https://www.apqc.org/sites/default/files/files/PCF%20Collateral/Intro%20to%20PCF%20-%20FINAL.pdf), ©2018, figure 1 et pages PDF 1–2. Convention générale des niveaux et identifiants ; ne prouve pas les feuilles Retail 7.2.1.
[^11]: Microsoft, [présentation sur l’architecture retail hébergée par APQC](https://www.apqc.org/sites/default/files/files/RetailPCF-Microsoft.pdf), pages PDF 15–16, carte marquée V1 9.15.12. Libellés consultés par extraction textuelle ; imbrication visuelle non certifiée. Référence distincte du PCF.
[^12]: Microsoft, [What’s new or changed in the business process catalog February 2025](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/about-whats-new-2025-february), changements sur dossiers, produits et commandes. Déplacements et changements de niveau effectivement décrits.
[^13]: Business Architecture Guild, [Business Architecture / BPM Alignment Position Paper](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/docs/batobpmalignmentpositionpape.pdf), octobre 2014, pages PDF 12–19. Relations capacités/processus et distinctions de décomposition.
[^14]: SAP Learning, [Supply Protection](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-) et [Check Against Allocation](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-check-against-allocation), introductions fonctionnelles S/4HANA aATP, éditions produit inconnues ; voir aussi la [note locale SAP-stock](../../sap-stock.md).
[^15]: Microsoft, [Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), sections finalités, allocation virtuelle et distinction avec réservation ; mise à jour affichée 13 août 2025. Fonction produit, pas catalogue de capacités.
[^16]: Microsoft, [articles et produits](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/design-to-retire-introduction), [fournisseurs et achats](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/source-to-pay-areas), [flux de stock](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/inventory-to-deliver-areas), [commandes](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/order-to-cash-areas-overview), [dossiers et réclamations](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/case-to-resolution-introduction). Sections thématiques et dates détaillées dans l’[annexe Microsoft](notes-microsoft.md).
[^17]: SAP EA Knowledge Base, [Sales Order Management in CX – Part 1](https://community.sap.com/t5/enterprise-architecture-knowledge-base/application-decisions-for-sales-order-management-in-cx-part-1/ta-p/14274899), décembre 2025 ; [Service Request Management](https://community.sap.com/t5/enterprise-architecture-knowledge-base/application-decisions-for-service-request-management/ta-p/13898197), octobre 2024, édité février 2026 ; [Sourcing Process](https://community.sap.com/t5/enterprise-architecture-knowledge-base/application-choices-and-decisions-for-the-sourcing-process/ta-p/13602349), février 2024. Extraits éditoriaux indexés consultés, ouvertures directes refusées ; ni pages complètes ni export RBA examinés. Localisateurs dans l’[annexe SAP/IBM](notes-sap-ibm.md).
[^18]: OMG/ARTS ODM 7.3, [vue 02010 : comptage et ajustements](https://www.omg.org/retail-depository/arts-odm-73/logical_02010.htm) et [vue 07620 : commandes et contrôle du stock](https://www.omg.org/retail-depository/arts-odm-73/logical_07620.htm). Passages narratifs effectivement lus.
[^19]: Oracle, [Retail Reference Model — fiche publique](https://www.oracle.com/a/ocom/docs/industries/retail/retail-reference-model-ds.pdf), pages PDF 1–2. Mentions de versions et années divergentes, décrites dans la section 9 ; bibliothèque actuelle non acquise.
[^20]: Business Architecture Guild, [Free Resources](https://learning.businessarchitectureguild.org/free-resources), notice de l’introduction/glossaire BIZBOK 15.0 et conditions d’accès ; guide complet non consulté.
[^21]: APQC, [PCF Retail 7.2.1](https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-retail-pdf-version-721), notice du 28 avril 2023 et formulaire d’accès ; fichier sectoriel non consulté.
[^22]: Microsoft, [vue générale du catalogue de processus](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/overview), avertissement sur titres de juillet 2026 et schémas antérieurs ; The Open Group, [guide fourni pour l’examen TOGAF](https://help.opengroup.org/hc/en-us/articles/32109993154066-What-Open-Book-Is-Provided-With-the-TOGAF-Enterprise-Architecture-Part-2-Exam), mise à jour du 3 mai 2026, identifiant G211/version 2 repéré, corps non examiné.

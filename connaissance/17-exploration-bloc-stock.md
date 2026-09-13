# Explorer le bloc stock : états, disponibilité et engagements

Apports [U26](01-contributions-utilisateur.md#u26) et [U27](01-contributions-utilisateur.md#u27), 9 septembre 2026. Analyse A18, proposition P66, [CMP020](../marche/comparaisons.md#cmp020). Cette exploration prolonge la [vue du socle](16-capacites-socle-transactionnel.md) et l’[étude comparative](../marche/etudes/2026-09-09-modeles-marche/etude-comparative.md). Les regroupements restent proposés ; les 36 CAP conservent leur définition et leur statut.

## Ce que propose Laurent

Un bloc Inventory réunit visibilité de tous les stocks, disponibilité par usage et modification des allocations/états. Le message annonce deux sous-blocs mais en liste trois : l’analyse suit ces trois sujets. Le stock virtuel/logique est ensuite évoqué comme fonction supplémentaire possible, sans définition arrêtée.

La démarche part d’une ressource durable du commerce et cherche les aptitudes nécessaires pour la connaître, déterminer ses usages et agir. C’est une entrée pertinente pour le socle. La réserve porte sur la cohérence des sous-blocs : « Management » regroupe toutes les modifications alors que les deux premières rubriques décrivent des sujets métier. Une séparation générale consultation/modification couperait la tenue d’un même objet entre plusieurs blocs. La visibilité peut aussi concerner les disponibilités et les engagements.

## Trois familles proposées

| Famille proposée | Question métier | Exemples de capacités à préciser | Candidats existants mobilisés |
| --- | --- | --- | --- |
| États et mouvements de stock | Quelles quantités sont connues, où, sous quel statut, et quels faits expliquent leur évolution ? | Tenir les positions ; enregistrer réception, transfert et sortie ; constater un comptage et régulariser un écart ; exposer une vue consolidée avec provenance et fraîcheur. | CAP004/CAP005 ; Q011/Q013/Q065. Le périmètre actuel de CAP004 reste magasin. |
| Disponibilité par usage | Quelle quantité peut être utilisée pour une finalité, dans un contexte et à une échéance donnés ? | Déterminer l’éligibilité ; calculer et expliquer une disponibilité pour vente, réassort ou autre usage défini ; tenir compte des restrictions, protections et engagements applicables. | CAP006 ; Q012/Q038. Aucun calcul local existant présumé. |
| Allocations, protections et engagements | À quel usage ou demande une quantité est-elle affectée, protégée ou engagée ? | Tenir les affectations/protections applicables ; réviser une allocation ; réserver, confirmer, consommer ou libérer un engagement selon son cycle. | CAP007/CAP008/CAP009/CAP010/CAP035 ; Q018/Q030–Q032/Q049. Ne pas internaliser d’avance le calcul amont MAP. |

La modification de l’état de stock appartient ici à la première famille ; celle d’une protection ou d’un engagement à la troisième. Ce sont des choix d’analyse autour des objets et résultats. Ils ne prescrivent ni trois applications, ni trois bases, ni des frontières définitives. Une capacité complète peut lire, décider, enregistrer un fait et publier son résultat.

La disponibilité est une réponse contextualisée ; l’engagement est une décision tenue vis-à-vis d’une demande ou d’un usage. Un service peut articuler les deux, par exemple vérifier puis réserver. Leur distinction sémantique ne préjuge pas du contrat ni des garanties d’exécution à retenir.

## Tous les stocks : dimensions et autorités

Entrepôt et magasin décrivent des lieux ou types de lieux ; transit décrit une situation logistique ; blocage en douane décrit un statut ou une restriction. Ces dimensions peuvent se superposer : un même stock peut être en entrepôt et sous douane. Les traiter comme des compartiments toujours disjoints ferait compter plusieurs fois les mêmes unités.

La maille doit permettre de distinguer article/unité de mesure, localisation ou segment de transit, statut, propriétaire, détenteur et éventuel bénéficiaire d’une affectation, selon le besoin. Un approvisionnement attendu, un stock détenu par un tiers et une quantité physiquement reçue doivent rester identifiables ; la date et la fiabilité d’une information ne sont pas accessoires à son usage. Ce sont des dimensions candidates, pas un schéma de données arrêté.

L’indépendance de l’organisation signifie que la capacité n’est pas définie par l’organigramme. Elle peut néanmoins avoir besoin de faits métier tels que le propriétaire, les droits d’usage et le lieu. La visibilité transverse ne donne pas automatiquement autorité de modification : le stock C-Log peut être connu via ses contrats, tout en conservant son autorité d’exécution. Distinguer demande de mouvement, confirmation du mouvement et copie de consultation. Les responsabilités actuelles restent à documenter.

## Stock virtuel ou logique : une notion à qualifier

**Statut historique de cette exploration U26/U27 :** U76 fournit ensuite la distinction retenue pour le vocabulaire local : physique = existence réelle, logique = états métier, virtuel = quantité calculée disponible. Lire [C53](04-corrections.md#c53) et [TER040–TER042](19-glossaire-metier.md#distinction-courante-des-stocks-et-frontière-proposée-u76u77). Les quatre interprétations ci-dessous conservent la recherche initiale et ne remplacent pas cette convention ; Q066 est partiellement répondue.

« Stock virtuel/logique » n’est pas encore une capacité définie. Un objet ou une représentation peut être nécessaire sans imposer un bloc supplémentaire. Quatre interprétations sont à distinguer :

| Sens possible, proposé pour l’analyse | Exemple | Conséquence possible |
| --- | --- | --- |
| Vue consolidée | Regrouper les positions de plusieurs lieux dans une vue entreprise | Capacité de visibilité dans la première famille ; conserver la provenance et éviter les doublons. |
| Quantité calculée | Stock utilisable pour un usage à une date, à partir des états et règles | Relève de la disponibilité ; un approvisionnement attendu demeure distinct du stock reçu. |
| Pool logique affecté | Quantités protégées pour le web ou un groupe de demandes | Objet avec règles, solde et consommation dans la troisième famille ; créer, réviser, consulter ou libérer le pool sont des capacités candidates. |
| Offre de ressources externes ou futures | Quantité annoncée par un fournisseur, utilisable sous certaines conditions | Qualifier source, droits, horizon et engagement possible ; ne pas assimiler cette offre à un stock détenu ni étendre la vente nominale GBM aux approvisionnements futurs. |

La dernière interprétation est une hypothèse de sens, sans usage local déclaré. L’intérêt d’une famille supplémentaire dépendrait d’une responsabilité métier propre : objet identifiable, règles et cycle de vie distincts, résultats que les autres familles ne couvrent pas déjà. La question [Q066](06-questions.md#q066) conserve cette exploration ouverte.

## Exemple pour éprouver le modèle

Exemple fictif pour un SKU, un instant et une unité communs. On suppose des pools exclusifs et une politique web limitée à son pool, sans emprunt entre pools ni approvisionnement futur. Ces règles ne décrivent pas GBM.

| Quantités physiques recensées, ventilées sans recouvrement | Quantité |
| --- | --- |
| Bloquées pour l’usage étudié | 20 |
| Pool web : déjà réservées | 10 |
| Pool web : encore engageables | 20 |
| Autres quantités éligibles, sans réservation | 50 |
| Total physique | 100 |

Le stock physique est de 100, dont 80 éligibles dans cet exemple. Le pool web contient 30, **dont** 10 déjà réservées : sa quantité encore engageable est 20. Les 30 du pool et les 10 réservées ne s’ajoutent pas au stock physique ; ce sont des affectations et un sous-ensemble. Une nouvelle réservation de 5 fait passer les réservées web à 15 et l’encore engageable à 15, sans changer le total physique. Une expédition ultérieure produit un autre fait et doit aussi solder ou consommer l’engagement selon son cycle, sans double déduction.

Cette grille distingue position, disponibilité calculée, pool logique et engagement. Elle ne propose pas une formule universelle : protections et réservations peuvent se recouvrir, et deux disponibilités calculées pour des usages concurrents ne sont pas nécessairement additionnables.

## Différence avec le marché

| Référence examinée | Appui au découpage | Différence à conserver |
| --- | --- | --- |
| SAP RBA | Gestion des stocks distincte de la promesse ; contrôles de disponibilité et d’allocation dans cette dernière | Le bloc Inventory proposé ici rassemble des responsabilités que SAP répartit entre plusieurs aires. Aucun niveau SAP précis ni équivalence de sous-blocs n’en découle. |
| Microsoft Inventory Visibility | La solution décrit une allocation virtuelle à des groupes et la distingue de la réservation liée aux transactions | « Visibility » ne signifie pas consultation seule. Le pool logique est un objet de fonction produit, pas la preuve d’un quatrième domaine de capacités standard. |
| ARTS ODM 7.3 | La vue 07620 distingue effets de commande sur disponibilité et d’expédition sur stock physique | Appui sur les données et effets métier ; ne fixe ni une taxonomie de capacités ni les règles de réservation Beaumanoir. |

Sources reconsultées le 2026-09-09 : [SAP Learning, exemple RBA](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), section *Business Capability Model Example*, ELM014 ; [Microsoft, allocation Inventory Visibility](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), sections *Allocation virtual pool* et distinction avec réservation, ELM028 ; [ARTS, vue 07620](https://www.omg.org/retail-depository/arts-odm-73/logical_07620.htm), ELM024. Éditions, dates affichées et limites d’accès antérieures restent celles des fiches MKT04/MKT14/MKT08. L’extrait SAP ne fournit pas toutes les définitions des feuilles ; la fonction Microsoft et le modèle de données ARTS ne deviennent pas des catalogues métier.

Ce regroupement local est cohérent avec la recherche d’un socle générique, sous réserve de définir ses frontières. Le prochain travail est de décrire, pour chaque capacité candidate, résultat, objet/états, règles, autorité et effets, puis contrat — avec une correspondance marché argumentée. P66 propose cette exploration, sans modifier aujourd’hui le catalogue CAP.

## Complément allocation et réservation

U28/U29 approfondissent le vocabulaire dans la [comparaison SAP/Microsoft](../marche/allocation-reservation-sap-microsoft.md). P67 distingue les résultats métier et les modes d’exécution ; Q067 garde la transition historique précise ouverte. L’enveloppe initiale d’un pool, son solde et sa consommation doivent être distingués, notamment pour lire les mesures Microsoft. Aucune définition CAP modifiée.

## Affinement par les politiques et la promesse

[U30/U31](18-politiques-engagement-gbm-brd.md) précisent les comportements nécessaires à BRD et le principe de réservation GBM. P69 propose de situer le réexamen des promesses dans Order Promising : la famille exploratoire allocations/protections/engagements sert à étudier les interactions, sans imposer que la promesse appartienne au même bloc que la tenue du stock. Rattachement SAP corroboré dans la documentation de solution, feuille RBA précise non établie.

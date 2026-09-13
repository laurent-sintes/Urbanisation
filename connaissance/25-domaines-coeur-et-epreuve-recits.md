# Domaines cœur : première carte éprouvée par les récits

**Statut documentaire après U106–U112 (13 septembre 2026) :** cette note conserve la source narrative P81 0.9 et ses analyses. Le modèle courant fait désormais autorité dans le [backlog JSON](../modeles/backlog/model.json) et la [release pointée](../modeles/release/current.json). Ne pas maintenir ce tableau comme un second catalogue éditable. Les formulations et limites historiques restent des preuves ; voir [C70](04-corrections.md#c70).

11 septembre 2026 — version de travail 0.9, après U103 ; origine : 10 septembre 2026, version 0.1 ; [U63/U64](01-contributions-utilisateur.md#u63), F165/F166, A39 et [P81](05-propositions.md#p81). **Carte de travail : sept domaines transactionnels de travail et le groupe Business References réunissant cinq références ; douze repères détaillés et 36 capacités recensées, dont les neuf capacités d’Order Promising validées par Laurent en U95.** Les rattachements de protection et réservation à D01, et d’affectation à D03, suivent U74/U75 ; les autres frontières détaillées restent à éprouver. D02 est en réexamen. Order Promising conserve son rôle de domaine reconnu en U52 ; sa liste est validée en U95, avec des frontières détaillées encore ouvertes.

Cette note est la vue de travail courante de P81. Elle fait évoluer les [options U51](22-options-domaines-socle.md) à la lumière des précisions OMS/Supply, du périmètre FLOW et des objets des deux couches. Le [registre des 36 CAP](09-capacites-candidates.md) conserve ses fiches et leur provenance ; les rapprochements ci-dessous permettent de discuter leurs reformulations, regroupements et compléments. Les repères stables D01–D13 et leurs suffixes identifient des éléments de cette proposition, pas de nouvelles fiches du registre CAP ni des identifiants de marché. Le statut des capacités de la carte est distingué : D03 validé en U95, autres contenus selon leurs validations ou propositions antérieures.

**Audit marché U99 disponible :** [achats/ventes, référentiels, prix et revue des 34 capacités](../audits/2026-09-11-modele-marche-achats-ventes-referentiels.md). L’audit porte sur la version 0.6 à 34 capacités ; ses constats datés sont conservés. U100 confirme depuis l’autonomie article (D08.d) et réoriente la revue des commandes vers les documents d’autorisation de la Supply générique. D04/D07 restent à refondre ; prix appliqué et consommé contractuel restent ouverts. Voir [la note U100](26-supply-documents-autorisations.md), C66 et CMP058. Les points d’accueil des récits ne valent pas couverture exhaustive.

## Lecture de la proposition

Une capacité décrit **ce que sait faire l’entreprise indépendamment de son organisation et de ses outils**. Un domaine réunit des problèmes liés, leurs connaissances et leurs règles. La carte vise le socle transactionnel ; les dossiers de réassort, de vente ou de SAV appartiennent à l’autre modèle, qui possède ses propres objets.

Les aptitudes sont exprimées au niveau métier. Leur position ici ne décide pas de leur réalisation dans un nouveau développement : la logistique est hors développement FLOW et en adhérence ; les frontières de décision doivent être éprouvées. Finance, contrôle de gestion, conformité, design produit et planification de saison restent hors domaines du périmètre. Les moteurs et contrats décrivent des moyens et des relations entre domaines.

La vue synthétique distingue les domaines transactionnels de travail du groupe de présentation **Business References**, retenu selon l’accord contextuel de Laurent U103. Le groupe rassemble les références ; il ne constitue pas une capacité mère ni un domaine métier fusionné.

| Domaine de travail ou groupe de présentation | Problème ou Finalité | Statut |
| --- | --- | --- |
| **D01 — Inventory Management** | Quels stocks sont connus, comment évoluent-ils et quelles protections préservent leurs usages ? | Visibilité et protection étayées ; rattachement de Supply Protection orienté par U74, maille et inventaire à approfondir. |
| **D02 — Resource Availability and Commitments** | Où décrire le calcul de disponibilité et l’évolution des engagements après les rattachements U74/U75 ? | Domaine en réexamen ; deux aptitudes conservées, autonomie non justifiée à ce stade. |
| **D03 — Order Promising** | Quelles quantités et dates peut-on engager envers un besoin, avec quelles ressources affectées, puis réviser ? | Neuf capacités validées en U95 ; besoins Boardriders explicites, réalisation et règles détaillées à préciser. |
| **D04 — Commercial Commitments** | Quels engagements propres aux commandes lient les parties, et comment évoluent-ils ? | Commandes distinctes des Agreements U98 ; revue réorientée U100 vers les documents d’autorisation de Supply générique, avec D07. |
| **D05 — Operational Resource Balancing** | Quels manques ou excédents apparaissent par rapport aux besoins et objectifs opérationnels ? | Réassort étayé ; redistribution et réalisation FLOW en frontière. |
| **D06 — Execution Options** | Où une prestation est-elle admissible et quelle capacité de réalisation reste mobilisable ? | Cas magasin étayé ; autonomie logistique et autorités à préserver. |
| **D07 — Execution Commitments and Facts** | Quel résultat de réalisation est attendu, engagé, constaté ou encore attendu ? | Interface décrite ; contenu exact des engagements et retours de faits à préciser. |
| **Business References — groupe de présentation** | Disposer des références externes des parties, contrats, articles, catalogues et réseau nécessaires aux opérations. | Regroupement retenu U103 ; cinq modèles et ingestions distincts, voir le détail ci-dessous. |

**Détail du groupe Business References :**

| Référence et repère conservé | Problème couvert | Statut du contenu |
| --- | --- | --- |
| **D09 — Party / Role** | Quelles parties et quels rôles de référence sont reçus pour les opérations ? | Référentiel maître externe ; une seule capacité d’ingestion, U97. |
| **D11 — Agreement** | Quels contrats de référence et conditions particulières sont reçus pour commander et promettre ? | Référentiel maître externe ; une seule capacité d’ingestion, U97/U98. |
| **D08 — Product Reference** | Quelle référence article autonome permet de reconnaître le même SKU dans plusieurs catalogues ? | Autonomie confirmée U100 ; ingestion seule dans la continuité U97, libellé proposé. |
| **D12 — Catalog** | Quels catalogues, prix et zones d’application sont reçus pour les opérations ? | Référentiel maître externe ; une seule capacité d’ingestion, U97. |
| **D13 — Fulfillment Network** | Quels points et relations du réseau de réalisation sont connus et utilisables par la Supply ? | Référentiel demandé U102 ; ingestion et contenu détaillé proposés, maître à préciser. |

Les douze repères restent disponibles pour la traçabilité ; leur préfixe D ne prescrit plus leur affichage au même niveau. L’ordre ne définit aucun enchaînement de processus. D02 reste en réexamen ; D01–D03 constituent le noyau le mieux documenté. Le groupe de présentation ne fusionne ni modèles ni autorités, et ne fixe pas une hiérarchie Univers/Domain Area. D08.a–c et D10 restent retirés ; les noms et définitions détaillés gardent leurs statuts propres.

## Capacités proposées et frontières

Les colonnes de résultat donnent une définition courte de l’aptitude, complétée par le problème et les limites du domaine. Les objets cités restent des pistes de modèle métier ; ils ne fixent pas des agrégats. Les libellés sont en anglais après U66. Inventory Management, Order Promising, Product Information Management et Party Management réemploient des noms de marché ; leur usage ne vaut pas équivalence complète. Supply Protection et Supply Assignment reprennent les aptitudes nommées par Laurent en U67. Les autres formulations sont des traductions locales proposées. Les définitions et Finalité restent en français. La [correction C48](04-corrections.md#c48) conserve les 44 noms précédents.

<a id="d01-stocks"></a>

### D01 — Inventory Management

**Vue consolidée après U81 — 11 septembre 2026.** P81 version 0.4 ; précisions U68–U77, A42–A51 et [C50](04-corrections.md#c50)/[C51](04-corrections.md#c51). Six aptitudes sont rattachées à D01 dans P81. Une [version à cinq capacités](#proposition-de-cinq-capacités-d01-u83), P82, est proposée après U83, sans fusion adoptée. Supply Protection et réservation conservent leurs repères historiques D02.b/D02.c, qui ne désignent plus leur domaine courant ; les autres repères sont inchangés. La maille reste à éprouver. Establish inventory positions reste en réexamen après U82. Stocktaking est retenu pour D01.d selon U86 ; voir [la revue des noms](#noms-des-capacités-de-stock-revue-u82) et C58 pour la provenance.

**Réexamen U78 :** Laurent hésite sur la réservation. Son rattachement D01 issu de U75 reste affiché comme option en discussion, sans nouveau déplacement. La [comparaison SAP/Microsoft](../marche/allocation-reservation-sap-microsoft.md#réservation-et-frontière-inventory-management-order-promising-u78), ELM070–ELM072/CMP042, montre que Microsoft réserve du présent et du commandé non reçu, et que SAP décrit des quantités réservées par Supply Assignment. Une séparation réservation/affectation strictement disjointe ne se déduit pas du marché ; [C54](04-corrections.md#c54).

**Finalité proposée :** disposer d’une connaissance fiable, partageable et traçable des stocks physiques, de leurs états logiques et des ressources futures attendues, préserver les usages retenus et enregistrer les quantités engagées, afin de fonder les décisions d’approvisionnement, de vente et d’exécution sur des faits et des règles cohérents.

**Problème du domaine :** quels stocks physiques et ressources futures sont connus, où se trouvent-ils ou sont-ils attendus, quels états logiques qualifient les stocks physiques, quels faits expliquent leurs variations et quelles protections préservent les usages retenus et quelles quantités sont réservées ? Les stocks peuvent être en magasin, entrepôt, transit, sous douane ou chez un tiers. Lieu, détenteur et propriétaire sont des dimensions métier utiles ; leurs valeurs organisationnelles ne définissent pas les capacités. Un approvisionnement attendu reste distinct du stock reçu. U79 précise le potentiel contractuel, le planifié et les fournitures en cours ; U80 confirme que la notion de stock futur est gérée dans D01 et D03. Voir [la représentation du futur](#stock-futur-potentiel-et-ressources-attendues-u79), sans attribution automatique de toutes les autorités sources à D01.

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D01.a | **Establish inventory positions** : déterminer les quantités de stock physique et leurs états logiques par article, lieu, détenteur et propriétaire lorsque ces dimensions sont pertinentes, en distinguant les ressources futures attendues. | Disposer d’une connaissance exploitable des ressources. |
| D01.b | **Record inventory facts** : qualifier les faits qui font évoluer les quantités physiques et les états logiques, notamment entrées, sorties, changements d’état et consommations. | Expliquer les variations et leur provenance. |
| D01.c | **Provide a consolidated inventory view** : présenter les positions physiques, leurs états logiques et les ressources futures connues dans une vue cohérente, sans double comptage, avec source, périmètre et fraîcheur. | Permettre une lecture commune des stocks distribués. |
| D01.d | **Stocktaking** : établir les quantités constatées par comptage, les confronter aux quantités enregistrées, qualifier les écarts et établir les corrections justifiées. | Fiabiliser les quantités enregistrées — Inventory accuracy. |
| D02.b | **Supply Protection** : établir et appliquer les quantités ou limites d’usage destinées à des groupes, avec leur validité. | Préserver les possibilités d’approvisionnement des usages retenus. |
| D02.c | **Reservation** : établir un engagement de quantité pour un besoin identifié, dont les usages concurrents doivent tenir compte. | Donner effet à un engagement de ressource. |

#### Proposition de cinq capacités D01 — U83

**Vue de discussion recommandée : [P82](05-propositions.md#p82), issue de U83/F187/A57.** Les titres courts ci-dessous proposent une lecture plus simple ; les définitions explicitent ce que sait faire l’entreprise. Cette alternative réunit les anciennes D01.a et D01.b sans perdre leurs résultats. Elle n’est pas encore adoptée : P81 conserve ses six lignes D01 et les références historiques. Correspondances et limites en [CMP045](../marche/comparaisons.md#cmp045).

**Finalité :** connaître et actualiser les stocks physiques, leurs états logiques et les ressources futures, fiabiliser cette connaissance et maîtriser les protections et engagements de quantités.

| Nom proposé | Capacité décrite | Finalité | Raccordement aux repères actuels |
| --- | --- | --- | --- |
| **Inventory Tracking** | Enregistrer les faits de stock et en établir les effets sur les quantités physiques et les états logiques ; suivre les ressources futures connues et leurs évolutions, en distinguant actuel et attendu. | Disposer d’un état du stock à jour et expliquer son évolution. | Réunion proposée D01.a + D01.b. |
| **Inventory Visibility** | Fournir une lecture cohérente des stocks physiques, de leurs états logiques et des ressources futures dans les différents lieux et périmètres, avec provenance et fraîcheur, sans double compte. | Permettre aux décisions de s’appuyer sur une connaissance partagée. | D01.c. |
| **Stocktaking** | Établir les quantités constatées par comptage, les confronter aux quantités enregistrées, qualifier les écarts et établir les corrections justifiées. | Fiabiliser les quantités enregistrées — Inventory accuracy. | D01.d ; la définition conserve rapprochement et correction. |
| **Supply Protection** | Définir et appliquer les quantités ou limites d’usage protégées pour des groupes ou usages, avec leur validité et leurs règles de consommation. | Préserver les ressources destinées aux usages retenus. | Repère historique D02.b, rattaché à D01. |
| **Reservation** | Engager, ajuster ou libérer une quantité pour un besoin identifié, en faisant porter ses effets sur les usages concurrents. | Donner effet à l’engagement de ressource durant son cycle. | Repère historique D02.c, rattaché à D01, frontière en réexamen. |

**Noms retenus après U86 :** Reservation est choisi en U84 et Stocktaking en U86 par Laurent, le 2026-09-11. Stocktaking conserve comptage, rapprochement et corrections justifiées, avec Inventory accuracy comme Finalité. Le nom Counting reste une alternative historique et un terme Microsoft. La fusion D01.a/b et les frontières détaillées demeurent proposées ; C58 conserve les anciens libellés.

**Pourquoi réunir D01.a et D01.b :** établir un état du stock et le faire évoluer par les faits décrivent ici une même aptitude durable. Le regroupement rend explicite la continuité, sans effacer les faits de gestion ni leurs documents. La portée Inventory Tracking dépasse le suivi des lots, colis ou transports ; ce nom est une proposition locale, pas un libellé exact SAP ou Microsoft. Si deux aptitudes distinctes sont finalement démontrées, leurs références antérieures restent disponibles.

**Frontières :** Inventory Tracking établit et actualise la connaissance ; Inventory Visibility la rend exploitable dans une vue commune. Leur séparation reste à éprouver. Counting ne signifie pas pilotage des campagnes ou développement de l’exécution physique logistique par FLOW : les constats et autorités en adhérence restent distingués. Supply Protection conserve le libellé retenu ; Reservation, retenu en U84, abrège le titre précédent sans trancher ses liens avec Supply Assignment. Ajuster/libérer explicite le cycle déjà discuté, sans déplacer toute D02.d. Le stock virtuel calculé et la promesse restent dans D03 ; le futur reste connu dans D01 et mobilisé dans D03.

#### Noms des capacités de stock — revue U82

**Statut historique U82, complété par U86 :** Stocktaking est désormais retenu pour D01.d. Laurent contestait Establish inventory positions et le nom proposé Physical Inventory. Les noms historiques de la table restent visibles pour la traçabilité ; les options ci-dessous ne sont pas encore adoptées. Sources vérifiées le 2026-09-11 : [ELM075](../marche/elements.md#elm075), [ELM076](../marche/elements.md#elm076), [CMP044](../marche/comparaisons.md#cmp044), correction [C56](04-corrections.md#c56).

| Objet à nommer | SAP : libellé et nature | Microsoft : libellé et nature | Proposition locale |
| --- | --- | --- | --- |
| D01.a — connaître et actualiser les quantités et états | Managing Stocks by Quantity : tâche expliquée dans la documentation produit, avec quantités libres, en contrôle qualité, réservées et commandées non reçues. | On-hand inventory : notion exposée par la vue On-hand list. Maintain inventory levels : business process area plus large, incluant mouvements, comptages et ajustements. | **Manage inventory quantities**, adaptation du libellé SAP ; conserver physique, états logiques et ressources futures dans la définition. |
| D01.d — constater, comparer et régulariser | Physical Inventory, expliqué par stock-taking et comparaison aux quantités enregistrées. | Count inventory : processus ; Counting : journal permettant comptage et rapprochement des différences. | **Count and reconcile inventory** ; **Stocktaking** comme intitulé court possible si la définition conserve le rapprochement et les corrections justifiées. |

**Finalité et portée :** Inventory accuracy exprime la fiabilité/exactitude recherchée. La formulation naturelle serait Inventory Accuracy Assurance plutôt que accuracy ensurment, mais ce nom local serait plus large que le comptage : prévention, vérification des faits, rapprochements et correction pourraient y contribuer. Pour la maille actuelle, privilégier un résultat explicite de comptage et rapprochement, et placer « fiabiliser les quantités enregistrées par confrontation aux constats » dans Finalité. Truth est déconseillé : il n’explicite ni le contrôle effectué ni les limites d’un constat. L’analyse est proposée, pas une règle de marché.

**Granularité :** le nom proposé pour D01.a ne valide pas sa séparation de D01.b ; les mouvements et changements d’état font précisément évoluer les quantités. Stocktaking nomme l’aptitude de comptage ; campagnes, tâches et outils sont ses réalisations, et le comptage physique logistique reste en adhérence FLOW. Aucun nouveau niveau ni capacité ajouté.

**Lecture métier des six aptitudes :**

- **D01.a — Positions connues :** établir combien de stock est connu, où et dans quel état à une date donnée. Exemple fictif : 100 unités de l’article X dans le dépôt A, dont 20 bloquées. La définition des dimensions et des états est un sujet lié ; configurer la structure dans un outil ne fournit pas ces positions à lui seul.
- **D01.b — Faits et évolution :** enregistrer les faits qui font évoluer les positions et en établir les effets. Une sortie de 5 unités fait passer 100 à 95 ; une levée de blocage change l’état sans augmenter le total. Un changement d’état ou de propriété peut exister sans déplacement physique.
- **D01.c — Visibilité :** rendre les stocks compréhensibles dans une vue cohérente. Deux copies décrivant les mêmes unités ne s’additionnent pas. Une vue peut présenter positions, protections et disponibilités sans prendre autorité sur toutes leurs règles.
- **D01.d — Stocktaking, nom retenu en U86 :** constater les quantités présentes, comparer aux positions enregistrées et régulariser les écarts justifiés. Exemple fictif : 100 unités enregistrées et 97 comptées ; après vérification de l’écart, ajustement justifié de −3 avec provenance. Un comptage est un constat à qualifier. Enregistrer les quantités constatées précise le sens de « comptabiliser les données réelles » en U72, sans étendre le domaine à la valorisation financière. L’extension à d’autres rapprochements reste à qualifier ; le noyau ne désigne pas toute activité de qualité de données.

- **Supply Protection — repère historique D02.b, désormais dans D01 :** définir et appliquer les protections de quantités pour des bénéficiaires ou usages, avec leurs conditions de validité et de consommation. Exemple fictif : protéger 40 unités pour un canal sans modifier les 100 unités physiques connues. La règle métier est distincte du paramétrage de son moteur ; les modalités de priorité et la portée sur le futur restent à préciser.

- **Reservation — repère historique D02.c, désormais dans D01 :** engager une quantité pour un besoin identifié, avec un effet sur ce qui reste utilisable par les demandes concurrentes. La réservation ne déplace pas physiquement les biens. Son articulation avec l’affectation, la consommation et la libération reste à détailler ; le nom Reservation est retenu selon U84, avec ancien libellé conservé en C57.

**Clarification U81 :** le stock logique est explicitement inclus dans D01.a/b/c ; Physical Inventory ne désigne que la capacité de constater et rapprocher le physique. Les noms et repères sont conservés. La précision de D03.a et les formulations D01 sont des clarifications locales, avec historique [C55](04-corrections.md#c55) et correspondances actualisées en CMP043 ; aucune équivalence détaillée supplémentaire n’est établie.

**Correspondances de marché — [ELM068](../marche/elements.md#elm068), [CMP039](../marche/comparaisons.md#cmp039) et [CMP040](../marche/comparaisons.md#cmp040) et [CMP041](../marche/comparaisons.md#cmp041).** Les noms et contenus rapprochés ne valent pas équivalences complètes. Les comportements de produit éclairent les aptitudes sans les réduire à leurs réalisations ; la hiérarchie RBA reste distincte.

| Capacité locale | SAP : noms et contenu proches | Microsoft : noms et contenu proches |
| --- | --- | --- |
| D01.a — Establish inventory positions | Managing Stocks by Quantity : quantités, états et stocks spéciaux, dans le cours produit. | On-hand inventory, dimensions et mesures décrits par Inventory Visibility. |
| D01.b — Record inventory facts | Goods Receipt, Goods Issue, Stock Transfer, Transfer Posting : variations et changements de qualification, parfois sans déplacement physique. | Inventory journals : transactions de stock, notamment Movement et Transfer. Ce sont des moyens documentés de réalisation. |
| D01.c — Provide a consolidated inventory view | Aperçu de stock et listes repérés ; consolidation de tous les SI avec non-double-comptage non démontrée par ces passages. | Inventory Visibility : visibilité multisource et multilieu ; garanties locales de source, fraîcheur et non-double-comptage à préciser. |
| D01.d — Stocktaking, retenu en U86 | Physical Inventory, feuille RBA attestée en ELM014 ; comptage, confrontation et corrections expliqués dans le cours produit. | Counting et Inventory adjustment : rapprochement du constat et des quantités enregistrées, puis ajustement. |
| Supply Protection — rattachée à D01 en U74 | Supply Protection : quantités protégées pour des groupes, horizons, restrictions et consommation dans la documentation aATP. | Inventory Visibility inventory allocation : pools alloués et consommation protégée, distinction avec réservation. |
| Reservation — rattachée à D01 en U75 | Reservation pour mouvements planifiés en Inventory Management, et quantités réservées par Supply Assignment dans aATP (ELM070/ELM072) ; pas d’équivalence complète ni rang RBA exact établi. | Réservations ERP sur présent et commandé non reçu ; précision progressive possible. Inventory Visibility soft reservations pour l’engagement quantitatif et sa compensation (ELM071). |

Sources examinées le 11 septembre 2026 : [SAP, stock et inventaire](https://learning.sap.com/courses/inventory-management-and-physical-inventory-in-sap-s-4hana/defining-inventory-management-and-physical-inventory-1), [Microsoft, Inventory Visibility](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility), [Microsoft, Inventory journals](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-journals). Éditions et passages dans ELM068 ; pas de nouvelle vérification externe en U73. Après U74, [SAP Supply Protection](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-) et [Microsoft Inventory Visibility allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation) sont reconsultés ; limites dans CMP040.

Au niveau du domaine, **Inventory Management** est une Business Area SAP, sous Supply Chain Execution et Supply – Fulfill Demand ; chez Microsoft, le nom désigne un module de solution. Le module et le cours SAP couvrent aussi des sujets répartis ailleurs dans notre proposition, dont réservations ou valeur. Un nom partagé ne fixe pas les frontières ; voir [SAP RBA](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content).

**Autres modèles :** [TMF687 Stock Management](https://www.tmforum.org/open-digital-architecture/open-apis/stock-management-api-TMF687/v4.0) rapproche représentation, consultation et ajustement du stock, avec une réservation qui déborde le D01 actuel ; ses notifications ne démontrent pas nos faits de gestion et le guide complet n’est pas lu. ARTS ODM 7.3, vue 02010, éclaire comptage et ajustement au niveau des données (ELM024, preuve antérieure). Aucun correspondant précis BIZBOK/Guild n’est établi dans notre corpus : Asset Management dans le support public de 2019 est trop large (ELM066). Cela ne prouve pas l’absence de capacités dans ces modèles.

**Frontières et points à éprouver :**

- **D01.a / D01.b :** les faits et leurs effets maintiennent précisément les positions connues. La distinction peut décrire état et évolution d’une même aptitude ; la nécessité de deux capacités n’est pas établie. Les repères restent conservés pendant le réexamen. La distinction a/c entre connaissance et visibilité commune reste également à éprouver par ses résultats métier.
- **Supply Protection :** rattachée à D01 selon U74, avec provenance [C51](04-corrections.md#c51) et comparaison [CMP040](../marche/comparaisons.md#cmp040). Le calcul de disponibilité D02.a, conservé en réexamen, doit tenir compte des protections et réservations D01 ; la promesse D03 mobilise ces résultats. La frontière détaille les responsabilités métier sans imposer appels, moteurs ou composants. Le calcul amont des politiques et leur portée sur le futur restent à préciser ; aucune internalisation automatique de la planification de saison.
- **Types de stock — distinction U76 :** stock physique = biens existant réellement ; stock logique = états métier de ces biens ; stock virtuel = quantité considérée disponible selon un calcul. [TER040–TER042](19-glossaire-metier.md#distinction-courante-des-stocks-et-frontière-proposée-u76u77) et [C53](04-corrections.md#c53) remplacent l’emploi antérieur indifférencié de logique/virtuel. Exemple utilisateur : 100 pièces, réparties en 60 libres, 20 réservées, 10 allouées, 5 bloquées, 5 défectueuses. La partition est celle de l’exemple ; pour des états croisant qualité et engagement, les règles de combinaison restent à formaliser. Une vue consolidée expose ces informations sans les définir à elle seule.
- **Partage physique/logique/virtuel — U81 :** Inventory Management gère les stocks physiques et leurs états logiques ainsi que la connaissance des ressources futures U79/U80. Order Promising détermine le stock virtuel mobilisable pour un usage et un horizon, puis l’utilise pour établir une promesse quantité/date. Les calculs qui établissent des positions ou états dans D01 ne sont pas exclus ; une vue D01 peut aussi exposer un résultat issu de D03 sans en prendre autorité. Le sens U76 de quantité calculée est conservé, avec son usage de promesse explicité. La nécessité d’une capacité de disponibilité distincte de D03.a reste à éprouver ; Q066 reste ouverte sur les règles, objets et autorités. Voir [C55](04-corrections.md#c55).
- **Réservation / affectation — U75 :** réservation en D01, Supply Assignment en D03. Engager une quantité vis-à-vis d’usages concurrents et établir quelles ressources couvrent une demande sont des résultats distincts selon Laurent. Leur cohérence et leurs autorités sont à préciser, sans deux objets ou séquence obligatoires. Une même opération métier peut mobiliser les deux aptitudes.
- **Exemple fictif de disponibilité :** sur 100 unités présentes, 20 sont bloquées et 30 sont déjà réservées parmi les 80 utilisables ; dans ce cas simple, sans autre protection, contrainte ou futur, 50 restent réservables. Ce résultat est une lecture du stock selon ces règles, pas un troisième stock. Si protections et réservations se recouvrent, les soustraire indépendamment serait incorrect ; aucune formule universelle n’est adoptée.
- **Fiabilité et autorités :** deux systèmes indiquant 100 et 97 ne démontrent pas un écart physique. Vérifier dates, périmètres, unités, faits et autorités avant de distinguer correction d’une copie et ajustement métier. La qualité de l’information est une finalité commune ; datahub et golden data ne définissent pas D01.d ni une autorité centrale sur C-Log. Les constats ne se réduisent pas aux mouvements externes.
- **Réalisation :** comptage et mouvements logistiques ne deviennent pas des développements FLOW. Organisation des campagnes, tâches et validations à relier au modèle processus ; logistique hors développement de la plateforme et en adhérence. Valorisation financière en interface.

**Objets et faits à examiner :** position, mouvement, constat, ajustement, protection et réservation ; détention et propriété chez un tiers. **Provenance :** U03/U04/U26/U48/U68–U77 ; CAP004/CAP005 ; Q065 pour les pratiques et autorités d’inventaire, Q069 pour les pertes, consommations et reliquats du cas à façon. D01.d demeure une aptitude plausible étayée par le marché, dont les pratiques locales restent à préciser. Les anciennes formulations et leurs clarifications sont conservées en C48/C50 et A42–A46.

<a id="d02-disponibilité-et-engagements-de-ressources"></a>

### D02 — Resource Availability and Commitments

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D02.a | **Determine resource availability for a given use** : apprécier les quantités admissibles à un horizon, compte tenu des états, attentes, protections et engagements. | Évaluer ce qui peut être mobilisé dans une situation donnée. |
| D02.d | **Adjust resource commitments** : réviser, transférer ou libérer les quantités affectées selon les décisions autorisées. | Maintenir des affectations cohérentes avec les besoins et les ressources. |

**Audit de frontière U87/U88 :** [P83](05-propositions.md#p83) propose de résorber les deux formulations ci-dessus dans les aptitudes D01/D03 concernées ; aucune suppression ni renumérotation appliquée. Le domaine demandé par Laurent pour la revue est Order Promising (D03).

**Statut après U75 : domaine en réexamen.** Protection et réservation ont rejoint D01 ; Supply Assignment a rejoint D03. Deux aptitudes restent ici à titre de trace de travail, sans justifier à elles seules un domaine autonome. La disponibilité pourrait être une détermination au service d’Inventory Visibility ou de la faisabilité de promesse ; D02.d doit être répartie ou reformulée selon ce qui est modifié (réservation, affectation ou autre engagement). Aucun déplacement supplémentaire ni suppression d’identifiant n’est décidé.

Les définitions U67 de Supply Protection et Supply Assignment comme aptitudes métier restent acquises ; Allocation Run décrit une réalisation. U75 distingue réservation et affectation par leur résultat. Les objets, cardinalités, cycles et autorités qui relient les deux restent à préciser, sans séquence ou composants obligatoires.

**Provenance :** U10/U26/U30/U31/U67 ; CAP006–CAP010. **Marché :** ELM016–ELM018/ELM028/ELM031/ELM032/ELM034/[ELM067](../marche/elements.md#elm067), CMP021–CMP023/[CMP038](../marche/comparaisons.md#cmp038) ; appuis de comportements SAP/Microsoft, avec adaptation locale du regroupement. Stock virtuel/logique reste une notion à qualifier (Q066), pas un onzième domaine déduit du vocabulaire.

<a id="d03-promesse-de-fourniture"></a>

### D03 — Order Promising

**Statut : neuf capacités validées par Laurent le 11 septembre 2026, U95/F201, P83.** Quatre capacités d’action et cinq capacités de décision sont retenues dans ce domaine. Ces deux catégories sont des lectures de contribution, pas deux niveaux hiérarchiques supplémentaires ni des étapes imposées. Les frontières détaillées et les autorités opérationnelles restent à préciser.

**Finalité :** proposer, établir et maintenir des engagements de fourniture réalisables, en quantité et en date, en mobilisant les ressources présentes ou futures et les possibilités d’acheminement.

**Espace problématique :** que pouvons-nous promettre pour satisfaire une demande, sous quelles conditions, avec quelles ressources et quelle solution de fourniture ? Comment maintenir cette promesse lorsque la situation évolue ? Les demandes peuvent notamment provenir de la vente et du réassort, sans imposer un objet Demande universel ni reproduire les parcours dans le socle.

<a id="proposition-de-présentation-u87u88"></a>

#### Capacités d’action validées — U95

| Repère | Capacité et résultat métier | Finalité |
| --- | --- | --- |
| D03.a | **Promise Proposal** : construire une proposition de fourniture précisant quantités, dates, conditions et alternatives possibles, à partir des ressources et possibilités de réalisation. | Faire naître une proposition de promesse réalisable. |
| D03.b | **Promise Confirmation** : établir les quantités et dates promises, en distinguant la part confirmée de celle qui ne l’est pas. | Donner un engagement explicite au destinataire. |
| D02.e | **Supply Assignment** : affecter, réaffecter ou libérer des ressources admissibles présentes ou futures pour couvrir des demandes ou engagements. | Assurer la couverture des demandes par des ressources identifiées. |
| D03.c | **Promise Revision** : réexaminer les promesses lorsque ressources, demandes, dates ou priorités changent et établir les modifications autorisées. | Maintenir des engagements cohérents avec la situation et les priorités applicables. |

Le repère historique D02.e est conservé pour Supply Assignment, rattachée à D03 depuis U75. Proposition, engagement et couverture effective ne sont pas synonymes. L’articulation précise entre proposition et engagement reste à décrire par les règles ; aucun ordre obligatoire entre confirmation et affectation. Réexaminer peut maintenir une promesse ; réaffecter peut en préserver quantité/date. Le cas Boardriders U30/U31 nécessite de pouvoir réexaminer selon les priorités, sans preuve de configuration installée.

<a id="capacités-de-décision-ajoutées-à-lexploration-u91"></a>

#### Capacités de décision validées — U95

| Repère | Capacité et résultat métier | Finalité |
| --- | --- | --- |
| D03.d | **Allocation Eligibility Decision** : décider quelle quantité une demande peut consommer au regard des allocations, protections et droits applicables. | Respecter les droits d’accès aux ressources. |
| D03.e | **Fulfillment Source Decision** : choisir la source ou la combinaison de sources permettant de satisfaire la demande. | Fonder la promesse sur des origines de fourniture admissibles. |
| D03.f | **Fulfillment Route Decision** : choisir la chaîne d’acheminement jusqu’à destination : étapes, points de passage, modes et services, selon les contraintes de délai, de capacité et de coût. | Fonder la promesse sur un acheminement réalisable. |
| D03.g | **Product Substitution Decision** : décider quel produit de remplacement est admissible pour satisfaire la demande dans les conditions autorisées. | Permettre une réponse acceptable lorsque le produit demandé ne peut pas être fourni tel quel. |
| D03.h | **Supply Creation Decision** : décider de recourir à une fourniture nouvelle et qualifier les conditions nécessaires pour fonder la promesse. | Rendre possible une fourniture que les ressources déjà présentes ou attendues ne permettent pas de satisfaire. |

Ces capacités appartiennent à Order Promising pour les décisions relatives à la promesse. Les politiques génériques de réseau, d’approvisionnement ou de protection ne sont pas absorbées dans ce domaine. La capacité à décider, chaque décision produite et l’acteur autorisé à décider restent distincts. Source et acheminement peuvent être décidés conjointement. Les décisions peuvent contribuer à Promise Proposal et Promise Revision ; leurs interactions ne constituent pas des doubles comptages de capacités ou une décomposition logicielle obligatoire.

#### Frontières et objets à préciser

| Domaine ou périmètre | Contribution et limite |
| --- | --- |
| Inventory Management — D01 | Stocks physiques/logiques, connaissance des ressources futures, protections et réservations. Order Promising calcule et utilise la disponibilité promettable. La frontière réservation/affectation doit éviter de compter deux fois les effets d’un engagement. |
| Fulfillment Network — D13 et Execution Options — D06 | Réseau et caractéristiques reçus en D13, capacités et options admissibles appréciées en D06, utilisés pour les décisions de source et d’acheminement. Le partage détaillé avec D06.c demeure à préciser. |
| Product Reference — D08, Catalog — D12 et Agreement — D11 | Caractéristiques de référence reçues et conditions particulières pour décider des substitutions et de la promesse ; leurs sources restent maîtres. La négociation éventuelle relève du modèle processus. |
| Commercial Commitments — D04 ; Execution Commitments and Facts — D07 | Obligations, engagements de réalisation, ressources attendues et faits utiles. Décider d’une fourniture nouvelle ne vaut pas, à lui seul, autorisation d’un engagement d’achat. |
| Logistique et C-Log | Possibilités et réalisation logistiques avec leurs autorités propres. Choisir une option fondant la promesse n’absorbe pas la planification détaillée du transport, les chargements ou l’affectation des véhicules. Logistique hors développement FLOW, en adhérence. |

**Objets et faits à explorer :** proposition de fourniture, promesse confirmée, demande et part non confirmée, affectation ressource/demande, options de source/acheminement, décision et révision. Aucun aggregate root unique, schéma de persistance ou document universel décidé. La date livrable dépend aussi de l’amont U80 ; une priorité ne crée pas de ressource et une attente future ne prouve pas l’existence physique du stock.

#### ATP retenu et CTP différé — U95

**ATP est associé à la promesse**, notamment à Promise Proposal. Il peut inclure des ressources futures planifiées ; aucune formule universelle adoptée. Le **CTP reste au glossaire**, mais son placement et son utilisation dans la carte sont différés par Laurent. Son rapprochement avec l’analytics opérationnelle pouvant alimenter la planification des commandes ou la protection des stocks est une piste à examiner ultérieurement, pas un domaine propriétaire validé.

**Supply Creation Decision reste validée.** La mise en attente de CTP ne supprime pas l’aptitude à décider d’un recours à une fourniture nouvelle et ne choisit pas le moyen de l’évaluer. Ne pas confondre définition Microsoft de CTP et futur placement local. TER044/TER045 et CMP051/CMP052 conservent cette distinction.

**Marché et provenance :** U30/U31/U75/U80/U81/U90–U95 ; C63 ; [P83](05-propositions.md#p83), [CMP052](../marche/comparaisons.md#cmp052). Les appuis SAP, Microsoft et Oracle de [la comparaison](../marche/order-promising-comparaison-capacites.md) sont partiels ; la validation métier locale ne valide ni les équivalences ni une couverture exhaustive du marché. Le diagnostic U89 porte sur l’état antérieur ; les règles détaillées et cas d’épreuve demeurent nécessaires. Noms et versions antérieurs conservés dans les corrections, le journal et l’audit initial. Les anciennes ancres U87/U88 et U91 pointent vers cette vue courante.

<a id="d04-engagements-commerciaux"></a>

### D04 — Commercial Commitments

**Réorientation U100 :** les quatre lignes ci-dessous sont la proposition antérieure, conservée pour la revue ; elles ne constituent pas un découpage commercial validé du socle. Étudier avec D07 les documents d’autorisation, leurs évolutions et leurs liens aux décisions et faits de réalisation. Les parcours achat/vente/après-vente/réassort appartiennent au modèle processus. Le nom et les frontières de D04 sont à refondre selon [la note U100](26-supply-documents-autorisations.md).

**Statut après U97/U98 :** domaine candidat pour les engagements propres aux commandes d’achat et de vente, distincts des Agreements. Laurent confirme cette distinction ; le regroupement commun, le nom et les quatre capacités restent à examiner.

**Finalité proposée :** connaître les engagements portés par les commandes et ce qui reste à accomplir après leur évolution et leur réalisation.

**Espace problématique :** qui s’engage à fournir ou acquérir quoi dans une commande, sous quelles conditions reçues, et que reste-t-il à accomplir après modification, livraison ou retour ? Les parties, obligations, règles de changement et imputations des réalisations relient ces problèmes.

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D04.a | **Establish a commercial commitment** : établir l’engagement propre à une commande, avec parties, biens ou prestations, quantités, conditions applicables et degré de fermeté. | Disposer d’une référence sur ce qui est commandé et engagé. |
| D04.b | **Amend commercial obligations** : modifier ou éteindre les engagements d’une commande selon les conditions applicables, en conservant leur histoire. | Faire évoluer les obligations transactionnelles et leurs effets. |
| D04.c | **Determine commitment fulfillment and remaining obligations** : rapprocher les obligations d’une commande des réalisations et corrections qui lui sont imputables. | Connaître les obligations encore ouvertes. |
| D04.d | **Authorize a return or replacement** : décider de l’autorisation et des obligations correctives applicables à une commande selon les conditions reçues et les faits. | Donner effet à une solution commerciale admissible après fourniture. |

**Objets et faits :** commande d’achat ou de vente, engagement de prestation à éprouver, modification de commande, autorisation de reprise et réalisation imputée. Agreement est le contrat de référence reçu en D11 ; sa création et sa modification n’appartiennent pas à D04. Le rapprochement commande/Agreement ne fixe ni cardinalité, ni identité commune, ni règles de consommation contractuelle universelles.

#### Première revue Commercial Commitments — U96

La proposition [P84](05-propositions.md#p84) conserve les noms de discussion **Commitment Creation**, **Commitment Revision**, **Commitment Reconciliation** et **Return and Replacement Decision**, respectivement D04.a–d, désormais limités aux commandes. Les trois premiers décrivent des actions, le dernier une décision ; ils ne constituent pas une séquence obligatoire. Noms et maille non validés. La [revue initiale](../audits/2026-09-11-reference-data-boundaries.md#historique-d04-remplacé-version-05) est conservée comme historique remplacé.

**Frontières :** Party / Role fournit les identités et rôles reçus ; Agreement fournit les contrats et conditions particulières ; Catalog fournit les catalogues et informations applicables. D04 utilise ces références sans les administrer. D03 porte la promesse, ses décisions et sa couverture ; D07 porte les engagements et faits de réalisation. Le modèle processus porte les dossiers, négociations, tâches et validations organisationnelles. Finance et réalisation logistique demeurent en interface.

**Épreuve par les récits :** les trois cas d’achat U48 alimentent l’exploration des commandes, sans démontrer la fermeté des Planned Purchase Orders (Q034). La façon appelle des obligations distinctes sur composants et prestation (Q069). Le réassort U53 ne produit pas automatiquement une vente pour tout transfert. Les besoins Boardriders U30/U31 éprouvent le lien commande/promesse ; les retours restent insuffisamment détaillés (Q048). Une révision de promesse ne modifie pas automatiquement le contrat de référence.

**Marché :** Sales Order Management et Purchase Order Management SAP, commandes et retours Microsoft : appuis partiels déjà examinés, ELM063/ELM085/ELM086. Les Sales/Purchase agreements Microsoft et Agreement Management TM Forum éclairent désormais D11 ; leurs fonctions de création ou changement de contrat ne justifient pas des capacités locales D04. Le domaine commun achat/vente reste une construction proposée. [CMP054](../marche/comparaisons.md#cmp054) corrige la portée de CMP053 ; aucune nouvelle équivalence précise revendiquée.

<a id="d05-équilibrage-opérationnel-des-ressources"></a>

### D05 — Operational Resource Balancing

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D05.a | **Determine operational coverage targets** : établir niveaux et seuils applicables par ressource et périmètre. | Donner une référence au renouvellement opérationnel des stocks. |
| D05.b | **Determine net resource requirements** : identifier les manques ou excédents en tenant compte des positions, besoins et approvisionnements attendus pertinents. | Former un besoin justifié sans ignorer les ressources déjà attendues. |
| D05.c | **Determine resource redistribution** : proposer les quantités et destinations permettant de traiter des déséquilibres selon les contraintes. | Rééquilibrer les ressources lorsque leur distribution devient inadaptée. |

**Objets et faits :** objectif applicable, besoin net, proposition de redistribution. Le dossier Demande de réassort et son suivi restent dans le modèle processus ; le socle peut produire le besoin qui l’alimente. Calculer le besoin ne promet ni ne réalise le transfert. D05.c est une hypothèse issue de U57, avec attribution de réalisation ouverte ; les prévisions et optimisations logistiques restent en adhérence. Pas de planification de saison incluse.

**Provenance :** U06/U53/U57/U58 ; CAP011–CAP013. **Marché :** contrôle de parcours par ELM022/ELM027, références historiques contextualisées dans l’étude. Aucun domaine complet ni algorithme actuel comparable établi ; D05.c non comparée précisément.

<a id="d06-possibilités-dexécution"></a>

### D06 — Execution Options

**Frontière U102 :** D13 reçoit les références du Fulfillment Network. Les capacités ci-dessous restent proposées pour apprécier les possibilités d’exécution selon les besoins et la situation. D06.a utilise les lieux et prestations de référence ; elle ne doit plus être lue comme administration ou contrôle de qualité de ces références. La maille D06.a/c reste à éprouver pour éviter un doublon.

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D06.a | **Qualify locations and feasible services** : connaître les lieux, leurs rôles opérationnels et les prestations qui y sont admissibles. | Identifier les possibilités concrètes de réalisation. |
| D06.b | **Determine available execution capacity** : apprécier limites applicables, charge engagée et capacité restante pour une prestation et une période. | Éviter de confondre disponibilité d’article et possibilité de le servir. |
| D06.c | **Determine eligible execution options** : établir et comparer les origines ou prestations compatibles avec un résultat attendu. | Éclairer un choix réalisable selon les critères autorisés. |

**Objets et faits :** lieu, prestation admissible, limite de charge, option d’exécution. Les références des sites et du réseau sont reçues en D13 ; elles sont utilisées ici pour apprécier les possibilités d’exécution. Les parties et leurs rôles relèvent de D09. Les limites applicables peuvent être fournies par l’organisation ; leur contrôle est distinct de l’affectation de tâches. D07 porte les engagements qui consomment ou libèrent la charge. Le choix d’entrepôt et de transporteur exercé par C-Log reste en adhérence ; D06.c n’en transfère pas l’autorité à FLOW. Sa frontière avec D03 et le modèle processus est à éprouver sur le choix magasin.

**Provenance :** U04/U06/U07 ; CAP002/CAP015–CAP017, Q015–Q019/Q063. **Marché :** exécution et ressources repérées dans l’étude ; capacités précises de service/quota non comparées. Le domaine est surtout fondé sur le récit de préparation et d’expédition magasin.

<a id="d07-engagements-et-faits-dexécution"></a>

### D07 — Execution Commitments and Facts

**Frontière à reprendre après U100 :** distinguer document autorisant le mouvement, engagement de son exécution et fait de réalisation. Revoir le partage avec D04 sans créer deux fois le même engagement ; pas de fusion ni de transfert d’autorité logistique déduit. Voir [la note U100](26-supply-documents-autorisations.md).

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D07.a | **Formalize a service requirement** : exprimer biens, destinataire, résultat et opérations nécessaires à une réalisation. | Rendre le besoin compréhensible et exploitable par l’exécutant. |
| D07.b | **Establish and adjust execution commitments** : qualifier prise en charge, portée, validité et effets des refus, retraits ou révisions. | Savoir quelle réalisation est effectivement engagée et quelle charge elle mobilise. |
| D07.c | **Qualify execution results and discrepancies** : rattacher constats de production, expédition, réception ou consommation au résultat attendu. | Donner aux autres domaines des faits utilisables et expliquer les écarts. |
| D07.d | **Identify and qualify expected resources** : qualifier quantités, dates, provenance et fermeté des résultats de réalisation encore attendus. | Permettre un raisonnement sur les ressources futures avec leurs limites. |

**Objets et faits :** besoin de prestation, engagement d’exécution, ressource attendue, réalisation ou écart documenté. Le domaine représente le contrôle métier à la frontière ; le routage interne, le transport et l’exécution physique logistiques sont hors développement FLOW. La confection à façon est un cas d’épreuve de prestations et de ressources, sans domaine Manufacturing imposé. Le suivi documentaire de dossier, les relances, les tâches et l’échéance des quinze minutes restent dans l’autre modèle. Les règles d’acceptation tardive et d’effet sur les engagements doivent cependant être explicites.

D07.d propose un point d’accueil pour le futur, relié à D04 et D03. Plusieurs étapes de la même fourniture ne doivent pas être comptées comme des ressources futures différentes. Le détail du suivi amont ne prouve ni autorité de référence ni fiabilité de chaque date. D07.c ne signifie pas que les consommations à façon sont aujourd’hui captées dans la plateforme.

**Provenance :** U03–U07/U10/U30/U48 ; CAP018/CAP020/CAP030–CAP032/CAP036, Q018/Q034–Q036/Q040–Q043/Q069. **Marché :** ELM043/ELM044/ELM059 ; descriptions de produit utilisées pour éprouver les faits, sans équivalence à un domaine générique d’exécution.

<a id="référentiels-ingérés-u97u98"></a>

## Business References

**Regroupement retenu U103 :** [P87](05-propositions.md#p87) s’applique comme groupe de présentation à Party / Role, Agreement, Product Reference, Catalog et Fulfillment Network. Une ingestion distincte par référence ; modèles et identifiants conservés. Le groupe ne crée ni capacité générique supplémentaire ni domaine commun de maîtrise. [Comparaison marché](../marche/regroupement-referentiels.md), C69/Q075 ; réseau détaillé ouvert en Q076. **Finalité :** disposer des références externes nécessaires aux opérations et décisions de la Supply.

**Orientation explicite de Laurent, 11 septembre 2026 :** la plateforme n’est maître ni de Party / Role, ni d’Agreement, ni de Catalog. U100 confirme en complément le référentiel article autonome : Product Reference rejoint ce groupe. U102 ajoute Fulfillment Network. Les cinq références sont contiguës et reçoivent chacune une seule capacité d’ingestion ; pour le réseau, ce périmètre prolonge U97 à titre proposé, sans maître identifié. Le groupe de présentation est retenu U103 ; aucun rang de domaine autonome n’est imposé aux références. Les modèles restent distincts et se relient par identifiants. Création, modification, vérification des données, dédoublonnage, enrichissement et parcours d’enregistrement ou de recrutement restent aux applications maîtres externes.

L’ingestion désigne ici l’aptitude à recevoir les informations de référence et leurs évolutions pour les utiliser dans les opérations. API, événements et mécanismes de persistance sont des moyens à concevoir ; ils ne créent pas de capacités supplémentaires. Appliquer une condition à une promesse est une décision du domaine consommateur, distincte de la vérification des données du référentiel.

<a id="d09-parties-et-relations"></a>

### D09 — Party / Role

**Finalité :** disposer des identités et rôles de référence nécessaires pour relier les opérations aux bonnes parties.

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D09.d | **Party / Role Ingestion** : recevoir les parties, leurs identifiants, rôles et relations de référence ainsi que leurs évolutions, en conservant les références du maître externe. | Utiliser une identité de référence commune dans les opérations. |

Le référentiel Party / Role externe porte la responsabilité d’identité sans doublon des personnes juridiquement responsables selon U97. Les applications CRM/SRM contribuent aux références clients/fournisseurs ; leur répartition détaillée avec Party / Role reste à documenter. Les rôles métier ne sont pas les habilitations RBAC du modèle processus. D09.a–c sont retirées, sans réutilisation de leurs repères.

### D11 — Agreement

**Finalité :** disposer des contrats de référence et de leurs conditions pour former les commandes et honorer leurs promesses.

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D11.a | **Agreement Ingestion** : recevoir les contrats fournisseurs ou clients, leurs références Party et Catalog, leurs conditions particulières et leurs évolutions depuis les applications maîtres externes. | Mettre les conditions contractuelles de référence à disposition des décisions et engagements transactionnels. |

Un Agreement indique le ou les catalogues permettant de commander, identifie le Party et précise les conditions particulières utiles à Order Promising. CRM/SRM sont cités par Laurent comme applications de référencement externes ; aucune configuration installée ni autorité par attribut n’est déduite. U98 distingue explicitement les commandes des Agreements. Les commandes D04 peuvent s’y référer ; elles ne deviennent pas des contrats de référence à administrer ici.

<a id="d08-produits-opérationnels"></a>

### D08 — Product Reference

**Finalité :** disposer d’une référence article autonome, utilisable dans plusieurs catalogues et par les opérations de la Supply.

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D08.d | **Product Reference Ingestion** : recevoir les articles, leurs identifiants SKU, caractéristiques de référence utiles et évolutions depuis leur maître externe, indépendamment de leur présence dans les catalogues. | Reconnaître les mêmes articles dans les différents catalogues et opérations. |

**Statut :** autonomie du référentiel confirmée par Laurent en U100 ; nom et rédaction détaillée proposés dans la continuité de l’ingestion seule U97. D08 est réactivé pour le même sujet article, sans réutiliser ses anciennes capacités D08.a–c ni restaurer leur administration/qualification. Source maîtresse, attributs, unités et conversions restent à préciser. [INF21](10-autorites-information.md#inf21), [CMP058](../marche/comparaisons.md#cmp058) : appui partiel produit/catalogue du corpus ELM090/ELM091, sans équivalence native de capacité.

### D12 — Catalog

**Finalité :** disposer des catalogues applicables, avec les prix et zones géographiques nécessaires aux opérations.

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D12.a | **Catalog Ingestion** : recevoir les catalogues construits à l’extérieur, leurs références de produits, prix, zones géographiques d’application et évolutions. | Permettre de commander et d’utiliser les informations commerciales reçues. |

La construction des catalogues et prix relève d’applications externes. U100 distingue le référentiel article D08 : un même SKU peut être proposé dans plusieurs catalogues. D12 référence ces articles ; il ne porte pas leur identité maîtresse. Sources, unités, conditionnements et attributs de présentation restent à préciser selon leurs autorités. Aucune administration produit locale ajoutée.

**Provenance et marché communs :** U97/U98, F203–F208, C64/P85 ; [autorités INF18–INF20](10-autorites-information.md#inf18). Noms d’ingestion locaux, sans équivalence native de capacité établie ; [CMP054](../marche/comparaisons.md#cmp054) et [correspondances](../marche/correspondances-domaines-coeur.md). Les modèles de marché plus larges ne valent pas délégation de maîtrise à la plateforme.

### D13 — Fulfillment Network

**Finalité proposée :** disposer d’une représentation de référence des lieux et des relations du réseau nécessaires pour organiser la réalisation des mouvements de marchandises.

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D13.a | **Fulfillment Network Ingestion** : recevoir les points du réseau, leurs caractéristiques de référence, leurs relations et liens vers les parties responsables, ainsi que leurs évolutions depuis les sources maîtresses externes. | Donner aux opérations et décisions une connaissance commune du réseau de réalisation. |

**Statut :** Laurent demande ce référentiel et confirme Party ≠ lieu en U102. Fulfillment Network corrige uniquement l’orthographe du verbatim Fullfilment Network. Repère D13, définition et contenu détaillé proposés ; le groupe de présentation Business References est retenu U103, sans rang de domaine autonome imposé à D13. La réception seule prolonge U97, sans attribuer une maîtrise du réseau à la plateforme.

**Contenu candidat, à éprouver :**

- Points et rôles : magasins, entrepôts, points de transit, sites fournisseurs et destinations clients utiles aux mouvements. Distinguer nœuds référencés du réseau et adresses ponctuelles associées à une transaction ; ne pas imposer l’enregistrement permanent de toute adresse client.
- Relations entre points : liaisons autorisées ou proposées comme référence, portée et validité. Une liaison référencée n’est pas le parcours choisi pour une commande.
- Caractéristiques utiles : prestations offertes, stockage possible, calendriers, horaires limites et délais de référence, selon l’autorité compétente. Ces attributs ne sont pas encore une liste validée et peuvent provenir de plusieurs maîtres.
- Liens aux Party : responsable, exploitant ou prestataire, avec rôles à préciser ; propriétaire du stock et exploitant du lieu ne sont pas automatiquement la même partie.

**Frontières :** D13 décrit le réseau reçu ; D01 connaît les stocks ; D06 apprécie l’aptitude à servir un besoin et la capacité restante ; D03 conserve Fulfillment Source Decision et Fulfillment Route Decision ; D07 suit engagements et faits. Charge courante, quantité disponible, ressources affectées et acheminement choisi ne deviennent pas des attributs maîtres du réseau. Délais annoncés et dates calculées restent distincts.

**Autorités et adhérences :** [INF22](10-autorites-information.md#inf22), [Q076](06-questions.md#q076). Aucune maîtrise globale C-Log ou FLOW déduite, aucune conception ni exécution logistique ajoutée aux développements FLOW. Les responsabilités de décision existantes restent à respecter.

**Marché :** [CMP060](../marche/comparaisons.md#cmp060). Appuis partiels existants sur les lieux et contraintes ; équivalence précise du réseau complet et de l’ingestion encore non comparée. Le nom n’est pas présenté comme un domaine natif attesté des éditeurs.

#### Repères retirés de la vue active

<a id="d10-conditions-commerciales"></a>

D08 Product Information Management et D10 Commercial Terms ont été retirés après U97. U100 réactive le même sujet article D08, renommé Product Reference à titre proposé, avec une nouvelle ingestion D08.d. D08.a–c, D10.a–c et D09.a–c restent retirées ; D10 demeure inactif. Les [définitions remplacées](../audits/2026-09-11-reference-data-boundaries.md#repères-et-état-remplacé) restent consultables. Les nouveaux domaines Agreement et Catalog reçoivent D11 et D12 : D08 et D10 ne sont pas réutilisés pour d’autres concepts.

## Stock futur, potentiel et ressources attendues — U79

**Source :** [U79](01-contributions-utilisateur.md#u79), F183 ; analyse A53. Laurent souhaite pouvoir référencer les ressources futures pour un entrepôt ou magasin et envisager leur affectation à des commandes. Le tableau qualifie son apport ; les catégories anglaises et précautions sont proposées, sans nouveaux niveaux ni capacités adoptés.

| Situation citée | Qualification de travail | Ce que la représentation doit distinguer |
| --- | --- | --- |
| Contrat fournisseur encore valide et non consommé jusqu’à sa limite haute | Purchasing potential | Possibilité d’achat restante ; quantité, validité, délais et conditions de fourniture à établir. Le reliquat seul ne prouve pas une réception datée. |
| Commande d’achat planifiée non engagée | Planned supply | Intention d’approvisionnement avec quantité et date prévisionnelles ; absence d’engagement fournisseur à conserver. |
| Commande engagée, en fabrication | Ordered supply | Quantité commandée, part confirmée et échéances attendues à distinguer ; commande et confirmation ne sont pas synonymes. |
| Acheminement par transporteur, douane, trajet vers l’entrepôt | In-transit inventory / expected receipt | Les biens peuvent déjà exister physiquement ; ils restent une entrée future pour la destination. Localisation actuelle, propriété et disponibilité à destination sont des dimensions distinctes. |
| Réception et rangement dans l’entrepôt | Received inventory / putaway | Le bien est déjà présent ; sa possibilité d’usage peut dépendre de contrôles ou du rangement. Arrivée, réception enregistrée et date utilisable ne sont pas automatiquement identiques. |

**Futur et virtuel :** futur qualifie ici la mise à disposition attendue pour un lieu et un usage ; il ne signifie pas toujours absence d’existence physique. Une ressource future peut alimenter le stock virtuel calculé défini en U76, mais l’entrée attendue et le résultat du calcul restent distincts. L’expression « existent virtuellement » de U79 est conservée comme représentation anticipée, sans remplacer silencieusement TER042. La mise en stock ou le rangement s’appelle putaway dans la documentation Microsoft (ELM073).

**Représentation proposée :** article, quantité/unité, origine et référence justificative, lieu actuel si connu, destination attendue, date de réception et date utilisable si différentes, état d’avancement, degré de confirmation, restrictions et quantités déjà engagées. Ces informations expliquent le résultat métier ; elles n’imposent ni schéma de données ni agrégat. Exemple fictif : 100 unités attendues au dépôt A le 20 septembre, dont 30 affectées à une commande ; elles ne sont pas pour autant présentes aujourd’hui au dépôt A. Les 70 restantes ne sont mobilisables que si les règles applicables le permettent.

**Continuité et absence de double compte :** contrat, commande planifiée, commande ferme, expédition et réception peuvent se rapporter à la même fourniture. Ne pas additionner leurs quantités comme autant de ressources indépendantes. Relier remplacement du plan, consommation du potentiel, réceptions partielles, reliquats, reports, annulations et effets sur les affectations. Les protections/réservations ne doivent pas être déduites deux fois lorsqu’elles expriment le même engagement. Ces règles sont à détailler avec les autorités concernées.

**Incidence sur les domaines — orientation U80 et responsabilités proposées :** [U80](01-contributions-utilisateur.md#u80)/F184 confirme que le stock futur est géré dans **Inventory Management et Order Promising**. La lecture suivante précise les responsabilités à éprouver : D01 représente les ressources futures, leurs états et leur disponibilité attendue ; D03 détermine les quantités et dates permettant de satisfaire une demande en mobilisant ces ressources. D04 connaît l’accord et ses obligations restantes ; D07.d qualifie les ressources attendues et leurs évolutions à partir des engagements et faits utiles. La présence du futur dans D01 et D03 est donc une orientation utilisateur, tandis que l’autorité détaillée entre D01/D04/D07 reste à arbitrer. Aucun déplacement ni ajout de capacité. La logistique et putaway demeurent en adhérence, hors développement FLOW.

**Date de promesse — U80/A54 :** elle ne dépend pas uniquement de la logistique sortante. Distinguer approvisionnement potentiel ou engagé, fabrication et acheminement amont, réception, disponibilité pour l’usage, puis préparation et livraison au destinataire. Les dates et conditions sont à combiner selon la situation, les règles et les possibilités d’exécution ; ce n’est pas une addition universelle de délais. Exemple fictif : arrivée au dépôt le 20 septembre, stock utilisable pour préparation le 22, livraison possible le 24 selon calendrier et transport. Un stock physiquement reçu le 20 n’est pas forcément immédiatement mobilisable pour cette promesse. Une date calculée possible ne vaut pas à elle seule confirmation fournisseur ou promesse ferme. Les modèles des deux domaines restent distincts, avec provenance des informations et cohérence des engagements.

**Marché :** [ELM073](../marche/elements.md#elm073)/[ELM074](../marche/elements.md#elm074), [CMP043](../marche/comparaisons.md#cmp043), vérifiés le 2026-09-11. Microsoft documente des entrées futures datées et leur distinction d’avec le présent ; SAP cite plusieurs ressources futures pour Supply Assignment. La totalité du potentiel fournisseur comme stock admissible n’est pas démontrée. Les types de documents ou étapes de réalisation ne deviennent pas automatiquement des sous-capacités. Q066 reste ouverte sur les objets, droits, autorités et règles.

## Épreuve par les récits

**Actualisation U97/U98 :** les points d’accueil des références utilisent désormais les trois ingestions. Ce raccordement ne démontre ni la présence des flux ni la couverture de règles non racontées ; les limites de chaque récit sont conservées.

**Raccordé** signifie que les problèmes du récit disposent d’un point d’accueil dans cette proposition ; cela ne prouve ni couverture exhaustive, ni définition complète, ni réalisation installée. **Partiel** indique les règles manquantes. **Adhérence** identifie ce qui reste dans l’autre modèle ou hors développement. Les scénarios déduits sont signalés comme tests, distincts des faits racontés.

| Cas et source | Capacités mobilisées | Résultat du contrôle et manque visible |
| --- | --- | --- |
| Stocks magasin par marque, copies consolidées, représentation entrepôt — U03/U04/U07 | D01.a–c, D02.a | **Raccordé, règles partielles.** Source, fraîcheur et non-double-comptage sont explicites ; autorité entrepôt et garanties de synchronisation restent inconnues. Une copie n’établit pas une autorité unique. |
| Vente sur stock, protection marque/canal, réservation à la commande — U10/U30 | D01 (protection D02.b, réservation D02.c), D02.a/d en réexamen, D03.b, D04.a | **Raccordé.** Protection de groupe distincte de réservation ; ni FIFO de lots ni garantie technique d’absence de survente déduits (C19/C20). |
| Expédition par C-Log, choix entrepôt et transporteur — U04/U06/U07/U58 | D06.a/c, D07.a/c | **Raccordé à la frontière.** Choix et réalisation logistiques restent en adhérence ; la carte ne les attribue pas au développement FLOW. |
| Prestations spécifiques et transfert préalable vers un entrepôt apte — U06/U07/U58 | D06.a/c, D07.a/c | **Adhérence explicite.** L’entreprise exprime les prestations requises ; C-Log choisit le parcours et le transfert préalable. Les résultats utiles au commerce sont à contractualiser, sans développer le routage ou le traitement d’erreur logistique dans FLOW. |
| Magasins participants, quotas et classement du moins sollicité — U04 | D06.a–c, D07.b | **Partiel.** Ressource de service distincte du stock ; sens de la charge et moment de consommation/libération inconnus. Tester deux engagements concurrents sur la dernière possibilité est une inférence utile. |
| Refus ou non-réponse après quinze minutes, nouvelle tentative, commande conservée — U04/U05, C07/C29 | D04.b/c, D07.b ; liens D02.d | **Raccordé avec l’autre modèle.** Le processus porte attente, nouvelle tentative et escalade ; le socle précise les effets sur engagements. L’expiration ne supprime pas la vente. Réservation et acceptation tardive restent à décrire. |
| Réassort automatique aux seuils IRMA–Storeland — U06/U62 | D05.a/b, D03.a/b, D07.a | **Raccordé, règles partielles.** Le besoin alimente un objet processus Demande de réassort. Quantité nette, prise en compte des entrées attendues et autorité de confirmation à préciser. |
| Réassort intra-société ou entre sociétés — U53 | D05.b, D03, D02, D07 ; D04/D09 selon obligations | **Raccordé comme cas d’épreuve.** Les aptitudes de fourniture sont communes ; les parties et obligations varient. Aucun achat/vente imposé à tout transfert ; effets financiers en interface. |
| Aléa amont et remplacement des données d’allocation MAP — U10, C17 | D07.d, D01 (Supply Protection, repère D02.b), D02.d, D03.c si une promesse est touchée | **Partiel.** Il existe un point d’accueil pour la politique applicable et le futur ; objets remplacés et effets actuels sur les engagements restent inconnus. Le recalcul amont n’est pas internalisé. |
| Prévisions de ventes, anticipation de stockage et lotissement des achats — U10 | Résultats amont utiles à D05/D07 ; engagements D04 à qualifier | **Adhérence amont.** Les décisions de saison et de stockage logistique ne sont pas des capacités à développer dans le socle par défaut ; leur prise en compte opérationnelle reste à décrire. |
| Fabrication complète fournisseur, Planned Purchase Order — U48 cas 1 | D12, D09, D11, D04.a, D07.c/d | **Partiel.** Demande prévisionnelle, engagement ferme, avancée et ressource attendue sont distingués. Fermeté et autorités inconnues ; design et planification restent en amont. |
| Achat de produits finis sur catalogue — U48 cas 2 | D12, D09, D11, D04.a/c, D07 | **Raccordé au niveau des problèmes.** Cycle et conditions détaillés non décrits. L’analogie wholesaler ne prouve pas un canal local de revente. |
| Fabrication à façon avec achats de tissus et accessoires — U48 cas 3 | D08/D12 (informations reçues à préciser), D04.a/c, D01.a/b/d, D02, D07.c/d | **Partiel, manque important.** Engagement de prestation, ressources confiées, consommations et résultat ont une place. Propriété, détention, pertes, reliquats et conversions ne sont pas établis ; Q069. Aucun domaine Fabrication imposé. |
| Documents fournisseur, progression fabrication/acheminement et douane — U03/U10/U61 | D04.c, D07.c/d, D01.a/b selon le fait | **Partiel et adhérence.** Les faits, documents et états opérationnels peuvent être reliés ; relances dans le processus, politique de conformité hors domaine. Document reçu ne signifie pas événement physique prouvé. |
| Vente B2B et B2C dans le périmètre historique de Beaumanoir — U02/U03 | D04.a–c, D09/D11/D12, D03 | **Raccordé au niveau des problèmes.** Canaux et outils ne créent pas de domaines ; conditions propres au B2B, prix et autorité de commande restent peu décrits. |
| Extension de gamme mentionnée dans les usages et demandes logistiques — U03/U06 | D12, D04, D06/D07 ; modèle processus | **Mention seule, couverture non démontrée.** Aucun déroulement détaillé n’est disponible ; le point d’accueil proposé ne permet pas de conclure aux règles de commande, d’assortiment ou de fourniture. |
| Boardriders : commander malgré l’insuffisance immédiate, avec ressources futures — U30 | D04.a/c, D07.d, D01 (réservation D02.c), D02.a en réexamen, D03.a–c et Supply Assignment (D02.e) | **Besoin cible raccordé.** Séparer commande, attente, confirmation et affectation ; la part non couverte reste visible. Horizons, fermeté et configuration installée inconnus. |
| Boardriders : servir une demande prioritaire par réaffectation — U30/U31 | D03.c, D02.d, D04.b/c | **Besoin cible raccordé.** La révision porte sur les promesses et leurs effets ; règles de protection des engagements fermes et traitement des demandes dépriorisées restent inconnus. Aucun comportement Gold attribué au périmètre historique de Beaumanoir. |
| Supply avec rééquilibrage, prévision et aléas propres — U57/U58 | D05.c, D07.d, D03.c ; interfaces d’anticipation | **Partiel et adhérence.** Ces problèmes restent visibles ; prévisions et optimisations logistiques ne deviennent pas des développements FLOW. Le seul exemple IRMA ne fixe pas tout le périmètre. |
| Retours et échanges comme parcours OMS — U54 ; SAV Sarenza U01/U02 en contrôle complémentaire | D11/D12 (conditions reçues), D04.d/c, D07, D01 | **Partiel, récit insuffisant.** Droits, autorisation, reprise physique et effet commercial ont des points d’accueil ; le dossier reste dans l’autre modèle. Aucun parcours détaillé de retour du périmètre historique de Beaumanoir ou de Boardriders n’est inventé. |

**Constat historique de raccordement, limité après U99/C65 :** les histoires avaient un point d’accueil au niveau des familles ; cela ne démontre pas la couverture précise des références produit reçues ni des responsabilités de prix appliqué et de consommation contractuelle. Elles font néanmoins apparaître plusieurs capacités encore insuffisamment exprimées et des périmètres faiblement documentés. Ce constat est une lecture des sources listées, sans taux de couverture de l’entreprise ; les besoins Boardriders U30 ne constituent pas un récit complet de son existant.

## Capacités à mieux faire apparaître et compléments plausibles

« Non listée » est apprécié par rapport aux intitulés des 36 CAP : certaines aptitudes sont déjà évoquées dans les notes sans fiche propre. Un complément ci-dessous peut rester une précision de définition ; il ne demande pas automatiquement une nouvelle capacité.

| Complément proposé | Pourquoi le remonter | Niveau de preuve et accueil proposé |
| --- | --- | --- |
| **Qualifier les ressources futures et leur fermeté** | Boardriders doit pouvoir raisonner au-delà du stock présent ; le suivi fournisseur ne suffit pas à définir ce qui est mobilisable. | Besoin U30 explicite ; capacité distincte encore proposée. D07.d, D02.a ; ELM035/ELM043. |
| **Distinguer réalisation, couverture et reste à satisfaire** | Une demande conservée, partiellement couverte ou dépriorisée ne doit pas disparaître du modèle. | Déduction de U04/U05/U30 ; fractionnement concret non raconté. D03.b/D04.c ; définition détaillée non comparée. |
| **Contrôler les engagements de capacité de service** | Le quota magasin est une autre contrainte que la quantité d’articles. | U04 explicite ; contenu à préciser de CAP016/CAP018. D06.b/D07.b ; règles de concurrence et réponse tardive inférées. |
| **Rapprocher et corriger les écarts de stock** | La visibilité n’assure pas à elle seule la fiabilité de la position. | Complément marché déjà identifié, sans récit local d’inventaire. D01.d ; ELM014/ELM024, Q065. |
| **Rapprocher matières confiées, consommations et résultat** | La fabrication à façon peut laisser des composants chez un tiers, des pertes ou reliquats à expliquer. | U48 justifie l’examen ; comportements détaillés issus du marché et hypothèses. D01/D04.c/D07.c ; ELM043/ELM044, Q069. |
| **Utiliser les unités, conversions et conditionnements reçus** | Tissus, accessoires et produits finis peuvent exprimer les quantités différemment. | Informations utiles, règles et sources non décrites ; ancienne D08.c retirée. Pas de capacité de qualification de référentiel après U97. |
| **Déterminer les droits de reprise et leurs effets** | Un retour n’est pas seulement un dossier ou un mouvement physique. | Périmètre déclaré, détail faible. D04.d utilise les conditions reçues de D11/D12 ; ELM047 partiel, Q048. |
| **Appliquer les restrictions de relation commerciale reçues** | Le récit distingue service FIFO et exclusion éventuelle d’un mauvais payeur. | U10 donne un indice ; règles non établies. Ancienne D09.c retirée ; décision à attribuer au domaine consommateur, sans domaine de crédit ou recouvrement ajouté. |

Les substitutions de produit, livraisons fractionnées et regroupements de besoins méritent des **tests complémentaires** si les récits les confirment. Ils pourraient enrichir D03/D04/D07 avec les informations externes D12, mais aucun besoin local de substitution ou règle de fractionnement n’est déclaré ici. Préserver l’identité d’un engagement lors d’un échange répété et tracer une correction sont aussi des exigences de cohérence à expliciter dans les domaines, sans créer un domaine technique de messages ou de documents.

## Raccordement aux 36 candidats historiques

Ce tableau est une lecture de couverture et de reformulation, plusieurs-à-plusieurs. Il ne remplace ni les définitions ni les regroupements historiques des fiches.

| Candidats | Accueil dans P81 ou frontière conservée |
| --- | --- |
| CAP001 | D08.d reçoit la référence article autonome U100 ; administration article exclue. D12 peut proposer les mêmes SKU dans plusieurs catalogues ; attributs et sources à préciser. |
| CAP002 | D09.d pour les parties, D13.a pour les références de réseau ; D06 apprécie les possibilités d’exécution. Autorités détaillées ouvertes. |
| CAP003 | D11.a/D12.a pour les références reçues ; D04 pour les conditions appliquées aux commandes. Administration exclue. |
| CAP004/CAP005 | D01 ; portée magasin de CAP004 conservée dans le registre. |
| CAP006 | D02.a ; utilisation du résultat par D03. |
| CAP007/CAP008/CAP009 | D01 pour Supply Protection (repère historique D02.b) ; liens aux engagements D02.d et calcul amont à délimiter. |
| CAP010 | D01 pour réservation (D02.c), D03 pour affectation (D02.e) et confirmation D03.b ; D02.d en réexamen. Contenu composite à examiner. |
| CAP011/CAP012/CAP013 | D05 ; déclenchement et suivi du dossier réassort reliés au modèle processus. |
| CAP014 | D04 ; parcours de commande dans l’autre modèle et promesse dans D03. |
| CAP015/CAP016/CAP017 | D06 ; engagements de charge D07.b, choix C-Log en adhérence. |
| CAP018 | Partie engagement D07.b ; sollicitations, échéances et reprises dans le modèle processus. |
| CAP019 | Résolution du cas dans le modèle processus ; effets demandés aux domaines du socle à qualifier. |
| CAP020 | D07.a ; frontière avec la logistique. |
| CAP021/CAP022/CAP023/CAP024/CAP025 | Logistique hors développement FLOW ; contrats, besoins et faits utiles reliés à D06/D07, sans absorption. |
| CAP026/CAP027/CAP028 | Prévision et planification amont ou logistique en adhérence ; résultats opérationnels utiles à D05/D07 à qualifier. |
| CAP029 | D04.a/D07.a ; engagement ferme distinct de la demande émise. |
| CAP030/CAP031/CAP032 | Faits et ressources attendues dans D07 ; réalisations imputées dans D04 ; dossiers, relances et conformité en frontière. |
| CAP033/CAP034 | D11/D12 pour les conditions reçues, D04.d pour les droits appliqués et effets ; dossier SAV dans le modèle processus, mouvements D01/D07 et finance en interface. |
| CAP035 | D03.c et conséquences D02.d ; règles propres aux périmètres conservées. |
| CAP036 | Résultat connaissable via D07.c ; préparation et expédition physiques hors développement logistique de FLOW. |

## Frontières à challenger en premier

| Frontière | Proposition initiale | Ce qui pourrait la faire évoluer |
| --- | --- | --- |
| Stock / disponibilité / protection / promesse | D01 pour stock, protection et réservation après U74/U75 ; D03 pour promesse et affectation ; D02 en réexamen. | Éprouver les autres frontières, notamment disponibilité/promesse et affectation/réservation. Tester protection sans commande puis futur et réaffectation Boardriders ; autonomie de D02 à réexaminer après U75, sans nouvelle frontière présumée. |
| Achat / vente / prestation | D04 commun aux obligations, avec variantes distinctes. | Séparer si leurs problèmes et connaissances divergent trop ; aucune symétrie de pouvoir de confirmation postulée. Les trois achats et le transfert inter-sociétés sont discriminants. |
| Référence contractuelle / commande / droits après fourniture | D11 reçoit les Agreements ; D04 examine les engagements de commandes et leurs effets. | U98 confirme leur distinction ; préciser les décisions transactionnelles qui appliquent les conditions reçues et les droits du SAV. |
| Possibilité / engagement d’exécution | D06 et D07, avec engagement de charge explicite. | Unifier si leur séparation n’aide pas à comprendre les règles ; conserver dans tous les cas la distinction article disponible, site admissible et prise en charge engagée. |
| Équilibrage / processus / logistique | D05 pour besoin et décision opérationnels ; dossiers et exécution en frontière. | Délimiter les aptitudes à réaliser dans FLOW à partir de l’autorité métier, sans transférer implicitement les prévisions et décisions C-Log. |

Je commencerais le challenge par **D01–D03**, puis **D04/D07 sur la fabrication à façon et le réassort entre sociétés**. D06 rend visible le cas magasin qui manquerait à une carte limitée au stock. D09/D11/D08/D12/D13 reçoivent les références externes selon U97/U100/U102 et les précisions de maîtrise encore ouvertes ; les sources et règles d’usage demandent des récits plus détaillés.

## Appuis de marché et limites

La [comparaison CMP036](../marche/comparaisons.md#cmp036) conserve les adaptations et la provenance. Réexamen ciblé le 10 septembre 2026, en complément de l’étude U25 :

- **SAP RBA** : [Reference Architecture Content](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), sections Framework / Business Capability Model Example, ELM014. Hiérarchie native Enterprise Domain → Business Domain → Business Area → Business Capability. Inventory Management et Order Promising sont des Business Areas ; Sourcing and Procurement est un Business Domain. Notre niveau ne prétend pas reproduire uniformément ces niveaux. Cours sans édition de catalogue.
- **SAP et Microsoft, ressources** : [Supply Protection](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-), groupes et documents ventes/transferts ; [Inventory Visibility allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), distinction allocation/soft reservation. ELM017/ELM028, compléments de lecture dans ELM062. Comportements de produit, sans correspondance complète à D01 ou D02 ; rattachement local de protection actualisé en CMP040.
- **SAP, promesse** : [Basic ATP](https://learning.sap.com/courses/configuring-supply-chain-business-scenarios-in-sap-s4hana-cloud-public-edition/introducing-basic-available-to-promise_ee3a33eb-4a91-4f85-a8b6-9bc1189e9540) et [Backorder Processing](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-backorder-processing-for-advanced-atp-in-sap-s-4hana), ELM046/ELM062 ; quantités/dates, ventes/transferts et réexamen. Éditions des cours non exposées ; aucune configuration Boardriders prouvée.
- **SAP, sous-traitance** : [Outlining Subcontracting](https://learning.sap.com/courses/detailing-subcontracting-and-supplier-consignment/outlining-subcontracting_af403e3e-188d-4dbb-bde1-632253739fa6), introduction / Applicable Process Steps, ELM043 : commande, composants fournis et consommation liée au résultat. Édition non exposée ; comportement local à confirmer.
- **BIZBOK/Guild et TM Forum** : ELM053/ELM057/ELM058 restent des appuis pour relier capacités, objets, états et résultats ; ils ne fournissent pas ici une carte retail détaillée. Guide Guild complet et SID détaillé non lus. IBM reste historique non prioritaire après U60.

Chaque domaine signale les correspondances partielles et les aptitudes non comparées. Aucun complément plausible n’est déclaré spécifique à Beaumanoir du seul fait qu’aucune équivalence n’a été trouvée. La couverture documentaire historique des CAP demeure 16 rapprochements /20 sans comparaison précise ; elle ne mesure pas les 35 formulations courantes de P81.

## Noms proches dans les références du marché — U65

La [table de correspondances du 11 septembre 2026](../marche/correspondances-domaines-coeur.md), CMP037, donne les noms SAP, Microsoft et TM Forum les plus proches et quelques exemples historiques Guild. Les niveaux et natures sont explicités. Les appuis nouveaux sur les référentiels, les unités et les possibilités d’exécution complètent les pistes ci-dessus ; les définitions ne sont pas encore toutes comparées individuellement. U65 n’avait renommé aucun domaine ou capacité ; U66 applique ensuite la nomenclature anglaise, avec provenance C48, et U67 précise la distinction aptitude/réalisation en C49.

**Comparaison préalable U89 — Order Promising :** la [revue des noms, de la nature et de la couverture](../marche/order-promising-comparaison-capacites.md) éprouve P83 sur SAP RBA, SAP/Microsoft et Oracle. Quatre critères explicites, quatre partiels et deux non décrits dans une grille locale de dix critères, distincte d’un nombre de capacités. Les propositions et les dix domaines/35 aptitudes restent inchangés.

**Historique U94, placement CTP différé en U95 — ATP/CTP :** [distinction Microsoft et application proposée à P83](../marche/order-promising-comparaison-capacites.md#atp-et-ctp-chez-microsoft-u94), CMP051. ATP comprend déjà des ressources futures ; CTP explore aussi les moyens de couvrir le manque. Deux raisonnements mobilisables dans Promise Proposal, sans deux capacités supplémentaires ni changement de frontière validés.

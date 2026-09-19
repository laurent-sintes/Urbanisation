# Audit de maturité du modèle FLOW — v007

**16 septembre 2026 — demande U249.** Base auditée : publication `2026-09-16.2`, **55 nœuds, 41 capacités, 74 relations**, référencée par l'index de release. Les champs des 55 nœuds et le contenu des 74 relations sont identiques dans le backlog au début de l'audit. Les quatre objets/documents/événements supplémentaires du backlog sont des illustrations non publiées. L'audit s'applique donc aussi au contenu courant de ces capacités, sans confondre les deux espaces.

**Mon diagnostic : les frontières principales sont cohérentes et le catalogue mérite d'être conservé comme base. Le niveau suivant de maturité dépend surtout de responsabilités mieux attribuées, de dépendances explicites et de fiches utilisables sans connaître nos conversations.** La comparaison au marché ne justifie pas une refonte générale ni l'ajout d'une série de domaines ERP.

Le principal risque actuel est qu'un lecteur comprenne chaque intitulé séparément mais ne sache pas expliquer une opération complète : comment une optimisation devient une commande ; comment une promesse devient un engagement de stock ; comment un fait logistique corrige le stock et le reste à satisfaire. Certaines réponses existent dans les textes ou les accords, mais sont peu visibles dans le modèle structuré.

## 1. Ce que le marché confirme et ce qu'il challenge

Les sources sont des documentations **fonctionnelles de produits**, processus, API et composants. Elles ne constituent pas trois catalogues homogènes de Business Capabilities. Les rapprochements sont des recouvrements partiels ou des appuis argumentés, jamais une équivalence déduite du nom. Les versions, passages lus et limites sont conservés dans les annexes ; 29 sources officielles consultées ou revérifiées le 16 septembre 2026.

| Sujet | Points communs documentés | Écart ou question pour FLOW |
| --- | --- | --- |
| **Stock, protection, réservation — D01** | Microsoft distingue allocation à des groupes et réservation pour une demande. SAP articule protection et disponibilité. | Distinction à conserver. La définition de Supply Protection ne restitue pas encore la gouvernance/tenue transactionnelle discutée. Expliquer affectation, engagement et consommation pour éviter les doubles comptes. [Microsoft allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), [SAP aATP](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/e541e617043545a0bb60e5067d037046.html). |
| **Promesse — D03** | Disponibilité, alternatives de réalisation, priorités, réexamen et arbitrages économiques se retrouvent dans les fonctions étudiées. | **CTP FLOW est volontairement plus large** : modifier protections ou autres engagements dépasse le sens usuel documenté chez Microsoft/Oracle. Il faut expliquer qui propose, autorise et applique ces changements ; conserver la maille ATP/CTP/PTP adoptée. [Microsoft CTP](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp), [Oracle Promising](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fascp/overview-of-database-centric-order-promising.html). |
| **Orders — D04** | Les suites distinguent documents de commande, évolution de leur cycle, blocages et documents d'exécution. | Une gestion par type, avec Structuring et Lifecycle transverses, reste lisible. Les objets techniques des produits ne justifient pas des capacités supplémentaires. La responsabilité sur le devenir des retours reste ouverte. [Microsoft achats](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-creation), [Oracle holds](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/fauom/sales-order-hold.html). |
| **Optimisation — D05** | Microsoft sépare suggestions et affermissement ; SAP IBP transmet des résultats de planification à l'exécution ; Oracle publie certaines politiques calculées vers Inventory Management. | Le choix local décision/planning/application est solide. Le manque concerne **le porteur de l'application des paramètres et de la mise en action des apports**, pas une autre capacité de calcul. L'exemple Oracle PAR reste particulier, sans généralisation à tous les magasins. [Microsoft plans](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans), [SAP transfert des résultats](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/66a038fcf40f4f779c6b4696aede83a6.html?locale=en-US), [Oracle PAR](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26c/faurp/par-policies.html). |
| **Pilotage de l'exécution — D06** | Demandes aux exécutants, suivi, changements et coordination se retrouvent chez les éditeurs ; TM Forum documente les dépendances entre demandes de service. | Orchestration / Adaptation Decision est une séparation locale défendable, pas un découpage natif universel. Oracle Supply Chain Orchestration recouvre plusieurs de nos domaines : son nom ne justifie pas de tout déplacer dans D06. [Oracle orchestration](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26c/fauco/overview-of-supply-orchestration.html), [TMFC007](https://oda-production.s3.eu-west-2.amazonaws.com/v1.0.0/TMFC007_Service_Order_Management_v1.2.1.pdf). |
| **Référentiels** | Produits, parties, conditions, lieux, services et calendriers alimentent les traitements des suites. | FLOW les reçoit de maîtres externes : c'est un choix de frontière, pas un retard fonctionnel face à un ERP qui les administre. Ne pas ajouter leur administration locale. Catalogue/SLA configurés, capacité contextuelle et engagements individuels doivent rester distincts. [Oracle données de promesse](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/fascp/keep-availability-in-global-order-promising-and-inventory-management-synchronized.html), [TMF633](https://www.tmforum.org/open-digital-architecture/open-apis/service-catalog-management-api-TMF633/v4.0). |

**Les différences à préserver** sont donc la séparation promesse / tenue des Orders / exécution, l'optimisation analytique distincte de son application, les maîtres et exécutants externes, et les Service Orders distincts des Supply Orders. Ces différences ne constituent pas en elles-mêmes des lacunes.

## 2. Les manques : attribuer avant d'ajouter

| Repère | Manque observé | Nature du manque | Recommandation et cas de contrôle |
| --- | --- | --- | --- |
| M01 | **Application des seuils de stock** : D05.a décide ; D02.b décrit surtout des limites destinées à des groupes | Attribution incomplète, attestée par les définitions | Décider quel management tient chaque famille de paramètres. Passer le seuil de réassort de 60 à 80 à compter de lundi ne doit pas être confondu avec interdire de vendre les 80 dernières pièces. Pas de renommage automatique de Supply Protection. |
| M02 | **Mise en action de l'optimisation** : le porteur du déclenchement reste explicitement « à instruire » dans D05.e | Responsabilité/contrat incomplets | Raccorder scénario retenu, autorité de lancement et création/modification d'Order D04. Tester une proposition de 50 puis un recalcul : la commande déjà créée doit être reconnue, sans doublon. Une nouvelle capacité n'est nécessaire que si une responsabilité durable reste sans porteur. |
| M03 | **Cohérence des représentations de stock** entre sources | Responsabilité non explicitée, à confirmer | D01 sait compter et tenir les faits ; qui explique « entrepôt 100 / FLOW 90 » ? Distinguer décalage documentaire, doublon et écart physique avant correction. Examiner d'abord la couverture par D01.f/g/c ; Stocktaking et Execution Reconciliation ne couvrent pas automatiquement cette question. [Microsoft WMS externe](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-external-erp). |
| M04 | **Devenir du bien retourné** : décision laissée ouverte dans D04.l | Candidat crédible à une responsabilité distincte | Après réception/constat, décider remise en vente, isolement, renvoi ou autre destination applicable. Une décision spécialisée peut être justifiée si FLOW en porte le résultat ; sinon définir le contrat avec Business Services ou l'exécutant. Aucun remboursement ou contrôle physique absorbé. [Microsoft retours](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns), [SAP retours](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/ef17554b70b946e588cf4fb378fa4622.html). |
| M05 | **Capacité exploitable pour promettre** | Contrat d'entrée incomplet ; capacité D06.b déjà présente | Qualifier maximum, charge et disponible communiqué, avec unité/fenêtre/fraîcheur. Un maximum de 1 000 préparations n'autorise pas une nouvelle demande de 200 si 900 sont déjà engagées. Ne pas inventer le calcul du résiduel ni ajouter Capacity Reservation sans cas métier. |
| M06 | **Demande prévisionnelle, coûts, incertitude, calendriers** utilisés par D03/D05 | Interfaces et autorités à documenter | Décrire les informations reçues et leur validité, notamment prévisions versus demandes déjà intégrées. L'absence de Forecasting ou d'un domaine Finance n'est pas un manque démontré du périmètre FLOW. |
| M07 | **Objets/résultats et événements échangés** | Niveau de modélisation encore absent de la release | Commencer par les contrats indispensables : quantité promise, couverture, réservation, recommandation d'apport, demande de prestation, fait et écart. Ne pas transformer ces candidats en sous-capacités. Quatre illustrations existent déjà dans le backlog ; elles ne constituent pas un modèle d'objets adopté. |

Business Services reste un univers sans domaines détaillés : c'est une **limite connue du niveau de maturité global**, pas une erreur de Supply. Finance, contrôle de gestion, conformité, design produit, planification de saison et réalisation interne des logisticiens restent exclus. Leurs interfaces utiles méritent d'être visibles ; leurs modules ne sont pas des « manques » à recopier depuis une suite.

## 3. Granularité : une maille par type de résultat

Je retiendrais le critère suivant pour la suite : **une décision répond à une question métier identifiable ; une action ou une gestion prend en charge un résultat durable et un ensemble cohérent d'opérations.** Il ne s'agit pas d'obtenir des capacités de même taille ou autant de capacités dans chaque domaine.

| Famille | Test de bonne maille | Application au modèle |
| --- | --- | --- |
| Décision | Question, alternatives, contraintes et résultat choisis sont explicables séparément | Les quatre décisions D05 sont un bon étalon. Plusieurs calculs ou paramètres peuvent concourir à une décision. Ne pas recréer des capacités Calculation. |
| Action / gestion | Un objet, un état ou un résultat est tenu dans la durée ; plusieurs opérations cohérentes appartiennent à la même aptitude | Les cinq gestions d'Orders, Structuring, Reservation et Service Order Management peuvent rester larges. Hold/Resume/Cancel, batch et écran ne deviennent pas des capacités. |
| Planning | Reconfigurer, simuler, valider en mobilisant des décisions | D05.f est cohérent. Il ne devient pas le parent des quatre décisions et n'impose pas de validation humaine. |
| Connaissance / visibilité | Une situation est rendue exploitable avec provenance, maille et fraîcheur | Inventory Visibility et Execution Capacity Visibility doivent avoir des résultats distincts de la tenue des faits ou des calculs de décision. |
| Orchestration | Coordonner des prestations et leurs dépendances selon le plan retenu | Conserver la séparation d'Execution Adaptation Decision, qui choisit la variation. |

**Trois points précis à arbitrer :**

- **Order Lifecycle Management** est de nature `decision`. Cette nature est défendable s'il décide des autorisations de transition tandis que les gestions par type tiennent les états. S'il porte la tenue du cycle elle-même, une famille gestion/action est plus cohérente. Le nom Management ne suffit pas à prouver une erreur ; expliquer le partage avant de reclasser.
- **Promise Proposal / Confirmation / Revision** sont des actions plus fines que les gestions d'Orders. Leurs résultats peuvent justifier cette différence. Leur description doit montrer composition, engagement et modification de l'engagement, sans refaire ATP/CTP/PTP. Je ne recommande pas une fusion automatique de choix déjà adoptés.
- **Les natures ne sont pas homogènes** : 11 manquent ; les gestions D04 sont `action`, Service Order Management est `management`, cinq ingestions n'ont pas de nature et D14.a est `action`. Définir la convention de familles et sous-familles avant de les remplir. La généralisation de Management au-delà de Stock Protection reste proposée dans le glossaire de modélisation.

CTP mérite une vigilance particulière : sa réponse est un **plan candidat de satisfaction**, plus large qu'une décision de seuil ou d'échéancier. Son ampleur est volontaire ; ses sorties et responsabilités mobilisées doivent justifier cette maille. La granularité n'impose pas de rouvrir le choix ATP/CTP/PTP.

## 4. Relations : le défaut le plus structurant

Sur **74 relations, 53 décrivent l'arbre ou la présentation**. Il reste **21 relations transversales**, dont 18 entre capacités. **22 capacités n'ont aucun lien transverse**, dont six ingestions : les 16 autres comprennent tout D01, presque tout D03 et les deux capacités transverses D04.

Le modèle contient donc des responsabilités qui sont connues par leurs textes mais isolées dans le graphe. De plus, certaines flèches signifient « utilise », d'autres « alimente ». Elles ne peuvent pas toutes être présentées comme « a besoin de » dans le même sens.

**Recommandation : une vue consommateur → fournisseur, avec le résultat attendu sur chaque lien.** Exemple : ATP → Inventory Visibility pour le stock admissible ; ATP → Supply Protection pour les restrictions actives ; Promise Proposal → ATP pour une solution ; Execution Reconciliation → Tracking et Service Order Management pour comparer constaté et attendu.

La [matrice détaillée](relations.md) décrit les dépendances à instruire, les liens existants à normaliser et les entrées des référentiels/exécutants. Elle distingue résultat attendu, condition d'utilisation et incertitude. Elle ne prescrit pas d'API, de séquence technique, de cardinalité ni de transaction distribuée. Les cycles de réexamen sont légitimes.

## 5. Descriptions : donner au lecteur une situation et un effet

| Mesure sur les 41 capacités | Résultat |
| --- | --- |
| Définition et finalité présentes | 41 |
| Périmètre `scope` présent | 26 ; manque aux 6 capacités D01 et aux 9 D03 |
| Exemple métier situé | 20 ; manque aux 15 D01/D03 et aux 6 ingestions |
| Nature renseignée | 30 |
| Référence textuelle obsolète au domaine D07 | 6 fiches : D04.i–m et D05.c |

Un champ présent n'est pas une preuve de qualité. D04/D05/D06 sont nettement plus explicites, mais leurs longues réserves et mentions historiques peuvent masquer le résultat principal. À l'inverse, « établir les priorités relatives des commandes » ne suffit pas à comprendre l'intervention d'Order Prioritization dans une situation réelle.

**Gabarit proposé pour chaque fiche :** une définition autonome ; le résultat produit ou tenu à jour ; les principales informations nécessaires ; un cas métier avec situation, intervention et résultat ; les frontières qui évitent une confusion. Conserver l'histoire des renommages et les preuves d'adoption dans la provenance, les limites métier dans la fiche. Les exemples doivent rester signalés comme illustrations, sans devenir des règles d'exploitation adoptées.

Exemple proposé pour **Supply Protection** : « Gérer la validité et la tenue transactionnelle des protections et limites d'usage retenues pour des groupes. Une décision retient 200 pièces protégées pour le web jusqu'à vendredi ; la capacité rend cette protection applicable et tient ses évolutions. ATP en tient compte. Ces 200 pièces ne sont ni un stock physique supplémentaire ni une réservation pour une commande précise. » La responsabilité de décider les 200 pièces reste distincte ; l'attribution des seuils de réassort n'est pas réglée par cet exemple.

La [grille des 41 capacités](qualite-granularite.md) contient les constats fiche par fiche et **huit compléments de description proposés**, principalement sur D01/D03. Une correction de texte ne transfère aucune validation à un contenu nouveau.

## 6. Ordre de travail recommandé

| Priorité | Lot proposé | Critère de sortie |
| --- | --- | --- |
| **P1** | Attribuer application des politiques, mise en action D05 et contrat promesse/affectation/réservation | Un réassort et deux commandes concurrentes s'expliquent de bout en bout, sans responsabilité orpheline ni double engagement |
| **P1** | Normaliser la lecture des dépendances et compléter les liens métier essentiels | Pour une capacité critique, on peut voir de quel résultat elle a besoin, qui le fournit et sous quelles conditions |
| **P1** | Réaligner Supply Protection et corriger les six références au domaine D07 | Les fiches ne contredisent plus les frontières adoptées ; les identifiants D07.* restent inchangés |
| **P2** | Arbitrer les natures et compléter les 15 périmètres / 21 exemples absents | Chaque fiche est compréhensible isolément et la maille se justifie par son résultat |
| **P2** | Instruire devenir des retours et rapprochement des représentations de stock | Attribution à une capacité existante, à un externe, ou justification explicite d'une capacité nouvelle |
| **P2** | Préciser contrats de capacité, entrées de décision et premiers objets/faits | Maximum ≠ disponible, prévision ≠ commande, estimation ≠ engagement ≠ résultat ; les consommateurs savent interpréter les données |

**Je commencerais par consolider le catalogue existant.** Les deux sujets qui peuvent réellement conduire à des capacités supplémentaires sont le devenir des biens retournés et, si les capacités D01 ne le couvrent pas, la réconciliation des représentations de stock. Le marché justifie leur examen ; il n'impose ni leur nom ni leur emplacement.

## Dossier de preuve et limites

- [Microsoft](microsoft.md) : 12 sources, rapprochement des 41 capacités par groupes, limites de preuve explicites.
- [SAP et Oracle](sap-oracle.md) : 14 sources, versions consultées et comparaisons non établies signalées.
- [TM Forum](tm-forum.md) : trois sources ciblées sur catalogue, Service Orders et dépendances.
- [Relations](relations.md) et [qualité/granularité](qualite-granularite.md) : contrôles internes et propositions détaillées.
- [Mesures](metriques.json), [script de reproduction](mesurer.py), [empreintes initiales](empreintes-avant.json) et [vérification](verification.json).

SAP Help a été exploité sur ses passages officiels indexés lorsque l'ouverture directe était vide. Les éditions Oracle varient selon les pages accessibles ; elles ne sont pas présentées comme une édition uniforme. Aucun test de produit, étude de licence, mesure de couverture installée ou lecture exhaustive de tous les manuels n'est revendiqué. Les absences de correspondance ne prouvent pas une absence de fonctionnalité chez un éditeur.

**Le modèle et ses publications restent inchangés.** Seuls les livrables d'audit, la contribution et les registres documentaires sont enrichis. Les recommandations restent proposées ; aucun changement de catalogue, validation, release, commit ou push n'est produit par cet audit.

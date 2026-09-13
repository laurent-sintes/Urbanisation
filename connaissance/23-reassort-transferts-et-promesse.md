# Réassort, transferts et cœur commun de supply

10 septembre 2026 — [U53](01-contributions-utilisateur.md#u53), [U54](01-contributions-utilisateur.md#u54), [U55](01-contributions-utilisateur.md#u55), [U56](01-contributions-utilisateur.md#u56), [U57](01-contributions-utilisateur.md#u57), [U58](01-contributions-utilisateur.md#u58), F151–F158 ; analyse A33/A34/P77/C43/C44. Cette note éprouve les [frontières de domaines](22-options-domaines-socle.md), sans nouvelle hiérarchie ni capacité validée.

## L’hypothèse de Laurent et sa portée

U53 considère un réassort depuis un stock, généralement en entrepôt, vers un magasin. Un problème logistique semblable peut être qualifié d’achat/vente entre sociétés ou de rééquilibrage interne, avec des différences de facturation. Laurent propose d’examiner un cœur générique **Supply Decision & Execution** et demande s’il correspond à Order Promising.

U54 précise que les demandes de réassort, commandes eCommerce et retours distingués par un OMS relèvent, dans sa lecture, des **processus commerciaux au-dessus de la supply execution**. Leurs différences de parcours ne suffisent donc pas à définir trois domaines du socle. La capability map conserve la portée transactionnelle fixée en U50 ; le modèle fonctionnel orienté processus décrit ces parcours.

**U55 précise la définition retenue par Laurent : un OMS est un Case Management préimplémenté pour la vente, au-dessus du transactionnel Supply.** Cette définition guide notre modèle ; les réalisations de produits seront comparées séparément. Les moteurs peuvent exister des deux côtés (U49). Ni l’unification de toutes les demandes en un objet, ni une même règle de traitement pour toutes les variantes ne sont adoptées ; Q052 reste ouverte.

**U56 définit la Supply comme la couche transactionnelle de contrôle, d’orchestration et d’optimisation de la logistique.** La réalisation logistique sur le terrain et l’autonomie du SI C-Log sont préservées. Optimiser exprime ici une finalité ; les natures de capacités discutées précédemment ne sont pas modifiées.

**Lecture proposée : ces cas partagent des problèmes de supply ; Order Promising en couvre une partie, pas l’ensemble.** Supply Decision & Execution est ici l’intitulé proposé par Laurent. Aucun domaine natif SAP de ce nom ni niveau Univers obligatoire n’est établi.

## Intelligence opérationnelle de la Supply

U57 précise deux responsabilités complémentaires : servir les commandes du commerce et porter une intelligence de backoffice pour le rééquilibrage, la prévision et les impondérables. La Supply n’est donc pas limitée à attendre et exécuter une nouvelle commande de vente.

Lecture proposée : les demandes commerciales peuvent déclencher des décisions de Supply, tandis que ses propres constats et anticipations peuvent conduire à proposer un transfert, réviser une couverture ou rechercher une réponse à un aléa. Ces initiatives restent soumises aux règles et engagements en vigueur. Le calcul d’un besoin de renouvellement est à examiner ici indépendamment du type de dossier utilisé ensuite dans l’OMS.

Cette distinction fait apparaître un autre test de frontière : **la promesse envers une demande** et **les décisions qui maintiennent la capacité du réseau à servir les besoins présents et futurs**. Le second périmètre peut inclure plus que la promesse ; il n’est pas adopté comme domaine unique. Les prévisions, leur horizon et leur rôle restent à préciser dans le cadre de U57, sans importer la planification de saison exclue.

## Périmètre FLOW et adhérence logistique

**U58 précise que la logistique est hors du développement de la plateforme du Programme FLOW, mais reste en adhérence.** Le modèle fonctionnel de Supply exploré ici ne vaut donc pas liste de composants ou de capacités à réaliser dans FLOW. L’autonomie du SI C-Log, déjà déclarée, est conservée ; l’exclusion exprimée porte sur la logistique, pas seulement sur cette filiale.

Le rééquilibrage, la prévision et la gestion des impondérables évoqués en U57 restent des aptitudes à comprendre pour analyser la relation commerce–Supply–logistique. Leur évocation n’attribue pas leur développement à FLOW. Inversement, U58 n’exclut pas globalement toutes les capacités Supply de la plateforme. Leur responsabilité précise reste à qualifier.

Conséquence de travail proposée : décrire les contrats et adhérences utiles au commerce, notamment :

- demandes de prestation, contraintes et engagements échangés avec la logistique ;
- états de stock, capacités de réalisation, confirmations et événements d’exécution utiles au socle ;
- aléas, refus et propositions d’adaptation pouvant affecter une promesse ou un dossier commercial ;
- autorité sur les informations et décisions prises de chaque côté.

Ce sont des axes de description, sans nouveau contrat arrêté ni transfert de responsabilité. Q040–Q044 conservent leurs questions de frontière ; cet apport ne les résout pas. Les moyens internes de réalisation logistique ne deviennent pas des développements FLOW. C44 conserve le risque d’interprétation corrigé.

## Les distinctions concrètes chez SAP

Sources primaires examinées le 10 septembre 2026, à partir des passages cités ci-dessous. Ce sont des descriptions de modèles ou de produits, sans preuve de déploiement local.

### Transfert interne et transfert entre sociétés

Le cours sur le transfert intra-company décrit un **Stock Transport Order**, une livraison sortante et des mouvements de sortie/réception, sans facture intercompany. La même logique de transfert est aussi traitée dans les scénarios intercompany. [S1, ELM045]

Le cours Cloud Public Edition distingue les scénarios **1P9** et **5HP** : achats et factures entre sociétés accompagnent les flux. Dans 5HP, une commande de vente est générée à partir de la commande d’achat ; le changement de propriété en transit est distingué des mouvements physiques. Il ne faut pas généraliser ce chaînage avancé à tous les transferts SAP. [S2, ELM045]

Le point utile pour notre modèle est la distinction entre mouvement physique, détention, propriété, engagement commercial et facturation. L’identité d’un lieu ne suffit pas à les déterminer. La société SAP, le périmètre de valorisation et la propriété métier doivent rester qualifiés. L’absence de facture intercompany n’exclut pas un effet comptable : SAP décrit des écritures selon les périmètres de valorisation. [S3, ELM045]

Ces constats servent à documenter l’interface avec la finance ; ils n’ajoutent ni domaine comptable ni règle fiscale au projet.

### La promesse concerne aussi les transferts

SAP décrit des engagements quantité/date envers un client **ou un site receveur**, notamment pour les commandes clients et les ordres de transfert. BOP peut réexaminer ces deux types de besoins. Order Promising ne se limite donc pas au SalesOrder. [S4/S5, ELM046]

Cela n’assimile pas toute la vie d’un achat, d’une vente ou d’un retour à une promesse. Dans l’extrait RBA, **Supply – Fulfill Demand** est un Enterprise Domain ; **Supply Chain Execution** est un Business Domain qui comprend notamment **Order Promising**, **Inventory Management**, **Warehouse Management** et **Transportation Management** comme Business Areas. **Sourcing and Procurement** est un autre Business Domain du même ensemble supérieur. [S6, ELM014]

La distinction native soutient une séparation entre promesse, faits de stock et exécution. Elle ne valide pas nos frontières locales ni l’inclusion de tout Supply – Fulfill Demand : planification de saison, production et finance conservent les limites du projet.

### Les retours mobilisent d’autres problèmes

La documentation ARM distingue notamment avis préalable, réception, inspection et suites du retour ; elle permet aussi un retour direct du client au fournisseur. Un retour peut donc mobiliser des mécanismes logistiques communs tout en nécessitant une qualification du bien et une décision de traitement. [S7, ELM047]

Pour notre analyse, une éventuelle promesse de remplacement est à distinguer de l’autorisation du retour, de son acheminement et de la disponibilité future du bien reçu. Un retour annoncé n’est pas automatiquement une ressource utilisable.

## Des problèmes à analyser, sans reproduire les types de parcours

Le tableau est une grille d’analyse du socle, **pas un déroulement de processus ni cinq nouveaux domaines adoptés**.

| Problème commun à examiner | Résultat ou connaissance recherchés | Variations à conserver |
| --- | --- | --- |
| Déterminer ou recevoir un besoin de ressource | Article, quantité, destination et horizon demandés. | Le calcul d’un besoin de réassort, la demande d’un client et le besoin de composants ont des origines et règles distinctes. |
| Déterminer la couverture et la promesse | Ressources admissibles, quantités/dates confirmables, affectations et révisions possibles. | Source interne ou externe, protections, fermeté, priorités et pouvoir de confirmation. L’entreprise ne promet pas automatiquement à la place d’un fournisseur externe. |
| Engager et constater l’exécution | Prestation demandée, engagement de réalisation, expédition, réception et écarts. | Sens du flux, acteurs, sites et résultats ; demandes, engagements et événements à la frontière FLOW. Développement logistique hors périmètre FLOW (U58) et autonomie C-Log conservée. |
| Connaître les ressources et leurs mouvements | Positions, états, provenance et faits expliquant les variations. | Stock en transit, détention chez un tiers, propriété, qualité et admissibilité. |
| Qualifier les engagements commerciaux et leurs effets | Parties, obligations, conditions applicables et liens aux biens concernés. | Achat/vente, transfert ou retour. Les différences ne se réduisent pas à l’existence d’une facture ; le rattachement détaillé des aptitudes reste à éprouver. |

U54 situe la différenciation des parcours dans le modèle de processus. Cela laisse à identifier les règles et faits transactionnels durables que ces parcours utilisent. Ces règles ne sont ni effacées ni toutes placées dans la couche processus par la seule qualification commerciale d’un dossier.

## Le test de frontière à poursuivre

Exemple hypothétique, sans nouveau fait d’existant : fournir 100 unités à un magasin pour une date demandée. Comparer le même besoin selon que source et destination relèvent de la même société ou de sociétés différentes. Examiner séparément :

- les quantités et dates disponibles, les protections et l’engagement de la source ;
- la prestation de livraison et ses faits de départ, transit et arrivée ;
- les parties, conditions, changements de propriété et faits nécessaires à la facturation.

Conserver une même famille d’aptitudes lorsque le problème et le résultat sont identiques, avec des règles contextualisées. Ne pas déduire cette identité du seul trajet physique. Les scénarios OMS peuvent différer tout en sollicitant ces aptitudes communes.

La précédente comparaison Achats / Réassort rapprochait des sujets de mailles différentes : **formation d’un besoin de renouvellement** et **prise d’un engagement commercial**. Un cas de réassort peut mobiliser les deux, puis promesse, exécution et stock ; il n’a pas à être rangé en entier dans une seule case. C43 conserve la formulation remplacée.

La bonne question devient : quelles aptitudes génériques rendent possibles ces différentes satisfactions de besoin, et quels ensembles de problèmes cohérents justifient des domaines ? P77 garde ouverts le niveau et les frontières de Supply Decision & Execution. Aucun déplacement de CAP011–CAP014, CAP029 ou des autres candidats n’est effectué.

## Sources et limites de consultation

- **S1** — [Setting up a Stock Transfer Process for an Intra-Company Stock Transfer](https://learning.sap.com/courses/configuring-cross-application-processes-in-sap-s-4hana-sales-and-procurement/setting-up-a-stock-transfer-process-for-an-intra-company-stock-transfer_ad0e9a99-4f15-42d1-9ba5-8eecac49d235), SAP S/4HANA, édition non précisée ; Stock Transport Orders with Outbound Deliveries et One-Step Versus Two-Step Procedure, texte consulté.
- **S2** — [Exploring the Advanced Intercompany Stock Transfer (5HP) Scenario](https://learning.sap.com/courses/managing-inventory-movements-and-stock-transfers-in-sap-s-4hana-cloud-public-edition/exploring-the-advanced-intercompany-stock-transfer-5hp-scenario_cb5f1869-1aee-4f11-b97c-22d6fc37564b), Cloud Public Edition, édition non précisée ; introduction et scénarios 1P9/5HP, texte consulté.
- **S3** — [Performing Stock Transfers Between Plants](https://learning.sap.com/courses/inventory-management-in-sap-cloud-erp/performing-stock-transfers-between-plants-2), cours dont le texte vise S/4HANA, édition non précisée ; Cross-Plant Stock Transfer, texte consulté pour les effets de valorisation.
- **S4** — [Introducing Basic Available-to-Promise](https://learning.sap.com/courses/configuring-supply-chain-business-scenarios-in-sap-s4hana-cloud-public-edition/introducing-basic-available-to-promise_ee3a33eb-4a91-4f85-a8b6-9bc1189e9540), Cloud Public Edition, édition non précisée ; Introduction to Available-to-Promise, texte consulté. Le cours nomme 2LN Basic Available-to-Promise Processing : conserver ce libellé documentaire séparément de la page 2608 citée en ELM036.
- **S5** — [Outlining Advanced Available-to-Promise](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-advanced-available-to-promise-aatp-in-sap-s-4hana), S/4HANA, édition non précisée ; introduction et Back Order Processing, texte consulté. Pas d’identité de fonctions ou de licence entre toutes les éditions déduite.
- **S6** — [Discovering the Reference Architecture Content](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), catalogue d’édition inconnue ; Business Capability Model Example, texte reconsulté.
- **S7** — [Outlining Customer Returns in SAP S/4HANA](https://learning.sap.com/courses/configuring-cross-application-processes-in-sap-s-4hana-sales-and-procurement/outlining-customer-returns-in-sap-s-4hana_fd6b26bd-b0cb-4e34-89be-8cbc6162efb3), édition non précisée ; Standard Scenarios for Customer Returns, texte consulté. Une autre leçon BKP repérée par recherche renvoyait 404 ; elle n’est pas utilisée comme preuve. Une page Help de prérequis intercompany ne fournissait pas de texte exploitable ; S1/S2 sont les preuves retenues.

[CMP032](../marche/comparaisons.md#cmp032) distingue appuis documentaires et adaptation locale. Les capacités et questions existantes conservent leurs statuts ; aucun modèle produit SAP ni norme comptable n’est adopté.

**Suite U63/U64 :** la [carte éprouvée sur les récits](25-domaines-coeur-et-epreuve-recits.md) utilise réassort, achats et exécution comme cas traversant des domaines de problèmes. ELM062 précise les sources SAP réexaminées : la leçon S5 citée dans cette note porte actuellement surtout sur l’activation ; les preuves courantes de réexamen s’appuient sur Basic ATP et le cours BOP ciblé, sans changer la provenance de la lecture antérieure.

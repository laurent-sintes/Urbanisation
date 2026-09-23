# Audit des capacités — application aux huit sous-domaines

**Appliqué au backlog le 23 septembre 2026 — U673. Aucune publication effectuée.**

[Source YAML](../modeles/backlog/capability-subdomain-audit-U667.yaml) · [Vue du backlog](../restitutions/backlog.md). Cette restitution est dérivée des données structurées.

Le modèle comprend **8 sous-domaines et 59 capacités** : 57 capacités existantes conservées dans le domaine, 2 créées dans Plans. Demand Planning et son comportement de publication sortent du périmètre, sans sous-domaine APS.

| Sous-domaine | ID conservé ou créé | Capacités |
| --- | --- | ---: |
| Master Data | business-references | 14 |
| Policies | subdomain-policies | 3 |
| Plans | subdomain-plans | 2 |
| Order Management | D04 | 11 |
| Inventory Management | D01 | 6 |
| Order Promising | D18 | 5 |
| Demand & Supply Matching | D03 | 9 |
| Fulfilment Orchestration | D06 | 9 |

## Frontières appliquées

- **Plans** ingère et expose Supply et Demand Plans fournis par l’APS externe. Supply Plan porte les mouvements de stock prévus hors achats.
- **Matching** construit et gère son master plan de matching : couverture et affectations, sans le confondre avec Supply Plan.
- **Order Promising** calcule et recommande une réponse ; il sert Order Management avant engagement et Matching pour ses arbitrages.
- **Order Management** porte les commandes et engagements ; **Fulfilment** adapte localement la réalisation en préservant promesse et grands équilibres.
- **Policies** tient les règles actives. Les décisions contextualisées sur les valeurs restent dans Matching ; les réservations restent dans Inventory.
- **Master Data** conserve les sept sujets de référence et leurs capacités distinctes, avec autorité locale Supply et maîtrise d’entreprise externe.

## Application capacité par capacité

Les identifiants et noms des capacités conservées restent stables. ATP/CTP/PTP ne sont pas fusionnées ; leurs frontières ont été précisées.

### Master Data

Fournir les références locales nécessaires pour comprendre les produits, les acteurs, les accords, les offres et le réseau mobilisés par la Supply.

| ID | Capacité | Application |
| --- | --- | --- |
| D08.d | Product Reference Ingestion | Rattachement conservé. Frontière corrigée dans la fiche. |
| D08.e | Product Reference Visibility | Rattachement conservé. Frontière corrigée dans la fiche. |
| D09.d | Party / Role Ingestion | Rattachement conservé. Frontière corrigée dans la fiche. |
| D09.e | Party / Role Visibility | Rattachement conservé. Frontière corrigée dans la fiche. |
| D11.a | Agreement Ingestion | Rattachement conservé. Frontière corrigée dans la fiche. |
| D11.b | Agreement Visibility | Rattachement conservé. Frontière corrigée dans la fiche. |
| D12.a | Product Catalog Ingestion | Rattachement conservé. Frontière corrigée dans la fiche. |
| D12.b | Product Catalog Visibility | Rattachement conservé. Frontière corrigée dans la fiche. |
| D13.a | Fulfillment Network Ingestion | Rattachement conservé. Frontière corrigée dans la fiche. |
| D13.b | Fulfillment Network Visibility | Rattachement conservé. Frontière corrigée dans la fiche. |
| D14.a | Service Catalog Ingestion | Rattachement conservé. Frontière corrigée dans la fiche. |
| D14.b | Service Catalog Visibility | Rattachement conservé. Frontière corrigée dans la fiche. |
| D16.a | Assortment Ingestion | Rattachement conservé. Frontière corrigée dans la fiche. |
| D16.b | Assortment Visibility | Rattachement conservé. Frontière corrigée dans la fiche. |

### Policies

Définir, maintenir et rendre applicables les règles qui encadrent les protections, les priorités et le recours aux ressources et prestataires Supply.

| ID | Capacité | Application |
| --- | --- | --- |
| D02.b | Supply Protection | Rattachée depuis Reference & Policy Management. |
| D19.a | Service Provider Policy | Rattachée depuis Reference & Policy Management. |
| D19.b | Demand Protection Policy | Rattachée depuis Reference & Policy Management. |

### Plans

Recevoir et rendre utilisables les Demand Plans et Supply Plans calculés hors du domaine pour éclairer la promesse et le Matching.

| ID | Capacité | Application |
| --- | --- | --- |
| plans-ingestion | Plan Ingestion | Créée : Recevoir et intégrer les Supply et Demand Plans fournis par l’APS externe, avec leur origine, horizon, version et statut. Supply Plan désigne les prévisions d’entrées ou de sorties de stock hors achats. |
| plans-visibility | Plan Visibility | Créée : Rendre consultables les projections de demande et de mouvements de stock hors achats, leurs versions, dates, conditions et fraîcheur pour éclairer la promesse et le Matching. |

### Order Management

Gérer les commandes, leurs exigences et leurs évolutions, et porter les engagements de satisfaction jusqu’à leur conclusion.

| ID | Capacité | Application |
| --- | --- | --- |
| D04.i | Sales Order | Rattachement conservé. Frontière corrigée dans la fiche. |
| D04.j | Purchase Order | Rattachement conservé. Frontière corrigée dans la fiche. |
| D04.k | Transfer Order | Rattachement conservé. Frontière corrigée dans la fiche. |
| D04.l | Return Order | Rattachement conservé. |
| D04.m | Supplier Return | Rattachement conservé. |
| D04.n | Order Structuring | Rattachement conservé. |
| D04.o | Order Lifecycle Management | Rattachement conservé. |
| D04.q | Order Archiving | Rattachement conservé. |
| D04.r | Consignment Fill-up Order | Rattachement conservé. |
| D04.t | Consignment Pick-up Order | Rattachement conservé. |
| D03.n | Fulfillment Commitment | Rattachement conservé. Frontière corrigée dans la fiche. |

### Inventory Management

Établir et rendre visibles les positions de stock, leurs mouvements, leurs régimes et les réservations qui engagent des quantités pour des besoins identifiés.

| ID | Capacité | Application |
| --- | --- | --- |
| D01.f | Inventory Tracking | Rattachement conservé. Frontière corrigée dans la fiche. |
| D01.g | Record Inventory Movements | Rattachement conservé. |
| D01.c | Inventory Visibility | Rattachement conservé. |
| D01.d | Stocktaking | Rattachement conservé. |
| D02.c | Reservation | Rattachement conservé. |
| D01.h | Consigned Inventory Management | Rattachement conservé. |

### Order Promising

Déterminer et recommander ce qu’on peut promettre, en quantité, date et conditions.

| ID | Capacité | Application |
| --- | --- | --- |
| D18.a | Supply Visibility | Rattachement conservé. Frontière corrigée dans la fiche. |
| D03.i | Available-to-Promise (ATP) | Rattachée depuis Demand & Supply Optimization. |
| D03.j | Capable-to-Promise (CTP) | Rattachée depuis Demand & Supply Optimization. Frontière corrigée dans la fiche. |
| D03.k | Profitable-to-Promise (PTP) | Rattachée depuis Demand & Supply Optimization. |
| D03.l | Delivery Schedule Decision | Rattachée depuis Demand & Supply Optimization. |

### Demand & Supply Matching

Construire et maintenir le master plan de matching qui arbitre la couverture de la demande et les affectations de ressources, en mobilisant les décisions spécialisées et en faisant appliquer les changements autorisés.

| ID | Capacité | Application |
| --- | --- | --- |
| D03.m | Order Prioritization | Rattachement conservé. |
| D03.o | Fulfillment Plan Decision | Rattachement conservé. Frontière corrigée dans la fiche. |
| D05.a | Inventory Target Decision | Rattachement conservé. Frontière corrigée dans la fiche. |
| D05.d | Group Protection Decision | Rattachement conservé. |
| D05.g | Initial Stocking Decision | Rattachement conservé. Frontière corrigée dans la fiche. |
| D05.e | Replenishment Decision | Rattachement conservé. Frontière corrigée dans la fiche. |
| D05.c | Stock Redistribution Decision | Rattachement conservé. |
| D05.f | Demand & Supply Optimization Planning | Rattachement conservé. Frontière corrigée dans la fiche. |
| D05.h | Reservation Policy Decision | Rattachement conservé. |

### Fulfilment Orchestration

Obtenir la réalisation attendue en coordonnant les prestations, leurs dépendances et leurs résultats, et rechercher des adaptations locales qui préservent la promesse de l’Order et les grands équilibres du Matching.

| ID | Capacité | Application |
| --- | --- | --- |
| D06.b | Service Capacity Visibility | Rattachement conservé. |
| D07.a | Service Requirements Decision | Rattachement conservé. |
| D07.b | Service Task Management | Rattachement conservé. |
| D07.c | Service Reconciliation | Rattachement conservé. |
| D07.d | Operations Tracking | Rattachement conservé. Frontière corrigée dans la fiche. |
| D06.d | Process Orchestration | Rattachement conservé. |
| D06.e | Service Selection Decision | Rattachement conservé. |
| D06.f | Process Adaptation Decision | Rattachement conservé. Frontière corrigée dans la fiche. |
| D05.i | Return Disposition Decision | Rattachée depuis Demand & Supply Optimization. Frontière corrigée dans la fiche. |

## Décisions de placement mises en œuvre

Les décisions de cible de stock, d’implantation et de réassort restent dans Matching pour les ajustements opérationnels de couverture ; elles ne reconstruisent pas le calcul prévisionnel externe. Return Disposition Decision rejoint Fulfilment pour le devenir logistique des biens, avec recours à Matching pour les impacts collectifs. Ces placements suivent les recommandations de l’audit, appliquées sur demande U673.

## Retrait et préservation

D17.a Demand Planning et BHV095 sont retirés du catalogue actif. Leur état antérieur, leurs liens et leurs preuves restent conservés dans le commit `364d19a90d70159d37278317c7c8f47c46971e56`. Les 80 autres comportements conservent leurs identifiants et leurs parents ; Apply Plan et Simulation & Analysis restent sous D05.f. L’audit historique U431 n’est pas rouvert.

## Portée des accords

Les noms et rattachements appliqués sont capturés à portée explicite sur le modèle final. Les formulations détaillées produites pendant la mise en œuvre et les qualifications complémentaires ne sont pas globalement adoptées. Le délai de 200 ms reste un objectif envisagé, pas une garantie. Aucune publication, aucun commit et aucun push ne découlent de cette application.

## Appuis marché

Les rapprochements CMP269–CMP272 et leurs limites sont conservés dans les annexes et les fiches. Le vocabulaire Order Promising est étayé notamment par [Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/fascp/overview-of-global-order-promising.html) et [Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations). Les frontières des produits ne prescrivent pas celles du modèle FLOW.

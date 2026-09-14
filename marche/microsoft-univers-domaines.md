# Microsoft et notre découpage Univers / Domaine

14 septembre 2026 — U184/U185. Analyse proposée, fondée sur le backlog courant et les sources Microsoft. [Correspondances structurées](../modeles/backlog/microsoft-urbanism-fit.json).

Dynamics 365 désigne une gamme ; Business Central, Finance et Supply Chain Management sont des produits de cette gamme. Ces niveaux commerciaux ne correspondent pas à nos univers et domaines. Le modèle local permet d’en cartographier les responsabilités, mais n’est pas une reproduction de leur découpage logiciel.

## Au niveau des univers

Business Central couvre finance, achats, ventes, stock, production et services dans une application. Supply Chain Management comprend des opérations transactionnelles, des workflows d’approbation organisés par rôles/hiérarchies et des fonctions d’exécution en entrepôt. Un même produit peut donc traverser les responsabilités que nous distinguons.

Supply porte notre pilotage transactionnel ; Business Services porte la prise en charge des processus transverses. Les workflows Microsoft fournissent des illustrations possibles, sans prouver une équivalence de leur produit avec tout Business Services. L’exécution logistique reste en adhérence. Aucun domaine Business Services ou nouvel univers Services n’est créé.

## Au niveau des domaines et références

| Périmètre Microsoft | Repère local | Appréciation |
| --- | --- | --- |
| Inventory management | D01 Inventory Management | Proximité de problème ; frontières à examiner, notamment réception, sortie et qualité. Le nom ne prouve pas la couverture complète. |
| Product information management | D08 Product Reference | Références et ingestion se rapprochent. Microsoft peut créer/administrer le maître ou importer un PLM/PIM ; FLOW ne conserve que la responsabilité de projection. |
| Warehouse management | Adhérence d’exécution, échanges à éprouver avec D06/D07 | Les tâches de préparation/manutention ne deviennent pas des capacités FLOW du seul fait de leur présence dans SCM. |
| Fonctionnalités achats/ventes de Business Central | Notamment D04 Order Management | D04 générique peut servir à analyser les commandes ; les parcours commerciaux du produit doivent être distingués. Pas de correspondance exhaustive établie. |

Le catalogue Microsoft de processus est encore une autre lecture : scénarios et activités enchaînées. Il peut éprouver nos capacités ; il ne fournit pas directement les domaines définis comme espaces problématiques.

## Usage proposé

Conserver notre hiérarchie métier et établir des correspondances multiples entre éléments de cette hiérarchie et responsabilités des produits. Chaque correspondance indique son recouvrement, ses écarts, sa source et son statut. Les exemples JSON sont des candidats d’analyse, sans effet sur les validations ou la release. Aucun achat de logiciel ni choix de référence principale n’est déduit.

## Sources

- [Microsoft — What is Dynamics 365?](https://www.microsoft.com/en-us/dynamics-365/what-is-dynamics-365) — consulté le 14 septembre 2026.
- [Microsoft Learn — Welcome to Business Central](https://learn.microsoft.com/en-us/dynamics365/business-central/welcome) — consulté le 14 septembre 2026.
- [Microsoft Learn — Supply Chain Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/supply-chain-management-welcome) — consulté le 14 septembre 2026.
- [Microsoft Learn — Inventory management overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-home-page) — consulté le 14 septembre 2026.
- [Microsoft Learn — Product information overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information) — consulté le 14 septembre 2026.
- [Microsoft Learn — Procurement and sourcing workflows](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-sourcing-workflows) — consulté le 14 septembre 2026.
- [Microsoft Learn — Warehouse management overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/warehouse-management-overview) — consulté le 14 septembre 2026.
- [Microsoft Learn — End-to-end scenarios and business processes](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/overview) — consulté le 14 septembre 2026.

## Localisation du stock — U186

Inventory Management est explicitement un module du produit Dynamics 365 Supply Chain Management. Le rapprochement avec notre univers Supply et D01 Inventory Management est donc clair à ce niveau. La réserve U185 porte sur les périmètres globaux et la couverture fine, pas sur une prétendue séparation du stock et de la Supply chez Microsoft. Sources MFIT03/04 relues le 14 septembre 2026.

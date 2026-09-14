# SAP ECC : Requisition, Order et notre séparation Case/Supply

14 septembre 2026 — U154/U155. Exploration du point 6 uniquement. U155 corrige le mot Requirement en Requisition ; l’analyse porte sur la séparation entre demande d’achat et commande, puis entre commerce et Supply. Les observations Storeland restent déclarées par Laurent, sans vérification indépendante de son modèle produit ou installé.

| Notion SAP | Définition consultée, reformulée | Source, version et accès |
| --- | --- | --- |
| Purchase Requisition | Demande/instruction interne aux achats pour procurer une quantité de bien ou de service à une date donnée. | [SAP ERP — Purchase Requisition](https://help.sap.com/docs/SAP_ERP/967e1c2a6a8c4183b7e07d28e7574445/4f7eb65334e6b54ce10000000a174cb4.html), version détaillée non établie. Extrait indexé consulté ; ouverture sans texte exploitable. |
| Purchase Order | Demande/instruction d’une organisation d’achat à un fournisseur ou site, avec quantité, échéances et conditions. Plusieurs quantités partielles peuvent être inscrites aux échéances. | [SAP ERP Purchasing, 6.0 EHP8 SP25 — Purchase Order](https://help.sap.com/docs/SAP_ERP_SPV/967e1c2a6a8c4183b7e07d28e7574445/a07eb65334e6b54ce10000000a174cb4.html), extrait indexé détaillé consulté. |
| Sales Order | Engagement commercial sur produits/services, prix, quantités et dates ; son traitement combine prix, disponibilité, transmission de besoins et échéancement. | [SAP ERP, 6.18 Latest — Sales Order](https://help.sap.com/docs/SAP_ERP/15f6005df5a343d096f63b554e47e14a/4a64b65334e6b54ce10000000a174cb4.html?locale=en-US&state=PRODUCTION&version=6.18.latest), extrait indexé détaillé consulté. |
| Requirements en SD | Besoins transmis notamment depuis commandes et livraisons ; la transmission peut être activée/désactivée selon les documents. | [SAP ERP — Working with Requirements in Sales and Distribution Processing](https://help.sap.com/docs/SAP_ERP/04ed152d92884a6da49c778a13aecb21/6b7bbb53707db44ce10000000a174cb4.html?locale=en-US), version détaillée non établie. Extrait indexé consulté ; page ouverte sans texte. Distinction utile mais secondaire après U155. |

Tous les contrôles datent du 14 septembre 2026. Descriptions produit, pas configurations installées. Aucun contenu inaccessible n’est présenté comme intégralement lu. Le mot contractual employé dans la description Sales Order ne fusionne pas l’Order avec notre référentiel Agreement.

## Lecture proposée

La distinction achats sert à séparer un besoin interne adressé aux achats de la commande adressée au fournisseur/site. Elle n’établit pas à elle seule une frontière entre couche Case et couche Supply. Une Requisition peut être produite par un parcours humain ou une logique de planification ; ce n’est pas nécessairement un dossier de Case Management.

La description de Sales Order confirme l’intuition d’une intégration de préoccupations commerciales et Supply dans le même document/parcours SAP. C’est un choix intégré, pas une preuve d’absence de séparation interne des fonctions et documents. Notre frontière architecturale ne se déduit pas du seul nom Order. Il n’est pas établi ici qu’un équivalent générique Sales Requisition serait requis ou systématique dans ECC ; ne pas inférer son absence absolue dans toutes extensions.

Pour poursuivre pas à pas, trois notions sont proposées à distinguer : le besoin exprimé, le dossier qui en organise le traitement (Case), et l’engagement/instruction transactionnel retenu (Order/Command à arbitrer). Demand et Case ne sont pas des synonymes automatiques. Command peut exprimer une instruction ; ne pas le confondre automatiquement avec la commande métier persistante. Aucune adoption des noms, d’un modèle d’objets, d’une cardinalité ou d’une implémentation n’est faite ici.

## ATP/CTP validés en U154

Le point fort des définitions U148 est la différence de résultat : promesse faisable sous engagements/politiques donnés, versus plan de changements permettant une promesse. La différence n’est pas présent/futur : ATP peut mobiliser du futur déjà engagé. Le calcul ou plan ne réalise pas seul ses mesures. Le nom CTP garde une portée locale plus large que les descriptions produit consultées. Cette orientation est appliquée à D03, sans publication.

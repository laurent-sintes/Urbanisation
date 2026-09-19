# Positionnement proposé de Logistics Visibility — U300

**Audit clos U431.** Tous les candidats sont intégrés, couverts par l’existant ou retirés. P04/P10/P12 ne créent aucun comportement supplémentaire. Frontière commerciale et financière externe à Supply ; règles et contrats détaillés conservés comme travaux ultérieurs non bloquants. [Bilan de clôture](cloture-U431.md). Les états et propositions antérieurs ci-dessous conservent leur portée historique.

**État courant U427 :** Replenishment Decision porte Requirement-based Replenishment (BHV083), Target-based Replenishment (BHV084) et Replenishment Adjustment (BHV085). Deux politiques et un mécanisme combinable ; noms, définitions présentées et rattachements adoptés. Exemples, justifications et comparaison Microsoft documentés avec leur portée éditoriale. P01–P03 sont intégrés : le point réassort est clos. Les autres arbitrages de l’audit restent distincts ; les conclusions antérieures de non-décomposition et de réouverture ci-dessous sont historiques.

**État courant U424 :** Lifecycle unique en D04 avec six dimensions et leurs états explicites. Rescheduling BHV041 est intégré à Preparation & Revision BHV038 ; Cancellation BHV042 est intégré à Termination BHV043, avec distinction entre annulation et clôture. Les anciens identifiants sont conservés dans les preuves et ne sont pas réutilisés. D03 mobilise Lifecycle ; D06 garde orchestration et réalisations. Nouvelles formulations et listes détaillées éditoriales. Les décompositions antérieures ci-dessous sont historiques.

**État courant U420 :** Order Archiving appartient à D03 ; Order Lifecycle Management appartient à D04, avec Order Release. Structuring et Split restent dans D03. Identifiants, définitions et parents des comportements conservés. Les mentions U417/U418 ci-dessous sont historiques et remplacées sur ces rattachements. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml).

**État courant U417/U418 :** dans D03 Order Backlog Management, Structuring porte Order Splitting et Lifecycle porte Order Release. Les capacités D04.n/D04.o conservent leurs identifiants historiques. Planning prépare les scénarios ; Lifecycle autorise ; Process Orchestration coordonne les services. Gel et suspension sont combinables, sans séquence universelle. Aucun ajout de nœud ou comportement ; arbitrage de placement du carnet résolu. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml). Les anciens rattachements ci-dessous sont historiques.

**État courant U414 :** Order Backlog Planning (D03.p) est créé dans D03. Order Release BHV039 y est déplacé, identité et définition conservées. Lifecycle conserve huit comportements ; Split et Structuring restent en D04 pour le prochain arbitrage. Planning mobilise les décisions et prépare la prise en charge ; affectation, promesse et orchestration gardent leurs responsabilités. Aucun comportement supplémentaire : 47 capacités et 73 comportements. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml). Les anciens rattachements ci-dessous restent historiques.

**État courant U413 :** D03 devient Order Backlog Management. Le travail collectif du carnet prépare son engagement vers les processus, en mobilisant les décisions spécialisées. D04 conserve la demande par intention. Réexamen ciblé de Lifecycle/Structuring : parents inchangés, aucune nouvelle capacité ou comportement. P11 demeure intégré à Order Release ; son placement côté carnet reste à concrétiser. [Mandat, comparaison et réexamen](../../modeles/backlog/order-backlog-review.yaml). Les noms et positions des états précédents sont historiques.

**État courant U410 :** P11 est résolu par enrichissement d’Order Release (BHV039) : conditions individuelles et collectives, complétude, éléments indispensables et traitement partiel. Aucun comportement ajouté ; autorisation distincte de l’affectation et de Process Orchestration. Autoriser ensemble ne signifie pas démarrer simultanément. Les mentions antérieures de P11 ouvert sont historiques. [Accord et comparaison](../../modeles/backlog/order-lifecycle-behaviors.yaml).

**État courant U409 :** le Process orchestre des Services. D06 devient Process Management ; Process Orchestration et Process Adaptation Decision restent distincts. Operations Tracking porte les trois visibilités physiques et Process Tracking. Neuf noms adoptés ; Service Catalog Ingestion et Service Reconciliation sont deux intitulés dérivés proposés. Aucun ajout de comportement ni changement de responsabilité. Les intitulés des états datés ci-dessous restent historiques. [Convention et comparaison](../../modeles/backlog/execution-services-review.yaml).

**État courant U406 :** 47 capacités et 74 comportements. Warehouse Visibility, Transportation Visibility, Store Visibility et Business Process Tracking intégrés sous Execution Tracking (BHV079–082). Tasks et appels sont des objets suivis, pas des niveaux de comportement. Digital Service Visibility est remplacé ; le besoin numérique demeure couvert. [Portées et comparaison](../../modeles/backlog/execution-services-review.yaml). Les propositions et mentions de non-intégration ci-dessous sont historiques.

**État courant U403 :** 47 capacités et 74 comportements. Supplier Confirmation (BHV078) complète Purchase Order et résout A06 sur le catalogue : demande, réponse fournisseur et engagement accepté distincts ; impacts, mutations et promesse client gardent leurs responsables. Refuser un report ne supprime pas le risque annoncé. [Explication et comparaison](../../modeles/backlog/purchase-order-behaviors.yaml). Les mentions antérieures d’un point A06 ouvert restent historiques.

**État courant U402 :** 47 capacités et 74 comportements. Les trois mécanismes CTP BHV075–077 sont intégrés : ressources supplémentaires, alternatives de satisfaction et réexamen d’engagements. P14–P16 ne sont plus conditionnels ; A05 est résolu sur la frontière de catalogue, les règles détaillées restant distinctes. Fulfillment Plan Decision conserve le choix collectif. [Portée et comparaison](../../modeles/backlog/d03-review.yaml). Les états datés ci-dessous conservent leur valeur historique.

**État courant U391 :** Purchase Order porte Stock Procurement, Direct Delivery et Service Procurement (BHV058–060). Consignation instruite séparément dans la gestion du stock. [Accord et intégration](../2026-09-18-purchase-order-U391/README.md).

**État courant U388 :** Return for Repair (BHV057) complète Supplier Return : restitution attendue du même bien réparé, distincte du remplacement. L’ajout n’est plus conditionnel ; achats de prestation et exécution conservent leurs responsabilités. [Portée de l’ajout](../2026-09-18-supplier-repair-U388/README.md).

**État courant U387 :** Supplier Return porte Return for Credit et Return for Replacement (BHV055–056), distingués par l’apport de remplacement attendu. Finance, achat et exécution restent distincts. [Accord et intégration](../2026-09-18-supplier-return-U387/README.md).

**État courant U385 :** définition élargie de Customer Return et cinq parcours combinables adoptés : Return to Stock, Repair and Refurbishment, Return to Supplier, Return to Customer et Scrapping (BHV050–054). Les axes commerciaux et les autres filières restent à instruire. [Accord et intégration](../2026-09-18-customer-return-U385/README.md).

**État courant U384 :** noms courts Sales Order, Purchase Order, Transfer Order, Customer Return et Supplier Return adoptés. Cinq parcours Customer Return détaillés en proposition dans `modeles/backlog/customer-return-behaviors.yaml`, sans ajout au catalogue à ce stade. [Nommage et étude](../2026-09-18-customer-return-U384/README.md).

**État courant U383 :** cinq capacités par type d’Order sont rétablies sous D04 ; Order Type D04.p est retiré. Lifecycle, Structuring et Archiving restent transverses. Return Disposition Decision porte Policy-based Disposition et Value Recovery Optimization (BHV048–049). Les prises en charge des retours restent à détailler. Les états datés ci-dessous sont historiques. [Portée et comparaison](../2026-09-18-orders-disposition-U383/README.md).

**État courant U380 :** Return Disposition Decision (D05.i) est adoptée sous Inventory Optimization, sans comportement. A04 est résolue sur le devenir logistique du bien ; autorisation commerciale, remboursement et remplacement client restent distincts. [Accord et intégration](../2026-09-18-return-disposition-U380/README.md).

**État courant U378 :** Fulfillment Plan Decision (D03.o) produit le scénario collectif ; D03 porte le nom adopté Fulfillment Optimization. A02 est résolue sur la responsabilité ; les contrats détaillés restent proposés. Aucun sous-niveau ou comportement ajouté. Les états U364 et antérieurs ci-dessous sont historiques. [Accord et intégration](../2026-09-18-fulfillment-plan-U378/README.md).

**État courant U364 :** Supply Assignment porte application d’un plan, complément préservant les affectations et réaffectation des liens modifiables (BHV045–BHV047). La distinction stabilité/adaptation est adoptée ; les décisions spécialisées et Freezing gardent leurs responsabilités. A01/A02 restent ouverts. [Portée et comparaison](../2026-09-18-supply-assignment-U364/README.md).

**État courant U363 :** D04 comporte Order Type (cinq variantes), Order Lifecycle Management (neuf comportements), Order Structuring et Order Archiving. Split est une mutation avec filiation ; Spread concerne l’affectation des ressources entre Orders. Les états datés ci-dessous sont historiques. [Refonte et portée](../2026-09-18-d04-U363/README.md).

**Validation U350 :** Order Freezing est le nom adopté pour BHV037. Le principe et le parent U349 sont conservés ; les détails et contrats restent proposés.

**État courant U349 :** Order Lifecycle Management porte Order Firming (BHV036) et la protection contre les réoptimisations (BHV037, nom éditorial Order Freezing). Affermissement, gel et mise en attente sont distincts. Accord et limites dans `modeles/backlog/order-lifecycle-behaviors.yaml` ; P11 reste ouvert. Catalogue : 41 capacités et 28 comportements.

**Clarification U345 / C99 :** Supply Assignment porte l’application des affectations d’un plan ; D04 garde ses effets sur les Orders. Trois mécanismes documentés en proposition dans `modeles/backlog/supply-assignment-mechanisms-review.yaml`. Simulation & Analysis explicite les recommandations ; compensation logicielle hors de cette décomposition métier. Aucun nouveau nœud.

**État courant U343 :** les quatre comportements BHV032–BHV035 et le parent D05 sont adoptés, dans la portée des noms et responsabilités présentées. Modalités détaillées, contrats et comparaisons restent proposés. Les mentions U342 ci-dessous décrivent l’état antérieur. [Portée de validation](../2026-09-18-reservation-policy-adoption/README.md).

**État courant U342 :** Reservation Policy Decision (D05.h), nom et définition adoptés. Quatre comportements BHV032–BHV035 documentés et proposés ; parent D05 proposé. Catalogue : 41 capacités et 26 comportements, dont ces quatre nouvelles propositions. [Recensement et frontières](../2026-09-18-reservation-policy/README.md). A01 reste ouvert au-delà de cette décision.

**État courant U334 :** Stocktaking porte politique et demandes de vérification, ainsi que Periodic Physical Inventory (BHV029), Cycle Counting (BHV030) et Spot Counting (BHV031). P08/P09 intégrés ; traitement des écarts commun et réalisation physique par les exécutants. Catalogue : 40 capacités, 22 comportements. Les sections datées conservent leurs états historiques. [Portée de la validation](../2026-09-18-stocktaking-behaviors/README.md).

**État courant U332 :** Inventory Target Decision porte trois comportements frères : Store Inventory Optimization (BHV026), Distribution Center Inventory Optimization (BHV027) et Multi-Echelon Inventory Optimization (BHV028). P13 est intégré ; P12 reste sans création recommandée. Catalogue : 40 capacités et 19 comportements. Les sections datées ci-dessous conservent leurs états historiques. [Portée de la validation](../2026-09-18-inventory-target-behaviors/README.md).

**État courant U318 :** deux comportements intégrés sous Stock Redistribution Decision : rééquilibrage entre sites (BHV024) et consolidation des stocks dispersés (BHV025), dont assortiments de tailles et reliquats. Définitions françaises et rattachements adoptés ; noms anglais éditoriaux. Catalogue : 40 capacités, 16 comportements. [Portée de l’accord](../2026-09-18-redistribution-behaviors/README.md). P01–P03 sur le réassort restent ouverts. Les textes datés ci-dessous conservent leur portée historique.

**Réexamen U324 / C98 :** les min/max peuvent dépendre des besoins et varier par période. Coverage Target Decision détermine les valeurs ; Supply Protection gouverne leur application ; Replenishment Decision détermine les apports. La création des comportements proposés U323 est suspendue faute de bénéfice différenciant établi. [Comparaison CMP111](../../marche/comparaisons.md#cmp111).

Décrire Logistics Visibility comme comportement d’Execution Tracking dans D06 Execution Management. Maintenir la capacité générique de suivi des prestations physiques et non physiques.

**Définition proposée.** Rendre visible et traçable la progression physique des marchandises depuis leur prélèvement dans un espace de stockage jusqu’à leur remise au point de destination, en reliant les événements de préparation, manutention, transport et étapes intermédiaires, avec leur localisation, quantités, jalons, estimations et écarts.

**Pourquoi décomposer.** La continuité du parcours physique nécessite de relier les marchandises, unités logistiques, prestations et événements à travers plusieurs étapes et exécutants. Elle permet de retrouver où sont les quantités, ce qui leur est arrivé et ce qui reste attendu malgré les fractionnements, regroupements et changements de prise en charge. Ce bénéfice dépasse la consultation isolée du statut d’une prestation ; il ne crée pas un comportement par étape ou interface.

**Cohérence FLOW.** Le mandat de D07.d couvre déjà le suivi des faits, jalons et estimations de toutes les prestations. La spécialisation conserve la maille large de la capacité, évite de créer deux suivis concurrents du même parcours et ne supprime pas les prestations documentaires ni les ressources futures encore attendues.

**Marché.** SAP relie visibilité physique, jalons, ETA, exceptions et contexte des Orders ; son intégration prévoit les événements de préparation. GS1 décrit le partage des faits de localisation/mouvement entre partenaires. Ces sources étayent le résultat et sa complexité ; elles ne prescrivent pas le rattachement FLOW proposé.

[S29 — SAP](https://www.sap.com/products/business-network/global-track-and-trace.html), [S38 — SAP](https://help.sap.com/docs/business-network-global-track-and-trace/send-documents-from-erp-to-gtt/c667ee93eaa8461da2dcfc24cf53e793.html), [S41 — GS1](https://www.gs1.org/standards/epcis)

## Alternatives

- **Capacité sœur autonome sous D06** : Défendable si FLOW veut distinguer durablement visibilité logistique et suivi des autres services. Exigerait alors de réduire explicitement le périmètre d’Execution Tracking ; conserver les deux mandats actuels au même niveau laisserait un recouvrement.
- **Renommer Execution Tracking en Logistics Visibility** : Non recommandé : le mandat actuel comprend aussi résultats documentaires et autres prestations non physiques. Le nom adopté pour le parcours physique ne suffit pas à supprimer cette responsabilité.
- **Sous Inventory Visibility** : Non recommandé : Inventory Visibility décrit quantités et états ; le parcours logistique traverse les prestations d’exécution. Des faits partagés ne font pas un lien de décomposition.

## Frontières

| Responsabilité | Résultat |
| --- | --- |
| Inventory Visibility — D01.c | Quantités physiques, états logiques et ressources futures ; pas de disparition de stock au premier picking. |
| Logistics Visibility — comportement proposé | Parcours physique, localisation, progression, jalons, ETA et écarts visibles, depuis le picking au point final. |
| Execution Reconciliation — D07.c | Rapprocher et qualifier les résultats réalisés face aux attendus ; rendre visible 98 sur 100 ne clôt pas le rapprochement des deux manquants. |
| Execution Adaptation Decision — D06.f | Choisir la variation métier rendue nécessaire par un aléa. |
| Execution Orchestration — D06.d | Coordonner la réalisation des prestations et les conséquences du plan retenu. |

**Exemple.** Un transfert porte sur 100 pièces : 60 sont préparées puis chargées, 40 attendent ; une partie des colis passe par un dépôt. Le comportement reconstitue la position et la progression des quantités, sans attendre que chaque Service Order soit clôturé. Le signalement d’un retard ne choisit pas le transporteur de remplacement.

**Arbitrage.** Logistics Visibility est-il un comportement spécialisé du suivi de toute prestation, plutôt qu’une capacité autonome ? Proposition : comportement sous D07.d Execution Tracking, dans D06. Valider la justification de décomposition sur ce bénéfice de continuité physique.

**Déjà établi.** Le nom U297, le parcours physique demandé U296 et le principe sans doublon des exceptions U299. Aucun nouvel arbitrage sur l’implémentation WMS/TMS ou Case Management requis pour ce rattachement.

Si adopté : créer un seul comportement et sa relation contains, consigner la justification sur le parent et maintenir les responsabilités non physiques. À ce stade, aucun changement du catalogue ou publication.

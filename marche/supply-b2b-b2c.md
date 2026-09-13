# Supply : socle commun et variantes B2B/B2C

Recherche du 13 septembre 2026 — U140, C77, CMP065. Orientation utilisateur : univers Case différé, univers Supply exploré maintenant, Order distinct du Case, domaine Order Management commun. Conclusions détaillées ci-dessous proposées par Codex ; aucune équivalence globale de marché ni preuve de déploiement.

## Réponse

Le marché offre des socles communs, mais les différences de supply ne se limitent pas au commercial. Les contraintes de satisfaction et de réalisation peuvent différer : fractionnement, dates, conditionnements, regroupements, priorités, destinations et réception. Cela appelle des capacités suffisamment riches et des règles explicites, sans imposer un domaine B2B et un domaine B2C.

Une classification client ne remplace pas les caractéristiques de la commande : une entreprise peut demander une pièce urgente et un particulier plusieurs livraisons volumineuses. Les exemples ci-dessous sont des cas d’épreuve proposés, pas des statistiques de fréquence établies.

## Constats du marché

- **SAP S/4HANA for Fashion and Vertical Business** présente un socle intégré pour wholesale et retail, avec segmentation par client/canal/région, destination ou caractéristiques produit fixées plus tard et approvisionnement flexible. C’est un appui à un socle commun riche ; pas la preuve que toutes les règles sont identiques ni un catalogue de capacités adopté. [Cours SAP](https://learning.sap.com/courses/outlining-sap-s-4hana-for-fashion-and-vertical-business-and-implementing-best-practices/comparing-with-sap-fashion-management-solution-fms-1), Benefits et Flexibility, texte lu le 2026-09-13 ; cours évolutif, édition exacte inconnue.
- **Microsoft Dynamics 365 Supply Chain Management** utilise des delivery schedules sur commandes de vente et d’achat : une quantité est répartie sur plusieurs livraisons avec dates, quantités, modes et dimensions de stockage propres. C’est une aptitude d’échelonnement exprimée sans imposer deux domaines selon la catégorie du client. [Delivery schedules](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-schedules), introduction et fonctionnement, texte lu ; mise à jour affichée 2025-05-07.
- **IBM Sterling OMS** conserve la famille Sales/Purchase/Return/Transfer déjà vérifiée en ELM112. La présentation produit mentionne B2C et B2B, et une vue commune commandes/stock. Ouverture directe désormais 403 ; l’appui B2B/B2C repose sur l’extrait indexé et la lecture précédente, pas une inspection exhaustive de fonctionnalités. [Product overview](https://www.ibm.com/docs/en/order-management?topic=overview-sterling-order-management-system-product), introduction, documentation évolutive sans édition précise.

Ni ces constats ni la typologie TM Forum ne prouvent une capacité logicielle illimitée. Il faut distinguer couverture fonctionnelle et dimensionnement des réalisations futures.

## Contraintes à éprouver sur le modèle

| Dimension | Variantes à supporter, sans les enfermer dans B2B ou B2C | Point d’accueil local proposé |
| --- | --- | --- |
| Quantités et unités | Pièce, carton, lot, assortiment ; multiples et conversions à expliciter. | Références produit/conditions reçues, contenu de l’Order ; contraintes utilisées par promesse et exécution. |
| Temps | Livraison unique, échéancier, fenêtre de réception, délai maximal. | Order exprime la contrainte ; Order Promising décide de la faisabilité ; D07 suit la réalisation. |
| Fractionnement et regroupement | Livraison partielle autorisée/interdite, lignes à servir ensemble, plusieurs destinations. | Contraintes de l’Order et décisions de promesse ; besoins opérationnels en D07. |
| Priorités | Protection par population, service prioritaire, réaffectation de ressources. | Inventory Management et Order Promising ; cas Boardriders déjà déclarés. |
| Acheminement et réception | Colis ou palettes, exigences de conditionnement, rendez-vous ou consignes de réception. | Références et contraintes consommées par la Supply ; réalisation et autorités logistiques hors développement FLOW. |
| Retours | Unitaire ou groupé, relié à la fourniture initiale, partiel ; destination et état reçu. | Order de retour, faits D07, mouvements/états D01 ; traitement commercial dans Case. |
| Échelle | Quantité par ligne, lignes par Order, Orders simultanés, pics, fréquence des modifications. | Exigences à quantifier ; aucune nouvelle capacité métier créée par un seuil technique. |

Les besoins d’échelonnement, regroupement ou conversion pourraient faire apparaître des lacunes de capacité dans la carte actuelle. Il faut les comparer aux définitions avant de les réduire à des paramètres ou d’ajouter une sous-capacité. Ni les différences de comportement ni les grands volumes ne disparaissent grâce à un moteur.

## Case, Order et décisions

La séparation retenue est locale : Case porte la demande dans son contexte ; Order porte son pilotage transactionnel. L’analogie avec TM Forum porte sur la séparation des responsabilités et représentations, pas sur une équivalence officielle de nos objets. Les liens et cardinalités restent ouverts.

Order Management peut recevoir ou faire évoluer des Orders de diverses natures selon les autorités convenues. Il ne récupère pas automatiquement toutes les décisions : source, promesse et affectation restent rattachées à leurs domaines. La liste héritée de D04 reste à auditer avec D07 ; Return and Replacement Decision ne devient pas validée par le seul ajout des retours au périmètre.

**DMN** modélise les décisions et règles ; il complète BPMN et CMMN, sans remplacer à lui seul un workflow ou un cycle de vie. [OMG — DMN](https://www.omg.org/dmn/), présentation officielle consultée le 2026-09-13, notation sans choix de version ou moteur dans FLOW. Les invariants métier, autorisations, états et faits restent explicités indépendamment des moteurs.

## Application au projet

D04 est renommé Order Management dans le backlog selon l’orientation U140. Le nom est validé dans cette portée ; la définition et la finalité reformulées sont proposées par Codex. Les capacités ne sont pas modifiées ni validées collectivement. Le principe Case/Supply est enregistré en JSON et dans AGENTS.md ; la hiérarchie détaillée des univers reste à construire. Aucune release publiée.

# Microsoft : catalogue de processus et éclairage sur le stock

## Structure et portée

Le catalogue public Microsoft organise l’implémentation de Dynamics 365 en six niveaux : processus de bout en bout, aire de processus, processus, scénario, processus système et cas de test. Les aires regroupent souvent des fonctions ou départements ; les scénarios décrivent des configurations réutilisables ; les niveaux inférieurs rejoignent les écrans et la validation du logiciel. Les six niveaux ne sont donc pas six profondeurs de capacités métier. L’introduction indique quinze parcours de bout en bout ; le détail de chaque entrée n’est pas nécessairement rédigé. [MS01](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/about), sections « What’s in the catalog? » et « Catalog IDs », mise à jour affichée 08/01/2026.

La numérotation distingue notamment 40 pour le cycle de vie des produits, 60 pour les flux de stock/livraison, 65 pour la commande jusqu’à l’encaissement et 75 pour l’approvisionnement jusqu’au paiement. La vue générale prévient que les titres correspondent au catalogue de juillet 2026 mais que certains schémas restent antérieurs : ce contenu web ne vaut pas export homogène de cette édition. [MS02](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/overview), introduction et tableau des parcours. Consultation de toutes les sources ci-dessous : 09/09/2026 ; classeur complet non acquis.

## Contenus commerce observés

| Thème | Contenu effectivement décrit | Nature et preuve |
| --- | --- | --- |
| Articles et données produit | Gestion du cycle de vie, enrichissement d’attributs, catégories et relations entre produits ; merchandising retail. | Processus plus large que le référentiel opérationnel. MS03, présentation du cycle de vie. |
| Fournisseurs et achats | Création/tenue des fournisseurs, contrats, demandes et commandes d’achat, confirmation, transmission et retours fournisseur. | Aires de processus et fonctions de réalisation. MS04, relations fournisseur et acquisition de biens/services. |
| Stock et inventaire | Suivi des niveaux, mouvements, ajustements de gains/pertes et comptage tournant. | Une même aire réunit politique, surveillance, réassort et faits de stock. MS05, maintien des niveaux de stock. |
| Réassort | Plans de réapprovisionnement associés au maintien des niveaux. | Présence du thème ; politique comparable à IRMA non établie. MS05. |
| Entrées, sorties et exécution | Réception/inspection/rangement, préparation/emballage/expédition, retours clients à l’entrée ; entrepôts et transport. | Parcours d’exécution. MS05, flux entrants/sortants et transport. |
| Commandes, disponibilité et allocation | Commandes de vente multicanales, dates de livraison et promesse ; renvois vers la fonction d’allocation. | Les « capabilities » listées sont explicitement celles des produits Dynamics. MS06, gestion des commandes. |
| Retours | Commandes de retour et annulations dans la vente ; réception du retour dans les flux entrants ; retours fournisseurs dans l’achat. | Même thème réparti entre plusieurs parcours. MS04/MS05/MS06. |
| SAV et dossiers | Réception, affectation, investigation et clôture des demandes, réclamations et problèmes clients ou salariés. | Processus de dossier plus large que le SAV commerce. MS07, présentation du traitement de dossier. |

Sources des lignes :

- **MS03** — Microsoft, [Introduction to the design to retire end-to-end business process](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/design-to-retire-introduction), section « Design to retire overview ». Page évolutive ; édition de catalogue non attribuée au passage.
- **MS04** — Microsoft, [Overview of the Source to pay business process areas](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/source-to-pay-areas), sections fournisseur, contractualisation et acquisition ; mise à jour affichée 20/05/2025.
- **MS05** — Microsoft, [Overview of the Inventory to deliver business process areas](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/inventory-to-deliver-areas), sections maintien des niveaux, entrées et sorties ; page évolutive.
- **MS06** — Microsoft, [Overview of the Order to cash end-to-end business process](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/order-to-cash-areas-overview), sections politiques et commandes ; mise à jour affichée 24/04/2026.
- **MS07** — Microsoft, [Help organizations manage and optimize their case to resolution processes](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/case-to-resolution-introduction), section « Case to resolution overview » ; mise à jour affichée 26/04/2024.

## Évolution réelle de la hiérarchie

La note de février 2025 décrit le déplacement des processus de rappel/retour depuis le traitement des dossiers vers la commande/encaissement. Elle décrit aussi le passage de certains regroupements produit à un niveau inférieur. Cela montre qu’un besoin conservé peut changer de rattachement et de profondeur : un comparateur durable doit tracer l’édition et le déplacement, pas seulement le libellé ou le numéro de niveau. [MS08 — changements de février 2025](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/about-whats-new-2025-february), sections « Changes to Case to resolution processes » et « Improvements to Design to retire processes ».

## Allocation : un rapprochement fonctionnel précis

La documentation Inventory Visibility décrit une préallocation virtuelle de stock à des groupes (canaux, clients, régions), avant les ventes individuelles. Elle vise à protéger les quantités et à suivre leur consommation ; elle est distinguée d’une réservation associée à une transaction. Les deux mécanismes peuvent fonctionner séparément ou être articulés. C’est un appui pour rapprocher la finalité de protection de groupes de celle de SAP Supply Protection, tout en laissant ouverts les horizons, formules, priorités et effets détaillés. Ce constat porte sur deux fonctions de produit, pas sur une équivalence de leurs catalogues métier. [MS09 — Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), sections « Business background and purpose », « Allocation virtual pool » et « Difference between inventory allocation and soft reservation » ; mise à jour affichée 13/08/2025.

La définition des niveaux d’une hiérarchie d’allocation dans ce produit concerne des groupes de consommation : elle est encore distincte des six niveaux du catalogue de processus et des niveaux d’une carte de capacités. Aucun paramétrage Microsoft ou SAP n’est attribué à Beaumanoir.

## Conséquence pour la comparaison

Le catalogue Microsoft fournit un contrôle concret des parcours et de leur réalisation. Il peut aider à retrouver les sujets récurrents et les variantes B2B/B2C. Ses contenus de finance, de planification et d’organisation sont plus larges que le socle commerce retenu ; les extraire sans conserver leur type ferait perdre cette différence. La correspondance doit passer par un résultat métier explicite, puis préciser quel processus le mobilise et quelle fonction logicielle le réalise.

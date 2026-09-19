# ATP, aATP et couverture — U260

Étude du 16 septembre 2026. État comparé : backlog après U251, discussion U256–U260. Correspondance CMP087 proposée ; principe ATP accepté en U260, compléments détaillés proposés. Aucun changement du catalogue de capacités ni publication.

## Couverture : deux registres séparés

Le glossaire de modélisation porte la convention de description MOD005 : toujours préciser **ce qui est couvert, par quoi, dans quel périmètre/horizon et selon quel critère**. Une couverture candidate, une affectation enregistrée, une promesse confirmée et une réalisation constatée ne sont pas interchangeables ; ces qualifications ne constituent pas un cycle de statuts imposé.

Le glossaire métier précise TER022, déjà existant, et ajoute TER077 pour la couverture de stock. Exemple local : une demande de 100 pièces peut avoir une couverture candidate de 60 pièces sur stock et 40 sur une réception prévue. Cela ne prouve ni leur affectation ni la confirmation d’une promesse. Dire que le stock représente dix jours de consommation répond à une autre question. Les définitions rédigées restent proposées.

## Définitions de référence

L’extrait officiel **APICS CPIM 6.1, édition 2019**, cite le Dictionary, 15e édition : ATP exprime la part non engagée du stock et de la production planifiée disponible pour soutenir la promesse. Il s’agit d’une **quantité**, appréciée dans le temps. Source historique vérifiée, pas une consultation du dictionnaire le plus récent. [S1, pages imprimées 1-208–1-209](https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf).

Microsoft Dynamics 365 SCM décrit également une quantité promettable à une date et considère stock non engagé, délais, réceptions et sorties prévues. Son ATP ne se limite donc pas au stock physiquement présent. Cette page distingue ATP et CTP par la prise en compte des capacités ; cette frontière produit ne remplace pas notre articulation D03/D06. [S2, Order promising, sections méthodes et CTP](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations).

Notre capacité ATP désigne l’aptitude à établir les possibilités de promesse. **Exiger une couverture explicative est un choix FLOW compatible avec ces références, pas une définition universelle imposant un lien à chaque lot.** Le glossaire TER044 conserve la définition actuelle et explicite cette distinction.

## Ce qu’apporte SAP aATP

Le cours SAP présente un ensemble de fonctions : PAC établit les quantités/dates confirmables ; Release for Delivery intervient dans la distribution des quantités avant lancement logistique ; Review Availability Check Result rend les résultats consultables. [S3, présentation fonctionnelle](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-advanced-available-to-promise-aatp-in-sap-s-4hana).

| Fonction native SAP | Résultat ou rôle documenté | Rapprochement FLOW proposé, partiel |
| --- | --- | --- |
| Product Availability Check — PAC | Quantités et dates de satisfaction | ATP, puis articulation avec échéancier et confirmation |
| Product Allocation — PAL | Limiter la consommation de groupes sur une période | Supply Protection pour gérer les règles ; ATP pour les respecter |
| Supply Protection — SUP | Préserver des quantités pour des groupes, avec protections mutuelles ou priorisées | Supply Protection ; Stock Allocation Decision détermine les quantités souhaitables |
| Alternative-Based Confirmation — ABC | Rechercher d’autres sites ou produits admissibles | ATP ou CTP selon les adaptations nécessaires, frontière à instruire |
| Backorder Processing — BOP | Réexaminer les confirmations lorsque offre ou demande changent | Prioritization, ATP/CTP, Promise Revision et Supply Assignment |
| Supply Assignment — ARun | Affecter les ressources appropriées aux besoins, notamment dans BOP | Supply Assignment ; équivalence complète non établie |
| Release for Delivery — RefDy | Préparer la distribution/libération vers la logistique | Articulation D03, cycle d’Order D04 et pilotage D06 à préciser |
| Supply Creation-Based Confirmation — SBC | Mobiliser PP/DS pour créer la supply manquante et établir la confirmation | CTP et mise en action distincte ; aucune production interne FLOW déduite |

PAL, ABC, BOP et ARun : [S4, sections portant ces noms](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5).

SUP illustre un cas proche de FLOW : protéger le canal e-commerce des commandes wholesale reçues plus tôt dans la saison. La protection d’un groupe ne désigne pas l’affectation à une commande identifiée. [S5, Supply Protection, introduction et variantes](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-).

SBC relie aATP à PP/DS : si les ressources existantes sont insuffisantes, le système peut créer des ordres planifiés, demandes d’achat ou de transfert. La faisabilité tient alors compte des composants et capacités. Cela montre que le périmètre produit **aATP déborde notre ATP et rejoint des responsabilités CTP**. [S6, Supply Creation-Based Confirmation](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-supply-based-confirmation-sbc-).

Ces rapprochements sont une analyse FLOW ; SAP ne propose pas notre séparation de capacités. Consulter une gamme ne prouve pas ses fonctions installées chez Beaumanoir.

## Périmètre ATP proposé pour la suite

**Établir les quantités et dates auxquelles une demande peut être satisfaite par les ressources présentes ou futures admissibles dans la situation de référence, et expliciter la couverture qui rend ces résultats réalisables.** Formulation de travail, non substituée à D03.i.

Quatre points à challenger :

1. **Situation de référence.** Quels stocks, réceptions attendues, sites, substitutions autorisées, engagements concurrents et règles sont admissibles ? Une ressource future déjà prévue n’est pas automatiquement du CTP.
2. **Résultat.** Quantité/date, sources au niveau utile, hypothèses et reliquat ; éviter d’exiger une affectation à un lot si produit/site/horizon suffit. Distinguer disponibilité, expédition et livraison grâce aux contraintes D06.
3. **Variantes et choix.** ATP peut-il fournir plusieurs couvertures ? Qui retient source et substitution ? PTP porte l’arbitrage économique et Delivery Schedule Decision l’échéancier ; leur articulation avec le choix de couverture reste à préciser.
4. **Effets.** Séparer possibilité calculée, affectation, réservation et confirmation. Ne pas laisser Supply Assignment refaire implicitement un arbitrage que l’on attribue à une décision.

Cas d’épreuve local : 100 pièces demandées vendredi, 60 disponibles et 40 sur réception déjà prévue lundi. ATP expose cette possibilité tardive et l’insuffisance vendredi. Si vendredi est impératif, elle ne satisfait pas la contrainte. Créer ou accélérer un apport relève d’une adaptation CTP. Une alternative déjà admissible depuis un autre site peut rester ATP : le seul changement de site ne suffit pas à classer une solution CTP. Déplacer un engagement existant ou déroger à une protection soulève une autre décision et son autorisation.

## Sources et limites de consultation

Toutes consultées le 16 septembre 2026, paraphrases sans reproduction intégrale.

| Source | Référence / élément | Édition et passage réellement consulté |
| --- | --- | --- |
| S1 | MKT21 / ELM082, nouvelle vérification | CPIM 6.1, 2019 ; PDF pages 1–2 pour les définitions ATP, extrait historique |
| S2 | MKT14 / ELM158 | Microsoft Learn évolutif, mise à jour affichée 2026-04-21 ; méthodes, ATP calculations, CTP calculations |
| S3 | MKT13 / ELM159 | SAP Learning, S/4HANA ; cours évolutif sans édition unique affichée, présentation des fonctions et RefDy |
| S4 | MKT13 / ELM160 | SAP Learning, S/4HANA ; cours évolutif sans édition unique affichée, sections PAC/PAL/BOP/ABC et note ARun |
| S5 | MKT13 / ELM161 | SAP Learning, S/4HANA ; cours évolutif, introduction SUP et core/prioritized protection |
| S6 | MKT13 / ELM162 | SAP Learning, S/4HANA ; cours évolutif mentionnant l’introduction en 2022, section SBC et intégration PP/DS |

Les pages Help Portal 2025 FPS01 repérées en recherche pour SBC/PAC n’ont pas fourni de corps lisible à l’ouverture ; les conclusions ci-dessus s’appuient sur les cours accessibles et ne prétendent pas vérifier toutes les éditions SAP. Les fonctions, restrictions et conditions commerciales ne sont pas présumées identiques entre éditions.

# D03 — décisions et vocabulaire

14 septembre 2026 — U147. Revue du backlog, sans publication. Les propositions structurées sont dans [d03-review.json](../modeles/backlog/d03-review.json), annexe d’instruction qui n’ajoute aucune capacité à la carte.

## Constats de marché

| Source et version | Passage consulté et constat | Adaptation locale et limites |
| --- | --- | --- |
| [Microsoft Dynamics 365 Supply Chain Management — Order promising](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations), documentation courante sans version produit figée | Sections Order promising / CTP calculations : ATP considère quantités disponibles et réceptions prévues ; CTP ajoute la prise en compte des capacités. Texte de page consulté le 14 septembre 2026. | Appui pour distinguer deux questions de faisabilité ; Microsoft décrit des méthodes de calcul, pas deux capacités de décision au rang natif attesté. |
| [Microsoft Business Central — Calculate order promising dates](https://learn.microsoft.com/en-us/dynamics365/business-central/sales-how-to-calculate-order-promising-dates), documentation courante | Sections About order promising / Capable to promise : scénario pour quantité absente du stock et des ordres planifiés, à produire, acheter ou transférer. Texte de page consulté le 14 septembre 2026. | CTP peut contribuer directement à la promesse ; ses réalisations et profondeurs diffèrent selon le produit. Ni simple disponibilité en stock ni analytics seule. |
| [SAP S/4HANA — Supply Creation-Based Confirmation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e296651f454c4284ade361292c633d69/40f313c8371047b1824c2565d63a8f79.html?version=2022.000), 2022 | Extrait indexé consulté le 14 septembre 2026 : création d’approvisionnement via PP/DS lorsque la quantité est insuffisante. Page ouverte sans texte exploitable. | Recouvrement partiel avec D03.h, pas avec le fractionnement des dates. Aucune équivalence universelle SBC/CTP ni capacité RBA établie. |
| [SAP S/4HANA aATP — Delivery Options](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/7ddf05566d667c65e10000000a44147b.html), 2025 FPS01 (février 2026) | Extrait indexé détaillé consulté le 14 septembre 2026 : réponse unique à date demandée, totalité à date ultérieure ou plusieurs livraisons partielles ; alternatives multi-sites également décrites. Page ouverte sans texte exploitable. | Appui pour une décision d’échéancement à éprouver. Ne prouve pas la nécessité de créer plusieurs commandes ni un domaine autonome. |

Ces descriptions produit n’attestent aucun déploiement dans le périmètre historique de Beaumanoir ou Boardriders. Aucun rang natif de Business Capability ni équivalence de niveau n’est déduit. La liste de décisions n’est pas déclarée exhaustive.

## Proposition de revue

- ATP Decision et CTP Decision : préciser les résultats de faisabilité avant de décider leur autonomie. Calculer les possibilités ne confirme pas encore une promesse. U147 rouvre le placement de CTP différé en U95.
- Supply Creation Decision concerne le recours à une ressource supplémentaire. Resource Provisioning Decision est un candidat local non adopté ; éviter de le doubler avec CTP si aucun résultat distinct ne justifie les deux.
- Delivery Schedule Decision est un candidat local pour le choix de quantités et dates fractionnées. Choisir plusieurs sources relève déjà de Fulfillment Source Decision ; fractionner la promesse n’implique pas plusieurs Orders.
- Allocation Decision simplifie le nom de D03.d, mais le sens large d’allocation fourni par Laurent recouvre aussi Supply Assignment : préserver la distinction entre quantité autorisée et ressource identifiée. Le nom reste proposé.
- Ressource est plus large que les biens qui circulent : une capacité de production est une ressource sans être un bien déplacé. Goods / marchandises ou Material Resource / ressource matérielle sont les candidats pour les biens présents ou futurs ; Item est leur référence. Supply décrit leur mise à disposition, pas le bien lui-même.
- Case désigne la demande processus, Order la commande Supply. Requirement peut expliciter un besoin quantifié et daté sans présumer un Case ou une commande déjà créée. Ne pas remplacer toutes les occurrences de demande par Order sans examiner les simulations et prévisions.
- Priorité entre commandes, choix du meilleur scénario et traitement du reliquat restent des contrôles de complétude proposés, sans création automatique de capacités.

## Application

Seul l’ordre des actions est modifié : Promise Proposal, Promise Confirmation, Promise Revision, Supply Assignment. Aucun ordre de workflow imposé. D03 et les noms contestés D03.d/D03.h sont en instruction ; les anciennes valeurs et leurs preuves de validation sont conservées. Les neuf capacités demeurent présentes, sans nouveaux libellés actifs. Release inchangée.


## U148 — faisabilité et adaptation

Laurent distingue la promesse à partir de l’existant/engagé et le plan de changements nécessaire pour honorer une commande. Cette distinction de résultats est retenue comme piste d’instruction. La restriction ATP aux achats fermes serait un périmètre local : la documentation Microsoft citée inclut des réceptions planifiées. Un calcul ATP n’engage pas nécessairement une ressource identifiée et ne confirme pas seul une promesse.

Vérification complémentaire du 14 septembre 2026 : [SAP aATP — Confirmation Strategies](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/1ba3a457ef816b10e10000000a441470.html), version non établie, extrait indexé consulté : le Backorder Processing peut avancer, retarder, réduire ou supprimer des confirmations selon les stratégies. [SAP aATP — Interactive Backorder Processing](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/dbe73c8f78cd440896553a571dae1983.html?locale=en-US&state=PRODUCTION&version=2023.latest), version 2023 Latest, extrait indexé consulté : modification et redistribution des confirmations. Limite : confirmations et commandes restent distinctes ; pas de preuve d’annulation automatique d’Orders. Comparaison produit, aucun classement natif de capacité ni déploiement local attesté.

Le CTP décrit par Microsoft prend en compte la possibilité de produire/obtenir les biens et les capacités ; aucune preuve examinée ne permet d’assimiler CTP à l’ensemble des changements de protections et engagements tiers imaginés ici. **Promise Feasibility Planning** est un nouveau candidat local pour le plan d’adaptation, non adopté, sans équivalent marché exact établi. CTP peut en être un moyen d’évaluation, avec le réexamen des confirmations et des protections.

La suppression envisagée de D03.d peut se justifier par intégration des contraintes dans ATP ; celle de D03.h par intégration du recours à de nouvelles ressources dans le plan. Elle ne découle pas de Supply Assignment, dont la définition actuelle affecte des ressources et n’en crée pas. Les hypothèses de retrait restent conditionnelles, sans modification de la liste active. Le besoin de Delivery Schedule Decision et l’ordre de présentation sont confirmés en U148. Avant ajout, expliciter sa différence avec l’échéancier produit par ATP : faisabilité des dates versus choix d’une solution parmi celles réalisables.


## U151 — alignement de la maille métier

Laurent retient ATP/CTP/PTP comme niveau d’aptitude à cartographier. La comparaison au marché éclaire cette construction locale, sans imposer les frontières produit. L’alternative `D03-ALIGNMENT-U151` dans le backlog JSON propose quatre actions conservées et quatre décisions : ATP, CTP, PTP, Delivery Schedule Decision. Les cinq décisions détaillées actuelles sont reprises comme choix/règles des capacités plus larges : droits/protections dans ATP ; ressource nouvelle dans le plan CTP ; source, acheminement et substitution dans la construction et la comparaison des scénarios.

Aucune équivalence exacte de cette décomposition avec un catalogue éditeur n’est établie. Les sources U147–U149 restent les appuis consultés ; aucune recherche nouvelle n’est revendiquée. Le CTP local suit le résultat souhaité U148 et reste plus large que le sens produit attesté. Son plan ne modifie pas automatiquement les Orders, leurs confirmations ou les protections. Supply Assignment applique les affectations mais ne réalise pas toutes les mesures du plan. Le choix d’échéancier reste proposé séparément car son besoin est confirmé en U148 ; sa frontière avec la proposition ATP/CTP demeure explicite. Le retrait de la liste active attend l’arbitrage de cette recomposition détaillée.


## Adoption U154

La recomposition U151 est validée et appliquée au backlog : huit capacités dont D03.i–l nouvelles décisions. Les anciens D03.d–h et l’alternative antérieure sont conservés dans `../modeles/backlog/history/pre-U154.json`. Les paragraphes indiquant une proposition non adoptée décrivent les étapes précédentes. Aucun changement des appuis marché ni prétention d’équivalence nouvelle. Exploration lexicale poursuivie séparément dans [Requisition/Order/Case](ecc-requisition-order-case.md).


## U251 — responsabilité de CTP précisée

Après l’audit U249 et le challenge U250, Laurent adopte CTP comme faisabilité après adaptation mobilisant les décisions spécialisées. Le nom et la maille ATP/CTP/PTP sont conservés. Chaque arbitrage de priorité, échéancier, économie, politique de stock ou service garde son responsable ; CTP ne devient pas leur autorité commune. Un apport pour honorer un Order conserve sa finalité distincte de l’optimisation du stock. Définition, exemple et portées : [frontières CTP](../connaissance/33-frontieres-ctp.md), CMP086. Six dépendances structurées proposées ; les étapes U148/U151/U154 ci-dessus restent historiques pour les formulations précisées. Release v007 inchangée.

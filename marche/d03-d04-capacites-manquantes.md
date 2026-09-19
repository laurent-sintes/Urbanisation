# D03/D04 — capacités manquantes à examiner

> **Évolution U214 — 15 septembre 2026 :** le backlog remplace les quatre capacités D04.e–h par cinq capacités par type d’ordre, Order Structuring et Order Lifecycle Management (D04.i–o). Les propositions de conserver quatre capacités sont historiques. Voir la [refonte et les descriptions concrètes](../connaissance/29-order-management-refonte.md) ; les publications restent inchangées.

14 septembre 2026 — U160. État de référence : huit capacités D03 et quatre D04 dans le backlog ; Simulation en instruction U159 et Backlog Management comme nom de domaine encore proposé. [Candidats structurés](../modeles/backlog/d03-d04-gap-review.json). Aucun ajout adopté.

## Appuis de marché

| Source | Contenu consulté et rapprochement |
| --- | --- |
| [Oracle 26B — Start Backlog Planning](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspc/start-backlog-planning.html) | Extrait indexé consulté le 14 septembre 2026 : priorisation du carnet selon une règle choisie. Appui pour Order Prioritization, pas preuve d’une capacité de rang natif. |
| [Oracle 26B — Item Availability and Constraint Analysis](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faubm/item-availability-and-constraint-analysis-of-configure-to-order-shipment-sets-and-arrival-sets.html) | Extrait indexé détaillé : analyse des contraintes de lignes et ensembles, retards et effet des composants bloquants. Appui partiel pour Backlog Assessment, dont le périmètre local proposé est plus large. |
| [SAP ERP 6.0 EHP7 SP28 — Incompletion Log](https://help.sap.com/docs/SAP_ERP_SPV/349992fb60854a62a264d716ad5c8f54/5deea852c8296028e10000000a441470.html?version=6.17.28) | Extrait indexé : documents enregistrables avec données manquantes de segmentation. Appui étroit au résultat de qualification distinct de l’enregistrement ; pas preuve de toutes conditions d’admissibilité d’une commande. |
| [Oracle 25C — Update and Split Order Lines](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/faiom/use-rest-api-to-update-and-split-fulfillment-lines.html) | Extrait indexé détaillé : séparation de lignes de réalisation, contraintes pour kits et ensembles. Appui à la structuration ; une ligne de réalisation Oracle n’est pas automatiquement un nouvel Order local. API et fonctions ne sont pas transformées en capacités. |
| [Oracle 25D — Holds](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/fauom/use-holds-to-temporarily-stop-processing.html) | Extrait indexé : suspension/reprise aux niveaux commande, ligne ou traitement. À expliciter dans Order Revision et à la frontière exécution ; pas trois capacités nouvelles déduites. |
| [SAP Learning — Supply Assignment](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4), version précise inconnue | Texte consulté U157 et extrait indexé revérifié : release check selon couverture et regroupements avant création de livraison. Question de frontière D03/D07/C-Log, pas extension de développement FLOW. |

## Résultats proposés

Deux lacunes de résultat ressortent nettement dans D03 : arbitrer les priorités (Order Prioritization) et diagnostiquer le carnet (Backlog Assessment). Les priorités sont déjà utilisées, leur établissement ne l’est pas ; les états/reliquats sont connus, leur diagnostic collectif n’est pas explicite. La simulation mesure les conséquences globales des scénarios selon U159 ; elle peut utiliser le diagnostic sans se confondre avec lui.

Dans D04, Order Qualification et Order Structuring sont à examiner avant de choisir entre nouvelles capacités et enrichissement de Registration/Revision. Ne pas transformer des contrôles de saisie ou opérations de split en capacités par simple traduction du produit. Autorités des références externes, Case et contenu applicable de l’Order restent distincts.

Fulfillment Release Decision est un candidat de frontière : une promesse ou une affectation n’autorise pas nécessairement le lancement. Mais D07 et la logistique en adhérence peuvent porter ce résultat. Ne pas l’ajouter d’office à D03.

Pas d’ajout automatique pour réaffectation/libération (Supply Assignment), ajustement de promesse (Promise Revision), suspension/reprise/annulation (Order Revision à préciser), ni duplication de Simulation déjà discutée. Les sources ventes ne démontrent pas couverture de toutes natures d’Orders. Aucun catalogue exhaustif, equivalence complète ni configuration locale attesté.


## Réexamen U161/U162 — aptitudes et activité

Cette section corrige les propositions précédentes. Laurent refuse de déduire la carte de capacités des opérations nécessaires aux processus. La présence d’une fonction chez un éditeur ne suffit pas à établir une aptitude autonome dans notre modèle.

Order Qualification est retirée : les contrôles évoqués constituent ici un principe général de fonctionnement. Order Structuring est rapprochée de Order Revision ; Codex recommande ce dernier libellé, plus large, sans nouvel arbitrage sur le nom ni ajout actif.

Order Prioritization reste en instruction. Codex propose de réserver ce terme à la priorité relative des commandes. Les dates dépendent aussi des contraintes et solutions de promesse ; confirmer un engagement est à rapprocher de Promise Confirmation. Modifier le contenu relève plutôt de Order Revision. Ces rapprochements sont explicatifs et ne prescrivent aucun processus.

Laurent précise explicitement que grooming désigne Backlog Refinement, une activité. Elle peut mobiliser plusieurs capacités sans devenir elle-même une capacité. Les candidats Backlog Assessment et Fulfillment Release Decision restent des propositions antérieures non arbitrées.


## Adoption U163 — Order Prioritization

Laurent valide Order Prioritization : « Établir et réviser les priorités relatives des commandes. » Capacité intégrée au backlog sous D03.m, avec relation explicite vers D03. La finalité et la codification de nature ajoutées à la fiche restent proposées par Codex. Cette adoption remplace l’état en instruction de ce seul candidat ; les autres arbitrages restent ouverts. Le rapprochement Oracle documenté plus haut reste un appui fonctionnel partiel, pas une équivalence de catalogue. Aucune release implicite.

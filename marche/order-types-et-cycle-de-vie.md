# Types d’Orders et pilotage opérationnel — U211

> **Évolution U214 — 15 septembre 2026 :** le backlog remplace les quatre capacités D04.e–h par cinq capacités par type d’ordre, Order Structuring et Order Lifecycle Management (D04.i–o). Les propositions de conserver quatre capacités sont historiques. Voir la [refonte et les descriptions concrètes](../connaissance/29-order-management-refonte.md) ; les publications restent inchangées.

15 septembre 2026. Analyse proposée en réponse à la clarification de Laurent. Complète [la comparaison U210](order-management-abstraction-comparaison.md). La liste des fonctionnalités de la famille Dynamics 365 était trop large pour répondre au besoin : préciser les Orders et les décisions qui font évoluer leur traitement.

## Base locale vérifiée

Lecture de `modeles/backlog/model.yaml` et `glossary.yaml` par `scripts/structured_io.py`. D04 cite achats, ventes, transferts et retours. Les quatre capacités Registration, Revision, Visibility et Reconciliation laissent les comportements de lancement, suspension, annulation et fractionnement largement à instruire. D03.m porte déjà Order Prioritization. D07.a exprime les prestations attendues sous forme de Service Orders.

U169 et TER065/TER066 distinguent les contextes : Supply Order porte la commande dont la Supply travaille couverture, priorités et promesse ; Service Order porte les prestations confiées à l’exécutant. Ne pas appliquer un cycle unique aux deux modèles. Les types ci-dessous ne créent aucun nœud, agrégat ou héritage dans le backlog.

## Familles à décrire

| Famille déjà citée dans D04 | Libellé de travail / variantes | Résultat à satisfaire |
| --- | --- | --- |
| Vente | Sales Order | Servir la commande d’un client. |
| Achat | Purchase Order | Obtenir des biens auprès d’un fournisseur. |
| Transfert | Transfer Order | Transférer des biens entre sites ou stocks, selon les responsabilités établies. |
| Retour | Customer Return Order ; Supplier Return Order | Organiser respectivement le retour depuis un client et le retour vers un fournisseur. Deux variantes explicatives, pas deux types nouveaux adoptés. |

Microsoft documente les ventes, achats et transferts dans ses paramètres d’ordres ; les retours clients sont des commandes de vente de type Returned order et les retours fournisseurs passent par des commandes d’achat de retour. [S1–S3] Ces représentations produit ne prescrivent pas notre schéma.

Réassort, eCommerce, B2B et intersociétés peuvent qualifier un scénario ou une relation entre commandes. Proposition : ne pas les empiler au même rang que les familles avant d’examiner ce qui change réellement dans le besoin, les parties et les règles. Un réassort peut se matérialiser par un achat, un transfert ou une vente selon la relation considérée ; cela reste une grille d’analyse des scénarios, pas un fait de déploiement.

Microsoft gère aussi des ordres de production et des documents d’exécution d’entrepôt. [S4, S9] Leur présence dans un produit nommé Supply Chain Management ne les ajoute pas automatiquement à D04. Un besoin de production, de transport ou de préparation doit être examiné en conservant la frontière des prestations U169. Les Shipment Orders Microsoft constituent un exemple concret de représentation propre au WMS, distincte des commandes amont ; leurs restrictions fonctionnelles empêchent une équivalence générale avec nos Service Orders.

## Catalogue de décisions et d’effets à cartographier

Noms de travail proposés, pas liste officielle de capacités Microsoft ni décision d’ajouter une capacité par ligne.

| Opération / responsabilité à instruire | Résultat métier recherché | Limite à préciser |
| --- | --- | --- |
| Create / Register | Reconnaître une commande et son contenu initial. | Origine, autorité, doublon ; D04.e existant. |
| Firm | Transformer une intention planifiée en commande ferme, si cette distinction existe. | Ne vaut pas démarrage physique. Microsoft transforme les ordres planifiés en achats, transferts ou productions effectifs. [S5] |
| Release | Autoriser le traitement ou libérer une portée vers l’exécution. | Définir le destinataire et le résultat ; frontière D04/D07/Services à instruire. |
| Hold | Bloquer une progression déterminée avec motif et portée. | Commande/ligne/quantité ; effets sur réservations et engagements ; ne pas présumer un arrêt physique immédiat. |
| Resume / Clear hold | Lever une restriction et rendre la progression de nouveau possible. | Plusieurs blocages peuvent nécessiter des levées distinctes ; ne vaut pas constat de redémarrage. |
| Advance / Postpone / Reschedule | Avancer ou reporter une échéance. | Distinguer date demandée, promesse et plan d’exécution. Une suggestion n’est pas une décision appliquée. |
| Amend | Intégrer un changement autorisé de contenu. | Quantité, destination, lignes ; D04.f existant et impacts vers les autres domaines. |
| Cancel | Retirer tout ou partie de la quantité encore à satisfaire, selon les autorisations. | Ne pas effacer des réalisations passées ni assimiler annulation à retour. |
| Close | Reconnaître une fin de traitement et expliciter le sort du restant. | Satisfait, annulé ou solde abandonné avec autorisation ; clôture financière et clôture opérationnelle peuvent différer. |

Le contrôle doit porter sur une portée explicite : commande, ligne, fraction de quantité ou échéancier. Les actions autorisées dépendent du type d’ordre et de son avancement. Cette matrice reste à construire ; aucune disponibilité universelle de toutes les actions n’est présumée.

## Les distinctions qui rendent le modèle concret

Microsoft distingue Released et Started pour la production ; la libération vers l’entrepôt concerne notamment ventes et transferts. [S4, S6] Il faut donc définir « lancement » par son effet, au lieu de confondre affermissement, autorisation et démarrage constaté.

La documentation des Holds décrit blocage, motifs, rôle autorisé à lever et effets configurables sur les réservations. [S7] Les messages Postpone/Advance sont des recommandations de planification, acceptées ou non par l’utilisateur. [S8] Un report de la date demandée relève d’une révision du besoin ; une révision de promesse concerne D03 ; un déplacement de la prestation nécessite la coordination avec D07 et l’exécutant. Une modification de priorité relève déjà de D03.m et ne constitue pas automatiquement un report.

Exemple fictif proposé : sur un transfert de 100 unités, 60 sont autorisées au traitement et 40 restent bloquées. Le report des 40 à lundi ne lève pas automatiquement leur blocage. Il faut identifier les conditions de reprise, les éventuelles promesses à réviser et les instructions déjà transmises. Cet exemple éprouve le besoin de portées partielles ; il ne valide aucune règle de gestion locale.

## Proposition de suite

Revoir explicitement le pilotage du cycle opérationnel au-delà de la tenue de la version applicable. Une capacité candidate **Order Lifecycle Management** pourrait regrouper la maîtrise des autorisations et restrictions de progression, avec Release, Hold, Resume, Cancel et Close comme fonctions à éprouver. Ce nom et ce regroupement ne sont pas adoptés. La définition doit la distinguer d’Order Revision et conserver les responsabilités réelles de l’exécutant. Le « lifecycle » de validation éditoriale du modèle est un autre sujet.

Pour la replanification, préciser d’abord quel engagement ou quelle date est modifié ; ne pas créer un Order Rescheduling générique absorbant D03 et Services. Préserver le retrait d’Order Qualification U161/U162. Le nombre final de capacités reste ouvert : Laurent a demandé d’explorer ces aptitudes concrètes, sans arbitrer leur granularité.

## Sources officielles

Consultées le 15 septembre 2026. Documentation produit Microsoft Dynamics 365 SCM ; aucune implémentation Beaumanoir ni équivalence de capacités déduite. Édition produit non figée lorsque l’URL ne la précise pas.

- **S1** — [Default order settings](https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/default-order-settings), extrait indexé détaillé : familles d’ordres et documents utilisant les paramètres.
- **S2** — [Sales returns](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns), extrait indexé détaillé : représentation des retours et remplacement.
- **S3** — [Create a purchase return order](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/create-purchase-return-order), extrait indexé : retour vers le fournisseur.
- **S4** — [Production process overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/production-process-overview), cycle produit, Released/Started et Ended ; vérifié par la recherche parallèle.
- **S5** — [Firm planned orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming), extrait indexé détaillé : transformation en ordres effectifs.
- **S6** — [Release to warehouse](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/release-to-warehouse-process), ventes et transferts ; extrait indexé et vérification parallèle.
- **S7** — [Manage order holds](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/tasks/manage-order-holds), texte vérifié dans U210 et recherche parallèle U211.
- **S8** — [Action messages](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages), texte consulté : suggestions Advance/Postpone/Increase/Decrease ; mise à jour affichée 26 mars 2026.
- **S9** — [Warehouse management only mode overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-overview), texte consulté : documents entrants/sortants propres au WMS et limites ; mise à jour affichée 20 novembre 2025.

Complément IBM Sterling vérifié par la recherche parallèle : [Order details tab](https://www.ibm.com/docs/en/order-management?topic=orders-order-details-tab) distingue notamment Schedule, Unschedule, Release, Cancel et Hold, soumis aux droits et règles de modification. Produit OMS, sans assimilation au modèle historique IBM CBM et sans nouvelle confirmation de l’hypothèse « ITM = IBM ».

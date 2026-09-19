# Refonte D04 — Order Management

15 septembre 2026 — U212–U215. Backlog uniquement ; publication v004 inchangée.

Autorité : [model.yaml](../modeles/backlog/model.yaml). Cette note restitue les champs générés depuis le backlog au moment de la refonte. Les noms et responsabilités courtes présentés sont adoptés ; les descriptions détaillées ci-dessous sont proposées selon U215.

## Remplacement et continuité des responsabilités

D04.e–h quittent la carte courante. L’enregistrement, la visibilité et le rapprochement sont intégrés aux cinq capacités par type. La révision se répartit entre contenu par type, structuration et cycle opérationnel. Aucun identifiant ni validation ancienne n’est transféré.

[Correspondances et portée](../modeles/backlog/d04-refactoring.yaml) ; [état antérieur intégral](../modeles/backlog/history/pre-U214.yaml). Les deux capacités transversales sont au même niveau que les cinq types ; aucun cycle uniforme ni hiérarchie logicielle n’est imposé.

## D04.i — Sales Order Management

Gérer les commandes clients à satisfaire : enregistrer ce qui est demandé, maintenir les quantités, destinations et échéances applicables, suivre les évolutions autorisées et déterminer ce qui reste à servir.

**Finalité** : Disposer d’une commande client exploitable et d’un reste à satisfaire explicable pendant son traitement.

**Concrètement**

Type de commande : [Sales Order](../modeles/backlog/glossary.yaml).

Enregistrer l’origine et le contenu applicable, intégrer les modifications autorisées avec leur historique, rendre la situation consultable et rapprocher les réalisations pour déterminer le reste à satisfaire. Les transformations de structure mobilisent [Order Structuring](../modeles/backlog/model.yaml) ; les autorisations et restrictions de progression mobilisent [Order Lifecycle Management](../modeles/backlog/model.yaml). Ces capacités transversales sont des responsabilités complémentaires, pas des sous-capacités répétées sous chaque type.

Une commande client peut comporter plusieurs lignes et échéances. Exemple fictif : sur 100 pièces commandées, 60 sont livrées et 40 restent à servir, avant prise en compte des annulations ou ajustements autorisés. Une demande de report des 40 pièces doit préciser la date demandée ; elle ne change pas automatiquement la promesse confirmée. Un retour ultérieur donne lieu à une commande de retour distincte, reliée à l’origine lorsque connue, et non à l’effacement de la livraison.

Les conditions contractuelles restent des références ; cette capacité ne confère pas l’autorité de négocier ou de modifier un Agreement. Priorités, couverture et promesses restent dans Order Promising ; prestations, engagements et faits d’exécution dans D07 et le contexte Services. Les règles d’imputation, tolérances, autorisations et effets sur les réservations sont à instruire. Les exemples sont fictifs et ne prouvent aucun déploiement.

## D04.j — Purchase Order Management

Gérer les commandes d’achat adressées aux fournisseurs : maintenir les biens, quantités, destinations et échéances attendus, intégrer les évolutions autorisées et rapprocher les réceptions pour connaître le reste à recevoir.

**Finalité** : Suivre ce qui est commandé au fournisseur, ce qui a évolué et ce qui reste attendu.

**Concrètement**

Type de commande : [Purchase Order](../modeles/backlog/glossary.yaml).

Enregistrer l’origine et le contenu applicable, intégrer les modifications autorisées avec leur historique, rendre la situation consultable et rapprocher les réalisations pour déterminer le reste à satisfaire. Les transformations de structure mobilisent [Order Structuring](../modeles/backlog/model.yaml) ; les autorisations et restrictions de progression mobilisent [Order Lifecycle Management](../modeles/backlog/model.yaml). Ces capacités transversales sont des responsabilités complémentaires, pas des sous-capacités répétées sous chaque type.

Lorsque le contexte distingue intention planifiée et commande ferme, l’affermissement engage le traitement de la commande selon les autorisations définies ; il ne prouve pas un démarrage de fabrication. Exemple fictif : une commande de 100 pièces comporte 60 pièces reçues et 40 restantes ; le fournisseur propose de décaler les 40. Conserver la proposition, la date retenue et leurs conséquences à examiner sur les demandes aval, sans confondre suggestion et décision acceptée. La négociation du contrat et l’exécution du fournisseur ne sont pas absorbées.

Les conditions contractuelles restent des références ; cette capacité ne confère pas l’autorité de négocier ou de modifier un Agreement. Priorités, couverture et promesses restent dans Order Promising ; prestations, engagements et faits d’exécution dans D07 et le contexte Services. Les règles d’imputation, tolérances, autorisations et effets sur les réservations sont à instruire. Les exemples sont fictifs et ne prouvent aucun déploiement.

## D04.k — Transfer Order Management

Gérer les ordres de déplacement de marchandises entre sites : maintenir origine, destination, quantités et échéances, suivre les modifications et rapprocher départs et arrivées pour connaître le transfert restant à satisfaire.

**Finalité** : Rendre explicite ce qui doit être transféré, vers quel site et ce qui reste à acheminer ou à recevoir.

**Concrètement**

Type de commande : [Transfer Order](../modeles/backlog/glossary.yaml).

Enregistrer l’origine et le contenu applicable, intégrer les modifications autorisées avec leur historique, rendre la situation consultable et rapprocher les réalisations pour déterminer le reste à satisfaire. Les transformations de structure mobilisent [Order Structuring](../modeles/backlog/model.yaml) ; les autorisations et restrictions de progression mobilisent [Order Lifecycle Management](../modeles/backlog/model.yaml). Ces capacités transversales sont des responsabilités complémentaires, pas des sous-capacités répétées sous chaque type.

Exemple discuté : sur un transfert de 100 pièces, 60 peuvent être autorisées pour traitement et 40 mises en attente. Reporter les 40 à lundi ne lève pas leur blocage. Les quantités autorisées, expédiées et reçues expriment des situations différentes ; une expédition ne prouve pas la réception. Scinder le transfert conserve les liens à la demande initiale et évite le double comptage. Préparer, transporter et réceptionner physiquement relèvent des exécutants.

Les conditions contractuelles restent des références ; cette capacité ne confère pas l’autorité de négocier ou de modifier un Agreement. Priorités, couverture et promesses restent dans Order Promising ; prestations, engagements et faits d’exécution dans D07 et le contexte Services. Les règles d’imputation, tolérances, autorisations et effets sur les réservations sont à instruire. Les exemples sont fictifs et ne prouvent aucun déploiement.

## D04.l — Customer Return Management

Gérer les commandes de retour provenant des clients : représenter les biens et quantités attendus en retour, leur origine et leur destination, intégrer les évolutions autorisées et rapprocher les réceptions effectives.

**Finalité** : Connaître le retour client attendu, son avancement et la part qui reste à traiter.

**Concrètement**

Type de commande : [Customer Return Order](../modeles/backlog/glossary.yaml).

Enregistrer l’origine et le contenu applicable, intégrer les modifications autorisées avec leur historique, rendre la situation consultable et rapprocher les réalisations pour déterminer le reste à satisfaire. Les transformations de structure mobilisent [Order Structuring](../modeles/backlog/model.yaml) ; les autorisations et restrictions de progression mobilisent [Order Lifecycle Management](../modeles/backlog/model.yaml). Ces capacités transversales sont des responsabilités complémentaires, pas des sous-capacités répétées sous chaque type.

Exemple fictif : un retour porte sur 10 pièces d’une vente antérieure ; 6 sont reçues et 4 restent attendues, sous réserve des règles de rapprochement. Le motif, le lien à la vente et les autorisations disponibles permettent d’expliquer le dossier. La commande de retour porte son propre traitement : elle n’annule pas rétroactivement la vente. Autorisation commerciale de reprise, remboursement, remplacement et décision sur le sort des biens restent à délimiter ; réception physique et contrôle par l’exécutant ne sont pas réalisés par cette capacité.

Les conditions contractuelles restent des références ; cette capacité ne confère pas l’autorité de négocier ou de modifier un Agreement. Priorités, couverture et promesses restent dans Order Promising ; prestations, engagements et faits d’exécution dans D07 et le contexte Services. Les règles d’imputation, tolérances, autorisations et effets sur les réservations sont à instruire. Les exemples sont fictifs et ne prouvent aucun déploiement.

## D04.m — Supplier Return Management

Gérer les commandes de renvoi de marchandises aux fournisseurs : maintenir les biens, quantités, destinataires et conditions de retour applicables, intégrer les évolutions et suivre le reste à retourner.

**Finalité** : Piloter un retour fournisseur explicite et traçable, distinct de la commande d’achat initiale.

**Concrètement**

Type de commande : [Supplier Return Order](../modeles/backlog/glossary.yaml).

Enregistrer l’origine et le contenu applicable, intégrer les modifications autorisées avec leur historique, rendre la situation consultable et rapprocher les réalisations pour déterminer le reste à satisfaire. Les transformations de structure mobilisent [Order Structuring](../modeles/backlog/model.yaml) ; les autorisations et restrictions de progression mobilisent [Order Lifecycle Management](../modeles/backlog/model.yaml). Ces capacités transversales sont des responsabilités complémentaires, pas des sous-capacités répétées sous chaque type.

Exemple fictif : 10 pièces doivent être retournées au fournisseur ; 6 sont expédiées et 4 restent à envoyer. L’expédition des 6 ne prouve ni leur réception par le fournisseur ni un avoir financier. Conserver les liens à l’achat ou à la réception d’origine lorsqu’ils sont connus. Mettre le reliquat en attente, en modifier l’échéance ou l’annuler nécessite d’en préciser la portée et l’autorisation. Le traitement physique et le règlement financier ne sont pas déduits du seul statut de l’ordre.

Les conditions contractuelles restent des références ; cette capacité ne confère pas l’autorité de négocier ou de modifier un Agreement. Priorités, couverture et promesses restent dans Order Promising ; prestations, engagements et faits d’exécution dans D07 et le contexte Services. Les règles d’imputation, tolérances, autorisations et effets sur les réservations sont à instruire. Les exemples sont fictifs et ne prouvent aucun déploiement.

## D04.n — Order Structuring

Organiser les Orders Supply et leurs éléments en scindant, regroupant ou répartissant des ordres, lignes et quantités entre échéances ou destinations, selon les décisions autorisées, tout en conservant leur origine et leurs liens.

**Finalité** : Obtenir une structure de commandes exploitable sans perdre la demande initiale, les quantités ni la traçabilité des transformations.

**Concrètement**

Split : scinder un ordre ou une ligne en plusieurs éléments. Merge / Consolidate : regrouper des demandes compatibles. Spread : répartir des quantités entre échéances, destinations ou ordres. Plusieurs échéances ne nécessitent pas toujours plusieurs Orders ; les niveaux de transformation admissibles restent à préciser.

Exemple fictif : répartir 100 pièces en 60 pour une première échéance et 40 pour une seconde. La transformation conserve les liens à l’origine et permet de retrouver la quantité initiale, sans compter à la fois le parent et ses résultats comme des demandes supplémentaires. Les règles de regroupement, d’identité et de réversibilité sont à instruire ; aucun regroupement entre types d’ordres n’est présumé.

Matérialiser une répartition décidée relève de cette capacité. Calculer la meilleure couverture ou choisir un échéancier mobilise Order Promising, notamment Delivery Schedule Decision ; affecter les ressources relève de Supply Assignment. Un regroupement physique de colis ou de transports relève de l’exécution. Structurer ne vaut ni affermir, ni autoriser le lancement, ni lever une attente.

## D04.o — Order Lifecycle Management

Gouverner la progression des Orders Supply : affermir, autoriser leur lancement, mettre en attente, reprendre, reporter ou avancer les échéances relevant de l’ordre, annuler et clôturer, avec la portée, les motifs et la trace des décisions.

**Finalité** : Savoir ce qui peut progresser, ce qui est bloqué et pourquoi, ainsi que les conditions de reprise ou de fin du traitement.

**Concrètement**

Affermir (Firm) transforme une intention planifiée en ordre ferme lorsque cette distinction existe. Libérer (Release) autorise sa prise en charge, pour tout ou partie de l’ordre. Démarrer (Start) doit distinguer l’autorisation de démarrage du constat d’un démarrage effectif ; ce dernier provient de l’exécution. Affermissement, libération et réalisation ne sont pas un même événement.

Mettre en attente (Hold) bloque une progression déterminée, avec motif et portée : ordre, ligne ou quantité selon les règles du type. Lever l’attente (Clear hold / Resume) retire le blocage concerné ; cela ne prouve ni la levée d’autres blocages ni la reprise physique. Les effets éventuels sur réservations et engagements doivent être explicites, pas automatiques par déduction.

Reporter / avancer (Postpone / Advance) change une échéance identifiée. Distinguer date demandée de l’ordre, date promise et plan de prestation : les deux dernières mobilisent leurs responsabilités de décision dans D03 et Services. Une proposition de report n’est pas une décision acceptée. Changer la priorité relative relève de [Order Prioritization](../modeles/backlog/model.yaml).

Annuler (Cancel) retire tout ou partie du reste à satisfaire selon l’autorisation applicable ; cela n’efface pas les réalisations passées et ne crée pas un retour. Clôturer (Close) constate la fin du traitement en expliquant le devenir du reliquat : satisfait, annulé ou écart autorisé à préciser. Une clôture opérationnelle ne prouve pas une clôture financière.

Exemple discuté : transfert de 100 pièces, 60 autorisées et 40 en attente. Reporter les 40 à lundi ne lève pas leur attente. Conserver qui a décidé, pourquoi, sur quelle quantité et avec quels effets attendus sur les promesses et prestations. Les transitions, autorités et règles détaillées restent à éprouver par type ; aucun cycle commun à tous les types ou aux Service Orders n’est imposé.

## Relations, marché et points ouverts

L’ancien lien D07.c → D04.h est archivé. Cinq contributions nouvelles D07.c → D04.i–m sont proposées pour conserver l’apport des faits d’exécution au rapprochement par type. Aucune validation automatique de leur grain ou de leur contrat.

Les appuis Microsoft/SAP/IBM de [U210](../marche/order-management-abstraction-comparaison.md) et [U211](../marche/order-types-et-cycle-de-vie.md) restent des comparaisons de travail. Chacune des sept nouvelles définitions est marquée non comparée individuellement ; aucune équivalence native ni couverture Beaumanoir/Boardriders/Sarenza déduite.

Q077 reste ouverte sur les transitions, autorités, effets croisés, imputations, cardinalités et volumétrie ; le choix du découpage et la place de Structuring/Lifecycle sont désormais tranchés. Q072 sur les engagements contractuels reste distincte.

# Les 41 capacités — avant/après

> Revue de référence U286–U289 avant migration. Le socle a été appliqué U290 ; les mentions de proposition ou de migration à venir ci-dessous décrivent cet état antérieur. Voir le [bilan courant](../2026-09-17-refonte-appliquee/rapport.md).

[Synthèse](rapport.md) · [Comportements](comportements.md) · [Dépendances](relations.md)

Toutes les nouvelles descriptions et illustrations restent proposées. Le maintien d’une valeur conserve son statut actuel. Les fonctions contenues dans les anciens scopes restent matière utile : aucune perte par retrait de la hiérarchie.

| ID | Capacité | Destination |
| --- | --- | --- |
| D01.f | Inventory Tracking | Conserver |
| D01.g | Record Inventory Movements | Conserver |
| D01.c | Inventory Visibility | Conserver |
| D01.d | Stocktaking | Décomposer sous condition |
| D02.b | Supply Protection | Refondre comportements |
| D02.c | Reservation | Frontière à arbitrer |
| D03.a | Promise Proposal | Regroupement et comportements adoptés U288 |
| D03.b | Promise Confirmation | Regroupement et comportements adoptés U288 |
| D03.c | Promise Revision | Regroupement et comportements adoptés U288 |
| D02.e | Supply Assignment | Frontière à arbitrer |
| D03.i | Available-to-Promise (ATP) | Conserver comportements |
| D03.j | Capable-to-Promise (CTP) | Conserver |
| D03.k | Profitable-to-Promise (PTP) | Conserver |
| D03.l | Delivery Schedule Decision | Conserver |
| D03.m | Order Prioritization | Conserver |
| D04.i | Sales Order Management | Conserver |
| D04.j | Purchase Order Management | Conserver |
| D04.k | Transfer Order Management | Conserver |
| D04.l | Customer Return Management | Conserver + manque à localiser |
| D04.m | Supplier Return Management | Conserver |
| D04.n | Order Structuring | Conserver |
| D04.o | Order Lifecycle Management | Nature à arbitrer |
| D05.a | Coverage Target Decision | Conserver |
| D05.d | Stock Allocation Decision | Conserver |
| D05.e | Replenishment Decision | Périmètre à étendre |
| D05.c | Stock Redistribution Decision | Conserver |
| D05.f | Inventory Planning | Refondre comportements |
| D06.b | Execution Capacity Visibility | Conserver |
| D07.a | Execution Requirements Decision | Conserver |
| D06.e | Execution Service Decision | Conserver proposition non adoptée |
| D06.f | Execution Adaptation Decision | Conserver |
| D06.d | Execution Orchestration | Décomposer sous condition |
| D07.b | Service Order Management | Conserver |
| D07.d | Execution Tracking | Conserver |
| D07.c | Execution Reconciliation | Conserver |
| D09.d | Party / Role Ingestion | Conserver |
| D11.a | Agreement Ingestion | Conserver |
| D08.d | Product Reference Ingestion | Conserver |
| D12.a | Catalog Ingestion | Conserver |
| D13.a | Fulfillment Network Ingestion | Conserver |
| D14.a | Execution Service Catalog Ingestion | Conserver |

## D01.f — Inventory Tracking

**Recommandation : Conserver** — État courant et attendu distinct des faits qui l’expliquent.

**Nom cible :** Inventory Tracking (nom courant : Inventory Tracking).

**Avant :** Établir et actualiser les quantités physiques et leurs états logiques à partir des faits de stock reconnus, par référence de produit, lieu, détenteur et propriétaire lorsque ces dimensions sont pertinentes ; suivre distinctement les ressources futures connues et leurs caractéristiques attendues.

**Cible proposée / valeur conservée :** Établir et actualiser les quantités physiques et leurs états logiques à partir des faits de stock reconnus, par référence de produit, lieu, détenteur et propriétaire lorsque ces dimensions sont pertinentes ; suivre distinctement les ressources futures connues et leurs caractéristiques attendues.

**Nature :** non établie — ne pas déduire automatiquement (unchanged_or_not_established).
**Frontière :** Corrections tardives et dimensions sont des règles, pas un comportement par événement.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** 100 présentes moins 30 sorties reconnues : 70 présentes ; 50 attendues restent futures.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D01.g Record Inventory Movements, D07.d Execution Tracking
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** Aucun champ adopté dans le lifecycle ; autres preuves historiques conservées dans le modèle.. Aucun accord étendu aux nouveaux textes.

## D01.g — Record Inventory Movements

**Recommandation : Conserver** — Responsabilité durable de preuve des mouvements malgré un nom formulé comme opération.

**Nom cible :** Record Inventory Movements (nom courant : Record Inventory Movements).

**Avant :** Enregistrer, qualifier et conserver les mouvements de stock et leurs justifications : réceptions, sorties, transferts, changements d’état ou de propriété et ajustements justifiés ; identifier les quantités concernées, les dates et les références explicatives, y compris sans déplacement physique.

**Cible proposée / valeur conservée :** Enregistrer, qualifier et conserver les mouvements de stock et leurs justifications : réceptions, sorties, transferts, changements d’état ou de propriété et ajustements justifiés ; identifier les quantités concernées, les dates et les références explicatives, y compris sans déplacement physique.

**Nature :** non établie — ne pas déduire automatiquement (unchanged_or_not_established).
**Frontière :** Enregistrer et corriger sont opérations du même résultat.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Tracer -5 justifié par comptage sans effacer le mouvement initial.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D01.d Stocktaking, D07.c Execution Reconciliation
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D01.c — Inventory Visibility

**Recommandation : Conserver** — Vue exploitable distincte de la tenue de l’état et du contrôle ATP.

**Nom cible :** Inventory Visibility (nom courant : Inventory Visibility).

**Avant :** Fournir une lecture cohérente des stocks physiques, de leurs états logiques et des ressources futures dans les différents lieux et périmètres, avec provenance et fraîcheur, sans double compte.

**Cible proposée / valeur conservée :** Fournir une lecture cohérente des stocks physiques, de leurs états logiques et des ressources futures dans les différents lieux et périmètres, avec provenance et fraîcheur, sans double compte.

**Nature :** non établie — ne pas déduire automatiquement (unchanged_or_not_established).
**Frontière :** Filtrer, consulter, agréger sont fonctions ; multi-site est un périmètre.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Afficher 70 présentes et 50 attendues à J+7 avec leur fraîcheur.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D01.f Inventory Tracking
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** Aucun champ adopté dans le lifecycle ; autres preuves historiques conservées dans le modèle.. Aucun accord étendu aux nouveaux textes.

## D01.d — Stocktaking

**Recommandation : Décomposer sous condition** — Contrôle récurrent et contrôle déclenché peuvent changer les pratiques de fiabilisation.

**Nom cible :** Stocktaking (nom courant : Stocktaking).

**Avant :** établir les quantités constatées par comptage, les confronter aux quantités enregistrées, qualifier les écarts et établir les corrections justifiées.

**Cible proposée / valeur conservée :** établir les quantités constatées par comptage, les confronter aux quantités enregistrées, qualifier les écarts et établir les corrections justifiées.

**Nature :** non établie — ne pas déduire automatiquement (unchanged_or_not_established).
**Frontière :** Les exécutants comptent ; mandat du déclenchement à arbitrer.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Comparer comptage régulier des articles sensibles et recomptage après écart de préparation.

**Comportements :** Recurring Stock Verification, Triggered Stock Verification
**Justification de décomposition :** Sous réserve du mandat, contrôle récurrent et contrôle déclenché organisent différemment la fiabilisation ; compter/comparer/corriger restent fonctions.

**A besoin de — proposition :** D01.c Inventory Visibility
**Marché / justification :** [S08 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting)

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** definition, finality, name. Aucun accord étendu aux nouveaux textes.

## D02.b — Supply Protection

**Recommandation : Refondre comportements** — Quatre mécanismes de configuration pour consommation et renouvellement.

**Nom cible :** Supply Protection (nom courant : Supply Protection).

**Avant :** Configurer et maintenir dans le temps les règles, seuils et quantités qui encadrent l’utilisation et le renouvellement des ressources, afin de maîtriser les risques de pénurie, de surstock et de déséquilibre.

**Cible proposée / valeur conservée :** Configurer et maintenir les politiques, règles et quantités qui encadrent l’usage et le renouvellement des ressources pour maîtriser pénurie, surstock et déséquilibre.

**Nature :** non établie — ne pas déduire automatiquement (unchanged_or_not_established).
**Frontière :** D05 décide les valeurs ; D02.b les applique transactionnellement ; les consommateurs les respectent.

**Fonctions conservées :** Attribuer et réallouer des enveloppes ; libérer l’inutilisé ; imputer ou corriger les consommations ; consulter les soldes. Maintenir seuils, validité, activation, dérogations et traçabilité. Les modalités unitaire/masse et écran/batch/flux/streaming ne créent pas de comportements.

**Exemple fictif :** Protéger 200 web, plafonner un groupe à 500, sécurité 40 et réassort sous 60 vers 100.

**Comportements :** Group Supply Protection, Consumption Capping, Safety Stock Policy, Replenishment Regulation
**Justification de décomposition :** Préserver un accès, limiter une consommation, absorber l’incertitude et réguler les apports répondent à des risques différents ; mécanismes combinables, pas étapes d’un cycle.

**A besoin de — proposition :** D05.a Coverage Target Decision, D05.d Stock Allocation Decision
**Marché / justification :** [S01 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), [S02 — SAP](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-), [S03 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification), [S04 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-replenishment), [S05 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/policy-assignment-sets.html), [S06 — RELEX](https://www.relexsolutions.com/solutions/automatic-replenishment-system/)

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D02.c — Reservation

**Recommandation : Frontière à arbitrer** — Conserver si engagement opposable distinct de l’affectation explicative.

**Nom cible :** Reservation (nom courant : Reservation).

**Avant :** établir un engagement de quantité pour un besoin identifié, dont les usages concurrents doivent tenir compte.

**Cible proposée / valeur conservée :** établir un engagement de quantité pour un besoin identifié, dont les usages concurrents doivent tenir compte.

**Nature :** non établie — ne pas déduire automatiquement (unchanged_or_not_established).
**Frontière :** Tester réservation sans affectation détaillée et affectation candidate sans réservation ; hypothèse à valider.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Un droit exclusif sur 40 peut précéder l’affectation du lot précis.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D01.c Inventory Visibility, D02.b Supply Protection
**Marché / justification :** [S12 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations)

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D03.a — Promise Proposal

**Recommandation : Regroupement et comportements adoptés U288** — U288 adopte Promise Management et requalifie cette responsabilité en comportement.

**Nom cible :** Promise Proposal (nom courant : Promise Proposal).

**Avant :** Construire une proposition de mise à disposition de ressources pour honorer une commande Supply, précisant quantités, dates, conditions et alternatives possibles, à partir des ressources et possibilités de réalisation.

**Cible proposée / valeur conservée :** Construire une proposition de mise à disposition de ressources pour honorer une commande Supply, précisant quantités, dates, conditions et alternatives possibles, à partir des ressources et possibilités de réalisation.

**Nature :** action (unchanged_or_not_established).
**Frontière :** Comportement de Promise Management selon U288. Les décisions de faisabilité, priorisation et échéancier restent distinctes ; confirmation ne prouve pas réservation, affectation ou prise en charge de service.

**Fonctions conservées :** Construire et présenter les propositions de promesse ; quantités, dates, conditions, alternatives.

**Exemple fictif :** Proposer 60 vendredi et 40 lundi sans les présenter comme confirmées.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D03.i Available-to-Promise (ATP), D03.j Capable-to-Promise (CTP), D03.k Profitable-to-Promise (PTP), D03.l Delivery Schedule Decision
**Marché / justification :** [S10 — SAP](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/73a1a457ef816b10e10000000a441470.html)

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** finality, name, nature. Aucun accord étendu aux nouveaux textes.

**Destination commune adoptée U288 : Promise Management ; définition détaillée proposée.** Gérer les propositions et engagements de promesse Supply, leurs confirmations et leurs révisions autorisées, avec quantités, dates, conditions et historique. Identifiant neuf si fusion retenue ; trois IDs retirés avec correspondance et redirection explicites. Aucun ancien accord transféré automatiquement.

## D03.b — Promise Confirmation

**Recommandation : Regroupement et comportements adoptés U288** — U288 adopte Promise Management et requalifie cette responsabilité en comportement.

**Nom cible :** Promise Confirmation (nom courant : Promise Confirmation).

**Avant :** établir les quantités et dates promises, en distinguant la part confirmée de celle qui ne l’est pas.

**Cible proposée / valeur conservée :** établir les quantités et dates promises, en distinguant la part confirmée de celle qui ne l’est pas.

**Nature :** action (unchanged_or_not_established).
**Frontière :** Comportement de Promise Management selon U288. Les décisions de faisabilité, priorisation et échéancier restent distinctes ; confirmation ne prouve pas réservation, affectation ou prise en charge de service.

**Fonctions conservées :** Enregistrer ce qui est confirmé et ce qui ne l’est pas, avec ses conditions et sa portée.

**Exemple fictif :** Confirmer 60 et laisser 40 non confirmées.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D03.a Promise Proposal, D02.c Reservation, D02.e Supply Assignment
**Marché / justification :** [S12 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations)

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** definition, finality, name, nature. Aucun accord étendu aux nouveaux textes.

**Destination commune adoptée U288 : Promise Management ; définition détaillée proposée.** Gérer les propositions et engagements de promesse Supply, leurs confirmations et leurs révisions autorisées, avec quantités, dates, conditions et historique. Identifiant neuf si fusion retenue ; trois IDs retirés avec correspondance et redirection explicites. Aucun ancien accord transféré automatiquement.

## D03.c — Promise Revision

**Recommandation : Regroupement et comportements adoptés U288** — U288 adopte Promise Management et requalifie cette responsabilité en comportement.

**Nom cible :** Promise Revision (nom courant : Promise Revision).

**Avant :** Réexaminer les promesses lorsque les ressources, commandes, dates ou priorités changent et établir les modifications autorisées.

**Cible proposée / valeur conservée :** Réexaminer les promesses lorsque les ressources, commandes, dates ou priorités changent et établir les modifications autorisées.

**Nature :** action (unchanged_or_not_established).
**Frontière :** Comportement de Promise Management selon U288. Les décisions de faisabilité, priorisation et échéancier restent distinctes ; confirmation ne prouve pas réservation, affectation ou prise en charge de service.

**Fonctions conservées :** Réexaminer les engagements affectés, enregistrer les révisions autorisées et conserver leur historique.

**Exemple fictif :** Retard de 2 jours : examiner une nouvelle promesse en conservant la précédente.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D03.i Available-to-Promise (ATP), D03.j Capable-to-Promise (CTP), D03.m Order Prioritization, D07.d Execution Tracking, D06.f Execution Adaptation Decision
**Marché / justification :** [S10 — SAP](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/73a1a457ef816b10e10000000a441470.html)

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** finality, name, nature. Aucun accord étendu aux nouveaux textes.

**Destination commune adoptée U288 : Promise Management ; définition détaillée proposée.** Gérer les propositions et engagements de promesse Supply, leurs confirmations et leurs révisions autorisées, avec quantités, dates, conditions et historique. Identifiant neuf si fusion retenue ; trois IDs retirés avec correspondance et redirection explicites. Aucun ancien accord transféré automatiquement.

## D02.e — Supply Assignment

**Recommandation : Frontière à arbitrer** — Terme Supply Assignment cohérent avec SAP ARun et déjà retenu U275 ; convention U289 écarte Allocation seul.

**Nom cible :** Supply Assignment (nom courant : Supply Assignment).

**Avant :** Affecter, réaffecter ou libérer des ressources admissibles présentes ou futures pour couvrir des commandes Supply, des engagements ou des besoins prévisionnels.

**Cible proposée / valeur conservée :** Affecter les ressources Supply présentes ou futures aux commandes identifiées, selon les priorités, les engagements et les contraintes applicables, afin d’en assurer la meilleure satisfaction possible. Le périmètre historique des autres besoins explicitement identifiés reste à qualifier, sans retrait implicite.

**Nature :** action (unchanged_or_not_established).
**Frontière :** Affectations aux commandes identifiées ; autres besoins historiques conservés à préciser. Décisions spécialisées, engagement de réservation, promesse et modification des Orders restent distincts.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Affecter 40 d’un arrivage à une commande puis changer leur provenance admissible.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D01.c Inventory Visibility, D02.b Supply Protection, D02.c Reservation, D03.m Order Prioritization
**Marché / justification :** [S01 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), [S12 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations)

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name, nature. Aucun accord étendu aux nouveaux textes.

## D03.i — Available-to-Promise (ATP)

**Recommandation : Conserver comportements** — Quatre comportements différencient admissibilité, réseau, mobilisation et projection.

**Nom cible :** Available-to-Promise (ATP) (nom courant : Available-to-Promise (ATP)).

**Avant :** Établir les quantités et dates auxquelles une demande ou un ensemble de demandes peut être satisfait par les ressources présentes ou futures admissibles dans la situation de référence, et expliciter la couverture qui rend ces engagements possibles.

**Cible proposée / valeur conservée :** Établir les quantités et dates auxquelles une demande ou un ensemble de demandes peut être satisfait par les ressources présentes ou futures admissibles dans la situation de référence, et expliciter la couverture qui rend ces engagements possibles.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Aucune politique modifiée ou réservation ; consommer les délais des exécutants.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Arrivage J+7 couvrant J+60 après engagements concurrents.

**Comportements :** Existing Commitment Consideration, Network Stock Availability, Operational Availability Timing, Future Supply Projection
**Justification de décomposition :** Quatre différences combinables modifient les possibilités : droits engagés, réseau, mobilisation et ressources futures ; aucun comportement par lieu ou technologie.

**A besoin de — proposition :** D01.c Inventory Visibility, D02.b Supply Protection, D02.c Reservation, D02.e Supply Assignment, D06.b Execution Capacity Visibility, D13.a Fulfillment Network Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** finality, name, nature. Aucun accord étendu aux nouveaux textes.

## D03.j — Capable-to-Promise (CTP)

**Recommandation : Conserver** — Faisabilité sous adaptation distincte des arbitrages mobilisés.

**Nom cible :** Capable-to-Promise (CTP) (nom courant : Capable-to-Promise (CTP)).

**Avant :** Déterminer les possibilités de satisfaction d’un Order nécessitant une adaptation des ressources ou des engagements, en mobilisant les décisions spécialisées et en explicitant les conditions de faisabilité et les impacts.

**Cible proposée / valeur conservée :** Déterminer les possibilités de satisfaction d’un Order nécessitant une adaptation des ressources ou des engagements, en mobilisant les décisions spécialisées et en explicitant les conditions de faisabilité et les impacts.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Aucun enfant par décision appelée ; apport pour Order ne dépend pas nécessairement de D05.e.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** 100 demandées, 60 admissibles : établir les conditions pour les 40 manquantes.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D03.i Available-to-Promise (ATP), D03.m Order Prioritization, D06.e Execution Service Decision, D05.a Coverage Target Decision, D05.d Stock Allocation Decision
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** definition, finality, name, nature. Aucun accord étendu aux nouveaux textes.

## D03.k — Profitable-to-Promise (PTP)

**Recommandation : Conserver** — Arbitrage économique autonome ; calcul du coût inclus.

**Nom cible :** Profitable-to-Promise (PTP) (nom courant : Profitable-to-Promise (PTP)).

**Avant :** Comparer et sélectionner les scénarios de promesse selon leurs coûts et conséquences économiques, dans les contraintes de service applicables.

**Cible proposée / valeur conservée :** Comparer et sélectionner les scénarios de promesse selon leurs coûts et conséquences économiques, dans les contraintes de service applicables.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Ne décide pas seul de faisabilité ou des conditions contractuelles.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Comparer transport accéléré et deux livraisons compatibles avec le service.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D03.i Available-to-Promise (ATP), D03.j Capable-to-Promise (CTP), D11.a Agreement Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Demande future, coûts, objectifs de service, risques, délais et règles selon le cas ; producteur et fraîcheur à qualifier, aucun référentiel maître inventé.

**Accords conservés :** definition, finality, name, nature. Aucun accord étendu aux nouveaux textes.

## D03.l — Delivery Schedule Decision

**Recommandation : Conserver** — Répartition temporelle distincte de la faisabilité et de sa matérialisation.

**Nom cible :** Delivery Schedule Decision (nom courant : Delivery Schedule Decision).

**Avant :** Choisir la répartition des quantités promises dans le temps, en une ou plusieurs échéances, parmi les possibilités réalisables et selon les conditions de la commande.

**Cible proposée / valeur conservée :** Choisir la répartition des quantités promises dans le temps, en une ou plusieurs échéances, parmi les possibilités réalisables et selon les conditions de la commande.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Une ou plusieurs échéances sont cas à décrire, pas deux comportements obligatoires.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Retenir 60 vendredi et 40 lundi parmi les options autorisées.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D03.i Available-to-Promise (ATP), D03.j Capable-to-Promise (CTP), D03.k Profitable-to-Promise (PTP), D11.a Agreement Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** definition, finality, name, nature. Aucun accord étendu aux nouveaux textes.

## D03.m — Order Prioritization

**Recommandation : Conserver** — Priorité des Orders différente des droits de groupes.

**Nom cible :** Order Prioritization (nom courant : Order Prioritization).

**Avant :** Établir et réviser les priorités relatives des commandes.

**Cible proposée / valeur conservée :** Établir et réviser les priorités relatives des commandes.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Pas un comportement par critère de classement ; ne modifie pas les quotas.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Arbitrer deux commandes concurrentes sur 80 pièces.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D11.a Agreement Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name, definition. Aucun accord étendu aux nouveaux textes.

## D04.i — Sales Order Management

**Recommandation : Conserver** — Un type d’Order par capacité reste cohérent avec l’accord.

**Nom cible :** Sales Order Management (nom courant : Sales Order Management).

**Avant :** Gérer les commandes clients à satisfaire : enregistrer ce qui est demandé, maintenir les quantités, destinations et échéances applicables, suivre les évolutions autorisées et déterminer ce qui reste à servir.

**Cible proposée / valeur conservée :** Gérer les commandes clients à satisfaire : enregistrer ce qui est demandé, maintenir les quantités, destinations et échéances applicables, suivre les évolutions autorisées et déterminer ce qui reste à servir.

**Nature :** action (unchanged_or_not_established).
**Frontière :** Pas de comportements CRUD ; promesse et progression gardent leurs responsables.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** 100 demandées, 60 livrées, 40 à servir ; retour distinct.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D04.n Order Structuring, D04.o Order Lifecycle Management, D07.c Execution Reconciliation, D03.b Promise Confirmation, D08.d Product Reference Ingestion, D09.d Party / Role Ingestion, D11.a Agreement Ingestion, D12.a Catalog Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D04.j — Purchase Order Management

**Recommandation : Conserver** — Engagement fournisseur avec dates et reliquat propres.

**Nom cible :** Purchase Order Management (nom courant : Purchase Order Management).

**Avant :** Gérer les commandes d’achat adressées aux fournisseurs : maintenir les biens, quantités, destinations et échéances attendus, intégrer les évolutions autorisées et rapprocher les réceptions pour connaître le reste à recevoir.

**Cible proposée / valeur conservée :** Gérer les commandes d’achat adressées aux fournisseurs : maintenir les biens, quantités, destinations et échéances attendus, intégrer les évolutions autorisées et rapprocher les réceptions pour connaître le reste à recevoir.

**Nature :** action (unchanged_or_not_established).
**Frontière :** Aucune négociation de contrat ou exécution fournisseur absorbée.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** 60 reçues sur 100 ; report proposé des 40 à instruire.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D04.n Order Structuring, D04.o Order Lifecycle Management, D07.c Execution Reconciliation, D08.d Product Reference Ingestion, D09.d Party / Role Ingestion, D11.a Agreement Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D04.k — Transfer Order Management

**Recommandation : Conserver** — Origine/destination et départ/arrivée distincts.

**Nom cible :** Transfer Order Management (nom courant : Transfer Order Management).

**Avant :** Gérer les ordres de déplacement de marchandises entre sites : maintenir origine, destination, quantités et échéances, suivre les modifications et rapprocher départs et arrivées pour connaître le transfert restant à satisfaire.

**Cible proposée / valeur conservée :** Gérer les ordres de déplacement de marchandises entre sites : maintenir origine, destination, quantités et échéances, suivre les modifications et rapprocher départs et arrivées pour connaître le transfert restant à satisfaire.

**Nature :** action (unchanged_or_not_established).
**Frontière :** Même type pour réassort ou redistribution ; finalités de décision distinctes.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** 60 expédiées sur 100 ne signifient pas 60 reçues.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D04.n Order Structuring, D04.o Order Lifecycle Management, D07.c Execution Reconciliation, D13.a Fulfillment Network Ingestion, D08.d Product Reference Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D04.l — Customer Return Management

**Recommandation : Conserver + manque à localiser** — Gestion du retour conservée ; choix du sort du bien non démontré couvert.

**Nom cible :** Customer Return Management (nom courant : Customer Return Management).

**Avant :** Gérer les commandes de retour provenant des clients : représenter les biens et quantités attendus en retour, leur origine et leur destination, intégrer les évolutions autorisées et rapprocher les réceptions effectives.

**Cible proposée / valeur conservée :** Gérer les commandes de retour provenant des clients : représenter les biens et quantités attendus en retour, leur origine et leur destination, intégrer les évolutions autorisées et rapprocher les réceptions effectives.

**Nature :** action (unchanged_or_not_established).
**Frontière :** Autorisation commerciale, remboursement et disposition ne sont pas implicitement absorbés.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** 6 reçues sur 10 ; identifier séparément qui décide réintégration ou rebut.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D04.n Order Structuring, D04.o Order Lifecycle Management, D07.c Execution Reconciliation, D04.i Sales Order Management, D08.d Product Reference Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D04.m — Supplier Return Management

**Recommandation : Conserver** — Renvoi fournisseur distinct de l’achat et du transport.

**Nom cible :** Supplier Return Management (nom courant : Supplier Return Management).

**Avant :** Gérer les commandes de renvoi de marchandises aux fournisseurs : maintenir les biens, quantités, destinataires et conditions de retour applicables, intégrer les évolutions et suivre le reste à retourner.

**Cible proposée / valeur conservée :** Gérer les commandes de renvoi de marchandises aux fournisseurs : maintenir les biens, quantités, destinataires et conditions de retour applicables, intégrer les évolutions et suivre le reste à retourner.

**Nature :** action (unchanged_or_not_established).
**Frontière :** Avoir financier et accord commercial hors de cette responsabilité.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Sur 10 à retourner, suivre les 4 encore à expédier.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D04.n Order Structuring, D04.o Order Lifecycle Management, D07.c Execution Reconciliation, D04.j Purchase Order Management, D09.d Party / Role Ingestion, D11.a Agreement Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D04.n — Order Structuring

**Recommandation : Conserver** — Transformation transverse avec conservation des quantités et liens.

**Nom cible :** Order Structuring (nom courant : Order Structuring).

**Avant :** Organiser les Orders Supply et leurs éléments en scindant, regroupant ou répartissant des ordres, lignes et quantités entre échéances ou destinations, selon les décisions autorisées, tout en conservant leur origine et leurs liens.

**Cible proposée / valeur conservée :** Organiser les Orders Supply et leurs éléments en scindant, regroupant ou répartissant des ordres, lignes et quantités entre échéances ou destinations, selon les décisions autorisées, tout en conservant leur origine et leurs liens.

**Nature :** action (unchanged_or_not_established).
**Frontière :** Split/merge/spread restent opérations ; choix de l’échéancier D03.l.

**Fonctions conservées :** Scinder, regrouper et répartir (split, merge, spread) avec liens à l’origine et conservation des quantités ; matérialiser les décisions autorisées.

**Exemple fictif :** Scinder 100 en 60 et 40 sans doubler la demande.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D03.l Delivery Schedule Decision
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D04.o — Order Lifecycle Management

**Recommandation : Nature à arbitrer** — Contenu mêlant gouvernance/application, nature courante decision à revoir.

**Nom cible :** Order Lifecycle Management (nom courant : Order Lifecycle Management).

**Avant :** Gouverner la progression des Orders Supply : affermir, autoriser leur lancement, mettre en attente, reprendre, reporter ou avancer les échéances relevant de l’ordre, annuler et clôturer, avec la portée, les motifs et la trace des décisions.

**Cible proposée / valeur conservée :** Gouverner et appliquer les évolutions autorisées du cycle de vie des Orders Supply, avec leur portée, leurs conditions et leurs effets sur le reste à satisfaire.

**Nature :** management (proposed_change).
**Frontière :** Recommander management ; autorisations incluses, décisions spécialisées distinctes.

**Fonctions conservées :** Affermir, libérer, autoriser le démarrage, mettre en attente, reprendre, reporter, avancer, annuler et clôturer avec portée et motifs. Distinguer autorisation et réalisation ; aucun cycle universel imposé.

**Exemple fictif :** Reporter 40 bloquées à lundi ne lève pas leur attente.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D03.b Promise Confirmation, D07.d Execution Tracking
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D05.a — Coverage Target Decision

**Recommandation : Conserver** — Décision des niveaux/seuils ; aucun enfant par paramètre.

**Nom cible :** Coverage Target Decision (nom courant : Coverage Target Decision).

**Avant :** Déterminer les niveaux de stock souhaitables et les seuils à retenir : couverture, sécurité, déclenchement du réassort, par produit, lieu et horizon.

**Cible proposée / valeur conservée :** Déterminer les niveaux de stock souhaitables et les seuils à retenir : couverture, sécurité, déclenchement du réassort, par produit, lieu et horizon.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Cible haute différente d’un plafond de groupe ou d’une capacité physique.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Sécurité 40, déclenchement 60, cible 100 : trois effets différents.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D01.c Inventory Visibility, D13.a Fulfillment Network Ingestion, D08.d Product Reference Ingestion
**Marché / justification :** [S03 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification), [S04 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-replenishment), [S05 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/policy-assignment-sets.html)

**Entrées externes :** Demande future, coûts, objectifs de service, risques, délais et règles selon le cas ; producteur et fraîcheur à qualifier, aucun référentiel maître inventé.

**Accords conservés :** name, definition. Aucun accord étendu aux nouveaux textes.

## D05.d — Stock Allocation Decision

**Recommandation : Conserver** — Déterminer quantités protégées et plafonds par groupe ; nom proposé pour éviter de confondre avec Supply Assignment. Portée métier conservée.

**Nom cible :** Group Protection Decision (nom courant : Stock Allocation Decision).

**Avant :** Déterminer les quantités à protéger ou les limites d’usage par canal ou groupe de bénéficiaires.

**Cible proposée / valeur conservée :** Déterminer les quantités à protéger ou les limites d’usage par canal ou groupe de bénéficiaires.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Ne pas renommer car allocation a un autre sens chez un éditeur.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Proposer 200 web et plafond 500 wholesale pour une période.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D01.c Inventory Visibility, D02.b Supply Protection, D05.a Coverage Target Decision
**Marché / justification :** [S01 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), [S02 — SAP](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-)

**Entrées externes :** Demande future, coûts, objectifs de service, risques, délais et règles selon le cas ; producteur et fraîcheur à qualifier, aucun référentiel maître inventé.

**Accords conservés :** name, definition. Aucun accord étendu aux nouveaux textes.

## D05.e — Replenishment Decision

**Recommandation : Périmètre à étendre** — Apports positifs seuls insuffisants pour maîtriser un excès futur.

**Nom cible :** Replenishment Decision (nom courant : Replenishment Decision).

**Avant :** Déterminer les apports nécessaires pour remplir le stock : quantités et dates, en tenant compte du stock disponible et des apports déjà engagés.

**Cible proposée / valeur conservée :** Déterminer les apports futurs et leurs ajustements en quantité et en date pour atteindre le stock souhaitable, en tenant compte du disponible, des besoins, des apports engagés et des contraintes de modification.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Extension aux apports futurs ; D04 autorise/applique les changements de commandes.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** 30 présentes et 80 attendues pour cible 100 : examiner réduction/report de 10.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D01.c Inventory Visibility, D02.b Supply Protection, D05.a Coverage Target Decision, D07.d Execution Tracking, D04.j Purchase Order Management, D04.k Transfer Order Management
**Marché / justification :** [S09 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages)

**Entrées externes :** Demande future, coûts, objectifs de service, risques, délais et règles selon le cas ; producteur et fraîcheur à qualifier, aucun référentiel maître inventé.

**Accords conservés :** name, definition. Aucun accord étendu aux nouveaux textes.

## D05.c — Stock Redistribution Decision

**Recommandation : Conserver** — Rééquilibrage existant distinct de l’ajustement des apports.

**Nom cible :** Stock Redistribution Decision (nom courant : Stock Redistribution Decision).

**Avant :** Déterminer les transferts de stock existant pour corriger les excédents et insuffisances entre sites.

**Cible proposée / valeur conservée :** Déterminer les transferts de stock existant pour corriger les excédents et insuffisances entre sites.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Coordonner Replenishment sans corriger deux fois le manque ; aucun transport réalisé ici.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Transférer 50 d’un site excédentaire en préservant ses engagements.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D01.c Inventory Visibility, D02.b Supply Protection, D13.a Fulfillment Network Ingestion, D05.e Replenishment Decision
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Demande future, coûts, objectifs de service, risques, délais et règles selon le cas ; producteur et fraîcheur à qualifier, aucun référentiel maître inventé.

**Accords conservés :** name, definition. Aucun accord étendu aux nouveaux textes.

## D05.f — Inventory Planning

**Recommandation : Refondre comportements** — Trois comportements retenus ; fonctions d’autorisation et application préservées.

**Nom cible :** Inventory Planning (nom courant : Inventory Planning).

**Avant :** Construire, simuler, analyser les impacts, évaluer et valider des scénarios de stock en mobilisant les décisions spécialisées, puis déclencher les actions retenues et connaître leur prise en compte via les capacités opérationnelles responsables.

**Cible proposée / valeur conservée :** Construire des scénarios alternatifs de stock, simuler et analyser leurs conséquences, puis adapter le scénario en cours à partir des faits, en mobilisant les décisions spécialisées et les capacités responsables de sa mise en action.

**Nature :** planning (unchanged_or_not_established).
**Frontière :** D05 mobilise ses décisions ; D04/D02.b appliquent et D06 garde son adaptation opérationnelle.

**Fonctions conservées :** Comparer et apprécier les options ; autoriser le scénario avec conditions ; déclencher les actions retenues via les capacités responsables et suivre leur prise en compte, y compris refus ou application partielle. L’analyse des impacts est dans Simulation & Analysis.

**Exemple fictif :** Explorer deux couvertures, analyser, puis adapter après retard d’arrivage.

**Comportements :** Scenario Construction, Simulation & Analysis, Scenario Execution Adaptation
**Justification de décomposition :** Explorer des alternatives, comprendre leurs conséquences et adapter un scénario engagé changent les pratiques de planification et leur articulation avec l’exécution.

**A besoin de — proposition :** D05.a Coverage Target Decision, D05.d Stock Allocation Decision, D05.e Replenishment Decision, D05.c Stock Redistribution Decision, D01.c Inventory Visibility, D07.d Execution Tracking, D02.b Supply Protection, D04.j Purchase Order Management, D04.k Transfer Order Management, D06.d Execution Orchestration
**Marché / justification :** [S07 — Kinaxis](https://www.kinaxis.com/en/solutions/sales-and-operations-planning)

**Entrées externes :** Demande future, coûts, objectifs de service, risques, délais et règles selon le cas ; producteur et fraîcheur à qualifier, aucun référentiel maître inventé.

**Accords conservés :** name, decomposition_rationale. Aucun accord étendu aux nouveaux textes.

## D06.b — Execution Capacity Visibility

**Recommandation : Conserver** — Capacité contextuelle communiquée, différente du SLA configuré.

**Nom cible :** Execution Capacity Visibility (nom courant : Execution Capacity Visibility).

**Avant :** Rendre visible la capacité opérationnelle communiquée par les exécutants, avec son contexte, sa période et sa fraîcheur, pour alimenter les décisions Supply.

**Cible proposée / valeur conservée :** Rendre visible la capacité opérationnelle communiquée par les exécutants, avec son contexte, sa période et sa fraîcheur, pour alimenter les décisions Supply.

**Nature :** knowledge (unchanged_or_not_established).
**Frontière :** Aucun comportement par canal de feedback ; contrat de disponible à préciser.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** 1 000 préparations annoncées ne signifient pas 1 000 encore disponibles.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D14.a Execution Service Catalog Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Informations communiquées par les exécutants ; unités, période, provenance, fraîcheur et distinction estimation/engagement/réalisé.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D07.a — Execution Requirements Decision

**Recommandation : Conserver** — Résultat de décision spécifique : prestations nécessaires.

**Nom cible :** Execution Requirements Decision (nom courant : Execution Requirements Decision).

**Avant :** Déterminer les prestations nécessaires.

**Cible proposée / valeur conservée :** Déterminer les prestations nécessaires.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Ne choisit pas encore l’exécutant et ne pilote pas ses opérations internes.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Livrer requiert préparation, document et transport.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D14.a Execution Service Catalog Ingestion, D13.a Fulfillment Network Ingestion, D04.i Sales Order Management
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name, definition. Aucun accord étendu aux nouveaux textes.

## D06.e — Execution Service Decision

**Recommandation : Conserver proposition non adoptée** — Conserver la proposition de choix des services ; fusion historique non validée par ce refacto.

**Nom cible :** Execution Service Decision (nom courant : Execution Service Decision).

**Avant :** Déterminer les services et exécutants à mobiliser pour les prestations nécessaires, en tenant compte de leur admissibilité et des contraintes.

**Cible proposée / valeur conservée :** Déterminer les services et exécutants à mobiliser pour les prestations nécessaires, en tenant compte de leur admissibilité et des contraintes.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Admissibilité/comparaison sont opérations de décision, pas comportements par filtre.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Choisir un service compatible destination, marchandises et créneau.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D07.a Execution Requirements Decision, D14.a Execution Service Catalog Ingestion, D13.a Fulfillment Network Ingestion, D06.b Execution Capacity Visibility
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** Aucun champ adopté dans le lifecycle ; autres preuves historiques conservées dans le modèle.. Aucun accord étendu aux nouveaux textes.

## D06.f — Execution Adaptation Decision

**Recommandation : Conserver** — Décide la variation opérationnelle, distincte de sa coordination.

**Nom cible :** Execution Adaptation Decision (nom courant : Execution Adaptation Decision).

**Avant :** Déterminer les variations du plan.

**Cible proposée / valeur conservée :** Déterminer les variations du plan.

**Nature :** decision (unchanged_or_not_established).
**Frontière :** Remonter effet promesse à D03 ; D05 peut revoir son scénario sans décider le transporteur.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Panne de préparation : retenir autre créneau ou réalisation partielle.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D07.d Execution Tracking, D07.b Service Order Management, D06.e Execution Service Decision, D06.b Execution Capacity Visibility
**Marché / justification :** [S11 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/faiom/overview-of-managing-change-that-occurs-during-order-fulfillment.html)

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name, definition. Aucun accord étendu aux nouveaux textes.

## D06.d — Execution Orchestration

**Recommandation : Décomposer sous condition** — Prérequis du plan et compensation d’un plan engagé : deux mécanismes candidats.

**Nom cible :** Execution Orchestration (nom courant : Execution Orchestration).

**Avant :** Coordonner les prestations et leurs dépendances.

**Cible proposée / valeur conservée :** Coordonner les prestations et leurs dépendances.

**Nature :** orchestration (unchanged_or_not_established).
**Frontière :** Décision D06.f séparée ; pas de rollback physique ni seconde promesse.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Changer de transporteur décidé : révoquer ce qui reste annulable et coordonner la nouvelle collecte.

**Comportements :** Dependency-driven Execution, Execution Compensation
**Justification de décomposition :** Faire progresser un plan et transformer un plan engagé posent des contraintes de coordination différentes, notamment les effets irréversibles.

**A besoin de — proposition :** D07.a Execution Requirements Decision, D06.e Execution Service Decision, D06.f Execution Adaptation Decision, D07.b Service Order Management, D07.d Execution Tracking
**Marché / justification :** [S11 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/faiom/overview-of-managing-change-that-occurs-during-order-fulfillment.html)

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name, definition. Aucun accord étendu aux nouveaux textes.

## D07.b — Service Order Management

**Recommandation : Conserver** — Demande, acceptation et réalisation distinctes ; gestion large.

**Nom cible :** Service Order Management (nom courant : Service Order Management).

**Avant :** Gérer les demandes de prestation adressées aux exécutants et leur cycle de vie : émission, acceptation ou refus, modification, annulation et clôture, selon le service.

**Cible proposée / valeur conservée :** Gérer les demandes de prestation adressées aux exécutants et leur cycle de vie : émission, acceptation ou refus, modification, annulation et clôture, selon le service.

**Nature :** management (unchanged_or_not_established).
**Frontière :** Émettre/accepter/modifier/clôturer sont fonctions, pas comportements par statut.

**Fonctions conservées :** Émettre, enregistrer acceptation/refus, modifier, annuler et clôturer selon le service ; distinguer SLA, engagement individuel et réalisation.

**Exemple fictif :** 100 demandées avant 16 h, 80 acceptées pour 17 h.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D07.a Execution Requirements Decision, D06.e Execution Service Decision, D14.a Execution Service Catalog Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** name, definition. Aucun accord étendu aux nouveaux textes.

## D07.d — Execution Tracking

**Recommandation : Conserver** — Connaissance des faits et estimations, sans décider ou tenir le stock.

**Nom cible :** Execution Tracking (nom courant : Execution Tracking).

**Avant :** Suivre les faits, jalons, estimations et résultats encore attendus des prestations pendant leur réalisation.

**Cible proposée / valeur conservée :** Suivre les faits, jalons, estimations et résultats encore attendus des prestations pendant leur réalisation.

**Nature :** knowledge (unchanged_or_not_established).
**Frontière :** Batch/streaming sont modalités ; distinguer faits et estimations.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** 60 préparées, 40 retardées, estimation de collecte révisée.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D07.b Service Order Management
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Informations communiquées par les exécutants ; unités, période, provenance, fraîcheur et distinction estimation/engagement/réalisé.

**Accords conservés :** name. Aucun accord étendu aux nouveaux textes.

## D07.c — Execution Reconciliation

**Recommandation : Conserver** — Résultat rapproché de l’attendu, autonome par rapport à l’avancement.

**Nom cible :** Execution Reconciliation (nom courant : Execution Reconciliation).

**Avant :** Rapprocher les résultats constatés des prestations attendues, qualifier les écarts et fournir les faits utiles aux domaines consommateurs.

**Cible proposée / valeur conservée :** Rapprocher les résultats constatés des prestations attendues, qualifier les écarts et fournir les faits utiles aux domaines consommateurs.

**Nature :** action (unchanged_or_not_established).
**Frontière :** Reliquat prestation différent du reliquat Order ; aucun rapprochement financier.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** 80 reçues sur 100 : qualifier l’écart et informer l’Order.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D07.b Service Order Management, D07.d Execution Tracking
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Conditions et événements externes pertinents selon le cas ; pas d’exhaustivité des contrats revendiquée.

**Accords conservés :** Aucun champ adopté dans le lifecycle ; autres preuves historiques conservées dans le modèle.. Aucun accord étendu aux nouveaux textes.

## D09.d — Party / Role Ingestion

**Recommandation : Conserver** — Projection externe des parties/rôles.

**Nom cible :** Party / Role Ingestion (nom courant : Party / Role Ingestion).

**Avant :** recevoir les parties, leurs identifiants, rôles et relations de référence ainsi que leurs évolutions, en conservant les références du maître externe.

**Cible proposée / valeur conservée :** recevoir les parties, leurs identifiants, rôles et relations de référence ainsi que leurs évolutions, en conservant les références du maître externe.

**Nature :** non établie — ne pas déduire automatiquement (unchanged_or_not_established).
**Frontière :** Lecture/recherche incluse ; ni maître local ni comportement par interface.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Recevoir un rôle destinataire avec identifiant et provenance du partenaire.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** Source maîtresse externe ; pas de fournisseur interne imposé.
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Maître externe à identifier selon le contexte ; projection en lecture/recherche, sans administration locale implicite.

**Accords conservés :** scope. Aucun accord étendu aux nouveaux textes.

## D11.a — Agreement Ingestion

**Recommandation : Conserver** — Projection des conditions utiles, contiguë à Party/Catalog.

**Nom cible :** Agreement Ingestion (nom courant : Agreement Ingestion).

**Avant :** Recevoir les contrats clients ou fournisseurs et leurs évolutions, y compris cadre, conditions particulières, périodes et engagements en quantité ou valeur, avec références Party et Catalog et provenance du maître externe.

**Cible proposée / valeur conservée :** Recevoir les contrats clients ou fournisseurs et leurs évolutions, y compris cadre, conditions particulières, périodes et engagements en quantité ou valeur, avec références Party et Catalog et provenance du maître externe.

**Nature :** non établie — ne pas déduire automatiquement (unchanged_or_not_established).
**Frontière :** Aucune négociation locale de l’Agreement.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Recevoir validité et conditions de livraison applicables.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D09.d Party / Role Ingestion, D12.a Catalog Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Maître externe à identifier selon le contexte ; projection en lecture/recherche, sans administration locale implicite.

**Accords conservés :** scope. Aucun accord étendu aux nouveaux textes.

## D08.d — Product Reference Ingestion

**Recommandation : Conserver** — Produit indépendant des catalogues ; rôles et variantes distincts.

**Nom cible :** Product Reference Ingestion (nom courant : Product Reference Ingestion).

**Avant :** Recevoir les références Product, leurs variantes, rôles, identifiants et caractéristiques utiles ainsi que leurs évolutions depuis les maîtres externes, indépendamment de leur présence dans les catalogues.

**Cible proposée / valeur conservée :** Recevoir les références Product, leurs variantes, rôles, identifiants et caractéristiques utiles ainsi que leurs évolutions depuis les maîtres externes, indépendamment de leur présence dans les catalogues.

**Nature :** non établie — ne pas déduire automatiquement (unchanged_or_not_established).
**Frontière :** Product/Container sont objets et rôles, pas comportements d’ingestion.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Recevoir taille/couleur avant intégration dans une offre.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** Source maîtresse externe ; pas de fournisseur interne imposé.
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Maître externe à identifier selon le contexte ; projection en lecture/recherche, sans administration locale implicite.

**Accords conservés :** scope. Aucun accord étendu aux nouveaux textes.

## D12.a — Catalog Ingestion

**Recommandation : Conserver** — Projection d’offre externe, différente du maître produit.

**Nom cible :** Catalog Ingestion (nom courant : Catalog Ingestion).

**Avant :** recevoir les catalogues construits à l’extérieur, leurs références de produits, prix, zones géographiques d’application et évolutions.

**Cible proposée / valeur conservée :** recevoir les catalogues construits à l’extérieur, leurs références de produits, prix, zones géographiques d’application et évolutions.

**Nature :** non établie — ne pas déduire automatiquement (unchanged_or_not_established).
**Frontière :** Aucune gouvernance locale du prix ou du catalogue.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Recevoir offre et zone d’application avec références produit.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D08.d Product Reference Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Maître externe à identifier selon le contexte ; projection en lecture/recherche, sans administration locale implicite.

**Accords conservés :** scope. Aucun accord étendu aux nouveaux textes.

## D13.a — Fulfillment Network Ingestion

**Recommandation : Conserver** — Projection des lieux/liens, différente de capacité et offre de service.

**Nom cible :** Fulfillment Network Ingestion (nom courant : Fulfillment Network Ingestion).

**Avant :** recevoir les points du réseau, leurs caractéristiques de référence, leurs relations et liens vers les parties responsables, ainsi que leurs évolutions depuis les sources maîtresses externes.

**Cible proposée / valeur conservée :** recevoir les points du réseau, leurs caractéristiques de référence, leurs relations et liens vers les parties responsables, ainsi que leurs évolutions depuis les sources maîtresses externes.

**Nature :** non établie — ne pas déduire automatiquement (unchanged_or_not_established).
**Frontière :** Ne décide pas implantation du réseau ni charge opérationnelle.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Recevoir darkstore et liens de desserte.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D09.d Party / Role Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Maître externe à identifier selon le contexte ; projection en lecture/recherche, sans administration locale implicite.

**Accords conservés :** scope. Aucun accord étendu aux nouveaux textes.

## D14.a — Execution Service Catalog Ingestion

**Recommandation : Conserver** — Projection de services/SLA/accès, différente du suivi.

**Nom cible :** Execution Service Catalog Ingestion (nom courant : Execution Service Catalog Ingestion).

**Avant :** Recevoir l’offre des services exécutants, leurs SLA configurés, conditions et accès, ainsi que leurs évolutions depuis les sources maîtresses externes.

**Cible proposée / valeur conservée :** Recevoir l’offre des services exécutants, leurs SLA configurés, conditions et accès, ainsi que leurs évolutions depuis les sources maîtresses externes.

**Nature :** action (unchanged_or_not_established).
**Frontière :** SLA, engagement individuel, estimation et résultat distincts ; pas de maître local.

**Fonctions conservées :** Les opérations utiles de la fiche actuelle restent explicables dans le périmètre ; aucune promotion automatique en comportement.

**Exemple fictif :** Recevoir service documentaire et accès sollicitation/feedback.

**Comportements :** Aucune décomposition recommandée à ce stade.
**Justification de décomposition :** Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.

**A besoin de — proposition :** D09.d Party / Role Ingestion, D13.a Fulfillment Network Ingestion
**Marché / justification :** Justification FLOW ; pas de nouvelle équivalence marché établie.

**Entrées externes :** Maître externe à identifier selon le contexte ; projection en lecture/recherche, sans administration locale implicite.

**Accords conservés :** Aucun champ adopté dans le lifecycle ; autres preuves historiques conservées dans le modèle.. Aucun accord étendu aux nouveaux textes.

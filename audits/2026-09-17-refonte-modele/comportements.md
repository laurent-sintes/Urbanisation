# Comportements et migration

> Revue de référence U286–U289 avant migration. Le socle a été appliqué U290 ; les mentions de proposition ou de migration à venir ci-dessous décrivent cet état antérieur. Voir le [bilan courant](../2026-09-17-refonte-appliquee/rapport.md).

[Synthèse](rapport.md)

Clés PLAN/PROTECT/COUNT/ORCH : repères de proposition, pas IDs de nouveaux nœuds. Un parent explicite, même couche ; pas de sous-comportement. Les quatre comportements COUNT/ORCH sont conditionnels.

## BHV001 — Existing Commitment Consideration

Parent : D03.i — Available-to-Promise (ATP). Statut : existing_adopted_rationale_proposed.

Établir les quantités admissibles pour la demande en tenant compte des allocations, protections et réservations, sans double décompte.

**Critère :** politique. **Bénéfice :** Respecter les droits sans promettre deux fois la même quantité.

**Exemple fictif :** 100 présentes dont 30 engagées ne donnent pas 100 libres.

**Frontière :** Situation de référence ; aucune réservation par ATP.

**Appui :** Justification FLOW ; pas de nouvelle équivalence marché établie.

## BHV002 — Network Stock Availability

Parent : D03.i — Available-to-Promise (ATP). Statut : existing_adopted_rationale_proposed.

Établir les possibilités de satisfaction à partir des lieux admissibles, entrepôts, magasins, darkstores ou autres espaces de stockage.

**Critère :** variante. **Bénéfice :** Élargir les possibilités au réseau admissible.

**Exemple fictif :** Un magasin autorisé contribue lorsque l’entrepôt est vide.

**Frontière :** Pas de comportement par type de lieu.

**Appui :** Justification FLOW ; pas de nouvelle équivalence marché établie.

## BHV003 — Operational Availability Timing

Parent : D03.i — Available-to-Promise (ATP). Statut : existing_adopted_rationale_proposed.

Déterminer quand une quantité peut effectivement contribuer à la promesse selon sa disponibilité opérationnelle.

**Critère :** mécanisme. **Bénéfice :** Convertir présence en disponibilité utilisable à temps.

**Exemple fictif :** Réserve mobilisable dans 2 jours versus rack disponible aujourd’hui.

**Frontière :** Consomme les délais opérationnels ; ne réorganise pas le prélèvement.

**Appui :** Justification FLOW ; pas de nouvelle équivalence marché établie.

## BHV004 — Future Supply Projection

Parent : D03.i — Available-to-Promise (ATP). Statut : existing_adopted_rationale_proposed.

Établir les possibilités à l’échéance en intégrant les réceptions attendues et les engagements concurrents, pour une promesse ou un ensemble.

**Critère :** mécanisme. **Bénéfice :** Permettre engagement futur sans exiger le stock aujourd’hui.

**Exemple fictif :** Arrivage J+7 contribuant à J+60 après autres engagements.

**Frontière :** Pas de création d’approvisionnement par ATP.

**Appui :** Justification FLOW ; pas de nouvelle équivalence marché établie.

## PLAN-CONSTRUCT — Scenario Construction

Parent : D05.f — Inventory Planning. Statut : direction_adopted_wording_proposed.

Construire plusieurs réponses possibles en explicitant leurs hypothèses, objectifs et contraintes.

**Critère :** variante. **Bénéfice :** Explorer des alternatives avant engagement.

**Exemple fictif :** Couvertures à 10 ou 15 jours pour les mêmes demandes.

**Frontière :** Copier est une fonction ; décisions spécialisées distinctes.

**Appui :** [S07 — Kinaxis](https://www.kinaxis.com/en/solutions/sales-and-operations-planning)

## PLAN-SIMULATE — Simulation & Analysis

Parent : D05.f — Inventory Planning. Statut : combined_behavior_adopted_wording_proposed.

Projeter les conséquences d’un scénario et analyser leurs impacts sur les indicateurs métier et les processus pour éclairer les choix.

**Critère :** mécanisme. **Bénéfice :** Comprendre compromis et effets locaux.

**Exemple fictif :** Service 94 à 97 %, stock +120 k€ ; identifier les magasins perdants.

**Frontière :** BHV006 et BHV010 réunis ; comparer reste une fonction, aucun recalcul imposé.

**Appui :** [S07 — Kinaxis](https://www.kinaxis.com/en/solutions/sales-and-operations-planning)

## PLAN-ADAPT — Scenario Execution Adaptation

Parent : D05.f — Inventory Planning. Statut : direction_adopted_wording_proposed.

Adapter le scénario de stock en cours aux écarts observés, compte tenu des actions engagées et des décisions spécialisées.

**Critère :** mécanisme. **Bénéfice :** Maintenir une trajectoire cohérente malgré les aléas.

**Exemple fictif :** Réviser apports et transferts après report fournisseur sans oublier les quantités expédiées.

**Frontière :** D06 décide la variation opérationnelle ; D04/D02.b appliquent leurs changements.

**Appui :** [S07 — Kinaxis](https://www.kinaxis.com/en/solutions/sales-and-operations-planning)

## PROTECT-GROUP — Group Supply Protection

Parent : D02.b — Supply Protection. Statut : proposed.

Configurer les droits préservant l’accès d’un groupe à des ressources face aux usages concurrents.

**Critère :** politique. **Bénéfice :** Éviter qu’une demande précoce épuise les ressources d’un autre groupe.

**Exemple fictif :** Préserver 200 pièces pour le web avant sa demande.

**Frontière :** Protection mutuelle ou priorisée décrites ensemble ; D05.d décide les quantités.

**Appui :** [S01 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), [S02 — SAP](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-)

## PROTECT-CAP — Consumption Capping

Parent : D02.b — Supply Protection. Statut : proposed.

Configurer les limites de consommation d’un groupe sur le périmètre et la période retenus.

**Critère :** politique. **Bénéfice :** Empêcher la surconsommation même si du stock reste accessible.

**Exemple fictif :** Un groupe ne dépasse pas 500 malgré un stock supérieur.

**Frontière :** Préserver un minimum et limiter un maximum diffèrent ; imputation et correction sont fonctions.

**Appui :** [S01 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation)

## PROTECT-BUFFER — Safety Stock Policy

Parent : D02.b — Supply Protection. Statut : proposed.

Configurer le stock tampon et ses conditions d’utilisation pour absorber les incertitudes.

**Critère :** mécanisme. **Bénéfice :** Expliciter le rôle de sécurité sans le confondre avec réservation ou déclenchement.

**Exemple fictif :** Sécurité 40 pour absorber retard fournisseur ; préciser quand elle peut être consommée.

**Frontière :** D05.a décide le niveau ; ne pas additionner deux fois le tampon et le minimum de réassort.

**Appui :** [S04 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-replenishment), [S05 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/policy-assignment-sets.html)

## PROTECT-REPLENISH — Replenishment Regulation

Parent : D02.b — Supply Protection. Statut : proposed.

Configurer les règles de déclenchement et de limitation du réassort qui encadrent le renouvellement du stock.

**Critère :** mécanisme. **Bénéfice :** Prévenir manque et excès par des règles cohérentes de renouvellement.

**Exemple fictif :** Sous 60 viser 100 ; appliquer la baisse de cible décidée en fin de vie.

**Frontière :** Min/Max et revue périodique décrites comme modalités, sans sous-comportements ; D05.e décide et D04 gère les apports.

**Appui :** [S03 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification), [S05 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/policy-assignment-sets.html), [S06 — RELEX](https://www.relexsolutions.com/solutions/automatic-replenishment-system/)

## COUNT-RECUR — Recurring Stock Verification

Parent : D01.d — Stocktaking. Statut : conditional_arbitration.

Fiabiliser le stock par un programme récurrent de constats et de rapprochements ciblés.

**Critère :** politique. **Bénéfice :** Organiser une fiabilisation régulière selon les risques.

**Exemple fictif :** Contrôles réguliers des références sensibles puis corrections justifiées.

**Frontière :** Réalisation du comptage chez l’exécutant ; mandat du programme à préciser.

**Appui :** [S08 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting)

## COUNT-TRIGGER — Triggered Stock Verification

Parent : D01.d — Stocktaking. Statut : conditional_arbitration.

Fiabiliser une situation de stock par une vérification ciblée face à un signal.

**Critère :** mécanisme. **Bénéfice :** Traiter une incertitude locale sans attendre le cycle régulier.

**Exemple fictif :** Recomptage après écart de préparation.

**Frontière :** Seuil ou anomalie sont déclencheurs ; pas un comportement par motif.

**Appui :** [S08 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting)

## ORCH-DEPEND — Dependency-driven Execution

Parent : D06.d — Execution Orchestration. Statut : conditional_arbitration.

Coordonner les prestations selon leurs prérequis et les résultats observés du plan retenu.

**Critère :** mécanisme. **Bénéfice :** Éviter des sollicitations dont les prérequis métier ne sont pas satisfaits.

**Exemple fictif :** Collecte conditionnée aux colis prêts et au document requis.

**Frontière :** Pas de workflow universel ; D06.f décide les variations.

**Appui :** [S11 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/faiom/overview-of-managing-change-that-occurs-during-order-fulfillment.html)

## ORCH-COMPENSATE — Execution Compensation

Parent : D06.d — Execution Orchestration. Statut : conditional_arbitration.

Coordonner les ajustements des prestations engagées pour appliquer une variation retenue en respectant les effets irréversibles.

**Critère :** mécanisme. **Bénéfice :** Éviter doublons et annulations impossibles lors d’un changement.

**Exemple fictif :** Changer de collecte après préparation ; révoquer seulement ce qui reste annulable.

**Frontière :** Pas de rollback physique ; décision D06.f et gestion D07.b distinctes.

**Appui :** [S11 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/faiom/overview-of-managing-change-that-occurs-during-order-fulfillment.html)

## PROMISE-PROPOSE — Promise Proposal

Parent : PROMISE-MANAGEMENT — Promise Management. Statut : behavior_role_adopted_U288_definition_reuse_proposed.

Construire une proposition de mise à disposition de ressources pour honorer une commande Supply, précisant quantités, dates, conditions et alternatives possibles, à partir des ressources et possibilités de réalisation.

**Critère :** mécanisme. **Bénéfice :** Explorer et expliciter une solution sans produire d’engagement confirmé.

**Exemple fictif :** 60 vendredi et 40 lundi proposés ; aucune réservation ou confirmation déduite.

**Frontière :** Comportement de Promise Management selon U288. Les décisions de faisabilité, priorisation et échéancier restent distinctes ; confirmation ne prouve pas réservation, affectation ou prise en charge de service.

**Appui :** Justification FLOW ; pas de nouvelle équivalence marché établie.

## PROMISE-CONFIRM — Promise Confirmation

Parent : PROMISE-MANAGEMENT — Promise Management. Statut : behavior_role_adopted_U288_definition_reuse_proposed.

établir les quantités et dates promises, en distinguant la part confirmée de celle qui ne l’est pas.

**Critère :** politique. **Bénéfice :** Faire passer des possibilités à un engagement explicite selon les autorisations et conditions.

**Exemple fictif :** 60 confirmées vendredi, 40 encore non confirmées ; affectation et réservation gardent leur contrat.

**Frontière :** Comportement de Promise Management selon U288. Les décisions de faisabilité, priorisation et échéancier restent distinctes ; confirmation ne prouve pas réservation, affectation ou prise en charge de service.

**Appui :** Justification FLOW ; pas de nouvelle équivalence marché établie.

## PROMISE-REVISE — Promise Revision

Parent : PROMISE-MANAGEMENT — Promise Management. Statut : behavior_role_adopted_U288_definition_reuse_proposed.

Réexaminer les promesses lorsque les ressources, commandes, dates ou priorités changent et établir les modifications autorisées.

**Critère :** mécanisme. **Bénéfice :** Maintenir les engagements cohérents lorsque ressources, demandes ou priorités évoluent.

**Exemple fictif :** Réexaminer les 40 après report d’arrivage et tracer la révision autorisée.

**Frontière :** Comportement de Promise Management selon U288. Les décisions de faisabilité, priorisation et échéancier restent distinctes ; confirmation ne prouve pas réservation, affectation ou prise en charge de service.

**Appui :** [S10 — SAP](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/73a1a457ef816b10e10000000a441470.html)

## Destination de chaque comportement existant

| Ancien ID | Nom | Traitement proposé | Destination | Conservation du besoin |
| --- | --- | --- | --- | --- |
| BHV001 | Existing Commitment Consideration | retain | BHV001 | Définition conservée ; justification rééprouvée selon U283. |
| BHV002 | Network Stock Availability | retain | BHV002 | Définition conservée ; justification rééprouvée selon U283. |
| BHV003 | Operational Availability Timing | retain | BHV003 | Définition conservée ; justification rééprouvée selon U283. |
| BHV004 | Future Supply Projection | retain | BHV004 | Définition conservée ; justification rééprouvée selon U283. |
| BHV005 | Scenario Construction | revise_definition | PLAN-CONSTRUCT | Préciser la construction d’alternatives ; conserver l’identité. |
| BHV006 | Scenario Simulation | broaden_and_rename | PLAN-SIMULATE | Conserver l’identité de simulation en intégrant l’analyse. |
| BHV010 | Scenario Impact Analysis | absorb_then_retire | PLAN-SIMULATE | Préserver indicateurs et explications dans le comportement combiné et archiver les accords U271. |
| BHV007 | Scenario Evaluation | demote_to_description | D05.f | Conserver comparaison/appréciation sans nœud autonome. |
| BHV008 | Scenario Validation | demote_to_description | D05.f | Conserver autorisation, conditions et réserves sans nœud autonome. |
| BHV009 | Scenario Application | demote_to_description | D05.f | Conserver application et prise en compte ; ne pas réutiliser cet ID pour adaptation. |
| BHV011 | Allocation | demote_to_description | D02.b | Conserver les opérations sur les enveloppes comme fonctions des mécanismes concernés ; pas de comportement par opération. |
| BHV012 | Reallocation | demote_to_description | D02.b | Conserver les opérations sur les enveloppes comme fonctions des mécanismes concernés ; pas de comportement par opération. |
| BHV013 | Allocation Release | demote_to_description | D02.b | Conserver les opérations sur les enveloppes comme fonctions des mécanismes concernés ; pas de comportement par opération. |
| BHV014 | Allocation Consumption | demote_to_description | D02.b | Conserver les opérations sur les enveloppes comme fonctions des mécanismes concernés ; pas de comportement par opération. |
| BHV015 | Allocation Visibility | demote_to_description | D02.b | Conserver les opérations sur les enveloppes comme fonctions des mécanismes concernés ; pas de comportement par opération. |

Les noms et valeurs adoptés sont conservés dans la capture et l’annexe. À la migration, BHV006 conserve son identité avec révision de contenu, BHV010 est absorbé et retiré. BHV009 ne devient pas adaptation : un nouvel identifiant sera créé. Les cinq comportements d’allocation sont retirés comme nœuds, avec leurs fonctions replacées dans Protection. Aucune de ces mutations n’est encore exécutée.

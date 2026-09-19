# Marché — preuves et limites

Consultation le 17 septembre 2026. Sources primaires ciblées ; pas d’étude exhaustive de tous les éditeurs ni de preuve de déploiement. Chaque rapprochement est proposé ; les choix de maille restent FLOW.

## S01 — Microsoft : Inventory Visibility inventory allocation

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation) — Page évolutive. Passage : Business background ; allocation APIs.
Protection des groupes et contrôle de surconsommation distincts des opérations API.
Limite : Ne tranche pas Reservation/Assignment FLOW.

## S02 — SAP : Outlining aATP with Supply Protection

[Source primaire](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-) — Cours sans édition unique. Passage : Core ; Prioritized ; Time Buckets.
Protection mutuelle ou priorisée ; validité et consommation contextualisées.
Limite : SuP ne couvre pas toute la prévention du surstock FLOW.

## S03 — Microsoft : Replenishment methods and quantity modification

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification) — Page évolutive. Passage : Period ; Min/Max ; quantity modification.
Méthodes de réassort et contraintes de quantité ont des effets distincts.
Limite : Une cible maximum n’est pas toujours un plafond dur.

## S04 — Microsoft : Safety stock fulfillment for items

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-replenishment) — Page évolutive. Passage : Min/Max ; variations temporelles.
Sécurité et niveaux de réassort alimentent la planification.
Limite : Tampon ne signifie pas interdiction universelle de consommer.

## S05 — Oracle : Policy Assignment Sets

[Source primaire](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/policy-assignment-sets.html) — 26B. Passage : Policy types ; overrides.
Méthodes et paramètres affectables aux segments et articles-lieux.
Limite : Configuration produit, pas catalogue de capacités.

## S06 — RELEX : Replenishment and allocation

[Source primaire](https://www.relexsolutions.com/solutions/automatic-replenishment-system/) — Page commerciale évolutive. Passage : Store space ; shelf-life ; ramp-downs.
Espace, durée de vie et arrêt progressif influencent les apports.
Limite : Pas de contrat détaillé ; markdown et planification de saison hors FLOW.

## S07 — Kinaxis : Sales and operations planning

[Source primaire](https://www.kinaxis.com/en/solutions/sales-and-operations-planning) — Page commerciale évolutive. Passage : Advanced scenarios ; Real-time agility.
Simulation, impacts et ajustements sont associés à la coordination.
Limite : Ne prescrit pas les trois comportements FLOW.

## S08 — Microsoft : Cycle counting

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting) — Page évolutive ; Warehouse management. Passage : Automatically create work ; Spot cycle counting.
Plans récurrents et contrôles déclenchés selon la situation sont distingués.
Limite : Périmètre WMS ; réalisation des comptages chez les exécutants.

## S09 — Microsoft : Action messages

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages) — Page datée 2026-03-26. Passage : Types of action messages.
Recommandations d’avancement, report et réduction d’apports.
Limite : Recommandation différente de l’autorisation de modifier une commande ferme.

## S10 — SAP : Backorder Processing (CA-ATP-BOP)

[Source primaire](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/73a1a457ef816b10e10000000a441470.html) — Édition non établie ; extrait indexé. Passage : Présentation BOP.
Une évolution offre/demande motive le réexamen des confirmations.
Limite : Appui à la révision ; ne démontre pas le regroupement Promise Management.

## S11 — Oracle : Managing Change During Order Fulfillment

[Source primaire](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/faiom/overview-of-managing-change-that-occurs-during-order-fulfillment.html) — 25C, historique explicite. Passage : Compensation ; fulfillment changes.
Un changement peut nécessiter des ajustements aux tâches engagées.
Limite : Aucun rollback physique universel ni reproduction du moteur Oracle.

## S12 — Microsoft : Inventory Visibility reservations

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations) — Page évolutive. Passage : Soft reservations ; offsets.
Réservation logique et décompte demandent une articulation explicite.
Limite : N’impose pas une fusion Reservation/Assignment.

## S13 — Microsoft : Firm planned orders

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming) — Page évolutive. Passage : Firming planned orders.
Affermir transforme les ordres planifiés en commandes d’achat, transfert ou production.
Limite : Ne démontre ni atomicité d’un scénario ni rattachement dans FLOW ; production non ajoutée au catalogue.

## S14 — Oracle : Release Plan

[Source primaire](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspc/release-plan.html) — 26B. Passage : Release planning recommendations.
La libération du plan transmet des recommandations nouvelles ou replanifiées vers les systèmes opérationnels via Supply Chain Orchestration.
Limite : Le composant Oracle couvre plusieurs responsabilités FLOW ; ne pas assimiler sa Supply Chain Orchestration à D06 seulement.


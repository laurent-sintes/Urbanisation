# Sources primaires — audit U292

Consultation : 17 septembre 2026. Les faits documentés sont séparés des recommandations FLOW. Les pages produit ne valent pas spécifications de couverture. Aucun déploiement Beaumanoir démontré. Synthèses sélectives ; aucune reproduction substantielle.

## S01 — Microsoft — Cycle counting

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting) — D365 SCM ; page évolutive.

Nature : documentation. Accès : Texte primaire consulté. Passage : Cycle counting plans / thresholds.

**Constat documentaire.** Les plans organisent les comptages ; un seuil de quantité peut déclencher un travail de comptage. L’existence du travail ne bloque pas automatiquement le stock.

**Limites.** Fonctions WMS : le détenteur du programme de contrôle FLOW reste à préciser ; aucune appropriation des opérations physiques.

## S02 — Microsoft — Inventory Visibility soft reservations

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations) — Inventory Visibility ; page évolutive.

Nature : documentation. Accès : Texte primaire consulté. Passage : Soft reservation / offset.

**Constat documentaire.** Un engagement logique réduit le disponible à réserver sans changer le stock physique. Un offset permet de rapprocher cette réservation de la réservation physique et d’éviter un double débit.

**Limites.** Soft ne signifie pas temporaire ni expiration automatique. Certains réglages autorisent la survente ; les garanties dépendent du contrat et de la configuration.

## S03 — Microsoft — Reserve inventory quantities

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities) — D365 SCM ; page évolutive.

Nature : documentation. Accès : Texte primaire consulté. Passage : Inventory reservation policies.

**Constat documentaire.** Les règles de réservation incluent FIFO, FEFO, même lot et prise en compte du stock commandé.

**Limites.** Une politique de sélection de stock ne prouve pas un comportement autonome ; certaines règles relèvent de l’exécutant.

## S04 — SAP — Explaining Supply Assignment

[Source primaire](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4) — S/4HANA Fashion ; cours évolutif.

Nature : documentation. Accès : Texte primaire consulté. Passage : Supply Assignment / Release checks.

**Constat documentaire.** ARun rapproche ressources et demandes ; les contrôles de taux de satisfaction conditionnent la libération de groupes de lignes. Une affectation ne suffit donc pas à autoriser la livraison.

**Limites.** Fonction et processus produit ; aucune preuve d’optimum global ni équivalence entre affectation, réservation et libération FLOW.

## S05 — SAP — Alternative-Based Confirmation

[Source primaire](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5) — S/4HANA ; cours couvrant plusieurs évolutions.

Nature : documentation. Accès : Texte primaire consulté. Passage : Alternative-Based Confirmation.

**Constat documentaire.** ABC examine des alternatives de sites et de produits pour améliorer les confirmations.

**Limites.** L’appellation aATP SAP ne fixe pas la frontière ATP/CTP FLOW. Une alternative déjà admissible peut relever de notre ATP ; une substitution exige des équivalences autorisées.

## S06 — SAP — Exploring Backorder Processing

[Source primaire](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe) — S/4HANA Cloud Public Edition ; cours évolutif.

Nature : documentation. Accès : Texte primaire consulté. Passage : Confirmation strategies.

**Constat documentaire.** Les stratégies BOP différencient les demandes dont la confirmation doit être préservée ou améliorée de celles qui peuvent céder des quantités.

**Limites.** Stratégies de produit ; ne pas copier chaque stratégie comme enfant de Promise Revision, qui est déjà terminal.

## S07 — Microsoft — Calculate delivery dates using CTP

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp) — Planning Optimization ; page évolutive.

Nature : documentation. Accès : Texte primaire consulté. Passage : CTP calculations.

**Constat documentaire.** CTP vérifie la faisabilité avec matières et capacités, notamment dans un contexte de fabrication.

**Limites.** Le CTP FLOW est plus large : adaptations Supply. Les variantes batch/temps réel ne justifient pas de comportements métier.

## S08 — Microsoft — Replenishment methods and quantity modification

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification) — D365 SCM ; mise à jour affichée 2026-07-01.

Nature : documentation. Accès : Texte primaire consulté. Passage : Requirement / Period / Min-Max.

**Constat documentaire.** Requirement couvre les besoins ; Period les regroupe sur une fenêtre ; Min/Max restaure une cible lorsque le seuil est franchi. Des contraintes de quantité modifient les propositions.

**Limites.** Regrouper les besoins par période ne signifie pas nécessairement revoir les stocks à cadence fixe. Un multiple de commande est un paramètre, pas un comportement.

## S09 — Microsoft — Action messages

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages) — D365 SCM ; page évolutive.

Nature : documentation. Accès : Texte primaire consulté. Passage : Advance / Postpone / Increase / Decrease.

**Constat documentaire.** La planification recommande des changements de dates ou de quantités sur des apports existants, selon les contraintes configurées.

**Limites.** Recommander ne modifie pas automatiquement une commande ferme ; ces verbes restent les opérations d’un mécanisme commun.

## S10 — Microsoft — Safety stock journal

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-journal) — D365 SCM ; page évolutive.

Nature : documentation. Accès : Texte primaire consulté. Passage : Calculate proposal / service level.

**Constat documentaire.** Les propositions de minimum mobilisent usages historiques, variabilité et niveau de service. Le produit permet ensuite d’appliquer les valeurs proposées.

**Limites.** FLOW sépare décision D05 et application D02.b. Minimum, cible et quantité rendue indisponible ne sont pas synonymes.

## S11 — Microsoft — Priority-based planning

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/priority-based-planning) — D365 SCM ; page évolutive.

Nature : documentation. Accès : Texte primaire consulté. Passage : Planning priority / net flow position.

**Constat documentaire.** La priorité de réapprovisionnement tient compte de la position de stock relativement aux seuils et aux cibles.

**Limites.** Urgence d’un besoin de stock et priorité commerciale d’un Order sont deux responsabilités à relier, pas à fusionner.

## S12 — Oracle — Overview of inventory rebalancing

[Source primaire](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html) — Fusion Cloud SCM 26B.

Nature : documentation. Accès : Texte primaire consulté. Passage : Inventory rebalancing / sweep locations.

**Constat documentaire.** Le rebalancing utilise des excédents pour couvrir des manques dans un groupe de lieux. Des lieux de collecte peuvent recevoir les excédents restants ; la protection du lieu donneur est prise en compte.

**Limites.** Mécanismes documentés ; pas promesse d’optimum réseau universel ni preuve de déploiement FLOW.

## S13 — Kinaxis — Probabilistic MEIO by Wahupa

[Source primaire](https://www.kinaxis.com/en/solutions/applications/probabilistic-meio-wahupa) — Page produit sans édition.

Nature : présentation produit. Accès : Texte primaire consulté. Passage : Multi-echelon inventory optimization.

**Constat documentaire.** L’offre présente un arbitrage probabiliste entre stock, coût et service, en coordonnant plusieurs échelons du réseau.

**Limites.** Présentation commerciale primaire : principe documenté, détail algorithmique et couverture exacte non établis. Appui moyen, pas preuve équivalente à un guide.

## S14 — RELEX — Inventory planning software

[Source primaire](https://www.relexsolutions.com/resources/inventory-planning-software/) — Page produit sans édition.

Nature : présentation produit. Accès : Texte primaire consulté. Passage : Fresh safety stock / inventory planning.

**Constat documentaire.** La présentation relie stock de sécurité, variabilité, niveau de service et coûts, dont la perte liée à la périssabilité pour les produits frais.

**Limites.** Périssabilité et pertinence par assortiment à vérifier. Ne pas transposer automatiquement des mécanismes alimentaires au textile.

## S15 — Manhattan — Optimized Fulfillment Sourcing

[Source primaire](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing) — Manhattan Active OMS ; page sans édition.

Nature : présentation produit. Accès : Texte primaire consulté. Passage : Sourcing objectives / inventory and operational factors.

**Constat documentaire.** Le sourcing considère service, coûts, marge, état des stocks et contraintes opérationnelles. La consolidation peut réduire les envois fragmentés.

**Limites.** Page produit : pas de spécification des garanties d’optimalité. L’offre traverse plusieurs capacités FLOW et ne fournit pas une hiérarchie à copier.

## S16 — Blue Yonder — Order Promising and Optimization

[Source primaire](https://blueyonder.com/solutions/order-management-and-commerce/order-promising-and-optimization) — Page produit sans édition.

Nature : présentation produit. Accès : Texte primaire consulté. Passage : Order promising and optimization.

**Constat documentaire.** La présentation combine disponibilité, coûts, lieux, vitesse et contraintes de réalisation dans le choix de fulfillment.

**Limites.** Appui aux dimensions de valeur uniquement. Pas de déduction sur un algorithme, un comportement précis ou la couverture installée.

## S17 — Oracle — Compensate Sales Orders That Change

[Source primaire](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html) — Fusion Cloud SCM 26B.

Nature : documentation. Accès : Texte primaire consulté. Passage : Compensation patterns / introductory warehouse example.

**Constat documentaire.** Des règles ajustent les tâches d’orchestration après changement : l’exemple de changement d’entrepôt annule puis recrée une demande d’expédition.

**Limites.** Compensation logique ; aucune garantie de retour arrière d’un fait physique. Les primitives Undo/Redo ne deviennent pas des comportements FLOW.

## S18 — Oracle — Guidelines for Managing Shipment Sets

[Source primaire](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/guidelines-for-managing-shipment-sets.html) — Fusion Cloud SCM 26A ; édition explicitement consultée.

Nature : documentation. Accès : Texte primaire consulté. Passage : Holds / splitting / scheduling.

**Constat documentaire.** Des lignes destinées à partir ensemble partagent des contraintes ; la mise en attente d’une ligne peut retenir l’ensemble. Des modifications nécessitent de sortir la ligne du groupe.

**Limites.** Ne pas universaliser les règles produit ; 26A n’est pas présentée comme dernière édition. La cohérence de groupe touche échéancier, structure et libération.

## S19 — SAP — Expected Event Overdue List

[Source primaire](https://help.sap.com/docs/SAP_EVENT_MANAGEMENT/1d2d343a67074058a30cd9ffd093ab50/bebccb53ad377114e10000000a174cb4.html) — SAP Event Management ; édition de la page non affichée.

Nature : documentation. Accès : Extrait officiel indexé ; ouverture sans corps exploitable. Passage : Expected Event Overdue List.

**Constat documentaire.** Le rapport repère les événements attendus en retard.

**Limites.** Extrait primaire indexé uniquement ; page ouverte sans corps exploitable. Produit historique, aucune affirmation de stratégie produit actuelle. Un retour absent ne prouve pas un retard physique.

## S20 — Oracle — IMPORTANT Actions and Considerations

[Source primaire](https://docs.oracle.com/en/cloud/saas/readiness/scm/26b/order26b/26B-order-mgmt-wn-t72535.htm) — Release Readiness 26B.

Nature : documentation. Accès : Texte primaire consulté. Passage : Removed Features: Planning for Orchestration Processes.

**Constat documentaire.** La note annonce le retrait de Planning for Orchestration Processes en 26D, avec désactivation du paramètre de planning et calcul de jeopardy.

**Limites.** Retrait annoncé pour 26D, pas retrait déjà effectif en 26B. Ne pas prendre cet ancien mécanisme comme preuve pérenne d’une recommandation de tracking.

## S21 — Microsoft — Inventory blocking

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking) — D365 SCM ; mise à jour affichée 2025-08-14.

Nature : documentation. Accès : Texte primaire consulté. Passage : Blocking inventory / expected receipts.

**Constat documentaire.** Du stock physique peut être bloqué pour la consommation ; une libération attendue peut intervenir dans la projection.

**Limites.** Décision qualité et opération de blocage ne sont pas automatiquement dans Supply Protection. Risques de double exclusion selon les mécanismes combinés.

## S22 — Microsoft — Inventory statuses

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-statuses) — D365 SCM ; page évolutive.

Nature : documentation. Accès : Texte primaire consulté. Passage : Inventory statuses.

**Constat documentaire.** Le statut permet de distinguer présence physique et disponibilité d’usage, avec des restrictions de modification selon les travaux en cours.

**Limites.** Un statut ou un lieu n’est pas à lui seul un comportement. FLOW doit recevoir l’état opposable sans inventer sa gouvernance.

## S23 — Microsoft — Sales returns

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns) — D365 SCM ; page évolutive.

Nature : documentation. Accès : Texte primaire consulté. Passage : Disposition actions / replacement orders.

**Constat documentaire.** Les dispositions peuvent conduire à remettre en stock, rebuter, retourner ou remplacer ; elles ont aussi des conséquences financières.

**Limites.** Processus produit plus large que Customer Return Management FLOW ; la décision de devenir et les conséquences financières ne sont pas attribuées par simple proximité.

## S24 — SAP — Outlining aATP with Supply Protection

[Source primaire](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-) — S/4HANA ; cours évolutif.

Nature : documentation. Accès : Texte primaire consulté. Passage : Core Supply Protection / Prioritized Supply Protection.

**Constat documentaire.** SAP distingue protections entre groupes et protections selon leur priorité. Une protection priorisée n’est pas un plafond absolu de consommation pour le groupe prioritaire.

**Limites.** Protection de groupe et plafonnement ont des effets différents. FLOW possède déjà BHV017 et BHV018 ; pas de sous-comportements supplémentaires.

## S25 — Oracle — Add Branches to Orchestration Processes

[Source primaire](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/add-branches-to-orchestration-processes.html) — Fusion Cloud SCM 26B.

Nature : documentation. Accès : Texte primaire consulté. Passage : Branching example / orchestration rules.

**Constat documentaire.** Les règles permettent d’orienter un processus d’orchestration selon des conditions métier.

**Limites.** Appui à la coordination conditionnelle ; ne prouve pas à lui seul toutes les sémantiques de synchronisation ou de parallélisme FLOW.

## S26 — Microsoft — Review and accept changes to confirmed purchase orders

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-changes-after-confirmation) — D365 SCM ; mise à jour affichée 2026-07-01.

Nature : documentation. Accès : Texte primaire consulté. Passage : Impacted downstream orders / review changes.

**Constat documentaire.** Les modifications fournisseur sur des achats confirmés sont examinées avec leurs conséquences sur les demandes aval avant reconfirmation. Le guide limite l’analyse aux impacts directs.

**Limites.** Le produit ne couvre pas tous les effets indirects. IA, écran et batch ne deviennent pas des comportements ; négociation et engagement reçu sont à distinguer de la promesse émise par FLOW.

## S27 — Microsoft — Create a purchase return order

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/create-purchase-return-order) — D365 SCM ; mise à jour affichée 2025-09-03.

Nature : documentation. Accès : Texte primaire consulté. Passage : Scenarios / marking / shipment.

**Constat documentaire.** Les retours fournisseur peuvent être partiels et référencer les réceptions ; le processus produit associe également des pièces financières.

**Limites.** Variantes et traçabilité utiles au périmètre existant. L’écriture financière n’est pas importée comme responsabilité Supply.

## S28 — Microsoft — Inventory Visibility inventory allocation

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation) — Inventory Visibility ; page évolutive.

Nature : documentation. Accès : Texte primaire consulté. Passage : Business background and purpose / Difference between inventory allocation and soft reservation.

**Constat documentaire.** La protection de quantités par groupes et le contrôle de surconsommation sont deux finalités explicites. Les enveloppes précèdent les transactions de vente ; la réservation logique peut imputer leur consommation.

**Limites.** Allocation désigne ici des droits de groupes, pas notre Supply Assignment. Les opérations des API ne constituent pas des comportements métier.

## S29 — SAP — SAP Business Network Global Track and Trace

[Source primaire](https://www.sap.com/products/business-network/global-track-and-trace.html) — Page produit évolutive, édition non indiquée.

Nature : présentation produit. Accès : Texte primaire consulté. Passage : FAQ: logistics visibility / solution scope.

**Constat documentaire.** Visibilité des expéditions : localisation, progression, statut et arrivée estimée, avec contexte commande ; alertes en cas de perturbation.

**Limites.** Présentation produit primaire, pas garantie universelle de précision ou de temps réel.

## S30 — Microsoft — Landed cost module overview

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/landed-cost-overview) — D365 SCM, page évolutive.

Nature : documentation. Accès : Texte primaire consulté. Passage : Goods in transit / tracking.

**Constat documentaire.** Le module documente les marchandises en transit et le suivi de leurs dates de livraison.

**Limites.** Périmètre produit spécifique ; pas équivalence intégrale avec le tracking multi-services FLOW, ni télémétrie continue démontrée.

## S31 — Microsoft — Approve and confirm purchase orders

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation) — D365 SCM ; mise à jour affichée 2026-09-08.

Nature : documentation. Accès : Texte primaire consulté. Passage : Approval / Changing / Canceling purchase orders.

**Constat documentaire.** Le guide distingue statuts de commande, approbation, modification et annulation du reliquat non réalisé. Le workflow d’approbation organise les activités permettant certains changements.

**Limites.** Pas de cycle universel à copier ; clôture financière hors périmètre de notre exemple.

## S32 — Camunda — Compensation

[Source primaire](https://docs.camunda.io/docs/components/modeler/bpmn/compensation-handler/) — Version affichée 8.9.

Nature : documentation. Accès : Texte primaire consulté. Passage : Compensation handlers.

**Constat documentaire.** Les gestionnaires de compensation traitent les effets d’activités achevées.

**Limites.** Document de réalisation BPMN, pas modèle métier ; ne prouve pas que toute compensation implique Case Management ni qu’un Order est toujours un case.

## S33 — Camunda — Workflow patterns

[Source primaire](https://docs.camunda.io/docs/components/concepts/workflow-patterns/) — Version affichée 8.9.

Nature : documentation. Accès : Texte primaire consulté. Passage : Interrupting events / compensation.

**Constat documentaire.** Les événements peuvent interrompre un traitement en cours ; la compensation est un mécanisme distinct de gestion des effets.

**Limites.** Interrompre un processus ne garantit pas l’arrêt d’un exécutant externe. Aucun moteur ni redémarrage global imposé.

## S34 — Oracle — Order/Shipment Visibility Actions

[Source primaire](https://docs.oracle.com/en/cloud/saas/transportation/26c/otmol/execution/giv/order_shipment_visibility_results.htm) — Oracle Transportation Management 26C.

Nature : documentation. Accès : Texte primaire consulté. Passage : Events Group Shipment Actions / Track and Trace.

**Constat documentaire.** Le guide emploie Track and Trace pour consulter parcours, origine, destination, dates, arrêts et unités expédiées, dans Order/Shipment Visibility.

**Limites.** Nom de fonction et périmètre documentés ; pas une capacité native ni preuve que le produit entier équivaut à Execution Tracking.

## S35 — project44 — Enhancing Automotive Finished Vehicle Logistics with Real Time Visibility

[Source primaire](https://www.project44.com/blog/enhancing-automotive-finished-vehicle-logistics-with-real-time-visibility/) — Article éditeur ; édition logicielle non indiquée.

Nature : article éditeur. Accès : Texte primaire indexé consulté. Passage : Real-time transportation visibility / multimodal tracking.

**Constat documentaire.** Le terme Transportation Visibility accompagne localisation, progression multimodale, ETA et notifications ; exemple automobile au niveau véhicule.

**Limites.** Appui lexical et de périmètre, pas import du contexte automobile ni garantie de temps réel pour FLOW.

## S36 — FourKites — Why FourKites Is Evolving Beyond Traditional Visibility Evaluation Frameworks

[Source primaire](https://www.fourkites.ai/blogs/evolving-beyond-traditional-visibility-evaluation-frameworks) — Article du 24 février 2025.

Nature : article éditeur. Accès : Texte primaire consulté. Passage : Real-Time Transportation Visibility / scope discussion.

**Constat documentaire.** L’éditeur utilise Real-Time Transportation Visibility et distingue ce socle d’une offre élargie aux stocks et à l’orchestration.

**Limites.** Positionnement commercial ; aucune validation de ses revendications de leadership ou de création du marché. Visibility ne garantit pas partout le même périmètre.

## S37 — CSCMP — SCM Definitions and Glossary of Terms

[Source primaire](https://cscmp.org/CSCMP/Educate/SCM_Definitions_and_Glossary_of_Terms.aspx) — Page professionnelle ; édition non indiquée.

Nature : définition professionnelle. Accès : Texte primaire consulté. Passage : Definition of Logistics Management / Boundaries and Relationships.

**Constat documentaire.** La logistique recouvre les flux et le stockage ; son périmètre comprend transport, entreposage, manutention et fulfillment.

**Limites.** Définition professionnelle de Logistics Management ; ne constitue pas une norme détaillée de Logistics Visibility ni une preuve de couverture d’un produit.

## S38 — SAP — Basic Knowledge: Connecting to SAP S/4HANA

[Source primaire](https://help.sap.com/docs/business-network-global-track-and-trace/send-documents-from-erp-to-gtt/c667ee93eaa8461da2dcfc24cf53e793.html) — SAP Business Network Global Track and Trace ; édition non affichée.

Nature : documentation. Accès : Extrait primaire indexé ; ouverture sans corps exploitable. Passage : Event data / integration with S/4HANA.

**Constat documentaire.** L’intégration documente des données d’événements Goods_Issue, Packing, Picking et Load_Begin.

**Limites.** Preuve de types d’événements prévus, pas garantie de chaque granularité ni de suivi continu de toute marchandise ; ouverture sans corps, extrait officiel indexé consulté.

## S39 — Manhattan — Unified Commerce: How One Platform Powers Every Channel

[Source primaire](https://www.manh.com/our-insights/resources/articles/what-is-unified-commerce) — Article produit évolutif ; édition non indiquée.

Nature : article produit. Accès : Texte primaire consulté. Passage : Fulfillment Visibility for Store and Warehouse.

**Constat documentaire.** Le libellé Fulfillment Visibility couvre des vues de travail en magasin et entrepôt, dont les listes de picking et les files de retours.

**Limites.** Présentation produit ; exemple de périmètre, pas définition universelle ni preuve de tous les événements physiques.

## S40 — Oracle — Cross-Product Features Compatible with Back-to-Back Fulfillment

[Source primaire](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faims/cross-product-features-compatible-with-back-to-back-fulfillment.html) — Fusion Cloud SCM 26B.

Nature : documentation. Accès : Texte primaire consulté. Passage : Provide Fulfillment Visibility.

**Constat documentaire.** La visibilité de fulfillment montre les statuts d’Orders de fabrication, transfert ou achat et signale des problèmes de satisfaction de la demande.

**Limites.** Usage dans le contexte back-to-back ; démontre une portée possible au-delà du seul parcours physique, pas l’obligation pour tous les éditeurs de ce périmètre.

## S41 — GS1 — EPCIS & CBV

[Source primaire](https://www.gs1.org/standards/epcis) — Page de présentation des standards ; aucune édition normative adoptée.

Nature : présentation officielle de standard. Accès : Texte primaire indexé consulté. Passage : Introduction: visibility / status, location, movement and chain of custody.

**Constat documentaire.** EPCIS soutient le partage d’informations sur les objets, les dates, les lieux, le contexte, les mouvements et les passages de responsabilité entre partenaires.

**Limites.** Appui au besoin de continuité de visibilité ; ne prescrit pas notre hiérarchie Capacité/Comportement ni l’adoption d’un schéma EPCIS. Les ETA proviennent ici des sources marché SAP, pas de cette seule introduction.

## S42 — Microsoft — Manage Dataverse auditing

[Source primaire](https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing) — Power Platform / Dataverse ; page évolutive mise à jour le 21 avril 2026.

Nature : documentation produit. Accès : Texte primaire consulté. Passage : Introduction, supported operations et activity logging.

**Constat documentaire.** Audit des modifications de données et accès ; journalisation complémentaire pour certaines activités.

**Limites.** Activation et couverture configurées ; ne garantit pas la totalité des opérations du SI. Dataverse ne constitue pas un modèle de capacités Supply.

## S43 — Camunda — Audit log

[Source primaire](https://docs.camunda.io/docs/components/audit-log/overview/) — Camunda 8.9.

Nature : documentation produit. Accès : Texte primaire consulté. Passage : About ; Impact on secondary storage.

**Constat documentaire.** Historique des opérations sur processus, identités et tâches, avec auteur, date et entités concernées.

**Limites.** Par défaut, les opérations utilisateur sont suivies, pas les opérations client. Périmètre de produit, pas audit universel de tous les systèmes.

## S44 — SAP — Learning about the SAP EWM Solution

[Source primaire](https://learning.sap.com/courses/cloud-onboarding-for-sap-ewm-for-sap-s-4hana-cloud-private-edition-extra-stack/learning-about-the-sap-ewm-solution) — EWM for SAP S/4HANA Cloud Private Edition, extra stack ; cours sans numéro de release.

Nature : documentation produit. Accès : Texte primaire consulté. Passage : Introduction ; Goods Receipt ; Storage & Operations ; Conclusion.

**Constat documentaire.** EWM distingue les opérations entrantes, internes et sortantes : déchargement, rangement, préparation et chargement, avec suivi des unités logistiques et intégration TM.

**Limites.** Appui au périmètre sur site ; ne prescrit pas deux ou trois comportements FLOW ni un libellé canonique Warehouse Visibility.

## S45 — Oracle — Warehouse Management

[Source primaire](https://www.oracle.com/scm/logistics/warehouse-management/) — Oracle Fusion Cloud Warehouse Management ; page produit sans édition figée.

Nature : présentation produit. Accès : Texte primaire consulté. Passage : Manage complex fulfillment processes ; Consumer goods ; Third-party Logistics.

**Constat documentaire.** La présentation couvre les flux entrants et sortants, le cross-docking et les opérations sur des sites allant de l’entrepôt au magasin.

**Limites.** Présentation commerciale, pas contrat exhaustif de collecte des événements ni nomenclature de comportements métier.

## S46 — Blue Yonder — What is Blue Yonder Store Execution Inventory Management?

[Source primaire](https://info.blueyonder.com/order-management-commerce/what-is-blue-yonder-store-execution-inventory-management) — Page produit évolutive sans édition figée.

Nature : présentation produit. Accès : Texte primaire indexé consulté. Passage : Présentation et processus magasin.

**Constat documentaire.** Store Execution désigne notamment les opérations de réception et de fiabilisation du stock en magasin ; la page décrit une réception directe en rayon et le résultat de disponibilité en rayon.

**Limites.** FAQ produit évolutive sans édition ; Store Execution est attesté, mais le composé Store Execution Visibility reste notre proposition de nom de comportement.

## S47 — RELEX — Automatic replenishment system

[Source primaire](https://www.relexsolutions.com/solutions/automatic-replenishment-system/) — Page produit évolutive sans édition figée.

Nature : présentation produit. Accès : Texte primaire indexé consulté. Passage : Présentation et processus magasin.

**Constat documentaire.** La page emploie direct-to-shelf replenishment et on-shelf availability, en reliant livraisons, capacité des rayons et manutention en magasin.

**Limites.** Page commerciale évolutive sans édition ; la planification du réassort ne prouve pas le suivi de chaque mise en rayon effectivement réalisée.

## S48 — Microsoft — View Workflow Status and Run History

[Source primaire](https://learn.microsoft.com/en-us/azure/logic-apps/view-workflow-status-run-history) — Azure Logic Apps ; documentation évolutive sans édition figée.

Nature : documentation produit. Accès : Texte primaire consulté. Passage : Workflow run history ; action status and inputs/outputs.

**Constat documentaire.** Consultation des exécutions et de leurs actions, de leur statut et de leurs entrées/sorties pour suivre les traitements.

**Limites.** Suivi d’un produit configuré ; un statut technique ne définit pas le résultat métier du service.

## S49 — Microsoft — Azure Business Process Tracking overview

[Source primaire](https://learn.microsoft.com/en-us/azure/business-process-tracking/overview) — Azure Business Process Tracking ; documentation évolutive, édition non figée.

Nature : documentation produit. Accès : Texte primaire indexé consulté. Passage : Business process design and tracking ; Limitations and known issues.

**Constat documentaire.** Corrélation des étapes et de leurs propriétés métier par identifiant de transaction, par exemple commande ou case.

**Limites.** Source consultée : mapping limité aux workflows Standard stateful de Logic Apps. Ne prescrit pas un comportement universel ni une architecture FLOW.

## S50 — Camunda — Process Observability & AI Agent Monitoring

[Source primaire](https://camunda.com/platform/observability/) — Présentation produit évolutive sans version figée.

Nature : présentation produit. Accès : Texte primaire consulté. Passage : Process instances, incidents and distinction from APM/log monitoring.

**Constat documentaire.** Visibilité des instances de processus en cours, de leurs variables et incidents, reliée au contexte du processus.

**Limites.** Page commerciale : ne démontre pas la collecte exhaustive des résultats de tout service externe. Le périmètre processus est plus large qu’une prestation numérique isolée.

## S51 — SAP — Allocation Management — Business Overview

[Source primaire](https://help.sap.com/docs/CARAB/00197153997746b4bec2020d00e66ea9/e99798c39a3f4956bd5ce509b39382f7.html?locale=en-US&state=PRODUCTION&version=5.0.2) — SAP Allocation Management 5.0 FPS02, URL versionnée.

Nature : documentation produit. Accès : Texte primaire indexé consulté ; ouverture sans corps exploitable. Passage : Business Scenarios : Initial Allocation ; In-Season Fill-In.

**Constat documentaire.** Initial Allocation couvre la première distribution de nouveaux produits vers les magasins, généralement au début d’une saison, collection ou thème. In-Season Fill-In couvre le réapprovisionnement automatique après les premières ventes.

**Limites.** Pas d’équivalence automatique avec Supply Assignment FLOW ; le périmètre produit mêle décision et traitement. Les capsules FLOW sont une hypothèse utilisateur.

## S52 — RELEX — Replenishment and allocation — seasonal items

[Source primaire](https://www.relexsolutions.com/solutions/automatic-replenishment-system/) — Présentation produit évolutive sans édition figée.

Nature : présentation produit. Accès : Texte primaire consulté. Passage : Manage the full cycle for your seasonal items ; Manage seasons effectively.

**Constat documentaire.** Distingue commandes présaison, initial allocation et automatic in-season replenishment.

**Limites.** Présentation commerciale ; ne prouve ni pratiques Beaumanoir ni formule de seuil précise. Complément S47 sur un passage différent.

## S53 — SAP — Physical Inventory

[Source primaire](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/ae735d9f76024645ad4f5b1a0e6e3387.html) — 2608.

Nature : documentation. Accès : Texte primaire indexé consulté. Aucun déploiement Beaumanoir attesté ; différences de taxonomie conservées.. Passage : Physical inventory procedures.

**Constat documentaire.** Distingue inventaire périodique, procédures continues et cycle counting ; confronte quantités physiques et enregistrées.

**Limites.** Périmètre produit Warehouse Management ; aucune attribution automatique à FLOW des opérations WMS, ni obligation comptable ajoutée.

## S54 — Oracle — Counting — full physical inventory / cycle counting

[Source primaire](https://docs.oracle.com/cd/E26401_01/doc.122/e48826/T256582T257763.htm) — 12.2.

Nature : documentation. Accès : Texte primaire indexé consulté. Aucun déploiement Beaumanoir attesté ; différences de taxonomie conservées.. Passage : Counting ; Cycle Counting.

**Constat documentaire.** Oppose le comptage périodique de sélections d’articles au comptage physique complet pour rapprocher les quantités.

**Limites.** Référence EBS, pas Fusion Cloud ; les contraintes de blocage transactionnel du produit ne sont pas imposées à FLOW.

## S55 — Microsoft — Inventory reservation policies

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities) — Documentation évolutive sans édition figée.

Nature : documentation. Accès : Pas de preuve dans ce passage d’un choix automatique du jalon de vente selon le stock et la vitesse de sortie. Texte primaire indexé consulté ; ouverture directe en erreur 503. Aucune couverture Beaumanoir démontrée.. Passage : Inventory reservation policies ; Item sales reservation ; Production parameters.

**Constat documentaire.** Politiques configurées : réservation automatique à la création des lignes de commande ou manuelle ; jalon de réservation configurable en production.

**Limites.** Pas de preuve dans ce passage d’un choix automatique du jalon de vente selon le stock et la vitesse de sortie. Texte primaire indexé consulté ; ouverture directe en erreur 503.

## S56 — commercetools — Inventory modes and expiration

[Source primaire](https://docs.commercetools.com/api/inventory-overview) — Documentation évolutive sans édition figée.

Nature : documentation. Accès : Ces leviers permettent une intégration adaptative ; ils ne prouvent pas un moteur fourni qui arbitre le jalon selon le risque de pénurie. Aucune couverture Beaumanoir démontrée.. Passage : Inventory modes ; Set the default expiration ; Reserve individual Line Items.

**Constat documentaire.** Réservation au panier ou à la commande, mode par panier ou ligne ; durée configurable par défaut et par entrée de stock, changement de mode possible sur ligne existante.

**Limites.** Ces leviers permettent une intégration adaptative ; ils ne prouvent pas un moteur fourni qui arbitre le jalon selon le risque de pénurie.

## S57 — IBM — Rules-based safety stock

[Source primaire](https://www.ibm.com/docs/en/sip?topic=stock-rules-based-safety) — Documentation évolutive sans édition figée.

Nature : documentation. Accès : Mécanisme voisin de protection des quantités vendables, pas décision du jalon de réservation pour un client. Texte primaire indexé consulté ; ouverture directe indisponible. Aucune couverture Beaumanoir démontrée.. Passage : Benefits ; Network and node level safety stock ; Safety stock and total availability.

**Constat documentaire.** Règles de stock de sécurité évaluées en temps réel ; valeurs fixes ou pourcentage au niveau réseau, validité temporelle et critères de contexte.

**Limites.** Mécanisme voisin de protection des quantités vendables, pas décision du jalon de réservation pour un client. Texte primaire indexé consulté ; ouverture directe indisponible.

## S58 — SAP — Availability Change Log Events in Backorder Processing

[Source primaire](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/62d58baf16434bf1a6ad16e55e4cd0f4.html) — 2608.

Nature : documentation. Accès : Révision des confirmations, pas preuve d’une adaptation du jalon de réservation panier/paiement. Texte primaire indexé consulté ; page ouverte sans texte exploitable. Aucune couverture Beaumanoir démontrée.. Passage : Capturing Changes Caused by Backorder Processing (BOP) Run.

**Constat documentaire.** BOP réévalue la disponibilité et le réalisme des confirmations lorsque la situation de demande ou d’offre change.

**Limites.** Révision des confirmations, pas preuve d’une adaptation du jalon de réservation panier/paiement. Texte primaire indexé consulté ; page ouverte sans texte exploitable.

## S59 — Oracle — Reservation Time Fence

[Source primaire](https://docs.oracle.com/cd/E26401_01/doc.122/e48842/T373258T377249.htm) — 12.2.

Nature : documentation. Accès : Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.. Passage : Reservation Time Fence ; Reserve Orders Concurrent Program ; Reservation Modes.

**Constat documentaire.** Une fenêtre avant la date planifiée conditionne la réservation automatique. Le programme Reserve Orders peut reprendre les lignes concernées.

**Limites.** Référence EBS, pas Fusion Cloud. Les modes Fair Share/Percentage/Partial du même chapitre mêlent arbitrage des quantités et réservation ; FLOW conserve leurs frontières. Texte primaire ouvert.

## S60 — IBM — Handling inventory reservation

[Source primaire](https://www.ibm.com/docs/en/order-management?topic=2-handling-inventory-reservation) — Documentation évolutive.

Nature : documentation. Accès : Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.. Passage : Introduction ; Creating reservations.

**Constat documentaire.** La réservation peut servir des clients prioritaires ou un ordre premier arrivé, premier servi.

**Limites.** Appui à des politiques différenciées ; ne prouve pas une optimisation automatique de la durée par catégorie. Texte primaire indexé consulté.

## S61 — IBM — Reservations

[Source primaire](https://www.ibm.com/docs/en/sip?topic=data-reservations) — Documentation évolutive.

Nature : documentation. Accès : Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.. Passage : Creating reservation for node or network ; Updating reservation quantity ; Defining expiration times.

**Constat documentaire.** Réservations par site ou réseau, expiration configurable et réservation partielle documentées.

**Limites.** Options de réalisation ; le réseau est décomposé en sites selon les priorités IBM. Ne prouve pas une réservation sans affectation sous-jacente. Texte indexé consulté ; ouverture directe indisponible.

## S62 — Shopify — Shopify Checkout

[Source primaire](https://help.shopify.com/en/manual/checkout-settings) — Documentation évolutive.

Nature : documentation. Accès : Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.. Passage : Introduction, contrôle du stock au checkout.

**Constat documentaire.** Stock retenu à la soumission des informations de paiement, avec libération en cas d’échec.

**Limites.** Jalon produit spécifique, distinct de l’ouverture de page et de l’encaissement effectif ; aucun déclencheur FLOW imposé.

## S63 — SAP — Handling Requirements with Fixed Date and Quantity

[Source primaire](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/413e5cf1373142a784f6c04b2caf3fc0.html) — 2025 FPS01 (Feb 2026).

Nature : documentation. Accès : Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.. Passage : Page entière.

**Constat documentaire.** Par défaut BOP conserve les confirmations marquées Fixed Date and Quantity et leur attribue Skip.

**Limites.** Un segment peut explicitement les inclure dans le contrôle ; ne prouve pas une immutabilité absolue ni le comportement de toute API ARun.

## S64 — Microsoft — Firm planned orders

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming) — Documentation évolutive.

Nature : documentation. Accès : Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.. Passage : Introduction.

**Constat documentaire.** Affermir transforme des ordres planifiés en commandes effectives achat, transfert ou production.

**Limites.** Transition de cycle de vie, pas synonyme de fixation de toutes les données d’une commande client.

## S65 — Microsoft — Keep supply for confirmed demand

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand) — Prérequis documenté : 10.0.48 build 10.0.2645.33 ou ultérieur.

Nature : documentation. Accès : Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.. Passage : What data is preserved ; Control how on-hand inventory is pegged ; Interaction with approved planned orders.

**Constat documentaire.** Préserve une chaîne liée à une demande confirmée, notamment ordres planifiés et liens de pegging, entre les passages de planification.

**Limites.** Comportement paramétré ; la conservation du stock reçu hors positive days exige un paramètre complémentaire. Ne prouve aucun déploiement Beaumanoir.

## S66 — Microsoft — Master plans — Freeze

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans) — Documentation évolutive.

Nature : documentation. Accès : Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.. Passage : Freeze ; Firming.

**Constat documentaire.** Le gel temporel conserve les ordres planifiés dans une fenêtre.

**Limites.** Le gel empêche aussi la création de nouveaux ordres planifiés dans cette fenêtre ; différent de protéger une commande individuelle.

## S67 — SAP — Backorder Processing — Reassignment

[Source primaire](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html) — 2025 FPS01.

Nature : documentation. Accès : Documentation primaire consultée, texte indexé SAP et page Microsoft ouverte ; aucune réalisation Beaumanoir démontrée.. Passage : Reassignment ; Requirement Sorting ; Supply Selection ; Release Check.

**Constat documentaire.** Le traitement peut conserver les affectations et compléter le reliquat, ou les réexaminer. Le mode preview ne produit pas d’effets logistiques.

**Limites.** Regroupement produit de décisions et d’action ; pas preuve qu’un plan externe arbitraire est importable ou qu’une simulation est appliquée sans recontrôle.

## S68 — Oracle — Start Backlog Planning

[Source primaire](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspc/start-backlog-planning.html) — 26B.

Nature : documentation. Accès : Source primaire consultée lors de la proposition U414.. Passage : Introduction ; When to Use.

**Constat documentaire.** Prioriser et replannifier la satisfaction sur l’ensemble du carnet à partir des ressources et demandes actualisées.

**Limites.** Documentation d’un produit et de son traitement planifié, pas taxonomie de capacités ni preuve de prise en charge de tous les types d’Orders FLOW.

## S69 — Oracle — Key Actions on Orders

[Source primaire](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faubm/key-actions-on-orders.html) — 25D, édition explicitement consultée.

Nature : documentation. Accès : Source primaire consultée lors de la proposition U414.. Passage : Plan Run Actions ; Attribute Data Simulation Actions ; Release Actions.

**Constat documentaire.** Travail du carnet, priorisation, simulation puis transmission des résultats retenus à Order Management.

**Limites.** Release Planning Results transmet des résultats de planification ; ce n’est pas une équivalence exacte de l’autorisation FLOW vers les processus. La séparation demande/carnet/processus est la convention FLOW.

## S70 — Microsoft — Planned orders simplified

[Source primaire](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-orders-simplified) — Page mise à jour le 3 octobre 2025.

Nature : documentation. Accès : Source primaire consultée lors de la proposition U414.. Passage : View, manage, and firm planned orders.

**Constat documentaire.** Revue, approbation et affermissement des propositions issues de la planification ; split disponible dans la page standard.

**Limites.** Propositions d’approvisionnement, pas tous les Orders FLOW. La liste d’opérations produit ne devient pas une décomposition automatique en comportements.


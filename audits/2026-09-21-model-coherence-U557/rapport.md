# Audit du modèle hors référentiels — U557

21 septembre 2026 — Backlog, diagnostic Codex demandé par Laurent. Les recommandations ci-dessous ne sont ni appliquées ni adoptées.

## Conclusion

**La structure tient et aucune disparition accidentelle de responsabilité n’est établie dans les retraits examinés. Le modèle n’est toutefois pas complètement consolidé : cinq frontières ou intégrations restent à préciser, auxquelles s’ajoutent quatre décalages rédactionnels.**

L’audit couvre le Domain Supply Chain Orchestration, sept Areas, 41 capacités et 79 comportements. Les 22 éléments d’Authoritative Data sont exclus ; leurs dépendances sont seulement contrôlées en frontière. Les descriptions ont été relues et éprouvées sur 15 parcours. Cela constitue une revue du périmètre décrit, pas une preuve d’exhaustivité de toute la Supply Chain ni de réalisation dans les SI.

## Ce qui pourrait donner l’impression d’avoir disparu

La comparaison avec la publication courante **2026-09-19.11**, sélectionnée par son index et son descripteur, montre sept comportements retirés et deux capacités devenues comportements. Les responsabilités correspondantes ont été retrouvées :

| Évolution | Responsabilités actuelles | Conclusion |
| --- | --- | --- |
| BHV045–047 retirés ; D02.e devient un comportement | Supply Assignment applique le plan, complète les affectations et révise les liens modifiables dans Order Backlog Planning | Consolidation, pas de perte établie |
| BHV088–090 retirés ; D04.s devient un comportement | Optimization Request Management conserve les sollicitations liées aux impondérables, périodiques et explicites | Modes de sollicitation regroupés |
| BHV093 retiré | D04.s suit la demande ; D02.e constate l’application et ses écarts | Responsabilité répartie explicitement |
| D17.b retirée depuis le baseline U540 | Le planning produisant les Planned Orders reste à son origine ; les suites opérationnelles appartiennent au domaine | Retrait volontaire U555 ; interface à préciser, sans recréer le planning |
| Anciens comportements de scénario retirés depuis le 17 septembre | Évaluation et autorisation dans Inventory Optimization Planning ; analyse dans Simulation & Analysis ; application dans Inventory Plan Application | Fonctions conservées |
| Anciennes opérations sur enveloppes retirées | Création, réallocation, libération, imputation/correction et consultation dans Supply Protection | Fonctions conservées |
| Anciens regroupements de promesse et de cycle de vie | Proposition/confirmation/révision dans Fulfillment Commitment ; report dans préparation/révision, annulation dans terminaison | Responsabilités conservées |

Les sept liens de décomposition retirés suivent les sept comportements consolidés. Les deux liens métier retirés de la demande d’optimisation sont remplacés par son appartenance au Planning et par la mobilisation de Fulfillment Plan Decision depuis ce Planning. Aucun lien métier supprimé depuis cette publication ne reste sans explication dans le périmètre audité.

Les retraits plus anciens de D04.p et de Business Services sont également documentés : répartition par familles d’Orders pour le premier ; retrait explicite U472 et Commerce différé pour le second. Ils ne justifient pas une restauration.

## Points à traiter

| Priorité | Constat | Correction proposée à maille capacité |
| --- | --- | --- |
| 1 — AUD557-01 | **Planned Orders : frontière décrite dans les Areas, responsabilité de prise en charge encore insuffisamment explicite dans les capacités.** L’affermissement existe déjà dans Order Firming. | Désigner, selon la nature de la demande, qui porte la proposition avant affermissement, ses révisions et son retrait, puis sa continuité avec l’Order. Utiliser Purchase Order, Transfer Order et le cycle de vie existants ; ne pas reconstruire le plan amont. |
| 1 — AUD557-02 | **Demand Planning est isolée dans le graphe métier.** C’est la seule des 41 capacités sans relation métier, alors que son texte cite les commandes connues et les consommateurs du plan. | Qualifier les relations avec Sales Order et les Plannings consommateurs, dont Inventory Optimization Planning. Les textes seuls ne remplacent pas ces relations explicites. |
| 1 — AUD557-03 | **Le porteur de la mise en vigueur des politiques de réservation reste à arbitrer.** La décision des conditions et la réservation sont présentes. | Attribuer cette responsabilité de management à une capacité existante, extérieure aux Plannings. Le modèle ne permet pas encore de désigner son propriétaire sans arbitrage. |
| 2 — AUD557-04 | **PTP, Delivery Schedule Decision et Fulfillment Plan Decision doivent produire des résultats compatibles, mais leur partage précis d’autorité reste ouvert.** | Préciser leurs résultats respectifs et le réexamen en cas d’incompatibilité, en s’appuyant sur la cohérence collective déjà portée par Fulfillment Plan Decision. Aucun algorithme ou ordre de calcul universel à imposer. |
| 2 — AUD557-05 | **Supply Assignment cible les commandes tout en conservant une réserve historique sur les besoins prévisionnels.** | Arbitrer le traitement des besoins sans commande : demande gérée, protection ou autre responsabilité selon leur sens. Le changement de parent n’a pas résolu cette frontière. |
| 3 — AUD557-06 | **Des formulations anciennes subsistent.** | Actualiser le lien Planning → Supply Planning dans le Domain ; le compte de capacités dans D03 ; la mention autonome Supply Reassignment dans BHV077 ; les verbes de réalisation conservés dans un passage de Stock Redistribution Decision. |

Les points 3 à 5 sont des réserves explicites déjà présentes, pas des fonctions récemment perdues. Le point 2 révèle une intégration inachevée de la nouvelle capacité. Le point 1 concerne la précision des responsabilités après le retrait volontaire U555.

## Ce que les références marché permettent de conclure

Les rapprochements détaillés, versions, passages et limites sont conservés dans [l’annexe YAML](../../modeles/backlog/model-coherence-audit-U557.yaml), correspondance CMP231. Dix documents primaires ont été consultés pour ces recommandations ciblées.

- **Passage du plan aux Orders :** [Microsoft — Firm planned orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming) et [Oracle — Manually Release Plan Recommendations](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faupc/manually-release-plan-recommendations.html) appuient la distinction entre propositions de plan et suites gérées. Le vocabulaire produit ne remplace pas les frontières FLOW entre affermissement, lancement et engagement.
- **Plan de demande et consommateurs :** [Oracle — Publish Plan](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspc/publish-plan-data.html) et [Demand Schedules](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspf/supply-plan-options-for-organizations-and-schedules.html) documentent publication et consommation. L’export technique ne prouve pas à lui seul une autorisation métier. Deux documents Oracle ne constituent pas un consensus interéditeurs.
- **Politique et réservation :** [commercetools — Inventory overview](https://docs.commercetools.com/api/inventory-overview) et [Microsoft — Reserve inventory quantities](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities) distinguent paramètres applicables et réservations. Ils ne désignent pas le propriétaire de cette gouvernance dans FLOW.
- **Décisions de satisfaction :** [Oracle — Alternative Fulfillment Scenarios](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26c/fascp/create-alternative-fulfillment-scenarios-to-reduce-cost.html) et [Microsoft — DOM](https://learn.microsoft.com/en-us/dynamics365/commerce/dom) combinent plusieurs dimensions de satisfaction. Leur découpage produit ne tranche pas l’autorité entre les capacités FLOW ; la priorité Oracle au délai n’est pas une pondération FLOW adoptée.
- **Affectation et carnet :** [SAP — Explaining Supply Assignment](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4) et [Oracle — Backlog Management Processes](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faubm/overview-of-backlog-management-processes.html) étayent le travail sur les commandes. Cela ne démontre pas une responsabilité d’affectation à des forecasts sans Order.

Aucune nouvelle capacité n’est recommandée à ce stade. Les corrections proposées reposent sur la cohérence du modèle et sur ces recouvrements fonctionnels partiels ; aucune innovation ni taxonomie universelle n’est revendiquée.

## Couverture et contrôles

Les 15 parcours documentés dans l’annexe couvrent : demandes planifiées ; réception et correction du stock ; promesse partielle ; carnet sous pénurie ; impondérables ; report/annulation ; implantation et réassort ; redistribution ; prévisions et précommandes ; retours clients ; retours fournisseurs ; consignation ; prestations ; structuration et archivage ; politiques de réservation.

Les responsabilités principales sont présentes. Les interfaces financières et commerciales restent à leurs frontières ; aucune absence d’un ERP complet n’est transformée en manque de l’orchestration. Les détails futurs de réservation, de capacités de service et d’application des plans conservés par la clôture U431 ne sont pas réouverts comme un nouvel audit des comportements.

Les [contrôles structurels](structural-checks.yaml) établissent : aucun parent manquant ou multiple pour les capacités/comportements, aucun cycle de décomposition, aucun sous-comportement et aucune extrémité de relation absente. Les 16 décisions restent présentes ; depuis U540, seuls deux libellés de lien vers Inventory Optimization Planning ont changé dans leurs fiches.

La [baseline](baseline.yaml) conserve les valeurs examinées et l’empreinte du modèle. La [validation finale](validation.json) conserve le résultat du validateur du projet. Le modèle audité et les publications restent inchangés par cette intervention. L’audit U431 n’est pas relancé ; aucun build, changement serveur ou release n’est nécessaire.

La prochaine étape proposée est de traiter les trois premiers points, d’arbitrer les deux frontières restantes et de nettoyer les descriptions dans le même lot. Cette proposition ne vaut pas accord sur les modifications.

## Complément demandé sur les inspirations — U558

Le [contrôle des inspirations](inspirations-U558.md) distingue conservation des références et qualité de leur restitution. Les 128 fiches ont au moins deux documents, mais certains appuis et exemples propres aux comportements retirés n’ont pas été reportés sur leurs successeurs. Deux nouveaux comportements n’ont pas encore de synthèse illustrée ; l’attribution des approches dans Demand Planning et quelques répétitions sont à corriger. Les preuves historiques sont conservées. Ces quatre constats documentaires complètent les six constats métier et rédactionnels ci-dessus.

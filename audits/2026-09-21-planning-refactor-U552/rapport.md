# Refacto des Plannings — U552 à U556

Le backlog applique les principes discutés : Planning porte son application, mobilise des décisions distinctes et consomme une configuration gérée à l’extérieur. Une demande propre à son travail peut être un comportement ; les Orders gardent leurs responsabilités de gestion, même lorsqu’ils naissent dans le Domain.

## Résultat

| Capacité / Area | Structure courante |
| --- | --- |
| Order Backlog Planning | Optimization Request Management ; Simulation & Analysis ; Scenario Authorization ; Supply Assignment |
| Inventory Optimization Planning | Scenario Construction ; Simulation & Analysis ; Scenario Execution Adaptation ; Inventory Plan Application |
| Supply Planning, Area D17 | Demand Planning ; capacité de couverture dupliquée D17.b retirée U555 |
| Demand Planning | Demand Plan Publication explicite la demande rendue applicable aux consommateurs |

D04.s conserve son identifiant et devient le comportement de gestion de demande. Les sollicitations après impondérable, périodiques ou volontaires sont des modalités décrites ; BHV088–090 ne restent pas des sous-comportements. BHV093 est consolidé : les faits d’application relèvent de Supply Assignment, le suivi et la conclusion du travail demandé d’Optimization Request Management. Les définitions, preuves et identifiants antérieurs sont préservés dans la [baseline](baseline.yaml) ; aucun identifiant retiré réutilisé.

L’origine Backoffice reste explicite dans le périmètre de D04.s. Le champ technique request_origins est réservé aux capacités dans le contrat actuel ; il n’a pas été transféré artificiellement à tout le Planning. Les deux relations redondantes vers Planning et sa décision sont remplacées par la décomposition et la coopération existante du Planning avec Fulfillment Plan Decision. Le lien vers Supply Assignment porte désormais les faits utiles au suivi.

Service Requests garde ses familles d’Orders et leurs origines applicables. La demande d’optimisation est gérée dans le Planning. L’autorisation d’un scénario ne remplace pas Order Release ; l’affectation ne devient ni réservation ni promesse. Les décisions et Supply Protection gardent leurs parents. Le catalogue Information n’est pas étendu.

## Accord et limites

U552 autorise le refacto ; il n’approuve pas automatiquement tous les noms, descriptions et nouvelles décompositions. U553 adopte précisément Supply Planning comme nom de l’Area D17 : [état antérieur](area-before-U553.yaml). Les formulations de mise en œuvre restent qualifiées dans le backlog. Les définitions de redistribution adoptées U551 restent intactes.

U554 demandait la suppression de D17.b si son périmètre était repris, sinon sa mise en attente. U555 précise que le planning amont produit déjà les Planned Orders et est pris en charge : D17.b et son lien de décomposition sont retirés pour éviter sa duplication. [État antérieur](coverage-before-removal-U555.yaml). La prise en charge des demandes issues du plan demeure distincte de sa construction. Aucun nouveau planning, conversion automatique en commande ferme ou contrat d’interface ajouté.

U556 fait porter cette frontière par les descriptions de Supply Planning, Service Requests, Fulfillment Optimization et Inventory Optimization, sans nom de solution. Les demandes planifiées alimentent les gestions et adaptations opérationnelles ; elles ne justifient pas la reconstruction de leur plan d’origine. Demand Planning et les Plannings opérationnels restent présents. Les [descriptions antérieures](area-descriptions-before-U556.yaml) sont conservées.

## Marché et preuves

[Oracle Backlog Management](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faubm/overview-of-backlog-management-processes.html) et [Key Actions on Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faubm/key-actions-on-orders.html) distinguent scénarios, simulation et transmission des résultats. [Salesforce](https://trailhead.salesforce.com/content/learn/modules/request-management-for-agentforce-it-service/explore-service-requests-and-resolutions) illustre qualification et suivi d’une demande IT ; ce n’est pas une taxonomie Supply.

Les sources Oracle de [release manuelle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faupc/manually-release-plan-recommendations.html) et [automatique](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fausp/automatic-release-options.html) étayent l’application du plan de stock. [Publish Plan](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspc/publish-plan-data.html) décrit un export ; [Demand Schedules](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspf/supply-plan-options-for-organizations-and-schedules.html) montre la consommation d’une demande. La mise en vigueur métier FLOW reste une adaptation explicite, pas la reproduction d’une interface technique.

[Oracle Plan Types](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faupc/overview-of-supply-chain-planning-plan-types.html) et [SAP Response and supply planning](https://www.sap.com/sea/products/scm/integrated-business-planning/features/response-and-supply-planning.html) éclairent les responsabilités articulées par l’Area. Supply Planning est le nom de l’Area FLOW retenu U553 ; son périmètre courant conserve Demand Planning sans reproduire le planning amont producteur des Planned Orders. Il ne correspond pas à l’intégralité des modules Supply homonymes des éditeurs. Aucun consensus de hiérarchie ou innovation revendiqué.

Les comparaisons et limites sont portées dans les fiches concernées et [le manifest](../../modeles/backlog/planning-refactor-U552.yaml), CMP229/CMP230. Aucun déploiement Beaumanoir inféré, aucune publication Atlas réalisée.


## Vérification

Validation du modèle sans erreur et 28 tests des comportements et comparaisons marché réussis. Le contrôle différentiel confirme les 16 décisions inchangées, les gestions partenaires préservées, un parent Capability pour chaque Behavior, aucun lien vers un élément retiré et le nom Supply Planning réservé à l’Area. Détail : [contrôle d’intégrité](integrity.yaml). Restitution du backlog actualisée ; aucune publication Atlas.

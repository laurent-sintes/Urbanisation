# Master Planning — proposition U568–U570

L’Area Master Planning construirait et actualiserait un plan Supply commun : satisfaire commandes et prévisions, ajuster les apports et les stocks, confronter les variantes aux protections et engagements, puis faire appliquer les suites retenues.

Le nom Master Planning est établi chez Microsoft, avec un périmètre qui dépasse la seule production. Son exemple Contoso Retailer associe prévisions, achats planifiés et réassort des magasins. SAP IBP étaye le périmètre intégré, avec un autre vocabulaire. Employer ce nom pour une Area FLOW reste un choix de modèle, sans consensus universel revendiqué.

Je recommande une capacité de gestion du plan commun, proposée sous le nom **Master Plan Management**, plutôt qu’une capacité distincte pour chaque action de simulation, validation ou lancement. Son service serait : construire, comparer, retenir, actualiser et faire appliquer le plan Supply commun en mobilisant les décisions spécialisées et en suivant les résultats réellement pris en compte.

| Responsabilité | Décomposition proposée | Éléments actuels à consolider |
| --- | --- | --- |
| Qualifier le travail et lancer ou relancer l’étude | Optimization Request Management | D04.s ; conserver les déclenchements volontaires, périodiques et liés aux impondérables. |
| Construire, simuler et analyser les options | Simulation & Analysis | BHV005, BHV006, BHV091 : conserver génération des scénarios, hypothèses, comparaison et possibilité de ne rien appliquer. |
| Retenir le scénario et autoriser ses suites | Scenario Authorization | BHV092 : autorisation humaine ou déléguée, distincte du calcul. |
| Appliquer les affectations ressources-besoins | Supply Assignment | D02.e, avec sa distinction d’avec Reservation. |
| Faire appliquer les ajustements d’apports, de stocks et les modifications autorisées | Supply Adjustment Application, nom proposé | BHV094 : achats, transferts et politiques sont pris en charge par leurs responsables. |

Le bénéfice d’adaptation aux écarts de BHV016 doit être repris explicitement dans l’actualisation du plan et son suivi ; il ne disparaît pas avec le regroupement. Les comportements restent terminaux, sans sous-comportements ni parcours rigide.

« Démarrer » désigne ici lancer le travail de planification ou appliquer le scénario autorisé selon le contexte. Le démarrage physique des prestations reste porté par la prise en charge des Orders et Process Management.

Order Backlog Planning et Inventory Optimization Planning cesseraient de produire des plans finaux autonomes. Le carnet, le stock, les apports et les protections deviendraient des angles d’étude et des contributions au même plan retenu. Les calculs spécialisés restent identifiables ; le nom d’un traitement logiciel ne crée pas automatiquement une capacité.

Exemples de contributions : CTP explore une couverture supplémentaire ; Group Protection Decision propose les quantités à protéger ; Inventory Target Decision détermine les cibles ; Replenishment Decision et Stock Redistribution Decision proposent les ajustements. La décision de cohérence d’ensemble aujourd’hui portée par Fulfillment Plan Decision devra être élargie et éventuellement renommée. Proposer une baisse ou une annulation d’achat reste distinct de modifier l’Order et ses engagements.

Demand Planning prépare la demande qui alimente le plan Supply. Sa prévision n’est pas un second plan concurrent d’affectation ou d’approvisionnement. Sa responsabilité est conservée ; son placement précis peut être confirmé avec la structure de l’Area.

U571 demande une recommandation plutôt qu’un choix immédiat. La recommandation Codex est de regrouper dans Master Planning les décisions dont le résultat détermine le contenu du plan Supply : affectations, priorités du plan, réassorts, transferts, propositions de cibles ou de protections. Les faisabilités réutilisables comme ATP/CTP peuvent rester dans leur responsabilité propre ; la configuration et la tenue effective des Orders restent distinctes. La cohérence d’ensemble doit appartenir à Master Planning. Aucun renommage ou déplacement du catalogue n’est appliqué par cette proposition.

Ce regroupement suit le résultat métier : les recommandations qui engagent ensemble les mêmes ressources appartiennent à la construction du plan. Leur calcul peut rester spécialisé et être sollicité depuis d’autres capacités. Proposer de protéger 150 pièces est une décision contributrice ; maintenir et mettre en vigueur la politique qui impose cette protection relève de Supply Protection. Le plan ne remplace pas la politique en cours par sa seule existence.

Le marché étaye un regroupement de ces arbitrages dans un périmètre de planification : Microsoft présente achats, stock et réassort dans Master Planning ; SAP IBP choisit conjointement production, achats, distribution et stock. Ces produits ne définissent pas notre hiérarchie de capacités et regroupent parfois des fonctions que FLOW distingue. Le rattachement des décisions reste donc une recommandation FLOW étayée, et non une taxonomie copiée des éditeurs.

Cette option conduit à réexaminer les Areas Fulfillment Optimization et Inventory Optimization après transfert de leurs responsabilités de planification. Leur maintien ou leur suppression dépendra des responsabilités autonomes restantes : ne pas conserver des Areas vides ou un second propriétaire du même résultat. Les responsabilités non contributrices, notamment disposition des retours et politique de réservation, demandent un examen ciblé de placement avant migration.

Appuis : [Microsoft Master plans](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans), [Microsoft Contoso Retailer](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-planning-setup-wizard), [SAP IBP optimisation intégrée](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/c1fb60cb1e9c49d99ada277ae57e9e6c/deb28978d5ba4c64bad78edcab913228.html), [Oracle étude, simulation et transmission du backlog](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faubm/overview-of-backlog-management-processes.html), [Microsoft propositions d’évolution des Orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages), [Business Central création, révision et annulation proposées](https://learn.microsoft.com/en-us/dynamics365/business-central/design-details-central-concepts-of-the-planning-system). Ces fonctions étayent les responsabilités ; la capacité Master Plan Management et ses comportements sont une proposition FLOW.


**Accord U572 :** le regroupement de principe recommandé est validé. Les noms détaillés, la liste exacte des transferts et la filiation des comportements ci-dessus restent des propositions à formaliser ; aucune fusion n’a encore été appliquée au catalogue canonique.

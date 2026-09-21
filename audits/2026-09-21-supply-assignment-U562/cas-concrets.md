# Cas concrets et responsabilités — U562–U565

Exemples fictifs pour qualifier la cible FLOW ; aucune réalisation installée déduite.

| Cas | Résultat recherché | Couverture dans FLOW |
| --- | --- | --- |
| Prévoir 1 000 ventes web en novembre à partir des ventes et précommandes. | Un plan de demande actualisé. | Demand Planning construit la demande attendue. |
| Protéger une enveloppe de 300 pièces pour le web sans désigner un arrivage. | Des conditions d’accès aux ressources pour un groupe. | Group Protection Decision détermine la protection. ; Supply Protection configure et maintient la politique applicable. |
| Affecter 300 pièces de l’arrivage A aux ventes web prévues en novembre, sans commande. | Un lien entre une ressource et un besoin prévisionnel identifié. | Le Planning commun prépare et suit les scénarios commandes-prévisions. ; Fulfillment Plan Decision détermine le scénario avec les décisions spécialisées. ; Supply Assignment applique les affectations. |
| Deux commandes demandent 100 et 200 pièces ; seules 150 sont disponibles. | Un scénario retenu, puis des liens d’affectation appliqués. | Order Backlog Planning construit et suit les scénarios. ; Fulfillment Plan Decision choisit le scénario avec les décisions spécialisées. ; Supply Assignment applique les affectations. |
| Réapprovisionner un magasin avec 40 pièces pour éviter une rupture. | Un ajustement de stock retenu puis pris en charge. | Inventory Optimization Planning prépare et applique le plan. ; Replenishment Decision détermine le réassort. ; Inventory Plan Application applique les suites avec les capacités partenaires. |
| Déplacer 40 pièces d’un magasin surstocké vers un autre qui en manque. | Un plan de redistribution retenu puis pris en charge. | Inventory Optimization Planning porte le plan. ; Stock Redistribution Decision détermine les transferts. ; Inventory Plan Application applique les suites avec les capacités partenaires. |
| Empêcher que 40 pièces engagées pour un besoin soient consommées par un autre. | Un engagement dont les usages concurrents doivent tenir compte. | Reservation établit cet engagement. |
| 500 pièces attendues doivent couvrir 300 commandées et 300 ventes prévisionnelles restantes en plus des commandes. | Un plan commun arbitre les affectations et explicite les 100 pièces non couvertes. | Le Planning commun prépare et suit les scénarios commandes-prévisions. ; Fulfillment Plan Decision détermine le scénario avec les décisions spécialisées. ; Supply Assignment applique les affectations. |

U562 confirme l’application du cas avant commande par Supply Assignment ; U565 confirme un même Planning pour les commandes et les prévisions. Le périmètre de D03.p est étendu avec sa décision du plan et ses comportements. Le nom Order Backlog Planning reste à revoir ; la frontière de couverture amont U555 est conservée.

Dans le cas 8, les 300 ventes prévisionnelles sont encore attendues en plus des commandes connues. La prévision totale ne doit pas être additionnée aux commandes qu’elle comprend déjà. Aucun quota, ratio ou ordre de priorité n’est adopté.

[Comparaison Microsoft](comparaison-microsoft.md) ; [détail et provenance structurés](../../modeles/backlog/supply-assignment-cases-U562.yaml).

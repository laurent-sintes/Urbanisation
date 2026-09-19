# Optimisation analytique et application du stock — comparaison U225

15 septembre 2026, Codex. Demande U225 après la clarification U224. Cible : orientation analytique D05 et application opérationnelle des paramètres/ajustements, dans l'annexe `modeles/backlog/stock-order-boundary.yaml`. Le modèle actif n'est pas encore refondu selon cette orientation. Définition D05 U223 conservée. Aucune adoption ni publication par cette étude.

## Conclusion

La séparation proposée est étayée par des comportements documentés chez Microsoft et SAP : produire des valeurs recommandées ou un plan est distinct de leur mise en application. Cela n'impose ni outil séparé, ni validation humaine, ni exécution différée. Notre D05 serait un domaine d'analyse prescriptive : il produit des résultats utilisables, au-delà d'indicateurs.

Le découpage précis des produits ne reproduit pas nos domaines. Chez SAP, la protection intervient dans aATP ; chez Microsoft, certaines fonctions opérationnelles sont dans Inventory Visibility et d'autres dans Master planning. Ces répartitions ne valident ni le rattachement local D01/D03/D05, ni une interface prête à l'emploi entre tous les modules cités.

## Constats externes, reformulés

| Élément | Ce que montre le passage consulté | Lecture pour notre modèle |
| --- | --- | --- |
| ELM122 — Microsoft Buffer profile and levels | Les minimums, maximums et points de commande sont recalculables. Une option permet d'appliquer automatiquement les résultats ou de les laisser sans effet jusqu'à leur acceptation. | Distinction explicite valeur calculée / valeur active. Ce calcul de buffers ne prouve pas l'optimisation des allocations de canaux. |
| ELM123 — Microsoft Firm planned orders | L'affermissement transforme les ordres planifiés en commandes d'achat, de transfert ou de production. Il peut être manuel ou automatisé suivant des règles. | Distinction proposition / Order opérationnel ; ne pas assimiler les objets natifs Microsoft à notre modèle d'Orders universellement. |
| ELM124 — Microsoft Inventory Visibility inventory allocation | Des quantités peuvent être affectées à des canaux ou groupes avant les ventes, protégées des autres usages et suivies en consommation. Cette allocation se distingue de la réservation liée à une vente. | Appui concret à Stock Protection ; la fonction n'établit pas à elle seule le calcul du meilleur quota. |
| ELM125 — SAP Integrated Planning Process | L'exemple IBP produit des cibles de stock qui alimentent la planification sous contraintes. Plusieurs étapes de planification sont distinguées. | Le marché ajoute une élaboration de plan entre objectifs et exécution. Les cadences de l'exemple et son S&OP ne sont pas des obligations locales ; aucune intégration externe standard démontrée par cet exemple. |
| ELM126 — SAP Supply Protection / Product Allocation | SAP distingue minimum protégé pour un groupe et plafond de quantité autorisée. Supply Protection est pris en compte lors du contrôle de disponibilité et peut réduire la quantité confirmable. | Appui partiel à D02.b et à la consommation des règles par D03. Minimum protégé, plafond d'allocation et seuil de réassort ont des effets distincts. |
| ELM127 — TM Forum SID StockLocation / StockItemRequestReplenishment | Les illustrations historiques décrivent un seuil local conduisant à une demande de réapprovisionnement, puis des possibilités de regroupement pour l'expédition. | Appui au côté application, plus concret que les seuls attributs TMF687. Aucun calcul optimal du seuil ni domaine analytique attesté par ces illustrations. |

## Correspondances proposées

Auteur : Codex, date : 2026-09-15. Statut de toutes les correspondances : proposé, sans valideur ni date de validation. Sources officielles dans le tableau suivant. Aucun contexte SI Beaumanoir évalué.

- **CMP072 — D05 / direction U224 :** appui méthodologique ELM122/ELM125 à la séparation recommandation et mise en application. Les trois noms analytiques de l'annexe restent des propositions locales ; les résultats des produits ne démontrent pas la même granularité de capacités.
- **CMP073 — D02.b / Stock Protection cité U224 :** recouvrement partiel ELM124/ELM126. Allocation par groupe étayée ; l'assimilation de tous les seuils de réassort à la protection ne l'est pas. Proposition : documenter chaque règle par son effet, sans imposer immédiatement une scission en plusieurs capacités. L'intégration aATP SAP appelle un contrat avec D03, pas un déplacement automatique de D02.b.
- **CMP074 — application opérationnelle U224, D04 et exécutants :** appui fonctionnel ELM123 et sémantique ELM127. Une demande calculée, un Order créé et un déplacement réalisé restent distingués. Le porteur exact du déclenchement du réassort dans notre modèle n'est pas tranché ; aucune nouvelle capacité ni relation créée.

## Conséquences proposées pour FLOW

Deux familles de résultats aideraient à rendre D05 concret :

1. **Paramètres recommandés** : objectifs, seuils, quotas/protections, associés au produit, lieu ou canal, à une période et aux hypothèses du calcul.
2. **Actions recommandées** : compléments ou transferts, avec quantités, dates et motifs.

Leur application met les paramètres en vigueur ou engage les Orders correspondants. Elle peut être automatique. La mesure des résultats et des écarts fournit ensuite les entrées de l'optimisation suivante. Cette boucle est une proposition locale, pas un processus universel de marché adopté.

Il faut préserver trois sens dans les descriptions : protéger 100 unités pour un canal ; limiter ce canal à 200 unités ; réapprovisionner un magasin quand sa position pertinente passe sous 40. Ces exemples fictifs sont des règles différentes, même si une politique de stock commune les calcule. Un minimum déclencheur ne signifie pas nécessairement que les unités restantes sont interdites à la vente.

Je réexaminerais les capacités selon les résultats analytiques recherchés avant de confirmer les libellés U224. Net Requirements Calculation peut être un calcul mobilisé plutôt qu'une capacité du même niveau. Le lancement effectif du réapprovisionnement doit être décrit dans l'application opérationnelle. Replenishment Optimization et Stock Redistribution Optimization doivent coordonner leurs résultats pour ne pas satisfaire deux fois le même manque.

## Sources et limites

Toutes les sources ont été consultées le 2026-09-15. Microsoft : documentation évolutive Dynamics 365 SCM, pas catalogue de capacités. SAP : versions précisées ci-dessous, pas SAP RBA. TM Forum : modèle d'information SID historique, pas version courante déduite. Synthèses sélectives et liens uniquement ; droits de redistribution intégrale non établis. La page indexée est distinguée de la lecture du document complet.

| Source | Référence / élément / localisateur | Accès réel |
| --- | --- | --- |
| [Buffer profile and levels](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/ddmrp-buffer-profile-and-levels) | MKT14, ELM122 ; Dynamic adjustments et Schedule automatic buffer value calculations ; édition produit précise non indiquée | Corps public lu, notamment l'option d'acceptation des valeurs. |
| [Firm planned orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming) | MKT14, ELM123 ; introduction et Auto-firm planned orders ; page mise à jour 25 mars 2026 | Corps public lu. |
| [Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation) | MKT14, ELM124 ; Business background and purpose, Allocation definition ; édition précise non indiquée | Texte détaillé indexé lu. |
| [Example: Integrated Planning Process with Unified Planning Area](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/bea60e563f3e787fe10000000a441470.html) | MKT24, ELM125 ; Inventory Optimization et Supply Review ; IBP 2605, exemple SAPIBP1 | Texte indexé lu ; pas de test produit. |
| [Using Supply Protection and Product Allocation](https://help.sap.com/docs/PRODUCT_ID/32da8359c8ee4e8b8e8c5e15cacba5aa/e9861099432c4fd9a569f129f2d4ceb1.html?locale=en-US&state=PRODUCTION&version=LATEST) | MKT13, ELM126 ; texte de comparaison ; Supply Chain 2602 affiché | Texte indexé lu ; URL évolutive, version conservée ici. |
| [Integration into Other Processes](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/e541e617043545a0bb60e5067d037046.html) | MKT13, ELM126 ; Product Availability Check et Product Allocation ; S/4HANA 2025 FPS01 (février 2026) | Texte indexé lu ; ouverture directe sans corps exploitable. |
| [StockLocation](https://www.tmforum.org/Browsable_HTML_SID_v22.0/html/EARoot/EA2/EA5/EA13/EA1/EA2269.htm) et [StockItemRequestReplenishment](https://www.tmforum.org/Browsable_HTML_SID_v22.0/html/EARoot/EA2/EA5/EA13/EA1/EA2299.htm) | MKT19, ELM127 ; légendes des figures SI.02-I01 et SI.04-I03 ; SID v22.0, mai 2022 | Légendes indexées lues ; ouvertures directes 403/cache miss. Diagrammes graphiques non inspectés : aucune relation détaillée inférée de leur dessin. |

Les fonctions relevées confirment une séparation de responsabilités, pas un découpage identique de produits, de domaines ou d'équipes. La release et les nœuds du backlog sont inchangés par cette étude.


## Retour de Laurent U226 — 16 septembre 2026

Microsoft devient la référence préférée pour le découpage et les noms. La distinction SAP entre planification et mise en action est retenue comme orientation. La décomposition analytique de Stock Protection est conditionnée à une décomposition correspondante de ses capacités opérationnelles ; distinguer des effets de règles ne suffit pas à créer une capacité par paramètre. Les trois noms analytiques proposés auparavant restent à réexaminer, sans adoption automatique de tout le catalogue Microsoft. Aucun nouveau contrôle externe ni modification des nœuds lors de ce retour.


## Application U235 — 16 septembre 2026

Le découpage local à cinq capacités est appliqué au backlog : D05.a Coverage Target Decision, D05.d Stock Allocation Decision, D05.e Replenishment Decision, D05.c Stock Redistribution Decision, D05.f Inventory Planning. D05.b est retirée, son calcul net intégré à D05.e. Portées adoptées et limites de comparaison dans [le registre de refonte](../modeles/backlog/d05-refactoring.yaml).

Contrôle documentaire ciblé du 16 septembre : sections Calculate and apply buffer values / Schedule automatic buffer value calculations de [Buffer profile and levels](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/ddmrp-buffer-profile-and-levels), Business background / Allocation definition d'[Inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), Net flow and qualified demand de [Demand-driven planning](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/ddmrp-planning). Textes indexés des pages officielles lus, documentation évolutive Dynamics 365 SCM ; version logicielle unique non indiquée. Le dernier passage relie position nette, demande qualifiée et quantité d’ordre planifié. Appui fonctionnel partiel à D05.e ; aucune méthode ou formule obligatoire importée. ELM122/ELM124 conservent leur sens, nouvelle source ELM128.

Les noms et le rang de capacités restent locaux. Les allocations opérationnelles ne prouvent pas un optimiseur de quotas. Le sens complet de Planning et la redistribution des excédents ne sont pas déclarés équivalents à un catalogue Microsoft/SAP. Aucune comparaison de déploiement SI ni nouvelle lecture exhaustive des catalogues SAP/TM Forum lors de cette application.

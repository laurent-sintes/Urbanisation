# Inventory Optimization — découpage U235

16 septembre 2026. Vue de lecture du [backlog YAML](../modeles/backlog/model.yaml). Noms, définitions courtes et rattachements adoptés U235 ; finalités, natures, descriptions détaillées et exemples restent proposés. Publication v005 inchangée.

Optimiser le stock consiste à choisir un compromis entre disponibilité, immobilisation et risque, puis à décider des ajustements nécessaires.

## Périmètre

Le domaine produit les paramètres et ajustements de stock à retenir selon le compromis entre disponibilité, immobilisation et risque. Quatre décisions spécialisées portent respectivement les cibles de couverture, les allocations aux groupes, les apports de réapprovisionnement et la redistribution du stock existant. [Inventory Planning](../modeles/backlog/model.yaml) les mobilise pour reconfigurer, simuler et valider un scénario cohérent ; cette mobilisation n’est pas une décomposition en sous-capacités.

Les calculs font partie des décisions. [Replenishment Decision](../modeles/backlog/model.yaml) intègre notamment les besoins nets, les contraintes, les quantités et dates à retenir. La redistribution et le réapprovisionnement demeurent distincts et coordonnés : leurs effets sur les stocks et manques sont pris en compte sans doublon. Les horizons restent opérationnels ; les prévisions et coûts peuvent être des entrées sans ajouter la planification de saison.

Exemple fictif : retenir une cible magasin de 100 pièces et un seuil de réassort de 60 ; allouer une quantité à un canal ; puis arbitrer entre apports et transfert depuis un site excédentaire. Une reconfiguration du service attendu peut conduire Inventory Planning à mobiliser de nouveau plusieurs décisions et comparer leurs effets ensemble.

Stock Protection désigne la gouvernance/management discutée en U230/U231 ; la capacité courante reste [Supply Protection](../modeles/backlog/model.yaml), sans renommage implicite. Son application signifie mettre à jour transactionnellement les données correspondantes, à l’unité, par groupe ou en masse, par écrans, batch, flux ou streaming. Décider les paramètres ou valider un scénario ne réalise pas ces mises à jour à lui seul.

La mise en action du réapprovisionnement engage les Orders ; [Order Management](../modeles/backlog/model.yaml) les gère, [Order Promising](../modeles/backlog/model.yaml) travaille leur satisfaction, les exécutants réalisent les prestations et [Inventory Management](../modeles/backlog/model.yaml) tient la connaissance des stocks et mouvements. Le déclenchement effectif n’est pas une capacité ajoutée dans D05. D03 cherche à satisfaire les Orders ; D05 cherche le stock souhaitable et ses ajustements. La distinction ne repose ni sur l’absence de commandes dans les entrées ni sur un partage global/individuel. La portée actuelle de Supply Assignment, incluant les besoins prévisionnels, est conservée.

La mise en application peut être automatique selon les règles et autorités ; aucun contrôle humain systématique, séquencement fixe ou découpage logiciel imposé. Les notions transversales soutenant la définition des objets du modèle restent dans le glossaire de modélisation séparé.

## D05.a — Coverage Target Decision

**Définition adoptée :** Déterminer les niveaux de stock souhaitables et les seuils à retenir : couverture, sécurité, déclenchement du réassort, par produit, lieu et horizon.

**Finalité proposée :** Définir les niveaux de stock auxquels comparer la situation connue ou attendue selon le compromis de service, immobilisation et risque.

Déterminer et réviser les niveaux à viser selon le produit, le lieu, l’horizon, les besoins, les délais et leurs incertitudes. Les objectifs de service, le coût du stock et les risques alimentent les arbitrages ; les formules et seuils détaillés restent à préciser. Les calculs nécessaires font partie de la décision.

Exemple fictif : retenir un minimum de 40 pièces, un seuil de réassort de 60 et une cible de 100 pour un magasin. Ces nombres illustrent des effets différents et ne constituent pas une règle adoptée. Le seuil déclencheur ne signifie pas que les pièces restantes sont interdites à la vente.

Cette décision détermine les paramètres à retenir ; la gestion de leur validité et leur mise à jour transactionnelle relèvent du management opérationnel. Elle ne réserve pas le stock à un Order, ne promet pas une fourniture et ne déclenche pas à elle seule un réassort. [Inventory Planning](../modeles/backlog/model.yaml) peut la mobiliser à nouveau avec d’autres hypothèses.

## D05.d — Stock Allocation Decision

**Définition adoptée :** Déterminer les quantités à protéger ou les limites d’usage par canal ou groupe de bénéficiaires.

**Finalité proposée :** Déterminer la répartition des droits d’usage du stock entre groupes, en préservant les usages retenus.

Déterminer les quantités protégées ou les limites d’usage pour des canaux, régions ou groupes de bénéficiaires, avec le périmètre et la période pertinents. Une protection minimale et un plafond de consommation ont des effets distincts ; leurs règles d’articulation et critères d’arbitrage restent à préciser. Le calcul de la répartition et la comparaison des options sont compris dans la décision.

Exemple fictif : sur un stock de 1 000 pièces, protéger 200 pièces pour le web et retenir un plafond de 500 pour un groupe de clients professionnels. Ce ne sont ni deux stocks physiques distincts ni une formule universelle. Ces valeurs doivent rester cohérentes avec les protections déjà actives, les engagements et la couverture du réseau.

Le résultat alimente la gouvernance et la tenue transactionnelle des données de Stock Protection, dont la capacité courante est [Supply Protection](../modeles/backlog/model.yaml). Décider de l’allocation ne met pas à jour ces données à lui seul. L’allocation à un groupe reste distincte d’une [Reservation](../modeles/backlog/model.yaml) pour un besoin identifié et de [Supply Assignment](../modeles/backlog/model.yaml) pour affecter des ressources à des besoins ou engagements. Les réserves existantes sur ces frontières sont conservées.

## D05.e — Replenishment Decision

**Définition adoptée :** Déterminer les apports nécessaires pour remplir le stock : quantités et dates, en tenant compte du stock disponible et des apports déjà engagés.

**Finalité proposée :** Retenir des apports adaptés pour combler les manques de stock, sans ignorer les contraintes ni les actions déjà engagées.

Évaluer les besoins nets et retenir les apports de [réapprovisionnement](../modeles/backlog/glossary.yaml), leurs quantités et dates, selon les cibles, le stock admissible, les entrées attendues, les contraintes et les actions déjà engagées. Une décision implique les calculs nécessaires : le calcul net est intégré à cette capacité, sans capacité Calculation autonome. Préciser la maille, l’horizon et les règles d’admissibilité ; ne pas déduire deux fois des demandes déjà intégrées à la cible.

Exemple fictif : pour une cible de 100 pièces, 30 présentes et 20 attendues à temps donnent un manque de 50, en l’absence d’autres besoins ou restrictions. Si les apports doivent être des multiples de 12, la décision peut retenir 60 pièces à une date pertinente, après examen de l’excédent créé et des autres contraintes. Une nouvelle évaluation tient compte des compléments déjà demandés ou commandés.

Le réapprovisionnement peut être un complément fournisseur ou un réassort magasin par le réseau habituel. [Stock Redistribution Decision](../modeles/backlog/model.yaml) examine séparément le rééquilibrage du stock existant ; les résultats sont coordonnés pour ne pas couvrir deux fois le même manque. Un transfert peut matérialiser l’un ou l’autre selon sa finalité ; aucun partage exclusif par type d’Order n’est imposé.

Le résultat précise les apports à retenir. Leur mise en action engage les Orders, gérés dans [Order Management](../modeles/backlog/model.yaml) ; [Order Promising](../modeles/backlog/model.yaml) décide comment les satisfaire. Retenir une quantité ou une date de réapprovisionnement n’est pas une promesse, une création ou un affermissement automatique d’Order, ni un mouvement physique. Le porteur détaillé du déclenchement opérationnel reste à instruire.

## D05.c — Stock Redistribution Decision

**Définition adoptée :** Déterminer les transferts de stock existant pour corriger les excédents et insuffisances entre sites.

**Finalité proposée :** Obtenir une répartition du stock mieux adaptée aux besoins des périmètres concernés.

Examiner les excédents et insuffisances entre sites puis déterminer les quantités, origines, destinations et dates pertinentes pour rééquilibrer le stock déjà présent. Les calculs de disponibilité admissible, de couverture et de conséquences sur les sites font partie de cette décision. Les critères économiques, tolérances et autorités détaillées restent à préciser.

Exemple fictif : transférer 50 pièces d’un site en excédent vers un autre site en manque, sous réserve de préserver les besoins et engagements du site donneur. La responsabilité reste distincte de [Replenishment Decision](../modeles/backlog/model.yaml), qui prévoit les apports ; leurs résultats doivent être coordonnés pour éviter le double comptage d’un même manque ou d’un même stock.

[Order Promising](../modeles/backlog/model.yaml) peut proposer un transfert pour satisfaire des Orders. Ici le résultat recherché est une meilleure répartition du stock ; le partage éventuel de données ou de moyens de calcul ne supprime pas cette distinction. Supply Assignment affecte des ressources à des besoins ou engagements sans réaliser à lui seul une redistribution physique.

La mise en action peut mobiliser des Orders gérés par D04, dont D03 travaille la satisfaction, puis des prestations suivies par D07 et réalisées par les exécutants. Décider d’un transfert ne modifie pas transactionnellement les stocks et ne réalise pas le transport ; aucun développement de logistique dans FLOW n’est déduit.

## D05.f — Inventory Planning

**Définition adoptée :** Reconfigurer les hypothèses et contraintes, mobiliser ces décisions, simuler leurs effets et valider un scénario cohérent.

**Finalité proposée :** Retenir un scénario de stock cohérent et explicite avant son application opérationnelle.

Reconfigurer les hypothèses et contraintes d’un scénario de stock, mobiliser les quatre décisions d’Inventory Optimization, simuler leurs conséquences et valider un ensemble cohérent de paramètres et d’ajustements. Les décisions peuvent être sollicitées plusieurs fois ; elles restent des capacités distinctes, pas des sous-capacités de Planning.

Exemple fictif : augmenter le service attendu dans certains magasins, réexaminer les cibles et allocations, puis comparer un scénario avec davantage d’apports à un scénario combinant apports et redistribution. Examiner ensemble les effets sur la disponibilité, l’immobilisation, les risques et les engagements avant de retenir un scénario. Une quantité déjà couverte par un transfert n’est pas de nouveau traitée comme manque à réapprovisionner.

Valider un scénario de planification ne valide pas les définitions du modèle d’urbanisme et ne met pas automatiquement les données opérationnelles à jour. La mise en application peut ensuite être manuelle ou automatique selon les règles et autorités, sans étape humaine systématique imposée. Stock Protection assure la gouvernance et la tenue transactionnelle de ses données ; la mise en action engage les Orders et les exécutants réalisent les prestations.

Les horizons demeurent opérationnels dans le périmètre actuel. Prévisions, coûts et contraintes peuvent être des entrées ; cela n’ajoute pas une capacité de prévision ou de planification de saison. Les notions transversales Decision, Planning et Management restent définies dans le glossaire de modélisation séparé, sans ajout au glossaire métier.

## Relations et historique

Les cinq capacités sont rattachées directement à D05. Inventory Planning mobilise les quatre décisions par des relations métier explicites ; aucune décomposition sous Planning. D05.b est conservée dans [le snapshot antérieur](../modeles/backlog/history/pre-U235.yaml), remplacée par D05.e sans transfert de validation.

Portées et empreintes : [registre U235](../modeles/backlog/d05-refactoring.yaml). Notions transversales : [glossaire de modélisation](../modeles/backlog/modeling-glossary.yaml), distinct du glossaire métier.


## Actualisation U269 — comportements du scénario

La description D05.f ci-dessus conserve l’état U235. U269 adopte désormais Scenario Construction, Scenario Simulation, Scenario Evaluation, Scenario Validation et Scenario Application. L’application déclenche les actions retenues et connaît leur prise en compte via les capacités opérationnelles responsables. Leurs responsabilités restent distinctes ; les quatre décisions D05 ne deviennent pas des comportements. Valeurs et portées courantes dans le modèle YAML et [les cinq comportements](35-comportements-inventory-planning.md). La synthèse de capacité actualisée reste proposée, sans héritage automatique de l’ancienne définition.

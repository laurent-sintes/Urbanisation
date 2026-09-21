# Complément — cohérence et complétude des inspirations, U558

21 septembre 2026. Diagnostic du backlog hors référentiels, complément à [l’audit du modèle](rapport.md). [Preuves et inventaire structurés](../../modeles/backlog/market-inspiration-audit-U558.yaml), CMP232.

**Les inspirations sont largement conservées, mais elles ne sont pas complètement consolidées après les regroupements.** Le contrôle numérique des références est satisfaisant ; il ne suffit pas à garantir leur transmission ni la justesse de leur présentation.

## Ce qui est conservé

- Les 128 fiches examinées possèdent chacune au moins deux documents de comparaison distincts, même en regroupant les éditions d’un même document Oracle.
- Elles contiennent 283 entrées de comparaison pour 131 URLs documentaires distinctes.
- Aucune URL de comparaison n’a été retirée des fiches qui existent toujours depuis la publication 2026-09-19.11.
- 126 fiches ont une synthèse d’inspiration illustrée. Les nouveaux comportements Inventory Plan Application et Demand Plan Publication ont déjà leurs références, mais pas encore cette synthèse.
- Les choix structurants récents sont généralement expliqués : application dans le Planning, décisions et configuration distinctes, périmètre FLOW différent des modules éditeurs. Les analogies Salesforce sont qualifiées comme telles, sans prétendre définir une capacité Supply standard.

## Écarts identifiés

| Constat | Effet | Recommandation |
| --- | --- | --- |
| **INS558-01 — Inspirations des comportements regroupés partiellement transmises** | Certains appuis restent dans l’historique et ne sont plus visibles sur les successeurs. Cinq URLs des comportements retirés ne figurent plus dans les comparaisons courantes du périmètre. | Reporter les apports et exemples encore utiles dans Supply Assignment, Optimization Request Management ou leur Planning, avec leurs limites. Justifier les remplacements ; ne pas recréer les anciens comportements. |
| **INS558-02 — Deux synthèses illustrées manquent** | Inventory Plan Application et Demand Plan Publication sont sourcés, mais leur restitution est moins complète. | Ajouter choix, approche FLOW, synthèse et exemple qualifié. La présence de deux sources reste distincte de la qualité de cette explication. |
| **INS558-03 — Demand Planning : attribution et synthèse à reprendre** | Le tableau attribue à l’approche Oracle la prise en compte des possibilités et apports planifiés, que le passage cité ne démontre pas. La ligne SAP reprend surtout une frontière FLOW. La synthèse parle de publication Oracle en laissant au second plan le cœur de Demand Planning étayé par SAP. | Séparer ce que documente chaque éditeur de l’adaptation FLOW et rétablir une synthèse couvrant toute la capacité. |
| **INS558-04 — Répétitions dans les tableaux** | Trois fiches présentent un même document Oracle dans plusieurs éditions ; seize lignes sur huit fiches répètent le même texte dans Périmètre et Approche. | Mettre l’édition pertinente au premier plan, conserver l’historique et distinguer ce qui est couvert de la manière d’agir. |

### Exemple de transmission incomplète

Les anciens comportements Incremental Supply Assignment et Supply Reassignment présentaient le cas SAP d’une commande de 100 pièces déjà affectée à hauteur de 70 : conserver 70 et chercher le complément, ou réexaminer les 100. Le comportement Supply Assignment conserve les deux modalités métier, mais son inspiration actuelle montre seulement la continuité d’un lien lors d’une réception.

La comparaison spécifique avec SAP Reassignment et son exemple n’ont donc pas suivi la consolidation. **C’est une perte de restitution, pas une perte de la responsabilité ni une destruction de la preuve historique.** La source est conservée dans la publication et les registres. Son ouverture directe a été tentée dans cette revue ; le portail SAP n’a pas fourni de texte exploitable, ce qui interdit de présenter son contenu comme nouvellement vérifié.

Le même suivi est documenté pour EDQA, l’appui aux réactions aux impondérables, et pour Service Process Studio, l’appui au suivi des suites. Les cinq URLs absentes sont listées dans l’annexe. Leur nombre ne signifie pas cinq fonctions sans preuve : certains sujets disposent d’autres sources ou éditions, à rapprocher explicitement.

### Attribution à corriger dans Demand Planning

[Oracle — Overview of Supply Chain Planning Plan Types](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faupc/overview-of-supply-chain-planning-plan-types.html), édition 26B, documente pour Demand Plan la prévision collaborative/statistique et l’alimentation d’un plan Supply ou Replenishment. Cette ligne ne suffit pas à lui attribuer notre formulation sur la confrontation aux apports planifiés.

[SAP — Demand planning](https://www.sap.com/products/scm/integrated-business-planning/features/demand-planning.html), page évolutive relue le 21 septembre, documente prévisions, collaboration et ajustements à partir des signaux de demande. La distinction FLOW entre demande connue, prévision et engagement doit être présentée comme notre frontière, sans l’attribuer à ce document.

Ces deux documents restent pertinents. C’est leur interprétation et leur placement dans le tableau qui doivent être affinés ; le constat ne remet pas en cause l’existence de Demand Planning.

## Portée du contrôle

Présence et conservation contrôlées sur les 128 fiches ; cohérence sémantique revue sur les 21 fiches modifiées depuis la publication et sur les inspirations des sept comportements regroupés. Les appuis primaires utiles aux constats ont été consultés ou leur limite d’accès consignée. Les 131 URLs n’ont pas toutes été reconsultées : cet audit ne certifie pas chaque affirmation inchangée ni la disponibilité actuelle de tous les liens.

Les inspirations des référentiels restent exclues ; celles des termes du glossaire ne sont pas comprises dans ces compteurs. Atlas affiche les publications : ces écarts concernent le backlog et sa future restitution, pas une modification déjà visible dans la publication courante. Aucune correction du modèle ni release effectuée par cet audit.

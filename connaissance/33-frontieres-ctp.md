# CTP : faisabilité après adaptation et décisions spécialisées

16 septembre 2026 — U250/U251. L'autorité de travail est `modeles/backlog/model.yaml` ; portées et empreintes dans `modeles/backlog/d03-review.yaml`, `ctp_boundaries_U251`. La v007 conserve son état publié.

## CTP

**Définition adoptée U251 :** Déterminer les possibilités de satisfaction d’un Order nécessitant une adaptation des ressources ou des engagements, en mobilisant les décisions spécialisées et en explicitant les conditions de faisabilité et les impacts.

CTP conserve son nom, sa nature de décision et sa finalité. Sa maille est celle d'une solution Supply candidate cohérente. Il peut identifier qu'une politique ou un engagement devrait évoluer ; chaque résultat spécialisé garde son responsable d'arbitrage.

| Résultat | Responsabilité | Contribution de CTP |
| --- | --- | --- |
| Priorité entre Orders | Order Prioritization | Utiliser les priorités dans les possibilités de satisfaction |
| Échéancier retenu | Delivery Schedule Decision | Fournir des quantités et dates possibles après adaptation |
| Arbitrage économique | PTP | Fournir possibilités et impacts comparables |
| Politiques d'allocation / niveaux et seuils | Stock Allocation Decision / Coverage Target Decision | Identifier un changement nécessaire et mobiliser la décision concernée |
| Service/exécutant compatible | Execution Service Decision | Mobiliser cette décision pour la faisabilité de la solution Supply |
| Variation du plan d'exécution | Execution Adaptation Decision | Contribuer au réexamen Supply si la variation affecte la satisfaction de l'Order |

La proposition ou le réexamen n'applique pas automatiquement les modifications d'Orders, de promesses, de protections, d'affectations ou de réservations. Un résultat candidat de décision ne vaut pas politique active. La responsabilité d'une éventuelle dérogation ponctuelle reste à préciser.

## Exemple proposé

Une commande demande 100 pièces vendredi ; seules 60 sont admissibles dans la situation de référence. CTP examine les conditions d'obtention des 40 manquantes. Une possibilité implique un apport supplémentaire et un service réalisable ; une autre aurait un impact sur une commande concurrente et mobilise donc l'arbitrage de priorité. Selon le cas, PTP compare les conséquences économiques et Delivery Schedule Decision retient un échéancier parmi les possibilités.

Le résultat n'est ni un achat déjà créé, ni une promesse modifiée, ni une protection levée. Il explicite ce qui rendrait la fourniture possible et les conditions restant à satisfaire. L'exemple est fictif et proposé ; il ne fixe aucune règle Beaumanoir ni séquence universelle entre décisions.

## Finalité Order et finalité stock

Un apport ou transfert envisagé pour honorer un Order relève de la satisfaction Supply. Replenishment Decision et Stock Redistribution Decision répondent à la recherche d'un stock souhaitable ou mieux réparti. Une même opération peut contribuer aux deux finalités sans fusion des responsabilités. U251 ne rend pas tout approvisionnement CTP dépendant de D05.

## Portée de l'application

Six relations sont proposées, orientées consommateur → fournisseur : CTP vers priorités, service, allocation et cibles de couverture ; PTP et Delivery Schedule Decision vers CTP. Elles sont conditionnelles, sans parenté ni appel technique obligatoire. Le type existant `relates-to` est conservé et son sens qualifié.

Seule la définition présentée reçoit la nouvelle validation de champ. Les accords de frontière sont consignés séparément ; le scope rédigé après le Go, l'exemple, les qualifications détaillées des relations et la reprise lexicale TER045 restent proposés. Les autres capacités gardent leurs champs et statuts. L'audit U249 reste un constat de v007, non réécrit rétrospectivement.

# Dépendances proposées et relations existantes

> Revue de référence U286–U289 avant migration. Le socle a été appliqué U290 ; les mentions de proposition ou de migration à venir ci-dessous décrivent cet état antérieur. Voir le [bilan courant](../2026-09-17-refonte-appliquee/rapport.md).

[Synthèse](rapport.md)

Propositions de contrats métier issues des descriptions ; elles ne sont pas toutes adoptées. Consommateur → fournisseur, avec résultat et condition. Les paires historiques sont des repères de recherche, pas des équivalences certifiées. Les références d’ingestion désignent les informations projetées ; elles n’imposent pas d’appeler le processus d’ingestion à chaque décision.

| Consommateur | Fournisseur | Résultat requis | Condition | Repères existants |
| --- | --- | --- | --- | --- |
| D01.f | D01.g | Faits de stock qualifiés et corrections tracées | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D01.f | D07.d | Faits, jalons et estimations | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D01.g | D01.d | Constats et corrections de comptage justifiés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D01.g | D07.c | Résultats rapprochés et écarts qualifiés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D01.c | D01.f | État courant et ressources futures séparés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D01.d | D01.c | Quantités et états avec provenance et fraîcheur | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D02.b | D05.a | Cibles et seuils proposés ou retenus | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D02.b | D05.d | Droits de groupes et limites proposés ou retenus | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D02.c | D01.c | Quantités et états avec provenance et fraîcheur | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D02.c | D02.b | Protections applicables, droits et limites par période | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.a | D03.i | Possibilités quantité/date de référence | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.a | D03.j | Possibilités sous adaptation et conditions | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.a | D03.k | Arbitrage économique | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.a | D03.l | Échéancier retenu | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.b | D03.a | Propositions de promesse | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.b | D02.c | Engagements opposables selon frontière à arbitrer | Selon arbitrage Reservation/Assignment ; ne pas déduire plusieurs fois un même engagement. | À créer/qualifier |
| D03.b | D02.e | Affectations aux besoins identifiés | Selon arbitrage Reservation/Assignment ; ne pas déduire plusieurs fois un même engagement. | À créer/qualifier |
| D03.c | D03.i | Possibilités quantité/date de référence | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.c | D03.j | Possibilités sous adaptation et conditions | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.c | D03.m | Priorités relatives des Orders | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.c | D07.d | Faits, jalons et estimations | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.c | D06.f | Variation opérationnelle retenue et impacts Supply | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-ADAPTATION-PROMISE-REVISION |
| D02.e | D01.c | Quantités et états avec provenance et fraîcheur | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D02.e | D02.b | Protections applicables, droits et limites par période | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D02.e | D02.c | Engagements opposables selon frontière à arbitrer | Selon arbitrage Reservation/Assignment ; ne pas déduire plusieurs fois un même engagement. | À créer/qualifier |
| D02.e | D03.m | Priorités relatives des Orders | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.i | D01.c | Quantités et états avec provenance et fraîcheur | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.i | D02.b | Protections applicables, droits et limites par période | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.i | D02.c | Engagements opposables selon frontière à arbitrer | Selon arbitrage Reservation/Assignment ; ne pas déduire plusieurs fois un même engagement. | À créer/qualifier |
| D03.i | D02.e | Affectations aux besoins identifiés | Selon arbitrage Reservation/Assignment ; ne pas déduire plusieurs fois un même engagement. | À créer/qualifier |
| D03.i | D06.b | Capacité contextuelle communiquée et datée | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.i | D13.a | Lieux et liens du réseau | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.j | D03.i | Possibilités quantité/date de référence | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.j | D03.m | Priorités relatives des Orders | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-CTP-ORDER-PRIORITIZATION |
| D03.j | D06.e | Services/exécutants compatibles retenus | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-CTP-EXECUTION-SERVICE |
| D03.j | D05.a | Cibles et seuils proposés ou retenus | Uniquement si l’option nécessite une évolution de politique ; aucune application par CTP. | REL-CTP-COVERAGE-TARGET |
| D03.j | D05.d | Droits de groupes et limites proposés ou retenus | Uniquement si l’option nécessite une évolution de politique ; aucune application par CTP. | REL-CTP-STOCK-ALLOCATION |
| D03.k | D03.i | Possibilités quantité/date de référence | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.k | D03.j | Possibilités sous adaptation et conditions | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-PTP-CTP-SCENARIOS |
| D03.k | D11.a | Conditions contractuelles et validité | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.l | D03.i | Possibilités quantité/date de référence | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.l | D03.j | Possibilités sous adaptation et conditions | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-DELIVERY-SCHEDULE-CTP |
| D03.l | D03.k | Arbitrage économique | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.l | D11.a | Conditions contractuelles et validité | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D03.m | D11.a | Conditions contractuelles et validité | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.i | D04.n | Structure transformée et liens à l’origine | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.i | D04.o | Progression autorisée et restrictions | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.i | D07.c | Résultats rapprochés et écarts qualifiés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-FACTS-D04.i |
| D04.i | D03.b | Engagements confirmés et part non confirmée | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.i | D08.d | Produits/variantes et caractéristiques utiles | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.i | D09.d | Parties et rôles externes | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.i | D11.a | Conditions contractuelles et validité | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.i | D12.a | Offre commerciale externe | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.j | D04.n | Structure transformée et liens à l’origine | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.j | D04.o | Progression autorisée et restrictions | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.j | D07.c | Résultats rapprochés et écarts qualifiés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-FACTS-D04.j |
| D04.j | D08.d | Produits/variantes et caractéristiques utiles | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.j | D09.d | Parties et rôles externes | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.j | D11.a | Conditions contractuelles et validité | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.k | D04.n | Structure transformée et liens à l’origine | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.k | D04.o | Progression autorisée et restrictions | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.k | D07.c | Résultats rapprochés et écarts qualifiés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-FACTS-D04.k |
| D04.k | D13.a | Lieux et liens du réseau | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.k | D08.d | Produits/variantes et caractéristiques utiles | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.l | D04.n | Structure transformée et liens à l’origine | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.l | D04.o | Progression autorisée et restrictions | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.l | D07.c | Résultats rapprochés et écarts qualifiés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-FACTS-D04.l |
| D04.l | D04.i | Demande client et conditions | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.l | D08.d | Produits/variantes et caractéristiques utiles | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.m | D04.n | Structure transformée et liens à l’origine | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.m | D04.o | Progression autorisée et restrictions | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.m | D07.c | Résultats rapprochés et écarts qualifiés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-FACTS-D04.m |
| D04.m | D04.j | Apports fournisseur attendus et possibilités de modification | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.m | D09.d | Parties et rôles externes | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.m | D11.a | Conditions contractuelles et validité | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.n | D03.l | Échéancier retenu | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.o | D03.b | Engagements confirmés et part non confirmée | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D04.o | D07.d | Faits, jalons et estimations | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.a | D01.c | Quantités et états avec provenance et fraîcheur | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.a | D13.a | Lieux et liens du réseau | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.a | D08.d | Produits/variantes et caractéristiques utiles | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.d | D01.c | Quantités et états avec provenance et fraîcheur | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.d | D02.b | Protections applicables, droits et limites par période | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.d | D05.a | Cibles et seuils proposés ou retenus | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.e | D01.c | Quantités et états avec provenance et fraîcheur | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.e | D02.b | Protections applicables, droits et limites par période | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.e | D05.a | Cibles et seuils proposés ou retenus | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.e | D07.d | Faits, jalons et estimations | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.e | D04.j | Apports fournisseur attendus et possibilités de modification | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.e | D04.k | Transferts attendus et possibilités de modification | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.c | D01.c | Quantités et états avec provenance et fraîcheur | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.c | D02.b | Protections applicables, droits et limites par période | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.c | D13.a | Lieux et liens du réseau | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.c | D05.e | Apports et ajustements recommandés selon arbitrage | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.f | D05.a | Cibles et seuils proposés ou retenus | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-INVENTORY-PLANNING-D05.a |
| D05.f | D05.d | Droits de groupes et limites proposés ou retenus | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-INVENTORY-PLANNING-D05.d |
| D05.f | D05.e | Apports et ajustements recommandés selon arbitrage | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-INVENTORY-PLANNING-D05.e |
| D05.f | D05.c | Rééquilibrage recommandé du stock existant | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-INVENTORY-PLANNING-D05.c |
| D05.f | D01.c | Quantités et états avec provenance et fraîcheur | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.f | D07.d | Faits, jalons et estimations | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D05.f | D02.b | Résultat de mise à jour des protections et des règles retenues, y compris refus/prise en compte partielle | Pour la mise en action des choix autorisés et le suivi de leur prise en compte ; aucune réalisation physique par Planning. | À créer/qualifier |
| D05.f | D04.j | Commandes d’apport créées ou modifiées selon choix autorisés et résultat de prise en compte | Pour la mise en action des choix autorisés et le suivi de leur prise en compte ; aucune réalisation physique par Planning. | À créer/qualifier |
| D05.f | D04.k | Orders de transfert créés ou modifiés selon choix autorisés et résultat de prise en compte | Pour la mise en action des choix autorisés et le suivi de leur prise en compte ; aucune réalisation physique par Planning. | À créer/qualifier |
| D05.f | D06.d | État de prise en compte et coordination des prestations nécessaires au scénario | Pour la mise en action des choix autorisés et le suivi de leur prise en compte ; aucune réalisation physique par Planning. | À créer/qualifier |
| D06.b | D14.a | Services, SLA et accès configurés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D07.a | D14.a | Services, SLA et accès configurés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D07.a | D13.a | Lieux et liens du réseau | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D07.a | D04.i | Demande client et conditions | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D06.e | D07.a | Prestations nécessaires | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D06.e | D14.a | Services, SLA et accès configurés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D06.e | D13.a | Lieux et liens du réseau | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D06.e | D06.b | Capacité contextuelle communiquée et datée | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-SERVICE-CAPACITY |
| D06.f | D07.d | Faits, jalons et estimations | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-TRACKING-ADAPTATION |
| D06.f | D07.b | Demandes et réponses de prise en charge | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D06.f | D06.e | Services/exécutants compatibles retenus | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-ADAPTATION-SERVICE |
| D06.f | D06.b | Capacité contextuelle communiquée et datée | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-ADAPTATION-CAPACITY |
| D06.d | D07.a | Prestations nécessaires | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D06.d | D06.e | Services/exécutants compatibles retenus | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D06.d | D06.f | Variation opérationnelle retenue et impacts Supply | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-ADAPTATION-ORCHESTRATION |
| D06.d | D07.b | Demandes et réponses de prise en charge | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-ORCHESTRATION-COMMITMENTS |
| D06.d | D07.d | Faits, jalons et estimations | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-TRACKING-ORCHESTRATION |
| D07.b | D07.a | Prestations nécessaires | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | REL-EXECUTION-REQUIREMENTS-SERVICE-ORDER |
| D07.b | D06.e | Services/exécutants compatibles retenus | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D07.b | D14.a | Services, SLA et accès configurés | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D07.d | D07.b | Demandes et réponses de prise en charge | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D07.c | D07.b | Demandes et réponses de prise en charge | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D07.c | D07.d | Faits, jalons et estimations | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D11.a | D09.d | Parties et rôles externes | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D11.a | D12.a | Offre commerciale externe | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D12.a | D08.d | Produits/variantes et caractéristiques utiles | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D13.a | D09.d | Parties et rôles externes | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D14.a | D09.d | Parties et rôles externes | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |
| D14.a | D13.a | Lieux et liens du réseau | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle. | À créer/qualifier |

Le regroupement Promise Management adopté U288 conduit à remplacer D03.a/b/c par la clé proposée PROMISE-MANAGEMENT. Les dépendances devenant internes ne créent pas de boucle ; les autres contrats sont conservés et dédoublonnés seulement après examen. La projection figure dans le YAML.

## Revue exhaustive des liens courants

| ID | Relation actuelle | Traitement | Motif |
| --- | --- | --- | --- |
| REL-MEMBER-D01.f | D01 → D01.f (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D01.g | D01 → D01.g (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D01.c | D01 → D01.c (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D01.d | D01 → D01.d (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D02.b | D01 → D02.b (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D02.c | D01 → D02.c (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D03.a | D03 → D03.a (contains) | redirect_after_adopted_merge | Regroupement adopté U288 ; rattacher le nouveau parent, préserver les liens de la responsabilité devenue comportement quand pertinents, sans transfert automatique de validation. |
| REL-MEMBER-D03.b | D03 → D03.b (contains) | redirect_after_adopted_merge | Regroupement adopté U288 ; rattacher le nouveau parent, préserver les liens de la responsabilité devenue comportement quand pertinents, sans transfert automatique de validation. |
| REL-MEMBER-D03.c | D03 → D03.c (contains) | redirect_after_adopted_merge | Regroupement adopté U288 ; rattacher le nouveau parent, préserver les liens de la responsabilité devenue comportement quand pertinents, sans transfert automatique de validation. |
| REL-MEMBER-D02.e | D03 → D02.e (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D03.i | D03 → D03.i (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D03.j | D03 → D03.j (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D03.k | D03 → D03.k (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D03.l | D03 → D03.l (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D05.a | D05 → D05.a (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D05.d | D05 → D05.d (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D05.e | D05 → D05.e (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D05.c | D05 → D05.c (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D05.f | D05 → D05.f (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D06.b | D06 → D06.b (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D07.a | D06 → D07.a (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D07.b | D06 → D07.b (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D07.c | D06 → D07.c (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D07.d | D06 → D07.d (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-GROUP-D09 | business-references → D09 (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D09.d | D09 → D09.d (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-GROUP-D11 | business-references → D11 (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D11.a | D11 → D11.a (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-GROUP-D08 | business-references → D08 (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D08.d | D08 → D08.d (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-GROUP-D12 | business-references → D12 (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D12.a | D12 → D12.a (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-GROUP-D13 | business-references → D13 (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D13.a | D13 → D13.a (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-ILL-001 | D03.b → ILL-OBJ-01 (confirms) | redirect_after_adopted_merge | Regroupement adopté U288 ; rattacher le nouveau parent, préserver les liens de la responsabilité devenue comportement quand pertinents, sans transfert automatique de validation. |
| REL-ILL-002 | D03.b → ILL-DOC-01 (associated-document) | redirect_after_adopted_merge | Regroupement adopté U288 ; rattacher le nouveau parent, préserver les liens de la responsabilité devenue comportement quand pertinents, sans transfert automatique de validation. |
| REL-ILL-003 | D03.b → ILL-EVT-01 (observed-result) | redirect_after_adopted_merge | Regroupement adopté U288 ; rattacher le nouveau parent, préserver les liens de la responsabilité devenue comportement quand pertinents, sans transfert automatique de validation. |
| REL-ILL-004 | ILL-DOC-01 → ILL-OBJ-01 (represents) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-ILL-005 | ILL-DOC-01 → ILL-EVT-01 (records) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-ILL-006 | D01 → D03 (provides-knowledge) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-ILL-007 | D11 → D03 (provides-conditions) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-ILL-008 | D13 → D06 (describes-network) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-UNIVERSE-SUPPLY-D01 | universe-supply → D01 (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-UNIVERSE-SUPPLY-D03 | universe-supply → D03 (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-UNIVERSE-SUPPLY-D04 | universe-supply → D04 (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-UNIVERSE-SUPPLY-D05 | universe-supply → D05 (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-UNIVERSE-SUPPLY-D06 | universe-supply → D06 (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-UNIVERSE-SUPPLY-business-references | universe-supply → business-references (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D03.m | D03 → D03.m (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D04.i | D04 → D04.i (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D04.j | D04 → D04.j (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D04.k | D04 → D04.k (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D04.l | D04 → D04.l (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D04.m | D04 → D04.m (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D04.n | D04 → D04.n (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D04.o | D04 → D04.o (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-EXECUTION-FACTS-D04.i | D07.c → D04.i (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-FACTS-D04.j | D07.c → D04.j (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-FACTS-D04.k | D07.c → D04.k (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-FACTS-D04.l | D07.c → D04.l (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-FACTS-D04.m | D07.c → D04.m (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-INVENTORY-PLANNING-D05.a | D05.f → D05.a (relates-to) | update_wording_only | Mobilisation conservée ; actualiser le vocabulaire de Planning. |
| REL-INVENTORY-PLANNING-D05.d | D05.f → D05.d (relates-to) | update_wording_only | Mobilisation conservée ; actualiser le vocabulaire de Planning. |
| REL-INVENTORY-PLANNING-D05.e | D05.f → D05.e (relates-to) | update_wording_only | Mobilisation conservée ; actualiser le vocabulaire de Planning. |
| REL-INVENTORY-PLANNING-D05.c | D05.f → D05.c (relates-to) | update_wording_only | Mobilisation conservée ; actualiser le vocabulaire de Planning. |
| REL-MEMBER-D06.d | D06 → D06.d (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-GROUP-D14 | business-references → D14 (presents) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D14.a | D14 → D14.a (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-SERVICE-CATALOG-EXECUTION | D14 → D06 (provides-conditions) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-SERVICE-CATALOG-PROMISING | D14 → D03 (provides-conditions) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-PROMISING | D06 → D03 (provides-knowledge) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-TRACKING-ORCHESTRATION | D07.d → D06.d (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-ORCHESTRATION-COMMITMENTS | D06.d → D07.b (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-MEMBER-D06.e | D06 → D06.e (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-MEMBER-D06.f | D06 → D06.f (contains) | retain | Hiérarchie explicite conservée ; aucun parent déduit du préfixe. |
| REL-EXECUTION-TRACKING-ADAPTATION | D07.d → D06.f (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-ADAPTATION-SERVICE | D06.f → D06.e (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-ADAPTATION-CAPACITY | D06.f → D06.b (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-ADAPTATION-ORCHESTRATION | D06.f → D06.d (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-ADAPTATION-PROMISE-REVISION | D06.f → D03.c (relates-to) | redirect_after_adopted_merge | Regroupement adopté U288 ; rattacher le nouveau parent, préserver les liens de la responsabilité devenue comportement quand pertinents, sans transfert automatique de validation. |
| REL-EXECUTION-SERVICE-CAPACITY | D06.e → D06.b (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-EXECUTION-REQUIREMENTS-SERVICE-ORDER | D07.a → D07.b (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-CTP-ORDER-PRIORITIZATION | D03.j → D03.m (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-CTP-EXECUTION-SERVICE | D03.j → D06.e (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-CTP-STOCK-ALLOCATION | D03.j → D05.d (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-CTP-COVERAGE-TARGET | D03.j → D05.a (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-PTP-CTP-SCENARIOS | D03.k → D03.j (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-DELIVERY-SCHEDULE-CTP | D03.l → D03.j (relates-to) | retain_and_qualify | Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique. |
| REL-ATP-BHV001 | D03.i → BHV001 (contains) | migrate_with_behavior | Définition conservée ; justification rééprouvée selon U283. |
| REL-ATP-BHV002 | D03.i → BHV002 (contains) | migrate_with_behavior | Définition conservée ; justification rééprouvée selon U283. |
| REL-ATP-BHV003 | D03.i → BHV003 (contains) | migrate_with_behavior | Définition conservée ; justification rééprouvée selon U283. |
| REL-ATP-BHV004 | D03.i → BHV004 (contains) | migrate_with_behavior | Définition conservée ; justification rééprouvée selon U283. |
| REL-PLANNING-BHV005 | D05.f → BHV005 (contains) | migrate_with_behavior | Préciser la construction d’alternatives ; conserver l’identité. |
| REL-PLANNING-BHV006 | D05.f → BHV006 (contains) | migrate_with_behavior | Conserver l’identité de simulation en intégrant l’analyse. |
| REL-PLANNING-BHV010 | D05.f → BHV010 (contains) | migrate_with_behavior | Préserver indicateurs et explications dans le comportement combiné et archiver les accords U271. |
| REL-PLANNING-BHV007 | D05.f → BHV007 (contains) | migrate_with_behavior | Conserver comparaison/appréciation sans nœud autonome. |
| REL-PLANNING-BHV008 | D05.f → BHV008 (contains) | migrate_with_behavior | Conserver autorisation, conditions et réserves sans nœud autonome. |
| REL-PLANNING-BHV009 | D05.f → BHV009 (contains) | migrate_with_behavior | Conserver application et prise en compte ; ne pas réutiliser cet ID pour adaptation. |
| REL-PROTECTION-BHV011 | D02.b → BHV011 (contains) | migrate_with_behavior | Conserver les opérations sur les enveloppes comme fonctions des mécanismes concernés ; pas de comportement par opération. |
| REL-PROTECTION-BHV012 | D02.b → BHV012 (contains) | migrate_with_behavior | Conserver les opérations sur les enveloppes comme fonctions des mécanismes concernés ; pas de comportement par opération. |
| REL-PROTECTION-BHV013 | D02.b → BHV013 (contains) | migrate_with_behavior | Conserver les opérations sur les enveloppes comme fonctions des mécanismes concernés ; pas de comportement par opération. |
| REL-PROTECTION-BHV014 | D02.b → BHV014 (contains) | migrate_with_behavior | Conserver les opérations sur les enveloppes comme fonctions des mécanismes concernés ; pas de comportement par opération. |
| REL-PROTECTION-BHV015 | D02.b → BHV015 (contains) | migrate_with_behavior | Conserver les opérations sur les enveloppes comme fonctions des mécanismes concernés ; pas de comportement par opération. |

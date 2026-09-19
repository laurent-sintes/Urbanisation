# Protection et affectation : complétude des décisions — U256

16 septembre 2026. Lecture du backlog après U251, de `d03-review.yaml` et de l'état historique `history/pre-U154.json`. Analyse proposée, sans modification du catalogue. Les capacités sont identifiées par leurs rattachements explicites ; D02.b/c appartiennent à D01, D02.e à D03.

## Direction examinée

Supply Protection peut porter la tenue opérationnelle des droits et limites d'usage par groupes, avec leur validité et leur cycle. Supply Assignment peut porter les affectations, réaffectations et libérations entre ressources et besoins. Les décisions fournissent les résultats nécessaires à ces actions. Une action large ne devient pas responsable de tous les arbitrages qu'elle applique.

Cette direction ne tranche pas encore le regroupement de Reservation avec Supply Assignment. Il faut tester si une affectation peut exister sans engagement opposable aux autres besoins, et si un engagement peut exister sans affectation détaillée. Une différence de résultat ou d'état ne suffit pas à imposer deux capacités ; elle peut aussi être tenue dans le cycle d'une même capacité large.

La complétude est examinée sur les cas ci-dessous. Elle ne constitue pas une preuve exhaustive sur tous les contextes Supply, dont les règles détaillées restent en instruction. « Présent » signifie responsabilité nommée dans le backlog, pas contrat intégralement défini ni validation de tous ses champs.

## Questions métier et couverture

| Cas / question de décision | Exemple fictif | Responsable actuel ou piste | Diagnostic |
| --- | --- | --- | --- |
| D01 — Quel niveau de stock et quels seuils viser ? | Cible magasin 100, seuil de réassort 60 | Coverage Target Decision — D05.a | Présent. Les paramètres de couverture ne sont pas tous des restrictions d'usage ; leur application opérationnelle reste à attribuer précisément. |
| D02 — Quelle quantité protéger ou quel plafond retenir pour un groupe, dans quel périmètre/période ? | Protéger 200 pièces pour le web sur un stock partagé | Stock Allocation Decision — D05.d | Présent. Le scope inclut périmètre et période ; ne pas créer une décision par paramètre, canal ou date. Supply Protection tient les valeurs applicables. |
| D03 — Quel besoin servir en priorité ? | Deux Orders concurrents pour 50 pièces | Order Prioritization — D03.m | Présent. Expliciter les critères et le résultat de priorité ; il ne constitue pas lui-même une affectation ou réservation. |
| D04 — Quelle quantité et quelles dates sont admissibles sous les règles actives ? | Un canal demande 70 pièces alors que seules 40 lui sont mobilisables | ATP — D03.i | Présent ; éligibilité et protections intégrées à ATP lors d'U154. Une dérogation à la règle est un autre cas, ci-dessous. |
| D05 — Quelles adaptations permettraient de satisfaire le besoin ? | Il manque 40 pièces à la date demandée | CTP — D03.j | Présent, clarifié U251. Établit possibilités/conditions/impacts en mobilisant les décisions spécialisées ; n'applique pas leurs résultats. |
| D06 — Quelle solution retenir selon ses conséquences économiques ? | Une livraison unique ou une solution avec complément urgent | PTP — D03.k | Présent. Décrire critères et contraintes ; un optimum économique ne crée pas une autorisation de déroger. |
| D07 — Quel échéancier retenir ? | 60 pièces vendredi et 40 lundi parmi les possibilités réalisables | Delivery Schedule Decision — D03.l | Présent. Le résultat retenu est distinct des possibilités de dates et de leur matérialisation dans les Orders. |
| D08 — Quelles ressources précises couvrent quels besoins ? | Couvrir 30 pièces par 20 présentes au site A et 10 d'une réception attendue | Responsabilité historique intégrée à la construction/comparaison des solutions ATP/CTP/PTP ; Supply Assignment applique/maintient la couverture | **Résultat insuffisamment explicite.** Identifier la maille du plan de couverture et le responsable du choix retenu, notamment lorsque le coût n'est pas le critère décisif. Ne pas attribuer silencieusement cette décision à l'action Supply Assignment ni créer automatiquement Supply Assignment Decision. |
| D09 — Une substitution de produit est-elle admissible pour ce besoin ? | Le produit demandé manque ; un autre produit est envisagé | Responsabilité historique intégrée aux solutions ATP/CTP/PTP sous règles applicables | **Cas à documenter.** Une variante taille/couleur n'est pas réputée interchangeable. Préciser les conditions externes et les arbitrages mobilisés. Pas de résurrection automatique d'une capacité retirée. |
| D10 — Peut-on exceptionnellement utiliser une quantité protégée pour un autre groupe ? | Mobiliser 30 pièces protégées pour le web afin de satisfaire un engagement B2B | Responsable de la dérogation ponctuelle non attribué ; point ouvert U251 | **Trou d'attribution.** Distinguer dérogation locale sous conditions et nouvelle politique de groupe déterminée par D05.d. Candidat à instruire : Protection Exception Decision, sans nom, domaine ou nouvelle capacité adoptés. Si une règle active autorise déjà l'usage, le cas peut relever de l'admissibilité ATP. |
| D11 — Quand un choix de couverture devient-il un engagement, et que libère une annulation ? | Couverture candidate, puis engagement ; annulation de 10 pièces | Articulation Supply Assignment / Reservation / Promise Confirmation-Revision / Order Lifecycle Management | **Contrat de cycle incomplet.** Un choix métier autonome reste à démontrer ; transitions, expiration et libération peuvent être des règles/opérations de gestion. Ne pas créer une décision pour chacun de ces verbes. |

Le choix de service/exécutant est déjà porté par Execution Service Decision en D06 ; la variation du plan d'exécution par Execution Adaptation Decision. Les apports et transferts destinés à optimiser le stock relèvent de Replenishment Decision et Stock Redistribution Decision en D05. Ces capacités complètent le contexte sans devenir des dépendances obligatoires de toute affectation ni de tout apport pour honorer un Order.

## Conséquence de la maille ATP/CTP/PTP

Avant U154, D03 distinguait notamment Allocation Eligibility Decision (D03.d), Fulfillment Source Decision (D03.e), Fulfillment Route Decision (D03.f), Product Substitution Decision (D03.g) et Supply Creation Decision (D03.h). Ces identités sont retirées et ne doivent pas être réutilisées.

Le choix U151/U154 a regroupé ces responsabilités dans une maille ATP/CTP/PTP plus agrégée. Leur absence comme nœuds ne démontre donc pas une disparition métier. U251 précise que CTP mobilise les décisions spécialisées existantes ; cela n'adopte pas un retour à toutes les anciennes sous-décisions comme capacités.

Il faut distinguer **question de décision fine** et **capacité de décision autonome**. La première peut être documentée dans une capacité existante. La seconde se justifie si elle porte un résultat durable identifiable, réutilisable et arbitré séparément. Les questions ou cas d'une fiche ne deviennent pas des sous-capacités implicites ni de nouveaux niveaux de modèle.

## Trois cas qui éprouvent le découpage

1. **Quota sans commande.** Déterminer 200 pièces de protection web, puis les rendre applicables et les réviser à leur échéance. Ce droit collectif existe sans affectation à un Order précis. D05.d et Supply Protection sont mobilisés ; la réservation d'un besoin individuel n'est pas déduite.
2. **Couverture puis engagement.** Pour un besoin de 30 pièces, une solution propose 20 présentes et 10 attendues. Établir qui choisit et retient cette couverture, puis quels effets rend la gestion opposables aux usages concurrents. La date promise, l'affectation des ressources et l'engagement doivent être interprétables sans trois doubles débits de quantité. Ce cas permet de juger si Reservation mérite une capacité distincte.
3. **Demande exceptionnelle sur protection.** Une commande B2B requiert 30 pièces protégées pour le web. Une priorité élevée ou un coût inférieur ne vaut pas à lui seul droit d'usage. Vérifier d'abord si la règle active autorise ce cas ; sinon attribuer la décision de dérogation, sa portée, ses impacts et sa durée. Une éventuelle révision durable de politique reste distincte.

## Recommandation

Conserver Supply Protection et Supply Assignment comme base d'actions larges à préciser ; laisser leur rattachement et Reservation inchangés pendant l'examen. Compléter d'abord les résultats et cas des décisions existantes : admissibilité, couverture par ressources identifiées, substitution, résultat retenu et effets d'engagement.

Instruire séparément la dérogation ponctuelle de protection. C'est le candidat le plus net à une décision supplémentaire dans les cas examinés ; son autonomie doit être établie avant ajout. Le choix détaillé de couverture est une zone à expliciter dans ATP/CTP/PTP, puis seulement à extraire si un arbitrage autonome reste sans porteur.

Les paramètres de stock qui ne restreignent pas les usages (par exemple le simple déclenchement du réassort) conservent leur question d'application ouverte. Cette analyse ne place pas automatiquement toutes les politiques de stock dans Supply Protection et n'applique pas les autres propositions U252.


## Suite U259 — programme de clarification proposé

Les 13 capacités de nature decision du backlog comprennent cinq décisions D03, quatre D05, trois D06 et Order Lifecycle Management, dont la nature reste à clarifier. Proposer une revue par ensembles d’arbitrages : D03 d’abord, D05 ensuite, D06 puis le contrat d’autorisation D04. Ce programme n’est pas une séquence d’exécution métier.

Pour chaque décision : question précise, entrées et contraintes, résultat choisi ou possibilités établies, frontières et consommateurs, exemple normal et exemple limite. Priorités de challenge D03 : situation de référence versus adaptation ; résultat de couverture suffisamment explicite ; partage du choix coût/service/échéancier entre PTP et Delivery Schedule Decision ; force des priorités ; distinction règle de protection active, nouvelle politique et dérogation.

Premier cas proposé : besoin de 100 pièces vendredi, 60 admissibles localement, 40 disponibles ailleurs à temps avec surcoût, ou 40 attendues lundi. Éprouver séparément une date impérative et une date préférée avec fractionnement autorisé. L’arbitrage économique ne rend pas admissible une solution contraire à une contrainte impérative. Hypothèse de travail proposée : ATP explicite une couverture réalisable (sources ou ressources pertinentes, quantités, dates, conditions), au-delà d’un seul total disponible ; niveau d’identification et responsabilité du choix retenu restent à préciser. Aucun changement de capacité appliqué.

# Audit d’Order Promising et proposition de capacités

11 septembre 2026 — Codex. Demande [U87](../connaissance/01-contributions-utilisateur.md#u87), précisée par [U88](../connaissance/01-contributions-utilisateur.md#u88), F191/F192 ; analyse A61 et proposition P83. État examiné : P81 version 0.4, après U86, et alternative D01 P82. Audit documentaire et conceptuel, sans entretien ni vérification de configuration installée.

## Conclusion

**Order Promising constitue un domaine cohérent pour le besoin décrit : déterminer une fourniture possible, s’engager, couvrir la demande par des ressources, puis réexaminer les promesses.** Ses quatre aptitudes actuelles sont recevables, mais leur formulation doit mieux distinguer quantité possible, quantité confirmée et quantité affectée. Une présentation avec quatre noms courts est recommandée ci-dessous, sans ajouter une capacité par calcul ou étape de traitement.

Le domaine visé est confirmé par U88 : Order Promising, repère D03 dans P81. L’examen initial du résiduel D02 est conservé comme audit de frontière utile, pas comme substitut à la demande. Aucun identifiant n’est renuméroté.

## Audit des quatre capacités Order Promising

| Capacité courante | Résultat de l’audit | Proposition |
| --- | --- | --- |
| D03.a — Assess supply feasibility | Résultat métier recevable. Sa définition réunit le stock virtuel mobilisable et la possibilité de fournir quantité/date. Les dates de l’amont, la mise à disposition et les possibilités de service doivent rester explicites ; un simple solde ATP ne suffit pas toujours. | **Supply Feasibility** : conserver ces résultats ensemble tant qu’une séparation utile n’est pas démontrée. |
| D03.b — Confirm a supply promise | Résultat distinct de la faisabilité. La formulation « établir les quantités et dates engagées et distinguer la part restant à couvrir » pouvait confondre confirmation et affectation. | **Confirmation** : distinguer quantité confirmée, non confirmée et couverture par affectation. Ne pas imposer confirmation et affectation simultanées. |
| D02.e — Supply Assignment, rattachée à D03 | Aptitude explicitement reconnue par Laurent. Le verbe affecter doit inclure les évolutions du lien aux ressources, avec les effets cohérents sur les réservations. | **Supply Assignment** : conserver le nom et préciser affectation, réaffectation et libération, sans double compte. |
| D03.c — Reassess supply promises | Besoin étayé par les priorités Boardriders et changements de ressources. Un réexamen ne modifie pas nécessairement une promesse ; le résultat peut aussi être de la maintenir. | **Promise Revision** : réexaminer les promesses et établir les modifications autorisées lorsqu’elles sont nécessaires. |

**Points de vigilance :** le cycle de confirmation et le réexamen se recouvrent partiellement. La distinction est utile à tester car l’arbitrage entre plusieurs demandes et les conséquences de priorités forment un résultat explicite dans U30/U31 ; elle ne justifie pas deux applications. Modifier la ressource affectée peut préserver quantité/date promises ; modifier une promesse ne déplace pas nécessairement le stock physique.

**Couverture plausible à approfondir :** fourniture partielle ou fractionnée, autre origine, changement de date et traitement des demandes non confirmées sont des variantes de faisabilité/confirmation/affectation, pas automatiquement quatre nouvelles capacités. Détection d’une promesse menacée et examen des conséquences sont à inclure dans le périmètre du réexamen ; besoin local détaillé non établi au-delà des cas déjà déclarés. Aucune capacité supplémentaire jugée nécessaire sur les seuls éléments examinés.

## Frontière avec le résiduel D02

D02 Resource Availability and Commitments ne contient plus que deux formulations après les transferts U75. Son autonomie n’est pas justifiée par les cas examinés. Recommandation complémentaire : intégrer la disponibilité de promesse à D03.a et répartir les modifications d’engagement selon l’objet concerné. Cette proposition n’applique aucun retrait de domaine.

## Diagnostic des deux capacités restantes

| Repère et formulation actuelle | Diagnostic | Nom court possible | Traitement recommandé |
| --- | --- | --- | --- |
| D02.a — Determine resource availability for a given use | Aptitude métier recevable, mais recouvrement avec D03.a depuis U81 : stock virtuel mobilisable selon usage et horizon. | Availability | Intégrer la disponibilité de promesse à la faisabilité D03.a. Les positions, états et connaissance du futur restent D01 ; leurs soldes élémentaires ne deviennent pas tous des promesses. |
| D02.d — Adjust resource commitments | Verbe valide mais objet trop générique : réviser une réservation, une protection, une affectation ou une promesse n’a pas le même résultat. | Commitment Adjustment | Répartir les effets entre Reservation, Supply Protection, Supply Assignment et révision de promesse. Ne pas créer une capacité pour le seul fait de modifier un objet. |

Des noms plus courts ne résolvent pas ces recouvrements. Un domaine plus général Supply Commitments serait une autre option de regroupement, mais remettrait en question des frontières déjà travaillées et n’est pas justifié par les récits examinés.

## Épreuve sur les récits et les références existantes

| Cas et provenance | Accueil proposé sans domaine D02 autonome | Limite ou règle à instruire |
| --- | --- | --- |
| Protection marque/canal, vente sur stock et service selon ordre d’arrivée — U10/U30 | D01 Supply Protection et Reservation ; D03 pour la faisabilité et la promesse. | Le principe déclaré ne prouve pas FIFO de lots ni contrôle technique empêchant toute survente. |
| Données de protection recalculées après aléa amont — U10 | D01 Supply Protection pour la règle applicable ; D01/D07 pour le futur, D03 si les promesses sont affectées. | L’objet remplacé par MAP et les effets sur engagements demeurent inconnus. Ne pas internaliser le calcul de planification de saison. |
| Demande non couverte immédiatement, puis ressources futures — U30/U79/U80 | D03 faisabilité, confirmation et Supply Assignment ; ressources connues dans D01, faits amont en adhérence D07. | Une commande peut exister sans couverture ; reliquat contractuel et réception confirmée ne sont pas équivalents. |
| Réaffectation au bénéfice d’une demande prioritaire Boardriders — U30/U31 | Révision de promesse et Supply Assignment en D03, avec effets cohérents sur Reservation D01. | Besoin déclaré, pas configuration installée ; engagements modifiables et sort des demandes dépriorisées à préciser. |
| Refus ou délai de réponse d’un exécutant — U04/U05, C07/C29 | D07 pour la prise en charge ; D01/D03 pour les conséquences éventuelles ; modèle processus pour attente et relance. | Ne pas assimiler expiration d’une tentative et annulation de commande ou libération automatique. |
| Retard, annulation, livraison partielle — tests de robustesse proposés | Mettre à jour les ressources et réviser les engagements concernés. | Ces variantes sont des tests de modèle, pas des récits locaux supplémentaires ; préserver les quantités déjà consommées et éviter doubles libérations. |

Les références résiduelles D02.a/d dans la carte ont aussi été examinées : cas de consolidation, vente, délai d’exécution, aléa amont et deux besoins Boardriders ; raccordements CAP006, CAP007–CAP010, CAP035 ; suggestion sur la fermeté du futur. Elles se répartissent conceptuellement comme ci-dessus, mais les liens courants ne sont pas supprimés avant arbitrage. Aucun cas examiné n’exige à lui seul un domaine D02 distinct ; ce résultat ne prouve pas une couverture exhaustive de l’entreprise.

## Vue proposée dans le style D01

Cette vue répond à U87/U88 pour **Order Promising**, actuellement D03. Elle concrétise les quatre aptitudes auditées et les points d’accueil du résiduel D02. Noms courts, définitions d’aptitudes indépendantes des outils et Finalité ; aucune nouvelle capacité ajoutée.

**Finalité :** déterminer et maintenir les quantités et dates de fourniture réalisables pour les demandes, en mobilisant les ressources présentes ou futures selon les règles applicables.

| Nom proposé | Ce que sait faire l’entreprise | Finalité | Raccordement |
| --- | --- | --- | --- |
| **Supply Feasibility** | Déterminer le stock virtuel mobilisable pour une demande et les quantités et dates possibles, en tenant compte des contraintes d’approvisionnement et d’exécution. | Évaluer ce que l’entreprise peut fournir et quand. | D03.a ; absorption proposée de D02.a pour la promesse. |
| **Confirmation** | Établir les quantités et dates promises, en distinguant ce qui est confirmé, non confirmé et encore non couvert par une affectation. | Donner un engagement explicite au destinataire. | D03.b. |
| **Supply Assignment** | Affecter, réaffecter ou libérer des ressources admissibles présentes ou futures pour couvrir des demandes ou engagements. | Relier les demandes aux ressources qui peuvent les satisfaire. | Repère historique D02.e, déjà situé dans D03 ; part pertinente de D02.d. |
| **Promise Revision** | Réexaminer les promesses lorsque ressources, dates, demandes ou priorités changent et établir les révisions autorisées ainsi que leurs conséquences. | Maintenir la cohérence et la faisabilité des engagements. | D03.c ; part pertinente de D02.d. |

Faisabilité, confirmation et affectation sont des résultats distincts ; aucune séquence obligatoire ni objet unique n’est prescrit. SAP peut les combiner dans une même réalisation. Réviser une promesse peut laisser l’affectation inchangée ; réaffecter une ressource peut préserver la date promise. Promise Revision rend visible l’arbitrage entre demandes illustré par Boardriders, même si sa séparation de Confirmation mérite d’être éprouvée comme toute maille proposée.

**Frontière D01 :** ressources physiques, états logiques et connaissance des ressources futures ; règles de protection et réservations. **Frontière D03 :** calcul de stock virtuel pour la promesse, engagement et couverture des demandes. Disponibilité d’une ressource à l’entrepôt et date livrable au destinataire restent distinctes. **Frontières D06/D07 :** possibilités d’exécution et faits utiles, sans internaliser le transport ou les opérations d’entrepôt hors développement FLOW.

## Appuis et limites de marché

[ELM077](../marche/elements.md#elm077), [CMP046](../marche/comparaisons.md#cmp046), pages officielles ouvertes le 2026-09-11 : SAP Product Availability Check / Backorder Processing et Microsoft Order promising / Inventory Visibility reservations. Les premiers éclairent calcul, confirmation et réexamen ; le cycle de réservation Microsoft inclut déjà ajustement et libération. Ces constats confortent la répartition par résultat et objet métier. Les titres courts proposés restent locaux ; ils ne sont pas présentés comme des feuilles SAP/Microsoft exactes.

Les appuis TM Forum et Guild de l’étude initiale restent partiels ; pas de nouveau catalogue consulté ici. Le nom de D02 n’a pas d’équivalent autonome établi dans notre corpus ; cette absence de preuve ne prouve pas son absence de tous les modèles du marché. Le contenu futur sous contrat, les règles de priorité et les autorités requièrent des précisions locales.

## Statut et mise en œuvre éventuelle

[P83](../connaissance/05-propositions.md#p83) porte la recommandation. Conserver D02.a/d comme traces d’origine dans les correspondances si la répartition est adoptée. Ne jamais réutiliser D02 pour renommer D03 sans décision explicite de convention d’identification. P81 conserve dix domaines et 35 formulations pendant la discussion ; les CAP historiques sont inchangées. Le présent audit ne valide ni le retrait de D02 ni les noms proposés pour Order Promising. U88 confirme le domaine visé, pas la proposition finale.

**Complément U89 — 2026-09-11 :** la [comparaison de noms, nature et couverture](../marche/order-promising-comparaison-capacites.md), A62/CMP047, étend l’épreuve aux alternatives, contrôles d’allocation et création d’approvisionnement. Les quatre aptitudes restent un point de départ ; cet audit ne démontre pas leur couverture de tous les comportements du marché.

**Suite U90 :** les nouveaux candidats Promise Verification et Promise Confirmation sont dans la [vue courante](../connaissance/25-domaines-coeur-et-epreuve-recits.md#proposition-de-présentation-u87u88). Les noms Supply Feasibility et Confirmation ci-dessus sont ceux de l’audit initial ; historique C59, appuis CMP048. Les réserves de couverture U89 sont conservées.

**Décision U95 — 2026-09-11, Laurent :** la liste courante de neuf capacités d’Order Promising est validée dans [P83](../connaissance/05-propositions.md#p83) et la carte version 0.5. Cet audit conserve son état initial à quatre propositions et ne constitue pas une nouvelle épreuve des neuf capacités. CTP reste au glossaire, placement différé ; les frontières détaillées demeurent à préciser. C63/CMP052.

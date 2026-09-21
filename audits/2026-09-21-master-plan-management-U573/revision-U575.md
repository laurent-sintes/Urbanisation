# Application du Master Plan — révision U575

**Planning Management** remplace Planning Request Management dans la proposition, selon l’instruction explicite de Laurent. Le nom change ; le comportement conserve le cadrage et le pilotage du travail de planification. La [nouvelle annexe](../../modeles/backlog/master-plan-application-U575.yaml) porte la proposition courante ; l’étude U573/U574 conserve les preuves et la structure antérieure.

Je recommande de regrouper les six comportements d’application proposés en **Master Plan Application** : faire appliquer les recommandations autorisées du Master Plan retenu, mobiliser les capacités responsables, puis établir ce qui a effectivement été pris en compte et les écarts.

Supply Assignment décrivait seulement les liens entre ressources et besoins. L’application du Master Plan est plus large : elle reprend ces affectations, les modifications des échéanciers et engagements, les suites sur les achats et transferts et les ajustements de politiques retenus. Il s’agit d’une consolidation de responsabilités, pas d’un simple renommage de Supply Assignment.

| Résultat que le plan fait appliquer | Exemples conservés | Responsabilité mobilisée |
| --- | --- | --- |
| Liens ressources-besoins | Affecter, compléter ou réaffecter des ressources aux commandes **et aux prévisions identifiées** | Contenu de D02.e repris dans l’application |
| Structure et engagements de satisfaction | Fractionner une commande, confirmer une partie, modifier un échéancier | Order Structuring, Order Splitting, Fulfillment Commitment |
| Approvisionnements | Créer, avancer, reporter, augmenter, réduire ou annuler un achat ou transfert selon autorisation | Purchase Order, Transfer Order, Order Lifecycle Management |
| Politiques applicables | Prendre en compte une nouvelle cible de stock ou une protection retenue | Supply Protection |

Ces catégories expliquent le comportement et ses coopérations. Elles ne deviennent ni des sous-comportements ni des plannings autonomes. Les décisions qui déterminent le contenu du plan restent distinctes ; la configuration en vigueur et les engagements gardent leurs responsables. Une application partielle ne vaut pas application réussie de tout le plan et peut demander un réexamen.

La proposition de capacité Master Plan Management comporte ainsi **six comportements directs** :

- **Planning Management** : cadrer, lancer, programmer, arrêter et relancer le travail de planification.
- **Simulation & Analysis** : construire et comparer les alternatives.
- **Plan Authorization** : retenir un scénario et autoriser ses recommandations.
- **Plan Version Management** : identifier la référence et conserver les variantes et révisions utiles.
- **Master Plan Application** : faire appliquer les recommandations autorisées et constater leurs effets.
- **Plan Monitoring & Replanning** : suivre la pertinence du plan et le réviser face aux écarts et impondérables.

Le suivi de l’application établit le résultat de sa mise en effet ; le suivi du plan réexamine ensuite sa pertinence face aux nouvelles conditions. Ces comportements sont combinables, sans séquence obligatoire ni validation humaine systématique.

Oracle documente une release commune aux recommandations de création, replanification et annulation, avec suivi des demandes non traitées. Cet appui reste partiel : il ne prouve pas à lui seul l’application de toutes les politiques et affectations FLOW. [Oracle 26B — Manually Release Plan Recommendations](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faupc/manually-release-plan-recommendations.html), ELM566.

Microsoft documente le firming, qui transforme les Planned Orders en Orders et en conserve l’historique. C’est également un périmètre plus étroit que l’application globale proposée. [Microsoft — Maintain planned orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/maintain-planned-orders), ELM588. Les deux sources primaires ont été relues le 21 septembre 2026. Le nom Master Plan Application et sa maille sont proposés par cohérence du modèle, sans équivalence de catalogue ni standard universel revendiqué.

La recommandation corrige la décomposition U573/U574 : des catégories d’effets différentes ne suffisent pas à justifier des comportements distincts au niveau landscape. L’ambiguïté d’Allocation signalée par Laurent est conservée ; les intitulés Order Allocation & Reallocation et Forecast Supply Allocation ne sont plus proposés comme comportements autonomes.

Seul le nom Planning Management est explicitement adopté en U575. La consolidation en Master Plan Application et les formulations détaillées restent proposées. Les onze cas d’action de l’étude sont conservés, notamment le cas avant commande ; ni hiérarchie canonique ni publication modifiées.

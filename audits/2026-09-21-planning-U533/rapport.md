# Audit landscape — Planning et décisions Supply

21 septembre 2026 — U533, complété par U534–U536. Sources structurées : [matrice et constats](../../modeles/backlog/planning-model-audit-U533.yaml).

## Précision de découpage U537–U538

**L’application du plan relève d’un comportement du Planning ; les configurations qu’il consomme restent portées par des capacités extérieures.** Supply Protection conserve donc sa responsabilité propre. Le réexamen a abouti en U539–U541 : Supply Assignment est désormais un comportement de Order Backlog Planning. Les trois responsabilités décrites plus bas représentent l’état antérieur du catalogue, pas un triptyque de capacités imposé. Les mécanismes BHV045–047 sont conservés comme modalités descriptives, avec leurs preuves historiques. Voir [l’audit transversal et le résultat courant](../2026-09-21-planning-principle-U540/rapport.md).

[Analyse, sources et portée](../../modeles/backlog/plan-application-review-U537.yaml), CMP220. Le rapprochement Oracle étaye application des résultats et consommation de règles ; leur rattachement dans FLOW reste un choix de modélisation. Aucun consensus ni innovation déduit de la documentation produit.

## Résultat

**Planning est intégrée sous Supply Chain Orchestration. Demand Planning et une capacité de couverture Supply ont été ajoutées ; le nom et le périmètre de cette seconde capacité sont désormais en réexamen selon U534.** L’audit recommande de conserver les décisions existantes dans leurs Areas spécialisées. Une décision appartient au périmètre du résultat qu’elle détermine, même lorsque plusieurs plans la mobilisent.

Audit des **56 capacités antérieures, dont 16 décisions**, avec lecture des responsabilités et examen structurel des **367 relations**. État résultant : **58 capacités et 369 relations**. Les 56 capacités antérieures sont conservées à l’identique. Pas de réouverture de l’audit des Behaviors U431, pas de règles détaillées, pas de vérification des systèmes installés.

L’accord U533 couvre le regroupement Planning, Demand Planning et la seconde capacité présentée, leurs noms et responsabilités courtes à la portée de la réponse validée. U534 rouvre le nom et le périmètre Supply Planning ; cette réserve prime sur une approbation courante non qualifiée. L’accord historique est conservé. Les conclusions de cet audit restent des recommandations.

## Réponse au placement des décisions

| Résultat de décision | Area recommandée | Motif |
| --- | --- | --- |
| Cibles, protections, apports, redistribution, réservation et devenir des retours | Inventory Optimization | Responsabilités spécialisées réutilisables dans plusieurs plans et situations opérationnelles. |
| Faisabilité, compromis économique et échéancier de promesse | Order Promising | Déterminer la promesse reste distinct de prévoir une demande ou préparer des apports. |
| Priorités et plan collectif d’affectation aux Orders | Fulfillment Optimization | Répartir les ressources du carnet, sans reprendre la prévision ou le plan d’achat fournisseur. |
| Prestations requises, choix des services et adaptation aux impondérables | Process Management | Déterminer les choix du plan d’exécution. |
| Demande de référence à retenir et couverture d’ensemble | Planning, si ces décisions sont distinguées | Responsabilités candidates propres aux nouveaux plans ; noms et décomposition à instruire, pas de création automatique. |

**Inventory Planning** reste le principal chevauchement : je recommande de le conserver comme planification spécialisée des scénarios de stock dans Inventory Optimization, en précisant ce que le plan d’ensemble lui demande et reçoit. Un déplacement n’est pas justifié par le seul mot Planning. Ce choix reste à arbitrer.

## Assignment Planning et portée de Supply Planning

U535 décrit la distribution de ressources limitées aux commandes de vente selon promesse, profit et équilibre/optimisation du stock. Le modèle possède déjà trois responsabilités complémentaires : **Order Backlog Planning** construit et compare les scénarios ; **Fulfillment Plan Decision** détermine un scénario collectif ; **Supply Assignment** applique les affectations. Les décisions de promesse et de stock contribuent à ce compromis.

**Recommandation : traiter Assignment Planning comme une clarification ou un candidat de nom pour Order Backlog Planning, sans créer une capacité concurrente.** La proposition de Laurent vise les ventes ; le périmètre courant couvre un carnet d’Orders plus large. Cette différence doit être arbitrée avant tout renommage. U528 maintient ce planning dans l’opérationnel, sous Fulfillment Optimization.

SAP Supply Planning couvre achats, production et distribution : le nom est effectivement large. Si D17.b doit porter le plan d’ensemble de couverture, il reste pertinent ; si elle porte seulement les futurs apports fournisseurs, un nom de procurement est à étudier. Procurement Planning est attesté, mais les documents consultés ne donnent pas un périmètre exactement équivalent au besoin textile. Aucun remplacement lexical automatique.

## Ce que démontre le marché

| Source | Appui utile | Limite |
| --- | --- | --- |
| [Oracle — Plan Types](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faupc/overview-of-supply-chain-planning-plan-types.html) | Plans de demande, Supply et plan intégré ; backlog distingué. | Types de plans, pas prescription des Areas FLOW. |
| [SAP — Inventory optimisation](https://www.sap.com/uk/products/scm/integrated-business-planning/features/inventory-optimization.html) | Cibles de stock utilisées par la planification Supply. | Ne prescrit pas le parent exact des décisions FLOW. |
| [Oracle — Backlog Management Processes](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faubm/overview-of-backlog-management-processes.html) | Planification, revue et simulation avant publication opérationnelle. | Pas preuve d’un optimum conjoint promesse/profit/stock. |
| [SAP — Supply Assignment Run Workflow](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9905622a5c1f49ba84e9076fc83a9c2c/863bbfb47d384f6aafff5347fb7e3dba.html) | Priorisation en pénurie, comparaison des simulations d’affectation. | Texte primaire indexé consulté, page directe initiale vide ; ventes et transferts. |
| [Oracle — Key Order Attributes](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faubm/key-order-attributes.html) | Dates, retards, revenus et marges du carnet. | Mesures disponibles ne prouvent pas un optimiseur multiobjectif. |
| [Oracle — Import Planned Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fascp/import-planned-orders.html) | Articulation recommandations de plans / promesse / Orders. | Hypothèse Oracle d’admissibilité des apports planifiés non adoptée. |
| [SAP — Supply Planning](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/c1fb60cb1e9c49d99ada277ae57e9e6c/66a038fcf40f4f779c6b4696aede83a6.html) | Périmètre achats, production et distribution. | Passage primaire indexé seulement ; portée produit. |

Les références et versions complémentaires sont conservées dans la matrice YAML. **Aucune innovation n’est revendiquée par défaut.** Demand Planning et Supply Planning sont des termes établis ; les simulations d’affectation sont documentées. Le libellé exact Assignment Planning et la séparation fine des décisions sont des propositions/adaptations FLOW. L’optimisation conjointe promesse–profit–stock n’est pas démontrée par les passages consultés ; son caractère innovant ne l’est pas davantage.

## Constats à traiter

### PA01 — Articuler Inventory Planning et Supply Planning

**Constat :** D05.f construit déjà des scénarios mobilisant cibles, protections, implantation, réassort et redistribution ; D17.b ajoute le plan de couverture d’ensemble.

**Recommandation :** Conserver D05.f comme planification spécialisée du stock, mobilisée par Supply Planning. Définir les résultats respectifs pour éviter deux scénarios applicables concurrents. Aucun transfert ni fusion automatique.

Cibles : D05.f, D17.b. Appuis : U533, ELM560, ELM552. Statut : proposition à instruire.

### PA02 — Qualifier les décisions propres aux deux nouveaux plans

**Constat :** Aucune des 16 décisions existantes ne porte explicitement le choix de demande de référence ni le compromis de couverture d’ensemble avant commandes. Les deux nouvelles capacités assurent leur construction/actualisation à maille large ; les porteurs des résultats de décision restent implicites.

**Recommandation :** Étudier Demand Plan Decision et Supply Plan Decision comme responsabilités candidates dans Planning, si leur résultat distinct justifie des capacités. Ne pas créer une décision par calcul ni déplacer les décisions de stock pour combler ce point.

Cibles : D17.a, D17.b. Appuis : U533, ELM557, ELM562, ELM552. Statut : proposition à instruire.

### PA03 — Couvrir explicitement les achats anticipés du réseau

**Constat :** Initial Stocking Decision vise le stock de départ des magasins ; Replenishment Decision vise les apports continus. Leur réunion ne démontre pas une responsabilité explicite de tout le plan d’achat fournisseur initial du réseau illustré par MAP.

**Recommandation :** Inclure ce besoin dans l’étude du résultat de couverture de Supply Planning/Supply Plan Decision ; articuler ensuite les demandes avec Purchase Order. Ne pas étendre Initial Stocking Decision par simple analogie de lancement.

Cibles : D17.b, D05.g, D05.e, D04.j. Appuis : U530, U533, ELM561, ELM552. Statut : proposition à instruire.

### PA04 — Distinguer scénario, demande planifiée, engagement et ressource future

**Constat :** Un plan peut recommander un apport avant sa prise en charge opérationnelle. Le modèle possède les responsabilités de commandes, de connaissance et de promesse, mais l’interface de D17 est nouvelle.

**Recommandation :** Qualifier le passage vers les Orders et le retour de prise en compte ; définir quelles ressources futures sont utilisables pour les promesses. Une hypothèse ne devient ni stock certain ni engagement par le seul recalcul.

Cibles : D17.b, D04.j, D04.o, D01.c, D03.i, D03.n, D02.c. Appuis : U533, ELM561. Statut : proposition à instruire.

### PA05 — Relier demande connue, ventes et prévisions sans confusion

**Constat :** MAP mobilise ventes et précommandes B2B ; le modèle n’explicite pas encore toutes les responsabilités d’alimentation du nouveau plan.

**Recommandation :** Identifier les informations et responsabilités sources au niveau capacité. Garder les statuts B2B, distinguer ventes et commandes, rendre cohérentes demande connue et anticipation. Ne pas faire des prévisions une ressource Core Data ni inventer les flux MAP.

Cibles : D17.a, D04.i, business-references. Appuis : U531, U532, U533, ELM558, ELM556. Statut : proposition à instruire.

### PA06 — Formaliser les relations métier de Planning

**Constat :** L’intégration ajoute deux relations contains, sans transférer les relations existantes. Les liens transversaux des nouvelles capacités restent à qualifier.

**Recommandation :** Consigner des liens de coopération avec conditions, effets et provenance ; les relations proposées ci-dessous ne sont pas des décompositions et ne sont pas ajoutées automatiquement au canonique par l’audit.

Cibles : D17.a, D17.b, D05, D04, D01, D06, D15, business-references. Appuis : U533. Statut : proposition à instruire.

### PA07 — Corriger les anciennes exclusions générales de planification

**Constat :** Le scope de Fulfillment Plan Decision parle encore de planification globale externe. Les restrictions locales de saison/horizon dans Inventory Planning et D05 doivent être relues comme limites de ces responsabilités, pas comme exclusion du Domain.

**Recommandation :** Remplacer le repère externe par la distinction avec le plan d’ensemble dans Planning. Préciser les frontières D05/D17 selon les résultats, sans supprimer automatiquement les limites spécialisées.

Cibles : D03.o, D05.f, D05. Appuis : U530, U531, U533. Statut : proposition à instruire.

### PA08 — Réexaminer le périmètre trop large de Supply Planning

**Constat :** U534 met le nom en réserve. SAP Supply Planning couvre achats, production et distribution ; le besoin MAP discuté porte notamment les achats fournisseurs.

**Recommandation :** Conserver D17.b comme capacité de travail à qualifier. Si son résultat couvre tout le réseau, Supply Planning reste cohérent ; si le résultat vise les apports fournisseurs, étudier un nom de procurement en vérifiant son périmètre. Ne pas adopter Procurement Planning sur une simple proximité lexicale.

Cibles : D17.b. Appuis : U534, ELM564, ELM565, ELM561. Statut : proposition à instruire.

### PA09 — Assignment Planning recouvre un ensemble existant

**Constat :** U535 vise la répartition des ressources limitées aux commandes de vente avec compromis promesse/profit/stock. D03.p organise déjà les scénarios, D03.o détermine un plan collectif et D02.e en applique les affectations.

**Recommandation :** Traiter Assignment Planning comme une clarification ou un candidat de nom pour D03.p, pas comme une nouvelle capacité. Conserver le rattachement opérationnel U528. Le périmètre ventes seules de U535 est plus étroit que le carnet d’Orders actuel et doit être arbitré avant tout renommage.

Cibles : D03.p, D03.o, D02.e, D15, D05. Appuis : U535, U536, ELM496, ELM381, ELM563. Statut : proposition à instruire.

### PA10 — Étayer le compromis promesse/profit/stock sans revendiquer une innovation non démontrée

**Constat :** Oracle documente dates et marges, SAP des simulations d’affectation et des cibles de stock. Les passages consultés ne démontrent pas une optimisation unifiée des trois dimensions.

**Recommandation :** Rendre explicites dans la proposition les objectifs et décisions mobilisées, sans pondération imposée. Qualifier ce rapprochement d’adaptation FLOW justifiée par le besoin et la séparation des responsabilités ; ne revendiquer ni standard complet ni innovation exclusive. Une innovation éventuelle exige un bénéfice distinct et une comparaison complémentaire.

Cibles : D03.o, D03.p, D03.k, D05.a, D05.d, D05.c. Appuis : U535, U536, ELM563, ELM381, ELM560. Statut : proposition à instruire.

## Matrice exhaustive des capacités antérieures

La matrice détaille les responsabilités conservées. Les références et empreintes des champs examinés sont dans le YAML ; les sources marché n’ont pas été réauditées exhaustivement pour les capacités hors impact.

| ID | Capacité | Area ou référentiel actuel | Conclusion |
| --- | --- | --- | --- |
| D01.f | Inventory Tracking | Inventory Management | Conserver la responsabilité actuelle de gestion, de faits ou de réalisation. L’ajout du plan d’ensemble n’apporte pas de motif de transfert ; les résultats peuvent contribuer au contexte des plans. |
| D01.g | Record Inventory Movements | Inventory Management | Conserver la responsabilité actuelle de gestion, de faits ou de réalisation. L’ajout du plan d’ensemble n’apporte pas de motif de transfert ; les résultats peuvent contribuer au contexte des plans. |
| D01.c | Inventory Visibility | Inventory Management | Connaissance du stock et ressources futures, avec statut et fraîcheur pour les scénarios. |
| D01.d | Stocktaking | Inventory Management | Conserver la responsabilité actuelle de gestion, de faits ou de réalisation. L’ajout du plan d’ensemble n’apporte pas de motif de transfert ; les résultats peuvent contribuer au contexte des plans. |
| D02.b | Supply Protection | Inventory Management | Gouverne et applique les politiques ; un scénario de protection n’est pas une politique en vigueur. |
| D02.c | Reservation | Inventory Management | Engagement de ressource distinct du plan et de l’affectation ; aucune réservation par simple hypothèse de couverture. |
| D02.e | Supply Assignment | Fulfillment Optimization | Applique les affectations aux commandes ; les besoins prévisionnels historiques restent à clarifier, sans assimilation à un Order. |
| D03.i | Available-to-Promise (ATP) | Order Promising | Possibilités de promesse ; un plan Supply ne suffit pas à rendre une ressource admissible. |
| D03.j | Capable-to-Promise (CTP) | Order Promising | Faisabilité de satisfaction sous adaptation ; mobilise déjà les décisions spécialisées sans les absorber. |
| D03.k | Profitable-to-Promise (PTP) | Order Promising | Arbitrage économique de promesse, pas arbitrage économique de tout plan d’entreprise. |
| D03.l | Delivery Schedule Decision | Order Promising | Échéancier de satisfaction des commandes ; différent des dates d’approvisionnement d’ensemble. |
| D03.m | Order Prioritization | Fulfillment Optimization | Priorités relatives des commandes, distinctes de la demande anticipée et des objectifs de plan. |
| D04.i | Sales Order | Service Requests | Fournit les demandes connues avec leurs statuts ; une précommande ne devient pas ferme par son utilisation dans le plan. |
| D04.j | Purchase Order | Service Requests | Porte les demandes/commandes d’achat et leur suivi ; planification et émission/affermissement doivent être articulés. |
| D04.k | Transfer Order | Service Requests | Porte les demandes de transfert issues des suites autorisées du plan. |
| D04.l | Customer Return | Service Requests | Conserver la responsabilité actuelle de gestion, de faits ou de réalisation. L’ajout du plan d’ensemble n’apporte pas de motif de transfert ; les résultats peuvent contribuer au contexte des plans. |
| D04.m | Supplier Return | Service Requests | Conserver la responsabilité actuelle de gestion, de faits ou de réalisation. L’ajout du plan d’ensemble n’apporte pas de motif de transfert ; les résultats peuvent contribuer au contexte des plans. |
| D04.n | Order Structuring | Service Requests | Conserver la responsabilité actuelle de gestion, de faits ou de réalisation. L’ajout du plan d’ensemble n’apporte pas de motif de transfert ; les résultats peuvent contribuer au contexte des plans. |
| D04.o | Order Lifecycle Management | Service Requests | Autorise et applique les transitions des Orders ; la révision d’un plan ne modifie pas silencieusement un engagement. |
| D05.a | Inventory Target Decision | Inventory Optimization | Cibles et seuils de stock, réutilisés par plan d’ensemble, scénarios de stock et réponses opérationnelles. |
| D05.d | Group Protection Decision | Inventory Optimization | Enveloppes et droits de groupes ; leur fixation reste distincte du plan global et de leur application. |
| D05.g | Initial Stocking Decision | Inventory Optimization | Apports de lancement des magasins ; ne couvre pas à elle seule le plan initial d’achat fournisseur du réseau. |
| D05.e | Replenishment Decision | Inventory Optimization | Apports continus et ajustements opérationnels ; Planning peut simuler leur résultat sans reprendre l’autorité de décision. |
| D05.c | Stock Redistribution Decision | Inventory Optimization | Déplacements du stock déjà existant ; décision de rééquilibrage mobilisable dans les scénarios. |
| D05.f | Inventory Planning | Inventory Optimization | Conserver comme planification spécialisée des scénarios de stock dans D05 ; expliciter ce que Supply Planning lui demande et reçoit, sans deux propriétaires du même scénario. |
| D06.b | Service Capacity Visibility | Process Management | Capacités opérationnelles contextualisées fournies par les exécutants ; ne les confondre ni avec référence configurée ni avec capacité future hypothétique. |
| D07.a | Service Requirements Decision | Process Management | Prestations requises pour satisfaire le besoin ; utilisables pour éprouver les scénarios sans transfert de responsabilité. |
| D07.b | Backing Service Orders | Process Management | Conserver la responsabilité actuelle de gestion, de faits ou de réalisation. L’ajout du plan d’ensemble n’apporte pas de motif de transfert ; les résultats peuvent contribuer au contexte des plans. |
| D07.c | Service Reconciliation | Process Management | Conserver la responsabilité actuelle de gestion, de faits ou de réalisation. L’ajout du plan d’ensemble n’apporte pas de motif de transfert ; les résultats peuvent contribuer au contexte des plans. |
| D07.d | Operations Tracking | Process Management | Faits, jalons et estimations alimentent l’actualisation sans transformer un attendu en réalisé. |
| D09.d | Party / Role Ingestion | Party / Role | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D11.a | Agreement Ingestion | Agreement | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D08.d | Product Reference Ingestion | Product Reference | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D12.a | Product Catalog Ingestion | Product Catalog | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D13.a | Fulfillment Network Ingestion | Fulfillment Network | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D06.d | Process Orchestration | Process Management | Conserver la responsabilité actuelle de gestion, de faits ou de réalisation. L’ajout du plan d’ensemble n’apporte pas de motif de transfert ; les résultats peuvent contribuer au contexte des plans. |
| D14.a | Service Catalog Ingestion | Service Catalog | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D06.e | Service Selection Decision | Process Management | Services et exécutants à mobiliser pour des prestations ; ne décide pas toute la couverture fournisseur d’un plan Supply. |
| D06.f | Process Adaptation Decision | Process Management | Adaptation du plan d’exécution aux impondérables ; les conséquences remontent aux plans sans changer son parent. |
| D03.n | Fulfillment Commitment | Order Promising | Engagements de satisfaction et révisions, distincts des hypothèses du plan. |
| D05.h | Reservation Policy Decision | Inventory Optimization | Conditions de réservation ; mise en vigueur et engagements individuels restent ailleurs. |
| D04.q | Order Archiving | Service Requests | Conserver la responsabilité actuelle de gestion, de faits ou de réalisation. L’ajout du plan d’ensemble n’apporte pas de motif de transfert ; les résultats peuvent contribuer au contexte des plans. |
| D03.o | Fulfillment Plan Decision | Fulfillment Optimization | Scénario collectif d’affectation aux commandes ; ni plan d’achat anticipé ni nouveau plan global. |
| D05.i | Return Disposition Decision | Inventory Optimization | Devenir logistique des retours ; effets possibles sur les ressources futures, sans finalité de plan global. |
| D04.r | Consignment Replenishment Order | Service Requests | Porte les demandes d’apport consignées, sans les assimiler à des achats. |
| D01.h | Consigned Inventory Management | Inventory Management | Conserver la responsabilité actuelle de gestion, de faits ou de réalisation. L’ajout du plan d’ensemble n’apporte pas de motif de transfert ; les résultats peuvent contribuer au contexte des plans. |
| D03.p | Order Backlog Planning | Fulfillment Optimization | Order Backlog Planning reste opérationnel selon U528 ; il peut consommer le contexte du plan d’ensemble sans rejoindre D17. |
| D04.s | Order Backlog Optimization Request | Service Requests | Demande de réexamen du carnet ; ne sert pas automatiquement de demande générique de révision du plan Supply. |
| D08.e | Product Reference Visibility | Product Reference | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D09.e | Party / Role Visibility | Party / Role | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D11.b | Agreement Visibility | Agreement | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D12.b | Product Catalog Visibility | Product Catalog | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D13.b | Fulfillment Network Visibility | Fulfillment Network | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D14.b | Service Catalog Visibility | Service Catalog | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D16.a | Assortment Ingestion | Assortment | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |
| D16.b | Assortment Visibility | Assortment | Les références utiles restent gérées dans Authoritative Data ; les besoins de lecture Planning sont à préciser, sans y stocker les prévisions comme données maîtres. |

## Arbitrages prioritaires

1. Préciser le résultat de D17.b : plan d’ensemble de couverture ou plan des apports fournisseurs, puis retenir son nom.
2. Clarifier Assignment Planning par rapport à Order Backlog Planning : périmètre des ventes ou de tous les Orders, sans doublon.
3. Définir l’articulation entre plan d’ensemble et scénarios spécialisés d’Inventory Planning.
4. Qualifier les décisions propres aux nouveaux plans et les interfaces vers les commandes, la promesse et la connaissance des ressources.

Les liens de coopération candidats sont qualifiés dans l’annexe. Ils ne deviennent pas des relations de décomposition. Les prévisions et les scénarios ne sont pas ajoutés au catalogue Core Data. Aucune release, aucun commit ni push effectués.


**Suite U539–U541 :** [audit transversal du principe](../2026-09-21-planning-principle-U540/rapport.md). Supply Assignment est désormais un comportement de Order Backlog Planning ; les compteurs et états décrits plus haut sont ceux de l’audit U533. La question de son maintien autonome est tranchée dans cette portée, tandis que Supply Planning reste en réexamen nominal.

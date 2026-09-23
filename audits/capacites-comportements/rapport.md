# Audit courant des capacités et comportements

État examiné le 23 septembre 2026 — demande U628, précision U629.

**Diagnostic : la consolidation de la hiérarchie est plus avancée que celle des contenus.** L'arbre et les types sont renseignés et cohérents avec les contrats techniques. Les reprises prioritaires concernent le plan commun, la propagation des nouvelles frontières dans les fiches et les liens, puis la précision des justifications marché. Le volume de références est conséquent ; il ne garantit pas leur adéquation au périmètre actuel.

Ce document est le dossier de travail courant de cet audit, destiné à préparer les arbitrages. Il ne remplace pas le catalogue YAML et ne constitue pas un nouvel accord. Le diagnostic initial n’a modifié ni modèle canonique ni publication. Depuis l’accord U631, le regroupement du Planning et la responsabilité Apply Plan sont appliqués au backlog ; les publications restent inchangées. L’accord U632 applique ensuite les cinq comportements de pilotage, avec leurs noms, définitions, frontières et type ; [portée et mise en œuvre](../../modeles/backlog/planning-pilotage-U632.yaml). Le suivi et l’ajustement restent à détailler. L'audit historique U431 conserve sa clôture.

## Périmètre et méthode

Source de l’audit initial, avant U631 : [backlog de travail](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml>), état `as_of: 2026-09-22`, empreinte SHA-256 `e2ecab9d8b5dfe6020180d67a37eb0d4ba1985ea8188912336ee1170ea8dd32a`.

Le cadre appliqué est Domain → Purpose / Finalité → Capability → Behavior, selon U624 et la [consolidation U626](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model-consolidation-U626.yaml>). Les codes et préfixes historiques ne déterminent pas les parents. Les sept référentiels restent des sujets de présentation sous Reference & Policy Management.

Contrôle de toutes les capacités et de tous les comportements : rattachements, types, définitions, présence des justifications de décomposition et structure des comparaisons. Lecture approfondie des périmètres sur les regroupements, nouvelles capacités, planifications, promesse, stocks, consignation et prestations. Contrôle des liens explicites et recherche des formulations résiduelles. Les 326 entrées marché ont été contrôlées formellement ; la vérification de leur pertinence documentaire est ciblée, avec 14 documents primaires relus en ligne et un document SAP tenté sans texte exploitable. Cet audit n'est donc pas une recertification sémantique individuelle des 326 correspondances.

Ce périmètre porte sur le catalogue métier courant, pas sur la réalisation installée dans les SI. Aucune couverture Beaumanoir, Boardriders ou Sarenza n'est déduite des fiches ou des références produits.

## Résultats d'ensemble

| Finalité | Capacités | Comportements |
| --- | ---: | ---: |
| Reference & Policy Management, sept référentiels compris | 17 | 4 |
| Demand Management | 12 | 37 |
| Inventory Management | 6 | 6 |
| Fulfillment Orchestration | 8 | 4 |
| Demand & Supply Optimization | 15 | 29 |
| Supply Management | 1 | 0 |
| **Total** | **59** | **80** |

- Aucun parent manquant ou multiple parmi ces 139 éléments ; aucun sous-comportement.
- 23 capacités décomposées, toutes avec une justification. Les 36 autres ne sont pas réputées incomplètes pour ce seul motif.
- Toutes les fiches ont un type. Capacités : 17 Action, 16 Decision, 12 Knowledge, 7 Management, 3 Planning, 3 Policy, 1 Orchestration. Les 80 comportements utilisent les sept formes méthodologiques.
- Toutes les fiches ont au moins deux documents distincts selon la normalisation du projet : 326 comparaisons, 165 URL documentaires distinctes. Le décompte ne vérifie pas, à lui seul, la qualité primaire ou la pertinence de chaque document.
- 23 fiches n'utilisent qu'un seul organisme. Cela respecte la règle des deux documents, sans établir de consensus interéditeurs.
- Le contrôle `validate_urbanism`, avec schéma, glossaire et sources du backlog courant, ne relève aucune erreur. Ce résultat vérifie les contrats, pas la justesse métier.

| Axe | Appréciation | Priorité |
| --- | --- | --- |
| Classement | Arbre solide ; gestion du plan commun et quelques coopérations restent insuffisamment matérialisées | Haute |
| Types | Exhaustifs ; frontière Action / Management à rendre plus discriminante pour les Orders | Moyenne |
| Contenus | Riches mais inégaux ; noms élargis, descriptions brèves et anciennes attributions subsistent | Haute |
| Cohérence | Principes explicites ; leur déclinaison dans certaines fiches et certains liens est inachevée | Haute |
| Manques | Surtout responsabilités et conditions à expliciter ; quelques décompositions candidates déjà étudiées | Haute |
| Références au marché | Bonne couverture documentaire ; attribution, adéquation de maille et synthèse à reprendre localement | Haute ciblée |

## Constats et recommandations

### A01 — Le plan commun est posé, sa gestion reste répartie entre deux héritages

**Statut courant : regroupement appliqué U631 ; décomposition détaillée en cours de construction.** Le constat ci-dessous décrit l’état initial.

**Constat, priorité haute.** [D05.f](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:6507>) se nomme Demand & Supply Optimization Planning mais définit toujours des plans d'ajustement des stocks. Ses comportements restent Scenario Construction, Simulation & Analysis, Scenario Execution Adaptation et Inventory Plan Application. [D03.p](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/common-planning-U631.yaml>) conserve un travail principalement centré sur les affectations, avec son étude, son autorisation et son application propres.

Les deux fiches précisent qu'elles contribuent à un même plan et se réconcilient avant application : **elles ne prescrivent donc pas deux plans finaux concurrents**. En revanche, la responsabilité qui maintient la référence commune, arbitre leur divergence et constate la prise en compte des effets combinés reste insuffisamment identifiable à cette maille. D03.o coordonne explicitement le scénario collectif, mais sa sortie reste décrite comme un Supply Assignment Plan.

**Recommandation.** Reprendre la proposition de gestion du plan commun, puis décider de la succession de D03.p / D05.f et de leurs comportements, sans fusionner les décisions spécialisées. Définir un cas d'épreuve : un même plan propose un achat, un transfert et une révision de protection ; le transfert est accepté, l'achat refusé. Quelle référence reste applicable et qui la révise ? Les annexes [U575–U578](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/master-plan-application-U575.yaml>) contiennent déjà du travail utile, dont Apply Plan ; leurs formulations détaillées ne sont pas globalement adoptées. Appuis marché M01 ci-dessous.

### A02 — Trois comportements portent des noms plus larges que leur responsabilité

**Constat, priorité haute.** [BHV026](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:12648>), [BHV027](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:12775>) et [BHV028](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:12909>) se nomment Store, Distribution Center et Multi-Echelon **Demand & Supply Optimization**. Leurs définitions déterminent des objectifs et seuils de stock ; leur parent reste Inventory Target Decision. Ces noms suggèrent une couverture plus large que le service décrit.

**Recommandation.** Conserver le périmètre de détermination des cibles et réexaminer les noms à cette maille ; les formulations antérieures en Inventory Optimization sont des candidats justifiables. Un élargissement réel nécessiterait de redéfinir la responsabilité et son parent. Il ne découle pas du seul nom de la finalité. M02 vérifie précisément le cas multi-échelons ; les fiches magasin et centre de distribution nécessiteront leur comparaison propre avant renommage.

### A03 — Quinze fiches conservent une attribution ambiguë de la faisabilité de promesse

**Constat, priorité haute.** La phrase « D04 porte possibilités et engagements de promesse » apparaît encore dans D04.i, D04.k, D01.h et BHV063 à BHV074. Les décisions ATP, CTP, PTP et Delivery Schedule Decision sont pourtant rattachées à D03 ; D04 porte Fulfillment Commitment. La phrase mélange établissement des possibilités et tenue de l'engagement.

**Recommandation.** Corriger cette attribution dans les 15 périmètres : Optimization établit les résultats de faisabilité et les arbitrages ; Demand porte proposition, confirmation, révision et mutations autorisées. Il s'agit d'aligner la rédaction sur la structure présente, pas de déplacer les capacités. Le même examen doit repérer les raccourcis historiques voisins, notamment dans D04.n.

### A04 — Les nouvelles coopérations ne sont pas toutes explicites à la maille capacité

**Constat, priorité moyenne.** [Supply Visibility D18.a](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:23634>), [Service Provider Policy D19.a](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:23734>), [Demand Protection Policy D19.b](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:23821>) et [Consignment Pick-up Order D04.t](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:23909>) n'ont aucune relation métier incidente hors hiérarchie. Leurs descriptions mentionnent pourtant des coopérations. Pour Supply, deux liens existent déjà au niveau Purpose, vers Inventory et Optimization : ce n'est pas une absence totale d'interaction.

**Recommandation.** Qualifier les coopérations utiles à la lecture des fiches : apports attendus et projections ; restrictions de recours et sélection du prestataire ; protections de demandes et classement/révision ; reprise de consignation et régime de stock/prestations. Choisir explicitement la maille des liens pour éviter de recopier mécaniquement ceux des Purposes. Huit autres capacités sans lien métier concernent les référentiels ; leur présentation par sujet ne suffit pas à établir une anomalie individuelle.

### A05 — La frontière du début d'exécution partielle reste à rendre opérante

**Constat, priorité haute.** U626 pose la révision possible d'une demande ferme avant exécution et l'adaptation des prestations engagées par Fulfillment. [Order Release BHV039](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:14653>) distingue correctement autorisation et début physique observé. La maille du début partiel et son effet sur les éléments encore révisables restent ouverts, comme le signale déjà l'annexe U626.

**Recommandation.** Préciser le contrat métier entre Lifecycle, suivi des opérations, plan et adaptation : pour 100 pièces dont 40 ont commencé à être préparées, quelles quantités, échéances et sources restent révisables, par qui et sur quel fait ? Distinguer constat de démarrage, protection applicable et éventuelle dérogation. Ce manque appelle d'abord une règle et des liens qualifiés, pas une nouvelle capacité automatique.

### A06 — Demand Planning ne nomme pas encore les arbitrages sur la demande retenue

**Constat, priorité haute.** [D17.a](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:23089>) rapproche prévisions, ventes et demandes connues. Son périmètre dit explicitement que les arbitrages sur la demande à retenir restent à préciser. Son seul comportement explicite est Demand Plan Publication ; les décisions de stock et de satisfaction ne peuvent pas remplacer cette responsabilité.

**Recommandation.** Décrire les décisions et leurs sorties : traiter des prévisions contradictoires, distinguer commande et prévision restante, retenir une demande et son incertitude. Décider ensuite de leur maille de modélisation. Comparaison de scénarios et révision sont présentes dans le périmètre : leur absence comme comportements nommés n'est pas une absence fonctionnelle démontrée. M01 distingue bien plan de demande et plan de couverture.

### A07 — Les suites d'achat du plan demandent un propriétaire explicite

**Constat, priorité moyenne.** Le catalogue contient CTP, Replenishment Decision, Initial Stocking Decision, Fulfillment Plan Decision et Purchase Order. Il couvre donc déjà faisabilité, apports et tenue de l'achat. La proposition Supply Procurement Decision de l'[annexe U568, section U581](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/master-planning-structure-U568.yaml>) n'est pas un nœud du catalogue courant.

**Recommandation.** Sur un besoin prévisionnel sans commande client, identifier qui retient un nouvel achat ou la modification d'un achat, avec quantités, dates et fournisseur admissible. Déterminer si les capacités existantes suffisent ou si cette proposition comble une responsabilité distincte. Ne pas conclure que « les achats manquent » ni créer une décision par opération ERP. Cette précision est dépendante du chantier A01.

### A08 — Action et Management distinguent imparfaitement les capacités d'Orders

**Constat, priorité moyenne.** Sales Order, Purchase Order, Transfer Order, Return Order et Supplier Return sont typés Action. Consignment Fill-up Order et Consignment Pick-up Order sont typés Management. Les définitions de ces familles portent pourtant toutes la prise en charge, les évolutions et le suivi d'une demande dans le temps. La convention historique des noms courts d'Orders comme capacités d'action explique le premier groupe, sans fournir un critère comparatif suffisant pour le second.

**Recommandation.** Expliciter le résultat dominant qui justifie le type pour chaque famille, puis harmoniser seulement si la distinction ne tient pas. Les deux grilles de types restent utiles : Policy pour une capacité et policy_strategy pour un comportement ne sont pas des qualifications interchangeables. Aucun reclassement automatique de Stocktaking ou Reservation Policy Decision n'est recommandé.

### A09 — Certaines définitions principales sont moins précises que leur périmètre

**Constat, priorité moyenne.** [Service Requirements Decision D07.a](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:7450>) se définit par « Déterminer les prestations nécessaires » ; [Process Adaptation Decision D06.f](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:10315>) par « Déterminer les variations du plan ». Leurs périmètres apportent heureusement les responsabilités et exemples manquants. Les définitions de BHV079–BHV081 énumèrent des opérations, alors que leurs périmètres décrivent correctement leur visibilité.

**Recommandation.** Remonter dans la définition le service concret, le résultat et la frontière décisive : prestations et résultats requis ; adaptation du plan d'exécution face à un aléa ; connaissance de l'avancement et du résultat des opérations. Préserver les exemples existants. L'objectif est une lecture autoportante dès la première phrase, sans réécriture générale des fiches.

### A10 — La nouvelle frontière Supply / Inventory n'est pas entièrement propagée

**Constat, priorité moyenne.** [Inventory Tracking D01.f](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:819>) déclare encore suivre distinctement les ressources futures et leurs caractéristiques attendues. D18.a porte désormais les apports attendus, tandis qu'Inventory Visibility précise déjà qu'il les consomme pour les positions et projections de stock.

**Recommandation.** Préciser que Tracking tient les positions issues des faits reconnus et indique comment il utilise la connaissance des apports fournie par Supply. La présence de quantités futures dans Inventory n'est pas une erreur : le point à résoudre est la responsabilité de leur établissement et de leur révision. M03 apporte des comparaisons fonctionnelles, sans imposer les frontières FLOW.

### A11 — La fin de Task et le rapprochement du Service doivent se relier explicitement

**Constat, priorité moyenne.** [Service Task Management D07.b](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:7610>) vérifie la fin du Service. [Service Reconciliation D07.c](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:7771>) rapproche attendu et réalisé et qualifie les écarts. Leurs responsabilités sont distinctes mais leur articulation pour terminer, poursuivre ou reprendre une prestation partiellement réalisée reste trop implicite. Un lien de dépendance existe déjà : il faut l'enrichir, pas annoncer une absence de lien.

**Recommandation.** Définir ce qui prouve le résultat métier, qui qualifie l'écart et quelle condition autorise la conclusion de la Task. Sur 80 pièces préparées sur 100, la fin technique d'un appel ne règle ni le reliquat ni l'acceptation du résultat partiel. L'activation différée, la reprise et le secours peuvent justifier des comportements de D07.b si leurs effets distincts apportent une lisibilité utile ; ils ne justifient pas un comportement par bouton. M04 fournit des appuis partiels bien délimités.

### A12 — Le nom Fill-up vient de SAP ; son attribution à Microsoft est erronée dans le texte courant

**Constat confirmé par U629, priorité haute ciblée.** [D04.r](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/model.yaml:17460>) affirme que Microsoft emploie Consignment Fill-up Order. La page Microsoft citée emploie Consignment replenishment order. L'origine SAP de Fill-up est conservée ; le constat ne remet pas en cause ce choix de nom.

**Recommandation.** Corriger uniquement l'attribution : SAP apporte le terme Fill-up ; Microsoft apporte une comparaison fonctionnelle dans la perspective de la consignation fournisseur. Séparer aussi les deux perspectives propriétaire/détenteur dans les exemples et les limites. Le portail SAP n'a pas fourni de texte lors de cette relecture ; la provenance antérieure et la précision de Laurent restent identifiées comme telles. M07 détaille cette limite.

### A13 — Quatre synthèses d'inspiration manquent, et huit entrées répètent leur résumé

**Constat, priorité moyenne pour les synthèses, faible pour la forme.** `market_inspiration` est absent de BHV096, D18.a, D19.a et D19.b, alors que leurs comparaisons existent. Il ne s'agit pas de fiches sans sources. Huit entrées répètent exactement le même texte dans `scope_summary` et `approach_summary` : deux de D07.b, deux de D04.r, deux de D18.a, une de D19.b et une de D04.t. Les autres champs conservent des informations : cette répétition ne rend pas toute la comparaison vide.

**Recommandation.** Écrire les quatre synthèses à partir des appuis réellement démontrés, puis distinguer le périmètre externe de la manière dont la source le traite. Ne pas ajouter une citation générique pour enrichir artificiellement une fiche.

### A14 — Les preuves des nouvelles capacités sont recevables mais souvent partielles

**Constat, priorité moyenne.** Les deux sources de Service Provider Policy portent sur Oracle Transportation Management ; elles n'établissent pas à elles seules un usage commun du nom pour tous les Services. La source Microsoft de Demand Protection Policy porte d'abord sur la protection de ressources par groupe. CMMN et les Job workers de Camunda éclairent des mécanismes de Task, sans démontrer tout le contrat d'achèvement d'une prestation physique. Ces limites sont déjà en bonne partie reconnues dans les fiches.

**Recommandation.** Conserver les bons appuis et rendre explicite ce qui est attesté, adapté ou encore non documenté : nom, résultat, périmètre et mécanisme. Chercher un second organisme lorsque cela améliore la preuve, sans transformer cette préférence en obligation générale. Les comparaisons M03 à M06 ci-dessous précisent les écarts utiles.

## Réexamen ciblé des références au marché

Documents relus le 23 septembre 2026. Les conclusions ci-dessous sont des interprétations de comparaison, pas des équivalences universelles ni des preuves d'installation. Sources évolutives sans édition figée sauf indication contraire.

| Repère / fiches | Documents et passages effectivement consultés | Points communs, différences et conséquence pour FLOW |
| --- | --- | --- |
| **M01 — D03.p, D05.f, D17.a** | [Microsoft, Master plans overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans), Using master plans, Firming, Action message ; [Oracle 26B, Plan types](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faupc/overview-of-supply-chain-planning-plan-types.html), tableau Demand / Supply / Demand and Supply / Backlog / Replenishment | Les sources documentent différents travaux de planification et des résultats intégrés possibles. Microsoft décrit aussi propositions d'apports et révisions. Elles ne prescrivent ni une seule capacité de gestion ni les comportements FLOW. Oracle distingue le plan de demande alimentant la couverture : garder cette responsabilité propre est cohérent. L'unicité de la référence retenue FLOW reste un choix à rendre opérant. |
| **M02 — BHV028 / Inventory Target Decision** | [SAP, Global (Multi-stage) Inventory Optimization](https://learning.sap.com/courses/mastering-sap-ibp-for-inventory-planning-and-optimization/global-multi-stage-inventory-optimization_c360cea7-b52e-45cb-9436-5ea0c79451a9), Global operator ; [Achkar et al., prépublication 2023](https://arxiv.org/abs/2306.10961), résumé seulement | Les deux documents traitent du dimensionnement des stocks de sécurité dans un réseau avec contraintes de service et de coût. Ils étayent la responsabilité de cibles, pas l'élargissement au pilotage général demande/apports suggéré par le nouveau nom. Leurs critères économiques ne deviennent pas une pondération imposée à FLOW. |
| **M03 — D18.a / D01.f / Inventory Visibility** | [Oracle 26B, Supply Chain Orchestration](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauco/overview-of-supply-orchestration.html), Manage supply et Change management ; [Microsoft, Inventory on-hand list](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-on-hand-list), introduction et tableau des quantités | Oracle relie demandes, apports, documents et changements ; Microsoft expose notamment stocks, attendus et réservations. Oracle couvre aussi orchestration et création, Microsoft réunit des mesures dans une vue. Appuis partiels pour la connaissance des apports ; aucune des deux sources ne prouve le découpage entre les Purposes FLOW. |
| **M04 — D07.b / D07.c** | [OMG CMMN 1.1, décembre 2016](https://www.omg.org/spec/CMMN/1.1/PDF), §5.4.10, table 5.39, p. 45 imprimée / page PDF 63 ; [Camunda, Job workers](https://docs.camunda.io/docs/components/concepts/job-workers/), complétion, échec, délai et livraison au moins une fois | CMMN distingue Task bloquante et non bloquante. Camunda décrit reprise et complétion de jobs, avec risque d'exécution répétée. Le choix FLOW d'attendre une fin métier vérifiée est plus spécifique ; le job technique n'est pas la prestation physique. Les sources éclairent la gouvernance et le besoin de distinguer les résultats, sans imposer la réalisation logicielle. |
| **M05 — D19.a** | [Oracle OTM 24A, Active/Inactive Flag](https://docs.oracle.com/en/cloud/saas/readiness/logistics/24a/otm24a/24A-otm-wn-f29771.htm), description et bénéfice ; [Oracle OTM 26B, Capacity Limit](https://docs.oracle.com/en/cloud/saas/transportation/26b/otmol/planning/capacity_manager/create_new_limit_data.htm), Using a Capacity Limit | Deux documents distincts sur activation et limites de recours/capacité d'un prestataire transport. Ils sont pertinents mais de même éditeur et de périmètre transport. Une capacité disponible et une restriction décidée face à un risque ne sont pas automatiquement le même résultat. Le nom et la généralisation à tous les Services restent une adaptation FLOW. |
| **M06 — D19.b** | [Microsoft, Inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), Business background, virtual pool ; [SAP, Exploring Backorder Processing](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe), Confirmation strategies | Microsoft réserve des droits de consommation à des groupes, y compris avant commande. SAP distingue des stratégies de maintien, amélioration ou dégradation des confirmations. Le second appui est plus directement lié aux protections des demandes ; le premier doit rester qualifié d'indirect pour cette fiche. FLOW sépare politiques, classement effectif, affectation et engagement. |
| **M07 — D04.r / D04.t** | [Microsoft, Set up consignment](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment), Consignment replenishment orders ; [Oracle 25D, Consigned Inventory Returns](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/famml/examples-of-consigned-inventory-returns.html), Material Received / Material Consumed ; [SAP, Consignment Orders](https://help.sap.com/docs/SAP_FASHION_MANAGEMENT/3d09d3032a1649f4abf6eea0a8f3ed11/a620215320ce9254e10000000a4450e5.html), tentative sans texte exploitable | Microsoft décrit la demande d'apport de biens restant propriété du fournisseur. Oracle distingue les retours selon état et consommation, avec certains mécanismes de retour au régime consigné. Ces sources éclairent le fonctionnement ; elles n'attestent pas le mot Fill-up chez Microsoft ni deux capacités identiques chez tous les éditeurs. L'origine SAP du terme est confirmée par U629 et la provenance antérieure ; aucune nouvelle vérification intégrale du passage SAP n'est prétendue. |

## Manques : ce qui doit être décidé avant de créer des éléments

| Besoin insuffisamment explicite | Couverture déjà présente | Suite recommandée |
| --- | --- | --- |
| Référence commune du plan, effets partiellement appliqués, suivi et révision | D03.p, D05.f, D03.o et propositions U575–U579 | Consolider la responsabilité et la succession des comportements ; ne pas ajouter une quatrième planification |
| Arbitrage de la demande retenue et incertitude | D17.a et BHV095 | Décrire les décisions avant de choisir de nouvelles capacités |
| Suites d'achat décidées pour les prévisions / le stock | CTP, décisions d'apport, plan collectif, Purchase Order ; proposition U581 | Délimiter le propriétaire et vérifier le recouvrement avant création |
| Début partiel d'exécution et éléments encore modifiables | Lifecycle, Release, Tracking, Process Adaptation | Définir règle, portée et coopération |
| Couverture, partage de la rareté et réexamen du plan | Résultat de D03.o ; comportements proposés U579 | Réexaminer le bénéfice de cette décomposition déjà étudiée, sans présenter ces sujets comme absents |
| Activation, reprise et conclusion d'une Task | D07.b, D07.c, D06.d et D06.f | Clarifier les résultats ; décomposer seulement si la complexité ou la lisibilité le justifie |

Les homonymes Initial Stocking, Direct Delivery, Inventory Rebalancing ou Stock Consolidation ne sont pas des doublons à fusionner automatiquement : une décision et une prise en charge d'Order peuvent partager une intention tout en produisant des résultats différents. Les comportements conservent leurs parents propres. Aucun manque Commerce, Finance ou fonctionnalité interne d'exécutant n'est ajouté au périmètre Supply.

## Ordre conseillé pour la reprise

1. **Plan commun et frontières** : A01, A05, A06, A07. Produire un schéma de responsabilités et quelques cas d'épreuve avant de déplacer ou de créer des éléments.
2. **Alignement du catalogue** : A02, A03, A04, A10, A11. Relier noms, périmètres et coopérations aux responsabilités retenues, en conservant identifiants et accords.
3. **Types, rédaction et preuves** : A08, A09, A12–A14. Corriger l'attribution SAP/Microsoft, compléter les synthèses et justifier les choix à la maille de chaque fiche.

Les corrections factuelles de rédaction, les arbitrages de responsabilité et les nouveaux comportements ont des portées différentes. Aucun accord global sur les recommandations de ce dossier n'est déduit de la demande d'audit.

## Proposition de reprise A01 — responsabilité du plan commun

U630 ouvre ce premier point ; U631 valide la capacité commune, sa définition présentée dans la réponse et la répartition des responsabilités. D05.f reprend D03.p ; D02.e devient Apply Plan et reprend BHV094 ; BHV006 reprend BHV091. Le choix des identifiants survivants est une mise en œuvre Codex. Six comportements hérités restent présents, avec la décomposition des cinq actes de pilotage et du suivi/ajustement à construire. Voir [les portées et successions](<C:/Dev/Beaumanoir Cartographie/modeles/backlog/common-planning-U631.yaml>).

**Recommandation : réunir Order Backlog Planning et Demand & Supply Optimization Planning dans une capacité de type Planning, sous Demand & Supply Optimization.** Le nom actuel Demand & Supply Optimization Planning peut servir de nom de travail. Il exprime une adaptation FLOW, pas un intitulé standard démontré par les sources. Le choix d'identifiant survivant et les successions des comportements seront établis avec la migration, en préservant les accords et sans réutiliser d'identifiant retiré.

**Définition adoptée U631, telle que présentée :** « Construire, comparer et maintenir un plan cohérent de couverture des commandes et des besoins prévisionnels restants ; mobiliser les décisions spécialisées, faire appliquer les recommandations autorisées et suivre leurs effets. » Le périmètre et l’horizon sont explicités dans le scope, comme compléments rédactionnels.

Le plan relie besoins, ressources présentes et attendues, affectations, nouveaux apports et ajustements proposés, ainsi que les conséquences des éventuelles révisions de politiques. Les recommandations précisent leurs hypothèses, conditions, interdépendances et besoins restant non couverts. Plusieurs scénarios peuvent être étudiés ; la référence retenue doit être identifiable pour le périmètre et l'horizon concernés. Une recommandation retenue et un engagement effectivement enregistré demeurent distincts.

| Responsabilité | Porteur proposé ou conservé |
| --- | --- |
| Organiser le travail, comparer les scénarios, maintenir la référence, suivre et ajuster le plan | Capacité Planning commune |
| Déterminer les résultats spécialisés et la compatibilité du scénario d'ensemble | Capacités Decision existantes, dont D03.o ; leurs périmètres seront alignés au plan commun |
| Rendre effectives les recommandations autorisées et connaître leur prise en compte | Apply Plan, comportement direct du Planning, mobilisant les responsables concernés ; continuité de D02.e et BHV094 à formaliser |
| Tenir les Orders, promesses, réservations et politiques applicables | Capacités partenaires actuelles, dans Demand, Inventory et Reference & Policy Management |
| Coordonner et adapter les prestations engagées | Fulfillment Orchestration |

Le type Planning convient parce que la capacité organise et actualise un plan en mobilisant des décisions. Le fait qu'elle « gère » un plan ne suffit pas à la typer Management. Les comportements sont des enfants du Planning ; les décisions mobilisées restent des capacités sœurs, reliées par des coopérations.

**Cas d'épreuve fictif.** Un scénario prévoit un transfert de 30 pièces et un nouvel achat de 70. Le transfert est pris en compte ; l'achat est refusé. Apply Plan constate ces deux résultats distincts. Le Planning conserve le transfert pris en compte et la recommandation refusée, rend visible le manque de couverture, puis mobilise les décisions pour proposer une révision. Une autre source ou échéance ne devient applicable que selon les autorisations et les prises en compte correspondantes. Aucun effacement du transfert ni disponibilité fictive des 70 pièces n'est déduit du refus. Un effet dépendant d'une autre recommandation doit être réexaminé avant sa propre application.

**Bénéfice et compromis.** Le regroupement rend explicite la responsabilité du plan et évite les doubles fonctions de simulation, d'application et de suivi. Il élargit la capacité et exige des comportements lisibles ; il ne centralise pas la maîtrise des engagements partenaires. Les cinq actes de pilotage distingués en U578 et Apply Plan restent des contraintes de continuité à respecter lors de la décomposition ; le regroupement ne les efface pas.

**Appuis marché réutilisés : M01.** Microsoft documente des plans mobilisant demande et supply, des propositions d'Orders et des ajustements ; Oracle distingue notamment plan de demande et plan intégré Demand and Supply. Points communs : scénarios et coordination des besoins/apports. Différence : leurs familles de plans et découpages de produits ne prescrivent ni une capacité FLOW unique ni sa taxonomie de comportements. Le regroupement est recommandé pour la cohérence des responsabilités FLOW ; aucune preuve d'une optimisation conjointe universelle de toutes les politiques n'est ajoutée. Les deux documents ont déjà été relus dans cette session ; aucun nouveau contrôle documentaire n'était nécessaire pour ce rapprochement inchangé.

## Contrôles et traçabilité

Demande, précision et ouverture de la reprise enregistrées dans [les contributions U628–U631](<C:/Dev/Beaumanoir Cartographie/connaissance/01-contributions-utilisateur.md>). Lecture structurée par `scripts/structured_io.py` et inspections ciblées par `scripts/inspect_model.py`. Contrôle du backlog courant par `validate_urbanism` avec le schéma et le glossaire : zéro erreur. Index des sources actualisé par `python scripts/refresh_sources.py` : 2 320 enregistrements ; sources figées inchangées. Après application U631 : `python scripts/validate_models.py` sans erreur, 36 tests des modèles/niveaux réussis, vue backlog actualisée. Quatre captures d’accord portent uniquement les champs et rattachements présentés. Aucun rejeu de l’audit U431 ni publication déclenchée.

Les mesures reproductibles et le script de lecture de cet audit sont temporaires sous `.runtime/audit-capacites-comportements-U628/` ; ils ne dupliquent pas le modèle et ne constituent pas une source métier concurrente.

# Prestations logistiques et ordres d’exécution — audit U674–U679

23 septembre 2026 — Codex. **Découpage, frontières et convention de maille adoptés par Laurent en U679. Application au modèle canonique en attente.** État étudié : backlog au commit `8816726`, release v022. [Proposition structurée et portée de l’accord](../modeles/backlog/logistics-execution-audit-U674.yaml), comparaison CMP273.

## Décision adoptée

Créer un sous-domaine **Service Order Management**, distinct d’**Order Management** et de **Fulfilment Orchestration**.

| Sous-domaine | Responsabilité adoptée |
| --- | --- |
| Order Management | Gérer les demandes à satisfaire et porter les engagements correspondants. |
| Service Order Management | Gérer les prestations confiées aux exécutants, leurs exigences, leurs engagements propres et leurs évolutions. |
| Fulfilment Orchestration | Composer et coordonner ces prestations, suivre leurs dépendances et rechercher les adaptations qui préservent la promesse et les équilibres du Matching. |

Service Catalog conserve la description de l’offre mobilisable. Les exécutants conservent l’organisation de leurs opérations internes.

Les familles d’ordres de services se situent au **niveau capacité**, comme les familles d’Orders entrants. Leurs noms ne se terminent pas par Management : **Picking Order**, **Packing Order**, **Value-Added Service Order**, **Cross-Docking Order**, selon les familles retenues. Ces noms ne constituent pas une liste exhaustive ; leurs définitions détaillées et comportements ne sont pas adoptés par extension.

La première recommandation de Codex, qui conservait tous les ordres dans Fulfilment et proposait un simple renommage générique de D07.b, est remplacée. La présence actuelle de D07.b ne justifiait pas la frontière cible. Le critère retenu distingue la gestion des engagements de prestation de leur coordination d’ensemble, avec une maille cohérente de part et d’autre.

## Ce que les sources établissent

| Référence primaire consultée | Constat | Conséquence pour FLOW et limite |
| --- | --- | --- |
| [Microsoft — Warehouse management only mode](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-overview), ELM133 | Les Inbound/Outbound Shipment Orders sont dédiés au besoin entrepôt, distincts des documents généraux de vente, achat ou transfert. | Appui direct à la séparation des deux rôles d’Order. Ne couvre pas toutes les prestations et ne prescrit pas un sous-domaine. |
| [Oracle — Shipment Request / Confirmation, 25D](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faims/shipment-request-and-shipment-confirmation-processes-for.html), ELM659 | Une demande au WMS/3PL conduit au picking, packing et shipping, puis à un compte rendu. | Une prestation confiée peut couvrir plusieurs opérations. Pas d’obligation universelle d’un Picking Order puis d’un Packing Order. |
| [SAP — Warehouse Order](https://help.sap.com/saphelp_ewm700_ehp02/helpdata/en/65/cccb53ad377114e10000000a174cb4/content.htm?no_cache=true), ELM660 | Le Warehouse Order regroupe du travail destiné à un opérateur. | Faux équivalent d’un ordre confié par l’orchestrateur à un prestataire. Documentation historique EWM 7.0 EHP2, utilisée pour sa sémantique. |
| [SAP — Value-Added Services, EWM 9.5 FPS02](https://help.sap.com/docs/SAP_EXTENDED_WAREHOUSE_MANAGEMENT/3d97bec9bf1649099384bb8167df3cf2/4cb48fea25d1664ce10000000a15822b.html), ELM658 ; [Oracle — Outbound Logistics, EBS 12.2](https://docs.oracle.com/cd/E26401_01/doc.122/e48830/T211976T317987.htm), ELM661 | SAP décrit des VAS Orders ; Oracle cite le repackaging et le kitting dans les VAS. | Appui à une famille de prestations légères. U675 précise le sens de light touch ; cela n’adopte pas toutes les activités industrielles que peut recouvrir VAS. |
| [Microsoft — Packing work](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/packing-work), ELM656 ; [Planned cross docking](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/planned-cross-docking), ELM657 | Packing et cross-docking ont des travaux explicites. Le cross-docking relie les entrées aux sorties ; ses demandes peuvent être portées par les lignes de Shipment Orders. | Visibilité distincte des opérations, sans en déduire autant d’Orders autonomes à la frontière FLOW. Deux sources Microsoft ne prouvent pas un consensus interéditeurs. |
| [TM Forum — TMF633 v4.0](https://www.tmforum.org/open-digital-architecture/open-apis/service-catalog-management-api-TMF633/v4.0), ELM129 ; [TMFC007 v2.0.0](https://www.tmforum.org/oda/directory/components-map/production/TMFC007), ELM492 | Catalogue et commandes de service sont séparés ; Service Order Management inclut une orchestration. | Le catalogue ne remplace pas la gestion des ordres. L’analogie télécom ne démontre pas qu’il faut séparer cette gestion de Fulfilment dans FLOW. |

Sources primaires consultées le 23 septembre 2026. SAP VAS : passage indexé détaillé consulté, ouverture directe sans corps exploitable. Les autres textes indiqués ont été ouverts. Versions, passages, nature native et limites sont conservés dans l’annexe. Étude ciblée, sans classement exhaustif des offres ni constat de réalisation installée chez Beaumanoir.

## Rapport avec le modèle existant

D07.b Service Task Management tient déjà activations, demandes, réponses, reprises et vérification de fin. Sa responsabilité devra être répartie explicitement dans la cible, sans perte ni création en doublon. Le fait qu’un Order soit formalisé par un ou plusieurs documents ne détermine pas le nombre de capacités métier.

D06.d Process Orchestration et D06.f Process Adaptation Decision décrivent coordination et adaptation. D07.a détermine les prestations ; D07.d suit leur progression ; D07.c rapproche attendu et réalisé ; D06.b rend visible la capacité communiquée. **Le rattachement détaillé de ces capacités n’a pas été présenté dans l’accord U679.** Il reste à instruire lors de l’application.

D14 Service Catalog doit rendre l’offre concrète : picking, packing, VAS et cross-docking, avec résultats, conditions et niveaux de service. Cette description ne remplace pas les capacités qui gèrent les engagements individuels.

TER066 décrit actuellement Service Order comme un document de formalisation facultative. La distinction entre instance métier, formalisation documentaire, contribution au processus et tâches internes devra être clarifiée. Ce complément est proposé, sans validation implicite de nouveaux champs.

Les formulations héritées restent à corriger dans ce lot : le lien REL-SERVICE-CATALOG-PROMISING attribue encore à D04 la construction de la promesse ; certains périmètres utilisent Availability ou Demand. Réexaminer le sens avec Order Promising et Order Management, sans supprimer automatiquement les usages directs du catalogue par D04.

## Familles présentées et précisions encore proposées

| Nom présenté au niveau capacité | Résultat illustratif, encore proposé |
| --- | --- |
| Picking Order | Gérer les prélèvements confiés et leurs suites, dont les manquants. |
| Packing Order | Gérer le conditionnement confié et la conformité des unités constituées. |
| Value-Added Service Order | Gérer le réétiquetage, le reconditionnement et les autres traitements légers précisés par U675. |
| Cross-Docking Order | Gérer les prestations de transit et leurs engagements entre réception et départ. |

Une prestation composite peut mobiliser plusieurs capacités. Les tâches opérateur, gestes et documents ne créent pas automatiquement des niveaux de décomposition. Aucune correspondance un pour un entre Order entrant et Service Order n’est adoptée.

Proposition de frontière pour le cross-docking : Matching arbitre quelles arrivées couvrent quels besoins ; les engagements de prestation relèvent de Service Order Management ; Fulfilment coordonne leur réalisation et les adaptations. Cette formulation détaillée doit être instruite dans les fiches, sans transférer le master plan de matching.

## Noms de marché et choix FLOW

**Service Order Management** est attesté chez TM Forum, où il comprend aussi de l’orchestration. Les sources Microsoft et Oracle appuient la séparation des commandes amont et des demandes aux exécutants. Elles ne prescrivent pas notre frontière exacte : celle-ci résulte du choix métier adopté U679.

**Logistics Execution** est un autre périmètre attesté, avec une portée plus directement opérationnelle : [SAP, présentation](https://help.sap.com/doc/a6a8c7536e8e2a4be10000000a174cb4/700_SFIN3E%20006/en-US/2f9cc7536e8e2a4be10000000a174cb4.html), ELM662, et [VAS Execution, S/4HANA 2025 FPS01](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9609b5f9e9304ef6850945b359a1f5d4/3771b65334e6b54ce10000000a174cb4.html?locale=en-US&state=PRODUCTION&version=2025.001), ELM664. Deux sources SAP ne prouvent pas un consensus.

**Supply Chain Execution** désigne un regroupement plus large ; la [brochure Oracle](https://www.oracle.com/us/products/applications/ebusiness/logistics/value-chain-execution-brief-068424.pdf), ELM663, porte un copyright 2009 et sert uniquement de preuve historique. Aucun sous-domaine standard transversal nommé **Execution Services** n’a été établi dans le corpus consulté.

## Portée de l’accord et application

L’accord U679 porte sur le sous-domaine Service Order Management, les frontières présentées, la maille capacité des familles et leur convention de nommage. Il ne valide pas toutes les descriptions de cet audit, les rattachements existants non présentés, une liste exhaustive des familles ou des pratiques installées.

L’accord est enregistré avec ses valeurs et leur empreinte dans l’annexe YAML. Le modèle canonique et la release v022 restent inchangés à ce stade ; la redistribution des capacités constitue le lot d’application à préparer. Aucun commit, push ou nouvelle publication réalisé.


## Complément U680/U681 — comportements de Value-Added Service Order

Laurent valide le principe et les angles présentés : **Labeling / Relabeling** (exigences, version attendue, conformité), **Repacking** (modification du conditionnement, consignes, résultat attendu) et **Kitting / Dekitting** (assemblage ou séparation d’ensembles, composants et écarts), **si cette dernière prestation entre dans le périmètre retenu**.

Ces comportements sont directement rattachés à Value-Added Service Order et restent terminaux. Ils décrivent les particularités de gestion de l’ordre, pas les gestes opérateur. Leur bénéfice est de distinguer la conformité de l’information appliquée, du conditionnement et de la composition d’un ensemble. Un paramètre de service seul ne crée pas un comportement.

La section vas_behaviors_U681 de l’annexe précise des définitions, exemples et frontières proposés : ils ne sont pas implicitement adoptés par cet accord. La distinction Repacking / Packing Order reste à expliciter pour éviter de commander deux fois la même prestation. Les sources SAP ELM658 et Oracle ELM661 déjà consultées étayent les familles VAS, mais ne prescrivent pas cette décomposition en comportements de gestion ; le détail du dekitting n’est pas établi dans ces passages.

Accord limité et empreinte enregistrés sous agreement_U681. Modèle canonique et publication inchangés ; aucune réouverture de l’audit historique des comportements.

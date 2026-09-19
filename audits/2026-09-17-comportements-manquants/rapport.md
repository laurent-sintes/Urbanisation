# Audit comparatif des comportements manquants — synthèse consolidée U298

**Audit clos U431.** Tous les candidats sont intégrés, couverts par l’existant ou retirés. P04/P10/P12 ne créent aucun comportement supplémentaire. Frontière commerciale et financière externe à Supply ; règles et contrats détaillés conservés comme travaux ultérieurs non bloquants. [Bilan de clôture](cloture-U431.md). Les états et propositions antérieurs ci-dessous conservent leur portée historique.

**État courant U427 :** Replenishment Decision porte Requirement-based Replenishment (BHV083), Target-based Replenishment (BHV084) et Replenishment Adjustment (BHV085). Deux politiques et un mécanisme combinable ; noms, définitions présentées et rattachements adoptés. Exemples, justifications et comparaison Microsoft documentés avec leur portée éditoriale. P01–P03 sont intégrés : le point réassort est clos. Les autres arbitrages de l’audit restent distincts ; les conclusions antérieures de non-décomposition et de réouverture ci-dessous sont historiques.

**État courant U424 :** Lifecycle unique en D04 avec six dimensions et leurs états explicites. Rescheduling BHV041 est intégré à Preparation & Revision BHV038 ; Cancellation BHV042 est intégré à Termination BHV043, avec distinction entre annulation et clôture. Les anciens identifiants sont conservés dans les preuves et ne sont pas réutilisés. D03 mobilise Lifecycle ; D06 garde orchestration et réalisations. Nouvelles formulations et listes détaillées éditoriales. Les décompositions antérieures ci-dessous sont historiques.

**État courant U420 :** Order Archiving appartient à D03 ; Order Lifecycle Management appartient à D04, avec Order Release. Structuring et Split restent dans D03. Identifiants, définitions et parents des comportements conservés. Les mentions U417/U418 ci-dessous sont historiques et remplacées sur ces rattachements. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml).

**État courant U417/U418 :** dans D03 Order Backlog Management, Structuring porte Order Splitting et Lifecycle porte Order Release. Les capacités D04.n/D04.o conservent leurs identifiants historiques. Planning prépare les scénarios ; Lifecycle autorise ; Process Orchestration coordonne les services. Gel et suspension sont combinables, sans séquence universelle. Aucun ajout de nœud ou comportement ; arbitrage de placement du carnet résolu. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml). Les anciens rattachements ci-dessous sont historiques.

**État courant U414 :** Order Backlog Planning (D03.p) est créé dans D03. Order Release BHV039 y est déplacé, identité et définition conservées. Lifecycle conserve huit comportements ; Split et Structuring restent en D04 pour le prochain arbitrage. Planning mobilise les décisions et prépare la prise en charge ; affectation, promesse et orchestration gardent leurs responsabilités. Aucun comportement supplémentaire : 47 capacités et 73 comportements. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml). Les anciens rattachements ci-dessous restent historiques.

**État courant U413 :** D03 devient Order Backlog Management. Le travail collectif du carnet prépare son engagement vers les processus, en mobilisant les décisions spécialisées. D04 conserve la demande par intention. Réexamen ciblé de Lifecycle/Structuring : parents inchangés, aucune nouvelle capacité ou comportement. P11 demeure intégré à Order Release ; son placement côté carnet reste à concrétiser. [Mandat, comparaison et réexamen](../../modeles/backlog/order-backlog-review.yaml). Les noms et positions des états précédents sont historiques.

**État courant U410 :** P11 est résolu par enrichissement d’Order Release (BHV039) : conditions individuelles et collectives, complétude, éléments indispensables et traitement partiel. Aucun comportement ajouté ; autorisation distincte de l’affectation et de Process Orchestration. Autoriser ensemble ne signifie pas démarrer simultanément. Les mentions antérieures de P11 ouvert sont historiques. [Accord et comparaison](../../modeles/backlog/order-lifecycle-behaviors.yaml).

**État courant U409 :** le Process orchestre des Services. D06 devient Process Management ; Process Orchestration et Process Adaptation Decision restent distincts. Operations Tracking porte les trois visibilités physiques et Process Tracking. Neuf noms adoptés ; Service Catalog Ingestion et Service Reconciliation sont deux intitulés dérivés proposés. Aucun ajout de comportement ni changement de responsabilité. Les intitulés des états datés ci-dessous restent historiques. [Convention et comparaison](../../modeles/backlog/execution-services-review.yaml).

**État courant U406 :** 47 capacités et 74 comportements. Warehouse Visibility, Transportation Visibility, Store Visibility et Business Process Tracking intégrés sous Execution Tracking (BHV079–082). Tasks et appels sont des objets suivis, pas des niveaux de comportement. Digital Service Visibility est remplacé ; le besoin numérique demeure couvert. [Portées et comparaison](../../modeles/backlog/execution-services-review.yaml). Les propositions et mentions de non-intégration ci-dessous sont historiques.

**État courant U403 :** 47 capacités et 74 comportements. Supplier Confirmation (BHV078) complète Purchase Order et résout A06 sur le catalogue : demande, réponse fournisseur et engagement accepté distincts ; impacts, mutations et promesse client gardent leurs responsables. Refuser un report ne supprime pas le risque annoncé. [Explication et comparaison](../../modeles/backlog/purchase-order-behaviors.yaml). Les mentions antérieures d’un point A06 ouvert restent historiques.

**État courant U402 :** 47 capacités et 74 comportements. Les trois mécanismes CTP BHV075–077 sont intégrés : ressources supplémentaires, alternatives de satisfaction et réexamen d’engagements. P14–P16 ne sont plus conditionnels ; A05 est résolu sur la frontière de catalogue, les règles détaillées restant distinctes. Fulfillment Plan Decision conserve le choix collectif. [Portée et comparaison](../../modeles/backlog/d03-review.yaml). Les états datés ci-dessous conservent leur valeur historique.

**État courant U391 :** Purchase Order porte Stock Procurement, Direct Delivery et Service Procurement (BHV058–060). Consignation instruite séparément dans la gestion du stock. [Accord et intégration](../2026-09-18-purchase-order-U391/README.md).

**État courant U388 :** Return for Repair (BHV057) complète Supplier Return : restitution attendue du même bien réparé, distincte du remplacement. L’ajout n’est plus conditionnel ; achats de prestation et exécution conservent leurs responsabilités. [Portée de l’ajout](../2026-09-18-supplier-repair-U388/README.md).

**État courant U387 :** Supplier Return porte Return for Credit et Return for Replacement (BHV055–056), distingués par l’apport de remplacement attendu. Finance, achat et exécution restent distincts. [Accord et intégration](../2026-09-18-supplier-return-U387/README.md).

**État courant U385 :** définition élargie de Customer Return et cinq parcours combinables adoptés : Return to Stock, Repair and Refurbishment, Return to Supplier, Return to Customer et Scrapping (BHV050–054). Les axes commerciaux et les autres filières restent à instruire. [Accord et intégration](../2026-09-18-customer-return-U385/README.md).

**État courant U384 :** noms courts Sales Order, Purchase Order, Transfer Order, Customer Return et Supplier Return adoptés. Cinq parcours Customer Return détaillés en proposition dans `modeles/backlog/customer-return-behaviors.yaml`, sans ajout au catalogue à ce stade. [Nommage et étude](../2026-09-18-customer-return-U384/README.md).

**État courant U383 :** cinq capacités par type d’Order sont rétablies sous D04 ; Order Type D04.p est retiré. Lifecycle, Structuring et Archiving restent transverses. Return Disposition Decision porte Policy-based Disposition et Value Recovery Optimization (BHV048–049). Les prises en charge des retours restent à détailler. Les états datés ci-dessous sont historiques. [Portée et comparaison](../2026-09-18-orders-disposition-U383/README.md).

**État courant U380 :** Return Disposition Decision (D05.i) est adoptée sous Inventory Optimization, sans comportement. A04 est résolue sur le devenir logistique du bien ; autorisation commerciale, remboursement et remplacement client restent distincts. [Accord et intégration](../2026-09-18-return-disposition-U380/README.md).

**État courant U378 :** Fulfillment Plan Decision (D03.o) produit le scénario collectif ; D03 porte le nom adopté Fulfillment Optimization. A02 est résolue sur la responsabilité ; les contrats détaillés restent proposés. Aucun sous-niveau ou comportement ajouté. Les états U364 et antérieurs ci-dessous sont historiques. [Accord et intégration](../2026-09-18-fulfillment-plan-U378/README.md).

**État courant U364 :** Supply Assignment porte application d’un plan, complément préservant les affectations et réaffectation des liens modifiables (BHV045–BHV047). La distinction stabilité/adaptation est adoptée ; les décisions spécialisées et Freezing gardent leurs responsabilités. A01/A02 restent ouverts. [Portée et comparaison](../2026-09-18-supply-assignment-U364/README.md).

**État courant U363 :** D04 comporte Order Type (cinq variantes), Order Lifecycle Management (neuf comportements), Order Structuring et Order Archiving. Split est une mutation avec filiation ; Spread concerne l’affectation des ressources entre Orders. Les états datés ci-dessous sont historiques. [Refonte et portée](../2026-09-18-d04-U363/README.md).

**Validation U350 :** Order Freezing est le nom adopté pour BHV037. Le principe et le parent U349 sont conservés ; les détails et contrats restent proposés.

**État courant U349 :** Order Lifecycle Management porte Order Firming (BHV036) et la protection contre les réoptimisations (BHV037, nom éditorial Order Freezing). Affermissement, gel et mise en attente sont distincts. Accord et limites dans `modeles/backlog/order-lifecycle-behaviors.yaml` ; P11 reste ouvert. Catalogue : 41 capacités et 28 comportements.

**Clarification U345 / C99 :** Supply Assignment porte l’application des affectations d’un plan ; D04 garde ses effets sur les Orders. Trois mécanismes documentés en proposition dans `modeles/backlog/supply-assignment-mechanisms-review.yaml`. Simulation & Analysis explicite les recommandations ; compensation logicielle hors de cette décomposition métier. Aucun nouveau nœud.

**État courant U343 :** les quatre comportements BHV032–BHV035 et le parent D05 sont adoptés, dans la portée des noms et responsabilités présentées. Modalités détaillées, contrats et comparaisons restent proposés. Les mentions U342 ci-dessous décrivent l’état antérieur. [Portée de validation](../2026-09-18-reservation-policy-adoption/README.md).

**État courant U342 :** Reservation Policy Decision (D05.h), nom et définition adoptés. Quatre comportements BHV032–BHV035 documentés et proposés ; parent D05 proposé. Catalogue : 41 capacités et 26 comportements, dont ces quatre nouvelles propositions. [Recensement et frontières](../2026-09-18-reservation-policy/README.md). A01 reste ouvert au-delà de cette décision.

**État courant U334 :** Stocktaking porte politique et demandes de vérification, ainsi que Periodic Physical Inventory (BHV029), Cycle Counting (BHV030) et Spot Counting (BHV031). P08/P09 intégrés ; traitement des écarts commun et réalisation physique par les exécutants. Catalogue : 40 capacités, 22 comportements. Les sections datées conservent leurs états historiques. [Portée de la validation](../2026-09-18-stocktaking-behaviors/README.md).

**État courant U332 :** Inventory Target Decision porte trois comportements frères : Store Inventory Optimization (BHV026), Distribution Center Inventory Optimization (BHV027) et Multi-Echelon Inventory Optimization (BHV028). P13 est intégré ; P12 reste sans création recommandée. Catalogue : 40 capacités et 19 comportements. Les sections datées ci-dessous conservent leurs états historiques. [Portée de la validation](../2026-09-18-inventory-target-behaviors/README.md).

**État courant U318 :** deux comportements intégrés sous Stock Redistribution Decision : rééquilibrage entre sites (BHV024) et consolidation des stocks dispersés (BHV025), dont assortiments de tailles et reliquats. Définitions françaises et rattachements adoptés ; noms anglais éditoriaux. Catalogue : 40 capacités, 16 comportements. [Portée de l’accord](../2026-09-18-redistribution-behaviors/README.md). P01–P03 sur le réassort restent ouverts. Les textes datés ci-dessous conservent leur portée historique.

**Réexamen U324 / C98 :** les min/max peuvent dépendre des besoins et varier par période. Coverage Target Decision détermine les valeurs ; Supply Protection gouverne leur application ; Replenishment Decision détermine les apports. La création des comportements proposés U323 est suspendue faute de bénéfice différenciant établi. [Comparaison CMP111](../../marche/comparaisons.md#cmp111).

**L’audit reste une base utile ; ses conclusions ont été mises à jour après U293–U297. Il n’est pas nécessaire de refaire toute l’étude marché à ce stade.** Le catalogue audité est inchangé ; les discussions ont corrigé le choix et la qualification des propositions. Les feedbacks datés conservent le raisonnement antérieur, pas des recommandations concurrentes.

**Le niveau Capacité → Comportement suffit pour les mécanismes étudiés. Le travail prioritaire consiste à rendre explicites quelques mécanismes et leurs contrats, pas à ajouter une profondeur ni à décomposer toutes les capacités.**

Le backlog refondu U290 contient **39 capacités et 14 comportements**, répartis sur quatre capacités. Les 35 autres ne sont pas 35 lacunes. Les seize fiches initiales se répartissent désormais en **7 candidats à instruire**, **5 options conditionnelles**, **3 propositions à réexaminer** et **1 retrait**. Les **7 arbitrages de responsabilité ou de contrat** restent ouverts. **Logistics Visibility** est le nom adopté U297 pour le parcours physique du picking au point final ; son niveau, son rattachement et les détails éditoriaux restent à instruire. Aucun nouveau BHV n’a été créé.

Cette conclusion vaut pour le périmètre Supply décrit. Elle ne démontre pas la complétude de Business Services, des opérations internes des exécutants ou des modèles de référence non encore détaillés. Aucun état installé ni taux de couverture des trois SI n’est inféré.

## Lecture et périmètre

- [Matrice et examen des 39 capacités, puis des 14 comportements](capacites.md).
- [16 fiches de mécanismes : définition, bénéfice, exemple, frontières et dépendances](propositions.md).
- [7 arbitrages, contrats et 10 cas métier fictifs](arbitrages-et-cas.md).
- [70 sources primaires avec édition, passage et limites](sources.md).
- [Autorité YAML des propositions](../../modeles/backlog/behavior-gap-audit.yaml).

Le socle U292 compare Microsoft, SAP, Oracle, Manhattan, Blue Yonder, Kinaxis et RELEX. Les compléments mobilisent Camunda pour les processus, project44/FourKites pour la visibilité et CSCMP pour le périmètre logistique. Guides, définitions professionnelles et présentations commerciales n’ont pas le même niveau de preuve. Il ne s’agit pas d’un inventaire exhaustif des produits ni d’un classement. Les six référentiels sont revus sur leur mandat de projection ; les offres MDM ne sont pas comparées exhaustivement. Les sources existantes ne sont pas présentées comme intégralement reconsultées en U298.

## Ce que la comparaison révèle

| Famille de marché | Apport pour FLOW | Écart à conserver / précaution |
| --- | --- | --- |
| Microsoft SCM / Inventory Visibility | Politiques concrètes : besoin net, seuil/cible, ajustement des apports ; engagement logique ; distinction protection/consommation. | Le produit combine calcul, données, écrans et application. FLOW doit conserver décision et management séparés. S02, S08–S11, S26, S28. |
| SAP aATP / Fashion ARun | Engagements révisables, alternatives, affectation et contrôle de cohérence avant libération. | aATP est une famille produit, pas notre capacité ATP. ARun ne rend pas Assignment synonyme de protection de groupes. S04–S06, S24. |
| Oracle SCM | Compensation d’exécution, groupes de livraison cohérents, redistribution et collecte d’excédents. | Une orchestration produit ne fixe pas l’organisation FLOW. Vérifier les éditions : retrait du planning/jeopardy annoncé en 26D dans les notes 26B. S12, S17–S20, S25. |
| Manhattan / Blue Yonder | Choix de fulfillment croisant service, économie, stock et contraintes opérationnelles. | Justifie notre valeur multidimensionnelle ; ne justifie ni un comportement par indicateur ni un super-optimiseur implicite dans Assignment. S15–S16. |
| Kinaxis / RELEX | Arbitrage de risque et cibles coordonnées ; effets des aléas et, selon assortiment, de la périssabilité. | Appuis commerciaux de principe. Coordination multi-échelons et politiques de fraîcheur restent conditionnelles au besoin FLOW. S13–S14. |

La séparation FLOW est utile : une politique est configurée, une décision propose un résultat, un Order enregistre sa mise en action, puis des prestations sont orchestrées. La comparaison devient plus précise lorsque l’on aligne les **résultats métier** plutôt que les noms de modules.

## État courant des recommandations

| Capacité | Mécanismes proposés | Ce qu’ils rendent compréhensible |
| --- | --- | --- |
| Replenishment Decision | Demand-linked Replenishment ; Target-restoring Replenishment ; Committed Supply Adjustment | Couvrir des besoins, restaurer une cible, corriger des apports existants : trois logiques, pas quatre verbes de modification. P01–P03, S08–S09. |
| Execution Orchestration | P04 à réexaminer ; P05 retiré | P04 peut décrire le fonctionnement normal du parent ou un mécanisme de processus, sans bénéfice distinct. La compensation P05 relève de l’adaptabilité du processus dans le contexte U293. Le choix de variation et la coordination métier restent distincts. S17/S25/S32/S33. |
| Stock Redistribution Decision | Shortage-driven Rebalancing ; Excess Consolidation | Couvrir un manque et regrouper des excédents n’ont pas le même déclencheur. Excédent s’apprécie selon périmètre et horizon. P06–P07, S12. |
| Stocktaking | Recurring Stock Verification ; Triggered Stock Verification | Assurance régulière et réponse à un doute. Condition : préciser le mandat FLOW par rapport à l’exécutant. P08–P09, S01. |
| Execution Tracking | Logistics Visibility : nom adopté ; P10 à réexaminer | Parcours physique complet du picking au point final. P10 ne doit pas recopier les écarts déjà inclus ; une portée aux autres prestations doit apporter un bénéfice distinct. Niveau et rattachement à préciser. S29/S37/S38. |
| Order Lifecycle Management | Coordinated Order Release à clarifier | Gérer états et transitions de l’Order ; ne pas confondre avec la coordination des prestations. Le comportement distinct n’est pas établi. P11, S04/S18/S31. |

Les sept candidats encore à instruire sont P01–P03 (réapprovisionnement), P06–P07 (redistribution) et P08–P09 (fiabilisation). Aucun n’est adopté. P08/P09 demandent notamment de confirmer le mandat FLOW face aux exécutants. **U299 valide les deux corrections P04/P10** : les exceptions logistiques ne doivent pas être dupliquées ; coordonner des dépendances ne suffit pas à constituer un comportement autonome du parent. Les fiches initiales restent à réexaminer selon ces règles validées, pas à créer en l’état. Les autres propositions ne sont pas validées par cet accord.

La révision dépasse le nommage : le parcours logistique inclut les opérations d’entrepôt, les passages intermédiaires et leurs événements. Inventory Visibility reste complémentaire ; sortir d’un emplacement pour picking ne supprime pas la quantité du stock. FLOW doit recevoir les faits utiles sans prendre en charge les opérations internes des exécutants.

## Ce que je ne décomposerais pas encore

**Inventory Target Decision** : la prise en compte du risque et du service est déjà proche de sa définition. La coordination de plusieurs lieux peut justifier un comportement distinct si nous voulons arbitrer leurs buffers conjointement. Je propose deux fiches conditionnelles, sans forcer une symétrie avec les mécanismes de management.

**CTP** : ressources additionnelles, alternatives de fulfillment et redistribution d’engagements constituent trois familles possibles. Mais une alternative de site déjà admissible appartient à ATP ; une substitution produit doit être autorisée ; une révision d’engagement doit respecter sa fermeté. Nommer ces comportements avant de préciser ces frontières ferait réapparaître les recouvrements que la refonte vient de réduire.

**Reservation et Supply Assignment** : le premier sujet est le contrat entre lien ressource-commande et engagement opposable. Le second est la cohérence d’un plan collectif : des décisions localement valables peuvent réclamer la même ressource. Le marché intègre ces étapes dans des produits ; il ne tranche pas leur responsabilité dans notre modèle.

**Application de plan aux Orders** : le principe reste bon. Un plan peut changer une affectation sans changer une commande ; un autre modifie contenu, structure et statut. Le rattacher tout entier à Lifecycle serait parfois trop étroit. A03 reprend l’arbitrage A8 existant, sans ouvrir une nouvelle hiérarchie.

**Retours et fournisseurs** : devenir d’un retour et révision d’un engagement fournisseur méritent un travail spécifique. Ce sont peut-être des mécanismes manquants, mais peut-être d’abord des responsabilités à attribuer entre Supply, Business Services et exécutant. Ni remboursement ni négociation ne sont absorbés implicitement.

## Les quatorze comportements existants restent utiles

ATP couvre déjà les engagements, tous les lieux admissibles, le temps opérationnel et les ressources futures. Planning conserve construction de scénarios, simulation/analyse et adaptation. Protection distingue enveloppes de groupe, plafonds, stock de sécurité et régulation du réassort. Promise Management conserve proposition, confirmation et révision.

La prochaine amélioration est contractuelle : exclusions et recouvrements de quantités, dates de validité, droits de révision, impacts, données d’entrée et limites d’autonomie. Les politiques BOP peuvent enrichir Promise Revision ; elles ne justifient pas un niveau inférieur. Les modalités écran, API, masse ou streaming restent des moyens d’application.

## Ordre de travail proposé

1. **Logistics Visibility** : [proposition U300](positionnement-U300.md) de comportement sous Execution Tracking (D06), avec justification de continuité physique. Niveau, rattachement et justification à valider ; le nom U297 n’est pas remis en débat.
2. **Replenishment Decision** : instruire P01–P03 sur C02/C03 ; puis redistribution P06/P07 sur C04. Appui documentaire concret, prise en compte des excédents.
3. **Reservation / Assignment / promesse** : A01/A02/A05 sur C01/C07/C10. Ensuite seulement décider la décomposition CTP.
4. **Fiabilisation, orchestration et cycle de vie** : confirmer le mandat P08/P09 ; réexaminer P04/P10/P11 avant toute création. P05 demeure retiré comme comportement autonome.
5. **Frontières complémentaires** : application de plan, engagements fournisseurs, devenir des retours et cibles réseau. Les cas peuvent conduire à une clarification sans ajout de nœud.

La consolidation U298 actualise les noms courants, les statuts, la matrice et les priorités sans modifier le catalogue. Les noms antérieurs sont des traces historiques, pas des options à réactiver par défaut. Une relecture ciblée des sources sera nécessaire lorsque le périmètre d’un candidat évoluera ou avant son adoption ; pas de recherche générale répétée sans nouveau besoin. Les mécanismes, rattachements et responsabilités restant ouverts demandent le travail conjoint. Aucune release.

## Contrôles et limites

Le générateur vérifie les 39 capacités, les 14 comportements, les parents des candidats, les références et le maintien des octets du catalogue et des 125 fichiers publiés/protégés de la refonte. Ces contrôles établissent la cohérence documentaire ; ils ne valident pas les choix métier. Résultat dans [checks.json](checks.json).

Empreinte du modèle audité : `2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2`.

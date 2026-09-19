# Audit V0 — comparaison large des éditeurs

État comparé : backlog `2026-09-13.3` (`as_of: 2026-09-17`), lu le 2026-09-19. Empreinte des octets : `2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2`.

Dans le périmètre Supply retenu et les sources consultées, les grandes responsabilités étudiées trouvent des correspondances dans FLOW. Ce volet ne démontre aucun grand manque de domaine ni anomalie P0 ; il ne prouve pas la complétude du modèle ou du marché. Pour une V0 présentable, le travail prioritaire porte sur les contrats entre responsabilités, quelques définitions trop courtes et les interfaces avec les activités exclues.

**8 éditeurs, 27 éléments officiels consultés, 16 axes et les 47 capacités passées en matrice.** 41 capacités ont un nouveau rapprochement proposé dans ce volet ; les autres sont explicitement non re-comparées. 23 fiches capacité n’ont actuellement aucun `fields.market_comparisons` : c’est une mesure de documentation locale, pas de couverture marché.

Sur les 27 URL uniques ayant fait l’objet d’une tentative d’ouverture, **23 textes ont effectivement été lus** (15 documentations, cours ou annonce technique, 7 présentations de solution et 1 article expert) ; **4 preuves restent limitées aux passages officiels indexés** (SAP Help sans texte extractible et 3 pages IBM en erreur 403).

La preuve détaillée et les correspondances audit-locales MKT-V0/ELM-V0/CMP-V0 sont dans [marche-editeurs.yaml](marche-editeurs.yaml). Ce document explique les résultats ; le modèle demeure `modeles/backlog/model.yaml`. Aucun champ du catalogue, accord historique, publication ou registre marché partagé n’est modifié.

## Portée et qualité des preuves

| Éditeur | Rôle dans le contrôle | Nature de preuve |
| --- | --- | --- |
| SAP | Promesse, protection, réexamen collectif et release B2B/fashion | Cours et documentation ; un extrait Help limité |
| Oracle | Sourcing, coûts de promesse, retours et compensation | Documentation technique officielle |
| Microsoft | DOM, réservation, calendrier, consignation et intercompany | Documentation technique officielle |
| IBM | Scheduling, règles de fulfillment et alertes | Extraits officiels indexés ; ouverture 403 |
| Manhattan | Sourcing, arbitrage des coûts et retours omnicanaux | Présentation produit / article officiel, sans test |
| Blue Yonder | Promesse, routage retour et cycle de stock retail | Présentation produit / article officiel, sans test |
| RELEX | Prévisions externes, implantation, réassort et fin de vie | Présentation produit / article officiel, sans test |
| o9 | Cibles réseau, risque et scénarios de stock | Présentation produit / article officiel, sans test |

Une fonctionnalité produit peut traverser plusieurs capacités FLOW. La comparaison porte sur résultat, responsabilité et contexte, jamais sur une équivalence de niveaux. Les pages commerciales corroborent une finalité, sans prouver un algorithme, un paramétrage ni une performance. L’annonce Microsoft intercompany reste une **Preview** limitée initialement aux commandes retail. Les passages IBM ne permettent pas une conclusion sur la totalité du produit. Les versions et localisateurs sont conservés par source.

## Matrice de couverture par axe

| Axe | Éléments FLOW | Appréciation | Preuves |
| --- | --- | --- | --- |
| Promesse de référence et future | D03.i, D03.n, D01.c | couvert au niveau des responsabilités ; contrat temporel à préciser | ELM-V0-02, ELM-V0-04, ELM-V0-09, ELM-V0-11 |
| Adaptations et alternatives de satisfaction | D03.j, D06.e, D06.f | couvert ; ABC SAP traverse la frontière ATP/CTP FLOW | ELM-V0-02, ELM-V0-08, ELM-V0-10 |
| Arbitrage économique et priorités | D03.k, D03.l, D03.m, D03.o | couvert ; descriptions D03.k/l/m trop brèves | ELM-V0-01, ELM-V0-05, ELM-V0-10, ELM-V0-20, ELM-V0-22 |
| Protection, plafonds, réservations | D02.b, D02.c, D05.d, D05.h | couvert ; contrat de décompte et validité à éprouver | ELM-V0-11, ELM-V0-12, ELM-V0-17, ELM-V0-27 |
| Backlog collectif et réaffectation | D03.p, D03.o, D02.e, D04.o | couvert ; scénario de pénurie/gels à éprouver | ELM-V0-01, ELM-V0-03, ELM-V0-10 |
| Cibles locales et multi-échelons | D05.a, BHV026, BHV027, BHV028 | couvert ; entrée prévision et hypothèses à expliciter | ELM-V0-25, ELM-V0-27 |
| Implantation et réassort | D05.g, D05.e, D05.f | couvert ; contraintes tailles/capacité et articulation à tester | ELM-V0-24, ELM-V0-25, ELM-V0-26 |
| Redistribution et fin de saison | D05.c, BHV024, BHV025 | couvert partiellement ; qualification des apports finaux à instruire | ELM-V0-24, ELM-V0-26, ELM-V0-27 |
| Consignation et propriété | D01.h, D04.r, D04.j, D01.g | couvert ; pas de manque de capacité établi | ELM-V0-13 |
| Orders, composition et intercompany | D04.i, D04.j, D04.k, D04.n, D04.o | responsabilités représentées ; Transfer Order non re-comparé finement ; synchronisation et partiel à tester | ELM-V0-03, ELM-V0-10, ELM-V0-15, ELM-V0-16, ELM-V0-18 |
| Retours et récupération de valeur | D04.l, D04.m, D05.i | retour client et disposition rapprochés ; Supplier Return non re-comparé ; interfaces externes à représenter | ELM-V0-07, ELM-V0-21, ELM-V0-23 |
| Exécution, services et exceptions | D06.d, D06.e, D06.f, D07.b, D07.c, D07.d | couvert ; scénarios de compensation/escalade à expliciter | ELM-V0-06, ELM-V0-10, ELM-V0-19, ELM-V0-20 |
| Temps et capacité opérationnelle | D06.b, D13.a, D14.a, BHV003 | responsables présents ; contrats sources/dates/capacité insuffisamment précis | ELM-V0-08, ELM-V0-14, ELM-V0-15, ELM-V0-20, ELM-V0-22 |
| Prévisions, assortiment et coûts | D05.a, D05.g, D05.e, D03.k | interfaces externes à expliciter ; nouveaux domaines non justifiés | ELM-V0-05, ELM-V0-25, ELM-V0-26 |
| Maîtres et projections référentielles | D08.d, D09.d, D11.a, D12.a, D13.a, D14.a | appuis partiels sur usages ; ingestion/mastering non comparés finement | ELM-V0-04, ELM-V0-13, ELM-V0-14, ELM-V0-16, ELM-V0-24 |
| Comptage, archivage et traçabilité des mouvements | D01.d, D04.q, D01.g | non comparé à nouveau dans ce volet ; comparaisons existantes non revalidées ici | Non re-comparé |

## Écarts à traiter ou arbitrer

### MKT-F01 — P1 — Contrat temporel de promesse et de service insuffisamment explicite

**Constat FLOW.** Aucune occurrence de calendrier, calendar, cut-off ou fuseau dans les champs definition/scope/finality des nœuds. BHV003 couvre les délais réels, mais pas le contrat de calcul du temps.

**Recommandation proposée.** Préciser source des calendriers, jours fermés, heure limite, fuseau, date départ/réception, fraîcheur et conduite sur donnée inconnue ; consommer un maître externe.

**Preuve attendue pour la V0.** Un exemple vendredi après cut-off avec fermeture lundi aboutit à une promesse expliquée ; les lecteurs identifient responsable et données sans supposer un simple ajout de jours.

**Frontière.** Aucune nouvelle capacité Calendar Management proposée ; absence de mot ne suffit pas à conclure absence fonctionnelle.

Appuis consultés : [ELM-V0-14 — Set up a fulfillment source working calendar](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/setup-fulfillment-source-calendar); [ELM-V0-15 — Calculate requested ship dates for purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/supplier-requested-confirmed-dates); [ELM-V0-08 — Database Promising](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/fascp/overview-of-database-centric-order-promising.html).

### MKT-F02 — P1 — PTP, priorités et échéancier restent trop peu définis pour une revue solution

**Constat FLOW.** D03.l et D03.m ont un scope limité à un exemple fictif. D03.k expose une frontière et un exemple, sans inputs, résultat argumenté, coûts ni gestion des préférences incompatibles.

**Recommandation proposée.** Expliciter question, entrées, contraintes impératives, préférences, résultat, justification et absence de solution. Séparer choix économique PTP et compromis collectif multidimensionnel.

**Preuve attendue pour la V0.** Un même jeu de demandes permet de distinguer priorité, échéancier et arbitrage économique, sans fixer de pondération métier par défaut.

**Frontière.** Le marché justifie les responsabilités, pas une formule unique ni de nouveaux comportements par critère.

Appuis consultés : [ELM-V0-01 — Exploring Backorder Processing](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe); [ELM-V0-05 — Create Alternative Fulfillment Scenarios to Reduce Cost](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26c/fascp/create-alternative-fulfillment-scenarios-to-reduce-cost.html); [ELM-V0-10 — DOM rules](https://learn.microsoft.com/en-us/dynamics365/commerce/dom-rules); [ELM-V0-20 — Optimized Fulfillment Sourcing](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing).

### MKT-F03 — P1 — Réservation, affectation, promesse et consommation : contrat commun à rendre éprouvable

**Constat FLOW.** Les responsabilités sont distinctes ; plusieurs relations gardent la formulation engagements opposables selon frontière à arbitrer. Le contrat quantitatif de passage vers consommation reste un point V0 à expliciter.

**Recommandation proposée.** Fixer pour chaque quantité l’effet sur disponibilité, son identité, libération/expiration, consommation partielle et échec de confirmation ; distinguer engagement logique et ressources physiques.

**Preuve attendue pour la V0.** Deux canaux promettant la dernière quantité, puis une expédition partielle, ne la comptent ni deux fois disponible ni deux fois indisponible.

**Frontière.** Pas de réservation obligatoire ou taxonomie soft/hard imposée ; tester les mécanismes choisis et leurs limites.

Appuis consultés : [ELM-V0-11 — Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations); [ELM-V0-12 — Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation); [ELM-V0-08 — Database Promising](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/fascp/overview-of-database-centric-order-promising.html).

### MKT-F04 — P1 — Changements en cours d’exécution et exceptions : fermer la boucle de responsabilité

**Constat FLOW.** Tracking, adaptation et orchestration sont présents et reliés. Les textes ne forment pas encore un cas de preuve complet sur refus répétés, annulation trop tardive et réalisé irréversible.

**Recommandation proposée.** Éprouver seuil d’arrêt, acteur de résolution, latitude de dérogation, prestation déjà exécutée, correction/compensation et révision de promesse.

**Preuve attendue pour la V0.** Un rejet répété n’entraîne pas une boucle indéfinie ; une demande annulée après sortie physique conserve les faits et identifie la suite responsable.

**Frontière.** Pas de nouveau domaine générique Exception Management déduit d’une console éditeur ; les seuils restent à arbitrer.

Appuis consultés : [ELM-V0-06 — Compensate Sales Orders That Change](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html); [ELM-V0-10 — DOM rules](https://learn.microsoft.com/en-us/dynamics365/commerce/dom-rules); [ELM-V0-19 — Order Hub](https://www.ibm.com/docs/en/order-management?topic=features-order-hub).

### MKT-F05 — P1 — Prévisions, assortiment, saison et coûts externes : entrées à rendre visibles

**Constat FLOW.** D05.g consomme un assortiment retenu et D05.f les hypothèses/prévisions ; aucun élément explicitement nommé Demand Forecast ou Assortment Plan dans le catalogue. Le coût consommé par PTP n’a pas de contrat dédié lisible.

**Recommandation proposée.** Décrire dans une vue de contexte les producteurs externes à identifier, version/horizon/maille, données absentes et retours vers eux ; ne pas attribuer de maître sans preuve.

**Preuve attendue pour la V0.** Un expert peut dire d’où viennent besoins, assortiment et coûts, et distinguer prévision, engagement fournisseur et demande ferme sans ajouter Demand Planning à FLOW.

**Frontière.** Finance, prévision commerciale, assortiment et saison ne deviennent pas de nouveaux domaines par comparaison éditeur.

Appuis consultés : [ELM-V0-25 — AI-driven forecasting & replenishment for retail profitability](https://www.relexsolutions.com/resources/ai-driven-retail-forecasting-and-replenishment/); [ELM-V0-26 — Capabilities to prioritize when implementing merchandising systems](https://www.relexsolutions.com/resources/which-capabilities-to-prioritize-when-implementing-merchandising-systems/); [ELM-V0-05 — Create Alternative Fulfillment Scenarios to Reduce Cost](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26c/fascp/create-alternative-fulfillment-scenarios-to-reduce-cost.html).

### MKT-F06 — P1 — Retours : interface admission/remboursement/remplacement à expliquer

**Constat FLOW.** Les parcours et décisions logistiques sont riches ; les textes excluent explicitement autorisation commerciale, remboursement et remplacement client. Ces exclusions doivent déboucher sur des interfaces expliquées.

**Recommandation proposée.** Présenter l’origine de l’autorisation et les faits/quantités transmis aux responsables des suites commerciales/financières ; distinguer réparation même bien et remplacement.

**Preuve attendue pour la V0.** Un retour partiellement accepté puis partiellement renvoyé au client ne vaut pas remboursement total ; responsable et événement justificatif sont identifiés.

**Frontière.** Aucun domaine Finance ni remboursement ajouté à Return Disposition Decision ; aucune pratique Sarenza supposée.

Appuis consultés : [ELM-V0-07 — Don't Refund Lines That You Return to Your Customer](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/don-t-refund-lines-that-you-return-to-your-customer.html); [ELM-V0-21 — Returns Management](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/returns-management); [ELM-V0-23 — Smart Disposition](https://blueyonder.com/solutions/returns-management/smart-disposition).

### MKT-F07 — P2 — Fashion et B2B : compléter les cas de preuve, pas multiplier les capacités

**Constat FLOW.** Tailles, couleurs, conditionnements, assortiment utile, intercompany et complétude sont déjà mentionnés. La fin de saison et la synchronisation de la chaîne B2B nécessitent une démonstration transversale.

**Recommandation proposée.** Éprouver pack indivisible, assortiment incomplet, reliquat de fin de saison, livraisons groupées et changement d’Order intercompany ; préciser intention de chaque apport.

**Preuve attendue pour la V0.** Le cas distingue implantation, réassort, redistribution et affectation ; il identifie la demande non satisfaite à la maille taille/ligne sans accord implicite sur les règles.

**Frontière.** La final allocation éditeur n’est pas automatiquement la Stock Consolidation FLOW ; la frontière doit être décidée au cas métier.

Appuis consultés : [ELM-V0-03 — Backorder Processing — Supply Assignment](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html); [ELM-V0-16 — Cross-Legal-Entity Fulfillment in Dynamics 365 | Preview](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/08/19/cross-legal-entity-fulfillment-dynamics-365/); [ELM-V0-24 — What is Blue Yonder Allocation & Replenishment?](https://info.blueyonder.com/retail-planning-category-management/what-is-blue-yonder-allocation-replenishment); [ELM-V0-26 — Capabilities to prioritize when implementing merchandising systems](https://www.relexsolutions.com/resources/which-capabilities-to-prioritize-when-implementing-merchandising-systems/).

### MKT-F08 — P2 — Capacité opérationnelle disponible et concurrence à éprouver

**Constat FLOW.** D06.b distingue correctement plafond, charge et disponible communiqué et exclut une réservation implicite ; la concurrence de plans utilisant un même créneau reste à démontrer.

**Recommandation proposée.** Préciser qui atteste et engage la capacité, avec unité, créneau, fraîcheur et réponse de prise en charge ; signaler conditionnel ou inconnu.

**Preuve attendue pour la V0.** Deux décisions consommant simultanément un créneau limité ne confondent pas information de capacité et engagement confirmé.

**Frontière.** Ne pas inventer Capacity Reservation dans FLOW si l’engagement reste chez l’exécutant ; identifier cette dépendance externe.

Appuis consultés : [ELM-V0-08 — Database Promising](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/fascp/overview-of-database-centric-order-promising.html); [ELM-V0-20 — Optimized Fulfillment Sourcing](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing); [ELM-V0-22 — Order Promising & Optimization](https://blueyonder.com/solutions/order-management-and-commerce/order-promising-and-optimization); [ELM-V0-24 — What is Blue Yonder Allocation & Replenishment?](https://info.blueyonder.com/retail-planning-category-management/what-is-blue-yonder-allocation-replenishment).

### MKT-F09 — P1 — Comparaisons marché des fiches trop inégales pour la V0

**Constat FLOW.** Ces capacités n’ont pas de fields.market_comparisons dans le modèle lu alors que l’audit dispose de rapprochements précis. Cela mesure une documentation locale, jamais une absence marché.

**Recommandation proposée.** Après revue, reporter les rapprochements utiles et leurs limites dans les fiches selon U311 ; conserver les correspondances proposées tant qu’elles ne sont pas validées.

**Preuve attendue pour la V0.** Chaque fiche prioritaire montre au moins un appui pertinent, sa différence avec FLOW et sa date ; aucune étiquette validée ou réalisée déduite.

**Frontière.** Cet audit écrit une annexe isolée ; il ne modifie pas les champs modèle ni les registres MKT/ELM/CMP existants.

Appuis consultés : [ELM-V0-01 — Exploring Backorder Processing](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe); [ELM-V0-05 — Create Alternative Fulfillment Scenarios to Reduce Cost](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26c/fascp/create-alternative-fulfillment-scenarios-to-reduce-cost.html); [ELM-V0-09 — Order promising](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations); [ELM-V0-11 — Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations); [ELM-V0-12 — Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation); [ELM-V0-14 — Set up a fulfillment source working calendar](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/setup-fulfillment-source-calendar).

## Ce que le marché ne justifie pas d’ajouter

- Un domaine ATP avancé : SAP aATP est un regroupement produit ; ATP, CTP, protections, priorités, affectation et promesse ont des frontières explicites dans FLOW.
- De nouveaux comportements de retours par code éditeur : D04.l, D04.m et D05.i couvrent déjà parcours, politiques et récupération de valeur.
- Un domaine MEIO : BHV028 est déjà rattaché à Inventory Target Decision ; o9 ne justifie pas d’en faire une nouvelle hiérarchie.
- Forecasting, Pricing, Finance, atelier de production ou WMS internes : les interfaces peuvent être nécessaires, leur réalisation demeure hors périmètre retenu.
- Une capacité par écran, algorithme, taille, seuil, canal ou type d’erreur. Démontrer d’abord une responsabilité durable ou un bénéfice de décomposition.

## Compléments non couverts par cette comparaison

La matrice n’est ni un benchmark de sélection produit ni une preuve d’exhaustivité du marché. Les six capacités sans nouvelle correspondance sont Stocktaking (D01.d), Transfer Order (D04.k), Supplier Return (D04.m), Service Requirements Decision (D07.a), Catalog Ingestion (D12.a) et Order Archiving (D04.q). Leur présence dans un axe apporte le contexte FLOW, sans nouvelle validation marché détaillée. Les comparaisons déjà inscrites sur leurs fiches restent dans leur état antérieur. Les rapprochements sur les autres ingestions portent surtout sur les informations utilisées, pas sur le mastering. Les interfaces retail/B2B et les scénarios de retour sont à éprouver avec les experts ; aucun existant Sarenza ou déploiement Beaumanoir n’est inféré.

## Index des passages effectivement consultés

| ID | Source et passage | Édition / accès |
| --- | --- | --- |
| ELM-V0-01 | [Exploring Backorder Processing](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe) — Backorder Processing Overview ; Confirmation Strategies ; Implementing Backorder Processing | Cours S/4HANA Cloud Public Edition évolutif ; pas de numéro de release affiché ; passage_consulte |
| ELM-V0-02 | [Using Advanced Available-To-Promise (aATP) in SAP S/4HANA](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5) — Product Availability Check ; Alternative-Based Confirmation ; Release for Delivery | Cours S/4HANA évolutif, plusieurs générations présentées ; passage_consulte |
| ELM-V0-03 | [Backorder Processing — Supply Assignment](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html) — Requirement Selection ; Requirement Sorting ; Release rule for supply assignment | 2025 FPS01 (Feb 2026), version affichée dans le passage indexé ; passage_indexe_consulte_ouverture_sans_texte |
| ELM-V0-04 | [Set Up Promising Rules and Sourcing Rules for Order Management](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/set-up-promising-rules-and-sourcing-rules-for-order-management.html) — Introduction ; Create Your Sourcing Rule ; Assign Your Sourcing Rule | Oracle Cloud SCM 26A ; passage_consulte |
| ELM-V0-05 | [Create Alternative Fulfillment Scenarios to Reduce Cost](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26c/fascp/create-alternative-fulfillment-scenarios-to-reduce-cost.html) — Introduction ; cost table ; Promise According to Arrival Date | Oracle Cloud SCM 26C ; passage_consulte |
| ELM-V0-06 | [Compensate Sales Orders That Change](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html) — Introduction ; example Create Shipment Redo ; compensation pattern | Oracle Cloud SCM 26B ; passage_consulte |
| ELM-V0-07 | [Don't Refund Lines That You Return to Your Customer](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/don-t-refund-lines-that-you-return-to-your-customer.html) — Return flows ; orchestration rule for Create Billing Lines | Oracle Cloud SCM 26B ; passage_consulte |
| ELM-V0-08 | [Database Promising](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/fascp/overview-of-database-centric-order-promising.html) — Promising Horizon and Other Order Promising Options ; Suppliers and Supplier Capacity | Oracle Cloud SCM 26A ; passage_consulte |
| ELM-V0-09 | [Order promising](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations) — Delivery date control methods ; ATP calculations | Documentation évolutive SCM, édition logicielle non unique ; passage_consulte |
| ELM-V0-10 | [DOM rules](https://learn.microsoft.com/en-us/dynamics365/commerce/dom-rules) — Common attributes ; Partial orders rule ; Maximum rejects rule ; Offline fulfillment location rule | Documentation mise à jour 2026-01-22 ; paramètres dépendant des versions Commerce ; passage_consulte |
| ELM-V0-11 | [Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations) — Sample use case for soft reservation ; Integrate soft reservations and offsets | SCM 10.0.33+ pour soft reservations sales orders ; dépendances de versions décrites dans la page ; passage_consulte |
| ELM-V0-12 | [Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation) — Allocation workflow ; Consume as a soft reservation | Documentation évolutive ; UI versions 1 et 2 distinguées ; passage_consulte |
| ELM-V0-13 | [Set up consignment](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment) — Consignment replenishment orders ; Inventory ownership change journal | Documentation évolutive SCM ; passage_consulte |
| ELM-V0-14 | [Set up a fulfillment source working calendar](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/setup-fulfillment-source-calendar) — Working hours ; time zone ; Using a calendar for Fulfillment optimization ; carrier pickup times | Documentation mise à jour 2026-01-30 ; passage_consulte |
| ELM-V0-15 | [Calculate requested ship dates for purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/supplier-requested-confirmed-dates) — Key terms and concepts ; calculation logic ; recalculations for updated orders | SCM 10.0.40+ et Planning Optimization, prérequis explicités ; passage_consulte |
| ELM-V0-16 | [Cross-Legal-Entity Fulfillment in Dynamics 365 | Preview](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/08/19/cross-legal-entity-fulfillment-dynamics-365/) — What we are releasing ; How it works ; initial release supports retail orders | Annonce officielle du 2026-08-19, Preview ; périmètre initial retail ; passage_consulte |
| ELM-V0-17 | [Scheduling shipment of an order or order line](https://www.ibm.com/docs/en/order-management?topic=shipped-scheduling-shipment-order-order-line) — Status control ; Earliest schedule date | Documentation SaaS évolutive, release non établie ; passage_indexe_consulte_ouverture_403 |
| ELM-V0-18 | [Defining fulfillment rules](https://www.ibm.com/docs/en/order-management?topic=components-defining-fulfillment-rules) — Split partially backordered or unscheduled lines ; use node from work order | Documentation SaaS évolutive, release non établie ; passage_indexe_consulte_ouverture_403 |
| ELM-V0-19 | [Order Hub](https://www.ibm.com/docs/en/order-management?topic=features-order-hub) — Manage alerts ; Managing exceptions ; sourcing and scheduling rules | Documentation SaaS évolutive, release non établie ; passage_indexe_consulte_ouverture_403 |
| ELM-V0-20 | [Optimized Fulfillment Sourcing](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/optimized-fulfillment-sourcing) — Fulfillment Sourcing Optimization ; Improving Profitability ; Ensuring Promises | Page produit évolutive sans numéro de version ; presentation_consultee |
| ELM-V0-21 | [Returns Management](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/returns-management) — Returns Done Right ; Maximize Returns Profitability | Page produit évolutive sans numéro de version ; presentation_consultee |
| ELM-V0-22 | [Order Promising & Optimization](https://blueyonder.com/solutions/order-management-and-commerce/order-promising-and-optimization) — Accuracy in delivery dates ; Lower cost to serve ; Smart resource allocation | Page produit évolutive sans numéro de version ; presentation_consultee |
| ELM-V0-23 | [Smart Disposition](https://blueyonder.com/solutions/returns-management/smart-disposition) — Intelligent routing ; Configure and enforce policy ; Customizable reason codes and rules | Page produit évolutive sans numéro de version ; presentation_consultee |
| ELM-V0-24 | [What is Blue Yonder Allocation & Replenishment?](https://info.blueyonder.com/retail-planning-category-management/what-is-blue-yonder-allocation-replenishment) — Key Capabilities 1–4 ; Push vs Pull ; lifecycle | FAQ produit 2026, édition logicielle non indiquée ; presentation_consultee |
| ELM-V0-25 | [AI-driven forecasting & replenishment for retail profitability](https://www.relexsolutions.com/resources/ai-driven-retail-forecasting-and-replenishment/) — How RELEX helps ; 6 keys ; seasonal planning | Article évolutif, édition logicielle non indiquée ; presentation_consultee |
| ELM-V0-26 | [Capabilities to prioritize when implementing merchandising systems](https://www.relexsolutions.com/resources/which-capabilities-to-prioritize-when-implementing-merchandising-systems/) — Traditional processes ; initial allocation ; final allocation ; evolution of merchandising | Article expert officiel, pas catalogue normatif de capacités ni version logicielle ; passage_consulte_article_expert |
| ELM-V0-27 | [How o9’s Multi-Echelon Inventory Optimization (MEIO) Software Works](https://o9solutions.com/solutions/supply-chain-planning/multi-echelon-inventory-optimization-docs) — Optimal Inventory Targets and Network Rebalancing ; Postponement ; Scenario Planning for Inventory Risk | Page solution évolutive, sans édition logicielle malgré le suffixe docs ; presentation_consultee |

Consultation de chaque source : 2026-09-19. Les synthèses sont originales et courtes ; aucun droit de redistribution intégrale du contenu tiers n’est présumé.

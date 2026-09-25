# Respect des règles — U773, recherche de marché U774

Le backlog reste **partiellement documenté au regard du minimum Microsoft Dynamics + SAP S/4HANA**. La recherche part des responsabilités FLOW et ajoute les correspondances utiles dans les fiches du modèle et du glossaire. Elle ne transforme pas une fonction produit en capacité et ne modifie pas le découpage pour obtenir artificiellement deux références.

62 documents primaires ont été exploités dans 224 rapprochements : 108 fiches métier et 59 termes enrichis ou réexaminés. Chaque rapprochement indique le mécanisme documenté, sa source, la date de consultation, les points communs et les limites. Deux autres pages SAP Help sur les prestations fashion restent des pistes à corps inaccessible ; elles ne sont pas ajoutées comme preuves consultées dans les fiches.

| Présence des deux familles produit | Avant U774 | Après U774 | Encore non établie |
| --- | --- | --- | --- |
| Fiches métier | 19/165 | 112/165 | 53 |
| Termes du glossaire | 21/124 | 56/124 | 68 |

Ces compteurs constatent la présence de références identifiables. Ils **ne certifient pas une équivalence de périmètre** ni la relecture de chaque ancienne référence. Les 224 rapprochements U774 ont une portée partielle explicitée ; les autres commentaires restent soumis à leurs preuves antérieures. Les publications historiques restent figées.

## Exemples de correspondances vérifiées

| Sujet FLOW | Dynamics | SAP S/4HANA | Frontière conservée |
| --- | --- | --- | --- |
| Kitting Order | [Process kit assembly and disassembly orders](https://learn.microsoft.com/en-us/dynamics365/commerce/process-kit-assembly-and-disassembly-orders) | [Performing Value-Added Services (VAS)](https://learning.sap.com/courses/exploring-business-processes-for-supply-chain-execution-in-sap-s-4hana-cloud-private-edition/performing-value-added-services-vas-) | Microsoft distingue assemblage et désassemblage ; la source SAP étaye le kitting. FLOW conserve une seule famille, sans réintroduire Value-Added Service Order. |
| Transport et suivi | [Transportation management statuses](https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/transportation-management-status) | [Managing Freight Orders and Freight Bookings](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-transportation-management/managing-freight-orders-and-freight-bookings_a83a6371-2f56-4fa2-8e12-ae0aab3c74c2) | Ordres, échanges de statut et connaissance de la progression restent distincts. |
| Ingestion des référentiels | [Exchange data between systems](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-exchange-data) | [Introducing the Retail Article Master](https://learning.sap.com/courses/discovering-retail-functions-and-business-processes-in-sap-s-4hana-retail/introducing-the-retail-article-master_bd2d9df6-bf54-4612-8fa0-b35c63fbb0d8) | Les échanges sont documentés ; les domaines sources Commerce, Finance et Design restent des choix FLOW. |
| Packing Order | [Packing work for packing outbound containers and processing shipments](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/packing-work) | [Integrating into Warehouse Processes](https://learning.sap.com/courses/business-processes-in-sap-s-4hana-transportation-management/integrating-into-warehouse-processes_a60ea8b3-d0d8-4c89-be2f-7a4a912240c4) | Les travaux exécutables WMS éclairent la prestation ; ils ne définissent pas toute la demande de service. |
| PTP et coûts | [Landed cost module overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/landed-cost-overview) | [Configuring Charge Management and Explaining the Charge Calculati](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-transportation-management/configuring-charge-management-and-explaining-the-charge-calculation-process_d2c3b050-5874-4439-a88e-8dcfa231311c) | Ces sources étayent des coûts. Elles ne prouvent ni un dossier économique contextuel exhaustif ni un PTP natif SAP équivalent. |
| Encaissement confié | [Manage payment authorizations](https://learn.microsoft.com/en-us/dynamics365/commerce/dev-itpro/manage-payment-authorizations) | [Explaining Digital Payments](https://learning.sap.com/courses/configuring-additional-settings-in-financial-accounting-in-sap-s-4hana/explaining-digital-payments) | L’autorisation ou un accusé de capture ne suffisent pas toujours à connaître le résultat final asynchrone. |
| Dédouanement confié | [Work with customs clearance](https://learn.microsoft.com/en-us/dynamics365/finance/localizations/russia/rus-work-with-customs-clearance) | [Describing the Integration into SAP Global Trade Services](https://learning.sap.com/courses/introducing-the-sap-s-4hana-for-international-trade/describing-the-integration-into-sap-global-trade-services_a4529c6b-0cb6-4361-944a-a5c0b540745b) | Dynamics : localisation Russie, pas preuve France. SAP : délégation de S/4HANA vers GTS, exécutant distinct. |

## Ce qui reste à établir

- Des appuis précis des deux éditeurs pour les prestations textiles spécialisées : finition, nettoyage, personnalisation et certaines retouches. Les mentions de services génériques ou de personnalisation logicielle ne suffisent pas.
- Les stratégies fines : optimisation multi-échelon, réservation adaptative au risque, propriété liée à l’ancienneté et évaluation économique contextuelle complète. Une opération voisine n’est pas une preuve de la stratégie.
- Les variantes et autres fiches restantes, identifiées individuellement dans `market_coverage` et `research_U774.remaining_missing` de l’annexe. Une recherche infructueuse ne démontre pas une absence de fonctionnalité chez l’éditeur.
- Les notions génériques du glossaire : les documents applicatifs ne donnent pas nécessairement une définition pertinente de « capacité », « domaine » ou de tous les verbes. Le minimum demandé reste non satisfait sur ces fiches ; aucune exception n’est décidée ici.

ARun affecte les ressources ; BOP réexamine les confirmations. La documentation SAP conserve cette différence de question métier. Le MRP ne représente pas tout le master plan FLOW. Une vague d’entrepôt étaye la libération groupée mais ne prouve pas, seule, la rétention décidée en amont par l’orchestration.

## Contrôles

La validation complète du modèle et les contrôles de livraison des lots sont exécutés sur l’état final. Les 72 capacités ont une catégorie ; les 75 comportements ont chacun un parent et respectent la règle zéro ou au moins deux ; 23 scénarios relient les 72 capacités. Ces résultats structurels ne démontrent pas une exhaustivité métier ou une réalisation installée.

Les nouvelles comparaisons ont été alignées entre modèle et glossaire sur les notions communes, sans changer les définitions pour les rapprocher d’un produit. Les choix de périmètre restent explicites. Les comparaisons nouvelles sont proposées, sans extension des accords antérieurs.

Le validateur technique contrôle la pluralité des documents, mais ne garantit ni la pertinence sémantique ni le minimum par famille produit. Les règles d’Atlas, de publication et de preuve terrain ne sont pas certifiées par un contrôle du seul YAML. Aucun déploiement Beaumanoir n’est déduit des documents du marché.

Les écarts et les correspondances sont suivis dans [l’annexe du backlog](../modeles/backlog/rule-compliance-U773.yaml), seule liste de suivi. [CMP307](../marche/comparaisons.md#cmp307) conserve la synthèse de recherche. Aucun release, commit ou push n’est effectué.

# Sources de l’audit U176

Consultation : 14 septembre 2026. Sources primaires ; versions et limites ci-dessous. Pas de configuration Beaumanoir déduite.

## S01

[SAP — Material / Product Master](https://learning.sap.com/courses/business-processes-in-sap-s-4hana-transportation-management/using-materials-master-data-for-transportation-management_e2173208-52f7-4ea7-a715-80fda149121e)

- Version : S/4HANA TM, version de cours non affichée.
- Accès : Texte consulté.
- Passage : Material Master ; Material Types.
- Apport : Référentiel transversal, incluant services et emballages ; origine historique du mot non établie.

## S02

[SAP — Retail Article Master](https://learning.sap.com/courses/discovering-retail-functions-and-business-processes-in-sap-s-4hana-retail/introducing-the-retail-article-master_bd2d9df6-bf54-4612-8fa0-b35c63fbb0d8)

- Version : S/4HANA Retail, version de cours non affichée.
- Accès : Texte consulté.
- Passage : Article Categories ; unités ; structured articles.
- Apport : Articles génériques, variantes, sets et prepacks ; plusieurs mailles de gestion et unités.

## S03

[SAP — Units of Measure in Inventory Management](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/91b21005dded4984bcccf4a69ae1300c/f962bd534f22b44ce10000000a174cb4.html)

- Version : 2025 FPS01, février 2026.
- Accès : Texte indexé consulté ; ouverture sans texte.
- Passage : Base unit / stockkeeping unit.
- Apport : Stockkeeping unit peut désigner l’unité de mesure du stock ; conversions depuis les unités de saisie.

## S04

[SAP — Maintaining Handling Units](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-warehouse-management/maintaining-handling-units-hu-_dcf41902-7052-4c3c-bbc0-2bab1a918e69)

- Version : S/4HANA Cloud Public Edition, cours non versionné.
- Accès : Texte consulté.
- Passage : Handling Unit.
- Apport : HU physique, emballage et contenu ; identité et imbrication.

## S05

[SAP — Serial Numbers with Material Stock](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/eb2a39dd0c124fed8252f684002d55e1/a8e46aae952f489bb57f242580cc365d.html?version=2023.latest)

- Version : 2023.latest.
- Accès : Texte indexé consulté ; ouverture sans texte.
- Passage : A_MaterialSerialNumber.
- Apport : Material, numéro de série, lot et position de stock distincts dans le modèle de données.

## S06

[SAP — Batch](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f340785101c548c9beeda9284efd18a0/8bfeb753128eb44ce10000000a174cb4.html?locale=en-US&state=PRODUCTION&version=2025.001)

- Version : 2025 FPS01.
- Accès : Texte indexé consulté ; ouverture sans texte.
- Passage : Définition Batch.
- Apport : Lot rattaché à un Material ; homogénéité selon les spécifications de production.

## M01

[Microsoft — Product information overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information)

- Version : Dynamics 365 SCM, documentation en ligne.
- Accès : Texte consulté.
- Passage : Products ; product masters ; variants ; released products.
- Apport : Product peut être Item ou Service ; famille, variante et mise à disposition dans une entité juridique distinctes.

## M02

[Microsoft — Product identifiers](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-identifiers)

- Version : Dynamics 365 SCM, documentation en ligne.
- Accès : Texte consulté.
- Passage : Product number ; item number ; GTIN.
- Apport : Identité produit globale, référence par entité juridique et identification des variantes ; conditionnements et GTIN.

## M03

[Microsoft — Set up stockkeeping units](https://learn.microsoft.com/en-us/dynamics365/business-central/inventory-how-to-set-up-stockkeeping-units)

- Version : Business Central, documentation en ligne.
- Accès : Texte consulté.
- Passage : Stockkeeping units.
- Apport : SKU est une fiche Item pour lieu et/ou variante, avec données spécifiques de gestion.

## M04

[Microsoft — Manage units of measure](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/tasks/manage-unit-measure)

- Version : Dynamics 365 SCM, documentation en ligne.
- Accès : Texte consulté.
- Passage : Unit classes ; decimal precision ; conversions.
- Apport : Mesures et précision gérées indépendamment de l’identité produit.

## M05

[Microsoft — Pack containers for shipment](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/packing-containers)

- Version : Dynamics 365 SCM, documentation en ligne.
- Accès : Texte consulté.
- Passage : Containers ; packing ; license plates.
- Apport : Conteneur physique, contenu, poids et référence d’expédition ; aucune équivalence générale LP/Container/SSCC démontrée.

## M06

[Microsoft — Item and raw material tracing](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/trace-items-raw-materials-inventory-production-sales)

- Version : Dynamics 365 SCM, documentation en ligne.
- Accès : Texte consulté.
- Passage : Tracking dimensions.
- Apport : Article, dimensions produit, lot/série et stockage distincts.

## M07

[Microsoft — Set up units of measure](https://learn.microsoft.com/en-us/dynamics365/business-central/inventory-how-setup-units-of-measure)

- Version : Business Central, documentation en ligne.
- Accès : Texte consulté.
- Passage : Base unit ; alternate units ; rounding.
- Apport : Unités de stock, achat, production et vente ; conversion et arrondi des quantités.

## G01

[GS1 — System Architecture](https://ref.gs1.org/architecture/system-architecture/)

- Version : 12.0.0, octobre 2024.
- Accès : Sections textuelles consultées.
- Passage : Tables 4-1 et 6-1.
- Apport : Identités de classe, lot, exemplaire et unité logistique distinctes ; GTIN, GTIN+lot/série, SSCC.

## G02

[GS1 — Logistic Label Guideline](https://ref.gs1.org/guidelines/logistic-label/)

- Version : 1.3, juillet 2019.
- Accès : Sections du PDF consultées.
- Passage : §4.1–4.5, pages imprimées 14–18.
- Apport : Unité logistique potentiellement aussi commerciale ; un article commercial peut être expédié en plusieurs morceaux/colis.

## G03

[GS1 — Global Data Model Attribute Implementation Guideline](https://ref.gs1.org/guidelines/gdm-implementation/1.13.0/)

- Version : 1.13, novembre 2024.
- Accès : Sections du PDF consultées.
- Passage : §2, page imprimée 25, attributs 56–59.
- Apport : Base, consumer, orderable et shipping unit sont des qualifications distinctes ; maille commerciale relative à la hiérarchie.

## G04

[GS1 Finland — Creating a variable-measure item](https://gs1.fi/en/customer-support/synkka/gs1-synkka-creating-variable-measure-item)

- Version : Guide Synkka en ligne, édition non établie.
- Accès : Texte consulté.
- Passage : Introduction.
- Apport : Mesures variables dans les transactions, tissus et rouleaux notamment.

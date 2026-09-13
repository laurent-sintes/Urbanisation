# Éléments de référence examinés

État : 2026-09-09. Les identifiants ELM sont des clés locales de traçabilité, jamais des identifiants attribués par les organismes. Les six libellés IBM ci-dessous constituent une sélection, pas la reproduction de sa carte.

## ELM001

- Référence : [MKT04](catalogue.md#mkt04), SAP RBA.
- Élément : trois niveaux de décomposition (Business Domain, Business Area, Business Capability), regroupés au niveau supérieur Enterprise Domain ; libellés et sources dans MKT04. Correction U24/C31 du 2026-09-09.
- Localisateur : leçon Defining Business Architecture, passage sur les niveaux de granularité ; complément Discovering the Reference Architecture Content, sections Reference Architecture Content Example et Business Capability Model Example, pour Enterprise Domain.
- Version : cours public consulté le 2026-09-09, édition du catalogue non établie.
- Nature : convention de structuration ; identifiant natif non fourni dans la leçon.
- Reformulation : rattacher une capacité à une aire métier, puis à un domaine métier, lui-même regroupé dans un domaine d’entreprise. La chaîne complète comporte quatre niveaux visibles.
- Limite : aucune correspondance automatique avec les trois niveaux proposés pour Beaumanoir.

## ELM002

- Référence : [MKT04](catalogue.md#mkt04), même leçon.
- Élément : séparation entre capacités, activités de processus et capacités de solution.
- Localisateur : passages décrivant les architectures métier et de solution.
- Version : même état documentaire que ELM001.
- Nature : règle de métamodèle ; identifiant natif non fourni.
- Reformulation : distinguer le besoin métier, son déroulement et son support logiciel.
- Limite : les liens locaux doivent encore être définis et validés.
- Réexamen U48 du 2026-09-10 : [Defining Business Architecture](https://learning.sap.com/courses/intelligent-enterprise-architecture-fundamentals/defining-business-architecture), passages sur les modèles de capacités, de processus et de solution consultés. Édition non précisée. Appui de CMP029 ; aucune exclusion universelle de la coordination des cartes métier déduite.

## Sélection IBM

Source commune : [MKT06](catalogue.md#mkt06), publication G510-6163-00, 2005, figure 6, page PDF 11 (page imprimée 9). Consultation du texte de la figure le 2026-09-09. Nature : composants d'un exemple retail. Identifiants natifs non fournis ; définitions détaillées absentes de l'extrait. Les reformulations françaises servent uniquement au repérage.

| Identifiant local | Libellé natif | Reformulation de repérage |
| --- | --- | --- |
| ELM003 | Item management | Gestion des articles |
| ELM004 | Allocation | Allocation |
| ELM005 | Replenishment | Réassort |
| ELM006 | Order management | Gestion des commandes |
| ELM007 | Customer service | Service client |
| ELM008 | Reverse logistics | Logistique des retours |

La définition native demeure « non disponible dans le passage consulté » pour ELM003–ELM008. Les correspondances sont donc limitées à des pistes lexicales. La sélection ne fixe ni leur place dans notre hiérarchie ni leur responsabilité organisationnelle.

## Appuis pour les deux couches

Examen du 2026-09-09 par Codex, à partir de U18/U19. Les définitions ci-dessous sont reformulées, sans citation normative littérale. Les sources officielles, éditions et limites d'accès sont centralisées dans les fiches MKT indiquées ; aucun identifiant natif distinct du localisateur n'est attribué à ces concepts.

### ELM009

- Référence : [MKT04](catalogue.md#mkt04), leçons SAP publiques, édition inconnue ; approfondissement de ELM002.
- Libellés natifs : *Business Capability Model*, *Business Process Model*, *Solution Capability*, *Solution Process*. Nature : distinction de métamodèle.
- Localisateur : *Discovering the Reference Architecture Content*, sections *Linking Business and Solution* et *RBA Link to RSA* ; *Designing Application Architecture*, *Product Map* et *Solution Process*.
- Définition reformulée : capacités et processus sont deux modèles métier indépendants des solutions ; leurs réalisations sont décrites séparément et reliées aux composants.
- Limite : ne prescrit pas que les capacités appartiennent exclusivement au socle transactionnel, ni que les processus seraient dépourvus de modèle métier propre.

### ELM010

- Référence : [MKT09](catalogue.md#mkt09), SOA-RM 1.0, 12 octobre 2006.
- Libellés natifs : *Service*, *Service Description*, *Policies and Contracts*. Nature : concepts d'architecture de services.
- Localisateur : §§3.1, 3.3.1 et 3.3.2.
- Définition reformulée : le service ouvre l'accès à des capacités ; sa description et ses politiques/contrats précisent les conditions d'interaction.
- Limite : ne constitue ni notre contrat métier complet, ni un choix HTTP, événementiel ou de plateforme.

### ELM011

- Référence : [MKT10](catalogue.md#mkt10), CMMN 1.1, décembre 2016.
- Libellés natifs : *Case*, *Case File*, *Case Plan Model*, *Case Roles*, *Tasks*. Nature : concepts de modélisation de dossiers.
- Localisateur : §§4.1, 4.3 et 5.2.2.
- Définition reformulée : un dossier articule informations, plan de traitement, rôles et tâches ; c'est un appui pour décrire les objets et comportements de la couche haute.
- Limite : la persistance durable et l'urbanisation propres demandées par U19 restent des exigences locales ; CMMN n'impose ici ni schéma de stockage ni modèle RBAC complet.

### ELM012

- Référence : [MKT11](catalogue.md#mkt11), OpenAPI Specification 3.2.0, introduction.
- Libellé natif : *OpenAPI Specification*. Nature : format de description d'interfaces.
- Définition reformulée : description d'API HTTP indépendante du langage de programmation.
- Limite : candidat pour la représentation d'un contrat ; sa sémantique et sa politique de compatibilité restent à définir.

### ELM013

- Référence : [MKT12](catalogue.md#mkt12), AsyncAPI Specification 3.0.0, introduction.
- Libellé natif : *AsyncAPI Specification*. Nature : format de description d'interfaces à messages.
- Définition reformulée : description des interfaces d'applications qui échangent des messages.
- Limite : ne détermine ni les faits métier publiés, ni les garanties de livraison ou d'évolution du contrat.

## Stock SAP

Examen sélectif du 2026-09-09 par Codex en réponse à U22/U23. Versions de catalogue/produit inconnues, limites dans MKT04/MKT13 ; aucun identifiant natif fourni par les passages consultés. ELM015–ELM018 sont des fonctions de solution, pas des feuilles RBA nouvellement découvertes. Reformulations françaises distinctes des libellés natifs.

### ELM014

- Référence : [MKT04](catalogue.md#mkt04), [cours RBA](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), section *Business Capability Model Example*, première image, lue visuellement.
- Nature : extrait de hiérarchie métier et sélection de capacités.
- Libellés natifs sélectionnés : *Inventory Management*, *Order Promising*, *Warehouse Management* (Business Areas) ; *Goods Receipt Processing*, *Physical Inventory*, *Product Availability Check*, *Product Allocation Check* (Business Capabilities).
- Rattachement : les trois aires relèvent du Business Domain *Supply Chain Execution*, lui-même regroupé sous l’Enterprise Domain *Supply – Fulfill Demand* (complément U24/C31, 2026-09-09). Les deux premières capacités citées relèvent de la gestion des stocks ; les deux suivantes de la promesse de commande.
- Définition détaillée : non fournie dans l’image. Reformulation : distinguer tenue/mouvements/comptage du stock, promesse et exécution en entrepôt.
- Limite : extrait pédagogique, sans export exhaustif ni correspondance automatique avec nos niveaux ou organisations. La [note](sap-stock.md) décrit les autres feuilles observées en français.
- Réexamen U43 du 2026-09-10 : S1, sections sur Enterprise Domains, structure et exemple du modèle ; texte consulté pour les premiers regroupements. [Analyse et limites](premier-niveau-regroupement-capacites.md), CMP026 ; ancienne provenance conservée.
- Réexamen U51 du 2026-09-10 : même cours SAP, sections Reference Architecture Content Example/Framework/Business Capability Model Example consultées ; hiérarchie et exemple stock/promesse confirmés, Sourcing and Procurement repéré comme domaine. Édition du catalogue toujours inconnue. CMP031 compare des options locales, sans équivalence de domaines complets.
- Réexamen U53 du 2026-09-10 : Business Capability Model Example reconsulté ; Order Promising, Inventory Management, Warehouse Management et Transportation Management demeurent distingués sous Supply Chain Execution. Leur regroupement supérieur ne vaut pas adoption du périmètre Supply – Fulfill Demand ; CMP032.

- Réexamen U59 du 2026-09-10 : même cours, sections Framework et Business Capability Model Example ; la maille Business Area est proposée comme point de comparaison pour les domaines locaux. La hiérarchie complète est conservée ; CMP033/P78 ne valident ni chaque aire comme espace problématique local ni le catalogue principal.

- Précision U66/U67, 2026-09-11 : [ELM067](#elm067) sépare niveau natif RBA et nature de l’aptitude métier. La présentation de Supply Protection / Supply Assignment comme fonctionnalités de produit ne disqualifie pas les capacités correspondantes ; C49/CMP038.

### ELM015

- Référence : [MKT13](catalogue.md#mkt13), [cours stocks et inventaires](https://learning.sap.com/courses/inventory-management-and-physical-inventory-in-sap-s-4hana/defining-inventory-management-and-physical-inventory-1), sections *Managing Stocks by Quantity*, *Planning, Entry, and Documentation of Goods Movements* et *Carrying Out the Physical Inventory*.
- Libellé natif : *Inventory Management and Physical Inventory*. Nature : responsabilités fonctionnelles S/4HANA.
- Définition reformulée : tenir les quantités et changements de stock avec leur documentation ; confronter un comptage au stock enregistré et enregistrer les différences.
- Limite : effets en valeur traités par SAP mais finance exclue de notre domaine. Ne détermine ni autorité Beaumanoir ni organisation de l’inventaire.

### ELM016

- Référence : [MKT13](catalogue.md#mkt13), [cours disponibilité](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/explaining-product-availability-check_c1ca2960-2d3c-40a6-a839-ff2ad9595f08), introduction, facteurs et résultats du contrôle.
- Libellé natif : *Product Availability Check*. Nature : fonction de solution aATP, distincte de la seule observation du libellé RBA dans ELM014.
- Définition reformulée : calculer les quantités et dates confirmables selon le stock, les demandes et les approvisionnements retenus par le contrôle.
- Limite : les ressources futures dépendent du périmètre de contrôle ; notre vente nominale GBM sur stock est conservée. Confirmation, réservation technique et cycle complet d’engagement ne sont pas déclarés équivalents.

### ELM017

- Référence : [MKT13](catalogue.md#mkt13), [cours protection](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-), section d’introduction à la protection d’approvisionnement.
- Libellé natif : *Supply Protection*. Nature : fonction de solution aATP.
- Définition reformulée : protéger une quantité pour un groupe vis-à-vis d’autres groupes suivant des critères et un horizon ; des priorités peuvent exister dans la solution.
- Limite : appui pour comparer protection et consommation ; aucune preuve d’équivalence avec MAP et aucune priorité SAP importée dans GBM.

- Complément U63/U64, 2026-09-10 : sections Supported and Affected Document Types / Stock Transport Orders reconsultées ; le cours traite ventes et transferts et relie consommation de protection aux quantités confirmées. Provenance complète et limites dans ELM062 ; aucun regroupement de domaines locaux déduit automatiquement.

- Précision U66/U67, 2026-09-11 : [ELM067](#elm067) sépare niveau natif RBA et nature de l’aptitude métier. La présentation de Supply Protection / Supply Assignment comme fonctionnalités de produit ne disqualifie pas les capacités correspondantes ; C49/CMP038.

- Réexamen U74 du 2026-09-11 : contenu de protection/allocation reconsulté pour le rattachement local à D01 ; passages et limites dans [CMP040](comparaisons.md#cmp040). Aucune équivalence de rang natif ni configuration Beaumanoir déduites.

### ELM018

- Référence : [MKT13](catalogue.md#mkt13), [cours allocation](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-check-against-allocation), présentation de l’allocation et de son contrôle.
- Libellé natif : *Product Allocation*. Nature : fonction de solution aATP.
- Définition reformulée : limiter les quantités confirmables selon périodes et caractéristiques ; articuler le contrôle avec celui de disponibilité.
- Limite : un plafond de confirmation n’est ni la protection d’un minimum pour un groupe ni la réservation d’une quantité pour une demande. Fonctionnement ARun local non établi.

## Éléments de l’étude comparative U25

Contrôle Codex du 2026-09-09. Les identifiants ELM restent locaux. Les sources originales, éditions et localisateurs sont dans les fiches MKT et annexes liées ; les définitions françaises sont des reformulations. Hors codes de vues ARTS, aucun identifiant natif d’élément n’est fourni ici. Aucune correspondance métier validée.

### ELM019

- Référence : [MKT01](catalogue.md#mkt01).
- Libellés natifs / repères : Business Capabilities ; stratification / leveling.
- Nature : Méthode.
- Édition et localisateur : G189, juin 2018, §§2.1/3/3.2, pages imprimées 2–3 et 6–10, copie du document primaire sur miroir tiers.
- Définition reformulée : Distinguer classement transversal et profondeur de décomposition, adaptée au besoin.
- Limite : G211/version 2 non lu ; aucune profondeur obligatoire ni nomenclature retail déduite.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-cadres-capacites.md).
- Réexamen U43 du 2026-09-10 : S2, G189 §3.2.1–3.2.2 ; texte consulté pour les premiers regroupements. [Analyse et limites](premier-niveau-regroupement-capacites.md), CMP026 ; ancienne provenance conservée.
- Réexamen U47 du 2026-09-10 : G189 §3.1, pages imprimées 6–7, distingue les approches descendante et ascendante et propose leur combinaison pour affiner la carte. [Document primaire sur miroir tiers](https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf), texte consulté ; appui méthodologique en CMP028, sans nomenclature commerce déduite.

### ELM020

- Référence : [MKT02](catalogue.md#mkt02).
- Libellés natifs / repères : Capability ; composition, aggregation, specialization.
- Nature : Métamodèle.
- Édition et localisateur : ArchiMate 3.1/C197, novembre 2019, §§7.1/7.3/7.6, copie externe ; tutoriel communautaire en complément.
- Définition reformulée : Représenter aptitude et relations sans imposer un catalogue sectoriel ni confondre décomposition et variante.
- Limite : Norme 3.2 non examinée ; aucune notation adoptée.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-cadres-capacites.md).

### ELM021

- Référence : [MKT03](catalogue.md#mkt03).
- Libellés natifs / repères : Tier ; Level ; Business Object.
- Nature : Pratiques de construction.
- Édition et localisateur : Atelier Guild du 20/06/2019, pages PDF 15–21 ; position paper octobre 2014, pages PDF 12–19.
- Définition reformulée : Séparer catégories et niveaux ; construire autour des objets/actions ; rapprocher capacités et processus plusieurs-à-plusieurs.
- Limite : Atelier et papier historiques ; pas guide BIZBOK 15 ni catalogue retail complet.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-cadres-capacites.md).
- Réexamen U43 du 2026-09-10 : S3, atelier 2019 pages PDF 17–21 ; texte consulté pour les premiers regroupements. [Analyse et limites](premier-niveau-regroupement-capacites.md), CMP026 ; ancienne provenance conservée.

- Réexamen U60 du 2026-09-10 : [atelier sur le CDN officiel](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf), pages 15–21, texte relu avec succès. Motifs de définition, information et rapprochement examinés ; un rapprochement d’objets garde un objet directeur. Sources 15.0 et métamodèle 2024 qualifiées séparément en ELM052–ELM054 ; pas de catalogue actuel déduit de l’atelier.

### ELM022

- Référence : [MKT05](catalogue.md#mkt05).
- Libellés natifs / repères : Retail Industry ; Business Process Areas ; Organizational Business Process Flows ; Business/System Process Flows.
- Nature : Niveaux et exemples de processus.
- Édition et localisateur : Guide Oracle RRM 14.1.1, juin 2015, pages imprimées 5–7, 12–21 et 26.
- Définition reformulée : Niveaux d’information L0–L3 avec liens non strictement hiérarchiques ; exemples achats, stock, allocation, réassort, B2B et retours.
- Limite : L2.5/3 ne crée pas un cinquième étage homogène. Bibliothèque actuelle non acquise ; fiche actuelle avec mentions divergentes.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-oracle-apqc-arts.md).

### ELM023

- Référence : [MKT07](catalogue.md#mkt07).
- Libellés natifs / repères : Category ; Process Group ; Process ; Activity ; Task.
- Nature : Classification de processus.
- Édition et localisateur : Introduction générale PCF ©2018, figure 1/pages PDF 1–2.
- Définition reformulée : Cinq niveaux nominaux ; identifiant distinct du chemin ; profondeur et granularité variables.
- Limite : Taxonomie, pas enchaînement de travail. Contenu Retail 7.2.1 non consulté.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-oracle-apqc-arts.md).
- Réexamen U43 du 2026-09-10 : S6, introduction générale et figure 1 ; texte consulté pour les premiers regroupements. [Analyse et limites](premier-niveau-regroupement-capacites.md), CMP026 ; ancienne provenance conservée.

### ELM024

- Référence : [MKT08](catalogue.md#mkt08).
- Libellés natifs / repères : 02010 ; 07620.
- Nature : Vues de données.
- Édition et localisateur : ARTS ODM 7.3, introduction, sommaire et narrations des deux vues.
- Définition reformulée : 02010 décrit comptage et ajustements ; 07620 distingue effets commande/disponibilité et expédition/stock physique.
- Limite : Identifiants natifs de vues, pas de capacités. Autres vues surtout repérées ; aucune règle GBM présumée.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-oracle-apqc-arts.md).

### ELM025

- Référence : [MKT06](catalogue.md#mkt06).
- Libellés natifs / repères : Direct ; Control ; Execute.
- Nature : Matrice de composants métier.
- Édition et localisateur : IBM G510-6163-00, 2005, pages PDF 7–11, figure 6 page PDF 11/imprimée 9, lecture visuelle.
- Définition reformulée : Croiser compétences et responsabilités ; examiner les répétitions de libellés dans leur contexte.
- Limite : Les trois lignes ne sont pas trois profondeurs ; définitions des cases absentes.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-sap-ibm.md).
- Réexamen U43 du 2026-09-10 : S4, cadre et exemple retail pages PDF 9–11 ; texte consulté pour les premiers regroupements. [Analyse et limites](premier-niveau-regroupement-capacites.md), CMP026 ; ancienne provenance conservée.
- Réexamen U51 du 2026-09-10 : document IBM G510-6163-00, 2005, figure 6 page imprimée 9 / PDF 11 relue pour les axes et thèmes retail. Les composants restent distincts de capacités métier ; CMP031.

- Réexamen U59 du 2026-09-10 : texte des pages PDF 9–11 et repères de la figure 6 relus. L’exemple retail offre une autre lecture par compétences et responsabilités ; les cases restent des composants. CMP033 n’assimile pas Direct/Control/Execute aux deux couches ni aux natures locales.

### ELM026

- Référence : [MKT14](catalogue.md#mkt14).
- Libellés natifs / repères : End-to-end processes ; Business process areas ; Business processes ; Scenarios ; System processes ; Test cases.
- Nature : Structure de catalogue.
- Édition et localisateur : Microsoft Learn About, sections niveaux/IDs, mise à jour 08/01/2026.
- Définition reformulée : Six niveaux du parcours métier à la configuration et au test ; certaines aires reflètent fonctions ou départements.
- Limite : Pas six profondeurs de capacités ; export complet non examiné.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-microsoft.md).
- Réexamen U43 du 2026-09-10 : S5, section des six niveaux, page du 08/01/2026 ; texte consulté pour les premiers regroupements. [Analyse et limites](premier-niveau-regroupement-capacites.md), CMP026 ; ancienne provenance conservée.

### ELM027

- Référence : [MKT14](catalogue.md#mkt14).
- Libellés natifs / repères : Inventory to deliver ; Order to cash ; Source to pay ; Design to retire ; Case to resolution.
- Nature : Contenus de processus et évolution.
- Édition et localisateur : Pages de présentation et aires, 2024–2026 ; changelog février 2025.
- Définition reformulée : Décrire les thèmes commerce et leurs réalisations ; retours déplacés du traitement des dossiers vers commande/encaissement en 2025.
- Limite : Dates hétérogènes ; certaines mentions sont des fonctions produit. Un déplacement ne prouve pas un nouveau besoin métier.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-microsoft.md).
- Réexamen U47 du 2026-09-10 : [Inventory to deliver — business process areas](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/inventory-to-deliver-areas), date affichée 2025-01-21. Sections Maintain inventory levels (comptage et ajustements), Process inbound goods (retours clients), Process outbound goods (retours fournisseurs) consultées. Contrôle de couverture proposé en CMP028 ; ni capacités ni domaines locaux déduits automatiquement de ces processus.
- Réexamen U51 du 2026-09-10 : [vue des scénarios](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/overview), tableau central et date affichée 2025-12-16 consultés. Source to pay, Order to cash et Inventory to deliver restent des parcours de contrôle, sans conversion automatique en domaines du socle ; CMP031. Les dates des autres pages et observations antérieures sont conservées séparément.

### ELM028

- Référence : [MKT14](catalogue.md#mkt14).
- Libellés natifs / repères : Inventory Visibility inventory allocation.
- Nature : Fonction de produit.
- Édition et localisateur : Page allocation, sections finalité/allocation virtuelle/réservation, mise à jour 13/08/2025.
- Définition reformulée : Préallouer une quantité à des groupes et suivre sa consommation, en distinguant réservation de transaction.
- Limite : Recouvrement de finalité avec protection SAP proposé ; mécanismes détaillés et usages locaux non établis.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-microsoft.md).

- Réexamen U74 du 2026-09-11 : contenu de protection/allocation reconsulté pour le rattachement local à D01 ; passages et limites dans [CMP040](comparaisons.md#cmp040). Aucune équivalence de rang natif ni configuration Beaumanoir déduites.

### ELM029

- Référence : [MKT04](catalogue.md#mkt04).
- Libellés natifs / repères : Sales Order Management ; Service Request Management ; Sourcing Process.
- Nature : Compléments éditoriaux.
- Édition et localisateur : SAP EA Knowledge Base,articles 2024–2026, extraits indexés des besoins métier.
- Définition reformulée : Éclairer commandes et support par des définitions RBA citées ; parcours de sourcing pour le contexte achats.
- Limite : Ouvertures directes 403 : extraits seulement. Pas export versionné ni rattachement complet reconstitué.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-sap-ibm.md).

### ELM030

- Référence : [MKT15](catalogue.md#mkt15).
- Libellés natifs / repères : Business Capability Reference Model.
- Nature : Carte retail historique.
- Édition et localisateur : Microsoft/APQC, carte V1 du 15/09/2012, pages PDF 15–16, texte extrait.
- Définition reformulée : Repérer produits, achats, stocks, allocation, réassort, exécution et service client comme thèmes de comparaison.
- Limite : Définitions absentes, emboîtement visuel non certifié ; distinct du PCF Retail et de Dynamics actuel.
- Sources et accès : [annexe de preuves](etudes/2026-09-09-modeles-marche/notes-oracle-apqc-arts.md).

### ELM031

- Référence : [MKT14](catalogue.md#mkt14), complément produit distinct du catalogue de processus.
- Libellé natif : Inventory Visibility reservations ; soft reservation / offset.
- Nature : Fonction de produit.
- Édition et localisateur : Microsoft Learn, mise à jour 27/07/2026, sections cas d’usage et intégration des réservations/compensations ; consultation 2026-09-09.
- Définition reformulée : Tenir une quantité réservée dans Inventory Visibility et l’articuler avec les changements de statut de la commande dans l’ERP.
- Limite : Paramétrage et versions conditionnent les contrôles ; pas de garantie ni de modèle de réservation universels.
- Source et accès : [page officielle](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), texte consulté ; analyse et localisateurs dans la [note comparative](allocation-reservation-sap-microsoft.md).

### ELM032

- Référence : [MKT13](catalogue.md#mkt13).
- Libellés natifs / identifiant : Supply Assignment (ARun), Backorder Processing ; SUPPLY_ASSIGNMENT_01.
- Nature : Fonctions de produit et articulation.
- Édition et localisateur : Cours SAP actuels sans édition précisée, sections PAC/BOP et Configure BOP Variant ; fiche de business function, Technical Data/Features, borne de disponibilité S/4HANA 1709. Consultation 2026-09-09.
- Définition reformulée : Distinguer confirmation et affectation, avec exécution de Supply Assignment possible dans BOP.
- Limite : Borne de business function, pas date de chacune des fonctions actuelles ; aucune scission historique globale démontrée ni usage Boardriders établi.
- Sources et accès : S5/S6/S8 dans la [note comparative](allocation-reservation-sap-microsoft.md), cours consultés et passage indexé de la fiche Help Portal.

- Précision U66/U67, 2026-09-11 : [ELM067](#elm067) sépare niveau natif RBA et nature de l’aptitude métier. La présentation de Supply Protection / Supply Assignment comme fonctionnalités de produit ne disqualifie pas les capacités correspondantes ; C49/CMP038.

### ELM033

- Référence : [MKT16](catalogue.md#mkt16).
- Libellés natifs / identifiants : Order Allocation Run ; FASHION_20_ARUN ; FASHION_03 ; FSH_BADI_ARUN_STOCK_PROTECTION.
- Nature : Documentation historique de produit.
- Édition et localisateur : SAP ERP 6.0 EHP8 SPS01, EA-RETAIL 618 SP1 ; Order Allocation Run (New), sections Technical Details, Features, Customizing ; consultation 2026-09-09.
- Définition reformulée : Ensemble Fashion associant sélection, affectation, libération et extension pour la protection de segments.
- Limite : Pas tout ECC, pas preuve d’un unique batch ni équivalence de l’ancien ARun avec tous les mécanismes actuels.
- Sources et accès : S7 et complément S9 (règle de réallocation, édition non affichée) dans la [note comparative](allocation-reservation-sap-microsoft.md) ; passage indexé consulté.

### ELM034

- Référence : [MKT14](catalogue.md#mkt14), complément produit SCM distinct du catalogue de processus.
- Libellé natif : Reserve inventory quantities ; Reserve ordered items.
- Nature : Fonction de produit.
- Édition et localisateur : Microsoft Learn, page mise à jour 29/08/2025, introduction et Policies on the Inventory and warehouse management parameters page ; consultation 2026-09-09.
- Définition reformulée : La réservation peut porter sur du physique présent ou sur du stock commandé non encore reçu, selon la politique configurée.
- Limite : Ne prouve ni une équivalence BOP/ARun ni une réalisation GBM/BRD. Version produit précise non affichée.
- Source et accès : [page officielle](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities), texte consulté ; [analyse U30](../connaissance/18-politiques-engagement-gbm-brd.md).

### ELM035

- Référence : [MKT13](catalogue.md#mkt13).
- Libellés natifs : Product Availability Check ; Backorder Processing — Supply Assignment ; Reassignment ; Configuration Options for Exception Handling.
- Nature : Conditions fonctionnelles de produit.
- Édition et localisateurs : S/4HANA 2025 FPS01, février 2026 ; PAC Use ; BOP Supply Selection, Reason Codes, Reassignment ; exceptions Use/Options. Consultation 2026-09-09.
- Définition reformulée : Distinguer confirmation et affectation ; futures réceptions et reprises selon règles ; révisions prioritaires avec possibilités d’exception.
- Limite : Une demande non confirmée n’est pas automatiquement affectable ; une priorité ne crée pas d’offre. Conditions et version, pas fonctionnement BRD prouvé.
- Sources et accès : S1/S2 de la [note GBM/BRD](../connaissance/18-politiques-engagement-gbm-brd.md), passages Help indexés consultés.

### ELM036

- Référence : [MKT13](catalogue.md#mkt13), distincte du modèle métier RBA MKT04.
- Libellés natifs / repères : Order Promising (2LN) ; Backorder Processing (BOP) ; Advanced Order Promising ; CA-ATP-BOP.
- Nature : Rattachement fonctionnel dans la documentation de solution.
- Édition et localisateur : page Cloud Public Edition affichée 2608 Latest, liste des fonctions PAC/BOP ; nouveautés S/4HANA 2023, OData API: Advanced Backorder Processing Run, tableau Solution Area/Capability. Consultation 2026-09-09.
- Définition reformulée : SAP présente BOP parmi les fonctions d’Order Promising ; l’API de réexamen est classée sous Advanced Order Promising / Advanced Available to Promise.
- Limite : Éditions distinctes ; classification de produit, aucune feuille native BOP ni profondeur établie dans le catalogue RBA complet. Aucun niveau local adopté.
- Sources et accès : S4 de la [note GBM/BRD et promesse](../connaissance/18-politiques-engagement-gbm-brd.md), passages indexés consultés.

### ELM037

- Référence : [MKT14](catalogue.md#mkt14), complément produit Inventory Visibility.
- Libellés natifs / repères : Allocate, Unallocate, Reallocate, Consume, Query ; soft reservation, offset.
- Nature : Opérations, objets et mesures d’un produit ; pas sous-capacités natives.
- Éditions et localisateurs : allocation, page du 13/08/2025, Terminology et Use the allocation APIs ; réservations, page du 27/07/2026, création, intégration/offset et annulation. Consultation 2026-09-09.
- Définition reformulée : Les fonctions disposent d’opérations et de règles détaillées, documentées dans leur contexte d’intégration.
- Limite : Hiérarchie de groupes et mesures ne donnent ni profondeur de carte ni capacités locales automatiques. Aucun usage Beaumanoir ou Boardriders démontré.
- Sources et accès : S2/S3 dans la [note de granularité](detail-fonctions-stock-promesse.md), textes Microsoft Learn consultés ; compléments ELM028/ELM031.

### ELM038

- Référence : [MKT13](catalogue.md#mkt13), distincte du modèle de capacités RBA.
- Libellés natifs / repères : Supply Protection Object / Group ; Core / Prioritized Supply Protection ; Product Allocation Characteristics / Sequences.
- Nature : Objets, états, variantes et règles de fonctions de produit.
- Éditions et localisateurs : cours SUP, sections objet/activation/groupes/variantes ; cours PAL, restrictions/périodes, sans édition précisée. Help 2025 FPS01, Characteristics Use et Product Allocation Sequences, Context/étapes 4–8. Consultation 2026-09-09.
- Définition reformulée : SUP et PAL détaillent les groupes, critères et horizons, avec cycle d’application ou composition de contrôles selon la fonction.
- Limite : Composition d’objets ou variante de règle, pas étage natif de sous-capacités vérifié. Préserver la distinction SUP/PAL et leurs versions.
- Sources et accès : S5/S6 dans la [note de granularité](detail-fonctions-stock-promesse.md), cours consultés et passages Help indexés ; compléments ELM017/ELM018.

### ELM039

- Référence : [MKT13](catalogue.md#mkt13).
- Libellés natifs / repères : Supply Assignment Rule ; BOP segment / variant / confirmation strategy / fallback variant / run.
- Nature : Règles d’affectation et objets de configuration/exécution du réexamen.
- Éditions et localisateurs : Supply Assignment Rule, General Settings/Supply Configuration/Assignment Configuration/Release Check Settings, 2025 FPS01 ; Key Concepts in Backorder Processing, définitions, 2023 Latest. Consultation 2026-09-09.
- Définition reformulée : Les fonctions ARun et BOP distinguent les règles de décision, paramètres de sélection et modes d’exécution.
- Limite : Éditions distinctes ; pas hiérarchie de capacités, pas transfert automatique du calcul métier dans la couche processus/organisation.
- Sources et accès : S7/S8 dans la [note de granularité](detail-fonctions-stock-promesse.md), passages Help indexés ; compléments ELM032/ELM035.

### ELM040

- Référence : [MKT13](catalogue.md#mkt13).
- Libellés natifs / repères : Manage Supply Protection ; maintain protected quantities ; Maintaining Material Master Data / Maintain the material master record.
- Nature : vocabulaire anglais de documentation de produit et de formation ; pas libellés français de capacités.
- Éditions et localisateurs : Apps for Supply Protection (SUP), 2608 Latest, sections Use et Business Roles ; cours Maintaining Material Master Data, titre et objectif, édition produit non précisée. Consultation 2026-09-09.
- Constat reformulé : SAP emploie Manage pour l’application de gestion des protections et Maintain pour les quantités protégées ou les données de référence.
- Limite : ces exemples ne prouvent ni une traduction canonique par tenir, ni l’absence de ce mot dans toute la documentation SAP. Aucun niveau de capacité déduit de ces verbes.
- Sources et accès : [Apps for Supply Protection](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/d308d458b5794b1cbf647aca23de4d9d.html), passage indexé consulté ; [Maintaining Material Master Data](https://learning.sap.com/courses/business-processes-in-sap-s-4hana-sourcing-procurement/maintaining-material-master-data), titre et objectif consultés via extrait indexé. Analyse et propositions françaises dans le [glossaire](../connaissance/19-glossaire-metier.md#provenance-de-tenir-et-choix-de-formulations).

### ELM041

- Référence : [MKT17](catalogue.md#mkt17).
- Libellés natifs : domain ; model ; bounded context.
- Nature : définitions conceptuelles.
- Édition et localisateur : Evans, référence DDD ©2015, page imprimée vi/page PDF 6, Definitions. Consultation du 2026-09-10.
- Constat reformulé : le domaine est le champ étudié ; le modèle en représente des aspects utiles à la résolution de problèmes ; le contexte délimité indique où un modèle particulier est défini et applicable.
- Limite : espace problématique est la lecture de travail exprimée en U45, pas une citation de cette définition native. Aucune hiérarchie de capacités ni correspondance un-à-un entre domaine local et contexte délimité déduite.
- Source et accès : [document primaire de l’auteur](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf), passage textuel consulté ; [analyse](premier-niveau-regroupement-capacites.md#donner-un-sens-au-domaine-avec-ddd).

- Précision U46 du 2026-09-10 : ELM041 atteste le passage du mémento de 2015, pas la formulation du livre complet. Recherche ciblée dans l’extrait éditeur du livre décrite sous MKT17 ; passage exact évoqué non localisé, sans preuve d’absence. La limite de travail actuelle exclut la conception des bounded contexts.

### ELM042

- Référence : [MKT10](catalogue.md#mkt10), OMG BPMN.
- Libellés natifs : Processes (Orchestration) ; Private non-executable / executable Business Processes.
- Nature : concepts de modélisation de processus, pas catalogue de capacités.
- Édition/localisateur : BPMN 2.0.2, janvier 2014, §7.2.1, page imprimée 21 / page PDF 51 ; consulté le 2026-09-10.
- Reformulation : l’orchestration décrit des processus, qui peuvent être modélisés sans être exécutables.
- Limite : ne fixe ni une liste de capacités métier ni le choix d’un moteur.
- Source : [spécification primaire](https://www.omg.org/spec/BPMN/2.0.2/PDF), texte du passage consulté ; CMP029.

### ELM043

- Référence : [MKT13](catalogue.md#mkt13), SAP S/4HANA Cloud.
- Libellés natifs : Subcontracting ; subcontract purchase requisition ; subcontract purchase order ; stock of material provided to supplier.
- Nature : description fonctionnelle de produit et processus.
- Édition/localisateur : cours Outlining Subcontracting, introduction et Applicable Process Steps ; édition produit non précisée, consulté le 2026-09-10.
- Reformulation : demande et commande de sous-traitance, composants fournis au prestataire et consommation reliée à la réception du résultat.
- Limite : aucune équivalence du Planned Purchase Order local avec le document SAP ; aucune propriété ou configuration Beaumanoir prouvée.
- Source : [cours primaire SAP](https://learning.sap.com/courses/detailing-subcontracting-and-supplier-consignment/outlining-subcontracting_af403e3e-188d-4dbb-bde1-632253739fa6), texte consulté ; CMP030.

### ELM044

- Référence : [MKT14](catalogue.md#mkt14), complément produit Dynamics 365 SCM, distinct du catalogue de processus.
- Libellés natifs : subcontracting ; service product ; vendor-managed warehouse.
- Nature : documentation de réalisation de la sous-traitance.
- Édition/localisateur : Manage subcontracting work in production, page du 2025-08-13, introduction, Subcontracting of route operations et paragraphes sur le stock au site fournisseur ; consulté le 2026-09-10.
- Reformulation : achat de service et mise à disposition des matières sont articulés dans plusieurs variantes de production, avec des représentations distinctes.
- Limite : aucune correspondance générale un-à-un avec SAP, aucune organisation de production ni modèle de stock imposé à Beaumanoir.
- Source : [documentation primaire Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/manage-subcontract-work-production), passages textuels consultés ; CMP030.

### ELM045

- Référence : [MKT13](catalogue.md#mkt13), SAP S/4HANA / Cloud Public Edition.
- Libellés natifs : Stock Transport Order ; Intra-Company Stock Transfer ; Intercompany Stock Transfer (1P9) ; Advanced Intercompany Stock Transfer (5HP).
- Nature : variantes de processus et objets de réalisation de transfert.
- Édition/localisateurs : cours d’éditions non précisées, consultés le 2026-09-10 ; S1 sections STO/One-Step Versus Two-Step, S2 scénarios 1P9/5HP, S3 Cross-Plant Stock Transfer.
- Reformulation : des mouvements comparables s’articulent avec des engagements et effets comptables différents. Dans 5HP, commande de vente et changement de propriété en transit sont explicités séparément.
- Limite : pas de règle fiscale universelle, ni d’identité de tous les scénarios SAP ou de preuve locale. Une facture et une écriture comptable sont distinguées.
- Sources primaires et accès : S1–S3 de la [note réassort](../connaissance/23-reassort-transferts-et-promesse.md#sources-et-limites-de-consultation), textes consultés ; page Help supplémentaire sans texte exploitable non retenue comme preuve.

### ELM046

- Référence : [MKT13](catalogue.md#mkt13), SAP S/4HANA et Cloud Public Edition.
- Libellés natifs : Available-to-Promise ; Product Availability Check ; Backorder Processing ; sales order ; stock transport order.
- Nature : périmètre fonctionnel de confirmation et réexamen.
- Édition/localisateurs : cours d’éditions non précisées, consultés le 2026-09-10 ; S4 Introduction to Available-to-Promise, S5 introduction et Back Order Processing.
- Reformulation : quantité/date peuvent être confirmées pour un client ou un site receveur ; le réexamen peut concerner des commandes clients et ordres de transfert.
- Limite : ne couvre pas toute la gestion d’un achat ou retour ; ne prouve aucune configuration locale. Libellé 2LN du cours distinct de la page versionnée ELM036 ; aucune harmonisation de version ou licence déduite.
- Sources primaires et accès : S4/S5 de la [note réassort](../connaissance/23-reassort-transferts-et-promesse.md#sources-et-limites-de-consultation), textes consultés.

- Réexamen U63/U64, 2026-09-10 : la leçon S5 renvoie actuellement surtout à l’activation ; Basic ATP et le cours BOP ciblé en ELM062 fournissent les preuves directes retenues pour la nouvelle carte. Cette observation ne réattribue pas la lecture historique à une nouvelle édition.

### ELM047

- Référence : [MKT13](catalogue.md#mkt13), SAP S/4HANA Advanced Returns Management.
- Libellés natifs : Materials Received ; Advanced Notice ; Inspection at Customer ; Direct Return to Vendor.
- Nature : description de scénarios de retour, distincte d’une capacité native RBA.
- Édition/localisateur : édition non précisée, consultation 2026-09-10 ; Outlining Customer Returns in SAP S/4HANA, Standard Scenarios for Customer Returns.
- Reformulation : réception, inspection, suites et effets commerciaux peuvent varier, notamment pour un retour direct au fournisseur.
- Limite : ne démontre ni une ressource immédiatement disponible ni un fonctionnement Sarenza ; aucun retour complet assimilé à Order Promising.
- Source et accès : S7 de la [note réassort](../connaissance/23-reassort-transferts-et-promesse.md#sources-et-limites-de-consultation), texte primaire consulté ; autre leçon BKP en 404 non utilisée.

### ELM048

- Référence : [MKT18](catalogue.md#mkt18), BIAN ; guide V8.1 daté juillet 2020.
- Libellés natifs : Business Area ; Business Domain ; Service Domain.
- Nature : classification de partitions fonctionnelles bancaires.
- Reformulation : les deux premiers regroupent les Service Domains ; différents layouts classent les mêmes partitions. Ces partitions sont définies par des besoins métier tout en guidant une conception de services autonomes.
- Source, localisateurs et accès : [guide officiel](https://bian.org/wp-content/uploads/2024/12/BIAN-Semantic-API-Pactitioner-Guide-V8.1-FINAL.pdf), §§2.1, 3.1, 4.2.1, pages 12–13, 26–27, 78–79 ; passages consultés le 2026-09-10.
- Limite : distinction avec la business capability ; ni hiérarchie SAP inversée par erreur ni catalogue retail. Pas de définition locale dérivée automatiquement ; état 14.0 non comparé en détail.

### ELM049

- Référence : [MKT19](catalogue.md#mkt19), TM Forum Functional Framework.
- Libellés natifs : domain ; sub-domain ; function.
- Nature : classification de fonctions du point de vue SI.
- Reformulation : domaines et sous-domaines regroupent les fonctions ; les sous-domaines ont un rôle taxonomique et les fonctions élémentaires sont au même niveau.
- Source/localisateurs : [présentation officielle](https://www.tmforum.org/open-digital-architecture/functional-framework/), Fundamental units / Recognizing functions ; consultée le 2026-09-10.
- Version/limite : GB1033 v26.0 identifié dans une notice, document détaillé non consulté. Une fonction SI n’est pas automatiquement notre capacité indépendante des outils.

### ELM050

- Référence : [MKT19](catalogue.md#mkt19), TM Forum Functional Architecture.
- Libellés natifs : Core Commerce Management ; Production ; Engagement Management ; Party Management ; Intelligence Management.
- Nature : blocs d’architecture fonctionnelle, distincts du catalogue des capacités.
- Reformulation : la présentation sépare commerce et fourniture du service. Cette séparation peut éclairer une étude de frontière sans fournir le découpage Beaumanoir.
- Source/localisateurs : [présentation officielle](https://www.tmforum.org/open-digital-architecture/functional-architecture/), Why is this important? / What has been accomplished so far? ; consultée le 2026-09-10.
- Version/limite : notices 2021 identifiées en MKT19, documents détaillés non consultés. Production télécom n’est pas déclarée équivalente à Supply ou à la logistique ; aucune prescription locale de cinq blocs.

### ELM051

- Référence : [MKT19](catalogue.md#mkt19), TM Forum Capability Framework.
- Libellé natif : Business Capability Framework.
- Nature : modèle de capacités lié à d’autres vues métier.
- Reformulation : le modèle de capacités est distinct des modèles de processus et d’architecture fonctionnelle de l’ODA.
- Source/localisateur : [présentation officielle](https://www.tmforum.org/open-digital-architecture/capability-framework/), Overview ; consultée le 2026-09-10.
- Version/limite : GB1029C v4.0.0 identifié dans une notice de mars 2026 ; catalogue détaillé membre non consulté. Structure fine et couverture de capacités non comparées.

### ELM052

- Référence : [MKT03](catalogue.md#mkt03), BIZBOK Guide 15.0, ©2026.
- Nature : définitions du glossaire ; libellés natifs Capability, Business Service, Capability Instance, Capability Level, Capability Tier.
- Reformulation : distinguer aptitude, service SOA, réalisation contextuelle, profondeur et catégorie. La capacité vise une finalité ou un résultat.
- Source/localisateurs : [Appendix A](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_glossary.pdf), pages imprimées 456–457 / PDF 4–5 ; consultées le 2026-09-10.
- Limite : définitions externes distinctes de la convention locale impérative U33 ; aucun remplacement automatique du glossaire Beaumanoir.

### ELM053

- Référence : [MKT03](catalogue.md#mkt03), Business Architecture Metamodel Guide v3.0, septembre 2024.
- Nature : métamodèle ; objet central et décomposition des capacités.
- Reformulation : les enfants conservent l’objet métier du parent ; capacité et réalisation contextuelle sont distinguées. Domain désigne ici une perspective d’architecture, notamment capacité ou information.
- Source/localisateurs : [guide officiel](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf), §§3, 5 et 5.2, pages PDF/imprimées 7, 12 et 17–19 ; texte consulté le 2026-09-10.
- Limite : ce document ne remplace pas le guide BIZBOK complet ; la tentative de capture de la page 19 échoue, aucune conclusion nouvelle tirée de sa figure. Ni domaine problématique local ni allocation logicielle déduits automatiquement.

### ELM054

- Référence : [MKT03](catalogue.md#mkt03), BIZBOK Guide 15.0, ©2026.
- Nature : introduction et présentation du contenu du guide.
- Reformulation : architecture métier et modèle opératoire sont reliés et distingués ; les parties annoncées couvrent capacité, Common Reference Model et articulation avec processus/Case Management.
- Source/localisateurs : [Part 1](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_introduction.pdf), pages 3, 6, 12 et 15–17 ; consultées le 2026-09-10.
- Limite : présentation du §2.2, du §8.6 et des autres sections, pas lecture de ces sections détaillées. La portée entreprise de la Guild n’étend pas notre capability map au-delà du socle.

### ELM055

- Référence : [MKT03](catalogue.md#mkt03), notices publiques des modèles Guild, état du 2026-09-10.
- Nature : disponibilité de livrables ; aucun contenu détaillé de capacités.
- Constat : Common Reference Model proposé ; version non affichée sur sa notice. Companion Guide v3.0 identifié séparément. Aucun Retail/Wholesale dans la liste publique examinée, malgré une équipe identifiée dans l’index.
- Sources/localisateurs : [liste officielle](https://learning.businessarchitectureguild.org/indref), introduction et conditions ; [Common Reference Model](https://learning.businessarchitectureguild.org/products/common-reference-model), Overview ; [Companion Guide v3.0](https://learning.businessarchitectureguild.org/products/business-architecture-common-reference-model-companion-guide-v30), titre/Contents ; pages consultées.
- Limites : téléchargement membre et licence, ressources non acquises ; absence de listing ne prouve pas inexistence. [Équipe Retail](https://www.businessarchitectureguild.org/members/group_select.asp?type=19895) : index consulté, ouverture directe en 403. L’annonce historique v7.0 dans le [webinar](https://learning.businessarchitectureguild.org/products/webinar-common-reference-model-companion-guide-walkthrough) n’établit pas la version distribuée aujourd’hui ; vidéo non consultée.

### ELM056

- Référence : [MKT04](catalogue.md#mkt04), SAP EA/RBA ; cours sans édition indiquée.
- Nature : modèle métier de l’information lié aux capacités, distinct du modèle de solution.
- Libellés natifs : Business Data Catalog ; Business Data Mapping ; Business Data Object ; Solution Data Object.
- Reformulation : identifier les concepts d’information à partir notamment des capacités et processus ; relier objets et capacités. Les objets métier sont distingués de leur représentation dans la solution.
- Sources/localisateurs : [Defining Business Architecture](https://learning.sap.com/courses/intelligent-enterprise-architecture-fundamentals/defining-business-architecture), Business Data Catalog / Business Data Mapping ; [Investigating the SAP Enterprise Architecture Methodology](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/investigating-the-sap-enterprise-architecture-methodology), Enterprise Architecture Concepts. Passages consultés le 2026-09-10.
- Limite : pas de dérivation exhaustive de schémas ou agrégats depuis les libellés de capacités ; catalogue détaillé versionné non acquis.

### ELM057

- Référence : [MKT03](catalogue.md#mkt03), Guild Metamodel Guide 3.0 de septembre 2024 et glossaire BIZBOK 15.0 ©2026.
- Nature : relations entre aptitude, information, états et résultats.
- Libellés natifs : Information Concept ; Business Object ; Outcome ; Event.
- Reformulation : une capacité utilise/modifie de l’information ; les concepts représentent les objets et leurs états. Le résultat et l’occurrence sont des notions distinctes.
- Sources/localisateurs : [métamodèle](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf), §§5.1.2, 5.2, 5.3, pages 15, 17–21, texte ; [glossaire](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_glossary.pdf), Event/Outcome, pages 459/461. Consultés le 2026-09-10.
- Limite : aucune identité Outcome = événement publié = document ; pas de prescription d’immutabilité, de racine d’agrégat ou de persistance. Capture du schéma page 21 échouée ; conclusion fondée sur les paragraphes textuels.

### ELM058

- Référence : [MKT19](catalogue.md#mkt19), TM Forum Information Framework SID et Capability Framework.
- Nature : modèle d’information métier et regroupements sémantiques.
- Libellés natifs : Business Entity ; Aggregate Business Entity (ABE).
- Reformulation : le SID décrit concepts, attributs et relations indépendamment des plateformes/langages/protocoles. Les ABEs regroupent des entités ou d’autres ABEs ; leurs noms ne fixent pas une frontière transactionnelle.
- Sources/localisateurs : [SID](https://www.tmforum.org/open-digital-architecture/information-framework-sid/), Overview / SID Domains / Business Entities ; [Capability Framework](https://www.tmforum.org/open-digital-architecture/capability-framework/), Overview. Pages publiques consultées le 2026-09-10.
- Limite : notices SID 26.0 et GB1029C v4.0.0 identifiées, catalogues complets et correspondances détaillées non consultés. Aucun ABE assimilé à une racine d’agrégat DDD.

### ELM059

- Référence : [MKT13](catalogue.md#mkt13), SAP S/4HANA Cloud, inventaire.
- Nature : documents de réalisation et notifications ; pas modèle de capacités.
- Libellés natifs : Material Document ; Created ; Canceled.
- Reformulation : le mouvement comptabilisé produit un document ; ses notifications le référencent. Mouvement/quantité se corrigent par annulation et nouvelle comptabilisation, mais certains compléments restent possibles.
- Sources/localisateurs : [The Document Concept](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/b19bce0a4e5f4256b101ed2be62fa94b.html?ai=true&q=BATCH+NUMBER), Document Types/note, version non exposée ; [Material Document Events](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3f57e7df4a114edabffe8b2d581a59ed/40783449115e4b53a9da6e513caf8f50.html), APIs for Inventory 2608, tableau Created/Canceled et payloads. Extractions indexées consultées le 2026-09-10 ; ouvertures directes sans texte exploitable.
- Limite : SAP appelle le document lui-même business object. Pas d’immutabilité absolue, de preuve locale ou d’équivalence de l’événement publié avec le fait métier U61.

### ELM060

- Référence : [MKT19](catalogue.md#mkt19), TM Forum, exemples documentés de ressources et notifications.
- Nature : schémas et contrats d’échange, distincts de la carte des capacités.
- Libellés natifs : ProductOrder ; ProductOrderStateChangeEvent ; Document.
- Reformulation : une ressource possède son cycle d’état et des notifications distinctes ; le schéma Document comporte état, version et date de mise à jour.
- Sources/localisateurs : [TMF622 v4.0.0](https://tmf-open-api-table-documents.s3.eu-west-1.amazonaws.com/OpenApiTable/TMF622_Product_Ordering/4.0.0/user_guides/TMF622_Product_Ordering_Management_API_v4.0.0_specification.pdf), ©2019, Lifecycle p.13 et Notification Resource Models pp.37–40 ; [Document](https://datamodel.tmforum.org/en/latest/Common/Document/), Description / Data model, repère snapshot 04/02/2020 pour les correspondances API. Consultés le 2026-09-10.
- Limite : exemples historiques examinés, pas dernières versions présumées ; ces ressources ne prouvent ni immutabilité de tous les documents ni Event Sourcing ni identité notification/fait de gestion.

### ELM061

- Référence : [MKT17](catalogue.md#mkt17), Eric Evans, DDD Reference ©2015, licence CC BY 4.0.
- Nature : précision d’un motif de conception invoqué par analogie dans U61.
- Libellé natif : Aggregate / root.
- Reformulation : l’agrégat délimite des invariants et une responsabilité de cohérence ; ses limites gouvernent aussi les transactions.
- Source/localisateur : [référence de l’auteur](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf), Aggregates, page imprimée 16 / PDF 23 ; passage textuel sur invariants/racine/transactions consulté le 2026-09-10.
- Limite : pas de conception d’agrégats ni de bounded contexts engagée ; l’objet métier de la carte n’est pas automatiquement une racine d’agrégat. Le mémento 2015 reste distinct du livre initial.

### ELM062

- Références : MKT04 SAP RBA ; MKT13 SAP S/4HANA ; MKT14 pour le complément Microsoft déjà associé à ELM028.
- Nature : réexamen ciblé des appuis de structure et de comportements de produit pour P81 ; nouveau passage BOP et compléments à des éléments déjà examinés.
- Libellés natifs : Business Capability Model ; Supply Protection ; Available-to-Promise ; Backorder Processing ; Subcontracting ; Inventory Visibility allocation.
- Consultation : 2026-09-10, textes primaires ouverts et lus avec contribution indépendante. Cours SAP sans édition exposée ; Microsoft conserve sa provenance datée en ELM028, sans déduire une version de livraison homogène.
- Sources et localisateurs : [SAP RBA](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), Framework / Business Capability Model Example ; [Supply Protection](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-), protection des groupes / Supported and Affected Document Types / Stock Transport Orders ; [Basic ATP](https://learning.sap.com/courses/configuring-supply-chain-business-scenarios-in-sap-s4hana-cloud-public-edition/introducing-basic-available-to-promise_ee3a33eb-4a91-4f85-a8b6-9bc1189e9540), Introduction to Available-to-Promise ; [BOP ciblé](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-backorder-processing-for-advanced-atp-in-sap-s-4hana), General Restrictions / Configure BOP Segments / Configure BOP Variant ; [Subcontracting](https://learning.sap.com/courses/detailing-subcontracting-and-supplier-consignment/outlining-subcontracting_af403e3e-188d-4dbb-bde1-632253739fa6), introduction / Applicable Process Steps ; [Microsoft allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), Difference between inventory allocation and soft reservation / Allocation virtual pool.
- Reformulation du complément : les aires de stock/promesse/exécution logistique sont distinctes dans l’exemple SAP, avec quatre niveaux natifs ; protection et promesse peuvent concerner ventes et transferts. Le BOP réexamine les confirmations selon les priorités ; les variantes décrites peuvent mobiliser ATP ou Supply Assignment. Allocation de groupe et réservation de transaction restent distinctes chez Microsoft. La sous-traitance relie composants fournis et résultat reçu.
- Limites : les domaines P81 sont locaux et non équivalents à ces catégories. Sourcing and Procurement est un Business Domain SAP, Inventory Management un Business Area. Sources de produits distinctes du catalogue de capacités ; aucune configuration Beaumanoir ni inclusion logistique dans FLOW prouvées. Le texte actuel de l’ancienne leçon S5 citée par ELM046 est surtout consacré à l’activation ; le réexamen présent s’appuie sur Basic ATP et le cours BOP ciblé ci-dessus, sans supprimer la lecture historique.

### ELM063

- Références : MKT04 SAP RBA ; MKT13 documentation fonctionnelle SAP, complétée par Retail, référentiels et pricing.
- Nature : libellés natifs de niveaux et de contenus différents, destinés à un rapprochement terminologique de P81.
- Consultation : 2026-09-11, contrôle ciblé avec contribution indépendante ; éditions de catalogue et de release non exposées dans les cours. La preuve antérieure des feuilles RBA est conservée en ELM014.
- Libellés : Inventory Management / Order Promising (Business Areas RBA), Product Availability Check / Product Allocation Check (Business Capabilities RBA) ; Supply Protection / Supply Assignment ; Sales Order Management / Purchase Order Management ; Replenishment Planning ; Plant Determination / Alternative-Based Confirmation ; Delivery Processing / Inbound Delivery / Outbound Delivery ; Product Master / Material Master / Retail Article Master ; Business Partner / Business Partner Roles ; Pricing / Condition Records / Condition Contract Management.
- Sources ouvertes : [RBA](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), Framework / Business Capability Model Example ; [Sales Order Management](https://learning.sap.com/courses/exploring-end-to-end-business-processes-in-sap-business-suite/describing-sales-order-management_ca7b816e-af6f-4a03-bd88-1a5bb42cef84), Overview / Processing / Pricing ; [Replenishment Planning](https://learning.sap.com/courses/discovering-retail-functions-and-business-processes-in-sap-s-4hana-retail/running-replenishment-planning_e456b0ed-3094-4056-9ba8-aa56cf6833ed), Replenishment in General / Perform Replenishment Planning ; [ATP](https://learning.sap.com/courses/performing-the-availability-check/acquiring-a-basic-understanding-of-available-to-promise-atp-_ae470c8e-1483-46ce-b5cc-e80647e8a32b), Level of the ATP Check ; [Business Partners](https://learning.sap.com/courses/exploring-business-processes-for-supply-chain-execution-in-sap-s-4hana-cloud-private-edition/maintaining-materials-and-business-partners), Business Partner Master Records.
- Sources examinées par extraits indexés : [Fashion](https://learning.sap.com/courses/outlining-sap-s-4hana-for-fashion-and-vertical-business-and-implementing-best-practices/comparing-with-sap-fashion-management-solution-fms-1), Order Fulfillment / Supply Protection ; [Procurement for Retail 5FM](https://learning.sap.com/courses/exploring-sap-s-4hana-cloud-public-edition-retail/ordering-merchandise-with-procurement-for-retail-5fm-_fe298f93-84ad-47ff-98ff-658e887e020d), objectif Set Up Purchase Order Management ; [Delivery Processing](https://help.sap.com/docs/SAP_SUPPLY_CHAIN_MANAGEMENT/f41048b9ca054326bb9774db1d46e866/13cccb53ad377114e10000000a174cb4.html), présentation EWM ; [Retail Article Master](https://learning.sap.com/courses/discovering-retail-functions-and-business-processes-in-sap-s-4hana-retail/introducing-the-retail-article-master_bd2d9df6-bf54-4612-8fa0-b35c63fbb0d8), Article Master — General / Conversion / Manage Product Master Data ; [Pricing](https://learning.sap.com/courses/configuring-pricing-in-sap-s-4hana-sales), description et titres d’unités Working with Condition Records / Getting to Know Condition Contract Management, sans lecture de toutes les leçons sous-jacentes.
- Reformulation et adaptation : plusieurs libellés correspondent à une seule ligne locale ; les rapprochements sont détaillés dans la note U65. Replenishment éclaire le réassort, ABC les origines alternatives, les masters les référentiels et Pricing les conditions de prix.
- Limites : seuls les niveaux RBA indiqués sont attestés comme tels ; les autres noms ne sont pas transformés en Business Areas. Pas de domaine SAP unique démontré pour D02/D04/D06/D07 ; quota magasin, totalité des droits après fourniture et exécution générique non couverts par ces seuls noms. Aucune équivalence ni configuration Beaumanoir établie.

### ELM064

- Référence : MKT14, avec distinction du catalogue de processus et des documentations de produit Dynamics 365 utilisées pour le compléter.
- Nature : intitulés d’aires de processus, de modules, de fonctionnalités et de concepts de référentiel.
- Consultation : 2026-09-11, pages publiques ouvertes et texte disponible malgré le bandeau générique de connexion Learn ; aucune connexion utilisée. Pas d’édition homogène de catalogue ou de release déduite des pages.
- Sources processus : [Inventory to deliver areas](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/inventory-to-deliver-areas), titres Maintain inventory levels / Process inbound goods / Process outbound goods / Manage warehouse operations, date 2025-01-21 ; [Order to cash areas](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/order-to-cash-areas-overview), Develop sales policies / Manage sales orders et liste Order promising, état reconsulté ; [Source to pay areas](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/source-to-pay-areas), Manage supplier relationships / Source and contract goods and services / Procure goods and services, date 2025-05-20.
- Sources stock : [Inventory management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-home-page), titre et présentation ; [Inventory Visibility allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation) et [Reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), titres et distinction déjà détaillée en ELM028/ELM031, pas nouvelle comparaison de toutes leurs règles.
- Sources exécution : [Distributed order management](https://learn.microsoft.com/en-us/dynamics365/commerce/dom), présentation, date 2026-06-03 ; [DOM rules](https://learn.microsoft.com/en-us/dynamics365/commerce/dom-rules), Fulfillment location priority / Offline fulfillment location / Maximum orders, date 2026-01-22 ; [Store order fulfillment](https://learn.microsoft.com/en-us/dynamics365/commerce/order-fulfillment-overview), titre et résumé public indexé consultés, pas toute la page lue.
- Sources référentiels et conditions : [Product information](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information), introduction Product information management / Product definition, date 2026-07-01 ; [Global address book](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/organization-administration/overview-global-address-book), présentation / Party roles, date 2026-03-18 ; [Unified pricing management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/unified-pricing-management/upm-pricing-management-overview), introduction / Pricing components, date 2026-04-21. Trade agreements est aussi attesté dans les pages achats et pricing.
- Reformulation et adaptation : les aires servent de repères de parcours ; DOM éclaire les choix et limites des possibilités d’exécution ; produit, parties et pricing fournissent des noms de périmètres de solution proches des thèmes locaux.
- Limites : ces noms ne définissent pas une hiérarchie de capacités équivalente à P81. DOM mélange décisions, affectations et suivi ; sa présence dans la colonne D06 ne classe pas l’OMS local dans une seule couche. La règle Maximum orders ne prouve pas l’équivalence aux quotas quotidiens/hebdomadaires locaux. Les droits après fourniture dépassent Pricing.

### ELM065

- Référence : MKT19, TM Forum ODA et Open APIs.
- Nature : noms de composants ODA, notices d’API et descriptions publiques, distingués des capacités métier et du SID.
- Consultation : 2026-09-11, avec contribution indépendante ; annuaire public sans version globale affichée. Les versions suivantes sont celles des notices consultées, pas un ensemble de dernières versions homogènes.
- Source d’inventaire : [Component Directory](https://www.tmforum.org/oda/directory/components-map), noms et blocs. TMFC002 Product Order Capture & Validation, TMFC033 Purchase Management, TMFC032 Supply Chain Management, TMFC014 Location Management et TMFC012 Resource Inventory sont retenus ici comme noms repérés, sans détail complet analysé.
- Pages ouvertes et lues : [TMFC009 Service Qualification Management](https://www.tmforum.org/oda/directory/components-map/production/TMFC009), v1.1.0, 2023-08-18 ; [TMFC005 Product Inventory](https://www.tmforum.org/oda/directory/components-map/core-commerce-management/TMFC005), v1.0.4, 2024-06-27 ; [TMFC039 Agreement Management](https://www.tmforum.org/oda/directory/components-map/party-management/TMFC039), v1.1.0, 2024-08-19 ; [TMFC007 Service Order Management](https://www.tmforum.org/oda/directory/components-map/production/TMFC007), v2.0.0, 2024-02-23 ; [TMFC011 Resource Order Management](https://www.tmforum.org/oda/directory/components-map/production/TMFC011), v1.2.0, 2026-06-12, statut Pre-production.
- Notices indexées examinées : [TMFC001 Product Catalog Management](https://www.tmforum.org/oda/directory/components-map/core-commerce-management/TMFC001), v2.1.2, 2025-11-12 ; [TMFC010 Resource Catalog Management](https://www.tmforum.org/oda/directory/components-map/production/TMFC010), v1.3.2, 2024-12-03 ; [TMFC028 Party Management](https://www.tmforum.org/oda/directory/components-map/party-management/TMFC028), v2.1.0, 2024-10-14, avec TMF669 Party Role Management ; [TMFC027 Product Configurator](https://www.tmforum.org/oda/directory/components-map/production/TMFC027), v2.1.1, 2023-11-27, bloc affiché Core Commerce Management malgré le chemin de l’URL.
- Stock/réservation, notices indexées : [TMF687 Stock Management v4.0](https://www.tmforum.org/open-digital-architecture/open-apis/stock-management-api-TMF687/v4.0), date 2026-05-15 relative à une mise à jour CTK ; [guide v4.0.0](https://www.tmforum.org/resources/specification/tmf687-stock-management-api-user-guide-v4-0-0/), approuvé 2021-01-18, extraits indexés examinés, ouverture directe 403 et guide intégral non lu ; [TMF716 Resource Reservation v4.0](https://www.tmforum.org/open-digital-architecture/open-apis/resource-reservation-TMF716/v4.0), notice de l’API.
- Reformulation : Stock Management décrit quantités, seuils, consultation et réservation du stock. Service Qualification apprécie faisabilité et date sans allocation de ressource. Agreement rapproche les accords et conditions. Les composants d’ordres, de catalogues et de parties fournissent des voisins sémantiques des domaines locaux.
- Limites : Product Inventory concerne des produits attribués/utilisés par des parties et n’est pas assimilé au stock retail. Les analogies de D03/D05/D06/D07/D10 sont partielles ; ni promesse ferme complète, ni redistribution, quota magasin, faits génériques ou droits après fourniture démontrés. Les API ne sont pas des capacités par leur seule existence ; aucun modèle télécom importé comme cible FLOW.

### ELM066

- Référence : MKT03, Business Architecture Guild ; atelier public Government Reference Model Workshop.
- Nature : exemples historiques de noms de capacités et de modèles de référence, distincts d’un catalogue retail actuel.
- Version et consultation : support daté du 21 mars 2019, PDF ouvert et texte lu le 2026-09-11 avec contribution indépendante. Les dates récentes proposées par l’index ne remplacent pas celle de la couverture.
- Source et localisateurs : [atelier public](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/baguild_gov_ref_model_worksh.pdf), page PDF 10 Customer Management / Product Management / Agreement Management et exemple Agreement Structuring ; pages 11–12 illustration Partner Management attribuée à Business Architecture Associates ; page 17 Asset Management parmi les capacités supporting du Common Reference Model.
- Adaptation : repères partiels pour D04, D08, D09 ; Asset Management est trop large pour servir d’équivalent à D01. Pas de nom précis démontré ici pour D02/D03/D05/D06/D07 ou pour tout D10.
- Limites : ne vaut ni consultation du guide BIZBOK complet ni catalogue retail livré ou actuel ; les exemples et attributions sont conservés. Aucune absence de capacité dans BIZBOK déduite d’une correspondance non trouvée dans ce support.

### ELM067

- Références : [MKT04](catalogue.md#mkt04) SAP RBA et [MKT13](catalogue.md#mkt13) documentation SAP S/4HANA ; contrôle ciblé U66/U67 du 2026-09-11, avec recherche indépendante.
- Nature : distinction entre classement dans un modèle d’architecture et présentation des moyens de réalisation dans une documentation de produit. Une même expression peut désigner une aptitude métier et une fonctionnalité qui la réalise.
- RBA : [Discovering the Reference Architecture Content](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), sections Linking Business and Solution et Business Capability Model Example, texte reconsulté. Inventory Management et Order Promising sont présentés comme Business Areas ; ELM014 conserve la lecture visuelle des feuilles Product Availability Check et Product Allocation Check. Business Capability et Solution Capability sont distinctes. Édition du catalogue non exposée.
- Supply Protection : [Introducing Basic Available-to-Promise](https://learning.sap.com/courses/configuring-supply-chain-business-scenarios-in-sap-s4hana-cloud-public-edition/introducing-basic-available-to-promise_ee3a33eb-4a91-4f85-a8b6-9bc1189e9540), section Introduction to Available-to-Promise, texte ouvert et lu. Advanced Available-to-Promise (1JW) est présenté comme un solution process et Supply Protection parmi ses fonctionnalités supplémentaires. Cours Public Edition sans version affichée ; définition de protection de groupes conservée en ELM017/ELM062.
- Supply Assignment : [fiche SAP Help](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/77c07c8d30664260a0b3ff864e6b5e78/8f5e14e242b74d42bada1c39c57fe291.html), Technical Data / Use / Features, extrait indexé examiné ; ouverture directe sans texte exploitable. Enterprise Business Function SUPPLY_ASSIGNMENT_01, disponible à partir de S/4HANA 1709. Cette borne ne date pas chacune des fonctionnalités décrites et ne donne pas l’édition courante de la page. Une fonction logicielle activable n’est pas un niveau Business Capability du catalogue RBA.
- Articulation produit : [Comparing with SAP Fashion Management Solution](https://learning.sap.com/courses/outlining-sap-s-4hana-for-fashion-and-vertical-business-and-implementing-best-practices/comparing-with-sap-fashion-management-solution-fms-1), section Order Fulfillment, texte consulté, édition non affichée ; intégration des fonctionnalités d’affectation à aATP. ELM032 conserve les lectures antérieures et la distinction affectation/confirmation.
- Reformulation et adaptation : protéger des ressources pour des usages ou groupes et couvrir des demandes par des ressources admissibles sont des aptitudes métier. Leurs définitions locales détaillées restent proposées. Allocation Run relève des mécanismes de réalisation ; une fonctionnalité ou un traitement peut contribuer à plusieurs capacités, sans équivalence un-à-un.
- Limite de preuve : aucun classement natif exact Supply Protection ou Supply Assignment comme Business Area, Business Capability RBA ou Solution Capability RSA n’est établi dans ce corpus. Ce résultat ne prouve ni leur absence des catalogues ni l’absence d’aptitudes métier correspondantes. Aucune configuration Beaumanoir ou Boardriders démontrée. Voir C49 et CMP038.

### ELM068

- Références : MKT04/MKT13 SAP, MKT14 Microsoft Dynamics 365, MKT19 TM Forum. Contrôle ciblé D01 du 2026-09-11 ; pages publiques ouvertes et texte lu. Les bandeaux de connexion Microsoft n’empêchaient pas la lecture du contenu ; aucune connexion utilisée.
- SAP RBA : [Discovering the Reference Architecture Content](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), Business Capability Model Example : Inventory Management est une Business Area sous Supply Chain Execution et Supply – Fulfill Demand. Édition du catalogue non exposée ; ELM014 conserve la preuve visuelle antérieure des feuilles, dont Physical Inventory. Pas de nouvelle lecture visuelle des feuilles dans ce contrôle.
- SAP produit : [Defining Inventory Management and Physical Inventory](https://learning.sap.com/courses/inventory-management-and-physical-inventory-in-sap-s-4hana/defining-inventory-management-and-physical-inventory-1), Managing Stocks by Quantity / Planning, Entry, and Documentation of Goods Movements / Carrying Out the Physical Inventory ; édition non affichée. Quantités et états, lots et stocks spéciaux ; Goods Receipt, Goods Issue, Stock Transfer et Transfer Posting ; comparaison au comptage et ajustement. Les Transfer Postings peuvent changer la qualification sans déplacement physique. La source traite aussi quantités commandées, réservations et valeur ; ne pas assimiler son périmètre complet à D01. Sommaire Analyses : listes de stock et documents repérées, sans lecture de la leçon détaillée.
- Microsoft périmètre : [Inventory management overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-home-page), présentation, page datée 2025-08-29 ; module incluant opérations entrantes/sortantes et contrôle, périmètre de solution plus large que D01.
- Microsoft visibilité : [Inventory Visibility Add-in overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility), présentation / Get a global view of real-time inventory / Central inventory adjustment / Inventory Visibility terminology ; page datée 2025-08-14. Vision de quantités et états multisources et multilieux, mises à jour et dimensions. Réservations, ATP et allocation également décrits ; leur présence dans le produit ne les rattache pas à D01. La mention temps réel n’établit pas une garantie locale de fraîcheur ou de non-double-comptage.
- Microsoft faits et écarts : [Inventory journals](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-journals), introduction / Types of inventory journals / Transfer / Counting / Inventory adjustment ; version de produit non établie. Transactions, comptage et corrections de quantités. Un Transfer journal ne suit pas le stock en transit ; la documentation renvoie à Transfer order pour ce besoin. Ne pas généraliser le comportement d’un journal à tous les transferts.
- TM Forum : [Stock Management API TMF687 v4.0](https://www.tmforum.org/open-digital-architecture/open-apis/stock-management-api-TMF687/v4.0), Overview et Release history. Représentation du stock, consultation, modification, ajustement, réservation et notifications. La date 15 mai 2026 correspond à une mise à jour CTK ; pas une nouvelle version homogène de modèle métier. Notice lue, guide complet non lu. Une notification ne prouve pas un historique de faits de gestion ni un rapprochement physique.
- Adaptation : appuis sémantiques séparés pour les quatre aptitudes D01.a–d, avec rapprochement particulièrement lisible de la consolidation à Inventory Visibility. Les termes de produit éclairent les capacités sans les réduire à leurs réalisations (C49).
- Limites : aucune équivalence complète de domaine ou de capacité, aucune exhaustivité du marché et aucune configuration Beaumanoir prouvées. BIZBOK/Guild et ARTS sont repris à partir de ELM066/ELM024, sans nouvelle consultation dans ce contrôle.

### ELM069

- Références : MKT14 Microsoft Dynamics 365 et MKT13 SAP S/4HANA ; examen ciblé du 2026-09-11 après U75, textes publics ouverts et consultés.
- Microsoft réservation : [Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), introduction / Sample use case for soft reservation / Configure reservation mappings and dimensions / Example available-for-reservation calculation. La soft reservation modifie la quantité réservée et la quantité disponible à réserver, sans mouvement physique immédiat ; création, ajustement, annulation et compensation à la consommation sont décrits. Une mesure calculée détermine la disponibilité pour réservation selon les mesures retenues. Borne 10.0.33 pour la fonctionnalité citée de réservation depuis les commandes de vente, pas version homogène de toute la page. Aucun cycle installé Beaumanoir déduit.
- Microsoft représentations : [Inventory Visibility Add-in overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility), introduction / Feature highlights / Inventory Visibility terminology, date affichée 2025-08-14. Mesures et dimensions, visibilité multisource, quantités réservées et calculées ; physique dans le vocabulaire des mesures produit ne signifie pas nécessairement stock matériellement présent. Le produit réunit ces comportements sans imposer nos domaines.
- SAP affectation : [Comparing with SAP Fashion Management Solution](https://learning.sap.com/courses/outlining-sap-s-4hana-for-fashion-and-vertical-business-and-implementing-best-practices/comparing-with-sap-fashion-management-solution-fms-1), Order Fulfillment ; cours sans édition affichée, texte reconsulté. Intégration des fonctionnalités de Supply Assignment à aATP ; prolongement de ELM032/ELM067. Cet appui ne fournit pas une feuille RBA exacte ni une équivalence complète avec l’aptitude locale.
- Reformulation : réservation et disponibilité calculée sont reliées, sans changement physique nécessaire ; la disponibilité dépend des mesures et règles de l’usage. L’affectation relie couverture de demande et ressources. Ces lectures confortent la distinction des résultats métier sans imposer des applications ou des objets distincts.
- Limites : la formule illustrative de Microsoft n’est pas transposée comme formule universelle. Pool logique, vue et ressource future restent distincts ; aucun calcul de priorité ou garantie d’absence de survente locale déduits. Les autres comparaisons D01 restent celles de ELM068/CMP039/CMP040.

### ELM070

- Référence : MKT13, SAP Inventory Management ; examen du 2026-09-11, textes SAP Learning ouverts et lus.
- Sources : [Outlining Reservations in SAP S/4HANA](https://learning.sap.com/courses/inventory-management-in-sap-cloud-erp/outlining-reservations-in-sap-s-4hana-1), Function and Origin of a Reservation / Structure of a Reservation / Goods Movement with Reference to a Reservation ; [Checking Availability](https://learning.sap.com/courses/inventory-management-in-sap-cloud-erp/checking-availability-1), Dynamic Availability Check / Customizing – Set up Availability Check. Cours sans édition produit exposée.
- Nature : documentation de capacités de réalisation et d’objets de produit ; pas nouveau rang RBA attesté.
- Reformulation : Reservation planifie une mise à disposition de marchandises pour un mouvement, une date et un usage. Sorties et transferts notamment ; document avec lignes article/quantité/date/lieu. Origines manuelles, besoins d’ordres/projets et transferts de réassort décrits. Ne pas assimiler automatiquement toute commande client à ce document.
- Disponibilité : le contrôle dynamique peut considérer stocks, entrées prévues et sorties/réservations ; il est utilisé notamment à la réservation et à la sortie de marchandises. L’exemple SAP 100 en stock, 30 et 20 réservées ne laisse que 50 disponibles ; une tentative de retrait de 60 déclenche avertissement ou erreur selon configuration.
- Limites : ne conclure ni que la réservation MM bloque toujours absolument le stock ni qu’elle ne le protège jamais. Effet du contrôle et comportement en cas d’insuffisance dépendent des règles documentées. Aucun paramétrage ni cycle local Beaumanoir démontrés.

### ELM071

- Référence : MKT14, Microsoft Dynamics 365 Supply Chain Management ; examen du 2026-09-11, pages publiques ouvertes et textes lus malgré les bandeaux génériques de connexion.
- Source principale : [Reserve inventory quantities](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities), introduction / Inventory reservation policies / Policies on the Inventory and warehouse management parameters page ; date affichée 2025-08-29, pas release homogène déduite. La réservation pour une commande empêche le prélèvement pour d’autres commandes sauf annulation totale ou partielle. Elle peut porter sur le stock présent et, selon configuration, sur des articles commandés mais pas encore reçus ; Reserve ordered items est explicité. Ventes, production et transferts sont documentés.
- Source de granularité : [Reservations in Warehouse management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/reservations-in-warehouse-management), Reservation hierarchies / Making reservations on different levels / On-hand representation and calculations, version globale non établie. Reserved physical et Reserved ordered sont distingués. Pour les articles et entrepôts concernés, les dimensions peuvent être précisées progressivement : réserver à une maille site/entrepôt/état sans fixer immédiatement l’emplacement ou l’unité logistique. Un reserved physical n’est donc pas nécessairement une pièce individuelle déjà sélectionnée.
- Source de soft reservation : [Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), Sample use case / Integrate soft reservations and offsets with Supply Chain Management ; page évolutive, conditions de version détaillées selon fonction, dont 10.0.33 pour la réservation depuis les commandes. Quantité encore réservable diminuée sans mouvement physique ; compensation lors du passage à une réservation ERP ou de la consommation, selon les règles d’intégration. Ne pas déduire une expiration automatique de soft, ni un caractère non engageant du seul adjectif.
- Adaptation : appui pour engagement de quantité présent/futur, précision de la ressource et cohérence entre représentations d’un même engagement. Réservation Microsoft peut inclure une liaison ressource/demande proche de ce que le modèle local appelle affectation.
- Limites : ces mécanismes sont des réalisations, pas une taxonomie de capacités locales imposée. Aucun FIFO, lot, source de vérité centralisée, configuration ou garantie d’absence de survente attribués à Beaumanoir. Les détails WMS n’entrent pas dans les développements FLOW par cette comparaison.

### ELM072

- Référence : MKT13, SAP S/4HANA Advanced Available-to-Promise ; examen du 2026-09-11.
- Sources et accès : [Quantities Reserved by Supply Assignment (ARun) in aATP](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/e11ff055aa2a6d55e10000000a4450e5.html), Use / Features / Example ; [Quantities Reserved by Supply Assignment (ARun) in MRP](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/f04ff9550e5d7e43e10000000a4450e5.html), Use / Features. Extraits indexés détaillés examinés, ouvertures directes sans texte exploitable. Version affichée dans l’index : 2025 FPS01 (Feb 2026) ; exemples portant des dates anciennes conservés comme illustrations de la source, pas datation de la fonctionnalité.
- Nature : effet des résultats de Supply Assignment sur calculs ATP/MRP, documentation de produit.
- Reformulation : SAP nomme explicitement les quantités réservées par Supply Assignment. Les stocks ou entrées futures déjà affectés à des besoins sont pris en compte comme engagés ; aATP ne peut promettre que la part restant disponible. Le besoin et la ressource affectés sont considérés ensemble.
- Adaptation : l’affectation peut produire un effet de réservation ; il n’est pas établi qu’il faille toujours deux engagements indépendants ou deux capacités entièrement disjointes. Cette observation est cohérente avec les précautions ELM032/ELM067, désormais mieux documentées.
- Limites : ne pas confondre cet effet avec le document Reservation de MM-IM. Les pages ne prouvent ni configuration Boardriders ni feuille RBA sous ces noms ; traitement MRP comporte des conditions/exceptions et n’est pas généralisé. Aucun lien natif un-à-un avec nos objets ou contrats.

### ELM073

- Référence : MKT14, Microsoft Dynamics 365 Supply Chain Management ; descriptions de produit, pas catalogue de capacités.
- Consultation : 2026-09-11, textes publics ouverts et lus. Version produit globale non précisée dans les passages utilisés.
- Source : [Purchase agreements](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements), page mise à jour le 2026-09-08 ; introduction, Policies for purchase agreements et Fulfillment calculations. Accords avec période de validité, engagements en quantité ou valeur, suivi du restant et option Max is enforced plafonnant le cumul des lignes de commande. Le reliquat est présenté comme engagement à satisfaire ; il ne démontre pas seul une quantité livrable à une date.
- Source : [Inventory Visibility on-hand change schedules and ATP](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-available-to-promise), page du 2025-06-17 ; How the on-hand change schedule and ATP calculations work. Dates et quantités attendues distinctes des quantités présentes ; scheduled supply et calcul ATP par horizon. À réception, l’exemple actualise la quantité présente et compense la variation prévue. Uncommitted qualifie ici la variation non encore appliquée au stock, pas nécessairement une commande non engagée chez un fournisseur.
- Source : [Set up a location directive for purchase order putaway](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/tasks/set-up-location-directive-purchase-order-put-away), titre et introduction ; putaway désigne le rangement des articles reçus vers leurs emplacements. Édition non relevée ; appui terminologique uniquement.
- Adaptation proposée : séparer potentiel contractuel, ressource attendue et résultat de disponibilité ; relier les transitions pour éviter les doubles comptes. Ces notions éclairent U79, sans imposer objets logiciels ni formule Microsoft.
- Limites : pas de preuve qu’un reliquat de contrat soit une entrée ATP native, ni que tout achat planifié soit réservable. Autorités et règles locales non établies.

### ELM074

- Référence : MKT13, SAP S/4HANA aATP ; description de produit.
- Libellé natif : Backorder Processing, passage relatif à Supply Assignment ; identifiant de page 6b8eb017a1d1431abde00056a249f72b.
- Source : [SAP Help — Backorder Processing](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html).
- Consultation : 2026-09-11, extrait indexé examiné ; ouverture directe sans texte exploitable. Version non affichée dans l’extrait, guide intégral non lu.
- Contenu consulté : stock physique et réceptions futures sont pertinents pour Supply Assignment ; l’extrait cite purchase orders, production order header, shipping notifications, planned orders et purchase requisitions. Il mentionne aussi la configuration du périmètre de contrôle de disponibilité.
- Reformulation : l’affectation peut considérer plusieurs origines de ressources futures, y compris des éléments planifiés selon les règles du produit.
- Adaptation : appui partiel à l’aptitude D02.e située en D03 et à U79 ; conserver nature, date, fermeté et admissibilité de chaque ressource.
- Limites : ne prouve ni admissibilité inconditionnelle de tous les éléments, ni utilisation directe d’un reliquat contractuel fournisseur, ni configuration Boardriders. Les planned orders SAP ne sont pas assimilés aux Planned Purchase Orders du récit ; aucun classement RBA déduit.

### ELM075

- Référence : MKT13 SAP S/4HANA ; vocabulaire de documentation produit, distinct du rang natif RBA déjà examiné en ELM014.
- Consultation : 2026-09-11, texte public ouvert et lu ; cours sans version de produit affichée.
- Source et localisateurs : [Defining Inventory Management and Physical Inventory](https://learning.sap.com/courses/inventory-management-and-physical-inventory-in-sap-s-4hana/defining-inventory-management-and-physical-inventory-1), The Tasks of Inventory Management / Managing Stocks by Quantity et Carrying Out the Physical Inventory.
- Libellés et contenu : Managing Stocks by Quantity désigne l’enregistrement des variations et la mise à jour des quantités ; le texte distingue libre utilisation, contrôle qualité, commandé non reçu et réservé. Physical Inventory est expliqué par un comptage physique, une comparaison aux quantités enregistrées et la régularisation des différences. Le terme stock-taking est employé dans cette explication.
- Source historique complémentaire : [physical inventory document (MM-IM)](https://help.sap.com/saphelp_snc70/helpdata/EN/35/26c065afab52b9e10000009b38f974/content.htm?no_cache=true), SAP Library Glossary, chemin snc70 ; édition exacte/date non affichées. Texte consulté : document de préparation, enregistrement des comptages et différences ; rapprochement explicite avec stocktaking process. Source historique uniquement, pas preuve de nouveauté S/4HANA.
- Adaptation : Manage inventory quantities est une proposition locale simplifiant le libellé SAP, avec états physiques/logiques et futur explicités dans la définition. Count and reconcile inventory propose de nommer le résultat de comptage et rapprochement ; Stocktaking est un intitulé court possible.
- Limites : aucun de ces deux libellés locaux n’est présenté comme une feuille SAP native. La mise à jour des stocks rapproche D01.a et D01.b ; pas de preuve de leur séparation obligatoire. La valorisation décrite par SAP ne rejoint pas le périmètre FLOW.

### ELM076

- Référence : MKT14 Microsoft Dynamics 365 ; distinguer notions et fonctions de produit, business process area et processus. Consultation : 2026-09-11, pages anglaises publiques ouvertes et lues ; version produit globale non précisée.
- [Inventory on-hand list](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-on-hand-list), introduction et Query your on-hand inventory : vue des biens, disponibilités, attentes et réservations, actualisée par les transactions. Date de page non relevée. On-hand inventory est ici une notion/vocabulaire de vue, pas une capacité nommée ; ne pas réduire automatiquement tout le contenu aux seules quantités physiquement présentes.
- [Maintain inventory levels](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/inventory-to-deliver-maintain-inventory-levels-overview), page anglaise du 2026-07-15 : introduction et process flow. Business process area dans Inventory to deliver, avec mouvements, comptages et ajustements. Count inventory est un processus listé. Périmètre plus large que D01.a ; la copie linguistique indexée datée de 2025 ne remplace pas la page anglaise consultée.
- [Inventory journals](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-journals), page du 2025-08-29, section Counting : enregistrement du comptage et ajustements pour rapprocher les différences. Counting est un type de journal de produit, pas un niveau natif de capacité. Cycle counting est cité comme variante ; aucune organisation de comptage importée dans la capability map.
- Reformulation et adaptation : le vocabulaire distingue connaissance des quantités, comptage et corrections. Inventory accuracy apparaît comme bénéfice/finalité dans Maintain inventory levels. Proposer Manage inventory quantities et Count and reconcile inventory pour les aptitudes locales, sans affirmer qu’il s’agit de noms Microsoft exacts.
- Limites : aucune paire de feuilles natives équivalentes à D01.a/D01.d prouvée. On-hand et Maintain inventory levels ne couvrent pas exactement la même maille ; ni fiabilité absolue, ni cible de moteur, ni configuration Beaumanoir démontrée.

**Complément ELM076 — U84, 2026-09-11 :** page anglaise Inventory journals ouverte et section Counting relue ; date affichée 2025-08-29. Le même passage associe comptage physique et ajustements de rapprochement. Appui à la proposition locale Counting, sans statut de Business Capability natif affirmé ni nouvelle fonctionnalité ajoutée.

### ELM077

- Références : MKT13 SAP S/4HANA, MKT14 Microsoft Dynamics 365. Audit U87, textes publics ouverts et lus le 2026-09-11 ; éditions globales non exposées dans les passages utilisés.
- SAP : [Using Advanced Available-To-Promise](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5), Product Availability Check, Backorder Processing et Confirmation Strategies. PAC détermine quantité/date et produit une confirmation ; BOP réexamine les confirmations après changement d’offre ou demande. Exemples : annulation, client prioritaire, fabrication en retard. Supply Assignment peut intervenir comme méthode de contrôle dans BOP. Ces réalisations peuvent combiner plusieurs résultats locaux ; pas de séparation logicielle imposée entre calcul, confirmation et affectation.
- Microsoft : [Order promising](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations), introduction, ATP calculations, CTP calculations. ATP prend en compte quantités non engagées, délais, entrées prévues et sorties ; ATP + Issue margin ajoute la préparation. CTP considère aussi les capacités. La formule, les moteurs et le périmètre de planification du produit ne sont pas adoptés pour FLOW ; aucune équivalence CTP avec D03 seul ou besoin de Manufacturing déduits. Date de page non relevée.
- Microsoft : [Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), introduction et Sample use case. Le cycle documenté comprend création, ajustement, annulation/libération et compensation ; il reste associé à la réservation. La configuration peut autoriser une poursuite en survente ; pas de garantie inconditionnelle déduite. Les fonctionnalités par version ne sont pas généralisées.
- Adaptation proposée : inclure la disponibilité de promesse dans D03 ; rattacher les révisions à l’objet engagé plutôt qu’à une aptitude générique sans objet défini. Les titres Supply Feasibility, Confirmation et Promise Revision sont locaux ; Supply Assignment conserve le nom déjà retenu pour l’aptitude.
- Limites : descriptions de produit, pas export exhaustif de capacités ni preuve de déploiement. La non-nécessité de D02 est une conclusion locale, pas une absence démontrée dans tous les référentiels. ELM014/ELM067 restent les preuves de rang RBA ; les réserves BIZBOK/TM Forum antérieures demeurent.

### ELM078

- Référence : MKT04, SAP Reference Business Architecture. Nouvelle lecture visuelle le 2026-09-11 du [schéma de cours](https://learning.sap.com/service/media/topic/a5b46f7b-c642-4fb7-8db0-b521946e9469/EAF00_10_en-US_media/EAF00_10_en-US_images/1BusCapabModel_Ex_image.png), colonne Order Promising ; complément de ELM014, pas remplacement d’édition.
- Source de contexte : [Discovering the Reference Architecture Content](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), section Business Capability Model. Édition de l’exemple inconnue.
- Nature : cinq éléments visibles au rang Business Capability dans une Business Area. Libellés transcrits et correspondances dans la [comparaison U89](order-promising-comparaison-capacites.md#2-ce-que-lon-peut-compter).
- Définition consultée : rangs et libellés du schéma ; définitions détaillées des cinq feuilles non disponibles dans l’image. Pas d’identifiant natif exposé. Le nombre cinq porte seulement sur cet extrait ; pas de preuve d’exhaustivité ni d’absence des capacités documentées ailleurs.

### ELM079

- Référence : MKT13 SAP S/4HANA. Textes publics lus le 2026-09-11, éditions globales non affichées.
- Sources : [Using Advanced Available-To-Promise](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5), sections PAL, ABC et Release for Delivery, complément PAC/BOP de ELM077 ; [Acquiring a Basic Understanding of ATP](https://learning.sap.com/courses/performing-the-availability-check/acquiring-a-basic-understanding-of-available-to-promise-atp-_ae470c8e-1483-46ce-b5cc-e80647e8a32b), passage SBC, extrait indexé détaillé consulté.
- Nature : comportements de produit, pas nouveaux rangs RBA déduits. Reformulation : contrôler les allocations ; chercher des alternatives ; provoquer un approvisionnement pour confirmer. SBC documente notamment la création de propositions d’approvisionnement et leur date, avec PP/DS en édition privée/on-premise.
- Adaptation et limite : [critères U89](order-promising-comparaison-capacites.md#3-couverture-éprouvée-sur-dix-critères-explicites), sans import de réalisation logistique ou de Manufacturing. PAL et SUP ne sont pas assimilés ; l’extrait RBA et ces produits ne constituent pas une édition homogène.

### ELM080

- Référence : MKT14 Microsoft Dynamics 365 Supply Chain Management. Textes publics lus le 2026-09-11 ; version globale non établie.
- Sources : [Order promising](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations), introduction, cinq méthodes de contrôle des dates, note de recalcul et CTP calculations ; date affichée 2026-04-21. [Delivery alternatives](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-alternatives), introduction, Delivery alternatives FastTab et Impact of selected alternative ; date affichée 2021-09-29.
- Nature : fonctionnalités et variantes de calcul. Reformulation : ATP/CTP éclairent la faisabilité ; alternatives de lieu, de variantes produit et de quantité partielle détaillées dans la seconde page. Les limites diffèrent selon les méthodes.
- Adaptation : ne pas réduire Microsoft au calcul de date, ni compter les cinq méthodes comme cinq capacités. La note de recalcul ne démontre pas une préemption globale de ressources entre commandes. Substitution générale et changement de variante ne sont pas équivalents. CMP047.

### ELM081

- Référence : MKT20 Oracle Fusion Cloud, édition 26B. Textes publics lus le 2026-09-11.
- Sources/localisateurs : [Overview of Global Order Promising](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fascp/overview-of-global-order-promising.html), introduction et Principles of Promising ; [Manage Supply Allocation Rules](https://docs.oracle.com/en/cloud/saas/readiness/scm/26b/order26b/26B-order-mgmt-wn-f42969.htm), introduction, allocation nodes, partage des règles avec Backlog Management.
- Nature : principes et comportements de produit. Reformulation : choix de ressources présentes/futures ou à créer, d’origines, de substitutions et de réponses fractionnées ; critères économiques possibles. Les allocations peuvent suivre des groupes de demandes et des priorités.
- Adaptation : contrôle de couverture P83, pas transposition du produit en capacités. Les sept principes ne sont pas sept capacités natives ; assignment sets ne prouve pas une équivalence avec Supply Assignment. Réexamen global du backlog et cycle d’affectation non établis par ces seuls passages. Aucun fonctionnement local déduit ; CMP047.

### ELM082

- Référence : MKT21 APICS CPIM ; [extrait officiel diffusé par ASCM](https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf), texte lu le 2026-09-11.
- Version/localisateurs : CPIM 6.1, édition 2019, PDF pages 1 et 3, pages imprimées 1-207 et 1-209, Master Scheduling and Sales et définition ATP ; PDF page 5, imprimée 1-211, Capable-to-Promise. Extrait citant le dictionnaire APICS 15e édition, pas dictionnaire complet examiné.
- Nature et reformulation : ATP, développé **Available-to-Promise**, désigne dans ce contexte la part non engagée du stock et de la production planifiée qui soutient la promesse client. CTP est distingué avec contraintes de capacité. Order promising est présenté comme la prise d’un engagement de livraison.
- Adaptation : appui au vocabulaire transverse proposé en U90 ; le calcul ou contrôle de l’ATP peut contribuer à une capacité locale de vérification. Aucun libellé natif Promise Verification ni hiérarchie en quatre capacités attestés. Pas de méthode de calcul universelle, d’architecture imposée ou d’extension FLOW à la planification de saison.

### ELM083

- Références : MKT13 SAP S/4HANA, complément Transportation Management ; MKT14 Microsoft et MKT20 Oracle pour promesse et transport. Contrôle le 2026-09-11.
- SAP : [Defining Planning Processes](https://learning.sap.com/courses/business-processes-in-sap-s-4hana-transportation-management/defining-planning-processes_c47bf785-22c2-4136-8ffd-83b8a22718d6), The Planning Processes et International Transportation, texte public ouvert et lu ; édition globale non affichée. Reformulation : planifier des acheminements peut combiner des modes, des étapes, des contraintes de capacité et des choix de transporteur. Nature : description de produit et processus, pas nouvelle feuille RBA attestée.
- Microsoft : [Delivery alternatives](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-alternatives), introduction, Delivery date control methods et Delivery alternatives FastTab, texte relu ; date affichée 2021-09-29. Mode, calendriers et délais de transport influencent les solutions et dates proposées. Cela ne prouve pas à lui seul une conception complète de chaînes multimodales dans cette fonction.
- Oracle : [Overview of Global Order Promising](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fascp/overview-of-global-order-promising.html), 26B, Supply Chain et Principles of Promising, texte relu ; modes et coûts de transit interviennent dans le choix des solutions. Ne pas assimiler ce comportement à tout Transportation Management.
- Adaptation : Fulfillment Route Decision est un nom local pour choisir l’acheminement qui soutient la promesse ; son autonomie et son domaine propriétaire restent proposés. Source et route peuvent être choisis conjointement ; aucun processus obligatoire ni périmètre de réalisation FLOW supplémentaire. CMP050.

### ELM084

- Référence : MKT14 Microsoft Dynamics 365, produits Supply Chain Management et Business Central explicitement distingués. Textes publics lus le 2026-09-11.
- [Order promising — Supply Chain Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations), ATP calculations et CTP calculations, date affichée 2026-04-21 : ATP inclut les ressources non engagées et les réceptions prévues ; CTP ajoute les capacités.
- [Calculate sales order delivery dates using CTP — Supply Chain Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp), How CTP compares to ATP, Near real-time CTP et comparaison des moteurs, date de page non relevée : la disponibilité des composants et des ressources de fabrication peut fonder une réponse lorsque le produit fini manque. Modalités de calcul dépendantes de version et configuration ; Near real-time CTP et Batch CTP sont des réalisations, pas deux capacités métier. C62 conserve la divergence avec la page générale ; conditions de version 10.0.41 et activation précisées dans la page détaillée.
- [Calculate order promising dates — Business Central](https://learn.microsoft.com/en-us/dynamics365/business-central/sales-how-to-calculate-order-promising-dates), About order promising, Available to promise, Capable to promise et Calculations, version globale/date de page non relevées : CTP raisonne sur le manque et la possibilité de produire, acheter ou transférer ; acceptation des dates peut créer des lignes de planification/réservation. Ne pas attribuer ce cycle tel quel à Supply Chain Management.
- Nature : concepts et comportements de produit ; adaptation locale ATP/CTP comme contributions possibles à Promise Proposal, CTP lié partiellement à Supply Creation Decision. Pas d’équivalence avec deux capacités locales, ni de promesse engageante déduite d’un calcul seul. CMP051.

### ELM085

- Référence : MKT13, SAP, lecture du 2026-09-11. [Describing Sales Order Management](https://learning.sap.com/courses/exploring-end-to-end-business-processes-in-sap-business-suite/describing-sales-order-management_ca7b816e-af6f-4a03-bd88-1a5bb42cef84), Sales Order Overview et Sales Order Processing ; texte public ouvert, édition globale inconnue. Complément à ELM063.
- Nature : description de produit et processus, pas nouveau rang RBA. Reformulation : la commande de vente rassemble parties, produits, conditions et résultats de contrôles, dont disponibilité et prix. Le cours présente aussi des rubriques séparées pour achats et contrats, sans analyse nouvelle complète de ces leçons.
- Adaptation : appui à la connaissance d’un engagement commercial et à ses relations avec la promesse/pricing. Ne pas copier les fonctions entourant l’objet Sales Order comme autant de capacités D04 ; ne pas fusionner les objets ou reprendre les rôles organisationnels du produit.
- Limites : les appuis Purchase Order Management de ELM063 et sous-traitance ELM043 restent antérieurs ; aucun domaine natif Commercial Commitments ni équivalence globale démontrés. CMP053.

### ELM086

- Référence : MKT14 Microsoft Dynamics 365 Supply Chain Management ; textes publics lus le 2026-09-11, pas édition produit globale établie.
- [Purchase agreements](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements), Commitment types, Fulfillment calculations, Confirmations and version history et Purchase agreements and intercompany trade ; date de page non relevée. Engagements, consommation/reliquat et historique illustrent le rapprochement D04, sans formule locale importée.
- [Sales agreements overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-agreements), mêmes sections et Returning an item ordered from a sales agreement ; date affichée 2026-04-27. Accord et commandes liées sont distingués. Une confirmation dans ce produit peut historiser une version sans être une condition de création de commande ; ne pas l’assimiler automatiquement à Promise Confirmation ou à l’entrée en vigueur d’une obligation.
- [Sales returns](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns), Return order process et Return material authorization ; date/version non relevées. Autoriser le renvoi ne vaut pas acceptation des biens ou attribution d’un crédit ; inspection et décisions ultérieures sont distinguées.
- Nature : documents, fonctionnalités et processus de produit ; reformulation et appui partiel à P84, pas quatre capacités natives équivalentes. Le modèle commun achats/ventes demeure local ; aucune règle de déploiement Beaumanoir, obligation juridique universelle ou import des capacités financières/logistiques. CMP053.

### ELM087

- Référence : MKT13 SAP MDG et MKT14 Microsoft Dynamics 365.
- Objet : Identité commune et spécialisations client/fournisseur.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [SAP Business Partner](https://learning.sap.com/courses/sap-master-data-governance-on-sap-s-4hana/explaining-the-integrated-object-model-for-the-business-partner), Integrated Object Model, données générales et dépendantes du rôle ; édition/date de publication non affichées.
- Source : [Microsoft Global address book](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/organization-administration/overview-global-address-book), introduction, Party roles et adresses ; page datée 2026-03-18.
- Reformulation : SAP relie Customer et Supplier au même Business Partner ; Microsoft permet plusieurs rôles sur une Party. Les données communes ne suppriment pas les attributs propres à la relation commerciale.
- Adaptation et limites : Modèles et fonctionnalités de produit. Appui à D09 partagé, pas à l’administration locale ni à une définition de Party limitée aux personnes morales. Aucun déploiement prouvé.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM088

- Référence : MKT13 SAP S/4HANA et MKT14 Dynamics 365.
- Objet : Contrats achats et ventes, distincts des commandes.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [SAP accords achats](https://learning.sap.com/courses/sap-s-4hana-contract-management/outlining-purchasing-agreements-in-sap-s-4hana), Purchasing Agreements et Key Features ; édition non affichée.
- Source : [SAP contrats ventes](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-sales-fundamental-business-processes/executing-solution-process-sales-contract-management-i9i-_cfe682c7-61d0-41a7-b730-e62c7d63dc55), Business Process Overview, périmètre I9I ; édition non affichée.
- Source : [Microsoft accords achats](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements), Commitment types, Fulfillment calculations et Apply purchase agreements ; date non relevée.
- Source : [Microsoft accords ventes](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-agreements), Commitment types, Pricing terms, Policies, Fulfillment ; contrôle du contenu, date antérieure 2026-04-27 consignée en ELM086.
- Reformulation : Les deux suites distinguent les contrats d’achat et de vente. SAP distingue aussi contrats et scheduling agreements. Microsoft expose plafonds et consommation par des commandes liées. Les contrats examinés peuvent viser des articles, catégories, quantités ou valeurs ; un lien à un catalogue nommé n’est pas une structure universelle démontrée.
- Adaptation et limites : Objets/processus produit, sans règle juridique générale. Le reliquat de contrat n’est ni un stock reçu ni un futur certain. D11 peut recevoir les deux variantes sans dupliquer sa capacité d’ingestion ; autorité des consommations à instruire.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM089

- Référence : MKT13 SAP S/4HANA et MKT14 Dynamics 365.
- Objet : Commandes achats et ventes spécialisées et reliées.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [SAP commande achat](https://learning.sap.com/courses/exploring-end-to-end-business-processes-in-sap-business-suite/managing-purchase-orders_dda0b0d0-7da6-43ec-b162-4faa1a6f339b), Purchase Order Overview, Sending Purchase Order, Document Structure ; édition inconnue.
- Source : [SAP commande vente](https://learning.sap.com/courses/exploring-end-to-end-business-processes-in-sap-business-suite/describing-sales-order-management_ca7b816e-af6f-4a03-bd88-1a5bb42cef84), Sales Order Overview et Processing ; édition inconnue, complément ELM085.
- Source : [Microsoft intercompany](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/intercompany-orders-and-return-orders), About intercompany orders, exemples commandes/retours/accords ; page 2026-05-29.
- Reformulation : La commande d’achat demande une fourniture au fournisseur ; la commande de vente porte la demande client et ses confirmations. SAP distingue les deux traitements. Microsoft relie deux commandes achat/vente en intercompany sans les fondre en un seul document.
- Adaptation et limites : Cette spécialisation produit motive une épreuve de D04 ; elle ne prescrit pas deux domaines de capacités ni une architecture OMS. Une commande d’achat peut exister sans document précédent. Les processus complets incluent des fonctions hors FLOW.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM090

- Référence : MKT13 SAP S/4HANA et MKT14 Dynamics 365 Commerce/SCM.
- Objet : Catalogues d’approvisionnement et de vente.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [SAP catalogues achats](https://learning.sap.com/courses/describing-requisitioning/managing-catalog-items_ed8d8ea7-25c0-46ab-a4c2-533e135916f4), Catalogs in Sourcing and Procurement, Internal/External Catalog ; édition non affichée.
- Source : [Microsoft catalogues achats](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-catalogs), introduction et Prerequisites ; page 2026-07-01.
- Source : [Microsoft catalogues B2B](https://learn.microsoft.com/en-us/dynamics365/commerce/catalogs-b2b-sites), introduction, Price groups, catalogues/canaux/assortiments ; versions 10.0.27+, page 2026-01-21.
- Reformulation : Les catalogues achats des pages SAP/Microsoft servent la sélection dans les demandes d’achat ; les catalogues Commerce B2B organisent les offres aux clients et se relient à des groupes de prix. Microsoft distingue ces parcours et contenus.
- Adaptation et limites : Les deux pages achats concernent surtout les besoins internes/achats indirects : elles ne prouvent pas le découpage de l’achat de marchandises à revendre. Ne pas confondre catalogue du fournisseur vu par un acheteur et tout le référentiel produit. Aucune capacité de publication ou validation locale proposée.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM091

- Référence : MKT14 Microsoft Dynamics 365 SCM.
- Objet : Définition produit commune et données importables.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [Microsoft Product information](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information), Product definition, Distribution/export/import, Product masters/variants ; page 2026-07-01.
- Reformulation : La définition produit partagée comprend identifiants, variantes, unités et conversions. Elle peut être importée de PLM/PDM/PIM. Le catalogue commercial seul ne démontre donc pas la couverture des références articles opérationnelles.
- Adaptation et limites : Description de produit et de distribution d’information. Appui à un besoin de Product Reference Ingestion, pas au rétablissement de D08.a–c en administration locale.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM092

- Référence : MKT13 SAP Retail, MKT14 Dynamics 365, MKT19 TM Forum.
- Objet : Données de prix et application de règles distinctes du catalogue.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [SAP prix Retail](https://learning.sap.com/courses/exploring-sap-s-4hana-cloud-public-edition-retail/performing-sales-pricing-for-retail-3i4-), Sales Pricing for Retail, niveaux de prix, validité et application des conditions ; périmètre 3I4, édition inconnue.
- Source : [Microsoft Unified pricing](https://learn.microsoft.com/en-us/dynamics365/supply-chain/unified-pricing-management/upm-pricing-management-overview), Pricing components, Architecture overview ; page 2026-04-21.
- Source : [TM Forum configurateur](https://www.tmforum.org/resources/specifications/tmfc027-product-configurator-v2-2-0/), notice publique, description et General Information ; 2.2.0 Team Approved 2026-03-24, publiée 2026-03-31, signalée Pre-production.
- Reformulation : SAP distingue conditions tarifaires, niveaux et périodes puis leur application. Microsoft calcule les prix de vente selon attributs et règles, consommables par d’autres applications. La notice TM Forum distingue les prix du catalogue de l’application des règles par le configurateur.
- Adaptation et limites : Ne pas affirmer un référentiel Pricing séparé universel : TM Forum conserve les prix au catalogue. La notice 2.2.0 n’est pas la Production ; lien annoncé 2.1.2 en échec à l’ouverture, spécification membre non lue. Unified pricing ne prouve pas unification achat/vente ni équivalence entre Vendor list price et prix d’achat engagé.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM093

- Référence : MKT13 SAP S/4HANA et Retail.
- Objet : Relations fournisseur/article et décision de source d’approvisionnement.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [SAP Purchasing Info Records](https://learning.sap.com/courses/sourcing-in-sap-s4hana/working-with-purchasing-info-records), Sources of Supply, Purchasing Info Record, Purchase Order Default Price ; édition inconnue.
- Source : [SAP procurement Retail](https://learning.sap.com/courses/exploring-sap-s-4hana-cloud-public-edition-retail/ordering-merchandise-with-procurement-for-retail-5fm-_fe298f93-84ad-47ff-98ff-658e887e020d), Procurement for Retail, Supply source determination, Retail-specific source determination ; périmètre 5FM.
- Reformulation : L’info record associe fournisseur et article avec conditions et délai. Le choix de source utilise des informations distinctes, dont contrats et listes de sources ; le cas Retail permet sources internes et externes. Le prix de référence et celui appliqué à une quantité commandée peuvent différer.
- Adaptation et limites : Les priorités de sélection sont propres aux variantes de produit et ne sont pas importées. Un quota fournisseur répartit l’approvisionnement ; il n’est pas automatiquement la protection de stock D01. Le choix opérationnel de fournisseur est à éprouver hors de la seule promesse client.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM094

- Référence : MKT13 SAP Retail.
- Objet : Assortiment et listing temporel.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [SAP assortiments](https://learning.sap.com/courses/exploring-sap-s-4hana-cloud-public-edition-retail/managing-assortments-3i5-), Assortments 3I5, association article/site et périodes de listing ; édition inconnue.
- Reformulation : Le listing associe articles et sites sur une période pour les opérations d’approvisionnement ; la leçon distingue ces périodes de la période de vente portée par l’article.
- Adaptation et limites : Différence de données à recevoir et de règles à appliquer ; ne pas créer un domaine de planification saisonnière ou de conception d’assortiment dans FLOW. La présence d’un article au catalogue ne suffit pas à prouver son admissibilité dans chaque lieu/date.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM095

- Référence : MKT13 SAP Retail.
- Objet : Sites et lieux opérationnels.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [SAP sites](https://learning.sap.com/courses/exploring-sap-s-4hana-cloud-public-edition-retail/maintaining-sites-for-retail-3i3-), Sites for Retail, Site and Organizational Assignments, site/storage location ; périmètre 3I3.
- Reformulation : SAP distingue magasins, centres de distribution et emplacements, reliés aux structures de l’entreprise. Le lieu opérationnel n’est pas réductible à l’identité d’un fournisseur ou client.
- Adaptation et limites : Ne pas reproduire les structures organisationnelles SAP dans la carte générique. D06 contient déjà des connaissances de lieux ; séparer réception des références et appréciation des possibilités d’exécution, sans choisir de maître ni créer automatiquement un domaine.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM096

- Référence : MKT19 TM Forum ODA.
- Objet : Parties, accords, catalogues et ordres : composants distincts.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [TMFC028 Party](https://www.tmforum.org/oda/directory/components-map/party-management/TMFC028), description, APIs dépendantes ; 2.1.0, publiée 2024-10-14.
- Source : [TMFC039 Agreement](https://www.tmforum.org/oda/directory/components-map/party-management/TMFC039), description, APIs exposées/dépendantes ; 1.1.0, publiée 2024-08-19.
- Source : [TMFC001 Catalog](https://www.tmforum.org/oda/directory/components-map/core-commerce-management/TMFC001), description et APIs ; 2.1.2, publiée 2025-11-12.
- Source : [TMFC002 Product Order](https://www.tmforum.org/oda/directory/components-map/core-commerce-management/TMFC002), description ; 2.1.0, publiée 2024-11-12.
- Source : [TMFC033 Purchase](https://www.tmforum.org/oda/directory/components-map/core-commerce-management/TMFC033), notice : Planned, sans version ni publication ; spécification annoncée non publiée.
- Reformulation : Party, Agreement et Catalog sont distingués, mais l’ODA contient aussi rôles, adresses/sites, catalogues de services et ressources. Agreement a une portée transversale entre parties. Product Order est orienté client ; Purchase Management est identifié séparément mais reste Planned dans la notice.
- Adaptation et limites : Ces notices de composants et API ne sont ni le SID intégral ni une carte de capacités retail. La seule notice Purchase ne démontre pas une symétrie complète achat/vente. Spécifications détaillées membres non consultées ; versions de notices non homogènes.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM097

- Référence : MKT03 Business Architecture Guild.
- Objet : Frontière de capacité et objet métier.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [Metamodel Guide](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf), v3.0 septembre 2024, §5.2, pages PDF 17–18, imprimées 17–18 ; passage textuel relu.
- Reformulation : Les décompositions conservent l’objet du parent : l’exemple Customer ne gère pas les accords ni les produits. Le guide distingue capacité et réalisation contextuelle.
- Adaptation et limites : Appui méthodologique, pas prescription Party/Agreement/Catalog en trois domaines, pas preuve d’une scission achats/ventes dans un catalogue retail. Guide BIZBOK complet et modèles membres non lus ; aucun schéma ou tableau graphique utilisé comme preuve nouvelle.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM098

- Référence : MKT14 Microsoft Dynamics 365.
- Objet : Réexamen ciblé des cycles, contraintes et retours.
- Consultation : 2026-09-11 ; passages textuels publics ouverts et lus, sans connexion. Des bandeaux génériques de connexion Microsoft n’empêchaient pas la lecture du texte.
- Nature : documentation de produit/composant, sauf ELM097 méthodologique ; les titres ne valent pas rangs natifs de capacités.
- Source : [Réservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), introduction : créer, ajuster, libérer et compenser à la consommation ; variantes produit conservées, date non relevée.
- Source : [DOM rules](https://learn.microsoft.com/en-us/dynamics365/commerce/dom-rules), Partial orders, Offline location, Maximum rejects/orders ; page 2026-01-22.
- Source : [Retours ventes](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns), Return order process et RMA ; édition/date non relevées.
- Reformulation : Le cycle de réservation comprend ses ajustements/libérations ; les règles DOM distinguent possibilités du lieu, fractionnement et charge. Un retour autorisé ne vaut pas acceptation physique ni décision de remède.
- Adaptation et limites : Appuis partiels à la révision du D02 résiduel, à D06 et à la maille D04.d. Ne pas importer le processus DOM complet, l’exécution entrepôt ou la finance ; aucune capacité ajoutée par opération produit.
- Rapprochement : audit U99, CMP055–CMP057 ; pas de validation métier déduite.

### ELM099

- Référence : MKT22 SAP Master Data Governance on SAP S/4HANA ; édition précise inconnue, leçon évolutive.
- Libellé natif : Out-of-the-Box Domain Models ; nature : domaines de données d’une solution, pas Business Areas RBA.
- Source et localisateur : [leçon SAP](https://learning.sap.com/courses/introducing-sap-master-data-governance/describing-data-domains-and-extensibility-options), section du même nom, liste textuelle et Extensibility Options ; consultée le 2026-09-11.
- Sens consulté, reformulé : une même solution accueille des modèles spécialisés, notamment client, fournisseur, produit et finance, avec des possibilités d’extension.
- Adaptation et limite : appui à la coexistence regroupement/séparation sémantique. N’établit pas notre trio ou quartet ni un domaine unique de capacités ; la couverture native diffère des extensions et des éditions cloud. Administration et qualité des maîtres non ajoutées à FLOW.

### ELM100

- Référence : MKT14 Microsoft Dynamics 365 ; guide évolutif d’architecture et documentation Supply Chain Management, pas catalogue de capacités.
- Sources et localisateurs : [Data architecture](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/data-management-architecture), Data architecture et Types of enterprise data, date affichée 2024-01-23 ; [Product information overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information), introduction et Distribution, export, and import of product data, date affichée 2026-07-01.
- Consultation : textes publics lus le 2026-09-11 malgré bandeau générique d’authentification ; pas de version globale unique. Une tentative d’ouverture d’une page Global address book a échoué ; elle n’est pas utilisée comme preuve nouvelle.
- Sens consulté, reformulé : Microsoft réunit plusieurs sujets sous la catégorie master data, distingue celle-ci des données de configuration et transactionnelles, et documente séparément l’information produit partagée et sa réception depuis un maître externe.
- Adaptation et limite : catégorie commune compatible avec objets spécialisés ; aucune hiérarchie native Domain/Capability ni modèle de réception unique établi. ELM091 conservé comme lecture précédente du sujet produit.

### ELM101

- Référence : MKT19 TM Forum ODA ; composants et Function Blocks, pas niveaux de business capabilities.
- Sources/localisateurs : [Agreement Management](https://www.tmforum.org/oda/directory/components-map/party-management/TMFC039), description et ODA Function Block, version 1.1.0 publiée 2024-08-19 ; [Product Catalog Management](https://www.tmforum.org/oda/directory/components-map/core-commerce-management/TMFC001), mêmes champs, version 2.1.2 publiée 2025-11-12 ; [annuaire](https://www.tmforum.org/oda/directory/components-map), rubriques Party Management et Core Commerce Management.
- Consultation : notices publiques relues le 2026-09-11 ; spécifications membres non lues.
- Sens consulté, reformulé : Agreement Management et le composant Party Management sont dans le bloc Party Management ; Product Catalog Management est dans Core Commerce Management. Un bloc peut donc regrouper plusieurs sujets distincts, sans bloc unique de tous les référentiels.
- Adaptation et limite : exemple d’agrégation utile, pas prescription de rattacher Agreement à Party localement. Product Catalog englobe spécifications produit et offre ; aucune correspondance automatique au SKU retail autonome. Complète ELM096 sur le rang de regroupement.

### ELM102

- Référence : MKT03 Business Architecture Guild ; The Business Architecture Metamodel Guide v3.0, septembre 2024.
- Source/localisateur : [guide public](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf), §5.2, page PDF 17 (index 16), continuation page 18 ; texte relu le 2026-09-11. Complément de ELM097, pas lecture du guide BIZBOK complet.
- Nature : principe de définition et décomposition des capacités.
- Sens consulté, reformulé : l’objet focal d’une capacité reste celui de ses sous-capacités ; l’exemple Customer ne prend pas en charge les accords ni les produits.
- Adaptation et limite : préserver les sens sous un regroupement de présentation. Ce passage ne prescrit ni un domaine par référentiel ni la hiérarchie locale Univers/Domaine/Capacité ; ne pas présenter notre conteneur comme capacité parente certifiée Guild. Aucun modèle retail réservé aux membres consulté.

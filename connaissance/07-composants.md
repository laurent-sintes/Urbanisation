# Organisations et applications

**Statut documentaire après U106–U112 (13 septembre 2026) :** registre source de la migration, conservé pour sa provenance. Les modèles de l’existant font désormais autorité dans [panorama-as-is](../modeles/panorama-as-is/current.json). Les besoins, orientations de cible et mentions non instruits sont séparés dans le [backlog](../modeles/backlog/panorama-candidates.json). Enrichir ensuite les JSON et les sources narratives utiles, sans entretenir deux inventaires concurrents ; voir [C70](04-corrections.md#c70).

Import initial : [référentiel JSON archivé](../archive/referentiel.json), section `composants`, consolidation du 9 septembre 2026. Les statuts et réserves ci-dessous sont ceux de la source.

## ORG-GBM

**id**

ORG-GBM

**type**

Organisation

**nom**

GBM — marques historiques

**perimetre**

GBM

**role**

Retail ≈90 %, B2B ≈10 % ; variantes par marque.

**source**

U01-U03

**reserve**

Liste détaillée des marques non donnée.

## APP-STR

**id**

APP-STR

**type**

Application / famille d’instances

**nom**

Storeland

**perimetre**

GBM

**role**

Stock magasin, back-office, demandes stock-to-store et réassort automatique.

**source**

U03;U06

**reserve**

Une instance Oracle par marque ; liste, versions et spécifiques inconnus.

## APP-POS

**id**

APP-POS

**type**

Ensemble applicatif

**nom**

Logiciels POS spécialisés

**perimetre**

GBM

**role**

Caisse et commandes pour client final en magasin.

**source**

U03

**reserve**

Noms et périmètres non inventoriés ; ne pas les inventer.

## APP-WEB

**id**

APP-WEB

**type**

Ensemble applicatif

**nom**

Sites eCommerce de marque

**perimetre**

GBM

**role**

Capture du parcours de commande eCommerce.

**source**

U04

**reserve**

Technologies et autorité commande non précisées.

## APP-UR

**id**

APP-UR

**type**

Application

**nom**

UR / United Retail

**perimetre**

GBM

**role**

Stock entrepôt présent ; réception de stocks magasin ; contribution multicanale eCommerce ; alignement C-Log.

**source**

U03;U04

**reserve**

Cylande puis Cegid ; modules/versions/instances déployés non confirmés.

## APP-SOC

**id**

APP-SOC

**type**

Application

**nom**

Socloz

**perimetre**

GBM

**role**

Ship-from-store et extension de gamme.

**source**

U03;U04

**reserve**

Localisation de chaque règle, réservation et état non établie.

## APP-TAL

**id**

APP-TAL

**type**

Plateforme technique

**nom**

Talend transverse

**perimetre**

GBM / transversal déclaré

**role**

Orchestration des échanges de données, notamment batchs décrits.

**source**

U03

**reserve**

Ne pas présumer tous les flux groupe ou absence de logique métier.

## APP-ZOH

**id**

APP-ZOH

**type**

Application

**nom**

Zoho

**perimetre**

GBM B2B

**role**

CRM clients B2B.

**source**

U03

**reserve**

Source de vérité de chaque attribut et édition non établies.

## APP-ELA

**id**

APP-ELA

**type**

Application

**nom**

Elastic

**perimetre**

GBM B2B

**role**

Prise de commande B2B.

**source**

U03

**reserve**

Ne pas assimiler à Elasticsearch ; aval non décrit.

## APP-IRM

**id**

APP-IRM

**type**

Application sur mesure

**nom**

IRMA

**perimetre**

GBM

**role**

Stocks optimaux ; calcul et référence des seuils minimum réassort.

**source**

U06

**reserve**

Sur Snowflake déclaré ; en déploiement ; couverture par marque inconnue.

## APP-SCO

**id**

APP-SCO

**type**

Application en retrait

**nom**

SCORTEX

**perimetre**

GBM

**role**

Outil historique remplacé par IRMA.

**source**

U06;U07

**reserve**

Fin de vie ; retrait complet non démontré ; périmètre détaillé non fourni.

## APP-MAP

**id**

APP-MAP

**type**

Application sur mesure

**nom**

MAP

**perimetre**

GBM

**role**

Forecast, protections logiques marque/canal, anticipation stockage, planification/émission demandes d’achat.

**source**

U10

**reserve**

Snowflake hypothétique ; consommateurs et autorité applicable non établis.

## APP-CBS

**id**

APP-CBS

**type**

Application

**nom**

CBS

**perimetre**

GBM

**role**

Suivi fabrication, fournisseur→port/Carrier, douanes entrepôts sous douane.

**source**

U10

**reserve**

Éditeur/technique non précisés ; lien avec application achats initiale à confirmer.

## ALIAS-ACH

**id**

ALIAS-ACH

**type**

Mention non rapprochée

**nom**

Application achats sur mesure initialement non nommée

**perimetre**

GBM

**role**

Suivi opérationnel des commandes et circulation documentaire.

**source**

U03

**reserve**

Entrée de rapprochement ; ne signifie pas existence certaine d’un composant supplémentaire à CBS/MAP.

## ORG-CLOG

**id**

ORG-CLOG

**type**

Organisation / SI autonome

**nom**

C-Log

**perimetre**

Frontière commerce-logistique

**role**

Filiale logistique centralisée ; SI autonome ; DSI dédié.

**source**

U03;U07

**reserve**

Pas un logiciel ; pas à absorber dans l’ERP commercial.

## APP-XRD

**id**

APP-XRD

**type**

Application externe au cœur commerce

**nom**

Crossroad — éditeur KBRW

**perimetre**

SI C-Log

**role**

Choix entrepôt/transporteur, construction de parcours dont transferts, suivi logistique et file d’erreur.

**source**

U06;U07

**reserve**

Répartition WMS/TMS et composants techniques non documentée.

## SI-SAR

**id**

SI-SAR

**type**

Paysage / application sur mesure

**nom**

Sarenza

**perimetre**

Sarenza

**role**

Plateforme initialement dite marketplace ; intégration catalogues et revente B2C ; SAV fort.

**source**

U01;U02

**reserve**

Modules, interfaces, instances et autres modèles à inventorier.

## APP-ECC

**id**

APP-ECC

**type**

Application

**nom**

SAP ECC

**perimetre**

BRD

**role**

Composant du paysage BRD.

**source**

U01

**reserve**

Couverture effective à instruire.

## APP-AFS

**id**

APP-AFS

**type**

Solution SAP

**nom**

SAP AFS / Allocation Run

**perimetre**

BRD

**role**

Enjeu d’allocation majeur.

**source**

U01;U02

**reserve**

Pas d’assimilation à toutes les fonctions S/4HANA actuelles.

## APP-NEW

**id**

APP-NEW

**type**

Application

**nom**

NewStore

**perimetre**

BRD

**role**

Composant cité du paysage BRD.

**source**

U01

**reserve**

Aucune couverture détaillée déclarée dans ce fil.

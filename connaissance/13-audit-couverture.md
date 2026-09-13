# Audit de couverture initial

Import initial : [référentiel JSON archivé](../archive/referentiel.json), section `audit_couverture`, consolidation du 9 septembre 2026. Les statuts et réserves ci-dessous sont ceux de la source.

## U01

**source**

U01

**chapitres**

01, 02, 03, 04, 15, 16

**registre**

F001–F010; P01–P20; P53

**controle**

Cadrage complet, exclusions, standards, options, trois SI, niveaux et livrables.

**statut**

Couvert

## U02

**source**

U02

**chapitres**

05, 13, 15

**registre**

F009; F011–F012; F020–F025; P21–P26

**controle**

Accord méthode, deux plateformes, proportions, BRD/ARun, Sarenza revente/SAV.

**statut**

Couvert

## U03

**source**

U03

**chapitres**

06, 07, 08, 09, 10

**registre**

F017; F026–F046; FL01–FL03; FL20

**controle**

Instances, stocks, POS, UR, Socloz, Talend, B2B, achats/documents.

**statut**

Couvert

## U04

**source**

U04

**chapitres**

07, 11, 12

**registre**

F047–F063; INF01–INF03; DEC10–DEC15

**controle**

Parcours complet, 15 minutes, quotas, classement, escalade incertaine, intervention humaine.

**statut**

Couvert

## U05

**source**

U05

**chapitres**

07, 14

**registre**

F058–F060; C07; P36

**controle**

Oui contextualisé par la question A04 : annulation demande magasin uniquement.

**statut**

Couvert

## U06

**source**

U06

**chapitres**

08, 10, 11, 12

**registre**

F064–F080; FL03; FL05; FL11–FL14

**controle**

SKU, IRMA/SCORTEX, EDI, prestations, choix, transfert, suivi/file d’erreur.

**statut**

Couvert

## U07

**source**

U07

**chapitres**

01, 10, 11, 12, 13, 14

**registre**

F013–F016; F071; F081–F085; C09–C13

**controle**

KBRW/Crossroad, SCORTEX, responsabilités information/décision, autonomie C-Log.

**statut**

Couvert

## U08

**source**

U08

**chapitres**

17 / sources

**registre**

C27

**controle**

Relance conservée intégralement, sans fait métier ajouté.

**statut**

Couvert

## U09

**source**

U09

**chapitres**

01, 13, 14

**registre**

F015; C12; P45–P50

**controle**

Business Capabilities toujours centrales ; niveau pertinent non figé.

**statut**

Couvert

## U10

**source**

U10

**chapitres**

09, 11, 12, 14

**registre**

F086–F102; FL15–FL19; C15–C23

**controle**

MAP trois niveaux, CBS, hypothèse Snowflake, trois cas allocation, FIFO/mauvais payeur.

**statut**

Couvert

## U11

**source**

U11

**chapitres**

17

**registre**

F018; P51–P52; C24

**controle**

Question stockage ; transparence sur absence de dossier préexistant.

**statut**

Couvert

## U12

**source**

U12

**chapitres**

17 / sources

**registre**

C27

**controle**

Seconde relance conservée intégralement.

**statut**

Couvert

## U13

**source**

U13

**chapitres**

00, 17, contrôle

**registre**

F018; présente version

**controle**

Livraison effective du dossier exhaustif, pas annonce d’un travail futur.

**statut**

Couvert

## Audit indépendant du fil partagé — 2026-09-09

Les déclarations de couverture ci-dessus appartiennent à la consolidation initiale. Un [audit direct de la conversation](../audits/2026-09-09-conversation-chatgpt.md) a ensuite contrôlé les 30 messages affichés, confirmé U01–U13 après normalisation et réintégré des développements assistant manquants ou condensés. Consulter ce rapport pour les corrections et les limites ; la couverture du texte ne vaut pas vérification du SI.

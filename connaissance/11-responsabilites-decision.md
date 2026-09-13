# Responsabilités de décision

**Statut documentaire après U106–U112 (13 septembre 2026) :** registre source de la migration, conservé pour sa provenance. Les modèles de l’existant font désormais autorité dans [panorama-as-is](../modeles/panorama-as-is/current.json). Les besoins, orientations de cible et mentions non instruits sont séparés dans le [backlog](../modeles/backlog/panorama-candidates.json). Enrichir ensuite les JSON et les sources narratives utiles, sans entretenir deux inventaires concurrents ; voir [C70](04-corrections.md#c70).

Import initial : [référentiel JSON archivé](../archive/referentiel.json), section `responsabilites_decision`, consolidation du 9 septembre 2026. Les entrées importées conservent leur provenance ; les compléments et corrections d’audit sont datés et sourcés.

## DEC01

**id**

DEC01

**decision**

Définir des protections marque/canal

**realisation**

MAP

**reserve**

Calcul décrit ; politique et autorisation métier non identifiées

**contexte**

Planification/allocation

**source**

U10

## DEC02

**id**

DEC02

**decision**

Calculer les seuils de réassort

**realisation**

IRMA

**reserve**

Source de référence déclarée ; coexistence éventuelle avec SCORTEX, à préciser par périmètre (F069, Q009)

**contexte**

Réassort magasin

**source**

U06

## DEC03

**id**

DEC03

**decision**

Déclencher une demande de réassort

**realisation**

Storeland

**reserve**

Seuil atteint ; quantité à déterminer

**contexte**

Réassort magasin

**source**

U06

## DEC04

**id**

DEC04

**decision**

Recalculer après aléa amont

**realisation**

MAP

**reserve**

Annule et remplace des données ; aucun effet sur commandes supposé

**contexte**

Planification/opération

**source**

U10

## DEC05

**id**

DEC05

**decision**

Produire la demande fournisseur

**realisation**

MAP

**reserve**

Demande distincte d’une commande ferme à qualifier

**contexte**

Achats

**source**

U10

## DEC06

**id**

DEC06

**decision**

Autoriser une vente sans stock

**realisation**

Politique GBM : non

**reserve**

Contrôle technique et stock de référence non établis

**contexte**

Ventes GBM

**source**

U10

## DEC07

**id**

DEC07

**decision**

Prioriser entre demandes de vente

**realisation**

Politique GBM : ordre d’arrivée

**reserve**

File et périmètre de protection non définis

**contexte**

Ventes GBM

**source**

U10

## DEC08

**id**

DEC08

**decision**

Reprioriser pour un client Gold

**realisation**

Non exercé dans le fonctionnement GBM décrit

**reserve**

Ne pas inventer fonction équivalente à ARun

**contexte**

Ventes GBM

**source**

U10

## DEC09

**id**

DEC09

**decision**

Exclure définitivement un mauvais payeur

**realisation**

Acteur/application non établis

**reserve**

Avant exclusion, traitement identique ; procédure externe non décrite

**contexte**

B2B / frontière

**source**

U10

## DEC10

**id**

DEC10

**decision**

Rechercher d’abord une solution entrepôt

**realisation**

Chaîne commerce non localisée précisément

**reserve**

Le stock est présent dans UR ; calculateur exact inconnu

**contexte**

eCommerce

**source**

U04

## DEC11

**id**

DEC11

**decision**

Déterminer les magasins éligibles

**realisation**

Chaîne SFS non localisée précisément

**reserve**

Stock + participation + quota

**contexte**

eCommerce/SFS

**source**

U04

## DEC12

**id**

DEC12

**decision**

Classer les magasins

**realisation**

Chaîne SFS non localisée précisément

**reserve**

Moins sollicité ; métrique inconnue

**contexte**

eCommerce/SFS

**source**

U04

## DEC13

**id**

DEC13

**decision**

Accepter la préparation/expédition

**realisation**

Magasin sollicité

**reserve**

Rôle humain et application exacts non fournis

**contexte**

SFS

**source**

U04

## DEC14

**id**

DEC14

**decision**

Annuler tentative et solliciter suivant

**realisation**

Chaîne SFS

**reserve**

Refus ou 15 minutes ; aucune annulation vente

**contexte**

SFS

**source**

U04;U05

## DEC15

**id**

DEC15

**decision**

Débloquer la situation par intervention

**realisation**

Responsable commercial marque

**reserve**

Appelle magasins ; pouvoirs non détaillés

**contexte**

SFS exception

**source**

U04

## DEC16

**id**

DEC16

**decision**

Choisir l’entrepôt

**realisation**

OMS C-Log / Crossroad

**reserve**

Aptitudes opérationnelles ; autres critères non fournis

**contexte**

Logistique externalisée au cœur

**source**

U04;U06;U07

## DEC17

**id**

DEC17

**decision**

Ajouter un transfert préalable

**realisation**

OMS C-Log / Crossroad dans le récit

**reserve**

Condition exacte et émission des ordres non détaillées

**contexte**

Logistique

**source**

U06;U07

## DEC18

**id**

DEC18

**decision**

Choisir le transporteur

**realisation**

OMS C-Log / Crossroad

**reserve**

Règles, offres et coût non décrits

**contexte**

Shipping

**source**

U04;U06

## DEC19

**id**

DEC19

**decision**

Reprendre une demande en erreur

**realisation**

Intervenant C-Log non identifié

**reserve**

File d’erreur ; reprise manuelle

**contexte**

Logistique exception

**source**

U06

## DEC20

**id**

DEC20

**decision**

Réserver/libérer stock ou quota

**realisation**

Non établi

**reserve**

À distinguer du choix et de l’acceptation

**contexte**

Transverse

**source**

P32;P34;Q017;Q018

## DEC21

**id**

DEC21

**decision**

Autoriser une promesse fondée sur une ressource future

**realisation**

Besoin explicitement exprimé par Laurent ; acteur et réalisation installée non établis.

**reserve**

Règles, périmètre d’autorité et limites de révision à préciser en Q068 ; ne s’applique pas automatiquement à GBM.

**contexte**

Ventes Boardriders

**source**

U30 ; F120 ; P68 ; 2026-09-09.

## DEC22

**id**

DEC22

**decision**

Réviser des engagements au profit d’une demande prioritaire

**realisation**

Besoin explicitement exprimé par Laurent ; acteur et réalisation installée non établis.

**reserve**

Règles, périmètre d’autorité et limites de révision à préciser en Q068 ; ne s’applique pas automatiquement à GBM.

**contexte**

Arbitrages Boardriders, exemple client Gold

**source**

U30 ; F120 ; P68 ; 2026-09-09.

## Frontière des décisions et des référentiels — U97/U98

Les autorités externes [INF18–INF20](10-autorites-information.md#inf18) portent les données de référence Party / Role, Agreement et Catalog. Les trois domaines de la plateforme ont seulement une capacité d’ingestion. Leur administration, vérification et parcours d’enregistrement ne constituent pas des responsabilités de décision à implémenter dans cette carte.

Order Promising utilise les conditions particulières reçues pour ses décisions validées U95. D04 reste à examiner pour les engagements propres aux commandes, distincts des Agreements. Appliquer une condition à une transaction n’est pas vérifier ou modifier la donnée de référence ; le domaine consommateur possède sa décision. L’identité de l’autorité opérationnelle reste à préciser par situation. Aucun DEC existant ni déploiement maître n’est réputé validé par cette orientation.

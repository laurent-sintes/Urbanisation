# Flux décrits

**Statut documentaire après U106–U112 (13 septembre 2026) :** registre source de la migration, conservé pour sa provenance. Les modèles de l’existant font désormais autorité dans [panorama-as-is](../modeles/panorama-as-is/current.json). Les besoins, orientations de cible et mentions non instruits sont séparés dans le [backlog](../modeles/backlog/panorama-candidates.json). Enrichir ensuite les JSON et les sources narratives utiles, sans entretenir deux inventaires concurrents ; voir [C70](04-corrections.md#c70).

Import initial : [référentiel JSON archivé](../archive/referentiel.json), section `flux`, consolidation du 9 septembre 2026. Les statuts et réserves ci-dessous sont ceux de la source.

## FL01

**id**

FL01

**origine**

APP-STR

**destination**

APP-UR

**contenu**

Représentations de stocks magasin par marque

**modalite**

Batch régulier

**source**

U03

**statut**

Décrit

**reserve**

Fréquence, fraîcheur et reprise inconnues.

## FL02

**id**

FL02

**origine**

APP-UR

**destination**

SI C-Log

**contenu**

Alignement de données

**modalite**

Batch

**source**

U03

**statut**

Décrit

**reserve**

Objets et sens de chaque message non précisés ; échanges bilatéraux décrits globalement.

## FL03

**id**

FL03

**origine**

APP-IRM

**destination**

APP-STR

**contenu**

Seuils minimum utilisés pour le réassort

**modalite**

Mécanisme non documenté

**source**

U06

**statut**

Dépendance fonctionnelle établie

**reserve**

Ne pas dessiner une interface directe comme preuve.

## FL04

**id**

FL04

**origine**

APP-WEB

**destination**

Fonction disponibilité / UR

**contenu**

Recherche prioritaire d’un stock entrepôt

**modalite**

Interface non documentée

**source**

U04

**statut**

Parcours décrit

**reserve**

Appelant/cible technique exacts inconnus.

## FL05

**id**

FL05

**origine**

Commerce GBM

**destination**

SI C-Log

**contenu**

Demande d’exécution logistique : origine, articles, destinataire, opérations

**modalite**

Fichier EDI

**source**

U06

**statut**

Décrit

**reserve**

Système émetteur exact selon chaque origine non fourni.

## FL06

**id**

FL06

**origine**

Chaîne SFS (Socloz contribue)

**destination**

Magasin sélectionné

**contenu**

Demande de préparation/expédition

**modalite**

Interface non documentée

**source**

U03;U04

**statut**

Décrit au niveau métier

**reserve**

Ne pas assigner toutes les décisions à Socloz.

## FL07

**id**

FL07

**origine**

Magasin sollicité

**destination**

Chaîne SFS

**contenu**

Acceptation, refus ou absence de réponse

**modalite**

Délai 15 minutes

**source**

U04

**statut**

Décrit

**reserve**

Événements et stockage techniques non fournis.

## FL08

**id**

FL08

**origine**

Chaîne SFS

**destination**

Magasin suivant

**contenu**

Nouvelle demande après annulation de tentative

**modalite**

Séquentiel décrit

**source**

U04;U05

**statut**

Décrit

**reserve**

Commande client inchangée dans son existence.

## FL09

**id**

FL09

**origine**

Chaîne SFS

**destination**

Responsable commercial marque

**contenu**

Alerte de non-prise en charge

**modalite**

Dans la journée : incertain

**source**

U04

**statut**

Décrit avec réserve

**reserve**

Règle de déclenchement exacte inconnue.

## FL10

**id**

FL10

**origine**

Responsable commercial marque

**destination**

Magasins

**contenu**

Appels pour débloquer la situation

**modalite**

Humain / téléphone

**source**

U04

**statut**

Décrit

**reserve**

Pouvoirs d’arbitrage non établis.

## FL11

**id**

FL11

**origine**

APP-STR

**destination**

Processus d’approvisionnement / C-Log

**contenu**

Demande automatique de réassort

**modalite**

Déclenchement sur seuil ; route exacte non précisée

**source**

U06

**statut**

Décrit fonctionnellement

**reserve**

Ne pas inventer passage obligatoire par UR.

## FL12

**id**

FL12

**origine**

APP-XRD

**destination**

Entrepôt(s)

**contenu**

Exécution du parcours et transfert éventuel

**modalite**

Mécanisme non documenté

**source**

U06

**statut**

Décrit au niveau métier

**reserve**

Outils WMS et interfaces non inventoriés.

## FL13

**id**

FL13

**origine**

APP-XRD

**destination**

Transport / transporteur

**contenu**

Choix et organisation du shipping

**modalite**

Mécanisme non documenté

**source**

U06

**statut**

Choix décrit

**reserve**

Messages et engagement transport non décrits.

## FL14

**id**

FL14

**origine**

APP-XRD

**destination**

File d’erreur / intervenants

**contenu**

Demande problématique à reprendre

**modalite**

Mise en file puis traitement manuel

**source**

U06

**statut**

Décrit

**reserve**

Responsables de reprise et retours commerce inconnus.

## FL15

**id**

FL15

**origine**

APP-MAP

**destination**

SI C-Log

**contenu**

Anticipation du stockage

**modalite**

Mécanisme non documenté

**source**

U10

**statut**

Décrit

**reserve**

Contenu, granularité, fréquence et engagement associés inconnus.

## FL16

**id**

FL16

**origine**

APP-MAP

**destination**

Système opérant non nommé

**contenu**

Jeux de données recalculés après aléa amont

**modalite**

Annule et remplace

**source**

U10

**statut**

Décrit

**reserve**

Consommateurs et conséquences sur engagements non identifiés.

## FL17

**id**

FL17

**origine**

APP-MAP

**destination**

Processus achats / fournisseur

**contenu**

Demande d’achat fournisseur ; U48 précise « Planned Purchase Order » pour le cas de fabrication complète par le fournisseur.

**modalite**

Mécanisme non documenté

**source**

U10 ; U48 ; F141

**statut**

Responsabilité décrite

**reserve**

Émission directe au fournisseur et commande ferme non prouvées.

## FL18

**id**

FL18

**origine**

Fournisseur / échanges amont

**destination**

APP-CBS

**contenu**

Éléments de suivi fabrication/livraison/documents

**modalite**

Mécanisme non documenté

**source**

U03;U10

**statut**

Responsabilité décrite

**reserve**

Ne pas prouver un flux CBS–MAP à partir de cette seule dépendance métier.

## FL19

**id**

FL19

**origine**

APP-CBS / processus achats

**destination**

Beaumanoir et acteurs douaniers

**contenu**

Documents / suivi opérationnel douane

**modalite**

Mécanisme non documenté

**source**

U03;U10

**statut**

À rapprocher

**reserve**

Identité avec application achats initiale non confirmée.

## FL20

**id**

FL20

**origine**

Client B2B

**destination**

APP-ELA

**contenu**

Prise de commande

**modalite**

Application B2B

**source**

U03

**statut**

Décrit

**reserve**

Zoho→Elastic ou Elastic→C-Log non attestés dans le fil.

## FL21

**id**

FL21

**origine**

Fournisseurs Sarenza

**destination**

SI-SAR

**contenu**

Catalogues articles constitués

**modalite**

Mécanisme non documenté

**source**

U02

**statut**

Décrit

**reserve**

Référentiel maître et rapprochements non détaillés.

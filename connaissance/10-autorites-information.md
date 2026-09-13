# Autorités sur les informations

**Statut documentaire après U106–U112 (13 septembre 2026) :** registre source de la migration, conservé pour sa provenance. Les modèles de l’existant font désormais autorité dans [panorama-as-is](../modeles/panorama-as-is/current.json). Les besoins, orientations de cible et mentions non instruits sont séparés dans le [backlog](../modeles/backlog/panorama-candidates.json). Enrichir ensuite les JSON et les sources narratives utiles, sans entretenir deux inventaires concurrents ; voir [C70](04-corrections.md#c70).

Import initial : [référentiel JSON archivé](../archive/referentiel.json), section `autorites_information`, consolidation du 9 septembre 2026. Les statuts et réserves ci-dessous sont ceux de la source.

## INF01

**id**

INF01

**objet**

Stock magasin

**autorite_ou_producteur**

Storeland par marque

**autres_contributions**

UR reçoit une copie batch

**reserve**

Autorité de tenue déclarée ; états détaillés inconnus

**source**

U03;U04

## INF02

**id**

INF02

**objet**

Stock entrepôt physique/logique

**autorite_ou_producteur**

Non établi

**autres_contributions**

UR contient une représentation ; SI C-Log réalise la logistique

**reserve**

Présence ≠ autorité

**source**

U04;U06

## INF03

**id**

INF03

**objet**

Disponibilité proposée à la vente

**autorite_ou_producteur**

Non établi

**autres_contributions**

Recherche entrepôt puis magasin décrite

**reserve**

Calcul/règle/engagement à séparer

**source**

U04;U10

## INF04

**id**

INF04

**objet**

Stocks optimaux et seuils réassort

**autorite_ou_producteur**

IRMA déclaré référence des seuils

**autres_contributions**

Storeland applique le déclenchement

**reserve**

Transition SCORTEX à dater par périmètre

**source**

U06

## INF05

**id**

INF05

**objet**

Protections marque/canal

**autorite_ou_producteur**

MAP calcule

**autres_contributions**

Système(s) opérant(s) consommateur(s) non nommés

**reserve**

Autorité applicable et versions inconnues

**source**

U10

## INF06

**id**

INF06

**objet**

Prévisions de vente

**autorite_ou_producteur**

MAP produit

**autres_contributions**

Consommateurs et versions non détaillés

**reserve**

Pas de maître opérationnel inventé

**source**

U10

## INF07

**id**

INF07

**objet**

Anticipations de stockage

**autorite_ou_producteur**

MAP produit

**autres_contributions**

C-Log reçoit

**reserve**

Résultat décisionnel accepté/ajusté non documenté

**source**

U10

## INF08

**id**

INF08

**objet**

Quotas et charge magasin

**autorite_ou_producteur**

Non établi

**autres_contributions**

Chaîne SFS utilise la contrainte

**reserve**

Auteur, compteur et persistance inconnus

**source**

U04

## INF09

**id**

INF09

**objet**

Aptitudes des entrepôts

**autorite_ou_producteur**

Non établi

**autres_contributions**

Crossroad utilise les opérations réalisables

**reserve**

Référentiel implicite, source inconnue

**source**

U06

## INF10

**id**

INF10

**objet**

Commande client

**autorite_ou_producteur**

Non établi

**autres_contributions**

POS/sites/Elastic contribuent ; commande maintenue pendant reprises SFS

**reserve**

Ne pas déduire maître de la seule saisie

**source**

U03-U05

## INF11

**id**

INF11

**objet**

Demande d’exécution magasin

**autorite_ou_producteur**

Non établi

**autres_contributions**

Chaîne SFS ; Socloz contribue

**reserve**

Cycle distinct de commande ; systèmes exacts inconnus

**source**

U03-U05

## INF12

**id**

INF12

**objet**

Demande d’exécution logistique

**autorite_ou_producteur**

Émetteur non établi par parcours

**autres_contributions**

EDI commerce→C-Log

**reserve**

Origine du besoin et statut logistique peuvent relever de responsabilités différentes

**source**

U06

## INF13

**id**

INF13

**objet**

Parcours et état logistique

**autorite_ou_producteur**

Crossroad suit le processus

**autres_contributions**

Équipes/outils de réalisation non inventoriés

**reserve**

Autorité du suivi décrit ; autorité de chaque fait physique non prouvée

**source**

U06;U07

## INF14

**id**

INF14

**objet**

Demande d’achat fournisseur

**autorite_ou_producteur**

MAP réalise la demande

**autres_contributions**

CBS suit fabrication/livraison amont

**reserve**

Référentiel commande ferme non établi

**source**

U10

## INF15

**id**

INF15

**objet**

Faits et pièces amont

**autorite_ou_producteur**

CBS suit

**autres_contributions**

Application achats initiale à rapprocher

**reserve**

Suivre ne signifie pas faire autorité sur toute pièce émise par fournisseur/douane

**source**

U03;U10

## INF16

**id**

INF16

**objet**

Clients B2B

**autorite_ou_producteur**

Zoho assure CRM

**autres_contributions**

Elastic capte les commandes

**reserve**

Autorité par attribut/exclusion non établie

**source**

U03;U10

## INF17

**id**

INF17

**objet**

Articles fournisseurs Sarenza

**autorite_ou_producteur**

Fournisseurs apportent catalogues

**autres_contributions**

Sarenza intègre les articles

**reserve**

Autorité locale et rapprochement non documentés

**source**

U02

## INF18

**id**

INF18

**objet**

Party / Role — identités, rôles et relations de référence

**autorite_ou_producteur**

Référentiel externe Party / Role ; identité sans doublon sous sa responsabilité selon U97.

**autres_contributions**

Applications CRM/SRM pour les références clients/fournisseurs ; plateforme consommatrice par D09.d.

**reserve**

Répartition des contributions et autorité par attribut à préciser ; aucun maître logiciel installé ni qualité constatée déduits. Les rôles métier sont distincts des habilitations RBAC.

**source**

U97/U98 ; F203–F208 ; C64/P85 ; orientation de plateforme déclarée le 2026-09-11, distincte des constats de déploiement.

## INF19

**id**

INF19

**objet**

Agreement — contrats clients/fournisseurs de référence

**autorite_ou_producteur**

Applications maîtres externes ; CRM/SRM cités par Laurent selon le contexte client/fournisseur.

**autres_contributions**

D11.a reçoit contrats, liens Party/Catalog et conditions particulières utilisées notamment par Order Promising.

**reserve**

Commandes distinctes selon U98. La maîtrise de leurs engagements transactionnels reste à examiner ; aucune application ou cardinalité technique arrêtée.

**source**

U97/U98 ; F203–F208 ; C64/P85 ; orientation de plateforme déclarée le 2026-09-11, distincte des constats de déploiement.

## INF20

**id**

INF20

**objet**

Catalog — catalogues, prix et zones géographiques d’application

**autorite_ou_producteur**

Applications externes de construction des catalogues.

**autres_contributions**

D12.a reçoit les catalogues et leurs évolutions, reliés aux Agreements par identifiants.

**reserve**

Source nommée, gestion des versions et autorité par attribut non établies. L’articulation avec les références articles, unités et conditionnements reste à préciser ; Catalog ne désigne pas automatiquement tout le PIM.

**source**

U97/U98 ; F203–F208 ; C64/P85 ; orientation de plateforme déclarée le 2026-09-11, distincte des constats de déploiement.

**Audit U99 :** INF18–INF20 restent les orientations de maîtrise externe. Q071/Q072 ouvrent la réception des références produit et les autorités du prix appliqué et du consommé contractuel ; aucune maîtrise installée supplémentaire n’est déduite. [Audit](../audits/2026-09-11-modele-marche-achats-ventes-referentiels.md).

## INF21

**id**

INF21

**objet**

Product Reference — article et identité SKU

**autorite_ou_producteur**

Référentiel article autonome par rapport aux catalogues, selon U100 ; application maîtresse non identifiée.

**autres_contributions**

D08.d reçoit les références article ; D12 reçoit les catalogues qui peuvent proposer les mêmes SKU. Réemploi par identifiants sans schéma détaillé imposé.

**reserve**

Maîtrise externe et ingestion seule appliquées dans la continuité U97. U100 confirme l’autonomie, sans nommer le maître ni préciser attributs, unités, conversions et versions. Aucune déduction de configuration installée.

**source**

U100/F212 ; U97 ; A71/C66 ; 2026-09-11.

## INF22

**id**

INF22

**objet**

Fulfillment Network — lieux et relations du réseau utiles à la Supply

**autorite_ou_producteur**

Maître non identifié par Laurent. Réception externe proposée dans la continuité U97 ; ne pas présumer un maître unique ni attribuer l’ensemble à C-Log.

**autres_contributions**

D13.a reçoit les références du réseau ; Party / Role fournit les identités responsables. D06 et D03 utilisent ces références pour apprécier les possibilités et décider ; D07 contribue les engagements et faits de réalisation.

**reserve**

Topologie, granularité, prestataires, calendriers, délais et règles de validité à éprouver. Autonomie C-Log et frontières FLOW préservées ; données d’un lieu tiers à distinguer des seuls nœuds maîtrisés du réseau.

**source**

U102/F214 pour l’orientation ; U97/U58 pour les limites ; A73/C68 pour les propositions, 2026-09-11.

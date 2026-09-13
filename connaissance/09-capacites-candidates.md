# Capacités candidates

**Statut documentaire après migration (13 septembre 2026) :** les 36 CAP historiques sont conservées dans leur [inventaire JSON de provenance](../modeles/backlog/legacy-capabilities.json). Elles ne sont pas les 36 capacités P81 de la [release courante](../modeles/release/current.json). Ce registre reste une source historique, sans bijection présumée.

Import initial : [référentiel JSON archivé](../archive/referentiel.json), section `capacites_candidates`, consolidation du 9 septembre 2026. Les entrées importées conservent leur provenance ; les compléments et corrections d’audit sont datés et sourcés.

La [vue du socle transactionnel](16-capacites-socle-transactionnel.md) propose une lecture prioritaire de ce catalogue à la suite de U21. Le catalogue global contient aussi des responsabilités de processus, d’amont et de C-Log ; ses 36 entrées ne sont pas toutes des capacités du socle. Les rattachements de la vue sont exploratoires et ne modifient pas les définitions ci-dessous.

Complément marché du 2026-09-09, U22/U23 : [analyse SAP-stock](../marche/sap-stock.md), CMP013–CMP017. Appuis sémantiques pour CAP004/CAP005/CAP006/CAP010 et CAP007/CAP008/CAP009/CAP035 ; aucune définition ni autorité modifiée. Inventaire physique à explorer en P64/Q065.

L’[exploration U26/U27 du bloc stock](17-exploration-bloc-stock.md) poursuit cette analyse avec P66/Q066/CMP020, sans modifier les CAP.

Le [glossaire métier](19-glossaire-metier.md), amorcé après U33–U35, précise la définition de capacité et propose un vocabulaire commun pour relire les candidats. Les libellés historiques contenant tenir sont à réexaminer ; aucun renommage ni changement des définitions n’est appliqué ici.

## CAP001

**id**

CAP001

**intitule**

Tenir le référentiel opérationnel des articles

**regroupement_de_travail**

Référentiels

**resultat**

Articles achetables/vendables/stockables, grain SKU.

**statut_perimetre**

Administration et qualification du référentiel article exclues de la vue plateforme après U97. Référence article autonome confirmée U100 : réception proposée D08.d, réemploi des mêmes SKU par plusieurs catalogues D12. Sources et attributs restent à préciser ; administration et qualification non restaurées.

**realisation_decrite**

À inventorier

**source**

U01;U02;U06;P29

**statut**

Fiche historique conservée ; périmètre de plateforme corrigé par U97/U98, C64. Ne pas lire le titre importé comme une capacité d’administration à développer.

**correction_2026_09_11**

U97/U98, C64 : ancien statut de périmètre « Dans le périmètre » ; ancien statut « Candidat de travail ; hiérarchie non validée ». Intitulé et résultat importés conservés comme provenance ; portée courante précisée ci-dessus.

## CAP002

**id**

CAP002

**intitule**

Tenir les référentiels des partenaires et lieux

**regroupement_de_travail**

Référentiels

**resultat**

Fournisseurs, clients B2B, magasins, entrepôts ; responsabilités à qualifier.

**statut_perimetre**

Administration et qualification des parties exclues de la vue plateforme après U97 ; ingestion D09.d. Les références des lieux et du réseau sont reçues en D13.a après U102 ; D06 apprécie les possibilités d’exécution à partir de ces références. Autorités ouvertes INF22/Q076.

**realisation_decrite**

Zoho contribue au CRM ; autorité non établie

**source**

U01;U03;P29

**statut**

Fiche historique conservée ; périmètre de plateforme corrigé par U97/U98, C64. Ne pas lire le titre importé comme une capacité d’administration à développer.

**correction_2026_09_11**

U97/U98, C64 : ancien statut de périmètre « Dans le périmètre » ; ancien statut « Candidat de travail ; hiérarchie non validée ». Intitulé et résultat importés conservés comme provenance ; portée courante précisée ci-dessus.

## CAP003

**id**

CAP003

**intitule**

Tenir les conditions commerciales applicables

**regroupement_de_travail**

Référentiels

**resultat**

Prix et conditions utiles aux opérations, frontière à préciser.

**statut_perimetre**

Administration des conditions et prix de référence exclue de la vue plateforme après U97 ; ingestion Agreement D11.a et Catalog D12.a. Leur application aux transactions reste à attribuer aux domaines consommateurs.

**realisation_decrite**

À inventorier

**source**

P29;P53

**statut**

Fiche historique conservée ; périmètre de plateforme corrigé par U97/U98, C64. Ne pas lire le titre importé comme une capacité d’administration à développer.

**correction_2026_09_11**

U97/U98, C64 : ancien statut de périmètre « Dans le périmètre à délimiter » ; ancien statut « Candidat de travail ; hiérarchie non validée ». Intitulé et résultat importés conservés comme provenance ; portée courante précisée ci-dessus.

## CAP004

**id**

CAP004

**intitule**

Tenir les états du stock magasin

**regroupement_de_travail**

Stock

**resultat**

État et mouvements dont le magasin/la marque répond.

**statut_perimetre**

Dans le périmètre

**realisation_decrite**

Storeland

**source**

U03;U04

**statut**

Candidat de travail ; hiérarchie non validée

## CAP005

**id**

CAP005

**intitule**

Rendre les stocks visibles

**regroupement_de_travail**

Stock

**resultat**

Partager une représentation du stock avec sa provenance et fraîcheur.

**statut_perimetre**

Dans le périmètre

**realisation_decrite**

Storeland/UR/Talend contribuent

**source**

U03;P27

**statut**

Candidat de travail ; hiérarchie non validée

## CAP006

**id**

CAP006

**intitule**

Déterminer la disponibilité utilisable

**regroupement_de_travail**

Stock

**resultat**

Calculer ce qui peut être proposé compte tenu des états et contraintes.

**statut_perimetre**

Dans le périmètre

**realisation_decrite**

Répartition à établir

**source**

U04;U10;P27;U30

**statut**

Candidat de travail ; hiérarchie non validée

**complement_2026_09_09**

U30 : le besoin BRD inclut des ressources présentes et futures admissibles ; politique et horizon à définir. La formule GBM et les autorités restent inconnues. [Analyse et CMP022/CMP023](18-politiques-engagement-gbm-brd.md).

## CAP007

**id**

CAP007

**intitule**

Définir les protections de stock

**regroupement_de_travail**

Allocation

**resultat**

Définir seuils/volumes logiques par marque et canal.

**statut_perimetre**

Frontière planification/opération à positionner

**realisation_decrite**

MAP calcule ; application opérationnelle inconnue

**source**

U10

**statut**

Candidat de travail ; hiérarchie non validée

## CAP008

**id**

CAP008

**intitule**

Tenir les protections applicables

**regroupement_de_travail**

Allocation

**resultat**

Porter la version de politique effectivement en vigueur.

**statut_perimetre**

Candidat analytique nouveau à valider

**realisation_decrite**

Autorité non établie

**source**

U07;U09;U10;P50

**statut**

Candidat de travail ; hiérarchie non validée

## CAP009

**id**

CAP009

**intitule**

Réviser les paramètres d’allocation

**regroupement_de_travail**

Allocation

**resultat**

Recalculer après aléa amont et republier une nouvelle politique.

**statut_perimetre**

Frontière à positionner

**realisation_decrite**

MAP

**source**

U10

**statut**

Candidat de travail ; hiérarchie non validée

## CAP010

**id**

CAP010

**intitule**

Gérer les engagements sur le stock

**regroupement_de_travail**

Stock / engagements

**resultat**

Réserver, affecter, confirmer et libérer les quantités.

**statut_perimetre**

Dans le périmètre

**realisation_decrite**

Répartition à établir

**source**

P27;P45;U30

**statut**

Candidat de travail ; hiérarchie non validée

**complement_2026_09_09**

U30 : réservation GBM au passage de commande au niveau métier ; BRD doit couvrir les comportements d’engagement présents/futurs et de révision cités. Q018/Q049/Q068 conservent les limites de connaissance. [Analyse et CMP022/CMP023](18-politiques-engagement-gbm-brd.md).

## CAP011

**id**

CAP011

**intitule**

Déterminer les paramètres de réassort

**regroupement_de_travail**

Réassort

**resultat**

Calculer stocks optimaux et seuils magasin.

**statut_perimetre**

Inclusion opérationnelle proposée

**realisation_decrite**

IRMA ; transition SCORTEX

**source**

U06;P37

**statut**

Candidat de travail ; hiérarchie non validée

## CAP012

**id**

CAP012

**intitule**

Tenir les paramètres de réassort applicables

**regroupement_de_travail**

Réassort

**resultat**

Conserver seuils de référence et périmètre/validité.

**statut_perimetre**

Dans le périmètre proposé

**realisation_decrite**

IRMA déclaré référence

**source**

U06;P48

**statut**

Candidat de travail ; hiérarchie non validée

## CAP013

**id**

CAP013

**intitule**

Déclencher l’approvisionnement magasin

**regroupement_de_travail**

Réassort

**resultat**

Détecter le seuil et lancer une demande.

**statut_perimetre**

Dans le périmètre

**realisation_decrite**

Storeland

**source**

U06

**statut**

Candidat de travail ; hiérarchie non validée

## CAP014

**id**

CAP014

**intitule**

Prendre en charge les commandes clients

**regroupement_de_travail**

Ventes

**resultat**

Saisir et maintenir les engagements commerciaux, indépendamment des tentatives d’exécution.

**statut_perimetre**

Dans le périmètre

**realisation_decrite**

POS/sites/Elastic ; autorité à établir

**source**

U03-U05;U30

**statut**

Candidat de travail ; hiérarchie non validée

**complement_2026_09_09**

U30 : BRD doit pouvoir prendre en charge les demandes décrites malgré une insuffisance de disponible immédiat. Séparer enregistrement de commande, confirmation quantité/date et affectation ; règles et réalisation à préciser. [Analyse et CMP022/CMP023](18-politiques-engagement-gbm-brd.md).

## CAP015

**id**

CAP015

**intitule**

Qualifier les services rendus par les sites

**regroupement_de_travail**

Exécution commerciale

**resultat**

Participation SFS et aptitude des sites aux prestations.

**statut_perimetre**

Commerce + frontière logistique

**realisation_decrite**

Référentiels à identifier

**source**

U04;U06;P42

**statut**

Candidat de travail ; hiérarchie non validée

## CAP016

**id**

CAP016

**intitule**

Gérer la charge et les quotas d’exécution

**regroupement_de_travail**

Exécution commerciale

**resultat**

Définir/appliquer quotas et disponibilité de service.

**statut_perimetre**

Dans le périmètre proposé

**realisation_decrite**

Magasins ; responsables/applications non établis

**source**

U04;P34

**statut**

Candidat de travail ; hiérarchie non validée

## CAP017

**id**

CAP017

**intitule**

Choisir l’origine de prise en charge

**regroupement_de_travail**

Exécution commerciale

**resultat**

Prioriser entrepôt/magasin et classer les candidats.

**statut_perimetre**

Frontière de décision centrale à explorer

**realisation_decrite**

Chaîne commerce + choix C-Log

**source**

U04;U07

**statut**

Candidat de travail ; hiérarchie non validée

## CAP018

**id**

CAP018

**intitule**

Gérer les demandes d’exécution magasin

**regroupement_de_travail**

Exécution commerciale

**resultat**

Solliciter, accepter, refuser, expirer, annuler et reprendre.

**statut_perimetre**

Dans le périmètre

**realisation_decrite**

Socloz contribue ; répartition détaillée inconnue

**source**

U03-U05

**statut**

Candidat de travail ; hiérarchie non validée

## CAP019

**id**

CAP019

**intitule**

Piloter la résolution d’une non-prise en charge

**regroupement_de_travail**

Situations

**resultat**

Alerter et coordonner les actions humaines.

**statut_perimetre**

Dans le périmètre

**realisation_decrite**

Responsable commercial + chaîne SFS

**source**

U04;P35

**statut**

Candidat de travail ; hiérarchie non validée

## CAP020

**id**

CAP020

**intitule**

Demander une prestation logistique

**regroupement_de_travail**

Interface commerce-logistique

**resultat**

Exprimer articles, destinataire, finalité et prestations requises.

**statut_perimetre**

Interface au périmètre

**realisation_decrite**

EDI vers C-Log

**source**

U06;P38

**statut**

Candidat de travail ; hiérarchie non validée

## CAP021

**id**

CAP021

**intitule**

Déterminer le parcours logistique

**regroupement_de_travail**

C-Log

**resultat**

Choisir entrepôt(s), éventuellement transfert préalable.

**statut_perimetre**

Externe : frontière, pas absorption

**realisation_decrite**

Crossroad/KBRW

**source**

U06;U07

**statut**

Candidat de travail ; hiérarchie non validée

## CAP022

**id**

CAP022

**intitule**

Organiser le transport aval

**regroupement_de_travail**

C-Log

**resultat**

Choisir transporteur et acheminement.

**statut_perimetre**

Externe : frontière

**realisation_decrite**

Crossroad pour choix décrit

**source**

U04;U06;U07

**statut**

Candidat de travail ; hiérarchie non validée

## CAP023

**id**

CAP023

**intitule**

Piloter l’exécution logistique

**regroupement_de_travail**

C-Log

**resultat**

Suivre opérations et résultats du parcours.

**statut_perimetre**

Externe : frontière

**realisation_decrite**

Crossroad

**source**

U06;U07

**statut**

Candidat de travail ; hiérarchie non validée

## CAP024

**id**

CAP024

**intitule**

Réaliser préparation et prestations entrepôt

**regroupement_de_travail**

C-Log

**resultat**

Picking, light-touch, packing, shipping.

**statut_perimetre**

Externe : ne pas détailler le SI C-Log

**realisation_decrite**

Équipes/sites et outils non inventoriés

**source**

U06;U07

**statut**

Candidat de travail ; hiérarchie non validée

## CAP025

**id**

CAP025

**intitule**

Résoudre un incident logistique

**regroupement_de_travail**

C-Log / interface

**resultat**

Reprendre une demande en échec et informer les parties.

**statut_perimetre**

Frontière

**realisation_decrite**

File d’erreur puis intervenants

**source**

U06

**statut**

Candidat de travail ; hiérarchie non validée

## CAP026

**id**

CAP026

**intitule**

Prévoir les ventes

**regroupement_de_travail**

Planification

**resultat**

Prévisions marque/modèle/couleur/taille et canal.

**statut_perimetre**

Contexte amont ; hors refonte implicite

**realisation_decrite**

MAP

**source**

U01;U10

**statut**

Candidat de travail ; hiérarchie non validée

## CAP027

**id**

CAP027

**intitule**

Anticiper les besoins de stockage

**regroupement_de_travail**

Planification / logistique

**resultat**

Préparer les besoins de stockage transmis à C-Log.

**statut_perimetre**

Contexte/interface à positionner

**realisation_decrite**

MAP

**source**

U10

**statut**

Candidat de travail ; hiérarchie non validée

## CAP028

**id**

CAP028

**intitule**

Planifier et lotir les besoins d’achat

**regroupement_de_travail**

Planification / achats

**resultat**

Organiser les demandes fournisseurs et lotissements.

**statut_perimetre**

Frontière amont/opération

**realisation_decrite**

MAP

**source**

U10

**statut**

Candidat de travail ; hiérarchie non validée

## CAP029

**id**

CAP029

**intitule**

Émettre une demande d’achat fournisseur

**regroupement_de_travail**

Achats

**resultat**

Produire la demande ; engagement ferme distinct à instruire.

**statut_perimetre**

Dans le périmètre opérationnel à qualifier

**realisation_decrite**

MAP. U48 précise l’émission de « Planned Purchase Order » dans le cas de fabrication complète par le fournisseur ; portée d’engagement et destinataire non établis (Q034).

**source**

U10 ; U48 ; F141

**statut**

Candidat de travail ; hiérarchie non validée

## CAP030

**id**

CAP030

**intitule**

Suivre la réalisation fournisseur

**regroupement_de_travail**

Achats

**resultat**

Suivi fabrication et progression opérationnelle.

**statut_perimetre**

Dans le périmètre proposé

**realisation_decrite**

CBS

**source**

U10

**statut**

Candidat de travail ; hiérarchie non validée

## CAP031

**id**

CAP031

**intitule**

Suivre l’acheminement fournisseur

**regroupement_de_travail**

Achats / logistique amont

**resultat**

Suivi fournisseur–port/Carrier.

**statut_perimetre**

Frontière à délimiter

**realisation_decrite**

CBS

**source**

U10

**statut**

Candidat de travail ; hiérarchie non validée

## CAP032

**id**

CAP032

**intitule**

Suivre les pièces nécessaires aux opérations

**regroupement_de_travail**

Achats

**resultat**

Collecter/transmettre/relancer les pièces et états requis.

**statut_perimetre**

Opérationnel proposé ; politique conformité exclue

**realisation_decrite**

Application achats initiale ; CBS à rapprocher

**source**

U03;U10;P30

**statut**

Candidat de travail ; hiérarchie non validée

## CAP033

**id**

CAP033

**intitule**

Prendre en charge le SAV

**regroupement_de_travail**

Après-vente

**resultat**

Recevoir réclamation, suivre objectif et décisions.

**statut_perimetre**

Dans le périmètre

**realisation_decrite**

Force Sarenza ; détail non décrit

**source**

U01;U02;P25

**statut**

Candidat de travail ; hiérarchie non validée

## CAP034

**id**

CAP034

**intitule**

Autoriser et traiter retour ou échange

**regroupement_de_travail**

Après-vente

**resultat**

Décider solution commerciale puis effets physiques, sans absorber exécution financière.

**statut_perimetre**

Dans le périmètre à qualifier

**realisation_decrite**

À inventorier

**source**

U01;P25;P53

**statut**

Candidat de travail ; hiérarchie non validée

## CAP035

**id**

CAP035

**intitule**

Arbitrer les demandes sous contrainte

**regroupement_de_travail**

Allocation / ventes

**resultat**

Décider d’une priorité ou d’une réaffectation dans un contexte admissible.

**statut_perimetre**

Candidat transverse, non actif comme repriorisation Gold dans GBM

**realisation_decrite**

GBM FIFO ; besoin BRD de réaffectation prioritaire déclaré en U30, réalisation à explorer

**source**

U02;U10;P54;P55;U30;U31

**statut**

Candidat de travail ; hiérarchie non validée

**complement_2026_09_09**

U30 établit le besoin BRD de réaffectation prioritaire ; U31/P69 propose de rattacher la révision des promesses à Order Promising. Aucun arbitrage Gold ajouté à GBM, aucune configuration BRD présumée. [Analyse et CMP022/CMP023](18-politiques-engagement-gbm-brd.md).

## CAP036

**id**

CAP036

**intitule**

Préparer et expédier les articles depuis un magasin

**regroupement_de_travail**

Exécution magasin / ventes omnicanales

**resultat**

Réaliser la préparation et l’expédition magasin et rendre leur résultat connaissable.

**statut_perimetre**

Candidat opérationnel SFS ; rattachement et profondeur à éprouver

**realisation_decrite**

Magasins sollicités dans U04 ; applications et responsabilité détaillée de réalisation à inventorier.

**source**

U04 ; A04/T08 section 3 ; P58

**statut**

Proposition assistant retrouvée à l’audit ; intitulé contextualisé par Codex. Candidat de travail, hiérarchie non validée.

**limite**

Distinct de la gestion des demandes CAP018 et des prestations entrepôt CAP024 ; ne pas élargir implicitement le périmètre C-Log.

**comparaison_marche**

Non comparée à un élément précis ; ajout à marche/comparaisons.md le 2026-09-09.

**Actualisation CAP001 — U100/C66 :** le périmètre auparavant formulé « Informations externes à recevoir ; articulation avec Catalog D12 à préciser sans assimiler catalogue commercial et totalité du modèle produit » est précisé par l’autonomie article et D08.d. Intitulé et résultat historiques conservés ; autres fiches inchangées.

**Actualisation CAP002 — U102/C68 :** ancien périmètre « Les lieux restent un sujet distinct en D06, avec autorités à préciser » remplacé par réception des références réseau en D13.a et appréciation contextuelle en D06. Intitulé et résultat historiques conservés, aucune administration réseau locale ajoutée.

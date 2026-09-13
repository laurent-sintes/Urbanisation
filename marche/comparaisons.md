# Comparaisons Beaumanoir–marché

État : 2026-09-09. Auteur : Codex. Statut global : exploratoire, aucune équivalence ni adoption validée. Sources locales : [capacités candidates](../connaissance/09-capacites-candidates.md), [corrections](../connaissance/04-corrections.md), [questions](../connaissance/06-questions.md). Les éléments externes et leurs versions sont décrits dans [elements.md](elements.md).

## Comparaison de structure

### CMP001

- Élément externe : ELM001, SAP RBA, version du catalogue non établie.
- Élément local : U01 et Q001, proposition Domaine / Capacité / Sous-capacité.
- Relation : comparaison de convention, pas correspondance terme à terme.
- Constat corrigé (U24/C31, 2026-09-09) : l’option locale envisage trois niveaux ; la présentation SAP complète ajoute Enterprise Domain au-dessus de Business Domain, Business Area et Business Capability. Comparer les rôles des niveaux et leur granularité, sans inférer une équivalence du nombre de niveaux.
- Adaptation proposée : préciser pour chaque niveau s'il regroupe ou s'il décrit une capacité, avant d'y rattacher les CAP.
- Justification : éviter qu'une ressemblance de libellés impose une granularité inadaptée.
- Preuve : principe externe consulté ; rapprochement à valider par Laurent. Aucun changement de hiérarchie effectué.

### CMP002

- Élément externe : ELM002, SAP RBA, même état documentaire.
- Éléments locaux : registres CAP, APP/ORG et FL ; orientation U02.
- Relation : appui méthodologique.
- Constat local : les registres séparent déjà capacités, composants et flux. Un flux de données ne décrit pas nécessairement un processus métier.
- Adaptation proposée : relier explicitement les activités d'un parcours aux capacités mobilisées et aux applications qui les soutiennent.
- Justification : faciliter une comparaison indépendante des produits et des chaînes applicatives existantes.
- Preuve : principe externe consulté ; aucune conformité SAP ni équivalence des deux plateformes revendiquée.

## Premiers rapprochements de contenu

Les CMP003–CMP008 utilisent les libellés de l'exemple IBM de 2005. Dans chaque ligne, la relation est une **piste lexicale**, la confiance sémantique est **faible**, la décision est **à instruire** et aucune adaptation n'est appliquée. Il faut une définition plus précise avant de conclure à une équivalence, une inclusion ou un recouvrement.

| ID | Élément externe | Capacités locales | Adaptation envisagée et justification | Écart à instruire |
| --- | --- | --- | --- | --- |
| CMP003 | ELM003 | CAP001 | Garder la maille opérationnelle SKU pour comparer un résultat métier précis. | Inclut-il la création des articles, leur diffusion et les attributs commerciaux ? |
| CMP004 | ELM004 | CAP007, CAP008, CAP009, CAP035 | Conserver les distinctions protection, tenue, révision et arbitrage pour exposer les responsabilités. | Distinguer protection GBM et arbitrage BRD ; ne pas importer de repriorisation Gold dans GBM. |
| CMP005 | ELM005 | CAP011, CAP012, CAP013 | Préserver les responsabilités distinctes d'IRMA et de Storeland. | Paramétrage, application et déclenchement constituent-ils des sous-capacités ou des activités ? |
| CMP006 | ELM006 | CAP014 | Distinguer commande client et demandes d'exécution. | Autorité de commande et périmètre exact du suivi à clarifier. |
| CMP007 | ELM007 | CAP033 | Examiner le SAV de Sarenza comme cas d'épreuve. | Le service client dépasse potentiellement le seul après-vente. |
| CMP008 | ELM008 | CAP034 | Séparer l'autorisation commerciale du retour de son exécution physique. | La logistique des retours ne couvre pas nécessairement l'autorisation ou l'échange ; frontière C-Log à préserver. |

Les justifications sont des analyses Codex à partir des connaissances locales, pas des définitions attribuées à IBM. Elles ne changent aucun statut métier.

## Orientation de deux couches métier

CMP009–CMP012 : auteur Codex, date 2026-09-09, état local U18–U20 et P60–P62 ; voir la [note d'orientation](../connaissance/15-orientation-deux-couches.md). Relation commune : **appui méthodologique**, sans équivalence. Statut : rapprochements à instruire ; aucun standard, format ou choix d'exécution adopté. U19 confirme un modèle métier, des objets, une persistance et une urbanisation propres à chaque couche. U20 précise la généricité du socle par rapport au métier de l'entreprise. Cette analyse ne renomme, ne déplace et ne reclasse aucune CAP, notamment CAP019 et CAP033.

### CMP009

- Élément externe : [ELM009](elements.md#elm009), SAP, état documentaire daté dans MKT04.
- Éléments locaux : F108, qualification du modèle du socle comme *Business Capability* ; F110, généricité par rapport au métier exercé ; U18–U20.
- Adaptation proposée : utiliser « capacités métier génériques du socle » pour préciser ce modèle dans notre périmètre commerce ; relier les deux urbanisations métier à leurs réalisations. La généricité se rapporte au métier de l'entreprise et se distingue du fonctionnement organisationnel.
- Justification : l'indépendance des capacités vis-à-vis des solutions chez SAP appuie cette intention. Son terme *Business Capability* a une portée plus large que le seul transactionnel ; conserver cette différence de périmètre permet la comparaison. La couche haute garde son propre modèle métier ; le socle n'est assimilé ni à un moteur universel ni à du simple CRUD.
- Limite de preuve : rapprochement terminologique proposé ; aucune équivalence entre les deux couches Beaumanoir et les modèles SAP n'est démontrée.

### CMP010

- Élément externe : [ELM010](elements.md#elm010), SOA-RM 1.0.
- Élément local : F107, contrats API/EDA durables entre les couches ; U18/U19.
- Adaptation proposée : préciser capacités accessibles, objets échangés, effets attendus et conditions d'usage de chaque contrat.
- Justification : service, description et contrat permettent de séparer l'accès à une capacité de sa réalisation.
- Limite de preuve : ces concepts ne prouvent ni découplage effectif ni stabilité future ; frontières, garanties et règles d'évolution restent locales et à instruire.

### CMP011

- Élément externe : [ELM011](elements.md#elm011), CMMN 1.1.
- Élément local : F109, modèle, objets, persistance et urbanisation propres à chaque couche ; U19.
- Adaptation proposée : éprouver les concepts de dossier, informations, rôles et tâches sur les situations longues de la couche haute, en les reliant au socle par contrats.
- Justification : ce modèle de dossier fournit un appui pour décrire un ensemble métier propre, au-delà d'un simple enchaînement d'appels.
- Limite de preuve : CMMN ne valide pas à lui seul nos frontières d'urbanisme, le stockage ou les droits d'accès. Aucun choix CMMN ni reclassement de capacités n'est effectué.

### CMP012

- Éléments externes : [ELM012](elements.md#elm012), OpenAPI 3.2.0 ; [ELM013](elements.md#elm013), AsyncAPI 3.0.0.
- Élément local : F107, contrats API/EDA ; U18/U19.
- Adaptation proposée : examiner ces formats pour décrire respectivement les interfaces HTTP et à messages, à partir de contrats métier définis.
- Justification : ils fournissent des représentations documentables indépendantes d'un produit d'exécution.
- Limite de preuve : les introductions seules ne valident ni couverture détaillée ni conformité ; compatibilité, versions, autorisations et garanties sémantiques restent à définir. Aucun format adopté.

## Stock dans SAP

CMP013–CMP017 : auteur Codex, date 2026-09-09, état local U22/U23, CAP inchangées. Statut commun : **rapprochements proposés, à instruire** ; aucune équivalence ou adoption. Les versions et localisateurs externes sont dans ELM014–ELM018 et MKT04/MKT13. Voir la [note SAP-stock](sap-stock.md).

### CMP013

- Élément externe : [ELM014](elements.md#elm014), extrait de hiérarchie SAP RBA, complété après U24/C31 par Enterprise Domain au-dessus du Business Domain (2026-09-09).
- Éléments locaux : P63/P64 et question U23 ; familles stock/disponibilité, protections/engagements et frontière C-Log.
- Relation : appui méthodologique.
- Adaptation proposée : examiner « Gestion des stocks » comme domaine local en documentant qu’il correspond chez SAP à un Business Area ; distinguer gestion des stocks, promesse et entrepôt.
- Justification : ne pas confondre niveau de regroupement, capacité et organisation ; conserver les quatre niveaux visibles de la référence lors du rapprochement.
- Limite : définitions détaillées des feuilles absentes ; cet exemple ne valide ni niveaux locaux ni découpage des deux couches. Aucune CAP C-Log n’est comparée individuellement ici.

### CMP014

- Élément externe : [ELM015](elements.md#elm015), description fonctionnelle des stocks S/4HANA.
- Éléments locaux : CAP004 et CAP005 ; U03/U04, INF01–INF03.
- Relation : appui sémantique ; confiance limitée par le détail local disponible.
- Adaptation proposée : expliciter quantités, états et mouvements tenus par une autorité, puis provenance et fraîcheur des représentations exposées.
- Justification : les états enregistrés éclairent le contenu à distinguer de sa copie ; la documentation produit ne définit pas à elle seule notre capacité de visibilité.
- Limite : CAP004 demeure magasin ; autorité entrepôt inconnue. La finance reste hors domaine. Aucun effet de temps réel ou absence de survente démontré.

### CMP015

- Éléments externes : [ELM014](elements.md#elm014), libellé métier du contrôle de disponibilité ; [ELM016](elements.md#elm016), éclairage fonctionnel aATP.
- Éléments locaux : CAP006 et CAP010 ; Q012/Q018/Q038.
- Relation : appui sémantique partiel, définition locale à compléter.
- Adaptation proposée : distinguer quantité/date confirmable et engagement tenu avec son cycle de modification/libération ; préciser leurs effets réciproques.
- Justification : consulter le stock ne suffit pas à définir la promesse ; une confirmation ne définit pas tout le modèle d’engagement.
- Limite : le produit peut considérer des entrées futures mais la vente GBM nominale sur stock est conservée. Réservation technique, moment d’engagement, invariants de concurrence et garanties locales restent inconnus.

### CMP016

- Éléments externes : [ELM017](elements.md#elm017) et [ELM018](elements.md#elm018), fonctions de protection et allocation S/4HANA.
- Éléments locaux : CAP007/CAP008/CAP009/CAP035 ; U02/U10 ; Q029–Q032/Q049.
- Relation : appui sémantique, sans équivalence de mécanisme.
- Adaptation proposée : distinguer quantité protégée pour un groupe, limite de confirmation, révision des paramètres et arbitrage sur des engagements.
- Justification : le mot allocation recouvre plusieurs résultats et responsabilités possibles.
- Limite : populations, unités, horizons et application MAP à préciser. Objets republiés et effet sur engagements inconnus. Ne pas importer de repriorisation Gold dans GBM ni assimiler ce contrôle à l’ARun utilisé chez Boardriders.

### CMP017

- Éléments externes : [ELM014](elements.md#elm014), feuille d’inventaire physique ; [ELM015](elements.md#elm015), comptage et traitement des différences.
- Éléments locaux : CAP004, P64 et Q065.
- Relation : appui sémantique et recherche d’un manque de description.
- Adaptation proposée : explorer constats de comptage, écarts et corrections, ainsi que leurs effets sur disponibilité et engagements ; distinguer organisation de campagne et enregistrement des faits.
- Justification : états/mouvements ne rendent pas explicite ce contenu ; les écarts de réception d’achat de P08 ne couvrent pas l’inventaire.
- Limite : manque de connaissance, pas capacité déclarée absente chez Beaumanoir. R20 mentionne des fonctions d’inventaire d’un produit sans prouver leur usage GBM. Aucun nouveau candidat ni élargissement à l’autorité C-Log.

## Périmètre restant à comparer

Les groupes ci-dessous orientent les recherches ; ils ne constituent pas des correspondances déjà prouvées.

| Capacités | Recherche prioritaire proposée | État |
| --- | --- | --- |
| CAP002, CAP003 | Définitions des référentiels et conditions dans SAP / ARTS | Élément externe précis non examiné |
| CAP015, CAP016, CAP017, CAP018, CAP019 | Exécution omnicanale et exceptions dans Oracle ; contrôle APQC | Élément externe précis non examiné |
| CAP020, CAP021, CAP022, CAP023, CAP024, CAP025 | Contrats et parcours logistiques dans Oracle / APQC | Élément externe précis non examiné ; C-Log reste une frontière |
| CAP026, CAP027, CAP028 | Interfaces de planification dans SAP / APQC | Élément externe précis non examiné ; maintien des exclusions amont |
| CAP029 | Demande d’achat et sous-traitance SAP | Complément U48 : rapprochement partiel ELM043/CMP030 ; statut ferme et document MAP non assimilés |
| CAP030, CAP031, CAP032 | Achats et suivi fournisseur dans SAP / Oracle / APQC | Fiches non comparées à un élément précis ; la lecture U48 de sous-traitance ne suffit pas à établir ces rapprochements |
| CAP036 | Préparation/expédition magasin dans Oracle / APQC | Candidat restitué à l’audit du fil le 2026-09-09 ; élément externe précis non examiné |

Bilan après U22/U23 : 15 capacités disposent d’au moins un rapprochement documentaire proposé, et 21 restent sans comparaison d’élément précis. Les 11 pistes lexicales IBM sont conservées ; SAP apporte des appuis à huit CAP, dont quatre déjà citées par IBM. Ce décompte mesure le travail documentaire, pas une couverture fonctionnelle démontrée. Zéro équivalence validée. La pertinence pour le B2B Boardriders et le modèle de revente/SAV Sarenza reste à démontrer.

## Vue exploratoire du socle

La [vue P63 du 2026-09-09](../connaissance/16-capacites-socle-transactionnel.md), issue de U21, propose huit familles d’exploration du socle. CMP003–CMP008 restent des pistes lexicales sur les CAP citées, sans équivalence des familles ni validation de leur rattachement. À sa création, 11 capacités avaient une piste lexicale et 25 restaient sans comparaison précise. Le complément SAP U22/U23 ci-dessus porte désormais ce suivi à 15 capacités avec rapprochement et 21 sans comparaison précise. Aucune définition CAP n’est modifiée.

## Reprise lors d'une évolution

Quand une capacité change, réexaminer les CMP qui la citent. Si sa définition, sa maille ou son périmètre évolue, marquer le rapprochement « à revalider » et dater la modification. Une capacité nouvelle doit recevoir une correspondance argumentée ou le statut « non comparée » ; elle ne doit pas être déclarée spécifique à Beaumanoir par défaut.

## Étude comparative des modèles

### CMP018

- Éléments externes : ELM001/ELM014 et ELM019–ELM030 ; références MKT01–MKT08/MKT14/MKT15, éclairage fonctionnel MKT13.
- Élément local : U25 ; [étude comparative](etudes/2026-09-09-modeles-marche/etude-comparative.md) ; Q001.
- Relation : appui méthodologique à la comparaison des structures et contenus.
- Constat : proximité de notion capacité, thèmes récurrents et niveaux de natures différentes. Les matrices comparent des modèles externes ; elles ne constituent pas un nouveau relevé exhaustif de correspondances avec les CAP locales.
- Adaptation proposée : qualifier nature, objet, résultat, périmètre et granularité avant de comparer les positions ; séparer niveaux, catégories, responsabilités et réalisation.
- Justification : les mêmes thèmes sont classés différemment selon l’objectif du modèle ; un chemin ne démontre pas l’équivalence.
- Preuve et limite : sources examinées selon leurs éditions et accès datés dans l’étude ; détails parfois absents ou historiques. Aucune équivalence de catalogue, conformité locale ou hiérarchie principale validée.
- Auteur/date/statut : Codex, 2026-09-09, analyse proposée.

### CMP019

- Éléments externes : ELM021 (frontières/décomposition) ; ELM023 (identité et chemin) ; ELM027 (déplacements documentés du catalogue Microsoft).
- Élément local : P65 ; méthode de maintenance ; Q001.
- Relation : appui méthodologique.
- Adaptation proposée : conserver une identité locale stable, plusieurs correspondances externes typées et versionnées, et un résultat métier explicite ; examiner objet/résultat/périmètre/granularité avant toute équivalence.
- Justification : distinguer une évolution de classement d’une évolution du besoin ; éviter de fusionner données, aptitudes, parcours et fonctions de produit.
- Preuve et limite : règle locale proposée à partir d’exemples sourcés ; ne fixe ni niveaux locaux ni découpage des applications. Les 36 CAP conservent leurs définitions et statuts.
- Auteur/date/statut : Codex, 2026-09-09, proposition à éprouver, aucun valideur métier.

## Exploration du bloc stock et du stock logique

### CMP020

- Éléments externes : ELM014, hiérarchie SAP RBA ; ELM024, ARTS vue 07620 ; ELM028, allocation virtuelle Microsoft Inventory Visibility. Sources reconsultées le 2026-09-09 ; éditions et limites dans MKT04/MKT08/MKT14.
- Éléments locaux : U26/U27 ; F113/F114 ; P66 ; [exploration du bloc stock](../connaissance/17-exploration-bloc-stock.md). CAP004/CAP005/CAP006/CAP007/CAP008/CAP009/CAP010/CAP035 citées dans la vue, sans changement de définition.
- Relation : appui méthodologique et sémantique, sans équivalence des blocs.
- Constat : la gestion des états/mouvements et la promesse sont des aires distinctes chez SAP ; Microsoft distingue allocation virtuelle de groupe et réservation de transaction ; ARTS distingue effets sur physique et disponible.
- Adaptation proposée : rattacher les opérations à leurs objets, définir disponibilité par usage/horizon et distinguer pools logiques des positions physiques. Une vue transverse ne transfère pas les autorités de modification. Le statut de stock virtuel/logique reste à préciser dans Q066.
- Justification : le bloc Inventory local rassemble des responsabilités réparties autrement dans le marché ; la famille Management mélange des effets sur stock et allocation. La présence d’un pool dans un produit ne prouve pas un quatrième domaine standard.
- Limite de preuve : proposition locale ; pas de trois applications/persistances imposées, ni d’extension de l’autorité CAP004 aux entrepôts. Aucun fonctionnement MAP/ARun ni politique de vente sur stock futur déduit. Ces CAP étaient déjà rapprochées : le total demeure 15 CAP avec rapprochement documentaire et 21 sans comparaison précise.
- Auteur/date/statut : Codex, 2026-09-09, proposition à éprouver ; aucune équivalence ou hiérarchie validée.

## Vocabulaire allocation et réservation

### CMP021

- Éléments externes : ELM017/ELM018/ELM028 et ELM031–ELM033 ; MKT13/MKT14/MKT16, états documentaires datés dans la [note comparative](allocation-reservation-sap-microsoft.md).
- Éléments locaux : U28/U29, F115/F116, P67 ; CAP007/CAP008/CAP009/CAP010/CAP035 citées sans modification, Q018/Q030–Q032/Q049/Q066/Q067.
- Relation : appui sémantique et méthodologique, recouvrements partiels de finalité ; aucune équivalence de mécanisme.
- Adaptation proposée : définir séparément enveloppe de groupe, engagement d’une demande, affectation de ressource, promesse quantité/date et révision ; comparer les effets, indépendamment des noms de fonctions et des modes batch/API.
- Justification : la lisibilité du vocabulaire et la variété de mécanismes sont deux critères distincts ; le regroupement dans un traitement ne fixe pas les frontières du socle.
- Limite : pas de supériorité générale d’éditeur démontrée ni de transition unique ECC–S/4 certifiée. Aucun fonctionnement local MAP/ARun importé ; les 15 CAP avec rapprochement et 21 sans comparaison précise restent inchangées.
- Auteur/date/statut : Codex, 2026-09-09 ; proposition à éprouver, aucun valideur métier.

## Politiques GBM/BRD et promesse aux demandes

### CMP022

- Éléments externes : ELM028/ELM031/ELM032 et ELM034/ELM035 ; MKT13/MKT14, versions datées dans la [note de travail](../connaissance/18-politiques-engagement-gbm-brd.md).
- Éléments locaux : U30, F117–F120, P68, CAP006/CAP010/CAP014/CAP035 enrichies de provenance le 2026-09-09, DEC21/DEC22 ; Q018/Q049/Q068.
- Relation : appui sémantique et recouvrement partiel des comportements.
- Adaptation proposée : un modèle de ressources et engagements exprimant politiques sur stock présent, offre future admissible et révision prioritaire ; distinguer commande, confirmation et affectation.
- Justification : le besoin BRD couvre tous les comportements cités par Laurent ; le principe GBM réserve au passage de commande, avec les limites connues de sa politique.
- Limite : pas de comportement exclusif SAP déduit ; Microsoft SCM documente aussi les entrées futures. Besoin BRD explicite, configuration installée inconnue. Les résultats et statuts des CAP ne sont pas modifiés ; aucune nouvelle CAP ni équivalence validée. Ces quatre CAP étaient déjà rapprochées : bilan 15/21 inchangé.
- Auteur/date/statut : Codex, 2026-09-09 ; rapprochement proposé, besoin U30 déclaré par Laurent.

### CMP023

- Éléments externes : ELM014 (aire RBA Order Promising) et ELM036 (BOP dans la documentation de solution), avec conditions ELM035.
- Éléments locaux : U31, F121, P69, CAP010/CAP035 ; regroupement exploratoire P66/P67 ; orientation des deux couches.
- Relation : appui sémantique et méthodologique pour une frontière de responsabilité.
- Adaptation proposée : rattacher la révision des promesses à Order Promising, avec accès aux ressources et contraintes de protection et effets coordonnés sur les engagements. La capacité générique est réexaminer et réviser les promesses aux demandes.
- Justification : le résultat principal porte sur une confirmation à une demande ; mobiliser un stock ou modifier une affectation ne suffit pas à classer toute la responsabilité dans la tenue du stock.
- Limite : rattachement produit BOP corroboré, feuille RBA non vérifiée. SAP peut aussi traiter des demandes de transfert. Aucun niveau, regroupement CAP définitif ou architecture d’applications validé. Aucun nouveau périmètre de CAP comparé, bilan 15/21 conservé.
- Auteur/date/statut : Codex, 2026-09-09 ; proposition issue de l’analyse de Laurent, à éprouver.

## Granularité des fonctions de marché

### CMP024

- Éléments externes : ELM014 et ELM037–ELM039, avec ELM034 pour les politiques de réservation Microsoft ; MKT04/MKT13/MKT14, versions et localisateurs dans la [note détaillée](detail-fonctions-stock-promesse.md).
- Éléments locaux : U32/U33, F122/F123/F124, A21/A22, P70 ; P66/P67/P69 ; précision C33. CAP007/CAP008 cités comme points d’entrée analytiques, sans modification.
- Relation : appui méthodologique et sémantique à la description détaillée.
- Adaptation proposée : typer séparément capacité, objet, opération, état, règle/variante et réalisation ; décomposer la carte selon des aptitudes métier durables indépendantes de l’organisation et des outils, dans le périmètre parent ; responsabilités et contrats viennent ensuite éclairer la réalisation. Ne pas compter les API ou les paramètres.
- Justification : SAP et Microsoft offrent un détail plus fin que les fonctions précédemment présentées, mais ce détail n’est pas un catalogue de sous-capacités homogène.
- Limite : aucun étage de sous-capacités RBA vérifié ; aucun nouveau candidat, transfert de planification ou niveau local adopté. Aucune nouvelle CAP rapprochée : bilan documentaire de 15 avec rapprochement et 21 sans comparaison précise conservé, zéro équivalence validée.
- Auteur/date/statut : Codex, 2026-09-09 ; proposition méthodologique à éprouver.

## Provenance des verbes du glossaire

### CMP025

- Éléments externes : ELM040, MKT13 ; vocabulaire anglais Manage/Maintain, éditions et accès précisés dans la fiche.
- Éléments locaux : U35, F127, A22, C34, P71 et VER002 du [glossaire](../connaissance/19-glossaire-metier.md).
- Relation : appui sémantique et clarification de provenance ; aucune équivalence de capacité.
- Adaptation proposée : mettre tenir en réexamen et choisir un verbe français selon l’aptitude et le résultat visés. Gérer les protections, mettre à jour les quantités protégées et déterminer la protection applicable sont des propositions de portées différentes, pas des traductions officielles ni des synonymes.
- Justification : tenir était une formulation de l’assistant, dont Laurent conteste la clarté ; le vocabulaire éditeur ne suffit pas à fixer nos libellés.
- Limite : aucune nomenclature française SAP vérifiée, aucun remplacement automatique des CAP. Le bilan reste de 15 CAP avec rapprochement documentaire et 21 sans comparaison précise, zéro équivalence validée.
- Auteur/date/statut : Codex, 2026-09-09 ; provenance clarifiée, formulations alternatives proposées.

## Premier niveau de regroupement

### CMP026

- Éléments externes : ELM014 (SAP RBA), ELM019 (TOGAF G189), ELM021 (atelier Guild), ELM025 (IBM CBM), ELM026 (Microsoft), ELM023 (APQC), reconsultés le 2026-09-10. Sources et localisateurs dans la [note comparative](premier-niveau-regroupement-capacites.md).
- Éléments locaux : U43/U44, F134/F135, A25, P73 ; vue du socle et glossaire Nature/Finalité.
- Relation : appui méthodologique et comparaison de structures ; aucune équivalence d’élément ou de niveau.
- Adaptation proposée : éprouver Univers / Domaine / Capacité rapporté par Laurent en U44, ou Domaine / Capacité si l’étage supérieur n’apporte pas de lecture utile ; distinguer catégories, capacités composites et qualifications transverses. Le draft de juin n’a pas été consulté.
- Justification : le marché examiné ne fixe pas un même premier niveau ; capacités, composants et processus obéissent à des structures différentes.
- Limite : supports historiques explicitement datés, catalogues complets non acquis. Stock/Promesse sont des exemples locaux, avec disponibilité et engagements à positionner. Aucun domaine complet comparé par sa seule étiquette, aucune nouvelle CAP rapprochée : bilan 15 avec rapprochement documentaire et 21 sans comparaison précise, zéro équivalence validée.
- Auteur/date/statut : Codex, 2026-09-10 ; proposition à éprouver, aucun classement métier validé.

## Sens du domaine avec DDD

### CMP027

- Élément externe : ELM041, MKT17, définitions d’Evans ©2015, page vi ; consultation du 2026-09-10.
- Éléments locaux : U45/U46, F136–F138, A25/A26/P73, C37/C38 et TER030.
- Relation : appui sémantique et méthodologique ; pas équivalence de hiérarchie ou de capacité.
- Adaptation proposée : partir d’un espace cohérent de problèmes métier liés entre eux, expliciter les liens, concepts et règles, puis déterminer les capacités nécessaires ; classer ensuite ces capacités dans la carte. La conception des bounded contexts est hors de l’étape actuelle selon U46.
- Justification : préciser la cohérence du domaine au-delà d’un simple regroupement de fiches partageant des objets ou des résultats.
- Limite : définition rédactionnelle locale proposée, distincte de la formulation native d’Evans. Univers reste une convention locale à éprouver ; domaine, capacité et frontière de modèle sont distingués. Aucun domaine concret ni découpage de réalisation adopté ; bilan de couverture CAP 15/21 inchangé.
- Auteur/date/statut : Codex, 2026-09-10 ; orientation U45 explicite, définitions détaillées et rattachements proposés.

## Construction itérative des domaines

### CMP028

- Éléments externes : ELM019 (TOGAF G189, juin 2018, §3.1, pages 6–7) et ELM027 (Microsoft Inventory to deliver, page du 2025-01-21, sections précisées dans la fiche), réexaminés le 2026-09-10.
- Éléments locaux : U47/F139, A27/P74 et [première liste de domaines](../connaissance/20-domaines-candidats.md), état du 2026-09-10.
- Relation : appui méthodologique et contrôle de couverture ; aucune équivalence de domaine ou de capacité.
- Adaptation proposée : une première liste de problèmes cohérents éclairée par le marché, immédiatement confrontée aux récits et candidats existants, puis ajustée par les cas difficiles et les lacunes constatées.
- Justification : combinaison des approches de construction documentée dans G189 ; comptage, ajustements et retours présents dans les processus Microsoft utiles comme cas de contrôle. Le terrain existant permet de commencer sans attendre une collecte exhaustive.
- Limites : six domaines proposés pour le noyau décrit, zones complémentaires maintenues visibles ; périmètres complets non comparés à cette maille. Les besoins Boardriders ne prouvent pas une configuration installée. Le marché ne valide ni le nombre de domaines, ni leurs intitulés, ni leurs frontières. Couverture CAP inchangée : 15 rapprochements documentaires, 21 sans comparaison précise, zéro équivalence validée.
- Auteur/date/statut : Codex, 2026-09-10 ; proposition à discuter avec Laurent.

## Achats à façon et orchestration

### CMP029

- Éléments externes : ELM002 (SAP RBA, cours d’édition non précisée) et ELM042 (BPMN 2.0.2 §7.2.1), consultés le 2026-09-10.
- Éléments locaux : U48/U49, F144–F146, A28/A29/P75/C40 et [analyse de l’orchestration](../connaissance/21-achats-et-orchestration.md), état du 2026-09-10 ; orientation U18–U21.
- Relation : appui méthodologique et sémantique.
- Adaptation proposée : distinguer aptitude métier durable, coordination spécifique d’un cas et moyen générique d’orchestration. U49 précise des moteurs dans les deux couches, orientés Case Management pour la couche processus ; même solution ou solutions distinctes restent possibles. Pas de boîte générique ajoutée à la carte du socle du seul fait de ces moyens.
- Justification : séparer les objets de modèle et leurs réalisations ; conserver le métier propre de la couche haute et les règles de validité des engagements dans leurs domaines.
- Limite : les sources externes ne prescrivent pas le placement des moteurs ; leur présence dans les deux couches est l’orientation locale explicite de U49. U50/F147 réaffirme que la capability map cible le socle et qu’un autre modèle fonctionnel orienté processus décrira la couche processus. Les usages plus larges du marché n’étendent pas la carte locale. Aucune plateforme unique ni nouvelle capacité validée.
- Auteur/date/statut : Codex, 2026-09-10 ; proposition à discuter.

### CMP030

- Éléments externes : ELM043 (cours SAP sous-traitance, édition produit inconnue), ELM044 (Microsoft SCM, page du 2025-08-13), consultés le 2026-09-10.
- Éléments locaux : U48/F140–F143, CAP029 précisée sur sa réalisation, P75 et [hypothèses sur les achats à façon](../connaissance/21-achats-et-orchestration.md), état du 2026-09-10.
- Relation : recouvrement partiel entre l’émission d’une demande d’achat de CAP029 et la création de demande décrite dans ELM043 ; contrôle de couverture pour le cas à façon avec ELM043/ELM044.
- Adaptation proposée : conserver la distinction besoin/engagement ferme, examiner les biens et prestations, ressources chez un tiers et liens composants/résultat comme objets et règles de capacités potentielles.
- Justification : U48 dépasse la seule variante d’enchaînement et expose des engagements et ressources à comprendre. Les deux produits fournissent des cas concrets pour approfondir ces questions.
- Limite : aucune équivalence entre Planned Purchase Order et Purchase Requisition/Order établie. La demande SAP citée est spécifique à la sous-traitance ; le document MAP de U48 est déclaré dans le premier cas, pas généralisé aux trois. Propriété et suivi locaux restent ouverts. Aucun rapprochement précis des fiches CAP030–CAP032 réalisé, ni capacité nouvelle créée.
- Bilan : CAP029 rejoint les capacités disposant d’un rapprochement documentaire partiel ; 16 CAP rapprochées, 20 sans comparaison précise, zéro équivalence validée. Ce chiffre mesure la documentation, pas la couverture fonctionnelle.
- Auteur/date/statut : Codex, 2026-09-10 ; rapprochement proposé et questions métier ouvertes.

## Options de découpage des domaines du socle

### CMP031

- Éléments externes : ELM001/ELM014 SAP RBA (cours d’édition non précisée), ELM025 IBM CBM (2005, figure 6), ELM027 Microsoft (vue des scénarios datée 2025-12-16) ; passages reconsultés le 2026-09-10. Les autres matrices de l’étude U25 sont reprises avec leurs limites antérieures.
- Éléments locaux : U51/U52, F148–F150, A31/A32/P76/C42, [options de domaines](../connaissance/22-options-domaines-socle.md), état du 2026-09-10, première liste U47 et cas achats U48 ; périmètre U50.
- Relation : appui méthodologique et comparaison de structures ; pistes de couverture des problèmes.
- Adaptation après U52 : le critère problématique guide les domaines et l’examen des frontières par les cas est confirmé. Source to Pay apporte une lecture processus ; Order Promising est reconnu comme domaine local, indépendamment de son niveau nominal SAP. Référence principale et grandes familles restent des choix d’appui et de présentation distincts de ce critère.
- Justification : les références offrent des mailles et des types distincts ; les récits permettent d’éprouver les frontières stock/disponibilité/promesse, achats/réassort et commande/exécution.
- Limites : les dix périmètres proposés sont locaux, sans nombre cible ni validation. Sites et conditions commerciales restent à délimiter. Domaines complets non comparés précisément ; aucun alignement de niveau, catalogue principal ni déplacement de CAP adopté. La capability map reste limitée au socle transactionnel.
- Auteur/date/statut : Codex, 2026-09-10 ; démarche confirmée par Laurent en U52, frontières détaillées et liste proposées. Couverture CAP conservée à 16 rapprochements documentaires et 20 sans comparaison précise ; zéro équivalence validée.

## Réassort, cœur commun et Order Promising

### CMP032

- Éléments externes : ELM014 (structure RBA), ELM045 (transferts SAP), ELM046 (promesse et réexamen ventes/transferts), ELM047 (retours ARM) ; cours d’éditions non précisées, passages consultés le 2026-09-10.
- Éléments locaux : U53–U58/F151–F158, A33/A34/P77/C43/C44 et [note réassort, transferts et promesse](../connaissance/23-reassort-transferts-et-promesse.md), état du 2026-09-10 ; anciens candidats conservés comme points d’appui.
- Relation : appui sémantique et contrôle des frontières ; pas équivalence de domaine complet.
- Adaptation proposée : examiner des problèmes de supply partagés entre parcours commerciaux, distinguer promesse, stock et exécution, puis qualifier séparément les engagements et effets commerciaux. U54/U55 placent les parcours de l’OMS dans un Case Management de vente ; U56 définit le transactionnel Supply comme contrôle, orchestration et optimisation de la logistique ; U57 lui attribue aussi rééquilibrage, prévision et gestion des impondérables.
- Justification : les transferts intra/intercompany offrent des cas discriminants ; SAP confirme des besoins de vente et transfert sans réunir toute leur vie dans Order Promising. L’opposition entre achat externe et réassort interne est insuffisante pour délimiter les domaines.
- Limites : Supply Decision & Execution est un intitulé local issu de Laurent, sans équivalence native SAP établie. Ni domaine unique ni modèle de demande universel adopté. Finance demeure une interface ; réalisation C-Log autonome. U58 place la logistique hors développement FLOW, en adhérence : les comparaisons métier et exemples de produits n’étendent pas le périmètre de réalisation de la plateforme. Les variantes produit ne prouvent aucun déploiement local ; les nouveaux appuis ne constituent pas une comparaison précise de CAP011–CAP013.
- Auteur/date/statut : Codex, 2026-09-10 ; définitions locales de Laurent appliquées, frontières proposées. Couverture CAP inchangée : 16 rapprochements documentaires, 20 sans comparaison précise, zéro équivalence validée.

## Granularité SAP et alternatives par domaines

### CMP033

- Éléments externes : ELM002/ELM009/ELM014 SAP ; ELM021 Guild ; ELM025 IBM ; ELM048 BIAN ; ELM049–ELM051 TM Forum.
- Éléments locaux : U59/F159, A35/P78, domaines de problèmes U45/U46/U52, [comparaison de granularité](premier-niveau-regroupement-capacites.md#granularité-sap-et-autres-modèles-orientés-domaines), état du 2026-09-10 ; périmètre FLOW U58.
- Relation : appui méthodologique et comparaison de mailles et de natures ; aucune équivalence de domaines ou capacités.
- Adaptation proposée : privilégier les aires SAP documentées comme grille d’épreuve du contenu commerce/stock. Employer IBM pour la contrelecture retail et BIAN/TM Forum pour éprouver regroupements et relations entre vues ; Guild pour la définition des aptitudes.
- Justification : les exemples stock/promesse offrent une maille opérationnelle compatible avec l’examen de problèmes locaux. Les alternatives enrichissent la comparaison tout en poursuivant des objectifs distincts ; domaines, capacités, partitions de services et fonctions SI ne sont pas interchangeables.
- Preuves et limites : cours SAP sans édition de catalogue ; IBM 2005 ; preuve Guild historique conservée, nouvelles ouvertures directes échouées ; guide BIAN 2020 distinct de la version 14.0 annoncée en 2026 ; présentations TM Forum lues, documents membres non consultés. Aucun catalogue retail complet nouvellement acquis ni classement exhaustif de marché.
- Auteur/date/statut : Codex, 2026-09-10 ; recommandation proposée, pas choix de catalogue principal par Laurent. Aucun transfert de réalisation logistique vers FLOW. Les 36 CAP restent inchangées, 16 rapprochements documentaires et 20 sans comparaison précise, zéro équivalence validée.

- Actualisation U60 du 2026-09-10 : les rôles proposés sont précisés par C45/P79/CMP034. IBM non prioritaire pour le découpage actuel ; BIAN périphérique ; TM Forum reste une piste. Les accès publics Guild 15.0 et métamodèle 2024 ont désormais réussi, sans accès au catalogue membre ni preuve d’un modèle retail livré.

## Approfondissement BIZBOK après U60

### CMP034

- Éléments externes : ELM021 atelier 2019 reconsulté ; ELM052 glossaire 15.0 ©2026 ; ELM053 Metamodel Guide 3.0 de septembre 2024 ; ELM054 introduction 15.0 ; ELM055 notices des modèles membres.
- Éléments locaux : U60/F160/F161, A36/P79/C45, définition U33, domaines problématiques U45/U46 et Order Promising U52 ; [étude ciblée](bizbok-capacites-et-domaines.md), état du 2026-09-10.
- Relation : appui sémantique et méthodologique, sans équivalence de capacité ou de domaine.
- Adaptation proposée : vérifier objet(s), résultat, périmètre et cohérence des sous-capacités ; distinguer ces règles de la délimitation des domaines par problèmes liés. Le service, la capacité et sa réalisation contextuelle restent des concepts distincts.
- Justification : la méthode Guild précise la décomposition ; elle ne fournit pas les frontières transactionnelles commerce déjà arrêtées ni une hiérarchie Univers/Domaine. L’exemple appliqué à Order Promising est local.
- Limites : guide intégral, §2.2 et modèles membres non consultés. Retail/Wholesale livré, version et contenu non établis ; version courante du Common Reference Model non affichée sur sa notice. Aucun rapprochement précis nouveau de CAP.
- Auteur/date/statut : Codex, 2026-09-10 ; priorités U60 appliquées, usage de méthode proposé. Portée du socle et adhérence logistique FLOW inchangées ; 16 CAP avec rapprochements documentaires, 20 sans comparaison précise, zéro équivalence validée.

## Capacités, objets, faits et documents

### CMP035

- Éléments externes : ELM056 SAP information métier/solution ; ELM057 Guild information/états/résultats ; ELM058 SID ; ELM059 documents/événements SAP ; ELM060 exemples de contrats TM Forum ; ELM061 agrégat DDD, en appui à l’analogie.
- Éléments locaux : U61/U62, F162–F164, A37/A38/P80, TER002/TER036–TER039 et [note d’articulation](../connaissance/24-capacites-objets-et-faits.md), état du 2026-09-10 ; U33 et orientation des deux couches.
- Relation : appui méthodologique et sémantique ; pas équivalence de catégories ni de capacités.
- Adaptation proposée : expliciter objets, états, faits et documents avec les capacités dans un modèle métier lié ; distinguer leur sens des frontières d’agrégat et des formes techniques d’échange ou de stockage.
- Justification : les trois approches décrivent l’information métier par des vues liées, sans la reporter entièrement à la réalisation. Les exemples de documents et notifications révèlent des différences de vocabulaire utiles.
- Limites : BIZBOK complet et SID détaillé non consultés ; exemples SAP Help obtenus via index ; TMF622 v4.0.0 et schéma Document historiques. Aucun ABE = aggregate root, Outcome = événement ni document = objet absolument immuable imposés. L’exemple de promesse est local ; les CAP ne sont pas décomposées.
- Auteur/date/statut : Codex, 2026-09-10 ; méthode proposée, pas adoption d’un schéma technique ou extension du périmètre. Couverture CAP 16 rapprochements documentaires /20 sans comparaison précise conservée, zéro équivalence validée.

### CMP036

- Éléments externes : ELM014–ELM018, ELM024, ELM028, ELM035/ELM036, ELM043–ELM047 et réexamen ELM062 ; ELM053/ELM057/ELM058 en appui de méthode et d’information.
- Éléments locaux : U63/U64, F165/F166, A39/P81, [carte et épreuve des récits](../connaissance/25-domaines-coeur-et-epreuve-recits.md), version de travail 0.1 du 2026-09-10 ; 34 formulations regroupées sous dix domaines.
- Relation : appuis partiels de structure, de sémantique et de couverture ; pas d’équivalence complète de domaines ni de capacités.
- Adaptation proposée : D01 stocks ; D02 disponibilité/protection/engagements de ressources ; D03 promesse ; D04 obligations commerciales communes à éprouver ; D05 équilibrage ; D06 possibilités d’exécution ; D07 engagements/faits d’exécution ; D08 produits ; D09 parties ; D10 conditions. Les coordonnées natives SAP sont préservées ; le domaine local a le sens problématique défini par Laurent.
- Justification : les cas de stock distribué, protection/réservation, futur et réaffectation, réassort et achat à façon mobilisent plusieurs problèmes stables ; les parcours ne deviennent pas des domaines. Le besoin de capacité de service et les parts restant à satisfaire complètent la lecture initiale.
- Limites et non-comparés : regroupement D04 achat/vente/prestation non comparé précisément ; D05.c redistribution, D06 service/quotas et définitions détaillées D08–D10 non comparés précisément. Les appuis de produit sur D01–D03/D07 sont partiels. Les compléments plausibles restent signalés individuellement ; SAP ne prescrit pas ces dix domaines. Aucun catalogue retail Guild/TM Forum détaillé consulté. IBM reste historique non prioritaire.
- Auteur/date/statut : Codex, 2026-09-10, proposition à challenger par Laurent. Les 36 CAP, leurs définitions et leur couverture documentaire historique 16/20 sont conservées ; cette mesure ne vaut pas couverture des 34 formulations P81 ni des entreprises. Aucun candidat ou arbitrage de réalisation validé.

### CMP037

- Éléments externes : ELM063 SAP, ELM064 Microsoft, ELM065 TM Forum, ELM066 exemples publics Guild ; ELM014/ELM028/ELM031 en continuité des lectures antérieures.
- Éléments locaux : U65/F167, A40, domaines D01–D10 de P81 version 0.1, dans la [table des noms proches](correspondances-domaines-coeur.md), comparaison du 2026-09-11.
- Relation : rapprochements terminologiques et sémantiques partiels ; types et niveaux explicités, aucune équivalence de domaines ou de capacités.
- Adaptation : rapprocher chaque domaine d’un ou plusieurs noms natifs, distinguer absence de nom unique et absence de contenu consulté, conserver les différences entre aire RBA, capacité RBA, aire de processus, fonctionnalité, objet, composant et API.
- Justification : les noms de stock/promesse/produit/partie/pricing fournissent des repères ; D02/D04/D06/D07 croisent plusieurs rubriques des références. Le contraste aide à challenger les frontières sans décider d’un renommage.
- Limites : Service Qualification ne suffit pas à une promesse ferme ; Product Inventory TMF n’est pas notre stock de marchandises ; pricing ne couvre pas tous les droits après fourniture. Les modèles détaillés Guild/TM Forum non consultés ne sont pas reconstitués. Les nouveaux appuis produits/unités et quotas éclairent les thèmes sans comparaison exhaustive des définitions de P81.
- Auteur/date/statut : Codex, 2026-09-11 ; lecture proposée, noms sourcés et adaptations non validées. P81 conserve dix domaines et 34 formulations ; registre des 36 CAP et couverture documentaire historique 16/20 inchangés.

### CMP038

- Éléments externes : ELM067 (distinction RBA/produit), ELM017/ELM032/ELM062 (protection et affectation) ; ELM063–ELM065 pour les noms anglais réemployés.
- Éléments locaux : U66/U67, F168–F171, A41, C48/C49 et P81 version 0.2 du 2026-09-11 ; D01 Inventory Management, D02.b Supply Protection et D02.e Supply Assignment. Voir la [carte courante](../connaissance/25-domaines-coeur-et-epreuve-recits.md) et les [correspondances des domaines](correspondances-domaines-coeur.md).
- Relation : réemploi lexical et appui sémantique pour des capacités métier ; correspondances partielles de contenu, sans équivalence de définitions complètes ni transfert automatique du niveau natif SAP.
- Adaptation : libellés de la carte en anglais selon U66, définitions en français ; Inventory Management adopté comme nom de D01. D02.b réemploie Supply Protection ; D02.e explicite Supply Assignment comme aptitude de couverture des demandes par des ressources présentes ou futures. Les 44 anciens libellés des dix domaines et 34 formulations sont conservés en C48. Les autres traductions locales restent proposées.
- Justification : U67 distingue les aptitudes de l’entreprise du mécanisme Allocation Run. Une documentation peut décrire leur réalisation sans fournir le rang exact de la capacité dans le catalogue RBA. La traduction conserve sens, résultats et limites ; elle ne réduit pas D10 à Pricing.
- Limites : le rattachement D02 et la frontière avec Reservation restent proposés. Affecter une ressource peut déjà l’engager ; affectation et réservation peuvent se révéler deux vues d’une même capacité selon les définitions retenues. Aucun objet, composant ou mécanisme unique imposé. La définition locale de Supply Assignment n’est pas une définition native RBA attestée ; les capacités correspondantes ne sont pas déclarées absentes de SAP.
- Auteur/date/statut : Codex, 2026-09-11. Nomenclature anglaise et nom Inventory Management demandés par Laurent ; nature métier de Supply Protection / Supply Assignment explicitée par Laurent en U67. Définitions détaillées, regroupements et équivalences restent à éprouver. P81 compte dix domaines et 35 formulations proposées ; les 36 CAP et leur couverture documentaire 16/20 restent inchangées.

### CMP039

- Éléments externes : ELM068 ; ELM014/ELM015 SAP, ELM024 ARTS et ELM066 Guild pour les preuves antérieures.
- Éléments locaux : U68/F172, A42, D01.a–d de P81 version 0.2 ; [fiche D01 dans la carte courante](../connaissance/25-domaines-coeur-et-epreuve-recits.md#d01-stocks). État comparé le 2026-09-11.
- Relation : rapprochements sémantiques de contenu ; Inventory Management est un nom commun réemployé, sans équivalence complète des périmètres. Les appuis produit ne sont pas présentés comme rangs natifs de capacités.
- Adaptation : ajout d’une Finalité proposée au domaine et d’une table capacité par capacité. D01.a rapproche quantités/états SAP et mesures/dimensions Microsoft ; D01.b rapproche mouvements et journaux ; D01.c rapproche la vue consolidée de Inventory Visibility, sans déduire une consolidation multisource SAP de simples listes ; D01.d rapproche Physical Inventory, Counting et Inventory adjustment. Aucun libellé ou définition des quatre capacités remplacés.
- Justification : mêmes problèmes de connaissance des stocks, de variation, de visibilité et d’écart, mais regroupements de marché différents. SAP détaille notamment les types de mouvements ; Microsoft expose une réalisation de visibilité multisource. Ces comparaisons ne prescrivent ni séparation en applications ni moteur unique.
- Autres références : TMF687 apporte une représentation du stock et des opérations d’ajustement, avec réservation qui déborde D01. ARTS 7.3 apporte un modèle de données de comptage/ajustement, pas des capacités. Asset Management dans le support Guild de 2019 est trop large pour établir une correspondance précise ; pas de capacité retail native inventée.
- Frontières : disponibilité par usage et engagements restent proposés en D02, promesse en D03 ; approvisionnement attendu distinct d’un stock reçu. D01 peut décrire le transit ou les biens chez un tiers sans prendre en charge leur déplacement. Valorisation financière en interface ; logistique hors développement FLOW, en adhérence.
- Auteur/date/statut : Codex, 2026-09-11 ; proposition de lecture pour revue par Laurent. Finalité et granularité restent à éprouver ; aucune équivalence validée. P81 conserve dix domaines et 35 formulations ; CAP historiques et couverture 16/20 inchangées.

**Précision de CMP039 après U69 — 2026-09-11 :** [C50](../connaissance/04-corrections.md#c50) clarifie la lecture locale sans changer les sources comparées. Physical Inventory / Counting appuient le rapprochement des constats et des positions en D01.d ; ils ne fondent pas une équivalence avec datahub ou golden data. La relation entre les résultats de D01.a et D01.b demeure à éprouver. Aucun libellé natif, nouvelle capacité ou équivalence ajouté ; pas de nouvelle vérification externe.

**Précision de CMP039 après U72 — 2026-09-11 :** la lecture métier de D01.d est explicitée autour de l’inventaire : constat de quantités, comparaison et régularisation des écarts. Physical Inventory est un nom proposé à partir du rapprochement déjà documenté ELM014/ELM068 ; aucune nouvelle équivalence, extension à tout rapprochement de données ou recherche externe.

### CMP040

- Éléments externes : ELM017/ELM028, reconsultés le 2026-09-11 après U74 ; ELM067 pour la distinction rang natif / aptitude métier. ELM068/CMP039 conservent les autres comparaisons de D01.
- Éléments locaux : U74/F178, A48/C51 et P81 version 0.3 ; Supply Protection rattachée à D01, avec repère historique D02.b conservé.
- Relation : appui sémantique pour la protection des ressources ; adaptation du rattachement local, aucune équivalence de hiérarchie externe ni de définition complète.
- Adaptation et justification : Inventory Management élargi à la maîtrise de la protection des stocks, selon l’orientation de Laurent. Protéger des usages sans modifier la quantité physique est un problème métier cohérent avec cette lecture. D02 prend en compte les protections dans disponibilité et engagements ; aucune fusion des domaines.
- Sources relues : [SAP Supply Protection](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-), Outline / Supply Protection Object / Core Supply Protection / Consuming Supply Protection, édition produit non précisée ; [Microsoft Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), présentation du pool virtuel, groupes et consommation, page évolutive sans release produit homogène établie. Textes ouverts et consultés ; ni activation ni configuration locale prouvées.
- Limites : le placement SAP dans la documentation aATP n’interdit pas le rattachement métier local à Inventory Management ; il ne le démontre pas non plus comme rang natif RBA. Microsoft allocation et SAP protection se recouvrent sans identité de toutes leurs règles. Nature, horizons, priorités et portée des ressources locales restent à préciser. Calcul amont de saison et logistique ne sont pas internalisés.
- Auteur/date/statut : Codex, 2026-09-11 ; rattachement local orienté explicitement par Laurent, autres définitions et frontières proposées. Dix domaines et 35 aptitudes conservés : cinq dans D01, quatre dans D02 ; 36 CAP historiques et couverture 16/20 inchangées.

### CMP041

- Éléments externes : ELM069, avec ELM031/ELM032/ELM067/ELM068 et les comparaisons CMP038–CMP040.
- Éléments locaux : U75/F179, A49/C52, TER016/TER021 et P81 version 0.4 ; réservation repère D02.c désormais en D01, Supply Assignment repère D02.e désormais en D03.
- Relation : adaptation de rattachement local et clarification sémantique ; rapprochements partiels de contenu, sans équivalence native de hiérarchie ni adoption des moyens techniques.
- Adaptation : réservation définie par l’engagement quantitatif pour un besoin et ses effets sur les usages concurrents ; affectation définie par la couverture ressource/demande. Microsoft Inventory Visibility reservations éclaire le premier résultat et le calcul de quantité encore réservable ; SAP Supply Assignment/aATP éclaire le second. La portée exacte du calcul de disponibilité reste en réexamen avec les capacités de visibilité et de faisabilité.
- Justification : Laurent distingue ces aptitudes et leurs domaines. Des représentations différentes du même stock ne créent pas de ressources supplémentaires ; physique, pools et projections doivent être distingués au sein de la proposition de regroupement, sans créer un domaine pour chaque représentation.
- Limites : cycles de réservation/affectation, autorité de modification et cardinalités locales non définis ; aucune partition rigide inventaire/ATP native affirmée. Un produit peut réaliser plusieurs capacités, un calcul peut servir plusieurs usages et une réservation peut accompagner une affectation. La suppression ou fusion de D02 n’est pas décidée.
- Auteur/date/statut : Codex, 2026-09-11 ; rattachements appliqués selon Laurent. Autres reformulations proposées. Dix domaines provisoires et 35 aptitudes conservés, dont D01 six, D02 deux et D03 quatre ; couverture historique CAP 16/20 inchangée.

- Précision U76/U77 du 2026-09-11 : la convention locale physique/logique/virtuel provient de Laurent, pas d’un catalogue externe. C53/TER040–TER042 corrigent la terminologie locale ; les mesures natives Microsoft et leur qualification physical/calculated ne constituent pas automatiquement des équivalents. Projection de promesse en D03 et disponible courant en D01 sont une proposition de partage ; aucun contenu externe nouveau ni nouvelle vérification.

### CMP042

- Éléments externes : ELM070 SAP Reservation/contrôle dynamique ; ELM071 Microsoft réservations ERP et Inventory Visibility ; ELM072 SAP quantités réservées par Supply Assignment.
- Éléments locaux : U78/F182, A52, C54 ; P81 version 0.4 D01 réservation (repère D02.c), D03 Supply Assignment (repère D02.e), TER016/TER017/TER040–TER042. [Analyse détaillée](allocation-reservation-sap-microsoft.md#réservation-et-frontière-inventory-management-order-promising-u78).
- Relation : recouvrements sémantiques et différences de mécanisme ; aucune équivalence complète, native ou de déploiement.
- Adaptation : conserver comme option Inventory Management pour engagement quantitatif et effets sur le stock, Order Promising pour couverture des demandes et promesses. Qualifier la possibilité que réservation et affectation soient deux faces d’un même engagement, sans duplication de quantités ni indépendance automatique de cycle.
- Justification : Microsoft réserve du présent et du commandé non reçu, avec précision progressive possible ; SAP distingue document de mouvement planifié et quantités réservées par Supply Assignment dans aATP. Le présent/futur ne suffit donc pas à placer les capacités. La source du calcul peut se situer dans plusieurs domaines selon le problème traité.
- Limites : il s’agit d’une option d’urbanisation locale, non d’une séparation universelle des éditeurs. Les règles de fermeté, replanification, annulation, consommation et autorités restent à éprouver sur les récits. L’hésitation U78 rouvre la question, sans supprimer l’orientation précédente ni changer les IDs.
- Auteur/date/statut : Codex, 2026-09-11 ; proposition et analyse documentaire. Le rattachement de réservation à D01 reste affiché mais en réexamen. Les dix domaines et 35 aptitudes de P81 ne sont pas promus ; CAP historiques et couverture 16/20 conservées.

### CMP043

- Éléments externes : [ELM073](elements.md#elm073), Microsoft accords, entrées futures/ATP et putaway ; [ELM074](elements.md#elm074), SAP réceptions futures pertinentes pour Supply Assignment.
- Éléments locaux : U79/F183/A53 ; P81 version 0.4, D01.a/D01.c, D03.a et Supply Assignment D02.e, D04.c, D07.d ; TER008/TER042/TER043. [Analyse dans la carte](../connaissance/25-domaines-coeur-et-epreuve-recits.md#stock-futur-potentiel-et-ressources-attendues-u79).
- Relation : appuis partiels sur les comportements ; aucune équivalence de domaines ou sous-capacités.
- Adaptation proposée : représenter séparément les quantités potentielles, planifiées, engagées et déjà physiques, avec destination et date attendues ; calculer ensuite leur contribution à la promesse selon les règles. La visibilité peut exposer ces informations sans prendre autorité sur contrats, achats ou faits logistiques.
- Justification : Microsoft distingue les variations futures du stock présent et décrit le solde d’accord séparément ; SAP cite plusieurs réceptions futures pour l’affectation. Représenter le futur et décider de son utilisation sont deux résultats à qualifier.
- Limites : gestion de tout potentiel contractuel comme stock affectable non démontrée par le marché. Frontière D01/D07 et fermeté du lien à la demande non arbitrées. État logistique, confirmation fournisseur et date utilisable ne sont pas interchangeables ; pas de transformation des étapes en sous-capacités.
- Auteur/date/statut : Codex, 2026-09-11 ; proposition d’analyse. Dix domaines et 35 aptitudes conservés, aucun rattachement modifié ni configuration installée attestée.

**Complément CMP043 — U80, 2026-09-11 :** la présence du stock futur dans D01 et D03 est désormais explicitée par Laurent, avec dépendance amont de la date de promesse. Cela précise le modèle local comparé ; la répartition détaillée connaissance/décision et les autorités demeurent proposées. Pas de nouvelle preuve externe ni équivalence native déduite.

**Complément CMP043 — U81, 2026-09-11 :** les définitions locales D01.a/b/c rendent explicites stock physique, états logiques et ressources futures ; D03.a explicite le calcul du stock virtuel puis la faisabilité quantité/date. C55 conserve les anciennes formulations. Les preuves ELM068 et ELM073/ELM074 servent d’appuis partiels déjà consultés ; la taxonomie physique/logique/virtuel et cette répartition sont locales. Aucun rapprochement complet de ces nouvelles formulations avec un catalogue natif ni nouvelle vérification externe effectué. Ce complément actualise la portée de comparaison, sans élargir les preuves ni valider une équivalence.

### CMP044

- Éléments externes : [ELM075](elements.md#elm075), SAP quantités et stock-taking ; [ELM076](elements.md#elm076), Microsoft on-hand, Maintain inventory levels, Count inventory et Counting.
- Éléments locaux : U82/F186/A56/C56 ; P81 version 0.4 D01.a et D01.d, définitions précisées après U81. [Revue des noms](../connaissance/25-domaines-coeur-et-epreuve-recits.md#noms-des-capacités-de-stock-revue-u82).
- Relation : vocabulaire et recouvrements partiels, sans équivalence de niveaux ni de capacités complètes.
- Adaptation proposée : D01.a Manage inventory quantities, nom local inspiré de Managing Stocks by Quantity ; D01.d Count and reconcile inventory, avec Stocktaking comme forme courte à examiner. Les noms des tables principales sont conservés pendant la revue ; aucune nouvelle capacité créée.
- Justification : quantités et états courants se distinguent du constat de comptage et de l’établissement des corrections. Truth est trop absolu et peu délimité pour le résultat ; Inventory accuracy exprime la finalité. Inventory Accuracy Assurance serait une formulation locale de portée plus large à définir, pas un nom natif établi.
- Limites : le nom de D01.a ne résout pas son chevauchement avec D01.b ; le comptage physique reste en adhérence logistique. Stocktaking ne doit pas masquer le rapprochement et la correction qui sont dans la définition courante. Décompte/constat, rapprochement et ajustement peuvent être réalisés différemment sans changer l’aptitude métier.
- Auteur/date/statut : Codex, 2026-09-11 ; propositions de nomenclature à discuter avec Laurent, pas de renommage adopté. P81 dix domaines/35 aptitudes et CAP36 conservés.

### CMP045

- Éléments locaux : U83/F187/A57 ; [P82](../connaissance/05-propositions.md#p82), alternative de cinq capacités D01 aux six capacités actuelles P81 version 0.4.
- Éléments externes : ELM068/ELM075/ELM076 pour stocks et comptage ; ELM017/ELM028 et CMP040 pour protection ; ELM070/ELM071/ELM072 et CMP042 pour réservation. Preuves déjà consultées, dont recherche U82 du 2026-09-11 ; pas de nouvelle vérification en U83.
- Inventory Tracking : proposition locale réunissant D01.a/b, appui partiel SAP Managing Stocks by Quantity incluant transactions et mises à jour. Microsoft On-hand inventory expose quantités et états actualisés ; aucun libellé natif exact Inventory Tracking ni équivalence de périmètre complet établis.
- Inventory Visibility : réemploi du nom de produit Microsoft pour une aptitude locale de visibilité ; ELM068. Le produit couvre aussi d’autres comportements, donc pas d’équivalence produit/capacité.
- Stocktaking : vocabulaire explicite SAP, rapproché de Count inventory et Counting Microsoft ; ELM075/ELM076. La définition locale inclut qualification des écarts et corrections ; aucune feuille native de ce périmètre exact sous ce nom prouvée.
- Supply Protection : libellé conservé et rapprochement CMP040 ; Inventory Reservation : titre abrégé local éclairé par CMP042, sans séparation absolue vis-à-vis de Supply Assignment.
- Adaptation et justification : fusion proposée de l’état et de son évolution ; titres courts, définitions actives et Finalité distincte. Inventory accuracy reste la finalité du rapprochement, pas une garantie de vérité absolue.
- Limites : aucun catalogue externe ne valide l’ensemble des cinq capacités ni les frontières D01/D03/D07. Les sources de produit éclairent les aptitudes ; on ne transforme pas leurs workflows en capacités ou développements FLOW. Réservation et visibilité gardent leurs limites de frontière.
- Auteur/date/statut : Codex, 2026-09-11 ; alternative proposée, non adoptée. P81 dix domaines/35 aptitudes et CAP36 inchangés ; pas de nouvel identifiant de capacité ni réutilisation.

**Complément CMP045 — U84, 2026-09-11 :** Reservation est le nom local adopté par Laurent ; Counting est proposé à la place de Stocktaking, dont le périmètre de comptage/rapprochement/correction est conservé. Microsoft Counting reconsulté en ELM076. Le changement des titres ne modifie pas les limites des correspondances ni les frontières. La fusion D01.a/b reste proposée ; noms antérieurs conservés en C57.

**Réexamen CMP045 — U85, 2026-09-11 :** le nom Stocktaking est de nouveau envisagé aux côtés de Counting. L’indépendance des outils vaut pour les deux aptitudes ; leur portée évoquée diffère selon A59. Aucune nouvelle preuve externe, changement de périmètre ou équivalence native déduite.

**Décision locale CMP045 — U86, 2026-09-11 :** Laurent adopte Stocktaking pour D01.d et la capacité correspondante P82, avec Inventory accuracy comme Finalité. Noms antérieurs en C58 ; définition de comptage/rapprochement/correction conservée. ELM075/ELM076 et les limites des correspondances restent applicables, sans équivalence supplémentaire ni changement des termes natifs SAP/Microsoft. Pas de nouvelle vérification externe pour appliquer ce choix local.

### CMP046

- Éléments externes : [ELM077](elements.md#elm077), contrôle SAP PAC/BOP et Microsoft promesse/réservations ; ELM014/ELM067 pour les rangs RBA précédemment examinés.
- Éléments locaux : U87/U88, F191/F192/A61 ; P83, D02.a/d et D01/D03 de P81 après U86. [Audit](../audits/2026-09-11-order-promising.md).
- Relation : recouvrement partiel et appui de vocabulaire ; aucune équivalence complète de domaines ou de hiérarchie.
- Adaptation : la disponibilité de promesse rejoint conceptuellement la faisabilité D03 ; réviser/libérer relève des capacités sur les objets concernés. Vue D03 proposée Supply Feasibility, Confirmation, Supply Assignment, Promise Revision ; noms locaux sauf réemploi Supply Assignment, sans rang natif supplémentaire affirmé.
- Justification : SAP lie PAC à la confirmation et réexamine avec BOP après annulation, retard ou priorité ; Microsoft situe ajustement/libération dans le cycle de réservation et combine disponibilité et dates dans Order promising. La séparation locale des résultats n’impose pas des étapes ou composants indépendants.
- Limites : les sources ne démontrent pas qu’un domaine D02 est absent de tous les modèles. Les règles du produit et CTP ne deviennent pas des capacités FLOW par copie. Le périmètre exact des autorités et engagements modifiables reste localement inconnu.
- Auteur/date/statut : Codex, 2026-09-11 ; analyse et proposition, non validées. D02 n’est pas supprimé, D03 n’est pas renuméroté ; CAP historiques inchangées.

### CMP047

- Éléments externes : ELM078–ELM081 ; appuis antérieurs ELM071/ELM072/ELM077 pour réservation/affectation. MKT04/MKT13/MKT14/MKT20, dates et limites détaillées dans ces notices.
- Éléments locaux : U89/F193/A62 ; P83 après U88, quatre capacités D03, et frontières D01/D04/D06/D07/D08 de P81 version 0.4.
- Relation : recouvrements partiels, appuis sémantiques et écarts de précision ; aucune équivalence complète ni même maille présumée. [Comparaison noms, nature et couverture](order-promising-comparaison-capacites.md).
- Adaptation proposée : conserver provisoirement les quatre hypothèses, éprouver leurs définitions par dix critères explicités. Quatre résultats explicites, quatre points partiels, deux non décrits ; pas dix capacités recommandées ni pourcentage de couverture du marché. Examiner prioritairement allocations consommables, lieu, substitution et approvisionnement à créer.
- Justification : les cinq feuilles de l’extrait SAP organisent autrement les problèmes ; Microsoft et Oracle apportent aussi des alternatives. Le corpus public Guild/TM Forum ne permet pas un comptage natif comparable sur ce domaine.
- Limites : nature de contribution proposée, noms locaux non adoptés ; frontières avec D06 et autonomie C-Log conservées. Le produit ne prouve ni besoin local ni réalisation installée. La confirmation autonome et sa séparation avec la révision restent à éprouver.
- Auteur/date/statut : Codex, 2026-09-11 ; comparaison préalable, non validée. Aucun changement de nombre, de définition ou de rattachement appliqué aux capacités.

### CMP048

- Éléments externes : ELM082/MKT21, appui lexical APICS ; ELM077/ELM080 pour l’emploi éditeur d’ATP/CTP. Source APICS vérifiée le 2026-09-11, sources éditeurs déjà examinées en U89.
- Éléments locaux : U90/F194/A63/C59 ; P83 et vue D03 après U90. Relation : appui sémantique, recouvrement partiel, aucun libellé natif identique établi pour les deux nouveaux candidats.
- Adaptation : Promise Verification remplace Supply Feasibility dans la vue proposée ; Promise Confirmation précise Confirmation. Vérification d’une possibilité avant engagement, confirmation de l’engagement, affectation des ressources et révision distinguées. Les premiers noms restent historiques dans l’étude U89.
- Justification : la promesse est le résultat fédérateur ; ATP est un vocabulaire métier attesté au-delà des éditeurs. Les alternatives, contrôles d’allocation et créations de fourniture demeurent à expliciter dans la couverture.
- Limites : ATP seul ne couvre pas toute la faisabilité ; Promise Verification peut évoquer une promesse existante, d’où sa définition nécessaire. Promise Confirmation n’est pas l’équivalent de Product Allocation Check. Aucun objet Promise unique, découpage IT ou ordre obligatoire confirmation/affectation.
- Auteur/date/statut : Codex, 2026-09-11 ; propositions lexicales de Laurent consignées, appréciation favorable de Supply Assignment et Promise Revision ; définitions détaillées et couverture non validées.

### CMP049

- Éléments externes : ELM078/ELM079 SAP RBA et produit ; ELM080 Microsoft, ELM081 Oracle, preuves du 2026-09-11 déjà consultées. Pas de nouvelle vérification externe après U91/U92.
- Éléments locaux : U91/U92/F195/F196/A64/C60 ; P83 après la correction du nom de première capacité.
- Relation : adaptation de noms et recouvrements partiels ; les noms anglais avec Decision sont locaux, pas feuilles SAP natives.
- Adaptation : ajout exploratoire de Allocation Eligibility Decision, Fulfillment Source Decision, Product Substitution Decision et Supply Creation Decision ; D03 proposé comme propriétaire de ces décisions qualifiées pour une promesse, avec fournisseurs de connaissances/contraintes D01/D06/D08 et engagements D04/D07. SAP Product Allocation Check, Fulfillment Location Determination, Product Substitution et Supply Creation Based Confirmation sont les appuis respectifs ; leurs définitions natives détaillées n’étant pas toutes disponibles, les relations demeurent partielles.
- Promise Formulation : nom proposé pour construire une proposition ; ATP peut contribuer à son calcul, sans équivalence de périmètre. Promise Verification rejeté par Laurent ; historique CMP048 conservé.
- Justification/limites : faire naître une promesse et rendre visibles ses décisions, tout en conservant la capacité de confirmation. Une décision à prendre, sa réalisation technique et l’autorité opérationnelle sont distinctes. Propriétaires et maille proposés, pas transfert C-Log ni quatre domaines logiciels supplémentaires. Les écarts U89 ne sont pas clos par de simples noms.
- Auteur/date/statut : Codex, 2026-09-11 ; ajouts à l’exploration demandés par Laurent, rattachements et noms proposés. P81 et CAP historiques inchangés.

### CMP050

- Éléments externes : ELM083 ; SAP Transportation Management pour la chaîne de transport, Microsoft et Oracle pour l’effet des options de transport sur la promesse. Vérification du 2026-09-11 ; éditions et limites dans ELM083.
- Éléments locaux : U93/F197/F198/A65/C61 ; P83, D03 et frontières D06/D07. Relation : recouvrement partiel et adaptation de vocabulaire, pas équivalence de domaines.
- Adaptation : ajouter Fulfillment Route Decision au-delà de Fulfillment Source Decision. D03 proposé pour le choix de la chaîne supportant la promesse ; possibilités qualifiées en D06, engagements utiles en D07. La construction et la planification détaillée de transport, rapprochées de Transportation Management, restent en adhérence avec leurs autorités. Pas de compétence C-Log transférée par le rattachement au domaine.
- Justification : disponibilité à la source et faisabilité d’acheminement ne sont pas synonymes. Une promesse de livraison dépend d’une solution réalisable jusqu’au destinataire ; les décisions peuvent être interdépendantes sans fusion des domaines.
- Nom de la première capacité : Promise Proposal remplace le candidat rejeté Promise Formulation. Adaptation locale proposée par Laurent ; pas de libellé natif équivalent vérifié, ni changement d’objet ou de caractère engageant décidé par le seul nom.
- Auteur/date/statut : Codex, 2026-09-11 ; candidats de nom et de rattachement, granularité à éprouver. Couverture enrichie au niveau du problème, pas audit de réalisation ; P81 historique et CAP36 conservés.

### CMP051

- Éléments externes : ELM084/MKT14, vérification Microsoft du 2026-09-11 ; ELM082/APICS demeure un appui historique distinct.
- Éléments locaux : U94/F199/A66 ; P83, Promise Proposal et Supply Creation Decision, ressources futures U79/U80 et TER044.
- Relation : recouvrement partiel et appui sémantique. ATP soutient la promesse par les ressources présentes/attendues disponibles ; CTP élargit la faisabilité aux moyens de produire ou approvisionner ce qui manque. Leurs réalisations peuvent lier calcul et confirmation ; pas d’équivalence automatique avec nos frontières de capacité.
- Adaptation proposée : documenter ces deux modes de raisonnement dans Promise Proposal ; mobiliser les aptitudes de décision et connaissances nécessaires, sans créer une capacité ATP et une capacité CTP par simple copie d’options produit.
- Limites : ATP comprend du futur ; CTP n’est pas synonyme de réservation future, de Supply Assignment ou de réaffectation prioritaire. Une quantité potentiellement achetable sous contrat ne devient pas promettable sans conditions de fourniture. Calendriers et transport concernent les deux raisonnements. Les capacités au sens ressources de production ne sont pas les Business Capabilities de notre carte.
- Auteur/date/statut : Codex, 2026-09-11 ; analyse non adoptée ; aucune modification du nombre de capacités ou de leur périmètre. C62 précise les variantes techniques et les limites des pages Microsoft.

### CMP052

- Sources externes : ELM077–ELM084 et CMP047–CMP051 déjà examinés ; aucune nouvelle vérification externe pour appliquer U95.
- Éléments locaux : U95/F200/F201/A67/C63 ; P83 validée, P81 version 0.5, neuf capacités d’Order Promising.
- Validation locale : **Laurent, 2026-09-11**, quatre capacités d’action et cinq capacités de décision. Anciennes correspondances de noms préservées ; D03.a Promise Proposal, D03.b Promise Confirmation, D03.c Promise Revision et D02.e Supply Assignment gardent leurs repères.
- Nouveaux repères locaux : D03.d Allocation Eligibility Decision, appui partiel SAP Product Allocation Check ; D03.e Fulfillment Source Decision, SAP Fulfillment Location Determination et alternatives Microsoft/Oracle ; D03.f Fulfillment Route Decision, transport et promesse ELM083 ; D03.g Product Substitution Decision, appuis partiels SAP/Oracle et variantes Microsoft ; D03.h Supply Creation Decision, SAP Supply Creation Based Confirmation et comportements de fourniture nouvelle documentés.
- Relation : adaptations locales et recouvrements partiels, pas équivalences validées. L’accord métier ne transforme pas ces noms en feuilles natives ni ne prouve toutes leurs règles ou une couverture exhaustive.
- ATP/CTP : ATP retenu dans la promesse. CTP reste documenté au glossaire mais son placement local est différé ; hypothèse analytics/planification/protection non adoptée. CMP051 conserve la définition Microsoft, sans imposer son implantation locale. Supply Creation Decision demeure dans la liste validée ; aucun lien CTP obligatoire.
- Limites : autorités opérationnelles et frontières D01/D06/D07 encore à préciser ; pas de transfert C-Log ni extension du périmètre de développement logistique. Aucun retrait D02 ni reclassement du registre CAP36.
- Auteur/date : Codex, 2026-09-11 ; enregistrement d’une validation locale explicite et actualisation des correspondances.

### CMP053

- Éléments externes : ELM085/ELM086, vérification SAP/Microsoft du 2026-09-11 ; ELM043/ELM063/ELM064/ELM065 comme appuis antérieurs de sous-traitance, commandes et composants TM Forum.
- Éléments locaux : U96/F202/A68/P84 ; D04.a–d de P81 version 0.5 ; récits U48/U53, Q034/Q069 et frontière avec D03 validé.
- Relation : recouvrements partiels et adaptations de vocabulaire. Commitment Creation/Revision rapprochés des accords/commandes et versions ; Commitment Reconciliation rapproché du suivi de consommation et reliquat ; Return and Replacement Decision rapproché des droits et suites des retours. Les quatre noms sont locaux et proposés, pas des feuilles SAP ou Microsoft exactes.
- Justification : achats et ventes présentent des problèmes communs d’obligation, de changement et de rapprochement, sans prouver un domaine natif unifié. Le contexte d’une réalisation reste essentiel pour savoir à quelle obligation l’imputer. Création d’une commande, réception, facturation et consommation d’un accord-cadre ne sont pas des événements interchangeables.
- Adaptation proposée : conserver la vue commune comme hypothèse, éprouver sa frontière avec des domaines achats/ventes spécialisés ; garder les quatre aptitudes initiales pour une première revue. Décisions d’acceptation et retours à clarifier, sans multiplication de capacités par défaut.
- Limites : aucune adoption de nom, frontière ou nombre ; dossier OMS et engagement commercial distincts. Le produit décrit des pratiques possibles, pas une configuration locale ni une règle juridique générale. Finance et réalisation logistique exclues des développements de cette vue ; CTP reste différé.
- Auteur/date/statut : Codex, 2026-09-11 ; première proposition D04 non validée, D03 inchangé.

### CMP054

- Éléments locaux : U97/U98, F203–F208, A69/C64/P85 ; P81 version 0.6. Trois domaines contigus, une ingestion chacun : D09 Party / Role, D11 Agreement, D12 Catalog. Commandes distinctes des Agreements ; D04 reste proposé pour leurs engagements.
- Corpus externe déjà consulté : ELM063/ELM064/ELM065/ELM066 et ELM085/ELM086. Aucune nouvelle vérification externe ; correction du périmètre local, pas nouvel arbitrage sur le contenu des catalogues de marché.
- Relation : rapprochements sémantiques partiels avec Business Partner / Party et rôles, accords clients/fournisseurs et catalogues. Les fonctionnalités de gestion complète de ces objets chez les éditeurs sont plus larges que notre consommation de références externes. Party / Role Ingestion, Agreement Ingestion et Catalog Ingestion sont des libellés locaux ; leur équivalence à des feuilles de capacité natives n’est pas établie.
- Correction de CMP053 : les fonctions de création, révision et consommation des Sales/Purchase agreements Microsoft éclairent le contrat de référence. Elles ne justifient pas de créer ou modifier ces contrats dans D04. Sales/Purchase Order Management et retours restent des appuis partiels pour les commandes transactionnelles. Agreement Management TM Forum est rapproché de D11 ; composants et capacités restent distincts.
- Adaptation : retirer D08.a–c, D09.a–c et D10.a–c de la vue plateforme et conserver leur historique. D04.a–d sont recentrées sur les commandes. Les conditions reçues sont appliquées par les domaines consommateurs, dont les neuf capacités validées d’Order Promising ; elles ne créent pas une capacité de vérification des références.
- Limites : Catalog ne désigne pas tout Product Information Management. Origines des caractéristiques, unités et conditionnements encore à préciser. Aucun contrat d’intégration, source logicielle installée, cardinalité détaillée ou équivalence complète n’est déduit. Le domaine commun de commandes D04 reste à éprouver.
- Auteur/date/statut : Codex, 2026-09-11 ; instruction de périmètre et distinction commandes/Agreements explicites de Laurent appliquées. Correspondances marché partielles, à approfondir pour les trois ingestions.

### CMP055

- Objet : Achat/vente selon l’objet.
- Éléments externes : ELM087–ELM090, ELM096/ELM097.
- État local : U99/F209/A70/C65/P86, P81 version 0.6, dix domaines et 34 capacités.
- Relation : Appui sémantique et recouvrements partiels. Identité Party commune, variantes de contrats et commandes spécialisées dans les suites ; ODA Agreement transversal. Les processus/modules ne valent pas domaines de capacités.
- Adaptation proposée : P86 : conserver les trois ingestions avec variantes ; éprouver un ou deux domaines de commandes, sans scission automatique.
- Preuve et limites : [audit complet](../audits/2026-09-11-modele-marche-achats-ventes-referentiels.md). Les notices de composants et documentations produit ne sont pas un catalogue retail homogène ; aucune configuration installée déduite.
- Auteur/date/statut : Codex, 2026-09-11 ; audit et propositions, aucune validation supplémentaire de Laurent.

### CMP056

- Objet : Références produit, catalogue et prix.
- Éléments externes : ELM088, ELM090–ELM097.
- État local : U99/F209/A70/C65/P86, P81 version 0.6, dix domaines et 34 capacités.
- Relation : Tripartition exhaustive non démontrée. Catalogue et produit distincts ; données tarifaires séparables mais pas toujours en domaine autonome. Application du prix, consommé contractuel et information fournisseur/article ne se déduisent pas d’une ingestion.
- Adaptation proposée : P86 AC01–AC08 : préciser réception produit, autorités du prix et du consommé, usages des références. Maîtrise externe conservée ; aucun nouveau domaine ou capacité actif.
- Preuve et limites : [audit complet](../audits/2026-09-11-modele-marche-achats-ventes-referentiels.md). Les notices de composants et documentations produit ne sont pas un catalogue retail homogène ; aucune configuration installée déduite.
- Auteur/date/statut : Codex, 2026-09-11 ; audit et propositions, aucune validation supplémentaire de Laurent.

### CMP057

- Objet : Revue des 34 capacités et doublons.
- Éléments externes : ELM089/ELM091–ELM098 ; corpus antérieur ELM014, ELM063–ELM083 qualifié dans l’audit.
- État local : U99/F209/A70/C65/P86, P81 version 0.6, dix domaines et 34 capacités.
- Relation : 34 repères revus, sans equivalence complète de capacité revendiquée. Recouvrements D02.a/d avec D01/D03 ; fusion D01.a/b proposée ; titres D04 trop génériques, frontières D06/D07 incomplètes.
- Adaptation proposée : P86 : propositions de noms courts et de répartition, neuf pistes AC non additives. D03 reste validé ; détails et autorités ouverts. API, moteurs, onboarding, finance et exécution logistique ne deviennent pas des ajouts FLOW.
- Preuve et limites : [audit complet](../audits/2026-09-11-modele-marche-achats-ventes-referentiels.md). Les notices de composants et documentations produit ne sont pas un catalogue retail homogène ; aucune configuration installée déduite.
- Auteur/date/statut : Codex, 2026-09-11 ; audit et propositions, aucune validation supplémentaire de Laurent.

### CMP058

- Éléments locaux : U100/F210–F212, A71/C66 ; P81 0.7, onze domaines et 35 capacités. Autonomie article confirmée ; nom Product Reference et D08.d Product Reference Ingestion proposés pour l’appliquer.
- Corpus déjà examiné : ELM089/ELM098 pour commandes et retours, ELM087/ELM095 pour parties et lieux, ELM090/ELM091 pour produit et catalogue. Consultation du corpus U99 datée du 2026-09-11 ; pas de nouvelle vérification externe dans cette mise à jour.
- Relation : appui partiel à la distinction produit/catalogue ; Product Reference Ingestion n’est pas une feuille native de capacités attestée. Le périmètre local de réception est plus étroit que la maîtrise produit des solutions.
- Adaptation : réactiver D08 pour le même sujet article avec une nouvelle capacité D08.d, sans restaurer D08.a–c. Lire les variantes Purchase/Sales/Return comme cas de couverture du socle générique, pas comme prescription de domaines locaux séparés.
- Limite majeure : aucune équivalence précise de marché encore établie pour l’ensemble du modèle de documents comme preuves d’autorisation de mouvement. Ne pas présenter les commandes éditeur comme universellement suffisantes pour autoriser la logistique, ni DMN comme modèle de capacités. Autorisation, acceptation d’exécution et fait réel restent distingués dans la proposition locale.
- Auteur/date/statut : Codex, 2026-09-11 ; orientation Laurent appliquée, raffinements et frontières D04/D07 proposés. [Note de référence](../connaissance/26-supply-documents-autorisations.md). D03 validé, CTP différé, logistique hors développement FLOW.

### CMP059

- État local : U101/F213/A72/C67/P87 ; P81 0.7, onze domaines et 35 aptitudes inchangés.
- Sources : ELM099–ELM102, consultation 2026-09-11 ; MKT22 ajouté pour MDG, autres éditions détaillées dans les éléments.
- Relation : appuis structurels et méthodologiques partiels, pas équivalence. Le regroupement de la gestion des données chez SAP, la catégorie Microsoft, les blocs ODA et la décomposition Guild ne décrivent pas le même objet.
- Adaptation proposée : groupe visuel Business References, conservant D09/D11/D08/D12 et leurs quatre ingestions ; modèles et autorités distincts. Alternative de domaine commun explicitée mais non appliquée.
- Justification : le périmètre de la plateforme est la réception des références, avec maîtrise externe. L’autonomie sémantique n’impose ni rang de domaine au premier niveau ni réalisation séparée.
- Limites : nom et regroupement locaux non validés ; aucune hiérarchie RBA vérifiée par MDG, aucun schéma universel de référentiels établi. Capacités de gouvernance produit et processus externes non importés.
- Auteur/date/statut : Codex, 2026-09-11 ; [étude ciblée](regroupement-referentiels.md), décision ouverte Q075.

### CMP060

- État local : U102/F214/A73/C68 ; P81 0.8 ; D13 Fulfillment Network et D13.a Fulfillment Network Ingestion proposés pour expliciter le référentiel demandé. Douze repères de domaines, 36 aptitudes ; rang de regroupement ouvert.
- Corpus déjà consulté : ELM095 pour les sites SAP, ELM098 pour les règles de lieux/charge Microsoft, ELM065/ELM096 pour les repères ODA dont Location Management. Aucune nouvelle consultation externe dans cette mise à jour.
- Relation : appuis partiels sur lieux et contraintes d’exécution. La correspondance précise de Fulfillment Network, incluant les relations entre points et les autorités, reste **non comparée**. Aucun nom ni niveau natif SAP/Microsoft/TM Forum affirmé pour D13 ou son ingestion.
- Adaptation : expliciter la réception des références réseau, distincte des parties ; préserver l’appréciation contextuelle en D06, les décisions D03 et les engagements/faits D07. Les nœuds, liaisons et caractéristiques détaillés sont des propositions locales.
- Limites : recevoir une topologie ne signifie ni concevoir le réseau, ni piloter le transport, ni développer la logistique dans FLOW. Maîtres et attributs ouverts INF22/Q076 ; pas de référentiel universel démontré.
- Auteur/date/statut : Codex, 2026-09-11 ; orientation Laurent appliquée, modèle détaillé et rang proposés. [Vue D13](../connaissance/25-domaines-coeur-et-epreuve-recits.md#d13-fulfillment-network).

### CMP061

- État local : U103/F215/A74/C69 ; P87 retenue sur la présentation ; P81 0.9.
- Corpus : ELM099–ELM102 et CMP059 pour les distinctions de niveaux ; CMP060 pour le réseau encore partiellement comparé. Aucune nouvelle consultation externe.
- Adaptation appliquée : Business References présenté comme groupe de cinq références autonomes ; sept domaines transactionnels de travail visibles à côté. Douze repères détaillés et 36 aptitudes conservés.
- Relation et limites : le regroupement est local, pas un domaine natif SAP, Microsoft, Guild ou TM Forum. L’accord ne valide pas de nouvelles équivalences, les maîtres ni le modèle détaillé du réseau ; il ne fusionne pas les capacités.
- Auteur/date/statut : Codex, 2026-09-11 ; application de l’accord contextuel de Laurent Go en U103, portée explicitée en F215 ; Q075 résolue, Q076 ouverte.

# Noms de marché proches des domaines cœur

11 septembre 2026 — vue locale actualisée après U100, [P81 version 0.7](../connaissance/25-domaines-coeur-et-epreuve-recits.md), onze domaines actifs. Corpus issu de U65/CMP037 et des approfondissements ultérieurs ; [CMP054](comparaisons.md#cmp054) corrige les frontières de référence. **Les noms externes sont des repères attestés dans le corpus ; les correspondances sont partielles.** Les quatre domaines Party / Role, Agreement, Product Reference et Catalog ne portent localement que l’ingestion. D08.d est une proposition de formulation appliquant l’autonomie article confirmée en U100. Les fonctionnalités de maîtrise décrites par le marché restent externes à la plateforme.

## SAP et Microsoft

Les intitulés anglais permettent de retrouver les références natives. **Aire RBA** signifie Business Area ; **capacité RBA**, Business Capability. Les autres noms SAP ci-dessous viennent de la documentation de produit. Côté Microsoft, les aires de processus et les fonctionnalités de produit sont distinguées. Le tableau ne juxtapose donc pas des niveaux supposés identiques.

| Domaine de P81 | Noms proches chez SAP | Noms proches chez Microsoft Dynamics 365 |
| --- | --- | --- |
| **D01 — Inventory Management** | **Inventory Management** — aire RBA ; **Supply Protection** — aptitude éclairée par la documentation aATP, rattachée localement à D01 après U74. | **Inventory management** — périmètre produit ; **Inventory Visibility inventory allocation** pour les protections et **Inventory Visibility reservations** pour la réservation ; **Maintain inventory levels** — aire de processus plus large. |
| **D02 — Resource Availability and Commitments** | **Product Availability Check**, **Product Allocation Check** — capacités RBA sous Order Promising ; Dispositions relatives aux disponibilités et à la révision des engagements : D02 en réexamen après U75. | Mesures calculées de disponibilité ; les réservations sont désormais rapprochées de D01. D02 ne désigne pas un équivalent autonome établi. |
| **D03 — Order Promising** | **Order Promising** — aire RBA ; **Available-to-Promise**, **Backorder Processing**, **Supply Assignment** — fonctionnalités de produit éclairant les aptitudes locales ; affectation rattachée à D03 en U75. | **Order promising** — fonctionnalité citée dans Manage sales orders ; **Calculate sales order delivery dates** — fonction de calcul. |
| **D04 — Commercial Commitments** | **Sales Order Management** + **Purchase Order Management** — périmètres fonctionnels de produit. | **Manage sales orders** + **Procure goods and services** — aires de processus, plus larges que les engagements transactionnels des commandes. |
| **D05 — Operational Resource Balancing** | **Replenishment Planning** — réassort Retail ; **Supply Chain Planning** est un voisin plus large, Business Domain RBA. | **Maintain inventory levels** — aire de processus incluant politiques, seuils et plans de réapprovisionnement. |
| **D06 — Execution Options** | **Plant Determination**, **Alternative-Based Confirmation (ABC)** — fonctions de sélection d’origines et d’alternatives, rapprochement partiel. | **Distributed order management (DOM)**, notamment **Fulfillment location priority rule**, **Offline fulfillment location rule**, **Maximum orders rule** — fonctionnalités et règles produit. |
| **D07 — Execution Commitments and Facts** | **Delivery Processing**, **Inbound Delivery**, **Outbound Delivery** — traitements et documents logistiques, recouvrement partiel. | **Process inbound goods**, **Process outbound goods** — aires de processus ; **Store order fulfillment** — périmètre produit. |
| **D09 — Party / Role** | **Business Partner**, **Business Partner Roles** — objets et rôles. | **Global address book**, **Party**, **Party roles** — référentiel et concepts ; ingestion seule localement. |
| **D11 — Agreement** | Contrats et conditions : rapprochement exact au périmètre local à approfondir. | **Sales agreements**, **Purchase agreements** — objets et fonctionnalités produit, plus larges que l’ingestion locale. |
| **D08 — Product Reference** | **Product Master**, **Retail Article Master** — objets et périmètres plus larges que notre réception de références. | **Product information management** — périmètre produit plus large ; réception de données externes examinée ELM091. D08.d est une formulation locale, CMP058. |
| **D12 — Catalog** | Catalogues d’achat examinés ELM090 ; contexte d’achats indirects à distinguer du commerce de marchandises. | Catalogues d’approvisionnement et catalogues B2B examinés ELM090 ; rapprochements partiels, distincts du référentiel produit D08. |

Sources, passages, accès et dates : [ELM063 — SAP](elements.md#elm063), [ELM064 — Microsoft](elements.md#elm064). Les noms D04 et D07 relient plusieurs rubriques externes ; ils ne désignent pas un domaine commun attesté chez les éditeurs. L’application des droits après fourniture aux commandes reste insuffisamment comparée ; Pricing ne suffit pas à la couvrir.

## TM Forum

Les noms ci-dessous proviennent de **composants ODA** ou d’**API**. Ils fournissent des repères terminologiques et des périmètres à comparer ; ce ne sont pas les entrées d’un catalogue de capacités retail. Les notices publiques et leurs versions sont qualifiées dans [ELM065](elements.md#elm065).

| Domaine de P81 | Noms proches attestés | Portée du rapprochement |
| --- | --- | --- |
| **D01 — Inventory Management** | **Stock Management** — API TMF687 ; **Resource Inventory** — composant TMFC012. | TMF687 est le repère le plus direct sur quantités et positions, avec réservation ; TMF716 Resource Reservation apporte un rapprochement partiel de la réservation rattachée en U75. Resource Inventory n’est pas entièrement comparé ici. |
| **D02 — Resource Availability and Commitments** | **Stock Management** — TMF687 ; **Resource Reservation** — TMF716. | D02 en réexamen ; la réservation TMF687/TMF716 est maintenant rapprochée de D01. Pas d’équivalence autonome établie pour les deux aptitudes restant dans D02. |
| **D03 — Order Promising** | **Service Qualification Management** — TMFC009. | Analogie limitée à la faisabilité et à une date calculée. La qualification n’alloue pas de ressources ; confirmation ferme et réexamen non démontrés. |
| **D04 — Commercial Commitments** | **Product Order Capture & Validation** — TMFC002 ; **Purchase Management** — TMFC033. | Repères de commandes et achats identifiés dans l’annuaire ; détails non analysés. Agreement Management est rapproché de D11 après U98. |
| **D05 — Operational Resource Balancing** | **Supply Chain Management** — TMFC032 ; **Stock Management** — TMF687. | TMFC032 est seulement un voisin plus large ; les seuils de TMF687 ne prouvent pas un domaine complet de calcul du besoin net et de redistribution. |
| **D06 — Execution Options** | **Service Qualification Management** — TMFC009 ; **Location Management** — TMFC014. | Faisabilité et lieux ; capacité et quota de préparation magasin non équivalents établis. |
| **D07 — Execution Commitments and Facts** | **Service Order Management** — TMFC007 ; **Resource Order Management** — TMFC011. | Commandes et orchestration de réalisation, avec une portée propre aux services et ressources télécom ; pas de domaine générique des faits démontré. |
| **D09 — Party / Role** | **Party Management** — TMFC028 ; **Party Role Management** — TMF669. | Proximité sur identités et rôles ; gestion native plus large que l’ingestion locale. |
| **D11 — Agreement** | **Agreement Management** — TMFC039. | Contrats de référence ; composant plus large que l’ingestion locale, distinct des commandes. |
| **D12 — Catalog** | **Product Catalog Management** — TMFC001 ; **Resource Catalog Management** — TMFC010. | Offres et spécifications différenciées ; pas d’équivalence complète au catalogue retail ingéré. |

**Faux ami à éviter : Product Inventory.** TMFC005 décrit les produits attribués à des parties ou utilisés par elles. Son libellé ne doit pas remplacer Inventory Management pour désigner notre stock de marchandises ; TMF687 Stock Management est plus pertinent dans cette comparaison.

## BIZBOK / Business Architecture Guild

L’atelier public **Government Reference Model Workshop du 21 mars 2019** fournit quelques noms utilisables, avec un statut historique et un contexte de modèles de référence distincts du catalogue retail actuel. [ELM066](elements.md#elm066) conserve le document, les pages et les attributions.

| Domaine local | Nom public repéré | Limite |
| --- | --- | --- |
| D04 — Commercial Commitments | Aucun équivalent précis de domaine commun de commandes établi dans le contenu examiné. | Agreement Management est désormais rapproché de D11, sans preuve de couverture des commandes D04. |
| D09 — Party / Role | **Customer Management** ; **Partner Management**. | Exemples plus larges que l’ingestion ; illustration Partner attribuée à Business Architecture Associates dans le support. |
| D11 — Agreement | **Agreement Management**, **Agreement Structuring**. | Exemples de capacités plus larges que l’ingestion locale du contrat de référence. |
| D12 — Catalog | **Product Management** comme voisin large. | Aucun équivalent précis de Catalog Ingestion démontré. |
| D01 — Inventory Management | **Asset Management** comme voisin très large. | Capacité support du Common Reference Model dans l’atelier ; insuffisant pour affirmer Inventory Management équivalent. |

Aucun nom suffisamment précis n’est établi dans ce contenu pour D02/D03/D05/D06/D07 ; les correspondances des trois ingestions restent partielles. Cela exprime une limite de consultation, pas une absence de ces sujets dans BIZBOK. Le guide intégral et le catalogue retail actuel ne sont pas revendiqués comme consultés.

## Ce que la comparaison apporte au challenge

**Inventory Management, Order Promising, Replenishment Planning, Product information management, Business Partner / Party Management et Pricing** fournissent des points de repère lisibles. Ils ne valident pas leur niveau de regroupement dans P81.

D02 et D03 se recouvrent dans le vocabulaire SAP ; D04 explore un noyau de commandes d’achat et de vente, distinct des Agreements en D11 ; D06 et D07 croisent qualification, choix, engagement et réalisation. Ces écarts sont utiles pour éprouver nos frontières, sans les corriger automatiquement. Source to pay et Order to cash restent des parcours ; aucun des deux ne devient le nom de D04.

Les domaines du socle, les objets des processus et les moyens de réalisation conservent leurs distinctions. Les références logistiques ou de planification plus larges n’étendent pas le développement FLOW. Les droits après fourniture et plusieurs aptitudes détaillées restent insuffisamment comparés.

## Aptitude métier et niveau SAP — U66/U67

Supply Protection et Supply Assignment peuvent désigner les aptitudes métier de protéger des ressources pour des groupes et de couvrir des demandes par des ressources. Laurent les qualifie ainsi en U67 ; Allocation Run désigne un mécanisme de réalisation. Le fait qu’une documentation SAP les présente comme fonctionnalités ne les réduit pas à de l’IT. [C49](../connaissance/04-corrections.md#c49) corrige cette confusion.

Dans les sources consultées, Inventory Management et Order Promising sont des Business Areas RBA ; Product Availability Check et Product Allocation Check sont des Business Capabilities RBA. Supply Protection est listée parmi les fonctionnalités additionnelles d’aATP ; Supply Assignment dispose notamment d’une Enterprise Business Function activable. Cette dernière expression ne désigne pas un niveau de la RBA. Leur entrée exacte comme Business Capability ou Solution Capability dans un catalogue RBA/RSA n’est pas établie ici, sans conclusion d’absence. [ELM067](elements.md#elm067), [CMP038](comparaisons.md#cmp038).

U74 rattache localement Supply Protection à Inventory Management ; [CMP040](comparaisons.md#cmp040) conserve l’adaptation et son contrôle documentaire. Les correspondances de contenu restent distinctes des niveaux natifs SAP. La définition de tout D01 n’est pas devenue équivalente à l’aire RBA homonyme.

U75 rattache la réservation à D01 et Supply Assignment à D03 ; [CMP041](comparaisons.md#cmp041) précise les rapprochements et leurs limites. Les anciennes lignes D02 ne doivent pas être lues comme un domaine validé ; sa cohérence autonome est en réexamen. La représentation de disponibilité par un produit ne prouve ni une capacité locale séparée ni un stock supplémentaire.

**Revue Order Promising U87/U88 — 2026-09-11 :** [audit](../audits/2026-09-11-order-promising.md), P83, ELM077/CMP046. Noms courts proposés Supply Feasibility, Confirmation, Supply Assignment et Promise Revision ; rattachements et IDs conservés. PAC peut produire une confirmation et BOP peut mobiliser Supply Assignment ; les quatre résultats locaux ne sont pas quatre composants natifs indépendants. D02 résiduel fait l’objet d’une recommandation de répartition, non appliquée.

**Complément U89 — D03 Order Promising :** [comparaison détaillée des quatre propositions](order-promising-comparaison-capacites.md), CMP047. Cinq feuilles visibles dans l’extrait SAP RBA, sans correspondance un-à-un ; Microsoft et Oracle détaillent aussi des alternatives. P83 reste proposée, frontières et repères conservés.

**Vocabulaire U90 — D03 :** Promise Verification et Promise Confirmation deviennent les candidats de la vue P83 ; Supply Assignment et Promise Revision sont appréciés par Laurent. [CMP048](comparaisons.md#cmp048) : appui lexical ATP, sans équivalence entre confirmation et contrôle d’allocation ni fermeture des écarts U89.

**Suite U91/U92 :** [CMP049](comparaisons.md#cmp049) ajoute les aptitudes de décision et leurs propriétaires proposés ; Promise Formulation remplace le candidat rejeté Promise Verification dans la vue P83. Pas de nouveau nom natif de marché établi ni de renumérotation.

**Suite U93 :** [CMP050](comparaisons.md#cmp050) ajoute la décision d’acheminement et ses appuis de marché, sans réduire la chaîne à la source ou à un délai. Promise Proposal devient le candidat courant ; autorités et frontières D03/D06/D07 restent à éprouver.

**Validation U95 — 2026-09-11, Laurent :** neuf capacités d’Order Promising retenues, avec quatre actions et cinq décisions. [CMP052](comparaisons.md#cmp052) relie les repères courants aux preuves existantes. La validation est locale ; les correspondances marché demeurent partielles. P81 version 0.5 compte 40 capacités ; ATP dans la promesse et placement CTP différé.

**Revue U96 — D04 :** [première vue Commercial Commitments](../connaissance/25-domaines-coeur-et-epreuve-recits.md#première-revue-commercial-commitments-u96), P84/CMP053, compare quatre aptitudes locales aux commandes, accords et retours. Le domaine commun achats/ventes reste à challenger ; pas de domaine natif équivalent ni de noms adoptés.

**Correction U97/U98 :** trois référentiels externes à ingestion seule ; D08/D10 retirés de la vue active, D09 recentré et D11/D12 ajoutés. La [trace remplacée](../audits/2026-09-11-reference-data-boundaries.md) conserve les anciennes aptitudes. Les rapprochements historiques U65/U96 ne valent pas validation de capacités de maîtrise dans la plateforme.

**Audit U99 — 2026-09-11 :** [rapport et revue des 34 capacités](../audits/2026-09-11-modele-marche-achats-ventes-referentiels.md), CMP055–CMP057. Party partagé, variantes achat/vente dans contrats/catalogues et commandes spécialisées ; aucune tripartition exhaustive démontrée. TMFC033 reste Planned. P86 propose les changements, sans modifier P81 0.6.

**Réorientation U100 — 2026-09-11 :** [CMP058](comparaisons.md#cmp058) distingue la référence article autonome confirmée (D08.d) des catalogues (D12). Les noms Purchase/Sales du marché servent à éprouver les variantes du socle Supply générique orienté documents d’autorisation ; ils ne prescrivent pas de scission transactionnelle locale. La correspondance précise de cette orientation documentaire au marché reste à établir. D04/D07 à reprendre ; neuf capacités D03 validées conservées. Les rapprochements TM Forum détaillés de D08.d restent à examiner, sans assimiler produit commercial télécom et SKU retail.

**Ajout U102 — Fulfillment Network :** la carte 0.8 ajoute D13.a, réception proposée des références de réseau, portant le total à douze repères de domaines et 36 aptitudes. [CMP060](comparaisons.md#cmp060) conserve les appuis partiels sur les lieux et indique le réseau complet non encore comparé. Les tableaux précédents correspondent à la version 0.7 et ne sont pas exhaustifs du nouvel état. D06 apprécie les options à partir de D13 ; aucune nouvelle hiérarchie native ni réalisation logistique affirmée.

**Présentation U103 :** [CMP061](comparaisons.md#cmp061) consigne le groupe local Business References retenu avec cinq références. La carte 0.9 modifie leur présentation, pas les 36 aptitudes ni les équivalences marché ; détails et maîtres du réseau encore ouverts.


**Évolution du backlog U116 — 13 septembre 2026 :** P82 devient la base de travail de D01. Inventory Tracking (D01.e) réunit D01.a/D01.b ; Inventory Visibility conserve D01.c. Les rapprochements antérieurs des deux premières aptitudes éclairent leur regroupement, sans créer une équivalence complète. Les appuis P82 (ELM068/ELM075/ELM076, CMP040/CMP042/CMP045) restent datés de leur examen initial ; aucune nouvelle vérification externe ici. Les trois autres capacités D01 conservent leurs correspondances et réserves. Voir [la correction Atlas et son périmètre](../audits/2026-09-13-atlas-d01.md).

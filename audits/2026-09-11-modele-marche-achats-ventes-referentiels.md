# Audit du modèle : achats, ventes, référentiels et capacités

> **Suite U100, 11 septembre 2026 :** cet audit conserve l’état P81 0.6 et ses constats marché. Laurent précise depuis une Supply générique fondée sur les documents d’autorisation, avec les parcours commerciaux dans la couche processus : la recommandation de choisir entre domaines Purchase/Sales est réorientée vers l’épreuve des variantes de ce socle. L’autonomie article est confirmée et explicitée par D08.d dans P81 0.7 (onze domaines, 35 capacités). Voir [la note U100](../connaissance/26-supply-documents-autorisations.md), C66/CMP058. Les autres propositions ne sont pas automatiquement adoptées.


11 septembre 2026 — demande [U99](../connaissance/01-contributions-utilisateur.md#u99). État audité : [P81 version 0.6](../connaissance/25-domaines-coeur-et-epreuve-recits.md), dix domaines actifs, 34 capacités. P82 et P84 sont examinées comme variantes proposées. Auteur : Codex. **Résultats et recommandations, sans changement automatique de la carte ni des validations de Laurent.** Suite proposée : P86 ; correspondances CMP055–CMP057.

Le marché conforte une **identité Party partagée**, des **relations d’achat et de vente spécialisées** et des **commandes distinctes des contrats de référence**. Il ne confirme pas un découpage universel des référentiels en exactement trois parties. Les principaux points à améliorer sont la visibilité des références produit, la distinction entre prix de référence et prix appliqué, et les responsabilités autour des commandes et de la consommation des contrats.

## 1. Méthode et portée

L’audit couvre Party, Agreement, Catalog et Order, puis examine les 34 capacités une à une. Il utilise des documentations officielles SAP et Microsoft, des notices TM Forum ODA et le guide public de métamodèle de la Business Architecture Guild. ELM087–ELM098 conservent sources, dates, versions disponibles et passages consultés. Les appuis stock/promesse antérieurs sont réutilisés avec leur provenance, notamment ELM014 et ELM075–ELM083 ; tous leurs produits ne sont pas réaudités exhaustivement.

Trois niveaux sont distingués : **constat externe**, **diagnostic local**, **proposition à arbitrer**. Un module SAP, une fonction Dynamics ou un composant ODA ne devient pas une capacité par copie de son titre. Le décompte de contrôle porte sur les 34 lignes locales, pas sur un taux de couverture du marché.

La maîtrise externe U97 est préservée. Comparer les aptitudes de l’entreprise et attribuer leur réalisation à FLOW sont deux questions différentes. Le socle reçoit les références et applique leurs conditions ; le référencement reste externe. Les moteurs, API, contrôles techniques et parcours d’approbation ne sont pas ajoutés à la capability map.

La Guild demande que les décompositions conservent l’objet de leur parent ; elle ne prescrit ni nos domaines problématiques ni trois référentiels. Son guide complet et ses modèles retail membres ne sont pas consultés. [Guide public, §5.2](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf), ELM097.

## 2. Achats et ventes : quelles séparations ?

| Objet | SAP | Microsoft | TM Forum / Guild | Conséquence proposée |
| --- | --- | --- | --- | --- |
| **Party / Role** | Business Partner commun ; données Customer/Supplier spécialisées. | Party commune ; rôles client/fournisseur contextualisés. | ODA distingue Party et Party Role. La Guild distingue objet client et accord, sans imposer deux identités. | **Garder D09 commun.** Une même partie peut être client et fournisseur. |
| **Agreement** | Contrats de vente et accords achats distincts ; contrats et scheduling agreements côté achats. | Sales agreements et Purchase agreements distincts, avec des principes de validité, engagement et consommation proches. | Agreement Management transversal entre parties ; pas de couple achat/vente imposé par sa notice. | **D11 commun reste défendable**, avec variantes Purchase Agreement / Sales Agreement dans les informations reçues. Une seule ingestion peut couvrir les deux. |
| **Catalog** | Catalogues d’approvisionnement ; article, assortiment et prix Retail également distincts. | Procurement catalogs et catalogues Commerce distincts. | ODA distingue offres/produits et catalogues de services/ressources ; pas de symétrie retail achat/vente démontrée. | **D12 commun reste possible**, en distinguant catalogue fournisseur reçu et catalogue de vente applicable. |
| **Order** | Purchase Order Management et Sales Order Management distingués. | Purchase Order et Sales Order distincts, y compris en intercompany. | Product Order orienté client ; Purchase Management identifié séparément, mais encore Planned. | **Éprouver D04 avec deux familles Purchase Order / Sales Order.** Séparation plus étayée que celle des ingestions. |

Sources : [SAP Business Partner](https://learning.sap.com/courses/sap-master-data-governance-on-sap-s-4hana/explaining-the-integrated-object-model-for-the-business-partner), [Microsoft Party](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/organization-administration/overview-global-address-book), ELM087 ; [accords achats](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements), [accords ventes](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-agreements), ELM088 ; [commandes intercompany](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/intercompany-orders-and-return-orders), ELM089 ; [catalogues achats](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-catalogs), [catalogues Commerce](https://learn.microsoft.com/en-us/dynamics365/commerce/catalogs-b2b-sites), ELM090 ; [ODA](../marche/elements.md#elm096).

**Limite des pages de catalogues achats :** Microsoft Procurement catalogs et SAP Catalog Items traitent principalement des biens pour usage interne et des achats indirects. Elles prouvent une lecture d’approvisionnement distincte, pas l’équivalence avec les catalogues de marchandises à revendre. Le cas de produits finis sur catalogue U48 reste notre épreuve principale.

### Le cas des commandes

Le noyau commun est réel : parties, lignes, quantités, conditions, dates, modifications et reste à réaliser. La différence métier à éprouver porte sur la responsabilité : **demander et suivre une fourniture auprès d’un fournisseur** ou **prendre un engagement de fourniture envers un client**. Elle existe même dans une organisation et un outil uniques. Les confirmations émises et reçues n’ont pas le même rôle dans la connaissance du futur.

| Option | Bénéfice | Condition |
| --- | --- | --- |
| Un domaine commun, par exemple **Order Commitments**, avec variantes achat/vente | Préserve le noyau générique et limite les duplications. | Démontrer que les résultats D04 ne masquent pas les différences d’engagement, confirmation et retour. Nom local proposé. |
| Deux domaines **Purchase Order Management** et **Sales Order Management**, côte à côte | Rend les asymétries lisibles ; vocabulaire proche de SAP. | Limiter chaque domaine aux aptitudes transactionnelles, sans réintroduire parcours OMS, tâches et validations organisationnelles. |

**Recommandation :** faire la prochaine revue D04 avec les deux familles en colonnes, puis arbitrer les domaines. Ne pas doubler d’emblée toutes les capacités. Pour Party, Agreement et Catalog, je ne recommande pas de scission automatique : des variantes de données ne démontrent pas deux aptitudes d’ingestion.

Le réassort intra-société U53 reste une fourniture sans vente automatiquement imposée. SAP expose le Stock Transport Order et Microsoft des commandes commerciales liées entre sociétés ; ces réalisations ne prescrivent pas notre modèle de transfert interne. [Commande d’achat SAP](https://learning.sap.com/courses/exploring-end-to-end-business-processes-in-sap-business-suite/managing-purchase-orders_dda0b0d0-7da6-43ec-b162-4faa1a6f339b), ELM089.

## 3. Trois référentiels : noyau cohérent, pas inventaire exhaustif

Il faut distinguer **famille d’informations**, **domaine**, **capacité qui utilise ces informations** et **application maître**. Une information nécessaire ne crée pas automatiquement un domaine ou une ingestion autonome.

| Famille | Présence dans le corpus | État local | Recommandation |
| --- | --- | --- | --- |
| **Party / Role** | SAP Business Partner, Microsoft Party, ODA Party/Role. | D09 explicite. | Conserver ; distinguer rôles de référence et parties retenues dans la transaction. |
| **Agreement** | Accords clients/fournisseurs ; TMFC039. | D11 explicite. | Recevoir portée, validité et conditions ; préciser séparément l’autorité sur la consommation. |
| **Catalog / Offering** | Catalogues Commerce/approvisionnement, Product Catalog ODA. | D12 explicite mais large. | Définir l’offre, son public et son champ d’application achat/vente. |
| **Product / Item** | Définition produit Microsoft, article SAP. | D08 retiré ; accueil implicite dans D12. | **Rendre explicite la réception des références article**, sans administration locale. Product Reference Ingestion à examiner. |
| **Price / Pricing Conditions** | Conditions SAP, groupes/règles Microsoft, prix de catalogue ODA. | Prix D12, conditions D11 ; calcul transactionnel sans propriétaire explicite. | Distinguer références reçues et application à la commande ; ingestion séparée conditionnelle. |
| **Supplier–Item / Source of Supply** | Purchasing Info Record, listes de sources, accords SAP. | Relation possible, contenu non établi. | Recevoir fournisseur/article, référence fournisseur, possibilités et délais utiles ; ne pas tout forcer dans Agreement. |
| **Assortment / Listing** | Article/site/période SAP ; assortiments liés au catalogue Microsoft. | La zone géographique D12 ne suffit pas à en définir le sens. | Recevoir les informations utiles et attribuer leur application ; conception d’assortiment et planification de saison externes/hors périmètre. |
| **Location / Site** | Sites/emplacements SAP ; dépendances géographiques ODA. | D06.a contient déjà lieux et prestations. | Séparer références reçues et possibilités d’exécution ; pas de nouveau domaine requis par le mot site. |
| **Unités, conversions, variantes, conditionnements** | Produit Microsoft et approvisionnement SAP. | Besoin reconnu, incomplet pour la façon U48. | Préciser les informations produit et leurs usages ; pas une capacité par attribut. |
| **Calendriers, délais, services, itinéraires** | Appuis antérieurs ELM083 et contraintes D06. | D03/D06/D07 partiels. | Connaissances d’amont/exécution, autorités à préciser avec C-Log ; pas un référentiel commercial supplémentaire universel. |

Sources : [produit Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information), ELM091 ; [fournisseur/article SAP](https://learning.sap.com/courses/sourcing-in-sap-s4hana/working-with-purchasing-info-records), ELM093 ; [assortiments](https://learning.sap.com/courses/exploring-sap-s-4hana-cloud-public-edition-retail/managing-assortments-3i5-), ELM094 ; [sites](https://learning.sap.com/courses/exploring-sap-s-4hana-cloud-public-edition-retail/maintaining-sites-for-retail-3i3-), ELM095. Ce tableau contrôle les informations ; **il ne propose pas dix domaines de référentiels**.

Les suites comprennent aussi données fiscales, comptes financiers, moyens de paiement, identité numérique et structures de conception. Leur existence n’en fait pas des domaines FLOW. Seules les références ou réponses utiles peuvent devenir des adhérences ; cette liste ne prétend pas épuiser ces interfaces.

### Point faible de la correction précédente

Retirer la maîtrise locale des articles répondait à U97. **La remplacer par une mention de produits dans Catalog ne démontre pas la couverture du référentiel article.** Un SKU peut être stocké, acheté à plusieurs fournisseurs et proposé dans plusieurs offres. Ses unités et caractéristiques ne doivent pas dépendre implicitement d’un catalogue commercial. C’est un manque de description, pas une demande de redevenir maître du produit.

Les contenus Agreement donnés par Laurent restent son orientation. Le marché apporte aussi validité, plafonds et consommation. **Commandes distinctes des Agreements ne signifie pas que seuls les Orders portent des engagements.** Commercial Commitments est donc trop large comme nom D04 après U98.

Une commande SAP peut exister sans référence à un document précédent. Les contrats examinés peuvent viser articles ou catégories sans démontrer un lien obligatoire à un catalogue nommé. Ce sont des cas à éprouver, sans retirer les liens voulus localement ni décider leurs cardinalités.

## 4. Les prix sont-ils séparés ?

**Le sens des prix est séparé plus nettement que leur stockage.**

| Question | Résultat | Responsabilité à préciser |
| --- | --- | --- |
| Quels tarifs et conditions avons-nous reçus ? | Références avec portée et période. | Maître externe ; réception par Catalog/Agreement ou Price Reference distinct à justifier. |
| Quel prix s’applique à cette commande et pourquoi ? | Prix transactionnel et conditions retenues. | **Transaction Pricing** si la plateforme calcule ; sinon résultat reçu d’une autorité externe. |
| Quel prix a été retenu dans l’engagement ? | Valeur et références appliquées à une version de commande. | Domaine de commande ; éviter un recalcul silencieux de l’historique lorsque les références changent. Règle locale proposée. |

SAP Retail distingue conditions tarifaires, niveaux et périodes puis leur application. Microsoft relie le catalogue à des groupes de prix et applique des règles à la commande. TM Forum décrit les prix au catalogue et leur application par le configurateur. **Un domaine Price autonome n’est donc pas obligatoire dans toutes les références.** [Prix SAP](https://learning.sap.com/courses/exploring-sap-s-4hana-cloud-public-edition-retail/performing-sales-pricing-for-retail-3i4-), [pricing Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/unified-pricing-management/upm-pricing-management-overview), [configurateur TM Forum](https://www.tmforum.org/resources/specifications/tmfc027-product-configurator-v2-2-0/), ELM092.

Les conditions d’achat et de vente restent spécialisées. Unified pricing ne prouve pas un modèle unique de tous les prix achats/ventes ; Vendor list price ne signifie pas prix d’achat engagé. **Transaction Pricing** exprime un calcul/application : Decision n’est pas imposé au seul motif qu’un résultat est calculé. Les dérogations commerciales sont un autre sujet.

Catalog et Agreement peuvent fournir des conditions complémentaires. Leur priorité, version et champ d’application devront être explicités dans les contrats durables. U97 ne choisit pas encore qui calcule le prix final ; cet audit n’attribue pas ce calcul à FLOW par défaut.

## 5. Revue des 34 capacités courantes

**Conserver** signifie qu’aucun défaut justifiant un retrait n’est identifié dans ce contrôle. **Préciser** vise un résultat, cycle, propriétaire ou une frontière incomplets ; **Reformuler** un nom trop large ou peu lisible ; **Recouvrement** une autonomie non démontrée. Ces avis ne changent pas les validations. Les noms proposés sont locaux, pas des feuilles natives revendiquées.

| Repère | Libellé courant | Diagnostic et proposition | Appui / limite |
| --- | --- | --- | --- |
| D01.a | Establish inventory positions | **Reformuler / recouvrement D01.b.** Inventory Tracking dans la fusion déjà proposée P82 exprime mieux la continuité quantités/états. | ELM075/076 ; nom local. |
| D01.b | Record inventory facts | **Recouvrement D01.a.** Enregistrer les faits et produire leurs effets peut rester une seule aptitude ; conserver la distinction faits/objets. | P82 ; les tâches produit ne démontrent pas deux capacités. |
| D01.c | Provide a consolidated inventory view | **Reformuler.** Inventory Visibility, déjà proposé ; garder physique, logique, futur et provenance. | ELM064/075/076 ; couverture multisource locale à éprouver. |
| D01.d | Stocktaking | **Conserver**, nom validé U86. Comptage, rapprochement et correction restent dans sa définition. | ELM014/076 ; pratiques locales non établies. |
| D02.b | Supply Protection, rattachée D01 | **Conserver.** Distinguer protection d’usage et objectif de réassort D05.a. | ELM067/069 ; un quota fournisseur ELM093 n’est pas une protection de stock. |
| D02.c | Reservation, rattachée D01 | **Préciser le cycle** : ajustement, libération et consommation ; pas une capacité par opération. | ELM098 ; rattachement en discussion inchangé. |
| D02.a | Determine resource availability for a given use | **Recouvrement prioritaire.** Stock virtuel pour promettre déjà dans D03.a ; disponible de réservation à préciser en D01. | U81, ELM077/080 ; autonomie D02 non justifiée. |
| D02.d | Adjust resource commitments | **Recouvrement prioritaire.** Ajustements/libérations dans Reservation ou Supply Assignment ; effets sur promesse dans D03.c. | ELM098 et D02.e ; répartir les résultats avant retrait. |
| D03.a | Promise Proposal | **Conserver**, validé U95. Expliciter ATP, quantités/dates, options et limites du futur. | ELM077–080 ; ATP ne crée pas une capacité en plus. |
| D03.b | Promise Confirmation | **Conserver**, validé. Distinguer promesse, acceptation de commande et confirmation fournisseur reçue. | ELM088/089 ; résultats distincts sans imposer trois documents. |
| D02.e | Supply Assignment, rattachée D03 | **Conserver**, validé. Couverture/réaffectation par ressources, sans doublon D02.d. | ELM067/077 ; Allocation Run reste une réalisation. |
| D03.c | Promise Revision | **Conserver**, validé. Backorder processing illustre le réexamen sans ajouter une capacité. | ELM077/079 ; préserver demandes dépriorisées et effets. |
| D03.d | Allocation Eligibility Decision | **Préciser**, nom validé. Accès quantitatif aux ressources ; pas toute admissibilité commerciale d’une commande. | ELM079 ; PAL est un appui partiel. |
| D03.e | Fulfillment Source Decision | **Conserver**, validé. Choix de source pour promettre ; pas toute sélection de fournisseur d’achat. | ELM079/080 ; distinction ELM093. |
| D03.f | Fulfillment Route Decision | **Préciser la frontière**, validé. Option d’acheminement soutenant la promesse, sans absorber la conception de tout le transport. | ELM083 ; autorités C-Log inchangées. |
| D03.g | Product Substitution Decision | **Conserver**, validé. Réception des équivalences et conditions à expliciter ; administration externe. | ELM079/080/091 ; variante et remplacement acceptable ne sont pas identiques. |
| D03.h | Supply Creation Decision | **Conserver**, validé. Nouvelle fourniture sans absorber achat, négociation ou fabrication. | ELM079 ; placement CTP toujours différé. |
| D04.a | Establish a commercial commitment | **Reformuler / spécialiser à l’essai.** Order Creation ou Order Commitment Creation ; distinguer commande émise, reçue, acceptée. | ELM089 ; Commercial Commitment désigne aussi des engagements d’Agreement. |
| D04.b | Amend commercial obligations | **Reformuler.** Order Revision, avec annulation et effets explicites. | ELM088/089 ; aucun changement du contrat maître. |
| D04.c | Determine commitment fulfillment and remaining obligations | **Reformuler / préciser.** Order Reconciliation ; distinguer reste commandé, promis, couvert et réalisé. | ELM089 ; consommé contractuel distinct, ELM088. |
| D04.d | Authorize a return or replacement | **Maille à éprouver.** Return Authorization et Replacement Decision si résultats autonomes ; distinguer retour client/fournisseur. | ELM098/089 ; permission de renvoi, acceptation des biens et remède différents. |
| D05.a | Determine operational coverage targets | **Reformuler / autorité.** Coverage Target Decision si le domaine décide ; sinon expliciter l’utilisation d’objectifs reçus. | IRMA/MAP U06/U10, ELM063 ; saison exclue. |
| D05.b | Determine net resource requirements | **Reformuler.** Net Requirements Calculation ; entrées attendues et unités explicites. | ELM063/093 ; besoin net distinct de commande confirmée. |
| D05.c | Determine resource redistribution | **Reformuler.** Stock Redistribution Decision si l’objet est bien le stock ; préciser proposition ou décision engageante. | U57, ELM063 partiel ; pas de comparaison complète démontrée. |
| D06.a | Qualify locations and feasible services | **Séparer les sens.** Références de lieux reçues et prestations admissibles ; ne pas suggérer la validation du maître. | ELM095/098 ; pas de nouveau domaine automatique. |
| D06.b | Determine available execution capacity | **Reformuler.** Execution Capacity Assessment ; moyens disponibles, pas Business Capabilities. | U04, ELM098 ; Maximum orders et quota local non équivalents. |
| D06.c | Determine eligible execution options | **Préciser / recouvrement D03.e/f.** Execution Option Assessment pour les possibilités ; le choix reste dans son domaine propriétaire. | ELM098 ; éviter deux propriétaires d’une même décision. |
| D07.a | Formalize a service requirement | **Reformuler.** Execution Requirement Definition ; service est ambigu sur le besoin adressé à la réalisation. | ELM043/047/065 partiels ; ni API ni dossier processus imposé. |
| D07.b | Establish and adjust execution commitments | **Préciser.** Execution Commitment Management comme titre candidat ; acceptation/refus et effets sur charge explicites. | U04/U05, ELM098 partiel ; promesse D03 distincte. |
| D07.c | Qualify execution results and discrepancies | **Reformuler.** Execution Reconciliation ; établir écarts et imputations à partir des faits reçus. | U48, ELM043/044/047 ; contrôle distinct de l’exécution physique. |
| D07.d | Identify and qualify expected resources | **Préciser / recouvrement D01.** Expected Supply Tracking : provenance/date/fermeté ; D01 représente le futur, D03 juge son admissibilité. | U79/U80, ELM093 ; éviter plusieurs maîtres du même futur. |
| D09.d | Party / Role Ingestion | **Conserver selon U97.** Réception d’identité et rôles, sans enrichissement, dédoublonnage ni recrutement. | ELM087/096 ; portée plus étroite que la maîtrise externe. |
| D11.a | Agreement Ingestion | **Conserver selon U97.** Expliciter achat/vente et conditions reçues ; ne pas absorber le suivi de consommation. | ELM088/096 ; consommé à attribuer séparément. |
| D12.a | Catalog Ingestion | **Conserver / délimiter.** Distinguer catalogues achat/vente, offres, articles et prix. | ELM090–092/096 ; ne démontre pas tout Product Reference. |

**En trop ou redondantes :** les deux lignes résiduelles D02 sont les candidates de retrait les plus solides, après répartition de leurs résultats. La fusion D01.a/b reste une proposition pertinente. Les frontières D06/D07 sont insuffisantes pour conclure à leur fusion ou suppression complète.

**Mal dites :** les formulations longues de D01, D04 et D05–D07 contrastent avec le style retenu pour Order Promising. Remplacer systématiquement Determine par Decision serait une autre imprécision : calcul, rapprochement et réception d’un fait gardent leur nature. Le titre peut être nominal ; la définition doit rester une aptitude de l’entreprise indépendante des outils.

## 6. Manques à examiner : capacités, informations ou responsabilités

AC01–AC09 sont des repères propres à cet audit, **pas des CAP ni des capacités validées**. Un manque peut être résolu par une meilleure définition ou une responsabilité externe.

| Repère | Aptitude / résultat proposé | Nature et Finalité | Preuve et intérêt | Accueil / statut |
| --- | --- | --- | --- | --- |
| AC01 | **Product Reference Ingestion** : recevoir articles, variantes, unités et conversions utiles. | Réception ; relier les opérations aux bons biens. | Besoin fort du stock et de la façon U48 ; ELM091. | **Priorité haute.** Capacité et domaine autonomes à éprouver, maître externe ; pas rétablissement de D08.a–c. |
| AC02 | **Price Reference Ingestion** : recevoir tarifs/conditions lorsque source et cycle sont distincts. | Réception ; disposer des références tarifaires. | ELM090/092 ; indépendance de cycle plausible, non déclarée localement. | **Conditionnel.** Peut rester dans les informations D11/D12. |
| AC03 | **Transaction Pricing** : appliquer les conditions reçues pour établir le prix de la commande. | Calcul/application ; établir la valeur commerciale de l’engagement. | ELM089/092 ; responsabilité peu visible après retrait D10.b. | **Priorité haute sur l’autorité**, pas sur un développement FLOW. D04/Pricing si local ; sinon résultat externe reçu. |
| AC04 | **Agreement Consumption Tracking** : imputer consommations/annulations au plafond et connaître le reliquat. | Rapprochement ; connaître le potentiel contractuel utilisable. | Potentiel fournisseur U79 ; ELM088. Distinct du reste à livrer d’une commande. | **Priorité haute sur l’autorité.** D04 peut fournir les faits, le maître externe peut calculer le reliquat. Aucun ajout à D11 ingestion seule. |
| AC05 | **Order Eligibility Decision** : décider si la demande peut devenir commande sous les conditions applicables. | Décision ; prendre un engagement admissible. | ELM089/096 ; exclusion U10, conditions U97. Distinct de la quantité disponible. | **À éprouver en D04.** Application de conditions reçues, pas vérification de leurs données maîtres. Peut préciser D04.a. |
| AC06 | **Purchase Source Decision** : choisir fournisseur/source d’approvisionnement opérationnelle. | Décision ; donner une origine au besoin d’achat. | ELM093 et achats U48 ; autonomie FLOW non déclarée. | **Candidat plausible** avec Purchase Order ; distinct du sourcing stratégique et de la source de promesse D03.e. |
| AC07 | **Supplier Commitment Reconciliation** : rapprocher quantités/dates demandées et annoncées, avec écarts explicites. | Rapprochement ; distinguer besoin, engagement reçu et ressource attendue. | Déduction U30/U48/U79, appui ELM089/093 partiel. | **Enrichissement des cas**, probablement D04.c/D07.d avant capacité autonome. Une annonce ne prouve pas la réalisation. |
| AC08 | **Product–Location Eligibility** : apprécier l’admissibilité article/opération/lieu/date selon les références reçues. | Appréciation/décision à préciser ; respecter les possibilités opérationnelles. | ELM094 ; réassort/extension de gamme comme épreuves, règles locales non décrites. | **Enrichissement probable D06.c/AC05.** Pas de construction des assortiments ni de planification saisonnière. |
| AC09 | **Return Authorization / Replacement Decision** : distinguer permission de retour et choix du remplacement. | Décisions ; donner une réponse commerciale précise. | ELM098 ; retours présents mais peu racontés. | **Décomposition possible D04.d**, pas deux capacités totalement absentes ; retour fournisseur à éprouver. |

### Épreuve sur les récits et cas construits

| Cas | Attendu | Conclusion |
| --- | --- | --- |
| Trois modes d’achat U48, dont composants et façonnier | Produits, unités, fournisseurs, prestations, commandes et réalisation distincts. | Accueil existant ; références article et engagements fournisseur trop implicites : AC01/AC07. |
| Potentiel achetable sous contrat U79 | Plafond, consommé et reliquat distincts des réceptions attendues. | Autorité du consommé/reliquat manquante : AC04. |
| Boardriders : commande non couverte U30 | Commande existante, parts non promises/non affectées visibles. | D04/D03 accueillent le principe ; accepter la commande ne confirme pas automatiquement l’ATP. |
| Boardriders : réaffectation prioritaire U30/U31 | Réviser couverture/promesse et préserver les demandes dépriorisées. | D03 couvre le résultat ; doublon possible D02.d. |
| Réassort intra/inter-sociétés U53 | Fourniture générique et engagements commerciaux selon le cas. | Commandes liées : repère de marché intercompany, pas modèle imposé au transfert interne. |
| Quotas et refus magasin U04/U05 | Stock, capacité de service, engagement d’exécution et dossier distincts. | D06/D07/processus accueillent les notions ; effets et autorités encore partiels. |
| Cas construit : même Party fournisseur et client | Identité commune et relations contextualisées. | D09 commun convient ; pas deux capacités d’ingestion par rôle. |
| Cas construit : même SKU dans plusieurs catalogues et tarifs | Article stable, offres et prix contextualisés. | AC01/AC03 rendent explicite ce que D12 seul ne démontre pas. |
| Cas construit : deux commandes consomment le dernier reliquat contractuel | Autorité explicite sur plafond, annulations et retours. | AC04/AC05 ; problème métier identifié sans choix de verrouillage ou de technologie. |

## 7. Suite recommandée

La prochaine revue devrait traiter **les commandes d’achat et de vente** avec la même grille : demande, engagement, conditions, confirmations, modifications, réalisations et reste. Elle permettra d’arbitrer un domaine commun ou deux domaines. Rendre explicites les références produit et l’autorité du pricing/consommé contractuel résout des trous de compréhension plus importants qu’une renumérotation.

[P86](../connaissance/05-propositions.md#p86) propose de garder Party partagé et Agreement/Catalog avec variantes achat/vente ; d’examiner Product Reference distinctement ; de distinguer Pricing sans en imposer la maîtrise locale ; de répartir les résultats D02 avant retrait ; et de poursuivre les noms courts. [Q070–Q073](../connaissance/06-questions.md#q070) consignent les arbitrages ouverts.

**Ne pas additionner les neuf lignes AC pour calculer une nouvelle cible** : certaines sont des informations, variantes ou précisions. La carte reste P81 0.6, dix domaines et 34 capacités. Les neuf capacités d’Order Promising restent validées ; CTP demeure différé.

## 8. Sources et limites

Les [éléments de marché](../marche/elements.md#elm087) conservent les liens officiels, localisateurs et versions. Les références connues MKT03, MKT13, MKT14 et MKT19 sont réutilisées ; aucun catalogue principal n’est adopté.

| Dossier | Objet vérifié le 11 septembre 2026 | Limite principale |
| --- | --- | --- |
| [ELM087](../marche/elements.md#elm087) | Party client/fournisseur | Modèles de produit ; pas déploiement local. |
| [ELM088](../marche/elements.md#elm088) | Contrats achats/ventes, consommation | Quatre pages SAP/Microsoft ; pas règle juridique générale. |
| [ELM089](../marche/elements.md#elm089) | Commandes SAP, intercompany Microsoft | Spécialisation des traitements ; pas deux domaines locaux obligatoires. |
| [ELM090](../marche/elements.md#elm090) | Catalogues achats/Commerce | Achats internes/indirects ; marchandises à revendre non assimilées. |
| [ELM091](../marche/elements.md#elm091) | Produit et import | Information partagée, pas toute l’offre commerciale. |
| [ELM092](../marche/elements.md#elm092) | Prix et application | TMFC027 2.2.0 Pre-production ; spécification membre non lue. |
| [ELM093](../marche/elements.md#elm093) | Fournisseur/article et sources | Règles propres aux variantes SAP ; priorités non importées. |
| [ELM094](../marche/elements.md#elm094) | Assortiment/listing | Article/site/période ; conception de saison exclue. |
| [ELM095](../marche/elements.md#elm095) | Sites/emplacements | Organisation SAP non transposée en capacités. |
| [ELM096](../marche/elements.md#elm096) | Structure ODA | Versions de notices différentes ; Purchase Management Planned, spécification non publiée. |
| [ELM097](../marche/elements.md#elm097) | Méthode Guild | Guide public v3.0 §5.2 ; pas modèle retail membres. |
| [ELM098](../marche/elements.md#elm098) | Réservations, DOM, retours | Contrôle ciblé ; appuis stock/promesse antérieurs restent partiels. |

Les pages Microsoft ont fourni leur texte malgré des bandeaux génériques de connexion ; aucune authentification utilisée. Une première URL Global address book a échoué ; la route officielle dev-itpro déjà connue a été lue. Le lien Production 2.1.2 depuis la notice TMFC027 a échoué : la conclusion utilise uniquement la notice publique 2.2.0, explicitement Pre-production. Aucun contenu payant n’est présenté comme consulté. Le SID intégral, Oracle/APQC et les autres références n’ont pas fait l’objet d’une nouvelle vérification pour cet audit ciblé.

## 9. Vérification documentaire

Les 34 repères courants doivent chacun apparaître une fois dans la table de revue. Les propositions AC ne changent ni noms ni définitions actives. Les contrôles exécutés sont consignés ci-dessous.

**Contrôle exécuté le 11 septembre 2026 :** 34 repères sur 34 présents exactement une fois dans la table ; neuf pistes AC distinctes. Dix domaines actifs conservés. Les définitions et statuts de P81 sont inchangés : seuls le lien vers cet audit et la réserve de couverture ont été ajoutés. Le registre CAP36 est identique à son état avant audit (SHA-256 texte UTF-8 : `0d41ed1699d3a48b9e01981036fbeddf9b5cdd76e6b3907487af9f9893d2b404`). Identifiants U/F/A/C/P/Q/INF/DEC/TER/VER/MKT/ELM/CMP uniques et séquentiels ; 797 liens locaux et ancres contrôlés sans erreur selon les conventions existantes. Aucun fichier d’archive modifié par ce travail. Les noms et contenus proposés restent soumis à arbitrage.

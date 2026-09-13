# Localisation des Orders dans la cartographie

Recherche Codex du 13 septembre 2026, U138/U139 ; ELM109–ELM113, CMP064. État local comparé : backlog et Urbanisation v002, D04 Commercial Commitments et D07 Execution Commitments and Facts, sans modification. Les recommandations nouvelles sont **Proposées par l’IA**.

## Conclusion et recommandation

Un domaine autonome Order Management est une option cohérente pour FLOW, à condition de délimiter un espace problématique propre : connaître la demande autorisée, ses lignes, sa version applicable et ce qui reste à satisfaire. Le seul objet Order ne justifie pas un domaine. La promesse, le stock et l’exécution possèdent déjà leurs problèmes et leurs autorités.

Le marché n’impose pas un domaine universel Orders. Trois lectures coexistent : séparation achat/vente dans les ERP, famille documentaire commune dans un OMS, distinction commande commerciale/demandes de réalisation dans une architecture par niveaux. Les rangs comparés diffèrent : modèle de capacités cité, navigation de produit, catalogue de processus ou composants d’architecture.

Je recommande d’éprouver un **Order Management transactionnel restreint**, comme remplacement possible de D04, distinct d’Agreement et d’Order Promising. La limite avec D07 conditionne cette proposition : si tout son résultat est déjà couvert par le besoin et le suivi d’exécution de D07, il faut fusionner ces responsabilités plutôt que maintenir deux domaines par inertie. Aucun remplacement appliqué.

## Localisations observées

| Référence | Placement effectivement documenté | Nature de la preuve et portée |
| --- | --- | --- |
| SAP RBA, cité dans la base d’architecture | Customer → Sales → Customer Order and Contract Management ; Sales Order Management cité dans ce contexte. | Article d’architecture, extrait indexé ; ouverture 403, édition exacte RBA inconnue. Pas un domaine générique de tous les Orders établi. [S1] |
| SAP S/4HANA, vue produit | Sales / Sales order management ; côté achat, Sourcing and Procurement → Operational Procurement → Purchase Order Processing dans le chemin de configuration documenté. | Fonctionnalités et navigation produit, pas preuve de rang RBA identique. [S2–S3] |
| Microsoft Dynamics 365 | Order to cash → Manage sales orders ; Source to pay → Procure goods and services pour les commandes d’achat. | Business process areas, pas domaines de capacités. Le produit traite aussi les transferts d’entrepôt avec Inventory management et Master planning. [S4–S6] |
| Oracle Fusion | Order Management pour la commande client et sa réalisation ; Procurement possède un espace Purchase Orders. | Frontières de produits et objets, pas une carte générique de capacités. [S7–S8] |
| IBM Sterling OMS | Famille documentaire Order : Sales, Planned, Return, Template, Purchase, Transfer, Master Order. | Typologie explicite d’objets d’un OMS ; appui à la généricité documentaire, aucune preuve d’un domaine métier autonome. [S9] |
| TM Forum ODA | Core Commerce Management : capture/validation de Product Order et orchestration de sa livraison ; Production : Service Order Management et Resource Order Management. Agreement Management est placé sous Party Management. | Carte de composants ODA, pas une liste de capacités métier ; illustration de séparation des responsabilités selon l’objet commandé. [S10] |

### Ce que ces différences nous apprennent

SAP et Microsoft offrent des noms précis pour achat et vente, mais leurs regroupements ne résolvent pas directement notre volonté de traiter achat, vente, réassort et retour par des aptitudes transactionnelles génériques. Reprendre leurs branches ferait entrer des parcours commerciaux dans le découpage que nous cherchons justement à construire autrement.

IBM Sterling fournit l’appui le plus direct à une famille de documents Order comportant plusieurs types. Il s’agit du produit OMS actuel, distinct du modèle IBM CBM 2005 que Laurent ne souhaite pas privilégier. Une famille d’objets commune ne signifie cependant ni règles entièrement identiques, ni objet universel obligatoire, ni partage d’une application imposé.

Oracle décrit la transformation de la commande d’origine en représentation exploitable pour sa réalisation ; elle peut avoir une structure différente. Cette distinction est utile à la frontière processus/Supply, mais son OMS traverse plusieurs de nos domaines. La présence de son produit Order Management ne justifie pas d’y déplacer localement promesse, réservation ou logistique.

TM Forum distingue la capture commerciale et l’orchestration, puis les demandes de service et de ressource. Cela appuie la possibilité de plusieurs modèles d’Order reliés. Product, Service et Resource ont leurs sens télécom ; ils ne se traduisent pas automatiquement par commande commerciale, transport et stock dans FLOW.

## Trois options locales

| Option | Intérêt | Difficulté pour FLOW | Avis proposé |
| --- | --- | --- | --- |
| Sales Order Management + Purchase Order Management, puis transferts/retours | Noms proches de la lecture ERP. | Réplique les contextes commerciaux et complique le cœur générique de réassort. | Ne pas privilégier pour la carte transactionnelle ; utile pour les correspondances et les processus. |
| Order Management commun, avec D07 distinct | Porte le cycle de la demande autorisée indépendamment du moyen de réalisation. | Risque de dupliquer définition du besoin et rapprochement des réalisations de D07. | Option à explorer en priorité avec une frontière explicite. |
| Un domaine regroupant Orders et engagements/faits d’exécution | Évite une séparation artificielle si leurs règles sont indissociables. | Peut devenir un domaine trop large, absorbant orchestration, promesse et stock. | Alternative à tester si la deuxième option ne produit pas de résultats distincts. |

## Frontières proposées pour la deuxième option

| Sujet | Propriétaire proposé ou orientation existante |
| --- | --- |
| Contrat complet et engagements de période | Agreement, projection externe selon U134 ; administration hors FLOW. |
| Négociation, parcours achat/vente/SAV, décision commerciale de passer ou modifier la commande | Modèle processus et produits responsables ; autorité détaillée encore à documenter. |
| Demande autorisée courante : lignes, quantités, origine/destination utiles, version, limites et reliquat | Order Management candidat ; contenu opérationnel distinct de la maîtrise commerciale. |
| Faisabilité, promesse, affectation et révision de promesse | Order Promising, conformément aux orientations et validations existantes. |
| Stocks physiques/logiques, mouvements, protection et réservation | Inventory Management, conformément au modèle courant. |
| Prestations attendues, prise en charge par les exécutants, faits et écarts | D07, à confronter au reliquat de commande pour éviter un doublon. |
| Réalisation logistique | Exécutants, dont C-Log ; toujours hors développement FLOW. |

Le socle pourrait recevoir et reconnaître les Orders et leurs révisions, exposer leur situation et établir le reliquat autorisé à satisfaire. Ce sont des résultats candidats à décrire en capacités, sans adopter ici de nouvelle liste. Recevoir une annulation commerciale n’est pas décider du droit à annuler ; accepter sa faisabilité opérationnelle peut impliquer promesse et exécution.

La copie d’une Order reçue n’en fait pas un référentiel du groupe Business References. C’est une information transactionnelle, éventuellement projetée, à laquelle la Supply peut rattacher son propre état. La règle des référentiels en lecture seule ne tranche pas toute l’autorité sur ces états. Un Order ne doit pas non plus devenir un simple message technique ou le dossier complet du processus commercial.

## Épreuve sur les récits

Les points suivants sont des accueils conceptuels proposés, pas des preuves de déploiement ou de couverture complète.

| Cas déclaré | Accueil à éprouver |
| --- | --- |
| Réassort entrepôt/magasin, même société ou sociétés différentes | Décrire la demande de transfert générique ; préserver les liens vers ses documents commerciaux éventuels sans créer une capacité différente pour chaque situation juridique. |
| Achats de produits finis ou issus d’un catalogue fournisseur | Une commande peut exprimer le résultat attendu indépendamment du parcours d’achat. Le choix commercial et le référentiel catalogue restent ailleurs. |
| Fabrication à façon | Plusieurs commandes et autorisations peuvent être liées : matières, fourniture au façonnier, résultat fini. Ne pas forcer un Order unique ; relations et dépendances restent à explorer. |
| Boardriders : couverture future et réaffectation prioritaire | L’Order porte la demande ; Order Promising traite couverture et révision de promesse. Un changement d’affectation ne doit pas être assimilé d’office à une modification de commande. |
| Retours | L’autorisation et la demande de retour peuvent être représentées ; la décision commerciale du recours et la prise en charge physique doivent rester distinguées. |

L’arbitrage utile est donc : **le cycle de la demande autorisée comporte-t-il des règles et un résultat durables qui restent distincts du cycle de ses engagements d’exécution ?** Si oui, un domaine Order Management est justifié. Sinon, rapprocher D04 et D07. Q074 reste ouverte ; ni domaine ni objet détaillé n’est adopté par la recherche.

## Sources, versions et limites d’accès

Consultation du 13 septembre 2026 ; synthèses sélectives, aucune reproduction de catalogue complet. Les versions de produits indiquées sont celles des documents examinés, pas une affirmation de dernière version disponible.

- **S1 — SAP EA Knowledge Base**, [Application Decisions for Sales Order Management in CX – Part 1](https://community.sap.com/t5/enterprise-architecture-knowledge-base/application-decisions-for-sales-order-management-in-cx-part-1/ta-p/14274899). Article de décembre 2025, passage de positionnement RBA retrouvé dans l’extrait indexé ; accès direct 403. Édition RBA non connue. Complète les limites déjà notées dans l’étude du 9 septembre.
- **S2 — SAP Cloud ERP Private**, [Sales](https://www.sap.com/uk/products/erp/s4hana-private-edition/features/sales.html), section Sales order management ; texte lu, présentation évolutive sans édition figée.
- **S3 — SAP S/4HANA Cloud**, [Manage Purchase Orders](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/38cbf557c328be12e10000000a4450e5.html?q=Manage+Teams+and+Responsibilities+-+Procurement), chemin de configuration Sourcing and Procurement / Operational Procurement / Purchase Order Processing dans l’extrait indexé ; ouverture sans texte. Rang RBA non déduit.
- **S4 — Microsoft**, [Order to cash overview](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/order-to-cash-overview), liste du flux, Manage sales orders ; texte lu, catalogue de processus évolutif.
- **S5 — Microsoft**, [Source to pay business process areas](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/source-to-pay-areas), Procure goods and services ; texte lu, page faisant état de révisions du catalogue depuis 2024.
- **S6 — Microsoft**, [Set up warehouses for transfer orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/transfer-orders-warehouse), début et chemins de paramétrage ; texte lu, mise à jour affichée 2026-07-01. Pas un rang de capacité.
- **S7 — Oracle Fusion Cloud Order Management 25C**, [Source Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/fauom/how-order-management-transforms-source-orders-into-sales-orders.html), transformation et structure ; texte relu, ELM108.
- **S8 — Oracle Fusion Cloud Procurement 25C**, [Purchase Order Infolets](https://docs.oracle.com/en/cloud/saas/procurement/25c/oaprc/purchase-order-infolets.html), espace Purchase Orders ; texte lu. Preuve du périmètre produit uniquement.
- **S9 — IBM Sterling OMS**, [Document types](https://www.ibm.com/docs/en/order-management?topic=configuration-document-types), table Order ; texte lu, édition précise non exposée. Le produit ne se confond pas avec IBM CBM 2005.
- **S10 — TM Forum**, [ODA Component Directory](https://www.tmforum.org/oda/directory/components-map), Core Commerce Management, Production et Party Management ; carte textuelle lue, édition d’ensemble non affichée. TMFC002, TMFC003, TMFC007, TMFC011, TMFC039. La page détaillée TMFC007 v1.2.2 retourne 403 ; aucune spécification complète revendiquée.

La recherche porte sur cinq références pertinentes, sans exhaustivité. Aucun nouveau catalogue BIZBOK membre ni export complet SAP RBA examiné. Les constats ne prouvent ni l’autorité installée chez Beaumanoir ni la réalisation d’une capacité dans un de ses SI.

# Audit landscape — Authoritative Data

21 septembre 2026 · demandes U511–U513 · diagnostic et recommandations proposés

**Conclusion : conserver la responsabilité commune et les distinctions de sens, mais alléger leur expression au niveau landscape.** Le corpus confirme que l’orchestration peut recevoir ses références de maîtres externes. Il ne justifie ni sept administrations autonomes ni quatorze capacités par une simple répétition Ingestion/Visibility. Il ne démontre pas non plus que ces quatorze capacités seraient inutiles : leur séparation doit s’appuyer sur des résultats et responsabilités propres.

La question du nom est différente : **Authoritative Data est documenté en architecture et gouvernance des données ; sa compréhension par un client métier n’est pas démontrée.** L’inquiétude U513 doit donc être traitée même si le concept reste pertinent.

## Périmètre et méthode

Audit de l’Area `business-references`, des sept références qu’elle présente, de leurs quatorze capacités et de leurs relations avec les autres Areas. Le backlog YAML fait autorité. Le commit de départ est `5957a17756d7def41be9a599e7de293245cceebc` ; empreinte et constats structurels dans [structural-findings.yaml](structural-findings.yaml).

Trois regards sont séparés : **modèle métier FLOW**, **structures de produits OMS**, **principes d’architecture et de gouvernance**. Un modèle de données d’éditeur ne constitue pas une carte de capacités. Le corpus couvre Microsoft Intelligent Order Management, Fluent Order Management et IBM Sterling, complétés par Oracle, EDM Council, OMG/Camunda, SAP Retail, Microsoft Commerce et TM Forum. Il s’agit d’un échantillon documentaire, sans classement de produits, preuve d’installation Beaumanoir ni vérification de leur disponibilité commerciale.

Les sources primaires ont été consultées le 21 septembre 2026. Éditions, passages, limites et interprétations sont conservés dans [fluent-documents.yaml](fluent-documents.yaml), [oms-documents.yaml](oms-documents.yaml) et [concept-documents.yaml](concept-documents.yaml). Les rapprochements et options sont consignés dans [l’annexe de revue](../../modeles/backlog/authoritative-data-landscape-U512.yaml). L’audit ne rouvre pas l’audit historique des comportements.

## Ce que montre le marché

| Référence | Constat sourcé | Portée pour FLOW et limite |
|---|---|---|
| [Microsoft IOM — Data management](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/data-management) | Un ERP peut rester maître des produits/comptes. Certains parcours fonctionnent sans master data locale, avec informations client ou produit portées par la commande. | Preuve directe d’une orchestration sans catalogue maître local obligatoire. Des fonctions d’import et d’administration restent disponibles. |
| [Microsoft IOM — Fulfillment and Returns Optimization](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/fulfillment-returns-optimization) | Sources, listes de sources, contraintes et stratégies sont distinguées et configurables ; les sources peuvent être des magasins, entrepôts ou fournisseurs. | Ce service d’optimisation nécessite des références et paramètres locaux. Leur découpage suit les usages de fulfillment, sans reproduire les sept sujets FLOW. |
| [Fluent — Order Workflow Templates Overview](https://docs.fluentcommerce.com/essential-knowledge/order-workflow-templates-overview) et [Product Sync](https://docs.fluentcommerce.com/essential-knowledge/product-sync-adobe-commerce-connector) | Les produits peuvent venir du PIM, ERP ou Commerce ; le connecteur Adobe documente synchronisation initiale et différentielle. L’orchestration distingue produits/catalogues, lieux/réseaux et catalogues de disponibilité. | Projections et sujets distincts coexistent. Product Catalogue Fluent ne prouve pas l’équivalence au catalogue commercial FLOW ; Virtual Catalogue ne vaut pas Assortment. |
| [Fluent — Manage Locations via UI](https://docs.fluentcommerce.com/by-type/manage-locations-via-ui) et [Creating and Editing Product Catalogues](https://docs.fluentcommerce.com/by-type/creating-and-editing-product-catalogues) | L’interface peut créer/modifier lieux et catalogues, selon configuration et permissions. | Le produit offre aussi une administration locale. Un scénario à maîtres externes ne permet pas d’affirmer « OMS sans administration ». |
| [IBM Sterling — External system integration](https://www.ibm.com/docs/en/order-management-sw/10.0.0?topic=systems-external-system-integration-overview) et [Organization roles](https://www.ibm.com/docs/en/order-management-sw/10.0.0?topic=organization-organizations-roles-participant-associations) | Synchronisation de produits et clients ; rôles Buyer, Seller, Carrier, Node, Enterprise. Les nœuds représentent des lieux ; transporteurs et entreprises configurent certains services et règles. | Les distinctions métier survivent à l’intégration externe. IBM les regroupe autrement, notamment autour des participants. Absence d’administration non démontrée. |

**Réponse à la question OMS : oui pour le scénario ; non démontré pour un produit excluant toute administration.** Le cas Microsoft montre même qu’une donnée nécessaire à l’orchestration n’exige pas toujours un référentiel local autonome. Pour FLOW, la responsabilité de fournir une référence applicable peut rester stable alors que sa réalisation varie selon le sujet ; cela ne décide pas ici d’une architecture de stockage ou d’accès distant.

## Les sept sujets sont-ils pertinents ?

| Sujet actuel | Utilité pour l’orchestration | Appui et appréciation landscape |
|---|---|---|
| Product Reference | Identifier le produit ou la variante, indépendamment de l’offre et de l’exemplaire physique. | Appui direct OMS pour les produits reçus. Distinction de sens solide. |
| Party / Role | Savoir qui intervient et à quel titre. | Organisations/rôles documentés chez IBM ; le périmètre juridique FLOW reste plus précis. À conserver distinct des lieux et habilitations. |
| Product Catalog | Connaître l’offre commerciale de référence. | [Microsoft Commerce B2B](https://learn.microsoft.com/en-us/dynamics365/commerce/catalogs-b2b-sites) documente produits, destinataires et conditions tarifaires. Sujet pertinent, mais catalogue commercial autonome non démontré comme invariant des OMS étudiés. |
| Assortment | Connaître la sélection applicable à un destinataire et une période. | [SAP Retail](https://learning.sap.com/courses/configuring-master-data-in-sap-s-4hana-cloud-private-edition-retail/assortment-1-1) documente son utilisation pour les articles recevables et les commandes. Sa maîtrise reste externe à FLOW. Aucun équivalent autonome établi dans le corpus OMS. |
| Agreement | Connaître les conditions et engagements convenus. | La distinction avec commandes et assortiment demeure cohérente avec U509/CMP205–206. Aucun référentiel générique d’accords établi dans ce corpus OMS ciblé ; ne pas confondre conditions de prix et Agreement complet. |
| Fulfillment Network | Connaître les lieux et les relations utilisables. | Sources/listes Microsoft, lieux/réseaux Fluent, nœuds IBM : appui OMS direct, structures différentes. La charge courante et le choix d’itinéraire restent ailleurs. |
| Service Catalog | Connaître les prestations exécutantes et leurs conditions de référence. | Services transporteurs IBM et paramètres transport Microsoft : recouvrements partiels. [TM Forum TMFC006](https://oda-production.s3.eu-west-2.amazonaws.com/v1.0.0/TMFC006_Service_Catalog_Management_v1.2.0.pdf) documente un catalogue de services plus large, incluant son cycle de vie. Aucun catalogue universel de Backing Services établi chez les OMS examinés. |

**Ces sept sujets sont défendables comme grille métier FLOW ; leur ensemble n’est pas une taxonomie standard OMS.** Leur distinction tient aussi à la question posée par l’orchestration, et pas seulement au cycle de vie de l’objet maître. Une identité produit, une offre, une sélection autorisée et un engagement contractuel ne deviennent pas interchangeables parce qu’ils sont reçus.

Le coût du découpage apparaît lorsque chaque sujet devient automatiquement un couple de capacités. Une provenance ou un format différent ne suffit pas à justifier une capacité métier autonome ; inversement, une implémentation commune ne suffit pas à fusionner des responsabilités différentes.

## Constats à traiter

| Priorité | Constat | Conséquence et recommandation |
|---|---|---|
| Forte | **Distinction incomplète entre réception et consommation.** 28 liens venant d’autres Areas ciblent les Ingestion ; aucune Visibility n’a de lien métier transversal. | Le graphe peut laisser croire qu’utiliser une référence nécessite d’exécuter une ingestion. Requalifier d’abord le service fourni, puis choisir la bonne extrémité. Aucun déplacement automatique vers Visibility : une consultation humaine et une fourniture aux décisions ne sont pas nécessairement le même service. |
| Forte | **La maille 7 × 2 reste insuffisamment justifiée à l’échelle landscape.** Les résultats propres existent, mais les périmètres répètent souvent la même réception/consultation. | Distinguer une vue commune de deux responsabilités et les spécialités sémantiques. N’individualiser ensuite que les capacités dont le bénéfice, le résultat ou la frontière métier sont établis. |
| Moyenne | **L’autorité locale est claire dans l’Area, moins homogène dans les fiches.** « Projection reçue » et « pas de maître local » peuvent être lus comme une copie sans responsabilité. | Clarifier que le cycle de vie d’entreprise reste externe, tandis que FLOW doit savoir quelle référence il utilise. La réception ne garantit pas à elle seule la validité, la complétude ou la fraîcheur. Les règles détaillées ne sont pas encore adoptées. |
| Moyenne | **Assortment n’a pas de consommateur opérationnel explicite.** Le seul lien métier actuel est Agreement → Assortment. | Faire apparaître son utilité pour les décisions/commandes avant d’en déduire de nouveaux liens. L’appui SAP montre un usage possible, pas une règle de blocage adoptée pour FLOW. |
| Moyenne | **Chevauchement rédactionnel Service Catalog.** D14.a Ingestion inclut encore consultation/recherche, désormais couvertes par D14.b Visibility. | Recentrer les descriptions lors du lot de correction retenu. La frontière avec capacité disponible, demande et prestation exécutée reste correcte. |
| Moyenne | **Des autorités restent ouvertes.** Prix appliqué à la commande et reliquat consommable d’Agreement (Q072), contenu/sources/validité du réseau (Q076), maître de configuration des services, identité et versions d’Assortment. | Ce sont des questions de responsabilité, pas des preuves de capacités manquantes. Les traiter par cas d’usage et engagement attendu ; ne pas ajouter un référentiel ou une capacité par défaut. |
| Moyenne | **Risque de lecture excessive du nom.** Authoritative Data peut suggérer un programme de gouvernance ou un MDM d’entreprise. | Hypothèse éditoriale appuyée par la réserve U513, pas résultat d’une étude client. Nommer immédiatement le service concret et expliciter l’autorité locale. |

Les IDs et qualifications des liens sont conservés dans la preuve structurelle. Les portées U479/U507/U509 demeurent applicables : une revue landscape ne remplace pas un accord sur une restructuration.

## Responsabilité locale : le point à rendre explicite

L’absence de création ou d’administration du produit maître ne dispense pas d’une responsabilité sur la référence utilisée : rattachement à la source, prise en compte de sa validité, changement ou retrait reçu, visibilité d’une donnée manquante ou périmée. **Il s’agit de questions à qualifier, pas de nouvelles fonctions supposées présentes.** Les fréquences, garanties, règles de conflit et possibilités de correction ne sont pas déduites du mot Authoritative.

[Oracle ORA Information Management](https://www.oracle.com/technetwork/topics/entarch/oracle-ra-info-mgmt-r3-1-1980395.pdf), §2.3.4 et §6.3.3.4.3, distingue données maîtresses/de classification et décrit une consolidation laissant les sources en contrôle. Le [CDMC de l’EDM Council](https://edmcouncil.org/wp-content/uploads/2023/02/CDMC-Information-Model-Controls-Tests-Mappings-V1.1.pdf), contrôle 3, qualifie explicitement sources et points de fourniture faisant autorité. Ces deux appuis soutiennent la distinction de responsabilité ; ils ne prescrivent pas une Area Supply ni une taxonomie à sept sujets.

Le périmètre dépasse la seule identité des produits et personnes : il comprend aussi conditions, relations et contexte d’application. Cela ne suffit pas à y rattacher toute politique ou tout paramètre d’orchestration. Les règles de décision, leur auteur et leur évolution restent à distinguer des données qu’elles consomment.

**DMN est compatible avec cette séparation, sans la dicter.** [OMG](https://www.omg.org/dmn/) décrit un langage de décisions et règles ; [Camunda](https://docs.camunda.io/docs/components/modeler/dmn/decision-requirements-graph/) distingue décisions, données d’entrée et sources de connaissance. Une donnée de référence peut alimenter une décision ; le graphe DMN ne prescrit ni référentiel unique, ni sept référentiels, ni transfert de toute logique métier vers cette Area. Le rattachement des paramètres partagés reste à instruire, comme le signalait déjà U478/U479.

## Noms : Backing Service Catalog et Authoritative Data

**Backing Service Catalog est cohérent comme précision FLOW.** U488 confirmait que Service Catalog contient les Backing Services ; U497 a conservé le nom Service Catalog tout en appliquant ce sens. Aucun accord antérieur sur le libellé long n’a été retrouvé dans les sources examinées. Le qualificatif distingue les prestations mobilisées par l’orchestration du catalogue des demandes reçues. En contrepartie, Backing reste du jargon : expliquer « prestations mobilisables auprès des exécutants ». Le marché consulté étaye Service Catalog ; il ne prouve pas que Backing Service Catalog soit un nom OMS établi. Recommandation de renommage à discuter, sans changement de périmètre.

Pour l’Area, trois choix raisonnables :

| Option anglaise | Bénéfice | Limite |
|---|---|---|
| Authoritative Data, expliqué par « Référentiels Supply » | Conserve le nom adopté et l’appui précis à l’autorité locale. | Le titre reste abstrait et peut intimider ; l’explication française est indispensable. |
| Supply Reference Data | Rend le contexte Supply et la fonction de référence plus immédiats. | Proposition de libellé contextualisé, pas standard OMS démontré. Reference Data peut désigner seulement codes/nomenclatures dans certaines sources, notamment Oracle ; expliciter que FLOW couvre aussi produits, parties et conditions. |
| Master and Reference Data | S’appuie sur deux catégories reconnues dans l’architecture Oracle. | Évoque davantage la gestion des maîtres et décrit des catégories de données plutôt que le service rendu ; moins adapté au rôle de projection exprimé par Laurent. |

**Préférence éditoriale proposée : Supply Reference Data, accompagné de « Référentiels Supply », si l’objectif prioritaire est l’accès client.** Conserver Authoritative Data dans les inspirations pour expliquer la responsabilité. C’est un compromis de lisibilité, non une supériorité démontrée par test client ; l’ambiguïté du terme Reference Data doit être explicitée. Aucun nom n’est remplacé dans le modèle par cet audit.

Phrase de service proposée : « Fournir aux décisions et opérations Supply les références communes sur les produits, partenaires, offres, sélections applicables, accords, lieux et prestations, en conservant leur lien avec les sources de l’entreprise. » Le détail précise le sens des assortiments et l’autorité locale, sans suggérer la reprise de l’administration des maîtres.

## Recommandation de structure

| Option | Bénéfice | Compromis | Avis |
|---|---|---|---|
| Conserver sept couples Ingestion/Visibility | Traçabilité fine déjà disponible ; spécialités visibles. | Répétition et impression de sept petits systèmes de gestion ; bénéfice propre à démontrer. | Acceptable si responsabilités distinctes établies. |
| **Deux responsabilités communes, sept sujets de lecture** | Rend immédiatement lisible « intégrer les références reçues » et « fournir/comprendre la référence applicable ». | Les différences métier doivent rester explicites ; une éventuelle traduction en capacités canoniques nécessite un nouvel arbitrage et l’examen des rattachements. | **Recommandée au niveau landscape.** |
| Un bloc générique sans sujets | Carte très compacte. | Masque les frontières produit/offre/assortiment/accord et les différences d’autorité ; affaiblit les échanges métier. | Non recommandée. |

Les deux responsabilités proposées ne sont pas de nouveaux noms de capacités adoptés. La seconde doit préciser l’usage par les décisions/opérations et la consultation par les personnes ; elle ne se réduit pas à une interface de recherche. Le choix n’est pas entre « sept MDM » et « une table générique » : les sujets peuvent rester distincts sans imposer des cycles maîtres, applications ou silos séparés.

**Ordre proposé pour la suite :** choisir la présentation client et le niveau de regroupement ; clarifier les services fournis par les liens ; éprouver trois cas (produit reçu, assortiment applicable, prestation et conditions) ; seulement ensuite modifier les capacités/rattachements concernés. Les critères sont résultat métier distinct, responsabilité d’applicabilité, consommateurs et traitement des changements — pas le seul nombre de types de données.

## Changements de ce lot et vérification

U511–U513 sont enregistrés avec leur portée. La fiche backlog Authoritative Data reçoit la comparaison OMS et la distinction entre sujets et capacités, en conservant ses noms, responsabilités et relations. Le rapport, les preuves et les options restent proposés. Les détails de capacités et les 28 liens ne sont pas corrigés dans ce lot d’audit. Les résultats de contrôles sont consignés dans `validation.txt` ; aucune publication Atlas n’est déclenchée.

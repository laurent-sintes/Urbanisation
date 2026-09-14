# Article, SKU, Material, bien et unité logistique

14 septembre 2026 — U176. Point 5 de vocabulaire ; le point 6 reste clos. Audit de SAP S/4HANA/Retail/EWM, Microsoft Dynamics 365 Supply Chain Management, Business Central et GS1. [Sources et conditions de consultation](sources.md), [registre JSON des sources](sources.json), [résultats structurés](../../../modeles/backlog/item-logistic-unit-audit.json).

## Conclusion

**Précision U181 :** SAP donne explicitement une définition d’Article fondée sur une plus petite unité commandable indépendamment et non subdivisible. L’audit initial aurait dû la citer. Elle coexiste avec les catégories génériques et structurées ci-dessous ; voir la [comparaison des définitions](article-definition-comparison.md). La réserve sur SKU universel ne doit pas effacer cette définition SAP.

La différence entre article et colis est fondée. En revanche, **SKU ne signifie pas universellement unité physique insécable, échangeable et vendable**. La référence, la quantité et son unité de mesure, les règles de commercialisation et le regroupement logistique relèvent de dimensions distinctes. Un vêtement vendu à la pièce est un cas possible, pas une définition générale adaptée à tous les achats de Beaumanoir.

Il faut également préciser « tout est un bien » : le vêtement et le carton physique sont des biens matériels ; leur référence et leur code ne sont pas eux-mêmes des biens matériels. Une unité logistique représente un ensemble physique constitué. Une expédition représente un regroupement ou une opération de réalisation. Les réunir sous un mot générique ne supprime pas leurs identités et responsabilités propres.

**Resource reste pertinent comme rôle de mobilisation**, applicable à un lieu, un bien ou un moyen selon le contexte. Il ne fournit pas seul la définition d’une nature d’objet. Aucun objet universel Resource, ni nouvelle capacité, n’est déduit de cet audit.

## 1. Les niveaux à distinguer

| Question | Concept de travail | Exemple local illustratif |
| --- | --- | --- |
| De quel type de produit parle-t-on ? | Modèle de produit / famille, lorsque pertinent | Une famille de chemises |
| Quelle référence opérationnelle distingue-t-on ? | Item / référence d’article ; SKU selon convention | Chemise modèle A, bleu, taille M |
| Quelle quantité est exprimée et dans quelle unité ? | Quantity + Unit of Measure | 12 pièces ; 27,5 mètres de tissu |
| Quelle quantité ou occurrence physique suit-on ? | Biens, lot ou exemplaire identifié lorsque nécessaire | 12 chemises d’un lot ; un exemplaire sérialisé |
| Comment l’offre est-elle conditionnée ? | Conditionnement de référence, composition, unité de commande/vente | Boîte standard de six ; assortiment de tailles |
| Quel ensemble physique est constitué ? | Logistic Unit / Handling Unit | Colis C001 contenant huit M et quatre L |
| Où et dans quel état ces quantités sont-elles suivies ? | Inventory Position | Quantités au site A, dans le colis C001, sous un statut donné |
| Quel acheminement les concerne ? | Shipment / Delivery, sens à préciser | Expédition E001 comprenant C001 et d’autres colis |

Cette grille est une proposition de lecture ; ce n’est ni une hiérarchie obligatoire, ni huit nouveaux objets adoptés. Un lot et une unité logistique ne sont pas nécessairement emboîtés de façon fixe. Des biens fongibles peuvent être suivis en quantités sans identifiant individuel.

## 2. Correspondances entre modèles

Les rapprochements portent sur le rôle du concept. Une cellule ne signifie pas identité de schéma ou de granularité. Product ne signifie pas nécessairement famille : il peut porter une référence opérationnelle ou un service selon le modèle.

| Concept | SAP | Dynamics 365 SCM | Business Central | GS1 |
| --- | --- | --- | --- | --- |
| Référence de produit/article | Material / Product ; Article en Retail, avec catégories | Product, Product master, Product variant ; Released product par entité | Item, variantes ; données SKU spécialisées | Classe d’article commercial, identifiée par GTIN |
| Quantité et unité | Base UoM et unités alternatives | Unités, conversions et précision | Unité de base et unités alternatives | Quantités/mesures et qualifications commerciales |
| Lot / exemplaire suivi | Batch / Serial Number | Dimensions Batch / Serial | Non audité en détail ici | GTIN + lot / GTIN + série |
| Ensemble physique manutentionné | Handling Unit, contenu et emballage | Container et License plate selon le processus | Non audité en détail ici | Logistic Unit identifiée par SSCC |
| Conditionnement référencé | UoM ; articles structurés ; emballage Material | Unités de conditionnement, GTIN | Unités alternatives | Hiérarchie commerciale et rôles base/consumer/orderable/shipping |

Appuis : [SAP S01–S06](sources.md#s01), [Microsoft M01–M07](sources.md#m01), [GS1 G01–G03](sources.md#g01). **License plate, Container, HU et SSCC ne sont pas déclarés synonymes exacts.** Le SSCC est un identifiant ; la HU ou le container est un objet de gestion, avec une portée propre au produit.

## 3. Pourquoi SAP dit Material

SAP décrit Material Master, également appelé Product Master, comme une référence transversale pour les opérations d’achat, de production, de vente et de transport. Son périmètre comprend matières premières, produits intermédiaires, produits finis, marchandises, emballages et certains services. **Material ne se traduit donc pas systématiquement par « matière première » ou par « bien physique ».** Le choix lexical historique n’est pas établi par les sources consultées ; aucune explication historique n’est inventée. [S01](sources.md#s01)

En Retail, SAP parle d’Article. Un article générique peut porter le modèle commun, et les variantes ses combinaisons opérationnelles. Les articles structurés — sets, displays, prepacks — et les unités multiples montrent qu’Article ne désigne pas toujours une pièce élémentaire. La gestion peut porter sur l’ensemble ou ses composants selon le contexte. C’est un point particulièrement utile pour les assortiments de tailles et les flux entre centre de distribution et magasin. [S02](sources.md#s02)

Autre piège : dans MM-IM, SAP emploie aussi **stockkeeping unit pour l’unité de mesure de base du stock**. Une occurrence de stockkeeping unit dans une documentation ne doit pas être traduite automatiquement en « code article ». [S03](sources.md#s03)

Le colis constitué se rapproche plutôt d’une **Handling Unit** : emballage et contenu physique, avec identité et possibilité d’imbrication. La référence du carton vide peut être un Material ; le carton rempli particulier peut être représenté par une HU. Le type d’emballage et l’ensemble constitué sont deux rôles différents. [S01](sources.md#s01), [S04](sources.md#s04)

## 4. Ce que dit Microsoft

Dans **Dynamics 365 SCM**, Product porte la définition de référence ; son type peut être Item ou Service. Un Product master permet des variantes. Released product signifie produit rendu utilisable dans une entité juridique, pas marchandise sortie du stock. [M01](sources.md#m01)

Le Product number et l’Item number n’ont pas toujours le même périmètre : le second est associé à une entité juridique. Pour un produit à variantes, l’identification doit aussi déterminer la combinaison concernée. Les conditionnements et identifiants GTIN sont traités séparément. On ne peut donc pas poser systématiquement « Item number seul = variante = exemplaire = SKU ». [M02](sources.md#m02)

**Business Central doit être distingué de SCM.** Une Stockkeeping Unit y conserve les données d’un Item pour une localisation et/ou une variante, notamment pour sa gestion d’approvisionnement. Ce sens n’est ni un colis, ni la plus petite pièce vendable. [M03](sources.md#m03)

Les unités de mesure permettent des conversions, des précisions et des arrondis ; Business Central distingue aussi unité de stock et unités d’achat/production/vente. La divisibilité est donc une règle de quantité et d’opération à définir, pas une propriété donnée par le mot SKU. [M04](sources.md#m04), [M07](sources.md#m07)

Dans le WMS SCM, le **Container** regroupe les articles emballés avec son identité et ses caractéristiques physiques ; l’expédition reste distincte. Les License plates interviennent également dans le suivi. Les lots et séries sont d’autres dimensions de traçabilité, indépendantes du seul numéro d’article. [M05](sources.md#m05), [M06](sources.md#m06)

## 5. GS1 : distinguer identité et rôle commercial

GS1 sépare explicitement classe de produit, lot, exemplaire et unité logistique par leurs mécanismes d’identification. Le GTIN identifie une classe ; l’identification d’une instance demande une information supplémentaire. La référence n’est donc pas l’exemplaire matériel. [G01](sources.md#g01)

Les qualifications **Base Unit, Consumer Unit, Orderable Unit et Shipping Unit** sont distinctes. La base correspond au niveau inférieur d’une hiérarchie commerciale définie ; cela n’établit pas une indivisibilité physique universelle. [G03](sources.md#g03)

Les deux axes commerce/logistique se croisent : une unité logistique peut aussi être une unité commercialisée, et un seul article commercial peut être transporté en plusieurs morceaux ou colis. Il ne faut donc pas imposer « un SKU = un colis » ni « tout colis contient plusieurs SKU ». [G02](sources.md#g02)

Enfin, les biens à mesure variable sont explicites, notamment les tissus et rouleaux. Un bien référencé peut être commandé selon une mesure ; la « pièce entière » n’est pas l’unité universelle de tous les échanges. [G04](sources.md#g04)

## 6. Épreuve sur les récits Beaumanoir et Boardriders

Ces exemples éprouvent le modèle ; ils ne prouvent aucune configuration installée.

| Situation | Épreuve sémantique | Résultat de l’audit |
| --- | --- | --- |
| Produits finis, modèle/couleur/taille | Distinguer référence opérationnelle et quantité de vêtements | Compatible avec Article/variant ou Product variant ; pièce entière peut être une règle locale |
| Fabrication à façon, achat de tissus | Commander une longueur de matière et suivre un rouleau physique | Contre-exemple à une définition universelle du SKU comme pièce insécable |
| Assortiment de tailles | Commander un pack et éventuellement répartir ses composants | Définir composition et règles de déconditionnement ; ne pas confondre pack référencé et colis réel |
| Colis contenant huit M et quatre L | Conserver référence et quantité de chaque contenu sous un identifiant logistique | Deux références, douze pièces, un colis : trois granularités |
| Reconditionnement de douze pièces en deux cartons | Modifier le regroupement sans créer douze nouveaux vêtements | Le nombre et l’identité des unités logistiques peuvent changer indépendamment des quantités de biens |
| Ressources futures pour les comportements Boardriders | Promettre une quantité avant connaissance des colis finaux | La ressource de promesse ne doit pas exiger une HU ou un SSCC déjà constitué |

Le dernier cas est une exigence à éprouver contre les règles opérationnelles, pas la preuve que tout achat ferme autorise toute promesse.

## 7. Effets sur le projet et propositions

| Élément courant | Constat | Suite proposée, sans adoption |
| --- | --- | --- |
| D08 Product Reference et D08.d | L’autonomie de la référence et son ingestion depuis un maître externe sont cohérentes | Préciser le grain modèle/variante et l’emploi local de SKU ; examiner les unités, compositions et conditionnements de référence utiles, sans créer de capacités d’administration |
| TER004 Article / unité de gestion | La définition ancienne risque de rapprocher trop fortement bien et référence malgré sa réserve sur l’exemplaire | Exprimer explicitement « référence opérationnelle permettant de distinguer et gérer des quantités de biens », comme proposition locale |
| D01 Inventory Management | Le suivi peut concerner des quantités, lots et unités logistiques en stock ou transit | Ne pas compter à la fois le colis et son contenu comme deux fois la même marchandise ; distinguer le carton lui-même s’il est suivi comme emballage |
| D03 / Supply Assignment | Resource doit rester utilisable pour les biens présents ou futurs | Qualifier la ressource dans son contexte ; ne pas exiger une unité logistique déjà constituée ni étendre Resource aux seuls biens |
| D07 et Services | Emballer, manutentionner et transporter mobilisent des identités opérationnelles | Éprouver les liens entre prestation, contenu et unités logistiques ; le détail de l’exécution reste en adhérence |
| D13 Fulfillment Network | Un magasin peut être une ressource dans un raisonnement | Conserver son identité de lieu ; aucune fusion des lieux et articles dans un objet Resource universel |

Je recommande de réserver **Goods / biens** au collectif matériel, **Item / référence d’article** à la définition opérationnelle, **Quantity + UoM** à la mesure et **Logistic Unit** à l’ensemble physique constitué pour manutention, stockage ou transport. Ce sont des propositions de vocabulaire ; elles ne constituent pas encore un inventaire d’objets adopté. Resource reste un rôle transversal ; Material reste une correspondance SAP contextualisée.

La prochaine décision utile est le sens local d’**Item/SKU** et la manière d’exprimer sa quantité minimale ou sa divisibilité selon l’opération. Le choix ne doit pas être déduit d’un libellé éditeur.

## Limites et résultat de contrôle

L’audit compare des modèles documentés, pas leurs performances ni leur installation. Les éditions SAP et Microsoft sont hétérogènes ; leurs particularités sont conservées dans les sources. Les concepts de colis et de traçabilité Business Central ne sont pas audités aussi finement que ceux de SCM. Les relations détaillées, frontières d’agrégats et maîtres des futures unités logistiques restent ouverts. Les domaines Business Services demeurent différés.

Aucune capacité ou donnée publiée n’est modifiée. Le registre JSON contient les correspondances, hypothèses, exemples et impacts proposés ; les définitions de capacités continuent à provenir du modèle courant.

## Précision Retail et wholesale — U177 à U179

Le nom SAP Retail ne réserve pas le modèle Article au commerce de détail. Les usages wholesale sont explicitement documentés ; Fashion réutilise cette architecture sur un périmètre fabrication/wholesale/retail. Voir le [complément sourcé](retail-wholesale.md) et ses [constats structurés](retail-wholesale.json).

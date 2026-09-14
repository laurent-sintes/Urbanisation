# Stock unifié, contenu et conditionnement des flux

14 septembre 2026 — U187 à U192. Orientation de Laurent : partir du modèle de stock unifié et décrire les conditionnements inbound/outbound, qui peuvent différer. [Propositions structurées](../modeles/backlog/unified-inventory-packaging.yaml).

La référence article indique ce dont on suit les quantités. Elle ne suffit pas à décrire comment ces quantités sont regroupées physiquement. L’exploration doit donc distinguer la position de stock, le contenu mesuré, le regroupement logistique identifié et les faits qui les font évoluer. Les noms Item/Article Reference, Inventory Position et Logistic Unit/Container restent des candidats.

La relation de contenu est centrale : quelle quantité de quel article est dans quelle unité logistique, quand et selon quelle source ? Lot, série, imbrication et distinction prévu/constaté ne sont ajoutés que si utiles. Cette relation n’est ni une hiérarchie de capacités ni une cardinalité logicielle déjà adoptée. Une spécification de conditionnement est distincte d’un contenant particulier.

| Étape illustrative au point A | Description | Quantité d’articles en A |
| --- | --- | --- |
| Réception inbound | Cartons I1 et I2, douze unités chacun | 24 |
| Reconditionnement pour stockage | Les vingt-quatre unités sont réunies dans le bac S1 | 24 |
| Packing outbound | Créer O1, O2 et O3 de quatre unités chacun ; douze restent dans S1 | 24 |
| Expédition outbound | O1, O2 et O3 quittent A | 12 |

Le reconditionnement seul change les regroupements, pas la quantité de biens dans cet exemple sans perte ni transformation. L’historique du contenu permet de relier entrants et sortants. Les nombres de cartons ne se somment pas aux quantités de marchandises ; les contenants imbriqués ne doublent pas leur contenu.

Inbound et outbound sont relatifs au point de stock. Un transfert A vers B est outbound de A et inbound de B. Dans un stock unifié incluant A, B et le transit, cela ne constitue pas une sortie puis une nouvelle création de biens : la continuité et les vues attendues doivent être rapprochées sans double compte. Le périmètre de propriété ne se déduit pas du seul déplacement.

Microsoft décrit Container comme la structure physique dans laquelle sont emballés les articles, avec informations de suivi et de dimensions. La [source consultée](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/packing-containers) traite l’emballage outbound ; elle ne prouve pas une équivalence universelle du mot Packaging ni un schéma inbound identique.

Les propositions interrogent D01 pour le suivi, les faits et la visibilité ; D07 pour les faits remontés par l’exécution ; D03 pour les contraintes de conditionnement utiles à la promesse. Un colis final peut être inconnu quand une promesse est étudiée. Les références D08/D13 restent externes et aucune nouvelle maîtrise de conditionnement n’est déduite. L’exécution du reconditionnement reste en adhérence de FLOW.

L’orientation utilisateur est conservée comme telle. Les définitions, noms, relations et invariants proposés ne sont pas automatiquement validés ; aucune capacité ou entité n’a été ajoutée à la carte active.

## Précision stockage et packing — U188

Laurent précise que le reconditionnement peut avoir lieu pour le stockage et que le packing des entrepôts peut créer les containers outbound à la volée. L’identité et la composition des contenants ne sont donc pas figées par l’inbound.

Proposition : représenter les usages inbound, stockage et outbound avec les mêmes concepts de contenu et d’unité logistique, sans créer automatiquement trois natures d’objet ou un cycle obligatoire. Les contenants peuvent être conservés ou remplacés ; une relation de contenu doit permettre de restituer la situation au moment des faits. L’exemple du bac S1 est illustratif, pas un processus imposé.

Une estimation de conditionnement et ses contraintes peuvent servir au pilotage avant que les colis physiques n’existent. La composition constatée arrive au moment du packing. Le stock unifié doit en recevoir les faits utiles ; l’exécution du packing reste celle des services logistiques. Les responsabilités de décision et le détail de la traçabilité restent à instruire. Aucun nouveau domaine ou capacité FLOW n’est créé par déduction.

## Packing contractuel et ATP — U189

Laurent précise que l’ATP d’une commande B2B doit prendre en compte le packing imposé par les conditions du client wholesale. La présence du stock ne prouve donc pas, seule, qu’une livraison conforme est réalisable.

Proposition : distinguer exigences de packing applicables, possibilités de réalisation et containers effectivement constitués. Les exigences peuvent être connues avant la promesse ; les identifiants et contenus finaux peuvent apparaître au packing. Conserver la provenance du contrat et la portée des exigences sur la commande.

Exemple proposé : vingt-quatre unités sont présentes en vrac ; la commande attend six cartons de quatre, mais le packing n’est réalisable que demain. On ne peut pas promettre une expédition conforme aujourd’hui sur le seul constat des quantités disponibles. Le packing et l’acheminement contribuent à la date réalisable. Cet exemple ne fixe ni règle de capacité ni seuil de service réel.

Rôles à instruire : D11 projette les conditions contractuelles, D04 porte ou référence les exigences de la commande, D06 apprécie les possibilités de packing, D03/ATP en tient compte dans la promesse, D07 suit les prestations et faits remontés. Ces responsabilités sont des propositions d’analyse ; aucune nouvelle capacité Packing ni instance d’objet n’est créée dans la carte.

Dans notre distinction ATP/CTP, mobiliser un packing possible dans les moyens et règles existants n’est pas automatiquement un plan d’adaptation CTP. Une modification de ces moyens ou engagements est à qualifier séparément. Le placement terminologique chez les éditeurs n’est pas établi par cette orientation locale. L’exécution reste en adhérence de FLOW.

## Références et unités — proposition U190

Laurent propose Product comme référence de design, Article ou Product Unit pour les biens unitaires, Container comme référence de design et Container Unit pour les contenants concrets. Il décrit un stockage direct dans un emplacement du Fulfillment Network ou dans un contenant, avec des contenants imbriqués. Ces propositions sont en instruction ; l’univers Design mentionné n’est pas créé dans la carte.

À l’étape U190, le grain d’Article/Product Unit était à préciser. U191 tranche ensuite : chaque exemplaire physique avec son identité propre. Le nom Référentiel ne suffit pas à distinguer ces deux usages. Container Type ou Container Specification est un libellé proposé par Codex pour rendre explicite le rôle de définition du contenant.

GS1 distingue le GTIN de classe commerciale, le GTIN complété d’une série pour un exemplaire et le SSCC de l’unité logistique. Le support scanné ne prouve pas une identité par pièce. Une identité logistique ne démontre pas non plus une indivisibilité. L’identification d’un actif réutilisable constitue encore un rôle distinct. [Source GS1](https://ref.gs1.org/architecture/system-architecture/), texte relu le 14 septembre 2026, table4-1.

La lecture Article comme référence vendable a été écartée pour ce modèle par U191. Article/Product Unit désigne un exemplaire physique avec identité propre. La collecte et la correspondance de ces identités restent à préciser si les sources ne fournissent que des quantités ; ne pas confondre identité créée dans le modèle et traçabilité physique démontrée. Une définition Product limitée au modèle de design peut nécessiter une précision supplémentaire du grain commercial/variante ; ce point reste ouvert.

Les collections de références et les registres d’unités physiques ou de positions ne doivent pas être confondus : l’orientation de projection externe des référentiels ne transforme pas toutes les données transactionnelles en références en lecture seule. L’autorité des identités/contenus des unités logistiques reste à instruire avec les exécutants.

## Grain clarifié — U191/U192

Laurent tranche : Article/Product Unit désigne chaque exemplaire physique avec son identité propre. Il confirme que cette notion est indépendante du code-barres. Ces points remplacent les réserves historiques sur le choix référence versus exemplaire ; ils ne valident pas tous les détails proposés.

| Terme de travail | Nature | Illustration |
| --- | --- | --- |
| Product | Référence de design du bien | Définition du produit concerné, grain à préciser |
| Article / Product Unit | Exemplaire physique individuel | Cette pièce précise |
| Container | Référence de design du contenant | Modèle de carton ou de bac |
| Container Unit | Contenant physique particulier | Ce carton précis ou ce bac précis |

Le contenu d’un Container Unit relie des exemplaires Product Unit et/ou d’autres Container Units. Les unités peuvent être situées directement dans les emplacements ou par leur contenant. Ces liens doivent pouvoir évoluer au reconditionnement et restituer les situations passées ; les règles détaillées restent proposées.

Le modèle ne doit pas conditionner l’existence conceptuelle d’un exemplaire à une étiquette particulière. En revanche, la manière de reconnaître physiquement un exemplaire, de lui attribuer un identifiant et de rapprocher plusieurs observations n’est pas encore définie. Le simple fait de générer un identifiant ne prouve pas une traçabilité physique. Le rôle exact de Design et le niveau de définition Product restent à instruire.


## Product Variant, Serial Number et GTIN — U193

Laurent précise qu’un Product Unit peut avoir un Serial Number et rapproche le GTIN du Product Variant. La structure de travail proposée devient Product (modèle de design), Product Variant (déclinaison précise, par exemple bleu/taille M), puis Product Unit (chaque exemplaire physique). Le niveau Variant et ses relations restent en instruction ; le grain individuel de Product Unit demeure tranché.

Le numéro de série est une donnée d’identification éventuelle, le code-barres un support de représentation. Dans GS1, la combinaison GTIN + numéro de série identifie l’exemplaire ; le numéro seul n’est pas présumé globalement unique. Notre modèle n’impose ni GS1 ni un numéro de série fabricant pour l’identité propre. [GS1 : sérialisation](https://support.gs1.org/support/solutions/articles/43000734238-how-does-serialisation-differ-from-unique-identification-in-the-gs1-system-).

Le GTIN correspond au niveau de référence commerciale, avec des distinctions de variante et de conditionnement commercial. Une unité et une boîte de plusieurs unités peuvent avoir des GTIN distincts : ne pas figer une relation un pour un entre Product Variant et GTIN. Cela ne donne pas un GTIN individuel à chaque Container Unit. [GS1 : produits et conditionnements](https://gs1.fi/en/barcodes/gs1-suppliers/product-and-packaging-coding). Sources consultées le 14 septembre 2026.

Les précisions sont structurées dans entity_structure_review.product_variant_and_identity_review. Aucun objet ajouté à la carte active et aucune publication.


## Un contenant est-il un produit ? — U194

Laurent observe une même structure référence/variante/unité et propose que Container soit un produit dont les règles de composition diffèrent. L’hypothèse est en instruction. Un bac acheté vide puis utilisé pour transporter des chemises illustre une même chose physique décrite comme produit et comme contenant.

SAP appuie la structure commune : Packaging Material est un type particulier de Material. Des caractéristiques supplémentaires portent poids/volume admissibles ; les instructions de packing précisent contenu, quantités, imbrication et exigences client. [SAP — Maintaining Packaging Information](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-warehouse-management/maintaining-packaging-information_d0d86e60-5eb5-4b2f-9ad8-1277f3fc3dd1). SAP définit par ailleurs la Handling Unit comme l’ensemble emballage/support et biens contenus, ce qui ne se réduit pas au seul contenant physique. [SAP — Handling Unit](https://help.sap.com/docs/PRODUCT_ID/3d97bec9bf1649099384bb8167df3cf2/a2043fc0-30be-41ec-b485-9a383eb901ac.html?locale=en-US&state=PRODUCTION&version=9.5.0.2). Sources consultées le 14 septembre 2026.

Proposition locale : partager la structure Product → Product Variant → Product Unit, et décrire Container Unit comme un rôle ou une spécialisation de l’exemplaire apte à contenir/supporter d’autres unités. Cela ne tranche pas un héritage IT ni une fusion de modèles. Un contenant vide conserve son aptitude ; sa composition réelle change sans changer nécessairement son identité. Le regroupement logistique et le support physique ont des identités/cycles à distinguer lorsque nécessaire.

Les règles concernent des caractéristiques physiques, les contraintes de packing du contexte (contrat, commande, usage) et l’intégrité des relations : pas de cycle, composition datée, comptage cohérent. Elles ne sont donc pas toutes attachées au seul référentiel du contenant. Contenance physique, nomenclature de fabrication et assortiment commercial restent des relations différentes : les chemises ne sont pas des composants du produit bac.

La formulation unités portant un GTIN est recevable pour le marquage de leur référence ; elle ne donne pas une identité individuelle par GTIN. La précision U193 demeure. Aucun objet actif fusionné ; alternative structurée dans entity_structure_review.container_as_product_review.



## Product commun, rôles Article et Container — U195

Laurent valide : « Un Product porte un rôle : Container ou Article ». Le choix courant est donc le rôle, situé au niveau Product. Les modèles antérieurs séparant obligatoirement Product et Container comme références sont conservés en historique dans l’annexe. Product Unit conserve son grain d’exemplaire physique individuel ; Article désigne désormais un rôle, et non le nom alternatif de toute unité physique.

Proposition de lecture : Article qualifie le bien constituant le contenu à stocker/déplacer ; Container qualifie le bien destiné à contenir ou supporter d’autres unités. Référence, variante et exemplaire forment la structure commune. La composition réelle relie les Product Units ; les contraintes définissent ce qui est autorisé. Les définitions détaillées, l’exclusivité ou le cumul des rôles, leurs variations et leurs cycles restent à instruire. Le mot ou de la contribution ne suffit pas à imposer une cardinalité technique.

Le principe et les noms de rôles sont validés dans product_roles_decision, avec source U195 et portée explicite ; les compléments restent proposés. Aucune nouvelle entité de la carte active ni publication implicite.

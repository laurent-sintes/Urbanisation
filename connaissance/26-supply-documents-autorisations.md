# Supply : documents d’autorisation et référence article

11 septembre 2026 — orientation de Laurent [U100](01-contributions-utilisateur.md#u100), reformulée en F210–F212. Les distinctions et pistes de conception signalées ci-dessous sont proposées par Codex ; elles ne constituent ni une configuration existante ni un standard de marché.

## Orientation retenue

La Supply transactionnelle doit pouvoir piloter des mouvements de marchandises à partir de documents qui en portent l’autorisation. Commande d’achat, commande de vente et autorisation de retour peuvent être comprises sous cette sémantique commune, tout en conservant leur origine et leur contexte. La couche processus porte les parcours achat, vente, après-vente et réassort. Le socle décide des actions appropriées au contexte ; DMN est cité comme exemple de moyen, sans choix de technologie.

Cette orientation précise U54–U57 et U61 : les deux couches portent du métier, chacune avec ses objets, sa persistance et son urbanisation. La couche processus exprime les situations commerciales et l’organisation ; le socle exprime les aptitudes génériques de contrôle de la Supply. Les échanges restent fondés sur des contrats durables. La logistique exécutante demeure en adhérence, hors développement FLOW, avec l’autonomie de C-Log préservée.

La séparation Purchase Order / Sales Order observée dans les produits ne devient donc pas une prescription de deux domaines transactionnels. Elle sert à rechercher les différences de règles et de résultats que le socle devra savoir traiter. Une sémantique documentaire commune n’impose pas pour autant un domaine Supply unique ni un objet ou aggregate root universel.

## Distinctions proposées pour préciser le modèle

| Notion | Sens de travail | Conséquence à éprouver |
| --- | --- | --- |
| Document d’autorisation | Pièce métier attestant qu’un mouvement est autorisé, dans un périmètre et sous des conditions. | Distinguer son origine commerciale, son effet autorisant et sa validité ; une commande reçue n’est pas automatiquement exécutable sans conditions. |
| Décision transactionnelle | Choix métier de l’action admissible selon contexte, références, autorisation et ressources. | L’aptitude appartient à un domaine ; le moteur la réalise. Les neuf capacités d’Order Promising restent validées. |
| Engagement d’exécution | Résultat de réalisation attendu et, selon les règles, accepté par son exécutant. | Distinguer autorisation commerciale et acceptation de réalisation ; frontière D04/D07 à revoir. |
| Fait de réalisation | Constat de ce qui a effectivement eu lieu, associé aux documents et ressources concernés. | Une autorisation n’atteste pas un départ ou une réception. Le rapprochement éclaire ce qui reste autorisé ou engagé. |
| Party et lieu | La Party porte un rôle et une responsabilité ; le lieu situe une origine ou une destination. | Proposer des liens Party–Location : un fournisseur peut avoir plusieurs sites, un client plusieurs adresses. Un point du réseau n’est pas nécessairement un espace de stockage. |

Ces distinctions développent le modèle [objets, documents et faits](24-capacites-objets-et-faits.md), sans fixer cardinalités, agrégats ni stockage technique. Elles évitent aussi de confondre autorisation métier de mouvement et habilitation RBAC d’un utilisateur.

Pour l’exploration, un document pourrait préciser article, quantité/unité, parties et rôles, origine/destination lorsqu’elles sont connues, conditions temporelles et références d’autorisation. Ce sont des informations candidates, pas un contrat d’API. La possibilité de décider une source après réception de la demande reste à éprouver avec Fulfillment Source Decision ; ne pas exiger deux lieux définitivement fixés trop tôt.

## Effet sur la carte

**D04 Commercial Commitments reste une proposition à refondre**, en examinant les autorisations documentées et leurs évolutions avec D07 Execution Commitments and Facts. Ses quatre anciennes aptitudes sont conservées comme matière de revue, pas comme validation de domaines Achat/Vente. En particulier, décider d’une solution commerciale de retour/remplacement et rendre son mouvement admissible à la Supply peuvent relever des deux modèles : leur frontière doit être précisée avant de renommer ou déplacer D04.d.

La généricité ne réduit pas Inventory Management ou Order Promising à des déplacements. Protection, réservation, connaissance du futur et révision de promesse restent nécessaires. Un changement d’état logique peut se produire sans transport de marchandises.

**Le référentiel article est autonome par rapport à Catalog**, conformément à U100 : l’identité du SKU peut être référencée dans plusieurs catalogues. Catalog porte les propositions commerciales et informations applicables déjà décrites en U97 ; il ne devient pas maître de l’identité de l’article. Prix, attributs, unités et conditionnements restent à détailler selon leurs autorités.

La carte 0.7 réactive **D08**, même sujet article qu’historiquement, sous le nom proposé **Product Reference**, avec la nouvelle aptitude **D08.d Product Reference Ingestion**. Les anciennes D08.a–c d’administration/qualification restent retirées. Cette traduction dans la carte prolonge le principe d’ingestion seule U97 ; le principe d’autonomie est confirmé, la formulation détaillée proposée. D09, D11, D08 et D12 restent contigus. Aucun PIM maître ni processus de référencement n’est développé dans le socle par cette décision.

## Comparaison et points ouverts

L’[audit U99](../audits/2026-09-11-modele-marche-achats-ventes-referentiels.md) reste une preuve datée du marché. Sa recommandation d’arbitrer entre domaines Purchase/Sales est réorientée par U100 : comparer les variantes comme tests du socle générique. L’autonomie produit/catalogue est appuyée partiellement par le corpus ELM090/ELM091 ; Product Reference Ingestion reste un libellé local. La correspondance précise du modèle d’autorisation documentaire au marché **n’est pas encore établie** : [CMP058](../marche/comparaisons.md#cmp058).

[Q070](06-questions.md#q070) est partiellement répondue sur l’orientation générique, encore ouverte sur les frontières D04/D07. [Q071](06-questions.md#q071) est partiellement répondue sur l’autonomie article ; les autres références restent à examiner. [Q074](06-questions.md#q074) porte sur le cycle d’autorisation, les décisions et les preuves de réalisation. Les responsabilités du prix et du consommé contractuel restent ouvertes en Q072. Aucun nouveau moteur, instance partagée ou domaine de capacités techniques adopté.

## Référentiel du réseau — U102

Laurent confirme Party ≠ lieu et propose **Fulfillment Network**. La [vue D13](25-domaines-coeur-et-epreuve-recits.md#d13-fulfillment-network) explicite désormais ce référentiel, distinct des parties, avec une réception seule proposée dans la continuité de U97. Le contenu candidat couvre points, relations, caractéristiques et liens aux parties responsables ; sa granularité et ses maîtres restent ouverts. Les exemples de nœuds et attributs sont des propositions Codex.

Le réseau décrit les points et possibilités de référence ; les documents de mouvement s’y rapportent sans exiger que toute destination ponctuelle soit un nœud permanent. D06 apprécie les possibilités et capacités restantes, D03 décide source et acheminement selon les autorités établies, D07 porte engagements et faits. Aucune conception ni exécution logistique ajoutée aux développements FLOW. Q074 partiellement répondue sur Party/lieu ; Q076 ouverte sur le réseau.

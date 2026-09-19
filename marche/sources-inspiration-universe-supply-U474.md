# Sources d’inspiration — proposition éditoriale U474

Discussion préparée par Codex le 19 septembre 2026 à la demande [U474](../connaissance/01-contributions-utilisateur.md#u474). Les alternatives et rapprochements ci-dessous sont proposés, sans adoption implicite. Ce document explique une proposition de lecture ; le modèle YAML reste l’autorité.

Suite de la discussion — [U475](../connaissance/01-contributions-utilisateur.md#u475) retient le format C et le contenu présenté dans la réponse : choix, tableau, synthèse et exemple Supply. Le backlog porte désormais cette rédaction. L’accord ne s’étend pas aux précisions documentaires non présentées, aux autres fiches ou à une conformité des modèles. La proposition initiale est conservée ci-dessous pour retracer le choix.

État étudié : `modeles/release/index.json` désigne le descripteur `urbanisation-v013-2026-09-19-122848.yaml`, puis `2026-09-19.6/model.yaml`. La fiche `universe-supply` publiée et le backlog courant ont été consultés. Son nom est adopté en U373. Ses comparaisons actuelles portent sur CSCMP, Microsoft et Oracle ; la recherche scientifique et SCOR sont des compléments de discussion, non ajoutés au catalogue par cette note.

## Avis et alternatives

Le nom « Sources d’inspiration » ouvre la rubrique à la recherche et aux référentiels professionnels. Il faut y conserver les références qui éclairent une différence, même lorsque FLOW ne reprend pas leur approche. Une ressemblance ne permet pas d’attribuer à une source l’origine historique du modèle.

Le rendu actuel met en avant les titres de documents et répète les raisons du nom et de la définition pour chaque source. Il cache les points communs et différences derrière un accordéon et ne compare pas les sources entre elles.

| Option | Contenu | Bénéfice | Compromis |
| --- | --- | --- | --- |
| A — Tableau | Choix en deux phrases, puis tableau commun Nom / Périmètre / Approche | Comparaison rapide | Les raisons et les exemples se lisent mal dans des cellules longues |
| B — Récit | Choix, puis trois paragraphes courts sur le nom, le périmètre et l’approche, avec exemple | Lecture naturelle et nuancée | Comparaison moins immédiate entre plusieurs sources |
| C — Format combiné, recommandé | Choix, tableau court, conclusion transversale et exemple | Répond aux questions métier en deux niveaux de lecture | Exige de supprimer les répétitions |

Recommandation : option C. Le paragraphe d’ouverture affirme le choix ; le tableau rend les références comparables ; le cas montre ce que leur différence signifie. Les détails bibliographiques restent accessibles après cette lecture. Les limites qui changent le sens d’un rapprochement restent visibles, par exemple « même nom, périmètre différent ».

## Exemple proposé : Supply Chain Orchestration

> Nous appelons cet univers **Supply Chain Orchestration** parce qu’il organise comment satisfaire les demandes : quelles quantités fournir, depuis où, à quelle date et avec quels moyens. Il coordonne les commandes, les stocks, les engagements et les prestations, tandis que les applications de référence gèrent les données produit et partenaires, et que les entrepôts et transporteurs réalisent les opérations physiques.

Oui, les sources consultées traitent de concepts voisins. Elles abordent cependant des objets différents : une responsabilité exercée par un acteur, un référentiel de processus, une discipline professionnelle ou un logiciel. Le tableau est une lecture comparative proposée par Codex, pas une déclaration d’équivalence des auteurs.

| Référence | Nom employé | Périmètre | Approche |
| --- | --- | --- | --- |
| Recherche — Zacharia, Sanders et Nix | Orchestrator | Un prestataire logistique coordonne plusieurs entreprises | Partager l’information et faire coopérer les partenaires |
| ASCM — SCOR DS | Orchestrate, dans un modèle de Supply Chain | Comprend stratégie, règles, risques, ressources et performance | Organiser et améliorer les processus de la chaîne |
| CSCMP — définition professionnelle | Supply Chain Management | Ensemble plus large : approvisionnement, transformation, logistique et coordination | Faire travailler ensemble activités et partenaires |
| Microsoft — suite Dynamics 365 | Supply Chain Management | Produits, stocks, achats, planification, production, entrepôts et transport | Réunir ces fonctions dans une suite logicielle |
| Oracle — module Fusion Cloud | Supply Chain Orchestration | Coordonner les approvisionnements en lien avec la demande et leurs changements | Faire coopérer plusieurs applications pour satisfaire les demandes |
| **Notre modèle FLOW** | **Supply Chain Orchestration** | **Commandes, stocks, engagements, optimisation et coordination de la réalisation** | **Décrire les responsabilités métier et leur coopération, indépendamment des outils** |

Lecture des rapprochements proposés :

- **CSCMP et Microsoft** utilisent le terme SCM pour un ensemble large ; l’un définit une discipline et l’autre le périmètre d’une suite. FLOW conserve un périmètre plus ciblé, notamment en laissant la gestion des données de référence et la réalisation physique aux responsables concernés.
- **SCOR et l’article scientifique** éclairent la coordination entre acteurs. SCOR la traite notamment sous l’angle de la stratégie et de la gouvernance ; l’article étudie le rôle d’un prestataire. FLOW décrit ce que l’entreprise doit savoir faire, sans imposer un prestataire ni reprendre tout le périmètre d’Orchestrate de SCOR.
- **Oracle et FLOW** emploient le même nom et partagent l’idée d’adapter les moyens à la demande. Oracle donne ce nom à un module qui coopère notamment avec Order Management, Inventory Management et Order Promising ; FLOW regroupe aussi les responsabilités de commandes, stocks et promesses. Les noms coïncident, les frontières ne coïncident pas.

### Exemple éditeur reformulé

Oracle décrit un fournisseur qui ne peut livrer que 75 unités sur les 100 attendues. Son orchestration recherche une autre source pour les 25 manquantes ; si elle n’en trouve pas, elle signale l’écart au responsable de la commande. Cet exemple vient de la documentation, pas d’une observation Beaumanoir.

**Lecture FLOW proposée :** ce cas relie le suivi de ce qui est attendu, l’examen d’autres moyens de satisfaire la demande et les conséquences sur la quantité ou la date promises. L’univers coordonne ces responsabilités ; les exécutants préparent et transportent les produits. Le cas illustre la finalité de l’univers sans dicter le découpage de toutes ses capacités.

### Variante entièrement rédigée — option B

Le SCM, tel que le décrit CSCMP, couvre l’ensemble de la chaîne ; Microsoft emploie aussi ce nom pour une suite étendue. Nous retenons « Orchestration » pour préciser notre responsabilité : organiser la satisfaction des demandes tout en conservant la gestion des données de référence et la réalisation physique chez les responsables concernés. Oracle emploie ce même nom pour un module plus ciblé, alors que SCOR et la recherche consultée abordent aussi la coopération entre acteurs sous un angle organisationnel. FLOW s’appuie sur cette idée commune de coordination, avec ses propres frontières métier.

## Documents consultés et limites

Tous consultés le **19 septembre 2026**. Synthèses sélectives, sans reproduction intégrale. Les comparaisons à FLOW sont les interprétations proposées ci-dessus.

| Source primaire | Édition / passage effectivement consulté | Appui et limites |
| --- | --- | --- |
| [Zacharia, Sanders et Nix — The Emerging Role of the Third-Party Logistics Provider (3PL) as an Orchestrator](https://bpb-us-w2.wpmucdn.com/wordpress.lehigh.edu/dist/e/653/files/2018/01/Zacharia-JBL-3PL-Orchestrator-Role-2011-27dqkbl.pdf) | Journal of Business Logistics, 2011, 32(1), 40–54 ; DOI 10.1111/j.2158-1592.2011.01004.x ; introduction, modèle, exemples et limites | Étude du rôle d’un prestataire ; entretiens dans un seul prestataire spécialisé transport. Atteste un usage scientifique d’orchestration, sans définition universelle ni équivalence avec FLOW. |
| [ASCM — SCOR Digital Standard](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/) | Page sans numéro d’édition ; présentation et définitions Orchestrate, Plan, Order, Source, Transform, Fulfill, Return, texte restitué par l’index de recherche | L’ouverture directe a renvoyé 403 ; comparaison limitée aux définitions primaires restituées, sans prétendre avoir audité le standard complet. Orchestrate dépasse la coordination opérationnelle. |
| [CSCMP — SCM Definitions and Glossary of Terms](https://cscmp.org/CSCMP/Educate/SCM_Definitions_and_Glossary_of_Terms.aspx) | Page sans édition ; Definition of Supply Chain Management ; Boundaries and Relationships | Définit la discipline professionnelle, pas un catalogue logiciel ni la frontière exacte de FLOW. |
| [Microsoft — Welcome to Dynamics 365 Supply Chain Management](https://learn.microsoft.com/en-us/dynamics365/supply-chain/supply-chain-management-welcome) | Mise à jour affichée 10 septembre 2025 ; Core concepts and tasks | Le sommaire documente les familles fonctionnelles de la suite ; il ne prouve ni leur détail ni une couverture installée. |
| [Oracle — Overview of Supply Chain Orchestration](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauco/overview-of-supply-orchestration.html) | Fusion Cloud 26B ; introduction, Manage Supply for Back-to-Back Flows et Automate Change Management, exemple 100/75 | Usage logiciel du nom et exemple explicite ; le module interagit avec d’autres produits, sans équivalence de catalogue avec FLOW. |

Le rapprochement avec la recherche et SCOR complète ici la discussion. Aucun consensus entre ces sources, aucune conformité au standard et aucune réalisation installée ne sont déduits de leur proximité. Aucun changement de responsabilité n’est proposé.

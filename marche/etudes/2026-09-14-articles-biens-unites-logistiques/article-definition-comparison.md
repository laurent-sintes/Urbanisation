# Article : définition lexicale et définition SAP

14 septembre 2026 — U181. Correction et précision de l’audit U176 et de la réponse U180.

Le dictionnaire décrit un objet particulier, membre d’une catégorie, ou une chose proposée à la vente. Il ne spécifie ni maille de commande ni indivisibilité.

SAP définit explicitement Article comme la plus petite unité ou le conditionnement client commandable indépendamment et non subdivisible. Cette définition rejoint l’intuition exprimée par Laurent en U176. Elle figure dans le glossaire historique et dans le cours Public Edition consulté : il ne faut pas la disqualifier comme simplement ancienne.

Le même cours qualifie pourtant le Generic Article d’abstrait et non opérationnel, et décrit des ensembles composés dont les composants sont vendus individuellement. La définition courte ne suffit donc pas à caractériser tout le modèle Article. Présenter une référence de gestion comme LA définition SAP serait également incomplet.

L’indivisibilité commerciale dépendante du contexte est une interprétation possible de notre part ; elle n’est pas explicitement formalisée ainsi dans ces sources. Conserver la tension documentaire plutôt que fabriquer une équivalence universelle. Le constat ne rend pas SKU universellement synonyme d’Article et ne valide aucun nouveau terme du modèle local.

L’audit initial a correctement repéré les catégories et différences de grain, mais aurait dû citer cette définition officielle avant de proposer sa synthèse. Voir C89 et les [constats structurés](article-definition-comparison.json).

## Sources

- [Collins — Article](https://www.collinsdictionary.com/dictionary/english/article) — Extrait indexé consulté, 14 septembre 2026.
- [SAP Library — article (IS-R-KUNDE)](https://help.sap.com/saphelp_snc70/helpdata/EN/35/2a8d69d3895cd5e10000009b38f974/content.htm) — Texte ouvert et consulté ; glossaire historique, 14 septembre 2026.
- [SAP Learning — Creating Products for Retail (3I1)](https://learning.sap.com/courses/exploring-sap-s-4hana-cloud-public-edition-retail/creating-products-for-retail-3i1-) — Texte ouvert et consulté ; cours Public Edition, version non précisée, 14 septembre 2026.

## Qui commande ? — U182

La définition ne précise pas les acteurs. Le complément du glossaire (articles généralement commandés pour un site puis vendus) suggère une lecture approvisionnement du commerçant ; c’est une inférence contextuelle, pas une restriction formelle aux fournisseurs. Le cours 3I1 distingue explicitement Order Unit (achat, données fournisseur/article), Sales Unit (vente) et Delivery/Issue Unit (livraison, notamment wholesale). On ne peut donc pas déduire une unité identique pour tous les échanges du seul mot commandé. Exemple local illustratif : une référence de chemise achetée par cartons de douze et vendue à la pièce. Les sources SAPDEF01/SAPDEF02 ont été relues le 14 septembre 2026.

## Booster vendu et display acheté — U183

Dans le scénario donné, le booster est l’article vendu à l’unité et le display l’unité achetée. La restriction de vente du display est une hypothèse de travail, sans vérification du contrat évoqué.

Un ensemble de composants peut être représenté comme article structuré avec référence d’achat propre. Pour un simple multiple de la même référence de booster, une unité d’achat alternative est également à examiner. Le nom commercial display ne suffit pas à choisir la catégorie SAP Display. Le droit de réaliser une vente est à distinguer de la nature et de la représentation de la référence. Aucun nombre de boosters ni achat possible à l’unité auprès du fournisseur n’est présumé.

Appuis : [Structured Articles](https://learning.sap.com/courses/configuring-master-data-in-sap-s-4hana-cloud-private-edition-retail/structured-articles-1), et cours 3I1 déjà référencé, relus le 14 septembre 2026. Les correspondances sont proposées, pas une configuration constatée.

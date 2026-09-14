# Sources de l’étude d’exploration d’Atlas

Consultation : **14 septembre 2026**. Demande : [U143](../../../connaissance/01-contributions-utilisateur.md#u143). Résultat : [étude et recommandations](etude.md).

Les identifiants UX ci-dessous sont propres à cette étude d’interface. Ils ne constituent ni des modèles de capacités, ni des correspondances MKT/ELM/CMP avec le métier Beaumanoir. Les pages sont des sources primaires des éditeurs ou mainteneurs ; leurs descriptions fonctionnelles ne constituent pas des mesures indépendantes de qualité, de facilité ou de performance.

Les documentations web sont évolutives. Sauf précision, leur numéro de version exact n’est pas fixé dans la page consultée. Aucune version de bibliothèque n’a été installée ou testée. L’implémentation éventuelle devra choisir des versions précises et leur documentation correspondante.

## UX01 — LikeC4

- **Organisme et nature :** projet LikeC4, outil ouvert de modèle textuel, vues et restitution ; licence MIT indiquée dans le dépôt.
- **État examiné :** documentation courante ; la navigation affichait « Latest 1.59.3 ». Cela n’établit pas la version exacte de la démonstration exécutée.
- **Contenus lus :** [présentation et dépôt](https://github.com/likec4/likec4), [modèle et identifiants](https://likec4.dev/dsl/model/), [vues](https://likec4.dev/dsl/views/), [prédicats et agrégation](https://likec4.dev/dsl/views/predicates/), [vues dynamiques](https://likec4.dev/dsl/views/dynamic/), [intégration React](https://likec4.dev/tooling/code-generation/react/), [Web Components](https://likec4.dev/tooling/code-generation/webcomponent/), [outillage IA](https://likec4.dev/tooling/ai-tools/), [CLI](https://likec4.dev/tooling/cli/).
- **Observation directe :** dans le [Playground](https://playground.likec4.dev/), passage de la vue initiale à la [vue interne SaaS](https://playground.likec4.dev/w/tutorial/saas/). Actions distinctes de navigation, relations et détails ; groupes internes et contexte externe observés sur l’écran. Ce parcours ne valide ni l’intégration Atlas ni l’accessibilité complète.
- **Apport et limite :** inspiration de navigation et candidat de restitution. Adapter explicitement les identifiants et vérifier les relations visuelles regroupées ; aucun remplacement implicite de notre JSON par le DSL.

## UX02 — IcePanel

- **Organisme et nature :** IcePanel, application de modélisation et collaboration hébergée.
- **État examiné :** documentation courante du produit ; version SaaS non numérotée dans les pages lues.
- **Contenus lus :** [diagrammes](https://docs.icepanel.io/core-features/diagramming), [Model Viewer](https://docs.icepanel.io/core-features/model-viewer), [recherche](https://docs.icepanel.io/core-features/global-search), [perspectives](https://docs.icepanel.io/visual-storytelling/perspective-tags), [flows](https://docs.icepanel.io/visual-storytelling/flows), [sémantique des flows](https://developer.icepanel.io/core-concepts/flows), [partage](https://docs.icepanel.io/collaboration/sharing), [exports](https://docs.icepanel.io/core-features/export), [API](https://developer.icepanel.io/), [MCP](https://docs.icepanel.io/integrations/mcp-server), [offres](https://icepanel.io/pricing).
- **Démonstration repérée :** [paysage public IcePanel](https://s.icepanel.io/poAqz4n9S6fOW3/c2sv), identifié depuis le site ; aucun parcours complet exécuté dans ce produit pendant l’étude.
- **Apport et limite :** cohérence des vues, filtres et récits. API/MCP et exports ne signifient pas disponibilité du code de l’interface. Fonctions et droits liés à l’offre ; aucun abonnement ou tarif retenu comme hypothèse d’architecture.

## UX03 — React Flow

- **Organisme et nature :** xyflow, bibliothèque React ouverte de diagrammes interactifs ; cœur MIT, offre Pro distincte.
- **État examiné :** documentation courante de la génération v12, sans version patch retenue. Article IA daté du **25 mars 2026**.
- **Contenus lus :** [nœuds personnalisés](https://reactflow.dev/learn/customization/custom-nodes), [API](https://reactflow.dev/api-reference), [placement](https://reactflow.dev/learn/layouting/layouting), [accessibilité](https://reactflow.dev/learn/advanced-use/accessibility), [tests](https://reactflow.dev/learn/advanced-use/testing), [performance](https://reactflow.dev/learn/advanced-use/performance), [Pro](https://reactflow.dev/pro), [formats de documentation IA](https://reactflow.dev/llms.txt), [position officielle sur l’aide au développement IA](https://xyflow.com/blog/llms-txt-agent-skills-ai-development).
- **Apport et limite :** composition de cartes riches et interactions intégrées à l’application. Le placement et le sens des relations restent à construire. Les exemples documentés n’ont pas été exécutés comme tests Atlas.

## UX04 — Cytoscape.js

- **Organisme et nature :** mainteneurs Cytoscape.js, bibliothèque JavaScript ouverte de visualisation et analyse de graphes, licence MIT.
- **État examiné :** documentation courante ; note **3.31.0 du 13 janvier 2025** lue pour l’introduction des types. Cette note ne désigne pas la dernière version du moteur.
- **Contenus lus :** [documentation et API](https://js.cytoscape.org/), [performance](https://js.cytoscape.org/#performance), [dépôt](https://github.com/cytoscape/cytoscape.js), [note sur les types](https://blog.js.cytoscape.org/2025/01/13/3.31.0-release/), [instructions de contribution](https://github.com/cytoscape/cytoscape.js/blob/unstable/AGENTS.md).
- **Apport et limite :** voisinages, parcours, calculs et rendu de réseaux. Les instructions de contribution ne sont pas un assistant IA intégré à Atlas. Aucun avantage de volume ou niveau d’accessibilité comparé n’a été mesuré.

## UX05 — Kumu

- **Organisme et nature :** Kumu, application de cartographie de systèmes et réseaux.
- **État examiné :** documentation courante, version produit non indiquée.
- **Contenus lus :** [focalisation](https://docs.kumu.io/guides/focus), [éditeurs de vues](https://docs.kumu.io/overview/user-interfaces/view-editors), [import](https://docs.kumu.io/guides/import), [présentations](https://docs.kumu.io/guides/presentations), [export](https://docs.kumu.io/guides/export). [Galerie publique](https://kumu.io/kumu/projects-in-the-wild#projects-in-the-wild) consultée comme référence de présentation.
- **Apport et limite :** profondeur/direction du voisinage, perspectives et focalisation progressive. Les exports JSON ne couvrent pas les présentations selon la documentation ; importer/exporter des données ne garantit pas la portabilité de toute l’expérience.

## UX06 — Obsidian

- **Organisme et nature :** Obsidian, application de notes avec graphe de liens.
- **État examiné :** aide courante, version de l’application non fixée.
- **Contenu lu :** [Graph view, dont graphe local et profondeur](https://obsidian.md/help/plugins/graph).
- **Apport et limite :** graphe local accompagnant l’élément lu. Les liens entre notes ne constituent pas un vocabulaire de relations métier ni une hiérarchie d’urbanisme.

## UX07 — Structurizr

- **Organisme et nature :** Structurizr, outillage de modèle d’architecture et vues, orienté C4.
- **État examiné :** documentation courante ; pas de version d’exécution retenue.
- **Contenus lus :** [navigation des diagrammes](https://docs.structurizr.com/ui/diagrams/navigation), [outils IA](https://docs.structurizr.com/ai), [MCP](https://docs.structurizr.com/ai/mcp). [Playground](https://playground.structurizr.com/) repéré.
- **Apport et limite :** discipline d’un modèle textuel et de vues vérifiables. Les conventions C4 ne sont pas reprises comme structure métier. Pas de benchmark comparatif indépendant dans cette étude.

## UX08 — D2

- **Organisme et nature :** Terrastruct / projet D2, langage et outillage de diagrammes textuels.
- **État examiné :** documentation courante, aucune version installée.
- **Contenus lus :** [composition](https://d2lang.com/tour/composition/), [FAQ](https://d2lang.com/tour/faq/). [Playground](https://play.d2lang.com/) repéré.
- **Apport et limite :** composition de schémas et exports narratifs. Ne remplace pas à lui seul l’état partagé arbre/fiche/graphe que nous proposons pour Atlas.

## UX09–UX11 — Moteurs de placement complémentaires

| ID | Projet et nature | Pages examinées | Usage envisagé et limite |
| --- | --- | --- | --- |
| UX09 | ELK.js, calcul de placement issu d’Eclipse Layout Kernel | [Dépôt et options](https://github.com/kieler/elkjs), [licence EPL-2.0](https://github.com/kieler/elkjs/blob/master/LICENSE.md), [adaptateur Cytoscape](https://github.com/cytoscape/cytoscape.js-elk) | Groupes, ports et placement de graphes ; calcule une disposition, pas l’expérience complète. Distinguer sa licence de celle de l’adaptateur. |
| UX10 | Dagre, placement de graphes dirigés | [Dépôt maintenu](https://github.com/dagrejs/dagre), [comparaison de placement React Flow](https://reactflow.dev/learn/layouting/layouting) | Option simple à éprouver pour une structure peu complexe ; ne présumer ni routage optimal ni couverture de tous les groupes. |
| UX11 | fCoSE, extension de placement Cytoscape de l’équipe iVis à Bilkent | [Dépôt et contraintes](https://github.com/iVis-at-Bilkent/cytoscape.js-fcose) | Placement de graphes composés, contraintes de position et alignement ; choix à mesurer si une vue réseau Cytoscape est retenue. |

Versions précises non retenues pour ces trois bibliothèques. Aucune n’a été installée et aucun test de performance n’a été exécuté.

## Éléments locaux effectivement examinés

- [Consignes courantes](../../../AGENTS.md), [corrections](../../../connaissance/04-corrections.md), [audit ergonomique U132/U133/U135](../../../audits/2026-09-13-ergonomie-atlas.md).
- [Index de release](../../../modeles/release/index.json), [descripteur v003](../../../modeles/release/urbanisation-v003-2026-09-13-173533.json), [modèle publié](../../../modeles/release/2026-09-13.5/model.json), [contrat de données d’Atlas](../../../app/model.js), [dépendances déclarées](../../../app/package.json).
- [Méthode de qualification des références](../../methode.md). Les concepts d’interface sont comparés comme tels, sans mapping automatique vers le référentiel métier.
- [Empreintes des fichiers applicatifs et modèles examinés](etat-examine.json). Elles décrivent l’état local de départ ; les pages Internet ne sont pas des captures archivées et pourront évoluer.

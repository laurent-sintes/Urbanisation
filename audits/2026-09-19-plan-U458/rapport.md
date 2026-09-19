# Exécution du plan Atlas — U458

19 septembre 2026. Premier jalon : socle et consultation mis en œuvre, cinq pilotes préparés. Les lots d’enrichissement généralisé et de recette métier restent à conduire ; ce bilan ne déclare pas la V0 entière terminée.

## Modifications appliquées

**Socle sans couches métier.** Les 142 nœuds du backlog ne portent plus `layer`. Le schéma, la validation et le lecteur acceptent ce modèle courant tout en préservant les contrats historiques. Le principe U455 interdit de réintroduire le champ dans le modèle courant. Six périmètres, deux formulations de comparaison interne et trois notes de relations ont été alignés sans changer les responsabilités. Identifiants, noms, parents et liens métier sont conservés. Les révisions retracent la migration ; les qualifications d’accord existantes restent intactes.

**Contenu de lecture métier.** Fiches, relations et recherche utilisent une liste explicite de champs métier. Les comparaisons produits ne sont plus affichées dans les fiches ni les glossaires. Le simulateur de réalisations logicielles a été retiré du guide. Les annotations internes restent dans les données d’origine, sans être utilisées comme critères de recherche. Cette séparation d’affichage n’est pas un dispositif de confidentialité : l’API locale reste un lecteur du snapshot complet.

**Recherche.** Nom exact et identifiant sont prioritaires. Une expression présente au début d’une définition passe avant des mots dispersés dans le texte. Le glossaire fournit des résultats distincts, avec extraits et liens de même version. Le filtre des termes fonctionne aussi sans saisir de texte ; les catégories ne sont plus confondues avec le type du premier comportement rencontré.

**Fiches.** Finalité, définition, rattachement et périmètre passent avant les responsabilités liées et les comportements. Les textes longs, conditions des relations et descriptions de comportements restent accessibles dans des détails dépliables. Les raccourcis déplacent aussi le focus clavier. Aucun résumé métier automatique n’a été inventé à partir des premiers mots : un paragraphe de périmètre affiché seul est indiqué comme extrait.

**Relations.** Les liens parcourus depuis l’élément choisi sont montrés par défaut. L’ajout des liens entre voisins est explicite et conservé dans l’URL. Les relations des comportements restent regroupées avec leur capacité, sans réécrire leurs origines. Les noms métier remplacent les identifiants seuls au dézoom ; la liste accessible et l’inspecteur restent disponibles. Le point d’entrée général présente les domaines et référentiels.

**Présentation.** Recherche remontée, aides secondaires regroupées en bas de l’arbre, textes secondaires assombris, tailles de lecture augmentées, surfaces neutres et accents limités. Les icônes des références et des types, l’ordre des décisions et leurs séparateurs restent en place. Le petit écran conserve l’accès au périmètre complet et aux glossaires.

## Résultats observés

Comparaison sur Purchase Order, publication v010, écran 1440 × 900. La hauteur d’une fiche dépend de l’ouverture de ses détails ; les mesures après portent sur l’état initial replié.

| Indicateur | Audit U453 | Après U458 |
| --- | --- | --- |
| Hauteur de la fiche | 4 928 px | 1 571 px |
| Position du périmètre | 1 302 px | 747 px |
| Position du rattachement | 4 764 px | 704 px |
| Premier résultat « Purchase Order » | Sales Order | Purchase Order |
| Résultats « Purchase Order » | 24 | 16, avec le glossaire et un index métier différent |
| Graphe autour de Purchase Order | 47 relations | 18 par défaut, 47 avec les liens entre voisins |

Les 18 relations incluent celles des comportements regroupés avec Purchase Order ; la fiche de capacité présente ses 14 liens directs propres. La différence est explicitée dans le graphe. Aucun lien publié n’est supprimé.

« Commande d’achat » conduit au terme Purchase Order, puis à sa capacité. « Bon de commande » est absent du vocabulaire de v010 : aucun résultat n’est inventé dans cette publication. Le terme proposé TER086, **Purchase Order Document**, explicite ce renvoi dans le backlog et distingue document, objet et capacité. Son parcours a été vérifié dans une fixture de future publication ; sa disponibilité réelle attend une release.

Captures : [fiche](purchase-sheet.png), [recherche française](french-search.png), [relations](direct-relations.png), [fiche mobile](mobile-sheet.png), [glossaire mobile](mobile-glossary.png). Mesures et parcours : [preuve navigateur](browser-verification.json).

## Contenus préparés pour la suite

Le [brouillon du guide](../../modeles/backlog/modeling-guide-U458.yaml) conserve six repères et remplace l’exploration de solutions par la coopération Commerce–Supply–logistique, sans créer ces trois domaines. Il retire aussi la condition de même couche pour les comportements. Le guide publié 2026-09-19.1 reste associé à v010 et garde ses formulations historiques jusqu’à une publication explicite de cette révision.

Les [cinq pilotes](pilotes.md), générés depuis [leur annexe YAML](../../modeles/backlog/information-pilots-U458.yaml), couvrent Purchase Order, Product Reference avec Product Reference Ingestion, Fulfillment Commitment, Supply Assignment et Reservation. Chaque cas distingue résultat, responsabilités, limites, informations candidates et exemple fictif. Le scénario commun comprend refus, retard et réalisation partielle.

Le [suivi V0](../../modeles/backlog/v0-readiness.yaml) reste l’unique registre des travaux et questions. Ses anciens comptages sont contextualisés ; ils ne sont pas présentés comme l’état actuel. Les questions techniques de persistance et concurrence sont hors Atlas, tandis que les effets métier restent à décrire.

## Arbitrages et dépendances

**Question soumise — V0-P01.** Pour une réception constatée de 60 pièces sur 100, conserver la convention U61 selon laquelle le fait de gestion est associé à un document identifié, éventuellement structuré sans fichier, ou permettre des faits sans document ? Recommandation : préserver la convention initiale. Aucune réponse n’est présumée ; ni cardinalité ni mécanisme de correction n’en sont déduits.

**À instruire ensuite.** L’autorité métier effective et les conditions d’alimentation de Product Reference ; l’identité et les versions des attendus et engagements ; les responsabilités qui autorisent leurs révisions. Les pilotes ne désignent aucun maître installé et n’ajoutent aucune réservation automatique. Ces précisions conditionnent l’extension utile du contrat d’information, pas les améliorations de lecture déjà réalisées.

Les sources comparatives restent internes. Le [tutoriel ArchiMate 101 de la communauté The Open Group](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/) distingue les informations conceptuelles des structures applicatives ; il ne tranche pas la convention FLOW fait/document. C’est un tutoriel non normatif, antérieur à ArchiMate 4. Le chapitre 4 consulté a redirigé vers l’authentification : aucune affirmation nouvelle n’en est tirée.

La [documentation Microsoft sur les approvisionnements](https://learn.microsoft.com/fr-fr/dynamics365/supply-chain/procurement/procurement-sourcing-overview) distingue demande, confirmation, échéances et constats de réception et emploie « bon de commande ». Elle soutient le vocabulaire et les exemples, sans imposer à FLOW la structure du produit. Les rapprochements disciplinaires antérieurs CMP171, CMP173 et CMP174 sont conservés.

## Vérifications et préservation

- Validation globale du modèle : zéro erreur ; restitution backlog régénérée.
- 68 tests frontend réussis ; compilation TypeScript/Vite réussie.
- 33 tests Python ciblés réussis : retrait des couches, comportements, révisions et préparation de publication.
- Navigateur Edge sans fenêtre : recherche, focus, fiche complète, glossaire, version fixe, options du graphe et retour navigateur ; aucun défaut JavaScript observé. Contrôles de débordement à 390 px et de repli à 720 × 450. Ces dimensions éprouvent le repli ; elles ne remplacent pas une recette humaine à un zoom navigateur de 200 %.
- Contrat du nouveau guide et références des cinq pilotes contrôlés.
- 291 fichiers protégés identiques : publications, index, révisions, preuves et guides versionnés. Les 142 nœuds, 346 identités et extrémités de relations du backlog sont conservés ; les cycles de validation des nœuds sont inchangés. [Preuve d’intégrité](invariants-verification.json).

L’interface compilée est disponible sur le serveur local après rechargement. La publication active reste **v010 / 2026-09-19.3**. Le vocabulaire ajouté, le modèle sans `layer` et le nouveau guide attendent leur publication. Aucune release, aucun commit ni push n’ont été effectués dans ce lot ; les changements déjà présents avant U458 sont préservés.

La généralisation des fiches d’information et la recette auprès de lecteurs réels restent à faire. Les améliorations mesurées de l’outil ne valent pas validation métier globale ni certification d’accessibilité.

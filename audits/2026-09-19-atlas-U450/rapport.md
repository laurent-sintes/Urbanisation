# Atlas — corrections de présentation U450 et formes de comportements U451

19 septembre 2026. Bilan de l’intervention U450/U451, réalisée sur v009. **Suivi U452 : v010 / 2026-09-19.3 est désormais publiée**, avec les types préparés ci-dessous et le méta modèle associé. [Rapport de publication](../2026-09-19-release-U452/rapport.md). Interface disponible sur le serveur local FLOW Atlas, port 8765.

## Modifications livrées dans Atlas

- Réserves, badges et filtres de validation, provenance interne et liens vers les sources du backlog retirés des fiches, cartes, arbre, glossaires et détails de relations. La mention « Publier ne vaut pas valider » est supprimée. Les conditions et effets métier des relations restent consultables, ainsi que les références externes de marché.
- Les annotations éditoriales connues insérées dans les périmètres et contextes ne sont plus présentées. Le filtre cible les références de contributions et les phrases éditoriales ; il préserve les réservations métier, le stock en réserve, les dates proposées et la validation d’un scénario. Les textes sources ne sont pas modifiés.
- Deux entrées : **Glossaire métier**, 100 termes ; **Glossaire du méta modèle**, 21 termes (11 MOD et 10 TER méthodologiques). Les anciens liens TER gardent leur identité et s’ouvrent dans le bon glossaire. Les textes et identités des 110 TER du snapshot restent inchangés.
- Liste et définition ont chacune leur panneau de défilement, borné et indépendant. La définition revient immédiatement en haut au changement de terme. Recherche, sélection initiale et affichage mobile vérifiés.
- **Comprendre le méta modèle** remplace l’ancien bouton. L’édition figée `2026-09-19.1` rétablit les six repères, actualise les exemples et contient le lexique méthodologique. Son association explicite à v009 est publiée ; l’ancienne édition et l’association à v007 sont conservées.
- Capacités des référentiels : six pictogrammes métier spécifiques, déterminés par les parents explicites. Les autres capacités conservent les icônes par nature, les décisions en fin de domaine et la séparation légère.
- Les sept formes de comportements disposent de sept pictogrammes. Une publication ancienne sans ce champ reste neutre, sans déduction depuis le nom ou le backlog.

Les données et preuves internes demeurent conservées dans les fichiers. Cette demande porte sur la présentation ; elle ne constitue pas une suppression des métadonnées dans les contrats API locaux.

## Typage du backlog

Les **76 comportements** portent désormais une forme principale proposée dans `fields.nature`. U451 adopte la grille ; aucun accord individuel sur ces classements n’est déduit de cette réponse. Les formes peuvent se combiner ; l’icône représente la forme principale.

| Forme | Nombre |
| --- | ---: |
| Politique / stratégie | 11 |
| Variante de parcours | 22 |
| Mécanisme | 13 |
| Périmètre métier | 7 |
| Dimension de raisonnement | 7 |
| Effet métier | 13 |
| Pratique de planification | 3 |

Justifications par comportement : [behavior-types-U451.yaml](../../modeles/backlog/behavior-types-U451.yaml). MOD006 définit le comportement ; MOD011 explique le typage. Aucun nouveau comportement, changement de parent ou réouverture de l’audit clos U431.

La comparaison méthodologique est consignée dans CMP170 : définition de Capability Behavior du [BIZBOK v15](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_glossary.pdf), exemples de politiques dans le [cycle counting Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting). Ces sources étayent la notion et des exemples ; les sept formes restent une convention FLOW, sans consensus de marché revendiqué.

## Correction du circuit de publication

Le guide manquait parce que l’index ne liait que v007 à une édition méthodologique. La préparation d’une future release capture désormais l’association explicite de sa version de départ et son empreinte. La publication contrôle cette capture et crée l’association de destination avant l’activation du pointeur métier. Une modification intermédiaire impose une nouvelle préparation. Aucune sélection automatique du guide le plus récent et aucun repli vers le backlog.

La comparaison du candidat métier `2026-09-19.3` porte sur **86 éléments existants** : 76 formes de comportements U451 et les 10 types de capacités complétés en U449. Aucun ajout ou retrait de nœud, aucun changement de relation, de nom ou de définition.

Le premier contrôle de publication suspendait la reprise des accords pour les révisions modifiées. Le réexamen compare chaque valeur approuvée à la décision déjà publiée en v009 : **73 transcriptions, 118 champs identiques**. Les nouveaux types demeurent proposés. Le [rapport du candidat](publication-review.json) ne signale aucune erreur avec ces transcriptions ; [preuves champ par champ](transcription-review.json). Ces fichiers de revue ne publient ni ne valident les nouveaux types.

À la clôture de U450/U451, la nouvelle release métier attendait le choix de Laurent. **U452 l’a ensuite autorisée ; v010 est publiée et les 76 formes ainsi que les dix types supplémentaires sont visibles dans Atlas.** Aucun commit ni push.

## Vérifications

- 63 tests frontend réussis, dont les deux tests du nettoyage éditorial exécutés après sa correction.
- Tests Python du modèle, des types, de la préparation et du guide réussis. Tests supplémentaires du report d’association et du refus d’un index modifié réussis. Un test de lien symbolique est ignoré sur Windows.
- `validate_models.py` : **0 erreur** ; restitution backlog régénérée ; TypeScript et build Vite réussis.
- Contrôles navigateur : six repères, glossaires séparés, liens historiques, défilement, recherche, mobile 390 px, absence des métadonnées internes, six icônes de référentiels ; les sept icônes de comportements sont vérifiées avec une fixture de publication isolée. Aucune erreur JavaScript. [Résultat](browser/verification.json).
- **231 fichiers protégés identiques octet par octet** : publications, révisions, décisions, preuves historiques et ancienne édition du guide. Relations et anciens champs du backlog préservés. L’API sert exactement le snapshot v009. [Vérification d’intégrité](verification.json).

Captures : [glossaire du méta modèle](browser/meta-glossary.png), [méta modèle](browser/meta-model.png), [mobile](browser/mobile-glossary.png). Les anciens scripts de vérification UI comportant des attentes sur les sources et validations reflètent les parcours antérieurs ; le contrôle concerné par U450 est `app/verify-atlas-presentation.mjs`.

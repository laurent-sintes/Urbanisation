# Typage des capacités et présentation Atlas — U449

Les 47 capacités du backlog portent désormais un type explicite dans le champ existant `fields.nature`. Les 37 valeurs déjà présentes sont conservées. Dix absences sont complétées comme propositions, dans la portée U435 ; aucun nom, définition, rattachement ou accord antérieur n’est remplacé.

| Type | Nombre | Icône Atlas |
| --- | ---: | --- |
| Action | 17 | Éclair |
| Decision | 16 | Bifurcation |
| Management | 7 | Réglages |
| Knowledge | 4 | Œil |
| Planning | 2 | Calendrier |
| Orchestration | 1 | Enchaînement |

La [grille méthodologique](../../modeles/backlog/capability-types-U449.yaml), rattachée à MOD007, définit les frontières et la portée de chaque type. Les classifications complétées concernent Inventory Tracking et Inventory Visibility (knowledge), Record Inventory Movements, Stocktaking, Reservation et cinq capacités d’ingestion (action). Les justifications individuelles sont dans [changes.yaml](changes.yaml). Reservation matérialise l’engagement ; Reservation Policy Decision conserve le choix de la politique.

## Présentation

Les décisions suivent systématiquement les autres capacités de chaque domaine ou référentiel. L’ordre relatif des éléments est conservé dans chaque partie. Le backlog porte ce même ordre par permutation des relations, sans modification de leur contenu. L’interface applique la partition à la publication sélectionnée, sans altérer le snapshot.

Un trait horizontal léger sépare les deux parties dans l’arbre, les listes des cartes, les fiches de domaine et les cartes détaillées. Il n’apparaît que si les deux parties existent. Les décisions commencent une nouvelle rangée dans la carte détaillée. Aucun nœud métier ni niveau de hiérarchie n’est ajouté. Les comportements gardent leur ordre.

Les icônes sont déterminées uniquement par le type publié ; le nom et le préfixe d’identifiant n’interviennent pas. Le libellé du type est lisible sur les fiches, cartes et descriptions accessibles. Une nature absente dans une publication historique reste non renseignée, avec une icône générique distincte des six types.

## Appui et limites

[OMG DMN](https://www.omg.org/dmn/) distingue la description des décisions de celle des processus et cas qui les mobilisent. Cette complémentarité étaye la distinction FLOW entre décision et orchestration. Les six catégories, leurs frontières fines et les icônes restent une convention FLOW ; DMN ne prescrit pas cette taxonomie. Source primaire consultée le 19 septembre 2026, MKT43/ELM259/CMP169. Aucun accord global sur les qualifications individuelles ni preuve de réalisation installée n’en découle.

## Vérifications et disponibilité

- 28 tests Python et 58 tests de l’interface réussis ; validation du modèle sans erreur et restitution backlog régénérée.
- Compilation Atlas réussie ; contrôles du rendu, des icônes, du tri, des séparations, du clavier et de l’affichage mobile réussis, sans erreur JavaScript.
- 230 fichiers de publication, révision et preuve vérifiés identiques ; champs et accords antérieurs préservés, contenu des relations inchangé.
- Le contrat de typage obligatoire s’applique aux modèles portant le nouveau principe ; les publications historiques restent compatibles.

La nouvelle interface est compilée et disponible sur le serveur local ; recharger une page Atlas déjà ouverte pour la recevoir. **La release active reste v009 / 2026-09-19.2.** Elle contient déjà 37 types, utilisés immédiatement pour la présentation. Les dix types complétés dans le backlog attendent une prochaine release. Aucun repli sur le backlog, aucune publication, aucun commit ni push effectués dans cette intervention.

[Preuves de vérification](verification.json) ; contrôles visuels reproductibles par `node app/verify-capability-types.mjs`.

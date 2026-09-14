# Publication v004 — U204

Publication `2026-09-14.1`, activée le 14 septembre 2026 à **14:50:44 UTC**. Descripteur `urbanisation-v004-2026-09-14-145044.yaml` ; modèle `modeles/release/2026-09-14.1/model.yaml`. [Note de release](../../modeles/release/2026-09-14.1/release-notes.md).

## Contenu publié

- 48 nœuds, dont 34 capacités, et 47 relations. D01 conserve ses six capacités, D04 ses quatre capacités de gestion des commandes.
- Retrait de D02 et de ses deux capacités résiduelles, sans renuméroter les autres identifiants. D02.b/D02.c restent en D01 et D02.e en D03.
- D03 conserve quatre actions et accueille ATP, CTP, PTP, Delivery Schedule Decision et Order Prioritization. Les cinq décisions détaillées antérieures sont conservées dans les historiques. La réflexion Backlog Management et Scenario Simulation reste dans le contexte, sans renommage ou ajout implicite.
- Business Services remplace le libellé Case sur l’identité conservée `universe-case`. Les domaines processus restent différés.
- L’audit U202 précise les références Product/Variant, les rôles Article/Container, les exemplaires physiques et les Orders contextualisés. Les formulations modifiées restent proposées dans leur portée.
- Premier glossaire publié : 93 termes, chacun en révision 1 avec `last_modified` UTC. Catalogue figé avec le modèle ; API JSON et navigation dans la même publication.

## Validation et preuve

Le premier rapport signalait 47 champs portant un accord dans le cycle d’instruction sans décision correspondante pour cette révision. Aucun de ces accords n’a été effacé pour rendre le contrôle permissif.

La réconciliation a examiné les valeurs et leurs preuves. Six transcriptions reprennent uniquement les champs inchangés de décisions antérieures, vérifiés par empreinte ; les autres champs restent proposés. Huit décisions transcrivent U154 sur D03.i–l et leurs rattachements, avec comparaison à l’alternative conservée dans `history/pre-U154.json`. Deux transcrivent U163 sur le nom/définition d’Order Prioritization et son rattachement contextuel à D03. Une transcrit U173 sur Business Services. Le rattachement d’Order Prioritization et la portée d’ingestion D08.d conservent leur qualification contextuelle.

Les **17 nouveaux identifiants ADOPT-058 à ADOPT-074** enregistrent ces accords existants, sans nouveau Go métier. Le catalogue final comporte **53 décisions** : 36 reprises identiques et 17 transcriptions. Les 18 décisions antérieures non reprises intégralement restent dans leurs publications ; six sont remplacées sur cette révision par une portée plus restreinte. `reconciliation.json` et `additional-decisions.json` détaillent preuves et champs. Les capacités se répartissent en 5 entièrement validées, 16 partiellement validées, 9 proposées et 4 en réexamen.

Un défaut du validateur n’autorisait `accepted` que pour les capacités, alors que le compilateur et le modèle permettent de valider les champs d’un univers. La correction maintient les exigences spécifiques des capacités et permet la validation complète des autres types uniquement avec preuve explicite pour tous leurs champs. Un test positif et un test de rejet d’une validation partielle abusivement présentée comme complète couvrent le cas Business Services.

## Contrôles et historique

- 79 tests Python du modèle réussis ; validation du projet sans erreur après publication.
- API Atlas identifiée : modèle `2026-09-14.1`, révision 4, source YAML, 48 nœuds et 93 termes. Catalogue courant concordant.
- 22 tests Python du lecteur/HTTP : 20 réussis, deux ignorés pour contraintes de plateforme.
- Navigateur : glossaire réel de v004, infobulles, navigation entre Product Unit et Serial Number, et v003 historique sans enrichissement depuis le backlog. Les scénarios synthétiques supplémentaires restent confinés au navigateur de test.
- 47 fichiers historiques de release, révision, décision et provenance contrôlés par empreinte : aucun modifié. Le nouvel index est activé en dernier.
- Le rapport suivant, exécuté en lecture seule, ne trouve aucune nouvelle révision d’élément ni variation du glossaire ; le modèle reste en révision 4 et le contrôle retourne zéro erreur.

Les restitutions Markdown sont régénérées. Le serveur est relancé avec le validateur corrigé. Les panoramas As Is et les objets illustratifs ne sont pas publiés dans cette release. Aucun commit ni push effectué.

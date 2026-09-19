# Publication v006 — U236

Publication `2026-09-16.1`, activée le 16 septembre 2026 à `07:59:52.422804Z` : [descripteur](../../modeles/release/urbanisation-v006-2026-09-16-075952.yaml), [note de release](../../modeles/release/2026-09-16.1/release-notes.md).

## Contenu et portée

53 nœuds, 39 capacités, 60 relations et 99 termes métier. D05 devient Inventory Optimization avec Coverage Target Decision, Stock Allocation Decision, Replenishment Decision, Stock Redistribution Decision et Inventory Planning. Les cinq capacités sont directement rattachées à D05 ; quatre relations de mobilisation partent de Planning. D05.b et son rattachement sont retirés ; le calcul net est intégré à Replenishment Decision, sans transfert d'identité ni de validation.

D01 et D03 portent les finalités clarifiées U219. D05 reprend le nom U220, la définition U223 et la refonte U235. Trois capacités et sept relations sont ajoutées ; une capacité et une relation sont retirées ; cinq nœuds existants et deux rattachements sont modifiés. Les principes restent inchangés. D04 reste identique à v005.

Le nouveau terme TER074 Replenishment reste proposé. Sa formulation antérieure à U224 attribuait encore à l'exploration D05 le déclenchement automatique et laissait la granularité ouverte. La correction éditoriale avant préparation rétablit décision analytique versus mise en action opérationnelle et renvoie à D05.e, conformément à U224/U235. L'état antérieur est dans [before-glossary.yaml](before-glossary.yaml). Les 98 autres termes restent inchangés. L'alerte de sens sur D05.e est examinée : son périmètre distingue déjà calcul net, résultat de décision, Orders et exécution ; le lien vers TER074 est cohérent, sans nouvelle validation de la définition lexicale.

Le glossaire de modélisation reste séparé et figé comme contexte, sans termes MOD dans le glossaire métier publié. Les alternatives, illustrations, analyses marché et autres annexes restent du contexte ; les quatre nœuds et huit relations illustratifs du backlog ne sont pas intégrés dans les compteurs de release. Le panorama As Is n'est pas publié par cette opération.

## Validations

82 décisions : 62 reprises compatibles et 20 transcriptions sourcées dans [new-decisions.json](new-decisions.json). Cinq transcriptions portent les nouvelles portées des domaines : trois finalités U219, le nom D05 U220 et sa définition U223. Quatorze portent U235 : cinq couples nom/définition, cinq rattachements directs et quatre couples d'extrémités de mobilisation. Finalités, natures, périmètres détaillés, exemples et qualification technique des mobilisations restent proposés.

La vingtième transcription concerne uniquement le nom inchangé Order Promising sur la nouvelle révision de D03. ADOPT-058 n'est pas reprise automatiquement : son empreinte et sa portée ont été réexaminées, puis transcrites sous un nouvel identifiant avec date et sources de l'accord d'origine. ADOPT-058 reste dans l'historique. Aucun accord sur la nouvelle définition de D03 n'est inventé.

Le [rapport initial](initial-report.json) conserve les lacunes de décisions avant transcription ; le [rapport publié](../../modeles/release/2026-09-16.1/changes.json) constate zéro erreur après transcription. Les publications ne valent pas validation métier.

## Vérifications

- Préparation et publication par `prepare_release.py`, activation de l'index en dernier.
- `validate_models.py` : zéro erreur, 1134 sources et 82 décisions au moment de la publication.
- `render_models.py` : vues régénérées ; `app/server.py --check` : release v006 et frontend prêt.
- Candidat contrôlé : cinq rattachements directs D05, quatre mobilisations depuis Planning, absence de D05.b, champs approuvés limités à nom/définition pour les cinq capacités et aucun MOD dans le glossaire métier.
- [Contrôle API](atlas-api.json) : identité FLOW Atlas, racine du projet, espace release, version `2026-09-16.1`, chemin publié et catalogue concordants. Tous les nœuds, relations et termes servis sont identiques au fichier publié.
- Les [88 empreintes protégées](protected-before.json) sont inchangées : fichiers historiques de publications/révisions/décisions/provenance, modèle de backlog et glossaire de modélisation. L'index courant et le glossaire métier sont les changements attendus.
- Navigateur : v006 visible, 53 éléments et 39 capacités ; Inventory Optimization affiche cinq enfants dans l'arbre.
- Glossaire : 99 termes ; fiche Replenishment proposée, définition corrigée et lien vers Replenishment Decision dans la même publication.
- Fiche Replenishment Decision : exemples concrets, rattachement direct et portée affichée « Définition, Libellé » adoptés ; Finalité, Nature et Périmètre à valider.
- Fiche Inventory Planning : définition reconfigurer/simuler/valider, rattachement à D05 et onglet « Relations 4 » présents.

Atlas disponible sur [127.0.0.1:8765](http://127.0.0.1:8765/). Aucun redémarrage nécessaire pour cette publication de données. Les anciennes versions restent sélectionnables. Aucun commit ni push.

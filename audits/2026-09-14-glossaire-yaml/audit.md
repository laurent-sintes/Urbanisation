# Audit du modèle face au glossaire — U202

Périmètre : tous les champs courants des 52 nœuds (34 capacités), principes et relations ; compléments de vocabulaire et décisions U154 à U195. Les citations, alternatives et preuves restent historiques.

| Repère | Constat | Traitement |
| --- | --- | --- |
| G01 | Article confondu avec référence SKU et absence des rôles Product dans Product Reference. | Préciser référence, variante, unité et rôles ; garder SKU comme correspondance à instruire. |
| G02 | Demandes et fourniture ambigus face aux Orders Supply et ressources. | Employer commande Supply quand elle est visée ; conserver besoins prévisionnels dans Supply Assignment. |
| G03 | Placement différé CTP contredit D03.j adopté. | Retirer le principe obsolète, conserver sa capture ; ajouter le principe To-Promise courant. |
| G04 | Univers Case obsolète face à Business Services. | Actualiser le vocabulaire du principe sans renommer les identifiants. |
| G05 | Service Order adopté n’apparaît pas dans la capacité qui exprime les prestations attendues. | Préciser le vocabulaire ; aucun nouvel objet de la carte ni cycle imposé. |
| G06 | Première table TER004 encore historique ; compléments récents font autorité sur les rôles. | Ajouter une entrée de lecture courante signalant explicitement les anciens sens ; ne pas réutiliser TER004 pour un autre concept. |
| G07 | Stock physique/logique/futur, ATP, distinction Party/lieu et projections externes compatibles ; détails packing proposés hors carte. | Conserver ; ne pas ajouter de capacité ni étendre un accord. |
| G08 | Cumul de rôles, grain commercial, règles de composition et portée générique de Resource encore ouverts. | Conserver en instruction ; aucune fusion forcée ou attribution de GTIN individuel. |

Les reformulations détaillées ajoutées par Codex restent proposées. Une validation de nom inchangé est conservée dans sa portée ; une ancienne validation de définition ne qualifie pas une nouvelle formulation. Le rapport JSON conserve les valeurs exactes et la capture avant application.


## Réalisation et contrôles

Les dix corrections de nœuds et les principes identifiés sont appliqués au backlog. Les définitions reformulées ne reprennent pas automatiquement la validation de leur ancienne valeur ; les noms inchangés gardent leur portée sourcée dans le backlog. Les 34 capacités sont conservées.

Dix documents courants sont passés en YAML après comparaison de leurs valeurs décodées. Les originaux JSON après audit sont conservés dans `json-before-yaml/` ; la capture `before-model.json` précède l’audit. `yaml-migration.json` trace les empreintes de conversion. Les notes de travail `glossary-text-references.yaml` et `modeling-roadmap.yaml` ont ensuite été actualisées explicitement pour refléter la décision YAML.

Le workflow produit désormais les modèles, captures d’entrée et descripteurs de nouvelles publications en YAML. Métadonnées techniques JSON et preuves historiques restent dans leur format d’origine. Atlas utilise le lecteur commun et renvoie du JSON. La version courante demeure v003 ; aucune release métier n’a été créée dans le projet.

Contrôles : validation du projet sans erreur ; 72 tests Python des modèles/lecteurs, 20 tests HTTP réussis et deux ignorés selon les capacités Windows, 30 tests JavaScript Atlas réussis. Le test HTTP prépare et active une publication YAML dans une copie isolée, vérifie la réponse JSON et la consultation historique JSON, puis vérifie le refus d’un YAML publié altéré. Les tests Windows nécessitant un sous-processus ou un renommage de préparation ont été exécutés hors sandbox après échec de permission. Aucun test ne modifie la release réelle.

Le rapport `publication-readiness.json` distingue la préparation métier du contrôle technique : 36 portées lifecycle ne trouvaient pas encore de décision de publication compatible avant l’audit, 47 après les révisions de cet audit. Leur transcription/réexamen est nécessaire avant une prochaine release ; les contrôles bloquent celle-ci au lieu de supprimer les accords du backlog ou de les étendre. Cette étape ne publie pas le modèle et ne contourne pas ce contrôle.

Dépendance : [PyYAML 6.0.3](https://pypi.org/project/PyYAML/6.0.3/), installée localement et épinglée dans `requirements.txt`. Le lecteur applique un sous-ensemble adapté aux valeurs JSON ; il ne prétend pas accepter tous les usages YAML. Les liens interactifs au glossaire restent hors de cette implémentation.

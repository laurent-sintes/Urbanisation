# Performance des mises à jour du référentiel par le LLM

19 septembre 2026. Périmètre précisé par Laurent : le temps de travail de l’agent sur le référentiel, et non la réactivité d’Atlas. Les premières mesures Atlas ont été écartées ; aucun changement d’interface ni de serveur n’a été effectué.

## Conclusion

Le ralentissement a deux causes distinctes : des commandes qui réanalysent les mêmes fichiers YAML à chaque nouveau processus, et un déroulement de travail trop chargé en lectures, relectures, scripts ponctuels et contrôles répétés. La première cause est mesurable et désormais réduite. La seconde demande une discipline de travail explicite ; accélérer Python ne suffit pas à rendre toutes les réponses du LLM instantanées.

Le cache précédent ne survivait pas à la commande Python. Il accélérait plusieurs lectures dans une commande, mais pas la succession inspection → modification → validation → restitution → préparation. La taille du référentiel a aussi augmenté depuis le premier audit : le modèle courant représente 1,32 Mo et 27 832 lignes ; le dépôt suit 1 972 fichiers pour 178,5 Mo. Ce volume ne doit pas devenir le volume lu par l’agent à chaque retour.

## Mesures avant/après

Commandes réelles exécutées successivement, dans des processus Python séparés, sur les mêmes données métier. Les temps comprennent le démarrage du processus. Avant : une mesure par commande. Après : médiane de trois mesures avec cache persistant alimenté. Ces observations locales ne constituent pas un benchmark statistique ni une mesure de la génération du LLM.

| Opération | Avant | Après, cache alimenté | Réduction |
| --- | ---: | ---: | ---: |
| Lecture ciblée du modèle | 1,522 s | 0,127 s | 92 % |
| Validation complète du projet | 6,031 s | 1,005 s | 83 % |
| Restitution du backlog | 1,787 s | 0,185 s | 90 % |
| Rapport de préparation de release | 10,323 s | 1,742 s | 83 % |

Les commandes `validate_models.py`, `render_models.py --space backlog` et `prepare_release.py report` restent les mêmes. Aucun contrôle de validation n’est sauté.

**Cas d’une modification :** une lecture du backlog avec des octets inédits, injectés uniquement dans le processus de mesure, force bien une nouvelle analyse YAML. La validation prend alors **2,275 s**, contre 6,031 s dans l’état initial : les autres entrées inchangées restent réutilisables. Il s’agit d’une simulation d’invalidation, pas d’une modification métier ni d’une publication. Réécrire entièrement le modèle avec sa vérification aller-retour coûte encore **2,556 s**. Ce coût reste légitime lorsqu’une sérialisation complète est nécessaire.

**Premier passage :** créer les caches ne rend pas la première lecture plus rapide : 1,610 s pour cette lecture, puis 4,625 s pour la validation et 6,359 s pour le rapport, qui bénéficient progressivement des fichiers déjà analysés. Les gains maximums concernent les opérations répétées et les parties inchangées.

Preuves : [état initial](before.json), [premier passage](after-first.json), [synthèse et échantillons](results.json), [invalidation et sérialisation](changed-input.json). Reproduction : `python audits/2026-09-19-reference-update-performance/measure.py NOM_NEUF`. Le script refuse d’écraser un résultat existant, ne publie pas et ne change pas le modèle ; la restitution identique n’est pas réécrite.

## Corrections appliquées

### 1. Réutiliser les analyses YAML entre commandes

`scripts/structured_io.py` utilise désormais un cache technique local dans `.runtime/parsed-models/`, via `scripts/parsed_cache.py`. Sa clé dépend des octets sources, du suffixe, du code du lecteur et du cache, de la version Python et de PyYAML. Les octets du fichier sont relus et hachés à chaque appel : conserver une date et une taille identiques ne peut pas masquer un changement.

Les données sont stockées en JSON, avec empreinte du contenu du cache ; aucun pickle. Une entrée absente, corrompue, inaccessible ou issue d’un autre lecteur provoque une nouvelle analyse des sources. Les écritures sont atomiques et le cache est limité à 128 entrées / 64 Mio. Les objets retournés restent indépendants des objets mis en cache. Les signatures des publications, contrats, références et accords continuent d’être vérifiés par leurs contrôles habituels.

Ce cache est jetable et ignoré par Git. Ce n’est ni un deuxième modèle, ni un résultat de validation, ni une autorité métier. Supprimer ses fichiers ne supprime aucune preuve ; le prochain passage les reconstruit. Le cache de parsing en mémoire reste disponible.

### 2. Donner à l’agent un outil de lecture ciblée

Nouvelle commande en lecture seule :

```powershell
python scripts/inspect_model.py D04.j --fields name definition scope
python scripts/inspect_model.py D04.j --fields name definition --relations
python scripts/inspect_model.py --query "Order" --limit 10
python scripts/inspect_model.py TER084 --collection terms
python scripts/inspect_model.py D04.j --space release --version 2026-09-19.6
```

Elle affiche les champs exacts, la provenance et les qualifications de la fiche, avec les parents et enfants explicitement reliés. La recherche de repérage porte sur noms et identifiants ; elle est paginée. Une demande d’identifiant explicite échoue s’il est absent, et ne complète jamais une release depuis le backlog. `--fields '*'` permet d’examiner tous les champs d’une fiche. Les champs non demandés ne sont pas réputés absents.

L’exemple Purchase Order renvoie **6,1 Ko**, au lieu de charger le modèle entier de 1,32 Mo : environ **216 fois moins de texte** pour ce besoin. Il ne s’agit pas d’une promesse de réponse LLM 216 fois plus rapide. [Sortie mesurée](query-example.json).

### 3. Réduire les causes de reprises inutiles

Les fixtures des tests de publication du guide utilisent maintenant le répertoire isolé commun, avec héritage des droits du workspace. L’ancien `TemporaryDirectory` créait des dossiers inaccessibles sous le jeton Windows restreint : le commit précédent avait dû relancer ces tests avec d’autres droits. Les quatre tests concernés passent désormais sans élévation.

Les règles de travail précisent maintenant : lecture ciblée, éditions groupées, un contrôle de l’état final, détail filtré depuis un rapport existant après troncature, et absence de build/recette UI pour une modification métier seule. Une petite intervention n’exige pas une nouvelle copie intégrale du modèle si Git conserve déjà exactement son état antérieur.

Huit paragraphes de cadrage détaillé sont déplacés **intégralement** vers `CONVENTIONS-MODELE.md`, avec un rappel des limites courantes dans AGENTS. Les instructions par défaut passent de 1 899 à 1 783 mots malgré l’ajout des nouvelles règles de performance. C’est une réduction modeste, pas la principale accélération. La [capture antérieure](AGENTS-before.md) et les textes déplacés préservent les accords.

## Ce qui reste à améliorer dans ma méthode

| Constat | Règle retenue / suite recommandée |
| --- | --- |
| `review_and_prepare.py` de U473 construit deux fois le candidat, puis `prepare()` le reconstruit une troisième fois. Le rapport initial ajoute encore un passage. | Diagnostic initial, corrections, préparation finale, puis lecture des artefacts préparés. Ne pas reconstruire un candidat uniquement pour relire ses résultats. |
| Des sorties de commandes sont tronquées alors que seuls quelques champs ou compteurs sont utiles. | Inspecteur ciblé, résumés et erreurs bornées ; conserver une sortie complète seulement comme artefact nécessaire. |
| Un nouveau script d’opération et plusieurs captures sont souvent produits pour chaque demande. | Réutiliser les outils maintenus ; captures limitées aux données effectivement concernées. Préserver les archives existantes. |
| Les tests complets peuvent être relancés après un travail déjà vérifié. | Réutiliser les résultats quand les entrées et le code n’ont pas changé ; rejouer les seuls contrôles affectés après correction. Une release conserve son contrôle d’intégrité final. |
| Le changement de révision d’une fiche enrichie suspend des accords portant sur des valeurs inchangées. | Prochaine amélioration possible : outil réutilisable de préparation du réexamen et de ses preuves. Ne pas supprimer ce réexamen ni élargir les accords pour gagner du temps. |

Le traitement des 40 décisions lors de U473 était du travail supplémentaire réel. Le prochain outil pourrait automatiser la comparaison des valeurs, les empreintes et le dossier de preuve ; le périmètre de l’accord doit toujours être examiné. Cette automatisation n’est pas implémentée dans cet audit.

Le temps propre au modèle LLM, au contexte de conversation et aux recherches externes n’est pas mesuré ici. Le long historique injecté, les instructions de l’environnement et le modèle utilisé ne sont pas entièrement contrôlés par le dépôt. Aucun changement de modèle IA ni multiplication de sous-agents n’est proposé sans mesure correspondante.

## Vérifications et limites

- 153 tests du modèle exécutés ; un échec transitoire de renommage Windows dans une fixture de préparation, puis réussite de ce cas en reprise ciblée. Les tests modifiés ensuite ont également été rejoués.
- 40 tests du lecteur : 37 réussis, trois ignorés pour la création de liens symboliques Windows. Aucun build frontend nécessaire.
- Tests du nouveau cache : reprise entre processus, mutations isolées, changement à date/taille identiques, nouveau parseur, corruption, sources invalides, cache inaccessible et limites de stockage.
- Tests de l’inspecteur : valeurs et fichiers préservés, relations explicites malgré un libellé additionnel, pagination, identifiants absents et absence de repli entre espaces.
- Validation réelle finale : zéro erreur. **777 fichiers de modèle, publications, provenance, connaissance, marché et restitutions inchangés**, vérifiés par SHA-256.

Aucun changement métier, aucune suppression d’historique, release, commit, push ou intervention sur le serveur. Les optimisations s’appliquent dès les prochaines commandes de mise à jour du référentiel.

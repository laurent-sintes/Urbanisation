# Parcours de release refactoré — U504

## Résultat

Le parcours courant est `python scripts/release.py --source SOURCE --activate`. Il construit une seule fois le candidat lorsque les accords sont prêts, puis prépare, publie, contrôle Atlas, génère la restitution et consigne un compte rendu avec les durées. Sans `--activate`, il prépare seulement. Aucun build, navigateur, commit, push ou redémarrage n’est déclenché.

Les accords explicites peuvent être enregistrés avant la release avec `scripts/record_decision.py`, dans l’annexe YAML `modeles/backlog/decision-intents.yaml`. Les champs sont sélectionnés explicitement ; aucune autorisation n’est déduite d’un lifecycle ou d’une publication. La révision finale est déterminée au moment de préparer. Les valeurs et leur contexte sont capturés et contrôlés. Une ancienne intention déjà publiée ne peut pas réactiver un accord ensuite reporté ou suspendu.

Le changement de révision seul ne suspend plus un accord. Le report automatique exige que les valeurs approuvées et le contexte métier soient identiques : cible, relations incidentes, voisins, ancêtres, principes et termes liés. Les métadonnées et références éditoriales connues peuvent évoluer ; les changements métier et champs inconnus restent à examiner. Les décisions reportées conservent auteur, date de l’accord et sources historiques sous un nouvel identifiant traçable.

Les accords composites disposent de `retain_partial` et d’une liste `approved_fields` explicite. Le réexamen ne peut reprendre que des valeurs historiques strictement inchangées. Les anciens dossiers retain/defer restent compatibles.

Un guide peut être préparé avec `--guide CHEMIN_YAML` : contrat, sources, version, octets et association sont contrôlés ensemble avant activation. Les éditions existantes restent figées. Aucune rédaction pédagogique n’est produite automatiquement.

## Reprise et contrôles

- Une préparation figée est reprise sans nouveau calcul ; une modification des données, contrats, sources, code ou du guide bloque sa publication.
- Une version déjà active peut être vérifiée à nouveau sans publication ni doublon de journal. De nouvelles entrées ne sont pas silencieusement ignorées.
- `published_checks_failed` distingue la publication réalisée d’une indisponibilité d’Atlas ou d’un contrôle final échoué.
- `publication_incomplete` signale les artefacts d’une écriture interrompue avant activation. Ils restent intacts et exigent un diagnostic ciblé ; le parcours ne prétend pas savoir réparer automatiquement une publication partiellement écrite.
- Le contrôle Atlas vérifie identité du serveur, dépôt, version, chemin, nœuds, relations, glossaire et guide. Il fonctionne aussi lorsque le script est lancé depuis un autre répertoire.

## Mesure

[Mesure enregistrée](benchmark.json) sur deux copies isolées du modèle v017, avec la même précision de note éditoriale sur Purchase Order :

| Parcours | Préparation totale mesurée | Calculs de candidat | Accords à réexaminer |
| --- | ---: | ---: | ---: |
| Règle précédente, diagnostic puis préparation | 37,40 s | 2 | 1 |
| Parcours regroupé, report contrôlé | 22,80 s | 1 | 0 |

Gain observé : **39 %** sur ce scénario. Les valeurs métier et les champs approuvés des candidats sont identiques. La différence d’identifiant de transcription reste traçable.

Il s’agit d’un seul échantillon séquentiel avec cache de lecture partagé, sans publication ni temps de réexamen humain : ce n’est pas un benchmark statistique ni une estimation de la durée de toutes les releases. L’économie principale de travail agent vient aussi de la suppression des transcriptions tardives, scripts de portée partielle et comptes rendus manuels redondants.

## Vérifications

**101 tests distincts réussis** sur les contrats de publication, décisions, contexte, réexamen partiel, intentions, versions, lifecycle, guide et parcours regroupé. Les échecs initiaux de reprise des comptes rendus ont été corrigés puis la suite concernée rejouée. Le test d’une modification purement metadata du lifecycle suit désormais la règle U504, en vérifiant la préservation de portée et de sources ; les changements métier restent refusés sans réexamen.

Validation du projet : **zéro erreur**. API Atlas vérifiée depuis un répertoire externe : v017 / `2026-09-19.10`. Les [772 fichiers historiques contrôlés](frozen-sha256.json) sont inchangés. Les modifications U503/U504 sont enregistrées et l’index courant des sources est actualisé.

Instructions, documentation et skill release mis à jour ; copie personnelle du skill synchronisée après vérification de l’absence de modification indépendante. Aucun registre d’accord réel créé, aucune nouvelle release, aucun commit ni push.

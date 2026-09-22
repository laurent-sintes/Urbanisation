# Optimisation de la release — 22 septembre 2026

## Périmètre livré

Étapes 1 et 2 : copies exactes vérifiées et cache adapté. Le format des accords et les publications historiques restent inchangés. La mutualisation des contextes des futurs accords reste le chantier distinct décrit dans le plan.

## Mesures comparables

Fixture historique isolée, mêmes données métier et même annexe réelle de 38 Mo. Cache disque dédié vide pour les deux premières mesures ; troisième mesure dans un nouveau processus avec cache disque alimenté. Pas de tests concurrents.

| Parcours | Candidat | Préparation figée | Publication isolée | Total |
| --- | ---: | ---: | ---: | ---: |
| before | 102.52 s | 158.04 s | 238.16 s | 498.73 s |
| after | 88.61 s | 2.42 s | 1.94 s | 92.96 s |
| warm | 2.58 s | 2.62 s | 2.54 s | 7.74 s |

Réduction de 81 % à cache vide. Le cas avec cache disque alimenté prend 7,74 s. Le coût initial restant est principalement le décodage YAML. La cible inférieure à une minute est atteinte sur le scénario mesuré avec cache alimenté, pas avec cache vide. Ces durées excluent les contrôles globaux et la recette Atlas ; elles ne se comparent pas directement au temps total de la release métier précédente.

## Changements

- Préparation des annexes par copie exacte, empreinte de source vérifiée pendant la copie et empreinte du résultat contrôlée après écriture.
- Publication des artefacts préparés par copie exclusive ; compilation du candidat, contrats, fraîcheur et empreintes toujours vérifiés avant activation.
- Réutilisation du rapport chargé et suppression des relectures destinées uniquement à réécrire un fichier.
- Cache mémoire : 128 Mio de sources, 128 entrées, au plus 64 Mio par entrée. Les objets Python peuvent occuper davantage.
- Cache disque : 256 Mio, 128 entrées, au plus 64 Mio par entrée. Empreinte des sources, signature du parseur, détection de corruption et indépendance des valeurs conservées.

## Vérifications

63 tests ciblés réussis : publication, préparation, sérialisation, cache et parcours regroupé. Le benchmark compare le contenu métier et les décisions avant/après (hors annotations de version calculées) et vérifie la conservation exacte de la grosse annexe. Les tests couvrent aussi modification après préparation, corruption, non-écrasement, commentaires et fins de ligne.

Commande : `python -m unittest scripts.test_publish_release scripts.test_prepare_release scripts.test_structured_io scripts.test_parsed_cache scripts.test_release_run`.

Mesures détaillées : [mesures.json](mesures.json). Empreintes historiques vérifiées séparément dans `history-check.json`. Aucun changement de pointeur Atlas ni publication réelle pendant les mesures.

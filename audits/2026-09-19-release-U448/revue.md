# Release U448 — préparation et publication

Publication autorisée par U448, depuis la version 2026-09-19.1. Les nouveaux champs proposés restent proposés ; aucune validation globale déduite de la publication.

## Contenu métier examiné

- Six domaines frères ; D03 Fulfillment Optimization contient quatre capacités, D15 Order Promising cinq, D04 Order Management neuf. Aucun domaine imbriqué.
- Ordre de lecture U447 : référentiels, demandes, stocks, exécution, promesse, optimisation de satisfaction, optimisation de stock.
- U445 : Fulfillment Commitment remplace Promise Management sur D03.n ; seul le nom est adopté. Les trois comportements existants sont conservés.
- U439/U442 : définition Structuring reformulée et proposée ; Grouping et Merging proposés sous le même parent. L’ancienne définition validée et son empreinte restent conservées dans la capture préalable.
- U436 : affectation et plan ne bloquent pas les usages concurrents ; la réservation porte seule cet effet. Les nouveaux liens issus de l’audit V0 restent qualifiés comme proposés.

La revue indépendante n’a trouvé aucune anomalie métier bloquante. Les frontières fines PTP/échéancier/plan et les conditions de regroupement/fusion restent ouvertes et visibles.

## Transcription des accords

Le premier rapport signalait 141 champs dont les accords devaient être portés vers les révisions candidates. **72 décisions** transcrivent ces champs, sur preuves strictes : décision historique sur la même identité et la même empreinte, ou portée explicite U438/U445 pour les noms et rattachements présentés. La demande U448 n’est jamais utilisée comme source de validation métier.

Les 173 décisions compatibles sont reprises automatiquement ; 70 anciennes décisions restent conservées mais suspendues pour les révisions modifiées. Les transcriptions remplacent les portées encore applicables, sans reprendre la définition de Structuring désormais proposée. [Preuve par champ](transcription-review.json) ; [décisions supplémentaires](additional-decisions.json).

## Glossaire et effet sur D03.o

110 termes avant et après, sans ajout ni retrait. TER016, TER017 et TER078 reçoivent les notes et réserves U436 ; TER085 actualise les responsabilités D03/D15 et la limite de comparaison Microsoft. Noms, définitions et descriptions courtes de ces quatre termes restent identiques.

L’alerte de référence D03.o → TER078 a été examinée. La précision excluant une réservation implicite ne change pas la définition adoptée de Fulfillment Plan Decision. Son empreinte U378 reste `76114b8bb1548adc61d20c602225630b05176112d5b22299a6a766aad2f1f658`. Les règles de consommation, d’expiration et de réservation automatique restent ouvertes. Aucun nouvel accord sur tout TER078 n’est déduit du statut partiel.

Une formulation historique de l’annexe promesse/affectation a été contextualisée avant préparation : l’absence de nom adopté décrivait U441/U444 ; U445 a ensuite adopté le nom. La capture précédente est conservée dans promise-review-before.yaml.

## Contrôles

44 tests des contrats de modèle, préparation de publication et libellés de relation réussis. Candidat figé sous `modeles/staging/2026-09-19.2/`. Les anciennes publications et preuves sont protégées par un inventaire de 185 empreintes, avec l’index actif capturé séparément puisqu’il doit changer après activation.

## Publication et disponibilité

**Urbanisation v009 / 2026-09-19.2 publiée et activée**, le 19 septembre 2026 à 01:30:37 UTC. Le descripteur [urbanisation-v009-2026-09-19-013037.yaml](../../modeles/release/urbanisation-v009-2026-09-19-013037.yaml) désigne le snapshot figé : 138 nœuds, six domaines, 47 capacités, 76 comportements, 338 relations et 110 termes.

La validation finale ne signale aucune erreur. Les vues ont été régénérées et le frontend est disponible. Le serveur Atlas du projet sert exactement les nœuds, relations et termes du snapshot activé ; la version antérieure 2026-09-19.1 reste accessible et inchangée. Les 185 fichiers protégés conservent leurs octets ; l’ancien index est capturé séparément avant activation. Aucun redémarrage, commit ou push.

[Vérification finale](verification.json) ; [notes de release figées](../../modeles/release/2026-09-19.2/release-notes.md).

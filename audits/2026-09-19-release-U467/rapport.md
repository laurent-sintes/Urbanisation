# Release U467 — Urbanisation v011

**v011 / 2026-09-19.4 publiée et activée le 19 septembre 2026 à 10:45:42 UTC.** Atlas sert le snapshot contrôlé sur [le serveur local](http://127.0.0.1:8765/). [Descripteur](../../modeles/release/urbanisation-v011-2026-09-19-104542.yaml) ; [note de release figée](../../modeles/release/2026-09-19.4/release-notes.md).

## Contenu à tester

- **Glossaire du méta modèle → Information métier** : définition indépendante d’un modèle de données implémentable, exemples et distinction proposition/engagement U466.
- **Comprendre le méta modèle** : six repères actualisés, coopération des univers et domaines sans couches métier ni simulateur de réalisations logicielles.
- **Fiches métier** : définition Supply corrigée, exemples concrets et onglet Marché & choix avec sources et raisons du vocabulaire retenu.
- **Glossaire métier** : 111 termes TER figés, dont Purchase Order Document ; séparation des deux glossaires et défilements déjà implémentés conservés. L’affichage comporte 101 termes métier et 22 termes de méta modèle, dont 12 MOD et 10 TER méthodologiques.

Le catalogue conserve 138 nœuds, 47 capacités, 76 comportements et 338 relations. Aucun ajout ou retrait de nœud, aucun changement de parent. Les révisions des 138 nœuds reflètent notamment le retrait du champ `layer` ; elles ne correspondent pas à 138 changements de responsabilité métier.

Les quatorze fiches d’information et leurs quinze liens U465 sont **figés comme contexte de travail**, sans devenir des éléments consultables dans Atlas. Leur contrat de catalogue et leur écran restent à développer. MOD012 et son exemple sont, eux, accessibles dans le nouveau guide figé `2026-09-19.2`, associé explicitement à v011. Les anciens guides et associations restent inchangés.

## Préparation et accords

123 décisions antérieures sont reprises à révision compatible. Le réexamen explicite transcrit 122 décisions pour les nouvelles révisions, portant sur **208 valeurs approuvées strictement identiques** à leurs preuves v010. Les champs, sources, dates et portée sont conservés ; aucune nouvelle rédaction n’est approuvée par cette opération. [Preuves par champ](transcription-review.json) ; [rapport après réexamen](reviewed-report.json).

Deux blocages de préparation ont été corrigés : les références internes du guide sont désormais contrôlées comme sources embarquées, tandis que ses références racines restent globales ; deux notes générales d’audit ont été rattachées aux premières nouvelles entrées MKT44/ELM260 pour ne plus modifier les captures historiques MKT43/ELM259. Le texte des notes est conservé. Aucun contrôle d’intégrité n’a été contourné.

## Contrôles

- Candidat préparé avec U467 puis publié depuis les entrées figées ; validation finale : **0 erreur**.
- 20 tests de préparation de release réussis ; quatre tests de publication du guide réussis après reprise hors sandbox, nécessaire pour les répertoires temporaires Windows.
- Restitutions générées, serveur contrôlé, frontend compilé déjà à jour par rapport aux sources ; aucune modification frontend dans cette release.
- API : identité FLOW Atlas et racine du projet vérifiées ; modèle, relations, principes et glossaire servis identiques au snapshot ; `sourcePath` désigne `modeles/release/2026-09-19.4/model.yaml`.
- Six parcours navigateur sur la publication réelle réussis, aucune erreur JavaScript. Le premier essai a nécessité une reprise hors sandbox pour lancer Edge sans fenêtre ; un sélecteur ambigu du test Marché & choix a été corrigé avant réussite.
- **301 fichiers historiques inchangés octet par octet**. v010 conserve son ancien guide, sans récupération de MOD012 depuis v011.

[Vérification API et intégrité](api-verification.json), [recette navigateur](browser-verification.json), [capture Information](v011-information.png). Serveur existant PID 24916, port 8765, sans redémarrage. Aucun commit, push ou déploiement distant.

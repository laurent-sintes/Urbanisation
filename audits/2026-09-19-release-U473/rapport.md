# Publication U473 — Urbanisation v013

La release **v013 / `2026-09-19.6`** est publiée et active depuis le 19 septembre 2026 à 12:28:48 UTC. [Atlas local](http://127.0.0.1:8765) sert exactement le snapshot figé, sans redémarrage du serveur existant (PID 24916).

## Changements disponibles

- Supply Chain Orchestration : entrée concrète, chaîne d’approvisionnement expliquée, exemples, liens glossaire avec infobulles, projections des maîtres externes et ingestion explicites.
- Marché & choix : justification du nom et du périmètre de l’univers avec CSCMP, Microsoft et Oracle ; seconde référence ajoutée aux 47 fiches précédemment à source unique. Les 120 fiches publiées qui comportent des comparaisons ont au moins deux URL sources distinctes.
- Business Services et TER067 retirés du courant ; Case et la frontière de Process Tracking corrigés. Commerce reste différé après la Supply Chain.
- Interface déjà construite : bandeau descriptif et onglets fixes, contenu défilant, fil d’Ariane et actions dans la barre haute sur grand écran, logo Beaumanoir discret près des statistiques. Catalogue d’informations masqué, qualifications internes masquées, sources marché accessibles.

La publication contient **137 nœuds, 47 capacités, 76 comportements, 338 relations et 110 termes métier**. Les 14 informations et 15 liens internes restent identiques à v012. Le guide du méta modèle `2026-09-19.2` conserve son contenu et dispose d’une association explicite à v013.

## Accords et intégrité

204 décisions historiques reprises automatiquement ; 40 transcriptions après réexamen explicite de 75 valeurs approuvées inchangées. Sources, date et portée des accords conservées ; aucun accord étendu aux nouveaux textes, exemples ou rapprochements. L’accord sur l’univers retiré reste historique. Les anciennes suspensions restent traçables dans le rapport de préparation, avec les décisions de remplacement séparées.

**430 fichiers historiques inchangés octet pour octet**, anciennes publications et associations conservées. Le modèle et le glossaire du backlog n’ont pas été modifiés par la publication. L’audit ne confond pas les 141 nœuds du backlog avec les 137 nœuds publiables : les quatre illustrations exclues restent du contexte.

## Contrôles

- Préparation figée et publication contrôlée ; validation finale : zéro erreur.
- Restitutions release, backlog et panorama régénérées ; contrôle serveur réussi.
- API : identité du serveur, index, descripteur v013 et égalité complète du modèle servi avec le snapshot vérifiés.
- Huit parcours navigateur réels réussis, aucune erreur JavaScript : univers, infobulles des comportements et du glossaire, fiche et bandeau fixe, trois sources univers, fiche enrichie à deux sources, exemples et masquage interne, deux glossaires et guide, historique v012, lecture mobile.
- Captures desktop et mobile relues : aucun débordement observé. Le frontend n’a pas été modifié pendant cette release ; son build et ses tests précédents restent applicables.

La dernière recette vérifie les écrans servis, pas seulement les données du disque. Un rechargement **Ctrl+F5** permet aux onglets déjà ouverts de charger la nouvelle interface ; une sélection historique reste volontairement fixe.

## Preuves

[Note de release figée](../../modeles/release/2026-09-19.6/release-notes.md) · [Revue avant publication](revue-avant-publication.md) · [Valeurs transcrites](transcription-review.json) · [Rapport de préparation](reviewed-report.json) · [API et intégrité](api-verification.json) · [Recette navigateur](browser-verification.json) · [Capture desktop](v013-base.png) · [Capture mobile](v013-mobile.png).

Aucun commit ni push effectué.

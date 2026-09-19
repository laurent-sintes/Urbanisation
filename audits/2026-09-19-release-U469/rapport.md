# U469 — Release v012 pour la revue de la base

**v012 / 2026-09-19.5 publiée et activée le 19 septembre 2026 à 11:23:23 UTC.** [Ouvrir cette version dans Atlas](http://127.0.0.1:8765/#version=2026-09-19.5). [Descripteur](../../modeles/release/urbanisation-v012-2026-09-19-112323.yaml) ; [note figée](../../modeles/release/2026-09-19.5/release-notes.md).

La priorité est la consolidation de la base, à partir des retours pas à pas de Laurent. L’extension du volet data/information est mise en attente dans les instructions et le suivi. Cette opération publie les travaux existants, sans les développer davantage.

## Périmètre publié

- Base inchangée par rapport à v011 : 138 nœuds, dont 47 capacités et 76 comportements, et 338 relations. Aucun changement de responsabilité, de définition ou de parent pendant cette release.
- Travaux U468 existants : 14 fiches d’information, 21 usages explicites de capacités et 15 liens entre informations, avec leur consultation Atlas. Le modèle backlog est resté identique octet par octet pendant la publication.
- 111 termes de glossaire figés ; guide du méta modèle `2026-09-19.2` repris explicitement, sans nouvelle rédaction ni modification des anciennes associations.
- 245 décisions antérieures conservées, aucune suspendue, aucune nouvelle. Les qualifications proposées des informations restent conservées ; la publication ne les transforme pas en accords métier.

## Vérifications

Préparation contrôlée depuis le backlog avec la source U469, lecture du candidat puis publication depuis le snapshot figé. [Évaluation préalable](evaluation.json) ; le rapport figé fait partie de la release.

- Validation des modèles : zéro erreur, 1 684 sources courantes indexées.
- Restitutions générées ; contrôle du serveur et disponibilité du frontend réussis.
- API : identité FLOW Atlas, racine du projet et version courante vérifiées ; tous les champs du modèle servi sont identiques au snapshot publié.
- Six parcours navigateur sur la publication réelle réussis : univers Supply, fiche Purchase Order et marché, deux glossaires, guide, travaux U468 et conservation de v011. Aucune erreur JavaScript.
- 366 fichiers historiques protégés inchangés. Les entrées antérieures des index et les associations de guides sont conservées ; seule la nouvelle publication est ajoutée et activée.

Aucun changement de code dans cette opération : le build et les 111 tests automatisés du lot U468, déjà réussis sur ce même code, n’ont pas été rejoués sans motif. La recette de disponibilité porte en revanche sur la nouvelle release réelle. [Preuves API et intégrité](api-verification.json) ; [recette navigateur](browser-verification.json).

Le serveur existant, PID 24916 sur le port 8765, n’a pas nécessité de redémarrage. Aucun commit, push ou déploiement distant. La suite attend les retours de revue de Laurent ; aucune généralisation automatique du volet information.

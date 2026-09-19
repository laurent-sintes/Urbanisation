# Atlas — ajustements U459

19 septembre 2026. Changements disponibles dans l’interface locale après rechargement ; aucune nouvelle release.

- **Vue univers** : l’infobulle d’une capacité présente sa définition puis la liste à puces de ses comportements. La liste provient uniquement des relations explicites du snapshot. Elle fonctionne aussi au focus clavier, se ferme avec Échap et ne crée pas de rubrique vide pour une capacité sans comportement.
- **Glossaire** : « En quelques mots » retiré dans les deux glossaires. La définition reste affichée une seule fois, avec contexte et exemples lorsqu’ils existent. Les anciennes URL vers la description courte conduisent à la définition ; aucune donnée historique supprimée. Les définitions n’ont pas été rallongées artificiellement dans ce correctif.
- **Marché** : rubrique « Repères marché » rétablie dans les fiches et le glossaire, avec accès direct depuis le sommaire des fiches. Chaque comparaison indique référence externe, nature du rapprochement, points communs, différences, choix FLOW et source primaire. Les détails sont dépliables pour préserver la lecture de la fiche. Les contenus comparatifs visibles sont également recherchables.

Le retrait des références marché venait d’une interprétation trop large du périmètre métier. U459/C107 corrige cette règle dans AGENTS.md, les conventions, la documentation et le principe courant. Les références comparatives à des offres restent pertinentes ; elles n’affirment pas qu’une solution est choisie ou installée. Statuts de revue, annotations d’accord et liens vers le backlog restent internes.

## Positionnement et couverture

L’interface restitue les qualifications réellement présentes : recouvrement partiel, appui sémantique, appui méthodologique, différence de périmètre, etc. Elle ne transforme pas un recouvrement partiel en conformité à un standard, ni une lacune documentaire en innovation. Les choix FLOW sont désormais explicitement affichés.

Dans v010, des comparaisons sont documentées pour **39 capacités sur 47, 63 comportements sur 76, 3 domaines sur 6, 1 référentiel sur 6 et 8 termes sur 110**. Les trois groupes n’ont pas de comparaison propre. Les autres fiches portent la mention « Positionnement non documenté dans cette publication » ; elles n’héritent pas silencieusement des comparaisons d’un voisin ou du backlog.

Le complément des comparaisons manquantes et des définitions trop brèves reste dans le travail métier du plan, suivi dans [v0-readiness.yaml](../../modeles/backlog/v0-readiness.yaml). Ce correctif ne prétend pas établir un classement exhaustif standard/innovation. [Couverture observée, avec les éléments manquants](market-coverage.json).

## Vérification

- 69 tests frontend réussis ; compilation réussie.
- Validation du modèle : zéro erreur ; restitution backlog actualisée.
- Parcours réels sur v010 : survol et clavier, comportements affichés, capacité sans comportement, marché et sources externes, glossaire et anciens liens, recherche RELEX, écran 390 px sans débordement. Aucun défaut JavaScript observé.
- 303 fichiers historiques protégés identiques ; nœuds et relations inchangés. Les comparaisons publiées n’ont pas été réécrites.

Preuves : [infobulle](universe-tooltip.png), [positionnement marché](market-position.png), [contrôles navigateur](browser-verification.json), [intégrité](integrity.json). Sources métier et portée de la demande : U459 et C107.

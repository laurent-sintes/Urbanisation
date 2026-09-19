# Intégration Cytoscape dans FLOW Atlas

Réalisation technique du 19 septembre 2026, autorisée par U419 après le choix de Cytoscape en U415. Ce dossier consigne la vérification de l'interface ; il ne constitue ni un nouvel audit métier ni une publication du backlog.

## Résultat

L'onglet **Relations** propose trois niveaux : capacités, domaines et référentiels, univers. Le lecteur choisit un voisinage de un à trois pas ou toute la publication, le sens de parcours, la qualification des liens et une disposition organique (fCoSE) ou hiérarchique (Dagre). La sélection donne accès aux relations originales, à leurs qualifications, conditions, effets et sources. Une liste accompagne le canvas pour la lecture au clavier.

La vue agrégée conserve le sens et les identifiants des relations sous-jacentes. Les relations internes restent inspectables. Les comportements sont projetés sur leur capacité explicitement parente, sans réécriture des extrémités originales. Les paramètres d'exploration sont conservés dans l'URL ; le partage fixe la publication consultée. React Flow reste chargé des cartes de structure.

## Frontières

- Une seule publication alimente chaque vue, résolue par index, descripteur et snapshot. Aucun complément depuis le backlog.
- Le filtre « a besoin de » exige un rôle `needs` explicite. Les anciennes qualifications textuelles ne sont pas reclassées automatiquement.
- Les regroupements suivent les rattachements explicites ; les référentiels ne deviennent pas des domaines. Aucun découpage de solution n'est déduit du modèle métier.
- Les nombres représentent des relations documentées, sans mesure implicite de criticité ou de couplage technique. Un parcours ne crée pas de dépendance transitive.

## Vérification

Les contrôles reproductibles sont `pnpm --dir app test`, `pnpm --dir app build` et `pnpm --dir app verify:dependencies`. Le dernier vérifie les publications courante et v003, plus une fixture HTTP synthétique pour les qualifications et agrégations absentes des anciennes publications. La fixture ne lit pas le backlog et ne modifie aucun snapshot.

Avec `ATLAS_URL`, ce test ajoute un contexte indépendant sans interception : chargement réel depuis le serveur Python, CSP, deux dispositions, relation qualifiée, navigation historique et cartes React Flow. Les résultats et captures sont dans [browser/](browser/), notamment [checks.json](browser/checks.json).

Le contrôle sur serveur a détecté l'injection d'un style en ligne par Cytoscape. Sa règle de positionnement est fournie par une feuille locale, identifiée avant l'initialisation du moteur : la CSP reste inchangée. Les anciennes attentes fixes sur les enfants de D04 et le nombre de référentiels ont été remplacées dans les tests navigateur par des comparaisons avec les relations explicites du snapshot.

Les tests unitaires (53), la compilation TypeScript/Vite et la validation des modèles passent. Les dix groupes de contrôles dédiés et les trois parcours supplémentaires sur serveur réel passent, sans erreur JavaScript, réseau ou violation de CSP. La vérification de quatre fichiers de publication par SHA-256 garantit qu'ils ne sont pas réécrits par les tests dédiés.

Les contrôles de navigation générale, arbre, glossaire et cartes d'univers et de référentiels passent également. Les résultats complémentaires restent dans `app/.runtime/qa-react/`, `qa-tree/`, `qa-glossary/`, `qa-universe/` et `qa-references/`.

## Limites

Les moteurs de placement s'exécutent sur le fil principal. Le bundle différé de la vue Relations représente environ 662 ko avant compression (203 ko gzip), et déclenche l'avertissement de taille de Vite. Aucune performance sur des milliers d'éléments n'est déduite des contrôles actuels. Le repli natif de groupes imbriqués n'est pas inclus dans cet incrément.

Les tests navigateur servent un build local ; aucun serveur utilisateur n'est démarré durablement et aucun navigateur visible n'est ouvert par ces vérifications.

# Optimisations appliquées — 19 septembre 2026

Les sept axes de l’audit technique sont traités. Aucun changement métier, release, commit ou push. Les publications et leurs preuves protégées sont conservées ; le modèle actif conserve son empreinte `2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2`.

## Résultats mesurés

| Charge identique | Avant | Après | Lecture |
| --- | ---: | ---: | --- |
| Validation du projet | 5,51 s | 3,39 s | 38 % de temps en moins ; zéro erreur |
| Restitutions complètes | 4,36 s | 2,29 s | 47 % de temps en moins |
| Rapport de préparation | 11,44 s | 5,97 s | 48 % de temps en moins |
| Audit historique complet | 79,30 s | 48,92 s | 38 % de temps en moins |
| Audit inchangé, checkpoint vérifié | 79,30 s auparavant | 0,66 s | Après un rejeu complet réussi ; empreintes revérifiées |
| Catalogue Atlas | 0,877 s | 0,030 s | Médiane de trois lectures après initialisation ; première lecture 0,495 s |
| Révision Atlas | 0,853 s | 0,022 s | Médiane après initialisation ; première lecture 0,615 s |
| Chargement Atlas | 2,760 s | 0,387 s | Médiane après initialisation ; première lecture 0,945 s |
| Rapport affiché | 2 113 710 octets | 3 552 octets | Synthèse ; détail intégral disponible |
| Fixture de publication par test | 40,84 Mo / 284 fichiers | 3,45 Mo / 27 fichiers | Copies indépendantes ; environ 55 Mo au lieu de 653 Mo sur 16 tests |
| Instructions chargées par défaut | 4 385 mots | 1 185 mots | Conventions métier détaillées conservées séparément |

Les mesures des scripts reprennent le protocole initial : une exécution, cache de parsing vidé entre charges, écritures de restitution interceptées. Les lectures Atlas sont des fonctions backend, sans navigateur ni transport HTTP. Les mesures réelles du checkpoint sont séparées : 48,28 s pour le rejeu complet, puis 0,66 s pour sa réutilisation après vidage du cache de parsing. Les gains ne s’additionnent pas. La latence du modèle IA et celle du rendu graphique n’ont pas été mesurées.

## Changements

1. **Lecture structurée** : rejet des alias pendant l’unique analyse YAML. Cache par contenu réel, limité à 128 entrées et 32 Mio de sources ; copie indépendante de chaque résultat. Les objets Python peuvent occuper davantage de mémoire. Le cache ne remplace aucune vérification de signature.
2. **Préparation de release** : lecture unique des annexes et de leurs versions précédentes ; sortie compacte par défaut. `--full` conserve le détail terminal ; `--output` l’écrit dans un nouveau fichier. Les 469 erreurs de validation de publication préexistantes sont toutes conservées et restent bloquantes. Aucun accord créé ou contourné.
3. **Contrôles proportionnés** : matrice dans AGENTS.md ; choix de l’espace avec `render_models.py --space`. Les vues et l’index de provenance identiques ne sont pas réécrits. La publication garde son parcours complet.
4. **Audit historique** : checkpoint local vérifié par SHA-256 des fichiers, inventaires, vues et scripts. Une modification, suppression, addition, corruption du checkpoint ou changement de runtime impose le rejeu ; `--full` le force. Les échecs suppriment l’ancien checkpoint. Une entrée changeant pendant le contrôle interdit d’enregistrer un succès. `-O` est refusé pour conserver les assertions.
5. **Instructions** : noyau courant compact et conventions chargées par sujet. Aucun agent supplémentaire. Les copies de skills, identiques lors de l’audit, ne sont pas supprimées : leur présence n’exécute aucun travail.
6. **Tests** : fixture historique minimale construite une seule fois pour la classe des tests de publication, puis copiée indépendamment ; fixture Atlas limitée aux entrées réellement utilisées. Après cette dernière réduction, les 22 tests Atlas passent en 18,95 s contre 52,14 s au premier passage de ce chantier (déjà avec le nouveau lecteur).
7. **Atlas** : réutilisation des documents analysés via le lecteur commun ; aucune notification React pour un catalogue identique. La publication historique, les changements de pointeur et les reprises après erreur conservent leur comportement.

## Conservation des instructions

| Ancienne section | Emplacement courant |
| --- | --- |
| Priorités et autorités | AGENTS.md, premier tableau |
| Modélisation, Decision/Planning/Management, frontières | Invariants d’AGENTS.md + sections détaillées de CONVENTIONS-MODELE.md |
| Validation, provenance, marché | AGENTS.md + détails conservés dans CONVENTIONS-MODELE.md |
| Exécution et Atlas | Matrice AGENTS.md + modeles/README.md + app/README.md |
| Lecture ciblée, Reservation, clôture U431 | CONVENTIONS-MODELE.md ; clôture rappelée dans AGENTS.md |

[Capture intégrale avant optimisation](AGENTS-before-optimization.md), conservée octet pour octet. Les noms et parents courants du YAML priment sur les repères datés des conventions. Aucun accord historique n’est réactivé.

## Vérification

- Tests du lecteur : scalaires et types, doublons, alias, données invalides, modification de contenu à taille/date identiques, mutations isolées, éviction du cache.
- Tests du checkpoint : changements d’entrée/code/sortie/inventaire, cache invalide, rejeu forcé, échec et modification concurrente.
- Tests de publication, préparation, validation, comportements, comparaisons, glossaire, cycles de vie et versions : réussis.
- Atlas : 22 tests, dont 2 ignorés car l’hôte interdit les liens symboliques ; altérations de publications et absence de repli vérifiées.
- Frontend : 54 tests réussis ; compilation TypeScript/Vite réussie. Avertissement existant sur le module de graphe chargé à la demande (662 Ko), sans mesure graphique justifiant une refonte supplémentaire.
- Contrôle global du modèle : zéro erreur. Audit historique réel : réussi, 125 fichiers protégés inchangés ; résultat identique au checkpoint.
- CLI synthétique avec sauvegarde détaillée : 469 erreurs présentes dans les deux formats. Le serveur local était arrêté lors du contrôle ; aucun service ni navigateur lancé. Les optimisations Python prendront effet à son prochain lancement ; le frontend compilé est prêt.

## Reproduire

`python audits/2026-09-19-performance/measure_after.py` rejoue les mesures après optimisation dans `after/`, sans écraser les mesures initiales. Cette commande est un benchmark complet, pas un contrôle quotidien. Les résultats bruts sont dans `after/*.json`. Pour les interventions courantes, suivre la matrice de contrôles d’AGENTS.md.

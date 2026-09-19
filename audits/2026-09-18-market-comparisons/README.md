# Comparaisons marché — U311

Règle ajoutée à AGENTS.md et à la méthode marché. Les comparaisons sont désormais des données structurées du modèle, avec un contrat commun pour les nœuds et les termes du glossaire. Elles comprennent points communs, différences, position FLOW, statut, source primaire, édition, passage, date de consultation et limites de preuve.

SAP et RELEX sont renseignés sur Replenishment Decision (D05.e), Implantation (TER079) et Réassort (TER080). Ces rapprochements restent proposés pour soutenir la discussion client. Aucune équivalence ni couverture installée n’est validée implicitement.

L’Atlas les affiche dans une rubrique dédiée, sur ordinateur et mobile, avec recherche sur les libellés éditeurs et accès aux sources. Une publication historique ne reçoit jamais les comparaisons du backlog. La compilation ne publie pas les données métier : elles seront visibles dans une release qui les contient.

## Vérifications

- Validation des modèles : zéro erreur.
- Contrat des comparaisons : trois tests réussis, y compris sources obligatoires, dates et URL invalides, compatibilité du glossaire historique.
- Atlas : 36 tests réussis ; compilation TypeScript/Vite réussie.
- Préparation des releases : 16 tests réussis sur projets isolés.
- Contrôle navigateur isolé : fiches capacité/glossaire, liens, recherche, mobile 390 px et publication historique ; [résultats](browser/checks.json).
- Vérification du candidat en mémoire : [conservation des comparaisons et diagnostic](publication-compatibility.json). Aucun fichier publié ni index de release modifié.

Le backlog présente par ailleurs trois relations anciennes vers des objets d’illustration exclus de la publication (REL-ILL-001 à REL-ILL-003). Le diagnostic est comparé au modèle capturé avant U311 ; ce sujet est distinct de l’ajout des comparaisons et reste à corriger avant une publication de ce backlog.

Les captures `model-before.yaml`, `glossary-before.yaml` et `audit-before.yaml` conservent l’état antérieur. Le recalage de l’audit vérifie qu’aucun champ métier préexistant ni relation n’a été altéré par U311.

# Comportements ATP et Atlas — U264

17 septembre 2026. Implémentation des choix U262/U263 sur demande U264.

## Résultat

- Nouveau type `behavior`, rattaché par `contains` à une capacité unique de même couche. Parent absent/multiple, autre type, couche différente, nom/définition vides et sous-niveaux refusés.
- BHV001–BHV004 rattachés explicitement à D03.i. Définitions adoptées U263 inchangées et empreintes conservées ; noms anglais, finalités et périmètres proposés. ATP et TER044 actualisés ; ancienne définition ATP conservée dans le snapshot avant modification, adoptions inchangées limitées aux nom/finalité/nature.
- Backlog : 63 nœuds, **41 capacités et 4 comportements**, 92 relations. Les quatre illustrations préexistantes restent hors publication. Glossaire méthodologique séparé, convention MOD006 et feuille de route actualisées.
- Atlas : comportements terminaux dans l’arbre, navigation clavier, filtre de type et recherche par ascendance/contenu ; descriptions après la définition de la capacité ; fiche individuelle avec retour à ATP ; icône et compteur distincts ; liens depuis la carte ATP dans Order Promising ; carte des quatre comportements.
- Restitution Markdown dérivée étendue. Frontend compilé dans app/dist, compatible avec le serveur actuel.

## Vérifications

- `validate_models.py` : **0 erreur**, provenance 1 214 enregistrements ; restitutions régénérées et `git diff --check` sans anomalie.
- Tests Python : **51 cas vérifiés** au total (24 intégrité modèle, 8 publication, 3 comportements et 16 préparation). La dernière relance des suites comportements/préparation termine avec **19/19** ; les 32 autres avaient passé. Deux dépendances historiques des fixtures corrigées : glossaire vivant incompatible avec ancien modèle et date de publication de test antérieure aux publications copiées. Aucun assouplissement des contrôles métier.
- Tests Atlas : **35/35**. Compilation TypeScript/Vite réussie ; avertissement habituel sur la taille du chunk ELK conservé.
- `verify-behaviors.mjs` : **six parcours bureau/mobile validés**, aucune erreur JavaScript, captures examinées. Vérifications : quatre définitions exactes, liens conservant la version, navigation clavier et terminalité, recherche filtrée, cartes et fiche, largeur mobile 390 px sans débordement, ancienne publication sans repli sur backlog.
- Projection par le compilateur de publication en mémoire : les quatre comportements et leurs définitions sont conservés, avec adoption partielle limitée à la définition dans la fixture de décision.

Les premières compilations/tests Node ont été bloqués par Windows (`spawn EPERM`) ; relance autorisée hors bac à sable. Les tests navigateur utilisent une interception limitée à leur navigateur et une identité de test 2099-01-01.1. Les captures ne représentent pas une nouvelle publication réelle.

## Publication distincte

Les **134 fichiers figés** inventoriés dans protected.json restent inchangés. Le serveur répond toujours avec la publication 2026-09-16.2 (v007). Aucune release, aucun commit ni push.

Le contrôle de candidat en lecture seule conserve les quatre comportements et ne relève aucune erreur de topologie/schéma. Il signale les transcriptions de décisions attendues lors d’une prochaine release pour les nouvelles révisions ATP, CTP préexistant et comportements/rattachements. C’est le travail habituel de préparation des preuves de publication, non une validation automatique par le changement de code. Détail dans candidate-check.json ; aucun candidat préparé ou activé par ce contrôle.

Captures et résultats : browser/results.json, browser/atp-sheet-desktop.png, browser/atp-sheet-mobile.png, browser/behavior-mobile.png et browser/domain-map.png.

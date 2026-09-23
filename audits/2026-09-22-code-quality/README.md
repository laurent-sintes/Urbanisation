# Audit de qualité Python et JavaScript/TypeScript

Date : 22 septembre 2026. État audité : répertoire de travail courant, comprenant les changements non commités. Audit sans correction du code métier ni modification des données réelles. Les reproductions Python utilisent les fixtures temporaires existantes ; le test de boucle JS est borné à 100 ms dans une VM, sans navigateur.

## Conclusion

Les contrats explicites, les tests de mutation, la séparation des publications et du backlog, le typage TypeScript strict et les contrôles des chemins constituent de bons garde-fous. Quatre défauts concrets subsistent malgré les tests réussis. Priorité à la conservation de la preuve historique, puis au contrôle du remplacement d’accord, au blocage de l’interface et à la robustesse du CLI Windows.

L’audit a inventorié 125 fichiers Python dans `scripts/` et `app/`, dont 34 fichiers de tests, et examiné de façon ciblée les parcours de registre, publication, validation, cache, serveur, navigation, recherche et rendu. Il ne constitue pas une revue ligne par ligne des scripts de migration historiques, une mesure de couverture des branches, un audit des dépendances ni une recette navigateur.

## Défauts confirmés

### F1 — P1 : la disparition de la preuve figée désactive le contrôle historique

Localisation : `scripts/decision_registry.py:124`, également `scripts/prepare_release.py:343–349`.

Le lecteur considère qu’un fichier `deferred/decision-intents.yaml` absent signifie qu’aucun registre n’a été consommé. C’est légitime pour une ancienne publication sans registre, mais pas pour une publication qui en avait figé un. L’existence sur disque ne permet pas de distinguer ces situations.

Reproduction : figer un accord, le retirer de l’index courant ; la validation le rejette. Supprimer ensuite le fichier figé : le même contrôle retourne zéro erreur et zéro accord, avec un fragment non référencé. La vérification devient donc permissive lorsque la preuve nécessaire disparaît. Le parcours de préparation emploie le même repli ; `load_current` vérifie les trois entrées principales et les preuves de réexamen, mais pas l’existence attendue de cette annexe.

Correction recommandée : conserver et vérifier un inventaire authentifié des annexes figées dans la publication ; accepter l’absence seulement si la publication d’origine n’en déclarait aucune. Contrôler l’empreinte de l’index figé et de ses fragments avant de l’utiliser comme référence. Ajouter une régression sur une publication déclarant un registre ensuite supprimé ou altéré.

### F2 — P2 : le remplacement d’accord utilise un résumé non vérifié

Localisation : `scripts/decision_registry.py:212–227`.

Le parcours rapide contrôle les empreintes des fragments, mais décide de la portée autorisée d’un remplacement à partir des résumés de l’index. Il relit le fragment si le nouvel identifiant existe déjà, sans relire celui nommé par `supersedes`.

Reproduction : ajouter `scope` à `approved_fields` dans le résumé du prédécesseur, sans modifier son fragment. Enregistrer un remplacement qui porte seulement sur `scope` renvoie `recorded: true`. La validation exhaustive rejette ensuite le registre avec `Registry shard summary mismatch` : le contrôle de publication protège encore la sortie, mais l’enregistrement a confirmé un résultat invalide.

Correction recommandée : charger et valider le fragment du prédécesseur avant d’évaluer le remplacement, puis utiliser sa portée réelle. Ce contrôle ciblé préserve le gain du découpage sans reparser tout l’historique.

### F3 — P2 : une recherche Unicode peut bloquer le rendu de la source

Localisation : `app/src/components/SourceDialog.tsx:13–15`.

`highlight` vérifie que la requête brute n’est pas vide, puis retire les diacritiques. Une requête composée uniquement de l’accent combinant U+0301 devient une chaîne vide. `indexOf('')` retourne zéro et `position` n’avance jamais : la boucle s’exécute sans fin sur le fil du rendu React.

Reproduction : extraction de la fonction réelle, remplacement du JSX par sa tranche de texte équivalente, exécution dans `vm` avec une limite de 100 ms. Résultat : expiration du délai. Le cas est rare, mais une simple saisie/copie de ce caractère suffit ; aucun document malformé n’est nécessaire.

Correction recommandée : vérifier la requête après normalisation, et partager cette normalisation avec le compteur des correspondances. Extraire la fonction de recherche/surlignage pour la tester directement, notamment avec accents combinants et chaînes vides après normalisation.

### F4 — P2 : la commande d’inspection échoue avec la console Windows courante

Localisation : `scripts/inspect_model.py:84`.

La sortie utilise `ensure_ascii=False` sans imposer un encodage UTF-8 du flux. Dans l’environnement Windows courant, la commande documentée échoue lorsqu’un champ ou une relation contient notamment `→` (U+2192).

Commande reproduite :

```powershell
python scripts/inspect_model.py D08 D08.d D08.e D02.b business-references --fields name definition scope purpose nature --relations
```

Résultat : `'charmap' codec can't encode character '\u2192'`. Les tests actuels vérifient la fonction `inspect`, sans exercer cette sortie du CLI. `python -X utf8` est un contournement disponible, pas une correction intégrée à la commande documentée.

Correction recommandée : définir une stratégie UTF-8 commune aux points d’entrée Python, ou utiliser une sérialisation JSON échappée lorsque le flux ne permet pas l’Unicode. Tester le CLI en sous-processus avec encodage contraint et caractères non ASCII.

## Maintenabilité — améliorations proposées, sans défaut fonctionnel supplémentaire déduit

- **Contrats du registre couplés à l’écriture** : `decision_registry.contract()` réimporte `record_decision`, lequel importe déjà le registre, et appelle ses fonctions privées. Extraire les contrats purs, empreintes et règles de succession dans un module indépendant réduirait ce couplage circulaire.
- **Validation centrale dense** : `validate_urbanism` compte 205 lignes et 81 constructions de branchement/comptage AST. Ces chiffres ne sont pas une mesure de complexité cyclomatique. Séparer les contrôles de topologie, de niveaux et de métadonnées faciliterait l’extension ciblée. La très grande fonction du script d’audit historique est inventoriée dans `metrics.json`, sans recommander de rouvrir cet audit métier clos.
- **Fonctions d’interface peu accessibles aux tests** : les tests JS couvrent surtout les modules de données et de navigation ; le bug du surlignage se trouve dans une fonction privée d’un composant TSX. Extraire les traitements purs et ajouter quelques tests ciblés apporte plus de valeur qu’une multiplication de tests reproduisant le JSX.
- **Contrôles statiques** : TypeScript est en mode strict. Aucune configuration Ruff/ESLint ni workflow `.github` n’a été trouvé dans le périmètre du dépôt inspecté. Introduire progressivement des règles de défauts probables et de hooks, sans reformatage global des archives. Cela ne remplace pas les tests d’intégrité.
- **Point d’entrée des tests Python** : certains tests acceptent l’import `scripts.test_*`, tandis que `test_lifecycle` utilise un import direct `lifecycle`. Un lanceur maintenu évitera les différences de découverte et les faux échecs d’import.

## Vérifications et résultats

| Vérification | Résultat |
| --- | --- |
| Tests Python des scripts | 267 cas réussis dans le lancement par modules ; le module lifecycle avait une erreur d’import liée à ce lancement. Ses 7 tests passent avec la découverte depuis `scripts` : 274 cas exécutés avec succès au total. |
| Tests Python du serveur et du guide | 40 cas : 37 réussis, 3 ignorés car les liens symboliques ne sont pas autorisés sur cet hôte Windows. |
| Tests JavaScript/TypeScript | 95 réussis via `pnpm --dir app test`. |
| Build Atlas | `tsc --noEmit` et Vite réussis ; avertissement existant de chunk supérieur à 500 Ko. |
| Analyse syntaxique Python | Fichiers inventoriés analysés par `ast.parse`. |
| Reproductions | F1 et F2 : fixtures isolées ; F3 : fonction extraite et VM bornée ; F4 : commande réelle en lecture seule. |

Les premiers lancements des tests JS/build ont nécessité l’autorisation des sous-processus Windows après `spawn EPERM` du bac à sable. Ce blocage d’environnement n’est pas classé comme défaut applicatif. La découverte Python avec `-t .` a également été remplacée par le lancement explicite des modules ; l’erreur d’import lifecycle a été vérifiée séparément. Les logs conservés rendent ces limites visibles.

## Preuves locales

- `reproduce.py` et `reproductions.json` : F1/F2, sans mutation des données réelles.
- `reproduce.mjs` : F3 ; ne pas supprimer sa limite d’exécution.
- `inspect-console.log` : F4.
- `python-tests.log`, `lifecycle-tests.log`, `server-tests.log`, `js-tests.log`, `build.log` : résultats des vérifications.
- `metrics.json` : inventaire Python et tailles de fonctions.

Aucune correction applicative, nouvelle publication, commit ou push n’a été effectué par cet audit.

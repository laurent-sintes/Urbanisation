# Audit de performance du projet FLOW

**Mise en œuvre terminée :** [changements, mesures après optimisation et contrôles](optimisations.md). Les constats ci-dessous décrivent l’état initial audité.

19 septembre 2026 — audit technique du travail sur le modèle et des chemins de lecture Atlas. Cet audit ne rouvre pas l’audit métier clos U431.

## Conclusion

Le ralentissement est confirmé et ses principales causes sont identifiées. Le coût dominant est l’analyse répétée des fichiers YAML, amplifiée par la relecture de l’historique et par l’application trop systématique du workflow complet à de petites modifications. Les volumes de sortie et l’accumulation des instructions alourdissent aussi le travail de l’agent.

Il n’est pas nécessaire de supprimer les preuves, d’affaiblir les contrôles ou de remplacer le YAML. Une expérience isolée réduit déjà d’environ 40 % plusieurs commandes en évitant une seconde analyse du même texte. Un cache limité à une invocation améliore encore la comparaison de release.

Les changements recommandés ne sont pas appliqués au code de production dans cet audit. Seuls ce dossier de mesures, les expériences isolées et une note de journal ont été ajoutés. Modèle, index de publication, sources courantes et instructions sont restés identiques pendant les mesures.

## Mesures

Environnement : Windows, Python 3.14.6, PyYAML 6.0.3, implémentation Python sans LibYAML (`__with_libyaml__ = false`). Mesures successives sur la machine locale, sans lancer les charges lourdes en parallèle. Une mesure par commande ; elles indiquent un ordre de grandeur, pas un engagement statistique. Le démarrage du processus et les imports sont exclus des temps internes ci-dessous.

Les écritures de restitution et d’index ont été interceptées en mémoire. Les calculs et contrôles sont exécutés ; les fichiers métiers ne sont pas régénérés. Pour Atlas : trois appels directs aux fonctions du backend, sans réseau ni navigateur. Le temps de génération des réponses de l’IA n’est pas mesuré.

| Commande ou chemin | Temps actuel mesuré | Observation |
| --- | ---: | --- |
| Actualisation des sources | 0,21 s | Faible coût ; pas une priorité d’optimisation. |
| Validation du projet | 5,51 s | 5,19 s dans les lectures structurées. |
| Restitutions Markdown | 4,36 s | 4,33 s dans les lectures structurées ; trois sorties régénérées. |
| Construction du rapport de release | 11,44 s | 130 lectures pour 79 fichiers ; 10,66 s dans les lectures structurées. |
| Contrôle et génération de l’audit historique | **79,30 s** | 45 fichiers structurés, 30,93 Mo analysés ; 78,87 s dans leur lecture/analyse. |
| Vérification des 125 empreintes protégées | **0,021 s** | Les SHA-256 des publications ne sont pas le goulet principal. |
| Atlas : catalogue des publications | 0,88 s médiane | Relit et analyse le modèle publié pour retourner un catalogue. |
| Atlas : calcul de révision | 0,85 s médiane | La résolution de release analyse déjà le modèle. |
| Atlas : chargement du modèle | 2,76 s médiane | Plusieurs analyses du même modèle au cours du traitement. |

Enchaîner actualisation, validation, rendu et audit représente environ **89 secondes de calcul** dans cette mesure, avant les recherches, l’analyse et les échanges. Relancer cette chaîne après chaque ajustement rend perceptible une lenteur qui augmente avec l’historique.

Preuves : [mesure de l’audit](audit.json), [validation](validate.json), [restitutions](render.json), [release](report.json), [Atlas et empreintes](runtime.json), [empreintes des entrées](inputs.json).

## 1. Analyse YAML doublée — priorité haute

Dans `scripts/structured_io.py:69`, `loads()` parcourt une première fois les événements avec `yaml.parse` pour interdire les alias, puis appelle `yaml.load` pour construire les valeurs. Les deux passes utilisent le parseur Python. `dumps()` ajoute une validation aller-retour utile, qui réutilise elle-même ce lecteur à deux passes.

Exemple : analyser le modèle de 1,05 Mo prend 2,43 s ; la même valeur est produite en 1,34 s avec un rejet des alias pendant l’unique construction. Le poids du fichier seul n’explique donc pas le coût.

### Expérience isolée

`experiments.py` utilise un Loader dérivé dans le processus de mesure, sans modifier `structured_io.py` ni les fichiers chargés. Il rejette les alias lors de la composition, tout en conservant les résolveurs et constructeurs existants.

| Charge | Actuel | Une seule analyse | Gain observé |
| --- | ---: | ---: | ---: |
| Validation | 5,51 s | 3,32 s | 40 % |
| Restitutions | 4,36 s | 2,65 s | 39 % |
| Rapport de release | 11,44 s | 6,91 s | 40 % |
| Rapport + cache par invocation | 11,44 s | 5,95 s | 48 % |

L’expérience compare les valeurs sur trois documents réels et les résultats sur 18 cas limites : alias et cycle, clés dupliquées ou non textuelles, types implicites, nombres non finis explicites, tags, document malformé et documents multiples. Elle vérifie également qu’une mutation du résultat mis en cache ne contamine pas une lecture suivante et qu’un contenu modifié n’utilise pas l’ancienne valeur.

Ce résultat justifie une implémentation ciblée, pas une adoption sans tests : conserver les tests de contrat, les refus de données interdites et les contrôles de publication. La variante LibYAML n’a pas été testée et n’est pas requise pour obtenir ce premier gain.

Le cache expérimental est fondé sur le contenu et retourne une copie : 61 accès réutilisés pour 69 entrées pendant le rapport. Un cache de dictionnaires mutables partagé sans copie serait dangereux : plusieurs scripts enrichissent ou modifient les structures chargées.

Preuves : [expérience parseur](parser-experiment.json), [mesures une passe](singlepass/report.json), [mesure avec cache](singlepass-cache/report.json), [contrôles du cache](cache-experiment.json).

## 2. L’audit courant rejoue l’historique — priorité haute

`scripts/render_behavior_gap_audit.py:28` déroule les migrations successives, leurs captures avant modification et leurs empreintes. Le script atteint 1 197 lignes et environ 120 Ko. Il lit 45 fichiers structurés différents : un simple cache de lectures répétées ne résoudra donc pas l’essentiel de ses 79 secondes.

Le script mélange trois responsabilités : vérifier l’intégrité historique, contrôler l’état courant et produire des pages. Les restitutions accumulent les anciens états sous un en-tête courant ; elles sont longues et peuvent ramener l’agent vers des arbitrages déjà soldés.

**Recommandation :** séparer une validation courante ciblée, une restitution courante et un contrôle historique explicite. Conserver toutes les captures. Après un contrôle historique réussi, enregistrer un résultat vérifié avec les empreintes des entrées et la version du vérificateur. Si ces entrées et le vérificateur sont inchangés, leur empreinte permet de réutiliser ce résultat ; sinon le contrôle complet doit être refait. Un simple booléen « audit clos » ou un cache basé uniquement sur la date de fichier ne suffit pas.

Cet audit métier est désormais clos : aucune raison de rejouer sa totalité après une discussion, une modification d’instruction ou une correction du frontend. L’exécution complète garde sa place pour une évolution de la chaîne de preuve, une modification du vérificateur ou un contrôle de publication concerné.

## 3. Rapports trop volumineux et lectures répétées — priorité haute

Le rapport de release sérialisé représente **2 113 710 octets**, soit environ 2,11 Mo. Il contient les avant/après détaillés et 43 annexes de contexte. Dans le tour précédent, cette sortie a été tronquée par l’outil, ce qui a nécessité une nouvelle exécution pour obtenir les compteurs utiles. Une réponse tronquée coûte donc à la fois du transfert, du contexte et des relances.

Dans `scripts/prepare_release.py:262` puis `:278`, les annexes sont relues pour collecter les références, comparer le contenu et produire les différences. Certaines sont analysées trois fois. La résolution de la release lit également le modèle, qui est relu par l’appelant.

**Recommandation :** rendre le résumé par défaut : version, compteurs, erreurs regroupées, validations conservées/suspendues, alertes de glossaire. Le détail reste disponible par identifiant ou fichier. Le JSON exhaustif doit être écrit une seule fois dans un artefact explicite et non imprimé par défaut dans la conversation. Charger chaque document une fois par opération et réutiliser sa valeur avec une stratégie de mutation explicite.

Le rapport de préparation conserve actuellement **469 erreurs de correspondance entre validations de lifecycle et décisions de publication**. Ce sont les erreurs métier/techniques déjà signalées dans U432, pas un défaut de la mesure ni une conséquence des expériences. Les variantes du parseur ne doivent pas les masquer. Les huit impacts de glossaire restent également à examiner pendant la préparation de release.

## 4. Workflow de contrôle disproportionné — priorité haute

`AGENTS.md:99` décrit une chaîne générale sources → validation → rendu. Elle ne propose pas de niveaux selon les fichiers réellement modifiés. Dans les échanges récents, j’ai appliqué trop souvent cette chaîne, parfois après un simple enregistrement documentaire, et ajouté des reprises du contrôle historique. Une part du ralentissement vient donc de ma méthode de travail.

### Matrice proposée

| Modification | Contrôle utile | Ce qui ne doit pas être systématique |
| --- | --- | --- |
| Discussion sans modification | Lecture et comparaison ciblées | Validation/rendu/tests du catalogue. |
| Contribution ou comparaison documentaire | Index des sources si les sources indexées changent ; contrôle des références ajoutées | Rejouer tout l’audit historique, rendre le modèle inchangé. |
| Annexe de proposition | Contrat et références de l’annexe, restitution concernée | Revalidation des captures métier sans rapport. |
| Catalogue/glossaire | Validation du graphe et des contrats affectés, puis rendu concerné | Répéter les mêmes tests après chaque fichier du même lot. |
| Code Python | Tests du module et de ses contrats consommateurs | Recompiler le frontend inchangé. |
| Frontend | Typage/build et tests du comportement modifié | Revalidation de l’historique des arbitrages métier. |
| Publication | Préparation figée, contrôles complets de publication, preuve et contrôle Atlas | Retirer un contrôle pour obtenir un feu vert artificiel. |

La matrice est une proposition d’évolution des instructions ; elle n’a pas remplacé les règles actives. Implémenter des commandes ciblées avant d’en faire le workflow standard. Grouper les modifications d’un lot, puis vérifier une fois ; recommencer seulement si des entrées pertinentes changent, si un test échoue ou si un doute nouveau apparaît.

Les sorties générées devraient être réécrites seulement lorsque leurs octets changent. Cela évite de modifier inutilement les dates, déclencher des observateurs ou charger les diffs de bruit.

## 5. Instructions et agents — priorité moyenne

- Un seul `AGENTS.md` actif a été trouvé ; **130 lignes mais 4 385 mots et environ 34,7 Ko**. De nombreux paragraphes très longs expliquent cette différence entre lignes et volume.
- Les quatre skills du dépôt et leurs copies personnelles sont identiques. C’est une duplication de distribution, pas la preuve d’un chargement double à chaque tour. Lire une seule copie pour une invocation suffit ; une vérification d’empreinte peut contrôler leur synchronisation.
- L’inventaire des agents actifs ne montre que l’agent principal. Aucun travail parallèle de sous-agents n’a été lancé pour cet audit. Les noms d’anciens agents présents dans le contexte ne prouvent pas qu’ils tournent encore.
- Les instructions mêlent règles permanentes, détails de capacités et comptes rendus successifs. Certaines mentions « à instruire » restent présentes avant des paragraphes plus récents qui les ont résolues. Lire tout le fichier pour reconstruire cette chronologie coûte du contexte et peut provoquer des réexamens inutiles.
- Les listes de fichiers non suivis et les lectures complètes de gros documents ont aussi été trop souvent renvoyées dans les outils. Préférer les compteurs, chemins concernés et passages ciblés.

**Recommandation :** un `AGENTS.md` stable, visant environ 1 000 à 1 500 mots : autorités, invariants de modélisation, portée des validations, workflow proportionné, pointeurs. Déplacer les décisions de domaine dans leurs annexes déjà existantes, avec un index d’état courant. Ne pas effacer les accords ni créer un second catalogue. Les instructions historiques restent des preuves, pas des instructions actives.

La taille du contexte et la répétition des lectures sont observées ; leur contribution exacte à la latence du modèle IA n’a pas été mesurée. Aucun changement de modèle IA ni multiplication d’agents n’est justifié par ces seules mesures.

## 6. Tests et scripts d’opération — priorité moyenne

`scripts/test_prepare_release.py:19` copie sept répertoires du projet pour **chaque test**, dont le backlog et tout son historique, puis remplace le modèle de travail par un ancien jeu de données. Au moment de l’audit, cela représente **284 fichiers / 40,84 Mo par test**, pour 16 méthodes : environ **653 Mo recopiés** sur une exécution complète, hors sorties des tests.

La fixture grandit donc avec le travail du projet alors que les tests visent un contrat historique stable. Réduire la fixture aux fichiers effectivement nécessaires et préparer une base une fois ; chaque test conserve sa copie privée des fichiers qu’il modifie. Ne pas partager des données mutables entre tests, ni utiliser des liens physiques vers les publications réelles.

Le dossier compte 85 scripts Python, dont 52 scripts d’opération ponctuelle (`apply_*`, `record_*`, etc.). Leur présence ne consomme pas du CPU par elle-même. Elle accroît cependant le coût de recherche et encourage la production d’un nouveau script et de plusieurs captures pour une petite modification. Distinguer outils maintenus et preuves d’opérations ; factoriser les primitives communes. Aucun script historique ne doit être rejoué ni supprimé automatiquement pour « nettoyer ».

## 7. Atlas : chemin de lecture coûteux — priorité moyenne pour ce problème, haute pour l’interface

`scripts/release_catalog.py:79` appelle `resolve_release()`, qui analyse le modèle publié, puis recharge les descripteurs. `app/src/usePublication.ts:20` déclenche une vérification toutes les cinq secondes lorsque la page est visible ; `publication.ts` demande `/api/releases`, même si aucune publication n’a changé.

La médiane locale de **0,88 s par catalogue** concerne le modèle publié actuel de 0,32 Mo. La prochaine release sera plus riche : extrapoler un temps exact serait injustifié, mais refaire cette analyse à chaque interrogation aggravera le coût. `load_model()` passe plusieurs fois par les fonctions de résolution/chargement et atteint 2,76 s.

**Recommandation :** mettre en cache les descripteurs et le modèle d’une publication immutable après validation ; invalider lors du changement d’index, descripteur, modèle ou configuration. Conserver la vérification d’intégrité et les protections de chemins. Le cache de l’index doit suivre les publications ; une version historique doit rester fixe. Éviter également d’émettre un nouvel état React lorsque version et catalogue sont identiques.

Le découpage différé des modules graphiques existe déjà ; les composants utilisent des mémorisations et évitent de recalculer le placement lors d’une simple sélection. Le bundle graphique compilé est d’environ 662 Ko non compressé, chargé séparément. Cela ne suffit pas à désigner Cytoscape ou React Flow comme cause principale. Aucun profil navigateur/GPU n’a été effectué ; cette investigation viendra seulement si une lenteur de manipulation persiste après correction du backend.

## Plan d’action priorisé

| Ordre | Action | Bénéfice attendu | Condition de sûreté |
| --- | --- | --- | --- |
| 1 | Sorties compactes et commandes de contrôle ciblées ; adapter le workflow | Éviter les dizaines de secondes de travail inutile et les rapports tronqués | Maintenir les contrôles complets avant publication. |
| 2 | Lecteur YAML à une passe | Environ 40 % sur les commandes mesurées | Étendre les tests de compatibilité et conserver tous les refus actuels. |
| 3 | Réutiliser les lectures pendant une commande ; séparer résolution et chargement | Rapport mesuré à 5,95 s avec les deux optimisations combinées | Cache limité, invalidation par contenu, isolation des mutations. |
| 4 | Séparer audit courant, rendu et preuve historique | Éviter les 79 s hors changements pertinents | Attestation liée aux empreintes des entrées et au vérificateur ; contrôle complet sinon. |
| 5 | Compacter AGENTS et indexer l’état courant des décisions | Réduire lectures et ambiguïtés | Tableau de correspondance ancien → nouveau ; aucun accord perdu. |
| 6 | Réduire les fixtures de test | Éviter environ 653 Mo de copies pour cette suite | Isolation et mêmes assertions métier/techniques. |
| 7 | Cache de publication Atlas et notifications React sans changement | Réduire interrogation et chargement | Tests changement d’index, version historique, fichier altéré, requêtes concurrentes. |

Les gains ne s’additionnent pas simplement : le cache et la réduction du nombre de commandes évitent parfois le même travail. Ne pas promettre un facteur global de vitesse à partir de ces seules mesures.

## Reproduction et périmètre

Depuis la racine, exécuter successivement, pas en parallèle :

```powershell
python audits/2026-09-19-performance/measure.py
python audits/2026-09-19-performance/experiments.py
python audits/2026-09-19-performance/runtime.py
```

Ces outils de diagnostic écrivent leurs résultats uniquement dans ce dossier et interceptent les écritures des tâches mesurées. Ne pas les utiliser comme remplacement des commandes réelles de publication. Le cache et le Loader expérimentaux restent locaux aux processus de mesure. Aucun paquet installé, aucun serveur démarré ou redémarré, aucune release, aucun commit/push, aucune modification des règles actives.

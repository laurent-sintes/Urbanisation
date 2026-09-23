# Audit — historique Git et publication légère

Audit du 23 septembre 2026, sur `66b4d7a2fc796ea4d48fe7da0461a794fab1c345`. Rapport technique : les propositions ci-dessous ne modifient ni les accords métier ni les règles actives de publication.

## Conclusion

Une refonte du stockage des accords et du parcours de publication est justifiée. Les optimisations de v020 ont corrigé l'explosion des rapports, mais le système continue à entretenir un historique parallèle à Git et à le contrôler pendant les opérations courantes.

Recommandation : une branche normale `codex/refonte-publication-legere` dans le dépôt actuel, éventuellement dans un worktree distinct. Conserver le modèle, les glossaires, les connaissances marché et le rendu Atlas ; remplacer le mécanisme de conservation, de validation et de publication. Cette recommandation a ensuite été autorisée et mise en œuvre ; voir le bilan de refonte en fin de document.

## Mesures après les modifications

Windows 11, Python 3.14.6. Deux publications complètes dans une copie isolée des données, à partir de v020, avec une seule modification éditoriale de `review.note`. Activation dans la copie, vérification HTTP exclue. Cache de parsing sur disque vide puis rempli ; cache mémoire vidé entre exécutions. La copie initiale (1,74 s) est exclue. « Froid » ne signifie pas cache système vidé. Une observation par cas : ni médiane ni engagement de performance.

| Étape | Cache froid | Cache chaud |
| --- | ---: | ---: |
| Construction du candidat | 67,83 s | 10,58 s |
| Préparation figée | 13,03 s | 13,37 s |
| Publication | 11,10 s | 10,52 s |
| Contrôles finaux | 4,45 s | 4,29 s |
| Total, initialisation comprise | **104,06 s** | **40,18 s** |

Les deux publications aboutissent sans erreur de validation. Le total comprend des opérations hors des quatre phases. Ces mesures ne reproduisent pas la consolidation de v020 avec ses 236 réexamens et ne permettent pas d'annoncer un gain direct par rapport aux 30 minutes ressenties.

Le benchmark maintenu `benchmark_record_decision.py --target D04.i --source U627 --runs 2` mesure une capture à **4,17 s**, la suivante à **0,41 s**, et la répétition idempotente à **0,21 s**. Il contrôle la conservation des valeurs et suspensions historiques sur copies temporaires. La vérification exhaustive finale a été exécutée en concurrence avec le profilage : sa durée n'est pas retenue comme référence.

Atlas local, observations uniques : statut **0,10 s**, modèle **0,84 s** (2,76 Mo), catalogue **0,10 s**. Le serveur réel reste sur v020.

Un profilage distinct d'une publication complète relève **14 appels à `validate_urbanism`**, **6 à `validate_release`**, **3 à `load_current`**, **4 à `read_registry`**, **2 à `read_consumed_registry`**, 57 lectures structurées et 9 sérialisations structurées. Ces appels ne portent pas tous sur le même objet : ils révèlent les couches successives de contrôle, pas 14 contrôles strictement identiques. Les durées instrumentées ne sont pas utilisées comme benchmark.

## Poids du système

Inventaire des fichiers suivis à HEAD, hors dépendances et caches ; Mo décimaux.

| Ensemble | Taille |
| --- | ---: |
| Arbre suivi complet : 2 870 fichiers | **549,3 Mo** |
| Publications `modeles/release` | 127,8 Mo |
| Révisions et sources figées | 175,5 Mo |
| Captures du registre courant | 46,1 Mo |
| Audits | 117,6 Mo |
| Provenance | 35,8 Mo |
| Décisions par publication | 6,2 Mo |
| Connaissance marché `marche` | **2,2 Mo** |
| Contributions et connaissances `connaissance` | 1,5 Mo |

Les blobs uniques représentent 478,2 Mo avant compression ; les packs Git occupent environ 94,9 Mo. Ces grandeurs ne s'additionnent pas. Le backlog contient aussi 21,8 Mo de `history/`, hors captures du registre.

Le `changes.json` de v020 est passé de 108,95 Mo à **1,71 Mo**, mais celui de v019 reste à **85,65 Mo**. Les anciennes copies expliquent donc encore une grande partie du poids courant. La base marché n'est pas la cause du problème.

Le dépôt contient 22 publications, 11 commits et aucun tag. Le premier commit date du 13 septembre 2026 (`68b3064`). Cela prouve que les captures manuelles ont continué après l'arrivée de Git ; cela ne suffit pas à établir pourquoi elles ont été créées initialement.

## Constats sur le code et les règles

1. **Le registre courant porte son passé.** `record_decision.validate_consumed_intents` et `decision_registry.validate_project_registry` exigent la conservation exacte des captures consommées et des suspensions historiques. Le découpage en fragments facilite l'écriture, mais n'enlève pas cette dépendance. Les 75 anciennes captures restent volumineuses malgré le format compact des nouvelles.
2. **La publication traverse plusieurs portes de validation.** `release.run`, `prepare_release.build_candidate`, `publish_prepared` et `final_checks` relisent, compilent et contrôlent successivement les données. Le contrôle final du projet inclut également des ensembles tels que le Panorama As Is, sans rapport direct avec une simple publication du modèle.
3. **La préparation reste une duplication coûteuse.** Même à chaud, figer puis publier prend 23,89 s. Les snapshots, copies de fragments et sérialisations contrôlées dominent alors le parcours. Accélérer seulement le parsing ne suffit plus.
4. **Le contexte d'accord est trop large et hétérogène.** La capture d'intention prend en compte le glossaire et les principes globaux ; la reprise des accords publiés suit notamment les termes référencés et écarte certaines métadonnées marché. Unifier ces critères autour des dépendances significatives éviterait des réexamens éditoriaux inutiles. Un changement de sens doit toujours suspendre la portée concernée.
5. **Atlas dépend des dossiers physiques de toutes les versions.** `release_catalog` et `app/atlas_data.py` attendent les snapshots du catalogue dans l'arbre courant. Cette dépendance doit être remplacée avant leur retrait.
6. **Les tests et instructions entretiennent l'ancien contrat.** Des tests de préparation utilisent des publications de production et un manifeste sous `modeles/staging/2026-09-13.4`, pourtant ignoré par Git. Les règles de fragments immuables et de rejeu historique imposent aussi le coût actuel. La refonte doit remplacer ces dépendances par de petites fixtures et réécrire les règles actives, plutôt qu'ajouter une nouvelle exception.

## Architecture proposée

| Responsabilité | Conservation cible |
| --- | --- |
| Modèle, glossaires, connaissances marché | Sources courantes suivies dans Git |
| Accords métier | État courant compact : cible, champs, portée, valeurs ou empreintes, auteur/date/source explicite |
| Évolutions des accords et anciennes réflexions | Historique Git ; conserver dans les connaissances seulement les raisons encore utiles |
| Publication courante | Un artefact autonome, produit une fois et activé après contrôle |
| Publications anciennes | Petit catalogue : version, commit exact, chemin et empreinte ; lecture Git à la demande |
| Staging, caches, traces détaillées | Temporaires, ignorés, avec rétention bornée |
| Comparaisons détaillées | Calcul à la demande, sans `changes.json` cumulatif |

**Git conserve les états ; il ne donne pas l'accord métier.** Un commit ou un tag ne valide pas implicitement tous les champs. Il faut garder les accords explicites et leurs limites, sans recopier à chaque release tous leurs états antérieurs. Un accord inchangé conserve son identité ; les nouvelles valeurs restent non approuvées tant qu'elles ne sont pas validées.

Parcours cible : identifier l'état source exact → compiler une fois → contrôler une fois le candidat et les accords concernés → activer atomiquement → vérifier version et disponibilité. Les empreintes doivent couvrir sources, code et dépendances du contrôle. Un état modifié après validation est refusé. L'audit historique exhaustif devient une opération distincte.

Une publication devrait référencer un état source committé ; une prévisualisation peut accepter un espace de travail modifié. Le contrat entre release et commit doit être décidé explicitement : la refonte ne doit pas introduire silencieusement un commit automatique dans une opération actuellement distincte.

Pour Atlas historique, charger ensemble modèle, glossaire et guide de la même version, avec cache local borné. Un déploiement sans `.git` reçoit un artefact courant autonome ; l'accès aux anciennes versions nécessite un accès au dépôt ou des exports sélectionnés.

Objectifs proposés à vérifier, pas performances acquises : publication ordinaire **<10 s à chaud, <30 s à froid** à volumétrie actuelle ; aucune validation courante proportionnelle au nombre de publications ; viser **<20 Mo de données courantes** hors dépendances et historique Git, après qualification des fichiers réellement utiles.

## Branche ou nouveau dépôt ?

| Option | Évaluation |
| --- | --- |
| Branche normale dans le dépôt actuel | **Recommandée** : refonte isolée, comparaison et retour arrière simples ; `main` reste utilisable |
| Clone ou duplication de `origin` | Recopie également l'historique ; ne simplifie ni code ni workflow |
| Branche orpheline | Nouvelle ascendance, mais migration et continuité documentaire plus délicates ; bénéfice limité pour ce problème |
| Nouveau dépôt | À réserver à une rupture volontaire de produit ou de gouvernance ; impose de maintenir l'accès à l'archive |

`origin` est le nom local du dépôt distant. Une branche normale permet déjà un arbre courant très allégé. Retirer des fichiers de cet arbre ne retire pas les blobs des anciens commits : le gain de checkout et le gain de stockage Git sont deux sujets distincts. Aucune réécriture de l'historique distant n'est nécessaire pour accélérer l'application.

Références Git officielles : [branches et branche orpheline](https://git-scm.com/docs/git-switch), [clonage](https://git-scm.com/docs/git-clone), [lecture d'un objet historique](https://git-scm.com/docs/git-show), [tags](https://git-scm.com/docs/git-tag), [conservation et nettoyage des objets](https://git-scm.com/docs/git-gc). Un tag peut être déplacé : le catalogue doit aussi fixer le commit exact, avec une règle de non-réécriture des versions publiées.

## Migration proposée

1. Référencer les 22 publications existantes par commit, chemin et empreinte. Elles sont déjà présentes dans Git à HEAD ; ne pas inventer un commit source historique pour chacune.
2. Introduire le lecteur Git des anciennes publications et un format d'accords courants compact, avec un adaptateur minimal des anciens formats.
3. Reconstruire le parcours unique de publication et ses tests : équivalence de v020, portée des accords, refus d'une source modifiée, activation et retour arrière, cohérence du glossaire historique.
4. Retirer de l'arbre de la branche les copies historiques devenues inutiles, les anciens workflows et leurs tests dépendants de la production. Actualiser ensemble AGENTS.md, README et skill release. Les anciennes règles et preuves restent accessibles dans Git.
5. Rejouer les mêmes scénarios de performance puis comparer avant bascule vers `main`.

L’audit initial était en lecture seule. La refonte autorisée ensuite est résumée ci-dessous ; ses traces techniques restent ignorées sous `.runtime/`.

## Refonte mise en œuvre

Branche `codex/refonte-publication-legere`, issue de `66b4d7a`. Aucun commit ni push implicite, aucune nouvelle release métier.

- Arbre actif : **549,3 → 29,5 Mo**, soit environ **−94,6 %**. Les anciens fichiers restent dans Git ; la taille des packs Git n’est pas réduite par ce retrait.
- **340,6 Mo** de préparations locales obsolètes supprimés ; elles correspondaient toutes à des versions déjà publiées.
- Les **22 versions** du catalogue sont lisibles avec contrôle des empreintes. Atlas sert v020 et la lecture HTTP de v019 a également été vérifiée.
- Modèle de travail, deux glossaires, snapshot publié, snapshot source et décisions v020 : octets comparés à HEAD et inchangés. Les **211 accords publiés** sont conservés. Seules les métadonnées de stockage du manifeste évoluent.
- Le registre courant ne contient que les intentions en attente : **0** après migration. Les captures consommées et leurs suspensions restent dans Git ; elles ne sont plus relues à chaque publication.
- Nouveau parcours dans `lean_release.py` : une construction et une validation du candidat, staging temporaire, vérification des sources, du code, de la base approuvée et des artefacts avant activation. Un report éditorial conserve l’identifiant et la note de l’accord. Pas de `changes.json` permanent, de copie du registre, de journal narratif ni d’audit global de fin de publication.
- Avant retrait, les octets de la version précédente doivent exister dans Git. Une préparation modifiée est refusée. Les anciennes preuves déjà retirées conservent leur référence d’origine lorsque la version courante est archivée à son tour.
- AGENTS.md, README et skill release révisés ensemble ; copie personnelle du skill synchronisée après vérification de son identité.

Le lecteur YAML utilise désormais LibYAML lorsqu’il est disponible, avec refus explicite des alias, des doublons et des types hors contrat. Le lecteur Python reste disponible. Le runtime local a été remis en cohérence avec les interpréteurs 3.12 et 3.14, sans changer la version épinglée **PyYAML 6.0.3**. Les distributions binaires correspondantes sont fournies par [le projet sur PyPI](https://pypi.org/project/PyYAML/6.0.3/). Les fichiers YAML existants ne sont pas normalisés.

Mesure du parcours complet sur copie isolée, changement éditorial, cache de parsing vide puis rempli, contrôle HTTP exclu : **19,14 s à froid et 15,19 s à chaud**, contre 104,06 s et 40,18 s avant refonte. Une observation par cas ; l’objectif proposé de 10 s à chaud reste non atteint. La suppression des copies historiques et l’accélération YAML contribuent au résultat ; ces mesures ne permettent pas d’isoler leur contribution respective.

Validation : 109 tests des contrats et des parcours passés ; 16 tests rejoués avec le lecteur natif passés ; 22 tests Atlas passés dont 2 ignorés, et 18 tests du guide passés dont 1 ignoré. Le contrôle global du modèle ne signale aucune erreur. Les 8 tests finaux du parcours léger passent, y compris la modification de la base approuvée et la préservation des preuves déjà archivées ; les 4 tests de lecture ciblée passent également.

Les anciennes fonctions de publication restent couvertes par leurs tests de compatibilité, mais sont refusées sur le dépôt migré : le seul point d’entrée courant est `release.py`. L’audit U431 clos se lit désormais dans Git ; son rejeu nécessite un checkout historique isolé et ne fait pas partie des contrôles ordinaires.

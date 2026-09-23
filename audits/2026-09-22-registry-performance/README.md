# Coût d’enregistrement des accords — 22 septembre 2026

Refactoring technique autorisé par Laurent, sans modification d’accord réel ni publication.

## Mesures

Registre mesuré : 41 777 489 octets, 69 intentions. Avant refactoring, les étapes isolées prennent 43,217 s pour la lecture YAML, 0,314 s pour le contrôle d’intégrité et 75,044 s pour la sérialisation avec relecture. Ce total d’environ 118,6 s ne mesure pas un enregistrement complet.

Après refactoring, sur une copie isolée : premier ajout sans cache 58,938 s ; ajouts suivants 4,975 s et 3,467 s ; répétition idempotente 1,089 s. La lecture indépendante du résultat prend 64,978 s. Des tests de publication tournaient en parallèle : ces mesures ne constituent pas un benchmark matériel strictement comparable.

Le script `scripts/benchmark_record_decision.py` reproduit la mesure avec des accords synthétiques dans une copie temporaire. Il vérifie les valeurs historiques, les suspensions, les octets conservés et les empreintes des fichiers réels avant de supprimer sa copie. Le rapport local est `.runtime/decision-benchmark/latest.json`.

## Changement réalisé

Le parseur détermine la position d’ajout dans la séquence YAML. Seules les nouvelles entrées sont sérialisées ; les anciens octets et les suspensions sont conservés. Un cache jetable lié aux octets et au code mémorise la lecture et cette position. Les autres dispositions YAML conservent le parcours complet avec contrôle aller-retour. Les empreintes des accords restent contrôlées à chaque enregistrement.

Un verrou système protège les écritures concurrentes et se libère à la fin du processus. Le remplacement demeure atomique avec détection d’une modification externe. Aucun contrat d’accord ou de publication n’est assoupli.

Validation : 43 tests de lecture, cache et enregistrement ; 77 tests de reprise, réexamen, préparation et publication. Tous réussis. La mesure indépendante confirme la conservation des valeurs et octets historiques ainsi que l’absence de changement des fichiers réels.

## Découpage et archivage proposés

Le descripteur courant désigné par `modeles/release/index.json` est `urbanisation-v019-2026-09-22-074501.yaml`, version `2026-09-22.4`. Son registre figé contient 64 des 69 intentions courantes. Elles représentent 91,8 % du volume des entrées mesuré par sérialisation JSON comparable ; ce pourcentage n’est pas une mesure exacte des octets YAML. Cinq intentions sont nouvelles. Le registre courant comporte 14 suspensions.

Être présent dans le snapshot ne signifie pas être un accord adopté : les annexes figées conservent aussi des éléments suspendus. La compilation vérifie la présence et l’identité des intentions et suspensions consommées afin d’empêcher une réactivation ou réécriture historique. Supprimer simplement ces entrées du registre courant ferait échouer ce contrat.

Évolution recommandée, non réalisée par ce premier refactoring : séparer les nouvelles intentions en petits fichiers immuables, maintenir un index léger et référencer les registres historiques déjà figés. Un lecteur de registre logique devra réunir ces références, contrôler identifiants et empreintes et préserver les liens de remplacement et de suspension. Les contrôles complets resteraient obligatoires lors de la publication. La migration devra couvrir la capture des annexes, leur relecture et la compatibilité avec les publications existantes, dont les octets resteront inchangés.

Cette évolution traiterait le coût de lecture à froid que l’ajout incrémental ne résout pas. Aucun archivage ni découpage physique n’a été effectué ici.

## Découpage réalisé après autorisation

Laurent a ensuite demandé de terminer cette optimisation. Le registre de 41 777 489 octets (SHA-256 `00e2466f662366258b32329d35bcf458ec8b8cd94c6c5931c204fd6e5cc702f5`) a été remplacé par un index YAML de 29 304 octets et 69 fragments immuables : 64 sous `archive/`, 5 sous `active/`. L’archive conserve les captures déjà figées, sans déduire une adoption ni changer les 14 suspensions. Les portions YAML de chaque intention sont extraites à leurs positions de parseur et conservées sans resérialisation ; le registre reconstitué est comparé intégralement à l’original avant la bascule atomique. Aucune publication existante n’est modifiée.

La commande d’ajout vérifie les empreintes de tous les fragments mais ne parse que les accords directement concernés. Les fichiers sont adressés par leur contenu ; le verrou protège le lot et l’index est remplacé après les écritures. Un fragment laissé par une interruption reste sans effet tant qu’il n’est pas référencé. Le lecteur complet vérifie en plus les résumés, valeurs et contextes ; la publication l’utilise, fige les fragments référencés avec leur arborescence et conserve la vérification des historiques consommés. Les fragments non référencés ne sont pas publiés. Les registres monolithiques historiques restent compatibles.

Tests : 49 tests de registre, sérialisation et cache ; 78 tests de préparation, publication, reprise et réexamen, tous réussis. Le cas de publication du registre découpé est rejoué après l’ajout du contrôle des fragments non référencés. Il vérifie une publication puis la préparation suivante, ainsi que l’indépendance des preuves figées après corruption du fragment de travail. Validation générale : zéro erreur.

Mesure finale sur copie isolée avec cache vide : premier ajout 5,092 s, suivants 1,539 s et 1,582 s, répétition idempotente 0,948 s. La relecture YAML indépendante complète prend 48,461 s et confirme l’identité des valeurs historiques ; les fichiers réels restent inchangés par le benchmark. Le découpage accélère les opérations courantes, sans supprimer le coût des contrôles exhaustifs de publication.

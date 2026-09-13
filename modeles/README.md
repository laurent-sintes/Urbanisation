# Modèles structurés

**Fonctionnement courant U117–U123 :** [index.json](release/index.json) désigne un descripteur `urbanisation-vNNN-YYYY-MM-DD-HHMMSS.json`, qui porte version, horodatages UTC, chemin et empreinte du modèle et de sa note de release. Chaque élément et le modèle global ont une révision entière automatique et `last_modified`. Atlas consulte uniquement ces publications, avec sélection des versions ; le backlog reste l’espace de construction. Les descriptions du refactoring initial ci-dessous sont historiques lorsqu’elles mentionnent `current.json`.

État au 13 septembre 2026, après U106–U111. Les fichiers JSON portent le modèle ; les Markdown conservent les récits, les analyses, les décisions argumentées et les restitutions. La règle complète de maintenance est dans [AGENTS.md](../AGENTS.md).

## Trois espaces

| Espace | Rôle | Entrée faisant autorité |
| --- | --- | --- |
| `backlog` | Modèle en réflexion, alternatives, illustrations et points à instruire | [backlog/model.json](backlog/model.json) |
| `release` | Dernière version publiée, avec le statut de validation de chaque élément | [release/index.json](release/index.json) |
| `panorama-as-is` | Connaissance de l’existant des trois SI ; distincte de la cible | [panorama-as-is/current.json](panorama-as-is/current.json) |

**Publication et validation sont distinctes.** Conformément à U111, la [release 2026-09-13.2](release/2026-09-13.2/model.json) contient les **36 capacités**, dont **9 validées**, **8 portant des validations partielles** et **19 sans validation individuelle enregistrée**. Parmi les 27 dernières, 12 sont en réexamen, dont Reservation qui conserve un nom adopté. Les statuts affichés sont 9 validées, 7 partiellement validées, 8 non validées et 12 en réexamen. Les validations partielles portent parfois sur le nom seul ou sur le principe d’ingestion. Elles ne valident pas automatiquement la définition, la finalité ou le rattachement.

La première extraction restreinte, `2026-09-13.1`, est conservée comme historique. Elle n’est plus désignée par `current.json`. Le backlog et la release peuvent contenir les mêmes identifiants : ce sont des états de travail et de publication du même modèle, pas deux catalogues à enrichir séparément.

**Évolution U116 :** le backlog `2026-09-13.3` utilise les cinq capacités D01 de P82 et contient 35 capacités au total. Inventory Tracking (`D01.e`) regroupe D01.a/D01.b ; Inventory Visibility conserve D01.c à la révision 2. Les autres domaines sont inchangés. La release `.2` reste à 36 capacités jusqu’à une nouvelle publication demandée. Les repères historiques ne sont pas réutilisés. Voir [l’audit Atlas D01](../audits/2026-09-13-atlas-d01.md).

## Organisation physique

```text
modeles/
  backlog/
    model.json                         # graphe de travail et alternatives
    legacy-capabilities.json           # 36 CAP historiques, distinctes de P81
    panorama-candidates.json            # besoins, cible ou mentions non instruits
    modeling-roadmap.json                # extensions prévues, sans les instancier
    applicability.json                  # épreuve distincte pour les quatre contextes
  staging/<version>/                    # candidat et rapport contrôlables, non publiés
  release/
    current.json                       # version locale publiée et empreinte
    <version>/model.json
    <version>/manifest.json             # liens et empreintes des entrées gelées
    <version>/changes.json              # bilan des nouvelles publications
  panorama-as-is/
    current.json
    shared-2026-09-13.1.json             # contexte commun, notamment C-Log
    beaumanoir-historique/versions/<version>/panorama.json
    boardriders/versions/<version>/panorama.json
    sarenza/versions/<version>/panorama.json
  revisions/<version>/backlog.json      # état de travail gelé pour publication
  decisions/<version>.json              # portées de validation et preuves
  provenance/source-records.json        # index courant des sources capturées
  provenance/<version>/source-records.json
  schemas/
    urbanism.schema.json
    decisions.schema.json
    panorama.schema.json
    panorama-record.schema.json
```

Les trois dossiers du panorama sont des périmètres SI. Le fichier partagé ne constitue pas un quatrième SI. La date de version exprime une consolidation de connaissance : elle ne prouve pas une observation récente de l’installation.

## Structure du modèle

Le graphe distingue `domain`, `reference`, `group`, `capability`, `object`, `document` et `event`. Le champ `layer` distingue `transactional` et `process`. Le cycle de publication est porté par `space`, indépendamment de la couche métier.

Chaque nœud a un identifiant stable, une révision, des champs de contenu, un statut et des sources. `fields` contient notamment `name`, `definition`, `finality` et, quand elles sont établies, `nature`, `scope`, `independence` ou `mastership`. Une valeur absente reste inconnue ; la vue ne la complète pas depuis un autre espace.

Les relations ont également leur identifiant, leur type, leurs extrémités et leur statut. `contains` décrit la décomposition et `presents` un groupe de présentation. Les autres liens décrivent des relations métier, sans convertir automatiquement objets, documents ou événements en sous-capacités. Les préfixes historiques ne déterminent jamais les parents : D02.b et D02.c sont rattachées à D01 ; D02.e à D03.

La hiérarchie peut être approfondie, mais un nouveau niveau ou une nouvelle relation doit avoir un sens défini. Étendre le schéma et les règles de graphe avant d’ajouter un nouveau type. Cette souplesse technique ne valide ni un niveau universel, ni des bounded contexts, ni un modèle processus détaillé.

## Statuts et décisions

| Valeur JSON | Présentation française | Sens |
| --- | --- | --- |
| `accepted` | Validé | Portée présentée explicitement adoptée ; ses limites restent applicables |
| `partial` | Partiellement validé | Certains aspects seulement sont adoptés, ou l’accord est contextuel |
| `proposed` | Non validé en release ; proposé en backlog | Contenu disponible à discuter, sans validation enregistrée |
| `under_review` | En réexamen | Dernier état conservé avec une réserve explicite à instruire |
| `illustration` | Illustration | Exemple pédagogique, conservé dans le backlog |

Dans la release complète, `approved_fields` et `proposed_fields` qualifient séparément les champs d’un nœud. `adoption_ids` renvoie aux décisions `ADOPT-*`, qui transcrivent les accords existants avec auteur, date, source, interprétation explicite ou contextuelle, cible, révision et empreinte de chaque valeur adoptée. Ces repères techniques n’ajoutent aucune nouvelle validation métier. La validation d’un nom ne s’étend pas aux autres champs.

Les rattachements sont qualifiés séparément. Reservation conserve notamment le dernier rattachement U75 avec le réexamen U78 ; son nom adopté ne ferme pas cette question de frontière. Le groupe Business References reste un groupe de présentation de cinq modèles distincts. Les neuf capacités d’Order Promising sont validées dans la portée U95 ; aucune autorité logistique supplémentaire n’est attribuée par cette validation.

Le backlog conserve les alternatives P82 et P84 dans `alternatives`. Elles ne remplacent pas silencieusement les 36 fiches publiées. Les quatre objets, document et fait illustratifs sont conservés avec leurs huit relations, sans promotion par la migration.

## Panorama des SI actuels

Les données distinguent composants et mentions (`objects`), flux (`flows`), autorités sur l’information (`information_authorities`) et responsabilités de décision (`decision_responsibilities`). Chaque fiche conserve son texte source, ses champs d’origine, ses sources et corrections, sa qualification de preuve et son intention As Is ou cible.

Les 85 repères des registres initiaux sont affectés une seule fois : 74 dans les panoramas et leur contexte partagé, 11 dans les éléments à instruire du backlog. Les besoins exprimés pour Boardriders et les orientations de plateforme ne deviennent pas des preuves de configuration installée.

Sarenza est `not_assessed`, avec des listes vides. Cela signifie « non traité », et non « aucun composant ». Les anciennes mentions demeurent traçables dans le backlog. Les dates `observed_at` sont nulles tant qu’aucune observation datée n’est établie. Les extrémités de flux non résolues conservent leur libellé source ; aucun rapprochement d’identité n’est inventé.

## Faire évoluer les modèles

Selon U113, l’exploration et la construction se font **dans le backlog par défaut**, y compris dans FLOW Atlas. La publication reste une action distincte pilotée par le skill `release`. Une comparaison seule n’active aucune version.

U112 fixe la priorité : **domaines et capacités**, puis leur épreuve sur les trois SI et FLOW cible. U141 structure désormais **Supply** et **Case** comme univers dans le backlog : groupes `group_role: urbanism_level`, `level_ref: universe`. Les domaines transactionnels et Business References sont rattachés à Supply ; Case réserve l’exploration processus. Business References reste un groupe de présentation. La [feuille de route](backlog/modeling-roadmap.json) prépare le lien Case/Order sans instancier leur inventaire détaillé ou leurs cardinalités. L’état avant cette refonte est conservé dans [history/pre-U141.json](backlog/history/pre-U141.json).

Les relations peuvent porter `qualification` : sens (`meaning`), rôle, conditions, effets et périmètre. Le type générique `relates-to` permet capacité → capacité/objet/document/événement avec un sens explicite. Les sources et le statut appartiennent au lien lui-même. Cela prépare la structure ; aucun nouveau lien métier réel n’a été ajouté. Une relation entre capacités n’est pas automatiquement une décomposition ; un objet peut concerner plusieurs capacités sans propriétaire exclusif présumé.

Le [registre d’applicabilité](backlog/applicability.json) prépare quatre contextes, trois `as_is` et FLOW `target`. Il conserve séparément applicabilité, couverture décrite et responsabilité de réalisation. Les évaluations futures référencent l’espace, la version et l’identifiant du domaine ou de la capacité, leurs preuves et réalisations lorsqu’elles sont connues. Le tableau est vide à ce stade : absence de résultat signifie non évalué. Les récits déjà analysés restent disponibles et leur qualification structurée reste à faire. Les schémas associés sont contrôlés avec les autres modèles.

1. Lire les corrections, le JSON concerné et ses sources. Enregistrer d’abord tout nouvel apport de Laurent ; distinguer proposition et validation.
2. Modifier le backlog JSON, conserver les identifiants et incrémenter la révision des éléments modifiés. Actualiser les liens marché ou signaler leur comparaison restant à faire dans les sources associées. Consigner l’analyse en Markdown.
3. Pour une publication, figer une nouvelle révision JSON dans `revisions/`, les décisions applicables dans `decisions/` et les preuves dans `provenance/`. Une modification d’un champ adopté ne réutilise pas automatiquement la validation de sa valeur antérieure. Les décisions doivent cibler les révisions et empreintes réellement publiées.
4. Utiliser le [skill release](../skills/release/SKILL.md) et [prepare_release.py](../scripts/prepare_release.py) pour comparer le backlog vivant, préparer le candidat et publier sa capture contrôlée. La préparation écrit seulement `modeles/staging/<version>/`. La publication refuse une entrée altérée ou un contexte modifié depuis la préparation, puis active le pointeur local en dernier. Les décisions sont conservées automatiquement à identité, révision et valeurs identiques ; une reprise sur une autre révision exige une réévaluation explicite. Le rapport distingue les validations suspendues et conserve leur historique.
5. Exécuter les contrôles, actualiser les restitutions et le journal. Publier un contenu candidat ne constitue jamais une validation métier. Une publication externe reste une action différente de cette publication locale.

Commande employée pour la publication complète initiale, conservée comme exemple **à ne pas rejouer avec cette version déjà créée** :

```powershell
python scripts/publish_release.py --from-manifest modeles/release/2026-09-13.1/manifest.json --version 2026-09-13.2 --source U111 --activate
```

Cet ancien appel republie une capture historique ; il n’intègre pas le backlog vivant. Pour le travail courant, employer `python scripts/prepare_release.py report`, puis `prepare --version VERSION --source SOURCE`, et `publish --version VERSION --activate`. La source doit autoriser cette publication, et non seulement la création du skill. Une nouvelle publication requiert une nouvelle version et des entrées gelées cohérentes. Les scripts ne fabriquent pas les validations métier. Les enveloppes versionnées et leurs sources gelées ne sont jamais éditées sur place ; seules les entrées courantes et les pointeurs évoluent. Le suivi Git a été ajouté après le refactoring, selon U114, avec le dépôt distant Urbanisation. Les captures figées restent des preuves distinctes des commits ; leur publication GitHub nécessite un push. `.gitattributes` préserve les octets utilisés pour leurs empreintes.

Pour le panorama, enrichir les données structurées à partir de nouvelles preuves, puis créer une nouvelle version par SI et réviser l’index. Une nouvelle date de consolidation ne doit pas avancer artificiellement `observed_at`. Le fichier partagé reste lui aussi versionné.

## Migration initiale et contrôles

[migrate_urbanism.py](../scripts/migrate_urbanism.py) et [extract_panorama.py](../scripts/extract_panorama.py) sont les extracteurs de migration. Ils ne constituent pas le circuit d’édition courant. Après changement des sources historiques, ne pas réimporter le Markdown sur le JSON vivant. Le premier script exige une destination vierge ; le second refuse l’écrasement différent d’une version gelée. `--check` vérifie la concordance de la capture historique, pas la présence de nouvelles connaissances.

```powershell
python scripts/refresh_sources.py
python scripts/validate_models.py
python -m unittest discover -s scripts -p "test_*.py"
python scripts/extract_panorama.py --check
python scripts/render_models.py
```

Les schémas utilisent un sous-ensemble explicite de [JSON Schema 2020-12](https://json-schema.org/draft/2020-12). Les enveloppes sont fermées avec `additionalProperties: false`, suivant la [définition officielle des objets](https://json-schema.org/understanding-json-schema/reference/object). Le validateur local de bibliothèque standard n’implémente pas tout JSON Schema : il refuse les mots-clés non pris en charge. Les règles complémentaires vérifient identités, sources, types de relations, cycles, empreintes, publications gelées et portée des validations. Les index de pointeurs sont contrôlés sémantiquement ; tous les JSON annexes n’ont pas encore un schéma autonome.

[FLOW Atlas](../app/README.md) est une restitution en lecture seule des trois espaces. Le Markdown des [restitutions](../restitutions/README.md) est généré depuis les JSON. Les analyses de marché MKT/ELM/CMP, le glossaire, les récits et les questions restent dans leurs registres documentaires avec leurs identifiants ; leur indexation comme sources ne vaut pas migration complète en graphe. Les 36 CAP historiques restent distinctes des 36 capacités P81.

Voir l’[audit de structure et d’extraction](../audits/2026-09-13-structure-modeles.md) pour les constats, les limites et les preuves.


## Cycle de vie — U131

Les nœuds et relations du backlog portent `lifecycle` : `ai_proposed` (Proposé par l’IA), `under_instruction` (En cours d’instruction), `urbanist_validated` (Validé par l’urbaniste). Sources, date d’enregistrement, champs validés et empreintes qualifient la portée. Une validation limitée au nom ne valide pas la définition. Les décisions ADOPT et `review` restent les preuves techniques détaillées ; publication et cycle sont indépendants.

`lifecycle_policy: 1` rend ce champ obligatoire pour chaque nœud et relation du modèle courant. Une empreinte périmée ou une validation sans portée bloque le contrôle. Les modèles historiques sans cette politique restent compatibles.

Les modèles historiques sans lifecycle restent lisibles. L’introduction initiale de ce champ conserve les accords sur les contenus strictement inchangés, avec des décisions de transcription traçables lors de la prochaine préparation. Les illustrations ne sont pas rendues publiables par leur cycle. Les principes de fonctionnement et les données As Is conservent leurs contrats distincts.

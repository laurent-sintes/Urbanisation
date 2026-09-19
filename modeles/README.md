# Modèles structurés

**Publication U473 : v013 / `2026-09-19.6`.** Retours de revue U470–U472 publiés : univers Supply expliqué concrètement, périmètre d’orchestration et projections externes explicités, 47 fiches enrichies en références marché, Business Services retiré. Les 47 capacités, 76 comportements et 338 relations sont conservés. Le catalogue d’informations reste préservé en interne et masqué dans Atlas ; son extension reste en attente. Bandeau fixe et barre haute compacte disponibles. [Rapport](../audits/2026-09-19-release-U473/rapport.md) ; [note figée](release/2026-09-19.6/release-notes.md).

**Retrait U472 publié dans v013 :** Business Services est retiré, ainsi que son terme TER067 ; Supply Chain Orchestration reste le seul univers instancié. Aucun domaine, capacité ou lien n’était rattaché à cet univers vide. Le commerce est différé après la Supply Chain. V012 et son historique restent inchangés. [Rapport du retrait](../audits/2026-09-19-business-services-U472/rapport.md).

## Informations métier — contrat U468

Le catalogue courant réside dans [`backlog/model.yaml`](backlog/model.yaml), propriété `information_catalog` : 14 informations issues des cinq pilotes, 21 usages explicites par les capacités et 15 liens qualifiés. L’annexe [`information-cards-U465.yaml`](backlog/information-cards-U465.yaml) conserve le pilote et ses preuves ; elle n’est plus la source du catalogue courant.

Chaque information décrit une question métier, une définition, un contexte, les éléments essentiels à son sens, une justification de maille, des limites, des exemples et des références marché. Ce contrat organise une cartographie conceptuelle, sans définir de tables, d’API ni de schéma logiciel implémentable. Les rôles rattachent les informations à des capacités existantes ; les liens entre informations expriment un sens, une condition et un effet. Ils ne créent aucun niveau dans l’arbre ni aucun flux technique implicite.

La collection est facultative pour préserver les anciennes publications. Le schéma et les contrôles interdisent les identités dupliquées, les capacités absentes ou exclues et les liens orphelins. La préparation fige le catalogue dans le snapshot, lui attribue des révisions et empreintes, puis publie exactement ce contenu. Les différences et notes de publication recensent les ajouts, modifications et retraits. Une publication ancienne sans catalogue reste sans catalogue ; Atlas ne consulte pas l’annexe pilote.

Les fiches et liens conservent leurs qualifications internes proposées ; U466 porte uniquement sur la distinction et la coexistence proposition/engagement. Ce premier contrat n’ajoute pas de circuit d’adoption implicite des fiches. Autorités locales, versions, confirmations et règles de libération ne sont pas déduites des exemples.

L’intégration U468 est publiée dans **v012** par U469 ; v011 reste inchangée. Le catalogue est conservé sans enrichissement dans v013, avec sa consultation masquée dans Atlas à la demande U470. [Rapport d’implémentation et recette isolée](../audits/2026-09-19-informations-atlas-U468/rapport.md).

## Publications et jalons antérieurs

**Publication U467 : v011 / `2026-09-19.4`.** Retrait des couches métier, définition Supply corrigée, exemples et choix marché enrichis, glossaire métier de 111 termes. L’édition méthodologique `2026-09-19.2` est explicitement associée à v011 : six repères et Information (MOD012), avec l’exemple proposition/engagement U466. Les quatorze fiches pilotes U465 sont figées comme contexte, sans devenir des nœuds consultables. Les 47 capacités et 76 comportements, leurs parents et les accords à valeurs inchangées sont conservés. [Note figée](release/2026-09-19.4/release-notes.md) ; [rapport et contrôles](../audits/2026-09-19-release-U467/rapport.md). L’index désigne la publication courante ; les paragraphes suivants conservent leur contexte historique.

**Publication U452 : v010 / `2026-09-19.3`.** Les 47 capacités et 76 comportements sont typés dans Atlas. Les dix compléments U449 et les 76 formes U451 sont publiés, avec leurs qualifications proposées conservées. L’édition méthodologique `2026-09-19.1` reste accessible par une association explicite à v010 : six repères et deux glossaires distincts. Noms, définitions, rattachements et anciens snapshots préservés. [Note de release](release/2026-09-19.3/release-notes.md) ; [rapport et vérifications](../audits/2026-09-19-release-U452/rapport.md). L’index reste l’autorité de la publication courante ; les mentions de versions antérieures ci-dessous sont historiques.

**Typage U449 :** 37 valeurs préservées, dix compléments proposés. Icônes par type et décisions en fin de liste, avec séparation visuelle dans Atlas. L’interface utilise les types de la publication sélectionnée, avec une icône spécifique pour les capacités contenues par les référentiels. [Grille](backlog/capability-types-U449.yaml) ; [rapport initial](../audits/2026-09-19-capability-types-U449/rapport.md).

**D03/D15 — U438–U446 :** Fulfillment Optimization et Order Promising sont deux domaines frères sous Supply. Structuring et Archiving sont dans D04 ; Fulfillment Commitment remplace Promise Management (U445). Grouping et Merging sont intégrés comme comportements proposés. [Rapport des modifications](../audits/2026-09-19-d03-U437/modifications.md) ; [portée de l’accord de structure](backlog/d03-domain-review-U437.yaml), [Structuring](backlog/order-structuring-review-U439.yaml) et [engagement / affectation](backlog/promise-assignment-review-U441.yaml).

**Lecture U447 :** référentiels, Order Management, Inventory Management, Process Management, Order Promising, Fulfillment Optimization, Inventory Optimization. [Ordre de présentation](backlog/reading-order-U447.yaml) ; aucune nouvelle hiérarchie.

**Backlog U290 refondu** : Promise Management, mécanismes Protection, trois comportements Planning et convention Supply Assignment à valeur multidimensionnelle. Voir le [bilan de migration](../audits/2026-09-17-refonte-appliquee/rapport.md) et le [registre des identités et questions ouvertes](backlog/refactoring-implementation.yaml). Les publications restent inchangées ; les paragraphes datés ci-dessous conservent leur contexte historique.

## Deux glossaires distincts — U232

- **Glossaire métier** : [backlog/glossary.yaml](backlog/glossary.yaml), vocabulaire des domaines métier, figé dans les publications selon le workflow existant.
- **Glossaire de modélisation** : [backlog/modeling-glossary.yaml](backlog/modeling-glossary.yaml), notions transversales en support à la définition des objets du modèle : Decision, Planning, Management, application transactionnelle. Identifiants MOD distincts ; les portées utilisateur et les formulations proposées sont conservées.

Le second registre est documentaire et séparé : il ne complète pas implicitement le glossaire métier publié ou son résolveur lexical. Les discussions antérieures restent des sources ; les sens courants de ces quatre notions font autorité dans modeling-glossary.yaml. La séparation U232 porte sur les notions discutées U229–U231, sans reclassification globale des notions et verbes historiques.

**Publication U448 : v009 / `2026-09-19.2`.** L’index désigne `urbanisation-v009-2026-09-19-013037.yaml`, puis `2026-09-19.2/model.yaml` : 138 nœuds, six domaines frères, 47 capacités, 76 comportements, 338 relations et 110 termes de glossaire. Référentiels présentés en premier, Order Promising et Fulfillment Optimization séparés, Fulfillment Commitment nommé selon U445 ; Grouping et Merging restent proposés. Accords transcrits à portée constante, anciennes publications préservées et disponibilité Atlas vérifiée. [Note de release](release/2026-09-19.2/release-notes.md) ; [revue des preuves et impacts](../audits/2026-09-19-release-U448/revue.md). L’index reste l’autorité de publication courante ; les mentions de versions courantes ci-dessous sont historiques.

## Format courant — U200/U202

Le backlog vivant et les nouvelles publications du modèle métier sont en **YAML**. L’entrée de travail est `backlog/model.yaml` ; ses annexes courantes sont aussi en YAML. Les captures `legacy-capabilities.json`, `panorama-candidates.json`, `backlog/history/`, les panoramas et les preuves historiques restent dans leur format d’origine. Ne pas créer de copie JSON éditable concurrente.

La prochaine publication produira `<publication>/model.yaml`, un descripteur `urbanisation-vNNN-YYYY-MM-DD-HHMMSS.yaml` et une entrée figée `revisions/<publication>/backlog.yaml`. `index.json`, `manifest.json`, décisions, preuves et rapports restent des métadonnées techniques JSON. Les anciennes releases JSON et leurs empreintes ne sont jamais réécrites. La release active v003 demeure celle publiée avant cette migration.

Le serveur charge YAML/JSON avec `scripts/structured_io.py` puis renvoie du JSON aux API. Aucun modèle parallèle n’est stocké dans Atlas. Les valeurs métier et leurs empreintes canoniques ne dépendent pas de la mise en forme YAML ; l’empreinte du fichier publié reste calculée sur ses octets exacts.

Installer la dépendance locale avec `python -m pip install --target .tools/yaml-runtime -r requirements.txt`. Les dates, identifiants et mots comme `on` restent des chaînes ; seules les valeurs booléennes `true`/`false`, nombres JSON et `null` sont typées implicitement. Les clés dupliquées, alias, objets Python et valeurs hors du contrat JSON sont refusés. Un champ multiligne peut utiliser `|` ; `|-` évite d’ajouter une fin de ligne à sa valeur. Les textes balisés du glossaire restent une proposition de syntaxe distincte du présent refactoring.

[Audit sémantique, corrections et preuves de conversion](../audits/2026-09-14-glossaire-yaml/audit.md). Les descriptions initiales ci-dessous restent historiques pour les formats et versions qu’elles citent.


**Fonctionnement courant U117–U123 :** [index.json](release/index.json) désigne un descripteur `urbanisation-vNNN-YYYY-MM-DD-HHMMSS.json`, qui porte version, horodatages UTC, chemin et empreinte du modèle et de sa note de release. Chaque élément et le modèle global ont une révision entière automatique et `last_modified`. Atlas consulte uniquement ces publications, avec sélection des versions ; le backlog reste l’espace de construction. Les descriptions du refactoring initial ci-dessous sont historiques lorsqu’elles mentionnent `current.json`.

État au 13 septembre 2026, après U106–U111. Les fichiers JSON portent le modèle ; les Markdown conservent les récits, les analyses, les décisions argumentées et les restitutions. La règle complète de maintenance est dans [AGENTS.md](../AGENTS.md).

## Trois espaces

| Espace | Rôle | Entrée faisant autorité |
| --- | --- | --- |
| `backlog` | Modèle en réflexion, alternatives, illustrations et points à instruire | [backlog/model.yaml](backlog/model.yaml) |
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

Le graphe distingue `domain`, `reference`, `group`, `capability`, `behavior`, `object`, `document` et `event`. **U455 retire l’axe métier transactionnel/processus** : univers et domaines coopèrent par des responsabilités et interactions explicites. U458 retire `layer` du backlog courant. Le principe `PRINCIPLE-DOMAIN-INTERACTIONS` interdit sa réintroduction ; les anciens snapshots conservent leurs champs et leur contrôle historique. Le lecteur ne s’en sert plus pour déduire une frontière métier. `space` porte le cycle de publication. Ancien principe, nouveaux principes et impacts : [domain-interactions-U455-U456.yaml](backlog/domain-interactions-U455-U456.yaml).

**U456 : Atlas reste strictement métier.** Structures d’information métier, autorités, documents et faits y ont leur place ; catalogues d’applications/produits logiciels, contrats techniques et liens vers les réalisations restent hors d’Atlas. Les dossiers de solution peuvent citer la référence métier. Cette décision corrige la proposition d’audit ; elle ne réécrit pas les publications ni l’application courante.

Chaque nœud a un identifiant stable, une révision, des champs de contenu, un statut et des sources. `fields` contient notamment `name`, `definition`, `finality` et, quand elles sont établies, `nature`, `scope`, `independence` ou `mastership`. Une valeur absente reste inconnue ; la vue ne la complète pas depuis un autre espace.

Les relations ont également leur identifiant, leur type, leurs extrémités et leur statut. `contains` décrit la décomposition et `presents` un groupe de présentation. Les autres liens décrivent des relations métier, sans convertir automatiquement objets, documents ou événements en sous-capacités. Les préfixes historiques ne déterminent jamais les parents : D02.b et D02.c sont rattachées à D01 ; D02.e à D03.

Une relation peut porter une expression courte dans `fields.label` (ou `fields.verb`), lue de `source_id` vers `target_id`. Cet objet optionnel n’accepte que ces deux chaînes non vides. Le sens complet reste dans `qualification`. Avec le rôle `needs`, la flèche va toujours du consommateur vers le fournisseur du résultat ; le libellé ne change ni cette orientation ni le type du lien. Atlas affiche le libellé commun aux relations regroupées, sinon le libellé de famille et le détail de chaque relation.

Ces champs font partie du contenu révisé et figé de la relation. Leur ajout n’étend pas l’accord sur les extrémités ou la qualification : la portée des preuves de cycle de vie demeure explicite. Leur modification impose une révision et ne peut pas altérer une publication existante.

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

U112 fixe la priorité : **domaines et capacités**, puis leur épreuve sur les trois SI et FLOW cible. U141 structure désormais **Supply** et **Case** comme univers dans le backlog : groupes `group_role: urbanism_level`, `level_ref: universe`. Les domaines transactionnels et Business References sont rattachés à Supply ; Case réserve l’exploration processus. Business References reste un groupe de présentation. La [feuille de route](backlog/modeling-roadmap.yaml) prépare le lien Case/Order sans instancier leur inventaire détaillé ou leurs cardinalités. L’état avant cette refonte est conservé dans [history/pre-U141.json](backlog/history/pre-U141.json).

Les relations peuvent porter `qualification` : sens (`meaning`), rôle, conditions, effets et périmètre. Le type générique `relates-to` permet capacité → capacité/objet/document/événement avec un sens explicite. Les sources et le statut appartiennent au lien lui-même. Cela prépare la structure ; aucun nouveau lien métier réel n’a été ajouté. Une relation entre capacités n’est pas automatiquement une décomposition ; un objet peut concerner plusieurs capacités sans propriétaire exclusif présumé.

**Convention fait–document U461** : lorsqu’un modèle porte `PRINCIPLE-MANAGEMENT-FACT-DOCUMENT`, chaque fait de gestion (`event`) doit être relié à un document identifié par `records` (document → fait). Le document peut être structuré sans fichier. Le validateur vérifie le lien et la nature des extrémités ; il n’impose ni relation un-à-un, ni version, ni règle de correction. Les publications antérieures sans ce principe conservent leur contrat. Les exemples candidats du lot 3 restent dans `backlog/information-pilots-U458.yaml` ; ils ne sont pas promus automatiquement en nœuds.

Le [registre d’applicabilité](backlog/applicability.yaml) prépare quatre contextes, trois `as_is` et FLOW `target`. Il conserve séparément applicabilité, couverture décrite et responsabilité de réalisation. Les évaluations futures référencent l’espace, la version et l’identifiant du domaine ou de la capacité, leurs preuves et réalisations lorsqu’elles sont connues. Le tableau est vide à ce stade : absence de résultat signifie non évalué. Les récits déjà analysés restent disponibles et leur qualification structurée reste à faire. Les schémas associés sont contrôlés avec les autres modèles.

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
# Glossaire publié et références textuelles — U203

Le vocabulaire courant est dans `backlog/glossary.yaml`. Les identifiants TER/VER sont stables ; `name`, `short_description`, `definition`, `review` et `source_refs` sont obligatoires. Les sens homonymes disposent de repères distincts : TER004 est historique ; TER060 décrit Article comme rôle de Product. Le registre Markdown conserve les récits et preuves, sans seconde autorité à maintenir.

Les chaînes peuvent contenir `[unités physiques](glossary:TER059)` ou `[Inventory Tracking](model:D01.f#definition)`. Le texte affiché peut être traduit ou au pluriel. Seul le lien explicite détermine sa cible, dans le même modèle ; le parseur ne crée aucune relation métier. Préfixer un crochet ouvrant par `\` pour conserver un exemple littéral. La notation est indépendante de YAML et reste une chaîne dans l’API JSON.

La préparation embarque le glossaire dans `glossary` du snapshot et du modèle publié ; elle surveille aussi l’empreinte de son fichier de travail. Une release historique sans ce champ reste sans glossaire. Chaque terme et le catalogue sont versionnés automatiquement, avec UTC `last_modified`. `glossary_changes` et `glossary_reference_impacts` du rapport indiquent les différences et les références à un sens modifié, y compris par un autre terme ; examiner leur portée avant publication, sans déduire une validation depuis une phrase inchangée. Les anciens snapshots restent immuables.

Dans Atlas, la fiche de terme propose sa description courte, sa définition et son contexte ; provenance et validations restent internes depuis U450. Les liens `model` ouvrent les éléments de tout type. `#definition`, `#finality` et `#scope` désignent les sections de fiche correspondantes ; Dans le glossaire, `#definition` désigne la définition ; l’ancien lien `#short-description` y est redirigé depuis U459, sans rubrique « En quelques mots » redondante. L’URL Atlas encode séparément la publication, la cible et la section.

U450 sépare les accès au glossaire métier et au glossaire du méta modèle. Le guide méthodologique versionné porte ses termes MOD et la liste des termes TER du snapshot relevant du méta modèle ; les identités et textes TER ne sont pas réécrits. `modeling-guides/index.yaml` associe précisément l’édition à la publication. La préparation capture l’association de la version de départ, puis la publication la reporte explicitement après contrôle des empreintes, sans choix par tri ni repli vers le backlog. Une modification de l’association après préparation exige un nouveau candidat.


## Comportements — U262 à U264

Le type `behavior` précise une capacité et constitue son dernier niveau descriptif. Une unique relation structurelle `contains` le rattache à un parent de type `capability`. U455/U458 retirent le critère de couche du modèle courant. Les contrôles refusent absence/multiplicité de parent, parent d’un autre type, nom/définition vides et enfants sous un comportement. Une relation métier `relates-to` peut relier un comportement à une capacité, un comportement, un objet, un document ou un événement, avec qualification explicite ; elle ne crée pas un parent.

Identités BHV001–BHV004, quatre comportements ATP ; rattachements explicites, aucun parent déduit des identifiants. Le compteur des capacités reste distinct. Définitions U263 adoptées, noms anglais et compléments proposés ; source et portées : connaissance/34-comportements-atp.md et d03-review.yaml. La publication utilise le mécanisme normal de révisions, décisions et snapshots ; cette évolution ne publie pas le backlog.


## Justifier les comportements — U265

Une capacité décomposée porte `fields.decomposition_rationale`, texte expliquant la complexité ou le bénéfice ciblé. Cette propriété fait partie des champs métier versionnés ; sa présence ne la valide pas. `PRINCIPLE-JUSTIFIED-BEHAVIOR` active le contrôle de présence non vide pour les capacités ayant des enfants de type behavior. Les snapshots antérieurs restent lisibles sans cette exigence rétroactive. Le contrôle ne juge pas la pertinence de la justification : elle reste à examiner métier.

Le niveau reste terminal, les comportements combinables et facultatifs. Les propositions d’audit sont dans `backlog/behavior-audit.yaml`, hors catalogue actif ; les 41 fiches ne sont pas 41 demandes de décomposition. Les justifications sont affichées dans les fiches Atlas et la restitution dérivée lorsqu’elles appartiennent au snapshot consulté.


## Audit des comportements manquants après U290

`backlog/behavior-gap-audit.yaml` porte les propositions U292 ; [rapport et annexes](../audits/2026-09-17-comportements-manquants/rapport.md). Les IDs P/A/C sont locaux à l’audit, pas des nœuds du catalogue. Régénérer et contrôler les vues avec `python -m scripts.render_behavior_gap_audit`. Le contrôle exige l’empreinte du modèle audité ; après évolution de celui-ci, réexaminer l’analyse avant d’actualiser la baseline. Aucun candidat n’est adopté automatiquement.


## Comparaison marché structurée — U311

`fields.market_comparisons` porte les rapprochements sur les nœuds ; `market_comparisons` porte les mêmes informations sur les termes du glossaire métier. Contrat commun : `$defs.marketComparisons` dans le schéma d’urbanisme. Une entrée contient éditeur/produit, libellé/nature externe, relation, points communs, différences, position FLOW, statut et source datée. Les statuts proposés ne deviennent pas validés à la publication. Champ facultatif pour les éléments non étudiés ; lorsqu’un rapprochement est documenté, il doit être renseigné. Les anciennes publications restent valides sans ce champ.

U462 ajoute deux précisions facultatives par rapprochement : `term_choice` explique le choix de vocabulaire et les alternatives écartées ; `definition_choice` explique le périmètre retenu. Elles restent rattachées à la source primaire de la comparaison, avec les décisions internes dans `source_refs`. Un nom repris ne présume pas un effet métier identique chez l’éditeur et dans FLOW.

`fields.examples` conserve les illustrations explicitement structurées : titre, situation, résultat éventuel (`outcome`), leçon métier éventuelle (`lesson`) et provenance interne (`source_refs`). Aucune valeur d’accord n’est déduite d’un exemple. Atlas donne priorité à ce champ ; pour une publication antérieure, il peut mettre en valeur les seuls passages déjà marqués comme exemples dans le périmètre de ce même snapshot. Aucun scénario n’est généré depuis une définition ni récupéré dans le backlog.


## Exécution ciblée et performances

Après une modification, utiliser la matrice de contrôles d’[AGENTS.md](../AGENTS.md). Actualiser la provenance seulement si une source indexée a changé ; valider une fois l’état final du modèle. `render_models.py --space backlog`, `--space release` ou `--space panorama-as-is` limite la restitution à l’espace concerné ; sans option, tous les espaces sont traités. Les restitutions identiques ne sont pas réécrites.

`prepare_release.py report` affiche une synthèse avec le nombre d’erreurs et l’aptitude à préparer une release. `--full` imprime tous les détails ; `--output chemin-nouveau.json` enregistre le rapport complet dans un nouveau fichier, sans écraser un fichier existant. Les vérifications et le rapport figé d’une préparation restent complets.

`python -m scripts.render_behavior_gap_audit` réutilise un contrôle réussi uniquement si les empreintes des modèles, historiques, preuves protégées, vues et scripts sont identiques. Le checkpoint local est dans `.runtime/behavior-audit-checkpoint.json`, hors Git. Tout changement, disparition, ajout ou cache invalide impose le rejeu. `--full` force ce rejeu ; `--details` affiche toutes les vérifications. Un échec supprime le checkpoint précédent. Une modification d’entrée pendant le contrôle interdit de mémoriser sa réussite. Ce cache de vérification n’accorde aucune validation métier et n’est jamais utilisé par la publication. Python `-O` est refusé pour conserver les assertions.

Le lecteur YAML rejette les alias pendant l’unique analyse. Son cache en mémoire est borné à 128 entrées et 32 Mio de fichiers sources (les objets Python peuvent occuper davantage). Chaque lecture relit et hache les octets ; taille et date ne suffisent jamais à déclarer un fichier inchangé. Chaque appel reçoit une copie indépendante. Les signatures des publications sont toujours contrôlées.


## Améliorations de lecture U458

Atlas indexe les champs métier et le glossaire du snapshot sélectionné, avec priorité au nom exact et à l’identifiant. U459 corrige le retrait des comparaisons : leurs champs de positionnement métier sont affichés et recherchables. Réserves, statuts et sources internes restent hors affichage et hors index de recherche. Les champs autorisés sont explicites dans `app/src/businessContent.ts` ; cette séparation de présentation n’est pas un contrôle d’accès à l’API locale. Les dépendances directes sont montrées par défaut ; les liens entre voisins se demandent explicitement. Les fiches gardent leurs conditions et effets accessibles dans les détails.

`backlog/modeling-guide-U458.yaml` conserve la source de travail des six repères sans couches métier ni exploration de réalisations. U467 en publie une édition figée `2026-09-19.2`, explicitement associée à v011 ; v010 garde son guide précédent. Les sources de leçons sont embarquées dans le guide ; ses références racines relèvent du registre global. La préparation contrôle cette distinction sans inventer de source globale pour un extrait local. Les cinq cas pilotes sont dans `backlog/information-pilots-U458.yaml`, affinés par `backlog/information-cards-U465.yaml` ; leur suivi et leurs arbitrages restent dans `backlog/v0-readiness.yaml`.


## Pluralité des sources marché — U470/U471

Le champ racine optionnel `market_reference_policy: two_primary_sources` exige au moins deux documents distincts pour chaque nœud non illustratif, relation ou terme comportant des comparaisons. `validate_models.py` et la préparation de publication l’appliquent ; les URL ne deviennent pas distinctes par changement d’ancre ou ajout de paramètres. Les fiches sans comparaison ne reçoivent aucun appui fictif. La qualité primaire et la pertinence sont contrôlées éditorialement. La politique participe à l’empreinte du modèle et laisse les snapshots historiques sans marqueur inchangés.

U470 masque temporairement le catalogue Informations métier dans Atlas sans supprimer ses données du modèle. Aucune extension n’est engagée pendant cette consolidation.

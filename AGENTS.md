# Objectif et fonctionnement

## Publication courante — U204

**14 septembre 2026 : v004**, publication `2026-09-14.1`, descripteur `urbanisation-v004-2026-09-14-145044.yaml`, publiée à `2026-09-14T14:50:44.079623Z`. Elle contient **48 nœuds, 34 capacités, 47 relations et 93 termes de glossaire**. `modeles/release/index.json` pointe vers ce descripteur et `2026-09-14.1/model.yaml` ; les anciennes releases restent immuables et sélectionnables.

Cette publication intègre le retrait D02 sans renumérotation, D03 avec ATP/CTP/PTP, Delivery Schedule Decision et Order Prioritization, Business Services et l’audit de vocabulaire U202. Les nouvelles formulations proposées ne sont pas validées par la publication. Les 53 décisions comprennent 36 reprises identiques et 17 transcriptions documentées : six à portée restreinte sur des valeurs inchangées, onze issues des accords U154/U163/U173. Dix-huit anciennes décisions ne sont plus applicables intégralement sur cette révision et restent dans l’historique ; les six reprises partielles ont de nouveaux identifiants. Les correspondances marché, alternatives et illustrations non intégrées restent du contexte figé.

Le contrôle de statut s’applique aux nœuds de tout type : un univers dont tous les champs sont explicitement adoptés peut être `accepted`. Pour une capacité, nom, définition, finalité et nature restent nécessaires. Les contrôles d’empreinte, d’identité et de portée restent obligatoires. Voir [le bilan v004](audits/2026-09-14-release-v004/bilan.md) et la [note de release](modeles/release/2026-09-14.1/release-notes.md). Atlas sert le modèle YAML et le glossaire en JSON, avec infobulles et navigation vérifiées. Aucun commit ni push inclus.

## Glossaire et liens dans Atlas — U203

**14 septembre 2026 :** Atlas possède une entrée **Glossaire** distincte de l’arbre métier, avec recherche et fiches. Les liens lexicaux explicites affichent une description courte au survol et au focus clavier ; Échap ferme l’infobulle, le clic ouvre la fiche ou sa section dans la même publication. Les liens de rattachement, d’exploration et d’extrémité de relation disposent du même aperçu. Pour un élément sans `short_description`, l’aperçu utilise sa finalité, puis sa définition.

- Autorité du vocabulaire courant : `modeles/backlog/glossary.yaml`. Les tableaux et discussions de `connaissance/19-glossaire-metier.md` restent des sources historiques. La consolidation conserve 81 identifiants TER/VER et ajoute TER057–TER068 ; TER004 conserve son ancien sens, Article comme rôle possède TER060. Les nouvelles formulations restent proposées, sans étendre les validations des échanges aux compléments éditoriaux.
- Texte léger dans les chaînes YAML : `[libellé](glossary:TER059)` ou `[libellé](model:D01.f#definition)`. Identités explicites, pas de reconnaissance automatique des mots. Ce lien lexical ne crée aucune relation de décomposition ou de possession métier. La syntaxe ne permet pas d’insérer du HTML.
- Une préparation de release incorpore et fige le glossaire dans le modèle publié. Catalogue et termes reçoivent `revision`, `last_modified` UTC et empreinte ; le modèle global tient compte du glossaire. Le rapport et la note signalent ses changements et les textes référençant un sens modifié, à réexaminer. Une modification du glossaire après préparation exige une nouvelle préparation.
- Atlas résout exclusivement dans le snapshot consulté. Une ancienne release dépourvue de glossaire l’indique ; aucun repli vers le backlog. La publication courante v003 reste inchangée par U203. Les liens absents sont signalés dans l’interface et refusés lors de la validation du modèle à publier.
- Vérifications : `app/test-glossary.mjs`, `app/verify-glossary.mjs`, `scripts/test_glossary.py` et scénarios isolés de publication. Le [bilan U203](audits/2026-09-14-glossaire-atlas/bilan.md) distingue l’état réel v003 des données de test navigateur.

## Règles courantes YAML et audit de vocabulaire — U200/U202

**Cette section remplace les consignes de format JSON du backlog et des nouvelles releases ci-dessous.** Laurent demande d’abord l’audit du modèle face au glossaire, puis son application, puis le refactoring YAML. Audit et capture avant correction dans `audits/2026-09-14-glossaire-yaml/`. Dix nœuds précisés, 34 capacités conservées ; nouvelles formulations proposées, portées validées inchangées conservées sans extension. D08 distingue Product/Variant, rôles Article/Container et Product Unit ; les principes CTP différé et univers Case sont actualisés.

- Autorité de travail : `modeles/backlog/model.yaml`, annexes courantes `.yaml`. Ne pas recréer un `model.json` concurrent. Les captures `legacy-capabilities.json`, `panorama-candidates.json` et `history/` restent historiques ; le panorama As Is n’est pas migré par cette opération.
- Nouvelles publications : `<publication>/model.yaml`, `revisions/<publication>/backlog.yaml` et descripteur `urbanisation-v<NNN>-<YYYY>-<MM>-<DD>-<HHMMSS>.yaml`. `release/index.json`, manifestes, décisions et preuves conservent leur format technique JSON. Anciennes releases JSON immuables, toujours sélectionnables.
- La conversion YAML conserve exactement les valeurs après l’audit. Les révisions métier utilisent le contenu canonique ; les empreintes des fichiers publiés protègent leurs octets. Un changement de format ne vaut ni modification sémantique ni validation. Le lecteur refuse deux autorités homonymes YAML/JSON.
- Dépendance locale PyYAML épinglée dans `requirements.txt`, installation : `python -m pip install --target .tools/yaml-runtime -r requirements.txt`. Lecture/écriture par `scripts/structured_io.py` ; dates et identifiants restent du texte, clés dupliquées et alias refusés. Aucun chargement d’objets Python depuis YAML.
- Atlas lit le YAML publié ou le JSON historique et renvoie du JSON sur ses API. Il reste exclusivement sur la release. Aucun commit, push ou publication métier implicite dans cet audit/refactoring.
- U202 ne réalisait pas les liens textuels. Leur mise en œuvre ultérieure relève de U203, décrite ci-dessus.

Les chemins `.json` de backlog dans les anciens récits désignent leurs états historiques ; consulter le `.yaml` courant pour travailler. Le guide `modeles/README.md` et les skills `release`/`server-admin` décrivent le fonctionnement actualisé.


## Orientation ergonomique d’Atlas — U132/U133

**Réalisation U152/U153 — 14 septembre 2026 : Atlas utilise React, TypeScript et React Flow avec une interface sur mesure.** L’application courante dans `app/` remplace le frontend JavaScript initial ; l’essai comparatif reste historique. `app/src/model.ts` projette une publication sans changer ses nœuds ni ses relations ; `publication.ts` et `usePublication.ts` assurent le suivi du catalogue et les historiques fixes. L’arbre, les cartes, les fiches et la recherche emploient les SVG Lucide de `app/src/icons.tsx` : correspondances graphiques par nom connu et repli par type, sans nouvelle autorité métier. Objets, documents et événements ont des repères distincts, sans inventaire ajouté. Compiler par `pnpm --dir app build`, puis recharger la page ; Python sert uniquement `app/dist/`, aucun serveur Node permanent. Après clonage, installer les dépendances verrouillées puis compiler. Les publications restent lues à l’exécution depuis l’API, jamais embarquées dans le bundle. Voir [le bilan du refactoring](audits/2026-09-14-refactoring-atlas.md) et `app/README.md`. Aucun historique de visites ; aucune publication métier, aucun commit ni push implicite.

**Choix validé U150 — 14 septembre 2026 : React Flow avec interface sur mesure est retenu pour la suite d’Atlas.** Laurent tranche explicitement après l’essai U146 : « Pas de débat : React Flow / sur mesure est bien meilleur. Je valide ! ». La comparaison de moteurs est close ; LikeC4 n’est plus candidat à l’intégration, tout en restant une référence d’inspiration et un historique d’essai. Conserver l’arbre gauche, la fiche centrale lisible, la recherche et l’exploration des relations sur le modèle JSON publié. Les mentions de choix non adopté dans l’étude U143 et l’essai U146 ci-dessous décrivent leurs étapes antérieures ; U150 prévaut. La validation porte sur l’orientation technique et ergonomique, sans validation métier ni publication supplémentaire. L’intégration demandée ensuite par U152 est décrite ci-dessus.

Demande de Laurent du **13 septembre 2026** : auditer l’ergonomie d’Atlas, avec une navigation arborescente à gauche et un examen des pages de détail dont les composants sont signalés comme concentrés à droite et trop serrés. Retenir l’arbre à gauche comme orientation de navigation. Sa structure doit provenir des relations explicites du modèle publié ; ne pas déduire les parents des identifiants, inventer des niveaux ou transformer les relations métier transversales en décomposition. Le groupe de présentation Business References reste distinct d’un niveau sémantique d’urbanisme. La demande porte sur l’audit, sans publication ni validation métier supplémentaire. Voir [l’audit ergonomique](audits/2026-09-13-ergonomie-atlas.md).

Précision U133 du même jour : supprimer les visites récentes de l’interface. Ne pas les conserver dans un accès secondaire.

**Réalisation U135 — 13 septembre 2026 :** le Go suivant l’audit autorise sa mise en œuvre dans Atlas. Navigation par arbre gauche à largeur réglable, expansion et sélection conservées ; sur écran étroit, arbre en tiroir. Fiche métier centrale avec Finalité, Définition, Périmètre et réserves visibles ; sources, révision et portée détaillée dans une section ouvrable. Aucun historique de visites récentes. La recherche et ses filtres portent sur la publication consultée ; aucun synonyme provenant du backlog n’est ajouté implicitement. Les anciennes coquilles de navigation vides reviennent à Urbanisation. Cette évolution de l’interface ne publie ni ne valide de contenu métier.

**Étude U143 — 14 septembre 2026 :** rechercher des outils modernes de cartographie pour enrichir l’expérience d’exploration ; pistes citées par Laurent : Cytoscape.js, LikeC4, React Flow et IcePanel. La génération, la compréhension et la maintenance du code par IA sont un critère explicite. Voir [l’étude d’inspiration](marche/etudes/2026-09-14-exploration-atlas/etude.md) et ses sources. Les choix de moteur et parcours qui y sont proposés restent des recommandations ; la demande n’autorise pas à les considérer comme adoptés ni à modifier le modèle. L’arbre gauche et la suppression des visites récentes restent acquis.

**Essai U146 — 14 septembre 2026 :** le Go suivant U143 autorise un prototype comparatif React Flow / LikeC4, dans `prototypes/atlas-exploration/`, avec arbre, recherche, fiche centrale et relation D07.c → D04.h sur la même publication v003. Le [bilan](prototypes/atlas-exploration/bilan.md) conserve résultats et limites. Le prototype consulte une publication précise via l’API Atlas ; la projection LikeC4 est générée depuis l’index/descripteur et ne constitue pas une autorité parallèle. Les liens agrégés sont explicités et retrouvent leurs relations sources. Cet essai n’adopte pas définitivement un moteur, ne remplace pas l’application courante et ne publie aucun contenu métier. Les travaux U144/U145 du backlog restent distincts.

## Règles courantes de publication et d’Atlas — U117 à U123

**Publication U142 — 13 septembre 2026 :** version courante **v003**, publication `2026-09-13.5`, descripteur `urbanisation-v003-2026-09-13-173533.json`. 51 nœuds, 36 capacités, univers Supply/Case et D04.e–h publiés. 54 décisions : 45 transcriptions du cycle U131 et neuf décisions sourcées U140/U141, dont réaffirmation des portées Agreement. Les anciennes décisions ADOPT-028/034 restent historiques et sont remplacées sur cette révision par ADOPT-054/055. Les validations partielles ne sont pas étendues aux compléments proposés. Les publications précédentes restent sélectionnables ; les indications v002 ci-dessous sont historiques.

**Publication U130 — 13 septembre 2026 :** la version courante est **v002**, publication `2026-09-13.4`, descripteur `urbanisation-v002-2026-09-13-162623.json`. Elle contient 36 capacités, dont six en D01 : Inventory Tracking, Record Inventory Movements, Inventory Visibility, Stocktaking, Supply Protection et Reservation. La décision ADOPT-048 transpose U129 sur le seul nom de D01.g ; définition et finalité restent proposées. Les 46 décisions de v001 sont conservées, sans nouvelle suspension. Les indications de release v001 et de cinq capacités D01 ci-dessous sont des jalons historiques.

**Atlas affiche uniquement les versions publiées, sous le nom Urbanisation.** Le backlog reste l’espace de construction du projet, hors de l’interface ; le panorama As Is reste également dans ses fichiers distincts. Les anciennes règles d’interface à trois espaces ci-dessous sont historiques et remplacées par cette section.

La publication courante est désignée par `modeles/release/index.json` → descripteur `urbanisation-v<NNN>-<YYYY>-<MM>-<DD>-<HHMMSS>.json` → `<publication>/model.json`. La version entière du modèle est complétée à trois chiffres au minimum ; l’heure du nom est UTC. Le descripteur contient aussi `revision`, l’identifiant de publication `version`, `published_at`, `last_modified`, les chemins et empreintes du modèle et de sa note de release. L’ancien `release/current.json` est conservé comme historique dans `release/legacy/` après la première activation du nouvel index. Ne pas créer une copie concurrente du modèle dans Atlas ni choisir une version par tri arbitraire de fichiers.

Le workflow calcule automatiquement `revision` et `last_modified` (UTC ISO 8601) pour le modèle global, les nœuds de tout type, les relations et les principes. Nouvel élément : 1 ; contenu modifié : +1 ; contenu inchangé : mêmes valeurs. Les champs de provenance et de statut saisis sont du contenu ; les champs calculés de publication et la révision saisie dans le backlog ne pilotent pas l’incrément. Une empreinte `content_sha256` distingue le contenu soumis des notes de validation calculées. La première date enregistrée ne prétend pas retrouver une date historique inconnue. Aucun fichier publié ou preuve figée n’est réécrit.

`$release` couvre comparaison, préparation, production, activation locale et vérification dans Atlas. Les candidats non validés restent publiables. La reprise des validations reste soumise aux identités, révisions et valeurs compatibles ; une nouvelle révision peut suspendre une reprise, sans effacer la décision historique. Le rapport le signale. Une demande expressément limitée à auditer, comparer ou préparer reste en lecture/préparation seule.

La liste **Version publiée** présente les publications de la plus récente à la plus ancienne. Par défaut, Atlas suit la publication courante et recharge automatiquement ses données sous cinq secondes lorsqu’il est visible, ou au retour au premier plan. Une version historique sélectionnée reste fixe ; son lien conserve l’identifiant de publication. Les requêtes backlog et panorama ne sont plus exposées par les API Atlas. Les sources documentaires restent consultables pour la provenance.

Après publication, vérifier l’identité du serveur puis la version et le contenu de `/api/model`. Démarrer Atlas s’il est arrêté ; relancer le serveur si son code Python a changé ou s’il sert un état incohérent, au même port avec `server-admin`. Un changement JSON seul ne requiert pas de relance. Après changement du JavaScript, recharger la page pour installer ce code. Ne pas confondre release produite et Atlas disponible ; aucun commit ou push implicite.

L’audit U117/U118 porte sur les douze repères : D01 à cinq capacités et onze renommages sans changement de sens dans D04–D07, soit 35 capacités au total. D03 et les cinq références étaient correctement repris ; D02 et les noms conditionnels D05 restent à instruire. Voir [l’audit complet](audits/2026-09-13-domaines-et-urbanisation.md). Les états décrits en U106–U116 ci-dessous sont conservés comme historique.


## Structure courante après refactoring — U106 à U111

Consignes de Laurent du **13 septembre 2026** : le modèle en réflexion s’appelle **backlog**, le modèle publié s’appelle **release**, et la connaissance de l’existant **panorama-as-is**, avec trois dossiers SI. Le modèle fait autorité en **JSON** ; le Markdown sert aux récits, insights, analyses, décisions argumentées et restitutions. U110 exige que les règles issues du refactoring soient consignées ici. Cette section remplace l’autorité Markdown décrite dans la réalisation historique U105 ; les mentions de versions P81 plus bas restent des jalons historiques sourcés.

**Précision U111 : la release contient les 36 capacités, même non validées. Publier ne vaut pas valider.** La release courante est désignée par `modeles/release/current.json`, sans déduire la dernière version du tri des noms de fichiers. À l’issue de ce refactoring, il s’agit de `2026-09-13.2`, issue de P81 0.9 : 49 nœuds, 36 capacités et 41 relations. Les neuf capacités d’Order Promising restent validées ; les autres conservent leur qualification. Huit portent des validations partielles, dont Reservation en réexamen, et dix-neuf n’ont pas de validation individuelle enregistrée. Les statuts affichés se répartissent donc en 9 `accepted`, 7 `partial`, 8 `proposed` et 12 `under_review` pour les capacités. Ces nombres décrivent cette version, pas une contrainte permanente du modèle.

### Autorités et fichiers

| Contenu | Autorité courante | Règle |
| --- | --- | --- |
| Modèle en réflexion | `modeles/backlog/model.json` | Modifier le JSON ; conserver les propositions, réexamens, alternatives et illustrations distincts. |
| Modèle publié | `modeles/release/current.json` → `<version>/model.json` | Consulter la version pointée ; aucun complément depuis le backlog ou le Markdown. |
| Portée des validations | `modeles/decisions/<version>.json`, référencé par le manifeste de release | Chaque décision cible des champs, une révision et des empreintes, avec auteur, date et sources. |
| Entrée figée d’une publication | `modeles/revisions/<version>/backlog.json` | Figer avant publication ; ne pas recalculer une release depuis le backlog vivant. |
| Preuves | `modeles/provenance/<version>/source-records.json` ; index courant distinct | Conserver captures et empreintes ; une évolution ultérieure d’un registre ne réécrit pas la preuve publiée. |
| Panorama actuel | `modeles/panorama-as-is/current.json` | Trois dossiers : `beaumanoir-historique/`, `boardriders/`, `sarenza/`, chacun avec versions. |
| Contexte partagé du panorama | `modeles/panorama-as-is/shared-<version>.json` | C-Log et contexte commun ; pas un quatrième SI, ni une interface présumée avec chacun. |
| Éléments As Is à instruire | `modeles/backlog/panorama-candidates.json` | Besoins, cible et mentions non étudiées restent distincts de l’existant. |
| Schémas et intégrité | `modeles/schemas/`, `scripts/validate_models.py` | Structure JSON, identités, relations, sources, décisions, empreintes et pointeurs contrôlés. |
| Restitutions | `restitutions/` et FLOW Atlas dans `app/` | Vues dérivées en lecture seule ; aucune autorité métier supplémentaire. |

Le [guide des modèles](modeles/README.md) décrit les fichiers et le cycle de publication. L’[audit du refactoring](audits/2026-09-13-structure-modeles.md) conserve les constats, extractions, limites et résultats de contrôle. Les 36 fiches CAP historiques sont préservées dans `modeles/backlog/legacy-capabilities.json` ; ne pas les assimiler par leur nombre aux 36 capacités P81. Les originaux ChatGPT restent inchangés dans `archive/`.

### Modèle, statut et validation

- Chaque nœud possède `id`, `revision`, `kind`, `layer`, `fields`, `review`, `source_refs` et un localisateur. Distinguer `domain`, `reference`, `group`, `capability`, `object`, `document` et `event`. La couche `transactional` ou `process` est indépendante du cycle `backlog` ou `release`.
- Les relations ont leurs propres identifiants, extrémités, types, statuts et sources. Déduire les parents des relations explicites, jamais des préfixes : D02.b/D02.c sont rattachées à D01 et D02.e à D03. `contains` et `presents` ne constituent pas la même relation. Les objets, documents et faits ne deviennent pas automatiquement des sous-capacités.
- En release, `accepted` signifie validé dans sa portée, `partial` partiellement validé, `proposed` non validé, `under_review` en réexamen. `illustration` est réservé au backlog dans la publication actuelle. Le même élément peut avoir un nom adopté, une définition proposée et un rattachement remis en discussion.
- `approved_fields` et `proposed_fields` qualifient les champs ; `adoption_ids` renvoie aux preuves `ADOPT-*`. Ces identifiants transcrivent les accords antérieurs, sans créer de nouveaux arbitrages. Préserver la distinction entre validation explicite et interprétation contextuelle. Ne pas déduire une validation depuis la présence en release ou depuis un libellé de statut éditorial.
- Conserver les alternatives non retenues dans le backlog et les rendre consultables dans Atlas. U116 choisit P82 comme découpage courant de D01 : ce n’est plus une alternative à appliquer. P84 reste distincte des nœuds courants. Une modification de valeur ou de révision ne transporte pas automatiquement une ancienne validation vers le nouveau contenu.
- Pour un type ou un niveau supplémentaire, définir son sens et ses relations, puis faire évoluer schéma et contrôles. La profondeur technique libre de la vue ne valide pas une hiérarchie métier. Le modèle processus détaillé reste à construire.
- Les correspondances marché et le glossaire restent des registres documentaires sourcés à ce stade. Leur indexation dans la provenance ne vaut pas conversion complète en modèle structuré. Continuer leurs mises à jour avec les capacités ; ne pas inventer des équivalences lors de la migration.

### Correction D01 et cohérence Atlas — U115/U116

Le backlog `2026-09-13.3` contient **35 capacités**, dont cinq dans D01 : **Inventory Tracking** (`D01.e`), **Inventory Visibility** (`D01.c`, révision 2), **Stocktaking** (`D01.d`), **Supply Protection** (`D02.b`) et **Reservation** (`D02.c`). U116 choisit cette base de travail sans validation métier supplémentaire. D01.e réunit D01.a et D01.b ; leurs anciens identifiants et relations sont conservés dans les versions historiques et ne doivent pas être réutilisés. Stocktaking, Supply Protection et Reservation conservent leurs champs, validations partielles et réserves.

La release `2026-09-13.2` reste inchangée : 36 capacités, dont six dans D01. Ne pas aligner les espaces en écrasant une version publiée. Une demande de release permettra d’intégrer le backlog. Voir [l’audit D01](audits/2026-09-13-atlas-d01.md).

Pour répondre sur le modèle courant, lire les nœuds et relations du JSON de l’espace demandé. Distinguer explicitement la carte courante, les propositions dans `alternatives` et les historiques. Une proposition encore non validée peut devenir la base de travail du backlog sur instruction de Laurent ; validation et choix d’une base de réflexion restent distincts. Les registres Markdown servent à expliquer cette évolution, sans remplacer le JSON dans nos réponses.

### Panorama et preuve de l’existant

Le panorama décrit l’état de connaissance des SI actuels, séparé de la cible. Les 85 repères initiaux sont conservés : 74 dans les trois panoramas et leur contexte partagé, 11 à instruire dans le backlog. Les collections distinguent composants/mentions, flux, autorités d’information et responsabilités de décision. Conserver le texte et les champs source, la qualification de preuve et les corrections.

**Sarenza est non traité (`not_assessed`)**, avec des collections vides ; ne pas en déduire une absence de composants. Ses anciennes mentions restent dans le backlog. Les besoins Boardriders, les orientations des référentiels de la plateforme et les responsabilités non localisées ne prouvent aucun déploiement. `as_of` date la consolidation ; `observed_at` reste nul sans observation datée. Les extrémités de flux non résolues conservent leur libellé source et un identifiant nul. Aucun appariement de nom, maître de donnée, version installée ou interface n’est inventé.

### Extensions prévues et priorité de travail — U112

Laurent demande de préparer la suite **sans l’explorer prématurément**. La [feuille de route JSON](modeles/backlog/modeling-roadmap.json) réserve un niveau au-dessus des domaines, dont le nom pourrait être Univers / Universe, mais dont le nom définitif, le sens et les instances restent ouverts. Ne pas créer ce niveau par déduction. Le contrat prévoit `group_role: urbanism_level` avec `level_ref`, distinct du rôle `presentation` de Business References ; cela ne transforme pas les groupes de présentation existants en niveaux sémantiques.

Les types `object`, `document` et `event` sont prévus pour un inventaire ultérieur. Leurs rattachements aux capacités seront des relations métier caractérisées, indépendantes de la hiérarchie. Prévoir aussi les relations entre capacités : une relation métier entre deux capacités n’est pas nécessairement une décomposition en sous-capacités. Aucun lien de possession exclusive, cardinalité, ordre obligatoire ou agrégat n’est présumé.

Le contrat relationnel dispose de `qualification` : `meaning` obligatoire pour un nouveau lien générique `relates-to`, puis `role`, `conditions`, `effects` et `scope` lorsque connus. Chaque relation garde son identifiant, ses extrémités, sa révision, ses sources et son statut propre. `relates-to` est un type technique permettant les liens capacité → capacité/objet/document/événement ; il ne constitue ni un vocabulaire métier adopté ni la preuve d’un lien réel. U112 autorise cette structure, pas le remplissage de relations imaginées. Les huit liens illustratifs historiques restent qualifiés comme tels ; leurs informations manquantes ne sont pas inventées.

**Travail actuel : domaines et capacités, puis épreuve de leur applicabilité aux trois SI Beaumanoir et à la plateforme FLOW de demain.** Le [registre d’applicabilité](modeles/backlog/applicability.json) déclare quatre contextes : périmètre historique de Beaumanoir, Boardriders, Sarenza (`as_is`) et plateforme FLOW (`target`). Chaque future évaluation cible un élément, un espace, une version et un contexte, avec sa justification et ses preuves. Distinguer applicabilité du problème, couverture décrite et responsabilité de réalisation. Pour FLOW, une pertinence métier n’implique pas un développement plateforme : l’adhérence externe reste une réponse possible, notamment pour la logistique.

Le tableau `assessments` est initialement vide : **absence de ligne = non évalué, jamais non couvert**. Les épreuves déjà consignées dans les récits P81 restent disponibles mais ne sont pas automatiquement transformées en preuves de couverture opérationnelle. Sarenza demeure non traité. Une validation de capacité dans le modèle commun ne valide pas son application dans chaque SI ni sa réalisation installée. Les schémas `applicability.schema.json` et `modeling-roadmap.schema.json` sont contrôlés avec le modèle ; les évaluations n’enrichissent pas le panorama par simple déduction.

### Backlog par défaut et skills de travail — U113

Par défaut, **explorer, discuter et construire le modèle se fait dans `modeles/backlog/`**, y compris pour afficher une capacité sans précision d’espace. Ne pas publier une évolution au seul motif qu’elle vient d’être rédigée. La release est la version publiée ; sa consultation explicite et ses liens restent possibles. Les API et l’entrée de FLOW Atlas adoptent également backlog par défaut.

Les deux skills initiaux U113 sont maintenus avec le projet puis installés dans le dossier personnel de skills Codex ; les skills Git ajoutés en U114 sont décrits ci-dessous :

- **`release`**, source dans [skills/release/SKILL.md](skills/release/SKILL.md) : comparer les évolutions du backlog à la release pointée, évaluer leurs effets et validations, préparer une nouvelle version figée, contrôler puis publier localement. La demande de release autorise ce cycle ; ne pas ajouter une confirmation systématique. Une demande limitée à comparer ou préparer s’arrête avant publication. Les candidats peuvent être publiés avec leurs statuts, conformément à U111. Aucune modification de valeur ne reçoit implicitement la validation de sa version antérieure.
- **`server-admin`**, source dans [skills/server-admin/SKILL.md](skills/server-admin/SKILL.md) : vérifier, démarrer, arrêter et redémarrer le serveur local FLOW Atlas via `Lancer-FLOW-Atlas.ps1`. Garder le port demandé (8765 par défaut), vérifier l’identité et le suivi du processus, puis constater le résultat. Démarrer sans fenêtre de navigateur sauf demande contraire. Une opération serveur ne modifie pas les modèles ni leurs validations.

Les copies personnelles sont dans `C:/Users/laure/.codex/skills/release/` et `C:/Users/laure/.codex/skills/server-admin/` pour ce poste. Maintenir les sources du projet et réinstaller les deux fichiers du skill (`SKILL.md`, `agents/openai.yaml`) lorsqu’ils évoluent, sans écraser un skill tiers homonyme. Ces deux skills `release` et `server-admin` sont propres à ce projet malgré leur découverte personnelle ; aucun déploiement externe ou push Git n’est compris dans leurs actions. Les fichiers de skill sont en UTF-8. Leur validation officielle utilise `skill-creator/scripts/quick_validate.py` ; PyYAML 6.0.2 est installé uniquement dans `.tools/skill-validation/` pour cet outillage, sans dépendance supplémentaire de FLOW Atlas.

La comparaison de release inclut les ajouts, retraits, changements de champs, rattachements, relations caractérisées et statuts. Les validations suspendues et les contenus restant dans le backlog doivent apparaître dans le bilan. La préparation n’actualise pas `release/current.json`. Une publication utilise uniquement l’état figé et contrôlé, avec preuve de ses entrées ; une évolution du backlog, de ses annexes ou de la release de départ après préparation exige une nouvelle évaluation. Les décisions compatibles sont reprises à même identité, révision et valeurs ; une autre révision suspend la reprise automatique, sans effacer l’accord historique. Les nouvelles décisions doivent avoir un nouvel identifiant et des preuves explicites. Vérifier aussi les notes narratives lorsqu’une validation est suspendue ; les anciennes affirmations de validation restent historiques et ne qualifient pas la nouvelle révision. Le rapport des changements accompagne chaque nouvelle publication dans `changes.json`. Ne pas republier simplement l’ancien instantané en ignorant le backlog courant.

Pour une nouvelle contribution source, `python scripts/refresh_sources.py` actualise uniquement l’index de provenance courant. Il ne relit pas les tableaux comme modèles et ne réécrit ni les preuves gelées ni les releases. Les scripts de comparaison et de préparation utilisés par le skill sont décrits dans son entrée et dans `modeles/README.md`.

### Travail sous Git et dépôt distant — U114

Le projet est suivi sous Git depuis le **13 septembre 2026**, avec `origin` pointant vers **https://github.com/laurent-sintes/Urbanisation.git**. Le dépôt distant était vide et public lors de la configuration, avec accès administrateur du compte connecté `laurent-sintes`. La branche locale initiale est `main`. L’identité auteur est configurée uniquement dans ce dépôt, avec le compte GitHub et son adresse sans réponse ; ne pas modifier l’identité Git globale.

Distinguer les actions : construire dans le backlog, publier le modèle avec `release`, enregistrer des fichiers dans un commit avec `commit`, puis envoyer des commits à GitHub avec `push`. Un commit ou un push ne valide aucune capacité, ne publie pas automatiquement une nouvelle release métier et n’intervient pas sur le serveur.

- **`commit`** : source [skills/commit/SKILL.md](skills/commit/SKILL.md), copie personnelle `C:/Users/laure/.codex/skills/commit/`. Examiner le diff et l’index, vérifier le périmètre et les contrôles pertinents, puis créer un commit local au message descriptif. Respecter les changements de Laurent ; pas d’amendement ni de réécriture implicite, pas de push automatique.
- **`push`** : source [skills/push/SKILL.md](skills/push/SKILL.md), copie personnelle `C:/Users/laure/.codex/skills/push/`. Vérifier la destination de lecture et d’envoi, la branche, l’upstream et les commits concernés ; actualiser les références distantes, envoyer sans force ni suppression et vérifier le hash distant. Une invocation simple envoie les commits existants. Une demande d’envoyer les modifications ou de « commit et push » inclut leur commit préalable. Signaler les changements laissés hors de l’envoi. Ce skill cible Urbanisation ; `flow-push` concerne le dépôt distinct FLOW-Program.

Les demandes de commit ou push autorisent l’action correspondante sans confirmation systématique. Créer ou modifier le skill ne l’invoque pas. Une demande limitée à vérifier ou préparer reste sans commit/push. Un problème de conflit, d’authentification ou de protection de branche doit être résolu dans le périmètre autorisé, sans effacement de travail ni changement de destination ou de visibilité comme contournement.

Versionner les sources documentaires, archives d’origine, modèles JSON, preuves et versions publiées, restitutions, application, scripts et sources des quatre skills. `.gitignore` exclut `.tools/`, l’état du serveur `app/.runtime/`, les caches, dépendances, tests temporaires, fichiers d’environnement locaux et `modeles/staging/`. Les preuves et modèles publiés ne sont pas exclus. Les copies personnelles de skills ne sont pas dans ce dépôt : les mettre à jour depuis `skills/` quand leurs sources évoluent.

**Préserver les empreintes :** `.gitattributes` désactive la conversion automatique des fins de ligne (`* -text`). Git doit conserver les octets des archives et fichiers figés ; les différences textuelles restent consultables. La règle whitespace reconnaît CRLF comme fin de ligne (`cr-at-eol`) sans le convertir. Ne pas normaliser ces fichiers à l’occasion d’un commit. Les contrôles sont adaptés aux changements, et les validations déjà exécutées sur le même contenu peuvent être réutilisées. Ne pas lancer de release métier pour rendre le dépôt propre.

La mise sous Git crée une base locale versionnée. Le premier envoi distant relève d’une demande de push ; la création de ces skills n’envoie pas le contenu du projet à GitHub.

### Maintenance et publication locale

1. Lire le JSON concerné, les sources et `connaissance/04-corrections.md`. Enregistrer l’apport utilisateur avant sa reformulation ; consigner ici toute nouvelle règle de fonctionnement.
2. Modifier le backlog JSON et les analyses associées, en conservant les identifiants. Réviser les éléments modifiés et leurs correspondances marché. Les registres historiques de carte et panorama sont des entrées de migration, plus des catalogues concurrents à tenir en parallèle.
3. Pour publier le backlog courant, suivre le skill `release` : `python scripts/prepare_release.py report`, puis `prepare --version VERSION --source SOURCE`, puis `publish --version VERSION --activate`. La préparation fige le candidat et son rapport dans `modeles/staging/<version>/` sans modifier la release. La publication contrôle les entrées figées et l’absence de changement depuis leur préparation ; `--activate` actualise le pointeur local en dernier. `publish_release.py --from-manifest` reste un outil historique de republication d’une ancienne capture, sans intégration du backlog courant. La publication de candidats est autorisée par U111 ; une nouvelle validation métier exige toujours un accord explicite avec sa portée.
4. Ne jamais écraser les releases, révisions ou preuves gelées. Une correction donne lieu à une nouvelle version ; le pointeur courant indique celle à consulter. Le panorama et son contexte partagé suivent également des versions explicites. L’absence de Git était un constat de la migration initiale ; U114 ajoute maintenant le suivi Git décrit ci-dessous. Les captures figées conservent leur rôle de preuves et ne sont pas remplacées par l’historique Git.
5. Exécuter `python scripts/validate_models.py`, puis les contrôles adaptés. Régénérer les Markdown de lecture avec `python scripts/render_models.py` ; compléter le journal, les corrections et l’audit si nécessaire.

Les extracteurs `scripts/migrate_urbanism.py` et `scripts/extract_panorama.py` servent à la migration initiale dans une destination neuve et aux contrôles de cette capture. Ne pas les employer pour réimporter automatiquement le Markdown sur le modèle courant. `python scripts/extract_panorama.py --check` vérifie les fiches de départ et leurs corrections liées ; il ne découvre pas le SI.

Contrôles du modèle : `python -m unittest discover -s scripts -p "test_*.py"`. Les schémas utilisent un sous-ensemble documenté de JSON Schema 2020-12 ; le validateur local refuse les mots-clés non pris en charge. Il ne faut pas le présenter comme une implémentation complète de la norme.

FLOW Atlas lit les JSON avec un sélecteur Release / Backlog / Panorama As Is, le Backlog étant la vue initiale selon U113. Un lien ou une demande explicite vers un autre espace est respecté. Aucun repli implicite entre espaces. `app/exploration.json` ne porte que la présentation ; `app/model-metadata.json` et `app/legacy/exploration-before-json.json` sont historiques. Le Markdown est lu uniquement pour ouvrir les sources. Le serveur est local, en lecture seule, sur `127.0.0.1`. Lancer `Lancer-FLOW-Atlas.ps1` ; après changement Python, arrêter et relancer avec le lanceur identifié, puis actualiser la vue. Un changement JSON ou de présentation requiert une actualisation.

Contrôles d’application : `python app/server.py --check`, `python -m unittest discover -s app -p test_data.py`, `node --test --test-isolation=none app/test-model.mjs`. Pour une évolution de parcours, utiliser aussi `node app/verify-browser.mjs` avec son serveur et Playwright disponibles ; voir [app/README.md](app/README.md). Ne pas reprendre les tests historiques du prototype comme preuve de l’application courante. Ces opérations locales n’incluent aucune publication sur Internet.

## Objectif du projet

**Application U141 — 13 septembre 2026 :** le Go structure les univers **Supply** et **Case** dans le backlog, avec `group_role: urbanism_level` et `level_ref: universe`. Supply accueille les domaines transactionnels et le groupe Business References ; Case reste réservé, sans capacités processus inventées. D04 comporte désormais quatre capacités : **Order Registration, Order Revision, Order Visibility, Order Reconciliation**, repères D04.e–h ; noms et descriptions courtes présentés validés par Laurent, détails nouveaux proposés. Les anciens D04.a–d sont retirés de la carte active, conservés dans `modeles/backlog/history/pre-U141.json` et les releases ; aucun identifiant réutilisé. Agreement inclut contrat complet, périodes et engagements projetés. D04 suit la commande autorisée, D07 les prestations, prises en charge et faits ; grain détaillé et comportements ouverts Q077. Le lien Case/Order est préparé dans la feuille de route sans cardinalité ni nouvel inventaire d’objets. Voir C78 et `connaissance/27-order-management-et-univers.md`. Ces règles remplacent les réserves historiques sur l’absence de niveau supérieur structuré ; aucun changement implicite de release.

**Orientation U140 — 13 septembre 2026 :** distinguer le **Case**, demande traitée ultérieurement dans l’univers **Case**, de l’**Order**, objet de pilotage transactionnel de l’univers **Supply**, priorité de l’exploration actuelle. Retenir **Order Management** comme domaine commun aux commandes de toutes natures, notamment achat, vente, transfert et retour, pour tous clients et volumes. D04 reprend ce nom dans le backlog ; ses capacités historiques restent à refondre, sans validation automatique. Les variantes reposent sur des règles, décisions et workflows ; DMN est cité pour les décisions, sans choix de moteur ni confusion avec le workflow complet. Conserver les invariants et objets métier durables : un moteur ne remplace pas leur définition. Ne pas créer deux domaines Supply B2B/B2C par défaut ; éprouver leurs contraintes distinctes, leur couverture et leurs volumes. Les mots univers Supply/Case expriment l’orientation ; leur introduction dans la hiérarchie JSON et les rattachements détaillés restent à concevoir. Analogie TM Forum partielle, pas équivalence Case/Product Order ni mapping automatique Service/Resource. Voir U140, C77 et [la comparaison](marche/supply-b2b-b2c.md).

Construire une base de connaissance évolutive pour cartographier les capacités métier Beaumanoir, décrire l'existant de GBM, Boardriders et Sarenza et explorer leur convergence vers un SI cible.

Le périmètre couvre le cœur ERP commerce : achats, ventes, SAV, stocks, allocations et référentiels opérationnels associés. Finance, contrôle de gestion, conformité, design produit et planification de saison sont exclus comme domaines ; leurs interfaces utiles restent à documenter. Le SI C-Log conserve son autonomie. La logistique est hors du périmètre de développement de la plateforme du Programme FLOW, mais reste en adhérence (U58/F158). Documenter les interactions utiles, les autorités et les responsabilités de décision à cette frontière ; comprendre une aptitude logistique ne l’inscrit pas dans les développements FLOW. La définition fonctionnelle de Supply ne fixe pas à elle seule cette répartition.

Les capacités métier restent au centre de la cartographie. Préciser les autorités sur les informations et les responsabilités de décision selon les marques, canaux, SI et situations. La hiérarchie et les capacités candidates restent à éprouver. L’orientation précisée par Laurent (U18/U19/U20) est une urbanisation à deux couches : socle ERP portant les capacités liées au métier envisagées de manière générique, et couche processus/organisation/situations. Chacune possède son modèle métier durable, ses objets, sa persistance et son urbanisation ; elles communiquent par contrats durables, avec API et EDA envisagées. Périmètre réaffirmé par Laurent en U50 : la capability map cible la couche transactionnelle ; un autre modèle fonctionnel orienté processus décrira la couche processus. Maintenir ces deux modèles distincts, même lorsque les deux couches utilisent des moteurs de décision, détermination et orchestration. Documenter les comportements propres à la couche processus dans son modèle fonctionnel et leurs liens avec les capacités du socle, sans étendre la capability map à cette couche. Préserver cette intention ; expliciter les différences de vocabulaire avec le marché sans substituer une autre architecture. Les répartitions détaillées et choix techniques restent à éprouver. Voir `connaissance/15-orientation-deux-couches.md`.

Priorité de travail fixée par Laurent (U21) : explorer d’abord les capacités métier génériques du socle transactionnel à partir des récits Beaumanoir. Approfondir la couche processus aux frontières utiles à cette exploration. La première vue de travail est dans `connaissance/16-capacites-socle-transactionnel.md` ; ses regroupements restent proposés. L’exploration du bloc stock et du stock virtuel/logique (U26/U27) est dans `connaissance/17-exploration-bloc-stock.md` ; P66 reste une proposition, avec Q066 ouverte. Les apports U30/U31 précisent le besoin BRD de comportements sur stock présent/futur et de réaffectation prioritaire, ainsi que le rattachement proposé du réexamen à la promesse ; voir `connaissance/18-politiques-engagement-gbm-brd.md`. Besoin métier déclaré et réalisation installée restent distincts ; P68/P69 sont des propositions de modèle et de frontière.

L’étude préalable demandée par Laurent (U25) est disponible dans `marche/etudes/2026-09-09-modeles-marche/etude-comparative.md` : équivalences, récurrences, structures, niveaux et contenus, avec sources et limites de preuve. La consulter avant de poursuivre la décomposition locale ; ses propositions ne constituent pas une hiérarchie ni des équivalences validées.

Maintenir aussi un référentiel de marché pour comparer durablement notre urbanisation aux cadres standard et aux modèles d'éditeurs. Attribuer à chaque référence un rôle explicite et conserver la provenance des adaptations. Cette exigence n'impose aucune structure principale ni solution éditeur.

Précision de Laurent en U49 : le socle transactionnel et la couche processus sont tous deux envisagés avec des moyens de décision, détermination et orchestration ; la couche processus est orientée Case Management. Ne pas réserver l’orchestration à la couche haute. Chaque couche conserve son modèle métier et ses autorités. Une même solution ou des solutions distinctes restent possibles, sans choix de produit, d’instance partagée ou de mutualisation arrêté. Distinguer l’aptitude métier de son moteur de réalisation ; voir `connaissance/15-orientation-deux-couches.md` et C40.

Précisions de Laurent en U54–U56 : les parcours commerciaux réassort, eCommerce et retours distingués dans un OMS se situent au-dessus de la supply execution. Pour notre modèle, l’OMS est un Case Management préimplémenté pour la vente ; la Supply est la couche transactionnelle de contrôle, d’orchestration et d’optimisation de la logistique. Délimiter ses domaines à partir des problèmes génériques sollicités par les parcours, sans reproduire leurs types dans la capability map. Préserver la distinction avec la réalisation logistique et l’autonomie de C-Log. U57 précise son double rôle : répondre aux commandes du commerce et porter une intelligence opérationnelle de backoffice, notamment rééquilibrage, prévision et gestion des impondérables. Ne pas réduire la Supply à l’exécution passive des demandes commerciales ; préciser le périmètre des prévisions sans réintroduire automatiquement la planification de saison exclue. Ces définitions locales guident la comparaison aux produits ; elles n’imposent ni objet Demande unique ni domaine Supply unique. Voir `connaissance/23-reassort-transferts-et-promesse.md`.

## Maîtrise externe des référentiels — U97/U98

**Règle courante, précisée en U134 le 13 septembre 2026 :** les référentiels de la Supply sont des projections ; leurs sources de vérité sont gérées par des produits tiers. Chaque référentiel comporte **au moins une capacité d’ingestion** et peut porter des capacités de **visibilité et de recherche en lecture seule**. Cette précision remplace la restriction historique « une ingestion et rien d’autre » ci-dessous, sans réintroduire création, administration, dédoublonnage ou validation métier des données maîtresses. L’ingestion maintient la projection locale ; lecture seule qualifie son usage par les consommateurs. Ne pas déduire le maître exact d’un attribut ou d’un périmètre des exemples de familles d’applications. Ne pas étendre automatiquement cette règle des référentiels aux états transactionnels propres à la Supply. Agreement et commande restent distincts ; D04/D07 sont à réexaminer selon U100. Consulter C75 et [l’audit D04/Agreement](audits/2026-09-13-d04-agreement-projections.md). Les noms de capacités suggérés dans cet audit sont proposés par l’IA, sans adoption ni publication implicite.

Orientation impérative de Laurent, 11 septembre 2026 : la plateforme n’est maître ni de **Party / Role**, ni d’**Agreement**, ni de **Catalog**. Regrouper ces trois domaines sans intercaler d’autre domaine ; chacun ne porte qu’une capacité d’ingestion. Les applications externes portent création, modification, vérification des données, dédoublonnage, enrichissement et parcours d’enregistrement ou de recrutement. Ne pas réintroduire ces aptitudes dans la vue plateforme sous une autre formulation.

Conserver trois modèles distincts, reliés par identifiants. Agreement reçoit l’identité du Party, le ou les catalogues permettant de commander et les conditions particulières utiles à Order Promising ; Catalog reçoit notamment prix et zones géographiques d’application. Party / Role porte une identité de référence sans doublon hors plateforme ; ses rôles métier restent distincts de RBAC. CRM/SRM et applications de catalogue sont cités comme sources externes, sans preuve de maîtrise installée par application ou attribut.

U98 confirme que **les commandes sont distinctes des Agreements**. Continuer à examiner les engagements transactionnels de commandes en D04, sans y placer l’administration des contrats de référence. Les décisions des domaines consommateurs appliquent les informations reçues ; elles ne constituent pas des capacités de vérification du référentiel. P81 version 0.6 contient dix domaines actifs et 34 capacités, avec D09/D11/D12 contigus. Les repères retirés restent traçables en C64 et dans l’audit du 11 septembre. Les neuf capacités d’Order Promising validées en U95 restent acquises.

## Définition des capacités et vocabulaire

- Définition impérative réaffirmée par Laurent en U33 : une capacité décrit **ce que sait faire l’entreprise indépendamment de son organisation et de ses outils**. Conserver ce sens dans le catalogue, ses vues et toute décomposition.
- Définir d’abord l’aptitude métier durable, son résultat et son périmètre. Une sous-capacité doit elle-même respecter cette définition et rester dans le périmètre de sa capacité mère. Une responsabilité organisationnelle, un contrat, une opération ou un découpage logiciel ne suffit pas à créer une capacité.
- Approfondir les documentations de marché pour expliquer, illustrer et éprouver les capacités. Qualifier séparément leurs objets, opérations, règles, variantes et réalisations ; ne pas transformer automatiquement ces détails en sous-capacités.
- Maintenir le glossaire des notions et des verbes dans `connaissance/19-glossaire-metier.md`. Distinguer la définition de capacité réaffirmée par Laurent des autres définitions proposées. Ne pas renommer automatiquement les candidats ni présumer une validation du vocabulaire détaillé.
- Délimiter les domaines comme des espaces cohérents de problèmes métier liés entre eux, conformément au guide de Laurent en U45/U46. Expliciter les liens, connaissances, concepts et règles qui rendent utile leur étude commune, puis identifier les capacités nécessaires. Des relations entre domaines n’imposent pas leur fusion. Rester à cette étape sur la cartographie métier ; ne pas engager de découpage en bounded contexts, applications ou services. Distinguer le souvenir du livre d’Evans des passages effectivement consultés dans ses sources ; voir `marche/premier-niveau-regroupement-capacites.md`. U52 confirme l’examen des frontières par les cas et reconnaît Order Promising comme domaine au sens problématique local ; son périmètre détaillé reste ouvert. Source to Pay est une lecture processus, utile pour examiner la couverture et les traversées de domaines. Ne pas présenter ces deux lectures comme des découpages de même nature ; aucun catalogue principal ni liste complète validé.
- Nommer **Finalité** la colonne qui décrit à quoi sert une capacité, conformément au choix de Laurent en U42. La distinguer de sa nature de contribution ; les natures et les contenus proposés restent à éprouver.
- Employer un verbe et un objet métier explicites pour proposer un libellé ; sa définition complète doit rester indépendante de l’organisation et des outils. Le vocabulaire des actions aide à clarifier le sens, sans imposer une capacité pour chaque verbe ou opération.
- À la suite de U34, éviter « fonction » sans qualificatif : employer « fonctionnalité de produit » pour un comportement offert par un outil et « regroupement de capacités » pour une agrégation dans la carte. Aucun niveau hiérarchique nommé Fonction n’est adopté. U35 met le verbe « tenir » en réexamen : il provenait d’une formulation assistant, pas d’un libellé SAP français vérifié. Préférer un verbe explicitant le résultat pour les nouvelles propositions, sans renommage automatique des capacités existantes.

## Collaboration

- Échanger en français et tutoyer Laurent.
- Avancer de manière itérative et exploratoire : approfondir les récits, ouvrir et comparer des options, puis consigner les arbitrages explicites.
- Communiquer clairement, signaler les incertitudes et poser des questions ciblées lorsque l'information manque.
- Réaliser les mises à jour documentaires demandées ou nécessaires dans le périmètre convenu. Les validations métier et arbitrages de cible appartiennent à Laurent.
- Maintenir la connaissance dans les fichiers au fil des échanges, sans dépendre de la seule mémoire de conversation.

## Libellés dans les documents

- Les abréviations GBM et BRD sont autorisées dans nos échanges et dans les noms de fichiers.
- À l’intérieur des documents rédigés, employer les libellés canoniques des entités dans les titres, paragraphes, tableaux, légendes et libellés de liens, plutôt que ces abréviations. Reprendre les dénominations de référence en conservant le périmètre désigné, notamment la distinction entre le périmètre historique de Beaumanoir et l’ensemble du groupe ; écrire Boardriders pour BRD.
- Préserver les verbatims, les identifiants stables et les chemins de fichiers, conformément aux règles de provenance. Appliquer la convention au texte rédigé autour de ces éléments.

## Organisation

- `README.md` : point d'entrée et navigation.
- `modeles/` : autorités JSON backlog, release et panorama-as-is, schémas et preuves versionnées.
- `connaissance/` : récits, apports, analyses, corrections et historiques Markdown ; modèles structurés dans `modeles/`.
- `restitutions/` : Markdown générés à partir des JSON, sans édition métier directe.
- `scripts/` : migration initiale, comparaison/préparation/publication, indexation des sources, contrôles et génération des vues.
- `skills/` : sources des skills du projet, avec copies personnelles installées pour leur découverte.
- `app/` : FLOW Atlas, lecteur local des modèles JSON et des sources documentaires.
- `marche/` : références du marché, éléments externes examinés, méthode et correspondances avec Beaumanoir.
- `JOURNAL.md` : historique des évolutions.
- `audits/` : contrôles datés, preuves de couverture, écarts et corrections.
- `archive/` : fichiers d'origine ChatGPT, conservés sans modification. Ils ne sont pas synchronisés avec les registres courants.
- `AGENTS.md` : référence pour l'objectif et le fonctionnement ; `CONVENTIONS.md` renvoie à ces règles.

Avant une mise à jour métier, lire les registres pertinents et les corrections dans `connaissance/04-corrections.md`. Consulter les documents archivés pour les développements narratifs initiaux.

## Provenance et validation

Un fait déclaré n'est pas une preuve de configuration ; une proposition assistant n'est pas une décision validée.

- Conserver les identifiants et les références aux sources. Ne jamais réutiliser un identifiant pour un autre objet.
- Enregistrer chaque nouvel apport métier de Laurent avec un identifiant U disponible, sa date, son texte et son contexte avant d'en tirer des assertions. Signaler une reformulation ; ne pas la présenter comme un verbatim. Consigner les consignes de fonctionnement dans ce fichier et le journal.
- Séparer déclarations, hypothèses, propositions, décisions explicites et points à confirmer. Préserver les limites et le périmètre : marque, canal, SI et période.
- Consigner chaque correction avec sa source et actualiser les entrées concernées. Conserver la formulation remplacée dans la correction ou le journal.
- Fermer une question seulement avec une réponse sourcée. Conserver les questions résolues.
- Ne promouvoir une capacité candidate ou une option cible qu'après validation explicite, avec auteur et date.
- Une documentation éditeur décrit un produit ; elle ne prouve pas le fonctionnement du déploiement Beaumanoir. Dater et sourcer toute nouvelle vérification externe.
- Les mentions de couverture et de vérification importées décrivent le travail ChatGPT initial, sans valoir audit indépendant. La conversation originale a été consultée et capturée dans `archive/conversation-chatgpt-2026-09-09.json` et sa copie de lecture Markdown. L'audit daté est dans `audits/2026-09-09-conversation-chatgpt.md` ; ses limites restent explicites. Les contributions assistant consolidées restent des synthèses.

## Cycle de mise à jour

1. Lire les connaissances et corrections pertinentes.
2. Enregistrer la nouvelle source ou la consigne de fonctionnement.
3. Actualiser les registres concernés, leurs statuts et leurs références, sans effacer les réserves non levées.
4. Contrôler les identifiants, la cohérence des références et les liens modifiés.
5. Ajouter une entrée au journal et expliquer brièvement à Laurent les changements et les points encore ouverts.

Éviter les synthèses concurrentes sans liens vers leurs sources. Les modèles JSON font autorité ; les productions Word, PDF et restitutions Markdown doivent être issues de l’espace courant choisi et datées. Préserver les originaux dans `archive/`.

## Comparaison au marché

- Suivre `marche/methode.md` pour qualifier les références et leurs correspondances.
- Distinguer cadre de modélisation, modèle de capacités, processus, composants métier, données et description de produit.
- Conserver organisme, version ou inconnue, source, date, localisateur, définition consultée, adaptation et justification. Distinguer une référence identifiée d'un contenu réellement examiné.
- À chaque évolution d'une capacité, actualiser ses correspondances marché ou signaler explicitement qu'elle n'est pas encore comparée. Une similitude de libellé ne vaut pas équivalence.
- Signaler les constructions Beaumanoir comme locales ; ne jamais les présenter comme un standard sans provenance. L'absence de correspondance trouvée ne prouve pas qu'une capacité est spécifique.
- Vérifier les sources pertinentes avant un arbitrage ; dater les contrôles et conserver l'historique des versions. Aucun catalogue principal n'est retenu sans validation explicite de Laurent.

Orientation des références précisée par Laurent en U60 : conserver IBM CBM 2005 comme preuve historique, sans en faire une référence actuelle prioritaire. Tenir compte de sa réserve sur BIAN et la lecture par services, distincte de la définition de capacité. TM Forum demeure une piste intéressante ; BIZBOK est approfondi dans `marche/bizbok-capacites-et-domaines.md`. Ni modèle principal ni règle de décomposition obligatoire adoptés ; la livraison d’un modèle Retail/Wholesale Guild reste non établie par les sources examinées.

Précision de modèle de Laurent en U61 : la plateforme distingue objets métier rapprochés d’aggregate roots, faits de gestion envisagés comme événements associés à des documents, et documents représentant des états ou des objets non modifiables produits/captés. Conserver cette distinction et sa provenance ; les périmètres d’agrégats, cardinalités et règles détaillées restent à préciser. La note `connaissance/24-capacites-objets-et-faits.md` propose de relier ce modèle à l’analyse des capacités, sans assimiler automatiquement objet métier, document, fait et notification ni présumer un choix de persistance.

Précision U62 : les objets métier existent dans les deux couches. Laurent cite Demande de réassort pour le modèle processus, dans l’approche Case Management ; les domaines transactionnels ont également leurs objets. Ne pas utiliser la seule présence d’un objet métier pour qualifier la couche. Conserver les liens entre modèles sans présumer leur fusion ni une convention universelle de demande.

Précision de méthode U63/U64 : la [carte de travail des domaines cœur](connaissance/25-domaines-coeur-et-epreuve-recits.md), P81, doit être éprouvée sur les récits du périmètre historique de Beaumanoir et de Boardriders. Distinguer points d’accueil conceptuels, couverture partielle, adhérences et inconnues. Signaler aussi les capacités cœur plausibles absentes des listes, en séparant besoins déclarés, déductions des récits et suggestions de marché. Le nombre de domaines, les formulations de P81 (34 en version 0.1, 35 en version 0.2 après U66/U67) et leurs rattachements restent proposés ; ils ne remplacent pas les 36 fiches CAP historiques ni leurs statuts.

## Nomenclature anglaise et réemploi du marché

Consigne explicite de Laurent en U66 : employer une nomenclature en anglais et réutiliser les noms de marché lorsqu’ils conviennent au périmètre, notamment **Inventory Management**, retenu pour D01. Conserver les définitions et échanges en français, sauf demande contraire. Dans la carte courante, traduire les libellés en conservant identifiants, sens, résultats et limites ; préserver les noms historiques comme provenance. Les traductions locales restent proposées lorsqu’aucun nom de marché adéquat n’est établi. Ne pas réduire une définition pour la faire entrer dans un nom connu : par exemple Pricing ne couvre pas tous les droits et conditions de D10.

Le choix d’un nom ne valide pas une frontière ni une capacité. Qualifier le niveau et la nature exacts des termes externes : Business Area, Business Capability, fonctionnalité de produit, objet ou API. Une Enterprise Business Function SAP activable n’est pas automatiquement une Business Capability RBA ; ne pas qualifier Supply Protection / Supply Assignment comme Business Areas, ni comme entrées RBA ou RSA, sans preuve du catalogue correspondant.

Précision de Laurent en U67 : **Supply Protection** et **Supply Assignment** expriment des aptitudes métier de l’entreprise ; **Allocation Run** relève des mécanismes de réalisation IT. Ne pas confondre nature de l’aptitude et présentation de sa réalisation dans une documentation produit. L’absence de rang natif RBA établi ne disqualifie pas la capacité métier. Conserver distincts le sens métier, le mécanisme et le classement externe ; définitions détaillées, maille et rattachements restent à éprouver, notamment la frontière affectation/réservation. Voir C49 et P81 version 0.2.

Méthode de revue précisée en U68 : reprendre les domaines un par un, en commençant par D01, avec nom anglais, Finalité, capacités décrites et correspondances dans les autres modèles. Qualifier les rapprochements et leurs limites ; la présentation ne vaut pas validation des frontières ni des équivalences.

Orientation de rattachement U74 : Laurent place **Supply Protection** dans **Inventory Management**, entendu au sens large. Appliquer ce rattachement dans la carte de travail et les correspondances, sans déplacer automatiquement disponibilité, réservation, affectation ou promesse. P81 version 0.3 conserve le repère historique D02.b pour Supply Protection désormais située en D01 ; son préfixe ne désigne plus son domaine courant. Le rattachement local ne prouve pas une équivalence native SAP RBA ; définitions détaillées et autres frontières restent à éprouver.

Orientations U75 : rattacher **Reservation** à **Inventory Management** et **Supply Assignment** à **Order Promising**, en distinguant engagement quantitatif et couverture des engagements/commandes par des ressources. P81 version 0.4 conserve les repères historiques D02.c/D02.e pour ces mêmes aptitudes. Le calcul de disponibilité et la notion de stock logique/virtuel sont interrogés, sans définition ni granularité autonome validées. D02 reste en réexamen ; ne pas maintenir un domaine par simple inertie de numérotation. La proposition de regrouper les représentations dans Inventory Management doit préserver leurs différences et l’absence de double comptage ; ce regroupement détaillé n’est pas encore un arbitrage utilisateur.

Vocabulaire explicitement fourni par Laurent en U76 : **stock physique** = ce qui existe réellement quelque part ; **stock logique** = les états métier de ce même stock ; **stock virtuel** = une quantité considérée disponible selon un calcul. Conserver ces sens distincts (TER040–TER042, C53), sans assimiler stock logique à une simple vue consolidée ni employer logique/virtuel comme synonymes. Les exemples chiffrés sont illustratifs ; combinaisons d’états et prévention des doubles déductions restent à préciser. U77 propose physique/logique dans Inventory Management et virtuel dans Promising : conserver ce statut d’hypothèse. Distinguer projection de promesse et disponible courant de réservation avant d’attribuer tout calcul à un domaine. Q066 est partiellement répondue sur le vocabulaire, toujours ouverte sur les règles et autorités.

Réexamen U78 : Laurent hésite sur la réservation et demande l’appui SAP/Microsoft. Conserver le rattachement U75 comme option de travail remise en discussion, sans le présenter comme une frontière ferme ni le déplacer sans nouvelle orientation. ELM070–ELM072/CMP042 montrent réservations Microsoft sur présent et commandé non reçu, Reservations SAP de mouvements planifiés et effets de réservation de Supply Assignment. Distinguer résultats et autorités sans imposer deux cycles indépendants ni une séparation universelle réservation/affectation ; C54.

Précision U79/U80 : Laurent inclut potentiel fournisseur sous contrat, achats planifiés non engagés et approvisionnements en cours dans l’exploration des stocks futurs. U80 confirme que la notion de stock futur est gérée dans **Inventory Management et Order Promising** ; la date de promesse dépend aussi de l’amont, pas seulement de la logistique sortante. Préserver cette orientation sans confondre représentation d’une ressource attendue et quantité virtuelle calculée U76. Les autorités détaillées, degrés de fermeté et critères d’admissibilité restent à éprouver ; une présence de la notion dans les deux domaines ne fusionne pas leurs modèles. Voir la carte P81, U79/U80 et Q066.

Clarification U81 : rendre explicites **stocks physiques et logiques dans Inventory Management**, et **stock virtuel calculé puis appliqué à la promesse dans Order Promising**. Le mot états ne doit pas masquer la notion de stock logique. Préserver la connaissance des ressources futures dans D01 selon U79/U80 et distinguer calcul de faisabilité et engagement de promesse. Physical Inventory désigne une capacité de constat et rapprochement physique, pas le périmètre entier de D01. Les formules, objets, autorités et frontières détaillées restent à éprouver ; voir C55 et la carte P81.

Précision U82 : Establish inventory positions et la proposition de nom local Physical Inventory sont contestés par Laurent. Les conserver comme provenance sans les présenter comme libellés satisfaisants ou adoptés ; consulter la revue D01 et C56 avant de les réutiliser. Distinguer noms natifs SAP/Microsoft, adaptations proposées, aptitude au comptage/rapprochement et finalité d’exactitude. Stocktaking, Manage inventory quantities et Count and reconcile inventory restent des options, sans arbitrage définitif.

Précision U84 : employer **Reservation**, sans préfixe Inventory, pour la capacité de D01 ; choix explicite de Laurent. **Counting** est la proposition courante pour le comptage et rapprochement, avec préférence exprimée, sans adoption définitive ; conserver dans sa définition qualification des écarts et corrections justifiées. Stocktaking reste une proposition antérieure et un terme de marché, avec historique C57.

Réexamen U85 : le titre Stocktaking est de nouveau discuté face à Counting, car Laurent y voit l’aptitude de faire l’inventaire indépendamment des outils. Ne pas considérer Counting comme adopté ni comme intrinsèquement informatique. P82 laisse les deux noms ouverts ; la définition de comptage/rapprochement/correction est conservée.

Décision U86 — 2026-09-11 : Laurent retient **Stocktaking**, en un mot, pour la capacité D01.d et sa représentation dans P82 ; **Inventory accuracy** en exprime la Finalité. Employer ce nom courant, avec comptage, rapprochement, qualification des écarts et corrections justifiées dans la définition. Cette décision remplace les options de nom ouvertes en U82/U84/U85 ; préserver les noms antérieurs dans les historiques. Voir C58.

Précision U88 : dans la demande de revue du deuxième domaine après Inventory Management (U87), Laurent vise **Order Promising**, encore identifié D03 dans les fichiers. Utiliser le nom pour éviter l’ambiguïté ; ne pas renuméroter D02/D03 automatiquement. L’audit daté et la proposition de style sont dans `audits/2026-09-11-order-promising.md` et P83 ; propositions non adoptées.

Précision U91/U92 : Laurent demande d’ajouter les aptitudes de décision ressortant de la comparaison de marché et préfère **décision** à **détermination** dans les formulations locales de ces choix. Identifier leur domaine propriétaire, en distinguant capacité à décider, décision produite et autorité opérationnelle. Préserver les noms natifs de marché dans leur provenance. Les rattachements détaillés restent proposés. Promise Verification est rejeté en U92 : la première capacité d’Order Promising doit faire naître une promesse. Promise Formulation était un candidat assistant, rejeté en U93 au profit du candidat Promise Proposal proposé par Laurent ; articulation avec Promise Confirmation à éprouver. U93 demande aussi d’examiner l’acheminement comme chaîne de transport jusqu’à destination, au-delà du choix de source. Fulfillment Route Decision et son propriétaire sont proposés, sans transfert d’autorité C-Log ni extension des développements FLOW. Voir P83/C61/CMP050.

Validation U95 — 2026-09-11, Laurent : les **quatre capacités d’action et cinq capacités de décision d’Order Promising** sont validées, noms courants dans P83 et P81 version 0.5. Ne plus présenter cette liste comme non adoptée ; conserver les réserves détaillées de frontière, d’autorité et d’équivalence marché. Repères D03.d à D03.h ajoutés pour les décisions ; D02.e Supply Assignment conservé. Les autres domaines et le registre CAP36 gardent leurs statuts. **ATP appartient à la promesse ; CTP reste au glossaire, mais son placement est différé.** Analytics opérationnelle pour planification/protection demeure une hypothèse à explorer plus tard ; ne pas poursuivre cette décomposition sans reprise du sujet. Supply Creation Decision reste dans la liste validée, sans imposer CTP comme réalisation. C63/CMP052.

Audit U99 — 2026-09-11 : consulter `audits/2026-09-11-modele-marche-achats-ventes-referentiels.md` avant le prochain arbitrage sur D04 et les référentiels. P86 et Q070–Q073 distinguent variantes achat/vente, référence produit, prix appliqué et consommation des contrats. Le trio U97 reste la carte courante, pas une norme universelle ; aucune proposition de l’audit n’est adoptée automatiquement. C65 conserve cette précaution.

Orientation U100 — 2026-09-11 : la Supply transactionnelle est envisagée de manière générique, orientée documents portant la preuve d’autorisation de déplacement de marchandises ; les parcours achat, vente, après-vente et réassort appartiennent au modèle processus. Le socle décide des actions selon le contexte ; DMN est un exemple, pas une solution choisie. Les deux couches conservent leur métier, leur modèle et leurs moyens de décision/orchestration. Ne pas déduire des modules Purchase/Sales du marché des domaines locaux séparés, ni imposer un domaine Supply ou document universel. La distinction proposée autorisation/engagement d’exécution/fait de réalisation et le lien Party/lieu sont à éprouver ; voir `connaissance/26-supply-documents-autorisations.md` et Q074. D04/D07 restent à refondre sans modifier la validation D03 ni étendre le périmètre logistique FLOW.

U100 confirme également l’autonomie du référentiel article : un SKU peut être proposé dans plusieurs catalogues. Dans la continuité de l’ingestion seule U97, P81 0.7 réactive le sujet D08 sous le nom proposé Product Reference avec D08.d Product Reference Ingestion ; D08.a–c restent retirées. Onze domaines actifs et 35 aptitudes, dont les neuf D03 validées ; noms et frontières non explicitement adoptés restent proposés. D09/D11/D08/D12 forment le groupe contigu des références ; aucune maîtrise produit locale réintroduite. L’audit U99 reste daté ; sa recommandation sur les commandes est réorientée par U100, pas effacée.

Précision U102 — 2026-09-11 : Laurent confirme Party ≠ lieu et demande le référentiel **Fulfillment Network** (orthographe normalisée hors verbatim). P81 0.8 le rend explicite par D13 et l’ingestion proposée D13.a ; le rang de domaine et le regroupement Business References restent ouverts après U101, désormais sur cinq références. Prolonger le principe de réception seule U97 sans attribuer de maître du réseau à FLOW ou C-Log par défaut. D13 décrit les références du réseau ; D06 apprécie les possibilités d’exécution ; D03 conserve les décisions de source/acheminement ; D07 les engagements/faits. Préserver la distinction avec stocks et charge courante, et examiner lieux permanents versus destinations ponctuelles. Contenu, topologie et autorités ouverts INF22/Q076 ; logistique toujours en adhérence. Voir la section D13 de `connaissance/25-domaines-coeur-et-epreuve-recits.md` et CMP060.

Accord U103 — 2026-09-11 : le Go contextuel de Laurent est appliqué au groupe de présentation **Business References**, avec cinq références et cinq ingestions distinctes : Party / Role, Agreement, Product Reference, Catalog, Fulfillment Network. P87 retenue dans cette portée, Q075 résolue ; ne plus présenter le groupe comme une option non retenue. P81 0.9 distingue sept domaines transactionnels de travail et ce groupe dans la vue synthétique, tout en conservant les douze repères détaillés et 36 aptitudes. Aucune fusion des modèles, aucun niveau hiérarchique universel, aucune nouvelle capacité mère. Contenu et maîtres du réseau restent ouverts Q076 ; ne pas étendre le Go aux attributs candidats ou aux autres domaines.

Demande d’expérience U104 — 2026-09-13 : Laurent souhaite une application simple pour explorer et comprendre le modèle, avec recherche directe et possibilité d’accueillir des niveaux d’urbanisme supplémentaires ainsi que documents, objets métier et événements. Concevoir une navigation de profondeur libre ; distinguer regroupements, couches transactionnelle/processus et relations entre notions métier. La demande ne valide aucune hiérarchie supplémentaire ni décomposition automatique capacité → objet → document → événement. Les vues applicatives restent dérivées, datées et reliées aux registres avec leurs statuts et sources. Voir la [proposition FLOW Atlas](prototypes/model-explorer/README.md) ; aucun outil ni hébergement adopté.

Réalisation historique U105 — 2026-09-13 : le Go contextuel de Laurent autorise la construction de l’[application locale FLOW Atlas](app/README.md), initialement lecteur des registres Markdown. Les choix techniques ne valident aucun contenu métier. U106–U111 remplacent cette autorité pour les modèles : la lecture courante provient désormais des JSON backlog, release et panorama-as-is, avec sources documentaires accessibles. Maintenir provenance, date, identifiants stables et réserves. Le prototype U104 reste une démonstration historique. Aucune publication externe n’est comprise dans cet accord.


## Réexamen D01 — U125/U126, 13 septembre 2026

Le backlog sépare désormais les mouvements de stock et leur état résultant, selon U125. D01.e, ancien regroupement, reste historique ; D01.f Inventory Tracking et D01.g Inventory Movements portent la nouvelle proposition. Six capacités D01, 36 au total ; la publication v001 demeure à cinq et 35. Les autres capacités sont conservées. Noms et définitions détaillés restent proposés. U126 ouvre le vocabulaire Ledger, sans adoption : Inventory Ledger Management est une alternative du backlog. Consulter C73/CMP062 avant de reprendre l’ancienne fusion. Aucune réalisation logistique, valorisation financière ou technologie de persistance déduite de cette séparation.


## Nom adopté pour D01.g — U129

Décision de Laurent du 13 septembre 2026 : employer **Record Inventory Movements** pour D01.g dans le backlog. Ce choix remplace les candidats Inventory Movements et Inventory Ledger Management comme noms de capacité. La validation porte sur le nom ; définition, finalité et frontières détaillées restent proposées. Conserver D01.f Inventory Tracking distincte. Lors de la prochaine release, transcrire U129 dans une nouvelle décision du seul champ name pour la révision préparée de D01.g ; aucune publication implicite. Voir C74.


## Cycle de vie courant — U131

Trois statuts sont retenus pour les éléments de la cartographie (domaines, capacités, regroupements, objets, documents, événements et relations) :

- **Proposé par l’IA** (`ai_proposed`) : contenu proposé par Codex, pas encore discuté avec Laurent.
- **En cours d’instruction** (`under_instruction`) : contenu présenté et effectivement discuté ensemble. La seule génération ou présentation ne suffit pas.
- **Validé par l’urbaniste** (`urbanist_validated`) : accord explicite de Laurent, notamment « Go » ou « je valide », dans son contexte.

Enregistrer ce cycle dans `lifecycle`, avec sources, date d’enregistrement et portée. Un Go sur un nom fait passer l’élément à Validé par l’urbaniste pour ce nom : la définition et les autres champs gardent leur statut propre. Les champs validés et leurs empreintes sont conservés ; ne pas étendre l’accord ni l’hériter depuis le domaine parent. Le champ technique `review` et les décisions ADOPT conservent les preuves détaillées ; ils ne constituent pas des étapes supplémentaires du cycle affiché. Les illustrations restent qualifiées comme telles indépendamment du cycle.

Un réexamen discuté replace l’élément en cours d’instruction, en conservant les accords encore applicables. Un amendement proposé par l’IA doit rester une proposition distincte jusqu’à discussion ; ne pas écraser une valeur validée ni transporter son accord sur un nouveau contenu. Les décisions, sources et releases figées gardent l’historique. Pour la reprise initiale, la date enregistrée est la date de migration, pas une date historique inventée.

La seule introduction de `lifecycle` selon U131 ne modifie aucun contenu déjà approuvé : le workflow peut transcrire les accords existants sous de nouveaux identifiants pour la révision suivante, uniquement si le contenu hors lifecycle est strictement identique et si chaque valeur approuvée conserve son empreinte. Il conserve auteur, date et sources d’origine et ajoute la provenance de migration U131. Toute modification métier reste soumise au contrôle habituel ; U131 n’est pas une nouvelle validation métier.

Backlog et release restent indépendants de ce cycle : les trois statuts sont publiables. Les anciennes releases restent immuables et affichent leurs statuts historiques ; les nouveaux libellés s’appliqueront dans Atlas à la prochaine publication qui contient lifecycle. Ne pas assimiler le cycle des éléments de cartographie aux statuts de preuve des faits As Is.


## Retrait de D02 — U145, 14 septembre 2026

Le backlog retire D02 Resource Availability and Commitments et ses capacités résiduelles D02.a/D02.d selon U145. Ne pas renuméroter les autres domaines, ni réutiliser ces identifiants. D02.b/D02.c restent rattachées à Inventory Management (D01) et D02.e à Order Promising (D03) : les préfixes ne définissent pas les parents. Conserver l’état antérieur dans `modeles/backlog/history/pre-U145.json` et la reprise dans `audits/2026-09-14-d02-couverture.md` (C79). Le backlog contient 34 capacités ; v003 conserve son contenu publié jusqu’à une nouvelle release. Le retrait n’adopte pas de nouvelles définitions pour les capacités d’accueil.


## Revue D03 — U147

U147 rouvre ATP/CTP et la complétude des décisions : CTP n’est plus à laisser hors discussion au motif de U95, mais son rang reste à arbitrer. Présenter les actions dans l’ordre Promise Proposal, Promise Confirmation, Promise Revision, Supply Assignment, sans ordre de workflow induit. Aligner progressivement le vocabulaire Case/demande et Order/commande, en distinguant les besoins de simulation ou prévision. Ressource/fourniture, Allocation Eligibility Decision et Supply Creation Decision sont en réexamen ; conserver les valeurs approuvées jusqu’à arbitrage des remplacements. Propositions structurées dans `modeles/backlog/d03-review.json`, appuis et limites dans `marche/revue-d03-decisions-vocabulaire.md`. Aucun ajout automatique de capacité ni publication.


## Granularité des décisions D03 — U151

Laurent retient ATP/CTP/PTP comme niveau des aptitudes de décision à cartographier. Aligner les propositions sur ce niveau métier plutôt que créer une capacité autonome pour chaque choix de source, règle d’allocation ou critère. L’alternative structurée `D03-ALIGNMENT-U151` du backlog propose la recomposition avec Delivery Schedule Decision et les quatre actions conservées. Les règles et choix absorbés restent à documenter ; ne pas supprimer leur couverture. Les définitions nouvelles et cette recomposition détaillée ne sont pas encore validées. Préserver l’écart documenté entre le plan d’adaptation CTP envisagé localement en U148 et les réalisations de marché.


## Adoption D03 et priorité de vocabulaire — U154

U154 valide la recomposition D03 à huit capacités : quatre actions dans l’ordre convenu et quatre décisions D03.i–l (ATP, CTP, PTP, Delivery Schedule Decision). D03.d–h sont retirées, conservées dans `modeles/backlog/history/pre-U154.json`. Cette adoption remplace les mentions historiques de neuf capacités et l’état proposé de U151 ; pas de renumérotation ni de release implicite. Les choix fins restent à documenter dans les aptitudes larges. Le CTP local est le plan d’adaptation U148, avec provenance et écart au marché conservés. Explorer maintenant seulement le point 6 : Requirement/Order et Case/Demand/Command ; le substantif des ressources (point 5) attend. Ne renommer aucun objet automatiquement ni confondre Purchase Requisition et Requirement. Les usages Storeland/ECC rapportés par Laurent restent des déclarations, pas une preuve de déploiement exhaustif.


## Carnet d’Orders — U157

Laurent demande de considérer les Orders comme des éléments d’un carnet qui se travaille : priorisation, découpage, évaluation et engagement. Cette orientation ne fusionne pas Case et Order et ne choisit pas un produit. Le backlog opérationnel est distinct du dossier de conception `modeles/backlog/`. Examiner le recouvrement Backlog Management / Supply Assignment et les capacités D03/D04 par leurs résultats ; ne pas assimiler périmètre produit et définition locale, ni ajouter deux aptitudes redondantes. C82 et `marche/backlog-management-supply-assignment.md` corrigent l’opposition trop simple entre produit de simulation et simple application. Aucun renommage ou fusion adopté.


## Hypothèse de domaine Backlog Management — U158

Explorer Backlog Management comme nom et espace problématique de D03, plutôt qu’ajouter une capacité générale de même nom à côté de Supply Assignment. Option dans `D03-BACKLOG-DOMAIN-U158` ; aucune adoption définitive. Examiner la frontière avec D04 et les résultats de Supply Assignment, dont l’évaluation de scénarios. La simulation peut exprimer une aptitude métier mais son existence comme mode produit ne suffit pas ; éviter les doublons ATP/CTP/PTP. Le découpage U154 reste actif jusqu’à nouvel arbitrage.


## Calcul et simulation — U159

Dans l’exploration D03, ATP/CTP/PTP calculent des solutions ; la simulation mesure leurs impacts au niveau global selon la précision explicite de Laurent. Ne plus la traiter par défaut comme un simple mode ou doublon de ces calculs. Les mécanismes peuvent être partagés, les résultats sont distincts ; les calculs ne sont pas nécessairement limités à une commande isolée. Nom, définition détaillée, indicateurs et rattachement de la capacité de simulation restent à valider.


## Méthode capacités et activité de refinement — U161/U162

Ne pas construire un catalogue de services en transformant les étapes et contrôles nécessaires à l’implémentation des processus en capacités. Partir de ce que sait faire durablement l’entreprise, indépendamment de son organisation et de ses outils. Les fonctions produit servent d’illustrations et d’épreuves, sans imposer la granularité de la carte.

Dans la discussion D03/D04, Laurent emploie grooming au sens de **Backlog Refinement, une activité**, pas une capacité. Order Qualification est retirée des candidats U160 car les vérifications évoquées relèvent ici d’un principe général de contrôle. Le rapprochement Order Structuring/Order Revision et la portée d’Order Prioritization restent en instruction ; aucun nouveau nom validé. Voir [le réexamen](marche/d03-d04-capacites-manquantes.md) et l’annexe JSON des candidats. Ne pas étendre Prioritization à tout le refinement par déduction.


## Adoption Order Prioritization — U163

U163 valide Order Prioritization dans D03 : « Établir et réviser les priorités relatives des commandes. » Le backlog contient désormais D03.m et sa relation explicite à D03, soit neuf capacités dans ce domaine. Nom et définition discutée portent la validation ; finalité et codification de nature ajoutées par Codex restent proposées. Cette décision remplace l’état en instruction d’Order Prioritization mentionné pour U161/U162. Ne pas élargir cette capacité à tout le Backlog Refinement, à la révision du contenu ou à la confirmation de promesse. Le nom de domaine Backlog Management reste une hypothèse. Aucune publication automatique.


## Intentions, Orders et demande d’exécution — U165

Laurent exclut le pattern logiciel Command du contenu métier de la carte. Il réaffirme Order dans Supply et précise la finalité de l’univers amont : faire émerger et affiner les intentions des parties prenantes en demandes ou problèmes à résoudre ; leur résolution mobilise des Orders Supply, laquelle sollicite des plateformes exécutantes. Le nom actuel Case doit être réexaminé car il désigne une mécanique ; aucun remplacement choisi.

Command comme objet métier de demande d’exécution est une hypothèse en instruction, distincte du pattern technique et d’une capacité. Ne pas instancier cet objet, créer un univers Execution, imposer de cardinalité ou renommer des capacités par simple déduction. D07 fournit un point d’appui à éprouver. La logistique reste hors développement FLOW, en adhérence. Voir l’annexe `modeles/backlog/vocabulary-review.json` et l’étude de vocabulaire, complément U165.


## Plateforme exécutante au-delà de la logistique — U167

Laurent confirme que la plateforme de services ne doit pas être enfermée dans la logistique. Étudier la demande d’exécution comme prestation métier générique. Service Order est une proposition de Codex appuyée sur le vocabulaire TM Forum/SAP, sans adoption du nom, schéma, catalogue, domaine ni nouveau modèle d’objets. Les résultats attendus, conditions demandées, prise en charge et faits réalisés restent distincts ; aucune extension du développement FLOW à la logistique n’est déduite.


## Orders contextualisés Supply / Services — U168

Laurent affirme des Orders Supply et des Orders de service, avec des définitions propres aux contextes Supply et Services. Préserver cette frontière sémantique et les contrats explicites entre modèles ; ne pas imposer un Order universel ni un cycle commun. Cette orientation ne valide pas tout le schéma proposé U167. La qualification stricte et la granularité des bounded contexts DDD restent à instruire : ne pas transformer automatiquement univers ou domaines de capacités en bounded contexts, ni créer un univers Services ou un découpage logiciel par déduction.


## Validation de la frontière Supply / Services — U169

U169 valide la distinction des modèles et des Orders contextualisés présentée après U168. Supply Order : commande dont on travaille couverture, priorités et promesse. Service Order : commande de prestations confiées à un exécutant. Supply décide comment satisfaire les commandes ; Services organise et réalise les prestations puis rend compte des résultats. Employer Order localement lorsque le contexte est clair, et Supply Order / Service Order dans les comparaisons et échanges.

Conserver des contrats explicites entre modèles sans objet Order partagé ni cycle commun imposé. Les domaines de capacités sont des espaces problématiques ; les bounded contexts délimitent la validité des modèles. Granularité interne ouverte : aucun univers Services, nouveau type de nœud, objet détaillé, cardinalité ou déploiement n’est créé par cette validation. Les attributs U167 restent proposés. La portée validée et ses empreintes figurent dans `modeles/backlog/vocabulary-review.json`, section `context_boundaries_U168`. Cette section remplace les mentions historiques de nom Service Order seulement proposé. Aucune publication implicite.


## Réexamen Case / Business Processes — U170

Laurent rouvre explicitement le nom et la définition de l’univers Case et propose « Processus métier ? ». Conserver Business Processes comme candidat en instruction, sans renommage automatique. Distinguer le nom d’une couche d’organisation des processus du périmètre métier d’un univers ; Supply et Services possèdent aussi des processus. La définition amont reformulée par Codex porte la prise en charge des intentions, leur précision en demandes/problèmes et leur traitement jusqu’au résultat attendu ; elle reste proposée. État courant et portée dans `modeles/backlog/vocabulary-review.json`, `upstream_universe_review`.


## Offre amont et plateforme Case Management — U171

Laurent précise que l’approche s’appuie sur une plateforme de Case Management pour les processus métier de durée moyenne ou longue qui impactent l’entreprise. L’offre s’adresse aux clients, fournisseurs, partenaires et services internes ; aucun seuil temporel fixé. Codex propose Business Services comme nom d’univers métier amont, sans adoption. Distinguer offre/résultat pour les parties prenantes, processus de traitement et plateforme qui les réalise ; conserver la frontière avec les prestations du contexte Services U169. Cette orientation ne transforme pas les capacités Supply en services applicatifs et n’instancie ni catalogue ni nouveaux objets. Proposition structurée dans `modeles/backlog/vocabulary-review.json`.


## Plateforme des processus transverses — U172

Laurent précise les besoins de la plateforme amont : portail, espaces par utilisateur, management des demandes, planification et affectation des contributions lorsque plusieurs services interviennent, à l’image d’un service desk. Elle doit représenter les grands processus transverses de l’entreprise. Consigner ces besoins dans le modèle processus à construire ; ne pas les transformer automatiquement en capacités Supply ni démarrer un développement de portail.

Distinguer affectation du travail et des responsabilités des équipes, Supply Assignment et planification des contributions versus échéancier de fourniture. Les services organisationnels, l’offre de services métier et les prestations exécutantes ne sont pas synonymes. Business Services reste un nom candidat ; la définition amont actualisée par Codex reste proposée. Voir `upstream_universe_review.platform_scope_U172` dans l’annexe JSON de vocabulaire.


## Business Services adopté — U173

U173 valide **Business Services** et sa définition : « Prendre en charge et piloter les grands processus transverses de l’entreprise, de la demande d’une partie prenante au résultat attendu, en coordonnant les contributions des services et en mobilisant les moyens nécessaires à leur réalisation. » L’univers du backlog garde l’identifiant `universe-case`, passe en révision 2 et porte la validation du nom et de la définition. Son ancien état est conservé dans `modeles/backlog/history/pre-U173.json` et les publications historiques.

Les quatre dimensions présentées — accès des parties prenantes, travail des équipes, coordination, pilotage transverse — sont validées comme descriptions du périmètre dans l’annexe JSON. **Les domaines de Business Services seront travaillés plus tard** : ne pas transformer ces dimensions ou les fonctions du portail en domaines/capacités. Case Management reste l’approche de réalisation et Case peut désigner le dossier ; l’univers s’appelle désormais Business Services. Cette section remplace les mentions antérieures de nom candidat. Aucun renommage du contexte Services exécutant, aucune publication implicite.


## Point 6 clos, point 5 actif — U174

Laurent clôt explicitement le point 6 de vocabulaire et demande de travailler le point 5, consacré au substantif des biens/ressources mobilisés dans Supply. Respecter cette clôture : ne pas rouvrir les alternatives historiques Demand/Requirement, ni en déduire leur validation générale. Les portées adoptées restent conservées. Point 5 à instruire pas à pas à partir de la préférence pour ressource plutôt que fourniture ; aucun remplacement global automatique. Statut de travail dans les annexes JSON `vocabulary-review.json` et `d03-review.json`.


## Point 5 : stock et mouvement — U175

Laurent apprécie Resource comme terme générique mais souligne son sens dépendant du contexte : magasin dans Fulfillment Network, bien transporté, etc. Ne pas adopter la définition restreinte U174 comme définition universelle. Examiner d’abord si les biens stockés et transportés appellent des objets distincts. La proposition de continuité des biens avec représentations distinctes de stock et d’acheminement reste à instruire ; aucun objet ajouté. Point 6 toujours clos. Voir l’annexe de vocabulaire et `marche/ressource-stock-et-mouvement.md`.


## Audit article / SKU / unité logistique — U176

La demande U176 audite les distinctions SAP, Microsoft et GS1 sur le point 5. Ne pas traiter l’hypothèse SKU = unité physique insécable comme validée. Conserver les contextes des noms Material/Product/Article, Item et Stockkeeping Unit. L’audit propose de distinguer référence, quantité/unité de mesure, biens suivis, conditionnement et unité logistique ; ces propositions ne créent ni objets ni capacités. Resource reste générique et contextualisé. Les fonctions d’emballage des produits ne transfèrent pas l’exécution logistique à FLOW ; les références restent ingérées depuis leurs maîtres externes.

Sources et limites : `marche/etudes/2026-09-14-articles-biens-unites-logistiques/`. Résultats structurés : `modeles/backlog/item-logistic-unit-audit.json`. Glossaire complété, C87. Point 6 clos, domaines Business Services différés ; aucun renommage métier ni publication déduit de l’audit.


## Définition SAP Article et lecture du modèle — U181

L’audit U176 est complété par la définition explicite SAP d’une plus petite unité ou d’un conditionnement client commandable indépendamment et non subdivisible. Ne pas remplacer cette définition par notre synthèse référence de gestion. Conserver aussi les catégories SAP génériques abstraites et structurées décomposables ; leur réconciliation par une indivisibilité commerciale contextuelle reste une interprétation. Voir C89 et marche/etudes/2026-09-14-articles-biens-unites-logistiques/article-definition-comparison.md. Cela ne valide ni le sens universel de SKU ni un nouveau terme du modèle local.


## Exploration guidée par le stock unifié — U187

Laurent demande de revenir aux entités en partant du modèle de stock unifié. Les références d’article seules ne suffisent pas ; prendre en compte les conditionnements des flux Inbound et Outbound, qui peuvent différer. Ces deux termes sont une préférence utilisateur explicite. L’exploration ciblée est consignée dans modeles/backlog/unified-inventory-packaging.json et connaissance/28-stock-unifie-et-conditionnements.md. L’orientation ne valide pas automatiquement les noms Container/Logistic Unit, le schéma ou les relations proposés par Codex. L’inventaire exhaustif reste différé ; les propositions n’instancient pas d’objets dans la carte. Préserver la responsabilité externe de l’exécution logistique et des référentiels.


**Précision U188 :** le modèle de stock unifié doit permettre le reconditionnement des contenants entrants pour le stockage et la création des contenants outbound au moment du packing. Ne pas présumer une identité ou une composition inchangée entre entrée, stockage et sortie. L’orientation est conservée dans l’annexe U187 ; les entités détaillées, leurs relations et responsabilités proposées restent à instruire. La logistique exécutante demeure en adhérence de FLOW.


**Précision U189 :** dans le modèle local, prendre en compte le packing contractuel dans la promesse ATP d’une commande B2B ; ne pas assimiler stock présent et livraison conforme réalisable. La constitution à la volée des containers U188 ne dispense pas d’évaluer le conditionnement attendu avant la promesse. Les rôles proposés D11/D04/D06/D03/D07 restent à instruire ; aucune nouvelle capacité ou définition éditeur n’est adoptée par déduction.


## Première structure d’entités du stock unifié — U190

Laurent propose Product, Article ou Product Unit, Container et Container Unit, avec références de design, localisation directe et contenants imbriqués. L’exploration ciblée des objets est désormais explicitement en cours dans la feuille de route, sans inventaire exhaustif ni instanciation prématurée dans la carte. Conserver la distinction entre proposition utilisateur, précision de grain à obtenir et libellés proposés par Codex. Ne pas déduire une sérialisation ou une indivisibilité d’un code-barres ; ne pas créer un univers Design ni transférer la maîtrise des références à FLOW par cette mention. Voir modeles/backlog/unified-inventory-packaging.json, entity_structure_review, et connaissance/28-stock-unifie-et-conditionnements.md.


**Clarification U191/U192 :** Article/Product Unit désigne chaque exemplaire physique avec son identité propre ; cette question de grain est tranchée et ne doit pas être reposée comme ouverte. Laurent confirme l’indépendance vis-à-vis du code-barres. Préserver cette portée explicite sans valider automatiquement tous les noms, liens, identifiants ou mécanismes de traçabilité. Les références et unités concrètes restent des concepts en exploration dans l’annexe ; aucune création automatique d’univers Design ou de maîtrise locale des référentiels.


**Précision U193 :** Product Unit peut porter un Serial Number, indépendant du support code-barres. Product Variant est introduit comme niveau auquel rapprocher le GTIN de référence commerciale. La structure Product/Variant/Unit reste en instruction dans l’annexe du stock unifié ; le grain individuel U191 reste acquis. Ne pas imposer de série fabricant, de GTIN ou de support particulier à toute unité, ni de bijection variante/GTIN : distinguer les conditionnements commerciaux et l’identité du contenant physique.


**Décision U195 :** Product est le concept commun et porte un rôle **Article** ou **Container**. Retenir le choix du rôle au niveau Product, sans imposer deux familles indépendantes de référentiels. Product Unit conserve le grain individuel U191 ; Article devient un nom de rôle, non l’alternative courante au nom générique Product Unit. Principe et noms validés, définitions détaillées et multiplicité des rôles encore ouvertes. Les anciennes hypothèses U190/U194 sont historiques sur ces points. Portée dans `modeles/backlog/unified-inventory-packaging.json`, `entity_structure_review.product_roles_decision`.


**Besoin U196 :** les textes du modèle (libellés, descriptions, etc.) doivent pouvoir référencer explicitement des notions du glossaire. Proposition JSON dans `modeles/backlog/glossary-text-references.json` : segments de texte et identifiants stables, glossaire figé par publication, liens lexicaux distincts des relations métier. Ce contrat reste proposé ; les champs actifs sont encore des chaînes et le glossaire documentaire n’est pas encore migré. Ne pas annoncer les liens Atlas comme disponibles ni déduire une validation des définitions par leur référencement.


**Précision U197, remplace le format proposé U196 :** conserver les textes en chaînes JSON lisibles ; Laurent écarte les tableaux de segments au profit d’une syntaxe légère de type Markdown. Proposition courante : `[texte affiché](glossary:IDENTIFIANT)`. Identifiants stables et glossaire figé par publication restent les principes proposés. La syntaxe exacte et son parseur ne sont pas encore validés/implémentés ; ne pas présenter les liens Atlas comme disponibles. Historique et contrat courant dans `modeles/backlog/glossary-text-references.json`.

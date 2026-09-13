# Audit de structure et reprise des modèles

13 septembre 2026 — audit demandé par Laurent en [U106](../connaissance/01-contributions-utilisateur.md#u106), précisé par [U107](../connaissance/01-contributions-utilisateur.md#u107), [U108](../connaissance/01-contributions-utilisateur.md#u108) et [U109](../connaissance/01-contributions-utilisateur.md#u109). La précision [U111](../connaissance/01-contributions-utilisateur.md#u111) demandant de publier toutes les capacités dans la release s’applique à la publication ; elle ne constitue pas leur validation métier.

## Conclusion et portée

Le projet dispose d’une connaissance riche et traçable, mais le modèle initial était réparti entre des tableaux Markdown, les qualifications de l’application et une configuration d’exploration contenant aussi des objets et relations métier. Cette organisation ne permettait pas de distinguer proprement une version publiée, ses validations partielles, les alternatives en réflexion et les descriptions de SI existants.

La séparation retenue est **backlog / release / panorama-as-is**, avec des données JSON faisant autorité pour les modèles. Les Markdown conservent la capture des contributions, les récits, les raisonnements, les comparaisons, les réserves et les restitutions. Une extraction depuis ces documents constitue une opération de reprise datée ; elle ne doit pas devenir une synchronisation permanente de deux modèles éditables concurrents.

**La release publie le modèle courant, y compris les capacités non validées.** Chaque élément conserve son statut et la portée de ses validations. Le nombre de capacités publiées n’est donc pas le nombre de capacités validées. Les alternatives et illustrations ne sont pas automatiquement incorporées à cette publication.

Cet audit examine les artefacts et leur traçabilité. Il ne vérifie ni les installations Beaumanoir, ni les interfaces par observation, ni la fraîcheur des configurations au 13 septembre 2026. Les résultats de contrôle applicatif final doivent être distingués des contrôles d’extraction déjà réalisés ci-dessous.

## Constats dans l’organisation initiale

Les localisateurs de code de cette section désignent la version examinée avant adaptation du lecteur. Les fichiers applicatifs peuvent ensuite changer de rôle ; ces constats décrivent l’état initial, pas un défaut nécessairement encore présent après la migration.

| Constat | Preuve examinée | Conséquence pour la structure |
| --- | --- | --- |
| Les capacités courantes sont définies dans un document de travail. | [P81](../connaissance/25-domaines-coeur-et-epreuve-recits.md) ; ancien lecteur `app/atlas_data.py`, constante `MAP_PATH` et fonction `_parse_map`, lignes 21 et 163–240 de la version auditée. | La ponctuation, les titres et le format des tableaux participaient au contrat de données. Une rédaction éditoriale pouvait changer ou casser l’extraction. |
| Les qualifications sont dans un autre fichier que les définitions. | [model-metadata.json](../app/model-metadata.json) ; ancien `load_model`, lignes 250–291. | Les textes et rattachements venaient du Markdown ; les statuts, réserves et synthèses des domaines venaient du JSON applicatif. |
| La configuration d’interface contient aussi du métier. | [ancienne configuration conservée](../app/legacy/exploration-before-json.json), objets illustratifs et huit relations. | Les objets, documents, faits et relations doivent rejoindre le modèle structuré avec leur statut. Icônes et parcours d’aide relèvent de la présentation. |
| Le prototype contient une copie datée de la carte de travail. | [model-snapshot.json](../prototypes/model-explorer/model-snapshot.json) et [note du prototype](../prototypes/model-explorer/README.md). | Cette démonstration ne constitue pas une release validée et ne doit pas redevenir une source de repli. |
| Un statut unique résume des validations de portée différente. | `status` / `statusNote` dans les métadonnées ; ancien `statusInfo`, `app/app.js`, lignes 49–57. | Un nom adopté, un rattachement retenu, une liste validée et une définition proposée ne peuvent pas être réduits au même booléen. |
| L’application conservait les statuts précédents après une modification de texte, avec une alerte de relecture. | Ancien `metadataReviewRequired`, `app/atlas_data.py`, lignes 272–291. | Cette alerte prévient le lecteur, mais ne conserve pas la valeur exacte antérieurement validée. Il faut versionner les objets et les décisions. |
| Les liens de démonstration n’ont pas d’identifiant stable. | Huit relations de `app/exploration.json` ; identifiant alors facultatif dans `app/model.js`, lignes 103–104. | Une relation doit pouvoir être discutée, adoptée, révisée ou retirée en tant que telle. |
| Le panorama est mélangé à des orientations de cible dans certains registres. | [INF18–22](../connaissance/10-autorites-information.md#inf18) et [DEC21–22](../connaissance/11-responsabilites-decision.md#dec21). | Leur extraction dans une carte de l’existant donnerait à tort l’apparence d’une réalisation installée. |
| Les tests du moteur initial utilisent le snapshot du prototype. | `app/test-model.mjs`, ligne 6 de la version auditée. | Ils protègent la navigation, mais ne suffisent pas à vérifier le contrat du nouveau modèle courant. |

L’empreinte de P81 correspondait à celle de `model-metadata.json` lors de cet audit : le problème relevé est un problème de structure et de maintenance, pas une désynchronisation alors constatée.

Plusieurs garanties initiales doivent être conservées : refus d’un extrait invalide sans retour silencieux au prototype, identifiants indépendants de leurs préfixes historiques, absence de profondeur imposée à la navigation et séparation du graphe métier de la hiérarchie de présentation. **D02.e était correctement rattachée à Order Promising ; D02.b et D02.c à Inventory Management.** Aucun défaut de rattachement n’a été constaté sur ces repères.

## Structure documentaire et autorité des données

| Emplacement | Rôle durable | Règle d’évolution |
| --- | --- | --- |
| [modeles/backlog/model.json](../modeles/backlog/model.json) | Modèle en réflexion, alternatives, propositions, illustrations et éléments déjà acquis replacés dans leur contexte. | Les propositions évoluent ici ; une modification ne vaut pas validation. |
| [modeles/release/current.json](../modeles/release/current.json) | Pointeur vers la dernière publication du modèle courant. | La version publiée demeure explicite ; le pointeur ne contient pas un deuxième modèle éditable. |
| `modeles/release/<version>/` | Modèle publié et manifeste de provenance. | Une version différente nécessite un nouveau répertoire. La publication conserve les statuts, y compris non validés. |
| `modeles/revisions/<version>/` | État du backlog utilisé pour une publication. | Conserver le contenu ayant servi à produire la release et ses empreintes. |
| `modeles/decisions/` | Décisions et portée des validations associées aux éléments. | Auteur, date, source et portée doivent être distingués de la version technique du schéma. |
| [modeles/provenance/source-records.json](../modeles/provenance/source-records.json) et captures versionnées | Index des sources et textes capturés. | Les captures liées à une release restent conservées ; une nouvelle analyse enrichit une nouvelle capture ou l’index courant. |
| [modeles/panorama-as-is/current.json](../modeles/panorama-as-is/current.json) | Index des trois panoramas et du contexte partagé. | La date de consolidation décrit l’état de connaissance, pas une observation des déploiements. |
| [modeles/backlog/panorama-candidates.json](../modeles/backlog/panorama-candidates.json) | Mentions à instruire, besoins et orientations exclus de l’existant décrit. | Un passage dans l’As Is exige une preuve et un périmètre adaptés. |
| `modeles/schemas/` | Contrats de structure et types des enregistrements. | Faire évoluer le schéma explicitement, avec contrôle des anciens états et des références. |
| `connaissance/`, `marche/`, `audits/` | Sources, récits, analyses, comparaisons, corrections et restitutions. | Les tableaux historiques restent lisibles, mais ne doivent plus concurrencer le modèle JSON courant. |
| `app/` | Lecture et présentation des modèles. | Consommer les contrats JSON ; ne pas conserver une deuxième qualification métier éditable dans la présentation. |
| `archive/` et `prototypes/` | Provenance d’origine et historique des expériences. | Ne pas les synchroniser avec la carte courante. |

JSON a été choisi pour la reprise : les contrats existants de l’application utilisent déjà ce format et les outils de contrôle peuvent le lire directement. Ce choix évite de maintenir deux formats de données faisant simultanément autorité. Il ne prescrit aucune technologie d’application ni base de données.

Les espaces backlog, release et panorama sont distincts des couches d’urbanisation transactionnelle et processus. Un élément de backlog peut relever de l’une ou l’autre couche. Un panorama décrit une réalisation ou une mention de SI, sans transformer son arborescence applicative en décomposition de capacités.

## Reprise du modèle d’urbanisme et portée de la release

La reprise du backlog contient **53 nœuds** : 36 capacités, sept domaines transactionnels de travail, cinq références, le groupe Business References et quatre éléments illustratifs — deux objets, un document et un événement. Les alternatives P82 et P84 sont conservées séparément. Les 36 fiches CAP historiques restent une autre nomenclature de travail ; leur reprise de provenance ne crée pas une équivalence automatique avec les 36 lignes actives de P81.

La première compilation `2026-09-13.1` avait appliqué une lecture restrictive du mot release : 25 nœuds, dont 17 capacités portant au moins une validation ou orientation retenue. Elle reste historique. La précision suivante de Laurent demande de publier la carte courante entière avec ses statuts.

La publication complète sous **`2026-09-13.2`** contient donc **49 nœuds et les 36 capacités** : neuf capacités validées, huit portant des validations partielles et dix-neuf non validées. Les quatre illustrations restent dans le backlog. La release est une photographie publiée de ce modèle, pas une affirmation que ses 49 nœuds sont validés. Les contrôles finaux de cette publication et de son lecteur sont consignés ci-dessous. Les statuts affichés distinguent 9 capacités validées, 7 partiellement validées, 8 non validées et 12 en réexamen ; parmi ces dernières, Reservation conserve son nom adopté.

Cette séparation doit rester visible dans le modèle et les restitutions :

- **Publication** : cet élément figure dans la version de référence consultable.
- **Validation** : une décision identifiée porte sur l’élément ou sur certains de ses champs et relations.
- **Réserve** : les limites de frontière, d’autorité, de définition ou d’équivalence restent ouvertes dans leur portée exacte.

Par exemple, adopter le nom Stocktaking ne valide pas automatiquement toute la décomposition d’Inventory Management. De même, le regroupement Business References ne crée ni capacité mère ni domaine fusionné. La validation U95 des capacités d’Order Promising ne transforme pas les objets et faits illustratifs de l’exemple de promesse en modèle détaillé validé.

## Reprise du panorama As Is

L’extraction lit intégralement les quatre registres [composants](../connaissance/07-composants.md), [flux](../connaissance/08-flux.md), [autorités sur les informations](../connaissance/10-autorites-information.md) et [responsabilités de décision](../connaissance/11-responsabilites-decision.md), avec les corrections pertinentes. Elle conserve leurs **85 repères** : 20 composants ou mentions, 21 flux, 22 entrées INF et 22 entrées DEC.

| Destination | Objets ou mentions | Flux | INF | DEC | Portée |
| --- | ---: | ---: | ---: | ---: | --- |
| [Périmètre historique de Beaumanoir](../modeles/panorama-as-is/beaumanoir-historique/versions/2026-09-13.1/panorama.json) | 14 | 17 | 14 | 15 | Fonctionnement partiellement décrit, réserves conservées. |
| [Boardriders](../modeles/panorama-as-is/boardriders/versions/2026-09-13.1/panorama.json) | 3 | 0 | 0 | 0 | Composants ou solution cités ; couverture détaillée non établie. |
| [Sarenza](../modeles/panorama-as-is/sarenza/versions/2026-09-13.1/panorama.json) | 0 | 0 | 0 | 0 | `not_assessed`, conformément à U109. |
| [Contexte partagé C-Log](../modeles/panorama-as-is/shared-2026-09-13.1.json) | 2 | 3 | 2 | 4 | Frontière et contexte partagé ; ce n’est pas un quatrième SI. |
| [Candidats du backlog](../modeles/backlog/panorama-candidates.json) | 1 | 1 | 6 | 3 | Besoins, orientations ou mentions à instruire. |
| **Total conservé** | **20** | **21** | **22** | **22** | **85 identifiants uniques.** |

Les onze enregistrements du backlog sont conservés intégralement :

- **INF18–22** : maîtrise externe des cinq références envisagées pour la plateforme ; ce sont des orientations, sans preuve de déploiement.
- **DEC21–22** : besoins Boardriders sur les ressources futures et la révision prioritaire des engagements ; les réalisations installées ne sont pas établies.
- **DEC20** : responsabilité non localisée, issue de propositions et questions. La précision C32 sur le principe de réservation au passage de commande reste associée, sans inventer son réalisateur.
- **SI-SAR, FL21 et INF17** : mentions initiales Sarenza, à instruire. Elles ne sont pas présentées comme un panorama déjà traité.

Chaque fiche conserve `source_fields` et `source_record_text` sans réécriture des formulations historiques. Les champs de lecture utilisent les libellés canoniques. Les objets sont typés pour distinguer organisation, application, famille d’applications, ensemble, plateforme technique et mention non rapprochée.

Ainsi, ORG-CLOG reste une organisation ; la mention « SI C-Log » dans un flux n’est pas résolue artificiellement vers cet identifiant comme s’il s’agissait d’un logiciel. APP-AFS reste une mention de solution et fonctionnalité, avec périmètre de déploiement non établi. ALIAS-ACH ne crée pas un composant supplémentaire réputé distinct de MAP ou CBS.

Les **26 extrémités de flux non résolues** restent exprimées par leur libellé source, avec identifiant nul. FL03 reste une dépendance fonctionnelle ; sa présence ne prouve pas une interface directe entre IRMA et Storeland. Les interfaces, messages, fréquences ou responsabilités manquants ne sont pas complétés par déduction.

Tous les enregistrements portent `observed_at: null`. `as_of: 2026-09-13` est la date de publication de l’état de connaissance. Aucun enregistrement n’est promu au niveau de preuve `observed` à partir d’un récit. Les réserves sur les versions, marques, périodes de déploiement et autorités restent applicables.

Le contexte partagé est lui-même versionné dans `shared-2026-09-13.1.json` ; l’index et les trois panoramas le référencent avec son empreinte. Son partage n’affirme pas une interface avec chacun des trois SI.

## Traçabilité et anomalie de bornage DEC22

Une comparaison stricte a identifié une différence de longueur entre la fiche DEC22 et sa capture dans l’index général des sources. La fiche panorama contient **435 caractères** ; la capture générale en contient **1 341**. Les 435 premiers caractères sont identiques, puis la capture générale inclut la section de même niveau « Frontière des décisions et des référentiels — U97/U98 ».

La cause est la différence entre deux règles de bornage : l’extracteur du panorama s’arrête au prochain titre de section, tandis que la capture générale initiale s’arrêtait au prochain titre portant un identifiant reconnu. Le dernier identifiant du document absorbait donc la section de contexte suivante. **Aucun champ de DEC22 n’a été perdu.**

Le correctif recommandé au contrôle consiste à retrouver la section identifiée à l’intérieur de la capture et à la borner au prochain titre de niveau inférieur ou égal avant comparaison. Le texte capturé et son empreinte historiques doivent rester intacts. Un simple test de préfixe serait insuffisant, car il accepterait aussi une fiche tronquée. Les futures captures peuvent appliquer directement le bornage par structure Markdown. Le validateur commun applique désormais ce bornage et contrôle le texte capturé et son empreinte sans les modifier.

## Contrôles et limites de cette livraison

La précision U112 ajoute une préparation de structure : feuille de route JSON, distinction du futur niveau sémantique et des groupes de présentation, qualification des relations et registre d’applicabilité pour les trois SI et FLOW cible. Les schémas acceptent les objets/documents/événements et les relations capacité → capacité ou entité métier, avec sens explicite. Aucun nouveau niveau nommé Universe, objet ou lien réel n’est créé. Les évaluations sont vides et ne valent pas absence de couverture ; l’épreuve actuelle reste centrée sur domaine/capacité. La release .2 gelée n’est pas réécrite par cette préparation.

| Contrôle | Résultat constaté à la rédaction |
| --- | --- |
| Relecture des quatre registres panorama et corrections pertinentes | Réalisée ; classement individuel des INF et DEC, exclusion des besoins et orientations de cible. |
| Conservation des repères et champs panorama | 85 repères uniques ; égalité des `source_fields` avec les champs extraits ; aucun repère perdu ou dupliqué. |
| Références aux sections source | 85 localisateurs vérifiés. |
| Intégrité des fichiers pointés par l’index panorama | Cinq empreintes vérifiées : trois panoramas, contexte partagé et candidats. |
| Extrémités de flux | Références identifiées résolues ; 26 libellés non résolus conservés explicitement. |
| Reproductibilité de l’extraction panorama | `python -B scripts/extract_panorama.py --check` réussi. |
| Protection des versions du panorama | Modifications simulées d’une version Boardriders et du contexte partagé rejetées avant écriture. |
| Ajout d’analyse sans incidence métier | Ajout simulé d’une correction non liée : extraction gelée inchangée, sans écriture de fichiers de test. |
| JSON de backlog initial | 53 nœuds lus ; 36 capacités et quatre illustrations distinguées. |
| Validation commune des schémas, statuts et décisions | `scripts/validate_models.py` réussi sur la release .2 ; validations par champ, preuves et entrées gelées contrôlées. Tests négatifs de fausse validation, valeur modifiée, identifiants, références, cycles et isolation du backlog réussis. |
| Lecture applicative des espaces JSON et navigation | 15 tests Python (un ignoré pour lien symbolique non autorisé), 8 tests JavaScript, parcours navigateur des trois espaces réussis. Largeurs 375/768/1360 px sans débordement, zéro erreur JavaScript. |

Le [script d’extraction du panorama](../scripts/extract_panorama.py) est une reprise qualifiée et reproductible, pas un outil de découverte automatique du SI. Un changement dans les fiches ou leurs corrections liées exige une nouvelle qualification et une nouvelle version. Les empreintes globales des documents sources décrivent la capture initiale : un ajout d’analyse ailleurs dans un registre ne doit pas réécrire les versions gelées.

Le [script de reprise de l’urbanisme](../scripts/migrate_urbanism.py) est également un outil de migration. Après reprise, les évolutions des modèles doivent être faites dans les JSON courants, avec décisions, sources et restitutions adaptées ; l’application doit lire ces données plutôt que reparcourir les tableaux Markdown à chaque requête.

Restent à approfondir sur le fond : les dix-neuf capacités non validées, les frontières et autorités des capacités partiellement validées, la refonte D04/D07, le périmètre exact de Reservation, les contenus et maîtres détaillés des références et le modèle processus. Leur visibilité dans une release ne les clôt pas. CTP conserve son placement différé et la logistique reste hors développement de la plateforme FLOW, en adhérence avec le SI autonome de C-Log.


Clôture des contrôles : **44 tests des contrats, de l’intégrité, de la publication et des extensions U112 réussis** ; validateur global sans erreur. Il retrouve 36 capacités dans chacun des deux espaces, 47 adoptions, 85 repères de panorama, quatre contextes d’applicabilité et zéro évaluation inventée. Les contrôles applicatifs sont indiqués dans le tableau ci-dessus. Les 159 liens locaux examinés sont résolus ; les trois originaux ChatGPT conservent leurs empreintes initiales. Le serveur principal FLOW Atlas a été redémarré et sa nouvelle API de schéma 2 vérifiée.

Le backlog courant 2026-09-13.2 reprend explicitement les neuf statuts accepted d’Order Promising. La correction porte sur leur qualification, sans changement des champs ou de leurs révisions ; les instantanés et releases gelés restent intacts.

# U464 — Information : sens métier et granularité

La notion recherchée se situe à la rencontre de **l’Information Concept** de l’architecture métier et de **l’élémentarité** de la modélisation sémantique. Aucune des sources consultées ne définit exactement *Information* comme « groupe minimum de données insécables explicitant une capacité ». Cette formulation peut devenir une convention FLOW, en distinguant son fondement de son adaptation locale.

## Définition proposée

> Ensemble minimal d’éléments qui, reliés dans un contexte donné, portent un sens métier déterminé et explicitent ce qu’une capacité connaît, utilise, produit ou fait évoluer.

> L’information est décrite indépendamment de sa représentation informatique. La cartographie des informations métier ne constitue pas un modèle de données implémentable.

Le nom retenu dans la proposition est **Information**, libellé français **Information métier**, repère **MOD012**. Cette rédaction et son critère de granularité restent proposés ; la demande U464 ne vaut pas validation anticipée de ces phrases.

## Ce que disent les références

| Référence effectivement consultée | Notion et apport | Limite pour FLOW |
| --- | --- | --- |
| [ISO/IEC 15944-1:2025](https://www.iso.org/obp/ui?_escaped_fragment_=iso:std:iso-iec:15944:-1:ed-3:v1:en), §3.13 et §3.29, reprenant ISO/IEC 2382:2015 | L’information porte une signification dans un contexte ; les données en sont une représentation. | Ne pose pas une maille minimale de cartographie. |
| [ISO 20691:2022](https://www.iso.org/obp/ui?_escaped_fragment_=iso:std:iso:20691:ed-1:v1:en), §3.10 | *Data element* : « unit of data that is considered in context to be indivisible ». Le numéro de téléphone illustre une divisibilité différente selon le contexte. | Concerne l’organisation des données ; ce n’est pas un synonyme automatique d’Information métier. |
| [OMG SBVR 1.5](https://www.omg.org/spec/SBVR/1.5/PDF), §24.2.1 p.222 et §24.2.2.1 p.255 | Un fait élémentaire ne se décompose pas en faits plus simples conservant ensemble le même sens dans le schéma considéré. | Critère logique plus strict que l’utilité ou la cohérence d’une fiche. |
| [Terry Halpin — What Is An Elementary Fact?](https://www.orm.net/pdf/ElemFact.pdf), 1993, pp.2–3 et 6–8 | La décomposition dépend aussi des contraintes ; un regroupement intuitif n’est pas nécessairement élémentaire. | Pas de preuve d’atomicité par le seul choix d’un nom comme Commande ou Engagement. |
| [TOGAF G190 — Information Mapping](https://governance.foundation/assets/frameworks/togaf/g190%20-%20Information%20Mapping.pdf), 2019, chap.1–2 et 4–6 | Les concepts d’information explicitent le vocabulaire métier et se relient aux capacités. | Des concepts larges comme Client ou Produit ne sont pas nécessairement minimaux. |
| [Business Architecture Guild — Metamodel Guide v3.0](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf), 2024, §5.3–5.3.1 | Les capacités utilisent et modifient des concepts d’information. La carte métier se distingue du modèle IT. | Ne pas importer toute la taxonomie ni sa correspondance objets–capacités. |

Les passages sont paraphrasés, sauf la courte citation signalée. Consultation : **19 septembre 2026**. Les entrées ISO sont officielles mais ne constituent pas une lecture intégrale des normes citées ; G190 est un document primaire de 2019 lu sur un miroir tiers, sans prétendre vérifier toute la 10e édition. Les autres PDF sont publiés par leur organisme ou auteur. Aucune copie des normes ou guides n’est redistribuée.

## Comment comprendre « minimal » et « insécable »

La proposition retient un **minimum relatif à une question métier explicite**. Elle exige de préserver les éléments et leurs liens nécessaires à ce sens. Elle ne revendique pas leur irréductibilité logique au sens de SBVR/ORM : celle-ci demanderait une analyse plus formelle des règles du métier.

Ce choix est délibéré. Réduire toute la carte à des faits élémentaires pourrait la rendre beaucoup plus fine que les responsabilités qu’elle doit expliquer. À l’inverse, appeler Information n’importe quel dossier ferait perdre le critère de minimum demandé. Une Information doit répondre à une question identifiable ; plusieurs sens autonomes se décrivent séparément et se relient.

**Exemple repris des échanges sur la promesse (U441/U443).** Une ligne demande 100 pièces. L’engagement prévoit 60 pièces le 25 septembre et 40 le 28 septembre. Pour comprendre ce qui est promis, il faut conserver chaque association entre ligne, quantité, unité et date. Deux listes indépendantes « 60, 40 » et « 25, 28 » perdraient ces associations. L’échéancier contient toutefois deux échéances ; cet exemple ne démontre pas qu’il constitue un fait élémentaire unique.

Les données peuvent être stockées séparément et reliées tout en conservant exactement ce sens. **La cohérence sémantique n’impose donc ni un enregistrement unique ni une mise à jour technique indivisible.** Le modèle décrit des types d’information ; les quantités et dates du cas illustrent des occurrences.

Un bon contrôle de maille consiste à vérifier :

1. Quelle question métier cette Information permet-elle de comprendre ?
2. Quel contexte et quels liens sont nécessaires pour éviter une ambiguïté ?
3. Quels éléments sont superflus pour cette question, ou expriment un autre sens autonome ?
4. Quelles capacités la connaissent, l’utilisent, l’établissent ou la font évoluer ?

## Frontières à conserver

Une commande est un objet métier ; ses quantités demandées, les engagements et les réalisations portent des informations distinctes. Un document peut en formaliser plusieurs. La capacité décrit ce que l’entreprise sait faire ; l’Information en explicite le contenu. Aucune bijection avec une table, un document ou une capacité n’est imposée.

Le **fait élémentaire** de la logique ne se confond pas avec le **fait de gestion** FLOW. La convention U461 continue d’associer chaque fait de gestion à un document identifié ; elle n’impose pas un document propre à chaque propriété descriptive. Information ne devient pas non plus un sous-niveau de Comportement.

Les informations de référence peuvent préciser leurs autorités et sources d’alimentation métier. Ces précisions n’attribuent pas à Supply la maîtrise de données externes et ne désignent aucun système installé sans preuve.

## Alternatives et recommandation

| Option | Intérêt | Compromis |
| --- | --- | --- |
| Information Concept | Vocabulaire établi de l’architecture métier. | Trop large pour garantir seul ton exigence de minimum. |
| Elementary Fact | Correspondance théorique précise avec l’irréductibilité logique. | Maille potentiellement trop fine ; risque de confusion avec le fait de gestion. |
| **Information, avec convention FLOW explicite** | Conserve le nom et l’objectif demandés, le sens, le contexte et les usages par les capacités. | Nécessite une justification de la maille sur chaque cas, sans prétendre être une définition normative universelle. |

Je recommande la troisième option. Si l’objectif devient une irréductibilité logique stricte, ce sera un choix de méthode à arbitrer : il ne faut pas le déduire de cette rédaction. La prochaine étape concrète est d’éprouver la maille sur les cinq pilotes déjà préparés avant d’introduire de nouveaux nœuds ou relations dans le catalogue.

## Intégration et contrôles

La proposition est inscrite dans [le glossaire méthodologique](../../modeles/backlog/modeling-glossary.yaml), MOD012, et reprise dans le **brouillon** du guide destiné à une future publication. L’[analyse structurée](../../modeles/backlog/information-definition-U464.yaml) conserve sources, différences et critères ; le suivi des pilotes renvoie à cette proposition.

Le modèle métier, son glossaire, son schéma et les publications restent inchangés. Atlas ne lit pas ce brouillon tant qu’un guide n’a pas été publié puis associé explicitement à une release. Les résultats des contrôles sont conservés dans [verification.json](verification.json).

Validation modèle : **0 erreur**. Guide futur validé directement, définition cohérente entre les trois documents structurés, sources résolues. Tests du lecteur de guide : **17 réussis, 1 ignoré** car Windows n’autorise pas ici la création de liens symboliques. Les 11 termes méthodologiques antérieurs et les 303 fichiers historiques protégés sont inchangés ; les empreintes du catalogue métier, du glossaire métier et du schéma sont également identiques. L’appel initial des tests par module a échoué sur un import local ; leur point d’entrée `python app/test_modeling_guide.py` a permis le contrôle complet hors du seul cas ignoré.

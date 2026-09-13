# TOGAF, ArchiMate et BIZBOK : structures et capacités

Note de recherche du 9 septembre 2026, Codex, pour l’étude comparative demandée par Laurent. Périmètre : MKT01–MKT03 du [catalogue](../../catalogue.md). Méthode : [qualification des correspondances](../../methode.md). Lecture ciblée ; aucune adoption de standard ou validation de capacité Beaumanoir.

## Résultat de la comparaison

**Ces trois références ne sont pas trois catalogues concurrents de capacités commerce.** TOGAF apporte une méthode d’architecture ; ArchiMate, un langage pour représenter ses objets et relations ; BIZBOK, des pratiques d’architecture métier assorties de modèles de référence. La distinction entre méthode TOGAF et langage ArchiMate est explicitement corroborée par la [présentation officielle Open Group, §§1–3](https://help.opengroup.org/hc/en-us/articles/32115987894930-How-the-ArchiMate-Language-and-the-TOGAF-Standard-Complement-Each-Other).

| Référence examinée | Structure observée | Ce que cela permet de comparer |
| --- | --- | --- |
| TOGAF, guide historique G189, 2018 | Capacités de niveau 1, décomposées en capacités plus fines ; classement transversal distinct | Règles de construction et profondeur, pas une nomenclature retail imposée |
| ArchiMate, spécification historique 3.1, 2019 | Type `Capability`, relations entre éléments ; pas de chaîne native Enterprise Domain / Business Domain / Business Area | Sémantique des objets et des liens, distincte du contenu d’une carte |
| Guild, atelier public 2019 | Objets métier et actions ; deux axes séparés, `Tier` et `Level` | Cohérence de décomposition, réutilisation des concepts et regroupements |
| Guild, position paper BPM 2014 | Capacités, processus et flux de valeur rapprochés par des relations | Différences de sémantique et correspondances plusieurs-à-plusieurs |

Les dates sont celles des éditions examinées ; elles ne désignent pas leurs versions actuelles. Les deux documents historiques Open Group ont été lus sur un **hébergement tiers**, avec auteur, titre et édition identifiés dans le document. Leur conformité au fichier actuellement distribué par l’éditeur n’a pas été vérifiée.

## TOGAF : niveaux adaptables et classement distinct

Dans **G189**, une capacité décrit une aptitude durable de l’entreprise, indépendamment de l’organisation et des moyens qui la réalisent. Le guide distingue :

- **Stratification** : regroupements généralement stratégique, cœur et support.
- **Leveling** : décomposition d’une capacité en capacités plus détaillées, adaptée aux destinataires et aux décisions. Trois à six niveaux sont présentés comme pratique fréquente, sans maximum obligatoire.

Le guide recommande des noms compréhensibles et une définition précise ; sa préférence grammaticale pour des noms composés anglais n’est pas une preuve qu’un libellé français à l’infinitif serait un processus. Ses exemples illustrent la méthode et ne constituent pas un catalogue commerce. [Document primaire Open Group G189, copie externe, §§2.1, 3 et 3.2, pages imprimées 2–3 et 6–10](https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf).

Une [page officielle mise à jour le 3 mai 2026](https://help.opengroup.org/hc/en-us/articles/32109993154066-What-Open-Book-Is-Provided-With-the-TOGAF-Enterprise-Architecture-Part-2-Exam) identifie **Business Capabilities, Version 2, G211**. Le corps de ce guide n’a pas été consulté sur le site éditeur : ne pas attribuer automatiquement les détails ci-dessus à cette édition.

## ArchiMate : la grammaire de la carte

Dans **ArchiMate 3.1**, `Capability` désigne une aptitude possédée par une organisation, une personne ou un système. Les capacités peuvent être composées, agrégées ou spécialisées. Elles peuvent contribuer à d’autres capacités et être réalisées par des comportements du modèle. La spécification les distingue des processus et des fonctions, et relie les capacités et flux de valeur au modèle économique, les processus au modèle opératoire. [Document primaire Open Group C197, copie externe, §§7.1, 7.3.1–7.3.2 et 7.6, pages imprimées 51–53 et 57](https://governance.foundation/assets/frameworks/archimate/ARCHIMATE_v3_1_specifikacia.pdf).

**Inférence structurale :** cette grammaire permet une décomposition récursive ; elle ne fournit pas des niveaux métier numérotés ayant un contenu sectoriel fixe. La composition et la spécialisation ne doivent pas être confondues : décomposer une aptitude et distinguer ses variantes sont deux relations différentes.

Le [tutoriel communautaire ArchiMate 101](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/), sections *Architecture Domains*, *Importance of viewpoints* et *The generic metamodel*, confirme pédagogiquement le rôle du métamodèle, des vues adaptées aux destinataires et de la composition. Ses domaines et couches classent des **types d’éléments d’architecture** : ils ne sont donc pas les niveaux d’un catalogue de capacités retail. Le tutoriel est une contribution communautaire hébergée par Open Group ; il précise que son contenu n’est pas une garantie ou une approbation de l’organisme. Il ne remplace pas une spécification normative actuelle.

## BIZBOK/Guild : objets, actions et deux axes

L’[atelier officiel Guild du 20 juin 2019, pages PDF 15–21](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf) présente une construction par **objet métier + action**, par exemple autour du client ou de l’accord. Les capacités enfants restent dans la frontière de l’objet parent ; la précision des définitions sert à réduire ambiguïtés et redondances. Deux coordonnées sont séparées :

- `Tier` : stratégique, cœur / relation client, support.
- `Level` : profondeur de décomposition ; le gabarit montre 1 à 6, avec un détail adapté au besoin.

Les motifs illustrés comprennent définition de l’objet, gestion de ses informations, rapprochements et états. Ce sont des pratiques exposées en atelier, avec attribution à BIZBOK, pas la lecture intégrale de sa version courante. Les pages 4–5 montrent aussi des références sectorielles et un modèle commun. **Aucun catalogue retail complet et actuel de la Guild n’a été examiné ici.**

La [page publique de ressources de la Guild](https://learning.businessarchitectureguild.org/free-resources), consultée le 9 septembre 2026, annonce l’introduction et le glossaire **BIZBOK 15.0**, et réserve le guide complet aux membres. Les liens PDF de cette édition n’ont pas livré de contenu exploitable lors de cette recherche ; ses règles détaillées ne sont donc pas revendiquées comme vérifiées.

## Capacité et processus : proximité ne signifie pas identité

Le [position paper Guild d’octobre 2014, pages PDF 12–19](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/docs/batobpmalignmentpositionpape.pdf) distingue la décomposition fonctionnelle des capacités du découpage des flux opératoires avec déclenchements, sorties et passage du contrôle. Il établit explicitement une relation plusieurs-à-plusieurs entre capacités et processus. Il observe également que certaines classifications appelées « processus » ressemblent, dans leurs niveaux supérieurs, à des regroupements de capacités.

**Conséquence pour la comparaison :** un intitulé de processus peut fournir une capacité candidate, mais le rapprochement dépend de sa définition et du niveau examiné. Il faut regarder si le texte décrit un résultat métier réutilisable ou l’enchaînement particulier qui l’obtient. Ce papier est une position méthodologique historique ; il ne requalifie pas automatiquement toutes les feuilles APQC ou Oracle.

## Implications proposées pour Beaumanoir

Ces implications sont des analyses locales à éprouver, pas des règles adoptées :

1. **Séparer quatre coordonnées** : nature de l’élément, profondeur, catégorie stratégique/cœur/support et couche d’urbanisation Beaumanoir. Les confondre rendrait une comparaison de « niveaux » trompeuse.
2. **Comparer des frontières, pas des numéros** : un L1 Guild, un Business Area SAP et un domaine local peuvent avoir des étendues différentes. Documenter objet, résultat, inclusions, exclusions et capacités enfants avant de conclure à une équivalence.
3. **Utiliser le stock comme cas test** : « Stock » est notre objet à étudier ; « tenir les mouvements » ou « déterminer une disponibilité » sont des aptitudes candidates ; le comptage organisé en magasin est un parcours susceptible de les mobiliser. Ces formulations sont locales et ne prétendent pas être des feuilles BIZBOK.
4. **Préserver les deux urbanisations demandées par Laurent** : ces lectures aident à distinguer aptitudes durables et modalités opératoires. Elles ne prescrivent ni leur persistance, ni leurs contrats, ni leur découpage en applications. La portée marché du mot capacité reste plus large que notre sélection du socle ERP.

La comparaison du **contenu commerce effectivement commun** doit donc reposer sur les modèles sectoriels et éditeurs de l’étude. Ces trois références servent surtout à vérifier la construction et la sémantique de cette comparaison.

## Traçabilité de la lecture

Les huit sources sont liées au passage qui les utilise. État de consultation : 9 septembre 2026. Localisateurs supplémentaires : G189, page PDF 2 pour publication juin 2018 et identifiant ; C197, page PDF 2 pour publication novembre 2019 et identifiant ; atelier Guild, page PDF 1 pour date et pages 15–21 pour méthode ; position paper, pages portant octobre 2014. Tutoriel ArchiMate : aucune édition normative annoncée. Pages d’assistance Open Group : 26 décembre 2025 et 3 mai 2026. Aucune archive PDF intégrale n’a été ajoutée au projet. Les extraits sont reformulés et les limites d’accès restent explicites.

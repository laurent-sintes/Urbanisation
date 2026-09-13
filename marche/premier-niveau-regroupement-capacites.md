# Premier niveau de regroupement des capacités

10 septembre 2026 — réponse à [U43](../connaissance/01-contributions-utilisateur.md#u43), [U44](../connaissance/01-contributions-utilisateur.md#u44) et [U45](../connaissance/01-contributions-utilisateur.md#u45), complétés par [U46](../connaissance/01-contributions-utilisateur.md#u46), F134–F138, A25/A26 et [P73](../connaissance/05-propositions.md#p73). Complément ciblé de l’[étude comparative](etudes/2026-09-09-modeles-marche/etude-comparative.md), pas remplacement de ses résultats. Six références de structure réexaminées, puis un complément DDD pour le sens du domaine ; aucun catalogue principal ni niveau local définitivement adopté.

**L’hypothèse Univers / Domaine / Capacité rapportée par Laurent en U44 est cohérente comme structure de travail**, à condition de définir le rôle de chaque étage. Domaine → Capacité reste une option plus compacte si Univers n’ajoute pas de lecture utile. La profondeur des capacités dépend ensuite de leur définition. Les références examinées offrent des regroupements nommés, des capacités composites de niveau 1 ou des matrices ; elles ne fixent pas un même nom, une même maille ou une même profondeur pour ce premier niveau. Domain Area n’est pas un étage commun établi par cette comparaison.

## Ce que proposent les références examinées

| Référence et nature | Premiers regroupements observés | Conséquence pour notre carte |
| --- | --- | --- |
| SAP RBA — modèle de capacités | Enterprise Domain → Business Domain → Business Area → Business Capability. | Plusieurs catégories précèdent la capacité nommée comme telle. Une aire SAP peut avoir une maille pertinente pour notre domaine local ; cela demande une comparaison de contenu. S1. |
| TOGAF — guide de méthode, édition examinée 2018 | Capacités de niveau 1, puis décomposition en niveaux plus fins ; classement stratégique/cœur/support sur un axe distinct. | Le premier élément peut être une capacité composite. Aucun étage nommé Domaine n’est requis par ce passage. S2. |
| Business Architecture Guild — atelier de pratiques 2019 | Capacités de niveau 1 puis sous-capacités ; distinction entre Tier (stratégique/cœur/support) et Level (profondeur). Exemple de départ autour de la gestion du client. | Un regroupement par rôle dans l’entreprise ne doit pas être confondu avec la décomposition d’une aptitude. L’atelier n’est pas le guide BIZBOK actuel complet. S3. |
| IBM CBM — modèle de composants, édition 2005 | Compétences métier en colonnes, responsabilités de direction, contrôle et exécution en lignes. Exemple retail : clients, produits/services, canaux, logistique et administration de l’entreprise. | Deux axes forment une matrice ; les trois lignes ne sont pas des niveaux parent/enfant. Le composant inclut une logique de réalisation distincte de notre définition de capacité. S4. |
| Microsoft Dynamics — catalogue de processus, page 2026 | End-to-end processes → Business process areas → Business processes, puis contenus de réalisation et de test. | Le premier regroupement correspond à un parcours, le second à une aire de processus. Microsoft précise que certaines aires suivent les grandes fonctions ou départements : ce n’est pas directement notre découpage indépendant de l’organisation. S5. |
| APQC PCF — classification de processus, introduction 2018 | Category → Process Group → Process, puis activités et tâches. | Category est un niveau de taxonomie de processus ; le PCF seul ne représente pas leur enchaînement. Son sommet ne devient pas automatiquement une capacité mère. Contenu Retail détaillé non acquis. S6. |

Les dates sont celles des documents examinés, pas une affirmation de dernière édition. SAP et Microsoft disposent ici de pages évolutives ; les supports TOGAF, Guild, IBM et APQC sont historiques et identifiés comme tels. Les autres références de l’étude initiale, dont Oracle et ARTS, conservent leurs conclusions et limites ; elles ne sont pas nouvellement vérifiées dans ce complément.

## Le choix important : catégorie ou capacité composite

Un **regroupement** rassemble des capacités selon un périmètre explicite. Après U45, ce périmètre doit d’abord exprimer un espace de problèmes métier. Le nom Stock sert à classer les aptitudes nécessaires pour répondre à ces problèmes ; il ne suffit pas de réunir toutes les fiches mentionnant un objet stock.

Une **capacité composite** décrit déjà ce que sait faire l’entreprise. Gérer le stock ne devient une capacité mère que si l’on explicite son résultat, ses limites et la contribution de ses enfants. Lui donner un libellé large ne suffit pas à prouver cette cohérence.

C’est la distinction que les niveaux numérotés masquent parfois. Un domaine local, une aire SAP et une capacité de niveau 1 dans un atelier Guild peuvent offrir des points de comparaison, mais ils ne sont pas interchangeables par leur place dans un schéma. Le rapprochement porte sur les définitions, les inclusions et les exclusions. [CMP026](comparaisons.md#cmp026).

## Convention locale proposée

| Terme | Proposition d’usage |
| --- | --- |
| Univers | Grand champ d’activité réunissant plusieurs domaines. Terme rapporté par Laurent en U44 ; définition de travail proposée ci-dessous. |
| Domaine / Domain | Espace cohérent de problèmes métier liés entre eux, dont la carte regroupe les capacités nécessaires. Premier regroupement dans l’option compacte, ou rattaché à un Univers si cet étage apporte une lecture utile. |
| Sous-domaine / Subdomain | Regroupement supplémentaire possible si le volume et les frontières le justifient ; aucun étage obligatoire ajouté aujourd’hui. |
| Domain Area | Ne pas le retenir par défaut : son sens devrait être défini localement. La source SAP examinée emploie Business Area ; elle ne fournit pas une définition commune de Domain Area pour les autres modèles. |
| Bloc | Terme de dessin ou de discussion possible, à qualifier lorsqu’il désigne une catégorie, une capacité ou un élément d’urbanisation. Il ne suffit pas à préciser le type représenté. |
| Capacité de niveau 1, 2… | Repère de profondeur lorsqu’une aptitude est réellement décomposée. Le numéro ne fixe pas à lui seul la taille de la capacité. |

Deux structures sont à éprouver : **Univers → Domaine → Capacité**, proposée antérieurement par Laurent, et **Domaine → Capacité**, option compacte discutée en réponse à U43. Les sous-capacités se justifient ensuite par le contenu. Les domaines restent des catégories d’exploration ; ils n’imposent pas une application, une équipe, une persistance ou un contrat par domaine. Les deux urbanisations du projet et l’autonomie de C-Log sont préservées. Nature et Finalité restent des propriétés de lecture des capacités ; Capturer, Restituer ou Adapter ne deviennent pas des domaines par cette proposition.

Pour commencer à gérer un domaine, décrire les problèmes auxquels il répond, son libellé, sa définition, ses concepts et règles, ses inclusions/exclusions, les capacités pressenties, les correspondances externes et son statut. Aucun alignement numérique sur un niveau d’éditeur n’est requis. Une comparaison de domaine entier doit établir sa couverture ; citer quelques feuilles ne suffit pas à la valider.

## Exemple de vue à discuter

Cet exemple illustre la colonne Domaine, sans modifier les fiches CAP. Les natures et finalités conservent le statut proposé dans le [glossaire](../connaissance/19-glossaire-metier.md#hypothèse-sur-les-natures-de-capacité).

| Domaine proposé | Capacité discutée | Nature envisagée | Finalité |
| --- | --- | --- | --- |
| Stock | Enregistrer les états et mouvements — appui CAP004, actuellement documenté sur le magasin | Capturer | Disposer de faits permettant d’expliquer les quantités et leurs variations. |
| Stock | Rendre les stocks visibles — CAP005 | Restituer | Partager une connaissance contextualisée des positions de stock utile aux opérations. |
| Promesse | Réexaminer et réviser les promesses — CAP035/P69 | Adapter | Conserver des engagements compatibles avec l’évolution des ressources et des règles. |
| À positionner | Déterminer la disponibilité — CAP006 | Décider ou évaluer | Établir ce qui peut être proposé pour un usage et un horizon donnés. |
| À positionner | Protections et engagements — CAP007–CAP010, ensemble de candidats à distinguer | À préciser selon la capacité | Protéger certains usages et matérialiser les engagements envers les demandes. |

À positionner est un statut de rattachement, pas un domaine. Le stock n’est pas rebaptisé disponibilité ; rendre un stock visible n’implique pas que toute sa quantité soit utilisable. La ligne collective CAP007–CAP010 ne fusionne pas les candidats et ne masque pas la frontière planification/opération.

Les noms Stock et Promesse offrent deux points d’entrée pour discuter les frontières. Les qualifier de domaines locaux ne signifie pas qu’ils soient des Business Domains SAP : la source SAP place leurs thèmes dans des aires sous l’exécution de la chaîne logistique. Le rattachement de la disponibilité, des protections et des engagements reste à instruire à partir de leurs résultats et dépendances, sans déduire un partage d’applications.

## Reprendre l’hypothèse de juin : Univers / Domaine / Capacité

U44 indique que Laurent avait déjà proposé ces trois niveaux dans un draft d’urbanisation posé en juin. Le draft n’a pas été consulté ici ; aucune année, aucun découpage précis ou choix d’alors n’est reconstitué. Il s’agit d’une hypothèse à reprendre et éprouver, pas d’un arbitrage définitif.

| Niveau envisagé | Définition proposée | Exemple illustratif |
| --- | --- | --- |
| Univers | Grand champ d’activité de l’entreprise, utile pour regrouper plusieurs domaines. | Commerce, si la carte doit se lire dans une vue d’entreprise plus large. |
| Domaine | Espace cohérent de problèmes métier liés entre eux ; les capacités nécessaires y sont rattachées après analyse. | Stock ; Promesse. |
| Capacité | Ce que sait faire l’entreprise indépendamment de son organisation et de ses outils. | Rendre les stocks visibles ; réexaminer et réviser les promesses. |

L’exemple Commerce → Stock → Rendre les stocks visibles ne prétend pas reproduire le draft. Dans un projet déjà limité au cœur commerce, un univers unique Commerce peut n’être qu’un titre de périmètre ; dans une carte plus large, il peut apporter une navigation utile. Le niveau Univers ne justifie pas de réintroduire les domaines exclus du projet.

Par son rôle de grand regroupement, Univers peut se comparer au regroupement supérieur SAP ; cela ne prouve pas un même périmètre. Domaine peut, selon sa maille, se rapprocher d’un domaine ou d’une aire SAP, d’une compétence IBM ou du périmètre d’une capacité composite dans un autre modèle. Ces comparaisons sont des pistes de lecture, pas des équivalences de types ni de contenus. Il n’est pas nécessaire de reproduire chaque étage SAP pour que la carte locale soit cohérente.

L’hypothèse de juin est donc une base exploitable. Les critères de choix sont l’intelligibilité, l’absence de répétition inutile entre niveaux, la cohérence du périmètre des enfants et la traçabilité des comparaisons. Nature et Finalité demeurent des colonnes descriptives, indépendantes de cette hiérarchie.

## Donner un sens au domaine avec DDD

U45 précise le guide de Laurent : le domaine comme espace problématique. La définition native d’Evans dans la référence de 2015 est « A sphere of knowledge, influence, or activity. » Le même passage distingue le modèle, qui sélectionne des aspects du domaine pour résoudre des problèmes, et le bounded context, qui délimite où un modèle particulier est applicable. [S7]

**Définition de travail précisée après U46 : un domaine est un espace cohérent de problèmes métier liés entre eux, que l’on gagne à comprendre et à traiter ensemble.** Cette rédaction interprète l’orientation de Laurent ; elle ne prétend pas être une citation d’Evans. Le domaine donne un sens au classement, même si ses frontières continuent d’être affinées. La cohérence repose sur les liens entre les problèmes, leurs concepts et leurs règles ; des dépendances entre domaines sont normales et ne justifient pas automatiquement leur fusion.

L’ordre d’analyse devient : identifier les problèmes, comprendre les concepts et règles, préciser les limites, puis définir les aptitudes nécessaires. La carte regroupe ensuite ces capacités. Un vocabulaire, un objet ou un type d’action commun constitue un indice ; il ne prouve pas à lui seul l’existence d’un domaine unique.

| Problématique à examiner | Questions qui lui donnent du sens | Aptitudes possibles, sans nouveau découpage validé |
| --- | --- | --- |
| Connaissance du stock | Quelles quantités sont connues, où, dans quels états, et quels faits expliquent leurs variations ? | Enregistrer, rapprocher et restituer les faits et positions pertinents. |
| Protection des ressources | Quels usages faut-il préserver et sous quelles règles d’accès concurrent ? | Définir des protections et déterminer celles qui s’appliquent. |
| Disponibilité | Quelle quantité est utilisable pour cet usage, à cet horizon et sous cette politique ? | Déterminer une disponibilité contextualisée. |
| Promesse | Que peut-on engager envers une demande et comment faire évoluer cet engagement après un changement ? | Établir, confirmer, réexaminer ou adapter les promesses selon les règles. |

Ces quatre lignes sont des **problématiques à confronter**, pas quatre domaines automatiquement adoptés. Le stock intervient dans plusieurs d’entre elles. Ce partage d’objet ne suffit ni à les fusionner ni à les séparer ; examiner leurs règles, sens et dépendances. Les frontières disponibilité/protection/engagement/promesse restent à éprouver.

Domaine et sous-domaine peuvent décrire des périmètres de problèmes à des mailles différentes. La position locale appelée Domaine ne reçoit pas une profondeur DDD universelle. Univers demeure notre hypothèse de grand regroupement ; le passage d’Evans ne définit pas la chaîne Univers / Domaine / Capacité.

**Limite de travail précisée en U46 : rester sur les problèmes métier liés et les capacités nécessaires.** Laurent juge la notion de bounded context trop précise pour cette étape. Sa définition issue de la source DDD est conservée comme provenance, mais aucun découpage en bounded contexts, applications ou services n’est à produire ici. L’orientation à deux couches demeure ; ses choix de conception ne sont pas anticipés par la catégorisation.

Pour préciser un domaine, commencer par trois questions : quels problèmes traite-t-il ; qu’est-ce qui les relie et rend utile de les étudier ensemble ; quels problèmes restent voisins avec des relations explicites ? La proximité d’objets ou le fait de partager des données n’est qu’un indice, pas un critère suffisant de fusion.

**Sur le livre évoqué en U46 :** la vérification précédente portait uniquement sur le mémento de 2015. Un [extrait du livre fourni par l’éditeur](https://www.informit.com/content/images/9780321125217/samplepages/0321125215.pdf), ©2004, impression de juin 2011 indiquée, a été examiné le 10 septembre 2026. Il contient des pages liminaires et du début du livre ; la recherche ciblée n’a pas retrouvé la formulation exacte évoquée par Laurent. L’extrait ne permet aucune conclusion sur son absence du livre complet. La définition de travail ci-dessus suit le sens donné par Laurent, sans se présenter comme une citation bibliographique retrouvée.

## Sources et portée de la vérification

Consultation ciblée le **10 septembre 2026**. Documents lus par leurs passages textuels ; versions antérieures et preuves de l’étude initiale conservées. Les sources ne prouvent aucune configuration de Beaumanoir ou de Boardriders.

- **S1 — SAP**, [cours RBA](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), sections Reference Architecture Content Example, Reference Architecture Content Framework et Business Capability Model Example. Page publique, édition du catalogue non établie. MKT04/ELM014. Regroupements et lien domaine/aire/capacité vérifiés dans le texte ; catalogue complet non acquis.
- **S2 — The Open Group**, [guide G189](https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf), juin 2018, §3.2.1–3.2.2, pages imprimées 9–10. Document primaire consulté sur un miroir tiers ; conformité à l’exemplaire actuellement distribué non vérifiée. MKT01/ELM019. G211/version 2 non consulté ; ne pas lui attribuer les règles du document historique.
- **S3 — Business Architecture Guild**, [atelier du 20 juin 2019](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf), pages PDF 17–21 : catégories, décomposition et gabarit. MKT03/ELM021. Support public historique ; pas lecture du guide BIZBOK 15.0 complet ni de son catalogue retail.
- **S4 — IBM**, [CBM, G510-6163-00](https://public.dhe.ibm.com/software/emea/dk/frontlines/g510-6163-component-business-models.pdf), 2005, pages PDF 9–11, cadre et exemple retail. MKT06/ELM025. Compétences et responsabilités, pas hiérarchie de sous-capacités ni référentiel retail actuel établi.
- **S5 — Microsoft**, [présentation du catalogue](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/about), section What’s in the catalog?, page datée du 8 janvier 2026. MKT14/ELM026. Structure web consultée ; pas export homogène du catalogue ni carte de capacités indépendante des produits. La page détaillée liée sur les niveaux a également été ouverte ; les conclusions ici reposent sur la présentation datée.
- **S6 — APQC**, [introduction au PCF](https://www.apqc.org/sites/default/files/files/PCF%20Collateral/Intro%20to%20PCF%20-%20FINAL.pdf), ©2018, figure 1 et pages PDF 1–2. MKT07/ELM023. Structure générale vérifiée ; aucune acquisition nouvelle du détail Retail 7.2.1.

- **S7 — Eric Evans / Domain Language**, [référence DDD](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf), ©2015, page imprimée vi/page PDF 6, Definitions ; texte consulté le 10 septembre 2026. MKT17/ELM041/CMP027. Document de l’auteur, licence CC BY 4.0. Définition native et adaptation locale distinguées ; aucun catalogue commerce ni structure Univers / Domaine / Capacité déduits.

Ce complément réutilise six éléments externes déjà enregistrés et ajoute ELM041 pour DDD. Il ajoute CMP026/CMP027 et enrichit la proposition locale P73. Aucune nouvelle capacité, équivalence validée ou couverture de domaine complet n’est déduite.

## Application aux domaines du socle après U51

Les [options de découpage](../connaissance/22-options-domaines-socle.md) appliquent ces distinctions au socle : référence principale filtrée, grandes familles ou domaines de problèmes. La liste proposée et les frontières restent à discuter ; CMP031, sans adoption d’un catalogue ou hiérarchie.

## Granularité SAP et autres modèles orientés domaines

Complément du 10 septembre 2026 à [U59](../connaissance/01-contributions-utilisateur.md#u59), F159, A35/P78 et [CMP033](comparaisons.md#cmp033). Il complète les six références examinées plus haut par BIAN et TM Forum. L’appréciation de Laurent reste exploratoire ; aucun catalogue principal n’est adopté.

### Pourquoi la maille SAP paraît adaptée

**Avis proposé : SAP est un point de départ particulièrement pertinent pour éprouver le contenu commerce/stock de nos domaines, surtout à la maille Business Area.** Ce jugement porte sur les exemples effectivement examinés ; il ne constitue pas un classement exhaustif de tous les modèles.

La chaîne native reste **Enterprise Domain → Business Domain → Business Area → Business Capability**. L’exemple documenté situe Inventory Management et Order Promising sous Supply Chain Execution, lui-même sous Supply – Fulfill Demand. [Cours SAP, Framework et Business Capability Model Example](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), reconsulté le 10 septembre 2026, édition du catalogue inconnue ; ELM014.

Pour notre lecture problématique, Stock et Promesse peuvent donc être examinés à une maille comparable à ces aires, en décrivant leurs problèmes, concepts et règles. Le Business Domain SAP est ici un regroupement plus large. Ce rapprochement ne demande pas de rebaptiser tous les niveaux ni d’attribuer uniformément chaque aire SAP à un domaine local.

SAP distingue également capacités, processus et réalisations. Cela soutient notre travail sur des modèles liés ; leur séparation n’impose pas l’architecture locale à deux couches. [Defining Business Architecture](https://learning.sap.com/courses/intelligent-enterprise-architecture-fundamentals/defining-business-architecture), passages capability/process centric et RBA/RSA, reconsultés le 10 septembre 2026 ; cours sans édition identifiée, ELM002/ELM009.

Les intitulés sont une bonne entrée, mais la cohérence problématique doit encore être démontrée pour chaque périmètre. Les définitions natives retail/fashion complètes et versionnées manquent toujours. Pour FLOW, le rattachement d’une capacité à une aire SAP ne décide pas si elle sera développée dans la plateforme : **la logistique reste hors développement et en adhérence** (U58).

### Les alternatives pertinentes et leur rôle

| Référence | Organisation observée | Apport proposé pour notre travail | Différence fondamentale |
| --- | --- | --- | --- |
| **BIAN** | Business Area → Business Domain → Service Domain, dans le guide 2020. | Examiner comment des périmètres stables contribuent à plusieurs scénarios. | Catalogue bancaire ; le Service Domain guide déjà une partition de services, distincte d’une capacité métier. ELM048. |
| **TM Forum ODA** | Le Functional Framework classe des fonctions en domaines/sous-domaines ; le Capability Framework constitue un autre modèle. | Comparer le sens des regroupements et les relations entre vues. | Fonctions SI, blocs d’architecture et capacités sont distincts ; détail du catalogue de capacités non examiné. ELM049–ELM051. |
| **IBM CBM retail** | Compétences métier croisées avec Direct / Control / Execute. | Autre lecture sectorielle pour repérer des sujets et responsabilités oubliés. | Matrice de composants, document de 2005 ; ses trois lignes ne sont ni nos couches ni des niveaux de capacités. ELM025. |
| **Business Architecture Guild / BIZBOK** | Capacités de haut niveau décomposées, objets métier et niveaux distincts des catégories. | Éprouver la définition et la décomposition des aptitudes. | Pas une chaîne Univers / Domaine imposée par les passages consultés ; catalogue retail complet non examiné. ELM021. |

Sources détaillées et limites BIAN/TM Forum : [MKT18](catalogue.md#mkt18) et [MKT19](catalogue.md#mkt19). Pour IBM : [publication officielle](https://public.dhe.ibm.com/software/emea/dk/frontlines/g510-6163-component-business-models.pdf), G510-6163-00, 2005, pages PDF 9–11 et figure 6, texte relu le 10 septembre 2026. Pour la Guild, reprendre les passages historiques réellement consultés en ELM021 : les nouvelles ouvertures directes des présentations sectorielles et du PDF d’atelier ont échoué. Les extraits indexés signalent une équipe Retail ; ils ne prouvent pas qu’un modèle retail complet est disponible et étudié.

Un point TM Forum mérite une exploration ultérieure : la Functional Architecture sépare **Core Commerce** et **Production**, au sens de commerce et fourniture du service. C’est une analogie utile pour éprouver les responsabilités commerce/Supply et les adhérences logistiques ; Production ne se traduit pas automatiquement par notre Supply. La présentation est consultée, pas les spécifications détaillées. [Source officielle](https://www.tmforum.org/open-digital-architecture/functional-architecture/), ELM050.

### Usage proposé

P78 propose d’utiliser SAP comme **première grille d’épreuve du contenu et de la maille**. Après U60/C45, IBM est conservé comme historique non prioritaire, BIAN reste périphérique à la définition de capacité et TM Forum demeure une piste. La Guild est approfondie pour la définition et la décomposition en P79. Les références de processus APQC, Oracle RRM et Microsoft Dynamics conservent leur rôle de contrôle de couverture déjà documenté ; elles ne deviennent pas des cartes de domaines par changement d’étiquette.

Pour les domaines prioritaires, décrire le problème, les inclusions/exclusions et quelques aptitudes, puis confronter les cas de stock, promesse, achats et réassort. Conserver le niveau natif de chaque référence, qualifier le rapport au périmètre FLOW et tracer chaque adaptation. Cette étape ne fixe ni application, ni service, ni objet universel par domaine. Les 36 capacités candidates restent inchangées ; aucune équivalence de domaine entier n’est établie.

### Approfondissement et priorités après U60

La [recherche BIZBOK](bizbok-capacites-et-domaines.md) ajoute des preuves issues de l’introduction et du glossaire 15.0 ©2026 et du Metamodel Guide 3.0 de septembre 2024, désormais consultés sur le CDN officiel. Elle distingue objet central des capacités, décomposition et domaines problématiques locaux. Le Common Reference Model existe comme livrable membre ; livraison, version et contenu d’un modèle Retail/Wholesale ne sont pas établis. Le tableau U59 conserve la comparaison historique des natures ; les rôles courants suivent les réserves de Laurent en U60.

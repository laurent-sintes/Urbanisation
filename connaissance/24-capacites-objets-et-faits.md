# Capacités, objets métier, faits de gestion et documents

10 septembre 2026 — [U61](01-contributions-utilisateur.md#u61) et [U62](01-contributions-utilisateur.md#u62), F162–F164, A37/A38/P80 et [CMP035](../marche/comparaisons.md#cmp035). Sources comparées : SAP, BIZBOK/Guild et TM Forum. Cette note complète l’[orientation à deux couches](15-orientation-deux-couches.md), le [glossaire](19-glossaire-metier.md) et la [recherche BIZBOK](../marche/bizbok-capacites-et-domaines.md).

**Proposition : faire émerger le sens des objets, états, faits et documents pendant l’analyse des capacités, dans un modèle métier lié à la carte. La conception de la plateforme précise ensuite leur réalisation, par itérations avec le métier.** Le seul libellé d’une capacité ne permet pas de déduire tout ce modèle.

## Distinction apportée par Laurent

U61 distingue les objets métier de la plateforme, rapprochés d’aggregate roots, des faits de gestion : événements associés à des documents. Ces documents représentent des états d’aggregate roots ou sont des objets non modifiables produits ou captés. C’est une orientation locale déclarée ; les autres références emploient des catégories différentes.

L’analogie avec une racine d’agrégat invite à examiner identité, cycle de vie et règles de cohérence, sans décider ici de ses limites exactes. Le mémento d’Evans traite précisément des invariants, de leur garant et de la frontière transactionnelle ; ces éléments ne sont pas déduits du seul objet central d’une capacité. [ELM061](../marche/elements.md#elm061), motif de conception consulté uniquement pour qualifier l’analogie.

## Ce que l’analyse métier peut préciser

| Sujet | À faire émerger avec les capacités et les cas | À préciser lors de la conception de plateforme |
| --- | --- | --- |
| Objet métier | Sens, identité utile au métier, relations, cycle de vie et autorité sur son état. | Racines d’agrégats, objets internes et représentations de lecture ; allocation aux composants. |
| État | Situation et informations qui valent à un instant, transitions autorisées, règles qui doivent toujours rester vraies. | Mécanismes assurant la cohérence et traitement des accès concurrents. Les exigences de cohérence restent métier. |
| Fait de gestion | Ce qui s’est produit ou a été constaté, date pertinente, source, objets concernés et effet attendu. | Enregistrement, publication, corrélation, ordre de traitement et reprise des doublons. |
| Document | Ce qui est attesté, produit ou capté, contenu significatif, version applicable, règles de modification ou de correction. | Formats, stockage, signatures éventuelles si exigées, représentation de la version et modalités d’échange. |
| Contrat | Signification d’une demande et de sa réponse, engagement, refus et événement pertinent pour les parties. | API/message, schéma, protocole, garanties de transport et compatibilité technique. |

Cette grille décrit des dimensions de travail au sein de l’urbanisation à deux couches du projet. Les deux modèles métier durables du projet restent distincts. L’expression détaillée des règles peut faire réviser une capacité ou un objet : l’analyse n’est pas une succession à sens unique.

Le caractère non modifiable d’un document peut être une exigence métier. Ses modalités de conservation relèvent de la conception. À cette étape, préciser le sens d’une correction et ce qui doit rester traçable sans choisir un moteur, un journal d’événements ou une base de données.

## Des objets métier dans les deux couches

**Précision déclarée en U62 :** les processus s’appuient souvent sur des objets métier, dans une approche Case Management ; Laurent cite **Demande de réassort**. Les domaines transactionnels portent eux aussi des objets métier. Cette précision prolonge les modèles propres à chaque couche déjà posés en U19.

| Lecture | Objet et connaissances à examiner | Statut |
| --- | --- | --- |
| Processus de réassort | Demande de réassort comme objet de suivi d’une situation : besoin exprimé, traitement, décisions de parcours, exceptions et clôture. | Objet cité par Laurent ; contenu et états proposés pour illustration. |
| Domaines transactionnels mobilisés | Positions de stock, allocations, réservations ou engagements de fourniture, avec leurs règles et états propres. | Exemples à éprouver ; ni liste validée ni frontières d’agrégats décidées. |
| Relations entre modèles | Références des engagements concernés, quantités et dates confirmées, faits de réalisation utiles au suivi de la demande. | Contenu de contrat à préciser ; aucune cardinalité imposée. |

Le problème traité, les règles, le cycle de vie et l’autorité sur l’état aident à situer un objet. Sa seule qualification d’objet métier ne détermine pas sa couche. De même, la présence d’une orchestration ou d’une persistance est compatible avec chacune des deux couches.

Dans une illustration de réassort, le processus pourrait suivre une demande « partiellement satisfaite », tandis que le socle conserve les engagements et les faits qui justifient cette situation. La règle de passage à cet état de suivi et les informations contractuelles nécessaires doivent être explicites. Le socle peut posséder une représentation de la demande utile à ses décisions, sans reprendre l’ensemble du dossier processus. Le choix d’une convention universelle Demande/Commande reste ouvert en Q052 ; l’exemple ne le tranche pas.

L’analyse des capacités éclaire donc en priorité les objets du **socle transactionnel** visé par la carte. L’analyse du modèle processus explicite les objets de cette couche et leurs liens au socle. Les deux modèles se précisent ensemble à leur frontière ; aucun objet du processus n’est transformé automatiquement en capacité de notre carte.

## Ce que montrent les références

| Référence | Constat documentaire | Portée pour notre question |
| --- | --- | --- |
| **SAP** | Le Business Data Catalog relie objets d’information et capacités ; SAP distingue objets métier et objets de solution. | L’information métier s’explicite avant le schéma de réalisation ; elle dispose d’une vue liée à la carte. [ELM056](../marche/elements.md#elm056). |
| **BIZBOK / Guild** | Capacité, information, états et résultats sont reliés dans le métamodèle ; les concepts d’information donnent un sens partagé aux objets. | Une définition de capacité amène à préciser ce qu’elle utilise, transforme et produit. Le détail se conserve aussi dans le modèle d’information. [ELM057](../marche/elements.md#elm057). |
| **TM Forum** | Le SID est un modèle d’information métier indépendant des plateformes ; entités, attributs et relations sont explicites. Les ABEs sont des regroupements. | Les vues métier existent avant les contrats d’API ; aucune assimilation ABE / aggregate root. [ELM058](../marche/elements.md#elm058). |

Ces constats soutiennent une méthode de modèles liés ; ils ne fournissent pas une transformation automatique capacité → objet → agrégat → événement → document. L’information et les faits ne deviennent pas pour autant des capacités ou des sous-capacités.

### Fait, résultat, document et notification

Le glossaire BIZBOK distingue un résultat et une occurrence. L’état atteint par un objet, le fait qui l’explique, le document qui en porte une représentation et le message qui en informe un consommateur sont des notions à relier, avec leurs propres sens. [ELM057]

SAP illustre concrètement cette différence : un mouvement comptabilisé produit un Material Document, tandis que des événements Created/Canceled le référencent. SAP appelle aussi ce document business object. Le mouvement et la quantité sont corrigés par annulation et nouvelle comptabilisation ; certains compléments restent possibles. Le terme document SAP ne prouve donc pas une immutabilité absolue. [ELM059](../marche/elements.md#elm059), extraits indexés.

Dans l’exemple d’API TMF622 examiné, le cycle de la commande et ses notifications sont distincts. Le schéma TM Forum Document porte état, version et date de mise à jour ; le terme seul n’établit pas les règles d’immutabilité locales. [ELM060](../marche/elements.md#elm060), exemples historiques explicitement datés.

Pour notre modèle, la publication d’un événement de création de document peut indiquer qu’un justificatif a été enregistré, sans prouver à elle seule quel fait opérationnel s’est produit ni quand il s’est produit. Il faut définir ce sens et son autorité. Les liens objet/fait/document ne sont pas supposés un-pour-un ; la conservation d’un fait n’impose pas l’Event Sourcing.

## Exemple proposé : confirmer une promesse de fourniture

Illustration métier, sans nouveau fait d’existant, nouvelle CAP ni modèle éditeur prétendu. L’aptitude envisagée est de confirmer les quantités et dates auxquelles une demande peut être satisfaite selon les règles applicables.

| Élément à expliciter | Exemple de contenu métier |
| --- | --- |
| Objets concernés | Besoin présenté à la promesse, ressources admissibles et engagement de fourniture ; objets, identités et relations à préciser. |
| Résultat | Une quantité et une date confirmées pour la demande. |
| État | L’engagement considéré est confirmé, avec les valeurs applicables. |
| Fait de gestion | À un instant donné, telle quantité et telle date ont été confirmées pour telle demande. |
| Document associé | Une confirmation identifiée et versionnée portant les engagements et conditions retenus ; contenu exact à définir. |
| Révision | Une nouvelle décision peut changer la promesse courante ; préciser la relation à la confirmation antérieure et le fait de révision. |
| Publication éventuelle | Un message informe les parties du changement avec les références nécessaires ; son envoi ne constitue pas la décision métier. |

La demande de cet exemple désigne ce que la promesse doit satisfaire ; elle ne postule ni objet Demande universel ni identité avec la Demande de réassort du processus. Nous pouvons décrire ce sens sans décider si les objets représentant la demande et l’engagement partagent un agrégat, si la confirmation représente tout l’état ou une sélection utile, ni quel format sera échangé. Ces choix doivent être éprouvés avec les règles, les autorités et les contraintes de cohérence. L’OMS peut utiliser le résultat dans son modèle de processus ; il ne devient pas propriétaire de tous les objets du socle.

## Proposition pour les fiches de capacités

P80 propose de conserver le libellé et la définition de l’aptitude, puis de documenter au niveau utile : **objets concernés ; informations nécessaires ; résultat et états ; faits produits ou captés ; documents associés ; règles et autorité ; liens aux contrats**. Les notions partagées sont définies dans le glossaire et le modèle métier, plutôt que répétées avec des sens divergents dans chaque fiche.

La carte permet de naviguer entre ces éléments. Elle ne devient ni un schéma de tables ni un catalogue d’API. Une opération, un document ou un événement ne crée pas automatiquement une sous-capacité. Les formes exactes des fiches et les rattachements restent proposés ; les 36 CAP sont conservées.

Les règles d’immutabilité détaillées, le contenu des états documentés et les cardinalités restent à préciser. La logistique demeure hors développement FLOW, en adhérence ; un fait reçu de la logistique doit notamment conserver sa source et la responsabilité de sa qualification.

## Sources, versions et limites

Consultation le 10 septembre 2026. Les références ne prouvent aucune configuration Beaumanoir.

- **SAP métier** : [Defining Business Architecture](https://learning.sap.com/courses/intelligent-enterprise-architecture-fundamentals/defining-business-architecture), Business Data Catalog / Business Data Mapping ; [Methodology](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/investigating-the-sap-enterprise-architecture-methodology), Enterprise Architecture Concepts. Cours non versionnés, passages ouverts et lus ; ELM056.
- **Guild** : [Metamodel Guide v3.0](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf), septembre 2024, §§5.1.2/5.2/5.3 ; [glossaire 15.0](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_glossary.pdf), ©2026, Event/Outcome. Texte consulté, pas guide BIZBOK intégral ; ELM057.
- **TM Forum métier** : [SID](https://www.tmforum.org/open-digital-architecture/information-framework-sid/) et [Capability Framework](https://www.tmforum.org/open-digital-architecture/capability-framework/), présentations publiques ; SID 26.0 et GB1029C v4.0.0 détaillés non consultés ; ELM058.
- **Exemples de réalisation** : pages SAP Help sur Material Document et notifications, version 2608 pour les événements, extraits indexés consultés et accès directs sans texte ; TMF622 v4.0.0 ©2019, pages 13 et 37–40, et schéma Document portant un repère 2020. Liens exacts et limites en ELM059/ELM060. Ces exemples n’établissent pas l’état des éditions actuelles complètes.
- **Analogie DDD** : [Evans, référence 2015](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf), Aggregates p.16 / PDF 23 ; passage textuel consulté, ELM061. La qualification de l’analogie n’engage pas un découpage de conception.

**Application U63/U64 :** la [première carte des domaines cœur](25-domaines-coeur-et-epreuve-recits.md) associe problèmes, capacités, Finalité et objets de travail, puis les éprouve sur les récits. P81 conserve le caractère proposé des enrichissements et des frontières ; les objets des deux couches restent distincts.

## Objets de référence et commandes — U97/U98

Party / Role, Agreement et Catalog sont des modèles de référence distincts, reçus de maîtres externes et reliés par identifiants. Leur représentation locale ne donne pas autorité pour les créer, modifier ou vérifier. Agreement porte le contrat de référence ; la commande transactionnelle reste distincte selon U98. Ces précisions métier ne fixent pas les agrégats, cardinalités, événements ou règles de persistance. Voir [P85 et la carte courante](25-domaines-coeur-et-epreuve-recits.md#référentiels-ingérés-u97u98), C64 et INF18–INF20.

## Document comme preuve d’autorisation — U100

Laurent ajoute une sémantique métier commune aux commandes d’achat, de vente, de retour et éventuellement à d’autres documents : prouver l’autorisation d’un déplacement de marchandises. Cela précise l’usage des documents sans imposer un schéma universel, un agrégat unique ou une persistance particulière. La distinction proposée entre autorisation, acceptation d’exécution et fait réalisé prolonge U61 ; les responsabilités des domaines restent à préciser. Les Party sont à relier aux lieux, sans confondre acteurs et points physiques. Voir [la note U100](26-supply-documents-autorisations.md), Q074.

U100 confirme aussi une référence article indépendante des catalogues : le même SKU peut être proposé dans plusieurs d’entre eux. D08.d reçoit la référence article dans la continuité de U97 ; D12 référence les articles dans les catalogues reçus. Source maîtresse, attributs et cardinalités détaillées restent ouverts.

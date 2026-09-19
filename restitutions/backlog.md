# Backlog — 2026-09-13.3

Restitution générée depuis le modèle structuré, connaissance au 2026-09-17. Ne pas éditer cette vue pour modifier le modèle.

Publication et validation sont distinctes. Le statut d’un rattachement peut différer de celui de la capacité.

## Niveaux d’urbanisation

| Repère | Nom | Niveau | Contenu direct | Statut |
| --- | --- | --- | --- | --- |
| universe-case | Business Services | universe | Exploration différée | Validé par l’urbaniste — portée : name, definition |
| universe-supply | Supply Chain Orchestration | universe | Inventory Management, Order Backlog Management, Order Management, Inventory Optimization, Process Management, Business References | Validé par l’urbaniste — portée : name |

Les groupes de présentation, dont Business References, conservent leur rôle distinct.

## D01 — Inventory Management

Statut : **Validé par l’urbaniste — portée : finality**.

Connaître les stocks et les ressources attendues, expliquer leurs variations, fiabiliser les quantités et préserver les usages par les protections et réservations. Le stock futur est connu ici et mobilisé par Order Promising.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D01.f | Inventory Tracking | En cours d’instruction | Établir et actualiser les quantités physiques et leurs états logiques à partir des faits de stock reconnus, par référence de produit, lieu, détenteur et propriétaire lorsque ces dimensions sont pertinentes ; suivre distinctement les ressources futures connues et leurs caractéristiques attendues. | Disposer d’un état du stock à jour, expliqué par les faits reconnus, en distinguant présent et attendu. | En cours d’instruction |
| D01.g | Record Inventory Movements | Validé par l’urbaniste — portée : name | Enregistrer, qualifier et conserver les mouvements de stock et leurs justifications : réceptions, sorties, transferts, changements d’état ou de propriété et ajustements justifiés ; identifier les quantités concernées, les dates et les références explicatives, y compris sans déplacement physique. | Disposer d’un historique traçable des faits qui expliquent les variations du stock. | En cours d’instruction |
| D01.c | Inventory Visibility | En cours d’instruction | Fournir une lecture cohérente des stocks physiques, de leurs états logiques et des ressources futures dans les différents lieux et périmètres, avec provenance et fraîcheur, sans double compte. | Permettre aux décisions de s’appuyer sur une connaissance partagée. | En cours d’instruction |
| D01.d | Stocktaking | Validé par l’urbaniste — portée : definition, finality, name | établir les quantités constatées par comptage, les confronter aux quantités enregistrées, qualifier les écarts et établir les corrections justifiées. | Fiabiliser les quantités enregistrées — Inventory accuracy. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D02.b | Supply Protection | Validé par l’urbaniste — portée : name | Configurer et maintenir les politiques, règles et quantités qui encadrent l’usage et le renouvellement des ressources pour maîtriser pénurie, surstock et déséquilibre. | Encadrer l’usage et le renouvellement des ressources pour réduire pénurie, surstock et déséquilibre. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D02.c | Reservation | Validé par l’urbaniste — portée : name | établir un engagement de quantité pour un besoin identifié, dont les usages concurrents doivent tenir compte. | Donner effet à un engagement de ressource. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D01.h | Consigned Inventory Management | Validé par l’urbaniste — portée : name, definition | Appliquer au stock consigné les conditions de l’accord : propriété, droits d’usage, échéances et suites autorisées ; mobiliser les capacités responsables lorsqu’une acquisition, un retour ou une autre issue devient nécessaire. | Respecter les droits et obligations sur le stock fournisseur détenu, pendant sa présence dans le réseau et lors de ses suites. | Validé par l’urbaniste — portée : type, source_id, target_id |

## D03 — Order Backlog Management

Statut : **Validé par l’urbaniste — portée : name, finality**.

Travailler collectivement le carnet d’Orders Supply pour prioriser les demandes, évaluer leurs possibilités de satisfaction, construire les scénarios d’affectation et préparer puis engager la part retenue vers les processus, en préservant le sens des demandes et les engagements applicables.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D02.e | Supply Assignment | Validé par l’urbaniste — portée : name, nature | Affecter les ressources Supply présentes ou futures aux commandes identifiées, selon les priorités, les engagements et les contraintes applicables, afin de maximiser la valeur multidimensionnelle de leur satisfaction. | Maximiser la valeur multidimensionnelle de la satisfaction des commandes sous contraintes, en matérialisant les affectations retenues. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.i | Available-to-Promise (ATP) | Validé par l’urbaniste — portée : finality, name, nature | Établir les quantités et dates auxquelles une demande ou un ensemble de demandes peut être satisfait par les ressources présentes ou futures admissibles dans la situation de référence, et expliciter la couverture qui rend ces engagements possibles. | Établir une solution de promesse réalisable dans la situation de référence. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.j | Capable-to-Promise (CTP) | Validé par l’urbaniste — portée : definition, finality, name, nature | Déterminer les possibilités de satisfaction d’un Order nécessitant une adaptation des ressources ou des engagements, en mobilisant les décisions spécialisées et en explicitant les conditions de faisabilité et les impacts. | Établir à quelles conditions une promesse deviendrait réalisable après adaptation. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.k | Profitable-to-Promise (PTP) | Validé par l’urbaniste — portée : definition, finality, name, nature | Comparer et sélectionner les scénarios de promesse selon leurs coûts et conséquences économiques, dans les contraintes de service applicables. | Retenir une solution économiquement pertinente parmi les possibilités examinées. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.l | Delivery Schedule Decision | Validé par l’urbaniste — portée : definition, finality, name, nature | Choisir la répartition des quantités promises dans le temps, en une ou plusieurs échéances, parmi les possibilités réalisables et selon les conditions de la commande. | Retenir un échéancier acceptable pour honorer la commande. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.m | Order Prioritization | Validé par l’urbaniste — portée : name, definition | Établir et réviser les priorités relatives des commandes. | Arbitrer les commandes à satisfaire en priorité lorsque leurs besoins se trouvent en concurrence. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D04.n | Order Structuring | Validé par l’urbaniste — portée : name, definition | Organiser et faire évoluer le découpage et la composition des Orders et de leurs éléments, en préservant leurs liens, leurs quantités et leurs engagements. | Conserver une lecture cohérente de l’ensemble, de ses engagements et de sa satisfaction au fil des évolutions de ses composants. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D03.n | Promise Management | Validé par l’urbaniste — portée : name | Gérer les propositions et engagements de promesse Supply, leurs confirmations et leurs révisions autorisées, avec quantités, dates, conditions et historique. | Établir et maintenir des engagements Supply explicites et cohérents avec les possibilités retenues. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D04.q | Order Archiving | Validé par l’urbaniste — portée : name | Organiser la conservation historique des Orders éligibles en dehors de leur usage opérationnel courant, tout en préservant leur consultation, leurs versions utiles et leurs liens. | Permettre la recherche et l’explication d’anciens engagements sans maintenir indéfiniment les commandes dans le traitement courant ; maîtriser ce qui reste consultable. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D03.o | Fulfillment Plan Decision | Validé par l’urbaniste — portée : name, definition, nature | Déterminer un scénario cohérent d’affectation des ressources Supply aux commandes, en mobilisant les décisions spécialisées et les politiques applicables, afin de maximiser la valeur multidimensionnelle de leur satisfaction. | Proposer un plan d’affectation collectivement cohérent pour satisfaire les commandes selon les objectifs applicables. | En cours d’instruction |
| D03.p | Order Backlog Planning | Validé par l’urbaniste — portée : name, nature | Construire, comparer et maintenir les scénarios de satisfaction du carnet d’Orders, en mobilisant les décisions spécialisées, puis préparer la prise en charge de la part retenue par les processus. | Transformer les scénarios de satisfaction du carnet en une préparation cohérente de leur prise en charge, en conservant la maîtrise des engagements. | Validé par l’urbaniste — portée : type, source_id, target_id |

## D04 — Order Management

Statut : **Validé par l’urbaniste — portée : name**.

Capter et maintenir les demandes Supply selon leur intention métier, leurs parties, leurs conditions et leur résultat attendu, et gouverner leur cycle de vie, en articulation avec le travail collectif du carnet et les processus.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D04.i | Sales Order | Validé par l’urbaniste — portée : name | Gérer les commandes clients à satisfaire : enregistrer ce qui est demandé, maintenir les quantités, destinations et échéances applicables, suivre les évolutions autorisées et déterminer ce qui reste à servir. | Disposer d’une commande client exploitable et d’un reste à satisfaire explicable pendant son traitement. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D04.j | Purchase Order | Validé par l’urbaniste — portée : name | Prendre en charge les commandes d’achat de biens ou de prestations adressées aux fournisseurs, maintenir les attentes et les évolutions autorisées et rapprocher les réalisations pour connaître le reste à satisfaire. | Disposer d’attentes d’achat explicables, en biens ou prestations, et connaître ce qui reste à satisfaire selon les accords applicables. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D04.k | Transfer Order | Validé par l’urbaniste — portée : name | Gérer les ordres de déplacement de marchandises entre sites : maintenir origine, destination, quantités et échéances, suivre les modifications et rapprocher départs et arrivées pour connaître le transfert restant à satisfaire. | Rendre explicite ce qui doit être transféré, vers quel site et ce qui reste à acheminer ou à recevoir. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D04.l | Customer Return | Validé par l’urbaniste — portée : name, definition | Prendre en charge les retours clients, leurs commandes et leurs suites logistiques, jusqu’au résultat attendu selon les décisions et autorisations applicables. | Connaître le retour client attendu, suivre ses suites logistiques et expliquer le résultat obtenu pour chaque produit ou quantité. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D04.m | Supplier Return | Validé par l’urbaniste — portée : name | Prendre en charge les retours de marchandises aux fournisseurs et suivre leurs suites attendues, selon les accords applicables, en distinguant renvoi sans remplacement, remplacement et réparation avec restitution du bien. | Piloter un retour fournisseur explicite et traçable, distinct de la commande d’achat initiale. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D04.o | Order Lifecycle Management | Validé par l’urbaniste — portée : name, nature, definition | Gouverner les évolutions autorisées des Orders selon leurs différentes dimensions métier, en préservant la cohérence entre engagements, modifications en préparation et réalisations acquises. | Savoir ce qui peut progresser, ce qui est bloqué et pourquoi, ainsi que les conditions de reprise ou de fin du traitement. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D04.r | Consignment Replenishment Order | Validé par l’urbaniste — portée : name, definition | Demander et suivre un apport fournisseur : produits, quantités, destinations, dates et reste à recevoir, sans engagement d’achat des marchandises. | Disposer d’un apport fournisseur attendu et traçable, distinct de l’acquisition des marchandises. | Validé par l’urbaniste — portée : type, source_id, target_id |

## D05 — Inventory Optimization

Statut : **Validé par l’urbaniste — portée : name, finality, definition**.

Optimiser le stock consiste à choisir un compromis entre disponibilité, immobilisation et risque, puis à décider des ajustements nécessaires.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D05.a | Inventory Target Decision | Validé par l’urbaniste — portée : name, definition | Déterminer les objectifs de stock et les seuils associés, par produit, lieu et période, selon les besoins, le niveau de service recherché, les délais et les risques. | Définir les niveaux de stock auxquels comparer la situation connue ou attendue selon le compromis de service, immobilisation et risque. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D05.d | Group Protection Decision | Validé par l’urbaniste — portée : definition, name | Déterminer les quantités à protéger ou les limites d’usage par canal ou groupe de bénéficiaires. | Déterminer la répartition des droits d’usage du stock entre groupes, en préservant les usages retenus. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D05.e | Replenishment Decision | Validé par l’urbaniste — portée : name | Déterminer les apports successifs et leurs ajustements en quantité et en date pour entretenir la disponibilité pendant la commercialisation, selon les besoins, les objectifs de stock, les apports engagés et les contraintes applicables. | Entretenir la disponibilité en ajustant les apports continus, tout en maîtrisant l’immobilisation et le risque d’excédent. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D05.c | Stock Redistribution Decision | Validé par l’urbaniste — portée : name | Déterminer les transferts de stock existant entre sites pour mieux répondre aux besoins, reconstituer des assortiments utiles ou regrouper des stocks dispersés, en tenant compte des coûts et risques. | Obtenir une répartition du stock mieux adaptée aux besoins des périmètres concernés. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D05.f | Inventory Planning | Validé par l’urbaniste — portée : name | Construire des scénarios alternatifs de stock, simuler et analyser leurs conséquences, puis adapter le scénario en cours à partir des faits, en mobilisant les décisions spécialisées et les capacités responsables de sa mise en action. | Choisir et maintenir une trajectoire de stock cohérente, reliée à sa mise en action et aux faits observés. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D05.g | Initial Stocking Decision | Validé par l’urbaniste — portée : name, definition | Déterminer les quantités à apporter à chaque magasin et leurs dates pour constituer le stock initial nécessaire au lancement, à partir de l’assortiment retenu, des objectifs de stock et des contraintes applicables. | Préparer la disponibilité initiale des produits en magasin, en maîtrisant l’immobilisation et le risque dès le lancement. | En cours d’instruction |
| D05.h | Reservation Policy Decision | Validé par l’urbaniste — portée : name, definition | Déterminer dans quelles situations, à quel moment et pour quelle durée réserver des ressources afin de sécuriser la promesse, selon le risque de pénurie et le coût d’indisponibilité pour les autres demandes. | Choisir comment sécuriser les ressources d’une promesse tout en maîtrisant leur indisponibilité pour les autres demandes. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D05.i | Return Disposition Decision | Validé par l’urbaniste — portée : name, definition, nature | Déterminer le devenir logistique d’un produit retourné, selon son état constaté, les politiques applicables et les possibilités de récupération de valeur. | Retenir une orientation pertinente pour récupérer la valeur des produits retournés et maîtriser leurs coûts et risques. | Validé par l’urbaniste — portée : type, source_id, target_id |

## D06 — Process Management

Statut : **Validé par l’urbaniste — portée : definition, name**.

Orchestrer l’exécution Supply en coordonnant les prestations, en suivant leur réalisation et en adaptant le plan aux aléas, en articulation avec la promesse Supply.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D06.b | Service Capacity Visibility | Validé par l’urbaniste — portée : name | Rendre visible la capacité opérationnelle communiquée par les exécutants, avec son contexte, sa période et sa fraîcheur, pour alimenter les décisions Supply. | Donner à D03 et aux décisions d’exécution une connaissance exploitable des capacités annoncées par les exécutants. | En cours d’instruction |
| D07.a | Service Requirements Decision | Validé par l’urbaniste — portée : name, definition | Déterminer les prestations nécessaires. | Déterminer les résultats de prestation nécessaires à la réalisation du besoin Supply. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D07.b | Service Order Management | Validé par l’urbaniste — portée : name, definition | Gérer les demandes de prestation adressées aux exécutants et leur cycle de vie : émission, acceptation ou refus, modification, annulation et clôture, selon le service. | Tenir les demandes de prestation, leur prise en charge et leurs évolutions de façon explicite et traçable. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D07.c | Service Reconciliation | En cours d’instruction | Rapprocher les résultats constatés des prestations attendues, qualifier les écarts et fournir les faits utiles aux domaines consommateurs. | Expliquer les écarts de réalisation et alimenter le rapprochement des Orders sans confondre leurs reliquats. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D07.d | Operations Tracking | Validé par l’urbaniste — portée : name | Suivre les faits, jalons, estimations et résultats encore attendus des prestations pendant leur réalisation. | Donner une connaissance actualisée de l’exécution pour anticiper les écarts et permettre l’adaptation. | Validé par l’urbaniste — portée : type, source_id, target_id |
| D06.d | Process Orchestration | Validé par l’urbaniste — portée : name, definition | Coordonner les prestations et leurs dépendances. | Coordonner la réalisation du plan retenu entre les exécutants. | Proposé par l’IA |
| D06.e | Service Selection Decision | Validé par l’urbaniste — portée : name | Déterminer les services et exécutants à mobiliser pour les prestations nécessaires, en tenant compte de leur admissibilité et des contraintes. | Retenir des services utilisables pour réaliser les prestations requises dans le cadre Supply applicable. | Proposé par l’IA |
| D06.f | Process Adaptation Decision | Validé par l’urbaniste — portée : name, definition | Déterminer les variations du plan. | Retenir une variation de réalisation adaptée à l’aléa et aux contraintes Supply. | Validé par l’urbaniste — portée : type, source_id, target_id |

## D09 — Party / Role

Statut : **Validé par l’urbaniste — portée : mastership, name**.

Recevoir les références des parties et leurs rôles métier, distincts des habilitations RBAC. L’identité sans doublon relève du maître externe ; les modèles se relient par identifiants.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D09.d | Party / Role Ingestion | En cours d’instruction | recevoir les parties, leurs identifiants, rôles et relations de référence ainsi que leurs évolutions, en conservant les références du maître externe. | Utiliser une identité de référence commune dans les opérations. | Validé par l’urbaniste — portée : source_id, target_id, type |

## D11 — Agreement

Statut : **Validé par l’urbaniste — portée : mastership, name**.

Recevoir et consulter la projection du contrat complet : cadre, conditions particulières, périodes de validité et engagements en quantité ou en valeur, avec identifiants Party et Catalog. Les commandes restent distinctes et consomment les conditions reçues ; administration du contrat maître externe.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D11.a | Agreement Ingestion | En cours d’instruction | Recevoir les contrats clients ou fournisseurs et leurs évolutions, y compris cadre, conditions particulières, périodes et engagements en quantité ou valeur, avec références Party et Catalog et provenance du maître externe. | Mettre les conditions contractuelles de référence à disposition des décisions et engagements transactionnels. | Validé par l’urbaniste — portée : source_id, target_id, type |

## D08 — Product Reference

Statut : **Proposé par l’IA**.

Recevoir les références Product et leurs Product Variants depuis leurs maîtres externes, indépendamment des catalogues qui les proposent. Product porte un rôle Article ou Container. Distinguer ces références des Product Units, exemplaires physiques suivis dans les opérations ; les identifiants commerciaux ne constituent pas à eux seuls leur identité individuelle.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D08.d | Product Reference Ingestion | En cours d’instruction | Recevoir les références Product, leurs variantes, rôles, identifiants et caractéristiques utiles ainsi que leurs évolutions depuis les maîtres externes, indépendamment de leur présence dans les catalogues. | Reconnaître les mêmes références produit dans les différents catalogues et opérations, sans les confondre avec les exemplaires physiques. | Validé par l’urbaniste — portée : source_id, target_id, type |

## D12 — Catalog

Statut : **Validé par l’urbaniste — portée : mastership, name**.

Recevoir les catalogues construits à l’extérieur et les informations commerciales applicables. Une même référence de produit ou de variante peut figurer dans plusieurs catalogues ; son identité maîtresse relève de Product Reference.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D12.a | Catalog Ingestion | En cours d’instruction | recevoir les catalogues construits à l’extérieur, leurs références de produits, prix, zones géographiques d’application et évolutions. | Permettre de commander et d’utiliser les informations commerciales reçues. | Validé par l’urbaniste — portée : source_id, target_id, type |

## D13 — Fulfillment Network

Statut : **Validé par l’urbaniste — portée : independence, name**.

Recevoir les points du réseau, leurs caractéristiques et relations de référence et leurs liens aux parties responsables. Les lieux restent distincts des parties ; stocks, charge et acheminement choisi appartiennent aux domaines consommateurs.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D13.a | Fulfillment Network Ingestion | En cours d’instruction | recevoir les points du réseau, leurs caractéristiques de référence, leurs relations et liens vers les parties responsables, ainsi que leurs évolutions depuis les sources maîtresses externes. | Donner aux opérations et décisions une connaissance commune du réseau de réalisation. | Validé par l’urbaniste — portée : source_id, target_id, type |

## D14 — Service Catalog

Statut : **Validé par l’urbaniste — portée : definition, name**.

Le référentiel contient la liste des services et leurs SLA globaux en configuration.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D14.a | Service Catalog Ingestion | En cours d’instruction | Recevoir l’offre des services exécutants, leurs SLA configurés, conditions et accès, ainsi que leurs évolutions depuis les sources maîtresses externes. | Mettre à disposition une projection de référence exploitable par la qualification, la promesse et l’orchestration. | Proposé par l’IA |

**Justification de la décomposition — D01.d :** Établir une référence complète sur un périmètre, entretenir la fiabilité par contrôles récurrents et répondre rapidement à une situation ciblée correspondent à trois politiques ou variantes métier, avec des bénéfices distincts. Les mêmes responsabilités de rapprochement et de correction justifiée sont mobilisées ; les interfaces et outils de comptage ne créent pas de comportement supplémentaire.

## Comportements — Stocktaking

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV029 | Periodic Physical Inventory | Validé par l’urbaniste — portée : name, definition | Vérifier l’ensemble du stock d’un périmètre lors d’une campagne, pour établir une référence fiable. |
| BHV030 | Cycle Counting | Validé par l’urbaniste — portée : name, definition | Vérifier régulièrement des sélections d’articles ou d’emplacements, avec une fréquence adaptée aux enjeux. |
| BHV031 | Spot Counting | Validé par l’urbaniste — portée : name, definition | Vérifier ponctuellement un stock ciblé lorsqu’une situation le justifie. |

**Justification de la décomposition — D02.b :** Préserver un accès, limiter une consommation, absorber l’incertitude et réguler les apports répondent à des risques différents ; mécanismes combinables, pas étapes d’un cycle.

## Comportements — Supply Protection

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV017 | Group Supply Protection | Validé par l’urbaniste — portée : name | Configurer les droits préservant l’accès d’un groupe à des ressources face aux usages concurrents. |
| BHV018 | Consumption Capping | Validé par l’urbaniste — portée : name | Configurer les limites de consommation d’un groupe sur le périmètre et la période retenus. |
| BHV019 | Safety Stock Policy | Validé par l’urbaniste — portée : name | Configurer le stock tampon et ses conditions d’utilisation pour absorber les incertitudes. |
| BHV020 | Replenishment Regulation | Validé par l’urbaniste — portée : name | Configurer les règles de déclenchement et de limitation du réassort qui encadrent le renouvellement du stock. |

**Justification de la décomposition — D02.e :** Trois mécanismes combinables apportent des bénéfices distincts : application traçable d’un plan retenu, stabilité en complétant sans remettre en jeu les liens existants, adaptation collective en révisant les liens autorisés. Le choix de préserver ou réviser change les pratiques de préparation et les engagements à coordonner ; il ne se réduit pas à une opération CRUD ou une optimisation technique de calcul. L’application d’un plan peut mobiliser l’une ou l’autre politique.

## Comportements — Supply Assignment

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV045 | Supply Assignment Plan Application | En cours d’instruction | Appliquer les affectations d’un plan retenu, en contrôlant qu’elles restent applicables et en signalant les écarts. |
| BHV046 | Incremental Supply Assignment | Validé par l’urbaniste — portée : definition | Compléter les besoins non affectés tout en préservant les affectations existantes. |
| BHV047 | Supply Reassignment | Validé par l’urbaniste — portée : definition | Réviser les affectations modifiables pour appliquer de nouveaux arbitrages entre commandes. |

**Justification de la décomposition — D03.i :** Quatre différences combinables modifient les possibilités : droits engagés, réseau, mobilisation et ressources futures ; aucun comportement par lieu ou technologie.

## Comportements — Available-to-Promise (ATP)

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV001 | Existing Commitment Consideration | Validé par l’urbaniste — portée : definition | Établir les quantités admissibles pour la demande en tenant compte des allocations, protections et réservations, sans double décompte. |
| BHV002 | Network Stock Availability | Validé par l’urbaniste — portée : definition | Établir les possibilités de satisfaction à partir des lieux admissibles, entrepôts, magasins, darkstores ou autres espaces de stockage. |
| BHV003 | Operational Availability Timing | Validé par l’urbaniste — portée : definition | Déterminer quand une quantité peut effectivement contribuer à la promesse selon sa disponibilité opérationnelle. |
| BHV004 | Future Supply Projection | Validé par l’urbaniste — portée : definition | Établir les possibilités à l’échéance en intégrant les réceptions attendues et les engagements concurrents, pour une promesse ou un ensemble. |

**Justification de la décomposition — D03.j :** Distinguer trois leviers métier : obtenir davantage de ressources, changer la solution de satisfaction, ou réexaminer des engagements existants. Les conditions, les parties concernées et les conséquences diffèrent réellement. La décomposition rend explicite ce qui doit changer pour rendre une commande satisfaisable, sans confondre faisabilité, choix collectif et application. Plusieurs leviers peuvent se combiner.

## Comportements — Capable-to-Promise (CTP)

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV075 | Additional Supply Feasibility | Validé par l’urbaniste — portée : name, definition | Les possibilités de satisfaire la demande en obtenant des ressources supplémentaires, avec quantités, dates et conditions de disponibilité. |
| BHV076 | Fulfillment Alternative Feasibility | Validé par l’urbaniste — portée : name, definition | Les possibilités obtenues en modifiant les modalités de satisfaction par rapport à la situation de référence. |
| BHV077 | Commitment Rebalancing Feasibility | Validé par l’urbaniste — portée : name, definition | Les possibilités obtenues en révisant des engagements modifiables, en explicitant les conséquences sur les commandes concernées. |

**Justification de la décomposition — D04.i :** Livraison, retrait, livraison fournisseur et relation intersociétés changent la prise en charge de la commande, la preuve de satisfaction et les engagements à coordonner. Ces parcours doivent se lire dans la capacité.

## Comportements — Sales Order

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV066 | Ship to Customer | Validé par l’urbaniste — portée : name, definition | Prendre en charge la commande à livrer au client depuis le réseau : entrepôt, magasin ou autre lieu admissible. |
| BHV067 | Customer Pickup | Validé par l’urbaniste — portée : name, definition | Prendre en charge la mise à disposition et le retrait au lieu convenu. Une commande prête reste distincte d’une commande effectivement retirée. |
| BHV068 | Direct Delivery | Validé par l’urbaniste — portée : name, definition | Prendre en charge la commande dont le fournisseur livre directement le client, en coordonnant les attendus de vente et d’achat. |
| BHV069 | Intercompany Sales | Validé par l’urbaniste — portée : name, definition | Prendre en charge une vente entre entités juridiques du groupe, avec cohérence entre engagements de vente et d’achat. |

**Justification de la décomposition — D04.j :** Les parcours changent la nature de l’attendu, la destination, les dépendances entre commandes et les preuves de réalisation : apport en stock, livraison directe au client, prestation. Cette différence métier justifie la décomposition sans recopier le cycle de vie commun. Supplier Confirmation ajoute le mécanisme de construction d’un engagement avec une autre partie, qui peut répondre autrement que demandé : cette différence change le pilotage de l’achat et la fiabilité des ressources attendues. Il se combine avec les trois parcours ; les opérations accepter, refuser et reconfirmer ne sont pas des comportements séparés.

## Comportements — Purchase Order

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV058 | Stock Procurement | Validé par l’urbaniste — portée : name, definition | Acheter des marchandises destinées au stock du réseau ; suivre les quantités et dates restant à recevoir. |
| BHV059 | Direct Delivery | Validé par l’urbaniste — portée : name, definition | Acheter des marchandises livrées directement par le fournisseur au client ; coordonner les attentes des commandes d’achat et de vente. |
| BHV060 | Service Procurement | Validé par l’urbaniste — portée : name, definition | Acheter une prestation ; suivre ce qui est attendu puis reconnu réalisé. |
| BHV078 | Supplier Confirmation | Validé par l’urbaniste — portée : name, definition | Prendre en charge l’établissement et les révisions de l’engagement fournisseur sur une commande d’achat, en distinguant la demande, la réponse fournisseur et les conditions finalement acceptées. |

**Justification de la décomposition — D04.k :** Les transferts servent des intentions distinctes : démarrer un stock, l’alimenter, le rééquilibrer, le regrouper ou satisfaire une commande identifiée. L’attendu et la justification doivent rester lisibles même lorsque le transport ou l’outil est commun.

## Comportements — Transfer Order

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV070 | Initial Stocking | Validé par l’urbaniste — portée : name, definition | Porter les transferts constituant le stock de départ : implantation d’une saison, d’une capsule ou d’un nouveau lieu. |
| BHV071 | Continuous Replenishment | Validé par l’urbaniste — portée : name, definition | Porter les transferts alimentant régulièrement un lieu pendant l’activité. |
| BHV072 | Inventory Rebalancing | Validé par l’urbaniste — portée : name, definition | Porter les transferts corrigeant un déséquilibre entre lieux, par exemple d’un magasin disposant d’un excédent vers un magasin qui manque de stock. |
| BHV073 | Stock Consolidation | Validé par l’urbaniste — portée : name, definition | Porter les transferts regroupant des stocks dispersés : reconstitution de tailles, concentration ou rapatriement de reliquats. |
| BHV074 | Order-Driven Transfer | Validé par l’urbaniste — portée : name, definition | Porter un transfert nécessaire à une commande identifiée, en conservant son lien et son échéance. |

**Justification de la décomposition — D04.l :** Les parcours diffèrent par le devenir attendu, les responsabilités sollicitées, les immobilisations et les preuves nécessaires pour considérer le retour traité. Cette complexité justifie des comportements métier ; les étapes de saisie, inspection, validation et clôture ne constituent pas chacune un comportement.

## Comportements — Customer Return

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV050 | Return to Stock | Validé par l’urbaniste — portée : name, definition | Prendre en charge la remise en disponibilité du produit. |
| BHV051 | Repair and Refurbishment | Validé par l’urbaniste — portée : name, definition | Prendre en charge une remise en état, suivre son résultat et la suite attendue. |
| BHV052 | Return to Supplier | Validé par l’urbaniste — portée : name, definition | Relier le retour client à sa prise en charge par Supplier Return. |
| BHV053 | Return to Customer | Validé par l’urbaniste — portée : name, definition | Prendre en charge la restitution du produit au client, après réparation ou décision de non-reprise. |
| BHV054 | Scrapping | Validé par l’urbaniste — portée : name, definition | Prendre en charge la mise au rebut retenue : conserver l’autorisation, suivre la réalisation et rapprocher la preuve avec la sortie de stock. |

**Justification de la décomposition — D04.m :** Le retour sans remplacement éteint l’attente de marchandises au titre des quantités reprises ; le retour avec remplacement conserve un apport attendu. Cette différence change le suivi des quantités, des dates et des engagements aval. Elle justifie deux parcours métier, indépendamment des motifs du retour et des interfaces. Le retour pour réparation ajoute un attendu distinct : récupérer le même bien remis en état, avec sa traçabilité et son immobilisation, plutôt que recevoir un autre produit.

## Comportements — Supplier Return

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV055 | Return for Credit | Validé par l’urbaniste — portée : name, definition | Prendre en charge un retour fournisseur donnant lieu à un avoir ou remboursement attendu, sans remplacement des marchandises retournées. |
| BHV056 | Return for Replacement | Validé par l’urbaniste — portée : name, definition | Prendre en charge un retour associé à un remplacement attendu, en conservant les liens entre marchandises renvoyées et apports de remplacement. |
| BHV057 | Return for Repair | Validé par l’urbaniste — portée : name | Prendre en charge l’envoi d’un bien au fournisseur pour réparation puis sa récupération, en préservant son identité et l’attendu de restitution. |

**Justification de la décomposition — D04.n :** La scission permet à des parties d’une demande de devenir traitables distinctement tout en préservant filiation, quantités et engagements. Cette complexité et ce bénéfice justifient Order Splitting comme comportement de Structuring. La composition persistante demeure dans la responsabilité large de la capacité, sans comportement créé pour chaque opération de regroupement.

## Comportements — Order Structuring

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV044 | Order Splitting | En cours d’instruction | Scinder un Order ou ses éléments en parties traitables distinctement, en préservant la filiation, la cohérence des quantités et les engagements applicables. |

**Justification de la décomposition — D04.o :** Une commande peut être ferme, partiellement libérée, gelée sur certains éléments et suspendue sur une progression, tandis qu’une modification reste en brouillon. Ces effets distincts et leurs contraintes de combinaison justifient six mécanismes métier, sans comportement par état ni cycle linéaire universel. Préparation/révision distingue contenu applicable et proposé ; fin de la demande préserve la différence entre retrait du besoin et clôture.

## Comportements — Order Lifecycle Management

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV036 | Order Firming | Validé par l’urbaniste — portée : name, definition | Transformer une intention planifiée en ordre ferme, avec les engagements et restrictions de révision associés. |
| BHV037 | Order Freezing | Validé par l’urbaniste — portée : name | Protéger les éléments désignés d’un Order contre leur modification par les réoptimisations, en explicitant la portée du gel et les conditions autorisées de révision. |
| BHV038 | Order Preparation & Revision | En cours d’instruction | Gouverner la préparation et la prise d’effet du contenu initial ou révisé d’un Order, en distinguant le contenu applicable des modifications en préparation et en préservant les engagements et réalisations acquis. |
| BHV039 | Order Release | Validé par l’urbaniste — portée : name, definition | Autoriser la prise en charge de tout ou partie d’un Order, ou d’un ensemble d’Orders liés, lorsque les conditions de lancement individuelles et collectives sont satisfaites. |
| BHV040 | Order Hold & Resume | Validé par l’urbaniste — portée : name | Suspendre une progression désignée pour un motif métier puis permettre sa reprise lorsque les conditions de levée sont réunies. |
| BHV043 | Order Termination | En cours d’instruction | Gouverner le retrait autorisé de tout ou partie du besoin et la clôture de son suivi opérationnel, en préservant les réalisations acquises et en explicitant le devenir du reliquat. |

**Justification de la décomposition — D05.a :** Trois façons de déterminer les cibles selon la demande servie et le périmètre d’arbitrage : disponibilité client et contraintes locales du magasin ; alimentation de la demande aval du centre de distribution ; coordination des protections et des cibles entre échelons interdépendants. Le bénéfice est de rendre explicites les compromis locaux et globaux sans créer un comportement par type de bâtiment ni une séquence imposée.

## Comportements — Inventory Target Decision

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV026 | Store Inventory Optimization | Validé par l’urbaniste — portée : name | Déterminer les objectifs et seuils de stock d’un magasin pour assurer la disponibilité client, selon la demande locale, l’assortiment retenu, les contraintes de présentation et de capacité, les délais de réassort et le risque d’excédent. |
| BHV027 | Distribution Center Inventory Optimization | Validé par l’urbaniste — portée : name | Déterminer les objectifs et seuils de stock d’un centre de distribution pour servir les magasins ou canaux desservis, selon leurs besoins prévus, les délais fournisseurs, les aléas d’approvisionnement et les contraintes de stockage. |
| BHV028 | Multi-Echelon Inventory Optimization | Validé par l’urbaniste — portée : name, definition | Déterminer conjointement les objectifs de stock de plusieurs échelons du réseau, en tenant compte de leurs dépendances, pour atteindre le service recherché au meilleur compromis de stock et de risque. |

**Justification de la décomposition — D05.e :** Deux politiques produisent des apports selon des logiques métier distinctes : satisfaire des besoins datés ou rétablir une cible de stock. L’ajustement des apports existants ajoute un mécanisme combinable qui évite de répondre à tout changement par une commande supplémentaire et traite pénuries, excédents ou décalages sous engagements. Cette différence et ce bénéfice justifient les trois comportements ; seuils, périodes et tailles de lot restent des paramètres. Détermination des cibles, décision d’apports, application aux Orders et réalisation restent distinctes.

## Comportements — Replenishment Decision

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV083 | Requirement-based Replenishment | Validé par l’urbaniste — portée : name, definition | Déterminer les apports pour satisfaire des besoins datés, après déduction des ressources utilisables et des apports attendus. |
| BHV084 | Target-based Replenishment | Validé par l’urbaniste — portée : name, definition | Déterminer les apports pour retrouver une cible de stock selon les seuils applicables, sans nécessiter une commande identifiée pour chaque apport. |
| BHV085 | Replenishment Adjustment | Validé par l’urbaniste — portée : name, definition | Déterminer comment modifier les apports déjà prévus pour éviter pénuries, excédents ou décalages, en respectant les engagements. |

**Justification de la décomposition — D05.c :** Distinguer deux mécanismes aux bénéfices différents : améliorer la couverture des lieux receveurs en préservant les donneurs, ou réduire la fragmentation du stock par concentration, avec reconstitution d’assortiments ou regroupement de reliquats même sans manque immédiat à destination.

## Comportements — Stock Redistribution Decision

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV024 | Inventory Rebalancing | Validé par l’urbaniste — portée : definition | Déplacer du stock vers les lieux qui en ont davantage besoin, en préservant les besoins des donneurs. |
| BHV025 | Stock Consolidation | Validé par l’urbaniste — portée : definition | Regrouper des quantités fragmentées pour leur redonner une utilité ou libérer des sites. |

**Justification de la décomposition — D05.f :** Explorer des alternatives, comprendre leurs conséquences et adapter un scénario engagé changent les pratiques de planification et leur articulation avec l’exécution.

## Comportements — Inventory Planning

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV005 | Scenario Construction | Validé par l’urbaniste — portée : name | Construire plusieurs réponses possibles en explicitant leurs hypothèses, objectifs et contraintes. |
| BHV006 | Simulation & Analysis | Validé par l’urbaniste — portée : name | Projeter les conséquences d’un scénario et analyser leurs impacts sur les indicateurs métier et les processus pour éclairer les choix. |
| BHV016 | Scenario Execution Adaptation | Validé par l’urbaniste — portée : name | Adapter le scénario de stock en cours aux écarts observés, compte tenu des actions engagées et des décisions spécialisées. |

**Justification de la décomposition — D07.d :** Les trois périmètres physiques rendent lisibles les situations et opérations propres à l’entrepôt, au transport et au magasin ; livré ne signifie pas mis en rayon. Le suivi transversal des processus explique les résultats, attentes et blocages métier en reliant Tasks et appels sous-jacents. Ce sont des perspectives combinables aux bénéfices distincts, sans sous-comportements ni découpage par bouton, interface ou fournisseur.

## Comportements — Operations Tracking

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV079 | Warehouse Visibility | Validé par l’urbaniste — portée : name, definition | Réception, manutention, préparation et expédition dans les entrepôts et plateformes. |
| BHV080 | Transportation Visibility | Validé par l’urbaniste — portée : name, definition | Acheminements, progression, arrivées estimées et remise au destinataire. |
| BHV081 | Store Visibility | Validé par l’urbaniste — portée : name, definition | Réception magasin, passage en réserve, mise en rayon et réassort de la surface de vente. |
| BHV082 | Process Tracking | Validé par l’urbaniste — portée : name, definition | Suivre l’avancement des processus d’exécution Supply et de leurs Tasks métier, en reliant chaque Task aux prestations et appels de services qui contribuent à sa réalisation, pour rendre explicites les résultats acquis, les attentes, les échecs et leurs conséquences sur la progression. |

**Justification de la décomposition — D03.n :** Distinguer proposition, établissement de l’engagement et réexamen de cet engagement : trois façons d’agir avec effets différents, sans multiplier les capacités d’action.

## Comportements — Promise Management

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV021 | Promise Proposal | Validé par l’urbaniste — portée : name | Construire une proposition de mise à disposition de ressources pour honorer une commande Supply, précisant quantités, dates, conditions et alternatives possibles, à partir des ressources et possibilités de réalisation. |
| BHV022 | Promise Confirmation | Validé par l’urbaniste — portée : name | établir les quantités et dates promises, en distinguant la part confirmée de celle qui ne l’est pas. |
| BHV023 | Promise Revision | Validé par l’urbaniste — portée : name | Réexaminer les promesses lorsque les ressources, commandes, dates ou priorités changent et établir les modifications autorisées. |

**Justification de la décomposition — D05.h :** Le jalon du parcours, la proximité du besoin, la différenciation des engagements de service et l’adaptation au risque changent chacun la façon de sécuriser une promesse et le coût d’immobilisation. Quatre mécanismes combinables sont retenus U343 ; durées, seuils, canaux et interfaces restent des paramètres ou des contextes. La complexité visée est l’arbitrage de ces mécanismes sans retirer implicitement les garanties existantes.

## Comportements — Reservation Policy Decision

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV032 | Milestone-Based Reservation Policy | Validé par l’urbaniste — portée : name | Déterminer les événements du parcours métier à partir desquels la ressource doit être réservée, puis les conditions de maintien de cette protection au fil du parcours. |
| BHV033 | Time-Fenced Reservation Policy | Validé par l’urbaniste — portée : name | Déterminer à quelle distance de la date de besoin commencer à réserver, afin de sécuriser l’échéance sans immobiliser trop tôt les ressources. |
| BHV034 | Demand-Differentiated Reservation Policy | Validé par l’urbaniste — portée : name | Déterminer des conditions de réservation différentes selon les engagements de service attachés aux demandes, aux clients ou aux canaux, en respectant les priorités et droits d’usage établis. |
| BHV035 | Risk-Adaptive Reservation Policy | Validé par l’urbaniste — portée : name | Adapter les conditions de déclenchement et de durée de réservation à la tension sur les ressources et au risque d’immobilisation inutile, dans les limites des engagements déjà accordés. |

**Justification de la décomposition — D05.i :** Distinguer les cas dont la disposition est déterminée par une politique connue des cas nécessitant un arbitrage contextuel entre plusieurs devenirs autorisés ; rendre visibles la standardisation des prises en charge et la récupération de valeur, sans imposer une technologie de décision.

## Comportements — Return Disposition Decision

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV048 | Policy-based Disposition | Validé par l’urbaniste — portée : name, definition | Déterminer l’orientation selon une politique établie, en fonction de l’état du produit, de sa catégorie et des conditions applicables. |
| BHV049 | Value Recovery Optimization | Validé par l’urbaniste — portée : name, definition | Comparer plusieurs devenirs autorisés selon la valeur récupérable, les coûts, les délais et les risques. |

**Justification de la décomposition — D04.r :** Rendre lisibles les deux intentions d’apport : établir le stock de départ à une échéance de lancement, puis entretenir son alimentation pendant l’activité. La différence de finalité et de résultat attendu est utile même si le traitement est commun.

## Comportements — Consignment Replenishment Order

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV061 | Initial Stocking | Validé par l’urbaniste — portée : name, definition | Prendre en charge l’apport initial de stock consigné pour une saison, une capsule ou un lancement, et suivre sa satisfaction avant l’échéance de démarrage. |
| BHV062 | Continuous Replenishment | Validé par l’urbaniste — portée : name, definition | Prendre en charge les apports successifs de stock consigné pendant l’activité, selon l’évolution du besoin, et suivre leur satisfaction. |

**Justification de la décomposition — D01.h :** Les obligations sur le stock diffèrent selon consommation, durée contractuelle ou sortie sans acquisition ; expliciter ce qui change la propriété et ce qui met fin à la détention évite de confondre mouvement et achat.

## Comportements — Consigned Inventory Management

Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.

| Repère | Comportement | Statut | Définition |
| --- | --- | --- | --- |
| BHV063 | Consumption-Based Ownership Transfer | Validé par l’urbaniste — portée : name, definition | Appliquer le transfert de propriété lors de la vente ou consommation prévue par l’accord. |
| BHV064 | Aging-Based Ownership Transfer | Validé par l’urbaniste — portée : name, definition | Appliquer l’acquisition à l’échéance d’une durée contractuelle. |
| BHV065 | Consignment Exit | Validé par l’urbaniste — portée : name, definition | Prendre en charge une sortie autorisée de la consignation ou de la détention : reprise fournisseur, orientation vers un soldeur, seconde main ou destruction selon l’accord et la décision retenue. |

## Comparaison par rapport au marché — D01.d Stocktaking

### SAP — Physical Inventory

SAP S/4HANA Cloud Public Edition Warehouse Management · Procédures métier et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Distingue inventaire périodique, procédures continues et cycle counting ; confronte quantités physiques et enregistrées.

**Différences.** Périmètre produit Warehouse Management ; aucune attribution automatique à FLOW des opérations WMS, ni obligation comptable ajoutée.

**Position FLOW.** U334 adopte Periodic Physical Inventory, Cycle Counting et Spot Counting sous Stocktaking, ainsi que la politique et les demandes de vérification. Réalisation physique par les exécutants ; traitement des écarts commun et ajustements tracés par Record Inventory Movements. Comparaison produit proposée ; aucun déploiement déduit.

[Physical Inventory](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/ae735d9f76024645ad4f5b1a0e6e3387.html) — 2608, consulté le 2026-09-18.

**Passage.** Physical inventory procedures

**Limite de preuve.** Texte primaire indexé consulté. Aucun déploiement Beaumanoir attesté ; différences de taxonomie conservées.

Références : U333, ELM207, CMP115, U334.

### Oracle — Counting — full physical inventory / cycle counting

E-Business Suite Mobile Supply Chain Applications · Procédures métier et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Oppose le comptage périodique de sélections d’articles au comptage physique complet pour rapprocher les quantités.

**Différences.** Référence EBS, pas Fusion Cloud ; les contraintes de blocage transactionnel du produit ne sont pas imposées à FLOW.

**Position FLOW.** U334 adopte Periodic Physical Inventory, Cycle Counting et Spot Counting sous Stocktaking, ainsi que la politique et les demandes de vérification. Réalisation physique par les exécutants ; traitement des écarts commun et ajustements tracés par Record Inventory Movements. Comparaison produit proposée ; aucun déploiement déduit.

[Counting — full physical inventory / cycle counting](https://docs.oracle.com/cd/E26401_01/doc.122/e48826/T256582T257763.htm) — 12.2, consulté le 2026-09-18.

**Passage.** Counting ; Cycle Counting

**Limite de preuve.** Texte primaire indexé consulté. Aucun déploiement Beaumanoir attesté ; différences de taxonomie conservées.

Références : U333, ELM207, CMP115, U334.

### Microsoft — Cycle counting

Dynamics 365 SCM Warehouse Management · Procédures métier et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Plans récurrents, seuils déclenchant un comptage et comptage ponctuel sans travail préexistant ; traitement des différences constatées.

**Différences.** Spot ne signifie pas exclusivement déclenché par anomalie. Un seuil de comptage ne prouve pas une incohérence ; ce n’est pas un seuil de réassort. Les modalités produit se combinent et ne forment pas trois capacités universelles.

**Position FLOW.** U334 adopte Periodic Physical Inventory, Cycle Counting et Spot Counting sous Stocktaking, ainsi que la politique et les demandes de vérification. Réalisation physique par les exécutants ; traitement des écarts commun et ajustements tracés par Record Inventory Movements. Comparaison produit proposée ; aucun déploiement déduit.

[Cycle counting](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Automatically create cycle counting work ; Spot cycle counting ; Resolve cycle counting differences

**Limite de preuve.** Texte primaire indexé consulté. Aucun déploiement Beaumanoir attesté ; différences de taxonomie conservées.

Références : U333, ELM207, CMP115, U334.

## Comparaison par rapport au marché — D03 Order Backlog Management

### Oracle — Start Backlog Planning

Fusion Cloud SCM 26B · Processus et fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Prioriser et replannifier la satisfaction sur l’ensemble du carnet à partir des ressources et demandes actualisées.

**Différences.** Documentation d’un produit et de son traitement planifié, pas taxonomie de capacités ni preuve de prise en charge de tous les types d’Orders FLOW.

**Position FLOW.** D03 Order Backlog Management : les décisions spécialisées alimentent le travail collectif du carnet. D04 conserve la demande selon son intention, D06 orchestre les services. Rattachements de préparation/release en réexamen ciblé.

[Start Backlog Planning](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspc/start-backlog-planning.html) — 26B, consulté le 2026-09-19.

**Passage.** Introduction ; When to Use

**Limite de preuve.** Source primaire ouverte lors de la discussion ; aucune preuve de déploiement Beaumanoir. Niveaux et périmètres produits non transposés automatiquement.

Références : U411, U412, U413, ELM246, CMP157.

### Oracle — Key Actions on Orders

Fusion Cloud SCM 25D · Fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Travail du carnet, priorisation, simulation puis transmission des résultats retenus à Order Management.

**Différences.** Release Planning Results transmet des résultats de planification ; ce n’est pas une équivalence exacte de l’autorisation FLOW vers les processus. La séparation demande/carnet/processus est la convention FLOW.

**Position FLOW.** D03 Order Backlog Management : les décisions spécialisées alimentent le travail collectif du carnet. D04 conserve la demande selon son intention, D06 orchestre les services. Rattachements de préparation/release en réexamen ciblé.

[Key Actions on Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faubm/key-actions-on-orders.html) — 25D, édition explicitement consultée, consulté le 2026-09-19.

**Passage.** Plan Run Actions ; Attribute Data Simulation Actions ; Release Actions

**Limite de preuve.** Source primaire ouverte lors de la discussion ; aucune preuve de déploiement Beaumanoir. Niveaux et périmètres produits non transposés automatiquement.

Références : U411, U412, U413, ELM246, CMP157.

### Microsoft — View, manage, and approve planned orders

Dynamics 365 Supply Chain Management · Pratique et fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Revoir et modifier les ordres planifiés, approuver les ajustements et préparer leur affermissement ; conservation des ajustements approuvés sous conditions lors des planifications suivantes.

**Différences.** Approvisionnements planifiés de production, achat et transfert. Aucun équivalent universel aux commandes clients, retours ou à tout le carnet FLOW ; approbation, affermissement et release restent distincts.

**Position FLOW.** D03 Order Backlog Management : les décisions spécialisées alimentent le travail collectif du carnet. D04 conserve la demande selon son intention, D06 orchestre les services. Rattachements de préparation/release en réexamen ciblé.

[View, manage, and approve planned orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/approved-planned-order) — Page mise à jour le 2 septembre 2026, consulté le 2026-09-19.

**Passage.** View and edit the status of planned orders ; Approve planned orders

**Limite de preuve.** Source primaire ouverte lors de la discussion ; aucune preuve de déploiement Beaumanoir. Niveaux et périmètres produits non transposés automatiquement.

Références : U411, U412, U413, ELM246, CMP157.

## Comparaison par rapport au marché — D02.e Supply Assignment

### SAP — Supply Assignment (ARun)

S/4HANA aATP · Mécanisme métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Affectation des ressources aux besoins ; accès par BOP, ITA, affectation immédiate et API.

**Différences.** Fonctionnalité intégrée ; ni couverture de toutes les capacités FLOW ni réalisation exclusivement batch démontrées.

**Position FLOW.** U345/C99 : Supply Assignment porte l’application des affectations d’un plan ; décisions spécialisées et autres capacités gardent leurs responsabilités. Les recommandations éclairent Simulation & Analysis sans constituer un engagement.

[Supply Assignment (ARun)](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/d335e3418f4348ffbae9f11888a62cc7.html) — 2025 FPS01, consulté le 2026-09-18.

**Passage.** Introduction et modes d’accès

**Limite de preuve.** Documentation primaire consultée, texte indexé SAP et page Microsoft ouverte ; aucune réalisation Beaumanoir démontrée.

Références : U345, C99, ELM215, CMP123.

### SAP — Backorder Processing — Reassignment

S/4HANA aATP · Mécanisme métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Le traitement peut conserver les affectations et compléter le reliquat, ou les réexaminer. Le mode preview ne produit pas d’effets logistiques.

**Différences.** Regroupement produit de décisions et d’action ; pas preuve qu’un plan externe arbitraire est importable ou qu’une simulation est appliquée sans recontrôle.

**Position FLOW.** U345/C99 : Supply Assignment porte l’application des affectations d’un plan ; décisions spécialisées et autres capacités gardent leurs responsabilités. Les recommandations éclairent Simulation & Analysis sans constituer un engagement.

[Backorder Processing — Reassignment](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html) — 2025 FPS01, consulté le 2026-09-18.

**Passage.** Reassignment ; Requirement Sorting ; Supply Selection ; Release Check

**Limite de preuve.** Documentation primaire consultée, texte indexé SAP et page Microsoft ouverte ; aucune réalisation Beaumanoir démontrée.

Références : U345, C99, ELM215, CMP123.

### SAP — Steps in Order Allocation Run — Allocation

ERP Fashion Management · Stratégie de répartition dans un processus produit · Recouvrement partiel · statut : proposed

**Points communs.** ARun peut affecter le stock selon FIFO ou une répartition proportionnelle fondée sur les quantités demandées (spread logic). Le regroupement des besoins est un prérequis au Spread.

**Différences.** Référence ERP Fashion, sans garantie pour toute édition aATP. ARun est le processus intégré ; Spread une de ses stratégies. La répartition ne nécessite pas la création de nouvelles commandes.

**Position FLOW.** Spread est une politique de répartition des ressources entre commandes. Les décisions déterminent les parts ; Supply Assignment applique les liens. Aucun agrégat décisionnel ou comportement automatique ajouté. U363 applique la structure ; les correspondances marché restent proposées.

[Steps in Order Allocation Run](https://help.sap.com/docs/SAP_ERP_SPV/f48e74ad3b3740bc8c9eaade394a3c1e/3d1df055aa2a6d55e10000000a4450e5.html) — Édition non relevée dans le passage indexé ; SAP ERP Fashion Management, consulté le 2026-09-18.

**Passage.** Requirement Grouping ; Allocation ; Release Rules

**Limite de preuve.** Passage primaire indexé consulté, complété par Allocation déjà documenté ELM222. Aucune preuve de configuration ou version Beaumanoir.

Références : U361, ELM223, CMP132, U363, CMP133.

### Microsoft — Keep supply for confirmed demand

Dynamics 365 SCM · Fonction produit ou mécanisme technique ; pas capacité FLOW par défaut · Recouvrement partiel · statut : proposed

**Points communs.** Préserve une chaîne liée à une demande confirmée, notamment ordres planifiés et liens de pegging, entre les passages de planification.

**Différences.** Comportement paramétré ; la conservation du stock reçu hors positive days exige un paramètre complémentaire. Ne prouve aucun déploiement Beaumanoir.

**Position FLOW.** Appui à la stabilité des affectations, mais périmètre produit plus large incluant la chaîne de planification. Ne démontre pas une équivalence exacte avec Incremental Supply Assignment.

[Keep supply for confirmed demand](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand) — Prérequis documenté : 10.0.48 build 10.0.2645.33 ou ultérieur, consulté le 2026-09-18.

**Passage.** What data is preserved ; Control how on-hand inventory is pegged ; Interaction with approved planned orders

**Limite de preuve.** Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.

Références : U346, U347, ELM216, CMP124.

## Comparaison par rapport au marché — D03.j Capable-to-Promise (CTP)

### Microsoft — Calculate delivery dates using CTP

Dynamics 365 Supply Chain Management / Planning Optimization · Mécanisme ou processus produit · Recouvrement partiel · statut : proposed

**Points communs.** CTP vérifie matières et capacités pour déterminer les dates réalisables, notamment pour assembler ou produire à la demande.

**Différences.** Appui au mécanisme d’apport supplémentaire ; le CTP FLOW est plus large que ce cas de fabrication. Aucun processus de production interne FLOW ni équivalence de taxonomie déduit.

**Position FLOW.** Trois mécanismes combinables sous CTP, noms FLOW ; faisabilité distincte du scénario collectif et de sa mise en application.

[Calculate delivery dates using CTP](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp) — Documentation évolutive ; mise à jour affichée 2026-07-27, consulté le 2026-09-18.

**Passage.** How CTP compares to ATP ; exemple de fabrication de A à partir de B et C

**Limite de preuve.** Texte primaire consulté ; aucune taxonomie universelle ni preuve de déploiement Beaumanoir.

Références : U402, ELM241, CMP152.

### SAP — Alternative-Based Confirmation

SAP S/4HANA aATP · Mécanisme ou processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Alternative-Based Confirmation examine des sites alternatifs et des produits de substitution selon des règles.

**Différences.** SAP expose ABC sous aATP. FLOW distingue alternatives déjà admissibles (ATP) et adaptations de la référence (CTP). L’exemple express est une illustration FLOW ; cette page ne prouve pas un mécanisme ABC de choix de transport express.

**Position FLOW.** Trois mécanismes combinables sous CTP, noms FLOW ; faisabilité distincte du scénario collectif et de sa mise en application.

[Alternative-Based Confirmation](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5) — S/4HANA ; cours couvrant plusieurs évolutions, consulté le 2026-09-18.

**Passage.** Advanced ATP Scenario: Alternative-Based Confirmation (ABC)

**Limite de preuve.** Texte primaire consulté ; aucune taxonomie universelle ni preuve de déploiement Beaumanoir.

Références : U402, ELM241, CMP152.

### SAP — Exploring Backorder Processing

SAP S/4HANA Cloud Public Edition / Backorder Processing · Mécanisme ou processus produit · Recouvrement partiel · statut : proposed

**Points communs.** BOP réexamine les confirmations selon disponibilités et priorités, avec stratégies de préservation, amélioration et redistribution.

**Différences.** Le processus SAP traverse plusieurs responsabilités FLOW : faisabilité CTP, décision collective, priorités, révision de promesse et application des affectations. BOP ne correspond pas à un comportement CTP unique ni à une autorité de CTP pour choisir les perdants.

**Position FLOW.** Trois mécanismes combinables sous CTP, noms FLOW ; faisabilité distincte du scénario collectif et de sa mise en application.

[Exploring Backorder Processing](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe) — S/4HANA Cloud Public Edition ; cours évolutif, consulté le 2026-09-18.

**Passage.** Backorder Processing Overview ; Confirmation Strategies

**Limite de preuve.** Texte primaire consulté ; aucune taxonomie universelle ni preuve de déploiement Beaumanoir.

Références : U402, ELM241, CMP152.

## Comparaison par rapport au marché — D04.i Sales Order

### Microsoft — Customer orders in point of sale (POS)

Dynamics 365 Commerce · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Commandes livrées à une adresse et commandes retirées au lieu/date convenus ; choix entre magasins et entrepôts admissibles.

**Différences.** Source Commerce/POS, pas preuve de couverture universelle de toutes les ventes B2B ; ne transfère pas l’exécution physique à Sales Order.

**Position FLOW.** Shipping/Pickup et Direct delivery sont documentés par Microsoft ; Intercompany constitue une dimension de relation commerciale combinable avec un parcours de livraison. Il ne s’agit pas de quatre catégories mutuellement exclusives.

[Customer orders in point of sale (POS)](https://learn.microsoft.com/en-us/dynamics365/commerce/customer-orders-overview) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Typical scenarios ; shipment or pickup

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Microsoft — Direct deliveries

Dynamics 365 SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Fournisseur livre directement le client ; commande de vente reliée à l’achat.

**Différences.** Choix documentaire produit distinct des responsabilités FLOW ; ne prouve pas une disponibilité ni une promesse automatique.

**Position FLOW.** Shipping/Pickup et Direct delivery sont documentés par Microsoft ; Intercompany constitue une dimension de relation commerciale combinable avec un parcours de livraison. Il ne s’agit pas de quatre catégories mutuellement exclusives.

[Direct deliveries](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/direct-deliveries) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction ; Delivery date ; order lines

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Microsoft — Intercompany orders and return orders

Dynamics 365 SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Commandes de vente et achat liées entre entités juridiques.

**Différences.** Transaction commerciale intersociétés distincte d’un simple transfert entre lieux ; pas de schéma comptable prescrit pour FLOW.

**Position FLOW.** Shipping/Pickup et Direct delivery sont documentés par Microsoft ; Intercompany constitue une dimension de relation commerciale combinable avec un parcours de livraison. Il ne s’agit pas de quatre catégories mutuellement exclusives.

[Intercompany orders and return orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/intercompany-orders-and-return-orders) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction ; intercompany sales and purchase orders

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — D04.j Purchase Order

### Microsoft — Create purchase orders

Dynamics 365 SCM · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Les commandes peuvent porter des produits physiques ou des services ; destination, quantités et dates sont précisées.

**Différences.** Types de lignes produit, pas une taxonomie de comportements.

**Position FLOW.** Trois parcours FLOW adoptés U391 ; nature produit et maille de capacité restent distinctes. Frontières achat/exécution/stocks préservées.

[Create purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-creation) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Adding purchase order lines

**Limite de preuve.** Page primaire ouverte ; aucune preuve de réalisation Beaumanoir.

Références : U390, U391, ELM235, CMP146.

### Microsoft — Direct deliveries

Dynamics 365 SCM · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Livraison fournisseur au client et liens entre lignes achat/vente ; coordination des dates et destinations sans passage physique dans l’entrepôt du vendeur.

**Différences.** FLOW ne reprend pas automatiquement les règles de propagation des dates ni les écritures du produit.

**Position FLOW.** Trois parcours FLOW adoptés U391 ; nature produit et maille de capacité restent distinctes. Frontières achat/exécution/stocks préservées.

[Direct deliveries](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/direct-deliveries) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction, Delivery date, Delivery address, Warehouse

**Limite de preuve.** Page primaire ouverte ; aucune preuve de réalisation Beaumanoir.

Références : U390, U391, ELM235, CMP146.

### SAP — Manage Service Entry Sheets - Lean Services / Planned and Unplanned Services

S/4HANA on-premise · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Les prestations exécutées sont constatées par référence à une commande d’achat ; services planifiés et non planifiés.

**Différences.** Application et documents SAP, pas une nouvelle capacité d’exécution FLOW ; aucune feuille de saisie imposée.

**Position FLOW.** Trois parcours FLOW adoptés U391 ; nature produit et maille de capacité restent distinctes. Frontières achat/exécution/stocks préservées.

[Manage Service Entry Sheets - Lean Services / Planned and Unplanned Services](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/4ac8acf820ad41a8a5841420085ba68d.html) — 2025 FPS01 (Feb 2026) affichée sur la page associée Planned and Unplanned Services, consulté le 2026-09-18.

**Passage.** Introduction et Create or change a service entry sheet with reference to a purchase order

**Limite de preuve.** Passages primaires indexés lus ; ouverture directe du portail sans texte exploitable ; aucune preuve de réalisation Beaumanoir.

Références : U390, U391, ELM235, CMP146.

### Microsoft — Vendor collaboration with external vendors

Dynamics 365 Supply Chain Management · Processus, fonction ou objet produit · Recouvrement partiel · statut : proposed

**Points communs.** Le processus distingue envoi de la commande, réponse fournisseur (acceptation, refus, changements) et confirmation, avec versions et historique. Les changements peuvent porter sur quantités, dates et échéanciers.

**Différences.** Vendor collaboration couvre plus que ce comportement (notamment RFQ et factures). FLOW conserve le mécanisme d’engagement sur Purchase Order, sans copier l’interface, les étapes manuelles ou tous les statuts produit.

**Position FLOW.** Supplier Confirmation est un mécanisme combinable de Purchase Order ; engagement reçu distinct de la promesse client et de la réalisation. Confirmation et révision restent dans un seul comportement.

[Vendor collaboration with external vendors](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/vendor-collaboration-work-external-vendors) — Documentation évolutive ; mise à jour affichée 2025-07-21, consulté le 2026-09-19.

**Passage.** Working with POs when vendor collaboration is used ; Changing a PO ; Updating a PO when a vendor suggests changes

**Limite de preuve.** Texte primaire ouvert et consulté ; aucune preuve de réalisation installée chez Beaumanoir.

Références : U403, ELM242, CMP153.

### Microsoft — Review and accept changes to confirmed purchase orders

Dynamics 365 Supply Chain Management · Processus, fonction ou objet produit · Recouvrement partiel · statut : proposed

**Points communs.** L’examen de modifications d’achats confirmés s’appuie sur leurs conséquences sur les demandes aval avant reconfirmation et permet des échanges avec le fournisseur.

**Différences.** Cette fonction documente les impacts directs, pas tous les impacts indirects. FLOW répartit engagement fournisseur, analyse des possibilités, décision collective et promesse client entre capacités distinctes. Aucune capacité Copilot ou écran créée.

**Position FLOW.** Supplier Confirmation est un mécanisme combinable de Purchase Order ; engagement reçu distinct de la promesse client et de la réalisation. Confirmation et révision restent dans un seul comportement.

[Review and accept changes to confirmed purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-changes-after-confirmation) — Documentation évolutive ; mise à jour affichée 2026-07-01, consulté le 2026-09-19.

**Passage.** Review changes to confirmed purchase orders ; Step 3, note on direct downstream impacts

**Limite de preuve.** Texte primaire ouvert et consulté ; aucune preuve de réalisation installée chez Beaumanoir.

Références : U403, ELM242, CMP153.

### SAP — Create Supplier Confirmation (Optional)

SAP S/4HANA Cloud Best Practices / Direct Procurement with Inbound Delivery (2TX) · Processus, fonction ou objet produit · Recouvrement partiel · statut : proposed

**Points communs.** Le passage expose une Supplier Confirmation rattachée au Purchase Order, avec date de livraison et quantité confirmées.

**Différences.** Appui au nom et aux données d’engagement ; le passage ne démontre pas à lui seul la totalité du mécanisme FLOW, ses révisions et impacts. Supplier Confirmation y est un objet/processus produit, pas une taxonomie de comportements d’entreprise.

**Position FLOW.** Supplier Confirmation est un mécanisme combinable de Purchase Order ; engagement reçu distinct de la promesse client et de la réalisation. Confirmation et révision restent dans un seul comportement.

[Create Supplier Confirmation (Optional)](https://help.sap.com/docs/s4hana-cloud-best-practices/direct-procurement-with-inbound-delivery-2tx-hr/create-supplier-confirmation-optional) — Édition non affichée dans le passage indexé consulté, consulté le 2026-09-19.

**Passage.** Enter Reference Purchase Order ; Create Supplier Confirmation Item ; Create Confirmation Line Data

**Limite de preuve.** Passage primaire indexé consulté ; ouverture directe du portail sans texte exploitable ; aucune preuve de réalisation installée chez Beaumanoir.

Références : U403, ELM242, CMP153.

## Comparaison par rapport au marché — D04.k Transfer Order

### SAP — Allocation Table with Reference to an OAPC-Based Purchase Order

ERP Retail · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Répartition d’achat initial et documents subséquents dont stock transport orders.

**Différences.** Appui partiel et historique pour implantation ; pas une décomposition native des capacités FLOW. Allocation reste un terme éditeur qualifié.

**Position FLOW.** Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Allocation Table with Reference to an OAPC-Based Purchase Order](https://help.sap.com/docs/SAP_ERP/75c4b203fca64320b998cc04e2eb1468/24e4c353b677b44ce10000000a174cb4.html?version=6.17.latest) — 6.17, documentation historique, consulté le 2026-09-18.

**Passage.** Fixed Initial Buy Allocation ; follow-on documents

**Limite de preuve.** Passage primaire indexé consulté ; ouverture du portail sans texte exploitable ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Microsoft — Set up warehouses for transfer orders

Dynamics 365 SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Besoins de destination alimentés par des transferts planifiés depuis un entrepôt source.

**Différences.** Décrit le réassort ; pas une taxonomie exhaustive de cinq comportements.

**Position FLOW.** Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Set up warehouses for transfer orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/transfer-orders-warehouse) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Warehouse levels ; Refilling ; Transport lead time

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Microsoft — Integrate Supply Chain Management transfer orders with Intelligent Order Management

Dynamics 365 Intelligent Order Management / SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Transferts pour réassort, pointe de demande, prestations et satisfaction de commandes ; visibilité des transferts entrants associés au produit de commande.

**Différences.** La page porte un avertissement preview ; appui sur le sens métier, pas recommandation de produit ni assertion de disponibilité générale.

**Position FLOW.** Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Integrate Supply Chain Management transfer orders with Intelligent Order Management](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/integrate-transfer-orders) — Documentation évolutive avec avertissement preview, consulté le 2026-09-18.

**Passage.** Typical reasons ; View transfer order products on sales order product page

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Oracle — Overview of Inventory Rebalancing

Fusion Cloud Replenishment Planning · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Rééquilibrage excédents/manques et ordres planifiés ; transfert possible vers un lieu de regroupement.

**Différences.** Le produit combine décision et génération des ordres ; FLOW garde ces responsabilités séparées.

**Position FLOW.** Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Overview of Inventory Rebalancing](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html) — 26B, consulté le 2026-09-18.

**Passage.** Salient Features ; planned inbound and outbound orders

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Nextail — Merkal implements AI to centralize and streamline inventory planning across all channels

Inventory Planning · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Transferts de fin de saison, rééquilibrage du réseau et consolidation des tailles.

**Différences.** Témoignage éditeur/client, pas spécification normative ni preuve de déploiement Beaumanoir.

**Position FLOW.** Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Merkal implements AI to centralize and streamline inventory planning across all channels](https://nextail.co/customer/merkal-footwear-inventory-planning/) — Étude client, version non affichée, consulté le 2026-09-18.

**Passage.** Sharper store transfers ; customer quote on consolidation

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — D04.l Customer Return

### SAP — Logistical Follow-Up Activities

S/4HANA Cloud — Warehouse Management · Suites de processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Remise en stock disponible, réparation, expédition fournisseur, restitution client et rebut documentés.

**Différences.** Documents, mouvements et étapes de processus ne sont pas automatiquement des capacités ou comportements FLOW ; absence d’équivalence de niveau.

**Position FLOW.** Appui au choix de parcours métier ; préserver D05.i pour choisir, D04 pour les Orders, D06 pour les prestations et D01 pour les stocks. U385 adopte les parcours sous Customer Return ; correspondance marché proposée distincte de cet accord.

[Logistical Follow-Up Activities](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/aeb252c114df4dac9abf1626ccb04233.html) — 2602 affiché par le passage primaire indexé, consulté le 2026-09-18.

**Passage.** Table : 0011, 0012, 0005, 0021 et 0026

**Limite de preuve.** Texte primaire indexé consulté ; portail direct partiellement inaccessible. Aucune réalisation Beaumanoir déduite.

Références : U384, ELM232, CMP143, U385.

### Microsoft — Disposition codes and disposition actions

Dynamics 365 Supply Chain Management · Configuration et actions de traitement produit · Recouvrement partiel · statut : proposed

**Points communs.** Codes réparation, reconditionnement, renvoi fournisseur ; actions de remise en stock, rebut et restitution au client.

**Différences.** Les six actions prédéfinies combinent effets logistiques et financiers ; un code libre ne prouve pas un processus natif complet de réparation.

**Position FLOW.** Conserver les parcours logistiques et expliciter les interfaces commerciales sans absorber remboursement et comptabilité. U385 adopte les parcours sous Customer Return ; correspondance marché proposée distincte de cet accord.

[Specify how to dispose of returned items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items) — Mise à jour affichée 2025-05-07, consulté le 2026-09-18.

**Passage.** Disposition types/codes ; six disposition actions

**Limite de preuve.** Page primaire ouverte ; fonctionnalités produit, sans preuve de couverture Beaumanoir.

Références : U384, ELM232, CMP143, U385.

## Comparaison par rapport au marché — D04.m Supplier Return

### Microsoft — Purchase return order / replacement purchase order

Dynamics 365 Business Central · Processus et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Le retour peut être associé à un avoir ; un remplacement peut générer une commande d’achat distincte.

**Différences.** Fonctions produit mêlant logistique et comptabilité ; ne pas attribuer cette documentation Business Central à Dynamics 365 SCM. La nouvelle commande est un choix produit, pas une obligation FLOW.

**Position FLOW.** U387 adopte deux parcours distingués par l’attendu de marchandises. Les choix documentaires éditeurs et les opérations financières restent distincts ; correspondance proposée.

[Purchase return order / replacement purchase order](https://learn.microsoft.com/en-us/dynamics365/business-central/purchasing-how-process-purchase-returns-cancellations) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Create a replacement purchase order from a purchase return order ; introduction

**Limite de preuve.** Page primaire ouverte. Aucune réalisation Beaumanoir déduite.

Références : U386, ELM233, CMP144, U387.

### SAP — Create a New Return to Supplier

Business ByDesign · Processus et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Suites : avoir, remplacement ou combinaison partielle. Le remplacement modifie le reste à livrer de l’achat ; la seule émission d’un avoir ne crée pas ce même attendu.

**Différences.** Documentation ByDesign, pas S/4HANA. Restrictions particulières au scénario tiers ; séparation de vues acheteur/logistique non imposée à l’organisation FLOW.

**Position FLOW.** U387 adopte deux parcours distingués par l’attendu de marchandises. Les choix documentaires éditeurs et les opérations financières restent distincts ; correspondance proposée.

[Create a New Return to Supplier](https://help.sap.com/docs/SAP_BUSINESS_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2d9b97f7722d1014a974a1fa1d11fd10.html) — May 2026 affiché dans le passage primaire indexé, consulté le 2026-09-18.

**Passage.** Overview ; Create a Return to Supplier in Purchasing

**Limite de preuve.** Texte primaire indexé effectivement consulté ; ouverture directe sans contenu exploitable. Aucune réalisation Beaumanoir déduite.

Références : U386, ELM233, CMP144, U387.

### Oracle — Return to Supplier for Credit Only

Fusion Cloud SCM — Receiving · Processus et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Retour pour avoir sans remplacement attendu : conserver la commande d’achat fermée aux réceptions futures, plutôt que la rouvrir.

**Différences.** Effet produit sur une commande existante ; FLOW retient la différence d’attendu Supply sans imposer cette mécanique de statut ou absorber la comptabilité.

**Position FLOW.** U387 adopte deux parcours distingués par l’attendu de marchandises. Les choix documentaires éditeurs et les opérations financières restent distincts ; correspondance proposée.

[Return to Supplier for Credit Only](https://docs.oracle.com/en/cloud/saas/readiness/scm/25a/inv25a/25A-inventory-wn-f35542.htm) — 25A, consulté le 2026-09-18.

**Passage.** Présentation de la fonctionnalité Return for credit

**Limite de preuve.** Page primaire ouverte. Aucune réalisation Beaumanoir déduite.

Références : U386, ELM233, CMP144, U387.

### Oracle — Repair at sourcing / Repair-Return

E-Business Suite — Service Parts Planning · Processus et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** La réparation externe peut mobiliser un achat au réparateur et des documents de mouvement du bien.

**Différences.** Planification de pièces de service et réparation, pas preuve d’un comportement de retour fournisseur dans Oracle Fusion ou dans le retail FLOW.

**Position FLOW.** U388 place le suivi du renvoi et de la restitution sous Supplier Return. Achat de prestation et orchestration restent distincts ; rattachement FLOW, pas équivalence au catalogue Oracle.

[Repair at sourcing / Repair-Return](https://docs.oracle.com/cd/E18727-01/doc.121/e13338/T515331T515340.htm) — Release 12.1, référence historique, consulté le 2026-09-18.

**Passage.** Repair Program Influence on Service Supply Chain Lead Time Offset ; Assigning Sourcing Rule – Repair at

**Limite de preuve.** Page primaire ouverte le 18 septembre 2026 ; référence historique EBS 12.1, pas preuve de couverture Fusion ou Beaumanoir. Le passage ne démontre pas une traçabilité sérialisée identique à notre exigence.

Références : U386, U388, ELM233, CMP144.

## Comparaison par rapport au marché — D04.n Order Structuring

### Microsoft — Delivery schedules

Dynamics 365 SCM · Structure métier ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Une ligne commerciale demeure comme en-tête de lignes de livraison ; sa quantité agrège celles des livraisons.

**Différences.** Hiérarchie de lignes dans une commande, pas preuve d’un nouvel Order chapeau ni d’une capacité autonome.

**Position FLOW.** U417 : Structuring couvre découpage et composition dans D03 ; Split en est un comportement.

[Delivery schedules](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-schedules) — 2025-05-07, consulté le 2026-09-18.

**Passage.** Commercial line et delivery lines

**Limite de preuve.** Passages primaires indexés consultés ; niveaux et contextes éditeurs conservés.

Références : U355, ELM220, CMP129, U363, CMP133.

### Oracle — Split Order Lines

Fusion Cloud Order Management · Structure métier ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Une ligne de 50 peut être scindée en 30 et 20 selon l’entrepôt ; le produit conserve la quantité globale et adapte les processus associés.

**Différences.** Division de lignes/fulfillment et réalisation logicielle ; ni deux Orders commerciaux autonomes ni placement sous une capacité FLOW démontrés.

**Position FLOW.** U417 : Structuring couvre découpage et composition dans D03 ; Split en est un comportement.

[Split Order Lines](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/fauom/split-fulfillment-lines.html) — 25D, consulté le 2026-09-18.

**Passage.** Exemple Seattle/Denver et effets du split

**Limite de preuve.** Passages primaires indexés consultés ; niveaux et contextes éditeurs conservés.

Références : U355, ELM220, CMP129, U363, CMP133.

### SAP — Order Hierarchy

ERP Orders CS-SE/PM-WOC-MO · Structure métier ou fonction produit · Appui méthodologique · statut : proposed

**Points communs.** Hiérarchie d’ordres et sous-ordres avec responsabilité du leading order sur l’exécution des ordres inférieurs.

**Différences.** Contexte maintenance/service, pas commandes Supply de vente/achat/transfert ; analogie de responsabilité seulement, aucun objet FLOW prescrit.

**Position FLOW.** U417 : Structuring couvre découpage et composition dans D03 ; Split en est un comportement.

[Order Hierarchy](https://help.sap.com/docs/SAP_ERP/b4174aff4a234ed5be928a10c60997fb/45c8b65334e6b54ce10000000a174cb4.html) — 6.0 EHP8 Latest, consulté le 2026-09-18.

**Passage.** Definition ; Structure

**Limite de preuve.** Passages primaires indexés consultés ; niveaux et contextes éditeurs conservés.

Références : U355, ELM220, CMP129, U363, CMP133.

### Oracle — What’s a Split Order Line

Fusion Cloud SCM 26B · Mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Découper une ligne pour satisfaire la demande entre entrepôts ou dates ; les parties peuvent progresser différemment.

**Différences.** La structure documentaire Oracle et ses restrictions ne prescrivent pas une hiérarchie ou un découpage logiciel FLOW.

**Position FLOW.** U420 : Structuring dans D03, Lifecycle dans D04 ; Split sous Structuring, Release sous Lifecycle. Frontière FLOW, pas taxonomie éditeur adoptée.

[What’s a Split Order Line](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/fulfillment-line-splits.html) — 26B, consulté le 2026-09-19.

**Passage.** How Order Management Determines Availability ; How Split Order Lines Affect Status

**Limite de preuve.** Sources primaires ouvertes lors de la proposition ; aucune preuve installée Beaumanoir.

Références : U416, U417, U418, ELM248, CMP159.

## Comparaison par rapport au marché — D04.o Order Lifecycle Management

### SAP — Handling Requirements with Fixed Date and Quantity

S/4HANA aATP · Mécanisme ou transition métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Par défaut BOP conserve les confirmations marquées Fixed Date and Quantity et leur attribue Skip.

**Différences.** Un segment peut explicitement les inclure dans le contrôle ; ne prouve pas une immutabilité absolue ni le comportement de toute API ARun.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Handling Requirements with Fixed Date and Quantity](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/413e5cf1373142a784f6c04b2caf3fc0.html) — 2025 FPS01 (Feb 2026), consulté le 2026-09-18.

**Passage.** Page entière

**Limite de preuve.** Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.

Références : U346, U347, ELM216, CMP124, U349, CMP125, U350, U420, U424.

### Microsoft — Firm planned orders

Dynamics 365 SCM · Mécanisme ou transition métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Affermir transforme des ordres planifiés en commandes effectives achat, transfert ou production.

**Différences.** Transition de cycle de vie, pas synonyme de fixation de toutes les données d’une commande client.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Firm planned orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction

**Limite de preuve.** Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.

Références : U346, U347, ELM216, CMP124, U349, CMP125, U350, U420, U424.

### Microsoft — Keep supply for confirmed demand

Dynamics 365 SCM · Mécanisme ou transition métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Préserve une chaîne liée à une demande confirmée, notamment ordres planifiés et liens de pegging, entre les passages de planification.

**Différences.** Comportement paramétré ; la conservation du stock reçu hors positive days exige un paramètre complémentaire. Ne prouve aucun déploiement Beaumanoir.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Keep supply for confirmed demand](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand) — Prérequis documenté : 10.0.48 build 10.0.2645.33 ou ultérieur, consulté le 2026-09-18.

**Passage.** What data is preserved ; Control how on-hand inventory is pegged ; Interaction with approved planned orders

**Limite de preuve.** Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.

Références : U346, U347, ELM216, CMP124, U349, CMP125, U350, U420, U424.

### Microsoft — Master plans — Freeze

Dynamics 365 SCM · Mécanisme ou transition métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Le gel temporel conserve les ordres planifiés dans une fenêtre.

**Différences.** Le gel empêche aussi la création de nouveaux ordres planifiés dans cette fenêtre ; différent de protéger une commande individuelle.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Master plans — Freeze](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Freeze ; Firming

**Limite de preuve.** Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.

Références : U346, U347, ELM216, CMP124, U349, CMP125, U350, U420, U424.

### Oracle — Order Management Statuses

Fusion Cloud Order Management · Fonction ou état produit · Recouvrement partiel · statut : proposed

**Points communs.** Une commande enregistrée mais non soumise au fulfillment reste Draft et peut être modifiée.

**Différences.** Référence 25C ; distinction brouillon/soumission, pas équivalence automatique avec ordre planifié/affermissement Microsoft.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Order Management Statuses](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/fauom/order-management-statuses.html) — 25C, consulté le 2026-09-18.

**Passage.** Draft

**Limite de preuve.** Passages primaires indexés consultés ; aucune réalisation client démontrée.

Références : U353, U354, ELM219, CMP128, U363, CMP133, U420, U424.

### Microsoft — Release to warehouse

Dynamics 365 SCM · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** La libération de ventes et transferts vers l’entrepôt prépare les objets logistiques nécessaires au traitement.

**Différences.** Mise en œuvre WMS spécifique ; FLOW distingue autorisation métier et orchestration/réalisation des prestations.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Release to warehouse](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/release-to-warehouse-process) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Release to warehouse process

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U420, U424.

### Microsoft — Manage order holds

Dynamics 365 SCM · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Mise en attente avec motifs, conditions de levée et effet configurable sur les réservations ; progression logistique bloquée.

**Différences.** Le checkout du hold est un verrou logiciel distinct. Les effets de réservation sont paramétrés, pas une conséquence universelle du Hold.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Manage order holds](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/tasks/manage-order-holds) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction ; Set up order hold codes ; Manage orders on hold

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U420, U424.

### Oracle — Hold Your Sales Orders

Fusion Cloud Order Management · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Un hold peut viser une étape de traitement : les autres étapes peuvent avancer jusqu’au point bloqué.

**Différences.** Le modèle FLOW décrit portée et effets métier ; il ne copie pas les tâches d’orchestration Oracle.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Hold Your Sales Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/sales-order-hold.html) — 26B, consulté le 2026-09-18.

**Passage.** Introduction ; How Holds Work

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U420, U424.

### Microsoft — Action messages

Dynamics 365 SCM · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Suggestions Advance/Postpone de changement d’échéances sur des ordres existants.

**Différences.** Suggestion et application distinctes. Ne prouve pas une capacité autonome de calcul d’échéancier sous Lifecycle.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Action messages](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction ; Select action messages

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U420, U424.

### Microsoft — Approve and confirm purchase orders

Dynamics 365 SCM · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Annulation encadrée des quantités restantes et Finalize pour empêcher de nouveaux traitements.

**Différences.** Achat, pas cycle universel. Clôture opérationnelle FLOW ne reprend pas toute la finalisation financière du produit.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Approve and confirm purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Canceling purchase orders ; modification après confirmation

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U420, U424.

### Oracle — Cancel Sales Orders

Fusion Cloud Order Management · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Annulation des quantités non expédiées selon états et conditions ; les quantités déjà réalisées ne sont pas effacées.

**Différences.** Cycle de commande de vente propre au produit ; compensation du processus reste dans la couche processus, pas nouveau comportement de Lifecycle.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Cancel Sales Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/cancel-sales-orders.html) — 26B, consulté le 2026-09-18.

**Passage.** Cancel Remaining Quantity

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U420, U424.

### Microsoft — Approve and confirm purchase orders

Dynamics 365 SCM · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Annulation encadrée des quantités restantes et Finalize pour empêcher de nouveaux traitements.

**Différences.** Achat, pas cycle universel. Clôture opérationnelle FLOW ne reprend pas toute la finalisation financière du produit.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Approve and confirm purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Canceling purchase orders ; modification après confirmation

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U420, U424.

### SAP — Functional Details: Manage Sales Orders - Version 2

S/4HANA Cloud · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Blocages par objet et rejet des lignes ; le rejet de toutes les lignes peut terminer le document sous conditions.

**Différences.** Restrictions si déjà livré ou achat lié. Rejection produit n’est pas équivalent à toute annulation ou clôture FLOW ; facturation hors périmètre métier étudié.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Functional Details: Manage Sales Orders - Version 2](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/e7f14402cf5846b4b3d0d677c15414b1.html?locale=en-US) — Édition non relevée dans le passage indexé, consulté le 2026-09-18.

**Passage.** Delivery Block and Billing Block ; Rejection of all Items

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U420, U424.

### Oracle — What’s a Split Order Line

Fusion Cloud Order Management · Fonction produit, verbe descriptif ou stratégie de répartition · Appui sémantique · statut : proposed

**Points communs.** Split couvre plusieurs entrepôts, dates ou articles substituts, et peut créer plusieurs lignes et tâches de fulfillment.

**Différences.** Ne signifie pas toujours création de plusieurs commandes autonomes ; la fonction produit combine décisions et effets que FLOW sépare.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[What’s a Split Order Line](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/fulfillment-line-splits.html) — 26B, consulté le 2026-09-18.

**Passage.** How Order Management Determines Availability

**Limite de preuve.** Oracle ouvert ; passages Microsoft et SAP indexés consultés, page SAP dynamique sans texte à l’ouverture. Aucune implémentation Beaumanoir déduite.

Références : U360, ELM222, CMP131, U363, CMP133, U420, U424.

### Microsoft — View, manage, and approve planned orders

Dynamics 365 Supply Chain Management · Mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Les statuts suivent la préparation des ordres planifiés ; l’approbation préserve certains ajustements face aux recalculs sous conditions.

**Différences.** Périmètre approvisionnements planifiés. Pas de taxonomie universelle ni de preuve que gel, suspension et affermissement forment un seul cycle.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[View, manage, and approve planned orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/approved-planned-order) — Page mise à jour le 2 septembre 2026, consulté le 2026-09-19.

**Passage.** View and edit the status of planned orders ; Approve planned orders

**Limite de preuve.** Sources primaires ouvertes lors de la proposition ; aucune preuve installée Beaumanoir.

Références : U416, U417, U418, ELM248, CMP159, U420, U424.

### Microsoft — Purchase order overview

Dynamics 365 Supply Chain Management · Statuts et processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Plusieurs statuts coexistent sur une commande : approbation, quantités et documents.

**Différences.** Cette page ne propose pas nos six comportements ni une liste universelle de statuts.

**Position FLOW.** U424 : dimension métier et états FLOW explicités ; correspondance proposée et portée distincte de l’accord sur le modèle.

[Purchase order overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-overview) — Documentation évolutive consultée le 19 septembre 2026, consulté le 2026-09-19.

**Passage.** Purchase order statuses

**Limite de preuve.** Source primaire ouverte ; aucune preuve de déploiement Beaumanoir. Les libellés FLOW détaillés restent éditoriaux.

Références : U424, ELM251, CMP162.

## Comparaison par rapport au marché — D05.a Inventory Target Decision

### SAP — Calculate Target Inventory Components

SAP IBP · Opérateur de planification · Recouvrement partiel · statut : proposed

**Points communs.** Détermine les cibles de stock et leurs composantes, ainsi que le point de commande ; résultats concrets correspondant à une partie importante de la responsabilité D05.a.

**Différences.** Opérateur produit qui dépend de Global (Multi-Stage) Inventory Optimization ; produit aussi des indicateurs et conversions. Ni unité logicielle ni séquence SAP ne dictent la capacité FLOW. Les contraintes et politiques détaillées ne sont pas déclarées équivalentes.

**Position FLOW.** Appui fonctionnel à D05.a Inventory Target Decision : déterminer objectifs et seuils de stock. Nom et définition FLOW adoptés U329. Préserver la maille décision sans importer le découpage logiciel, ni recréer Calculation ; correspondance partielle proposée, sans équivalence complète validée.

[Calculate Target Inventory Components](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/c1fb60cb1e9c49d99ada277ae57e9e6c/ab7b2b5a7bc24b86b949ee10d3275053.html?MDT_Attr_Appl_Models-BMforMDT=PDS+Activity&locale=en-US&version=LATEST) — 2608, consulté le 2026-09-18.

**Passage.** Description et fonctionnalités de l’opérateur

**Limite de preuve.** Source primaire consultée (SAP : texte indexé détaillé ; Microsoft et Oracle : page ouverte). Aucun déploiement Beaumanoir ni usage obligatoire d’IA démontré.

Références : U328, ELM204, CMP112, U329.

### Microsoft — Safety stock journals — Calculate a proposal

Dynamics 365 Supply Chain Management · Fonctionnalité et processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Détermine un minimum proposé selon les consommations historiques, délais et service ; montre son impact sur la valeur du stock. Le résultat proposé est distinct de sa mise à jour effective.

**Différences.** Appui partiel : ne documente pas à lui seul tous les objectifs et seuils de FLOW. Le même journal regroupe proposition, révision et application ; FLOW distingue les responsabilités métier sans imposer plusieurs logiciels. Le rôle du minimum dépend de la méthode de réapprovisionnement.

**Position FLOW.** Appui fonctionnel à D05.a Inventory Target Decision : déterminer objectifs et seuils de stock. Nom et définition FLOW adoptés U329. Préserver la maille décision sans importer le découpage logiciel, ni recréer Calculation ; correspondance partielle proposée, sans équivalence complète validée.

[Use the safety stock journal to update minimum coverage for items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-journal) — Mise à jour affichée 2025-08-22, consulté le 2026-09-18.

**Passage.** Calculate minimum coverage based on historical usage ; Calculate a proposal ; Post the new minimum quantity

**Limite de preuve.** Source primaire consultée (SAP : texte indexé détaillé ; Microsoft et Oracle : page ouverte). Aucun déploiement Beaumanoir ni usage obligatoire d’IA démontré.

Références : U328, ELM204, CMP112, U329.

### Oracle — Policy parameters — calculation of policy values

Fusion Cloud SCM Replenishment Planning · Règles de détermination des paramètres de stock · Recouvrement partiel · statut : proposed

**Points communs.** Calcule des valeurs de politique par article et lieu ; documente distinctement les méthodes de calcul des quantités et leur utilisation pour le réapprovisionnement.

**Différences.** Ensemble fonctionnel plus large comprenant configuration, valeurs par défaut et surcharges ; ne constitue pas une capacité nommée Inventory Target Decision. Les politiques et formules Oracle restent des références, pas des règles FLOW adoptées.

**Position FLOW.** Appui fonctionnel à D05.a Inventory Target Decision : déterminer objectifs et seuils de stock. Nom et définition FLOW adoptés U329. Préserver la maille décision sans importer le découpage logiciel, ni recréer Calculation ; correspondance partielle proposée, sans équivalence complète validée.

[Policy Assignment Sets](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/policy-assignment-sets.html) — 26B, consulté le 2026-09-18.

**Passage.** Policy Parameters — Method for Calculation of Quantities / How the Policy Type Is Used

**Limite de preuve.** Source primaire consultée (SAP : texte indexé détaillé ; Microsoft et Oracle : page ouverte). Aucun déploiement Beaumanoir ni usage obligatoire d’IA démontré.

Références : U328, ELM204, CMP112, U329.

### SAP — Minimum and Maximum Safety Stock

SAP IBP · Mécanisme d’optimisation documenté · Recouvrement partiel · statut : proposed

**Points communs.** Les opérateurs multi-stage peuvent ajuster les stocks de sécurité amont et aval pour respecter le service et les contraintes de sécurité.

**Différences.** Le mécanisme documenté porte sur les stocks de sécurité ; ne prouve pas toutes les cibles, un optimum garanti ou une réalisation Beaumanoir.

**Position FLOW.** U331/U332 adoptent le comportement Multi-Echelon Inventory Optimization sous D05.a, aux côtés des variantes magasin et centre de distribution. Le résultat est un ensemble coordonné de cibles ; l’affectation et les décisions d’apport restent distinctes. Comparaison marché proposée ; P13 intégré comme BHV028.

[Minimum and Maximum Safety Stock](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/c94e89301b884790b30fbd82a687bcc1.html) — Documentation évolutive, édition non identifiée sur cet extrait, consulté le 2026-09-18.

**Passage.** How to Use — Target Service Level

**Limite de preuve.** Texte primaire indexé consulté le 18 septembre 2026. Le mécanisme documenté porte sur les stocks de sécurité ; ne prouve pas toutes les cibles, un optimum garanti ou une réalisation Beaumanoir.

Références : U330, ELM205, CMP113, U332.

### RELEX — Multi-echelon inventory optimization

Inventory optimization · Mécanisme d’optimisation documenté · Recouvrement partiel · statut : proposed

**Points communs.** Positionne les stocks de sécurité en considérant les dépendances du réseau, délais, variabilité et service ; oppose cette approche aux dimensionnements isolés.

**Différences.** Présentation éditeur et scénario illustratif ; bénéfices annoncés non mesurés pour FLOW, algorithme non audité.

**Position FLOW.** U331/U332 adoptent le comportement Multi-Echelon Inventory Optimization sous D05.a, aux côtés des variantes magasin et centre de distribution. Le résultat est un ensemble coordonné de cibles ; l’affectation et les décisions d’apport restent distinctes. Comparaison marché proposée ; P13 intégré comme BHV028.

[Multi-echelon inventory optimization](https://www.relexsolutions.com/resources/inventory-optimization/) — Article évolutif, sans version produit figée, consulté le 2026-09-18.

**Passage.** Multi-echelon inventory optimization

**Limite de preuve.** Texte primaire indexé consulté le 18 septembre 2026. Présentation éditeur et scénario illustratif ; bénéfices annoncés non mesurés pour FLOW, algorithme non audité.

Références : U330, ELM205, CMP113, U332.

## Comparaison par rapport au marché — D05.g Initial Stocking Decision

### SAP — Initial Allocation

Allocation Management · Scénarios métier d’un produit · Recouvrement partiel · statut : proposed

**Points communs.** Première distribution de produits vers les magasins pour préparer leur lancement commercial ; rapprochement avec l’implantation initiale décrite par Laurent.

**Différences.** SAP décrit un produit qui couvre planification et traitement de la distribution. FLOW sépare décision des apports, gestion des Orders et exécution. Le réassort décrit par Laurent est guidé par des seuils ; cette documentation SAP ne démontre pas une formule identique. La notion SAP de collection ou thème ne prouve pas un usage de capsules chez Beaumanoir.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[SAP Allocation Management — Business Overview](https://help.sap.com/docs/CARAB/00197153997746b4bec2020d00e66ea9/e99798c39a3f4956bd5ce509b39382f7.html?locale=en-US&state=PRODUCTION&version=5.0.2) — 5.0 FPS02 — version de la documentation consultée, consulté le 2026-09-18.

**Passage.** Business Scenarios : Initial Allocation ; In-Season Fill-In

**Limite de preuve.** Texte primaire indexé consulté ; ouverture de la page sans corps exploitable. Pas de preuve de déploiement Beaumanoir, ni d’équivalence de hiérarchie Capacité → Comportement.

Références : ELM198, CMP106, U310, U311, U313, U314, CMP107, U315, CMP108, U316.

### RELEX — Initial allocation

Replenishment and allocation · Fonctions présentées par l’éditeur · Recouvrement partiel · statut : proposed

**Points communs.** Première distribution de produits vers les magasins pour préparer leur lancement commercial ; rapprochement avec l’implantation initiale décrite par Laurent.

**Différences.** La présentation RELEX associe aussi commandes présaison et gestion de fin de saison. Ces fonctions ne sont pas ajoutées implicitement à FLOW. Le réassort produit utilise notamment des prévisions ; une identité avec les seuils et règles Beaumanoir n’est pas établie.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[RELEX — Replenishment and allocation](https://www.relexsolutions.com/solutions/automatic-replenishment-system/) — Présentation produit évolutive, sans édition figée, consulté le 2026-09-18.

**Passage.** Manage the full cycle for your seasonal items ; Manage seasons effectively

**Limite de preuve.** Présentation commerciale primaire consultée. Aucun contrat fonctionnel exhaustif, aucune formule de seuil équivalente ni déploiement Beaumanoir démontré.

Références : ELM198, CMP106, U310, U311, U313, U314, CMP107, U315, CMP108, U316.

### OASIS — Initial Stocking of the Area by Retailer

Universal Business Language (UBL) · Processus métier documenté dans un standard d’échanges · Appui sémantique · statut : proposed

**Points communs.** Constitution d’un stock de départ au début d’une relation commerciale ou d’une saison ; le processus Initial Stocking est distingué du réassort périodique.

**Différences.** UBL décrit un processus producteur-distributeur avec commandes et livraisons, notamment pour des articles NOS saisonniers. FLOW isole la décision des apports, sans adopter ce schéma de coopération, sa cadence hebdomadaire ni ses délais de livraison.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[Universal Business Language Version 2.4](https://docs.oasis-open.org/ubl/UBL-2.4.html) — 2.4, consulté le 2026-09-18.

**Passage.** 2.3.3.5.3.3 Initial Stocking of the Area by Retailer ; 2.3.3.5.3.4 Periodic (Weekly) Replenishment

**Limite de preuve.** Texte primaire consulté. Attestation du terme Initial Stocking dans un contexte saisonnier ; pas une normalisation du nom Initial Stocking Decision ni un consensus des logiciels de mode.

Références : U315, ELM200, CMP108, U316.

### Logility — Initial distribution

Présentation retail — cas Groupe Dynamite · Terme descriptif employé dans une présentation client · Appui sémantique · statut : proposed

**Points communs.** Distribution initiale distinguée du réassort dans un contexte de mode, de magasins et de déclinaisons style/couleur/taille.

**Différences.** La présentation ne définit pas une capacité de décision ni ses entrées/sorties. Distribution décrit le flux vers les magasins ; le terme ne précise pas à lui seul la frontière avec la réalisation logistique.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[Retail Optimization Gives Groupe Dynamite an Edge](https://www.logility.com/webcast/retail-optimization-gives-groupe-dynamite-an-edge/) — Page de présentation sans édition figée ni date affichée, consulté le 2026-09-18.

**Passage.** Présentation textuelle du webcast, initial distribution as well as replenishment

**Limite de preuve.** Texte primaire de présentation consulté ; vidéo non visionnée. Usage descriptif attesté, pas nom de module ou taxonomie standard démontré.

Références : U315, ELM200, CMP108, U316.

### Nextail — First Allocation / initial distribution

First Allocation · Nom d’une solution et formulation descriptive de sa finalité · Appui sémantique · statut : proposed

**Points communs.** La solution First Allocation vise la distribution initiale de nouveaux produits aux magasins ; Replenishment et Store Transfers sont présentés séparément.

**Différences.** Le nom de solution conserve Allocation ; initial distribution apparaît dans sa description. Le produit regroupe prévisions, optimisation et paramètres : ce regroupement ne définit pas la hiérarchie FLOW.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[Nextail — Solution specifications](https://help.nextail.co/en/solution-specifications) — Documentation en ligne non versionnée, consulté le 2026-09-18.

**Passage.** First Allocation ; Replenishment ; Store Transfers

**Limite de preuve.** Documentation primaire consultée. Confirme le sens d’initial distribution mais pas son adoption comme libellé officiel de capacité.

Références : U315, ELM200, CMP108, U316.

## Comparaison par rapport au marché — D05.e Replenishment Decision

### SAP — In-Season Fill-In

Allocation Management · Scénarios métier d’un produit · Recouvrement partiel · statut : proposed

**Points communs.** Réapprovisionnement après les premières ventes ou pendant la commercialisation, distinct de la mise en place initiale. Appui au réassort continu demandé U313.

**Différences.** SAP décrit un produit qui couvre planification et traitement de la distribution. FLOW sépare décision des apports, gestion des Orders et exécution. Le réassort décrit par Laurent est guidé par des seuils ; cette documentation SAP ne démontre pas une formule identique. La notion SAP de collection ou thème ne prouve pas un usage de capsules chez Beaumanoir.

**Position FLOW.** U427 : deux politiques de réassort et un mécanisme d’ajustement combinable sous D05.e. La décomposition métier n’impose pas celle du produit ; Inventory Target Decision détermine les cibles, D04 applique les changements autorisés et D06 orchestre.

[SAP Allocation Management — Business Overview](https://help.sap.com/docs/CARAB/00197153997746b4bec2020d00e66ea9/e99798c39a3f4956bd5ce509b39382f7.html?locale=en-US&state=PRODUCTION&version=5.0.2) — 5.0 FPS02 — version de la documentation consultée, consulté le 2026-09-18.

**Passage.** Business Scenarios : Initial Allocation ; In-Season Fill-In

**Limite de preuve.** Texte primaire indexé consulté ; ouverture de la page sans corps exploitable. Pas de preuve de déploiement Beaumanoir, ni d’équivalence de hiérarchie Capacité → Comportement.

Références : ELM198, CMP106, U310, U311, U313, U314, CMP107, U315, CMP108, U316, U427.

### RELEX — In-season replenishment

Replenishment and allocation · Fonctions présentées par l’éditeur · Recouvrement partiel · statut : proposed

**Points communs.** Réapprovisionnement après les premières ventes ou pendant la commercialisation, distinct de la mise en place initiale. Appui au réassort continu demandé U313.

**Différences.** La présentation RELEX associe aussi commandes présaison et gestion de fin de saison. Ces fonctions ne sont pas ajoutées implicitement à FLOW. Le réassort produit utilise notamment des prévisions ; une identité avec les seuils et règles Beaumanoir n’est pas établie.

**Position FLOW.** U427 : deux politiques de réassort et un mécanisme d’ajustement combinable sous D05.e. La décomposition métier n’impose pas celle du produit ; Inventory Target Decision détermine les cibles, D04 applique les changements autorisés et D06 orchestre.

[RELEX — Replenishment and allocation](https://www.relexsolutions.com/solutions/automatic-replenishment-system/) — Présentation produit évolutive, sans édition figée, consulté le 2026-09-18.

**Passage.** Manage the full cycle for your seasonal items ; Manage seasons effectively

**Limite de preuve.** Présentation commerciale primaire consultée. Aucun contrat fonctionnel exhaustif, aucune formule de seuil équivalente ni déploiement Beaumanoir démontré.

Références : ELM198, CMP106, U310, U311, U313, U314, CMP107, U315, CMP108, U316, U427.

### Microsoft — Requirement / Period / Min./Max.

Dynamics 365 Supply Chain Management — Master planning · Méthodes de réapprovisionnement configurables dans un produit · Appui aux politiques, pas équivalence de hiérarchie · statut : proposed

**Points communs.** Requirement traite les besoins identifiés, Period les regroupe sur une fenêtre, Min./Max. restaure un niveau cible lorsque le stock prévisionnel passe sous un seuil. Ces règles éclairent deux façons de décider les apports, par besoins datés ou par seuil/cible.

**Différences.** Microsoft produit des ordres planifiés et couvre aussi des scénarios à la commande. FLOW sépare décision de stock, gestion des Orders et promesse D03. Le réassort Beaumanoir par seuils ne prouve pas une formule Min/Max exacte. Period et les multiples de quantité restent des modalités ; ils ne créent pas automatiquement des comportements.

**Position FLOW.** U427 : deux politiques de réassort et un mécanisme d’ajustement combinable sous D05.e. La décomposition métier n’impose pas celle du produit ; Inventory Target Decision détermine les cibles, D04 applique les changements autorisés et D06 orchestre.

[Replenishment methods and quantity modification](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification) — Documentation D365 SCM, mise à jour affichée 2026-07-01, consulté le 2026-09-18.

**Passage.** Coverage codes ; Impact of the order quantity from default order settings

**Limite de preuve.** Texte primaire consulté le 18 septembre 2026. Pas de preuve de politique Requirement installée chez Beaumanoir ; ni correspondance univoque entre méthode logicielle et comportement métier.

Références : U323, ELM202, CMP110, U324, C98, CMP111, U425, U427.

### Microsoft — Action messages — Advance / Postpone / Increase / Decrease

Dynamics 365 Supply Chain Management — Master planning · Recommandations de planification sur des ordres existants · Recouvrement fonctionnel · statut : proposed

**Points communs.** La planification recommande de modifier dates et quantités d’apports existants après évolution des besoins, pour limiter manques et excédents.

**Différences.** Les types de message ne sont pas des comportements FLOW. La recommandation et son application aux Orders restent distinctes. L’aptitude à ajuster les apports appartient déjà au périmètre D05.e ; un comportement séparé exige un mécanisme ou bénéfice supplémentaire, au-delà de ces opérations.

**Position FLOW.** U427 : deux politiques de réassort et un mécanisme d’ajustement combinable sous D05.e. La décomposition métier n’impose pas celle du produit ; Inventory Target Decision détermine les cibles, D04 applique les changements autorisés et D06 orchestre.

[Action messages](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages) — Documentation D365 SCM, mise à jour affichée 2026-03-26, consulté le 2026-09-18.

**Passage.** Introduction ; Select action messages ; Action messages for orders related to safety stock

**Limite de preuve.** Texte primaire consulté. Les règles Microsoft de période de gel et de stock de sécurité ne sont pas adoptées pour FLOW ; aucun engagement ferme déclaré librement modifiable.

Références : U323, ELM202, CMP110, U324, C98, CMP111, U425, U427.

### Microsoft — Minimum/maximum keys / seasonal inventory levels

Dynamics 365 Supply Chain Management — Master planning · Paramètres temporels de couverture · Appui à la séparation paramètres / utilisation · statut : proposed

**Points communs.** Les niveaux minimum et maximum peuvent être différenciés selon les périodes saisonnières. La logique Min/Max réagit au stock disponible projeté ; une configuration n’est donc pas nécessairement fixe ni indépendante de la demande.

**Différences.** FLOW place la détermination des valeurs dans Inventory Target Decision et leur gouvernance/application dans Supply Protection. Les écrans et clés Microsoft ne prescrivent pas cette décomposition ; aucun calendrier mensuel ou formule du produit imposé à Beaumanoir.

**Position FLOW.** U427 : deux politiques de réassort et un mécanisme d’ajustement combinable sous D05.e. La décomposition métier n’impose pas celle du produit ; Inventory Target Decision détermine les cibles, D04 applique les changements autorisés et D06 orchestre.

[Safety stock fulfillment for items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-replenishment) — Documentation D365 SCM, mise à jour affichée 2026-03-26, consulté le 2026-09-18.

**Passage.** Example: Minimum key ; Example: Min/max coverage code

**Limite de preuve.** Texte primaire consulté le 18 septembre 2026. Variation saisonnière documentée ; pas preuve d’une réoptimisation automatique à chaque événement ni d’une configuration Beaumanoir installée.

Références : U324, C98, ELM203, CMP111, U425, U427.

### Oracle — Policy parameters — Min-max planning

Fusion Cloud SCM — Replenishment Planning · Calcul et utilisation de paramètres de politique · Appui fonctionnel, pas équivalence de capacités · statut : proposed

**Points communs.** Le minimum est calculé à partir de la demande pendant le délai et du stock de sécurité. La politique utilise ensuite une position de stock pour déterminer le déclenchement et la quantité de réapprovisionnement.

**Différences.** Les paramètres Oracle et leurs formules sont propres au produit et à la politique choisie. FLOW conserve les responsabilités de décision et de management distinctes sans imposer cette formule ni confondre minimum de sécurité, seuil de commande et cible.

**Position FLOW.** U427 : deux politiques de réassort et un mécanisme d’ajustement combinable sous D05.e. La décomposition métier n’impose pas celle du produit ; Inventory Target Decision détermine les cibles, D04 applique les changements autorisés et D06 orchestre.

[Policy Assignment Sets](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/policy-assignment-sets.html) — Fusion Cloud SCM 26B, consulté le 2026-09-18.

**Passage.** Policy Parameters, table Policy Type / Method for Calculation of Quantities / How the Policy Type Is Used, Min-max planning

**Limite de preuve.** Documentation primaire consultée. Appui à la dépendance des seuils aux besoins/délais ; pas d’équivalence de hiérarchie FLOW ni de preuve d’installation Beaumanoir.

Références : U324, C98, ELM203, CMP111, U425, U427.

### Microsoft — Coverage settings

Dynamics 365 Supply Chain Management · Méthodes et recommandations produit · Recouvrement partiel · statut : proposed

**Points communs.** Per requirement, Per period et Min/Max décrivent des méthodes distinctes de réapprovisionnement et de dimensionnement des lots.

**Différences.** FLOW conserve ces politiques dans une capacité de décision, sans comportement automatique par méthode. La page présente aussi Priority et Decoupling point : leur présence ne valide pas leur adoption ni une couverture exhaustive par cet arbitrage.

**Position FLOW.** U427 : deux politiques de réassort et un mécanisme d’ajustement combinable sous D05.e. La décomposition métier n’impose pas celle du produit ; Inventory Target Decision détermine les cibles, D04 applique les changements autorisés et D06 orchestre.

[Coverage settings](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/coverage-settings) — 2026-03-25, consulté le 2026-09-19.

**Passage.** Coverage codes

**Limite de preuve.** Page primaire consultée ; aucune preuve de déploiement Beaumanoir ni alignement de taxonomie imposé.

Références : U425, ELM252, CMP163, U427.

### Microsoft — Action messages

Dynamics 365 Supply Chain Management · Méthodes et recommandations produit · Recouvrement partiel · statut : proposed

**Points communs.** Les changements de besoins conduisent à des suggestions d’avance, report, augmentation et diminution des ordres existants.

**Différences.** FLOW distingue recommandation, vérification/application autorisée et réalisation. La recommandation d’annulation dans FLOW ne présume pas un code Cancel dans cette liste Microsoft.

**Position FLOW.** U427 : deux politiques de réassort et un mécanisme d’ajustement combinable sous D05.e. La décomposition métier n’impose pas celle du produit ; Inventory Target Decision détermine les cibles, D04 applique les changements autorisés et D06 orchestre.

[Action messages](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages) — 2026-03-26, consulté le 2026-09-19.

**Passage.** Introduction ; Select action messages

**Limite de preuve.** Page primaire consultée ; aucune preuve de déploiement Beaumanoir ni alignement de taxonomie imposé.

Références : U425, ELM252, CMP163, U427.

## Comparaison par rapport au marché — D05.c Stock Redistribution Decision

### Oracle — Inventory Rebalancing / sweep location

Fusion Cloud SCM — Replenishment Planning · Fonctionnalité de planification · Recouvrement partiel · statut : proposed

**Points communs.** Transferts de lieux en excédent vers des lieux en manque et possibilité de diriger des excédents vers un lieu de collecte. Le calcul tient compte des demandes, apports et protections du donneur.

**Différences.** Oracle décrit un traitement exécuté avant le replenishment et générant des ordres planifiés. FLOW sépare décision, application aux Orders et exécution sans adopter cet ordre de traitement. Oracle 26B précise que ce rebalancing ne fournit pas de recommandations échelonnées dans le temps.

**Position FLOW.** U318 adopte deux comportements sous Stock Redistribution Decision : rééquilibrage entre sites et consolidation de stocks dispersés, avec reconstitution d’assortiments de tailles et regroupement des reliquats. Les formulations anglaises Inventory Rebalancing et Stock Consolidation sont éditoriales ; les correspondances produit restent proposées. FLOW décide les transferts intersites ; D04 gère les Orders et D06 l’exécution.

[Overview of Inventory Rebalancing](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html) — Fusion Cloud SCM 26B, consulté le 2026-09-18.

**Passage.** Salient Features ; Additional Points About Inventory Rebalancing

**Limite de preuve.** Documentation primaire consultée ; ne démontre ni un optimum universel, ni la décomposition FLOW, ni un déploiement Beaumanoir.

Références : U317, ELM201, CMP109, U318.

### Nextail — Inventory rebalancing / consolidation

Store Transfers / Inventory Rebalancing — cas Merkal · Usage produit et témoignage client publié par l’éditeur · Appui sémantique et recouvrement partiel · statut : proposed

**Points communs.** Rééquilibrage de fin de saison entre magasins et amélioration de la disponibilité des tailles par consolidation. La valeur recherchée dépasse le simple comblement d’un manque global en unités.

**Différences.** Le témoignage documente le bénéfice de consolidation des tailles, pas les règles de calcul ni une taxonomie de comportements. FLOW réunit, selon U318, reconstitution d’assortiments et regroupement des reliquats sous un même mécanisme de consolidation intersites, tout en conservant leurs cas et critères distincts.

**Position FLOW.** U318 adopte deux comportements sous Stock Redistribution Decision : rééquilibrage entre sites et consolidation de stocks dispersés, avec reconstitution d’assortiments de tailles et regroupement des reliquats. Les formulations anglaises Inventory Rebalancing et Stock Consolidation sont éditoriales ; les correspondances produit restent proposées. FLOW décide les transferts intersites ; D04 gère les Orders et D06 l’exécution.

[Merkal implements AI to centralize and streamline inventory planning across all channels](https://nextail.co/customer/merkal-footwear-inventory-planning/) — Page de cas client évolutive sans édition figée, consulté le 2026-09-18.

**Passage.** Sharper store transfers and deeper insights for additional revenue ; témoignage Alberto Garcia sur size availability / consolidation

**Limite de preuve.** Texte primaire de la page consulté ; étude téléchargeable non consultée. Aucune métrique commerciale reprise ni applicabilité Beaumanoir présumée.

Références : U317, ELM201, CMP109, U318.

### SAP — Stock Consolidation

Extended Warehouse Management · Opération interne d’entrepôt · Périmètre différent malgré proximité de nom · statut : proposed

**Points communs.** Le terme consolidation désigne un regroupement de stock avec un bénéfice de quantité ou d’espace.

**Différences.** SAP EWM regroupe du stock à l’intérieur d’un entrepôt, pour compléter des unités de stockage ou libérer des emplacements. Le sujet FLOW examiné est la décision de regroupement entre sites ; cette fonction EWM ne doit pas être présentée comme son équivalent.

**Position FLOW.** U318 adopte deux comportements sous Stock Redistribution Decision : rééquilibrage entre sites et consolidation de stocks dispersés, avec reconstitution d’assortiments de tailles et regroupement des reliquats. Les formulations anglaises Inventory Rebalancing et Stock Consolidation sont éditoriales ; les correspondances produit restent proposées. FLOW décide les transferts intersites ; D04 gère les Orders et D06 l’exécution.

[Stock Consolidation](https://help.sap.com/docs/PRODUCT_ID/9832125c23154a179bfa1784cdc9577a/d0b4ebf54dda4179b68e334607e7fb5b.html) — EWM 2025 FPS01 — février 2026, consulté le 2026-09-18.

**Passage.** Définition de Stock Consolidation et deux stratégies

**Limite de preuve.** Texte primaire indexé consulté ; ouverture directe sans corps exploitable. Contre-exemple de périmètre, pas preuve de couverture de redistribution intersites.

Références : U317, ELM201, CMP109, U318.

## Comparaison par rapport au marché — D06 Process Management

### Camunda — Process orchestration

Process Orchestration Handbook, page web courante · Concept et offre logicielle · Recouvrement partiel · statut : proposed

**Points communs.** Coordination des tâches manuelles et automatisées, des personnes, systèmes et dispositifs participant au processus.

**Différences.** Camunda décrit une plateforme et des mécanismes transverses. FLOW cartographie des responsabilités métier et sépare explicitement décision d’adaptation, orchestration et suivi.

**Position FLOW.** Le Process orchestre des Services ; Process Orchestration reprend le vocabulaire établi. Les autres intitulés FLOW ne constituent pas une taxonomie Camunda.

[Process Orchestration Handbook](https://camunda.com/process-orchestration/) — Page web consultée le 19 septembre 2026, consulté le 2026-09-19.

**Passage.** What is process orchestration? ; Processes with diverse endpoints

**Limite de preuve.** Source primaire effectivement consultée ; présentation éditeur, sans preuve de déploiement Beaumanoir.

Références : U407, U408, U409, ELM244, CMP155.

### Microsoft — Orchestration flows and providers

Dynamics 365 Intelligent Order Management · Mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Parcours de commande coordonné par actions, événements, politiques et communications avec les providers.

**Différences.** Le parcours IOM est contextualisé à la commande ; son périmètre produit ne se transpose pas directement au domaine FLOW. Séparer Service et Process ne présume ni provider unique ni cardinalité Task/appel.

**Position FLOW.** Appui à la distinction entre progression du processus et contributions des services ; aucune taxonomie complète adoptée.

[Intelligent Order Management overview](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview) — Documentation web, mise à jour 2026-01-30, consulté le 2026-09-19.

**Passage.** Providers ; Orchestration

**Limite de preuve.** Source primaire effectivement consultée ; pas de preuve installée Beaumanoir.

Références : U407, U408, U409, ELM244, CMP155.

## Comparaison par rapport au marché — D07.d Operations Tracking

### SAP — Learning about the SAP EWM Solution

EWM for SAP S/4HANA Cloud Private Edition, extra stack ; cours sans numéro de release · documentation produit · Recouvrement partiel · statut : proposed

**Points communs.** EWM distingue les opérations entrantes, internes et sortantes : déchargement, rangement, préparation et chargement, avec suivi des unités logistiques et intégration TM.

**Différences.** Appui au périmètre sur site ; ne prescrit pas deux ou trois comportements FLOW ni un libellé canonique Warehouse Visibility.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[Learning about the SAP EWM Solution](https://learning.sap.com/courses/cloud-onboarding-for-sap-ewm-for-sap-s-4hana-cloud-private-edition-extra-stack/learning-about-the-sap-ewm-solution) — EWM for SAP S/4HANA Cloud Private Edition, extra stack ; cours sans numéro de release, consulté le 2026-09-19.

**Passage.** Introduction ; Goods Receipt ; Storage & Operations ; Conclusion

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

### project44 — Enhancing Automotive Finished Vehicle Logistics with Real Time Visibility

Article éditeur du 22 août 2023 ; édition logicielle non indiquée · article éditeur · Recouvrement partiel · statut : proposed

**Points communs.** Le terme Transportation Visibility accompagne localisation, progression multimodale, ETA et notifications ; exemple automobile au niveau véhicule.

**Différences.** Appui lexical et de périmètre, pas import du contexte automobile ni garantie de temps réel pour FLOW.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[Enhancing Automotive Finished Vehicle Logistics with Real Time Visibility](https://www.project44.com/blog/enhancing-automotive-finished-vehicle-logistics-with-real-time-visibility/) — Article éditeur du 22 août 2023 ; édition logicielle non indiquée, consulté le 2026-09-19.

**Passage.** Real-time transportation visibility / multimodal tracking

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

### Blue Yonder — What is Blue Yonder Store Execution Inventory Management?

Page produit évolutive sans édition figée · présentation produit · Recouvrement partiel · statut : proposed

**Points communs.** Store Execution désigne notamment les opérations de réception et de fiabilisation du stock en magasin ; la page décrit une réception directe en rayon et le résultat de disponibilité en rayon.

**Différences.** Présentation produit : réception et disponibilité en rayon documentées ; Store Visibility est le nom FLOW adopté par cohérence, pas une taxonomie éditeur démontrée.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[What is Blue Yonder Store Execution Inventory Management?](https://info.blueyonder.com/order-management-commerce/what-is-blue-yonder-store-execution-inventory-management) — Page produit évolutive sans édition figée, consulté le 2026-09-19.

**Passage.** Présentation et processus magasin

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

### Microsoft — Azure Business Process Tracking overview

Azure Business Process Tracking ; page mise à jour 2025-09-11 · documentation produit · Recouvrement partiel · statut : proposed

**Points communs.** Corrélation des étapes et de leurs propriétés métier par identifiant de transaction, par exemple commande ou case.

**Différences.** Le produit documenté mappe des étapes métier sur les opérations des workflows Standard stateful Logic Apps. FLOW retient le concept de suivi métier ; le lien Task/appels est sa convention, sans équivalence un pour un ni obligation Azure.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[Azure Business Process Tracking overview](https://learn.microsoft.com/en-us/azure/business-process-tracking/overview) — Azure Business Process Tracking ; page mise à jour 2025-09-11, consulté le 2026-09-19.

**Passage.** Business process design and tracking ; Limitations and known issues

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

### Microsoft — View Workflow Status and Run History

Azure Logic Apps ; documentation évolutive sans édition figée · documentation produit · Recouvrement partiel · statut : proposed

**Points communs.** Consultation des exécutions et de leurs actions, de leur statut et de leurs entrées/sorties pour suivre les traitements.

**Différences.** Suivi d’un produit configuré ; un statut technique ne définit pas le résultat métier du service.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[View Workflow Status and Run History](https://learn.microsoft.com/en-us/azure/logic-apps/view-workflow-status-run-history) — Azure Logic Apps ; documentation évolutive sans édition figée, consulté le 2026-09-19.

**Passage.** Workflow run history ; action status and inputs/outputs

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

### Camunda — Process Observability & AI Agent Monitoring

Présentation produit évolutive sans version figée · présentation produit · Recouvrement partiel · statut : proposed

**Points communs.** Visibilité des instances de processus en cours, de leurs variables et incidents, reliée au contexte du processus.

**Différences.** Présentation commerciale de Process Observability, incluant des moyens d’intervention et d’analyse plus larges que le tracking FLOW. Ne prouve pas une collecte exhaustive de tout service externe.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[Process Observability & AI Agent Monitoring](https://camunda.com/platform/observability/) — Présentation produit évolutive sans version figée, consulté le 2026-09-19.

**Passage.** Process instances, incidents and distinction from APM/log monitoring

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

## Comparaison par rapport au marché — D06.d Process Orchestration

### Camunda — Process orchestration

Process Orchestration Handbook, page web courante · Concept et offre logicielle · Recouvrement partiel · statut : proposed

**Points communs.** Coordination des tâches manuelles et automatisées, des personnes, systèmes et dispositifs participant au processus.

**Différences.** Camunda décrit une plateforme et des mécanismes transverses. FLOW cartographie des responsabilités métier et sépare explicitement décision d’adaptation, orchestration et suivi.

**Position FLOW.** Le Process orchestre des Services ; Process Orchestration reprend le vocabulaire établi. Les autres intitulés FLOW ne constituent pas une taxonomie Camunda.

[Process Orchestration Handbook](https://camunda.com/process-orchestration/) — Page web consultée le 19 septembre 2026, consulté le 2026-09-19.

**Passage.** What is process orchestration? ; Processes with diverse endpoints

**Limite de preuve.** Source primaire effectivement consultée ; présentation éditeur, sans preuve de déploiement Beaumanoir.

Références : U407, U408, U409, ELM244, CMP155.

### Microsoft — Orchestration flows and providers

Dynamics 365 Intelligent Order Management · Mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Parcours de commande coordonné par actions, événements, politiques et communications avec les providers.

**Différences.** Le parcours IOM est contextualisé à la commande ; son périmètre produit ne se transpose pas directement au domaine FLOW. Séparer Service et Process ne présume ni provider unique ni cardinalité Task/appel.

**Position FLOW.** Appui à la distinction entre progression du processus et contributions des services ; aucune taxonomie complète adoptée.

[Intelligent Order Management overview](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview) — Documentation web, mise à jour 2026-01-30, consulté le 2026-09-19.

**Passage.** Providers ; Orchestration

**Limite de preuve.** Source primaire effectivement consultée ; pas de preuve installée Beaumanoir.

Références : U407, U408, U409, ELM244, CMP155.

## Comparaison par rapport au marché — D14 Service Catalog

### Camunda — Process orchestration

Process Orchestration Handbook, page web courante · Concept et offre logicielle · Recouvrement partiel · statut : proposed

**Points communs.** Coordination des tâches manuelles et automatisées, des personnes, systèmes et dispositifs participant au processus.

**Différences.** Camunda décrit une plateforme et des mécanismes transverses. FLOW cartographie des responsabilités métier et sépare explicitement décision d’adaptation, orchestration et suivi.

**Position FLOW.** Le Process orchestre des Services ; Process Orchestration reprend le vocabulaire établi. Les autres intitulés FLOW ne constituent pas une taxonomie Camunda.

[Process Orchestration Handbook](https://camunda.com/process-orchestration/) — Page web consultée le 19 septembre 2026, consulté le 2026-09-19.

**Passage.** What is process orchestration? ; Processes with diverse endpoints

**Limite de preuve.** Source primaire effectivement consultée ; présentation éditeur, sans preuve de déploiement Beaumanoir.

Références : U407, U408, U409, ELM244, CMP155.

### Microsoft — Orchestration flows and providers

Dynamics 365 Intelligent Order Management · Mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Parcours de commande coordonné par actions, événements, politiques et communications avec les providers.

**Différences.** Le parcours IOM est contextualisé à la commande ; son périmètre produit ne se transpose pas directement au domaine FLOW. Séparer Service et Process ne présume ni provider unique ni cardinalité Task/appel.

**Position FLOW.** Appui à la distinction entre progression du processus et contributions des services ; aucune taxonomie complète adoptée.

[Intelligent Order Management overview](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview) — Documentation web, mise à jour 2026-01-30, consulté le 2026-09-19.

**Passage.** Providers ; Orchestration

**Limite de preuve.** Source primaire effectivement consultée ; pas de preuve installée Beaumanoir.

Références : U407, U408, U409, ELM244, CMP155.

## Comparaison par rapport au marché — D06.f Process Adaptation Decision

### Camunda — Process orchestration

Process Orchestration Handbook, page web courante · Concept et offre logicielle · Recouvrement partiel · statut : proposed

**Points communs.** Coordination des tâches manuelles et automatisées, des personnes, systèmes et dispositifs participant au processus.

**Différences.** Camunda décrit une plateforme et des mécanismes transverses. FLOW cartographie des responsabilités métier et sépare explicitement décision d’adaptation, orchestration et suivi.

**Position FLOW.** Le Process orchestre des Services ; Process Orchestration reprend le vocabulaire établi. Les autres intitulés FLOW ne constituent pas une taxonomie Camunda.

[Process Orchestration Handbook](https://camunda.com/process-orchestration/) — Page web consultée le 19 septembre 2026, consulté le 2026-09-19.

**Passage.** What is process orchestration? ; Processes with diverse endpoints

**Limite de preuve.** Source primaire effectivement consultée ; présentation éditeur, sans preuve de déploiement Beaumanoir.

Références : U407, U408, U409, ELM244, CMP155.

### Microsoft — Orchestration flows and providers

Dynamics 365 Intelligent Order Management · Mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Parcours de commande coordonné par actions, événements, politiques et communications avec les providers.

**Différences.** Le parcours IOM est contextualisé à la commande ; son périmètre produit ne se transpose pas directement au domaine FLOW. Séparer Service et Process ne présume ni provider unique ni cardinalité Task/appel.

**Position FLOW.** Appui à la distinction entre progression du processus et contributions des services ; aucune taxonomie complète adoptée.

[Intelligent Order Management overview](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview) — Documentation web, mise à jour 2026-01-30, consulté le 2026-09-19.

**Passage.** Providers ; Orchestration

**Limite de preuve.** Source primaire effectivement consultée ; pas de preuve installée Beaumanoir.

Références : U407, U408, U409, ELM244, CMP155.

## Comparaison par rapport au marché — BHV006 Simulation & Analysis

### Microsoft — Action messages

Dynamics 365 SCM · Mécanisme métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Recommandations de changement de quantités ou dates, distinctes de leur application.

**Différences.** Appui à la notion de recommandation ; ne démontre pas que toute recommandation résulte d’une simulation ni ne valide notre hiérarchie de capacités.

**Position FLOW.** U345/C99 : Supply Assignment porte l’application des affectations d’un plan ; décisions spécialisées et autres capacités gardent leurs responsabilités. Les recommandations éclairent Simulation & Analysis sans constituer un engagement.

[Action messages](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages) — Mise à jour 2026-03-26, consulté le 2026-09-18.

**Passage.** Introduction ; Select action messages

**Limite de preuve.** Documentation primaire consultée, texte indexé SAP et page Microsoft ouverte ; aucune réalisation Beaumanoir démontrée.

Références : U345, C99, ELM215, CMP123.

## Comparaison par rapport au marché — BHV024 Inventory Rebalancing

### Oracle — Inventory Rebalancing / sweep location

Fusion Cloud SCM — Replenishment Planning · Fonctionnalité de planification · Recouvrement partiel · statut : proposed

**Points communs.** Transferts de lieux en excédent vers des lieux en manque et possibilité de diriger des excédents vers un lieu de collecte. Le calcul tient compte des demandes, apports et protections du donneur.

**Différences.** Oracle décrit un traitement exécuté avant le replenishment et générant des ordres planifiés. FLOW sépare décision, application aux Orders et exécution sans adopter cet ordre de traitement. Oracle 26B précise que ce rebalancing ne fournit pas de recommandations échelonnées dans le temps.

**Position FLOW.** U318 adopte deux comportements sous Stock Redistribution Decision : rééquilibrage entre sites et consolidation de stocks dispersés, avec reconstitution d’assortiments de tailles et regroupement des reliquats. Les formulations anglaises Inventory Rebalancing et Stock Consolidation sont éditoriales ; les correspondances produit restent proposées. FLOW décide les transferts intersites ; D04 gère les Orders et D06 l’exécution.

[Overview of Inventory Rebalancing](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html) — Fusion Cloud SCM 26B, consulté le 2026-09-18.

**Passage.** Salient Features ; Additional Points About Inventory Rebalancing

**Limite de preuve.** Documentation primaire consultée ; ne démontre ni un optimum universel, ni la décomposition FLOW, ni un déploiement Beaumanoir.

Références : U317, ELM201, CMP109, U318.

### Nextail — Inventory rebalancing / consolidation

Store Transfers / Inventory Rebalancing — cas Merkal · Usage produit et témoignage client publié par l’éditeur · Appui sémantique et recouvrement partiel · statut : proposed

**Points communs.** Rééquilibrage de fin de saison entre magasins et amélioration de la disponibilité des tailles par consolidation. La valeur recherchée dépasse le simple comblement d’un manque global en unités.

**Différences.** Le témoignage documente le bénéfice de consolidation des tailles, pas les règles de calcul ni une taxonomie de comportements. FLOW réunit, selon U318, reconstitution d’assortiments et regroupement des reliquats sous un même mécanisme de consolidation intersites, tout en conservant leurs cas et critères distincts.

**Position FLOW.** U318 adopte deux comportements sous Stock Redistribution Decision : rééquilibrage entre sites et consolidation de stocks dispersés, avec reconstitution d’assortiments de tailles et regroupement des reliquats. Les formulations anglaises Inventory Rebalancing et Stock Consolidation sont éditoriales ; les correspondances produit restent proposées. FLOW décide les transferts intersites ; D04 gère les Orders et D06 l’exécution.

[Merkal implements AI to centralize and streamline inventory planning across all channels](https://nextail.co/customer/merkal-footwear-inventory-planning/) — Page de cas client évolutive sans édition figée, consulté le 2026-09-18.

**Passage.** Sharper store transfers and deeper insights for additional revenue ; témoignage Alberto Garcia sur size availability / consolidation

**Limite de preuve.** Texte primaire de la page consulté ; étude téléchargeable non consultée. Aucune métrique commerciale reprise ni applicabilité Beaumanoir présumée.

Références : U317, ELM201, CMP109, U318.

## Comparaison par rapport au marché — BHV025 Stock Consolidation

### Oracle — Inventory Rebalancing / sweep location

Fusion Cloud SCM — Replenishment Planning · Fonctionnalité de planification · Recouvrement partiel · statut : proposed

**Points communs.** Transferts de lieux en excédent vers des lieux en manque et possibilité de diriger des excédents vers un lieu de collecte. Le calcul tient compte des demandes, apports et protections du donneur.

**Différences.** Oracle décrit un traitement exécuté avant le replenishment et générant des ordres planifiés. FLOW sépare décision, application aux Orders et exécution sans adopter cet ordre de traitement. Oracle 26B précise que ce rebalancing ne fournit pas de recommandations échelonnées dans le temps.

**Position FLOW.** U318 adopte deux comportements sous Stock Redistribution Decision : rééquilibrage entre sites et consolidation de stocks dispersés, avec reconstitution d’assortiments de tailles et regroupement des reliquats. Les formulations anglaises Inventory Rebalancing et Stock Consolidation sont éditoriales ; les correspondances produit restent proposées. FLOW décide les transferts intersites ; D04 gère les Orders et D06 l’exécution.

[Overview of Inventory Rebalancing](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html) — Fusion Cloud SCM 26B, consulté le 2026-09-18.

**Passage.** Salient Features ; Additional Points About Inventory Rebalancing

**Limite de preuve.** Documentation primaire consultée ; ne démontre ni un optimum universel, ni la décomposition FLOW, ni un déploiement Beaumanoir.

Références : U317, ELM201, CMP109, U318.

### Nextail — Inventory rebalancing / consolidation

Store Transfers / Inventory Rebalancing — cas Merkal · Usage produit et témoignage client publié par l’éditeur · Appui sémantique et recouvrement partiel · statut : proposed

**Points communs.** Rééquilibrage de fin de saison entre magasins et amélioration de la disponibilité des tailles par consolidation. La valeur recherchée dépasse le simple comblement d’un manque global en unités.

**Différences.** Le témoignage documente le bénéfice de consolidation des tailles, pas les règles de calcul ni une taxonomie de comportements. FLOW réunit, selon U318, reconstitution d’assortiments et regroupement des reliquats sous un même mécanisme de consolidation intersites, tout en conservant leurs cas et critères distincts.

**Position FLOW.** U318 adopte deux comportements sous Stock Redistribution Decision : rééquilibrage entre sites et consolidation de stocks dispersés, avec reconstitution d’assortiments de tailles et regroupement des reliquats. Les formulations anglaises Inventory Rebalancing et Stock Consolidation sont éditoriales ; les correspondances produit restent proposées. FLOW décide les transferts intersites ; D04 gère les Orders et D06 l’exécution.

[Merkal implements AI to centralize and streamline inventory planning across all channels](https://nextail.co/customer/merkal-footwear-inventory-planning/) — Page de cas client évolutive sans édition figée, consulté le 2026-09-18.

**Passage.** Sharper store transfers and deeper insights for additional revenue ; témoignage Alberto Garcia sur size availability / consolidation

**Limite de preuve.** Texte primaire de la page consulté ; étude téléchargeable non consultée. Aucune métrique commerciale reprise ni applicabilité Beaumanoir présumée.

Références : U317, ELM201, CMP109, U318.

### SAP — Stock Consolidation

Extended Warehouse Management · Opération interne d’entrepôt · Périmètre différent malgré proximité de nom · statut : proposed

**Points communs.** Le terme consolidation désigne un regroupement de stock avec un bénéfice de quantité ou d’espace.

**Différences.** SAP EWM regroupe du stock à l’intérieur d’un entrepôt, pour compléter des unités de stockage ou libérer des emplacements. Le sujet FLOW examiné est la décision de regroupement entre sites ; cette fonction EWM ne doit pas être présentée comme son équivalent.

**Position FLOW.** U318 adopte deux comportements sous Stock Redistribution Decision : rééquilibrage entre sites et consolidation de stocks dispersés, avec reconstitution d’assortiments de tailles et regroupement des reliquats. Les formulations anglaises Inventory Rebalancing et Stock Consolidation sont éditoriales ; les correspondances produit restent proposées. FLOW décide les transferts intersites ; D04 gère les Orders et D06 l’exécution.

[Stock Consolidation](https://help.sap.com/docs/PRODUCT_ID/9832125c23154a179bfa1784cdc9577a/d0b4ebf54dda4179b68e334607e7fb5b.html) — EWM 2025 FPS01 — février 2026, consulté le 2026-09-18.

**Passage.** Définition de Stock Consolidation et deux stratégies

**Limite de preuve.** Texte primaire indexé consulté ; ouverture directe sans corps exploitable. Contre-exemple de périmètre, pas preuve de couverture de redistribution intersites.

Références : U317, ELM201, CMP109, U318.

## Comparaison par rapport au marché — BHV026 Store Inventory Optimization

### SAP — Decomposed (Single-Stage) Inventory Optimization

SAP IBP · Opérateur produit · Appui sémantique · statut : proposed

**Points communs.** Détermine localement stock de sécurité et position cible par produit-lieu, avec des dépendances distinctes de la topologie complète du réseau.

**Différences.** SAP exige ici des résultats du Global Multi-Stage en entrée ; ce n’est pas une preuve de trajectoire obligatoire local puis global. Ne définit pas deux capacités nommées magasin et entrepôt.

**Position FLOW.** U332 adopte trois comportements frères sous Inventory Target Decision : magasin, centre de distribution et multi-échelon. La comparaison reste proposée ; SAP Single-Stage/Multi-Stage et les fonctions RELEX ne constituent pas une nomenclature équivalente de capacités FLOW.

[Decomposed (Single-Stage) Inventory Optimization](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/a46e510f47e94abebb61afb1cda2f65d.html) — 2605, consulté le 2026-09-18.

**Passage.** Présentation ; Inputs and Outputs

**Limite de preuve.** Texte primaire indexé consulté ; rapprochement proposé et aucune réalisation Beaumanoir attestée.

Références : U331, ELM206, CMP114, U332.

### RELEX — Store inventory / DC forecast / multi-echelon optimization

Inventory planning · Mécanismes fonctionnels décrits par l’éditeur · Appui sémantique · statut : proposed

**Points communs.** Considère disponibilité en rayon et contraintes de réserves/DC ; oppose dimensionnement par lieu et positionnement coordonné des stocks de sécurité du réseau.

**Différences.** Présentation fonctionnelle et scénario illustratif ; pas catalogue de capacités ni preuve de formule ou de déploiement Beaumanoir.

**Position FLOW.** U332 adopte trois comportements frères sous Inventory Target Decision : magasin, centre de distribution et multi-échelon. La comparaison reste proposée ; SAP Single-Stage/Multi-Stage et les fonctions RELEX ne constituent pas une nomenclature équivalente de capacités FLOW.

[Inventory optimization: Keys to a successful strategy](https://www.relexsolutions.com/resources/inventory-optimization/) — Article évolutif sans version produit figée, consulté le 2026-09-18.

**Passage.** Storage and space optimization capabilities ; Multi-echelon inventory optimization

**Limite de preuve.** Texte primaire indexé consulté ; rapprochement proposé et aucune réalisation Beaumanoir attestée.

Références : U331, ELM206, CMP114, U332.

## Comparaison par rapport au marché — BHV027 Distribution Center Inventory Optimization

### SAP — Decomposed (Single-Stage) Inventory Optimization

SAP IBP · Opérateur produit · Appui sémantique · statut : proposed

**Points communs.** Détermine localement stock de sécurité et position cible par produit-lieu, avec des dépendances distinctes de la topologie complète du réseau.

**Différences.** SAP exige ici des résultats du Global Multi-Stage en entrée ; ce n’est pas une preuve de trajectoire obligatoire local puis global. Ne définit pas deux capacités nommées magasin et entrepôt.

**Position FLOW.** U332 adopte trois comportements frères sous Inventory Target Decision : magasin, centre de distribution et multi-échelon. La comparaison reste proposée ; SAP Single-Stage/Multi-Stage et les fonctions RELEX ne constituent pas une nomenclature équivalente de capacités FLOW.

[Decomposed (Single-Stage) Inventory Optimization](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/a46e510f47e94abebb61afb1cda2f65d.html) — 2605, consulté le 2026-09-18.

**Passage.** Présentation ; Inputs and Outputs

**Limite de preuve.** Texte primaire indexé consulté ; rapprochement proposé et aucune réalisation Beaumanoir attestée.

Références : U331, ELM206, CMP114, U332.

### RELEX — DC forecasts from projected store orders

Inventory planning · Fonction de prévision aval pour planification des stocks · Appui sémantique · statut : proposed

**Points communs.** La demande d’un centre de distribution peut provenir des commandes magasins projetées ; elle ne se réduit pas à une prévision indépendante de ventes consommateur.

**Différences.** Appui à la différence de contexte ; ne définit pas un comportement nommé Distribution Center Inventory Optimization et ne transfère pas la prévision dans D05.a.

**Position FLOW.** U332 adopte trois comportements frères sous Inventory Target Decision : magasin, centre de distribution et multi-échelon. La comparaison reste proposée ; SAP Single-Stage/Multi-Stage et les fonctions RELEX ne constituent pas une nomenclature équivalente de capacités FLOW.

[The best inventory planning software: AI-powered, planner-driven](https://www.relexsolutions.com/resources/inventory-planning-software/) — Article évolutif sans version produit figée, consulté le 2026-09-18.

**Passage.** DC forecasts from projected store orders

**Limite de preuve.** Texte primaire indexé consulté ; rapprochement proposé et aucune réalisation Beaumanoir attestée.

Références : U331, ELM206, CMP114, U332.

## Comparaison par rapport au marché — BHV028 Multi-Echelon Inventory Optimization

### SAP — Decomposed (Single-Stage) Inventory Optimization

SAP IBP · Opérateur produit · Appui sémantique · statut : proposed

**Points communs.** Détermine localement stock de sécurité et position cible par produit-lieu, avec des dépendances distinctes de la topologie complète du réseau.

**Différences.** SAP exige ici des résultats du Global Multi-Stage en entrée ; ce n’est pas une preuve de trajectoire obligatoire local puis global. Ne définit pas deux capacités nommées magasin et entrepôt.

**Position FLOW.** U332 adopte trois comportements frères sous Inventory Target Decision : magasin, centre de distribution et multi-échelon. La comparaison reste proposée ; SAP Single-Stage/Multi-Stage et les fonctions RELEX ne constituent pas une nomenclature équivalente de capacités FLOW.

[Decomposed (Single-Stage) Inventory Optimization](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/a46e510f47e94abebb61afb1cda2f65d.html) — 2605, consulté le 2026-09-18.

**Passage.** Présentation ; Inputs and Outputs

**Limite de preuve.** Texte primaire indexé consulté ; rapprochement proposé et aucune réalisation Beaumanoir attestée.

Références : U331, ELM206, CMP114, U332.

### RELEX — Store inventory / DC forecast / multi-echelon optimization

Inventory planning · Mécanismes fonctionnels décrits par l’éditeur · Appui sémantique · statut : proposed

**Points communs.** Considère disponibilité en rayon et contraintes de réserves/DC ; oppose dimensionnement par lieu et positionnement coordonné des stocks de sécurité du réseau.

**Différences.** Présentation fonctionnelle et scénario illustratif ; pas catalogue de capacités ni preuve de formule ou de déploiement Beaumanoir.

**Position FLOW.** U332 adopte trois comportements frères sous Inventory Target Decision : magasin, centre de distribution et multi-échelon. La comparaison reste proposée ; SAP Single-Stage/Multi-Stage et les fonctions RELEX ne constituent pas une nomenclature équivalente de capacités FLOW.

[Inventory optimization: Keys to a successful strategy](https://www.relexsolutions.com/resources/inventory-optimization/) — Article évolutif sans version produit figée, consulté le 2026-09-18.

**Passage.** Storage and space optimization capabilities ; Multi-echelon inventory optimization

**Limite de preuve.** Texte primaire indexé consulté ; rapprochement proposé et aucune réalisation Beaumanoir attestée.

Références : U331, ELM206, CMP114, U332.

## Comparaison par rapport au marché — BHV029 Periodic Physical Inventory

### SAP — Physical Inventory

SAP S/4HANA Cloud Public Edition Warehouse Management · Procédures métier et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Distingue inventaire périodique, procédures continues et cycle counting ; confronte quantités physiques et enregistrées.

**Différences.** Périmètre produit Warehouse Management ; aucune attribution automatique à FLOW des opérations WMS, ni obligation comptable ajoutée.

**Position FLOW.** U334 adopte Periodic Physical Inventory, Cycle Counting et Spot Counting sous Stocktaking, ainsi que la politique et les demandes de vérification. Réalisation physique par les exécutants ; traitement des écarts commun et ajustements tracés par Record Inventory Movements. Comparaison produit proposée ; aucun déploiement déduit.

[Physical Inventory](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/ae735d9f76024645ad4f5b1a0e6e3387.html) — 2608, consulté le 2026-09-18.

**Passage.** Physical inventory procedures

**Limite de preuve.** Texte primaire indexé consulté. Aucun déploiement Beaumanoir attesté ; différences de taxonomie conservées.

Références : U333, ELM207, CMP115, U334.

### Oracle — Counting — full physical inventory / cycle counting

E-Business Suite Mobile Supply Chain Applications · Procédures métier et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Oppose le comptage périodique de sélections d’articles au comptage physique complet pour rapprocher les quantités.

**Différences.** Référence EBS, pas Fusion Cloud ; les contraintes de blocage transactionnel du produit ne sont pas imposées à FLOW.

**Position FLOW.** U334 adopte Periodic Physical Inventory, Cycle Counting et Spot Counting sous Stocktaking, ainsi que la politique et les demandes de vérification. Réalisation physique par les exécutants ; traitement des écarts commun et ajustements tracés par Record Inventory Movements. Comparaison produit proposée ; aucun déploiement déduit.

[Counting — full physical inventory / cycle counting](https://docs.oracle.com/cd/E26401_01/doc.122/e48826/T256582T257763.htm) — 12.2, consulté le 2026-09-18.

**Passage.** Counting ; Cycle Counting

**Limite de preuve.** Texte primaire indexé consulté. Aucun déploiement Beaumanoir attesté ; différences de taxonomie conservées.

Références : U333, ELM207, CMP115, U334.

## Comparaison par rapport au marché — BHV030 Cycle Counting

### Microsoft — Cycle counting

Dynamics 365 SCM Warehouse Management · Procédures métier et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Plans récurrents, seuils déclenchant un comptage et comptage ponctuel sans travail préexistant ; traitement des différences constatées.

**Différences.** Spot ne signifie pas exclusivement déclenché par anomalie. Un seuil de comptage ne prouve pas une incohérence ; ce n’est pas un seuil de réassort. Les modalités produit se combinent et ne forment pas trois capacités universelles.

**Position FLOW.** U334 adopte Periodic Physical Inventory, Cycle Counting et Spot Counting sous Stocktaking, ainsi que la politique et les demandes de vérification. Réalisation physique par les exécutants ; traitement des écarts commun et ajustements tracés par Record Inventory Movements. Comparaison produit proposée ; aucun déploiement déduit.

[Cycle counting](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Automatically create cycle counting work ; Spot cycle counting ; Resolve cycle counting differences

**Limite de preuve.** Texte primaire indexé consulté. Aucun déploiement Beaumanoir attesté ; différences de taxonomie conservées.

Références : U333, ELM207, CMP115, U334.

### SAP — Physical Inventory

SAP S/4HANA Cloud Public Edition Warehouse Management · Procédures métier et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Distingue inventaire périodique, procédures continues et cycle counting ; confronte quantités physiques et enregistrées.

**Différences.** Périmètre produit Warehouse Management ; aucune attribution automatique à FLOW des opérations WMS, ni obligation comptable ajoutée.

**Position FLOW.** U334 adopte Periodic Physical Inventory, Cycle Counting et Spot Counting sous Stocktaking, ainsi que la politique et les demandes de vérification. Réalisation physique par les exécutants ; traitement des écarts commun et ajustements tracés par Record Inventory Movements. Comparaison produit proposée ; aucun déploiement déduit.

[Physical Inventory](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/ae735d9f76024645ad4f5b1a0e6e3387.html) — 2608, consulté le 2026-09-18.

**Passage.** Physical inventory procedures

**Limite de preuve.** Texte primaire indexé consulté. Aucun déploiement Beaumanoir attesté ; différences de taxonomie conservées.

Références : U333, ELM207, CMP115, U334.

### Oracle — Counting — full physical inventory / cycle counting

E-Business Suite Mobile Supply Chain Applications · Procédures métier et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Oppose le comptage périodique de sélections d’articles au comptage physique complet pour rapprocher les quantités.

**Différences.** Référence EBS, pas Fusion Cloud ; les contraintes de blocage transactionnel du produit ne sont pas imposées à FLOW.

**Position FLOW.** U334 adopte Periodic Physical Inventory, Cycle Counting et Spot Counting sous Stocktaking, ainsi que la politique et les demandes de vérification. Réalisation physique par les exécutants ; traitement des écarts commun et ajustements tracés par Record Inventory Movements. Comparaison produit proposée ; aucun déploiement déduit.

[Counting — full physical inventory / cycle counting](https://docs.oracle.com/cd/E26401_01/doc.122/e48826/T256582T257763.htm) — 12.2, consulté le 2026-09-18.

**Passage.** Counting ; Cycle Counting

**Limite de preuve.** Texte primaire indexé consulté. Aucun déploiement Beaumanoir attesté ; différences de taxonomie conservées.

Références : U333, ELM207, CMP115, U334.

## Comparaison par rapport au marché — BHV031 Spot Counting

### Microsoft — Cycle counting

Dynamics 365 SCM Warehouse Management · Procédures métier et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Plans récurrents, seuils déclenchant un comptage et comptage ponctuel sans travail préexistant ; traitement des différences constatées.

**Différences.** Spot ne signifie pas exclusivement déclenché par anomalie. Un seuil de comptage ne prouve pas une incohérence ; ce n’est pas un seuil de réassort. Les modalités produit se combinent et ne forment pas trois capacités universelles.

**Position FLOW.** U334 adopte Periodic Physical Inventory, Cycle Counting et Spot Counting sous Stocktaking, ainsi que la politique et les demandes de vérification. Réalisation physique par les exécutants ; traitement des écarts commun et ajustements tracés par Record Inventory Movements. Comparaison produit proposée ; aucun déploiement déduit.

[Cycle counting](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Automatically create cycle counting work ; Spot cycle counting ; Resolve cycle counting differences

**Limite de preuve.** Texte primaire indexé consulté. Aucun déploiement Beaumanoir attesté ; différences de taxonomie conservées.

Références : U333, ELM207, CMP115, U334.

## Comparaison par rapport au marché — D05.h Reservation Policy Decision

### Microsoft — Inventory reservation policies

Dynamics 365 SCM · Règle ou mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Politiques configurées : réservation automatique à la création des lignes de commande ou manuelle ; jalon de réservation configurable en production.

**Différences.** Pas de preuve dans ce passage d’un choix automatique du jalon de vente selon le stock et la vitesse de sortie. Texte primaire indexé consulté ; ouverture directe en erreur 503.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Inventory reservation policies](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities) — Documentation évolutive sans édition figée, consulté le 2026-09-18.

**Passage.** Inventory reservation policies ; Item sales reservation ; Production parameters

**Limite de preuve.** Pas de preuve dans ce passage d’un choix automatique du jalon de vente selon le stock et la vitesse de sortie. Texte primaire indexé consulté ; ouverture directe en erreur 503. Aucune couverture Beaumanoir démontrée.

Références : U341, ELM212, CMP120, U342, U343.

### commercetools — Inventory modes and expiration

Composable Commerce · Règle ou mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Réservation au panier ou à la commande, mode par panier ou ligne ; durée configurable par défaut et par entrée de stock, changement de mode possible sur ligne existante.

**Différences.** Ces leviers permettent une intégration adaptative ; ils ne prouvent pas un moteur fourni qui arbitre le jalon selon le risque de pénurie.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Inventory modes and expiration](https://docs.commercetools.com/api/inventory-overview) — Documentation évolutive sans édition figée, consulté le 2026-09-18.

**Passage.** Inventory modes ; Set the default expiration ; Reserve individual Line Items

**Limite de preuve.** Ces leviers permettent une intégration adaptative ; ils ne prouvent pas un moteur fourni qui arbitre le jalon selon le risque de pénurie. Aucune couverture Beaumanoir démontrée.

Références : U341, ELM212, CMP120, U342, U343.

### IBM — Rules-based safety stock

Sterling Intelligent Promising · Règle ou mécanisme produit · Appui méthodologique · statut : proposed

**Points communs.** Règles de stock de sécurité évaluées en temps réel ; valeurs fixes ou pourcentage au niveau réseau, validité temporelle et critères de contexte.

**Différences.** Mécanisme voisin de protection des quantités vendables, pas décision du jalon de réservation pour un client. Texte primaire indexé consulté ; ouverture directe indisponible.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Rules-based safety stock](https://www.ibm.com/docs/en/sip?topic=stock-rules-based-safety) — Documentation évolutive sans édition figée, consulté le 2026-09-18.

**Passage.** Benefits ; Network and node level safety stock ; Safety stock and total availability

**Limite de preuve.** Mécanisme voisin de protection des quantités vendables, pas décision du jalon de réservation pour un client. Texte primaire indexé consulté ; ouverture directe indisponible. Aucune couverture Beaumanoir démontrée.

Références : U341, ELM212, CMP120, U342, U343.

### SAP — Availability Change Log Events in Backorder Processing

S/4HANA Cloud 2608 · Règle ou mécanisme produit · Appui méthodologique · statut : proposed

**Points communs.** BOP réévalue la disponibilité et le réalisme des confirmations lorsque la situation de demande ou d’offre change.

**Différences.** Révision des confirmations, pas preuve d’une adaptation du jalon de réservation panier/paiement. Texte primaire indexé consulté ; page ouverte sans texte exploitable.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Availability Change Log Events in Backorder Processing](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/62d58baf16434bf1a6ad16e55e4cd0f4.html) — 2608, consulté le 2026-09-18.

**Passage.** Capturing Changes Caused by Backorder Processing (BOP) Run

**Limite de preuve.** Révision des confirmations, pas preuve d’une adaptation du jalon de réservation panier/paiement. Texte primaire indexé consulté ; page ouverte sans texte exploitable. Aucune couverture Beaumanoir démontrée.

Références : U341, ELM212, CMP120, U342, U343.

### Oracle — Reservation Time Fence

E-Business Suite Order Management · Mécanisme ou règle fonctionnelle produit · Recouvrement partiel · statut : proposed

**Points communs.** Une fenêtre avant la date planifiée conditionne la réservation automatique. Le programme Reserve Orders peut reprendre les lignes concernées.

**Différences.** Référence EBS, pas Fusion Cloud. Les modes Fair Share/Percentage/Partial du même chapitre mêlent arbitrage des quantités et réservation ; FLOW conserve leurs frontières. Texte primaire ouvert.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Reservation Time Fence](https://docs.oracle.com/cd/E26401_01/doc.122/e48842/T373258T377249.htm) — 12.2, consulté le 2026-09-18.

**Passage.** Reservation Time Fence ; Reserve Orders Concurrent Program ; Reservation Modes

**Limite de preuve.** Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.

Références : U342, ELM213, CMP121, U343.

### IBM — Handling inventory reservation

Sterling Order Management · Mécanisme ou règle fonctionnelle produit · Recouvrement partiel · statut : proposed

**Points communs.** La réservation peut servir des clients prioritaires ou un ordre premier arrivé, premier servi.

**Différences.** Appui à des politiques différenciées ; ne prouve pas une optimisation automatique de la durée par catégorie. Texte primaire indexé consulté.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Handling inventory reservation](https://www.ibm.com/docs/en/order-management?topic=2-handling-inventory-reservation) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction ; Creating reservations

**Limite de preuve.** Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.

Références : U342, ELM213, CMP121, U343.

### IBM — Reservations

Sterling Intelligent Promising · Mécanisme ou règle fonctionnelle produit · Recouvrement partiel · statut : proposed

**Points communs.** Réservations par site ou réseau, expiration configurable et réservation partielle documentées.

**Différences.** Options de réalisation ; le réseau est décomposé en sites selon les priorités IBM. Ne prouve pas une réservation sans affectation sous-jacente. Texte indexé consulté ; ouverture directe indisponible.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Reservations](https://www.ibm.com/docs/en/sip?topic=data-reservations) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Creating reservation for node or network ; Updating reservation quantity ; Defining expiration times

**Limite de preuve.** Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.

Références : U342, ELM213, CMP121, U343.

### Shopify — Shopify Checkout

Checkout · Mécanisme ou règle fonctionnelle produit · Recouvrement partiel · statut : proposed

**Points communs.** Stock retenu à la soumission des informations de paiement, avec libération en cas d’échec.

**Différences.** Jalon produit spécifique, distinct de l’ouverture de page et de l’encaissement effectif ; aucun déclencheur FLOW imposé.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Shopify Checkout](https://help.shopify.com/en/manual/checkout-settings) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction, contrôle du stock au checkout

**Limite de preuve.** Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.

Références : U342, ELM213, CMP121, U343.

## Comparaison par rapport au marché — BHV032 Milestone-Based Reservation Policy

### Microsoft — Inventory reservation policies

Dynamics 365 SCM · Règle ou mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Politiques configurées : réservation automatique à la création des lignes de commande ou manuelle ; jalon de réservation configurable en production.

**Différences.** Pas de preuve dans ce passage d’un choix automatique du jalon de vente selon le stock et la vitesse de sortie. Texte primaire indexé consulté ; ouverture directe en erreur 503.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Inventory reservation policies](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities) — Documentation évolutive sans édition figée, consulté le 2026-09-18.

**Passage.** Inventory reservation policies ; Item sales reservation ; Production parameters

**Limite de preuve.** Pas de preuve dans ce passage d’un choix automatique du jalon de vente selon le stock et la vitesse de sortie. Texte primaire indexé consulté ; ouverture directe en erreur 503. Aucune couverture Beaumanoir démontrée.

Références : U341, ELM212, CMP120, U342, U343.

### commercetools — Inventory modes and expiration

Composable Commerce · Règle ou mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Réservation au panier ou à la commande, mode par panier ou ligne ; durée configurable par défaut et par entrée de stock, changement de mode possible sur ligne existante.

**Différences.** Ces leviers permettent une intégration adaptative ; ils ne prouvent pas un moteur fourni qui arbitre le jalon selon le risque de pénurie.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Inventory modes and expiration](https://docs.commercetools.com/api/inventory-overview) — Documentation évolutive sans édition figée, consulté le 2026-09-18.

**Passage.** Inventory modes ; Set the default expiration ; Reserve individual Line Items

**Limite de preuve.** Ces leviers permettent une intégration adaptative ; ils ne prouvent pas un moteur fourni qui arbitre le jalon selon le risque de pénurie. Aucune couverture Beaumanoir démontrée.

Références : U341, ELM212, CMP120, U342, U343.

### Shopify — Shopify Checkout

Checkout · Mécanisme ou règle fonctionnelle produit · Recouvrement partiel · statut : proposed

**Points communs.** Stock retenu à la soumission des informations de paiement, avec libération en cas d’échec.

**Différences.** Jalon produit spécifique, distinct de l’ouverture de page et de l’encaissement effectif ; aucun déclencheur FLOW imposé.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Shopify Checkout](https://help.shopify.com/en/manual/checkout-settings) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction, contrôle du stock au checkout

**Limite de preuve.** Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.

Références : U342, ELM213, CMP121, U343.

## Comparaison par rapport au marché — BHV033 Time-Fenced Reservation Policy

### Oracle — Reservation Time Fence

E-Business Suite Order Management · Mécanisme ou règle fonctionnelle produit · Recouvrement partiel · statut : proposed

**Points communs.** Une fenêtre avant la date planifiée conditionne la réservation automatique. Le programme Reserve Orders peut reprendre les lignes concernées.

**Différences.** Référence EBS, pas Fusion Cloud. Les modes Fair Share/Percentage/Partial du même chapitre mêlent arbitrage des quantités et réservation ; FLOW conserve leurs frontières. Texte primaire ouvert.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Reservation Time Fence](https://docs.oracle.com/cd/E26401_01/doc.122/e48842/T373258T377249.htm) — 12.2, consulté le 2026-09-18.

**Passage.** Reservation Time Fence ; Reserve Orders Concurrent Program ; Reservation Modes

**Limite de preuve.** Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.

Références : U342, ELM213, CMP121, U343.

## Comparaison par rapport au marché — BHV034 Demand-Differentiated Reservation Policy

### Microsoft — Inventory reservation policies

Dynamics 365 SCM · Règle ou mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Politiques configurées : réservation automatique à la création des lignes de commande ou manuelle ; jalon de réservation configurable en production.

**Différences.** Pas de preuve dans ce passage d’un choix automatique du jalon de vente selon le stock et la vitesse de sortie. Texte primaire indexé consulté ; ouverture directe en erreur 503.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Inventory reservation policies](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities) — Documentation évolutive sans édition figée, consulté le 2026-09-18.

**Passage.** Inventory reservation policies ; Item sales reservation ; Production parameters

**Limite de preuve.** Pas de preuve dans ce passage d’un choix automatique du jalon de vente selon le stock et la vitesse de sortie. Texte primaire indexé consulté ; ouverture directe en erreur 503. Aucune couverture Beaumanoir démontrée.

Références : U341, ELM212, CMP120, U342, U343.

### IBM — Handling inventory reservation

Sterling Order Management · Mécanisme ou règle fonctionnelle produit · Recouvrement partiel · statut : proposed

**Points communs.** La réservation peut servir des clients prioritaires ou un ordre premier arrivé, premier servi.

**Différences.** Appui à des politiques différenciées ; ne prouve pas une optimisation automatique de la durée par catégorie. Texte primaire indexé consulté.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Handling inventory reservation](https://www.ibm.com/docs/en/order-management?topic=2-handling-inventory-reservation) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction ; Creating reservations

**Limite de preuve.** Synthèse sélective de documentation primaire ; aucune réalisation Beaumanoir démontrée.

Références : U342, ELM213, CMP121, U343.

## Comparaison par rapport au marché — BHV035 Risk-Adaptive Reservation Policy

### commercetools — Inventory modes and expiration

Composable Commerce · Règle ou mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Réservation au panier ou à la commande, mode par panier ou ligne ; durée configurable par défaut et par entrée de stock, changement de mode possible sur ligne existante.

**Différences.** Ces leviers permettent une intégration adaptative ; ils ne prouvent pas un moteur fourni qui arbitre le jalon selon le risque de pénurie.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Inventory modes and expiration](https://docs.commercetools.com/api/inventory-overview) — Documentation évolutive sans édition figée, consulté le 2026-09-18.

**Passage.** Inventory modes ; Set the default expiration ; Reserve individual Line Items

**Limite de preuve.** Ces leviers permettent une intégration adaptative ; ils ne prouvent pas un moteur fourni qui arbitre le jalon selon le risque de pénurie. Aucune couverture Beaumanoir démontrée.

Références : U341, ELM212, CMP120, U342, U343.

### IBM — Rules-based safety stock

Sterling Intelligent Promising · Règle ou mécanisme produit · Appui méthodologique · statut : proposed

**Points communs.** Règles de stock de sécurité évaluées en temps réel ; valeurs fixes ou pourcentage au niveau réseau, validité temporelle et critères de contexte.

**Différences.** Mécanisme voisin de protection des quantités vendables, pas décision du jalon de réservation pour un client. Texte primaire indexé consulté ; ouverture directe indisponible.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Rules-based safety stock](https://www.ibm.com/docs/en/sip?topic=stock-rules-based-safety) — Documentation évolutive sans édition figée, consulté le 2026-09-18.

**Passage.** Benefits ; Network and node level safety stock ; Safety stock and total availability

**Limite de preuve.** Mécanisme voisin de protection des quantités vendables, pas décision du jalon de réservation pour un client. Texte primaire indexé consulté ; ouverture directe indisponible. Aucune couverture Beaumanoir démontrée.

Références : U341, ELM212, CMP120, U342, U343.

### SAP — Availability Change Log Events in Backorder Processing

S/4HANA Cloud 2608 · Règle ou mécanisme produit · Appui méthodologique · statut : proposed

**Points communs.** BOP réévalue la disponibilité et le réalisme des confirmations lorsque la situation de demande ou d’offre change.

**Différences.** Révision des confirmations, pas preuve d’une adaptation du jalon de réservation panier/paiement. Texte primaire indexé consulté ; page ouverte sans texte exploitable.

**Position FLOW.** U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.

[Availability Change Log Events in Backorder Processing](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/62d58baf16434bf1a6ad16e55e4cd0f4.html) — 2608, consulté le 2026-09-18.

**Passage.** Capturing Changes Caused by Backorder Processing (BOP) Run

**Limite de preuve.** Révision des confirmations, pas preuve d’une adaptation du jalon de réservation panier/paiement. Texte primaire indexé consulté ; page ouverte sans texte exploitable. Aucune couverture Beaumanoir démontrée.

Références : U341, ELM212, CMP120, U342, U343.

## Comparaison par rapport au marché — BHV036 Order Firming

### Microsoft — Firm planned orders

Dynamics 365 SCM · Mécanisme ou transition métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Affermir transforme des ordres planifiés en commandes effectives achat, transfert ou production.

**Différences.** Transition de cycle de vie, pas synonyme de fixation de toutes les données d’une commande client.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Firm planned orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction

**Limite de preuve.** Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.

Références : U346, U347, ELM216, CMP124, U349, CMP125, U350, U424.

## Comparaison par rapport au marché — BHV037 Order Freezing

### SAP — Handling Requirements with Fixed Date and Quantity

S/4HANA aATP · Mécanisme ou transition métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Par défaut BOP conserve les confirmations marquées Fixed Date and Quantity et leur attribue Skip.

**Différences.** Un segment peut explicitement les inclure dans le contrôle ; ne prouve pas une immutabilité absolue ni le comportement de toute API ARun.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Handling Requirements with Fixed Date and Quantity](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/413e5cf1373142a784f6c04b2caf3fc0.html) — 2025 FPS01 (Feb 2026), consulté le 2026-09-18.

**Passage.** Page entière

**Limite de preuve.** Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.

Références : U346, U347, ELM216, CMP124, U349, CMP125, U350, U424.

### Microsoft — Keep supply for confirmed demand

Dynamics 365 SCM · Mécanisme ou transition métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Préserve une chaîne liée à une demande confirmée, notamment ordres planifiés et liens de pegging, entre les passages de planification.

**Différences.** Comportement paramétré ; la conservation du stock reçu hors positive days exige un paramètre complémentaire. Ne prouve aucun déploiement Beaumanoir.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Keep supply for confirmed demand](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand) — Prérequis documenté : 10.0.48 build 10.0.2645.33 ou ultérieur, consulté le 2026-09-18.

**Passage.** What data is preserved ; Control how on-hand inventory is pegged ; Interaction with approved planned orders

**Limite de preuve.** Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.

Références : U346, U347, ELM216, CMP124, U349, CMP125, U350, U424.

### Microsoft — Master plans — Freeze

Dynamics 365 SCM · Mécanisme ou transition métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Le gel temporel conserve les ordres planifiés dans une fenêtre.

**Différences.** Le gel empêche aussi la création de nouveaux ordres planifiés dans cette fenêtre ; différent de protéger une commande individuelle.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Master plans — Freeze](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Freeze ; Firming

**Limite de preuve.** Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.

Références : U346, U347, ELM216, CMP124, U349, CMP125, U350, U424.

## Comparaison par rapport au marché — BHV038 Order Preparation & Revision

### Oracle — Order Management Statuses

Fusion Cloud Order Management · Fonction ou état produit · Recouvrement partiel · statut : proposed

**Points communs.** Une commande enregistrée mais non soumise au fulfillment reste Draft et peut être modifiée.

**Différences.** Référence 25C ; distinction brouillon/soumission, pas équivalence automatique avec ordre planifié/affermissement Microsoft.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Regroupement de préparation/révision, incluant la date du besoin.

[Order Management Statuses](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/fauom/order-management-statuses.html) — 25C, consulté le 2026-09-18.

**Passage.** Draft

**Limite de preuve.** Passages primaires indexés consultés ; aucune réalisation client démontrée.

Références : U353, U354, ELM219, CMP128, U363, CMP133, U424.

### Microsoft — Action messages

Dynamics 365 SCM · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Suggestions Advance/Postpone de changement d’échéances sur des ordres existants.

**Différences.** Suggestion et application distinctes. Ne prouve pas une capacité autonome de calcul d’échéancier sous Lifecycle.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Regroupement de préparation/révision, incluant la date du besoin.

[Action messages](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction ; Select action messages

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U424.

### Microsoft — Approve and confirm purchase orders

Dynamics 365 Supply Chain Management · Statuts et processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Draft, In review, Approved, Rejected ; révision et réapprobation des commandes engagées.

**Différences.** Effective, Withdrawn et Superseded explicitent ici la portée des versions ; pas une transcription des enums Microsoft. Pas de poursuite inconditionnelle de l’exécution.

**Position FLOW.** U424 : dimension métier et états FLOW explicités ; correspondance proposée et portée distincte de l’accord sur le modèle.

[Approve and confirm purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation) — Documentation évolutive consultée le 19 septembre 2026, consulté le 2026-09-19.

**Passage.** Approval of purchase orders ; Changing purchase orders

**Limite de preuve.** Source primaire ouverte ; aucune preuve de déploiement Beaumanoir. Les libellés FLOW détaillés restent éditoriaux.

Références : U424, ELM251, CMP162.

## Comparaison par rapport au marché — BHV039 Order Release

### Microsoft — Release to warehouse

Dynamics 365 SCM · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** La libération de ventes et transferts vers l’entrepôt prépare les objets logistiques nécessaires au traitement.

**Différences.** Mise en œuvre WMS spécifique ; FLOW distingue autorisation métier et orchestration/réalisation des prestations.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Release to warehouse](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/release-to-warehouse-process) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Release to warehouse process

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U420, U424.

### SAP — Explaining Supply Assignment

S/4HANA Fashion ; cours évolutif · Mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** SAP distingue affectation et release check : les quantités affectées sont confrontées aux besoins pour autoriser la création de livraison, selon les règles de satisfaction.

**Différences.** ARun et ITA sont des mécanismes produit mêlant des responsabilités séparées dans FLOW. Le statut SAP ou le contrôle de livraison ne définit pas un cycle universel pour tous les Orders.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Explaining Supply Assignment](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4) — S/4HANA Fashion ; cours évolutif, consulté le 2026-09-19.

**Passage.** Supply Assignment / Release checks

**Limite de preuve.** Source primaire ouverte et consultée lors de la proposition ; aucune preuve installée Beaumanoir. Oracle 26A explicitement consulté, sans affirmation de dernière version.

Références : U410, ELM245, CMP156, U420, U424.

### Oracle — Guidelines for Managing Shipment Sets

Fusion Cloud SCM 26A ; édition explicitement consultée · Mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Oracle documente les shipment sets pour des lignes destinées à être expédiées ensemble, avec des contraintes collectives de progression et de mise en attente.

**Différences.** Un shipment set de lignes ne prouve pas une composition persistante de plusieurs Orders ni une capacité autonome. Ses contraintes produit ne sont pas imposées au modèle FLOW.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Guidelines for Managing Shipment Sets](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/faiom/guidelines-for-managing-shipment-sets.html) — Fusion Cloud SCM 26A ; édition explicitement consultée, consulté le 2026-09-19.

**Passage.** Holds / splitting / scheduling

**Limite de preuve.** Source primaire ouverte et consultée lors de la proposition ; aucune preuve installée Beaumanoir. Oracle 26A explicitement consulté, sans affirmation de dernière version.

Références : U410, ELM245, CMP156, U420, U424.

## Comparaison par rapport au marché — BHV040 Order Hold & Resume

### Microsoft — Manage order holds

Dynamics 365 SCM · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Mise en attente avec motifs, conditions de levée et effet configurable sur les réservations ; progression logistique bloquée.

**Différences.** Le checkout du hold est un verrou logiciel distinct. Les effets de réservation sont paramétrés, pas une conséquence universelle du Hold.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Manage order holds](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/tasks/manage-order-holds) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction ; Set up order hold codes ; Manage orders on hold

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U424.

### Oracle — Hold Your Sales Orders

Fusion Cloud Order Management · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Un hold peut viser une étape de traitement : les autres étapes peuvent avancer jusqu’au point bloqué.

**Différences.** Le modèle FLOW décrit portée et effets métier ; il ne copie pas les tâches d’orchestration Oracle.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Autorisation, protection, suspension, engagement et réalisation restent distincts.

[Hold Your Sales Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/sales-order-hold.html) — 26B, consulté le 2026-09-18.

**Passage.** Introduction ; How Holds Work

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U424.

## Comparaison par rapport au marché — BHV043 Order Termination

### Microsoft — Approve and confirm purchase orders

Dynamics 365 SCM · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Annulation encadrée des quantités restantes et Finalize pour empêcher de nouveaux traitements.

**Différences.** Achat, pas cycle universel. Clôture opérationnelle FLOW ne reprend pas toute la finalisation financière du produit.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Annulation et clôture distinguées au sein de la fin de demande.

[Approve and confirm purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Canceling purchase orders ; modification après confirmation

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U424.

### SAP — Functional Details: Manage Sales Orders - Version 2

S/4HANA Cloud · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Blocages par objet et rejet des lignes ; le rejet de toutes les lignes peut terminer le document sous conditions.

**Différences.** Restrictions si déjà livré ou achat lié. Rejection produit n’est pas équivalent à toute annulation ou clôture FLOW ; facturation hors périmètre métier étudié.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Annulation et clôture distinguées au sein de la fin de demande.

[Functional Details: Manage Sales Orders - Version 2](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/e7f14402cf5846b4b3d0d677c15414b1.html?locale=en-US) — Édition non relevée dans le passage indexé, consulté le 2026-09-18.

**Passage.** Delivery Block and Billing Block ; Rejection of all Items

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U424.

### Oracle — Cancel Sales Orders

Fusion Cloud Order Management · Mécanisme métier réalisé par une fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Annulation des quantités non expédiées selon états et conditions ; les quantités déjà réalisées ne sont pas effacées.

**Différences.** Cycle de commande de vente propre au produit ; compensation du processus reste dans la couche processus, pas nouveau comportement de Lifecycle.

**Position FLOW.** U424 : Lifecycle unique en D04, mobilisé par D03 ; comportements par dimensions métier et états explicites. Les états FLOW ne sont pas tous des codes natifs de cette source. Annulation et clôture distinguées au sein de la fin de demande.

[Cancel Sales Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/cancel-sales-orders.html) — 26B, consulté le 2026-09-18.

**Passage.** Cancel Remaining Quantity

**Limite de preuve.** Passages primaires consultés : pages Microsoft ouvertes ou indexées, SAP et Oracle indexés. Aucune réalisation Beaumanoir démontrée.

Références : U351, ELM217, CMP126, U363, CMP133, U424.

### Microsoft — Approve and confirm purchase orders

Dynamics 365 Supply Chain Management · Statuts et processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Retrait encadré des quantités restantes et fin du traitement.

**Différences.** FLOW distingue annulation quantitative, clôture opérationnelle et archivage ; ne reprend pas la finalisation financière Microsoft.

**Position FLOW.** U424 : dimension métier et états FLOW explicités ; correspondance proposée et portée distincte de l’accord sur le modèle.

[Approve and confirm purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation) — Documentation évolutive consultée le 19 septembre 2026, consulté le 2026-09-19.

**Passage.** Canceling purchase orders ; Changing purchase orders

**Limite de preuve.** Source primaire ouverte ; aucune preuve de déploiement Beaumanoir. Les libellés FLOW détaillés restent éditoriaux.

Références : U424, ELM251, CMP162.

## Comparaison par rapport au marché — BHV044 Order Splitting

### Oracle — What’s a Split Order Line

Fusion Cloud Order Management · Fonction produit, verbe descriptif ou stratégie de répartition · Appui sémantique · statut : proposed

**Points communs.** Split couvre plusieurs entrepôts, dates ou articles substituts, et peut créer plusieurs lignes et tâches de fulfillment.

**Différences.** Ne signifie pas toujours création de plusieurs commandes autonomes ; la fonction produit combine décisions et effets que FLOW sépare.

**Position FLOW.** U417 : Split est un comportement de Structuring dans D03 ; les structures documentaires éditeurs ne sont pas imposées à FLOW.

[What’s a Split Order Line](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/fulfillment-line-splits.html) — 26B, consulté le 2026-09-18.

**Passage.** How Order Management Determines Availability

**Limite de preuve.** Oracle ouvert ; passages Microsoft et SAP indexés consultés, page SAP dynamique sans texte à l’ouverture. Aucune implémentation Beaumanoir déduite.

Références : U360, ELM222, CMP131, U363, CMP133.

## Comparaison par rapport au marché — D04.q Order Archiving

### Microsoft — Archive Dynamics 365 Supply Chain Management Sales orders data

Dynamics 365 SCM · Fonction produit ou mécanisme de conservation · Recouvrement partiel · statut : proposed

**Points communs.** Archivage des commandes avec consultation ultérieure des en-têtes, lignes et informations liées.

**Différences.** Documentation de réalisation technique via Dataverse ; FLOW retient le résultat de conservation et de consultation, sans imposer cette architecture.

**Position FLOW.** U420 : Archiving relève de D03, distinct de Lifecycle en D04. Conservation et consultation des Orders historiques ; aucun choix de stockage ni règle légale imposé. Le rattachement au carnet est un choix FLOW, pas une taxonomie éditeur.

[Archive Dynamics 365 Supply Chain Management Sales orders data](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/archive-so) — 2026-01-14, consulté le 2026-09-18.

**Passage.** Set up an archival job ; View historical data

**Limite de preuve.** Passages primaires indexés effectivement consultés ; aucune preuve d’installation Beaumanoir.

Références : U352, ELM218, CMP127, U363, CMP133, U420.

### Oracle — Order Purge and Archive

E-Business Suite Order Management · Fonction produit ou mécanisme de conservation · Recouvrement partiel · statut : proposed

**Points communs.** Archivage sous conditions d’éligibilité et purge définitive des archives sont distincts.

**Différences.** Référence EBS, pas Fusion ; aucune durée de conservation ou obligation légale FLOW déduite.

**Position FLOW.** U420 : Archiving relève de D03, distinct de Lifecycle en D04. Conservation et consultation des Orders historiques ; aucun choix de stockage ni règle légale imposé. Le rattachement au carnet est un choix FLOW, pas une taxonomie éditeur.

[Order Purge and Archive](https://docs.oracle.com/cd/E26401_01/doc.122/e48843/T335476T430137.htm) — 12.2, consulté le 2026-09-18.

**Passage.** Eligible Orders ; Purge Archive Program

**Limite de preuve.** Passages primaires indexés effectivement consultés ; aucune preuve d’installation Beaumanoir.

Références : U352, ELM218, CMP127, U363, CMP133, U420.

### Microsoft — Archive documents

Business Central · Fonction produit ou mécanisme de conservation · Recouvrement partiel · statut : proposed

**Points communs.** Archive peut désigner des versions successives consultables, certaines restaurables sous conditions.

**Différences.** Ne pas assimiler cette notion produit à la seule sortie des commandes du stock opérationnel ; restauration de version ne signifie pas réouverture métier.

**Position FLOW.** U420 : Archiving relève de D03, distinct de Lifecycle en D04. Conservation et consultation des Orders historiques ; aucun choix de stockage ni règle légale imposé. Le rattachement au carnet est un choix FLOW, pas une taxonomie éditeur.

[Archive documents](https://learn.microsoft.com/en-us/dynamics365/business-central/across-how-to-archive-documents) — 2025-10-15, consulté le 2026-09-18.

**Passage.** Introduction ; Restore ; Delete archived versions

**Limite de preuve.** Passages primaires indexés effectivement consultés ; aucune preuve d’installation Beaumanoir.

Références : U352, ELM218, CMP127, U363, CMP133, U420.

## Comparaison par rapport au marché — BHV045 Supply Assignment Plan Application

### SAP — Supply Assignment (ARun)

S/4HANA aATP · Mécanisme métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Affectation des ressources aux besoins ; accès par BOP, ITA, affectation immédiate et API.

**Différences.** Fonctionnalité intégrée ; ni couverture de toutes les capacités FLOW ni réalisation exclusivement batch démontrées.

**Position FLOW.** U345/C99 : Supply Assignment porte l’application des affectations d’un plan ; décisions spécialisées et autres capacités gardent leurs responsabilités. Les recommandations éclairent Simulation & Analysis sans constituer un engagement. U364 : trois mécanismes sous Supply Assignment, avec distinction explicite entre complément conservant les liens et réaffectation des liens révisables. Les décisions et Order Freezing gardent leurs responsabilités. Correspondance proposée.

[Supply Assignment (ARun)](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/d335e3418f4348ffbae9f11888a62cc7.html) — 2025 FPS01, consulté le 2026-09-18.

**Passage.** Introduction et modes d’accès

**Limite de preuve.** Documentation primaire consultée, texte indexé SAP et page Microsoft ouverte ; aucune réalisation Beaumanoir démontrée.

Références : U345, C99, ELM215, CMP123, U364, CMP134.

### SAP — Backorder Processing — Reassignment

S/4HANA aATP · Mécanisme métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Le traitement peut conserver les affectations et compléter le reliquat, ou les réexaminer. Le mode preview ne produit pas d’effets logistiques.

**Différences.** Regroupement produit de décisions et d’action ; pas preuve qu’un plan externe arbitraire est importable ou qu’une simulation est appliquée sans recontrôle.

**Position FLOW.** U345/C99 : Supply Assignment porte l’application des affectations d’un plan ; décisions spécialisées et autres capacités gardent leurs responsabilités. Les recommandations éclairent Simulation & Analysis sans constituer un engagement. U364 : trois mécanismes sous Supply Assignment, avec distinction explicite entre complément conservant les liens et réaffectation des liens révisables. Les décisions et Order Freezing gardent leurs responsabilités. Correspondance proposée.

[Backorder Processing — Reassignment](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html) — 2025 FPS01, consulté le 2026-09-18.

**Passage.** Reassignment ; Requirement Sorting ; Supply Selection ; Release Check

**Limite de preuve.** Documentation primaire consultée, texte indexé SAP et page Microsoft ouverte ; aucune réalisation Beaumanoir démontrée.

Références : U345, C99, ELM215, CMP123, U364, CMP134.

## Comparaison par rapport au marché — BHV046 Incremental Supply Assignment

### SAP — Backorder Processing — Reassignment

S/4HANA aATP · Mécanisme métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Le traitement peut conserver les affectations et compléter le reliquat, ou les réexaminer. Le mode preview ne produit pas d’effets logistiques.

**Différences.** Regroupement produit de décisions et d’action ; pas preuve qu’un plan externe arbitraire est importable ou qu’une simulation est appliquée sans recontrôle.

**Position FLOW.** U345/C99 : Supply Assignment porte l’application des affectations d’un plan ; décisions spécialisées et autres capacités gardent leurs responsabilités. Les recommandations éclairent Simulation & Analysis sans constituer un engagement. U364 : trois mécanismes sous Supply Assignment, avec distinction explicite entre complément conservant les liens et réaffectation des liens révisables. Les décisions et Order Freezing gardent leurs responsabilités. Correspondance proposée.

[Backorder Processing — Reassignment](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html) — 2025 FPS01, consulté le 2026-09-18.

**Passage.** Reassignment ; Requirement Sorting ; Supply Selection ; Release Check

**Limite de preuve.** Documentation primaire consultée, texte indexé SAP et page Microsoft ouverte ; aucune réalisation Beaumanoir démontrée.

Références : U345, C99, ELM215, CMP123, U364, CMP134.

### Microsoft — Keep supply for confirmed demand

Dynamics 365 SCM · Fonction produit ou mécanisme technique ; pas capacité FLOW par défaut · Recouvrement partiel · statut : proposed

**Points communs.** Préserve une chaîne liée à une demande confirmée, notamment ordres planifiés et liens de pegging, entre les passages de planification.

**Différences.** Comportement paramétré ; la conservation du stock reçu hors positive days exige un paramètre complémentaire. Ne prouve aucun déploiement Beaumanoir.

**Position FLOW.** Appui à la stabilité des affectations, mais périmètre produit plus large incluant la chaîne de planification. Ne démontre pas une équivalence exacte avec Incremental Supply Assignment. U364 : trois mécanismes sous Supply Assignment, avec distinction explicite entre complément conservant les liens et réaffectation des liens révisables. Les décisions et Order Freezing gardent leurs responsabilités. Correspondance proposée.

[Keep supply for confirmed demand](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand) — Prérequis documenté : 10.0.48 build 10.0.2645.33 ou ultérieur, consulté le 2026-09-18.

**Passage.** What data is preserved ; Control how on-hand inventory is pegged ; Interaction with approved planned orders

**Limite de preuve.** Passages primaires consultés : pages indexées SAP, documentation Microsoft et Drools. Aucune installation client démontrée.

Références : U346, U347, ELM216, CMP124, U364, CMP134.

## Comparaison par rapport au marché — BHV047 Supply Reassignment

### SAP — Backorder Processing — Reassignment

S/4HANA aATP · Mécanisme métier réalisé par un produit · Recouvrement partiel · statut : proposed

**Points communs.** Le traitement peut conserver les affectations et compléter le reliquat, ou les réexaminer. Le mode preview ne produit pas d’effets logistiques.

**Différences.** Regroupement produit de décisions et d’action ; pas preuve qu’un plan externe arbitraire est importable ou qu’une simulation est appliquée sans recontrôle.

**Position FLOW.** U345/C99 : Supply Assignment porte l’application des affectations d’un plan ; décisions spécialisées et autres capacités gardent leurs responsabilités. Les recommandations éclairent Simulation & Analysis sans constituer un engagement. U364 : trois mécanismes sous Supply Assignment, avec distinction explicite entre complément conservant les liens et réaffectation des liens révisables. Les décisions et Order Freezing gardent leurs responsabilités. Correspondance proposée.

[Backorder Processing — Reassignment](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html) — 2025 FPS01, consulté le 2026-09-18.

**Passage.** Reassignment ; Requirement Sorting ; Supply Selection ; Release Check

**Limite de preuve.** Documentation primaire consultée, texte indexé SAP et page Microsoft ouverte ; aucune réalisation Beaumanoir démontrée.

Références : U345, C99, ELM215, CMP123, U364, CMP134.

## Comparaison par rapport au marché — D03.o Fulfillment Plan Decision

### Microsoft — Intelligent Fulfillment Optimization / Fulfillment plan

Dynamics 365 Intelligent Order Management · Service d’optimisation et résultat produit · Recouvrement partiel · statut : proposed

**Points communs.** Le service mobilise configurations et stocks, optimise des commandes groupées et produit un fulfillment plan.

**Différences.** La stratégie est une entrée. La page ne prouve ni l’examen exhaustif de toutes les ressources de l’entreprise ni la décomposition FLOW en ATP/CTP/PTP.

**Position FLOW.** U378 intègre Fulfillment Plan Decision : scénario de plan issu de décisions spécialisées. Fulfillment plan est un résultat Microsoft ; le suffixe Decision et le découpage restent propres à FLOW. Correspondance proposée.

[Intelligent Fulfillment Optimization architecture](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/ifo-arch) — Documentation mise à jour le 30 janvier 2026, consulté le 2026-09-18.

**Passage.** Fulfillment strategies ; Fulfillment optimization in order orchestration flows

**Limite de preuve.** Page primaire ouverte ; comparaison du résultat, aucune identité de capacités ou garantie d’optimum global.

Références : U377, ELM228, CMP139, U378.

### Microsoft — Fulfillment and Returns Optimization provider

Dynamics 365 Intelligent Order Management · Service produit · Appui fonctionnel · statut : proposed

**Points communs.** Détermine les sources de satisfaction selon objectifs et configuration métier.

**Différences.** Service logiciel intégré ; absence de preuve d’une correspondance niveau par niveau au modèle FLOW.

**Position FLOW.** U378 intègre Fulfillment Plan Decision : scénario de plan issu de décisions spécialisées. Fulfillment plan est un résultat Microsoft ; le suffixe Decision et le découpage restent propres à FLOW. Correspondance proposée.

[Fulfillment and Returns Optimization provider overview](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/fulfillment-returns-optimization) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction

**Limite de preuve.** Page primaire ouverte.

Références : U377, U378.

## Comparaison par rapport au marché — D05.i Return Disposition Decision

### Microsoft — Disposition codes and disposition actions

Dynamics 365 Supply Chain Management · Configuration et traitement de retour produit · Recouvrement partiel · statut : proposed

**Points communs.** Distingue le motif du retour de ce qui doit arriver au bien ; les codes déterminent des suites logistiques.

**Différences.** Les actions produit peuvent aussi déclencher des effets financiers. Elles ne sont ni des capacités FLOW ni automatiquement des comportements.

**Position FLOW.** U380 intègre la décision de devenir logistique dans D05, distincte de l’inspection, des Orders, de l’exécution et des suites financières. Correspondance proposée ; les codes et activités produit ne sont pas des comportements FLOW.

[Specify how to dispose of returned items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Disposition code and disposition action

**Limite de preuve.** Page primaire ouverte ; aucune couverture installée déduite.

Références : U379, ELM229, CMP140, U380.

### SAP — Logistical Follow-Up Activities

S/4HANA Cloud Public Edition · Suites logistiques de processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Après inspection, orientation vers stock disponible, stock spécifié, fournisseur, réparation ou rebut selon le cas.

**Différences.** Catalogue d’activités incluant documents et mouvements ; ne prouve ni une capacité autonome au même nom ni un rattachement à D05.

**Position FLOW.** U380 intègre la décision de devenir logistique dans D05, distincte de l’inspection, des Orders, de l’exécution et des suites financières. Correspondance proposée ; les codes et activités produit ne sont pas des comportements FLOW.

[Logistical Follow-Up Activities](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/aad8417242c84d70a64b2742fe818c90.html) — Documentation Cloud évolutive ; édition précise du passage non établie, consulté le 2026-09-18.

**Passage.** Table of logistical follow-up activities

**Limite de preuve.** Passages primaires indexés consultés ; portail partiellement inaccessible en lecture directe.

Références : U379, ELM229, CMP140, U380.

### Microsoft — Disposition codes and actions

Dynamics 365 Supply Chain Management · Configuration ou mécanisme produit ; pas un catalogue de capacités · Recouvrement partiel · statut : proposed

**Points communs.** Les codes de disposition représentent différentes suites du retour, dont réparation, renvoi fournisseur et revente.

**Différences.** La documentation de configuration ne prouve pas un moteur de sélection automatique par état. Les actions mêlent effets physiques et financiers.

**Position FLOW.** Appui au vocabulaire et à la prise en charge ; le mécanisme Policy-based Disposition reste une interprétation FLOW.

[Specify how to dispose of returned items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items) — Mise à jour affichée 2025-05-07, consulté le 2026-09-18.

**Passage.** Disposition type, common code et disposition action

**Limite de preuve.** Page primaire consultée ; correspondance proposée, sans équivalence exacte de nom ou niveau ni preuve de réalisation Beaumanoir.

Références : U382, U383, ELM230, ELM231, CMP141, CMP142.

### Blue Yonder — Rules and optimized return disposition

Returns Management / Smart Disposition · Configuration ou mécanisme produit ; pas un catalogue de capacités · Recouvrement partiel · statut : proposed

**Points communs.** Choix de canal et destination selon règles et contexte, récupération de valeur et coûts.

**Différences.** Produit plus large incluant admission et remboursement ; page commerciale sans détail algorithmique ni preuve de déploiement Beaumanoir.

**Position FLOW.** Appui aux deux mécanismes proposés ; conserver uniquement le choix du devenir logistique dans D05.i.

[Smart Disposition](https://blueyonder.com/solutions/returns-management/smart-disposition) — Page produit évolutive, sans édition affichée, consulté le 2026-09-18.

**Passage.** Intelligent routing ; Customizable reason codes and rules ; Key Benefits

**Limite de preuve.** Page primaire consultée ; correspondance proposée, sans équivalence exacte de nom ou niveau ni preuve de réalisation Beaumanoir.

Références : U382, U383, ELM230, ELM231, CMP141, CMP142.

### Manhattan — Dynamic return location

Active Order Management / Returns Management · Configuration ou mécanisme produit ; pas un catalogue de capacités · Recouvrement partiel · statut : proposed

**Points communs.** Détermination dynamique du lieu de retour pour accélérer la remise en vente.

**Différences.** Ne démontre pas à elle seule la sélection de toutes les filières de réparation ou de disposition.

**Position FLOW.** Le contexte réseau nourrit la stratégie ; frontière à maintenir avec redistribution et exécution.

[Returns Management](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/returns-management) — Page produit évolutive, sans édition affichée, consulté le 2026-09-18.

**Passage.** Returns Done Right ; Maximize Returns Profitability

**Limite de preuve.** Page primaire consultée ; correspondance proposée, sans équivalence exacte de nom ou niveau ni preuve de réalisation Beaumanoir.

Références : U382, U383, ELM230, ELM231, CMP141, CMP142.

## Comparaison par rapport au marché — BHV048 Policy-based Disposition

### Microsoft — Disposition codes and actions

Dynamics 365 Supply Chain Management · Configuration ou mécanisme produit ; pas un catalogue de capacités · Recouvrement partiel · statut : proposed

**Points communs.** Les codes de disposition représentent différentes suites du retour, dont réparation, renvoi fournisseur et revente.

**Différences.** La documentation de configuration ne prouve pas un moteur de sélection automatique par état. Les actions mêlent effets physiques et financiers.

**Position FLOW.** Appui au vocabulaire et à la prise en charge ; le mécanisme Policy-based Disposition reste une interprétation FLOW.

[Specify how to dispose of returned items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items) — Mise à jour affichée 2025-05-07, consulté le 2026-09-18.

**Passage.** Disposition type, common code et disposition action

**Limite de preuve.** Page primaire consultée ; correspondance proposée, sans équivalence exacte de nom ou niveau ni preuve de réalisation Beaumanoir.

Références : U382, U383, ELM230, ELM231, CMP141, CMP142.

### Blue Yonder — Rules and optimized return disposition

Returns Management / Smart Disposition · Configuration ou mécanisme produit ; pas un catalogue de capacités · Recouvrement partiel · statut : proposed

**Points communs.** Choix de canal et destination selon règles et contexte, récupération de valeur et coûts.

**Différences.** Produit plus large incluant admission et remboursement ; page commerciale sans détail algorithmique ni preuve de déploiement Beaumanoir.

**Position FLOW.** Appui aux deux mécanismes proposés ; conserver uniquement le choix du devenir logistique dans D05.i.

[Smart Disposition](https://blueyonder.com/solutions/returns-management/smart-disposition) — Page produit évolutive, sans édition affichée, consulté le 2026-09-18.

**Passage.** Intelligent routing ; Customizable reason codes and rules ; Key Benefits

**Limite de preuve.** Page primaire consultée ; correspondance proposée, sans équivalence exacte de nom ou niveau ni preuve de réalisation Beaumanoir.

Références : U382, U383, ELM230, ELM231, CMP141, CMP142.

## Comparaison par rapport au marché — BHV049 Value Recovery Optimization

### Blue Yonder — Rules and optimized return disposition

Returns Management / Smart Disposition · Configuration ou mécanisme produit ; pas un catalogue de capacités · Recouvrement partiel · statut : proposed

**Points communs.** Choix de canal et destination selon règles et contexte, récupération de valeur et coûts.

**Différences.** Produit plus large incluant admission et remboursement ; page commerciale sans détail algorithmique ni preuve de déploiement Beaumanoir.

**Position FLOW.** Appui aux deux mécanismes proposés ; conserver uniquement le choix du devenir logistique dans D05.i.

[Smart Disposition](https://blueyonder.com/solutions/returns-management/smart-disposition) — Page produit évolutive, sans édition affichée, consulté le 2026-09-18.

**Passage.** Intelligent routing ; Customizable reason codes and rules ; Key Benefits

**Limite de preuve.** Page primaire consultée ; correspondance proposée, sans équivalence exacte de nom ou niveau ni preuve de réalisation Beaumanoir.

Références : U382, U383, ELM230, ELM231, CMP141, CMP142.

### Manhattan — Dynamic return location

Active Order Management / Returns Management · Configuration ou mécanisme produit ; pas un catalogue de capacités · Recouvrement partiel · statut : proposed

**Points communs.** Détermination dynamique du lieu de retour pour accélérer la remise en vente.

**Différences.** Ne démontre pas à elle seule la sélection de toutes les filières de réparation ou de disposition.

**Position FLOW.** Le contexte réseau nourrit la stratégie ; frontière à maintenir avec redistribution et exécution.

[Returns Management](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/returns-management) — Page produit évolutive, sans édition affichée, consulté le 2026-09-18.

**Passage.** Returns Done Right ; Maximize Returns Profitability

**Limite de preuve.** Page primaire consultée ; correspondance proposée, sans équivalence exacte de nom ou niveau ni preuve de réalisation Beaumanoir.

Références : U382, U383, ELM230, ELM231, CMP141, CMP142.

## Comparaison par rapport au marché — BHV050 Return to Stock

### SAP — SAP Transfer to Free Available Stock

S/4HANA Cloud — Warehouse Management · Suites de processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Appui au parcours Return to Stock : SAP Transfer to Free Available Stock.

**Différences.** Documents, mouvements et étapes de processus ne sont pas automatiquement des capacités ou comportements FLOW ; absence d’équivalence de niveau.

**Position FLOW.** D05.i retient l’orientation ; D06 organise les prestations et D01 enregistre état et disponibilité. Aucun stock réputé disponible par simple clôture de l’Order. Parcours adopté U385 ; correspondance proposée, pas une équivalence de niveau.

[Logistical Follow-Up Activities](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/aeb252c114df4dac9abf1626ccb04233.html) — 2602 affiché par le passage primaire indexé, consulté le 2026-09-18.

**Passage.** Table : 0011, 0012, 0005, 0021 et 0026

**Limite de preuve.** Texte primaire indexé consulté ; portail direct partiellement inaccessible. Aucune réalisation Beaumanoir déduite.

Références : U384, ELM232, CMP143, U385.

### Microsoft — Microsoft Credit (volet logistique uniquement)

Dynamics 365 Supply Chain Management · Configuration et actions de traitement produit · Recouvrement partiel · statut : proposed

**Points communs.** Appui au parcours Return to Stock : Microsoft Credit (volet logistique uniquement).

**Différences.** Les six actions prédéfinies combinent effets logistiques et financiers ; un code libre ne prouve pas un processus natif complet de réparation.

**Position FLOW.** D05.i retient l’orientation ; D06 organise les prestations et D01 enregistre état et disponibilité. Aucun stock réputé disponible par simple clôture de l’Order. Parcours adopté U385 ; correspondance proposée, pas une équivalence de niveau.

[Specify how to dispose of returned items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items) — Mise à jour affichée 2025-05-07, consulté le 2026-09-18.

**Passage.** Disposition types/codes ; six disposition actions

**Limite de preuve.** Page primaire ouverte ; fonctionnalités produit, sans preuve de couverture Beaumanoir.

Références : U384, ELM232, CMP143, U385.

## Comparaison par rapport au marché — BHV051 Repair and Refurbishment

### SAP — SAP In-House Repair (Service)

S/4HANA Cloud — Warehouse Management · Suites de processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Appui au parcours Repair and Refurbishment : SAP In-House Repair (Service).

**Différences.** Documents, mouvements et étapes de processus ne sont pas automatiquement des capacités ou comportements FLOW ; absence d’équivalence de niveau.

**Position FLOW.** La réalisation de la réparation reste chez l’exécutant et son orchestration dans D06. Le coût acceptable et le choix du devenir sont dans D05.i. Aucun atelier interne imposé. Parcours adopté U385 ; correspondance proposée, pas une équivalence de niveau.

[Logistical Follow-Up Activities](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/aeb252c114df4dac9abf1626ccb04233.html) — 2602 affiché par le passage primaire indexé, consulté le 2026-09-18.

**Passage.** Table : 0011, 0012, 0005, 0021 et 0026

**Limite de preuve.** Texte primaire indexé consulté ; portail direct partiellement inaccessible. Aucune réalisation Beaumanoir déduite.

Références : U384, ELM232, CMP143, U385.

### Microsoft — Microsoft Repair / Remanufacture-Refurbish (codes)

Dynamics 365 Supply Chain Management · Configuration et actions de traitement produit · Recouvrement partiel · statut : proposed

**Points communs.** Appui au parcours Repair and Refurbishment : Microsoft Repair / Remanufacture-Refurbish (codes).

**Différences.** Les six actions prédéfinies combinent effets logistiques et financiers ; un code libre ne prouve pas un processus natif complet de réparation.

**Position FLOW.** La réalisation de la réparation reste chez l’exécutant et son orchestration dans D06. Le coût acceptable et le choix du devenir sont dans D05.i. Aucun atelier interne imposé. Parcours adopté U385 ; correspondance proposée, pas une équivalence de niveau.

[Specify how to dispose of returned items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items) — Mise à jour affichée 2025-05-07, consulté le 2026-09-18.

**Passage.** Disposition types/codes ; six disposition actions

**Limite de preuve.** Page primaire ouverte ; fonctionnalités produit, sans preuve de couverture Beaumanoir.

Références : U384, ELM232, CMP143, U385.

## Comparaison par rapport au marché — BHV052 Return to Supplier

### SAP — SAP Ship to Supplier

S/4HANA Cloud — Warehouse Management · Suites de processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Appui au parcours Return to Supplier : SAP Ship to Supplier.

**Différences.** Documents, mouvements et étapes de processus ne sont pas automatiquement des capacités ou comportements FLOW ; absence d’équivalence de niveau.

**Position FLOW.** Supplier Return D04.m porte la commande fournisseur ; ce comportement porte son articulation avec le retour client. L’accord de reprise est une condition, jamais déduit du choix logistique. Parcours adopté U385 ; correspondance proposée, pas une équivalence de niveau.

[Logistical Follow-Up Activities](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/aeb252c114df4dac9abf1626ccb04233.html) — 2602 affiché par le passage primaire indexé, consulté le 2026-09-18.

**Passage.** Table : 0011, 0012, 0005, 0021 et 0026

**Limite de preuve.** Texte primaire indexé consulté ; portail direct partiellement inaccessible. Aucune réalisation Beaumanoir déduite.

Références : U384, ELM232, CMP143, U385.

### Microsoft — Microsoft Return to Vendor (code)

Dynamics 365 Supply Chain Management · Configuration et actions de traitement produit · Recouvrement partiel · statut : proposed

**Points communs.** Appui au parcours Return to Supplier : Microsoft Return to Vendor (code).

**Différences.** Les six actions prédéfinies combinent effets logistiques et financiers ; un code libre ne prouve pas un processus natif complet de réparation.

**Position FLOW.** Supplier Return D04.m porte la commande fournisseur ; ce comportement porte son articulation avec le retour client. L’accord de reprise est une condition, jamais déduit du choix logistique. Parcours adopté U385 ; correspondance proposée, pas une équivalence de niveau.

[Specify how to dispose of returned items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items) — Mise à jour affichée 2025-05-07, consulté le 2026-09-18.

**Passage.** Disposition types/codes ; six disposition actions

**Limite de preuve.** Page primaire ouverte ; fonctionnalités produit, sans preuve de couverture Beaumanoir.

Références : U384, ELM232, CMP143, U385.

## Comparaison par rapport au marché — BHV053 Return to Customer

### SAP — SAP Send Back to Customer

S/4HANA Cloud — Warehouse Management · Suites de processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Appui au parcours Return to Customer : SAP Send Back to Customer.

**Différences.** Documents, mouvements et étapes de processus ne sont pas automatiquement des capacités ou comportements FLOW ; absence d’équivalence de niveau.

**Position FLOW.** Ne décide pas du refus commercial. Ne crée pas implicitement une nouvelle vente, ne remplace pas la réservation/promesse d’un article de remplacement. D06 suit l’acheminement. Parcours adopté U385 ; correspondance proposée, pas une équivalence de niveau.

[Logistical Follow-Up Activities](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/aeb252c114df4dac9abf1626ccb04233.html) — 2602 affiché par le passage primaire indexé, consulté le 2026-09-18.

**Passage.** Table : 0011, 0012, 0005, 0021 et 0026

**Limite de preuve.** Texte primaire indexé consulté ; portail direct partiellement inaccessible. Aucune réalisation Beaumanoir déduite.

Références : U384, ELM232, CMP143, U385.

### Microsoft — Microsoft Return to customer

Dynamics 365 Supply Chain Management · Configuration et actions de traitement produit · Recouvrement partiel · statut : proposed

**Points communs.** Appui au parcours Return to Customer : Microsoft Return to customer.

**Différences.** Les six actions prédéfinies combinent effets logistiques et financiers ; un code libre ne prouve pas un processus natif complet de réparation.

**Position FLOW.** Ne décide pas du refus commercial. Ne crée pas implicitement une nouvelle vente, ne remplace pas la réservation/promesse d’un article de remplacement. D06 suit l’acheminement. Parcours adopté U385 ; correspondance proposée, pas une équivalence de niveau.

[Specify how to dispose of returned items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items) — Mise à jour affichée 2025-05-07, consulté le 2026-09-18.

**Passage.** Disposition types/codes ; six disposition actions

**Limite de preuve.** Page primaire ouverte ; fonctionnalités produit, sans preuve de couverture Beaumanoir.

Références : U384, ELM232, CMP143, U385.

## Comparaison par rapport au marché — BHV054 Scrapping

### SAP — SAP Transfer to Scrap

S/4HANA Cloud — Warehouse Management · Suites de processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Appui au parcours Scrapping : SAP Transfer to Scrap.

**Différences.** Documents, mouvements et étapes de processus ne sont pas automatiquement des capacités ou comportements FLOW ; absence d’équivalence de niveau.

**Position FLOW.** D05.i décide du devenir, l’exécutant réalise, D06 trace et D01 enregistre. Ne regroupe pas donation, recyclage et revente secondaire sous le même résultat. Parcours adopté U385 ; correspondance proposée, pas une équivalence de niveau.

[Logistical Follow-Up Activities](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/aeb252c114df4dac9abf1626ccb04233.html) — 2602 affiché par le passage primaire indexé, consulté le 2026-09-18.

**Passage.** Table : 0011, 0012, 0005, 0021 et 0026

**Limite de preuve.** Texte primaire indexé consulté ; portail direct partiellement inaccessible. Aucune réalisation Beaumanoir déduite.

Références : U384, ELM232, CMP143, U385.

### Microsoft — Microsoft Scrap

Dynamics 365 Supply Chain Management · Configuration et actions de traitement produit · Recouvrement partiel · statut : proposed

**Points communs.** Appui au parcours Scrapping : Microsoft Scrap.

**Différences.** Les six actions prédéfinies combinent effets logistiques et financiers ; un code libre ne prouve pas un processus natif complet de réparation.

**Position FLOW.** D05.i décide du devenir, l’exécutant réalise, D06 trace et D01 enregistre. Ne regroupe pas donation, recyclage et revente secondaire sous le même résultat. Parcours adopté U385 ; correspondance proposée, pas une équivalence de niveau.

[Specify how to dispose of returned items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items) — Mise à jour affichée 2025-05-07, consulté le 2026-09-18.

**Passage.** Disposition types/codes ; six disposition actions

**Limite de preuve.** Page primaire ouverte ; fonctionnalités produit, sans preuve de couverture Beaumanoir.

Références : U384, ELM232, CMP143, U385.

## Comparaison par rapport au marché — BHV055 Return for Credit

### Microsoft — Purchase return order / replacement purchase order

Dynamics 365 Business Central · Processus et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Le retour peut être associé à un avoir ; un remplacement peut générer une commande d’achat distincte.

**Différences.** Fonctions produit mêlant logistique et comptabilité ; ne pas attribuer cette documentation Business Central à Dynamics 365 SCM. La nouvelle commande est un choix produit, pas une obligation FLOW.

**Position FLOW.** Accord de reprise consommé, non négocié ici ; finance émet, comptabilise et rapproche l’avoir. Retour expédié, accepté et financièrement réglé restent distincts. Ne pas confondre avec Credit only côté client, qui peut ne comporter aucun retour physique. Correspondance proposée, distincte de la validation du comportement FLOW.

[Purchase return order / replacement purchase order](https://learn.microsoft.com/en-us/dynamics365/business-central/purchasing-how-process-purchase-returns-cancellations) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Create a replacement purchase order from a purchase return order ; introduction

**Limite de preuve.** Page primaire ouverte. Aucune réalisation Beaumanoir déduite.

Références : U386, ELM233, CMP144, U387.

### SAP — Create a New Return to Supplier

Business ByDesign · Processus et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Suites : avoir, remplacement ou combinaison partielle. Le remplacement modifie le reste à livrer de l’achat ; la seule émission d’un avoir ne crée pas ce même attendu.

**Différences.** Documentation ByDesign, pas S/4HANA. Restrictions particulières au scénario tiers ; séparation de vues acheteur/logistique non imposée à l’organisation FLOW.

**Position FLOW.** Accord de reprise consommé, non négocié ici ; finance émet, comptabilise et rapproche l’avoir. Retour expédié, accepté et financièrement réglé restent distincts. Ne pas confondre avec Credit only côté client, qui peut ne comporter aucun retour physique. Correspondance proposée, distincte de la validation du comportement FLOW.

[Create a New Return to Supplier](https://help.sap.com/docs/SAP_BUSINESS_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2d9b97f7722d1014a974a1fa1d11fd10.html) — May 2026 affiché dans le passage primaire indexé, consulté le 2026-09-18.

**Passage.** Overview ; Create a Return to Supplier in Purchasing

**Limite de preuve.** Texte primaire indexé effectivement consulté ; ouverture directe sans contenu exploitable. Aucune réalisation Beaumanoir déduite.

Références : U386, ELM233, CMP144, U387.

### Oracle — Return to Supplier for Credit Only

Fusion Cloud SCM — Receiving · Processus et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Retour pour avoir sans remplacement attendu : conserver la commande d’achat fermée aux réceptions futures, plutôt que la rouvrir.

**Différences.** Effet produit sur une commande existante ; FLOW retient la différence d’attendu Supply sans imposer cette mécanique de statut ou absorber la comptabilité.

**Position FLOW.** Accord de reprise consommé, non négocié ici ; finance émet, comptabilise et rapproche l’avoir. Retour expédié, accepté et financièrement réglé restent distincts. Ne pas confondre avec Credit only côté client, qui peut ne comporter aucun retour physique. Correspondance proposée, distincte de la validation du comportement FLOW.

[Return to Supplier for Credit Only](https://docs.oracle.com/en/cloud/saas/readiness/scm/25a/inv25a/25A-inventory-wn-f35542.htm) — 25A, consulté le 2026-09-18.

**Passage.** Présentation de la fonctionnalité Return for credit

**Limite de preuve.** Page primaire ouverte. Aucune réalisation Beaumanoir déduite.

Références : U386, ELM233, CMP144, U387.

## Comparaison par rapport au marché — BHV056 Return for Replacement

### Microsoft — Purchase return order / replacement purchase order

Dynamics 365 Business Central · Processus et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Le retour peut être associé à un avoir ; un remplacement peut générer une commande d’achat distincte.

**Différences.** Fonctions produit mêlant logistique et comptabilité ; ne pas attribuer cette documentation Business Central à Dynamics 365 SCM. La nouvelle commande est un choix produit, pas une obligation FLOW.

**Position FLOW.** Purchase Order porte l’apport attendu ; le marché utilise selon le produit une nouvelle commande liée ou le rétablissement d’un attendu sur la commande initiale. Aucun choix documentaire imposé. La date convenue ne vaut pas réception, ni disponibilité opposable automatique pour ATP. Correspondance proposée, distincte de la validation du comportement FLOW.

[Purchase return order / replacement purchase order](https://learn.microsoft.com/en-us/dynamics365/business-central/purchasing-how-process-purchase-returns-cancellations) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Create a replacement purchase order from a purchase return order ; introduction

**Limite de preuve.** Page primaire ouverte. Aucune réalisation Beaumanoir déduite.

Références : U386, ELM233, CMP144, U387.

### SAP — Create a New Return to Supplier

Business ByDesign · Processus et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** Suites : avoir, remplacement ou combinaison partielle. Le remplacement modifie le reste à livrer de l’achat ; la seule émission d’un avoir ne crée pas ce même attendu.

**Différences.** Documentation ByDesign, pas S/4HANA. Restrictions particulières au scénario tiers ; séparation de vues acheteur/logistique non imposée à l’organisation FLOW.

**Position FLOW.** Purchase Order porte l’apport attendu ; le marché utilise selon le produit une nouvelle commande liée ou le rétablissement d’un attendu sur la commande initiale. Aucun choix documentaire imposé. La date convenue ne vaut pas réception, ni disponibilité opposable automatique pour ATP. Correspondance proposée, distincte de la validation du comportement FLOW.

[Create a New Return to Supplier](https://help.sap.com/docs/SAP_BUSINESS_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2d9b97f7722d1014a974a1fa1d11fd10.html) — May 2026 affiché dans le passage primaire indexé, consulté le 2026-09-18.

**Passage.** Overview ; Create a Return to Supplier in Purchasing

**Limite de preuve.** Texte primaire indexé effectivement consulté ; ouverture directe sans contenu exploitable. Aucune réalisation Beaumanoir déduite.

Références : U386, ELM233, CMP144, U387.

## Comparaison par rapport au marché — BHV057 Return for Repair

### Oracle — Repair at sourcing / Repair-Return

E-Business Suite — Service Parts Planning · Processus et fonctions produit · Recouvrement partiel · statut : proposed

**Points communs.** La réparation externe peut mobiliser un achat au réparateur et des documents de mouvement du bien.

**Différences.** Planification de pièces de service et réparation, pas preuve d’un comportement de retour fournisseur dans Oracle Fusion ou dans le retail FLOW.

**Position FLOW.** U388 place le suivi du renvoi et de la restitution sous Supplier Return. Achat de prestation et orchestration restent distincts ; rattachement FLOW, pas équivalence au catalogue Oracle.

[Repair at sourcing / Repair-Return](https://docs.oracle.com/cd/E18727-01/doc.121/e13338/T515331T515340.htm) — Release 12.1, référence historique, consulté le 2026-09-18.

**Passage.** Repair Program Influence on Service Supply Chain Lead Time Offset ; Assigning Sourcing Rule – Repair at

**Limite de preuve.** Page primaire ouverte le 18 septembre 2026 ; référence historique EBS 12.1, pas preuve de couverture Fusion ou Beaumanoir. Le passage ne démontre pas une traçabilité sérialisée identique à notre exigence.

Références : U386, U388, ELM233, CMP144.

## Comparaison par rapport au marché — BHV058 Stock Procurement

### Microsoft — Create purchase orders

Dynamics 365 SCM · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Les commandes peuvent porter des produits physiques ou des services ; destination, quantités et dates sont précisées.

**Différences.** Types de lignes produit, pas une taxonomie de comportements.

**Position FLOW.** D05/D03 déterminent les besoins ou réponses ; D06 suit les prestations et D01 enregistre le stock. Aucun comportement distinct par type de site. Correspondance proposée, distincte de l’accord sur le comportement FLOW.

[Create purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-creation) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Adding purchase order lines

**Limite de preuve.** Page primaire ouverte ; aucune preuve de réalisation Beaumanoir.

Références : U390, U391, ELM235, CMP146.

## Comparaison par rapport au marché — BHV059 Direct Delivery

### Microsoft — Direct deliveries

Dynamics 365 SCM · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Livraison fournisseur au client et liens entre lignes achat/vente ; coordination des dates et destinations sans passage physique dans l’entrepôt du vendeur.

**Différences.** FLOW ne reprend pas automatiquement les règles de propagation des dates ni les écritures du produit.

**Position FLOW.** Livrer un magasin de notre réseau relève du premier parcours lorsque l’objectif est son stock. La décision de sourcing, la promesse et l’orchestration restent distinctes ; pas de propagation automatique implicite. Correspondance proposée, distincte de l’accord sur le comportement FLOW.

[Direct deliveries](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/direct-deliveries) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction, Delivery date, Delivery address, Warehouse

**Limite de preuve.** Page primaire ouverte ; aucune preuve de réalisation Beaumanoir.

Références : U390, U391, ELM235, CMP146.

## Comparaison par rapport au marché — BHV060 Service Procurement

### Microsoft — Create purchase orders

Dynamics 365 SCM · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Les commandes peuvent porter des produits physiques ou des services ; destination, quantités et dates sont précisées.

**Différences.** Types de lignes produit, pas une taxonomie de comportements.

**Position FLOW.** D04 porte l’achat ; D06 sollicite, orchestre et suit les services via les Service Orders. Pas de Purchase Order imposée pour chaque appel de service ; comptabilité et négociation contractuelle hors périmètre. Extension explicite de la définition actuelle centrée sur les biens. Correspondance proposée, distincte de l’accord sur le comportement FLOW.

[Create purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-creation) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Adding purchase order lines

**Limite de preuve.** Page primaire ouverte ; aucune preuve de réalisation Beaumanoir.

Références : U390, U391, ELM235, CMP146.

### SAP — Manage Service Entry Sheets - Lean Services / Planned and Unplanned Services

S/4HANA on-premise · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Les prestations exécutées sont constatées par référence à une commande d’achat ; services planifiés et non planifiés.

**Différences.** Application et documents SAP, pas une nouvelle capacité d’exécution FLOW ; aucune feuille de saisie imposée.

**Position FLOW.** D04 porte l’achat ; D06 sollicite, orchestre et suit les services via les Service Orders. Pas de Purchase Order imposée pour chaque appel de service ; comptabilité et négociation contractuelle hors périmètre. Extension explicite de la définition actuelle centrée sur les biens. Correspondance proposée, distincte de l’accord sur le comportement FLOW.

[Manage Service Entry Sheets - Lean Services / Planned and Unplanned Services](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/4ac8acf820ad41a8a5841420085ba68d.html) — 2025 FPS01 (Feb 2026) affichée sur la page associée Planned and Unplanned Services, consulté le 2026-09-18.

**Passage.** Introduction et Create or change a service entry sheet with reference to a purchase order

**Limite de preuve.** Passages primaires indexés lus ; ouverture directe du portail sans texte exploitable ; aucune preuve de réalisation Beaumanoir.

Références : U390, U391, ELM235, CMP146.

## Comparaison par rapport au marché — D04.r Consignment Replenishment Order

### Microsoft — Set up consignment

Dynamics 365 SCM · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Consignment replenishment order demande et suit les quantités à livrer dans un intervalle de dates ; le fournisseur conserve la propriété à réception. Le traitement de changement de propriété génère ensuite un Purchase Order.

**Différences.** Document produit illustré en production ; ne justifie pas une capacité Procurement Order générique couvrant tous les apports.

**Position FLOW.** U395 adopte la responsabilité FLOW et son parent ; le rapprochement produit/capacité reste partiel. Les conditions contractuelles FLOW et les comportements ne sont pas déduits automatiquement du produit.

[Set up consignment](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Consignment replenishment orders ; Overview of the consignment process

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U391, U392, U393, U394, U395, ELM236, ELM237, CMP147, CMP148, CMP149.

### SAP — Item Category

S/4HANA on-premise · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Une ligne de Purchase Order de catégorie Consignment exige une réception de marchandises mais pas une réception de facture sur cette ligne.

**Différences.** Le nom de l’objet ERP ne prouve pas un achat/transfert de propriété à sa création ; catégorie de ligne, pas nouvelle capacité. Aucun comportement légal universel déduit.

**Position FLOW.** U395 adopte la responsabilité FLOW et son parent ; le rapprochement produit/capacité reste partiel. Les conditions contractuelles FLOW et les comportements ne sont pas déduits automatiquement du produit.

[Item Category](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/a37eb65334e6b54ce10000000a174cb4.html) — Documentation évolutive, édition non confirmée dans le passage lu, consulté le 2026-09-18.

**Passage.** Table des catégories : Consignment

**Limite de preuve.** Passage primaire indexé consulté ; ouverture directe sans texte exploitable ; aucune preuve de déploiement Beaumanoir.

Références : U391, U392, U393, U394, U395, ELM236, ELM237, CMP147, CMP148, CMP149.

### Oracle — Consigned Inventory

Fusion Cloud SCM · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Consignment Order demande les expéditions avec quantités, lieux et dates selon l’accord ; les biens reçus restent propriété fournisseur.

**Différences.** Intitulé fonctionnel du parcours ; ne démontre pas un nouvel objet technique indépendant du Purchase Order.

**Position FLOW.** U395 adopte la responsabilité FLOW et son parent ; le rapprochement produit/capacité reste partiel. Les conditions contractuelles FLOW et les comportements ne sont pas déduits automatiquement du produit.

[Consigned Inventory](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faims/consigned-inventory.html) — 25D, consulté le 2026-09-18.

**Passage.** Consignment Order ; Ship and Receive Items

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U391, U392, U393, U394, U395, ELM236, ELM237, CMP147, CMP148, CMP149.

## Comparaison par rapport au marché — D01.h Consigned Inventory Management

### Microsoft — Set up consignment

Dynamics 365 SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Apport distinct de l’acquisition ; propriété fournisseur puis changement de propriété avant consommation dans l’exemple de production.

**Différences.** Ne prescrit pas le fait générateur contractuel retail ni une vente automatique à chaque mouvement.

**Position FLOW.** Microsoft et Oracle documentent acquisition à consommation, échéance et retours. Les sorties vers soldeur, seconde main ou destruction sont le besoin FLOW U391 ; couverture globale de ces issues non établie. Consignment Exit est un libellé de synthèse FLOW, plus large que les retours documentés.

[Set up consignment](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Overview ; Inventory ownership change journal

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Oracle — Consigned Inventory Aging

Fusion Cloud SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Une durée convenue peut déclencher l’acquisition ; transaction Transfer to Owned, acquisition usuelle par utilisation ou expiration de durée.

**Différences.** Condition d’accord, pas loi générale de consignation ; la documentation décrit une opération manuelle et ne prouve pas une automatisation imposée.

**Position FLOW.** Microsoft et Oracle documentent acquisition à consommation, échéance et retours. Les sorties vers soldeur, seconde main ou destruction sont le besoin FLOW U391 ; couverture globale de ces issues non établie. Consignment Exit est un libellé de synthèse FLOW, plus large que les retours documentés.

[Consigned Inventory Aging](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/famml/consigned-inventory-aging.html) — 26A, consulté le 2026-09-18.

**Passage.** Aging Process ; Aging Period ; Transfer to Owned

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Oracle — Examples of Consigned Inventory Returns

Fusion Cloud SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Retour fournisseur distingué selon propriété et communication de consommation ; un retour de stock encore consigné ne génère pas nécessairement d’avoir.

**Différences.** Ne couvre pas les filières soldeur, seconde main ou destruction ; aucun droit de disposition universel.

**Position FLOW.** Microsoft et Oracle documentent acquisition à consommation, échéance et retours. Les sorties vers soldeur, seconde main ou destruction sont le besoin FLOW U391 ; couverture globale de ces issues non établie. Consignment Exit est un libellé de synthèse FLOW, plus large que les retours documentés.

[Examples of Consigned Inventory Returns](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/famml/examples-of-consigned-inventory-returns.html) — 25D, consulté le 2026-09-18.

**Passage.** Material received and put away ; Material consumed

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV061 Initial Stocking

### Microsoft — Set up consignment

Dynamics 365 SCM · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Consignment replenishment order demande et suit les quantités à livrer dans un intervalle de dates ; le fournisseur conserve la propriété à réception. Le traitement de changement de propriété génère ensuite un Purchase Order.

**Différences.** Document produit illustré en production ; ne justifie pas une capacité Procurement Order générique couvrant tous les apports.

**Position FLOW.** U398 adopte ce comportement pour expliciter l’intention métier FLOW. La source Microsoft décrit la demande d’apport ; elle ne prescrit pas ce découpage en deux comportements.

[Set up consignment](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Consignment replenishment orders ; Overview of the consignment process

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U397, U398, CMP148, CMP150.

## Comparaison par rapport au marché — BHV062 Continuous Replenishment

### Microsoft — Set up consignment

Dynamics 365 SCM · Processus, document ou fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Consignment replenishment order demande et suit les quantités à livrer dans un intervalle de dates ; le fournisseur conserve la propriété à réception. Le traitement de changement de propriété génère ensuite un Purchase Order.

**Différences.** Document produit illustré en production ; ne justifie pas une capacité Procurement Order générique couvrant tous les apports.

**Position FLOW.** U398 adopte ce comportement pour expliciter l’intention métier FLOW. La source Microsoft décrit la demande d’apport ; elle ne prescrit pas ce découpage en deux comportements.

[Set up consignment](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Consignment replenishment orders ; Overview of the consignment process

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U397, U398, CMP148, CMP150.

## Comparaison par rapport au marché — BHV063 Consumption-Based Ownership Transfer

### Microsoft — Set up consignment

Dynamics 365 SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Apport distinct de l’acquisition ; propriété fournisseur puis changement de propriété avant consommation dans l’exemple de production.

**Différences.** Ne prescrit pas le fait générateur contractuel retail ni une vente automatique à chaque mouvement.

**Position FLOW.** U401 adopte ce comportement sous Consigned Inventory Management. Microsoft et Oracle documentent acquisition à consommation, échéance et retours. Les sorties vers soldeur, seconde main ou destruction sont le besoin FLOW U391 ; couverture globale de ces issues non établie. Consignment Exit est un libellé de synthèse FLOW, plus large que les retours documentés.

[Set up consignment](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Overview ; Inventory ownership change journal

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Oracle — Consigned Inventory Aging

Fusion Cloud SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Une durée convenue peut déclencher l’acquisition ; transaction Transfer to Owned, acquisition usuelle par utilisation ou expiration de durée.

**Différences.** Condition d’accord, pas loi générale de consignation ; la documentation décrit une opération manuelle et ne prouve pas une automatisation imposée.

**Position FLOW.** U401 adopte ce comportement sous Consigned Inventory Management. Microsoft et Oracle documentent acquisition à consommation, échéance et retours. Les sorties vers soldeur, seconde main ou destruction sont le besoin FLOW U391 ; couverture globale de ces issues non établie. Consignment Exit est un libellé de synthèse FLOW, plus large que les retours documentés.

[Consigned Inventory Aging](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/famml/consigned-inventory-aging.html) — 26A, consulté le 2026-09-18.

**Passage.** Aging Process ; Aging Period ; Transfer to Owned

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV064 Aging-Based Ownership Transfer

### Oracle — Consigned Inventory Aging

Fusion Cloud SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Une durée convenue peut déclencher l’acquisition ; transaction Transfer to Owned, acquisition usuelle par utilisation ou expiration de durée.

**Différences.** Condition d’accord, pas loi générale de consignation ; la documentation décrit une opération manuelle et ne prouve pas une automatisation imposée.

**Position FLOW.** U401 adopte ce comportement sous Consigned Inventory Management. Microsoft et Oracle documentent acquisition à consommation, échéance et retours. Les sorties vers soldeur, seconde main ou destruction sont le besoin FLOW U391 ; couverture globale de ces issues non établie. Consignment Exit est un libellé de synthèse FLOW, plus large que les retours documentés.

[Consigned Inventory Aging](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/famml/consigned-inventory-aging.html) — 26A, consulté le 2026-09-18.

**Passage.** Aging Process ; Aging Period ; Transfer to Owned

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV065 Consignment Exit

### Oracle — Examples of Consigned Inventory Returns

Fusion Cloud SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Retour fournisseur distingué selon propriété et communication de consommation ; un retour de stock encore consigné ne génère pas nécessairement d’avoir.

**Différences.** Ne couvre pas les filières soldeur, seconde main ou destruction ; aucun droit de disposition universel.

**Position FLOW.** U401 adopte ce comportement sous Consigned Inventory Management. Microsoft et Oracle documentent acquisition à consommation, échéance et retours. Les sorties vers soldeur, seconde main ou destruction sont le besoin FLOW U391 ; couverture globale de ces issues non établie. Consignment Exit est un libellé de synthèse FLOW, plus large que les retours documentés.

[Examples of Consigned Inventory Returns](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/famml/examples-of-consigned-inventory-returns.html) — 25D, consulté le 2026-09-18.

**Passage.** Material received and put away ; Material consumed

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV066 Ship to Customer

### Microsoft — Customer orders in point of sale (POS)

Dynamics 365 Commerce · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Commandes livrées à une adresse et commandes retirées au lieu/date convenus ; choix entre magasins et entrepôts admissibles.

**Différences.** Source Commerce/POS, pas preuve de couverture universelle de toutes les ventes B2B ; ne transfère pas l’exécution physique à Sales Order.

**Position FLOW.** U401 adopte ce comportement sous Sales Order. Shipping/Pickup et Direct delivery sont documentés par Microsoft ; Intercompany constitue une dimension de relation commerciale combinable avec un parcours de livraison. Il ne s’agit pas de quatre catégories mutuellement exclusives.

[Customer orders in point of sale (POS)](https://learn.microsoft.com/en-us/dynamics365/commerce/customer-orders-overview) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Typical scenarios ; shipment or pickup

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV067 Customer Pickup

### Microsoft — Customer orders in point of sale (POS)

Dynamics 365 Commerce · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Commandes livrées à une adresse et commandes retirées au lieu/date convenus ; choix entre magasins et entrepôts admissibles.

**Différences.** Source Commerce/POS, pas preuve de couverture universelle de toutes les ventes B2B ; ne transfère pas l’exécution physique à Sales Order.

**Position FLOW.** U401 adopte ce comportement sous Sales Order. Shipping/Pickup et Direct delivery sont documentés par Microsoft ; Intercompany constitue une dimension de relation commerciale combinable avec un parcours de livraison. Il ne s’agit pas de quatre catégories mutuellement exclusives.

[Customer orders in point of sale (POS)](https://learn.microsoft.com/en-us/dynamics365/commerce/customer-orders-overview) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Typical scenarios ; shipment or pickup

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV068 Direct Delivery

### Microsoft — Direct deliveries

Dynamics 365 SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Fournisseur livre directement le client ; commande de vente reliée à l’achat.

**Différences.** Choix documentaire produit distinct des responsabilités FLOW ; ne prouve pas une disponibilité ni une promesse automatique.

**Position FLOW.** U401 adopte ce comportement sous Sales Order. Shipping/Pickup et Direct delivery sont documentés par Microsoft ; Intercompany constitue une dimension de relation commerciale combinable avec un parcours de livraison. Il ne s’agit pas de quatre catégories mutuellement exclusives.

[Direct deliveries](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/direct-deliveries) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction ; Delivery date ; order lines

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV069 Intercompany Sales

### Microsoft — Intercompany orders and return orders

Dynamics 365 SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Commandes de vente et achat liées entre entités juridiques.

**Différences.** Transaction commerciale intersociétés distincte d’un simple transfert entre lieux ; pas de schéma comptable prescrit pour FLOW.

**Position FLOW.** U401 adopte ce comportement sous Sales Order. Shipping/Pickup et Direct delivery sont documentés par Microsoft ; Intercompany constitue une dimension de relation commerciale combinable avec un parcours de livraison. Il ne s’agit pas de quatre catégories mutuellement exclusives.

[Intercompany orders and return orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/intercompany-orders-and-return-orders) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction ; intercompany sales and purchase orders

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV070 Initial Stocking

### SAP — Allocation Table with Reference to an OAPC-Based Purchase Order

ERP Retail · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Répartition d’achat initial et documents subséquents dont stock transport orders.

**Différences.** Appui partiel et historique pour implantation ; pas une décomposition native des capacités FLOW. Allocation reste un terme éditeur qualifié.

**Position FLOW.** U401 adopte ce comportement sous Transfer Order. Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Allocation Table with Reference to an OAPC-Based Purchase Order](https://help.sap.com/docs/SAP_ERP/75c4b203fca64320b998cc04e2eb1468/24e4c353b677b44ce10000000a174cb4.html?version=6.17.latest) — 6.17, documentation historique, consulté le 2026-09-18.

**Passage.** Fixed Initial Buy Allocation ; follow-on documents

**Limite de preuve.** Passage primaire indexé consulté ; ouverture du portail sans texte exploitable ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV071 Continuous Replenishment

### Microsoft — Set up warehouses for transfer orders

Dynamics 365 SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Besoins de destination alimentés par des transferts planifiés depuis un entrepôt source.

**Différences.** Décrit le réassort ; pas une taxonomie exhaustive de cinq comportements.

**Position FLOW.** U401 adopte ce comportement sous Transfer Order. Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Set up warehouses for transfer orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/transfer-orders-warehouse) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Warehouse levels ; Refilling ; Transport lead time

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Microsoft — Integrate Supply Chain Management transfer orders with Intelligent Order Management

Dynamics 365 Intelligent Order Management / SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Transferts pour réassort, pointe de demande, prestations et satisfaction de commandes ; visibilité des transferts entrants associés au produit de commande.

**Différences.** La page porte un avertissement preview ; appui sur le sens métier, pas recommandation de produit ni assertion de disponibilité générale.

**Position FLOW.** U401 adopte ce comportement sous Transfer Order. Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Integrate Supply Chain Management transfer orders with Intelligent Order Management](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/integrate-transfer-orders) — Documentation évolutive avec avertissement preview, consulté le 2026-09-18.

**Passage.** Typical reasons ; View transfer order products on sales order product page

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV072 Inventory Rebalancing

### Oracle — Overview of Inventory Rebalancing

Fusion Cloud Replenishment Planning · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Rééquilibrage excédents/manques et ordres planifiés ; transfert possible vers un lieu de regroupement.

**Différences.** Le produit combine décision et génération des ordres ; FLOW garde ces responsabilités séparées.

**Position FLOW.** U401 adopte ce comportement sous Transfer Order. Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Overview of Inventory Rebalancing](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html) — 26B, consulté le 2026-09-18.

**Passage.** Salient Features ; planned inbound and outbound orders

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Microsoft — Integrate Supply Chain Management transfer orders with Intelligent Order Management

Dynamics 365 Intelligent Order Management / SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Transferts pour réassort, pointe de demande, prestations et satisfaction de commandes ; visibilité des transferts entrants associés au produit de commande.

**Différences.** La page porte un avertissement preview ; appui sur le sens métier, pas recommandation de produit ni assertion de disponibilité générale.

**Position FLOW.** U401 adopte ce comportement sous Transfer Order. Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Integrate Supply Chain Management transfer orders with Intelligent Order Management](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/integrate-transfer-orders) — Documentation évolutive avec avertissement preview, consulté le 2026-09-18.

**Passage.** Typical reasons ; View transfer order products on sales order product page

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV073 Stock Consolidation

### Oracle — Overview of Inventory Rebalancing

Fusion Cloud Replenishment Planning · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Rééquilibrage excédents/manques et ordres planifiés ; transfert possible vers un lieu de regroupement.

**Différences.** Le produit combine décision et génération des ordres ; FLOW garde ces responsabilités séparées.

**Position FLOW.** U401 adopte ce comportement sous Transfer Order. Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Overview of Inventory Rebalancing](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/overview-of-inventory-rebalancing.html) — 26B, consulté le 2026-09-18.

**Passage.** Salient Features ; planned inbound and outbound orders

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

### Nextail — Merkal implements AI to centralize and streamline inventory planning across all channels

Inventory Planning · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Transferts de fin de saison, rééquilibrage du réseau et consolidation des tailles.

**Différences.** Témoignage éditeur/client, pas spécification normative ni preuve de déploiement Beaumanoir.

**Position FLOW.** U401 adopte ce comportement sous Transfer Order. Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Merkal implements AI to centralize and streamline inventory planning across all channels](https://nextail.co/customer/merkal-footwear-inventory-planning/) — Étude client, version non affichée, consulté le 2026-09-18.

**Passage.** Sharper store transfers ; customer quote on consolidation

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV074 Order-Driven Transfer

### Microsoft — Integrate Supply Chain Management transfer orders with Intelligent Order Management

Dynamics 365 Intelligent Order Management / SCM · Processus, mécanisme ou document produit ; étude client lorsque précisé · Recouvrement partiel · statut : proposed

**Points communs.** Transferts pour réassort, pointe de demande, prestations et satisfaction de commandes ; visibilité des transferts entrants associés au produit de commande.

**Différences.** La page porte un avertissement preview ; appui sur le sens métier, pas recommandation de produit ni assertion de disponibilité générale.

**Position FLOW.** U401 adopte ce comportement sous Transfer Order. Microsoft documente le réassort, le rééquilibrage et les transferts liés aux ventes ; Oracle et Nextail documentent rééquilibrage/regroupement ; SAP Retail historique appuie l’implantation. Les cinq comportements forment une proposition FLOW, pas une taxonomie éditeur copiée.

[Integrate Supply Chain Management transfer orders with Intelligent Order Management](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/integrate-transfer-orders) — Documentation évolutive avec avertissement preview, consulté le 2026-09-18.

**Passage.** Typical reasons ; View transfer order products on sales order product page

**Limite de preuve.** Page primaire ouverte ; aucune preuve de déploiement Beaumanoir.

Références : U400, U401, ELM240, CMP151.

## Comparaison par rapport au marché — BHV075 Additional Supply Feasibility

### Microsoft — Calculate delivery dates using CTP

Dynamics 365 Supply Chain Management / Planning Optimization · Mécanisme ou processus produit · Recouvrement partiel · statut : proposed

**Points communs.** CTP vérifie matières et capacités pour déterminer les dates réalisables, notamment pour assembler ou produire à la demande.

**Différences.** Appui au mécanisme d’apport supplémentaire ; le CTP FLOW est plus large que ce cas de fabrication. Aucun processus de production interne FLOW ni équivalence de taxonomie déduit.

**Position FLOW.** Trois mécanismes combinables sous CTP, noms FLOW ; faisabilité distincte du scénario collectif et de sa mise en application.

[Calculate delivery dates using CTP](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp) — Documentation évolutive ; mise à jour affichée 2026-07-27, consulté le 2026-09-18.

**Passage.** How CTP compares to ATP ; exemple de fabrication de A à partir de B et C

**Limite de preuve.** Texte primaire consulté ; aucune taxonomie universelle ni preuve de déploiement Beaumanoir.

Références : U402, ELM241, CMP152.

## Comparaison par rapport au marché — BHV076 Fulfillment Alternative Feasibility

### SAP — Alternative-Based Confirmation

SAP S/4HANA aATP · Mécanisme ou processus produit · Recouvrement partiel · statut : proposed

**Points communs.** Alternative-Based Confirmation examine des sites alternatifs et des produits de substitution selon des règles.

**Différences.** SAP expose ABC sous aATP. FLOW distingue alternatives déjà admissibles (ATP) et adaptations de la référence (CTP). L’exemple express est une illustration FLOW ; cette page ne prouve pas un mécanisme ABC de choix de transport express.

**Position FLOW.** Trois mécanismes combinables sous CTP, noms FLOW ; faisabilité distincte du scénario collectif et de sa mise en application.

[Alternative-Based Confirmation](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5) — S/4HANA ; cours couvrant plusieurs évolutions, consulté le 2026-09-18.

**Passage.** Advanced ATP Scenario: Alternative-Based Confirmation (ABC)

**Limite de preuve.** Texte primaire consulté ; aucune taxonomie universelle ni preuve de déploiement Beaumanoir.

Références : U402, ELM241, CMP152.

## Comparaison par rapport au marché — BHV077 Commitment Rebalancing Feasibility

### SAP — Exploring Backorder Processing

SAP S/4HANA Cloud Public Edition / Backorder Processing · Mécanisme ou processus produit · Recouvrement partiel · statut : proposed

**Points communs.** BOP réexamine les confirmations selon disponibilités et priorités, avec stratégies de préservation, amélioration et redistribution.

**Différences.** Le processus SAP traverse plusieurs responsabilités FLOW : faisabilité CTP, décision collective, priorités, révision de promesse et application des affectations. BOP ne correspond pas à un comportement CTP unique ni à une autorité de CTP pour choisir les perdants.

**Position FLOW.** Trois mécanismes combinables sous CTP, noms FLOW ; faisabilité distincte du scénario collectif et de sa mise en application.

[Exploring Backorder Processing](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe) — S/4HANA Cloud Public Edition ; cours évolutif, consulté le 2026-09-18.

**Passage.** Backorder Processing Overview ; Confirmation Strategies

**Limite de preuve.** Texte primaire consulté ; aucune taxonomie universelle ni preuve de déploiement Beaumanoir.

Références : U402, ELM241, CMP152.

## Comparaison par rapport au marché — BHV078 Supplier Confirmation

### Microsoft — Vendor collaboration with external vendors

Dynamics 365 Supply Chain Management · Processus, fonction ou objet produit · Recouvrement partiel · statut : proposed

**Points communs.** Le processus distingue envoi de la commande, réponse fournisseur (acceptation, refus, changements) et confirmation, avec versions et historique. Les changements peuvent porter sur quantités, dates et échéanciers.

**Différences.** Vendor collaboration couvre plus que ce comportement (notamment RFQ et factures). FLOW conserve le mécanisme d’engagement sur Purchase Order, sans copier l’interface, les étapes manuelles ou tous les statuts produit.

**Position FLOW.** Supplier Confirmation est un mécanisme combinable de Purchase Order ; engagement reçu distinct de la promesse client et de la réalisation. Confirmation et révision restent dans un seul comportement.

[Vendor collaboration with external vendors](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/vendor-collaboration-work-external-vendors) — Documentation évolutive ; mise à jour affichée 2025-07-21, consulté le 2026-09-19.

**Passage.** Working with POs when vendor collaboration is used ; Changing a PO ; Updating a PO when a vendor suggests changes

**Limite de preuve.** Texte primaire ouvert et consulté ; aucune preuve de réalisation installée chez Beaumanoir.

Références : U403, ELM242, CMP153.

### Microsoft — Review and accept changes to confirmed purchase orders

Dynamics 365 Supply Chain Management · Processus, fonction ou objet produit · Recouvrement partiel · statut : proposed

**Points communs.** L’examen de modifications d’achats confirmés s’appuie sur leurs conséquences sur les demandes aval avant reconfirmation et permet des échanges avec le fournisseur.

**Différences.** Cette fonction documente les impacts directs, pas tous les impacts indirects. FLOW répartit engagement fournisseur, analyse des possibilités, décision collective et promesse client entre capacités distinctes. Aucune capacité Copilot ou écran créée.

**Position FLOW.** Supplier Confirmation est un mécanisme combinable de Purchase Order ; engagement reçu distinct de la promesse client et de la réalisation. Confirmation et révision restent dans un seul comportement.

[Review and accept changes to confirmed purchase orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-changes-after-confirmation) — Documentation évolutive ; mise à jour affichée 2026-07-01, consulté le 2026-09-19.

**Passage.** Review changes to confirmed purchase orders ; Step 3, note on direct downstream impacts

**Limite de preuve.** Texte primaire ouvert et consulté ; aucune preuve de réalisation installée chez Beaumanoir.

Références : U403, ELM242, CMP153.

### SAP — Create Supplier Confirmation (Optional)

SAP S/4HANA Cloud Best Practices / Direct Procurement with Inbound Delivery (2TX) · Processus, fonction ou objet produit · Recouvrement partiel · statut : proposed

**Points communs.** Le passage expose une Supplier Confirmation rattachée au Purchase Order, avec date de livraison et quantité confirmées.

**Différences.** Appui au nom et aux données d’engagement ; le passage ne démontre pas à lui seul la totalité du mécanisme FLOW, ses révisions et impacts. Supplier Confirmation y est un objet/processus produit, pas une taxonomie de comportements d’entreprise.

**Position FLOW.** Supplier Confirmation est un mécanisme combinable de Purchase Order ; engagement reçu distinct de la promesse client et de la réalisation. Confirmation et révision restent dans un seul comportement.

[Create Supplier Confirmation (Optional)](https://help.sap.com/docs/s4hana-cloud-best-practices/direct-procurement-with-inbound-delivery-2tx-hr/create-supplier-confirmation-optional) — Édition non affichée dans le passage indexé consulté, consulté le 2026-09-19.

**Passage.** Enter Reference Purchase Order ; Create Supplier Confirmation Item ; Create Confirmation Line Data

**Limite de preuve.** Passage primaire indexé consulté ; ouverture directe du portail sans texte exploitable ; aucune preuve de réalisation installée chez Beaumanoir.

Références : U403, ELM242, CMP153.

## Comparaison par rapport au marché — BHV079 Warehouse Visibility

### SAP — Learning about the SAP EWM Solution

EWM for SAP S/4HANA Cloud Private Edition, extra stack ; cours sans numéro de release · documentation produit · Recouvrement partiel · statut : proposed

**Points communs.** EWM distingue les opérations entrantes, internes et sortantes : déchargement, rangement, préparation et chargement, avec suivi des unités logistiques et intégration TM.

**Différences.** Appui au périmètre sur site ; ne prescrit pas deux ou trois comportements FLOW ni un libellé canonique Warehouse Visibility.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[Learning about the SAP EWM Solution](https://learning.sap.com/courses/cloud-onboarding-for-sap-ewm-for-sap-s-4hana-cloud-private-edition-extra-stack/learning-about-the-sap-ewm-solution) — EWM for SAP S/4HANA Cloud Private Edition, extra stack ; cours sans numéro de release, consulté le 2026-09-19.

**Passage.** Introduction ; Goods Receipt ; Storage & Operations ; Conclusion

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

## Comparaison par rapport au marché — BHV080 Transportation Visibility

### project44 — Enhancing Automotive Finished Vehicle Logistics with Real Time Visibility

Article éditeur du 22 août 2023 ; édition logicielle non indiquée · article éditeur · Recouvrement partiel · statut : proposed

**Points communs.** Le terme Transportation Visibility accompagne localisation, progression multimodale, ETA et notifications ; exemple automobile au niveau véhicule.

**Différences.** Appui lexical et de périmètre, pas import du contexte automobile ni garantie de temps réel pour FLOW.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[Enhancing Automotive Finished Vehicle Logistics with Real Time Visibility](https://www.project44.com/blog/enhancing-automotive-finished-vehicle-logistics-with-real-time-visibility/) — Article éditeur du 22 août 2023 ; édition logicielle non indiquée, consulté le 2026-09-19.

**Passage.** Real-time transportation visibility / multimodal tracking

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

## Comparaison par rapport au marché — BHV081 Store Visibility

### Blue Yonder — What is Blue Yonder Store Execution Inventory Management?

Page produit évolutive sans édition figée · présentation produit · Recouvrement partiel · statut : proposed

**Points communs.** Store Execution désigne notamment les opérations de réception et de fiabilisation du stock en magasin ; la page décrit une réception directe en rayon et le résultat de disponibilité en rayon.

**Différences.** Présentation produit : réception et disponibilité en rayon documentées ; Store Visibility est le nom FLOW adopté par cohérence, pas une taxonomie éditeur démontrée.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[What is Blue Yonder Store Execution Inventory Management?](https://info.blueyonder.com/order-management-commerce/what-is-blue-yonder-store-execution-inventory-management) — Page produit évolutive sans édition figée, consulté le 2026-09-19.

**Passage.** Présentation et processus magasin

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

## Comparaison par rapport au marché — BHV082 Process Tracking

### Microsoft — Azure Business Process Tracking overview

Azure Business Process Tracking ; page mise à jour 2025-09-11 · documentation produit · Recouvrement partiel · statut : proposed

**Points communs.** Corrélation des étapes et de leurs propriétés métier par identifiant de transaction, par exemple commande ou case.

**Différences.** Le produit documenté mappe des étapes métier sur les opérations des workflows Standard stateful Logic Apps. FLOW retient le concept de suivi métier ; le lien Task/appels est sa convention, sans équivalence un pour un ni obligation Azure.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[Azure Business Process Tracking overview](https://learn.microsoft.com/en-us/azure/business-process-tracking/overview) — Azure Business Process Tracking ; page mise à jour 2025-09-11, consulté le 2026-09-19.

**Passage.** Business process design and tracking ; Limitations and known issues

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

### Microsoft — View Workflow Status and Run History

Azure Logic Apps ; documentation évolutive sans édition figée · documentation produit · Recouvrement partiel · statut : proposed

**Points communs.** Consultation des exécutions et de leurs actions, de leur statut et de leurs entrées/sorties pour suivre les traitements.

**Différences.** Suivi d’un produit configuré ; un statut technique ne définit pas le résultat métier du service.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[View Workflow Status and Run History](https://learn.microsoft.com/en-us/azure/logic-apps/view-workflow-status-run-history) — Azure Logic Apps ; documentation évolutive sans édition figée, consulté le 2026-09-19.

**Passage.** Workflow run history ; action status and inputs/outputs

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

### Camunda — Process Observability & AI Agent Monitoring

Présentation produit évolutive sans version figée · présentation produit · Recouvrement partiel · statut : proposed

**Points communs.** Visibilité des instances de processus en cours, de leurs variables et incidents, reliée au contexte du processus.

**Différences.** Présentation commerciale de Process Observability, incluant des moyens d’intervention et d’analyse plus larges que le tracking FLOW. Ne prouve pas une collecte exhaustive de tout service externe.

**Position FLOW.** Quatre perspectives de tracking complémentaires sous Operations Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.

[Process Observability & AI Agent Monitoring](https://camunda.com/platform/observability/) — Présentation produit évolutive sans version figée, consulté le 2026-09-19.

**Passage.** Process instances, incidents and distinction from APM/log monitoring

**Limite de preuve.** Texte primaire ouvert et consulté ; synthèse sélective. Aucune couverture installée Beaumanoir déduite.

Références : U305, U308, U404, U405, U406, ELM243, CMP154.

### Camunda — Process orchestration

Process Orchestration Handbook, page web courante · Concept et offre logicielle · Recouvrement partiel · statut : proposed

**Points communs.** Coordination des tâches manuelles et automatisées, des personnes, systèmes et dispositifs participant au processus.

**Différences.** Camunda décrit une plateforme et des mécanismes transverses. FLOW cartographie des responsabilités métier et sépare explicitement décision d’adaptation, orchestration et suivi.

**Position FLOW.** Le Process orchestre des Services ; Process Orchestration reprend le vocabulaire établi. Les autres intitulés FLOW ne constituent pas une taxonomie Camunda.

[Process Orchestration Handbook](https://camunda.com/process-orchestration/) — Page web consultée le 19 septembre 2026, consulté le 2026-09-19.

**Passage.** What is process orchestration? ; Processes with diverse endpoints

**Limite de preuve.** Source primaire effectivement consultée ; présentation éditeur, sans preuve de déploiement Beaumanoir.

Références : U407, U408, U409, ELM244, CMP155.

### Microsoft — Orchestration flows and providers

Dynamics 365 Intelligent Order Management · Mécanisme produit · Recouvrement partiel · statut : proposed

**Points communs.** Parcours de commande coordonné par actions, événements, politiques et communications avec les providers.

**Différences.** Le parcours IOM est contextualisé à la commande ; son périmètre produit ne se transpose pas directement au domaine FLOW. Séparer Service et Process ne présume ni provider unique ni cardinalité Task/appel.

**Position FLOW.** Appui à la distinction entre progression du processus et contributions des services ; aucune taxonomie complète adoptée.

[Intelligent Order Management overview](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview) — Documentation web, mise à jour 2026-01-30, consulté le 2026-09-19.

**Passage.** Providers ; Orchestration

**Limite de preuve.** Source primaire effectivement consultée ; pas de preuve installée Beaumanoir.

Références : U407, U408, U409, ELM244, CMP155.

## Comparaison par rapport au marché — D03.p Order Backlog Planning

### Oracle — Start Backlog Planning

Fusion Cloud SCM 26B · Processus et fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Prioriser et replannifier la satisfaction sur l’ensemble du carnet à partir des ressources et demandes actualisées.

**Différences.** Documentation d’un produit et de son traitement planifié, pas taxonomie de capacités ni preuve de prise en charge de tous les types d’Orders FLOW.

**Position FLOW.** U417 : Planning prépare les scénarios en mobilisant les décisions ; Lifecycle autorise la prise en charge. La release produit Oracle ne se transpose pas automatiquement à FLOW.

[Start Backlog Planning](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspc/start-backlog-planning.html) — 26B, consulté le 2026-09-19.

**Passage.** Introduction ; When to Use

**Limite de preuve.** Source primaire ouverte lors de la discussion ; aucune preuve de déploiement Beaumanoir. Niveaux et périmètres produits non transposés automatiquement.

Références : U414, ELM247, CMP158.

### Oracle — Key Actions on Orders

Fusion Cloud SCM 25D · Fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Travail du carnet, priorisation, simulation puis transmission des résultats retenus à Order Management.

**Différences.** Release Planning Results transmet des résultats de planification ; ce n’est pas une équivalence exacte de l’autorisation FLOW vers les processus. La séparation demande/carnet/processus est la convention FLOW.

**Position FLOW.** U417 : Planning prépare les scénarios en mobilisant les décisions ; Lifecycle autorise la prise en charge. La release produit Oracle ne se transpose pas automatiquement à FLOW.

[Key Actions on Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faubm/key-actions-on-orders.html) — 25D, édition explicitement consultée, consulté le 2026-09-19.

**Passage.** Plan Run Actions ; Attribute Data Simulation Actions ; Release Actions

**Limite de preuve.** Source primaire ouverte lors de la discussion ; aucune preuve de déploiement Beaumanoir. Niveaux et périmètres produits non transposés automatiquement.

Références : U414, ELM247, CMP158.

### Microsoft — Planned orders simplified

Dynamics 365 Supply Chain Management · Fonction produit · Recouvrement partiel · statut : proposed

**Points communs.** Revue, approbation et affermissement des propositions issues de la planification ; split disponible dans la page standard.

**Différences.** Propositions d’approvisionnement, pas tous les Orders FLOW. La liste d’opérations produit ne devient pas une décomposition automatique en comportements.

**Position FLOW.** U417 : Planning prépare les scénarios en mobilisant les décisions ; Lifecycle autorise la prise en charge. La release produit Oracle ne se transpose pas automatiquement à FLOW.

[Planned orders simplified](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-orders-simplified) — Page mise à jour le 3 octobre 2025, consulté le 2026-09-19.

**Passage.** View, manage, and firm planned orders

**Limite de preuve.** Source primaire ouverte lors de la proposition ; aucune preuve installée Beaumanoir.

Références : U414, ELM247, CMP158.

## Comparaison par rapport au marché — BHV083 Requirement-based Replenishment

### Microsoft — Per requirement / Per period

Dynamics 365 Supply Chain Management · Méthodes de réapprovisionnement et lotissement · Recouvrement partiel · statut : proposed

**Points communs.** Microsoft distingue apports par besoin et agrégation des besoins nets sur une période.

**Différences.** FLOW retient une seule politique métier orientée besoins datés. La période est une modalité et les objets créés par le produit ne deviennent pas une obligation de création d’Order par la décision.

**Position FLOW.** U427 : comportement métier adopté sous Replenishment Decision. Comparaison descriptive, sans alignement taxonomique exact ni preuve de déploiement Beaumanoir.

[Coverage settings](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/coverage-settings) — 2026-03-25, consulté le 2026-09-19.

**Passage.** Coverage codes

**Limite de preuve.** Page primaire ouverte avant intégration. Les noms FLOW ne sont pas présentés comme un catalogue de capacités Microsoft.

Références : U427, ELM253, CMP164.

## Comparaison par rapport au marché — BHV084 Target-based Replenishment

### Microsoft — Min/Max

Dynamics 365 Supply Chain Management · Méthodes de réapprovisionnement et lotissement · Recouvrement partiel · statut : proposed

**Points communs.** Microsoft documente un réassort vers un niveau cible lorsque la quantité projetée passe sous un seuil.

**Différences.** FLOW distingue la détermination des objectifs de leur utilisation pour les apports. Aucun seuil permanent, formule unique, comportement par paramètre ou couverture de toutes les méthodes Microsoft n’est déduit.

**Position FLOW.** U427 : comportement métier adopté sous Replenishment Decision. Comparaison descriptive, sans alignement taxonomique exact ni preuve de déploiement Beaumanoir.

[Coverage settings](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/coverage-settings) — 2026-03-25, consulté le 2026-09-19.

**Passage.** Coverage codes

**Limite de preuve.** Page primaire ouverte avant intégration. Les noms FLOW ne sont pas présentés comme un catalogue de capacités Microsoft.

Références : U427, ELM253, CMP164.

## Comparaison par rapport au marché — BHV085 Replenishment Adjustment

### Microsoft — Action messages — Advance / Postpone / Increase / Decrease

Dynamics 365 Supply Chain Management · Recommandations produit · Recouvrement partiel · statut : proposed

**Points communs.** Microsoft produit des suggestions de modification d’ordres existants en réponse aux changements de besoins.

**Différences.** Les recommandations et leur application restent séparées dans FLOW. La liste Microsoft consultée ne justifie pas un code Cancel natif ; l’annulation admissible est une possibilité FLOW soumise aux conditions métier. Pas de garantie d’arrêt des services par le calcul.

**Position FLOW.** U427 : comportement métier adopté sous Replenishment Decision. Comparaison descriptive, sans alignement taxonomique exact ni preuve de déploiement Beaumanoir.

[Action messages](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages) — 2026-03-26, consulté le 2026-09-19.

**Passage.** Introduction ; Select action messages

**Limite de preuve.** Page primaire ouverte avant intégration. Les noms FLOW ne sont pas présentés comme un catalogue de capacités Microsoft.

Références : U427, ELM253, CMP164.

## Comparaison par rapport au marché — Supply — sens fonctionnel du projet

### Microsoft — Balancing supply and demand

Dynamics 365 Business Central · Notion métier ou fonction produit documentée · Appui sémantique · statut : proposed

**Points communs.** Supply désigne le côté ressources : stock et apports entrants, notamment achats, production, transferts entrants et retours clients. Supply orders alimente ce côté du bilan.

**Différences.** Sémantique de planification Business Central, pas définition d’un périmètre organisationnel FLOW.

**Position FLOW.** Le sens fonctionnel FLOW est une convention locale ; Microsoft emploie ici supply au sens ressources. Aucune équivalence.

[Balancing supply and demand](https://learn.microsoft.com/en-us/dynamics365/business-central/design-details-balancing-demand-and-supply) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Supply and demand ; Process orders ; Priorities on the supply side

**Limite de preuve.** Documentation primaire ouverte ou passage primaire indexé consulté ; synthèse sélective, aucune réalisation Beaumanoir déduite.

Références : U366, U367, ELM225, CMP136.

### CSCMP — SCM Definitions and Glossary of Terms

Définitions professionnelles · Notion métier ou fonction produit documentée · Appui sémantique · statut : proposed

**Points communs.** SCM couvre approvisionnement, transformation, logistique et coordination entre partenaires. Le fulfillment figure parmi les activités logistiques.

**Différences.** Définition de Supply Chain Management, utilisée pour délimiter le périmètre ; ce n’est pas une taxonomie de capacités FLOW.

**Position FLOW.** Le périmètre fonctionnel FLOW est plus limité que celui de SCM ; aucune extension de responsabilité par le vocabulaire.

[SCM Definitions and Glossary of Terms](https://cscmp.org/CSCMP/Educate/SCM_Definitions_and_Glossary_of_Terms.aspx) — Page de référence sans édition affichée, consulté le 2026-09-18.

**Passage.** Definitions of Supply Chain Management ; Logistics Management

**Limite de preuve.** Documentation primaire ouverte ou passage primaire indexé consulté ; synthèse sélective, aucune réalisation Beaumanoir déduite.

Références : U366, U367, ELM225, CMP136.

## Comparaison par rapport au marché — Implantation

### SAP — Initial Allocation

Allocation Management · Scénarios métier d’un produit · Recouvrement partiel · statut : proposed

**Points communs.** Première distribution de produits vers les magasins pour préparer leur lancement commercial ; rapprochement avec l’implantation initiale décrite par Laurent.

**Différences.** SAP décrit un produit qui couvre planification et traitement de la distribution. FLOW sépare décision des apports, gestion des Orders et exécution. Le réassort décrit par Laurent est guidé par des seuils ; cette documentation SAP ne démontre pas une formule identique. La notion SAP de collection ou thème ne prouve pas un usage de capsules chez Beaumanoir.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[SAP Allocation Management — Business Overview](https://help.sap.com/docs/CARAB/00197153997746b4bec2020d00e66ea9/e99798c39a3f4956bd5ce509b39382f7.html?locale=en-US&state=PRODUCTION&version=5.0.2) — 5.0 FPS02 — version de la documentation consultée, consulté le 2026-09-18.

**Passage.** Business Scenarios : Initial Allocation ; In-Season Fill-In

**Limite de preuve.** Texte primaire indexé consulté ; ouverture de la page sans corps exploitable. Pas de preuve de déploiement Beaumanoir, ni d’équivalence de hiérarchie Capacité → Comportement.

Références : ELM198, CMP106, U310, U311, U313, U314, CMP107, U315, CMP108, U316.

### RELEX — Initial allocation

Replenishment and allocation · Fonctions présentées par l’éditeur · Recouvrement partiel · statut : proposed

**Points communs.** Première distribution de produits vers les magasins pour préparer leur lancement commercial ; rapprochement avec l’implantation initiale décrite par Laurent.

**Différences.** La présentation RELEX associe aussi commandes présaison et gestion de fin de saison. Ces fonctions ne sont pas ajoutées implicitement à FLOW. Le réassort produit utilise notamment des prévisions ; une identité avec les seuils et règles Beaumanoir n’est pas établie.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[RELEX — Replenishment and allocation](https://www.relexsolutions.com/solutions/automatic-replenishment-system/) — Présentation produit évolutive, sans édition figée, consulté le 2026-09-18.

**Passage.** Manage the full cycle for your seasonal items ; Manage seasons effectively

**Limite de preuve.** Présentation commerciale primaire consultée. Aucun contrat fonctionnel exhaustif, aucune formule de seuil équivalente ni déploiement Beaumanoir démontré.

Références : ELM198, CMP106, U310, U311, U313, U314, CMP107, U315, CMP108, U316.

### OASIS — Initial Stocking of the Area by Retailer

Universal Business Language (UBL) · Processus métier documenté dans un standard d’échanges · Appui sémantique · statut : proposed

**Points communs.** Constitution d’un stock de départ au début d’une relation commerciale ou d’une saison ; le processus Initial Stocking est distingué du réassort périodique.

**Différences.** UBL décrit un processus producteur-distributeur avec commandes et livraisons, notamment pour des articles NOS saisonniers. FLOW isole la décision des apports, sans adopter ce schéma de coopération, sa cadence hebdomadaire ni ses délais de livraison.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[Universal Business Language Version 2.4](https://docs.oasis-open.org/ubl/UBL-2.4.html) — 2.4, consulté le 2026-09-18.

**Passage.** 2.3.3.5.3.3 Initial Stocking of the Area by Retailer ; 2.3.3.5.3.4 Periodic (Weekly) Replenishment

**Limite de preuve.** Texte primaire consulté. Attestation du terme Initial Stocking dans un contexte saisonnier ; pas une normalisation du nom Initial Stocking Decision ni un consensus des logiciels de mode.

Références : U315, ELM200, CMP108, U316.

### Logility — Initial distribution

Présentation retail — cas Groupe Dynamite · Terme descriptif employé dans une présentation client · Appui sémantique · statut : proposed

**Points communs.** Distribution initiale distinguée du réassort dans un contexte de mode, de magasins et de déclinaisons style/couleur/taille.

**Différences.** La présentation ne définit pas une capacité de décision ni ses entrées/sorties. Distribution décrit le flux vers les magasins ; le terme ne précise pas à lui seul la frontière avec la réalisation logistique.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[Retail Optimization Gives Groupe Dynamite an Edge](https://www.logility.com/webcast/retail-optimization-gives-groupe-dynamite-an-edge/) — Page de présentation sans édition figée ni date affichée, consulté le 2026-09-18.

**Passage.** Présentation textuelle du webcast, initial distribution as well as replenishment

**Limite de preuve.** Texte primaire de présentation consulté ; vidéo non visionnée. Usage descriptif attesté, pas nom de module ou taxonomie standard démontré.

Références : U315, ELM200, CMP108, U316.

### Nextail — First Allocation / initial distribution

First Allocation · Nom d’une solution et formulation descriptive de sa finalité · Appui sémantique · statut : proposed

**Points communs.** La solution First Allocation vise la distribution initiale de nouveaux produits aux magasins ; Replenishment et Store Transfers sont présentés séparément.

**Différences.** Le nom de solution conserve Allocation ; initial distribution apparaît dans sa description. Le produit regroupe prévisions, optimisation et paramètres : ce regroupement ne définit pas la hiérarchie FLOW.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[Nextail — Solution specifications](https://help.nextail.co/en/solution-specifications) — Documentation en ligne non versionnée, consulté le 2026-09-18.

**Passage.** First Allocation ; Replenishment ; Store Transfers

**Limite de preuve.** Documentation primaire consultée. Confirme le sens d’initial distribution mais pas son adoption comme libellé officiel de capacité.

Références : U315, ELM200, CMP108, U316.

## Comparaison par rapport au marché — Réassort

### SAP — In-Season Fill-In

Allocation Management · Scénarios métier d’un produit · Recouvrement partiel · statut : proposed

**Points communs.** Alimenter les stocks magasins pendant la commercialisation après la mise en place initiale ; rapprochement avec le Réassort décrit par Laurent.

**Différences.** SAP décrit un produit qui couvre planification et traitement de la distribution. FLOW sépare décision des apports, gestion des Orders et exécution. Le réassort décrit par Laurent est guidé par des seuils ; cette documentation SAP ne démontre pas une formule identique. La notion SAP de collection ou thème ne prouve pas un usage de capsules chez Beaumanoir.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[SAP Allocation Management — Business Overview](https://help.sap.com/docs/CARAB/00197153997746b4bec2020d00e66ea9/e99798c39a3f4956bd5ce509b39382f7.html?locale=en-US&state=PRODUCTION&version=5.0.2) — 5.0 FPS02 — version de la documentation consultée, consulté le 2026-09-18.

**Passage.** Business Scenarios : Initial Allocation ; In-Season Fill-In

**Limite de preuve.** Texte primaire indexé consulté ; ouverture de la page sans corps exploitable. Pas de preuve de déploiement Beaumanoir, ni d’équivalence de hiérarchie Capacité → Comportement.

Références : ELM198, CMP106, U310, U311, U313, U314, CMP107, U316.

### RELEX — In-season replenishment

Replenishment and allocation · Fonctions présentées par l’éditeur · Recouvrement partiel · statut : proposed

**Points communs.** Alimenter les stocks magasins pendant la commercialisation après la mise en place initiale ; rapprochement avec le Réassort décrit par Laurent.

**Différences.** La présentation RELEX associe aussi commandes présaison et gestion de fin de saison. Ces fonctions ne sont pas ajoutées implicitement à FLOW. Le réassort produit utilise notamment des prévisions ; une identité avec les seuils et règles Beaumanoir n’est pas établie.

**Position FLOW.** Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.

[RELEX — Replenishment and allocation](https://www.relexsolutions.com/solutions/automatic-replenishment-system/) — Présentation produit évolutive, sans édition figée, consulté le 2026-09-18.

**Passage.** Manage the full cycle for your seasonal items ; Manage seasons effectively

**Limite de preuve.** Présentation commerciale primaire consultée. Aucun contrat fonctionnel exhaustif, aucune formule de seuil équivalente ni déploiement Beaumanoir démontré.

Références : ELM198, CMP106, U310, U311, U313, U314, CMP107, U316.

## Comparaison par rapport au marché — Split

### Oracle — What’s a Split Order Line

Fusion Cloud Order Management · Fonction produit, verbe descriptif ou stratégie de répartition · Appui sémantique · statut : proposed

**Points communs.** Split couvre plusieurs entrepôts, dates ou articles substituts, et peut créer plusieurs lignes et tâches de fulfillment.

**Différences.** Ne signifie pas toujours création de plusieurs commandes autonomes ; la fonction produit combine décisions et effets que FLOW sépare.

**Position FLOW.** Split comme mutation avec filiation ; composition persistante distincte. U363 applique la structure ; les correspondances marché restent proposées.

[What’s a Split Order Line](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/fulfillment-line-splits.html) — 26B, consulté le 2026-09-18.

**Passage.** How Order Management Determines Availability

**Limite de preuve.** Oracle ouvert ; passages Microsoft et SAP indexés consultés, page SAP dynamique sans texte à l’ouverture. Aucune implémentation Beaumanoir déduite.

Références : U360, ELM222, CMP131, U363, CMP133.

## Comparaison par rapport au marché — Spread

### SAP — Steps in Order Allocation Run — Allocation

ERP Fashion Management · Stratégie de répartition dans un processus produit · Recouvrement partiel · statut : proposed

**Points communs.** ARun peut affecter le stock selon FIFO ou une répartition proportionnelle fondée sur les quantités demandées (spread logic). Le regroupement des besoins est un prérequis au Spread.

**Différences.** Référence ERP Fashion, sans garantie pour toute édition aATP. ARun est le processus intégré ; Spread une de ses stratégies. La répartition ne nécessite pas la création de nouvelles commandes.

**Position FLOW.** Spread est une politique de répartition des ressources entre commandes. Les décisions déterminent les parts ; Supply Assignment applique les liens. Aucun agrégat décisionnel ou comportement automatique ajouté. U363 applique la structure ; les correspondances marché restent proposées.

[Steps in Order Allocation Run](https://help.sap.com/docs/SAP_ERP_SPV/f48e74ad3b3740bc8c9eaade394a3c1e/3d1df055aa2a6d55e10000000a4450e5.html) — Édition non relevée dans le passage indexé ; SAP ERP Fashion Management, consulté le 2026-09-18.

**Passage.** Requirement Grouping ; Allocation ; Release Rules

**Limite de preuve.** Passage primaire indexé consulté, complété par Allocation déjà documenté ELM222. Aucune preuve de configuration ou version Beaumanoir.

Références : U361, ELM223, CMP132, U363, CMP133.

## Comparaison par rapport au marché — Supply

### Microsoft — Balancing supply and demand

Dynamics 365 Business Central · Notion métier ou fonction produit documentée · Appui sémantique · statut : proposed

**Points communs.** Supply désigne le côté ressources : stock et apports entrants, notamment achats, production, transferts entrants et retours clients. Supply orders alimente ce côté du bilan.

**Différences.** Sémantique de planification Business Central, pas définition d’un périmètre organisationnel FLOW.

**Position FLOW.** Sens métier ressources, illustré par Microsoft Business Central et SAP ARun ; ce n’est pas un synonyme universel d’approvisionnement ni de Supply Chain.

[Balancing supply and demand](https://learn.microsoft.com/en-us/dynamics365/business-central/design-details-balancing-demand-and-supply) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Supply and demand ; Process orders ; Priorities on the supply side

**Limite de preuve.** Documentation primaire ouverte ou passage primaire indexé consulté ; synthèse sélective, aucune réalisation Beaumanoir déduite.

Références : U366, U367, ELM225, CMP136.

### SAP — Backorder Processing — Supply Assignment

S/4HANA aATP · Notion métier ou fonction produit documentée · Appui sémantique · statut : proposed

**Points communs.** Supply Assignment relie besoins, stocks et réceptions futures ; réaffectation paramétrable.

**Différences.** Fonction intégrée SAP ; FLOW sépare décision, affectation, réservation et promesse.

**Position FLOW.** Sens métier ressources, illustré par Microsoft Business Central et SAP ARun ; ce n’est pas un synonyme universel d’approvisionnement ni de Supply Chain.

[Backorder Processing — Supply Assignment](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html) — 2025 FPS01 (Feb 2026), consulté le 2026-09-18.

**Passage.** Supply Selection ; Assignment ; Reassignment

**Limite de preuve.** Documentation primaire ouverte ou passage primaire indexé consulté ; synthèse sélective, aucune réalisation Beaumanoir déduite.

Références : U366, U367, ELM225, CMP136.

## Comparaison par rapport au marché — Supply Chain

### CSCMP — SCM Definitions and Glossary of Terms

Définitions professionnelles · Notion métier ou fonction produit documentée · Appui sémantique · statut : proposed

**Points communs.** SCM couvre approvisionnement, transformation, logistique et coordination entre partenaires. Le fulfillment figure parmi les activités logistiques.

**Différences.** Définition de Supply Chain Management, utilisée pour délimiter le périmètre ; ce n’est pas une taxonomie de capacités FLOW.

**Position FLOW.** Définition éditoriale appuyée sur ASCM et sur le périmètre de Supply Chain Management défini par CSCMP. Supply Chain désigne le système ; Supply Chain Management sa gestion.

[SCM Definitions and Glossary of Terms](https://cscmp.org/CSCMP/Educate/SCM_Definitions_and_Glossary_of_Terms.aspx) — Page de référence sans édition affichée, consulté le 2026-09-18.

**Passage.** Definitions of Supply Chain Management ; Logistics Management

**Limite de preuve.** Documentation primaire ouverte ou passage primaire indexé consulté ; synthèse sélective, aucune réalisation Beaumanoir déduite.

Références : U366, U367, ELM225, CMP136.

### ASCM — What is supply chain logistics?

Ressource professionnelle · Notion métier ou fonction produit documentée · Appui sémantique · statut : proposed

**Points communs.** La supply chain est décrite comme un réseau amont-aval ; le fulfillment est orienté vers la réalisation des commandes.

**Différences.** Présentation pédagogique centrée sur les biens ; ne tranche pas tous les cas de retours ou services numériques FLOW.

**Position FLOW.** Définition éditoriale appuyée sur ASCM et sur le périmètre de Supply Chain Management défini par CSCMP. Supply Chain désigne le système ; Supply Chain Management sa gestion.

[What is supply chain logistics?](https://www.ascm.org/topics/logistics/) — Page évolutive, consulté le 2026-09-18.

**Passage.** Supply chain vs logistics ; Order processing and fulfillment

**Limite de preuve.** Documentation primaire ouverte ou passage primaire indexé consulté ; synthèse sélective, aucune réalisation Beaumanoir déduite.

Références : U366, U367, ELM225, CMP136.

## Comparaison par rapport au marché — Fulfillment

### Microsoft — Intelligent Fulfillment Optimization

Dynamics 365 Intelligent Order Management · Notion métier ou fonction produit documentée · Appui sémantique · statut : proposed

**Points communs.** Stratégies de satisfaction associant sources, objectifs et contraintes ; optimisation possible de commandes groupées et restitution d’un plan.

**Différences.** Service logiciel, plus large qu’une décision de cadre. Objectif de proximité documenté ; aucune équivalence complète à D03 ni solveur universel multiobjectif démontré.

**Position FLOW.** La documentation Microsoft distingue optimisation de la satisfaction et opérations effectives de fulfillment. Formulation FLOW proposée ; aucune nouvelle capacité agrégée n’est créée par le terme.

[Intelligent Fulfillment Optimization](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/ifo-arch) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Fulfillment sources ; Business constraints ; Fulfillment strategies

**Limite de preuve.** Documentation primaire ouverte ou passage primaire indexé consulté ; synthèse sélective, aucune réalisation Beaumanoir déduite.

Références : U366, U367, ELM225, CMP136.

### Microsoft — Store order fulfillment

Dynamics 365 Commerce · Notion métier ou fonction produit documentée · Appui sémantique · statut : proposed

**Points communs.** Fulfillment inclut des opérations effectives de préparation et remise ou expédition des commandes.

**Différences.** Le produit décrit l’exécution magasin ; FLOW distingue pilotage et opérations internes des exécutants.

**Position FLOW.** La documentation Microsoft distingue optimisation de la satisfaction et opérations effectives de fulfillment. Formulation FLOW proposée ; aucune nouvelle capacité agrégée n’est créée par le terme.

[Store order fulfillment](https://learn.microsoft.com/en-us/dynamics365/commerce/order-fulfillment-overview) — Documentation évolutive, consulté le 2026-09-18.

**Passage.** Introduction ; Pick ; Pack ; Pick up ; Shipping

**Limite de preuve.** Documentation primaire ouverte ou passage primaire indexé consulté ; synthèse sélective, aucune réalisation Beaumanoir déduite.

Références : U366, U367, ELM225, CMP136.

### ASCM — What is supply chain logistics?

Ressource professionnelle · Notion métier ou fonction produit documentée · Appui sémantique · statut : proposed

**Points communs.** La supply chain est décrite comme un réseau amont-aval ; le fulfillment est orienté vers la réalisation des commandes.

**Différences.** Présentation pédagogique centrée sur les biens ; ne tranche pas tous les cas de retours ou services numériques FLOW.

**Position FLOW.** La documentation Microsoft distingue optimisation de la satisfaction et opérations effectives de fulfillment. Formulation FLOW proposée ; aucune nouvelle capacité agrégée n’est créée par le terme.

[What is supply chain logistics?](https://www.ascm.org/topics/logistics/) — Page évolutive, consulté le 2026-09-18.

**Passage.** Supply chain vs logistics ; Order processing and fulfillment

**Limite de preuve.** Documentation primaire ouverte ou passage primaire indexé consulté ; synthèse sélective, aucune réalisation Beaumanoir déduite.

Références : U366, U367, ELM225, CMP136.

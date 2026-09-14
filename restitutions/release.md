# Release — 2026-09-14.1

Restitution générée depuis le modèle structuré, connaissance au 2026-09-14. Ne pas éditer cette vue pour modifier le modèle.

Publication et validation sont distinctes. Le statut d’un rattachement peut différer de celui de la capacité.

## Niveaux d’urbanisation

| Repère | Nom | Niveau | Contenu direct | Statut |
| --- | --- | --- | --- | --- |
| universe-case | Business Services | universe | Exploration différée | Validé par l’urbaniste — portée : name, definition |
| universe-supply | Supply | universe | Inventory Management, Order Promising, Order Management, Operational Resource Balancing, Execution Options, Execution Commitments and Facts, Business References | Validé par l’urbaniste — portée : name |

Les groupes de présentation, dont Business References, conservent leur rôle distinct.

## D01 — Inventory Management

Statut : **En cours d’instruction**.

Connaître les stocks et les ressources attendues, expliquer leurs variations, fiabiliser les quantités et préserver les usages par les protections et réservations. Le stock futur est connu ici et mobilisé par Order Promising.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D01.f | Inventory Tracking | Proposé par l’IA | Établir et actualiser les quantités physiques et leurs états logiques à partir des faits de stock reconnus, par référence de produit, lieu, détenteur et propriétaire lorsque ces dimensions sont pertinentes ; suivre distinctement les ressources futures connues et leurs caractéristiques attendues. | Disposer d’un état du stock à jour, expliqué par les faits reconnus, en distinguant présent et attendu. | En cours d’instruction |
| D01.g | Record Inventory Movements | Validé par l’urbaniste — portée : name | Enregistrer, qualifier et conserver les mouvements de stock et leurs justifications : réceptions, sorties, transferts, changements d’état ou de propriété et ajustements justifiés ; identifier les quantités concernées, les dates et les références explicatives, y compris sans déplacement physique. | Disposer d’un historique traçable des faits qui expliquent les variations du stock. | En cours d’instruction |
| D01.c | Inventory Visibility | En cours d’instruction | Fournir une lecture cohérente des stocks physiques, de leurs états logiques et des ressources futures dans les différents lieux et périmètres, avec provenance et fraîcheur, sans double compte. | Permettre aux décisions de s’appuyer sur une connaissance partagée. | En cours d’instruction |
| D01.d | Stocktaking | Validé par l’urbaniste — portée : definition, finality, name | établir les quantités constatées par comptage, les confronter aux quantités enregistrées, qualifier les écarts et établir les corrections justifiées. | Fiabiliser les quantités enregistrées — Inventory accuracy. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D02.b | Supply Protection | Validé par l’urbaniste — portée : name | établir et appliquer les quantités ou limites d’usage destinées à des groupes, avec leur validité. | Préserver les possibilités d’approvisionnement des usages retenus. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D02.c | Reservation | Validé par l’urbaniste — portée : name | établir un engagement de quantité pour un besoin identifié, dont les usages concurrents doivent tenir compte. | Donner effet à un engagement de ressource. | Validé par l’urbaniste — portée : source_id, target_id, type |

## D03 — Order Promising

Statut : **Validé par l’urbaniste — portée : name**.

Établir ce qui peut être promis pour honorer une commande Supply, sous quelles conditions, avec quelles ressources et quelles possibilités de mise à disposition, puis maintenir la promesse lorsque la situation évolue.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D03.a | Promise Proposal | Validé par l’urbaniste — portée : finality, name, nature | Construire une proposition de mise à disposition de ressources pour honorer une commande Supply, précisant quantités, dates, conditions et alternatives possibles, à partir des ressources et possibilités de réalisation. | Faire naître une proposition de promesse réalisable. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.b | Promise Confirmation | Validé par l’urbaniste — portée : definition, finality, name, nature | établir les quantités et dates promises, en distinguant la part confirmée de celle qui ne l’est pas. | Donner un engagement explicite au destinataire. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.c | Promise Revision | Validé par l’urbaniste — portée : finality, name, nature | Réexaminer les promesses lorsque les ressources, commandes, dates ou priorités changent et établir les modifications autorisées. | Maintenir des engagements cohérents avec la situation et les priorités applicables. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D02.e | Supply Assignment | Validé par l’urbaniste — portée : name, nature | Affecter, réaffecter ou libérer des ressources admissibles présentes ou futures pour couvrir des commandes Supply, des engagements ou des besoins prévisionnels. | Assurer la couverture des commandes, engagements ou besoins prévisionnels par des ressources identifiées. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.i | Available-to-Promise (ATP) | Validé par l’urbaniste — portée : definition, finality, name, nature | Établir les quantités et dates proposées pour honorer une commande avec les stocks et engagements admissibles, en appliquant les protections et règles existantes, sans modifier ces engagements ou politiques. | Établir une solution de promesse réalisable dans la situation de référence. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.j | Capable-to-Promise (CTP) | Validé par l’urbaniste — portée : definition, finality, name, nature | Proposer un plan cohérent d’adaptation des ressources et engagements pour honorer une commande : approvisionnements supplémentaires, révisions des quantités ou dates des autres commandes ou de leurs promesses, et changements de protection, avec impacts et autorisations nécessaires. | Établir à quelles conditions une promesse deviendrait réalisable après adaptation. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.k | Profitable-to-Promise (PTP) | Validé par l’urbaniste — portée : definition, finality, name, nature | Comparer et sélectionner les scénarios de promesse selon leurs coûts et conséquences économiques, dans les contraintes de service applicables. | Retenir une solution économiquement pertinente parmi les possibilités examinées. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.l | Delivery Schedule Decision | Validé par l’urbaniste — portée : definition, finality, name, nature | Choisir la répartition des quantités promises dans le temps, en une ou plusieurs échéances, parmi les possibilités réalisables et selon les conditions de la commande. | Retenir un échéancier acceptable pour honorer la commande. | Validé par l’urbaniste — portée : source_id, target_id, type |
| D03.m | Order Prioritization | Validé par l’urbaniste — portée : name, definition | Établir et réviser les priorités relatives des commandes. | Arbitrer les commandes à satisfaire en priorité lorsque leurs besoins se trouvent en concurrence. | Validé par l’urbaniste — portée : source_id, target_id, type |

## D04 — Order Management

Statut : **Validé par l’urbaniste — portée : name**.

Piloter les Orders transactionnels de la Supply, distincts des Cases : connaître leur contenu applicable, leurs évolutions et leur situation, pour toutes natures de commandes, notamment achats, ventes, transferts et retours, indépendamment des catégories de clients et des volumes. Distinguer les conditions contractuelles reçues, la promesse et les engagements de réalisation ; frontières détaillées avec D07 à instruire.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D04.e | Order Registration | Validé par l’urbaniste — portée : name, definition | Reconnaître et enregistrer une commande Supply et son origine. | Disposer d’une commande identifiée et reliée à son origine pour engager son traitement transactionnel. | Proposé par l’IA |
| D04.f | Order Revision | Validé par l’urbaniste — portée : name, definition | Intégrer ses évolutions autorisées, avec leur historique. | Conserver la version applicable de la commande et la trace de ses évolutions. | Proposé par l’IA |
| D04.g | Order Visibility | Validé par l’urbaniste — portée : name, definition | Restituer son contenu applicable et sa situation. | Partager une connaissance intelligible de la commande et de son avancement. | Proposé par l’IA |
| D04.h | Order Reconciliation | Validé par l’urbaniste — portée : name, definition | Établir ce qui reste à satisfaire en rapprochant commande, modifications et réalisations. | Connaître le reliquat de la commande à satisfaire, sans confondre les reliquats contractuels et de prestation. | Proposé par l’IA |

## D05 — Operational Resource Balancing

Statut : **En cours d’instruction**.

Établir les objectifs de couverture, les besoins nets et les redistributions utiles à l’équilibrage opérationnel. Le dossier Demande de réassort appartient au modèle processus ; calculer un besoin ne promet ni ne réalise un transfert.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D05.a | Determine operational coverage targets | En cours d’instruction | établir niveaux et seuils applicables par ressource et périmètre. | Donner une référence au renouvellement opérationnel des stocks. | En cours d’instruction |
| D05.b | Net Requirements Calculation | En cours d’instruction | identifier les manques ou excédents en tenant compte des positions, besoins et approvisionnements attendus pertinents. | Former un besoin justifié sans ignorer les ressources déjà attendues. | En cours d’instruction |
| D05.c | Determine resource redistribution | En cours d’instruction | proposer les quantités et destinations permettant de traiter des déséquilibres selon les contraintes. | Rééquilibrer les ressources lorsque leur distribution devient inadaptée. | En cours d’instruction |

## D06 — Execution Options

Statut : **En cours d’instruction**.

Utiliser les références du réseau et les contraintes opérationnelles pour apprécier les possibilités concrètes de réalisation et les options compatibles avec un besoin.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D06.a | Qualify locations and feasible services | En cours d’instruction | connaître les lieux, leurs rôles opérationnels et les prestations qui y sont admissibles. | Identifier les possibilités concrètes de réalisation. | En cours d’instruction |
| D06.b | Execution Capacity Assessment | Proposé par l’IA | apprécier limites applicables, charge engagée et capacité restante pour une prestation et une période. | Éviter de confondre disponibilité des biens et possibilité de réaliser la prestation attendue. | En cours d’instruction |
| D06.c | Execution Option Assessment | En cours d’instruction | établir et comparer les origines ou prestations compatibles avec un résultat attendu. | Éclairer un choix réalisable selon les critères autorisés. | En cours d’instruction |

## D07 — Execution Commitments and Facts

Statut : **En cours d’instruction**.

Exprimer les prestations nécessaires à la réalisation des Orders, suivre leur prise en charge, rapprocher les faits des prestations attendues et qualifier les ressources restant attendues. D04 conserve la commande autorisée et son reliquat ; D07 ne recrée ni Case ni Agreement.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D07.a | Execution Requirement Definition | Proposé par l’IA | Exprimer les prestations attendues pour réaliser les commandes Supply, sous forme de commandes de service (Service Orders), avec biens, destinataires, résultats et opérations nécessaires, sans recréer leur autorisation commerciale. | Rendre le besoin compréhensible et exploitable par l’exécutant. | En cours d’instruction |
| D07.b | Execution Commitment Management | En cours d’instruction | qualifier prise en charge, portée, validité et effets des refus, retraits ou révisions. | Savoir quelle réalisation est effectivement engagée et quelle charge elle mobilise. | En cours d’instruction |
| D07.c | Execution Reconciliation | En cours d’instruction | Rapprocher les faits de production, expédition, réception ou consommation des prestations attendues et qualifier leurs écarts ; fournir ces résultats au rapprochement de l’Order sans se substituer à son reliquat. | Donner aux autres domaines des faits utilisables et expliquer les écarts. | En cours d’instruction |
| D07.d | Expected Supply Tracking | En cours d’instruction | qualifier quantités, dates, provenance et fermeté des résultats de réalisation encore attendus. | Permettre un raisonnement sur les ressources futures avec leurs limites. | En cours d’instruction |

## D09 — Party / Role

Statut : **Validé par l’urbaniste — portée : mastership, name**.

Recevoir les références des parties et leurs rôles métier, distincts des habilitations RBAC. L’identité sans doublon relève du maître externe ; les modèles se relient par identifiants.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D09.d | Party / Role Ingestion | Validé par l’urbaniste — portée : scope | recevoir les parties, leurs identifiants, rôles et relations de référence ainsi que leurs évolutions, en conservant les références du maître externe. | Utiliser une identité de référence commune dans les opérations. | Validé par l’urbaniste — portée : source_id, target_id, type |

## D11 — Agreement

Statut : **Validé par l’urbaniste — portée : mastership, name**.

Recevoir et consulter la projection du contrat complet : cadre, conditions particulières, périodes de validité et engagements en quantité ou en valeur, avec identifiants Party et Catalog. Les commandes restent distinctes et consomment les conditions reçues ; administration du contrat maître externe.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D11.a | Agreement Ingestion | Validé par l’urbaniste — portée : scope | Recevoir les contrats clients ou fournisseurs et leurs évolutions, y compris cadre, conditions particulières, périodes et engagements en quantité ou valeur, avec références Party et Catalog et provenance du maître externe. | Mettre les conditions contractuelles de référence à disposition des décisions et engagements transactionnels. | Validé par l’urbaniste — portée : source_id, target_id, type |

## D08 — Product Reference

Statut : **Proposé par l’IA**.

Recevoir les références Product et leurs Product Variants depuis leurs maîtres externes, indépendamment des catalogues qui les proposent. Product porte un rôle Article ou Container. Distinguer ces références des Product Units, exemplaires physiques suivis dans les opérations ; les identifiants commerciaux ne constituent pas à eux seuls leur identité individuelle.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D08.d | Product Reference Ingestion | Validé par l’urbaniste — portée : scope | Recevoir les références Product, leurs variantes, rôles, identifiants et caractéristiques utiles ainsi que leurs évolutions depuis les maîtres externes, indépendamment de leur présence dans les catalogues. | Reconnaître les mêmes références produit dans les différents catalogues et opérations, sans les confondre avec les exemplaires physiques. | Validé par l’urbaniste — portée : source_id, target_id, type |

## D12 — Catalog

Statut : **Validé par l’urbaniste — portée : mastership, name**.

Recevoir les catalogues construits à l’extérieur et les informations commerciales applicables. Une même référence de produit ou de variante peut figurer dans plusieurs catalogues ; son identité maîtresse relève de Product Reference.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D12.a | Catalog Ingestion | Validé par l’urbaniste — portée : scope | recevoir les catalogues construits à l’extérieur, leurs références de produits, prix, zones géographiques d’application et évolutions. | Permettre de commander et d’utiliser les informations commerciales reçues. | Validé par l’urbaniste — portée : source_id, target_id, type |

## D13 — Fulfillment Network

Statut : **Validé par l’urbaniste — portée : independence, name**.

Recevoir les points du réseau, leurs caractéristiques et relations de référence et leurs liens aux parties responsables. Les lieux restent distincts des parties ; stocks, charge et acheminement choisi appartiennent aux domaines consommateurs.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D13.a | Fulfillment Network Ingestion | Validé par l’urbaniste — portée : scope | recevoir les points du réseau, leurs caractéristiques de référence, leurs relations et liens vers les parties responsables, ainsi que leurs évolutions depuis les sources maîtresses externes. | Donner aux opérations et décisions une connaissance commune du réseau de réalisation. | Validé par l’urbaniste — portée : source_id, target_id, type |

## Portée des validations

| Repère | Champs adoptés | Champs restant proposés | Décisions |
| --- | --- | --- | --- |
| universe-case | definition, name | Aucun | ADOPT-074 |
| universe-supply | name | definition | ADOPT-056 |
| business-references | name | Aucun | ADOPT-042-LIFECYCLE-r2 |
| D01 | Aucun | definition, finality, name, scope | Aucune |
| D01.f | Aucun | definition, finality, name | Aucune |
| D01.g | name | definition, finality | ADOPT-048-LIFECYCLE-r2 |
| D01.c | Aucun | definition, finality, name | Aucune |
| D01.d | definition, finality, name | Aucun | ADOPT-021-LIFECYCLE-r2 |
| D02.b | name | definition, finality | ADOPT-023-LIFECYCLE-r2 |
| D02.c | name | definition, finality | ADOPT-025-LIFECYCLE-r2 |
| D03 | name | definition, finality | ADOPT-058 |
| D03.a | finality, name, nature | definition | ADOPT-059 |
| D03.b | definition, finality, name, nature | Aucun | ADOPT-005-LIFECYCLE-r2 |
| D03.c | finality, name, nature | definition | ADOPT-060 |
| D02.e | name, nature | definition, finality | ADOPT-061 |
| D03.i | definition, finality, name, nature | Aucun | ADOPT-064 |
| D03.j | definition, finality, name, nature | Aucun | ADOPT-066 |
| D03.k | definition, finality, name, nature | Aucun | ADOPT-068 |
| D03.l | definition, finality, name, nature | Aucun | ADOPT-070 |
| D03.m | definition, name | finality, nature | ADOPT-072 |
| D04 | name | definition, finality, scope | ADOPT-049 |
| D04.e | definition, name | finality, scope | ADOPT-050 |
| D04.f | definition, name | finality, scope | ADOPT-051 |
| D04.g | definition, name | finality, scope | ADOPT-052 |
| D04.h | definition, name | finality, scope | ADOPT-053 |
| D05 | Aucun | definition, finality, name | Aucune |
| D05.a | Aucun | definition, finality, name | Aucune |
| D05.b | Aucun | definition, finality, name | Aucune |
| D05.c | Aucun | definition, finality, name | Aucune |
| D06 | Aucun | definition, finality, name | Aucune |
| D06.a | Aucun | definition, finality, name | Aucune |
| D06.b | Aucun | definition, finality, name | Aucune |
| D06.c | Aucun | definition, finality, name | Aucune |
| D07 | Aucun | definition, finality, name, scope | Aucune |
| D07.a | Aucun | definition, finality, name | Aucune |
| D07.b | Aucun | definition, finality, name | Aucune |
| D07.c | Aucun | definition, finality, name | Aucune |
| D07.d | Aucun | definition, finality, name | Aucune |
| D09 | mastership, name | definition, finality | ADOPT-027-LIFECYCLE-r2 |
| D09.d | scope | definition, finality, name | ADOPT-032-LIFECYCLE-r2 |
| D11 | mastership, name | definition, finality | ADOPT-054 |
| D11.a | scope | definition, finality, name | ADOPT-055 |
| D08 | Aucun | definition, finality, independence, name | Aucune |
| D08.d | scope | definition, finality, name | ADOPT-062 |
| D12 | mastership, name | definition, finality | ADOPT-063 |
| D12.a | scope | definition, finality, name | ADOPT-036-LIFECYCLE-r2 |
| D13 | independence, name | definition, finality | ADOPT-031-LIFECYCLE-r2 |
| D13.a | scope | definition, finality, name | ADOPT-040-LIFECYCLE-r2 |

Les validations contextuelles et les réserves détaillées restent dans les décisions et les sources JSON.

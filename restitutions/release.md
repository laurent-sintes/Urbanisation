# Release — 2026-09-13.2

Restitution générée depuis le JSON, connaissance au 2026-09-13. Ne pas éditer cette vue pour modifier le modèle.

Publication et validation sont distinctes. Le statut d’un rattachement peut différer de celui de la capacité.

## D01 — Inventory Management

Statut : **Partiellement validé**.

Connaître les stocks et les ressources attendues, expliquer leurs variations, fiabiliser les quantités et préserver les usages par les protections et réservations. Le stock futur est connu ici et mobilisé par Order Promising.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D01.a | Establish inventory positions | En réexamen | déterminer les quantités de stock physique et leurs états logiques par article, lieu, détenteur et propriétaire lorsque ces dimensions sont pertinentes, en distinguant les ressources futures attendues. | Disposer d’une connaissance exploitable des ressources. | Non validé |
| D01.b | Record inventory facts | Non validé | qualifier les faits qui font évoluer les quantités physiques et les états logiques, notamment entrées, sorties, changements d’état et consommations. | Expliquer les variations et leur provenance. | Non validé |
| D01.c | Provide a consolidated inventory view | Non validé | présenter les positions physiques, leurs états logiques et les ressources futures connues dans une vue cohérente, sans double comptage, avec source, périmètre et fraîcheur. | Permettre une lecture commune des stocks distribués. | Non validé |
| D01.d | Stocktaking | Partiellement validé | établir les quantités constatées par comptage, les confronter aux quantités enregistrées, qualifier les écarts et établir les corrections justifiées. | Fiabiliser les quantités enregistrées — Inventory accuracy. | Validé |
| D02.b | Supply Protection | Partiellement validé | établir et appliquer les quantités ou limites d’usage destinées à des groupes, avec leur validité. | Préserver les possibilités d’approvisionnement des usages retenus. | Validé |
| D02.c | Reservation | En réexamen | établir un engagement de quantité pour un besoin identifié, dont les usages concurrents doivent tenir compte. | Donner effet à un engagement de ressource. | En réexamen |

## D02 — Resource Availability and Commitments

Statut : **En réexamen**.

Deux aptitudes de disponibilité et d’ajustement subsistent comme traces de travail après les rattachements de Supply Protection et Reservation à Inventory Management, et de Supply Assignment à Order Promising.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D02.a | Determine resource availability for a given use | En réexamen | apprécier les quantités admissibles à un horizon, compte tenu des états, attentes, protections et engagements. | Évaluer ce qui peut être mobilisé dans une situation donnée. | Non validé |
| D02.d | Adjust resource commitments | En réexamen | réviser, transférer ou libérer les quantités affectées selon les décisions autorisées. | Maintenir des affectations cohérentes avec les besoins et les ressources. | Non validé |

## D03 — Order Promising

Statut : **Partiellement validé**.

Établir ce qui peut être promis pour satisfaire une demande, sous quelles conditions, avec quelles ressources et quelle solution de fourniture, puis maintenir la promesse lorsque la situation évolue.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D03.a | Promise Proposal | Validé | construire une proposition de fourniture précisant quantités, dates, conditions et alternatives possibles, à partir des ressources et possibilités de réalisation. | Faire naître une proposition de promesse réalisable. | Validé |
| D03.b | Promise Confirmation | Validé | établir les quantités et dates promises, en distinguant la part confirmée de celle qui ne l’est pas. | Donner un engagement explicite au destinataire. | Validé |
| D02.e | Supply Assignment | Validé | affecter, réaffecter ou libérer des ressources admissibles présentes ou futures pour couvrir des demandes ou engagements. | Assurer la couverture des demandes par des ressources identifiées. | Validé |
| D03.c | Promise Revision | Validé | réexaminer les promesses lorsque ressources, demandes, dates ou priorités changent et établir les modifications autorisées. | Maintenir des engagements cohérents avec la situation et les priorités applicables. | Validé |
| D03.d | Allocation Eligibility Decision | Validé | décider quelle quantité une demande peut consommer au regard des allocations, protections et droits applicables. | Respecter les droits d’accès aux ressources. | Validé |
| D03.e | Fulfillment Source Decision | Validé | choisir la source ou la combinaison de sources permettant de satisfaire la demande. | Fonder la promesse sur des origines de fourniture admissibles. | Validé |
| D03.f | Fulfillment Route Decision | Validé | choisir la chaîne d’acheminement jusqu’à destination : étapes, points de passage, modes et services, selon les contraintes de délai, de capacité et de coût. | Fonder la promesse sur un acheminement réalisable. | Validé |
| D03.g | Product Substitution Decision | Validé | décider quel produit de remplacement est admissible pour satisfaire la demande dans les conditions autorisées. | Permettre une réponse acceptable lorsque le produit demandé ne peut pas être fourni tel quel. | Validé |
| D03.h | Supply Creation Decision | Validé | décider de recourir à une fourniture nouvelle et qualifier les conditions nécessaires pour fonder la promesse. | Rendre possible une fourniture que les ressources déjà présentes ou attendues ne permettent pas de satisfaire. | Validé |

## D04 — Commercial Commitments

Statut : **En réexamen**.

Examiner qui s’engage à fournir ou acquérir quoi, sous quelles conditions reçues, et les obligations restantes après modification, livraison ou retour. Les commandes restent distinctes des Agreements de référence.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D04.a | Establish a commercial commitment | En réexamen | établir l’engagement propre à une commande, avec parties, biens ou prestations, quantités, conditions applicables et degré de fermeté. | Disposer d’une référence sur ce qui est commandé et engagé. | Non validé |
| D04.b | Amend commercial obligations | En réexamen | modifier ou éteindre les engagements d’une commande selon les conditions applicables, en conservant leur histoire. | Faire évoluer les obligations transactionnelles et leurs effets. | Non validé |
| D04.c | Determine commitment fulfillment and remaining obligations | En réexamen | rapprocher les obligations d’une commande des réalisations et corrections qui lui sont imputables. | Connaître les obligations encore ouvertes. | Non validé |
| D04.d | Authorize a return or replacement | En réexamen | décider de l’autorisation et des obligations correctives applicables à une commande selon les conditions reçues et les faits. | Donner effet à une solution commerciale admissible après fourniture. | Non validé |

## D05 — Operational Resource Balancing

Statut : **Non validé**.

Établir les objectifs de couverture, les besoins nets et les redistributions utiles à l’équilibrage opérationnel. Le dossier Demande de réassort appartient au modèle processus ; calculer un besoin ne promet ni ne réalise un transfert.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D05.a | Determine operational coverage targets | Non validé | établir niveaux et seuils applicables par ressource et périmètre. | Donner une référence au renouvellement opérationnel des stocks. | Non validé |
| D05.b | Determine net resource requirements | Non validé | identifier les manques ou excédents en tenant compte des positions, besoins et approvisionnements attendus pertinents. | Former un besoin justifié sans ignorer les ressources déjà attendues. | Non validé |
| D05.c | Determine resource redistribution | Non validé | proposer les quantités et destinations permettant de traiter des déséquilibres selon les contraintes. | Rééquilibrer les ressources lorsque leur distribution devient inadaptée. | Non validé |

## D06 — Execution Options

Statut : **Non validé**.

Utiliser les références du réseau et les contraintes opérationnelles pour apprécier les possibilités concrètes de réalisation et les options compatibles avec un besoin.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D06.a | Qualify locations and feasible services | Non validé | connaître les lieux, leurs rôles opérationnels et les prestations qui y sont admissibles. | Identifier les possibilités concrètes de réalisation. | Non validé |
| D06.b | Determine available execution capacity | Non validé | apprécier limites applicables, charge engagée et capacité restante pour une prestation et une période. | Éviter de confondre disponibilité d’article et possibilité de le servir. | Non validé |
| D06.c | Determine eligible execution options | Non validé | établir et comparer les origines ou prestations compatibles avec un résultat attendu. | Éclairer un choix réalisable selon les critères autorisés. | Non validé |

## D07 — Execution Commitments and Facts

Statut : **En réexamen**.

Exprimer le besoin de prestation, suivre les engagements d’exécution, rattacher les résultats et écarts aux attentes, et qualifier les ressources encore attendues.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D07.a | Formalize a service requirement | En réexamen | exprimer biens, destinataire, résultat et opérations nécessaires à une réalisation. | Rendre le besoin compréhensible et exploitable par l’exécutant. | Non validé |
| D07.b | Establish and adjust execution commitments | En réexamen | qualifier prise en charge, portée, validité et effets des refus, retraits ou révisions. | Savoir quelle réalisation est effectivement engagée et quelle charge elle mobilise. | Non validé |
| D07.c | Qualify execution results and discrepancies | En réexamen | rattacher constats de production, expédition, réception ou consommation au résultat attendu. | Donner aux autres domaines des faits utilisables et expliquer les écarts. | Non validé |
| D07.d | Identify and qualify expected resources | En réexamen | qualifier quantités, dates, provenance et fermeté des résultats de réalisation encore attendus. | Permettre un raisonnement sur les ressources futures avec leurs limites. | Non validé |

## D09 — Party / Role

Statut : **Partiellement validé**.

Recevoir les références des parties et leurs rôles métier, distincts des habilitations RBAC. L’identité sans doublon relève du maître externe ; les modèles se relient par identifiants.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D09.d | Party / Role Ingestion | Partiellement validé | recevoir les parties, leurs identifiants, rôles et relations de référence ainsi que leurs évolutions, en conservant les références du maître externe. | Utiliser une identité de référence commune dans les opérations. | Validé |

## D11 — Agreement

Statut : **Partiellement validé**.

Recevoir les Agreements, les identités Party, les catalogues permettant de commander et les conditions particulières utiles à Order Promising. Les commandes transactionnelles restent distinctes des contrats de référence.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D11.a | Agreement Ingestion | Partiellement validé | recevoir les contrats fournisseurs ou clients, leurs références Party et Catalog, leurs conditions particulières et leurs évolutions depuis les applications maîtres externes. | Mettre les conditions contractuelles de référence à disposition des décisions et engagements transactionnels. | Validé |

## D08 — Product Reference

Statut : **Partiellement validé**.

Reconnaître les mêmes articles par leur référence SKU indépendamment des catalogues qui les proposent. La référence article est reçue depuis un maître externe.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D08.d | Product Reference Ingestion | Partiellement validé | recevoir les articles, leurs identifiants SKU, caractéristiques de référence utiles et évolutions depuis leur maître externe, indépendamment de leur présence dans les catalogues. | Reconnaître les mêmes articles dans les différents catalogues et opérations. | Validé |

## D12 — Catalog

Statut : **Partiellement validé**.

Recevoir les catalogues construits à l’extérieur et les informations commerciales applicables. Un même SKU peut figurer dans plusieurs catalogues ; son identité maîtresse relève de Product Reference.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D12.a | Catalog Ingestion | Partiellement validé | recevoir les catalogues construits à l’extérieur, leurs références de produits, prix, zones géographiques d’application et évolutions. | Permettre de commander et d’utiliser les informations commerciales reçues. | Validé |

## D13 — Fulfillment Network

Statut : **Partiellement validé**.

Recevoir les points du réseau, leurs caractéristiques et relations de référence et leurs liens aux parties responsables. Les lieux restent distincts des parties ; stocks, charge et acheminement choisi appartiennent aux domaines consommateurs.

| Repère | Capacité | Statut | Définition | Finalité | Rattachement |
| --- | --- | --- | --- | --- | --- |
| D13.a | Fulfillment Network Ingestion | Partiellement validé | recevoir les points du réseau, leurs caractéristiques de référence, leurs relations et liens vers les parties responsables, ainsi que leurs évolutions depuis les sources maîtresses externes. | Donner aux opérations et décisions une connaissance commune du réseau de réalisation. | Validé |

## Portée des validations

| Repère | Champs adoptés | Champs restant proposés | Décisions |
| --- | --- | --- | --- |
| business-references | name | Aucun | ADOPT-042 |
| D01 | name, scope | definition, finality | ADOPT-001 |
| D01.a | Aucun | definition, finality, name | Aucune |
| D01.b | Aucun | definition, finality, name | Aucune |
| D01.c | Aucun | definition, finality, name | Aucune |
| D01.d | definition, finality, name | Aucun | ADOPT-021 |
| D02.b | name | definition, finality | ADOPT-023 |
| D02.c | name | definition, finality | ADOPT-025 |
| D02 | Aucun | definition, finality, name | Aucune |
| D02.a | Aucun | definition, finality, name | Aucune |
| D02.d | Aucun | definition, finality, name | Aucune |
| D03 | name | definition, finality | ADOPT-002 |
| D03.a | definition, finality, name, nature | Aucun | ADOPT-003 |
| D03.b | definition, finality, name, nature | Aucun | ADOPT-005 |
| D02.e | definition, finality, name, nature | Aucun | ADOPT-007 |
| D03.c | definition, finality, name, nature | Aucun | ADOPT-009 |
| D03.d | definition, finality, name, nature | Aucun | ADOPT-011 |
| D03.e | definition, finality, name, nature | Aucun | ADOPT-013 |
| D03.f | definition, finality, name, nature | Aucun | ADOPT-015 |
| D03.g | definition, finality, name, nature | Aucun | ADOPT-017 |
| D03.h | definition, finality, name, nature | Aucun | ADOPT-019 |
| D04 | Aucun | definition, finality, name | Aucune |
| D04.a | Aucun | definition, finality, name | Aucune |
| D04.b | Aucun | definition, finality, name | Aucune |
| D04.c | Aucun | definition, finality, name | Aucune |
| D04.d | Aucun | definition, finality, name | Aucune |
| D05 | Aucun | definition, finality, name | Aucune |
| D05.a | Aucun | definition, finality, name | Aucune |
| D05.b | Aucun | definition, finality, name | Aucune |
| D05.c | Aucun | definition, finality, name | Aucune |
| D06 | Aucun | definition, finality, name | Aucune |
| D06.a | Aucun | definition, finality, name | Aucune |
| D06.b | Aucun | definition, finality, name | Aucune |
| D06.c | Aucun | definition, finality, name | Aucune |
| D07 | Aucun | definition, finality, name | Aucune |
| D07.a | Aucun | definition, finality, name | Aucune |
| D07.b | Aucun | definition, finality, name | Aucune |
| D07.c | Aucun | definition, finality, name | Aucune |
| D07.d | Aucun | definition, finality, name | Aucune |
| D09 | mastership, name | definition, finality | ADOPT-027 |
| D09.d | scope | definition, finality, name | ADOPT-032 |
| D11 | mastership, name | definition, finality | ADOPT-028 |
| D11.a | scope | definition, finality, name | ADOPT-034 |
| D08 | independence | definition, finality, name | ADOPT-030 |
| D08.d | scope | definition, finality, name | ADOPT-038 |
| D12 | mastership, name | definition, finality | ADOPT-029 |
| D12.a | scope | definition, finality, name | ADOPT-036 |
| D13 | independence, name | definition, finality | ADOPT-031 |
| D13.a | scope | definition, finality, name | ADOPT-040 |

Les validations contextuelles et les réserves détaillées restent dans les décisions et les sources JSON.

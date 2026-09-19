# D03 — proposition de structuration après U437

**État historique de la proposition, remplacé par les choix U438/U445.** Les deux domaines frères sont désormais intégrés ; voir le [rapport des modifications finales](modifications.md). Les comparaisons et le raisonnement ci-dessous expliquent la proposition présentée avant adoption.

Le défaut principal de D03 est sa réunion de trois problèmes : établir et tenir une promesse, arbitrer la satisfaction des demandes, puis structurer et conserver les Orders. Le carnet reste une vue de travail utile ; il ne suffit pas à définir une responsabilité de domaine.

Cette note explique la [proposition structurée](../../modeles/backlog/d03-domain-review-U437.yaml). Le [catalogue courant](../../modeles/backlog/model.yaml) conserve les noms et rattachements adoptés tant que Laurent n’a pas arbitré. Les corrections éditoriales appliquées sont détaillées plus bas.

## Proposition à arbitrer

| Domaine proposé | Responsabilité directrice | Capacités concernées |
| --- | --- | --- |
| **Order Promising** | Établir ce qui peut être promis, sous quelles conditions, puis maintenir les propositions et engagements | ATP, CTP, PTP, Delivery Schedule Decision, Promise Management |
| **Fulfillment Optimization** — conserver D03 proposé | Arbitrer la satisfaction des Orders sous contraintes, déterminer un plan cohérent et matérialiser les affectations retenues | Order Prioritization, Fulfillment Plan Decision, Order Backlog Planning, Supply Assignment |
| **Order Management** — D04 existant | Tenir les demandes, leur structure et leur historique | Y rattacher Order Structuring et Order Archiving, en complément des capacités actuelles |

La proposition garde toutes les capacités et tous les comportements. Elle ne crée pas un troisième niveau dans l’arbre. Un éventuel nom **Fulfillment Planning** pour Order Backlog Planning reste une piste lexicale à arbitrer, sans consensus marché revendiqué. Aucun identifiant n’est attribué au domaine supplémentaire avant adoption.

**Bénéfice :** rendre visibles la responsabilité de l’engagement et celle du choix de satisfaction. **Compromis :** ces domaines doivent échanger des possibilités, des arbitrages et des engagements compatibles ; leur séparation ne supprime pas leurs dépendances.

L’alternative consiste à garder les neuf capacités dans **Fulfillment Optimization**, avec les mêmes deux déplacements vers D04. Elle simplifie la carte, mais rend moins visible la responsabilité transactionnelle de maintien des promesses. Renommer seulement le domaine en conservant ses onze capacités ne traite pas le problème.

## Recouvrements qui demandent un traitement explicite

| Capacités | Résultats à distinguer | Risque actuel |
| --- | --- | --- |
| ATP / CTP et Delivery Schedule Decision | Possibilités réalisables ; échéancier retenu | Trois décisions donnant l’impression de choisir les mêmes quantités et dates |
| PTP et Fulfillment Plan Decision | Choix économique contextualisé ; compromis final multidimensionnel | Deux autorités finales sur le scénario ; élimination économique implicite d’une alternative utile à un autre objectif |
| Order Backlog Planning et Fulfillment Plan Decision | Organisation des hypothèses, simulations et scénarios ; décision de cohérence des affectations | Deux responsabilités décrites comme la construction et la sélection d’un même plan |
| Fulfillment Plan Decision et Supply Assignment | Choix d’affectation ; liens effectivement matérialisés | L’action d’affecter revendique à nouveau l’optimisation |
| Fulfillment Plan Decision et Promise Management | Plan de satisfaction ; proposition ou engagement autorisé | Une solution proposée prise pour un engagement, ou deux solutions concurrentes |

Les décisions fines restent utiles conformément à U328/U329. Leur justification exige un résultat métier et une autorité identifiables : les répartir dans deux domaines ne suffit pas. Les règles de compatibilité PTP/échéancier/plan doivent être précisées avant de considérer leurs contrats comme achevés. Cette proposition n’attribue pas un poids économique ou une priorité implicite.

Exemple fictif : pour une demande de 100 pièces, ATP établit ce qui est réalisable sans adaptation et CTP les alternatives conditionnelles. Les arbitrages peuvent retenir 60 vendredi et 40 lundi, en tenant compte des autres demandes. Le plan précise les ressources correspondantes ; Supply Assignment matérialise les liens ; Promise Management porte la proposition et sa confirmation autorisée. Deux échéances ne créent pas automatiquement deux Orders. **Seule Reservation bloque les usages concurrents** (U436).

La séparation ne repose pas sur « individuel contre collectif » : ATP peut considérer plusieurs demandes et une optimisation une seule. Il ne s’agit pas non plus d’une séquence d’appels obligatoire ou d’un découpage logiciel.

## Ce que le marché étaye

Sources officielles effectivement consultées le 19 septembre 2026 ; les correspondances proposées sont aussi enregistrées sur D03.

- **SAP** présente le Backorder Processing dans Order Promising : les changements de disponibilités et de priorités conduisent à réexaminer les confirmations. Cela montre un périmètre plus large que le seul calcul ATP. [SAP Learning — Exploring Backorder Processing](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/exploring-backorder-processing_fed6ddd5-39be-41ab-a977-e41a1c3715fe).
- **Microsoft** décrit DOM comme une solution d’order fulfillment optimization, orientée choix des sources et arbitrage de contraintes et d’objectifs. [Microsoft Learn — Distributed order management](https://learn.microsoft.com/en-us/dynamics365/commerce/dom).
- **Microsoft emploie aussi Order promising**, pour les possibilités de dates et de disponibilité, notamment ATP/CTP. Les deux termes ne constituent donc pas une opposition SAP/Microsoft. [Microsoft Learn — Order promising](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations).
- **Oracle** décrit Backlog Planning comme un traitement de replanification des demandes. Cela étaye une pratique de travail du carnet ; cette source ne constitue pas un modèle de domaines d’entreprise. [Oracle 26B — Start Backlog Planning](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspc/start-backlog-planning.html).

Ces documents décrivent des fonctions et périmètres produits, principalement dans des contextes de vente et de transfert. Ils n’imposent ni deux domaines FLOW, ni une généralisation identique à tous les types d’Order, ni un changement de la règle U436. La scission recommandée est une proposition de cohérence métier FLOW, pas une architecture SAP ou Microsoft importée.

## Modifications effectivement réalisées

- Contribution U437 enregistrée avec son verbatim et sa portée.
- **D03 :** définition et périmètre alignés sur U420 : il prépare la satisfaction et mobilise Lifecycle pour l’autorisation de prise en charge. La note de revue périmée est actualisée.
- **Supply Assignment :** définition et finalité recentrées sur la matérialisation et le maintien des affectations retenues. L’optimisation collective reste portée par Fulfillment Plan Decision, déjà introduite en U378.
- Trois rapprochements marché proposés ajoutés à D03 ; options et arbitrages consignés dans l’annexe YAML.
- Aucun changement de nom, parent, relation ou principe. Les **570 valeurs validées** antérieures et leurs empreintes sont préservées. La structure conserve **47 capacités et 74 comportements**.

L’état antérieur est conservé dans [model-before-U437.yaml](model-before-U437.yaml). Les modifications structurelles attendent l’arbitrage demandé au titre des problèmes complexes de U435. Aucun contenu publié n’est modifié.

# Operational Resource Balancing / Order Promising

**Application U219–U221 :** les finalités D01/D03/D05 sont actualisées dans le backlog. D05 s’appelle désormais **Inventory Optimization**, selon U220 ; réapprovisionnement automatique envisagé dans son périmètre proposé U221. Les trois capacités sont conservées et précisées autour du stock. Voir [les descriptions courantes](../connaissance/30-stock-et-orders.md). Les analyses ci-dessous retracent la discussion avant cette mise à jour.

15 septembre 2026 — U217. Lecture des champs et relations du [backlog courant](../modeles/backlog/model.yaml), des réserves D05 et de la recomposition D03 U154/U163. Analyse locale, sans nouvelle affirmation sur un produit du marché. Aucun changement du modèle.

## Clarification courante U218

Laurent précise : « D03 tente d'assouvir les orders. D05 tente de gérer le stock ». La frontière est désormais guidée par l'objet et la finalité : satisfaction des Orders dans D03, gestion du stock dans D05. La lecture besoin/solution ci-dessous est une analyse antérieure et ne suffit pas à définir cette frontière.

Interprétation proposée : D05 cherche les niveaux et la répartition souhaitables du stock, puis les ajustements nécessaires ; D03 cherche une solution permettant de satisfaire les Orders, quitte à proposer des adaptations de ressources dans le CTP. Un transfert peut être envisagé pour rééquilibrer le stock ou pour satisfaire une commande ; la ressemblance de l'opération ne suffit pas à fusionner les responsabilités. La recommandation U217 de réexaminer D05.c demeure un examen de frontière, sans présumer son retrait.

D01 conserve ses responsabilités existantes de représentation et fiabilisation du stock, mouvements, visibilité, inventaire, protection et réservation. Cette liste ne réduit pas Inventory Management à une observation passive. L'articulation D01/D05, les objectifs détaillés de D05 et leurs autorités restent à préciser. Aucun changement des définitions canoniques, des validations antérieures ou de la publication v005 par cette prise de note.

## Différence de résultat proposée pour la lecture

| Domaine | Question principale | Résultats actuellement décrits |
| --- | --- | --- |
| D05 Operational Resource Balancing | De quoi manque-t-on, où, et par rapport à quel objectif ? | Niveaux/seuils de couverture, besoins nets ou excédents, propositions de redistribution. |
| D03 Order Promising | Comment couvrir une demande et que peut-on s’engager à fournir ? | Solutions ATP/CTP, comparaison PTP, affectations, priorités, échéancier et promesses proposées/confirmées/révisées. |

La distinction est analytique et reste à éprouver. D05 ne se limite pas nécessairement à une étape antérieure à toute commande ; D03 ne traite pas seulement une commande isolée. Supply Assignment couvre aussi des besoins prévisionnels, Order Prioritization arbitre entre commandes, et le CTP local peut proposer de modifier les engagements envers d’autres commandes. Éviter une frontière artificielle collectif/individuel, prévisionnel/ferme ou court/long terme. La planification de saison reste hors de D05 dans les textes actuels.

## Recouvrements

| Zone | Constat sur le contenu courant | Frontière de travail proposée |
| --- | --- | --- |
| D05.a / CTP et protections | Les objectifs de couverture et les protections contraignent l’emploi des ressources. Le CTP peut proposer des changements de protection. | Une cible de stock ou de couverture n’est pas un droit de consommation ou une quantité protégée. Préciser la nature des objectifs D05.a et l’autorité de leur modification. |
| D05.b / ATP, CTP, Supply Assignment | Les capacités confrontent positions, besoins, ressources attendues et admissibilité. Supply Assignment inclut les besoins prévisionnels. | D05.b produit le besoin net à traiter ; D03 produit une solution de couverture et, le cas échéant, une promesse. Des calculs communs ne suffisent ni à prouver deux aptitudes ni à imposer deux moteurs. |
| D05.c / CTP, Supply Assignment et choix de source | Proposer des quantités et destinations pour corriger un déséquilibre rejoint la conception d’un plan d’adaptation et la réaffectation des ressources. Le CTP local est explicitement large. | Point de recouvrement le plus fort : distinguer l’objectif de redistribution souhaité de la sélection d’une solution réalisable avec ses sources, dates, engagements et impacts. Si D05.c porte déjà cette dernière décision complète, sa responsabilité fait doublon. |

Les relations transversales D03/D05 ne sont pas formalisées dans le graphe courant. L’analyse ne crée donc pas un lien métier adopté ni un ordre de processus obligatoire.

## Exemple fictif

Un magasin vise 100 pièces ; 30 sont disponibles et 20 supplémentaires sont attendues et admissibles sur l’horizon considéré. En supposant que la cible exprime tout le besoin pertinent et qu’il n’y ait pas d’autres demandes ou restrictions à déduire, D05.b établit un complément de 50. Ce calcul simplifié n’est pas une formule universelle.

D03 examine comment servir ces 50 : ressource disponible dans un entrepôt, arrivage futur, transfert depuis un autre site, contraintes de protection et commandes concurrentes. Il peut proposer puis confirmer 30 pièces mardi et 20 vendredi, ou un autre scénario. Le type d’Order résultant et son autorité ne sont pas déduits automatiquement de l’exemple.

D04 gère l’ordre et ses transformations/progression selon la refonte U214. D07 et Services portent les prestations et leurs réalisations. Un scénario CTP peut conduire à réexaminer le besoin ou les objectifs : cette lecture n’impose pas une chaîne à sens unique.

## Avis proposé, non adopté

Conserver pour l’instant la distinction entre besoin/objectif de rééquilibrage et solution de couverture/promesse. Examiner D05.c en premier : son résultat doit être distinct des plans CTP et des affectations ; sinon son maintien comme aptitude autonome n’est pas justifié. Clarifier D05.b en parallèle pour ne pas dupliquer un calcul générique de couverture déjà mobilisé dans D03.

Le nom Operational Resource Balancing demeure large au regard de capacités surtout décrites autour du renouvellement des stocks et du rééquilibrage. La frontière et le libellé pourront être précisés après cet examen ; aucune fusion ou nouvelle nomenclature n’est adoptée par U217.

Sources locales : U154/U163, définitions courantes D03 et D05, [récits D05](../connaissance/25-domaines-coeur-et-epreuve-recits.md), [corrections](../connaissance/04-corrections.md). D05 reste proposé ; cette analyse n’étend pas les validations D03.

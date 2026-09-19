# Supply Assignment : convention de vocabulaire FLOW

17 septembre 2026 — U289 ; correction C93. Convention de travail stabilisée sous mandat utilisateur, fondée sur Assignment déjà retenu U275. Les formulations détaillées restent éditoriales ; aucune équivalence universelle de marché revendiquée.

## Conclusion

**Le besoin n’a pas changé : affecter des ressources contraintes aux commandes. Supply Assignment est le terme retenu.** La confusion venait de l’alternance de Codex entre enveloppes de groupes, affectations aux commandes et répartition magasin.

## Marché

| Source | Sens documenté | Limite |
| --- | --- | --- |
| [SAP — Explaining Supply Assignment](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4) | ARun affecte les ressources aux besoins de commandes en pénurie ; stocks présents et futurs sont distingués. | SAP conserve le nom ARun et le vocabulaire allocated ; pas un algorithme optimal universel ni un catalogue de capacités FLOW. |
| [SAP — Explaining aATP Product Allocation (PAL)](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-aatp-product-allocation-pal-_dd30c229-d63f-4aba-a950-a174280c4a58) | PAL limite la consommation de groupes de demandes ; disponibilité et ARun respectent ces limites. | PAL ne signifie pas le même résultat que Supply Assignment. |
| [Microsoft — Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation) | Enveloppes affectées à des groupes avant les commandes, avec protection et contrôle de surconsommation. | Pas synonyme de l’affectation à des commandes identifiées. |
| [Oracle — Retail Allocation Cloud Service / Allocation Overview](https://docs.oracle.com/en/industries/retail/retail-allocation-cloud/latest/ralim/allocation-overview.htm) | Allocation au niveau des lieux selon leurs besoins, pouvant utiliser stock entrepôt ou apports attendus. | Autre acception d’allocation ; ne pas la confondre avec affectation à des commandes déjà identifiées. |

Le libellé ARun et le verbe allocated restent présents dans la documentation SAP. Ils n’annulent pas le nom Supply Assignment ni la différence avec Product Allocation. Le mot allocation seul ne permet donc pas d’identifier le mécanisme.

## Convention FLOW

**Supply Assignment — Affectation des ressources aux commandes**

Affecter les ressources Supply présentes ou futures aux commandes identifiées, selon les priorités, les engagements et les contraintes applicables, afin d’en assurer la meilleure satisfaction possible.

**Supply Assignment Plan — Plan d’affectation des ressources aux commandes**

Ensemble cohérent d’affectations proposées ou retenues précisant les ressources, quantités et dates destinées aux commandes d’un périmètre, avec les hypothèses et contraintes applicables.

- Employer Supply Assignment / affectation pour les ressources destinées aux commandes ; pas Allocation comme synonyme dans les libellés FLOW.
- Employer plan d’affectation, sans alterner avec plan d’allocation.
- Pour les droits de groupes : enveloppes de protection, droits d’usage ou plafonds de consommation selon le résultat.
- Répartition et distribution sont des verbes descriptifs ; toujours préciser entre quoi et quoi, pas de concepts concurrents.
- Allocation reste un terme éditeur ou historique qualifié : SAP PAL, Microsoft Inventory Allocation, Oracle Retail Allocation, ancien Order Allocation Run.
- Optimiser la satisfaction des commandes est la finalité ; l’objectif exact dépend de priorités, service, coûts et engagements, pas du seul volume confirmé.

## Ce qui reste distinct

- **protection** : Configure les droits et contraintes des groupes ; ne choisit pas la ressource de chaque Order.
- **assignment** : Matérialise et maintient le lien ressources ↔ commandes ; mobilise les arbitrages spécialisés selon le modèle.
- **reservation** : Effet d’engagement sur les usages concurrents ; peut être porté par la même affectation, articulation toujours à arbitrer sans double déduction.
- **promising** : Établit les possibilités et gouverne les engagements quantité/date ; affecté, réservé et promis restent distincts.
- **order_management** : Applique les changements d’Orders autorisés issus du plan ; ne devient pas implicitement propriétaire du lien d’affectation.
- **execution** : Réalise et suit les prestations ; affectation ne prouve pas mouvement physique.

Exemple fictif : 100 pièces disponibles pour deux commandes demandant 80 chacune. Un plan retient 60 pour la première et 40 pour la seconde selon les priorités. Cette affectation ne prouve ni confirmation de promesse ni mouvement physique. Une protection de groupe pourrait en amont restreindre les quantités admissibles.

## Conséquences pour la refonte

Le mécanisme d’application dans D04 concerne les conséquences sur les Orders. Le lien ressource-commande demeure Supply Assignment dans le modèle courant. Un plan peut changer les affectations sans changer les Orders : ne pas déduire automatiquement créations de transferts ou nouvelle capacité D04.

Le nom courant Stock Allocation Decision concerne les groupes. La cible propose **Group Protection Decision**, à périmètre inchangé, pour supprimer cette ambiguïté. Le nom adopté du catalogue actif n’a pas été changé par cette étude.

Le périmètre historique Supply Assignment couvre aussi d’autres besoins identifiés, dont prévisionnels. Aucune suppression implicite de cette extension ; finalité et cas commandes stabilisés ici.

## Traçabilité

Sources complètes : [annexe terminologique](../modeles/backlog/assignment-terminology.yaml). Cible complète : [refonte U286](../audits/2026-09-17-refonte-modele/rapport.md). Capture avant correction : audits/2026-09-17-vocabulaire-affectation/.

T1 — Cours S/4HANA Fashion évolutif sans édition unique ; Supply Assignment: Basics ; Supply Assignment (ARun) ; consulté 2026-09-17.
T2 — Cours évolutif sans édition unique ; PAL Concept ; Advanced ATP and Supply Assignment ; consulté 2026-09-17.
T3 — Page évolutive ; Business background ; Allocation definition ; consulté 2026-09-17.
T4 — latest, édition de la page non figée ; Allocation Overview ; Item Sources ; Calculation Parameters ; consulté 2026-09-17.


## Application U290

Laurent confirme : la finalité est de **maximiser une valeur multidimensionnelle** sous contraintes. Le volume promis ou la marge seuls ne la résument pas. Service, engagements, coûts et risques sont des critères illustratifs ; aucune pondération universelle n’est adoptée. Les décisions spécialisées de priorité, faisabilité, arbitrage économique et échéancier conservent leurs responsabilités.

Le backlog est maintenant refondu : D05.d porte Group Protection Decision ; les mentions de nom actif conservé plus haut décrivent la situation avant U290. [Bilan de migration](../audits/2026-09-17-refonte-appliquee/rapport.md). La pluralité d’objectifs est cohérente avec [Microsoft IFO](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/ifo-arch) ; le choix des critères FLOW reste propre à notre modèle.

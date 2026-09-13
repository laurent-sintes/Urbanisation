# Degré de détail des fonctions de stock et de promesse

Analyse Codex du 9 septembre 2026, à la suite de [U32](../connaissance/01-contributions-utilisateur.md#u32), F122, A21 et P70. Complément à la [comparaison allocation/réservation](allocation-reservation-sap-microsoft.md) et aux [politiques du périmètre historique de Beaumanoir et de Boardriders](../connaissance/18-politiques-engagement-gbm-brd.md). Correspondance méthodologique CMP024 ; aucune nouvelle capacité locale validée.

## Les fonctions présentées ne sont pas le dernier degré de détail

Les précédentes réponses présentaient surtout les grandes fonctions et leurs finalités. Les documentations SAP et Microsoft précisent leurs objets, règles, variantes, opérations et réalisations. En revanche, cette profondeur fonctionnelle ne constitue pas nécessairement une hiérarchie officielle de sous-capacités métier.

Dans l’extrait SAP RBA consulté, les contrôles de disponibilité et d’allocation apparaissent comme des **Business Capabilities** sous l’aire **Order Promising**. Aucune décomposition native supplémentaire sous ces feuilles n’a été vérifiée ; l’extrait n’est pas le catalogue complet. Il ne place pas automatiquement toutes les fonctions de produit étudiées au même niveau RBA. [S1]

De même, les niveaux du catalogue de processus Microsoft et les groupes paramétrables d’Inventory Visibility ne sont pas des niveaux de capacités. Les détails ci-dessous sont qualifiés selon leur nature.

## Exemples concrets chez Microsoft

| Fonction examinée | Éléments plus fins réellement documentés | Nature des éléments |
| --- | --- | --- |
| Allocation Inventory Visibility | Créer une allocation, la retirer, déplacer des quantités entre groupes, consommer une quantité et consulter les allocations | Opérations exposées par les API [S2] |
| Allocation Inventory Visibility | Groupe bénéficiaire, combinaison de groupes, quantité encore allouable, solde alloué et consommation | Objets et mesures ; hiérarchie de groupes, pas hiérarchie de capacités [S2] |
| Réservation Inventory Visibility | Demander une réservation avec contrôle de quantité disponible, réduire/libérer une réservation, réduire la réservation souple lors du relais avec les états de l’ERP | Opérations et règles d’intégration ; le dernier mécanisme est l’offset [S3] |
| Réservation dans Supply Chain Management | Stock présent ou commandé non reçu ; mode manuel/automatique ; choix selon des critères de lots et de dates | Types de ressources et politiques de réservation [S4] |

La documentation d’allocation distingue aussi l’acte de consommer une enveloppe et la possibilité de produire simultanément une réservation souple. On peut donc étudier précisément les effets d’une opération, au-delà du simple libellé « allocation ». Le terme technique *physical measure* employé par Inventory Visibility peut désigner une mesure d’allocation : il ne signifie pas que toute mesure est un stock physiquement présent. [S2]

La réservation souple possède un contrôle de disponibilité, des dimensions et des règles de compensation. L’offset réduit la quantité réservée dans Inventory Visibility ; il ne signifie pas que la réservation dans l’ERP est annulée. Les versions et paramètres conditionnent les transitions décrites. [S3]

## Exemples concrets chez SAP

| Fonction examinée | Éléments plus fins réellement documentés | Nature des éléments |
| --- | --- | --- |
| Supply Protection — SUP | Objet de protection, groupes définis par caractéristiques, quantités par période, activation ; protection horizontale ou priorisée | Objets, états et variantes de politique [S5] |
| Product Allocation — PAL | Objet d’allocation, combinaisons de caractéristiques, quantités planifiées par période, séquences de contrôles et règles de consommation temporelle | Données, composition des contrôles et règles [S6] |
| Supply Assignment — ARun | Tri des ressources, affectation séquentielle ou proportionnelle, reprise d’affectations existantes, contrôles de libération | Opérations et règles d’affectation [S7] |
| Backorder Processing — BOP | Segments de demandes, variantes, stratégies de confirmation, variantes de secours et exécutions simulées ou planifiées | Objets de configuration, stratégies et modes d’exécution [S8] |

Un objet de protection peut contenir plusieurs groupes ; les groupes portent des quantités et des caractéristiques. Il s’agit d’une structure d’objets métier. Les protections horizontales et priorisées sont des variantes de règles. L’activation et la modification des quantités décrivent un cycle d’utilisation. Ces trois descriptions apportent du détail sans constituer trois étages successifs de capacités. [S5]

De la même manière, une variante BOP regroupe des paramètres d’exécution ; ce n’est pas une sous-capacité de promesse. Le résultat métier reste à distinguer de l’organisation du traitement, conformément à la proposition de rattachement à Order Promising.

## Comment utiliser ce détail dans notre modèle

P70 propose de décrire chaque capacité avec une fiche distinguant les dimensions suivantes. Ce tableau est une grille locale de travail, pas une classification native d’un éditeur.

| Dimension de description | Exemple autour de la protection d’une quantité |
| --- | --- |
| Résultat métier | Rendre une protection applicable et déterminer son effet sur une demande |
| Objets et relations | Protection, bénéficiaire, ressource concernée, période de validité |
| Opérations | Définir, rendre applicable, modifier, retirer, consulter |
| Règles et variantes | Priorité relative, horizon, consommation, limites à respecter |
| Effets et garanties attendus | Quantité protégée encore opposable et motif d’une restriction ; cohérence avec les engagements |
| Réalisation | Fonction SAP, service Microsoft ou autre application ; API, événement ou traitement de masse |

Il peut être utile de distinguer **définir une politique de protection**, **tenir la protection applicable** et **déterminer la restriction pour une demande** : les résultats diffèrent. CAP007/CAP008 et les contrôles de disponibilité donnent des points d’entrée pour l’analyse. Mais la frontière avec la planification reste à examiner ; aucun calcul amont n’est automatiquement internalisé dans le socle.

À l’inverse, créer, modifier et supprimer le même objet peuvent rester les opérations d’une seule capacité. Le nombre d’API, de tables, de paramètres ou d’écrans ne détermine pas le nombre de capacités.

Précision U33/C33 : la décomposition doit distinguer des **aptitudes métier durables de l’entreprise, indépendantes de son organisation et de ses outils**, dans le périmètre de la capacité mère et avec des frontières explicites. Le résultat aide à décrire chaque aptitude ; attribuer une responsabilité ou définir un contrat ne suffit pas à en créer une. La fiche peut continuer à se préciser même lorsque l’on arrête de décomposer la carte. Les différences de politiques du périmètre historique de Beaumanoir et de Boardriders doivent être exprimées sans multiplier automatiquement les capacités par variante.

## Sources et localisateurs

Consultation du 2026-09-09 ; reformulations sélectives. Les informations de produit ne prouvent aucun usage ou paramétrage local. ELM037–ELM039 complètent les éléments déjà examinés, sans modifier les définitions CAP.

- **S1 — SAP**, [Discovering the Reference Architecture Content](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), *Business Capability Model Example* et *RBA Link to RSA*. Cours public sans édition de catalogue identifiée ; ELM014.
- **S2 — Microsoft**, [Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), *Terminology*, *Use the allocation APIs*, *Consume as a soft reservation*. Page mise à jour le 13/08/2025, texte consulté ; ELM037, complément ELM028.
- **S3 — Microsoft**, [Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), création par API, intégration/offset et annulation ; page mise à jour le 27/07/2026, texte consulté ; ELM037, complément ELM031.
- **S4 — Microsoft**, [Reserve inventory quantities](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities), introduction et politiques de réservation ; page mise à jour le 29/08/2025 ; ELM034. Le FIFO par date de réception d’un lot est une règle de sélection de ressource, distincte de l’ordre d’arrivée des demandes de vente déclaré pour le périmètre historique de Beaumanoir.
- **S5 — SAP**, [Outlining aATP with Supply Protection](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-), objet, activation, protections horizontales/priorisées et groupes. Cours sans édition produit précisée ; ELM038, complément ELM017.
- **S6 — SAP**, [Outlining aATP with Check Against Allocation](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-check-against-allocation), restrictions et périodes de consommation, cours sans édition produit précisée ; [Characteristics](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/cf3ce5573b0df032e10000000a441470.html), *Use*, et [How to Maintain Product Allocation Sequences](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/dede2d1ac0ce4b54b83dde07ddc03b1e.html), *Context*, étapes 4–8. Passages Help indexés, S/4HANA 2025 FPS01, février 2026 ; ELM038, complément ELM018.
- **S7 — SAP**, [Supply Assignment Rule](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/8835cf8d77174b798327a4c3d14484e0.html), *General Settings*, *Supply Configuration*, *Assignment Configuration*, *Release Check Settings*. Passage indexé, même édition 2025 FPS01 ; ELM039, complément ELM032/ELM035.
- **S8 — SAP**, [Key Concepts in Backorder Processing](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/3ea2a457ef816b10e10000000a441470.html?locale=en-US&state=PRODUCTION&version=2023.latest), définitions des concepts segment, variante, stratégie, repli et run. Passage indexé, documentation affichée 2023 Latest ; ELM039. Édition distincte des autres pages Help, sans supposer une configuration identique dans toutes les versions.

## Vocabulaire commun

Le [glossaire des notions et actions](../connaissance/19-glossaire-metier.md), issu de U33–U35, qualifie les mots et leur provenance. Dans cette note, fonction désigne une fonctionnalité de produit ; aucun étage de capacités appelé Fonction n’est établi. Les détails de produit servent à expliquer et illustrer les aptitudes métier.

# Inventaire reproductible des liens métier

Source : `audits/2026-09-19-audit-profond-v0/model-before-U435.yaml` ; SHA-256 `2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2`.

Relations structurelles exclues. Cet inventaire conserve les orientations originales ; un lien `needs` va du consommateur au fournisseur.

## REL-ILL-001

`D03.n` Promise Management → `ILL-OBJ-01` Engagement de fourniture

Type : `confirms` ; rôle : `non renseigné` ; statut : `under_review`.

Sens : Non renseigné.

Conditions : 

Effets : 

Sources : P80, U290

## REL-ILL-002

`D03.n` Promise Management → `ILL-DOC-01` Confirmation de promesse

Type : `associated-document` ; rôle : `non renseigné` ; statut : `under_review`.

Sens : Non renseigné.

Conditions : 

Effets : 

Sources : P80, U290

## REL-ILL-003

`D03.n` Promise Management → `ILL-EVT-01` Promesse confirmée

Type : `observed-result` ; rôle : `non renseigné` ; statut : `under_review`.

Sens : Non renseigné.

Conditions : 

Effets : 

Sources : P80, U290

## REL-ILL-004

`ILL-DOC-01` Confirmation de promesse → `ILL-OBJ-01` Engagement de fourniture

Type : `represents` ; rôle : `non renseigné` ; statut : `illustration`.

Sens : Non renseigné.

Conditions : 

Effets : 

Sources : P80

## REL-ILL-005

`ILL-DOC-01` Confirmation de promesse → `ILL-EVT-01` Promesse confirmée

Type : `records` ; rôle : `non renseigné` ; statut : `illustration`.

Sens : Non renseigné.

Conditions : 

Effets : 

Sources : P80

## REL-ILL-006

`D01` Inventory Management → `D03` Order Backlog Management

Type : `provides-knowledge` ; rôle : `non renseigné` ; statut : `illustration`.

Sens : Non renseigné.

Conditions : 

Effets : 

Sources : U80, U81

## REL-ILL-007

`D11` Agreement → `D03` Order Backlog Management

Type : `provides-conditions` ; rôle : `non renseigné` ; statut : `illustration`.

Sens : Non renseigné.

Conditions : 

Effets : 

Sources : U97

## REL-ILL-008

`D13` Fulfillment Network → `D06` Process Management

Type : `describes-network` ; rôle : `non renseigné` ; statut : `illustration`.

Sens : Non renseigné.

Conditions : 

Effets : 

Sources : U102

## REL-EXECUTION-FACTS-D04.i

`D07.c` Service Reconciliation → `D04.i` Sales Order

Type : `relates-to` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : Les faits et écarts imputés aux prestations alimentent le rapprochement de la commande ; le reliquat de prestation reste distinct du reliquat Order.

Conditions : Faits imputés à une prestation identifiée ; lien avec les lignes de commande à préciser.

Effets : Alimenter le reliquat Order sans modifier le contrat maître ni confondre le reliquat de prestation.

Sources : U141, U214, U215, U384

## REL-EXECUTION-FACTS-D04.j

`D07.c` Service Reconciliation → `D04.j` Purchase Order

Type : `relates-to` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : Les faits et écarts imputés aux prestations alimentent le rapprochement de la commande ; le reliquat de prestation reste distinct du reliquat Order.

Conditions : Faits imputés à une prestation identifiée ; lien avec les lignes de commande à préciser.

Effets : Alimenter le reliquat Order sans modifier le contrat maître ni confondre le reliquat de prestation.

Sources : U141, U214, U215, U384

## REL-EXECUTION-FACTS-D04.k

`D07.c` Service Reconciliation → `D04.k` Transfer Order

Type : `relates-to` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : Les faits et écarts imputés aux prestations alimentent le rapprochement de la commande ; le reliquat de prestation reste distinct du reliquat Order.

Conditions : Faits imputés à une prestation identifiée ; lien avec les lignes de commande à préciser.

Effets : Alimenter le reliquat Order sans modifier le contrat maître ni confondre le reliquat de prestation.

Sources : U141, U214, U215, U384

## REL-EXECUTION-FACTS-D04.l

`D07.c` Service Reconciliation → `D04.l` Customer Return

Type : `relates-to` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : Les faits et écarts imputés aux prestations alimentent le rapprochement de la commande ; le reliquat de prestation reste distinct du reliquat Order.

Conditions : Faits imputés à une prestation identifiée ; lien avec les lignes de commande à préciser.

Effets : Alimenter le reliquat Order sans modifier le contrat maître ni confondre le reliquat de prestation.

Sources : U141, U214, U215, U384

## REL-EXECUTION-FACTS-D04.m

`D07.c` Service Reconciliation → `D04.m` Supplier Return

Type : `relates-to` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : Les faits et écarts imputés aux prestations alimentent le rapprochement de la commande ; le reliquat de prestation reste distinct du reliquat Order.

Conditions : Faits imputés à une prestation identifiée ; lien avec les lignes de commande à préciser.

Effets : Alimenter le reliquat Order sans modifier le contrat maître ni confondre le reliquat de prestation.

Sources : U141, U214, U215, U384

## REL-INVENTORY-PLANNING-D05.a

`D05.f` Inventory Planning → `D05.a` Inventory Target Decision

Type : `relates-to` ; rôle : `needs` ; statut : `partial`.

Sens : Inventory Planning mobilise Inventory Target Decision pour reconfigurer, simuler et valider un scénario de stock cohérent.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U229, U233, U235, U290

## REL-INVENTORY-PLANNING-D05.d

`D05.f` Inventory Planning → `D05.d` Group Protection Decision

Type : `relates-to` ; rôle : `needs` ; statut : `partial`.

Sens : Inventory Planning mobilise Group Protection Decision pour reconfigurer, simuler et valider un scénario de stock cohérent.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U229, U233, U235, U290

## REL-INVENTORY-PLANNING-D05.e

`D05.f` Inventory Planning → `D05.e` Replenishment Decision

Type : `relates-to` ; rôle : `needs` ; statut : `partial`.

Sens : Inventory Planning mobilise Replenishment Decision pour reconfigurer, simuler et valider un scénario de stock cohérent.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U229, U233, U235, U290

## REL-INVENTORY-PLANNING-D05.c

`D05.f` Inventory Planning → `D05.c` Stock Redistribution Decision

Type : `relates-to` ; rôle : `needs` ; statut : `partial`.

Sens : Inventory Planning mobilise Stock Redistribution Decision pour reconfigurer, simuler et valider un scénario de stock cohérent.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U229, U233, U235, U290

## REL-SERVICE-CATALOG-EXECUTION

`D14` Service Catalog → `D06` Process Management

Type : `provides-conditions` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : Le référentiel fournit l’offre, les SLA configurés et les accès des services ; le domaine qualifie leur emploi et pilote les prestations dans le contexte.

Conditions : 

Effets : 

Sources : U237, U238, U240, U242, U243, U244

## REL-SERVICE-CATALOG-PROMISING

`D14` Service Catalog → `D03` Order Backlog Management

Type : `provides-conditions` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : D03 utilise les conditions de service configurées pour construire la promesse, avec la capacité contextuelle fournie par D06 et les autres informations Supply.

Conditions : 

Effets : 

Sources : U237, U238, U240, U242, U243, U244

## REL-EXECUTION-PROMISING

`D06` Process Management → `D03` Order Backlog Management

Type : `provides-knowledge` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : D06 décrit les capacités et possibilités opérationnelles ainsi que les évolutions d’exécution utiles au calcul et au réexamen de la promesse Supply par D03.

Conditions : 

Effets : 

Sources : U237, U238, U240, U242, U243, U244

## REL-EXECUTION-TRACKING-ORCHESTRATION

`D07.d` Operations Tracking → `D06.d` Process Orchestration

Type : `relates-to` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : Le tracking fournit faits, jalons et estimations utiles à la coordination des prestations par Orchestration. La décision de variation relève séparément d’Adaptation Decision.

Conditions : 

Effets : 

Sources : U237, U238, U240, U242, U243, U244, U247

## REL-EXECUTION-ORCHESTRATION-COMMITMENTS

`D06.d` Process Orchestration → `D07.b` Service Order Management

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : L’orchestration mobilise Service Order Management pour tenir les demandes de prestation et leurs évolutions selon le plan retenu ; le choix d’une variation relève d’Adaptation Decision.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U237, U238, U240, U242, U243, U244, U247, U290

## REL-EXECUTION-TRACKING-ADAPTATION

`D07.d` Operations Tracking → `D06.f` Process Adaptation Decision

Type : `relates-to` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : Les faits, jalons et estimations signalent les aléas à prendre en compte pour déterminer une variation du plan.

Conditions : 

Effets : 

Sources : U245, U246, U247

## REL-EXECUTION-ADAPTATION-SERVICE

`D06.f` Process Adaptation Decision → `D06.e` Service Selection Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : Adaptation Decision mobilise Service Decision pour déterminer des services utilisables dans la variation envisagée.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U245, U246, U247, U290

## REL-EXECUTION-ADAPTATION-CAPACITY

`D06.f` Process Adaptation Decision → `D06.b` Service Capacity Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : La décision d’adaptation utilise la capacité communiquée et son contexte ; Visibility ne décide ni du plan ni des ressources à engager.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U245, U246, U247, U290

## REL-EXECUTION-ADAPTATION-ORCHESTRATION

`D06.f` Process Adaptation Decision → `D06.d` Process Orchestration

Type : `relates-to` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : La variation retenue fournit le plan à coordonner par Orchestration ; décider l’adaptation et coordonner sa réalisation sont des responsabilités distinctes.

Conditions : 

Effets : 

Sources : U245, U246, U247

## REL-EXECUTION-ADAPTATION-PROMISE-REVISION

`D06.f` Process Adaptation Decision → `BHV023` Promise Revision

Type : `relates-to` ; rôle : `non renseigné` ; statut : `under_review`.

Sens : Si une variation remet la promesse Supply en cause, Adaptation Decision fournit les faits et variantes à D03 pour son réexamen ; elle ne révise pas elle-même la promesse.

Conditions : 

Effets : 

Sources : U245, U246, U247, U290

## REL-EXECUTION-SERVICE-CAPACITY

`D06.e` Service Selection Decision → `D06.b` Service Capacity Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : La décision de service mobilise la capacité communiquée pour apprécier les moyens utilisables dans le contexte.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U245, U246, U247, U290

## REL-EXECUTION-REQUIREMENTS-SERVICE-ORDER

`D07.a` Service Requirements Decision → `D07.b` Service Order Management

Type : `relates-to` ; rôle : `non renseigné` ; statut : `proposed`.

Sens : Les prestations nécessaires déterminées alimentent les demandes tenues par Service Order Management, sans présumer une cardinalité ou une émission automatique.

Conditions : 

Effets : 

Sources : U245, U246, U247

## REL-CTP-ORDER-PRIORITIZATION

`D03.j` Capable-to-Promise (CTP) → `D03.m` Order Prioritization

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : CTP a besoin des priorités retenues pour construire une solution respectant les arbitrages entre Orders.

Conditions : Lorsque des Orders sont en concurrence ; CTP ne redéfinit pas lui-même leur priorité. | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U250, U251, U290

## REL-CTP-EXECUTION-SERVICE

`D03.j` Capable-to-Promise (CTP) → `D06.e` Service Selection Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : CTP a besoin des possibilités de service compatibles déterminées par Service Selection Decision pour établir la faisabilité Supply.

Conditions : Lorsque la réalisation des prestations conditionne la solution ; une confirmation préalable de promesse n’est pas imposée à l’étude. | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U250, U251, U290, U409

## REL-CTP-STOCK-ALLOCATION

`D03.j` Capable-to-Promise (CTP) → `D05.d` Group Protection Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : CTP mobilise Group Protection Decision pour déterminer les modifications de droits d’usage envisagées dans un scénario.

Conditions : Si le scénario nécessite un changement de politique d’allocation ; une valeur candidate ne devient pas une protection active par sa seule production. | Uniquement si l’option nécessite une évolution de politique ; aucune application par CTP.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U250, U251, U290

## REL-CTP-COVERAGE-TARGET

`D03.j` Capable-to-Promise (CTP) → `D05.a` Inventory Target Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : CTP mobilise Inventory Target Decision pour déterminer les évolutions de niveaux ou seuils de stock envisagées dans un scénario.

Conditions : Si une évolution de ces politiques est nécessaire ; un apport pour un Order ne crée pas cette dépendance à lui seul. | Uniquement si l’option nécessite une évolution de politique ; aucune application par CTP.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U250, U251, U290

## REL-PTP-CTP-SCENARIOS

`D03.k` Profitable-to-Promise (PTP) → `D03.j` Capable-to-Promise (CTP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : PTP a besoin des possibilités de satisfaction après adaptation et de leurs impacts établis par CTP pour porter l’arbitrage économique applicable.

Conditions : Lorsque des scénarios d’adaptation sont comparés ; PTP peut aussi examiner des possibilités issues d’autres décisions. | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U250, U251, U290

## REL-DELIVERY-SCHEDULE-CTP

`D03.l` Delivery Schedule Decision → `D03.j` Capable-to-Promise (CTP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : Delivery Schedule Decision a besoin des possibilités de quantités et dates après adaptation établies par CTP pour retenir un échéancier réalisable.

Conditions : Lorsque l’échéancier repose sur une adaptation ; ce lien n’impose pas de passer par CTP pour tout échéancier. | Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U250, U251, U290

## REL-NEEDS-U290-002

`D01.f` Inventory Tracking → `D01.g` Record Inventory Movements

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de faits de stock qualifiés et corrections tracées.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-003

`D01.f` Inventory Tracking → `D07.d` Operations Tracking

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de faits, jalons et estimations.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-004

`D01.g` Record Inventory Movements → `D01.d` Stocktaking

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de constats et corrections de comptage justifiés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-005

`D01.g` Record Inventory Movements → `D07.c` Service Reconciliation

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de résultats rapprochés et écarts qualifiés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-006

`D01.c` Inventory Visibility → `D01.f` Inventory Tracking

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de état courant et ressources futures séparés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-007

`D01.d` Stocktaking → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de quantités et états avec provenance et fraîcheur.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-008

`D02.b` Supply Protection → `D05.a` Inventory Target Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de cibles et seuils proposés ou retenus.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-009

`D02.b` Supply Protection → `D05.d` Group Protection Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de droits de groupes et limites proposés ou retenus.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-010

`D02.c` Reservation → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de quantités et états avec provenance et fraîcheur.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-011

`D02.c` Reservation → `D02.b` Supply Protection

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de protections applicables, droits et limites par période.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-012

`D03.n` Promise Management → `D03.i` Available-to-Promise (ATP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de possibilités quantité/date de référence.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-014

`D03.n` Promise Management → `D03.j` Capable-to-Promise (CTP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de possibilités sous adaptation et conditions.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-016

`D03.n` Promise Management → `D03.k` Profitable-to-Promise (PTP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de arbitrage économique.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-017

`D03.n` Promise Management → `D03.l` Delivery Schedule Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de échéancier retenu.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-018

`D03.n` Promise Management → `D02.c` Reservation

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de engagements opposables selon frontière à arbitrer.

Conditions : Selon arbitrage Reservation/Assignment ; ne pas déduire plusieurs fois un même engagement.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-019

`D03.n` Promise Management → `D02.e` Supply Assignment

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de affectations aux besoins identifiés.

Conditions : Selon arbitrage Reservation/Assignment ; ne pas déduire plusieurs fois un même engagement.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-020

`D03.n` Promise Management → `D03.m` Order Prioritization

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de priorités relatives des Orders.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-021

`D03.n` Promise Management → `D07.d` Operations Tracking

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de faits, jalons et estimations.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-022

`D03.n` Promise Management → `D06.f` Process Adaptation Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de variation opérationnelle retenue et impacts Supply.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-023

`D02.e` Supply Assignment → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de quantités et états avec provenance et fraîcheur.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-024

`D02.e` Supply Assignment → `D02.b` Supply Protection

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de protections applicables, droits et limites par période.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-025

`D02.e` Supply Assignment → `D02.c` Reservation

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de engagements opposables selon frontière à arbitrer.

Conditions : Selon arbitrage Reservation/Assignment ; ne pas déduire plusieurs fois un même engagement.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-026

`D02.e` Supply Assignment → `D03.m` Order Prioritization

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de priorités relatives des Orders.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-027

`D03.i` Available-to-Promise (ATP) → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de quantités et états avec provenance et fraîcheur.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-028

`D03.i` Available-to-Promise (ATP) → `D02.b` Supply Protection

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de protections applicables, droits et limites par période.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-029

`D03.i` Available-to-Promise (ATP) → `D02.c` Reservation

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de engagements opposables selon frontière à arbitrer.

Conditions : Selon arbitrage Reservation/Assignment ; ne pas déduire plusieurs fois un même engagement.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-030

`D03.i` Available-to-Promise (ATP) → `D02.e` Supply Assignment

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de affectations aux besoins identifiés.

Conditions : Selon arbitrage Reservation/Assignment ; ne pas déduire plusieurs fois un même engagement.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-031

`D03.i` Available-to-Promise (ATP) → `D06.b` Service Capacity Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de capacité contextuelle communiquée et datée.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-032

`D03.i` Available-to-Promise (ATP) → `D13.a` Fulfillment Network Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de lieux et liens du réseau.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-033

`D03.j` Capable-to-Promise (CTP) → `D03.i` Available-to-Promise (ATP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de possibilités quantité/date de référence.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-038

`D03.k` Profitable-to-Promise (PTP) → `D03.i` Available-to-Promise (ATP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de possibilités quantité/date de référence.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-040

`D03.k` Profitable-to-Promise (PTP) → `D11.a` Agreement Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de conditions contractuelles et validité.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-041

`D03.l` Delivery Schedule Decision → `D03.i` Available-to-Promise (ATP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de possibilités quantité/date de référence.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-043

`D03.l` Delivery Schedule Decision → `D03.k` Profitable-to-Promise (PTP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de arbitrage économique.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-044

`D03.l` Delivery Schedule Decision → `D11.a` Agreement Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de conditions contractuelles et validité.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-045

`D03.m` Order Prioritization → `D11.a` Agreement Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de conditions contractuelles et validité.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-046

`D04.i` Sales Order → `D04.n` Order Structuring

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des liens de composition persistants et des règles de cohérence de l’ensemble auquel participe l’Order.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290, U363

## REL-NEEDS-U290-047

`D04.i` Sales Order → `D04.o` Order Lifecycle Management

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de progression autorisée et restrictions.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-048

`D04.i` Sales Order → `D07.c` Service Reconciliation

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de résultats rapprochés et écarts qualifiés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-049

`D04.i` Sales Order → `D03.n` Promise Management

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de engagements confirmés et part non confirmée.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-050

`D04.i` Sales Order → `D08.d` Product Reference Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de produits/variantes et caractéristiques utiles.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-051

`D04.i` Sales Order → `D09.d` Party / Role Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de parties et rôles externes.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-052

`D04.i` Sales Order → `D11.a` Agreement Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de conditions contractuelles et validité.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-053

`D04.i` Sales Order → `D12.a` Catalog Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de offre commerciale externe.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-054

`D04.j` Purchase Order → `D04.n` Order Structuring

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des liens de composition persistants et des règles de cohérence de l’ensemble auquel participe l’Order.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290, U363

## REL-NEEDS-U290-055

`D04.j` Purchase Order → `D04.o` Order Lifecycle Management

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de progression autorisée et restrictions.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-056

`D04.j` Purchase Order → `D07.c` Service Reconciliation

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de résultats rapprochés et écarts qualifiés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-057

`D04.j` Purchase Order → `D08.d` Product Reference Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de produits/variantes et caractéristiques utiles.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-058

`D04.j` Purchase Order → `D09.d` Party / Role Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de parties et rôles externes.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-059

`D04.j` Purchase Order → `D11.a` Agreement Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de conditions contractuelles et validité.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-060

`D04.k` Transfer Order → `D04.n` Order Structuring

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des liens de composition persistants et des règles de cohérence de l’ensemble auquel participe l’Order.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290, U363

## REL-NEEDS-U290-061

`D04.k` Transfer Order → `D04.o` Order Lifecycle Management

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de progression autorisée et restrictions.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-062

`D04.k` Transfer Order → `D07.c` Service Reconciliation

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de résultats rapprochés et écarts qualifiés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-063

`D04.k` Transfer Order → `D13.a` Fulfillment Network Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de lieux et liens du réseau.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-064

`D04.k` Transfer Order → `D08.d` Product Reference Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de produits/variantes et caractéristiques utiles.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-065

`D04.l` Customer Return → `D04.n` Order Structuring

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des liens de composition persistants et des règles de cohérence de l’ensemble auquel participe l’Order.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290, U363

## REL-NEEDS-U290-066

`D04.l` Customer Return → `D04.o` Order Lifecycle Management

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de progression autorisée et restrictions.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-067

`D04.l` Customer Return → `D07.c` Service Reconciliation

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de résultats rapprochés et écarts qualifiés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-068

`D04.l` Customer Return → `D04.i` Sales Order

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de demande client et conditions.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-069

`D04.l` Customer Return → `D08.d` Product Reference Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de produits/variantes et caractéristiques utiles.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-070

`D04.m` Supplier Return → `D04.n` Order Structuring

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des liens de composition persistants et des règles de cohérence de l’ensemble auquel participe l’Order.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290, U363

## REL-NEEDS-U290-071

`D04.m` Supplier Return → `D04.o` Order Lifecycle Management

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de progression autorisée et restrictions.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-072

`D04.m` Supplier Return → `D07.c` Service Reconciliation

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de résultats rapprochés et écarts qualifiés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-073

`D04.m` Supplier Return → `D04.j` Purchase Order

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de apports fournisseur attendus et possibilités de modification.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-074

`D04.m` Supplier Return → `D09.d` Party / Role Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de parties et rôles externes.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-075

`D04.m` Supplier Return → `D11.a` Agreement Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de conditions contractuelles et validité.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-076

`D04.n` Order Structuring → `D03.l` Delivery Schedule Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de échéancier retenu.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-077

`D04.o` Order Lifecycle Management → `D03.n` Promise Management

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de engagements confirmés et part non confirmée.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-078

`D04.o` Order Lifecycle Management → `D07.d` Operations Tracking

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de faits, jalons et estimations.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-079

`D05.a` Inventory Target Decision → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de quantités et états avec provenance et fraîcheur.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-080

`D05.a` Inventory Target Decision → `D13.a` Fulfillment Network Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de lieux et liens du réseau.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-081

`D05.a` Inventory Target Decision → `D08.d` Product Reference Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de produits/variantes et caractéristiques utiles.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-082

`D05.d` Group Protection Decision → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de quantités et états avec provenance et fraîcheur.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-083

`D05.d` Group Protection Decision → `D02.b` Supply Protection

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de protections applicables, droits et limites par période.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-084

`D05.d` Group Protection Decision → `D05.a` Inventory Target Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de cibles et seuils proposés ou retenus.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-085

`D05.e` Replenishment Decision → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de quantités et états avec provenance et fraîcheur.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-086

`D05.e` Replenishment Decision → `D02.b` Supply Protection

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de protections applicables, droits et limites par période.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-087

`D05.e` Replenishment Decision → `D05.a` Inventory Target Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de cibles et seuils proposés ou retenus.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-088

`D05.e` Replenishment Decision → `D07.d` Operations Tracking

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de faits, jalons et estimations.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-089

`D05.e` Replenishment Decision → `D04.j` Purchase Order

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de apports fournisseur attendus et possibilités de modification.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-090

`D05.e` Replenishment Decision → `D04.k` Transfer Order

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de transferts attendus et possibilités de modification.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-091

`D05.c` Stock Redistribution Decision → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de quantités et états avec provenance et fraîcheur.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-092

`D05.c` Stock Redistribution Decision → `D02.b` Supply Protection

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de protections applicables, droits et limites par période.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-093

`D05.c` Stock Redistribution Decision → `D13.a` Fulfillment Network Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de lieux et liens du réseau.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-094

`D05.c` Stock Redistribution Decision → `D05.e` Replenishment Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de apports et ajustements recommandés selon arbitrage.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-099

`D05.f` Inventory Planning → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de quantités et états avec provenance et fraîcheur.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-100

`D05.f` Inventory Planning → `D07.d` Operations Tracking

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de faits, jalons et estimations.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-101

`D05.f` Inventory Planning → `D02.b` Supply Protection

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de résultat de mise à jour des protections et des règles retenues, y compris refus/prise en compte partielle.

Conditions : Pour la mise en action des choix autorisés et le suivi de leur prise en compte ; aucune réalisation physique par Planning.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-102

`D05.f` Inventory Planning → `D04.j` Purchase Order

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de commandes d’apport créées ou modifiées selon choix autorisés et résultat de prise en compte.

Conditions : Pour la mise en action des choix autorisés et le suivi de leur prise en compte ; aucune réalisation physique par Planning.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-103

`D05.f` Inventory Planning → `D04.k` Transfer Order

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de orders de transfert créés ou modifiés selon choix autorisés et résultat de prise en compte.

Conditions : Pour la mise en action des choix autorisés et le suivi de leur prise en compte ; aucune réalisation physique par Planning.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-104

`D05.f` Inventory Planning → `D06.d` Process Orchestration

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de état de prise en compte et coordination des prestations nécessaires au scénario.

Conditions : Pour la mise en action des choix autorisés et le suivi de leur prise en compte ; aucune réalisation physique par Planning.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-105

`D06.b` Service Capacity Visibility → `D14.a` Service Catalog Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de services, SLA et accès configurés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-106

`D07.a` Service Requirements Decision → `D14.a` Service Catalog Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de services, SLA et accès configurés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-107

`D07.a` Service Requirements Decision → `D13.a` Fulfillment Network Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de lieux et liens du réseau.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-108

`D07.a` Service Requirements Decision → `D04.i` Sales Order

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de demande client et conditions.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-109

`D06.e` Service Selection Decision → `D07.a` Service Requirements Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de prestations nécessaires.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-110

`D06.e` Service Selection Decision → `D14.a` Service Catalog Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de services, SLA et accès configurés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-111

`D06.e` Service Selection Decision → `D13.a` Fulfillment Network Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de lieux et liens du réseau.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-113

`D06.f` Process Adaptation Decision → `D07.d` Operations Tracking

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de faits, jalons et estimations.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-114

`D06.f` Process Adaptation Decision → `D07.b` Service Order Management

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de demandes et réponses de prise en charge.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-117

`D06.d` Process Orchestration → `D07.a` Service Requirements Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de prestations nécessaires.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-118

`D06.d` Process Orchestration → `D06.e` Service Selection Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de services/exécutants compatibles retenus.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-119

`D06.d` Process Orchestration → `D06.f` Process Adaptation Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de variation opérationnelle retenue et impacts Supply.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-121

`D06.d` Process Orchestration → `D07.d` Operations Tracking

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de faits, jalons et estimations.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-122

`D07.b` Service Order Management → `D07.a` Service Requirements Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de prestations nécessaires.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-123

`D07.b` Service Order Management → `D06.e` Service Selection Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de services/exécutants compatibles retenus.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-124

`D07.b` Service Order Management → `D14.a` Service Catalog Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de services, SLA et accès configurés.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-125

`D07.d` Operations Tracking → `D07.b` Service Order Management

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de demandes et réponses de prise en charge.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-126

`D07.c` Service Reconciliation → `D07.b` Service Order Management

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de demandes et réponses de prise en charge.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-127

`D07.c` Service Reconciliation → `D07.d` Operations Tracking

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de faits, jalons et estimations.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-128

`D11.a` Agreement Ingestion → `D09.d` Party / Role Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de parties et rôles externes.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-129

`D11.a` Agreement Ingestion → `D12.a` Catalog Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de offre commerciale externe.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-130

`D12.a` Catalog Ingestion → `D08.d` Product Reference Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de produits/variantes et caractéristiques utiles.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-131

`D13.a` Fulfillment Network Ingestion → `D09.d` Party / Role Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de parties et rôles externes.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-132

`D14.a` Service Catalog Ingestion → `D09.d` Party / Role Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de parties et rôles externes.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-NEEDS-U290-133

`D14.a` Service Catalog Ingestion → `D13.a` Fulfillment Network Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de lieux et liens du réseau.

Conditions : Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.

Effets : Résultat consommé sans transfert de responsabilité du fournisseur.

Sources : U286, U290

## REL-INVENTORY-PLANNING-D05.g

`D05.f` Inventory Planning → `D05.g` Initial Stocking Decision

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des quantités et dates d’implantation pour construire et simuler un scénario comprenant un lancement.

Conditions : Lorsque nécessaire au scénario ; pas de séquence ni d’appel technique systématique.

Effets : Consommer le résultat sans transférer la responsabilité métier de la capacité fournisseur.

Sources : U313, U316

## REL-INITIAL-STOCKING-INVENTORY

`D05.g` Initial Stocking Decision → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des quantités et états de stock admissibles par magasin, avec provenance et fraîcheur.

Conditions : Lorsque nécessaire au scénario ; pas de séquence ni d’appel technique systématique.

Effets : Consommer le résultat sans transférer la responsabilité métier de la capacité fournisseur.

Sources : U313, U316

## REL-INITIAL-STOCKING-TARGET

`D05.g` Initial Stocking Decision → `D05.a` Inventory Target Decision

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des objectifs de stock au lancement, proposés ou retenus, pour déterminer les apports initiaux.

Conditions : Lorsque nécessaire au scénario ; pas de séquence ni d’appel technique systématique.

Effets : Consommer le résultat sans transférer la responsabilité métier de la capacité fournisseur.

Sources : U313, U316

## REL-INITIAL-STOCKING-PROTECTION

`D05.g` Initial Stocking Decision → `D02.b` Supply Protection

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des protections et droits d’usage applicables au périmètre et à la période du lancement.

Conditions : Lorsque nécessaire au scénario ; pas de séquence ni d’appel technique systématique.

Effets : Consommer le résultat sans transférer la responsabilité métier de la capacité fournisseur.

Sources : U313, U316

## REL-INITIAL-STOCKING-PURCHASE

`D05.g` Initial Stocking Decision → `D04.j` Purchase Order

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des apports fournisseur engagés, de leurs dates et de leurs possibilités de modification lorsque ces achats contribuent au lancement.

Conditions : Lorsque nécessaire au scénario ; pas de séquence ni d’appel technique systématique.

Effets : Consommer le résultat sans transférer la responsabilité métier de la capacité fournisseur.

Sources : U313, U316

## REL-INITIAL-STOCKING-TRANSFER

`D05.g` Initial Stocking Decision → `D04.k` Transfer Order

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des transferts engagés et de leurs dates pour éviter de demander deux fois les mêmes apports initiaux.

Conditions : Lorsque nécessaire au scénario ; pas de séquence ni d’appel technique systématique.

Effets : Consommer le résultat sans transférer la responsabilité métier de la capacité fournisseur.

Sources : U313, U316

## REL-INITIAL-STOCKING-TRACKING

`D05.g` Initial Stocking Decision → `D07.d` Operations Tracking

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin de l’avancement et des estimations des prestations engagées pour apprécier si les apports arriveront à temps pour le lancement.

Conditions : Lorsque nécessaire au scénario ; pas de séquence ni d’appel technique systématique.

Effets : Consommer le résultat sans transférer la responsabilité métier de la capacité fournisseur.

Sources : U313, U316

## REL-REDISTRIBUTION-INITIAL-STOCKING

`D05.c` Stock Redistribution Decision → `D05.g` Initial Stocking Decision

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des apports initiaux recommandés lorsqu’un rééquilibrage peut couvrir les mêmes manques ; coordonner les résultats sans double comptage.

Conditions : Lorsque nécessaire au scénario ; pas de séquence ni d’appel technique systématique.

Effets : Consommer le résultat sans transférer la responsabilité métier de la capacité fournisseur.

Sources : U313, U316

## REL-RESERVATION-POLICY-INVENTORY

`D05.h` Reservation Policy Decision → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des quantités, états, engagements connus et de leur fraîcheur pour apprécier la tension sans double compte.

Conditions : Selon le contexte utile à la décision ou à son application ; aucun appel systématique ni ordre d’exécution imposé.

Effets : Utiliser les informations ou conditions sans transférer la responsabilité métier du fournisseur.

Sources : U342

## REL-RESERVATION-POLICY-ATP

`D05.h` Reservation Policy Decision → `D03.i` Available-to-Promise (ATP)

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des possibilités de disponibilité présentes et futures dans le contexte, sans recalculer l’ATP.

Conditions : Selon le contexte utile à la décision ou à son application ; aucun appel systématique ni ordre d’exécution imposé.

Effets : Utiliser les informations ou conditions sans transférer la responsabilité métier du fournisseur.

Sources : U342

## REL-RESERVATION-POLICY-PRIORITY

`D05.h` Reservation Policy Decision → `D03.m` Order Prioritization

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des priorités décidées lorsque les régimes de réservation sont différenciés ; ne reclasse pas les Orders.

Conditions : Selon le contexte utile à la décision ou à son application ; aucun appel systématique ni ordre d’exécution imposé.

Effets : Utiliser les informations ou conditions sans transférer la responsabilité métier du fournisseur.

Sources : U342

## REL-RESERVATION-POLICY-PROTECTION

`D05.h` Reservation Policy Decision → `D02.b` Supply Protection

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des droits et restrictions actifs qui encadrent les réservations possibles.

Conditions : Selon le contexte utile à la décision ou à son application ; aucun appel systématique ni ordre d’exécution imposé.

Effets : Utiliser les informations ou conditions sans transférer la responsabilité métier du fournisseur.

Sources : U342

## REL-RESERVATION-POLICY-AGREEMENT

`D05.h` Reservation Policy Decision → `D11.a` Agreement Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des conditions de service disponibles dans la projection des Agreements lorsqu’elles encadrent les régimes de réservation.

Conditions : Selon le contexte utile à la décision ou à son application ; aucun appel systématique ni ordre d’exécution imposé.

Effets : Utiliser les informations ou conditions sans transférer la responsabilité métier du fournisseur.

Sources : U342

## REL-RESERVATION-POLICY-APPLICATION

`D02.c` Reservation → `D05.h` Reservation Policy Decision

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des conditions de réservation retenues et mises en vigueur par le management responsable pour établir et maintenir les engagements ; une recommandation non activée ne s’applique pas implicitement.

Conditions : Selon le contexte utile à la décision ou à son application ; aucun appel systématique ni ordre d’exécution imposé.

Effets : Utiliser les informations ou conditions sans transférer la responsabilité métier du fournisseur.

Sources : U342

## REL-INVENTORY-PLANNING-D05.h

`D05.f` Inventory Planning → `D05.h` Reservation Policy Decision

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des politiques de réservation alternatives et de leurs effets pour les scénarios où cet arbitrage modifie disponibilité, immobilisation et risque.

Conditions : Selon le contexte utile à la décision ou à son application ; aucun appel systématique ni ordre d’exécution imposé.

Effets : Utiliser les informations ou conditions sans transférer la responsabilité métier du fournisseur.

Sources : U342

## REL-NEEDS-U349-D03.n

`D03.n` Promise Management → `BHV037` Order Freezing

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin de connaître les éléments de l’Order protégés contre une révision de promesse et les conditions de dérogation.

Conditions : Lorsqu’une protection applicable concerne le résultat ou l’affectation à modifier.

Effets : Respecter la protection ou rendre explicite la révision autorisée nécessaire ; ne pas la lever silencieusement.

Sources : U349, CMP125

## REL-NEEDS-U349-D02.e

`D02.e` Supply Assignment → `BHV037` Order Freezing

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin de connaître les affectations explicitement protégées et les marges de substitution encore autorisées.

Conditions : Lorsqu’une protection applicable concerne le résultat ou l’affectation à modifier.

Effets : Respecter la protection ou rendre explicite la révision autorisée nécessaire ; ne pas la lever silencieusement.

Sources : U349, CMP125

## REL-NEEDS-U363-D04.q-D04.o

`D04.q` Order Archiving → `D04.o` Order Lifecycle Management

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin de la situation opérationnelle et du devenir des reliquats pour apprécier l’éligibilité à l’archivage.

Conditions : Lorsque le contexte et la portée de l’Order le nécessitent.

Effets : Consommer le résultat sans absorber la responsabilité du fournisseur.

Sources : U363, CMP133

## REL-NEEDS-U363-D04.q-D04.n

`D04.q` Order Archiving → `D04.n` Order Structuring

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des liens de composition à préserver dans la conservation historique.

Conditions : Lorsque le contexte et la portée de l’Order le nécessitent.

Effets : Consommer le résultat sans absorber la responsabilité du fournisseur.

Sources : U363, CMP133

## REL-NEEDS-U363-D04.o-D04.n

`D04.o` Order Lifecycle Management → `D04.n` Order Structuring

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin de connaître les engagements de l’ensemble qu’une mutation d’un composant doit préserver.

Conditions : Lorsque le contexte et la portée de l’Order le nécessitent.

Effets : Consommer le résultat sans absorber la responsabilité du fournisseur.

Sources : U363, CMP133

## REL-NEEDS-U378-01

`D03.o` Fulfillment Plan Decision → `D03.i` Available-to-Promise (ATP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des possibilités de quantités et dates dans la situation de référence.

Conditions : Selon le cas et les hypothèses du scénario ; aucune séquence ou invocation systématique imposée.

Effets : Résultat mobilisé sans transférer la responsabilité de la capacité fournisseur.

Sources : U377, U378, ELM228, CMP139

## REL-NEEDS-U378-02

`D03.o` Fulfillment Plan Decision → `D03.j` Capable-to-Promise (CTP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des possibilités sous adaptation et de leurs conditions de faisabilité lorsque la référence ne suffit pas.

Conditions : Selon le cas et les hypothèses du scénario ; aucune séquence ou invocation systématique imposée.

Effets : Résultat mobilisé sans transférer la responsabilité de la capacité fournisseur.

Sources : U377, U378, ELM228, CMP139

## REL-NEEDS-U378-03

`D03.o` Fulfillment Plan Decision → `D03.k` Profitable-to-Promise (PTP)

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de la comparaison économique des scénarios, sans réduire la valeur multidimensionnelle à la seule marge.

Conditions : Selon le cas et les hypothèses du scénario ; aucune séquence ou invocation systématique imposée.

Effets : Résultat mobilisé sans transférer la responsabilité de la capacité fournisseur.

Sources : U377, U378, ELM228, CMP139

## REL-NEEDS-U378-04

`D03.o` Fulfillment Plan Decision → `D03.m` Order Prioritization

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des priorités relatives des commandes pour établir le scénario collectif.

Conditions : Selon le cas et les hypothèses du scénario ; aucune séquence ou invocation systématique imposée.

Effets : Résultat mobilisé sans transférer la responsabilité de la capacité fournisseur.

Sources : U377, U378, ELM228, CMP139

## REL-NEEDS-U378-05

`D03.o` Fulfillment Plan Decision → `D03.l` Delivery Schedule Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des échéanciers admissibles et retenus pour rendre cohérentes quantités et dates.

Conditions : Selon le cas et les hypothèses du scénario ; aucune séquence ou invocation systématique imposée.

Effets : Résultat mobilisé sans transférer la responsabilité de la capacité fournisseur.

Sources : U377, U378, ELM228, CMP139

## REL-NEEDS-U378-06

`D03.o` Fulfillment Plan Decision → `D02.b` Supply Protection

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des protections actives encadrant les usages admissibles des ressources.

Conditions : Selon le cas et les hypothèses du scénario ; aucune séquence ou invocation systématique imposée.

Effets : Résultat mobilisé sans transférer la responsabilité de la capacité fournisseur.

Sources : U377, U378, ELM228, CMP139

## REL-NEEDS-U378-07

`D02.e` Supply Assignment → `D03.o` Fulfillment Plan Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin du scénario retenu de plan d’affectation pour matérialiser les liens ressources-commandes concernés.

Conditions : Selon le cas et les hypothèses du scénario ; aucune séquence ou invocation systématique imposée.

Effets : Résultat mobilisé sans transférer la responsabilité de la capacité fournisseur.

Sources : U377, U378, ELM228, CMP139

## REL-NEEDS-U380-01

`D05.i` Return Disposition Decision → `D07.d` Operations Tracking

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des constats et résultats d’inspection remontés par les exécutants pour déterminer le devenir du produit.

Conditions : Selon le cas de retour et les informations disponibles ; aucune séquence ou invocation systématique imposée.

Effets : Résultat consommé sans transférer la responsabilité du fournisseur ; décision et réalisation distinguées.

Sources : U379, U380, ELM229, CMP140

## REL-NEEDS-U380-02

`D05.i` Return Disposition Decision → `D01.c` Inventory Visibility

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de l’état connu et de la disponibilité du stock retourné pour contextualiser ses orientations.

Conditions : Selon le cas de retour et les informations disponibles ; aucune séquence ou invocation systématique imposée.

Effets : Résultat consommé sans transférer la responsabilité du fournisseur ; décision et réalisation distinguées.

Sources : U379, U380, ELM229, CMP140

## REL-NEEDS-U380-03

`D04.l` Customer Return → `D05.i` Return Disposition Decision

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin de l’orientation retenue pour préparer et suivre les suites du retour client, en mobilisant les capacités des Orders nécessaires.

Conditions : Selon le cas de retour et les informations disponibles ; aucune séquence ou invocation systématique imposée.

Effets : Résultat consommé sans transférer la responsabilité du fournisseur ; décision et réalisation distinguées.

Sources : U379, U380, ELM229, CMP140, U383, CMP142

## REL-NEEDS-U380-04

`D06.d` Process Orchestration → `D05.i` Return Disposition Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin de l’orientation retenue et de ses conditions pour coordonner les prestations logistiques de suite du retour.

Conditions : Selon le cas de retour et les informations disponibles ; aucune séquence ou invocation systématique imposée.

Effets : Résultat consommé sans transférer la responsabilité du fournisseur ; décision et réalisation distinguées.

Sources : U379, U380, ELM229, CMP140

## REL-NEEDS-U383-ARCHIVING-D04.i

`D04.q` Order Archiving → `D04.i` Sales Order

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin du contenu, des versions et des règles de conservation propres aux Orders de ce type.

Conditions : Selon les Orders à conserver et les politiques applicables.

Effets : Conserver les traces sans reprendre leur gestion courante.

Sources : U382, U383, ELM230, ELM231, CMP141, CMP142

## REL-NEEDS-U383-ARCHIVING-D04.j

`D04.q` Order Archiving → `D04.j` Purchase Order

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin du contenu, des versions et des règles de conservation propres aux Orders de ce type.

Conditions : Selon les Orders à conserver et les politiques applicables.

Effets : Conserver les traces sans reprendre leur gestion courante.

Sources : U382, U383, ELM230, ELM231, CMP141, CMP142

## REL-NEEDS-U383-ARCHIVING-D04.k

`D04.q` Order Archiving → `D04.k` Transfer Order

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin du contenu, des versions et des règles de conservation propres aux Orders de ce type.

Conditions : Selon les Orders à conserver et les politiques applicables.

Effets : Conserver les traces sans reprendre leur gestion courante.

Sources : U382, U383, ELM230, ELM231, CMP141, CMP142

## REL-NEEDS-U383-ARCHIVING-D04.l

`D04.q` Order Archiving → `D04.l` Customer Return

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin du contenu, des versions et des règles de conservation propres aux Orders de ce type.

Conditions : Selon les Orders à conserver et les politiques applicables.

Effets : Conserver les traces sans reprendre leur gestion courante.

Sources : U382, U383, ELM230, ELM231, CMP141, CMP142

## REL-NEEDS-U383-ARCHIVING-D04.m

`D04.q` Order Archiving → `D04.m` Supplier Return

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin du contenu, des versions et des règles de conservation propres aux Orders de ce type.

Conditions : Selon les Orders à conserver et les politiques applicables.

Effets : Conserver les traces sans reprendre leur gestion courante.

Sources : U382, U383, ELM230, ELM231, CMP141, CMP142

## REL-NEEDS-U385-SUPPLIER-RETURN

`BHV052` Return to Supplier → `D04.m` Supplier Return

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin de la prise en charge de l’Order de retour fournisseur et de ses résultats pour suivre la suite du retour client.

Conditions : Lorsque le devenir retenu et les autorisations applicables prévoient un renvoi fournisseur.

Effets : Préserver les liens et quantités entre retours sans créer une seconde responsabilité de gestion de la commande fournisseur.

Sources : U382, U384, U385, ELM232, CMP143

## REL-NEEDS-U387-REPLACEMENT-PURCHASE

`BHV056` Return for Replacement → `D04.j` Purchase Order

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin de l’apport de remplacement porté par Purchase Order, de ses quantités, dates et résultats pour suivre le remplacement restant attendu.

Conditions : Lorsque l’accord applicable prévoit un remplacement de marchandises.

Effets : Relier le renvoi et l’apport sans les compter deux fois, sans imposer une nouvelle commande ni modifier automatiquement les promesses.

Sources : U386, U387, ELM233, CMP144

## REL-NEEDS-U388-REPAIR-EXECUTION

`BHV057` Return for Repair → `D06.d` Process Orchestration

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin de la coordination des prestations de renvoi, réparation et restitution selon les services retenus.

Conditions : Lorsque ces prestations relèvent de l’orchestration Supply.

Effets : Suivre l’Order sans reprendre l’orchestration détaillée ni la réalisation physique.

Sources : U386, U388, ELM233, CMP144

## REL-NEEDS-U391-DIRECT-SALES

`BHV059` Direct Delivery → `D04.i` Sales Order

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des attentes de la commande de vente et du lien avec les quantités achetées pour le client.

Conditions : Lorsque le fournisseur livre directement le client.

Effets : Expliquer les écarts achat/vente sans modifier automatiquement la promesse.

Sources : U390, U391, ELM235, CMP146

## REL-NEEDS-U391-SERVICE-ORDER

`BHV060` Service Procurement → `D07.b` Service Order Management

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des sollicitations et résultats des services pour rapprocher l’attendu d’achat et le réalisé.

Conditions : Lorsqu’une prestation achetée est exécutée via la plateforme de services.

Effets : Distinguer engagement d’achat et pilotage opérationnel ; aucun achat imposé pour tout appel de service.

Sources : U390, U391, ELM235, CMP146

## REL-NEEDS-U391-STOCK-FACTS

`BHV058` Stock Procurement → `D01.g` Record Inventory Movements

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : A besoin des faits de réception enregistrés pour déterminer le reste à recevoir.

Conditions : Lorsqu’un achat alimente le stock du réseau.

Effets : Ne pas assimiler réception annoncée et stock réellement reçu.

Sources : U390, U391, ELM235, CMP146

## REL-NEEDS-U395-01

`D01.h` Consigned Inventory Management → `D11.a` Agreement Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des conditions de l’accord ingérées depuis le maître externe pour appliquer au stock les droits, obligations et échéances.

Conditions : Selon le cas et les conditions applicables ; aucun appel systématique imposé.

Effets : Consommer le résultat ou les conditions sans transférer la responsabilité de leur fournisseur.

Sources : U391, U392, U393, U394, U395, ELM236, ELM237, CMP147, CMP148, CMP149

## REL-NEEDS-U395-02

`D04.r` Consignment Replenishment Order → `D11.a` Agreement Ingestion

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin des conditions de l’accord ingérées depuis le maître externe pour formuler et suivre la demande d’apport consigné.

Conditions : Selon le cas et les conditions applicables ; aucun appel systématique imposé.

Effets : Consommer le résultat ou les conditions sans transférer la responsabilité de leur fournisseur.

Sources : U391, U392, U393, U394, U395, ELM236, ELM237, CMP147, CMP148, CMP149

## REL-NEEDS-U395-03

`D04.r` Consignment Replenishment Order → `D05.g` Initial Stocking Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin du besoin d’implantation retenu lorsque la demande correspond à un premier apport.

Conditions : Selon le cas et les conditions applicables ; aucun appel systématique imposé.

Effets : Consommer le résultat ou les conditions sans transférer la responsabilité de leur fournisseur.

Sources : U391, U392, U393, U394, U395, ELM236, ELM237, CMP147, CMP148, CMP149

## REL-NEEDS-U395-04

`D04.r` Consignment Replenishment Order → `D05.e` Replenishment Decision

Type : `relates-to` ; rôle : `needs` ; statut : `under_review`.

Sens : A besoin du besoin de réassort retenu lorsque la demande correspond à une alimentation continue.

Conditions : Selon le cas et les conditions applicables ; aucun appel systématique imposé.

Effets : Consommer le résultat ou les conditions sans transférer la responsabilité de leur fournisseur.

Sources : U391, U392, U393, U394, U395, ELM236, ELM237, CMP147, CMP148, CMP149

## REL-NEEDS-U424-D03.p-D04.o

`D03.p` Order Backlog Planning → `D04.o` Order Lifecycle Management

Type : `relates-to` ; rôle : `needs` ; statut : `proposed`.

Sens : Mobilise les transitions autorisées des Orders pour mettre en action le scénario retenu.

Conditions : Selon les engagements, protections et conditions de prise en charge du scénario ; aucun appel systématique.

Effets : Obtenir l’engagement, la protection, l’autorisation ou la suspension applicable ; la réalisation demeure pilotée et observée en D06.

Sources : U424, ELM251, CMP162

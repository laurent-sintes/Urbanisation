# Audit des domaines et de la publication Urbanisation

13 septembre 2026 — U117/U118. Comparaison des nœuds JSON avec P81, P82–P87, les corrections C63–C72 et l’audit marché du 11 septembre. Les sources du marché ne sont pas revérifiées lors de ce contrôle de cohérence interne.

## Résultats par domaine

| Repère | Domaine ou référence | Capacités | Résultat |
| --- | --- | --- | --- |
| D01 | Inventory Management | 5 | P82/U116 intégré : cinq capacités ; regroupement D01.a/b sous D01.e. |
| D02 | Resource Availability and Commitments | 2 | Deux aptitudes résiduelles en réexamen, pas de retrait adopté. Recouvrements avec Inventory Management et Order Promising à résoudre. |
| D03 | Order Promising | 9 | Neuf noms, définitions et validations U95 correctement repris ; aucune correction métier. |
| D04 | Commercial Commitments | 4 | Quatre libellés courts P84 intégrés selon U118. Contrats distincts des commandes, frontière documentaire U100 encore à revoir. |
| D05 | Operational Resource Balancing | 3 | Net Requirements Calculation intégré. Coverage Target Decision et Stock Redistribution Decision restent conditionnels à l’autorité et au périmètre : alternatives dans le backlog. |
| D06 | Execution Options | 3 | Execution Capacity Assessment et Execution Option Assessment intégrés. D06.a reste inchangé : distinction références reçues/prestations à préciser. |
| D07 | Execution Commitments and Facts | 4 | Quatre libellés courts de l’audit U99 intégrés ; frontières D04/D01 et adhérence logistique conservées. |
| D09 | Party / Role | 1 | Ingestion seule et nom correctement repris ; autorité externe et réserves conservées. |
| D11 | Agreement | 1 | Ingestion seule et nom correctement repris ; autorité externe et réserves conservées. |
| D08 | Product Reference | 1 | Ingestion seule et nom correctement repris ; autorité externe et réserves conservées. |
| D12 | Catalog | 1 | Ingestion seule et nom correctement repris ; autorité externe et réserves conservées. |
| D13 | Fulfillment Network | 1 | Ingestion seule et nom correctement repris ; autorité externe et réserves conservées. |

D10 reste retiré ; les cinq références restent regroupées sous Business References. L’audit ne crée aucun domaine ni capacité supplémentaire. Il ne conclut pas que tous les domaines étaient obsolètes.

## Onze libellés corrigés

| Repère | Avant | Après |
| --- | --- | --- |
| D04.a | Establish a commercial commitment | Commitment Creation |
| D04.b | Amend commercial obligations | Commitment Revision |
| D04.c | Determine commitment fulfillment and remaining obligations | Commitment Reconciliation |
| D04.d | Authorize a return or replacement | Return and Replacement Decision |
| D05.b | Determine net resource requirements | Net Requirements Calculation |
| D06.b | Determine available execution capacity | Execution Capacity Assessment |
| D06.c | Determine eligible execution options | Execution Option Assessment |
| D07.a | Formalize a service requirement | Execution Requirement Definition |
| D07.b | Establish and adjust execution commitments | Execution Commitment Management |
| D07.c | Qualify execution results and discrepancies | Execution Reconciliation |
| D07.d | Identify and qualify expected resources | Expected Supply Tracking |

Définitions, finalités, natures et rattachements inchangés pour ces onze renommages. Sources : P84 pour D04 ; P86 et audit U99 pour D05–D07. Aucune équivalence éditeur supplémentaire ni validation métier créée. Les décisions conditionnelles et les pistes prix/consommation contractuelle restent ouvertes.

## Publication et contrôle

La publication intègre D01 et les onze noms retenus. Atlas lit uniquement les releases, désormais présentées comme Urbanisation. Le backlog et le panorama restent des fichiers de travail ; les anciennes versions publiées sont accessibles dans la liste des versions.

Les horodatages et versions entières sont calculés à la préparation pour le modèle, les nœuds, relations et principes. Le premier horodatage enregistre le début du suivi lorsque la date historique précise est inconnue. Les métadonnées de provenance et de statut font partie du contenu versionné ; les champs calculés de publication ne provoquent pas de révisions artificielles.

L’évolution de la notice D01 entraîne une nouvelle révision du domaine : ADOPT-001 reste historique et sa reprise automatique est suspendue par la règle de même révision. Les neuf capacités Order Promising restent validées ; cette suspension ne change pas leur statut. Les valeurs anciennement approuvées de D01 restent consultables dans la version .2.

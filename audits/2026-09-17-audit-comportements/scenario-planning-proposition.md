# Planning et comportements du scénario — U267

**Actualisation U269 :** la réponse présentée à Laurent est désormais adoptée pour Inventory Planning : cinq noms et descriptions courtes, rattachements, bénéfice et application via les capacités responsables. [Implémentation et portées](../../connaissance/35-comportements-inventory-planning.md). Le corps ci-dessous conserve la proposition U267/U268 ; les mentions « à arbitrer » sur ce principe d’application décrivent cet état antérieur. Les détails non présentés restent proposés.

17 septembre 2026. Proposition discutée, non appliquée au catalogue. Elle précise la piste B1 de l’audit ; les trois comportements suggérés auparavant ne sont pas un découpage adopté.

## Correction de la proposition de Codex

Reconfiguration reprenait trop littéralement les trois verbes U229. Construction couvre une première élaboration, une copie et une modification de scénario ; reconfiguration peut en préciser une modalité. Planning nomme la capacité, scénario l’objet sur lequel portent ses comportements. Employer le même objet dans les intitulés rend la décomposition plus cohérente.

## Cinq comportements proposés

| Intitulé anglais proposé | Résultat concret proposé | Complexité ou bénéfice ciblé |
| --- | --- | --- |
| Scenario Construction | Un scénario explicite : périmètre, hypothèses, objectifs, contraintes et options envisagées. | Distinguer le scénario initial et ses modifications, connaître exactement ce qui est exploré. |
| Scenario Simulation | Les conséquences projetées du scénario, en mobilisant les décisions pertinentes. | Explorer les effets sans confondre projection et application. |
| Scenario Evaluation | L’appréciation d’un scénario et sa comparaison éventuelle à d’autres ou à une référence, selon des critères explicites. | Une simulation produit des conséquences ; leur évaluation rend les compromis compréhensibles. Comparaison et évaluation peuvent rester dans un comportement. |
| Scenario Validation | Le scénario retenu et autorisé pour application, avec ses conditions et réserves. | Identifier le résultat utilisable, distinct des options encore exploratoires ; cette définition reste à valider avec Laurent. |
| Scenario Application | Le déclenchement des actions correspondant au scénario retenu et la connaissance de leur prise en compte. | Relier le scénario à ses effets opérationnels, y compris application partielle, refus et écarts. Le propriétaire du pilotage de l’application reste à arbitrer. |

Exemple fictif : construire deux scénarios de couverture magasin à 10 et 15 jours ; simuler les quantités et effets attendus ; comparer disponibilité, immobilisation et risque ; retenir un scénario ; appliquer les seuils/quotas et solliciter les Orders appropriés via leurs capacités responsables. Les critères et impacts chiffrés ne sont pas calculés dans cet exemple.

Ces descriptions sont rédigées par Codex. Les noms anglais, le choix d’Evaluation comme libellé et les résultats détaillés ne sont pas adoptés par U267. Le nom Planning de D05.f n’est pas renommé. Les cinq comportements ne sont pas instanciés comme nœuds.

## Frontière d’application à instruire

Application ne signifie pas seulement marquer le scénario actif. La proposition consiste à déclencher les mises en action et connaître leur résultat via les capacités responsables : protections et données applicables, gestion des Orders, pilotage des prestations par D06. L’activation du scénario, l’application transactionnelle et la réalisation physique restent distinguées.

L’expérience de Planning peut donner accès à cette application ; cela ne décide pas à elle seule quelle capacité en porte la coordination. Attribuer ce comportement à D05.f préciserait son rôle actuel analytique : c’est un arbitrage à faire explicitement, pas une conséquence du nom Planning. La capacité de gestion opérationnelle conserve sa propre responsabilité et peut être sollicitée depuis d’autres contextes. Aucun écran, batch, contrôle humain ou contrat de lot atomique n’est imposé.

Les comportements sont combinables et itératifs ; cette présentation ne crée pas un workflow obligatoire. Les décisions de couverture, quotas, apports et redistribution restent des capacités mobilisées, pas des comportements déplacés sous Planning.

## Comparaison marché requise par U268 — CMP090

Sources primaires consultées le 17 septembre 2026. Fonctions produit comparées à nos comportements ; aucun catalogue natif de cinq comportements identiques démontré.

| Proposition de Laurent | Appui marché consulté | Recommandation FLOW et justification |
| --- | --- | --- |
| Construction de scénario | SAP IBP permet la création de scénarios et la modification de jeux d’hypothèses (S1/S2). | Construction couvre création initiale et modification : plus large et plus approprié que Reconfiguration. |
| Simulation | SAP distingue simulation des résultats et scénarios conservés ; Microsoft utilise des plans pour explorer des stratégies (S1/S3). | Conserver : produire les conséquences projetées en mobilisant les décisions, distinctement de l’évaluation de ces conséquences. |
| Comparaison / Évaluation | Oracle compare des plans par indicateurs agrégés et au niveau des Orders ; SAP propose la comparaison de scénarios (S1/S4). | Préférer Scenario Evaluation : apprécier un scénario selon des critères, avec comparaison facultative. Cette portée locale élargie est proposée, pas une traduction normative. |
| Validation | Oracle expose une action Approve, dont la disponibilité dépend du type de plan (S5). | Conserver le choix/autorisation d’un scénario ; critères, réserves et automatisation restent explicites. Ne pas importer un workflow humain obligatoire. |
| Application du scénario | Oracle Release transmet les recommandations approuvées aux systèmes d’exécution ; Microsoft affermit des ordres planifiés ; SAP peut promouvoir les données d’un scénario dans une version active (S1/S5/S6). | L’application a un appui marché. Distinguer promotion de données de planification et mise en action opérationnelle. Proposer un comportement qui sollicite les capacités responsables et rend leur prise en compte visible ; décider explicitement de son rattachement à Planning. |

**Conclusion proposée :** les cinq comportements sont une meilleure piste que les trois premiers proposés par Codex. Planning demeure le nom de la capacité, scénario l’objet de ses comportements. L’application ne doit pas être écartée au seul motif que D05 est analytique : le marché montre le passage du plan à l’exécution. Pour FLOW, la cohérence se construit en décrivant la collaboration avec Supply Protection, les gestions d’Orders et D06, tout en conservant leurs responsabilités propres. Le mandat de déclenchement/pilotage donné à D05.f reste un arbitrage, pas une mise à jour implicite.

### Sources et portée

- **S1 — SAP IBP**, cours public, édition précise non affichée : [Creating and Comparing Versions and Scenarios](https://learning.sap.com/courses/mastering-the-advanced-configuration-in-sap-ibp/creating-and-comparing-versions-and-scenarios-1), sections Simulation and Scenario Concept / Version Planning and Simulation. Création, comparaison, simulation et promotion des données ; promotion ne prouve pas une exécution physique.
- **S2 — SAP IBP**, cours public, édition non affichée : [Versions and Scenarios](https://learning.sap.com/courses/mastering-sap-ibp-for-response-and-supply-order-based-planning-fr/versions-and-scenarios_d42f03ea-be09-49b7-9256-dc93207edee0_fr-FR), Versions / Scénarios / Copie des données. Reconsultation ELM169.
- **S3 — Microsoft Dynamics 365 SCM**, documentation évolutive : [Master plans overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans), Using master plans / Action message. Reconsultation ELM168.
- **S4 — Oracle Supply Planning 26B** : [How You Compare Supply Plans and Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fausp/how-you-compare-supply-plans-and-orders.html), Plan Comparison / Order Comparison. Comparaisons à deux granularités ; aucune équivalence de niveau de capacité déduite.
- **S5 — Oracle Supply Chain Planning 25D** : [Actions to Manage Your Plans](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faupc/actions-to-manage-your-plans.html), tableau des actions, notamment Approve / Release / Run. Les possibilités diffèrent selon les types de plans ; ne pas universaliser leurs états.
- **S6 — Microsoft Dynamics 365 SCM**, documentation évolutive : [Firm planned orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming), modes d’affermissement. Application d’ordres planifiés, pas preuve d’une application universelle de scénario. Reconsultation ELM168.

Le bénéfice ciblé de la décomposition est de distinguer hypothèses, conséquences, appréciation, choix applicable et effets effectivement déclenchés. Les correspondances restent proposées ; U268 adopte la méthode de discussion, pas ces cinq comportements.

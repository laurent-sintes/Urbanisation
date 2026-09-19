# Offre de services et pilotage de l'exécution — challenge marché U239

16 septembre 2026 — Codex. Proposition U237, périmètre D06/D07 confirmé U238 ; D05 conservé. Comparaison de concepts, contrats et fonctions de produits, sans équivalence automatique avec des capacités métier. Aucun changement des nœuds ni publication.

## Conclusion proposée

Le couple référentiel d'offre / domaine de pilotage est cohérent avec les références examinées. Un domaine unique D06/D07 est un choix local possible, pas une structure commune imposée par Microsoft, SAP et TM Forum. L'offre ne prouve pas la faisabilité d'une prestation précise ; sollicitation, engagement et résultat doivent rester distincts.

Je conserve Execution Service Catalog et Execution Management comme noms proposés. Je précise le second : « Piloter les prestations confiées aux exécutants, en qualifiant leur faisabilité, en gérant leurs engagements et leurs dépendances, puis en suivant leurs résultats et leurs écarts. » Cette définition et le découpage restent à discuter.

## Constats documentaires

| Élément | Passage consulté, reformulé | Appui et limite pour FLOW |
| --- | --- | --- |
| ELM129 — TMF633 Service Catalog Management | Gestion du cycle des éléments du catalogue de services. | Appui à un référentiel séparé ; ne prouve ni catalogue logistique natif ni obligation d'un endpoint unique par service. |
| ELM130 — TMF645 Service Qualification Management | Qualification avant commande, portant sur la disponibilité du service au lieu du client. | Appui à l'évaluation contextuelle distincte de l'offre. L'adaptation à charge d'entrepôt et capacité transport est locale. |
| ELM131 — TMF641 Service Ordering Management | Création, modification et consultation des Service Orders, avec notifications ; v4.2 documente aussi jalons et risques de non-tenue dans son historique. | Appui au contrat de sollicitation/suivi ; ni garantie de streaming continu ni cycle commun à toutes prestations. |
| ELM132 — TMFC007 Service Order Management | Le composant orchestre la réalisation, peut solliciter des interventions de techniciens, déléguer à d'autres gestionnaires et gérer les dépendances entre éléments. Les dates de réalisation considèrent aussi charge/capacité. | Appui à coordination et engagements, y compris physiques. Son périmètre télécom inclut des choix de ressources internes ; ne pas tout transférer à FLOW. |
| ELM133 — Microsoft Dynamics 365 SCM | Les Carrier Services portent des contraintes et paramètres de transport ; les modes de sollicitation peuvent être manuels ou EDI. En WMS only, les Inbound/Outbound Shipment Orders sont distincts des Orders amont et les événements signalent des étapes de réception/expédition, dont les détails sont ensuite consultés. | Appui concret à offre, demande spécialisée et retours. Le WMS autonome ne constitue pas une plateforme générique de tous les services. |
| ELM134 — SAP S/4HANA TM | Les Freight Orders distinguent cycle de vie et états d'exécution ; dans le scénario Last Mile examiné, In Execution ne permet pas l'annulation. Le suivi analyse retards, événements inattendus et écarts bloquants ou non. | Appui aux contraintes du physique et aux résultats/écarts. Ne pas imposer la même réversibilité à un transport et à une production documentaire. |
| ELM135 — TMF623 SLA Management, référence historique | La présentation R14.5.1 traite du cycle de vie des SLA et des violations, dans les relations fournisseur/client ou multi-partenaires. | Appui historique à une responsabilité distincte ; aucune assertion de version actuelle ni reprise du schéma détaillé. |

## Ce que je challengerais dans la proposition

1. **Un service ne se réduit pas à un endpoint et un SLA.** Distinguer résultat métier, fournisseur, conditions d'éligibilité, contrat de sollicitation et retours. L'endpoint est un rattachement technique : plusieurs services peuvent partager un accès, un service peut avoir plusieurs accès selon le contexte. Recommandation de conception locale, non cardinalité imposée par les sources. Un adaptateur peut rendre accessible à FLOW un exécutant partiellement informatisé.
2. **L'offre ne vaut pas disponibilité.** Préserver l'évaluation dynamique de D06.b/c dans le domaine regroupé. La Supply doit pouvoir obtenir une faisabilité, une date et les conditions associées avant de promettre. D03 garde l'engagement envers l'Order ; les exécutants ou leur pilotage fournissent les possibilités de réalisation. Maîtrise exacte du choix et réservation éventuelle de capacité à instruire.
3. **Un SLA n'est ni une estimation ni une mesure constatée.** Proposition : profil applicable en référence, engagement daté pour la prestation, prévision actualisée et résultat observé distincts. Les SLA concernent également les services numériques. Lien à Agreement à définir pour éviter deux autorités contractuelles ; aucun nouveau référentiel SLA autonome imposé.
4. **Le suivi doit porter sur des jalons et résultats explicites.** Préciser ce qui est remonté, quand et avec quelle fraîcheur ; distinguer absence de nouvelles, retard et échec. Un événement peut signaler qu'un résultat est disponible sans en porter tous les détails. Le qualificatif « continu » décrit la continuité du suivi ; il ne démontre pas une télémétrie en temps réel uniforme.
5. **Le domaine unique doit porter les dépendances utiles entre prestations.** Exemple local : préparation terminée avant enlèvement ; échec documentaire bloquant seulement les départs concernés. Choisir ce que FLOW coordonne et ce que le prestataire livre comme service composé. Ne pas recréer les tâches WMS/TMS internes ou imposer un moteur de workflow central.
6. **Les règles de modification dépendent du service et de son avancement.** Demander une annulation ne signifie pas l'obtenir ; après réalisation physique, une prestation corrective peut être nécessaire. Cette observation ne prescrit pas une capacité d'annulation distincte ni un rollback universel.

## Responsabilités proposées, sans création de capacités

Le regroupement doit préserver l'offre admissible de D06.a (référence versus évaluation contextualisée), les évaluations D06.b/c, les Service Orders D07.a, les prises en charge D07.b, le rapprochement et ses contributions à D04 de D07.c, ainsi que les résultats encore attendus D07.d. Ajouter explicitement à l'étude coordination des prestations et traitement des exceptions. Éviter de réduire le domaine à envoyer/suivre/rapprocher ; ne pas transformer chaque opération en capacité.

Cas d'épreuve proposé : une commande requiert préparation, document et transport ; capacité d'entrepôt insuffisante avant le cut-off, acceptation du transport, exécution partielle, document en échec et nouvelle heure prévue. Vérifier qui peut réviser quoi, quelles promesses D03 doit revoir, ce que D04 conserve et quels faits D01 enregistre. Aucun cas ne démontre un déploiement dans les SI Beaumanoir.

## Sources, versions et limites d'accès

Consultation du **16 septembre 2026**, sources officielles uniquement. Synthèses limitées et liens ; aucune redistribution de schéma ou catalogue. Les pages API annoncent Apache 2.0 sauf mention contraire ; guides et TMFC007 portent RAND. L'étude compare les passages lus, sans adoption ni déclaration de conformité.

| Repère | Source officielle et édition | Accès et localisateur |
| --- | --- | --- |
| ELM129 / MKT19 | [TMF633 v4.0](https://www.tmforum.org/open-digital-architecture/open-apis/service-catalog-management-api-TMF633/v4.0) | Page ouverte, Overview ; assets détaillés non examinés. |
| ELM130 / MKT19 | [TMF645 v5.0](https://www.tmforum.org/open-digital-architecture/open-apis/service-qualification-management-api-TMF645/v5.0) | Présentation et historique consultés ; disponibilité au lieu du client, pas preuve d'un algorithme logistique. |
| ELM131 / MKT19 | [TMF641 v4.2](https://www.tmforum.org/open-digital-architecture/open-apis/service-ordering-management-api-TMF641/v4.2) | Overview et historique multiversion ; v4.2 stable datée du 14 août 2026 sur la page. Le schéma complet n'est pas audité. |
| ELM132 / MKT19 | [TMFC007 v1.2.1](https://oda-production.s3.eu-west-2.amazonaws.com/v1.0.0/TMFC007_Service_Order_Management_v1.2.1.pdf) | PDF, texte pages 5 et 9–12 consulté ; approbation 2 juillet 2024. Fonctions d'un composant, pas capacités FLOW. Graphiques non interprétés. |
| ELM133 / MKT14 | [Set up shipping carriers](https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/tasks/set-up-shipping-carriers) | Page ouverte, services, tender et rating profiles ; documentation en ligne sans édition produit figée. |
| ELM133 / MKT14 | [Warehouse management only mode overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-overview) ; [External ERP systems](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-external-erp) | Textes ouverts : documents spécialisés, scénario réception/expédition et événements. Ne pas généraliser les processus non pris en charge au produit SCM complet. |
| ELM134 / MKT13 | [Freight Order Statuses](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e322becd165844e5868e590bc8efafaf/fcfb5489d40d4e8b87fb4960cef76918.html) | Texte indexé détaillé ; Last Mile Distribution, 2025 FPS01 (février 2026). Portée du scénario conservée. |
| ELM134 / MKT13 | [Freight Order Execution Detailed View](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/e612dc0d2131484a89a79862411eb467.html) | Texte indexé lu, ouverture directe sans corps exploitable ; Fiori F2750. Édition non affichée dans cet extrait, ne pas lui attribuer celle d'une autre page. |
| ELM135 / MKT19 | [TMF623 R14.5.1](https://www.tmforum.org/resources/standard/tmf623-sla-management-api-rest-specification-r14-5-0/) | Présentation officielle indexée ; source historique, guide complet non lu et statut actuel non établi. |

## Correspondance CMP076

État local comparé : proposition `execution-services-review.yaml` U237/U238 face à la release v006. ELM129–135 fournissent des appuis sémantiques et fonctionnels partiels. La composition locale catalogue + domaine unique, les rattachements, les noms et la granularité ne sont pas validés par ces rapprochements. Auteur Codex, 16 septembre 2026 ; statut proposé, aucun valideur de comparaison. Les modèles d'éditeur et composants ODA ne prouvent ni équivalence de domaine ni couverture installée.


## Retour utilisateur U240 — principes locaux adoptés

Laurent précise le point 1 : le référentiel décrit les services et SLA globaux de configuration ; D06 décrit la capacité logistique dans le contexte, par exemple un nombre maximal de préparations ; D03 utilise D06 pour calculer sa promesse Supply. Ne pas transformer cette contribution en un second calcul de promesse dans D06 ni imposer la qualification technique télécom comme nom de capacité.

Les points 2, 3 et 5 sont acceptés : coordination entre exécutants et autonomie interne, distinction des engagements/prévisions/résultats également pour les services numériques, séparation service métier/accès technique. Le point 4 est confirmé comme tracking des opérations logistiques. Le périmètre général conserve les services non logistiques U237. Les noms, capacités détaillées et correspondances marché restent proposés. Portées exactes et empreintes dans `modeles/backlog/execution-services-review.yaml`, `user_agreements_U240`. Aucune modification de la carte ni publication.

## Comparaison du modèle révisé — U241

L'[étude complémentaire U241](execution-services-revised-comparison.md) compare explicitement les principes U240. ELM136/137 précisent les appuis Microsoft CTP et SAP PP/DS vers aATP ; CMP077 distingue ces analogies de nos frontières métier. Les questions de capacité disponible, consommation par les engagements et réexamen de promesse restent des propositions locales, sans modifier les accords U240.

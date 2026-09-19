# Comparaison du modèle d'exécution révisé — U241

Date : 16 septembre 2026. Auteur : Codex. État comparé : principes U240 de `modeles/backlog/execution-services-review.yaml`, sans restructuration des nœuds D06/D07. Statut : analyse et recommandations proposées ; aucune équivalence ou couverture installée validée. D05 conservé, publication v006 inchangée.

## Appréciation

La séparation retenue est cohérente : le référentiel décrit l'offre et les SLA configurés ; D06 fournit la capacité d'exécution contextualisée et pilote les prestations ; D03 décide de la promesse Supply. Le marché fournit des appuis à ces responsabilités, sans imposer leur regroupement dans nos domaines. Le catalogue commun entrepôt, transport et production documentaire constitue une abstraction FLOW à éprouver, pas un catalogue natif commun démontré chez les trois références.

## Microsoft — une promesse tenant compte des contraintes

Dynamics 365 SCM décrit un CTP tenant compte du stock, de la capacité de production et des temps de transport. Sa documentation distingue aussi une marge de préparation ajoutée à l'ATP. Elle appuie la mobilisation d'informations opérationnelles par la promesse, mais ne prouve pas une interface native de capacité résiduelle de préparation d'entrepôt. Un délai configuré et un plafond de charge sont deux informations différentes. Voir [CTP](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp), ELM136.

L'étude U239 documente les services transporteurs, les ordres spécialisés et événements du mode WMS autonome (ELM133). Ces éléments confortent l'autonomie de l'exécutant et ses échanges avec l'amont. Ils ne démontrent pas un référentiel universel de services d'exécution. La frontière FLOW est une adaptation métier, pas la transcription des modules Microsoft.

## SAP — l'analogie la plus précise pour D06 vers D03

Dans SBC, PP/DS évalue les ressources et composants, crée des propositions d'approvisionnement et transmet leurs dates de disponibilité à aATP, qui détermine la confirmation de la commande. Le transfert d'un résultat de faisabilité vers la promesse est proche de notre frontière. Le contexte reste la production et l'approvisionnement ; il ne démontre pas le contrat logistique envisagé pour D06. Les créations d'ordres du scénario SAP ne sont pas importées dans FLOW. Voir [SBC en PP/DS](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f899ce30af9044299d573ea30b533f1c/4c56297de7c33a0de10000000a42189c.html), ELM137.

Les statuts et le suivi des Freight Orders (ELM134, étude U239) appuient le tracking, les écarts et les engagements opérationnels. Réunir ces responsabilités avec la capacité contextuelle dans un domaine FLOW demeure un choix d'urbanisme, sans présumer une application unique.

## TM Forum — catalogue, qualification et coordination

TMF633 distingue le catalogue ; TMF645 qualifie la disponibilité avant commande ; TMF641 organise les échanges de commandes de service. Ces API fournissent des repères de contrat, pas une taxonomie de capacités logistiques. Voir [TMF645 v5.0](https://www.tmforum.org/open-digital-architecture/open-apis/service-qualification-management-api-TMF645/v5.0) et les sources ELM129–131 dans l'étude U239.

Le composant TMFC007 décrit le calcul d'une date de prestation à partir des ressources/charges ainsi que l'orchestration des dépendances entre commandes de service. Il éclaire notre pilotage ; son contexte télécom et sa granularité empêchent une équivalence complète avec D06. Un exécutant peut fournir un engagement daté pour sa prestation ; D03 conserve la composition de la promesse Supply. Voir [TMFC007 v1.2.1](https://oda-production.s3.eu-west-2.amazonaws.com/v1.0.0/TMFC007_Service_Order_Management_v1.2.1.pdf), fonctions 571 et 598, ELM132.

## Ce qui reste à préciser dans FLOW

Ces propositions ne sont pas des lacunes prouvées par le marché ni de nouvelles capacités adoptées.

1. **Capacité maximale et disponibilité contextuelle.** D03 doit pouvoir interpréter une mesure : service, site, période, unité, charge déjà prise et fraîcheur. Un maximum ne dit pas seul ce qui reste accessible. Il faut aussi éviter d'additionner des plafonds de services qui partagent les mêmes équipes ou quais.
2. **Effet des engagements sur la capacité.** Déterminer quand une demande ou une acceptation consomme de la capacité, puis quand un report ou une annulation la libère. La simple consultation d'un solde expose deux demandes concurrentes au même disponible. Ce point ne prescrit ni réservation obligatoire à toute simulation ni mécanisme technique particulier ; il peut relever de la gestion des engagements existante.
3. **Boucle de révision.** Un fait logistique ou une nouvelle estimation dans D06 peut rendre une promesse intenable. Préciser les informations transmises à D03 et les conditions de réexamen, sans assimiler chaque événement à un recalcul automatique ou à une nouvelle promesse.

Illustration locale, chiffres fictifs : un SLA prévoit une préparation sous 24 h. Pour un créneau donné, D06 connaît un plafond de 1 000 préparations et 850 déjà engagées. Sous hypothèse d'unités homogènes, il reste 150 préparations ; D03 examine une demande de 200 avec le stock, les priorités et le transport. Le SLA seul ne justifie pas la promesse de 200. L'exemple n'adopte ni une formule générale ni un découpage supplémentaire.

## Sources et preuve — complément de l'étude U239

Consultation : 2026-09-16. Synthèses et liens seulement, pas de reproduction des catalogues. Les limites et conditions recensées dans [l'étude U239](execution-services-catalog-and-management.md) restent applicables aux ELM129–135.

| Élément | Référence, nature et édition | Passage réellement consulté et limites |
| --- | --- | --- |
| ELM136 | MKT14 ; fonctionnalité CTP de Dynamics 365 SCM ; documentation en ligne, édition produit non figée | Page ouverte, introduction et options de contrôle des dates. Aucun schéma d'API ni test de produit ; pas de preuve de plafond natif de préparation. Source Microsoft Learn liée ci-dessus. |
| ELM137 | MKT13 ; processus SBC avec PP/DS et aATP ; S/4HANA 2025 FPS01, février 2026 | Texte officiel indexé lu : Use et description du transfert des dates. Ouverture directe sans corps exploitable. Pas d'audit de configuration, licence ou déploiement. Source SAP Help liée ci-dessus. |
| ELM130 / ELM132 | MKT19 ; TMF645 v5.0 et TMFC007 v1.2.1 | Pages revérifiées ; texte PDF pages 9–11, fonctions 571 et 598. Pas d'interprétation des graphiques ni d'audit de conformité. |

## CMP077

Cibles : responsabilités U240 du référentiel, de D06 et D03 ; adaptations discutées de D06/D07, nœuds encore inchangés. Éléments : ELM129–134 et ELM136–137. Relations : appui méthodologique à la séparation configuration/faisabilité/promesse, recouvrements fonctionnels partiels pour coordination et suivi. Les engagements datés de prestation restent compatibles avec la responsabilité Supply de D03. Les trois précisions ci-dessus sont des recommandations locales, sans validation implicite par leur rapprochement marché. Auteur Codex, 2026-09-16 ; statut proposé, aucun valideur ni date de validation.


## Suite U242 — orchestration et adaptation adoptées localement

Laurent approuve le point 3 sur le retour vers le réexamen de la promesse et précise la responsabilité du domaine : orchestrer l'exécution Supply pour permettre tracking et adaptation. Un SLA compatible peut être démenti par un échec opérationnel ; il faut réagir et rechercher une variation du plan. Ce principe complète U240 ; D03 conserve la promesse et les exécutants leurs opérations internes. Les conditions d'adaptation et de réexamen restent ouvertes.

Les points 1/2 sur le disponible et sa consommation restent proposés ; aucune correspondance marché, définition complète ou granularité n'est validée par cet accord. Portées et empreintes : execution-services-review.yaml, user_agreements_U242. La proposition de synthèse de définition y est actualisée et son état antérieur conservé.


## Précision U243 — portée des règles d'adaptation

La latitude d'adaptation reste une question pertinente de fonctionnement, mais Laurent précise qu'elle n'impacte pas le catalogue des capacités. Elle ne conditionne donc pas la définition des capacités d'orchestration, tracking et adaptation. Question conservée séparément dans operating_rule_questions de l'annexe ; aucun changement des correspondances marché.


## Application U244 — correspondance CMP078

Le backlog comporte désormais D06 Execution Management, huit capacités directement rattachées et D14 Execution Service Catalog avec son ingestion. D07 est retiré comme domaine ; ses quatre capacités conservent leurs identités sous D06. CMP078 détaille les appuis et les parties non comparées à cette nouvelle maille ; aucun nouvel accord sur les équivalences de marché. Voir [la description concrète](../connaissance/32-execution-orchestration.md).


## Révision U247 — décisions, visibilité et gestion des Service Orders

Le catalogue appliqué distingue désormais Service Order Management, Capacity Visibility, Orchestration et Adaptation Decision. Qualification et options sont regroupées dans une proposition de Service Decision. CMP079 actualise la comparaison à cette maille ; les fonctions de calcul des éditeurs ne deviennent pas des preuves de responsabilité de calcul dans Capacity Visibility. Les anciennes descriptions U244 restent historiques.

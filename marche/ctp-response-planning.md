# CTP local et Response Planning

14 septembre 2026 — U156. La définition D03.j validée U154 reste inchangée. Le rapprochement porte sur le résultat métier du plan d’adaptation, pas sur une architecture ou un choix de produit.

## Sources examinées

- [SAP Learning — Overview of Order-Based Supply Planning](https://learning.sap.com/courses/discovering-sap-ibp-harmonized-planning-area/overview-of-order-based-supply-planning), cours courant avec contexte 2508, sections Sales Order Confirmation et Response Planning, texte consulté le 14 septembre 2026. Plans d’approvisionnement, confirmations et ajustements d’allocations simulés avant application. Rapprochement fort avec U148 ; processus de planification, pas capacité RBA attestée. Allocation SAP et profil complet de protection local ne sont pas déclarés identiques.
- [Oracle — Analyze and Replan Backlog, 25B](https://docs.oracle.com/en/cloud/saas/readiness/scm/25b/scp25b/25B-sc-planning-wn-f36735.htm), texte consulté : simulation de replanification des commandes, changement de sourcing et fractionnement, puis transmission pour exécution. Recouvrement sur le carnet de commandes, pas preuve de couverture du plan global U148.
- [Kinaxis — Supply Chain Response Management](https://www.kinaxis.com/resources/content/c/supply-chain-respons?x=shovp6), présentation de date/version inconnues, page ouverte et extrait indexé consultés. Cas de commande nouvelle avec contraintes d’approvisionnement et de capacité, scénarios alternatifs comparés. Appui historique/conceptuel, pas vérification des fonctionnalités installées ou actuelles.

## Conclusion d’analyse proposée

Le périmètre est cohérent : produire un plan de changements nécessaire à l’exécution d’une commande, avec impacts et conditions. Response Planning est un nom de marché plus directement rapprochable que CTP seul. Les sources organisent ces aptitudes dans des processus ou offres, ce qui ne dicte pas la maille de notre capability map ni sa couche.

La couverture exacte de toutes les protections et annulations commerciales n’est pas démontrée. Réviser une confirmation n’annule pas juridiquement ou commercialement un Order. Simuler une adaptation ne vaut ni décision d’application ni exécution. D03 peut porter la réponse à une commande ; la planification globale indépendante de cet objectif reste une frontière à examiner, sans étendre FLOW à la planification de saison ou à l’exécution logistique.

Le nom Response Planning est une piste à discuter, pas un remplacement automatique de Capable-to-Promise (CTP). Le modèle validé et la release sont conservés. Le retour U156 permet d’améliorer notre correspondance marché sans remettre en cause la validité du résultat métier adopté.

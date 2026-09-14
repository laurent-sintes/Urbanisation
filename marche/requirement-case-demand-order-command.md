# Requirement, Case, Demand, Order et Command

14 septembre 2026 — U164. Définitions proposées par Codex, à instruire ; aucune nouvelle validation. [Annexe structurée](../modeles/backlog/vocabulary-review.json).

## Distinctions proposées

| Terme | Sens proposé | Frontière |
| --- | --- | --- |
| Requirement | Besoin à satisfaire ; dans notre contexte Supply, préciser la ressource requise et, lorsque connus, la quantité, le lieu et la date. | Ne désigne pas automatiquement une exigence logicielle ni une demande d’achat ; peut provenir d’une commande, d’une prévision ou d’un autre besoin. Recouvrement Demand à instruire, pas deux objets imposés. |
| Demand | Demande adressée aux ressources Supply, constatée ou anticipée ; peut être individuelle ou agrégée. | Ne pas réserver le terme à la couche Case ni à une phase précédant les Orders. Demand et Requirement se recouvrent dans les usages de planification ; pas de séparation universelle brut/formalisé établie. |
| Case | Dossier de traitement d’une situation en vue d’un résultat, avec son contexte, ses décisions, ses activités et son suivi. | Précision proposée au raccourci local Case = demande : le Case organise le traitement, il ne se réduit pas au besoin exprimé. La distinction normative Case/CaseFile reste conservée ; aucune cardinalité avec Order décidée. |
| Order | Commande métier durable de pilotage Supply : contenu applicable de ce qui est demandé ou autorisé, évolutions et situation de réalisation. | Orientation locale U140/U141 conservée ; la présence d’un Order ne prouve ni promesse confirmée, ni couverture complète. Tous types de commandes ; Order ne désigne pas exclusivement notre couche Supply chez les éditeurs. |
| Command | Instruction demandant une action, par exemple réviser une commande ou réserver une quantité. | Peut exprimer une intention métier ; le sens logiciel CQRS est un usage particulier. Ne pas remplacer Order par Command ni assimiler une instruction à un fait réalisé ou une capacité. |

Ces mots ne constituent ni cinq étapes d’un processus ni cinq objets à implémenter. Requirement et Demand se recouvrent selon les contextes ; une séparation brut/formalisé ou prévision/ferme ne résulte pas des sources. La formulation antérieure « Case = demande » était trop courte : Case porte le traitement de la situation, CaseFile ses informations selon CMMN. Cette précision ne retire pas l’orientation Supply/Case adoptée localement.

Une commande de transfert peut représenter un besoin pour le stock source et un apport attendu pour le destinataire. Une prévision peut exprimer une demande sans Order ferme. Il faut donc préciser le point de vue et le degré d’engagement avant de choisir les mots.

## Exemple de travail, sans cardinalité imposée

Pour un réassort, le besoin peut être 100 articles dans un magasin à une date donnée (Demand/Requirement, choix ouvert). Le Case organise le traitement de cette situation. Un Transfer Order peut porter la commande Supply retenue ; modifier sa quantité est une instruction (Command) portant sur cet Order. Ni le nombre de Cases/Orders ni la nécessité d’un Case pour tout Order ne sont établis par cet exemple. La commande peut exister avant sa couverture ou sa promesse confirmée.

## Sources et portée

- [OMG CMMN 1.1, sections 4.1 et 5.3.1](https://www.omg.org/spec/CMMN/1.1/PDF) : Texte des sections consulté le 2026-09-14 ; Case comme traitement d’une situation, CaseFile comme informations du dossier. Le titre de métadonnées fourni par le moteur est erroné, le corps est bien CMMN v1.1.
- [SAP S/4HANA — Net Requirements Calculation for MRP](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/fe39e10a9a864a8f8dc9537704f0fa13/46abce5314894208e10000000a174cb4.html) : Extrait indexé consulté le 2026-09-14 ; ouverture sans texte. Besoins indépendants, clients, dépendants, réservations et prévisions ; édition détaillée non établie.
- [Microsoft Business Central — Plan for new demand order by order](https://learn.microsoft.com/en-us/dynamics365/business-central/production-how-to-plan-for-new-demand) : Texte consulté le 2026-09-14, notamment sources de demande (ventes, composants, assemblage, services, projets) et Supply Orders ; documentation en ligne, version produit non figée.
- [Microsoft — CQRS pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs) : Texte consulté le 2026-09-14 ; les Commands représentent des tâches métier et portent une intention de changement. Appui de vocabulaire logiciel, aucun choix de CQRS pour la plateforme.

Voir aussi [l’étude ECC U154/U155](ecc-requisition-order-case.md) : Purchase Requisition est distincte de Requirement et ne correspond pas automatiquement à Case. Les descriptions de marché ne prouvent aucune configuration installée Beaumanoir. Les usages TM Forum de plusieurs niveaux d’Orders ne sont pas une équivalence automatique entre Product Order et Case local.


## U165 — demande métier d’exécution

Laurent exclut le pattern logiciel Command de la cartographie des capacités. Il propose un autre sens : l’objet métier qui matérialise une demande d’exécution adressée par la Supply à une plateforme de services logistiques ou autre. Cette hypothèse remplace le centre de la proposition U164 pour Command ; le nom reste ouvert. Codex propose de le qualifier provisoirement Execution Command ou Execution Request, sans adoption.

L’univers actuellement nommé Case reçoit une orientation métier plus précise : émergence et affinage des intentions des parties prenantes, demandes et problèmes à résoudre ; la résolution mobilise des Orders Supply. Le nom Case doit être réexaminé parce qu’il décrit une mécanique. Aucun nom de remplacement n’est choisi.

Order reste la commande Supply, travaillée, priorisée et promise. La demande d’exécution précise le résultat confié à un exécutant et ses contraintes ; cet exécutant conserve la responsabilité de ses moyens et décisions propres. L’exemple « préparer et expédier un lot pour un destinataire dans une fenêtre donnée » est une illustration Codex, pas un grain adopté.

Le modèle actif D07 fournit un point d’appui : Execution Requirement Definition exprime les prestations attendues, Execution Commitment Management suit leur prise en charge et Execution Reconciliation les rapproche des faits. Il s’agit d’un rapprochement proposé, sans nouveau lien structuré ni objet créé. Demande transmise, acceptation de l’exécutant et fait réalisé restent distincts ; les retours peuvent conduire à réviser les décisions Supply et le traitement amont.

Cette lecture exprime trois responsabilités sans imposer trois couches techniques, une chaîne obligatoire, une cardinalité Case/Order/Command ou un univers Execution supplémentaire. Logistique hors développement FLOW, en adhérence. Le terme services désigne ici l’offre d’exécution évoquée par Laurent ; il ne transforme pas les capacités en services applicatifs.

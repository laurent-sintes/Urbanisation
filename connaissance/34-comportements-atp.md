# Comportements et ATP — U262 à U264

17 septembre 2026. Comportement est le dernier niveau descriptif sous une capacité (U262). Les quatre définitions ATP sont adoptées U263 ; U264 demande leur implémentation et l’évolution d’Atlas. Les conditions et résultats sont décrits factuellement, sans niveau promotionnel « Advanced ATP ».

## Contrat du modèle

Un nœud `behavior` possède une identité, une définition, des sources et une portée de validation. Une seule relation structurelle `contains` le rattache à une capacité de même couche. Il ne contient aucun enfant. Les relations métier transversales restent distinctes du rattachement et doivent être qualifiées. Ne pas créer de parents à partir des identifiants. Les comportements ne sont pas comptés comme capacités.

## ATP

ATP établit les engagements possibles pour une demande ou un ensemble dans la situation de référence, avec leur couverture. Sa synthèse et son périmètre sont actualisés ; nom, finalité et nature adoptés inchangés conservés. La nouvelle rédaction de synthèse reste proposée, sans transporter l’adoption de l’ancienne définition.

## BHV001

**Existing Commitment Consideration** — Établir les quantités admissibles pour la demande en tenant compte des allocations, protections et réservations, sans double décompte.

## BHV002

**Network Stock Availability** — Établir les possibilités de satisfaction à partir des lieux admissibles, entrepôts, magasins, darkstores ou autres espaces de stockage.

## BHV003

**Operational Availability Timing** — Déterminer quand une quantité peut effectivement contribuer à la promesse selon sa disponibilité opérationnelle.

## BHV004

**Future Supply Projection** — Établir les possibilités à l’échéance en intégrant les réceptions attendues et les engagements concurrents, pour une promesse ou un ensemble.

Les définitions françaises et les rattachements à ATP sont adoptés. Les noms anglais, finalités et périmètres explicatifs ajoutés restent proposés. L’annexe d03-review.yaml conserve les valeurs adoptées et leurs empreintes ; model.yaml porte les nœuds et relations courants. Cette implémentation ne publie pas le backlog.

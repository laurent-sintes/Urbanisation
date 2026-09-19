# Refonte D04 — U363

Arbre courant :

```text
Order Management
├── Order Type
│   ├── Sales Order Management
│   ├── Purchase Order Management
│   ├── Transfer Order Management
│   ├── Customer Return Management
│   └── Supplier Return Management
├── Order Lifecycle Management
│   ├── Order Drafting
│   ├── Order Firming
│   ├── Order Freezing
│   ├── Order Release
│   ├── Order Hold & Resume
│   ├── Order Rescheduling
│   ├── Order Cancellation
│   ├── Order Closure
│   └── Order Splitting
├── Order Structuring
└── Order Archiving
```

Les identifiants D04.i–m sont préservés comme comportements. Type désigne une variante métier ; Lifecycle ses mutations ; Structuring une composition durable ; Archiving la conservation historique. Spread concerne la répartition des ressources, hors D04.

[Portées et descriptions structurées](../../modeles/backlog/order-lifecycle-behaviors.yaml). [Preuve de migration](implementation.yaml). Les snapshots before conservent les validations et l’historique ; aucune release modifiée.

Contrôles effectués : validation du modèle sans erreur, 11 tests comportements/comparaisons marché réussis, audit des migrations et de l’arbre D04 réussi, 125 fichiers publiés ou preuves figées inchangés. Restitutions régénérées. Le backlog comporte désormais 38 capacités et 40 comportements ; cette modification ne constitue pas une nouvelle publication dans l’Atlas.

# Stock et Orders — bilan U219/U220/U221

15 septembre 2026. Mise à jour du backlog uniquement.

Les finalités D01/D03/D05 sont reprises de l’explication acceptée U219. Le nom Inventory Optimization est retenu selon U220. Les trois capacités D05, avec identifiants conservés, précisent les objectifs, besoins nets et redistributions de stock. Les descriptions distinguent la satisfaction d’un Order du stock souhaitable, même lorsqu’un transfert peut servir les deux finalités. Les capacités de D01 et D03 ne sont pas réécrites.

Coverage Target Decision et Stock Redistribution Decision sont des libellés proposés courants ; leur ancienne alternative P86-D05 est historisée dans [le registre de frontière](../../modeles/backlog/stock-order-boundary.yaml), sans adoption implicite. Inventory Balancing est une proposition intermédiaire remplacée par le choix U220.

Le réapprovisionnement automatique U221 figure dans le périmètre proposé et l’annexe de travail, avec complément de stock, déclenchement conditionnel et prise en compte des demandes en cours. Aucune capacité autonome ajoutée par le seul mode automatique. TER074 Replenishment est proposé ; les 98 sens précédents sont conservés à l’identique.

## Conservation et contrôles

- [État complet pré-U219](../../modeles/backlog/history/pre-U219.yaml), copie exacte du modèle avant modification ; empreinte dans le registre de frontière.
- Six nœuds modifiés : D01, D03, D05, D05.a, D05.b et D05.c. Identifiants, toutes les relations, principes et autres nœuds inchangés : [vérification](verification.json).
- Finalités des domaines adoptées U219 ; nom D05 adopté U220. Les autres champs validés inchangés conservent leur portée ; les nouvelles descriptions et règles restent proposées. Une future préparation devra réexaminer la reprise des décisions sur les nouvelles révisions.
- 55 nœuds, 37 capacités et 62 relations dans le backlog ; 99 termes de glossaire.
- Le [contrôle des empreintes de release](release-before.json) confirme que v005 et les versions historiques restent inchangées.
- Correspondances marché explicitement non réévaluées pour les nouvelles formulations ; aucune couverture des SI déduite.
- `refresh_sources.py` : 1095 sources ; `validate_models.py` : zéro erreur ; `render_models.py` : restitutions régénérées ; `git diff --check` : propre.

Les [descriptions lisibles](../../connaissance/30-stock-et-orders.md) sont une restitution datée des champs, pas une autorité concurrente. Aucun code Atlas, aucune publication, aucun commit ni push.

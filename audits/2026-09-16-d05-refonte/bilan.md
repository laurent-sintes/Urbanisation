# Refonte Inventory Optimization — U235

16 septembre 2026. Application au backlog après la proposition U233 et la clarification U234. Aucune publication, aucun commit ni push.

## Résultat

| Identifiant | Capacité | Traitement |
| --- | --- | --- |
| D05.a | Coverage Target Decision | Identité conservée, définition précisée. |
| D05.d | Stock Allocation Decision | Nouvelle capacité. |
| D05.e | Replenishment Decision | Nouvelle capacité, périmètre plus complet remplaçant D05.b. |
| D05.c | Stock Redistribution Decision | Identité conservée, décision distincte du réapprovisionnement. |
| D05.f | Inventory Planning | Nouvelle capacité, mobilise les quatre décisions. |

Les cinq capacités sont directement rattachées à D05. Quatre relations `relates-to` expriment la mobilisation des décisions par Planning, sans relation de décomposition. D05.b Net Requirements Calculation et son rattachement sont conservés dans le snapshot pré-U235 ; aucune identité réutilisée ni validation héritée. Les calculs sont compris dans Replenishment Decision.

Noms et définitions courtes présentés avant l'accord sont repris à l'identique et marqués validés. Les finalités, natures, descriptions détaillées et exemples ajoutés restent proposés. Les rattachements au domaine sont validés ; la formulation technique des liens de mobilisation reste proposée. Conditions et effets non détaillés sont des listes vides explicites.

Définition D05 U223, nom et finalité inchangés. Son périmètre explicatif distingue décisions, Planning, tenue transactionnelle et mise en action. D01/D03/D04 et les autres nœuds sont inchangés. Aucun renommage de Supply Protection ni création de Replenishment Management.

## Preuves et contrôles

- État antérieur exact : [pre-U235.yaml](../../modeles/backlog/history/pre-U235.yaml).
- Portées et empreintes des valeurs adoptées : [d05-refactoring.yaml](../../modeles/backlog/d05-refactoring.yaml).
- Descriptions lisibles actuelles : [Inventory Optimization](../../connaissance/31-inventory-optimization.md).
- Annexe de frontière et revue D03 avant modification conservées dans ce dossier.
- [verification.json](verification.json) : invariants du graphe, empreintes des glossaires séparés et de tous les fichiers de release.
- `python scripts/refresh_sources.py` : 1 133 sources ; aucune preuve publiée réécrite.
- `python scripts/validate_models.py` : **0 erreur** après explicitation des listes techniques `conditions` / `effects` sur les quatre nouvelles relations. La première passe avait signalé ces huit propriétés manquantes ; correction sans invention de règle métier.
- `python scripts/render_models.py` : restitutions régénérées.
- `git diff --check` : aucune erreur.

Backlog : **57 nœuds, 39 capacités, 68 relations**, contre 55/37/62 avant application. Identifiants ajoutés : D05.d/e/f ; retiré : D05.b. Définition D05 adoptée, autres nœuds, autres relations, principes et alternatives inchangés hors périmètre explicité.

Les deux glossaires sont inchangés et restent séparés. La release v005 / 2026-09-15.1 et ses fichiers historiques sont inchangés ; Atlas continue donc d'afficher cette release. Pas de contrôle navigateur pour une modification limitée au backlog.

## Limites

Les exemples chiffrés, autorités détaillées, coûts, horizons et règles d'application ne sont pas validés par leur rédaction. Le responsable opérationnel du déclenchement reste à préciser. La coordination des décisions ne prescrit ni moteur commun ni ordre obligatoire. La couche technique existante est conservée ; le caractère analytique ne crée pas un nouveau niveau d'urbanisme.

CMP075 et le registre de refonte qualifient les rapprochements marché : partiels, avec appui sémantique pour les allocations et équivalence détaillée de redistribution non démontrée. Aucun catalogue éditeur ou déploiement Beaumanoir n'est assimilé au modèle local.

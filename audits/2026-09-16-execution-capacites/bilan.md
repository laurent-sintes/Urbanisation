# Bilan U247 — capacités d’exécution

Application au backlog le 16 septembre 2026, après le Go suivant la clarification U246. Aucune publication, aucun commit ni push.

## Catalogue appliqué

| Identifiant | Capacité | Portée de validation |
| --- | --- | --- |
| D07.a | Execution Requirements Decision | Nom et responsabilité courte du dernier tableau U247. |
| D06.e | Execution Service Decision | Fusion qualification/options appliquée comme proposition ; aucun transfert de validation. |
| D06.b | Execution Capacity Visibility | Nom retenu U246 ; description détaillée proposée. |
| D07.b | Service Order Management | Nom et définition présentée avant le Go U247. |
| D06.d | Execution Orchestration | Nom et responsabilité courte du dernier tableau U247. |
| D07.d | Execution Tracking | Nom repris U247 ; description existante et compléments proposés. |
| D07.c | Execution Reconciliation | Nœud inchangé, avec son statut proposé. |
| D06.f | Execution Adaptation Decision | Nom et responsabilité courte du dernier tableau U247. |

Les huit capacités sont directement rattachées à D06. Finalités, natures, exemples et périmètres détaillés ne sont pas validés par leur application. Les empreintes exactes sont dans les cycles de vie et application_U247 de l’annexe.

## Identités et relations

D06.a et D06.c sont retirées ; leur fusion reçoit D06.e. D06.f distingue l’adaptation de D06.d qui conserve l’orchestration. D07.a conserve la détermination des prestations, précisée comme décision ; D07.b conserve la tenue des prises en charge, explicitée dans le cycle de demande de service. Captures : `modeles/backlog/history/pre-U247.yaml`, `before-description.md` et `before-review.yaml`.

Les anciens liens vers les options et depuis l’orchestration vers Promise Revision sont historisés. Les relations nouvelles relient le tracking à l’adaptation, celle-ci aux services, à la capacité visible, à l’orchestration et à Promise Revision dans D03. La décision de services mobilise la visibilité ; la décision de besoins alimente Service Order Management. Ces qualifications restent proposées et ne prescrivent pas de séquence technique universelle.

## Contrôles

`verification.json` contient les contrôles de portée réussis :

- Tous les nœuds hors capacités modifiées inchangés, notamment D03, D05, D06 comme domaine et D14.
- Toutes les relations antérieures hors retraits ou qualifications explicitement révisées préservées ; cinq contributions D07.c vers D04.i–m identiques.
- Huit capacités dans D06, aucun identifiant retiré encore actif ou utilisé comme extrémité de relation.
- 112 fichiers protégés inchangés : publications et preuves figées, plus les deux glossaires.
- Sources documentaires du modèle et empreintes des champs validés cohérentes.
- `refresh_sources.py` : 1 158 sources ; `validate_models.py` : **0 erreur**.
- Restitutions régénérées ; `git diff --check` réussi.

Résultat : **59 nœuds, 41 capacités, 82 relations**, glossaire métier inchangé à 101 termes. CMP079 actualise les correspondances à partir des études déjà consultées ; aucune nouvelle équivalence de marché affirmée. Atlas conserve la release désignée par son index.

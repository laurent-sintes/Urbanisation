# Bilan U244 — refonte de l’exécution

Application au backlog le 16 septembre 2026. Aucun commit, push ou publication.

## Résultat

- D06 devient Execution Management, avec huit capacités directement rattachées. La définition présentée après U242 est retenue dans la portée de la demande U244 ; le nom et les compléments éditoriaux restent proposés.
- D07 est retiré comme domaine. D07.a–d gardent leurs identifiants et sont rattachées explicitement à D06. Leurs identifiants ne définissent pas leur parent.
- D06.a devient Execution Service Qualification ; D07.d devient Execution Tracking en conservant le suivi des ressources encore attendues. D06.d Execution Orchestration est ajoutée ; son découpage et sa formulation restent proposés.
- D14 Execution Service Catalog et D14.a Execution Service Catalog Ingestion sont ajoutés sous Business References : six référentiels. SLA configurés, service métier et accès informatiques sont distingués de la capacité et du suivi opérationnels.
- Les contributions vers D03 et les relations entre tracking, orchestration, options et engagements sont explicites, avec qualifications proposées. La promesse Supply reste dans D03.
- TER075 Execution Service et TER076 Service Level Agreement sont ajoutés comme propositions ; les 99 termes antérieurs et le glossaire de modélisation sont préservés.

Le catalogue est appliqué ; la latitude d’adaptation reste une question de fonctionnement sans impact sur sa définition, selon U243. Le modèle ne présume ni autorité locale sur les maîtres de référence, ni réalisation interne de la logistique, ni automatisation ou contrôle humain obligatoire.

## Continuité et portée

Capture exacte avant changement : `modeles/backlog/history/pre-U244.yaml`. Glossaire antérieur : `before-glossary.yaml`. L’annexe `modeles/backlog/execution-services-review.yaml` contient les accords U240/U242/U243 inchangés et l’application U244. Le retrait du domaine D07 et de son lien à Supply ne retire aucune capacité ni relation de rapprochement des Orders.

Les portées adoptées et les formulations proposées restent distinguées par lifecycle/review. Quatre rattachements D07.a–d vers D06 et la présentation de D14 transcrivent le regroupement et le nouveau référentiel demandés. Le rattachement de la nouvelle capacité d’orchestration et celui de l’ingestion restent proposés avec leur granularité. Aucun identifiant retiré réutilisé ; aucune validation de D07 transférée à D06.

CMP078 actualise les correspondances marché depuis les études U239/U241 ; pas de nouvelle consultation ni équivalence globale. Les descriptions concrètes figurent dans `connaissance/32-execution-orchestration.md` et les champs du modèle, qui reste l’autorité.

## Vérification

`verification.json` contient les résultats des contrôles de portée :

- D03, D05 et tous les nœuds hors refonte inchangés ; les relations antérieures hors cinq modifications de structure restent identiques.
- Huit capacités dans D06 ; six références présentées ; aucun domaine D07 actif.
- Cinq liens D07.c vers D04.i–m conservés à l’identique.
- Contribution D06 vers D03 et mobilisation de Promise Revision présentes.
- Empreintes des validations et des fichiers source valides.
- 111 fichiers protégés inchangés : publications, entrées figées, décisions, provenance figée et glossaire de modélisation.
- `python scripts/refresh_sources.py` : 1 154 sources ; `python scripts/validate_models.py` : **0 erreur**.
- `python scripts/render_models.py` : restitutions régénérées ; `git diff --check` : réussi.

Backlog résultant : **59 nœuds, 41 capacités, 77 relations, 101 termes métier**. Les illustrations restent dans le backlog. Atlas consulte toujours la release désignée par l’index ; aucun changement du frontend ou du serveur nécessaire pour cette mise à jour du backlog.

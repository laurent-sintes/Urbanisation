# Release v007 — U248

Publication locale **2026-09-16.2**, descripteur `urbanisation-v007-2026-09-16-094222.yaml`. Activation le 16 septembre 2026. Aucun commit ni push.

## Contenu publié

55 nœuds, 41 capacités, 74 relations et 101 termes métier. D06 regroupe huit capacités d’exécution ; D07 est retiré comme domaine, ses capacités conservent leurs identités et leurs rattachements explicites à D06. D14 Execution Service Catalog et son ingestion portent le sixième référentiel. D05 est conservé.

Service Order Management et Execution Capacity Visibility reprennent les accords U246/U247. Orchestration et Adaptation Decision sont distinctes. Execution Service Decision regroupe qualification/options comme proposition. Les qualifications des nouvelles relations et descriptions détaillées restent proposées. Les liens vers D03 préservent sa responsabilité de promesse Supply ; les cinq contributions de rapprochement vers D04 sont conservées.

Deux termes ajoutés : TER075 Execution Service et TER076 Service Level Agreement, proposés ; les 99 termes antérieurs sont inchangés. Aucun impact lexical signalé. Le glossaire de modélisation est figé comme contexte séparé, sans ajout au glossaire métier. Quatre nœuds illustratifs et huit relations illustratives du backlog restent exclus de la publication ; alternatives, annexes et applicabilité restent du contexte.

## Validation et provenance

96 décisions : **82 reprises compatibles et 14 nouvelles transcriptions sourcées**, aucune suspension. Les transcriptions portent sur les seuls champs déjà adoptés dans U240/U244/U246/U247 et les rattachements U238/U244/U245/U247. Le Go est interprété dans son contexte, sans étendre les accords aux compléments éditoriaux. U248 autorise la publication, pas de nouveaux arbitrages métier.

Le rapport initial signalait les portées lifecycle sans décision de publication correspondante. Elles ont été transcrites dans `new-decisions.json` aux révisions calculées du candidat ; rapport préparé et validation finale sans erreur. Les décisions antérieures restent conservées, aucun historique réécrit.

## Vérifications

- Préparation et activation par `prepare_release.py`, publication source U248.
- `validate_models.py` : **0 erreur**, 96 décisions ; restitutions régénérées.
- `app/server.py --check` : frontend prêt, 55 nœuds et 41 capacités publiés.
- Serveur existant FLOW Atlas sur 8765, racine du dépôt et espace release vérifiés ; aucun redémarrage nécessaire pour les seules données.
- `/api/model` : version et chemin exacts, égalité intégrale des nœuds, relations et glossaire avec le snapshot publié. `/api/releases` désigne la nouvelle version.
- Navigateur : v007 affichée, huit capacités sous Execution Management, six référentiels, fiche Service Order Management avec nom/définition adoptés et détails proposés ; glossaire 101 termes, fiche TER075 dans la même publication.
- 113 empreintes capturées avant publication : seul `release/index.json` a changé intentionnellement. Les 112 autres fichiers protégés, dont le backlog et ses glossaires, restent identiques.

Preuves locales : `initial-report.json`, `reviewed-report.json`, `new-decisions.json`, `protected-before.json`, `atlas-api.json` et `verification.json`. Les anciens modèles restent sélectionnables ; un lien vers une version historique reste fixe.

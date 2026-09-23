# Point de reprise — U626

**Mise à jour du 23 septembre 2026 : reprise effectuée et lot terminé.** Voir [le compte rendu final](compte-rendu.md) et [les contrôles finaux](verification-final.json). Les sections ci-dessous conservent l'état exact de la suspension du 22 septembre ; elles ne décrivent plus du travail en attente.

**Suspendu à la demande de Laurent le 22 septembre 2026 pour éteindre l'ordinateur.** L'écriture en cours s'est terminée avec un code de sortie 0. Aucun processus lancé par ce lot ne reste en cours. Aucune release, aucun commit ni push effectué.

## Objectif à reprendre

Laurent a demandé : « Tu peux mettre à jour un maximum de notions ? », à la suite de l'audit U625 sur glossaire, métamodèle, Domain et Purpose. Terminer la consolidation, contrôler le résultat et restituer les acquis et les formulations encore proposées. La suspension ne vaut pas validation métier du lot.

## État enregistré

- Contribution U626 ajoutée dans `connaissance/01-contributions-utilisateur.md`.
- Captures exactes des quatre fichiers métier avant modification dans `before/` ; empreintes dans `inputs.json`. Ne pas modifier ces preuves ni celles de l'audit U625.
- Backlog organisé en six Purposes : Reference & Policy Management (`business-references`), Demand Management (`D04`), Supply Management (`D18`), Inventory Management (`D01`), Demand & Supply Optimization (`D03`), Fulfillment Orchestration (`D06`).
- Anciens Purposes D05, D15 et D17 retirés du catalogue courant, avec leur état antérieur et succession conservés dans `modeles/backlog/model-consolidation-U626.yaml`. Les capacités existantes gardent leurs identifiants.
- Promesse et Demand Planning rattachés à Demand ; décisions de couverture et ajustement regroupées en D03 ; Supply Protection déplacée dans le Purpose références/policies et qualifiée Policy.
- Capacités proposées ajoutées : Supply Visibility (`D18.a`), Service Provider Policy (`D19.a`), Demand Protection Policy (`D19.b`), Consignment Pick-up Order (`D04.t`). Le modèle contient désormais 59 capacités.
- D07.b devient Service Task Management, avec pilotage de la Task et document Service Order optionnel. D04.r devient Consignment Fill-up Order, avec les deux perspectives de consignation proposées.
- Glossaire : huit termes ajoutés (TER089–TER096), Service Order et Return Order harmonisés ; environ trente entrées modifiées ou ajoutées au total. Métamodèle : cinq entrées ajoutées (MOD015–MOD019), Purpose et gouvernance clarifiés.
- Guide méthodologique, AGENTS.md et cadrage courant de CONVENTIONS-MODELE.md actualisés.
- Affichage Purpose préparé dans `app/src/model.ts`, `types.ts`, `presentation.ts`, `dependencyGraph.ts`, activé par `PRINCIPLE-DOMAIN-PURPOSE` dans le snapshot ; les anciens snapshots doivent garder Area.
- Même activation dans `scripts/render_models.py` ; contrôles opt-in de finalités non vides et rattachement à exactement un Purpose dans `scripts/validate_models.py`.
- Tests ajoutés dans `scripts/test_model_levels.py` et `app/test-dependency-graph.mjs` ; **pas encore exécutés**.
- Dernière commande terminée : `python audits/2026-09-22-model-update-U626/finalize_content.py`, résultat : 77 nœuds, 29 relations, 30 termes et 8 entrées méthodologiques modifiés ou créés par rapport aux captures. Voir `changes.json`.

## Contrôles encore à faire — aucune affirmation de validation du lot

1. Relire le résultat final et les transformations éditoriales. Les scripts datés ont utilisé des remplacements : vérifier spécialement que noms natifs d'éditeurs, titres de sources, références historiques et preuves n'ont pas été renommés dans les champs d'inspiration. Les comparer aux captures `before/` et corriger uniquement les textes courants concernés.
2. Vérifier les renvois : aucun lien vers les Purposes retirés ; ne pas confondre D05 avec les capacités D05.a, D17 avec D17.a, etc. Les champs courants ont été réécrits, mais rechercher aussi dans le catalogue Informations interne et dans les liens structurés du guide. Ne pas étendre ce catalogue masqué.
3. Vérifier la cohérence de la description du plan commun : D03.p et D05.f sont conservés comme contributions complémentaires, sans deux plans finaux indépendants. La refonte détaillée des comportements du plan reste un chantier distinct, non réalisée ici.
4. Examiner les champs `lifecycle`, `proposed_fields` et la portée des accords. Les anciennes preuves du registre sont préservées ; les champs modifiés ne doivent pas rester présentés comme approuvés. U626 autorise le travail, pas toutes les nouvelles formulations et affectations. Les noms explicitement adoptés auparavant (U581, U590) peuvent être capturés séparément avec `record_intents` si leur contextualisation exacte est confirmée ; **aucun nouvel accord n'a encore été enregistré pendant U626**.
5. Lancer `python scripts/refresh_sources.py` : U626 n'est pas encore dans l'index des sources. Puis lancer une fois `python scripts/validate_models.py` et corriger les erreurs réelles. Le résultat zéro erreur de U625 concerne l'état précédent, pas ce lot.
6. Exécuter les tests concernés : au minimum `python -m unittest scripts.test_model_levels scripts.test_glossary scripts.test_market_comparisons scripts.test_market_reference_policy scripts.test_lifecycle scripts.test_data_governance scripts.test_modeling_guide_publication`, puis les tests frontend de modèle, publication, guide et dépendances. Ajouter d'autres tests seulement si les changements ou échecs le justifient.
7. Lancer `python scripts/render_models.py --space backlog`, puis `pnpm --dir app build`. Aucun navigateur ni redémarrage serveur requis pour cette demande.
8. Vérifier la conservation des publications et archives ; produire le compte rendu final du lot et le statut de clôture des écarts U625. Ne pas réécrire l'audit initial comme s'il avait examiné le nouvel état.

## Précautions de reprise

`apply_update.py` et `finalize_content.py` sont des migrations datées de ce lot, pas des commandes de maintenance à rejouer aveuglément. Les sources sont déjà écrites. Continuer depuis les YAML actuels avec `scripts.structured_io`, en utilisant les captures pour contrôler les deltas. `apply_update.py` refuse un lot déjà appliqué ; `finalize_content.py` peut ajouter des mentions en doublon à l'annexe s'il est rejoué.

Le dépôt comportait déjà de nombreux changements avant U626. Ne pas les annuler ni attribuer tous les diffs à ce lot. Aucune publication ni autorisation globale supplémentaire à inférer. Les nouvelles formulations et capacités restent proposées lorsque l'accord explicite antérieur ne couvre pas leurs champs.

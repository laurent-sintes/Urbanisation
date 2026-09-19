# Refonte appliquée — U290

Le backlog contient désormais **39 capacités et 14 comportements**. La refonte porte sur le socle recommandé U286–U289 ; elle conserve la profondeur Capacité → Comportement. Les publications et la version consultée dans Atlas sont inchangées.

Autorité : [modèle courant](../../modeles/backlog/model.yaml) et [registre de migration](../../modeles/backlog/refactoring-implementation.yaml). La [cible initiale](../2026-09-17-refonte-modele/rapport.md) conserve la revue avant application.

## Changements appliqués

| Ensemble | Résultat |
| --- | --- |
| Promise Management | D03.n remplace trois capacités ; proposition, confirmation et révision deviennent BHV021–023. |
| Inventory Planning | Scenario Construction, Simulation & Analysis, Scenario Execution Adaptation. Comparaison, autorisation et mise en action restent décrites. |
| Supply Protection | Group Supply Protection, Consumption Capping, Safety Stock Policy, Replenishment Regulation. Les opérations sur enveloppes restent dans le périmètre. |
| ATP | Quatre comportements et leurs accords préservés intégralement. |
| Supply Assignment | Maximiser la valeur multidimensionnelle de la satisfaction des commandes sous contraintes ; ni volume seul, ni marge seule. |
| D05.d | Group Protection Decision remplace le nom ambigu Stock Allocation Decision, sans changer le résultat attendu. |
| D04.o et D05.e | Cycle de vie qualifié management ; ajustements des apports futurs explicités sous contraintes. L’application des conséquences de plans sur les Orders est décrite. |

## Portée de validation

U290 autorise cette mise en œuvre et confirme la finalité de valeur multidimensionnelle. Les descriptions de synthèse, exemples fictifs et contrats détaillés ajoutés restent éditoriaux ; le cycle de vie conserve seulement les accords correspondant aux valeurs effectivement inchangées ou aux libellés retenus. Les décisions historiques et leurs empreintes ne sont pas réécrites.

Les arbitrages spécialisés restent distincts : Order Prioritization pour les priorités, ATP/CTP pour les possibilités et la faisabilité, PTP pour le compromis économique, Delivery Schedule Decision pour les échéanciers. La finalité de valeur de Supply Assignment ne crée pas une décision générale absorbant ces capacités.

## Dépendances et identités

Les 133 contrats proposés ont tous une destination tracée ; 130 relations les portent après regroupement des contrats équivalents. Les dépendances devenues internes à Promise Management ne créent pas de boucle. Les relations de sens différent et les liens objets/documents/événements sont préservés. Les contrats détaillés sont en instruction, pas déclarés validés collectivement.

| Identifiant retiré | Destination |
| --- | --- |
| D03.a — Promise Proposal | BHV021 — Promise Proposal |
| D03.b — Promise Confirmation | BHV022 — Promise Confirmation |
| D03.c — Promise Revision | BHV023 — Promise Revision |
| BHV007 — Scenario Evaluation | D05.f — Inventory Planning |
| BHV008 — Scenario Validation | D05.f — Inventory Planning |
| BHV009 — Scenario Application | D05.f — Inventory Planning |
| BHV010 — Scenario Impact Analysis | BHV006 — Simulation & Analysis |
| BHV011 — Allocation | D02.b — Supply Protection |
| BHV012 — Reallocation | D02.b — Supply Protection |
| BHV013 — Allocation Release | D02.b — Supply Protection |
| BHV014 — Allocation Consumption | D02.b — Supply Protection |
| BHV015 — Allocation Visibility | D02.b — Supply Protection |

Ces correspondances assurent la traçabilité de migration et la réécriture des liens actifs. Elles ne redirigent pas les liens de publications anciennes : chaque publication reste autonome. Les identifiants retirés ne sont pas réutilisés.

## Points maintenus ouverts

- A3 : articulation réservation/affectation et décompte sans doublon.
- A6 : quatre comportements optionnels Stocktaking/Orchestration non créés.
- A7 : contrats détaillés intégrés sous instruction, données/conditions à éprouver.
- A8 : application de plan explicitée dans D04 ; parent transverse du comportement encore ouvert.

## Étape suivante — U291

Examiner les capacités encore peu décrites en comportements, en partant de cas métier et de mécanismes documentés sur le marché. Pour chaque ajout, démontrer une complexité ou un bénéfice ciblé ; ne pas réintroduire de listes de fonctions ni chercher une décomposition uniforme. Cette étape est demandée pour après la refonte et n’est pas engagée dans cette passe.

## Comparaison marché et contrôles

Les choix s’appuient sur la [comparaison de la cible](../2026-09-17-refonte-modele/sources.md) et la [convention Assignment](../../marche/assignment-allocation-convention.md). [Microsoft Intelligent Fulfillment Optimization](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/ifo-arch) documente objectifs métier et contraintes, notamment les coûts ; cela appuie une finalité plurielle, sans prescrire les dimensions ni les pondérations FLOW.

Contrôles structurels : 71 nœuds, 216 relations ; chaque comportement possède un seul parent capacité, tous les retraits sont tracés, quatre enregistrements ATP identiques, 125 fichiers historiques protégés inchangés. [Résultats](checks.json). Les tests et la validation générale complètent ces contrôles ; ils ne valent pas validation métier.

Régénération : `python -m scripts.render_refactoring_implementation`.

## Vérification finale

Validation générale : 0 erreur. Les 24 tests comportements/préparation de publication passent, dont un après relance ciblée à la suite d’un refus d’accès Windows sur le renommage d’un dossier temporaire. Aucune modification de code pour contourner cet incident. Vues dérivées régénérées et git diff --check sans anomalie. Les 125 fichiers historiques protégés sont inchangés.

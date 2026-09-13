# D01 — Complétude de la publication

13 septembre 2026 — demande [U124](../connaissance/01-contributions-utilisateur.md#u124). Audit documentaire et contrôle local ; aucune nouvelle comparaison externe ni validation métier.

## Conclusion

La publication v001 (`2026-09-13.3`) et l'API Atlas présentent les cinq capacités courantes du backlog. Aucun nœud D01 supplémentaire perdu lors de cette publication n'est établi. Cette concordance technique ne démontre pas la complétude métier du domaine : des précisions discutées ne sont pas explicites dans les définitions structurées.

Le souvenir d'un ledger reste non résolu. Aucune occurrence antérieure de ce terme n'a été retrouvée dans les fichiers textuels du projet ni dans les messages utilisateur et assistant du journal local de cette conversation avant U124. Cela ne prouve pas qu'il n'a jamais été évoqué ailleurs.

## Cheminement retrouvé

| État | Nombre et périmètre | Devenir |
| --- | --- | --- |
| A23 / U36, puis lecture U37 | Huit hypothèses autour du stock et des commandes ; sept après exclusion de la commande client dans la grille des natures. | Stock, visibilité, disponibilité, définition des protections, protections en vigueur, engagements de ressources et révision des promesses. Ce périmètre traverse plusieurs domaines ultérieurs. |
| P81 après U74/U75 | Six capacités dans D01. | Positions, faits de stock, visibilité, Stocktaking, Supply Protection et Reservation. |
| P82 / U83, noms précisés U84/U86 | Cinq capacités proposées. | Positions et faits réunis dans Inventory Tracking ; les quatre autres aptitudes sont conservées. |
| U116 | Cinq capacités retenues comme base courante du backlog. | Accord de travail explicite, sans nouvelle validation métier. |
| Publication v001 | Cinq capacités reprises. | Inventory Tracking, Inventory Visibility, Stocktaking, Supply Protection, Reservation. |

Sources : [grille des natures U37](../connaissance/19-glossaire-metier.md), [exploration du stock](../connaissance/17-exploration-bloc-stock.md), [P81/P82](../connaissance/25-domaines-coeur-et-epreuve-recits.md#proposition-de-cinq-capacités-d01-u83), [audit U115/U116](2026-09-13-atlas-d01.md).

Les réponses originales de la tâche « Intégrer les synthèses ChatGPT » ont été relues : tour `01a08a35-b313-76f2-a42e-38ac94637eef` pour les huit hypothèses ; `01a09014-cf00-7012-8158-eee96ef82af2` pour D01 à six ; `01a09025-fd46-7c72-9917-c4d820a64f13` pour la proposition à cinq. La consultation paginée a restitué 62 tours, dont huit sans contenu ; la recherche du terme ledger a donc été complétée dans les messages du journal local de la conversation. Les résumés ci-dessus sont des reformulations, pas des verbatims.

## Ledger et écarts de précision

Si ledger désigne le registre des faits expliquant les variations du stock, le résultat métier le plus proche était **D01.b — Record inventory facts**, désormais regroupé avec D01.a dans **D01.e — Inventory Tracking**. C'est une interprétation à confirmer, pas une correspondance historique démontrée. Le mot ledger ne permet pas à lui seul de choisir entre objet, document et capacité autonome.

| Sujet | Précision dans les sources | État structuré publié et point à reprendre |
| --- | --- | --- |
| Inventory Tracking | D01.a précisait article, lieu, détenteur et propriétaire ; D01.b expliquait entrées, sorties, changements d'état et consommations. | La fusion conserve faits, effets, physique/logique et futur, mais ces dimensions et exemples ne sont plus explicites dans la définition. Vérifier leur restitution lors de l'enrichissement des objets et faits. |
| Supply Protection | P82 précise validité et règles de consommation. Les anciennes CAP distinguaient définition des protections et protections en vigueur. | La définition conservée de P81 indique établir et appliquer les limites et leur validité ; les règles de consommation sont moins explicites. Les deux anciennes CAP ne sont plus deux capacités D01 autonomes. |
| Reservation | P82 précise engager, ajuster et libérer pendant le cycle. | La définition conservée de P81 indique seulement établir un engagement et ses effets concurrents. Ajustement et libération ne sont pas explicites. |

Ces écarts sont des pertes de précision dans la consolidation, pas la preuve de capacités autonomes manquantes. La prochaine reprise du backlog doit les traiter à partir des sources et éclaircir ce que Laurent désigne par ledger avant de proposer une nouvelle décomposition.

## Vérification et portée

- Comparaison directe des fichiers `modeles/release/2026-09-13.2/model.json` et `modeles/release/2026-09-13.3/model.json` : six puis cinq capacités D01.
- Lecture de `/api/model` sur le serveur local : cinq noms conformes à la publication v001.
- Recherche textuelle ledger dans connaissance, marché, audits, modèles, archives textuelles, application, prototype, puis dans l'historique de la présente conversation : aucune occurrence antérieure retrouvée.
- Le contrôle ne constitue ni une extraction des archives binaires, ni une recherche exhaustive de toutes les autres conversations.
- Aucun modèle ni fichier de release modifié par cet audit. Le nombre cible et le rôle du ledger restent à éclaircir.

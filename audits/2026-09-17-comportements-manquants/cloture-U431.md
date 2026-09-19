# Clôture de l’audit des comportements — U431

Clôture adoptée le 2026-09-19. Clôture du catalogue de capacités et comportements de l’audit existant ; aucun changement de catalogue.

Catalogue conservé : **47 capacités et 74 comportements**.

## Candidats soldés

| Candidat | Couverture existante | Justification |
| --- | --- | --- |
| P04 | D06.d Process Orchestration | La coordination des prestations et de leurs dépendances appartient à la définition de Process Orchestration. Aucun mécanisme distinct justifiant un comportement supplémentaire. |
| P10 | D07.d Operations Tracking | Operations Tracking et ses quatre comportements rendent visibles progression, écarts, attentes et échecs physiques ou numériques. La détection transverse des exceptions ne justifie pas un doublon. |
| P12 | D05.a Inventory Target Decision | Inventory Target Decision détermine déjà objectifs et seuils selon besoins, service, délais et risques. Ses comportements magasin, centre de distribution et multi-échelon intègrent ces critères ; aucun bénéfice distinct établi pour le candidat. |

Les 16 candidats de l’audit sont soldés : 12 intégrés, 3 couverts par l’existant et 1 retiré.

## Frontière de l’univers

Les responsabilités commerciales et financières restent externes à Supply Chain Orchestration. Le modèle conserve le devenir des biens, les demandes, les prestations et les stocks. Les échanges avec les services externes restent descriptibles sans absorber leurs responsabilités.

## Travaux ultérieurs non bloquants

- **Reservation / Supply Assignment** : Quel effet un lien d’affectation produit-il sur les usages concurrents, et à quel moment existe un engagement opposable ?
- **Application d’un plan aux Orders** : Le plan change-t-il les liens d’affectation, le contenu/structure des Orders, leur état, ou plusieurs de ces objets ?
- **Interfaces commerciales et financières** : Préciser les autorisations, résultats et conditions échangés, ainsi que le rattachement externe si nécessaire.
- **Disponibilité et capacité opposables** : Quels états, unités, horizons et dates d’effet rendent une ressource réellement engageable ?

Les précisions déjà signalées sur les critères de décision, les options admissibles et les tolérances fournisseurs restent également des règles à instruire selon les cas. Aucune nouvelle étude ni reprise générale des liens déclenchée.

## Portée de la clôture

Ne valide pas globalement les champs éditoriaux, contrats, règles ou comparaisons ; ne prouve ni complétude du marché ni couverture installée ; aucune release.

Sources : U431, exclusion Supply U429 ; comparaisons de frontière ELM254/ELM255 et CMP165/CMP166. Preuves conservées dans `modeles/backlog/history/behavior-audit-closure-U431/`.

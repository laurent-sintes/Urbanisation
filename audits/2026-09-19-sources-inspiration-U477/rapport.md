# Reprise complète des Sources d’inspiration — U477

Les **247 fiches** du périmètre sont couvertes : **137 fiches du modèle et 110 termes du glossaire métier**. La rédaction de Supply Chain Orchestration retenue en U475 est conservée ; **246 fiches sont reprises**, dont **127 auparavant sans référence** et 119 avec des comparaisons existantes.

Le résultat est intégré dans [le modèle backlog](../../modeles/backlog/model.yaml) et [le glossaire métier](../../modeles/backlog/glossary.yaml). [La restitution du backlog](../../restitutions/backlog.md) contient les 247 rubriques. La publication courante reste **v014 / 2026-09-19.7** : cette intervention ne produit pas de release.

## Contenu livré

Chaque fiche comporte un choix FLOW en ouverture, un tableau des noms, périmètres et approches, une synthèse comparant les sources entre elles et avec FLOW, puis un cas concret. Les exemples réellement donnés par les sources sont attribués ; les cas construits sont signalés comme illustrations FLOW. Les détails bibliographiques et limites restent consultables.

Les 246 rédactions nouvelles portent **502 comparaisons**, **246 exemples** et s’appuient sur **156 documents primaires distincts**. Chaque fiche possède au moins deux documents pertinents ; plusieurs pages d’un même organisme ne constituent pas une preuve de consensus. La recherche et les consortiums sont mobilisés lorsqu’ils apportent un éclairage précis, sans remplir artificiellement une catégorie de sources sur chaque fiche.

| Lot | Fiches du modèle | Termes | Total | Relevé |
| --- | ---: | ---: | ---: | --- |
| Commandes et leurs variantes | 42 | 23 | 65 | [Comparaisons](orders-output.yaml), [sources](orders-sources.yaml) |
| Stocks, protections et optimisation | 44 | 26 | 70 | [Comparaisons](inventory-output.yaml), [sources](inventory-sources.yaml) |
| Promesse et affectation | 24 | 16 | 40 | [Comparaisons](promising-output.yaml), [sources](promising-sources.yaml) |
| Notions fondamentales | 0 | 13 | 13 | [Comparaisons](foundations-output.yaml), [sources](foundations-sources.yaml) |
| Référentiels, services et suivi | 26 | 32 | 58 | [Comparaisons](references-output.yaml), [sources](references-sources.yaml) |
| **Reprise U477** | **136** | **110** | **246** | [Registre documentaire commun](consulted-documents.yaml) |

Les documents communs à plusieurs lots sont comptés une seule fois dans le total de 156. L’univers Supply déjà rédigé complète la couverture de 247 fiches.

## Choix de rédaction et de preuve

- Les rapprochements justifient chaque fiche à son propre niveau. Un comportement ne recopie pas la justification générale de sa capacité et un domaine ne devient pas une liste de fonctions d’un éditeur.
- Les noms identiques qui recouvrent des effets différents sont expliqués : Allocation, Confirmation, Release, Supply, Service et Catalog notamment.
- Les références trop générales ou ne soutenant plus le rapprochement sont remplacées par des passages plus précis. Les anciennes valeurs et leur provenance restent dans [la capture antérieure](before/) et les relevés des lots.
- Les notices ou passages primaires indexés utilisables restent explicitement distingués d’une lecture intégrale. Une page vide, bloquée ou inaccessible n’est pas présentée comme relue ; aucune version non vérifiée n’est inventée.
- Les conventions locales, notamment CTP dans FLOW, Spread, Movement Authorization et les verbes métier, ne sont pas présentées comme des définitions universelles.
- Les références reçues depuis des maîtres externes, la demande de prestation, la prise en charge, la réalisation, l’estimation et l’engagement restent distincts.

Les nouvelles correspondances sont **proposées**. U477 autorise leur rédaction complète ; il ne constitue pas une adoption de toutes leurs formulations. Les noms, définitions, responsabilités, parents, relations, accords et empreintes d’accord antérieurs sont préservés. Le catalogue Informations métier reste masqué et n’est pas étendu.

## Vérifications

- Identifiants attendus : 246 deltas, aucune omission ni duplication ; univers Supply inchangé.
- Contrats réels des comparaisons et profils : aucun champ obligatoire manquant, synthèses sous forme de listes, exemples sourcés, au moins deux documents distincts par fiche.
- Relecture croisée : [Orders](orders-review.md), [Foundations](foundations-review.md), [References](references-review.yaml), ainsi que relecture des 70 fiches Inventory et des 40 fiches Promising. Correction d’un lien proposition/promesse et de libellés de sources ; réserves internes retirées de plusieurs synthèses publiques.
- `python scripts/refresh_sources.py` : 1 906 sources indexées.
- `python scripts/validate_models.py` : **0 erreur**.
- `python -m unittest scripts.test_market_inspiration` : **10 tests réussis**.
- `python scripts/render_models.py --space backlog` : restitution régénérée, **247 rubriques** ; cibles des liens éditoriaux valides.
- Égalité structurelle vérifiée hors champs Sources d’inspiration et provenance ajoutée. **613 fichiers protégés inchangés octet par octet**, dont publications, révisions, décisions, preuves et autres annexes du backlog.

[Résultat machine](integration.json), [empreintes des fichiers préservés](preserved-files.json), [inventaire de périmètre](inventory.yaml). Registres : MKT57–MKT66, ELM327–ELM482, CMP189–CMP193. Les deltas et scripts de rédaction sont des traces de travail ; les seuls catalogues d’autorité restent les YAML du backlog. Les relectures finales ont corrigé certains deltas : ne pas les remplacer en relançant un ancien script de rédaction.

Aucun code applicatif n’a changé dans cette reprise. Aucun nouveau build, navigateur, audit des comportements, commit, push ou publication n’a été déclenché.

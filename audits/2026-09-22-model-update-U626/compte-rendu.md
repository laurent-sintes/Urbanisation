# Consolidation U626 — terminée le 23 septembre 2026

Le backlog a été consolidé à partir de l'audit U625 et des décisions antérieures de Laurent. Il comprend **six Purposes, 59 capacités, 120 termes métier et 19 notions méthodologiques**. Le lot est terminé et contrôlé ; aucune release n'a été lancée.

## Changements métier

| Purpose | Responsabilité clarifiée |
| --- | --- |
| Reference & Policy Management | Références et policies réunies ; gouvernance des données indépendante du type de capacité |
| Demand Management | Intention, exigences, demande prévisionnelle et promesse de satisfaction |
| Supply Management | Apports attendus, échéances, qualification et incertitudes |
| Inventory Management | Stock, mouvements, réservations et positions projetées |
| Demand & Supply Optimization | Plan commun et décisions de couverture, ajustements autorisés avant exécution |
| Fulfillment Orchestration | Tasks, sollicitation des services, suivi, vérification de fin et re-sourcing |

Les anciens Purposes D05/D15/D17 sont conservés comme preuves dans l'annexe du lot ; leurs capacités conservent leurs identifiants. Les nouvelles responsabilités matérialisées sont Supply Visibility, Demand Protection Policy, Service Provider Policy et Consignment Pick-up Order. Backing Service Orders devient Service Task Management ; la Task gouverne la sollicitation et peut produire un document Service Order. Consignment Fill-up Order qualifie la mise en consignation, avec les deux perspectives proposées. Consignment Issue reste un comportement de Sales Order.

Le glossaire distingue désormais Task, Service, Service Order, Service Catalog, Service Provider Policy, Consignment, Fill-up, Pick-up, Issue et Re-sourcing ; Return Order et Transfer Order ont été harmonisés. Huit entrées ont été ajoutées, trente entrées modifiées ou créées par rapport à la capture initiale. Les notions Capability, réalisation, fonction, fonctionnalité de produit et regroupement ont reçu une autorité méthodologique explicite, avec conservation des termes et renvois historiques.

## Traitement des constats U625

| Constat | Résultat du lot |
| --- | --- |
| A01 — responsabilités dispersées | Six Purposes matérialisés ; promesse dans Demand, policies réunies et apports attendus explicites |
| A02 — contradiction D17 | Ancien Purpose retiré ; Demand Planning reste identifié D17.a dans Demand, plan de couverture en D03 |
| A03 — Task / Service Order | Définitions et capacité de gouvernance alignées ; document optionnel, fin de service distincte d'un acquittement |
| A04 — frontière d'exécution | Règle avant/après début d'exécution et reprise ciblée écrites dans les scopes concernés |
| A05 — Purpose | Métamodèle, guide, rendu Markdown et affichage adaptés ; anciens snapshots conservant Area |
| A06 — glossaire | Notions manquantes ajoutées, noms courants et renvois harmonisés ; autorités méthodologiques précisées |
| A07 — marché | Correspondances réaffectées aux responsabilités ; différences et limites conservées ; compléments de preuve sur Task, policies et consignation |
| A08 — contrôles | Finalités obligatoires et rattachement unique contrôlés pour les états adoptant le principe Purpose ; historiques non soumis rétroactivement |

Ces corrections clôturent les incohérences ciblées dans le backlog de travail, sans transformer les nouvelles formulations en accords. La refonte détaillée des comportements du plan commun reste distincte : les capacités de planification conservées décrivent leurs contributions complémentaires, pas deux plans finaux concurrents. Le signal et la maille du début d'exécution partielle restent à préciser au niveau du contrat métier concerné.

## Validation et intégrité

- Validation complète : **0 erreur**, 71 intentions enregistrées, aucun fragment non référencé.
- Tests Python concernés : **30 tests + 7 tests lifecycle réussis**.
- Tests frontend : suite initiale de 52 tests réussie ; après correction de la carte mixte références/policies, les 34 tests concernés ont été rejoués avec succès.
- Build frontend réussi ; avertissement de taille de chunk, sans échec de compilation.
- Restitution backlog régénérée ; les 59 capacités ont exactement un Purpose ancêtre.
- Titres et métadonnées des sources conservées comparés aux mêmes emplacements de la capture antérieure : aucun renommage accidentel trouvé.
- Captures initiales intactes ; aucune modification des fichiers publiés sous `modeles/release`.

La carte d'un Purpose réunissant références et policies montre maintenant les deux catégories ; les seules références ne masquent plus les capacités de policy.

Les tests frontend qui lancent le lecteur Python des snapshots ont nécessité de sortir du sandbox Windows après un échec `spawn EPERM` ; ils ont ensuite réussi. Les premiers échecs de schéma et de fixture ont été corrigés avant le contrôle final.

## Accords et publication

Deux intentions ont été enregistrées en une écriture, limitées aux **noms** déjà adoptés : Demand & Supply Optimization (U581) et Service Provider Policy (U590). Les définitions, nouveaux noms de capacités et rattachements détaillés introduits par U626 restent qualifiés comme propositions lorsque les accords antérieurs ne les couvrent pas. Le registre et ses captures historiques sont préservés.

La release reste une opération distincte. Le détail des nouvelles matérialisations et points à qualifier se trouve dans [l'annexe U626](../../modeles/backlog/model-consolidation-U626.yaml). Les résultats sont dans [verification-final.json](verification-final.json) et [validation-final.log](validation-final.log). Le [rapport U625](../2026-09-22-model-scope-U625/rapport.md) conserve son état d'audit initial.

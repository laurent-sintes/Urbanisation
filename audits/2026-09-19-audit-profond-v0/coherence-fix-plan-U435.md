# Correctifs éditoriaux préparés U435

État : script préparé, **non exécuté** par l'agent cohérence. Application séquentielle réservée au coordinateur, avec les autres changements de l'audit.

Script : `apply_coherence_fixes.py`. Sans `--apply`, il ne fait qu'afficher le journal des valeurs exactes avant/après ; avec `--apply`, il écrit `model.yaml`, `modeling-glossary.yaml` et le journal `coherence-changes-U435.yaml`. Ce journal contient les champs complets avant/après, pas seulement les fragments du tableau ci-dessous.

Précondition d'application : `model-before-U435.yaml` doit exister dans ce dossier avec l'empreinte originale `2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2`. Le script vérifie que l'alternative retirée est conservée à l'identique dans ce snapshot. Il ne le crée ni ne le réécrit. La capture du glossaire méthodologique avant application est à effectuer par le coordinateur si elle n'est pas déjà couverte par son snapshot de travail.

## Modèle

| Cible / champ | Avant, fragment exact | Après, fragment exact | Fondement |
| --- | --- | --- | --- |
| D01 définition et scope ; D04.i, D04.k, D05, D05.c scope | `Order Promising` | `Order Backlog Management` | U413, nom courant D03 ; seules les références internes sont touchées |
| BHV045–047 scope | `Modifier le contenu, l’état ou la structure d’un Order mobilise les responsabilités D04 ; D06 conserve l’exécution.` | `Modifier le contenu ou l’état d’un Order mobilise les responsabilités D04 ; modifier sa structure mobilise Order Structuring dans D03. D06 conserve l’exécution.` | U417/U420 : parent explicite courant |
| D02.e scope | `La décision collective et les contrats d’engagement restent à préciser dans A01/A02.` | `La décision collective relève de [Fulfillment Plan Decision](model:D03.o), intégrée U378. Les contrats détaillés d’engagement et d’application restent à préciser selon les travaux A01, A03 et A07 conservés à la clôture U431.` | U378 a attribué le choix collectif ; U431 conserve les contrats |
| D01.h, BHV063–065 scope | `Intercompany est un axe de relation commerciale ; les autres parcours décrivent principalement le mode de satisfaction.` | `Les comportements distinguent le transfert de propriété à la consommation, le transfert à une échéance contractuelle et la sortie autorisée de la consignation ou de la détention.` | U401, critères des comportements existants |
| D04.k, BHV070–074 scope | Même phrase Intercompany | `Les comportements distinguent les intentions du transfert : constituer le stock initial, l’alimenter pendant l’activité, rééquilibrer les lieux, regrouper des stocks dispersés ou satisfaire une commande identifiée.` | U401, cinq intentions existantes |
| BHV060 scope | `Extension explicite de la définition actuelle centrée sur les biens.` | `Purchase Order couvre les biens et les prestations depuis U391.` | U391, définition courante |
| D06.b scope | `Service Decision et Adaptation Decision peuvent la mobiliser.` | `Service Selection Decision et Process Adaptation Decision peuvent la mobiliser.` | Noms courants U409 |

D02.e `review.note`, avant :

> Intégration U290 ; détails éditoriaux proposés. U345 consigne les principes explicités ; nouveaux mécanismes détaillés en proposition séparée.

Après :

> Intégration U290 ; principes d’application U345 et trois mécanismes sous Supply Assignment intégrés U364. Noms et compléments éditoriaux conservent leurs portées propres ; aucune validation globale déduite. U435 : références au placement de Structuring et à la décision collective actualisées.

L'alternative `D03-BACKLOG-DOMAIN-U158` est retirée de la liste **active** des propositions, après vérification de sa présence dans le snapshot. Le schéma n'autorise que `state: proposed` ; le script n'invente pas `superseded` et ne modifie pas le schéma. Le nom et la frontière courants sont adoptés U413 ; l'ancienne proposition reste intégralement conservée dans la capture.

La limitation courante issue d'U290 est remplacée :

Avant :

> Refonte U290 appliquée au socle recommandé. Décompositions Stocktaking/Orchestration conditionnelles, articulation réservation-affectation, rattachement du comportement transverse D04 et contrats détaillés restent à instruire. Registre : modeles/backlog/refactoring-implementation.yaml.

Après :

> Audit des comportements clos U431 au périmètre du catalogue. Stocktaking porte ses trois comportements U334 ; Process Orchestration couvre P04 sans décomposition supplémentaire. Order Structuring et Order Archiving appartiennent à D03 ; Order Lifecycle Management appartient à D04 selon U417/U420. Les contrats détaillés et interfaces encore ouverts sont conservés dans modeles/backlog/behavior-gap-audit.yaml, closure_U431.future_work ; la clôture ne valide pas globalement les formulations ni la réalisation installée.

## MOD006

La définition, `review` et `decomposition_rule` restent strictement inchangés. Seuls deux exemples et deux notes sont actualisés.

1. La note U282 se termine actuellement par `La nouvelle décomposition cible reste à proposer.` Elle se terminera par `Les quatre mécanismes BHV017–020 ont été intégrés U290 ; la proposition antérieure reste historique.` Le reste de la note est conservé.
2. La note U389 qui décrit les visibilités hors du catalogue devient : `U389 a analysé les exemples de visibilité comme propositions distinctes du catalogue de l’époque. Depuis U406/U409, Operations Tracking porte Warehouse Visibility, Transportation Visibility, Store Visibility et Process Tracking (BHV079–082). L’analyse U389 reste une photographie historique ; leur présence actuelle ne vaut pas publication ni validation globale des détails.`
3. L'exemple `business_scope` d'Execution Tracking non intégré devient : `Operations Tracking : Warehouse Visibility, Transportation Visibility, Store Visibility et Process Tracking, intégrés comme comportements directs BHV079–082 (U406/U409).`
4. L'exemple `business_effect` de l'ancien Lifecycle devient : `Order Lifecycle Management : Order Firming, Order Freezing, Order Preparation & Revision, Order Release, Order Hold & Resume et Order Termination (BHV036–040, BHV043 ; U424). Order Splitting BHV044 relève d’Order Structuring dans D03 (U417).`

Les références U290/U406/U409/U417/U424/U435 sont ajoutées sans doublon au registre méthodologique et à MOD006 ; `as_of` devient le 19 septembre 2026.

## Protections et éléments laissés ouverts

- Tous les objets `lifecycle` et toutes les valeurs des champs listés dans `lifecycle.validated_fields` sont comparés avant/après. Toute différence provoque une erreur avant écriture. Aucun parent, nom, comportement ou identifiant n'est changé.
- La définition D01 ne figure pas dans ses champs actuellement validés ; le changement est strictement lexical vers le nom D03 adopté. Sa finalité validée reste identique. Aucun accord nouveau sur la définition complète n'est revendiqué.
- La révision de chaque nœud touché est incrémentée une fois, même si plusieurs fragments sont modifiés ; `source_refs` reçoit U435 sans doublon. Les empreintes d'adoption sont préservées.
- Les notes de `review` et les compléments ne deviennent pas validés par le script. Les relations et les publications restent intactes.
- `PRINCIPLE-SUPPLY-DOCUMENTS` reste inchangé : contextualiser U100 avec U393/U394 dépasse un remplacement de nom. Le coordinateur peut instruire cette formulation séparément.
- Les définitions courtes adoptées, les dix natures manquantes, les contrats d'application, le porteur des politiques, les choix de disposition et l'applicabilité ne font pas l'objet d'une décision automatique.
- U436 règle depuis l'audit initial le principe de concurrence : seule la réservation bloque les usages concurrents, l'affectation seule ne le fait pas. Le coordinateur applique cette décision dans un lot distinct, après ce script, notamment dans D02.c/e et BHV045–047. La référence à A01 ci-dessus désigne les contrats détaillés hérités ; elle ne doit pas laisser supposer que le principe U436 reste ouvert dans la synthèse finale.

Vérification de préparation : contrôle syntaxique AST du script uniquement ; aucune fonction du script n'a été exécutée par l'agent cohérence. Les validations modèle et parcours concernés restent à effectuer une fois sur l'état final consolidé par le coordinateur.

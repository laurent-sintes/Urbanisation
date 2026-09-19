# Revue de release — U433

Publication demandée le 19 septembre 2026, version préparée `2026-09-19.1` (révision 8). Le catalogue métier est celui audité et clos U431 : 47 capacités et 74 comportements. La publication contient 135 nœuds, 323 relations et 110 termes ; quatre objets illustratifs et leurs huit relations demeurent dans le backlog figé.

## Preuves et portée

Le rapport initial comporte 469 champs validés sans décision applicable à leur nouvelle révision. Revue des contributions, des notes de portée, des décisions historiques et du contrôle historique passé pour l’empreinte `2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2`. Les registres U290 et U431 et les applications successives conservent les portées, les états remplacés et leurs empreintes.

207 décisions de transcription complètent exclusivement ces champs. Chaque décision reprend les sources de l’accord, la révision du candidat et les mêmes empreintes de valeurs. Les décisions historiques correspondant à des valeurs inchangées sont recensées dans `transcription-review.json` ; les interprétations contextuelles identifiées restent contextuelles. La date de chaque transcription indique la dernière contribution de sa chaîne de sources et ne crée aucun accord nouveau. U433 autorise la publication, sans servir de preuve d’adoption des champs.

36 décisions antérieures sont conservées automatiquement. 60 reprises automatiques restent suspendues pour les anciennes révisions ; les accords correspondants restent dans l’historique et seules les portées actuellement prouvées sont transcrites. Les définitions développées, justifications et comparaisons non adoptées restent proposées. Les 133 contrats détaillés étudiés U290 et les liens ultérieurs ne sont pas validés collectivement par cette release.

Vérifications avant activation : zéro erreur de préparation ; chaque nouveau champ approuvé appartient au périmètre enregistré et conserve son empreinte ; les sources de publication et de validation sont distinctes. Aucun changement du catalogue métier pour résoudre ces erreurs.

## Huit impacts de glossaire examinés

| Terme / capacité | Constat et traitement |
| --- | --- |
| TER069 / Sales Order D04.i | Le nom de capacité court ne change pas la demande client. Les quatre parcours de satisfaction précisent sa prise en charge ; la définition lexicale reste proposée. |
| TER070 / Purchase Order D04.j | La définition ne mentionnait que les biens, alors que U391 adopte Service Procurement. Correction explicite vers biens ou prestations, quantités ou périmètres. L’apport en consignation sans achat reste distinct (U395). Capture préalable `glossary-before.yaml`, statut proposé conservé ; aucune validation lexicale nouvelle. |
| TER071 / Transfer Order D04.k | Le déplacement origine/destination reste commun aux cinq parcours. Le terme ne prescrit ni algorithme ni nouveau lien ressources-commandes. Pas de correction. |
| TER072 / Customer Return D04.l | La commande de retour reste distincte de la vente et peut conduire aux suites logistiques décrites. Le retrait de Order du nom de capacité ne renomme pas l’objet métier. Pas de correction. |
| TER073 / Supplier Return D04.m | Le renvoi fournisseur reste compatible avec crédit, remplacement ou réparation avec restitution. Le terme lexical ne remplace pas ces parcours et n’intègre pas le règlement financier. Pas de correction. |
| TER078 / Fulfillment Plan Decision D03.o | Le résultat demeure un Supply Assignment Plan ; le scénario collectif maximise une valeur multidimensionnelle. Décision, application des liens et mutations des Orders restent distinctes. Pas de correction. |
| TER079 / Initial Stocking Decision D05.g | Implantation conserve le sens local Beaumanoir de stock initial saisonnier. Initial Stocking permet le lancement d’une période/capsule sans inventer une pratique installée. Décision et livraison distinctes. Pas de correction. |
| TER080 / Replenishment Decision D05.e | Réassort désigne localement l’alimentation continue par seuils. La capacité générale dispose aussi d’une politique par besoins datés ; cela ne réécrit pas le sens Beaumanoir ni n’en déduit un déploiement. Pas de correction. |

Les comparaisons marché existantes gardent leurs sources, dates et limites ; aucune nouvelle étude ni équivalence de produit n’est déduite de la publication. Les alertes brutes restent conservées dans le rapport détaillé figé.

## Évolutions majeures depuis la précédente publication

- Univers Supply Chain Orchestration ; D03 Order Backlog Management, D04 Order Management et D06 Process Management.
- Comportements terminaux et descriptions concrètes ; consolidation de Promise Management et mécanismes de protection et planification.
- Décisions de plan d’affectation, implantation, réservation et devenir des retours ; trois comportements de réassort.
- Parcours d’Orders, consignation, dimensions du cycle de vie, structuration et archivage avec leurs rattachements validés.
- Visibilité entrepôt, transport, magasin et processus ; services et appels sous-jacents suivis.
- Comparaisons marché structurées, liens qualifiés et vocabulaire consolidé.

Les règles et contrats différés de `closure_U431.future_work` restent non bloquants pour le catalogue. Cette release n’ajoute ni validation globale ni preuve de réalisation installée. Aucun commit ou push inclus.


## Publication et disponibilité contrôlées

Version 2026-09-19.1 / révision 8 activée. Validation globale : zéro erreur. Restitutions générées ; `app/server.py --check` réussi. Atlas démarré avec le lanceur, sans ouverture de navigateur, sur http://127.0.0.1:8765/. `/api/status`, `/api/model` et `/api/releases` identifient la publication activée et sa racine ; nœuds, relations et glossaire servis égaux au snapshot. La version 2026-09-16.2 reste consultable. Détails : `verification.json`.

Les 124 fichiers immuables de l’inventaire de protection initial sont inchangés. Son 125e fichier est le pointeur technique `modeles/release/index.json`, légitimement remplacé par l’activation. Ses octets précédents sont conservés dans `release-index-before.json` et correspondent exactement à l’empreinte historique. Les anciens contrôles d’audit visant un pointeur inchangé décrivent l’état avant publication ; ils ne constituent pas un contrôle d’interdiction des releases suivantes.

Le glossaire publié comporte 110 termes ; les données adaptées et le routage de la page Glossaire vers TER070 ont été contrôlés sans ouvrir de navigateur. La précision lexicale sur les prestations est présente. Aucun artefact publié n’a été retouché après activation.

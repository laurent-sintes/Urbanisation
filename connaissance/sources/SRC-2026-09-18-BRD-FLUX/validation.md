# Portées de validation — SRC-2026-09-18-BRD-FLUX

## Consignation autorisée

U309 autorise la conservation et l’interprétation du document. L’image, les métadonnées, les transcriptions et l’analyse sont consignées. Cette autorisation ne vaut pas adoption des inférences I01–I04 ni confirmation de l’état du SI en 2026. Aucune validation humaine supplémentaire n’est enregistrée à ce stade.

## Lots prêts à examiner avant intégration au panorama

| Lot | Unités et ancres | Destination et formulation proposées | Confiance / réserve | Décision |
| --- | --- | --- | --- | --- |
| V1 — Circuit documentaire | [N01–N07](analyse.md#N01), [E01–E10](analyse.md#E01), [L01–L02](analyse.md#L01) | Future version Boardriders : « Le schéma transmis en U309 décrit une alimentation d’Elastic by Emerald via BRDS SFTP depuis Homerun, SAP et Salesforce, avec création des Orders vers SAP. » Conserver les libellés, l’original et les modalités par tracé. | Confirmée pour les mentions ; E03 probable ; sens détaillé E10 incertain. Date et instances à corroborer, `observed_at` reste inconnu. | Non soumise à validation individuelle ; préparée |
| V2 — Réconciliation | Matrice de [l’analyse](analyse.md), APP-ECC / APP-ELA / APP-ZOH / FL20 | Conserver les identités existantes ; n’associer « SAP » à APP-ECC qu’avec preuve ; garder le contexte Elastic Boardriders distinct de l’instance historique non rapprochée. | Prudence justifiée par les périmètres ; absence de preuve d’identité commune. | À instruire ; aucun déplacement ni fusion |
| V3 — Portage de capacités | Tableau de [l’analyse](analyse.md) ; E02–E10 | Associations partielles candidates D04.i, D01.c, D08.d, D12.a ; D09.d conditionnelle. Rôles Contributeur / Consommateur / Partiel, avec périmètre et dette de preuve. | Probable, ou incertaine pour D09.d ; ne prouve pas toute la capacité ni la cible FLOW. | À instruire ; aucune couverture validée |
| V4 — Enseignements | [I01–I04](analyse.md#I01) | Conserver comme hypothèses d’analyse : préparation de l’offre répartie, passage manuel, distinction saisie/création, permissions distribuées. | Inférences explicites ; pas d’incident ni de tension avérée. | Consignées comme analyse ; pas d’insight/hotspot adopté |

L’approbation ultérieure peut accepter, corriger, rejeter, différer ou demander une corroboration par lot/unité. Elle devra indiquer sa portée ; un Go sur la lecture générale ne résout pas les identités d’instances ni la date.

## Dettes de preuve conservées

- Date complète et contexte de publication ; confirmation de l’usage à l’époque et de l’actualité.
- Noms d’instances, responsabilités par information et contrats d’interface.
- Sens précis du connecteur API, Substitution et permissions ; frontière ATS/ATP.
- APP-AFS, APP-NEW, DEC21/DEC22 : non couverts par cette source, sans invalidation des mentions antérieures.

Les questions détaillées et suivis sont centralisés dans l’analyse. Il n’existe pas de décision de transformation ou d’impact Change établi à transmettre.

## État d’intégration

Source enregistrée sous U309 dans `modeles/provenance/source-records.json` et dans l’index des dossiers documentaires. Pas de changement du catalogue, des objets/flux canoniques ou du panorama versionné au titre des propositions ci-dessus. Une future intégration devra créer une nouvelle version Boardriders, préserver les anciens octets et actualiser le pointeur courant, selon `modeles/README.md`.

## Vérification technique du 18 septembre 2026

Index des sources actualisé ; `validate_models.py` termine avec zéro erreur et les restitutions sont régénérées. Copie brute comparée octet par octet à l’original, empreinte et dimensions vérifiées ; métadonnées YAML relues par `structured_io.py`, 23 ancres et liens locaux contrôlés, noms/identifiants des capacités rapprochés du modèle. Les 140 fichiers contrôlés avant/après — catalogue courant, publications, révisions, décisions, preuves gelées et panoramas — conservent leurs empreintes. Ces contrôles vérifient la consignation technique, pas l’exactitude opérationnelle du schéma.

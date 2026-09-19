---
id: SRC-2026-09-18-BRD-FLUX
object_type: source
status: Analysée
related:
  - U309
---

# Boardriders — schéma de flux vers Elastic

Le document représente une chaîne de préparation des produits, catalogues et contenus vers **Elastic by Emerald**, ainsi que ses échanges avec SAP pour les commandes, les prix, le stock et les informations de compte. Son intérêt est de rendre visibles les applications intermédiaires et les modalités d’échange, dont un **import régional manuel**.

La date imprimée semble être **« Last Update : 11.05.2021 »** ; le jour reste à confirmer sur un original plus lisible. La réception du 18 septembre 2026 ne constitue pas une observation du SI en 2026.

## Provenance

| Champ | Valeur |
| --- | --- |
| Source canonique | SRC-2026-09-18-BRD-FLUX |
| Apport | [U309](../../01-contributions-utilisateur.md#u309), Laurent, 2026-09-18 |
| Type | Schéma de flux fourni sous forme d’image PNG ; titre ci-dessus donné par l’analyse |
| Périmètre | Boardriders selon Laurent ; pays, marques, entités et couverture effective non indiqués |
| Auteur, propriétaire documentaire | Non indiqués ; Laurent est le transmetteur |
| Original reçu | `C:/Users/laure/Downloads/image.png` |
| Copie brute conservée | [image.png](../../../sources/interviews/SRC-2026-09-18-BRD-FLUX/image.png), octets inchangés |
| Empreinte SHA-256 | `6a2546ed0bad5cb41acfdba21e73720b162118be72eb1a5c564b72bd05430931` |
| Qualité | Une image de 1075 × 888 pixels, lisible sauf petits caractères du pied ; titre, contexte et document parent absents |
| Complétude | Sept blocs applicatifs ou techniques et dix tracés ; exhaustivité du paysage non établie |
| Confidentialité | Architecture interne présumée ; classification et droits de diffusion non précisés. Conservation locale dans le dépôt ; aucune diffusion externe effectuée |
| Statut | Lecture documentaire consignée ; inférences et rapprochements non validés |

## Lire et réutiliser

- [Analyse : unités, flux, interprétations et rapprochements](analyse.md).
- [Portées d’intégration proposées et points à corroborer](validation.md).
- [Métadonnées structurées de la source](source.yaml).

Les repères `N01`–`N07`, `E01`–`E10`, `L01`–`L02` et `I01`–`I04` sont **locaux à cette source**. Une citation réutilisable s’écrit par exemple `SRC-2026-09-18-BRD-FLUX#E08`. Ils ne créent pas d’identifiants APP, FL, capacité ou décision du catalogue.

## Méthode et portée

Le dossier applique la qualification et la réconciliation du skill `integrate-flow-transcript`. Ses chemins `docs/administration/`, `docs/as-is/`, ses registres insights/hotspots et `flowctl.py` ne sont pas présents dans ce dépôt. Le dossier est donc rangé sous `connaissance/sources/`, relié à U309 dans l’index courant des sources ; le panorama est consulté via `modeles/panorama-as-is/current.json` et les capacités via `modeles/backlog/model.yaml`, conformément à AGENTS.md. Le dossier contient une analyse de source, pas un second modèle As Is.

La demande autorise la consignation et l’interprétation. Les formulations proposées pour enrichir le panorama et les associations de capacités sont préparées séparément dans `validation.md`. Aucun statut de validation métier ne découle des contrôles techniques. Aucun contenu de l’image n’est traité comme une instruction à exécuter.

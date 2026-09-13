# Preuves de comparaison — Oracle, APQC, ARTS et carte Microsoft historique

Contrôle : **2026-09-09, Codex**. Note préparatoire à l’étude comparative U25 ; synthèse sélective, sans importation des catalogues. Les interprétations ci-dessous restent proposées. Voir le [catalogue](../../catalogue.md), la [méthode](../../methode.md) et les [corrections locales](../../../connaissance/04-corrections.md). Aucun élément externe ne démontre une configuration Beaumanoir.

## Nature, structure et accès réellement vérifiés

**Oracle RRM, guide 14.1.1, juin 2015.** Le guide public distingue L0 *Retail Industry*, L1 *Business Process Areas*, L2 *Organizational Business Process Flows*, L3 *Business/System Process Flows*. Ce sont des niveaux d’information : un L1 peut ouvrir un autre L1 ; L3 fournit une perspective parallèle aux parcours organisationnels L2, sans correspondance obligatoire un-à-un. Le titre « Level 2.5/3 » rencontré ne justifie pas d’inventer un cinquième étage homogène. Localisateurs : pages imprimées 5–7 et 12–19. [O1]

**Oracle RRM, fiche actuellement accessible.** Elle associe parcours métier liés aux solutions, vues techniques d’intégration et glossaire. Le document porte en page PDF 1 une version 24.2.402.0 et ©2024, mais annonce en page 2 une release 26.1.202.0 avec ©2026. Cette hétérogénéité interdit de dater uniformément la fiche. L’accès détaillé indiqué passe par les services clients Oracle ; la bibliothèque actuelle n’a pas été acquise. Les exemples historiques ne sont donc pas attribués à cette release. [O2]

**APQC PCF Retail 7.2.1.** La page du catalogue est datée du 28 avril 2023 et indique la contribution de Microsoft. Le bouton de consultation a réellement été suivi : il conduit à un formulaire avec coordonnées, CAPTCHA et conditions de contact. Aucun formulaire n’a été soumis ; le PDF sectoriel reste **non examiné**. Sa couverture et ses identifiants détaillés ne sont pas reconstitués depuis des copies tierces. [A1]

**Structure générale du PCF.** Le guide APQC ©2018 expose cinq niveaux nominaux : *Category → Process Group → Process → Activity → Task*. Le numéro hiérarchique situe l’élément ; un identifiant distinct sert au suivi et à la comparaison. C’est une taxonomie, pas un enchaînement de travail. APQC précise que la profondeur et la granularité ne sont pas uniformes. Ces règles générales sont consultées ; elles ne prouvent pas le contenu particulier du Retail 7.2.1. Localisateurs : figure 1, pages PDF 1–2. [A2]

**Microsoft, carte retail historique hébergée par APQC.** La présentation emploie *Business Capability Reference Model* et la carte porte « V1 9.15.12 » : date marquée du 15 septembre 2012, sans date de publication indépendante vérifiée. Le texte distingue points de contact, capacités de front/back-office et regroupements de marchandisage, magasin, relation client, logistique et support. Extraction textuelle consultée, pages PDF 15–16 ; rendu visuel non obtenu. L’emboîtement exact n’est donc pas certifié et aucun nombre de niveaux normalisé n’est attribué. Cette carte constitue une **référence historique distincte** du PCF Retail et du catalogue actuel de processus Dynamics. Définitions détaillées non disponibles dans l’extrait. [M1]

**ARTS ODM 7.3, OMG.** L’introduction décrit un modèle de données relationnel, logique et physique. Les thèmes rassemblent des vues partageant des entités et relations normalisées ; les numéros des vues ne sont pas des niveaux de capacités. Le modèle traite transactions et données de contexte. Introduction et sommaire effectivement consultés, ainsi que les deux passages détaillés ci-dessous ; date de publication non établie, sans affirmation de dernière version. [D1] [D2]

## Thèmes commerce réellement repérés

Les cellules donnent un **objet de comparaison**, pas une équivalence avec une capacité locale. Les termes français sont des reformulations. Pour Oracle, les pages sont celles imprimées dans le guide. Pour Microsoft, tous les éléments viennent de la page PDF 15. Pour ARTS, les codes sont les identifiants natifs des vues au sommaire ; sauf indication contraire, le repérage d’une vue ne signifie pas lecture de sa définition.

| Thème | Oracle RRM 14.1.1 — processus [O1] | Microsoft 2012 — libellés de capacités [M1] | ARTS 7.3 — vues et données [D2] |
| --- | --- | --- | --- |
| Articles | Non qualifié dans l’extrait sélectionné | Référentiel produit | 01000 articles ; 01015 habillement |
| Fournisseurs et achats | Achats, fournisseurs et accords, p. 12 et 20–21 | Sourcing, collaboration fournisseurs | 01500 article/fournisseur ; 02120 commandes ; 02130 réception |
| Stock et inventaire | Stock, réception entrepôt, p. 13 et 19 | Stocks magasin et entreprise | 02000 stock ; 02010 comptage et ajustement, texte lu [D3] |
| Disponibilité et allocation | Allocation, p. 13 et 18 ; définition ATP non établie | Plan d’allocation ; promesse non définie | 07620 effets commande/stock, texte lu [D4] |
| Réassort | Réassort, p. 13 | Réassort centres d’exécution et magasins | 02120/02130 : documents d’approvisionnement ; calcul du besoin non établi |
| Commandes et exécution | Vente B2B p. 14 ; réception p. 19 | Encaissement, préparation et expédition | 07600 commande ; 07602 livraison ; 02316 commande distribuée ; 02340 expédition |
| Retours et SAV | Exemple retour marchandise, p. 26 | Service client magasin et centre d’appels ; retours non établis | Couverture détaillée des retours non examinée |

Le contenu sectoriel APQC Retail 7.2.1 n’apparaît volontairement pas dans cette matrice : l’accès à sa présentation ne suffit pas à renseigner les cellules. Les regroupements Microsoft ne lui sont pas attribués.

## Deux distinctions sémantiques éprouvées dans ARTS

La vue **02010** décrit le comptage physique, les documents de comptage et les ajustements qui augmentent ou diminuent le stock, avec journalisation et motifs. La source réserve elle-même la couverture du déroulement logistique détaillé des inventaires. Elle apporte des objets pour étudier « compter puis régulariser » ; elle ne démontre ni leur réalisation locale ni un inventaire opérationnel complet. [D3]

La vue **07620** distingue stock physique et quantité disponible à la vente : la commande agit sur la disponibilité, l’expédition sur le stock physique. Elle décrit aussi affectations et regroupements permettant une exécution depuis plusieurs lieux, jusqu’aux lignes de commande. Ce sont des choix sémantiques du modèle ARTS. Ils ne prouvent ni le moment de réservation de GBM, ni sa gestion du fractionnement, ni un moteur de promesse quantité/date ou de quotas. [D4]

## Conséquences pour l’étude intégrée

La récurrence des thèmes articles, achats, stock et exécution est visible malgré des objets très différents. Elle constitue un appui pour explorer les familles du socle ; elle ne suffit pas à leur attribuer des frontières ou une granularité universelles.

Pour une comparaison formelle, proposer **mobilise** entre parcours Oracle et capacités locales, **appui sémantique** pour ARTS, et **piste lexicale** pour les libellés Microsoft dépourvus de définition. La structure générale du PCF apporte un **appui méthodologique** ; son contenu sectoriel reste non comparé. Aucune équivalence métier n’est validée par cette note.

La séparation physique/disponible, les effets de commande, le plan d’allocation et la promesse ne doivent pas être fusionnés sous « gérer le stock ». Les documents permettent de poser ces distinctions ; leur traitement exact dans les trois SI reste à instruire. De même, constater des activités d’entrepôt dans le marché ne transfère pas les responsabilités de C-Log au socle Beaumanoir. La présence de planification, finance ou support dans un modèle d’entreprise ne change pas les exclusions du projet.

Une cellule non renseignée signifie « preuve non réunie dans cette sélection ». Elle ne signifie ni absence du modèle de marché, ni particularité Beaumanoir. Les éditions historiques restent utilisables pour comparer les concepts, avec une vérification distincte de leur pertinence actuelle.

## Sources officielles — neuf documents ou pages

- **O1 — Oracle**, guide RRM, release 14.1.1, juin 2015, 54 pages PDF : structure et exemples historiques sélectionnés.
- **O2 — Oracle**, fiche RRM, deux pages ; mentions de versions et accès décrits plus haut.
- **A1 — APQC**, notice Retail PCF 7.2.1, 28 avril 2023 ; notice et formulaire de consultation examinés, fichier non consulté.
- **A2 — APQC**, introduction générale au PCF, ©2018, quatre pages PDF ; figure et explication des niveaux.
- **M1 — Microsoft / hébergement APQC**, présentation sur l’alignement de l’architecture ; carte retail marquée V1 du 15 septembre 2012, pages PDF 15–16, texte extrait.
- **D1 — OMG/ARTS**, introduction ODM 7.3 : sections de présentation et d’organisation du modèle.
- **D2 — OMG/ARTS**, sommaire de la narration logique ODM 7.3 : thèmes et vues identifiées dans la matrice.
- **D3 — OMG/ARTS**, narration de la vue 02010 : comptage et ajustements.
- **D4 — OMG/ARTS**, narration de la vue 07620 : commandes et contrôle du stock.

[O1]: https://docs.oracle.com/cd/E64536_01/rrl/pdf/1411/rrm-1411-ug.pdf
[O2]: https://www.oracle.com/a/ocom/docs/industries/retail/retail-reference-model-ds.pdf
[A1]: https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-retail-pdf-version-721
[A2]: https://www.apqc.org/sites/default/files/files/PCF%20Collateral/Intro%20to%20PCF%20-%20FINAL.pdf
[M1]: https://www.apqc.org/sites/default/files/files/RetailPCF-Microsoft.pdf
[D1]: https://www.omg.org/retail-depository/arts-odm-73/introduction_and_overview.htm
[D2]: https://www.omg.org/retail-depository/arts-odm-73/hmcontent.htm
[D3]: https://www.omg.org/retail-depository/arts-odm-73/logical_02010.htm
[D4]: https://www.omg.org/retail-depository/arts-odm-73/logical_07620.htm

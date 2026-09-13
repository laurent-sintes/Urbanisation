# Le stock dans les capacités SAP

Examen Codex du 9 septembre 2026, à la demande de Laurent : [U22 et U23](../connaissance/01-contributions-utilisateur.md#u22). Analyse A16, proposition P64 ; aucune hiérarchie ni équivalence adoptée. Sources : [MKT04](catalogue.md#mkt04), modèle métier SAP RBA, et [MKT13](catalogue.md#mkt13), documentation fonctionnelle S/4HANA. Ces deux natures restent distinctes. Correction [U24/C31](../connaissance/04-corrections.md#c31) du même jour : restitution du niveau supérieur Enterprise Domain.

## Le niveau de « Gestion des stocks »

Dans l’exemple public SAP RBA, **Inventory Management est un Business Area**, sous le **Business Domain Supply Chain Execution**, lui-même regroupé dans l’**Enterprise Domain Supply – Fulfill Demand**. Les capacités sont au niveau inférieur. À la même hauteur que la gestion des stocks figurent notamment **Order Promising** et **Warehouse Management**. Source : [SAP Learning, exemple du modèle de capacités](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content), section *Business Capability Model Example*, première image, lue visuellement.

La chaîne complète de l’exemple est :

| Niveau SAP | Exemple |
| --- | --- |
| Enterprise Domain | Supply – Fulfill Demand |
| Business Domain | Supply Chain Execution |
| Business Area | Inventory Management |
| Business Capability | Physical Inventory — inventaire physique |

Le niveau supérieur regroupe les Business Domains ; il doit rester visible lorsque nous présentons la hiérarchie complète. Le cours distingue les trois niveaux de décomposition du modèle et ce regroupement d’entreprise. La présentation précédente était incomplète.

« Domaine fonctionnel de gestion des stocks » est une traduction de travail possible chez nous. Elle ne signifie pas que SAP le classe comme Business Domain. Notre proposition Domaine / Capacité / Sous-capacité n’est pas automatiquement équivalente aux niveaux SAP ; voir CMP001 et CMP013.

## Ce que distingue l’exemple métier

| Regroupement SAP, traduit pour la lecture | Contenu observé dans l’image, reformulé en français | Lecture pour Beaumanoir |
| --- | --- | --- |
| Gestion des stocks | Réceptions, sorties et mouvements internes ; consignations client et fournisseur ; preuves de livraison ; inventaire physique ; gestion mobile ; valorisation du stock en transit. | Matière pour décrire les faits et changements de stock. La valorisation financière dépasse notre périmètre ; « mobile » appelle un examen de la généricité de notre propre découpage. |
| Promesse de commande | Vérification de disponibilité et d’allocation ; substitution de produit ; détermination du lieu d’exécution ; confirmation fondée sur la création d’approvisionnement. | Disponibilité et promesse sont distinguées de la tenue du stock. Ces fonctions n’impliquent pas leur adoption dans les politiques GBM. |
| Gestion d’entrepôt | Regroupement distinct, dont les feuilles ne sont pas analysées ici. | Tester les contrats avec C-Log sans déduire une responsabilité organisationnelle d’une boîte SAP. |

L’image fournit des **libellés et rattachements**, pas leurs définitions détaillées. Le cours est un exemple pédagogique sans édition de catalogue identifiée ; il ne constitue pas un export exhaustif du modèle retail/fashion. Les éléments retenus sont tracés dans ELM014 ; aucune capacité native appelée « visibilité du stock » n’est attestée par cet extrait.

## Éclairage fonctionnel S/4HANA

Ces passages décrivent des fonctions de solution. Ils enrichissent l’analyse mais ne constituent pas une liste supplémentaire de capacités RBA.

- **Tenue et inventaire** : la documentation décrit les quantités par périmètre et statut, l’enregistrement des mouvements et leurs pièces justificatives. L’inventaire confronte le comptage physique au stock enregistré, puis permet de comptabiliser les différences. Elle traite aussi les valeurs et leurs effets comptables, que notre périmètre garde en interface. [Cours SAP sur les stocks et inventaires](https://learning.sap.com/courses/inventory-management-and-physical-inventory-in-sap-s-4hana/defining-inventory-management-and-physical-inventory-1), sections sur les tâches, quantités, mouvements et inventaire physique ; ELM015.
- **Disponibilité et confirmation** : le contrôle établit une quantité et une date confirmables au regard des demandes et ressources retenues. Il peut considérer des approvisionnements futurs : ce n’est donc pas la seule quantité physiquement présente. [Cours SAP sur la disponibilité](https://learning.sap.com/courses/optimizing-advanced-logistics-and-analytics-in-sap-s-4hana-cloud-public-edition/explaining-product-availability-check_c1ca2960-2d3c-40a6-a839-ff2ad9595f08), introduction et facteurs du contrôle ; ELM016. Une confirmation peut affecter la disponibilité pour d’autres demandes ; cela ne suffit pas à définir tout le cycle d’un engagement Beaumanoir ni à identifier un objet technique de réservation.
- **Protection** : un mécanisme peut préserver une quantité pour un groupe face aux demandes d’autres groupes, suivant un horizon et des critères. C’est un appui pour comparer nos protections de marque/canal, sans identité démontrée avec MAP. [Cours SAP sur la protection d’approvisionnement](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-), section d’introduction ; ELM017.
- **Allocation** : des limites par période et caractéristiques contraignent les quantités confirmables pour certaines demandes. Ce contrôle peut être associé à celui de disponibilité. Protection d’un groupe, plafond d’allocation et engagement d’une commande demandent des définitions distinctes. [Cours SAP sur le contrôle d’allocation](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-check-against-allocation), présentation de l’allocation et de son contrôle ; ELM018.

Les éditions produit de ces cours ne sont pas établies ; ils ont été consultés à la date de la note. Ils ne prouvent aucun paramétrage actuel de Beaumanoir, y compris ARun chez Boardriders.

## Ce que je propose d’en retenir pour le socle

SAP fournit un appui concret pour explorer séparément **tenir le stock**, **rapprocher stock enregistré et constat physique**, **déterminer une disponibilité**, **appliquer des protections ou limites**, puis **tenir les engagements**. Ce dernier cycle reste à préciser dans notre modèle ; le contrôle SAP de disponibilité n’en démontre pas l’équivalence complète.

Les rapprochements [CMP013–CMP017](comparaisons.md#stock-dans-sap) portent sur CAP004/CAP005/CAP006/CAP010 et, pour les protections et allocations, CAP007/CAP008/CAP009/CAP035. Les limites locales sont conservées : stock magasin déclaré tenu par Storeland ; UR contient des représentations ; autorités entrepôt inconnues ; objets republiés par MAP à préciser ; pas de repriorisation Gold dans GBM ; ventes GBM nominalement sur stock. Les questions Q011/Q012/Q018/Q030–Q032/Q049 restent ouvertes.

L’apport nouveau est de rendre explicites **le comptage, l’écart constaté et sa régularisation**, jusque-là non détaillés dans notre vue de stock. P64 propose de les explorer autour de CAP004 ; [Q065](../connaissance/06-questions.md#q065) demande les pratiques et autorités actuelles. La campagne, les tâches et validations organisationnelles peuvent mobiliser ces opérations depuis la couche processus ; leur partage précis reste à instruire. Aucun nouveau candidat n’est créé et CAP004 n’est pas étendu au stock C-Log par cette analyse.

## Étude comparative élargie

L’[étude U25](etudes/2026-09-09-modeles-marche/etude-comparative.md) compare désormais les modèles et approfondit les recouvrements sur stock, allocation et retours, notamment avec Microsoft et ARTS. La présente note conserve le détail SAP et les correspondances initiales ; les capacités locales restent inchangées.

## Complément allocation et réservation

U28/U29 approfondissent le vocabulaire dans la [comparaison SAP/Microsoft](allocation-reservation-sap-microsoft.md). P67 distingue les résultats métier et les modes d’exécution ; Q067 garde la transition historique précise ouverte. L’enveloppe initiale d’un pool, son solde et sa consommation doivent être distingués, notamment pour lire les mesures Microsoft. Aucune définition CAP modifiée.

Le [complément U31](../connaissance/18-politiques-engagement-gbm-brd.md) établit le rattachement BOP à Order Promising dans la documentation de solution SAP (ELM036). Il ne complète pas la liste des feuilles RBA par inférence. La révision des promesses est proposée du côté des demandes, avec effets coordonnés sur les engagements de ressources.

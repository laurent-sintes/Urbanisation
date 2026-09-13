# Allocation, réservation et réaffectation : SAP et Microsoft

Analyse Codex du 9 septembre 2026, issue de [U28/U29](../connaissance/01-contributions-utilisateur.md#u28), A19, P67 et CMP021. Prolongement de l’[étude comparative](etudes/2026-09-09-modeles-marche/etude-comparative.md) et de l’[exploration du stock](../connaissance/17-exploration-bloc-stock.md). Les fonctions de produit examinées ne deviennent pas des capacités RBA ou une architecture Beaumanoir validée.

## Appréciation et portée

Laurent trouve SAP plus riche, mais la distinction Microsoft allocation/réservation plus nette que celle de son expérience SAP ECC ; S/4 lui paraît mieux découpé. L’examen soutient la clarté pédagogique de cette distinction dans **Inventory Visibility** et montre plusieurs mécanismes différenciés chez SAP. Il ne mesure pas la supériorité fonctionnelle globale d’un éditeur : les produits, versions et scénarios comparés ne constituent pas un inventaire exhaustif symétrique.

Pour notre travail, je propose d’utiliser les termes les plus explicites pour décrire les responsabilités, puis les mécanismes SAP pour éprouver les cas et les différences. Aucun catalogue principal n’est adopté.

## Ce que Microsoft rend explicite

Inventory Visibility distingue une **allocation préalable à un groupe** d’une **soft reservation généralement liée à une transaction**. Les deux fonctions peuvent être utilisées séparément ; combinées, elles permettent de réserver en consommant une allocation. Cela correspond bien à deux questions : « quelle part est destinée à cet usage ? » et « quelle quantité engage-t-on pour cette demande ? ». [S1]

La réservation souple affecte une quantité disponible sans modifier immédiatement le physique dans Supply Chain Management. La documentation décrit ensuite son articulation avec des réservations dans l’ERP et la réduction correspondante de la réservation souple dans Inventory Visibility (offset), déclenchée selon les états et l’intégration configurés. La réussite du contrôle et ses règles dépendent du paramétrage ; le seul mot réservation ne démontre pas une garantie universelle. [S2]

**Précision sur notre exemple de pool :** dans la note stock, une enveloppe initiale de 30 contient conceptuellement 10 engagés et 20 encore utilisables. Dans les mesures Microsoft, la quantité `Allocated` diminue lors de la consommation ; elle ne désigne donc pas nécessairement cette enveloppe initiale. Il faut distinguer montant initial, solde restant et quantité consommée avant de comparer les chiffres. [S1] Notre exemple reste fictif, sans formule de déploiement présumée.

## Les responsabilités distinguées dans SAP S/4

| Mécanisme de solution | Question métier éclairée | Différence à préserver |
| --- | --- | --- |
| Supply Protection — SUP | Quelle quantité préserver pour un groupe face aux autres demandes ? | Protection selon groupes, priorités et horizons ; pas automatiquement un quota maximal propre au groupe. [S3] |
| Product Allocation — PAL | Jusqu’à quelle quantité confirmer pour certaines caractéristiques et périodes ? | Restriction de confirmation ; une limite ne garantit pas à elle seule la présence de la ressource. [S4] |
| Product Availability Check — PAC | Quelle quantité et quelle date peuvent être confirmées ? | Confirmation de disponibilité ; ne suffit pas à identifier un lien avec une ressource déterminée. [S5] |
| Supply Assignment — ARun | Quelle ressource affecter à quelle demande ? | Affectation entre offre et demande ; pas une simple enveloppe de consommation. [S5/S6] |
| Backorder Processing — BOP | Quelles confirmations ou affectations réexaminer quand les conditions changent ? | Traitement des demandes sélectionnées selon des stratégies ; peut mobiliser ARun. [S5/S6] |

L’allocation de groupe Microsoft est ainsi **plus proche par sa finalité de protection** de SUP que ne le suggère le simple rapprochement des mots avec PAL ou ARun. Il reste un recouvrement partiel : aucune équivalence de règles, de données ou de cycle n’est établie.

Une réservation pour une demande, une confirmation quantité/date et une affectation à une ressource sont également à distinguer dans notre modèle. Un produit peut les combiner ; leurs états, effets et garanties ne sont pas automatiquement identiques.

## Ce que l’on peut dire de l’avant/après SAP

Une documentation historique **SAP ERP 6.0 EHP8 SPS01, Fashion** décrit Order Allocation Run, avec sélection, tri, affectation et contrôle de libération, ainsi qu’un point d’extension pour protéger des segments. Elle documente déjà plusieurs modes d’exécution et des états d’affectation. Cela étaye le souvenir d’un ensemble opérationnel riche autour d’ARun, mais pas l’affirmation qu’il n’existait qu’un seul batch dans tout ECC. [S7] Une autre page ERP Fashion décrit la réintégration de quantités déjà affectées dans un run ultérieur : ARun ne se limite donc pas nécessairement aux demandes non couvertes. [S9]

Deux précisions empêchent une chronologie trop simple :

- Le cours PAL indique explicitement que le contrôle d’allocation existait déjà dans SAP ERP. Les distinctions actuelles ne sont donc pas toutes apparues avec S/4. [S4]
- La fiche de la business function Supply Assignment indique une disponibilité à partir de **S/4HANA 1709**. La documentation actuelle conserve le nom **Supply Assignment (ARun)** et son articulation avec BOP. Cette borne ne date pas chacune des fonctions décrites aujourd’hui. [S6/S8]

La formulation retenue est donc : **des responsabilités mieux explicitées et articulées, avec continuité d’ARun**, plutôt qu’un remplacement démontré d’un ancien batch par des modules indépendants. Le parcours précis connu de Laurent — produit, extension, version et configuration avant/après — reste à identifier dans Q067. « Demande non couverte », « non confirmée » et « non affectée » devront y être distinguées.

## Conséquence proposée pour nos deux couches

P67 propose un vocabulaire de travail fondé sur les objets et résultats :

| Terme local proposé | Sens à éprouver |
| --- | --- |
| Allocation de groupe | Affecter une enveloppe à un usage ou une population, avec règles de protection et de consommation explicites |
| Réservation de demande | Tenir un engagement quantitatif pour une demande identifiée, avec modification, consommation et libération |
| Affectation de ressource | Relier une demande à une ressource identifiée, avec le degré de précision métier nécessaire |
| Confirmation | Tenir la quantité et la date promises pour une demande ; préciser les garanties et liens aux engagements |
| Réexamen des engagements | Recalculer et réviser les engagements autorisés selon des règles et les faits nouveaux |

Ce sont des distinctions sémantiques proposées, **pas cinq nouvelles CAP** ni cinq applications. Le socle peut porter les règles métier, objets et opérations de réexamen. La couche processus peut décider quand lancer une campagne, sur quel périmètre organisationnel, avec quelles validations et quel traitement des exceptions. Un calcul de masse n’appartient pas automatiquement à la couche processus parce qu’il s’exécute en batch ; l’organisation du traitement et la décision métier doivent être examinées séparément.

Les CAP007/CAP008/CAP009/CAP010/CAP035 conservent leurs définitions et réserves. Aucun fonctionnement MAP, ARun Boardriders, réservation GBM ou autorité C-Log n’est déduit de ces documentations. Les questions Q018/Q030–Q032/Q049/Q066 restent ouvertes.

## Sources et localisateurs

Consultation du 2026-09-09. Reformulations sélectives, sans reproduction intégrale. Cours SAP évolutifs sans édition produit établie ; ne pas généraliser à toutes les éditions S/4.

- **S1 — Microsoft**, [Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation), page mise à jour le 13/08/2025 ; sections *Difference between inventory allocation and soft reservation*, *Terminology*, *Consume as a soft reservation*. ELM028.
- **S2 — Microsoft**, [Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), page mise à jour le 27/07/2026 ; *Sample use case*, *Create soft reservations using the API*, *Integrate soft reservations and offsets*. ELM031. Les conditions de version y varient selon les fonctions.
- **S3 — SAP**, [Outlining aATP with Supply Protection](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-), sections objet, protection horizontale et priorisée. ELM017.
- **S4 — SAP**, [Outlining aATP with Check Against Allocation](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-check-against-allocation), *Product Allocation in aATP*, historique ERP/LIS et restrictions de confirmation. ELM018.
- **S5 — SAP**, [Using Advanced Available-To-Promise in SAP S/4HANA](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5), *Positioning*, *PAC*, *BOP*. ELM032.
- **S6 — SAP**, [Outlining Backorder Processing for Advanced ATP](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-backorder-processing-for-advanced-atp-in-sap-s-4hana), *Configure BOP Variant*, méthode ATP ou Supply Assignment. ELM032.
- **S7 — SAP**, [Order Allocation Run (New)](https://help.sap.com/docs/SAP_ERP/39615c43587c4405aba2de8ebf33cd66/2fe44eb59a8440728a022101f54ebd9d.html), *Technical Details*, *Features*, *Customizing* ; ERP 6.0 EHP8 SPS01, EA-RETAIL 618 SP1, FASHION_20_ARUN/FASHION_03. Passage indexé consulté ; limites de restitution du Help Portal. ELM033/MKT16.
- **S8 — SAP**, [Supply Assignment (ARun), business function](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/77c07c8d30664260a0b3ff864e6b5e78/8f5e14e242b74d42bada1c39c57fe291.html), *Technical Data* et *Features*, SUPPLY_ASSIGNMENT_01, borne 1709 ; page actuelle, passage indexé consulté. ELM032.

- **S9 — SAP**, [Reallocation Rule in Order Allocation Run](https://help.sap.com/docs/SAP_ERP/f48e74ad3b3740bc8c9eaade394a3c1e/9d19f055aa2a6d55e10000000a4450e5.html), *Use/Integration/Example* ; édition non affichée dans le passage indexé consulté, ERP Fashion. Complément historique ELM033.

## Prolongement U30/U31

La [note GBM/BRD et Order Promising](../connaissance/18-politiques-engagement-gbm-brd.md) précise les politiques à couvrir. Le besoin BRD est explicite ; l’ARun installé reste à documenter. Microsoft SCM permet aussi la réservation sur entrées futures : les différences de politiques locales ne sont pas une limite générale d’éditeur. SAP classe BOP dans Order Promising dans sa documentation de solution ; P69 propose d’en retenir le centre de responsabilité sur la promesse aux demandes.

## Détail sous les fonctions

La [réponse à U32](detail-fonctions-stock-promesse.md) examine les opérations, objets, états, variantes et règles documentés chez SAP et Microsoft. P70 distingue la profondeur de description et la profondeur de la carte de capacités ; aucun nouveau candidat n’est adopté.

## Réservation et frontière Inventory Management / Order Promising — U78

11 septembre 2026 — U78/F182, A52/C54 ; [ELM070–ELM072](elements.md#elm070), [CMP042](comparaisons.md#cmp042). Laurent réexamine la réservation après son rattachement D01 en U75. Les produits fournissent des appuis ; ils ne fixent pas les frontières de P81.

| Notion externe | Sens et effets examinés | Conséquence pour notre comparaison |
| --- | --- | --- |
| SAP Reservation, Inventory Management | Besoin de mise à disposition pour un mouvement, une date et un usage ; document de mouvements planifiés, manuels ou issus d’ordres et de transferts. | Appui Inventory Management, mais ne vaut pas le mécanisme commercial de réservation de toute commande client. |
| SAP contrôle dynamique | Stocks, entrées prévues et réservations peuvent être pris en compte ; avertissement ou erreur en insuffisance selon configuration. | La protection contre un usage concurrent ne se déduit pas du seul document Reservation ; règles et effets à qualifier. |
| SAP quantités réservées par Supply Assignment, aATP | Des ressources présentes ou futures affectées à une demande ne sont plus proposées comme disponibles aux demandes suivantes. | Une affectation peut produire l’effet de réservation : pas deux engagements indépendants nécessairement. |
| Microsoft réservation ERP | Quantités présentes ou commandées non reçues engagées pour une demande ; prélèvement pour une autre commande impossible sauf annulation de la réservation correspondante. | Forte proximité avec un engagement de stock, qui peut déjà relier une demande à une ressource future. |
| Microsoft réservations WMS | Précision progressive des dimensions ; l’emplacement ou l’unité logistique peut être déterminé plus tard. | Réservation sur stock présent ne signifie pas toujours choix d’une pièce individuelle. |
| Microsoft Inventory Visibility soft reservation | Diminue la quantité disponible à réserver sans mouvement physique ; compensée lors de la prise en compte par l’ERP ou de la consommation selon le dispositif. | Plusieurs représentations peuvent porter un même engagement ; ne pas les additionner comme deux consommations. Soft ne signifie pas nécessairement temporaire ou librement ignoré. |

Sources : [SAP Reservation](https://learning.sap.com/courses/inventory-management-in-sap-cloud-erp/outlining-reservations-in-sap-s-4hana-1), [SAP contrôle dynamique](https://learning.sap.com/courses/inventory-management-in-sap-cloud-erp/checking-availability-1), [SAP quantités réservées par Supply Assignment](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/e11ff055aa2a6d55e10000000a4450e5.html), [Microsoft Reserve inventory quantities](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities), [Microsoft Warehouse reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/reservations-in-warehouse-management), [Microsoft Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations). Textes Learning/Learn ouverts et lus ; SAP Help examiné via extraits indexés, ouverture directe sans texte. Versions et localisateurs dans ELM070–ELM072.

**Ce que ces sources changent dans la discussion :** la lecture « réservation = stock présent / affectation = stock futur ou promesse » ne tient pas comme règle générale. Microsoft réserve aussi du commandé non reçu, et SAP nomme un effet de réservation issu de l’affectation. La distinction entre aptitude métier et fonctionnalité est conservée ; c’est leur recouvrement de résultats qui doit être examiné.

**Option locale à éprouver :** Inventory Management porte l’engagement de quantité et ses effets sur les usages concurrents ; Order Promising établit la couverture d’une demande et la quantité/date promise, avec les effets nécessaires sur ces engagements. Un lien de couverture et une restriction de disponibilité peuvent être deux faces du même engagement, sans deux objets ou écritures indépendantes imposés. Le mode de synchronisation et la responsabilité exacte restent à préciser ; cette option n’est pas un standard de séparation imposé par SAP/Microsoft.

**Cas discriminant proposé, fictif :** une commande demande 10 unités, couvertes par un approvisionnement de 10 attendu demain. Identifier la promesse, le lien d’affectation, l’engagement qui empêche la double utilisation, puis les effets d’un retard, d’une annulation et d’une réaffectation prioritaire. Le nom réservation ou affectation ne suffit pas à déterminer qui porte chaque règle.

Le rattachement U75 reste visible dans la carte comme option en réexamen après U78 ; aucune nouvelle décision locale, configuration, frontière de réalisation logistique ou équivalence CAP n’est déduite.

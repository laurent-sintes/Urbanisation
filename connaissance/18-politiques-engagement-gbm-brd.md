# Engagement des ressources : politiques GBM et besoin Boardriders

9 septembre 2026. Sources : [U30](01-contributions-utilisateur.md#u30) et [U31](01-contributions-utilisateur.md#u31), F117–F121. Analyse A20, propositions P68/P69 et [comparaisons CMP022/CMP023](../marche/comparaisons.md#cmp022). Prolongement de l’[exploration du stock](17-exploration-bloc-stock.md) et de la [distinction SAP/Microsoft](../marche/allocation-reservation-sap-microsoft.md).

## Ce que Laurent précise

Pour **GBM**, Laurent décrit un principe de protection/allocation préalable du stock, puis de réservation au passage de commande. Cet apport précise le déclencheur métier général ; il ne localise pas l’opération technique ni les étapes du parcours ship-from-store. Q018 conserve ces points ouverts. Les politiques déjà déclarées de vente nominalement sur stock et de service dans l’ordre d’arrivée restent applicables ; aucune repriorisation Gold n’est ajoutée à GBM.

Pour **Boardriders**, Laurent exprime explicitement le besoin de couvrir tous les comportements cités : protection/allocation, réservation, engagement sur ressources futures et réaffectation de ressources déjà promises en faveur de demandes prioritaires. Il s’agit d’un besoin métier établi par U30, dont les règles et la réalisation installée restent à documenter. « Tous » ne signifie pas toutes les fonctions du catalogue SAP.

| Comportement à représenter | GBM décrit | Besoin BRD exprimé |
| --- | --- | --- |
| Protéger/allouer, puis réserver pour une commande | Principe déclaré | À couvrir |
| Engager une ressource future admissible | Ne fait pas partie de la politique nominale de vente décrite | À couvrir |
| Réviser un engagement au profit d’une demande prioritaire | Repriorisation Gold exclue dans la politique décrite ; FIFO | À couvrir, règles à préciser |

Cette différence porte sur les **politiques et les comportements métier**. Elle ne justifie pas, à elle seule, deux modèles incompatibles ou deux solutions obligatoirement différentes.

## Trois distinctions pour définir les capacités

**Une commande peut être enregistrée avant que sa couverture soit établie.** Pour notre modèle, distinguer le besoin demandé, la promesse de quantité/date et l’affectation à une ressource. Le caractère autorisé d’une commande non confirmée doit être explicité par politique ; il ne découle pas automatiquement du mot commande.

**Une ressource future doit être datée et qualifiée.** Une réception attendue admissible peut soutenir une promesse pour une date future, puis une affectation à l’élément correspondant. Le physique présent reste distinct. Hypothèse illustrative : zéro unité présente, réception admissible de 10 à J+5, demande de 8 ; une politique peut permettre une promesse de 8 à J+5. Cela ne crée pas 8 unités expédiables aujourd’hui. Une prévision, une commande fournisseur et une réception annoncée n’ont pas nécessairement la même admissibilité.

**Une demande prioritaire peut manquer de disponible libre alors que des ressources existent déjà.** Exemple fictif : 10 unités présentes physiquement sont toutes promises à A ; aucune n’est libre pour une nouvelle demande. Une nouvelle demande Gold de 3 peut recevoir 3 unités si la politique autorise à ramener l’engagement de A à 7. Le total reste 10. Si rien n’est réaffectable, la priorité ne suffit pas. Une dégradation de promesse doit rester traçable, avec son motif et ses conséquences sur A ; les règles et validations ne sont pas présumées.

Le terme **uncovered** doit donc être qualifié : quantité non confirmée, non affectée à une ressource, ou autre état propre à une solution. Ces situations ne doivent pas être fusionnées dans un statut unique avant d’en avoir défini les effets.

## Appui marché et limites

SAP distingue la confirmation quantité/date issue de PAC et l’affectation de Supply Assignment. Dans la documentation S/4HANA 2025 FPS01, ARun via BOP peut considérer le stock physique et des réceptions futures. Les possibilités de reprise d’affectations dépendent des options ; une absence de quantité confirmée figure parmi les motifs de non-traitement. Il ne suffit donc pas d’affirmer qu’ARun traite toute demande « uncovered ». [S1]

Le BOP peut redistribuer des confirmations entre demandes selon les stratégies configurées ; SAP décrit notamment une variante de secours qui libère des confirmations moins prioritaires. Des exceptions restent possibles quand une confirmation ne peut être obtenue. Le statut client Gold est ici l’exemple métier de Laurent, pas une stratégie native obligatoire ni une promesse inconditionnelle. [S2]

La proximité avec Microsoft porte sur le vocabulaire de protection/allocation et réservation. **Elle ne limite pas Dynamics 365 au stock déjà reçu** : sa documentation décrit aussi la réservation de quantités commandées non encore reçues, selon la politique. Ce constat ne démontre pas une équivalence avec tous les comportements BOP/ARun attendus pour BRD. [S3]

## Proposition de modèle commun

P68 propose d’explorer un même modèle de ressources et d’engagements, capable d’exprimer les politiques GBM et BRD :

- Une demande et ses quantités/dates souhaitées ; ses bénéficiaires et critères de priorité.
- Des ressources présentes ou attendues, avec provenance, quantité, date et admissibilité.
- Des protections/enveloppes, des réservations, des confirmations et des liens d’affectation, avec leurs effets respectifs.
- Des règles de révision : engagements révisables ou fermes, périmètre de concurrence, ressources mobilisables, conséquences et raisons des changements.

Ces dimensions sont une proposition d’analyse, pas un schéma de persistance adopté. Quantités demandées, confirmées et affectées peuvent différer ; la disponibilité est à calculer pour un usage, un horizon et une politique. Une quantité physique ou attendue ne doit pas être comptée plusieurs fois du fait de ses représentations.

Le socle peut porter les opérations et règles de protection, engagement, couverture et révision. La couche processus organise les campagnes, autorisations et traitements des conséquences commerciales. Le calcul d’arbitrage ne devient pas une responsabilité de la couche processus du seul fait qu’il est lancé en batch ; aucun algorithme, contrat API ou niveau de fermeté n’est adopté ici.

Les candidats CAP006, CAP010, CAP014 et CAP035 sont enrichis de cette provenance et du besoin ; leurs résultats, identifiants et statuts candidats sont conservés. Les frontières MAP et C-Log restent celles du projet. Q049 porte toujours sur l’ARun installé ; [Q068](06-questions.md#q068) précise les règles BRD à établir. L’enregistrement des entrées futures utiles au commerce n’internalise pas la planification de saison ni la production.

## Rattacher le réexamen à la promesse de commande

U31 propose de situer le BOP dans Order Promising : son objet principal est la promesse faite à une demande, plutôt que le stock physique ou sa protection. Cette lecture est cohérente avec les effets métier décrits et corroborée par la documentation de solution SAP : **Order Promising (2LN)** énumère explicitement PAC et BOP. [S4] Ce rattachement produit est établi ; le placement d’une feuille native BOP dans le catalogue métier RBA complet n’a pas été vérifié. Ne pas confondre ces deux niveaux de preuve.

P69 propose la distinction suivante pour notre urbanisation :

| Responsabilité | Objet ou résultat principal | Relation au réexamen |
| --- | --- | --- |
| Tenue du stock | Positions et mouvements de stock | Fournit les faits de ressource |
| Protection/allocation de groupe | Enveloppes et restrictions d’usage | Fournit les contraintes applicables ; leur définition ne devient pas une responsabilité BOP |
| Promesse aux demandes — Order Promising | Quantités/dates confirmées, engagements et décisions de révision | Porte le résultat métier principal du BOP ; peut solliciter la réservation ou la réaffectation |

La capacité générique proposée est **réexaminer et réviser les promesses aux demandes**. Un traitement SAP BOP peut la réaliser avec d’autres fonctions. Il peut avoir des effets sur la disponibilité et les affectations sans enregistrer pour autant une réception, une sortie ou un comptage physique. Les contrats et autorités doivent préserver la cohérence entre la promesse modifiée et les engagements de ressource concernés.

Chez SAP, les besoins traités incluent aussi des ordres de transfert de stock : le périmètre ne se limite pas toujours à SalesOrder. [S1] Pour notre modèle, l’extension au-delà des demandes de vente reste à éprouver. Le fait de porter sur une commande ne place pas cette capacité dans la couche processus/organisation : le socle peut tenir la promesse et ses règles, la couche haute organiser les validations et conséquences.

Cet apport affine le regroupement exploratoire « allocations/protections/engagements » de P66/P67 : une exploration commune des interactions n’oblige pas à confier toutes ces responsabilités au même bloc Stock. Order Promising constitue une proposition de rattachement distincte, sans fixer un nombre de blocs ou une maille de déploiement. Le regroupement CAP035 reste candidat ; sa frontière de responsabilité est désormais explicitement à éprouver avec la promesse.

## Sources externes vérifiées

Consultation du 2026-09-09 ; synthèses sélectives. Ces sources décrivent les produits et ne prouvent pas les configurations Beaumanoir.

- **S1 — SAP**, [Product Availability Check](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/86990a56d448792de10000000a44538d.html), *Use* ; [Backorder Processing — Supply Assignment](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html), *Supply Selection*, *Reason Codes*, *Reassignment* et stratégies BOP. Édition 2025 FPS01, février 2026 ; passages Help indexés consultés. ELM035, complément ELM016/ELM032.
- **S2 — SAP**, [Configuration Options for Exception Handling](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/673b323ed3484b8bb96014c8d8c4d6c7.html), *Use/Options*, même édition ; passage indexé consulté. ELM035.
- **S3 — Microsoft**, [Reserve inventory quantities](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities), introduction et *Policies on the Inventory and warehouse management parameters page*. Page mise à jour le 29/08/2025, texte consulté ; édition produit précise non affichée. ELM034, MKT14 complément produit.
- **S4 — SAP**, [Order Promising (2LN)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/a84abdd39b9c4c7bb46e82f7adc2d2b5.html), liste des fonctions PAC/BOP ; documentation Cloud Public Edition affichée *2608 Latest*, passage indexé consulté. Complément : [OData API: Advanced Backorder Processing Run](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f5d3e1005efd4e86acf9a65abf428082/d5d215e9ab124c8888e2d399f4b603fe.html?locale=en-US&state=PRODUCTION&version=2023.000), nouveautés S/4HANA 2023, *Business Details* et tableau classant l’API dans Advanced Order Promising / Advanced Available to Promise. ELM036 : classification de solution, pas feuille RBA.

## Détail sous les fonctions

La [réponse à U32](../marche/detail-fonctions-stock-promesse.md) examine les opérations, objets, états, variantes et règles documentés chez SAP et Microsoft. P70 distingue la profondeur de description et la profondeur de la carte de capacités ; aucun nouveau candidat n’est adopté.

# Lot 3 — pilotes approfondis et convention fait–document

19 septembre 2026 — U460/U461. Le lot dispose de cinq fiches et quinze cas concrets pour une revue PO/expert. Le principe fait–document est tranché ; la recette métier et la généralisation ne sont pas déclarées terminées.

## Décision intégrée

U461 confirme : **tout fait de gestion est associé à un document métier identifié**, éventuellement conservé sous forme structurée sans PDF.

Le principe est ajouté au backlog, aux conventions et au brouillon du guide méthodologique. V0-P01 est résolu au niveau de ce principe. Les exemples distinguent la commande d’achat attendue, le document de réception et le fait « 60 pièces reçues vendredi ».

Le contrôle du modèle exige désormais une relation `records` de document vers fait lorsque le nouveau principe est présent. Il vérifie une association effective à un document du modèle ; il n’impose pas un document unique par fait, un fichier, une politique de version ou une règle de correction. Les publications antérieures conservent leur contrat.

## Modifications métier

| Élément | Modification et intérêt |
| --- | --- |
| Product Reference | Comparaison Microsoft ajoutée ; la projection FLOW est distinguée du périmètre plus large d’administration des maîtres. |
| Product Reference Ingestion | Comparaison Microsoft ajoutée ; autorité sur le contenu et source d’alimentation sont distinguées. |
| Fulfillment Commitment | Nom canonique rétabli dans une différence de comparaison qui utilisait encore Promise Management. |
| Six termes du glossaire | Contextes concrets ajoutés pour Product Reference, Product, Product Variant, Product Unit, fait de gestion et document. Définitions existantes préservées. |
| Product Unit | Appui sémantique GS1 ajouté ; aucune codification ou conformité obligatoire déduite. |
| Fait de gestion | Exemple Microsoft de réception documentée ajouté ; la convention générale demeure un choix FLOW. |

Les quatre nouvelles comparaisons portent leurs sources, passages, dates, points communs, différences et positions FLOW dans les fiches concernées. Elles restent proposées. Les repères Microsoft existants pour Reservation et Supply Assignment ont aussi été relus pour les pilotes ; aucun découpage produit n’est importé.

## Cinq pilotes et quinze cas

Le [support de revue](pilotes.md) est généré depuis [l’annexe YAML](../../modeles/backlog/information-pilots-U458.yaml), qui reste la source. Chaque fiche explicite informations, responsabilités et frontières.

- **Purchase Order** : réception partielle documentée, réponse fournisseur différente de la demande, achat d’une prestation. Le document de réception candidat ne remplace ni le bon de commande ni l’engagement fournisseur.
- **Product Reference** : variante partagée par deux catalogues, caractéristiques contradictoires, information reçue récemment mais ancienne. Autorité, émetteur, contexte, validité et fraîcheur utile sont distingués. Aucun acteur réel ou seuil de fraîcheur inventé.
- **Fulfillment Commitment** : proposition sans confirmation, remplacement de ressource à conditions constantes, retard sans changement de ressource.
- **Supply Assignment** : affectation sans réservation, affectation gelée, application d’un plan recalculé.
- **Reservation** : quantité réservée avant affectation d’un lot, échéance dépassée, annulation de commande.

**Sept cas expliquent une frontière du modèle courant ; huit révèlent une règle à préciser.** Il s’agit d’une revue documentaire, pas de quinze tests métier validés par un PO. Les conclusions ouvertes sont rattachées aux questions V0-P02/P03/A01/A02/A06.

La lecture transversale reste simple : la commande porte l’attendu ; Fulfillment Commitment porte l’engagement de satisfaction ; Supply Assignment relie des ressources à la commande ; seule Reservation bloque leur usage concurrent ; le fait et son document associé rendent compte d’un constat. Cette lecture ne prescrit pas un enchaînement universel.

## Appuis et limites marché

- Microsoft [Product information overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information) : appui au vocabulaire des références et variantes ; le périmètre FLOW reste celui d’une projection.
- Microsoft [Exchange data between systems](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-exchange-data) : exemple de réception de références, dans un contexte produit spécifique.
- GS1 [identification et sérialisation](https://support.gs1.org/support/solutions/articles/43000734238-how-does-serialisation-differ-from-unique-identification-in-the-gs1-system-) : éclairage sur la distinction référence/instance, sans conformité globale déduite.
- Microsoft [réception d’achat](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/record-receipt-goods-purchase-order) : exemple de document associé au constat, sans prescription universelle.

Sources relues le 19 septembre 2026. Provenance : ELM280–285 et CMP175–178. Le tutoriel communautaire ArchiMate déjà utilisé a été revu : ce support pédagogique ne prescrit pas le lien obligatoire FLOW et n’est pas une preuve normative concernant ArchiMate 4. Aucun constat de standardisation ou d’innovation n’est fabriqué.

## Contrôles et portée

- Validation générale : **0 erreur**, index actualisé à **1 660 sources**.
- **18 tests Python réussis**, dont 7 couvrent la convention fait–document. Les 4 tests d’association du guide ont été relancés hors sandbox après un refus d’accès Windows à leurs répertoires temporaires ; ils passent. Les quatre répertoires vides de cet essai ont été nettoyés.
- Brouillon méthodologique valide ; liens des pilotes, termes, sources et questions vérifiés.
- **142 identités de nœuds et 346 relations conservées** ; aucune capacité ou information candidate promue en nouveau nœud. Définitions, états de revue et empreintes d’accord existantes préservés.
- **303 fichiers historiques et de publication identiques**. [Preuve des invariants](verification.json).
- Restitution backlog régénérée. Aucun code frontend modifié dans ce lot ; pas de compilation frontend nécessaire.

Le suivi unique est [v0-readiness.yaml](../../modeles/backlog/v0-readiness.yaml). Restent à préciser l’autorité effective des références, l’identité et les versions des engagements/documents, les autorisations de révision et le devenir des réservations dans les exceptions.

La prochaine étape du plan est la préparation du contrat minimal des informations métier et de leur navigation dans Atlas, à partir de ces cas. Les inconnues restent explicites ; elles ne justifient ni un maître supposé ni une cardinalité par analogie avec un ERP. La généralisation attend la relecture des pilotes.

**Atlas continue de présenter v010.** Ces changements de contenu et le guide brouillon attendent une nouvelle release demandée séparément. Aucun commit, push ou changement de serveur effectué.

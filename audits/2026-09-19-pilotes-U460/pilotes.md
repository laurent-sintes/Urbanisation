# Cinq pilotes métier — revue U460/U461

Lecture générée depuis [information-pilots-U458.yaml](../../modeles/backlog/information-pilots-U458.yaml). Le YAML reste la source. Exemples fictifs et descriptions proposées ; aucune réalisation installée supposée.

**Décision retenue (U461).** Tout fait de gestion est associé à un document métier identifié, éventuellement structuré sans PDF. Les règles de version, correction et nombre exact de documents restent à préciser.

**Résultat de la revue documentaire.** Quinze cas : sept expliquent une frontière déjà posée ; huit exposent une règle métier encore ouverte. Ce travail ne remplace pas une relecture PO/expert.

| Notion | Question à laquelle elle répond |
| --- | --- |
| Attendu de commande | Que demande-t-on ? |
| Fulfillment Commitment | Que propose-t-on ou que s’engage-t-on à satisfaire ? |
| Supply Assignment | Quelles ressources sont retenues pour quelles commandes ? |
| Reservation | Quelle ressource est engagée de manière opposable aux usages concurrents ? |
| Fait de gestion et document associé | Que constate-t-on, et quel document identifié le consigne ? |

## Purchase Order

Maintenir les attentes d’achat et expliquer ce qui reste à satisfaire.

**Responsabilités et frontières**

- Distinguer ce qui est demandé au fournisseur, sa réponse et les conditions acceptées.
- Conserver biens ou prestations, quantités ou unités, destinations et échéances applicables.
- Rapprocher les résultats reçus avec les attendus de la commande.
- Order Lifecycle Management conserve les évolutions du cycle de vie.
- Order Structuring conserve scission, regroupement et fusion ; Order Archiving la conservation.
- Service Reconciliation qualifie les résultats des prestations ; Inventory Management tient les mouvements de stock.
- La négociation contractuelle, la finance et la réalisation physique ne sont pas absorbées.

**Informations à éprouver**

- **Purchase Order** : Objet commande, distinct de la capacité ; référence lexicale TER070. Informations utiles : Parties et rôles, Biens ou prestations attendus, Quantités et unités, Destinations, Échéances, Conditions applicables. Attendus ou lignes ; plusieurs parcours peuvent coexister. Identité des lignes et cardinalités à éprouver.
- **Supplier Commitment** : Réponse puis engagement fournisseur accepté ; distinct de la demande et de notre promesse client. Informations utiles : Quantités, Dates, Conditions, Lien avec les attendus concernés. Proposition conceptuelle ; aucun second objet canonique créé.
- **Purchase Order Document** : Bon de commande exprimant le contenu de la commande à un moment donné ; proposition lexicale TER086. Aucune règle de version, signature, immutabilité ou cardinalité nouvelle.
- **Receipt Fact** : Fait de réception associé à un document métier identifié, à rapprocher de l’attendu (convention U461). Informations utiles : Quantité et unité constatées, Attendu concerné, Moment du constat, Écart expliqué, Document métier associé identifié. Exemple métier, pas un message ni un nouveau nœud.
- **Receipt Document** : Document identifié qui consigne la réception ; peut être structuré sans PDF. Informations utiles : Référence du document, Constat de réception consigné, Attendus concernés. Exemple candidat du pilote ; pas un nouveau nœud. Identité, version, correction et nombre exact de documents à instruire.

**Responsabilités sur les informations — propositions de lecture**

| Information | Responsabilité | Intervention et limite |
| --- | --- | --- |
| Attendus d’achat | Purchase Order | Établit et maintient. Biens ou prestations, quantités, échéances et reste à satisfaire. |
| Résultats de prestation et écarts | Service Reconciliation | Rapproche et qualifie. Transmet les faits utiles à Purchase Order ; ne se substitue pas à la réception physique. |
| Document de réception associé au fait | Purchase Order | Utilise pour le rapprochement. Porteur de production et règles de correction du document à préciser ; aucune propriété exclusive déduite. |

**Exemple fictif.** 100 pièces demandées vendredi ; le fournisseur propose 60 vendredi et 40 mardi. Accepter sa réponse ne révise pas automatiquement la promesse client. Lorsque 60 pièces sont réellement reçues, le constat explique les 40 restantes, sans confondre confirmation fournisseur et réalisation. Le fait « 60 pièces reçues » est associé au document de réception identifié REC-EXEMPLE-01, sous forme structurée dans cet exemple ; ce document ne remplace ni le bon de commande ni l’engagement fournisseur.

**Cas de revue**

### Réception partielle documentée

100 pièces attendues ; 60 réellement reçues.

Le document REC-EXEMPLE-01 consigne le fait de réception ; le rapprochement explique 40 restantes.

**Limite.** Une confirmation fournisseur ne constitue pas une réception.

**Conclusion documentaire.** Frontière expliquée par le modèle courant.

### Réponse fournisseur différente de la demande

100 vendredi demandées ; réponse de 60 vendredi et 40 mardi.

Demande, réponse et conditions acceptées restent distinguées ; la promesse client ne change pas automatiquement.

**Limite.** Qui accepte une révision et comment l’identifier restent à qualifier.

**Conclusion documentaire.** Règle à préciser : V0-P03.

### Achat d’une prestation

Une prestation achetée est annoncée terminée ; un écart est constaté.

Purchase Order conserve l’attendu d’achat ; Service Reconciliation qualifie le résultat. Le fait de gestion est associé à un document identifié.

**Limite.** Ne pas transformer une prestation en quantité de stock ; le document métier exact reste à qualifier.

**Conclusion documentaire.** Règle à préciser : V0-P03.

## Product Reference

Mettre à disposition de Supply des références produit communes, reçues de leurs autorités externes.

**Responsabilités et frontières**

- Recevoir et projeter les références Product et Product Variant.
- Préserver la distinction avec Product Unit, exemplaire physique individuel.
- Distinguer une référence produit du catalogue qui la propose.
- Aucune administration implicite de maître produit dans Supply.
- Aucun PIM, ERP, propriétaire Beaumanoir ou flux installé supposé.

**Informations à éprouver**

- **Product Reference** : Projection d’informations de référence, à relier à leur origine métier. Informations utiles : Identité Product, Déclinaisons Product Variant, Rôle Article ou Container, Identifiants applicables. Product, Product Variant et Product Unit conservent leurs sens du glossaire ; aucune nouvelle clé technique.
- **Reference Origin** : Informations de provenance métier de la projection, sans nouveau maître dans Supply. Informations utiles : Autorité déclarée sur le contenu, Source qui le transmet, Contexte concerné. Attributs conceptuels à éprouver ; ni application ni identité d’acteur réelle supposée.
- **Reference Validity** : Situer le contenu dans le temps et son contexte d’usage. Informations utiles : Validité applicable lorsqu’elle est connue, Moment de réception, Fraîcheur requise selon l’usage. Aucun champ technique obligatoire, seuil universel ou stratégie de conflit imposé.

**Responsabilités sur les informations — propositions de lecture**

| Information | Responsabilité | Intervention et limite |
| --- | --- | --- |
| Product / Product Variant | Product Reference Ingestion | Reçoit et actualise la projection. L’autorité sur les maîtres reste externe. |
| Référence produit utile à l’achat | Purchase Order | Consulte. La dépendance publiée ne constitue pas une preuve de flux installé. |

**Projection : informations à distinguer**

- **Autorité métier** : Extérieure à Supply ; responsabilité métier précise non établie dans ce pilote.
- **Source d’alimentation** : Information transmise par une autorité ou un relais à identifier ; ne pas assimiler automatiquement émetteur et autorité.
- **Contexte** : Sens, périmètre et validité des références utilisées par les commandes et les opérations.
- **Fraîcheur utile** : Ancienneté de l’information disponible par rapport au besoin métier. Recevoir maintenant une ancienne description ne la rend pas récente ; aucun délai universel ni arrêt automatique des commandes adopté.
- **Contradiction** : Exemple à instruire : une même déclinaison est reçue avec deux caractéristiques contradictoires. Qui fait autorité, qui arbitre et quel usage reste permis pendant la résolution ?
- **Information absente** : Distinguer une référence inconnue d’une indisponibilité physique. Le comportement opérationnel permis en cas de référence absente reste à déterminer par usage.
- **Validité** : Période ou contexte dans lequel la caractéristique vaut ; distinct du moment de réception de l’information.

**Exemple fictif.** Une commande mentionne une déclinaison taille M. Supply utilise la référence reçue pour la reconnaître ; elle ne crée pas pour autant une nouvelle définition maîtresse du produit.

**Cas de revue**

### Une variante dans deux catalogues

Un tee-shirt bleu M est proposé dans deux catalogues ; deux exemplaires physiques sont présents.

Une même référence de variante peut servir aux offres ; les deux exemplaires restent deux Product Units.

**Limite.** Ni identité individuelle déduite du catalogue, ni fusion d’exemplaires.

**Conclusion documentaire.** Frontière expliquée par le modèle courant.

### Deux descriptions contradictoires

Deux sources transmettent des caractéristiques incompatibles pour la même référence.

Distinguer autorité métier et émetteur rend la question visible ; le pilote ne choisit pas le gagnant.

**Limite.** Aucun écrasement automatique par le dernier message ni arbitrage maître confié à Supply.

**Conclusion documentaire.** Règle à préciser : V0-P02.

### Information reçue récemment mais ancienne

Une description datée de lundi est reçue vendredi pour un usage samedi.

Réception, validité et fraîcheur utile sont trois questions distinctes ; il faut qualifier l’usage.

**Limite.** Aucune durée de fraîcheur ni autorisation de poursuivre inventée.

**Conclusion documentaire.** Règle à préciser : V0-P02.

## Fulfillment Commitment

Proposer, confirmer et réviser les quantités, dates et conditions de satisfaction.

**Responsabilités et frontières**

- Rendre distincts demande initiale, proposition et engagement confirmé.
- Mobiliser les décisions de faisabilité et d’échéancier sans refaire leurs arbitrages.
- Ne choisit pas une seconde fois l’échéancier ; ne modifie pas généralement le contenu de l’Order.
- Aucun mouvement physique ni réservation automatique.

**Informations à éprouver**

- **Fulfillment Commitment** : Engagement de satisfaction ; le nom est aussi celui d’une capacité, sans identité entre les deux notions. Informations utiles : Commande concernée, Quantités, Dates, Conditions, Distinction proposition et confirmation. Les engagements peuvent exprimer des parts de satisfaction ; identités et cardinalités à préciser.

**Responsabilités sur les informations — propositions de lecture**

| Information | Responsabilité | Intervention et limite |
| --- | --- | --- |
| Proposition et engagement de satisfaction | Fulfillment Commitment | Propose, confirme et révise. Quantités, dates et conditions distinctes de la demande ; autorisations détaillées à préciser. |

**Exemple fictif.** Pour 100 pièces demandées vendredi, proposer 60 vendredi et 40 lundi. Remplacer une ressource affectée peut préserver cet engagement si ses conditions restent tenues.

**Cas de revue**

### Proposition sans confirmation

60 vendredi et 40 lundi sont proposés pour une demande de 100 vendredi.

Les possibilités et la proposition n’établissent pas seules un engagement confirmé.

**Limite.** La confirmation ne produit pas implicitement une réservation.

**Conclusion documentaire.** Frontière expliquée par le modèle courant.

### Changement de ressource à conditions constantes

L’arrivage B remplace A avec les mêmes quantités, dates et conditions de satisfaction.

L’affectation change ; l’engagement de satisfaction peut rester identique.

**Limite.** La compatibilité des conditions doit être vérifiée ; aucune nouvelle autorisation générale déduite.

**Conclusion documentaire.** Frontière expliquée par le modèle courant.

### Retard sans changement de ressource

La même ressource reste affectée, mais un retard compromet la date promise.

Le retard appelle le réexamen de l’engagement, sans effacer la demande ni modifier automatiquement la promesse.

**Limite.** L’autorité qui accepte ou refuse la révision reste à préciser.

**Conclusion documentaire.** Règle à préciser : V0-P03.

## Supply Assignment

Maintenir les ressources retenues pour des commandes identifiées.

**Responsabilités et frontières**

- Matérialiser les affectations retenues et leurs modifications autorisées.
- Mobiliser les décisions spécialisées qui déterminent les choix.
- Une affectation ne bloque pas les usages concurrents.
- Gel de modification, réservation de ressource et engagement de satisfaction ont des effets distincts.

**Informations à éprouver**

- **Supply Assignment** : Lien métier entre ressource et commande ; résultat maintenu par la capacité homonyme. Informations utiles : Commande concernée, Ressource retenue, Quantité, Conditions temporelles applicables. Aucun objet technique ni identité de ligne imposés ; la maille dépend des ressources et commandes du cas.

**Responsabilités sur les informations — propositions de lecture**

| Information | Responsabilité | Intervention et limite |
| --- | --- | --- |
| Lien ressource–commande | Supply Assignment | Établit et modifie selon choix autorisé. Ne bloque pas les usages concurrents ; ne choisit pas à nouveau le plan. |

**Exemple fictif.** Remplacer l’affectation de 40 pièces de l’arrivage A par celle de l’arrivage B sans changer la promesse.

**Cas de revue**

### Affectation sans réservation

40 pièces d’un arrivage sont affectées à la commande A ; B les demande aussi.

L’affectation seule ne donne pas à A un droit opposable à B.

**Limite.** La politique d’arbitrage reste distincte ; ne pas annoncer une disponibilité physique garantie.

**Conclusion documentaire.** Frontière expliquée par le modèle courant.

### Affectation gelée

Une modification de l’affectation est interdite dans le scénario.

Le gel protège la modification du lien ; il ne devient pas une réservation de ressource.

**Limite.** Le gel n’interdit pas à lui seul tout usage concurrent.

**Conclusion documentaire.** Frontière expliquée par le modèle courant.

### Plan recalculé

Un nouveau plan recommande de remplacer A par B.

La recommandation et son application aux liens ressource–commande restent distinctes.

**Limite.** Les conditions de prise en compte et les effets sur les Orders sont à préciser.

**Conclusion documentaire.** Règle à préciser : V0-A02.

## Reservation

Donner effet à un engagement de quantité dont les usages concurrents doivent tenir compte.

**Responsabilités et frontières**

- Établir l’engagement de ressource pour le besoin identifié.
- Le rendre opposable aux usages concurrents selon la frontière adoptée.
- Un droit exclusif peut précéder l’affectation d’un lot précis.
- Ne pas déduire expiration, consommation, libération ou déclenchement automatique.

**Informations à éprouver**

- **Reservation** : Engagement portant sur la ressource ; distinct de la promesse de satisfaction et de l’affectation. Informations utiles : Besoin bénéficiaire, Quantité, Périmètre de ressource concerné, Conditions applicables. Les droits et leur évolution restent à qualifier ; aucun mécanisme de concurrence technique.

**Responsabilités sur les informations — propositions de lecture**

| Information | Responsabilité | Intervention et limite |
| --- | --- | --- |
| Engagement de ressource opposable | Reservation | Établit. Effet de blocage concurrent adopté ; détails de libération et de consommation ouverts. |

**Exemple fictif.** Une réservation de 40 pièces exclut leur usage concurrent même si le lot précis sera affecté ultérieurement.

**Cas de revue**

### Quantité réservée sans lot individuel

40 pièces d’un périmètre de ressource sont réservées ; le lot précis n’est pas encore affecté.

La réservation peut être opposable avant la désignation d’un lot précis.

**Limite.** Pas d’affectation physique ni de mouvement de stock déduits.

**Conclusion documentaire.** Frontière expliquée par le modèle courant.

### Échéance dépassée

Une réservation existe ; l’échéance demandée est dépassée.

Il faut une règle explicite pour décider du maintien, de l’expiration ou de la libération.

**Limite.** Aucune libération automatique déduite de la seule date.

**Conclusion documentaire.** Règle à préciser : V0-A01, V0-A06.

### Commande annulée

L’annulation d’une commande bénéficiant d’une réservation est demandée.

Distinguer autorisation d’annulation, évolution de la commande et devenir de l’engagement de ressource.

**Limite.** Le devenir de la réservation et ses conditions d’application restent à préciser.

**Conclusion documentaire.** Règle à préciser : V0-A01, V0-A02, V0-A06.

## Repères marché

Rapprochements proposés, maintenant portés par les fiches du backlog ; ils attendent une publication pour apparaître dans Atlas.

- **D08 — Recouvrement partiel** : [Product information overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information). Appui sur un vocabulaire établi, avec une frontière FLOW explicite : recevoir les références sans administrer leurs maîtres.
- **D08.d — Recouvrement partiel** : [Exchange data between systems](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-exchange-data). Appui sur un mécanisme documenté ; distinguer autorité, émetteur et projection. Aucun flux installé supposé.
- **TER059 — Appui sémantique** : [How does serialisation differ from unique identification in the GS1 System?](https://support.gs1.org/support/solutions/articles/43000734238-how-does-serialisation-differ-from-unique-identification-in-the-gs1-system-). Appui sémantique sur GS1, sans GTIN obligatoire ni affirmation de conformité au standard.
- **TER036 — Appui sémantique** : [Record the receipt of goods on the purchase order](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/record-receipt-goods-purchase-order). Le lien obligatoire fait–document est une convention FLOW ; cet exemple l’illustre sans la prescrire.

Réservations et liens aux demandes confirmées : documentation Microsoft relue, ELM283/284. Les rapprochements déjà présents sur Reservation et Supply Assignment restent distincts des règles FLOW.

## Questions restantes

- **V0-P02** : Autorité métier effective, source d’alimentation, portée, validité, fraîcheur utile et traitement des contradictions de Product Reference. Aucun maître installé inventé.
- **V0-P03** : Identité des attendus, des engagements et de leurs versions ; qui accepte ou refuse une révision. Aucune cardinalité ni autorisation généralisée depuis un exemple.
- **V0-A01** : Expiration, consommation, libération, automatisation éventuelle et mécanismes techniques ; règles d’admissibilité des protections distinctes.
- **V0-A02** : Contrat détaillé d’application du plan aux affectations, structures et états des Orders, selon le scénario.
- **V0-A06** : Porteur de gouvernance et application des versions opérationnelles des politiques de réservation, distinct de D05.h qui décide.

Relire les cinq fiches avec PO et expert ; instruire V0-P02/P03 et les règles ciblées sans bloquer la description des frontières déjà établies. Lot 4 : contrat minimal et navigation des informations, sans généralisation anticipée.

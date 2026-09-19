# Cinq pilotes — support de revue

Vue générée depuis `modeles/backlog/information-pilots-U458.yaml`. Propositions internes, sans publication ni adoption globale.

## Purchase Order

Maintenir les attentes d’achat et expliquer ce qui reste à satisfaire.

**Responsabilités**

- Distinguer ce qui est demandé au fournisseur, sa réponse et les conditions acceptées.
- Conserver biens ou prestations, quantités ou unités, destinations et échéances applicables.
- Rapprocher les résultats reçus avec les attendus de la commande.

**Frontières**

- Order Lifecycle Management conserve les évolutions du cycle de vie.
- Order Structuring conserve scission, regroupement et fusion ; Order Archiving la conservation.
- Service Reconciliation qualifie les résultats des prestations ; Inventory Management tient les mouvements de stock.
- La négociation contractuelle, la finance et la réalisation physique ne sont pas absorbées.

**Informations à éprouver**

- **Purchase Order** : Objet commande, distinct de la capacité ; référence lexicale TER070. Informations utiles : Parties et rôles, Biens ou prestations attendus, Quantités et unités, Destinations, Échéances, Conditions applicables.
- **Supplier Commitment** : Réponse puis engagement fournisseur accepté ; distinct de la demande et de notre promesse client. Informations utiles : Quantités, Dates, Conditions, Lien avec les attendus concernés.
- **Purchase Order Document** : Bon de commande exprimant le contenu de la commande à un moment donné ; proposition lexicale TER086.
- **Receipt Fact** : Constat de réception à rapprocher de l’attendu ; document porteur à qualifier selon la convention fait/document. Informations utiles : Quantité et unité constatées, Attendu concerné, Moment du constat, Écart expliqué.

**Exemple fictif.** 100 pièces demandées vendredi ; le fournisseur propose 60 vendredi et 40 mardi. Accepter sa réponse ne révise pas automatiquement la promesse client. Lorsque 60 pièces sont réellement reçues, le constat explique les 40 restantes, sans confondre confirmation fournisseur et réalisation.

Questions : V0-P01, V0-P03.

## Product Reference

Mettre à disposition de Supply des références produit communes, reçues de leurs autorités externes.

**Responsabilités**

- Recevoir et projeter les références Product et Product Variant.
- Préserver la distinction avec Product Unit, exemplaire physique individuel.
- Distinguer une référence produit du catalogue qui la propose.

**Frontières**

- Aucune administration implicite de maître produit dans Supply.
- Aucun PIM, ERP, propriétaire Beaumanoir ou flux installé supposé.

**Informations à éprouver**

- **Product Reference** : Projection d’informations de référence, à relier à leur origine métier. Informations utiles : Identité Product, Déclinaisons Product Variant, Rôle Article ou Container, Identifiants applicables.

**Projection**

- Extérieure à Supply ; responsabilité métier précise non établie dans ce pilote.
- Information transmise par une autorité ou un relais à identifier ; ne pas assimiler automatiquement émetteur et autorité.
- Sens, périmètre et validité des références utilisées par les commandes et les opérations.
- Besoin métier à définir selon l’usage ; aucun délai universel inventé.
- Exemple à instruire : une même déclinaison est reçue avec deux caractéristiques contradictoires. Qui fait autorité, qui arbitre et quel usage reste permis pendant la résolution ?

**Exemple fictif.** Une commande mentionne une déclinaison taille M. Supply utilise la référence reçue pour la reconnaître ; elle ne crée pas pour autant une nouvelle définition maîtresse du produit.

Questions : V0-P02.

## Fulfillment Commitment

Proposer, confirmer et réviser les quantités, dates et conditions de satisfaction.

**Responsabilités**

- Rendre distincts demande initiale, proposition et engagement confirmé.
- Mobiliser les décisions de faisabilité et d’échéancier sans refaire leurs arbitrages.

**Frontières**

- Ne choisit pas une seconde fois l’échéancier ; ne modifie pas généralement le contenu de l’Order.
- Aucun mouvement physique ni réservation automatique.

**Informations à éprouver**

- **Fulfillment Commitment** : Engagement de satisfaction ; le nom est aussi celui d’une capacité, sans identité entre les deux notions. Informations utiles : Commande concernée, Quantités, Dates, Conditions, Distinction proposition et confirmation.

**Exemple fictif.** Pour 100 pièces demandées vendredi, proposer 60 vendredi et 40 lundi. Remplacer une ressource affectée peut préserver cet engagement si ses conditions restent tenues.

Questions : V0-P03, V0-A02.

## Supply Assignment

Maintenir les ressources retenues pour des commandes identifiées.

**Responsabilités**

- Matérialiser les affectations retenues et leurs modifications autorisées.
- Mobiliser les décisions spécialisées qui déterminent les choix.

**Frontières**

- Une affectation ne bloque pas les usages concurrents.
- Gel de modification, réservation de ressource et engagement de satisfaction ont des effets distincts.

**Informations à éprouver**

- **Supply Assignment** : Lien métier entre ressource et commande ; résultat maintenu par la capacité homonyme. Informations utiles : Commande concernée, Ressource retenue, Quantité, Conditions temporelles applicables.

**Exemple fictif.** Remplacer l’affectation de 40 pièces de l’arrivage A par celle de l’arrivage B sans changer la promesse.

Questions : V0-A02.

## Reservation

Donner effet à un engagement de quantité dont les usages concurrents doivent tenir compte.

**Responsabilités**

- Établir l’engagement de ressource pour le besoin identifié.
- Le rendre opposable aux usages concurrents selon la frontière adoptée.

**Frontières**

- Un droit exclusif peut précéder l’affectation d’un lot précis.
- Ne pas déduire expiration, consommation, libération ou déclenchement automatique.

**Informations à éprouver**

- **Reservation** : Engagement portant sur la ressource ; distinct de la promesse de satisfaction et de l’affectation. Informations utiles : Besoin bénéficiaire, Quantité, Périmètre de ressource concerné, Conditions applicables.

**Exemple fictif.** Une réservation de 40 pièces exclut leur usage concurrent même si le lot précis sera affecté ultérieurement.

Questions : V0-A01, V0-A06.

## Coopération Commerce–Supply–logistique

Exemple pédagogique fictif ; pas un workflow universel ni des flux installés.

1. Commerce exprime une intention de 100 pièces vendredi.
2. Supply détermine les possibilités ; Fulfillment Commitment propose 60 vendredi et 40 lundi.
3. Une réponse est confirmée selon les autorisations applicables, encore à préciser.
4. Supply Assignment matérialise les ressources retenues. Leur usage concurrent reste possible tant qu’aucune réservation ne le bloque.
5. Reservation peut établir le droit opposable ; son déclenchement n’est pas réputé automatique.
6. Les prestations attendues sont adressées aux responsabilités de réalisation concernées, sans confondre attente et réalisation.
7. Les constats et écarts alimentent le rapprochement des prestations et des commandes, chacun dans sa responsabilité.

**Refus et écarts**

- Un refus fournisseur n’efface pas la demande et ne restaure aucune capacité physique.
- Un retard conduit à réexaminer les engagements ; il ne les modifie pas automatiquement.
- Une réception partielle explique le restant à satisfaire sans devenir une nouvelle promesse.

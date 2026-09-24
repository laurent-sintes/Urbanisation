# Transport : familles d’Orders et variantes — recherche U699/U700

24 septembre 2026. Les propositions font autorité dans [l’annexe du backlog unique](../modeles/backlog/transport-order-behavior-proposals-U699.yaml). Ce document expose les preuves et le raisonnement ; aucun nouvel audit ouvert.

## Conclusion

Conserver Transport Order pour faire déplacer les marchandises. Proposer Transport Booking Order comme seconde famille seulement lorsque la réservation de capacité constitue une demande et un engagement autonomes. La présence d’un document Booking dans un TMS ne suffit pas à créer cette responsabilité. Le transport routier, maritime, aérien, colis, dédié ou groupé ne crée pas mécaniquement des capacités distinctes.

## Comportements proposés

Le socle est la demande de déplacement point à point. Les cinq variantes suivantes se combinent : par exemple une tournée multi-arrêts peut être programmée et comporter des rendez-vous. Elles ne constituent pas des sous-niveaux ou un enchaînement obligatoire.

### Multi-Stop Transport

Tenir une demande comportant plusieurs lieux de collecte ou livraison, les exigences par arrêt et les suites d’un changement ou d’une réalisation partielle.

**Différence métier :** Plusieurs points de résultat : une livraison effectuée ne clôture pas nécessairement l’ensemble de l’ordre.
**Exemple fictif fashion :** Une tournée dessert trois magasins ; deux sont livrés, le troisième reste à traiter.
**Frontière :** L’ordre conserve les arrêts demandés et leurs contraintes. Optimiser la tournée ou décider de sa modification reste dans la coordination ; les tournées internes d’un transporteur ne créent pas ce comportement si FLOW ne les commande pas.
**Appuis :** ELM685, ELM686.

### Multi-Leg Transport

Tenir une demande de transport à plusieurs étapes explicites, avec points de remise, exigences intermédiaires et résultat final convenus.

**Différence métier :** La réalisation d’une étape ou d’un transbordement ne vaut pas livraison finale ; conditions et engagements intermédiaires à préserver.
**Exemple fictif fashion :** Pré-acheminement, traversée maritime puis livraison à l’entrepôt ; exigences de remise précisées aux interfaces.
**Frontière :** Variante seulement si les étapes sont exposées dans la prestation confiée. Plusieurs Transport Orders confiés séparément sont une composition pilotée par Fulfilment, pas des sous-Orders obligatoires ni des sous-comportements.
**Appuis :** ELM687, ELM688.

### Scheduled Transport

Tenir une demande rattachée à un départ ou à un service programmé, et les conséquences d’un changement de programme ou d’un départ manqué.

**Différence métier :** L’engagement dépend d’une occurrence de service identifiée ; changer de départ peut nécessiter une nouvelle acceptation.
**Exemple fictif fashion :** La navette entre deux entrepôts part chaque soir ; le lot doit être pris en charge sur le départ convenu.
**Frontière :** Décrire le rattachement et ses suites, pas construire les horaires, le réseau ou une tournée. Une simple date demandée ne suffit pas. Deux sources SAP attestent le mécanisme sans consensus interéditeurs.
**Appuis :** ELM689, ELM690.

### Pickup & Delivery Appointments

Tenir les créneaux de collecte ou livraison convenus avec les parties, leurs confirmations, modifications et conséquences sur l’engagement.

**Différence métier :** Distinguer une fenêtre souhaitée, un horaire estimé et un rendez-vous effectivement accepté.
**Exemple fictif fashion :** Un magasin confirme un créneau de réception ; un retard impose de tenir le créneau renégocié.
**Frontière :** Aucun Appointment Order systématique. Ne pas recopier la planification de quai ou la décision d’adaptation. Oracle documente aussi la collecte ; DHL étaye surtout la livraison.
**Appuis :** ELM691, ELM692.

### Delivery Rescheduling & Redirection

Tenir les demandes autorisées de report ou changement de lieu de remise et les suites d’une tentative de livraison infructueuse.

**Différence métier :** Une instruction du destinataire peut modifier le résultat convenu ; conserver demande, acceptation et limites données par l’expéditeur.
**Exemple fictif fashion :** Après une absence, le destinataire demande un retrait en point relais ; tenir la nouvelle remise acceptée.
**Frontière :** La demande de changement ne vaut ni acceptation ni modification automatique de la promesse commerciale. Fulfilment choisit les adaptations ; Order Management conserve les engagements à satisfaire. Proche du rendez-vous, mais couvre aussi changement de lieu et remise après échec.
**Appuis :** ELM692, ELM693.

## Deuxième famille possible : Transport Booking Order

La pré-réservation d’espace est documentée chez SAP pour un chargeur maritime et par DCSA pour les échanges de booking. La confirmation peut déjà engager le prestataire à transporter : réservation et ordre de déplacement ne sont donc pas nécessairement deux engagements distincts. Le nom Transport Booking Order est une proposition FLOW ; les sources ne prescrivent pas cette taxonomie.

Le critère de séparation est concret : FLOW peut-il demander et suivre une capacité confirmée, la modifier ou la libérer, alors que les instructions détaillées de déplacement ne sont pas encore arrêtées ? Si oui, une famille distincte rend ce résultat visible. Si non, le booking reste une étape de Transport Order. Exemple fictif : capacité réservée pour un départ de collection, puis désignation des lots. Les affectations internes du Matching et les accords-cadres restent distincts.

## Variantes écartées comme capacités autonomes

Modes et formats de chargement caractérisent l’offre. Groupage et dédié changent des conditions, mais le regroupement interne des marchandises ne constitue pas une demande nouvelle de FLOW. La collecte ou livraison d’un retour reste un transport lié à une intention de retour. Le niveau de service urgent ne crée pas à lui seul un mécanisme distinct.

Carrier selection, tendering et optimisation de tournée restent des responsabilités de décision ou coordination ; le comportement tient les exigences et conséquences des décisions. Les constats et preuves de livraison proviennent des capacités existantes de suivi et rapprochement. La douane rend un résultat différent, mais nécessite un cadrage séparé si FLOW doit commander ce service. Freight Forwarding Order n’est pas suffisamment comparé pour être proposé ici.

## Limites de preuve

Les variantes sont attestées comme mécanismes de produits ou prestations. Leur traduction en comportements de gestion de l’ordre est une proposition de modélisation. Aucun déploiement ni besoin installé de Beaumanoir n’est déduit. Le socle Transport Order est ajouté au backlog selon U698 ; ses variantes et le booking restent proposés. Publication 2026-09-24.1 inchangée.

## Corpus primaire
- **ELM685** — [Oracle : Order Release: Order Stops](https://docs.oracle.com/en/cloud/saas/transportation/26a/otmol/planning/order_manager/or_stops.htm) ; 26A ; Creating a Shipment Stop ; accès direct.
- **ELM686** — [SAP : Multi-Pickup, Multi-Drop](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/7194e95ee2e447b9954dc449d3a06971.html) ; Version non établie dans le passage indexé ; Canceling Freight Orders, Canceling Stops ; accès indexed.
- **ELM687** — [SAP : Transportation Stages and Dates/Times in the Freight Unit](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/9c8fdae3f57b48bc9cf4d5cfae3f130c.html) ; 2025 FPS01 ; Transportation Stages ; accès indexed.
- **ELM688** — [Oracle : Order Movement](https://docs.oracle.com/en/cloud/saas/transportation/25c/otmol/planning/order_manager/order_movement/order_movement.htm) ; 25C ; Creating an order movement ; accès indexed.
- **ELM689** — [SAP : Use of Schedules](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/65978154f98b46c2b77906547c880936.html) ; Version non établie dans le passage indexé ; Features ; accès indexed.
- **ELM690** — [SAP : Ad Hoc Loading](https://help.sap.com/docs/PRODUCTS/f5d3e1005efd4e86acf9a65abf428082/df9df83274d04a79b186c38eb69e8d5b.html) ; 2025 FPS01 ; Business Details ; accès indexed.
- **ELM691** — [Oracle : Set Appointments](https://docs.oracle.com/en/cloud/saas/transportation/25c/otmol/general/appointments.htm) ; 25C ; Introduction ; Order Appointments ; Shipment Stop Appointments ; accès direct.
- **ELM692** — [DHL : NZ Exporter’s Guide to Last Mile Delivery](https://www.dhl.com/discover/en-nz/logistics-advice/logistics-insights/last-mile-delivery-solutions) ; Page évolutive, édition non indiquée ; Can customers choose their delivery time? ; What happens if the customer isn’t home? ; accès indexed.
- **ELM693** — [UPS : Help and Support Center](https://www.ups.com/us/en/business-solutions/grow-your-business-solutions) ; Page évolutive, édition non indiquée ; How do I change a delivery I’m receiving? ; accès indexed.
- **ELM694** — [SAP : Sample Ocean Freight Process for Shippers (Outbound)](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/ca69ceb75dad454bad9bbeb25613b198.html?version=latest) ; Version non établie dans le passage indexé ; Introduction du processus chargeur ; accès indexed_direct_empty.
- **ELM695** — [DCSA : Booking standard](https://dcsa.org/standards/booking) ; Présentation publique évolutive ; version du standard non établie ; The problem ; The solution ; accès direct.
- **ELM696** — [SAP : Freight Booking – Confirm](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/2f36056ae9a044bba55bcbad204b7bc5/2ef80c370bc645c19fc266b746d3094f.html) ; Version non établie dans le passage indexé ; Service Nodes : TransportationOrderBooking ; BookingCapacity ; accès indexed.
- **ELM697** — [DHL : LTL Shipment Solutions](https://www.dhl.com/gb-en/home/ship/ltl-shipping.html) ; Page évolutive, édition non indiquée ; What’s the difference between LTL, PTL and FTL? ; accès indexed.

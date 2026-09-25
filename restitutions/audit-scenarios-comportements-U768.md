# Audit des comportements et scénarios — appliqué U769

Application dans le backlog le 25 septembre 2026. Aucune nouvelle release.

## Résultat

- Sept comportements de motifs de commande retirés ; situations conservées dans les scénarios.
- Cinq variantes de Return Order précisées : engagements, quantités et preuves attendues.
- Quatre comportements de pilotage Master Planning conservés : ils ne sont pas des scénarios. Leur granularité reste une question distincte, sans refacto dans ce lot.
- Treize familles de cas complétées.
- 22 récits avec étapes et mapping mobilisent 71 capacités sur 71. Ce comptage ne vaut pas exhaustivité des variantes ni validation globale.
- 17 autres exemples structurés restent des illustrations locales sans mapping par étapes.

## Reclassifications

| Ancien comportement | Scénarios de remplacement |
| --- | --- |
| BHV061 — Initial Stocking | consignment-launch-replenishment |
| BHV062 — Continuous Replenishment | consignment-launch-replenishment |
| BHV070 — Initial Stocking | fashion-launch |
| BHV071 — Continuous Replenishment | transfer-replenishment-order-driven |
| BHV072 — Inventory Rebalancing | redistribute-protected-stock |
| BHV073 — Stock Consolidation | redistribute-protected-stock |
| BHV074 — Order-Driven Transfer | transfer-replenishment-order-driven |

## Familles de cas complétées

- **G01 — Promesse B2C concurrente, réservation puis annulation** : last-item-concurrency.
- **G02 — Substitution, autre site ou express avec prix différent** : substitution-price-service.
- **G03 — Achat supplémentaire et approvisionnement lié à une vente** : additional-purchase-partial.
- **G04 — Retrait magasin non honoré ou livraison directe fournisseur** : pickup-or-direct-shipment.
- **G05 — Transport interrompu et adaptation locale** : transport-missed-connection.
- **G06 — Prestation distante en échec ou notification ambiguë** : remote-payment-ambiguous.
- **G07 — Données corrigées ou périmées et plans contradictoires** : reference-plan-correction.
- **G08 — Redistribution et protections en concurrence** : redistribute-protected-stock.
- **G09 — Retour fournisseur : avoir, remplacement ou réparation** : supplier-return-outcomes.
- **G10 — Kit, personnalisation, nettoyage ou cross-docking** : gift-kits-crossdock.
- **G11 — Propriété en transit, à échéance ou fait douanier** : ownership-transit-deadline.
- **G12 — Split, regroupement et fusion avec engagements existants** : order-structuring-engaged.
- **G13 — Choisir un prestataire et libérer une commande B2B incomplète** : b2b-release-deadline.

## Récits du modèle

### Livrer une commande B2B avec un stock partiel

Illustration FLOW fictive : un client B2B attend 100 vêtements ; 60 sont disponibles et une rentrée de 40 est annoncée. Plusieurs solutions de livraison sont examinées.

1. **Qualifier les 100 vêtements attendus.** Le client demande 100 pièces vendredi ; il accepte une livraison partielle uniquement si elle est annoncée. Résultat : Quantité, date et condition de fractionnement sont explicites.
   Capacités : Sales Order — Porter la demande et les engagements acceptés. ; Inventory Visibility — Exposer les 60 pièces disponibles et la rentrée annoncée de 40 avec ses réserves.
2. **Construire les possibilités.** Comparer 60 pièces plus tôt puis 40 après réception, et 100 ensemble. Si une solution exige une ressource supplémentaire, tester sa faisabilité sans créer une commande d’achat. Résultat : Options datées avec leurs conditions et incertitudes.
   Capacités : Available-to-Promise (ATP) — Évaluer le stock présent et projeté net des engagements et protections. ; Capable-to-Promise (CTP) — Évaluer si nécessaire les possibilités supplémentaires et leurs contraintes de capacité.
3. **Éclairer puis choisir la promesse.** Comparer deux transports à une seule expédition, sans supposer que le moins cher est toujours préférable. Résultat : Une proposition choisie, accompagnée de ses hypothèses, peut être acceptée dans la commande.
   Capacités : Profitable-to-Promise (PTP) — Produire le dossier économique local des options sans choisir. ; Promise Selection Decision — Choisir la proposition au regard du service, des évaluations et des règles.
4. **Affecter puis libérer les prestations.** Si le regroupement est accepté, affecter les ressources puis retenir les ordres éligibles jusqu’à complétude, dans la limite de la date promise. Résultat : Les prestations compatibles sont libérées ensemble ; la préparation commune est demandée explicitement.
   Capacités : Supply Assignment — Affecter les ressources dans les équilibres du master plan. ; Plan Application — Appliquer les affectations retenues. ; Service Order Release Decision — Déterminer le moment et le groupe de libération. ; Process Orchestration — Déclencher et coordonner les prestations. ; Packing Order — Porter l’exigence de conditionnement commun.

À vérifier : Évaluer, choisir, engager, affecter et libérer ont des responsabilités distinctes. La rétention ne décale pas silencieusement la promesse ; une expédition commune ne garantit pas à elle seule une palette unique.

### Remettre en vente une robe retournée

Illustration FLOW fictive. Une cliente retourne une robe dont une couture est ouverte. Le retour est accepté, mais la remise en stock vendable dépend du contrôle et de la réparation.

1. **Recevoir et contrôler.** Le retour est attendu puis reçu ; le prestataire confirme la couture ouverte et transmet le contrôle. Résultat : La robe est reçue mais sa remise en vente reste conditionnelle.
   Capacités : Return Order — Porter le retour attendu et son achèvement. ; Inspection Order — Demander le contrôle et son résultat. ; Operations Tracking — Capter les faits d’exécution distants.
2. **Choisir le devenir.** La réparation est autorisée et jugée pertinente pour cette robe ; une pièce irréparable suivrait une autre route. Résultat : Une route de réparation est choisie sans confondre retour et réparation.
   Capacités : Return Disposition Decision — Décider de la destination et du traitement de l’article retourné. ; Repair & Alteration Order — Porter la prestation de réparation confiée. ; Process Orchestration — Coordonner les dépendances et attendre la fin de réparation.
3. **Rendre la robe à nouveau disponible.** Après réparation et contrôle conforme, les faits reconnus autorisent le reclassement du stock. Résultat : La robe apparaît dans le stock vendable avec une trace de ses mouvements.
   Capacités : Inventory Tracking — Recevoir les faits de stock. ; Inventory Ledger — Conserver les mouvements et corrections reconnus. ; Inventory Visibility — Exposer la disponibilité actualisée.

À vérifier : Le retour ne réalise pas lui-même la réparation. Un simple accusé de réception de prestation ne vaut pas réalisation conforme.

### Vendre une partie du stock consigné puis reprendre le solde

Illustration FLOW fictive. Un fournisseur confie 100 vestes à un distributeur. Selon le contrat fictif, les 30 vendues changent de propriétaire à la vente ; les 70 restantes sont reprises.

1. **Apporter les 100 vestes.** L’apport est demandé puis reçu chez le dépositaire sans achat immédiat. Résultat : 100 vestes sont détenues pour le compte du fournisseur.
   Capacités : Consignment Fill-up Order — Porter la demande d’apport en consignation. ; Inventory Tracking — Recevoir le fait de réception et sa dimension propriétaire. ; Inventory Ledger — Enregistrer le mouvement physique reconnu.
2. **Reconnaître le transfert des 30 vendues.** Le fait de vente est rapproché de la clause de l’accord ; la réception initiale ne suffit pas à changer la propriété. Résultat : Le transfert reconnu de 30 vestes est tracé avec son fondement.
   Capacités : Sales Order — Porter la vente et ses engagements. ; Agreement Visibility — Rendre accessibles les conditions applicables. ; Inventory Ownership Transfer Decision — Qualifier le déclencheur contractuel et déterminer le transfert. ; Inventory Ownership Ledger — Conserver la date, les parties, les quantités et le fondement du changement.
3. **Reprendre les 70 restantes.** La campagne se termine et le fournisseur demande la reprise du solde. Résultat : Le solde repris est rapproché de la demande et du stock.
   Capacités : Consignment Pick-up Order — Porter la demande de reprise. ; Process Orchestration — Coordonner la prestation de reprise. ; Inventory Visibility — Exposer séparément détention, propriété et disponibilité du solde.

À vérifier : Détention et propriété évoluent indépendamment. Ce cas de vente ne couvre pas les contrats à échéance ni les transferts en transit.

### Préparer une capsule pour l’ouverture de magasins

Illustration FLOW fictive. Une capsule de 200 robes doit arriver sur cintres, étiquetée et conditionnée par magasin avant l’ouverture. Un plan externe prévoit les besoins ; le stock disponible doit être réparti.

1. **Préparer les données utiles.** Les références, assortiments et prévisions sont reçus avant le calcul de réapprovisionnement. Résultat : Les besoins prévus et les données nécessaires sont accessibles avec leur origine.
   Capacités : Master Data Ingestion — Intégrer les référentiels fournis par les domaines sources. ; Plan Ingestion — Intégrer les Supply et Demand Plans externes. ; Demand Plan Visibility — Exposer les besoins prévus pertinents. ; Supply Plan Visibility — Exposer les mouvements prévus hors achats.
2. **Déterminer les transferts.** Les besoins des magasins sont confrontés aux ressources ; les affectations retenues sont appliquées. Résultat : Des demandes de transfert identifiées portent quantités et dates.
   Capacités : Replenishment — Déterminer les besoins de réapprovisionnement. ; Supply Assignment — Affecter les ressources entre demandes. ; Plan Application — Appliquer le plan retenu. ; Transfer Order — Porter chaque transfert attendu et ses engagements.
3. **Préparer puis expédier.** Le prestataire doit étiqueter, mettre sur cintre et conditionner par magasin avant la prise en charge transport. Résultat : Les prestations suivent les dépendances demandées et leur achèvement est observable.
   Capacités : Labeling Order — Porter les exigences d’étiquetage. ; Garment Finishing Order — Porter la mise sur cintre requise. ; Packing Order — Porter le conditionnement par destination. ; Transport Order — Porter le transport attendu. ; Process Orchestration — Composer et coordonner la séquence. ; Operations Tracking — Capter les résultats des prestations.

À vérifier : L’APS demeure extérieur au domaine. L’ouverture est un contexte du Transfer Order ; les exigences concrètes sont portées par les prestations.

### Réagir à une pénurie sans confondre promesse et affectation

Illustration FLOW fictive. Un lot annoncé de 100 pièces est ramené à 60. Deux clients attendent chacun 50 pièces ; leurs protections et dates diffèrent.

1. **Établir la situation.** L’annonce corrigée est reçue et rapprochée des engagements existants. Résultat : Les 40 pièces manquantes et les demandes touchées sont identifiées.
   Capacités : Inventory Tracking — Intégrer le fait corrigé. ; Inventory Visibility — Exposer les ressources actualisées. ; Order Visibility — Exposer les commandes et promesses concernées.
2. **Réexaminer les équilibres.** Comparer des répartitions possibles en respectant les protections applicables, sans modifier encore les commandes. Résultat : Une proposition de réaffectation est explicitée.
   Capacités : Master Planning — Piloter le recalcul du master plan sur le périmètre pertinent. ; Demand Prioritization — Prioriser les demandes. ; Demand Protection Policy — Fournir les règles de protection de la demande. ; Simulation & Analysis — Comparer les effets des hypothèses. ; Supply Assignment — Déterminer les affectations proposées.
3. **Réexaminer puis appliquer.** Évaluer les nouvelles possibilités de promesse et les impacts économiques avant de retenir les changements autorisés. Résultat : Les choix de promesse et d’affectation sont traçables et leur application reste distincte.
   Capacités : Available-to-Promise (ATP) — Évaluer les disponibilités restantes et projetées. ; Profitable-to-Promise (PTP) — Éclairer les impacts économiques locaux. ; Promise Selection Decision — Choisir les propositions de promesse révisées. ; Sales Order — Porter les changements d’engagement acceptés. ; Plan Application — Appliquer les affectations autorisées.

À vérifier : La réaffectation des ressources ne réécrit pas silencieusement une promesse. Le dossier économique ne décide pas à la place de Promise Selection Decision.

### Exporter des vêtements et attendre la fin des prestations distantes

Illustration FLOW fictive. Un client attend 500 chemises exportées. Le contrat fictif impose un paiement confirmé avant libération ; la douane et la facturation sont exécutées par des intervenants externes.

1. **Préparer les prestations.** Les conditions contractuelles et les besoins documentaires déterminent les prestations requises. Résultat : Transport, documents et dépendances sont définis.
   Capacités : Agreement Visibility — Exposer les conditions applicables. ; Service Requirements Decision — Déterminer les exigences de service. ; Transport Booking Order — Demander la réservation de transport. ; Document Production Order — Demander les documents requis. ; Customs Clearance Order — Porter la prestation de dédouanement confiée.
2. **Déclencher les flux financiers.** La facture puis l’encaissement sont demandés aux exécutants compétents ; une acceptation technique ne vaut pas paiement. Résultat : La collecte est en cours et son achèvement reste attendu.
   Capacités : Billing Order — Porter la demande de facturation. ; Payment Collection Order — Porter le déclenchement et le résultat attendu de collecte. ; Process Orchestration — Coordonner les dépendances et attendre les résultats.
3. **Libérer au vu des résultats.** Les notifications sont rapprochées des ordres ; la confirmation de paiement et les conditions de passage autorisent la suite. Résultat : La prestation transport est libérée sur des résultats reconnus.
   Capacités : Operations Tracking — Capter les notifications d’exécution distante. ; Service Reconciliation — Rapprocher les résultats des prestations demandées. ; Operations Visibility — Exposer les prestations terminées ou bloquées. ; Service Order Release Decision — Décider de la libération des ordres éligibles. ; Transport Order — Porter les engagements de transport.

À vérifier : Orchestrer la facturation ou l’encaissement ne signifie pas les exécuter dans Supply Chain Orchestration. Les règles du cas sont des hypothèses illustratives, pas des obligations universelles.

### Traiter un écart de comptage avant de repromettre

Illustration FLOW fictive. Un emplacement contient 58 pulls alors que le registre en indique 60 ; une commande en attend 60.

1. **Constater puis qualifier l’écart.** Un comptage contradictoire confirme 58 pièces. La correction n’est enregistrée qu’après reconnaissance selon les règles applicables. Résultat : Le registre porte une correction justifiée de deux pièces.
   Capacités : Stocktaking — Organiser le comptage et qualifier l’écart. ; Inventory Ledger — Enregistrer la correction reconnue avec sa justification.
2. **Mesurer les conséquences.** La disponibilité actualisée est confrontée à la commande ; une autre rentrée peut éventuellement combler l’écart. Résultat : Une proposition explicite est préparée pour la commande touchée.
   Capacités : Inventory Visibility — Exposer le stock corrigé et les ressources pertinentes. ; Available-to-Promise (ATP) — Évaluer la quantité et la date réalisables. ; Promise Selection Decision — Choisir la proposition à soumettre. ; Sales Order — Conserver ou modifier la promesse selon le résultat accepté.

À vérifier : Un comptage brut ne devient pas automatiquement une correction. Une correction de stock ne modifie pas à elle seule la promesse client.

### Deux clients veulent le dernier pull

Illustration FLOW fictive. À 10 h, deux clients demandent le dernier pull bleu M. Le premier panier obtient une réservation limitée ; il est ensuite annulé.

1. **Évaluer les deux demandes.** Les deux consultations peuvent voir une disponibilité avant tout engagement exclusif. Résultat : Les réponses de disponibilité restent distinctes du droit réservé.
   Capacités : Available-to-Promise (ATP) — Évaluer la quantité disponible à la date demandée. ; Inventory Visibility — Exposer le stock et les engagements connus.
2. **Retenir et engager une proposition.** Une seule réservation est accordée selon les règles applicables ; l’autre demande attend ou reçoit une alternative. Résultat : Aucune double réservation du dernier pull.
   Capacités : Reservation — Attribuer le droit réservé et son échéance. ; Promise Selection Decision — Choisir une proposition compatible avec les conditions obtenues. ; Sales Order — Porter la commande et la promesse acceptée.
3. **Annuler et libérer.** Le premier client annule avant préparation ; la réservation correspondante est levée puis la seconde demande est réévaluée. Résultat : Le pull redevient disponible sans duplication de droit.
   Capacités : Sales Order — Porter l’annulation effective. ; Reservation — Libérer le droit devenu sans objet. ; Available-to-Promise (ATP) — Réévaluer la seconde demande sur la situation actualisée.

À vérifier : Une évaluation ATP ne garantit pas à elle seule une exclusivité. L’expiration d’une réservation doit également produire un état observable avant réutilisation.

### Comparer une substitution, un autre site et un transport express

Illustration FLOW fictive. Une boutique attend 20 robes vendredi. La référence demandée arrive lundi ; une robe autorisée en substitution existe ailleurs, avec un autre prix et un transport express plus cher.

1. **Qualifier les alternatives autorisées.** Le catalogue, l’assortiment et les prix applicables permettent de comparer la robe demandée et la substitution, ainsi que les services de transport. Résultat : Les prix et conditions des alternatives sont explicites.
   Capacités : Product Catalog Visibility — Exposer les offres éligibles. ; Assortment Visibility — Vérifier l’assortiment applicable à cette boutique. ; Price Book Visibility — Exposer prix produit et service, contexte et validité.
2. **Évaluer le service et l’économie.** Comparer attente jusqu’à lundi, départ depuis un autre site et substitution livrable vendredi. Résultat : Chaque possibilité comporte date, conditions, coûts et risques connus.
   Capacités : Available-to-Promise (ATP) — Évaluer les disponibilités présentes et futures. ; Service Selection Decision — Proposer les prestations compatibles. ; Profitable-to-Promise (PTP) — Comparer les conséquences économiques sans sélectionner.
3. **Choisir et faire accepter.** La substitution plus coûteuse ne devient la promesse qu’après le choix et l’acceptation requis. Résultat : La commande conserve la référence et les conditions réellement acceptées.
   Capacités : Promise Selection Decision — Choisir la proposition au regard des règles et évaluations. ; Sales Order — Porter la modification acceptée de la demande et de la promesse.

À vérifier : Un prix de service ne se confond pas avec le prix produit. L’option la moins coûteuse ne remplace pas automatiquement l’article.

### Approvisionner une vente et traiter une confirmation fournisseur partielle

Illustration FLOW fictive. Un client demande 100 vestes vendredi sans stock disponible. Le fournisseur pourrait en livrer 100, mais confirme finalement 60 vendredi et 40 mardi.

1. **Évaluer puis planifier.** Une possibilité d’achat est évaluée ; le master plan détermine ensuite les ressources à proposer pour la vente. Résultat : L’hypothèse est distinguée de la commande réelle.
   Capacités : Capable-to-Promise (CTP) — Évaluer la faisabilité conditionnelle de l’apport. ; Master Planning — Piloter le plan et ses arbitrages. ; Supply Assignment — Déterminer l’affectation proposée. ; Plan Application — Mettre en application le plan autorisé. ; Purchase Order — Porter la demande d’achat réelle et sa confirmation.
2. **Réexaminer les engagements.** La confirmation 60/40 déclenche une réévaluation ; le client accepte le fractionnement ou une nouvelle proposition est nécessaire. Résultat : Dates et quantités confirmées restent distinctes des dates demandées.
   Capacités : Purchase Order — Conserver les deux échéances fournisseur. ; Available-to-Promise (ATP) — Évaluer les disponibilités projetées corrigées. ; Promise Selection Decision — Choisir la proposition révisée. ; Sales Order — Tenir les engagements acceptés par le client.
3. **Recevoir puis traiter une annulation de solde.** 60 sont reçues ; si le client annule les 40 restantes, la suite de l’achat dépend de son propre engagement fournisseur. Résultat : Le solde achat ne disparaît pas avec la seule annulation de vente.
   Capacités : Inventory Tracking — Capter la réception réelle. ; Purchase Order — Rapprocher réception et reste à recevoir ; tenir les suites autorisées sur le solde. ; Supply Assignment — Réexaminer l’affectation du solde devenu sans demande. ; Sales Order — Porter l’annulation des 40 demandées.

À vérifier : CTP ne crée pas l’achat. Une confirmation n’est pas une réception ; une annulation de vente n’annule pas automatiquement l’achat.

### Traiter un retrait non honoré ou une livraison directe partielle

Illustration FLOW fictive. Deux clients choisissent des services différents : Léa retire une veste en magasin ; Amir reçoit deux chemises directement du fournisseur. Aucun passage par l’entrepôt central n’est prévu.

1. **Porter les modalités promises.** La veste est préparée pour retrait ; les chemises sont demandées au fournisseur pour livraison à Amir. Résultat : Les commandes distinguent destinataire, preuve et date attendus.
   Capacités : Sales Order — Porter les modalités de chacune des ventes. ; Purchase Order — Porter l’achat avec livraison directe fournisseur. ; Process Orchestration — Coordonner les prestations adaptées à chaque parcours.
2. **Constater les exceptions.** Léa ne vient pas dans le délai prévu ; une seule chemise est remise à Amir. Résultat : Absence de retrait et livraison partielle sont connues sans clôture fictive.
   Capacités : Operations Tracking — Capter les preuves ou absences de réalisation. ; Sales Order — Tenir le reste à satisfaire de chaque vente. ; Purchase Order — Rapprocher le résultat du fournisseur et son solde.
3. **Adapter les suites.** Selon les règles acceptées, le retrait est prolongé ou annulé ; la seconde chemise reste attendue ou fait l’objet d’une nouvelle proposition. Résultat : Les quantités sont libérées ou restent engagées selon la décision effective.
   Capacités : Process Orchestration — Coordonner les suites autorisées. ; Reservation — Adapter les réservations concernées. ; Inventory Visibility — Exposer les disponibilités sans retour physique inventé. ; Promise Selection Decision — Choisir une nouvelle proposition si nécessaire.

À vérifier : Préparer ne prouve pas le retrait. La livraison directe ne crée pas de réception fictive en entrepôt.

### Sauver une livraison après une correspondance manquée

Illustration FLOW fictive. Un lot de 80 manteaux manque sa correspondance. Une liaison routière peut encore livrer vendredi, mais la place et le coût doivent être vérifiés.

1. **Qualifier l’aléa.** Le transporteur annonce le retard ; la réservation initiale n’est plus suffisante pour tenir la date. Résultat : Le segment affecté et l’engagement menacé sont identifiés.
   Capacités : Operations Tracking — Capter le fait de retard. ; Service Reconciliation — Le rapprocher de la prestation attendue. ; Transport Booking Order — Conserver la place réservée et les changements confirmés. ; Transport Order — Porter l’obligation d’acheminement.
2. **Comparer les solutions locales.** Une liaison routière offre 80 places ; sa disponibilité et ses contraintes sont qualifiées. Résultat : Une alternative réalisable et ses impacts sont exposés.
   Capacités : Service Capacity Visibility — Exposer les capacités de service annoncées. ; Service Selection Decision — Sélectionner une prestation compatible. ; Profitable-to-Promise (PTP) — Éclairer le surcoût et les risques économiques. ; Process Adaptation Decision — Déterminer l’adaptation locale préservant la promesse.
3. **Appliquer ou faire réexaminer.** Si la solution tient vendredi, les ordres sont adaptés ; sinon une réévaluation de promesse et des affectations est nécessaire. Résultat : Aucun déplacement silencieux de date ni réaffectation globale par Fulfilment.
   Capacités : Process Orchestration — Coordonner les prestations modifiées. ; Promise Selection Decision — Choisir une nouvelle proposition si la promesse devient intenable. ; Supply Assignment — Réexaminer les affectations si l’équilibre du Matching est touché.

À vérifier : La réservation de transport et le transport réalisé sont distincts. Une adaptation locale ne décide pas seule de nouveaux équilibres globaux.

### Attendre un encaissement malgré des notifications ambiguës

Illustration FLOW fictive. Une collecte de 1 000 euros est confiée à un prestataire. Deux notifications identiques annoncent 600 euros encaissés, puis un autre message annonce un échec.

1. **Attendre le résultat métier.** Le prestataire accepte la demande mais ne confirme pas encore l’encaissement. Résultat : La prestation reste en cours.
   Capacités : Payment Collection Order — Porter montant demandé et résultat attendu. ; Process Orchestration — Attendre l’achèvement requis avant de poursuivre.
2. **Rapprocher les notifications.** Les deux annonces de 600 correspondent au même fait ; l’échec contradictoire doit être qualifié. Résultat : 600 ne deviennent pas 1 200 et la contradiction reste visible.
   Capacités : Operations Tracking — Capter et corréler les faits distants sans double comptage. ; Service Reconciliation — Rapprocher résultats, montants et demande ; qualifier l’écart. ; Operations Visibility — Exposer réalisation partielle et état non résolu.
3. **Clore ou poursuivre explicitement.** Après clarification, 600 sont reconnus ; les 400 restants sont relancés ou font l’objet d’une clôture partielle autorisée. Résultat : La suite logistique dépend du résultat reconnu et des conditions applicables.
   Capacités : Payment Collection Order — Tenir le solde et la clôture autorisée. ; Process Orchestration — Coordonner la suite ou maintenir l’attente.

À vérifier : Acceptation technique, paiement et clôture sont trois faits différents. Un message tardif ou dupliqué ne doit pas créer un second résultat.

### Réexaminer une préparation après correction des données sources

Illustration FLOW fictive. Une boutique prépare une capsule de 120 robes. Commerce corrige l’assortiment, Design la variante, Finance un prix ; un Demand Plan ancien annonce encore 150 pièces.

1. **Intégrer les corrections sourcées.** Les apports sont rapprochés des références locales, de leurs identités et dates de validité. Résultat : Les changements connus gardent origine et portée.
   Capacités : Master Data Ingestion — Intégrer les apports Commerce, Finance et Design. ; Product Reference Visibility — Exposer la variante corrigée. ; Party / Role Visibility — Identifier les parties et rôles concernés. ; Agreement Visibility — Exposer les conditions applicables. ; Price Book Visibility — Exposer le prix et sa période de validité.
2. **Vérifier les possibilités de service.** La boutique consulte l’offre corrigée, les 120 robes de son assortiment, le site et les prestations disponibles. Résultat : Le changement d’assortiment ne devient pas automatiquement un changement de promesse.
   Capacités : Product Catalog Visibility — Exposer les offres éligibles. ; Assortment Visibility — Exposer l’assortiment en vigueur. ; Fulfillment Network Visibility — Exposer sites et réseau utilisables. ; Service Catalog Visibility — Exposer les prestations proposées.
3. **Traiter le décalage de plan.** L’ancien plan de 150 est distingué de la version corrigée ; l’APS reçoit le besoin de correction hors domaine et le plan reçu reste qualifié. Résultat : Le calcul local utilise une version identifiée ou explicite son incertitude.
   Capacités : Plan Ingestion — Recevoir les versions et corrections des plans externes. ; Demand Plan Visibility — Exposer la prévision et sa validité connue. ; Master Planning — Conduire le réexamen local sur les hypothèses explicites.

À vérifier : Autorité des domaines sources et source de vérité locale Supply restent distinctes. Le scénario n’impose pas de maître supplémentaire ni de correction automatique dans l’APS.

### Rééquilibrer et consolider des stocks sous protections

Illustration FLOW fictive. Un magasin conserve 80 pulls qui se vendent peu, un second risque une rupture avec 5 pièces, et deux petits sites détiennent chacun 10 pièces. Le web possède une protection explicite.

1. **Comparer cibles et protections.** Les cibles et règles sont examinées avant toute redistribution, y compris les droits réservés et le groupe web. Résultat : Les ressources mobilisables et les protections sont explicites.
   Capacités : Inventory Target Optimization — Déterminer les cibles de stock utiles. ; Group Protection Optimization — Proposer les protections de groupes. ; Reservation Policy Optimization — Évaluer les règles de réservation appropriées. ; Supply Protection Policy — Porter les règles actives de protection de ressources. ; Demand Protection Policy — Porter les règles actives de protection des demandes.
2. **Construire deux actions complémentaires.** Proposer un apport au magasin en rupture et la consolidation des petits reliquats sur un site, sous réserve des besoins protégés. Résultat : Rééquilibrage et consolidation gardent des objectifs distincts dans le même plan.
   Capacités : Stock Redistribution — Déterminer les déplacements de redistribution. ; Demand Prioritization — Prioriser les demandes concurrentes. ; Master Planning — Piloter l’arbitrage du master plan. ; Supply Assignment — Déterminer les affectations compatibles.
3. **Demander les déplacements retenus.** Les propositions autorisées deviennent des transferts avec quantités, origine, destination et date. Résultat : Les transferts suivent le même cycle malgré des motifs différents.
   Capacités : Plan Application — Appliquer le plan autorisé. ; Transfer Order — Porter les déplacements et leur reste à satisfaire.

À vérifier : Protection active et optimisation de la protection sont distinctes. Rééquilibrer ou consolider ne crée pas deux cycles de Transfer Order.

### Suivre trois issues contractuelles d’un retour fournisseur

Illustration FLOW fictive. Après contrôle, 12 vestes défectueuses sont reprises : 4 donnent lieu à avoir, 4 à remplacement, 4 à réparation, selon l’accord accepté.

1. **Qualifier les quantités et leur orientation.** Les défauts et l’accord déterminent les suites ; un retour client éventuel garde son lien avec les vestes. Résultat : Chaque groupe de quatre possède un attendu explicite.
   Capacités : Return Order — Tenir le retour client lié le cas échéant. ; Return Disposition Decision — Déterminer le devenir autorisé. ; Supplier Return Order — Porter les trois engagements fournisseur distincts.
2. **Exécuter et reconnaître les mouvements.** Les vestes sont expédiées ; l’expédition ne prouve ni avoir, ni remplacement, ni réparation. Résultat : Les mouvements sont tracés mais les engagements restent ouverts.
   Capacités : Process Orchestration — Coordonner la reprise et les prestations requises. ; Inventory Ledger — Conserver les mouvements reconnus. ; Supplier Return Order — Rapprocher les résultats des attentes contractuelles.
3. **Solder chaque attendu.** L’avoir est confirmé, trois remplacements sur quatre arrivent et les quatre réparations sont acceptées. Résultat : Un remplacement reste attendu ; le solde n’est pas masqué par les autres résultats.
   Capacités : Supplier Return Order — Tenir les soldes par engagement et leur preuve. ; Return Order — Répercuter le résultat pertinent sur le retour client lié.

À vérifier : L’avoir est exécuté hors de la tenue de Supplier Return Order. Une même quantité ne doit pas être soldée à la fois comme avoir et remplacement sans justification.

### Composer des coffrets personnalisés puis traiter les reliquats

Illustration FLOW fictive. Une campagne prévoit 40 coffrets contenant chacun un foulard et un bonnet personnalisé. Dix foulards nécessitent un nettoyage ; 60 composants arrivent en transit sans stockage durable.

1. **Préparer les composants.** Les arrivées en cross-dock et les prélèvements de stock doivent fournir les bons composants ; dix foulards attendent un nettoyage conforme. Résultat : Les composants admissibles sont identifiés avant assemblage.
   Capacités : Cross-Docking Order — Porter les exigences de transit et de correspondance entrées-sorties. ; Picking Order — Porter les prélèvements nécessaires. ; Cleaning Order — Porter le nettoyage et son résultat attendu. ; Process Orchestration — Coordonner disponibilité et dépendances.
2. **Personnaliser et assembler.** Chaque bonnet reçoit le marquage requis ; un foulard et un bonnet conformes composent chaque coffret. Résultat : 40 coffrets attendus gardent une correspondance avec leurs composants.
   Capacités : Personalization Order — Porter le marquage et ses critères d’acceptation. ; Kitting Order — Porter la composition, les quantités et la conformité du kit. ; Packing Order — Porter le conditionnement de présentation et d’expédition.
3. **Décomposer le reliquat autorisé.** La campagne s’achève avec cinq coffrets non expédiés ; leur décomposition est demandée, mais les bonnets personnalisés ne sont pas réputés interchangeables. Résultat : Les composants récupérés et leurs conditions d’utilisation sont reconnus.
   Capacités : Kitting Order — Porter le Dekitting et les composants attendus. ; Service Reconciliation — Rapprocher les résultats de prestation. ; Inventory Ledger — Enregistrer les transformations de stock reconnues. ; Inventory Visibility — Exposer les disponibilités selon l’état reconnu.

À vérifier : Repacking change le conditionnement ; Kitting/Dekitting change la composition suivie. Ni transit ni personnalisation ne justifient une duplication des quantités.

### Distinguer transfert contractuel, transit et formalité douanière

Illustration FLOW fictive. Deux lots suivent des contrats différents : 200 manteaux achetés deviennent notre propriété à un jalon contractuel avant réception ; 50 robes consignées changent de propriétaire à une échéance convenue.

1. **Identifier les conditions.** L’accord de chaque lot définit le déclencheur et les preuves attendues. Résultat : Aucun événement universel de transfert n’est supposé.
   Capacités : Agreement Visibility — Exposer les clauses pertinentes. ; Inventory Ownership Transfer Decision — Qualifier les conditions et faits nécessaires.
2. **Reconnaître le bon fait.** Le jalon du premier lot est attesté ; l’échéance du second est vérifiée. Une formalité douanière n’a d’effet sur la propriété que si son lien contractuel est établi. Résultat : Chaque transfert reconnu possède un fondement propre.
   Capacités : Inventory Ownership Transfer Decision — Déterminer le transfert pour chaque contexte. ; Customs Clearance Order — Porter la formalité et fournir son résultat pertinent. ; Inventory Ownership Ledger — Conserver les transferts reconnus et leurs preuves.
3. **Rapprocher la réception ultérieure.** Les manteaux sont reçus trois jours après leur transfert de propriété. Résultat : La réception physique n’enregistre pas un second transfert.
   Capacités : Inventory Ledger — Tracer le mouvement physique reconnu. ; Inventory Ownership Ledger — Permettre le rapprochement avec le transfert déjà reconnu. ; Inventory Visibility — Exposer séparément détention et propriété.

À vérifier : Le cas n’énonce aucune règle juridique universelle. Statut douanier, détention et propriété ne sont pas interchangeables.

### Scinder, regrouper ou fusionner sans perdre les engagements

Illustration FLOW fictive. Une vente de 100 pièces doit partir en deux fois ; deux transferts pour une ouverture voyagent ensemble ; deux achats encore modifiables de 30 et 20 pièces pourraient être fusionnés.

1. **Scinder une vente engagée.** La vente devient deux unités suivies de 60 et 40, liées à la demande initiale. Les réservations et affectations doivent rester cohérentes. Résultat : La quantité totale reste 100 et les engagements ne sont pas doublés.
   Capacités : Order Structuring — Déterminer et porter la structuration autorisée avec sa filiation. ; Sales Order — Tenir les engagements de vente. ; Reservation — Adapter les droits réservés aux identités suivies. ; Supply Assignment — Maintenir la cohérence des affectations.
2. **Regrouper les transferts.** Les deux transferts gardent leur identité mais les prestations compatibles sont réalisées ensemble. Résultat : Un regroupement logistique n’efface aucune demande.
   Capacités : Order Structuring — Porter le regroupement sans fusion d’identité. ; Transfer Order — Tenir les deux transferts et leurs soldes. ; Process Orchestration — Coordonner les prestations communes et leur rattachement.
3. **Fusionner seulement si compatible.** Les achats 30 et 20 deviennent un achat 50 si conditions et autorisations le permettent ; une prestation déjà engagée peut empêcher cette fusion. Résultat : La filiation et les engagements externes sont préservés.
   Capacités : Order Structuring — Porter la fusion autorisée et les liens d’origine. ; Purchase Order — Tenir l’engagement d’achat résultant. ; Process Orchestration — Rapprocher les prestations déjà lancées avant toute adaptation.

À vérifier : Split, group et merge ont des effets différents sur l’identité. Une opération de structure ne doit pas annuler implicitement un engagement externe.

### Libérer une préparation B2B à l’approche de sa limite d’attente

Illustration FLOW fictive. Un client attend 300 vêtements sur une palette. 280 sont prêts, 20 arrivent demain ; attendre facilite le packing mais menace le départ transport.

1. **Qualifier prestataire et exigences.** Deux prestataires annoncent des créneaux différents ; le client veut une préparation commune et une palette unique si réalisable. Résultat : Les critères de compatibilité, charge et service sont explicites.
   Capacités : Service Provider Policy — Fournir les règles de choix du prestataire. ; Service Capacity Visibility — Exposer les capacités annoncées. ; Service Requirements Decision — Déterminer les exigences de préparation et conditionnement. ; Service Selection Decision — Choisir une prestation compatible.
2. **Comparer attente et libération.** Une fenêtre de transmission groupée peut organiser la charge ; attendre les 20 peut permettre une consolidation, mais seulement jusqu’à la limite compatible avec la promesse. Résultat : Le choix de rétention ou libération est explicite et borné.
   Capacités : Service Order Release Decision — Déterminer ensemble et moment de libération. ; Picking Order — Porter l’exigence de préparation commune. ; Packing Order — Porter le résultat de conditionnement attendu.
3. **Adapter si la complétude n’arrive pas.** Les 20 sont retardés ; une solution locale est recherchée avant de réexaminer la promesse si nécessaire. Résultat : Le prestataire reçoit des ordres cohérents ; aucun retard client silencieux.
   Capacités : Process Adaptation Decision — Déterminer l’adaptation locale autorisée. ; Process Orchestration — Coordonner la libération et les prestations. ; Promise Selection Decision — Choisir une nouvelle proposition si l’engagement est menacé.

À vérifier : Transmettre ensemble ne garantit pas une préparation ni une palette communes. L’optimisation de release ne remplace pas les vagues et tâches détaillées de l’entrepôt.

### Réapprovisionner un magasin ou servir une commande identifiée

Illustration FLOW fictive. Un magasin manque de pulls : 20 sont demandés pour réalimenter son stock, tandis que 2 sont destinés à une commande client précise.

1. **Distinguer les besoins.** Le besoin de stock et celui du client sont identifiés pour éviter de compter deux fois les deux pièces engagées. Résultat : Les quantités et destinations du besoin sont explicites.
   Capacités : Replenishment — Déterminer le besoin de réapprovisionnement. ; Sales Order — Porter la demande client identifiée.
2. **Affecter et demander le transfert.** Le plan retient les ressources et autorise leur déplacement vers le magasin. Résultat : Les 22 pièces à transférer sont reliées à leurs besoins respectifs.
   Capacités : Supply Assignment — Affecter les ressources aux demandes. ; Plan Application — Appliquer le plan autorisé. ; Transfer Order — Porter le transfert et son échéance.
3. **Rapprocher le résultat.** Seules 20 pièces arrivent d’abord ; le transfert reste partiellement ouvert et l’affectation des quantités reçues ne se déduit pas de l’ordre d’arrivée. Résultat : Réception, solde du transfert et satisfaction client restent distincts.
   Capacités : Transfer Order — Tenir le reste à recevoir. ; Inventory Tracking — Capter la réception réelle. ; Supply Assignment — Maintenir les affectations explicites.

À vérifier : Le motif du transfert ne remplace pas la décision d’affectation.

### Implanter puis réalimenter un stock consigné

Illustration FLOW fictive. Un corner reçoit 100 vestes pour son ouverture. Deux semaines plus tard, 30 ventes conduisent à demander un apport complémentaire de 30, selon les besoins retenus.

1. **Déterminer le besoin initial.** Le lancement nécessite 100 vestes au corner à une date précise. Résultat : L’apport retenu est porté par une commande identifiée.
   Capacités : Replenishment — Déterminer le besoin d’apport. ; Consignment Fill-up Order — Porter l’apport initial en consignation et sa date.
2. **Recevoir sans confondre propriété.** Les 100 vestes sont reçues sous le régime prévu par l’accord. Résultat : Détention et reste à apporter sont rapprochés.
   Capacités : Consignment Fill-up Order — Rapprocher la réception du besoin initial. ; Inventory Tracking — Capter le fait de réception. ; Inventory Visibility — Exposer stock détenu et propriété connue.
3. **Réalimenter pendant l’activité.** Après les ventes, un nouveau besoin de 30 est retenu et fait l’objet d’un apport distinct. Résultat : Le même cycle d’Order traite un motif d’alimentation continue.
   Capacités : Replenishment — Déterminer le besoin complémentaire. ; Consignment Fill-up Order — Porter le nouvel apport et son solde.

À vérifier : Ouverture et alimentation continue sont deux contextes, pas deux cycles imposés.

## Traçabilité

Annexe structurée : [audit U768](../modeles/backlog/scenario-behavior-audit-U768.yaml). Apports U768/U769 ; comparaison marché CMP304 conservée. Les nouveaux récits sont fictifs et leur rédaction reste proposée ; aucune preuve de réalisation Beaumanoir.

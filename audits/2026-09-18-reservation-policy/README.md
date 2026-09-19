# Reservation Policy Decision — comportements et portée de validation

Restitution dérivée de [reservation-policy-review.yaml](../../modeles/backlog/reservation-policy-review.yaml) et du [catalogue](../../modeles/backlog/model.yaml).

**U342/U343 : capacité, quatre comportements et rattachement D05 adoptés dans la portée présentée. Les responsabilités résumées sont validées ; définitions développées, modalités, contrats et comparaisons restent éditoriaux.**

> Déterminer dans quelles situations, à quel moment et pour quelle durée réserver des ressources afin de sécuriser la promesse, selon le risque de pénurie et le coût d’indisponibilité pour les autres demandes.

Recensement des mécanismes pertinents dans le périmètre adopté et les sources consultées ; pas de prétention à toutes les politiques imaginables ni à une couverture installée.

## Pourquoi ces comportements

Le jalon du parcours, la proximité du besoin, la différenciation des engagements de service et l’adaptation au risque changent chacun la façon de sécuriser une promesse et le coût d’immobilisation. Quatre mécanismes combinables sont retenus U343 ; durées, seuils, canaux et interfaces restent des paramètres ou des contextes. La complexité visée est l’arbitrage de ces mécanismes sans retirer implicitement les garanties existantes.

| Comportement | Mécanisme | Bénéfice |
| --- | --- | --- |
| Milestone-Based Reservation Policy | Politique de déclenchement par engagement ou événement métier | Rendre cohérent ce que le client croit garanti avec le stade atteint dans la vente, tout en limitant les immobilisations prématurées. |
| Time-Fenced Reservation Policy | Mécanisme de fenêtre temporelle avant le besoin | Conserver de la flexibilité pour les demandes proches tout en organisant la sécurisation progressive des échéances futures. |
| Demand-Differentiated Reservation Policy | Politique différenciée de service | Rendre possibles des engagements commerciaux distincts sans appliquer une immobilisation maximale à toutes les demandes. |
| Risk-Adaptive Reservation Policy | Mécanisme de décision contextuelle selon le risque | Réagir aux évolutions de demande et de disponibilité en arbitrant entre perte de promesse et indisponibilité du stock pour d’autres ventes. |

## Milestone-Based Reservation Policy — BHV032

**Responsabilité adoptée U343.** À quel événement du parcours commencer à réserver et maintenir la protection.

**Définition développée, éditoriale.**

Déterminer les événements du parcours métier à partir desquels la ressource doit être réservée, puis les conditions de maintien de cette protection au fil du parcours.

**Mécanisme.** Choisir un jalon significatif : ajout au panier, demande explicite de mise de côté, soumission du paiement, acceptation de la commande ou autre engagement convenu. Définir les conditions de passage d’une protection provisoire à celle qui accompagne la commande. Un écran n’est pas le jalon métier.

**Bénéfice.** Rendre cohérent ce que le client croit garanti avec le stade atteint dans la vente, tout en limitant les immobilisations prématurées.

**Entrées.**

- États et événements du parcours
- Nature de l’engagement client
- Conditions de paiement et d’annulation
- Objectifs de service

**Résultats.**

- Jalon déclencheur
- Conditions de maintien, d’expiration et de libération
- Règle de continuité lors de la confirmation

Exemple fictif : une pièce reste vendable pendant la consultation du panier ; la soumission du paiement déclenche une réservation de dix minutes. Un paiement accepté prolonge l’engagement pour servir la commande, sans libération intermédiaire de la pièce.

**Frontières.** Choisir le jalon et les conditions ne pilote pas le parcours : les processus les mobilisent ; Reservation établit et maintient les engagements. Panier, paiement et commande sont des options de politique, pas trois comportements.

**Niveau de preuve.** Mécanismes de déclenchement directement documentés ; nom de regroupement FLOW adopté U343.

- [Microsoft — Inventory reservation policies](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities) (Documentation évolutive sans édition figée, consulté le 2026-09-18). Politiques configurées : réservation automatique à la création des lignes de commande ou manuelle ; jalon de réservation configurable en production. Limites : Pas de preuve dans ce passage d’un choix automatique du jalon de vente selon le stock et la vitesse de sortie. Texte primaire indexé consulté ; ouverture directe en erreur 503.
- [commercetools — Inventory modes and expiration](https://docs.commercetools.com/api/inventory-overview) (Documentation évolutive sans édition figée, consulté le 2026-09-18). Réservation au panier ou à la commande, mode par panier ou ligne ; durée configurable par défaut et par entrée de stock, changement de mode possible sur ligne existante. Limites : Ces leviers permettent une intégration adaptative ; ils ne prouvent pas un moteur fourni qui arbitre le jalon selon le risque de pénurie.
- [Shopify — Shopify Checkout](https://help.shopify.com/en/manual/checkout-settings) (Documentation évolutive, consulté le 2026-09-18). Stock retenu à la soumission des informations de paiement, avec libération en cas d’échec. Limites : Jalon produit spécifique, distinct de l’ouverture de page et de l’encaissement effectif ; aucun déclencheur FLOW imposé.

## Time-Fenced Reservation Policy — BHV033

**Responsabilité adoptée U343.** À quelle distance de la date de besoin commencer à réserver.

**Définition développée, éditoriale.**

Déterminer à quelle distance de la date de besoin commencer à réserver, afin de sécuriser l’échéance sans immobiliser trop tôt les ressources.

**Mécanisme.** Définir une fenêtre de réservation relative à la date de besoin ou d’expédition. Une demande déjà acceptée peut rester hors de cette fenêtre ; l’entrée dans la fenêtre déclenche une nouvelle appréciation selon les conditions applicables. Distinguer cet horizon du délai d’expiration d’une réservation déjà accordée.

**Bénéfice.** Conserver de la flexibilité pour les demandes proches tout en organisant la sécurisation progressive des échéances futures.

**Entrées.**

- Date de besoin ou d’expédition
- Délais de préparation
- Engagements déjà pris
- Disponibilité présente et future admissible

**Résultats.**

- Fenêtre avant le besoin
- Conditions de réexamen à l’entrée dans la fenêtre
- Traitement d’un changement d’échéance

Exemple fictif : pour une livraison dans trente jours, décider de commencer la réservation à J-7. Cela ne signifie ni ignorer la demande dans l’ATP avant J-7, ni autoriser une promesse sans ressources crédibles.

**Frontières.** La date réalisable reste du ressort des décisions de promesse ; ce comportement choisit quand sécuriser les ressources par réservation. Il ne programme pas les opérations logistiques et ne recalcule pas la promesse.

**Niveau de preuve.** Reservation Time Fence est un terme et un mécanisme explicites chez Oracle EBS.

- [Oracle — Reservation Time Fence](https://docs.oracle.com/cd/E26401_01/doc.122/e48842/T373258T377249.htm) (12.2, consulté le 2026-09-18). Une fenêtre avant la date planifiée conditionne la réservation automatique. Le programme Reserve Orders peut reprendre les lignes concernées. Limites : Référence EBS, pas Fusion Cloud. Les modes Fair Share/Percentage/Partial du même chapitre mêlent arbitrage des quantités et réservation ; FLOW conserve leurs frontières. Texte primaire ouvert.

## Demand-Differentiated Reservation Policy — BHV034

**Responsabilité adoptée U343.** Quelles conditions appliquer selon les engagements de service.

**Définition développée, éditoriale.**

Déterminer des conditions de réservation différentes selon les engagements de service attachés aux demandes, aux clients ou aux canaux, en respectant les priorités et droits d’usage établis.

**Mécanisme.** Distinguer des régimes de réservation lorsque les conditions de service le justifient : mise de côté convenue pour un client professionnel, protection au paiement pour une vente en ligne, réservation dès acceptation d’une demande urgente. La différence doit modifier la garantie ou le processus ; un simple filtre client ne suffit pas.

**Bénéfice.** Rendre possibles des engagements commerciaux distincts sans appliquer une immobilisation maximale à toutes les demandes.

**Entrées.**

- Conditions commerciales et de service
- Typologie du besoin
- Priorités déjà décidées
- Droits et protections applicables

**Résultats.**

- Régimes par contexte de demande
- Jalons et durées différenciés
- Conditions explicites de dérogation

Exemple fictif : un accord professionnel prévoit une mise de côté dès acceptation pendant quarante-huit heures, tandis que la vente web standard réserve au paiement. Ces durées illustrent des engagements différents et ne constituent pas des règles Beaumanoir constatées.

**Frontières.** Order Prioritization garde le classement des Orders ; Group Protection Decision garde les enveloppes des groupes. Ce comportement ne choisit ni les commandes gagnantes ni les quantités affectées : il décide du régime de réservation applicable à la demande.

**Niveau de preuve.** Besoins de réservation différenciés attestés ; leur regroupement comme comportement décisionnel est une interprétation FLOW.

- [Microsoft — Inventory reservation policies](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities) (Documentation évolutive sans édition figée, consulté le 2026-09-18). Politiques configurées : réservation automatique à la création des lignes de commande ou manuelle ; jalon de réservation configurable en production. Limites : Pas de preuve dans ce passage d’un choix automatique du jalon de vente selon le stock et la vitesse de sortie. Texte primaire indexé consulté ; ouverture directe en erreur 503.
- [IBM — Handling inventory reservation](https://www.ibm.com/docs/en/order-management?topic=2-handling-inventory-reservation) (Documentation évolutive, consulté le 2026-09-18). La réservation peut servir des clients prioritaires ou un ordre premier arrivé, premier servi. Limites : Appui à des politiques différenciées ; ne prouve pas une optimisation automatique de la durée par catégorie. Texte primaire indexé consulté.

## Risk-Adaptive Reservation Policy — BHV035

**Responsabilité adoptée U343.** Comment adapter le déclenchement et la durée selon la tension et le risque d’immobilisation inutile.

**Définition développée, éditoriale.**

Adapter les conditions de déclenchement et de durée de réservation à la tension sur les ressources et au risque d’immobilisation inutile, dans les limites des engagements déjà accordés.

**Mécanisme.** Appliquer des règles conditionnelles, réestimer les paramètres ou sélectionner une politique selon la situation. Examiner les stocks libres, les engagements concurrents, leur vitesse et variabilité, les entrées attendues et leur fiabilité. La probabilité de conversion et les abandons peuvent éclairer le coût d’une réservation précoce. Une politique conditionnelle peut être définie à l’avance ; adaptation ne signifie ni apprentissage obligatoire ni réécriture permanente des règles.

**Bénéfice.** Réagir aux évolutions de demande et de disponibilité en arbitrant entre perte de promesse et indisponibilité du stock pour d’autres ventes.

**Entrées.**

- Disponibilité après engagements et protections
- Vitesse des demandes et réservations concurrentes
- Fiabilité des entrées et du stock
- Durée du parcours et conversion, si connues
- Objectifs et limites de service

**Résultats.**

- Politique sélectionnée ou paramètres recommandés
- Motif métier du choix et horizon de validité
- Conditions de réexamen et solution de repli si les informations sont insuffisantes

Exemple fictif : une capsule dispose de huit pièces alors que les demandes s’accélèrent. Pour sécuriser le paiement, proposer une protection plus précoce et courte ; si les paniers sont surtout abandonnés, retenir au contraire une protection plus tardive. Le risque de pénurie seul ne détermine pas le sens de l’adaptation.

**Frontières.** Ne pas déduire deux fois les mêmes engagements ; ne pas assimiler sorties physiques et demandes nouvelles. ATP reste fournisseur de possibilités, PTP de l’arbitrage économique de satisfaction des Orders. Une révision de politique ne révoque pas implicitement les réservations existantes ; leurs modifications suivent les conditions accordées.

**Niveau de preuve.** Leviers commercetools et adaptations voisines IBM/SAP ; aucun moteur standard de sélection du jalon par risque démontré. Mécanisme FLOW issu de U341 et adopté U343, sans revendication d’innovation exclusive.

- [commercetools — Inventory modes and expiration](https://docs.commercetools.com/api/inventory-overview) (Documentation évolutive sans édition figée, consulté le 2026-09-18). Réservation au panier ou à la commande, mode par panier ou ligne ; durée configurable par défaut et par entrée de stock, changement de mode possible sur ligne existante. Limites : Ces leviers permettent une intégration adaptative ; ils ne prouvent pas un moteur fourni qui arbitre le jalon selon le risque de pénurie.
- [IBM — Rules-based safety stock](https://www.ibm.com/docs/en/sip?topic=stock-rules-based-safety) (Documentation évolutive sans édition figée, consulté le 2026-09-18). Règles de stock de sécurité évaluées en temps réel ; valeurs fixes ou pourcentage au niveau réseau, validité temporelle et critères de contexte. Limites : Mécanisme voisin de protection des quantités vendables, pas décision du jalon de réservation pour un client. Texte primaire indexé consulté ; ouverture directe indisponible.
- [SAP — Availability Change Log Events in Backorder Processing](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/62d58baf16434bf1a6ad16e55e4cd0f4.html) (2608, consulté le 2026-09-18). BOP réévalue la disponibilité et le réalisme des confirmations lorsque la situation de demande ou d’offre change. Limites : Révision des confirmations, pas preuve d’une adaptation du jalon de réservation panier/paiement. Texte primaire indexé consulté ; page ouverte sans texte exploitable.

## Combiner les mécanismes

Un régime professionnel différencié peut réserver à l’acceptation, seulement dans une fenêtre de sept jours avant le besoin, avec une durée adaptée au risque. Ces mécanismes se combinent ; ni niveaux de maturité ni séquence obligatoire.

Les paramètres communs précisent bénéficiaire, contexte, déclencheur, horizon avant le besoin, validité après réservation, maintien, libération et réexamen. Une recommandation doit être mise en vigueur par le management responsable avant application. Les engagements déjà accordés gardent leurs conditions.

## Recensement des variantes et limites du découpage

Chaque ligne indique où documenter le cas ; les lignes ne sont pas des comportements supplémentaires.

| Cas examiné | Traitement retenu | Justification et frontière |
| --- | --- | --- |
| Panier, paiement, commande, demande explicite de mise de côté | BHV032 | Options de jalon métier ; aucun comportement par écran. |
| Réservation progressive au fil des engagements | BHV032 | Conditions de continuité dans le même mécanisme ; ne pas créer une fonction de conversion de statut comme comportement. |
| Réservation à l’approche de la date de besoin | BHV033 | Fenêtre avant le besoin distincte de l’expiration après réservation. |
| Clients, canaux, types de besoin ou engagements contractuels | BHV034 | Justifié seulement si la garantie ou le processus diffère ; un simple filtre ne suffit pas. |
| Stock faible, pic de demande, accélération des engagements | BHV035 | Signaux d’une même décision de risque, pas trois comportements. |
| Entrée fournisseur incertaine, stock peu fiable, retards | BHV035 | Autres facteurs de risque ; utiliser les constats et estimations disponibles sans absorber le tracking. |
| Probabilité de conversion, abandon, durée du parcours | BHV035 | Hypothèse décisionnelle FLOW ; aucun moteur standard attesté. Pas de scoring obligatoire ni nouveau comportement par indicateur. |
| Durée fixe, expiration événementielle, prolongation conditionnelle | Paramètres communs | Le mécanisme choisit les conditions ; Reservation réalise maintien et libération. Une durée chiffrée ne justifie pas un comportement. |
| Manuel, règles déterministes, optimisation, IA | Modes de réalisation | Ne différencient pas à eux seuls le résultat métier ni la capacité. |
| Politique structurelle versus décision contextuelle | Modalités combinables | Une règle conditionnelle fixée à l’avance peut produire une décision adaptée au contexte. |
| Réservation partielle, complète ou coordonnée d’un ensemble | Candidat de frontière à instruire | Effet métier possible sur les ensembles indissociables. Oracle et IBM documentent des modalités partielles ; le choix quantitatif ou la cohérence de promesse peut relever de D03. Pas ajouté à la capacité sans élargissement explicite de son résultat. |
| Réseau versus site, quantité générique versus lot ou unité | Reservation / Supply Assignment | Portée de l’engagement et affectation des ressources ; ne pas confondre avec choix du moment de réservation. IBM réseau décompose déjà en sites. |
| Stock actuel versus ressources futures | ATP / Reservation | Admissibilité et portée de l’engagement ; conserver les comportements ATP déjà adoptés. |
| FIFO/FEFO, priorité, partage équitable, pourcentage entre Orders | D03 / Supply Assignment | Choix des ressources ou des bénéficiaires ; les modes éditeurs ne sont pas recopiés dans la décision de politique temporelle. |
| Reprise d’une réservation au profit d’une autre demande | Arbitrage des engagements existants | Ne pas présenter la préemption comme un simple paramètre adaptatif. Conditions de révision, Promise Management et processus de compensation à mobiliser selon le cas. |
| Enveloppes par groupe et stock tampon | Supply Protection / décisions D05 existantes | Protection préalable des usages, distincte d’un engagement de réservation au bénéfice d’un besoin. |
| Créer, modifier, libérer, prolonger, rechercher | Fonctions de Reservation | Opérations produit à documenter dans les descriptions, pas comportements de décision. |
| Tester plusieurs politiques et mesurer leurs effets | Inventory Planning | Simulation & analyse reste le comportement de Planning ; mobilise cette décision sans duplication. |
| Vente sans réservation, backorder ou survente autorisée | Option et frontière | La décision peut conclure à différer ou ne pas réserver avant un jalon. Autoriser une vente sans ressource et modifier la promesse ne sont pas des pouvoirs implicites de cette capacité. |

## Rattachement et relations

**Parent adopté U343 : D05 Inventory Optimization.** Compromis disponibilité, immobilisation et risque ; le choix de politique reste distinct de la satisfaction des Orders D03.

| Consommateur | A besoin de | Sens proposé |
| --- | --- | --- |
| Reservation Policy Decision | Inventory Visibility | A besoin des quantités, états, engagements connus et de leur fraîcheur pour apprécier la tension sans double compte. |
| Reservation Policy Decision | Available-to-Promise (ATP) | A besoin des possibilités de disponibilité présentes et futures dans le contexte, sans recalculer l’ATP. |
| Reservation Policy Decision | Order Prioritization | A besoin des priorités décidées lorsque les régimes de réservation sont différenciés ; ne reclasse pas les Orders. |
| Reservation Policy Decision | Supply Protection | A besoin des droits et restrictions actifs qui encadrent les réservations possibles. |
| Reservation Policy Decision | Agreement Ingestion | A besoin des conditions de service disponibles dans la projection des Agreements lorsqu’elles encadrent les régimes de réservation. |
| Reservation | Reservation Policy Decision | A besoin des conditions de réservation retenues et mises en vigueur par le management responsable pour établir et maintenir les engagements ; une recommandation non activée ne s’applique pas implicitement. |
| Inventory Planning | Reservation Policy Decision | A besoin des politiques de réservation alternatives et de leurs effets pour les scénarios où cet arbitrage modifie disponibilité, immobilisation et risque. |

## Arbitrages ouverts

- Arbitrer le porteur de gouvernance et de mise en vigueur des politiques.
- Qualifier les réservations coordonnées/partielles avant tout élargissement de la capacité.
- Instruire les descriptions détaillées et contrats sans confondre la validation des comportements avec celle de toutes les modalités.

Aucun changement d’une publication ; l’Atlas continuera à présenter la release courante jusqu’à une nouvelle publication demandée.

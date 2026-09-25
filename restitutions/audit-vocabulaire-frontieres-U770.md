# Audit du vocabulaire, des définitions, du marché et des frontières — U770

## Conclusion

Le découpage principal est défendable. Les risques les plus nets viennent du décalage entre glossaire, définitions révisées, portées cumulatives et commentaires marché. Corriger ces contradictions avant une nouvelle refonte.

**Les 22 recommandations sont appliquées au backlog sous délégation U771.** Le détail des modifications et des qualifications préservées figure dans [l’annexe canonique](../modeles/backlog/vocabulary-boundary-audit-U770.yaml). La publication Atlas reste distincte.

L’application corrige les définitions PTP/CTP et les renvois périmés, clarifie les responsabilités de sélection, d’affectation, d’intégration et de visibilité, et harmonise la graphie Fulfilment. Supply Plan, Demand Plan et Matching Master Plan sont distingués dans le glossaire. Les arguments marché circulaires ou manquants ont été remplacés par les rapprochements et limites déjà documentés ; cela ne constitue pas une revalidation exhaustive des sources.

**Receiving Order** complète les familles de services : demande et engagements de réception confiée, résultat et écarts. Un scénario de réception partielle relie les commandes, l’orchestration, l’inspection et les faits de stock. Le backlog comporte désormais **72 capacités et 23 scénarios structurés**. Deux documents Microsoft étayent ce choix local sans établir un consensus de vocabulaire.

Les constats ci-dessous décrivent l’état audité avant correction et conservent les motifs de l’intervention. Ils ne constituent pas une seconde backlog.

## Périmètre initial et limites

164 fiches métier (71 capacités, 75 comportements, 9 sous-domaines, 8 références et 1 domaine), 121 termes ; 404 comparaisons représentant 218 URL distinctes.
Les définitions et les structures ont été parcourues ; les portées et sources ont été approfondies sur les points signalés. Dix documents primaires ont été relus. Il ne s’agit pas d’une revalidation exhaustive des 218 documents externes. L’annexe indique la profondeur de lecture par fiche.

## Constats initiaux et recommandations appliquées

### F01 — PTP choisit dans le glossaire mais évalue dans la capacité (P1)

**Nature :** demonstrated_inconsistency. **Fiches :** TER068, D03.k, D03.l.

**Constat :** TER068.definition et short_description : « Comparer et sélectionner les scénarios de promesse ». D03.k.definition : « sans sélectionner la réponse ».

**Risque :** L’infobulle et la fiche attribuent le choix à deux responsables différents.

**Recommandation :** Aligner définition et résumé de TER068 sur l’évaluation économique locale ; réserver la sélection à Promise Selection Decision. Conserver séparément le sens natif Oracle, qui combine évaluation et choix.

**Critère de clôture :** Aucune définition FLOW de PTP ne lui attribue une sélection ; le recouvrement partiel Oracle reste explicite.

### F02 — Le glossaire CTP conserve l’ancien périmètre d’adaptation (P1)

**Nature :** demonstrated_inconsistency. **Fiches :** TER045, D03.j, BHV075, BHV076.

**Constat :** TER045.definition : adaptation « des ressources ou des engagements » et mobilisation des décisions spécialisées. D03.j.scope exclut création d’achat, affectation, engagement et adaptation décidée.

**Risque :** CTP peut être lu comme une capacité d’arbitrage et de révision concurrente du Matching et du Fulfilment.

**Recommandation :** Réécrire définition, résumé et contexte de TER045 selon la faisabilité conditionnelle et les deux profondeurs adoptées. Isoler le repère U251 dans l’historique.

**Critère de clôture :** Glossaire, capacité et comportements distinguent tous évaluation, décision de mobilisation et application.

### F03 — Master Planning situe encore Promising dans Inventory (P1)

**Nature :** demonstrated_inconsistency. **Fiches :** D05.f, subdomain-order-promising, D01.

**Constat :** D05.f.scope : « ATP/CTP/PTP et le réexamen de promesse restent dans Inventory ». D01.scope les place dans Order Promising ; rattachements explicites conformes à ce dernier.

**Risque :** La lecture de Master Planning contredit l’arbre publié.

**Recommandation :** Corriger le renvoi textuel vers Order Promising ; conserver les rattachements actuels.

**Critère de clôture :** Aucun texte courant ne localise ces quatre capacités dans Inventory Management.

### F04 — Plan Application conserve des noms et autorités devenus obsolètes (P1)

**Nature :** demonstrated_inconsistency. **Fiches :** D02.e, D03.o, D05.h.

**Constat :** D02.e.scope : « Demand, Inventory et Master Data conservent commandes, engagements, réservations et politiques ». Même scope : « Le mécanisme d’affectation conserve son sens métier Supply Assignment : matérialiser et maintenir les liens ». La fin de la fiche distingue correctement Supply Assignment qui choisit et Plan Application qui matérialise.

**Risque :** Deux sens de Supply Assignment et une autorité des politiques mal localisée subsistent dans la même fiche.

**Recommandation :** Conserver une seule frontière : Supply Assignment détermine, Plan Application fait appliquer et vérifie la prise en compte ; Orders, Inventory et Policies possèdent leurs actes. Employer les noms canoniques au lieu des anciens périmètres.

**Critère de clôture :** Le texte n’attribue plus aux deux capacités la même décision ni les politiques à Master Data.

### F05 — Replenishment inclut et exclut simultanément le lancement (P1)

**Nature :** demonstrated_inconsistency. **Fiches :** D05.e, TER074, TER079, TER080.

**Constat :** D05.e.definition : « apports initiaux et successifs ». Début du scope : « après la constitution du stock de départ ». Plus loin : « Replenishment conserve les apports de lancement ». TER074 désigne encore Demand & Supply Optimization.

**Risque :** La responsabilité des apports initiaux reste incertaine malgré leur intégration.

**Recommandation :** Décrire l’ensemble des apports dès le début ; conserver Réassort comme cas d’alimentation continue et Implantation comme contexte initial. Actualiser TER074 vers Matching.

**Critère de clôture :** Aucune exclusion du lancement dans la portée de Replenishment ; termes français explicitement plus étroits.

### F06 — Le glossaire Catalog porte encore les prix sans distinguer Price Book (P1)

**Nature :** demonstrated_inconsistency. **Fiches :** TER049, D12.b, price-book-visibility, TER097, master-data-ingestion.

**Constat :** TER049.definition attribue les prix au Product Catalog. D12.b.scope sépare les tarifs dans Price Book Visibility. master-data-ingestion.scope conserve un ancien paragraphe catalogue/produits/prix.

**Risque :** Offre et tarification de référence risquent de devenir deux sources concurrentes.

**Recommandation :** Préciser que le catalogue décrit les offres et leur éligibilité, avec des liens tarifaires possibles ; Price Book porte les tarifs. Une association n’impose ni duplication ni catalogue unique par tarif.

**Critère de clôture :** Les trois fiches et le glossaire donnent la même distinction offre, tarif, prix contextualisé.

### F07 — Transfer Order reste limité au rééquilibrage dans le glossaire (P2)

**Nature :** demonstrated_inconsistency. **Fiches :** TER071, D04.k.

**Constat :** TER071.definition : déplacement « pour rééquilibrer leur répartition ». D04.k et ses scénarios couvrent aussi implantation, réassort, consolidation et commande identifiée.

**Risque :** Le glossaire réduit abusivement le périmètre de la capacité.

**Recommandation :** Définir le déplacement demandé entre sites ; donner le rééquilibrage comme exemple parmi les finalités, sans réintroduire les comportements retirés.

**Critère de clôture :** Les cinq motifs conservés dans les scénarios sont compatibles avec la définition générale.

### F08 — Orchestration conserve l’ancien partage Tracking / Visibility (P1)

**Nature :** demonstrated_inconsistency. **Fiches :** D06.d, D07.c, D07.d, operations-visibility, BHV082.

**Constat :** D06.d.scope : Operations Tracking « rend visibles » et mentionne Process Tracking. D07.c.scope : « Le tracking rend visible l’avancement ». D07.d intègre les faits ; Operations Visibility expose les résultats et porte Process Visibility.

**Risque :** Le lecteur peut reconstruire une capacité de suivi retirée ou attribuer la restitution à Integration.

**Recommandation :** Remplacer les formulations historiques par captation/intégration, rapprochement et restitution ; désigner Process Visibility comme perspective de Operations Visibility.

**Critère de clôture :** Aucune capacité Process Tracking implicite ; les liens et le texte suivent le partage courant.

### F09 — Attribution erronée du terme Consignment Fill-up à Microsoft (P1)

**Nature :** demonstrated_inconsistency. **Fiches :** D04.r, TER091.

**Constat :** D04.r.scope : « Microsoft emploie Consignment Fill-up Order ». Deux documents Microsoft consultés utilisent Consignment replenishment order pour l’apport entrant.

**Risque :** La justification du nom donne une fausse convergence lexicale interéditeurs.

**Recommandation :** Conserver le choix FLOW/SAP Fill-up si souhaité, mais corriger l’attribution Microsoft et expliciter la perspective fournisseur entrant documentée.

**Critère de clôture :** Libellé natif, perspective et adaptation FLOW sont distingués sans prétendre à un nom Microsoft Fill-up.

### F10 — Commentaires marché en retard sur les types et responsabilités (P1)

**Nature :** demonstrated_inconsistency. **Fiches :** D03.k, D08.e, D14.b.

**Constat :** Deux comparaisons D03.k parlent encore d’« évaluation économique Knowledge ». D08.e et D14.b limitent FLOW à la consultation alors que les définitions incluent construction et rafraîchissement de la vue locale.

**Risque :** La partie marché contredit la partie métier et minore l’autorité locale de la connaissance.

**Recommandation :** Actualiser la position FLOW en Evaluation pour PTP ; préciser pour Visibility la composition et maintenance de la vue locale sans maîtrise d’entreprise externe.

**Critère de clôture :** Les commentaires ne réintroduisent ni ancien type ni projection passive.

### F11 — Des comparaisons CTP héritées soutiennent surtout des fonctions voisines (P2)

**Nature :** evidence_quality. **Fiches :** D03.j, BHV075, BHV076.

**Constat :** D03.j conserve ABC (autres sites/produits) et BOP (réexamen des confirmations). D03.j.scope précise qu’une simple alternative de stock/site/produit n’est pas automatiquement du CTP. Microsoft présente principalement CTP par la prise en compte des matières et capacités.

**Risque :** Le nombre de références peut donner l’impression que ces pages prouvent les deux profondeurs FLOW.

**Recommandation :** Conserver ABC/BOP comme appuis adjacents ou renvoyer aux bonnes fiches ; faire des sources de faisabilité les appuis directs. Présenter Supply-Based / Capacity-Constrained comme structuration FLOW argumentée, pas nomenclature Microsoft.

**Critère de clôture :** Chaque comparaison indique le résultat précis soutenu et ce qu’elle ne démontre pas.

### F12 — Le volume documentaire ne constitue pas une justification par fiche (P2)

**Nature :** evidence_quality. **Fiches :** D02.e, D05.f.

**Constat :** 164 fiches possèdent au moins deux URL distinctes, mais cela ne vérifie pas la pertinence des passages. 141 definition_choice reproduisent exactement la définition de la fiche ; 252 comparaisons ne renseignent pas ce champ. Master Planning contient deux URL répétées ; Plan Application porte 21 comparaisons de mailles diverses.

**Risque :** Accumulation et textes génériques rendent difficiles la lecture du choix de nom et la preuve du périmètre.

**Recommandation :** Hiérarchiser deux appuis directs par fiche, conserver les sources adjacentes avec leur rôle, dédupliquer les répétitions et remplacer les justifications circulaires par un raisonnement. L’absence d’un champ ne prouve pas à elle seule l’absence d’argument dans les autres champs.

**Critère de clôture :** Deux passages pertinents et un argument propre au nom/périmètre sont identifiables ; aucun consensus déduit du seul nombre de liens.

### F13 — Supply Plan et master plan sont des sens FLOW à rendre plus explicites (P2)

**Nature :** intentional_difference. **Fiches :** plans-visibility, subdomain-plans, D05.f, TER078.

**Constat :** FLOW limite Supply Plan aux mouvements prévus hors achats et réserve le master plan au Matching. Microsoft traite des supply forecasts conduisant notamment à des achats planifiés ; ses master plans englobent plusieurs calculs. Le glossaire ne possède pas d’entrée distincte Supply Plan ni Demand Plan.

**Risque :** Un lecteur du marché peut supposer un périmètre plus large ou confondre le plan externe avec le plan interne.

**Recommandation :** Conserver le découpage validé ; ajouter au glossaire les sens FLOW de Supply Plan, Demand Plan et master plan de matching, avec différences explicites et exemple d’achat projeté. Ne pas renommer automatiquement.

**Critère de clôture :** Un achat projeté APS, un mouvement prévu hors achats et une affectation interne sont distinguables.

### F14 — Sélection de promesse, de service et adaptation locale : expliciter les décisions (P2)

**Nature :** clarification. **Fiches :** D03.l, D06.e, D06.f, service-order-release-decision, D03.o.

**Constat :** Promise Selection choisit une proposition ; Service Selection choisit les moyens ; Process Adaptation choisit les adaptations ; Release choisit ensembles et moments. D06.e.scope renvoie encore aux possibilités de promesse D18, identifiant absent du modèle courant.

**Risque :** Sur une alternative express ou autre site, plusieurs capacités peuvent sembler choisir la même solution.

**Recommandation :** Conserver les capacités ; expliciter leurs sorties et coopérations : option de promesse, prestation/exécutant, révision locale du plan, décision de libération, affectation collective. Corriger D18. Aucune chaîne universelle ni nouvelle règle d’autorité nécessaire.

**Critère de clôture :** Le scénario transport retardé identifie une seule responsabilité par décision et le recours à Promising/Matching si leurs engagements sont touchés.

### F15 — Service Reconciliation et encaissement : distinguer résultat et comptabilité (P2)

**Nature :** clarification. **Fiches :** D07.c, service-order-payment-collection.

**Constat :** D07.c.scope : « aucun rapprochement financier ». Le scénario remote-payment-ambiguous lui fait rapprocher 600 reçus sur 1 000 demandés, doublons et contradiction. Payment Collection exclut l’absorption automatique du rapprochement financier.

**Risque :** L’exclusion générale peut interdire le rapprochement du résultat de la prestation que le scénario demande pourtant.

**Recommandation :** Distinguer rapprochement opérationnel demande/résultat de collecte et rapprochement bancaire/comptable restant externe. La preuve financière est fournie par le service compétent ; Service Reconciliation qualifie le résultat reçu.

**Critère de clôture :** Le cas partiel est traitable sans que FLOW certifie les écritures, le règlement bancaire ou l’affectation comptable.

### F16 — Réception : responsabilité annoncée mais aucune famille spécialisée (P2)

**Nature :** open_modeling_choice. **Fiches :** subdomain-service-orders, D07.a, D07.c.

**Constat :** Le scope de Service Order Management conserve explicitement les prestations de réception sans famille spécialisée. Les 16 familles d’Orders actuelles ne comportent pas de Receiving Order. Microsoft distingue demandes entrantes d’entrepôt et retours de réception ; cela atteste un objet de prestation, pas une capacité FLOW obligatoire.

**Risque :** Un cas de réception confiée ne peut pas pointer une capacité d’Order explicite ; les 71 capacités mobilisées ne prouvent donc pas que toutes les responsabilités annoncées sont couvertes.

**Recommandation :** Arbitrer Receiving Order si la réception est une prestation autonome commandée et suivie ; sinon documenter sa prise en charge exacte par une famille existante. Ne pas créer un ordre par fait reçu ni automatiquement Putaway/Storage Orders.

**Critère de clôture :** Un scénario de réception confiée désigne la capacité qui porte demande, engagement et reste à satisfaire.

### F17 — Ingestion des référentiels et maintien des vues : préciser la remise de responsabilité (P2)

**Nature :** clarification. **Fiches :** master-data-ingestion, D08.e, D09.e, D11.b, D12.b, D13.b, D14.b, D16.b, price-book-visibility.

**Constat :** Master Data Ingestion intègre les apports et maintient les références locales. Les sept Visibility historiques construisent et rafraîchissent leurs vues ; Price Book Visibility décrit surtout la consultation. Le scope Ingestion accumule les anciennes descriptions par référentiel et répète les mêmes frontières.

**Risque :** Deux capacités peuvent être comprises comme responsables de la même correction ou de la même fraîcheur.

**Recommandation :** Préciser sans ajouter de capacité : ingestion reconnaît et intègre les apports sourcés ; la connaissance compose et expose la référence locale utilisable, sa validité et ses incohérences. Harmoniser Price Book et condenser le texte sans perdre les huit sujets.

**Critère de clôture :** Le scénario de correction d’un prix permet d’identifier prise en compte du fait, version locale exposée et utilisation aval.

### F18 — Des définitions trop courtes ne rendent pas le service concret (P2)

**Nature :** editorial_precision. **Fiches :** D07.a, D06.d, BHV079, BHV080, BHV081.

**Constat :** D07.a : « Déterminer les prestations nécessaires ». D06.d : « Coordonner les prestations et leurs dépendances ». BHV079–081 listent surtout des opérations ou lieux.

**Risque :** Le lecteur doit lire toute la portée pour comprendre entrée, résultat et frontière.

**Recommandation :** Faire commencer la définition par le résultat rendu : exigences de service établies, progression coordonnée jusqu’au résultat, état d’avancement restitué. Garder les détails et exemples dans la portée.

**Critère de clôture :** Chaque définition seule permet de comprendre ce qui est produit sans absorber décision voisine ou exécution physique.

### F19 — Convention lexicale et références de travail à harmoniser (P3)

**Nature :** editorial_precision. **Fiches :** D06, D13, D13.b, D07.a, service-order-inspection, service-order-transport-booking, service-order-payment-collection.

**Constat :** Fulfilment Orchestration coexiste avec Fulfillment Network et Fulfillment Cost Evaluation. Inspection Order : « demandes de inspection ». Des fiches conservent « Recommander une capacité distincte » ou « nom provisoire » ; Payment Collection porte une ambiguïté déjà reconnue.

**Risque :** Des écarts de style et de maturité sont perçus comme des différences métier.

**Recommandation :** Choisir une convention orthographique FLOW en préservant les intitulés natifs cités ; corriger la grammaire. Séparer description cible, conditions d’applicabilité et réserves internes. Ne pas ajouter Decision/Management partout ni renommer un terme validé sur préférence seule.

**Critère de clôture :** Même sens, même graphie hors citations ; descriptions compréhensibles sans historique de la conversation.

### F20 — Le glossaire garde des sens historiques ou trop généraux (P2)

**Nature :** demonstrated_inconsistency. **Fiches :** TER056, TER065, TER030, VER019, VER002.

**Constat :** TER056 présente encore Inventory Ledger Management comme candidat non adopté, au milieu de la définition du registre. TER030.context décrit Purpose alors que la hiérarchie utilise Subdomain. VER019 limite Libérer à la levée d’une restriction, alors que Service Order Release autorise le lancement. Supply Order est un terme local générique ; Oracle distingue supply order et sales order.

**Risque :** Les infobulles réintroduisent des concepts remplacés ou confondent deux sens de release.

**Recommandation :** Séparer sens courant et historique ; qualifier Libérer une ressource / Libérer un ordre pour exécution. Pour Supply Order, marquer le sens local et le distinguer du document Oracle ; conserver les identifiants historiques et renvois méthodologiques.

**Critère de clôture :** La lecture métier ne présente ni Purpose comme niveau courant ni un seul sens ambigu de release.

### F21 — Protection de ressources et protection de demandes : deux axes à conserver (P2)

**Nature :** clarification. **Fiches :** D02.b, D19.b, D05.d, D03.m.

**Constat :** Supply Protection porte enveloppes, plafonds et règles sur ressources ; Demand Protection porte éligibilité, priorité et protection contre réoptimisation. Un même groupe web peut apparaître des deux côtés.

**Risque :** La même condition pourrait être saisie deux fois et diverger si son objet protégé n’est pas explicite.

**Recommandation :** Garder les deux capacités : déclarer pour chaque règle si elle contraint la ressource mobilisable ou le traitement d’une demande. Les optimisations proposent, les Policy activent, les décisions consomment. Référencer la même règle lorsque nécessaire plutôt que la dupliquer.

**Critère de clôture :** Le cas stock protégé pour le web distingue enveloppe ressource, demande prioritaire et réservation individuelle.

### F22 — Noms d’Orders de services et PTP : conserver les adaptations FLOW explicites (P2)

**Nature :** intentional_difference. **Fiches :** subdomain-service-orders, D03.k, service-order-document-production, service-order-billing, service-order-payment-collection.

**Constat :** Les fiches d’Orders fashion indiquent correctement que les prestataires documentent des opérations, pas une taxonomie normalisée d’Orders. Oracle PTP sélectionne une possibilité de moindre coût ; FLOW sépare l’évaluation de la sélection. Microsoft DOM optimise également les sources ; il n’est pas une capacité native nommée PTP.

**Risque :** Une simplification des commentaires pourrait transformer une analogie pertinente en équivalence de marché non démontrée.

**Recommandation :** Préserver ces écarts volontaires ; présenter les noms composés comme FLOW et la correspondance comme appui sémantique ou recouvrement partiel. Aucun renommage automatique ni fusion pour coller à un produit.

**Critère de clôture :** Les fiches distinguent toujours choix FLOW, terme natif et résultat réellement étayé.

## Coopérations à conserver

| Frontière | Diagnostic | Lecture recommandée |
| --- | --- | --- |
| Inventory Tracking / Ledger / Visibility | Coopération saine | Recevoir les faits ; tenir les écritures reconnues ; composer les positions. Ne pas fusionner intégration, registre et consultation. |
| Inventory Visibility / ATP | Coopération saine | La vue décrit les ressources et engagements ; ATP évalue leur admissibilité pour une demande. Le stock projeté ne vaut pas une promesse. |
| ATP / CTP | Frontière définie, glossaire à corriger | Ressources admissibles de référence / faisabilité conditionnelle de ressources à obtenir ou constituer. Une autre date ou un autre site ne suffit pas à caractériser CTP. |
| PTP / Promise Selection | Frontière définie, glossaire contradictoire | Dossier économique local / proposition choisie. Pas de fusion. |
| Supply Assignment / Plan Application | Frontière définie, prose résiduelle ambiguë | Déterminer les liens / matérialiser les changements autorisés et recueillir leur résultat. |
| Purchase Order de service / Service Order | Coopération saine | Engagement d’achat envers le fournisseur / exigences et engagement de la prestation confiée. Pas de rapport un-à-un obligatoire. |
| Transfer Order / Transport Order | Coopération saine | Besoin de déplacement entre sites / prestation d’acheminement confiée ; un transfert peut mobiliser plusieurs prestations. |
| Transport Booking / Reservation | Coopération saine | Engagement de capacité auprès d’un prestataire / droit interne sur une ressource pour un besoin. Des noms proches ne justifient pas une fusion. |
| Return Order / Return Disposition / Repair Order | Coopération saine après U769 | Tenir le retour / déterminer le devenir / tenir la prestation de réparation. Les scénarios racontent leur coopération. |
| Document Production / Billing / Customs Clearance | Coopération saine à préserver | Produire ou assembler un livrable / demander émission de facture / confier une procédure douanière. Une pièce documentaire peut servir les deux autres sans créer leurs faits. |
| Operations Tracking / Service Reconciliation / Operations Visibility / Service Orders | Clarification ciblée F08/F15 | Faits intégrés / conformité et écarts / état restitué / engagement et solde individuels ; la même donnée consommée ne constitue pas un doublon de responsabilité. |
| Master Planning / Simulation / décisions spécialisées | Coopération saine | Pilotage du plan / comparaison d’alternatives / décisions contributrices. Les quatre comportements Schedule/Run/Stop/Rerun ne deviennent pas des capacités ou des scénarios par cet audit. |

## Séquence appliquée sous U771

1. Corriger les contradictions entre définitions, glossaire, portées et commentaires marché.
2. Clarifier les sorties et responsabilités ; hiérarchiser les preuves ; harmoniser la rédaction.
3. Ajouter Receiving Order pour porter une réception confiée, avec ses engagements et résultats.

Le modèle canonique est mis à jour ; la publication demeure inchangée. L’application est tracée dans [l’annexe unique du backlog](../modeles/backlog/vocabulary-boundary-audit-U770.yaml). La restitution ne constitue pas une seconde backlog.

## Sources primaires relues

- [Microsoft — Consignment](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment) — consultation du 25 septembre 2026.
- [Microsoft — Create a consignment replenishment order](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/tasks/create-consignment-replenishment-order) — consultation du 25 septembre 2026.
- [Oracle — Profitable-to-promise](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26c/fascp/create-alternative-fulfillment-scenarios-to-reduce-cost.html) — consultation du 25 septembre 2026.
- [Microsoft — Master plans](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans) — consultation du 25 septembre 2026.
- [Microsoft — Supply forecasts](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/supply-forecast) — consultation du 25 septembre 2026.
- [Microsoft — CTP](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp) — consultation du 25 septembre 2026.
- [Microsoft — DOM](https://learn.microsoft.com/en-us/dynamics365/commerce/dom) — consultation du 25 septembre 2026.
- [Microsoft — Product information](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information) — consultation du 25 septembre 2026.
- [Microsoft — Warehouse exchange data](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-exchange-data) — consultation du 25 septembre 2026.
- [Oracle — Back-to-back flows](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauco/how-orchestration-processes-back-to-back-flows.html) — consultation du 25 septembre 2026.

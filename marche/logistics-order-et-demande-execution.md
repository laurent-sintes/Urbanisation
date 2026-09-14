# Demande d’exécution : les noms du marché

14 septembre 2026 — U165/U166. Recherche d’objets et documents métier, pas catalogue de capacités. Noms locaux encore ouverts. [Comparaison structurée](../modeles/backlog/vocabulary-review.json).

| Référence | Noms | Sens et rapprochement | Source et version |
| --- | --- | --- | --- |
| SAP Digital Manufacturing | Logistics Order | Ordre de transport de matières et encours entre emplacements de l’atelier. Nom exact attesté ; périmètre atelier plus étroit que la demande générique adressée à toute plateforme logistique. | [Source](https://help.sap.com/docs/sap-digital-manufacturing/execution/manage-logistics-orders?locale=en-US&state=PRODUCTION&version=latest) — Documentation latest, édition non figée |
| Microsoft Dynamics 365 Supply Chain Management, Warehouse management only mode | Inbound Shipment Order, Outbound Shipment Order | Documents dédiés à l’exécution en entrepôt, utilisés notamment avec un ERP ou un OMS externe. Fort rapprochement : documents logistiques pouvant remplacer les documents généraux achat, vente et transfert du seul point de vue WMS. Pas une couverture générale de toutes prestations ; restrictions retours, production et transport documentées. | [Source](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-overview) — Documentation en ligne, version produit non figée |
| SAP EWM | Warehouse Request, Outbound Delivery Order, Outbound Delivery Request | Warehouse Request porte le travail demandé au WMS ; Outbound Delivery Order en est un type. Messages de demande et document interne du WMS sont distingués dans la version consultée. Rapprochement pertinent au niveau entrepôt, sans mapping universel avec un objet unique FLOW. | [Source](https://help.sap.com/docs/SAP_SUPPLY_CHAIN_MANAGEMENT/ce32eae1b3db423fb4625f3d692cae6f/39cecb53ad377114e10000000a174cb4.html?locale=en-US&state=PRODUCTION&version=7.0.2VERSIONFORSAPHANA) — SCM 7.0.2 version for SAP HANA |
| SAP Transportation Management | Freight Order | Document de planification et réalisation du transport routier ou ferroviaire ; peut être affecté à un transporteur. Spécifique au transport ; Freight Booking également présent pour aérien/maritime. | [Source](https://help.sap.com/docs/SAP_TRANSPORTATION_MANAGEMENT/54cf405c9d9e4c96bf091967ea29d6a7/ff8bbbea9bd0421b9f833793d8d52b3d.html) — 9.6 FPS02 |
| Oracle Fusion Cloud Inventory Management | Shipment Request | Demande d’expédition transmise à un WMS ou à un prestataire logistique tiers, avec retour de confirmation. Appui direct pour la frontière Supply/exécution sortante ; ne couvre pas seul toute prestation logistique. | [Source](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/faims/Chunk1514687883.html) — 25C |
| GS1 EDI | Transport Instruction, Transport Instruction and Response | Vocabulaire standard d’instruction et de réponse pour le transport. Appui de nom et de distinction instruction/réponse ; guide complet non consulté dans cette recherche. | [Source](https://www.gs1.org/standards/edi) — Index des standards, édition du guide non établie |
| SAP EWM — Warehouse Order | Warehouse Order | Lot de travail exécutable constitué de tâches d’entrepôt ou de postes d’inventaire pour un opérateur. Granularité interne d’exécution ; ne pas le confondre avec la demande amont de prestation. | [Source](https://help.sap.com/docs/SAP_SUPPLY_CHAIN_MANAGEMENT/ce32eae1b3db423fb4625f3d692cae6f/65cccb53ad377114e10000000a174cb4.html?version=7.0.2VERSIONFORSAPHANA) — SCM 7.0.2 version for SAP HANA |

## Lecture pour FLOW

Logistics Order est bien attesté, avec un usage atelier dans SAP Digital Manufacturing. Il peut être proposé localement pour un ordre de prestation logistique, sans présenter notre sens plus large comme le standard SAP. Le mode WMS autonome Microsoft constitue l’appui le plus direct à la distinction évoquée par Laurent : les Orders métier généraux restent dans le système amont et les Shipment Orders portent le besoin du point de vue entrepôt. Oracle emploie Shipment Request à cette frontière sortante ; SAP distingue des documents EWM et TM selon les prestations et étapes.

Proposition de travail : Order reste le pilotage Supply ; Logistics Order pourrait matérialiser une prestation logistique confiée ; Execution Request pourrait servir de terme plus général si des prestations non logistiques sont incluses. Ces noms et cette généralisation restent proposés, sans nouvel objet, hiérarchie ou lien créé. L’appui D07 U165 reste à instruire. Aucun équivalent universel exact démontré entre tous les produits.

Le suffixe Order n’implique pas la même responsabilité aux deux niveaux : le document demandé à un prestataire et les tâches produites dans son organisation sont distincts. Warehouse Order chez SAP est précisément un lot interne de travail, ce qui en fait un faux équivalent pour notre frontière amont.

## Consultation

- SAP Digital Manufacturing : Texte indexé détaillé consulté le 2026-09-14.
- Microsoft Dynamics 365 Supply Chain Management, Warehouse management only mode : Texte indexé détaillé consulté le 2026-09-14.
- SAP EWM : Texte indexé détaillé consulté le 2026-09-14 ; variantes récentes possibles.
- SAP Transportation Management : Texte indexé détaillé consulté le 2026-09-14.
- Oracle Fusion Cloud Inventory Management : Page ouverte et texte consulté le 2026-09-14.
- GS1 EDI : Index officiel consulté via résultat indexé le 2026-09-14 ; ouverture du guide spécifique en erreur.
- SAP EWM — Warehouse Order : Texte indexé détaillé consulté le 2026-09-14.

Aucun produit ou déploiement Beaumanoir n’est déduit. Les instructions et demandes ne sont pas des preuves de prise en charge ni de réalisation ; la logistique reste en adhérence du développement FLOW.


## U167 — généralisation à une prestation de service

Laurent confirme que la plateforme exécutante ne doit pas être limitée à la logistique. Codex propose **Service Order** : commande métier adressée à un prestataire pour réaliser une ou plusieurs prestations, précisant les résultats attendus et les conditions de réalisation. Définition et nom restent proposés.

TM Forum emploie Service Order pour placer et suivre une commande de service ; SAP CRM emploie ce nom pour une commande de prestations à un fournisseur de services. Service Request peut, chez SAP, porter une demande de résolution de problème liée à un produit : ce sens se rapproche davantage du traitement amont. Il n’existe pas de déduction universelle Request avant Order, ni Order nécessairement déjà accepté.

L’objet candidat porterait identité/version, parties, origine, prestations et résultats, paramètres pertinents, conditions demandées et liens vers réponses et faits. Le prestataire conserve ses moyens et son organisation. Conditions souhaitées, engagements acceptés et résultats constatés doivent être distingués. Cette liste prépare la discussion sans créer un schéma, un catalogue de services, des relations ni des capacités supplémentaires.

Sources consultées le 14 septembre 2026 :

- [TM Forum — Service Ordering Management API TMF641](https://www.tmforum.org/open-digital-architecture/open-apis/service-ordering-management-api-TMF641/v4.1) : Présentation officielle indexée consultée le 2026-09-14 : placer, créer, modifier et consulter des Service Orders et suivre leurs notifications. URL v4.1 avec historique multiversion ; schéma détaillé non consulté. Appui au nom et à la responsabilité de commande de service ; le domaine télécom ne définit pas automatiquement un objet générique FLOW.

- [SAP CRM — Service Order](https://help.sap.com/docs/SAP_CUSTOMER_RELATIONSHIP_MANAGEMENT/62fb3bfc9f124f598f6e911e17321a3c/276806825cd111da36bb000f20dac9ef.html) : Extrait indexé consulté le 2026-09-14 ; édition détaillée inconnue. Objet métier représentant les commandes d’un client à un prestataire pour fournir des services, avec éventuelles pièces en après-vente.

- [SAP CRM — Service Request](https://help.sap.com/docs/SAP_CUSTOMER_RELATIONSHIP_MANAGEMENT/8450ce4407c3424ab678aaf10431af69/2765bcc45cd111da36bb000f20dac9ef.html?locale=en-US&state=PRODUCTION&version=7.0.2.24) : Texte indexé détaillé consulté le 2026-09-14 ; CRM 7.0 EHP2 SP24. Demande de résolution d’un problème lié à un produit, avec documentation et résultats ; ne se confond pas avec la définition locale proposée de prestation confiée.


## U168 — Orders contextualisés

Laurent affirme deux contextes, Supply et Services, avec des définitions propres des Orders. Cette distinction est consignée ; les formulations et attributs détaillés proposés U167 ne reçoivent pas de validation globale.

L’interprétation DDD est pertinente pour une frontière sémantique : les modèles peuvent donner des sens distincts au même mot et expliciter leurs relations. [Martin Fowler — Bounded Context](https://martinfowler.com/bliki/BoundedContext.html), extrait consulté le 14 septembre 2026. La présence d’Orders différents ne suffit cependant pas à fixer exactement un bounded context pour tout Supply et un pour tout Services : leur cohérence interne et la granularité restent à instruire.

Proposition Codex : employer Order localement si le contexte est explicite, et Supply Order / Service Order aux frontières ; préserver les règles et cycles propres, avec contrats d’échange et correspondances explicites. Ne pas imposer de modèle Order universel, de cardinalité, de symétrie des états ou de découpage applicatif. Cette réflexion ne transforme pas les domaines de capacités en bounded contexts ni ne crée un univers Services automatiquement.


## Validation U169 — frontière Supply / Services

Laurent valide la restitution de U168. Supply Order désigne la commande dont on travaille couverture, priorités et promesse ; Service Order désigne la commande de prestations confiées à un exécutant. Supply décide comment satisfaire les commandes ; Services organise et réalise les prestations, puis rend compte des résultats.

Order peut être le nom local ; Supply Order / Service Order qualifient le contexte dans les échanges et comparaisons. Les modèles communiquent par contrats explicites sans objet partagé ou cycle identique imposé. Les domaines de capacités délimitent des espaces problématiques, les bounded contexts la validité des modèles. La granularité interne reste ouverte.

Cette validation remplace les mentions historiques de nom seulement proposé pour Service Order. Elle n’adopte pas les attributs détaillés U167, de cardinalité, d’univers supplémentaire ni de déploiement. Portée et empreintes dans l’annexe JSON, section context_boundaries_U168.

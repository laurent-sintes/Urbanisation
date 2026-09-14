# Retail chez SAP et application au wholesale

14 septembre 2026 — U177, U178, U179. Complément de l’audit U176, sans modification de carte ni adoption de vocabulaire local.

Retail conserve son sens métier de commerce de détail. SAP Retail désigne aussi une solution sectorielle qui couvre les opérations nécessaires à cette activité, incluant achats, distribution, réassort, gestion des stocks et vente. Le nom sectoriel n’est pas une frontière de couche d’urbanisation.

SAP documente explicitement la vente de prepacks complets en wholesale, et la vente de leurs composants dans le scénario retail. Les displays sont également expédiés aux magasins ou à des clients wholesale. Ensemble, composants et règles de gestion du stock restent à distinguer ; leur traitement dépend du paramétrage. Ce sont des usages documentés, pas une règle universelle de commercialisation.

SAP S/4HANA for Fashion and Vertical Business couvre fabrication, wholesale et retail et repose sur l’architecture de la solution SAP Retail. La source retrace une séparation historique entre AFS pour wholesale/fabrication et Retail pour les magasins, puis leur convergence. Cela explique pourquoi on retrouve un vocabulaire Retail dans une solution de périmètre plus large. Ne pas généraliser ce constat à toutes les éditions ou installations SAP, ni conclure à son usage installé chez Boardriders.

Dans l’audit, employer « modèle Article de SAP Retail, également mobilisé par Fashion/wholesale » plutôt que laisser entendre « modèle réservé au commerce de détail ». Les articles génériques et variantes expriment une déclinaison de références ; les articles structurés expriment une composition. Aucun de ces deux mécanismes n’est adopté automatiquement comme objet ou capacité FLOW. La continuité de référence à travers les canaux est une piste d’urbanisation à éprouver.

## Sources consultées

Les trois pages SAP Learning ont été ouvertes et leur texte lu le 14 septembre 2026 ; versions de cours non indiquées.

- [Retail Article Master](https://learning.sap.com/courses/discovering-retail-functions-and-business-processes-in-sap-s-4hana-retail/introducing-the-retail-article-master_bd2d9df6-bf54-4612-8fa0-b35c63fbb0d8) — Catégories et usages des variantes dans les achats, la logistique et la vente.
- [Structured Articles](https://learning.sap.com/courses/configuring-master-data-in-sap-s-4hana-cloud-private-edition-retail/structured-articles-1) — Sections Structured Articles: Structure and Definition : prepacks en wholesale, displays vers wholesale customers, niveau de stock configurable.
- [Fashion and Vertical Business](https://learning.sap.com/courses/outlining-sap-s-4hana-for-fashion-and-vertical-business-and-implementing-best-practices/understanding-sap-s-4hana-for-fashion-and-vertical-business) — Sections From Mill to Till et Vertical Processes : portée fabrication/wholesale/retail, architecture Retail et distinction historique AFS/Retail.

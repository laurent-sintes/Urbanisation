# Visibility dans Authoritative Data — analyse marché U519, cadrage U520

> Cadrage postérieur U523–U525 : la comparaison est portée par la fiche de travail de Visibility ; Fluent Sourcing correspond au Network FLOW. La frontière PLAN/orchestration reste à arbitrer Q078 et Inventory Planning Context est en attente. Voir la [comparaison courante](comparaison-oracle-fluent-U522.md). Aucune capacité existante n’est supprimée.

**Le marché étaye une capacité qui fournit les références selon les besoins des consommateurs Supply, indépendamment de leur organisation dans le stockage.** Les sources consultées ne définissent pas un catalogue commun de vues ni un nombre de capacités à reprendre.

Analyse au 21 septembre 2026. La demande U520 maintient la discussion au niveau des capacités, y compris pour les référentiels. Les exemples ci-dessous expliquent le service rendu ; ils ne proposent pas de nouveaux Behaviors ni un détail de règles.

## Service proposé pour Visibility

**Rendre les références utiles à l’orchestration consultables sous une forme adaptée aux capacités Supply qui les consomment.**

La capacité permet de rechercher et consulter les références pertinentes et de rapprocher plusieurs sujets lorsque l’usage le justifie. Son bénéfice est une lecture métier utile, indépendante du domaine source et de l’organisation du stockage. Les décisions, la tenue des états opérationnels et les actions restent portées par les capacités consommatrices.

Dans la structure discutée, les responsabilités sont complémentaires :

| Capacité proposée | Service rendu | Axe de lecture |
| --- | --- | --- |
| Ingestion | Recevoir les données de référence des domaines qui les fournissent. | Domaines sources |
| Core Data | Conserver et organiser les références locales nécessaires à l’orchestration. | Ensembles conservés |
| Visibility | Rendre ces références consultables selon les usages des capacités Supply. | Besoins consommateurs |

Cette tripartition reste une proposition FLOW ; les documents de produits ne constituent pas une adoption ou une nomenclature de capacités équivalente.

## Comparaison avec le marché

| Sources primaires | Ce qu’elles documentent | Conséquence à la maille capacité |
| --- | --- | --- |
| Fluent — Reference Sourcing Conditions / Criteria | Le sourcing croise les caractéristiques de plusieurs sujets et le contexte de demande. | La lecture consommée traverse produit, parties et réseau. |
| Microsoft IOM — API DOM / FRO ; IBM Sterling — Node sourcing/scheduling | L’optimisation combine références produit, lieux et prestations avec des états opérationnels. | Un consommateur a besoin d’un contexte cohérent ; toutes ses entrées ne relèvent pas d’Authoritative Data. |
| Oracle — Assignments and Rules et données collectées ; SAP — ABC | Les caractéristiques produit/client/lieu servent plusieurs usages de promesse et d’orchestration. | Une même base de références peut servir plusieurs lectures et décisions. |
| Microsoft SCM et Oracle Replenishment Planning | Approvisionnement et planification utilisent des regroupements adaptés aux produits, lieux et conditions. | Les besoins dépassent ceux d’un OMS de vente ; le périmètre Supply FLOW est plus large. |
| Microsoft Sales returns et Fluent Returns Component | Les retours rapprochent des références de qualification et des données propres au dossier. | Les références restent distinctes du dossier et de l’issue décidée. |

**Constat :** les consommations par usage sont documentées. **Interprétation FLOW :** elles soutiennent Visibility orientée consommateurs. **Limite :** elles ne prouvent ni un nom commun de capacité, ni six vues standard, ni leur matérialisation ou leur autonomie logicielle. Les sources couvrent cinq éditeurs dans un échantillon ciblé ; elles ne démontrent aucune réalisation Beaumanoir.

## Grands besoins à couvrir

Il s’agit des Areas consommatrices actuelles, et non d’une proposition de six nouvelles capacités ou de six vues.

| Area consommatrice | Besoin auquel Visibility contribue |
| --- | --- |
| Service Requests | Qualifier les demandes et leurs conditions, qu’il s’agisse de vente, d’achat, de transfert, d’apport ou de retour. |
| Inventory Management | Identifier et contextualiser les stocks, les lieux et les responsabilités associées. |
| Process Management | Préparer le recours aux services et prestataires de réalisation. |
| Order Promising | Fournir le contexte de référence nécessaire à l’évaluation des possibilités de satisfaction. |
| Fulfillment Optimization | Donner les références utiles pour comparer et organiser la satisfaction des demandes. |
| Inventory Optimization | Fournir le contexte des décisions d’implantation, de réassort, de redistribution et de retour. |

Les mêmes références peuvent servir plusieurs capacités, et une capacité peut mobiliser plusieurs sujets Core Data. Les correspondances sont donc plusieurs-à-plusieurs. Les exemples logistiques sont mieux couverts par le corpus que les prestations humaines ou numériques ; les éléments économiques et contractuels doivent rester situés à leur portée documentaire.

La lecture locale a porté sur les 42 capacités opérationnelles. Le relevé distingue besoins directs, usages indirects et capacités tenant des états ou produisant des effets. Il sert de preuve interne, sans fixer de décomposition supplémentaire.

## Frontières et portée

Une référence de lieu ou de service reste distincte du stock ou de la capacité disponible. Le contexte d’une promesse reste distinct de la promesse calculée. Les conditions d’un retour restent distinctes du dossier et de la décision sur ce retour. Fluent documente aussi des projections opérationnelles ATS/ATP : le terme projection ne suffit donc pas à classer une donnée dans Authoritative Data.

À cette étape, la recommandation porte sur **le service rendu et la frontière de Visibility**. Le nombre et les noms des vues, leurs champs, les Behaviors éventuels et le détail des règles sont différés conformément à U520. Les sujets Core Data déjà discutés restent à leur statut actuel ; aucun ajout détaillé n’est déclenché par la recherche.

U521 demande de garantir la lisibilité des références à la release : la synthèse comparative et deux appuis primaires sont désormais portés dans Sources d’inspiration de la fiche canonique Authoritative Data. L’enrichissement est éditorial ; noms, définitions, structure, relations et accords restent inchangés. Aucun catalogue Information étendu et aucune publication. L’accord U518 sur Party Restrictions conserve sa portée.

## Preuves et proposition

- [Proposition au niveau capacité](../../modeles/backlog/authoritative-data-views-U519.yaml)
- [Oracle, SAP et compléments — relevé primaire](oracle-sap-planning-evidence.yaml)
- [Fluent — relevé primaire](fluent-evidence.yaml)
- [Microsoft et IBM — relevé primaire](oms-evidence.yaml)
- [Index bibliographique et correspondances ELM](source-index.yaml)
- [Lecture des consommateurs du modèle](consumer-map.yaml)

Les notes exploratoires détaillées des relevés ont été produites pendant U519. Elles restent des matériaux documentaires internes ; le présent cadrage U520 définit la maille de la proposition.

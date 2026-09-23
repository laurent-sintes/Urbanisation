# Revue détaillée — U625

État capturé le 22 septembre 2026. Lecture sémantique au périmètre glossaire / métamodèle / Domain / Purpose, complétée par le contrôle exhaustif des métadonnées marché. « Aucun écart supplémentaire identifié » ne signifie ni accord métier ni relecture externe exhaustive des sources. Les constats A01–A08 sont détaillés dans [rapport.md](rapport.md).

## Domain et Purposes

| ID | Nom courant | Rapprochements | Constats | Revue |
| --- | --- | --- | --- | --- |
| universe-supply | Supply Chain Orchestration | 6 | A01 A02 | Périmètre général étayé. Actualiser le renvoi au plan d'ensemble D17 et la place des politiques maîtrisées ; services numériques/humains au service de ce Domain, sans extension à toute l'entreprise. |
| business-references | Authoritative Data | 11 | A01 A07 | Sept références conservées, gouvernances présentes ; finalité commune avec les policies encore absente du scope et de la présentation canonique. |
| D04 | Service Requests | 3 | A01 A03 A06 A07 | Demand doit porter besoins, exigences et promesse U595. Ancien Service Order encore cité. Sources Salesforce IT/TMF641 partielles pour cette finalité. |
| D01 | Inventory Management | 2 | A01 A07 | Stock et apports attendus à distinguer lors de la refonte. Réservation, position, mouvement et protection restent des responsabilités distinctes ; pas de suppression déduite du changement de Purpose. |
| D06 | Process Management | 2 | A03 A04 A07 | Actualiser Task et document optionnel U616/U617, frontière d'exécution, reprise ciblée et renvoi vers Demand pour la promesse. |
| D15 | Order Promising | 2 | A01 A04 | La promesse reste utile ; son appartenance à un Purpose séparé et son articulation avec les décisions du plan ne reflètent pas U595. ATP/CTP/PTP restent des repères marché possibles. |
| D03 | Fulfillment Optimization | 3 | A01 A04 A07 | Compléter l'arbitrage avant exécution, y compris demandes fermes ; finalité commune avec le travail de plan à rendre explicite sans prendre en charge les réalisations. |
| D05 | Inventory Optimization | 2 | A01 A07 | Responsabilités d'ajustement identifiées ; les rattacher au cadrage du plan sans déduire un déplacement global ni étendre la preuve scientifique à toutes les capacités. |
| D17 | Supply Planning | 4 | A02 A07 | Plan d'ensemble, demande prévisionnelle et plan amont sont décrits à des mailles incompatibles. Définition, scope, enfant et positions marché à réaligner. |

## Métamodèle

| ID | Terme | Résultat | Revue |
| --- | --- | --- | --- |
| MOD001 | Decision | À conserver | Convention Decision incluant ses calculs. Références utilisateur présentes ; pas de comparaison de fiche autonome à inventer. |
| MOD002 | Planning | À conserver | Planning inclut actualisation, simulation/analyse et application du plan retenu ; mobilise des décisions distinctes. U537/U538 et CMP220 tracés. |
| MOD003 | Management | À conserver | Management distingue tenue durable des états/engagements et cadre Policy. Le nom Management d'une capacité ne suffit pas à la reclasser. |
| MOD004 | Application transactionnelle | À conserver | Application transactionnelle reste distincte du choix et de la réalisation physique ; convention locale sourcée. |
| MOD005 | Couverture — convention de description | À conserver | Couverture qualifiée par objet, périmètre, horizon et critère. Ne vaut pas preuve de réalisation installée. |
| MOD006 | Capability Behavior | À conserver | Comportement terminal et justification de décomposition présents ; typologie et CMP145 référencés. Audit U431 non rouvert. |
| MOD007 | Capability Nature | A05 | Sept natures dont Policy présentes, distinctes de la gouvernance. Remplacer l'exemple d'une Area Policy Management par un exemple compatible U618/U624 ; pas de reclassement global. |
| MOD008 | Domain | A05 | Définition avec Purposes présente. Compléter la traçabilité U624 et harmoniser les documents de méthode ; références métier auxiliaires sans cinquième niveau descriptif imposé. |
| MOD013 | Purpose | A05 A07 | Purpose/Finalité et définition U624 présents. Relier la comparaison élargie U620–U624 à la fiche ; garder convention FLOW distincte d'un standard de marché. |
| MOD009 | Business Reference | À conserver | Les trois gouvernances des références sont décrites ; un sujet peut présenter des responsabilités distinctes sans fusion de données. |
| MOD010 | Model Relationship | A08 | Appartenance, présentation et interactions distinguées. Compléter le contrôle de rattachement Purpose ; une dépendance ne crée pas de parent. |
| MOD011 | Behavior Nature | À conserver | Nature de comportement distincte de la nature de capacité et de sa gouvernance ; policy_strategy ne remplace pas policy. |
| MOD012 | Information | À conserver | Information distincte d'un modèle de données implémentable ; catalogue interne masqué et sans extension, conformément U470. |
| MOD014 | Data Governance | À conserver | Domain-managed = CRUD local ; Projection = vérité externe ; Domain-View = vue construite et rafraîchie par le domaine. Valeurs indépendantes du type. |

Compléments hors des 14 entrées : autorité de Capability (TER001), distinction du niveau Purpose et du champ finality, mise à jour du guide U458. Deux termes portent une comparaison méthodologique explicite ; les autres ont des sources utilisateur ou des annexes. Ce constat de format ne démontre pas une absence de preuve marché.

## Glossaire métier — 112 entrées

| ID | Nom courant | Rapprochements | Constats | Revue |
| --- | --- | --- | --- | --- |
| TER001 | Capacité métier | 2 | A06 | Définition méthodologique ; organiser son autorité et son renvoi depuis le glossaire métier. Capability manque comme entrée autonome du glossaire méthodologique. |
| TER002 | Objet métier | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER003 | Ressource | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER004 | Article / unité de gestion | 2 | A06 | Clarifier le renvoi vers TER060 Article et la distinction avec unité physique / unité de gestion ; pas de fusion automatique. |
| TER005 | Stock | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER006 | Position de stock | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER007 | Mouvement de stock | 2 | A06 | Alias ou distinction à rendre explicite avec TER055 ; aucune contradiction certaine déduite de la proximité. |
| TER008 | Ressource attendue | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER009 | Disponibilité | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER010 | Besoin | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER011 | Demande | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER012 | Commande | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER013 | Engagement | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER014 | Promesse | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER015 | Confirmation de promesse | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER016 | Réservation de ressource | 2 | — | Distinction réservation / protection à conserver ; aucun nouvel écart identifié. |
| TER017 | Affectation de ressource | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER018 | Allocation de groupe | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER019 | Protection de ressource | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER020 | Plafond de confirmation | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER021 | Pool de ressources | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER022 | Couverture d’une demande | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER023 | Règle métier | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER024 | Processus | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER025 | Opération métier | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER026 | Réalisation d’une capacité | 2 | A06 | Notion de réalisation relevant du vocabulaire méthodologique ; conserver identifiant et liens historiques. |
| TER027 | Fonction | 2 | A06 | Notion principalement méthodologique ; préciser son autorité et éviter deux définitions concurrentes. |
| TER028 | Fonctionnalité de produit | 2 | A06 | Distinction produit/capacité à préserver dans le vocabulaire méthodologique. |
| TER029 | Regroupement de capacités | 2 | A05 A06 | Regroupement de lecture distinct de Purpose fondé sur une finalité ; faire un renvoi explicite, sans les assimiler. |
| TER030 | Domaine | 2 | A05 A06 | Domaine méthodologique à articuler avec MOD008 et la hiérarchie U624 ; éviter une assimilation automatique au sous-domaine DDD. |
| TER031 | Orchestration | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER032 | Fabrication à façon | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER033 | Planned Purchase Order | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER034 | OMS — sens fonctionnel du projet | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER035 | Supply — sens fonctionnel du projet | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER036 | Fait de gestion — sens plateforme | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER037 | Document — sens plateforme | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER038 | État d’objet métier | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER039 | Notification d’événement | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER040 | Stock physique | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER041 | Stock logique | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER042 | Stock virtuel | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER043 | Stock futur | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER001 | Définir | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER002 | Tenir — en réexamen | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER003 | Déterminer | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER004 | Calculer | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER005 | Vérifier | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER006 | Autoriser | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER007 | Enregistrer | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER008 | Demander | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER009 | Protéger | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER010 | Allouer à un groupe | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER011 | Réserver | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER012 | Affecter | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER013 | Promettre | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER014 | Confirmer | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER015 | Prioriser | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER016 | Arbitrer | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER017 | Réviser | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER018 | Réaffecter | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER019 | Libérer | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER020 | Consommer | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER021 | Annuler | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER022 | Rapprocher | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER023 | Exécuter | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER024 | Gérer | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| VER025 | Valider | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER044 | Available-to-Promise — ATP | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER045 | Capable-to-Promise — CTP | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER046 | Party | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER047 | Role | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER048 | Agreement | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER049 | Product Catalog | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER050 | Reference Ingestion | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER051 | Movement Authorization | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER052 | Product Reference | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER053 | Location | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER054 | Fulfillment Network | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER055 | Stock movement / Inventory movement ; Goods movement chez SAP | 2 | A06 | Alias ou distinction à expliciter avec TER007 ; les usages Stock/Inventory/Goods Movement peuvent rester documentés. |
| TER056 | Ledger / Inventory Ledger | 2 | — | Le candidat Inventory Ledger Management est explicitement non adopté ; ce statut exploratoire n'est pas une erreur à effacer. |
| TER057 | Product | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER058 | Product Variant | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER059 | Product Unit | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER060 | Article | 2 | A06 | Articuler Article avec TER004 et les unités ; préserver les différences de granularité. |
| TER061 | Container | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER062 | GTIN | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER063 | Serial Number | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER064 | Case | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER065 | Supply Order | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER066 | Backing Service Order | 2 | A03 | Backing Service Order encore canonique ; nom et définition à aligner avec le document Service Order éventuellement produit par une Task U616. |
| TER068 | Profitable-to-Promise (PTP) | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER069 | Sales Order | 2 | — | Sales Order reste l'intention de vente ; Consignment Issue doit être expliqué comme comportement, pas comme nouvelle famille autonome. |
| TER070 | Purchase Order | 2 | — | L'achat de biens ou prestations reste compatible avec U619 ; ne pas transformer toute sollicitation de Service en achat. |
| TER071 | Transfer Order | 2 | A06 | Déplacement physique défini trop largement pour expliquer à lui seul la distinction locale transfert / consignation / retour. Ajouter la frontière d'intention. |
| TER072 | Customer Return Order | 2 | A06 | Customer Return Order reste le nom du glossaire, alors que D04.l est Return Order U612 ; synchroniser sans réintroduire les comportements abandonnés. |
| TER073 | Supplier Return Order | 2 | — | Le retour vers fournisseur et ses suites restent utiles ; ne pas confondre son sens avec une reprise de consignation sans motif de retour. |
| TER074 | Replenishment | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER075 | Service | 2 | — | Service physique, humain ou numérique déjà correctement couvert ; la lacune porte sur la Task et le document qui l'entourent. |
| TER076 | Service Level Agreement (SLA) | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER077 | Couverture de stock | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER078 | Supply Assignment Plan | 3 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER079 | Implantation | 3 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER080 | Réassort | 2 | — | Sens local de Réassort explicitement distingué des usages plus larges du marché ; pas de normalisation automatique. |
| TER081 | Split | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER082 | Spread | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER083 | Supply | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER084 | Supply Chain | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER085 | Fulfillment | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER086 | Purchase Order Document | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER087 | Assortment | 2 | — | Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes. |
| TER088 | Service Provider | 2 | — | Service Provider déjà nommé ; conserver la différence fournisseur métier / connecteur de produit, et relier la policy locale. |

## Notions à couvrir ou relier explicitement

Task ; consignation et ses deux sens ; Consignment Fill-up ; Consignment Pick-up ; Consignment Issue ; distinction Service Provider / Service Catalog / Service Provider Policy. Les ajouts de définitions n'impliquent pas de nouveaux nœuds de capacité. Aucun identifiant retiré ne doit être réutilisé.

## Reproduction

`python audits/2026-09-22-model-scope-U625/build_review_matrix.py` régénère uniquement cette matrice à partir des pièces d'audit capturées et des appréciations explicites du script ; cette commande ne réaudite pas un backlog ultérieur.

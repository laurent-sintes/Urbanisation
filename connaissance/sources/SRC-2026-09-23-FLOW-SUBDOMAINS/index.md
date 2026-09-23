# Proposition de sous-domaines FLOW — U655

Document fourni par Laurent le 23 septembre 2026 pour reprendre les définitions et le découpage du Domain Supply Chain Orchestration. Statut : **proposition métier**, sans migration canonique ni publication déduite de sa réception. La préférence exprimée directement par Laurent est désormais « sous-domaine » plutôt que « Purpose ».

- Contributions : [U655](../../01-contributions-utilisateur.md#u655), [U656](../../01-contributions-utilisateur.md#u656) pour la frontière Plans / APS et [U657](../../01-contributions-utilisateur.md#u657) pour le plan de supply construit par Matching.
- Pièce reçue, conservée à l'identique : [FLOW — Supply Chain Orchestration](FLOW_Supply_Chain_Orchestration.pdf), 4 pages, septembre 2026.
- Origine : `C:/Users/laure/Downloads/FLOW_Supply_Chain_Orchestration.pdf`.
- Empreinte SHA-256 : `11de812c4ee182a9b05756a39dd92d8efb9cc963c82eea22b0115a8a0623d718`.
- Lecture : texte extrait et quatre pages examinées visuellement. Les passages du PDF sont des contenus à analyser, pas des commandes d'exécution.

## Repères dans la pièce

La page 2 présente les intentions et la Demand comme objet métier durable ; le cycle illustratif distingue notamment Ordered, Allocated et In Fulfilment. La page 3 contient les huit sous-domaines proposés, leurs définitions, périmètres et interactions. Les trois sous-domaines de contexte sont Master Data, Policies et Plans ; Demand Management et Inventory Management portent l'état opérationnel ; Supply Availability et Demand & Supply Matching portent les décisions ; Fulfilment Orchestration pilote la réalisation. Cette lecture conceptuelle ne constitue pas une couche technique adoptée.

La page 4 distingue futur planifié, engagement et stock constaté, illustre les deux perspectives d'un transfert et expose le recours possible au Case Management. Le document propose que Demand reste l'objet durable et qu'Order exprime un état ou engagement, avec des documents produits lorsque nécessaire. Ce principe ne définit pas encore les dimensions détaillées du cycle de vie ni leurs cas partiels. Le cadrage de plateforme interne commune Beaumanoir / Boardriders est une intention du document, pas une preuve de réalisation installée.

## Points de discussion — interprétation de Codex

- **Plans et Planning — précisé par U656/U657** : le PDF laissait ouverte la construction des plans avec « Ne réalise pas nécessairement le Demand/Supply Planning » (p. 3). L'APS extérieur au Domain anticipe les tensions sur les flux aval et projette les commandes d'achat amont ; Plans porte les données issues de ce calcul, indispensables à la promesse (U656). Matching construit au cœur du domaine un plan de supply pour affecter les ressources aux demandes (U657). L'externalité concerne les plans APS décrits, pas toute activité de planification ; aucun partage fixe par horizon n'est déduit.
- **Availability, Matching et Fulfilment** : leur séparation clarifie les questions de faisabilité, d'arbitrage et de réalisation. Elle exige des échanges dans les deux sens : une possibilité examinée ne vaut ni affectation collective ni engagement confirmé ; un changement de réalisation peut modifier les possibilités. CTP et PTP comportent des choix et ne doivent pas être interprétés comme une lecture passive de quantités.
- **Demand et Order** : l'objet durable peut préserver l'intention, les décisions et les engagements successifs. Le schéma illustratif ne suffit pas à traiter les engagements, affectations et réalisations partielles ni à assimiler leurs dimensions à un statut unique.
- **Master Data** : la représentation faisant autorité pour le Domain est compatible avec une maîtrise d'entreprise externe, explicitement permise par la pièce. Ne pas déduire une reprise de la maîtrise PIM/MDM.

## Appuis primaires consultés le 23 septembre 2026

Ces rapprochements sont des appuis ciblés à la discussion ; ils ne constituent ni une comparaison complète de huit nouvelles fiches ni une validation du découpage.

- **Microsoft, Master plans overview**, documentation évolutive, mise à jour affichée le 25 mars 2026 : [source](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans), sections « Using master plans », « Firming », « Action message ». Point commun : plans distincts, projections et changements proposés. Différence : Microsoft réunit l'utilisation des plans et des mécanismes de calcul et de génération d'ordres ; il ne prescrit pas un sous-domaine FLOW Plans indépendant. Appui à l'explicitation de la responsabilité de construction du plan.
- **Oracle, Overview of Global Order Promising**, Fusion Cloud SCM 25C : [source](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/fascp/overview-of-global-order-promising.html), introduction et « Principles of Promising ». Point commun : prise en compte des ressources présentes ou futures et des possibilités ATP/CTP/PTP. Le passage sur les règles available-to-promise mentionne expressément les planned orders reçus de Supply Planning : il étaye l'utilisation des résultats de planification par la promesse, précisée U656. Différence : Oracle combine aussi choix de sources, substitutions, coûts et fractionnements ; ces fonctions traversent plusieurs sous-domaines de la proposition FLOW. Cette source ne prouve ni une séparation universelle Availability / Matching / Fulfilment, ni l'externalité de tous les calculs APS au sens du Domain FLOW.
- **OMG, Case Management Model and Notation 1.1**, décembre 2016 : [source](https://www.omg.org/spec/CMMN/1.1/PDF), §1, §4.1 et §5.3.1. Appui méthodologique au dossier durable et au travail adapté aux circonstances ; CaseFile fournit le contexte d'information. La spécification ne prescrit ni Demand comme objet maître Supply, ni Order comme état : ce sont des choix de modélisation FLOW proposés dans la pièce.
- **Limite d'accès** : la page SAP « Time-Series-Based Supply Planning Optimizer » a été ouverte mais n'a livré aucun texte exploitable dans cette consultation. Aucun constat nouveau n'est fondé sur cette tentative.

## Clarification acquise — U656

La construction des plans APS décrits est extérieure au Domain Supply Chain Orchestration. Aucun produit ni réalisation installée n'est déduit. L'APS fournit un futur calculé ; Plans le rend utilisable dans le domaine ; Supply Availability s'en sert pour évaluer les possibilités de promesse. Les engagements des demandes et les faits de stock restent distincts de ces projections. U657 complète immédiatement cette frontière : Matching construit son plan de supply dans le domaine.

Formulation de travail proposée par Codex, non encore adoptée dans ces termes : « Recevoir, tenir à jour et rendre disponibles les plans de demande et d'approvisionnement calculés par l'APS externe au domaine, afin d'éclairer la promesse par les besoins, les tensions et les apports futurs anticipés. »

Conséquence de cohérence à instruire lors de la reprise : la responsabilité de construction du plan de demande actuellement décrite par Demand Planning (D17.a) ne peut pas être réintroduite implicitement dans Plans. Aucun déplacement ni retrait de capacité n'est appliqué par cette note. Les décisions opérationnelles de Matching et Fulfilment restent à décrire dans leur propre périmètre. Les modalités d'intégration, de version et de rapprochement entre projections et engagements ne sont pas encore spécifiées par Laurent.

## Plan de supply construit par Matching — U657

Laurent précise que Demand & Supply Matching est une activité cœur du domaine et s'appuie sur la construction d'un plan de supply pour affecter les ressources. Il faut donc distinguer la fourniture de plans anticipatifs par l'APS et la construction du plan par lequel l'orchestration arbitre la couverture des demandes. Le sous-domaine Plans n'absorbe pas automatiquement tous les plans du seul fait de leur nom.

Formulation de travail proposée par Codex, non encore adoptée dans ces termes : « Construire et maintenir un plan de supply cohérent pour répondre aux demandes, en arbitrant l'affectation des ressources selon les disponibilités, les engagements et les politiques applicables. » Les responsabilités de construction du plan et de décisions spécialisées restent descriptibles ; aucun déplacement de capacité n'est appliqué ici.

L'exemple Microsoft de plans recalculés à partir de la demande et de la supply, ainsi que ses propositions de modification d'ordres, apporte un recouvrement fonctionnel partiel avec cette planification. Oracle illustre l'utilisation par la promesse d'apports issus de Supply Planning. Ces deux documents déjà consultés éclairent la coexistence des responsabilités ; ils ne prescrivent ni le sous-domaine FLOW Matching, ni une frontière universelle entre APS et orchestration. Aucun second dossier marché n'est ouvert pour cette seule précision.

## Évaluation marché et clarification du vocabulaire — U658–U660

U658 demande ensuite une comparaison du découpage au marché. L'[étude structurée](../../../modeles/backlog/subdomains-market-review-U658.yaml) et [CMP269](../../../marche/comparaisons.md#cmp269) portent la comparaison des huit sous-domaines : responsabilités étayées, frontières locales et recommandations, avec au moins deux documents primaires distincts par comparaison.

U659/U660 précise que Demand désigne la demande face à l'offre et envisage Order pour l'objet opérationnel individuel. Recommandation Codex : Order Management est un candidat mieux étayé pour gérer cet objet, son cycle de vie et ses engagements. Si ce choix est retenu, Order nomme l'objet durable et l'engagement devient une de ses dimensions ; la formule Order = état du PDF reste la proposition historique à réviser. Demand Plan et Demand & Supply Matching conservent leur sens de demande face à l'offre. Aucun nom n'est encore adopté par cette discussion et le PDF reçu reste inchangé.

# Order Management : rendre les responsabilités concrètes

> **Évolution U214 — 15 septembre 2026 :** le backlog remplace les quatre capacités D04.e–h par cinq capacités par type d’ordre, Order Structuring et Order Lifecycle Management (D04.i–o). Les propositions de conserver quatre capacités sont historiques. Voir la [refonte et les descriptions concrètes](../connaissance/29-order-management-refonte.md) ; les publications restent inchangées.

Analyse Codex du 15 septembre 2026, en réponse à U210. « ITM » est interprété provisoirement comme IBM ; clarification demandée, sans réponse enregistrée à la rédaction. Aucune modification du modèle, validation ou publication métier.

**Précision U211 :** Laurent cherche les types d’Orders Supply et les aptitudes de lancement, mise en attente et report. La suite [Types d’Orders et pilotage opérationnel](order-types-et-cycle-de-vie.md) recentre la recherche. Le maintien des quatre capacités suggéré ci-dessous était provisoire et ne ferme pas l’examen de ces responsabilités.

## Base locale

Lecture de `modeles/backlog/model.yaml` par `scripts/structured_io.py`. Les champs du domaine D04 et des capacités D04.e–h sont identiques à ceux de `modeles/release/2026-09-14.1/model.yaml` (v004). Cette égalité de contenu ne fusionne pas leurs espaces ni leurs preuves de validation.

Le domaine couvre les Orders transactionnels d’achat, de vente, de transfert et de retour. Il distingue Case, Agreement, promesse D03 et prestations/faits d’exécution D07. Ses capacités sont Order Registration, Order Revision, Order Visibility et Order Reconciliation. Leurs noms et définitions courtes disposent des accords U141 ; les finalités et périmètres complémentaires ne sont pas validés par cette comparaison.

Le périmètre des quatre capacités renvoie encore à Q077 pour annulation, suspension, fractionnement, commandes liées et limites de volumétrie. Les objets, règles et exemples sont donc insuffisamment détaillés pour éprouver les capacités. Ce constat rejoint [la note D04 et les univers](../connaissance/27-order-management-et-univers.md). La [revue D03/D04](d03-d04-capacites-manquantes.md) conserve le retrait d’Order Qualification et le rapprochement proposé de Structuring avec Revision : ces candidats ne sont pas réintroduits ici.

## Références comparées

Les sources n’ont pas la même nature. Un processus Microsoft, une capacité RBA SAP, un composant CBM IBM et une fonction Sterling ne constituent pas quatre désignations d’un même niveau.

| Référence | Apport observé | Conséquence proposée pour D04 |
| --- | --- | --- |
| Microsoft Business Process Catalog / Dynamics 365 | Manage sales orders rassemble un parcours soutenu par plusieurs produits : retours, blocages, suivi, calcul de dates, promesse et autres fonctions. [S1] | Employer ces situations comme contrôle de couverture, en répartissant les responsabilités entre nos domaines. |
| SAP RBA, définition citée par SAP EA Knowledge Base | Sales Order Management possède un périmètre client large, avec création multicanal, prix, disponibilité, risque crédit, transmission logistique et suivi. Customer Order Monitoring est distingué. L’extrait indexé est disponible ; l’ouverture directe retourne 403. [S3] | Comparer les résultats et les frontières, sans copier ce périmètre entier dans notre domaine commun. |
| IBM CBM | La note locale documente la matrice historique de 2005, compétences × Direct/Control/Execute, avec Order Management en contrôle/exécution. Les cases retail ne détaillent pas les règles des commandes. [S6] | Repère historique de responsabilités, d’un apport limité pour rendre D04 concret. |
| IBM Sterling Order Management | Documentation de produit détaillant annulation, modifications autorisées et modifications en attente. [S7–S9] | Éprouver le cycle de vie, les pouvoirs de modification et les effets sur l’exécution. Ces fonctions ne deviennent pas automatiquement des capacités CBM. |

Notre périmètre est transversal aux types de commandes, mais sa responsabilité est plus restreinte que le traitement commercial et logistique complet d’une commande client. L’existence d’une fonction externe ne démontre donc pas son absence dans D04 : elle peut relever de D03, D07, des référentiels, de la couche amont ou d’une adhérence. Aucune installation Microsoft/SAP/IBM ni couverture Beaumanoir n’est déduite de ces documentations.

## Trois apports concrets

**Microsoft : rendre le blocage observable et gouverné.** La documentation explique les motifs de mise en attente, le rôle autorisé à lever un blocage et l’effet sur la préparation/expédition. Une option peut retirer les réservations physiques. [S2] Cela fournit des questions précises : qui autorise la suspension, quelle partie du traitement est arrêtée, quels engagements sont affectés et qui décide de la reprise ? Le rattachement détaillé entre D04, D01 et D07 reste à instruire.

**SAP : préciser la structure de la commande.** Le cours Sales Order Management distingue en-tête, lignes et échéanciers portant des quantités/dates de livraison. [S4] Le cours Fashion décrit aussi le rejet d’une quantité partielle via un motif au niveau d’un échéancier et la création d’une sous-ligne associée. [S5] Il s’agit d’un comportement produit particulier, pas d’une règle universelle ni d’une cardinalité adoptée pour FLOW. L’enseignement est de distinguer commande entière, ligne, quantité et échéance lorsqu’on parle de révision ou de reliquat.

**IBM Sterling : préciser l’autorisation et l’effet d’une modification.** L’annulation est contrôlée par permissions, motifs et règles selon les états. [S7] Des modifications de commandes confirmées peuvent rester en attente, puis être enregistrées, abandonnées ou expirer ; elles s’accompagnent d’un blocage du traitement. [S8] Les règles peuvent tenir compte des états aux niveaux en-tête et ligne. [S9] La question utile pour notre modèle est ce qui devient applicable, à quel moment, et avec quelle coordination des engagements déjà pris.

## Enrichir les quatre capacités avant de redécouper

Le tableau suivant constitue une proposition d’épreuve et d’explication, sans nouvelles définitions adoptées ni inventaire d’objets créé.

| Capacité existante | Manifestation métier à expliciter | Questions à instruire |
| --- | --- | --- |
| Order Registration | Reconnaître une commande issue d’un parcours, avec son origine, ses lignes, quantités, unités et conditions applicables. | Identité et doublons ; types de commandes ; données indispensables ; lien à l’autorité amont. |
| Order Revision | Intégrer une correction autorisée de quantité, date ou destination ; traiter l’annulation partielle et conserver l’historique. | Modification après début d’exécution ; portions encore modifiables ; effet sur promesses, réservations et prestations ; suspension/fractionnement à préciser. |
| Order Visibility | Expliquer, par commande et ligne, ce qui est demandé, promis, en cours, réalisé, annulé ou bloqué. | Sources de chaque information ; fraîcheur ; coexistence d’états différents ; distinction entre visibilité et décision de promesse. |
| Order Reconciliation | Déterminer les quantités restant à satisfaire en tenant compte des révisions et réalisations reconnues. | Grain d’imputation ; unités ; faits retenus ; doublons ; tolérances ; sur-réalisation ; clôture et reliquats. |

Les principales lacunes sont le grain métier (commande/ligne/échéance), les dimensions de quantité, les règles de modification selon l’avancement, les autorités et les liens avec D03/D07. La critique d’abstraction ne démontre pas à elle seule qu’il manque une capacité autonome. L’analyse de conformité et les contrôles ne sont pas renommés Order Qualification.

**Exemple fictif à éprouver.** Une ligne commande 100 unités ; 40 sont reconnues comme satisfaites ; une annulation autorisée retire 10 unités non satisfaites. Sans autre ajustement, 50 restent à satisfaire. Registration a identifié la commande, Revision a intégré l’annulation, Visibility explique les différentes quantités et Reconciliation établit le solde. Une quantité promise ou réservée ne constitue pas à elle seule une quantité réalisée. Le fait retenu pour reconnaître la satisfaction dépend de la nature de la commande et reste à préciser : expédition et réception ne sont pas interchangeables par principe.

Pour éprouver le caractère commun de D04, reprendre cet exercice sur une vente B2B partiellement livrée, une vente B2C modifiée après lancement, un achat reçu partiellement, un transfert et un retour. Ces scénarios sont des propositions, pas des observations de SI. Les événements et documents pourront ensuite être caractérisés, avec leur signification et leur provenance, sans déduire automatiquement un agrégat ou un workflow obligatoire.

## Sources et limites d’accès

Consultation du 15 septembre 2026. Reformulations sélectives ; aucun export exhaustif des catalogues, aucune équivalence intégrale ni édition produit uniforme établie.

- **S1 — Microsoft Learn**, [Order to cash — business process areas](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/order-to-cash-areas-overview), section Manage sales orders et fonctions associées, mise à jour affichée 24 avril 2026. Texte consulté. Le catalogue et certaines illustrations évoluent à des rythmes différents.
- **S2 — Microsoft Learn**, [Manage order holds](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/tasks/manage-order-holds), mise à jour 6 mai 2026, texte consulté ; fonctions Supply Chain Management, pas feuilles natives d’une carte de capacités.
- **S3 — SAP EA Knowledge Base**, [Application Decisions for Sales Order Management in CX — Part 1](https://community.sap.com/t5/enterprise-architecture-knowledge-base/application-decisions-for-sales-order-management-in-cx-part-1/ta-p/14274899), définition attribuée à RBA. Extrait indexé revérifié ; accès direct 403. Édition RBA inconnue. Voir aussi [la note comparative historique](etudes/2026-09-09-modeles-marche/notes-sap-ibm.md).
- **S4 — SAP Learning**, [Describing Sales Order Management](https://learning.sap.com/courses/exploring-end-to-end-business-processes-in-sap-business-suite/describing-sales-order-management_ca7b816e-af6f-4a03-bd88-1a5bb42cef84), passage indexé sur les trois niveaux de document consulté ; cours Business Suite sans édition précise établie.
- **S5 — SAP Learning**, [Explaining Sales Order Handling](https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-sales-order-handling_b87d52ef-bf38-4a67-b6f5-7324019d8c24), texte de cours consulté, notamment rejet de quantité partielle ; S/4HANA Fashion, édition précise inconnue.
- **S6 — IBM Business Consulting Services**, [Component business models: Making specialization real](https://public.dhe.ibm.com/software/emea/dk/frontlines/g510-6163-component-business-models.pdf), G510-6163-00, 2005. Figure retail précédemment lue et documentée dans la note locale du 9 septembre ; lien retrouvé, téléchargement web en timeout ce jour. Aucun catalogue IBM actuel présumé.
- **S7 — IBM Documentation**, [Canceling orders](https://www.ibm.com/docs/en/order-management?topic=cancellations-canceling-orders), extrait indexé détaillé consulté ; documentation Sterling Order Management, version précise non fixée par l’URL.
- **S8 — IBM Documentation**, [Pending changes on confirmed orders](https://www.ibm.com/docs/en/order-management?topic=management-pending-changes-confirmed-orders), texte consulté ; même réserve d’édition.
- **S9 — IBM Documentation**, [Defining modification rules](https://www.ibm.com/docs/en/order-management?topic=groups-defining-modification-rules), extrait indexé consulté ; ouverture directe non restituée. Même réserve d’édition.

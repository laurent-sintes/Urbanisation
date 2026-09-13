# Orders, Agreements et Commitments

Contrôle du 13 septembre 2026 — U136, C76, CMP063. Objets et comportements de produits comparés à D04/D11/D07 du backlog et d’Urbanisation v002 ; aucun rang de Business Capability natif établi par ces pages. Synthèse Codex, propositions non adoptées.

## Constat

Orders est plus direct que Commercial Commitments pour désigner les commandes. Commitment n’est pas leur synonyme : Microsoft utilise précisément ce mot pour des engagements des Agreements. La réponse précédente de Codex décrivait l’intention locale de D04, mais ne devait pas être comprise comme une définition de marché.

| Référence | Distinctions observées | Conséquence locale proposée |
| --- | --- | --- |
| Microsoft Dynamics 365 Supply Chain Management | Sales Agreement / Sales Order et Purchase Agreement / Purchase Order. Les lignes d’Agreement portent des commitments en quantité ou valeur ; plusieurs commandes peuvent les consommer. | Préserver Agreement/Order ; éviter Commitments comme nom discriminant de D04. |
| SAP | Sales Contract distinct de Sales Order ; Purchase Order décrit une demande ou instruction de fourniture. | Appui lexical à Order pour la commande ; aucune preuve d’un domaine générique local adopté. |
| Oracle Fusion Cloud Order Management 25C | Source Order reçu ou saisi, transformé pour le fulfillment, lignes associées à l’orchestration. La structure résultante peut différer de celle reçue. | Appui partiel à la distinction document source et représentation opérationnelle de réalisation. |

Microsoft distingue aussi les lignes de commandes liées et non liées à un Agreement : la présence d’un Agreement référencé n’est pas une nécessité universelle pour toute commande dans ce produit. Notre définition ne doit pas imposer ce lien sans besoin local établi.

Les documents Microsoft décrivent création et suivi des Agreements dans le produit complet. U134 maintient ces fonctions hors de la plateforme FLOW : l’existence d’une fonction éditeur n’impose pas sa maîtrise locale. La projection externe reste un choix d’architecture explicite.

Oracle fournit une analogie utile pour séparer commande d’origine et orchestration de sa réalisation. Il ne prouve ni notre séparation exacte en deux couches, ni un objet universel achat/vente/transfert, ni que D04 et D07 doivent être deux domaines. L’OMS Oracle couvre des responsabilités traversant plusieurs de nos domaines ; ce n’est pas un équivalent direct de D04.

## Proposition pour poursuivre

Employer Order pour l’objet commande. Examiner Order Management comme candidat de nom de domaine uniquement après avoir décidé ce que la Supply possède de son cycle de vie. Si elle reçoit l’autorisation commerciale et pilote sa réalisation, préciser ces résultats avec D07 ; ne pas importer tout le périmètre d’un OMS. Agreement reste un référentiel projeté et les autorités sur les commandes restent ouvertes. Aucune modification de capacité effectuée.

## Sources consultées et limites

- Microsoft, [Sales agreements overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-agreements), introduction, Commitment types, Applying sales agreements during the ordering process ; page évolutive sans édition produit figée. Texte lu malgré le bandeau de connexion.
- Microsoft, [Purchase agreements](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-agreements), introduction, Commitment types, Applying purchase agreements in the ordering process ; page évolutive, texte lu.
- SAP, [Manage Sales Contracts](https://help.sap.com/docs/sap_s4hana_cloud/a376cd9ea00d476b96f18dea1247e6a5/b9b779568741762fe10000000a4450e5.html?q=solution+order), extrait indexé sur la création d’une Sales Order ultérieure ; édition exacte non récupérée. Ouverture directe sans texte exploitable : appui limité à cet extrait.
- SAP, [Purchase Orders](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/25a41481f62e469ba0e61015a0d39d20/ca56a952e3d27b6ae10000000a423f68.html), Definition, version affichée dans le résultat 2025 FPS01 (février 2026). Passage retourné par le moteur de recherche ; ouverture directe sans texte. Appui lexical limité.
- Oracle, [How Order Management Transforms Source Orders Into Sales Orders](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/fauom/how-order-management-transforms-source-orders-into-sales-orders.html), transformation et Parts of Sales Orders You Can Use After Transformation, édition 25C ; texte lu. Ce complément Order Management est distinct du périmètre GOP déjà étudié en MKT20 et du Retail Reference Model MKT05.

Reformulations uniquement ; aucune reproduction de catalogue. Pas de preuve de déploiement Beaumanoir, de rang RBA, BIZBOK ou TM Forum ni d’équivalence globale de domaine.
## Complément U137 — cadre et engagements de période

13 septembre 2026. Laurent propose de composer un cadre contractuel et des engagements de période pour obtenir les conditions applicables à une commande. Hypothèse en cours d’instruction : aucun nouvel objet ni domaine adopté.

Cette lecture est cohérente comme structuration locale, mais ne constitue pas une décomposition universelle du marché. Dans la page Microsoft Purchase agreements, introduction et Commitment types (relue ce jour, mise à jour affichée 2026-09-08), un même Agreement comporte une période de validité et des lignes d’engagement en quantité ou en valeur. Un objet Engagement saisonnier autonome n’est pas imposé par ce passage.

La composition locale pourrait donc être comprise comme un ensemble de conditions applicables, sans présumer un troisième document contractuel. Il reste à distinguer engagement ferme, plafond de commande et prévision ; leurs effets sur la Supply ne sont pas interchangeables. Les commandes liées contribuent à la consommation de l’Agreement ; cette consommation ne prouve pas une livraison réalisée. Illustration hypothétique : 1 000 pièces engagées, 300 commandées, 200 reçues donnent 700 restant à commander et 100 restant à recevoir sur cette commande, hors autres règles ou corrections.

Selon U134, cadre et engagements contractuels seraient reçus de leurs maîtres externes dans les projections de référence ; cette distinction conceptuelle ne réintroduit pas leur administration dans FLOW. L’autorité sur les compteurs de consommation reste à instruire (Q072). ELM106/CMP063 sont affinés sur le vocabulaire, sans nouvelle équivalence ni modification de capacité.

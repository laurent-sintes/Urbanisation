"""Record the next Order behavior discussion without changing the catalog."""
from pathlib import Path
from hashlib import sha256
from scripts.structured_io import read, dumps

ROOT = Path(__file__).resolve().parents[1]


def main():
    target = ROOT / 'modeles/backlog/purchase-order-behaviors.yaml'
    assert not target.exists()
    model = ROOT / 'modeles/backlog/model.yaml'
    before = sha256(model.read_bytes()).hexdigest()

    def append(name, text):
        with (ROOT / name).open('a', encoding='utf-8') as out:
            out.write('\n\n' + text.strip() + '\n')

    append('connaissance/01-contributions-utilisateur.md', '''## U390

**id**

U390

**date**

2026-09-18

**titre**

Poursuivre l’examen des comportements des Orders

**texte**

next*

**contexte et portée**

Après la clarification méthodologique U389 et les retours client/fournisseur, demande de poursuivre. Codex propose Purchase Order comme prochain sujet, à la suite des liens discutés entre retour fournisseur et achat de remplacement ou de prestation. Ce choix de séquence et les comportements proposés ne sont pas validés par cette demande. Aucun changement de catalogue ou publication.''')

    sources = [
        dict(id='PO-S1', vendor='Microsoft', product='Dynamics 365 SCM', title='Create purchase orders', url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-creation', edition='Documentation évolutive', locator='Adding purchase order lines', consulted_on='2026-09-18', access='Page primaire ouverte', finding='Les commandes peuvent porter des produits physiques ou des services ; destination, quantités et dates sont précisées.', limit='Types de lignes produit, pas une taxonomie de comportements.'),
        dict(id='PO-S2', vendor='Microsoft', product='Dynamics 365 SCM', title='Direct deliveries', url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/direct-deliveries', edition='Documentation évolutive', locator='Introduction, Delivery date, Delivery address, Warehouse', consulted_on='2026-09-18', access='Page primaire ouverte', finding='Livraison fournisseur au client et liens entre lignes achat/vente ; coordination des dates et destinations sans passage physique dans l’entrepôt du vendeur.', limit='FLOW ne reprend pas automatiquement les règles de propagation des dates ni les écritures du produit.'),
        dict(id='PO-S3', vendor='SAP', product='S/4HANA on-premise', title='Manage Service Entry Sheets - Lean Services / Planned and Unplanned Services', url='https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/4ac8acf820ad41a8a5841420085ba68d.html', edition='2025 FPS01 (Feb 2026) affichée sur la page associée Planned and Unplanned Services', locator='Introduction et Create or change a service entry sheet with reference to a purchase order', consulted_on='2026-09-18', access='Passages primaires indexés lus ; ouverture directe du portail sans texte exploitable', finding='Les prestations exécutées sont constatées par référence à une commande d’achat ; services planifiés et non planifiés.', limit='Application et documents SAP, pas une nouvelle capacité d’exécution FLOW ; aucune feuille de saisie imposée.'),
        dict(id='PO-S4', vendor='Microsoft', product='Dynamics 365 SCM', title='Set up consignment', url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment', edition='Documentation évolutive', locator='Inventory ownership change journal', consulted_on='2026-09-18', access='Page primaire ouverte', finding='Le transfert de propriété du stock fournisseur déclenche un traitement de commande d’achat distinct de la présence physique préalable.', limit='Le parcours de consignation traverse stock et achat ; rattachement de tout le parcours à Purchase Order non établi.'),
    ]
    proposals = [
        dict(id='PO-P01', name='Stock Procurement', definition='Prendre en charge l’achat de marchandises destinées à entrer dans le stock du réseau et suivre les apports attendus jusqu’à leur réception.', mechanism='Parcours d’approvisionnement physique avec quantités et échéances restant à recevoir.', benefit='Fiabiliser les apports futurs sans confondre commande fournisseur, arrivée et stock disponible.', example='Exemple fictif : achat de 2 000 vestes destinées à un entrepôt ou directement à des magasins.', boundary='D05/D03 déterminent les besoins ou réponses ; D06 suit les prestations et D01 enregistre le stock. Aucun comportement distinct par type de site.', source_ids=['PO-S1'], naming='Libellé descriptif FLOW proposé ; la source établit le mécanisme, pas ce nom comme niveau de capacité.'),
        dict(id='PO-P02', name='Direct Delivery', definition='Prendre en charge un achat dont le fournisseur livre directement le client, en conservant le lien avec la commande de vente concernée.', mechanism='Coordination des attentes achat et vente, des destinations et des preuves de livraison.', benefit='Éviter un faux apport au stock interne et rendre explicables les conséquences d’un écart fournisseur pour le client.', example='Exemple fictif : un fournisseur livre 100 pièces directement à un client wholesale.', boundary='Livrer un magasin de notre réseau relève du premier parcours lorsque l’objectif est son stock. La décision de sourcing, la promesse et l’orchestration restent distinctes ; pas de propagation automatique implicite.', source_ids=['PO-S2'], naming='Terme natif Microsoft ; variante FLOW à valider.'),
        dict(id='PO-P03', name='Service Procurement', definition='Prendre en charge l’achat d’une prestation et suivre ce qui est attendu puis reconnu réalisé, selon les conditions applicables.', mechanism='Attente de prestation et constat de réalisation, au lieu d’un apport d’articles à recevoir.', benefit='Distinguer engagement d’achat, réalisation opérationnelle et résultat du service.', example='Exemple fictif : commande de réparation de 50 pièces auprès d’un prestataire.', boundary='D04 porte l’achat ; D06 sollicite, orchestre et suit les services via les Service Orders. Pas de Purchase Order imposée pour chaque appel de service ; comptabilité et négociation contractuelle hors périmètre. Extension explicite de la définition actuelle centrée sur les biens.', source_ids=['PO-S1', 'PO-S3'], naming='Vocabulaire SAP de procurement de services ; sélection à la maille FLOW proposée.'),
    ]
    for p in proposals:
        p.update(status='proposed', parent_id='D04.j', differentiating_form='process_variant')
    document = dict(id='PURCHASE-ORDER-BEHAVIORS-U390', status='proposed', source_refs=['U390','U389','ELM235','CMP146'], capability_id='D04.j', baseline_sha256=before, proposed_definition='Prendre en charge les commandes d’achat de biens ou de prestations adressées aux fournisseurs, maintenir les attentes et les évolutions autorisées et rapprocher les réalisations pour connaître le reste à satisfaire.', decomposition_rationale='Les parcours changent la nature de l’attendu, la destination, les dépendances entre commandes et les preuves de réalisation : apport en stock, livraison directe au client, prestation. Cette différence métier justifie la décomposition sans recopier le cycle de vie commun.', proposals=proposals, additional_candidate=dict(name='Consignment Procurement', status='boundary_to_examine', source_ids=['PO-S4'], rationale='Acquérir du stock déjà détenu physiquement sous propriété fournisseur ; différence métier pertinente.', unresolved='Séparer gestion du stock fournisseur et acte d’acquisition. Ne pas placer tout le cycle de consignation sous Purchase Order ni présumer l’applicabilité Beaumanoir.'), exclusions=['Brouillon, affermissement, gel, attente et annulation restent dans Order Lifecycle Management.', 'Livraisons partielles et échéanciers restent des explications communes tant qu’un bénéfice de décomposition supplémentaire n’est pas démontré.', 'Un remplacement à la suite d’un Supplier Return est une origine de besoin ; il ne justifie pas seul un comportement d’achat supplémentaire.', 'Sous-traitance industrielle et achats indirects généraux non instruits dans cette passe ; ne pas étendre implicitement FLOW à tout Procurement.'], market_comparisons=[dict(comparison_ref='CMP146', source_ids=['PO-S1','PO-S2','PO-S3'], relationship='Recouvrement partiel', similarities='Biens et services achetés ; livraison directe avec lien achat/vente ; preuve de prestation réalisée.', differences='Les éditeurs décrivent documents, processus et fonctions. FLOW propose trois comportements sous une capacité d’action sans adopter leur taxonomie produit.', flow_position='Socle de trois variantes proposé ; frontière Service Procurement / Service Order explicitée.', status='proposed'),dict(comparison_ref='CMP146',source_ids=['PO-S4'],relationship='Piste de décomposition',similarities='Acquisition dissociée de la réception physique.',differences='Consignation traverse plusieurs capacités et ne se résume pas au Purchase Order.',flow_position='Candidat conservé à instruire ; aucun quatrième comportement adopté.',status='under_review')], sources=sources, catalog_changed=False)
    target.write_text(dumps(document), encoding='utf-8')
    append('marche/elements.md', '''### ELM235

U390 — 18 septembre 2026. Microsoft Dynamics 365 SCM : Create purchase orders (Adding purchase order lines), Direct deliveries (introduction, dates, adresses et entrepôt), Set up consignment (Inventory ownership change journal), pages primaires ouvertes. SAP S/4HANA on-premise : Manage Service Entry Sheets - Lean Services et Planned and Unplanned Services, passages primaires indexés consultés ; édition 2025 FPS01 (Feb 2026) affichée sur cette dernière, ouvertures directes sans texte exploitable.

Sources, URL, localisateurs et limites conservés dans modeles/backlog/purchase-order-behaviors.yaml, PO-S1 à PO-S4. Nature : processus, documents et fonctions produit. Distinctions biens/prestations, livraison directe et acquisition de stock consigné. Aucune taxonomie de capacités équivalente ni preuve Beaumanoir ; synthèses sans reproduction intégrale.''')
    append('marche/comparaisons.md', '''### CMP146

U390 — Codex, 18 septembre 2026 ; Purchase Order D04.j au backlog courant, empreinte dans modeles/backlog/purchase-order-behaviors.yaml. ELM235 : recouvrement partiel avec les processus achat Microsoft et SAP.

Proposition de Stock Procurement, Direct Delivery et Service Procurement : attentes et preuves distinctes, coordination achat/vente pour le direct, réalisation d’une prestation pour le service. La définition actuelle limitée aux biens est à élargir explicitement si la proposition est adoptée. L’achat relève de D04 ; la sollicitation et le suivi opérationnel relèvent de D06, sans imposer un achat pour tout appel de service. Stock et finance gardent leurs responsabilités.

Consignment Procurement reste un candidat : la documentation Microsoft distingue acquisition et détention physique, mais ne justifie pas d’attribuer toute la consignation à D04. Les libellés, définitions et rattachements proposés restent à valider ; aucun catalogue modifié. Périmètre limité à ce prochain sujet, aucune exhaustivité de tous les modes d’achat revendiquée.''')
    append('JOURNAL.md', '''## 2026-09-18 — U390 : proposition des comportements Purchase Order

Après les retours, trois variantes proposées avec comparaison Microsoft/SAP ELM235/CMP146 : stock, livraison directe et prestations. Consignation conservée comme candidat à frontière ouverte. Définition actuelle centrée sur les biens à élargir explicitement si accord. Catalogue et publications inchangés.''')
    assert sha256(model.read_bytes()).hexdigest() == before
    assert read(target)['status']=='proposed'
    print('U390: three proposals and one candidate recorded; catalog unchanged.')


if __name__ == '__main__':
    main()

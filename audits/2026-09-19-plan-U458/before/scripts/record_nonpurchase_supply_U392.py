"""Document the order needed for non-purchase consignment supply."""
from scripts.apply_supplier_return_U387 import ROOT, save, append


def main():
    assert not (ROOT/'modeles/backlog/nonpurchase-supply-order-review.yaml').exists()
    append('connaissance/01-contributions-utilisateur.md','''## U392

**id**

U392

**date**

2026-09-18

**titre**

Examiner l’Order d’approvisionnement sans achat

**texte**

En effet, il peut y avoir un approvisionnement dans les stocks sans acte d'achat. Il ne manque pas un Procurement Order pour gérer ça ? Que dit le marché ?

**contexte et portée**

Question de modélisation dans la continuité de U391 : distinguer la demande et le suivi de l’apport des droits de propriété sur le stock. Procurement Order est un nom interrogé, pas adopté. Comparaison marché demandée ; aucun renommage de Purchase Order ni nouvelle capacité acquis. L’intégration des trois comportements validés U391 reste à terminer et contrôler indépendamment de cet arbitrage.''')
    sources=[
        dict(id='NP-S1',vendor='Microsoft',product='Dynamics 365 SCM',title='Set up consignment',url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment',edition='Documentation évolutive',locator='Consignment replenishment orders ; Overview of the consignment process',access='Page primaire ouverte',finding='Consignment replenishment order demande et suit les quantités à livrer dans un intervalle de dates ; le fournisseur conserve la propriété à réception. Le traitement de changement de propriété génère ensuite un Purchase Order.',limit='Document produit illustré en production ; ne justifie pas une capacité Procurement Order générique couvrant tous les apports.'),
        dict(id='NP-S2',vendor='SAP',product='S/4HANA on-premise',title='Item Category',url='https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/a37eb65334e6b54ce10000000a174cb4.html',edition='Documentation évolutive, édition non confirmée dans le passage lu',locator='Table des catégories : Consignment',access='Passage primaire indexé consulté ; ouverture directe sans texte exploitable',finding='Une ligne de Purchase Order de catégorie Consignment exige une réception de marchandises mais pas une réception de facture sur cette ligne.',limit='Le nom de l’objet ERP ne prouve pas un achat/transfert de propriété à sa création ; catégorie de ligne, pas nouvelle capacité. Aucun comportement légal universel déduit.'),
        dict(id='NP-S3',vendor='Oracle',product='Fusion Cloud SCM',title='Consigned Inventory',url='https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faims/consigned-inventory.html',edition='25D',locator='Consignment Order ; Ship and Receive Items',access='Page primaire ouverte',finding='Consignment Order demande les expéditions avec quantités, lieux et dates selon l’accord ; les biens reçus restent propriété fournisseur.',limit='Intitulé fonctionnel du parcours ; ne démontre pas un nouvel objet technique indépendant du Purchase Order.'),
        dict(id='NP-S4',vendor='Oracle',product='Fusion Cloud SCM',title='How Supply Chain Orchestration Works',url='https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26a/fauco/how-supply-orchestration-works.html',edition='26A',locator='Transform and assign request ; Orchestrate supply order ; Fulfill',access='Page primaire ouverte',finding='Un Supply Order orchestre plusieurs modes, notamment achat, fabrication et transfert, avec leurs documents d’exécution.',limit='Plus large que l’apport consigné ; empièterait sur les responsabilités d’orchestration si recopié comme simple type d’Order FLOW.'),
    ]
    for s in sources:s['consulted_on']='2026-09-18'
    save('modeles/backlog/nonpurchase-supply-order-review.yaml',dict(id='NONPURCHASE-SUPPLY-ORDER-U392',status='proposed',source_refs=['U392','U391','ELM237','CMP148'],problem='Représenter une demande fournisseur d’apport de stock sans la confondre avec l’acquisition, l’exécution logistique ou la gestion durable du stock consigné.',existing_coverage='Transfer Order couvre déjà les transferts ; Supplier Return et les retours peuvent également conduire à des apports. Ne pas inventer un manque pour tous les flux sans achat.',recommendation=dict(name='Consignment Replenishment Order',parent_id='D04',kind='capability',definition='Demander et suivre un apport de stock fournisseur sous consignation : produits, quantités, lieux, dates et reste à recevoir, sans confondre cette demande avec un achat.',status='proposed_not_created',rationale='Nommage natif Microsoft correspondant au besoin précis démontré ; ordre d’apport distinct de la gestion du régime de stock.',benefit='Suivre une livraison attendue sans créer un achat fictif ni rendre disponible un stock non reçu.',boundary='D01 gère l’état et le régime du stock ; D04 suit la demande d’apport ; D06 orchestre les prestations ; D03/D05 décident du besoin ou de la réponse selon leur finalité. Lifecycle, Structuring et Archiving restent transverses.',naming_limit='Replenishment dans cet intitulé éditeur couvre la demande d’alimentation du stock consigné, y compris son premier apport ; ne fusionne pas Initial Stocking et Replenishment Decision de FLOW.'),alternatives=[dict(name='Procurement Order',assessment='Pas de convention générique indépendante de Purchase Order établie par les sources consultées. Risque de chevauchement achat/apport/prestation ; nom non adopté.'),dict(name='Purchase Order avec variante de consignation',assessment='Approche documentaire SAP compatible avec plusieurs régimes, mais contredirait notre séparation métier U391 si la distinction achat/apport disparaît. Aucun rejet technique de SAP.'),dict(name='Supply Order',assessment='Oracle documente un objet d’orchestration plus large couvrant achat/fabrication/transfert ; pas un simple synonyme du manque identifié.')],market_comparisons=[dict(comparison_ref='CMP148',status='proposed',similarities='Demande fournisseur et suivi des quantités/dates peuvent précéder toute acquisition ; mécanisme explicite chez Microsoft et Oracle, catégorie de ligne chez SAP.',differences='Les éditeurs ne retiennent pas un nom et une structure uniques. Document, catégorie de ligne, capacité et objet d’orchestration ne sont pas équivalents.',flow_position='Proposer un type d’Order ciblé dans D04 ; conserver séparément la gestion du régime de stock proposée U391. Aucun nouveau nœud ni comportement créé.',source_ids=[s['id'] for s in sources])],sources=sources,catalog_changed=False))
    append('marche/elements.md','''### ELM237

U392 — 18 septembre 2026. Sources primaires NP-S1–4 dans modeles/backlog/nonpurchase-supply-order-review.yaml : Microsoft Consignment replenishment orders (page Set up consignment ouverte), SAP S/4HANA Item Category / Consignment (passage indexé, portail sans texte), Oracle Fusion 25D Consignment Order et 26A Supply Order orchestration (pages ouvertes).

Nature : document de demande, catégorie de ligne et objet d’orchestration. Distinction entre apport physique, propriété et acquisition ; aucun consensus sur un Procurement Order générique démontré. Les noms et localisateurs natifs, limites et dates sont conservés dans l’annexe.''')
    append('marche/comparaisons.md','''### CMP148

U392 — Codex, 18 septembre 2026 ; nouveau type d’Order à instruire sous D04, en lien avec la gestion de stock proposée CMP147. ELM237 soutient un besoin de demande d’apport consigné distinct de l’achat, mais les réalisations divergent : Consignment Replenishment Order Microsoft, Purchase Order avec catégorie Consignment SAP, Consignment Order dans le parcours Oracle.

Recommandation de nom ciblé Microsoft pour FLOW ; pas de Procurement Order générique sans autres cas qui justifient ce périmètre. L’objet Supply Order Oracle est plus large et orchestre achat, fabrication et transfert : ne pas le recopier comme simple type d’Order. D01 conserve le régime de stock et D06 l’exécution. Aucun nouveau nœud créé, noms et rattachements à valider.''')
    append('JOURNAL.md','''## 2026-09-18 — U392 : apport fournisseur sans achat

Comparaison Microsoft/SAP/Oracle ELM237/CMP148 : demande d’apport distincte du régime de stock et de l’acquisition. Consignment Replenishment Order proposé comme type ciblé D04 ; Procurement Order générique et Supply Order comparés avec leurs limites. Aucun nouveau nœud ou renommage de Purchase Order.''')
    print('U392 recorded; no catalog changes.')


if __name__=='__main__':
    main()

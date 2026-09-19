"""Persist the intent-led architecture principle and its market limits."""
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read


def main():
    target='modeles/backlog/order-intent-principles.yaml'
    assert not (ROOT/target).exists()
    out=ROOT/'audits/2026-09-18-order-intent-U393'
    assert not out.exists()
    model=ROOT/'modeles/backlog/model.yaml'
    before=sha256(model.read_bytes()).hexdigest()
    append('connaissance/01-contributions-utilisateur.md','''## U393

**id**

U393

**date**

2026-09-18

**titre**

Modéliser les demandes selon les intentions et relations entre parties

**texte**

Mon avis et mon intention en tant qu'architecte :

SAP a conçu ses order pour piloter les opérations logistiques et les documents nécessaires à la conformité. Voilà pourquoi chez SAP, c'est un Purchase Order avec un flag consignment car j'ai un seul type d'order pour gérer le source-to-stock.

Dans un SI moderne orienté processus / Case Management, on concoit les demandes par rapport aux intentions et aux rapport entre les parties prenantes. LE consignement n'est pas juste une manière de gérer la comptabilité du stock. Mon stock est vue dans ce type de contrat comme un espace de stockage distant vis à vis de mon fournisseur qu'il loue. Je ne lui achète pas du stock, je lui loue un espace. La différence est que ce n'est pas lui qui "pousse" la marchandise, on est à flux tiré, c'est à dire que ce sont mes ventes qui impliquent un réassort du stock. Dans un esprit process oriented, microsoft a l'approche la plus moderne.

Qu'en penses tu ? Si tu es ok cette logique doit être consignée (c'est le case de le dire :)).

**contexte et portée**

Laurent explicite un principe cible d’architecture : partir des intentions et des relations entre parties pour concevoir les demandes et leur traitement orienté processus/Case Management. Il demande de mémoriser cette logique si Codex la partage. Codex retient ce principe et distingue la description de l’offre envisagée (stockage pour le fournisseur, rémunération/location et réassort tiré par les ventes) de la définition générale de la consignation et d’une pratique Beaumanoir prouvée. L’explication historique de SAP et le classement général de modernité restent des appréciations, non des faits démontrés. La comparaison conforte une meilleure adéquation sémantique de la séparation Microsoft pour le cas FLOW. Aucun nouveau nom, nœud, workflow universel ou découpage logiciel validé implicitement.''')
    out.mkdir()
    for relative in ['AGENTS.md','modeles/backlog/consignment-inventory-review.yaml','modeles/backlog/nonpurchase-supply-order-review.yaml']:
        (out/(ROOT/relative).name).write_bytes((ROOT/relative).read_bytes())
    sources=[
        dict(id='OI-S1',vendor='Microsoft',product='Dynamics 365 SCM',title='Set up consignment',url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment',edition='Documentation évolutive, mise à jour affichée 2026-05-06',locator='Overview of the consignment process ; Consignment replenishment orders',access='Page primaire ouverte',finding='Demande d’apport distincte du Purchase Order généré au changement de propriété ; quantités et dates selon demande prévue/réelle.',limit='L’exemple comporte une création manuelle en contexte production ; il ne prouve ni Case Management généralisé, ni location d’espace obligatoire, ni réassort retail strictement proportionnel aux ventes.'),
        dict(id='OI-S2',vendor='SAP',product='S/4HANA Cloud Public Edition',title='Exploring the Supplier Consignment (2LG) Scenario',url='https://learning.sap.com/courses/handling-special-stocks-and-physical-inventory-in-sap-s-4hana-cloud-public-edition/exploring-the-supplier-consignment-2lg-scenario_f7d023c2-e7c4-4af1-aaed-084fd946e5fa',edition='Formation évolutive, version non affichée',locator='Create Consignment Purchase Order ; Regular Consignment Ordering ; Consignment Withdrawals',access='Page primaire ouverte',finding='Catégorie de ligne Consignment, propriété fournisseur conservée ; demandes générables par MRP selon les besoins. Retraits, vente, transfert au stock propre et rebut sont distingués.',limit='Réutilisation de document ERP attestée ; motivations historiques de conception/conformité et incapacité au pilotage par les besoins non démontrées. Aucun droit de destruction déduit des options du produit.'),
        dict(id='OI-S3',vendor='SAP',product='Business Network for Supply Chain',title='Supplier-Managed Inventory',url='https://help.sap.com/docs/business-network-for-supply-chain/business-network-for-supply-chain-integration-and-configuration/e6fe41e52bef4c4ebcb82fab3d6b1dfc.html',edition='Documentation évolutive, version non affichée',locator='Détermination des besoins de réapprovisionnement',access='Passage primaire indexé lu ; ouverture directe sans texte exploitable',finding='Le fournisseur peut déterminer le réassort selon demande brute, stock et min/max.',limit='Illustration que signal de demande et acteur de décision sont deux axes distincts ; ne valide pas un VMI pour FLOW.'),
    ]
    for source in sources:source['consulted_on']='2026-09-18'
    principle='Modéliser une demande par son intention métier, les parties et leurs rôles, la relation ou l’accord applicable, les engagements attendus et le résultat à obtenir. Décrire ensuite son traitement et ses adaptations ; les documents ERP, mouvements logistiques et écritures sont des réalisations ou effets à relier, pas l’autorité qui fixe la sémantique de la demande.'
    context=dict(status='target_intent_expressed_by_user_not_installed_fact',source_refs=['U393'],perspective='Le fournisseur dispose d’un espace de stockage distant dans le réseau du distributeur ; le distributeur propose une offre de mise à disposition de cet espace.',commercial_model='Location/rémunération d’espace évoquée par Laurent ; nature précise, assiette, montant et conditions non définis. Ne pas la transformer en condition universelle de consignation.',ownership='L’apport en consignation n’est pas un achat de marchandises ; un éventuel changement de propriété ultérieur reste distinct, selon le montage retenu.',replenishment='Les ventes et l’évolution du besoin déclenchent ou alimentent le réassort demandé dans la cible décrite ; pas de poussée fournisseur unilatérale présumée.',limits=['Aucun automatisme une vente = une unité immédiatement commandée.', 'Réassort tiré par la demande ne désigne pas, à lui seul, l’acteur responsable du calcul ou de la décision.', 'Ne pas déduire de VMI, de transfert automatique à chaque vente, de tarif de stockage ou de responsabilité assurantielle non explicités.', 'Stockage, propriété, pilotage du réassort et rémunération sont des dimensions séparées de l’offre.'])
    comparison=dict(comparison_ref='CMP149',status='editorial_comparison',common='Microsoft distingue explicitement les intentions d’apport et d’acquisition. SAP conserve des effets métier distincts dans une structure documentaire commune et peut générer des apports selon les besoins.',difference='La séparation Microsoft est plus directement alignée sur le vocabulaire métier FLOW pour ce cas. Ni l’existence de deux objets ni une catégorie de ligne ne mesure à elle seule la maturité processus ou Case Management de l’éditeur.',flow_position='Adopter le principe de modélisation par intentions exprimé U393 ; préférence locale justifiée pour la séparation des demandes, sans classement général des éditeurs.',source_ids=[s['id'] for s in sources])
    save(target,dict(id='ORDER-INTENT-PRINCIPLES-U393',as_of='2026-09-18',status='principle_recorded_from_user',source_refs=['U393','U391','U392','ELM238','CMP149'],principle=principle,review=dict(adopted_scope='Direction architecturale exprimée et demande de mémorisation U393 : intentions et relations entre parties avant choix des documents.',editorial_scope='Formulation, grille d’analyse, exemples et comparaison marché rédigés par Codex ; noms de capacités encore proposés non validés par extension.'),analysis_grid=['Quelle intention et quel résultat métier ?', 'Qui demande, à qui, et sous quels rôles ?', 'Quel accord, quels droits et engagements ?', 'Quels événements rendent la demande satisfaite ou imposent une adaptation ?', 'Quels services et capacités sont mobilisés ?', 'Quels documents et effets matérialisent cette intention dans chaque réalisation ?'],architecture_boundaries=['Un document ERP peut porter plusieurs intentions métier ; plusieurs documents peuvent réaliser une intention. Ne pas calquer capacité ou case sur une table ERP.', 'Des opérations physiques communes ne fusionnent pas des demandes dont intentions ou engagements diffèrent.', 'Les couches transactionnelle Supply et processus Business Services restent distinctes ; ne pas imposer un Order universel, un workflow unique, un case par document ou un logiciel.', 'Réutiliser Lifecycle, Structuring et Archiving ; ne pas créer un comportement pour chaque étape technique.', 'Conserver les accords antérieurs Purchase Order ; les noms Consigned Inventory Management et Consignment Replenishment Order demeurent proposés.'],consignment_target=context,market_comparisons=[comparison],sources=sources,catalog_changed=False))
    for relative in ['modeles/backlog/consignment-inventory-review.yaml','modeles/backlog/nonpurchase-supply-order-review.yaml']:
        d=read(ROOT/relative)
        d['source_refs']=list(dict.fromkeys(d['source_refs']+['U393','CMP149']))
        d['architecture_U393']=dict(principle_ref=target,status='direction_recorded_no_new_name_adopted',intent='Distinguer service de stockage offert au fournisseur, demande d’apport et éventuelle acquisition.',context=context)
        d['market_comparisons'].append(comparison)
        # The comparison sources resolve locally as well as in the principle register.
        d['sources'].extend(sources)
        save(relative,d)
    agents=ROOT/'AGENTS.md'
    text=agents.read_text(encoding='utf-8')
    marker='- Objets métier, documents et événements restent distincts'
    instruction='- **Demandes par intention (U393)** : partir de l’intention métier, des parties/rôles, de leur relation ou accord, des engagements et du résultat attendu ; décrire ensuite le traitement et ses adaptations. Les documents ERP et mouvements ne dictent pas le découpage métier. Un document commun peut réaliser plusieurs intentions ; aucun Order, case ou workflow universel imposé. Pour la consignation, distinguer offre de stockage au fournisseur, demande d’apport, régime de propriété, réassort et acquisition éventuelle. Location d’espace et flux tiré par les ventes décrivent l’intention FLOW exprimée, pas toute consignation ni un existant prouvé. Principe, portées et comparaison : [order-intent-principles.yaml](modeles/backlog/order-intent-principles.yaml).\n'
    assert marker in text
    agents.write_text(text.replace(marker,instruction+marker,1),encoding='utf-8')
    append('marche/elements.md','''### ELM238

U393 — 18 septembre 2026. Microsoft Dynamics 365 SCM, Set up consignment (page mise à jour 2026-05-06, ouverte) ; SAP Learning S/4HANA Cloud Public Edition, Exploring the Supplier Consignment (2LG) Scenario (formation évolutive ouverte) ; SAP Business Network, Supplier-Managed Inventory (passage primaire indexé, portail sans texte exploitable). URL, passages et limites dans modeles/backlog/order-intent-principles.yaml, OI-S1–3.

Constats : Microsoft sépare demande d’apport et achat lors du transfert ; SAP réutilise une catégorie de ligne en conservant les effets de propriété et peut générer les demandes selon les besoins MRP. L’acteur du réassort et le signal de demande sont deux axes distincts. Aucune motivation historique exclusive de SAP ni maturité Case Management globale démontrée ; la location d’espace rémunérée est l’intention FLOW décrite par Laurent, pas une propriété universelle tirée des sources.''')
    append('marche/comparaisons.md','''### CMP149

U393 — Codex, 18 septembre 2026 ; appui méthodologique et comparaison partielle du principe de demande par intention. ELM238 : séparation documentaire Microsoft directement lisible pour les intentions d’apport/acquisition ; SAP porte des distinctions métier dans une structure documentaire commune et propose aussi une alimentation selon les besoins.

Retenir pour FLOW les intentions, relations et engagements comme point de départ. La préférence Microsoft porte sur cette adéquation sémantique précise ; aucune supériorité globale, ancienneté explicative ou réalisation Case Management déduite du seul nombre de types de documents. La cible décrite assemble stockage pour le fournisseur, régime de propriété et réassort tiré par les ventes ; rémunération/location est une condition de l’offre à préciser, pas la définition générale de consignation. Pas de création de capacité, changement de nom ou décomposition acquis par extension.''')
    append('JOURNAL.md','''## 2026-09-18 — U393 : architecture des demandes par intention

Principe mémorisé dans AGENTS.md et order-intent-principles.yaml ; annexes de consignation/apport reliées à cette direction. Offre de stockage/location et réassort tiré par les ventes enregistrés comme intention exprimée, distincte de l’existant et de la définition générale de consignation. Comparaison Microsoft/SAP ELM238/CMP149, avec limites sur les motivations historiques et le jugement de modernité. Catalogue métier inchangé.''')
    assert sha256(model.read_bytes()).hexdigest()==before
    (out/'README.md').write_text('# U393 — demandes par intention\n\nPrincipe canonique : modeles/backlog/order-intent-principles.yaml. Captures des instructions et annexes antérieures conservées ici. Aucun nœud, relation ou champ du catalogue métier modifié.\n\nEmpreinte du catalogue conservée : `'+before+'`.\n',encoding='utf-8')
    print('U393 recorded: architectural principle and scoped offer; business catalog unchanged.')


if __name__=='__main__':
    main()

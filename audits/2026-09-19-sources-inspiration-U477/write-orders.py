"""Delta éditorial U477 : textes écrits fiche par fiche, sérialisation seulement."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.structured_io import read, dumps, write_text_if_changed

ROOT = Path(__file__).parent
INPUT = read(ROOT / 'orders-input.yaml')
OLD = {n['id']: n.get('fields', n) for k in ('nodes', 'terms') for n in INPUT[k]}
COL = {n['id']: k for k in ('nodes','terms') for n in INPUT[k]}
S = {}

def src(key, vendor, product, title, url, version, locator, concept, scope, approach, finding, limits='Documentation primaire consultée ; périmètre du produit, sans preuve de déploiement Beaumanoir.'):
    S[key] = dict(vendor=vendor, product=product, source_title=title, source_url=url, source_version=version, source_locator=locator, consulted_on='2026-09-19', concept_name=concept, scope_summary=scope, approach_summary=approach, finding=finding, evidence_limits=limits)

MS='https://learn.microsoft.com/en-us/dynamics365/'
SCM=MS+'supply-chain/'
OC='https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/'
EV='Documentation évolutive consultée le 19 septembre 2026'
SAP='Cours SAP Learning ; édition non indiquée dans le passage'
src('pos','Microsoft','Dynamics 365 Commerce','Customer orders in point of sale (POS)',MS+'commerce/customer-orders-overview',EV,'Typical scenarios ; Order fulfillment ; Editing customer orders','Customer order','Vente en magasin, livraison ou retrait différé.','Choisir le parcours par ligne et suivre la commande.','La commande peut être expédiée ou retirée, dans un autre magasin ou plus tard ; couverture Commerce/POS, pas tout le B2B.')
src('store','Microsoft','Dynamics 365 Commerce','Store order fulfillment',MS+'commerce/order-fulfillment-overview',EV,'Accepting orders ; Shipping orders ; Picking up orders','Order fulfillment','Préparation, expédition et retrait depuis un magasin.','Enchaîner les opérations selon le mode de remise.','Le retrait effectivement effectué et l’expédition constituent des actions distinctes ; retrait partiel possible.')
src('direct','Microsoft','Dynamics 365 SCM','Direct deliveries',SCM+'sales-marketing/direct-deliveries',EV,'Introduction ; Deliver a sales order directly ; Update delivery dates','Direct delivery','Marchandises livrées directement par le fournisseur au client.','Relier lignes de vente et d’achat.','Les dates et quantités concernées restent coordonnées ; les marchandises ne passent pas physiquement par le dépôt propre.')
src('inter','Microsoft','Dynamics 365 SCM','Intercompany orders and return orders',SCM+'sales-marketing/intercompany-orders-and-return-orders',EV,'Introduction ; two-legged and three-legged intercompany order chains','Intercompany order','Vente et achat entre sociétés d’un groupe.','Relier les commandes de chaque société.','Les chaînes peuvent associer une vente externe à un achat et une vente internes ; relation juridique et livraison se combinent.')
src('pocreate','Microsoft','Dynamics 365 SCM','Create purchase orders',SCM+'procurement/purchase-order-creation',EV,'Create a purchase order ; Purchase order lines','Purchase order','Biens et services attendus d’un fournisseur.','Préciser fournisseur, lignes, quantités et dates.','L’achat couvre des produits et des services ; l’origine peut être une demande, un plan, un accord ou une vente directe.')
src('po','Microsoft','Dynamics 365 SCM','Purchase order overview',SCM+'procurement/purchase-order-overview',EV,'Purchase order types ; Purchase order statuses','Purchase order','Commande fournisseur, réception et facturation.','Suivre plusieurs statuts et documents associés.','L’état des quantités, le statut documentaire et l’approbation ne se confondent pas.')
src('consign','Microsoft','Dynamics 365 SCM','Set up consignment',SCM+'inventory/consignment',EV,'Consignment replenishment orders ; Ownership change journals','Consignment replenishment order','Apport fournisseur conservant sa propriété.','Suivre l’arrivée, puis traiter séparément le changement de propriétaire.','La réception de consignation n’est pas un achat ; le changement de propriété déclenche ensuite un Purchase Order.')
src('towh','Microsoft','Dynamics 365 SCM','Set up warehouses for transfer orders',SCM+'warehousing/transfer-orders-warehouse',EV,'Plan replenishment for warehouses ; Transport days','Planned transfer order','Réapprovisionnement d’un dépôt par un autre.','Déduire les transferts des besoins et des délais.','La planification peut générer des ordres de transfert selon entrepôt de couverture et jours de transport.')
src('supply','Oracle','Supply Chain Orchestration','Overview of Supply Chain Orchestration',OC+'26b/fauco/overview-of-supply-orchestration.html','Oracle Fusion Cloud SCM 26B','Supply requests ; Supply orders ; Drop Ship ; Changes','Supply order','Approvisionnement par achat, fabrication ou transfert.','Relier demande d’approvisionnement et documents de réalisation.','Supply order est un objet d’approvisionnement Oracle ; son nom ne désigne pas toutes les commandes du vocabulaire FLOW.')
src('b2b','Oracle','Supply Chain Orchestration','Use Supply Chain Orchestration in Your Back-to-Back Flows',OC+'26b/fauco/how-orchestration-processes-back-to-back-flows.html','Oracle Fusion Cloud SCM 26B','Buy ; Transfer ; Return Sales Orders ; Contract Manufacturing','Back-to-back flow','Approvisionnement lié à une commande client.','Conserver le lien entre demande et achat, fabrication ou transfert.','La ressource est procurée pour la vente identifiée ; le retour d’un produit neuf inutilisé peut rejoindre le disponible.')
src('rebal','Oracle','Replenishment Planning','Overview of Inventory Rebalancing',OC+'26b/faurp/overview-of-inventory-rebalancing.html','Oracle Fusion Cloud SCM 26B','Introduction ; Planned orders ; Release','Inventory rebalancing','Excédents et manques entre emplacements.','Proposer puis libérer des transferts de rééquilibrage.','Les stocks excédentaires couvrent les emplacements en manque ; la documentation porte surtout la décision de planification.')
src('to','Microsoft','Intelligent Order Management','Integrate transfer orders',MS+'intelligent-order-management/integrate-transfer-orders',EV,'Transfer order information ; Inbound and outbound transfer orders','Transfer order','Déplacement entre dépôts avec dates et quantités.','Suivre départs, réceptions et liens avec les ventes.','Les commandes de transfert portent les deux lieux et leur progression ; elles peuvent être visibles depuis la demande client.')
src('merkal','Nextail','Inventory planning','Merkal footwear inventory planning','https://nextail.co/customer/merkal-footwear-inventory-planning/',EV,'End-of-season transfers ; consolidation and size availability','Store transfers','Regroupement du stock et des tailles en fin de saison.','Adapter les transferts aux possibilités de vente.','Le cas Merkal évoque une meilleure consolidation et disponibilité des tailles.','Témoignage publié par le fournisseur ; mécanisme illustré, aucun résultat chiffré ni causalité indépendante retenus.')
src('dispo','Microsoft','Dynamics 365 SCM','Specify how to dispose of returned items',SCM+'sales-marketing/specify-how-to-dispose-of-returned-items',EV,'Disposition codes ; Disposition actions','Return disposition','Sort du produit retourné et compensation.','Associer un résultat de traitement au retour.','Credit, Scrap, Replace et Return to customer ont des effets distincts ; un code Repair ne prouve pas un parcours complet de réparation.')
src('bcret','Microsoft','Dynamics 365 Business Central','Process purchase returns or cancellations',MS+'business-central/purchasing-how-process-purchase-returns-cancellations',EV,'Purchase return orders ; Create a replacement purchase order ; Credit memos','Purchase return order','Renvoi fournisseur, avoir et remplacement éventuel.','Relier retour, correction et nouvel achat de remplacement.','Une commande de retour permet de suivre le renvoi ; le remplacement peut créer une commande d’achat séparée.')
src('credit','Oracle','Inventory Management','Return to Supplier for Credit Only','https://docs.oracle.com/en/cloud/saas/readiness/scm/25a/inv25a/25A-inventory-wn-f35542.htm','Oracle Cloud Readiness 25A','Business Benefits ; Steps to Enable ; Tips and Considerations','Return for credit only','Retour fournisseur sans marchandise de remplacement.','Attendre le crédit sans rouvrir la quantité d’achat.','L’option empêche la réouverture de la commande pour un remplacement ; des restrictions de flux sont indiquées.')
src('gp','Microsoft','Dynamics GP','Returns Management', 'https://learn.microsoft.com/en-us/dynamics-gp/distribution/returnsmanagement',EV,'RMA types ; RTV types ; Repair and return ; Creating an RTV from an RMA','RMA / RTV','Retours client et fournisseur avec suites distinctes.','Relier crédit, remplacement, réparation et restitution.','RTV Repair and Return attend le même bien ; un retour fournisseur peut être créé à partir du retour client.','Documentation d’un produit différent de Dynamics 365 ; nommage et mécanismes propres, sans équivalence de couverture supposée.')
src('repairplan','Oracle','Service Parts Planning','Service Planning Concepts','https://docs.oracle.com/cd/E18727-01/doc.121/e13338/T515331T515340.htm','Oracle E-Business Suite 12.1','Repair Return Pull ; Repair Return Push ; Repair delays','Repair return','Pièces défectueuses envoyées en réparation.','Planifier transfert, réparation et retour des pièces utilisables.','Le délai de réparation inclut les mouvements ; modes de retour, prépositionnement et échange sont distingués.','Source de planification des pièces ; ne démontre pas à elle seule le suivi opérationnel de chaque bien sérialisé.')
src('bcarchive','Microsoft','Dynamics 365 Business Central','Archive documents',MS+'business-central/across-how-to-archive-documents',EV,'Archive sales and purchase documents ; Restore ; Retention policies','Document archive','Versions des documents de vente et d’achat.','Conserver, consulter et parfois restaurer une version.','L’archivage peut garder plusieurs versions ; restauration et rétention restent soumises à conditions.')
src('archive','Microsoft','Dynamics 365 finance and operations','Archive sales orders',MS+'fin-ops-core/dev-itpro/sysadmin/archive-so',EV,'Prerequisites ; Long term retention ; History','Sales order archive','Commandes de vente éligibles hors usage courant.','Sélectionner les commandes entièrement facturées puis conserver leur histoire.','La fonction d’archivage exclut certains flux, notamment intercompany ; archive historique et opération courante sont séparées.')
src('merge','Infor','LN','Commingling purchase orders','https://docs.infor.com/ln/10.7/en-us/lnolh/help/td/onlinemanual/000321.html','Infor LN 10.7','Commingling purchase orders ; Conditions ; Results','Commingling','Fusion d’achats compatibles.','Créer une commande résultante avec renvoi aux origines.','Des commandes Created compatibles sont réunies ; les détails d’origine subsistent et des conditions de prix peuvent changer.')
src('set','Oracle','Order Management','Ship Order Lines in Shipment Sets',OC+'26a/fauom/ship-order-lines-in-shipment-sets.html#s20054853','Oracle Fusion Cloud SCM 26A','Shipment sets ; Examples ; Guidelines','Shipment set','Lignes de vente à expédier ensemble.','Conserver les lignes, imposer des conditions communes.','Ordinateur, écran, souris et clavier peuvent partager date et expédition sans nécessairement partager un colis.')
src('setguide','Oracle','Order Management','Guidelines for Managing Shipment Sets',OC+'26a/faiom/guidelines-for-managing-shipment-sets.html','Oracle Fusion Cloud SCM 26A','Shipment set attributes ; Shippable and nonshippable lines','Shipment set','Contraintes collectives de lignes à satisfaire ensemble.','Coordonner les étapes selon les attributs communs.','Un ensemble peut attendre ses lignes ; les restrictions diffèrent selon les parcours, notamment dropship.')
src('firm','Microsoft','Planning Optimization','Firm planned orders',SCM+'master-planning/planning-optimization/planned-order-firming',EV,'Manual firming ; Automatic firming ; Grouping','Planned order firming','Proposition planifiée transformée en ordre effectif.','Affermir manuellement ou selon un horizon et des règles.','L’affermissement produit des achats, transferts ou fabrications ; le regroupement par fournisseur peut réunir les achats.')
src('plans','Microsoft','Master planning','Master plans',SCM+'master-planning/master-plans',EV,'Freeze time fence ; Firming time fence','Freeze / firming time fence','Horizon de protection et horizon d’affermissement.','Paramétrer séparément deux effets du plan.','Freeze empêche les modifications planifiées dans un horizon ; Firming y transforme les propositions en commandes.')
src('keep','Microsoft','Planning Optimization','Keep supply for confirmed demand',SCM+'master-planning/planning-optimization/keep-supply-for-confirmed-demand',EV,'What data is preserved ; Confirmed demand ; Examples','Keep supply for confirmed demand','Chaîne de ressources d’une demande confirmée.','Préserver les liens et certains résultats lors d’un nouveau plan.','La protection de la couverture conserve davantage qu’une date ; certains ajustements restent possibles.','Fonction conditionnée à la version et à la configuration documentées ; n’établit pas un gel universel de tous les champs.')
src('approved','Microsoft','Planning Optimization','Approve planned orders',SCM+'master-planning/planning-optimization/approved-planned-order',EV,'View and edit status ; Approve planned orders','Approved planned order','Proposition planifiée conservée pour affermissement.','Protéger l’ordre approuvé contre sa recréation.','Approved conserve un ordre planifié ; ce n’est pas encore un achat ferme.')
src('approve','Microsoft','Dynamics 365 SCM','Approve and confirm purchase orders',SCM+'procurement/purchase-order-approval-confirmation',EV,'Approval statuses ; Confirming ; Changes ; Finalized','Approval / confirmation','Préparation, approbation et engagement d’un achat.','Distinguer les décisions et conserver les versions confirmées.','Approved, Confirmed et Finalized ont des effets distincts ; pro forma sans journal et confirmation engagée diffèrent.')
src('changes','Microsoft','Dynamics 365 SCM','Review and accept changes to confirmed purchase orders',SCM+'procurement/purchase-order-changes-after-confirmation',EV,'Assess changes ; Review impacted demand ; Accept changes','Confirmed purchase order changes','Réponses fournisseur modifiant quantité ou date.','Évaluer les conséquences avant de retenir le changement.','La revue distingue les valeurs avant/après et leurs conséquences sur la demande ; une proposition n’est pas un accord automatique.')
src('statuses','Oracle','Order Management','Order Management Statuses',OC+'25c/fauom/order-management-statuses.html','Oracle Fusion Cloud SCM 25C','Order ; Order line ; Fulfillment line ; Task ; Orchestration process','Order management status','Progression d’une vente à plusieurs niveaux.','Différencier commande, ligne, tâche et processus.','Un statut synthétique résulte de plusieurs progressions ; les statuts d’objets différents ne sont pas interchangeables.')
src('release','Microsoft','Warehouse Management','Release to warehouse process',SCM+'warehousing/release-to-warehouse-process',EV,'Introduction ; Manual and automatic release ; Partial release','Release to warehouse','Commandes ou quantités transmises au dépôt.','Autoriser le lancement et former les expéditions.','La libération peut être partielle ; la création des travaux et vagues dépend du parcours configuré.')
src('hold','Microsoft','Dynamics 365 SCM','Manage order holds',SCM+'sales-marketing/tasks/manage-order-holds',EV,'Create a hold code ; Apply ; Remove','Order hold','Commande bloquée pour un motif identifié.','Suspendre puis lever le blocage avec les droits requis.','Adresse, paiement ou contrôle de crédit peuvent bloquer l’expédition ; le sort des réservations relève d’une option distincte.')
src('ohold','Oracle','Order Management','Hold Your Sales Orders',OC+'26b/fauom/sales-order-hold.html','Oracle Fusion Cloud SCM 26B','Hold tasks ; Multiple holds ; Release a hold','Task hold','Étape d’une vente suspendue.','Cibler la progression et justifier sa reprise.','Plusieurs blocages peuvent viser des étapes différentes, par exemple expédition et facturation.')
src('cancel','Oracle','Order Management','Cancel Sales Orders',OC+'26b/fauom/cancel-sales-orders.html','Oracle Fusion Cloud SCM 26B','Cancel an order ; Partially shipped lines ; Closed orders','Order cancellation','Reliquat d’une vente encore annulable.','Conserver les expéditions acquises, retirer ce qui reste.','Exemple : 10 commandées, 7 expédiées, 3 encore annulables ; une commande close exige un autre traitement.')
src('schedule','Microsoft','Dynamics 365 SCM','Delivery schedules',SCM+'sales-marketing/delivery-schedules',EV,'Create delivery schedules ; Manage delivery lines ; Example','Delivery schedule','Quantité commerciale répartie en livraisons.','Conserver le total et détailler quantités et échéances.','Exemple : 600 chaises, six livraisons de 100 sur six mois.')
src('split','Oracle','Order Management','Fulfillment Line Splits',OC+'26b/fauom/fulfillment-line-splits.html','Oracle Fusion Cloud SCM 26B','Split manually ; Split automatically ; Examples','Fulfillment line split','Une ligne satisfaite par plusieurs parties.','Répartir les quantités entre sources ou dates.','Exemple : une demande de 50 tablettes servie à hauteur de 30 et 20 depuis deux lieux ; restrictions selon le parcours.')
src('vendor','Microsoft','Dynamics 365 SCM','Vendor collaboration with external vendors',SCM+'procurement/vendor-collaboration-work-external-vendors',EV,'Purchase order responses ; Accept with changes ; Confirmation','Vendor purchase order response','Acceptation, refus ou contre-proposition fournisseur.','Enregistrer la réponse puis confirmer selon les règles.','Une acceptation avec modification et une acceptation sans changement ne suivent pas la même confirmation automatique.')
src('ubl','OASIS','Universal Business Language','Universal Business Language Version 2.4','https://docs.oasis-open.org/ubl/UBL-2.4.html','UBL 2.4','3.2.47 Order ; 3.2.48 Order Cancellation ; 3.2.49 Order Change ; 3.2.50 Order Response','Order / Order Response','Commande de biens ou services et réponse échangées.','Séparer demande, changement, annulation et réponse.','Les documents UBL distinguent commande, réponse détaillée, changement et annulation complète.','Standard d’échange documentaire ; ne normalise ni toutes les responsabilités FLOW ni les termes français locaux.')
src('oconsign','Oracle','Inventory Management','Consigned Inventory',OC+'25d/faims/consigned-inventory.html','Oracle Fusion Cloud SCM 25D','Consignment agreements ; Orders ; Consumption advice','Consignment order','Stock détenu mais appartenant au fournisseur.','Séparer approvisionnement, consommation et règlement.','L’ordre périodique exprime quantité, lieu et date ; la consommation intervient dans le transfert de propriété et le règlement.')
src('nextail','Nextail','Retail inventory optimization','Solution specifications','https://help.nextail.co/en/solution-specifications',EV,'First Allocation ; Replenishment ; Store Transfers','First Allocation / Replenishment','Implantation, réassort et transferts retail.','Distinguer premier apport et distribution continue.','First Allocation précède la vente du nouveau produit ; Replenishment renouvelle le stock ; Store Transfers rééquilibre le réseau.')
src('sapinter','SAP','S/4HANA Sales','Executing the Advanced Intercompany Sales and Stock Transfer Process','https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/executing-the-advanced-intercompany-sales-and-stock-transfer-process_c5f8e409-c8e3-4e0a-b736-6d1d93d0f2bc',SAP,'Classic versus advanced intercompany sales ; Process','Advanced intercompany sales','Vente impliquant sociétés vendeuse et livreuse.','Relier achat et vente internes dans le parcours avancé.','Le parcours avancé ajoute des documents internes au scénario classique ; livraison directe au client compatible avec intercompany.')
src('subcontract','SAP','S/4HANA Procurement','Outlining Subcontracting','https://learning.sap.com/courses/detailing-subcontracting-and-supplier-consignment/outlining-subcontracting_af403e3e-188d-4dbb-bde1-632253739fa6',SAP,'Subcontracting process ; Components ; Ownership','Subcontracting','Composants confiés à un fournisseur pour transformation.','Fournir les composants et acheter le produit transformé selon l’accord.','La fourniture et propriété des composants distinguent la sous-traitance d’un achat classique ; tous les achats de services n’en relèvent pas.')
src('depot','Oracle','Service Logistics','Manage Repair Orders from the Depot Repair Page','https://docs.oracle.com/en/cloud/saas/service-logistics/26b/fasul/manage-repair-orders-from-the-depot-repair-page.html','Oracle Fusion Cloud Service Logistics 26B','Create repair work orders ; Return to customer ; Serialized assets','Depot repair','Bien retourné, réparé puis restitué.','Relier retour, travail de réparation et bien expédié.','Le suivi des biens sérialisés aide à restituer le bon équipement ; une quantité non réparable peut réduire le retour attendu.')
src('cmmn','OMG','Case Management Model and Notation','Case Management Model and Notation','https://www.omg.org/cmmn/','Page de présentation CMMN consultée le 19 septembre 2026','What is case management ; Case file ; Human judgment','Case','Dossier évolutif autour d’une situation.','Mobiliser informations, événements et jugement des acteurs.','CMMN traite les dossiers dont le déroulement s’adapte ; pas un synonyme général de commande.')
src('case','Microsoft','Dynamics 365 Finance and Operations','Case management overview',MS+'fin-ops-core/dev-itpro/organization-administration/cases',EV,'Examples: City Power & Light ; Fabrikam employees','Case management','Situation, échanges et actions suivis dans un dossier.','Rattacher les contacts et pièces à un même cas.','Exemple éditeur : plusieurs appels pour une panne électrique sont réunis dans le même cas avec un ordre de service lié.')
src('potypes','Oracle','Purchasing','What’s the difference between a purchase order, a purchase agreement, and a contract agreement?','https://docs.oracle.com/en/cloud/saas/procurement/26a/oaprc/Chunk145966296.html','Oracle Fusion Cloud Procurement 26A','Purchase Order ; Blanket Purchase Agreement ; Contract Purchase Agreement','Purchase order','Achat défini de biens ou services.','Distinguer commande et accord préparant des achats futurs.','La commande précise les quantités et livraisons ; l’accord ne contient pas nécessairement ces engagements détaillés.')
src('safety','Microsoft','Planning Optimization','Safety stock fulfillment for items',SCM+'master-planning/safety-stock-replenishment',EV,'Introduction ; Example Safety stock ; Min/max coverage code','Safety stock requirement','Besoin de protection contre la rupture.','Comparer stock projeté et seuil, puis prévoir un apport.','Un minimum de stock génère un besoin sans constituer une commande client ; ce besoin coexiste avec la demande réelle.')
src('sapret','SAP','S/4HANA Sales','Managing Customer Returns','https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/managing-customer-returns_f224d287-07ad-41fe-9897-2eb2ee4b33dc',SAP,'Customer Returns ; Refund ; In-house Repair ; Send back to customer','Customer returns','Retour, inspection et suite choisie pour le client.','Relier commande de retour, compensation et documents de suivi.','Crédit, remplacement et réparation sont des parcours distingués ; des retours peuvent être dirigés vers le fournisseur.')
src('sapsales','SAP','S/4HANA Sales','Executing a Standard Sales from Stock Process','https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/executing-a-standard-sales-from-stock-process_f4aacaf6-1a5c-4f30-8d32-fd3e8e691252',SAP,'Sales order ; Outbound delivery ; Goods issue ; Billing','Sales from stock','Vente satisfaite depuis le stock.','Relier commande, livraison, sortie et facturation.','La vente commence par une commande et mobilise ensuite plusieurs activités et documents distincts.')
src('epp','Oracle','Purchasing','Purchase Orders','https://docs.oracle.com/cd/E26401_01/doc.122/e48931/T446883T443953.htm','Oracle E-Business Suite 12.2','Standard Purchase Orders ; Planned Purchase Orders ; Scheduled Releases ; Shipments','Standard / Planned Purchase Order','Achats détaillés ou engagement à livraisons précisées ensuite.','Distinguer le type de commande et ses échéances.','Planned Purchase Order désigne ici un engagement à long terme ; ce n’est pas le même sens que la proposition à affermir de Microsoft.')
src('service','SAP','S/4HANA Procurement','Processing a Service Entry Sheet','https://learning.sap.com/courses/business-processes-in-sap-s-4hana-sourcing-and-procurement/processing-a-service-entry-sheet_e42ab0b6-291a-4dad-9f5c-7f508d21ae5c',SAP,'Service Entry and Approval ; Create and Approve a Service Entry Sheet','Service entry sheet','Prestation commandée puis déclarée réalisée.','Séparer enregistrement du service et approbation.','Exemple pédagogique : réparation d’imprimante avec pièce supplémentaire ; constat de service lié à l’achat, puis approbation.')
src('receipt','Microsoft','Dynamics 365 SCM','Product receipt against purchase orders',SCM+'procurement/product-receipt-against-purchase-orders',EV,'Preregistration ; Registration ; Product receipt ; Correction','Product receipt','Biens reçus rapprochés de la commande fournisseur.','Distinguer annonce, arrivée et réception enregistrée.','Une réception conserve quantité, date et référence ; sa correction n’efface pas nécessairement le document antérieur.')

OUT={'source':'U477','nodes':[],'terms':[]}
USED={}
EXAMPLES={}

def cmp(key, same, diff, concept=None, scope=None, approach=None):
    return dict(key=key, similarities=same, differences=diff, concept_name=concept, scope_summary=scope, approach_summary=approach)

def ex(key, title, situation, outcome, lesson, real=False):
    return dict(key=key, title=title if real else 'Illustration FLOW — '+title, situation=situation, outcome=outcome, lesson=lesson, origin='Exemple du document primaire' if real else 'Illustration FLOW construite ; mécanisme étayé par le document')

def card(id, choice, scope, approach, comparisons, synthesis, example, note=None):
    assert id in OLD and not any(n['id']==id for n in OUT[COL[id]])
    cs=[]
    for c in comparisons:
        s=S[c['key']]
        priors=[r for r in OLD[id].get('market_comparisons',[]) if r['source_url']==s['source_url']]
        refs=list(dict.fromkeys([ref for r in priors for ref in r.get('source_refs',[])]+['U477']))
        out={k:s[k] for k in ('vendor','product','source_title','source_url','source_version','source_locator','consulted_on','evidence_limits')}
        out.update(element_name=c['concept_name'] or s['concept_name'], element_type='Concept et usage documentés', relationship='Recouvrement partiel', similarities=c['similarities'], differences=c['differences'], flow_position=approach, status=priors[0].get('status','proposed') if priors else 'proposed', source_refs=refs)
        for k in ('concept_name','scope_summary','approach_summary'):out[k]=c[k] or s[k]
        cs.append(out)
        USED.setdefault(c['key'],[]).append(id)
    s=S[example['key']]
    e={k:v for k,v in example.items() if k not in ('key','origin')}
    e.update(source_title=s['source_title'],source_url=s['source_url'],source_refs=next(c['source_refs'] for c in cs if c['source_url']==s['source_url']))
    EXAMPLES.setdefault(example['key'],[]).append(dict(id=id,title=e['title'],origin=example['origin']))
    entry=dict(id=id,market_comparisons=cs,market_inspiration=dict(choice=choice,flow_scope=scope,flow_approach=approach,synthesis=synthesis,examples=[e]))
    if note:entry['editorial_notes']=note
    OUT[COL[id]].append(entry)

# Les fiches ci-dessous sont rédigées explicitement ; les helpers ne produisent aucun texte métier.
card('D04.i',
 'Savoir ce que le client attend et ce qui reste à lui servir. Sales Order conserve ce nom usuel pour la gestion de la commande, avec livraison, retrait ou livraison directe selon les lignes.',
 'Contenu, évolutions et reste à satisfaire de la commande client.',
 'Maintenir la demande client ; faire expliciter séparément sa promesse et sa réalisation.',
 [cmp('pos','Livraison et retrait sont deux façons de satisfaire une commande.','Le parcours POS ne couvre pas à lui seul toutes les ventes FLOW.'),cmp('direct','L’achat direct reste relié à la quantité vendue.','La gestion du lien ne rend pas Sales Order responsable de l’expédition fournisseur.'),cmp('inter','Les commandes entre sociétés conservent leurs liens commerciaux.','Intercompany qualifie les parties ; ce n’est pas un mode de livraison concurrent du retrait ou de l’expédition.')],
 ['Microsoft Commerce distingue les modes de remise au client ; les documentations Direct delivery et Intercompany ajoutent respectivement le chemin fournisseur et la relation entre sociétés.', 'FLOW retient ces distinctions combinables. Le contenu attendu reste dans Sales Order, tandis que choisir la meilleure solution, promettre et exécuter mobilisent d’autres responsabilités.'],
 ex('pos','Une vente, deux modes de remise','Un client commande une veste à retirer samedi et un sac à recevoir chez lui.','Chaque ligne conserve son lieu, sa date et son reste à servir.','Le retrait de la veste ne clôt pas automatiquement la demande du sac.'))

card('D04.j',
 'Savoir ce qu’un fournisseur doit encore apporter, en biens ou en prestations. Purchase Order couvre la commande d’achat et ses changements, avec un résultat attendu explicite.',
 'Attentes fournisseur, conditions applicables, réponses et reste à recevoir.',
 'Rapprocher la commande, les réponses acceptées et les réalisations ; garder l’accord de référence distinct.',
 [cmp('pocreate','L’achat porte aussi sur des services.','La saisie produit ne définit pas les autorisations métier de modification.'),cmp('potypes','Commande précise et accord d’achat ont des portées différentes.','Oracle classe des documents ; FLOW décrit la prise en charge durable de la commande.'),cmp('vendor','La réponse fournisseur peut accepter, refuser ou proposer un écart.','Une réponse reçue n’établit pas automatiquement le contenu applicable.')],
 ['Microsoft explique comment exprimer l’achat et recueillir la réponse du fournisseur ; Oracle sépare la commande détaillée des accords qui encadrent des achats futurs.', 'FLOW reprend cette séparation pour conserver un attendu lisible. Le choix d’acheter, la négociation de l’accord et la réalisation physique ne se déduisent pas de la seule présence de la commande.'],
 ex('vendor','Une date fournisseur à examiner','Un achat attend 80 pièces vendredi ; le fournisseur propose lundi.','La date proposée est visible avant son acceptation.','Le besoin, la réponse et l’engagement retenu restent distinguables.'),
 'Recentrage sur commande et réponse fournisseur. Les détails Direct delivery et Service Entry Sheet restent documentés dans BHV059/BHV060 ; ancienne page SAP de confirmation non nécessaire à cette synthèse.')

card('D04.k',
 'Suivre ce qui doit quitter un site et arriver dans un autre. Transfer Order garde le nom du marché pour l’ordre de déplacement, quel que soit le motif de l’apport.',
 'Origine, destination, quantités, dates et restant à déplacer.',
 'Maintenir l’ordre et rapprocher départ et arrivée sans confondre transfert demandé et stock déjà reçu.',
 [cmp('to','Deux lieux et deux étapes rendent le transfert explicable.','L’intégration IOM est un exemple de mise en œuvre, pas une architecture imposée.'),cmp('towh','Le réassort peut produire un ordre entre dépôts.','FLOW ne limite pas les transferts aux besoins calculés par la planification.')],
 ['Microsoft IOM expose le transfert à suivre ; la documentation SCM montre comment un besoin de réapprovisionnement peut le faire naître. Les deux traitent le même déplacement depuis des points de vue différents.', 'FLOW conserve la commande comme responsabilité propre. Implantation, réassort, rééquilibrage et satisfaction d’une vente expliquent son intention sans changer la distinction départ/arrivée.'],
 ex('to','Expédié ne signifie pas reçu','Un transfert prévoit 40 pièces de l’entrepôt au magasin ; 40 partent, 38 arrivent.','Le suivi montre deux pièces à expliquer.','Le reste et l’écart ne se calculent pas à partir d’un unique statut « terminé ».'),
 'Sources détaillant rééquilibrage et consolidation recentrées sur BHV072/BHV073. L’ancien STO SAP est remplacé ici par deux pages Microsoft directement lisibles sur le suivi et l’origine des transferts.')

card('D04.l',
 'Prendre en charge ce que devient un produit retourné par un client. Customer Return relie le retour aux suites retenues : stock, remise en état, fournisseur, restitution ou rebut.',
 'Retour client et résultat logistique attendu après examen.',
 'Conserver le retour, la décision et la suite attendue ; rapprocher les réalisations sans effacer la vente.',
 [cmp('sapret','Le retour ouvre plusieurs suites possibles après inspection.','Le parcours SAP inclut la compensation financière ; FLOW distingue les responsabilités concernées.'),cmp('dispo','Le sort du produit est différent du motif de retour.','Un code de disposition n’est pas la preuve de l’exécution complète de la suite.')],
 ['SAP présente un parcours lié de retour et de suivi ; Microsoft détaille les choix de disposition et leurs effets. Tous deux évitent de réduire le retour à une simple quantité négative.', 'FLOW retient une demande de retour distincte de la vente et explicite le résultat attendu pour chaque quantité. Un remboursement et une remise en stock ne désignent pas le même résultat.'],
 ex('dispo','Deux états dans un même retour','Sur deux articles rendus, l’un est revendable et l’autre doit être expertisé.','Les deux quantités suivent des suites différentes.','Le retour reste traçable même si son traitement est réparti.'),
 'La page SAP Help historique renvoie un texte vide lors de la consultation ; remplacement par le cours primaire SAP Managing Customer Returns, lisible et pertinent.')

card('D04.m',
 'Savoir ce qui est attendu après un renvoi au fournisseur : argent, remplacement ou retour du bien réparé. Supplier Return garde ces trois résultats distincts.',
 'Marchandises renvoyées et contrepartie ou restitution attendue.',
 'Relier le renvoi à son résultat sans réouvrir implicitement un achat de remplacement.',
 [cmp('bcret','Renvoi et remplacement éventuel restent liés.','Business Central peut représenter le remplacement par un nouvel achat.'),cmp('credit','Un retour pour crédit n’attend aucune nouvelle marchandise.','L’option Oracle documente ce seul résultat.'),cmp('gp','Repair and Return distingue restitution du même bien et remplacement.','Ce parcours Dynamics GP ne prouve pas la couverture de tout ERP.',concept='Return to Vendor',scope='Retour fournisseur pour crédit, remplacement ou réparation.',approach='Qualifier le résultat attendu du fournisseur.')],
 ['Business Central organise les documents du renvoi ; Oracle isole explicitement le crédit sans remplacement ; Dynamics GP distingue la réparation avec restitution.', 'FLOW classe les variantes par le résultat attendu du fournisseur. Cette lecture évite de considérer tout départ de stock comme une simple correction d’achat.'],
 ex('gp','Attendre le bon résultat','Deux appareils partent au fournisseur : l’un doit être remplacé, l’autre réparé puis restitué.','Les attentes ne sont pas soldées par le seul départ.','L’identité compte pour la réparation ; le lien au renvoi compte aussi pour le remplacement.'),
 'Ancienne page SAP Business ByDesign inaccessible en texte ; remplacée par Dynamics GP pour les résultats du renvoi. Oracle Service Parts Planning est conservé au niveau BHV057, où sa limite de planification est explicite.')

card('D04.n',
 'Adapter la forme des commandes pour les traiter sans perdre leur origine. Order Structuring distingue scinder, traiter ensemble et remplacer plusieurs commandes par une seule.',
 'Composition des commandes et liens entre éléments d’origine et résultants.',
 'Préserver quantités, filiation et engagements à chaque changement de structure.',
 [cmp('schedule','Un total peut être réparti en plusieurs échéances.','L’échéancier ne fusionne pas plusieurs commandes.'),cmp('set','Des lignes restent distinctes tout en partageant une contrainte de départ.','Un groupe logistique n’est pas une nouvelle demande unique.'),cmp('merge','Plusieurs achats compatibles peuvent donner une commande résultante.','Les conditions et effets de fusion propres à Infor ne s’appliquent pas automatiquement à tous les Orders.')],
 ['Microsoft illustre le fractionnement, Oracle le traitement collectif et Infor la fusion. Ces trois mécanismes répondent à des besoins différents, même s’ils changent tous la forme du travail à traiter.', 'FLOW les réunit dans Order Structuring pour rendre les transformations explicables. La quantité d’origine et les engagements ne disparaissent pas avec une nouvelle présentation.'],
 ex('schedule','600 chaises échelonnées','Microsoft prend une vente de 600 chaises à livrer par lots de 100 pendant six mois.','L’échéancier détaille les six livraisons sous le total commercial.','Scinder les échéances ne crée pas six demandes indépendantes sans origine.',True),
 'Deux pages Oracle de split redondantes recentrées sur BHV044 ; ajout de Shipment Sets et Infor Commingling pour couvrir réellement regroupement et fusion. Ancienne référence SAP de livraison ne suffit pas à couvrir ces trois mécanismes.')

card('D04.o',
 'Savoir ce qui peut encore changer, commencer ou s’arrêter dans une commande. Order Lifecycle Management distingue ces droits et engagements au lieu de les résumer par un seul statut.',
 'Préparation, engagement, gel, lancement, suspension et fin de la commande.',
 'Rendre explicites les transitions autorisées et conserver les engagements et réalisations acquis.',
 [cmp('statuses','Plusieurs progressions coexistent autour d’une commande.','Les niveaux de statut Oracle ne constituent pas les six dimensions métier FLOW.'),cmp('approve','Préparation, approbation et confirmation produisent des effets différents.','La succession propre aux achats Microsoft n’est pas un cycle universel des Orders.'),cmp('ohold','Une suspension vise une étape déterminée.','La levée d’un blocage ne confirme ni une nouvelle promesse ni la clôture de l’ordre.')],
 ['Oracle sépare les statuts des objets et les blocages des étapes ; Microsoft sépare les décisions d’approbation et de confirmation d’achat. Les deux montrent pourquoi « commande en cours » ne suffit pas.', 'FLOW organise ces questions en dimensions métier indépendantes. Une commande peut être engagée, partiellement réalisée et suspendue pour son reliquat sans contradiction.'],
 ex('ohold','Engagée mais suspendue','Une commande confirmée est bloquée avant expédition pour vérifier l’adresse.','Le blocage porte sur le départ ; l’engagement reste identifié.','Reprendre le traitement et réviser la promesse sont deux décisions différentes.'),
 'Seize anciennes entrées, dont un doublon de confirmation, recentrées sur trois documents à la maille Lifecycle. Affermissement, gel, release, annulation et split restent sourcés dans leurs propres fiches ; aucun nouveau cycle séquentiel adopté.')

card('D04',
 'Disposer d’une demande Supply claire et maintenue jusqu’à son résultat ou sa fin. Order Management porte les commandes et leurs évolutions, avec des responsabilités distinctes pour optimiser, promettre et exécuter.',
 'Intentions, parties, conditions, structure, cycle de vie et conservation des commandes Supply.',
 'Gérer chaque famille selon son résultat attendu et rendre ses échanges avec la promesse et les processus explicites.',
 [cmp('po','Les quantités demandées, reçues et restant à traiter doivent rester explicables.','Une vue d’achat ne couvre pas toutes les commandes Supply.'),cmp('supply','Une demande relie plusieurs documents et acteurs de satisfaction.','Supply Chain Orchestration Oracle inclut la coordination d’approvisionnement ; son périmètre dépasse la gestion des Orders FLOW.'),cmp('sapsales','La commande et les documents de réalisation sont liés.','Le processus de vente complet réunit des activités réparties entre plusieurs responsabilités FLOW.')],
 ['Microsoft montre la gestion d’une famille de commandes ; SAP décrit le parcours complet d’une vente ; Oracle coordonne les documents nécessaires à l’approvisionnement. Les noms proches recouvrent donc des périmètres différents.', 'FLOW retient Order Management pour maintenir les demandes et leurs règles d’évolution. Le domaine ne récupère ni toute l’optimisation ni toute l’exécution simplement parce qu’un éditeur les présente dans le même produit.'],
 ex('po','Un attendu conservé malgré les livraisons','Un fournisseur devait apporter 100 pièces ; 60 sont reçues et 10 du reliquat sont annulées.','La commande explique 60 reçues, 10 retirées et 30 encore attendues.','Le domaine conserve la demande applicable et son historique ; le fait de réception vient de sa réalisation.'))

card('BHV036',
 'Transformer une proposition d’approvisionnement en ordre ferme. Order Firming nomme ce passage d’engagement sans lui attribuer automatiquement tous les effets d’un gel.',
 'Intention planifiée, ordre résultant et restrictions associées.',
 'Expliciter ce que l’affermissement engage et les révisions encore autorisées.',
 [cmp('firm','Une proposition devient un achat, transfert ou ordre de fabrication effectif.','Le déclenchement automatique de Microsoft n’impose pas une règle FLOW.'),cmp('plans','Les horizons d’affermissement et de gel ont des effets distincts.','La proximité de la date ne rend pas ces deux décisions équivalentes.')],
 ['Microsoft Firm planned orders décrit le passage à l’ordre ; Master plans distingue le paramétrage de ce passage et celui du gel. Deux documents d’un éditeur éclairent la distinction, sans prouver un vocabulaire universel.', 'FLOW garde Firming pour le changement d’engagement. Les éléments protégés et les exceptions de révision doivent être précisés séparément.'],
 ex('firm','De proposition à achat','Le plan propose 120 pièces pour lundi ; l’acheteur affermit la proposition.','Un ordre ferme devient la référence de suivi.','Cela ne dit pas, à lui seul, si sa date pourra être renégociée.'))

card('BHV037',
 'Protéger ce qui a été décidé contre un nouveau calcul qui le modifierait. Order Freezing précise les éléments gelés et les exceptions permises.',
 'Quantités, dates ou liens désignés, et conditions de révision.',
 'Définir la portée de la protection ; ne pas la confondre avec une suspension du traitement.',
 [cmp('plans','Une zone du plan peut être protégée des changements.','L’horizon Freeze de Microsoft est une forme particulière du gel.'),cmp('keep','La couverture d’une demande confirmée peut être conservée au recalcul.','La fonction protège une chaîne précise et laisse certains ajustements possibles.')],
 ['Microsoft décrit d’un côté un horizon gelé, de l’autre une préservation liée aux demandes confirmées. La protection est donc temporelle dans un cas et liée à un engagement dans l’autre.', 'FLOW garde un sens plus explicite : dire ce qui ne peut plus être changé par quel recalcul. Une commande gelée peut continuer à être exécutée.'],
 ex('keep','Conserver une couverture engagée','Une vente confirmée est couverte par un achat identifié ; le prochain plan propose un autre achat.','La règle de protection peut conserver la chaîne déjà retenue.','La protection du lien n’est pas automatiquement celle de tous les champs.'),
 'Ancienne comparaison SAP aATP remplacée dans la synthèse par les deux formes de protection Microsoft directement consultables ; aucun gel de confirmation SAP généralisé à tout Order.')

card('BHV038',
 'Préparer un changement sans perdre de vue ce qui s’applique encore. Order Preparation & Revision rend distincts le contenu en travail et la version applicable.',
 'Contenu initial ou révisé et conditions de sa prise d’effet.',
 'Examiner les conséquences du changement avant application, en préservant le déjà réalisé.',
 [cmp('approve','Une demande de changement ne vaut pas confirmation révisée.','Les étapes d’approbation dépendent du parcours d’achat configuré.'),cmp('changes','Quantités et dates proposées se comparent aux valeurs antérieures.','L’évaluation produit ne remplace pas les règles métier d’acceptation FLOW.')],
 ['Microsoft décrit la gouvernance de l’achat puis un outil de revue des changements fournisseur. Le premier document traite l’autorisation ; le second aide à comprendre les conséquences.', 'FLOW rassemble ces deux besoins pour toute préparation ou révision concernée. Une nouvelle date demandée ne remplace pas silencieusement une date déjà engagée.'],
 ex('changes','Réviser le reste','Sur 100 pièces commandées, 60 sont déjà reçues ; une nouvelle date est proposée pour les 40 autres.','Le changement vise le reliquat et reste identifiable jusqu’à son acceptation.','Les 60 reçues ne redeviennent pas une quantité à négocier.'),
 'Messages de planification et statuts Oracle retirés du tableau court : ils signalent une évolution sans étayer aussi directement l’acceptation du contenu révisé.')

card('BHV039',
 'Autoriser un lancement lorsque ses conditions sont remplies. Order Release peut concerner une quantité, une commande ou un ensemble qui doit partir ensemble.',
 'Éligibilité au lancement individuelle et collective.',
 'Distinguer autorisation, transmission et exécution effective.',
 [cmp('release','La libération peut porter sur une partie de commande.','Release to warehouse est une destination particulière, pas la définition de toutes les releases.'),cmp('setguide','Des conditions collectives peuvent retenir plusieurs lignes.','Shipment Set décrit une contrainte de groupe ; sa présence ne prouve pas un départ exécuté.')],
 ['Microsoft documente l’autorisation vers le dépôt ; Oracle montre les dépendances d’un ensemble à expédier. Les deux approches combinent un contrôle individuel et des conditions de traitement collectif.', 'FLOW retient cette logique de lancement explicite. Un engagement ou une réservation ne vaut pas, par lui-même, autorisation de démarrer.'],
 ex('setguide','Attendre l’ensemble convenu','Une tenue doit partir complète ; veste et pantalon sont prêts, la chemise manque.','L’autorisation du groupe attend la condition de complétude retenue.','L’exemple illustre une règle métier choisie ; il ne l’impose pas à tous les groupes.'),
 'Source SAP Supply Assignment pertinente pour affectation et release conditionnelle, mais retirée du tableau court au profit de la release dépôt et des contraintes collectives directement ciblées.')

card('BHV040',
 'Suspendre une étape pour une raison précise puis permettre sa reprise. Order Hold & Resume conserve le motif, la portée du blocage et les conditions de levée.',
 'Progression suspendue, motif et reprise autorisée.',
 'Viser l’étape concernée et traiter séparément les effets sur engagements et ressources.',
 [cmp('hold','Un motif peut empêcher l’expédition jusqu’à contrôle.','Le devenir des réservations est une option distincte du blocage.'),cmp('ohold','Plusieurs blocages peuvent viser des tâches différentes.','Le mécanisme Oracle ne transforme pas toute la commande en un état unique arrêté.')],
 ['Microsoft présente le blocage de commande avant expédition ; Oracle le positionne sur des tâches et autorise plusieurs motifs simultanés. Leur point commun est un empêchement explicite et réversible.', 'FLOW garde cette précision pour expliquer ce qui peut continuer. Lever un blocage ne supprime pas un autre motif encore actif.'],
 ex('ohold','Deux contrôles, deux levées','Une expédition attend une adresse correcte ; la facturation attend un contrôle distinct.','La correction d’adresse permet seulement de lever le premier blocage.','Reprise doit toujours préciser la progression libérée.'))

card('BHV043',
 'Retirer ce qui n’est plus attendu et fermer le suivi lorsqu’il n’a plus de suite. Order Termination distingue annulation du reliquat et clôture, sans effacer les réalisations.',
 'Quantités retirées, reliquat résolu et fin du suivi opérationnel.',
 'Expliciter les effets encore annulables et préserver ce qui a déjà été réalisé.',
 [cmp('cancel','La partie livrée n’est pas annulée comme le reliquat.','Une vente close peut nécessiter un retour plutôt qu’une annulation.'),cmp('approve','Finalized a un effet de clôture propre à l’achat.','La clôture financière Microsoft ne définit pas toutes les fins de suivi FLOW.')],
 ['Oracle montre l’annulation de ce qui reste à expédier ; Microsoft décrit une clôture financière empêchant les modifications. Retrait de demande et fin de traitement ont donc des effets différents.', 'FLOW les rend explicites dans Order Termination. Un reliquat ne disparaît pas sous le seul mot « clôturé » : son devenir doit rester compréhensible.'],
 ex('cancel','Trois unités encore annulables','Oracle illustre dix unités commandées, dont sept déjà expédiées et trois restant sur d’autres lignes.','Les trois restantes peuvent être annulées selon le parcours ; les sept expédiées restent réalisées.','La fin de la demande conserve la trace de ce qui a effectivement été servi.',True),
 'Doublon Microsoft regroupé ; ancienne page SAP de complétion retirée de la synthèse courte, sans modification des preuves historiques.')

card('BHV044',
 'Traiter séparément des parties d’une demande tout en conservant son origine. Order Splitting porte la filiation et la cohérence des quantités et engagements.',
 'Parties issues d’une commande ou d’une ligne.',
 'Relier chaque partie au total initial et préciser ce qui change pour sa satisfaction.',
 [cmp('split','Une ligne peut être satisfaite depuis plusieurs lieux.','Les restrictions Oracle dépendent du parcours et des ensembles de livraison.'),cmp('schedule','Une quantité commerciale peut être répartie sur plusieurs dates.','Un échéancier préparé n’est pas nécessairement un split déclenché pendant l’exécution.')],
 ['Oracle montre le fractionnement pour satisfaire une ligne ; Microsoft répartit une vente en échéances. L’un adapte le traitement, l’autre exprime des livraisons prévues.', 'FLOW retient dans les deux cas le besoin de conserver l’origine et le total. Les parties ne deviennent pas des demandes sans rapport ni de nouvelles quantités à additionner au parent.'],
 ex('split','Cinquante tablettes, deux sources','Oracle présente une demande de 50 tablettes répartie en 30 depuis un lieu et 20 depuis un autre.','Deux parties restent rattachées à la même demande de 50.','La somme explique le service attendu ; le parent ne compte pas comme une troisième livraison.',True))

card('D04.q',
 'Retrouver l’histoire d’une commande lorsqu’elle quitte le travail courant. Order Archiving conserve les versions et liens utiles selon des critères explicites.',
 'Commandes éligibles à la conservation historique et consultation ultérieure.',
 'Séparer archivage, clôture et purge ; rendre les traces consultables.',
 [cmp('archive','La commande peut sortir de l’usage courant tout en restant consultable.','La fonction SCM impose ses propres critères, dont l’exclusion de certains intercompany.'),cmp('bcarchive','Plusieurs versions documentaires peuvent être conservées.','Restaurer une version reste conditionnel ; une archive n’est pas toujours un ordre réactivable.')],
 ['Microsoft SCM met l’accent sur les commandes entièrement facturées et leur conservation ; Business Central insiste sur les versions documentaires et leur réutilisation éventuelle.', 'FLOW retient la conservation historique comme responsabilité propre. Archiver ne prouve ni que toute obligation est éteinte ni que le contenu pourra être restauré dans le courant.'],
 ex('bcarchive','Retrouver une ancienne date','Une commande a changé de date avant sa clôture ; un litige demande la version précédente.','L’archive permet de consulter le contenu et les liens conservés.','La consultation de preuve ne modifie pas la commande actuelle.'),
 'Ancienne documentation Oracle de purge remplacée dans le tableau court par deux formes d’archivage explicitement distinguées ; aucune purge historique exécutée.')

card('BHV050',
 'Rendre à nouveau utilisable un produit revenu du client lorsque son état le permet. Return to Stock vise la remise en disponibilité, après la décision appropriée.',
 'Quantité retournée déclarée admissible au stock utilisable.',
 'Relier le retour et la remise en disponibilité, sans assimiler arrivée physique et produit revendable.',
 [cmp('dispo','Le résultat Credit peut remettre le produit dans le stock.','L’effet de crédit est associé dans Microsoft ; il ne définit pas le seul résultat logistique FLOW.'),cmp('b2b','Un produit neuf retourné peut rejoindre le disponible.','L’exemple Oracle ne généralise pas ce résultat à tout état de retour.',concept='Returned stock',scope='Produit retourné admissible à un nouvel usage.',approach='Réintégrer le produit utilisable après retour.')],
 ['Microsoft associe des effets à une disposition ; Oracle illustre le retour au disponible d’un article inutilisé. Tous deux supposent que le produit puisse être remis en circulation.', 'FLOW met l’accent sur ce résultat : la quantité doit devenir utilisable, pas seulement apparaître reçue. Un contrôle encore ouvert doit rester visible.'],
 ex('b2b','Un article inutilisé revient','Oracle décrit le retour d’un équipement neuf dont la configuration ne convenait pas au client.','Le produit inutilisé peut rejoindre le disponible.','Le cas étaye la remise en stock admissible ; il ne décide pas du sort d’un article endommagé.',True),
 'Page SAP Help historique vide remplacée par un exemple Oracle explicite ; conservation de la disposition Microsoft avec sa limite financière.')

card('BHV051',
 'Obtenir un produit remis en état et savoir quelle suite lui donner. Repair and Refurbishment suit la réparation et son résultat dans le traitement du retour client.',
 'Remise en état demandée, résultat constaté et suite attendue.',
 'Relier produit retourné, intervention et destination après traitement.',
 [cmp('depot','Le retour peut mener à un travail de réparation lié au bien.','Depot Repair décrit une mise en œuvre spécifique, notamment pour les équipements identifiés.'),cmp('sapret','Le retour client peut être dirigé vers une réparation interne.','La présence du parcours ne garantit pas que chaque produit sera réparable.')],
 ['Oracle détaille le lien au travail de réparation et au bien ; SAP intègre la réparation parmi les suites du retour client. Les deux dépassent le simple libellé d’un code de retour.', 'FLOW conserve le résultat de remise en état et la suite attendue. Réparation achevée, retour en stock et restitution au client restent des résultats à distinguer.'],
 ex('depot','Réparation puis orientation','Un article retourné est réparé ; le contrôle final décide s’il peut être restitué au client.','Le résultat de l’intervention est lié au retour.','Le suivi ne s’arrête pas à l’envoi à l’atelier.'),
 'Le code Repair de Microsoft n’étaye pas à lui seul une prise en charge complète. Remplacement de cette preuve insuffisante et de la page SAP vide par deux parcours primaires de réparation.')

card('BHV052',
 'Passer d’un retour client à un renvoi au fournisseur sans perdre le lien entre les deux. Return to Supplier conserve la suite attendue de cette prise en charge.',
 'Lien entre le retour client et la demande Supplier Return.',
 'Transmettre l’attendu et conserver la filiation entre deux commandes de retour distinctes.',
 [cmp('gp','Un retour fournisseur peut être issu d’un retour client.','Créer la commande de retour fournisseur ne suffit pas à prouver le départ ou son résultat.',concept='Return to Vendor from customer return',scope='Retour fournisseur issu du retour client.',approach='Créer le retour fournisseur en conservant le lien au client.'),cmp('sapret','Le retour client peut être orienté vers le fournisseur.','Les parcours directs ou via site ne sont pas une règle unique de circulation.')],
 ['Dynamics GP rend explicite la création du RTV depuis le RMA ; SAP présente l’orientation vers le fournisseur dans le retour client. Les deux relient deux relations métier distinctes.', 'FLOW conserve ce passage de relais. La décision de renvoyer ne transforme pas le retour client en commande fournisseur indifférenciée.'],
 ex('gp','Un défaut à traiter par le fournisseur','Un client rend un article défectueux ; la suite retenue exige une prise en charge fournisseur.','Une demande fournisseur est reliée au retour client.','La réponse au client reste suivie même quand un autre acteur reçoit le produit.'),
 'ReturnVendor comme code Microsoft ne démontre pas ce lien complet ; les parcours GP et SAP Learning remplacent les anciennes preuves trop indirectes.')

card('BHV053',
 'Restituer le produit au client lorsqu’il doit lui revenir, après réparation ou refus de reprise. Return to Customer précise quel bien et quelle quantité sont à remettre.',
 'Restitution liée au retour initial et à la décision prise.',
 'Suivre le bien jusqu’à sa remise attendue au client, avec identité préservée lorsque nécessaire.',
 [cmp('dispo','Return to customer prévoit une restitution après non-reprise.','Cette disposition ne couvre pas à elle seule la réparation avant restitution.',concept='Return to customer',scope='Retour refusé puis produit rendu au client.',approach='Orienter le produit vers sa restitution.'),cmp('depot','Le produit réparé peut être renvoyé au bon client.','Le suivi sérialisé Oracle concerne les biens concernés, sans imposer la sérialisation de tous les articles.')],
 ['Microsoft décrit le retour au client lorsque la reprise est refusée ; Oracle décrit la restitution après réparation. Le même mouvement final peut donc répondre à deux motifs très différents.', 'FLOW réunit le résultat de restitution tout en conservant sa cause. Il ne l’assimile ni à un remplacement ni à une nouvelle vente sans lien.'],
 ex('depot','Restituer le bien réparé','Un appareil portant un numéro de série revient après réparation.','Le bien à expédier est rattaché au client qui l’avait retourné.','La bonne quantité ne suffit pas lorsque l’identité du bien est un engagement.'),
 'Page SAP Help vide remplacée par Oracle Depot Repair, complément direct du cas de non-reprise Microsoft.')

card('BHV054',
 'Suivre la mise au rebut retenue jusqu’à sa preuve et à sa traduction dans le stock. Scrapping conserve l’autorisation distincte de la destruction réalisée.',
 'Produit retourné destiné au rebut, décision et réalisation.',
 'Rapprocher la preuve de mise au rebut avec la quantité sortie du stock.',
 [cmp('dispo','Scrap est un résultat différent de la remise en stock.','Le choix d’une disposition ne constitue pas une preuve matérielle de destruction.',concept='Scrap',scope='Produit retourné destiné à être éliminé.',approach='Appliquer la disposition choisie et ses effets associés.'),cmp('gp','Le traitement d’un RMA peut conduire au rebut.','La procédure produit ne définit pas toutes les autorisations et preuves requises par FLOW.',concept='RMA scrap',scope='Mise au rebut d’un produit revenu du client.',approach='Suivre cette suite dans le dossier de retour.')],
 ['Microsoft SCM associe au rebut une disposition ; Dynamics GP le place parmi les suites du retour. Les deux identifient le sort du produit, sans fournir une preuve universelle de destruction.', 'FLOW exige de pouvoir expliquer la décision puis sa réalisation. Une quantité ne doit pas être considérée détruite parce qu’un écran affiche seulement « rebut ».'],
 ex('dispo','Décider puis constater','Trois articles retournés sont déclarés irrécupérables et autorisés au rebut.','La réalisation doit ensuite être rapprochée de ces trois articles.','Le mécanisme éditeur soutient l’orientation ; le lien autorisation/preuve est la lecture FLOW.'),
 'Page SAP historique vide remplacée par le traitement RMA Dynamics GP ; aucune garantie environnementale ou réglementaire déduite de ces documents.')

card('BHV055',
 'Renvoyer au fournisseur sans attendre de nouvelle marchandise. Return for Credit conserve l’attendu d’avoir ou de remboursement lié au renvoi.',
 'Retour fournisseur dont la contrepartie attendue est financière.',
 'Séparer preuve du renvoi et obtention du crédit ; ne pas recréer un besoin de remplacement.',
 [cmp('credit','Le crédit sans remplacement est explicitement distingué.','Les restrictions de l’option Oracle restent propres au produit.'),cmp('bcret','Retour et avoir peuvent être liés.','Business Central propose aussi d’autres suites ; toute commande de retour n’est pas un retour pour crédit.')],
 ['Oracle nomme précisément Credit Only ; Business Central organise le renvoi et les corrections associées. Le premier insiste sur l’absence de remplacement, le second sur les documents à rapprocher.', 'FLOW retient cette absence d’apport attendu comme frontière. Le départ du produit ne suffit pas à déclarer la contrepartie reçue.'],
 ex('credit','Renvoi sans remplacement','Un lot défectueux est retourné avec accord pour un avoir et sans nouvel envoi.','Aucune réception de remplacement n’est attendue.','L’achat initial ne doit pas être interprété comme rouvert pour la même quantité.'),
 'Référence SAP Business ByDesign vide non reconduite ; Oracle et Business Central étayent directement le résultat choisi.')

card('BHV056',
 'Obtenir des marchandises de remplacement après un renvoi fournisseur. Return for Replacement garde ensemble le renvoyé et le nouvel apport attendu.',
 'Retour fournisseur et quantité de remplacement liée.',
 'Suivre les deux mouvements sans confondre remplacement et réparation du même bien.',
 [cmp('bcret','Le remplacement peut produire une nouvelle commande d’achat liée.','Le document supplémentaire ne doit pas faire compter deux fois l’attendu.'),cmp('gp','Replacement et Repair and Return sont des suites distinctes.','Un remplacement ne garantit pas le retour de l’identité d’origine.',concept='Return to Vendor — Replacement',scope='Remplacement attendu après retour fournisseur.',approach='Lier le renvoi au nouvel article attendu.')],
 ['Business Central met en avant l’achat de remplacement ; Dynamics GP distingue les types de retour et leur résultat. Les deux conservent un lien entre ce qui part et ce qui doit revenir.', 'FLOW suit cet attendu comme une variante métier propre. La satisfaction dépend de l’apport de remplacement admissible, pas seulement de l’expédition du retour.'],
 ex('bcret','Un mauvais article remplacé','Un fournisseur a livré un article qui doit être retourné puis remplacé par le bon.','Le renvoi et la commande de remplacement restent liés.','Deux documents peuvent porter un seul enchaînement métier de remplacement.'),
 'Page SAP Business ByDesign vide remplacée par la distinction explicite des types RTV dans Dynamics GP.')

card('BHV057',
 'Récupérer le bien confié au fournisseur après sa réparation. Return for Repair conserve l’identité et l’attendu de restitution, au-delà du seul renvoi.',
 'Envoi en réparation, délai et retour du même bien.',
 'Rapprocher départ, réparation et restitution en conservant l’identité concernée.',
 [cmp('gp','Repair and Return attend le bien réparé.','Le parcours produit ne définit pas toutes les règles de garantie et d’acceptation.',concept='Return to Vendor — Repair and Return',scope='Bien renvoyé au fournisseur pour réparation et restitution.',approach='Suivre le même bien jusqu’à son retour réparé.'),cmp('repairplan','Les délais de transport et de réparation composent le retour attendu.','Oracle traite la planification des pièces, pas une preuve suffisante du suivi individuel.')],
 ['Dynamics GP distingue opérationnellement réparation et remplacement ; Oracle Service Parts Planning explique les délais et modes de couverture par réparation. Ces sources sont complémentaires, pas équivalentes.', 'FLOW retient l’attendu du même bien. Le résultat diffère d’un simple échange même si les quantités et dates semblent identiques.'],
 ex('gp','Le même appareil doit revenir','Un appareil numéroté part au fournisseur pour réparation.','La restitution attendue désigne cet appareil, avec son état après intervention.','Un autre appareil reçu peut nécessiter une modification d’accord ; il ne solde pas silencieusement la réparation.'))

card('BHV058',
 'Faire entrer les marchandises achetées dans le stock du réseau. Stock Procurement suit l’apport restant à recevoir, avec ses quantités et dates.',
 'Achats destinés au stock, sans livraison directe au client.',
 'Conserver la destination stock et rapprocher les réceptions de la commande.',
 [cmp('pocreate','L’achat précise articles, quantités et destination.','Tous les achats Microsoft ne sont pas destinés au stock.'),cmp('epp','Les échéances d’achat détaillent les apports prévus.','Le type documentaire Oracle ne définit pas à lui seul le motif de constitution du stock.',concept='Standard purchase order',scope='Achat détaillé avec lignes et livraisons.',approach='Décrire les marchandises et leurs échéances.')],
 ['Microsoft montre la création de l’achat ; Oracle en détaille les types et livraisons. Tous deux permettent de suivre un apport de marchandises.', 'FLOW qualifie ici la destination : le stock du réseau. La prévision qui justifie l’achat et la réception physique restent distinctes du suivi de cet attendu.'],
 ex('pocreate','Compléter un apport au dépôt','Un achat prévoit 200 pièces au dépôt, dont 150 ont été reçues.','50 restent attendues selon la commande applicable.','Le stock constaté et l’apport encore prévu ne sont pas le même nombre.'))

card('BHV059',
 'Acheter pour que le fournisseur livre directement le client. Direct Delivery, côté Purchase Order, suit l’engagement fournisseur et son lien avec la vente.',
 'Achat destiné à une livraison fournisseur–client.',
 'Coordonner les attentes d’achat et de vente sans inventer un passage physique par le stock propre.',
 [cmp('direct','Les lignes d’achat et de vente sont reliées.','Le côté achat et le côté client n’ont pas le même engagement à suivre.'),cmp('supply','Le dropship fait porter la livraison par le fournisseur.','L’orchestration Oracle couvre davantage que ce comportement d’achat.',concept='Drop ship supply',scope='Approvisionnement livré directement au client.',approach='Déclencher et suivre l’achat lié à la vente.')],
 ['Microsoft explicite les liens de lignes ; Oracle situe le dropship parmi les façons d’approvisionner une vente. Les deux évitent le passage physique dans le dépôt du vendeur.', 'FLOW décrit ici l’attente envers le fournisseur. Le comportement homonyme de Sales Order conserve, lui, l’attente du client ; ce sont deux points de vue liés.'],
 ex('direct','Un envoi fournisseur suivi côté achat','Un fournisseur doit livrer 12 pièces directement au client ; il n’en expédie que huit.','L’achat conserve quatre pièces restantes et le lien vers la vente.','Une quantité annoncée au client doit rester cohérente avec l’attendu fournisseur.'))

card('BHV060',
 'Acheter une prestation et savoir ce qui a été reconnu réalisé. Service Procurement distingue l’attendu commandé, le service déclaré et son acceptation.',
 'Prestation fournisseur, périmètre attendu et réalisation reconnue.',
 'Rapprocher le service de son achat avec les preuves et décisions applicables.',
 [cmp('pocreate','Une commande fournisseur peut acheter un service.','La ligne d’achat ne prouve pas que la prestation a eu lieu.'),cmp('service','La réalisation déclarée et son approbation sont distinctes.','La feuille de service SAP est une forme documentaire, pas un document imposé à FLOW.')],
 ['Microsoft ouvre la commande d’achat aux services ; SAP montre ensuite comment constater et approuver la prestation. Les deux sources éclairent des moments complémentaires.', 'FLOW retient le service attendu puis reconnu réalisé. Commander une réparation, la faire exécuter et accepter son résultat restent trois faits différents.'],
 ex('service','La réparation de l’imprimante','Dans l’exercice SAP, une imprimante est réparée avec remplacement supplémentaire d’une pièce.','La prestation est enregistrée en référence à l’achat, puis envoyée à approbation.','L’exemple rend visible l’écart possible entre ce qui était prévu et ce qui doit être accepté.',True),
 'La page SAP Help historique Manage Service Entry Sheets est remplacée par son cours primaire lisible et son exemple de prestation.')

card('D04.r',
 'Demander un apport fournisseur sans acheter immédiatement la marchandise. Consignment Replenishment Order suit l’arrivée du stock qui reste propriété du fournisseur.',
 'Produits, quantités, destinations, dates et reste à recevoir en consignation.',
 'Distinguer demande d’apport, réception et événement ultérieur de transfert de propriété.',
 [cmp('consign','Un ordre spécifique suit le réapprovisionnement en consignation.','Le changement de propriété déclenche un achat dans Microsoft ; ce montage ne doit pas être supposé partout.'),cmp('oconsign','Possession du stock et propriété sont séparées.','Oracle emploie Consignment order dans un ensemble avec accord et consommation ; les documents diffèrent.')],
 ['Microsoft nomme Consignment replenishment order la demande d’apport ; Oracle articule ordre de consignation, consommation et règlement. Leur point commun est la séparation entre détention et propriété.', 'FLOW retient le nom Microsoft pour rendre cette intention lisible. L’ordre ne porte pas implicitement l’engagement d’acheter les marchandises à leur arrivée.'],
 ex('consign','Recevoir sans acheter à l’arrivée','Un fournisseur apporte 100 pièces consignées ; 20 sont utilisées plus tard.','La réception des 100 et le changement de propriété concerné restent deux faits distincts.','Le suivi d’apport ne doit pas transformer d’emblée les 100 en achat ferme.'),
 'Source SAP de consignation non retenue dans le tableau court, les deux montages Microsoft et Oracle suffisant à expliciter le choix sans multiplier les documents.')

card('BHV061',
 'Avoir le premier stock consigné prêt au démarrage d’une saison ou d’un lancement. Initial Stocking précise cette intention initiale au sein de la demande de consignation.',
 'Apport initial consigné et échéance de démarrage.',
 'Suivre les quantités attendues avant le lancement, en conservant le régime de propriété fournisseur.',
 [cmp('consign','L’ordre d’apport peut porter quantité et date avant consommation.','Microsoft ne nomme pas ce parcours Initial Stocking ; la distinction est celle du modèle FLOW.'),cmp('oconsign','L’apport et la consommation sont séparés.','La documentation Oracle ne définit pas une variante initiale de saison.')],
 ['Microsoft et Oracle étayent le mécanisme de consignation, avec des documents différents. Aucun des deux passages ne suffit à faire d’Initial Stocking un nom partagé pour cette variante.', 'FLOW ajoute le point de vue métier du lancement : être prêt à une date, avant un réassort régulier. Cette intention ne transforme pas l’apport consigné en achat.'],
 ex('consign','Préparer un lancement consigné','Une capsule doit démarrer lundi avec 60 pièces consignées ; 45 sont arrivées.','15 restent attendues avant le démarrage.','Le critère de service est la préparation du lancement, avec propriété fournisseur conservée.'))

card('BHV062',
 'Entretenir le stock consigné pendant la période de vente. Continuous Replenishment suit les apports successifs nécessaires au réassort, sans les confondre avec l’achat des produits.',
 'Apports récurrents consignés et reste à recevoir.',
 'Relier chaque apport à ses attentes et dates ; suivre séparément la consommation.',
 [cmp('consign','Prévision et demande peuvent entraîner des apports consignés.','Le calcul de l’apport ne relève pas ici de la gestion de la commande.'),cmp('oconsign','Des ordres de consignation peuvent être périodiques.','La périodicité n’impose ni cadence unique ni achat à chaque réception.')],
 ['Microsoft décrit la demande d’apport ; Oracle mentionne des commandes périodiques et le règlement lié à la consommation. Les deux maintiennent la propriété séparée de l’arrivée.', 'FLOW qualifie ici le réassort en cours de période. Le suivi des commandes conserve les apports demandés ; il ne fixe pas seul combien réapprovisionner.'],
 ex('oconsign','Réassort après les premières ventes','Le stock consigné diminue en cours de saison ; un nouvel apport de 25 pièces est demandé pour jeudi.','Quantité attendue et arrivée restent suivies jusqu’à satisfaction.','Le réassort est continu par son intention, sans supposer un calendrier obligatoire.'))

card('BHV066',
 'Faire livrer le client depuis le réseau qui le sert. Ship to Customer suit la quantité à expédier et la destination convenue dans la commande client.',
 'Vente à livrer au client depuis un site du réseau.',
 'Maintenir l’attendu de livraison et rapprocher sa réalisation, sans confondre préparation et livraison acquise.',
 [cmp('store','Un magasin peut servir une commande à expédier.','Le parcours magasin ne couvre pas tous les exécutants du réseau.'),cmp('sapsales','La vente sur stock relie commande et livraison.','Le processus SAP comprend aussi des responsabilités d’exécution et de facturation.')],
 ['Microsoft décrit le service d’une vente depuis un magasin ; SAP présente la vente sur stock avec ses documents de livraison. Le choix du lieu ne change pas l’attente du client d’être livré.', 'FLOW conserve ce mode de satisfaction dans Sales Order. La capacité suit l’attendu ; préparer, transporter et remettre le produit conservent leurs responsabilités propres.'],
 ex('store','Un magasin expédie','Une commande demande trois articles à une adresse ; un magasin du réseau est retenu pour les expédier.','Le suivi distingue prise en charge, départ et résultat attendu.','Accepter la commande au magasin ne prouve pas qu’elle est déjà livrée.'))

card('BHV067',
 'Permettre au client de retirer ce qui lui est destiné au lieu convenu. Customer Pickup distingue la disponibilité pour retrait de la remise effectivement effectuée.',
 'Commande client à retirer, lieu, échéance et quantité restante.',
 'Suivre préparation puis retrait réel, y compris partiel.',
 [cmp('pos','Le lieu et la date de retrait appartiennent au parcours client.','Une commande de retrait peut être créée dans un autre magasin que celui de remise.'),cmp('store','Le retrait réel fait l’objet d’une étape propre.','Les statuts de facturation Microsoft ne constituent pas une définition universelle du retrait.')],
 ['Microsoft Commerce décrit le choix du retrait dans la commande puis sa réalisation par le magasin. Les deux pages séparent la promesse de mise à disposition de l’action de remise.', 'FLOW reprend cette distinction pour expliquer ce qui attend encore le client. Prêt à retirer ne signifie pas retiré.'],
 ex('store','Retrait en deux fois','Deux articles sont prêts ; le client n’en emporte qu’un aujourd’hui.','Un article reste à remettre selon les conditions applicables.','Le retrait partiel ne solde pas automatiquement toute la commande.'))

card('BHV068',
 'Satisfaire la commande client par un envoi direct du fournisseur. Direct Delivery, côté Sales Order, conserve ce que le client attend et son lien avec l’achat qui le couvre.',
 'Demande client servie directement par le fournisseur.',
 'Rapprocher l’attente client et les réalisations fournisseur, sans doubler les quantités.',
 [cmp('direct','La vente est reliée à l’achat qui organise l’envoi direct.','Les dates fournisseur ne doivent pas devenir une promesse client sans règle explicite.'),cmp('supply','Le dropship sert une vente sans passage dans le dépôt propre.','La coordination d’approvisionnement Oracle ne remplace pas le suivi du client.',concept='Drop ship sales fulfillment',scope='Vente satisfaite directement par le fournisseur.',approach='Relier le résultat client à l’approvisionnement direct.')],
 ['Microsoft décrit le couplage des lignes d’achat et de vente ; Oracle le situe dans l’orchestration du dropship. Les deux relient un engagement fournisseur à une attente client.', 'FLOW donne à la vente son propre point de vue, complémentaire du comportement d’achat BHV059. Une seule livraison peut satisfaire les deux attentes liées ; elle ne compte pas deux fois.'],
 ex('direct','Le client attend le reliquat','Sur 15 pièces vendues, cinq sont déjà livrées ; les dix restantes passent en livraison directe.','La vente conserve l’historique des cinq et l’attendu des dix.','Le mécanisme suit les quantités concernées, sans réécrire la réalisation antérieure.'),
 'Deux sources centrées sur le dropship ; l’exemple numérique est une illustration FLOW du mécanisme de livraison partielle décrit par Microsoft.')

card('BHV069',
 'Suivre une vente entre sociétés du groupe en conservant les engagements de chacune. Intercompany Sales qualifie la relation commerciale et peut se combiner avec une livraison directe.',
 'Commandes liées de sociétés juridiquement distinctes.',
 'Relier ventes et achats internes sans confondre sociétés, flux physiques et client final.',
 [cmp('inter','Les chaînes associent plusieurs commandes de sociétés distinctes.','Le nombre de documents dépend du montage retenu.'),cmp('sapinter','La société vendeuse et la société livreuse peuvent différer.','Le parcours avancé SAP ajoute des liens absents de son parcours classique.')],
 ['Microsoft présente des chaînes à deux ou trois branches ; SAP distingue intercompany classique et avancé. Les deux couvrent la relation entre sociétés, avec des documents différents.', 'FLOW conserve cette dimension plutôt qu’une catégorie de livraison exclusive. Une vente intercompany peut donc rester liée à un envoi direct au client final.'],
 ex('sapinter','Vendeur et livreur différents','Le cours SAP montre une société vendeuse en Allemagne et une société livreuse aux États-Unis pour servir le client.','Le parcours avancé relie les commandes internes nécessaires.','La localisation du départ et la relation commerciale doivent être expliquées séparément.',True))

card('BHV070',
 'Faire arriver le premier stock au site avant son lancement. Initial Stocking, côté Transfer Order, suit le transfert d’implantation décidé pour une saison, une capsule ou une ouverture.',
 'Transfert initial, assortiment attendu et date de démarrage.',
 'Suivre l’apport retenu jusqu’au site ; distinguer décision d’implantation et déplacement effectif.',
 [cmp('nextail','First Allocation distingue la première distribution du réassort.','Nextail traite l’optimisation de l’apport ; FLOW décrit ici l’ordre qui le porte.',concept='First Allocation',scope='Première distribution des nouveaux produits.',approach='Proposer où et combien implanter.'),cmp('to','Un ordre suit quantités et dates entre deux lieux.','Microsoft ne nomme pas une variante Initial Stocking dans cette page.')],
 ['Nextail éclaire l’intention du premier apport ; Microsoft documente le transfert qui peut le réaliser. Ni le calcul de distribution ni la commande de déplacement ne suffisent seuls à dire que le magasin est prêt.', 'FLOW conserve Initial Stocking pour cette intention métier, distincte du réassort continu. Le comportement suit l’exécution de l’apport décidé sans refaire la décision de quantités.'],
 ex('nextail','Préparer l’ouverture','Un site doit ouvrir avec un assortiment initial apporté depuis l’entrepôt.','Chaque quantité retenue donne un attendu de transfert avant l’ouverture.','Le modèle sépare le choix de l’assortiment et le suivi du déplacement.'))

card('BHV071',
 'Approvisionner régulièrement les sites pendant leur activité. Continuous Replenishment suit les transferts de réassort et ce qu’il reste à recevoir.',
 'Apports de réassort entre sites en cours de période.',
 'Suivre les commandes issues du besoin de réassort avec leurs quantités, dates et arrivées.',
 [cmp('towh','Le besoin d’un dépôt peut produire un transfert depuis son dépôt de couverture.','La règle Microsoft n’impose pas une origine ou une fréquence unique.'),cmp('nextail','Replenishment traite la distribution continue.','L’optimisation Nextail décide des apports ; le comportement FLOW suit les transferts retenus.',concept='Replenishment',scope='Réassort pendant la période de vente.',approach='Adapter les apports à l’évolution du besoin.')],
 ['Microsoft montre une relation de couverture entre dépôts ; Nextail ajuste la distribution retail en cours de période. Le premier formalise une origine de transfert, le second met l’accent sur l’évolution du besoin.', 'FLOW garde le suivi de l’apport continu comme intention du Transfer Order. Le stock initial et le réassort peuvent utiliser des documents semblables tout en répondant à des enjeux différents.'],
 ex('towh','Compléter le magasin','Les ventes ont diminué le stock d’un magasin ; un transfert de 18 pièces est attendu jeudi.','Le suivi distingue quantité demandée, départ et arrivée.','La décision de 18 pièces reste explicable en amont du transfert.'))

card('BHV072',
 'Déplacer un excédent vers un site qui en a davantage besoin. Inventory Rebalancing suit les transferts retenus pour corriger un déséquilibre du réseau.',
 'Transferts entre sites donneurs et receveurs.',
 'Conserver l’intention de rééquilibrage et suivre le déplacement décidé.',
 [cmp('rebal','Les excédents peuvent couvrir les manques ailleurs dans le réseau.','Oracle décrit surtout le calcul et la libération du plan.'),cmp('nextail','Store Transfers redistribue le stock entre magasins.','Le périmètre retail Nextail n’est pas toutes les formes de transfert FLOW.',concept='Store Transfers',scope='Rééquilibrage entre magasins.',approach='Déplacer selon les possibilités de vente attendues.')],
 ['Oracle oppose excédents et manques ; Nextail examine les possibilités de vente entre magasins. Les deux recherchent une meilleure utilisation du stock existant, avec des objectifs formulés différemment.', 'FLOW distingue la décision de rééquilibrage et les transferts à suivre. Déplacer un excédent n’est pas automatiquement le même besoin que regrouper des reliquats ou préparer une ouverture.'],
 ex('rebal','Réduire un déséquilibre','Un magasin a 30 pièces peu demandées ; un autre risque de manquer de dix pièces.','Un transfert retenu permet de déplacer une partie de l’excédent.','Les quantités sont illustratives ; le comportement porte le transfert, pas le calcul de l’optimum.'))

card('BHV073',
 'Regrouper des stocks dispersés pour retrouver une offre plus utile, par exemple une série de tailles. Stock Consolidation suit cette intention propre, souvent en fin de saison.',
 'Transferts de reliquats vers les sites de regroupement retenus.',
 'Conserver le motif de consolidation et suivre les quantités effectivement regroupées.',
 [cmp('merkal','Le regroupement peut améliorer la disponibilité des tailles.','Le témoignage ne prouve pas une méthode universelle ni son résultat chez Beaumanoir.'),cmp('rebal','Le stock existant est redistribué entre sites.','Excédent vers manque ne suffit pas à définir la consolidation d’une série.')],
 ['Nextail décrit chez Merkal une consolidation liée aux tailles ; Oracle présente le rééquilibrage excédent/manque. Le mouvement peut se ressembler, mais son bénéfice attendu diffère.', 'FLOW garde Stock Consolidation pour rendre visible le regroupement de fragments utiles ensemble. Le motif ne se réduit pas à remplir un site déficitaire.'],
 ex('merkal','Regrouper les tailles chez Merkal','Le cas publié par Nextail évoque les transferts de fin de saison et une meilleure consolidation des tailles.','Le regroupement vise une offre de tailles plus utilisable.','FLOW retient ce bénéfice de regroupement, sans reprendre de gain chiffré ni en déduire une installation locale.',True))

card('BHV074',
 'Faire venir le stock nécessaire à une commande identifiée. Order-Driven Transfer conserve le lien entre ce déplacement et la demande qu’il doit permettre de satisfaire.',
 'Transfert dédié ou lié à une commande et à son échéance.',
 'Maintenir le lien de satisfaction et suivre l’arrivée utile à la commande.',
 [cmp('b2b','Un transfert peut approvisionner spécifiquement une vente.','Back-to-back comporte des règles de liaison propres à Oracle.'),cmp('to','La commande client peut rendre visibles ses transferts entrants.','La visibilité du lien ne garantit pas à elle seule la promesse client.')],
 ['Oracle formalise une chaîne back-to-back pour procurer la ressource d’une vente ; Microsoft expose les transferts liés dans la gestion des commandes. Les deux rendent la demande d’origine visible.', 'FLOW conserve ce lien comme intention métier distincte du réassort général. Un retard de transfert doit pouvoir être rapproché de la commande concernée.'],
 ex('b2b','Une pièce arrive pour une vente','Un client attend une référence absente du site de service mais disponible dans un autre dépôt.','Un transfert est relié à cette vente et à sa date utile.','La réception future reste un attendu ; elle ne prouve pas une livraison client déjà faite.'))

card('BHV078',
 'Comprendre la réponse du fournisseur avant d’en faire un engagement applicable. Supplier Confirmation distingue la commande envoyée, la proposition reçue et l’accord retenu.',
 'Réponses fournisseur sur quantités, dates et conditions.',
 'Conserver les écarts proposés et leur acceptation, avec les conséquences sur la demande.',
 [cmp('vendor','Le fournisseur peut accepter, refuser ou demander des changements.','Une réponse avec écart ne se confirme pas comme une acceptation inchangée.'),cmp('ubl','Order Response distingue acceptation, refus et contre-proposition.','Le message normalisé ne détermine pas l’autorité interne qui accepte l’écart.',concept='Order Response',scope='Réponse du vendeur à une commande.',approach='Expliciter l’accord, le refus ou la contre-proposition.')],
 ['OASIS décrit le sens d’une réponse échangée ; Microsoft montre son traitement et la confirmation qui peut suivre. La réception du message et son effet sur l’engagement sont deux questions.', 'FLOW garde les trois lectures : demandé, répondu, accepté. Un fournisseur annonçant une date n’établit pas automatiquement ce que le client final peut se voir promettre.'],
 ex('vendor','Une quantité inférieure proposée','Le fournisseur répond 80 pièces au lieu des 100 demandées, à la même date.','L’écart de 20 reste visible jusqu’à décision.','La réponse est connue ; son acceptation et les conséquences sur les engagements restent à traiter.'),
 'La revue détaillée des changements Microsoft reste mobilisée dans BHV038 ; la page SAP de confirmation est remplacée par UBL Order Response pour comparer message métier et parcours produit.')

card('BHV086',
 'Traiter ensemble des commandes qui doivent rester distinctes. Order Grouping conserve les identités tout en portant les conditions communes de leur traitement.',
 'Ensemble de commandes ou lignes liées, sans remplacement par une commande unique.',
 'Rendre le groupe et ses contraintes explicites en préservant chaque demande.',
 [cmp('set','Des lignes distinctes peuvent devoir partir ensemble.','Un Shipment Set est un cas particulier de groupe.'),cmp('release','Plusieurs commandes peuvent contribuer à une expédition selon les règles.','Le regroupement logistique ne fusionne pas leurs engagements commerciaux.')],
 ['Oracle forme un ensemble à contraintes communes ; Microsoft peut regrouper des lignes lors du lancement vers le dépôt. Les deux gardent des demandes distinctes sous un traitement collectif.', 'FLOW choisit Grouping pour cette conservation des identités. La contrainte commune doit être nommée : même départ, complétude ou autre condition explicite.'],
 ex('set','Un équipement livré ensemble','Oracle illustre un ordinateur, un écran, une souris et un clavier regroupés pour l’expédition.','Les lignes gardent leur identité ; des colis séparés restent possibles.','Grouper porte la condition commune, pas nécessairement l’emballage unique.',True))

card('BHV087',
 'Remplacer plusieurs commandes compatibles par une commande résultante. Order Merging conserve leur origine et vérifie ce que la fusion change aux quantités et engagements.',
 'Commandes d’origine, commande résultante et conditions de compatibilité.',
 'Tracer la filiation et les effets de remplacement, au-delà d’un simple groupe d’affichage.',
 [cmp('merge','La commande résultante remplace les commandes réunies avec des liens d’origine.','Infor limite le mécanisme à des achats compatibles et à certains états.'),cmp('firm','Des propositions peuvent être réunies lors de la création d’un achat ferme.','Regrouper pendant l’affermissement n’est pas nécessairement fusionner des commandes déjà engagées.')],
 ['Infor décrit une fusion d’achats existants compatibles ; Microsoft réunit des propositions lors de leur affermissement. Le résultat peut être une commande unique, mais le point de départ n’a pas le même engagement.', 'FLOW retient Merging lorsque les identités d’origine sont remplacées par une demande résultante traçable. Les conditions commerciales ne doivent pas changer silencieusement.'],
 ex('merge','Deux achats deviennent un','Deux achats compatibles du même fournisseur sont réunis dans une commande résultante.','Les lignes et quantités d’origine restent explicables depuis le résultat.','La fusion exige de suivre le remplacement et ses conséquences, pas seulement d’additionner les totaux.'))

src('relex','RELEX','Replenishment and allocation','Automatic Replenishment System','https://www.relexsolutions.com/solutions/automatic-replenishment-system/',EV,'Manage the full cycle for seasonal items ; Manage seasons effectively','Initial allocation','Première distribution saisonnière, puis réassort.', 'Articuler avant-saison, apport initial et vie de la saison.','Initial allocation est distincte du réassort pendant la saison.','Présentation commerciale primaire ; aucune performance chiffrée ni installation locale déduite.')
src('logility','Logility','Retail optimization','Retail Optimization Gives Groupe Dynamite an Edge','https://www.logility.com/webcast/retail-optimization-gives-groupe-dynamite-an-edge/',EV,'Présentation écrite du webcast ; initial distribution and replenishment','Initial distribution','Premier apport de produits, tailles et assortiments aux magasins.','Distinguer distribution initiale et réassort selon les lieux.','La présentation Groupe Dynamite mentionne la distribution initiale et des courbes style/couleur/taille par canal.','Présentation écrite primaire consultée ; vidéo non visionnée. Témoignage fournisseur, sans gains chiffrés ni preuve locale.')
src('ascm','ASCM','Supply chain knowledge','What Is Logistics?','https://www.ascm.org/topics/logistics/',EV,'Order processing and fulfillment ; Outbound ; Reverse logistics','Order processing and fulfillment','Activités allant du traitement de commande au produit arrivé à destination.','Organiser et réaliser préparation, emballage et expédition.','ASCM inclut les activités physiques jusqu’à destination dans le fulfillment.','Texte primaire indexé consulté après erreur à l’ouverture ; page logistique générale, pas définition universelle de toutes les commandes FLOW.')

card('TER010',
 'Nommer ce qui manque ou le résultat recherché avant de choisir comment le demander. Besoin reste une convention locale plus large qu’une commande déjà formalisée.',
 'Résultat souhaité ou manque, exprimé ou encore à préciser.',
 'Distinguer le besoin, sa formulation en demande et la réponse retenue.',
 [cmp('safety','Un manque à couvrir peut exister sans commande client.','Le besoin de sécurité chiffré est un cas particulier, pas la définition de tout besoin.'),cmp('supply','Une demande d’approvisionnement vise un résultat à obtenir.','L’objet Supply Request d’Oracle est déjà formalisé et plus étroit que le sens local.',concept='Supply request',scope='Demande formalisée d’un apport.',approach='Exprimer l’approvisionnement requis pour le traiter.')],
 ['Microsoft montre un besoin issu d’un seuil de stock ; Oracle traite une demande d’approvisionnement déjà identifiée. Les deux se situent à des moments différents de sa formalisation.', 'FLOW conserve Besoin pour parler du résultat recherché même avant une commande. Ce rapprochement éclaire la convention, sans transformer le terme en objet universel adopté.'],
 ex('safety','Un stock trop faible avant commande','Un stock risque de passer sous son minimum ; aucun achat n’a encore été lancé.','Un besoin de couverture est identifié.','Identifier ce besoin ne prouve ni une demande acceptée ni une ressource promise.'))

card('TER011',
 'Rendre identifiable ce que quelqu’un souhaite obtenir. Demande précise le résultat et, lorsque cela a du sens, l’objet, la quantité, l’échéance et le bénéficiaire.',
 'Expression suivable d’un résultat souhaité.',
 'Conserver l’expression initiale sans lui attribuer acceptation, promesse ou couverture.',
 [cmp('supply','La Supply Request exprime un apport attendu.','Oracle définit un objet d’approvisionnement ; FLOW conserve une notion plus générale.',concept='Supply request',scope='Demande d’approvisionnement à traiter.',approach='Transmettre le résultat et les caractéristiques requis.'),cmp('ubl','La commande émise et la réponse reçue sont distinctes.','Order est une forme précise de demande commerciale, pas le mot Demande dans tous ses usages.',concept='Order / response',scope='Instruction d’achat et réponse du vendeur.',approach='Distinguer expression et acceptation.')],
 ['Oracle montre une demande adressée à l’orchestration ; OASIS distingue l’ordre commercial de sa réponse. Tous deux permettent de séparer ce qui est demandé de ce qui est accepté.', 'FLOW retient cette séparation de sens. La convention ne crée pas un objet unique qui remplacerait toutes les familles de commandes ou de demandes.'],
 ex('ubl','Demander n’est pas obtenir','Un acheteur demande 40 pièces pour jeudi ; le fournisseur n’a pas encore répondu.','La demande est identifiable mais non confirmée par cette seule émission.','Quantité demandée, quantité promise et quantité reçue restent trois notions distinctes.'))

card('TER012',
 'Formaliser une instruction et ses conditions pour pouvoir la suivre. Commande doit être qualifiée par son contexte : client, achat ou ordre de déplacement, par exemple.',
 'Acte ou document exprimant une instruction commerciale ou opérationnelle.',
 'Préciser la famille et ses effets, sans supposer confirmation ni exécution à l’enregistrement.',
 [cmp('ubl','Order formalise un achat de biens ou services.','UBL vise les échanges acheteur–vendeur, pas tous les ordres opérationnels.',concept='Order',scope='Document d’instruction commerciale.',approach='Exprimer la commande entre parties.'),cmp('to','Transfer Order formalise un déplacement demandé.','Il ne constitue pas nécessairement une vente ou un achat entre deux parties commerciales.')],
 ['OASIS donne à Order un sens commercial d’échange ; Microsoft emploie Transfer Order pour un déplacement entre dépôts. Le mot Order ne suffit donc pas à déterminer la relation métier.', 'FLOW conserve Commande comme terme à qualifier. Aucun schéma universel de commande ni effet d’engagement automatique n’est déduit de ce rapprochement.'],
 ex('to','Un ordre de déplacement','Un document demande de déplacer 20 pièces du dépôt A vers B lundi.','La commande porte cette instruction ; départ et réception restent à constater.','La nature opérationnelle de l’ordre doit être précisée avant d’en déduire ses effets.'))

card('TER032',
 'Nommer l’achat dans lequel le donneur d’ordre procure des composants et confie leur transformation. Fabrication à façon conserve ce sens de travail local, avec les responsabilités à préciser.',
 'Composants acquis puis confiés à un façonnier pour transformation.',
 'Préciser les biens fournis, leur propriété et le résultat acheté sans assimiler tous les montages de sous-traitance.',
 [cmp('subcontract','Le donneur d’ordre fournit des composants au transformateur.','Le montage SAP précise des règles de stock et propriété non automatiquement établies dans le contexte local.'),cmp('b2b','Contract Manufacturing relie fabrication externe et achat.','Ce terme Oracle peut couvrir d’autres répartitions de responsabilités que la fabrication à façon rapportée.',concept='Contract manufacturing',scope='Fabrication confiée à un partenaire.',approach='Relier ordre de fabrication et achat externe.')],
 ['SAP Subcontracting insiste sur les composants fournis ; Oracle Contract Manufacturing organise les documents d’une fabrication externe. Le recouvrement est réel mais leurs montages ne sont pas synonymes exacts.', 'FLOW conserve le sens rapporté par Laurent. Les sources aident à poser les questions de propriété et de consommation ; elles ne répondent pas à la place de l’étude du cas local.'],
 ex('subcontract','Transformer des composants confiés','Un donneur d’ordre achète du tissu et le confie pour confectionner des pièces.','Le résultat transformé est attendu, avec les composants fournis identifiés.','L’illustration rend le mécanisme concret ; elle ne décrit pas un flux installé chez Beaumanoir.'))

card('TER033',
 'Conserver le nom rapporté pour le document émis par MAP dans le cas U48. Planned Purchase Order ne dit pas encore, dans ce contexte local, si la commande est ferme.',
 'Nom historique d’un document local, après planification en volumes et délais.',
 'Qualifier son engagement et son cycle avant toute équivalence avec un objet éditeur.',
 [cmp('firm','Planned purchase order peut désigner une proposition à affermir.','Cet usage Microsoft ne démontre pas la nature du document MAP.',concept='Planned purchase order',scope='Proposition d’achat issue du plan.',approach='Transformer la proposition en commande par affermissement.'),cmp('epp','Le même nom existe chez Oracle Purchasing.','Chez Oracle EBS, il peut porter un engagement long terme avec livraisons précisées ensuite.',concept='Planned Purchase Order',scope='Engagement d’achat avec échéances encore prévisionnelles.',approach='Préciser les livraisons par releases.')],
 ['Microsoft et Oracle emploient des noms très proches pour des engagements différents : proposition à affermir d’un côté, achat long terme décliné ensuite de l’autre.', 'FLOW conserve donc la réserve du terme MAP. Le nom ne permet pas de choisir entre Planned Order, Purchase Requisition et Purchase Order ni de fermer la question locale.'],
 ex('firm','Le nom du fichier ne suffit pas','Un document MAP porte « Planned Purchase Order » après planification.','Avant rapprochement, il faut établir ce qu’il engage envers le fournisseur.','Le passage Microsoft à l’ordre ferme fournit une question de comparaison, pas une réponse sur MAP.'),
 'Statut lexical historique conservé ; aucune équivalence du document MAP, clôture de Q034 ou adoption nouvelle déduite de la recherche.')

card('TER038',
 'Décrire la situation d’un objet à un instant donné. État d’objet métier couvre les valeurs utiles et ne se limite pas à une étiquette de statut.',
 'Situation courante ou représentée à une date donnée.',
 'Distinguer dimensions de l’état, document qui les montre et événement qui les change.',
 [cmp('po','Approbation, document et quantités ont des statuts distincts.','Leur liste est propre aux achats Microsoft.'),cmp('statuses','Commande, ligne et tâche peuvent progresser différemment.','Un résumé Oracle n’est pas l’état complet de tout objet métier.')],
 ['Microsoft sépare plusieurs dimensions d’un achat ; Oracle distingue les niveaux de progression de la vente. Les deux montrent qu’un seul statut peut masquer une situation plus riche.', 'FLOW conserve État pour la situation et les valeurs pertinentes. Un document daté en donne une représentation ; l’événement explique comment elle a changé.'],
 ex('po','Approuvée et partiellement reçue','Une commande d’achat est approuvée, avec 60 pièces reçues sur 100.','Son état combine accord et quantité restante.','« Approuvée » ne permet pas à lui seul de connaître les 40 encore attendues.'))

card('TER064',
 'Rassembler les informations et actions nécessaires pour traiter une situation. Case désigne un dossier, distinct d’une commande et sans être un univers ou niveau du modèle FLOW.',
 'Dossier d’une situation, demande ou problème à résoudre.',
 'Relier pièces, échanges et activités autour de la situation suivie.',
 [cmp('cmmn','Le dossier évolue avec les informations et décisions.','CMMN est une notation de traitement adaptatif ; le terme FLOW n’impose pas son formalisme.'),cmp('case','Plusieurs contacts peuvent relever du même dossier.','Le produit peut aussi lier un ordre de service ; Case et Order ne deviennent pas synonymes.')],
 ['OMG traite la structure d’un dossier adaptable ; Microsoft donne des exemples d’utilisation opérationnelle. Leur point commun est de réunir des éléments autour d’une situation, même si les actions ne sont pas toutes prévues au départ.', 'FLOW conserve ce vocabulaire utile sans recréer l’univers Business Services retiré. Le dossier peut référencer une commande et garder une finalité différente.'],
 ex('case','Plusieurs appels pour une panne','Dans l’exemple Microsoft City Power & Light, plusieurs appels sur une panne électrique sont rattachés au même cas.','Le dossier est relié à l’ordre de service ouvert pour la panne.','Un dossier regroupe le traitement de la situation ; l’ordre porte une instruction distincte.',True))

card('TER065',
 'Désigner une commande dont la Supply travaille la couverture, les priorités et la promesse. Supply Order est ici un terme local ; son sens est plus large que l’objet homonyme Oracle.',
 'Commandes considérées du point de vue de leur satisfaction Supply.',
 'Préciser la famille de commande avant de parler de ses ressources et engagements.',
 [cmp('supply','Oracle relie une demande aux ordres qui procurent la ressource.','Son Supply Order est un objet d’approvisionnement, pas toutes les commandes prises en charge par la Supply.'),cmp('b2b','Demande client et approvisionnement sont reliés.','La chaîne Oracle conserve justement des rôles distincts entre vente et fourniture.')],
 ['Oracle utilise Supply Order pour orchestrer l’apport, et distingue en back-to-back la vente qui le motive. Deux documents du même éditeur éclairent cet usage précis, sans établir le sens du terme partout sur le marché.', 'FLOW conserve son vocabulaire local plus large. Lire Supply Order dans une documentation Oracle exige donc de vérifier le périmètre avant de rapprocher les objets.'],
 ex('b2b','La vente et son apport','Une vente conduit à un transfert pour obtenir le produit.','La vente et le transfert restent deux commandes avec leurs attendus propres.','Le point de vue Supply peut porter sur les deux ; cela ne les transforme pas en un seul objet Oracle.'))

card('TER069',
 'Nommer la commande qui exprime ce que le client demande. Sales Order désigne ici l’objet métier ; la capacité homonyme décrit l’activité qui le prend en charge.',
 'Biens, quantités et conditions demandés par le client.',
 'Conserver la demande distincte de sa promesse et de ses documents de livraison.',
 [cmp('pos','La commande client porte des modalités de remise différentes.','Le périmètre Commerce reste orienté vente en magasin.'),cmp('sapsales','La commande est distincte de la livraison et de la facture.','Le processus SAP est plus large que l’objet défini ici.')],
 ['Microsoft montre les variantes de remise d’une commande client ; SAP situe la commande avant les documents de réalisation. Les deux donnent au même objet une place dans un parcours plus large.', 'FLOW reprend le nom établi pour la commande, sans confondre l’objet et la capacité Sales Order. L’adoption du nom de capacité ne valide pas automatiquement toute définition lexicale.'],
 ex('pos','Une commande à retirer','Le client commande deux articles pour retrait samedi.','La commande conserve les deux articles et le lieu convenu.','Le fait qu’elle existe ne prouve ni sa disponibilité ni son retrait.'))

card('TER070',
 'Nommer la commande qui exprime ce qui est acheté à un fournisseur. Purchase Order inclut biens et prestations, avec leurs conditions applicables.',
 'Attendu d’achat adressé au fournisseur.',
 'Distinguer commande, accord de référence et simple apport consigné sans achat.',
 [cmp('pocreate','Les lignes d’achat couvrent produits et services.','La structure d’écran Microsoft n’est pas un schéma imposé au terme FLOW.'),cmp('potypes','Commande et accord d’achat n’ont pas le même contenu d’engagement.','Oracle autorise des noms locaux de documents ; le nom seul ne suffit donc pas.')],
 ['Microsoft explicite ce qu’une commande peut acheter ; Oracle la distingue des accords préalables. Le recouvrement porte sur un attendu fournisseur suffisamment précisé.', 'FLOW conserve Purchase Order pour cet achat, distinct de la capacité qui le gère et du bon de commande qui en représente une version. La consignation sans engagement d’achat garde une autre qualification.'],
 ex('potypes','Un accord puis une commande','Un accord prévoit des conditions pour la saison ; une commande demande ensuite 50 pièces pour une date précise.','Les deux restent liés mais n’expriment pas le même attendu.','Le volume commandé ne se déduit pas de la seule existence de l’accord.'))

card('TER071',
 'Nommer l’ordre qui demande un déplacement entre deux lieux. Transfer Order porte les quantités et échéances attendues ; il n’est ni le départ ni l’arrivée.',
 'Déplacement de marchandises demandé, origine et destination.',
 'Conserver l’instruction et rapprocher ses réalisations distinctes.',
 [cmp('to','Origine, destination et progression décrivent le même ordre.','Les champs d’intégration Microsoft ne sont pas une définition universelle.'),cmp('towh','Un besoin de réassort peut devenir une commande de transfert.','Un ordre peut aussi répondre à une autre intention que ce calcul de planification.')],
 ['Microsoft IOM expose l’objet et son suivi ; SCM décrit un mode de production de l’ordre depuis les besoins. Leur point commun est le déplacement demandé, avec des vues différentes sur son origine.', 'FLOW retient ce sens d’objet. La capacité Transfer Order gère l’ordre ; les faits de départ et de réception constatent sa réalisation.'],
 ex('to','Le document précède le mouvement','Un ordre prévoit 30 pièces entre deux sites demain.','L’ordre est connu avant que les marchandises ne partent.','Il porte un attendu, pas un stock déjà arrivé à destination.'))

card('TER072',
 'Nommer la commande qui porte le retour du client. Customer Return Order conserve une identité distincte de la vente d’origine, tout en pouvant lui être reliée.',
 'Marchandises que le client retourne et suite attendue.',
 'Conserver le retour et son lien d’origine sans effacer la vente réalisée.',
 [cmp('sapret','Le retour a ses propres documents et suites.','Crédit, remplacement et logistique ne se résument pas au nom du document.'),cmp('gp','Le RMA organise une prise en charge de retour client.','RMA peut insister sur l’autorisation et le parcours ; ce n’est pas un synonyme exact dans tout produit.',concept='Return Material Authorization',scope='Retour client identifié avec son résultat.',approach='Suivre le retour et les documents associés.')],
 ['SAP parle de commande de retour ; Dynamics GP organise un RMA. Les noms diffèrent et leurs effets dépendent du parcours, mais les deux conservent un traitement distinct de la vente.', 'FLOW retient Customer Return Order pour l’objet demandé. Le nom n’impose ni remboursement immédiat ni remise en stock automatique.'],
 ex('sapret','La vente reste dans l’histoire','Après livraison, le client retourne une pièce pour examen.','Une commande de retour la prend en charge et peut référencer la vente.','La pièce livrée ne devient pas rétroactivement une pièce jamais livrée.'))

card('TER073',
 'Nommer la commande qui porte un renvoi de marchandises au fournisseur. Supplier Return Order reste distinct de l’achat d’origine et indique la suite attendue.',
 'Renvoi fournisseur, quantités et contrepartie ou restitution attendue.',
 'Relier retour et achat sans assimiler avoir, remplacement et réparation.',
 [cmp('bcret','Purchase Return Order désigne le document de renvoi.','Le nom Microsoft est proche mais les suites dépassent un avoir unique.'),cmp('gp','RTV distingue notamment crédit, remplacement et réparation.','La terminologie propre à GP ne rend pas tous les retours identiques.',concept='Return to Vendor',scope='Retour fournisseur avec résultat qualifié.',approach='Suivre le type de suite attendu après renvoi.')],
 ['Business Central met l’accent sur la commande de retour d’achat ; Dynamics GP sur le Return to Vendor et ses variantes. Tous deux gardent la relation au fournisseur, avec des découpages documentaires propres.', 'FLOW retient Supplier Return Order pour l’objet de renvoi. Le choix de résultat appartient à son contenu ; il ne se déduit pas du seul mouvement sortant.'],
 ex('bcret','Un retour lié à l’achat','Cinq pièces non conformes sont renvoyées au fournisseur avec attente de remplacement.','Le renvoi est identifié séparément de l’achat initial.','Le lien conserve l’origine ; il n’efface pas la réception déjà constatée.'))

card('TER079',
 'Nommer le premier apport qui permet de démarrer la saison en stock. Implantation garde le sens donné par Laurent ; Initial Stocking est le terme anglais retenu dans FLOW.',
 'Livraison initiale de stock au début de la période concernée.',
 'Distinguer choix des apports, commandes de déplacement et livraison effective.',
 [cmp('nextail','First Allocation traite la première distribution de nouveaux produits.','Allocation nomme ici une décision retail ; ce n’est pas automatiquement Supply Assignment.',concept='First Allocation',scope='Première distribution avant les ventes.',approach='Déterminer les quantités initiales par magasin.'),cmp('relex','Initial allocation est distinguée du réassort en saison.','RELEX décrit une fonction d’optimisation, alors que le terme local vise la livraison initiale.'),cmp('logility','Initial distribution désigne le premier apport, distinct du réassort.','Le témoignage n’établit pas une nomenclature commune aux trois éditeurs.')],
 ['Nextail emploie First Allocation, RELEX Initial allocation et Logility Initial distribution. Les trois distinguent premier apport et réassort ; leurs noms insistent différemment sur le choix ou la distribution.', 'FLOW garde Initial Stocking pour l’intention métier d’implantation. Décider les apports et réaliser la livraison restent séparés ; ces sources ne prouvent aucune cadence cible ni pratique locale supplémentaire.'],
 ex('logility','Première distribution chez Groupe Dynamite','La présentation Logility évoque une meilleure distribution initiale et des courbes style/couleur/taille adaptées aux canaux.','Premier apport et réassort sont présentés comme deux moments à améliorer.','FLOW retient cette distinction d’intention, sans reprendre un gain mesuré ni assimiler le calcul à la livraison.',True),
 'RELEX, Nextail et la présentation écrite Logility conservés et réexaminés ; vidéo non visionnée. SAP Help CARAB vide ; UBL est moins direct pour ce sens lexical. Le terme anglais adopté reste Initial Stocking.')

card('TER085',
 'Parler de la satisfaction effective d’une commande, depuis son organisation jusqu’à sa réalisation. Fulfillment ne se réduit ni à calculer une promesse ni à réserver un stock.',
 'Activités qui organisent et réalisent le résultat attendu.',
 'Préciser la commande et son résultat ; distinguer choix, engagement et exécution.',
 [cmp('store','Fulfillment inclut préparation, expédition et retrait effectif.','La page porte les commandes servies par les magasins.'),cmp('ascm','Fulfillment comprend les activités jusqu’au produit arrivé à destination.','La page ASCM décrit surtout les flux de produits ; l’extension à d’autres commandes doit être explicitée.')],
 ['Microsoft décrit le fulfillment en magasin ; ASCM l’inscrit dans la chaîne des activités logistiques jusqu’à destination. Les deux incluent une réalisation physique, avec une maille opérationnelle pour l’un et plus générale pour l’autre.', 'FLOW conserve un sens large, à préciser selon le résultat de chaque commande. Ce terme ne crée pas une nouvelle capacité qui absorberait les responsabilités déjà distinguées.'],
 ex('store','Du choix du stock à la remise','Une commande est affectée à un magasin, préparée puis remise au client.','Le résultat attendu est accompli lorsque les conditions de service sont réalisées.','La sélection du magasin prépare la satisfaction ; elle n’en est pas la preuve.'),
 'IFO réexaminé mais écarté du tableau lexical court car il décrit l’optimisation spécialisée. ASCM conservé à partir du texte primaire indexé après erreur d’ouverture ; aucune définition universelle des retours ou services numériques déduite.')

card('TER086',
 'Nommer le bon qui représente la commande d’achat à un moment donné. Purchase Order Document distingue ce support, la commande suivie et la capacité qui la gère.',
 'Représentation datée du contenu d’une commande d’achat.',
 'Identifier la version représentée sans assimiler le document au cycle de vie complet de la commande.',
 [cmp('ubl','Order est explicitement un document échangé.','Le format UBL ne prescrit pas la séparation conceptuelle objet/capacité choisie par FLOW.',concept='Order document',scope='Document d’échange d’une commande de biens ou services.',approach='Exprimer le contenu adressé à l’autre partie.'),cmp('bcarchive','Les documents d’achat peuvent conserver plusieurs versions.','La restauration dépend du produit ; tout document n’est pas une commande réactivable.')],
 ['OASIS décrit ce qu’un document Order transmet ; Business Central montre que ses versions peuvent être conservées. Les deux éclairent la représentation d’un contenu, avec des objectifs différents.', 'FLOW emploie Purchase Order Document pour lever l’ambiguïté du bon de commande. Un document émis hier peut rester une preuve sans représenter le contenu actuellement applicable.'],
 ex('bcarchive','Deux bons, une commande','Un bon initial prévoit vendredi ; une version ultérieure porte lundi après changement accepté.','Les deux documents peuvent expliquer l’histoire d’une même commande.','Le nombre de versions ne doit pas être pris pour le nombre d’achats.'))

card('VER001',
 'Établir clairement une signification, une règle ou une caractéristique. Définir désigne ici ce travail de cadrage, distinct de l’application de ce qui a été défini.',
 'Sens, caractéristiques ou règles rendus explicites.',
 'Nommer l’objet défini et les effets que son application devra produire.',
 [cmp('plans','Les horizons du plan fixent des règles de protection ou d’affermissement.','C’est un usage de définition de règles, pas une définition normative du verbe français.',concept='Time fence settings',scope='Règles temporelles d’un plan.',approach='Établir les horizons et effets attendus.'),cmp('safety','Le seuil précise une règle de protection du stock.','Définir le minimum ne signifie pas que le stock y satisfait déjà.',concept='Safety stock level',scope='Minimum de stock défini pour un article et un lieu.',approach='Fixer le seuil utilisé par la planification.')],
 ['Les deux documents Microsoft montrent comment établir une règle avant son usage : horizon du plan ou minimum de stock. Ils n’imposent pas un verbe canonique français.', 'FLOW retient Définir comme convention de rédaction. Le résultat doit dire ce qui devient explicite ; la capacité d’appliquer cette règle doit être décrite séparément.'],
 ex('safety','Fixer un minimum','Une règle retient un minimum de 20 pièces pour un article à un site.','Le seuil est défini ; l’analyse peut ensuite constater si le stock y répond.','La définition de la règle ne crée aucune pièce disponible.'))

card('VER002',
 'Exprimer précisément le résultat de maintien à jour plutôt que s’appuyer sur un verbe ambigu. Tenir reste en réexamen et n’est pas proposé comme libellé par défaut.',
 'Sens proposé pour conserver des informations cohérentes et à jour.',
 'Préciser le résultat attendu, par exemple intégrer un changement ou rendre une situation consultable.',
 [cmp('changes','Un changement fournisseur doit être pris en compte avec ses conséquences.','Microsoft décrit une opération précise, pas un équivalent vérifié du verbe Tenir.',concept='Review purchase order changes',scope='Changements de commande fournisseur examinés.',approach='Comparer puis accepter les valeurs modifiées.'),cmp('statuses','La situation suivie doit refléter les progressions pertinentes.','La documentation de statuts ne justifie pas un libellé français générique.')],
 ['Microsoft décrit la revue d’un changement ; Oracle explique les situations de commande visibles. Ces usages montrent des résultats concrets mais n’apportent aucun équivalent lexical commun à Tenir.', 'FLOW conserve donc la réserve exprimée par Laurent. Selon le contexte, mieux vaut dire ce qui est mis à jour, rapproché ou rendu consultable ; aucun renommage n’est adopté ici.'],
 ex('changes','Dire ce qui change','Une réponse fournisseur propose une autre date ; l’information doit être examinée puis intégrée si elle est acceptée.','Le résultat attendu peut être formulé directement.','« Intégrer la date acceptée » explique davantage que « tenir la commande ».'),
 'Réserve U35 maintenue explicitement. Aucun libellé français SAP vérifié, aucune adoption du verbe ni substitution automatique.')

card('VER007',
 'Faire entrer durablement un fait ou une décision dans ce qui est connu. Enregistrer précise le résultat métier devenu consultable, au-delà de la seule action de saisie.',
 'Fait ou décision pris en compte avec son contexte et ses effets.',
 'Dire ce qui devient connu, puis distinguer les décisions ou réalisations qui peuvent suivre.',
 [cmp('receipt','Quantité et date reçues deviennent des faits consultables.','Annonce, arrivée et réception enregistrée ont des effets différents.',concept='Record product receipt',scope='Réception rapprochée d’une commande.',approach='Conserver quantité, date et référence de réception.'),cmp('service','La prestation réalisée est enregistrée avant approbation.','La sauvegarde du constat ne vaut pas acceptation du service.',concept='Service entry',scope='Prestation déclarée réalisée.',approach='Conserver le constat lié à l’achat.')],
 ['Microsoft distingue plusieurs moments de constat d’une réception ; SAP sépare l’enregistrement du service et son approbation. Dans les deux cas, rendre un fait connu ne remplace pas toutes les étapes qui l’entourent.', 'FLOW emploie Enregistrer pour décrire cette prise en compte durable. Le texte doit préciser si l’on connaît une annonce, une réalisation ou une décision.'],
 ex('service','Connu avant acceptation','Le prestataire déclare la réparation terminée et le constat est enregistré.','La réalisation déclarée est consultable ; l’acceptation peut encore être en attente.','L’enregistrement ne doit pas masquer ce qui reste à décider.'))

card('VER014',
 'Préciser quel fait, résultat ou engagement est établi. Confirmer doit toujours indiquer sa portée : accuser réception et accepter une date n’ont pas le même effet.',
 'Résultat ou engagement attesté, avec effet explicite.',
 'Nommer ce qui est confirmé, par qui et ce que la confirmation change.',
 [cmp('vendor','Une réponse fournisseur et la confirmation de la commande sont distinguées.','Le mécanisme d’acceptation automatique est conditionnel.'),cmp('approve','Confirmed enregistre un achat comme engagé après accord fournisseur.','Une confirmation pro forma ne produit pas le même journal ; le nom de l’action ne suffit pas.',concept='Purchase order confirmation',scope='Achat approuvé puis confirmé.',approach='Enregistrer l’engagement selon l’accord reçu.')],
 ['Microsoft distingue la réponse du fournisseur, son traitement et l’action de confirmation. Les deux pages ne décrivent donc pas un effet unique du mot Confirm.', 'FLOW utilise cette ambiguïté pour exiger un complément précis. La convention ne transforme ni un accusé de réception ni une saisie en promesse de satisfaction.'],
 ex('vendor','Message reçu, date non acceptée','Un fournisseur accuse réception de la commande mais n’a pas accepté la date demandée.','L’échange est connu ; la date reste à confirmer au sens d’engagement.','Le verbe doit préciser l’effet, pas seulement l’existence d’une réponse.'))

card('VER017',
 'Réexaminer ce qui existe et le modifier si nécessaire. Réviser porte une évolution métier justifiée, avec un avant, un après et une prise d’effet.',
 'Règle, décision ou engagement existant réexaminé.',
 'Identifier le changement retenu et ses conséquences sans confondre projet de modification et version applicable.',
 [cmp('changes','Le changement de date ou quantité est évalué par rapport à l’existant.','La revue peut conduire à ne pas accepter la proposition.'),cmp('approve','Une demande de changement précède une nouvelle approbation selon le parcours.','La séquence Microsoft est propre à l’achat ; elle n’est pas obligatoire pour toute révision.',concept='Request change',scope='Modification d’un achat déjà approuvé.',approach='Réouvrir la préparation selon les règles d’approbation.')],
 ['La revue Microsoft aide à comprendre le changement ; le parcours d’approbation gouverne sa prise d’effet. Examiner et appliquer la révision sont donc distinguables.', 'FLOW retient ce sens de changement métier raisonné. Republier le même contenu ou recalculer sans modification retenue ne démontre pas à soi seul une révision.'],
 ex('changes','Revoir une date annoncée','Un délai fournisseur augmente ; la date confirmée est réexaminée avec les demandes concernées.','Une nouvelle date peut être retenue après décision, ou la proposition refusée.','La révision se comprend par son effet sur l’engagement existant.'))

card('VER021',
 'Retirer un effet encore applicable selon les règles de l’objet concerné. Annuler conserve l’histoire et ne signifie pas défaire physiquement ce qui a déjà eu lieu.',
 'Partie de demande, décision ou effet identifié pouvant être retirée.',
 'Préciser l’effet annulé et les autres traitements encore nécessaires.',
 [cmp('cancel','Le reliquat d’une vente peut être annulé sans effacer l’expédié.','Annuler une vente close peut exiger un retour distinct.'),cmp('receipt','L’annulation d’un reçu peut produire une écriture de contrepassation.','Corriger le constat n’est pas transporter les marchandises dans l’autre sens.',concept='Cancel product receipt',scope='Effet d’une réception enregistrée corrigé.',approach='Conserver la correction et sa référence.')],
 ['Oracle retire la partie encore annulable de la demande ; Microsoft corrige l’effet d’une réception enregistrée. Le même verbe vise donc des objets et conséquences différents.', 'FLOW exige de nommer cet effet. L’annulation n’efface pas l’historique et ne propage pas automatiquement son résultat à toutes les commandes liées.'],
 ex('cancel','Annuler le reste','Dix pièces étaient demandées ; sept ont été servies et les trois restantes ne sont plus voulues.','L’annulation porte sur les trois encore attendues.','Les sept réalisées restent connues ; leur éventuel retour relève d’un autre traitement.'))

card('VER025',
 'Dire l’effet recherché avant d’employer Valider. Selon le cas, il faut vérifier, autoriser, accepter ou confirmer ; ces actions ne sont pas interchangeables.',
 'Terme courant à expliciter avant son usage canonique.',
 'Choisir le verbe qui décrit la décision ou le contrôle réellement effectué.',
 [cmp('approved','Approved peut protéger une proposition de planification.','Cela n’en fait pas encore une commande ferme ; traduire par « validée » masque cet effet.'),cmp('service','L’approbation d’un service produit des effets distincts de son enregistrement.','L’effet dépend du parcours de service ; il diffère de l’approbation d’un ordre planifié.',concept='Service entry approval',scope='Constat de prestation soumis à acceptation.',approach='Autoriser les effets liés à l’approbation du service.')],
 ['Microsoft Approved préserve une proposition ; SAP approuve un constat de service avec des effets de gestion. Même un nom proche d’approbation ne garantit donc pas la même décision.', 'FLOW conserve Valider comme mot à préciser. Les sources éclairent le risque d’ambiguïté ; elles ne fondent pas une nouvelle définition universelle ni l’adoption d’un verbe unique.'],
 ex('approved','Une proposition approuvée reste planifiée','Un ordre planifié reçoit le statut Approved mais n’a pas été affermi.','Il peut être conservé par le plan sans être encore un achat ferme.','Dire seulement « ordre validé » empêcherait de comprendre ce qui a changé.'))

ADDITIONAL_NOTES={
 'BHV061':'UBL réexaminé : ses échanges de commande ne distinguent pas l’implantation consignée. Microsoft et Oracle étayent le régime ; l’intention initiale demeure propre à FLOW.',
 'BHV062':'UBL réexaminé : le cadre documentaire d’échange est moins direct que les deux pages de consignation pour le réassort continu sans achat immédiat.',
 'BHV066':'La page Commerce Customer orders reste documentée dans D04.i ; le comportement est recentré sur le service depuis le magasin et le parcours SAP de vente sur stock.',
 'BHV070':'Ancienne page SAP STO vide à la consultation. UBL traite des échanges sans isoler l’intention initiale ; remplacement par First Allocation et le suivi Transfer Order, dont les limites sont explicites.',
 'BHV071':'Page IOM Transfer orders réexaminée mais recentrée sur D04.k : elle porte le suivi commun. Les deux références retenues distinguent ici génération d’un réassort et optimisation continue.',
 'BHV072':'Page IOM Transfer orders réexaminée mais recentrée sur D04.k : elle porte le suivi commun plutôt que le motif de rééquilibrage.',
 'BHV086':'Oracle EBS Line Sets réexaminé, convergent avec Shipment Sets 26A retenu. L’ancienne page SAP ERP_SPV renvoie un texte vide ; la release Microsoft complète le groupe par son traitement collectif.',
}

# Journal des URL historiques non retenues dans les comparaisons courtes.
# Les ouvertures sans texte ne sont pas déclarées comme des lectures de contenu.
OTHER_REVIEWS={
 'https://docs.oracle.com/cd/E26401_01/doc.122/e48843/T335476T336783.htm':(
  'Page primaire ouverte ; Line (Ship or Arrival) Sets, lignes 51–255 lues.',
  'Ensembles conservant les lignes, attributs communs et contrôles de complétude ; rapprochement fidèle du grouping.',
  'Regroupé avec Shipment Sets 26A pour éviter deux variantes Oracle détaillant le même mécanisme.'),
 'https://docs.oracle.com/cd/E26401_01/doc.122/e48843/T335476T430137.htm':(
  'Page primaire ouverte ; Purge Set, Order, and Quote Purge Selection, lignes 1105–1178 lues.',
  'Sélection de commandes closes/annulées, purge et consultation limitée via Purge Set ; préconditions explicites.',
  'Ne pas présenter la purge comme équivalent complet de la conservation historique consultable FLOW.'),
 'https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/fauom/split-fulfillment-lines.html':(
  'Page primaire ouverte et lue ; exemple et procédure Split Order Lines.',
  'La demande de 50 conserve son total après répartition 30/20.',
  'Regroupée avec Fulfillment Line Splits 26B, plus générale sur les variantes et limites.'),
 SCM+'master-planning/action-messages':(
  'Page primaire ouverte et lue ; messages Advance/Postpone et exemple de matière arrivant trop tard.',
  'Le plan propose des changements à appliquer en tenant compte des dépendances.',
  'Proposition de recalcul moins directe que la préparation, la revue et l’acceptation de contenu pour Lifecycle.'),
 MS+'intelligent-order-management/ifo-arch':(
  'Page primaire ouverte et lue ; introduction, sources et business constraints.',
  'IFO recherche sources et quantités selon contraintes et objectifs.',
  'Périmètre d’optimisation spécialisé, trop étroit pour définir à lui seul Fulfillment.'),
 'https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4':(
  'Page primaire ouverte et lue ; Supply Assignment Basics et Scenarios, lignes 178–223.',
  'ARun associe ressource et demande puis un contrôle de release décide de permettre la livraison.',
  'Source pertinente mais centrée sur affectation ARun ; la fiche Release retient lancement dépôt et contrainte collective sans importer le couplage produit.'),
}

def finish():
    required={'vendor','product','element_name','element_type','relationship','similarities','differences','flow_position','source_title','source_url','source_version','source_locator','consulted_on','status','source_refs','evidence_limits','concept_name','scope_summary','approach_summary'}
    for kind in ('nodes','terms'):
        by={e['id']:e for e in OUT[kind]}
        expected=[e['id'] for e in INPUT[kind]]
        assert len(by)==len(OUT[kind]) and set(by)==set(expected),(kind,set(expected)-set(by))
        OUT[kind]=[by[id] for id in expected]
    rows=OUT['nodes']+OUT['terms']
    for row in rows:
        if row['id'] in ADDITIONAL_NOTES:
            row['editorial_notes']=ADDITIONAL_NOTES[row['id']]
        assert len({c['source_url'].split('#')[0] for c in row['market_comparisons']})>=2,row['id']
        for c in row['market_comparisons']:
            assert required==set(c),(row['id'],required-set(c),set(c)-required)
            assert all(c[k] and (not isinstance(c[k],str) or c[k].strip()) for k in required),row['id']
            assert c['source_url'].startswith(('https://','http://')) and 'U477' in c['source_refs']
        ins=row['market_inspiration']
        assert set(ins)=={'choice','flow_scope','flow_approach','synthesis','examples'}
        assert isinstance(ins['synthesis'],list) and 2<=len(ins['synthesis'])<=3
        assert all(isinstance(p,str) and p.strip() for p in ins['synthesis'])
        assert len(ins['examples'])>=1
        for e in ins['examples']:
            assert set(e)=={'title','situation','outcome','lesson','source_title','source_url','source_refs'}
            assert all(e.values()) and e['source_url'] in {c['source_url'] for c in row['market_comparisons']}
        previous=OLD[row['id']].get('market_comparisons',[])
        for c in row['market_comparisons']:
            oldrefs={ref for prior in previous if prior['source_url']==c['source_url'] for ref in prior.get('source_refs',[])}
            assert oldrefs<=set(c['source_refs']),(row['id'],'lost provenance')
        if any(c['source_url'] not in {n['source_url'] for n in row['market_comparisons']} for c in previous):
            assert row.get('editorial_notes'),(row['id'],'missing replacement rationale')
    records=[]
    old_by_url={}
    for id,f in OLD.items():
        for c in f.get('market_comparisons',[]):
            old_by_url.setdefault(c['source_url'],[]).append(dict(id=id,source_refs=c.get('source_refs',[]),status=c.get('status'),previous_source_title=c['source_title'],previous_source_version=c.get('source_version'),previous_source_locator=c.get('source_locator')))
    for key,s in S.items():
        if key not in USED:
            continue
        records.append(dict(local_key=key,**s,supported_ids=list(dict.fromkeys(USED[key])),previous_correspondences=old_by_url.get(s['source_url'],[]),examples=EXAMPLES.get(key,[]),consultation_method='Texte primaire indexé consulté après erreur à l’ouverture' if key=='ascm' else 'Page primaire ouverte ; passages identifiés lus',presentation_status='retained'))
    current_urls={r['source_url'] for r in records}
    legacy=[]
    for url,previous in old_by_url.items():
        retained_ids=[r['id'] for r in rows if any(c['source_url']==url for c in r['market_comparisons'])]
        if url in current_urls:
            review=dict(consultation_method=next(r['consultation_method'] for r in records if r['source_url']==url),finding=next(r['finding'] for r in records if r['source_url']==url),disposition='Réexaminée et conservée dans les fiches ciblées ; les retraits locaux sont justifiés dans editorial_notes.')
        elif 'help.sap.com/' in url:
            review=dict(consultation_method='Ouverture de la page primaire : aucun texte restitué (0 ligne).',finding='Contenu non vérifiable dans cette consultation ; aucune affirmation nouvelle fondée sur cette page.',disposition='Remplacée par les documents primaires lisibles pertinents cités dans les fiches ; preuves et références précédentes conservées dans before/.')
            if '4ac8acf820ad41a8a5841420085ba68d' in url:
                review.update(consultation_method='Ouverture sans texte ; extrait primaire indexé Manage Service Entry Sheets lu.',finding='L’extrait confirme la relation aux achats de services ; le cours SAP complet donne la distinction constat/approbation et un exemple.',disposition='Remplacée par Processing a Service Entry Sheet, texte primaire complet et cas explicite.')
        else:
            assert url in OTHER_REVIEWS,('historical URL not reviewed',url)
            method,finding,disposition=OTHER_REVIEWS[url]
            review=dict(consultation_method=method,finding=finding,disposition=disposition)
        legacy.append(dict(source_url=url,consulted_on='2026-09-19',previous_correspondences=previous,retained_ids=retained_ids,**review))
    log=dict(source='U477',batch='orders',sources=records,historical_source_reviews=legacy,limits='53 documents primaires initiaux complétés par ASCM et Logility ; lectures ciblées, sans vidéo Logility ni consultation fictive des pages SAP vides. Les illustrations FLOW sont explicitement distinguées des cas présents dans les documents. Aucune adoption, réalisation installée ou équivalence universelle ajoutée.')
    # Contrats JSON Schema limités au delta ; pas de validation du modèle global.
    import json
    from jsonschema import Draft202012Validator
    schema=json.loads((ROOT.parents[1]/'modeles/schemas/urbanism.schema.json').read_text(encoding='utf-8'))
    for name in ('marketComparisons','marketInspiration'):
        assert name in schema['$defs'],name
    comp_validator=Draft202012Validator({'$ref':'#/$defs/marketComparisons','$defs':schema['$defs']})
    ins_validator=Draft202012Validator({'$ref':'#/$defs/marketInspiration','$defs':schema['$defs']})
    for row in rows:
        comp_validator.validate(row['market_comparisons'])
        ins_validator.validate(row['market_inspiration'])
    write_text_if_changed(ROOT/'orders-output.yaml',dumps(OUT))
    write_text_if_changed(ROOT/'orders-sources.yaml',dumps(log))
    reread=read(ROOT/'orders-output.yaml')
    assert reread==OUT
    print(f"ORDERS OK: {len(OUT['nodes'])} nodes, {len(OUT['terms'])} terms, {sum(len(r['market_comparisons']) for r in rows)} comparisons, {len(records)} retained primary documents, {len(legacy)} historical URLs reviewed; IDs, provenance, examples, >=2 URLs, JSON Schema and YAML roundtrip pass")

if __name__=='__main__':
    finish()

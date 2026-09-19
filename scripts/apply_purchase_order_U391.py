"""Apply the scoped Purchase Order approval and preserve the consignment correction."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

OUT = ROOT / 'audits/2026-09-18-purchase-order-U391'


def main():
    assert not OUT.exists()
    mp = ROOT / 'modeles/backlog/model.yaml'
    before = read(mp)
    m = deepcopy(before)
    rp = 'modeles/backlog/purchase-order-behaviors.yaml'
    review = read(ROOT / rp)
    assert review['status'] == 'proposed'
    ids = ['BHV058', 'BHV059', 'BHV060']
    assert not set(ids) & {n['id'] for n in m['nodes']}
    append('connaissance/01-contributions-utilisateur.md', '''## U391

**id**

U391

**date**

2026-09-18

**titre**

Valider Purchase Order et replacer la consignation dans la gestion du stock

**texte**

Le "Consignment Procurement" ne touche pas l'acte d'achat en lui même mais joue sur la possession de stock qui des impacts sur la compta (valorisation de stock), la facturation, la responsabilité assurantielle et également la politique de traitement du stock après la saison (envoi chez un soldeur seconde main ou renvoi au fournisseur ou destruction etc.). C'est une capacité de gestion du stock, une offre qu'on propose au fournisseur. Je ne sais pas comment le marché gère ça dans les carto de capacité.

Pour les Purchase Orders, je valide.

**contexte et portée**

Accord sur Stock Procurement, Direct Delivery et Service Procurement, leurs responsabilités présentées et leur rattachement à Purchase Order ; principe d’élargissement aux prestations et frontière achat/Service Order acquis. Rédactions développées et contrats détaillés gardent leur statut éditorial. Le candidat Consignment Procurement ne doit pas être intégré comme quatrième comportement d’achat. Laurent situe la responsabilité dans la gestion du stock et décrit une offre au fournisseur, avec impacts comptables, de facturation, assurantiels et devenir après saison. Recherche de positionnement marché demandée ; aucun nouveau nom ou découpage détaillé de capacité n’est encore validé. Aucune publication demandée.''')
    append('connaissance/04-corrections.md', '''## C102

**id**

C102

**sources**

U391

**constat**

U390 conservait Consignment Procurement comme candidat supplémentaire sous Purchase Order, principalement vu par l’acquisition du stock déjà détenu.

**correction**

Cette entrée est trop étroite pour le besoin décrit par Laurent. Retirer le candidat du découpage achat et instruire une responsabilité de gestion du stock sous accord fournisseur : détention, propriété, droits et obligations, faits transmis à la finance et devenir du stock, notamment après saison. Les sources Microsoft et Oracle documentent un possible achat/transfert de propriété dans le cycle ; ce lien demeure sans faire de tout le cycle un comportement d’achat. Comptabilité, facturation et assurance ne sont pas automatiquement absorbées par FLOW. Le nom et la maille de la capacité restent proposés.''')
    OUT.mkdir()
    for stem in ['model', 'purchase-order-behaviors', 'behavior-gap-audit']:
        (OUT / (stem + '-before.yaml')).write_bytes((ROOT / f'modeles/backlog/{stem}.yaml').read_bytes())
    refs = ['U390', 'U391', 'ELM235', 'CMP146']
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    def life(values, adopted=()):
        return dict(state='urbanist_validated' if adopted else 'under_instruction', recorded_at=stamp,
            recorded_by='Codex', source_refs=['U391'], validated_fields=list(adopted),
            value_sha256={f:value_hash(values[f]) for f in adopted},
            note='Noms, responsabilités présentées et rattachements adoptés U391 ; descriptions développées et comparaisons qualifiées séparément.')

    sources = {s['id']:s for s in review['sources']}

    def comparison(source_id, position):
        s = sources[source_id]
        return dict(vendor=s['vendor'], product=s['product'], element_name=s['title'],
            element_type='Processus, document ou fonction produit', relationship='Recouvrement partiel',
            similarities=s['finding'], differences=s['limit'], source_title=s['title'], source_url=s['url'],
            source_version=s['edition'], source_locator=s['locator'], consulted_on=s['consulted_on'],
            evidence_limits=s['access'] + ' ; aucune preuve de réalisation Beaumanoir.', flow_position=position,
            status='proposed', source_refs=refs)

    parent = next(n for n in m['nodes'] if n['id']=='D04.j')
    assert 'definition' not in parent['lifecycle']['validated_fields']
    parent['fields']['definition'] = review['proposed_definition']
    parent['fields']['finality'] = 'Disposer d’attentes d’achat explicables, en biens ou prestations, et connaître ce qui reste à satisfaire selon les accords applicables.'
    parent['fields']['decomposition_rationale'] = review['decomposition_rationale']
    parent['fields']['scope'] = (
        'Purchase Order porte les commandes d’achat de biens ou de prestations, en référence aux conditions applicables. '
        'Le libellé désigne une capacité d’action ; [Purchase Order](glossary:TER070) reste également un objet métier distinct.\n\n'
        'Trois parcours sont adoptés U391 : Stock Procurement pour les apports au stock du réseau, Direct Delivery pour une livraison fournisseur directement au client, '
        'Service Procurement pour une prestation attendue puis reconnue réalisée. Une commande peut combiner plusieurs lignes ou attendus ; aucun parcours exclusif au niveau du document imposé.\n\n'
        'Maintenir produits ou prestations, quantités ou unités applicables, destinations, échéances, conditions référencées et évolutions autorisées. '
        'Rapprocher les réalisations et conserver les écarts pour expliquer ce qui reste à satisfaire, sans prendre une date annoncée pour un résultat acquis. '
        'Une livraison fournisseur directement à un magasin du réseau relève de Stock Procurement lorsqu’elle alimente son stock ; Direct Delivery vise ici le client de la commande de vente.\n\n'
        'Exemples fictifs : 60 pièces reçues sur 100 laissent 40 à recevoir ; une prestation reconnue réalisée pour 30 pièces sur 50 laisse 20 à traiter. '
        'Un report proposé par le fournisseur ne modifie pas automatiquement la promesse client.\n\n'
        '[Order Lifecycle Management](model:D04.o) conserve brouillon, affermissement, gel, lancement, attente, report, annulation, clôture et split. '
        '[Order Structuring](model:D04.n) conserve la composition persistante et [Order Archiving](model:D04.q) la conservation. '
        'Aucune recopie de ces responsabilités sous les trois parcours.\n\n'
        '[Fulfillment Optimization](model:D03) et [Inventory Optimization](model:D05) déterminent les réponses et besoins selon leur finalité. '
        '[Service Order Management](model:D07.b) et [Execution Orchestration](model:D06.d) conservent sollicitation et pilotage des prestations ; '
        'un appel de service ne nécessite pas systématiquement une commande d’achat. [Inventory Management](model:D01) enregistre les états et mouvements. '
        'La finance traite facturation et règlement ; la négociation contractuelle et l’exécution physique fournisseur ne sont pas absorbées.\n\n'
        'U391 : la consignation est instruite comme responsabilité de gestion du stock, pas comme quatrième comportement de Purchase Order. '
        'Un transfert de propriété peut mobiliser l’achat selon l’accord sans déplacer toute la consignation dans cette capacité. '
        'La reprise fournisseur et le remplacement demeurent liés à [Supplier Return](model:D04.m), sans comportement par origine du besoin.')
    parent['fields']['market_comparisons'] = [comparison(s, 'Trois parcours FLOW adoptés U391 ; nature produit et maille de capacité restent distinctes. Frontières achat/exécution/stocks préservées.') for s in ['PO-S1','PO-S2','PO-S3']]
    parent['revision'] += 1
    parent['source_refs'] = list(dict.fromkeys(parent['source_refs'] + refs))
    parent['review'] = dict(state='partial', note='Trois parcours et extension aux prestations adoptés U391 ; définition du parent et précisions éditoriales non présentées intégralement.')
    # Exact responsibilities shown in the response approved by Laurent.
    definitions = [
        'Acheter des marchandises destinées au stock du réseau ; suivre les quantités et dates restant à recevoir.',
        'Acheter des marchandises livrées directement par le fournisseur au client ; coordonner les attentes des commandes d’achat et de vente.',
        'Acheter une prestation ; suivre ce qui est attendu puis reconnu réalisé.',
    ]
    adoptions=[]
    for ident, p, definition in zip(ids, review['proposals'], definitions):
        fields=dict(name=p['name'], definition=definition, finality=p['benefit'],
            scope=p['mechanism']+'\n\n'+p['example']+'\n\n'+p['boundary']+'\n\n'
                'Les mutations communes mobilisent [Order Lifecycle Management](model:D04.o), la composition [Order Structuring](model:D04.n) et la conservation [Order Archiving](model:D04.q). '
                'Aucune négociation de contrat, réalisation physique ni fonction comptable reprise par ce comportement. Les exemples ne prouvent aucune pratique installée.',
            market_comparisons=[comparison(s,p['boundary']+' Correspondance proposée, distincte de l’accord sur le comportement FLOW.') for s in p['source_ids']])
        node=dict(id=ident,revision=1,kind='behavior',layer=parent['layer'],fields=fields,source_refs=refs,
            source_locator=dict(path='connaissance/01-contributions-utilisateur.md',anchor='u391'),adoption_ids=[],
            review=dict(state='partial',note='Nom, responsabilité présentée et parent adoptés ; compléments et correspondances proposés.'),lifecycle=life(fields,['name','definition']))
        m['nodes'].append(node)
        rel=dict(id='REL-BEHAVIOR-'+ident,revision=1,type='contains',source_id='D04.j',target_id=ident,source_refs=refs,review=dict(state='accepted',note='Rattachement adopté U391.'))
        rel['lifecycle']=life(rel,['type','source_id','target_id']);m['relations'].append(rel)
        p.update(status='integrated_U391',node_id=ident)
        adoptions.append(dict(node_id=ident,parent_id='D04.j',adopted_fields=['name','definition'],value_sha256=node['lifecycle']['value_sha256']))
    for ident, source, target, meaning, condition, effect in [
        ('DIRECT-SALES','BHV059','D04.i','A besoin des attentes de la commande de vente et du lien avec les quantités achetées pour le client.','Lorsque le fournisseur livre directement le client.','Expliquer les écarts achat/vente sans modifier automatiquement la promesse.'),
        ('SERVICE-ORDER','BHV060','D07.b','A besoin des sollicitations et résultats des services pour rapprocher l’attendu d’achat et le réalisé.','Lorsqu’une prestation achetée est exécutée via la plateforme de services.','Distinguer engagement d’achat et pilotage opérationnel ; aucun achat imposé pour tout appel de service.'),
        ('STOCK-FACTS','BHV058','D01.g','A besoin des faits de réception enregistrés pour déterminer le reste à recevoir.','Lorsqu’un achat alimente le stock du réseau.','Ne pas assimiler réception annoncée et stock réellement reçu.'),
    ]:
        m['relations'].append(dict(id='REL-NEEDS-U391-'+ident,revision=1,type='relates-to',source_id=source,target_id=target,source_refs=refs,
            qualification=dict(role='needs',meaning=meaning,conditions=[condition],effects=[effect]),review=dict(state='proposed',note='Formalisation du contrat éditoriale.'),lifecycle=life({})))
    save('modeles/backlog/model.yaml',m)
    migration=dict(source_refs=refs,model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),delta={},behaviors=[],adopted_behaviors=adoptions,capability_id='D04.j',scope='Trois parcours et élargissement aux prestations adoptés ; parent développé et contrats éditoriaux ; consignation exclue du découpage achat.')
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]};new={x['id']:x for x in m[key]}
        migration['delta'][key]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},changed={i:value_hash(new[i]) for i in sorted(new.keys()&old.keys()) if old[i]!=new[i]},removed=sorted(old.keys()-new.keys()))
    (OUT/'implementation.yaml').write_text(dumps(migration),encoding='utf-8')
    review.update(status='integrated_U391',catalog_changed=True,implementation_U391=migration)
    review['source_refs'].append('U391')
    review['additional_candidate'].update(status='withdrawn_from_purchase_order_U391',current_direction='Gestion du stock et offre au fournisseur ; voir consignment-inventory-review.yaml. Historique U390 conservé ; aucun quatrième comportement d’achat.',source_refs=['U391','C102'])
    review['market_comparisons'][0]['flow_position']='Trois parcours intégrés U391 ; correspondance marché reste proposée.'
    review['market_comparisons'][1].update(status='reframed_U391',flow_position='Retiré du découpage Purchase Order ; distinction acquisition/détention conservée, étude portée par consignment-inventory-review.yaml.')
    save(rp,review)
    dp='modeles/backlog/d04-refactoring.yaml';d=read(ROOT/dp);d['purchase_order_U391']=dict(status='integrated',source_refs=['U391'],capability_id='D04.j',behavior_ids=ids,review_path=rp);save(dp,d)
    ap='modeles/backlog/behavior-gap-audit.yaml';a=read(ROOT/ap)
    a['source_refs'].append('U391');a['implementation_U391']=migration;a['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest()
    assessment=next(x for x in a['assessments'] if x['capability_id']=='D04.j')
    assessment.update(existing_behaviors=ids,verdict='trois parcours intégrés U391',diagnosis=review['decomposition_rationale'],recommendation='Stock, livraison directe et prestations ; consignation instruite en gestion du stock, pas en quatrième comportement d’achat.')
    for ident in ids:
        a['existing_behavior_review'].append(dict(behavior_id=ident,status='integrated_U391',market_sources=[],recommendation='Nom, responsabilité et parent adoptés U391 ; Microsoft/SAP ELM235/CMP146 dans les fiches ; contrats proposés.'))
    save(ap,a)
    append('marche/comparaisons.md', '''### Intégration CMP146 — U391

Stock Procurement, Direct Delivery et Service Procurement intégrés sous Purchase Order (BHV058–060), avec responsabilités présentées et rattachements adoptés. Principe d’extension aux prestations acquis ; définition développée du parent éditoriale. Achat, sollicitation opérationnelle, stock et finance demeurent distincts. Consignment Procurement retiré des candidats achat : C102 et CMP147 instruisent la responsabilité de gestion du stock demandée. Comparaisons marché dans les fiches, sans validation automatique ni publication.''')
    agents=ROOT/'AGENTS.md';text=agents.read_text(encoding='utf-8')
    marker='- **Nommage marché (U294)**'
    text=text.replace(marker,'- **Purchase Order (U391)** : Stock Procurement, Direct Delivery et Service Procurement sont adoptés ; biens et prestations sont couverts. D04 porte l’achat, D06 la sollicitation et l’orchestration ; pas d’achat obligatoire pour chaque appel de service. Consignment Procurement est retiré du découpage achat : instruire la gestion du stock sous accord fournisseur, en séparant propriété, détention, droits/obligations, effets financiers et devenir du stock. Nom et découpage de cette capacité restent proposés dans `modeles/backlog/consignment-inventory-review.yaml`.\n'+marker,1)
    agents.write_text(text,encoding='utf-8')
    (OUT/'README.md').write_text('# Purchase Order — U391\n\nBHV058–060 intégrés : Stock Procurement, Direct Delivery, Service Procurement. Noms, responsabilités présentées et parents adoptés. Extension aux prestations acquise ; textes développés et contrats proposés. Consignation retirée des candidats achat et instruite séparément en gestion du stock. Backlog uniquement.\n',encoding='utf-8')
    print('U391: three Purchase Order behaviors integrated; consignment candidate removed from purchase decomposition.')


if __name__=='__main__':
    main()

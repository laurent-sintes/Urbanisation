"""Integrate the approved U400 batch in the existing behavior review."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read
from scripts.lifecycle import value_hash

OUT = ROOT / 'modeles/backlog/history/grouped-orders-U401'


def main():
    assert not OUT.exists()
    rp = 'modeles/backlog/consignment-sales-transfer-review.yaml'
    review = read(ROOT/rp)
    assert review['status'] == 'proposed_in_existing_audit'
    mp = ROOT/'modeles/backlog/model.yaml'; before = read(mp); model = deepcopy(before)
    new_ids = [f'BHV{i:03d}' for i in range(63,75)]
    assert not set(new_ids) & {n['id'] for n in model['nodes']}
    assert '## U401\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U401

**id**

U401

**date**

2026-09-18

**titre**

Adopter les douze comportements de consignation, vente et transfert

**texte**

Je valide !

**contexte et portée**

Accord sur le lot présenté après U400 : trois comportements sous Consigned Inventory Management (Consumption-Based Ownership Transfer, Aging-Based Ownership Transfer, Consignment Exit), quatre sous Sales Order (Ship to Customer, Customer Pickup, Direct Delivery, Intercompany Sales), cinq sous Transfer Order (Initial Stocking, Continuous Replenishment, Inventory Rebalancing, Stock Consolidation, Order-Driven Transfer). Noms, responsabilités présentées, rattachements et frontières exposées acquis. Les définitions validées reprennent les responsabilités effectivement présentées ; les descriptions développées, justifications éditoriales et comparaisons restent qualifiées séparément. Les comportements sont combinables selon le cas, notamment la dimension commerciale Intercompany ; Direct Delivery côté vente reste distinct du comportement côté achat. Décisions D03/D05, prise en charge D04, stock D01 et exécution D06 gardent leurs responsabilités. Aucune reprise générale des liens, nouveau chantier Atlas, nouvel audit ou release : U399 reste applicable.''')
    OUT.mkdir()
    for relative, name in [(mp,'model-before.yaml'), (ROOT/rp,'proposal-before.yaml'),
                           (ROOT/'modeles/backlog/behavior-gap-audit.yaml','behavior-gap-audit-before.yaml'),
                           (ROOT/'modeles/backlog/consignment-inventory-review.yaml','consignment-review-before.yaml')]:
        (OUT/name).write_bytes(relative.read_bytes())
    refs = ['U400','U401','ELM240','CMP151']
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    def life(values, approved):
        return dict(state='urbanist_validated',recorded_at=stamp,recorded_by='Codex',source_refs=['U401'],
            validated_fields=approved,value_sha256={k:value_hash(values[k]) for k in approved},
            note='U401 : noms, responsabilités présentées et parents adoptés ; descriptions développées et comparaisons éditoriales.')
    sources = {s['id']:s for s in review['sources']}
    def market(sid, position):
        s = sources[sid]
        return dict(vendor=s['vendor'],product=s['product'],element_name=s['title'],
            element_type='Processus, mécanisme ou document produit ; étude client lorsque précisé',relationship='Recouvrement partiel',
            similarities=s['finding'],differences=s['limit'],flow_position=position,
            source_title=s['title'],source_url=s['url'],source_version=s['edition'],source_locator=s['locator'],
            consulted_on=s['consulted_on'],evidence_limits=s['access']+' ; aucune preuve de déploiement Beaumanoir.',
            status='proposed',source_refs=refs)
    # Definitions are the responsibilities actually shown to Laurent, not unseen expansions from the proposal file.
    definitions = [
        'Appliquer le transfert de propriété lors de la vente ou consommation prévue par l’accord.',
        'Appliquer l’acquisition à l’échéance d’une durée contractuelle.',
        'Prendre en charge une sortie autorisée de la consignation ou de la détention : reprise fournisseur, orientation vers un soldeur, seconde main ou destruction selon l’accord et la décision retenue.',
        'Prendre en charge la commande à livrer au client depuis le réseau : entrepôt, magasin ou autre lieu admissible.',
        'Prendre en charge la mise à disposition et le retrait au lieu convenu. Une commande prête reste distincte d’une commande effectivement retirée.',
        'Prendre en charge la commande dont le fournisseur livre directement le client, en coordonnant les attendus de vente et d’achat.',
        'Prendre en charge une vente entre entités juridiques du groupe, avec cohérence entre engagements de vente et d’achat.',
        'Porter les transferts constituant le stock de départ : implantation d’une saison, d’une capsule ou d’un nouveau lieu.',
        'Porter les transferts alimentant régulièrement un lieu pendant l’activité.',
        'Porter les transferts corrigeant un déséquilibre entre lieux, par exemple d’un magasin disposant d’un excédent vers un magasin qui manque de stock.',
        'Porter les transferts regroupant des stocks dispersés : reconstitution de tailles, concentration ou rapatriement de reliquats.',
        'Porter un transfert nécessaire à une commande identifiée, en conservant son lien et son échéance.',
    ]
    adoptions = []; cursor = 0
    for group in review['groups']:
        parent = next(n for n in model['nodes'] if n['id']==group['capability_id'])
        for field in ['scope','decomposition_rationale','market_comparisons']:
            assert field not in parent['lifecycle']['validated_fields']
        behavior_ids = new_ids[cursor:cursor+len(group['candidates'])]
        parent['fields']['decomposition_rationale'] = group['decomposition_rationale']
        links = ', '.join(f"[{c['name']}](model:{ident})" for c,ident in zip(group['candidates'],behavior_ids))
        parent['fields']['scope'] += '\n\nU401 : comportements adoptés — '+links+'. '+review['combination']+'\n\n'+review['common_boundaries']
        parent['fields']['market_comparisons'] = [market(sid,group['market_position']) for sid in dict.fromkeys(s for c in group['candidates'] for s in c['source_ids'])]
        parent['revision'] += 1; parent['source_refs'] = list(dict.fromkeys(parent['source_refs']+refs))
        parent['review']['note'] += ' U401 : comportements adoptés ; justification et descriptions développées éditoriales.'
        for candidate,ident in zip(group['candidates'],behavior_ids):
            definition = definitions[cursor]; cursor += 1
            scope = (candidate['boundary']+'\n\nExemple fictif : '+candidate['example']+'\n\n'
                +review['common_boundaries']+'\n\n'+review['combination']+'\n\n'
                'Les modalités de paiement, autorisations, tolérances et échéances contractuelles restent des règles à préciser selon le contexte. '
                'Cet exemple n’établit aucune pratique installée chez Beaumanoir.')
            if candidate['name']=='Consignment Exit':
                scope += ' Le comportement porte les filières de sortie autorisées ; les déclencheurs d’acquisition par consommation ou durée sont décrits par les deux comportements frères. Aucune sortie sans autorisation ni transfert de propriété implicite.'
            if ident=='BHV068':
                scope += ' [Direct Delivery côté achat](model:BHV059) porte l’engagement fournisseur ; ce comportement porte l’attendu client. Les deux perspectives peuvent intervenir sur la même livraison.'
            fields = dict(name=candidate['name'],definition=definition,finality=candidate['benefit'],scope=scope,
                market_comparisons=[market(sid,'U401 adopte ce comportement sous '+group['name']+'. '+group['market_position']) for sid in candidate['source_ids']])
            node = dict(id=ident,revision=1,kind='behavior',layer=parent['layer'],fields=fields,source_refs=refs,
                source_locator=dict(path='connaissance/01-contributions-utilisateur.md',anchor='u401'),adoption_ids=[],
                review=dict(state='partial',note='Nom, définition présentée et parent adoptés U401 ; finalité, scope et correspondances éditoriaux.'),
                lifecycle=life(fields,['name','definition']))
            model['nodes'].append(node)
            rel = dict(id='REL-BEHAVIOR-'+ident,revision=1,type='contains',source_id=parent['id'],target_id=ident,source_refs=refs,
                review=dict(state='accepted',note='Rattachement adopté dans le lot U401.'))
            rel['lifecycle'] = life(rel,['type','source_id','target_id']); model['relations'].append(rel)
            adoptions.append(dict(node_id=ident,parent_id=parent['id'],adopted_fields=['name','definition'],value_sha256=node['lifecycle']['value_sha256']))
            candidate.update(status='integrated_U401',node_id=ident,adopted_definition=definition)
        group['behavior_ids'] = behavior_ids
    assert cursor==12
    # Verify that this integration never alters an earlier approved field or a pre-existing relation.
    nodes = {n['id']:n for n in model['nodes']}
    for old in before['nodes']:
        for field in old['lifecycle']['validated_fields']:
            assert nodes[old['id']]['fields'][field]==old['fields'][field]
    assert model['relations'][:len(before['relations'])]==before['relations']
    save('modeles/backlog/model.yaml',model)
    migration = dict(source_refs=refs,model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),
        model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),delta={},adopted_behaviors=adoptions,behaviors=[])
    for key in ['nodes','relations']:
        old = {x['id']:x for x in before[key]}; new = {x['id']:x for x in model[key]}
        migration['delta'][key] = dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
            changed={i:value_hash(new[i]) for i in sorted(old.keys() & new.keys()) if old[i]!=new[i]},removed=sorted(old.keys()-new.keys()))
    save((OUT/'implementation.yaml').relative_to(ROOT),migration)
    review.update(status='integrated_U401',catalog_changed=True,implementation_ref='modeles/backlog/history/grouped-orders-U401/implementation.yaml')
    review['source_refs'].append('U401'); save(rp,review)
    ap='modeles/backlog/behavior-gap-audit.yaml'; audit=read(ROOT/ap)
    audit['source_refs'].append('U401'); audit['implementation_U401']=migration
    audit['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest()
    for group in review['groups']:
        assessment=next(a for a in audit['assessments'] if a['capability_id']==group['capability_id'])
        assessment.update(existing_behaviors=group['behavior_ids'],verdict='lot intégré U401',diagnosis=group['decomposition_rationale'],
            recommendation='Noms, responsabilités présentées et parents adoptés ; décisions, régime de stock et exécution distincts. Compléments éditoriaux et comparaison : consignment-sales-transfer-review.yaml.')
        for ident in group['behavior_ids']:
            audit['existing_behavior_review'].append(dict(behavior_id=ident,status='integrated_U401',market_sources=[],
                recommendation='Comportement du lot U401 intégré avec portée de validation ; sources ELM240/CMP151 dans la fiche et l’annexe groupée.'))
    save(ap,audit)
    p='modeles/backlog/consignment-inventory-review.yaml'; ci=read(ROOT/p)
    ci['source_refs'].append('U401')
    ci['candidate']['decomposition_status']='Trois comportements intégrés U401, BHV063–065 : transfert à consommation, transfert à échéance et sortie autorisée. Portées dans consignment-sales-transfer-review.yaml.'
    ci['current_U401']=dict(status='behaviors_integrated',behavior_ids=new_ids[:3],review_path=rp)
    save(p,ci)
    p='modeles/backlog/d04-refactoring.yaml'; d04=read(ROOT/p)
    d04['sales_transfer_U401']=dict(status='behaviors_integrated',source_refs=['U401'],sales_behavior_ids=new_ids[3:7],transfer_behavior_ids=new_ids[7:],review_path=rp)
    save(p,d04)
    agents=ROOT/'AGENTS.md'; text=agents.read_text(encoding='utf-8')
    marker='- **Nommage marché (U294)**'
    assert marker in text
    text=text.replace(marker,'- **Lot consignation, vente et transfert (U401)** : douze comportements intégrés sous D01.h, D04.i et D04.k ; définitions et portées dans `modeles/backlog/consignment-sales-transfer-review.yaml`. Intercompany Sales peut se combiner avec un mode de livraison ; Direct Delivery côté vente porte l’attendu client, côté achat l’engagement fournisseur. Décision, suivi de l’Order et exécution restent distincts. Lot de l’audit existant ; aucune reprise des liens au titre des règles U398/U399.\n'+marker,1)
    agents.write_text(text,encoding='utf-8')
    append('marche/comparaisons.md','''### Intégration CMP151 — U401

Douze comportements intégrés : BHV063–065 sous Consigned Inventory Management, BHV066–069 sous Sales Order, BHV070–074 sous Transfer Order. Noms, responsabilités présentées et parents validés ; comparaisons qualifiées séparément. Les sources spécifiques remplacent les anciennes correspondances génériques des trois parents, conservées dans la capture antérieure. Limites SAP indexé, IOM preview, Nextail témoignage et périmètre FLOW de Consignment Exit préservées. Pas de nouvelle recherche générale, nouvelle capacité ni modification des liens métier existants.''')
    append('JOURNAL.md','''## 2026-09-18 — U401 : lot consignation, vente et transfert intégré

Douze comportements validés ajoutés au backlog (BHV063–074) avec définitions présentées, parents, exemples, bénéfices et comparaison marché. Justifications de décomposition sur les trois capacités ; audit existant et annexes mis à jour. Aucun lien métier existant ni champ antérieurement validé modifié. Preuves techniques dans modeles/backlog/history/grouped-orders-U401 ; aucune nouvelle étude d’audit, release ou modification Atlas.''')
    (OUT/'README.md').write_text('# U401 — preuve d’intégration\n\nDouze comportements du lot U400, validé U401. Noms, définitions présentées et parents adoptés ; descriptions développées et comparaisons distinctes. Capture antérieure et empreintes dans implementation.yaml. Aucun audit supplémentaire ni changement des relations métier existantes.\n',encoding='utf-8')
    print('U401 integrated: 12 behaviors, 3 parents, existing relations and adopted fields preserved.')


if __name__=='__main__':
    main()

"""Add the explicitly requested Supplier Return repair path."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

OUT = ROOT / 'audits/2026-09-18-supplier-repair-U388'


def main():
    assert not OUT.exists()
    mp=ROOT/'modeles/backlog/model.yaml'; before=read(mp); m=deepcopy(before)
    rp='modeles/backlog/supplier-return-behaviors.yaml'; review=read(ROOT/rp)
    assert review['status']=='integrated_U387'
    assert 'BHV057' not in {n['id'] for n in m['nodes']}
    assert '## U388\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U388

**id**

U388

**date**

2026-09-18

**titre**

Ajouter Return for Repair sous Supplier Return

**texte**

Ajoute Return for Repair stp

**contexte et portée**

Demande explicite d’ajouter le candidat discuté U386 sous Supplier Return, après les deux parcours adoptés U387. Nom, principe de renvoi pour réparation avec restitution attendue du même bien et rattachement acquis. La réserve de création conditionnelle est levée ; responsabilités d’achat de prestation, exécution physique et enregistrement de stock restent distinctes. La rédaction détaillée, les exemples et les nouveaux contrats ne sont pas validés globalement. Aucune restriction aux seules garanties ni gratuité implicite ; aucune publication demandée.''')
    OUT.mkdir()
    for stem in ['model','supplier-return-behaviors','behavior-gap-audit']:
        (OUT/(stem+'-before.yaml')).write_bytes((ROOT/f'modeles/backlog/{stem}.yaml').read_bytes())
    refs=['U386','U388','ELM233','CMP144']; stamp=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    def life(values, approved=()):
        return dict(state='urbanist_validated' if approved else 'under_instruction', recorded_at=stamp, recorded_by='Codex',
            source_refs=['U388'], validated_fields=list(approved), value_sha256={f:value_hash(values[f]) for f in approved},
            note='Nom, principe et parent demandés U388 ; rédaction détaillée et contrat proposés.')
    parent=next(n for n in m['nodes'] if n['id']=='D04.m')
    parent['fields']['definition']='Prendre en charge les retours de marchandises aux fournisseurs et suivre leurs suites attendues, selon les accords applicables, en distinguant renvoi sans remplacement, remplacement et réparation avec restitution du bien.'
    parent['fields']['decomposition_rationale'] += ' Le retour pour réparation ajoute un attendu distinct : récupérer le même bien remis en état, avec sa traçabilité et son immobilisation, plutôt que recevoir un autre produit.'
    parent['fields']['scope']=parent['fields']['scope'].replace('Deux comportements combinables sont adoptés U387.',
        'Trois comportements combinables sont retenus : Return for Credit et Return for Replacement adoptés U387, complétés par Return for Repair demandé U388.')
    obsolete='Return for Repair reste à instruire : reprise au titre d’une obligation du fournisseur et achat de prestation à un réparateur ne sont pas automatiquement la même responsabilité. Aucun troisième comportement, service de réparation ou schéma comptable ajouté par extension.'
    assert obsolete in parent['fields']['scope']
    parent['fields']['scope']=parent['fields']['scope'].replace(obsolete,
        'Return for Repair suit le renvoi et la restitution attendue du même bien. Le traitement physique reste chez le fournisseur ou prestataire et son orchestration dans D06. '
        'Lorsque la prestation nécessite un achat, Purchase Order porte cet achat ; aucun devis, garantie, gratuité ou schéma comptable imposé. '
        'Une impossibilité de réparer peut conduire à un autre devenir après décision autorisée, jamais à un remplacement implicite.')
    parent['revision']+=1; parent['source_refs']=list(dict.fromkeys(parent['source_refs']+refs))
    parent['review']['note']='Trois parcours : Credit et Replacement adoptés U387 ; Repair ajouté U388. Définition développée et contrats restent éditoriaux.'
    candidate=deepcopy(review['conditional_candidate'])
    market=deepcopy(review['market_comparisons'][3])
    market.update(source_locator='Repair Program Influence on Service Supply Chain Lead Time Offset ; Assigning Sourcing Rule – Repair at',
        evidence_limits='Page primaire ouverte le 18 septembre 2026 ; référence historique EBS 12.1, pas preuve de couverture Fusion ou Beaumanoir. Le passage ne démontre pas une traçabilité sérialisée identique à notre exigence.',
        flow_position='U388 place le suivi du renvoi et de la restitution sous Supplier Return. Achat de prestation et orchestration restent distincts ; rattachement FLOW, pas équivalence au catalogue Oracle.',
        source_refs=refs)
    parent['fields']['market_comparisons'].append(deepcopy(market))
    fields=dict(name='Return for Repair', definition=candidate['definition'], finality=candidate['benefit'],
        scope=('Préserver le lien entre le bien envoyé, la prestation attendue et le bien restitué. Suivre quantités, dates convenues, avancement et résultat, '
            'sans déduire la disponibilité du seul envoi ou d’une date annoncée. Restituer le même bien réparé se distingue de fournir un autre produit de remplacement.\n\n'
            'Exemple fictif : dix pièces sont renvoyées au fournisseur pour reprise de couture. Huit reviennent réparées, deux restent attendues. '
            'Si deux pièces ne sont pas réparables, leur autre devenir nécessite une décision autorisée ; le parcours ne transforme pas silencieusement cet attendu en remplacement.\n\n'
            '[Supplier Return](model:D04.m) porte le suivi de l’Order et du bien. [Purchase Order](model:D04.j) porte l’achat de prestation lorsqu’il est nécessaire. '
            '[Execution Management](model:D06) coordonne les prestations et remonte leurs faits ; [Inventory Management](model:D01) enregistre mouvements et états. '
            'L’exécutant réalise la réparation. La garantie, le coût et l’accord de prise en charge sont des conditions applicables ; ni gratuité ni négociation absorbée.\n\n'
            'Ce parcours peut servir une remise en état issue de [Customer Return](model:D04.l), sans dupliquer la prise en charge client. '
            'Les autres retours peuvent suivre Credit ou Replacement selon leurs accords ; aucun sous-comportement ou séquence universelle. Les exemples sont illustratifs.'),
        market_comparisons=[market])
    node=dict(id='BHV057', revision=1, kind='behavior', layer=parent['layer'], fields=fields, source_refs=refs,
        source_locator=dict(path='connaissance/01-contributions-utilisateur.md',anchor='u388'),adoption_ids=[],
        review=dict(state='partial',note='Nom, principe de réparation avec restitution du même bien et parent adoptés ; définition développée et descriptions proposées.'),lifecycle=life(fields,['name']))
    m['nodes'].append(node)
    rel=dict(id='REL-BEHAVIOR-BHV057',revision=1,type='contains',source_id='D04.m',target_id='BHV057',source_refs=refs,review=dict(state='accepted',note='Ajout explicite U388.'))
    rel['lifecycle']=life(rel,['type','source_id','target_id']);m['relations'].append(rel)
    m['relations'].append(dict(id='REL-NEEDS-U388-REPAIR-EXECUTION',revision=1,type='relates-to',source_id='BHV057',target_id='D06.d',source_refs=refs,
        qualification=dict(role='needs',meaning='A besoin de la coordination des prestations de renvoi, réparation et restitution selon les services retenus.',
            conditions=['Lorsque ces prestations relèvent de l’orchestration Supply.'],effects=['Suivre l’Order sans reprendre l’orchestration détaillée ni la réalisation physique.']),
        review=dict(state='proposed',note='Contrat détaillé éditorial.'),lifecycle=life({})))
    save('modeles/backlog/model.yaml',m)
    principle='Suivre l’envoi du bien au fournisseur puis la restitution attendue du même bien réparé, distincte du remplacement par un autre produit.'
    migration=dict(source_refs=refs,model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),
        delta={},behaviors=[],adopted_behaviors=[dict(node_id='BHV057',parent_id='D04.m',adopted_fields=['name'],value_sha256=node['lifecycle']['value_sha256'],principle=principle,principle_sha256=value_hash(principle))])
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]};new={x['id']:x for x in m[key]}
        migration['delta'][key]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},changed={i:value_hash(new[i]) for i in sorted(new.keys()&old.keys()) if new[i]!=old[i]},removed=sorted(old.keys()-new.keys()))
    (OUT/'implementation.yaml').write_text(dumps(migration),encoding='utf-8')
    review['conditional_candidate']['status']='integrated_U388'
    review['conditional_candidate']['node_id']='BHV057'
    review['conditional_candidate']['recommendation']='Ajouté U388 ; conserver achat, réparation physique, suivi du retour et stock distincts. L’issue décrit le point de frontière étudié U386, pas un blocage courant.'
    review['status']='integrated_U388';review['source_refs'].append('U388');review['implementation_U388']=migration
    review['current_U388']=dict(capability_id='D04.m',behavior_ids=['BHV055','BHV056','BHV057'],scope='Trois parcours intégrés ; les contrats détaillés gardent leur statut propre.')
    save(rp,review)
    current=dict(source_refs=['U388'],capability_id='D04.m',behavior_ids=['BHV055','BHV056','BHV057'],status='integrated',review_path=rp)
    for stem in ['d04-refactoring','order-lifecycle-behaviors']:
        p=f'modeles/backlog/{stem}.yaml';d=read(ROOT/p);d['supplier_return_U388']=current;save(p,d)
    ap='modeles/backlog/behavior-gap-audit.yaml';a=read(ROOT/ap);a['source_refs'].append('U388');a['implementation_U388']=migration;a['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest()
    assessment=next(x for x in a['assessments'] if x['capability_id']=='D04.m')
    assessment.update(existing_behaviors=['BHV055','BHV056','BHV057'],verdict='trois parcours intégrés U388',diagnosis=parent['fields']['decomposition_rationale'],recommendation='Distinguer absence de remplacement, remplacement et restitution du bien réparé ; achat de prestation et exécution restent distincts.')
    a['existing_behavior_review'].append(dict(behavior_id='BHV057',status='integrated_U388',market_sources=[],recommendation='Nom, principe et parent acquis U388 ; rapprochement Oracle EBS et limites dans la fiche via ELM233/CMP144. Contrats détaillés proposés.'))
    save(ap,a)
    append('marche/comparaisons.md', '''### Complément CMP144 — U388

Return for Repair ajouté sous Supplier Return (BHV057) à la demande explicite de Laurent. Le point de rattachement laissé conditionnel U386 est tranché ; les frontières d’achat de prestation, d’orchestration et de stock restent distinctes. La page primaire Oracle EBS 12.1 est ouverte de nouveau : Repair Return (Pull), délais de transfert/réparation/réception et achat au réparateur sont documentés. Le passage n’établit pas une traçabilité sérialisée identique à notre exigence. Comparaison proposée, sans assimilation au catalogue Oracle Fusion ni preuve de déploiement. Nom, principe et parent acquis ; détails éditoriaux non adoptés globalement. Preuve : audits/2026-09-18-supplier-repair-U388/implementation.yaml.''')
    (OUT/'README.md').write_text('''# Return for Repair — U388

BHV057 ajouté sous Supplier Return. Nom, principe et parent acquis ; restitution du même bien réparé distincte du remplacement. Achat de prestation, exécution et stocks conservent leurs responsabilités. Aucun devis ou coût de réparation implicitement validé. Comparaison Oracle EBS documentée avec ses limites. Le caractère conditionnel U386 est levé ; détails éditoriaux et contrats restent proposés. Backlog uniquement.
''',encoding='utf-8')
    print('U388: BHV057 integrated under Supplier Return.')


if __name__=='__main__':
    main()

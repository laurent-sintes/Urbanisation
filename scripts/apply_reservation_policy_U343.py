"""Record U343 with field-scoped approvals and preserve the U342 proposal."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

from scripts.lifecycle import value_hash
from scripts.structured_io import read, dumps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'audits/2026-09-18-reservation-policy-adoption'


def append(path, text):
    with (ROOT/path).open('a', encoding='utf-8') as stream:
        stream.write('\n\n'+text.strip()+'\n')


def main():
    assert not OUT.exists(), 'U343 already recorded.'
    assert '## U343\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    OUT.mkdir()
    for name in ['model', 'reservation-policy-review', 'assignment-reservation-review', 'behavior-gap-audit']:
        (OUT/(name+'-before.yaml')).write_bytes((ROOT/('modeles/backlog/'+name+'.yaml')).read_bytes())
    (OUT/'report-before.md').write_bytes((ROOT/'audits/2026-09-18-reservation-policy/README.md').read_bytes())
    append('connaissance/01-contributions-utilisateur.md', '''## U343

**id**

U343

**date**

2026-09-18

**titre**

Validation des comportements de Reservation Policy Decision et du rattachement à D05

**texte**

Je valide

**contexte et portée**

Accord sur la proposition présentée après U342 : Milestone-Based Reservation Policy, Time-Fenced Reservation Policy, Demand-Differentiated Reservation Policy et Risk-Adaptive Reservation Policy, combinables et directement sous Reservation Policy Decision ; rattachement de cette capacité à D05 Inventory Optimization. Les noms et responsabilités résumées dans le tableau sont adoptés, ainsi que les cinq relations de décomposition. Les définitions développées, exemples détaillés, entrées/résultats, relations « a besoin de », comparaisons marché et 19 cas de frontière ne reçoivent pas de validation globale implicite. Les exemples chiffrés restent illustratifs. Portée et empreintes dans reservation-policy-review.yaml, adoption_U343. Aucune release demandée.''')
    m=read(ROOT/'modeles/backlog/model.yaml'); before=deepcopy(m)
    nodes={n['id']:n for n in m['nodes']}
    r=read(ROOT/'modeles/backlog/reservation-policy-review.yaml')
    now=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    summaries={
        'BHV032':'À quel événement du parcours commencer à réserver et maintenir la protection.',
        'BHV033':'À quelle distance de la date de besoin commencer à réserver.',
        'BHV034':'Quelles conditions appliquer selon les engagements de service.',
        'BHV035':'Comment adapter le déclenchement et la durée selon la tension et le risque d’immobilisation inutile.'}
    scope='U343 adopte le nom, la responsabilité résumée et le parent ; descriptions développées et correspondances restent éditoriales.'
    behaviors=[]
    position='U343 adopte les quatre mécanismes sous Reservation Policy Decision et D05 comme domaine. Le rapprochement marché reste proposé ; aucun moteur adaptatif standard ni déploiement client déduit.'
    for e in r['behaviors']:
        n=nodes[e['node_id']]
        n['revision']+=1
        n['source_refs'].append('U343')
        n['lifecycle']=dict(state='urbanist_validated',recorded_at=now,recorded_by='Codex',source_refs=['U343'],
            validated_fields=['name'],value_sha256={'name':value_hash(n['fields']['name'])},note=scope)
        n['review']=dict(state='partial',note=scope)
        n['editorial_basis']+=' U343 adopte nom, responsabilité du tableau et parent ; empreinte de la responsabilité dans reservation-policy-review.yaml.'
        for c in n['fields']['market_comparisons']:
            c['flow_position']=position
            c['source_refs']=list(dict.fromkeys(c['source_refs']+['U343']))
        summary=summaries[n['id']]
        adopted=dict(node_id=n['id'],parent_id='D05.h',adopted_fields=['name'],value_sha256=n['lifecycle']['value_sha256'],
            responsibility=summary,responsibility_sha256=value_hash(summary),
            relation_id='REL-BEHAVIOR-'+n['id'])
        behaviors.append(adopted)
        e['status']='adopted_name_responsibility_parent_U343'
        e['adopted_responsibility']=summary
        e['adopted_responsibility_sha256']=value_hash(summary)
        e['definition_status']='editorial_proposed'
        e['evidence']=e['evidence'].replace('nom de regroupement FLOW proposé','nom de regroupement FLOW adopté U343').replace('Proposition FLOW issue de U341','Mécanisme FLOW issu de U341 et adopté U343')
    cap=nodes['D05.h']; cap['revision']+=1; cap['source_refs'].append('U343')
    cap['review']['note']='Nom et définition adoptés U342 ; décomposition et parent D05 adoptés U343. Descriptions détaillées et comparaisons restent éditoriales.'
    cap['lifecycle']['note']=cap['review']['note']
    cap['fields']['scope']=cap['fields']['scope'].replace('Les quatre comportements proposés se combinent','Les quatre comportements adoptés U343 se combinent')
    cap['fields']['scope']=cap['fields']['scope'].replace('Rattachement proposé à Inventory Optimization','Rattachement adopté U343 à Inventory Optimization')
    cap['fields']['scope']=cap['fields']['scope'].replace('Ce parent n’a pas été présenté lors de la validation U342 et reste proposé.','Ce parent proposé après U342 est adopté U343 ; les contrats détaillés restent proposés.')
    cap['fields']['decomposition_rationale']=cap['fields']['decomposition_rationale'].replace('sont proposés','sont retenus U343')
    for c in cap['fields']['market_comparisons']:
        c['flow_position']=position; c['source_refs']=list(dict.fromkeys(c['source_refs']+['U343']))
    adopted_relations=[]
    for rel in m['relations']:
        if rel['id'] not in ['REL-MEMBER-D05.h']+[e['relation_id'] for e in behaviors]:
            continue
        rel['revision']+=1; rel['source_refs'].append('U343')
        rel['review']=dict(state='accepted',note='Décomposition présentée et adoptée U343.')
        fields=['type','source_id','target_id']
        rel['lifecycle']=dict(state='urbanist_validated',recorded_at=now,recorded_by='Codex',source_refs=['U343'],
            validated_fields=fields,value_sha256={f:value_hash(rel[f]) for f in fields},note=rel['review']['note'])
        adopted_relations.append(dict(relation_id=rel['id'],adopted_fields=fields,value_sha256=rel['lifecycle']['value_sha256']))
    r['source_refs'].append('U343'); r['status']='capability_behaviors_and_parent_adopted_scoped'
    r['adopted_parent']=r.pop('proposed_parent'); r['adopted_parent']['source_refs']=['U343']
    r['decomposition_rationale']=cap['fields']['decomposition_rationale']
    r['adoption_U343']=dict(source_refs=['U343'],scope=scope,behaviors=behaviors,relations=adopted_relations)
    r['open_questions']=['Arbitrer le porteur de gouvernance et de mise en vigueur des politiques.',
        'Qualifier les réservations coordonnées/partielles avant tout élargissement de la capacité.',
        'Instruire les descriptions détaillées et contrats sans confondre la validation des comportements avec celle de toutes les modalités.']
    for c in r['market_comparisons']:
        c['flow_position']=position;c['source_refs']=list(dict.fromkeys(c['source_refs']+['U343']))
    (ROOT/'modeles/backlog/reservation-policy-review.yaml').write_text(dumps(r),encoding='utf-8')
    discussion=read(ROOT/'modeles/backlog/assignment-reservation-review.yaml')
    discussion['source_refs'].append('U343')
    discussion['adoption_U343']=dict(capability_id='D05.h',domain_id='D05',behavior_ids=list(summaries),
        registry='modeles/backlog/reservation-policy-review.yaml',scope=scope+' A01 reste ouvert sur les autres frontières affectation/réservation.')
    (ROOT/'modeles/backlog/assignment-reservation-review.yaml').write_text(dumps(discussion),encoding='utf-8')
    (ROOT/'modeles/backlog/model.yaml').write_text(dumps(m),encoding='utf-8')
    migration=dict(source_refs=['U343'],model_before=str((OUT/'model-before.yaml').relative_to(ROOT)).replace('\\','/'),
        model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),delta={},behaviors=[],
        adopted_behaviors=behaviors,adopted_relations=adopted_relations,scope=scope)
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]};new={x['id']:x for x in m[key]}
        migration['delta'][key]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
            changed={i:value_hash(new[i]) for i in sorted(new.keys()&old.keys()) if new[i]!=old[i]},removed=sorted(old.keys()-new.keys()))
    (OUT/'implementation.yaml').write_text(dumps(migration),encoding='utf-8')
    audit=read(ROOT/'modeles/backlog/behavior-gap-audit.yaml');audit['source_refs'].append('U343')
    audit['implementation_U343']=migration
    audit['baseline']['sha256']=sha256((ROOT/'modeles/backlog/model.yaml').read_bytes()).hexdigest()
    for a in audit['assessments']:
        if a['capability_id']=='D05.h':
            a['verdict']='quatre comportements et parent D05 adoptés U343'
            a['diagnosis']=r['decomposition_rationale']
            a['recommendation']='Préciser gouvernance des politiques et contrats détaillés ; conserver les comparaisons avec leurs limites de preuve.'
    for a in audit['existing_behavior_review']:
        if a['behavior_id'] in summaries:
            a['status']='adopted_scope_editorial_details_proposed'
            a['recommendation']='U343 : nom, responsabilité présentée et parent adoptés ; définitions développées, modalités et correspondances proposées.'
    (ROOT/'modeles/backlog/behavior-gap-audit.yaml').write_text(dumps(audit),encoding='utf-8')
    p=ROOT/'AGENTS.md'; text=p.read_text(encoding='utf-8')
    text=text.replace('## Précision Reservation — U339–U342','## Précision Reservation — U339–U343')
    text=text.replace('D05 comme parent et les quatre comportements BHV032–BHV035 restent proposés','U343 adopte D05 comme parent et les quatre comportements BHV032–BHV035 (noms, responsabilités présentées et parents) ; les détails éditoriaux et comparaisons gardent leurs statuts propres')
    p.write_text(text,encoding='utf-8')
    append('marche/comparaisons.md','''Complément U343 à CMP121 — 18 septembre 2026 : Laurent adopte les quatre comportements de Reservation Policy Decision (noms et responsabilités résumées présentées) et le rattachement à D05. Les équivalences marché ne sont pas validées par cet accord ; les limites sur le moteur adaptatif restent explicites. Aucune nouvelle proposition marché ni changement de périmètre motivant une nouvelle recherche.''')
    append('JOURNAL.md','''## 2026-09-18 — U343 : adoption des politiques de réservation

Quatre comportements adoptés sous Reservation Policy Decision et rattachement D05 confirmé. Noms et responsabilités présentées tracés séparément des détails éditoriaux ; cinq relations contains validées. État U342 préservé dans audits/2026-09-18-reservation-policy-adoption. Aucune nouvelle publication.''')
    (OUT/'README.md').write_text('# Validation U343 — Reservation Policy Decision\n\nQuatre noms de comportements et responsabilités présentées adoptés, avec leur parent D05.h et le parent D05 de la capacité. Les descriptions développées, contrats et comparaisons restent proposés.\n\nPortée et empreintes : [implementation.yaml](implementation.yaml). [Documentation courante](../2026-09-18-reservation-policy/README.md).\n',encoding='utf-8')
    print('U343 recorded: four behaviors and five containment relations adopted with scoped evidence.')


if __name__=='__main__':
    main()

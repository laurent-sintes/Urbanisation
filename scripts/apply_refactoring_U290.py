"""Apply the reviewed U286–U289 core under U290; freeze evidence first.

One-shot migration, deliberately refuses a second run. Rendering is separate.
"""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re

from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-17-refonte-appliquee'
STAMP = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def write(path, value):
    (ROOT/path).write_text(dumps(value), encoding='utf-8')


def append(path, value):
    with (ROOT/path).open('a', encoding='utf-8') as f:
        f.write('\n\n'+value.strip()+'\n')


def cycle(item, approved=(), note='Intégration U290 ; détails éditoriaux proposés.'):
    fields = item.get('fields', item)
    old = item.get('lifecycle', {})
    retained = [k for k in old.get('validated_fields', [])
                if k in fields and old['value_sha256'][k] == value_hash(fields[k])]
    keys = list(dict.fromkeys(retained+list(approved)))
    item['lifecycle'] = dict(state='urbanist_validated' if keys else 'under_instruction',
        recorded_at=STAMP, recorded_by='Codex',
        source_refs=list(dict.fromkeys(old.get('source_refs', [])+['U290'])),
        validated_fields=keys, value_sha256={k:value_hash(fields[k]) for k in keys}, note=note)
    item['review'] = dict(state='partial' if keys else 'under_review', note=note)
    item['source_refs'] = list(dict.fromkeys(item.get('source_refs', [])+['U290']))
    if 'approved_fields' in item: item['approved_fields'] = keys
    if 'proposed_fields' in item: item['proposed_fields'] = [k for k in fields if k not in keys]


def node(identifier, kind, fields, approved=()):
    n = dict(id=identifier, revision=1, kind=kind, layer='transactional', fields=fields,
             source_refs=['U290'], source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u290'), adoption_ids=[])
    cycle(n, approved)
    return n


def contains(parent, child):
    r = dict(id='REL-MEMBER-'+child, revision=1, type='contains', source_id=parent, target_id=child, source_refs=['U290'])
    cycle(r, ['type','source_id','target_id'], 'Structure de la refonte demandée U290 ; formulations détaillées qualifiées sur chaque nœud.')
    return r


def main():
    if OUT.exists(): raise SystemExit('Capture U290 déjà présente : ne pas réappliquer.')
    OUT.mkdir()
    paths=['model','refactoring-target','glossary','modeling-glossary','assignment-terminology']
    for name in paths:
        (OUT/(name+'-before.yaml')).write_bytes((ROOT/f'modeles/backlog/{name}.yaml').read_bytes())
    (OUT/'AGENTS-before.md').write_bytes((ROOT/'AGENTS.md').read_bytes())
    protected={p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest()
        for folder in ['release','revisions','decisions','provenance'] for p in (ROOT/'modeles'/folder).rglob('*')
        if p.is_file() and p.name!='source-records.json'}
    (OUT/'protected.json').write_text(json.dumps(protected,indent=2),encoding='utf-8')
    m=read(ROOT/'modeles/backlog/model.yaml'); before=deepcopy(m)
    t=read(ROOT/'modeles/backlog/refactoring-target.yaml')
    assert sha256((OUT/'model-before.yaml').read_bytes()).hexdigest()==t['baseline']['sha256']
    ns={n['id']:n for n in m['nodes']}; profiles={c['id']:c for c in t['capabilities']}
    old_promise=['D03.a','D03.b','D03.c']; new_promise='D03.n'
    assert new_promise not in ns
    mapping={'PROMISE-MANAGEMENT':new_promise, 'PLAN-CONSTRUCT':'BHV005', 'PLAN-SIMULATE':'BHV006',
             'PLAN-ADAPT':'BHV016', 'PROTECT-GROUP':'BHV017', 'PROTECT-CAP':'BHV018',
             'PROTECT-BUFFER':'BHV019', 'PROTECT-REPLENISH':'BHV020',
             'PROMISE-PROPOSE':'BHV021', 'PROMISE-CONFIRM':'BHV022', 'PROMISE-REVISE':'BHV023'}
    redirects={**dict(zip(old_promise,['BHV021','BHV022','BHV023'])),
               'BHV007':'D05.f','BHV008':'D05.f','BHV009':'D05.f','BHV010':'BHV006',
               **{f'BHV{i:03}':'D02.b' for i in range(11,16)}}
    retired=set(redirects)
    assert all(v not in ns for k,v in mapping.items() if k not in ['PLAN-CONSTRUCT','PLAN-SIMULATE'])
    # New wording is editorial. Retain only hashes of truly unchanged adopted values.
    for c in t['capabilities']:
        if c['id'] in old_promise: continue
        n=ns[c['id']]; target=c['target']; f=n['fields']
        for key in ['name','definition','finality','nature']:
            if target.get(key): f[key]=target[key]
        # Existing scopes contain useful concrete operations: keep them unless obsolete.
        if c['id'] not in ['D02.b','D05.f']:
            additions=[]
            if c['id'] not in ['D05.d','D04.o']:
                additions.append('Frontière : '+target['boundary'])
            additions.append('Exemple fictif : '+target['example'])
            f['scope']='\n\n'.join(filter(None,[f.get('scope','')]+additions))
        else:
            f['scope']=target['scope']
        if c['behavior_keys'] and c['recommendation']!='conditional_behaviors':
            f['decomposition_rationale']=c['decomposition_rationale']
        cycle(n, ['name'] if c['id']=='D05.d' else ['nature'] if c['id']=='D04.o' else [])
        n['editorial_basis']='Refonte U290 depuis la cible U286–U289. Formulations et exemples ajoutés restent éditoriaux ; accords antérieurs conservés seulement sur valeurs inchangées. Historique : audits/2026-09-17-refonte-appliquee/model-before.yaml.'
    ns['D02.b']['fields']['scope'] += '\n\nLes opérations de création d’enveloppes, réallocation entre groupes, libération des droits inutilisés, imputation de consommation et consultation des quantités allouées, consommées et restantes restent des fonctions utiles. Les règles ont une validité, une portée et des conditions de dérogation. Leur application transactionnelle est possible à l’unité, par groupe ou en masse, via écran, batch, flux ou streaming ; ces modalités ne créent pas de comportement supplémentaire.'
    ns['D05.d']['fields']['scope'] += '\n\nLa décision porte les quantités protégées et limites d’usage des groupes. Supply Protection applique les droits retenus ; Supply Assignment affecte les ressources aux commandes. L’ancien nom Stock Allocation Decision est conservé dans les preuves historiques.'
    ns['D05.e']['fields']['finality']='Adapter les apports futurs pour maîtriser les manques et les excès, compte tenu des engagements et des contraintes de modification.'
    ns['D05.e']['fields']['scope'] += '\n\nExaminer aussi la réduction, le report ou l’annulation d’apports devenus excessifs. Une recommandation ne modifie pas un Order ferme : D04 vérifie et applique les changements autorisés. Si la modification est impossible, conserver explicitement l’excès résiduel et les options restantes.'
    ns['D04.o']['fields']['scope'] += '\n\nL’application d’un scénario ou d’un plan d’affectation peut déclencher ces transitions autorisées ; les changements de structure mobilisent Order Structuring et les changements de contenu les gestions par type. Conserver l’origine du plan, la portée, les résultats, refus et effets partiels. Supply Assignment conserve les liens ressources-commandes. Le parent d’un éventuel comportement transverse d’application de plan reste à instruire, sans nouvelle capacité ajoutée.'
    assignment=ns['D02.e']['fields']
    assignment['definition']='Affecter les ressources Supply présentes ou futures aux commandes identifiées, selon les priorités, les engagements et les contraintes applicables, afin de maximiser la valeur multidimensionnelle de leur satisfaction.'
    assignment['finality']='Maximiser la valeur multidimensionnelle de la satisfaction des commandes sous contraintes, en matérialisant les affectations retenues.'
    assignment['scope'] += '\n\nLa valeur peut combiner service, respect des engagements, coûts, contribution économique et risques ; ces dimensions sont des exemples, sans pondération ni formule universelle adoptée. Les décisions spécialisées conservent leurs responsabilités : priorité des Orders, faisabilité ATP/CTP, arbitrage économique PTP et échéancier. Affecter, réaffecter et libérer maintiennent les liens aux ressources ; affecté, réservé, promis et réalisé restent distincts. Le périmètre historique des engagements et besoins prévisionnels est conservé, avec articulation à préciser.'
    merge=t['merge_proposal']
    f=dict(name=merge['name'],definition=merge['definition'],nature='management',
           finality='Établir et maintenir des engagements Supply explicites et cohérents avec les possibilités retenues.',
           decomposition_rationale=merge['decomposition_rationale'].replace(' Principe adopté U288 ; formulation justificative proposée.',''),
           scope='Trois comportements : proposition sans engagement confirmé, confirmation des quantités et dates, révision lorsque la situation évolue. Les décisions ATP/CTP/PTP, priorités et échéancier restent distinctes, ainsi que Supply Assignment et Reservation. Exemple fictif : proposer 60 vendredi et 40 lundi, confirmer la première part puis réexaminer la seconde après retard fournisseur. Aucune confirmation n’est assimilée à un mouvement physique ni à une réservation automatique.')
    promise=node(new_promise,'capability',f,['name']); promise['source_refs']+=['U288']
    m['nodes'].append(promise); ns[new_promise]=promise
    m['relations'].append(contains('D03',new_promise))
    for b in t['behaviors']:
        if b['status']=='conditional_arbitration' or b['key'].startswith('BHV'): continue
        identifier=mapping[b['key']]; parent=mapping.get(b['parent_id'],b['parent_id'])
        boundary=b['boundary'].replace('BHV006 et BHV010 réunis ; comparer reste une fonction, aucun recalcul imposé.', 'La projection et son analyse forment un même résultat explicatif ; comparaison et autorisation restent des fonctions utiles, sans calcul dupliqué.')
        fields=dict(name=b['name'],definition=b['definition'],scope=f"Critère différenciant : {b['differentiator']}. Bénéfice ciblé : {b['targeted_benefit']}\n\n{boundary}\n\nExemple fictif : {b['example']}")
        if identifier in ns:
            n=ns[identifier]; n['fields']=fields; cycle(n,['name'])
        else:
            n=node(identifier,'behavior',fields,['name']); m['nodes'].append(n); ns[identifier]=n
            m['relations'].append(contains(parent,identifier))
        if 'origin_capability_id' in b:
            old=next(n for n in before['nodes'] if n['id']==b['origin_capability_id'])
            if old['fields'].get('scope'): n['fields']['scope']+='\n\n'+old['fields']['scope']
        n['editorial_basis']='Comportement de la cible U286–U289 appliqué U290 ; définition détaillée, exemple et périmètre éditoriaux. Marché et justification : modeles/backlog/refactoring-target.yaml, '+b['key']+'.'
    # Explicitly remove obsolete nodes. Full records and adoptions remain in frozen baseline.
    m['nodes']=[n for n in m['nodes'] if n['id'] not in retired]
    relation_log=[]; kept=[]
    for r in m['relations']:
        old=deepcopy(r)
        if r['type']=='contains' and (r['source_id'] in retired or r['target_id'] in retired):
            relation_log.append(dict(id=r['id'],action='retired_structure',before=old)); continue
        for end in ['source_id','target_id']:
            r[end]=redirects.get(r[end],r[end])
        if r['type'] in ['confirms','associated-document','observed-result'] and old['source_id'] in old_promise:
            r['source_id']=new_promise
        if r['source_id']==r['target_id']:
            relation_log.append(dict(id=r['id'],action='internalized',before=old)); continue
        if r!=old:
            cycle(r); relation_log.append(dict(id=r['id'],action='redirected_to_same_responsibility',before=old,after=deepcopy(r)))
        kept.append(r)
    m['relations']=kept
    # Contracts use capability endpoints; equivalent projected contracts coalesce.
    contract_map={}; merged_deps={}
    for dep in t['dependencies']:
        a=new_promise if dep['consumer'] in old_promise else dep['consumer']
        b=new_promise if dep['provider'] in old_promise else dep['provider']
        if a==b:
            contract_map[dep['key']]=dict(action='internal_to_promise_management'); continue
        key=(a,b,dep['result'],dep['condition'],dep['effect'])
        merged_deps.setdefault(key,[]).append(dep['key'])
    for (a,b,result,condition,effect),origins in merged_deps.items():
        # Only reuse a historical edge already expressing consumer -> provider.
        existing=next((r for r in m['relations'] if r['type']=='relates-to' and r['source_id']==a and r['target_id']==b and
            ('mobilise' in r.get('qualification',{}).get('meaning','') or 'a besoin' in r.get('qualification',{}).get('meaning','') or 'utilise la capacité' in r.get('qualification',{}).get('meaning',''))),None)
        if existing:
            rel=existing
            q=rel['qualification']; q['role']='needs'
            q['conditions']=list(dict.fromkeys(q.get('conditions',[])+[condition]))
            q['effects']=list(dict.fromkeys(q.get('effects',[])+[effect]))
            q['scope']=q.get('scope','')+' Résultat attendu : '+result+'.'
            cycle(rel)
        else:
            rel=dict(id=f'REL-NEEDS-U290-{len(contract_map)+1:03}',revision=1,type='relates-to',source_id=a,target_id=b,
                source_refs=['U286','U290'],qualification=dict(role='needs',meaning=f'A besoin de {result[0].lower()+result[1:]}.',conditions=[condition],effects=[effect],scope='Contrat métier proposé : consommateur → fournisseur de résultat. Aucun appel technique systématique ; sources de données et conditions à éprouver.'))
            cycle(rel); m['relations'].append(rel)
        for origin in origins: contract_map[origin]=dict(action='integrated_contract_under_instruction',relation_id=rel['id'])
    # Rewrite active references only; never touch historical proofs or releases.
    def rewrite(value):
        if isinstance(value,str):
            for old,new in redirects.items():
                value=re.sub(r'(model:)'+re.escape(old)+r'(?=[)#])',lambda match:match[1]+new,value)
            return value.replace('Stock Allocation Decision','Group Protection Decision')
        if isinstance(value,list): return [rewrite(x) for x in value]
        if isinstance(value,dict): return {k:rewrite(v) for k,v in value.items()}
        return value
    for n in m['nodes']:
        prev=deepcopy(n['fields']); n['fields']=rewrite(n['fields'])
        if prev!=n['fields']: cycle(n)
    for r in m['relations']:
        if 'qualification' in r:
            prev=deepcopy(r['qualification']); r['qualification']=rewrite(prev)
            if prev!=r['qualification']: cycle(r)
    ns['D03']['fields']['scope']=ns['D03']['fields']['scope'].replace('D07 et Services portent','D06 et les services exécutants portent')+'\n\nPromise Management regroupe proposition, confirmation et révision en trois comportements. La satisfaction recherchée maximise une valeur multidimensionnelle selon objectifs et contraintes ; PTP conserve son arbitrage économique spécialisé.'
    ns['D05']['fields']['scope']=ns['D05']['fields']['scope'].replace('allocations aux groupes','droits de protection des groupes').replace('Le comportement Scenario Application','La fonction de mise en action')
    ns['D05']['fields']['scope']+='\n\nInventory Planning est décrit par trois comportements : Scenario Construction, Simulation & Analysis et Scenario Execution Adaptation. Comparaison, validation et déclenchement restent dans son périmètre ; aucune nouvelle capacité de décision ni application transactionnelle absorbée.'
    for identifier in ['D02.b','D05.d','D05.e','D04.o','D02.e','D03','D05']: cycle(ns[identifier])
    for p in m['principles']:
        if p['id']=='PRINCIPLE-JUSTIFIED-BEHAVIOR':
            p['statement']='Toute décomposition en comportements est justifiée par une complexité ou un bénéfice ciblé. Mécanisme, politique, variante ou bénéfice différencient les façons d’agir. Les opérations produit et modalités unité/masse/interface ne justifient pas seules un comportement. Capacité → Comportement est terminal.'; p['source_refs']+=['U282','U283','U290']
        if p['id']=='PRINCIPLE-INVENTORY-SCENARIO-APPLICATION':
            p['statement']='Inventory Planning comporte construction de scénarios alternatifs, Simulation & Analysis et adaptation du scénario en cours. Comparaison, autorisation et mise en action restent des fonctions utiles. L’application mobilise Supply Protection, les gestions d’Orders et D06 sans absorber leurs responsabilités.';p['source_refs']+=['U283','U284','U290']
    m['principles'].append(dict(id='PRINCIPLE-SUPPLY-ASSIGNMENT-VALUE',statement='Supply Assignment affecte les ressources aux commandes afin de maximiser une valeur multidimensionnelle sous contraintes. Les critères, règles de priorité et arbitrages économiques restent explicites et mobilisent les décisions spécialisées ; aucune pondération universelle ni optimum garanti. Supply Assignment Plan signifie plan d’affectation, distinct des enveloppes de protection de groupes.',source_refs=['U275','U289','U290']))
    m['limitations']=[x for x in m['limitations'] if 'aucune fusion ou rétrogradation' not in x]
    m['limitations'].append('Refonte U290 appliquée au socle recommandé. Décompositions Stocktaking/Orchestration conditionnelles, articulation réservation-affectation, rattachement du comportement transverse D04 et contrats détaillés restent à instruire. Registre : modeles/backlog/refactoring-implementation.yaml.')
    m['source_version']+=' + U290 refonte des comportements, Promise Management et valeur multidimensionnelle'
    for source in m['source_files']:
        source['sha256']=sha256((ROOT/source['path']).read_bytes()).hexdigest()
    write('modeles/backlog/model.yaml',m)
    glossary=read(ROOT/'modeles/backlog/glossary.yaml')
    for term in glossary['terms']:
        if term['id'] in ['TER017','TER078']:
            term['notes']=term.get('notes','')+'\n\nU290 : la finalité de l’affectation est de maximiser une valeur multidimensionnelle sous contraintes. Service, engagements, coûts et risques sont des exemples éditoriaux ; leurs poids et modes d’arbitrage ne sont pas fixés.'
            term['source_refs']=list(dict.fromkeys(term['source_refs']+['U290']))
    write('modeles/backlog/glossary.yaml',glossary)
    term=read(ROOT/'modeles/backlog/assignment-terminology.yaml')
    term['source_refs'].append('U290'); term['canonical']['definition']=assignment['definition']
    term['state']='convention_confirmed_U290'; term['name_cleanup']['status']='applied_U290'
    term['authority']='Convention confirmée et refonte demandée U290 ; valeur multidimensionnelle adoptée. Formulations détaillées et critères ajoutés restent éditoriaux.'
    term['rules'][-1]='Maximiser une valeur multidimensionnelle sous contraintes ; les critères et leurs priorités sont explicites, sans réduire la valeur au volume promis ni à la marge.'
    write('modeles/backlog/assignment-terminology.yaml',term)
    method=read(ROOT/'modeles/backlog/modeling-glossary.yaml')
    planning=next(x for x in method['terms'] if x['id']=='MOD002')
    planning['definition']='Construire des scénarios alternatifs, simuler et analyser leurs conséquences, puis adapter le scénario en cours en mobilisant les décisions spécialisées et les capacités responsables de sa mise en action.'
    planning['notes'].append('U290 applique la refonte : trois comportements Inventory Planning. Les anciennes décompositions U269/U271 ci-dessus décrivent les accords historiques remplacés, pas la hiérarchie courante.')
    planning['source_refs'].append('U290'); planning['review']['state']='partial'
    write('modeles/backlog/modeling-glossary.yaml',method)
    # Preserve target as the reviewed baseline, with a clear pointer to implementation.
    t['state']='core_implemented_U290_with_open_questions'
    t['implementation']=dict(source_ref='U290',registry='modeles/backlog/refactoring-implementation.yaml',report='audits/2026-09-17-refonte-appliquee/rapport.md')
    write('modeles/backlog/refactoring-target.yaml',t)
    registry=dict(id='REFACTORING-U290',as_of='2026-09-17',source_refs=['U286','U287','U288','U289','U290'],
        state='core_implemented',baseline='audits/2026-09-17-refonte-appliquee/model-before.yaml',
        reviewed_target='audits/2026-09-17-refonte-appliquee/refactoring-target-before.yaml',
        applied_names=mapping,retired_node_redirects=redirects,retired_ids_never_reuse=sorted(retired),
        capability_merge=dict(source_ids=old_promise,target_id=new_promise,behavior_ids=['BHV021','BHV022','BHV023']),
        relation_migration=relation_log,dependency_contracts=contract_map,
        decision_scope='U290 autorise la refonte présentée et adopte la valeur multidimensionnelle. Les nouveaux détails éditoriaux et contrats gardent leurs statuts proposés ; les accords antérieurs ne sont conservés que pour leurs valeurs inchangées.',
        open_questions=['A3 : articulation réservation/affectation et décompte sans doublon.', 'A6 : quatre comportements optionnels Stocktaking/Orchestration non créés.', 'A7 : contrats détaillés intégrés sous instruction, données/conditions à éprouver.', 'A8 : application de plan explicitée dans D04 ; parent transverse du comportement encore ouvert.'],
        migration_choices=['D03.n est une nouvelle capacité ; D03.a/b/c redirigent vers leurs comportements respectifs pour conserver la précision des liens métier.', 'D05.d renommé Group Protection Decision à périmètre conservé.', 'D04.o nature management ; D05.e ajustements des apports futurs explicités sous contraintes.', 'Les 133 propositions de contrats sont tracées, coalescées après fusion seulement si résultat/condition/effet identiques ; les liens métier de sens différent sont conservés.'])
    write('modeles/backlog/refactoring-implementation.yaml',registry)
    for annex in ['d03-review','d05-refactoring','supply-protection-review','behavior-audit']:
        doc=read(ROOT/f'modeles/backlog/{annex}.yaml')
        doc['implementation_U290']=dict(state='core_applied',registry='modeles/backlog/refactoring-implementation.yaml',source_refs=['U290'],note='Les accords historiques ci-dessus restent des preuves datées ; lire le modèle courant et le registre pour les valeurs et rattachements après refonte.')
        write(f'modeles/backlog/{annex}.yaml',doc)
    # Backlog-only exploration metadata. Published model is not changed.
    p=ROOT/'app/exploration.json'; exploration=read(p)
    for old in old_promise:
        if old in exploration['aliases']: exploration['aliases'][redirects[old]]=exploration['aliases'].pop(old)
    exploration['aliases'][new_promise]='promise management promesse proposition confirmation révision'
    exploration['aliases']['D02.e']='affectation ressources commandes supply assignment valeur plan'
    exploration['confirmation']='BHV022'
    for step in exploration['steps']:
        if step['id']=='D03.b': step.update(id='BHV022',label='Comportement',text='Promise Confirmation précise les engagements de Promise Management ; regroupement U288, refonte U290.')
    p.write_text(json.dumps(exploration,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    append('JOURNAL.md','''## 2026-09-17 — U290 : refonte du backlog appliquée

Valeur multidimensionnelle pour Supply Assignment ; Promise Management D03.n et trois comportements ; trois comportements Planning ; quatre mécanismes Supply Protection ; ATP conservé. D05.d devient Group Protection Decision, D04.o management et D05.e explicite les ajustements d’apports sous contraintes. Les opérations restent dans les descriptions. Contrats de dépendance tracés sous instruction ; options conditionnelles et questions sans solution restent ouvertes. Captures, correspondances et portées : modeles/backlog/refactoring-implementation.yaml. Aucune publication modifiée.''')
    print('U290 core migrated; run validation and render before delivery.')


if __name__=='__main__': main()

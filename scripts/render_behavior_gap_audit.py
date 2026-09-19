"""Validate and render the proposed U292 audit without modifying the model."""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from scripts.structured_io import read, write_text_if_changed, yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'audits/2026-09-17-comportements-manquants'


def main():
    a=read(ROOT/'modeles/backlog/behavior-gap-audit.yaml')
    model=read(ROOT/a['baseline']['path'])
    nodes={n['id']:n for n in model['nodes']}
    caps={i for i,n in nodes.items() if n['kind']=='capability'}
    behaviors={i for i,n in nodes.items() if n['kind']=='behavior'}
    sources={s['id']:s for s in a['sources']}
    proposals={p['id']:p for p in a['candidates']}
    assert len(sources)==len(a['sources']) and len(proposals)==len(a['candidates'])
    assert {x['capability_id'] for x in a['assessments']}==caps
    assert len(a['assessments'])==len(caps)
    assert {b for x in a['assessments'] for b in x['existing_behaviors']}==behaviors
    assert {x['behavior_id'] for x in a['existing_behavior_review']}==behaviors
    assert a['baseline']['sha256']==sha256((ROOT/a['baseline']['path']).read_bytes()).hexdigest(), 'Baseline changed: re-audit before rendering.'
    current_model=model
    comparison_model=model
    for migration_key in ('implementation_U427', 'implementation_U425', 'implementation_U424', 'implementation_U420', 'implementation_U417', 'implementation_U414', 'implementation_U413', 'implementation_U410', 'implementation_U409', 'implementation_U406', 'implementation_U403', 'implementation_U402', 'implementation_U401', 'implementation_U398', 'implementation_U395', 'implementation_U391', 'implementation_U388', 'implementation_U387', 'implementation_U385', 'implementation_U384', 'implementation_U383', 'implementation_U380', 'implementation_U378', 'implementation_U373', 'implementation_U364', 'implementation_U363', 'implementation_U350', 'implementation_U349', 'implementation_U345', 'implementation_U343', 'implementation_U342', 'implementation_U334', 'implementation_U332'):
        if not a.get(migration_key):
            continue
        from scripts.lifecycle import value_hash
        migration=a[migration_key]
        capture=ROOT/migration['model_before']
        assert sha256(capture.read_bytes()).hexdigest()==migration['model_before_sha256']
        migrated_model=comparison_model
        comparison_model=read(capture)
        # Check each adoption against its actual historical stage. Later approved
        # reclassifications must not invalidate the preserved earlier agreement.
        model=migrated_model
        nodes={n['id']:n for n in model['nodes']}
        for collection in ['nodes','relations']:
            old={x['id']:x for x in comparison_model[collection]}
            new={x['id']:x for x in migrated_model[collection]}
            delta=migration['delta'][collection]
            assert new.keys()-old.keys()==set(delta['added'])
            assert old.keys()-new.keys()==set(delta['removed'])
            assert {i for i in old.keys()&new.keys() if old[i]!=new[i]}==set(delta['changed'])
            for identifier,digest in {**delta['added'],**delta['changed']}.items():
                assert value_hash(new[identifier])==digest, migration_key+' delta changed: '+identifier
        assert {k:v for k,v in migrated_model.items() if k not in ['nodes','relations']}=={k:v for k,v in comparison_model.items() if k not in ['nodes','relations']}
        if migration_key == 'implementation_U427':
            expected = {'BHV083', 'BHV084', 'BHV085'}
            assert set(migration['delta']['nodes']['added']) == expected
            assert set(migration['delta']['nodes']['changed']) == {'D05.e'}
            assert not migration['delta']['nodes']['removed']
            assert set(migration['delta']['relations']['added']) == {'REL-BEHAVIOR-'+i for i in expected}
            assert not migration['delta']['relations']['removed'] and not migration['delta']['relations']['changed']
            assert {r['target_id'] for r in model['relations'] if r['type']=='contains' and r['source_id']=='D05.e'} == expected
            assert nodes['D05.e']['fields']['decomposition_rationale']
            for previous in comparison_model['nodes']:
                for field in previous.get('lifecycle', {}).get('validated_fields', []):
                    assert nodes[previous['id']]['fields'][field] == previous['fields'][field]
            for adoption in migration['behaviors']:
                node = nodes[adoption['node_id']]
                assert node['kind']=='behavior' and node['layer']==nodes['D05.e']['layer']
                assert node['lifecycle']['validated_fields']==adoption['validated_fields']
                for field, digest in adoption['value_sha256'].items():
                    assert value_hash(node['fields'][field])==digest
                assert node['fields']['market_comparisons']
                assert not any(r['type']=='contains' and r['source_id']==node['id'] for r in model['relations'])
                parents = [r for r in model['relations'] if r['type']=='contains' and r['target_id']==node['id']]
                assert len(parents)==1 and parents[0]['source_id']=='D05.e'
                assert parents[0]['lifecycle']['validated_fields']==['type','source_id','target_id']
        if migration_key == 'implementation_U425':
            assert migration['delta']['nodes']['added'] == {} and migration['delta']['nodes']['removed'] == []
            assert set(migration['delta']['nodes']['changed']) == {'D05.e'}
            assert model['relations'] == comparison_model['relations']
            assert not [r for r in model['relations'] if r['type']=='contains' and r['source_id']=='D05.e']
            old=next(n for n in comparison_model['nodes'] if n['id']=='D05.e')
            assert nodes['D05.e']['fields']['definition'] == old['fields']['definition']
            assert nodes['D05.e']['lifecycle'] == old['lifecycle']
        if migration_key == 'implementation_U424':
            assert not migration['delta']['nodes']['added']
            assert set(migration['delta']['nodes']['removed']) == {'BHV041','BHV042'}
            assert set(migration['delta']['relations']['removed']) == {'REL-BEHAVIOR-BHV041','REL-BEHAVIOR-BHV042'}
            assert set(migration['delta']['relations']['added']) == {'REL-NEEDS-U424-D03.p-D04.o'}
            assert not migration['delta']['relations']['changed']
            assert set(r['target_id'] for r in model['relations'] if r['type']=='contains' and r['source_id']=='D04.o') == set(migration['dimension_ids'])
            assert len(migration['dimension_ids']) == 6
            assert nodes['D04.o']['fields']['definition'] == migration['adopted_definition']
            assert value_hash(migration['adopted_definition']) == nodes['D04.o']['lifecycle']['value_sha256']['definition']
            for identifier in migration['dimension_ids']:
                scope=nodes[identifier]['fields']['scope']
                for section in ['Dimension gouvernée','Portée des statuts','États possibles','Combinaisons et transitions','Exemple métier fictif']:
                    assert section in scope, (identifier,section)
                assert migration['editorial_state_lists'][identifier]
                for state in migration['editorial_state_lists'][identifier]: assert state in scope
                assert [r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']==identifier] == ['D04.o']
                assert 'scope' not in nodes[identifier]['lifecycle']['validated_fields']
            for previous in comparison_model['nodes']:
                if previous['id'] in migration['merges']: continue
                for field in previous.get('lifecycle',{}).get('validated_fields',[]):
                    if (previous['id'],field) in {('D04.o','definition'),('BHV043','name')}: continue
                    assert nodes[previous['id']]['fields'][field] == previous['fields'][field]
            for identifier,parent in {'D04.o':'D04','D04.q':'D03','D04.n':'D03'}.items():
                assert [r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']==identifier] == [parent]
        if migration_key == 'implementation_U420':
            for collection in ['nodes','relations']:
                assert not migration['delta'][collection]['added'] and not migration['delta'][collection]['removed']
            assert set(migration['delta']['relations']['changed']) == {'REL-MEMBER-D04.o','REL-MEMBER-D04.q'}
            for identifier,parent in {'D04.o':'D04','D04.q':'D03','D04.n':'D03','BHV039':'D04.o','BHV044':'D04.n'}.items():
                assert [r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']==identifier] == [parent]
            for previous in comparison_model['nodes']:
                current=nodes[previous['id']]
                for field in previous.get('lifecycle',{}).get('validated_fields',[]):
                    assert current['fields'][field] == previous['fields'][field]
                if previous['kind']=='behavior':
                    assert current['fields']['definition'] == previous['fields']['definition']
                    assert [r for r in model['relations'] if r['type']=='contains' and r['target_id']==previous['id']] == [r for r in comparison_model['relations'] if r['type']=='contains' and r['target_id']==previous['id']]
        if migration_key == 'implementation_U417':
            for collection in ['nodes', 'relations']:
                assert not migration['delta'][collection]['added'] and not migration['delta'][collection]['removed']
            assert set(migration['delta']['relations']['changed']) == set(migration['moves'])
            current_relations = {r['id']:r for r in model['relations']}
            for identifier, parent in migration['moves'].items():
                relation = current_relations[identifier]
                assert relation['source_id'] == parent
                for field in ['type','source_id','target_id']:
                    assert value_hash(relation[field]) == relation['lifecycle']['value_sha256'][field]
            for identifier, parent in {'D04.n':'D03','D04.o':'D03','BHV044':'D04.n','BHV039':'D04.o'}.items():
                assert [r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']==identifier] == [parent]
            assert nodes['D04.n']['fields']['definition'] == migration['structuring_definition']
            assert nodes['D04.n']['lifecycle']['value_sha256']['definition'] == value_hash(migration['structuring_definition'])
            assert not [r for r in model['relations'] if r['type']=='contains' and r['source_id']=='D03.p']
            assert len([r for r in model['relations'] if r['type']=='contains' and r['source_id']=='D04.o']) == 8
            assert 'definition' not in nodes['D03.p']['lifecycle']['validated_fields']
            for previous in comparison_model['nodes']:
                if previous['kind']=='behavior':
                    assert nodes[previous['id']]['fields']['definition'] == previous['fields']['definition']
                for field in previous.get('lifecycle',{}).get('validated_fields',[]):
                    if previous['id']=='D03.p' and field=='definition':
                        continue
                    assert nodes[previous['id']]['fields'][field] == previous['fields'][field]
        if migration_key == 'implementation_U414':
            assert set(migration['delta']['nodes']['added']) == {'D03.p'}
            assert set(migration['delta']['nodes']['changed']) == {'D03', 'D04.o', 'BHV039'}
            assert not migration['delta']['nodes']['removed']
            assert set(migration['delta']['relations']['added']) == {'REL-MEMBER-D03.p'}
            assert set(migration['delta']['relations']['changed']) == {'REL-BEHAVIOR-BHV039'}
            assert not migration['delta']['relations']['removed']
            cap = nodes['D03.p']
            assert cap['kind'] == 'capability' and cap['layer'] == nodes['D03']['layer']
            assert cap['fields']['name'] == migration['adopted_capability']['name']
            assert cap['fields']['definition'] == migration['adopted_capability']['definition']
            assert cap['fields']['decomposition_rationale']
            for field in ['name', 'definition', 'nature']:
                assert value_hash(cap['fields'][field]) == cap['lifecycle']['value_sha256'][field]
            assert [r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']=='D03.p'] == ['D03']
            assert [r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']=='BHV039'] == ['D03.p']
            assert [r['target_id'] for r in model['relations'] if r['type']=='contains' and r['source_id']=='D03.p'] == ['BHV039']
            assert len([r for r in model['relations'] if r['type']=='contains' and r['source_id']=='D04.o']) == 8
            for relation in model['relations']:
                if relation['id'] in {'REL-BEHAVIOR-BHV039', 'REL-MEMBER-D03.p'}:
                    for field in ['type','source_id','target_id']:
                        assert value_hash(relation[field]) == relation['lifecycle']['value_sha256'][field]
            for previous in comparison_model['nodes']:
                for field in previous.get('lifecycle', {}).get('validated_fields', []):
                    assert nodes[previous['id']]['fields'][field] == previous['fields'][field]
            old_nodes = {n['id']: n for n in comparison_model['nodes']}
            assert nodes['BHV044'] == old_nodes['BHV044'] and nodes['D04.n'] == old_nodes['D04.n']
        if migration_key == 'implementation_U413':
            assert not migration['delta']['nodes']['added'] and not migration['delta']['nodes']['removed']
            assert model['relations'] == comparison_model['relations']
            assert nodes['D03']['fields']['name'] == migration['adopted_name'] == 'Order Backlog Management'
            assert value_hash(migration['adopted_name']) == migration['name_sha256']
            assert nodes['D03']['lifecycle']['value_sha256']['name'] == migration['name_sha256']
            assert 'U413' in nodes['D03']['lifecycle']['source_refs']
            for previous in comparison_model['nodes']:
                for field in previous.get('lifecycle', {}).get('validated_fields', []):
                    if previous['id'] == 'D03' and field == 'name':
                        continue
                    assert nodes[previous['id']]['fields'][field] == previous['fields'][field]
            assert [r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']=='BHV039'] == ['D04.o']
        if migration_key == 'implementation_U410':
            assert set(migration['delta']['nodes']['changed']) == {'BHV039', 'D04.o'}
            assert not migration['delta']['nodes']['added'] and not migration['delta']['nodes']['removed']
            assert model['relations'] == comparison_model['relations']
            assert nodes['BHV039']['fields']['definition'] == migration['adopted_definition']
            assert value_hash(migration['adopted_definition']) == migration['definition_sha256']
            assert nodes['BHV039']['lifecycle']['value_sha256']['definition'] == migration['definition_sha256']
            assert 'U410' in nodes['BHV039']['lifecycle']['source_refs']
            for previous in comparison_model['nodes']:
                for field in previous.get('lifecycle', {}).get('validated_fields', []):
                    assert nodes[previous['id']]['fields'][field] == previous['fields'][field]
            assert len([r for r in model['relations'] if r['type'] == 'contains' and r['source_id'] == 'D04.o']) == 9
        if migration_key == 'implementation_U409':
            old_nodes = {n['id']: n for n in comparison_model['nodes']}
            assert len(migration['adopted_names']) == 9
            for identifier, name in migration['names'].items():
                assert nodes[identifier]['fields']['name'] == name
                if identifier in migration['adopted_names']:
                    assert nodes[identifier]['lifecycle']['value_sha256']['name'] == value_hash(name)
                    assert 'U409' in nodes[identifier]['lifecycle']['source_refs']
                else:
                    assert nodes[identifier]['lifecycle'] == old_nodes[identifier]['lifecycle']
            for identifier, previous in old_nodes.items():
                assert nodes[identifier]['kind'] == previous['kind']
                assert nodes[identifier]['layer'] == previous['layer']
                for field in previous.get('lifecycle', {}).get('validated_fields', []):
                    if field == 'name' and identifier in migration['adopted_names']:
                        continue
                    assert nodes[identifier]['fields'][field] == previous['fields'][field]
            assert [(r['id'], r['type'], r['source_id'], r['target_id']) for r in model['relations']] == [(r['id'], r['type'], r['source_id'], r['target_id']) for r in comparison_model['relations']]
            assert {r['target_id'] for r in model['relations'] if r['type'] == 'contains' and r['source_id'] == 'D07.d'} == {'BHV079', 'BHV080', 'BHV081', 'BHV082'}
        if migration_key in ('implementation_U401', 'implementation_U402', 'implementation_U403', 'implementation_U406'):
            expected = {
                'D01.h': {'BHV063', 'BHV064', 'BHV065'},
                'D04.i': {'BHV066', 'BHV067', 'BHV068', 'BHV069'},
                'D04.k': {'BHV070', 'BHV071', 'BHV072', 'BHV073', 'BHV074'},
            }
            if migration_key == 'implementation_U402':
                expected = {'D03.j': {'BHV075', 'BHV076', 'BHV077'}}
            if migration_key == 'implementation_U403':
                expected = {'D04.j': {'BHV058', 'BHV059', 'BHV060', 'BHV078'}}
            if migration_key == 'implementation_U406':
                expected = {'D07.d': {'BHV079', 'BHV080', 'BHV081', 'BHV082'}}
            added = {'BHV078'} if migration_key == 'implementation_U403' else set().union(*expected.values())
            assert set(migration['delta']['nodes']['changed']) == set(expected)
            assert set(migration['delta']['nodes']['added']) == added
            assert not migration['delta']['nodes']['removed']
            assert set(migration['delta']['relations']['added']) == {'REL-BEHAVIOR-'+i for i in added}
            assert not migration['delta']['relations']['changed'] and not migration['delta']['relations']['removed']
            assert {entry['node_id'] for entry in migration['adopted_behaviors']} == added
            assert len(migration['adopted_behaviors']) == len(added)
            for parent_id, children in expected.items():
                assert {r['target_id'] for r in model['relations'] if r['type']=='contains' and r['source_id']==parent_id} == children
                assert nodes[parent_id]['fields']['decomposition_rationale']
            for adoption in migration['adopted_behaviors']:
                node = nodes[adoption['node_id']]
                parent_id = adoption['parent_id']
                assert node['id'] in expected[parent_id]
                assert node['kind']=='behavior' and node['layer']==nodes[parent_id]['layer']
                assert node['lifecycle']['validated_fields']==adoption['adopted_fields']==['name','definition']
                for field, digest in adoption['value_sha256'].items():
                    assert value_hash(node['fields'][field]) == digest
                parents = [r for r in model['relations'] if r['type']=='contains' and r['target_id']==node['id']]
                assert len(parents)==1 and parents[0]['source_id']==parent_id
                assert parents[0]['lifecycle']['validated_fields']==['type','source_id','target_id']
                assert not any(r['type']=='contains' and r['source_id']==node['id'] for r in model['relations'])
            for previous in comparison_model['nodes']:
                for field in previous.get('lifecycle',{}).get('validated_fields',[]):
                    assert nodes[previous['id']]['fields'][field]==previous['fields'][field]
            if migration_key == 'implementation_U406':
                physical = a['adoption_U305']['values']['behaviors']
                for identifier, approved in zip(['BHV079','BHV080'], physical[:2]):
                    assert nodes[identifier]['fields']['name'] == approved['name']
                    assert nodes[identifier]['fields']['definition'] == approved['scope']
                store = a['adoption_U308']['values']
                assert nodes['BHV081']['fields']['name'] == store['name']
                assert nodes['BHV081']['fields']['definition'] == store['scope']
                assert nodes['BHV082']['fields']['name'] == 'Business Process Tracking'
                assert nodes['BHV082']['lifecycle']['source_refs'] == ['U406']
                assert not any(n['fields'].get('name') == 'Digital Service Visibility' for n in model['nodes'])
        if migration_key == 'implementation_U395':
            assert set(migration['delta']['nodes']['added']) == {'D01.h', 'D04.r'}
            assert set(migration['delta']['nodes']['changed']) == {'D01', 'D04'}
            assert not migration['delta']['nodes']['removed']
            assert {n['id'] for n in migrated_model['nodes'] if n['kind'] == 'behavior'} == {n['id'] for n in comparison_model['nodes'] if n['kind'] == 'behavior'}
            for adoption in migration['adopted_capabilities']:
                node = nodes[adoption['node_id']]
                assert node['kind'] == 'capability'
                for field, digest in adoption['value_sha256'].items():
                    assert value_hash(node['fields'][field]) == digest
                parents = [r for r in model['relations'] if r['type'] == 'contains' and r['target_id'] == node['id']]
                assert len(parents) == 1 and parents[0]['source_id'] == adoption['parent_id']
                assert parents[0]['lifecycle']['validated_fields'] == ['type', 'source_id', 'target_id']
            for previous in comparison_model['nodes']:
                for field in previous.get('lifecycle', {}).get('validated_fields', []):
                    assert nodes[previous['id']]['fields'][field] == previous['fields'][field]
        if migration_key in ('implementation_U387','implementation_U388','implementation_U391','implementation_U398'):
            parent_id = {'implementation_U391':'D04.j', 'implementation_U398':'D04.r'}.get(migration_key, 'D04.m')
            assert set(migration['delta']['nodes']['changed'])=={parent_id}
            assert not migration['delta']['nodes']['removed']
            added={entry['node_id'] for entry in migration['adopted_behaviors']}
            assert set(migration['delta']['nodes']['added'])==added
            expected = ({'BHV061','BHV062'} if migration_key=='implementation_U398' else {'BHV058','BHV059','BHV060'} if migration_key=='implementation_U391' else {'BHV055','BHV056'} | ({'BHV057'} if migration_key=='implementation_U388' else set()))
            assert {r['target_id'] for r in model['relations'] if r['type']=='contains' and r['source_id']==parent_id}==expected
            assert nodes[parent_id]['fields']['decomposition_rationale']
            for adoption in migration['adopted_behaviors']:
                node=nodes[adoption['node_id']]
                assert node['kind']=='behavior' and node['layer']==nodes[parent_id]['layer']
                assert node['lifecycle']['validated_fields']==adoption['adopted_fields']
                for field,digest in adoption['value_sha256'].items():
                    assert value_hash(node['fields'][field])==digest
                if 'principle' in adoption:
                    assert value_hash(adoption['principle'])==adoption['principle_sha256']
                parents=[r for r in model['relations'] if r['type']=='contains' and r['target_id']==node['id']]
                assert len(parents)==1 and parents[0]['source_id']==parent_id
                assert parents[0]['lifecycle']['validated_fields']==['type','source_id','target_id']
                assert not any(r['type']=='contains' and r['source_id']==node['id'] for r in model['relations'])
            for previous in comparison_model['nodes']:
                for field in previous.get('lifecycle',{}).get('validated_fields',[]):
                    assert nodes[previous['id']]['fields'][field]==previous['fields'][field]
        if migration_key=='implementation_U385':
            assert set(migration['delta']['nodes']['changed'])=={'D04.l'}
            assert not migration['delta']['nodes']['removed']
            expected={a['node_id'] for a in migration['adopted_behaviors']}
            assert set(migration['delta']['nodes']['added'])==expected
            assert {r['target_id'] for r in model['relations'] if r['type']=='contains' and r['source_id']=='D04.l'}==expected
            assert nodes['D04.l']['fields']['definition']==migration['adopted_definition']
            assert value_hash(migration['adopted_definition'])==migration['definition_sha256']
            assert nodes['D04.l']['lifecycle']['value_sha256']['definition']==migration['definition_sha256']
            assert nodes['D04.l']['fields']['decomposition_rationale']
            for adoption in migration['adopted_behaviors']:
                node=nodes[adoption['node_id']]
                assert node['kind']=='behavior' and node['layer']==nodes['D04.l']['layer']
                assert node['lifecycle']['validated_fields']==adoption['adopted_fields']
                for field,digest in adoption['value_sha256'].items():
                    assert value_hash(node['fields'][field])==digest
                parents=[r for r in model['relations'] if r['type']=='contains' and r['target_id']==node['id']]
                assert len(parents)==1 and parents[0]['source_id']=='D04.l'
                assert parents[0]['lifecycle']['validated_fields']==['type','source_id','target_id']
                assert not any(r['type']=='contains' and r['source_id']==node['id'] for r in model['relations'])
            relay=next(r for r in model['relations'] if r['id']=='REL-NEEDS-U385-SUPPLIER-RETURN')
            assert (relay['source_id'],relay['target_id'],relay['qualification']['role'])==('BHV052','D04.m','needs')
            assert relay['lifecycle']['validated_fields']==[]
            for previous in comparison_model['nodes']:
                for field in previous.get('lifecycle',{}).get('validated_fields',[]):
                    assert nodes[previous['id']]['fields'][field]==previous['fields'][field]
        if migration_key=='implementation_U384':
            assert not migration['delta']['relations']['added'] and not migration['delta']['relations']['removed']
            previous_relations={r['id']:r for r in comparison_model['relations']}
            for relation in model['relations']:
                previous=previous_relations[relation['id']]
                for field in ['type','source_id','target_id','lifecycle']:
                    assert relation.get(field)==previous.get(field)
                if relation != previous:
                    assert {k:v for k,v in relation['qualification'].items() if k!='scope'}=={k:v for k,v in previous['qualification'].items() if k!='scope'}
            assert not migration['delta']['nodes']['added'] and not migration['delta']['nodes']['removed']
            for ident,name in migration['adopted_names'].items():
                assert nodes[ident]['kind']=='capability'
                assert nodes[ident]['fields']['name']==name
                assert nodes[ident]['lifecycle']['value_sha256']['name']==value_hash(name)
            for previous in comparison_model['nodes']:
                for field in previous.get('lifecycle',{}).get('validated_fields',[]):
                    if field=='name' and previous['id'] in migration['adopted_names']:
                        continue
                    assert nodes[previous['id']]['fields'][field]==previous['fields'][field]
        if migration_key=='implementation_U383':
            assert set(migration['delta']['nodes']['added'])=={'BHV048','BHV049'}
            assert migration['delta']['nodes']['removed']==['D04.p']
            assert 'D04.p' not in nodes
            assert all('D04.p' not in (r['source_id'],r['target_id']) for r in model['relations'])
            assert {r['target_id'] for r in model['relations'] if r['type']=='contains' and r['source_id']=='D04'}==set(migration['domain_children'])
            for ident in migration['restored_capabilities']:
                assert nodes[ident]['kind']=='capability'
                assert [r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']==ident]==['D04']
            for adoption in migration['adopted_strategies']:
                node=nodes[adoption['node_id']]
                assert node['kind']=='behavior' and node['layer']==nodes['D05.i']['layer']
                assert node['lifecycle']['validated_fields']==adoption['adopted_fields']
                for field,digest in adoption['value_sha256'].items():
                    assert value_hash(node['fields'][field])==digest
                assert [r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']==node['id']]==['D05.i']
                assert not any(r['type']=='contains' and r['source_id']==node['id'] for r in model['relations'])
            assert nodes['D05.i']['fields']['decomposition_rationale']
            for previous in comparison_model['nodes']:
                if previous['id'] in nodes:
                    for field in previous.get('lifecycle',{}).get('validated_fields',[]):
                        assert nodes[previous['id']]['fields'][field]==previous['fields'][field]
        if migration_key=='implementation_U380':
            assert set(migration['delta']['nodes']['added'])=={'D05.i'}
            assert set(migration['delta']['nodes']['changed'])=={'D05','D04.l'}
            disposition=nodes['D05.i']
            assert disposition['kind']=='capability' and disposition['fields']['nature']=='decision'
            assert disposition['lifecycle']['validated_fields']==['name','definition','nature']
            for field,digest in migration['value_sha256'].items():
                assert value_hash(disposition['fields'][field])==digest
            parents=[r for r in model['relations'] if r['type']=='contains' and r['target_id']=='D05.i']
            assert len(parents)==1 and parents[0]['source_id']=='D05'
            assert parents[0]['lifecycle']['validated_fields']==['type','source_id','target_id']
            assert not any(r['type']=='contains' and r['source_id']=='D05.i' for r in model['relations'])
            old_nodes={n['id']:n for n in comparison_model['nodes']}
            new_nodes={n['id']:n for n in migrated_model['nodes']}
            for identifier in ('D05','D04.l'):
                for field in old_nodes[identifier]['lifecycle']['validated_fields']:
                    assert new_nodes[identifier]['fields'][field]==old_nodes[identifier]['fields'][field]
            for relation in migrated_model['relations']:
                if relation['id'] in migration['delta']['relations']['added'] and relation['type']=='relates-to':
                    assert relation['lifecycle']['validated_fields']==[]
                    assert relation['qualification']['role']=='needs'
                    assert relation['qualification']['meaning']
        if migration_key=='implementation_U378':
            assert set(migration['delta']['nodes']['added'])=={'D03.o'}
            assert set(migration['delta']['nodes']['changed'])=={'D03'}
            plan=nodes['D03.o']
            assert plan['kind']=='capability' and plan['fields']['nature']=='decision'
            assert plan['lifecycle']['validated_fields']==['name','definition','nature']
            for field,digest in migration['value_sha256'].items():
                assert value_hash(plan['fields'][field])==digest
            assert nodes['D03']['fields']['name']=='Fulfillment Optimization'
            assert not any(r['type']=='contains' and r['source_id']=='D03.o' for r in model['relations'])
            parents=[r for r in model['relations'] if r['type']=='contains' and r['target_id']=='D03.o']
            assert len(parents)==1 and parents[0]['source_id']=='D03'
            assert parents[0]['lifecycle']['validated_fields']==[]
            for relation in migrated_model['relations']:
                if relation['id'] in migration['delta']['relations']['added']:
                    assert relation['lifecycle']['validated_fields']==[]
                    if relation['type']=='relates-to':
                        assert relation['qualification']['role']=='needs'
                        assert relation['qualification']['meaning']
        if migration_key=='implementation_U373':
            assert set(migration['delta']['nodes']['changed'])=={'universe-supply'}
            current=next(n for n in migrated_model['nodes'] if n['id']=='universe-supply')
            previous=next(n for n in comparison_model['nodes'] if n['id']=='universe-supply')
            assert current['fields']['name']=='Supply Chain Orchestration'
            assert {k:v for k,v in current['fields'].items() if k!='name'}=={k:v for k,v in previous['fields'].items() if k!='name'}
            assert current['lifecycle']['validated_fields']==['name']
            assert current['lifecycle']['value_sha256']['name']==value_hash(current['fields']['name'])
        if migration_key=='implementation_U364':
            assert set(migration['delta']['nodes']['changed'])=={'D02.e'}
            expected={entry['node_id'] for entry in migration['adopted_mechanisms']}
            assert {r['target_id'] for r in model['relations'] if r['type']=='contains' and r['source_id']=='D02.e'}==expected
            for entry in migration['adopted_mechanisms']:
                node=nodes[entry['node_id']]
                assert node['kind']=='behavior' and node['layer']==nodes[entry['parent_id']]['layer']
                assert node['lifecycle']['validated_fields']==entry['adopted_fields']
                for field,digest in entry['value_sha256'].items():
                    assert value_hash(node['fields'][field])==digest
                assert value_hash(entry['principle'])==entry['principle_sha256']
                parents=[r for r in model['relations'] if r['type']=='contains' and r['target_id']==entry['node_id']]
                assert len(parents)==1 and parents[0]['source_id']==entry['parent_id']
                assert parents[0]['lifecycle']['validated_fields']==['type','source_id','target_id']
                assert not any(r['type']=='contains' and r['source_id']==entry['node_id'] for r in model['relations'])
            assert nodes['D02.e']['fields']['decomposition_rationale']
        if migration_key=='implementation_U363':
            def children(parent):
                return {r['target_id'] for r in model['relations'] if r['type']=='contains' and r['source_id']==parent}
            assert children('D04')==set(migration['domain_children'])
            assert children(migration['type_parent'])==set(migration['reclassified_types'])
            assert children('D04.o')==set(migration['lifecycle_children'])
            previous={n['id']:n for n in comparison_model['nodes']}
            for identifier in migration['reclassified_types']:
                assert nodes[identifier]['kind']=='behavior'
                assert nodes[identifier]['layer']=='transactional'
                assert nodes[identifier]['fields']['name']==previous[identifier]['fields']['name']
                assert not children(identifier)
            assert not migration['delta']['nodes']['removed']
            assert not migration['delta']['relations']['removed']
        if migration_key=='implementation_U350':
            adoption=migration['adoption']
            node=nodes[adoption['node_id']]
            assert node['lifecycle']['validated_fields']==adoption['adopted_fields']
            for field,digest in adoption['value_sha256'].items():
                assert value_hash(node['fields'][field])==digest
        if migration_key=='implementation_U349':
            stage_nodes={n['id']:n for n in migrated_model['nodes']}
            for adoption in migration['adopted_behaviors']:
                node=stage_nodes[adoption['node_id']]
                assert node['lifecycle']['validated_fields']==adoption['adopted_fields']
                for field,digest in adoption['value_sha256'].items():
                    assert value_hash(node['fields'][field])==digest
                if 'principle' in adoption:
                    assert value_hash(adoption['principle'])==adoption['principle_sha256']
                parents=[r for r in model['relations'] if r['type']=='contains' and r['target_id']==node['id']]
                assert len(parents)==1 and parents[0]['source_id']==adoption['parent_id']
                assert parents[0]['lifecycle']['validated_fields']==['type','source_id','target_id']
            assert nodes['D04.o']['fields']['decomposition_rationale']
        if migration_key=='implementation_U345':
            for entry in migration['principles']:
                assert value_hash(entry['statement'])==entry['statement_sha256']
                assert entry['statement'] in nodes[entry['node_id']]['fields']['scope']
        if migration_key=='implementation_U343':
            for adoption in migration['adopted_behaviors']:
                node=nodes[adoption['node_id']]
                assert node['lifecycle']['validated_fields']==adoption['adopted_fields']
                for field,digest in adoption['value_sha256'].items():
                    assert value_hash(node['fields'][field])==digest
                assert value_hash(adoption['responsibility'])==adoption['responsibility_sha256']
                assert [r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']==node['id']]==[adoption['parent_id']]
            for adoption in migration['adopted_relations']:
                relation=next(r for r in model['relations'] if r['id']==adoption['relation_id'])
                assert relation['lifecycle']['validated_fields']==adoption['adopted_fields']
                for field,digest in adoption['value_sha256'].items():
                    assert value_hash(relation[field])==digest
        if migration_key=='implementation_U342':
            # Validate the U342 proposal at its preserved stage, before U343 adoption.
            stage_nodes={n['id']:n for n in migrated_model['nodes']}
            adoption=migration['capability']
            node=stage_nodes[adoption['node_id']]
            assert node['lifecycle']['validated_fields']==adoption['adopted_fields']
            for field,digest in adoption['value_sha256'].items():
                assert value_hash(node['fields'][field])==digest
            parent_links=[r for r in migrated_model['relations'] if r['type']=='contains' and r['target_id']==node['id']]
            assert len(parent_links)==1 and parent_links[0]['source_id']==migration['proposed_parent_id']
            assert parent_links[0]['lifecycle']['validated_fields']==[]
            for identifier in migration['proposed_behaviors']:
                assert stage_nodes[identifier]['lifecycle']['validated_fields']==[]
                assert stage_nodes[identifier]['review']['state']=='proposed'
                assert [r['source_id'] for r in migrated_model['relations'] if r['type']=='contains' and r['target_id']==identifier]==[node['id']]
        if migration_key=='implementation_U334':
            assert value_hash(migration['adopted_mandate'])==migration['adopted_mandate_sha256']
            assert migration['adopted_mandate'] in nodes['D01.d']['fields']['scope']
        for adoption in (migration.get('behaviors', []) if migration_key != 'implementation_U427' else []):
            node=nodes[adoption['node_id']]
            assert node['lifecycle']['validated_fields']==adoption['adopted_fields']
            for field,digest in adoption['value_sha256'].items():
                assert value_hash(node['fields'][field])==digest
            for field in ['question','particularity']:
                assert value_hash(adoption[field])==adoption[field+'_sha256']
            parents=[r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']==node['id']]
            assert parents==[adoption['parent_id']]
    model=current_model
    nodes={n['id']:n for n in model['nodes']}
    if a.get('market_fields_U330'):
        from copy import deepcopy
        from scripts.lifecycle import value_hash
        enrichment=a['market_fields_U330']
        capture=ROOT/enrichment['model_before']
        assert sha256(capture.read_bytes()).hexdigest()==enrichment['model_before_sha256']
        restored=deepcopy(comparison_model)
        comparison_model=read(capture)
        item=next(n for n in restored['nodes'] if n['id']==enrichment['node_id'])
        previous=next(n for n in comparison_model['nodes'] if n['id']==enrichment['node_id'])
        assert value_hash(item)==enrichment['node_sha256']
        assert item['fields']['market_comparisons'][:len(previous['fields']['market_comparisons'])]==previous['fields']['market_comparisons']
        item['fields']['market_comparisons']=previous['fields']['market_comparisons']
        item['revision']-=1
        assert restored==comparison_model, 'U330 must only enrich D05.a market comparisons.'
    if a.get('implementation_U329'):
        from scripts.lifecycle import value_hash
        migration=a['implementation_U329']
        capture=ROOT/migration['model_before']
        assert sha256(capture.read_bytes()).hexdigest()==migration['model_before_sha256']
        migrated_model=comparison_model
        comparison_model=read(capture)
        for collection in ['nodes','relations']:
            old={x['id']:x for x in comparison_model[collection]}
            new={x['id']:x for x in migrated_model[collection]}
            delta=migration['delta'][collection]
            assert new.keys()==old.keys(), 'U329 must preserve all identities.'
            assert not delta['added'] and not delta['removed']
            assert {i for i in old if old[i]!=new[i]}==set(delta['changed'])
            for identifier,digest in delta['changed'].items():
                assert value_hash(new[identifier])==digest, 'U329 delta changed: '+identifier
        assert {k:v for k,v in migrated_model.items() if k not in ['nodes','relations']}=={k:v for k,v in comparison_model.items() if k not in ['nodes','relations']}
        adoption=migration['adoption']
        item=nodes[adoption['node_id']]
        assert item['lifecycle']['validated_fields']==adoption['validated_fields']
        for field,digest in adoption['value_sha256'].items():
            assert value_hash(item['fields'][field])==digest
            assert item['fields'][field]==adoption['values'][field]
    if a.get('market_fields_U328'):
        from copy import deepcopy
        from scripts.lifecycle import value_hash
        enrichment=a['market_fields_U328']
        capture=ROOT/enrichment['model_before']
        assert sha256(capture.read_bytes()).hexdigest()==enrichment['model_before_sha256']
        restored=deepcopy(comparison_model)
        comparison_model=read(capture)
        item=next(n for n in restored['nodes'] if n['id']==enrichment['node_id'])
        assert value_hash(item)==enrichment['node_sha256']
        assert item['fields'].pop('market_comparisons')
        item['revision']-=1
        assert restored==comparison_model, 'U328 must only enrich the D05.a market comparisons.'
    if a.get('market_fields_U324'):
        from copy import deepcopy
        from scripts.lifecycle import value_hash
        enrichment=a['market_fields_U324']
        capture=ROOT/enrichment['model_before']
        assert sha256(capture.read_bytes()).hexdigest()==enrichment['model_before_sha256']
        restored=deepcopy(comparison_model)
        comparison_model=read(capture)
        item=next(n for n in restored['nodes'] if n['id']==enrichment['node_id'])
        previous=next(n for n in comparison_model['nodes'] if n['id']==enrichment['node_id'])
        assert value_hash(item)==enrichment['node_sha256']
        item['fields']['market_comparisons']=previous['fields']['market_comparisons']
        item['revision']-=1
        assert restored==comparison_model, 'U324 must only clarify market comparisons.'
    if a.get('market_fields_U323'):
        from copy import deepcopy
        from scripts.lifecycle import value_hash
        enrichment=a['market_fields_U323']
        capture=ROOT/enrichment['model_before']
        assert sha256(capture.read_bytes()).hexdigest()==enrichment['model_before_sha256']
        restored=deepcopy(comparison_model)
        comparison_model=read(capture)
        item=next(n for n in restored['nodes'] if n['id']==enrichment['node_id'])
        previous=next(n for n in comparison_model['nodes'] if n['id']==enrichment['node_id'])
        assert value_hash(item)==enrichment['node_sha256']
        assert item['fields']['market_comparisons'][:len(previous['fields']['market_comparisons'])]==previous['fields']['market_comparisons']
        item['fields']['market_comparisons']=previous['fields']['market_comparisons']
        item['revision']-=1
        assert restored==comparison_model, 'U323 must only enrich market comparisons.'
    if a.get('implementation_U318'):
        from scripts.lifecycle import value_hash
        migration=a['implementation_U318']
        capture=ROOT/migration['model_before']
        assert sha256(capture.read_bytes()).hexdigest()==migration['model_before_sha256']
        migrated_model=comparison_model
        comparison_model=read(capture)
        for collection in ['nodes','relations']:
            old={x['id']:x for x in comparison_model[collection]}
            new={x['id']:x for x in migrated_model[collection]}
            delta=migration['delta'][collection]
            assert new.keys()-old.keys()==set(delta['added'])
            assert old.keys()-new.keys()==set(delta['removed'])
            assert {i for i in old.keys()&new.keys() if old[i]!=new[i]}==set(delta['changed'])
            for identifier,digest in {**delta['added'],**delta['changed']}.items():
                assert value_hash(new[identifier])==digest, 'U318 delta changed: '+identifier
        assert {k:v for k,v in migrated_model.items() if k not in ['nodes','relations']}=={k:v for k,v in comparison_model.items() if k not in ['nodes','relations']}
        for adoption in migration['behaviors']:
            node=nodes[adoption['node_id']]
            assert value_hash(adoption['label_fr'])==adoption['label_fr_sha256']
            assert node['lifecycle']['validated_fields']==adoption['adopted_fields']
            for field,digest in adoption['value_sha256'].items():
                assert value_hash(node['fields'][field])==digest
            parents=[r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']==node['id']]
            assert parents==[adoption['parent_id']]
    if a.get('market_fields_U317'):
        from copy import deepcopy
        from scripts.lifecycle import value_hash
        enrichment=a['market_fields_U317']
        capture=ROOT/enrichment['model_before']
        assert sha256(capture.read_bytes()).hexdigest()==enrichment['model_before_sha256']
        restored=deepcopy(comparison_model)
        comparison_model=read(capture)
        item=next(n for n in restored['nodes'] if n['id']==enrichment['node_id'])
        assert value_hash(item)==enrichment['node_sha256']
        assert item['fields'].pop('market_comparisons')
        item['revision']-=1
        assert restored==comparison_model, 'U317 must only document the D05.c comparison.'
    if a.get('implementation_U316'):
        from scripts.lifecycle import value_hash
        migration=a['implementation_U316']
        capture=ROOT/migration['model_before']
        assert sha256(capture.read_bytes()).hexdigest()==migration['model_before_sha256']
        migrated_model=comparison_model
        comparison_model=read(capture)
        for collection in ['nodes','relations']:
            old={x['id']:x for x in comparison_model[collection]}
            new={x['id']:x for x in migrated_model[collection]}
            delta=migration['delta'][collection]
            assert new.keys()-old.keys()==set(delta['added'])
            assert old.keys()-new.keys()==set(delta['removed'])
            assert {i for i in old.keys()&new.keys() if old[i]!=new[i]}==set(delta['changed'])
            for identifier, digest in {**delta['added'],**delta['changed']}.items():
                assert value_hash(new[identifier])==digest, 'U316 delta changed: '+identifier
        assert {k:v for k,v in migrated_model.items() if k not in ['nodes','relations']}=={k:v for k,v in comparison_model.items() if k not in ['nodes','relations']}
    if a.get('market_fields_U311'):
        from copy import deepcopy
        original=read(ROOT/a['market_fields_U311']['model_before'])
        without_comparison=deepcopy(comparison_model)
        assert next(n for n in without_comparison['nodes'] if n['id']=='D05.e')['fields'].pop('market_comparisons')
        assert without_comparison==original, 'U311 must only add documented market comparisons.'
    for p in a['candidates']:
        assert p['parent_id'] in caps and p['status'] in ['proposed','withdrawn_U293','needs_clarification_U293','needs_reassessment_U298','needs_reassessment_U426','covered_by_existing_U425','covered_by_existing_U431','implemented_U318','implemented_U332','implemented_U334','implemented_U402','implemented_U410','implemented_U427']
        assert set(p['needs'])<=caps and set(p['market_sources'])<=set(sources)
        assert p['parent_id'] not in p['needs']
        assert p['differentiating_criterion'] in ['mécanisme','politique','variante','bénéfice ciblé']
        assert all(p[k] for k in ['definition','decomposition_rationale','example','boundary','validation_question'])
    for x in a['assessments']:
        assert set(x['candidate_ids'])<=set(proposals)
        assert all(proposals[i]['parent_id']==x['capability_id'] for i in x['candidate_ids'])
        assert set(x['market_sources'])<=set(sources)
    for x in a['arbitrations']:
        assert set(x['capabilities'])<=caps and set(x['market_sources'])<=set(sources)
    if a.get('current_synthesis_U298'):
        synthesis=a['current_synthesis_U298']
        categories=['retained_candidate_ids','conditional_candidate_ids','reassess_candidate_ids','withdrawn_candidate_ids']
        if 'covered_candidate_ids' in synthesis:
            categories.append('covered_candidate_ids')
            assert all(proposals[i]['status'] in ['covered_by_existing_U425','covered_by_existing_U431'] and proposals[i]['covered_by'] in caps for i in synthesis['covered_candidate_ids'])
        if 'implemented_candidate_ids' in synthesis:
            categories.append('implemented_candidate_ids')
            assert all(proposals[i]['status'] in ['implemented_U318','implemented_U332','implemented_U334','implemented_U402','implemented_U410','implemented_U427'] and proposals[i]['implemented_as'] in behaviors for i in synthesis['implemented_candidate_ids'])
        classified=[i for k in categories for i in synthesis[k]]
        assert len(classified)==len(set(classified)) and set(classified)==set(proposals)
        assert all(proposals[i]['status']=='proposed' for k in categories[:2] for i in synthesis[k])
        assert all(proposals[i]['status'].startswith('needs_') for i in synthesis['reassess_candidate_ids'])
        assert all(proposals[i]['status'].startswith('withdrawn') for i in synthesis['withdrawn_candidate_ids'])
    if a.get('adopted_corrections_U299'):
        from scripts.lifecycle import value_hash
        for correction in a['adopted_corrections_U299']['corrections']:
            assert correction['candidate_id'] in ['P04','P10']
            assert correction['validated_fields']==['rule']
            assert correction['value_sha256']['rule']==value_hash(correction['rule'])
    valid_refs=set(proposals)|{x['id'] for x in a['arbitrations']}
    assert all(set(x['tests'])<=valid_refs for x in a['scenarios'])
    for x in a['existing_behavior_review']:
        assert set(x['market_sources'])<=set(sources)
    relations={r['id']:r for r in model['relations']}
    for c in a['contracts']:
        # Qualified business dependencies can target a specific terminal behavior.
        assert c['consumer'] in caps|behaviors and c['provider'] in caps|behaviors
        for i in c['existing_needs_relation_ids']:
            r=relations[i]
            assert (r['source_id'],r['target_id'])==(c['consumer'],c['provider'])
            assert r.get('qualification',{}).get('role')=='needs'
    protected=json.loads((ROOT/'audits/2026-09-17-refonte-appliquee/protected.json').read_text(encoding='utf-8'))
    assert all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in protected.items()), 'Published evidence changed.'
    OUT.mkdir(parents=True,exist_ok=True)
    def write(name, lines):
        if a.get('feedback_U324') and name != 'sources.md':
            lines=lines[:1]+['','**Réexamen U324 / C98 :** les min/max peuvent dépendre des besoins et varier par période. Coverage Target Decision détermine les valeurs ; Supply Protection gouverne leur application ; Replenishment Decision détermine les apports. La création des comportements proposés U323 est suspendue faute de bénéfice différenciant établi. [Comparaison CMP111](../../marche/comparaisons.md#cmp111).']+lines[1:]
        elif a.get('feedback_U323') and name != 'sources.md':
            lines=lines[:1]+['','**Discussion U323, proposée :** deux politiques de réassort, par besoins datés et par seuil/cible. Les ajustements d’apports existants resteraient dans leurs descriptions, sans comportement autonome à ce stade. [Comparaison Microsoft CMP110](../../marche/comparaisons.md#cmp110). Aucun nouveau comportement adopté.']+lines[1:]
        if a.get('implementation_U318'):
            if name != 'sources.md':
                lines=lines[:1]+['','**État courant U318 :** deux comportements intégrés sous Stock Redistribution Decision : rééquilibrage entre sites (BHV024) et consolidation des stocks dispersés (BHV025), dont assortiments de tailles et reliquats. Définitions françaises et rattachements adoptés ; noms anglais éditoriaux. Catalogue : 40 capacités, 16 comportements. [Portée de l’accord](../2026-09-18-redistribution-behaviors/README.md). P01–P03 sur le réassort restent ouverts. Les textes datés ci-dessous conservent leur portée historique.']+lines[1:]
            if a.get('implementation_U332') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U332 :** Inventory Target Decision porte trois comportements frères : Store Inventory Optimization (BHV026), Distribution Center Inventory Optimization (BHV027) et Multi-Echelon Inventory Optimization (BHV028). P13 est intégré ; P12 reste sans création recommandée. Catalogue : 40 capacités et 19 comportements. Les sections datées ci-dessous conservent leurs états historiques. [Portée de la validation](../2026-09-18-inventory-target-behaviors/README.md).']+lines[1:]
            if a.get('implementation_U334') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U334 :** Stocktaking porte politique et demandes de vérification, ainsi que Periodic Physical Inventory (BHV029), Cycle Counting (BHV030) et Spot Counting (BHV031). P08/P09 intégrés ; traitement des écarts commun et réalisation physique par les exécutants. Catalogue : 40 capacités, 22 comportements. Les sections datées conservent leurs états historiques. [Portée de la validation](../2026-09-18-stocktaking-behaviors/README.md).']+lines[1:]
            if a.get('implementation_U342') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U342 :** Reservation Policy Decision (D05.h), nom et définition adoptés. Quatre comportements BHV032–BHV035 documentés et proposés ; parent D05 proposé. Catalogue : 41 capacités et 26 comportements, dont ces quatre nouvelles propositions. [Recensement et frontières](../2026-09-18-reservation-policy/README.md). A01 reste ouvert au-delà de cette décision.']+lines[1:]
            if a.get('implementation_U343') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U343 :** les quatre comportements BHV032–BHV035 et le parent D05 sont adoptés, dans la portée des noms et responsabilités présentées. Modalités détaillées, contrats et comparaisons restent proposés. Les mentions U342 ci-dessous décrivent l’état antérieur. [Portée de validation](../2026-09-18-reservation-policy-adoption/README.md).']+lines[1:]
            if a.get('implementation_U345') and name != 'sources.md':
                lines=lines[:1]+['','**Clarification U345 / C99 :** Supply Assignment porte l’application des affectations d’un plan ; D04 garde ses effets sur les Orders. Trois mécanismes documentés en proposition dans `modeles/backlog/supply-assignment-mechanisms-review.yaml`. Simulation & Analysis explicite les recommandations ; compensation logicielle hors de cette décomposition métier. Aucun nouveau nœud.']+lines[1:]
            if a.get('implementation_U349') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U349 :** Order Lifecycle Management porte Order Firming (BHV036) et la protection contre les réoptimisations (BHV037, nom éditorial Order Freezing). Affermissement, gel et mise en attente sont distincts. Accord et limites dans `modeles/backlog/order-lifecycle-behaviors.yaml` ; P11 reste ouvert. Catalogue : 41 capacités et 28 comportements.']+lines[1:]
            if a.get('implementation_U350') and name != 'sources.md':
                lines=lines[:1]+['','**Validation U350 :** Order Freezing est le nom adopté pour BHV037. Le principe et le parent U349 sont conservés ; les détails et contrats restent proposés.']+lines[1:]
            if a.get('implementation_U363') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U363 :** D04 comporte Order Type (cinq variantes), Order Lifecycle Management (neuf comportements), Order Structuring et Order Archiving. Split est une mutation avec filiation ; Spread concerne l’affectation des ressources entre Orders. Les états datés ci-dessous sont historiques. [Refonte et portée](../2026-09-18-d04-U363/README.md).']+lines[1:]
            if a.get('implementation_U364') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U364 :** Supply Assignment porte application d’un plan, complément préservant les affectations et réaffectation des liens modifiables (BHV045–BHV047). La distinction stabilité/adaptation est adoptée ; les décisions spécialisées et Freezing gardent leurs responsabilités. A01/A02 restent ouverts. [Portée et comparaison](../2026-09-18-supply-assignment-U364/README.md).']+lines[1:]
            if a.get('implementation_U378') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U378 :** Fulfillment Plan Decision (D03.o) produit le scénario collectif ; D03 porte le nom adopté Fulfillment Optimization. A02 est résolue sur la responsabilité ; les contrats détaillés restent proposés. Aucun sous-niveau ou comportement ajouté. Les états U364 et antérieurs ci-dessous sont historiques. [Accord et intégration](../2026-09-18-fulfillment-plan-U378/README.md).']+lines[1:]
            if a.get('implementation_U380') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U380 :** Return Disposition Decision (D05.i) est adoptée sous Inventory Optimization, sans comportement. A04 est résolue sur le devenir logistique du bien ; autorisation commerciale, remboursement et remplacement client restent distincts. [Accord et intégration](../2026-09-18-return-disposition-U380/README.md).']+lines[1:]
            if a.get('implementation_U383') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U383 :** cinq capacités par type d’Order sont rétablies sous D04 ; Order Type D04.p est retiré. Lifecycle, Structuring et Archiving restent transverses. Return Disposition Decision porte Policy-based Disposition et Value Recovery Optimization (BHV048–049). Les prises en charge des retours restent à détailler. Les états datés ci-dessous sont historiques. [Portée et comparaison](../2026-09-18-orders-disposition-U383/README.md).']+lines[1:]
            if a.get('implementation_U384') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U384 :** noms courts Sales Order, Purchase Order, Transfer Order, Customer Return et Supplier Return adoptés. Cinq parcours Customer Return détaillés en proposition dans `modeles/backlog/customer-return-behaviors.yaml`, sans ajout au catalogue à ce stade. [Nommage et étude](../2026-09-18-customer-return-U384/README.md).']+lines[1:]
            if a.get('implementation_U385') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U385 :** définition élargie de Customer Return et cinq parcours combinables adoptés : Return to Stock, Repair and Refurbishment, Return to Supplier, Return to Customer et Scrapping (BHV050–054). Les axes commerciaux et les autres filières restent à instruire. [Accord et intégration](../2026-09-18-customer-return-U385/README.md).']+lines[1:]
            if a.get('implementation_U387') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U387 :** Supplier Return porte Return for Credit et Return for Replacement (BHV055–056), distingués par l’apport de remplacement attendu. Finance, achat et exécution restent distincts. [Accord et intégration](../2026-09-18-supplier-return-U387/README.md).']+lines[1:]
            if a.get('implementation_U388') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U388 :** Return for Repair (BHV057) complète Supplier Return : restitution attendue du même bien réparé, distincte du remplacement. L’ajout n’est plus conditionnel ; achats de prestation et exécution conservent leurs responsabilités. [Portée de l’ajout](../2026-09-18-supplier-repair-U388/README.md).']+lines[1:]
            if a.get('implementation_U391') and name != 'sources.md':
                lines=lines[:1]+['','**État courant U391 :** Purchase Order porte Stock Procurement, Direct Delivery et Service Procurement (BHV058–060). Consignation instruite séparément dans la gestion du stock. [Accord et intégration](../2026-09-18-purchase-order-U391/README.md).']+lines[1:]
            if a.get('implementation_U402') and name != 'sources.md':
                lines=lines[:1]+['',f'**État courant U402 :** {len(caps)} capacités et {len(behaviors)} comportements. Les trois mécanismes CTP BHV075–077 sont intégrés : ressources supplémentaires, alternatives de satisfaction et réexamen d’engagements. P14–P16 ne sont plus conditionnels ; A05 est résolu sur la frontière de catalogue, les règles détaillées restant distinctes. Fulfillment Plan Decision conserve le choix collectif. [Portée et comparaison](../../modeles/backlog/d03-review.yaml). Les états datés ci-dessous conservent leur valeur historique.']+lines[1:]
            if a.get('implementation_U403') and name != 'sources.md':
                lines=lines[:1]+['',f'**État courant U403 :** {len(caps)} capacités et {len(behaviors)} comportements. Supplier Confirmation (BHV078) complète Purchase Order et résout A06 sur le catalogue : demande, réponse fournisseur et engagement accepté distincts ; impacts, mutations et promesse client gardent leurs responsables. Refuser un report ne supprime pas le risque annoncé. [Explication et comparaison](../../modeles/backlog/purchase-order-behaviors.yaml). Les mentions antérieures d’un point A06 ouvert restent historiques.']+lines[1:]
            if a.get('implementation_U406') and name != 'sources.md':
                lines=lines[:1]+['',f'**État courant U406 :** {len(caps)} capacités et {len(behaviors)} comportements. Warehouse Visibility, Transportation Visibility, Store Visibility et Business Process Tracking intégrés sous Execution Tracking (BHV079–082). Tasks et appels sont des objets suivis, pas des niveaux de comportement. Digital Service Visibility est remplacé ; le besoin numérique demeure couvert. [Portées et comparaison](../../modeles/backlog/execution-services-review.yaml). Les propositions et mentions de non-intégration ci-dessous sont historiques.']+lines[1:]
            if a.get('implementation_U409') and name != 'sources.md':
                lines=lines[:1]+['', '**État courant U409 :** le Process orchestre des Services. D06 devient Process Management ; Process Orchestration et Process Adaptation Decision restent distincts. Operations Tracking porte les trois visibilités physiques et Process Tracking. Neuf noms adoptés ; Service Catalog Ingestion et Service Reconciliation sont deux intitulés dérivés proposés. Aucun ajout de comportement ni changement de responsabilité. Les intitulés des états datés ci-dessous restent historiques. [Convention et comparaison](../../modeles/backlog/execution-services-review.yaml).']+lines[1:]
            if a.get('implementation_U410') and name != 'sources.md':
                lines=lines[:1]+['', '**État courant U410 :** P11 est résolu par enrichissement d’Order Release (BHV039) : conditions individuelles et collectives, complétude, éléments indispensables et traitement partiel. Aucun comportement ajouté ; autorisation distincte de l’affectation et de Process Orchestration. Autoriser ensemble ne signifie pas démarrer simultanément. Les mentions antérieures de P11 ouvert sont historiques. [Accord et comparaison](../../modeles/backlog/order-lifecycle-behaviors.yaml).']+lines[1:]
            if a.get('implementation_U413') and name != 'sources.md':
                lines=lines[:1]+['', '**État courant U413 :** D03 devient Order Backlog Management. Le travail collectif du carnet prépare son engagement vers les processus, en mobilisant les décisions spécialisées. D04 conserve la demande par intention. Réexamen ciblé de Lifecycle/Structuring : parents inchangés, aucune nouvelle capacité ou comportement. P11 demeure intégré à Order Release ; son placement côté carnet reste à concrétiser. [Mandat, comparaison et réexamen](../../modeles/backlog/order-backlog-review.yaml). Les noms et positions des états précédents sont historiques.']+lines[1:]
            if a.get('implementation_U414') and name != 'sources.md':
                lines=lines[:1]+['', '**État courant U414 :** Order Backlog Planning (D03.p) est créé dans D03. Order Release BHV039 y est déplacé, identité et définition conservées. Lifecycle conserve huit comportements ; Split et Structuring restent en D04 pour le prochain arbitrage. Planning mobilise les décisions et prépare la prise en charge ; affectation, promesse et orchestration gardent leurs responsabilités. Aucun comportement supplémentaire : 47 capacités et 73 comportements. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml). Les anciens rattachements ci-dessous restent historiques.']+lines[1:]
            if a.get('implementation_U417') and name != 'sources.md':
                lines=lines[:1]+['', '**État courant U417/U418 :** dans D03 Order Backlog Management, Structuring porte Order Splitting et Lifecycle porte Order Release. Les capacités D04.n/D04.o conservent leurs identifiants historiques. Planning prépare les scénarios ; Lifecycle autorise ; Process Orchestration coordonne les services. Gel et suspension sont combinables, sans séquence universelle. Aucun ajout de nœud ou comportement ; arbitrage de placement du carnet résolu. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml). Les anciens rattachements ci-dessous sont historiques.']+lines[1:]
            if a.get('implementation_U420') and name != 'sources.md':
                lines=lines[:1]+['', '**État courant U420 :** Order Archiving appartient à D03 ; Order Lifecycle Management appartient à D04, avec Order Release. Structuring et Split restent dans D03. Identifiants, définitions et parents des comportements conservés. Les mentions U417/U418 ci-dessous sont historiques et remplacées sur ces rattachements. [Portées et comparaison](../../modeles/backlog/order-backlog-review.yaml).']+lines[1:]
            if a.get('implementation_U424') and name != 'sources.md':
                lines=lines[:1]+['', '**État courant U424 :** Lifecycle unique en D04 avec six dimensions et leurs états explicites. Rescheduling BHV041 est intégré à Preparation & Revision BHV038 ; Cancellation BHV042 est intégré à Termination BHV043, avec distinction entre annulation et clôture. Les anciens identifiants sont conservés dans les preuves et ne sont pas réutilisés. D03 mobilise Lifecycle ; D06 garde orchestration et réalisations. Nouvelles formulations et listes détaillées éditoriales. Les décompositions antérieures ci-dessous sont historiques.']+lines[1:]
            if a.get('replenishment_reassessment_U426') and not a.get('implementation_U427') and name != 'sources.md':
                lines=lines[:1]+['', '**Réexamen courant U426 :** les descriptions de Replenishment Decision ont été enrichies U425. P01–P03 sont réouverts suite à la question de Laurent : politiques selon besoins datés / cible et ajustement des apports comme comportements possibles. Aucun nouveau nœud appliqué. Leur clôture U425 n’est plus le statut courant.']+lines[1:]
            if a.get('implementation_U427') and name != 'sources.md':
                lines=lines[:1]+['', '**État courant U427 :** Replenishment Decision porte Requirement-based Replenishment (BHV083), Target-based Replenishment (BHV084) et Replenishment Adjustment (BHV085). Deux politiques et un mécanisme combinable ; noms, définitions présentées et rattachements adoptés. Exemples, justifications et comparaison Microsoft documentés avec leur portée éditoriale. P01–P03 sont intégrés : le point réassort est clos. Les autres arbitrages de l’audit restent distincts ; les conclusions antérieures de non-décomposition et de réouverture ci-dessous sont historiques.']+lines[1:]
            if a.get('closure_U431') and name != 'sources.md':
                lines=lines[:1]+['', '**Audit clos U431.** Tous les candidats sont intégrés, couverts par l’existant ou retirés. P04/P10/P12 ne créent aucun comportement supplémentaire. Frontière commerciale et financière externe à Supply ; règles et contrats détaillés conservés comme travaux ultérieurs non bloquants. [Bilan de clôture](cloture-U431.md). Les états et propositions antérieurs ci-dessous conservent leur portée historique.']+lines[1:]
            write_text_if_changed(OUT/name, '\n'.join(lines)+'\n')
            return
        if a.get('feedback_U317') and name != 'sources.md':
            lines=lines[:1]+['','**Discussion U317 :** réexaminer Stock Redistribution Decision, le rééquilibrage et la consolidation intersites, notamment les tailles dispersées. [Comparaison CMP109](../../marche/comparaisons.md#cmp109). Aucun comportement nouveau adopté ; P01–P03 sur le réassort restent ouverts.']+lines[1:]
        if a.get('implementation_U316'):
            if name != 'sources.md':
                lines=lines[:1]+['','**État courant U316 :** Initial Stocking Decision (D05.g) porte l’implantation ; Replenishment Decision (D05.e) porte le réassort continu. Le nom et la définition présentés d’Initial Stocking Decision sont adoptés ; relations détaillées et correspondances marché restent proposées. Catalogue : 40 capacités, 14 comportements. [Portée et intégration](../2026-09-18-initial-stocking/README.md). Les textes datés ci-dessous conservent leur portée historique.']+lines[1:]
            write_text_if_changed(OUT/name, '\n'.join(lines)+'\n')
            return
        if a.get('feedback_U313'):
            if name != 'sources.md':
                lines=lines[:1]+['','**Discussion courante U313 :** deux décisions distinctes sont demandées pour l’implantation et le réassort continu. La proposition U310 de deux comportements sous Replenishment Decision est retirée ; les noms anglais et frontières détaillées restent à instruire. [Comparaison marché CMP107](../../marche/comparaisons.md#cmp107). Les textes datés ci-dessous conservent leur portée historique.']+lines[1:]
            write_text_if_changed(OUT/name, '\n'.join(lines)+'\n')
            return
        if a.get('feedback_U310'):
            if name not in ['sources.md','feedback-U310.md']:
                lines=lines[:1]+['','**Discussion courante U310 :** implantation initiale et réassort continu sont les politiques métier décrites par Laurent. P01/P02/P03 sont à réexaminer à cette lumière. [Comparaison et frontières](feedback-U310.md). Store Visibility reste le nom adopté U308 ; les textes datés conservent leurs formulations historiques.']+lines[1:]
            write_text_if_changed(OUT/name, '\n'.join(lines)+'\n')
            return
        if a.get('adoption_U308'):
            if name not in ['sources.md','validation-U308.md']:
                lines=lines[:1]+['','**Nom courant U308 : Store Visibility**, même périmètre et parent que Store Execution Visibility adopté U305. Warehouse Visibility et Transportation Visibility restent adoptés ; Digital Service Visibility reste proposé U306. [Accord de nommage](validation-U308.md). Les formulations datées ci-dessous sont historiques.']+lines[1:]
            write_text_if_changed(OUT/name, '\n'.join(lines)+'\n')
            return
        if a.get('feedback_U306'):
            if name not in ['sources.md','feedback-U306.md']:
                lines=lines[:1]+['','**Discussion courante U306 :** les trois comportements logistiques sont adoptés U305. La visibilité des prestations numériques est un besoin explicite ; Digital Service Visibility est proposé en complément. [Besoin, périmètre et marché](feedback-U306.md). Les textes datés gardent leur portée historique.']+lines[1:]
            write_text_if_changed(OUT/name, '\n'.join(lines)+'\n')
            return
        if a.get('adoption_U305'):
            if name not in ['sources.md','validation-U305.md']:
                lines=lines[:1]+['','**Arbitrage courant U305 :** Warehouse Visibility, Transportation Visibility et Store Execution Visibility adoptés directement sous Execution Tracking. Logistics Visibility demeure englobant. [Portée de l’accord](validation-U305.md). Les propositions datées ci-dessous conservent leur formulation historique.']+lines[1:]
            write_text_if_changed(OUT/name, '\n'.join(lines)+'\n')
            return
        if a.get('feedback_U304'):
            if name not in ['sources.md','feedback-U304.md']:
                lines=lines[:1]+['','**Discussion courante U304 :** Execution Tracking couvre les opérations numériques et physiques (U301/U302). La granularité de Logistics Visibility est réouverte : spécialisations entrepôt, transport et opérations magasin proposées. [Périmètre et comparaison](feedback-U304.md). Les arbitrages antérieurs de niveau restent historiques.']+lines[1:]
            write_text_if_changed(OUT/name, '\n'.join(lines)+'\n')
            return
        if a.get('current_synthesis_U298'):
            if name not in ['sources.md','rapport.md']:
                lines=lines[:1]+['','**Synthèse courante U298 :** Logistics Visibility est le nom adopté ; sept candidats à instruire, cinq conditionnels, P04/P10/P11 à réexaminer, P05 retiré. [Résultat consolidé](rapport.md). Les feedbacks datés conservent l’historique.']+lines[1:]
            write_text_if_changed(OUT/name, '\n'.join(lines)+'\n')
            return
        revisions=[
            ('U297','Le nom Logistics Visibility est adopté pour le parcours physique U296. Le niveau et le rattachement restent proposés ; les recommandations de noms antérieures sont remplacées.'),
            ('U296','Logistics Visibility est recommandé pour le parcours physique complet, du picking au point final. Les noms proposés antérieurement restent historiques ; aucun renommage adopté.'),
            ('U295','Inventory Visibility est conservé ; Transportation Visibility est recommandé pour le périmètre d’acheminement discuté. Aucun nom adopté.'),
            ('U294','Track and Trace remplace la proposition de nom Transit Visibility ; aucun nom adopté.'),
            ('U293','P05 retiré ; P11 à clarifier ; visibilité du transit à rendre explicite.')]
        for revision,summary in revisions:
            if a.get('feedback_'+revision):
                if name not in ['sources.md','feedback-'+revision+'.md']:
                    lines=lines[:1]+['',f'**Discussion courante {revision} :** {summary} [Comparaison et périmètre](feedback-{revision}.md).']+lines[1:]
                break
        write_text_if_changed(OUT/name, '\n'.join(lines)+'\n')
    def refs(ids):
        return ', '.join(f"[{i} — {sources[i]['vendor']}]({sources[i]['url']})" for i in ids) or 'Comparaison directe non établie ; raisonnement sur le modèle FLOW.'
    def cap(i):
        return i+' '+nodes[i]['fields']['name']

    if a.get('feedback_U310'):
        f=a['feedback_U310']
        assert set(f['market_sources'])<=set(sources)
        write('feedback-U310.md',['# Implantation et réassort — U310','',f['conclusion'],'','**Pourquoi revoir la proposition.** '+f['reason'],'','**Existant et cible.** '+f['current_context'],'','**Marché.** '+f['market'],'',refs(f['market_sources']),'','**Frontières.** '+f['boundary'],'','**Conséquence pour l’audit.** '+f['audit_impact'],'','Termes ajoutés au glossaire métier ; aucun nouveau nœud de capacité ou comportement.'])

    if a.get('adoption_U308'):
        from scripts.lifecycle import value_hash
        f=a['adoption_U308']
        v=f['values']
        assert v['parent_id'] in caps
        assert set(f['validated_fields'])==set(v)
        assert all(f['value_sha256'][k]==value_hash(v[k]) for k in v)
        previous=next(b for b in a['adoption_U305']['values']['behaviors'] if b['name']==v['previous_name'])
        assert v['scope']==previous['scope']
        assert [b['name'] for b in a['current_visibility_names']]==['Warehouse Visibility','Transportation Visibility','Store Visibility']
        write('validation-U308.md',['# Store Visibility — nom adopté U308','','**Nom courant :** '+v['name']+'. Ancien nom : '+v['previous_name']+'.','','**Périmètre conservé.** '+v['scope'],'','Parent : **Execution Tracking**. Niveau : comportement.','',f['reason'],'','**Justification marché / modèle.** '+f['market_comparison'],'',f['implementation_status']])

    if a.get('feedback_U306'):
        from scripts.lifecycle import value_hash
        f=a['feedback_U306']
        assert f['parent_id'] in caps and set(f['market_sources'])<=set(sources)
        assert f['requirement_sha256']==value_hash(f['user_requirement'])
        write('feedback-U306.md',['# Digital Service Visibility — proposition U306','','**Besoin exprimé.** '+f['user_requirement'],'','**Définition proposée.** '+f['definition'],'','**Périmètre.** '+f['scope'],'','**Bénéfice de décomposition.** '+f['rationale'],'','**Exemple.** '+f['example'],'','**Frontières.** '+f['boundary'],'','**Marché.** '+f['market_comparison'],'',refs(f['market_sources']),'','**Portée.** '+f['validation_scope'],'','Catalogue et publications inchangés.'])

    if a.get('adoption_U305'):
        from scripts.lifecycle import value_hash
        adoption=a['adoption_U305']
        v=adoption['values']
        assert v['parent_id'] in caps
        assert set(adoption['validated_fields'])==set(v)
        assert all(adoption['value_sha256'][k]==value_hash(v[k]) for k in v)
        rows=['# Visibilité logistique — accord U305','',adoption['scope'],'','Parent : **'+v['parent_name']+'**. Niveau : comportement.','','| Comportement adopté | Périmètre adopté |','| --- | --- |']
        rows += ['| '+b['name']+' | '+b['scope']+' |' for b in v['behaviors']]
        rows += ['','Logistics Visibility : '+v['logistics_visibility_role'],'','**Bénéfice magasin.** '+v['store_benefit'],'',adoption['implementation_status'],'','Aucune release.']
        write('validation-U305.md',rows)

    if a.get('feedback_U304'):
        from scripts.lifecycle import value_hash
        rule=a['tracking_scope_U301']
        assert rule['value_sha256']['rule']==value_hash(rule['rule'])
        f=a['feedback_U304']
        assert set(f['market_sources'])<=set(sources)
        write('feedback-U304.md', ['# Visibilité des opérations magasin — U304','',f['conclusion'],'','**Périmètre.** '+f['scope'],'','**Bénéfice de décomposition.** '+f['rationale'],'','**Proposition courante.** '+f['recommendation'],'','**Limites.** '+f['limits'],'',refs(f['market_sources']),'','Le mandat de traçabilité numérique et physique U301/U302 reste acquis. La décomposition reste proposée ; aucun changement du catalogue ni publication.'])

    if a.get('positioning_U300'):
        f=a['positioning_U300']
        assert f['parent_id'] in caps and f['kind']=='behavior'
        assert nodes[f['domain_id']]['kind'] in ('domain', 'area')
        assert set(f['market_sources'])<=set(sources)
        rows=['# Positionnement proposé de Logistics Visibility — U300','',f['recommendation'],'','**Définition proposée.** '+f['definition'],'','**Pourquoi décomposer.** '+f['decomposition_rationale'],'','**Cohérence FLOW.** '+f['model_justification'],'','**Marché.** '+f['market_justification'],'',refs(f['market_sources']),'','## Alternatives','']
        for x in f['alternatives']:
            rows += ['- **'+x['option']+'** : '+x['assessment']]
        rows += ['','## Frontières','','| Responsabilité | Résultat |','| --- | --- |']
        for x in f['boundaries']:
            rows += ['| '+x['capability']+' | '+x['role']+' |']
        rows += ['','**Exemple.** '+f['example'],'','**Arbitrage.** '+f['decision_to_validate'],'','**Déjà établi.** '+f['not_to_revalidate'],'',f['implementation_scope']]
        write('positionnement-U300.md',rows)

    if a.get('feedback_U297'):
        from scripts.lifecycle import value_hash
        f=a['feedback_U297']
        assert f['validated_fields']==['name']
        assert f['value_sha256']['name']==value_hash(f['name'])
        write('feedback-U297.md',['# Logistics Visibility — nom validé','',f['scope'],'',f['validation_boundary'],'','**Définition éditoriale proposée.** '+f['proposed_definition'],'',f['distinction'],'','Validation : U297 ; comparaison marché : CMP102. Catalogue et publications inchangés.'])

    if a.get('feedback_U296'):
        f=a['feedback_U296']
        assert set(f['market_sources'])<=set(sources)
        write('feedback-U296.md',['# Logistics Visibility — du picking au point final','',f['requested_scope'],'',f['recommendation'],'','**Définition proposée.** '+f['proposed_definition'],'',f['comparison'],'',f['boundaries'],'','**Cas d’épreuve.** '+f['verification'],'',f['decision_scope'],'','Sources : '+refs(f['market_sources'])])

    if a.get('feedback_U295'):
        f=a['feedback_U295']
        assert set(f['market_sources'])<=set(sources)
        write('feedback-U295.md',['# Inventory Visibility et visibilité du transport','',f['verified'],'',f['conclusion'],'',f['recommendation'],'',f['scope'],'',f['boundary'],'','Sources : '+refs(f['market_sources'])])

    if a.get('feedback_U294'):
        f=a['feedback_U294']
        assert set(f['market_sources'])<=set(sources)
        write('feedback-U294.md',['# Track and Trace — alignement du nom sur le marché','',f['rule'],'',f['evidence'],'',f['recommendation'],'','**Définition proposée.** '+f['proposed_definition'],'',f['scope'],'',f['modeling_limit'],'','**Sources.** '+refs(f['market_sources']),'','**Limite d’accès.** '+f['access_limit']])

    if a.get('feedback_U293'):
        f=a['feedback_U293']
        rows=['# Feedback U293 — clarification de l’audit','',f['scope'],'',f['current_summary'],'']
        for x in f['points']:
            rows += ['## '+x['topic'],'',x['conclusion'],'','**Proposition.** '+x['proposal'],'','**Frontières.** '+x['boundary'],'','**Comparaison marché.** '+refs(x['market_sources']),'']
        write('feedback-U293.md',rows)

    rows=['# Sources primaires — audit U292','',
        'Consultation : 17 septembre 2026. Les faits documentés sont séparés des recommandations FLOW. Les pages produit ne valent pas spécifications de couverture. Aucun déploiement Beaumanoir démontré. Synthèses sélectives ; aucune reproduction substantielle.', '']
    for s in a['sources']:
        rows += [f"## {s['id']} — {s['vendor']} — {s['native_label']}",'',
            f"[Source primaire]({s['url']}) — {s['edition']}.",'',
            f"Nature : {s['nature']}. Accès : {s['access']}. Passage : {s['locator']}.",'',
            '**Constat documentaire.** '+s['observed_fact'],'', '**Limites.** '+s['limits'],'']
    write('sources.md',rows)

    rows=[f'# Revue des {len(caps)} capacités et des {len(behaviors)} comportements','',
        'Revue exhaustive du catalogue FLOW au périmètre capturé ; profondeur documentaire marché variable et explicitée. Une absence de comportement n’est pas une absence de couverture. Le verdict porte sur la lisibilité du modèle, pas sur la couverture d’un SI installé.', '',
        '| Capacité | Verdict | Comportements existants | Candidats proposés |', '| --- | --- | --- | --- |']
    for x in a['assessments']:
        rows.append(f"| {cap(x['capability_id'])} | {x['verdict']} | {', '.join(x['existing_behaviors']) or '—'} | {', '.join(x['candidate_ids']) or '—'} |")
    for x in a['assessments']:
        rows += ['',f"## {cap(x['capability_id'])}",'', '**Diagnostic.** '+x['diagnosis'],'',
                 '**Proposition.** '+x['recommendation'],'', '**Appuis.** '+refs(x['market_sources'])]
    rows += ['', '## Réexamen des comportements existants','',
             'Aucun remplacement proposé. Les précisions ci-dessous restent éditoriales et à valider ; elles ne réécrivent pas les accords antérieurs.','',
             '| Comportement | Précision utile | Appui |','| --- | --- | --- |']
    for x in a['existing_behavior_review']:
        rows.append(f"| {x['behavior_id']} {nodes[x['behavior_id']]['fields']['name']} | {x['recommendation']} | {refs(x['market_sources'])} |")
    write('capacites.md',rows)

    rows=['# Suivi des mécanismes candidats et des intégrations','',
        'Les fiches conservent les formulations initiales pour traçabilité. Leur statut courant et leur note de réexamen indiquent les intégrations et les propositions restantes ; les identifiants P ne sont pas des BHV. Une intégration ne valide pas par extension les anciens contrats ou dépendances proposés.', '']
    if a.get('current_synthesis_U298'):
        rows += ['**Statuts courants.** '+', '.join(f"{status} : {count}" for status,count in Counter(p['status'] for p in a['candidates']).items())+'.','']
    for p in a['candidates']:
        rows += [f"## {p['id']} — {p['name']}",'',f"Parent initialement proposé : **{cap(p['parent_id'])}**. Priorité initiale : {p['priority']}. Statut courant : **{p['status']}**. {p.get('review_note','')}",'',
            '**Résultat.** '+p['definition'],'', f"**Critère : {p['differentiating_criterion']}.** {p['decomposition_rationale']}",'',
            '**Cas fictif.** '+p['example'],'','**Frontières et non-doublon.** '+p['boundary'],'',
            '**Appuis marché.** '+refs(p['market_sources']),'', '**A besoin de.** '+', '.join(cap(i) for i in p['needs'])+'.','',
            '**Arbitrage.** '+p['validation_question'],'']
    write('propositions.md',rows)

    rows=['# Frontières, contrats et cas d’épreuve','',
        'Ajouter un comportement ne résout pas une responsabilité absente, deux résultats confondus ou un contrat de données incomplet. Les arbitrages suivants précèdent les décompositions concernées.', '']
    for x in a['arbitrations']:
        rows += [f"## {x['id']} — {x['title']}",'', x['question'],'', '**Proposition.** '+x['recommendation'],'',
            '**Limite.** '+x['limit'],'', '**Capacités.** '+', '.join(cap(i) for i in x['capabilities'])+'.','',
            '**Marché.** '+refs(x['market_sources']),'']
    rows += ['## Contrats entre capacités à éprouver','',
        'Ces contrats ne constituent pas une nouvelle architecture d’intégration. Le catalogue possède déjà des relations ; une flèche ne suffit pas à prouver la sémantique du résultat échangé.', '',
        '| Consommateur | Fournisseur / contrat attendu | Invariant proposé | Traçabilité |','| --- | --- | --- | --- |']
    for c in a['contracts']:
        trace=', '.join(c['existing_needs_relation_ids']) or 'Lien non établi ; à instruire'
        rows.append(f"| {c['consumer']} | {c['provider']} : {c['result']} | {c['invariant']} | {trace} |")
    rows += ['', '## Cas fictifs de validation','',
        'Ces exemples servent à discuter le modèle ; ils ne sont pas des faits observés chez GBM, Boardriders ou Sarenza. Sarenza demeure non évalué.', '']
    for x in a['scenarios']:
        rows += [f"### {x['id']} — {x['title']}",'',x['given'],'','Résultat attendu : '+x['expected'],'', 'Éprouve : '+', '.join(x['tests'])+'.','']
    write('arbitrages-et-cas.md',rows)

    if a.get('closure_U431'):
        closure = a['closure_U431']
        rows = ['# Clôture de l’audit des comportements — U431', '',
                'Clôture adoptée le '+closure['date']+'. '+closure['scope'], '',
                f'Catalogue conservé : **{len(caps)} capacités et {len(behaviors)} comportements**.', '',
                '## Candidats soldés', '',
                '| Candidat | Couverture existante | Justification |', '| --- | --- | --- |']
        for item in closure['covered_candidates']:
            rows.append(f"| {item['candidate_id']} | {cap(item['capability_id'])} | {item['rationale']} |")
        rows += ['', 'Les 16 candidats de l’audit sont soldés : 12 intégrés, 3 couverts par l’existant et 1 retiré.', '',
                 '## Frontière de l’univers', '',
                 'Les responsabilités commerciales et financières restent externes à Supply Chain Orchestration. Le modèle conserve le devenir des biens, les demandes, les prestations et les stocks. Les échanges avec les services externes restent descriptibles sans absorber leurs responsabilités.', '',
                 '## Travaux ultérieurs non bloquants', '']
        for item in closure['future_work']:
            rows += ['- **'+item['subject']+'** : '+item['remaining']]
        rows += ['', 'Les précisions déjà signalées sur les critères de décision, les options admissibles et les tolérances fournisseurs restent également des règles à instruire selon les cas. Aucune nouvelle étude ni reprise générale des liens déclenchée.', '',
                 '## Portée de la clôture', '', closure['limits'], '',
                 'Sources : U431, exclusion Supply U429 ; comparaisons de frontière ELM254/ELM255 et CMP165/CMP166. Preuves conservées dans `modeles/backlog/history/behavior-audit-closure-U431/`.']
        write_text_if_changed(OUT/'cloture-U431.md', '\n'.join(rows)+'\n')

    rows=['# Audit comparatif des comportements manquants — synthèse consolidée U298','',
        '**L’audit reste une base utile ; ses conclusions ont été mises à jour après U293–U297. Il n’est pas nécessaire de refaire toute l’étude marché à ce stade.** Le catalogue audité est inchangé ; les discussions ont corrigé le choix et la qualification des propositions. Les feedbacks datés conservent le raisonnement antérieur, pas des recommandations concurrentes.','',
        '**Le niveau Capacité → Comportement suffit pour les mécanismes étudiés. Le travail prioritaire consiste à rendre explicites quelques mécanismes et leurs contrats, pas à ajouter une profondeur ni à décomposer toutes les capacités.**','',
        'Le backlog refondu U290 contient **39 capacités et 14 comportements**, répartis sur quatre capacités. Les 35 autres ne sont pas 35 lacunes. Les seize fiches initiales se répartissent désormais en **7 candidats à instruire**, **5 options conditionnelles**, **3 propositions à réexaminer** et **1 retrait**. Les **7 arbitrages de responsabilité ou de contrat** restent ouverts. **Logistics Visibility** est le nom adopté U297 pour le parcours physique du picking au point final ; son niveau, son rattachement et les détails éditoriaux restent à instruire. Aucun nouveau BHV n’a été créé.','',
        'Cette conclusion vaut pour le périmètre Supply décrit. Elle ne démontre pas la complétude de Business Services, des opérations internes des exécutants ou des modèles de référence non encore détaillés. Aucun état installé ni taux de couverture des trois SI n’est inféré.','',
        '## Lecture et périmètre','',
        '- [Matrice et examen des 39 capacités, puis des 14 comportements](capacites.md).',
        '- [16 fiches de mécanismes : définition, bénéfice, exemple, frontières et dépendances](propositions.md).',
        '- [7 arbitrages, contrats et 10 cas métier fictifs](arbitrages-et-cas.md).',
        f"- [{len(sources)} sources primaires avec édition, passage et limites](sources.md).",
        '- [Autorité YAML des propositions](../../modeles/backlog/behavior-gap-audit.yaml).','',
        'Le socle U292 compare Microsoft, SAP, Oracle, Manhattan, Blue Yonder, Kinaxis et RELEX. Les compléments mobilisent Camunda pour les processus, project44/FourKites pour la visibilité et CSCMP pour le périmètre logistique. Guides, définitions professionnelles et présentations commerciales n’ont pas le même niveau de preuve. Il ne s’agit pas d’un inventaire exhaustif des produits ni d’un classement. Les six référentiels sont revus sur leur mandat de projection ; les offres MDM ne sont pas comparées exhaustivement. Les sources existantes ne sont pas présentées comme intégralement reconsultées en U298.','',
        '## Ce que la comparaison révèle','',
        '| Famille de marché | Apport pour FLOW | Écart à conserver / précaution |','| --- | --- | --- |',
        '| Microsoft SCM / Inventory Visibility | Politiques concrètes : besoin net, seuil/cible, ajustement des apports ; engagement logique ; distinction protection/consommation. | Le produit combine calcul, données, écrans et application. FLOW doit conserver décision et management séparés. S02, S08–S11, S26, S28. |',
        '| SAP aATP / Fashion ARun | Engagements révisables, alternatives, affectation et contrôle de cohérence avant libération. | aATP est une famille produit, pas notre capacité ATP. ARun ne rend pas Assignment synonyme de protection de groupes. S04–S06, S24. |',
        '| Oracle SCM | Compensation d’exécution, groupes de livraison cohérents, redistribution et collecte d’excédents. | Une orchestration produit ne fixe pas l’organisation FLOW. Vérifier les éditions : retrait du planning/jeopardy annoncé en 26D dans les notes 26B. S12, S17–S20, S25. |',
        '| Manhattan / Blue Yonder | Choix de fulfillment croisant service, économie, stock et contraintes opérationnelles. | Justifie notre valeur multidimensionnelle ; ne justifie ni un comportement par indicateur ni un super-optimiseur implicite dans Assignment. S15–S16. |',
        '| Kinaxis / RELEX | Arbitrage de risque et cibles coordonnées ; effets des aléas et, selon assortiment, de la périssabilité. | Appuis commerciaux de principe. Coordination multi-échelons et politiques de fraîcheur restent conditionnelles au besoin FLOW. S13–S14. |','',
        'La séparation FLOW est utile : une politique est configurée, une décision propose un résultat, un Order enregistre sa mise en action, puis des prestations sont orchestrées. La comparaison devient plus précise lorsque l’on aligne les **résultats métier** plutôt que les noms de modules.','',
        '## État courant des recommandations','',
        '| Capacité | Mécanismes proposés | Ce qu’ils rendent compréhensible |','| --- | --- | --- |',
        '| Replenishment Decision | Demand-linked Replenishment ; Target-restoring Replenishment ; Committed Supply Adjustment | Couvrir des besoins, restaurer une cible, corriger des apports existants : trois logiques, pas quatre verbes de modification. P01–P03, S08–S09. |',
        '| Execution Orchestration | P04 à réexaminer ; P05 retiré | P04 peut décrire le fonctionnement normal du parent ou un mécanisme de processus, sans bénéfice distinct. La compensation P05 relève de l’adaptabilité du processus dans le contexte U293. Le choix de variation et la coordination métier restent distincts. S17/S25/S32/S33. |',
        '| Stock Redistribution Decision | Shortage-driven Rebalancing ; Excess Consolidation | Couvrir un manque et regrouper des excédents n’ont pas le même déclencheur. Excédent s’apprécie selon périmètre et horizon. P06–P07, S12. |',
        '| Stocktaking | Recurring Stock Verification ; Triggered Stock Verification | Assurance régulière et réponse à un doute. Condition : préciser le mandat FLOW par rapport à l’exécutant. P08–P09, S01. |',
        '| Execution Tracking | Logistics Visibility : nom adopté ; P10 à réexaminer | Parcours physique complet du picking au point final. P10 ne doit pas recopier les écarts déjà inclus ; une portée aux autres prestations doit apporter un bénéfice distinct. Niveau et rattachement à préciser. S29/S37/S38. |',
        '| Order Lifecycle Management | Coordinated Order Release à clarifier | Gérer états et transitions de l’Order ; ne pas confondre avec la coordination des prestations. Le comportement distinct n’est pas établi. P11, S04/S18/S31. |','',
        'Les sept candidats encore à instruire sont P01–P03 (réapprovisionnement), P06–P07 (redistribution) et P08–P09 (fiabilisation). Aucun n’est adopté. P08/P09 demandent notamment de confirmer le mandat FLOW face aux exécutants. **U299 valide les deux corrections P04/P10** : les exceptions logistiques ne doivent pas être dupliquées ; coordonner des dépendances ne suffit pas à constituer un comportement autonome du parent. Les fiches initiales restent à réexaminer selon ces règles validées, pas à créer en l’état. Les autres propositions ne sont pas validées par cet accord.','',
        'La révision dépasse le nommage : le parcours logistique inclut les opérations d’entrepôt, les passages intermédiaires et leurs événements. Inventory Visibility reste complémentaire ; sortir d’un emplacement pour picking ne supprime pas la quantité du stock. FLOW doit recevoir les faits utiles sans prendre en charge les opérations internes des exécutants.','',
        '## Ce que je ne décomposerais pas encore','',
        f"**{nodes['D05.a']['fields']['name']}** : la prise en compte du risque et du service est déjà proche de sa définition. La coordination de plusieurs lieux peut justifier un comportement distinct si nous voulons arbitrer leurs buffers conjointement. Je propose deux fiches conditionnelles, sans forcer une symétrie avec les mécanismes de management.",'',
        '**CTP** : ressources additionnelles, alternatives de fulfillment et redistribution d’engagements constituent trois familles possibles. Mais une alternative de site déjà admissible appartient à ATP ; une substitution produit doit être autorisée ; une révision d’engagement doit respecter sa fermeté. Nommer ces comportements avant de préciser ces frontières ferait réapparaître les recouvrements que la refonte vient de réduire.','',
        '**Reservation et Supply Assignment** : le premier sujet est le contrat entre lien ressource-commande et engagement opposable. Le second est la cohérence d’un plan collectif : des décisions localement valables peuvent réclamer la même ressource. Le marché intègre ces étapes dans des produits ; il ne tranche pas leur responsabilité dans notre modèle.','',
        '**Application de plan aux Orders** : le principe reste bon. Un plan peut changer une affectation sans changer une commande ; un autre modifie contenu, structure et statut. Le rattacher tout entier à Lifecycle serait parfois trop étroit. A03 reprend l’arbitrage A8 existant, sans ouvrir une nouvelle hiérarchie.','',
        '**Retours et fournisseurs** : devenir d’un retour et révision d’un engagement fournisseur méritent un travail spécifique. Ce sont peut-être des mécanismes manquants, mais peut-être d’abord des responsabilités à attribuer entre Supply, Business Services et exécutant. Ni remboursement ni négociation ne sont absorbés implicitement.','',
        '## Les quatorze comportements existants restent utiles','',
        'ATP couvre déjà les engagements, tous les lieux admissibles, le temps opérationnel et les ressources futures. Planning conserve construction de scénarios, simulation/analyse et adaptation. Protection distingue enveloppes de groupe, plafonds, stock de sécurité et régulation du réassort. Promise Management conserve proposition, confirmation et révision.','',
        'La prochaine amélioration est contractuelle : exclusions et recouvrements de quantités, dates de validité, droits de révision, impacts, données d’entrée et limites d’autonomie. Les politiques BOP peuvent enrichir Promise Revision ; elles ne justifient pas un niveau inférieur. Les modalités écran, API, masse ou streaming restent des moyens d’application.','',
        '## Ordre de travail proposé','',
        '1. **Logistics Visibility** : [proposition U300](positionnement-U300.md) de comportement sous Execution Tracking (D06), avec justification de continuité physique. Niveau, rattachement et justification à valider ; le nom U297 n’est pas remis en débat.',
        '2. **Replenishment Decision** : instruire P01–P03 sur C02/C03 ; puis redistribution P06/P07 sur C04. Appui documentaire concret, prise en compte des excédents.',
        '3. **Reservation / Assignment / promesse** : A01/A02/A05 sur C01/C07/C10. Ensuite seulement décider la décomposition CTP.',
        '4. **Fiabilisation, orchestration et cycle de vie** : confirmer le mandat P08/P09 ; réexaminer P04/P10/P11 avant toute création. P05 demeure retiré comme comportement autonome.',
        '5. **Frontières complémentaires** : application de plan, engagements fournisseurs, devenir des retours et cibles réseau. Les cas peuvent conduire à une clarification sans ajout de nœud.','',
        'La consolidation U298 actualise les noms courants, les statuts, la matrice et les priorités sans modifier le catalogue. Les noms antérieurs sont des traces historiques, pas des options à réactiver par défaut. Une relecture ciblée des sources sera nécessaire lorsque le périmètre d’un candidat évoluera ou avant son adoption ; pas de recherche générale répétée sans nouveau besoin. Les mécanismes, rattachements et responsabilités restant ouverts demandent le travail conjoint. Aucune release.','',
        '## Contrôles et limites','',
        'Le générateur vérifie les 39 capacités, les 14 comportements, les parents des candidats, les références et le maintien des octets du catalogue et des 125 fichiers publiés/protégés de la refonte. Ces contrôles établissent la cohérence documentaire ; ils ne valident pas les choix métier. Résultat dans [checks.json](checks.json).',
        '',f"Empreinte du modèle audité : `{a['baseline']['sha256']}`."]
    write('rapport.md',rows)
    checks=dict(status='passed',capabilities_reviewed=len(caps),existing_behaviors_reviewed=len(behaviors),
        market_sources=len(sources),candidate_priorities=dict(Counter(p['priority'] for p in a['candidates'] if p['status']=='proposed')),
        candidate_statuses=dict(Counter(p['status'] for p in a['candidates'])),
        candidates=len(proposals),arbitrations=len(a['arbitrations']),scenarios=len(a['scenarios']),
        active_model_unchanged=True,protected_files_unchanged=len(protected),
        model_sha256=a['baseline']['sha256'],scope='Structural and preservation checks; U297 name approval recorded separately; no additional business adoption.')
    if a.get('market_fields_U311'):
        checks['market_enrichment_verified']='U311: only D05.e.market_comparisons added to catalogue; prior fields unchanged'
    if a.get('implementation_U316'):
        checks['active_model_unchanged']=False
        checks['scope']='U316 scoped catalogue migration and existing audit preservation; proposed details are not adopted.'
        checks['migration_U316_verified']=a['implementation_U316']['delta']
        checks['market_enrichment_verified']='U311 verified against immutable pre-U316 capture; subsequent U316 changes checked separately.'
    if a.get('market_fields_U317'):
        checks['market_fields_U317_verified']='Only D05.c market comparisons and revision changed after U316.'
    if a.get('implementation_U318'):
        checks['migration_U318_verified']=a['implementation_U318']['delta']
        checks['scope']='U318 redistribution behaviors, adopted fields and parents checked; earlier U316/U317 migrations verified against captures.'
    if a.get('market_fields_U323'):
        checks['market_fields_U323_verified']='Only D05.e market comparisons and revision enriched after U318.'
    if a.get('market_fields_U324'):
        checks['market_fields_U324_verified']='Only D05.e market comparisons and revision clarified after U323.'
    if a.get('market_fields_U328'):
        checks['market_fields_U328_verified']='Only D05.a market comparisons and revision enriched after U324.'
    if a.get('implementation_U329'):
        checks['migration_U329_verified']=a['implementation_U329']['delta']
        checks['scope']='U329 adopted name and definition, updated references and prior migrations checked against preserved captures.'
    if a.get('market_fields_U330'):
        checks['market_fields_U330_verified']='Only D05.a market comparisons and revision enriched after U329.'
    if a.get('implementation_U332'):
        checks['migration_U332_verified']=a['implementation_U332']['delta']
        checks['scope']='U332 three sibling behaviors, scoped approvals and prior migrations verified against preserved captures.'
    if a.get('implementation_U334'):
        checks['migration_U334_verified']=a['implementation_U334']['delta']
        checks['scope']='U334 Stocktaking mandate and behaviors, scoped approvals and prior migrations checked against preserved captures.'
    if a.get('implementation_U342'):
        checks['migration_U342_verified']=a['implementation_U342']['delta']
        checks['scope']='U342 capability approval and proposed behaviors/parent checked independently; prior migrations and frozen evidence preserved.'
    if a.get('implementation_U343'):
        checks['migration_U343_verified']=a['implementation_U343']['delta']
        checks['scope']='U343 scoped behavior and parent adoption verified; U342 proposal and prior evidence preserved.'
    if a.get('implementation_U345'):
        checks['migration_U345_verified']=a['implementation_U345']['delta']
        checks['scope']='U345 plan application and recommendation explanations verified; earlier approvals and frozen evidence preserved.'
    if a.get('implementation_U349'):
        checks['migration_U349_verified']=a['implementation_U349']['delta']
        checks['scope']='U349 firming and optimization protection integrated with scoped adoption; prior stages and frozen evidence preserved.'
    if a.get('implementation_U350'):
        checks['migration_U350_verified']=a['implementation_U350']['delta']
        checks['scope']='U349 behaviors and U350 Freezing name adoption verified; earlier approvals and frozen evidence preserved.'
    if a.get('implementation_U363'):
        checks['migration_U363_verified']=a['implementation_U363']['delta']
        checks['scope']='U363 D04 hierarchy, identity preservation and prior adoption evidence verified; publications unchanged.'
    if a.get('implementation_U364'):
        checks['migration_U364_verified']=a['implementation_U364']['delta']
        checks['scope']='U364 Supply Assignment terminal behaviors and scoped adoption verified; historical migrations and published evidence preserved.'
    if a.get('implementation_U378'):
        checks['migration_U378_verified']=a['implementation_U378']['delta']
        checks['scope']='U378 plan decision and U369 domain name adopted; proposed dependency contracts, prior migrations and frozen publications checked.'
    if a.get('implementation_U380'):
        checks['migration_U380_verified']=a['implementation_U380']['delta']
        checks['scope']='U380 disposition decision and D05 parent adopted; proposed contracts, earlier adopted fields and frozen publications preserved.'
    if a.get('implementation_U383'):
        checks['migration_U383_verified']=a['implementation_U383']['delta']
        checks['scope']='U383 order capabilities and disposition strategies verified; earlier adoptions checked at their preserved stages; publications unchanged.'
    if a.get('implementation_U384'):
        checks['migration_U384_verified']=a['implementation_U384']['delta']
        checks['scope']='U384 scoped names verified; prior adopted fields and relationships preserved; Customer Return proposal remains outside the catalog.'
    if a.get('implementation_U385'):
        checks['migration_U385_verified']=a['implementation_U385']['delta']
        checks['scope']='U385 Customer Return definition, terminal behaviors, adoption scopes and supplier relay verified; historical stages and frozen publications preserved.'
    for migration_key in ('implementation_U387','implementation_U388','implementation_U391'):
        if a.get(migration_key):
            checks[migration_key.replace('implementation','migration')+'_verified']=a[migration_key]['delta']
            checks['scope']='Supplier Return and Purchase Order paths, terminal hierarchy and prior adopted fields verified; frozen publications preserved.'
    if a.get('current_synthesis_U298'):
        checks['current_candidate_categories']={k:len(a['current_synthesis_U298'][k]) for k in ['retained_candidate_ids','conditional_candidate_ids','reassess_candidate_ids','withdrawn_candidate_ids']}
    if a.get('adopted_corrections_U299'):
        checks['adopted_correction_hashes_verified']=['P04','P10']
    if a.get('implementation_U395'):
        checks['migration_U395_verified'] = a['implementation_U395']['delta']
        checks['scope'] = 'U395 consignment capabilities, approved names/definitions/parents and unchanged previous adopted fields verified; no behavior added; frozen publications preserved.'
    if a.get('implementation_U398'):
        checks['migration_U398_verified'] = a['implementation_U398']['delta']
        checks['scope'] = 'Existing audit updated for U398 approved consignment behaviors; earlier adopted fields and frozen publications preserved. U399: interaction rules recorded for future work, no new audit.'
    if a.get('implementation_U401'):
        checks['migration_U401_verified'] = a['implementation_U401']['delta']
        checks['scope'] = 'Existing audit updated for U401: twelve approved consignment, sales and transfer behaviors; parents, terminal hierarchy, previous adopted fields, existing relations and frozen publications preserved.'
    if a.get('implementation_U402'):
        checks['migration_U402_verified'] = a['implementation_U402']['delta']
        checks['scope'] = 'Existing audit updated for U402: three CTP behaviors; approved fields, existing relations, terminal hierarchy and frozen publications preserved.'
    if a.get('implementation_U403'):
        checks['migration_U403_verified'] = a['implementation_U403']['delta']
        checks['scope'] = 'Existing audit updated for U403: Supplier Confirmation under Purchase Order; historical adopted fields, existing relations and frozen publications preserved.'
    if a.get('implementation_U406'):
        checks['migration_U406_verified'] = a['implementation_U406']['delta']
        checks['scope'] = 'Existing audit updated for U406: three physical visibility behaviors and Business Process Tracking; terminal hierarchy, previous adopted fields and frozen publications preserved.'
    if a.get('implementation_U409'):
        checks['migration_U409_verified'] = a['implementation_U409']['delta']
        checks['scope'] = 'Existing audit updated for U409: Process orchestrates Services; nine approved names, two editorial labels, unchanged topology and previous non-name approvals; historical evidence and frozen publications preserved.'
    if a.get('implementation_U410'):
        checks['migration_U410_verified'] = a['implementation_U410']['delta']
        checks['scope'] = 'Existing audit updated for U410: P11 integrated into existing Order Release, adopted definition and unchanged graph; previous approvals and frozen publications preserved.'
    if a.get('implementation_U413'):
        checks['migration_U413_verified'] = a['implementation_U413']['delta']
        checks['scope'] = 'Existing audit updated for U413: Order Backlog Management name adopted, targeted placement review recorded, unchanged graph and prior non-name approvals; frozen publications preserved.'
    if a.get('implementation_U414'):
        checks['migration_U414_verified'] = a['implementation_U414']['delta']
        checks['scope'] = 'Existing audit updated for U414: Order Backlog Planning created, Order Release reparented with unchanged identity and definition; Split and Structuring unchanged; historical approvals and frozen publications preserved.'
    if a.get('implementation_U417'):
        checks['migration_U417_verified'] = a['implementation_U417']['delta']
        checks['scope'] = 'Existing audit updated for U417/U418: Structuring and Lifecycle under Order Backlog Management; Split under Structuring, Release under Lifecycle; behavior definitions and historical evidence preserved.'
    if a.get('implementation_U420'):
        checks['migration_U420_verified'] = a['implementation_U420']['delta']
        checks['scope'] = 'Existing audit updated for U420: Archiving in D03; Lifecycle in D04; behavior definitions and parents unchanged; prior approvals and frozen publications preserved.'
    if a.get('implementation_U424'):
        checks['migration_U424_verified'] = a['implementation_U424']['delta']
        checks['scope'] = 'Existing audit updated for U424: six Lifecycle dimensions with explicit states, scopes and constraints; two merged behaviors with preserved historical approvals; no lower hierarchy or implicit state-value adoption.'
    if a.get('implementation_U425'):
        checks['migration_U425_verified'] = a['implementation_U425']['delta']
    if a.get('replenishment_reassessment_U426') and not a.get('implementation_U427'):
        assert all(proposals[i]['status']=='needs_reassessment_U426' for i in ['P01','P02','P03'])
        checks['scope'] = 'U425 descriptions retained; U426 reopens P01-P03 as possible behaviors. No new nodes, no implicit approval of proposed names or definitions; historical migrations preserved.'
    if a.get('implementation_U427'):
        for candidate, behavior in {'P01':'BHV083','P02':'BHV084','P03':'BHV085'}.items():
            assert proposals[candidate]['status']=='implemented_U427'
            assert proposals[candidate]['implemented_as']==behavior
        checks['migration_U427_verified'] = a['implementation_U427']['delta']
        checks['scope'] = 'U427 integrates three Replenishment Decision behaviors: two policies plus a combinable adjustment mechanism. P01-P03 closed as implemented; historical approvals and other audit arbitrations preserved.'
    if a.get('closure_U431'):
        closure = a['closure_U431']
        assert closure['status']=='closed'
        assert sha256((ROOT/a['baseline']['path']).read_bytes()).hexdigest()==closure['model_sha256']
        assert sha256((ROOT/closure['audit_before']).read_bytes()).hexdigest()==closure['audit_before_sha256']
        prior = read(ROOT/closure['audit_before'])
        assert prior['baseline']==a['baseline']
        for key in prior:
            if key.startswith('implementation_'):
                assert prior[key]==a[key], 'Historical implementation changed: '+key
        for identifier, parent in {'P04':'D06.d','P10':'D07.d','P12':'D05.a'}.items():
            assert proposals[identifier]['status']=='covered_by_existing_U431'
            assert proposals[identifier]['covered_by']==parent
        assert all(p['status'].startswith(('implemented_', 'covered_by_existing_', 'withdrawn_')) for p in a['candidates'])
        assert all(x['catalogue_status_U431']=='closed' for x in a['arbitrations'])
        for category in ['retained_candidate_ids','conditional_candidate_ids','reassess_candidate_ids']:
            assert not a['current_synthesis_U298'][category]
        checks['audit_status']='closed_U431'
        checks['closure_catalogue_unchanged']=True
        checks['scope']='Existing behavior audit closed U431. All candidates disposed; catalogue unchanged; future rules and interface contracts retained without blanket validation.'
    write_text_if_changed(OUT/'checks.json', json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
    return checks


def checked_run(full=False):
    if not __debug__:
        raise RuntimeError('Historical assertions require Python without -O')
    from scripts.verification_checkpoint import run
    # Include all model/history files, code and protected evidence, including
    # additions/removals. Only generated views may change during a full run.
    def paths():
        files = []
        for folder in ('modeles', 'audits', 'scripts'):
            files.extend(p for p in (ROOT/folder).rglob('*') if p.is_file()
                         and '__pycache__' not in p.parts
                         and 'staging' not in p.parts
                         and '2026-09-19-performance' not in p.parts)
        protected = json.loads((ROOT/'audits/2026-09-17-refonte-appliquee/protected.json').read_text(encoding='utf-8'))
        files.extend(ROOT/p for p in protected)
        return files
    outputs = [OUT/name for name in ['arbitrages-et-cas.md', 'capacites.md', 'checks.json', 'cloture-U431.md', 'feedback-U293.md', 'feedback-U294.md', 'feedback-U295.md', 'feedback-U296.md', 'feedback-U297.md', 'feedback-U304.md', 'feedback-U306.md', 'feedback-U310.md', 'positionnement-U300.md', 'propositions.md', 'rapport.md', 'sources.md', 'validation-U305.md', 'validation-U308.md']]
    return run(ROOT/'.runtime/behavior-audit-checkpoint.json', paths, main, outputs,
               full=full, runtime='PyYAML '+yaml.__version__)


if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true', help='Replay every historical assertion, ignoring the checkpoint')
    parser.add_argument('--details', action='store_true', help='Print every historical check')
    args = parser.parse_args()
    checks, reused = checked_run(args.full)
    summary = checks if args.details else {k: checks[k] for k in (
        'status', 'audit_status', 'capabilities_reviewed', 'existing_behaviors_reviewed',
        'protected_files_unchanged', 'scope') if k in checks}
    print(json.dumps(dict(summary, checkpoint_reused=reused), ensure_ascii=False))

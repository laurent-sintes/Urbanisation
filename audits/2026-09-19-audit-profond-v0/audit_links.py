"""Read-only, reproducible graph audit; generated files are audit evidence, not models."""
from collections import Counter, defaultdict, deque
import argparse
from hashlib import sha256
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps

OUT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--model', default='modeles/backlog/model.yaml', help='Current model or an immutable audit snapshot.')
parser.add_argument('--tag', default='', help='Output filename suffix, for example after-U435.')
args = parser.parse_args()
MODEL = ROOT / args.model
suffix = '-' + args.tag if args.tag else ''
model = read(MODEL)
nodes = {n['id']: n for n in model['nodes']}
relations = model['relations']
structural = [r for r in relations if r['type'] in ('contains', 'presents')]
business = [r for r in relations if r['type'] not in ('contains', 'presents')]
parents = defaultdict(list)
children = defaultdict(list)
for relation in structural:
    parents[relation['target_id']].append(relation['source_id'])
    children[relation['source_id']].append(relation['target_id'])

def endpoint(ident):
    if nodes[ident]['kind'] == 'behavior' and len(parents[ident]) == 1:
        return parents[ident][0]
    return ident

adj = defaultdict(set)
incoming = defaultdict(list)
outgoing = defaultdict(list)
pair_relations = defaultdict(list)
for relation in business:
    source, target = relation['source_id'], relation['target_id']
    outgoing[source].append(relation['id'])
    incoming[target].append(relation['id'])
    adj[source].add(target)
    adj[target].add(source)
    pair_relations[tuple(sorted((endpoint(source), endpoint(target))))].append(relation['id'])

def strings(value, path='fields'):
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for key, nested in value.items():
            # Market citations do not assert an interaction in the FLOW model.
            if key != 'market_comparisons':
                yield from strings(nested, path + '.' + key)
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            yield from strings(nested, path + f'[{index}]')

inline_missing = []
inline_count = 0
unresolved = []
for source, node in nodes.items():
    for path, value in strings(node.get('fields', {})):
        for match in re.finditer(r'\[([^\]]+)\]\(model:([A-Za-z0-9_.-]+)(?:#[^)]+)?\)', value):
            target = match.group(2)
            inline_count += 1
            if target not in nodes:
                unresolved.append({'source_id': source, 'target_id': target, 'field': path})
                continue
            first, second = endpoint(source), endpoint(target)
            # A semantic mention is only a review candidate, never a proven missing edge.
            if first != second and tuple(sorted((first, second))) not in pair_relations:
                if nodes[first]['kind'] == nodes[second]['kind'] == 'capability':
                    inline_missing.append({'source_id': source, 'target_id': target,
                                           'projected_source': first, 'projected_target': second,
                                           'field': path, 'label': match.group(1)})

cycles = []
def visit(ident, trail):
    if ident in trail:
        cycles.append(trail[trail.index(ident):] + [ident])
        return
    for child in children[ident]:
        visit(child, trail + [ident])
for ident in nodes:
    visit(ident, [])

components = []
remaining = set(nodes)
while remaining:
    seed = min(remaining)
    reached = {seed}
    pending = deque([seed])
    while pending:
        for other in adj[pending.popleft()] - reached:
            reached.add(other)
            pending.append(other)
    remaining -= reached
    components.append(sorted(reached))

generic_condition = 'Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.'
generic_effect = 'Résultat consommé sans transfert de responsabilité du fournisseur.'
duplicates = defaultdict(list)
for relation in business:
    duplicates[(relation['type'], relation['source_id'], relation['target_id'])].append(relation['id'])
metrics = {
    'model_path': str(MODEL.relative_to(ROOT)).replace('\\', '/'),
    'model_sha256': sha256(MODEL.read_bytes()).hexdigest(),
    'model_version': model.get('version'),
    'node_count': len(nodes),
    'node_kinds': dict(Counter(n['kind'] for n in nodes.values())),
    'relation_count': len(relations),
    'relation_types': dict(Counter(r['type'] for r in relations)),
    'business_relation_count': len(business),
    'missing_endpoints': [r['id'] for r in relations if r['source_id'] not in nodes or r['target_id'] not in nodes],
    'structural_multi_parents': {k: v for k, v in parents.items() if len(v) > 1},
    'structural_cycles': cycles,
    'roots': [n for n in nodes if not parents[n]],
    'business_self_links': [r['id'] for r in business if r['source_id'] == r['target_id']],
    'duplicate_business_triples': [v for v in duplicates.values() if len(v) > 1],
    'meaning_nonempty': sum(bool(r.get('qualification', {}).get('meaning')) for r in business),
    'conditions_nonempty': sum(bool(r.get('qualification', {}).get('conditions')) for r in business),
    'effects_nonempty': sum(bool(r.get('qualification', {}).get('effects')) for r in business),
    'role_needs': sum(r.get('qualification', {}).get('role') == 'needs' for r in business),
    'business_label_or_verb_nonempty': sum(bool(r.get('fields', {}).get('label') or r.get('fields', {}).get('verb')) for r in business),
    'exact_generic_condition_only': sum(r.get('qualification', {}).get('conditions') == [generic_condition] for r in business),
    'exact_generic_effect_only': sum(r.get('qualification', {}).get('effects') == [generic_effect] for r in business),
    'unqualified_business_relations': [r['id'] for r in business if not r.get('qualification', {}).get('meaning')],
    'business_review_states': dict(Counter(r.get('review', {}).get('state', 'absent') for r in business)),
    'business_lifecycle_states': dict(Counter(r.get('lifecycle', {}).get('state', 'absent') for r in business)),
    'capability_business_degrees': [dict(id=ident, name=n['fields']['name'], incoming=incoming[ident], outgoing=outgoing[ident]) for ident,n in nodes.items() if n['kind']=='capability'],
    'business_components_sizes': sorted([len(c) for c in components], reverse=True),
    'behavior_business_endpoints': [ident for ident,n in nodes.items() if n['kind']=='behavior' and (incoming[ident] or outgoing[ident])],
    'inline_model_reference_count': inline_count,
    'unresolved_inline_model_references': unresolved,
    'inline_capability_mentions_without_business_pair': inline_missing,
    'interpretation_limit': 'Absence de lien direct, degré et mention textuelle sont des signaux de revue, pas des exigences de workflow ni une preuve de capacité absente. Les dépendances métier peuvent être cycliques ; les seuls cycles recherchés comme défauts sont structurels.',
}
release_root = ROOT / 'modeles/release'
release_index = read(release_root / 'index.json')
descriptor_path = release_root / release_index['current']
descriptor = read(descriptor_path)
snapshot_path = release_root / descriptor['path']
snapshot = read(snapshot_path)
published_relations = {r['id']: r for r in snapshot['relations']}
published_nodes = {n['id']: n for n in snapshot['nodes']}
published_business = [r for r in snapshot['relations'] if r['type'] not in ('contains', 'presents')]
metrics['published_comparison'] = {
    'version': descriptor['version'],
    'descriptor_path': str(descriptor_path.relative_to(ROOT)).replace('\\', '/'),
    'snapshot_path': str(snapshot_path.relative_to(ROOT)).replace('\\', '/'),
    'descriptor_hash_ok': sha256(descriptor_path.read_bytes()).hexdigest() == next(p['sha256'] for p in release_index['publications'] if p['descriptor'] == release_index['current']),
    'snapshot_hash_ok': sha256(snapshot_path.read_bytes()).hexdigest() == descriptor['sha256'],
    'node_count': len(snapshot['nodes']),
    'relation_count': len(snapshot['relations']),
    'business_relation_count': len(published_business),
    'business_meaning_nonempty': sum(bool(r.get('qualification', {}).get('meaning')) for r in published_business),
    'backlog_only_node_ids': sorted(nodes.keys() - published_nodes.keys()),
    'backlog_only_relation_ids': sorted(r['id'] for r in relations if r['id'] not in published_relations),
    'common_relation_content_differences': [r['id'] for r in relations if r['id'] in published_relations and any(r.get(k) != published_relations[r['id']].get(k) for k in ['fields', 'qualification', 'source_id', 'target_id', 'type'])],
    'common_node_fields_differences': [ident for ident in nodes.keys() & published_nodes.keys() if nodes[ident].get('fields') != published_nodes[ident].get('fields')],
}
(OUT / f'metrics-liens{suffix}.yaml').write_text(dumps(metrics), encoding='utf-8')
lines = ['# Inventaire reproductible des liens métier', '',
         f"Source : `{metrics['model_path']}` ; SHA-256 `{metrics['model_sha256']}`.", '',
         'Relations structurelles exclues. Cet inventaire conserve les orientations originales ; un lien `needs` va du consommateur au fournisseur.', '']
for relation in business:
    q = relation.get('qualification', {})
    lines += [f"## {relation['id']}", '',
              f"`{relation['source_id']}` {nodes[relation['source_id']]['fields']['name']} → `{relation['target_id']}` {nodes[relation['target_id']]['fields']['name']}", '',
              f"Type : `{relation['type']}` ; rôle : `{q.get('role', 'non renseigné')}` ; statut : `{relation.get('review', {}).get('state', 'absent')}`.", '',
              'Sens : ' + q.get('meaning', 'Non renseigné.'), '',
              'Conditions : ' + ' | '.join(q.get('conditions', [])), '',
              'Effets : ' + ' | '.join(q.get('effects', [])), '',
              'Sources : ' + ', '.join(relation.get('source_refs', [])), '']
(OUT / f'inventaire-liens{suffix}.md').write_text('\n'.join(lines), encoding='utf-8')
print(dumps({k:v for k,v in metrics.items() if k not in ['capability_business_degrees', 'inline_capability_mentions_without_business_pair']}))
print('Candidate mentions:',len(inline_missing))

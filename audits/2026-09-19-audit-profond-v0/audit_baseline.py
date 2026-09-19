"""Read-only inventory of the live model and its selected publication for U434.

Run from repository root. Only writes metrics.yaml next to this script.
These measurements do not establish business coverage or approval.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def inventory():
    path = ROOT / 'modeles/backlog/model.yaml'
    model = read(path)
    nodes = model['nodes']
    relations = model['relations']
    gloss = read(ROOT / 'modeles/backlog/glossary.yaml')
    idx = read(ROOT / 'modeles/release/index.json')
    descriptor_path = ROOT / 'modeles/release' / idx['current']
    desc = read(descriptor_path)
    published_path = descriptor_path.parent / desc['path']
    published = read(published_path)
    result = {
        'audit_id': 'AUDIT-V0-U434', 'consulted_on': '2026-09-19',
        'model': {'path': path.relative_to(ROOT).as_posix(), 'sha256': digest(path),
                  'declared_version': model['version'], 'declared_as_of': model['as_of']},
        'counts': {'nodes': len(nodes), 'relations': len(relations),
                   'node_kinds': dict(Counter(n['kind'] for n in nodes)),
                   'relation_types': dict(Counter(r['type'] for r in relations)),
                   'glossary_terms': len(gloss['terms'])},
        'market': {}, 'validation_scope': {},
        'publication': {'index_current': idx['current'], 'version': desc['version'],
                        'sha256': digest(published_path),
                        'nodes': len(published['nodes']), 'relations': len(published['relations'])},
    }
    for kind in ('domain', 'reference', 'capability', 'behavior'):
        subset = [n for n in nodes if n['kind'] == kind]
        result['market'][kind] = {
            'count': len(subset),
            'with_comparison': sum(bool(n['fields'].get('market_comparisons')) for n in subset),
            'without_comparison': [n['id'] for n in subset if not n['fields'].get('market_comparisons')],
        }
        result['validation_scope'][kind] = {
            'lifecycle_states': dict(Counter(n.get('lifecycle', {}).get('state') for n in subset)),
            'fields_validated': {field: sum(field in n.get('lifecycle', {}).get('validated_fields', []) for n in subset)
                                 for field in ('name', 'definition', 'scope', 'finality', 'decomposition_rationale', 'market_comparisons')},
            'definition_not_in_validated_fields': [n['id'] for n in subset
                if 'definition' not in n.get('lifecycle', {}).get('validated_fields', [])],
        }
    comps = [c for n in nodes for c in n['fields'].get('market_comparisons', [])]
    result['market']['entries'] = len(comps)
    result['market']['vendors_raw'] = dict(Counter(c.get('vendor') for c in comps))
    result['market']['statuses'] = dict(Counter(c.get('status') for c in comps))
    result['glossary'] = {
        'review_states': dict(Counter(t['review']['state'] for t in gloss['terms'])),
        'with_comparison': sum(bool(t.get('market_comparisons')) for t in gloss['terms']),
    }
    published_by_id = {n['id']: n for n in published['nodes']}
    result['publication']['nodes_only_in_backlog'] = [n['id'] for n in nodes if n['id'] not in published_by_id]
    result['publication']['common_nodes_different_fields'] = [n['id'] for n in nodes
        if n['id'] in published_by_id and n['fields'] != published_by_id[n['id']]['fields']]
    published_rel = {r['id']: r for r in published['relations']}
    result['publication']['relations_only_in_backlog'] = [r['id'] for r in relations if r['id'] not in published_rel]
    # Baseline immutable publications, revisions, decisions and frozen provenance.
    protected = [p for folder in ('release', 'revisions', 'decisions', 'provenance')
                 for p in (ROOT / 'modeles' / folder).rglob('*') if p.is_file()
                 and p.name != 'source-records.json']
    result['protected_files'] = {p.relative_to(ROOT).as_posix(): digest(p) for p in sorted(protected)}
    return result


if __name__ == '__main__':
    result = inventory()
    output = Path(__file__).with_name('metrics.yaml')
    output.write_text(dumps(result), encoding='utf-8')
    print(dumps({k: v for k, v in result.items() if k != 'protected_files'}))
    print(f"Protected files recorded: {len(result['protected_files'])}")

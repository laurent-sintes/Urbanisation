"""One-off U449 migration; existing types, approvals and publications are preserved."""
from collections import Counter
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
from scripts.structured_io import read, dumps

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent
path = ROOT / 'modeles/backlog/model.yaml'
before_bytes = path.read_bytes()
with (AUDIT / 'model-before.yaml').open('xb') as capture:
    capture.write(before_bytes)
protected = {}
for folder in ('release', 'revisions', 'decisions', 'provenance'):
    for item in (ROOT / 'modeles' / folder).rglob('*'):
        if item.is_file() and item.name != 'source-records.json':
            protected[item.relative_to(ROOT).as_posix()] = sha256(item.read_bytes()).hexdigest()
(AUDIT / 'protected-before.json').write_text(json.dumps(protected, indent=2), encoding='utf-8')
model = read(path)
before = deepcopy(model)
completions = {
    'D01.f': ('knowledge', 'Établir et actualiser une connaissance des états et quantités, comme Operations Tracking.'),
    'D01.c': ('knowledge', 'Rendre les états de stock lisibles, comme Service Capacity Visibility.'),
    'D01.g': ('action', 'Enregistrer les faits et leurs justifications ; aucune sélection de scénario.'),
    'D01.d': ('action', 'Réaliser le comptage et le rapprochement justifié, comme Service Reconciliation.'),
    'D02.c': ('action', 'Matérialiser un engagement qui bloque les usages concurrents ; la politique de réservation reste une décision distincte.'),
    **{identifier: ('action', 'Recevoir et intégrer une projection de maître externe, comme Service Catalog Ingestion ; aucune administration du maître.')
       for identifier in ('D09.d', 'D11.a', 'D08.d', 'D12.a', 'D13.a')},
}
for node in model['nodes']:
    if node['id'] in completions:
        assert 'nature' not in node['fields']
        node['fields']['nature'] = completions[node['id']][0]
        node.setdefault('source_refs', []).append('U449')
        if 'nature' not in node.setdefault('proposed_fields', []):
            node['proposed_fields'].append('nature')
        assert 'nature' not in node.get('lifecycle', {}).get('validated_fields', [])
model['principles'].append({
    'id': 'PRINCIPLE-CAPABILITY-NATURE',
    'statement': 'Chaque capacité porte un type explicite dans fields.nature. Les icônes correspondent à ce type ; les décisions sont présentées après les autres capacités de chaque domaine, avec une séparation visuelle légère lorsque les deux groupes sont présents. Cet ordre de lecture ne définit ni séquence d’exécution ni hiérarchie supplémentaire.',
    'source_refs': ['U449'],
})
nodes = {node['id']: node for node in model['nodes']}
orders = {}
for parent in model['nodes']:
    if parent['kind'] not in ('domain', 'reference'):
        continue
    positions = [i for i, relation in enumerate(model['relations'])
                 if relation['source_id'] == parent['id'] and relation['type'] == 'contains'
                 and nodes[relation['target_id']]['kind'] == 'capability']
    relations = [model['relations'][i] for i in positions]
    ordered = sorted(relations, key=lambda relation: nodes[relation['target_id']]['fields']['nature'] == 'decision')
    for i, relation in zip(positions, ordered):
        model['relations'][i] = relation
    orders[parent['id']] = [relation['target_id'] for relation in ordered]
assert {r['id']: r for r in before['relations']} == {r['id']: r for r in model['relations']}
for previous, current in zip(before['nodes'], model['nodes']):
    for key, value in previous['fields'].items():
        assert current['fields'][key] == value
    assert previous.get('lifecycle') == current.get('lifecycle')
    assert previous.get('approved_fields') == current.get('approved_fields')
path.write_text(dumps(model), encoding='utf-8')
summary = {'completed': {key: {'nature': value[0], 'rationale': value[1], 'status': 'proposed'} for key, value in completions.items()},
           'counts': dict(Counter(n['fields']['nature'] for n in model['nodes'] if n['kind'] == 'capability')),
           'orders': orders, 'existing_values_and_approvals_preserved': True,
           'source_refs': ['U435', 'U449'], 'protected_files': len(protected)}
(AUDIT / 'changes.yaml').write_text(dumps(summary), encoding='utf-8')
print(json.dumps({'completed': len(completions), 'counts': summary['counts'], 'protected_files': len(protected)}))

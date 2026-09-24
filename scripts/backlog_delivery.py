"""Expose delivery declarations; never infer approval from an annex status."""
from pathlib import Path

try:
    from .structured_io import read
except ImportError:
    from structured_io import read


def check_delivery(root, candidate):
    root = Path(root)
    nodes = {n['id']: n for n in candidate['nodes']}
    relations = candidate['relations']
    rows, errors = [], []
    for path in sorted((root / 'modeles/backlog').glob('*.yaml')):
        doc = read(path)
        if not isinstance(doc, dict) or 'publication_delivery' not in doc:
            continue
        declaration = doc['publication_delivery']
        label = path.name
        if not isinstance(declaration, dict) or declaration.get('state') not in ('pending', 'applied'):
            errors.append('backlog-delivery: invalid declaration in ' + label)
            continue
        state = declaration['state']
        rows.append({'path': path.relative_to(root).as_posix(), 'state': state,
                     'summary': declaration.get('summary', ''),
                     'source_refs': declaration.get('source_refs', [])})
        if state == 'pending':
            continue
        required = declaration.get('required_nodes', [])
        absent = declaration.get('absent_nodes', [])
        if not required and not absent:
            errors.append('backlog-delivery: applied declaration without checks in ' + label)
        for item in required:
            ident = item['id']
            node = nodes.get(ident)
            if node is None:
                errors.append(f'backlog-delivery: {label}: required node missing: {ident}')
                continue
            for field, expected in item.get('fields', {}).items():
                if node['fields'].get(field) != expected:
                    errors.append(f'backlog-delivery: {label}: field mismatch: {ident}.{field}')
            if 'parent' in item and not any(r['type'] == 'contains' and r['source_id'] == item['parent']
                                            and r['target_id'] == ident for r in relations):
                errors.append(f'backlog-delivery: {label}: missing parent: {ident}')
        for ident in absent:
            if ident in nodes:
                errors.append(f'backlog-delivery: {label}: retired node still present: {ident}')
    return rows, errors

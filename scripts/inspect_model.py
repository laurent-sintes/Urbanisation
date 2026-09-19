"""Read exact model records/fields without flooding the agent with whole files."""
import argparse
import json
from pathlib import Path
try:
    from .structured_io import read, working_path
    from .release_catalog import resolve_release
except ImportError:
    from structured_io import read, working_path
    from release_catalog import resolve_release

ROOT = Path(__file__).resolve().parents[1]


def inspect(root=ROOT, *, space='backlog', version=None, collection='nodes', ids=(),
            fields=None, query='', limit=20, offset=0, relations=False):
    root = Path(root)
    if space not in ('backlog', 'release') or collection not in ('nodes', 'relations', 'terms'):
        raise ValueError('Espace ou collection inconnus.')
    if limit < 1 or offset < 0:
        raise ValueError('Pagination invalide.')
    if version and space != 'release':
        raise ValueError('Une version explicite concerne uniquement une release.')
    if space == 'release':
        pointer = resolve_release(root/'modeles/release', version)
        path = root/'modeles/release'/pointer['path']
        model = read(path)
        document = model.get('glossary', {}) if collection == 'terms' else model
    else:
        path = working_path(root/'modeles/backlog', 'glossary' if collection == 'terms' else 'model')
        document = read(path)
        model = document
    records = document.get(collection, [])
    by_id = {item['id']: item for item in records}
    missing = set(ids) - by_id.keys()
    if missing:
        raise ValueError('Identifiants absents de cette source : ' + ', '.join(sorted(missing)))
    matches = [by_id[identifier] for identifier in ids] if ids else [item for item in records
        if query.casefold() in (item['id'] + ' ' + item.get('fields', item).get('name', '')).casefold()]
    # Explicit IDs are never silently truncated. Pagination applies to discovery.
    selected = matches if ids else matches[offset:offset+limit]
    results = []
    for item in selected:
        values = item if collection == 'relations' else item.get('fields', item)
        if not ids:
            results.append({key: value for key, value in {
                'id': item['id'], 'kind': item.get('kind'), 'name': values.get('name'),
                'source_id': item.get('source_id'), 'target_id': item.get('target_id')}.items() if value is not None})
            continue
        requested = fields if fields is not None else (
            ('type', 'source_id', 'target_id', 'qualification', 'fields') if collection == 'relations'
            else ('name', 'definition', 'finality', 'scope', 'nature'))
        record = {'id': item['id'], 'kind': item.get('kind'),
                  'fields': values if requested == ['*'] else {key: values[key] for key in requested if key in values},
                  'source_refs': item.get('source_refs', []),
                  'lifecycle': item.get('lifecycle'), 'review': item.get('review')}
        if collection == 'nodes':
            edges = model.get('relations', [])
            record['parents'] = [{'id': edge['source_id'], 'relation_id': edge['id'], 'type': edge['type']}
                                 for edge in edges if edge.get('target_id') == item['id'] and edge['type'] in ('contains', 'presents')]
            record['children'] = [{'id': edge['target_id'], 'relation_id': edge['id'], 'type': edge['type']}
                                  for edge in edges if edge.get('source_id') == item['id'] and edge['type'] in ('contains', 'presents')]
            if relations:
                record['relations'] = [edge for edge in edges if item['id'] in (edge.get('source_id'), edge.get('target_id'))]
        results.append(record)
    return {'source': path.relative_to(root).as_posix(), 'space': space, 'version': model.get('version'),
            'collection': collection, 'total_matches': len(matches), 'returned': len(results),
            'next_offset': offset+limit if not ids and offset+limit < len(matches) else None, 'items': results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ids', nargs='*')
    parser.add_argument('--space', choices=('backlog', 'release'), default='backlog')
    parser.add_argument('--version')
    parser.add_argument('--collection', choices=('nodes', 'relations', 'terms'), default='nodes')
    parser.add_argument('--fields', nargs='+', help='Noms exacts des champs ; * pour tous les champs de la fiche.')
    parser.add_argument('--query', default='')
    parser.add_argument('--limit', type=int, default=20)
    parser.add_argument('--offset', type=int, default=0)
    parser.add_argument('--relations', action='store_true')
    args = vars(parser.parse_args())
    try:
        print(json.dumps(inspect(**args), ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError) as error:
        parser.exit(1, str(error)+'\n')


if __name__ == '__main__': main()

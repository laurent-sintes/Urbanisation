"""Record an explicitly scoped agreement now; bind it to a release only later.

The live annex is append-only. Neither lifecycle metadata nor a release operation
creates an agreement. Semantic changes make an unmaterialized intent stale.
"""
import argparse
from copy import deepcopy
from datetime import date
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import tempfile

try:
    from .structured_io import read, loads, dumps, working_path
except ImportError:
    from structured_io import read, loads, dumps, working_path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = '1.0.0'
REGISTRY_PATH = 'modeles/backlog/decision-intents.yaml'
METADATA = frozenset({
    'lifecycle', 'review', 'field_review', 'field_status', 'source_refs', 'correction_refs',
    'source_locator', 'source_files', 'source_version', 'source_path', 'sourcePath',
    'revision', 'version', 'as_of', 'last_modified', 'content_sha256', 'schema_version',
    'adoption_ids', 'approved_fields', 'proposed_fields', 'missing_fields',
    'validated_fields', 'recorded_at', 'recorded_by', 'decided_at', 'published_at',
    'captured_at', 'consulted_on', 'created_at', 'updated_at',
})
INTENT_KEYS = {'id', 'author', 'decided_at', 'recorded_at', 'interpretation', 'reviewer',
               'source_refs', 'note', 'target'}
TARGET_KEYS = {'collection', 'id', 'approved_fields', 'values', 'value_sha256',
               'context', 'context_sha256'}


def canonical_sha256(value):
    return sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                             separators=(',', ':'), allow_nan=False).encode('utf-8')).hexdigest()


def _text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(label + ' must be a nonempty string')
    return value


def _date(value, label):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        raise ValueError(label + ' must use YYYY-MM-DD')
    try:
        date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(label + ' is not a valid date') from error
    return value


def _strings(values, label):
    if not isinstance(values, list) or not values:
        raise ValueError(label + ' must be a nonempty list')
    for value in values:
        _text(value, label)
    if len(set(values)) != len(values):
        raise ValueError(label + ' must contain unique values')
    return values


def _nonempty(value):
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (dict, list)):
        return bool(value)
    return True  # False and zero are meaningful business values.


def _records(values, label):
    if not isinstance(values, list):
        raise ValueError(label + ' must be a list')
    result = {}
    for value in values:
        if not isinstance(value, dict):
            raise ValueError(label + ' contains an invalid record')
        identifier = _text(value.get('id'), label + ' id')
        if identifier in result:
            raise ValueError(label + ' contains duplicate id: ' + identifier)
        result[identifier] = value
    return result


def _source_ids(sources):
    if not isinstance(sources, dict):
        raise ValueError('sources must be a registry or an ID-to-record mapping')
    if 'records' in sources:
        return set(_records(sources['records'], 'sources'))
    if any(not isinstance(record, dict) or record.get('id', identifier) != identifier
           for identifier, record in sources.items()):
        raise ValueError('Invalid source mapping')
    for identifier in sources:
        _text(identifier, 'source id')
    return set(sources)


def semantic(value):
    """Ignore editorial provenance and generated revisions, never business prose."""
    if isinstance(value, dict):
        return {key: semantic(item) for key, item in value.items() if key not in METADATA}
    if isinstance(value, list):
        return [semantic(item) for item in value]
    return deepcopy(value)


def semantic_context(snapshot, collection, target_id):
    """Capture a conservative neighborhood plus all principles and glossary terms."""
    if collection not in ('nodes', 'relations'):
        raise ValueError('collection must be nodes or relations')
    nodes = _records(snapshot.get('nodes'), 'nodes')
    relations = _records(snapshot.get('relations'), 'relations')
    target = (nodes if collection == 'nodes' else relations).get(target_id)
    if target is None:
        raise ValueError('Unknown target: ' + collection + '/' + target_id)
    anchors = {target_id} if collection == 'nodes' else {target.get('source_id'), target.get('target_id')}
    incident = {key: relation for key, relation in relations.items()
                if relation.get('source_id') in anchors or relation.get('target_id') in anchors}
    neighbors = anchors | {relation.get(key) for relation in incident.values()
                           for key in ('source_id', 'target_id')}
    # Moving the Area or Domain changes the meaning of a capability's context
    # even when the capability and its immediate membership edge are untouched.
    pending = list(neighbors)
    while pending:
        identifier = pending.pop()
        for key, relation in relations.items():
            if relation.get('type') in ('contains', 'presents') and relation.get('target_id') == identifier:
                incident[key] = relation
                parent = relation.get('source_id')
                if parent not in neighbors:
                    neighbors.add(parent)
                    pending.append(parent)
    if None in neighbors or neighbors - nodes.keys():
        raise ValueError('Semantic context has an unknown relation endpoint')
    return {
        'target': semantic(target),
        'incident_relations': {key: semantic(value) for key, value in sorted(incident.items())},
        'related_nodes': {key: semantic(nodes[key]) for key in sorted(neighbors)
                          if collection != 'nodes' or key != target_id},
        'principles': semantic(snapshot.get('principles', [])),
        'glossary': semantic(snapshot.get('glossary', {})),
    }


def _values(snapshot, collection, target_id, fields):
    if collection not in ('nodes', 'relations'):
        raise ValueError('collection must be nodes or relations')
    target = _records(snapshot.get(collection), collection).get(target_id)
    if target is None:
        raise ValueError('Unknown target: ' + collection + '/' + target_id)
    available = target.get('fields', {}) if collection == 'nodes' else target
    values = {}
    for field in _strings(fields, 'fields'):
        if field in METADATA:
            raise ValueError('Cannot approve editorial metadata: ' + field)
        if field not in available or not _nonempty(available[field]):
            raise ValueError('Selected field is absent or empty: ' + target_id + '.' + field)
        values[field] = deepcopy(available[field])
    return values


def validate_document(document, sources=None):
    """Strict annex contract, including internal value/context integrity."""
    if (not isinstance(document, dict) or set(document) not in ({'schema_version', 'intents'}, {'schema_version', 'intents', 'suspensions'})
            or document.get('schema_version') != SCHEMA_VERSION):
        raise ValueError('Decision intent registry must use strict schema_version 1.0.0')
    intents = _records(document.get('intents'), 'intents')
    known = _source_ids(sources) if sources is not None else None
    for intent in intents.values():
        if set(intent) not in (INTENT_KEYS, INTENT_KEYS | {'supersedes'}):
            raise ValueError('Invalid intent keys: ' + intent['id'])
        if 'supersedes' in intent:
            _text(intent['supersedes'], 'supersedes')
            if intent['supersedes'] == intent['id']:
                raise ValueError('An intent cannot supersede itself')
        for field in ('author', 'reviewer', 'note'):
            _text(intent[field], field)
        for field in ('decided_at', 'recorded_at'):
            _date(intent[field], field)
        if intent['interpretation'] not in ('explicit', 'contextual'):
            raise ValueError('interpretation must be explicit or contextual')
        refs = _strings(intent['source_refs'], 'source_refs')
        if known is not None and set(refs) - known:
            raise ValueError('Unknown decision sources: ' + ', '.join(sorted(set(refs) - known)))
        target = intent['target']
        if not isinstance(target, dict) or set(target) != TARGET_KEYS:
            raise ValueError('Invalid intent target: ' + intent['id'])
        _text(target['id'], 'target id')
        if target['collection'] not in ('nodes', 'relations'):
            raise ValueError('collection must be nodes or relations')
        fields = _strings(target['approved_fields'], 'approved_fields')
        if any(field in METADATA for field in fields):
            raise ValueError('Cannot approve editorial metadata')
        for key in ('values', 'value_sha256'):
            if not isinstance(target[key], dict) or set(target[key]) != set(fields):
                raise ValueError('Intent field capture mismatch: ' + intent['id'])
        if any(not _nonempty(target['values'][field]) or
               canonical_sha256(target['values'][field]) != target['value_sha256'][field] for field in fields):
            raise ValueError('Intent value hash mismatch: ' + intent['id'])
        context = target['context']
        if (not isinstance(context, dict) or set(context) !=
                {'target', 'incident_relations', 'related_nodes', 'principles', 'glossary'}
                or canonical_sha256(context) != target['context_sha256']):
            raise ValueError('Intent context hash mismatch: ' + intent['id'])
    seen = set()
    for entry in document.get('suspensions', []):
        if not isinstance(entry, dict) or set(entry) != {'intent_id', 'reviewer', 'reviewed_at', 'source_refs', 'rationale'}:
            raise ValueError('Invalid intent suspension')
        identifier = entry['intent_id']
        if identifier not in intents or identifier in seen:
            raise ValueError('Unknown or duplicate suspended intent: ' + str(identifier))
        seen.add(identifier)
        _text(entry['reviewer'], 'suspension reviewer')
        _text(entry['rationale'], 'suspension rationale')
        _date(entry['reviewed_at'], 'suspension reviewed_at')
        refs = _strings(entry['source_refs'], 'suspension source_refs')
        if known is not None and set(refs) - known:
            raise ValueError('Unknown suspension sources')
    return document


def make_intent(snapshot, sources, *, intent_id, collection, target_id, fields,
                source_refs, author, decided_at, interpretation, note, reviewer,
                recorded_at=None, supersedes=None):
    _text(intent_id, 'id')
    _text(target_id, 'target id')
    fields = sorted(_strings(fields, 'fields'))
    source_refs = sorted(_strings(source_refs, 'source_refs'))
    values = _values(snapshot, collection, target_id, fields)
    context = semantic_context(snapshot, collection, target_id)
    intent = {
        'id': intent_id, 'author': author, 'decided_at': decided_at,
        'recorded_at': recorded_at or date.today().isoformat(),
        'interpretation': interpretation, 'reviewer': reviewer,
        'source_refs': source_refs, 'note': note,
        'target': {'collection': collection, 'id': target_id, 'approved_fields': fields,
                   'values': values, 'value_sha256': {key: canonical_sha256(value) for key, value in values.items()},
                   'context': context, 'context_sha256': canonical_sha256(context)},
    }
    if supersedes is not None:
        intent['supersedes'] = supersedes
    validate_document({'schema_version': SCHEMA_VERSION, 'intents': [intent]}, sources)
    return intent


def superseded_intents(document):
    """Explicit replacements preserve the old proof and cannot broaden its fields."""
    seen, replaced = {}, set()
    for intent in document['intents']:
        predecessor = intent.get('supersedes')
        if predecessor is not None:
            if predecessor not in seen or predecessor in replaced:
                raise ValueError('Supersedes must name an earlier, unreplaced intent: ' + predecessor)
            old, new = seen[predecessor]['target'], intent['target']
            if ((old['collection'], old['id']) != (new['collection'], new['id'])
                    or not set(new['approved_fields']).issubset(old['approved_fields'])):
                raise ValueError('Replacement must keep the target and not broaden approved fields')
            replaced.add(predecessor)
        seen[intent['id']] = intent
    return replaced


def _historical_match(intent, decision):
    if decision.get('decision_state') != 'accepted':
        return False
    if any(intent[key] != decision.get(key) for key in
           ('id', 'author', 'decided_at', 'recorded_at', 'interpretation', 'note')):
        return False
    if sorted(intent['source_refs']) != sorted(decision.get('source_refs', [])):
        return False
    target, historical = intent['target'], decision.get('target', {})
    return (all(target[key] == historical.get(key) for key in ('collection', 'id', 'value_sha256'))
            and sorted(target['approved_fields']) == sorted(historical.get('approved_fields', [])))


def compile_intents(document, snapshot, active_decisions, sources, consumed_document=None):
    """Return only new decisions; known IDs never reapprove a later revision.

    Pass every decision and the frozen intent annex from the base publication.
    The latter prevents resurrection after automatic carry or explicit review
    has replaced the original decision ID in subsequent publication cycles.
    """
    validate_document(document, sources)
    current_intents = {intent['id']: intent for intent in document['intents']}
    consumed = {}
    if consumed_document is not None:
        validate_document(consumed_document, sources)
        consumed = {intent['id']: intent for intent in consumed_document['intents']}
        for identifier, intent in consumed.items():
            if current_intents.get(identifier) != intent:
                raise ValueError('Consumed decision intent was removed or changed: ' + identifier)
    version = _text(snapshot.get('version'), 'snapshot version')
    historical = _records(active_decisions.get('decisions') if isinstance(active_decisions, dict)
                          else active_decisions, 'active decisions')
    suspended = {entry['intent_id']: entry for entry in document.get('suspensions', [])}
    old_suspended = {entry['intent_id']: entry for entry in (consumed_document or {}).get('suspensions', [])}
    for identifier, entry in old_suspended.items():
        if suspended.get(identifier) != entry:
            raise ValueError('Consumed intent suspension was removed or changed: ' + identifier)
    for identifier in suspended.keys() - old_suspended.keys():
        if identifier in consumed or identifier in historical:
            raise ValueError('Published intents require the publication review workflow, not suspension')
    replaced = superseded_intents(document)
    for intent in document['intents']:
        if (intent.get('supersedes') in consumed or intent.get('supersedes') in historical):
            if intent['id'] not in consumed and intent['id'] not in historical:
                raise ValueError('Published intents require the publication review workflow, not supersedes')
    decisions = []
    for intent in document['intents']:
        identifier, target = intent['id'], intent['target']
        if identifier in historical:
            if not _historical_match(intent, historical[identifier]):
                raise ValueError('Decision intent ID conflicts with a historical decision: ' + identifier)
            continue
        if identifier in consumed:
            continue
        if identifier in replaced or identifier in suspended:
            continue
        try:
            values = _values(snapshot, target['collection'], target['id'], target['approved_fields'])
            context = semantic_context(snapshot, target['collection'], target['id'])
        except ValueError as error:
            raise ValueError('Stale decision intent ' + identifier + ': ' + str(error)) from error
        if any(canonical_sha256(value) != target['value_sha256'][field] for field, value in values.items()):
            raise ValueError('Stale decision intent ' + identifier + ': approved values changed')
        if canonical_sha256(context) != target['context_sha256']:
            raise ValueError('Stale decision intent ' + identifier + ': semantic context changed')
        item = _records(snapshot[target['collection']], target['collection'])[target['id']]
        revision = item.get('revision')
        if type(revision) is not int or revision < 1:
            raise ValueError('Final target revision is missing or invalid: ' + target['id'])
        decision = {key: deepcopy(intent[key]) for key in
                    ('id', 'author', 'decided_at', 'recorded_at', 'interpretation', 'source_refs', 'note')}
        decision['decision_state'] = 'accepted'
        decision['target'] = {'collection': target['collection'], 'id': target['id'], 'revision': revision,
                              'approved_fields': deepcopy(target['approved_fields']),
                              'value_sha256': deepcopy(target['value_sha256']), 'import_version': version}
        decisions.append(decision)
    return {'schema_version': SCHEMA_VERSION, 'version': version, 'decisions': decisions}


def record_intent(root=ROOT, **parameters):
    """Atomically append one scoped agreement, without editing the live model."""
    return record_intents(root, [parameters])[0]


def record_intents(root, parameters):
    """Capture a reviewed batch against one final snapshot and write it once."""
    if not parameters:
        raise ValueError('At least one intent is required')
    root = Path(root).resolve()
    path = root / REGISTRY_PATH
    if not path.parent.is_dir():
        raise ValueError('Missing backlog directory: ' + str(path.parent))
    snapshot = read(working_path(path.parent))
    glossary_path = working_path(path.parent, 'glossary')
    if glossary_path.exists():
        snapshot['glossary'] = read(glossary_path)
    sources = read(root / 'modeles/provenance/source-records.json')
    before = path.read_bytes() if path.exists() else None
    document = loads(before.decode('utf-8-sig')) if before is not None else {'schema_version': SCHEMA_VERSION, 'intents': []}
    validate_document(document, sources)
    results = []
    for params in parameters:
        existing = next((item for item in document['intents'] if item['id'] == params.get('intent_id')), None)
        intent = make_intent(snapshot, sources, **params,
                             recorded_at=existing['recorded_at'] if existing else None)
        if existing and existing != intent:
            raise ValueError('Decision intent ID already exists with different content: ' + intent['id'])
        results.append({'recorded': existing is None, 'path': str(path), 'intent': intent})
        if existing is None:
            document['intents'].append(intent)
    superseded_intents(document)
    if not any(result['recorded'] for result in results):
        return results
    content = dumps(document).encode('utf-8')
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(mode='wb', dir=path.parent, prefix='.decision-intents-', suffix='.tmp', delete=False) as stream:
            temp_path = Path(stream.name)
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        if (path.read_bytes() if path.exists() else None) != before:
            raise ValueError('Decision intent registry changed concurrently; retry with the current registry')
        os.replace(temp_path, path)
    finally:
        if temp_path is not None and temp_path.exists():
            temp_path.unlink()
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--id', dest='intent_id', required=True)
    parser.add_argument('--collection', choices=('nodes', 'relations'), required=True)
    parser.add_argument('--target', dest='target_id', required=True)
    parser.add_argument('--fields', action='append', required=True)
    parser.add_argument('--source', dest='source_refs', action='append', required=True)
    parser.add_argument('--author', required=True)
    parser.add_argument('--decided-at', required=True)
    parser.add_argument('--interpretation', choices=('explicit', 'contextual'), required=True)
    parser.add_argument('--note', required=True)
    parser.add_argument('--reviewer', required=True)
    parser.add_argument('--supersedes', help='Earlier unpublished intent explicitly re-examined; same target and fields or subset')
    arguments = vars(parser.parse_args(argv))
    try:
        result = record_intent(**arguments)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print(json.dumps({'recorded': result['recorded'], 'path': result['path'], 'id': result['intent']['id']}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

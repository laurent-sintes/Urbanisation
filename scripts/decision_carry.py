"""Conservative context comparison for carrying an existing, unchanged approval.

Only explicitly identified editorial metadata and market documentation are ignored.
Business fields, unknown content and the local graph context remain significant.
This module never creates an approval or changes its scope.
"""

from copy import deepcopy

try:
    from .element_versions import GENERATED
    from .glossary import references
    from .validate_models import canonical_sha256
except ImportError:
    from element_versions import GENERATED
    from glossary import references
    from validate_models import canonical_sha256


EDITORIAL_METADATA = GENERATED | {
    'source_refs', 'correction_refs', 'source_locator', 'review', 'lifecycle',
    'editorial_basis',
}
MARKET_FIELDS = {'market_comparisons', 'market_inspiration'}
ROOT_METADATA = EDITORIAL_METADATA | {
    'version', 'as_of', 'space', 'source_version', 'source_files', 'publication',
    'release_kind', 'excluded_nodes',
}


def business_record(record):
    """Strip only known metadata at record boundaries; retain unknown fields."""
    if not isinstance(record, dict):
        return deepcopy(record)
    result = {key: deepcopy(value) for key, value in record.items()
              if key not in EDITORIAL_METADATA | MARKET_FIELDS}
    if isinstance(result.get('fields'), dict):
        result['fields'] = {key: value for key, value in result['fields'].items()
                            if key not in MARKET_FIELDS}
    if isinstance(result.get('qualification'), dict):
        result['qualification'] = {key: value for key, value in result['qualification'].items()
                                   if key not in {'source_refs', 'correction_refs'}}
    return result


def _index(records):
    result = {}
    for item in records:
        if not isinstance(item, dict) or not isinstance(item.get('id'), str) or item['id'] in result:
            raise ValueError('Invalid or duplicate context identifier')
        result[item['id']] = item
    return result


def _model_context(snapshot, seed_ids):
    nodes = _index(snapshot.get('nodes', []))
    relations = _index(snapshot.get('relations', []))
    selected = set(seed_ids)
    incident = {identifier: relation for identifier, relation in relations.items()
                if relation.get('source_id') in seed_ids or relation.get('target_id') in seed_ids}
    for relation in incident.values():
        selected.update(relation[key] for key in ('source_id', 'target_id'))
    # Explicit model links carry business meaning even without a graph edge.
    for value in [nodes.get(identifier, {}) for identifier in seed_ids] + list(incident.values()):
        selected.update(target for kind, target in references(business_record(value)) if kind == 'model')
    # A Domain/Area move changes context even when the capability itself is untouched.
    pending = list(selected)
    while pending:
        identifier = pending.pop()
        for edge_id, relation in relations.items():
            if relation.get('type') not in ('contains', 'presents') or relation.get('target_id') != identifier:
                continue
            incident[edge_id] = relation
            parent = relation['source_id']
            if parent not in selected:
                selected.add(parent)
                pending.append(parent)
    return ({identifier: business_record(nodes.get(identifier)) for identifier in selected},
            {identifier: business_record(relation) for identifier, relation in incident.items()})


def _glossary_context(snapshot, context):
    glossary = snapshot.get('glossary', {})
    terms = _index(glossary.get('terms', []))
    selected, pending = {}, [context]
    while pending:
        for kind, identifier in references(pending.pop()):
            if kind != 'glossary' or identifier in selected:
                continue
            selected[identifier] = business_record(terms.get(identifier))
            if selected[identifier] is not None:
                pending.append(selected[identifier])
    return selected


def classify_context(original, previous_snapshot, snapshot):
    """Return ``{safe: bool, reasons: list[str]}`` without mutating any input.

    Safety requires the original approved values and their local context to be
    unchanged. Context includes direct neighbors, membership ancestors, incident
    relations, global principles and transitively referenced glossary terms.
    """
    reasons = []
    try:
        target = original['target']
        collection, identifier = target['collection'], target['id']
        if collection not in ('nodes', 'relations') or original.get('decision_state') != 'accepted':
            return {'safe': False, 'reasons': ['decision_not_accepted_or_supported']}
        before = _index(previous_snapshot.get(collection, []))
        after = _index(snapshot.get(collection, []))
        if identifier not in before or identifier not in after:
            return {'safe': False, 'reasons': ['target_missing']}
        old, new = before[identifier], after[identifier]
        if old.get('revision') != target['revision']:
            reasons.append('prior_revision_mismatch')
        old_values = old.get('fields', {}) if collection == 'nodes' else old
        new_values = new.get('fields', {}) if collection == 'nodes' else new
        approved = target['approved_fields']
        if (not isinstance(approved, list) or not approved
                or any(not isinstance(field, str) for field in approved)
                or len(set(approved)) != len(approved)
                or set(approved) != set(target['value_sha256'])):
            return {'safe': False, 'reasons': ['invalid_approved_scope']}
        if any(field not in old_values or field not in new_values
               or canonical_sha256(old_values[field]) != target['value_sha256'][field]
               or canonical_sha256(new_values[field]) != target['value_sha256'][field]
               for field in approved):
            reasons.append('approved_values_changed_or_unverified')
        if business_record(old) != business_record(new):
            reasons.append('target_business_changed')
        seeds = {identifier} if collection == 'nodes' else {
            value[key] for value in (old, new) for key in ('source_id', 'target_id')
        }
        old_nodes, old_relations = _model_context(previous_snapshot, seeds)
        new_nodes, new_relations = _model_context(snapshot, seeds)
        if old_nodes != new_nodes:
            reasons.append('neighbor_or_ancestor_business_changed')
        if old_relations != new_relations:
            reasons.append('incident_or_membership_relation_changed')
        if any(value is None for value in [*old_nodes.values(), *new_nodes.values()]):
            reasons.append('context_node_missing')
        old_principles = {key: business_record(value) for key, value in _index(previous_snapshot.get('principles', [])).items()}
        new_principles = {key: business_record(value) for key, value in _index(snapshot.get('principles', [])).items()}
        if old_principles != new_principles:
            reasons.append('principles_changed')
        # Unknown root/glossary properties are significant by default.
        root_context = lambda model: {key: value for key, value in model.items()
                                      if key not in ROOT_METADATA | {'nodes', 'relations', 'principles', 'glossary'}}
        if root_context(previous_snapshot) != root_context(snapshot):
            reasons.append('global_business_context_changed')
        glossary_header = lambda model: business_record({key: value for key, value in model.get('glossary', {}).items()
                                                        if key not in {'terms', 'version', 'as_of', 'source_files'}})
        old_terms = _glossary_context(previous_snapshot, [old_nodes, old_relations, old_principles])
        new_terms = _glossary_context(snapshot, [new_nodes, new_relations, new_principles])
        # A first catalogue or an unrelated catalogue header does not redefine
        # an approval whose business context contains no explicit term links.
        if (old_terms or new_terms) and glossary_header(previous_snapshot) != glossary_header(snapshot):
            reasons.append('glossary_context_changed')
        if old_terms != new_terms:
            reasons.append('referenced_glossary_changed')
        if any(value is None for value in [*old_terms.values(), *new_terms.values()]):
            reasons.append('referenced_glossary_missing')
    except (KeyError, TypeError, ValueError, AttributeError):
        reasons.append('invalid_context')
    return {'safe': not reasons, 'reasons': reasons or ['unchanged_business_context']}

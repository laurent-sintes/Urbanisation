"""Lifecycle labels and evidence checks, distinct from publication and field approval."""
import hashlib
import json
from datetime import datetime

LABELS = {'ai_proposed': 'Proposé par l’IA', 'under_instruction': 'En cours d’instruction',
          'urbanist_validated': 'Validé par l’urbaniste'}


def value_hash(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def validate_lifecycle(item):
    cycle = item.get('lifecycle')
    if cycle is None:  # Historical models retain their original vocabulary.
        return []
    errors = []
    label = 'lifecycle/' + item['id']
    if cycle.get('state') not in LABELS:
        errors.append(label + ': unknown state')
    try:
        datetime.fromisoformat(cycle['recorded_at'].replace('Z', '+00:00'))
    except (KeyError, ValueError, TypeError):
        errors.append(label + ': invalid recorded_at')
    # Relation approvals concern top-level endpoints/qualification, even when an
    # optional fields object carries their presentation label.
    values = item if 'source_id' in item and 'target_id' in item else item.get('fields', item)
    scope = cycle.get('validated_fields', [])
    hashes = cycle.get('value_sha256', {})
    if set(scope) != set(hashes):
        errors.append(label + ': validation scope and hashes differ')
    for field in scope:
        if field not in values or value_hash(values[field]) != hashes[field]:
            errors.append(label + ': approved value changed: ' + field)
    if cycle.get('state') == 'urbanist_validated' and not scope:
        errors.append(label + ': urbanist validation requires an explicit scope')
    if cycle.get('state') == 'ai_proposed' and scope:
        errors.append(label + ': AI proposal cannot claim approved fields')
    return errors


def lifecycle_label(item):
    return LABELS.get(item.get('lifecycle', {}).get('state'))

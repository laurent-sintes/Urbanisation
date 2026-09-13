"""Automatic element revisions in prepared snapshots; never edit historical files."""
from datetime import datetime, timezone
import hashlib
import json

COLLECTIONS = ('nodes', 'relations', 'principles')
GENERATED = {'revision', 'last_modified', 'content_sha256', 'adoption_ids',
             'approved_fields', 'proposed_fields', 'missing_fields'}


def content_hash(item):
    value = {k: v for k, v in item.items() if k not in GENERATED}
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def assign_versions(snapshot, previous, now=None, published=None):
    """Version submitted content before publication derives validation notes.

    content_sha256 retains this input fingerprint so derived notes do not cause
    artificial revisions on subsequent publications of unchanged working data.
    A first timestamp records when version tracking began, not an invented past.
    """
    stamp = now or datetime.now(timezone.utc).isoformat(timespec='microseconds').replace('+00:00', 'Z')
    changes = []
    for collection in COLLECTIONS:
        before = {item['id']: item for item in previous.get(collection, [])}
        visible = {item['id']: item for item in (published or {}).get(collection, [])}
        for item in snapshot.get(collection, []):
            old = before.get(item['id'])
            fingerprint = content_hash(item)
            # Legacy snapshots may precede derived published review states.
            # Bootstrap against the actual published element when no input hash exists.
            baseline = visible.get(item['id'], old) if old else None
            previous_hashes = {old['content_sha256']} if old and 'content_sha256' in old else ({content_hash(old), content_hash(baseline)} if old else set())
            changed = old is not None and fingerprint not in previous_hashes
            revision = (old.get('revision', 1) + int(changed)) if old else 1
            item.update(revision=revision, last_modified=old.get('last_modified', stamp) if old and not changed else stamp,
                        content_sha256=fingerprint)
            if not old or changed or 'last_modified' not in old:
                changes.append({'collection': collection, 'id': item['id'], 'revision': revision,
                                'last_modified': item['last_modified'],
                                'reason': 'new' if not old else 'changed' if changed else 'tracking_initialized'})
    root_value = {'model_id': snapshot['model_id'], 'limitations': snapshot.get('limitations', []),
                  'elements': {c: [(e['id'], e['content_sha256']) for e in snapshot.get(c, [])] for c in COLLECTIONS}}
    fingerprint = content_hash(root_value)
    changed = fingerprint != previous.get('content_sha256')
    revision = previous.get('revision', 0) + int(changed)
    snapshot.update(element_versioning=1, revision=max(1, revision), content_sha256=fingerprint,
                    last_modified=stamp if changed else previous['last_modified'])
    return changes

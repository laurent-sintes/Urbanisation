"""One-time migration: retire only tracked, byte-identical historical artifacts."""
import hashlib
import json
from pathlib import Path
import re

from . import git_history
from .structured_io import read, dumps
from .release_catalog import resolve_release
from .decision_registry import is_index, load_entry


def migrate(root, apply=False):
    root = Path(root).resolve()
    resume = git_history.enabled(root)
    commit = git_history.git(root, 'rev-parse', 'HEAD').decode().strip()
    tracked = {}
    for record in git_history.git(root, 'ls-tree', '-rz', 'HEAD').split(b'\0'):
        if record:
            meta, name = record.split(b'\t', 1)
            tracked[name.decode('utf-8')] = meta.split()[2].decode()
    pointer = resolve_release(root / 'modeles/release')
    version = pointer['version']
    manifest_path = root / f'modeles/release/{version}/manifest.json'
    manifest = read(manifest_path)
    keep = {f'modeles/release/{version}/{name}' for name in ('model.yaml', 'manifest.json', 'release-notes.md')}
    keep.update((manifest_path.parent / manifest[key + '_path']).resolve().relative_to(root).as_posix()
                for key in ('input_revision', 'decisions', 'provenance'))
    registry_path = root / 'modeles/backlog/decision-intents.yaml'
    registry = read(registry_path)
    if resume:
        if manifest.get('migration_origin', {}).get('commit') != commit:
            raise ValueError('Migration base changed')
        pending = registry['intents']
        pending_ids = {i['id'] for i in pending}
    else:
        consumed = read(root / f'modeles/revisions/{version}/deferred/decision-intents.yaml')
        if not is_index(registry) or not is_index(consumed):
            raise ValueError('Migration expects the current indexed registry')
        consumed_entries = {e['id']: e for e in consumed['entries']}
        pending = []
        for entry in registry['entries']:
            previous = consumed_entries.get(entry['id'])
            if previous:
                if previous['sha256'] != entry['sha256']:
                    raise ValueError('Consumed capture changed: ' + entry['id'])
            else:
                pending.append(load_entry(registry_path, entry))
        if set(consumed_entries) - {e['id'] for e in registry['entries']}:
            raise ValueError('Consumed captures missing')
        # Preserve any still-pending supersession chain; migration never evaluates approval.
        pending_ids = {i['id'] for i in pending}
        if any(i.get('supersedes') and i['supersedes'] not in pending_ids for i in pending):
            raise ValueError('Pending supersession depends on a published capture')
    prefixes = {'audits', 'modeles/backlog/history', 'modeles/backlog/decision-intents'}
    for name in tracked:
        match = re.match(r'(modeles/(?:release|revisions|provenance)/\d{4}-\d{2}-\d{2}\.[1-9]\d*)/', name)
        if match:
            prefixes.add(match[1])
        if re.fullmatch(r'modeles/decisions/\d{4}-\d{2}-\d{2}\.[1-9]\d*\.json', name):
            prefixes.add(name)
    retiring = [name for name in tracked if (root / name).is_file() and name not in keep and any(name == p or name.startswith(p + '/') for p in prefixes)]
    # Verify all bytes before the first deletion, including the live captures.
    originals = [] if resume else [registry_path.relative_to(root).as_posix(), manifest_path.relative_to(root).as_posix()]
    for name in retiring + originals:
        content = (root / name).read_bytes()
        oid = hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest()
        if tracked.get(name) != oid:
            raise ValueError('Uncommitted artifact: ' + name)
    allowed = re.compile(r'^(?:audits/|modeles/backlog/(?:history|decision-intents)/|modeles/(?:release|revisions|provenance)/[0-9]{4}-[0-9]{2}-[0-9]{2}\.[1-9][0-9]*/|modeles/decisions/[0-9]{4}-[0-9]{2}-[0-9]{2}\.[1-9][0-9]*\.json$)')
    if any(not allowed.match(name) for name in retiring):
        raise ValueError('Retirement outside explicit historical allowlist')
    if not apply:
        from collections import Counter
        return {'dry_run': True, 'files': len(retiring),
                'bytes': sum((root / p).stat().st_size for p in retiring),
                'groups': dict(Counter('/'.join(p.split('/')[:2]) for p in retiring)),
                'preserved_current_files': sorted(keep),
                'code_business_sources_and_market_eligible': False}
    index = {'schema_version': '1.0.0', 'archives': [{'path': p, 'commit': commit} for p in sorted(prefixes)]}
    (root / git_history.INDEX).write_text(json.dumps(index, indent=2) + '\n', encoding='utf-8')
    new_registry = {'schema_version': '1.0.0', 'intents': pending,
                    'suspensions': [s for s in registry.get('suspensions', []) if s['intent_id'] in pending_ids]}
    registry_path.write_text(dumps(new_registry), encoding='utf-8')
    # Business snapshot and decision bytes are preserved. Only storage metadata changes.
    manifest['kind'] = 'git_release'
    for key in ('decision_review', 'decision_registry_files', 'prepared_manifest_sha256'):
        manifest.pop(key, None)
    manifest['migration_origin'] = {'commit': commit, 'path': manifest_path.relative_to(root).as_posix()}
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    retired_bytes = 0
    for name in retiring:
        path = (root / name).resolve()
        if not path.is_relative_to(root) or path == root:
            raise ValueError('Unsafe migration path')
        retired_bytes += path.stat().st_size
        path.unlink()
    return {'base_commit': commit, 'retired_files': len(retiring), 'retired_bytes': retired_bytes,
            'pending_intents': len(pending), 'version': version}


if __name__ == '__main__':
    import sys
    print(json.dumps(migrate(Path(__file__).resolve().parents[1], apply='--apply' in sys.argv), indent=2))

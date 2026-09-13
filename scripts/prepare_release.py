"""Compare live backlog, prepare an immutable candidate, then publish explicitly.

report is read-only. prepare writes only modeles/staging/<version>. publish copies
verified staged inputs into the permanent history; --activate changes the local
pointer last. Neither operation grants a business validation.
"""
import argparse
import copy
from datetime import date
import json
import os
from pathlib import Path
import re
import shutil
import sys
import uuid

try:
    from .element_versions import assign_versions
    from .release_catalog import resolve_release, register
    from . import publish_release as publisher
    from .json_contract import validate as validate_contract
    from .validate_models import canonical_sha256, validate_release, validate_sources, validate_urbanism
except ImportError:
    from element_versions import assign_versions
    from release_catalog import resolve_release, register
    import publish_release as publisher
    from json_contract import validate as validate_contract
    from validate_models import canonical_sha256, validate_release, validate_sources, validate_urbanism

ROOT = Path(__file__).resolve().parents[1]
read, digest, write = publisher.read, publisher.digest, publisher.write
PUBLICATION_FIELDS = {'adoption_ids', 'approved_fields', 'proposed_fields', 'missing_fields'}


def checked_path(base, relative):
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError('Path escapes its intended directory: ' + str(relative))
    return path


def valid_version(version):
    if not isinstance(version, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}\.[1-9]\d*', version):
        raise ValueError('Version must use YYYY-MM-DD.N with a positive sequence number')
    date.fromisoformat(version.split('.')[0])
    return version


def references(document):
    found = set()
    if isinstance(document, dict):
        for key, value in document.items():
            if key in ('source_refs', 'correction_refs'):
                found.update(value)
            else:
                found.update(references(value))
    elif isinstance(document, list):
        for value in document:
            found.update(references(value))
    return found


def load_current(root):
    models = (Path(root).resolve() / 'modeles').resolve()
    pointer = resolve_release(models / 'release')
    release_path = checked_path(models / 'release', pointer['path'])
    if digest(release_path) != pointer['sha256']:
        raise ValueError('Current release pointer hash mismatch')
    release = read(release_path)
    manifest_path = release_path.parent / 'manifest.json'
    manifest = read(manifest_path)
    if (manifest['model_sha256'] != pointer['sha256'] or manifest['version'] != pointer['version']
            or release['version'] != pointer['version']):
        raise ValueError('Current release manifest/version mismatch')
    inputs = {}
    for key in ('input_revision', 'decisions', 'provenance'):
        path = (manifest_path.parent / manifest[key + '_path']).resolve()
        if not path.is_relative_to(models) or digest(path) != manifest[key + '_sha256']:
            raise ValueError('Frozen input path or hash mismatch: ' + key)
        inputs[key] = read(path)
    errors = validate_release(release, inputs['decisions'], inputs['input_revision'],
                              {r['id']: r for r in inputs['provenance']['records']},
                              read(models / 'schemas/urbanism.schema.json'))
    if errors:
        raise ValueError('\n'.join(errors))
    return models, pointer, release, inputs, manifest_path


def suggested_version(models):
    prefix = date.today().isoformat() + '.'
    used = set()
    for folder in ('release', 'revisions', 'staging', 'provenance'):
        base = models / folder
        if base.exists():
            used.update(p.name for p in base.iterdir())
    number = 1
    while prefix + str(number) in used or (models / 'decisions' / (prefix + str(number) + '.json')).exists():
        number += 1
    return prefix + str(number)


def reconcile_decisions(old_document, snapshot, additional=None, previous_snapshot=None):
    """Retain exact revision AND approved values; never carry across a revision."""
    targets = {c: {item['id']: item for item in snapshot[c]} for c in ('nodes', 'relations')}
    previous_targets = {c: {item['id']: item for item in (previous_snapshot or {}).get(c, [])} for c in targets}
    kept, deferred = [], []
    for original in old_document['decisions']:
        target = original['target']
        item = targets[target['collection']].get(target['id'])
        values = item.get('fields', {}) if item and target['collection'] == 'nodes' else item
        reason = None
        if item is None:
            reason = 'target_removed'
        elif any(field not in values or canonical_sha256(values[field]) != target['value_sha256'][field]
                 for field in target['approved_fields']):
            reason = 'approved_value_changed'
        elif item['revision'] != target['revision']:
            old = previous_targets[target['collection']].get(target['id'])
            ignored = PUBLICATION_FIELDS | {'revision', 'last_modified', 'content_sha256', 'lifecycle'}
            content = lambda record: {k: v for k, v in record.items() if k not in ignored}
            # U131 introduces a lifecycle without changing the approved content.
            # Transcribe, rather than overwrite, the original decision. This is
            # deliberately limited to the first addition of lifecycle metadata.
            if (old and 'lifecycle' not in old and 'U131' in item.get('lifecycle', {}).get('source_refs', [])
                    and content(old) == content(item) and old['revision'] == target['revision']):
                decision = copy.deepcopy(original)
                decision['id'] = original['id'] + '-LIFECYCLE-r' + str(item['revision'])
                decision['recorded_at'] = snapshot['as_of']
                decision['source_refs'] = list(dict.fromkeys(original['source_refs'] + ['U131']))
                decision['note'] += ' Transcription de ' + original['id'] + ' pour l’introduction du cycle U131 ; valeurs et portée inchangées.'
                decision['target'].update(revision=item['revision'], import_version=snapshot['version'])
                kept.append(decision)
                continue
            reason = 'revision_changed_requires_explicit_reassessment'
        if reason:
            deferred.append({'id': original['id'], 'target': target['id'], 'reason': reason,
                             'approved_fields': target['approved_fields']})
        else:
            decision = copy.deepcopy(original)
            decision['target']['import_version'] = snapshot['version']
            kept.append(decision)
    if additional:
        if additional['version'] != snapshot['version']:
            raise ValueError('Additional decisions must target the prepared version')
        # A new decision gets a new stable identifier. No existing decision is rewritten.
        old_ids = {item['id'] for item in old_document['decisions']}
        for decision in additional['decisions']:
            if decision['id'] in old_ids or decision['id'] in {item['id'] for item in kept}:
                raise ValueError('Additional decision must use a new id: ' + decision['id'])
            kept.append(copy.deepcopy(decision))
    return {'schema_version': '1.0.0', 'version': snapshot['version'], 'decisions': kept}, deferred


def explain_deferred_validations(snapshot, decisions, deferred, previous_release=None):
    """Keep old editorial notes as history, never as approval of a new revision."""
    for collection in ('nodes', 'relations'):
        previous = {r['id']: r for r in (previous_release or {}).get(collection, [])}
        for item in snapshot[collection]:
            removed = [d for d in deferred if d['target'] == item['id']]
            applicable = [d for d in decisions['decisions']
                          if d['decision_state'] == 'accepted'
                          and d['target']['collection'] == collection
                          and d['target']['id'] == item['id']]
            previous_item = previous.get(item['id'], {})
            previous_note = previous_item.get('review', {}).get('note', '')
            original_note = item['review']['note']
            if (not removed and previous_item.get('revision') == item['revision']
                    and 'Note antérieure, qui ne qualifie pas cette révision' in previous_note
                    and previous_note.endswith('« ' + original_note + ' »')
                    and set(previous_item.get('adoption_ids', [])) == {d['id'] for d in applicable}):
                # Preserve the qualification on later publications while the live
                # backlog still carries its original editorial note.
                item['review']['note'] = previous_note
                continue
            if not removed and (applicable or item['review']['state'] not in ('accepted', 'partial')):
                continue
            current = ('Seules les décisions applicables à cette version qualifient les champs validés ; '
                       'elles ne rétablissent pas les validations antérieures suspendues.' if applicable else
                       'Aucune validation antérieure reprise pour cette révision ; '
                       'aucune validation courante applicable enregistrée.')
            history = (' Validations conservées dans l’historique : ' + ', '.join(d['id'] for d in removed) + '.'
                       if removed else ' Le statut éditorial du backlog ne constitue pas une preuve de validation.')
            item['review']['note'] = (current + history
                                     + ' Note antérieure, qui ne qualifie pas cette révision : « '
                                     + original_note + ' »')


def changes(before, after, path=''):
    """Return explicit before/after values, including relation qualification."""
    result = []
    if isinstance(before, dict) and isinstance(after, dict):
        for key in sorted(set(before) | set(after)):
            here = path + '/' + key
            if key not in before or key not in after:
                result.append({'path': here, 'before_present': key in before, 'after_present': key in after,
                               'before': before.get(key), 'after': after.get(key)})
            else:
                result.extend(changes(before[key], after[key], here))
    elif before != after:
        result.append({'path': path, 'before': before, 'after': after})
    return result


def model_diff(previous, candidate):
    result = {}
    for collection in ('nodes', 'relations'):
        before = {r['id']: r for r in previous[collection]}
        after = {r['id']: r for r in candidate[collection]}
        result[collection] = {'added': [after[k] for k in sorted(set(after) - set(before))],
                              'removed': [before[k] for k in sorted(set(before) - set(after))],
                              'modified': []}
        for identifier in sorted(set(before) & set(after)):
            delta = changes(before[identifier], after[identifier])
            if delta:
                result[collection]['modified'].append({'id': identifier, 'changes': delta})
    result['principles'] = changes(previous.get('principles', []), candidate.get('principles', []))
    return result


def revision_errors(previous_snapshot, snapshot):
    errors = []
    for collection in ('nodes', 'relations'):
        previous = {r['id']: r for r in previous_snapshot[collection]}
        for item in snapshot[collection]:
            old = previous.get(item['id'])
            if not old:
                continue
            if item['revision'] < old['revision']:
                errors.append(item['id'] + ': revision cannot decrease')
            keys = ('fields', 'kind', 'layer', 'group_role', 'level_ref') if collection == 'nodes' else ('type', 'source_id', 'target_id', 'qualification')
            if any(item.get(k) != old.get(k) for k in keys) and item['revision'] <= old['revision']:
                errors.append(item['id'] + ': changed model content requires a new revision')
    return errors


def build_candidate(root=ROOT, version=None, source_refs=None, additional_path=None):
    models, pointer, previous, inputs, manifest_path = load_current(root)
    version = valid_version(version or suggested_version(models))
    live_path = models / 'backlog/model.json'
    live = read(live_path)
    snapshot = copy.deepcopy(live)
    snapshot.update(space='backlog', version=version, as_of=version.split('.')[0])
    for collection in ('nodes', 'relations'):
        for item in snapshot[collection]:
            for key in PUBLICATION_FIELDS:
                item.pop(key, None)
    element_changes = assign_versions(snapshot, inputs['input_revision'], published=previous)
    additional = read(additional_path) if additional_path else None
    decisions, deferred_decisions = reconcile_decisions(inputs['decisions'], snapshot, additional, inputs['input_revision'])
    explain_deferred_validations(snapshot, decisions, deferred_decisions, previous)
    publication_refs = source_refs or previous.get('publication', {}).get('source_refs', [])
    deferred_paths = [p for p in sorted((models / 'backlog').glob('*.json')) if p.name != 'model.json']
    all_refs = references(snapshot) | references(decisions) | set(publication_refs)
    for path in deferred_paths:
        all_refs.update(references(read(path)))
    provenance = publisher.publication_sources(inputs['provenance'], read(models / 'provenance/source-records.json'), sorted(all_refs))
    sources = {r['id']: r for r in provenance['records']}
    urbanism_schema = read(models / 'schemas/urbanism.schema.json')
    errors = validate_contract(decisions, read(models / 'schemas/decisions.schema.json'))
    errors += validate_sources(provenance) + validate_urbanism(snapshot, sources, urbanism_schema)
    errors += revision_errors(inputs['input_revision'], snapshot)
    if errors:
        # Report still needs to explain edits even when their revisions need correction.
        fatal = [e for e in errors if 'requires a new revision' not in e]
        if fatal:
            raise ValueError('\n'.join(fatal))
    candidate = publisher.compile_snapshot(snapshot, decisions, version, publication_refs)
    errors += validate_release(candidate, decisions, snapshot, sources, urbanism_schema)
    deferred_artifacts = []
    for path in deferred_paths:
        previous_path = models / 'revisions' / pointer['version'] / 'deferred' / path.name
        deferred_artifacts.append({'path': path.relative_to(models).as_posix(), 'sha256': digest(path),
                                   'comparison': 'changed' if previous_path.exists() and read(previous_path) != read(path) else 'unchanged' if previous_path.exists() else 'baseline_not_captured',
                                   'changes': changes(read(previous_path), read(path)) if previous_path.exists() else [],
                                   'disposition': 'frozen_as_context_only_not_published_as_model'})
    report = {'schema_version': '1.0.0', 'base_version': pointer['version'], 'candidate_version': version,
              'element_version_changes': element_changes,
              'publication_is_business_validation': False, 'changes': model_diff(previous, candidate),
              'retained_decision_ids': [d['id'] for d in decisions['decisions'] if d['id'] in {o['id'] for o in inputs['decisions']['decisions']}],
              'deferred_decisions': deferred_decisions,
              'new_decision_ids': [d['id'] for d in decisions['decisions'] if d['id'] not in {o['id'] for o in inputs['decisions']['decisions']}],
              'deferred_artifacts': deferred_artifacts,
              'backlog_only': {'alternatives': [r['id'] for r in snapshot.get('alternatives', [])],
                               'illustrations': [r['id'] for r in snapshot['nodes'] + snapshot['relations'] if r['review']['state'] == 'illustration']},
              'validation_errors': sorted(set(errors)),
              'note': 'Les validations différées restent dans les versions antérieures. Les artefacts de contexte gelés ne deviennent pas des éléments publiés.'}
    return {'models': models, 'pointer': pointer, 'snapshot': snapshot, 'decisions': decisions,
            'provenance': provenance, 'candidate': candidate, 'report': report,
            'backlog_sha256': digest(live_path), 'base_manifest_sha256': digest(manifest_path),
            'publication_refs': publication_refs}


def prepare(root, version, source_refs, additional_path=None):
    bundle = build_candidate(root, version, source_refs, additional_path)
    models = bundle['models']
    if bundle['report']['validation_errors']:
        raise ValueError('\n'.join(bundle['report']['validation_errors']))
    if not source_refs:
        raise ValueError('Preparation requires explicit publication source IDs')
    destination = checked_path(models / 'staging', version)
    for path in (destination, models / 'release' / version, models / 'revisions' / version,
                 models / 'provenance' / version, models / 'decisions' / (version + '.json')):
        if path.exists():
            raise ValueError('Version already exists; choose a new version: ' + str(path))
    destination.parent.mkdir(exist_ok=True)
    temporary = destination.parent / ('.prepare-' + uuid.uuid4().hex)
    temporary.mkdir()
    try:
        for name, key in [('backlog.json', 'snapshot'), ('decisions.json', 'decisions'),
                          ('source-records.json', 'provenance'), ('candidate.json', 'candidate'), ('report.json', 'report')]:
            write(temporary / name, bundle[key])
        deferred = []
        for record in bundle['report']['deferred_artifacts']:
            source_path = checked_path(models, record['path'])
            path = temporary / 'deferred' / source_path.name
            write(path, read(source_path))
            deferred.append({'path': path.relative_to(temporary).as_posix(), 'sha256': digest(path),
                             'source_path': record['path'], 'source_sha256': record['sha256']})
        manifest = {'schema_version': '1.0.0', 'kind': 'prepared_release', 'version': version,
                    'base_pointer': bundle['pointer'], 'base_manifest_sha256': bundle['base_manifest_sha256'],
                    'live_backlog_sha256': bundle['backlog_sha256'], 'publication_source_refs': source_refs,
                    'files': {name: digest(temporary / name) for name in ('backlog.json', 'decisions.json', 'source-records.json', 'candidate.json', 'report.json')},
                    'schemas': {name: digest(models / 'schemas' / name) for name in ('urbanism.schema.json', 'decisions.schema.json')},
                    'deferred': deferred}
        write(temporary / 'manifest.json', manifest)
        os.rename(temporary, destination)
    finally:
        if temporary.exists():
            if temporary.resolve().parent != destination.parent.resolve() or not temporary.name.startswith('.prepare-'):
                raise ValueError('Unsafe staging cleanup target')
            shutil.rmtree(temporary)
    return {'prepared_manifest': str(destination / 'manifest.json'), 'report': str(destination / 'report.json'),
            'candidate': str(destination / 'candidate.json'), 'release_activated': False}


def publish_prepared(root, version, activate=False):
    models, pointer, _, _, current_manifest_path = load_current(root)
    valid_version(version)
    stage = checked_path(models / 'staging', version)
    manifest = read(stage / 'manifest.json')
    if manifest.get('kind') != 'prepared_release' or manifest.get('version') != version:
        raise ValueError('Invalid prepared manifest')
    if manifest['base_pointer'] != pointer or digest(current_manifest_path) != manifest['base_manifest_sha256']:
        raise ValueError('Current release changed since preparation; prepare a fresh candidate')
    if digest(models / 'backlog/model.json') != manifest['live_backlog_sha256']:
        raise ValueError('Backlog changed since preparation; prepare a fresh candidate')
    required_files = {'backlog.json', 'decisions.json', 'source-records.json', 'candidate.json', 'report.json'}
    if set(manifest['files']) != required_files:
        raise ValueError('Prepared manifest file inventory mismatch')
    for name, sha in manifest['files'].items():
        if digest(checked_path(stage, name)) != sha:
            raise ValueError('Prepared artifact hash mismatch: ' + name)
    for name, sha in manifest['schemas'].items():
        if digest(checked_path(models / 'schemas', name)) != sha:
            raise ValueError('Model contract changed since preparation: ' + name)
    for item in manifest['deferred']:
        if digest(checked_path(stage, item['path'])) != item['sha256']:
            raise ValueError('Deferred artifact hash mismatch')
        if digest(checked_path(models, item['source_path'])) != item['source_sha256']:
            raise ValueError('Backlog context changed since preparation; prepare a fresh candidate')
    snapshot, decisions, provenance = (read(stage / name) for name in ('backlog.json', 'decisions.json', 'source-records.json'))
    if snapshot['version'] != version or decisions['version'] != version:
        raise ValueError('Prepared input version mismatch')
    source_refs = manifest['publication_source_refs']
    if not source_refs or not set(source_refs) <= {r['id'] for r in provenance['records']}:
        raise ValueError('Missing prepared publication evidence')
    release = publisher.compile_snapshot(snapshot, decisions, version, source_refs)
    if release != read(stage / 'candidate.json'):
        raise ValueError('Prepared candidate differs from current compiler result')
    errors = validate_sources(provenance)
    errors += validate_contract(decisions, read(models / 'schemas/decisions.schema.json'))
    errors += validate_release(release, decisions, snapshot, {r['id']: r for r in provenance['records']}, read(models / 'schemas/urbanism.schema.json'))
    errors += read(stage / 'report.json')['validation_errors']
    if errors:
        raise ValueError('\n'.join(errors))
    release_dir, revision_dir, proof_dir = (models / folder / version for folder in ('release', 'revisions', 'provenance'))
    decision_path = models / 'decisions' / (version + '.json')
    for path in (release_dir, revision_dir, proof_dir, decision_path):
        if path.exists():
            raise ValueError('Version already exists; publication history is immutable')
    # All checks precede writes. Interrupted output stays unactivated for diagnosis.
    release_dir.mkdir()
    revision_dir.mkdir()
    proof_dir.mkdir()
    write(revision_dir / 'backlog.json', snapshot)
    write(decision_path, decisions)
    write(proof_dir / 'source-records.json', provenance)
    for item in manifest['deferred']:
        write(checked_path(revision_dir, item['path']), read(checked_path(stage, item['path'])))
    write(release_dir / 'model.json', release)
    write(release_dir / 'changes.json', read(stage / 'report.json'))
    report=read(stage / 'report.json')
    notes=[f"# Urbanisation — version {release['revision']}", '', f"Publication {version} · modèle modifié le {release['last_modified']}.", '',
           f"{sum(n['kind']=='capability' for n in release['nodes'])} capacités ; les statuts et réserves sont conservés.", '', '## Changements', '']
    changed_ids={e['id'] for e in report['element_version_changes'] if e['collection']=='nodes' and e['reason'] in ('new','changed')}
    for action in ('added','removed','modified'):
        for item in report['changes']['nodes'][action]:
            if action=='modified' and item['id'] not in changed_ids:continue
            renaming=next((c for c in item.get('changes',[]) if c['path']=='/fields/name'),None)
            detail=(' — '+item['fields']['name']) if 'fields' in item else (' — '+str(renaming['before'])+' → '+str(renaming['after'])) if renaming else ' — contenu ou notice actualisé'
            notes.append(f"- {action} : {item['id']}" + detail)
    notes+=['', '## Validations et points ouverts', '',
            f"{len(report['retained_decision_ids'])} décisions antérieures conservées ; {len(report['deferred_decisions'])} suspendues pour les révisions modifiées.",
            f"{sum('-LIFECYCLE-r' in key for key in report['new_decision_ids'])} accords transcrits à portée identique pour le cycle U131 ; {sum('-LIFECYCLE-r' not in key for key in report['new_decision_ids'])} autres décisions nouvelles sourcées.",
            'Aucune publication ne vaut validation métier. Les noms conditionnels de D05, le résiduel D02 et les frontières Supply restent à instruire.', '']
    notes += [f"- {d['id']} ({d['target']}) : conservée dans l’historique, reprise suspendue pour cette révision." for d in report['deferred_decisions']]
    notes += ['', 'Les éléments inchangés conservent leurs révisions. L’initialisation de last_modified marque le début du suivi lorsque la date antérieure est inconnue.', '']
    (release_dir/'release-notes.md').write_text('\n'.join(notes),encoding='utf-8')
    output = {'schema_version': '1.0.0', 'version': version, 'model_sha256': digest(release_dir / 'model.json'),
              'input_revision_path': f'../../revisions/{version}/backlog.json', 'input_revision_sha256': digest(revision_dir / 'backlog.json'),
              'decisions_path': f'../../decisions/{version}.json', 'decisions_sha256': digest(decision_path),
              'provenance_path': f'../../provenance/{version}/source-records.json', 'provenance_sha256': digest(proof_dir / 'source-records.json'),
              'source_files': release['source_files'], 'node_count': len(release['nodes']),
              'capability_count': sum(n['kind'] == 'capability' for n in release['nodes']),
              'complete_capability_count': sum(n['kind'] == 'capability' and n['review']['state'] == 'accepted' for n in release['nodes']),
              'changes_path': 'changes.json', 'changes_sha256': digest(release_dir / 'changes.json'),
              'prepared_manifest_sha256': digest(stage / 'manifest.json'),
              'note': 'Publication du backlog préparé ; validations conservées seulement à révision et valeurs identiques.'}
    write(release_dir / 'manifest.json', output)
    if activate:
        register(models/'release',release,version+'/release-notes.md',write,publisher.activate_pointer)
    return {'version': version, 'manifest': str(release_dir / 'manifest.json'), 'release_activated': activate,
            'capability_count': output['capability_count'], 'complete_capability_count': output['complete_capability_count']}


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='Project root; useful for isolated verification')
    commands = parser.add_subparsers(dest='command', required=True)
    for command in ('report', 'prepare'):
        child = commands.add_parser(command)
        child.add_argument('--version', required=command == 'prepare')
        child.add_argument('--source', action='append', required=command == 'prepare')
        child.add_argument('--decisions', type=Path, help='Only new, explicitly sourced decisions for the prepared version')
    child = commands.add_parser('publish')
    child.add_argument('--version', required=True)
    child.add_argument('--activate', action='store_true')
    args = parser.parse_args()
    if args.command == 'report':
        result = build_candidate(args.root, args.version, args.source, args.decisions)['report']
    elif args.command == 'prepare':
        result = prepare(args.root, args.version, args.source, args.decisions)
    else:
        result = publish_prepared(args.root, args.version, args.activate)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

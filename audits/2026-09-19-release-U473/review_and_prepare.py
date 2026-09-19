"""Réexamen ciblé des accords historiques et préparation de la release U473."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.prepare_release import build_candidate, load_current, prepare
from scripts.structured_io import dumps, read
from scripts.validate_models import canonical_sha256

audit = Path(__file__).parent
version = '2026-09-19.6'


def save(name, value):
    with (audit/name).open('x', encoding='utf-8', newline='\n') as stream:
        stream.write(dumps(value, Path(name).suffix))


mutable = {'modeles/release/index.json', 'modeles/modeling-guides/index.yaml',
           'modeles/provenance/source-records.json'}
protected = {}
for folder in ('release', 'revisions', 'decisions', 'provenance', 'modeling-guides'):
    for path in (ROOT/'modeles'/folder).rglob('*'):
        relative = path.relative_to(ROOT).as_posix()
        if path.is_file() and relative not in mutable:
            protected[relative] = sha256(path.read_bytes()).hexdigest()
if (audit/'protected-files.json').exists():
    assert read(audit/'protected-files.json') == protected, 'Historical baseline changed'
else:
    save('protected-files.json', protected)
for name in (*sorted(mutable - {'modeles/provenance/source-records.json'}),
             'modeles/backlog/model.yaml', 'modeles/backlog/glossary.yaml'):
    destination = audit/'before'/name
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        assert destination.read_bytes() == (ROOT/name).read_bytes(), name
    else:
        with destination.open('xb') as stream:
            stream.write((ROOT/name).read_bytes())

bundle = build_candidate(ROOT, version, ['U473'])
_, _, previous, inputs, _ = load_current(ROOT)
assert previous['version'] == '2026-09-19.5'
old = {c: {item['id']: item for item in previous[c]} for c in ('nodes', 'relations')}
new = {c: {item['id']: item for item in bundle['candidate'][c]} for c in old}
assert set(old['nodes']) - set(new['nodes']) == {'universe-case'}
assert not set(new['nodes']) - set(old['nodes'])
assert set(old['relations']) == set(new['relations'])
for collection in old:
    for identifier, current in new[collection].items():
        prior = old[collection][identifier]
        if collection == 'nodes':
            assert current['kind'] == prior['kind'], identifier
            changed = {key for key in current['fields'].keys() | prior['fields'].keys()
                       if current['fields'].get(key) != prior['fields'].get(key)}
            allowed = {'market_comparisons'}
            if identifier == 'universe-supply':
                allowed |= {'definition', 'finality', 'scope', 'examples'}
            if identifier == 'BHV082':
                allowed.add('scope')
            assert changed <= allowed, (identifier, changed)
        else:
            for field in ('type', 'source_id', 'target_id', 'qualification'):
                assert current.get(field) == prior.get(field), (identifier, field)

historical = {decision['id']: decision for decision in inputs['decisions']['decisions']}
decisions, evidence, retired = [], [], []
for deferred in bundle['report']['deferred_decisions']:
    original = historical[deferred['id']]
    if deferred['reason'] == 'target_removed':
        assert deferred['target'] == 'universe-case'
        retired.append(dict(decision=original['id'], target='universe-case', source='U472',
                            disposition='Accord historique conservé ; univers retiré, aucune reprise.'))
        continue
    assert deferred['reason'] == 'revision_changed_requires_explicit_reassessment', deferred
    target = original['target']
    collection, identifier = target['collection'], target['id']
    current, prior = new[collection][identifier], old[collection][identifier]
    values = current['fields'] if collection == 'nodes' else current
    prior_values = prior['fields'] if collection == 'nodes' else prior
    for field in target['approved_fields']:
        assert values[field] == prior_values[field], (identifier, field)
        assert canonical_sha256(values[field]) == target['value_sha256'][field], (identifier, field)
    decision = deepcopy(original)
    decision['id'] = f'ADOPT-U473-UNCHANGED-{len(decisions)+1:03d}'
    assert decision['id'] not in historical
    decision['recorded_at'] = '2026-09-19'
    decision['note'] += (' Réexamen U473 de ' + original['id'] +
        ' : valeurs approuvées inchangées, contrôlées par empreinte contre v012 ; identité, type et relations métier conservés. '
        'Les nouveaux textes, exemples, périmètres et rapprochements marché ne reçoivent aucun accord par extension. '
        'Les sources et la date de l’accord historique restent seules autorités des valeurs transcrites. '
        'Preuve : audits/2026-09-19-release-U473/transcription-review.json.')
    decision['target'].update(revision=current['revision'], import_version=version)
    decisions.append(decision)
    evidence.append(dict(decision=decision['id'], prior_decision=original['id'],
        historical_path='modeles/decisions/2026-09-19.5.json', target=identifier,
        collection=collection, old_revision=target['revision'], new_revision=current['revision'],
        approved_fields=target['approved_fields'], unchanged_value_sha256=target['value_sha256'],
        historical_source_refs=original['source_refs']))

assert len(decisions) == 40 and len(retired) == 1
save('additional-decisions.json', dict(schema_version='1.0.0', version=version, decisions=decisions))
save('transcription-review.json', dict(version=version, reviewed_decisions=len(decisions),
    unchanged_approved_fields=sum(len(item['approved_fields']) for item in evidence),
    scope='Transcriptions à portée constante ; aucune valeur nouvelle approuvée.',
    retired=retired, items=evidence))
final = build_candidate(ROOT, version, ['U473'], audit/'additional-decisions.json')
assert not final['report']['validation_errors'], final['report']['validation_errors']
save('reviewed-report.json', final['report'])
prepare(ROOT, version, ['U473'], audit/'additional-decisions.json')
print(json.dumps(dict(version=version, historical_decisions_retained=len(final['report']['retained_decision_ids']),
    transcribed_decisions=len(decisions), approved_fields=sum(len(item['approved_fields']) for item in evidence),
    retired_decisions=len(retired), protected_files=len(protected), validation_errors=0)))

"""Réexamen explicite de valeurs approuvées inchangées, puis préparation U467."""
from copy import deepcopy
from pathlib import Path
from hashlib import sha256
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.prepare_release import build_candidate, load_current, prepare
from scripts.validate_models import canonical_sha256
from scripts.structured_io import read, dumps
from app.modeling_guide import _validate_guide

audit = Path(__file__).parent
version = '2026-09-19.4'
bundle = build_candidate(ROOT, version, ['U467'])
_, _, previous, inputs, _ = load_current(ROOT)
assert previous['version'] == '2026-09-19.3'
old = {collection: {item['id']: item for item in previous[collection]} for collection in ['nodes','relations']}
new = {collection: {item['id']: item for item in bundle['snapshot'][collection]} for collection in old}
for collection in old:
    for identifier, item in old[collection].items():
        current = new[collection][identifier]
        if collection == 'nodes':
            assert current['kind'] == item['kind']
        else:
            for field in ['type','source_id','target_id','qualification']:
                assert current.get(field) == item.get(field), (identifier,field)

historical = {d['id']:d for d in inputs['decisions']['decisions']}
decisions, evidence = [], []
for i, deferred in enumerate(bundle['report']['deferred_decisions'], 1):
    assert deferred['reason'] == 'revision_changed_requires_explicit_reassessment', deferred
    original = historical[deferred['id']]
    target = original['target']; collection = target['collection']; identifier = target['id']
    current = new[collection][identifier]; prior = old[collection][identifier]
    values = current['fields'] if collection == 'nodes' else current
    prior_values = prior['fields'] if collection == 'nodes' else prior
    for field in target['approved_fields']:
        assert values[field] == prior_values[field], (identifier,field)
        assert canonical_sha256(values[field]) == target['value_sha256'][field], (identifier,field)
    decision = deepcopy(original)
    decision['id'] = f'ADOPT-U467-UNCHANGED-{i:03d}'
    assert decision['id'] not in historical
    decision['recorded_at'] = '2026-09-19'
    decision['note'] += (' Réexamen U467 de ' + original['id'] +
        ' : valeurs approuvées inchangées, contrôlées par empreinte contre v010 ; identité, type et relations métier conservés. '
        'Le retrait de layer et les compléments éditoriaux ne créent aucun accord sur un nouveau champ. '
        'Preuve : audits/2026-09-19-release-U467/transcription-review.json.')
    decision['target'].update(revision=current['revision'], import_version=version)
    decisions.append(decision)
    evidence.append(dict(decision=decision['id'], prior_decision=original['id'],
        historical_path='modeles/decisions/2026-09-19.3.json', target=identifier,
        collection=collection, old_revision=target['revision'], new_revision=current['revision'],
        approved_fields=target['approved_fields'], unchanged_value_sha256=target['value_sha256']))


def save(name, value):
    with (audit/name).open('x', encoding='utf-8', newline='\n') as stream:
        stream.write(dumps(value, Path(name).suffix))


save('additional-decisions.json', dict(schema_version='1.0.0', version=version, decisions=decisions))
save('transcription-review.json', dict(version=version, reviewed_decisions=len(decisions),
    unchanged_approved_fields=sum(len(e['approved_fields']) for e in evidence),
    scope='Transcriptions à portée constante ; aucune valeur nouvelle approuvée.', items=evidence))

guide = read(ROOT/'modeles/backlog/modeling-guide-U458.yaml')
guide['scope'] = ('Édition méthodologique publiée avec U467. Principes retenus et formulations pédagogiques proposées '
                  'restent distincts. Ce guide ne crée aucun élément du catalogue métier ; les fiches pilotes U465 '
                  'restent un contexte de travail séparé.')
guide['source_refs'].append('U467')
guide['sources'].append(dict(id='U467', title='Release pour tester Atlas',
    excerpt='Lance une release que je teste un peu',
    scope='Autorise la publication locale et l’association explicite de cette édition du guide ; aucune validation globale du contenu.'))
_validate_guide(guide, '2026-09-19.2')
save('guide-candidate.yaml', guide)

final = build_candidate(ROOT, version, ['U467'], audit/'additional-decisions.json')
assert not final['report']['validation_errors'], final['report']['validation_errors']
save('reviewed-report.json', final['report'])
prepare(ROOT, version, ['U467'], audit/'additional-decisions.json')
print(json.dumps(dict(version=version, historical_decisions_retained=len(final['report']['retained_decision_ids']),
    transcribed_decisions=len(decisions), approved_fields=sum(len(e['approved_fields']) for e in evidence),
    validation_errors=0, guide_sha256=sha256((audit/'guide-candidate.yaml').read_bytes()).hexdigest())))

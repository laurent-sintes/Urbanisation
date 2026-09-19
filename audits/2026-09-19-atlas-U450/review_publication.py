"""Review unchanged approval values before proposing publication of type fields."""
from collections import defaultdict
from datetime import date
from pathlib import Path
import json
import re
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.prepare_release import build_candidate, load_current
from scripts.lifecycle import value_hash

out = Path(__file__).parent
version = '2026-09-19.3'
bundle = build_candidate(ROOT, version)
_, _, previous, inputs, _ = load_current(ROOT)
old_nodes = {n['id']: n for n in previous['nodes']}
missing = defaultdict(list)
for error in bundle['report']['validation_errors']:
    match = re.fullmatch(r'release/([^:]+): lifecycle approval lacks a matching decision: (.+)', error)
    assert match, error
    missing[match[1]].append(match[2])
decisions, evidence = [], []
for item in bundle['snapshot']['nodes']:
    if item['id'] not in old_nodes:
        continue
    before = old_nodes[item['id']]['fields']
    assert {k:v for k,v in item['fields'].items() if k != 'nature'} == {k:v for k,v in before.items() if k != 'nature'}
    fields = sorted(missing.get(item['id'], []))
    if not fields:
        continue
    assert 'nature' not in fields
    refs, proofs, originals = [], [], []
    for field in fields:
        fingerprint = value_hash(item['fields'][field])
        assert fingerprint == item['lifecycle']['value_sha256'][field]
        matches = [d for d in inputs['decisions']['decisions'] if d['decision_state'] == 'accepted' and d['target']['collection'] == 'nodes' and d['target']['id'] == item['id'] and field in d['target']['approved_fields'] and d['target']['value_sha256'][field] == fingerprint]
        assert matches, (item['id'], field)
        original = matches[-1]
        originals.append(original)
        refs += original['source_refs']
        proofs.append({'field':field, 'value_sha256':fingerprint, 'historical_decision':original['id'], 'historical_path':'modeles/decisions/' + previous['version'] + '.json'})
    identifier = f'ADOPT-TYPES-UNCHANGED-{item["id"]}-r{item["revision"]}'
    decisions.append({'id':identifier, 'decision_state':'accepted', 'author':'Laurent',
        'decided_at':max(d['decided_at'] for d in originals), 'recorded_at':date.today().isoformat(),
        'interpretation':'contextual' if any(d['interpretation']=='contextual' for d in originals) else 'explicit',
        'source_refs':list(dict.fromkeys(refs)),
        'note':'Réexamen des valeurs inchangées après ajout du type : noms, définitions et finalités identiques aux accords historiques contrôlés par empreinte. Les nouveaux champs nature restent proposés. Preuves : audits/2026-09-19-atlas-U450/transcription-review.json.',
        'target':{'collection':'nodes','id':item['id'],'revision':item['revision'],'approved_fields':fields,
            'value_sha256':{f:value_hash(item['fields'][f]) for f in fields},'import_version':version}})
    evidence.append({'id':item['id'], 'decision':identifier, 'fields':proofs})
def save(name, value):
    with (out / name).open('x', encoding='utf-8') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2); stream.write('\n')
save('additional-decisions.json', {'schema_version':'1.0.0','version':version,'decisions':decisions})
save('transcription-review.json', {'version':version,'decisions':len(decisions),'fields':sum(len(e['fields']) for e in evidence),'items':evidence})
reviewed = build_candidate(ROOT, version, additional_path=out / 'additional-decisions.json')
assert not reviewed['report']['validation_errors'], reviewed['report']['validation_errors']
save('publication-review.json', reviewed['report'])
print(json.dumps({'version':version,'reviewed_decisions':len(decisions),'unchanged_approved_fields':sum(len(e['fields']) for e in evidence),'validation_errors':0}))

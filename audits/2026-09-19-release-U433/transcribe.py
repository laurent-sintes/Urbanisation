"""One-off, scope-preserving transcription for the reviewed U433 release.

This does not infer approvals or change the backlog. It only fills missing
publication decisions for the exact field hashes of the audited catalogue.
"""
from collections import defaultdict
from datetime import date
from hashlib import sha256
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read
from scripts.lifecycle import validate_lifecycle, value_hash
from scripts.prepare_release import build_candidate

OUT = Path(__file__).resolve().parent
VERSION = '2026-09-19.1'
MODEL_HASH = '2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2'


def main():
    if sha256((ROOT/'modeles/backlog/model.yaml').read_bytes()).hexdigest() != MODEL_HASH:
        raise ValueError('Catalogue changed; a new scoped review is required')
    checks = read(ROOT/'audits/2026-09-17-comportements-manquants/checks.json')
    if checks['status'] != 'passed' or checks['model_sha256'] != MODEL_HASH or checks['audit_status'] != 'closed_U431':
        raise ValueError('Missing completed historical verification of this catalogue')
    bundle = build_candidate(ROOT, VERSION, ['U433'])
    missing = defaultdict(list)
    for error in bundle['report']['validation_errors']:
        match = re.fullmatch(r'release/([^:]+): lifecycle approval lacks a matching decision: (.+)', error)
        if not match:
            raise ValueError('Unreviewed validation error: '+error)
        missing[match[1]].append(match[2])
    if sum(map(len, missing.values())) != 469 or len(missing) != 207:
        raise ValueError('Reviewed scope changed')
    sources = {s['id']: s for s in read(ROOT/'modeles/provenance/source-records.json')['records']}
    historical = []
    for path in (ROOT/'modeles/decisions').glob('*.json'):
        for decision in read(path)['decisions']:
            if decision['decision_state'] == 'accepted':
                historical.append((path.relative_to(ROOT).as_posix(), decision))
    decisions, evidence = [], []
    for collection in ('nodes', 'relations'):
        for item in bundle['snapshot'][collection]:
            if item['id'] not in missing:
                continue
            errors = validate_lifecycle(item)
            if errors:
                raise ValueError('\n'.join(errors))
            life = item['lifecycle']
            fields = sorted(missing[item['id']])
            if not set(fields) <= set(life['validated_fields']):
                raise ValueError('Transcription would enlarge the recorded scope')
            values = item['fields'] if collection == 'nodes' else item
            hashes = {f: value_hash(values[f]) for f in fields}
            if any(hashes[f] != life['value_sha256'][f] for f in fields):
                raise ValueError('Approved value changed')
            refs = life['source_refs']
            if not refs or any(ref not in sources for ref in refs) or 'U433' in refs:
                raise ValueError('Missing approval sources or publication request used as approval')
            dates = []
            for ref in refs:
                if re.fullmatch(r'U\d+', ref):
                    match = re.search(r'\*\*date\*\*\s+(\d{4}-\d{2}-\d{2})', sources[ref]['captured_text'])
                    if match:
                        dates.append(match[1])
            if not dates:
                raise ValueError('No dated user evidence: '+item['id'])
            predecessors = []
            contextual = False
            for path, old in historical:
                target = old['target']
                if (target['collection'], target['id']) != (collection, item['id']):
                    continue
                same = [f for f in fields if target['value_sha256'].get(f) == hashes[f]]
                if same:
                    predecessors.append({'path': path, 'decision_id': old['id'], 'unchanged_fields': same})
                    contextual |= old['interpretation'] == 'contextual'
            identifier = f"ADOPT-U433-TRANSCRIPTION-{item['id']}-r{item['revision']}"
            decisions.append({
                'id': identifier, 'decision_state': 'accepted', 'author': 'Laurent',
                'decided_at': max(dates), 'recorded_at': date.today().isoformat(),
                'interpretation': 'contextual' if contextual else 'explicit',
                'source_refs': refs,
                'note': ('Transcription pour publication des accords antérieurs, après revue U433 : '
                         + life['note'] + ' Portée strictement limitée aux champs et empreintes ci-dessous. '
                         'La date indique la dernière contribution de la chaîne référencée, pas un nouvel accord. '
                         'U433 autorise la publication uniquement. Traçabilité : '
                         'audits/2026-09-19-release-U433/transcription-review.json.'),
                'target': {'collection': collection, 'id': item['id'], 'revision': item['revision'],
                           'approved_fields': fields, 'value_sha256': hashes, 'import_version': VERSION},
            })
            evidence.append({'decision_id': identifier, 'collection': collection, 'id': item['id'],
                'fields': fields, 'hashes': hashes, 'lifecycle_sha256': value_hash(life),
                'source_hashes': {r: sources[r]['content_sha256'] for r in refs},
                'historical_matches': predecessors, 'scope_note': life['note']})
    document = {'schema_version': '1.0.0', 'version': VERSION, 'decisions': decisions}
    for name, value in [('additional-decisions.json', document), ('transcription-review.json', {
            'version': VERSION, 'model_sha256': MODEL_HASH, 'target_count': len(evidence),
            'field_count': sum(len(e['fields']) for e in evidence), 'items': evidence})]:
        with (OUT/name).open('x', encoding='utf-8') as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
    print(json.dumps({'decisions': len(decisions), 'fields': sum(len(e['fields']) for e in evidence)}))


if __name__ == '__main__':
    main()

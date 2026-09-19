"""Transcribe exact historical approvals and U438/U445, without inferring new scope."""
from collections import defaultdict
from datetime import date
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read
from scripts.lifecycle import validate_lifecycle,value_hash
from scripts.prepare_release import build_candidate
OUT=Path(__file__).parent
VERSION='2026-09-19.2'

def main():
    model_path=ROOT/'modeles/backlog/model.yaml'
    model_hash=sha256(model_path.read_bytes()).hexdigest()
    bundle=build_candidate(ROOT,VERSION,['U448'])
    missing=defaultdict(list)
    for error in bundle['report']['validation_errors']:
        match=re.fullmatch(r'release/([^:]+): lifecycle approval lacks a matching decision: (.+)',error)
        if not match:raise ValueError('Unexpected error: '+error)
        missing[match[1]].append(match[2])
    assert sum(map(len,missing.values()))==141
    sources={s['id']:s for s in read(ROOT/'modeles/provenance/source-records.json')['records']}
    historical=[]
    for path in (ROOT/'modeles/decisions').glob('*.json'):
        historical += [(path.relative_to(ROOT).as_posix(),d) for d in read(path)['decisions'] if d['decision_state']=='accepted']
    explicit={('D03','name'):'U438',('D15','name'):'U438',('D03.n','name'):'U445'}
    members={'D03.i':'D15','D03.j':'D15','D03.k':'D15','D03.l':'D15','D03.n':'D15','D04.n':'D04','D04.q':'D04','D02.e':'D03','D03.m':'D03','D03.o':'D03','D03.p':'D03'}
    for id in members:
        for field in ['type','source_id','target_id']:explicit[('REL-MEMBER-'+id,field)]='U438'
    decisions=[];evidence=[]
    for collection in ['nodes','relations']:
        for item in bundle['snapshot'][collection]:
            if item['id'] not in missing:continue
            assert not validate_lifecycle(item)
            values=item['fields'] if collection=='nodes' else item
            fields=sorted(missing[item['id']]);field_proofs=[];refs=[];contextual=False
            assert set(fields)<=set(item['lifecycle']['validated_fields'])
            for field in fields:
                fingerprint=value_hash(values[field]);assert fingerprint==item['lifecycle']['value_sha256'][field]
                accepted=explicit.get((item['id'],field))
                if accepted:
                    if item['id'].startswith('REL-MEMBER-'):
                        target=item['id'].removeprefix('REL-MEMBER-')
                        assert (item['type'],item['source_id'],item['target_id'])==('contains',members[target],target)
                    else:assert values[field]=={'D03':'Fulfillment Optimization','D15':'Order Promising','D03.n':'Fulfillment Commitment'}[item['id']]
                    refs.append(accepted)
                    field_proofs.append(dict(field=field,value_sha256=fingerprint,authority=accepted,
                        evidence='Explicit choice recorded with presented scope; name or parent only.'))
                else:
                    matches=[(path,d) for path,d in historical if d['target']['collection']==collection and d['target']['id']==item['id'] and field in d['target']['approved_fields'] and d['target']['value_sha256'].get(field)==fingerprint]
                    if not matches:raise ValueError(f'No historical field-level proof: {item["id"]}.{field}')
                    latest=sorted(matches,key=lambda match:match[0])[-1]
                    refs+=latest[1]['source_refs'];contextual|=latest[1]['interpretation']=='contextual'
                    field_proofs.append(dict(field=field,value_sha256=fingerprint,historical_decision=latest[1]['id'],historical_path=latest[0],source_refs=latest[1]['source_refs']))
            refs=list(dict.fromkeys(refs));assert 'U448' not in refs and all(r in sources for r in refs)
            dates=[]
            for ref in refs:
                if re.fullmatch(r'U\d+',ref):
                    match=re.search(r'\*\*date\*\*\s+(\d{4}-\d{2}-\d{2})',sources[ref]['captured_text'])
                    if match:dates.append(match[1])
            assert dates
            id=f'ADOPT-U448-TRANSCRIPTION-{item["id"]}-r{item["revision"]}'
            decisions.append(dict(id=id,decision_state='accepted',author='Laurent',decided_at=max(dates),recorded_at=date.today().isoformat(),
                interpretation='contextual' if contextual else 'explicit',source_refs=refs,
                note='Transcription à portée constante pour la release U448 : preuves exactes par champ dans audits/2026-09-19-release-U448/transcription-review.json. Les champs inchangés reprennent leurs décisions historiques ; U438/U445 autorisent uniquement les noms et rattachements présentés. U448 autorise la publication, sans nouvel accord métier. La date reprend la dernière contribution de la chaîne de preuve.',
                target=dict(collection=collection,id=item['id'],revision=item['revision'],approved_fields=fields,value_sha256={f:value_hash(values[f]) for f in fields},import_version=VERSION)))
            evidence.append(dict(decision_id=id,id=item['id'],collection=collection,fields=field_proofs,
                source_hashes={r:sources[r]['content_sha256'] for r in refs}))
    assert sha256(model_path.read_bytes()).hexdigest()==model_hash
    def output(name,obj):
        with (OUT/name).open('x',encoding='utf-8') as stream:json.dump(obj,stream,ensure_ascii=False,indent=2);stream.write('\n')
    output('additional-decisions.json',dict(schema_version='1.0.0',version=VERSION,decisions=decisions))
    output('transcription-review.json',dict(version=VERSION,model_sha256=model_hash,target_count=len(decisions),field_count=sum(len(e['fields']) for e in evidence),items=evidence))
    protected={}
    for folder in ['release','revisions','decisions','provenance']:
        for path in (ROOT/'modeles'/folder).rglob('*'):
            if path.is_file() and path!=ROOT/'modeles/release/index.json':protected[path.relative_to(ROOT).as_posix()]=sha256(path.read_bytes()).hexdigest()
    output('protected-before.json',protected)
    print(json.dumps(dict(decisions=len(decisions),fields=sum(len(e['fields']) for e in evidence),protected_files=len(protected),model_sha256=model_hash)))

if __name__=='__main__':main()

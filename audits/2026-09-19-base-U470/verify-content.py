from pathlib import Path
from hashlib import sha256
from collections import Counter
import sys,json
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).parent
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read
from scripts.market_comparison import document_key,validate_reference_policy
m=read(ROOT/'modeles/backlog/model.yaml');g=read(ROOT/'modeles/backlog/glossary.yaml')
before=read(HERE/'before/modeles/backlog/model.yaml')
previous=read(HERE/'before/modeles/backlog/glossary.yaml')
baseline=json.loads((HERE/'single-references.json').read_text(encoding='utf-8'))
protected=json.loads((HERE/'protected-files.json').read_text(encoding='utf-8'))
assert all(sha256((ROOT/name).read_bytes()).hexdigest()==digest for name,digest in protected.items())
assert m['relations']==before['relations']
assert m['information_catalog']==before['information_catalog']
assert m['principles']==before['principles']
lookup={n['id']:n['fields'] for n in m['nodes']}|{t['id']:t for t in g['terms']}
evidence=[]
for old in baseline:
    fields=lookup[old['id']];cs=fields['market_comparisons']
    assert fields['name']==old['name'] and fields['definition']==old['definition'],old['id']
    assert cs[:-1]==old['entries'],old['id']
    assert len({document_key(c['source_url']) for c in cs})==2,old['id']
    evidence.append({'id':old['id'],'name':old['name'],'documents':2,'vendors':sorted({c['vendor'] for c in cs}),
                     'added_source':cs[-1]['source_title'],'added_url':cs[-1]['source_url']})
allowed={x['id'] for x in baseline}|{'universe-supply'}
oldnodes={n['id']:n for n in before['nodes']}
assert {n['id'] for n in m['nodes']}==set(oldnodes)
for n in m['nodes']:
    old=oldnodes[n['id']]
    if n['id'] not in allowed:assert n==old,n['id']
    assert n.get('lifecycle')==old.get('lifecycle'),n['id']
    if n['id'] in allowed-{'universe-supply'}:
        assert {k:v for k,v in n['fields'].items() if k!='market_comparisons'}=={k:v for k,v in old['fields'].items() if k!='market_comparisons'},n['id']
oldterms={t['id']:t for t in previous['terms']}
assert {t['id'] for t in g['terms']}==set(oldterms)
for t in g['terms']:
    if t['id'] not in allowed|{'TER031','TER050','TER084'}:assert t==oldterms[t['id']],t['id']
assert not validate_reference_policy(m|{'glossary':g})
rows=[(n['id'],n.get('fields',{}).get('market_comparisons',[])) for n in m['nodes'] if n['review']['state']!='illustration']+[(t['id'],t.get('market_comparisons',[])) for t in g['terms']]
result={'status':'passed','single_reference_cards_completed':len(evidence),'cards_with_market_comparisons':sum(bool(cs) for _,cs in rows),
        'remaining_single_reference_cards':0,'cards_without_comparisons':sum(not cs for _,cs in rows),
        'new_comparisons_with_other_vendor':sum(len(e['vendors'])>1 for e in evidence),
        'protected_files_unchanged':len(protected),'nodes':len(m['nodes']),'relations_unchanged':len(m['relations']),
        'information_items_unchanged':len(m['information_catalog']['items']),
        'lifecycle_approvals_unchanged':True,'details':evidence}
(HERE/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='details'},ensure_ascii=False))

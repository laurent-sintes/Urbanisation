from pathlib import Path
from collections import Counter
import sys,json
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read
sys.stdout.reconfigure(encoding='utf-8')
m=read(ROOT/'modeles/backlog/model.yaml');g=read(ROOT/'modeles/backlog/glossary.yaml')
for n in m['nodes']:
 if n.get('level_ref')=='universe':print(json.dumps(n,ensure_ascii=False,indent=2))
print('GLOSSARY KEYWORDS')
for t in g['terms']:
 if any(w in t['name'].lower() for w in ('supply','référ','projection','ingestion','chaîne','source','orchestration')):print(json.dumps(t,ensure_ascii=False))
entries=[(n['id'],n['fields'].get('name'),n['fields'].get('market_comparisons',[])) for n in m['nodes'] if n['review']['state']!='illustration']
entries += [(t['id'],t['name'],t.get('market_comparisons',[])) for t in g['terms']]
print('COUNTS',Counter(len({x['source_url'] for x in c}) for _,_,c in entries))
print('SINGLE REFERENCES',[(i,n,c[0]['vendor'],c[0]['source_url']) for i,n,c in entries if len({x['source_url'] for x in c})==1])

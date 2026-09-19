"""Read-only inventory of the explicitly selected Atlas publication."""
import sys, json, hashlib
from pathlib import Path
from collections import Counter
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read
OUT = Path(__file__).parent
release = ROOT / 'modeles/release'
index = read(release / 'index.json')
descriptor = read(release / index['current'])
snapshot = release / descriptor['path']
assert hashlib.sha256(snapshot.read_bytes()).hexdigest() == descriptor['sha256']
model = read(snapshot)
nodes, relations = model['nodes'], model['relations']
business = [r for r in relations if r['type'] not in ['contains', 'presents']]
backlog = read(ROOT / 'modeles/backlog/model.yaml')
schema = read(ROOT / 'modeles/schemas/urbanism.schema.json')
guide = read(ROOT / 'modeles/modeling-guides/versions/2026-09-19.1.yaml')
data = {
 'publication':{'descriptor':index['current'],'version':descriptor['version'],'sha256':descriptor['sha256']},
 'nodes':len(nodes), 'kinds':dict(Counter(n['kind'] for n in nodes)),
 'layers':dict(Counter(n['layer'] for n in nodes)),
 'capability_types':dict(Counter(n['fields'].get('nature') for n in nodes if n['kind']=='capability')),
 'behavior_types':dict(Counter(n['fields'].get('nature') for n in nodes if n['kind']=='behavior')),
 'relations':len(relations), 'relation_types':dict(Counter(r['type'] for r in relations)),
 'business_relations':len(business),
 'qualified_business_relations':{key:sum(bool(r.get('qualification',{}).get(key)) for r in business) for key in ['meaning','role','conditions','effects','scope']},
 'field_counts':dict(Counter(k for n in nodes for k in n['fields'])),
 'allowed_fields':list(schema['$defs']['node']['properties']['fields']['properties']),
 'allowed_kinds':schema['$defs']['node']['properties']['kind']['enum'],
 'data_nodes_backlog':[{'id':n['id'],'kind':n['kind'],'name':n['fields']['name'],'review':n.get('review')} for n in backlog['nodes'] if n['kind'] in ['object','document','event']],
 'references':[{'id':n['id'],'name':n['fields']['name'],'mastership':n['fields'].get('mastership'),'fields':list(n['fields']), 'capabilities':[r['target_id'] for r in relations if r['type']=='contains' and r['source_id']==n['id']]} for n in nodes if n['kind']=='reference'],
 'guide_lessons':[{'id':l['id'],'label':l['label'],'title':l['title']} for l in guide['lessons']],
 'groups':[{'id':n['id'],'fields':n['fields'],'group_role':n.get('group_role'),'level_ref':n.get('level_ref'),'layer':n['layer']} for n in nodes if n['kind']=='group'],
 'scope_words':sorted([{'id':n['id'],'name':n['fields']['name'],'scope_words':len(n['fields'].get('scope','').split())} for n in nodes],key=lambda n:n['scope_words'],reverse=True)[:8],
}
(OUT/'model-observations.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
protected = [ROOT/'modeles/release/index.json',ROOT/'modeles/backlog/model.yaml',ROOT/'modeles/backlog/glossary.yaml',ROOT/'modeles/backlog/modeling-glossary.yaml']
for dirname in ['modeles/release','modeles/modeling-guides','modeles/schemas','app/src','app/dist']:
 protected.extend(p for p in (ROOT/dirname).rglob('*') if p.is_file())
hashes={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(protected))}
manifest=OUT/'protected-files.json'
if not manifest.exists(): manifest.write_text(json.dumps(hashes,indent=2),encoding='utf8')
else:
 initial=json.loads(manifest.read_text(encoding='utf8'))
 assert hashes==initial, 'Un fichier du modèle ou de l’application a changé pendant l’audit.'
print(json.dumps({k:data[k] for k in ['publication','kinds','layers','relation_types','qualified_business_relations','data_nodes_backlog','scope_words']},ensure_ascii=False,indent=2))
print(f'Protected files: {len(hashes)}')

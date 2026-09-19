from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from scripts.structured_io import read,dumps,write_text_if_changed
HERE=Path(__file__).parent
m=read(ROOT/'modeles/backlog/model.yaml')
n=next(x for x in m['nodes'] if x['id']=='BHV069')
c=n['fields']['market_comparisons'][-1]
c.update(vendor='SAP',product='S/4HANA Sales',element_name='Advanced Intercompany Sales Processing',
    source_title='Executing the Advanced Intercompany Sales and Stock Transfer Process',
    source_url='https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/executing-the-advanced-intercompany-sales-and-stock-transfer-process_c5f8e409-c8e3-4e0a-b736-6d1d93d0f2bc',
    source_version='Cours évolutif ; parcours avancé introduit en S/4HANA 2022',
    source_locator='Advanced Intercompany Sales Processing : commandes SO2, PO3 et SO4 ; propagation des changements',
    similarities='Les commandes de vente et d’achat entre entités juridiques sont liées et leurs changements coordonnés.',
    differences='SAP inclut des automatismes et des effets comptables dans ce parcours ; FLOW conserve une responsabilité métier indépendante.',
    source_refs=['U470','U471','ELM322','CMP186'])
n['source_refs']=[r for r in n['source_refs'] if r!='ELM314']+['ELM322']
write_text_if_changed(ROOT/'modeles/backlog/model.yaml',dumps(m))
a=read(HERE/'additions.yaml');a['market_comparisons']['BHV069']=c;write_text_if_changed(HERE/'additions.yaml',dumps(a))
s=read(HERE/'sources.yaml');s['sources'].append(dict(id='ELM322',market_ref='MKT13',element_type=c['element_type'],vendor=c['vendor'],product=c['product'],consulted_on='2026-09-19',**{k:v for k,v in c.items() if k.startswith('source_') and k!='source_refs'}));write_text_if_changed(HERE/'sources.yaml',dumps(s))
with (ROOT/'marche/elements.md').open('a',encoding='utf-8',newline='') as f:
    f.write('\n\n### ELM322\n\nU471 — MKT13, SAP S/4HANA Sales, ['+c['source_title']+']('+c['source_url']+'). '+c['source_version']+'. Passage primaire consulté le 19 septembre 2026 : '+c['source_locator']+'. Libellé natif : Advanced Intercompany Sales Processing ; processus produit, pas capacité native. Second appui distinct pour BHV069 (CMP186), à la place du doublon documentaire détecté lors du contrôle. ELM314 conserve la relecture de la première source Microsoft ; il ne compte pas comme un deuxième document. Reformulation et limites dans additions.yaml ; aucune règle comptable ou automatisation importée.\n')
# Correct the new, unpublished source registry count, without touching older records.
p=ROOT/'marche/catalogue.md';t=p.read_text(encoding='utf-8');t=t.replace('registre des 30 documents consultés','registre des 31 documents consultés');write_text_if_changed(p,t)
r=read(ROOT/'modeles/backlog/v0-readiness.yaml');r['source_refs']=list(dict.fromkeys(r['source_refs']+['U470','U471']));write_text_if_changed(ROOT/'modeles/backlog/v0-readiness.yaml',dumps(r))
for term in read(ROOT/'modeles/backlog/glossary.yaml')['terms']:
    if term['id'] in ['TER012','TER005']:print(term['id'],term['name'])

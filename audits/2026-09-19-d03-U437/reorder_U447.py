"""Reorder presentation only, keeping every element and relation value intact."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read,dumps
path=ROOT/'modeles/backlog/model.yaml';out=Path(__file__).parent/'model-before-order-U447.yaml'
assert not out.exists();out.write_bytes(path.read_bytes())
before=read(path);m=deepcopy(before)
domain_order=['business-references','D04','D01','D06','D15','D03','D05']
reference_order=['D08','D09','D12','D11','D13','D14']
for parent,order in [('universe-supply',domain_order),('business-references',reference_order)]:
    positions=[i for i,r in enumerate(m['relations']) if r['type']=='presents' and r['source_id']==parent]
    rels={m['relations'][i]['target_id']:m['relations'][i] for i in positions}
    assert set(rels)==set(order)
    for position,target in zip(positions,order):m['relations'][position]=rels[target]
# The Markdown renderer uses node-array order for domain/reference headings.
ordered_ids=reference_order+domain_order[1:]
positions=[i for i,n in enumerate(m['nodes']) if n['kind'] in ['domain','reference']]
nodes={n['id']:n for n in m['nodes']}
assert {m['nodes'][i]['id'] for i in positions}==set(ordered_ids)
for position,identifier in zip(positions,ordered_ids):m['nodes'][position]=nodes[identifier]
assert {x['id']:x for x in m['nodes']}=={x['id']:x for x in before['nodes']}
assert {x['id']:x for x in m['relations']}=={x['id']:x for x in before['relations']}
m['source_version']+=' + U447 ordre de lecture référentiels, base opérationnelle, promesse, optimisations'
for e in m['source_files']:e['sha256']=sha256((ROOT/e['path']).read_bytes()).hexdigest()
path.write_text(dumps(m),encoding='utf-8')
reading=dict(source_refs=['U447','U435'],status='presentation_applied',
    authority='model.yaml : ordre des relations presents pour Atlas ; ordre des nœuds domain/reference pour Markdown.',
    supply_presentation_order=domain_order,reference_presentation_order=reference_order,
    rationale=['Références de produits, parties, offres, accords, réseau et services avant les demandes et faits opérationnels.',
        'Demandes des Orders, puis ressources de stock et réalisation des services avant les engagements de promesse.',
        'Optimisation de satisfaction et optimisation des stocks en fin de lecture.'],
    limits='Ordre de lecture, pas workflow chronologique ni hiérarchie de domaines. Aucun identifiant, parent, champ métier, comportement ou accord changé.',
    model_before_sha256=sha256(out.read_bytes()).hexdigest(),
    atlas='L’Atlas conserve sa publication actuelle ; cet ordre sera porté par une prochaine release explicitement demandée.')
(ROOT/'modeles/backlog/reading-order-U447.yaml').write_text(dumps(reading),encoding='utf-8')
print('Presentation reordered only:', ' -> '.join(domain_order))
print('References:', ' -> '.join(reference_order))

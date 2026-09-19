from pathlib import Path
from hashlib import sha256
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.structured_io import read

root = Path(__file__).resolve().parents[2]
folder = Path(__file__).resolve().parent
protected = json.loads((folder / 'protected-files.json').read_text(encoding='utf-8-sig'))
differences = [name for name, digest in protected.items() if sha256((root / name).read_bytes()).hexdigest() != digest]
assert not differences, differences
before, after = read(folder / 'model-before.yaml'), read(root / 'modeles/backlog/model.yaml')
assert [n['id'] for n in before['nodes']] == [n['id'] for n in after['nodes']]
scopes = {'D14', 'D07.d', 'D06', 'D06.d', 'D06.f', 'BHV082'}
market = {'D04.o', 'BHV043'}
for old, new in zip(before['nodes'], after['nodes']):
    assert 'layer' not in new
    assert old['kind'] == new['kind']
    assert old.get('lifecycle') == new.get('lifecycle'), old['id']
    allowed = ({'scope'} if old['id'] in scopes else set()) | ({'market_comparisons'} if old['id'] in market else set())
    changed = {key for key in old['fields'].keys() | new['fields'].keys() if old['fields'].get(key) != new['fields'].get(key)}
    assert changed <= allowed, (old['id'], changed)
assert [(r['id'], r['source_id'], r['target_id'], r['type']) for r in before['relations']] == [(r['id'], r['source_id'], r['target_id'], r['type']) for r in after['relations']]
sys.path.insert(0, str(root / 'app'))
from modeling_guide import _validate_guide
guide = read(root / 'modeles/backlog/modeling-guide-U458.yaml')
_validate_guide(guide, guide['version'])
pilots = read(root / 'modeles/backlog/information-pilots-U458.yaml')
ids = {n['id'] for n in after['nodes']}
terms = {t['id'] for t in read(root / 'modeles/backlog/glossary.yaml')['terms']}
questions = {d['id'] for d in read(root / 'modeles/backlog/v0-readiness.yaml')['decisions']}
assert len(pilots['pilots']) == 5
for pilot in pilots['pilots']:
    assert pilot['node_ref'] in ids
    assert set(pilot.get('glossary_refs', [])) <= terms
    assert set(pilot.get('open_items', [])) <= questions
    if 'capability_ref' in pilot:
        assert pilot['capability_ref'] in ids
report = {'protected_files_unchanged': len(protected), 'nodes_preserved': len(after['nodes']), 'node_lifecycles_unchanged': True, 'relation_identities_and_endpoints_unchanged': len(after['relations']), 'layers_removed': len(after['nodes']), 'guide_draft_valid': guide['version'], 'pilot_references_valid': 5, 'publication_changed': False}
(folder / 'invariants-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report))

# Generated review view, not a second editable catalogue.
lines = ['# Cinq pilotes — support de revue', '', 'Vue générée depuis `modeles/backlog/information-pilots-U458.yaml`. Propositions internes, sans publication ni adoption globale.', '']
names = {n['id']: n['fields']['name'] for n in after['nodes']}
for pilot in pilots['pilots']:
    lines += ['## ' + names[pilot['node_ref']], '', pilot['result'], '', '**Responsabilités**', '']
    lines += ['- ' + x for x in pilot['responsibilities']]
    lines += ['', '**Frontières**', ''] + ['- ' + x for x in pilot['boundaries']]
    lines += ['', '**Informations à éprouver**', '']
    lines += ['- **' + x['name'] + '** : ' + x['role'] + (' Informations utiles : ' + ', '.join(x.get('essentials', [])) + '.' if x.get('essentials') else '') for x in pilot['information_candidates']]
    if 'projection' in pilot:
        lines += ['', '**Projection**', ''] + ['- ' + value for value in pilot['projection'].values()]
    lines += ['', '**Exemple fictif.** ' + pilot['example'], '', 'Questions : ' + ', '.join(pilot['open_items']) + '.', '']
lines += ['## Coopération Commerce–Supply–logistique', '', pilots['scenario']['qualification'], '']
lines += [f'{i}. {step}' for i, step in enumerate(pilots['scenario']['steps'], 1)]
lines += ['', '**Refus et écarts**', ''] + ['- ' + step for step in pilots['scenario']['exceptions']]
(folder / 'pilotes.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

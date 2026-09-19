"""Contrôles ciblés des changements U460/U461 et lecture dérivée des cinq pilotes."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
FOLDER = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'app'))
from scripts.structured_io import read, write_text_if_changed
from scripts.validate_models import _source_refs
from modeling_guide import _validate_guide

before = read(FOLDER / 'before/modeles/backlog/model.yaml')
model = read(ROOT / 'modeles/backlog/model.yaml')
nodes = {n['id']: n for n in model['nodes']}
glossary_before = read(FOLDER / 'before/modeles/backlog/glossary.yaml')
glossary = read(ROOT / 'modeles/backlog/glossary.yaml')
terms = {t['id']: t for t in glossary['terms']}
pilots = read(ROOT / 'modeles/backlog/information-pilots-U458.yaml')
readiness = read(ROOT / 'modeles/backlog/v0-readiness.yaml')
questions = {q['id']: q for q in readiness['decisions']}
sources = {s['id']: s for s in read(ROOT / 'modeles/provenance/source-records.json')['records']}

protected = {}
for manifest in ['2026-09-19-plan-U458', '2026-09-19-atlas-U459']:
    protected.update(read(ROOT / f'audits/{manifest}/protected-files.json'))
assert all(sha256((ROOT / path).read_bytes()).hexdigest() == digest for path, digest in protected.items())
assert before['relations'] == model['relations']
assert before['alternatives'] == model['alternatives']
assert before['principles'] == model['principles'][:-1]
assert model['principles'][-1]['id'] == 'PRINCIPLE-MANAGEMENT-FACT-DOCUMENT'
assert [n['id'] for n in before['nodes']] == list(nodes)
node_changes = []
for old in before['nodes']:
    new = nodes[old['id']]
    changed = {k for k in old.keys() | new.keys() if old.get(k) != new.get(k)}
    if not changed:
        continue
    assert old['id'] in ['D08', 'D08.d', 'D03.n'], old['id']
    assert changed <= {'fields', 'source_refs', 'revision', 'proposed_fields'}, changed
    fields = {k for k in old['fields'].keys() | new['fields'].keys() if old['fields'].get(k) != new['fields'].get(k)}
    assert fields == {'market_comparisons'}, fields
    assert old.get('lifecycle') == new.get('lifecycle')
    assert old.get('review') == new.get('review')
    assert old.get('approved_fields') == new.get('approved_fields')
    assert new['revision'] == old['revision'] + 1
    node_changes.append(old['id'])
assert node_changes == ['D08', 'D08.d', 'D03.n']

assert [t['id'] for t in glossary_before['terms']] == list(terms)
term_changes = []
for old in glossary_before['terms']:
    new = terms[old['id']]
    changed = {k for k in old.keys() | new.keys() if old.get(k) != new.get(k)}
    if not changed:
        continue
    assert old['id'] in ['TER036','TER037','TER052','TER057','TER058','TER059']
    assert changed <= {'context','market_comparisons','source_refs','revision'}, changed
    assert new['review'] == old['review']
    assert new['definition'] == old['definition']
    term_changes.append(old['id'])

guide = read(ROOT / 'modeles/backlog/modeling-guide-U458.yaml')
_validate_guide(guide, guide['version'])
assert not _source_refs(pilots, sources)
assert not _source_refs(readiness, sources)
assert questions['V0-P01']['status'] == 'principle_resolved_U461'
assert len(pilots['pilots']) == 5
pilot_ids = {p['id'] for p in pilots['pilots']}
cases = pilots['review_U460']['cases']
assert len({c['id'] for c in cases}) == len(cases) == 15
assert set(Counter(c['pilot'] for c in cases).values()) == {3}
for pilot in pilots['pilots']:
    assert pilot['node_ref'] in nodes
    assert set(pilot.get('glossary_refs', [])) <= terms.keys()
    assert set(pilot['open_items']) <= questions.keys()
    if 'capability_ref' in pilot:
        assert nodes[pilot['capability_ref']]['kind'] == 'capability'
    for row in pilot['information_responsibilities']:
        assert nodes[row['node_ref']]['kind'] == 'capability'
for case in cases:
    assert case['pilot'] in pilot_ids
    assert set(case['open_items']) <= questions.keys()
    assert (case['status'] == 'business_rule_open') == bool(case['open_items'])

counts = Counter(c['status'] for c in cases)
proof = dict(protected_files_unchanged=len(protected), nodes_preserved=len(nodes),
             relations_unchanged=len(model['relations']), node_changes=node_changes,
             term_context_changes=term_changes, definitions_and_approval_states_preserved=True,
             new_comparisons=4, new_principles=1, pilot_count=5, case_count=15,
             review_cases=dict(counts), guide_draft_valid=guide['version'],
             source_and_pilot_references_valid=True, publication_changed=False)
write_text_if_changed(FOLDER / 'verification.json', json.dumps(proof, ensure_ascii=False, indent=2) + '\n')

lines = ['# Cinq pilotes métier — revue U460/U461', '',
    'Lecture générée depuis [information-pilots-U458.yaml](../../modeles/backlog/information-pilots-U458.yaml). Le YAML reste la source. Exemples fictifs et descriptions proposées ; aucune réalisation installée supposée.', '',
    '**Décision retenue (U461).** Tout fait de gestion est associé à un document métier identifié, éventuellement structuré sans PDF. Les règles de version, correction et nombre exact de documents restent à préciser.', '',
    '**Résultat de la revue documentaire.** Quinze cas : sept expliquent une frontière déjà posée ; huit exposent une règle métier encore ouverte. Ce travail ne remplace pas une relecture PO/expert.', '',
    '| Notion | Question à laquelle elle répond |', '| --- | --- |',
    '| Attendu de commande | Que demande-t-on ? |',
    '| Fulfillment Commitment | Que propose-t-on ou que s’engage-t-on à satisfaire ? |',
    '| Supply Assignment | Quelles ressources sont retenues pour quelles commandes ? |',
    '| Reservation | Quelle ressource est engagée de manière opposable aux usages concurrents ? |',
    '| Fait de gestion et document associé | Que constate-t-on, et quel document identifié le consigne ? |', '']
assert counts == {'boundary_explained': 7, 'business_rule_open': 8}
for pilot in pilots['pilots']:
    name = nodes[pilot['node_ref']]['fields']['name']
    lines += [f'## {name}', '', pilot['result'], '', '**Responsabilités et frontières**', '']
    lines += ['- ' + s for s in pilot['responsibilities'] + pilot['boundaries']]
    lines += ['', '**Informations à éprouver**', '']
    for item in pilot['information_candidates']:
        lines += [f"- **{item['name']}** : {item['role']} " +
                  ('Informations utiles : ' + ', '.join(item['essentials']) + '. ' if item.get('essentials') else '') + item['granularity']]
    lines += ['', '**Responsabilités sur les informations — propositions de lecture**', '',
              '| Information | Responsabilité | Intervention et limite |', '| --- | --- | --- |']
    for row in pilot['information_responsibilities']:
        lines += [f"| {row['information']} | {nodes[row['node_ref']]['fields']['name']} | {row['role']}. {row['boundary']} |"]
    if 'projection' in pilot:
        labels = {'authority':'Autorité métier','feeding_source':'Source d’alimentation','context':'Contexte',
                  'freshness':'Fraîcheur utile','contradiction':'Contradiction','missing_information':'Information absente','validity':'Validité'}
        lines += ['', '**Projection : informations à distinguer**', '']
        lines += [f'- **{labels[k]}** : {v}' for k,v in pilot['projection'].items()]
    lines += ['', '**Exemple fictif.** ' + pilot['example'], '', '**Cas de revue**', '']
    for case in (c for c in cases if c['pilot']==pilot['id']):
        state = 'Règle à préciser : ' + ', '.join(case['open_items']) if case['open_items'] else 'Frontière expliquée par le modèle courant'
        lines += [f"### {case['title']}", '', case['given'], '', case['reading'], '',
                  '**Limite.** ' + case['boundary'], '', '**Conclusion documentaire.** ' + state + '.', '']

lines += ['## Repères marché', '', 'Rapprochements proposés, maintenant portés par les fiches du backlog ; ils attendent une publication pour apparaître dans Atlas.', '']
for identifier, entries in [('D08', nodes['D08']['fields']['market_comparisons']), ('D08.d', nodes['D08.d']['fields']['market_comparisons']),
                            ('TER059', terms['TER059']['market_comparisons']), ('TER036', terms['TER036']['market_comparisons'])]:
    for entry in entries:
        lines += [f"- **{identifier} — {entry['relationship']}** : [{entry['source_title']}]({entry['source_url']}). {entry['flow_position']}"]
lines += ['', 'Réservations et liens aux demandes confirmées : documentation Microsoft relue, ELM283/284. Les rapprochements déjà présents sur Reservation et Supply Assignment restent distincts des règles FLOW.', '',
          '## Questions restantes', '']
for key in ['V0-P02','V0-P03','V0-A01','V0-A02','V0-A06']:
    lines += [f"- **{key}** : {questions[key]['remaining']}"]
lines += ['', pilots['review_U460']['next_step'], '']
write_text_if_changed(FOLDER / 'pilotes.md', '\n'.join(lines))
print(json.dumps(proof, ensure_ascii=True))

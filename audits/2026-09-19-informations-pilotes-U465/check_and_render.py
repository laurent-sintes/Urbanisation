"""Contrôle ciblé du pilote et restitution dérivée de son annexe YAML."""
from pathlib import Path
from hashlib import sha256
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, write_text_if_changed
from app.modeling_guide import _validate_guide

sys.stdout.reconfigure(encoding='utf-8')
catalogue = read(ROOT / 'modeles/backlog/information-cards-U465.yaml')
pilots = read(ROOT / 'modeles/backlog/information-pilots-U458.yaml')
before = read(AUDIT / 'before/modeles/backlog/information-pilots-U458.yaml')
model = read(ROOT / 'modeles/backlog/model.yaml')
nodes = {n['id']: n for n in model['nodes']}
sources = {r['id'] for r in read(ROOT / 'modeles/provenance/source-records.json')['records']}
cards = {c['id']: c for c in catalogue['cards']}
supports = {s['id']: s for s in catalogue['market_support']}
pilot_ids = {p['id'] for p in pilots['pilots']}
assert len(cards) == len(catalogue['cards'])
assert len(supports) == len(catalogue['market_support'])
assert len({c['name'] for c in cards.values()}) == len(cards)


def check_sources(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key == 'source_refs':
                assert set(item) <= sources, (key, set(item) - sources)
            elif key == 'source_ref':
                assert item in sources, item
            check_sources(item)
    elif isinstance(value, list):
        for item in value:
            check_sources(item)


check_sources(catalogue)
for card in cards.values():
    assert card['pilot_ref'] in pilot_ids
    assert card['market_comparison']['support_ref'] in supports
    for role in card['capability_roles']:
        assert nodes[role['capability_ref']]['kind'] == 'capability', role
    for field in ['question', 'definition', 'context', 'essential_elements', 'granularity_rationale', 'example']:
        assert card[field], (card['id'], field)
    assert card['review']['definition'] == 'proposed'
assert {c['id'] for c in cards.values() if c['review'].get('adopted_scope')} == {'PINFO-011', 'PINFO-012'}
assert len({l['id'] for l in catalogue['links']}) == len(catalogue['links'])
for link in catalogue['links']:
    assert link['from_ref'] in cards and link['to_ref'] in cards
    assert all(link[k] for k in ['meaning','condition','effect','source_refs'])

old_cases = {c['id']: c for c in before['review_U460']['cases']}
assert pilots['review_U460'] == before['review_U460'], 'La revue historique doit rester intacte.'
assert {c['case_ref'] for c in catalogue['case_coverage']} == set(old_cases)
assert len(catalogue['case_coverage']) == len(old_cases)
for case in catalogue['case_coverage']:
    old = old_cases[case['case_ref']]
    assert set(case['information_refs']) <= cards.keys()
    assert case['pilot_ref'] == old['pilot']
    assert case['open_items'] == old['open_items']
    assert case['prior_status'] == old['status']
for example in catalogue['additional_examples']:
    assert set(example['information_refs']) <= cards.keys()
assert len({e['id'] for e in catalogue['additional_examples']}) == len(catalogue['additional_examples'])
for current, old in zip(pilots['pilots'], before['pilots'], strict=True):
    assert current['information_candidates'] == old['information_candidates']
    assert set(current['information_card_refs']) == {c['id'] for c in cards.values() if c['pilot_ref'] == current['id']}
    # Ajouts U465/U466 seulement ; aucun accord ou responsabilité historique réécrit.
    for key, val in old.items():
        if key == 'source_refs':
            assert current[key][:len(val)] == val
        else:
            assert current[key] == val, (current['id'], key)

meta = read(ROOT / 'modeles/backlog/modeling-glossary.yaml')
old_meta = read(AUDIT / 'before/modeles/backlog/modeling-glossary.yaml')
assert [t for t in meta['terms'] if t['id'] != 'MOD012'] == [t for t in old_meta['terms'] if t['id'] != 'MOD012']
term = next(t for t in meta['terms'] if t['id'] == 'MOD012')
assert term['definition'] == next(t for t in old_meta['terms'] if t['id'] == 'MOD012')['definition']
guide = read(ROOT / 'modeles/backlog/modeling-guide-U458.yaml')
_validate_guide(guide, guide['version'])
guide_term = next(t for t in guide['glossary']['terms'] if t['id'] == 'MOD012')
assert guide_term['definition'] == term['definition']
assert guide_term['examples'] == term['examples']
check_sources(meta)

protected = read(AUDIT / 'protected-files.json')
changed = [p for p, digest in protected.items() if sha256((ROOT / p).read_bytes()).hexdigest() != digest]
assert not changed, changed
result = dict(status='passed', cards=len(cards), pilots=len(pilot_ids),
              links=len(catalogue['links']), capability_roles=sum(len(c['capability_roles']) for c in cards.values()),
              market_supports=len(supports), inherited_cases=len(old_cases),
              additional_examples=len(catalogue['additional_examples']),
              preserved_files=len(protected), source_references='resolved', capability_references='resolved',
              prior_candidates_and_review='preserved', prior_method_terms='preserved',
              general_information_definition='unchanged_proposal', draft_guide='valid',
              adoption='U466 distinction and coexistence only', human_review='not_performed')
write_text_if_changed(AUDIT / 'verification.json', json.dumps(result, ensure_ascii=False, indent=2) + '\n')

lines = [
    '# Informations métier — cinq pilotes U465/U466', '',
    '19 septembre 2026. Restitution dérivée de [l’annexe YAML du backlog](../../modeles/backlog/information-cards-U465.yaml), qui fait autorité pour ces propositions. Ce document est un support de lecture interne, pas une publication Atlas.', '',
    '## Ce qui est maintenant explicite', '',
    '**Proposition de satisfaction et engagement de satisfaction sont deux informations métier reliées.** U466 adopte cette distinction : une nouvelle proposition peut être examinée pendant que l’engagement actuel reste valable. Les noms anglais et les définitions détaillées restent des rédactions proposées.', '',
    f'Les cinq pilotes portent **{len(cards)} fiches, {len(catalogue["links"])} liens qualifiés et {result["capability_roles"]} contributions de capacités**. Chaque fiche explicite une question, son contexte minimal, son exemple et les raisons de ses choix de vocabulaire et de définition. Les 15 cas antérieurs sont repris ; quatre exemples complètent l’épreuve de granularité. Aucun résultat de recette humaine n’est revendiqué.', '',
    'Le découpage sépare des sens utiles : demandé, répondu, accepté, constaté, restant ; référence, caractéristique, identifiant, autorité, réception ; proposé, engagé, affecté, réservé. Ces informations sont transverses aux capacités. Elles ne forment ni une nouvelle couche ni un niveau sous Comportement.', '',
    '## Vue d’ensemble', '',
    '| Pilote | Information proposée | Question métier |', '| --- | --- | --- |',
]
for c in cards.values():
    lines.append(f'| {c["pilot_ref"].removeprefix("PILOT-").title()} | [{c["name"]}](#{c["id"].lower()}) — {c["label_fr"]} | {c["question"]} |')
lines += ['', '## Comment lire ces fiches', ''] + [f'- {r}' for r in catalogue['reading_rules']]
lines += ['', '**Critère de maille.** Chaque fiche explique un sens autonome, avec les liens nécessaires à sa compréhension. Un ensemble de plusieurs échéances peut réunir plusieurs occurrences d’information ; le choix de cette maille ne démontre pas une irréductibilité logique. Il ne prescrit pas davantage un enregistrement ou une mise à jour technique indivisible.', '',
          '**Documents et faits.** Purchase Order reste un objet métier, et les documents d’achat ou de réception gardent leur nature. Les fiches d’information en explicitent le contenu. Le résultat de réception associé à un fait de gestion conserve son document identifié, conformément à U461. Ni un poids produit ni un solde calculé ne deviennent automatiquement des faits de gestion.', '',
          '## Les fiches', '']
for c in cards.values():
    lines += [f'<a id="{c["id"].lower()}"></a>', '', f'### {c["name"]} — {c["label_fr"]}', '',
              f'**Question :** {c["question"]}', '', c['definition'], '',
              f'**Contexte :** {c["context"]}', '', '**Éléments qui portent le sens :**', '']
    lines += [f'- {e}' for e in c['essential_elements']]
    lines += ['', f'**Pourquoi cette maille :** {c["granularity_rationale"]}', '',
              '**Frontières :** ' + ' '.join(c['separate_meanings']), '', '**Capacités concernées :**', '']
    for role in c['capability_roles']:
        lines.append(f'- {nodes[role["capability_ref"]]["fields"]["name"]} ({role["capability_ref"]}) **{role["role"]}** : {role["meaning"]}')
    lines += ['', '**Exemple illustratif :** ' + c['example']['text'], '',
              '**Terme retenu :** ' + c['market_comparison']['term_choice'], '',
              '**Définition et marché :** ' + c['market_comparison']['definition_choice'], '',
              f'Appui : [{c["market_comparison"]["support_ref"]}](#{c["market_comparison"]["support_ref"].lower()}). Origines : ' + ', '.join(c['source_refs']) + '.', '',
              '**Document / fait :** ' + c['document_and_fact_boundary'], '',
              '**À préciser :** ' + (', '.join(c['open_items']) or 'Aucune règle nouvelle identifiée comme indispensable à cet exemple ; la fiche reste proposée.') + '.', '']
    if c['review'].get('adopted_scope'):
        lines += ['**Portée U466 :** distinction et coexistence adoptées ; noms, rédaction et règles détaillées proposés.', '']
lines += ['## Liens : sens, conditions et effets', '',
          'Ces liens sont propres au pilote. Ils ne remplacent pas les relations publiées et n’infèrent pas un flux technique depuis une dépendance.', '']
for link in catalogue['links']:
    lines += [f'### {link["id"]} — {cards[link["from_ref"]]["name"]} → {cards[link["to_ref"]]["name"]}', '',
              f'**Sens :** {link["meaning"]}.', '', f'**Condition :** {link["condition"]}', '',
              f'**Effet :** {link["effect"]}', '', 'Origines : ' + ', '.join(link['source_refs']) + '.', '']
lines += ['## Épreuve des cas déjà préparés', '',
          'Cette matrice vérifie la capacité explicative du découpage. Les questions ouvertes et les résultats antérieurs de U460 sont conservés ; aucun cas ouvert n’est déclaré résolu par la seule rédaction.', '',
          '| Cas | Lecture avec les informations | Règles encore ouvertes |', '| --- | --- | --- |']
for case in catalogue['case_coverage']:
    lines.append(f'| {case["case_ref"]} — {case["title"]} | {case["reading"]} ({", ".join(case["information_refs"])}) | {", ".join(case["open_items"]) or "Frontière expliquée, sans recette humaine"} |')
lines += ['', '### Exemples supplémentaires', '']
for case in catalogue['additional_examples']:
    lines += [f'**{case["title"]}.** {case["example"]} {case["expected_reading"]}', '']
lines += ['## Références et positionnement', '',
          'Les références suivantes apportent des exemples et des concepts. Elles ne constituent ni une sélection de produits ni une preuve d’implémentation. Les mots descriptifs FLOW ne sont qualifiés ni standards ni innovants en l’absence de preuve. Les sources d’architecture de U464 restent des appuis méthodologiques, distincts des exemples éditeurs.', '']
for s in supports.values():
    lines += [f'<a id="{s["id"].lower()}"></a>', '', f'### {s["id"]}', '',
              f'**Constat sourcé :** {s["observed"]}', '', f'**Point commun :** {s["common_ground"]}', '',
              f'**Différence et limite FLOW :** {s["flow_difference"]}', '']
    for src in s['sources']:
        lines += [f'- [{src["title"]}]({src["url"]}) — {src["locator"]}. Consultation : {src["consulted_on"]}. {src["limit"]}']
    lines += ['', 'Traçabilité : ' + ', '.join(s['source_refs']) + ' ; CMP184. Rapprochement proposé par Codex.', '']
lines += ['## Bilan et suite', '', catalogue['recommendation']['result'], '',
          '**Modifications opérées :** catalogue pilote créé ; cinq pilotes reliés aux fiches tout en préservant leurs candidats initiaux ; exemple U466 ajouté à MOD012 et au brouillon du guide ; arbitrage, correspondances marché et suivi V0 actualisés. La définition générale de MOD012 reste inchangée et proposée.', '',
          '**Prochaine étape recommandée :** ' + catalogue['recommendation']['next_step'], '',
          '**Questions métier conservées :**', '']
lines += [f'- {q}' for q in catalogue['recommendation']['open_business_rules']]
lines += ['', catalogue['recommendation']['human_review'], '',
          '**Contrôles ciblés réussis :** sources, capacités, liens, couverture des quinze cas, conservation des candidats et de leur revue antérieure, cohérence MOD012/guide. Les 306 empreintes protégées sont identiques, dont le catalogue métier, son glossaire, son schéma et 303 fichiers historiques. [Résultats du contrôle](verification.json).', '',
          'Atlas reste sur sa publication actuelle : aucune fiche pilote n’est lue depuis le backlog. Aucun nouveau type canonique, changement UI ou publication n’est réalisé dans cette étape.', '']
execution_path = AUDIT / 'execution-checks.json'
if execution_path.exists():
    execution = read(execution_path)
    assert all(c['exit_code'] == 0 for c in execution['commands'])
    lines += ['**Validation et tests exécutés :** validation des modèles à zéro erreur ; 17 tests du guide réussis, 1 ignoré car Windows n’autorise pas la création de liens symboliques. Index des sources actualisé à 1 681 entrées. [Trace des commandes](execution-checks.json). Aucun build frontend requis pour ces modifications documentaires.', '']
write_text_if_changed(AUDIT / 'rapport.md', '\n'.join(lines))
print(json.dumps(result, ensure_ascii=False))

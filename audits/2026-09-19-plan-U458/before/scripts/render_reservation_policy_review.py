"""Render the U342 review from authoritative YAML; do not edit the derived report."""
from pathlib import Path
from scripts.structured_io import read

ROOT = Path(__file__).resolve().parents[1]


def main():
    r = read(ROOT/'modeles/backlog/reservation-policy-review.yaml')
    m = read(ROOT/'modeles/backlog/model.yaml')
    nodes = {n['id']: n for n in m['nodes']}
    cap = nodes[r['capability_id']]
    adopted = 'adoption_U343' in r
    status = ('**U342/U343 : capacité, quatre comportements et rattachement D05 adoptés dans la portée présentée. Les responsabilités résumées sont validées ; définitions développées, modalités, contrats et comparaisons restent éditoriaux.**'
              if adopted else '**U342 : nom et définition de la capacité adoptés. Les quatre comportements, leurs descriptions et le rattachement à D05 sont proposés.**')
    rows = ['# Reservation Policy Decision — comportements et portée de validation', '',
        'Restitution dérivée de [reservation-policy-review.yaml](../../modeles/backlog/reservation-policy-review.yaml) et du [catalogue](../../modeles/backlog/model.yaml).', '',
        status, '',
        '> ' + cap['fields']['definition'], '', r['scope_limit'], '',
        '## Pourquoi ces comportements', '', r['decomposition_rationale'], '',
        '| Comportement | Mécanisme | Bénéfice |', '| --- | --- | --- |']
    for e in r['behaviors']:
        n = nodes[e['node_id']]
        assert n['lifecycle']['validated_fields'] == (['name'] if adopted else [])
        assert [x['source_id'] for x in m['relations'] if x['type']=='contains' and x['target_id']==e['node_id']] == [cap['id']]
        rows.append(f"| {n['fields']['name']} | {e['criterion']} | {e['benefit']} |")
    for e in r['behaviors']:
        n = nodes[e['node_id']]
        rows += ['', '## ' + n['fields']['name'] + ' — ' + n['id'], '']
        if adopted:
            rows += ['**Responsabilité adoptée U343.** ' + e['adopted_responsibility'], '', '**Définition développée, éditoriale.**', '']
        rows += [n['fields']['definition'], '',
                 '**Mécanisme.** ' + e['mechanism'], '', '**Bénéfice.** ' + e['benefit'], '', '**Entrées.**', '']
        rows += ['- ' + text for text in e['inputs']]
        rows += ['', '**Résultats.**', ''] + ['- ' + text for text in e['outputs']]
        rows += ['', e['example'], '', '**Frontières.** ' + e['boundary'], '', '**Niveau de preuve.** ' + e['evidence'], '']
        for c in n['fields']['market_comparisons']:
            rows += [f"- [{c['vendor']} — {c['element_name']}]({c['source_url']}) ({c['source_version']}, consulté le {c['consulted_on']}). {c['similarities']} Limites : {c['differences']}"]
    rows += ['', '## Combiner les mécanismes', '', r['combination_example'], '',
             'Les paramètres communs précisent bénéficiaire, contexte, déclencheur, horizon avant le besoin, validité après réservation, maintien, libération et réexamen. Une recommandation doit être mise en vigueur par le management responsable avant application. Les engagements déjà accordés gardent leurs conditions.', '',
             '## Recensement des variantes et limites du découpage', '',
             'Chaque ligne indique où documenter le cas ; les lignes ne sont pas des comportements supplémentaires.', '',
             '| Cas examiné | Traitement retenu | Justification et frontière |', '| --- | --- | --- |']
    for c in r['coverage']:
        rows.append(f"| {c['topic']} | {c['disposition']} | {c['rationale']} |")
    parent = r['adopted_parent'] if adopted else r['proposed_parent']
    rows += ['', '## Rattachement et relations', '', ('**Parent adopté U343 : D05 Inventory Optimization.** ' if adopted else '**Parent proposé : D05 Inventory Optimization.** ') + parent['rationale'], '',
             '| Consommateur | A besoin de | Sens proposé |', '| --- | --- | --- |']
    for rel in m['relations']:
        if rel['type']=='relates-to' and cap['id'] in [rel['source_id'], rel['target_id']]:
            rows.append(f"| {nodes[rel['source_id']]['fields']['name']} | {nodes[rel['target_id']]['fields']['name']} | {rel['qualification']['meaning']} |")
    rows += ['', '## Arbitrages ouverts', ''] + ['- '+q for q in r['open_questions']]
    rows += ['', 'Aucun changement d’une publication ; l’Atlas continuera à présenter la release courante jusqu’à une nouvelle publication demandée.']
    path = ROOT/'audits/2026-09-18-reservation-policy/README.md'
    path.write_text('\n'.join(rows)+'\n', encoding='utf-8')
    print('Rendered:', path)


if __name__ == '__main__':
    main()

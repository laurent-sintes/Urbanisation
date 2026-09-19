"""Render reading views from the current structured models. No business data is edited."""
import json
from collections import Counter
from pathlib import Path
try:
    from .release_catalog import resolve_release
    from .lifecycle import lifecycle_label
except ImportError:
    from release_catalog import resolve_release
    from lifecycle import lifecycle_label

ROOT = Path(__file__).resolve().parents[1]
LABELS = {'accepted':'Validé','partial':'Partiellement validé','proposed':'Non validé','under_review':'En réexamen','illustration':'Illustration'}


def status(item):
    label = lifecycle_label(item)
    if label:
        scope = item['lifecycle'].get('validated_fields', [])
        return label + (' — portée : ' + ', '.join(scope) if scope else '')
    return LABELS[item['review']['state']]


try:
    from .structured_io import read, working_path, write_text_if_changed
except ImportError:
    from structured_io import read, working_path, write_text_if_changed


def cell(value):
    return str(value).replace('|','\\|').replace('\n',' ')


def market_lines(entries):
    lines = []
    for entry in entries:
        lines += [f"### {entry['vendor']} — {entry['element_name']}", '',
                  f"{entry['product']} · {entry['element_type']} · {entry['relationship']} · statut : {entry['status']}", '',
                  '**Points communs.** ' + entry['similarities'], '',
                  '**Différences.** ' + entry['differences'], '',
                  '**Position FLOW.** ' + entry['flow_position'], '',
                  f"[{entry['source_title']}]({entry['source_url']}) — {entry['source_version']}, consulté le {entry['consulted_on']}.", '',
                  '**Passage.** ' + entry['source_locator'], '',
                  '**Limite de preuve.** ' + entry['evidence_limits'], '',
                  'Références : ' + ', '.join(entry['source_refs']) + '.', '']
    return lines


def render(model, label):
    lines = [f'# {label} — {model["version"]}', '', f'Restitution générée depuis le modèle structuré, connaissance au {model["as_of"]}. Ne pas éditer cette vue pour modifier le modèle.', '', 'Publication et validation sont distinctes. Le statut d’un rattachement peut différer de celui de la capacité.', '']
    nodes = {n['id']:n for n in model['nodes']}
    universes = [n for n in model['nodes'] if n.get('group_role') == 'urbanism_level']
    if universes:
        lines += ['## Niveaux d’urbanisation', '', '| Repère | Nom | Niveau | Contenu direct | Statut |', '| --- | --- | --- | --- | --- |']
        for universe in universes:
            children = [nodes[r['target_id']]['fields'].get('name', r['target_id']) for r in model['relations'] if r['type'] == 'presents' and r['source_id'] == universe['id']]
            lines.append('| ' + ' | '.join(cell(v) for v in [universe['id'], universe['fields'].get('name', ''), universe['level_ref'], ', '.join(children) or 'Exploration différée', status(universe)]) + ' |')
        lines += ['', 'Les groupes de présentation, dont Business References, conservent leur rôle distinct.', '']
    for domain in model['nodes']:
        if domain['kind'] not in ('domain','reference'):
            continue
        lines += [f'## {domain["id"]} — {domain["fields"].get("name", "Libellé à préciser")}', '', f'Statut : **{status(domain)}**.', '', domain['fields'].get('definition','Définition à préciser.'), '', '| Repère | Capacité | Statut | Définition | Finalité | Rattachement |', '| --- | --- | --- | --- | --- | --- |']
        for relation in model['relations']:
            if relation['type'] != 'contains' or relation['source_id'] != domain['id']:
                continue
            n=nodes[relation['target_id']]; f=n['fields']
            lines.append('| '+ ' | '.join(cell(v) for v in [n['id'], f.get('name','Libellé à préciser'), status(n),f.get('definition','À préciser'),f.get('finality','À préciser'),status(relation)])+' |')
        lines += ['']
    for capability in model['nodes']:
        behaviors = [nodes[r['target_id']] for r in model['relations']
                     if r['type'] == 'contains' and r['source_id'] == capability['id']
                     and nodes[r['target_id']]['kind'] == 'behavior']
        if not behaviors:
            continue
        rationale = capability['fields'].get('decomposition_rationale')
        if rationale:
            lines += [f'**Justification de la décomposition — {capability["id"]} :** {rationale}', '']
        lines += [f'## Comportements — {capability["fields"].get("name", capability["id"])}', '',
                  'Dernier niveau de détail de la capacité ; les comportements ne sont pas des capacités supplémentaires.', '',
                  '| Repère | Comportement | Statut | Définition |', '| --- | --- | --- | --- |']
        for behavior in behaviors:
            lines.append('| ' + ' | '.join(cell(v) for v in [behavior['id'], behavior['fields']['name'], status(behavior), behavior['fields']['definition']]) + ' |')
        lines += ['']
    for node in model['nodes']:
        entries = node['fields'].get('market_comparisons', [])
        if entries:
            lines += [f"## Comparaison par rapport au marché — {node['id']} {node['fields'].get('name', '')}", ''] + market_lines(entries)
    for term in model.get('glossary', {}).get('terms', []):
        if term.get('market_comparisons'):
            lines += [f"## Comparaison par rapport au marché — {term['name']}", ''] + market_lines(term['market_comparisons'])
    if model['space']=='release':
        lines += ['## Portée des validations', '', '| Repère | Champs adoptés | Champs restant proposés | Décisions |', '| --- | --- | --- | --- |']
        for n in model['nodes']:
            lines.append('| '+ ' | '.join(cell(v) for v in [n['id'],', '.join(n.get('approved_fields',[])) or 'Aucun',', '.join(n.get('proposed_fields',[])) or 'Aucun',', '.join(n.get('adoption_ids',[])) or 'Aucune'])+' |')
        lines += ['', 'Les validations contextuelles et les réserves détaillées restent dans les décisions et les sources JSON.', '']
    return '\n'.join(lines)


def main(space='all'):
    destination = ROOT/'restitutions'
    destination.mkdir(exist_ok=True)
    generated = []
    if space in ('all', 'release'):
        pointer = resolve_release(ROOT/'modeles/release')
        release = read(ROOT/'modeles/release'/pointer['path'])
        write_text_if_changed(destination/'release.md', render(release, 'Release'))
        generated.append('release')
    if space in ('all', 'backlog'):
        backlog = read(working_path(ROOT/'modeles/backlog'))
        backlog['glossary'] = read(working_path(ROOT/'modeles/backlog', 'glossary'))
        write_text_if_changed(destination/'backlog.md', render(backlog, 'Backlog'))
        generated.append('backlog')
    if space in ('all', 'panorama-as-is'):
        render_panorama(destination)
        generated.append('panorama-as-is')
    print('Views checked/generated: ' + ', '.join(generated))


def render_panorama(destination):
    index=read(ROOT/'modeles/panorama-as-is/current.json')
    lines=['# Panorama As Is', '', 'Restitution générée depuis les JSON. La consolidation ne prouve pas une observation récente du déploiement.', '', '| SI | Évaluation | Composants et mentions | Flux | Autorités d’information | Responsabilités de décision |', '| --- | --- | --- | --- | --- | --- |']
    for p in index['panoramas']:
        data=read(ROOT/p['path'])
        name=data.get('name') or data.get('canonical_name') or {'beaumanoir-historique-si':'Périmètre historique de Beaumanoir','boardriders-si':'Boardriders','sarenza-si':'Sarenza'}[data['model_id']]
        counts=[len(data[k]) for k in ['objects','flows','information_authorities','decision_responsibilities']]
        lines.append('| '+' | '.join(map(str,[name,'Non traité' if data['assessment_status']=='not_assessed' else 'Partiellement documenté']+counts))+' |')
    lines += ['', 'Le contexte partagé, notamment C-Log, reste dans son fichier distinct. Les besoins et orientations non établis comme existant sont conservés dans le backlog.', '']
    write_text_if_changed(destination/'panorama-as-is.md', '\n'.join(lines))


if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--space', choices=['all', 'backlog', 'release', 'panorama-as-is'], default='all')
    main(parser.parse_args().space)

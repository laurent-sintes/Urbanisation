"""Render reading views from the current JSON models. No business data is edited."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {'accepted':'Validé','partial':'Partiellement validé','proposed':'Non validé','under_review':'En réexamen','illustration':'Illustration'}


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def cell(value):
    return str(value).replace('|','\\|').replace('\n',' ')


def render(model, label):
    lines = [f'# {label} — {model["version"]}', '', f'Restitution générée depuis le JSON, connaissance au {model["as_of"]}. Ne pas éditer cette vue pour modifier le modèle.', '', 'Publication et validation sont distinctes. Le statut d’un rattachement peut différer de celui de la capacité.', '']
    nodes = {n['id']:n for n in model['nodes']}
    for domain in model['nodes']:
        if domain['kind'] not in ('domain','reference'):
            continue
        lines += [f'## {domain["id"]} — {domain["fields"].get("name", "Libellé à préciser")}', '', f'Statut : **{LABELS[domain["review"]["state"]]}**.', '', domain['fields'].get('definition','Définition à préciser.'), '', '| Repère | Capacité | Statut | Définition | Finalité | Rattachement |', '| --- | --- | --- | --- | --- | --- |']
        for relation in model['relations']:
            if relation['type'] != 'contains' or relation['source_id'] != domain['id']:
                continue
            n=nodes[relation['target_id']]; f=n['fields']
            lines.append('| '+ ' | '.join(cell(v) for v in [n['id'], f.get('name','Libellé à préciser'), LABELS[n['review']['state']],f.get('definition','À préciser'),f.get('finality','À préciser'),LABELS[relation['review']['state']]])+' |')
        lines += ['']
    if model['space']=='release':
        lines += ['## Portée des validations', '', '| Repère | Champs adoptés | Champs restant proposés | Décisions |', '| --- | --- | --- | --- |']
        for n in model['nodes']:
            lines.append('| '+ ' | '.join(cell(v) for v in [n['id'],', '.join(n.get('approved_fields',[])) or 'Aucun',', '.join(n.get('proposed_fields',[])) or 'Aucun',', '.join(n.get('adoption_ids',[])) or 'Aucune'])+' |')
        lines += ['', 'Les validations contextuelles et les réserves détaillées restent dans les décisions et les sources JSON.', '']
    return '\n'.join(lines)


def main():
    destination=ROOT/'restitutions'; destination.mkdir(exist_ok=True)
    pointer=read(ROOT/'modeles/release/current.json')
    release=read(ROOT/'modeles/release'/pointer['path'])
    backlog=read(ROOT/'modeles/backlog/model.json')
    for name,model,label in [('release',release,'Release'),('backlog',backlog,'Backlog')]:
        (destination/(name+'.md')).write_text(render(model,label),encoding='utf-8')
    index=read(ROOT/'modeles/panorama-as-is/current.json')
    lines=['# Panorama As Is', '', 'Restitution générée depuis les JSON. La consolidation ne prouve pas une observation récente du déploiement.', '', '| SI | Évaluation | Composants et mentions | Flux | Autorités d’information | Responsabilités de décision |', '| --- | --- | --- | --- | --- | --- |']
    for p in index['panoramas']:
        data=read(ROOT/p['path'])
        name=data.get('name') or data.get('canonical_name') or {'beaumanoir-historique-si':'Périmètre historique de Beaumanoir','boardriders-si':'Boardriders','sarenza-si':'Sarenza'}[data['model_id']]
        counts=[len(data[k]) for k in ['objects','flows','information_authorities','decision_responsibilities']]
        lines.append('| '+' | '.join(map(str,[name,'Non traité' if data['assessment_status']=='not_assessed' else 'Partiellement documenté']+counts))+' |')
    lines += ['', 'Le contexte partagé, notamment C-Log, reste dans son fichier distinct. Les besoins et orientations non établis comme existant sont conservés dans le backlog.', '']
    (destination/'panorama-as-is.md').write_text('\n'.join(lines),encoding='utf-8')
    print('Generated: restitutions/release.md, backlog.md, panorama-as-is.md')


if __name__=='__main__':
    main()

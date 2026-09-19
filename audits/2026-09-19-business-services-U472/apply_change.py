"""Application ponctuelle du retrait U472, avec conservation des états précédents."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps

AUDIT = Path(__file__).resolve().parent
BEFORE = AUDIT / 'before'
BEFORE.mkdir(exist_ok=False)
paths = ['modeles/backlog/model.yaml', 'modeles/backlog/glossary.yaml', 'modeles/backlog/modeling-roadmap.yaml']
for rel in paths:
    path = ROOT / rel
    (BEFORE / path.name).write_bytes(path.read_bytes())
protected = {str(p.relative_to(ROOT)).replace('\\', '/'): sha256(p.read_bytes()).hexdigest()
             for folder in ['modeles/release', 'modeles/backlog/history', 'modeles/revisions', 'modeles/decisions']
             for p in (ROOT / folder).rglob('*') if p.is_file()}
(AUDIT / 'protected-files.yaml').write_text(dumps(protected), encoding='utf-8')

model = read(ROOT / paths[0])
old = deepcopy(model)
assert sum(n['id'] == 'universe-case' for n in model['nodes']) == 1
assert not any('universe-case' in [r['source_id'], r['target_id']] for r in model['relations'])
model['nodes'] = [n for n in model['nodes'] if n['id'] != 'universe-case']
tracking = next(n for n in model['nodes'] if n['id'] == 'BHV082')
previous = 'Le périmètre est celui des processus d’exécution Supply ; le pilotage global des processus Business Services reste distinct.'
assert previous in tracking['fields']['scope']
tracking['fields']['scope'] = tracking['fields']['scope'].replace(previous, 'Le périmètre est celui des processus d’exécution Supply ; le suivi de l’ensemble des processus de l’entreprise reste hors de cette responsabilité.')
tracking['source_refs'].append('U472')
tracking['review']['note'] += ' U472 retire la référence à l’univers Business Services dans le périmètre ; responsabilité, nom, définition et accords antérieurs inchangés.'

documents = next(p for p in model['principles'] if p['id'] == 'PRINCIPLE-SUPPLY-DOCUMENTS')
previous = 'Les parcours transverses de Business Services conservent leurs responsabilités et leurs interactions explicites, sans constituer une couche processus.'
assert previous in documents['statement']
documents['statement'] = documents['statement'].replace(previous, 'Les parcours transverses articulent les responsabilités des domaines par leurs interactions explicites, sans constituer une couche processus.')
documents['source_refs'].append('U472')
cases = next(p for p in model['principles'] if p['id'] == 'PRINCIPLE-CASE-SUPPLY-ORDERS')
previous = 'Business Services porte le traitement des demandes et problèmes des parties prenantes ; le Case en est un dossier de traitement.'
assert previous in cases['statement']
cases['statement'] = cases['statement'].replace(previous, 'Un Case est un dossier de traitement d’une demande ou d’un problème ; cette notion ne présume aucun univers de rattachement.')
cases['source_refs'].append('U472')
model['principles'].append({
    'id': 'PRINCIPLE-SUPPLY-FIRST',
    'statement': 'Le périmètre actuellement travaillé est Supply Chain Orchestration. Le commerce sera étudié après la Supply Chain ; aucun univers Commerce n’est créé par anticipation.',
    'source_refs': ['U472'],
})
model['limitations'] = [x.replace('Le détail métier de Business Services et des objets, documents, événements', 'Le détail métier des objets, documents, événements') for x in model['limitations']]
model['limitations'].append('U472 retire l’univers Business Services (universe-case) et son entrée de glossaire TER067. Identifiants non réutilisables ; états antérieurs et accords conservés dans audits/2026-09-19-business-services-U472/before/ et les publications historiques. Le commerce est différé après la Supply Chain.')
model['source_version'] += ' + U472 retrait de Business Services, commerce différé après la Supply Chain'
(ROOT / paths[0]).write_text(dumps(model), encoding='utf-8')

glossary = read(ROOT / paths[1])
assert sum(t['id'] == 'TER067' for t in glossary['terms']) == 1
glossary['terms'] = [t for t in glossary['terms'] if t['id'] != 'TER067']
case = next(t for t in glossary['terms'] if t['id'] == 'TER064')
for field in ['short_description', 'definition']:
    case[field] = 'Dossier de traitement d’une situation, d’une demande ou d’un problème.'
case['context'] = 'Notion de dossier de traitement, distincte d’un Order. Elle ne désigne ni un univers ni un niveau du modèle FLOW.'
case['source_refs'].append('U472')
case['review']['note'] += ' U472 retire le rattachement à Business Services ; la notion de dossier demeure, sans nouveau périmètre adopté.'
glossary['source_refs'].append('U472')
(ROOT / paths[1]).write_text(dumps(glossary), encoding='utf-8')

roadmap = read(ROOT / paths[2])
roadmap['as_of'] = '2026-09-19'
roadmap['source_refs'].append('U472')
extension = next(e for e in roadmap['extensions'] if e['id'] == 'EXT-HIGHER-LEVEL')
extension['note'] += ' U472 remplace le maintien de Business Services : universe-case est retiré sans réutilisation d’identifiant. Seul Supply Chain Orchestration demeure instancié comme univers ; commerce différé après la Supply Chain, sans remplacement automatique.'
roadmap['limitations'] = [x.replace('ses domaines seront travaillés plus tard.', 'ce maintien est remplacé par le retrait U472.') for x in roadmap['limitations']]
roadmap['limitations'].append('U472 : terminer le travail Supply Chain avant d’étudier le commerce. Les mentions de Business Services dans les annexes de décisions antérieures restent des preuves historiques, pas un périmètre courant à développer.')
(ROOT / paths[2]).write_text(dumps(roadmap), encoding='utf-8')

assert model['relations'] == old['relations']
assert model['information_catalog'] == old['information_catalog']
for node in model['nodes']:
    prior = next(n for n in old['nodes'] if n['id'] == node['id'])
    if node['id'] != 'BHV082': assert node == prior, node['id']
    else:
        assert node['lifecycle'] == prior['lifecycle']
        assert node['fields']['definition'] == prior['fields']['definition']
print('U472 applied: one empty universe and one glossary entry removed; Supply structure and relations preserved.')

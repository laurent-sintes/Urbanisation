"""Application ponctuelle U251 ; ne pas réexécuter."""
from pathlib import Path
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

OUT = Path(__file__).resolve().parent
HISTORY = ROOT / 'modeles/backlog/history/pre-U251.yaml'
assert not HISTORY.exists(), 'Application déjà effectuée.'
STAMP = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
DOC = 'connaissance/33-frontieres-ctp.md'

def write(path, value):
    (ROOT / path).write_text(dumps(value), encoding='utf-8', newline='\n')

def append(path, text):
    with (ROOT / path).open('ab') as stream:
        stream.write(('\n\n' + text.strip() + '\n').encode('utf-8'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

model = read(ROOT / 'modeles/backlog/model.yaml')
before = deepcopy(model)
HISTORY.write_bytes((ROOT / 'modeles/backlog/model.yaml').read_bytes())
for name in ['d03-review.yaml', 'glossary.yaml']:
    (OUT / ('before-' + name)).write_bytes((ROOT / 'modeles/backlog' / name).read_bytes())
protected = {p.relative_to(ROOT).as_posix(): sha(p)
             for folder in ['modeles/release', 'modeles/revisions', 'modeles/decisions', 'modeles/provenance']
             for p in (ROOT / folder).rglob('*')
             if p.is_file() and p != ROOT / 'modeles/provenance/source-records.json'}
protected['modeles/backlog/modeling-glossary.yaml'] = sha(ROOT / 'modeles/backlog/modeling-glossary.yaml')
(OUT / 'protected-before.json').write_text(json.dumps(protected, indent=2) + '\n', encoding='utf-8')

append('connaissance/01-contributions-utilisateur.md', '''## U251

**id**

U251

**date**

2026-09-16

**titre**

Resserrer CTP sur la faisabilité après adaptation et ses décisions spécialisées

**texte**

Go

**contexte et portée**

Accord suivant U250 : conserver CTP, adopter la définition présentée de faisabilité après adaptation et les frontières proposées avec priorité, échéancier, PTP, politiques de stock, décision de service et adaptation de l’exécution. CTP assemble une solution Supply cohérente en mobilisant les décisions spécialisées ; chaque résultat conserve son responsable d’arbitrage. Un achat/transfert pour satisfaire un Order ne dépend pas obligatoirement d’une décision D05 d’optimisation du stock. Appliquer au backlog ; exemples, qualification détaillée des nouvelles relations et reprise lexicale restent proposés. Cet accord ne porte pas sur l’ensemble des recommandations de l’audit U249 et ne demande ni publication, ni commit, ni push.
''')

node = next(n for n in model['nodes'] if n['id'] == 'D03.j')
definition = 'Déterminer les possibilités de satisfaction d’un Order nécessitant une adaptation des ressources ou des engagements, en mobilisant les décisions spécialisées et en explicitant les conditions de faisabilité et les impacts.'
node['revision'] += 1
node['fields']['definition'] = definition
node['fields']['scope'] = '''Établir les possibilités de satisfaction de l’Order lorsque la situation de référence ne suffit pas : ressources supplémentaires, autres dates ou adaptations d’engagements à examiner. Le résultat est une solution Supply candidate cohérente, avec quantités et dates réalisables sous conditions, adaptations nécessaires, impacts et points restant à autoriser. Les hypothèses de modification ne sont pas des politiques actives ni des engagements déjà modifiés.

Mobiliser [Order Prioritization](model:D03.m) pour les arbitrages entre Orders et [Execution Service Decision](model:D06.e) pour les services/exécutants compatibles. Si une évolution des politiques de stock est envisagée, mobiliser [Stock Allocation Decision](model:D05.d) ou [Coverage Target Decision](model:D05.a) selon le résultat concerné ; CTP peut identifier la nécessité de cette évolution sans décider seul des valeurs de politique. Une dérogation ponctuelle à une politique n’est pas attribuée automatiquement à CTP par cette frontière.

Les possibilités et impacts établis peuvent alimenter [Profitable-to-Promise (PTP)](model:D03.k), qui porte l’arbitrage économique, et [Delivery Schedule Decision](model:D03.l), qui retient l’échéancier parmi les possibilités réalisables. Identifier les dates possibles fait partie de la faisabilité ; choisir l’échéancier retenu conserve son responsable. Ces mobilisations n’imposent ni appel systématique à toutes les décisions, ni séquence universelle, ni hiérarchie de sous-capacités.

Exemple fictif : une commande demande 100 pièces vendredi, mais seules 60 sont admissibles dans la situation de référence. CTP examine sous quelles conditions obtenir les 40 manquantes : apport supplémentaire disponible à temps ou autre solution compatible. La disponibilité du service nécessaire est éclairée par D06 ; une variante qui dégraderait une autre commande respecte l’arbitrage de priorité. Les possibilités et conséquences alimentent, selon le cas, le choix économique et l’échéancier. Le résultat ne crée pas automatiquement un achat et ne modifie pas de lui-même une autre promesse ou une protection.

[Execution Adaptation Decision](model:D06.f) détermine les variations du plan d’exécution face aux aléas. Lorsqu’une variation affecte la satisfaction de l’Order, le réexamen de la promesse dans D03 peut mobiliser CTP. [Promise Revision](model:D03.c) établit les modifications autorisées de promesse ; les capacités de gestion concernées tiennent les Orders, protections, affectations et réservations. CTP ne reprend pas leur application transactionnelle.

Un apport ou un transfert envisagé pour honorer l’Order conserve cette finalité, distincte de [Replenishment Decision](model:D05.e) et [Stock Redistribution Decision](model:D05.c), qui recherchent un stock souhaitable ou mieux réparti. Leur opération commune ne crée pas une dépendance obligatoire de tout approvisionnement CTP à D05. Le partage éventuel de données ou de calculs n’impose pas de fusion. CTP reste une décision agrégée de faisabilité sous adaptation ; elle ne devient pas par cette composition une capacité Planning ni une seconde autorité sur les arbitrages spécialisés.'''
node['source_refs'] = list(dict.fromkeys(node['source_refs'] + ['U250', 'U251', 'CMP086']))
node['source_locator'] = {'path': DOC, 'anchor': 'ctp'}
node['review'] = {'state': 'partial', 'note': 'U251 adopte la nouvelle définition et les frontières présentées. Nom, finalité et nature inchangés, portées U154 conservées. Le périmètre détaillé et l’exemple ajoutés restent proposés ; les accords de frontière sont délimités dans d03-review.yaml.'}
node['lifecycle'].update({'recorded_at': STAMP, 'source_refs': ['U154', 'U251'],
    'value_sha256': {k: value_hash(node['fields'][k]) for k in ['definition', 'finality', 'name', 'nature']},
    'note': 'U251 : définition présentée adoptée. Nom, finalité et nature inchangés de U154 ; aucun transfert de validation au scope éditorial ajouté. Ancienne définition et portée conservées dans history/pre-U251.yaml.'})
for k in ['approved_fields', 'proposed_fields']:
    node.pop(k, None)

relations = [
('REL-CTP-ORDER-PRIORITIZATION', 'D03.j', 'D03.m', 'CTP a besoin des priorités retenues pour construire une solution respectant les arbitrages entre Orders.', 'Lorsque des Orders sont en concurrence ; CTP ne redéfinit pas lui-même leur priorité.'),
('REL-CTP-EXECUTION-SERVICE', 'D03.j', 'D06.e', 'CTP a besoin des possibilités de service compatibles déterminées par Execution Service Decision pour établir la faisabilité Supply.', 'Lorsque la réalisation des prestations conditionne la solution ; une confirmation préalable de promesse n’est pas imposée à l’étude.'),
('REL-CTP-STOCK-ALLOCATION', 'D03.j', 'D05.d', 'CTP mobilise Stock Allocation Decision pour déterminer les modifications de droits d’usage envisagées dans un scénario.', 'Si le scénario nécessite un changement de politique d’allocation ; une valeur candidate ne devient pas une protection active par sa seule production.'),
('REL-CTP-COVERAGE-TARGET', 'D03.j', 'D05.a', 'CTP mobilise Coverage Target Decision pour déterminer les évolutions de niveaux ou seuils de stock envisagées dans un scénario.', 'Si une évolution de ces politiques est nécessaire ; un apport pour un Order ne crée pas cette dépendance à lui seul.'),
('REL-PTP-CTP-SCENARIOS', 'D03.k', 'D03.j', 'PTP a besoin des possibilités de satisfaction après adaptation et de leurs impacts établis par CTP pour porter l’arbitrage économique applicable.', 'Lorsque des scénarios d’adaptation sont comparés ; PTP peut aussi examiner des possibilités issues d’autres décisions.'),
('REL-DELIVERY-SCHEDULE-CTP', 'D03.l', 'D03.j', 'Delivery Schedule Decision a besoin des possibilités de quantités et dates après adaptation établies par CTP pour retenir un échéancier réalisable.', 'Lorsque l’échéancier repose sur une adaptation ; ce lien n’impose pas de passer par CTP pour tout échéancier.')]
for rid, source, target, meaning, condition in relations:
    assert rid not in {r['id'] for r in model['relations']}
    model['relations'].append({'id': rid, 'revision': 1, 'type': 'relates-to', 'source_id': source, 'target_id': target,
        'source_refs': ['U250', 'U251'],
        'qualification': {'meaning': meaning, 'scope': 'Consommateur → fournisseur de résultat métier ; aucune hiérarchie ni séquence technique universelle.', 'conditions': [condition], 'effects': []},
        'review': {'state': 'proposed', 'note': 'Projection structurée des frontières adoptées U251 ; qualification détaillée proposée, pas de nouveau type de relation.'},
        'lifecycle': {'state': 'ai_proposed', 'recorded_at': STAMP, 'recorded_by': 'Codex', 'source_refs': ['U251'], 'validated_fields': [], 'value_sha256': {}, 'note': 'Relations rédigées après le Go ; aucune validation implicite de leur qualification détaillée.'}})

principle = next(p for p in model['principles'] if p['id'] == 'PRINCIPLE-TO-PROMISE')
principle['statement'] = 'D03 distingue ATP, CTP et PTP : ATP établit les possibilités dans la situation de référence ; CTP détermine la faisabilité après adaptation en mobilisant les décisions spécialisées ; PTP porte l’arbitrage économique des scénarios. Les priorités, l’échéancier, les politiques de stock et les services conservent leurs responsables d’arbitrage. Le CTP local reste plus large que les acceptions éditeur consultées, sans séquence universelle ni application automatique des adaptations.'
principle['source_refs'] += ['U251']
model['source_version'] += ' + U251 CTP faisabilité après adaptation et frontières des décisions spécialisées'
model['as_of'] = '2026-09-16'

review = read(ROOT / 'modeles/backlog/d03-review.yaml')
review['ctp_boundaries_U251'] = {
    'source_refs': ['U250', 'U251'], 'state': 'urbanist_validated', 'target_id': 'D03.j',
    'history_path': 'modeles/backlog/history/pre-U251.yaml',
    'adopted_definition': definition, 'definition_sha256': value_hash(definition),
    'unchanged_adopted_fields': {k: {'source_refs': ['U154'], 'value': node['fields'][k], 'sha256': value_hash(node['fields'][k])} for k in ['name', 'finality', 'nature']},
    'adopted_boundaries': [
        'Order Prioritization porte les arbitrages entre commandes ; CTP mobilise les priorités.',
        'CTP établit les possibilités réalisables après adaptation ; Delivery Schedule Decision retient la répartition quantité/date.',
        'CTP établit faisabilité et conséquences des variantes ; PTP porte leur arbitrage économique.',
        'CTP peut identifier un changement de protection ou seuil nécessaire ; les décisions spécialisées portent les politiques de stock.',
        'CTP mobilise D06 pour les possibilités de service compatibles avec le besoin Supply.',
        'D06 décide des variations du plan d’exécution ; CTP contribue au réexamen de satisfaction de l’Order si nécessaire.',
        'Les achats/transferts pour satisfaire un Order et les décisions D05 d’optimisation du stock gardent leurs finalités ; pas de dépendance obligatoire de tout apport CTP à D05.',
        'CTP conserve une maille agrégée de faisabilité sous adaptation ; chaque résultat spécialisé conserve son responsable d’arbitrage.'],
    'proposed_details': {'scope_sha256': value_hash(node['fields']['scope']), 'relation_ids': [r[0] for r in relations], 'glossary_term': 'TER045', 'note': 'Périmètre détaillé, exemple, qualification des relations et reprise lexicale proposés ; ne pas étendre le Go de définition à ces ajouts.'},
    'open_points': ['Contrats précis et autorités d’application des adaptations.', 'Responsabilité d’une éventuelle dérogation ponctuelle à une politique, distincte de sa redéfinition.', 'Simulation avant enregistrement d’un Order : conserver la question antérieure ouverte.'],
    'market_comparison': {'id': 'CMP086', 'state': 'proposed', 'basis': 'Actualisation de CMP081 et des sources de l’audit U249 ; aucune nouvelle équivalence ni nouvelle consultation éditeur revendiquée.'}}
write('modeles/backlog/d03-review.yaml', review)

glossary = read(ROOT / 'modeles/backlog/glossary.yaml')
term = next(t for t in glossary['terms'] if t['id'] == 'TER045')
term['definition'] = definition
term['short_description'] = 'Déterminer les possibilités de satisfaction d’un Order après adaptation, en mobilisant les décisions spécialisées.'
term['context'] = 'Sens FLOW : faisabilité Supply sous adaptation. Priorités, échéancier, arbitrage économique, politiques de stock et services gardent leurs décisions responsables.'
term['notes'] = 'Alignement documentaire sur D03.j après U251 ; la définition de capacité est adoptée, cette reprise lexicale et ses compléments restent proposés. CTP ne met pas en application les adaptations et ne devient pas une définition éditeur universelle. État antérieur conservé dans audits/2026-09-16-ctp-frontieres/before-glossary.yaml.'
term['source_refs'] += ['U250', 'U251']
term['source_locator'] = {'path': DOC, 'anchor': 'ctp'}
term['review'] = {'state': 'proposed', 'note': 'Reprise lexicale après U251 ; pas de validation supplémentaire du glossaire déduite de l’accord sur la capacité.'}
write('modeles/backlog/glossary.yaml', glossary)

for item in model['source_files']:
    if (ROOT / item['path']).is_file(): item['sha256'] = sha(ROOT / item['path'])
model['source_files'].append({'path': DOC, 'sha256': sha(ROOT / DOC)})
write('modeles/backlog/model.yaml', model)

assert [n for n in before['nodes'] if n['id'] != 'D03.j'] == [n for n in model['nodes'] if n['id'] != 'D03.j']
assert model['relations'][:len(before['relations'])] == before['relations']
assert all(sha(ROOT / p) == value for p, value in protected.items())
(OUT / 'verification.json').write_text(json.dumps({'changed_nodes': ['D03.j'], 'added_relations': [r[0] for r in relations], 'changed_glossary_terms': ['TER045'], 'protected_files': len(protected), 'protected_unchanged': True}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('U251 appliqué : CTP, principe, TER045 ; six relations proposées ; autres capacités et publications inchangées.')

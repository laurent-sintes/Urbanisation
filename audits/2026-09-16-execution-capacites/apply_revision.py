"""Application ponctuelle U247, avec capture exacte et contrôles de portée."""
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

AUDIT = Path(__file__).resolve().parent
DOC = 'connaissance/32-execution-orchestration.md'
HISTORY = ROOT / 'modeles/backlog/history/pre-U247.yaml'
MODEL = ROOT / 'modeles/backlog/model.yaml'
STAMP = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
assert not HISTORY.exists(), 'Ne pas réexécuter cette application.'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def append(path, text):
    with (ROOT / path).open('ab') as stream:
        stream.write(('\n\n' + text.strip() + '\n').encode('utf-8'))

def write(path, data):
    (ROOT / path).write_text(dumps(data), encoding='utf-8', newline='\n')

before = read(MODEL)
HISTORY.write_bytes(MODEL.read_bytes())
(AUDIT / 'before-description.md').write_bytes((ROOT / DOC).read_bytes())
(AUDIT / 'before-review.yaml').write_bytes((ROOT / 'modeles/backlog/execution-services-review.yaml').read_bytes())
protected_files = [p for folder in ['modeles/release', 'modeles/revisions', 'modeles/decisions', 'modeles/provenance']
                   for p in (ROOT / folder).rglob('*') if p.is_file() and p != ROOT / 'modeles/provenance/source-records.json']
protected_files += [ROOT / 'modeles/backlog/glossary.yaml', ROOT / 'modeles/backlog/modeling-glossary.yaml']
protected = {p.relative_to(ROOT).as_posix(): sha(p) for p in protected_files}
(AUDIT / 'protected-before.json').write_text(json.dumps(protected, indent=2), encoding='utf-8')

append('connaissance/01-contributions-utilisateur.md', '''## U247

**id**

U247

**date**

2026-09-16

**titre**

Appliquer Service Order Management et le catalogue d'exécution révisé

**texte**

Go

**contexte et portée**

Accord suivant la proposition U246 de Service Order Management et le tableau séparant décision des prestations, gestion des demandes, orchestration, tracking et adaptation. Appliquer cette clarification avec Execution Capacity Visibility retenu U246 et la séparation demandée U245. Le nom et la définition présentée de Service Order Management sont adoptés ; les noms et responsabilités courtes du dernier tableau sont transcrits dans leur portée, sans étendre l'accord aux descriptions détaillées ajoutées. La fusion qualification/options en Execution Service Decision, présentée en U245 mais non reprise dans le dernier tableau, est appliquée comme proposition du catalogue en discussion ; elle ne reçoit pas de validation métier implicite. Aucune publication, aucun commit ni push demandé.
''')

model = deepcopy(before)
nodes = {n['id']: n for n in model['nodes']}
review = read(ROOT / 'modeles/backlog/execution-services-review.yaml')
prior_agreements = {k: deepcopy(v) for k,v in review.items() if k.startswith('user_agreements_')}

def cycle(values, approved=(), refs=None):
    return {'state': 'urbanist_validated' if approved else 'ai_proposed', 'recorded_at': STAMP,
            'recorded_by': 'Codex', 'source_refs': refs or ['U245', 'U246', 'U247'],
            'validated_fields': list(approved), 'value_sha256': {k: value_hash(values[k]) for k in approved},
            'note': 'U247 : portée limitée au dernier tableau et à la définition présentée de Service Order Management ; nom Capacity Visibility selon U246. Compléments détaillés proposés.'}

def update(identifier, fields, approved=(), refs=None, new=False):
    if new:
        assert identifier not in nodes
        node = {'id': identifier, 'revision': 1, 'kind': 'capability', 'layer': 'transactional', 'source_refs': [], 'adoption_ids': []}
        nodes[identifier] = node
        model['nodes'].append(node)
    else:
        node = nodes[identifier]
        assert not node['lifecycle']['validated_fields'] and not node.get('adoption_ids'), identifier
        node['revision'] += 1
    node['fields'] = fields
    node['source_refs'] = list(dict.fromkeys(node['source_refs'] + ['U245', 'U246', 'U247', 'CMP079']))
    node['source_locator'] = {'path': DOC, 'anchor': identifier.lower().replace('.', '-')}
    node['review'] = {'state': 'partial' if approved else 'proposed',
                      'note': 'Noms et responsabilités courtes adoptés uniquement dans la portée lifecycle ; finalités, natures et périmètres détaillés proposés. La fusion qualification/options reste proposée.'}
    node['lifecycle'] = cycle(fields, approved, refs)
    node['editorial_basis'] = 'Application du challenge U245/U246 selon U247 ; contexte et détails concrets rédigés par Codex, sans transfert de validation depuis les identifiants retirés.'
    for key in ['approved_fields', 'proposed_fields']:
        node.pop(key, None)

update('D07.a', {
    'name': 'Execution Requirements Decision',
    'definition': 'Déterminer les prestations nécessaires.',
    'finality': 'Déterminer les résultats de prestation nécessaires à la réalisation du besoin Supply.',
    'nature': 'decision',
    'scope': 'Déterminer, à partir du besoin Supply et de ses contraintes, les prestations et résultats requis : préparation, réception, transport ou production de documents. Préciser biens ou documents concernés, quantités, destinataires, lieux et échéances utiles.\n\nExemple : réaliser la livraison requiert une préparation, un document et un transport. La décision explicite ces besoins ; Service Order Management tient ensuite les demandes adressées aux exécutants et leurs évolutions. La décision de service choisit les moyens de service pour y répondre.\n\nLa capacité ne se limite plus à formuler un message ou à exprimer un Service Order. Elle ne recrée ni l’autorisation de la commande D04, ni sa promesse D03, ni un Agreement ou un Case. D07.a conserve son identité pour la responsabilité de détermination des prestations, précisée par U245/U247.'
}, ['name', 'definition'], ['U247'])
update('D06.b', {
    'name': 'Execution Capacity Visibility',
    'definition': 'Rendre visible la capacité opérationnelle communiquée par les exécutants, avec son contexte, sa période et sa fraîcheur, pour alimenter les décisions Supply.',
    'finality': 'Donner à D03 et aux décisions d’exécution une connaissance exploitable des capacités annoncées par les exécutants.',
    'nature': 'knowledge',
    'scope': 'Rendre accessible la capacité logistique dans son contexte, par exemple le nombre maximal de préparations communiqué pour un site et un créneau. Expliciter le service, l’unité, la période, l’origine et la fraîcheur des informations disponibles.\n\nExemple : l’entrepôt annonce un plafond de 1 000 préparations sur un créneau ; si une charge ou un disponible sont également communiqués, les présenter avec leur sens et leur date de connaissance. Ne pas transformer sans règle connue ce plafond en capacité encore disponible.\n\nCette visibilité ne décide pas d’augmenter les ressources de l’exécutant, ne calcule pas implicitement un disponible à partir d’une formule non convenue et ne réserve pas la capacité. D03 l’utilise pour sa promesse Supply ; Service Decision et Adaptation Decision peuvent la mobiliser. Le nom est adopté U246 ; les détails de représentation et contrats restent proposés.'
}, ['name'], ['U246'])
update('D07.b', {
    'name': 'Service Order Management',
    'definition': 'Gérer les demandes de prestation adressées aux exécutants et leur cycle de vie : émission, acceptation ou refus, modification, annulation et clôture, selon le service.',
    'finality': 'Tenir les demandes de prestation, leur prise en charge et leurs évolutions de façon explicite et traçable.',
    'nature': 'management',
    'scope': 'Tenir ce qui est demandé à un exécutant, ce qu’il accepte de réaliser et les évolutions de cette prise en charge. L’émission d’une demande, son acceptation et sa réalisation restent distinctes. Les opérations possibles dépendent du service et de son état ; aucun cycle universel ni acceptation systématiquement différée n’est imposé.\n\nExemple : demander à l’entrepôt de préparer 100 colis avant 16 h ; enregistrer l’acceptation, le refus ou une autre échéance proposée ; tenir ensuite une demande de modification ou d’annulation et la réponse correspondante. Le tracking renseigne en parallèle la préparation commencée, les 60 colis prêts ou le retard annoncé.\n\nRequirements Decision détermine les prestations nécessaires ; Orchestration coordonne les prestations et leurs dépendances ; Adaptation Decision détermine la variation du plan. Cette gestion met à jour transactionnellement les demandes et leurs états, unitairement ou en groupe selon les interfaces disponibles ; ces modalités ne créent pas de capacités supplémentaires.\n\nConserver la distinction entre SLA configuré, engagement individuel, estimation et résultat. Les exécutants gardent leurs opérations internes et D03 la promesse Supply. D07.b conserve la gestion des prises en charge et engagements, désormais explicitée dans le cycle du Service Order.'
}, ['name', 'definition'], ['U247'])
update('D06.d', {
    'name': 'Execution Orchestration',
    'definition': 'Coordonner les prestations et leurs dépendances.',
    'finality': 'Coordonner la réalisation du plan retenu entre les exécutants.',
    'nature': 'orchestration',
    'scope': 'Coordonner le déclenchement et l’enchaînement des prestations du plan retenu, en tenant compte de leurs dépendances, des prises en charge et des faits d’exécution. Mobiliser Service Order Management pour tenir les demandes et leurs évolutions.\n\nExemple : coordonner la préparation, la disponibilité du document et la collecte. Si la décision d’adaptation retient un autre transporteur, coordonner la modification des prestations concernées et leur nouvel enchaînement.\n\nLa détermination de la variation du plan appartient à Execution Adaptation Decision. L’orchestration peut lui transmettre un aléa, mais ne porte plus cette décision dans sa propre définition. Les exécutants conservent l’organisation de leurs opérations internes. Aucun moteur de workflow, contrôle humain systématique ou rollback physique universel n’est présumé.'
}, ['name', 'definition'], ['U247'])
tracking = deepcopy(nodes['D07.d']['fields'])
tracking['scope'] = tracking['scope'].replace('Le tracking alimente l’orchestration et le réexamen de promesse lorsque nécessaire.', 'Le tracking alimente l’orchestration pour la coordination des prestations et Adaptation Decision pour la recherche d’une variation du plan ; D03 conserve le réexamen de la promesse lorsque nécessaire.')
update('D07.d', tracking, ['name'], ['U247'])
update('D06.e', {
    'name': 'Execution Service Decision',
    'definition': 'Déterminer les services et exécutants à mobiliser pour les prestations nécessaires, en tenant compte de leur admissibilité et des contraintes.',
    'finality': 'Retenir des services utilisables pour réaliser les prestations requises dans le cadre Supply applicable.',
    'nature': 'decision',
    'scope': 'Regrouper les responsabilités d’admissibilité et de comparaison d’options auparavant portées par D06.a et D06.c. Exploiter le catalogue des services, les lieux et relations du réseau, les conditions applicables et la visibilité sur la capacité. Déterminer les services utilisables, puis les moyens à mobiliser.\n\nExemple : identifier les transporteurs desservant une destination, compatibles avec les marchandises et les horaires, puis déterminer le service à solliciter. La qualification désignait ce contrôle d’admissibilité ; elle n’est plus une capacité distincte dans cette proposition.\n\nLa décision reste dans le besoin Supply et les contraintes portés par D03. Elle ne reprend pas la décision de couverture de l’Order ou la révision de sa promesse. Elle peut être mobilisée pour le plan initial ou par Adaptation Decision. Le regroupement et cette formulation sont appliqués comme proposition ; aucune validation antérieure de D06.a/c n’est transférée.'
}, new=True)
update('D06.f', {
    'name': 'Execution Adaptation Decision',
    'definition': 'Déterminer les variations du plan.',
    'finality': 'Retenir une variation de réalisation adaptée à l’aléa et aux contraintes Supply.',
    'nature': 'decision',
    'scope': 'Déterminer la variation à retenir lorsqu’un fait, un retard ou un échec remet en cause le plan d’exécution. Mobiliser les décisions de service, les capacités communiquées et les informations sur les demandes et réalisations.\n\nExemple : un SLA était compatible avec la collecte, mais une panne retarde la préparation. Déterminer une autre collecte, un autre transporteur ou une réalisation partielle selon les possibilités ; Orchestration coordonne ensuite les prestations du plan retenu.\n\nSi la variation remet la promesse Supply en cause, fournir à D03 les faits et variantes utiles à son réexamen. Cette capacité ne décide pas seule d’une nouvelle promesse. La latitude d’adaptation relève des règles de fonctionnement et ne conditionne pas le catalogue.\n\nDecision détermine une réponse métier ; Planning conserve le sens reconfigurer, simuler et valider en mobilisant des décisions. La séparation demandée n’ajoute pas automatiquement une capacité Planning ou un contrôle humain obligatoire.'
}, ['name', 'definition'], ['U247'], new=True)

retired_nodes = ['D06.a', 'D06.c']
retired_relations = ['REL-MEMBER-D06.a', 'REL-MEMBER-D06.c', 'REL-EXECUTION-ORCHESTRATION-OPTIONS', 'REL-EXECUTION-ORCHESTRATION-PROMISE-REVISION']
model['nodes'] = [n for n in model['nodes'] if n['id'] not in retired_nodes]
model['relations'] = [r for r in model['relations'] if r['id'] not in retired_relations]
relations = {r['id']: r for r in model['relations']}

def new_relation(identifier, kind, source, target, meaning=None, approved=False):
    assert identifier not in relations
    r = {'id': identifier, 'revision': 1, 'type': kind, 'source_id': source, 'target_id': target,
         'source_refs': ['U245', 'U246', 'U247'],
         'review': {'state': 'accepted' if approved else 'proposed', 'note': 'Rattachement de l’adaptation séparée demandé U245/U247.' if approved else 'Projection explicite des responsabilités ; qualification détaillée proposée.'}}
    if meaning:
        r['qualification'] = {'meaning': meaning, 'scope': 'Relation métier sans hiérarchie entre capacités ni séquence technique universelle.', 'conditions': [], 'effects': []}
    r['lifecycle'] = cycle(r, ['type','source_id','target_id'] if approved else ())
    model['relations'].append(r)
    relations[identifier] = r

def revise_relation(identifier, meaning):
    r = relations[identifier]
    assert not r['lifecycle']['validated_fields']
    r['revision'] += 1
    r['qualification']['meaning'] = meaning
    r['source_refs'] = list(dict.fromkeys(r['source_refs'] + ['U247']))
    r['lifecycle'] = cycle(r)
    r['review'] = {'state': 'proposed', 'note': 'Qualification actualisée pour la séparation orchestration/adaptation U247 ; pas de validation détaillée.'}

new_relation('REL-MEMBER-D06.e', 'contains', 'D06', 'D06.e')
new_relation('REL-MEMBER-D06.f', 'contains', 'D06', 'D06.f', approved=True)
revise_relation('REL-EXECUTION-TRACKING-ORCHESTRATION', 'Le tracking fournit faits, jalons et estimations utiles à la coordination des prestations par Orchestration. La décision de variation relève séparément d’Adaptation Decision.')
revise_relation('REL-EXECUTION-ORCHESTRATION-COMMITMENTS', 'L’orchestration mobilise Service Order Management pour tenir les demandes de prestation et leurs évolutions selon le plan retenu ; le choix d’une variation relève d’Adaptation Decision.')
new_relation('REL-EXECUTION-TRACKING-ADAPTATION', 'relates-to', 'D07.d', 'D06.f', 'Les faits, jalons et estimations signalent les aléas à prendre en compte pour déterminer une variation du plan.')
new_relation('REL-EXECUTION-ADAPTATION-SERVICE', 'relates-to', 'D06.f', 'D06.e', 'Adaptation Decision mobilise Service Decision pour déterminer des services utilisables dans la variation envisagée.')
new_relation('REL-EXECUTION-ADAPTATION-CAPACITY', 'relates-to', 'D06.f', 'D06.b', 'La décision d’adaptation utilise la capacité communiquée et son contexte ; Visibility ne décide ni du plan ni des ressources à engager.')
new_relation('REL-EXECUTION-ADAPTATION-ORCHESTRATION', 'relates-to', 'D06.f', 'D06.d', 'La variation retenue fournit le plan à coordonner par Orchestration ; décider l’adaptation et coordonner sa réalisation sont des responsabilités distinctes.')
new_relation('REL-EXECUTION-ADAPTATION-PROMISE-REVISION', 'relates-to', 'D06.f', 'D03.c', 'Si une variation remet la promesse Supply en cause, Adaptation Decision fournit les faits et variantes à D03 pour son réexamen ; elle ne révise pas elle-même la promesse.')
new_relation('REL-EXECUTION-SERVICE-CAPACITY', 'relates-to', 'D06.e', 'D06.b', 'La décision de service mobilise la capacité communiquée pour apprécier les moyens utilisables dans le contexte.')
new_relation('REL-EXECUTION-REQUIREMENTS-SERVICE-ORDER', 'relates-to', 'D07.a', 'D07.b', 'Les prestations nécessaires déterminées alimentent les demandes tenues par Service Order Management, sans présumer une cardinalité ou une émission automatique.')

model['source_version'] += ' + U247 Service Order Management, Capacity Visibility, décisions et séparation orchestration/adaptation'
model['limitations'].append('U247 applique le catalogue révisé : D06.a/c retirées et regroupées dans D06.e Execution Service Decision, fusion toujours proposée ; D06.f Execution Adaptation Decision séparée de D06.d Orchestration. D06.b devient Capacity Visibility et D07.b Service Order Management. États antérieurs dans history/pre-U247.yaml. Portées adoptées limitées aux noms et responsabilités présentés ; descriptions détaillées et qualifications de relations proposées. Aucun identifiant retiré réutilisé, aucune publication implicite.')
model['principles'].append({'id': 'PRINCIPLE-EXECUTION-DECISION-AND-COORDINATION',
    'statement': 'La visibilité sur la capacité rend accessibles les informations communiquées par les exécutants. La décision de besoins détermine les prestations nécessaires ; Service Order Management tient les demandes et leur cycle. Orchestration coordonne les prestations et leurs dépendances ; Adaptation Decision détermine les variations du plan. D03 conserve la promesse Supply et les exécutants leurs opérations internes.', 'source_refs': ['U245','U246','U247']})

order = ['D07.a','D06.e','D06.b','D07.b','D06.d','D07.d','D07.c','D06.f']
lines = ['# Pilotage et orchestration de l’exécution — U247', '',
    'Catalogue courant du backlog après U247, le 16 septembre 2026. Autorité : `modeles/backlog/model.yaml`. D06 regroupe huit capacités ; D05, D03 et les références restent inchangés. La release et Atlas conservent leur publication.', '',
    'Service Order Management remplace le nom abstrait Execution Commitment Management. Capacity Visibility est retenu U246. Les noms et responsabilités courtes du dernier tableau sont repris dans leur portée ; la fusion qualification/options en Execution Service Decision reste proposée. Les descriptions détaillées et exemples sont des compléments proposés.', '',
    '| Identifiant | Capacité | Responsabilité |', '| --- | --- | --- |']
lines += [f"| {i} | {nodes[i]['fields']['name']} | {nodes[i]['fields']['definition']} |" for i in order]
for i in ['D06'] + order + ['D14','D14.a']:
    f=nodes[i]['fields']
    lines += ['', f'<a id="{i.lower().replace(".","-")}"></a>', f'## {i} — {f["name"]}', '', f['definition'], '', f['scope']]
lines += ['', '## Continuité, vocabulaire et sources', '',
    'D06.a/c et leurs rattachements sont conservés dans history/pre-U247.yaml ; la décision de service reçoit une nouvelle identité D06.e. L’adaptation reçoit D06.f ; D06.d garde la coordination. Les capacités D07.a–d gardent leurs identités et leur rattachement explicite à D06. Les cinq liens de rapprochement D07.c vers D04.i–m sont inchangés.', '',
    'Les deux glossaires sont inchangés. Decision détermine une réponse métier ; Visibility restitue une connaissance ; Management tient les demandes et leurs évolutions. Planning reste reconfigurer, simuler et valider en mobilisant des décisions. La latitude d’adaptation n’impacte pas le catalogue.', '',
    'CMP079 actualise les correspondances depuis les études U239/U241 et CMP078, sans nouvelle consultation de source éditeur. Les granularités et frontières locales ne sont pas des équivalences de marché.', '',
    'État documentaire U244 conservé dans audits/2026-09-16-execution-capacites/before-description.md ; accords et application détaillés dans execution-services-review.yaml.', '']
(ROOT / DOC).write_text('\n'.join(lines), encoding='utf-8', newline='\n')

append('marche/comparaisons.md', '''### CMP079

- État comparé : catalogue D06 après U247, en remplacement de la maille U244 pour les responsabilités modifiées. Date : 2026-09-16 ; auteur Codex ; statut proposé, aucune validation d'équivalence.
- Sources existantes : études U239/U241 et ELM129–134 / ELM136–137, consultées le 16 septembre 2026 ; aucune nouvelle consultation éditeur dans cette application.
- D07.b Service Order Management : appuis fonctionnels partiels ELM131 et ELM133 aux demandes de service, réponses et évolutions ; pas de cycle universel ni équivalence à un domaine logiciel.
- D06.b Capacity Visibility : recouvrement limité aux informations de capacité utiles à la promesse ; les calculs CTP/PP/DS des ELM136/137 ne sont pas assimilés à cette visibilité. Responsabilité de calcul du disponible non attribuée par ce nom.
- D06.e Service Decision : proposition regroupant qualification et options ; appui partiel ELM130 à l'admissibilité, équivalence du choix de service non établie. D07.a Requirements Decision : définition du besoin, équivalence détaillée non établie.
- D06.d Orchestration : appui ELM132 aux dépendances. D06.f Adaptation Decision : séparation locale demandée U245/U247, aucune capacité native équivalente démontrée. D07.d tracking et D07.c rapprochement conservent les limites CMP078.
- La promesse Supply reste D03 ; les exécutants gardent leurs opérations internes. Description et limites : connaissance/32-execution-orchestration.md et execution-services-review.yaml, application_U247.
''')
append('marche/execution-services-revised-comparison.md', '''## Révision U247 — décisions, visibilité et gestion des Service Orders

Le catalogue appliqué distingue désormais Service Order Management, Capacity Visibility, Orchestration et Adaptation Decision. Qualification et options sont regroupées dans une proposition de Service Decision. CMP079 actualise la comparaison à cette maille ; les fonctions de calcul des éditeurs ne deviennent pas des preuves de responsabilité de calcul dans Capacity Visibility. Les anciennes descriptions U244 restent historiques.
''')
review['state']='applied_to_backlog_U247'
review['source_refs'].append('U247')
review['review_U245']['state']='applied_U247_with_scoped_approvals'
review['review_U245']['model_mutation']=True
review['review_U245']['application_note']='Application U247 détaillée séparément ; ancien catalogue conservé dans history/pre-U247.yaml.'
review['review_U246']['state']='applied_U247_service_order_management_adopted'
review['review_U246']['model_mutation']=True
review['application_U247']={
    'source_refs':['U245','U246','U247'], 'before_snapshot':HISTORY.relative_to(ROOT).as_posix(), 'before_sha256':sha(HISTORY),
    'capability_ids':order,'new_ids':['D06.e','D06.f'],'retired_node_ids':retired_nodes,'retired_relation_ids':retired_relations,
    'identity_notes':'D06.e regroupe deux responsabilités, sans réutilisation de leurs identifiants ; D06.f sépare la décision de variation de la coordination D06.d. D07.b conserve la tenue des prises en charge, précisée en gestion du Service Order.',
    'adopted_fields':{i:{'fields':nodes[i]['lifecycle']['validated_fields'],'value_sha256':nodes[i]['lifecycle']['value_sha256'],'source_refs':nodes[i]['lifecycle']['source_refs']} for i in order if i!='D07.c'},
    'proposed_details':['Fusion qualification/options et formulation de Service Decision','Définition détaillée de Capacity Visibility','Finalités, natures, périmètres et exemples','Qualifications des relations'],
    'market_comparison':'CMP079','publication':'Aucune nouvelle publication ; aucun commit ni push.'
}
review['publication']='Catalogue révisé appliqué au backlog U247 ; publication courante et Atlas inchangés.'
write('modeles/backlog/execution-services-review.yaml', review)
assert all(read(ROOT / 'modeles/backlog/execution-services-review.yaml')[k]==v for k,v in prior_agreements.items())

p=ROOT/'AGENTS.md'
data=p.read_bytes()
start=data.index('U245 rouvre le catalogue des capacités :'.encode('utf-8'))
end=data.index('U244 applique la refonte :'.encode('utf-8'),start)
replacement='U247 applique le catalogue révisé après U245/U246 : **Execution Capacity Visibility**, **Service Order Management**, **Execution Requirements Decision**, **Execution Orchestration**, **Execution Tracking**, **Execution Reconciliation** et **Execution Adaptation Decision** sont distinctes ; **Execution Service Decision** regroupe qualification et options comme proposition. Huit capacités directement rattachées à D06. D06.a/c sont retirées au profit de D06.e ; D06.f porte l’adaptation séparée de D06.d. Les noms et responsabilités courtes adoptés restent limités aux portées enregistrées ; les détails ajoutés et la fusion de services restent proposés. État antérieur : `history/pre-U247.yaml`. U244 avait appliqué la refonte :'.encode('utf-8')
data=data[:start]+replacement+data[end+len('U244 applique la refonte :'.encode('utf-8')):]
data=data.replace('**Pilotage de l\'exécution — U237 à U246 :**'.encode('utf-8'),'**Pilotage de l\'exécution — U237 à U247 :**'.encode('utf-8'))
p.write_bytes(data)
append('JOURNAL.md', '''## 2026-09-16 — U247 : catalogue d'exécution révisé appliqué

Service Order Management adopté avec sa définition présentée ; Capacity Visibility retenu selon U246. Orchestration et Adaptation Decision séparées. Requirements Decision détermine les prestations nécessaires ; tracking et rapprochement conservés. D06.e regroupe qualification/options comme proposition ; D06.a/c archivées, D06.f nouvel identifiant d'adaptation. Huit capacités directement rattachées à D06, liens actualisés et D03/D05 préservés. Portées dans application_U247 ; descriptions détaillées proposées. Deux glossaires et publications inchangés. Contrôles et captures dans audits/2026-09-16-execution-capacites. Aucun commit, push ni publication.
''')
for entry in model['source_files']:
    entry['sha256']=sha(ROOT / entry['path'])
write('modeles/backlog/model.yaml', model)

after_nodes={n['id']:n for n in model['nodes']}
changed_nodes={'D06.a','D06.b','D06.c','D06.d','D07.a','D07.b','D07.d'}
changed_relations=set(retired_relations)|{'REL-EXECUTION-TRACKING-ORCHESTRATION','REL-EXECUTION-ORCHESTRATION-COMMITMENTS'}
checks={
    'untouched_nodes_preserved':all(after_nodes[n['id']]==n for n in before['nodes'] if n['id'] not in changed_nodes),
    'untouched_relations_preserved':all(relations[r['id']]==r for r in before['relations'] if r['id'] not in changed_relations),
    'eight_direct_capabilities':{r['target_id'] for r in model['relations'] if r['type']=='contains' and r['source_id']=='D06'}==set(order),
    'retired_ids_absent':not any(i in after_nodes for i in retired_nodes),
    'no_retired_relation_endpoints':not any(r['source_id'] in retired_nodes or r['target_id'] in retired_nodes for r in model['relations']),
    'protected_files_unchanged':all(sha(ROOT/p)==h for p,h in protected.items()),
    'adaptation_to_d03':relations['REL-EXECUTION-ADAPTATION-PROMISE-REVISION']['target_id']=='D03.c',
    'model_source_hashes_valid':all(sha(ROOT/f['path'])==f['sha256'] for f in model['source_files'])
}
assert all(checks.values()),checks
result={'checks':checks,'protected_files':len(protected),'nodes':len(model['nodes']),'capabilities':sum(n['kind']=='capability' for n in model['nodes']),'relations':len(model['relations'])}
(AUDIT/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))

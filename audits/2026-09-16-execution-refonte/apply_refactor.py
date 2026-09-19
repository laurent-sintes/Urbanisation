"""Application ponctuelle U244 ; refuse de réécrire la capture avant refonte."""
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
MODEL = ROOT / 'modeles/backlog/model.yaml'
HISTORY = ROOT / 'modeles/backlog/history/pre-U244.yaml'
DOC = 'connaissance/32-execution-orchestration.md'
STAMP = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
REFS = ['U237', 'U238', 'U240', 'U242', 'U243', 'U244']
assert not HISTORY.exists(), 'Capture existante : ne pas réexécuter.'

def write(path, value):
    (ROOT / path).write_text(dumps(value), encoding='utf-8', newline='\n')

def append(path, text):
    with (ROOT / path).open('ab') as stream:
        stream.write(('\n\n' + text.strip() + '\n').encode('utf-8'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

before = read(MODEL)
HISTORY.write_bytes(MODEL.read_bytes())
(AUDIT / 'before-glossary.yaml').write_bytes((ROOT / 'modeles/backlog/glossary.yaml').read_bytes())
protected_paths = [p for folder in ['modeles/release', 'modeles/revisions', 'modeles/decisions', 'modeles/provenance']
                   for p in (ROOT / folder).rglob('*') if p.is_file() and p != ROOT / 'modeles/provenance/source-records.json']
protected_paths.append(ROOT / 'modeles/backlog/modeling-glossary.yaml')
protected = {p.relative_to(ROOT).as_posix(): sha(p) for p in protected_paths}
(AUDIT / 'protected-before.json').write_text(json.dumps(protected, indent=2), encoding='utf-8')
append('connaissance/01-contributions-utilisateur.md', '''## U244

**id**

U244

**date**

2026-09-16

**titre**

Appliquer le référentiel des services et la refonte du pilotage de l'exécution

**texte**

On peut mettre à jour le modèle ?

**contexte et portée**

Demande d'application dans le backlog des principes U237–U243 : nouveau référentiel, regroupement D06/D07 avec D05 conservé, capacité contextuelle alimentant D03, orchestration, tracking et adaptation. La définition de domaine présentée après U242 est retenue pour cette application. La latitude d'adaptation ne conditionne pas le catalogue. Les noms anglais non explicitement adoptés et le détail des capacités, descriptions et relations conçus pendant cette application restent proposés. Aucune publication, aucun commit ni push demandé.
''')

model = deepcopy(before)
nodes = {n['id']: n for n in model['nodes']}
relations = {r['id']: r for r in model['relations']}

def lifecycle(fields, adopted=(), state='ai_proposed', refs=None, note='Compléments proposés pour appliquer U244 ; aucune validation de détail déduite.'):
    return {'state': 'urbanist_validated' if adopted else state, 'recorded_at': STAMP,
            'recorded_by': 'Codex', 'source_refs': refs or REFS,
            'validated_fields': list(adopted), 'value_sha256': {k: value_hash(fields[k]) for k in adopted}, 'note': note}

def edit_node(identifier, fields, adopted=(), refs=None):
    n = nodes[identifier]
    assert not n.get('adoption_ids') and not n['lifecycle']['validated_fields'], identifier
    n['revision'] += 1
    n['fields'] = fields
    n['source_refs'] = list(dict.fromkeys(n['source_refs'] + REFS + ['CMP078']))
    n['source_locator'] = {'path': DOC, 'anchor': identifier.lower().replace('.', '-')}
    n['review'] = {'state': 'partial' if adopted else 'proposed', 'note': 'Principes U240/U242/U243 appliqués en U244. Seuls les champs explicitement listés dans lifecycle sont adoptés ; noms et compléments non listés restent proposés.'}
    n['lifecycle'] = lifecycle(fields, adopted, refs=refs)
    n['adoption_ids'] = []
    for key in ['approved_fields', 'proposed_fields']:
        n.pop(key, None)
    return n

def new_node(identifier, kind, fields, adopted=(), refs=None):
    assert identifier not in nodes
    n = {'id': identifier, 'revision': 1, 'kind': kind, 'layer': 'transactional', 'fields': fields,
         'source_refs': REFS + ['CMP078'], 'source_locator': {'path': DOC, 'anchor': identifier.lower().replace('.', '-')},
         'review': {'state': 'partial' if adopted else 'proposed', 'note': 'Création pour U244 ; définition adoptée uniquement si indiquée dans lifecycle. Nom, granularité et détails non listés proposés.'},
         'adoption_ids': [], 'lifecycle': lifecycle(fields, adopted, refs=refs)}
    nodes[identifier] = n
    model['nodes'].append(n)
    return n

edit_node('D06', {
    'name': 'Execution Management',
    'definition': 'Orchestrer l’exécution Supply en coordonnant les prestations, en suivant leur réalisation et en adaptant le plan aux aléas, en articulation avec la promesse Supply.',
    'finality': 'Maintenir une exécution cohérente et adaptable, depuis les possibilités de réalisation jusqu’aux résultats constatés.',
    'scope': 'Connaître les services admissibles et la capacité logistique contextualisée ; exprimer les prestations, gérer leurs engagements, coordonner leurs dépendances, suivre leur avancement et adapter le plan aux aléas. Les services couvrent entrepôt, transport et prestations telles que la production de documents.\n\nUn SLA configuré compatible ne garantit pas la réussite opérationnelle. Exemple : la préparation prend du retard et menace la collecte ; rechercher une autre collecte, un autre service ou une réalisation partielle selon les contraintes, puis mobiliser D03 si la promesse doit être réexaminée.\n\nLe référentiel D14 décrit l’offre et les SLA globaux ; D06 traite le contexte opérationnel. D03 conserve la décision de promesse Supply, D04 les Orders et leurs reliquats, D01 la représentation du stock et de ses mouvements. Les exécutants conservent leurs opérations internes. La latitude d’adaptation est une règle de fonctionnement, sans effet sur le catalogue des capacités.'
}, ['definition'], ['U242', 'U244'])

edit_node('D06.a', {
    'name': 'Execution Service Qualification',
    'definition': 'Qualifier les lieux et services admissibles pour une prestation dans son contexte opérationnel.',
    'finality': 'Identifier les services réellement utilisables pour le résultat attendu.',
    'nature': 'decision',
    'scope': 'Mobiliser les lieux et relations de Fulfillment Network ainsi que les services, conditions et SLA du catalogue d’exécution. Examiner leur applicabilité au besoin : origine, destination, nature des biens ou documents, horaires et restrictions.\n\nExemple : un service de préparation existe au catalogue, mais le site concerné ne prend pas en charge cette catégorie de marchandises. Qualifier cette inadmissibilité sans administrer le référentiel. La capacité quantitative est évaluée par Execution Capacity Assessment ; la comparaison des solutions relève d’Execution Option Assessment.'
})
edit_node('D06.b', {
    'name': 'Execution Capacity Assessment',
    'definition': 'Décrire et apprécier la capacité opérationnelle des exécutants dans le contexte d’une prestation et d’une période.',
    'finality': 'Fournir à D03 et à l’orchestration les possibilités et limites concrètes de réalisation.',
    'nature': 'decision',
    'scope': 'Décrire notamment le nombre maximal de préparations dans un contexte donné, comme précisé en U240. D03 utilise cette connaissance pour sa promesse Supply.\n\nExemple illustratif : un entrepôt annonce un plafond de préparation pour le créneau considéré. Les unités, horizons, charge déjà engagée, ressources partagées et fraîcheur permettent d’interpréter ce chiffre ; leur détail demeure proposé. Un maximum ne constitue pas à lui seul une formule de capacité résiduelle.\n\nCette capacité évalue la réalisation possible ; elle ne confirme pas une promesse Supply. La mesure et la consommation de capacité restent à préciser comme règles, sans imposer un algorithme ou une réservation à chaque simulation.'
})
edit_node('D06.c', {
    'name': 'Execution Option Assessment',
    'definition': 'Établir et comparer les variantes de réalisation compatibles avec le résultat attendu et la situation opérationnelle.',
    'finality': 'Éclairer une solution initiale ou une adaptation réalisable du plan d’exécution.',
    'nature': 'decision',
    'scope': 'Comparer les origines, prestations, combinaisons ou séquences possibles à partir des services qualifiés, capacités contextuelles et engagements. Conserver cette responsabilité utile aussi avant une promesse.\n\nExemple : après un retard de préparation, examiner une collecte ultérieure ou un autre service de transport. Une variante peut préserver le résultat attendu ou nécessiter le réexamen de la promesse par D03. L’évaluation ne vaut ni engagement de l’exécutant ni modification de la promesse ; l’orchestration coordonne la mise en œuvre de la variante selon les règles applicables.'
})
edit_node('D07.a', {
    'name': 'Execution Requirement Definition',
    'definition': 'Exprimer les prestations nécessaires à la réalisation des Orders Supply sous forme de Service Orders compréhensibles par les exécutants.',
    'finality': 'Transmettre une demande de prestation explicite, exploitable et rattachable à son besoin.',
    'nature': 'action',
    'scope': 'Préciser résultats attendus, biens ou documents concernés, lieux, destinataires, quantités et échéances utiles. Distinguer une demande, son acceptation et sa réalisation ; aucune cardinalité Order/Service Order ni séquence technique universelle n’est imposée.\n\nExemple : exprimer les prestations de préparation, de production documentaire et de transport nécessaires à une commande. Le Service Order reste propre au contexte des prestations ; il ne recrée ni l’autorisation commerciale, ni l’Agreement, ni le Case. Le canal de sollicitation est décrit par les accès du service.'
})
edit_node('D07.b', {
    'name': 'Execution Commitment Management',
    'definition': 'Gérer la prise en charge et les engagements des exécutants, leur portée, leur validité et leurs évolutions.',
    'finality': 'Savoir ce qui est effectivement engagé et faire évoluer les prestations de manière maîtrisée.',
    'nature': 'management',
    'scope': 'Tenir les acceptations, refus, retraits, modifications et engagements de réalisation ; traiter les sollicitations de suspension, annulation ou reprise selon les possibilités propres au service et à son état. Distinguer SLA configuré, engagement pris pour une prestation, estimation actualisée et résultat constaté.\n\nExemple : un transporteur accepte une collecte à 16 h ; un retard impose de réviser cet engagement. L’estimation d’arrivée mise à jour n’est pas à elle seule une nouvelle acceptation. Un acquittement informatique ne prouve pas la réussite physique.\n\nLes règles éventuelles de consommation/libération de capacité restent à définir ; leur détail ne crée pas une nouvelle capacité. Les exécutants conservent leurs opérations internes et D03 la promesse Supply.'
})
edit_node('D07.c', {
    'name': 'Execution Reconciliation',
    'definition': 'Rapprocher les résultats constatés des prestations attendues, qualifier les écarts et fournir les faits utiles aux domaines consommateurs.',
    'finality': 'Expliquer les écarts de réalisation et alimenter le rapprochement des Orders sans confondre leurs reliquats.',
    'nature': 'action',
    'scope': 'Rapprocher production, préparation, expédition, réception, consommation et résultats documentaires des prestations demandées et engagées. Les quantités manquantes, écarts et résultats partiels sont qualifiés à la maille pertinente.\n\nExemple : 80 unités sont reçues sur les 100 attendues ; qualifier l’écart de prestation et en transmettre les faits à la commande concernée. D04 conserve le reliquat de l’Order et D01 la représentation des mouvements de stock. Les cinq contributions existantes vers les capacités par type d’Order sont conservées, avec leur statut proposé. Le tracking rend visible l’avancement ; le rapprochement explique le réalisé au regard de l’attendu.'
})
edit_node('D07.d', {
    'name': 'Execution Tracking',
    'definition': 'Suivre les faits, jalons, estimations et résultats encore attendus des prestations pendant leur réalisation.',
    'finality': 'Donner une connaissance actualisée de l’exécution pour anticiper les écarts et permettre l’adaptation.',
    'nature': 'knowledge',
    'scope': 'Conserver la responsabilité d’Expected Supply Tracking : quantités, dates, provenance et fermeté des ressources encore attendues. Étendre explicitement le suivi aux opérations et résultats des services, y compris documentaires, sans créer un cycle identique pour tous.\n\nExemple : préparation commencée, retard annoncé, expédition partielle, transport en cours ou document en échec. Identifier le fait, la prestation et sa fraîcheur ; distinguer estimation, engagement et constat. Le feedback continu signifie un suivi pendant la prestation, sans télémétrie temps réel uniforme imposée.\n\nLe tracking alimente l’orchestration et le réexamen de promesse lorsque nécessaire. Il ne décide pas seul d’une variante et ne tient pas le stock à la place de D01.'
})
new_node('D06.d', 'capability', {
    'name': 'Execution Orchestration',
    'definition': 'Coordonner les prestations et leurs dépendances, puis adapter le plan d’exécution en réponse aux faits et aux aléas.',
    'finality': 'Maintenir une réalisation cohérente du résultat attendu malgré les changements de situation.',
    'nature': 'orchestration',
    'scope': 'Coordonner les prestations entre exécutants à partir des demandes, engagements, évaluations et faits. Rechercher une variation du plan lorsque le réel contredit les conditions prévues ; mobiliser l’évaluation des options et la gestion des engagements pour la rendre exécutable.\n\nExemple : un SLA prévoit une préparation compatible avec la collecte, mais une panne retarde le départ. Exploiter le tracking, comparer les variantes et coordonner les prestations concernées, notamment transport et document. D03 réexamine la promesse Supply lorsque celle-ci est remise en cause.\n\nCette orchestration porte l’exécution Supply et respecte les opérations internes des exécutants. Les conditions d’autonomie, coûts et autorisations relèvent des règles de fonctionnement et ne conditionnent pas le catalogue. Aucun contrôle humain obligatoire, technologie de workflow, objet Plan formalisé ou rollback physique universel n’est imposé.'
})
new_node('D14', 'reference', {
    'name': 'Execution Service Catalog',
    'definition': 'Le référentiel contient la liste des services et leurs SLA globaux en configuration.',
    'finality': 'Partager une description des services exécutants, de leurs conditions et de leurs accès pour les mobiliser dans la Supply.',
    'scope': 'Offre de préparation, réception, transport et autres services tels que la production de documents. Décrire le résultat rendu, le prestataire, les conditions d’éligibilité et le SLA de réalisation applicable, ainsi que les accès informatiques de sollicitation et de feedback.\n\nExemple : un service de préparation à délai configuré, un transport et une génération de document ont des résultats et engagements différents. Le SLA exprime le service rendu, notamment lorsqu’il dépend du physique ; il reste distinct du temps de réponse informatique. L’identité métier d’un service est distincte de ses accès techniques ; un exécutant partiellement manuel peut être sollicité via une adaptation.\n\nCharge actuelle, capacité contextuelle, demandes, engagements individuels, estimations et résultats relèvent de D06. Fulfillment Network décrit les lieux et relations, Party les parties, Agreement les accords maîtres et Catalog les offres commerciales. Aucun protocole ni endpoint unique imposé.',
    'mastership': 'Projection de sources maîtresses externes, suivant le principe courant des référentiels Supply. Maître de configuration et articulation avec Agreement à préciser ; aucune administration locale présumée.'
}, ['definition'], ['U240', 'U244'])
new_node('D14.a', 'capability', {
    'name': 'Execution Service Catalog Ingestion',
    'definition': 'Recevoir l’offre des services exécutants, leurs SLA configurés, conditions et accès, ainsi que leurs évolutions depuis les sources maîtresses externes.',
    'finality': 'Mettre à disposition une projection de référence exploitable par la qualification, la promesse et l’orchestration.',
    'nature': 'action',
    'scope': 'Ingestion du référentiel, dans la continuité du principe des projections Supply. Recevoir les évolutions des services et de leurs accès sans reprendre la maîtrise des données. Consultation et recherche restent en lecture seule pour les consommateurs.\n\nL’ingestion du catalogue ne reçoit pas à sa place le tracking des opérations et ne transforme pas une évolution du SLA en révision automatique des engagements déjà pris. Maîtres et contrats d’échange seront définis dans les règles de fonctionnement.'
})

# Retrait du seul domaine ; les identités des capacités D07 restent stables.
model['nodes'] = [n for n in model['nodes'] if n['id'] != 'D07']
model['relations'] = [r for r in model['relations'] if r['id'] != 'REL-UNIVERSE-SUPPLY-D07']
for ident in ['D07.a', 'D07.b', 'D07.c', 'D07.d']:
    r = relations['REL-MEMBER-' + ident]
    r['source_id'] = 'D06'
    r['revision'] += 1
    r['source_refs'] = list(dict.fromkeys(r['source_refs'] + ['U238', 'U244']))
    r['review'] = {'state': 'accepted', 'note': 'Rattachement des capacités existantes au domaine regroupé demandé U238/U244 ; pas de validation des nouvelles formulations.'}
    r['lifecycle'] = lifecycle(r, ['type', 'source_id', 'target_id'], refs=['U238', 'U244'])

def relation(identifier, kind, source, target, meaning=None, adopted=False):
    assert identifier not in relations
    r = {'id': identifier, 'revision': 1, 'type': kind, 'source_id': source, 'target_id': target,
         'source_refs': REFS, 'review': {'state': 'accepted' if adopted else 'proposed',
         'note': 'Regroupement ou nouveau référentiel demandé en U244.' if adopted else 'Relation explicitée pour U244 ; détail de projection proposé.'}}
    if meaning:
        r['qualification'] = {'meaning': meaning, 'conditions': [], 'effects': [],
                              'scope': 'Responsabilité métier ; aucun contrat technique, seuil, automatisation ou cardinalité imposé.'}
    r['lifecycle'] = lifecycle(r, ['type', 'source_id', 'target_id'] if adopted else (), refs=['U244'])
    model['relations'].append(r)
    relations[identifier] = r
    return r

relation('REL-MEMBER-D06.d', 'contains', 'D06', 'D06.d')
relation('REL-GROUP-D14', 'presents', 'business-references', 'D14', adopted=True)
relation('REL-MEMBER-D14.a', 'contains', 'D14', 'D14.a')
relation('REL-SERVICE-CATALOG-EXECUTION', 'provides-conditions', 'D14', 'D06', 'Le référentiel fournit l’offre, les SLA configurés et les accès des services ; le domaine qualifie leur emploi et pilote les prestations dans le contexte.')
relation('REL-SERVICE-CATALOG-PROMISING', 'provides-conditions', 'D14', 'D03', 'D03 utilise les conditions de service configurées pour construire la promesse, avec la capacité contextuelle fournie par D06 et les autres informations Supply.')
relation('REL-EXECUTION-PROMISING', 'provides-knowledge', 'D06', 'D03', 'D06 décrit les capacités et possibilités opérationnelles ainsi que les évolutions d’exécution utiles au calcul et au réexamen de la promesse Supply par D03.')
relation('REL-EXECUTION-TRACKING-ORCHESTRATION', 'relates-to', 'D07.d', 'D06.d', 'Le tracking fournit faits, jalons et estimations permettant à l’orchestration de détecter les aléas et d’adapter le plan.')
relation('REL-EXECUTION-ORCHESTRATION-OPTIONS', 'relates-to', 'D06.d', 'D06.c', 'L’orchestration mobilise l’évaluation des options pour rechercher et comparer des variantes ; cette mobilisation ne crée pas une hiérarchie de capacités.')
relation('REL-EXECUTION-ORCHESTRATION-COMMITMENTS', 'relates-to', 'D06.d', 'D07.b', 'L’orchestration mobilise la gestion des engagements pour coordonner les prestations et leurs évolutions ; les possibilités propres à chaque service sont respectées.')
relation('REL-EXECUTION-ORCHESTRATION-PROMISE-REVISION', 'relates-to', 'D06.d', 'D03.c', 'Lorsqu’une variation d’exécution remet la promesse en cause, l’orchestration fournit les faits et variantes utiles à son réexamen par D03 ; elle ne révise pas elle-même la promesse Supply.')

model['source_version'] += ' + U244 référentiel des services, regroupement D06/D07 et orchestration adaptative'
model['as_of'] = '2026-09-16'
model['limitations'].append('U244 regroupe D06/D07 sous D06 et ajoute D14 Execution Service Catalog. D07 seul est retiré, ses capacités conservent leurs identités et leurs liens de rapprochement D04. D06.d ajoute l’orchestration, D07.d élargit le tracking. État antérieur : history/pre-U244.yaml. La définition de domaine et les principes sont adoptés dans leurs portées ; nouveaux noms et compléments de capacités proposés. La latitude d’adaptation est hors définition du catalogue. Aucune publication implicite.')
model['principles'].append({'id': 'PRINCIPLE-EXECUTION-ORCHESTRATION',
    'statement': 'Le référentiel des services porte l’offre et les SLA configurés ; D06 décrit la capacité contextuelle et orchestre l’exécution, son tracking et son adaptation. D03 utilise D06 pour la promesse Supply et son réexamen ; les exécutants gardent leurs opérations internes. Un SLA compatible n’empêche pas un échec opérationnel. La latitude d’adaptation relève des règles de fonctionnement sans impact sur le catalogue des capacités.', 'source_refs': ['U240', 'U242', 'U243', 'U244']})

glossary = read(ROOT / 'modeles/backlog/glossary.yaml')
for identifier, name, short, definition, notes in [
    ('TER075', 'Execution Service', 'Prestation proposée par un exécutant avec un résultat et des conditions définis.', 'Service rendu par un exécutant, notamment entrepôt, transport ou production de documents, décrit par son résultat, ses conditions et ses engagements de service.', 'L’offre est décrite dans [Execution Service Catalog](model:D14) ; une demande de prestation utilise un [Service Order](glossary:TER066). Le service métier est distinct de son accès informatique et de chacune de ses réalisations.'),
    ('TER076', 'Service Level Agreement (SLA)', 'Engagement de niveau de service applicable sous des conditions définies.', 'Engagement de niveau de service décrivant les conditions et résultats de service attendus, notamment les délais de réalisation applicables.', 'Dans cette refonte, le référentiel D14 contient les SLA globaux configurés. Ils restent distincts de l’engagement individuel de prestation, de l’estimation actualisée et du résultat observé. Un SLA compatible ne garantit pas la réussite opérationnelle ; le maître de configuration et le lien à Agreement restent à préciser.')
]:
    assert identifier not in {t['id'] for t in glossary['terms']}
    glossary['terms'].append({'id': identifier, 'name': name, 'short_description': short, 'definition': definition,
        'context': 'Définition métier proposée pour la refonte U244 ; pas de nouveau type d’objet instancié.', 'notes': notes,
        'source_refs': REFS, 'source_locator': {'path': DOC, 'anchor': 'vocabulaire'},
        'review': {'state': 'proposed', 'note': 'Formulation proposée ; les principes adoptés ne valident pas le terme entier.'}})
glossary['as_of'] = '2026-09-16'
glossary['source_refs'] = list(dict.fromkeys(glossary['source_refs'] + ['U244']))
write('modeles/backlog/glossary.yaml', glossary)

catalog_ids = ['D06.a', 'D06.b', 'D06.c', 'D07.a', 'D07.b', 'D07.d', 'D07.c', 'D06.d']
doc = ['# Pilotage et orchestration de l’exécution — U244', '',
       'Mise à jour du backlog le 16 septembre 2026. Autorité : `modeles/backlog/model.yaml`. D05 conservé ; D06 regroupe les responsabilités de D06/D07. D07 est retiré comme domaine, ses capacités gardent leurs identifiants. La release reste inchangée.', '',
       'Les principes U240/U242/U243 et la définition de domaine présentée avant U244 sont adoptés dans leurs portées. Les nouveaux noms anglais, le détail des capacités, les exemples et qualifications de relations restent proposés. La latitude d’adaptation ne conditionne pas le catalogue.', '',
       '| Identifiant | Capacité du domaine D06 | Responsabilité |', '| --- | --- | --- |']
doc += [f"| {i} | {nodes[i]['fields']['name']} | {nodes[i]['fields']['definition']} |" for i in catalog_ids]
for identifier in ['D06'] + catalog_ids + ['D14', 'D14.a']:
    f = nodes[identifier]['fields']
    doc += ['', f'<a id="{identifier.lower().replace(".", "-")}"></a>', f'## {identifier} — {f["name"]}', '', f['definition'], '', f['scope']]
doc += ['', '## Vocabulaire', '', 'TER075 Execution Service et TER076 Service Level Agreement sont ajoutés comme propositions au glossaire métier. TER066 Service Order conserve son sens. Le glossaire de modélisation reste distinct et inchangé.', '',
        '## Frontières et continuité', '', 'Les cinq liens D07.c vers D04.i–m sont conservés à l’identique. D01/D03/D04/D05 et les cinq référentiels existants conservent leurs nœuds. D06.a continue la qualification des lieux/services ; D07.d conserve les ressources encore attendues et étend son tracking aux prestations. Aucun préfixe d’identifiant ne détermine le parent.', '',
        'La nouvelle définition de D06 rend l’adaptation explicite. Les règles d’autonomie, mesures et contrats d’échange restent des questions de fonctionnement. La réalisation interne des exécutants et la promesse Supply D03 restent distinctes.', '',
        '## Marché', '', 'CMP078 actualise la projection locale de CMP077 sur les nœuds appliqués. Les études U239/U241 restent les preuves consultées ; aucune nouvelle vérification éditeur réalisée dans cette application. Appuis partiels TM Forum au catalogue/qualification/orchestration et Microsoft/SAP à la contribution de capacité vers la promesse ; aucune équivalence globale ou couverture installée démontrée.', '']
(ROOT / DOC).write_text('\n'.join(doc), encoding='utf-8', newline='\n')

append('marche/comparaisons.md', '''### CMP078

- État comparé : backlog appliqué U244, D06 regroupé, D14 nouveau référentiel ; nœuds D06.a–d et D07.a–d, D14.a. D05 inchangé.
- Éléments : ELM129–134 et ELM136–137, consultés le 16 septembre 2026 dans les études U239/U241. Actualisation de correspondance depuis ces preuves, sans nouvelle consultation éditeur.
- D14/D14.a : appui sémantique ELM129 au catalogue, aucune équivalence de l’ingestion locale. D06.a : qualification ELM130, adaptation télécom/logistique. D06.b : ELM136/137 soutiennent partiellement capacité vers promesse, sans preuve de l’API logistique envisagée. D06.c : options de réalisation, équivalence détaillée non établie.
- D07.a/b : appuis ELM131/133 aux demandes et engagements, sans cycle universel. D07.d : appuis ELM133/134 aux faits et suivi, extension documentaire et ressources attendues locales. D07.c : rapprochement de prestations versus reliquats Order, équivalence détaillée non établie. D06.d : appui ELM132 à la coordination des dépendances ; latitude d’adaptation locale hors définition du catalogue selon U243.
- Justification, limites et sources : execution-services-revised-comparison.md et connaissance/32-execution-orchestration.md. Noms et granularité d’application proposés ; aucune équivalence globale, conformité ou preuve de couverture installée.
- Auteur/date/statut : Codex, 2026-09-16, proposé ; aucun valideur de comparaison.
''')
append('marche/execution-services-revised-comparison.md', '''## Application U244 — correspondance CMP078

Le backlog comporte désormais D06 Execution Management, huit capacités directement rattachées et D14 Execution Service Catalog avec son ingestion. D07 est retiré comme domaine ; ses quatre capacités conservent leurs identités sous D06. CMP078 détaille les appuis et les parties non comparées à cette nouvelle maille ; aucun nouvel accord sur les équivalences de marché. Voir [la description concrète](../connaissance/32-execution-orchestration.md).
''')
for entry in model['source_files']:
    entry['sha256'] = sha(ROOT / entry['path'])
model['source_files'].append({'path': DOC, 'sha256': sha(ROOT / DOC)})
write('modeles/backlog/model.yaml', model)

review = read(ROOT / 'modeles/backlog/execution-services-review.yaml')
review['state'] = 'applied_to_backlog_U244'
review['source_refs'].append('U244')
review['identity_question']['no_model_mutation'] = False
review['identity_question']['resolution'] = 'U238 confirme D06/D07 et conserve D05 ; regroupement appliqué en U244, D07 retiré comme domaine.'
review['assistant_proposal']['state'] = 'applied_U244_names_and_details_proposed_see_field_scopes'
review['open_points'][0] = 'Éprouver les noms et la granularité appliqués en U244 ; leur proposition est dans le modèle actif, les règles de latitude restent séparées.'
review['publication'] = 'Refonte appliquée au backlog U244 ; aucune nouvelle publication. Atlas conserve la release désignée par son index.'
review['application_U244'] = {
    'source_refs': ['U244'], 'before_snapshot': HISTORY.relative_to(ROOT).as_posix(), 'before_sha256': sha(HISTORY),
    'domain_id': 'D06', 'retired_domain_id': 'D07', 'reference_id': 'D14', 'capability_ids': catalog_ids,
    'reference_capability_ids': ['D14.a'], 'new_ids': ['D06.d', 'D14', 'D14.a'],
    'retained_capability_ids': ['D06.a', 'D06.b', 'D06.c', 'D07.a', 'D07.b', 'D07.c', 'D07.d'],
    'retired_relation_ids': ['REL-UNIVERSE-SUPPLY-D07'], 'market_comparison': 'CMP078',
    'approved_node_fields': {i: n['lifecycle']['validated_fields'] for i,n in nodes.items() if i in ['D06','D14']},
    'proposed_details': ['Noms anglais non explicitement adoptés', 'Granularité et descriptions détaillées des capacités', 'Exemples et qualifications des relations', 'TER075 et TER076'],
    'preservation': 'D05 et les autres nœuds hors refonte inchangés ; cinq liens D07.c vers D04.i–m identiques ; aucun transfert de validation depuis D07 retiré.'
}
write('modeles/backlog/execution-services-review.yaml', review)

p = ROOT / 'AGENTS.md'
data = p.read_bytes()
old = 'Noms, découpage détaillé, mesure de capacité et maître de configuration restent à préciser ; les nœuds ne sont pas encore restructurés.'.encode('utf-8')
new = 'U244 applique la refonte : D06 **Execution Management** regroupe huit capacités, dont **Execution Orchestration** ; D07 est retiré comme domaine et ses capacités gardent leurs identités sous D06. D07.d devient **Execution Tracking**, avec maintien des résultats encore attendus. D14 **Execution Service Catalog** et son ingestion rejoignent Business References. Nouveaux noms et détails de capacités restent proposés ; la définition de domaine présentée avant U244 est adoptée. Les règles de mesure et le maître de configuration restent à préciser sans bloquer le catalogue. État antérieur conservé dans `history/pre-U244.yaml` ; aucune publication implicite.'.encode('utf-8')
assert data.count(old) == 1
data = data.replace(old, new).replace('**Pilotage de l\'exécution — U237 à U243 :**'.encode('utf-8'), '**Pilotage de l\'exécution — U237 à U244 :**'.encode('utf-8'))
p.write_bytes(data)
append('JOURNAL.md', '''## 2026-09-16 — U244 : refonte de l’exécution appliquée au backlog

D06 Execution Management regroupe les responsabilités D06/D07, ajoute Execution Orchestration et élargit D07.d en Execution Tracking avec conservation des résultats encore attendus. D14 Execution Service Catalog et son ingestion ajoutés. Les relations D03/capacité/révision et tracking/orchestration/options/engagements sont explicites ; cinq liens de rapprochement D04 préservés. D05 inchangé. Captures, portées et contrôles dans audits/2026-09-16-execution-refonte et execution-services-review.yaml. Noms et détails ajoutés proposés ; définition de domaine présentée avant U244 adoptée. TER075/076 proposés, glossaire de modélisation séparé inchangé. Aucune publication, commit ou push.
''')

# Invariants de portée, contrôlés avant les validations standard.
after_nodes = {n['id']: n for n in model['nodes']}
changed = {'D06', 'D06.a', 'D06.b', 'D06.c', 'D07', 'D07.a', 'D07.b', 'D07.c', 'D07.d'}
assert all(after_nodes[n['id']] == n for n in before['nodes'] if n['id'] not in changed)
after_rel = {r['id']: r for r in model['relations']}
changed_rel = {'REL-UNIVERSE-SUPPLY-D07'} | {'REL-MEMBER-' + i for i in ['D07.a','D07.b','D07.c','D07.d']}
assert all(after_rel[r['id']] == r for r in before['relations'] if r['id'] not in changed_rel)
assert {r['target_id'] for r in model['relations'] if r['type']=='contains' and r['source_id']=='D06'} == set(catalog_ids)
assert all(sha(ROOT / name) == fingerprint for name,fingerprint in protected.items())
print(json.dumps({'nodes': len(model['nodes']), 'capabilities': sum(n['kind']=='capability' for n in model['nodes']), 'relations': len(model['relations']), 'glossary_terms': len(glossary['terms']), 'protected_files': len(protected), 'scope_checks': 'passed'}))

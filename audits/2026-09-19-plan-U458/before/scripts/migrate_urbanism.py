"""One-time, reviewable Markdown import. Never overwrite an existing release.

After this import, JSON is edited directly; this is not the application's reader.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import re
import sys
import html
import unicodedata

ROOT = Path(__file__).resolve().parents[1]

def plain_text(value):
    value = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', value)
    return html.unescape(value.replace('**','').replace('`','')).strip()


def heading_anchor(value):
    value = unicodedata.normalize('NFKC', plain_text(value)).lower()
    return re.sub(r'[-\s]+','-',re.sub(r'[^\w\s-]','',value).strip())


def _parse_map(text):
    """Bootstrap parser copied in purpose from the audited former Atlas reader."""
    version = re.search(r'version de travail\s+(\d+(?:\.\d+)+)',text[:1800])[1]
    domains=[]; domain=None; table=False; group='transactional'; anchor=None
    for line_num,line in enumerate(text.splitlines(),1):
        if '<a id=' in line:
            anchor=re.search(r'id="([^"]+)"',line)[1]
        heading=re.match(r'^### (D\d{2}) — (.+)$',line)
        if heading:
            domain={'id':heading[1],'name':heading[2],'group':group,'sourceAnchor':anchor or heading_anchor(heading[1]+' — '+heading[2]),'sourceLine':line_num,'capabilities':[]}
            domains.append(domain);table=False;anchor=None
        elif line.startswith('#'):
            table=False;anchor=None
            if line.startswith('## '):
                domain=None
                if line=='## Business References': group='references'
        elif domain and line.startswith('| Repère |'):
            table=True
        elif table and line.startswith('|'):
            cells=[c.strip() for c in line.strip('|').split('|')]
            if re.fullmatch(r'D\d{2}\.[a-z]+',cells[0]):
                m=re.fullmatch(r'\*\*(.+?)\*\*\s*:\s*(.+)',cells[1]);assert m
                domain['capabilities'].append({'id':cells[0],'name':plain_text(m[1]),'definition':plain_text(m[2]),'purpose':plain_text(cells[2]),'parentId':domain['id'],'sourceAnchor':domain['sourceAnchor'],'sourceLine':line_num})
        elif table:
            table=False
    assert len(domains)==12 and sum(len(d['capabilities']) for d in domains)==36
    return 'P81 '+version,'2026-09-11',domains

VERSION = '2026-09-13.1'
MAP = 'connaissance/25-domaines-coeur-et-epreuve-recits.md'
USERS = 'connaissance/01-contributions-utilisateur.md'


def sha(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def write(path, value, immutable=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    if immutable and path.exists() and path.read_text(encoding='utf-8') != content:
        raise ValueError(f'Immutable file already exists: {path}')
    path.write_text(content, encoding='utf-8')


def source_records():
    records = []
    registry_names = {'U':'01-contributions-utilisateur.md','F':'02-assertions.md','A':'03-contributions-assistant.md','C':'04-corrections.md','P':'05-propositions.md','Q':'06-questions.md','CAP':'09-capacites-candidates.md','INF':'10-autorites-information.md','DEC':'11-responsabilites-decision.md','MKT':'catalogue.md','ELM':'elements.md','CMP':'comparaisons.md','ORG':'07-composants.md','APP':'07-composants.md','SI':'07-composants.md','ALIAS':'07-composants.md','FL':'08-flux.md'}
    for folder in ('connaissance', 'marche'):
        for path in sorted((ROOT / folder).glob('*.md')):
            text = path.read_text(encoding='utf-8')
            headings = list(re.finditer(r'^#{2,3} ((?:U|F|A|C|P|Q|CAP|INF|DEC|MKT|ELM|CMP)\d+|(?:ORG|APP|SI|ALIAS)-[A-Z0-9-]+|FL\d+)\b[^\n]*', text, re.M))
            for i, m in enumerate(headings):
                prefix = re.match(r'[A-Z]+',m[1])[0]
                if registry_names.get(prefix) != path.name:
                    continue
                end = headings[i+1].start() if i+1 < len(headings) else len(text)
                block = text[m.start():end].strip()
                records.append({'id': m[1], 'path': path.relative_to(ROOT).as_posix(), 'anchor': heading_anchor(m[0].lstrip('# ')), 'line': text[:m.start()].count('\n')+1, 'content_sha256': hashlib.sha256(block.encode()).hexdigest(), 'captured_text': block})
            # Earlier market records are table rows, not headings.
            existing = {r['id'] for r in records}
            for m in re.finditer(r'^\| ((?:CMP|ELM|MKT)\d+) \|.*$', text, re.M):
                if m[1] not in existing:
                    records.append({'id': m[1], 'path': path.relative_to(ROOT).as_posix(), 'anchor': '', 'line': text[:m.start()].count('\n')+1, 'content_sha256': hashlib.sha256(m[0].encode()).hexdigest(), 'captured_text': m[0]})
    assert len({r['id'] for r in records}) == len(records), 'Duplicate source identity'
    return records


def build(destination):
    text = (ROOT / MAP).read_text(encoding='utf-8')
    version, date, domains = _parse_map(text)
    metadata = json.loads((ROOT / 'app/model-metadata.json').read_text(encoding='utf-8'))
    assert metadata['sourceSha256'] == hashlib.sha256((ROOT / MAP).read_bytes()).hexdigest(), 'Metadata requires review'
    meta = {d['id']: d for d in metadata['domains']}
    state_map = {'retained': 'partial', 'validated': 'partial', 'review': 'under_review', 'hypothesis': 'proposed', 'proposed': 'proposed'}
    nodes, relations = [], []
    def node(identifier, kind, fields, refs, locator, state='proposed', note='', layer='transactional'):
        n = {'id': identifier, 'revision': 1, 'kind': kind, 'layer': layer, 'fields': fields, 'source_refs': refs, 'source_locator': locator, 'review': {'state': state, 'note': note}}
        nodes.append(n)
        return n
    def relation(identifier, typ, source, target, refs, state='proposed', note=''):
        r = {'id': identifier, 'revision': 1, 'type': typ, 'source_id': source, 'target_id': target, 'source_refs': refs, 'review': {'state': state, 'note': note}}
        relations.append(r)
        return r
    node('business-references', 'group', {'name': 'Business References'}, ['U103'], {'path': MAP, 'anchor': 'business-references'}, 'accepted', 'Groupe de présentation, pas une capacité mère.')
    for d in domains:
        baseline = meta[d['id']]
        # Domain summaries remain explicitly authored working formulations.
        fields = {'name': d['name'], 'definition': baseline['definition'], 'finality': baseline['purpose']}
        loc = {'path': MAP, 'anchor': d['sourceAnchor'], 'line': d['sourceLine']}
        kind = 'reference' if d['group'] == 'references' else 'domain'
        n = node(d['id'], kind, fields, baseline['sources'], loc, state_map[baseline['status']], baseline['statusNote'])
        n['editorial_basis'] = 'Domain definition/finality: dated assistant summary from app/model-metadata.json, not independently approved.'
        if kind == 'reference':
            relation('REL-GROUP-' + d['id'], 'presents', 'business-references', d['id'], ['U103'], 'accepted', 'Appartenance de présentation uniquement.')
        cm = {c['id']: c for c in baseline['capabilities']}
        for c in d['capabilities']:
            info = cm[c['id']]
            loc = {'path': MAP, 'anchor': c['sourceAnchor'], 'line': c['sourceLine']}
            fields = {'name': c['name'], 'definition': c['definition'], 'finality': c['purpose']}
            if d['id'] == 'D03':
                fields['nature'] = 'decision' if c['id'] in ['D03.d','D03.e','D03.f','D03.g','D03.h'] else 'action'
            node(c['id'], 'capability', fields, info['sources'], loc, state_map[info['status']], info['statusNote'])
            relation('REL-MEMBER-' + c['id'], 'contains', d['id'], c['id'], info['sources'], state_map[info['status']], 'Parent explicite ; ne jamais le déduire de l’identifiant.')
    # Keep the alternative P82 as its own proposal, not as the approved D01.
    start = text.index('#### Proposition de cinq capacités D01')
    end = text.index('#### Noms des capacités de stock', start)
    alternatives = []
    rows = [line for line in text[start:end].splitlines() if line.startswith('| **')]
    proposal_members = []
    for i, row in enumerate(rows, 1):
        cells = [plain_text(c) for c in row.strip('|').split('|')]
        proposal_members.append({'name': cells[0], 'definition': cells[1], 'finality': cells[2], 'legacy_alignment': cells[3]})
    assert len(proposal_members) == 5
    alternatives.append({'id': 'P82', 'kind': 'alternative_decomposition', 'target_id': 'D01', 'state': 'proposed', 'source_refs': ['P82','U83','U86'], 'members': proposal_members, 'note': 'Fusion D01.a/D01.b et nom Inventory Visibility non adoptés ; les noms Reservation et Stocktaking ont leurs décisions distinctes.'})
    alternatives.append({'id': 'P84', 'kind': 'alternative_labels', 'target_id': 'D04', 'state': 'proposed', 'source_refs': ['P84','U100'], 'field_overrides': [{'target_id': ident, 'field': 'name', 'value': name} for ident,name in [('D04.a','Commitment Creation'),('D04.b','Commitment Revision'),('D04.c','Commitment Reconciliation'),('D04.d','Return and Replacement Decision')]], 'note': 'D04/D07 à refondre selon la Supply documentaire générique.'})
    exploration = json.loads((ROOT / 'app/legacy/exploration-before-json.json').read_text(encoding='utf-8'))
    for n in exploration['nodes']:
        if n['id'].startswith('ILL-'):
            node(n['id'], n['kind'], {'name': n['name'], 'definition': n['definition'], 'finality': n['purpose']}, n['sources'], {'path': n['sourcePath'], 'anchor': ''}, 'illustration', n['statusNote'], n.get('modelId', 'transactional'))
    for i,r in enumerate(exploration['relations'], 1):
        relation(f'REL-ILL-{i:03}', r['type'], r['from'], r['to'], r['sources'], 'illustration', 'Relation illustrative importée ; identité nouvellement allouée, aucune validation métier.')
    ids = {n['id']: n for n in nodes}
    rids = {r['id']: r for r in relations}
    decisions = []
    def accept(identifier, fields, source_refs, mode='explicit', note='', overrides=None):
        n = ids[identifier]
        if overrides:
            n['fields'].update(overrides)
        decisions.append({'id': f'ADOPT-{len(decisions)+1:03}', 'decision_state': 'accepted', 'author': 'Laurent', 'decided_at': '2026-09-11', 'recorded_at': '2026-09-13', 'interpretation': mode, 'source_refs': source_refs, 'note': note, 'target': {'collection': 'nodes', 'id': identifier, 'revision': n['revision'], 'approved_fields': fields, 'value_sha256': {f: sha(n['fields'][f]) for f in fields}}})
    def accept_relation(identifier, refs, review='accepted', note='', mode='explicit'):
        r = rids[identifier]
        r['review'] = {'state': review, 'note': note}
        decisions.append({'id': f'ADOPT-{len(decisions)+1:03}', 'decision_state': 'accepted', 'author': 'Laurent', 'decided_at': '2026-09-11', 'recorded_at': '2026-09-13', 'interpretation': mode, 'source_refs': refs, 'note': note, 'target': {'collection': 'relations', 'id': identifier, 'revision': 1, 'approved_fields': ['type','source_id','target_id'], 'value_sha256': {f: sha(r[f]) for f in ['type','source_id','target_id']}}})
    accept('D01', ['name','scope'], ['U66','U80','U81'], note='Le périmètre est une reformulation des orientations ; liste complète de capacités non validée.', overrides={'scope': 'Stocks physiques, états logiques et connaissance des ressources futures ; disponibilité virtuelle pour la promesse dans Order Promising.'})
    accept('D03', ['name'], ['U52','U95'])
    d03 = [c for d in domains if d['id']=='D03' for c in d['capabilities']]
    for c in d03:
        accept(c['id'], ['name','definition','finality','nature'], ['U95','P83','C63'], note='Quatre actions et cinq décisions dans la portée présentée ; autorités et interactions détaillées non adoptées.')
        accept_relation('REL-MEMBER-'+c['id'], ['U95','U75'], note='Liste adoptée dans Order Promising, y compris D02.e.')
    accept('D01.d', ['name','definition','finality'], ['U86','C58'], 'contextual', 'Accord sur Stocktaking et sens de comptage/rapprochement/correction ; ne valide pas la fusion P82.')
    accept_relation('REL-MEMBER-D01.d', ['U86'], mode='contextual', note='Capacité discutée dans D01 ; maille complète du domaine ouverte.')
    accept('D02.b', ['name'], ['U67'])
    accept_relation('REL-MEMBER-D02.b', ['U74'])
    accept('D02.c', ['name'], ['U84'])
    accept_relation('REL-MEMBER-D02.c', ['U75','U78'], 'under_review', 'Dernier rattachement retenu U75, réexaminé U78 ; pas de nouvelle frontière décidée.')
    for ident in ['D09','D11','D12']:
        accept(ident, ['name','mastership'], ['U97','U98'], overrides={'mastership': 'external'})
    accept('D08', ['independence'], ['U100'], overrides={'independence': 'Référence article autonome ; un SKU peut être proposé dans plusieurs catalogues.'})
    accept('D13', ['name','independence'], ['U102'], overrides={'independence': 'Party et lieu distincts ; référentiel Fulfillment Network demandé.'})
    for parent, child in [('D09','D09.d'),('D11','D11.a'),('D12','D12.a'),('D08','D08.d'),('D13','D13.a')]:
        refs = ['U97'] if parent in ['D09','D11','D12'] else ['U103']
        accept(child, ['scope'], refs, 'explicit' if refs==['U97'] else 'contextual', 'Ingestion seule ; nom anglais exact et prose détaillée restent proposés.', {'scope': 'Recevoir les informations de référence et leurs évolutions ; aucune administration ou validation des données maîtresses dans la plateforme.'})
        accept_relation('REL-MEMBER-'+child, refs, mode='explicit' if refs==['U97'] else 'contextual', note='Une ingestion pour ce référentiel ; détails et maître par attribut ouverts.')
    accept('business-references', ['name'], ['U103'], 'contextual', 'Accord contextuel déjà consigné, sur la présentation de cinq références uniquement.')
    for parent in ['D09','D11','D08','D12','D13']:
        accept_relation('REL-GROUP-'+parent, ['U103'], mode='contextual', note='Groupe de présentation distinct d’un domaine fusionné.')
    # Explicit architecture principles, separate from the graph hierarchy.
    principles = [
        {'id':'PRINCIPLE-TWO-LAYERS','statement':'Socle transactionnel et modèle processus distincts ; chacun possède ses objets, sa persistance et son urbanisation.','source_refs':['U18','U19','U20','U49','U50','U62']},
        {'id':'PRINCIPLE-CAPABILITY','statement':'Une capacité décrit ce que sait faire l’entreprise indépendamment de son organisation et de ses outils.','source_refs':['U33']},
        {'id':'PRINCIPLE-SUPPLY-DOCUMENTS','statement':'Supply générique orientée documents d’autorisation ; les parcours commerciaux appartiennent au modèle processus.','source_refs':['U100']},
        {'id':'PRINCIPLE-FLOW-LOGISTICS','statement':'Logistique hors développement FLOW, en adhérence ; autonomie C-Log conservée.','source_refs':['U58']},
        {'id':'PRINCIPLE-CTP-DEFERRED','statement':'ATP associé à la promesse ; CTP conservé au glossaire et placement différé.','source_refs':['U95']},
        {'id':'PRINCIPLE-ORDER-AGREEMENT','statement':'Commandes distinctes des Agreements de référence.','source_refs':['U98']},
    ]
    inputs = [MAP, USERS, 'connaissance/04-corrections.md','connaissance/05-propositions.md','app/model-metadata.json','app/legacy/exploration-before-json.json']
    basis = [{'path':p, 'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in inputs]
    common = {'schema_version':'1.0.0','model_id':'flow-urbanism','version':VERSION,'as_of':'2026-09-13','source_version':version,'source_files':basis}
    backlog = {**common,'space':'backlog','nodes':nodes,'relations':relations,'alternatives':alternatives,'principles':principles,'limitations':['Les propositions et illustrations ne sont pas validées par leur extraction.','Le modèle processus détaillé reste à construire.','Les synthèses de domaines importées de la présentation sont identifiées comme éditoriales.']}
    release_nodes, release_relations = {}, {}
    for decision in decisions:
        t = decision['target']; source = ids[t['id']] if t['collection']=='nodes' else rids[t['id']]
        target_collection = release_nodes if t['collection']=='nodes' else release_relations
        if source['id'] not in target_collection:
            if t['collection']=='nodes':
                target_collection[source['id']] = {k:copy.deepcopy(source[k]) for k in ['id','revision','kind','layer','source_refs','source_locator']}
                target_collection[source['id']]['fields'] = {}
                target_collection[source['id']]['review'] = {'state':'partial','note':'Seuls les champs explicitement présents sont repris comme adoptés ; autres aspects ouverts.'}
            else:
                target_collection[source['id']] = copy.deepcopy(source)
            target_collection[source['id']]['adoption_ids'] = []
        out = target_collection[source['id']]
        if t['collection']=='nodes':
            out['fields'].update({f:source['fields'][f] for f in t['approved_fields']})
            out['missing_fields'] = sorted(set(source['fields'])-set(out['fields']))
        out['adoption_ids'].append(decision['id'])
    for c in d03:
        release_nodes[c['id']]['review'] = {'state':'accepted','note':'Capacité validée U95 dans sa portée présentée ; frontières et autorités détaillées ouvertes.'}
    for r in release_relations.values():
        assert r['source_id'] in release_nodes and r['target_id'] in release_nodes
    release = {**common,'space':'release','release_kind':'partial_baseline','nodes':list(release_nodes.values()),'relations':list(release_relations.values()),'principles':principles,'limitations':['Première compilation des validations antérieures, pas une nouvelle validation globale.','Une fiche partielle peut ne pas avoir de nom anglais adopté : afficher son identifiant sans reprendre le libellé du backlog.','Reservation conserve son rattachement antérieur avec réexamen visible.','Absence de capacité en release ne signifie pas absence de besoin dans l’entreprise.'],'excluded_nodes':[{'id':n['id'],'reason':'Aucun aspect de cette fiche individuelle adopté dans les sources examinées.','source_refs':n['source_refs']} for n in nodes if n['id'] not in release_nodes]}
    for n in nodes:
        n['adoption_ids'] = [d['id'] for d in decisions if d['target']['collection']=='nodes' and d['target']['id']==n['id']]
    for d in decisions:
        d['target']['import_version'] = VERSION
    write(destination/'backlog/model.json',backlog)
    write(destination/f'revisions/{VERSION}/backlog.json',backlog,True)
    write(destination/f'decisions/{VERSION}.json',{'schema_version':'1.0.0','version':VERSION,'decisions':decisions},True)
    path=destination/f'release/{VERSION}/model.json'
    write(path,release,True)
    write(destination/'release/current.json',{'schema_version':'1.0.0','model_id':'flow-urbanism','space':'release','version':VERSION,'path':f'{VERSION}/model.json','sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    records = source_records()
    write(destination/'provenance/source-records.json',{'schema_version':'1.0.0','captured_at':'2026-09-13','records':records})
    write(destination/f'provenance/{VERSION}/source-records.json',{'schema_version':'1.0.0','captured_at':'2026-09-13','records':records},True)
    # Preserve CAP history as a separate inventory, not a second active map.
    write(destination/'backlog/legacy-capabilities.json',{'schema_version':'1.0.0','space':'backlog','model_id':'legacy-capabilities','version':VERSION,'records':[r for r in records if re.fullmatch(r'CAP\d+',r['id'])],'note':'Catalogue historique composite ; aucune bijection déduite avec les 36 aptitudes P81.'})
    write(destination/f'release/{VERSION}/manifest.json',{'schema_version':'1.0.0','version':VERSION,'model_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'decisions_path':f'../../decisions/{VERSION}.json','decisions_sha256':hashlib.sha256((destination/f'decisions/{VERSION}.json').read_bytes()).hexdigest(),'input_revision_path':f'../../revisions/{VERSION}/backlog.json','input_revision_sha256':hashlib.sha256((destination/f'revisions/{VERSION}/backlog.json').read_bytes()).hexdigest(),'provenance_path':f'../../provenance/{VERSION}/source-records.json','provenance_sha256':hashlib.sha256((destination/f'provenance/{VERSION}/source-records.json').read_bytes()).hexdigest(),'source_files':basis,'node_count':len(release_nodes),'capability_count':sum(n['kind']=='capability' for n in release_nodes.values()),'complete_capability_count':9,'note':'Compilation technique de décisions existantes ; aucune nouvelle décision métier.'},True)
    return {'backlog_nodes':len(nodes),'backlog_capabilities':36,'release_nodes':len(release_nodes),'release_capabilities':sum(n['kind']=='capability' for n in release_nodes.values()),'decisions':len(decisions)}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination',type=Path,required=True,help='Fresh output directory; never use the live model directory for a re-import.')
    args=parser.parse_args()
    if (args.destination/'release/current.json').exists():
        raise SystemExit('Destination already contains a release; choose a fresh staging directory.')
    print(json.dumps(build(args.destination),ensure_ascii=False))

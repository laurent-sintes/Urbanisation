"""Apply the approved Process / Service naming without changing the graph."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read
from scripts.lifecycle import value_hash

OUT = ROOT / 'modeles/backlog/history/process-services-U409'
NAMES = {
    'D06': 'Process Management',
    'D06.d': 'Process Orchestration',
    'D06.f': 'Process Adaptation Decision',
    'D07.d': 'Operations Tracking',
    'BHV082': 'Process Tracking',
    'D06.b': 'Service Capacity Visibility',
    'D07.a': 'Service Requirements Decision',
    'D06.e': 'Service Selection Decision',
    'D14': 'Service Catalog',
    'D14.a': 'Service Catalog Ingestion',
    'D07.c': 'Service Reconciliation',
}
# These two derived labels were not individually presented for approval.
EDITORIAL = {'D14.a', 'D07.c'}
REFS = ['U407', 'U408', 'U409', 'ELM244', 'CMP155']


def main():
    assert not OUT.exists(), 'Never overwrite historical evidence.'
    path = ROOT / 'modeles/backlog/model.yaml'
    before = read(path)
    model = deepcopy(before)
    old_nodes = {n['id']: n for n in before['nodes']}
    replacements = sorted(((old_nodes[i]['fields']['name'], name) for i, name in NAMES.items()), key=lambda x: -len(x[0]))
    def renamed(text):
        for old, new in replacements:
            text = text.replace(old, new)
        return text

    contributions = [
        ('U407', 'Proposer Process Orchestration', 'J’hésite sur le mot "Execution". Est-ce que ce n’est pas tout simplement Process Orchestration ?', 'Discussion du nom D06.d ; comparaison Camunda, Microsoft et Oracle. Aucun changement de couche ou de périmètre implicite.'),
        ('U408', 'Préférer Process et supprimer Business dans le tracking', 'Je pense qu’on peut supprimer le terme "Business" : on est dans une carto business.\nExecution Adaptation doit devenir Process Adaptation.\n\nFranchement, je pense qu’execution doit être remplacé par process.', 'Orientation de nommage. La réponse distingue Process pour le pilotage, Service pour les prestations et Operations pour les faits suivis ; Decision reste explicite pour D06.f.'),
        ('U409', 'Adopter la convention Process orchestre des Services', 'Le Process orchestre des services : le modèle est simple.\n\nGo', 'Accord sur la convention et les neuf noms présentés : D06, D06.d, D06.f, D07.d, BHV082, D06.b, D07.a, D06.e et D14. D14.a et D07.c reçoivent des intitulés éditoriaux cohérents, sans validation individuelle déduite. Identifiants, responsabilités, comportements, parents et couches conservés ; descriptions explicatives et comparaisons gardent leur portée éditoriale. Pas de généralisation à tous les mots Business ni au comportement Scenario Execution Adaptation d’Inventory Planning. Aucun nouvel audit ni release.'),
    ]
    for ident, title, verbatim, scope in contributions:
        assert f'## {ident}\n' not in (ROOT / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
        append('connaissance/01-contributions-utilisateur.md', f'## {ident}\n\n**id**\n\n{ident}\n\n**date**\n\n2026-09-19\n\n**titre**\n\n{title}\n\n**texte**\n\n{verbatim}\n\n**contexte et portée**\n\n{scope}')
    OUT.mkdir()
    for rel, name in [('modeles/backlog/model.yaml', 'model-before.yaml'), ('modeles/backlog/behavior-gap-audit.yaml', 'audit-before.yaml'), ('modeles/backlog/execution-services-review.yaml', 'review-before.yaml'), ('AGENTS.md', 'AGENTS-before.md')]:
        (OUT / name).write_bytes((ROOT / rel).read_bytes())

    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    explanation = 'Convention U409 : le Process orchestre des Services. Les Tasks expriment les contributions au processus ; les services réalisent les prestations sollicitées, humaines, physiques ou numériques. Un appel informatique est un moyen de sollicitation ou de feedback, pas le service métier lui-même. Process Orchestration coordonne la progression ; Process Adaptation Decision choisit les adaptations ; Operations Tracking rend visibles les opérations et Process Tracking leur contribution à la progression du processus. Les exécutants gardent leurs opérations internes. Le périmètre Supply et les couches du modèle restent inchangés ; aucun moteur de workflow ou nouveau niveau descriptif imposé.'
    comparisons = [dict(
        vendor='Camunda', product='Process Orchestration Handbook, page web courante', element_name='Process orchestration', element_type='Concept et offre logicielle', relationship='Recouvrement partiel',
        similarities='Coordination des tâches manuelles et automatisées, des personnes, systèmes et dispositifs participant au processus.',
        differences='Camunda décrit une plateforme et des mécanismes transverses. FLOW cartographie des responsabilités métier et sépare explicitement décision d’adaptation, orchestration et suivi.',
        flow_position='Le Process orchestre des Services ; Process Orchestration reprend le vocabulaire établi. Les autres intitulés FLOW ne constituent pas une taxonomie Camunda.',
        source_title='Process Orchestration Handbook', source_url='https://camunda.com/process-orchestration/', source_version='Page web consultée le 19 septembre 2026', source_locator='What is process orchestration? ; Processes with diverse endpoints', consulted_on='2026-09-19', evidence_limits='Source primaire effectivement consultée ; présentation éditeur, sans preuve de déploiement Beaumanoir.', status='proposed', source_refs=REFS),
        dict(vendor='Microsoft', product='Dynamics 365 Intelligent Order Management', element_name='Orchestration flows and providers', element_type='Mécanisme produit', relationship='Recouvrement partiel',
        similarities='Parcours de commande coordonné par actions, événements, politiques et communications avec les providers.',
        differences='Le parcours IOM est contextualisé à la commande ; son périmètre produit ne se transpose pas directement au domaine FLOW. Séparer Service et Process ne présume ni provider unique ni cardinalité Task/appel.',
        flow_position='Appui à la distinction entre progression du processus et contributions des services ; aucune taxonomie complète adoptée.', source_title='Intelligent Order Management overview', source_url='https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview', source_version='Documentation web, mise à jour 2026-01-30', source_locator='Providers ; Orchestration', consulted_on='2026-09-19', evidence_limits='Source primaire effectivement consultée ; pas de preuve installée Beaumanoir.', status='proposed', source_refs=REFS)]
    for node in model['nodes']:
        prior = deepcopy(node)
        validated = set(node.get('lifecycle', {}).get('validated_fields', []))
        for key in ('scope', 'finality', 'decomposition_rationale', 'independence', 'mastership'):
            if key in node['fields'] and key not in validated:
                node['fields'][key] = renamed(node['fields'][key])
        # Preserve native vendor names, source titles, dates and historical statements.
        for comp in node['fields'].get('market_comparisons', []):
            if 'flow_position' in comp:
                comp['flow_position'] = renamed(comp['flow_position'])
        if node['id'] in NAMES:
            node['fields']['name'] = NAMES[node['id']]
            if node['id'] not in EDITORIAL:
                life = node.setdefault('lifecycle', {})
                life.update(state='urbanist_validated', recorded_at=stamp, recorded_by='Codex')
                life['validated_fields'] = list(dict.fromkeys(life.get('validated_fields', []) + ['name']))
                life.setdefault('value_sha256', {})['name'] = value_hash(NAMES[node['id']])
                life['source_refs'] = list(dict.fromkeys(life.get('source_refs', []) + ['U409']))
                life['note'] = life.get('note', '') + ' U409 : nouveau nom adopté ; validations des autres champs inchangées, ancien nom et empreintes conservés dans history/process-services-U409.'
            node.setdefault('review', {}).update(state='partial', note='U409 : nom adopté sauf D14.a et D07.c, intitulés dérivés proposés. Autres champs gardent leur qualification propre ; historique capturé avant renommage.')
        if node['id'] in {'D06', 'D06.d', 'D06.f', 'D14', 'D07.d', 'BHV082'}:
            assert 'scope' not in validated
            node['fields']['scope'] += '\n\n' + explanation
        if node['id'] in {'D06', 'D06.d', 'D06.f', 'D14', 'BHV082'}:
            node['fields'].setdefault('market_comparisons', []).extend(deepcopy(comparisons))
        if prior != node:
            node['revision'] += 1
            node['source_refs'] = list(dict.fromkeys(node.get('source_refs', []) + REFS))
    for relation in model['relations']:
        prior = deepcopy(relation)
        # Only refresh narrative references, never endpoints, adoption hashes or topology.
        if 'qualification' not in relation.get('lifecycle', {}).get('validated_fields', []):
            for key in ('meaning', 'conditions', 'effects'):
                if isinstance(relation.get('qualification', {}).get(key), str):
                    relation['qualification'][key] = renamed(relation['qualification'][key])
        if relation != prior:
            relation['revision'] = relation.get('revision', 1) + 1
            relation['source_refs'] = list(dict.fromkeys(relation.get('source_refs', []) + ['U409']))
    save('modeles/backlog/model.yaml', model)
    migration = dict(source_refs=REFS, model_before=(OUT / 'model-before.yaml').relative_to(ROOT).as_posix(), model_before_sha256=sha256((OUT / 'model-before.yaml').read_bytes()).hexdigest(), names=NAMES, adopted_names={i: n for i, n in NAMES.items() if i not in EDITORIAL}, editorial_names={i: NAMES[i] for i in sorted(EDITORIAL)}, delta={})
    for key in ('nodes', 'relations'):
        old = {v['id']: v for v in before[key]}; new = {v['id']: v for v in model[key]}
        assert old.keys() == new.keys()
        migration['delta'][key] = dict(added={}, removed=[], changed={i: value_hash(new[i]) for i in sorted(new) if new[i] != old[i]})
    save((OUT / 'implementation.yaml').relative_to(ROOT), migration)
    review = read(ROOT / 'modeles/backlog/execution-services-review.yaml')
    review['process_services_U409'] = dict(status='integrated', source_refs=REFS, principle='Le Process orchestre des Services.', names=NAMES, adopted_names=migration['adopted_names'], editorial_names=migration['editorial_names'], explanation=explanation, market_comparisons=comparisons, implementation_ref=(OUT / 'implementation.yaml').relative_to(ROOT).as_posix(), historical_note='Les sections datées antérieures conservent noms, accords et preuves historiques. Cette section fixe le nommage courant sans modifier les responsabilités.')
    review['source_refs'] = list(dict.fromkeys(review['source_refs'] + REFS))
    save('modeles/backlog/execution-services-review.yaml', review)
    audit = read(ROOT / 'modeles/backlog/behavior-gap-audit.yaml')
    audit['implementation_U409'] = migration
    audit['baseline']['sha256'] = sha256(path.read_bytes()).hexdigest()
    audit['source_refs'] = list(dict.fromkeys(audit['source_refs'] + REFS))
    for assessment in audit['assessments']:
        for key in ('name', 'diagnosis', 'recommendation'):
            if isinstance(assessment.get(key), str): assessment[key] = renamed(assessment[key])
    save('modeles/backlog/behavior-gap-audit.yaml', audit)
    agents = ROOT / 'AGENTS.md'
    text = renamed(agents.read_text(encoding='utf-8'))
    marker = '| D06 Process Management |'
    assert marker in text
    text = text.replace('**Operations Tracking (U305/U308/U406)**', '**Operations Tracking (U305/U308/U406/U409)**')
    text = text.replace('D14 décrit l’offre des services exécutants', '**Process / Service (U409)** : le Process orchestre des Services. D06 Process Management conserve son périmètre Supply ; Process Orchestration coordonne, Process Adaptation Decision choisit les adaptations. Les prestations relèvent de Service Requirements Decision, Service Selection Decision, Service Capacity Visibility et du référentiel Service Catalog. Operations Tracking porte les trois visibilités physiques et Process Tracking. Les Tasks et appels restent des objets suivis, sans nouveau niveau. D14.a Service Catalog Ingestion et D07.c Service Reconciliation sont des intitulés dérivés proposés ; ne pas étendre la validation. Pas de remplacement lexical global dans les termes éditeurs, les preuves, Business Services ou Scenario Execution Adaptation. Voir `modeles/backlog/execution-services-review.yaml`, `process_services_U409`.\n\nD14 décrit l’offre des services exécutants', 1)
    agents.write_text(text, encoding='utf-8')
    append('marche/elements.md', '### ELM244\n\nProcess Orchestration — Camunda ; orchestration et providers — Microsoft Dynamics 365 IOM. Sources primaires consultées le 19 septembre 2026, passages, URL, éditions et limites dans modeles/backlog/execution-services-review.yaml, process_services_U409.market_comparisons. Coordination de tâches humaines et automatisées chez Camunda ; actions, événements et providers côté Microsoft. Aucun catalogue de capacités universel ni existant Beaumanoir déduit.')
    append('marche/comparaisons.md', '### CMP155\n\nU407–U409 — Le Process orchestre des Services. Process Orchestration possède un appui lexical Camunda ; Microsoft conforte la distinction entre progression du parcours et contributions des providers. FLOW sépare décision d’adaptation, coordination et suivi. Process Management, Operations Tracking et les noms centrés sur Service expriment la cohérence du modèle FLOW, pas un consensus de taxonomie éditeur. Business est supprimé du nom FLOW Process Tracking, sans renommer le produit Azure Business Process Tracking dans les sources. Accord limité aux noms présentés et au principe ; les deux intitulés dérivés D14.a/D07.c et les comparaisons restent proposés. Responsabilités et couches conservées.')
    append('connaissance/32-execution-orchestration.md', '## Convention courante U409 — Process et Service\n\nLe Process orchestre des Services. D06 devient Process Management ; les noms et portées courants sont dans modeles/backlog/execution-services-review.yaml, process_services_U409. Les sections précédentes conservent leur valeur historique. Operations Tracking porte Warehouse Visibility, Transportation Visibility, Store Visibility et Process Tracking. Les noms changent sans ajouter de capacité ou déplacer de responsabilité ; les identifiants restent stables.')
    append('JOURNAL.md', '## 2026-09-19 — U407–U409 : le Process orchestre des Services\n\nConvention et neuf noms présentés adoptés ; deux intitulés dérivés proposés. Références narratives et comparaisons des fiches actualisées, noms natifs éditeurs préservés. Historique des accords capturé, audit existant suivi sans nouvelle étude. Pas de changement de graphe ni de publication.')
    (OUT / 'README.md').write_text('# U409 — Process et Services\n\nLe Process orchestre des Services. Neuf noms adoptés, deux noms dérivés proposés ; voir implementation.yaml. Aucun ajout ou retrait de nœud, de relation ou de comportement. Les validations antérieures et les intitulés sources sont préservés. Aucune release.\n', encoding='utf-8')
    print('U409 integrated: 9 adopted names, 2 editorial labels; unchanged topology.')


if __name__ == '__main__':
    main()

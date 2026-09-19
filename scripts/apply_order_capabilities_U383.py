"""Restore order capabilities and integrate adopted disposition strategies."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-18-orders-disposition-U383'
TYPES = ['D04.i', 'D04.j', 'D04.k', 'D04.l', 'D04.m']


def save(path, data):
    (ROOT / path).write_text(dumps(data), encoding='utf-8')


def append(path, text):
    with (ROOT / path).open('a', encoding='utf-8') as f:
        f.write('\n\n' + text.strip() + '\n')


def main():
    assert not OUT.exists(), 'Do not overwrite the preserved migration.'
    mp = ROOT / 'modeles/backlog/model.yaml'
    before = read(mp)
    m = deepcopy(before)
    n = {x['id']: x for x in m['nodes']}
    assert n['D04.p']['kind'] == 'capability'
    assert all(n[i]['kind'] == 'behavior' for i in TYPES)
    assert not {'BHV048', 'BHV049'} & n.keys()
    cp = ROOT / 'connaissance/01-contributions-utilisateur.md'
    assert '## U383\n' not in cp.read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U383

**id**

U383

**date**

2026-09-18

**titre**

Rétablir les capacités par type d’Order et adopter les stratégies de disposition

**texte**

Ah zut, ça remet en cause mon choix de mettre des types d'order. C'est une erreur, il faut pour chaque type d'order une capacité explicite afin de détailler les comportements. Pour les policies, tes recherches sont fructuantes : tu peux les prendre en compte

**contexte et portée**

Remplace le regroupement U363 sous Order Type : vente, achat, transfert, retour client et retour fournisseur redeviennent cinq capacités explicites, avec leurs identifiants. Lifecycle, Structuring et Archiving restent transverses. Accord pour intégrer les deux stratégies présentées de Return Disposition Decision : Policy-based Disposition et Value Recovery Optimization, avec leurs responsabilités et leur parent. Les prises en charge remise en stock, réparation et renvoi exprimées U382 restent la direction de décomposition de la gestion des retours ; leur rédaction détaillée et leurs frontières ne sont pas validées par extension. Aucun sous-comportement ni nouveau type d’Order. Les compléments éditoriaux, relations détaillées et correspondances marché gardent leur statut propre. Aucune release demandée.''')
    OUT.mkdir()
    for stem in ['model', 'behavior-gap-audit', 'return-disposition-review', 'd04-refactoring', 'order-lifecycle-behaviors', 'refactoring-implementation']:
        (OUT / (stem + '-before.yaml')).write_bytes((ROOT / f'modeles/backlog/{stem}.yaml').read_bytes())
    (OUT / 'AGENTS-before.md').write_bytes((ROOT / 'AGENTS.md').read_bytes())
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    refs = ['U382', 'U383', 'ELM230', 'ELM231', 'CMP141', 'CMP142']

    def life(values, approved=()):
        return dict(state='urbanist_validated' if approved else 'under_instruction', recorded_at=stamp,
                    recorded_by='Codex', source_refs=['U383'], validated_fields=list(approved),
                    value_sha256={f: value_hash(values[f]) for f in approved},
                    note='Accord U383 limité aux champs indiqués ; compléments éditoriaux et comparaisons proposés.')

    def touch(item):
        item['revision'] += 1
        item['source_refs'] = list(dict.fromkeys(item['source_refs'] + ['U383', 'CMP142']))

    old_sentence = 'U363 : variante terminale d’Order Type ; identifiant historique conservé.'
    for ident in TYPES:
        item = n[ident]
        item['kind'] = 'capability'
        item['fields']['nature'] = 'action'
        assert old_sentence in item['fields']['scope']
        item['fields']['scope'] = item['fields']['scope'].replace(old_sentence,
            'U383 : capacité explicite propre au type d’Order, avec son identifiant historique. Les comportements spécifiques peuvent être décrits lorsqu’un mécanisme ou un bénéfice le justifie ; Lifecycle, Structuring et Archiving restent transverses.')
        item['fields']['scope'] = item['fields']['scope'].replace('selon les règles de la variante', 'selon les règles du type d’Order')
        for comparison in item['fields'].get('market_comparisons', []):
            comparison['flow_position'] = ('U383 : capacité explicite par finalité d’Order, pour décrire ses mécanismes propres sans recopier Lifecycle, Structuring ou Archiving. '
                'Choix de maille FLOW ; la structure des modules et types produit ne prescrit pas cette hiérarchie. Correspondance à ce nouveau périmètre à confirmer.')
            comparison['status'] = 'under_review'
            comparison['source_refs'] = list(dict.fromkeys(comparison['source_refs'] + ['U383', 'CMP142']))
        item['review'] = dict(state='partial', note='Capacité par type rétablie U383 ; nom antérieurement adopté conservé. Descriptions et mécanismes futurs qualifiés séparément.')
        touch(item)
    n['D04.l']['fields']['scope'] += ('\n\nDirection U382/U383 : distinguer les prises en charge de remise en stock, réparation et renvoi. '
        'Leur décomposition détaillée est à instruire sous cette capacité redevenue explicite. Elle devra distinguer suivi du retour et de ses suites, décision D05.i, orchestration D06 et écritures de stock D01. '
        'Le renvoi vers un fournisseur mobilise Supplier Return Management ; ne pas dupliquer sa gestion d’Order ni absorber la réalisation physique.')
    n['D04']['fields']['scope'] = ('Cinq capacités explicites par type d’Order : Sales Order Management, Purchase Order Management, Transfer Order Management, Customer Return Management et Supplier Return Management. '
        'Order Lifecycle Management, Order Structuring et Order Archiving restent trois capacités transverses. Les types ne sont plus des comportements d’une capacité générique Order Type. '
        'Chaque capacité peut décrire des comportements propres lorsqu’une complexité ou un bénéfice le justifie, sans recopier les mutations communes ni imposer un cycle universel. '
        'Split transforme les commandes ; Spread répartit des ressources entre commandes et relève des décisions et de Supply Assignment.')
    touch(n['D04'])
    n['D04.o']['fields']['scope'] = n['D04.o']['fields']['scope'].replace('Le contenu spécifique demeure géré selon Order Type.',
        'Le contenu spécifique demeure géré par les capacités de vente, achat, transfert, retour client et retour fournisseur.')
    touch(n['D04.o'])
    m['nodes'] = [x for x in m['nodes'] if x['id'] != 'D04.p']
    removed_relations = ['REL-MEMBER-D04.p', 'REL-NEEDS-U363-D04.q-D04.p']
    m['relations'] = [r for r in m['relations'] if r['id'] not in removed_relations]
    for relation in m['relations']:
        if relation['id'] in ['REL-MEMBER-' + i for i in TYPES]:
            relation['source_id'] = 'D04'
            relation['lifecycle'] = life(relation, ['type', 'source_id', 'target_id'])
            relation['review'] = dict(state='accepted', note='U383 rétablit une capacité par type directement sous D04 ; état U363 préservé dans la capture.')
            touch(relation)
        elif relation['id'] == 'REL-NEEDS-U380-03':
            relation['source_id'] = 'D04.l'
            relation['qualification']['meaning'] = 'A besoin de l’orientation retenue pour préparer et suivre les suites du retour client, en mobilisant les capacités des Orders nécessaires.'
            relation['review'] = dict(state='proposed', note='Source précisée après retrait d’Order Type U383 ; contrat détaillé proposé.')
            touch(relation)
    for ident in TYPES:
        m['relations'].append(dict(id=f'REL-NEEDS-U383-ARCHIVING-{ident}', revision=1, type='relates-to', source_id='D04.q', target_id=ident,
            source_refs=refs, qualification=dict(role='needs', meaning='A besoin du contenu, des versions et des règles de conservation propres aux Orders de ce type.',
            conditions=['Selon les Orders à conserver et les politiques applicables.'], effects=['Conserver les traces sans reprendre leur gestion courante.']),
            review=dict(state='proposed', note='Déclinaison du contrat d’archivage après retrait du regroupement ; détail proposé.'), lifecycle=life({})))

    review_path = 'modeles/backlog/return-disposition-review.yaml'
    review = read(ROOT / review_path)
    analysis = review['behavior_review_U382']
    markets = []
    extra = {
        'Microsoft': ('Dynamics 365 Supply Chain Management', 'Disposition codes and actions', 'Specify how to dispose of returned items'),
        'Blue Yonder': ('Returns Management / Smart Disposition', 'Rules and optimized return disposition', 'Smart Disposition'),
        'Manhattan': ('Active Order Management / Returns Management', 'Dynamic return location', 'Returns Management')}
    for item in analysis['market_comparisons']:
        c = deepcopy(item)
        c['product'], c['element_name'], c['source_title'] = extra[c['vendor']]
        c.update(element_type='Configuration ou mécanisme produit ; pas un catalogue de capacités', relationship='Recouvrement partiel',
            evidence_limits='Page primaire consultée ; correspondance proposée, sans équivalence exacte de nom ou niveau ni preuve de réalisation Beaumanoir.',
            source_refs=refs)
        markets.append(c)
    disposition = n['D05.i']
    disposition['fields']['scope'] = disposition['fields']['scope'].replace(
        '[Order Type](model:D04.p) porte les Orders nécessaires, dont [Customer Return Management](model:D04.l) et [Supplier Return Management](model:D04.m).',
        '[Customer Return Management](model:D04.l) et [Supplier Return Management](model:D04.m) portent leurs Orders respectifs et mobilisent les autres capacités D04 nécessaires aux suites retenues.')
    disposition['fields']['scope'] += ('\n\nDeux stratégies combinables sont adoptées U383 : Policy-based Disposition détermine l’orientation selon une politique établie ; Value Recovery Optimization compare les devenirs autorisés dans le contexte. '
        'Une politique peut borner le choix puis l’optimisation le départager, sans séquence obligatoire ni opposition humain/règles/IA. '
        'Rapidité, circularité et réduction des coûts restent des objectifs ou politiques ; aucun comportement supplémentaire créé pour chaque critère. '
        'Le choix du lieu s’articule avec Stock Redistribution Decision et les décisions d’exécution, sans en transférer les responsabilités.')
    disposition['fields']['decomposition_rationale'] = analysis['proposed_decomposition_rationale']
    disposition['fields']['market_comparisons'] += deepcopy(markets)
    touch(disposition)
    adopted = []
    definitions = [
        'Déterminer l’orientation selon une politique établie, en fonction de l’état du produit, de sa catégorie et des conditions applicables.',
        'Comparer plusieurs devenirs autorisés selon la valeur récupérable, les coûts, les délais et les risques.']
    for index, candidate in enumerate(analysis['candidates']):
        ident = f'BHV{48 + index:03}'
        fields = dict(name=candidate['name'], definition=definitions[index], finality=candidate['benefit'],
            scope=(candidate['example'] + '\n\n' + candidate['boundary'] + '\n\n' + analysis['combination'] +
                   '\n\nLa stratégie détermine une orientation ; elle n’administre pas les politiques, ne réalise pas le traitement et ne modifie pas le stock. '
                   'Les constats d’inspection sont des entrées. Les contraintes obligatoires restent applicables, même si une autre issue paraît plus rentable. '
                   'Libellé FLOW adopté U383 ; aucun catalogue éditeur commun portant ce nom n’est revendiqué. Exemples fictifs, sans preuve de pratique Beaumanoir.'),
            market_comparisons=deepcopy(markets[:2] if index == 0 else markets[1:]))
        node = dict(id=ident, revision=1, kind='behavior', layer='transactional', fields=fields, source_refs=refs,
            source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u383'),
            review=dict(state='partial', note='Nom, responsabilité présentée et rattachement adoptés U383 ; détails éditoriaux et correspondances proposés.'),
            adoption_ids=[], lifecycle=life(fields, ['name', 'definition']))
        m['nodes'].append(node)
        relation = dict(id=f'REL-BEHAVIOR-{ident}', revision=1, type='contains', source_id='D05.i', target_id=ident,
                        source_refs=refs, review=dict(state='accepted', note='Décomposition en stratégies validée U383.'))
        relation['lifecycle'] = life(relation, ['type', 'source_id', 'target_id'])
        m['relations'].append(relation)
        adopted.append(dict(node_id=ident, parent_id='D05.i', adopted_fields=['name', 'definition'], value_sha256=node['lifecycle']['value_sha256']))
    # Preserve every prior adopted field on surviving nodes.
    new_nodes = {x['id']: x for x in m['nodes']}
    for old in before['nodes']:
        if old['id'] not in new_nodes:
            continue
        for field in old.get('lifecycle', {}).get('validated_fields', []):
            assert new_nodes[old['id']]['fields'][field] == old['fields'][field], (old['id'], field)
    assert 'D04.p' not in dumps(m)
    save('modeles/backlog/model.yaml', m)
    migration = dict(source_refs=refs, model_before=(OUT / 'model-before.yaml').relative_to(ROOT).as_posix(),
        model_before_sha256=sha256((OUT / 'model-before.yaml').read_bytes()).hexdigest(), delta={}, behaviors=[],
        restored_capabilities=TYPES, retired_node_ids=['D04.p'], retired_relation_ids=removed_relations,
        domain_children=TYPES + ['D04.n', 'D04.o', 'D04.q'], adopted_strategies=adopted,
        scope='U383 : cinq capacités d’Order rétablies ; deux stratégies de disposition adoptées. Aucun nouveau comportement d’action créé sans description instruite.')
    for key in ['nodes', 'relations']:
        old = {x['id']: x for x in before[key]}; new = {x['id']: x for x in m[key]}
        migration['delta'][key] = dict(added={i: value_hash(new[i]) for i in sorted(new.keys() - old.keys())},
            changed={i: value_hash(new[i]) for i in sorted(new.keys() & old.keys()) if new[i] != old[i]}, removed=sorted(old.keys() - new.keys()))
    (OUT / 'implementation.yaml').write_text(dumps(migration), encoding='utf-8')
    current = dict(source_refs=['U382', 'U383'], capability_ids=migration['domain_children'], restored_capabilities=TYPES,
        retired_ids=['D04.p'], scope='Remplace la structure U363 : une capacité par type ; Lifecycle, Structuring et Archiving transverses. Identifiants stables, aucun quatrième niveau.',
        return_behaviors_direction='Remise en stock, réparation, renvoi : mécanismes demandés U382 ; définitions et rattachements détaillés à instruire, sans absorption des décisions ni de l’exécution physique.')
    for stem in ['d04-refactoring', 'order-lifecycle-behaviors', 'assignment-terminology']:
        path = f'modeles/backlog/{stem}.yaml'; data = read(ROOT / path)
        data['current_U383'] = deepcopy(current)
        data['source_refs'] = list(dict.fromkeys(data.get('source_refs', []) + ['U383']))
        if stem == 'order-lifecycle-behaviors':
            data['status'] = 'order_types_restored_as_capabilities_U383'
        save(path, data)
    review['source_refs'].append('U383')
    review['implementation_U383'] = migration
    review['current_U383'] = dict(node_id='D05.i', behavior_ids=['BHV048', 'BHV049'],
        adopted_fields=['name', 'definition'], status='strategies_integrated',
        structural_issue_resolved='D04.l redevient une capacité ; ses mécanismes de prise en charge restent à détailler séparément des stratégies.')
    save(review_path, review)
    registry = read(ROOT / 'modeles/backlog/refactoring-implementation.yaml')
    registry['retired_ids_never_reuse'].append('D04.p')
    registry['order_capabilities_U383'] = dict(source_refs=['U383'], retired_id='D04.p', successor_ids=TYPES,
        rationale='Retrait du regroupement générique ; succession un-vers-plusieurs, sans redirection arbitraire vers une seule capacité.',
        retired_relation_ids=removed_relations, evidence=(OUT / 'implementation.yaml').relative_to(ROOT).as_posix())
    save('modeles/backlog/refactoring-implementation.yaml', registry)

    ap = 'modeles/backlog/behavior-gap-audit.yaml'; audit = read(ROOT / ap)
    audit['source_refs'] = list(dict.fromkeys(audit['source_refs'] + refs))
    audit['implementation_U383'] = migration
    audit['baseline']['sha256'] = sha256(mp.read_bytes()).hexdigest()
    old_assessments = read(ROOT / 'audits/2026-09-18-d04-U363/behavior-gap-audit-before.yaml')['assessments']
    audit['assessments'] = [x for x in audit['assessments'] if x['capability_id'] != 'D04.p']
    for ident in TYPES:
        old = deepcopy(next(x for x in old_assessments if x['capability_id'] == ident))
        old.update(name=n[ident]['fields']['name'], existing_behaviors=[], verdict='capacité rétablie U383',
            diagnosis='Responsabilité propre au type rétablie pour permettre sa décomposition terminale.',
            recommendation='Décrire les mécanismes propres lorsque justifiés ; ne pas recopier Lifecycle, Structuring ou Archiving.')
        if ident == 'D04.l':
            old['recommendation'] = current['return_behaviors_direction']
        audit['assessments'].append(old)
    a = next(x for x in audit['assessments'] if x['capability_id'] == 'D05.i')
    a.update(existing_behaviors=['BHV048', 'BHV049'], verdict='stratégies intégrées U383',
        diagnosis=analysis['proposed_decomposition_rationale'], recommendation='Conserver stratégies de décision et prises en charge distinctes ; mécanismes combinables, pas de comportement par issue.')
    audit['existing_behavior_review'] = [x for x in audit['existing_behavior_review'] if x['behavior_id'] not in TYPES]
    for entry in adopted:
        audit['existing_behavior_review'].append(dict(behavior_id=entry['node_id'], status='integrated_U383',
            recommendation='Nom, responsabilité et parent adoptés ; stratégie distincte du traitement physique et des effets commerciaux.', market_sources=['S23']))
    for item in audit['candidates']:
        if item['id'] == 'P03':
            item['needs'] = ['D04.j', 'D04.k', 'D04.o', 'D05.a']
    for a in audit['arbitrations']:
        if a['id'] == 'A04':
            a['capabilities'] = ['D04.l', 'D04.m', 'D05.c', 'D06.f', 'D05.i']
            a['status'] = 'decision_strategies_integrated_U383'
            a['recommendation'] = 'D05.i porte les stratégies de devenir ; les capacités de retour D04.l/m sont rétablies. Détailler les prises en charge exprimées U382 en préservant D01/D06.'
        if a['id'] == 'A06':
            a['capabilities'] = ['D04.j', 'D03.n', 'D05.e']
    save(ap, audit)
    sf_path = 'modeles/backlog/supply-fulfillment-audit.yaml'; sf = read(ROOT / sf_path)
    def update_current_targets(obj):
        if isinstance(obj, dict):
            if obj.get('id') == 'SF-A07':
                obj['target_ids'] = ['TER065', 'D04'] + TYPES
            for value in obj.values(): update_current_targets(value)
        elif isinstance(obj, list):
            for value in obj: update_current_targets(value)
    update_current_targets(sf)
    save(sf_path, sf)
    append('marche/elements.md', '''### ELM231

18 septembre 2026 ; U383. Microsoft Dynamics 365 SCM, Purchase order overview, documentation évolutive : introduction et Types of purchase orders, page primaire ouverte. https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-overview . Gestion propre aux achats, suivi des réceptions ; retour fournisseur représenté comme type de commande d’achat dans le produit. Nature : document et processus produit, pas catalogue normatif de capacités.

Microsoft Disposition codes/action et Blue Yonder Smart Disposition, ELM229/ELM230, relus sur pages primaires. Configuration des orientations et optimisation du devenir ; limites et différences dans les fiches. Aucune réalisation Beaumanoir déduite.''')
    append('marche/comparaisons.md', '''## CMP142

Codex ; 18 septembre 2026 ; U383 ; ELM229–ELM231 ; backlog D04.i–m et D05.i/BHV048–049. Statut : correspondances proposées ; structure et stratégies adoptées séparément.

Une capacité par type d’Order est justifiée par la maille terminale FLOW : chaque responsabilité peut décrire ses mécanismes sans sous-comportement. Microsoft documente des processus propres aux achats et aux retours, mais traite le retour fournisseur comme type d’achat ; les cinq capacités FLOW ne sont donc pas un découpage universel des produits. Les correspondances héritées des cinq variantes sont marquées à réexaminer après changement de maille. Order Type D04.p est retiré, identifiant non réutilisable ; Lifecycle, Structuring et Archiving restent transverses.

Policy-based Disposition et Value Recovery Optimization sont intégrés sous D05.i. Blue Yonder documente règles, orientation contextuelle et récupération de valeur ; Microsoft fournit le vocabulaire de disposition. Nos noms et la séparation décision/application ne sont pas un catalogue natif partagé. Les limites commerciales et financières des offres, ainsi que l’absence de preuve algorithmique ou de réalisation Beaumanoir, restent explicites dans les fiches. Direction remise en stock/réparation/renvoi conservée pour l’instruction des comportements d’action, sans les importer comme codes produit ni modifier implicitement D01/D06.''')
    (OUT / 'README.md').write_text('''# Capacités d’Order et stratégies de disposition — U383

Les cinq capacités D04.i–m sont rétablies directement sous D04. Order Type D04.p est retiré du catalogue actif, avec preuve et interdiction de réutiliser son identifiant. Lifecycle, Structuring et Archiving conservent leurs responsabilités. Les liens d’archivage sont distribués vers les capacités explicites ; le besoin de disposition du retour cible Customer Return Management.

Return Disposition Decision porte Policy-based Disposition (BHV048) et Value Recovery Optimization (BHV049). Noms, responsabilités présentées et rattachements sont adoptés. Les justifications de décomposition, descriptions développées et comparaisons marché sont documentées sans adoption globale implicite. Les champs déjà adoptés des autres nœuds sont préservés.

Les prises en charge remise en stock, réparation et renvoi sont une direction acquise U382 ; leur définition détaillée reste à instruire sous les capacités restaurées, en distinguant Orders, décision, prestations et stocks. Aucun quatrième niveau, aucune duplication des mutations communes.

Backlog uniquement ; aucune publication. Capture préalable et delta dans ce dossier.
''', encoding='utf-8')
    print('U383 applied: five Order capabilities restored; BHV048/BHV049 integrated; D04.p retired.')


if __name__ == '__main__':
    main()

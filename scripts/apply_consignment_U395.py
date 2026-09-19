"""Integrate the two approved consignment responsibilities, without behaviors."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

OUT = ROOT / 'audits/2026-09-18-consignment-U395'


def main():
    assert not OUT.exists(), 'Preserve the recorded migration.'
    mp = ROOT / 'modeles/backlog/model.yaml'
    before = read(mp)
    m = deepcopy(before)
    assert not {'D01.h', 'D04.r'} & {n['id'] for n in m['nodes']}
    assert '## U395\n' not in (ROOT / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U395

**id**

U395

**date**

2026-09-18

**titre**

Adopter les deux capacités de consignation et leurs frontières

**texte**

Je valide

**contexte et portée**

Accord sur la proposition présentée après la parenthèse historique SAP/Microsoft : Consignment Replenishment Order dans D04 et Consigned Inventory Management dans D01, leurs noms et responsabilités présentées. La première demande et suit l’apport fournisseur sans engagement d’achat des marchandises ; la seconde applique au stock les conditions de l’accord et mobilise les capacités responsables des suites autorisées. Agreement fournit les conditions ; D05 décide des besoins d’implantation ou de réassort ; D04 porte les demandes ; D01 applique le régime et enregistre les évolutions ; D06 orchestre les prestations. Exemple présenté : 500 pièces pour une implantation, fin de la demande d’apport distincte de fin de la consignation. Replenishment dans le nom Microsoft inclut le premier apport sans fusionner Initial Stocking et Replenishment Decision. Aucun comportement proposé à cette étape. Descriptions développées, contrats de dépendance et comparaisons gardent leur qualification éditoriale. Aucune release demandée.''')
    OUT.mkdir()
    paths = ['model', 'consignment-inventory-review', 'nonpurchase-supply-order-review', 'order-intent-principles', 'behavior-gap-audit']
    for stem in paths:
        (OUT / (stem + '-before.yaml')).write_bytes((ROOT / f'modeles/backlog/{stem}.yaml').read_bytes())
    (OUT / 'AGENTS-before.md').write_bytes((ROOT / 'AGENTS.md').read_bytes())
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    refs = ['U391', 'U392', 'U393', 'U394', 'U395', 'ELM236', 'ELM237', 'CMP147', 'CMP148', 'CMP149']

    def life(values, approved=()):
        return dict(state='urbanist_validated' if approved else 'under_instruction', recorded_at=stamp,
            recorded_by='Codex', source_refs=['U395'], validated_fields=list(approved),
            value_sha256={f: value_hash(values[f]) for f in approved},
            note='U395 : noms, responsabilités et rattachements adoptés ; précisions éditoriales et contrats détaillés qualifiés séparément. Aucun comportement.')

    ci = read(ROOT / 'modeles/backlog/consignment-inventory-review.yaml')
    np = read(ROOT / 'modeles/backlog/nonpurchase-supply-order-review.yaml')

    def comparison(source, position):
        return dict(vendor=source['vendor'], product=source['product'], element_name=source['title'],
            element_type='Processus, document ou fonction produit', relationship='Recouvrement partiel',
            similarities=source['finding'], differences=source['limit'], source_title=source['title'],
            source_url=source['url'], source_version=source['edition'], source_locator=source['locator'],
            consulted_on=source['consulted_on'], evidence_limits=source['access'] + ' ; aucune preuve de déploiement Beaumanoir.',
            flow_position=position, status='proposed', source_refs=refs)

    shared = ('[Agreement](model:D11) fournit les conditions applicables, y compris celles de l’offre de stockage. '
        '[Inventory Optimization](model:D05) décide des besoins d’implantation ou de réassort ; '
        '[Order Management](model:D04) porte les demandes correspondantes ; '
        '[Inventory Management](model:D01) applique le régime du stock et enregistre ses évolutions ; '
        '[Execution Management](model:D06) orchestre les prestations physiques et numériques.')
    example = ('Exemple fictif présenté et adopté : une demande porte sur 500 pièces pour une implantation. '
        'Les réceptions satisfont progressivement la demande d’apport. Les pièces restent ensuite gérées sous l’accord de consignation : '
        'vente autorisée, éventuel transfert de propriété, échéance de reprise. La fin de la demande ne met pas fin à la gestion de la consignation. '
        'Cet exemple ne décrit pas une pratique installée prouvée chez Beaumanoir.')
    definitions = {
        'D04.r': 'Demander et suivre un apport fournisseur : produits, quantités, destinations, dates et reste à recevoir, sans engagement d’achat des marchandises.',
        'D01.h': 'Appliquer au stock consigné les conditions de l’accord : propriété, droits d’usage, échéances et suites autorisées ; mobiliser les capacités responsables lorsqu’une acquisition, un retour ou une autre issue devient nécessaire.',
    }
    specs = [
        ('D04.r', 'D04', 'Consignment Replenishment Order',
         'Disposer d’un apport fournisseur attendu et traçable, distinct de l’acquisition des marchandises.',
         'La capacité suit la demande sous accord de consignation, ses quantités attendues et le reste à recevoir. '
         'La réception conserve la propriété fournisseur selon l’accord. Le stock reçu relève ensuite de [Consigned Inventory Management](model:D01.h). '
         'Le terme Replenishment de Microsoft couvre ici l’alimentation du stock consigné, y compris le premier apport ; '
         '[Initial Stocking Decision](model:D05.g) et [Replenishment Decision](model:D05.e) restent distinctes. '
         'Les mutations, la structuration et l’archivage mobilisent les capacités transverses D04. '
         '[Purchase Order](model:D04.j) conserve l’acte d’achat éventuel ; aucun achat fictif, réservation ou disponibilité de stock non reçu ne découle de cette demande.',
         np, ['NP-S1', 'NP-S2', 'NP-S3']),
        ('D01.h', 'D01', 'Consigned Inventory Management',
         'Respecter les droits et obligations sur le stock fournisseur détenu, pendant sa présence dans le réseau et lors de ses suites.',
         'La cible initiale concerne le fournisseur propriétaire et le distributeur détenteur. '
         'La capacité applique les conditions référencées d’Agreement ; elle ne négocie pas le contrat et n’administre pas son maître. '
         'Détention, propriété, droit d’usage, responsabilité et rémunération du stockage sont distincts. '
         '[Inventory Tracking](model:D01.f) et [Record Inventory Movements](model:D01.g) conservent les états et mouvements. '
         '[Consignment Replenishment Order](model:D04.r) porte la demande d’apport ; [Purchase Order](model:D04.j), '
         '[Supplier Return](model:D04.m) ou les autres Orders pertinents portent les suites retenues. '
         'Les faits utiles sont transmis à la comptabilité, la facturation et l’assurance sans absorber leurs responsabilités. '
         'Les issues autorisées après saison ne se confondent ni avec la décision du devenir ni avec sa réalisation. '
         'Location rémunérée, transfert de propriété à chaque vente et droit de destruction ne sont pas des règles universelles déduites de la consignation.',
         ci, ['CI-S2', 'CI-S3', 'CI-S5', 'CI-S6']),
    ]
    adoptions = []
    for ident, parent, name, finality, scope, review, source_ids in specs:
        sources = {s['id']: s for s in review['sources']}
        fields = dict(name=name, definition=definitions[ident], nature='management', finality=finality,
            scope=scope + '\n\n' + shared + '\n\n' + example,
            market_comparisons=[comparison(sources[s],
                'U395 adopte la responsabilité FLOW et son parent ; le rapprochement produit/capacité reste partiel. '
                'Les conditions contractuelles FLOW et les comportements ne sont pas déduits automatiquement du produit.') for s in source_ids])
        node = dict(id=ident, revision=1, kind='capability', layer='transactional', fields=fields, source_refs=refs,
            source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u395'),
            review=dict(state='partial', note='Nom, définition et rattachement adoptés U395 ; nature technique management, finalité développée, scope et comparaisons éditoriaux.'),
            adoption_ids=[], lifecycle=life(fields, ['name', 'definition']))
        m['nodes'].append(node)
        rel = dict(id='REL-MEMBER-' + ident, revision=1, type='contains', source_id=parent, target_id=ident,
            source_refs=refs, review=dict(state='accepted', note='Rattachement explicitement adopté U395.'))
        rel['lifecycle'] = life(rel, ['type', 'source_id', 'target_id'])
        m['relations'].append(rel)
        adoptions.append(dict(node_id=ident, parent_id=parent, adopted_fields=['name', 'definition'], value_sha256=node['lifecycle']['value_sha256']))
    nodes = {n['id']: n for n in m['nodes']}
    for ident in ['D01', 'D04']:
        node = nodes[ident]
        assert 'scope' not in node['lifecycle']['validated_fields']
        if ident == 'D01':
            node['fields']['scope'] += '\n\n[Consigned Inventory Management](model:D01.h) applique les conditions du stock consigné ; la demande d’apport relève de D04. Frontière adoptée U395.'
        else:
            node['fields']['scope'] = node['fields']['scope'].replace('Cinq capacités explicites', 'Six capacités explicites').replace(
                'Customer Return et Supplier Return.', 'Customer Return, Supplier Return et Consignment Replenishment Order.', 1)
        node['revision'] += 1
        node['source_refs'].append('U395')
    # Detailed links are editorial interpretations of the adopted boundaries.
    dependencies = [
        ('D01.h', 'D11.a', 'A besoin des conditions de l’accord ingérées depuis le maître externe pour appliquer au stock les droits, obligations et échéances.'),
        ('D04.r', 'D11.a', 'A besoin des conditions de l’accord ingérées depuis le maître externe pour formuler et suivre la demande d’apport consigné.'),
        ('D04.r', 'D05.g', 'A besoin du besoin d’implantation retenu lorsque la demande correspond à un premier apport.'),
        ('D04.r', 'D05.e', 'A besoin du besoin de réassort retenu lorsque la demande correspond à une alimentation continue.'),
    ]
    for idx, (source, target, meaning) in enumerate(dependencies, 1):
        m['relations'].append(dict(id=f'REL-NEEDS-U395-{idx:02d}', revision=1, type='relates-to',
            source_id=source, target_id=target, source_refs=refs,
            qualification=dict(role='needs', meaning=meaning, conditions=['Selon le cas et les conditions applicables ; aucun appel systématique imposé.'],
                effects=['Consommer le résultat ou les conditions sans transférer la responsabilité de leur fournisseur.']),
            review=dict(state='under_review', note='Frontières adoptées U395 ; contrat détaillé éditorial.'), lifecycle=life({})))
    save('modeles/backlog/model.yaml', m)
    migration = dict(source_refs=['U395'], model_before=(OUT / 'model-before.yaml').relative_to(ROOT).as_posix(),
        model_before_sha256=sha256((OUT / 'model-before.yaml').read_bytes()).hexdigest(), delta={}, adopted_capabilities=adoptions, behaviors=[])
    for key in ['nodes', 'relations']:
        old = {x['id']: x for x in before[key]}; new = {x['id']: x for x in m[key]}
        migration['delta'][key] = dict(added={i: value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
            changed={i: value_hash(new[i]) for i in sorted(old.keys() & new.keys()) if old[i] != new[i]}, removed=sorted(old.keys()-new.keys()))
    save((OUT / 'implementation.yaml').relative_to(ROOT), migration)
    for stem, data, ident, key in [('consignment-inventory-review', ci, 'D01.h', 'candidate'),
                                 ('nonpurchase-supply-order-review', np, 'D04.r', 'recommendation')]:
        data['status'] = 'integrated_U395'
        data['source_refs'].append('U395')
        data[key]['status'] = 'name_definition_parent_adopted_U395'
        data[key]['definition'] = definitions[ident]
        data['catalog_changed'] = True
        data['current_U395'] = dict(node_id=ident, adopted_fields=['name', 'definition'], behaviors='not_decomposed',
            evidence='audits/2026-09-18-consignment-U395/implementation.yaml',
            remaining='Comportements à instruire avec bénéfice ou complexité démontrés ; contrats détaillés éditoriaux.')
        data['architecture_U393']['status'] = 'principle_recorded_names_subsequently_adopted_U395'
        data['market_comparisons'][0]['flow_position'] = (
            'U395 intègre D01.h Consigned Inventory Management et D04.r Consignment Replenishment Order, '
            'leurs noms, responsabilités présentées et parents. Aucun comportement créé ; correspondance marché partielle, '
            'distincte de la validation des capacités FLOW.')
        save(f'modeles/backlog/{stem}.yaml', data)
    principle = read(ROOT / 'modeles/backlog/order-intent-principles.yaml')
    principle['source_refs'].append('U395')
    principle['review']['editorial_scope'] = 'Principe U393/U394 conservé ; deux noms, responsabilités et parents adoptés U395. Autres compléments éditoriaux et comportements non adoptés par extension.'
    principle['architecture_boundaries'][-1] = 'Purchase Order reste distinct ; Consigned Inventory Management (D01.h) et Consignment Replenishment Order (D04.r) adoptés U395, sans comportement supplémentaire.'
    principle['catalog_changed'] = True
    principle['implementation_U395'] = 'audits/2026-09-18-consignment-U395/implementation.yaml'
    save('modeles/backlog/order-intent-principles.yaml', principle)
    audit = read(ROOT / 'modeles/backlog/behavior-gap-audit.yaml')
    audit['source_refs'].append('U395')
    audit['implementation_U395'] = migration
    audit['baseline']['sha256'] = sha256(mp.read_bytes()).hexdigest()
    for item in adoptions:
        node = nodes[item['node_id']]
        audit['assessments'].append(dict(capability_id=node['id'], name=node['fields']['name'], existing_behaviors=[], verdict='conserver',
            diagnosis='Responsabilité et parent adoptés U395 ; aucune décomposition présentée.',
            recommendation='Instruire les comportements selon U265/U389 ; comparaisons Microsoft/SAP/Oracle dans la fiche et les annexes de consignation.',
            market_sources=[], candidate_ids=[]))
    purchase = next(a for a in audit['assessments'] if a['capability_id'] == 'D04.j')
    purchase['recommendation'] = 'Stock, livraison directe et prestations ; consignation distinguée dans D01.h et D04.r depuis U395, sans quatrième comportement Purchase Order.'
    save('modeles/backlog/behavior-gap-audit.yaml', audit)
    agents = ROOT / 'AGENTS.md'
    text = agents.read_text(encoding='utf-8')
    text = text.replace('Nom et découpage de cette capacité restent proposés dans `modeles/backlog/consignment-inventory-review.yaml`.',
        'U395 adopte **Consigned Inventory Management** (D01.h) et **Consignment Replenishment Order** (D04.r), leurs responsabilités et parents ; comportements à instruire. Agreement fournit les conditions, D05 les besoins, D04 les demandes, D01 le régime et les états, D06 les prestations. Annexes : `consignment-inventory-review.yaml` et `nonpurchase-supply-order-review.yaml`.')
    text = text.replace('cinq capacités explicites de vente, achat, transfert, retour client et retour fournisseur (D04.i–m),',
        'cinq capacités explicites de vente, achat, transfert, retour client et retour fournisseur (D04.i–m), complétées U395 par Consignment Replenishment Order (D04.r),')
    agents.write_text(text, encoding='utf-8')
    append('JOURNAL.md', '''## 2026-09-18 — U395 : deux capacités de consignation adoptées

Consigned Inventory Management D01.h et Consignment Replenishment Order D04.r intégrées au backlog, avec noms, définitions présentées et parents validés. Comparaisons Microsoft/SAP/Oracle dans les fiches ; frontières, exemple des 500 pièces et sens large de Replenishment documentés. Quatre dépendances détaillées restent éditoriales. Aucun comportement ajouté. Annexes, instructions et audit courant alignés ; preuve et capture dans audits/2026-09-18-consignment-U395. Aucune release.''')
    (OUT / 'README.md').write_text('# Consignation — U395\n\nDeux capacités adoptées : D01.h Consigned Inventory Management et D04.r Consignment Replenishment Order. Noms, définitions présentées et rattachements validés ; descriptions développées et comparaisons éditoriales. Aucun comportement ajouté.\n\nCaptures antérieures et empreintes : implementation.yaml. Les quatre dépendances détaillées restent en instruction. Backlog uniquement.\n', encoding='utf-8')
    print('U395 integrated: two capabilities, two adopted parents, four editorial dependencies, no behaviors.')


if __name__ == '__main__':
    main()

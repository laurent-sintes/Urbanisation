"""Integrate the Customer Return behaviors approved after U384."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-18-customer-return-U385'


def save(path, value):
    (ROOT / path).write_text(dumps(value), encoding='utf-8')


def append(path, text):
    with (ROOT / path).open('a', encoding='utf-8') as f:
        f.write('\n\n' + text.strip() + '\n')


def main():
    assert not OUT.exists(), 'Preserve the existing migration.'
    mp = ROOT / 'modeles/backlog/model.yaml'; before = read(mp); m = deepcopy(before)
    rp = 'modeles/backlog/customer-return-behaviors.yaml'; review = read(ROOT / rp)
    assert review['status'] == 'proposed'
    identifiers = [f'BHV{i:03}' for i in range(50, 55)]
    assert not set(identifiers) & {n['id'] for n in m['nodes']}
    cp = ROOT / 'connaissance/01-contributions-utilisateur.md'
    assert '## U385\n' not in cp.read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U385

**id**

U385

**date**

2026-09-18

**titre**

Adopter les cinq comportements de Customer Return

**texte**

Je valide

**contexte et portée**

Accord sur la proposition U384 : définition élargie de Customer Return, cinq comportements Return to Stock, Repair and Refurbishment, Return to Supplier, Return to Customer et Scrapping, leurs responsabilités présentées et leur rattachement sous D04.l. Parcours combinables ; renvoi fournisseur par relais à Supplier Return, restitution du même bien distincte d’un remplacement, décision et réalisation distinctes. Le bénéfice du découpage est acquis ; sa formulation détaillée et les nouveaux contrats restent éditoriaux. Les correspondances marché conservent leur qualification propre. Remplacement client, règlement sans retour, donation, recyclage et revente secondaire restent des axes à instruire, sans adoption ni création automatique. Aucune release demandée.''')
    OUT.mkdir()
    for name in ['model', 'customer-return-behaviors', 'behavior-gap-audit']:
        (OUT / (name + '-before.yaml')).write_bytes((ROOT / f'modeles/backlog/{name}.yaml').read_bytes())
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    refs = ['U382', 'U384', 'U385', 'ELM232', 'CMP143']
    def life(values, approved=()):
        return dict(state='urbanist_validated' if approved else 'under_instruction', recorded_at=stamp,
            recorded_by='Codex', source_refs=['U385'], validated_fields=list(approved),
            value_sha256={f: value_hash(values[f]) for f in approved},
            note='U385 : noms, responsabilités présentées et rattachements adoptés ; descriptions développées, contrats et comparaisons qualifiés séparément.')
    parent = next(n for n in m['nodes'] if n['id'] == 'D04.l')
    parent['fields']['definition'] = review['proposed_definition']
    parent['fields']['finality'] = 'Connaître le retour client attendu, suivre ses suites logistiques et expliquer le résultat obtenu pour chaque produit ou quantité.'
    parent['fields']['decomposition_rationale'] = review['decomposition_rationale']
    parent['fields']['scope'] = ('La capacité couvre les commandes de retour et leurs suites logistiques selon les décisions et autorisations applicables. '
        'Le libellé Customer Return désigne une capacité d’action ; [Customer Return Order](glossary:TER072) reste l’objet métier associé.\n\n'
        + ' '.join(review['shared_functions']) + '\n\n'
        'Les cinq comportements adoptés U385 sont des parcours métier combinables : Return to Stock, Repair and Refurbishment, Return to Supplier, Return to Customer et Scrapping. '
        'Une réparation peut précéder remise en stock ou restitution au client. Les différents produits ou quantités d’un même retour peuvent suivre des parcours différents, sans créer un quatrième niveau.\n\n'
        '[Return Disposition Decision](model:D05.i) choisit le devenir. Customer Return prépare et suit sa prise en charge via les capacités responsables : '
        '[Supplier Return](model:D04.m) porte l’Order fournisseur, [Execution Management](model:D06) coordonne les prestations et en trace les résultats, '
        '[Inventory Management](model:D01) enregistre mouvements et états. La réception physique et la réparation restent chez les exécutants. '
        'Décider, solliciter une prestation et constater sa réalisation ne se confondent pas ; reçu, accepté et disponible sont des situations distinctes.\n\n'
        '[Order Lifecycle Management](model:D04.o) gouverne les mutations, [Order Structuring](model:D04.n) les compositions et [Order Archiving](model:D04.q) la conservation historique. '
        'Ces fonctions communes ne sont pas recopiées sous chaque comportement. L’Order de retour n’efface pas la vente d’origine.\n\n'
        'Exemple fictif : sur dix pièces attendues, six sont reçues et quatre restent attendues. Parmi les six reçues, certaines peuvent être remises en stock et d’autres nécessiter une réparation. '
        'Conserver origine, motif, quantités, décisions applicables et preuves de résultat ; aucune réception ou remise en disponibilité ne se déduit du seul état de la commande.\n\n'
        'L’autorisation commerciale du retour, le remboursement et le remplacement client restent à délimiter. Restituer le bien n’est pas envoyer un autre produit ; '
        'un règlement sans retour physique ne crée aucune réception fictive. Donation, recyclage et revente secondaire ne sont pas assimilés au rebut. '
        'Les règles détaillées, le porteur des décisions commerciales et ces autres axes restent à instruire. Aucun déploiement Beaumanoir présumé.')
    parent['fields']['market_comparisons'] = deepcopy(review['market_comparisons'])
    for c in parent['fields']['market_comparisons']:
        c['source_refs'].append('U385')
        c['flow_position'] += ' U385 adopte les parcours sous Customer Return ; correspondance marché proposée distincte de cet accord.'
    parent['lifecycle']['validated_fields'] = list(dict.fromkeys(parent['lifecycle']['validated_fields'] + ['definition']))
    parent['lifecycle']['value_sha256']['definition'] = value_hash(parent['fields']['definition'])
    parent['lifecycle']['source_refs'].append('U385')
    parent['lifecycle']['recorded_at'] = stamp
    parent['lifecycle']['note'] = 'Nom adopté U384 conservé ; définition élargie et décomposition adoptées U385. Détails éditoriaux qualifiés séparément.'
    parent['review'] = dict(state='partial', note='Nom, définition et cinq comportements adoptés ; scope développé et comparaisons proposés dans leur formulation détaillée.')
    parent['revision'] += 1; parent['source_refs'].append('U385')
    # Use the responsibility sentences actually presented in the conversation.
    definitions = [
        'Prendre en charge la remise en disponibilité du produit.',
        'Prendre en charge une remise en état, suivre son résultat et la suite attendue.',
        'Relier le retour client à sa prise en charge par Supplier Return.',
        'Prendre en charge la restitution du produit au client, après réparation ou décision de non-reprise.',
        'Prendre en charge la mise au rebut retenue : conserver l’autorisation, suivre la réalisation et rapprocher la preuve avec la sortie de stock.']
    adoptions = []
    for ident, proposal, definition in zip(identifiers, review['proposals'], definitions):
        comparisons = deepcopy(review['market_comparisons'])
        for c, term in zip(comparisons, proposal['market_terms']):
            c['element_name'] = term
            c['similarities'] = f'Appui au parcours {proposal["name"]} : {term}.'
            c['flow_position'] = proposal['boundary'] + ' Parcours adopté U385 ; correspondance proposée, pas une équivalence de niveau.'
            c['source_refs'].append('U385')
        fields = dict(name=proposal['name'], definition=definition, finality=proposal['benefit'],
            scope=(proposal['mechanism'] + '\n\nExemple fictif : ' + proposal['example'] + '\n\n' + proposal['boundary'] + '\n\n'
                'Ce comportement appartient à [Customer Return](model:D04.l). Il peut se combiner avec les autres parcours du retour selon le produit ou la quantité. '
                'Le choix du devenir est porté par [Return Disposition Decision](model:D05.i). Les preuves de résultat proviennent des responsabilités opérationnelles compétentes. '
                'Aucune inspection, écriture de stock, prestation physique ou décision de remboursement absorbée ; aucun logiciel ni traitement manuel imposé.'),
            market_comparisons=comparisons)
        node = dict(id=ident, revision=1, kind='behavior', layer=parent['layer'], fields=fields, source_refs=refs,
            source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u385'), adoption_ids=[],
            review=dict(state='partial', note='Nom, responsabilité présentée et parent adoptés U385 ; précisions rédactionnelles et comparaisons proposées.'),
            lifecycle=life(fields, ['name', 'definition']))
        m['nodes'].append(node)
        r = dict(id=f'REL-BEHAVIOR-{ident}', revision=1, type='contains', source_id='D04.l', target_id=ident,
                 source_refs=refs, review=dict(state='accepted', note='Parent et décomposition explicitement adoptés U385.'))
        r['lifecycle'] = life(r, ['type', 'source_id', 'target_id']); m['relations'].append(r)
        adoptions.append(dict(node_id=ident, parent_id='D04.l', adopted_fields=['name', 'definition'], value_sha256=node['lifecycle']['value_sha256']))
        proposal.update(status='integrated_U385', node_id=ident)
        proposal['source_refs'].append('U385')
    # Make the supplier relay explicit without copying the Supplier Return capability.
    m['relations'].append(dict(id='REL-NEEDS-U385-SUPPLIER-RETURN', revision=1, type='relates-to', source_id='BHV052', target_id='D04.m',
        source_refs=refs, qualification=dict(role='needs', meaning='A besoin de la prise en charge de l’Order de retour fournisseur et de ses résultats pour suivre la suite du retour client.',
            conditions=['Lorsque le devenir retenu et les autorisations applicables prévoient un renvoi fournisseur.'],
            effects=['Préserver les liens et quantités entre retours sans créer une seconde responsabilité de gestion de la commande fournisseur.']),
        review=dict(state='proposed', note='Principe de relais acquis ; contrat détaillé proposé.'), lifecycle=life({})))
    save('modeles/backlog/model.yaml', m)
    migration = dict(source_refs=refs, model_before=(OUT / 'model-before.yaml').relative_to(ROOT).as_posix(),
        model_before_sha256=sha256((OUT / 'model-before.yaml').read_bytes()).hexdigest(), delta={}, behaviors=[],
        adopted_behaviors=adoptions, capability_id='D04.l', adopted_definition=parent['fields']['definition'],
        definition_sha256=value_hash(parent['fields']['definition']),
        scope='U385 : définition élargie et cinq parcours combinables adoptés ; descriptions et contrat de relais qualifiés séparément.')
    for key in ['nodes', 'relations']:
        old = {x['id']:x for x in before[key]}; new = {x['id']:x for x in m[key]}
        migration['delta'][key] = dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
            changed={i:value_hash(new[i]) for i in sorted(new.keys() & old.keys()) if new[i]!=old[i]}, removed=sorted(old.keys()-new.keys()))
    (OUT / 'implementation.yaml').write_text(dumps(migration), encoding='utf-8')
    review.update(status='integrated_U385', definition_status='adopted_and_applied_U385', rationale_status='principle_adopted_editorial_wording_U385', implementation_U385=migration,
        naming_convention='Noms des capacités adoptés U384 ; cinq noms de comportements, responsabilités présentées et définition élargie adoptés U385. Les correspondances et précisions éditoriales gardent leurs statuts.')
    review['renvoi_clarification'] = 'Fournisseur et client sont distingués par leur contrepartie, obligation et preuve finale ; les deux comportements précisant le renvoi U382 sont adoptés U385.'
    review['source_refs'].append('U385'); save(rp, review)
    current = dict(source_refs=['U385'], capability_id='D04.l', behavior_ids=identifiers, status='integrated',
                   review_path=rp, remaining='Remplacement client, règlement sans retour et autres filières à instruire ; contrats détaillés proposés.')
    for stem in ['d04-refactoring', 'order-lifecycle-behaviors', 'return-disposition-review']:
        path=f'modeles/backlog/{stem}.yaml'; doc=read(ROOT/path); doc['customer_return_U385']=current; save(path,doc)
    ap='modeles/backlog/behavior-gap-audit.yaml'; audit=read(ROOT/ap)
    audit['source_refs'].append('U385'); audit['implementation_U385']=migration
    audit['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest()
    assessment=next(a for a in audit['assessments'] if a['capability_id']=='D04.l')
    assessment.update(existing_behaviors=identifiers, verdict='parcours intégrés U385', diagnosis=review['decomposition_rationale'],
        recommendation='Préserver parcours combinables et frontières décision/exécution/stocks. Remplacement client et règlement sans retour restent des axes distincts à instruire.')
    for ident in identifiers:
        audit['existing_behavior_review'].append(dict(behavior_id=ident, status='integrated_U385', market_sources=['S23'],
            recommendation='Nom, responsabilité et parent adoptés ; pas de sous-comportement, de décision de disposition dupliquée ni de réalisation physique absorbée.'))
    arbitration=next(a for a in audit['arbitrations'] if a['id']=='A04')
    arbitration.update(status='logistical_paths_integrated_U385', recommendation='D05.i choisit le devenir ; Customer Return porte cinq prises en charge, avec relais vers Supplier Return. D06 conserve prestations et D01 stocks.',
        limit='Autorisation commerciale, remboursement, remplacement et règlement sans retour restent à attribuer. La liste des parcours n’est pas une preuve d’exhaustivité de toutes les filières.')
    save(ap,audit)
    append('marche/comparaisons.md', '''### Intégration CMP143 — U385

La définition élargie de Customer Return et les cinq parcours proposés U384 sont adoptés et intégrés sous BHV050–BHV054. Les correspondances SAP/Microsoft, leurs écarts et limites sont portés par la capacité et chaque comportement, avec statut proposé distinct de l’accord métier. Return to Supplier mobilise Supplier Return sans dupliquer sa responsabilité. Les nouvelles descriptions détaillées et le contrat formalisé de relais restent éditoriaux. Les autres axes commerciaux ou filières ne sont pas intégrés par extension. Preuve : audits/2026-09-18-customer-return-U385/implementation.yaml.''')
    (OUT/'README.md').write_text('''# Customer Return — adoption U385

Définition élargie de D04.l appliquée. Cinq comportements terminaux et combinables : BHV050 Return to Stock, BHV051 Repair and Refurbishment, BHV052 Return to Supplier, BHV053 Return to Customer et BHV054 Scrapping.

Noms, responsabilités présentées et parents adoptés. La justification de décomposition, les exemples, les frontières et les comparaisons sont intégrés ; les précisions éditoriales et le contrat Supplier Return gardent un statut propre. Les captures préservent le modèle et l’étude U384.

Remplacement client, règlement sans retour, donation, recyclage et revente secondaire restent à instruire. Aucune publication, aucun commit ni push.
''',encoding='utf-8')
    print('U385: Customer Return definition and BHV050–BHV054 integrated.')


if __name__ == '__main__':
    main()

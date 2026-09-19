"""Apply the scoped Return Disposition Decision agreement, retaining evidence."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-18-return-disposition-U380'


def save(path, data):
    (ROOT / path).write_text(dumps(data), encoding='utf-8')


def main():
    assert not OUT.exists(), 'Recorded migration must not be overwritten.'
    mp = ROOT / 'modeles/backlog/model.yaml'
    before = read(mp); m = deepcopy(before)
    assert not any(n['id'] == 'D05.i' for n in m['nodes'])
    review = read(ROOT / 'modeles/backlog/return-disposition-review.yaml')
    proposal = review['proposal']
    refs = ['U379', 'U380', 'ELM229', 'CMP140']
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    def cycle(values, fields):
        return dict(state='urbanist_validated' if fields else 'under_instruction',
                    recorded_at=stamp, recorded_by='Codex', source_refs=['U380'],
                    validated_fields=fields, value_sha256={f:value_hash(values[f]) for f in fields},
                    note='U380 : accord limité aux champs indiqués ; contrats détaillés et compléments éditoriaux proposés.')

    cp = ROOT / 'connaissance/01-contributions-utilisateur.md'
    text = cp.read_text(encoding='utf-8')
    assert '## U380\n' not in text
    text += '''\n\n## U380

**id**

U380

**date**

2026-09-18

**titre**

Adopter Return Disposition Decision dans Inventory Optimization

**texte**

Je valide

**contexte et portée**

Accord sur la proposition présentée après U379 : nom Return Disposition Decision, définition du devenir logistique selon état constaté, politiques et récupération de valeur, nature décision et rattachement à D05 Inventory Optimization. Inspection par l’exécutant, choix de devenir, Orders D04, orchestration D06 et enregistrement des mouvements/états D01 restent distincts. Autorisation commerciale du retour, remboursement et remplacement client ne sont pas absorbés. Aucun comportement supplémentaire. Les nouveaux contrats détaillés, exemples développés et correspondances marché gardent leur statut éditorial propre ; aucune publication demandée.
'''
    cp.write_text(text, encoding='utf-8')
    OUT.mkdir()
    (OUT / 'model-before.yaml').write_bytes(mp.read_bytes())
    (OUT / 'review-before.yaml').write_text(dumps(review), encoding='utf-8')
    fields = dict(name=proposal['name'], definition=proposal['definition'], nature='decision',
        finality='Retenir une orientation pertinente pour récupérer la valeur des produits retournés et maîtriser leurs coûts et risques.',
        scope=('La décision produit une orientation logistique et ses conditions : remise en stock utilisable, réparation ou reconditionnement, renvoi fournisseur ou sortie définitive selon les filières autorisées. '
               'Le motif du retour explique son origine ; il ne détermine pas à lui seul le devenir du produit.\n\n'
               'L’inspection fournit les faits sur l’état du bien. La décision mobilise ces constats, les politiques applicables et les possibilités de récupération de valeur ; elle ne réalise pas l’inspection physique. '
               'Lorsque les informations sont insuffisantes, expliciter les conditions restant à vérifier sans rendre implicitement le produit disponible. '
               'Le lieu de réalisation de cette décision peut être un système ou un exécutant externe ; la capacité ne prescrit ni organisation ni développement interne.\n\n'
               '[Order Type](model:D04.p) porte les Orders nécessaires, dont [Customer Return Management](model:D04.l) et [Supplier Return Management](model:D04.m). '
               '[Execution Management](model:D06) coordonne et suit les prestations ; [Inventory Management](model:D01) enregistre les mouvements et états résultants. '
               'Décider une remise en stock ne prouve pas son exécution et ne réalise pas l’écriture transactionnelle. '
               '[Stock Redistribution Decision](model:D05.c) conserve le choix des déplacements de stock existant entre sites.\n\n'
               'L’autorisation commerciale du retour, le remboursement et le remplacement client restent distincts du devenir logistique du bien retourné. '
               'Une orientation vers le fournisseur ne vaut ni accord commercial de reprise ni avoir financier. '
               'Les seuils de coût, règles d’acceptation et filières admissibles sont des politiques ; aucun code de disposition, écran ou action produit ne devient automatiquement un comportement.\n\n'
               'Exemple fictif : huit pièces sont constatées revendables et deux nécessitent une remise en état. La décision détermine si cette remise en état est pertinente et autorisée, puis oriente les lots. '
               'Les capacités opérationnelles organisent et enregistrent la réalisation. Cet exemple ne prouve aucune pratique installée chez Beaumanoir.'))
    fields['market_comparisons'] = deepcopy(review['market_comparisons'])
    for comparison in fields['market_comparisons']:
        comparison['source_refs'].append('U380')
        comparison['flow_position'] = ('U380 intègre la décision de devenir logistique dans D05, distincte de l’inspection, des Orders, de l’exécution et des suites financières. '
                                       'Correspondance proposée ; les codes et activités produit ne sont pas des comportements FLOW.')
    node = dict(id='D05.i', revision=1, kind='capability', layer='transactional', fields=fields,
                source_refs=refs, source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u380'),
                review=dict(state='partial', note='Nom, définition, nature et rattachement D05 adoptés U380 ; compléments éditoriaux et contrats détaillés proposés.'),
                adoption_ids=[], lifecycle=cycle(fields, ['name', 'definition', 'nature']))
    m['nodes'].append(node)
    parent = dict(id='REL-MEMBER-D05.i', revision=1, type='contains', source_id='D05', target_id='D05.i', source_refs=refs,
                  review=dict(state='accepted', note='Rattachement à Inventory Optimization présenté U379 et validé U380.'))
    parent['lifecycle'] = cycle(parent, ['type', 'source_id', 'target_id'])
    m['relations'].append(parent)
    nodes = {n['id']:n for n in m['nodes']}
    domain = nodes['D05']
    domain['fields']['scope'] += ('\n\n[Return Disposition Decision](model:D05.i) détermine le devenir logistique des produits retournés selon leur état, les politiques et la récupération de valeur. '
                                'Inspection, décision et réalisation restent distinctes ; aucun remboursement ou remplacement client absorbé. Rattachement adopté U380.')
    returned = nodes['D04.l']
    old = 'Autorisation commerciale de reprise, remboursement, remplacement et décision sur le sort des biens restent à délimiter ; réception physique et contrôle par l’exécutant ne sont pas réalisés par cette capacité.'
    assert old in returned['fields']['scope']
    returned['fields']['scope'] = returned['fields']['scope'].replace(old,
        'Autorisation commerciale de reprise, remboursement et remplacement client restent à délimiter. '
        '[Return Disposition Decision](model:D05.i) détermine le devenir logistique du bien ; réception physique et contrôle restent réalisés par l’exécutant.')
    for n in [domain, returned]:
        assert 'scope' not in n['lifecycle']['validated_fields']
        n['revision'] += 1
        n['source_refs'] = list(dict.fromkeys(n['source_refs'] + ['U380']))
    dependencies = [
        ('D05.i', 'D07.d', 'A besoin des constats et résultats d’inspection remontés par les exécutants pour déterminer le devenir du produit.'),
        ('D05.i', 'D01.c', 'A besoin de l’état connu et de la disponibilité du stock retourné pour contextualiser ses orientations.'),
        ('D04.p', 'D05.i', 'A besoin de l’orientation retenue lorsqu’elle détermine le contenu d’un Order de suite du retour.'),
        ('D06.d', 'D05.i', 'A besoin de l’orientation retenue et de ses conditions pour coordonner les prestations logistiques de suite du retour.'),
    ]
    for index, (source, target, meaning) in enumerate(dependencies, 1):
        m['relations'].append(dict(id=f'REL-NEEDS-U380-{index:02d}', revision=1, type='relates-to', source_id=source, target_id=target,
            source_refs=refs, qualification=dict(role='needs', meaning=meaning,
                conditions=['Selon le cas de retour et les informations disponibles ; aucune séquence ou invocation systématique imposée.'],
                effects=['Résultat consommé sans transférer la responsabilité du fournisseur ; décision et réalisation distinguées.'],
                scope='Dépendance métier proposée ; contrats précis non adoptés globalement.'),
            review=dict(state='under_review', note='Frontières acquises U380 ; qualification détaillée proposée.'), lifecycle=cycle({}, [])))
    save('modeles/backlog/model.yaml', m)
    migration = dict(source_refs=refs, model_before=(OUT / 'model-before.yaml').relative_to(ROOT).as_posix(),
                     model_before_sha256=sha256((OUT / 'model-before.yaml').read_bytes()).hexdigest(), delta={}, behaviors=[],
                     node_id=node['id'], adopted_fields=['name','definition','nature'], value_sha256=node['lifecycle']['value_sha256'],
                     parent_id='D05', parent_relation_id=parent['id'])
    for key in ['nodes', 'relations']:
        old = {x['id']:x for x in before[key]}; new = {x['id']:x for x in m[key]}
        migration['delta'][key] = dict(added={i:value_hash(new[i]) for i in new.keys()-old.keys()},
            changed={i:value_hash(new[i]) for i in old.keys() & new.keys() if old[i] != new[i]}, removed=sorted(old.keys()-new.keys()))
    (OUT / 'implementation.yaml').write_text(dumps(migration), encoding='utf-8')
    review['status'] = 'integrated_U380'
    review['source_refs'].append('U380')
    review['implementation_U380'] = migration
    review['current_U380'] = dict(node_id='D05.i', parent_id='D05', adopted_fields=['name','definition','nature'],
        adopted_parent_fields=['type','source_id','target_id'], no_behavior=True,
        remaining='Contrats précis, exemples développés et comparaisons qualifiés séparément ; règles non bloquantes pour le catalogue.')
    save('modeles/backlog/return-disposition-review.yaml', review)
    audit = read(ROOT / 'modeles/backlog/behavior-gap-audit.yaml')
    audit['source_refs'].append('U380'); audit['implementation_U380'] = migration
    audit['baseline']['sha256'] = sha256(mp.read_bytes()).hexdigest()
    audit['assessments'].append(dict(capability_id='D05.i', name=fields['name'], existing_behaviors=[], verdict='conserver',
        diagnosis='Décision de devenir logistique adoptée U380 ; aucune décomposition démontrée.',
        recommendation='Conserver décision, inspection, exécution et suites commerciales distinctes ; aucun comportement par code produit.',
        market_sources=['S23'], candidate_ids=[]))
    arbitration = next(x for x in audit['arbitrations'] if x['id'] == 'A04')
    arbitration.update(status='logistical_responsibility_resolved_U380',
        recommendation='Return Disposition Decision D05.i porte le devenir logistique ; D04 conserve les Orders, D06 les prestations et D01 les stocks.',
        limit='L’autorisation commerciale, le remboursement et le remplacement client restent distincts, non attribués par cet accord. Les contrats précis gardent leur statut proposé.')
    arbitration['capabilities'].append('D05.i')
    save('modeles/backlog/behavior-gap-audit.yaml', audit)
    d05 = read(ROOT / 'modeles/backlog/d05-refactoring.yaml')
    d05['source_refs'].append('U380')
    d05['return_disposition_U380'] = dict(node_id='D05.i', name=fields['name'], status='name_definition_nature_parent_adopted',
        review_path='modeles/backlog/return-disposition-review.yaml', boundary='Décider le devenir logistique ; aucun remboursement ni réalisation physique repris.')
    save('modeles/backlog/d05-refactoring.yaml', d05)
    (OUT / 'README.md').write_text('''# Return Disposition Decision — U380

D05.i est intégrée dans Inventory Optimization. Nom, définition et nature décision sont adoptés ; le rattachement D05 est validé. Inspection, devenir logistique, gestion des Orders, réalisation et enregistrement des stocks restent distincts. Autorisation commerciale, remboursement et remplacement client ne sont pas absorbés.

Aucun comportement créé. Finalité rédigée, détails de description, quatre contrats de dépendance et correspondances marché restent qualifiés séparément. Les comparaisons Microsoft Disposition et SAP Logistical Follow-Up Activities sont dans la fiche.

L’audit A04 est résolu sur le devenir logistique ; ses questions commerciales ne sont pas déclarées résolues. Le scope D05 et la frontière du retour client sont mis en cohérence sans modifier leurs champs déjà adoptés. Preuves : model-before.yaml et implementation.yaml.

Backlog uniquement ; aucune publication, aucun commit ni push.
''', encoding='utf-8')
    print('U380: capability D05.i and adopted D05 parent integrated; no behavior created.')


if __name__ == '__main__':
    main()

"""Apply the two Supplier Return behaviors approved after U386."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-18-supplier-return-U387'


def save(path, data):
    (ROOT / path).write_text(dumps(data), encoding='utf-8')


def append(path, text):
    with (ROOT / path).open('a', encoding='utf-8') as f:
        f.write('\n\n' + text.strip() + '\n')


def main():
    assert not OUT.exists(), 'Do not overwrite the migration evidence.'
    mp = ROOT / 'modeles/backlog/model.yaml'; before = read(mp); m = deepcopy(before)
    rp = 'modeles/backlog/supplier-return-behaviors.yaml'; review = read(ROOT / rp)
    assert review['status'] == 'proposed'
    ids = ['BHV055', 'BHV056']
    assert not set(ids) & {n['id'] for n in m['nodes']}
    assert '## U387\n' not in (ROOT / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U387

**id**

U387

**date**

2026-09-18

**titre**

Adopter Return for Credit et Return for Replacement

**texte**

Je valide

**contexte et portée**

Accord sur la recommandation U386 : deux comportements sous Supplier Return, Return for Credit (sans remplacement attendu) et Return for Replacement (apport attendu conservé), leurs noms, responsabilités présentées et rattachements. Purchase Order porte l’apport de remplacement sans imposer une nouvelle commande ou une réouverture de l’existante. La finance conserve le règlement ; les deux parcours peuvent coexister sur des quantités différentes. Return for Repair demeure conditionnel et non créé. Définition élargie du parent et précisions rédactionnelles non présentées intégralement restent éditoriales ; les comparaisons et contrats détaillés gardent leur qualification propre. Aucune publication demandée.''')
    OUT.mkdir()
    for stem in ['model', 'supplier-return-behaviors', 'behavior-gap-audit']:
        (OUT / (stem + '-before.yaml')).write_bytes((ROOT / f'modeles/backlog/{stem}.yaml').read_bytes())
    refs = ['U386', 'U387', 'ELM233', 'CMP144']
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    def life(values, approved=()):
        return dict(state='urbanist_validated' if approved else 'under_instruction', recorded_at=stamp,
            recorded_by='Codex', source_refs=['U387'], validated_fields=list(approved),
            value_sha256={f: value_hash(values[f]) for f in approved},
            note='U387 : noms, responsabilités présentées et parents adoptés ; descriptions développées, contrats et correspondances qualifiés séparément.')
    parent = next(n for n in m['nodes'] if n['id'] == 'D04.m')
    assert 'definition' not in parent['lifecycle']['validated_fields']
    parent['fields']['definition'] = review['proposed_definition']
    parent['fields']['decomposition_rationale'] = review['decomposition_rationale']
    parent['fields']['scope'] = ('Supplier Return porte les commandes de renvoi aux fournisseurs et le suivi de leurs suites attendues. '
        'Le libellé désigne une capacité d’action ; [Supplier Return Order](glossary:TER073) reste l’objet métier associé.\n\n'
        'Deux comportements combinables sont adoptés U387. Return for Credit ne prévoit pas de remplacement pour les quantités reprises. '
        'Return for Replacement conserve un apport attendu et le lien entre le sortant et le remplacement. '
        + review['combination'] + '\n\n' + ' '.join(review['shared_functions']) + '\n\n'
        '[Purchase Order](model:D04.j) porte l’apport de remplacement : commande liée ou adaptation de l’attendu existant selon les règles applicables, sans choix documentaire imposé. '
        'Ne pas compter deux fois le remplacement dans les ressources futures. Les confirmations, dates et réceptions restent des faits distincts ; leur usage par la promesse mobilise les capacités responsables.\n\n'
        'L’accord de reprise est consommé ; sa négociation et le règlement financier ne sont pas absorbés. Supplier Return peut référencer l’avoir ou son état communiqué, '
        'sans l’émettre, le comptabiliser ni le rapprocher. Expédition, réception fournisseur, acceptation et règlement restent distincts. '
        '[Execution Management](model:D06) conserve prestations et suivi ; [Inventory Management](model:D01) enregistre mouvements et états. '
        'Lifecycle, Structuring et Archiving conservent leurs responsabilités communes.\n\n'
        'Le retour peut provenir d’un [Customer Return](model:D04.l), d’une réception fournisseur ou du stock, sans créer un comportement par origine ou motif. '
        'Défaut, erreur de livraison, excédent et fin de saison ne suffisent pas seuls à justifier un nouveau parcours. '
        'Return for Credit côté fournisseur prévoit un renvoi ; ne pas le confondre avec Credit only côté client, qui peut ne comporter aucun flux physique.\n\n'
        'Exemple fictif : sur 100 pièces reprises, 60 sont traitées sans remplacement et 40 doivent être remplacées. Suivre les quantités de chaque parcours et les apports réellement attendus. '
        'Aucun avoir ou remplacement ne se déduit du seul statut de l’Order.\n\n'
        'Return for Repair reste à instruire : reprise au titre d’une obligation du fournisseur et achat de prestation à un réparateur ne sont pas automatiquement la même responsabilité. '
        'Aucun troisième comportement, service de réparation ou schéma comptable ajouté par extension. Les exemples ne prouvent aucune pratique Beaumanoir.')
    parent['fields']['market_comparisons'] = deepcopy(review['market_comparisons'][:3])
    for c in parent['fields']['market_comparisons']:
        c['source_refs'].append('U387')
        c['flow_position'] = 'U387 adopte deux parcours distingués par l’attendu de marchandises. Les choix documentaires éditeurs et les opérations financières restent distincts ; correspondance proposée.'
    parent['revision'] += 1
    parent['source_refs'] = list(dict.fromkeys(parent['source_refs'] + refs))
    parent['review'] = dict(state='partial', note='Nom court antérieurement adopté ; deux comportements adoptés U387. Définition élargie et descriptions développées éditoriales.')
    definitions = [review['proposals'][0]['definition'],
        'Prendre en charge un retour associé à un remplacement attendu, en conservant les liens entre marchandises renvoyées et apports de remplacement.']
    adoptions = []
    for ident, p, definition in zip(ids, review['proposals'], definitions):
        comparisons = deepcopy(parent['fields']['market_comparisons'] if ident == 'BHV055' else parent['fields']['market_comparisons'][:2])
        for c in comparisons:
            c['flow_position'] = p['boundary'] + ' Correspondance proposée, distincte de la validation du comportement FLOW.'
        fields = dict(name=p['name'], definition=definition, finality=p['benefit'],
            scope=(p['mechanism'] + '\n\n' + p['example'] + '\n\n' + p['boundary'] + '\n\n'
                + review['combination'] + '\n\n'
                'Ce parcours relève de [Supplier Return](model:D04.m). Les mutations des Orders, la composition et l’archivage restent transverses. '
                'D06 conserve l’exécution et D01 les écritures de stock. Les décisions et autorisations applicables sont consommées sans négociation ou réalisation physique implicite. '
                'Aucun produit logiciel, statut technique ou séquence obligatoire imposé ; les règles de contrat détaillées restent à préciser.'),
            market_comparisons=comparisons)
        node = dict(id=ident, revision=1, kind='behavior', layer=parent['layer'], fields=fields, source_refs=refs,
            source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u387'), adoption_ids=[],
            review=dict(state='partial', note='Nom, responsabilité présentée et parent adoptés U387 ; précisions et comparaisons proposées.'), lifecycle=life(fields, ['name','definition']))
        m['nodes'].append(node)
        r = dict(id=f'REL-BEHAVIOR-{ident}', revision=1, type='contains', source_id='D04.m', target_id=ident,
            source_refs=refs, review=dict(state='accepted', note='Rattachement explicite adopté U387.'))
        r['lifecycle'] = life(r, ['type','source_id','target_id']); m['relations'].append(r)
        adoptions.append(dict(node_id=ident, parent_id='D04.m', adopted_fields=['name','definition'], value_sha256=node['lifecycle']['value_sha256']))
        p.update(status='integrated_U387', node_id=ident)
    m['relations'].append(dict(id='REL-NEEDS-U387-REPLACEMENT-PURCHASE', revision=1, type='relates-to', source_id='BHV056', target_id='D04.j',
        source_refs=refs, qualification=dict(role='needs', meaning='A besoin de l’apport de remplacement porté par Purchase Order, de ses quantités, dates et résultats pour suivre le remplacement restant attendu.',
            conditions=['Lorsque l’accord applicable prévoit un remplacement de marchandises.'],
            effects=['Relier le renvoi et l’apport sans les compter deux fois, sans imposer une nouvelle commande ni modifier automatiquement les promesses.']),
        review=dict(state='proposed', note='Responsabilité Purchase Order acquise ; formalisation détaillée du contrat proposée.'), lifecycle=life({})))
    save('modeles/backlog/model.yaml', m)
    migration = dict(source_refs=refs, model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),
        model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(), delta={}, behaviors=[], adopted_behaviors=adoptions,
        capability_id='D04.m', scope='Deux parcours adoptés ; définition élargie du parent éditoriale ; Return for Repair non créé.')
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]}; new={x['id']:x for x in m[key]}
        migration['delta'][key]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
            changed={i:value_hash(new[i]) for i in sorted(new.keys()&old.keys()) if new[i]!=old[i]}, removed=sorted(old.keys()-new.keys()))
    (OUT/'implementation.yaml').write_text(dumps(migration),encoding='utf-8')
    review.update(status='integrated_U387', definition_status='applied_editorial_not_adopted', rationale_status='principle_adopted_editorial_wording', implementation_U387=migration)
    review['source_refs'].append('U387'); save(rp,review)
    current=dict(source_refs=['U387'], capability_id='D04.m', behavior_ids=ids, status='integrated', review_path=rp, remaining='Return for Repair reste conditionnel ; contrats détaillés proposés.')
    for stem in ['d04-refactoring','order-lifecycle-behaviors']:
        path=f'modeles/backlog/{stem}.yaml'; doc=read(ROOT/path); doc['supplier_return_U387']=current; save(path,doc)
    ap='modeles/backlog/behavior-gap-audit.yaml'; audit=read(ROOT/ap)
    audit['source_refs'].append('U387'); audit['implementation_U387']=migration; audit['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest()
    assessment=next(a for a in audit['assessments'] if a['capability_id']=='D04.m')
    assessment.update(existing_behaviors=ids, verdict='parcours intégrés U387', diagnosis=review['decomposition_rationale'],
        recommendation='Conserver attendu de remplacement distinct de l’avoir ; Purchase Order porte l’apport. Return for Repair reste à instruire.')
    for ident in ids:
        audit['existing_behavior_review'].append(dict(behavior_id=ident, status='integrated_U387', market_sources=['S27'], recommendation='Nom, responsabilité et parent adoptés ; correspondances détaillées dans la fiche. Aucun règlement financier ou troisième parcours absorbé.'))
    save(ap,audit)
    append('marche/comparaisons.md', '''### Intégration CMP144 — U387

Return for Credit (BHV055) et Return for Replacement (BHV056) sont adoptés sous Supplier Return. La distinction porte sur l’apport de remplacement attendu ; finance, négociation, exécution et stock restent distincts. Les comparaisons Microsoft Business Central, SAP ByDesign et Oracle Fusion Cloud sont présentes dans les fiches avec leurs versions, différences et limites. Correspondances proposées, sans assimilation des produits ou des niveaux. La formalisation de la dépendance à Purchase Order est proposée ; la responsabilité de l’apport est acquise. Return for Repair demeure conditionnel et non créé. Définition élargie du parent éditoriale. Preuve : audits/2026-09-18-supplier-return-U387/implementation.yaml.''')
    (OUT/'README.md').write_text('''# Supplier Return — U387

BHV055 Return for Credit et BHV056 Return for Replacement intégrés sous D04.m. Noms, responsabilités présentées et parents adoptés ; la description élargie du parent, les précisions et les correspondances gardent leurs portées propres. La justification de décomposition distingue absence et maintien d’un apport de remplacement.

Purchase Order porte l’apport ; le contrat détaillé est proposé. Le règlement financier n’est pas absorbé. Les deux parcours peuvent se combiner par quantités ; Return for Repair reste à instruire. Captures et delta préservent le modèle antérieur. Backlog uniquement, aucune publication.
''',encoding='utf-8')
    print('U387: BHV055 and BHV056 integrated; Return for Repair remains conditional.')


if __name__ == '__main__':
    main()

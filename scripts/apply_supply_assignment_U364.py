"""Integrate the scoped U364 distinction, retaining historical evidence."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

from scripts.lifecycle import value_hash
from scripts.structured_io import read, dumps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'audits/2026-09-18-supply-assignment-U364'


def append(path, text):
    with (ROOT/path).open('a', encoding='utf-8') as f:
        f.write('\n\n'+text.strip()+'\n')


def main():
    assert not OUT.exists(), 'U364 already integrated.'
    mp = ROOT/'modeles/backlog/model.yaml'
    ap = ROOT/'modeles/backlog/behavior-gap-audit.yaml'
    rp = ROOT/'modeles/backlog/supply-assignment-mechanisms-review.yaml'
    m, audit, review = read(mp), read(ap), read(rp)
    nodes = {n['id']: n for n in m['nodes']}
    assert not {'BHV045', 'BHV046', 'BHV047'} & nodes.keys()
    assert '## U364\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    OUT.mkdir()
    for path in [mp, ap, rp]:
        (OUT/(path.stem+'-before.yaml')).write_bytes(path.read_bytes())
    append('connaissance/01-contributions-utilisateur.md', '''## U364

**id**

U364

**date**

2026-09-18

**titre**

Rendre visible la distinction entre complément et réaffectation

**texte**

Oui je veux rendre visible cette distinction

**contexte et portée**

Réponse à la proposition de trois comportements sous Supply Assignment : application d’un plan (principe déjà acquis U345), complément préservant les affectations existantes, réaffectation des ressources modifiables. Accord explicite sur la distinction stabilité/adaptation et sa visibilité dans le modèle. Les deux définitions présentées sont conservées à l’identique et leur rattachement est retenu ; noms anglais utilisés comme libellés proposés, exemples développés, comparaisons et contrats non validés globalement. Aucune réoptimisation implicite dans la capacité d’action, aucun algorithme de recalcul partiel imposé, aucune publication demandée.''')
    before = deepcopy(m)
    refs = ['U364', 'CMP134']
    now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    def life(values, fields=()):
        return dict(state='urbanist_validated' if fields else 'under_instruction', recorded_at=now,
                    recorded_by='Codex', source_refs=['U364'], validated_fields=list(fields),
                    value_sha256={f: value_hash(values[f]) for f in fields},
                    note='Distinction et rattachements U364 ; libellés et détails éditoriaux sans validation globale.')

    microsoft = deepcopy(next(c for c in review['clarifications_U346_U347']['market_comparisons']
                              if c['element_name']=='Keep supply for confirmed demand'))
    microsoft['flow_position'] = ('Appui à la stabilité des affectations, mais périmètre produit plus large incluant la chaîne '
                                 'de planification. Ne démontre pas une équivalence exacte avec Incremental Supply Assignment.')
    specifications = [
        ('BHV045', 'Supply Assignment Plan Application',
         'Appliquer les affectations d’un plan retenu, en contrôlant qu’elles restent applicables et en signalant les écarts.',
         'Rendre opérationnels les choix retenus sans leur substituer silencieusement un autre plan.',
         'Le plan affecte 60 pièces présentes et 40 attendues à une commande. Si une ressource manque, expliquer l’écart sans substituer silencieusement un autre plan.', []),
        ('BHV046', 'Incremental Supply Assignment',
         'Compléter les besoins non affectés tout en préservant les affectations existantes.',
         'Favoriser la stabilité des affectations et des pratiques de préparation tout en satisfaisant de nouveaux besoins ou reliquats.',
         'Sur 100 pièces demandées, conserver les 70 déjà affectées et rechercher les 30 restantes.', ['definition']),
        ('BHV047', 'Supply Reassignment',
         'Réviser les affectations modifiables pour appliquer de nouveaux arbitrages entre commandes.',
         'Permettre l’adaptation collective aux changements de ressources, de priorités et de demandes, dans les marges autorisées.',
         'Après le retard d’un arrivage, modifier les ressources affectées à plusieurs commandes en respectant leurs protections.', ['definition']),
    ]
    common = ('Les décisions spécialisées choisissent les affectations ; Supply Assignment matérialise leurs résultats. '
              'Une affectation ne confirme pas seule une promesse et ne réserve pas implicitement le stock. '
              'Respecter les restrictions applicables de [Order Freezing](model:BHV037), les réservations et les engagements. '
              'Modifier le contenu, l’état ou la structure d’un Order mobilise les responsabilités D04 ; D06 conserve l’exécution. '
              'API, batch, écran, unité et masse restent des modalités, sans comportement supplémentaire. '
              'Les exemples sont fictifs ; les règles d’exception et contrats détaillés restent à éprouver.')
    specific = [
        'Un plan peut prescrire un complément avec préservation ou une réaffectation : les trois comportements sont combinables, sans séquence imposée. '
        'Restituer les écarts entre les affectations prévues et appliquées ; un écart peut appeler une nouvelle décision. '
        'Aucune transaction atomique de tout le plan ou validation humaine systématique n’est imposée.',
        'Préserver l’existant est la politique de ce traitement ; cela ne crée pas un gel durable de chaque Order. '
        'Ce mécanisme vise le reliquat, sans promettre une stratégie technique de recalcul incrémental, RETE ou traitement par API. '
        'Si une affectation conservée devient irréalisable, rendre l’exception visible ; sa révision relève d’un arbitrage et du mécanisme de réaffectation. '
        'La préservation ne garantit pas la présence physique de la ressource.',
        'La réaffectation peut modifier les ressources associées, y compris entre plusieurs commandes, dans le périmètre révisable. '
        'Elle n’autorise pas à dégrader une promesse protégée ni à lever silencieusement une réservation ou un gel. '
        'Elle peut préserver une partie des liens existants ; aucune suppression et reconstruction complète n’est imposée par FLOW. '
        'Spread est une politique de répartition qui alimente les décisions ; ce comportement applique leurs résultats sans devenir un optimiseur concurrent.',
    ]
    adopted = []
    for index, (identifier, name, definition, finality, example, approved) in enumerate(specifications):
        proposal = review['mechanisms'][index]
        comparisons = deepcopy(proposal['market_comparisons'])
        if index == 1:
            comparisons.append(deepcopy(microsoft))
        for c in comparisons:
            c['source_refs'] = list(dict.fromkeys(c['source_refs']+refs))
            c['consulted_on'] = '2026-09-18'
            c['flow_position'] += (' U364 : trois mécanismes sous Supply Assignment, avec distinction explicite entre '
                                   'complément conservant les liens et réaffectation des liens révisables. '
                                   'Les décisions et Order Freezing gardent leurs responsabilités. Correspondance proposée.')
        fields = dict(name=name, definition=definition, finality=finality,
                      scope='Exemple fictif : '+example+'\n\n'+specific[index]+'\n\n'+common,
                      market_comparisons=comparisons)
        if index == 1:
            fields['scope'] += '\n\nNommage : libellé descriptif FLOW ; pas de terme unifié du marché démontré.'
        if index == 2:
            fields['scope'] += '\n\nNommage : Reassignment reprend le terme SAP. Le périmètre FLOW sépare la décision de sa mise en application.'
        m['nodes'].append(dict(id=identifier, revision=1, kind='behavior', layer='transactional', fields=fields,
                              source_refs=list(dict.fromkeys(proposal.get('source_refs', [])+['U345']+refs)),
                              source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u364'),
                              adoption_ids=[], review=dict(state='partial', note='Principes et rattachement acquis ; noms et compléments éditoriaux proposés.'),
                              lifecycle=life(fields, approved)))
        rel = dict(id='REL-BEHAVIOR-'+identifier, revision=1, type='contains', source_id='D02.e', target_id=identifier,
                   source_refs=['U345', 'U364'], review=dict(state='accepted', note='Décomposition visible de Supply Assignment, U364.'))
        rel['lifecycle'] = life(rel, ['type', 'source_id', 'target_id'])
        m['relations'].append(rel)
        adopted.append(dict(node_id=identifier, parent_id='D02.e', adopted_fields=approved,
                            value_sha256={f:value_hash(fields[f]) for f in approved},
                            principle=proposal['definition'] if index==0 else definition,
                            principle_sha256=value_hash(proposal['definition'] if index==0 else definition),
                            source_refs=['U345'] if index==0 else ['U364']))
        proposal['current_U364'] = dict(node_id=identifier, name=name, principle_status='adopted', wording_status='proposed_name_and_details',
                                        definition=definition, parent_id='D02.e', source_refs=refs)
    parent = nodes['D02.e']
    parent['revision'] += 1
    parent['source_refs'] = list(dict.fromkeys(parent['source_refs']+refs))
    parent['fields']['decomposition_rationale'] = ('Trois mécanismes combinables apportent des bénéfices distincts : application traçable '
        'd’un plan retenu, stabilité en complétant sans remettre en jeu les liens existants, adaptation collective en révisant les liens autorisés. '
        'Le choix de préserver ou réviser change les pratiques de préparation et les engagements à coordonner ; il ne se réduit pas à une opération CRUD '
        'ou une optimisation technique de calcul. L’application d’un plan peut mobiliser l’une ou l’autre politique.')
    parent['fields']['scope'] += ('\n\nU364 : [Supply Assignment Plan Application](model:BHV045) matérialise un plan retenu ; '
        '[Incremental Supply Assignment](model:BHV046) complète les besoins non affectés en conservant l’existant ; '
        '[Supply Reassignment](model:BHV047) applique une révision des affectations modifiables. '
        'Ces comportements sont combinables. Préservation pendant un traitement et gel durable sont distincts ; '
        'aucun algorithme incrémental imposé. La décision collective et les contrats d’engagement restent à préciser dans A01/A02.')
    parent['fields']['market_comparisons'].append(microsoft)
    mp.write_text(dumps(m), encoding='utf-8')

    migration = dict(source_refs=['U345', 'U364'], model_before=str((OUT/'model-before.yaml').relative_to(ROOT)).replace('\\','/'),
                     model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),
                     delta={}, behaviors=[], adopted_mechanisms=adopted)
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]}; new={x['id']:x for x in m[key]}
        migration['delta'][key]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
                                    changed={i:value_hash(new[i]) for i in sorted(new.keys()&old.keys()) if new[i]!=old[i]},
                                    removed=sorted(old.keys()-new.keys()))
    (OUT/'implementation.yaml').write_text(dumps(migration), encoding='utf-8')
    review['status']='principles_integrated_U364'
    review['source_refs']=list(dict.fromkeys(review['source_refs']+refs))
    review['implementation_U364']=migration
    review['current_U364']=dict(parent_id='D02.e', behavior_ids=[x[0] for x in specifications],
        distinction='Compléter en préservant les affectations existantes ou réviser les affectations modifiables.',
        scope='Cette section et model.yaml décrivent la cible intégrée ; les propositions initiales conservent leurs formulations historiques.')
    rp.write_text(dumps(review), encoding='utf-8')

    audit['source_refs']=list(dict.fromkeys(audit['source_refs']+refs))
    audit['implementation_U364']=migration
    audit['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest()
    source_ids=[]
    for comparison in [review['mechanisms'][1]['market_comparisons'][0], microsoft]:
        source=next((s for s in audit['sources'] if s['url']==comparison['source_url']),None)
        if source is None:
            sid='S'+str(max(int(s['id'][1:]) for s in audit['sources'])+1).zfill(2)
            source=dict(id=sid,vendor=comparison['vendor'],native_label=comparison['element_name'],native_id=None,
                url=comparison['source_url'],edition=comparison['source_version'],consulted_on='2026-09-18',
                locator=comparison['source_locator'],nature='documentation',access=comparison['evidence_limits'],
                observed_fact=comparison['similarities'],limits=comparison['differences'],reuse='Synthèse sélective et lien.')
            audit['sources'].append(source)
        source_ids.append(source['id'])
    assessment=next(x for x in audit['assessments'] if x['capability_id']=='D02.e')
    assessment.update(existing_behaviors=[x[0] for x in specifications],verdict='trois mécanismes intégrés U364',
        diagnosis=parent['fields']['decomposition_rationale'],
        recommendation='Conserver les décisions spécialisées et les protections ; A01/A02 restent ouverts pour les contrats et la cohérence collective.',
        market_sources=list(dict.fromkeys(assessment['market_sources']+source_ids)))
    for identifier, *_ in specifications:
        audit['existing_behavior_review'].append(dict(behavior_id=identifier,status='integrated_U364',market_sources=source_ids,
            recommendation='Principe et parent acquis ; pas de confusion entre stabilité métier, gel et stratégie de recalcul. Détails et contrats à éprouver.'))
    arbitration=next(x for x in audit['arbitrations'] if x['id']=='A03')
    arbitration.update(status='partially_resolved_U364',
        recommendation='Supply Assignment porte application du plan, complément préservant et réaffectation. D04 garde les mutations des Orders ; D06 garde l’exécution.',
        limit='Principes et rattachements intégrés U345/U364 ; contrats entre capacités et détails éditoriaux ne sont pas validés globalement.')
    ap.write_text(dumps(audit),encoding='utf-8')
    append('marche/comparaisons.md', '''## CMP134

- Codex ; 18 septembre 2026 ; U345/U364 ; ELM215/ELM216 ; backlog D02.e et BHV045–BHV047.
- SAP S/4HANA aATP 2025 FPS01, Backorder Processing, section Reassignment : passage primaire indexé relu pendant la discussion. Sans Reassignment, conserver les affectations et traiter le reliquat ; avec Reassignment, remettre en jeu les affectations du périmètre sélectionné. Source : https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html
- Microsoft Dynamics 365 SCM, Keep supply for confirmed demand, sections What data is preserved et Control how on-hand inventory is pegged, page primaire relue pendant la discussion : conservation d’une chaîne et du pegging entre planifications, avec conditions particulières pour le stock reçu. Source : https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand
- Recouvrement partiel : SAP associe décisions et application ; FLOW les sépare. Reassignment est un terme SAP établi ; Incremental Supply Assignment reste un libellé descriptif FLOW, sans consensus de nommage démontré. Microsoft protège une chaîne plus large, sans équivalence exacte avec le complément d’affectation FLOW. Pas de preuve d’import d’un plan externe arbitraire chez SAP, ni de réalisation Beaumanoir.
- U364 adopte la distinction stabilité/adaptation et sa représentation. Compléter sans remettre en jeu l’existant n’est ni un gel permanent, ni RETE, ni une promesse de recalcul partiel. Correspondances et noms restent proposés dans leur portée ; descriptions et limites exposées dans les fiches.''')
    append('JOURNAL.md', '''## 2026-09-18 — U364 : comportements Supply Assignment

Intégration BHV045–BHV047 : application de plan, complément préservant les affectations et réaffectation des liens modifiables. Distinction adoptée, compléments éditoriaux qualifiés ; décisions, réservations et Freezing séparés. Comparaisons SAP/Microsoft conservées dans les fiches (CMP134). Audit courant actualisé ; preuves antérieures capturées, aucune publication.''')
    (OUT/'README.md').write_text('''# Supply Assignment — U364

Trois comportements sous D02.e :

- BHV045 **Supply Assignment Plan Application** : appliquer les affectations d’un plan retenu et signaler les écarts.
- BHV046 **Incremental Supply Assignment** : compléter les besoins non affectés tout en préservant les affectations existantes.
- BHV047 **Supply Reassignment** : réviser les affectations modifiables pour appliquer de nouveaux arbitrages entre commandes.

Les deux politiques rendent visibles stabilité et adaptation. Un plan peut mobiliser l’une ou l’autre ; aucun sous-comportement ni séquence imposée. Les décisions choisissent, Supply Assignment applique ; Freezing limite les révisions autorisées. La politique incrémentale n’impose pas un algorithme de recalcul.

U364 valide la distinction et son rattachement ; U345 avait acquis l’application de plan. Les deux définitions de politique reprennent les formulations présentées ; noms anglais et détails éditoriaux ne sont pas validés globalement. Comparaisons SAP et Microsoft dans les fiches, avec recouvrements et limites, CMP134. Les arbitrages A01/A02 restent ouverts.

[Annexe structurée](../../modeles/backlog/supply-assignment-mechanisms-review.yaml) · [Preuve de migration](implementation.yaml). Backlog uniquement, aucune release.
''',encoding='utf-8')
    print('U364 integrated: BHV045–BHV047 under Supply Assignment.')


if __name__=='__main__':
    main()

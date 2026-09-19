"""Integrate the scoped U349 agreement; preserve earlier model evidence."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

from scripts.lifecycle import value_hash
from scripts.structured_io import read, dumps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-18-order-lifecycle-behaviors'


def append(path, text):
    with (ROOT / path).open('a', encoding='utf-8') as f:
        f.write('\n\n' + text.strip() + '\n')


def main():
    assert not OUT.exists(), 'U349 already integrated.'
    contributions = (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    assert '## U348\n' not in contributions and '## U349\n' not in contributions
    OUT.mkdir()
    for name in ['model', 'behavior-gap-audit', 'supply-assignment-mechanisms-review']:
        (OUT/(name+'-before.yaml')).write_bytes((ROOT/('modeles/backlog/'+name+'.yaml')).read_bytes())
    for ident, title, quote, scope in [
        ('U348', 'Affermissement et niveau comportement',
         'Order Lifecycle Management contient des comportements dont l\'un deux est "affermir" : c\'est ça que tu veux dire ?',
         'Question de clarification. La réponse propose Order Firming sous Order Lifecycle Management, avec la définition reprise dans U349 ; le catalogue ne portait pas encore ce comportement.'),
        ('U349', 'Adoption de l’affermissement et ajout de la protection contre la réoptimisation',
         'Alors nous sommes ok.\nIl faut rajouter également ce mécanisme de protection contre l\'optimisation',
         'Accord sur Order Firming, sa définition présentée et son rattachement à Order Lifecycle Management, puis demande d’ajouter également le mécanisme de protection contre les réoptimisations dans ce contexte. Le principe de protection et le rattachement contextuel sont retenus ; son nom anglais, sa définition détaillée, les exemples, les modalités et les relations transversales sont éditoriaux. Aucun affermissement ne fige implicitement toutes les dates, quantités ou affectations. Aucune release demandée.')]:
        append('connaissance/01-contributions-utilisateur.md', f'## {ident}\n\n**id**\n\n{ident}\n\n**date**\n\n2026-09-18\n\n**titre**\n\n{title}\n\n**texte**\n\n{quote}\n\n**contexte et portée**\n\n{scope}')

    model_path = ROOT/'modeles/backlog/model.yaml'
    m = read(model_path)
    before = deepcopy(m)
    nodes = {n['id']: n for n in m['nodes']}
    assert not {'BHV036', 'BHV037'} & nodes.keys()
    now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    refs = ['U348', 'U349', 'ELM216', 'CMP125']

    def lifecycle(values, fields=()):
        return dict(state='urbanist_validated' if fields else 'under_instruction',
                    recorded_at=now, recorded_by='Codex', source_refs=['U349'],
                    validated_fields=list(fields), value_sha256={f: value_hash(values[f]) for f in fields},
                    note='Portée U349 consignée dans order-lifecycle-behaviors.yaml ; les compléments éditoriaux ne sont pas adoptés implicitement.')

    comparisons = deepcopy(read(ROOT/'modeles/backlog/supply-assignment-mechanisms-review.yaml')['clarifications_U346_U347']['market_comparisons'][2:])
    for c in comparisons:
        c['source_refs'] += ['U349', 'CMP125']
        c['element_type'] = 'Mécanisme ou transition métier réalisé par un produit'
        c['flow_position'] = ('U349 : affermissement et protection contre les réoptimisations sont deux comportements distincts sous Order Lifecycle Management. '
                              'Le gel porte sur les éléments explicitement protégés ; Promise Management et Supply Assignment gardent leurs responsabilités. '
                              'Order Freezing est un libellé éditorial, pas un terme unanimement établi à ce périmètre. Correspondance proposée.')

    firm_definition = 'Transformer une intention planifiée en ordre ferme, avec les engagements et restrictions de révision associés.'
    firm_scope = ('Passer d’une intention encore planifiée à un Order ferme selon les règles de son type, en conservant l’origine et les engagements associés. '
                  'Ce changement engage les pratiques de préparation et de coordination de l’entreprise ; il ne s’agit pas seulement de changer un statut informatique. '
                  'L’affermissement peut être automatique ou décidé par un acteur autorisé ; aucun contrôle manuel systématique imposé.\n\n'
                  'Exemple fictif : une proposition de transfert de 100 pièces destinée à une implantation magasin devient un ordre de transfert ferme, exploitable par les responsables de sa mise en œuvre. '
                  'Son affermissement ne prouve ni lancement, ni préparation physique, ni réservation de 100 pièces.\n\n'
                  'Les restrictions résultent de règles explicites : devenir ferme ne fige pas automatiquement toutes les dates, les quantités, la promesse ou la source. '
                  'Order Freezing porte le mécanisme distinct de protection contre les réoptimisations ; les deux peuvent se combiner. '
                  'La capacité de gestion du type d’Order conserve son contenu ; Promise Management garde la promesse et Supply Assignment les liens ressources-commandes. '
                  'L’existence de la distinction planifié/ferme s’apprécie par type d’Order ; aucun cycle universel imposé.')
    freeze_definition = ('Protéger les éléments désignés d’un Order contre leur modification par les réoptimisations, '
                         'en explicitant la portée du gel et les conditions autorisées de révision.')
    freeze_scope = ('Appliquer et maintenir une protection métier sur un Order, une ligne ou une quantité définie : échéance identifiée, quantité, engagement confirmé et, si cela est explicitement requis, affectation de ressources. '
                    'Distinguer les dates demandées des dates promises. Rendre les restrictions connues des décisions et des capacités qui appliquent leurs résultats ; le gel ne recalcule pas lui-même la meilleure promesse.\n\n'
                    'Exemple fictif : 100 pièces promises vendredi restent protégées contre une optimisation qui favoriserait une autre demande. '
                    'Changer d’entrepôt fournisseur demeure possible si la source n’est pas gelée et si les autres contraintes restent satisfaites. '
                    'Si un lot précis est également protégé, Supply Assignment doit préserver ce lien. Protéger un engagement et protéger son affectation sont des portées distinctes du mécanisme.\n\n'
                    'Le gel ne garantit pas la présence physique de la ressource. Si un incident rend l’engagement irréalisable, rendre l’exception visible et solliciter une révision selon les responsabilités et autorisations applicables ; '
                    'ne pas masquer l’échec ni lever silencieusement la protection. Les règles de durée, d’exception et de levée sont à préciser par contexte ; aucune immutabilité absolue ni validation humaine systématique imposée.\n\n'
                    'Le bénéfice est la stabilité des engagements et de la préparation opérationnelle ; le compromis est une latitude d’optimisation réduite. '
                    'Geler ne signifie pas mettre en attente l’exécution : Hold bloque une progression, le gel limite la modification des éléments désignés. '
                    'Ce mécanisme ne réserve pas implicitement le stock, ne crée pas une enveloppe Supply Protection et n’est ni un verrou transactionnel ni une stratégie de calcul incrémental. '
                    'API, écran, batch et flux sont des moyens d’application. Une simulation peut montrer une alternative hors gel si elle en expose la dérogation nécessaire ; son résultat ne modifie pas l’engagement protégé.\n\n'
                    'Nommage : Order Freezing reprend la notion de gel utilisée en planification. Le périmètre FLOW est une protection sélective des Orders ; '
                    'il ne reprend pas automatiquement le gel temporel Microsoft, qui limite aussi la création d’ordres planifiés. Nom et détails éditoriaux proposés.')
    definitions = [
        ('BHV036', 'Order Firming', firm_definition, 'Rendre explicite le passage d’une intention planifiée à un engagement opérationnel ferme.', firm_scope, [comparisons[1]], ['name', 'definition']),
        ('BHV037', 'Order Freezing', freeze_definition, 'Stabiliser les engagements et la préparation opérationnelle malgré les réoptimisations, tout en conservant les adaptations autorisées.', freeze_scope, [comparisons[0], comparisons[2], comparisons[3]], []),
    ]
    for ident, name, definition, finality, scope, market, approved in definitions:
        fields = dict(name=name, definition=definition, finality=finality, scope=scope, market_comparisons=market)
        m['nodes'].append(dict(id=ident, revision=1, kind='behavior', layer='transactional', fields=fields,
                              source_refs=refs, source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u349'),
                              adoption_ids=[], review=dict(state='partial', note='Principe et parent retenus U349 ; voir la portée champ par champ dans l’annexe.'),
                              editorial_basis='Mécanisme terminal et combinable. Aucun sous-comportement ; exemples fictifs et compléments éditoriaux proposés.',
                              lifecycle=lifecycle(fields, approved)))
        relation = dict(id='REL-BEHAVIOR-'+ident, revision=1, type='contains', source_id='D04.o', target_id=ident, source_refs=['U348', 'U349'],
                        review=dict(state='accepted', note='U349 : ajout des deux mécanismes dans le contexte explicite d’Order Lifecycle Management.'))
        relation['lifecycle'] = lifecycle(relation, ['type', 'source_id', 'target_id'])
        m['relations'].append(relation)

    parent = nodes['D04.o']
    parent['revision'] += 1
    # Correct the historical open parent after U345 without rewriting the old evidence.
    parent['fields']['scope'] = parent['fields']['scope'].replace(
        'Le parent d’un éventuel comportement transverse d’application de plan reste à instruire, sans nouvelle capacité ajoutée.',
        'U345 rattache l’application des affectations du plan à Supply Assignment ; les effets sur les Orders restent portés par leurs capacités responsables.')
    parent['fields']['scope'] += ('\n\nU349 distingue deux comportements : Order Firming transforme l’intention planifiée en ordre ferme ; '
                                 'Order Freezing protège les éléments désignés contre les réoptimisations. Ils sont combinables, sans équivalence automatique entre fermeté et gel. '
                                 'Le gel ne bloque pas la réalisation et ne réserve pas implicitement une ressource. Les autres opérations du cycle restent décrites sans devenir systématiquement des comportements.')
    rationale = ('Le passage d’une intention à un ordre ferme change les engagements et la préparation opérationnelle ; '
                 'la protection contre les réoptimisations stabilise certains résultats tout en limitant les adaptations admissibles. '
                 'Ces effets distincts justifient deux mécanismes combinables, sans créer un comportement pour chaque transition ni une séquence obligatoire. '
                 'La complexité ciblée est de préserver ce qui est engagé sans figer inutilement la manière de satisfaire l’Order.')
    parent['fields']['decomposition_rationale'] = rationale
    parent['fields']['market_comparisons'] = comparisons
    parent['source_refs'] += refs + ['U345']
    parent['review']['note'] = 'U349 ajoute deux mécanismes ; nom et nature historiques préservés, justification et compléments éditoriaux proposés.'

    for consumer, meaning in [
        ('D03.n', 'A besoin de connaître les éléments de l’Order protégés contre une révision de promesse et les conditions de dérogation.'),
        ('D02.e', 'A besoin de connaître les affectations explicitement protégées et les marges de substitution encore autorisées.')]:
        relation = dict(id='REL-NEEDS-U349-'+consumer, revision=1, type='relates-to', source_id=consumer, target_id='BHV037', source_refs=['U349', 'CMP125'],
                        qualification=dict(role='needs', meaning=meaning,
                                           conditions=['Lorsqu’une protection applicable concerne le résultat ou l’affectation à modifier.'],
                                           effects=['Respecter la protection ou rendre explicite la révision autorisée nécessaire ; ne pas la lever silencieusement.'],
                                           scope='Contrat métier proposé ; pas un appel technique imposé. Order Lifecycle Management gouverne la restriction, le consommateur garde sa responsabilité.'),
                        review=dict(state='proposed', note='Dépendance éditoriale proposée ; U349 ne valide pas ce contrat détaillé.'))
        relation['lifecycle'] = lifecycle(relation)
        m['relations'].append(relation)

    model_path.write_text(dumps(m), encoding='utf-8')
    adopted = [dict(node_id='BHV036', parent_id='D04.o', adopted_fields=['name', 'definition'],
                    value_sha256={k: value_hash(v) for k, v in [('name', 'Order Firming'), ('definition', firm_definition)]}),
               dict(node_id='BHV037', parent_id='D04.o', adopted_fields=[], value_sha256={},
                    principle='Protéger les commandes que l’on veut rendre fermes contre les demandes de réoptimisation.',
                    principle_source='U347 puis demande d’ajout U349', naming_status='editorial_proposal')]
    adopted[1]['principle_sha256'] = value_hash(adopted[1]['principle'])
    migration = dict(source_refs=['U348', 'U349'], model_before=str((OUT/'model-before.yaml').relative_to(ROOT)).replace('\\', '/'),
                     model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(), delta={}, behaviors=[],
                     adopted_behaviors=adopted, scope='Deux comportements ajoutés sous D04.o ; noms/définition adoptés seulement pour Order Firming, principe pour la protection. Contrats transversaux proposés.')
    for collection in ['nodes', 'relations']:
        old = {x['id']: x for x in before[collection]}; new = {x['id']: x for x in m[collection]}
        migration['delta'][collection] = dict(added={i: value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
                                              changed={i: value_hash(new[i]) for i in sorted(old.keys() & new.keys()) if old[i] != new[i]},
                                              removed=sorted(old.keys()-new.keys()))
    (OUT/'implementation.yaml').write_text(dumps(migration), encoding='utf-8')
    review = dict(id='ORDER-LIFECYCLE-BEHAVIORS-U349', source_refs=refs, parent_id='D04.o', status='principles_adopted_editorial_details_proposed',
                  decomposition_rationale=rationale, adoption_U349=adopted,
                  behavior_ids=['BHV036', 'BHV037'], proposed_contract_ids=['REL-NEEDS-U349-D03.n', 'REL-NEEDS-U349-D02.e'],
                  naming='Order Firming adopté ; Order Freezing est un nom éditorial fondé sur la notion marché de gel, sans équivalence exacte de périmètre.',
                  remaining_questions=['Conditions de levée et de révision par type d’Order.', 'Portées de gel selon les cas : résultat promis ou affectation également.', 'P11 Coordinated Order Release reste à instruire séparément.'],
                  market_comparisons=comparisons)
    (ROOT/'modeles/backlog/order-lifecycle-behaviors.yaml').write_text(dumps(review), encoding='utf-8')

    audit = read(ROOT/'modeles/backlog/behavior-gap-audit.yaml')
    audit['source_refs'] += ['U348', 'U349', 'CMP125']
    audit['implementation_U349'] = migration
    audit['baseline']['sha256'] = sha256(model_path.read_bytes()).hexdigest()
    for i, c in enumerate(comparisons, 63):
        audit['sources'].append(dict(id=f'S{i}', vendor=c['vendor'], native_label=c['element_name'], native_id=None, url=c['source_url'],
                                     edition=c['source_version'], consulted_on=c['consulted_on'], locator=c['source_locator'], nature='documentation',
                                     access=c['evidence_limits'], observed_fact=c['similarities'], limits=c['differences'], reuse='Synthèse sélective et lien.'))
    assessment = next(x for x in audit['assessments'] if x['capability_id']=='D04.o')
    assessment.update(existing_behaviors=['BHV036', 'BHV037'], verdict='deux mécanismes intégrés U349 ; détails et P11 à instruire',
                      diagnosis=rationale, recommendation='Préciser les portées de gel et conditions de révision ; ne pas confondre avec Hold, réservation ou orchestration. P11 reste ouvert.',
                      market_sources=['S63', 'S64', 'S65', 'S66'])
    for ident, market in [('BHV036', ['S64']), ('BHV037', ['S63', 'S65', 'S66'])]:
        audit['existing_behavior_review'].append(dict(behavior_id=ident, status='adopted_scope_editorial_details_proposed',
                                                      recommendation='Portée U349 dans order-lifecycle-behaviors.yaml ; ne pas transformer l’affermissement en gel total implicite.', market_sources=market))
    (ROOT/'modeles/backlog/behavior-gap-audit.yaml').write_text(dumps(audit), encoding='utf-8')
    p = ROOT/'modeles/backlog/supply-assignment-mechanisms-review.yaml'
    assignment = read(p)
    assignment['followup_U349'] = dict(source_refs=['U349'], behavior_ids=['BHV036', 'BHV037'], review_path='modeles/backlog/order-lifecycle-behaviors.yaml',
                                      status='principles_integrated', boundary='Les restrictions sont gouvernées sous Order Lifecycle Management ; Supply Assignment les respecte sans absorber le cycle de vie. Le calcul incrémental U346 reste distinct.')
    p.write_text(dumps(assignment), encoding='utf-8')
    append('marche/comparaisons.md', '''## CMP125

- Codex ; 18 septembre 2026 ; U348/U349 ; ELM216 ; D04.o, BHV036, BHV037. Sources Microsoft Firm planned orders, Keep supply for confirmed demand, Master plans — Freeze, et SAP Fixed Date and Quantity consultées de nouveau.
- Affermissement : transition planifié vers ferme. Protection : stabilité d’éléments désignés contre réoptimisation ; recouvre partiellement les protections SAP et Microsoft, sans les unifier artificiellement. Microsoft freeze time fence vise une fenêtre et empêche aussi la création d’ordres planifiés ; ce n’est pas une équivalence exacte avec un gel sélectif d’Order.
- U349 adopte Order Firming et sa définition présentée puis demande le mécanisme de protection. Order Freezing est le libellé éditorial ; périmètres, exceptions, exemples et contrats proposés. Bénéfice : stabilité des engagements et préparation ; compromis : liberté d’optimisation réduite.
- Protéger la date/quantité promise ne fige pas nécessairement la source. D04 gouverne les restrictions, D03 et Supply Assignment les respectent dans leurs responsabilités. Aucun lock technique ni réservation implicite. Pas de preuve de déploiement Beaumanoir.
- Comparaisons structurées sur la capacité et les comportements ; annexe order-lifecycle-behaviors.yaml. P11 non adopté par extension.''')
    append('JOURNAL.md', '''## 2026-09-18 — U349 : affermissement et protection contre les réoptimisations

Ajout de BHV036 Order Firming et BHV037 Order Freezing sous Order Lifecycle Management. Accord sur le nom/définition du premier, principe et parent contextuel du second ; nom anglais du second et détails éditoriaux proposés. Justification de décomposition, exemples concrets, comparaisons marché et deux dépendances proposées vers la protection. État avant conservé et audit des comportements actualisé ; aucune publication.''')
    p = ROOT/'AGENTS.md'
    text = p.read_text(encoding='utf-8')
    marker = '- Stock Protection relève de la gouvernance/management.'
    assert marker in text
    text = text.replace(marker, '- **Order Lifecycle Management (U349)** : Order Firming et protection contre les réoptimisations sont deux mécanismes distincts. Affermir ne fige pas implicitement dates, quantités, promesse ou affectation. Le gel limite les modifications, Hold limite la progression ; aucun verrou technique ni réservation implicite. Portées et statuts : `modeles/backlog/order-lifecycle-behaviors.yaml`.\n'+marker)
    p.write_text(text, encoding='utf-8')
    (OUT/'README.md').write_text('# Order Lifecycle Management — U349\n\nDeux comportements intégrés : Order Firming (BHV036) et protection contre les réoptimisations (BHV037, nom éditorial Order Freezing).\n\nLe modèle courant porte les descriptions, exemples et comparaisons. [Portée de validation et questions ouvertes](../../modeles/backlog/order-lifecycle-behaviors.yaml). [Preuve de migration](implementation.yaml). Les fichiers before conservent les états antérieurs ; aucune publication modifiée.\n', encoding='utf-8')
    print('U349 integrated: 2 behaviors, 2 containment relations, 2 proposed dependencies; earlier values preserved.')


if __name__ == '__main__':
    main()

"""Integrate the scoped U378 agreement; preserve prior evidence and publications."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-18-fulfillment-plan-U378'


def save(path, value):
    (ROOT / path).write_text(dumps(value), encoding='utf-8')


def main():
    assert not OUT.exists(), 'Migration already recorded; do not overwrite evidence.'
    mp = ROOT / 'modeles/backlog/model.yaml'
    before = read(mp)
    m = deepcopy(before)
    assert not any(n['id'] == 'D03.o' for n in m['nodes'])
    review = read(ROOT / 'modeles/backlog/fulfillment-strategy-review.yaml')
    proposal = review['global_plan_review_U377']
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    refs = ['U377', 'U378', 'ELM228', 'CMP139']

    def cycle(values, fields, sources):
        return dict(state='urbanist_validated' if fields else 'under_instruction',
                    recorded_at=stamp, recorded_by='Codex', source_refs=sources,
                    validated_fields=fields,
                    value_sha256={f: value_hash(values[f]) for f in fields},
                    note='Accord limité aux champs indiqués ; détails éditoriaux et contrats qualifiés séparément.')

    cp = ROOT / 'connaissance/01-contributions-utilisateur.md'
    text = cp.read_text(encoding='utf-8')
    assert '## U378\n' not in text
    text += '''\n\n## U378

**id**

U378

**date**

2026-09-18

**titre**

Adopter Fulfillment Plan Decision

**texte**

Le vocabulaire microsoft me plait énormément.

Je valide ta proposition

**contexte et portée**

Accord sur la proposition présentée après U377 : nom Fulfillment Plan Decision, nature décision et définition produisant un scénario cohérent de plan d’affectation, mobilisant les décisions spécialisées et les politiques applicables pour maximiser la valeur multidimensionnelle. Le choix du seul cadre U365/U376 ne constitue plus la cible. Principe de composition par dépendances, sans niveau inférieur de capacités ; application du plan par Supply Assignment distincte. Rattachement D03 cohérent avec la proposition en cours ; relation formelle et détails de contrats restent éditoriaux. Le nom de domaine Fulfillment Optimization adopté U369 est appliqué dans ce même domaine. Aucun accord global sur les comparaisons marché, nouveaux exemples, comportements ou publication.
'''
    cp.write_text(text, encoding='utf-8')
    OUT.mkdir()
    (OUT / 'model-before.yaml').write_bytes(mp.read_bytes())
    (OUT / 'review-before.yaml').write_text(dumps(review), encoding='utf-8')
    fields = dict(name=proposal['proposed_name'], definition=proposal['proposed_definition'], nature='decision',
        finality='Proposer un plan d’affectation collectivement cohérent pour satisfaire les commandes selon les objectifs applicables.',
        scope=('Le résultat est un scénario de [Supply Assignment Plan](glossary:TER078) : ressources présentes ou futures, quantités et dates proposées pour les commandes du périmètre, avec hypothèses et contraintes. '
               'La stratégie et le paramétrage sont des entrées ; choisir leur cadre ne suffit pas à produire le plan.\n\n'
               'La vision globale porte sur les ressources admissibles et les demandes de l’horizon examiné. Elle n’impose ni un recalcul intégral à chaque événement, ni un algorithme, ni une garantie d’optimum mathématique. '
               'Le plan doit rendre explicites les besoins non satisfaits et les conditions de faisabilité.\n\n'
               'Mobiliser les résultats d’[ATP](model:D03.i), de [CTP](model:D03.j), de [PTP](model:D03.k), d’[Order Prioritization](model:D03.m) et de [Delivery Schedule Decision](model:D03.l) selon le cas. '
               'Ces capacités gardent leurs responsabilités ; leur composition n’introduit aucune sous-capacité ni séquence universelle. '
               'Respecter protections, réservations et gels applicables ; aucune levée implicite par l’optimisation. Les politiques référentielles sont consommées sans administration implicite des maîtres.\n\n'
               '[Supply Assignment](model:D02.e) applique les affectations du plan retenu ; [Promise Management](model:D03.n) conserve proposition, confirmation et révision de promesse. '
               'Produire ce scénario ne réserve pas les ressources, ne modifie pas les Orders et ne déclenche pas à lui seul l’exécution. '
               'Cette décision opérationnelle collective ne reprend pas la planification globale externe.\n\n'
               'Exemple fictif : deux commandes demandent chacune 80 pièces alors que 100 pièces sont admissibles. Les considérer séparément peut donner deux possibilités incompatibles. '
               'La décision établit une proposition commune selon les priorités et contraintes, explicite les 60 pièces restant sans ressource et les éventuels apports futurs nécessaires. '
               'Le chiffrage illustre la cohérence collective ; il ne prescrit aucune politique de répartition.'))
    fields['market_comparisons'] = deepcopy(proposal['market_comparisons'])
    for entry in fields['market_comparisons']:
        entry['source_refs'] = list(dict.fromkeys(entry['source_refs'] + ['U378']))
        entry['flow_position'] = ('U378 intègre Fulfillment Plan Decision : scénario de plan issu de décisions spécialisées. '
                                 'Fulfillment plan est un résultat Microsoft ; le suffixe Decision et le découpage restent propres à FLOW. Correspondance proposée.')
    node = dict(id='D03.o', revision=1, kind='capability', layer='transactional', fields=fields,
                source_refs=refs, source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u378'),
                review=dict(state='partial', note='Nom, définition et nature adoptés U378 ; finalité rédigée, scope, exemples et comparaisons proposés.'),
                adoption_ids=[], lifecycle=cycle(fields, ['name', 'definition', 'nature'], ['U378']))
    m['nodes'].append(node)
    domain = next(n for n in m['nodes'] if n['id'] == 'D03')
    domain['fields']['name'] = 'Fulfillment Optimization'
    domain['revision'] += 1
    domain['source_refs'] = list(dict.fromkeys(domain['source_refs'] + ['U369', 'U378']))
    domain['lifecycle']['source_refs'] = list(dict.fromkeys(domain['lifecycle']['source_refs'] + ['U369']))
    domain['lifecycle']['value_sha256']['name'] = value_hash(domain['fields']['name'])
    domain['lifecycle']['recorded_at'] = stamp
    domain['lifecycle']['note'] = 'Nom adopté U369 appliqué U378 ; finalité et son accord antérieur inchangés. État précédent conservé dans la capture U378.'
    domain['review']['note'] = 'Nom Fulfillment Optimization adopté U369 ; définition et scope existants conservés.'

    parent = dict(id='REL-MEMBER-D03.o', revision=1, type='contains', source_id='D03', target_id='D03.o', source_refs=refs,
                  review=dict(state='under_review', note='Rattachement éditorial à D03, domaine de la décision de satisfaction.'),
                  lifecycle=cycle({}, [], ['U378']))
    m['relations'].append(parent)
    dependencies = [
        ('D03.o', 'D03.i', 'A besoin des possibilités de quantités et dates dans la situation de référence.'),
        ('D03.o', 'D03.j', 'A besoin des possibilités sous adaptation et de leurs conditions de faisabilité lorsque la référence ne suffit pas.'),
        ('D03.o', 'D03.k', 'A besoin de la comparaison économique des scénarios, sans réduire la valeur multidimensionnelle à la seule marge.'),
        ('D03.o', 'D03.m', 'A besoin des priorités relatives des commandes pour établir le scénario collectif.'),
        ('D03.o', 'D03.l', 'A besoin des échéanciers admissibles et retenus pour rendre cohérentes quantités et dates.'),
        ('D03.o', 'D02.b', 'A besoin des protections actives encadrant les usages admissibles des ressources.'),
        ('D02.e', 'D03.o', 'A besoin du scénario retenu de plan d’affectation pour matérialiser les liens ressources-commandes concernés.'),
    ]
    for index, (source, target, meaning) in enumerate(dependencies, 1):
        m['relations'].append(dict(id=f'REL-NEEDS-U378-{index:02d}', revision=1, type='relates-to', source_id=source, target_id=target,
            source_refs=refs, qualification=dict(role='needs', meaning=meaning,
                conditions=['Selon le cas et les hypothèses du scénario ; aucune séquence ou invocation systématique imposée.'],
                effects=['Résultat mobilisé sans transférer la responsabilité de la capacité fournisseur.'],
                scope='Relation et contrat détaillés proposés ; dépendance métier, pas hiérarchie ni appel technique.'),
            review=dict(state='under_review', note='Principe de composition acquis ; qualification précise proposée.'), lifecycle=cycle({}, [], ['U378'])))
    save('modeles/backlog/model.yaml', m)
    migration = dict(source_refs=refs, model_before=(OUT / 'model-before.yaml').relative_to(ROOT).as_posix(),
                     model_before_sha256=sha256((OUT / 'model-before.yaml').read_bytes()).hexdigest(), delta={}, behaviors=[],
                     adopted_fields=node['lifecycle']['validated_fields'], node_id=node['id'],
                     value_sha256=node['lifecycle']['value_sha256'], parent_relation_status='proposed')
    for key in ['nodes', 'relations']:
        old = {x['id']: x for x in before[key]}; new = {x['id']: x for x in m[key]}
        migration['delta'][key] = dict(added={i:value_hash(new[i]) for i in new.keys()-old.keys()},
            changed={i:value_hash(new[i]) for i in old.keys() & new.keys() if old[i] != new[i]}, removed=sorted(old.keys()-new.keys()))
    (OUT / 'implementation.yaml').write_text(dumps(migration), encoding='utf-8')
    review['status'] = 'plan_decision_integrated_U378'
    review['source_refs'].append('U378')
    review['global_plan_review_U377']['status'] = 'name_definition_nature_adopted_U378'
    review['implementation_U378'] = migration
    review['current_U378'] = dict(node_id='D03.o', name=fields['name'], adopted_fields=['name', 'definition', 'nature'],
        distinction='Produire le scénario collectif ; les stratégies sont des entrées, Supply Assignment applique le plan retenu.',
        no_behavior='Aucune décomposition en comportements justifiée à ce stade ; les décisions spécialisées restent des capacités sœurs.')
    save('modeles/backlog/fulfillment-strategy-review.yaml', review)
    audit = read(ROOT / 'modeles/backlog/behavior-gap-audit.yaml')
    audit['source_refs'].append('U378'); audit['implementation_U378'] = migration
    audit['baseline']['sha256'] = sha256(mp.read_bytes()).hexdigest()
    audit['assessments'].append(dict(capability_id='D03.o', name=fields['name'], existing_behaviors=[], verdict='conserver',
        diagnosis='Décision de cohérence collective adoptée U378 ; aucune décomposition descriptive nécessaire.',
        recommendation='Conserver les décisions spécialisées comme capacités sœurs ; liens de dépendance proposés, pas sous-capacités.',
        market_sources=[], candidate_ids=[]))
    arbitration = next(x for x in audit['arbitrations'] if x['id'] == 'A02')
    arbitration['status'] = 'responsibility_resolved_U378'
    arbitration['recommendation'] = 'Fulfillment Plan Decision D03.o produit le scénario collectif ; Supply Assignment applique le plan retenu. Décisions spécialisées conservées.'
    arbitration['limit'] = 'Responsabilité adoptée U378 ; détails de dépendances, critères et règles restent à préciser selon les cas, sans bloquer le catalogue.'
    arbitration['capabilities'] = list(dict.fromkeys(arbitration['capabilities'] + ['D03.o']))
    save('modeles/backlog/behavior-gap-audit.yaml', audit)
    naming = read(ROOT / 'modeles/backlog/supply-fulfillment-audit.yaml')
    naming['source_refs'].append('U378')
    naming['adoption_U369']['status'] = 'D03_applied_U378_D13_pending'
    naming['adoption_U369']['scope'] = 'D03 renommé U378 ; D13 reste adopté à appliquer. Univers renommé U373. Aucun accord global sur les compléments éditoriaux.'
    naming['action_plan']['requires_joint_validation'] = [x for x in naming['action_plan']['requires_joint_validation'] if 'Fulfillment Strategy' not in x]
    naming['action_plan']['adopted_pending_application'] = ['D13 : Supply Network ; adoption U369, application au référentiel encore à réaliser.']
    naming['implementation_U378'] = dict(domain='D03', name='Fulfillment Optimization', capability='D03.o', review_path='modeles/backlog/fulfillment-strategy-review.yaml')
    for finding in naming['findings']:
        if finding['id'] == 'SF-A02':
            finding['status'] = 'name_adopted_U369_applied_U378'
            finding['recommendation'] = 'Fulfillment Optimization est appliqué à D03 ; Fulfillment Plan Decision intégrée selon U378. Autres détails de périmètre non adoptés globalement.'
    save('modeles/backlog/supply-fulfillment-audit.yaml', naming)
    (OUT / 'README.md').write_text('''# Fulfillment Plan Decision — U378

D03.o produit un scénario cohérent de plan d’affectation en mobilisant les décisions spécialisées et les politiques. Nom, définition et nature décision sont adoptés. Finalité rédigée, exemples, relations détaillées et correspondances gardent leur statut propre.

D03 porte désormais le nom Fulfillment Optimization adopté U369. Aucun nouveau niveau hiérarchique ni comportement : les décisions restent sœurs, reliées par des dépendances proposées. Le plan candidat ne vaut ni réservation, ni promesse confirmée, ni application transactionnelle. Supply Assignment applique le plan retenu.

Microsoft : résultat Fulfillment Plan et service d’optimisation, distincts de la stratégie utilisée en entrée. Comparaisons et limites dans la fiche et l’annexe fulfillment-strategy-review.yaml. Le suffixe Decision est la convention FLOW.

La question de responsabilité A02 est résolue ; les règles et contrats détaillés ne sont pas adoptés globalement. D13 Supply Network reste un renommage acquis en attente d’application. Backlog uniquement ; aucune release, aucun push.

État précédent conservé dans model-before.yaml ; delta et empreintes dans implementation.yaml.
''', encoding='utf-8')
    print('U378 integrated: 1 capability, 1 domain rename, 8 proposed relations; no behavior or publication.')


if __name__ == '__main__':
    main()

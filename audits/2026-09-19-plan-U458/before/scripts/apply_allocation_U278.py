"""Refine Protection into the five peer behaviors requested in U278."""
from pathlib import Path
from hashlib import sha256
import json
from copy import deepcopy
from scripts.structured_io import read, dumps
from scripts.apply_planning_U269 import append, cycle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-17-protection-cinq-comportements'


def main():
    if OUT.exists():
        raise SystemExit('U278 already captured; do not reapply.')
    OUT.mkdir()
    for name in ('model', 'behavior-audit'):
        (OUT / f'{name}-before.yaml').write_bytes((ROOT / f'modeles/backlog/{name}.yaml').read_bytes())
    protected = {}
    for folder in ('release', 'revisions', 'decisions', 'provenance'):
        for p in (ROOT / 'modeles' / folder).rglob('*'):
            if p.is_file() and p != ROOT / 'modeles/provenance/source-records.json':
                protected[p.relative_to(ROOT).as_posix()] = sha256(p.read_bytes()).hexdigest()
    append('connaissance/01-contributions-utilisateur.md', '''## U278

**id**

U278

**date**

2026-09-17

**titre**

Cinq comportements pairs pour la gestion des enveloppes de Supply Protection

**texte**

Je trouve que les comportements sont plutot ceux ci :

1. attribution d’une enveloppe à un groupe (c'est l'allocation initiale) ;
2. réallocation entre groupes ;
3. libération des quantités inutilisées ;
4. imputation de la consommation ;
5. consultation des quantités allouées, consommées et restantes.

**contexte et portée**

Correction du regroupement réalisé en U277 : ces cinq résultats constituent les comportements pairs directement sous Supply Protection. Allocation conserve son identité BHV011 mais son périmètre devient l’attribution initiale ; l’ancien périmètre agrégé est capturé. Les cinq descriptions françaises sont reprises de la liste. Les nouveaux noms anglais, exemples, frontières et justification éditoriale restent proposés. Aucun sous-comportement, nouvelle capacité, renommage du parent ni publication demandé. Les comportements de seuils/validité restent à instruire.''')
    append('marche/comparaisons.md', '''Complément U278 à CMP092 — 17 septembre 2026 : Laurent corrige la maille en cinq comportements pairs sous Supply Protection. La recommandation précédente de les regrouper dans un seul comportement est remplacée. La source ELM176 est reconsultée, sections Use the allocation APIs, Allocate, Reallocate, Unallocate, Consume et Query. Chaque comportement est justifié par un résultat métier distinct : création de droits, changement de bénéficiaire, restitution, imputation d’usage ou visibilité. Cette justification porte sur les effets métier, pas sur le nombre d’API. Noms anglais nouveaux et descriptions complémentaires proposés ; pas d’équivalence normative Microsoft adoptée. Le solde d’enveloppe diffère du stock physique ; les autres risques de Protection ne sont pas intégralement couverts par ces cinq comportements.''')
    model = read(ROOT / 'modeles/backlog/model.yaml')
    original = deepcopy(model)
    assert not any(n['id'] == 'BHV012' for n in model['nodes'])
    entries = [
        ('BHV011', 'Allocation', "attribution d’une enveloppe à un groupe (c'est l'allocation initiale)",
         'Créer les droits initiaux d’un groupe sur un périmètre de ressources admissibles. Exemple fictif : attribuer 300 pièces au canal web sur un disponible commun de 1 000. Le résultat est une enveloppe effective ; aucun déplacement physique ni affectation à une commande n’est impliqué.'),
        ('BHV012', 'Reallocation', 'réallocation entre groupes',
         'Transférer des droits disponibles d’un groupe vers un autre. Exemple fictif : transférer 50 pièces du solde web vers les magasins ; le solde web baisse de 50 et celui des magasins augmente de 50. Le total des droits transférés est conservé dans ce cas simple. Cette opération ne déplace pas physiquement le stock et ne choisit pas à elle seule la répartition optimale.'),
        ('BHV013', 'Allocation Release', 'libération des quantités inutilisées',
         'Restituer au disponible commun des droits encore inutilisés, sans nouveau bénéficiaire désigné. Exemple fictif : libérer 20 pièces d’une enveloppe devenue excessive. Cela distingue la libération de la réallocation et de l’annulation d’une réservation. Les effets sur les engagements existants et les corrections de consommation restent à instruire.'),
        ('BHV014', 'Allocation Consumption', 'imputation de la consommation',
         'Enregistrer l’usage de droits contre la bonne enveloppe et actualiser son solde. Exemple fictif : imputer 80 sur une enveloppe de 300 laisse 220 disponibles dans le cas simple, sans autres mouvements. Le fait déclencheur (confirmation, réservation ou autre), les corrections et annulations restent à préciser. Microsoft permet un couplage à une réservation souple ; aucun couplage obligatoire ni double déduction avec Reservation ou Assignment n’est imposé.'),
        ('BHV015', 'Allocation Visibility', 'consultation des quantités allouées, consommées et restantes',
         'Rendre consultable l’état des droits par périmètre et bénéficiaire. Exemple fictif : retrouver l’enveloppe web, sa consommation et son solde, en tenant compte des réallocations et libérations. Ce résultat éclaire la maîtrise des enveloppes ; il se distingue de la visibilité du stock physique. La définition des cumuls, des périodes et de la fraîcheur reste à instruire.')]
    for identifier, name, definition, scope in entries:
        fields = {'name': name, 'definition': definition, 'scope': scope + '\n\nComportement terminal directement sous [Supply Protection](model:D02.b), combinable avec ses pairs sans séquence universelle. [Stock Allocation Decision](model:D05.d) reste la décision spécialisée des valeurs ; [Supply Assignment](model:D02.e) affecte les ressources aux besoins et [Reservation](model:D02.c) porte l’engagement de quantité. Écran, batch, flux et streaming restent des modalités, avec traitements unitaires, collectifs ou en masse selon le besoin.'}
        note = 'Description française et maille reprises de U278 ; nom anglais proposé sauf Allocation conservé U276. Périmètre, exemples et justification ajoutés proposés.'
        node = {'id': identifier, 'revision': 1, 'kind': 'behavior', 'layer': 'transactional', 'fields': fields,
                'source_refs': ['U276', 'U277', 'U278', 'CMP092'],
                'source_locator': {'path': 'connaissance/01-contributions-utilisateur.md', 'anchor': 'u278'},
                'review': {'state': 'partial', 'note': note}, 'adoption_ids': [],
                'lifecycle': cycle(fields, ['name', 'definition'] if identifier == 'BHV011' else ['definition'], ['U276', 'U278'] if identifier == 'BHV011' else ['U278'], note)}
        if identifier == 'BHV011':
            index = next(i for i,n in enumerate(model['nodes']) if n['id'] == identifier)
            node['revision'] = model['nodes'][index]['revision'] + 1
            model['nodes'][index] = node
        else:
            model['nodes'].append(node)
            rel = {'id': 'REL-PROTECTION-' + identifier, 'revision': 1, 'type': 'contains', 'source_id': 'D02.b', 'target_id': identifier,
                   'source_refs': ['U278'], 'review': {'state': 'accepted', 'note': 'Comportement pair de Supply Protection, découpage U278.'}}
            rel['lifecycle'] = cycle(rel, ['type', 'source_id', 'target_id'], ['U278'], rel['review']['note'])
            model['relations'].append(rel)
    parent = next(n for n in model['nodes'] if n['id'] == 'D02.b')
    parent['fields']['decomposition_rationale'] = 'Distinguer cinq résultats : créer des droits, changer leur bénéficiaire, les restituer, enregistrer leur usage et connaître leur état. Cette séparation rend explicites les effets différents sur les enveloppes et leurs soldes, aide à éviter les doubles déductions et différencie une libération d’une réallocation. Elle permet de discuter et vérifier chaque résultat indépendamment sans créer de sous-comportements ; elle ne découle pas du seul nombre d’API Microsoft.'
    parent['fields']['scope'] = parent['fields']['scope'].replace('[Allocation](model:BHV011) précise la gestion des enveloppes ;', '[Allocation](model:BHV011), [Reallocation](model:BHV012), [Allocation Release](model:BHV013), [Allocation Consumption](model:BHV014) et [Allocation Visibility](model:BHV015) décrivent cinq résultats distincts pour la gestion des enveloppes, directement sous cette capacité (U278) ;')
    parent['source_refs'].append('U278')
    parent['review']['note'] += ' U278 précise cinq comportements pairs et remplace le périmètre agrégé de BHV011 ; la justification éditoriale reste proposée.'
    (ROOT / 'modeles/backlog/model.yaml').write_text(dumps(model), encoding='utf-8')
    audit = read(ROOT / 'modeles/backlog/behavior-audit.yaml')
    audit['allocation_U276_U277']['superseded_scope_by'] = 'U278 : cinq comportements pairs ; BHV011 limité à l’attribution initiale. L’accord historique reste conservé.'
    audit['allocation_U278'] = {'state': 'adopted_in_stated_scope', 'source_refs': ['U278', 'CMP092'], 'parent_id': 'D02.b',
        'behavior_ids': [e[0] for e in entries], 'catalog_changed': True,
        'adopted_scope': 'Cinq descriptions françaises et décomposition en comportements pairs. Nom Allocation conservé ; nouveaux noms anglais proposés.',
        'proposed_details': 'Noms anglais BHV012–015, scopes et exemples, justification du parent.',
        'market_comparison': 'CMP092', 'historical_capture': 'audits/2026-09-17-protection-cinq-comportements/model-before.yaml'}
    entry = next(e for e in audit['assessments'] if e['capability_id'] == 'D02.b')
    entry['recommendation'] = 'Conserver ; cinq comportements pairs pour les enveloppes U278 ; seuils et validité à instruire'
    entry['candidate_detail'] = 'Attribution initiale ; réallocation ; libération ; imputation de consommation ; visibilité des enveloppes'
    entry['source_refs'].append('U278')
    audit['decision_boundary'] += ' U278 remplace le regroupement Allocation par cinq comportements pairs ; portées dans allocation_U278.'
    (ROOT / 'modeles/backlog/behavior-audit.yaml').write_text(dumps(audit), encoding='utf-8')
    old_nodes = {n['id']: n for n in original['nodes']}
    changed = [n['id'] for n in model['nodes'] if n['id'] in old_nodes and n != old_nodes[n['id']]]
    assert set(changed) == {'D02.b', 'BHV011'}, changed
    assert model['relations'][:len(original['relations'])] == original['relations']
    assert all(sha256((ROOT / p).read_bytes()).hexdigest() == h for p,h in protected.items())
    (OUT / 'integrity.json').write_text(json.dumps({'protected_files': protected, 'changed_existing_nodes': changed, 'new_nodes': [e[0] for e in entries[1:]], 'existing_relations_unchanged': len(original['relations'])}, indent=2), encoding='utf-8')
    print('Five peer behaviors recorded; identifiers and publications preserved.')


if __name__ == '__main__':
    main()

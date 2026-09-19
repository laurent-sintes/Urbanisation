"""Record U283 criteria and scoped Planning review; preserve historical adoptions."""
from pathlib import Path
from hashlib import sha256
import json
from scripts.structured_io import read, dumps
from scripts.apply_planning_U269 import append

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-17-planning-mecanismes'


def save(name, value):
    (ROOT / f'modeles/backlog/{name}.yaml').write_text(dumps(value), encoding='utf-8')


def main():
    assert '## U283' in (ROOT / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    if OUT.exists():
        raise SystemExit('U283 already integrated.')
    OUT.mkdir()
    for name in ('model', 'modeling-glossary', 'behavior-audit', 'd05-refactoring'):
        (OUT / f'{name}-before.yaml').write_bytes((ROOT / f'modeles/backlog/{name}.yaml').read_bytes())
    for path, name in [('AGENTS.md', 'AGENTS-before.md'), ('connaissance/35-comportements-inventory-planning.md', 'planning-before.md')]:
        (OUT / name).write_bytes((ROOT / path).read_bytes())
    protected = {p.relative_to(ROOT).as_posix(): sha256(p.read_bytes()).hexdigest()
                 for folder in ('release', 'revisions', 'decisions')
                 for p in (ROOT / 'modeles' / folder).rglob('*') if p.is_file()}
    note = ('U283 remplace la cible en six comportements : construction de scénarios alternatifs, simulation et adaptation '
            'de l’exécution d’un scénario sont les comportements retenus dans le principe. Analyse d’impact, évaluation, '
            'validation et application sont requalifiées en fonctions de produits, sans supprimer leurs besoins métier. '
            'Migration du catalogue à préciser ; valeurs et accords U269/U271 conservés comme historique, pas comme cible courante.')
    direction = {
        'source_refs': ['U283', 'CMP094'],
        'state': 'direction_adopted_catalog_migration_pending',
        'differentiating_criteria': ['Mécanisme', 'Politique', 'Variante', 'Bénéfice'],
        'accepted_behavior_directions': ['Construction de scénarios alternatifs', 'Simulation', 'Adaptation de l’exécution d’un scénario'],
        'functional_reclassification': ['BHV007', 'BHV008', 'BHV009', 'BHV010'],
        'note': note,
        'proposed_boundary': 'D05 adapte le scénario de stock à partir des faits et mobilise les décisions spécialisées ; D06 conserve adaptation opérationnelle et orchestration. Cette articulation détaillée reste proposée.',
        'open_points': ['Définitions et noms anglais révisés', 'Rattachement et identité du comportement d’adaptation, sans réutilisation implicite de BHV009', 'Préservation des fonctions et de leurs exigences dans les descriptions utiles, sans niveau supplémentaire'],
        'justification': 'Différencier des façons d’agir qui changent les pratiques et les processus ; conserver la justification par complexité ou bénéfice ciblé U265.',
    }
    model = read(ROOT / 'modeles/backlog/model.yaml')
    before = read(OUT / 'model-before.yaml')
    for n in model['nodes']:
        if n['id'] in ['D05.f', 'BHV005', 'BHV006', 'BHV007', 'BHV008', 'BHV009', 'BHV010']:
            n['review']['state'] = 'under_review'
            n['review']['note'] += '\n\n' + note
            n['source_refs'].append('U283')
    save('model', model)
    glossary = read(ROOT / 'modeles/backlog/modeling-glossary.yaml')
    glossary['source_refs'].append('U283')
    for term in glossary['terms']:
        if term['id'] not in ['MOD002', 'MOD006']:
            continue
        term['source_refs'].append('U283')
        if term['id'] == 'MOD006':
            addition = ('U283 retient Mécanisme, Politique, Variante ou bénéfice comme critères différenciants de décomposition. '
                        'Pour Planning, les effets sur les pratiques humaines et les processus distinguent les comportements '
                        'des fonctions de produits. Ces critères ne constituent pas quatre niveaux supplémentaires.')
        else:
            addition = note
            term['review']['state'] = 'under_review'
        term['notes'].append(addition)
        term['review']['adopted_scope'] += ' ' + addition
        term['review']['proposed_scope'] += ' Les formulations détaillées issues de U283 restent à préciser ; aucune nouvelle hiérarchie adoptée.'
    save('modeling-glossary', glossary)
    audit = read(ROOT / 'modeles/backlog/behavior-audit.yaml')
    audit['source_refs'].append('U283')
    audit['planning_mechanisms_U283'] = direction
    for key in ['scenario_planning_U267', 'scenario_impact_U270']:
        audit[key]['current_review_U283'] = note
    for item in audit['assessments']:
        if item.get('capability_id') == 'D05.f':
            item['state'] = 'under_review'
            item['recommendation'] = note
            item['source_refs'].append('U283')
    save('behavior-audit', audit)
    d05 = read(ROOT / 'modeles/backlog/d05-refactoring.yaml')
    d05['planning_mechanisms_U283'] = direction
    for key in ['scenario_behaviors_U269', 'scenario_impact_U271']:
        d05[key]['current_review_U283'] = note
    save('d05-refactoring', d05)
    p = ROOT / 'AGENTS.md'
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith('- **Maille des comportements'):
            lines[i] = ('- **Maille des comportements (U282/U283)** : Mécanisme, Politique, Variante ou bénéfice sont les critères différenciants. '
                        'Décrire une façon d’agir et son effet métier ; les opérations sur un concept restent matière de conception produit. '
                        'Pour Planning, expliciter les impacts sur les pratiques humaines et les processus. Ne pas créer quatre niveaux ni décomposer systématiquement. '
                        'Supply Protection : ancien découpage par opérations en réexamen. ATP inchangé à ce stade.')
        if line.startswith('- **Planning mobilise'):
            lines[i] = ('- **Planning mobilise les décisions**, qui restent distinctes. U283 retient comme comportements la construction de scénarios alternatifs, '
                        'la simulation et l’adaptation de l’exécution d’un scénario. Analyse d’impact, évaluation, validation et application sont requalifiées '
                        'en fonctions de produits ; leurs besoins restent à décrire. Le découpage U269/U271 en six comportements est historique et en réexamen. '
                        'Noms, définitions et migration du catalogue à préciser ; aucun transfert implicite de l’adaptation opérationnelle de D06 vers D05.')
        if line.startswith('- Inventory Planning :'):
            lines[i] = '- Inventory Planning : [historique et réexamen U283](connaissance/35-comportements-inventory-planning.md) ; direction courante dans `modeles/backlog/d05-refactoring.yaml`, section `planning_mechanisms_U283`. Accords U269/U271 conservés avec leurs empreintes.'
    p.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    p = ROOT / 'connaissance/35-comportements-inventory-planning.md'
    text = p.read_text(encoding='utf-8')
    first, rest = text.split('\n', 1)
    p.write_text(first + '\n\n> **Direction courante U283 :** ' + note + '\n> Voir `modeles/backlog/d05-refactoring.yaml`, section `planning_mechanisms_U283`. Les descriptions ci-dessous documentent le découpage historique.\n' + rest, encoding='utf-8')
    append('marche/elements.md', '''### ELM187

- Référence : MKT28, Kinaxis. Libellé natif : What is concurrent planning? Nature : présentation de méthode et de produit, pas norme de décomposition.
- Source : https://www.kinaxis.com/en/what-concurrent-planning ; sections How does concurrent planning work?, Improving agility, Planning proactively, Eliminating functional silos. Page évolutive sans édition logicielle ; texte consulté le 17 septembre 2026.
- Reformulation : les alternatives simulées aident les équipes à anticiper ; les changements et leurs impacts partagés permettent d’adapter les plans et de coordonner les acteurs.
- Limites : appui aux effets sur les pratiques et processus ; aucun catalogue normatif Capacité/Comportement, aucun déploiement Beaumanoir démontré. Synthèse sans import substantiel ; droits de republication non établis.''')
    append('marche/comparaisons.md', '''## CMP094

- Objet : U283 ; critères de comportement et réexamen de Planning, backlog D05.f, BHV005–010 et MOD006.
- Référence : ELM187 / MKT28 ; source primaire Kinaxis effectivement consultée le 17 septembre 2026.
- Relation : appui méthodologique et recouvrement partiel. Les effets sur la coordination et la réaction aux aléas étayent la distinction recherchée par Laurent.
- Choix FLOW : mécanisme, politique, variante ou bénéfice distinguent les comportements ; construction d’alternatives, simulation et adaptation retenues dans le principe. Les quatre autres éléments de Planning sont requalifiés en fonctions de produits selon U283. Kinaxis ne prescrit ni cette terminologie ni cette séparation.
- Limite et recommandation : un bénéfice générique ne suffit pas à différencier deux comportements ; préciser ce qui change concrètement dans la manière d’agir. Un impact humain peut exister même si la réalisation est automatisée. Ces précisions sont une interprétation proposée par Codex, cohérente avec U265 et les frontières existantes.
- Frontière proposée : adapter le scénario de stock via les décisions D05 ; conserver la décision d’adaptation et l’orchestration opérationnelles D06. Noms et définitions détaillés restent à instruire.
- Auteur/date/statut : Codex, 2026-09-17. Direction U283 adoptée dans sa portée ; correspondance marché proposée, aucune équivalence normative validée.''')
    append('JOURNAL.md', '''## 2026-09-17 — U283 : critères de comportement et Planning

Apport enregistré avant interprétation. AGENTS et glossaire méthodologique précisés ; direction Planning consignée dans les annexes. D05.f et ses six comportements marqués en réexamen ; requalification fonctionnelle BHV007–010 tracée. Aucun nom, définition adoptée, identifiant ou lien supprimé ; migration cible à préciser. Comparaison Kinaxis ELM187/CMP094, sans équivalence normative. Aucune publication.''')
    assert model['relations'] == before['relations']
    old = {n['id']: n for n in before['nodes']}
    assert all(n['fields'] == old[n['id']]['fields'] and n.get('lifecycle') == old[n['id']].get('lifecycle') for n in model['nodes'])
    assert all(sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in protected.items())
    (OUT / 'integrity.json').write_text(json.dumps({'protected_files': protected, 'node_values_and_lifecycle_unchanged': True, 'relations_unchanged': True}, indent=2), encoding='utf-8')
    print('U283 integrated; historical adoptions preserved.')


if __name__ == '__main__':
    main()

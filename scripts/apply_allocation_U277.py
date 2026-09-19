"""Enrich the working Allocation behavior from U276/U277; never publish."""
from pathlib import Path
from hashlib import sha256
import json
from scripts.structured_io import read, dumps
from scripts.apply_planning_U269 import append, cycle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-17-allocation-comportement'


def main():
    if OUT.exists():
        raise SystemExit('U277 already captured; do not reapply.')
    OUT.mkdir()
    for name in ('model', 'behavior-audit'):
        (OUT / f'{name}-before.yaml').write_bytes((ROOT / f'modeles/backlog/{name}.yaml').read_bytes())
    protected = {}
    for folder in ('release', 'revisions', 'decisions', 'provenance'):
        for p in (ROOT / 'modeles' / folder).rglob('*'):
            if p.is_file() and p != ROOT / 'modeles/provenance/source-records.json':
                protected[p.relative_to(ROOT).as_posix()] = sha256(p.read_bytes()).hexdigest()
    (OUT / 'protected.json').write_text(json.dumps(protected, indent=2), encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U277

**id**

U277

**date**

2026-09-17

**titre**

Alimenter les comportements par le détail fonctionnel Microsoft

**texte**

Le détail exposé par Microsoft est très bon. Il doit servir pour alimenter les comportements.

**contexte et portée**

Instruction d’enrichissement concret à partir de la documentation Microsoft Inventory Allocation discutée en U276. Intégrer Allocation sous Supply Protection selon le rattachement U276 et documenter les mécanismes utiles. Les formulations détaillées, exemples, justification et correspondances ajoutés restent proposés ; aucune conversion automatique de chaque API en comportement, aucun niveau supplémentaire, renommage ou release demandé.''')
    append('marche/elements.md', '''### ELM176

- Référence : MKT14, Microsoft Dynamics 365 Supply Chain Management / Inventory Visibility.
- Libellé natif : Inventory Visibility inventory allocation ; fonctionnalités produit et API.
- Source primaire : https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation ; page évolutive, édition non précisée, mise à jour affichée 2025-08-13, consultée le 2026-09-17.
- Passages lus : Business background and purpose ; Allocation definition ; Tips for using allocation ; Use the allocation APIs (Allocate, Unallocate, Reallocate, Consume, Consume as a soft reservation, Query).
- Reformulation : enveloppes par groupes, transfert et restitution de quantités, imputation de consommation et consultation du solde. Allocation logique ; couplage possible avec une réservation, sans identité des deux notions.
- Limites : la source décrit un produit et ses interfaces, pas une hiérarchie de capacités. Elle ne suffit pas à couvrir la prévention du surstock ou les périodes de validité FLOW. Pas de copie des contraintes techniques Microsoft dans le contrat métier.
- Rapprochement proposé : CMP092 ; aucun déploiement Beaumanoir déduit.''')
    append('marche/comparaisons.md', '''## CMP092

- Objet : D02.b Supply Protection et BHV011 Allocation, backlog U276/U277.
- Élément : ELM176 ; approfondissement de la source Microsoft déjà utilisée en ELM168.
- Relation : appui fonctionnel proposé, recouvrement partiel ; aucune équivalence normative.
- Choix FLOW : conserver un comportement Allocation terminal avec plusieurs mécanismes combinables décrits dans son périmètre. Ni un comportement par API, ni des sous-comportements.
- Bénéfice : distinguer gouvernance des enveloppes, consommation de droits et affectation de ressources ; rendre visibles les soldes et éviter de bloquer des ressources par des enveloppes devenues inutiles.
- Frontières : D05.d détermine les valeurs ; D02.e affecte aux besoins ; D02.c porte la réservation. Le point d’imputation et les corrections restent à instruire. Le volet surstock U274 dépasse cette documentation.
- Statut : nom et rattachement Allocation issus de U276 ; descriptions et justification éditoriales proposées sous mandat U277. Auteur : Codex, 2026-09-17. Pas de validation d’équivalence marché.''')
    model = read(ROOT / 'modeles/backlog/model.yaml')
    assert not any(n['id'] == 'BHV011' for n in model['nodes'])
    fields = {
        'name': 'Allocation',
        'definition': 'Établir, modifier ou libérer les enveloppes de quantités et les droits d’usage attribués à des groupes de bénéficiaires, pour un périmètre et une période donnés.',
        'scope': '''Gérer des enveloppes par produit, lieu et groupe de bénéficiaires, par exemple canal, région ou groupe de clients. Les dimensions identifient le périmètre ; elles ne créent pas de nouveaux comportements. La période de validité relève de la convention FLOW, sans la déduire de la seule API Microsoft.

Le détail Microsoft alimente les mécanismes suivants : attribuer une quantité disponible à une enveloppe ; transférer tout ou partie d’une enveloppe à un autre groupe ; libérer une quantité allouée ; imputer la consommation et consulter les quantités allouées, consommées et restantes. Ces mécanismes se combinent dans ce comportement terminal ; ils ne sont ni des sous-comportements ni une séquence imposée. Le partage reste logique et ne commande aucun déplacement physique.

Exemple fictif FLOW : sur 1 000 pièces admissibles, attribuer 300 au web. Une consommation de droits de 80 laisse un solde de 220. Réallouer 50 de ce solde aux magasins laisse 170 au web ; libérer encore 20 laisse 150 et restitue ces 20 au disponible commun. Cela ne prouve ni expédition ni réservation physique. La réallocation peut réduire un déséquilibre entre canaux ; elle ne résorbe pas à elle seule un surstock global.

[Stock Allocation Decision](model:D05.d) détermine les enveloppes à retenir ; Allocation rend les valeurs retenues effectives. [Supply Assignment](model:D02.e) affecte les ressources aux besoins ; [Reservation](model:D02.c) porte l’engagement de quantité. Microsoft permet de coupler consommation et réservation souple ; FLOW doit encore préciser quel fait métier consomme l’enveloppe, comment traiter annulations et corrections et comment éviter une double déduction. Aucun couplage systématique n’est imposé.

La cohérence des périmètres, les quantités consommables et les soldes doivent être contrôlés. Un plafond de consommation et un minimum protégé ont des effets distincts. La gestion des effets partiels en masse, des exceptions et de la concurrence reste à instruire ; écran, batch, flux et streaming sont des modalités d’application possibles, pas des comportements supplémentaires. Les seuils de couverture et la prévention du surstock dans Supply Protection dépassent ce seul comportement.'''
    }
    note = 'Nom et rattachement conceptuel adoptés U276 ; définition, détails Microsoft adaptés, exemple et frontières éditoriales proposés sous mandat U277.'
    node = {'id': 'BHV011', 'revision': 1, 'kind': 'behavior', 'layer': 'transactional', 'fields': fields,
            'source_refs': ['U274', 'U275', 'U276', 'U277', 'CMP092'],
            'source_locator': {'path': 'connaissance/01-contributions-utilisateur.md', 'anchor': 'u276'},
            'review': {'state': 'partial', 'note': note}, 'adoption_ids': [],
            'lifecycle': cycle(fields, ['name'], ['U276'], note)}
    model['nodes'].append(node)
    relation = {'id': 'REL-PROTECTION-BHV011', 'revision': 1, 'type': 'contains', 'source_id': 'D02.b', 'target_id': 'BHV011',
                'source_refs': ['U276'], 'review': {'state': 'accepted', 'note': 'Allocation est un comportement de Supply Protection, U276.'}}
    relation['lifecycle'] = cycle(relation, ['type', 'source_id', 'target_id'], ['U276'], relation['review']['note'])
    model['relations'].append(relation)
    parent = next(n for n in model['nodes'] if n['id'] == 'D02.b')
    parent['fields']['definition'] = 'Configurer et maintenir dans le temps les règles, seuils et quantités qui encadrent l’utilisation et le renouvellement des ressources, afin de maîtriser les risques de pénurie, de surstock et de déséquilibre.'
    parent['fields']['decomposition_rationale'] = 'Distinguer les enveloppes de droits d’usage par bénéficiaire des seuils de couverture : partage, consommation, réallocation et libération demandent un suivi de soldes spécifique. Rendre ces mécanismes explicites aide à éviter des droits surconsommés ou des protections inutilisées, sans confondre décision des valeurs et affectation aux commandes.'
    parent['fields']['scope'] = '''U274 élargit explicitement la protection à la pénurie et au surstock, avec configuration des règles et quantités dans le temps. [Allocation](model:BHV011) précise la gestion des enveloppes ; le catalogue des autres comportements reste à instruire, notamment les seuils de couverture et la validité des règles. La documentation Microsoft utilisée ne couvre pas à elle seule toute cette intention.

Les décisions spécialisées D05 restent distinctes. Programmer une validité dans le temps ne duplique pas la construction, simulation, analyse d’impact, évaluation, validation et application de scénarios d’[Inventory Planning](model:D05.f). Le partage exact de la planification reste à examiner avec Laurent. L’application transactionnelle peut être unitaire, collective ou en masse, via écran, batch, flux ou streaming ; la réalisation physique et l’affectation aux commandes gardent leurs capacités responsables.'''
    parent['source_refs'] += ['U274', 'U275', 'U276', 'U277', 'CMP092']
    parent['review']['note'] += ' U274 précise pénurie et surstock ; U276 adopte Allocation comme comportement. Définition de synthèse, justification et périmètre ajoutés proposés ; nom Supply Protection conservé sans nouvelle adoption.'
    (ROOT / 'modeles/backlog/model.yaml').write_text(dumps(model), encoding='utf-8')
    audit = read(ROOT / 'modeles/backlog/behavior-audit.yaml')
    audit['allocation_U276_U277'] = {
        'state': 'adopted_in_stated_scope', 'source_refs': ['U274', 'U275', 'U276', 'U277', 'CMP092'],
        'parent_id': 'D02.b', 'node_id': 'BHV011', 'relation_id': relation['id'], 'catalog_changed': True,
        'adopted_fields': ['name'], 'value_sha256': node['lifecycle']['value_sha256'],
        'adopted_relation_fields': ['type', 'source_id', 'target_id'],
        'proposed_details': 'Définition et périmètre BHV011 ; définition, scope et decomposition_rationale D02.b. Aucun autre comportement de Protection adopté.',
        'market_comparison': 'CMP092', 'historical_capture': 'audits/2026-09-17-allocation-comportement/model-before.yaml',
        'open_points': ['Fait métier consommant les droits et annulations/corrections', 'Articulation avec Reservation sans double déduction', 'Seuils contre pénurie et surstock', 'Validité et frontières avec Inventory Planning', 'Traitements en masse, exceptions et concurrence']}
    entry = next(e for e in audit['assessments'] if e['capability_id'] == 'D02.b')
    entry['recommendation'] = 'Conserver ; Allocation rattaché U276, enrichi par Microsoft U277 ; autres comportements à instruire'
    entry['source_refs'] += ['U274', 'U276', 'U277', 'CMP092']
    audit['decision_boundary'] += ' U276 adopte le nom et rattachement Allocation sous Supply Protection ; U277 demande son enrichissement. Portées dans allocation_U276_U277.'
    (ROOT / 'modeles/backlog/behavior-audit.yaml').write_text(dumps(audit), encoding='utf-8')
    before = read(OUT / 'model-before.yaml')
    old_nodes = {n['id']: n for n in before['nodes']}
    changed = [n['id'] for n in model['nodes'] if n['id'] in old_nodes and n != old_nodes[n['id']]]
    assert changed == ['D02.b'], changed
    assert model['relations'][:-1] == before['relations']
    assert all(sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in protected.items())
    (OUT / 'integrity.json').write_text(json.dumps({'protected_files_unchanged': len(protected), 'existing_relations_unchanged': len(before['relations']), 'changed_existing_nodes': changed, 'added_node': 'BHV011', 'added_relation': relation['id']}, indent=2), encoding='utf-8')
    print('BHV011 added; only D02.b revised; publications and existing relations unchanged.')


if __name__ == '__main__':
    main()

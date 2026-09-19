"""Apply the bounded U435 interaction corrections once, after root coordination.

This script is prepared by the links audit and deliberately not launched by its
author. It neither publishes nor grants approval. Root applies coordinated model
changes sequentially and runs the final project checks.
"""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps
from scripts.element_versions import content_hash

OUT = Path(__file__).resolve().parent
MODEL = ROOT / 'modeles/backlog/model.yaml'
AVOID_U436 = {'REL-NEEDS-U290-018', 'REL-NEEDS-U290-019', 'REL-NEEDS-U290-025',
              'REL-NEEDS-U290-029', 'REL-NEEDS-U290-030'}
NOTE = ('U435 : correction de lisibilité autorisée dans le nouvel audit V0. '
        'Expression et qualification éditoriales proposées ; aucune validation '
        'métier champ par champ ni flux installé déduits.')

LABELS = {
    'REL-NEEDS-U424-D03.p-D04.o': 'Mobilise les transitions autorisées des Orders',
    'REL-NEEDS-U378-07': 'Applique les affectations du scénario retenu',
    'REL-NEEDS-U290-012': 'Établit la promesse à partir des disponibilités',
    'REL-NEEDS-U290-017': 'Construit la promesse selon l’échéancier retenu',
    'REL-EXECUTION-ADAPTATION-PROMISE-REVISION': 'Fournit les impacts justifiant un réexamen de promesse',
    'REL-EXECUTION-TRACKING-ORCHESTRATION': 'Fournit les faits utiles à la coordination',
    'REL-EXECUTION-ADAPTATION-ORCHESTRATION': 'Fournit la variation retenue à coordonner',
    'REL-EXECUTION-REQUIREMENTS-SERVICE-ORDER': 'Fournit les prestations requises à solliciter',
    'REL-NEEDS-U290-102': 'Met en action les apports achetés retenus',
    'REL-NEEDS-U290-103': 'Met en action les transferts retenus',
    'REL-NEEDS-U385-SUPPLIER-RETURN': 'Mobilise le renvoi fournisseur pour la suite du retour client',
    'REL-NEEDS-U391-DIRECT-SALES': 'Aligne la livraison fournisseur sur l’attendu client',
}

SUPPLEMENTS = [
    ('CONSIGNED-LIFECYCLE', 'D04.r', 'D04.o', 'Mobilise les évolutions autorisées de la demande consignée',
     'Consignment Replenishment Order mobilise Order Lifecycle Management pour gouverner les évolutions autorisées de sa demande, en conservant lignes, quantités et engagements distincts.',
     'Lorsqu’une mutation de la demande est nécessaire et autorisée selon l’accord applicable.',
     'Conserver une demande cohérente sans créer un engagement d’achat ni réaliser la prestation.', ['U395', 'U398']),
    ('CONSIGNED-STRUCTURING', 'D04.r', 'D04.n', 'Conserve la structure et la filiation des apports consignés',
     'Consignment Replenishment Order mobilise Order Structuring pour les découpages et compositions autorisés de la demande, en conservant sa filiation et les quantités concernées.',
     'Si la demande doit être scindée ou intégrée à une composition persistante.',
     'Rendre la structure explicable sans compter deux fois le même apport ni imposer un Order chapeau.', ['U395', 'U398']),
    ('ARCHIVING-CONSIGNED', 'D04.q', 'D04.r', 'Conserve les versions de la demande d’apport consigné',
     'Order Archiving utilise le contenu, les versions et les traces de Consignment Replenishment Order pour assurer leur conservation selon la politique applicable.',
     'Lorsque les demandes ou leurs versions doivent être conservées selon les règles applicables.',
     'Préserver les traces sans reprendre la gestion courante de la demande ni confondre clôture et archivage.', ['U395', 'U398']),
    ('CONSIGNED-TRACKING', 'D01.h', 'D01.f', 'Applique les conditions de consignation au stock connu',
     'Consigned Inventory Management utilise les états de stock connus pour appliquer les conditions de l’accord sur le propriétaire, la détention, les droits d’usage et les échéances.',
     'Stock identifié comme consigné et conditions de l’accord disponibles ; état connu distingué des ressources futures.',
     'Appliquer le régime au bon périmètre sans inventer une réception ou modifier le maître de l’accord.', ['U395', 'U401']),
    ('CONSIGNED-PURCHASE', 'D01.h', 'D04.j', 'Mobilise l’achat applicable à l’acquisition du stock consigné',
     'Consigned Inventory Management mobilise Purchase Order lorsqu’une acquisition autorisée du stock consigné nécessite un acte d’achat, et utilise son résultat pour suivre l’issue de l’accord.',
     'Uniquement si les conditions de l’accord et la suite retenue prévoient un achat ; aucune acquisition automatique à la réception.',
     'Rattacher l’achat éventuel au stock concerné sans assimiler détention et propriété ni absorber la finance.', ['U395', 'U401']),
    ('CONSIGNED-SUPPLIER-RETURN', 'D01.h', 'D04.m', 'Mobilise la reprise fournisseur prévue par la consignation',
     'Consigned Inventory Management mobilise Supplier Return lorsqu’une issue autorisée de la consignation prévoit le renvoi des marchandises au fournisseur.',
     'Lorsque la suite retenue et l’accord permettent une reprise physique fournisseur.',
     'Suivre la reprise via l’Order responsable sans déduire sa réalisation physique du seul choix de sortie.', ['U395', 'U401']),
]


def new_relation(identifier, source, target, label, meaning, conditions, effects, sources, stamp, scope):
    return dict(id=identifier, revision=1, type='relates-to', source_id=source, target_id=target,
                fields={'label': label}, source_refs=list(dict.fromkeys(sources + ['U435'])),
                qualification=dict(role='needs', meaning=meaning, conditions=conditions, effects=effects, scope=scope),
                review=dict(state='proposed', note=NOTE),
                lifecycle=dict(state='under_instruction', recorded_at=stamp, recorded_by='Codex',
                               source_refs=['U435'], validated_fields=[], value_sha256={}, note=NOTE),
                last_modified=stamp)


def build_changes(document, stamp):
    """Pure preparation: returns model and change log without writing any file."""
    result = deepcopy(document)
    nodes = {node['id']: node for node in result['nodes']}
    relations = {relation['id']: relation for relation in result['relations']}
    proposals = read(OUT / 'findings-liens.yaml')['top_six_proposed_links']
    pairs = {(r['source_id'], r['target_id']) for r in result['relations'] if r['type'] == 'relates-to'}
    added = []
    for proposal in proposals:
        identifier = 'REL-AUDIT-U435-' + proposal['proposal_id']
        source, target = proposal['source_id'], proposal['target_id']
        assert source in nodes and target in nodes
        assert identifier not in relations and (source, target) not in pairs, identifier
        scope = ('Consommateur vers fournisseur de résultat métier ; pas de séquence technique imposée. '
                 'Justification dans ' + proposal['finding_id'] + '. '
                 'Précisions restant à instruire : ' + ' ; '.join(proposal['unknowns']) + '.')
        evidence_refs = {
            'PLNK-01': ['U413', 'U417'], 'PLNK-02': ['U410', 'U420'],
            'PLNK-03': ['U395', 'U398', 'U409'], 'PLNK-04': ['U395', 'U401'],
            'PLNK-05': ['U403'], 'PLNK-06': ['U395', 'U398', 'U427'],
        }
        conditions = proposal['conditions']
        if proposal['proposal_id'] == 'PLNK-05':
            conditions = ['Un achat contribue à la satisfaction concernée.',
                          'Distinguer demande, proposition fournisseur et engagement accepté.',
                          'Relier les quantités et échéances concernées.']
        added.append(new_relation(identifier, source, target, proposal['label'], proposal['meaning'],
                                  conditions, proposal['effects'], ['U398', 'U399'] + evidence_refs[proposal['proposal_id']], stamp, scope))
        pairs.add((source, target))
    for suffix, source, target, label, meaning, condition, effect, sources in SUPPLEMENTS:
        identifier = 'REL-AUDIT-U435-' + suffix
        assert source in nodes and target in nodes
        assert identifier not in relations and (source, target) not in pairs, identifier
        added.append(new_relation(identifier, source, target, label, meaning, [condition], [effect], sources, stamp,
                                  'Formalisation d’une interaction décrite dans les scopes de consignation ; '
                                  'règles détaillées et réalisation technique à instruire.'))
        pairs.add((source, target))
    changed = []
    assert not AVOID_U436.intersection(LABELS)
    for identifier, label in LABELS.items():
        relation = relations[identifier]
        assert not relation.get('lifecycle', {}).get('validated_fields'), identifier
        assert not relation.get('fields', {}).get('label'), identifier
        before = deepcopy(relation)
        relation.setdefault('fields', {})['label'] = label
        relation['revision'] += 1
        relation['last_modified'] = stamp
        relation['source_refs'] = list(dict.fromkeys(relation['source_refs'] + ['U435']))
        relation['review']['note'] += ' ' + NOTE
        relation['lifecycle'] = dict(state='under_instruction', recorded_at=stamp, recorded_by='Codex',
                                     source_refs=list(dict.fromkeys(relation.get('lifecycle', {}).get('source_refs', []) + ['U435'])),
                                     validated_fields=[], value_sha256={}, note=NOTE)
        if 'content_sha256' in relation:
            relation['content_sha256'] = content_hash(relation)
        changed.append(dict(id=identifier, before_revision=before['revision'], after_revision=relation['revision'],
                            fields_changed=['fields.label', 'source_refs', 'review.note', 'lifecycle', 'last_modified'],
                            source_id=relation['source_id'], target_id=relation['target_id'], label=label))
    result['relations'].extend(added)
    return result, dict(source='U435', recorded_at=stamp, added_relation_ids=[r['id'] for r in added],
                        labels_added=changed, existing_qualifications_changed=[],
                        avoided_U436_relation_ids=sorted(AVOID_U436),
                        adoption_created=False, publication_created=False)


def main():
    manifest_path = OUT / 'modifications-liens-appliquees.yaml'
    before_path = OUT / 'model-before-link-fixes.yaml'
    if manifest_path.exists() or before_path.exists():
        raise RuntimeError('Le correctif de liens a déjà été préparé/appliqué ici ; aucun rejeu implicite.')
    before_bytes = MODEL.read_bytes()
    model, report = build_changes(read(MODEL), datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'))
    encoded = dumps(model).encode('utf-8')
    report.update(before_sha256=sha256(before_bytes).hexdigest(), after_sha256=sha256(encoded).hexdigest())
    # Refuse a concurrent catalogue edit instead of silently overwriting it.
    if MODEL.read_bytes() != before_bytes:
        raise RuntimeError('Le backlog a changé pendant la préparation ; coordonner avant application.')
    before_path.write_bytes(before_bytes)
    MODEL.write_bytes(encoded)
    manifest_path.write_text(dumps(report), encoding='utf-8')
    print(dumps(report))


if __name__ == '__main__':
    main()

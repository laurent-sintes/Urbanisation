"""Reconcile one revision per U435/U436 edit and verify preserved approvals."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps
from scripts.element_versions import content_hash

OUT = Path(__file__).parent
BASE = OUT / 'model-before-U435.yaml'


def main():
    base = read(BASE)
    current_path = ROOT / 'modeles/backlog/model.yaml'
    current = read(current_path)
    report = {'source_refs': ['U435', 'U436'], 'nodes': [], 'relations': [], 'principles': []}
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    preserved_count = 0
    for collection in ('nodes', 'relations', 'principles'):
        before = {item['id']: item for item in base[collection]}
        now = {item['id']: item for item in current[collection]}
        assert not (before.keys() - now.keys()), (collection, 'Unexpected element removal')
        for identifier, item in now.items():
            old = before.get(identifier)
            if old is None:
                report[collection].append({'id': identifier, 'change': 'added'})
                if collection != 'principles':
                    assert not item.get('lifecycle', {}).get('validated_fields'), identifier
                continue
            old_values = old['fields'] if collection == 'nodes' else old
            new_values = item['fields'] if collection == 'nodes' else item
            for field in old.get('lifecycle', {}).get('validated_fields', []):
                assert old_values[field] == new_values[field], ('Approved value changed', identifier, field)
                assert item['lifecycle']['value_sha256'][field] == old['lifecycle']['value_sha256'][field]
                preserved_count += 1
            if collection == 'nodes':
                assert (item['kind'], item['layer'], item['fields']['name']) == (old['kind'], old['layer'], old['fields']['name'])
            if collection == 'relations':
                for field in ('type', 'source_id', 'target_id'):
                    assert item[field] == old[field], (identifier, field)
            if content_hash(item) == content_hash(old):
                continue
            if collection != 'principles':
                item['revision'] = old.get('revision', 1) + 1
                item['last_modified'] = stamp
                if 'content_sha256' in item:
                    item['content_sha256'] = content_hash(item)
            changed_fields = sorted(k for k in set(old_values) | set(new_values)
                                   if old_values.get(k) != new_values.get(k)
                                   and k not in ('revision', 'last_modified', 'content_sha256'))
            report[collection].append({'id': identifier, 'change': 'updated', 'changed_fields': changed_fields})
    current['source_version'] += ' + U435 préparation V0 et U436 frontière réservation/affectation'
    for entry in current.get('source_files', []):
        entry['sha256'] = sha256((ROOT / entry['path']).read_bytes()).hexdigest()
    current_path.write_text(dumps(current), encoding='utf-8')
    interactions_path = ROOT / 'modeles/backlog/business-interactions.yaml'
    interactions = read(interactions_path)
    interactions['status'] = 'targeted_application_U435'
    interactions['source_refs'] = list(dict.fromkeys(interactions['source_refs'] + ['U434', 'U435', 'U436']))
    interactions['relation_convention']['status'] = 'label_storage_and_display_implemented_U435'
    interactions['relation_convention']['label'] = ('Expression courte source vers cible dans relation.fields.label (verb accepté en compatibilité). '
        'Atlas respecte le libellé explicite aussi pour needs ; agrégats hétérogènes conservent leur famille et leurs relations détaillées.')
    interactions['rollout'] += (' U434 demande explicitement un nouvel audit profond ; U435 autorise les corrections évidentes. '
        'Douze liens proposés et dix-sept libellés de relations existantes sont traités dans ce lot. '
        'La qualification générale des autres liens reste à instruire ; U431 demeure clos.')
    interactions_path.write_text(dumps(interactions), encoding='utf-8')
    report['recorded_at'] = stamp
    report['model_before_sha256'] = sha256(BASE.read_bytes()).hexdigest()
    report['model_after_sha256'] = sha256(current_path.read_bytes()).hexdigest()
    report['previous_validated_values_preserved'] = preserved_count
    report['old_nodes_removed'] = []
    report['old_relations_removed_or_reoriented'] = []
    report['capability_count'] = sum(n['kind'] == 'capability' for n in current['nodes'])
    report['behavior_count'] = sum(n['kind'] == 'behavior' for n in current['nodes'])
    (OUT / 'changes-final.yaml').write_text(dumps(report), encoding='utf-8')
    print(dumps({k: v for k, v in report.items() if k not in ('nodes', 'relations', 'principles')}))
    print('Changed elements:', {k: len(report[k]) for k in ('nodes', 'relations', 'principles')})


if __name__ == '__main__':
    main()

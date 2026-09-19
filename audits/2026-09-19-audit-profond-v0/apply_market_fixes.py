"""Apply reviewed U435 market comparisons only; invoked by the root agent.

Default mode only reports the prepared patch. This file has not been executed
by the market-audit subagent. Element revisions are reconciled by the root.
"""
from copy import deepcopy
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps
from scripts.market_comparison import validate_comparisons


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode('utf-8')).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    plan = read(Path(__file__).with_name('market-fixes.yaml'))
    path = ROOT / 'modeles/backlog/model.yaml'
    original = read(path)
    model = deepcopy(original)
    nodes = {n['id']: n for n in model['nodes']}
    changed, already_applied = [], []
    for op in plan['operations']:
        node = nodes[op['node_id']]
        old = node['fields'].get('market_comparisons')
        new = op['market_comparisons']
        if old == new:
            already_applied.append(node['id'])
            continue
        if 'market_comparisons' in node.get('lifecycle', {}).get('validated_fields', []):
            raise ValueError(f"Champ validé à préserver : {node['id']}/market_comparisons")
        if digest(old) != op['before_market_comparisons_sha256']:
            raise ValueError(f"Rubrique marché changée depuis la préparation : {node['id']}")
        errors = validate_comparisons(new, node['id'] + '/market_comparisons')
        if errors:
            raise ValueError('\n'.join(errors))
        node['fields']['market_comparisons'] = new
        if 'U435' not in node['source_refs']:
            node['source_refs'].append('U435')
        changed.append(node['id'])
    if args.apply and changed:
        contributions = (ROOT / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
        if 'U435' not in contributions:
            raise ValueError('Enregistrer U435 et sa portée avant application du patch marché.')
        # The only model changes above are proposed comparisons and provenance.
        # Revision, source_files and global validation are finalized by the root.
        path.write_text(dumps(model), encoding='utf-8')
    print(json.dumps(dict(applied=args.apply, changed_nodes=changed,
        already_applied_nodes=already_applied,
        new_comparisons=plan['new_comparison_count'],
        updated_flow_positions=plan['updated_flow_position_count'],
        revisions='to_be_reconciled_by_root'), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

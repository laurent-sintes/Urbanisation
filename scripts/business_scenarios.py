"""Optional illustrative scenarios, resolved exclusively inside one model snapshot."""
from copy import deepcopy

LEVELS = {'domain', 'area', 'capability'}


def validate_scenarios(nodes):
    errors = []
    for identifier, node in nodes.items():
        fields = node.get('fields', {})
        seen = set()
        for example in fields.get('examples', []):
            key = example.get('id')
            if key:
                if node['kind'] not in LEVELS:
                    errors.append(f'{identifier}/examples: shared scenarios require a domain, subdomain or capability')
                if key in seen:
                    errors.append(f'{identifier}/examples: duplicate scenario id {key}')
                seen.add(key)
            for contribution in example.get('contributions', []):
                target = nodes.get(contribution['node_id'])
                if not target or target['kind'] not in LEVELS:
                    errors.append(f'{identifier}/examples: invalid contribution {contribution["node_id"]}')
        seen_refs = set()
        for ref in fields.get('scenario_refs', []):
            pair = (ref['node_id'], ref['scenario_id'])
            owner = nodes.get(ref['node_id'])
            if node['kind'] not in LEVELS:
                errors.append(f'{identifier}/scenario_refs: unsupported level')
            if pair in seen_refs or ref['node_id'] == identifier:
                errors.append(f'{identifier}/scenario_refs: duplicate or self reference {pair}')
            seen_refs.add(pair)
            if not owner or owner['kind'] not in LEVELS or not any(
                e.get('id') == ref['scenario_id'] for e in owner.get('fields', {}).get('examples', [])
            ):
                errors.append(f'{identifier}/scenario_refs: missing directly defined scenario {pair}')
    return errors


def scenarios_for_node(node, nodes):
    fields = node.get('fields', {})
    result = deepcopy(fields.get('examples', []))
    for ref in fields.get('scenario_refs', []):
        owner = nodes.get(ref['node_id'], {})
        example = next((e for e in owner.get('fields', {}).get('examples', [])
                        if e.get('id') == ref['scenario_id']), None)
        if example:
            result.append({**deepcopy(example), 'source_node': ref['node_id'], 'contribution': ref['contribution']})
    return result

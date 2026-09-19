"""Business information is a transverse catalogue within one model snapshot."""
try:
    from .market_comparison import validate_comparisons
except ImportError:
    from market_comparison import validate_comparisons


def versioned_items(model):
    catalogue = model.get('information_catalog')
    if not isinstance(catalogue, dict):
        return []
    return [catalogue] + catalogue.get('items', []) + catalogue.get('links', [])


def validate_information(model):
    if 'information_catalog' not in model:
        return []
    catalogue = model['information_catalog']
    if not isinstance(catalogue, dict) or any(not isinstance(catalogue.get(k), list) for k in ('items','links')):
        return ['information_catalog: items and links must be lists']
    errors, items = [], {}
    nodes = {n['id']:n for n in model['nodes']}
    used = set(nodes) | {r['id'] for r in model['relations']}
    for item in [catalogue] + catalogue['items'] + catalogue['links']:
        identifier = item.get('id') if isinstance(item, dict) else None
        if not isinstance(identifier, str) or not identifier.strip() or identifier in used:
            errors.append(f'information_catalog/{identifier}: missing, shared or duplicate identity')
        else:
            used.add(identifier)
    for item in catalogue['items']:
        if not isinstance(item, dict):
            continue
        identifier = item.get('id')
        items[identifier] = item
        roles = item.get('capability_roles')
        if not isinstance(roles, list) or not roles:
            errors.append(f'information_catalog/{identifier}: at least one capability role required')
            continue
        seen = set()
        for role in roles:
            target = role.get('capability_ref') if isinstance(role, dict) else None
            node = nodes.get(target, {})
            if node.get('kind') != 'capability' or node.get('review', {}).get('state') == 'illustration':
                errors.append(f'information_catalog/{identifier}: unknown or nonpublishable capability {target}')
            if target in seen:
                errors.append(f'information_catalog/{identifier}: repeated capability role {target}')
            seen.add(target)
        if 'market_comparisons' in item:
            errors.extend(validate_comparisons(item['market_comparisons'], f'information_catalog/{identifier}/market_comparisons'))
    for link in catalogue['links']:
        if not isinstance(link, dict):
            continue
        if link.get('from_ref') not in items or link.get('to_ref') not in items:
            errors.append(f'information_catalog/{link.get("id")}: dangling information link')
        if link.get('from_ref') == link.get('to_ref'):
            errors.append(f'information_catalog/{link.get("id")}: self link does not explain two distinct information concepts')
    return errors

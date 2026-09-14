/** Pure, read-only projection: published Atlas identifiers remain the authority. */
export function projectLikeC4(raw, descriptor) {
  const nodes = new Map(raw.nodes.map(node => [node.id, node]));
  if (nodes.size !== raw.nodes.length) throw new Error('Duplicate published node id');
  const structural = raw.relations.filter(relation => ['contains', 'presents'].includes(relation.type));
  const transverse = raw.relations.filter(relation => !['contains', 'presents'].includes(relation.type));
  const parentById = new Map();
  const childrenById = new Map();
  for (const relation of structural) {
    if (!nodes.has(relation.source_id) || !nodes.has(relation.target_id)) throw new Error(`Unknown endpoint: ${relation.id}`);
    if (parentById.has(relation.target_id)) throw new Error(`LikeC4 trial requires an unambiguous presentation parent: ${relation.target_id}`);
    parentById.set(relation.target_id, relation);
    const children = childrenById.get(relation.source_id) ?? [];
    children.push(relation.target_id);
    childrenById.set(relation.source_id, children);
  }
  // UTF-8 hex is bijective, unlike replacing punctuation with underscores.
  const localId = id => `n_${Buffer.from(id, 'utf8').toString('hex')}`;
  const atlasToLikeC4 = {};
  const fqn = (id, ancestors = new Set()) => {
    if (atlasToLikeC4[id]) return atlasToLikeC4[id];
    if (ancestors.has(id)) throw new Error(`Cyclic hierarchy: ${id}`);
    const next = new Set([...ancestors, id]);
    const parent = parentById.get(id);
    return atlasToLikeC4[id] = parent ? `${fqn(parent.source_id, next)}.${localId(id)}` : localId(id);
  };
  for (const id of nodes.keys()) fqn(id);
  const quote = value => JSON.stringify(String(value ?? ''));
  const text = value => typeof value === 'string' ? value : Array.isArray(value) ? value.join(' · ') : '';
  const stateLabel = state => ({ accepted: 'Validé dans sa portée', partial: 'Partiellement validé', proposed: 'Non validé', under_review: 'En réexamen' }[state] ?? state ?? 'Statut non renseigné');
  const kindOf = node => node.kind === 'group' ? (node.group_role === 'urbanism_level' ? (node.level_ref === 'universe' ? 'universe' : 'urbanismLevel') : 'presentation') : node.kind;
  const kindLabel = node => ({ universe: 'Univers', urbanismLevel: `Niveau d’urbanisme · ${node.level_ref ?? 'non nommé'}`, presentation: 'Groupe de présentation', domain: 'Domaine', capability: 'Capacité', reference: 'Référence', object: 'Objet métier', document: 'Document', event: 'Événement' }[kindOf(node)] ?? node.kind);
  const kinds = [...new Set(raw.nodes.map(kindOf))];
  const relationKinds = Object.fromEntries([...new Set(transverse.map(r => r.type))].map(type => [type, `r_${Buffer.from(type).toString('hex')}`]));
  const lines = [
    '// GENERATED from the selected published JSON. Do not edit; regenerate.',
    '// Nesting is a visual projection of explicit contains/presents; their source type is preserved.',
    'specification {',
    ...kinds.map(kind => `  element ${kind} { style { color ${kind === 'presentation' ? 'muted' : kind === 'capability' ? 'primary' : 'indigo'}\n    border ${kind === 'presentation' ? 'dotted' : 'solid'}\n    size medium } }`),
    ...Object.values(relationKinds).map(kind => `  relationship ${kind}`),
    '}', 'model {',
  ];
  function renderNode(id, depth) {
    const node = nodes.get(id);
    const parent = parentById.get(id);
    const indent = '  '.repeat(depth);
    const definition = text(node.fields.definition);
    const purpose = text(node.fields.finality) || text(node.fields.purpose) || definition;
    const summary = purpose.length > 155 ? `${purpose.slice(0, 152).trimEnd()}…` : purpose;
    lines.push(`${indent}${localId(id)} = ${kindOf(node)} ${quote(node.fields.name ?? id)} {`);
    lines.push(`${indent}  summary ${quote(summary)}`);
    lines.push(`${indent}  description ${quote(definition)}`);
    lines.push(`${indent}  technology ${quote(`${kindLabel(node)} · ${stateLabel(node.review?.state)}`)}`);
    lines.push(`${indent}  metadata { atlasId ${quote(id)}\n${indent}    reviewState ${quote(node.review?.state)}\n${indent}    sourceRefs ${quote(JSON.stringify(node.source_refs ?? []))}`);
    if (parent) lines.push(`${indent}    parentRelationId ${quote(parent.id)}\n${indent}    parentRelationType ${quote(parent.type)}`);
    lines.push(`${indent}  }`);
    for (const child of childrenById.get(id) ?? []) renderNode(child, depth + 1);
    lines.push(`${indent}}`);
  }
  for (const id of nodes.keys()) if (!parentById.has(id)) renderNode(id, 1);
  for (const relation of transverse) {
    if (!nodes.has(relation.source_id) || !nodes.has(relation.target_id)) throw new Error(`Unknown endpoint: ${relation.id}`);
    const meaning = relation.qualification?.meaning || text(relation.fields?.label) || relation.type;
    lines.push(`  ${fqn(relation.source_id)} -[${relationKinds[relation.type]}]-> ${fqn(relation.target_id)} ${quote(`${relation.type} · ${stateLabel(relation.review?.state)}`)} {`);
    lines.push(`    description ${quote(meaning)}`);
    lines.push(`    metadata { atlasRelationId ${quote(relation.id)}\n      atlasRelationType ${quote(relation.type)}\n      reviewState ${quote(relation.review?.state)}\n      qualification ${quote(JSON.stringify(relation.qualification ?? {}))}\n      sourceRefs ${quote(JSON.stringify(relation.source_refs ?? []))} }`);
    lines.push('    style { color amber\n      line dashed }', '  }');
  }
  lines.push('}', 'views {', '  view index {', '    title "Urbanisation publiée"', '    include *', '    autoLayout LeftRight', '  }');
  const mapViewByAtlasId = {};
  const relationViewByAtlasId = {};
  const atlasIdByView = {};
  const viewNodes = {};
  for (const node of raw.nodes) {
    const id = node.id;
    const mapView = `map_${localId(id)}`;
    mapViewByAtlasId[id] = mapView;
    atlasIdByView[mapView] = id;
    const visible = childrenById.get(id)?.length ? childrenById.get(id) : [id];
    viewNodes[mapView] = visible;
    lines.push(`  view ${mapView} of ${fqn(id)} {`, `    title ${quote(node.fields.name ?? id)}`, `    include ${visible.map(visibleId => fqn(visibleId)).join(', ')}`, '    autoLayout LeftRight', '  }');
    const relationView = `relations_${localId(id)}`;
    relationViewByAtlasId[id] = relationView;
    atlasIdByView[relationView] = id;
    const neighbors = new Set([id]);
    for (const relation of transverse) {
      if (relation.source_id === id || relation.target_id === id) {
        neighbors.add(relation.source_id);
        neighbors.add(relation.target_id);
      }
    }
    viewNodes[relationView] = [...neighbors];
    lines.push(`  view ${relationView} {`, `    title ${quote(`Relations · ${node.fields.name ?? id}`)}`, `    include ${[...neighbors].map(neighborId => fqn(neighborId)).join(', ')}`, '    autoLayout LeftRight', '  }');
  }
  lines.push('}');
  const likeC4ToAtlas = Object.fromEntries(Object.entries(atlasToLikeC4).map(([id, projected]) => [projected, id]));
  if (Object.keys(likeC4ToAtlas).length !== nodes.size) throw new Error('LikeC4 identifier collision');
  return {
    dsl: `${lines.join('\n')}\n`,
    manifest: {
      publication: descriptor.version,
      modelSha256: descriptor.sha256,
      atlasToLikeC4, likeC4ToAtlas, mapViewByAtlasId, relationViewByAtlasId, atlasIdByView, viewNodes,
      structuralRelations: structural.map(relation => ({ id: relation.id, type: relation.type, sourceId: relation.source_id, targetId: relation.target_id })),
      transverseRelations: transverse.map(relation => ({ id: relation.id, type: relation.type, sourceId: relation.source_id, targetId: relation.target_id })),
    },
  };
}

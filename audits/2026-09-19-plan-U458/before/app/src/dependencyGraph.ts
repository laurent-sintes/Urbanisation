import type { AtlasNode, AtlasRelation, PublishedModel } from './types.ts';
import { isStructural } from './model.ts';

export type DependencyLevel = 'capability' | 'domain' | 'universe';
export type DependencyFamily = 'needs' | 'other';

export interface DependencyOptions {
  level: DependencyLevel;
  focusId?: string;
  /** 0 displays the whole supplied publication; otherwise a breadth-first neighborhood. */
  depth: 0 | 1 | 2 | 3;
  direction: 'both' | 'incoming' | 'outgoing';
  family: 'all' | DependencyFamily;
}

export interface DependencyNode {
  id: string;
  item: AtlasNode;
  /** Endpoint IDs after behavior-to-capability projection, before visual grouping. */
  memberIds: string[];
  internalRelationIds: string[];
}

export interface DependencyEdge {
  id: string;
  source: string;
  target: string;
  label: string;
  family: DependencyFamily;
  count: number;
  relationIds: string[];
}

export interface DependencyProjection {
  nodes: DependencyNode[];
  edges: DependencyEdge[];
  /** Original objects from this publication, including their original behavior endpoints. */
  relations: AtlasRelation[];
  stats: {
    totalRelations: number;
    visibleRelations: number;
    internalRelations: number;
    /** Business endpoints before visual grouping, including isolated capabilities. */
    totalNodes: number;
    visibleNodes: number;
  };
  hiddenRelationCount: number;
}

type EndpointRelation = { relation: AtlasRelation; source: string; target: string; family: DependencyFamily };
const isUniverse = (node: AtlasNode): boolean => node.levelRef === 'universe';
const isGrouping = (node: AtlasNode): boolean => ['group', 'domain', 'reference'].includes(node.kind) || isUniverse(node);
const familyOf = (relation: AtlasRelation): DependencyFamily => relation.qualification.role === 'needs' ? 'needs' : 'other';

/**
 * Pure read-only projection of one verified publication. No relation is inferred from
 * identifiers, names, layers, labels, or the backlog. Business cycles are permitted.
 * Direction restricts the traversal; the resulting graph shows every original direct
 * relation between the reached endpoints, in its original direction.
 */
export function projectDependencies(model: PublishedModel, options: DependencyOptions): DependencyProjection {
  if (!['capability', 'domain', 'universe'].includes(options.level)) throw new Error('Niveau de dépendances inconnu.');
  if (![0, 1, 2, 3].includes(options.depth)) throw new Error('La profondeur doit être 0, 1, 2 ou 3.');
  if (!['both', 'incoming', 'outgoing'].includes(options.direction)) throw new Error('Sens de parcours inconnu.');
  if (!['all', 'needs', 'other'].includes(options.family)) throw new Error('Famille de relations inconnue.');
  if (options.focusId && !model.nodeById.has(options.focusId)) throw new Error(`Nœud de focalisation absent : ${options.focusId}.`);

  // adaptPublication already guarantees an unambiguous, acyclic structural hierarchy.
  const parents = new Map<string, AtlasRelation>();
  const children = new Map<string, string[]>();
  for (const relation of model.relations.filter(isStructural)) {
    parents.set(relation.targetId, relation);
    const siblings = children.get(relation.sourceId) ?? [];
    siblings.push(relation.targetId);
    children.set(relation.sourceId, siblings);
  }

  function node(id: string): AtlasNode {
    const item = model.nodeById.get(id);
    if (!item) throw new Error(`Extrémité absente de la publication : ${id}.`);
    return item;
  }

  function endpoint(id: string): string {
    if (node(id).kind !== 'behavior') return id;
    const parent = parents.get(id);
    if (parent?.type !== 'contains' || node(parent.sourceId).kind !== 'capability') {
      throw new Error(`Comportement sans parent capacité explicite : ${id}.`);
    }
    return parent.sourceId;
  }

  function ancestor(id: string, predicate: (item: AtlasNode) => boolean): string | undefined {
    let cursor: string | undefined = id;
    const seen = new Set<string>();
    while (cursor !== undefined) {
      if (seen.has(cursor)) throw new Error(`Cycle de rattachement explicite : ${cursor}.`);
      seen.add(cursor);
      if (predicate(node(cursor))) return cursor;
      cursor = parents.get(cursor)?.sourceId;
    }
    return undefined;
  }

  function displayedId(id: string): string {
    if (options.level === 'capability') return id;
    if (options.level === 'domain') {
      return ancestor(id, item => item.kind === 'domain' || item.kind === 'reference') ?? id;
    }
    // In particular, an unattached object/document/event does not acquire a universe.
    return ancestor(id, isUniverse) ?? id;
  }

  const allRelations: EndpointRelation[] = model.relations.filter(relation => !isStructural(relation)).map(relation => ({
    relation, source: endpoint(relation.sourceId), target: endpoint(relation.targetId), family: familyOf(relation),
  }));
  const endpointIds = new Set(allRelations.flatMap(relation => [relation.source, relation.target]));
  // Direct historical links between domains/references retain those endpoints. They
  // must never be copied onto their capabilities. Other leaf kinds retain their nature.
  const allNodeIds = new Set(model.nodes.filter(item => item.kind !== 'behavior'
    && (!isGrouping(item) || endpointIds.has(item.id))).map(item => item.id));
  const filtered = allRelations.filter(relation => options.family === 'all' || relation.family === options.family);
  let visible = new Set(allNodeIds);
  const focus = options.focusId ? node(options.focusId) : undefined;
  const full = options.depth === 0 || !focus;

  if (!full && focus) {
    const seeds = new Set<string>();
    if (isGrouping(focus)) {
      const pending = [focus.id];
      const seen = new Set<string>();
      while (pending.length) {
        const id = pending.shift()!;
        if (seen.has(id)) continue;
        seen.add(id);
        if (allNodeIds.has(id)) seeds.add(id);
        pending.push(...children.get(id) ?? []);
      }
      // Selecting an empty group still gives a visible, inspectable focus.
      if (!seeds.size) seeds.add(focus.id);
    } else {
      seeds.add(endpoint(focus.id));
    }
    visible = seeds;
    let frontier = new Set(seeds);
    for (let step = 0; step < options.depth; step += 1) {
      const next = new Set<string>();
      for (const relation of filtered) {
        if (options.direction !== 'incoming' && frontier.has(relation.source) && !visible.has(relation.target)) next.add(relation.target);
        if (options.direction !== 'outgoing' && frontier.has(relation.target) && !visible.has(relation.source)) next.add(relation.source);
      }
      next.forEach(id => visible.add(id));
      frontier = next;
      if (!frontier.size) break;
    }
  }

  const chosen = filtered.filter(relation => visible.has(relation.source) && visible.has(relation.target));
  const display = new Map<string, DependencyNode>();
  function ensureNode(id: string): DependencyNode {
    const current = display.get(id);
    if (current) return current;
    const item = { id, item: node(id), memberIds: [], internalRelationIds: [] };
    display.set(id, item);
    return item;
  }
  // The publication's order provides a deterministic projection for every renderer.
  for (const item of model.nodes) {
    if (visible.has(item.id)) ensureNode(displayedId(item.id)).memberIds.push(item.id);
  }
  if (full && options.level === 'domain') {
    for (const item of model.nodes.filter(item => item.kind === 'domain' || item.kind === 'reference')) ensureNode(item.id);
  }
  if (full && options.level === 'universe') {
    for (const item of model.nodes.filter(isUniverse)) ensureNode(item.id);
  }
  if (!full && focus && isGrouping(focus) && !display.size) ensureNode(focus.id);

  const buckets = new Map<string, { edge: DependencyEdge; relations: AtlasRelation[] }>();
  let internalRelations = 0;
  for (const entry of chosen) {
    const source = displayedId(entry.source);
    const target = displayedId(entry.target);
    if (source === target) {
      ensureNode(source).internalRelationIds.push(entry.relation.id);
      internalRelations += 1;
      continue;
    }
    const key = JSON.stringify([source, target, entry.family]);
    let bucket = buckets.get(key);
    if (!bucket) {
      bucket = {
        edge: {
          id: `dependency:${encodeURIComponent(source)}|${encodeURIComponent(target)}|${entry.family}`,
          source, target, family: entry.family,
          label: entry.family === 'needs' ? 'A besoin de' : 'Relation métier',
          count: 0, relationIds: [],
        },
        relations: [],
      };
      buckets.set(key, bucket);
    }
    bucket.edge.relationIds.push(entry.relation.id);
    bucket.edge.count += 1;
    bucket.relations.push(entry.relation);
  }
  const edges = [...buckets.values()].map(({ edge, relations }) => {
    // A normalized label is not invented from the prose qualification. Multiple
    // distinct descriptions remain in the original relations available to the UI.
    // An explicit business expression also describes a needs relation without
    // changing its consumer-to-provider direction or its semantic family.
    const label = relations[0].label;
    if (label && relations.every(relation => relation.label === label && relation.label !== relation.type)) edge.label = label;
    return edge;
  });
  return {
    nodes: [...display.values()],
    edges,
    relations: chosen.map(entry => entry.relation),
    stats: {
      totalRelations: allRelations.length,
      visibleRelations: chosen.length,
      internalRelations,
      totalNodes: allNodeIds.size,
      visibleNodes: [...visible].filter(id => allNodeIds.has(id)).length,
    },
    hiddenRelationCount: allRelations.length - chosen.length,
  };
}

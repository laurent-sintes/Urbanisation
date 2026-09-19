import type {
  AtlasNode, AtlasRelation, GraphProjection, JsonRecord, NeighborhoodOptions,
  PublishedModel, RawPublication, StructuralRelationType,
} from './types.ts';

import { plainInlineText } from './inlineLinks.ts';
const structuralTypes = new Set<string>(['contains', 'presents']);
export const isStructural = (relation: AtlasRelation): boolean => structuralTypes.has(relation.type);

export function textField(value: unknown): string {
  if (typeof value === 'string') return value;
  if (Array.isArray(value)) return value.filter(item => typeof item === 'string').join('\n');
  return '';
}

function freezeDeep<T>(value: T): T {
  if (value && typeof value === 'object' && !Object.isFrozen(value)) {
    for (const child of Object.values(value)) freezeDeep(child);
    Object.freeze(value);
  }
  return value;
}

function uniqueMap<T extends { id: string }>(items: readonly T[], label: string): Map<string, T> {
  const index = new Map<string, T>();
  for (const item of items) {
    if (typeof item.id !== 'string' || !item.id.trim() || index.has(item.id)) {
      throw new Error(`${label} : identifiant absent ou dupliqué (${item.id}).`);
    }
    index.set(item.id, item);
  }
  return index;
}

/** Accept an API response or the raw snapshot loaded by load-publication.mjs. */
export function adaptPublication(input: RawPublication): PublishedModel {
  if (!input || input.space !== 'release' || !input.version || !Array.isArray(input.nodes) || !Array.isArray(input.relations)) {
    throw new Error('Une publication release explicite avec nodes et relations est requise.');
  }
  // Cloning prevents either renderer from altering the API response or another view.
  const raw = freezeDeep(structuredClone(input));
  const nodes: AtlasNode[] = raw.nodes.map(node => {
    const fields = node.fields ?? {};
    return freezeDeep({
      id: node.id, name: plainInlineText(textField(fields.name)) || node.id, kind: node.kind,
      groupRole: node.group_role, levelRef: node.level_ref, layer: node.layer,
      revision: node.revision, lastModified: node.last_modified,
      purpose: textField(fields.finality), definition: textField(fields.definition), scope: textField(fields.scope),
      fields, review: node.review ?? {}, lifecycle: node.lifecycle,
      status: node.review?.state ?? 'unknown',
      fieldStatus: node.field_status ?? node.field_review ?? {},
      approvedFields: node.approved_fields ?? [], proposedFields: node.proposed_fields ?? [],
      adoptionIds: node.adoption_ids ?? [], sourceRefs: node.source_refs ?? [],
      sourceLocator: node.source_locator, raw: node,
    });
  });
  const nodeById = uniqueMap(nodes, 'Nœud');
  const glossary = raw.glossary?.terms ?? [];
  if (!Array.isArray(glossary)) throw new Error('Glossaire publié invalide.');
  const glossaryById = uniqueMap(glossary, 'Terme');
  const relations: AtlasRelation[] = raw.relations.map(relation => {
    if (!nodeById.has(relation.source_id) || !nodeById.has(relation.target_id)) {
      throw new Error(`Extrémité inconnue pour la relation ${relation.id}.`);
    }
    return freezeDeep({
      id: relation.id, sourceId: relation.source_id, targetId: relation.target_id,
      type: relation.type, revision: relation.revision, lastModified: relation.last_modified,
      label: textField(relation.fields?.label) || textField(relation.fields?.verb) || relation.type,
      qualification: relation.qualification ?? {}, fields: relation.fields ?? {},
      review: relation.review ?? {}, lifecycle: relation.lifecycle,
      status: relation.review?.state ?? 'unknown', fieldStatus: relation.field_status ?? relation.field_review ?? {},
      approvedFields: relation.approved_fields ?? [], proposedFields: relation.proposed_fields ?? [],
      adoptionIds: relation.adoption_ids ?? [], sourceRefs: relation.source_refs ?? [],
      sourceLocator: relation.source_locator, raw: relation,
    });
  });
  const relationById = uniqueMap(relations, 'Relation');
  // An ambiguous/cyclic hierarchy cannot be resolved by guessing from identifiers.
  const parentByChild = new Map<string, string>();
  for (const relation of relations.filter(isStructural)) {
    if (parentByChild.has(relation.targetId)) throw new Error(`Plusieurs parents explicites pour ${relation.targetId}.`);
    parentByChild.set(relation.targetId, relation.sourceId);
  }
  for (const node of nodes) {
    if (node.kind === 'behavior') {
      const parent = nodeById.get(parentByChild.get(node.id) ?? '');
      const relation = relations.find(edge => isStructural(edge) && edge.targetId === node.id);
      if (parent?.kind !== 'capability' || relation?.type !== 'contains' || parent.layer !== node.layer) {
        throw new Error(`Comportement sans rattachement unique à une capacité de même couche : ${node.id}.`);
      }
      if (relations.some(edge => isStructural(edge) && edge.sourceId === node.id)) {
        throw new Error(`Un comportement est un niveau terminal : ${node.id}.`);
      }
    }
    const seen = new Set<string>();
    let cursor: string | undefined = node.id;
    while (cursor !== undefined) {
      if (seen.has(cursor)) throw new Error(`Cycle de navigation explicite à ${cursor}.`);
      seen.add(cursor);
      cursor = parentByChild.get(cursor);
    }
  }
  return Object.freeze({
    version: raw.version, revision: raw.revision, sourcePath: raw.sourcePath,
    publication: Object.freeze({ version: raw.version, revision: raw.revision, sourcePath: raw.sourcePath }),
    nodes: Object.freeze(nodes), relations: Object.freeze(relations), nodeById, relationById,
    glossary: Object.freeze(glossary), glossaryById,
    sourceReferences: raw.sourceReferences ?? {}, limitations: raw.limitations ?? [], raw,
  });
}

export function structuralRelations(model: PublishedModel, type?: StructuralRelationType): AtlasRelation[] {
  return model.relations.filter(relation => type ? relation.type === type : isStructural(relation));
}

export function childrenOf(model: PublishedModel, id: string, type?: StructuralRelationType): AtlasNode[] {
  return structuralRelations(model, type).filter(relation => relation.sourceId === id).map(relation => model.nodeById.get(relation.targetId)!);
}

export function parentsOf(model: PublishedModel, id: string, type?: StructuralRelationType): AtlasNode[] {
  return structuralRelations(model, type).filter(relation => relation.targetId === id).map(relation => model.nodeById.get(relation.sourceId)!);
}

export function parentRelationOf(model: PublishedModel, id: string): AtlasRelation | undefined {
  return model.relations.find(relation => isStructural(relation) && relation.targetId === id);
}

export function rootsOf(model: PublishedModel): AtlasNode[] {
  const children = new Set(structuralRelations(model).map(relation => relation.targetId));
  return model.nodes.filter(node => !children.has(node.id));
}

/** Domain/reference cards expose their capabilities without changing the navigation hierarchy. */
export function hasCapabilityCards(model: PublishedModel, scopeId?: string): boolean {
  const visible = scopeId ? childrenOf(model, scopeId) : rootsOf(model);
  return visible.some(node => node.kind === 'domain' || node.kind === 'reference'
    || (node.kind === 'capability' && childrenOf(model, node.id).some(child => child.kind === 'behavior')));
}

/** Returns explicit ancestors followed by the selected node. A presentation group stays a group. */
export function lineageOf(model: PublishedModel, id: string): AtlasNode[] {
  const result: AtlasNode[] = [];
  let node = model.nodeById.get(id);
  while (node) {
    result.unshift(node);
    node = parentsOf(model, node.id)[0];
  }
  return result;
}

export function descendantsOf(model: PublishedModel, id: string): AtlasNode[] {
  const result: AtlasNode[] = [];
  const queue = childrenOf(model, id);
  while (queue.length) {
    const node = queue.shift()!;
    result.push(node);
    queue.push(...childrenOf(model, node.id));
  }
  return result;
}

const normalize = (value: string) => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('fr');
function fieldText(fields: JsonRecord): string {
  // Search only values actually present in the selected publication.
  return searchableText(fields);
}

export function searchableText(value: unknown): string {
  if (typeof value === 'string') return value;
  if (Array.isArray(value)) return value.map(searchableText).join(' ');
  if (value && typeof value === 'object') return Object.values(value).map(searchableText).join(' ');
  return '';
}

export function searchModel(model: PublishedModel, query: string): AtlasNode[] {
  const words = normalize(query).trim().split(/\s+/).filter(Boolean);
  if (!words.length) return [...model.nodes];
  return model.nodes.filter(node => {
    const haystack = normalize(`${node.id} ${node.kind} ${plainInlineText(fieldText(node.fields))} ${lineageOf(model, node.id).map(parent => parent.name).join(' ')}`);
    return words.every(word => haystack.includes(word));
  });
}

export function relatedTo(model: PublishedModel, id: string, includeStructural = false): AtlasRelation[] {
  return model.relations.filter(relation => (includeStructural || !isStructural(relation)) && (relation.sourceId === id || relation.targetId === id));
}

/** Breadth-first local exploration. Traversing an edge never changes its published direction. */
export function neighborhood(model: PublishedModel, id: string, options: NeighborhoodOptions = {}): GraphProjection {
  if (!model.nodeById.has(id)) throw new Error(`Nœud de focalisation absent : ${id}.`);
  const depth = options.depth ?? 1;
  const direction = options.direction ?? 'both';
  if (![1, 2].includes(depth)) throw new Error('La profondeur du voisinage doit être 1 ou 2.');
  const eligible = model.relations.filter(relation =>
    (options.includeStructural || !isStructural(relation)) &&
    (!options.relationTypes?.length || options.relationTypes.includes(relation.type)),
  );
  const visible = new Set([id]);
  const traversed = new Set<string>();
  let frontier = new Set([id]);
  for (let step = 0; step < depth; step++) {
    const next = new Set<string>();
    for (const relation of eligible) {
      if (direction !== 'incoming' && frontier.has(relation.sourceId)) {
        traversed.add(relation.id);
        if (!visible.has(relation.targetId)) next.add(relation.targetId);
      }
      if (direction !== 'outgoing' && frontier.has(relation.targetId)) {
        traversed.add(relation.id);
        if (!visible.has(relation.sourceId)) next.add(relation.sourceId);
      }
    }
    next.forEach(nodeId => visible.add(nodeId));
    frontier = next;
  }
  const relations = eligible.filter(relation => traversed.has(relation.id));
  const hiddenRelationCount = eligible.filter(relation => !traversed.has(relation.id) && (visible.has(relation.sourceId) || visible.has(relation.targetId))).length;
  return { focusId: id, mode: 'neighborhood', nodes: model.nodes.filter(node => visible.has(node.id)), relations, hiddenRelationCount };
}

/** A semantic step displays only explicit children, or the local business links of a leaf. */
export function focusGraph(model: PublishedModel, id?: string, options: NeighborhoodOptions = {}): GraphProjection {
  if (!id) return { mode: 'hierarchy', nodes: rootsOf(model), relations: [], hiddenRelationCount: 0 };
  const relation = model.relationById.get(id);
  if (relation) {
    return { focusId: id, mode: 'neighborhood', nodes: [model.nodeById.get(relation.sourceId)!, model.nodeById.get(relation.targetId)!], relations: [relation], hiddenRelationCount: 0 };
  }
  const children = childrenOf(model, id);
  if (!children.length) return neighborhood(model, id, options);
  const ids = new Set([id, ...children.map(node => node.id)]);
  const relations = model.relations.filter(edge => ids.has(edge.sourceId) && ids.has(edge.targetId));
  return {
    focusId: id, mode: 'hierarchy', nodes: [model.nodeById.get(id)!, ...children], relations,
    hiddenRelationCount: model.relations.filter(edge => !isStructural(edge) && (ids.has(edge.sourceId) || ids.has(edge.targetId)) && !(ids.has(edge.sourceId) && ids.has(edge.targetId))).length,
  };
}

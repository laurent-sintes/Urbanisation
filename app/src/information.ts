import type { BusinessInformation, PublishedModel } from './types.ts';
import { marketSearchText, marketText } from './marketContent.ts';

/** Only explicit containment/presentation connects a perimeter to its capabilities. */
export function informationForNode(model: PublishedModel, nodeId?: string): readonly BusinessInformation[] {
  if (!nodeId) return model.information;
  const node = model.nodeById.get(nodeId);
  if (!node || node.kind === 'behavior') return [];
  const ids = new Set([nodeId]);
  const queue = [nodeId];
  for (let i = 0; i < queue.length; i++) {
    for (const relation of model.relations) {
      if (['contains', 'presents'].includes(relation.type) && relation.sourceId === queue[i] && !ids.has(relation.targetId)) {
        ids.add(relation.targetId); queue.push(relation.targetId);
      }
    }
  }
  return model.information.filter(item => item.capability_roles.some(role => ids.has(role.capability_ref)));
}

/** Public prose only: no review notes, source IDs, audit questions or backlog paths. */
export function informationSearchText(item: BusinessInformation): string {
  return [item.label_fr, item.question, item.definition, item.context, ...item.essential_elements,
    ...item.boundaries, ...item.capability_roles.flatMap(role => [role.role, role.meaning]),
    ...item.examples.flatMap(example => [example.title, example.situation, example.outcome || '', example.lesson || '']),
    marketSearchText(item.market_comparisons)].map(value => marketText(value)).join('\n');
}

export function informationHref(model: PublishedModel, id = '', node = ''): string {
  const params = new URLSearchParams({ version: model.version, view: 'information' });
  if (id) params.set('information', id);
  if (node) params.set('node', node);
  return '#' + params;
}

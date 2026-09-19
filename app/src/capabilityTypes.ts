import type { AtlasNode } from './types.ts';

/** Explicit published nature only; names and identifiers never determine the type. */
export const capabilityTypes = {
  action: { label: 'Action', icon: 'Zap' },
  management: { label: 'Gestion', icon: 'SlidersHorizontal' },
  knowledge: { label: 'Connaissance / visibilité', icon: 'Eye' },
  orchestration: { label: 'Orchestration', icon: 'Workflow' },
  planning: { label: 'Planification', icon: 'CalendarCheck' },
  decision: { label: 'Décision', icon: 'GitBranch' },
} as const;
export type CapabilityNature = keyof typeof capabilityTypes;

export function capabilityNature(node: AtlasNode): CapabilityNature | undefined {
  const nature = node.fields.nature;
  return node.kind === 'capability' && typeof nature === 'string'
    && Object.hasOwn(capabilityTypes, nature) ? nature as CapabilityNature : undefined;
}

export function capabilityTypeLabel(node: AtlasNode): string {
  const nature = capabilityNature(node);
  return nature ? capabilityTypes[nature].label : 'Type non renseigné';
}

export const isDecision = (node: AtlasNode): boolean => capabilityNature(node) === 'decision';

/** Stable partition: keep the relative order inside both parts and preserve the input. */
export function decisionsLast(nodes: readonly AtlasNode[]): AtlasNode[] {
  return [...nodes.filter(node => !isDecision(node)), ...nodes.filter(isDecision)];
}

/** One boundary only, and only if both capability groups exist. */
export function startsDecisionSection(nodes: readonly AtlasNode[], index: number): boolean {
  return index > 0 && isDecision(nodes[index]) && !isDecision(nodes[index - 1])
    && nodes.slice(0, index).some(node => node.kind === 'capability' && !isDecision(node));
}

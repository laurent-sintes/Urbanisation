import type { AtlasNode } from './types.ts';

export const behaviorTypes = {
  policy_strategy: { label: 'Politique / stratégie', icon: 'SlidersHorizontal' },
  process_variant: { label: 'Variante de parcours', icon: 'Route' },
  intervention_mechanism: { label: 'Mécanisme', icon: 'Settings2' },
  business_scope: { label: 'Périmètre métier', icon: 'ScanLine' },
  decision_dimension: { label: 'Dimension de raisonnement', icon: 'Compass' },
  business_effect: { label: 'Effet métier', icon: 'ArrowLeftRight' },
  planning_practice: { label: 'Pratique de planification', icon: 'CalendarCheck' },
} as const;
export type BehaviorNature = keyof typeof behaviorTypes;
export function behaviorNature(node: AtlasNode): BehaviorNature | undefined {
  const value = node.fields.nature;
  return node.kind === 'behavior' && typeof value === 'string' && Object.hasOwn(behaviorTypes, value)
    ? value as BehaviorNature : undefined;
}
export function behaviorTypeLabel(node: AtlasNode): string {
  const nature = behaviorNature(node);
  return nature ? behaviorTypes[nature].label : 'Type non renseigné';
}

import type { AtlasNode, AtlasRelation } from './types';
import { capabilityTypeLabel } from './capabilityTypes.ts';
import { behaviorTypeLabel } from './behaviorTypes.ts';
export function kindLabel(node: AtlasNode) {
  if (node.groupRole === 'urbanism_level') return node.levelRef === 'universe' ? 'Univers' : 'Niveau d’urbanisme';
  if (node.kind === 'capability') return `Capacité · ${capabilityTypeLabel(node)}`;
  if (node.kind === 'behavior') return `Comportement · ${behaviorTypeLabel(node)}`;
  if (node.kind === 'area') return node.hierarchyLabel || 'Area';
  return ({ domain: 'Domaine', area: 'Area', capability: 'Capacité', behavior: 'Comportement', reference: 'Référence', group: 'Groupe de présentation', object: 'Objet métier', document: 'Document', event: 'Événement' } as Record<string,string>)[node.kind] || node.kind;
}
export function statusLabel(element: AtlasNode | AtlasRelation) {
  return ({ accepted: 'Validé dans sa portée', partial: 'Partiellement validé', proposed: 'Proposé', under_review: 'En réexamen' } as Record<string,string>)[element.status] || 'À qualifier';
}
export function shortText(text: string, length = 145) { return text.length > length ? `${text.slice(0, length).replace(/\s+\S*$/, '')}…` : text; }

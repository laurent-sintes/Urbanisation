import { behaviorTypeLabel } from '../behaviorTypes';
import { publicText } from '../publicText';
import { ArrowRight, ArrowUpRight, GitBranch } from 'lucide-react';
import { Fragment, type ReactNode } from 'react';
import type { AtlasNode, AtlasRelation, PublishedModel, MarketComparison } from '../types';
import { MarketComparisons } from './MarketComparisons';
import { kindLabel } from '../presentation';
import './details.css';
import { ModelText, ReferenceLink } from './ModelLinks';
import { NodeIcon } from '../icons';
import { childrenOf } from '../model';
import { capabilityTypeLabel, startsDecisionSection } from '../capabilityTypes';

const labels: Record<string, string> = {
  name: 'Libellé', finality: 'Finalité', definition: 'Définition', scope: 'Périmètre',
  nature: 'Nature', independence: 'Indépendance', mastership: 'Maîtrise des informations',
  decomposition_rationale: 'Pourquoi décomposer cette capacité',
  market_comparisons: 'Comparaison par rapport au marché',
  label: 'Libellé', verb: 'Verbe de relation', meaning: 'Sens métier', role: 'Rôle',
  conditions: 'Conditions', effects: 'Effets', state: 'État', note: 'Réserve',
  source_refs: 'Sources', approved_fields: 'Champs adoptés', proposed_fields: 'Champs proposés',
  validated_fields: 'Champs validés dans le cycle', recorded_by: 'Enregistré par',
  recorded_at: 'Date d’enregistrement', author: 'Auteur', date: 'Date',
};
const fieldName = (key: string) => labels[key] || key;
function hasValue(value: unknown) { return value !== undefined && value !== null && value !== '' && (!Array.isArray(value) || value.length > 0); }
function Value({ value }: { value: unknown }): ReactNode {
  if (value === undefined || value === null || value === '') return <span className="detail-muted">Non renseigné.</span>;
  if (Array.isArray(value)) return value.length ? <ul>{value.map((item, i) => <li key={i}><Value value={item}/></li>)}</ul> : <span className="detail-muted">Aucun élément renseigné.</span>;
  if (typeof value === 'object') return <dl className="detail-values">{Object.entries(value).map(([key, item]) => <div key={key}><dt>{fieldName(key)}</dt><dd><Value value={item}/></dd></div>)}</dl>;
  return <span className="detail-text"><ModelText text={publicText(typeof value === 'boolean' ? value ? 'Oui' : 'Non' : String(value))}/></span>;
}
export function BusinessSheet({ model, node }: { model: PublishedModel; node: AtlasNode }) {
  const parents = model.relations.filter(r => ['contains', 'presents'].includes(r.type) && r.targetId === node.id);
  const children = childrenOf(model, node.id);
  const behaviors = children.filter(child => child.kind === 'behavior');
  const otherChildren = children.filter(child => child.kind !== 'behavior');
  const extraFields = Object.entries(node.fields).filter(([key, value]) => ['nature', 'independence', 'mastership'].includes(key) && hasValue(value));
  return <article className="business-sheet sheet" data-testid="business-sheet" aria-label={`Fiche métier de ${node.name}`}>
    {node.kind === 'behavior' && <p className="behavior-context">Comportement de <ReferenceLink target={parents[0].sourceId}>{model.nodeById.get(parents[0].sourceId)?.name}</ReferenceLink> · Dernier niveau de détail</p>}
    <div className="sheet-main">
      <section id={`field-${node.id}-finality`} className="detail-finality"><h2>Finalité</h2><div className="business-copy"><Value value={node.fields.finality ?? node.purpose}/></div></section>
      <section id={`field-${node.id}-definition`}><h2>Définition</h2><div className="business-copy"><Value value={node.fields.definition ?? node.definition}/></div></section>
      {behaviors.length > 0 && <section className="behavior-section" aria-label="Comportements de la capacité">
        <h2>Comportements <span>{behaviors.length}</span></h2>
        <p className="detail-muted">Ce que cette capacité prend en compte et les résultats qu’elle produit.</p>
        <div className="behavior-list">{behaviors.map(behavior => <article className="behavior-summary" key={behavior.id} data-behavior-id={behavior.id}>
          <h3><ReferenceLink target={behavior.id}><NodeIcon node={behavior} size={21}/>{behavior.name}<ArrowUpRight size={16}/></ReferenceLink></h3>
          <p><ModelText text={behavior.definition}/></p>
        </article>)}</div>
      </section>}
      {hasValue(node.fields.scope) && <section id={`field-${node.id}-scope`}><h2>Périmètre</h2><div className="business-copy"><Value value={node.fields.scope}/></div></section>}
      <MarketComparisons id={`field-${node.id}-market_comparisons`} entries={node.fields.market_comparisons as MarketComparison[] | undefined}/>
      {extraFields.map(([key, value]) => <section key={key} id={`field-${node.id}-${key}`}><h2>{key === 'nature' ? node.kind === 'behavior' ? 'Type de comportement' : 'Type de capacité' : fieldName(key)}</h2><div className="business-copy"><Value value={key === 'nature' ? node.kind === 'behavior' ? behaviorTypeLabel(node) : capabilityTypeLabel(node) : value}/></div></section>)}
      {parents.length > 0 && <section className="detail-boundaries"><h2>Rattachement et frontières</h2>{parents.map(relation => <div className="detail-parent" key={relation.id}><p>{relation.type === 'presents' ? 'Présenté dans le groupe' : 'Rattaché à'} <ReferenceLink target={relation.sourceId}>{model.nodeById.get(relation.sourceId)?.name || relation.sourceId}<ArrowUpRight size={13} aria-hidden="true"/></ReferenceLink></p></div>)}</section>}
    </div>
    {otherChildren.length > 0 && <section className="sheet-children"><h2>Explorer ce périmètre <span>{otherChildren.length}</span></h2><div className="detail-children-list">{otherChildren.map((child, index) => <Fragment key={child.id}>{startsDecisionSection(otherChildren, index) && <hr className="decision-divider" aria-label="Capacités de décision"/>}<ReferenceLink target={child.id}><NodeIcon node={child} size={22}/><span><small>{kindLabel(child)}</small><strong>{child.name}</strong></span><ArrowRight size={18} aria-hidden="true"/></ReferenceLink></Fragment>)}</div></section>}
  </article>;
}

export function RelationDetails({ model, relation }: { model: PublishedModel; relation: AtlasRelation }) {
  const fields = Object.entries(relation.fields).filter(([key, value]) => !['label', 'verb'].includes(key) && hasValue(value));
  const qualifications = Object.entries(relation.qualification).filter(([key, value]) => key !== 'meaning' && hasValue(value));
  return <section className="relation-inspector relation-details" data-testid="relation-inspector" aria-label={`Détail de la relation ${relation.id}`}>
    <div className="section-kicker"><GitBranch size={16} aria-hidden="true"/>Comprendre la relation <span className="detail-identifiers">{relation.id}</span></div>
    <div className="relation-endpoints"><ReferenceLink target={relation.sourceId}>{model.nodeById.get(relation.sourceId)?.name || relation.sourceId}</ReferenceLink><ArrowRight size={21} aria-label="vers"/><ReferenceLink target={relation.targetId}>{model.nodeById.get(relation.targetId)?.name || relation.targetId}</ReferenceLink></div>
    <p className="relation-meaning"><ModelText text={relation.qualification.meaning || relation.label}/></p>
    <div className="relation-description">{qualifications.map(([key, value]) => <section key={key}><h2>{fieldName(key)}</h2><Value value={value}/></section>)}{fields.map(([key, value]) => <section key={key}><h2>{fieldName(key)}</h2><Value value={value}/></section>)}</div>
  </section>;
}

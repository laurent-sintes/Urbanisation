import { behaviorTypeLabel } from '../behaviorTypes';
import { publicText } from '../publicText';
import { ArrowRight, ArrowUpRight, GitBranch } from 'lucide-react';
import { Fragment, type ReactNode } from 'react';
import type { AtlasNode, AtlasRelation, PublishedModel, MarketComparison } from '../types';
import { businessFields, businessQualification } from '../businessContent';
import { kindLabel } from '../presentation';
import './details.css';
import { ModelText, ReferenceLink } from './ModelLinks';
import { NodeIcon } from '../icons';
import { childrenOf, relatedTo } from '../model';
import { capabilityTypeLabel, startsDecisionSection } from '../capabilityTypes';
import { businessExamples } from '../examples';
import { BusinessExamples } from './BusinessExamples';

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
export function BusinessSheet({ model, node, onShowMarket }: { model: PublishedModel; node: AtlasNode; onShowMarket: () => void }) {
  const parents = model.relations.filter(r => ['contains', 'presents'].includes(r.type) && r.targetId === node.id);
  const children = childrenOf(model, node.id);
  const behaviors = children.filter(child => child.kind === 'behavior');
  const otherChildren = children.filter(child => child.kind !== 'behavior');
  const fields = businessFields(node.fields);
  const examples = businessExamples(node.fields);
  const marketCount = (node.fields.market_comparisons as readonly MarketComparison[] | undefined)?.length || 0;
  const relations = relatedTo(model, node.id);
  const scopeParagraphs = (fields.scope || '').split(/\n\s*\n/);
  const longScope = (fields.scope?.length || 0) > 750;
  const sections = [examples.length > 0 && ['examples', 'Exemples'], fields.scope && ['scope', 'Périmètre'], relations.length > 0 && ['interactions', 'Interactions'], behaviors.length > 0 && ['behaviors', 'Comportements'], ['market_comparisons', 'Marché & choix']].filter(Boolean) as string[][];
  const jump = (field: string) => {
    if (field === 'market_comparisons') { onShowMarket(); return; }
    const target = document.getElementById(`field-${node.id}-${field}`);
    target?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    target?.focus({ preventScroll: true });
  };
  const groups = [
    { label: 'A besoin de', items: relations.filter(r => r.qualification.role === 'needs' && r.sourceId === node.id) },
    { label: 'Est utilisée par', items: relations.filter(r => r.qualification.role === 'needs' && r.targetId === node.id) },
    { label: 'Autres interactions', items: relations.filter(r => r.qualification.role !== 'needs') },
  ];
  return <article key={node.id} className="business-sheet sheet" data-testid="business-sheet" aria-label={`Fiche métier de ${node.name}`}>
    {node.kind === 'behavior' && <p className="behavior-context">Comportement de <ReferenceLink target={parents[0].sourceId}>{model.nodeById.get(parents[0].sourceId)?.name}</ReferenceLink> · Dernier niveau de détail</p>}
    {sections.length > 0 && <nav className="sheet-toc" aria-label="Dans cette fiche">{sections.map(([id, label]) => <button key={id} onClick={() => jump(id)}>{label}</button>)}</nav>}
    <div className="sheet-main">
      <section id={`field-${node.id}-finality`} className="detail-finality"><h2>À quoi cela sert</h2><div className="business-copy"><Value value={fields.finality || fields.definition}/></div></section>
      <section id={`field-${node.id}-definition`}><h2>Définition</h2><div className="business-copy"><Value value={fields.definition}/></div></section>
      <BusinessExamples id={`field-${node.id}-examples`} examples={examples}/>
      {parents.length > 0 && <div className="sheet-parent">{parents.map(relation => <span key={relation.id}>{relation.type === 'presents' ? 'Présenté dans' : 'Rattaché à'} <ReferenceLink target={relation.sourceId}>{model.nodeById.get(relation.sourceId)?.name || relation.sourceId}</ReferenceLink></span>)}</div>}
      {fields.scope && <section id={`field-${node.id}-scope`} tabIndex={-1} className="sheet-scope"><h2>Périmètre et limites</h2>
        {longScope ? <>{scopeParagraphs.length > 1 && <><p className="detail-muted">Extrait du périmètre</p><div className="business-copy"><Value value={scopeParagraphs[0]}/></div></>}<details className="sheet-disclosure"><summary>Lire le périmètre complet et ses conditions</summary><div className="business-copy"><Value value={fields.scope}/></div></details></> : <div className="business-copy"><Value value={fields.scope}/></div>}
      </section>}
      {(fields.nature || fields.mastership || fields.independence) && <dl className="sheet-facts">
        {fields.nature && <div><dt>{node.kind === 'behavior' ? 'Type de comportement' : 'Type de capacité'}</dt><dd>{node.kind === 'behavior' ? behaviorTypeLabel(node) : capabilityTypeLabel(node)}</dd></div>}
        {fields.mastership && <div><dt>Autorité sur les informations</dt><dd><Value value={fields.mastership === 'external' ? 'Informations de référence maîtrisées à l’extérieur de Supply.' : fields.mastership}/></dd></div>}
        {fields.independence && <div><dt>Autonomie</dt><dd><Value value={fields.independence}/></dd></div>}
      </dl>}
      {relations.length > 0 && <section id={`field-${node.id}-interactions`} tabIndex={-1} className="sheet-interactions"><h2>Responsabilités liées <span>{relations.length}</span></h2><div className="interaction-groups">{groups.filter(group => group.items.length).map(group => <div key={group.label}><h3>{group.label}</h3>{group.items.map(relation => {
        const other = relation.sourceId === node.id ? relation.targetId : relation.sourceId;
        return <details className="interaction-item" key={relation.id}><summary>{model.nodeById.get(other)?.name || other}</summary><p><ReferenceLink target={other}>Lire la fiche <ArrowUpRight size={14}/></ReferenceLink></p><Value value={relation.qualification.meaning || relation.label}/>{Object.entries(businessQualification(relation.qualification)).filter(([key]) => !['meaning', 'role'].includes(key)).map(([key, value]) => <div key={key}><h4>{fieldName(key)}</h4><Value value={value}/></div>)}</details>;
      })}</div>)}</div></section>}
      {behaviors.length > 0 && <section id={`field-${node.id}-behaviors`} tabIndex={-1} className="behavior-section" aria-label="Comportements de la capacité">
        <h2>Comportements <span>{behaviors.length}</span></h2>
        <div className="behavior-list">{behaviors.map(behavior => <details className="behavior-summary" key={behavior.id} data-behavior-id={behavior.id}>
          <summary><NodeIcon node={behavior} size={21}/><span>{behavior.name}<small>{behaviorTypeLabel(behavior)}</small></span></summary>
          <p><ModelText text={publicText(behavior.definition)}/></p><ReferenceLink target={behavior.id}>Lire le comportement <ArrowUpRight size={16}/></ReferenceLink>
        </details>)}</div>
      </section>}
    </div>
    <div className="sheet-market-entry"><p>{marketCount ? `${marketCount} rapprochement${marketCount > 1 ? 's' : ''} documenté${marketCount > 1 ? 's' : ''} : vocabulaire, périmètre retenu et sources.` : 'Le positionnement marché de cet élément reste à documenter dans cette publication.'}</p><button className="secondary-button" onClick={onShowMarket}>Marché & choix <ArrowUpRight size={16}/></button></div>
    {otherChildren.length > 0 && <section className="sheet-children"><h2>Explorer ce périmètre <span>{otherChildren.length}</span></h2><div className="detail-children-list">{otherChildren.map((child, index) => <Fragment key={child.id}>{startsDecisionSection(otherChildren, index) && <hr className="decision-divider" aria-label="Capacités de décision"/>}<ReferenceLink target={child.id}><NodeIcon node={child} size={22}/><span><small>{kindLabel(child)}</small><strong>{child.name}</strong></span><ArrowRight size={18} aria-hidden="true"/></ReferenceLink></Fragment>)}</div></section>}
  </article>;
}

export function RelationDetails({ model, relation }: { model: PublishedModel; relation: AtlasRelation }) {
  const fields = Object.entries(businessFields(relation.fields)).filter(([key, value]) => key !== 'name' && hasValue(value));
  const qualifications = Object.entries(businessQualification(relation.qualification)).filter(([key, value]) => key !== 'meaning' && hasValue(value));
  return <section className="relation-inspector relation-details" data-testid="relation-inspector" aria-label={`Détail de la relation ${relation.id}`}>
    <div className="section-kicker"><GitBranch size={16} aria-hidden="true"/>Comprendre la relation <span className="detail-identifiers">{relation.id}</span></div>
    <div className="relation-endpoints"><ReferenceLink target={relation.sourceId}>{model.nodeById.get(relation.sourceId)?.name || relation.sourceId}</ReferenceLink><ArrowRight size={21} aria-label="vers"/><ReferenceLink target={relation.targetId}>{model.nodeById.get(relation.targetId)?.name || relation.targetId}</ReferenceLink></div>
    <p className="relation-meaning"><ModelText text={publicText(relation.qualification.meaning || relation.label)}/></p>
    <div className="relation-description">{qualifications.map(([key, value]) => <section key={key}><h2>{fieldName(key)}</h2><Value value={key === 'role' && value === 'needs' ? 'A besoin de' : value}/></section>)}{fields.map(([key, value]) => <section key={key}><h2>{fieldName(key)}</h2><Value value={value}/></section>)}</div>
  </section>;
}

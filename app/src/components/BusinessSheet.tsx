import { ArrowRight, ArrowUpRight, ChevronDown, FileText, GitBranch } from 'lucide-react';
import type { ReactNode } from 'react';
import type { AtlasNode, AtlasRelation, PublishedModel, SourceLocator } from '../types';
import { kindLabel, statusLabel } from '../presentation';
import './details.css';
import { ModelText, ReferenceLink } from './ModelLinks';
import { NodeIcon } from '../icons';

type Element = AtlasNode | AtlasRelation;
type OpenSource = (id: string, locator?: SourceLocator) => void;
const labels: Record<string, string> = {
  name: 'Libellé', finality: 'Finalité', definition: 'Définition', scope: 'Périmètre',
  nature: 'Nature', independence: 'Indépendance', mastership: 'Maîtrise des informations',
  label: 'Libellé', verb: 'Verbe de relation', meaning: 'Sens métier', role: 'Rôle',
  conditions: 'Conditions', effects: 'Effets', state: 'État', note: 'Réserve',
  source_refs: 'Sources', approved_fields: 'Champs adoptés', proposed_fields: 'Champs proposés',
  validated_fields: 'Champs validés dans le cycle', recorded_by: 'Enregistré par',
  recorded_at: 'Date d’enregistrement', author: 'Auteur', date: 'Date',
};
const lifecycleLabels: Record<string, string> = {
  ai_proposed: 'Proposé par l’IA', under_instruction: 'En cours d’instruction', urbanist_validated: 'Validé par l’urbaniste',
};
const fieldName = (key: string) => labels[key] || key;
const names = (fields: readonly string[]) => fields.map(fieldName).join(', ');
function date(value: unknown) {
  return typeof value === 'string' && !Number.isNaN(Date.parse(value))
    ? new Intl.DateTimeFormat('fr-FR', { dateStyle: 'long', timeStyle: 'short' }).format(new Date(value))
    : 'Non renseignée';
}
function hasValue(value: unknown) { return value !== undefined && value !== null && value !== '' && (!Array.isArray(value) || value.length > 0); }
function Value({ value }: { value: unknown }): ReactNode {
  if (value === undefined || value === null || value === '') return <span className="detail-muted">Non renseigné.</span>;
  if (Array.isArray(value)) return value.length ? <ul>{value.map((item, i) => <li key={i}><Value value={item}/></li>)}</ul> : <span className="detail-muted">Aucun élément renseigné.</span>;
  if (typeof value === 'object') return <dl className="detail-values">{Object.entries(value).map(([key, item]) => <div key={key}><dt>{fieldName(key)}</dt><dd><Value value={item}/></dd></div>)}</dl>;
  return <span className="detail-text"><ModelText text={typeof value === 'boolean' ? value ? 'Oui' : 'Non' : String(value)}/></span>;
}
function SourceButtons({ model, refs, onOpenSource }: { model: PublishedModel; refs: readonly string[]; onOpenSource: OpenSource }) {
  return <div className="source-buttons">{refs.length ? refs.map(id => {
    const locator = model.sourceReferences[id] as SourceLocator | undefined;
    return locator?.path ? <button type="button" key={id} onClick={() => onOpenSource(id, locator)} title={locator.path}>{id}<ArrowUpRight size={13} aria-hidden="true"/></button> : <span key={id} title="Aucun localisateur documentaire disponible">{id}</span>;
  }) : <span className="detail-muted">Aucune référence renseignée.</span>}</div>;
}
function ValidationSummary({ item }: { item: Element }) {
  return <div className="detail-validation"><span className={`pill ${item.status}`}>{statusLabel(item)}</span><div>{item.lifecycle?.state && <p className="detail-cycle">Cycle : <strong>{lifecycleLabels[item.lifecycle.state] || item.lifecycle.state}</strong></p>}<p>{item.approvedFields.length ? <>Champs adoptés : <strong>{names(item.approvedFields)}</strong>.</> : 'Aucun champ explicitement adopté dans cette publication.'}</p>{item.proposedFields.length > 0 && <p>À valider : {names(item.proposedFields)}.</p>}</div></div>;
}
function Reservations({ item }: { item: Element }) {
  const lifecycleNote = item.lifecycle?.note;
  return <>{(item.review.note || lifecycleNote) && <section className="detail-reservations"><h2>Portée et réserves</h2>{item.review.note && <p>{item.review.note}</p>}{lifecycleNote && lifecycleNote !== item.review.note && <p>{lifecycleNote}</p>}</section>}</>;
}
function Provenance({ model, item, onOpenSource }: { model: PublishedModel; item: Element; onOpenSource: OpenSource }) {
  const lifecycle = item.lifecycle;
  return <details className="provenance detail-provenance" key={item.id}>
    <summary><FileText size={17} aria-hidden="true"/><span>Sources, révision et portée détaillée</span><small>{item.sourceRefs.length} références</small><ChevronDown size={16} aria-hidden="true"/></summary>
    <div className="provenance-body">
      <section><h3>Portée de validation</h3><p>Champs adoptés : {names(item.approvedFields) || 'aucun champ explicitement adopté'}.</p><p>Champs proposés : {names(item.proposedFields) || 'aucun champ indiqué ici'}.</p>
        {Object.keys(item.fieldStatus).length > 0 && <><h4>Qualification par champ</h4><Value value={item.fieldStatus}/></>}
        {item.adoptionIds.length > 0 && <><h4>Décisions de référence</h4><p className="detail-identifiers">{item.adoptionIds.join(' · ')}</p></>}
      </section>
      {lifecycle && <section><h3>Cycle d’instruction</h3><p><strong>{lifecycleLabels[lifecycle.state || ''] || lifecycle.state || 'Non renseigné'}</strong></p><p>Champs validés dans le cycle : {names(lifecycle.validated_fields || []) || 'aucun'}.</p>{lifecycle.note && <p>{lifecycle.note}</p>}<dl className="detail-meta"><div><dt>Enregistré par</dt><dd>{String(lifecycle.recorded_by || 'Non renseigné')}</dd></div><div><dt>Enregistré le</dt><dd>{date(lifecycle.recorded_at)}</dd></div></dl>{lifecycle.source_refs && <SourceButtons model={model} refs={lifecycle.source_refs} onOpenSource={onOpenSource}/>}</section>}
      <section><h3>Sources documentaires</h3><SourceButtons model={model} refs={item.sourceRefs} onOpenSource={onOpenSource}/>{item.sourceLocator?.path && <div className="detail-register"><button type="button" onClick={() => onOpenSource(item.id, item.sourceLocator)}><FileText size={15} aria-hidden="true"/>Ouvrir le registre source<ArrowUpRight size={14} aria-hidden="true"/></button><p className="detail-path">{item.sourceLocator.path}{item.sourceLocator.anchor ? ` #${item.sourceLocator.anchor}` : ''}</p></div>}</section>
      <section><h3>Publication et révision</h3><dl className="detail-meta"><div><dt>Identifiant</dt><dd>{item.id}</dd></div><div><dt>Révision de l’élément</dt><dd>{item.revision ?? 'Non renseignée'}</dd></div><div><dt>Dernière modification</dt><dd><time dateTime={item.lastModified}>{date(item.lastModified)}</time></dd></div><div><dt>Publication consultée</dt><dd>{model.revision ? `v${String(model.revision).padStart(3, '0')} · ` : ''}{model.version}</dd></div></dl>{model.sourcePath && <p className="detail-path">{model.sourcePath}</p>}</section>
    </div>
  </details>;
}

export function BusinessSheet({ model, node, onOpenSource }: { model: PublishedModel; node: AtlasNode; onOpenSource: OpenSource }) {
  const parents = model.relations.filter(r => ['contains', 'presents'].includes(r.type) && r.targetId === node.id);
  const children = model.relations.filter(r => ['contains', 'presents'].includes(r.type) && r.sourceId === node.id).map(r => model.nodeById.get(r.targetId)).filter((n): n is AtlasNode => Boolean(n));
  const extraFields = Object.entries(node.fields).filter(([key, value]) => !['name', 'finality', 'definition', 'scope'].includes(key) && hasValue(value));
  return <article className="business-sheet sheet" data-testid="business-sheet" aria-label={`Fiche métier de ${node.name}`}>
    <ValidationSummary item={node}/>
    <div className="sheet-main">
      <section id={`field-${node.id}-finality`} className="detail-finality"><h2>Finalité</h2><div className="business-copy"><Value value={node.fields.finality ?? node.purpose}/></div></section>
      <section id={`field-${node.id}-definition`}><h2>Définition</h2><div className="business-copy"><Value value={node.fields.definition ?? node.definition}/></div></section>
      {hasValue(node.fields.scope) && <section id={`field-${node.id}-scope`}><h2>Périmètre</h2><div className="business-copy"><Value value={node.fields.scope}/></div></section>}
      {extraFields.map(([key, value]) => <section key={key} id={`field-${node.id}-${key}`}><h2>{fieldName(key)}</h2><div className="business-copy"><Value value={value}/></div></section>)}
      <Reservations item={node}/>
      {parents.length > 0 && <section className="detail-boundaries"><h2>Rattachement et frontières</h2>{parents.map(relation => <div className="detail-parent" key={relation.id}><p>{relation.type === 'presents' ? 'Présenté dans le groupe' : 'Rattaché à'} <ReferenceLink target={relation.sourceId}>{model.nodeById.get(relation.sourceId)?.name || relation.sourceId}<ArrowUpRight size={13} aria-hidden="true"/></ReferenceLink></p><span className={`pill ${relation.status}`}>{statusLabel(relation)}</span>{relation.review.note && <p>{relation.review.note}</p>}{relation.lifecycle?.note && relation.lifecycle.note !== relation.review.note && <p>{relation.lifecycle.note}</p>}<Provenance model={model} item={relation} onOpenSource={onOpenSource}/></div>)}</section>}
      <Provenance model={model} item={node} onOpenSource={onOpenSource}/>
    </div>
    {children.length > 0 && <section className="sheet-children"><h2>Explorer ce périmètre <span>{children.length}</span></h2><div className="detail-children-list">{children.map(child => <ReferenceLink key={child.id} target={child.id}><NodeIcon node={child} size={22}/><span><small>{kindLabel(child)}</small><strong>{child.name}</strong></span><ArrowRight size={18} aria-hidden="true"/></ReferenceLink>)}</div></section>}
  </article>;
}

export function RelationDetails({ model, relation, onOpenSource }: { model: PublishedModel; relation: AtlasRelation; onOpenSource: OpenSource }) {
  const fields = Object.entries(relation.fields).filter(([key, value]) => !['label', 'verb'].includes(key) && hasValue(value));
  const qualifications = Object.entries(relation.qualification).filter(([key, value]) => key !== 'meaning' && hasValue(value));
  return <section className="relation-inspector relation-details" data-testid="relation-inspector" aria-label={`Détail de la relation ${relation.id}`}>
    <div className="section-kicker"><GitBranch size={16} aria-hidden="true"/>Comprendre la relation <span className="detail-identifiers">{relation.id}</span></div>
    <div className="relation-endpoints"><ReferenceLink target={relation.sourceId}>{model.nodeById.get(relation.sourceId)?.name || relation.sourceId}</ReferenceLink><ArrowRight size={21} aria-label="vers"/><ReferenceLink target={relation.targetId}>{model.nodeById.get(relation.targetId)?.name || relation.targetId}</ReferenceLink></div>
    <p className="relation-meaning"><ModelText text={relation.qualification.meaning || relation.label}/></p>
    <ValidationSummary item={relation}/>
    <div className="relation-description">{qualifications.map(([key, value]) => <section key={key}><h2>{fieldName(key)}</h2><Value value={value}/></section>)}{fields.map(([key, value]) => <section key={key}><h2>{fieldName(key)}</h2><Value value={value}/></section>)}</div>
    <Reservations item={relation}/><Provenance model={model} item={relation} onOpenSource={onOpenSource}/>
  </section>;
}

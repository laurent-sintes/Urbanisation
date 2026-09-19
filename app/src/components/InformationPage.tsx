import { useEffect, useRef, useState } from 'react';
import { ArrowRight, BookOpen, FileText, Search, Waypoints } from 'lucide-react';
import type { BusinessInformation, PublishedModel } from '../types';
import { informationForNode, informationHref, informationSearchText } from '../information';
import { marketText } from '../marketContent';
import { ModelText, ReferenceLink } from './ModelLinks';
import { MarketComparisons } from './MarketComparisons';
import { BusinessExamples } from './BusinessExamples';
import './information.css';

const readable = (text: string) => <ModelText text={marketText(text)}/>;
const normalize = (text: string) => text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('fr');

export function InformationPage({ model, selected, nodeId }: {
  model: PublishedModel; selected?: string; nodeId?: string;
}) {
  const [query, setQuery] = useState('');
  const [tab, setTab] = useState<'sheet' | 'market'>('sheet');
  const detail = useRef<HTMLElement>(null);
  const scope = nodeId ? model.nodeById.get(nodeId) : undefined;
  const items = informationForNode(model, nodeId);
  const item = selected ? model.informationById.get(selected) : items[0];
  const matches = items.filter(value => normalize(value.name + '\n' + informationSearchText(value)).includes(normalize(query.trim())));
  useEffect(() => {
    setTab('sheet');
    if (detail.current) { detail.current.scrollTop = 0; detail.current.focus({ preventScroll: true }); }
  }, [model.version, item?.id]);
  if (!model.hasInformationCatalogue) return <section className="empty-state information-empty">
    <Waypoints size={32}/><h2>Informations non publiées dans cette version</h2>
    <p>Cette publication ne contient pas de catalogue d’informations métier.</p>
  </section>;
  const links = item ? model.informationLinks.filter(link => link.from_ref === item.id || link.to_ref === item.id) : [];
  return <section className="information-page" aria-label="Catalogue des informations métier">
    <aside className="information-index" aria-label="Liste des informations">
      <div className="information-index-head">
        {scope && <div className="information-scope"><span>Dans {scope.name}</span><a href={informationHref(model)}>Toutes les informations</a></div>}
        <label className="information-search"><Search size={17}/><input aria-label="Rechercher une information métier" placeholder="Une information, un usage…" value={query} onChange={e => setQuery(e.target.value)}/></label>
        <p role="status">{matches.length} information{matches.length > 1 ? 's' : ''}</p>
      </div>
      <ul>{matches.map(value => <li key={value.id}><a href={informationHref(model, value.id, nodeId)} aria-current={item?.id === value.id ? 'page' : undefined}>
        <strong>{value.name}</strong><span>{value.label_fr}</span>
      </a></li>)}</ul>
      {!matches.length && <p className="information-no-match">Aucune information ne correspond dans ce périmètre.</p>}
    </aside>
    <article className="information-detail" ref={detail} tabIndex={-1} aria-label={item ? `Information : ${item.name}` : 'Information absente'} data-information-id={item?.id}>
      {!item ? <><h2>{selected ? 'Information absente de cette publication' : 'Aucune information documentée pour ce périmètre'}</h2><p><a href={informationHref(model)}>Parcourir les informations publiées</a></p></> : <>
        <header className="information-header"><p className="section-kicker">INFORMATION MÉTIER</p><h2>{item.name}</h2><p>{item.label_fr}</p></header>
        {scope && !items.some(value => value.id === item.id) && <p className="information-context-note">Cette information est liée à un autre périmètre. <a href={informationHref(model, item.id)}>Voir dans le catalogue complet</a></p>}
        <div className="information-tabs" role="tablist" aria-label="Lecture de l’information">{([
          ['sheet', 'Fiche', FileText], ['market', 'Sources d’inspiration', BookOpen],
        ] as const).map(([id, label, Icon]) => <button key={id} id={`information-tab-${id}`} role="tab" aria-selected={tab === id} tabIndex={tab === id ? 0 : -1} aria-controls="information-tab-panel" onClick={() => setTab(id)} onKeyDown={event => {
          if (['ArrowLeft','ArrowRight','Home','End'].includes(event.key)) {
            event.preventDefault(); const next = event.key === 'Home' ? 'sheet' : event.key === 'End' ? 'market' : tab === 'sheet' ? 'market' : 'sheet';
            setTab(next); document.getElementById(`information-tab-${next}`)?.focus();
          }
        }}><Icon size={16}/>{label}</button>)}</div>
        <div id="information-tab-panel" role="tabpanel" aria-labelledby={`information-tab-${tab}`}>
          {tab === 'market' ? <MarketComparisons id={`information-${item.id}-market`} entries={item.market_comparisons}/> : <>
            <p className="information-question">{readable(item.question)}</p>
            <section><h3>Définition</h3><p>{readable(item.definition)}</p></section>
            <BusinessExamples id={`information-${item.id}-examples`} examples={item.examples}/>
            <section><h3>Ce qui donne son sens à l’information</h3><p>{readable(item.context)}</p><ul>{item.essential_elements.map((value, i) => <li key={i}>{readable(value)}</li>)}</ul>
              <details><summary>Comprendre cette maille et ses limites</summary><p>{readable(item.granularity_rationale)}</p><ul>{item.boundaries.map((value, i) => <li key={i}>{readable(value)}</li>)}</ul><p>{readable(item.document_and_fact_boundary)}</p></details>
            </section>
            <section><h3>Usages par les capacités</h3><div className="information-roles">{item.capability_roles.map(role => <div key={role.capability_ref}>
              <ReferenceLink target={role.capability_ref}>{model.nodeById.get(role.capability_ref)?.name}</ReferenceLink>
              <strong>{readable(role.role)}</strong><p>{readable(role.meaning)}</p>
            </div>)}</div></section>
            <section><h3>Informations liées <span>{links.length}</span></h3>{links.length ? <div className="information-links">{links.map(link => {
              const from = model.informationById.get(link.from_ref)!, to = model.informationById.get(link.to_ref)!;
              return <details key={link.id}><summary><span>{from.id === item.id ? from.name : <a href={informationHref(model, from.id)}>{from.name}</a>}</span><ArrowRight size={16}/><span>{to.id === item.id ? to.name : <a href={informationHref(model, to.id)}>{to.name}</a>}</span><small>{readable(link.meaning)}</small></summary>
                <p><strong>Condition. </strong>{readable(link.condition)}</p><p><strong>Effet métier. </strong>{readable(link.effect)}</p>
              </details>;
            })}</div> : <p>Aucun lien documenté pour cette information dans cette publication.</p>}</section>
          </>}
        </div>
      </>}
    </article>
  </section>;
}

export function InformationSummary({ model, nodeId, items }: { model: PublishedModel; nodeId: string; items: readonly BusinessInformation[] }) {
  if (!items.length) return null;
  return <section id={`field-${nodeId}-information`} className="sheet-information" tabIndex={-1}>
    <h2>Informations métier <span>{items.length}</span></h2>
    <p>Le contenu métier que les capacités connaissent, utilisent ou font évoluer.</p>
    <div className="sheet-information-list">{items.map(item => <a key={item.id} href={informationHref(model, item.id, nodeId)}>
      <Waypoints size={19}/><span><strong>{item.name}</strong><small>{item.question}</small></span><ArrowRight size={16}/>
    </a>)}</div>
  </section>;
}

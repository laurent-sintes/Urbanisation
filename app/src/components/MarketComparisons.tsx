import type { MarketComparison } from '../types';
import { ModelText } from './ModelLinks';
import './market-comparisons.css';

const statuses = { proposed: 'Rapprochement proposé', under_review: 'À instruire', validated: 'Rapprochement validé dans sa portée' };

export function MarketComparisons({ entries, id }: { entries?: readonly MarketComparison[]; id: string }) {
  if (!entries?.length) return null;
  return <section id={id} className="market-comparisons" aria-label="Comparaison par rapport au marché">
    <h2>Comparaison par rapport au marché</h2>
    <p className="market-intro">Repères pour discuter du vocabulaire et des périmètres. Une proximité avec un produit ne prouve pas sa mise en œuvre chez Beaumanoir.</p>
    <div className="market-cards">{entries.map((entry, i) => <article className="market-card" key={`${entry.vendor}-${entry.element_name}-${i}`}>
      <header><div><p className="market-vendor">{entry.vendor} · {entry.product}</p><h3>{entry.element_name}</h3></div><span className="market-status">{statuses[entry.status]}</span></header>
      <p className="market-relationship">{entry.element_type} · {entry.relationship}</p>
      <dl className="market-content">
        <div><dt>Points communs</dt><dd><ModelText text={entry.similarities}/></dd></div>
        <div><dt>Différences et limites de périmètre</dt><dd><ModelText text={entry.differences}/></dd></div>
        <div className="market-choice"><dt>Choix retenu ou proposé pour FLOW</dt><dd><ModelText text={entry.flow_position}/></dd></div>
      </dl>
      <details className="market-evidence"><summary>Source et portée de la comparaison</summary>
        <p>{/^https?:\/\//i.test(entry.source_url) ? <a href={entry.source_url} target="_blank" rel="noopener noreferrer">{entry.source_title} ↗</a> : <span>{entry.source_title}</span>}</p>
        <p>{entry.source_version} · Consulté le {entry.consulted_on}</p>
        <p><strong>Passage :</strong> {entry.source_locator}</p>
        <p><strong>Limite de preuve :</strong> {entry.evidence_limits}</p>
        <p className="market-refs">Références : {entry.source_refs.join(' · ')}</p>
      </details>
    </article>)}</div>
  </section>;
}

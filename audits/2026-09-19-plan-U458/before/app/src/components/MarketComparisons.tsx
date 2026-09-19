import type { MarketComparison } from '../types';
import { ModelText } from './ModelLinks';
import './market-comparisons.css';

export function MarketComparisons({ entries, id }: { entries?: readonly MarketComparison[]; id: string }) {
  if (!entries?.length) return null;
  return <section id={id} className="market-comparisons" aria-label="Comparaison par rapport au marché">
    <h2>Comparaison par rapport au marché</h2>
    <div className="market-cards">{entries.map((entry, i) => <article className="market-card" key={`${entry.vendor}-${entry.element_name}-${i}`}>
      <header><div><p className="market-vendor">{entry.vendor} · {entry.product}</p><h3>{entry.element_name}</h3></div></header>
      <p className="market-relationship">{entry.element_type} · {entry.relationship}</p>
      <dl className="market-content">
        <div><dt>Points communs</dt><dd><ModelText text={entry.similarities}/></dd></div>
        <div><dt>Différences et limites de périmètre</dt><dd><ModelText text={entry.differences}/></dd></div>
      </dl>
      <details className="market-evidence"><summary>Source et portée de la comparaison</summary>
        <p>{/^https?:\/\//i.test(entry.source_url) ? <a href={entry.source_url} target="_blank" rel="noopener noreferrer">{entry.source_title} ↗</a> : <span>{entry.source_title}</span>}</p>
        <p>{entry.source_version} · Consulté le {entry.consulted_on}</p>
        <p><strong>Passage :</strong> {entry.source_locator}</p>
      </details>
    </article>)}</div>
  </section>;
}

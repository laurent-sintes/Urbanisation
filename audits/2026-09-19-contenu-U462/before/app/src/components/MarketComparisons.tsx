import type { MarketComparison } from '../types';
import { ModelText } from './ModelLinks';
import { marketText } from '../marketContent';
import './market-comparisons.css';

export function MarketComparisons({ entries, id }: { entries?: readonly MarketComparison[]; id: string }) {
  return <section id={id} tabIndex={-1} className="market-comparisons" aria-label="Repères marché">
    <h2>Repères marché</h2>
    {!entries?.length ? <p className="market-intro">Positionnement non documenté dans cette publication.</p> : <>
    <p className="market-intro">Points communs, écarts et appuis du modèle. Un rapprochement avec une offre n’implique pas son choix pour la réalisation.</p>
    <div className="market-cards">{entries.map((entry, i) => <details className="market-card" key={`${entry.vendor}-${entry.element_name}-${i}`}>
      <summary><span className="market-vendor">{entry.vendor} · {entry.product}</span><strong>{entry.element_name}</strong><span className="market-relationship">{marketText(entry.relationship)}</span></summary>
      <p className="market-relationship">{entry.element_type}</p>
      <p className="market-position"><strong>Positionnement :</strong> {marketText(entry.relationship)}</p>
      <dl className="market-content">
        <div><dt>Points communs</dt><dd><ModelText text={marketText(entry.similarities)}/></dd></div>
        <div><dt>Différences et limites de périmètre</dt><dd><ModelText text={marketText(entry.differences)}/></dd></div>
        {entry.flow_position && <div className="market-choice"><dt>Choix du modèle FLOW</dt><dd><ModelText text={marketText(entry.flow_position)}/></dd></div>}
      </dl>
      <details className="market-evidence"><summary>Source et portée de la comparaison</summary>
        <p>{/^https?:\/\//i.test(entry.source_url) ? <a href={entry.source_url} target="_blank" rel="noopener noreferrer">{entry.source_title} ↗</a> : <span>{entry.source_title}</span>}</p>
        <p>{entry.source_version} · Consulté le {entry.consulted_on}</p>
        <p><strong>Passage :</strong> {entry.source_locator}</p>
        {entry.evidence_limits && <p><strong>Portée de la source :</strong> <ModelText text={marketText(entry.evidence_limits)}/></p>}
      </details>
    </details>)}</div></>}
  </section>;
}

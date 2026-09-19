import type { MarketComparison } from '../types';
import { ModelText } from './ModelLinks';
import { marketText, marketComparisonsForReading } from '../marketContent';
import './market-comparisons.css';

export function MarketComparisons({ entries, id }: { entries?: readonly MarketComparison[]; id: string }) {
  return <section id={id} tabIndex={-1} className="market-comparisons" aria-label="Repères marché">
    <h2>Marché & choix du modèle</h2>
    {!entries?.length ? <p className="market-intro">Positionnement non documenté dans cette publication.</p> : <>
    <p className="market-intro">Pourquoi ces termes et ce périmètre : choix FLOW, appuis du marché et différences. Ces références éclairent le métier sans désigner une solution à implémenter.</p>
    <div className="market-cards">{marketComparisonsForReading(entries).map((entry, i) => <article className="market-card" key={`${entry.vendor}-${entry.element_name}-${i}`}>
      <header><div><p className="market-vendor">{entry.vendor} · {entry.product}</p><h3>{entry.element_name}</h3></div><span className="market-relationship">{marketText(entry.relationship)}</span></header>
      <div className="market-choice">
        {entry.term_choice && <p><strong>Pourquoi ce terme. </strong><ModelText text={marketText(entry.term_choice)}/></p>}
        {entry.definition_choice && <p><strong>Pourquoi cette définition. </strong><ModelText text={marketText(entry.definition_choice)}/></p>}
        {entry.flow_position && ![entry.term_choice, entry.definition_choice].some(text => marketText(text) === marketText(entry.flow_position)) && <p><strong>Position FLOW. </strong><ModelText text={marketText(entry.flow_position)}/></p>}
      </div>
      <p className="market-source"><strong>Source : </strong>{/^https?:\/\//i.test(entry.source_url) ? <a href={entry.source_url} target="_blank" rel="noopener noreferrer">{entry.source_title} ↗</a> : <span>{entry.source_title}</span>}<span>Consultée le {entry.consulted_on}</span></p>
      <details className="market-detail"><summary>Comparer les périmètres et examiner la source</summary>
      <p className="market-relationship">Nature de la référence : {entry.element_type}</p>
      <dl className="market-content">
        <div><dt>Points communs</dt><dd><ModelText text={marketText(entry.similarities)}/></dd></div>
        <div><dt>Différences et limites de périmètre</dt><dd><ModelText text={marketText(entry.differences)}/></dd></div>
      </dl>
      <div className="market-evidence">
        <p>{entry.source_version}</p>
        <p><strong>Passage :</strong> {entry.source_locator}</p>
        {entry.evidence_limits && <p><strong>Portée de la source :</strong> <ModelText text={marketText(entry.evidence_limits)}/></p>}
      </div></details>
    </article>)}</div></>}
  </section>;
}

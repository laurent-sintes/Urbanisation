import type { ReaderExample } from '../examples';
import { ModelText, ReferenceLink } from './ModelLinks';
import './examples.css';

export function BusinessExamples({ examples, id }: { examples: readonly ReaderExample[]; id: string }) {
  if (!examples.length) return null;
  return <section id={id} tabIndex={-1} className="business-examples" aria-label="Scénarios métier">
    <h2>Scénarios métier</h2>
    <div className="example-cards">{examples.map((example, index) => <article className="example-card" key={index}>
      <h3>{example.title}</h3>
      <p><ModelText text={example.situation}/></p>
      {example.sourceNode && <p><ReferenceLink target={example.sourceNode} anchor="examples">Scénario partagé — fiche d’origine</ReferenceLink></p>}
      {example.contribution && <p><strong>Contribution de cette fiche. </strong><ModelText text={example.contribution}/></p>}
      {example.trigger && <p><strong>Déclencheur. </strong><ModelText text={example.trigger}/></p>}
      {example.objective && <p><strong>Résultat recherché. </strong><ModelText text={example.objective}/></p>}
      {!!example.constraints?.length && <><h4>Contraintes</h4><ul>{example.constraints.map((text, i) => <li key={i}><ModelText text={text}/></li>)}</ul></>}
      {!!example.options?.length && <><h4>Options examinées</h4><ul>{example.options.map((option, i) => <li key={i}><strong>{option.title}. </strong><ModelText text={option.description}/></li>)}</ul></>}
      {!!example.contributions?.length && <><h4>Contributions métier</h4><ul>{example.contributions.map((contribution, i) => <li key={i}><ModelText text={contribution.role}/></li>)}</ul></>}
      {example.outcome && <p><strong>Ce qui se passe. </strong><ModelText text={example.outcome}/></p>}
      {example.lesson && <p className="example-lesson"><strong>Ce que cela illustre. </strong><ModelText text={example.lesson}/></p>}
    </article>)}</div>
  </section>;
}

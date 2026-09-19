import type { ReaderExample } from '../examples';
import { ModelText } from './ModelLinks';
import './examples.css';

export function BusinessExamples({ examples, id }: { examples: readonly ReaderExample[]; id: string }) {
  if (!examples.length) return null;
  return <section id={id} tabIndex={-1} className="business-examples" aria-label="Exemples concrets">
    <h2>Exemples concrets</h2>
    <div className="example-cards">{examples.map((example, index) => <article className="example-card" key={index}>
      <h3>{example.title}</h3>
      <p><ModelText text={example.situation}/></p>
      {example.outcome && <p><strong>Ce qui se passe. </strong><ModelText text={example.outcome}/></p>}
      {example.lesson && <p className="example-lesson"><strong>Ce que cela illustre. </strong><ModelText text={example.lesson}/></p>}
    </article>)}</div>
  </section>;
}

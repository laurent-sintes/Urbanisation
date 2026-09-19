import { useEffect, useId, useState } from 'react';
import { ArrowUpRight, BookOpen, ChevronDown, RefreshCw } from 'lucide-react';
import { fetchModelingGuide, type GuideLesson, type GuideResponse, type ModelingGuide } from '../modelingGuide';
import type { PublishedModel } from '../types';
import { ReferenceLink } from './ModelLinks';
import './modeling-guide.css';

type LoadState =
  | { version: string; status: 'loading' }
  | { version: string; status: 'error'; message: string }
  | { version: string; status: 'ready'; response: GuideResponse };

function readableDate(value: string) {
  const parts = /^(\d{4})-(\d{2})-(\d{2})$/.exec(value);
  if (!parts) return value;
  return new Intl.DateTimeFormat('fr-FR', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' })
    .format(new Date(Date.UTC(Number(parts[1]), Number(parts[2]) - 1, Number(parts[3]))));
}

function TechnicalScene({ scene }: { scene: GuideLesson['scene'] }) {
  const [selected, setSelected] = useState(0);
  const variant = scene.variants?.[selected];
  const outputId = useId();
  if (!variant) return null;
  const mark = (index: number) => String.fromCharCode(65 + index);
  return <div className="guide-technical-scene">
    <div className="guide-realization-controls">
      <p className="guide-scene-label">Change la réalisation technique</p>
      <div className="guide-variants" role="group" aria-label="Choisir une réalisation technique">
        {scene.variants?.map((item, index) => <button type="button" key={item.id} aria-pressed={index === selected}
          aria-controls={outputId} onClick={() => setSelected(index)}>{item.label}</button>)}
      </div>
    </div>
    <section className="guide-business" aria-label="Capacités métier stables">
      <p className="guide-scene-label">Le modèle métier reste le même</p>
      <div className="guide-business-cards">{scene.items.map((item, index) => <div className="guide-piece" key={index}>
        <span className="guide-capability-mark" aria-hidden="true">{mark(index)}</span>
        <div><small>{item.label}</small><strong>{item.text}</strong></div>
      </div>)}</div>
    </section>
    <div id={outputId} className="guide-realization-output" aria-live="polite" aria-atomic="true">
      <svg className="guide-mapping" viewBox="0 0 600 40" preserveAspectRatio="none" aria-hidden="true" focusable="false">
        {variant.realizations.flatMap((realization, index) => realization.capability_indexes.map(capabilityIndex =>
          <path key={`${index}-${capabilityIndex}`} d={`M ${(capabilityIndex + .5) * 600 / scene.items.length} 0 C ${(capabilityIndex + .5) * 600 / scene.items.length} 20, ${(index + .5) * 600 / variant.realizations.length} 20, ${(index + .5) * 600 / variant.realizations.length} 40`}/>))}
      </svg>
      <div className="guide-realizations" style={{ gridTemplateColumns: `repeat(${variant.realizations.length}, minmax(0, 1fr))` }}>
        {variant.realizations.map((realization, index) => <div className="guide-realization" key={`${variant.id}-${index}`}>
          <strong>{realization.label}</strong>
          <span className="guide-realization-meaning">Contribue à :</span>
          <ul>{realization.capability_indexes.map(capabilityIndex => <li key={capabilityIndex}>
            <span className="guide-capability-mark" aria-hidden="true">{mark(capabilityIndex)}</span>
            <span>{scene.items[capabilityIndex]?.text}</span>
          </li>)}</ul>
        </div>)}
      </div>
      <p className="guide-variant-description">{variant.description}</p>
    </div>
    <p className="guide-scene-caption">{scene.caption}</p>
  </div>;
}

function LessonScene({ scene }: { scene: GuideLesson['scene'] }) {
  if (scene.variants?.length) return <TechnicalScene scene={scene}/>;
  return <div className={`guide-scene guide-scene-${scene.kind}`}>
    {scene.parent && <p className="guide-parent">{scene.parent}</p>}
    <div className={`guide-scene-pieces${scene.connector && scene.items.length === 2 ? ' with-connector' : ''}`}>
      {scene.items.map((item, index) => <div className="guide-scene-unit" key={index}>
        <div className="guide-piece"><small>{item.label}</small><strong>{item.text}</strong></div>
        {index === 0 && scene.connector && scene.items.length === 2 && <span className="guide-connector">{scene.connector}</span>}
      </div>)}
    </div>
    <p className="guide-scene-caption">{scene.caption}</p>
  </div>;
}

function Lesson({ guide, lesson, model, index }: { guide: ModelingGuide; lesson: GuideLesson; model: PublishedModel; index: number }) {
  const [choice, setChoice] = useState<number>();
  const [explained, setExplained] = useState(false);
  const titleId = useId();
  const questionId = useId();
  const answerId = useId();
  const sourceIds = new Set(lesson.contributor.source_refs);
  const sources = guide.sources.filter(source => sourceIds.has(source.id));
  const modelLinks = lesson.model_links.filter(link => model.nodeById.has(link.id));
  const missingLinks = lesson.model_links.filter(link => !model.nodeById.has(link.id));
  const answer = choice !== undefined ? lesson.choices[choice]?.feedback : explained ? lesson.explanation : undefined;

  return <article className="guide-lesson" aria-labelledby={titleId}>
    <div className="guide-lesson-heading">
      <p className="guide-kicker">Clé {String(index + 1).padStart(2, '0')} / {String(guide.lessons.length).padStart(2, '0')}<span>Découvrir</span></p>
      <h2 id={titleId}>{lesson.title}</h2>
      <p className="guide-rule">{lesson.rule}</p>
    </div>
    <LessonScene scene={lesson.scene}/>
    <section className="guide-exercise" aria-labelledby={questionId}>
      <h3 id={questionId}>{lesson.question}</h3>
      <div className="guide-choices" role="group" aria-labelledby={questionId}>
        {lesson.choices.map((item, itemIndex) => <button type="button" key={itemIndex} aria-pressed={choice === itemIndex}
          aria-controls={answerId} onClick={() => { setChoice(itemIndex); setExplained(false); }}>{item.label}</button>)}
      </div>
      <button type="button" className="guide-reveal" aria-controls={answerId} aria-expanded={answer !== undefined}
        onClick={() => { setChoice(undefined); setExplained(true); }}>Voir directement l’explication<ChevronDown size={14} aria-hidden="true"/></button>
      <div id={answerId} className={`guide-answer${answer ? ' is-visible' : ''}`} role="status" aria-atomic="true">{answer && <p>{answer}</p>}</div>
    </section>
    <details className="guide-contribute">
      <summary><BookOpen size={17} aria-hidden="true"/>Pour contribuer<span>Critères, frontières et sources</span></summary>
      <div className="guide-contributor-content">
        <div className="guide-detail-grid">
          <section><h3>Le critère utile</h3><p>{lesson.contributor.criterion}</p></section>
          <section><h3>La frontière à préserver</h3><p>{lesson.contributor.boundary}</p></section>
        </div>
        <section className="guide-scope"><h3>Portée du principe et de l’exemple</h3><p>{lesson.contributor.scope}</p><p className="guide-established">Repère établi le {readableDate(lesson.established_at)}.</p></section>
        {lesson.model_links.length > 0 && <section className="guide-model-links">
          <h3>Dans la publication {model.version}</h3>
          {modelLinks.length > 0 && <ul>{modelLinks.map(link => <li key={link.id}><ReferenceLink target={link.id}>{model.nodeById.get(link.id)!.name}<ArrowUpRight size={13} aria-hidden="true"/></ReferenceLink></li>)}</ul>}
          {missingLinks.length > 0 && <p className="guide-unpublished">{missingLinks.map(link => link.label).join(' · ')} : {missingLinks.length === 1 ? 'exemple absent' : 'exemples absents'} de cette publication. L’illustration ci-dessus reste pédagogique.</p>}
        </section>}
        <details className="guide-sources">
          <summary>Sources et portée<span>{sources.length} {sources.length === 1 ? 'extrait figé' : 'extraits figés'}</span></summary>
          <p className="guide-source-intro">Ces extraits sont conservés avec la version {guide.version} du guide.</p>
          {sources.map(source => <section key={source.id} className="guide-source">
            <h3>{source.id} · {source.title}</h3>
            <blockquote>{source.excerpt}</blockquote>
            <p>{source.scope}</p>
          </section>)}
        </details>
      </div>
    </details>
  </article>;
}

export function ModelingGuidePage({ model, selected, onSelect }: { model: PublishedModel; selected?: string; onSelect: (id: string) => void }) {
  const [state, setState] = useState<LoadState>({ version: model.version, status: 'loading' });
  const [attempt, setAttempt] = useState(0);

  useEffect(() => {
    const version = model.version;
    const controller = new AbortController();
    let cancelled = false;
    setState({ version, status: 'loading' });
    fetchModelingGuide(version, controller.signal).then(response => {
      if (!cancelled) setState({ version, status: 'ready', response });
    }).catch((error: unknown) => {
      if (!cancelled && !controller.signal.aborted) setState({ version, status: 'error', message: error instanceof Error ? error.message : 'Le guide n’a pas pu être chargé.' });
    });
    return () => { cancelled = true; controller.abort(); };
  }, [model.version, attempt]);

  if (state.version !== model.version || state.status === 'loading') return <section className="guide-status" role="status" aria-live="polite"><p>Chargement des clés du modèle pour {model.version}…</p></section>;
  if (state.status === 'error') return <section className="guide-status"><div role="alert"><h2>Le guide n’est pas accessible</h2><p>{state.message}</p></div><button type="button" className="secondary-button" onClick={() => setAttempt(value => value + 1)}><RefreshCw size={16} aria-hidden="true"/>Réessayer</button></section>;
  const { response } = state;
  if (response.status === 'unavailable' || !response.guide) return <section className="guide-status"><BookOpen size={28} aria-hidden="true"/><h2>Guide non associé à cette publication</h2><p>{response.message}</p><small>Publication {model.version}</small></section>;
  const { guide } = response;
  const index = selected ? guide.lessons.findIndex(lesson => lesson.id === selected) : 0;
  const lesson = guide.lessons[index];

  return <div className="modeling-guide-page">
    <div className="guide-edition">
      <p>Guide {guide.version}<span aria-hidden="true"> · </span><span>Principes au {readableDate(guide.as_of)}</span></p>
      <p className="guide-association">{response.association?.note || response.message}</p>
    </div>
    <nav className="guide-topics" aria-label="Choisir un principe">
      {guide.lessons.map((item, itemIndex) => <button type="button" key={item.id} aria-pressed={item.id === lesson?.id}
        onClick={() => onSelect(item.id)}><span className="guide-topic-number" aria-hidden="true">{String(itemIndex + 1).padStart(2, '0')}</span><span>{item.label}</span></button>)}
    </nav>
    {lesson ? <Lesson key={`${model.version}:${guide.version}:${lesson.id}`} guide={guide} lesson={lesson} model={model} index={index}/>
      : <section className="guide-status"><h2>Principe absent de ce guide</h2><p>La référence « {selected} » ne figure pas dans cette version. Choisis l’un des repères ci-dessus.</p></section>}
    <p className="guide-footer">Explore librement. Les choix servent à comprendre les principes ; ils ne sont pas enregistrés.</p>
  </div>;
}

import { useEffect, useRef, useState } from 'react';
import { BookOpen, Search } from 'lucide-react';
import type { PublishedModel } from '../types';
import { ModelText, ReferenceLink } from './ModelLinks';
import { plainInlineText } from '../inlineLinks';

export function GlossaryPage({ model, selected }: { model: PublishedModel; selected?: string }) {
  const [query, setQuery] = useState('');
  const detail = useRef<HTMLElement>(null);
  const term = selected ? model.glossaryById.get(selected) : undefined;
  useEffect(() => { if (selected) { setQuery(''); detail.current?.focus(); } }, [selected, model.version]);
  const matches = model.glossary.filter(t => `${t.id} ${plainInlineText(t.name)} ${plainInlineText(t.short_description)} ${plainInlineText(t.definition)}`.toLocaleLowerCase('fr').includes(query.toLocaleLowerCase('fr')));
  if (!model.glossary.length) return <section className="glossary-empty"><BookOpen size={30}/><h2>Glossaire non publié dans cette version</h2><p>Cette publication ne contient pas de glossaire structuré. Il sera disponible dans une prochaine release.</p></section>;
  return <div className="glossary-page">
    <section className="glossary-index" aria-label="Termes du glossaire"><label className="glossary-search"><Search size={17}/><input aria-label="Rechercher dans le glossaire" placeholder="Un terme, une définition…" value={query} onChange={e => setQuery(e.target.value)}/></label><p>{matches.length} termes dans cette publication</p>
      <ul>{matches.map(t => <li key={t.id}><ReferenceLink kind="glossary" target={t.id} className={t.id === selected ? 'selected' : ''}>{plainInlineText(t.name)}</ReferenceLink><small>{t.id}{t.historical ? ' · historique' : ''}</small></li>)}</ul>
    </section>
    {term ? <article className="glossary-term" id={`term-${term.id}`} ref={detail} tabIndex={-1} aria-label={`Définition de ${term.name}`}><p className="eyebrow">{term.id}{term.historical ? ' · Sens historique' : ''}</p><h2>{plainInlineText(term.name)}</h2>
      <section id={`term-${term.id}-short-description`}><h3>Description courte</h3><p><ModelText text={term.short_description}/></p></section>
      <section id={`term-${term.id}-definition`}><h3>Définition</h3><p><ModelText text={term.definition}/></p></section>
      {term.context && <section><h3>Contexte</h3><p><ModelText text={term.context}/></p></section>}
      {term.notes && <section><h3>Précisions</h3><p><ModelText text={term.notes}/></p></section>}
      <section><h3>Portée et provenance</h3><p>{({ proposed: 'Proposé par l’IA', under_review: 'En cours d’instruction', accepted: 'Validé dans sa portée', partial: 'Partiellement validé' })[term.review.state] || term.review.state}</p><p>{term.review.note}</p><p>Sources : {term.source_refs.join(', ') || 'Non renseignées'}.</p><small>Publication {model.version}{term.revision ? ` · révision ${term.revision}` : ''}</small></section>
    </article> : <section className="glossary-empty"><h2>{selected ? 'Terme absent de cette publication' : 'Explorer les notions'}</h2><p>{selected ? `La référence ${selected} n’existe pas dans ce glossaire.` : 'Survole un terme pour lire sa description courte, puis ouvre sa fiche.'}</p></section>}
  </div>;
}

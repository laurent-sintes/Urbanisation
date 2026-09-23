import { useEffect, useMemo, useRef, useState, type ReactNode } from 'react';
import { ArrowLeft, ExternalLink, Search, X } from 'lucide-react';
import type { PublishedModel, SourceLocator } from '../types';
import { normalizeSourceText as normalize, sourceMatches } from '../sourceSearch';
import './details.css';

type Source = { id: string; locator?: SourceLocator };
type DocumentData = { path: string; title: string; content: string; anchor?: string };
type LocalSource = { id: string; locator: SourceLocator };
const slug = (text: string) => normalize(text).replace(/[^a-z0-9\s-]/g, '').trim().replace(/\s+/g, '-');
function highlight(text: string, query: string): ReactNode {
  const matches = sourceMatches(text, query), parts: ReactNode[] = [];
  if (!matches.length) return text;
  let position = 0;
  for (const { start, end } of matches) {
    parts.push(text.slice(position, start), <mark key={start}>{text.slice(start, end)}</mark>);
    position = end;
  }
  parts.push(text.slice(position)); return parts;
}
function inline(text: string, path: string, query: string, onFollow: (source: LocalSource) => void): ReactNode[] {
  const parts: ReactNode[] = [], pattern = /(`[^`]+`|\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\))/g;
  let offset = 0;
  for (const match of text.matchAll(pattern)) {
    parts.push(highlight(text.slice(offset, match.index), query));
    const token = match[0], key = match.index;
    if (token.startsWith('`')) parts.push(<code key={key}>{highlight(token.slice(1, -1), query)}</code>);
    else if (token.startsWith('**')) parts.push(<strong key={key}>{highlight(token.slice(2, -2), query)}</strong>);
    else {
      const link = token.match(/^\[([^\]]+)\]\(([^)]+)\)$/)!;
      const target = link[2].trim().replace(/^<|>$/g, '');
      let url: URL | undefined;
      try { url = new URL(target, new URL(path, `${location.origin}/`)); } catch { /* Invalid target is displayed as text. */ }
      if (url && ['http:', 'https:'].includes(url.protocol) && url.origin !== location.origin) parts.push(<a key={key} href={url.href} target="_blank" rel="noopener noreferrer">{highlight(link[1], query)}<ExternalLink size={11} aria-hidden="true"/></a>);
      else if (url && url.origin === location.origin && url.pathname.endsWith('.md')) {
        try { const locator = { path: decodeURIComponent(url.pathname.slice(1)), anchor: decodeURIComponent(url.hash.slice(1)) }; parts.push(<button type="button" className="source-doc-link" key={key} onClick={() => onFollow({ id: link[1], locator })}>{highlight(link[1], query)}</button>); } catch { parts.push(highlight(link[1], query)); }
      } else parts.push(highlight(link[1], query));
    }
    offset = match.index! + token.length;
  }
  parts.push(highlight(text.slice(offset), query)); return parts;
}
function renderDocument(data: DocumentData, query: string, onFollow: (source: LocalSource) => void): ReactNode[] {
  const lines = data.content.split(/\r?\n/), output: ReactNode[] = [], anchors = new Map<string, number>();
  const rich = (text: string) => inline(text, data.path, query, onFollow);
  let index = 0;
  while (index < lines.length) {
    const line = lines[index], number = index + 1;
    if (/^\s*```/.test(line)) {
      const code: string[] = []; index++;
      while (index < lines.length && !/^\s*```/.test(lines[index])) code.push(lines[index++]);
      output.push(<pre key={number} data-line={number} tabIndex={-1}><code>{highlight(code.join('\n'), query)}</code></pre>); index++; continue;
    }
    const explicit = line.match(/^\s*<a\s+(?:id|name)=["']([^"']+)["']\s*><\/a>\s*$/i);
    if (explicit) { output.push(<div key={number} data-anchor={explicit[1]} data-line={number} tabIndex={-1}/>); index++; continue; }
    const heading = line.match(/^(#{1,6})\s+(.+)$/);
    if (heading) {
      const base = slug(heading[2]), duplicate = anchors.get(base) || 0; anchors.set(base, duplicate + 1);
      const Tag = `h${Math.min(heading[1].length + 1, 6)}` as 'h2' | 'h3' | 'h4' | 'h5' | 'h6';
      output.push(<Tag key={number} data-anchor={`${base}${duplicate ? `-${duplicate}` : ''}`} data-line={number} tabIndex={-1}>{rich(heading[2])}</Tag>); index++; continue;
    }
    if (line.trim().startsWith('|') && /^\s*\|?\s*:?-{3,}/.test(lines[index + 1] || '')) {
      const cells = (row: string) => row.trim().replace(/^\||\|$/g, '').split('|').map(cell => cell.trim());
      const head = cells(line), rows: string[][] = []; index += 2;
      while (index < lines.length && lines[index].trim().startsWith('|')) rows.push(cells(lines[index++]));
      output.push(<div className="source-doc-table" key={number} data-line={number} tabIndex={0} aria-label="Tableau de la source"><table><thead><tr>{head.map((cell, i) => <th key={i} scope="col">{rich(cell)}</th>)}</tr></thead><tbody>{rows.map((row, i) => <tr key={i}>{row.map((cell, j) => <td key={j}>{rich(cell)}</td>)}</tr>)}</tbody></table></div>); continue;
    }
    if (/^\s*[-*]\s+/.test(line)) {
      const items: string[] = [];
      while (index < lines.length && /^\s*[-*]\s+/.test(lines[index])) items.push(lines[index++].replace(/^\s*[-*]\s+/, ''));
      output.push(<ul key={number} data-line={number} tabIndex={-1}>{items.map((item, i) => <li key={i}>{rich(item)}</li>)}</ul>); continue;
    }
    if (/^\s*\d+\.\s+/.test(line)) {
      const items: string[] = [], start = Number(line.match(/^\s*(\d+)/)![1]);
      while (index < lines.length && /^\s*\d+\.\s+/.test(lines[index])) items.push(lines[index++].replace(/^\s*\d+\.\s+/, ''));
      output.push(<ol key={number} data-line={number} start={start} tabIndex={-1}>{items.map((item, i) => <li key={i}>{rich(item)}</li>)}</ol>); continue;
    }
    if (/^\s*---+\s*$/.test(line)) output.push(<hr key={number} data-line={number}/>);
    else if (line.trim()) output.push(<p key={number} data-line={number} tabIndex={-1}>{rich(line)}</p>);
    index++;
  }
  return output;
}

export function SourceDialog({ model, source, onClose }: { model: PublishedModel; source: Source | null; onClose: () => void }) {
  const dialog = useRef<HTMLDialogElement>(null), body = useRef<HTMLDivElement>(null), trigger = useRef<HTMLElement | null>(null);
  const [trail, setTrail] = useState<LocalSource[]>([]), [data, setData] = useState<DocumentData | null>(null), [error, setError] = useState(''), [query, setQuery] = useState(''), [positionNote, setPositionNote] = useState('');
  const registered = source ? model.sourceReferences[source.id] as SourceLocator | undefined : undefined;
  const base = source ? { id: source.id, locator: source.locator || registered || {} } : null;
  const current = trail.at(-1) || base;
  const path = current?.locator.path || '', anchor = current?.locator.anchor || '', line = current?.locator.line;
  const sourceKey = source ? `${source.id}:${source.locator?.path || registered?.path || ''}:${source.locator?.anchor || registered?.anchor || ''}:${source.locator?.line || registered?.line || ''}` : '';
  useEffect(() => { setTrail([]); }, [sourceKey]);
  useEffect(() => {
    const element = dialog.current;
    if (source && element && !element.open) { trigger.current = document.activeElement instanceof HTMLElement ? document.activeElement : null; element.showModal(); }
    else if (!source && element?.open) { element.close(); if (trigger.current?.isConnected) trigger.current.focus({ preventScroll: true }); }
  }, [Boolean(source)]);
  useEffect(() => {
    if (!source) return;
    setData(null); setError(''); setQuery(''); setPositionNote('');
    if (!path) { setError('Aucun localisateur documentaire n’est disponible pour cette référence.'); return; }
    const controller = new AbortController();
    fetch(`/api/source?${new URLSearchParams({ path, anchor })}`, { signal: controller.signal, cache: 'no-store' }).then(async response => {
      const value = await response.json();
      if (!response.ok) throw new Error(typeof value.error === 'string' ? value.error : value.error?.message || `Source indisponible (${response.status}).`);
      if (typeof value.content !== 'string') throw new Error('Le contenu documentaire reçu est invalide.');
      return { path: String(value.path || path), title: String(value.title || current?.id || path), content: value.content, anchor } as DocumentData;
    }).then(value => { if (!controller.signal.aborted) setData(value); }).catch(cause => { if (!controller.signal.aborted) setError(cause instanceof Error ? cause.message : String(cause)); });
    return () => controller.abort();
  }, [Boolean(source), path, anchor, line, model.version]);
  useEffect(() => {
    if (!data || !body.current) return;
    const frame = requestAnimationFrame(() => {
      if (!body.current) return;
      body.current.querySelectorAll('.source-doc-target').forEach(element => element.classList.remove('source-doc-target'));
      let target: HTMLElement | undefined;
      if (query.trim()) target = body.current.querySelector<HTMLElement>('mark') || undefined;
      else if (anchor) target = [...body.current.querySelectorAll<HTMLElement>('[data-anchor]')].find(element => normalize(element.dataset.anchor || '') === normalize(anchor));
      if (!target && !query.trim() && line) target = [...body.current.querySelectorAll<HTMLElement>('[data-line]')].reverse().find(element => Number(element.dataset.line) <= line);
      if (target) { target.classList.add('source-doc-target'); target.scrollIntoView({ block: 'start' }); if (!query.trim()) { if (!target.hasAttribute('tabindex')) target.tabIndex = -1; target.focus({ preventScroll: true }); } }
      else body.current.scrollTop = 0;
      setPositionNote(!query.trim() && anchor && !target ? 'Repère non trouvé dans ce document ; contenu complet affiché.' : '');
    });
    return () => cancelAnimationFrame(frame);
  }, [data, anchor, line, query]);
  const rendered = useMemo(() => data ? renderDocument(data, query, next => { setTrail(previous => [...previous, next]); }) : null, [data, query]);
  const count = data ? sourceMatches(data.content, query).length : 0;
  return <dialog ref={dialog} className="source-dialog" aria-labelledby="source-document-title" onCancel={event => { event.preventDefault(); event.stopPropagation(); onClose(); }} onKeyDown={event => { if (event.key === 'Escape') event.stopPropagation(); }}>
    <header><div><span className="section-kicker">Source documentaire · texte complet</span><h2 id="source-document-title">{data?.title || (error ? 'Source indisponible' : current?.id || 'Source')}</h2></div><button type="button" className="source-close" aria-label="Fermer la source" onClick={onClose} autoFocus><X size={22}/></button></header>
    <div className="source-toolbar">{trail.length > 0 && <button type="button" className="source-return" onClick={() => setTrail(previous => previous.slice(0, -1))}><ArrowLeft size={15}/>Source précédente</button>}<label className="source-search"><Search size={16} aria-hidden="true"/><input aria-label="Rechercher dans la source" placeholder="Rechercher dans ce document…" value={query} disabled={!data} onChange={event => setQuery(event.target.value)}/>{query && <button type="button" aria-label="Effacer la recherche dans la source" onClick={() => setQuery('')}><X size={15}/></button>}</label>{query.trim() && <span role="status">{count} correspondance{count > 1 ? 's' : ''}</span>}</div>
    <p className="source-location">{path}{anchor ? ` #${anchor}` : ''}{line ? ` · ligne ${line}` : ''}<span>{positionNote}</span></p>
    <div ref={body} className="source-document" data-testid="source-document" tabIndex={-1}>{error ? <p role="alert">{error}</p> : data ? rendered : <p role="status">Chargement du document complet…</p>}</div>
  </dialog>;
}

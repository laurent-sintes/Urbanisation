import { useEffect, useRef, useState, type KeyboardEvent, type RefObject } from 'react';
import { ChevronDown, ChevronRight, Search, X, PanelLeftClose, Compass, BookOpen, Lightbulb } from 'lucide-react';
import type { AtlasNode, PublishedModel } from '../types';
import { childrenOf, lineageOf, parentRelationOf, rootsOf } from '../model';
import { searchPublication, type SearchResult } from '../search';
import { kindLabel } from '../presentation';
import { NodeIcon } from '../icons';
import { startsDecisionSection } from '../capabilityTypes';
import { preference, savePreference, type RouteState } from '../navigation';

interface Props {
  model: PublishedModel; route: RouteState; open: boolean; mobile: boolean;
  searchRef: RefObject<HTMLInputElement | null>;
  onClose: () => void; onNavigate: (id: string, focusHeading?: boolean) => void;
  onSearch: (changes: Partial<RouteState>) => void;
  onOpenGlossary: (mode: 'model' | 'meta') => void;
  onOpenTerm: (id: string) => void;
  onOpenPrinciples: () => void;
}
export function Sidebar({ model, route, open, mobile, searchRef, onClose, onNavigate, onSearch, onOpenGlossary, onOpenTerm, onOpenPrinciples }: Props) {
  const tree = useRef<HTMLDivElement>(null);
  const panel = useRef<HTMLElement>(null);
  const revealed = useRef('');
  const [expanded, setExpanded] = useState<Set<string>>(() => {
    const saved = preference<unknown>('expanded', []);
    return new Set(Array.isArray(saved) ? saved.filter(x => typeof x === 'string') : []);
  });
  const [focused, setFocused] = useState(route.node);
  const searching = Boolean(route.query || route.type);
  useEffect(() => {
    const ancestors = lineageOf(model, route.node).map(n => n.id);
    setExpanded(previous => new Set([...previous, ...ancestors]));
    setFocused(route.node);
  }, [model, route.node]);
  useEffect(() => savePreference('expanded', [...expanded]), [expanded]);
  useEffect(() => {
    const key = `${model.version}:${route.node}`;
    if (searching || revealed.current === key || !tree.current) return;
    const item = [...tree.current.querySelectorAll<HTMLElement>('[data-tree-id]')].find(el => el.dataset.treeId === route.node);
    const row = item?.firstElementChild as HTMLElement | undefined;
    if (!row) return;
    const bounds = tree.current.getBoundingClientRect(), rect = row.getBoundingClientRect();
    if (rect.bottom > bounds.bottom) tree.current.scrollTop += rect.bottom - bounds.bottom + 14;
    if (rect.top < bounds.top) tree.current.scrollTop -= bounds.top - rect.top + 14;
    revealed.current = key;
  }, [expanded, model.version, route.node, searching]);
  useEffect(() => {
    if (!open || !mobile) return;
    const previous = document.activeElement as HTMLElement | null;
    panel.current?.querySelector<HTMLButtonElement>('.drawer-close')?.focus();
    const key = (event: globalThis.KeyboardEvent) => {
      if (event.key === 'Escape') { event.preventDefault(); onClose(); }
      if (event.key !== 'Tab') return;
      const items = [...(panel.current?.querySelectorAll<HTMLElement>('button:not([disabled]):not([tabindex="-1"]),input,select,[role="treeitem"][tabindex="0"]') || [])].filter(el => el.offsetParent !== null);
      const first = items[0], last = items.at(-1);
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last?.focus(); }
      if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first?.focus(); }
    };
    document.addEventListener('keydown', key);
    return () => { document.removeEventListener('keydown', key); previous?.focus(); };
  }, [open, mobile, onClose]);
  const toggle = (id: string, value = !expanded.has(id)) => {
    if (!value && lineageOf(model, focused).some(node => node.id === id)) setFocused(id);
    setExpanded(previous => {
      const next = new Set(previous); value ? next.add(id) : next.delete(id); return next;
    });
  };
  const visibleIds: string[] = [];
  const visit = (node: AtlasNode) => { visibleIds.push(node.id); if (expanded.has(node.id)) childrenOf(model, node.id).forEach(visit); };
  rootsOf(model).filter(n => !['object','document','event'].includes(n.kind)).forEach(visit);
  const tabStop = visibleIds.includes(focused) ? focused : lineageOf(model, focused).reverse().find(node => visibleIds.includes(node.id))?.id || visibleIds[0];
  const focus = (id?: string) => {
    if (!id) return;
    setFocused(id);
    [...(tree.current?.querySelectorAll<HTMLElement>('[role="treeitem"]') || [])].find(el => el.dataset.treeId === id)?.focus();
  };
  const keydown = (event: KeyboardEvent<HTMLElement>, node: AtlasNode) => {
    if (event.target !== event.currentTarget) return;
    const items = [...(tree.current?.querySelectorAll<HTMLElement>('[role="treeitem"]') || [])];
    const index = items.indexOf(event.currentTarget);
    const ids = childrenOf(model, node.id).map(n => n.id);
    if (!['ArrowDown','ArrowUp','ArrowLeft','ArrowRight','Home','End','Enter',' '].includes(event.key)) return;
    event.preventDefault(); event.stopPropagation();
    if (event.key === 'ArrowDown') focus(items[index + 1]?.dataset.treeId);
    if (event.key === 'ArrowUp') focus(items[index - 1]?.dataset.treeId);
    if (event.key === 'Home') focus(items[0]?.dataset.treeId);
    if (event.key === 'End') focus(items.at(-1)?.dataset.treeId);
    if (event.key === 'ArrowRight' && ids.length) expanded.has(node.id) ? focus(ids[0]) : toggle(node.id, true);
    if (event.key === 'ArrowLeft') expanded.has(node.id) && ids.length ? toggle(node.id, false) : focus(parentRelationOf(model, node.id)?.sourceId);
    if (event.key === 'Enter' || event.key === ' ') onNavigate(node.id, mobile);
  };
  const renderNode = (node: AtlasNode, depth: number, decisionStart = false) => {
    const children = childrenOf(model, node.id);
    const isExpanded = expanded.has(node.id);
    return <li key={node.id} role="treeitem" data-tree-id={node.id} className={decisionStart ? 'decision-section-start' : undefined} aria-label={`${node.name} · ${kindLabel(node)}`}
      aria-level={depth} aria-expanded={children.length ? isExpanded : undefined} aria-selected={route.node === node.id}
      tabIndex={tabStop === node.id ? 0 : -1}
      onFocus={e => e.target === e.currentTarget && setFocused(node.id)} onKeyDown={e => keydown(e, node)}>
      <div className={`tree-row ${route.node === node.id ? 'selected' : ''}`} style={{ paddingLeft: (depth - 1) * 14 + 4 }} onClick={() => onNavigate(node.id)}>
        {children.length ? <button className="tree-toggle" tabIndex={-1} aria-label={`${isExpanded ? 'Replier' : 'Déplier'} ${node.name}`} data-tree-toggle={node.id} onClick={e => { e.stopPropagation(); toggle(node.id); }}>
          {isExpanded ? <ChevronDown size={13} /> : <ChevronRight size={13} />}
        </button> : <span className="tree-spacer" />}
        <NodeIcon node={node} size={17} />
        <span className="tree-label" title={`${node.id} · ${kindLabel(node)}`}>{node.name}</span>
        {children.length > 0 && <small>{children.length}</small>}
      </div>
      {children.length > 0 && isExpanded && <ul role="group">{children.map((child, index) => renderNode(child, depth + 1, startsDecisionSection(children, index)))}</ul>}
    </li>;
  };
  const results: SearchResult[] = route.query.trim() ? searchPublication(model, route.query)
    : route.type === 'glossary' ? model.glossary.map(term => ({ id: term.id, kind: 'glossary', name: term.name, excerpt: '', score: 0, term }))
    : model.nodes.map(node => ({ id: node.id, kind: 'model', name: node.name, excerpt: '', score: 0, node }));
  const matches = results.filter(result => !route.type || (result.kind !== 'model' ? route.type === result.kind : result.node?.kind === route.type));
  const kinds = [...new Set(model.nodes.map(n => n.kind))];
  return <aside ref={panel} id="atlas-tree-panel" className={`sidebar ${open ? 'open' : ''}`} aria-label="Navigation du modèle" aria-modal={mobile && open ? true : undefined} role={mobile && open ? 'dialog' : undefined}>
    <div className="sidebar-heading"><button className="root-link" onClick={() => onNavigate('')}><Compass size={20} />Urbanisation</button>
      <button className="drawer-close" aria-label="Fermer l’arbre" onClick={onClose}><PanelLeftClose size={20} /></button></div>
    <div className="search-box"><Search size={17} /><input ref={searchRef} id="fa-search" aria-label="Rechercher dans le modèle publié" placeholder="Un nom, une idée, un repère…" value={route.query} onChange={e => onSearch({ query: e.target.value })} onKeyDown={e => {
      if (e.key === 'ArrowDown') { e.preventDefault(); panel.current?.querySelector<HTMLButtonElement>('[data-search-result]')?.focus(); }
      if (e.key === 'Escape') onSearch({ query: '', type: '', status: '' });
    }} />{searching ? <button aria-label="Effacer la recherche et les filtres" onClick={() => onSearch({ query: '', type: '', status: '' })}><X size={14} /></button> : <kbd>Ctrl K</kbd>}</div>
    <div className="search-filters">
      <select id="fa-type" aria-label="Type d’élément" value={route.type} onChange={e => onSearch({ type: e.target.value })}><option value="">Tous les types</option>{kinds.map(kind => <option key={kind} value={kind}>{({ capability: 'Capacités', behavior: 'Comportements', domain: 'Domaines', reference: 'Référentiels', group: 'Univers et groupes', object: 'Objets métier', document: 'Documents', event: 'Événements' } as Record<string, string>)[kind] || kind}</option>)}<option value="glossary">Termes du glossaire</option></select>
    </div>
    {searching ? <div className="search-results" aria-label="Résultats de recherche"><p role="status">{matches.length} résultat{matches.length > 1 ? 's' : ''}</p>{matches.map(result => <button key={`${result.kind}:${result.id}`} data-search-result={result.id} onClick={() => result.kind === 'glossary' ? onOpenTerm(result.id) : onNavigate(result.id, true)} onKeyDown={e => {
      if (e.key === 'ArrowDown') { e.preventDefault(); (e.currentTarget.nextElementSibling as HTMLElement)?.focus(); }
      if (e.key === 'ArrowUp') { e.preventDefault(); const previous = e.currentTarget.previousElementSibling; previous?.tagName === 'BUTTON' ? (previous as HTMLElement).focus() : searchRef.current?.focus(); }
    }}>{result.node ? <NodeIcon node={result.node} size={20} framed /> : <BookOpen size={22}/>}<span><strong>{result.name}</strong><small>{result.node ? `${kindLabel(result.node)} · ${lineageOf(model, result.id).slice(0, -1).map(n => n.name).join(' / ')}` : 'Terme du glossaire'} · {result.id}</small>{result.excerpt && <span className="search-excerpt">{result.excerpt}</span>}</span></button>)}{!matches.length && <p>Aucun élément ne correspond dans cette publication.</p>}</div>
      : <div className="model-tree" ref={tree} role="tree" aria-label="Arbre d’urbanisation"><ul role="group">{rootsOf(model).filter(n => !['object','document','event'].includes(n.kind)).map(n => renderNode(n, 1))}</ul></div>}
    <nav className="sidebar-help" aria-label="Aide à la lecture">
      <button className="glossary-nav" onClick={() => onOpenGlossary('model')} aria-current={route.view === 'glossary' && route.glossary !== 'meta' ? 'page' : undefined}><BookOpen size={17}/>Glossaire métier</button>
      <button className="glossary-nav" onClick={() => onOpenGlossary('meta')} aria-current={route.view === 'glossary' && route.glossary === 'meta' ? 'page' : undefined}><BookOpen size={17}/>Glossaire du méta modèle</button>
      <button className="glossary-nav principles-nav" onClick={onOpenPrinciples} aria-current={route.view === 'principles' ? 'page' : undefined}><Lightbulb size={17}/>Comprendre le méta modèle</button>
    </nav>
    <div className="sidebar-bottom"><div className="sidebar-stats"><span>{model.nodes.length} éléments</span><span>{model.nodes.filter(n => n.kind === 'capability').length} capacités{model.nodes.some(n => n.kind === 'behavior') && <> · {model.nodes.filter(n => n.kind === 'behavior').length} comportements</>}</span></div><img className="beaumanoir-source-logo" src="/assets/beaumanoir-original.png" width="1564" height="605" alt="Groupe Beaumanoir" /></div>
  </aside>;
}

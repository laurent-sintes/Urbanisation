import { lazy, Suspense, useCallback, useEffect, useRef, useState, type KeyboardEvent } from 'react';
import { createRoot } from 'react-dom/client';
import { ArrowLeft, ArrowRight, ArrowUpRight, Box, Check, ChevronDown, ChevronRight, FileText, FlaskConical, GitBranch, Layers, Maximize2, Menu, Network, Search, X } from 'lucide-react';
import { adaptPublication, childrenOf, lineageOf, parentsOf, relatedTo, rootsOf, searchModel } from './model';
import { kindLabel, shortText, statusLabel } from './presentation';
import type { AtlasNode, AtlasRelation, PublishedModel, SourceLocator } from './types';
import { ReactFlowPane } from './ReactFlowPane';
import manifest from '../.generated/likec4-manifest.json';
import './styles.css';
const LikeC4Pane = lazy(() => import('./LikeC4Pane').then(m => ({ default: m.LikeC4Pane })));
type View = 'map' | 'sheet' | 'relations';
type Engine = 'react-flow' | 'likec4';
function initialState() {
  const params = new URLSearchParams(location.hash.slice(1));
  return { selected: params.get('node') || 'universe-supply', scope: params.get('scope') || 'universe-supply', view: (['map', 'sheet', 'relations'].includes(params.get('view') || '') ? params.get('view') : 'map') as View, engine: (params.get('engine') === 'likec4' ? 'likec4' : 'react-flow') as Engine };
}
function App() {
  const [model, setModel] = useState<PublishedModel>();
  const [error, setError] = useState('');
  const [requestedVersion, setRequestedVersion] = useState(() => new URLSearchParams(location.hash.slice(1)).get('version') || manifest.publication);
  const [state, setState] = useState(initialState);
  const [expanded, setExpanded] = useState(() => new Set(['universe-supply', 'D04']));
  const [query, setQuery] = useState('');
  const [drawer, setDrawer] = useState(false);
  const [relationId, setRelationId] = useState<string>();
  const [depth, setDepth] = useState<1 | 2>(1);
  const [direction, setDirection] = useState<'both' | 'incoming' | 'outgoing'>('both');
  const [perspective, setPerspective] = useState('');
  const [source, setSource] = useState<{ id: string; locator: SourceLocator; content?: string; error?: string }>();
  const sourceDialog = useRef<HTMLDialogElement>(null);
  const searchInput = useRef<HTMLInputElement>(null);
  const tree = useRef<HTMLDivElement>(null);
  const menuButton = useRef<HTMLButtonElement>(null);
  const sourceTrigger = useRef<HTMLElement | null>(null);
  const pendingSearchFocus = useRef(false);
  useEffect(() => {
    const abort = new AbortController();
    if (requestedVersion && requestedVersion !== manifest.publication) {
      setError(`Cet essai est préparé pour ${manifest.publication}, mais le lien demande ${requestedVersion}. Aucune autre publication n’a été chargée.`);
      return;
    }
    // Both engines use the exact publication from the generated LikeC4 projection.
    fetch(`/api/model?version=${encodeURIComponent(manifest.publication)}`, { signal: abort.signal }).then(async r => { if (!r.ok) throw new Error(`Publication indisponible (${r.status})`); return r.json(); }).then(raw => {
      const parsed = adaptPublication(raw);
      setModel(parsed);
      setState(s => ({ ...s, selected: parsed.nodeById.has(s.selected) ? s.selected : rootsOf(parsed)[0].id, scope: parsed.nodeById.has(s.scope) ? s.scope : rootsOf(parsed)[0].id }));
    }).catch(e => { if (e.name !== 'AbortError') setError(e.message); });
    return () => abort.abort();
  }, [requestedVersion]);
  useEffect(() => {
    const restore = () => {
      const version = new URLSearchParams(location.hash.slice(1)).get('version');
      setRequestedVersion(version || manifest.publication);
      if (version && version !== manifest.publication) { setError(`Ce lien demande ${version} ; cet essai est préparé pour ${manifest.publication}.`); return; }
      const next = initialState();
      if (model && (!model.nodeById.has(next.selected) || !model.nodeById.has(next.scope))) { setError('L’élément demandé est absent de la publication préparée.'); return; }
      setError(''); setState(next);
    };
    window.addEventListener('hashchange', restore);
    return () => window.removeEventListener('hashchange', restore);
  }, [model]);
  useEffect(() => {
    if (error || !model) return;
    const url = new URLSearchParams({ version: manifest.publication, node: state.selected, scope: state.scope, view: state.view, engine: state.engine });
    history.replaceState(null, '', `#${url}`);
  }, [state, error, model]);
  useEffect(() => {
    if (model) setExpanded(old => new Set([...old, ...lineageOf(model, state.selected).slice(0, -1).map(n => n.id)]));
    setRelationId(previous => {
      const relation = previous ? model?.relationById.get(previous) : undefined;
      return relation && [relation.sourceId, relation.targetId].includes(state.selected) ? previous : undefined;
    });
  }, [model, state.selected]);
  useEffect(() => {
    const handler = (event: globalThis.KeyboardEvent) => {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
        event.preventDefault();
        if (matchMedia('(max-width: 960px)').matches) { pendingSearchFocus.current = true; setDrawer(true); }
        else searchInput.current?.focus();
      }
      if (event.key === 'Escape') { setQuery(''); if (drawer) { setDrawer(false); menuButton.current?.focus(); } }
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, [drawer]);
  useEffect(() => { if (drawer && pendingSearchFocus.current) { searchInput.current?.focus(); pendingSearchFocus.current = false; } }, [drawer]);
  useEffect(() => {
    if (source) sourceDialog.current?.showModal();
    else { sourceDialog.current?.close(); sourceTrigger.current?.focus(); }
  }, [Boolean(source)]);
  const select = useCallback((id: string) => setState(s => ({ ...s, selected: id })), []);
  const read = useCallback((id: string) => { setState(s => ({ ...s, selected: id, view: 'sheet' })); setDrawer(false); setQuery(''); }, []);
  const explore = useCallback((id: string) => {
    if (!model) return;
    const hasChildren = childrenOf(model, id).length > 0;
    setState(s => ({ ...s, selected: id, scope: hasChildren ? id : parentsOf(model, id)[0]?.id || id, view: hasChildren ? 'map' : 'sheet' }));
    setDrawer(false); setQuery('');
  }, [model]);
  const openRelations = useCallback((id: string) => { setState(s => ({ ...s, selected: id, view: 'relations' })); setDirection('both'); setDepth(1); setDrawer(false); }, []);
  const selectRelation = useCallback((id: string) => {
    const relation = model?.relationById.get(id);
    if (!relation) return;
    setRelationId(id);
    setState(s => ({ ...s, selected: [relation.sourceId, relation.targetId].includes(s.selected) ? s.selected : relation.targetId, view: 'relations' }));
  }, [model]);
  const openSource = async (id: string) => {
    const locator = model?.sourceReferences[id] as SourceLocator | undefined;
    if (!locator?.path) return;
    sourceTrigger.current = document.activeElement as HTMLElement;
    setSource({ id, locator });
    try {
      const response = await fetch(`/api/source?${new URLSearchParams({ path: locator.path, anchor: locator.anchor || '' })}`);
      if (!response.ok) throw new Error('Source indisponible');
      const data = await response.json();
      const lines = String(data.content).split(/\r?\n/);
      const start = lines.findIndex(line => line.trim().toLowerCase() === `## ${id.toLowerCase()}`);
      let end = start + 1;
      while (end < lines.length && !/^##\s/.test(lines[end])) end++;
      const content = start >= 0 ? lines.slice(start, end).join('\n') : lines.slice(Math.max(0, (locator.line || 1) - 1), (locator.line || 1) + 100).join('\n');
      setSource(old => old?.id === id ? { ...old, content } : old);
    } catch (e) { setSource(old => old?.id === id ? { ...old, error: String(e) } : old); }
  };
  function treeKey(event: KeyboardEvent, node: AtlasNode) {
    if (!model) return;
    const items = [...(tree.current?.querySelectorAll<HTMLButtonElement>('[data-tree-id]') || [])];
    const index = items.indexOf(event.currentTarget as HTMLButtonElement);
    if (event.key === 'ArrowDown' || event.key === 'ArrowUp') { event.preventDefault(); items[Math.min(items.length - 1, Math.max(0, index + (event.key === 'ArrowDown' ? 1 : -1)))]?.focus(); }
    if (event.key === 'Home' || event.key === 'End') { event.preventDefault(); items[event.key === 'Home' ? 0 : items.length - 1]?.focus(); }
    if (event.key === 'ArrowRight') { event.preventDefault(); if (childrenOf(model, node.id).length && !expanded.has(node.id)) setExpanded(old => new Set([...old, node.id])); else items[index + 1]?.focus(); }
    if (event.key === 'ArrowLeft') { event.preventDefault(); if (expanded.has(node.id)) setExpanded(old => { const next = new Set(old); next.delete(node.id); return next; }); else { const parent = parentsOf(model, node.id)[0]; items.find(item => item.dataset.treeId === parent?.id)?.focus(); } }
  }
  function treeBranch(node: AtlasNode, level = 0): React.ReactNode {
    const children = childrenOf(model!, node.id);
    return <li key={node.id}>
      <div className={`tree-row ${state.selected === node.id ? 'selected' : ''}`} style={{ paddingLeft: 12 + level * 15 }}>
        {children.length ? <button className="tree-toggle" tabIndex={-1} aria-label={`${expanded.has(node.id) ? 'Replier' : 'Déplier'} ${node.name}`} onClick={() => setExpanded(old => { const next = new Set(old); if (next.has(node.id)) next.delete(node.id); else next.add(node.id); return next; })}>{expanded.has(node.id) ? <ChevronDown size={13}/> : <ChevronRight size={13}/>}</button> : <span className="tree-toggle leaf-mark">·</span>}
        <button data-tree-id={node.id} className="tree-label" aria-current={state.selected === node.id ? 'page' : undefined} aria-expanded={children.length ? expanded.has(node.id) : undefined} onClick={() => explore(node.id)} onKeyDown={e => treeKey(e, node)}>
          {node.kind === 'group' ? <Layers size={14}/> : node.kind === 'domain' ? <Box size={14}/> : <span className="tree-cap-dot"/>}<span>{node.name}</span>{children.length > 0 && <small>{children.length}</small>}
        </button>
      </div>
      {children.length > 0 && expanded.has(node.id) && <ul>{children.map(child => treeBranch(child, level + 1))}</ul>}
    </li>;
  }
  if (error) return <main className="startup"><h1>Publication indisponible</h1><p>{error}</p><p>Le prototype consulte la publication {manifest.publication} sur le serveur Atlas local.</p><button onClick={() => location.reload()}>Réessayer</button></main>;
  if (!model) return <main className="startup"><Layers/><h1>Ouverture de l’Atlas</h1><p>Lecture du modèle publié…</p></main>;
  const selected = model.nodeById.get(state.selected)!;
  const scope = model.nodeById.get(state.scope)!;
  const relations = relatedTo(model, selected.id);
  const relation = relationId ? model.relationById.get(relationId) : state.view === 'relations' ? relations[0] : undefined;
  const results = query.trim() ? searchModel(model, query) : [];
  const sourceButtons = (refs: readonly string[]) => <div className="source-buttons">{refs.map(id => model.sourceReferences[id] ? <button key={id} onClick={() => openSource(id)}>{id}<ArrowUpRight size={12}/></button> : <span key={id}>{id}</span>)}</div>;
  const referenceDetails = (item: AtlasNode | AtlasRelation) => <details className="provenance"><summary><FileText size={15}/>Sources, révision et portée détaillée<ChevronDown size={15}/></summary><div className="provenance-body"><p>Révision {item.revision ?? 'non renseignée'} · Publication {model.version}</p>{item.lifecycle?.state && <p>Instruction : {({ ai_proposed: 'Proposé par l’IA', under_instruction: 'En cours d’instruction', urbanist_validated: 'Validé par l’urbaniste' } as Record<string,string>)[item.lifecycle.state] || item.lifecycle.state}</p>}<p>Champs validés : {item.approvedFields.length ? item.approvedFields.join(', ') : 'aucun champ indiqué ici'}</p><p>Champs proposés : {item.proposedFields.length ? item.proposedFields.join(', ') : 'aucun champ indiqué ici'}</p>{item.lastModified && <p>Dernière modification : {item.lastModified}</p>}{sourceButtons(item.sourceRefs)}</div></details>;
  const relationInspector = (edge: AtlasRelation) => <section className="relation-inspector" data-testid="relation-inspector"><div className="section-kicker"><GitBranch size={15}/>COMPRENDRE LA RELATION<span className={`pill ${edge.status}`}>{statusLabel(edge)}</span></div><div className="relation-endpoints"><button onClick={() => openRelations(edge.sourceId)}>{model.nodeById.get(edge.sourceId)?.name}</button><ArrowRight size={20}/><button onClick={() => openRelations(edge.targetId)}>{model.nodeById.get(edge.targetId)?.name}</button></div><p className="relation-meaning">{edge.qualification.meaning || edge.label}</p><div className="relation-columns">{edge.qualification.conditions?.length ? <div><h3>Conditions</h3><ul>{edge.qualification.conditions.map((c, i) => <li key={i}>{c}</li>)}</ul></div> : null}{edge.qualification.effects?.length ? <div><h3>Effets</h3><ul>{edge.qualification.effects.map((c, i) => <li key={i}>{c}</li>)}</ul></div> : null}</div>{edge.qualification.scope && <p className="scope-note"><strong>Portée publiée</strong> {edge.qualification.scope}</p>}{edge.review.note && <p className="review-note">{edge.review.note}</p>}{referenceDetails(edge)}</section>;
  return <div className="atlas-shell">
    <header className="topbar"><div className="brand"><span className="brand-symbol"><Layers size={21}/></span><span>FLOW <strong>Atlas</strong></span><span className="lab-label"><FlaskConical size={12}/>Exploration</span></div><div className="engine-switch" aria-label="Moteur graphique"><button aria-pressed={state.engine === 'react-flow'} data-testid="engine-react-flow" onClick={() => setState(s => ({ ...s, engine: 'react-flow' }))}>React Flow</button><button aria-pressed={state.engine === 'likec4'} data-testid="engine-likec4" onClick={() => setState(s => ({ ...s, engine: 'likec4' }))}>LikeC4</button></div><a className="atlas-link" href={`http://127.0.0.1:8765/#node=${selected.id}&version=${model.version}`} target="_blank" rel="noreferrer">Atlas courant<ArrowUpRight size={14}/></a></header>
    {drawer && <button className="drawer-scrim" aria-label="Fermer l’arbre" onClick={() => { setDrawer(false); menuButton.current?.focus(); }}/>}
    <aside className={`sidebar ${drawer ? 'open' : ''}`} aria-label="Navigation du modèle"><div className="sidebar-heading"><div><span className="section-kicker">MODÈLE PUBLIÉ</span><h2>Urbanisation</h2></div><span className="version-tag">v{String(model.revision || 3).padStart(3, '0')}</span><button className="drawer-close" aria-label="Fermer l’arbre" onClick={() => { setDrawer(false); menuButton.current?.focus(); }}><X size={18}/></button></div><div className="search-box"><Search size={15}/><input ref={searchInput} aria-label="Rechercher dans le modèle publié" placeholder="Trouver un élément…" value={query} onChange={e => setQuery(e.target.value)} onKeyDown={e => { if (e.key === 'ArrowDown') { e.preventDefault(); document.querySelector<HTMLButtonElement>('[data-search-result]')?.focus(); } if (e.key === 'Enter' && results[0]) read(results[0].id); }}/>{query ? <button aria-label="Effacer la recherche" onClick={() => setQuery('')}><X size={13}/></button> : <kbd>Ctrl K</kbd>}</div>
      {query ? <div className="search-results" aria-live="polite"><span className="section-kicker">{results.length} RÉSULTAT{results.length > 1 ? 'S' : ''}</span>{results.map(n => <button key={n.id} data-search-result={n.id} onClick={() => read(n.id)}><strong>{n.name}</strong><small>{kindLabel(n)} · {lineageOf(model, n.id).slice(0, -1).map(p => p.name).join(' / ')}</small></button>)}{!results.length && <p>Aucun élément publié ne correspond.</p>}</div> : <div className="model-tree" ref={tree}><ul>{rootsOf(model).map(n => treeBranch(n))}</ul></div>}
      <div className="sidebar-bottom"><span className="live-dot"/><span>{model.nodes.length} éléments · {model.nodes.filter(n => n.kind === 'capability').length} capacités<br/><small>Publication {model.version}</small></span></div>
    </aside>
    <main className="workspace" id="main-content"><div className="breadcrumb-row"><button ref={menuButton} className="mobile-menu" onClick={() => setDrawer(true)}><Menu size={17}/>Arbre</button><nav aria-label="Fil d’Ariane"><button onClick={() => explore('universe-supply')}>Urbanisation</button>{lineageOf(model, selected.id).map(n => <span key={n.id}><ChevronRight size={13}/><button onClick={() => explore(n.id)} aria-current={n.id === selected.id ? 'page' : undefined}>{n.name}</button></span>)}</nav><button className="example-button" onClick={() => openRelations('D04.h')}><GitBranch size={14}/>Explorer un lien</button></div>
      <section className="page-heading"><div className="eyebrow"><span>{kindLabel(selected)}</span><span>{selected.id}</span><span className={`pill ${selected.status}`}>{statusLabel(selected)}</span></div><h1>{selected.name}</h1><p>{shortText(selected.purpose || selected.definition || 'Ce périmètre est réservé dans le modèle publié.', 215)}</p></section>
      <div className="view-bar"><div className="view-tabs" role="tablist" aria-label="Façon d’explorer"><button role="tab" aria-selected={state.view === 'map'} onClick={() => setState(s => ({ ...s, view: 'map', scope: childrenOf(model, selected.id).length ? selected.id : parentsOf(model, selected.id)[0]?.id || selected.id }))}><Layers size={16}/>Carte</button><button role="tab" aria-selected={state.view === 'sheet'} onClick={() => setState(s => ({ ...s, view: 'sheet' }))}><FileText size={16}/>Fiche</button><button role="tab" aria-selected={state.view === 'relations'} onClick={() => openRelations(selected.id)}><Network size={16}/>Relations<span className="count">{relations.length}</span></button></div><span className="reading-label"><span className="live-dot"/>Lecture seule</span></div>
      {state.view === 'sheet' ? <div className="sheet" data-testid="business-sheet"><div className="sheet-main"><span className="section-kicker">COMPRENDRE LE MÉTIER</span><h2>Finalité</h2><p>{selected.purpose || 'Finalité non renseignée dans cette publication.'}</p><h2>Définition</h2><p>{selected.definition || 'Définition non renseignée dans cette publication.'}</p>{selected.scope && <><h2>Périmètre</h2><p>{selected.scope}</p></>}{selected.review.note && <div className="review-note"><strong>Portée et réserves</strong><p>{selected.review.note}</p></div>}{referenceDetails(selected)}</div>{childrenOf(model, selected.id).length > 0 && <section className="sheet-children"><h2>Explorer ce périmètre</h2>{childrenOf(model, selected.id).map(n => <button key={n.id} onClick={() => explore(n.id)}><span><small>{kindLabel(n)}</small><strong>{n.name}</strong></span><ArrowRight size={17}/></button>)}</section>}{relations.length > 0 && <button className="primary-button" onClick={() => openRelations(selected.id)}>Explorer les relations<ArrowRight size={16}/></button>}</div> : <>
        <section className="map-panel"><div className="map-toolbar"><div><span className="section-kicker">{state.view === 'map' ? 'CARTE DU PÉRIMÈTRE' : 'VOISINAGE MÉTIER'}</span><strong>{state.view === 'map' ? scope.name : selected.name}</strong></div>{state.view === 'map' ? <div className="map-actions">{parentsOf(model, scope.id)[0] && <button onClick={() => explore(parentsOf(model, scope.id)[0].id)}><ArrowLeft size={14}/>Niveau supérieur</button>}{state.engine === 'react-flow' && <select aria-label="Mettre un statut en évidence" value={perspective} onChange={e => setPerspective(e.target.value)}><option value="">Tous les statuts</option><option value="accepted">Validé dans sa portée</option><option value="partial">Partiellement validé</option><option value="proposed">Proposé</option><option value="under_review">En réexamen</option></select>}</div> : <div className="map-actions">{state.engine === 'react-flow' ? <><select aria-label="Sens des relations" value={direction} onChange={e => setDirection(e.target.value as typeof direction)}><option value="both">Tous les sens</option><option value="incoming">Entrantes</option><option value="outgoing">Sortantes</option></select><select aria-label="Profondeur du voisinage" value={depth} onChange={e => setDepth(Number(e.target.value) as 1 | 2)}><option value="1">Voisins directs</option><option value="2">Jusqu’à 2 liens</option></select></> : <span className="toolbar-note">Voisins directs · tous les sens</span>}</div>}</div>
        <Suspense fallback={<div className="graph-canvas empty-state">Chargement du moteur LikeC4…</div>}>{state.engine === 'react-flow' ? <ReactFlowPane model={model} selectedId={selected.id} scopeId={scope.id} mode={state.view === 'map' ? 'map' : 'relations'} onSelect={select} onExplore={explore} onRead={read} onSelectRelation={selectRelation} relationId={relation?.id} depth={depth} direction={direction} perspective={perspective}/> : <LikeC4Pane model={model} selectedId={selected.id} scopeId={scope.id} mode={state.view === 'map' ? 'map' : 'relations'} onSelect={select} onExplore={explore} onSelectRelation={selectRelation}/>}</Suspense>
        <div className="map-footer"><span><Maximize2 size={13}/>Zoom pour lire · Explorer pour entrer dans un niveau</span><span>{state.engine === 'react-flow' ? 'React Flow' : 'LikeC4'}<Check size={12}/></span></div></section>
        {state.view === 'map' ? <section className="selection-strip"><span className="selection-icon"><Box size={21}/></span><div><span className="section-kicker">ÉLÉMENT SÉLECTIONNÉ</span><strong>{selected.name}</strong><span>{kindLabel(selected)} · {statusLabel(selected)}</span></div><button onClick={() => read(selected.id)}>Ouvrir la fiche<ArrowUpRight size={15}/></button></section> : <section className="accessible-relations"><div className="section-kicker">RELATIONS DIRECTES · {relations.length}</div>{relations.length ? relations.map(r => <button key={r.id} className={relation?.id === r.id ? 'active' : ''} data-relation-id={r.id} onClick={() => setRelationId(r.id)}><span>{model.nodeById.get(r.sourceId)?.name}<ArrowRight size={14}/>{model.nodeById.get(r.targetId)?.name}</span><span className={`pill ${r.status}`}>{statusLabel(r)}</span></button>) : <p>Aucune relation métier publiée pour cet élément.</p>}</section>}
        {state.view === 'relations' && relation && relationInspector(relation)}
      </>}
      <footer className="workspace-footer">Même publication, même sélection, deux moteurs à comparer. Les relations conservent leurs réserves.</footer>
    </main>
    <dialog ref={sourceDialog} className="source-dialog" onCancel={() => setSource(undefined)}><header><div><span className="section-kicker">SOURCE DOCUMENTAIRE</span><h2>{source?.id}</h2></div><button aria-label="Fermer la source" onClick={() => setSource(undefined)} autoFocus><X size={20}/></button></header><p className="source-location">{source?.locator.path}</p><pre>{source?.content || source?.error || 'Chargement de la source…'}</pre></dialog>
  </div>;
}
createRoot(document.getElementById('root')!).render(<App/>);

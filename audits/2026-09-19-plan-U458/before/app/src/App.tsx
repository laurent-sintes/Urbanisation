import { lazy, Suspense, useCallback, useEffect, useRef, useState, type CSSProperties } from 'react';
import { ArrowLeft, ChevronRight, Compass, Copy, FileText, GitBranch, LayoutGrid, Lightbulb, Maximize2, PanelLeft, RefreshCw, X } from 'lucide-react';
import { usePublication } from './usePublication';
import { useModelingGuide } from './useModelingGuide';
import { childrenOf, hasCapabilityCards, lineageOf, parentRelationOf, relatedTo } from './model';
import { kindLabel } from './presentation';
import { NodeIcon } from './icons';
import { preference, readRoute, routeHash, savePreference, type RouteState, type View } from './navigation';
import { Sidebar } from './components/Sidebar';
import { BusinessSheet } from './components/BusinessSheet';
import { GlossaryPage } from './components/GlossaryPage';
import { ModelLinksProvider, ModelText } from './components/ModelLinks';

const ReactFlowPane = lazy(() => import('./ReactFlowPane').then(module => ({ default: module.ReactFlowPane })));
const DependenciesPane = lazy(() => import('./DependenciesPane').then(module => ({ default: module.DependenciesPane })));
const ModelingGuidePage = lazy(() => import('./components/ModelingGuidePage').then(module => ({ default: module.ModelingGuidePage })));
const clampWidth = (width: number) => Math.min(420, Math.max(240, Number.isFinite(width) ? width : 300));
function initialRoute() {
  const saved = preference<string>('selection', '');
  return readRoute(location.hash || (typeof saved === 'string' ? saved : ''));
}
function useMobile() {
  const [mobile, setMobile] = useState(() => matchMedia('(max-width: 1000px)').matches);
  useEffect(() => {
    const query = matchMedia('(max-width: 1000px)');
    const update = () => setMobile(query.matches);
    query.addEventListener('change', update);
    return () => query.removeEventListener('change', update);
  }, []);
  return mobile;
}
export function App() {
  const [route, setRoute] = useState(initialRoute);
  const { model, loading, error, notice, reload } = usePublication(route.version || undefined);
  const { state: guideState, retry: retryGuide } = useModelingGuide(model?.version);
  const metaGlossary = guideState.status === 'ready' ? guideState.response.guide?.glossary : undefined;
  const isMetaTerm = (id: string) => metaGlossary?.model_term_ids.includes(id) || metaGlossary?.terms.some(term => term.id === id);
  const glossaryMode = route.term && isMetaTerm(route.term) ? 'meta' : route.glossary || 'model';
  const glossaryTitle = glossaryMode === 'meta' ? 'Glossaire du méta modèle' : 'Glossaire métier';
  const mobile = useMobile();
  const [drawer, setDrawer] = useState(false);
  const [width, setWidth] = useState(() => clampWidth(Number(preference('tree-width', 300))));
  const [announcement, setAnnouncement] = useState('');
  const search = useRef<HTMLInputElement>(null);
  const heading = useRef<HTMLHeadingElement>(null);
  const mapPanel = useRef<HTMLElement>(null);
  const selected = model?.nodeById.get(route.node);
  const view: View = route.view || (selected && !childrenOf(model!, selected.id).length ? 'sheet' : 'map');
  const validScope = route.scope && model?.nodeById.has(route.scope) ? route.scope : '';
  const scopeId = route.scope === '@root' ? undefined : validScope || (selected ? (childrenOf(model!, selected.id).length || ['group', 'domain', 'reference'].includes(selected.kind) ? selected.id : parentRelationOf(model!, selected.id)?.sourceId) : undefined);
  const scope = scopeId ? model?.nodeById.get(scopeId) : undefined;
  // The map heading describes its stable context; selection stays in the strip below.
  const referenceView = view === 'glossary' || view === 'principles';
  const headingNode = referenceView ? undefined : view === 'map' ? scope : selected;
  const changeRoute = useCallback((changes: Partial<RouteState>, replace = false) => {
    setRoute(previous => {
      const next = { ...previous, ...changes };
      history[replace ? 'replaceState' : 'pushState']({}, '', routeHash(next));
      return next;
    });
  }, []);
  const closeDrawer = useCallback(() => setDrawer(false), []);
  const followReference = useCallback((kind: 'glossary' | 'model', id: string, section = '') => {
    changeRoute({ version: model?.version || route.version, view: kind === 'glossary' ? 'glossary' : 'sheet', glossary: isMetaTerm(id) ? 'meta' : 'model',
      node: kind === 'model' ? id : '', term: kind === 'glossary' ? id : '', section, principle: '',
      scope: '', relation: '', source: '', anchor: '', sourceId: '', query: '', type: '', status: '' });
    setDrawer(false);
    if (!section && kind === 'model') setTimeout(() => heading.current?.focus({ preventScroll: true }), 30);
  }, [changeRoute, model?.version, route.version, metaGlossary]);
  const openGlossary = useCallback((glossary: 'model' | 'meta' = 'model') => {
    changeRoute({ view: 'glossary', glossary, node: '', term: '', principle: '', section: '', scope: '', relation: '', source: '', anchor: '', sourceId: '' });
    setDrawer(false);
    setTimeout(() => heading.current?.focus({ preventScroll: true }), 30);
  }, [changeRoute]);
  const openPrinciples = useCallback(() => {
    changeRoute({ view: 'principles', principle: '', node: '', term: '', section: '', scope: '', relation: '', source: '', anchor: '', sourceId: '', query: '', type: '', status: '' });
    setDrawer(false);
    setTimeout(() => heading.current?.focus({ preventScroll: true }), 30);
  }, [changeRoute]);
  useEffect(() => {
    if (!route.section || !model || view === 'principles') return;
    const timer = requestAnimationFrame(() => {
      const target = document.getElementById(view === 'glossary' ? `term-${route.term}-${route.section}` : `field-${route.node}-${route.section}`);
      if (target) { target.tabIndex = -1; target.focus({ preventScroll: true }); target.scrollIntoView({ block: 'center' }); }
    });
    return () => cancelAnimationFrame(timer);
  }, [route.section, route.term, route.node, model, view]);
  useEffect(() => {
    const back = () => { setRoute(readRoute(location.hash)); setDrawer(false); };
    window.addEventListener('hashchange', back);
    return () => window.removeEventListener('hashchange', back);
  }, []);
  useEffect(() => {
    // Remember only the selected location. There is no visit history.
    savePreference('selection', routeHash({ ...route, version: '', query: '', type: '', status: '', source: '', anchor: '', sourceId: '' }));
    history.replaceState({}, '', routeHash(route));
  }, [route]);
  useEffect(() => savePreference('tree-width', width), [width]);
  useEffect(() => {
    if (model && route.node && !model.nodeById.has(route.node)) {
      setAnnouncement(`L’élément ${route.node} n’existe pas dans cette publication. Retour à Urbanisation.`);
      changeRoute({ node: '', scope: '', view: 'map', relation: '' }, true);
    } else if (model && route.scope && route.scope !== '@root' && !model.nodeById.has(route.scope)) {
      setAnnouncement('Le périmètre de cette carte n’existe pas dans la publication. Le contexte de l’élément est rétabli.');
      changeRoute({ scope: '' }, true);
    }
  }, [model, route.node, route.scope, changeRoute]);
  useEffect(() => {
    const shortcut = (event: KeyboardEvent) => {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
        event.preventDefault(); if (mobile) setDrawer(true);
        setTimeout(() => search.current?.focus(), 30);
      }
    };
    document.addEventListener('keydown', shortcut);
    return () => document.removeEventListener('keydown', shortcut);
  }, [mobile]);
  const navigate = useCallback((id: string, focusHeading = true) => {
    changeRoute({ node: id, scope: '', view: undefined, term: '', principle: '', section: '', query: '', type: '', status: '', relation: '', source: '', anchor: '', sourceId: '' });
    setDrawer(false);
    if (focusHeading) setTimeout(() => heading.current?.focus({ preventScroll: true }), 50);
  }, [changeRoute]);
  const explore = useCallback((id: string) => {
    changeRoute({ node: id, scope: id, view: 'map', relation: '' });
  }, [changeRoute]);
  const read = useCallback((id: string) => {
    changeRoute({ node: id, view: 'sheet', relation: '' });
    setTimeout(() => heading.current?.focus({ preventScroll: true }), 30);
  }, [changeRoute]);
  const select = useCallback((id: string) => changeRoute({ node: id, scope: scopeId || '@root', relation: '' }), [changeRoute, scopeId]);
  const links = selected && model ? relatedTo(model, selected.id) : [];
  const copyLink = async () => {
    try {
      const pinned = { ...route, version: model?.version || route.version };
      const hash = routeHash(pinned);
      await navigator.clipboard.writeText(`${location.origin}/${hash.startsWith('#') ? hash : ''}`);
      setAnnouncement('Lien copié vers cette publication.');
    } catch { setAnnouncement('La copie est indisponible. Tu peux copier l’adresse dans le navigateur.'); }
  };
  const revision = model?.revision ? `v${String(model.revision).padStart(3, '0')}` : 'Publication';
  return <ModelLinksProvider value={{ model: model || null, route, onFollow: followReference }}><div className="atlas-shell" style={{ '--sidebar': `${width}px` } as CSSProperties}>
    <header className="topbar" inert={mobile && drawer}>
      <button className="brand" onClick={() => navigate('')} aria-label="FLOW Atlas, accueil"><span className="brand-symbol" aria-hidden="true"><img className="flow-source-mark" src="/assets/flow-original.png" width="1024" height="1024" alt="" /></span><strong>FLOW <b>Atlas</b></strong></button>
      <span className="topbar-context"><img className="beaumanoir-source-logo" src="/assets/beaumanoir-original.png" width="1564" height="605" alt="Groupe Beaumanoir" /></span>
      <button id="fa-refresh" className={`topbar-icon ${loading ? 'loading' : ''}`} aria-label="Actualiser la publication" title="Actualiser" disabled={loading} onClick={reload}><RefreshCw size={17} /></button>
    </header>
    {model && <Sidebar model={model} route={{ ...route, glossary: glossaryMode }} open={drawer} mobile={mobile} searchRef={search} onClose={closeDrawer} onNavigate={navigate} onOpenGlossary={openGlossary} onOpenPrinciples={openPrinciples} onSearch={changes => changeRoute(changes, true)} />}
    {model && <div className="rail-resizer" role="separator" tabIndex={0} aria-label="Largeur de l’arbre" aria-orientation="vertical" aria-valuemin={240} aria-valuemax={420} aria-valuenow={width}
      onKeyDown={e => { if (['ArrowLeft','ArrowRight','Home','End'].includes(e.key)) { e.preventDefault(); setWidth(value => e.key === 'Home' ? 240 : e.key === 'End' ? 420 : clampWidth(value + (e.key === 'ArrowRight' ? 10 : -10))); } }}
      onPointerDown={e => { e.currentTarget.setPointerCapture(e.pointerId); }}
      onPointerMove={e => { if (e.currentTarget.hasPointerCapture(e.pointerId)) setWidth(clampWidth(e.clientX)); }}
      onPointerUp={e => e.currentTarget.releasePointerCapture(e.pointerId)} />}
    {drawer && mobile && <button className="drawer-scrim" tabIndex={-1} aria-label="Fermer l’arbre" onClick={closeDrawer} />}
    <main id="fa-main" className={`workspace ${!model ? 'without-model' : ''}`} inert={mobile && drawer} aria-busy={loading}>
      {(error || notice || announcement) && <div className={`notice ${error ? 'error' : ''}`} role={error ? 'alert' : 'status'}>{error || notice || announcement}<button aria-label="Masquer le message" onClick={() => setAnnouncement('')} hidden={!announcement}><X size={14} /></button></div>}
      {!model ? <div className="empty-state"><Compass size={34} /><h1>{loading ? 'Ouverture du modèle…' : 'Publication indisponible'}</h1><p>{loading ? 'Chargement de l’Urbanisation publiée.' : 'Réessaie de charger la publication.'}</p>{!loading && <button className="secondary-button" onClick={reload}>Réessayer</button>}</div> : <>
        <div className="breadcrumb-row"><button id="fa-tree-open" className="mobile-menu" aria-expanded={drawer} aria-controls="atlas-tree-panel" onClick={() => setDrawer(true)}><PanelLeft size={16} />Arbre</button>
          <nav aria-label="Fil d’Ariane"><button onClick={() => navigate('')} aria-current={!headingNode && !referenceView ? 'page' : undefined}>Urbanisation</button>{headingNode && lineageOf(model, headingNode.id).map(node => <span key={node.id}><ChevronRight size={12} /><button onClick={() => navigate(node.id)} aria-current={headingNode.id === node.id ? 'page' : undefined}>{node.name}</button></span>)}{referenceView && <span><ChevronRight size={12}/><span aria-current="page">{view === 'principles' ? 'Comprendre le méta modèle' : glossaryTitle}</span></span>}</nav>
          <button className="share-button" onClick={copyLink}><Copy size={14} /><span>Copier le lien</span></button>
        </div>
        <header className="page-heading"><div className="heading-icon">{headingNode ? <NodeIcon node={headingNode} size={30} framed /> : <span className="node-icon framed tone-universe">{view === 'principles' ? <Lightbulb size={30} /> : <Compass size={30} />}</span>}</div><div>
          <div className="eyebrow"><span>{headingNode ? kindLabel(headingNode) : view === 'principles' ? 'LE MÉTA MODÈLE' : view === 'glossary' ? 'LE VOCABULAIRE PUBLIÉ' : 'LE MODÈLE PUBLIÉ'}</span>{headingNode && <span>{headingNode.id}</span>}</div>
          <h1 id="page-title" ref={heading} tabIndex={-1}>{view === 'principles' ? 'Comprendre le méta modèle' : view === 'glossary' ? glossaryTitle : headingNode?.name || 'Urbanisation'}</h1>
          {view !== 'sheet' && <p><ModelText text={view === 'principles' ? 'Six repères pour lire la carte et contribuer à sa construction.' : view === 'glossary' ? 'Les notions et leurs définitions dans la publication consultée.' : headingNode?.purpose || (headingNode ? 'Explore cet élément et ses relations dans le modèle publié.' : 'Parcours les univers, explore les capacités et découvre les liens qui les relient.')}/></p>}
        </div></header>
        <div className="view-bar"><div className="view-tabs" style={referenceView ? { display: 'none' } : undefined} role="tablist" aria-label="Vue du modèle">{([{ id: 'map', label: 'Carte', Icon: LayoutGrid }, { id: 'sheet', label: 'Fiche', Icon: FileText }, { id: 'relations', label: 'Relations', Icon: GitBranch }] as const).filter(tab => selected || tab.id !== 'sheet').map(tab => <button key={tab.id} role="tab" id={`tab-${tab.id}`} aria-controls="atlas-view" tabIndex={view === tab.id ? 0 : -1} aria-selected={view === tab.id} onClick={() => changeRoute({ view: tab.id, relation: '' })} onKeyDown={e => {
          if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
          e.preventDefault(); const items = [...e.currentTarget.parentElement!.querySelectorAll<HTMLButtonElement>('button')];
          items[(items.indexOf(e.currentTarget) + (e.key === 'ArrowRight' ? 1 : items.length - 1)) % items.length].click();
          items[(items.indexOf(e.currentTarget) + (e.key === 'ArrowRight' ? 1 : items.length - 1)) % items.length].focus();
        }}><tab.Icon size={16} />{tab.label}{tab.id === 'relations' && selected && !['group', 'domain', 'reference'].includes(selected.kind) && <span className="count">{links.length}</span>}</button>)}</div><span id="fa-version" className="reading-label">{revision} · {model.version}<span className={`live-dot ${route.version ? 'fixed' : ''}`} title={route.version ? 'Version fixe' : 'Suit la publication courante'} /></span></div>
        <div id="atlas-view" role={referenceView ? 'region' : 'tabpanel'} aria-labelledby={referenceView ? 'page-title' : `tab-${view === 'sheet' && !selected ? 'map' : view}`}>
          {view === 'principles' ? <Suspense fallback={<p role="status">Ouverture du méta modèle…</p>}><ModelingGuidePage key={model.version} model={model} selected={route.principle} state={guideState} retry={retryGuide} onSelect={principle => changeRoute({ principle })} /></Suspense> : view === 'glossary' ? <GlossaryPage model={model} selected={route.term} mode={glossaryMode} guideState={guideState} onRetry={retryGuide} onSelect={term => changeRoute({ view: 'glossary', glossary: glossaryMode, term, section: '' })}/> : view === 'sheet' && selected ? <BusinessSheet model={model} node={selected} /> : view === 'relations' ? <Suspense fallback={<div className="graph-canvas empty-state">Ouverture des relations…</div>}><DependenciesPane key={`${model.version}:${route.node}`} model={model} focusId={selected?.id} relationId={route.relation} settings={route} onSettings={changes => changeRoute(changes)} onSelectRelation={relation => changeRoute({ relation }, true)} onFocus={node => changeRoute({ node, scope: '', relation: '', view: 'relations', graphDepth: node ? 1 : 0 })} onRead={read}/></Suspense> : <>
            <section className="map-panel" ref={mapPanel} aria-label="Carte du modèle">
              <div className="map-toolbar"><div><strong>{scope?.name || 'Vue d’ensemble'}</strong><span className="toolbar-note">Entre dans une carte pour explorer son contenu.</span></div>
                <div className="map-actions">
                  {scope && <button onClick={() => navigate(parentRelationOf(model, scope.id)?.sourceId || '')}><ArrowLeft size={14} />Remonter</button>}
                <button aria-label="Afficher la carte en plein écran" title="Plein écran" onClick={() => { if (document.fullscreenElement) void document.exitFullscreen(); else void mapPanel.current?.requestFullscreen().catch(() => setAnnouncement('Le plein écran est indisponible dans ce navigateur.')); }}><Maximize2 size={16} /></button></div>
              </div>
              <Suspense fallback={<div className="graph-canvas empty-state">Ouverture de la carte…</div>}><ReactFlowPane model={model} selectedId={selected?.id || ''} scopeId={scopeId} onSelect={select} onExplore={explore} onRead={read} perspective="" /></Suspense>
              <div className="map-footer"><span>{hasCapabilityCards(model, scopeId) ? 'Cliquer sur un lien pour lire sa fiche · Faire défiler pour parcourir' : 'Molette pour zoomer · Glisser pour parcourir'}</span><span>Lecture seule</span></div>
            </section>
            {selected && <div className="selection-strip"><NodeIcon node={selected} size={24} framed /><div><strong>{selected.name}</strong><span>{kindLabel(selected)}</span></div><button className="secondary-button" onClick={() => read(selected.id)}>Ouvrir la fiche<ChevronRight size={14} /></button></div>}
          </>}
        </div>
        <footer className="workspace-footer">Urbanisation · {route.version ? 'Publication fixe' : 'Publication courante, actualisée automatiquement'}</footer>
      </>}
    </main>
  </div></ModelLinksProvider>;
}

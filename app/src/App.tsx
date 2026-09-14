import { lazy, Suspense, useCallback, useEffect, useMemo, useRef, useState, type CSSProperties } from 'react';
import { ArrowLeft, ChevronRight, Compass, Copy, FileText, GitBranch, LayoutGrid, Maximize2, PanelLeft, RefreshCw, X } from 'lucide-react';
import { usePublication } from './usePublication';
import { childrenOf, lineageOf, neighborhood, parentRelationOf, relatedTo } from './model';
import { kindLabel, statusLabel } from './presentation';
import { NodeIcon } from './icons';
import { preference, readRoute, routeHash, savePreference, type RouteState, type View } from './navigation';
import { Sidebar } from './components/Sidebar';
import { BusinessSheet, RelationDetails } from './components/BusinessSheet';
import { SourceDialog } from './components/SourceDialog';
import { GlossaryPage } from './components/GlossaryPage';
import { ModelLinksProvider, ModelText } from './components/ModelLinks';
import type { SourceLocator } from './types';

const ReactFlowPane = lazy(() => import('./ReactFlowPane').then(module => ({ default: module.ReactFlowPane })));
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
  const { model, catalog, loading, error, notice, reload } = usePublication(route.version || undefined);
  const mobile = useMobile();
  const [drawer, setDrawer] = useState(false);
  const [width, setWidth] = useState(() => clampWidth(Number(preference('tree-width', 300))));
  const [announcement, setAnnouncement] = useState('');
  const [depth, setDepth] = useState<1 | 2>(1);
  const [direction, setDirection] = useState<'both' | 'incoming' | 'outgoing'>('both');
  const [perspective, setPerspective] = useState('');
  const search = useRef<HTMLInputElement>(null);
  const heading = useRef<HTMLHeadingElement>(null);
  const mapPanel = useRef<HTMLElement>(null);
  const selected = model?.nodeById.get(route.node);
  const view: View = route.view || (selected && !childrenOf(model!, selected.id).length ? 'sheet' : 'map');
  const validScope = route.scope && model?.nodeById.has(route.scope) ? route.scope : '';
  const scopeId = route.scope === '@root' ? undefined : validScope || (selected ? (childrenOf(model!, selected.id).length || ['group', 'domain', 'reference'].includes(selected.kind) ? selected.id : parentRelationOf(model!, selected.id)?.sourceId) : undefined);
  const scope = scopeId ? model?.nodeById.get(scopeId) : undefined;
  // The map heading describes its stable context; selection stays in the strip below.
  const headingNode = view === 'glossary' ? undefined : view === 'map' ? scope : selected;
  const changeRoute = useCallback((changes: Partial<RouteState>, replace = false) => {
    setRoute(previous => {
      const next = { ...previous, ...changes };
      history[replace ? 'replaceState' : 'pushState']({}, '', routeHash(next));
      return next;
    });
  }, []);
  const closeDrawer = useCallback(() => setDrawer(false), []);
  const followReference = useCallback((kind: 'glossary' | 'model', id: string, section = '') => {
    changeRoute({ version: model?.version || route.version, view: kind === 'glossary' ? 'glossary' : 'sheet',
      node: kind === 'model' ? id : '', term: kind === 'glossary' ? id : '', section,
      scope: '', relation: '', source: '', anchor: '', sourceId: '', query: '', type: '', status: '' });
    setDrawer(false);
    if (!section && kind === 'model') setTimeout(() => heading.current?.focus({ preventScroll: true }), 30);
  }, [changeRoute, model?.version, route.version]);
  const openGlossary = useCallback(() => {
    changeRoute({ view: 'glossary', node: '', term: '', section: '', scope: '', relation: '', source: '', anchor: '', sourceId: '' });
    setDrawer(false);
    setTimeout(() => heading.current?.focus({ preventScroll: true }), 30);
  }, [changeRoute]);
  useEffect(() => {
    if (!route.section || !model) return;
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
    changeRoute({ node: id, scope: '', view: undefined, term: '', section: '', query: '', type: '', status: '', relation: '', source: '', anchor: '', sourceId: '' });
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
  const openSource = useCallback((id: string, locator?: SourceLocator) => {
    const reference = locator || model?.sourceReferences[id] as SourceLocator | undefined;
    if (reference?.path) changeRoute({ source: reference.path, anchor: reference.anchor || '', sourceId: id });
    else setAnnouncement(`Aucun document source disponible pour ${id}.`);
  }, [model, changeRoute]);
  const closeSource = useCallback(() => changeRoute({ source: '', anchor: '', sourceId: '' }, true), [changeRoute]);
  const source = useMemo(() => route.source ? { id: route.sourceId || route.anchor || route.source.split('/').at(-1) || 'Source', locator: { path: route.source, anchor: route.anchor } } : null, [route.source, route.anchor, route.sourceId]);
  const links = selected && model ? relatedTo(model, selected.id) : [];
  const projection = selected && model && view === 'relations' ? neighborhood(model, selected.id, { depth, direction }) : undefined;
  const relation = model?.relationById.get(route.relation);
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
      <button className="brand" onClick={() => navigate('')} aria-label="FLOW Atlas, accueil"><span className="brand-symbol"><Compass size={23} /></span><strong>FLOW <b>Atlas</b></strong></button>
      <span className="topbar-context">Le modèle métier, en perspective</span>
      <div className="publication-picker"><label htmlFor="fa-publication">Version publiée</label><select id="fa-publication" value={route.version} onChange={e => { setAnnouncement(''); changeRoute({ version: e.target.value, relation: '' }); }}>
        <option value="">Publication courante</option>
        {catalog?.releases.map(release => <option key={release.version} value={release.version}>{release.revision ? `v${String(release.revision).padStart(3, '0')} · ` : ''}{release.version}</option>)}
      </select></div>
      <button id="fa-refresh" className={`topbar-icon ${loading ? 'loading' : ''}`} aria-label="Actualiser la publication" title="Actualiser" disabled={loading} onClick={reload}><RefreshCw size={17} /></button>
    </header>
    {model && <Sidebar model={model} route={route} open={drawer} mobile={mobile} searchRef={search} onClose={closeDrawer} onNavigate={navigate} onOpenGlossary={openGlossary} onSearch={changes => changeRoute(changes, true)} />}
    {model && <div className="rail-resizer" role="separator" tabIndex={0} aria-label="Largeur de l’arbre" aria-orientation="vertical" aria-valuemin={240} aria-valuemax={420} aria-valuenow={width}
      onKeyDown={e => { if (['ArrowLeft','ArrowRight','Home','End'].includes(e.key)) { e.preventDefault(); setWidth(value => e.key === 'Home' ? 240 : e.key === 'End' ? 420 : clampWidth(value + (e.key === 'ArrowRight' ? 10 : -10))); } }}
      onPointerDown={e => { e.currentTarget.setPointerCapture(e.pointerId); }}
      onPointerMove={e => { if (e.currentTarget.hasPointerCapture(e.pointerId)) setWidth(clampWidth(e.clientX)); }}
      onPointerUp={e => e.currentTarget.releasePointerCapture(e.pointerId)} />}
    {drawer && mobile && <button className="drawer-scrim" tabIndex={-1} aria-label="Fermer l’arbre" onClick={closeDrawer} />}
    <main id="fa-main" className={`workspace ${!model ? 'without-model' : ''}`} inert={mobile && drawer} aria-busy={loading}>
      {(error || notice || announcement) && <div className={`notice ${error ? 'error' : ''}`} role={error ? 'alert' : 'status'}>{error || notice || announcement}<button aria-label="Masquer le message" onClick={() => setAnnouncement('')} hidden={!announcement}><X size={14} /></button></div>}
      {!model ? <div className="empty-state"><Compass size={34} /><h1>{loading ? 'Ouverture du modèle…' : 'Publication indisponible'}</h1><p>{loading ? 'Chargement de l’Urbanisation publiée.' : 'Réessaie ou sélectionne une autre publication.'}</p>{!loading && <button className="secondary-button" onClick={reload}>Réessayer</button>}</div> : <>
        <div className="breadcrumb-row"><button id="fa-tree-open" className="mobile-menu" aria-expanded={drawer} aria-controls="atlas-tree-panel" onClick={() => setDrawer(true)}><PanelLeft size={16} />Arbre</button>
          <nav aria-label="Fil d’Ariane"><button onClick={() => navigate('')} aria-current={!headingNode && view !== 'glossary' ? 'page' : undefined}>Urbanisation</button>{headingNode && lineageOf(model, headingNode.id).map(node => <span key={node.id}><ChevronRight size={12} /><button onClick={() => navigate(node.id)} aria-current={headingNode.id === node.id ? 'page' : undefined}>{node.name}</button></span>)}{view === 'glossary' && <span><ChevronRight size={12}/><span aria-current="page">Glossaire</span></span>}</nav>
          <button className="share-button" onClick={copyLink}><Copy size={14} /><span>Copier le lien</span></button>
        </div>
        <header className="page-heading"><div className="heading-icon">{headingNode ? <NodeIcon node={headingNode} size={30} framed /> : <span className="node-icon framed tone-universe"><Compass size={30} /></span>}</div><div>
          <div className="eyebrow"><span>{headingNode ? kindLabel(headingNode) : view === 'glossary' ? 'LE VOCABULAIRE PUBLIÉ' : 'LE MODÈLE PUBLIÉ'}</span>{headingNode && <span>{headingNode.id}</span>}{headingNode && <span className={`pill ${headingNode.status}`}>{statusLabel(headingNode)}</span>}</div>
          <h1 id="page-title" ref={heading} tabIndex={-1}>{view === 'glossary' ? 'Glossaire' : headingNode?.name || 'Urbanisation'}</h1>
          {view !== 'sheet' && <p><ModelText text={view === 'glossary' ? 'Les notions et leurs définitions dans la publication consultée.' : headingNode?.purpose || (headingNode ? 'Explore cet élément et ses relations dans le modèle publié.' : 'Parcours les univers, explore les capacités et découvre les liens qui les relient.')}/></p>}
        </div></header>
        <div className="view-bar"><div className="view-tabs" style={view === 'glossary' ? { display: 'none' } : undefined} role="tablist" aria-label="Vue du modèle">{([{ id: 'map', label: 'Carte', Icon: LayoutGrid }, { id: 'sheet', label: 'Fiche', Icon: FileText }, { id: 'relations', label: 'Relations', Icon: GitBranch }] as const).filter(tab => selected || tab.id === 'map').map(tab => <button key={tab.id} role="tab" id={`tab-${tab.id}`} aria-controls="atlas-view" tabIndex={view === tab.id ? 0 : -1} aria-selected={view === tab.id} onClick={() => changeRoute({ view: tab.id, relation: '' })} onKeyDown={e => {
          if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
          e.preventDefault(); const items = [...e.currentTarget.parentElement!.querySelectorAll<HTMLButtonElement>('button')];
          items[(items.indexOf(e.currentTarget) + (e.key === 'ArrowRight' ? 1 : items.length - 1)) % items.length].click();
          items[(items.indexOf(e.currentTarget) + (e.key === 'ArrowRight' ? 1 : items.length - 1)) % items.length].focus();
        }}><tab.Icon size={16} />{tab.label}{tab.id === 'relations' && <span className="count">{links.length}</span>}</button>)}</div><span id="fa-version" className="reading-label">{revision} · {model.version}<span className={`live-dot ${route.version ? 'fixed' : ''}`} title={route.version ? 'Version fixe' : 'Suit la publication courante'} /></span></div>
        <div id="atlas-view" role={view === 'glossary' ? 'region' : 'tabpanel'} aria-labelledby={view === 'glossary' ? 'page-title' : `tab-${selected ? view : 'map'}`}>
          {view === 'glossary' ? <GlossaryPage model={model} selected={route.term}/> : view === 'sheet' && selected ? <BusinessSheet model={model} node={selected} onOpenSource={openSource} /> : <>
            <section className="map-panel" ref={mapPanel} aria-label={view === 'relations' ? 'Graphe des relations métier' : 'Carte du modèle'}>
              <div className="map-toolbar"><div><strong>{view === 'relations' ? `Autour de ${selected?.name}` : scope?.name || 'Vue d’ensemble'}</strong><span className="toolbar-note">{view === 'relations' ? 'Suis les liens pour comprendre les interactions.' : 'Entre dans une carte pour explorer son contenu.'}</span></div>
                <div className="map-actions">{view === 'relations' ? <>
                  <select aria-label="Profondeur des relations" value={depth} onChange={e => setDepth(Number(e.target.value) as 1 | 2)}><option value="1">Voisins directs</option><option value="2">À deux pas</option></select>
                  <select aria-label="Sens des relations" value={direction} onChange={e => setDirection(e.target.value as typeof direction)}><option value="both">Tous les sens</option><option value="incoming">Entrantes</option><option value="outgoing">Sortantes</option></select>
                </> : <>
                  {scope && <button onClick={() => navigate(parentRelationOf(model, scope.id)?.sourceId || '')}><ArrowLeft size={14} />Remonter</button>}
                  <select aria-label="Mettre en évidence un statut" value={perspective} onChange={e => setPerspective(e.target.value)}><option value="">Tous les statuts</option>{[...new Set(model.nodes.map(n => n.status))].map(status => <option key={status} value={status}>{statusLabel({ status } as typeof model.nodes[number])}</option>)}</select>
                </>}<button aria-label="Afficher la carte en plein écran" title="Plein écran" onClick={() => { if (document.fullscreenElement) void document.exitFullscreen(); else void mapPanel.current?.requestFullscreen().catch(() => setAnnouncement('Le plein écran est indisponible dans ce navigateur.')); }}><Maximize2 size={16} /></button></div>
              </div>
              <Suspense fallback={<div className="graph-canvas empty-state">Ouverture de la carte…</div>}><ReactFlowPane model={model} selectedId={selected?.id || ''} scopeId={scopeId} mode={view === 'relations' && selected ? 'relations' : 'map'} onSelect={select} onExplore={explore} onRead={read} onSelectRelation={id => changeRoute({ relation: id, view: 'relations', node: view === 'relations' ? route.node : model.relationById.get(id)?.sourceId || route.node })} relationId={route.relation} depth={depth} direction={direction} perspective={perspective} /></Suspense>
              <div className="map-footer"><span>{view === 'relations' ? `${projection?.relations.length || 0} relation(s) affichée(s)${projection?.hiddenRelationCount ? ` · ${projection.hiddenRelationCount} hors du voisinage` : ''}` : 'Molette pour zoomer · Glisser pour parcourir'}</span><span>Lecture seule</span></div>
            </section>
            {selected && <div className="selection-strip"><NodeIcon node={selected} size={24} framed /><div><strong>{selected.name}</strong><span>{kindLabel(selected)} · {statusLabel(selected)}</span></div><button className="secondary-button" onClick={() => read(selected.id)}>Ouvrir la fiche<ChevronRight size={14} /></button></div>}
            {view === 'relations' && selected && <section className="accessible-relations" aria-label="Liste des relations"><h2>Relations du voisinage</h2>{projection?.relations.map(link => <button key={link.id} aria-pressed={relation?.id === link.id} onClick={() => changeRoute({ relation: link.id })}><span>{model.nodeById.get(link.sourceId)?.name}<span aria-hidden="true"> → </span>{model.nodeById.get(link.targetId)?.name}</span><small>{link.qualification.meaning || link.label}</small></button>)}{!projection?.relations.length && <p>Aucune relation métier publiée avec ces critères.</p>}</section>}
            {relation && view === 'relations' && <RelationDetails model={model} relation={relation} onOpenSource={openSource} />}
          </>}
        </div>
        <footer className="workspace-footer">Urbanisation · {route.version ? 'Publication fixe' : 'Publication courante, actualisée automatiquement'} · Modèle en cours de construction</footer>
      </>}
    </main>
    {model && <SourceDialog model={model} source={source} onClose={closeSource} />}
  </div></ModelLinksProvider>;
}

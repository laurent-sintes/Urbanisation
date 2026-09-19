import { useEffect, useLayoutEffect, useMemo, useState, useCallback, useRef } from 'react';
import { ReactFlow, ReactFlowProvider, Background, Controls, useReactFlow, type Node, type NodeProps } from '@xyflow/react';
import { ArrowUpRight, FileText, LayoutGrid } from 'lucide-react';
import { NodeIcon } from './icons';
import { ReferenceLink } from './components/ModelLinks';
import { childrenOf, rootsOf, hasCapabilityCards } from './model';
import { kindLabel, shortText, statusLabel } from './presentation';
import type { AtlasNode, PublishedModel } from './types';
import '@xyflow/react/dist/style.css';

type ChildList = { kind: 'capability' | 'reference' | 'behavior'; items: AtlasNode[] };
type Card = Node<{ item: AtlasNode; count: number; childList?: ChildList; onHeight: (id: string, height: number) => void; onExplore: (id: string) => void; onRead: (id: string) => void; highlighted: boolean; muted: boolean }, 'business'>;
type Container = Node<{ item: AtlasNode }, 'container'>;
function BusinessCard({ data, selected }: NodeProps<Card>) {
  const presentation = data.item.kind === 'group' && data.item.groupRole !== 'urbanism_level';
  const card = useRef<HTMLElement>(null);
  const expanded = data.childList !== undefined;
  const listLabel = data.childList?.kind === 'reference' ? 'Référentiels' : data.childList?.kind === 'behavior' ? 'Comportements' : 'Capacités';
  useLayoutEffect(() => {
    if (!expanded || !card.current) return;
    // Measure unscaled content, including wrapped names, instead of clipping a growing list.
    const measure = () => { if (card.current) data.onHeight(data.item.id, card.current.offsetHeight); };
    measure();
    const observer = new ResizeObserver(measure);
    observer.observe(card.current);
    return () => observer.disconnect();
  }, [expanded, data.item.id, data.onHeight]);
  return <article ref={card} className={`business-card ${expanded ? 'has-child-list' : ''} ${selected ? 'is-selected' : ''} ${presentation ? 'is-presentation' : ''} ${data.highlighted ? 'is-highlighted' : ''} ${data.muted ? 'is-muted' : ''}`} data-node-id={data.item.id}>
    <div className="card-eyebrow"><NodeIcon node={data.item} size={22}/><span>{kindLabel(data.item)}</span><span className="card-id">{data.item.id}</span></div>
    <h3 title={data.item.name}>{data.item.name}</h3>
    <p>{shortText(data.item.purpose || data.item.definition || 'Description non renseignée dans cette publication.', 115)}</p>
    {data.childList && <div className="card-child-list nodrag nopan nowheel" onClick={event => event.stopPropagation()} onDoubleClick={event => event.stopPropagation()} onKeyDown={event => { if (['Enter', ' '].includes(event.key)) event.stopPropagation(); }}>
      <div className="child-list-heading">{listLabel} <span>{data.childList.items.length}</span></div>
      {data.childList.items.length ? <ul aria-label={`${listLabel} de ${data.item.name}`}>
        {data.childList.items.map(child => <li key={child.id}><ReferenceLink target={child.id} className={`card-child-link ${child.kind === 'reference' ? 'reference-link' : child.kind === 'behavior' ? 'behavior-link' : 'capacity-link'}`}><NodeIcon node={child} size={16}/><span>{child.name}</span><ArrowUpRight size={12} className="child-arrow"/></ReferenceLink></li>)}
      </ul> : <p>Aucune capacité publiée.</p>}
    </div>}
    <div className="card-bottom"><span className={`status-dot ${data.item.status}`} title={statusLabel(data.item)}/><span>{data.count ? `${data.count} éléments` : statusLabel(data.item)}</span><button className="nodrag nopan" aria-label={`${data.count ? 'Explorer' : 'Lire'} ${data.item.name}`} onClick={e => { e.stopPropagation(); (data.count ? data.onExplore : data.onRead)(data.item.id); }}>{data.count ? 'Explorer' : 'Fiche'}<ArrowUpRight size={13}/></button></div>
  </article>;
}
function GroupCard({ data }: NodeProps<Container>) {
  return <div className={`map-container ${data.item.kind === 'group' && data.item.groupRole !== 'urbanism_level' ? 'presentation-container' : ''}`}><div className="container-label"><NodeIcon node={data.item} size={20}/><strong>{data.item.name}</strong><span>{kindLabel(data.item)}</span></div></div>;
}
const nodeTypes = { business: BusinessCard, container: GroupCard };

export interface ReactFlowPaneProps {
  model: PublishedModel; selectedId: string; scopeId?: string;
  onSelect: (id: string) => void; onExplore: (id: string) => void; onRead: (id: string) => void;
  perspective: string;
}
function Canvas(props: ReactFlowPaneProps) {
  const { model, selectedId, scopeId, perspective } = props;
  const [layout, setLayout] = useState<{nodes: Node[]; ms: number; width: number; height: number}>({ nodes: [], ms: 0, width: 0, height: 0 });
  const [cardHeights, setCardHeights] = useState<Record<string, number>>({});
  const [canvasWidth, setCanvasWidth] = useState(0);
  const [touch, setTouch] = useState(() => matchMedia('(pointer: coarse)').matches);
  const [fullscreen, setFullscreen] = useState(() => Boolean(document.fullscreenElement));
  const [error, setError] = useState('');
  const [arrangement, setArrangement] = useState(0);
  const { fitView } = useReactFlow();
  const container = useRef<HTMLDivElement>(null);
  const capabilityOverview = hasCapabilityCards(model, scopeId);
  const nativeTouchScroll = capabilityOverview && touch && !fullscreen;
  useEffect(() => {
    const pointer = matchMedia('(pointer: coarse)');
    const updatePointer = () => setTouch(pointer.matches);
    const updateFullscreen = () => setFullscreen(Boolean(document.fullscreenElement));
    pointer.addEventListener('change', updatePointer);
    document.addEventListener('fullscreenchange', updateFullscreen);
    return () => { pointer.removeEventListener('change', updatePointer); document.removeEventListener('fullscreenchange', updateFullscreen); };
  }, []);
  const onHeight = useCallback((id: string, height: number) => {
    setCardHeights(previous => previous[id] === height ? previous : { ...previous, [id]: height });
  }, []);
  const graph = useMemo(() => {
    if (!scopeId) return { nodes: rootsOf(model), group: undefined };
    const scope = model.nodeById.get(scopeId);
    if (!scope) return { nodes: [], group: undefined };
    const children = childrenOf(model, scopeId);
    // Cards only express explicit structure. A leaf never expands into business neighbours here.
    return children.length ? { nodes: [scope, ...children], group: scope } : { nodes: [scope], group: undefined };
  }, [model, scopeId]);
  useEffect(() => {
    let current = true;
    const start = performance.now();
    setError('');
    const group = graph.group;
    const items = graph.nodes.filter(n => n.id !== group?.id);
    const childLists = new Map<string, ChildList>();
    if (capabilityOverview) for (const item of items) {
      const children = childrenOf(model, item.id);
      if (item.kind === 'domain' || item.kind === 'reference') {
        childLists.set(item.id, { kind: 'capability', items: children.filter(child => child.kind === 'capability') });
      } else if (item.kind === 'capability' && children.some(child => child.kind === 'behavior')) {
        childLists.set(item.id, { kind: 'behavior', items: children.filter(child => child.kind === 'behavior') });
      } else if (item.kind === 'group' && item.groupRole !== 'urbanism_level') {
        const references = children.filter(child => child.kind === 'reference');
        if (references.length) childLists.set(item.id, { kind: 'reference', items: references });
      }
    }
    const inputs = items.map(n => ({ id: n.id, width: 300, height: childLists.has(n.id) ? cardHeights[n.id] || 260 + childLists.get(n.id)!.items.length * 34 : 220 }));
    // A bounded grid keeps cards readable; it does not create model relationships.
    const columns = Math.min(items.length, capabilityOverview ? Math.max(1, Math.min(3, Math.floor((canvasWidth - 60 + 28) / 328))) : items.length > 4 ? 3 : 2) || 1;
    const rows = Math.ceil(items.length / columns);
    const rowHeights = Array.from({ length: rows }, (_, row) => Math.max(...inputs.slice(row * columns, (row + 1) * columns).map(item => item.height)));
    const placement = Promise.resolve({
      id: 'canvas', width: columns * 300 + (columns - 1) * 28 + 32,
      height: rowHeights.reduce((sum, height) => sum + height, 0) + Math.max(0, rows - 1) * 28 + 32,
      children: inputs.map((item, index) => ({ ...item, x: 16 + (index % columns) * 328, y: 16 + rowHeights.slice(0, Math.floor(index / columns)).reduce((sum, height) => sum + height + 28, 0) }))
    });
    placement.then(result => {
      if (!current) return;
      const nodes: Node[] = [];
      if (group) nodes.push({ id: `group:${group.id}`, type: 'container', data: { item: group }, position: { x: 0, y: 0 }, width: (result.width || 380) + 28, height: (result.height || 250) + 70, style: { width: (result.width || 380) + 28, height: (result.height || 250) + 70 }, selectable: false, draggable: false, focusable: false });
      for (const position of result.children || []) {
        const item = model.nodeById.get(position.id)!;
        // Explicit dimensions keep a controlled node measurable during selection updates.
        // CSS sizes alone briefly hide it between the two clicks of a double-click.
        nodes.push({ id: item.id, type: 'business', data: { item, childList: childLists.get(item.id) }, position: { x: (position.x || 0) + (group ? 14 : 0), y: (position.y || 0) + (group ? 54 : 0) }, ...(group ? { parentId: `group:${group.id}`, extent: 'parent' as const } : {}), width: 300, height: position.height, style: { width: 300, height: position.height }, draggable: false, ariaLabel: `${kindLabel(item)} ${item.name}` });
      }
      setLayout({ nodes, ms: Math.round(performance.now() - start), width: (result.width || 380) + (group ? 28 : 0), height: (result.height || 250) + (group ? 70 : 0) });
    }).catch(e => current && setError(String(e)));
    return () => { current = false; };
  }, [graph, model, scopeId, arrangement, capabilityOverview, cardHeights, capabilityOverview ? canvasWidth : 0]);
  useEffect(() => { const id = setTimeout(() => fitView({ padding: 0.06, maxZoom: 1, duration: matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 220 }), 80); return () => clearTimeout(id); }, [layout, fitView]);
  useEffect(() => {
    if (!container.current) return;
    const observer = new ResizeObserver(() => {
      setCanvasWidth(container.current!.clientWidth);
      void fitView({ padding: .06, maxZoom: 1, duration: 0 });
    });
    observer.observe(container.current);
    return () => observer.disconnect();
  }, [fitView, scopeId]);
  const nodes = useMemo(() => layout.nodes.map(n => n.type !== 'business' ? n : { ...n, selected: n.id === selectedId, data: { ...n.data, onHeight, count: childrenOf(model, n.id).length, onExplore: props.onExplore, onRead: props.onRead, highlighted: Boolean(perspective && model.nodeById.get(n.id)?.status === perspective), muted: Boolean(perspective && model.nodeById.get(n.id)?.status !== perspective) } }), [layout, selectedId, model, props.onExplore, props.onRead, perspective, onHeight]);
  const select = useCallback((_event: unknown, node: Node) => { if (node.type === 'business') props.onSelect(node.id); }, [props.onSelect]);
  const emptyScope = scopeId && model.nodeById.get(scopeId);
  if (emptyScope && ['group', 'domain', 'reference'].includes(emptyScope.kind) && !childrenOf(model, emptyScope.id).length) return <div className="graph-canvas empty-state"><NodeIcon node={emptyScope} size={38}/><h2>{emptyScope.name}</h2><p>Aucun élément publié dans ce périmètre.</p></div>;
  if (error) return <div className="empty-state" role="alert">Le placement a échoué : {error}</div>;
  // Let the page grow with capability lists, keeping text near its natural size.
  const canvasHeight = capabilityOverview && layout.width && canvasWidth ? Math.max(420, Math.ceil(layout.height * Math.min(1, canvasWidth / layout.width)) + 70) : undefined;
  return <div ref={container} className={`graph-canvas ${capabilityOverview ? 'capabilities-canvas' : ''} ${nativeTouchScroll ? 'touch-scroll' : ''}`} style={canvasHeight ? { height: canvasHeight } : undefined} data-testid="react-flow-canvas" data-layout-ms={layout.ms}>
    <ReactFlow nodes={nodes} edges={[]} nodeTypes={nodeTypes} nodesDraggable={false} nodesConnectable={false} edgesReconnectable={false} deleteKeyCode={null} onNodeClick={select} onNodeDoubleClick={(_e, node) => node.type === 'business' && (childrenOf(model, node.id).length ? props.onExplore : props.onRead)(node.id)} zoomOnDoubleClick={false} panOnDrag={!nativeTouchScroll} zoomOnPinch={!nativeTouchScroll} zoomOnScroll={!capabilityOverview} preventScrolling={!capabilityOverview} minZoom={0.2} maxZoom={1.6} fitView proOptions={{ hideAttribution: false }} ariaLabelConfig={{ 'controls.zoomIn.ariaLabel': 'Agrandir', 'controls.zoomOut.ariaLabel': 'Réduire', 'controls.fitView.ariaLabel': 'Centrer la carte' }}>
      <Background gap={24} size={1} color="#d8e3df"/>
      <Controls showInteractive={false}/>
    </ReactFlow>
    <button className="arrange-button" onClick={() => setArrangement(v => v + 1)}><LayoutGrid size={14}/>Réorganiser</button>
    {!graph.nodes.length && <div className="empty-state"><FileText/>Ce périmètre est réservé.</div>}
  </div>;
}
export function ReactFlowPane(props: ReactFlowPaneProps) { return <ReactFlowProvider><Canvas {...props}/></ReactFlowProvider>; }

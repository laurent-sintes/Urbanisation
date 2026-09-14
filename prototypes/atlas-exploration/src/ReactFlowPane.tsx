import { useEffect, useMemo, useState, useCallback } from 'react';
import { ReactFlow, ReactFlowProvider, Background, Controls, Handle, Position, MarkerType, useReactFlow, type Node, type NodeProps, type Edge } from '@xyflow/react';
import { ArrowUpRight, Layers, FileText, Network, LayoutGrid } from 'lucide-react';
import ELK from 'elkjs/lib/elk.bundled.js';
import type { ElkNode } from 'elkjs/lib/elk-api';
import { childrenOf, focusGraph, isStructural, neighborhood } from './model';
import { kindLabel, shortText, statusLabel } from './presentation';
import type { AtlasNode, PublishedModel, NeighborhoodOptions } from './types';
import '@xyflow/react/dist/style.css';

type Card = Node<{ item: AtlasNode; count: number; inRelations: boolean; onExplore: (id: string) => void; onRead: (id: string) => void; highlighted: boolean; muted: boolean }, 'business'>;
type Container = Node<{ item: AtlasNode }, 'container'>;
function BusinessCard({ data, selected }: NodeProps<Card>) {
  const presentation = data.item.kind === 'group' && data.item.groupRole !== 'urbanism_level';
  return <article className={`business-card ${selected ? 'is-selected' : ''} ${presentation ? 'is-presentation' : ''} ${data.highlighted ? 'is-highlighted' : ''} ${data.muted ? 'is-muted' : ''}`} data-node-id={data.item.id}>
    {data.inRelations && <Handle type="target" position={Position.Left}/>}
    <div className="card-eyebrow"><span>{kindLabel(data.item)}</span><span className="card-id">{data.item.id}</span></div>
    <h3>{data.item.name}</h3>
    <p>{shortText(data.item.purpose || data.item.definition || 'Description non renseignée dans cette publication.', 115)}</p>
    <div className="card-bottom"><span className={`status-dot ${data.item.status}`} title={statusLabel(data.item)}/><span>{data.count ? `${data.count} éléments` : statusLabel(data.item)}</span><button className="nodrag nopan" aria-label={`${data.count ? 'Explorer' : 'Lire'} ${data.item.name}`} onClick={e => { e.stopPropagation(); (data.count ? data.onExplore : data.onRead)(data.item.id); }}>{data.count ? 'Explorer' : 'Fiche'}<ArrowUpRight size={13}/></button></div>
    {data.inRelations && <Handle type="source" position={Position.Right}/>}
  </article>;
}
function GroupCard({ data }: NodeProps<Container>) {
  return <div className={`map-container ${data.item.groupRole === 'presentation' ? 'presentation-container' : ''}`}><div className="container-label"><Layers size={16}/><strong>{data.item.name}</strong><span>{kindLabel(data.item)}</span></div></div>;
}
const nodeTypes = { business: BusinessCard, container: GroupCard };
const elk = new ELK();
export interface ReactFlowPaneProps {
  model: PublishedModel; selectedId: string; scopeId?: string; mode: 'map' | 'relations';
  onSelect: (id: string) => void; onExplore: (id: string) => void; onRead: (id: string) => void;
  onSelectRelation: (id: string) => void; relationId?: string; depth: 1 | 2;
  direction: NeighborhoodOptions['direction']; perspective: string;
}
function Canvas(props: ReactFlowPaneProps) {
  const { model, selectedId, scopeId, mode, depth, direction, perspective } = props;
  const [layout, setLayout] = useState<{nodes: Node[]; edges: Edge[]; ms: number}>({ nodes: [], edges: [], ms: 0 });
  const [error, setError] = useState('');
  const [arrangement, setArrangement] = useState(0);
  const { fitView } = useReactFlow();
  const graph = useMemo(() => mode === 'relations' ? neighborhood(model, selectedId, { depth, direction }) : focusGraph(model, scopeId), [model, mode, mode === 'relations' ? selectedId : scopeId, depth, direction]);
  useEffect(() => {
    let current = true;
    const start = performance.now();
    setError('');
    const group = graph.mode === 'hierarchy' && scopeId ? model.nodeById.get(scopeId) : undefined;
    const items = graph.nodes.filter(n => n.id !== group?.id);
    const edges = graph.relations.filter(r => !isStructural(r));
    const inputs = items.map(n => ({ id: n.id, width: 290, height: 194 }));
    // A bounded grid keeps cards readable; it does not create model relationships.
    const columns = Math.min(items.length, items.length > 4 ? 3 : 2) || 1;
    const rows = Math.ceil(items.length / columns);
    const placement: Promise<ElkNode> = graph.mode === 'hierarchy' ? Promise.resolve({
      id: 'canvas', width: columns * 290 + (columns - 1) * 28 + 32,
      height: rows * 194 + Math.max(0, rows - 1) * 28 + 32,
      children: inputs.map((item, index) => ({ ...item, x: 16 + (index % columns) * 318, y: 16 + Math.floor(index / columns) * 222 }))
    }) : elk.layout<ElkNode>({ id: 'canvas', layoutOptions: {
      'elk.algorithm': 'layered', 'elk.direction': 'RIGHT', 'elk.spacing.nodeNode': '32',
      'elk.layered.spacing.nodeNodeBetweenLayers': '100', 'elk.aspectRatio': '1.8',
      'elk.padding': '[top=16,left=16,bottom=16,right=16]',
    }, children: inputs, edges: edges.map(r => ({ id: r.id, sources: [r.sourceId], targets: [r.targetId] })) });
    placement.then(result => {
      if (!current) return;
      const nodes: Node[] = [];
      if (group) nodes.push({ id: `group:${group.id}`, type: 'container', data: { item: group }, position: { x: 0, y: 0 }, style: { width: (result.width || 380) + 28, height: (result.height || 250) + 70 }, selectable: false, draggable: false, focusable: false });
      for (const position of result.children || []) {
        const item = model.nodeById.get(position.id)!;
        nodes.push({ id: item.id, type: 'business', data: { item }, position: { x: (position.x || 0) + (group ? 14 : 0), y: (position.y || 0) + (group ? 54 : 0) }, ...(group ? { parentId: `group:${group.id}`, extent: 'parent' as const } : {}), style: { width: 290, height: 194 }, draggable: false, ariaLabel: `${kindLabel(item)} ${item.name}` });
      }
      const renderedEdges: Edge[] = edges.map(r => ({ id: r.id, source: r.sourceId, target: r.targetId, type: 'smoothstep', label: r.type === 'relates-to' ? 'Relation métier' : r.label, data: { relationId: r.id }, markerEnd: { type: MarkerType.ArrowClosed, color: '#337b79', width: 18, height: 18 }, style: { stroke: '#337b79', strokeWidth: 2 }, labelStyle: { fontSize: 11, fill: '#274b50' }, labelBgStyle: { fill: '#f6faf9', fillOpacity: 1 }, labelBgPadding: [8, 6], ariaLabel: r.qualification.meaning || r.label }));
      setLayout({ nodes, edges: renderedEdges, ms: Math.round(performance.now() - start) });
    }).catch(e => current && setError(String(e)));
    return () => { current = false; };
  }, [graph, model, scopeId, arrangement]);
  useEffect(() => { const id = setTimeout(() => fitView({ padding: 0.06, maxZoom: 1, duration: matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 220 }), 80); return () => clearTimeout(id); }, [layout, fitView]);
  const nodes = useMemo(() => layout.nodes.map(n => n.type !== 'business' ? n : { ...n, selected: n.id === selectedId, data: { ...n.data, count: childrenOf(model, n.id).length, inRelations: graph.mode === 'neighborhood', onExplore: props.onExplore, onRead: props.onRead, highlighted: Boolean(perspective && model.nodeById.get(n.id)?.status === perspective), muted: Boolean(perspective && model.nodeById.get(n.id)?.status !== perspective) } }), [layout, selectedId, model, graph.mode, props.onExplore, props.onRead, perspective]);
  const edges = useMemo(() => layout.edges.map(e => ({ ...e, selected: props.relationId === e.id, style: { ...e.style, strokeWidth: props.relationId === e.id ? 3 : 2 } })), [layout, props.relationId]);
  const select = useCallback((_event: unknown, node: Node) => { if (node.type === 'business') props.onSelect(node.id); }, [props.onSelect]);
  if (error) return <div className="empty-state" role="alert">Le placement a échoué : {error}</div>;
  return <div className="graph-canvas" data-testid="react-flow-canvas" data-layout-ms={layout.ms}>
    <ReactFlow nodes={nodes} edges={edges} nodeTypes={nodeTypes} nodesDraggable={false} nodesConnectable={false} edgesReconnectable={false} deleteKeyCode={null} onNodeClick={select} onEdgeClick={(_e, edge) => props.onSelectRelation(edge.id)} onNodeDoubleClick={(_e, node) => node.type === 'business' && props.onExplore(node.id)} minZoom={0.2} maxZoom={1.6} fitView proOptions={{ hideAttribution: false }} ariaLabelConfig={{ 'controls.zoomIn.ariaLabel': 'Agrandir', 'controls.zoomOut.ariaLabel': 'Réduire', 'controls.fitView.ariaLabel': 'Centrer la carte' }}>
      <Background gap={24} size={1} color="#d8e3df"/>
      <Controls showInteractive={false}/>
    </ReactFlow>
    <button className="arrange-button" onClick={() => setArrangement(v => v + 1)}><LayoutGrid size={14}/>Réorganiser</button>
    {graph.mode === 'neighborhood' && !graph.relations.length && <div className="graph-note"><Network size={16}/><span>Aucune relation métier publiée dans ce périmètre.</span></div>}
    {!graph.nodes.length && <div className="empty-state"><FileText/>Ce périmètre est réservé.</div>}
  </div>;
}
export function ReactFlowPane(props: ReactFlowPaneProps) { return <ReactFlowProvider><Canvas {...props}/></ReactFlowProvider>; }

import { useEffect, useMemo, useState } from 'react';
import { useDiagram } from 'likec4/react';
import {
  ReactLikeC4,
  isLikeC4ViewId,
  likec4model,
  type ReactLikeC4Props,
} from '../.generated/likec4.generated.js';
import manifestJson from '../.generated/likec4-manifest.json';
import type { PublishedModel } from './types';

interface ProjectionManifest {
  publication: string;
  modelSha256: string;
  atlasToLikeC4: Record<string, string>;
  likeC4ToAtlas: Record<string, string>;
  mapViewByAtlasId: Record<string, string>;
  relationViewByAtlasId: Record<string, string>;
  atlasIdByView: Record<string, string>;
  viewNodes: Record<string, string[]>;
}
const manifest: ProjectionManifest = manifestJson;

export interface LikeC4PaneProps {
  model: PublishedModel;
  selectedId: string;
  scopeId?: string;
  mode: 'map' | 'relations';
  onSelect: (id: string) => void;
  onExplore: (id: string) => void;
  onSelectRelation?: (relationId: string) => void;
}

/** Uses the public diagram API; no DOM mutation or model writeback. */
function SynchronizedSelection({ selectedId, viewId }: { selectedId: string; viewId: string }) {
  const diagram = useDiagram();
  useEffect(() => {
    const frame = requestAnimationFrame(() => {
      diagram.unhighlightAll();
      const node = diagram.currentView.nodes.find(candidate => manifest.likeC4ToAtlas[candidate.id] === selectedId);
      if (node) diagram.highlightNode(node.id);
    });
    return () => cancelAnimationFrame(frame);
  }, [diagram, selectedId, viewId]);
  return null;
}

export function LikeC4Pane({ model, selectedId, scopeId, mode, onSelect, onExplore, onSelectRelation }: LikeC4PaneProps) {
  const focusId = mode === 'relations' ? selectedId : scopeId ?? selectedId;
  const requestedView = (mode === 'relations' ? manifest.relationViewByAtlasId : manifest.mapViewByAtlasId)[focusId];
  const viewId = isLikeC4ViewId(requestedView) ? requestedView : 'index';
  const [edgeSelection, setEdgeSelection] = useState<{ ids: string[]; summary: boolean } | null>(null);
  useEffect(() => setEdgeSelection(null), [viewId]);
  const relationshipIds = useMemo(() => new Map(Array.from(likec4model.relationships(), relation => [relation.id, relation.getMetadata('atlasRelationId')] as const)), []);
  const summarizedEdgeCount = useMemo(() => likec4model.view(viewId).$view.edges.filter(edge => edge.relations.length > 1 || edge.relations.some(relationId => {
    const publishedId = relationshipIds.get(relationId);
    const relation = typeof publishedId === 'string' ? model.relationById.get(publishedId) : undefined;
    return relation && (relation.sourceId !== manifest.likeC4ToAtlas[edge.source] || relation.targetId !== manifest.likeC4ToAtlas[edge.target]);
  })).length, [viewId, model, relationshipIds]);
  const selected = model.nodeById.get(selectedId);
  const visibleIds = manifest.viewNodes[viewId] ?? [];
  const directlyConnected = model.relations.filter(relation => !['contains', 'presents'].includes(relation.type) && (relation.sourceId === selectedId || relation.targetId === selectedId));
  const canExploreSelected = model.relations.some(relation => ['contains', 'presents'].includes(relation.type) && relation.sourceId === selectedId);

  if (model.version !== manifest.publication) {
    return <div className="graph-empty" role="status">
      <strong>Cette vue LikeC4 correspond à une autre publication.</strong>
      <p>Vue générée : {manifest.publication}. Publication consultée : {model.version}.</p>
      <p>Relancer la génération du prototype pour comparer les mêmes données.</p>
    </div>;
  }

  const handleNodeClick: NonNullable<ReactLikeC4Props['onNodeClick']> = node => {
    const atlasId = manifest.likeC4ToAtlas[node.id];
    if (atlasId && model.nodeById.has(atlasId)) onSelect(atlasId);
  };
  const handleEdgeClick: NonNullable<ReactLikeC4Props['onEdgeClick']> = edge => {
    const ids = edge.relations.flatMap(relationId => {
      const publishedId = relationshipIds.get(relationId);
      return typeof publishedId === 'string' && model.relationById.has(publishedId) ? [publishedId] : [];
    });
    const uniqueIds = [...new Set(ids)];
    const source = manifest.likeC4ToAtlas[edge.source];
    const target = manifest.likeC4ToAtlas[edge.target];
    const summary = uniqueIds.length > 1 || uniqueIds.some(id => {
      const relation = model.relationById.get(id)!;
      return relation.sourceId !== source || relation.targetId !== target;
    });
    setEdgeSelection({ ids: uniqueIds, summary });
    if (uniqueIds.length === 1) onSelectRelation?.(uniqueIds[0]!);
  };

  return <section className="likec4-pane" aria-label="Carte LikeC4 du modèle publié" style={{ display: 'flex', flexDirection: 'column', minWidth: 0 }}>
    <div className="graph-toolbar" style={{ display: 'flex', justifyContent: 'space-between', gap: 16, alignItems: 'center', padding: '10px 16px', flexWrap: 'wrap' }}>
      <span>{mode === 'relations' ? 'Voisinage direct' : 'Niveau exploré'} · {model.nodeById.get(focusId)?.name ?? 'Urbanisation'}</span>
      {mode === 'map' && canExploreSelected && selectedId !== focusId && <button type="button" onClick={() => onExplore(selectedId)}>Explorer {selected?.name}</button>}
      {mode === 'relations' && directlyConnected.length === 0 && <span>Aucune relation métier directe publiée.</span>}
    </div>
    {summarizedEdgeCount > 0 && <p className="graph-summary-notice" style={{ margin: 0, padding: '8px 16px', background: '#fff8e6', color: '#78570a', fontSize: 13 }}>{summarizedEdgeCount} liaison{summarizedEdgeCount > 1 ? 's' : ''} résumée{summarizedEdgeCount > 1 ? 's' : ''} entre branches : les flèches regroupent des relations de leurs éléments. Cliquer pour lire les relations sources.</p>}
    <div className="likec4-diagram" style={{ position: 'relative', minWidth: 0 }}>
      <ReactLikeC4
        viewId={viewId}
        colorScheme="light"
        injectFontCss={false}
        style={{ position: 'absolute', inset: 0 }}
        pannable
        zoomable
        fitView
        controls
        background="dots"
        showNavigationButtons={false}
        enableSearch={false}
        enableElementDetails={false}
        enableRelationshipDetails={false}
        enableRelationshipBrowser={false}
        enableDynamicViewWalkthrough={false}
        enableFocusMode={false}
        reduceGraphics
        reactFlowProps={{ nodesDraggable: false, nodesFocusable: true, edgesFocusable: true, zoomOnDoubleClick: false }}
        onNodeClick={handleNodeClick}
        onEdgeClick={handleEdgeClick}
        onNavigateTo={to => {
          const atlasId = manifest.atlasIdByView[to];
          if (atlasId && model.nodeById.has(atlasId)) onExplore(atlasId);
        }}
      >
        <SynchronizedSelection selectedId={selectedId} viewId={viewId} />
      </ReactLikeC4>
    </div>
    {edgeSelection && <div role="status" className="graph-edge-inspection" style={{ padding: '10px 16px', borderTop: '1px solid #d9e2ec' }}>
      <strong>{edgeSelection.summary ? 'Résumé visuel entre branches' : 'Relation publiée'} · {edgeSelection.ids.length} relation{edgeSelection.ids.length > 1 ? 's' : ''}</strong>
      {edgeSelection.summary && <p>Cette flèche représente les relations des éléments contenus, sans ajouter de relation entre leurs groupes.</p>}
      {edgeSelection.ids.map(id => <button key={id} type="button" onClick={() => onSelectRelation?.(id)} style={{ display: 'block', marginTop: 6 }}>{model.relationById.get(id)?.label || id}</button>)}
    </div>}
    <details className="graph-accessible-list" style={{ padding: '10px 16px', borderTop: '1px solid #d9e2ec' }}>
      <summary>Éléments de cette vue · accès clavier ({visibleIds.length})</summary>
      <ul>{visibleIds.map(id => <li key={id}><button type="button" onClick={() => onSelect(id)}>{model.nodeById.get(id)?.name ?? id}</button>{model.relations.some(relation => ['contains', 'presents'].includes(relation.type) && relation.sourceId === id) && <button type="button" onClick={() => onExplore(id)} aria-label={`Explorer ${model.nodeById.get(id)?.name ?? id}`}>Explorer</button>}</li>)}</ul>
    </details>
  </section>;
}

export default LikeC4Pane;

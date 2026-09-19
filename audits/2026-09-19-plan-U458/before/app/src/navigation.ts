export type View = 'map' | 'sheet' | 'relations' | 'glossary' | 'principles';
export interface GraphRoute {
  graphLevel?: 'capability' | 'domain' | 'universe';
  graphDepth?: 0 | 1 | 2 | 3;
  graphDirection?: 'both' | 'incoming' | 'outgoing';
  graphFamily?: 'all' | 'needs' | 'other';
  graphLayout?: 'organic' | 'hierarchical';
  graphLabels?: 'focus' | 'all';
}
export interface RouteState extends GraphRoute {
  node: string; scope: string; view?: View; version: string;
  query: string; type: string; status: string; relation: string;
  source: string; anchor: string; sourceId: string;
  term?: string; section?: string;
  glossary?: 'model' | 'meta';
  principle?: string;
}
export function readRoute(hash: string): RouteState {
  const p = new URLSearchParams(hash.replace(/^#/, ''));
  const legacyRoots = ['atlas', 'transactional', 'process', 'references', 'panorama', 'backlog'];
  const node = p.get('node') || '';
  const view = p.get('view');
  const graph: GraphRoute = {};
  if (['capability', 'domain', 'universe'].includes(p.get('level') || '')) graph.graphLevel = p.get('level') as GraphRoute['graphLevel'];
  if (p.has('depth') && ['0', '1', '2', '3'].includes(p.get('depth')!)) graph.graphDepth = Number(p.get('depth')) as GraphRoute['graphDepth'];
  if (['both', 'incoming', 'outgoing'].includes(p.get('direction') || '')) graph.graphDirection = p.get('direction') as GraphRoute['graphDirection'];
  if (['all', 'needs', 'other'].includes(p.get('qualification') || '')) graph.graphFamily = p.get('qualification') as GraphRoute['graphFamily'];
  if (['organic', 'hierarchical'].includes(p.get('layout') || '')) graph.graphLayout = p.get('layout') as GraphRoute['graphLayout'];
  if (['focus', 'all'].includes(p.get('labels') || '')) graph.graphLabels = p.get('labels') as GraphRoute['graphLabels'];
  return {
    ...((view === 'relations' || view === 'links') ? graph : {}),
    node: view === 'principles' || legacyRoots.includes(node) ? '' : node,
    scope: view === 'principles' ? '' : p.get('scope') || '',
    view: view === 'links' ? 'relations' : ['map', 'sheet', 'relations', 'glossary', 'principles'].includes(view || '') ? view as View : undefined,
    ...(view === 'principles' && p.has('principle') ? { principle: p.get('principle') || '' } : {}),
    ...(p.has('term') ? { term: p.get('term') || '' } : {}),
    ...(p.get('glossary') === 'meta' ? { glossary: 'meta' as const } : {}),
    ...(p.has('section') ? { section: p.get('section') || '' } : {}),
    version: p.get('version') || '', query: p.get('q') || '', type: p.get('type') || '',
    status: p.get('status') || '', relation: p.get('relation') || '',
    source: p.get('source') || '', anchor: p.get('anchor') || '', sourceId: p.get('sourceId') || '',
  };
}
export function routeHash(route: RouteState): string {
  const p = new URLSearchParams();
  for (const [key, value] of Object.entries({
    version: route.version, node: route.node, scope: route.scope, view: route.view,
    q: route.query, type: route.type, status: route.status, relation: route.relation,
    source: route.source, anchor: route.anchor, sourceId: route.sourceId,
    term: route.term, section: route.section,
    glossary: route.view === 'glossary' ? route.glossary : undefined,
    principle: route.view === 'principles' ? route.principle : undefined,
    ...(route.view === 'relations' ? { level: route.graphLevel, depth: route.graphDepth, direction: route.graphDirection, qualification: route.graphFamily, layout: route.graphLayout, labels: route.graphLabels } : {}),
  })) if (value !== undefined && value !== '') p.set(key, String(value));
  return p.size ? `#${p}` : '/';
}
export function preference<T>(key: string, fallback: T): T {
  try { const value = localStorage.getItem(`flow-atlas:${key}`); return value ? JSON.parse(value) as T : fallback; }
  catch { return fallback; }
}
export function savePreference(key: string, value: unknown) {
  try { localStorage.setItem(`flow-atlas:${key}`, JSON.stringify(value)); } catch { /* Navigation works without storage. */ }
}

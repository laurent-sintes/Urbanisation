export type View = 'map' | 'sheet' | 'relations' | 'glossary';
export interface RouteState {
  node: string; scope: string; view?: View; version: string;
  query: string; type: string; status: string; relation: string;
  source: string; anchor: string; sourceId: string;
  term?: string; section?: string;
}
export function readRoute(hash: string): RouteState {
  const p = new URLSearchParams(hash.replace(/^#/, ''));
  const legacyRoots = ['atlas', 'transactional', 'process', 'references', 'panorama', 'backlog'];
  const node = p.get('node') || '';
  const view = p.get('view');
  return {
    node: legacyRoots.includes(node) ? '' : node,
    scope: p.get('scope') || '',
    view: view === 'links' ? 'relations' : ['map', 'sheet', 'relations', 'glossary'].includes(view || '') ? view as View : undefined,
    ...(p.has('term') ? { term: p.get('term') || '' } : {}),
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
  })) if (value) p.set(key, value);
  return p.size ? `#${p}` : '/';
}
export function preference<T>(key: string, fallback: T): T {
  try { const value = localStorage.getItem(`flow-atlas:${key}`); return value ? JSON.parse(value) as T : fallback; }
  catch { return fallback; }
}
export function savePreference(key: string, value: unknown) {
  try { localStorage.setItem(`flow-atlas:${key}`, JSON.stringify(value)); } catch { /* Navigation works without storage. */ }
}

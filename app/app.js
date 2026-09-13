import { createModel, lifecycleLabels } from './model.js';

const root = document.getElementById('flow-atlas');
const content = document.getElementById('fa-content');
const search = document.getElementById('fa-search');
const notice = document.getElementById('fa-notice');
const sourceDialog = document.getElementById('fa-source-dialog');
const sourceBody = document.getElementById('fa-source-body');
const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const normalize = value => String(value ?? '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
const iconPaths = {
  search: '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 4 4"/>',
  layers: '<path d="m3 7 9-4 9 4-9 4-9-4Zm0 5 9 4 9-4M3 17l9 4 9-4"/>',
  route: '<circle cx="5" cy="6" r="2"/><circle cx="19" cy="18" r="2"/><path d="M7 6h9a4 4 0 0 1 0 8H8a4 4 0 0 0 0 8"/>',
  compass: '<circle cx="12" cy="12" r="9"/><path d="m16 8-3 5-5 3 3-5 5-3Z"/>',
  waypoints: '<circle cx="5" cy="16" r="2"/><circle cx="12" cy="5" r="2"/><circle cx="19" cy="14" r="2"/><path d="m6 14 5-7m3 0 4 5m-11 4 10-2"/>',
  'arrow-left': '<path d="M20 12H4m6-6-6 6 6 6"/>',
  'arrow-right': '<path d="M4 12h16m-6-6 6 6-6 6"/>',
  'arrow-up-right': '<path d="M6 18 18 6M7 6h11v11"/>',
  'layout-grid': '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
  box: '<path d="m12 3 9 5v9l-9 5-9-5V8l9-5Zm-9 5 9 5 9-5m-9 5v9m-4-17 9 5"/>',
  'file-text': '<path d="M14 3H5v18h14V8l-5-5v5h5M8 12h8m-8 4h8"/>',
  zap: '<path d="m13 2-9 12h7l-1 8 10-12h-7l1-8Z"/>',
  database: '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 4 18 4 18 0V5M3 12c0 4 18 4 18 0"/>',
  library: '<path d="M3 3h4v18H3zM10 3h4v18h-4zM17 4l4-1 3 17-4 1-3-17Z"/>',
  component: '<path d="m12 2 4 4-4 4-4-4 4-4ZM6 8l4 4-4 4-4-4 4-4Zm12 0 4 4-4 4-4-4 4-4Zm-6 6 4 4-4 4-4-4 4-4Z"/>'
};
let data, model, nodes, labels, icons, steps;
let refreshPending = false;
let sourceRequest = 0;
let currentSource = null;
let seenRevision = '';
let maxIndex = history.state?.atlasIndex || 0;
let navigationIndex = maxIndex;
let routeNotice = '';
try { if (history.state?.atlasIndex !== undefined) maxIndex = Math.max(maxIndex, Number(sessionStorage.getItem('flow-atlas:max-index')) || 0); } catch { /* Session history still works without storage. */ }
function requestedSpace() { return 'release'; }
const state = { space: requestedSpace(), id: 'transactional', view: 'map', query: '', type: 'all', statusFilter: 'all', journey: -1, sourcePath: '', sourceAnchor: '' };
state.publication = new URLSearchParams(location.hash.slice(1)).get('version') || '';
const tree = document.getElementById('fa-tree');
const main = document.getElementById('fa-main');
const rail = document.getElementById('fa-rail');
const narrowScreen = matchMedia('(max-width: 1000px)');
const expanded = new Set(['transactional']);
let treeFocus = 'transactional', treeOpen = false, sourceTrigger = null;
try {
  const saved = JSON.parse(localStorage.getItem('flow-atlas:expanded') || 'null');
  if (Array.isArray(saved)) { expanded.clear(); saved.filter(id => typeof id === 'string').forEach(id => expanded.add(id)); }
} catch { /* Navigation also works without local storage. */ }
function saveExpansion() {
  try { localStorage.setItem('flow-atlas:expanded', JSON.stringify([...expanded])); } catch { /* Optional preference. */ }
}
function nodeKind(node) { return node.kind === 'group' && node.groupRole === 'urbanism_level' ? 'Niveau d’urbanisme' : labels[node.kind]; }
function revealSelection() {
  const selected = nodes.get(state.id);
  lineage(selected).slice(0, -1).forEach(node => expanded.add(node.id));
  treeFocus = selected.id;
  saveExpansion();
}
function renderTree() {
  const focused = tree.contains(document.activeElement);
  const scroll = document.getElementById('fa-tree-scroll');
  const top = scroll.scrollTop;
  const branch = (id, depth) => {
    const node = nodes.get(id), open = expanded.has(id), hasChildren = node.children.length > 0;
    return `<div role="treeitem" data-tree-id="${esc(id)}" tabindex="${id === treeFocus ? 0 : -1}" aria-labelledby="tree-label-${esc(id)}" aria-selected="${id === state.id}" aria-level="${depth}"${hasChildren ? ` aria-expanded="${open}"` : ''}><div class="fa-tree-row" data-tree-select="${esc(id)}">${hasChildren ? `<button class="fa-tree-toggle" data-tree-toggle="${esc(id)}" tabindex="-1" aria-label="${open ? 'Replier' : 'Déplier'} ${esc(node.name)}"><span aria-hidden="true">${open ? '⌄' : '›'}</span></button>` : '<span class="fa-tree-spacer" aria-hidden="true"></span>'}<span class="fa-tree-label" id="tree-label-${esc(id)}">${esc(node.name)}${node.kind === 'group' ? `<small>${esc(nodeKind(node))}</small>` : ''}</span>${hasChildren ? `<span class="fa-tree-count" aria-hidden="true">${node.children.length}</span>` : ''}</div>${hasChildren ? `<div role="group"${open ? '' : ' hidden'}>${node.children.map(child => branch(child, depth + 1)).join('')}</div>` : ''}</div>`;
  };
  const roots = ['transactional', ...(nodes.get('process')?.children.length ? ['process'] : [])];
  tree.innerHTML = roots.map(id => branch(id, 1)).join('');
  const target = [...tree.querySelectorAll('[role="treeitem"]')].find(el => el.dataset.treeId === treeFocus && !el.closest('[hidden]'));
  if (!target) { treeFocus = 'transactional'; tree.querySelector('[role="treeitem"]').tabIndex = 0; }
  scroll.scrollTop = top;
  if (focused) focusTree(treeFocus);
}
function focusTree(id) {
  const item = [...tree.querySelectorAll('[role="treeitem"]')].find(el => el.dataset.treeId === id && !el.closest('[hidden]'));
  if (!item) return;
  tree.querySelectorAll('[role="treeitem"]').forEach(el => { el.tabIndex = -1; });
  treeFocus = id; item.tabIndex = 0; item.focus({ preventScroll: true }); item.scrollIntoView({ block: 'nearest' });
}
function toggleBranch(id) {
  if (!nodes.get(id)?.children.length) return;
  if (expanded.has(id)) expanded.delete(id); else expanded.add(id);
  treeFocus = id; saveExpansion(); renderTree(); focusTree(id);
}
function setTreeOpen(open, returnFocus = true) {
  treeOpen = open && narrowScreen.matches;
  root.classList.toggle('fa-tree-is-open', treeOpen);
  document.getElementById('fa-tree-open').setAttribute('aria-expanded', String(treeOpen));
  document.getElementById('fa-tree-backdrop').hidden = !treeOpen;
  main.inert = treeOpen; root.querySelector('.fa-top').inert = treeOpen;
  rail.inert = narrowScreen.matches && !treeOpen;
  if (treeOpen) { rail.setAttribute('role', 'dialog'); rail.setAttribute('aria-modal', 'true'); focusTree(treeFocus); }
  else { rail.removeAttribute('role'); rail.removeAttribute('aria-modal'); if (returnFocus && narrowScreen.matches) document.getElementById('fa-tree-open').focus(); }
}
function focusContent() { (content.querySelector('h1') || content).focus({ preventScroll: true }); }

tree.addEventListener('click', event => {
  const toggle = event.target.closest('[data-tree-toggle]');
  if (toggle) { event.stopPropagation(); toggleBranch(toggle.dataset.treeToggle); return; }
  const row = event.target.closest('[data-tree-select]');
  if (row) { focusTree(row.dataset.treeSelect); move(row.dataset.treeSelect); }
});
tree.addEventListener('focusin', event => {
  if (event.target.matches('[role="treeitem"]')) treeFocus = event.target.dataset.treeId;
});
let typedPrefix = '', typedAt = 0;
tree.addEventListener('keydown', event => {
  const item = event.target.closest('[role="treeitem"]');
  if (!item) return;
  const id = item.dataset.treeId, node = nodes.get(id);
  const visible = [...tree.querySelectorAll('[role="treeitem"]')].filter(el => !el.closest('[hidden]'));
  const index = visible.indexOf(item);
  let next;
  if (event.key === 'ArrowDown') next = visible[Math.min(index + 1, visible.length - 1)];
  else if (event.key === 'ArrowUp') next = visible[Math.max(index - 1, 0)];
  else if (event.key === 'Home') next = visible[0];
  else if (event.key === 'End') next = visible.at(-1);
  else if (event.key === 'ArrowRight') {
    if (node.children.length && !expanded.has(id)) toggleBranch(id);
    else if (node.children.length) next = visible[index + 1];
  } else if (event.key === 'ArrowLeft') {
    if (node.children.length && expanded.has(id)) toggleBranch(id);
    else next = visible.find(el => el.dataset.treeId === node.parentId);
  } else if (event.key === 'Enter' || event.key === ' ') move(id);
  else if (event.key.length === 1 && !event.ctrlKey && !event.metaKey && !event.altKey) {
    const now = Date.now(); typedPrefix = now - typedAt > 700 ? event.key : typedPrefix + event.key; typedAt = now;
    next = [...visible.slice(index + 1), ...visible.slice(0, index + 1)].find(el => normalize(nodes.get(el.dataset.treeId).name).startsWith(normalize(typedPrefix)));
  } else return;
  event.preventDefault(); if (next) focusTree(next.dataset.treeId);
});
content.addEventListener('keydown', event => {
  const result = event.target.closest('.fa-result');
  if (!result || !['ArrowDown', 'ArrowUp', 'Home', 'End'].includes(event.key)) return;
  const results = [...content.querySelectorAll('.fa-result')], index = results.indexOf(result);
  const next = event.key === 'Home' ? 0 : event.key === 'End' ? results.length - 1 : index + (event.key === 'ArrowDown' ? 1 : -1);
  event.preventDefault(); if (next < 0) search.focus(); else results[Math.min(next, results.length - 1)].focus();
});
document.addEventListener('keydown', event => {
  if (!treeOpen) return;
  if (event.key === 'Escape') { event.preventDefault(); event.stopImmediatePropagation(); setTreeOpen(false); }
  if (event.key === 'Tab') {
    const targets = [...rail.querySelectorAll('button:not([tabindex="-1"]),select,[tabindex="0"]')].filter(el => el.getClientRects().length && !el.closest('[hidden]') && !el.disabled);
    const first = targets[0], last = targets.at(-1);
    if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
    else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
  }
}, true);
narrowScreen.addEventListener('change', () => setTreeOpen(false, false));
setTreeOpen(false, false);
const resizer = document.getElementById('fa-rail-resize');
function setRailWidth(value) {
  const width = Math.max(240, Math.min(420, Number(value) || 300));
  root.style.setProperty('--fa-tree-width', `${width}px`);
  resizer.setAttribute('aria-valuenow', String(width));
  try { localStorage.setItem('flow-atlas:tree-width', String(width)); } catch { /* Optional preference. */ }
}
try { setRailWidth(localStorage.getItem('flow-atlas:tree-width') || 300); } catch { setRailWidth(300); }
resizer.addEventListener('keydown', event => {
  if (['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) {
    event.preventDefault(); setRailWidth(event.key === 'Home' ? 240 : event.key === 'End' ? 420 : Number(resizer.getAttribute('aria-valuenow')) + (event.key === 'ArrowLeft' ? -20 : 20));
  }
});
resizer.addEventListener('pointerdown', event => { if (event.button !== 0) return; event.preventDefault(); resizer.setPointerCapture(event.pointerId); });
resizer.addEventListener('pointermove', event => { if (resizer.hasPointerCapture(event.pointerId)) setRailWidth(event.clientX - root.getBoundingClientRect().left); });
resizer.addEventListener('pointerup', event => { if (resizer.hasPointerCapture(event.pointerId)) resizer.releasePointerCapture(event.pointerId); });

function icon(name) {
  const key = icons?.[name] || name;
  return `<svg class="lucide" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${iconPaths[key] || iconPaths['layout-grid']}</svg>`;
}
root.querySelectorAll('[data-lucide]').forEach(el => { el.outerHTML = icon(el.dataset.lucide); });
function kind(node) { return `<span class="fa-kind" data-kind="${node.kind}">${icon(node.kind)}${esc(nodeKind(node) || node.kind)}</span>`; }
function lineage(node) { return model.lineage(node); }
function related(id) { return model.related(id); }
function statusInfo(node) {
  if (lifecycleLabels[node.lifecycle?.state]) return lifecycleLabels[node.lifecycle.state];
  if (node.status === 'navigation') return ['Navigation', 'neutral'];
  if (node.status === 'not_assessed') return ['Non traité', 'amber'];
  if (node.status === 'documented') return ['Partiellement documenté', 'amber'];
  if (node.status === 'declared') return ['Déclaré', 'neutral'];
  if (node.status === 'observed') return ['Observé', 'green'];
  if (node.parentRelation?.review?.state === 'under_review') return [node.status === 'partial' ? 'Validation partielle · en réexamen' : state.space === 'release' ? 'Non validé · en réexamen' : 'Rattachement en réexamen', 'amber'];
  if (node.status === 'partial') return ['Validation partielle', 'amber'];
  if (node.status === 'validated') return [node.kind === 'capability' ? 'Capacité validée' : 'Élément adopté', 'green'];
  if (node.status === 'illustration') return ['Exemple proposé', 'purple'];
  if (node.status === 'review') return [state.space === 'release' && node.kind === 'capability' ? 'Non validé · en réexamen' : 'En réexamen', 'amber'];
  return [state.space === 'release' ? 'Non validé' : 'Proposé', 'neutral'];
}
function badge(node) { const [text, tone] = statusInfo(node); return `<span class="fa-badge" data-tone="${tone}">${text}</span>`; }
function childrenText(node) {
  const count = node.children.length;
  if (!count) return labels[node.kind] || node.kind;
  const kinds = new Set(node.children.map(id => nodes.get(id).kind));
  const noun = kinds.size === 1 && kinds.has('capability') ? 'capacité' : kinds.size === 1 && kinds.has('reference') ? 'référence' : 'élément';
  return `${count} ${noun}${count > 1 ? 's' : ''}`;
}
function showNotice(message, action = '') { notice.innerHTML = message ? `<div class="fa-banner"><span>${esc(message)}</span>${action}</div>` : ''; }
function announce(message) { document.getElementById('fa-announcement').textContent = message; }
function route() {
  const params = new URLSearchParams();
  if (state.publication) params.set('version', state.publication);
  params.set('node', state.id);
  if (state.view !== 'map') params.set('view', state.view);
  if (state.query) params.set('q', state.query);
  if (state.type !== 'all') params.set('type', state.type);
  if (state.statusFilter !== 'all') params.set('status', state.statusFilter);
  if (state.journey >= 0) params.set('step', String(state.journey));
  if (state.sourcePath) { params.set('source', state.sourcePath); if (state.sourceAnchor) params.set('anchor', state.sourceAnchor); }
  return '#' + params.toString();
}
function readRoute() {
  const params = new URLSearchParams(location.hash.slice(1));
  const defaultNode = 'transactional';
  const requested = params.get('node') || defaultNode;
  state.id = nodes.has(requested) && requested !== 'atlas' && !(requested === 'process' && !nodes.get('process').children.length) ? requested : defaultNode;
  routeNotice = !nodes.has(requested) ? `L’élément ${requested} n’existe pas dans le modèle courant. La vue d’ensemble est affichée.` : '';
  state.view = params.get('view') === 'links' ? 'links' : 'map';
  state.query = params.get('q') || '';
  state.type = ['domain', 'reference', 'group', 'capability', 'object', 'document', 'event', 'component', 'flow', 'authority', 'responsibility', 'landscape'].includes(params.get('type')) ? params.get('type') : 'all';
  state.statusFilter = ['ai_proposed', 'under_instruction', 'urbanist_validated', 'validated', 'partial', 'review', 'illustration', 'proposed', 'declared', 'observed', 'not_assessed'].includes(params.get('status')) ? params.get('status') : 'all';
  const step = Number(params.get('step'));
  state.journey = params.has('step') && Number.isInteger(step) && steps[step]?.id === state.id ? step : -1;
  state.sourcePath = params.get('source') || '';
  state.sourceAnchor = params.get('anchor') || '';
  const available = [...nodes.values()].filter(node => node.kind !== 'model');
  if (!available.some(node => node.kind === state.type)) state.type = 'all';
  if (!available.some(node => node.status === state.statusFilter)) state.statusFilter = 'all';
  search.value = state.query;
}
function saveRoute(replace = false) {
  const next = route();
  if (location.hash !== next) {
    if (!replace) { navigationIndex++; maxIndex = navigationIndex; }
    history[replace ? 'replaceState' : 'pushState']({ atlasIndex: navigationIndex }, '', next);
    try { sessionStorage.setItem('flow-atlas:max-index', String(maxIndex)); } catch { /* Optional persistence. */ }
  }
  document.getElementById('fa-back').disabled = navigationIndex <= 0;
  document.getElementById('fa-forward').disabled = navigationIndex >= maxIndex;
}
function move(id, view = 'map', keepJourney = false) {
  if (!nodes.has(id)) return;
  if (id === 'atlas' || (id === 'process' && !nodes.get(id).children.length)) id = 'transactional';
  const fromTree = tree.contains(document.activeElement), wasDrawer = treeOpen;
  if (!keepJourney) state.journey = -1;
  Object.assign(state, { id, view, query: '', sourcePath: '', sourceAnchor: '' });
  search.value = '';
  revealSelection();
  saveRoute(); render(); syncSource();
  announce(`${nodes.get(id).name}. ${labels[nodes.get(id).kind]}.`);
  main.scrollTop = 0;
  const selected = [...tree.querySelectorAll('[role="treeitem"]')].find(el => el.dataset.treeId === id);
  if (selected && !narrowScreen.matches) selected.scrollIntoView({ block: 'nearest' });
  if (wasDrawer) setTreeOpen(false, false);
  if (fromTree && !wasDrawer) focusTree(id); else focusContent();
}
function tile(node) {
  return `<button class="fa-tile" data-go="${esc(node.id)}"><span class="fa-tile-top"><span class="fa-id">${node.id.startsWith('ILL-') ? 'ILLUSTRATION' : esc(node.kind === 'model' ? 'MODÈLE' : node.id)}</span>${badge(node)}</span><span class="fa-tile-name">${esc(node.name)}</span><span class="fa-tile-purpose">${esc(node.purpose)}</span><span class="fa-tile-foot"><span>${childrenText(node)}</span>${icon('arrow-up-right')}</span></button>`;
}
function sourceLink(id) {
  const prefix = id.match(/^[A-Z]+/)?.[0];
  const registries = { U: '01-contributions-utilisateur', F: '02-assertions', A: '03-contributions-assistant', C: '04-corrections', P: '05-propositions', Q: '06-questions' };
  return registries[prefix] ? { path: `connaissance/${registries[prefix]}.md`, anchor: id.toLowerCase() } : null;
}
function sourceButton(link, label, cls = '') {
  return `<button class="${cls}" data-source-path="${esc(link.path)}" data-source-anchor="${esc(link.anchor || '')}">${esc(label)}</button>`;
}
const fieldLabels = {name: 'Libellé', definition: 'Définition', finality: 'Finalité', scope: 'Périmètre', nature: 'Nature'};
function fieldNames(fields) { return fields.map(key => fieldLabels[key] || key).join(', '); }
function publicationDate(value) {
  if (!value || Number.isNaN(Date.parse(value))) return 'Non renseignée';
  return new Intl.DateTimeFormat('fr-FR', {dateStyle:'long', timeStyle:'short'}).format(new Date(value));
}
function validationSummary(node) {
  const approved = node.lifecycle?.validated_fields || node.approvedFields || [];
  const proposed = node.proposedFields || [];
  return `<div class="fa-validation-summary">${badge(node)}<span>${approved.length ? `Champs adoptés : ${esc(fieldNames(approved))}.` : 'Aucun champ explicitement adopté.'}${proposed.length ? ` À valider : ${esc(fieldNames(proposed))}.` : ''}</span></div>`;
}
function businessSheet(node) {
  const relation = node.parentRelation;
  return `<article class="fa-business" aria-label="Fiche métier de ${esc(node.name)}"><section class="fa-finality"><h2>Finalité</h2><p>${esc(node.purpose || 'À documenter.')}</p></section><section><h2>Définition</h2><p>${esc(node.definition || 'À documenter.')}</p></section>${node.scope ? `<section><h2>Périmètre</h2><p>${esc(node.scope)}</p></section>` : ''}${node.statusNote ? `<section class="fa-review-note"><h2>État de l’instruction</h2><p>${esc(node.statusNote)}</p>${node.missingFields?.length ? `<p>Champs à valider : ${esc(fieldNames(node.missingFields))}.</p>` : ''}</section>` : ''}${relation?.review?.note ? `<section class="fa-boundary"><h2>Rattachement et frontières</h2><p>${esc(relation.review.note)}</p>${relation.review.state === 'under_review' ? '<span class="fa-badge" data-tone="amber">Rattachement en réexamen</span>' : ''}</section>` : ''}</article>`;
}
function inspector(node) {
  const refs = node.sources.map(id => { const link = node.sourceLinks?.find(item => item.id === id) || sourceLink(id); return link ? sourceButton(link, id) : `<span>${esc(id)}</span>`; }).join('');
  const source = node.sourcePath ? sourceButton({path: node.sourcePath, anchor: node.sourceAnchor || ''}, 'Ouvrir le registre source', 'fa-button fa-source-open') : '';
  const relation = node.parentRelation;
  return `<details class="fa-provenance" id="fa-provenance"><summary>Sources et validation <span>${node.sources.length} références</span></summary><div class="fa-proof-body"><section><h2>Publication et révision</h2><dl><dt>Révision de l’élément</dt><dd>${esc(node.revision ?? 'Non renseignée')}</dd><dt>Dernière modification</dt><dd><time title="${esc(node.lastModified || '')}">${esc(publicationDate(node.lastModified))}</time></dd></dl></section><section><h2>Portée de validation</h2><p>Champs adoptés : ${esc(fieldNames(node.approvedFields || []) || 'aucun champ explicitement adopté')}.</p>${node.proposedFields?.length ? `<p>Champs proposés, à valider : ${esc(fieldNames(node.proposedFields))}.</p>` : ''}${node.lifecycle ? `<h3>Cycle de vie</h3><p>${esc(node.lifecycle.note || '')}</p><p>Portée validée : ${esc(fieldNames(node.lifecycle.validated_fields || []) || 'aucune')}.</p><p>Enregistré le ${esc(publicationDate(node.lifecycle.recorded_at))} · ${esc(node.lifecycle.recorded_by || '')}</p>` : ''}${node.adoptionIds?.length ? `<h3>Adoptions</h3><p class="fa-source-path">${esc(node.adoptionIds.join(', '))}</p>` : ''}</section>${relation ? `<section><h2>Preuves du rattachement</h2><p>${esc(relation.review?.note || '')}</p><p class="fa-source-path">${esc(relation.id)} · ${esc((relation.source_refs || []).join(', '))}</p></section>` : ''}<section><h2>Sources et provenance</h2><div class="fa-source">${refs || 'Aucune référence renseignée.'}</div>${source}<p class="fa-source-path">${esc(node.sourcePath || '')}</p></section>${node.modelPath ? `<section><h2>Modèle structuré</h2><p class="fa-source-path">${esc(node.modelPath)} · ${esc(node.id)}</p></section>` : ''}</div></details>`;
}
function relationView(node) {
  const links = related(node.id);
  if (!links.length) return `<div class="fa-empty">${kind(node)}<h2>Relations à documenter</h2><p>Aucune relation métier détaillée n’est représentée pour cet élément dans cette vue.</p>${node.children.length ? '<button class="fa-button" data-view="map">Explorer les éléments rattachés</button>' : ''}${steps.length ? '<button class="fa-button" data-journey="start">Voir l’exemple d’une promesse</button>' : ''}</div>`;
  return `<div class="fa-relations"><svg class="fa-links-svg" aria-hidden="true"></svg><div class="fa-graph-center">${kind(node)}<strong>${esc(node.name)}</strong></div><div class="fa-related-grid">${links.map(link => { const target = nodes.get(link.target); return `<button class="fa-related" data-go="${esc(target.id)}" data-open-view="links"><span class="fa-relation-label">${esc(link.label)} ↓</span>${kind(target)}<strong>${esc(target.name)}</strong><span class="fa-badge" data-tone="${link.status === 'illustration' ? 'purple' : 'neutral'}">${link.isIllustration || link.status === 'illustration' ? 'Lien illustratif' : link.lifecycle ? esc(lifecycleLabels[link.lifecycle.state]?.[0] || '') : 'Lien de lecture'} · ${esc(link.sources.join(', '))}</span></button>`; }).join('')}</div><p class="fa-edge-note">Les verbes se lisent depuis l’élément sélectionné. Les liens ne constituent pas une décomposition.</p></div>`;
}
function mapView(node) {
  if (node.id === 'transactional' && node.children.includes('business-references')) {
    const group = nodes.get('business-references');
    return `<div class="fa-grid">${node.children.filter(id => id !== group.id).map(id => tile(nodes.get(id))).join('')}</div><section class="fa-ref-group"><div class="fa-ref-head"><div><h2>${esc(group.name)}</h2><small>Groupe de présentation · ${childrenText(group)}</small></div><button class="fa-button" data-go="business-references">Explorer le groupe ${icon('arrow-right')}</button></div><div class="fa-ref-chips">${group.children.map(id => `<button data-go="${esc(id)}">${esc(nodes.get(id).name)}</button>`).join('')}</div></section><p class="fa-footnote">Les branches décrivent la structure du modèle. Elles ne représentent pas un enchaînement de processus.</p>`;
  }
  return node.children.length ? `<div class="fa-grid">${node.children.map(id => tile(nodes.get(id))).join('')}</div>` : '';
}
function renderJourney() {
  const area = document.getElementById('fa-journey');
  area.hidden = state.journey < 0;
  if (area.hidden) return;
  const step = steps[state.journey];
  area.className = 'fa-journey';
  area.innerHTML = `<div class="fa-journey-top"><strong>Suivre une promesse · ${state.journey + 1}/${steps.length}</strong><button class="fa-ghost" data-journey="close">Quitter le parcours ×</button></div><div class="fa-stepper">${steps.map((item, index) => `<button data-step="${index}" aria-current="${index === state.journey ? 'step' : 'false'}">${index + 1} · ${esc(item.label)}</button>`).join('')}</div><p>${esc(step.text)}</p><div class="fa-journey-actions"><span class="fa-badge" data-tone="purple">Détails métier illustratifs</span><button class="fa-button" data-journey="prev" ${state.journey === 0 ? 'disabled' : ''}>Précédent</button><button class="fa-button fa-primary" data-journey="next">${state.journey === steps.length - 1 ? 'Terminer' : 'Continuer →'}</button></div>`;
}
function drawEdges() {
  const graph = root.querySelector('.fa-relations');
  if (!graph) return;
  const svg = graph.querySelector('.fa-links-svg');
  const rect = graph.getBoundingClientRect();
  const center = graph.querySelector('.fa-graph-center').getBoundingClientRect();
  const x = center.left + center.width / 2 - rect.left, y = center.bottom - rect.top;
  svg.setAttribute('viewBox', `0 0 ${rect.width} ${rect.height}`);
  svg.innerHTML = [...graph.querySelectorAll('.fa-related')].map(element => {
    const target = element.getBoundingClientRect();
    const tx = target.left + target.width / 2 - rect.left, ty = target.top - rect.top;
    return `<path d="M ${x} ${y} C ${x} ${y + 18}, ${tx} ${ty - 20}, ${tx} ${ty}"/>`;
  }).join('');
}
function score(node, query) {
  const q = normalize(query).trim();
  const terms = normalize([node.name, node.id, node.purpose, node.definition, node.aliases, node.sources.join(' ')].join(' '));
  if (!q.split(/\s+/).every(term => terms.includes(term))) return 0;
  return (normalize(node.id) === q ? 100 : 0) + (normalize(node.name) === q ? 90 : 0) + (normalize(node.name).includes(q) ? 40 : 0) + (normalize(node.aliases).includes(q) ? 20 : 0) + 1;
}
function highlight(value, query) {
  const text = String(value || '');
  const flat = normalize(text);
  const ranges = [];
  normalize(query).trim().split(/\s+/).filter(Boolean).forEach(term => {
    let start = flat.indexOf(term);
    while (start !== -1) { ranges.push([start, start + term.length]); start = flat.indexOf(term, start + term.length); }
  });
  ranges.sort((a, b) => a[0] - b[0]);
  let output = '', offset = 0;
  ranges.forEach(([start, end]) => { if (start < offset) return; output += esc(text.slice(offset, start)) + '<mark>' + esc(text.slice(start, end)) + '</mark>'; offset = end; });
  return output + esc(text.slice(offset));
}
function matches() {
  return [...nodes.values()].filter(node => node.kind !== 'model').map(node => ({ node, score: score(node, state.query) })).filter(item => item.score && (state.type === 'all' || item.node.kind === state.type) && (state.statusFilter === 'all' || item.node.status === state.statusFilter)).sort((a, b) => b.score - a.score || a.node.name.localeCompare(b.node.name, 'fr'));
}
function searchResults() {
  const results = matches();
  return `<p class="fa-count" role="status">${results.length} résultat${results.length > 1 ? 's' : ''} dans tout le modèle</p><div class="fa-results">${results.map(({ node }) => {
    const path = lineage(node).filter(item => !['atlas', 'transactional'].includes(item.id));
    const aliasMatch = normalize(node.aliases).includes(normalize(state.query));
    return `<button class="fa-result" data-go="${esc(node.id)}"><span class="fa-result-top"><span>${highlight(node.name, state.query)}</span>${badge(node)}</span><p>${highlight(node.definition || node.purpose, state.query)}</p>${aliasMatch ? `<p>Vocabulaire associé : ${highlight(node.aliases, state.query)}</p>` : ''}<div class="fa-result-path">${labels[node.kind]} · ${highlight(node.id, state.query)} · ${esc(path.slice(0, -1).map(item => item.name).join(' / ') || nodes.get(model.modelOf(node))?.name || 'Modèle')}</div></button>`;
  }).join('') || '<div class="fa-empty"><h2>Aucun résultat</h2><p>Recherche un nom, un mot de la définition ou un identifiant publié, par exemple « Stocktaking », « stock » ou « D03.b ».</p><button class="fa-button" data-reset-filters>Réinitialiser les filtres</button></div>'}</div>`;
}
function renderSearch() {
  const available = [...nodes.values()].filter(node => node.kind !== 'model');
  const types = [...new Set(available.map(node => node.kind))];
  const statuses = [...new Set(available.map(node => node.status))];
  const options = (values, property, label) => values.map(value => `<option value="${esc(value)}">${esc(label(value))} (${available.filter(node => node[property] === value).length})</option>`).join('');
  const statusLabel = value => lifecycleLabels[value]?.[0] || ({validated:'Validés dans leur portée',partial:'Validation partielle',review:'En réexamen',proposed:'Non validés'})[value] || statusInfo(available.find(node => node.status === value))[0];
  content.innerHTML = `<div class="fa-heading"><div class="fa-heading-text"><div class="fa-eyebrow">Recherche directe</div><h1 tabindex="-1">Retrouver un élément</h1><p>Noms, identifiants et textes de la publication consultée.</p></div><button class="fa-button" data-clear-search>Revenir à la fiche</button></div><div class="fa-search-filters"><label>Type <select id="fa-type"><option value="all">Tous les éléments</option>${options(types, 'kind', type => labels[type])}</select></label><label>Statut <select id="fa-status"><option value="all">Tous les statuts</option>${options(statuses, 'status', statusLabel)}</select></label><button class="fa-button" data-reset-filters>Effacer les filtres</button><button class="fa-button" data-share>Copier le lien</button></div><div id="fa-results-area">${searchResults()}</div>`;
  document.getElementById('fa-type').value = state.type;
  document.getElementById('fa-status').value = state.statusFilter;
}
function render() {
  if (!model) return;
  const node = nodes.get(state.id);
  document.title = `${state.query ? `Recherche : ${state.query}` : node.name} — FLOW Atlas`;
  let path = lineage(node).filter(item => item.id !== 'atlas');
  if (!node.parentId && node.modelId) path = [nodes.get(node.modelId), node];
  document.getElementById('fa-breadcrumb').innerHTML = path.map((item, index) => `${index ? '<span aria-hidden="true">/</span>' : ''}${index === path.length - 1 ? `<span aria-current="page">${esc(item.name)}</span>` : `<button data-go="${esc(item.id)}">${esc(item.name)}</button>`}`).join('');
  renderTree();
  document.getElementById('fa-back').disabled = navigationIndex <= 0;
  document.getElementById('fa-forward').disabled = navigationIndex >= maxIndex;
  renderJourney();
  if (state.query) { renderSearch(); return; }
  const isOverview = node.kind === 'model', links = related(node.id);
  if (!links.length) state.view = 'map';
  const children = node.children.length;
  const childHeading = node.children.every(id => nodes.get(id).kind === 'capability') ? 'Capacités' : 'Éléments rattachés';
  const capCount = [...nodes.values()].filter(item => item.kind === 'capability').length;
  content.innerHTML = `<div class="fa-heading"><div class="fa-heading-text"><div class="fa-eyebrow">${isOverview ? 'Le modèle publié' : `${esc(nodeKind(node))} <span class="fa-heading-id">${esc(node.id)}</span>`}</div><h1 tabindex="-1">${esc(node.name)}</h1>${isOverview ? `<p>Explore les branches du modèle et découvre ce que recouvre chaque capacité.</p>` : ''}</div><div class="fa-heading-actions">${!isOverview ? '<button class="fa-button" data-proof>Sources et validation</button>' : ''}<button class="fa-button" data-share>Copier le lien</button></div></div>${isOverview ? `<div class="fa-overview-note">${capCount} capacités · ${children} branches à explorer <span>Publier ne vaut pas valider.</span></div>` : validationSummary(node)}${links.length ? `<div class="fa-toolbar"><div class="fa-segments" aria-label="Vue de l’élément"><button data-view="map" aria-pressed="${state.view === 'map'}">Fiche</button><button data-view="links" aria-pressed="${state.view === 'links'}">Relations · ${links.length}</button></div></div>` : ''}${state.view === 'links' ? `<section aria-label="Relations de ${esc(node.name)}">${relationView(node)}</section>` : `${isOverview ? '' : businessSheet(node)}${children ? `<section class="fa-children" aria-label="Structure de ${esc(node.name)}">${isOverview ? '' : `<div class="fa-section-heading"><h2>${childHeading}</h2><span>${children}</span></div>`}${mapView(node)}</section>` : ''}${!isOverview && !links.length ? '<p class="fa-relations-empty">Aucune relation métier documentée dans cette publication.</p>' : ''}`}${isOverview ? '' : inspector(node)}`;
  requestAnimationFrame(drawEdges);
}
async function fetchJson(url) {
  const response = await fetch(url, { cache: 'no-store' });
  const body = await response.json();
  if (!response.ok) throw new Error(typeof body.error === 'string' ? body.error : body.error?.message || body.message || `Erreur ${response.status}`);
  return body;
}
async function refresh(initial = false) {
  if (refreshPending) return;
  refreshPending = true;
  document.getElementById('fa-publication').disabled = true;
  const requestedSpace = state.space;
  document.getElementById('fa-refresh').disabled = true;
  if (data?.space !== state.space) content.innerHTML = '<p>Chargement de cet espace…</p>';
  showNotice(initial ? 'Lecture du modèle JSON…' : 'Actualisation en cours…');
  try {
    const selectedSpace = state.space;
    const [nextData, exploration, catalog] = await Promise.all([fetchJson('/api/model' + (state.publication ? '?version=' + encodeURIComponent(state.publication) : '')), fetchJson('/exploration.json'), fetchJson('/api/releases')]);
    if (selectedSpace !== state.space) return;
    if (nextData.space !== 'release') throw new Error('Urbanisation publiée attendue.');
    const nextModel = createModel(nextData, exploration);
    data = nextData; model = nextModel;
    ({ nodes, labels, icons, steps } = model);
    seenRevision = data.dataRevision;
    const select = document.getElementById('fa-publication');
    select.innerHTML = catalog.versions.map(item => `<option value="${esc(item.version === catalog.current_version ? '' : item.version)}">${esc(item.revision ? 'v' + String(item.revision).padStart(3, '0') : item.version)}${item.version === catalog.current_version ? ' · dernière' : ''}</option>`).join('');
    select.value = state.publication === catalog.current_version ? '' : state.publication;
    readRoute();
    if (initial) history.replaceState({ atlasIndex: navigationIndex }, '', route());
    document.getElementById('fa-date').textContent = `Urbanisation · ${data.revision ? 'v' + String(data.revision).padStart(3, '0') : data.version} · ${new Date(data.date).toLocaleDateString('fr-FR')}`;
    document.getElementById('fa-version').textContent = (data.revision ? 'v' + data.revision + ' · ' : '') + data.version;
    document.getElementById('fa-space-note').textContent = 'Urbanisation';
    revealSelection();
    render();
    const caps = [...nodes.values()].filter(n => n.kind === 'capability');
    const summary = caps.some(n => n.lifecycle)
      ? `Urbanisation : ${caps.length} capacités · ${caps.filter(n => n.status === 'ai_proposed').length} proposées par l’IA · ${caps.filter(n => n.status === 'under_instruction').length} en cours d’instruction · ${caps.filter(n => n.status === 'urbanist_validated').length} validées par l’urbaniste, selon la portée de chaque fiche.`
      : `Urbanisation : ${caps.length} capacités, dont ${caps.filter(n => n.status === 'validated').length} validées. Les autres statuts restent explicites.`;
    showNotice(routeNotice);
    await syncSource(true);
    announce(summary);
  } catch (error) {
    showNotice(`Le modèle n’a pas pu être chargé : ${error.message}`, '<button class="fa-button" data-retry>Réessayer</button>');
    if (!model || data?.space !== state.space) { model = null; nodes = new Map(); content.innerHTML = '<div class="fa-empty"><h1>Le modèle est indisponible</h1><p>Vérifie les fichiers source et réessaie. Les détails de l’erreur sont affichés au-dessus.</p></div>'; }
  } finally { refreshPending = false; document.getElementById('fa-refresh').disabled = false; document.getElementById('fa-publication').disabled = false; if (requestedSpace !== state.space) void refresh(); }
}
function slug(value) { return normalize(value).replace(/[^a-z0-9\s-]/g, '').trim().replace(/\s+/g, '-'); }
function inlineMarkdown(raw) {
  let text = esc(raw);
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, label, encodedTarget) => {
    const target = encodedTarget.replaceAll('&amp;', '&');
    if (/^https?:\/\//i.test(target)) return `<a href="${esc(target)}" target="_blank" rel="noopener noreferrer">${label}</a>`;
    if (/^[a-z]+:/i.test(target)) return label;
    try {
      const url = new URL(target, `${location.origin}/${currentSource.path}`);
      if (url.origin !== location.origin || !url.pathname.endsWith('.md')) return label;
      return `<button class="fa-doc-link" data-source-path="${esc(decodeURIComponent(url.pathname.slice(1)))}" data-source-anchor="${esc(decodeURIComponent(url.hash.slice(1)))}">${label}</button>`;
    } catch { return label; }
  });
  return text.replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
}
function renderDocument() {
  if (!currentSource) return;
  const lines = currentSource.content.split(/\r?\n/);
  const output = [];
  const anchors = new Map();
  let index = 0;
  while (index < lines.length) {
    const line = lines[index], number = index + 1;
    if (line.startsWith('```')) {
      const code = []; index++;
      while (index < lines.length && !lines[index].startsWith('```')) code.push(lines[index++]);
      output.push(`<pre data-line="${number}"><code>${esc(code.join('\n'))}</code></pre>`); index++; continue;
    }
    const explicit = line.match(/^<a\s+id=["']([^"']+)["']\s*><\/a>\s*$/);
    if (explicit) { output.push(`<div data-anchor="${esc(explicit[1])}" data-line="${number}"></div>`); index++; continue; }
    const heading = line.match(/^(#{1,6})\s+(.+)$/);
    if (heading) {
      const base = slug(heading[2]); const duplicate = anchors.get(base) || 0; anchors.set(base, duplicate + 1);
      output.push(`<h${Math.min(heading[1].length + 1, 6)} data-anchor="${esc(base + (duplicate ? '-' + duplicate : ''))}" data-line="${number}">${inlineMarkdown(heading[2])}</h${Math.min(heading[1].length + 1, 6)}>`); index++; continue;
    }
    if (line.trim().startsWith('|') && lines[index + 1]?.match(/^\s*\|?\s*:?-{3,}/)) {
      const cells = row => row.trim().replace(/^\||\|$/g, '').split('|').map(cell => cell.trim());
      const head = cells(line); index += 2;
      const rows = [];
      while (index < lines.length && lines[index].trim().startsWith('|')) rows.push(cells(lines[index++]));
      output.push(`<div class="fa-doc-table" data-line="${number}"><table><thead><tr>${head.map(cell => `<th>${inlineMarkdown(cell)}</th>`).join('')}</tr></thead><tbody>${rows.map(row => `<tr>${row.map(cell => `<td>${inlineMarkdown(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`); continue;
    }
    if (line.trim()) output.push(`<p data-line="${number}"${/^\s*[-*]\s/.test(line) ? ' class="fa-doc-list"' : ''}>${inlineMarkdown(line)}</p>`);
    index++;
  }
  sourceBody.innerHTML = output.join('');
}
function scrollSourceAnchor(anchor) {
  if (!anchor) { sourceBody.scrollTop = 0; return; }
  const target = [...sourceBody.querySelectorAll('[data-anchor]')].find(element => element.dataset.anchor === anchor || normalize(element.dataset.anchor) === normalize(anchor));
  if (target) { target.classList.add('fa-source-target'); target.scrollIntoView({ block: 'start' }); }
  else document.getElementById('fa-source-location').textContent += ' · repère non trouvé dans cette version';
}
async function syncSource(force = false) {
  if (!state.sourcePath) { sourceRequest++; if (sourceDialog.open) sourceDialog.close(); return; }
  const request = ++sourceRequest;
  if (!sourceDialog.open) sourceDialog.showModal();
  document.getElementById('fa-source-title').textContent = 'Lecture de la source…';
  document.getElementById('fa-source-find').value = '';
  document.getElementById('fa-source-find').disabled = true;
  sourceBody.textContent = 'Chargement…';
  try {
    const nextSource = force || currentSource?.path !== state.sourcePath ? await fetchJson('/api/source?' + new URLSearchParams({ path: state.sourcePath, anchor: state.sourceAnchor })) : currentSource;
    if (request !== sourceRequest) return;
    currentSource = nextSource;
    document.getElementById('fa-source-find').disabled = false;
    document.getElementById('fa-source-title').textContent = currentSource.title || state.sourcePath;
    document.getElementById('fa-source-location').textContent = currentSource.path + (state.sourceAnchor ? ` #${state.sourceAnchor}` : '');
    renderDocument(); requestAnimationFrame(() => scrollSourceAnchor(state.sourceAnchor));
  } catch (error) {
    if (request !== sourceRequest) return;
    document.getElementById('fa-source-title').textContent = 'Source indisponible';
    sourceBody.textContent = error.message;
  }
}
function openSource(path, anchor) { if (!sourceDialog.open) sourceTrigger = document.activeElement; state.sourcePath = path; state.sourceAnchor = anchor; saveRoute(); syncSource(); }
function closeSource() { state.sourcePath = ''; state.sourceAnchor = ''; sourceRequest++; if (sourceDialog.open) sourceDialog.close(); saveRoute(true); if (sourceTrigger?.isConnected) sourceTrigger.focus({ preventScroll: true }); else focusContent(); }
function findInSource() {
  if (!currentSource || currentSource.path !== state.sourcePath || document.getElementById('fa-source-find').disabled) return;
  renderDocument();
  const query = document.getElementById('fa-source-find').value.trim();
  if (!query) { scrollSourceAnchor(state.sourceAnchor); return; }
  const walker = document.createTreeWalker(sourceBody, NodeFilter.SHOW_TEXT);
  const texts = []; while (walker.nextNode()) texts.push(walker.currentNode);
  let first;
  for (const text of texts) {
    if (!normalize(text.textContent).includes(normalize(query))) continue;
    const span = document.createElement('span'); span.innerHTML = highlight(text.textContent, query);
    text.replaceWith(span); first ||= span.querySelector('mark');
  }
  if (first) first.scrollIntoView({ block: 'center' });
  document.getElementById('fa-source-location').textContent = `${currentSource.path} · ${sourceBody.querySelectorAll('mark').length} correspondances`;
}
async function copyLink() {
  try { await navigator.clipboard.writeText(location.href); showNotice('Lien copié. Il ouvrira cette vue sur une machine où FLOW Atlas est lancé.'); }
  catch { showNotice('Copie ce lien : ' + location.href); }
}
root.addEventListener('click', event => {
  const button = event.target.closest('button');
  if (!button || button.disabled) return;
  if (button.id === 'fa-tree-open') return setTreeOpen(true);
  if (['fa-tree-close', 'fa-tree-backdrop'].includes(button.id)) return setTreeOpen(false);
  if (button.hasAttribute('data-proof')) { const proof = document.getElementById('fa-provenance'); proof.open = true; proof.querySelector('summary').focus(); proof.scrollIntoView({block: 'start'}); return; }
  if (button.dataset.go) return move(button.dataset.go, button.dataset.openView || 'map');
  if (button.dataset.view) return move(state.id, button.dataset.view, state.journey >= 0);
  if (button.id === 'fa-back') return history.back();
  if (button.id === 'fa-forward') return history.forward();
  if (button.id === 'fa-refresh' || button.hasAttribute('data-retry')) return void refresh();
  if (button.hasAttribute('data-share')) return void copyLink();
  if (button.dataset.sourcePath) return openSource(button.dataset.sourcePath, button.dataset.sourceAnchor || '');
  if (button.hasAttribute('data-reset-filters')) { state.type = 'all'; state.statusFilter = 'all'; saveRoute(); render(); content.querySelector('[data-reset-filters]')?.focus(); return; }
  if (button.hasAttribute('data-clear-search')) { state.query = ''; search.value = ''; saveRoute(); render(); focusContent(); return; }
  if (button.dataset.journey || button.dataset.step !== undefined) {
    if (!steps.length) return;
    const action = button.dataset.journey;
    if (action === 'close') { state.journey = -1; saveRoute(true); return render(); }
    if (action === 'next' && state.journey === steps.length - 1) return move(model.confirmation, 'links');
    state.journey = button.dataset.step !== undefined ? Number(button.dataset.step) : action === 'start' ? 0 : state.journey + (action === 'prev' ? -1 : 1);
    return move(steps[state.journey].id, 'links', true);
  }
});
root.addEventListener('change', event => {
  if (event.target.id === 'fa-publication') {
    if (refreshPending) return;
    state.publication = event.target.value;
    saveRoute(); return void refresh();
  }
  if (!['fa-type', 'fa-status'].includes(event.target.id)) return;
  if (event.target.id === 'fa-type') state.type = event.target.value; else state.statusFilter = event.target.value;
  saveRoute(); document.getElementById('fa-results-area').innerHTML = searchResults();
});
search.addEventListener('input', () => {
  if (!model) return;
  const starting = !state.query;
  state.query = search.value.trim(); state.journey = -1;
  saveRoute(!starting); render();
});
document.addEventListener('keydown', event => {
  if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k' && !sourceDialog.open) { event.preventDefault(); search.focus(); search.select(); }
  if (event.defaultPrevented) return;
  if (event.key === 'Escape' && state.query && !sourceDialog.open) { state.query = ''; search.value = ''; saveRoute(); render(); search.focus(); }
  if (event.key === 'ArrowDown' && event.target === search && state.query) { const first = content.querySelector('.fa-result'); if (first) { event.preventDefault(); first.focus(); } }
  if (event.key === 'Enter' && event.target === search && state.query) { const first = matches()[0]; if (first) { event.preventDefault(); move(first.node.id); } }
});
sourceDialog.addEventListener('click', event => { const button = event.target.closest('[data-source-path]'); if (button) openSource(button.dataset.sourcePath, button.dataset.sourceAnchor || ''); });
document.getElementById('fa-close-source').addEventListener('click', closeSource);
sourceDialog.addEventListener('cancel', event => { event.preventDefault(); closeSource(); });
document.getElementById('fa-source-find').addEventListener('input', findInSource);
function restore() {
  const publication = new URLSearchParams(location.hash.slice(1)).get('version') || '';
  if (publication !== state.publication) { state.publication = publication; return void refresh(); }
  const space = requestedSpace();
  if (space !== state.space) {
    state.space = space; return void refresh();
  }
  if (!model || refreshPending || data?.space !== state.space) return;
  if (history.state?.atlasIndex === undefined) {
    navigationIndex++; maxIndex = navigationIndex;
    history.replaceState({ atlasIndex: navigationIndex }, '', location.href);
  } else navigationIndex = history.state.atlasIndex;
  maxIndex = Math.max(maxIndex, navigationIndex);
  try { sessionStorage.setItem('flow-atlas:max-index', String(maxIndex)); } catch { /* Optional persistence. */ }
  readRoute(); revealSelection(); saveRoute(true); showNotice(routeNotice); render(); syncSource(); if (!state.sourcePath) { main.scrollTop = 0; focusContent(); }
}
window.addEventListener('popstate', restore);
window.addEventListener('hashchange', restore);
new ResizeObserver(() => requestAnimationFrame(drawEdges)).observe(content);
let checkingPublication = false;
async function checkPublication() {
  if (refreshPending || checkingPublication || document.hidden) return;
  checkingPublication = true;
  try {
    const status = await fetchJson('/api/status' + (state.publication ? '?version=' + encodeURIComponent(state.publication) : ''));
    if (!model || status.revision !== seenRevision) await refresh();
  } catch { showNotice('Le serveur local est momentanément indisponible. La reconnexion est automatique.'); }
  finally { checkingPublication = false; }
}
setInterval(checkPublication, 5000);
document.addEventListener('visibilitychange', () => { if (!document.hidden) void checkPublication(); });
refresh(true);

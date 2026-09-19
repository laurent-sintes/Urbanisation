// Browser checks for the published dependency explorer. No backlog reads, no
// publication writes: atlas.test is intercepted in-page. Optional ATLAS_URL
// adds an independent live-server smoke check with its real CSP and no routing.
import { createRequire } from 'node:module';
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { resolve, extname, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import assert from 'node:assert/strict';
import { loadPublication } from '../scripts/load-publication.mjs';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH ||
  'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root = fileURLToPath(new URL('../', import.meta.url));
const dist = resolve(root, 'app/dist');
const output = process.env.ATLAS_DEPENDENCIES_OUTPUT || resolve(root, 'audits/2026-09-19-atlas-dependencies/browser');
const liveBase = process.env.ATLAS_URL?.replace(/\/$/, '');
const historicalVersion = '2026-09-13.5'; // v003 descriptor, resolved by the shared reader.
const [published, historical] = await Promise.all([
  loadPublication(), loadPublication({ version: historicalVersion }),
]);
const current = published.raw;
const old = historical.raw;
const fileHashes = new Map();
for (const path of new Set([published.sourcePath, published.descriptorPath, historical.sourcePath, historical.descriptorPath])) {
  if (path) fileHashes.set(path, createHash('sha256').update(await readFile(resolve(root, path))).digest('hex'));
}
assert.ok(current.nodes.some(node => node.id === 'D07.c'));
assert.ok(old.nodes.some(node => node.id === 'D07.c'));

// A small, explicit HTTP-only fixture exercises semantics absent from older
// publications. Its business names and relations are test data, never adopted.
const fixtureVersion = '2099-09-19.1';
const sourceId = 'QA-SRC-DEPENDENCIES';
const sourcePath = 'fixtures/dependencies-source.md';
const node = (id, kind, name, extra = {}) => ({
  id, kind, layer: 'transactional', fields: { name, definition: `Exemple de test : ${name}.` },
  review: { state: 'proposed', note: 'Fixture HTTP de test uniquement.' }, source_refs: [], ...extra,
});
const contains = (source_id, target_id) => ({
  id: `QA-CONTAINS-${source_id}-${target_id}`, type: 'contains', source_id, target_id,
  fields: {}, review: { state: 'accepted' }, source_refs: [],
});
const fixture = {
  ...structuredClone(current), version: fixtureVersion, revision: 0,
  sourcePath: 'fixtures/dependencies-model.json', glossary: { terms: [] },
  sourceReferences: { [sourceId]: { path: sourcePath, anchor: 'preuve-qa' } },
  nodes: [
    node('QA-U1', 'group', 'Univers QA source', { level_ref: 'universe' }),
    node('QA-U2', 'group', 'Univers QA cible', { level_ref: 'universe' }),
    node('QA-D1', 'domain', 'Domaine QA source'),
    node('QA-D2', 'domain', 'Domaine QA cible'),
    node('D07.c', 'capability', 'Capacité QA focale'),
    node('QA-B', 'capability', 'Capacité QA destinataire'),
    node('QA-C', 'capability', 'Capacité QA comportement'),
    node('QA-EMPTY', 'capability', 'Capacité QA isolée'),
    node('QA-BHV', 'behavior', 'Comportement QA explicite'),
  ],
  relations: [
    contains('QA-U1', 'QA-D1'), contains('QA-U2', 'QA-D2'),
    contains('QA-D1', 'D07.c'), contains('QA-D1', 'QA-EMPTY'),
    contains('QA-D2', 'QA-B'), contains('QA-D2', 'QA-C'), contains('D07.c', 'QA-BHV'),
    {
      id: 'QA-NEEDS-A-B', type: 'relates-to', source_id: 'D07.c', target_id: 'QA-B',
      fields: { label: 'Mobilise une réponse métier QA' },
      qualification: {
        role: 'needs', meaning: 'Sens qualifié QA : déterminer la réponse nécessaire.',
        conditions: ['Condition QA : une demande est recevable.'],
        effects: ['Effet QA : une réponse métier devient disponible.'],
        scope: 'Portée QA : aucune séquence ni interface technique présumée.',
      },
      source_refs: [sourceId], source_locator: { path: sourcePath, anchor: 'preuve-qa' },
      review: { state: 'proposed', note: 'Qualification de test proposée, sans adoption.' },
      approved_fields: [], proposed_fields: ['qualification', 'fields.label'],
    },
    {
      id: 'QA-RESULT-B-A', type: 'relates-to', source_id: 'QA-B', target_id: 'D07.c',
      fields: { label: 'Transmet un résultat QA' },
      qualification: {
        role: 'result-transmitted', meaning: 'Résultat QA transmis dans le sens inverse.',
        conditions: ['Condition QA inverse : le résultat est établi.'],
        effects: ['Effet QA inverse : la capacité focale reçoit le résultat.'],
      },
      source_refs: [], review: { state: 'proposed' },
    },
    {
      id: 'QA-BEHAVIOR-C', type: 'relates-to', source_id: 'QA-BHV', target_id: 'QA-C',
      fields: { label: 'Mobilise depuis un comportement QA' },
      qualification: { role: 'needs', meaning: 'Le comportement QA explicite mobilise une capacité distincte.' },
      source_refs: [], review: { state: 'proposed' },
    },
  ],
};
const served = new Map([[current.version, current], [old.version, old], [fixtureVersion, fixture]]);
const modelRequests = [], sourceRequests = [], errors = [], checks = [], unexpectedRequests = [];
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });

async function verifyLiveServer(base) {
  // Keep the real server isolated from the fixture page and its request routes.
  const context = await browser.newContext({ viewport: { width: 1440, height: 1050 }, reducedMotion: 'reduce' });
  const liveChecks = [], pageErrors = [], consoleErrors = [], failedRequests = [], httpErrors = [], cspViolations = [];
  await context.addInitScript(() => addEventListener('securitypolicyviolation', event => {
    console.error(`CSP violation: ${event.effectiveDirective} blocked ${event.blockedURI}`);
  }));
  const page = await context.newPage();
  page.setDefaultTimeout(30000);
  page.on('pageerror', error => pageErrors.push(error.message));
  page.on('console', message => {
    if (message.type() !== 'error') return;
    consoleErrors.push(message.text());
    if (/CSP violation:|Content Security Policy|unsafe-eval/i.test(message.text())) cspViolations.push(message.text());
  });
  page.on('requestfailed', request => {
    const error = request.failure()?.errorText || '';
    if (!error.includes('ERR_ABORTED')) failedRequests.push({ url: request.url(), error });
  });
  page.on('response', response => {
    if (response.status() >= 400) httpErrors.push({ url: response.url(), status: response.status() });
  });
  try {
    const fetchModel = async version => {
      const response = await context.request.get(base + '/api/model' + (version ? '?version=' + version : ''));
      assert.equal(response.ok(), true, `Publication disponible sur le serveur réel : ${version || 'courante'}`);
      return response.json();
    };
    const liveCurrent = await fetchModel();
    const liveHistorical = await fetchModel(old.version);
    for (const [actual, expected] of [[liveCurrent, current], [liveHistorical, old]]) {
      assert.equal(actual.version, expected.version);
      assert.deepEqual(actual.nodes, expected.nodes, 'Le serveur restitue les éléments du snapshot exact');
      assert.deepEqual(actual.relations, expected.relations, 'Le serveur restitue les relations du snapshot exact');
    }
    const pane = page.getByTestId('dependencies-pane');
    const canvas = page.getByTestId('cytoscape-canvas');
    const waitGraph = async () => {
      await pane.waitFor();
      await canvas.locator('canvas').first().waitFor({ state: 'attached' });
      await page.waitForFunction(() => document.querySelector('[data-testid="cytoscape-canvas"]')?.getAttribute('data-status') === 'ready');
      assert.ok(Number(await canvas.getAttribute('data-node-count')) > 0, 'Le serveur réel produit un canvas non vide');
    };
    const route = (model, view, nodeId = 'D07.c') => base + '/#' + new URLSearchParams({ version: model.version, node: nodeId, view });
    const response = await page.goto(route(liveCurrent, 'relations'));
    const csp = response?.headers()['content-security-policy'];
    assert.ok(csp, 'La page réelle doit recevoir la CSP du serveur');
    assert.match(csp, /script-src 'self'/);
    assert.equal(csp.includes("'unsafe-eval'"), false, 'Le test ne doit pas assouplir la CSP pour Cytoscape');
    await waitGraph();
    assert.ok(Number(await canvas.getAttribute('data-edge-count')) > 0);
    const relation = liveCurrent.relations.find(item => item.type === 'relates-to' && item.source_id === 'D07.c' && item.qualification?.meaning);
    assert.ok(relation, 'Une relation originale qualifiée existe dans la publication courante');
    const picker = pane.getByLabel('Inspecter un élément', { exact: true });
    const edgeValues = await picker.locator('option').evaluateAll(options => options.map(option => option.value).filter(value => value.startsWith('edge|')));
    let selected = false;
    for (const value of edgeValues) {
      await picker.selectOption(value);
      const original = pane.locator(`[data-relation-id="${relation.id}"]`);
      if (!await original.count()) continue;
      await original.click();
      selected = true;
      break;
    }
    assert.ok(selected, 'Une arête du canvas donne accès à la relation originale');
    const relationInspector = page.getByTestId('relation-inspector');
    const qualifiedText = await relationInspector.innerText();
    for (const text of [relation.qualification.meaning, ...(relation.qualification.conditions || []),
      ...(relation.qualification.effects || []), relation.qualification.scope].filter(Boolean)) {
      assert.ok(qualifiedText.includes(text), `Qualification publiée conservée sur serveur réel : ${text}`);
    }
    const endpointIds = await relationInspector.locator('.relation-endpoints a').evaluateAll(links => links.map(link => new URLSearchParams(new URL(link.href).hash.slice(1)).get('node')));
    assert.deepEqual(endpointIds, [relation.source_id, relation.target_id]);
    await pane.locator('.dependency-options > summary').click();
    await pane.getByLabel('Disposition', { exact: true }).selectOption('hierarchical');
    await waitGraph();
    liveChecks.push('Publication courante : canvas réel, dispositions organique et hiérarchique sous CSP stricte, relation originale et qualification complète.');

    await page.goto(route(liveHistorical, 'relations'));
    await waitGraph();
    await pane.getByLabel('Inspecter un élément', { exact: true }).selectOption('node|D07.c');
    await page.getByTestId('dependency-inspector').getByRole('button', { name: 'Ouvrir la fiche', exact: true }).click();
    await page.getByTestId('business-sheet').waitFor();
    let params = new URLSearchParams(new URL(page.url()).hash.slice(1));
    assert.equal(params.get('version'), liveHistorical.version);
    assert.equal(params.get('node'), 'D07.c');
    await page.getByRole('tab', { name: /^Relations(?:\s|$)/ }).click();
    await waitGraph();
    params = new URLSearchParams(new URL(page.url()).hash.slice(1));
    assert.equal(params.get('version'), liveHistorical.version);
    assert.equal(params.get('view'), 'relations');
    liveChecks.push('Historique v003 : graphe, ouverture de fiche et retour Relations par l’interface conservent le snapshot.');

    const universe = liveCurrent.nodes.find(item => item.level_ref === 'universe' && liveCurrent.relations.some(link => ['contains', 'presents'].includes(link.type) && link.source_id === item.id));
    assert.ok(universe, 'Un univers publié porte une carte non vide');
    const expectedCards = liveCurrent.relations.filter(link => ['contains', 'presents'].includes(link.type) && link.source_id === universe.id).map(link => link.target_id).sort();
    await page.goto(route(liveCurrent, 'map', universe.id));
    await page.waitForFunction(expected => JSON.stringify([...document.querySelectorAll('.business-card[data-node-id]')].map(card => card.dataset.nodeId).sort()) === JSON.stringify(expected), expectedCards);
    await page.locator('.react-flow__viewport').waitFor();
    assert.equal(await page.locator('.business-card').count(), expectedCards.length);
    liveChecks.push('Carte univers ReactFlow : les cartes correspondent exactement aux enfants explicites de la publication courante.');

    assert.deepEqual(pageErrors, [], 'Aucune erreur JavaScript sur le serveur réel');
    assert.deepEqual(cspViolations, [], 'Aucune violation de la CSP réelle');
    assert.deepEqual(consoleErrors, [], 'Aucune erreur console sur le serveur réel');
    assert.deepEqual(failedRequests, [], 'Aucune requête échouée sur le serveur réel');
    assert.deepEqual(httpErrors, [], 'Aucune réponse HTTP en erreur sur le serveur réel');
    return { status: 'passed', base, csp, checks: liveChecks, pageErrors, consoleErrors, cspViolations, failedRequests, httpErrors };
  } finally {
    await context.close();
  }
}

try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1050 }, reducedMotion: 'reduce' });
  page.setDefaultTimeout(20000);
  page.on('pageerror', error => errors.push(error.message));
  await page.route('**/*', async route => {
    const url = new URL(route.request().url());
    if (url.origin !== 'http://atlas.test') {
      unexpectedRequests.push(url.href);
      return route.abort();
    }
    if (url.pathname === '/api/releases') return route.fulfill({ json: {
      current_version: current.version,
      versions: [current, old, fixture].map(value => ({ version: value.version, revision: value.revision })),
    } });
    if (url.pathname === '/api/model') {
      const version = url.searchParams.get('version');
      modelRequests.push(version);
      const value = served.get(version);
      return route.fulfill(value ? { json: value } : { status: 404, json: { error: 'Publication de test inconnue.' } });
    }
    if (url.pathname === '/api/source') {
      sourceRequests.push({ path: url.searchParams.get('path'), anchor: url.searchParams.get('anchor') });
      if (url.searchParams.get('path') !== sourcePath) return route.fulfill({ status: 404, json: { error: 'Source hors fixture.' } });
      return route.fulfill({ json: {
        path: sourcePath, title: 'Source QA des interactions',
        content: '# Source QA des interactions\n\n<a id="preuve-qa"></a>\n\nPreuve QA locale : une qualification reste distincte de son regroupement graphique.\n',
      } });
    }
    if (url.pathname.startsWith('/api/')) {
      unexpectedRequests.push(url.pathname);
      return route.fulfill({ status: 404, json: { error: 'API non attendue dans ce test.' } });
    }
    const file = resolve(dist, '.' + (url.pathname === '/' ? '/index.html' : decodeURIComponent(url.pathname)));
    if (!file.startsWith(dist + sep)) return route.abort();
    try {
      return route.fulfill({ body: await readFile(file), contentType: ({
        '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css',
        '.svg': 'image/svg+xml', '.png': 'image/png', '.webmanifest': 'application/manifest+json',
      })[extname(file)] || 'application/octet-stream' });
    } catch { return route.fulfill({ status: 404, body: 'Not found' }); }
  });

  const pane = page.getByTestId('dependencies-pane');
  const canvas = page.getByTestId('cytoscape-canvas');
  const inspector = page.getByTestId('dependency-inspector');
  const picker = () => pane.getByLabel('Inspecter un élément', { exact: true });
  const settle = async () => {
    await page.evaluate(() => new Promise(resolveFrame => requestAnimationFrame(() => requestAnimationFrame(resolveFrame))));
    await canvas.locator('canvas').first().waitFor({ state: 'attached' });
    await page.waitForFunction(() => document.querySelector('[data-testid="cytoscape-canvas"]')?.getAttribute('data-status') === 'ready');
    // A ResizeObserver refits after its debounce without changing layout status.
    // Wait for actual host/canvas geometry to stabilize before clicking/capturing.
    await page.waitForFunction(() => {
      const host = document.querySelector('[data-testid="cytoscape-canvas"]');
      const surface = host?.querySelector('canvas');
      if (!host || !surface) return false;
      const signature = JSON.stringify([host.clientWidth, host.clientHeight,
        surface.width, surface.height, surface.clientWidth, surface.clientHeight]);
      if (window.__dependencyCanvasStability?.signature !== signature) {
        window.__dependencyCanvasStability = { signature, since: performance.now() };
        return false;
      }
      return performance.now() - window.__dependencyCanvasStability.since >= 180;
    });
  };
  const visit = async (version, nodeId = 'D07.c') => {
    await page.goto('http://atlas.test/#' + new URLSearchParams({ ...(version ? { version } : {}), node: nodeId, view: 'relations' }));
    await pane.waitFor();
    await settle();
  };
  const configure = async (values) => {
    const details = pane.locator('details').filter({ has: page.locator('summary', { hasText: 'Affiner l’exploration' }) });
    if (await details.count() && !(await details.evaluate(element => element.open))) await details.locator('summary').click();
    for (const [label, value] of Object.entries(values)) {
      await pane.getByLabel(label, { exact: true }).selectOption(value);
      await settle();
    }
  };
  const counts = async () => ({
    nodes: Number(await canvas.getAttribute('data-node-count')),
    edges: Number(await canvas.getAttribute('data-edge-count')),
  });
  const selectEdgeContaining = async (relationId) => {
    const values = await picker().locator('option').evaluateAll(options => options.map(option => option.value).filter(value => value.startsWith('edge|')));
    for (const value of values) {
      await picker().selectOption(value);
      if (await page.locator(`[data-relation-id="${relationId}"]`).count()) {
        await page.locator(`[data-relation-id="${relationId}"]`).click();
        await page.getByTestId('relation-inspector').waitFor();
        return value;
      }
    }
    throw new Error(`Relation originale non retrouvée dans les arêtes affichées : ${relationId}`);
  };
  const screenshot = async (name) => pane.screenshot({
    path: resolve(output, name), animations: 'disabled',
    // Fixed chrome otherwise appears halfway through a tall element screenshot.
    style: '.topbar { visibility: hidden !important; }',
  });
  const assertNoOverflow = async () => assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), 'Débordement horizontal');

  await visit();
  await configure({ 'Niveau de lecture': 'capability', 'Qualification': 'all', 'Profondeur': '1', 'Sens de parcours': 'both' });
  const currentCounts = await counts();
  assert.ok(currentCounts.nodes > 0 && currentCounts.edges > 0, 'La publication courante doit produire un vrai graphe');
  assert.ok(modelRequests.includes(current.version));
  const realRelation = current.relations.find(relation => relation.type === 'relates-to' && relation.source_id === 'D07.c' && relation.qualification?.meaning);
  assert.ok(realRelation, 'La publication doit fournir une relation réelle qualifiée');
  await selectEdgeContaining(realRelation.id);
  assert.ok((await page.getByTestId('relation-inspector').innerText()).includes(realRelation.qualification.meaning));
  await screenshot('published-capabilities.png');
  checks.push('Publication courante résolue par index/descripteur/snapshot : canvas Cytoscape réel et relation originale qualifiée.');

  await configure({ 'Qualification': 'needs' });
  if (!current.relations.some(relation => relation.qualification?.role === 'needs')) {
    assert.equal((await counts()).edges, 0);
    assert.match(await pane.innerText(), /aucun|aucune|0 relation/i);
    checks.push('Publication sans rôle needs : filtre vide explicite, aucun repli sur le backlog.');
  }

  await visit(fixtureVersion);
  await configure({ 'Niveau de lecture': 'capability', 'Qualification': 'all', 'Profondeur': '1', 'Sens de parcours': 'both', 'Disposition': 'organic', 'Libellés': 'focus' });
  assert.ok((await counts()).edges >= 3);
  await selectEdgeContaining('QA-NEEDS-A-B');
  const qualified = page.getByTestId('relation-inspector');
  for (const text of [fixture.relations[7].qualification.meaning, ...fixture.relations[7].qualification.conditions,
    ...fixture.relations[7].qualification.effects, fixture.relations[7].qualification.scope]) {
    assert.ok((await qualified.innerText()).includes(text), `Qualification conservée : ${text}`);
  }
  assert.match(await qualified.innerText(), /propos/i);
  await qualified.getByText('Sources, révision et portée détaillée', { exact: true }).click();
  await qualified.getByRole('button', { name: sourceId, exact: true }).click();
  await page.getByTestId('source-document').getByText('Preuve QA locale', { exact: false }).waitFor();
  assert.deepEqual(sourceRequests.at(-1), { path: sourcePath, anchor: 'preuve-qa' });
  await page.getByRole('button', { name: 'Fermer la source', exact: true }).click();
  await screenshot('qualified-link.png');
  checks.push('Fixture HTTP : qualification complète, conditions, effets, portée, statut proposé et source documentaire conservés.');

  await selectEdgeContaining('QA-RESULT-B-A');
  const endpoints = page.getByTestId('relation-inspector').locator('.relation-endpoints a');
  const hrefs = await endpoints.evaluateAll(links => links.map(link => link.getAttribute('href')));
  assert.equal(new URLSearchParams(hrefs[0].split('#')[1]).get('node'), 'QA-B');
  assert.equal(new URLSearchParams(hrefs[1].split('#')[1]).get('node'), 'D07.c');
  await selectEdgeContaining('QA-BEHAVIOR-C');
  assert.ok((await page.getByTestId('relation-inspector').innerText()).includes('Comportement QA explicite'));
  checks.push('Deux sens et qualifications distincts gardent leurs extrémités ; une projection depuis un comportement conserve la relation originale.');

  await configure({ 'Qualification': 'needs' });
  assert.equal((await counts()).edges, 2);
  await configure({ 'Qualification': 'other' });
  assert.equal((await counts()).edges, 1);
  await selectEdgeContaining('QA-RESULT-B-A');
  for (const direction of ['incoming', 'outgoing', 'both']) await configure({ 'Sens de parcours': direction });
  for (const depth of ['2', '3', '0', '1']) await configure({ 'Profondeur': depth });
  await configure({ 'Qualification': 'all', 'Disposition': 'hierarchical', 'Libellés': 'all' });
  assert.ok((await counts()).nodes >= 2);
  checks.push('Filtres de qualification, sens, profondeurs et deux dispositions utilisables sans erreur.');

  await configure({ 'Niveau de lecture': 'domain', 'Profondeur': '0' });
  assert.equal((await counts()).nodes, 2);
  await selectEdgeContaining('QA-NEEDS-A-B');
  assert.ok(await page.locator('[data-relation-id="QA-BEHAVIOR-C"]').count());
  await screenshot('domains-aggregate.png');
  await configure({ 'Niveau de lecture': 'universe' });
  assert.equal((await counts()).nodes, 2);
  await selectEdgeContaining('QA-RESULT-B-A');
  await screenshot('universes-aggregate.png');
  const permalink = page.url();
  await page.reload();
  await settle();
  assert.equal(page.url(), permalink);
  await configure({});
  assert.equal(await pane.getByLabel('Niveau de lecture', { exact: true }).inputValue(), 'universe');
  assert.equal(await pane.getByLabel('Profondeur', { exact: true }).inputValue(), '0');
  checks.push('Domaines et univers : regroupements inspectables, familles et relations originales accessibles.');
  checks.push('Lien direct : niveau Univers et profondeur complète conservés après rechargement.');

  await visit(fixtureVersion, 'QA-EMPTY');
  await configure({ 'Niveau de lecture': 'capability', 'Profondeur': '1', 'Qualification': 'all' });
  assert.equal((await counts()).edges, 0);
  assert.match(await pane.innerText(), /aucun|aucune|0 relation/i);
  checks.push('Capacité isolée : état sans relation utilisable.');

  await visit(fixtureVersion);
  await configure({ 'Niveau de lecture': 'capability', 'Qualification': 'all', 'Disposition': 'organic' });
  await page.setViewportSize({ width: 390, height: 844 });
  await settle();
  await assertNoOverflow();
  await screenshot('mobile-390.png');
  checks.push('Mobile 390 px : canvas et panneau sans débordement horizontal.');

  await page.setViewportSize({ width: 1440, height: 1050 });
  await visit(old.version);
  await configure({ 'Niveau de lecture': 'capability', 'Qualification': 'all', 'Profondeur': '1' });
  assert.ok((await counts()).nodes > 0);
  assert.equal(await page.getByText('Capacité QA focale', { exact: true }).count(), 0);
  await picker().selectOption('node|D07.c');
  await inspector.getByRole('button', { name: 'Ouvrir la fiche', exact: true }).click();
  await page.getByTestId('business-sheet').waitFor();
  assert.equal(new URLSearchParams(new URL(page.url()).hash.slice(1)).get('version'), old.version);
  assert.equal(new URLSearchParams(new URL(page.url()).hash.slice(1)).get('node'), 'D07.c');
  checks.push('Historique v003 : lecture d’une fiche épinglée au même snapshot, sans données de la fixture courante.');

  assert.ok(modelRequests.every(version => served.has(version)), 'Chaque appel modèle est épinglé à une publication connue');
  assert.deepEqual(unexpectedRequests, [], 'Aucun accès externe, backlog ou API imprévue');
  assert.deepEqual(errors, [], 'Aucune erreur JavaScript navigateur');
  const liveServer = liveBase ? await verifyLiveServer(liveBase) : undefined;
  for (const [path, sha] of fileHashes) {
    assert.equal(createHash('sha256').update(await readFile(resolve(root, path))).digest('hex'), sha, `Publication immuable : ${path}`);
  }
  const result = {
    status: 'passed', currentVersion: current.version, historicalVersion: old.version,
    fixtureVersion, fixtureOnly: !liveBase, checks, errors, modelRequests, sourceRequests, liveServer,
    publicationFilesUnchanged: fileHashes.size,
  };
  await writeFile(resolve(output, 'checks.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
} finally {
  await browser.close();
}

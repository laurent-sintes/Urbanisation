import { createRequire } from 'node:module';
import { mkdir, writeFile } from 'node:fs/promises';
import { loadPublication } from '../scripts/load-publication.mjs';
import assert from 'node:assert/strict';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = (process.env.ATLAS_URL || 'http://127.0.0.1:8765').replace(/\/$/, '');
const output = path.join(path.dirname(fileURLToPath(import.meta.url)), '.runtime', 'qa-react');
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const errors = [], consoleErrors = [], failedRequests = [], httpErrors = [], requests = [], checks = [];
let intentionalFailure = false;
let page;
try {
  const context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
  page = await context.newPage();
  page.setDefaultTimeout(30000);
  const monitorPage = observed => {
  observed.on('pageerror', error => errors.push(error.message));
  observed.on('console', message => {
    if (message.type() !== 'error') return;
    const text = message.text();
    if (intentionalFailure && /Failed to load resource.*503/.test(text)) return;
    consoleErrors.push(text);
  });
  observed.on('request', request => requests.push(request.url()));
  observed.on('requestfailed', request => {
    const error = request.failure()?.errorText || '';
    if (!error.includes('ERR_ABORTED')) failedRequests.push({ url: request.url(), error });
  });
  observed.on('response', response => {
    if (response.status() >= 400 && !(intentionalFailure && response.status() === 503 && response.url().includes('/api/model'))) httpErrors.push({ url: response.url(), status: response.status() });
  });
  };
  monitorPage(page);
  const api = await (await context.request.get(base + '/api/model')).json();
  const catalog = await (await context.request.get(base + '/api/releases')).json();
  const disk = await loadPublication();
  const pointer = disk.descriptor;
  assert.equal(api.space, 'release');
  assert.equal(api.version, pointer.version);
  assert.equal(catalog.current_version, pointer.version);
  assert.deepEqual(api.nodes, disk.raw.nodes);
  assert.deepEqual(api.glossary, disk.raw.glossary);
  const nameOf = id => api.nodes.find(node => node.id === id).fields.name;
  const waitHeading = name => page.getByRole('heading', { name, exact: true, level: 1 }).waitFor();
  const waitCards = async ids => {
    await page.waitForFunction(expected => JSON.stringify([...document.querySelectorAll('.business-card[data-node-id]')].map(node => node.dataset.nodeId).sort()) === JSON.stringify([...expected].sort()), ids);
    // The canvas fits after measuring its cards; interact only once its actual transform is stable.
    await page.waitForFunction(() => {
      const viewport = document.querySelector('.react-flow__viewport');
      if (!viewport) return false;
      const signature = JSON.stringify([viewport.getAttribute('style'), ...[...document.querySelectorAll('.business-card')].map(card => {
        const rect = card.getBoundingClientRect();
        return [rect.x, rect.y, rect.width, rect.height];
      })]);
      if (window.__atlasViewportStability?.signature !== signature) {
        window.__atlasViewportStability = { signature, since: performance.now() };
        return false;
      }
      return performance.now() - window.__atlasViewportStability.since >= 160;
    });
  };
  const gotoNode = async (id, view = 'map') => {
    await page.goto(base + '/#' + new URLSearchParams({ node: id, view }));
    await waitHeading(nameOf(id));
  };
  const capture = async name => {
    // Reset the outer scroll so fixed navigation is not drawn halfway down a full-page capture.
    await page.evaluate(() => window.scrollTo({ top: 0, left: 0, behavior: 'instant' }));
    return page.screenshot({ path: path.join(output, name + '.png'), fullPage: true });
  };

  if (!process.argv.includes('--interaction-only')) {
  await page.goto(base);
  await waitHeading('Urbanisation');
  await waitCards(['universe-case', 'universe-supply']);
  assert.ok((await page.locator('.sidebar-bottom').innerText()).includes(`${api.nodes.length} éléments · ${api.nodes.filter(n => n.kind === 'capability').length} capacités`));
  assert.match(await page.locator('#fa-version').innerText(), new RegExp(api.version.replace(/\./g, '\\.')));
  assert.equal(await page.locator('#fa-space').count(), 0);
  assert.equal(await page.getByText(/visites récentes/i).count(), 0);
  await capture('01-urbanisation');
  checks.push(`fresh root / ${api.nodes.length} published elements / no recent visits`);

  await gotoNode('business-references');
  await waitCards(api.relations.filter(relation => relation.type === 'presents' && relation.source_id === 'business-references').map(relation => relation.target_id));
  assert.match(await page.locator('.eyebrow').innerText(), /Groupe de présentation/i);
  for (const domain of api.nodes.filter(node => ['domain', 'reference'].includes(node.kind))) {
    await gotoNode(domain.id, 'map');
    const expected = api.relations.filter(relation => ['contains', 'presents'].includes(relation.type) && relation.source_id === domain.id).map(relation => relation.target_id);
    await waitCards(expected);
    assert.deepEqual(await page.locator('.business-card h3').allTextContents(), expected.map(nameOf), domain.id);
  }
  checks.push('all domain/reference maps match explicit published children');

  for (const space of ['backlog', 'release', 'panorama-as-is']) {
    await page.goto(base + '/#' + new URLSearchParams({ space, node: 'D01', view: 'map' }));
    await waitHeading(nameOf('D01'));
    await waitCards(['D01.f', 'D01.g', 'D01.c', 'D01.d', 'D02.b', 'D02.c']);
    assert.equal(new URL(page.url()).hash.includes('space='), false);
  }
  await page.goto(base + '/#node=transactional');
  await waitHeading('Urbanisation');
  await waitCards(['universe-case', 'universe-supply']);
  checks.push('legacy spaces and navigation shells recover to Urbanisation');
  }

  await page.goto(base + '/#node=D04&scope=missing&view=map');
  await waitHeading(nameOf('D04'));
  const orderChildren = api.relations.filter(relation => ['contains', 'presents'].includes(relation.type) && relation.source_id === 'D04').map(relation => relation.target_id);
  const orderLeaf = api.nodes.find(node => orderChildren.includes(node.id) && node.kind === 'capability'
    && !api.relations.some(relation => ['contains', 'presents'].includes(relation.type) && relation.source_id === node.id));
  assert.ok(orderLeaf, 'The current Order Management map must expose a published capability leaf.');
  await waitCards(orderChildren);
  await page.getByText('Le périmètre de cette carte n’existe pas dans la publication. Le contexte de l’élément est rétabli.', { exact: true }).waitFor();
  assert.equal(new URLSearchParams(new URL(page.url()).hash.slice(1)).has('scope'), false);
  await page.evaluate(leafId => {
    window.__atlasPointerAudit = [];
    for (const type of ['mousedown', 'mouseup', 'click', 'dblclick']) document.addEventListener(type, event => {
      const card = event.target.closest?.('.business-card');
      const leaf = document.querySelector(`.business-card[data-node-id="${leafId}"]`);
      const rect = leaf?.getBoundingClientRect();
      const wrapper = leaf?.closest('.react-flow__node');
      const style = wrapper ? getComputedStyle(wrapper) : undefined;
      window.__atlasPointerAudit.push({ type, detail: event.detail, target: event.target.tagName, targetClass: String(event.target.className), targetHtml: event.target.outerHTML?.slice(0, 500), id: card?.dataset.nodeId, x: event.clientX, y: event.clientY, cardTop: rect?.top, cardLeft: rect?.left, visibility: style?.visibility, pointerEvents: style?.pointerEvents, zIndex: style?.zIndex, viewport: document.querySelector('.react-flow__viewport')?.getAttribute('style'), hash: location.hash });
    }, true);
  }, orderLeaf.id);
  await page.locator(`.business-card[data-node-id="${orderLeaf.id}"] h3`).dblclick();
  await waitHeading(orderLeaf.fields.name);
  await page.getByTestId('business-sheet').waitFor();
  assert.equal(new URLSearchParams(new URL(page.url()).hash.slice(1)).get('view'), 'sheet');
  checks.push('invalid graph scope recovers safely / double-click on a leaf opens its sheet');
  if (process.argv.includes('--interaction-only')) {
    assert.deepEqual(errors, []);
    assert.deepEqual(consoleErrors, []);
    console.log(JSON.stringify({ checks, assets: requests.filter(url => url.includes('/assets/')), pointerAudit: await page.evaluate(() => window.__atlasPointerAudit || []) }));
    await browser.close();
    process.exit(0);
  }

  async function inspectSource(nodeId, sourceId) {
    await gotoNode(nodeId, 'sheet');
    const provenance = page.locator('.sheet-main > details.detail-provenance');
    await provenance.locator('summary').click();
    const trigger = provenance.getByRole('button', { name: sourceId, exact: true }).first();
    await trigger.click();
    const dialog = page.locator('dialog[open]');
    await dialog.locator(`[data-anchor="${sourceId.toLowerCase()}"]`).waitFor();
    assert.match(await dialog.locator('.source-location').innerText(), new RegExp('#' + sourceId.toLowerCase()));
    assert.ok((await dialog.getByTestId('source-document').innerText()).length > 1000);
    await capture('source-' + sourceId.toLowerCase());
    await page.keyboard.press('Escape');
    await page.locator('dialog[open]').waitFor({ state: 'detached' });
    assert.equal(await trigger.evaluate(element => document.activeElement === element), true);
    assert.equal(new URLSearchParams(new URL(page.url()).hash.slice(1)).has('source'), false);
  }
  await inspectSource('D01.f', 'P82');
  assert.ok(api.nodes.find(node => node.id === 'D07.c')?.source_refs.includes('U141'), 'The published reconciliation capability retains source U141.');
  await inspectSource('D07.c', 'U141');
  checks.push('P82 / U141 complete source reader, anchors and Escape focus restoration');

  const search = page.getByRole('textbox', { name: 'Rechercher dans le modèle publié' });
  await search.fill('ILL-OBJ-01');
  await page.getByText('Aucun élément ne correspond dans cette publication.', { exact: true }).waitFor();
  assert.equal(await page.locator('[data-search-result]').count(), 0);
  await search.fill('Inventory');
  await page.locator('#fa-type').selectOption('capability');
  await page.locator('#fa-status').selectOption('urbanist_validated');
  await page.locator('[data-search-result="D01.g"]').waitFor();
  assert.equal(await page.locator('[data-search-result="D01.f"]').count(), 0);
  await page.locator('#fa-status').selectOption(api.nodes.find(node => node.id === 'D01.f').lifecycle.state);
  await page.locator('[data-search-result="D01.f"]').waitFor();
  assert.equal(await page.locator('[data-search-result="D01.g"]').count(), 0);
  await page.getByRole('button', { name: 'Effacer la recherche et les filtres' }).click();
  await search.fill('Order Management');
  await page.locator('[data-search-result="D04"]').click();
  await waitHeading('Order Management');
  await page.reload();
  await waitHeading('Order Management');
  await page.goto(base);
  await waitHeading('Order Management');
  checks.push('published-only search / type and lifecycle filters / persisted current selection');

  await page.goto(base + '/#node=D04&scope=universe-supply&view=map');
  await waitHeading('Supply');
  await waitCards(api.relations.filter(relation => ['contains', 'presents'].includes(relation.type) && relation.source_id === 'universe-supply').map(relation => relation.target_id));
  assert.equal(await page.locator('.view-selection').innerText(), 'Sélection : Order Management');
  await page.goto(base + '/#node=D04&scope=universe-supply&view=map&version=2026-09-13.2');
  await waitHeading('Commercial Commitments');
  const historical = await (await context.request.get(base + '/api/model?version=2026-09-13.2')).json();
  await waitCards(historical.relations.filter(relation => ['contains', 'presents'].includes(relation.type) && relation.source_id === 'D04').map(relation => relation.target_id));
  assert.equal(new URLSearchParams(new URL(page.url()).hash.slice(1)).has('scope'), false);
  assert.match(page.url(), /version=2026-09-13.2/);
  await page.locator('#fa-refresh').click();
  await page.waitForFunction(() => document.querySelector('#fa-main').getAttribute('aria-busy') === 'false');
  await waitHeading('Commercial Commitments');
  assert.equal(new URLSearchParams(new URL(page.url()).hash.slice(1)).get('version'), '2026-09-13.2');
  await page.reload();
  await waitHeading('Commercial Commitments');
  await page.goto(base + '/#node=D04&view=map');
  await waitHeading('Order Management');
  await page.goBack();
  await waitHeading('Commercial Commitments');
  await page.goForward();
  await waitHeading('Order Management');
  checks.push('historical publication fixed across refresh / reload / browser history; missing universe scope recovered');

  const relation = api.relations.find(item => item.type === 'relates-to' && item.source_id === 'D07.c'
    && item.qualification?.meaning && item.qualification?.conditions?.length
    && item.qualification?.effects?.length && item.qualification?.scope);
  assert.ok(relation, 'The published reconciliation relation must retain its complete qualification.');
  await gotoNode(relation.source_id, 'relations');
  await page.waitForFunction(() => document.querySelector('[data-testid="cytoscape-canvas"]')?.getAttribute('data-status') === 'ready');
  await page.getByTestId('cytoscape-canvas').locator('canvas').first().waitFor({ state: 'attached' });
  const dependencyPicker = page.getByLabel('Inspecter un élément', { exact: true });
  for (const id of [relation.source_id, relation.target_id]) {
    assert.ok((await dependencyPicker.locator('option').evaluateAll(options => options.map(option => option.value))).includes(`node|${id}`));
  }
  const relationList = page.locator('.dependency-relations');
  if (!(await relationList.evaluate(element => element.open))) await relationList.locator(':scope > summary').click();
  const relationButton = page.locator(`[data-relation-id="${relation.id}"]`);
  await relationButton.click();
  await page.getByTestId('relation-inspector').waitFor();
  const inspector = await page.getByTestId('relation-inspector').innerText();
  assert.ok(inspector.includes(relation.qualification.meaning));
  assert.ok(inspector.includes(relation.qualification.conditions[0]));
  assert.ok(inspector.includes(relation.qualification.effects[0]));
  assert.ok(inspector.includes(relation.qualification.scope));
  const relationEndpoints = await page.getByTestId('relation-inspector').locator('.relation-endpoints a').evaluateAll(links => links.map(link => link.getAttribute('href')));
  assert.deepEqual(relationEndpoints.map(href => new URLSearchParams(href.split('#')[1]).get('node')), [relation.source_id, relation.target_id]);
  await capture('02-relation-detail');
  checks.push('real transverse relation direction and complete qualification');

  // A browser-only fixture exercises a new publication. No model file is edited.
  await gotoNode('D04');
  const updated = structuredClone(api);
  updated.version = 'browser-fixture-next';
  updated.dataRevision = 'browser-fixture-next';
  updated.nodes.find(node => node.id === 'D04').fields.name = 'Publication suivante · Order Management';
  const updatedCatalog = structuredClone(catalog);
  updatedCatalog.current_version = updated.version;
  updatedCatalog.versions.unshift({ version: updated.version, revision: 999, published_at: '2026-09-14T00:00:00Z', last_modified: '2026-09-14T00:00:00Z' });
  let failUpdatedRead = true;
  const catalogMatcher = url => url.pathname === '/api/releases';
  const modelMatcher = url => url.pathname === '/api/model' && url.searchParams.get('version') === updated.version;
  await page.route(catalogMatcher, route => route.fulfill({ json: updatedCatalog }));
  await page.route(modelMatcher, route => failUpdatedRead ? route.fulfill({ status: 503, json: { error: 'Échec simulé de lecture de la publication suivante' } }) : route.fulfill({ json: updated }));
  intentionalFailure = true;
  await page.getByText(/Actualisation impossible : Échec simulé/).waitFor({ timeout: 13000 });
  await waitHeading('Order Management');
  assert.ok((await page.locator('#fa-version').innerText()).includes(api.version));
  assert.equal(new URLSearchParams(new URL(page.url()).hash.slice(1)).get('node'), 'D04');
  assert.equal(await page.locator('#fa-main').getAttribute('aria-busy'), 'false');
  failUpdatedRead = false;
  await waitHeading(updated.nodes.find(node => node.id === 'D04').fields.name);
  intentionalFailure = false;
  assert.ok((await page.locator('#fa-version').innerText()).includes(updated.version));
  assert.equal(new URLSearchParams(new URL(page.url()).hash.slice(1)).get('node'), 'D04');
  assert.equal(await page.getByText(/Actualisation impossible : Échec simulé/).count(), 0);
  await page.unroute(catalogMatcher);
  await page.unroute(modelMatcher);
  await waitHeading('Order Management');
  assert.ok((await page.locator('#fa-version').innerText()).includes(api.version));
  checks.push('automatic pointer refresh / failure retains model / recovery keeps selected node');

  const historicalPage = await context.newPage();
  monitorPage(historicalPage);
  await historicalPage.goto(base + '/#node=D04&version=2026-09-13.2');
  await historicalPage.getByRole('heading', { name: 'Commercial Commitments', exact: true, level: 1 }).waitFor();
  await historicalPage.route(catalogMatcher, route => route.fulfill({ json: updatedCatalog }));
  await historicalPage.waitForResponse(async response => new URL(response.url()).pathname === '/api/releases' && (await response.json()).current_version === updated.version, { timeout: 12000 });
  await historicalPage.evaluate(() => new Promise(done => requestAnimationFrame(() => requestAnimationFrame(done))));
  assert.equal(await historicalPage.locator('h1').innerText(), 'Commercial Commitments');
  assert.match(historicalPage.url(), /version=2026-09-13.2/);
  await historicalPage.close();
  checks.push('historical selection remains fixed when current catalog advances');

  await gotoNode('D04', 'sheet');
  await capture('03-order-management-sheet');
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), true);
  assert.ok(!requests.some(url => /space=backlog|\/api\/panorama/.test(new URL(url).pathname + new URL(url).search)));
  assert.ok(!requests.some(url => /likec4|8767/.test(url)));
  assert.deepEqual(errors, []);
  assert.deepEqual(consoleErrors, []);
  assert.deepEqual(failedRequests, []);
  assert.deepEqual(httpErrors, []);
  const report = { checkedAt: new Date().toISOString(), checks, version: api.version, assets: [...new Set(requests.filter(url => url.includes('/assets/')))], errors, consoleErrors, failedRequests, httpErrors, screenshots: output };
  await writeFile(path.join(output, 'browser-results.json'), JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify(report));
} catch (error) {
  if (page) {
    await page.screenshot({ path: path.join(output, 'failure.png'), fullPage: true }).catch(() => {});
    await writeFile(path.join(output, 'browser-failure.json'), JSON.stringify({ error: String(error), url: page.url(), checks, errors, consoleErrors, failedRequests, httpErrors, assets: requests.filter(url => url.includes('/assets/')), pointerAudit: await page.evaluate(() => window.__atlasPointerAudit || []) }, null, 2) + '\n');
  }
  throw error;
} finally { await browser.close(); }

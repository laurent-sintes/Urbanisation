import { createRequire } from 'node:module';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = process.env.ATLAS_PROTOTYPE_URL || 'http://127.0.0.1:8767';
const prototypeRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const output = resolve(prototypeRoot, '.runtime/qa');
const manifest = JSON.parse(await readFile(resolve(prototypeRoot, '.generated/likec4-manifest.json'), 'utf8'));
await mkdir(output, { recursive: true });

const browser = await chromium.launch({ channel: 'msedge', headless: true });
const errors = [];
const failedRequests = [];
const httpErrors = [];
const modelRequests = [];
const measurements = [];
const screenshots = [];
let page;
async function capture(name) {
  const path = resolve(output, `${name}.png`);
  await page.screenshot({ path, fullPage: true, animations: 'disabled' });
  screenshots.push(path);
}
async function assertCanvas(engine, { edges = false } = {}) {
  const selector = engine === 'react-flow' ? '[data-testid="react-flow-canvas"]' : '.likec4-pane';
  await page.locator(selector).waitFor();
  // Playwright locators pierce LikeC4's open shadow root; document.querySelector does not.
  await page.locator(`${selector} .react-flow__node`).first().waitFor();
  if (edges) await page.locator(`${selector} .react-flow__edge`).first().waitFor();
  // Both engines schedule fitting after layout. Capture the settled viewport,
  // including delayed fits, rather than the first frame containing nodes.
  const viewport = page.locator(`${selector} .react-flow__viewport`).first();
  let previousTransform = '';
  let unchangedSince = Date.now();
  const deadline = Date.now() + 5000;
  while (Date.now() < deadline) {
    const transform = await viewport.getAttribute('style') || '';
    if (transform !== previousTransform) { previousTransform = transform; unchangedSince = Date.now(); }
    if (Date.now() - unchangedSince >= 250) break;
    await page.waitForTimeout(50);
  }
  assert.equal(await page.getByTestId(`engine-${engine}`).getAttribute('aria-pressed'), 'true');
  const bounds = await page.locator(selector).evaluate(element => ({ width: Math.round(element.getBoundingClientRect().width), height: Math.round(element.getBoundingClientRect().height) }));
  const geometry = { ...bounds, nodes: await page.locator(`${selector} .react-flow__node`).count(), edges: await page.locator(`${selector} .react-flow__edge`).count() };
  assert.ok(geometry.width > 100 && geometry.height > 250, JSON.stringify(geometry));
  return geometry;
}
function hashState() {
  return new URLSearchParams(new URL(page.url()).hash.slice(1));
}
async function heading(name) {
  await page.getByRole('heading', { level: 1, name, exact: true }).waitFor();
}

try {
  page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
  page.on('pageerror', error => errors.push(error.message));
  page.on('requestfailed', request => {
    if (!request.failure()?.errorText?.includes('ERR_ABORTED')) failedRequests.push({ url: request.url(), error: request.failure()?.errorText });
  });
  page.on('console', message => { if (message.type() === 'error') errors.push(`console: ${message.text()} (${message.location().url})`); });
  page.on('response', response => { if (response.status() >= 400) httpErrors.push({ url: response.url(), status: response.status() }); });
  page.on('request', request => { if (new URL(request.url()).pathname === '/api/model') modelRequests.push(request.url()); });
  const response = await page.request.get(`${base}/api/model?version=${encodeURIComponent(manifest.publication)}`);
  assert.equal(response.status(), 200, 'The prototype API proxy must be ready before browser verification');
  const raw = await response.json();
  assert.equal(raw.version, manifest.publication);
  const relation = raw.relations.find(candidate => candidate.id === 'REL-EXECUTION-FACTS-ORDER-RECONCILIATION');
  assert.ok(relation, 'The comparison fixture expects the published Execution/Order relation');
  const names = Object.fromEntries(raw.nodes.map(node => [node.id, node.fields.name]));

  for (const engine of ['react-flow', 'likec4']) {
    await page.goto(`${base}/#node=universe-supply&scope=universe-supply&view=map&engine=${engine}`);
    await page.reload();
    await heading(names['universe-supply']);
    measurements.push({ engine, view: 'supply', ...await assertCanvas(engine) });
    await capture(`${engine}-supply`);
    if (engine === 'likec4') {
      assert.match(await page.locator('.graph-summary-notice').innerText(), /liaison.*résumée.*entre branches/);
    }
    await page.locator('[data-tree-id="D04"]').click();
    await heading(names.D04);
    assert.equal(hashState().get('scope'), 'D04');
    measurements.push({ engine, view: 'domain', ...await assertCanvas(engine) });
    await capture(`${engine}-domain`);
    await page.locator('[data-tree-id="D04.h"]').click();
    await heading(names['D04.h']);
    await page.getByTestId('business-sheet').waitFor();
    assert.equal(await page.getByRole('tab', { name: 'Fiche', exact: true }).getAttribute('aria-selected'), 'true');
    await page.getByRole('tab', { name: /^Relations/ }).click();
    measurements.push({ engine, view: 'relations', ...await assertCanvas(engine, { edges: true }) });
    const inspector = page.getByTestId('relation-inspector');
    assert.ok((await inspector.innerText()).includes(relation.qualification.meaning));
    for (const text of [...relation.qualification.conditions, ...relation.qualification.effects]) assert.ok((await inspector.innerText()).includes(text));
    assert.match(await inspector.locator('.section-kicker').innerText(), /Proposé/);
    await capture(`${engine}-relations`);
    const other = engine === 'react-flow' ? 'likec4' : 'react-flow';
    await page.getByTestId(`engine-${other}`).click();
    await assertCanvas(other, { edges: true });
    await heading(names['D04.h']);
    assert.equal(hashState().get('node'), 'D04.h');
    assert.equal(hashState().get('view'), 'relations');
    await page.getByTestId(`engine-${engine}`).click();
    await assertCanvas(engine, { edges: true });

    // The graph's selection event updates the same business identity as the tree.
    const neighbor = engine === 'react-flow'
      ? page.locator('[data-node-id="D07.c"]')
      : page.locator('.likec4-pane .react-flow__node').filter({ hasText: names['D07.c'] }).first();
    await neighbor.click();
    await heading(names['D07.c']);
    assert.equal(hashState().get('node'), 'D07.c');
    assert.equal(await page.locator('[data-tree-id="D07.c"]').getAttribute('aria-current'), 'page');

    // Provenance opens a real local source and closing restores focus.
    await page.getByTestId('relation-inspector').locator('summary').click();
    const sourceId = relation.source_refs.find(id => raw.sourceReferences?.[id]);
    assert.ok(sourceId, 'Published source locator missing');
    const sourceButton = page.getByTestId('relation-inspector').getByRole('button', { name: sourceId, exact: true });
    await sourceButton.click();
    const dialog = page.getByRole('dialog');
    await dialog.getByRole('heading', { name: sourceId, exact: true }).waitFor();
    await page.waitForFunction(() => {
      const text = document.querySelector('.source-dialog pre')?.textContent;
      return text && !text.startsWith('Chargement');
    });
    assert.doesNotMatch(await dialog.locator('pre').innerText(), /Source indisponible/);
    assert.ok((await dialog.locator('pre').innerText()).length > 30);
    await capture(`${engine}-source`);
    await page.keyboard.press('Escape');
    assert.equal(await sourceButton.evaluate(element => document.activeElement === element), true);

    await page.keyboard.press('Control+k');
    const search = page.getByRole('textbox', { name: 'Rechercher dans le modèle publié' });
    assert.equal(await search.evaluate(element => document.activeElement === element), true);
    await search.fill('D02.b');
    await page.keyboard.press('ArrowDown');
    assert.equal(await page.evaluate(() => document.activeElement?.getAttribute('data-search-result')), 'D02.b');
    await page.keyboard.press('Enter');
    await heading(names['D02.b']);
    assert.equal(await page.locator('[data-tree-id="D02.b"]').getAttribute('aria-current'), 'page');
    assert.match(await page.getByRole('navigation', { name: 'Fil d’Ariane' }).innerText(), new RegExp(names.D01));
    assert.doesNotMatch(await page.locator('body').innerText(), /Visites récentes/);
  }

  for (const engine of ['react-flow', 'likec4']) {
    for (const width of [390, 320]) {
      await page.setViewportSize({ width, height: 844 });
      await page.goto(`${base}/#node=D04.h&scope=D04&view=relations&engine=${engine}`);
      await page.reload();
      await heading(names['D04.h']);
      await assertCanvas(engine, { edges: true });
      const metrics = await page.evaluate(() => ({ width: innerWidth, scrollWidth: document.documentElement.scrollWidth, overflow: document.documentElement.scrollWidth > innerWidth + 1 }));
      assert.equal(metrics.overflow, false, JSON.stringify({ engine, ...metrics }));
      measurements.push({ engine, view: 'mobile-relations', ...metrics });
      await capture(`${engine}-mobile-${width}`);
      await page.keyboard.press('Control+k');
      const search = page.getByRole('textbox', { name: 'Rechercher dans le modèle publié' });
      await search.waitFor({ state: 'visible' });
      assert.equal(await search.evaluate(element => document.activeElement === element), true);
      await search.fill('D04.h');
      await page.keyboard.press('Enter');
      await heading(names['D04.h']);
      await page.getByTestId('business-sheet').waitFor();
      assert.equal(await page.locator('.sidebar').evaluate(element => element.classList.contains('open')), false);
    }
  }
  // A foreign publication must never be silently replaced with the built snapshot.
  await page.setViewportSize({ width: 1440, height: 1000 });
  const requestsBeforeForeignLink = modelRequests.length;
  await page.goto(`${base}/#version=2026-09-13.4&node=D04.h&scope=D04&view=relations&engine=likec4`);
  await page.reload();
  await heading('Publication indisponible');
  assert.equal(hashState().get('version'), '2026-09-13.4');
  assert.equal(modelRequests.length, requestsBeforeForeignLink, 'No model should be fetched for an incompatible initial URL');
  await capture('publication-rejected');
  // Recover through a hash-only link, without a reload or replacement document.
  const documentOrigin = await page.evaluate(() => performance.timeOrigin);
  await page.goto(`${base}/#version=${manifest.publication}&node=D04.h&scope=D04&view=relations&engine=likec4`);
  await heading(names['D04.h']);
  await assertCanvas('likec4', { edges: true });
  assert.equal(await page.evaluate(() => performance.timeOrigin), documentOrigin);
  assert.equal(hashState().get('view'), 'relations');
  assert.equal(await page.locator('[data-tree-id="D04.h"]').getAttribute('aria-current'), 'page');
  await page.goto(`${base}/#version=${manifest.publication}&node=D02.b&scope=D01&view=sheet&engine=react-flow`);
  await heading(names['D02.b']);
  await page.getByTestId('business-sheet').waitFor();
  assert.equal(await page.evaluate(() => performance.timeOrigin), documentOrigin);
  assert.equal(hashState().get('node'), 'D02.b');
  assert.equal(hashState().get('view'), 'sheet');
  assert.equal(await page.getByTestId('engine-react-flow').getAttribute('aria-pressed'), 'true');
  assert.ok(modelRequests.every(url => new URL(url).searchParams.get('version') === manifest.publication));
  assert.deepEqual(errors, []);
  assert.deepEqual(failedRequests, []);
  assert.deepEqual(httpErrors, []);
  const report = { publication: raw.version, checks: ['both-engines', 'tree-to-map-to-sheet', 'qualified-relation', 'engine-selection-continuity', 'graph-to-tree-selection', 'source-and-focus', 'keyboard-search', 'non-prefix-parent', 'no-recent-visits', 'mobile-overflow', 'reject-foreign-publication', 'hash-link-navigation'], measurements, errors, failedRequests, httpErrors, modelRequests, screenshots };
  await writeFile(resolve(output, 'verification.json'), `${JSON.stringify(report, null, 2)}\n`, 'utf8');
  console.log(JSON.stringify(report, null, 2));
} catch (error) {
  if (page) await capture('failure').catch(() => {});
  console.error(JSON.stringify({ errors, failedRequests, httpErrors, measurements }, null, 2));
  throw error;
} finally {
  await browser.close();
}

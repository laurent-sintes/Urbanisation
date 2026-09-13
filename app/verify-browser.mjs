import { createRequire } from 'node:module';
import { mkdir, readFile } from 'node:fs/promises';
import assert from 'node:assert/strict';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = process.env.ATLAS_URL || 'http://127.0.0.1:8765';
const output = path.join(path.dirname(fileURLToPath(import.meta.url)), '.runtime', 'qa-urbanisation');
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
try {
  const context = await browser.newContext({ viewport: { width: 1360, height: 1000 } });
  const page = await context.newPage(); const errors = [], requests = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('request', r => requests.push(r.url()));
  await page.goto(base);
  await page.getByRole('heading', { name: 'Urbanisation', exact: true }).waitFor();
  assert.equal(await page.locator('#fa-space').count(), 0);
  assert.equal(await page.locator('[data-journey="start"]:visible').count(), 0);
  await page.goto(base + '/#node=business-references');
  await page.getByRole('heading', { name: 'Business References', exact: true, level: 1 }).waitFor();
  assert.equal(await page.locator('.fa-grid .fa-tile').count(), 5);
  const api = await (await page.request.get(base + '/api/model')).json();
  const index = JSON.parse(await readFile(new URL('../modeles/release/index.json', import.meta.url), 'utf8'));
  const pointer = JSON.parse(await readFile(new URL('../modeles/release/' + index.current, import.meta.url), 'utf8'));
  assert.equal(api.space, 'release'); assert.equal(api.version, pointer.version);
  assert.ok((await page.locator('#fa-version').innerText()).includes(api.version));
  await page.screenshot({ path: path.join(output, 'urbanisation.png'), fullPage: true });
  for (const domain of api.nodes.filter(n => ['domain', 'reference'].includes(n.kind))) {
    await page.goto(base + '/#node=' + domain.id);
    await page.locator('h1').filter({ hasText: domain.fields.name }).waitFor();
    const ids = api.relations.filter(r => r.type === 'contains' && r.source_id === domain.id).map(r => r.target_id);
    const expected = ids.map(id => api.nodes.find(n => n.id === id).fields.name);
    assert.deepEqual(await page.locator('.fa-grid .fa-tile-name').allTextContents(), expected, domain.id);
  }
  for (const oldSpace of ['backlog', 'release', 'panorama-as-is']) {
    await page.goto(base + '/#space=' + oldSpace + '&node=D01');
    await page.locator('.fa-grid [data-go="D01.f"]').waitFor();
    assert.equal(new URL(page.url()).hash.includes('space='), false);
    assert.equal(await page.locator('.fa-grid .fa-tile').count(), 6);
  }
  await page.locator('.fa-grid [data-go="D01.f"]').click();
  await page.locator('[data-proof]').click();
  await page.locator('.fa-source button').filter({ hasText: /^P82$/ }).click();
  await page.locator('#fa-source-dialog').getByRole('heading', { name: 'P82', exact: true }).waitFor();
  await page.locator('#fa-close-source').click();
  await page.locator('#fa-search').fill('Order Management');
  await page.locator('.fa-result[data-go="D04"]').click();
  await page.reload();
  await page.getByRole('heading', { name: 'Order Management', exact: true }).first().waitFor();
  await page.locator('#fa-publication').selectOption('2026-09-13.2');
  await page.getByRole('heading', { name: 'Commercial Commitments', exact: true }).first().waitFor();
  await page.locator('#fa-refresh').click();
  await page.getByRole('heading', { name: 'Commercial Commitments', exact: true }).first().waitFor();
  assert.match(page.url(), /version=2026-09-13.2/);
  await page.locator('#fa-publication').selectOption('');
  await page.getByRole('heading', { name: 'Order Management', exact: true }).first().waitFor();
  // Simulate another publication over HTTP without editing frozen project files.
  const updated = structuredClone(api);
  updated.version = 'publication-test'; updated.dataRevision = 'publication-test';
  updated.nodes.find(n => n.id === 'D04').fields.name = 'Updated publication';
  await page.route('**/api/model', route => route.fulfill({ json: updated }));
  await page.route('**/api/status', route => route.fulfill({ json: { revision: updated.dataRevision, space: 'release' } }));
  await page.getByRole('heading', { name: 'Updated publication', exact: true }).first().waitFor({ timeout: 12000 });
  assert.ok((await page.locator('#fa-version').innerText()).includes(updated.version));
  assert.match(page.url(), /node=D04/);
  await page.unroute('**/api/model'); await page.unroute('**/api/status');
  await page.getByRole('heading', { name: 'Order Management', exact: true }).first().waitFor({ timeout: 12000 });
  await page.goto(base + '/#node=D01');
  await page.locator('.fa-grid [data-go="D01.f"]').waitFor();
  for (const width of [1360, 768, 375]) {
    await page.setViewportSize({ width, height: 1000 });
    await page.screenshot({ path: path.join(output, `d01-${width}.png`), fullPage: true });
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1));
  }
  assert.ok(!requests.some(url => /space=backlog|\/api\/panorama/.test(url) && !url.includes('#')));
  // Preview the next lifecycle-enabled publication without modifying release.
  const backlog = JSON.parse(await readFile(new URL('../modeles/backlog/model.json', import.meta.url), 'utf8'));
  const preview = structuredClone(api);
  preview.dataRevision = 'lifecycle-preview';
  for (const node of preview.nodes) {
    const lifecycle = backlog.nodes.find(candidate => candidate.id === node.id)?.lifecycle;
    if (lifecycle) node.lifecycle = structuredClone(lifecycle);
  }
  await page.route('**/api/model', route => route.fulfill({ json: preview }));
  await page.route('**/api/status', route => route.fulfill({ json: { revision: preview.dataRevision, space: 'release' } }));
  await page.setViewportSize({ width: 1360, height: 1000 });
  await page.goto(base + '/#node=D01.g');
  await page.getByRole('heading', { name: 'Record Inventory Movements', exact: true }).first().waitFor();
  await page.locator('.fa-validation-summary .fa-badge').filter({ hasText: 'Validé par l’urbaniste' }).waitFor({ timeout: 12000 });
  const validatedCount = preview.nodes.filter(n => n.kind === 'capability' && n.lifecycle?.state === 'urbanist_validated').length;
  assert.ok((await page.locator('#fa-announcement').innerText()).includes(`${validatedCount} validées par l’urbaniste`));
  assert.ok((await page.locator('.fa-validation-summary').innerText()).includes('Validé par l’urbaniste'));
  await page.locator('[data-proof]').click();
  assert.ok((await page.locator('.fa-provenance').innerText()).includes('Portée validée : Libellé'));
  await page.screenshot({ path: path.join(output, 'lifecycle.png'), fullPage: true });
  await page.locator('#fa-search').fill('Inventory');
  await page.locator('#fa-status').selectOption('urbanist_validated');
  assert.equal(await page.locator('.fa-result[data-go="D01.g"]').count(), 1);
  assert.equal(await page.locator('.fa-result[data-go="D01.f"]').count(), 0);
  await page.locator('#fa-status').selectOption('under_instruction');
  assert.equal(await page.locator('.fa-result[data-go="D01.f"]').count(), 1);
  assert.deepEqual(errors, []);
  console.log(JSON.stringify({ checks: 'release-only/all-domains/legacy-links/source/search/automatic-refresh/mobile', version: api.version, errors, screenshots: output }));
} finally { await browser.close(); }

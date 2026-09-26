import { staticModelUrl } from './static-test-helpers.mjs';
// Browser-only candidate fixture. Never publishes or changes Atlas API data.
import { createRequire } from 'node:module';
import { execFileSync } from 'node:child_process';
import { mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root = fileURLToPath(new URL('../', import.meta.url));
const fixture = JSON.parse(execFileSync(process.env.ATLAS_PYTHON || 'python', ['-c',
  "import sys,json;sys.path.insert(0,'scripts');from structured_io import read;m=read('modeles/backlog/model.yaml');m['glossary']=read('modeles/backlog/glossary.yaml');print(json.dumps(m,ensure_ascii=True))"
], { cwd: root, encoding: 'utf8' }));
fixture.space = 'release'; fixture.version = '2099-01-01.1'; fixture.revision = 0;
fixture.nodes = fixture.nodes.filter(n => n.review.state !== 'illustration');
const nodeIds = new Set(fixture.nodes.map(n => n.id));
fixture.relations = fixture.relations.filter(r => r.review.state !== 'illustration' && nodeIds.has(r.source_id) && nodeIds.has(r.target_id));
for (const node of fixture.nodes) {
  node.approved_fields = node.lifecycle?.validated_fields ?? [];
  node.proposed_fields = Object.keys(node.fields).filter(key => !node.approved_fields.includes(key));
}
const children = parent => {
  const ids = new Set(fixture.relations.filter(r => r.type === 'contains' && r.source_id === parent).map(r => r.target_id));
  return fixture.nodes.filter(n => n.kind === 'behavior' && ids.has(n.id));
};
const behaviors = children('D03.i');
assert.equal(behaviors.length, 4);
const planningBehaviors = children('D05.f');
assert.equal(planningBehaviors.length, 6);
const base = process.env.ATLAS_URL || 'http://127.0.0.1:8765';
const output = new URL('../audits/2026-09-17-scenario-impact/browser/', import.meta.url);
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const errors = [], checks = [];
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
  page.setDefaultTimeout(15000);
  page.on('pageerror', error => errors.push(error.message));
  const published = await (await page.request.get(await staticModelUrl(base))).json();
  const catalog = await (await page.request.get(base + '/data/index.json')).json();
  await page.route('**/data/index.json', route => route.fulfill({ json: { ...catalog,
    versions: [{ version: fixture.version, revision: 0 }, ...catalog.versions] } }));
  await page.route('**/data/*/model.json', route => new URL(route.request().url()).pathname.split('/').at(-2) === fixture.version
    ? route.fulfill({ json: fixture }) : route.continue());
  const visit = async (node, view = 'sheet') => {
    await page.goto(base + '/#' + new URLSearchParams({ version: fixture.version, node, view }));
    await page.getByRole('heading', { level: 1, name: fixture.nodes.find(n => n.id === node).fields.name, exact: true }).waitFor();
  };
  await visit('D03.i');
  assert.equal(await page.locator('.behavior-summary').count(), 4);
  for (const node of behaviors) {
    const summary = page.locator(`[data-behavior-id="${node.id}"]`);
    assert.ok((await summary.innerText()).includes(node.fields.definition));
    const link = summary.getByRole('link');
    const params = new URLSearchParams(new URL(await link.getAttribute('href'), base).hash.slice(1));
    assert.equal(params.get('node'), node.id); assert.equal(params.get('version'), fixture.version);
  }
  await page.screenshot({ path: fileURLToPath(new URL('atp-sheet-desktop.png', output)), fullPage: true });
  checks.push('Candidate fixture: four exact adopted definitions, separate behavior labels and version-pinned links.');
  await page.locator('[data-behavior-id="BHV003"] a').click();
  await page.getByRole('heading', { level: 1, name: behaviors[2].fields.name, exact: true }).waitFor();
  await page.getByText('Dernier niveau de détail', { exact: false }).waitFor();
  assert.equal(await page.locator('[data-tree-id="BHV003"]').getAttribute('aria-selected'), 'true');
  assert.equal(await page.locator('[data-tree-id="BHV003"]').getAttribute('aria-expanded'), null);
  const parentLink = page.locator('.behavior-context a');
  await parentLink.focus(); await page.keyboard.press('Enter');
  await page.getByRole('heading', { level: 1, name: 'Available-to-Promise (ATP)', exact: true }).waitFor();
  await page.keyboard.press('Escape');
  await page.locator('[data-tree-id="D03.i"]').focus();
  await page.keyboard.press('ArrowRight');
  assert.equal(await page.evaluate(() => document.activeElement?.getAttribute('data-tree-id')), 'BHV001');
  await page.keyboard.press('Enter');
  checks.push('Behavior is terminal in the tree, keyboard navigation works and parent link returns to ATP.');
  const search = page.getByRole('textbox', { name: 'Rechercher dans le modèle publié' });
  await search.fill('ATP mobilisation');
  await page.getByLabel('Type d’élément', { exact: true }).selectOption('behavior');
  assert.ok(await page.locator('[data-search-result="BHV003"]').count());
  assert.equal(await page.locator('[data-search-result="D03.i"]').count(), 0);
  await page.locator('[data-search-result="BHV003"]').click();
  await page.getByRole('heading', { level: 1, name: behaviors[2].fields.name, exact: true }).waitFor();
  checks.push('Direct search combines ATP ancestry, French description and the Comportement filter.');
  await visit('D03', 'map');
  await page.locator('.business-card[data-node-id="D03.i"] .behavior-link').first().waitFor();
  assert.equal(await page.locator('.business-card[data-node-id="D03.i"] .behavior-link').count(), 4);
  await page.screenshot({ path: fileURLToPath(new URL('domain-map.png', output)), fullPage: true });
  await page.locator('.business-card[data-node-id="D03.i"] .behavior-link').first().click();
  await page.getByRole('heading', { level: 1, name: behaviors[0].fields.name, exact: true }).waitFor();
  await visit('D03.i', 'map');
  await page.locator('.business-card[data-node-id="BHV004"]').waitFor();
  assert.equal(await page.locator('.business-card').count(), 4);
  checks.push('Domain card exposes four behavior links; ATP map displays the four actual child nodes.');
  await page.setViewportSize({ width: 390, height: 844 });
  await visit('D03.i');
  assert.equal(await page.locator('.behavior-summary').count(), 4);
  assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
  await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
  await page.screenshot({ path: fileURLToPath(new URL('atp-sheet-mobile.png', output)), fullPage: true });
  await page.locator('[data-behavior-id="BHV004"] a').click();
  await page.getByRole('heading', { level: 1, name: behaviors[3].fields.name, exact: true }).waitFor();
  await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
  await page.screenshot({ path: fileURLToPath(new URL('behavior-mobile.png', output)), fullPage: true });
  checks.push('Mobile 390px: readable content, direct navigation and no horizontal overflow.');
  await page.setViewportSize({ width: 1440, height: 1000 });
  await visit('D05.f');
  assert.equal(await page.locator('.behavior-summary').count(), 6);
  await page.getByRole('heading', { name: 'Pourquoi décomposer cette capacité', exact: true }).waitFor();
  for (const node of planningBehaviors) {
    const summary = page.locator(`[data-behavior-id="${node.id}"]`);
    assert.ok((await summary.innerText()).includes(node.fields.definition));
  }
  await page.screenshot({ path: fileURLToPath(new URL('planning-sheet-desktop.png', output)), fullPage: true });
  await page.locator('[data-behavior-id="BHV009"] a').click();
  await page.getByRole('heading', { level: 1, name: 'Scenario Application', exact: true }).waitFor();
  assert.equal(await page.locator('[data-tree-id="BHV009"]').getAttribute('aria-selected'), 'true');
  assert.equal(await page.locator('[data-tree-id="BHV009"]').getAttribute('aria-expanded'), null);
  await page.locator('.behavior-context a').click();
  await page.getByRole('heading', { level: 1, name: 'Inventory Planning', exact: true }).waitFor();
  await visit('D05', 'map');
  assert.equal(await page.locator('.business-card[data-node-id="D05.f"] .behavior-link').count(), 6);
  for (const id of ['D05.a', 'D05.d', 'D05.e', 'D05.c']) {
    assert.equal(await page.locator(`.business-card[data-node-id="${id}"]`).count(), 1);
  }
  await page.setViewportSize({ width: 390, height: 844 });
  await visit('D05.f');
  assert.equal(await page.locator('.behavior-summary').count(), 6);
  assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
  await page.screenshot({ path: fileURLToPath(new URL('planning-sheet-mobile.png', output)), fullPage: true });
  checks.push('Planning has six adopted descriptions including impact analysis, visible justification, terminal application navigation and four separate domain decisions; mobile has no overflow.');
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.goto(base + '/#' + new URLSearchParams({ version: published.version, node: 'D03.i', view: 'sheet' }));
  await page.getByRole('heading', { level: 1, name: 'Available-to-Promise (ATP)', exact: true }).waitFor();
  assert.equal(await page.locator('.behavior-summary').count(), 0);
  assert.equal(await page.locator('[data-tree-id="BHV001"]').count(), 0);
  assert.equal((await (await page.request.get(await staticModelUrl(base))).json()).version, published.version);
  checks.push('Actual publication remains unchanged and receives no behavior from the backlog.');
  assert.deepEqual(errors, []);
  await writeFile(new URL('results.json', output), JSON.stringify({ fixtureOnly: true, publishedVersion: published.version, checks, errors }, null, 2));
  console.log(JSON.stringify({ checks, errors }, null, 2));
} finally { await browser.close(); }

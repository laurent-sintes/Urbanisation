import { createRequire } from 'node:module';
import { mkdir, writeFile } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = process.env.ATLAS_URL || 'http://127.0.0.1:8765';
const output = new URL('./.runtime/qa-capability-types/', import.meta.url);
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const errors = [], checks = [];
try {
  const page = await browser.newPage({ viewport: { width: 1500, height: 1050 }, reducedMotion: 'reduce' });
  page.setDefaultTimeout(15000);
  page.on('pageerror', error => errors.push(error.message));
  const model = await (await page.request.get(base + '/api/model')).json();
  const lookup = new Map(model.nodes.map(n => [n.id, n]));
  const hasAreas = model.nodes.some(n => n.kind === 'area');
  const domains = model.nodes.filter(n => n.kind === (hasAreas ? 'area' : 'domain'));
  const isDecision = n => n.kind === 'capability' && n.fields.nature === 'decision';
  const children = id => {
    const list = model.relations.filter(r => r.source_id === id && r.type === 'contains').map(r => lookup.get(r.target_id));
    return [...list.filter(n => !isDecision(n)), ...list.filter(isDecision)];
  };
  const ids = list => list.map(n => n.id);
  const linkedIds = locator => locator.evaluateAll(links => links.map(link => new URLSearchParams(new URL(link.href).hash.slice(1)).get('node')));
  const mixed = list => list.some(isDecision) && list.some(n => !isDecision(n));
  await page.goto(base + '/#node=universe-supply&view=map&scope=universe-supply');
  await page.locator('.business-card[data-node-id="D06"]').waitFor();
  for (const domain of domains) {
    const expected = children(domain.id);
    const card = page.locator(`.business-card[data-node-id="${domain.id}"]`);
    assert.deepEqual(await linkedIds(card.locator('.capacity-link')), ids(expected));
    assert.equal(await card.locator('.decision-section-start').count(), Number(mixed(expected)));
  }
  checks.push(`All ${domains.length} ${hasAreas ? 'area' : 'domain'} lists: stable ordering and exactly one separator only in mixed lists.`);
  const expectedIcons = { action: 'lucide-zap', management: 'lucide-sliders-horizontal', knowledge: 'lucide-eye', orchestration: 'lucide-workflow', planning: 'lucide-calendar-check', decision: 'lucide-git-branch' };
  for (const [type, cssClass] of Object.entries(expectedIcons)) {
    const icons = page.locator(`.card-child-list [data-capability-type="${type}"] svg`);
    assert.ok(await icons.count() > 0, type);
    for (const icon of await icons.all()) assert.ok((await icon.getAttribute('class')).includes(cssClass), type);
  }
  checks.push('All six types use their dedicated icon, including ATP and Order Prioritization.');
  const untyped = model.nodes.filter(n => n.kind === 'capability' && !n.fields.nature);
  for (const node of untyped) {
    const icon = page.locator(`.capacity-link[href*="node=${node.id}"] .node-icon svg`).first();
    // Reference ingestion capabilities are inside another map, outside this universe list.
    if (await icon.count()) assert.ok((await icon.getAttribute('class')).includes('lucide-box'));
  }
  checks.push('Historical missing types keep a neutral icon and never become inferred orchestration.');
  await page.screenshot({ path: fileURLToPath(new URL('universe.png', output)), fullPage: true });
  await page.goto(base + '/#node=D06&view=sheet');
  await page.locator('.business-sheet').waitFor();
  const expected = children('D06');
  assert.deepEqual(await linkedIds(page.locator('.detail-children-list > a')), ids(expected));
  assert.equal(await page.locator('.detail-children-list > .decision-divider').count(), 1);
  const branch = page.locator('[data-tree-id="D06"] > ul');
  assert.deepEqual(await branch.locator(':scope > [data-tree-id]').evaluateAll(items => items.map(item => item.dataset.treeId)), ids(expected));
  assert.equal(await branch.locator(':scope > .decision-section-start').count(), 1);
  const firstDecision = branch.locator(':scope > .decision-section-start');
  assert.equal(await firstDecision.evaluate(el => getComputedStyle(el).borderTopWidth), '1px');
  await firstDecision.focus();
  await page.keyboard.press('ArrowDown');
  assert.equal(await page.locator(':focus').getAttribute('data-tree-id'), expected[expected.findIndex(isDecision) + 1].id);
  checks.push('Sheet and tree: matching order, light border and keyboard traversal.');
  await page.goto(base + '/#node=D06&view=map&scope=D06');
  await page.locator('.map-decision-divider').waitFor();
  const cardPositions = await page.locator('.business-card').evaluateAll(cards => cards.map(card => ({ id: card.dataset.nodeId, y: card.getBoundingClientRect().top, bottom: card.getBoundingClientRect().bottom })));
  const nonDecisions = cardPositions.filter(card => !isDecision(lookup.get(card.id)));
  const decisions = cardPositions.filter(card => isDecision(lookup.get(card.id)));
  assert.ok(Math.min(...decisions.map(card => card.y)) > Math.max(...nonDecisions.map(card => card.bottom)));
  assert.equal(await page.locator('.map-decision-divider').count(), 1);
  await page.screenshot({ path: fileURLToPath(new URL('domain.png', output)), fullPage: true });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(base + '/#node=D06&view=sheet');
  await page.locator('.business-sheet').waitFor();
  assert.equal(await page.locator('.decision-divider').count(), 1);
  assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
  checks.push('Domain map: decisions start a separate row after the line; mobile sheet fits viewport.');
  assert.deepEqual(errors, []);
  await writeFile(new URL('verification.json', output), JSON.stringify({ version: model.version, checks, errors }, null, 2));
  console.log(JSON.stringify({ version: model.version, checks, errors }, null, 2));
} finally { await browser.close(); }

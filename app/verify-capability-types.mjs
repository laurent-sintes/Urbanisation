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
  const types = ['action', 'management', 'knowledge', 'orchestration', 'planning', 'policy', 'decision'];
  const nature = n => n.kind === 'capability' && types.includes(n.fields.nature) ? n.fields.nature : undefined;
  const rank = n => n.kind !== 'capability' ? -1 : nature(n) ? types.indexOf(nature(n)) : types.length;
  const children = id => {
    const list = model.relations.filter(r => r.source_id === id && r.type === 'contains').map(r => lookup.get(r.target_id));
    return [...list].sort((a, b) => rank(a) - rank(b));
  };
  const ids = list => list.map(n => n.id);
  const linkedIds = locator => locator.evaluateAll(links => links.map(link => new URLSearchParams(new URL(link.href).hash.slice(1)).get('node')));
  const boundaries = list => list.flatMap((n, i) => i > 0 && n.kind === 'capability' && list[i - 1].kind === 'capability' && nature(n) !== nature(list[i - 1]) ? [i] : []);
  await page.goto(base + '/#node=universe-supply&view=map&scope=universe-supply');
  await page.locator('.business-card[data-node-id="D06"]').waitFor();
  for (const domain of domains) {
    const expected = children(domain.id);
    const card = page.locator(`.business-card[data-node-id="${domain.id}"]`);
    assert.deepEqual(await linkedIds(card.locator('.capacity-link')), ids(expected));
    assert.equal(await card.locator('.capability-type-section-start').count(), boundaries(expected).length);
  }
  checks.push(`All ${domains.length} ${hasAreas ? 'area' : 'domain'} lists: stable ordering and a separator at each type boundary.`);
  const expectedIcons = { action: 'lucide-zap', management: 'lucide-sliders-horizontal', knowledge: 'lucide-eye', orchestration: 'lucide-workflow', planning: 'lucide-calendar-check', policy: 'lucide-shield-check', decision: 'lucide-git-branch' };
  for (const [type, cssClass] of Object.entries(expectedIcons)) {
    const icons = page.locator(`.card-child-list [data-capability-type="${type}"] svg`);
    // Historical publications may not contain every type.
    if (!model.nodes.some(n => nature(n) === type)) continue;
    for (const icon of await icons.all()) assert.ok((await icon.getAttribute('class')).includes(cssClass), type);
  }
  checks.push('Published types use their dedicated icon.');
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
  assert.equal(await page.locator('.detail-children-list > .capability-type-divider').count(), boundaries(expected).length);
  const branch = page.locator('[data-tree-id="D06"] > ul');
  assert.deepEqual(await branch.locator(':scope > [data-tree-id]').evaluateAll(items => items.map(item => item.dataset.treeId)), ids(expected));
  assert.equal(await branch.locator(':scope > .capability-type-section-start').count(), boundaries(expected).length);
  const firstDecision = branch.locator(':scope > .capability-type-section-start').first();
  assert.equal(await firstDecision.evaluate(el => getComputedStyle(el).borderTopWidth), '1px');
  await firstDecision.focus();
  await page.keyboard.press('ArrowDown');
  assert.equal(await page.locator(':focus').getAttribute('data-tree-id'), expected[boundaries(expected)[0] + 1].id);
  checks.push('Sheet and tree: matching order, light border and keyboard traversal.');
  await page.goto(base + '/#node=D06&view=map&scope=D06');
  await page.locator('.map-capability-type-divider').waitFor();
  const cardPositions = await page.locator('.business-card').evaluateAll(cards => cards.map(card => ({ id: card.dataset.nodeId, y: card.getBoundingClientRect().top, bottom: card.getBoundingClientRect().bottom })));
  for (const boundary of boundaries(expected)) {
    const preceding = expected.slice(0, boundary).map(n => n.id);
    const following = expected.slice(boundary).map(n => n.id);
    assert.ok(Math.min(...cardPositions.filter(c => following.includes(c.id)).map(c => c.y)) > Math.max(...cardPositions.filter(c => preceding.includes(c.id)).map(c => c.bottom)));
  }
  assert.equal(await page.locator('.map-capability-type-divider').count(), boundaries(expected).length);
  await page.screenshot({ path: fileURLToPath(new URL('domain.png', output)), fullPage: true });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(base + '/#node=D06&view=sheet');
  await page.locator('.business-sheet').waitFor();
  assert.equal(await page.locator('.capability-type-divider').count(), boundaries(expected).length);
  assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
  checks.push('Domain map: each type starts a separate row after the line; mobile sheet fits viewport.');
  assert.deepEqual(errors, []);
  await writeFile(new URL('verification.json', output), JSON.stringify({ version: model.version, checks, errors }, null, 2));
  console.log(JSON.stringify({ version: model.version, checks, errors }, null, 2));
} finally { await browser.close(); }

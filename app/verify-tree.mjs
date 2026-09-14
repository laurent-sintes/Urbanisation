import { createRequire } from 'node:module';
import { mkdir, writeFile } from 'node:fs/promises';
import assert from 'node:assert/strict';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = process.env.ATLAS_URL || 'http://127.0.0.1:8765';
const output = path.join(path.dirname(fileURLToPath(import.meta.url)), '.runtime', 'qa-tree');
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const checks = [], failures = [], measurements = [], browserErrors = [];
try {
  const page = await browser.newPage({ viewport: { width: 1366, height: 900 } });
  page.setDefaultTimeout(10000);
  page.on('pageerror', error => browserErrors.push(error.message));
  const item = id => page.locator(`[role="treeitem"][data-tree-id="${id}"]`);
  const heading = name => page.getByRole('heading', { name, exact: true, level: 1 });
  const activeTreeId = () => page.evaluate(() => document.activeElement?.getAttribute('data-tree-id'));
  const visit = async (id, name, extra = '') => {
    await page.goto(`${base}/#node=${encodeURIComponent(id)}${extra}`);
    await heading(name).waitFor();
    await page.locator('.business-sheet, .react-flow').first().waitFor();
  };
  const check = async (name, operation) => {
    try { await operation(); checks.push(name); console.log(`PASS ${name}`); }
    catch (error) {
      failures.push({ name, error: error.message });
      console.error(`FAIL ${name}: ${error.message}`);
      await page.screenshot({ path: path.join(output, `failure-${failures.length}.png`) }).catch(() => {});
    }
  };

  const status = await (await page.request.get(`${base}/api/status`)).json();
  assert.equal(status.appName, 'FLOW Atlas');
  const api = await (await page.request.get(`${base}/api/model`)).json();
  assert.equal(api.space, 'release');

  await check('Explicit parents, selection and no recent visits', async () => {
    await visit('D02.b', 'Supply Protection');
    assert.equal(await page.locator('#fa-recent, [data-recent], .recent-visits').count(), 0);
    assert.doesNotMatch(await page.locator('.sidebar').innerText(), /visites récentes|récemment exploré/i);
    assert.equal(await item('D01').getAttribute('aria-expanded'), 'true');
    assert.equal(await item('D02.b').getAttribute('aria-selected'), 'true');
    assert.equal(await item('D01').locator('[data-tree-id="D02.b"]').count(), 1);
    assert.equal(await item('process').count(), 0);
    assert.equal(await item('transactional').count(), 0);
    assert.equal(await item('universe-case').count(), 1);
    assert.equal(await item('universe-supply').count(), 1);
  });

  await check('Tree keyboard, expansion and selection stay distinct', async () => {
    await visit('D02.b', 'Supply Protection');
    if (await item('D03').getAttribute('aria-expanded') !== 'true') await page.locator('[data-tree-toggle="D03"]').click();
    await heading('Supply Protection').waitFor();
    await item('D02.e').focus();
    await page.keyboard.press('Enter');
    await heading('Supply Assignment').waitFor();
    assert.equal(await item('D03').locator('[data-tree-id="D02.e"]').count(), 1);
    assert.equal(await activeTreeId(), 'D02.e');
    await page.keyboard.press('ArrowLeft');
    assert.equal(await activeTreeId(), 'D03');
    await page.keyboard.press('ArrowLeft');
    assert.equal(await item('D03').getAttribute('aria-expanded'), 'false');
    await page.keyboard.press('ArrowRight');
    await page.keyboard.press('ArrowRight');
    assert.equal(await activeTreeId(), 'D03.a');
    await page.keyboard.press('ArrowDown');
    assert.notEqual(await activeTreeId(), 'D03.a');
    await page.keyboard.press('ArrowUp');
    assert.equal(await activeTreeId(), 'D03.a');
    const visible = await page.locator('[role="treeitem"]').evaluateAll(elements => elements.map(element => element.dataset.treeId));
    await page.keyboard.press('Home'); assert.equal(await activeTreeId(), visible[0]);
    await page.keyboard.press('End'); assert.equal(await activeTreeId(), visible.at(-1));
    assert.equal(await page.locator('[role="treeitem"][tabindex="0"]').count(), 1);
  });

  await check('Mouse collapse keeps a keyboard entry for the hidden selected leaf', async () => {
    await visit('D02.e', 'Supply Assignment');
    await item('D02.e').focus();
    await page.locator('[data-tree-toggle="D03"]').click();
    assert.equal(await item('D03').getAttribute('aria-expanded'), 'false');
    assert.equal(await item('D02.e').count(), 0);
    await heading('Supply Assignment').waitFor();
    const tabStop = page.locator('[role="treeitem"][tabindex="0"]');
    assert.equal(await tabStop.count(), 1);
    assert.equal(await tabStop.getAttribute('data-tree-id'), 'D03');
    // Entering the tree by Tab must still work after collapsing its selected branch.
    await page.locator('#fa-status').focus(); await page.keyboard.press('Tab');
    assert.equal(await activeTreeId(), 'D03');
    await page.keyboard.press('ArrowRight'); await page.keyboard.press('ArrowRight');
    assert.equal(await activeTreeId(), 'D03.a');
    await heading('Supply Assignment').waitFor();
  });

  await check('Expansion persists and search reveals the selected ancestors', async () => {
    await visit('D02.e', 'Supply Assignment');
    if (await item('business-references').getAttribute('aria-expanded') !== 'true') await page.locator('[data-tree-toggle="business-references"]').click();
    await page.reload(); await heading('Supply Assignment').waitFor();
    assert.equal(await item('business-references').getAttribute('aria-expanded'), 'true');
    await page.locator('#fa-search').fill('D01.g');
    await page.keyboard.press('ArrowDown');
    assert.equal(await page.evaluate(() => document.activeElement?.getAttribute('data-search-result')), 'D01.g');
    await page.keyboard.press('Enter'); await heading('Record Inventory Movements').waitFor();
    await page.waitForFunction(() => document.activeElement?.tagName === 'H1');
    assert.equal(await item('D01.g').getAttribute('aria-selected'), 'true');
    assert.equal(await item('D01').getAttribute('aria-expanded'), 'true');
    const readingWidth = await page.locator('.business-sheet .business-copy').first().evaluate(element => element.getBoundingClientRect().width);
    assert.ok(readingWidth > 600, `Central reading width: ${readingWidth}px`);
    await page.screenshot({ path: path.join(output, 'central-sheet.png') });
  });

  await check('Published validation scope and source focus restoration', async () => {
    await visit('D01.g', 'Record Inventory Movements', '&view=sheet');
    const proof = page.locator('.sheet-main > .detail-provenance');
    assert.equal(await proof.getAttribute('open'), null);
    await proof.locator('summary').click();
    assert.match(await proof.innerText(), /Champs adoptés : Libellé\./);
    assert.match(await proof.innerText(), /Champs proposés :.*Définition.*Finalité|Champs proposés :.*Finalité.*Définition/);
    assert.match(await proof.innerText(), /Champs validés dans le cycle : Libellé\./);
    const source = proof.getByRole('button', { name: 'U129', exact: true }).first();
    await source.click();
    const dialog = page.locator('.source-dialog');
    await dialog.locator('[data-anchor="u129"]').waitFor();
    assert.equal(await dialog.evaluate(element => element.open), true);
    assert.equal(await page.evaluate(() => document.activeElement?.getAttribute('data-anchor')), 'u129');
    assert.ok(await dialog.locator('[data-line]').count() > 100, 'The complete document is retained, beyond the selected contribution.');
    await dialog.getByRole('textbox', { name: 'Rechercher dans la source' }).fill('Record Inventory Movements');
    await dialog.locator('mark').first().waitFor();
    await page.keyboard.press('Escape');
    await dialog.waitFor({ state: 'hidden' });
    assert.equal(await source.evaluate(element => element === document.activeElement), true);
  });

  await check('Resizable tree clamps to 240–420px and persists', async () => {
    await visit('D01', 'Inventory Management');
    const separator = page.getByRole('separator', { name: 'Largeur de l’arbre' });
    await separator.focus(); await page.keyboard.press('End');
    assert.equal(await separator.getAttribute('aria-valuenow'), '420');
    assert.equal(await page.locator('.sidebar').evaluate(element => element.getBoundingClientRect().width), 420);
    await page.keyboard.press('ArrowRight'); assert.equal(await separator.getAttribute('aria-valuenow'), '420');
    await page.keyboard.press('Home'); assert.equal(await separator.getAttribute('aria-valuenow'), '240');
    assert.equal(await page.locator('.sidebar').evaluate(element => element.getBoundingClientRect().width), 240);
    await page.keyboard.press('ArrowLeft'); assert.equal(await separator.getAttribute('aria-valuenow'), '240');
    for (let i = 0; i < 6; i++) await page.keyboard.press('ArrowRight');
    await page.reload(); await heading('Inventory Management').waitFor();
    assert.equal(await separator.getAttribute('aria-valuenow'), '300');
    await page.screenshot({ path: path.join(output, 'domain.png') });
  });

  for (const width of [1920, 1366, 1024, 980, 390, 320]) {
    await check(`Reading layout at ${width}px`, async () => {
      await page.setViewportSize({ width, height: 844 });
      await visit('D01.g', 'Record Inventory Movements', '&view=sheet');
      await page.evaluate(() => window.scrollTo(0, 0));
      const metrics = await page.evaluate(() => ({
        width: innerWidth,
        overflow: document.documentElement.scrollWidth > innerWidth,
        definition: [...document.querySelectorAll('.business-sheet h2')].find(element => element.textContent === 'Définition')?.getBoundingClientRect().top,
        readingWidth: document.querySelector('.business-sheet .business-copy')?.getBoundingClientRect().width,
      }));
      measurements.push(metrics);
      await page.screenshot({ path: path.join(output, `sheet-${width}.png`) });
      assert.equal(metrics.overflow, false, JSON.stringify(metrics));
      assert.ok(metrics.definition < 844, `Definition below the first viewport: ${JSON.stringify(metrics)}`);
    });
    if (width <= 1000) await check(`Drawer keyboard, inert background and focus at ${width}px`, async () => {
      const menu = page.locator('#fa-tree-open'), sidebar = page.locator('.sidebar');
      await menu.click();
      assert.equal(await sidebar.getAttribute('role'), 'dialog');
      assert.equal(await sidebar.getAttribute('aria-modal'), 'true');
      assert.equal(await page.locator('#fa-main').evaluate(element => element.inert), true);
      assert.equal(await page.locator('.topbar').evaluate(element => element.inert), true);
      const focusables = sidebar.locator('button:not([disabled]):not([tabindex="-1"]), input, select, [role="treeitem"][tabindex="0"]');
      await focusables.first().focus(); await page.keyboard.press('Shift+Tab');
      assert.equal(await focusables.last().evaluate(element => element === document.activeElement), true, 'Shift+Tab wraps to the last drawer control.');
      await page.keyboard.press('Tab');
      assert.equal(await focusables.first().evaluate(element => element === document.activeElement), true, 'Tab wraps to the first drawer control.');
      await page.screenshot({ path: path.join(output, `drawer-${width}.png`) });
      await page.keyboard.press('Escape');
      await page.waitForFunction(() => !document.querySelector('.sidebar').classList.contains('open'));
      assert.equal(await menu.evaluate(element => element === document.activeElement), true);
      assert.equal(await page.locator('#fa-main').evaluate(element => element.inert), false);
      await menu.click(); await item('D01.d').focus(); await page.keyboard.press('Enter');
      await heading('Stocktaking').waitFor();
      await page.waitForFunction(() => document.activeElement?.tagName === 'H1');
      assert.equal(await page.locator('#fa-main').evaluate(element => element.inert), false);
      assert.equal(await sidebar.getAttribute('aria-modal'), null);
      assert.equal(await page.locator('#fa-tree-open').getAttribute('aria-expanded'), 'false');
    });
  }

  await check('Four extra explicit levels and distinct object/document/event relations', async () => {
    const fixture = structuredClone(api);
    for (let level = 1; level <= 4; level++) {
      fixture.nodes.push({ id: `TEST-L${level}`, kind: 'group', group_role: 'urbanism_level', level_ref: `TEST-LEVEL-${level}`, layer: 'transactional', fields: { name: `Niveau de test ${level}` }, review: { state: 'proposed' }, source_refs: [] });
      fixture.relations.push({ id: `TEST-R${level}`, type: 'contains', source_id: level === 1 ? 'D03' : `TEST-L${level - 1}`, target_id: `TEST-L${level}`, review: { state: 'proposed' }, source_refs: [] });
    }
    fixture.relations.find(relation => relation.type === 'contains' && relation.target_id === 'D03.b').source_id = 'TEST-L4';
    const artifacts = [
      { id: 'TEST-OBJ', kind: 'object', name: 'Objet de test', icon: 'lucide-box' },
      { id: 'TEST-DOC', kind: 'document', name: 'Document de test', icon: 'lucide-file-text' },
      { id: 'TEST-EVT', kind: 'event', name: 'Événement de test', icon: 'lucide-zap' },
    ];
    for (const artifact of artifacts) {
      fixture.nodes.push({ id: artifact.id, kind: artifact.kind, layer: 'transactional', fields: { name: artifact.name, definition: `Définition de ${artifact.name}.` }, review: { state: 'proposed' }, source_refs: [] });
      fixture.relations.push({ id: `REL-${artifact.id}`, type: 'relates-to', source_id: 'D03.b', target_id: artifact.id, fields: { label: 'utilise' }, qualification: { meaning: `Lien de test vers ${artifact.name}` }, review: { state: 'proposed' }, source_refs: [] });
    }
    await page.route('**/api/model*', route => route.fulfill({ json: fixture }));
    await page.setViewportSize({ width: 1366, height: 900 });
    // Full reload ensures this fixture is the only HTTP model read by the app.
    await page.goto(`${base}/#node=D03.b&view=sheet`); await page.reload();
    await heading('Promise Confirmation').waitFor(); await item('TEST-L4').waitFor();
    assert.equal(await item('D03.b').getAttribute('aria-level'), '7');
    assert.match(await item('TEST-L4').getAttribute('aria-label'), /Niveau d’urbanisme/);
    assert.equal(await item('TEST-L4').locator('[data-tree-id="D03.b"]').count(), 1);
    for (const artifact of artifacts) assert.equal(await item(artifact.id).count(), 0, `${artifact.kind} relation is not a structural child.`);
    await page.getByRole('tab', { name: /Relations/ }).click();
    for (const artifact of artifacts) {
      await page.locator(`.react-flow__node[data-id="${artifact.id}"]`).waitFor();
      assert.equal(await page.locator(`.react-flow__node[data-id="${artifact.id}"] [data-icon-kind="${artifact.kind}"] svg.${artifact.icon}`).count(), 1);
    }
    await page.screenshot({ path: path.join(output, 'future-relations.png') });
    for (const artifact of artifacts) {
      await visit(artifact.id, artifact.name, '&view=sheet');
      assert.equal(await page.locator(`.page-heading [data-icon-kind="${artifact.kind}"] svg.${artifact.icon}`).count(), 1);
      assert.equal(await item(artifact.id).count(), 0);
      assert.doesNotMatch(await page.getByRole('navigation', { name: 'Fil d’Ariane' }).innerText(), /Niveau de test|Order Promising/);
      assert.equal(await page.locator('.detail-boundaries').count(), 0);
      const fallback = page.locator('[role="treeitem"][tabindex="0"]');
      assert.equal(await fallback.count(), 1, 'A nonstructural artifact must not remove the keyboard entry into the tree.');
      assert.notEqual(await fallback.getAttribute('data-tree-id'), artifact.id);
      await page.locator('#fa-status').focus(); await page.keyboard.press('Tab');
      assert.equal(await fallback.evaluate(element => element === document.activeElement), true);
    }
    await page.unroute('**/api/model*');
  });
  await check('No browser exceptions', async () => assert.deepEqual(browserErrors, []));
  const result = { publication: api.version, serverPid: status.pid, checks, failures, measurements, browserErrors, output };
  await writeFile(path.join(output, 'results.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result));
  assert.equal(failures.length, 0, `${failures.length} ergonomics contract(s) failed; see ${path.join(output, 'results.json')}`);
} finally { await browser.close(); }

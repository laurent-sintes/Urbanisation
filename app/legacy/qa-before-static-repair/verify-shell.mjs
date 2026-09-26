import { staticModelUrl } from './static-test-helpers.mjs';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = (process.env.ATLAS_URL || 'http://127.0.0.1:8765').replace(/\/$/, '');
const output = fileURLToPath(new URL('./.runtime/qa-shell/', import.meta.url));
const baseline = process.argv.includes('--baseline');
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const errors = [], measurements = [];
try {
  const context = await browser.newContext({ reducedMotion: 'reduce', permissions: ['clipboard-read', 'clipboard-write'] });
  const page = await context.newPage();
  page.on('pageerror', error => errors.push(error.message));
  const snapshot = await (await context.request.get(await staticModelUrl(base))).json();
  const sample = snapshot.nodes.find(n => n.id === 'D04.j');
  const behavior = snapshot.nodes.filter(n => n.kind === 'behavior').sort((a,b) => b.fields.name.length-a.fields.name.length)[0];
  for (const viewport of [{ width: 1920, height: 1080 }, { width: 1440, height: 1000 }, { width: 1024, height: 768 }, { width: 390, height: 844 }, { width: 320, height: 568 }]) {
    await page.setViewportSize(viewport);
    await page.goto(`${base}/#node=universe-supply&view=map`);
    await page.locator('.capabilities-canvas').waitFor();
    await page.waitForFunction(() => document.querySelector('.business-card'));
    const reading = await page.locator('.workspace-content').boundingBox();
    measurements.push({ viewport, reading, topbar: await page.locator('.topbar').boundingBox() });
    await page.screenshot({ path: `${output}/${baseline ? 'before' : 'after'}-${viewport.width}.png` });
    if (baseline) continue;
    const nav = page.getByRole('navigation', { name: 'Fil d’Ariane' });
    assert.equal(await nav.count(), 1);
    const navBox = await nav.boundingBox();
    const barBox = await page.locator('.topbar').boundingBox();
    if (viewport.width > 1000) {
      assert.ok(navBox.y < barBox.y + barBox.height, 'Desktop breadcrumb must use top bar');
      assert.equal(await page.locator('.workspace-header .breadcrumb-row').count(), 0);
      assert.ok(barBox.height <= 56);
    } else {
      assert.ok(navBox.y >= barBox.y + barBox.height, 'Mobile breadcrumb must remain readable below bar');
      await page.locator('#fa-tree-open').click();
    }
    const logo = page.getByRole('img', { name: 'Groupe Beaumanoir', exact: true });
    assert.equal(await logo.count(), 1);
    const logoBox = await logo.boundingBox();
    assert.ok(logoBox.width <= 80 && logoBox.width >= 64);
    assert.ok(logoBox.y > viewport.height / 2 && logoBox.y + logoBox.height <= viewport.height);
    assert.ok(await logo.evaluate(el => el.naturalWidth > 0 && Boolean(el.closest('.sidebar-bottom'))));
    assert.ok(Math.abs(logoBox.width / logoBox.height - 1564 / 605) < .05);
    if (viewport.width <= 1000) {
      await page.screenshot({ path: `${output}/after-${viewport.width}-drawer.png` });
      await page.keyboard.press('Escape');
      assert.equal(await page.locator('#fa-tree-open').getAttribute('aria-expanded'), 'false');
      assert.equal(await page.evaluate(() => document.activeElement?.id), 'fa-tree-open');
    }
    await page.getByRole('button', { name: 'Copier le lien', exact: true }).click();
    assert.match(await page.evaluate(() => navigator.clipboard.readText()), /node=universe-supply/);
    await page.getByRole('button', { name: 'Masquer le message', exact: true }).click();
    await page.keyboard.press('Control+k');
    await page.waitForFunction(() => document.activeElement?.id === 'fa-search');
    if (viewport.width <= 1000) await page.locator('.drawer-close').click();
    for (const node of [sample, behavior]) {
      await page.goto(`${base}/#node=${node.id}&view=sheet`);
      await page.locator('.business-sheet').waitFor();
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
      for (const button of await nav.getByRole('button').all()) {
        const rect = await button.boundingBox();
        assert.ok(rect.width >= 24 && rect.height >= 24, `Breadcrumb target too small: ${await button.innerText()}`);
      }
      if (viewport.width > 1000) {
        const resizer = page.getByRole('separator', { name: 'Largeur de l’arbre' });
        await resizer.focus();
        for (const key of ['End', 'Home']) {
          await page.keyboard.press(key);
          const headerBox = await page.locator('.topbar').boundingBox();
          assert.equal(headerBox.height, 52);
          assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
          const navRight = await page.locator('.topbar-navigation .breadcrumb').boundingBox();
          const copy = await page.getByRole('button', { name: 'Copier le lien', exact: true }).boundingBox();
          assert.ok(navRight.x + navRight.width <= copy.x, 'Breadcrumb overlaps copy action');
        }
        await page.evaluate(() => localStorage.removeItem('flow-atlas:tree-width'));
        // Restore the default width for comparable viewport measurements.
        for (let step = 0; step < 6; step++) await page.keyboard.press('ArrowRight');
      }
      await nav.getByRole('button', { name: 'Urbanisation', exact: true }).click();
      await page.getByRole('heading', { name: 'Urbanisation', exact: true, level: 1 }).waitFor();
    }
  }
  assert.deepEqual(errors, []);
  const result = { version: snapshot.version, measurements, errors };
  if (!baseline) {
    const old = await readFile(`${output}/baseline.json`, 'utf8').then(JSON.parse).catch(() => undefined);
    if (old) result.gains = measurements.map((value, i) => ({ width: value.viewport.width, gainedHeight: Math.round(value.reading.height - old.measurements[i].reading.height) }));
  }
  await writeFile(`${output}/${baseline ? 'baseline' : 'report'}.json`, JSON.stringify(result, null, 2));
  console.log(JSON.stringify({ mode: baseline ? 'baseline' : 'checks', viewports: measurements.length, gains: result.gains, errors, output }, null, 2));
} finally { await browser.close(); }

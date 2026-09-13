const { chromium } = require('C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const fs = require('node:fs');
const assert = require('node:assert/strict');

(async () => {
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1080, height: 1100 }, deviceScaleFactor: 1 });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(pathToFileURL(path.join(__dirname, 'preview.html')).href);
    const frame = page.frameLocator('iframe');
    const app = frame.locator('#flow-atlas');
    async function capture(name) {
      await page.locator('iframe').evaluate(el => { el.style.height = '5000px'; });
      await page.waitForTimeout(200);
      const height = await app.evaluate(el => Math.ceil(el.scrollHeight));
      await page.locator('iframe').evaluate((el, h) => { el.style.height = `${h + 50}px`; }, height);
      await page.setViewportSize({ width: page.viewportSize().width, height: height + 100 });
      await page.waitForTimeout(200);
      await page.screenshot({ path: path.join(__dirname, name), fullPage: true });
    }
    await frame.getByRole('heading', { name: 'Socle transactionnel', exact: true }).waitFor();
    assert.equal(await frame.locator('.fa-grid .fa-tile').count(), 7);
    assert.equal(await frame.locator('.fa-ref-chips button').count(), 5);
    await capture('overview.png');

    await frame.locator('.fa-grid [data-go="D03"]').click();
    assert.equal(await frame.locator('.fa-grid .fa-tile').count(), 9);
    assert.equal(await frame.locator('.fa-grid .fa-badge').filter({ hasText: 'Capacité validée' }).count(), 9);
    await frame.locator('.fa-grid [data-go="D03.b"]').click();
    await frame.getByRole('heading', { name: 'Promise Confirmation', exact: true }).first().waitFor();
    await frame.getByRole('button', { name: 'Relations', exact: true }).click();
    assert.equal(await frame.locator('.fa-related').count(), 3);
    await frame.locator('.fa-related[data-go="ILL-DOC-01"]').click();
    await frame.getByRole('heading', { name: 'Confirmation de promesse', exact: true }).waitFor();
    await frame.locator('#fa-back').click();
    await frame.getByRole('heading', { name: 'Promise Confirmation', exact: true }).waitFor();
    await frame.locator('#fa-forward').click();
    await frame.getByRole('heading', { name: 'Confirmation de promesse', exact: true }).waitFor();

    const search = frame.locator('#fa-search');
    await search.fill('affectation');
    assert.deepEqual(await frame.locator('#fa-type option').evaluateAll(options => options.map(o => o.value)), ['all', 'domain', 'reference', 'group', 'capability', 'object', 'document', 'event']);
    assert.match(await frame.locator('.fa-results').innerText(), /Supply Assignment/);
    await frame.locator('.fa-result[data-go="D02.e"]').click();
    assert.match(await frame.locator('#fa-breadcrumb').innerText(), /Order Promising/);
    assert.match(await frame.locator('.fa-inspector').innerText(), /validée/);
    await search.fill('inventaire');
    assert.ok(await frame.locator('.fa-result[data-go="D01.d"]').count());
    await search.fill('D02.b');
    await search.press('Enter');
    assert.match(await frame.locator('#fa-breadcrumb').innerText(), /Inventory Management/);
    await search.fill('zzzintrouvable');
    await frame.getByRole('heading', { name: 'Aucun résultat' }).waitFor();
    await search.fill('promesse');
    await frame.locator('#fa-type').selectOption('event');
    assert.equal(await frame.locator('.fa-result').count(), 1);
    await frame.locator('.fa-result').click();
    await frame.getByRole('heading', { name: 'Promesse confirmée', exact: true }).first().waitFor();
    await search.fill('promesse');
    await frame.locator('#fa-type').selectOption('all');
    await frame.locator('#fa-status').selectOption('validated');
    const results = await frame.locator('.fa-result .fa-badge').allTextContents();
    assert.ok(results.length > 0 && results.every(s => s === 'Capacité validée'));
    await search.press('Escape');
    await search.press('Control+k');
    assert.equal(await search.evaluate(el => el === el.ownerDocument.activeElement), true);

    await frame.locator('.fa-nav[data-journey="start"]').click();
    for (const heading of ['Engagement de fourniture', 'Confirmation de promesse', 'Promesse confirmée']) {
      await frame.getByRole('button', { name: 'Continuer →', exact: true }).click();
      await frame.getByRole('heading', { name: heading, exact: true }).waitFor();
    }
    await capture('relations.png');
    await frame.getByRole('button', { name: 'Terminer', exact: true }).click();
    assert.equal(await frame.locator('#fa-journey').isVisible(), false);

    await frame.locator('.fa-nav[data-go="transactional"]').click();
    await frame.getByRole('button', { name: /Explorer le groupe/ }).click();
    assert.equal(await frame.locator('.fa-grid .fa-tile').count(), 5);
    await frame.locator('.fa-grid [data-go="D08"]').click();
    assert.equal(await frame.locator('.fa-grid .fa-tile').count(), 1);
    await frame.locator('.fa-grid .fa-tile').click();
    assert.match(await frame.locator('#fa-breadcrumb').innerText(), /Business References[\s\S]*Product Reference[\s\S]*Product Reference Ingestion/);
    await frame.locator('.fa-nav[data-go="process"]').click();
    await frame.getByRole('heading', { name: 'Modèle processus', exact: true }).waitFor();
    assert.equal(await frame.locator('.fa-grid .fa-tile').count(), 1);
    await frame.locator('.fa-nav[data-go="transactional"]').click();

    for (const width of [1080, 800, 480, 352]) {
      await page.setViewportSize({ width, height: 1100 });
      const overflow = await app.evaluate(el => ({ width: el.clientWidth, scroll: el.scrollWidth, documentWidth: el.ownerDocument.documentElement.clientWidth, documentScroll: el.ownerDocument.documentElement.scrollWidth }));
      assert.ok(overflow.scroll <= overflow.width + 2 && overflow.documentScroll <= overflow.documentWidth + 2, `Overflow at ${width}: ${JSON.stringify(overflow)}`);
      await frame.locator('.fa-nav[data-journey="start"]').click();
      const nestedOverflow = await app.evaluate(el => ({ width: el.clientWidth, scroll: el.scrollWidth }));
      assert.ok(nestedOverflow.scroll <= nestedOverflow.width + 2, `Detail overflow at ${width}`);
      if (width === 352) {
        assert.equal(await frame.locator('.fa-related-grid').evaluate(el => getComputedStyle(el).gridTemplateColumns.split(' ').length), 1);
        await capture('mobile.png');
      }
      await frame.locator('.fa-nav[data-go="transactional"]').click();
    }
    await page.setViewportSize({ width: 1080, height: 1100 });
    await page.emulateMedia({ colorScheme: 'dark' });
    await page.waitForTimeout(300);
    await capture('dark.png');
    assert.deepEqual(errors, []);
    const snapshot = JSON.parse(fs.readFileSync(path.join(__dirname, 'model-snapshot.json'), 'utf8').replace(/^\uFEFF/, ''));
    const caps = snapshot.domains.flatMap(d => d.capabilities);
    assert.equal(snapshot.domains.length, 12);
    assert.equal(caps.length, 36);
    assert.equal(new Set(caps.map(c => c.id)).size, 36);
    assert.equal(caps.filter(c => c.status === 'validated').length, 9);
    console.log('PASS: model counts, drill-down, typed relations, history, search/aliases/IDs, filters, keyboard, guided journey, references, process, four viewport sizes, dark theme, zero browser errors.');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });

import { createRequire } from 'node:module';
import { mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = (process.env.ATLAS_URL || 'http://127.0.0.1:8765').replace(/\/$/, '');
const output = new URL('./.runtime/qa-references/', import.meta.url);
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const checks = [], errors = [], measurements = [];
let page;
try {
  page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
  page.setDefaultTimeout(30000);
  page.on('pageerror', error => errors.push(error.message));
  const read = async version => {
    const response = await page.request.get(base + '/api/model' + (version ? '?version=' + version : ''), { timeout: 30000 });
    assert.equal(response.ok(), true);
    return response.json();
  };
  const current = await read();
  const historical = await read('2026-09-13.5');
  const nameOf = (model, id) => model.nodes.find(node => node.id === id).fields.name;
  const childrenOf = (model, id) => model.relations.filter(relation => ['presents', 'contains'].includes(relation.type) && relation.source_id === id).map(relation => model.nodes.find(node => node.id === relation.target_id));
  const hash = model => '#' + new URLSearchParams({ node: 'business-references', view: 'map', version: model.version });
  const routeOf = url => new URLSearchParams(new URL(url, base).hash.slice(1));
  const card = id => page.locator(`.business-card[data-node-id="${id}"]`);
  const heading = name => page.getByRole('heading', { level: 1, name, exact: true });
  const waitMap = async model => {
    await heading(nameOf(model, 'business-references')).waitFor();
    await page.waitForFunction(version => document.querySelector('#fa-version')?.dataset.version === version, model.version);
    const expected = childrenOf(model, 'business-references').map(node => node.id).sort();
    await page.waitForFunction(ids => JSON.stringify([...document.querySelectorAll('.business-card')].map(card => card.dataset.nodeId).sort()) === JSON.stringify(ids), expected);
    await page.waitForFunction(() => {
      const signature = document.querySelector('.react-flow__viewport')?.getAttribute('style') + JSON.stringify([...document.querySelectorAll('.business-card')].map(card => {
        const { x, y, width, height } = card.getBoundingClientRect();
        return [x, y, width, height];
      }));
      if (window.__referencesStable?.signature !== signature) {
        window.__referencesStable = { signature, since: performance.now() };
        return false;
      }
      return performance.now() - window.__referencesStable.since > 180;
    });
  };
  const inspect = async model => {
    const references = childrenOf(model, 'business-references');
    assert.ok(references.length > 0, 'Business References présente des référentiels publiés.');
    for (const reference of references) {
      assert.equal(reference.kind, 'reference');
      const expected = childrenOf(model, reference.id).filter(node => node.kind === 'capability');
      const links = card(reference.id).locator('a.capacity-link');
      assert.deepEqual(await links.allTextContents(), expected.map(node => node.fields.name), `${model.version} / ${reference.id}`);
      for (let index = 0; index < expected.length; index++) {
        const route = routeOf(await links.nth(index).getAttribute('href'));
        assert.equal(route.get('node'), expected[index].id);
        assert.equal(route.get('view'), 'sheet');
        assert.equal(route.get('version'), model.version);
        assert.equal(route.has('scope'), false);
      }
    }
    checks.push(`${model.version} : ${references.length} référentiels, capacités et liens exacts du snapshot publié.`);
  };
  const readCapability = async (model, referenceId, id, keyboard = false) => {
    const link = card(referenceId).getByRole('link', { name: nameOf(model, id), exact: true });
    if (keyboard) { await link.focus(); await page.keyboard.press('Enter'); }
    else await link.click();
    await heading(nameOf(model, id)).waitFor();
    await page.getByTestId('business-sheet').waitFor();
    assert.equal(routeOf(page.url()).get('node'), id);
    assert.equal(routeOf(page.url()).get('view'), 'sheet');
    assert.equal(routeOf(page.url()).get('version'), model.version);
  };
  const capture = async width => {
    await page.setViewportSize({ width, height: width < 600 ? 844 : 1000 });
    await waitMap(current);
    await page.mouse.move(5, 5);
    await page.keyboard.press('Escape');
    await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
    const geometry = await page.locator('.business-card').evaluateAll(cards => cards.map(card => {
      const rect = card.getBoundingClientRect();
      return { id: card.dataset.nodeId, links: [...card.querySelectorAll('a.capacity-link')].map(link => {
        const box = link.getBoundingClientRect();
        return { text: link.textContent, contained: box.left >= rect.left && box.right <= rect.right && box.top >= rect.top && box.bottom <= rect.bottom,
          unclipped: link.scrollHeight <= link.clientHeight + 1, fontSize: Number.parseFloat(getComputedStyle(link).fontSize) * rect.width / card.offsetWidth };
      }) };
    }));
    for (const reference of geometry) for (const link of reference.links) {
      assert.equal(link.contained && link.unclipped, true, `${width}px / ${reference.id} / ${link.text}`);
    }
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), true);
    measurements.push({ width, cards: geometry });
    await page.screenshot({ path: fileURLToPath(new URL('references-' + width + '.png', output)), fullPage: true });
  };

  await page.goto(base + '/' + hash(current));
  await waitMap(current);
  await inspect(current);
  await capture(1440);
  await readCapability(current, 'D08', 'D08.d');
  await page.goBack();
  await waitMap(current);
  await readCapability(current, 'D13', 'D13.a', true);
  checks.push('Clic et Entrée ouvrent directement la fiche de capacité sans sélection du référentiel ; publication conservée.');
  await page.goBack();
  await waitMap(current);
  await capture(390);
  await readCapability(current, 'D13', 'D13.a');
  checks.push('Desktop/mobile : textes non tronqués, aucun débordement, dernière capacité accessible sur écran étroit.');

  await page.evaluate(hash => { location.hash = hash; }, hash(historical));
  await waitMap(historical);
  await inspect(historical);
  await readCapability(historical, 'D08', 'D08.d');
  checks.push('v003 : le lien du référentiel ouvre la fiche de cette publication historique.');
  assert.deepEqual(errors, []);
  const report = { checkedAt: new Date().toISOString(), publication: current.version, checks, measurements, errors };
  await writeFile(new URL('browser-checks.json', output), JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify({ checks, errors }, null, 2));
} catch (error) {
  if (page) await page.screenshot({ path: fileURLToPath(new URL('failure.png', output)), fullPage: true }).catch(() => {});
  throw error;
} finally { await browser.close(); }

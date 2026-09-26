import { staticModelUrl } from './static-test-helpers.mjs';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = (process.env.ATLAS_URL || 'http://127.0.0.1:8765').replace(/\/$/, '');
const output = fileURLToPath(new URL('./.runtime/qa-fixed-header/', import.meta.url));
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const checks = [], errors = [];
let page;
try {
  const context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
  page = await context.newPage();
  page.on('pageerror', error => errors.push(error.message));
  const response = await context.request.get(await staticModelUrl(base));
  assert.ok(response.ok());
  const model = await response.json();
  assert.equal(model.space, 'release');
  const universe = model.nodes.find(node => node.id === 'universe-supply');
  const domain = model.nodes.find(node => node.id === 'D04');
  const capability = model.nodes.find(node => node.id === 'D04.j');
  const behavior = model.nodes.find(node => node.kind === 'behavior');
  const longest = [...model.nodes].sort((a, b) => (b.fields.finality?.length || 0) - (a.fields.finality?.length || 0))[0];
  assert.ok(universe && domain && capability && behavior && longest);
  const content = page.locator('.workspace-content');
  const header = page.locator('.workspace-header');
  const goto = async (node, view, extra = {}) => {
    await page.goto(`${base}/#${new URLSearchParams({ node: node?.id || '', view, ...extra })}`);
    await header.waitFor();
    const ready = { map: '.react-flow__viewport', sheet: '.business-sheet', market: '.market-page', relations: '.dependency-canvas', glossary: '.glossary-page', principles: '.modeling-guide-page' }[view];
    await page.locator(ready).waitFor();
  };
  const stableHeader = async (before, label) => {
    const after = await header.boundingBox();
    for (const key of ['x', 'y', 'width', 'height']) assert.ok(Math.abs(after[key] - before[key]) < 1, `${label}: header ${key} changed`);
    assert.equal(await page.evaluate(() => window.scrollY), 0, `${label}: document scrolled`);
    assert.equal(await page.locator('.workspace').evaluate(el => el.scrollTop), 0, `${label}: header container scrolled`);
  };
  const scrollCheck = async label => {
    const before = await header.boundingBox();
    const overflow = await content.evaluate(el => el.scrollHeight > el.clientHeight + 2);
    await content.evaluate(el => { el.scrollTop = el.scrollHeight; });
    if (overflow) assert.ok(await content.evaluate(el => el.scrollTop > 0), `${label}: content did not scroll`);
    await stableHeader(before, label);
    checks.push(`${label} : bandeau immobile${overflow ? ', contenu défilant' : ', contenu court accessible'}.`);
  };

  await goto(universe, 'map');
  await page.waitForFunction(() => document.querySelector('.capabilities-canvas')?.clientHeight > 600);
  const mapHeader = await header.boundingBox();
  const box = await content.boundingBox();
  await page.mouse.move(box.x + box.width / 2, box.y + Math.min(220, box.height / 2));
  await page.mouse.wheel(0, 350);
  await page.waitForFunction(() => document.querySelector('.workspace-content').scrollTop > 100);
  await stableHeader(mapHeader, 'Molette sur la carte univers');
  await scrollCheck('Carte univers');
  assert.equal(await page.getByRole('button', { name: 'Ouvrir la fiche', exact: true }).count(), 0);
  assert.equal(await page.locator('.selection-strip').count(), 0);
  await page.screenshot({ path: `${output}/desktop-map-scrolled.png` });

  // A selected card changes the Fiche target without moving the map's scope or scroll.
  const card = page.locator('.business-card[data-node-id="D04"]');
  await card.scrollIntoViewIfNeeded();
  const previousTop = await content.evaluate(el => el.scrollTop);
  await card.locator('h3').click();
  await page.waitForFunction(() => new URLSearchParams(location.hash.slice(1)).get('node') === 'D04');
  assert.equal(await page.locator('#page-title').innerText(), universe.fields.name);
  assert.ok(Math.abs(await content.evaluate(el => el.scrollTop) - previousTop) < 2, 'Selection moved the map');
  await stableHeader(mapHeader, 'Sélection de carte');
  assert.equal(await page.locator('.view-selection').innerText(), `Sélection : ${domain.fields.name}`);
  await page.getByRole('tab', { name: 'Fiche', exact: true }).click();
  await page.locator('.business-sheet').waitFor();
  assert.equal(await page.locator('#page-title').innerText(), domain.fields.name);
  assert.equal(await content.evaluate(el => el.scrollTop), 0);
  checks.push('Sélection sans saut, fiche sélectionnée accessible dans le bandeau, changement d’onglet remis en haut.');

  await goto(universe, 'map');
  await card.locator('h3').dblclick();
  await page.waitForFunction(() => new URLSearchParams(location.hash.slice(1)).get('scope') === 'D04');
  assert.equal(await page.locator('#page-title').innerText(), domain.fields.name);
  await page.getByRole('button', { name: 'Afficher la carte en plein écran', exact: true }).click();
  await page.waitForFunction(() => Boolean(document.fullscreenElement));
  await page.evaluate(() => document.exitFullscreen());
  await page.waitForFunction(() => !document.fullscreenElement);
  assert.ok(await header.isVisible());
  checks.push('Double-clic pour explorer un domaine et aller-retour en plein écran.');

  for (const node of [universe, domain, capability, behavior]) {
    for (const view of ['sheet', 'market']) {
      await goto(node, view);
      await scrollCheck(`${node.kind} / ${view}`);
    }
  }
  await goto(capability, 'relations');
  await scrollCheck('Relations');
  await goto(undefined, 'map');
  await scrollCheck('Accueil');
  for (const mode of ['model', 'meta']) {
    await goto(undefined, 'glossary', { glossary: mode });
    await scrollCheck(`Glossaire ${mode}`);
    const before = await header.boundingBox();
    await page.locator('.glossary-index ul').evaluate(el => { el.scrollTop = el.scrollHeight; });
    await stableHeader(before, 'Liste du glossaire');
  }
  await goto(undefined, 'principles');
  await scrollCheck('Guide du méta modèle');

  await goto(capability, 'sheet');
  const sheetHeader = await header.boundingBox();
  await page.getByRole('navigation', { name: 'Dans cette fiche' }).getByRole('button', { name: 'Comportements', exact: true }).click();
  const section = page.locator(`[id="field-${capability.id}-behaviors"]`);
  await page.waitForFunction(id => {
    const target = document.getElementById(id).getBoundingClientRect();
    const frame = document.querySelector('.workspace-content').getBoundingClientRect();
    return target.top >= frame.top && target.top < frame.bottom;
  }, `field-${capability.id}-behaviors`);
  await stableHeader(sheetHeader, 'Sommaire de fiche');
  await goto(capability, 'sheet', { section: 'behaviors' });
  await page.waitForFunction(() => document.querySelector('.workspace-content').scrollTop > 0);
  const sectionBox = await section.boundingBox(), contentBox = await content.boundingBox();
  assert.ok(sectionBox.y >= contentBox.y && sectionBox.y < contentBox.y + contentBox.height, 'Deep link target hidden');
  assert.equal(await page.locator('.workspace').evaluate(el => el.scrollTop), 0);
  await content.evaluate(el => { el.scrollTop = 0; el.focus({ preventScroll: true }); });
  await page.keyboard.press('PageDown');
  await page.waitForFunction(() => document.querySelector('.workspace-content').scrollTop > 0);
  await page.waitForFunction(() => {
    const top = document.querySelector('.workspace-content').scrollTop;
    if (window.__scrollStability?.top !== top) { window.__scrollStability = { top, since: performance.now() }; return false; }
    return performance.now() - window.__scrollStability.since > 120;
  });
  await stableHeader(sheetHeader, 'Clavier PageDown');
  await page.getByRole('tab', { name: 'Fiche', exact: true }).focus();
  await page.keyboard.press('ArrowRight');
  await page.getByRole('tab', { name: /^Relations/ }).waitFor({ state: 'visible' });
  assert.equal(await page.getByRole('tab', { name: /^Relations/ }).getAttribute('aria-selected'), 'true');
  assert.equal(await content.evaluate(el => el.scrollTop), 0);
  assert.equal(new URLSearchParams(new URL(page.url()).hash.slice(1)).has('section'), false);
  await page.getByRole('tab', { name: 'Fiche', exact: true }).click();
  assert.equal(await content.evaluate(el => el.scrollTop), 0, 'An old section link must not override tab navigation');
  checks.push('Sommaire, lien direct de section, PageDown et navigation clavier entre onglets.');

  for (const viewport of [{ width: 390, height: 844 }, { width: 320, height: 568 }, { width: 844, height: 390 }, { width: 720, height: 500 }]) {
    await page.setViewportSize(viewport);
    for (const [node, view] of [[universe, 'map'], [capability, 'sheet'], [longest, 'market']]) {
      await goto(node, view);
      const frame = await content.boundingBox();
      assert.ok(frame.height >= 120, `${viewport.width}×${viewport.height}, ${node.id}/${view}: reading area only ${frame.height}px`);
      assert.ok(frame.y + frame.height <= viewport.height + 1, 'Content extends below viewport');
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), 'Horizontal document overflow');
      await scrollCheck(`${viewport.width}×${viewport.height} / ${node.id} / ${view}`);
    }
    if (viewport.width === 390) await page.screenshot({ path: `${output}/mobile-scrolled.png` });
  }
  const touchContext = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, reducedMotion: 'reduce' });
  const touchPage = await touchContext.newPage();
  touchPage.on('pageerror', error => errors.push(error.message));
  await touchPage.goto(`${base}/#node=${universe.id}&view=map`);
  await touchPage.locator('.touch-scroll').waitFor();
  await touchPage.waitForFunction(() => document.querySelector('.capabilities-canvas')?.clientHeight > 1000);
  const touchHeader = await touchPage.locator('.workspace-header').boundingBox();
  const touch = await touchContext.newCDPSession(touchPage);
  await touch.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: 195, y: 720 }] });
  for (let y = 670; y >= 420; y -= 50) {
    await touch.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x: 195, y }] });
    await touchPage.evaluate(() => new Promise(resolve => requestAnimationFrame(resolve)));
  }
  await touch.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] });
  await touchPage.waitForFunction(() => document.querySelector('.workspace-content').scrollTop > 100);
  assert.deepEqual(await touchPage.locator('.workspace-header').boundingBox(), touchHeader);
  assert.equal(await touchPage.evaluate(() => scrollY), 0);
  await touchPage.locator('#fa-tree-open').click();
  await touchPage.locator('.drawer-close').click();
  assert.deepEqual(await touchPage.locator('.workspace-header').boundingBox(), touchHeader);
  await touch.detach();
  await touchContext.close();
  checks.push('Balayage tactile de la carte et ouverture/fermeture de l’arbre mobile : bandeau immobile.');
  assert.deepEqual(errors, []);
  await writeFile(`${output}/report.json`, JSON.stringify({ version: model.version, checks, errors }, null, 2));
  console.log(JSON.stringify({ version: model.version, passed: checks.length, output }, null, 2));
} catch (error) {
  if (page) await page.screenshot({ path: `${output}/failure.png` });
  throw error;
} finally {
  await browser.close();
}

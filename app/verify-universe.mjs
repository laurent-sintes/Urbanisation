import { createRequire } from 'node:module';
import { mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = (process.env.ATLAS_URL || 'http://127.0.0.1:8765').replace(/\/$/, '');
const output = new URL('./.runtime/qa-universe/', import.meta.url);
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const checks = [], errors = [], measurements = [];
let page;
try {
  page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
  page.setDefaultTimeout(30000);
  page.on('pageerror', error => errors.push(error.message));
  const fetchModel = async version => {
    const response = await page.request.get(base + '/api/model' + (version ? '?version=' + version : ''), { timeout: 30000 });
    assert.equal(response.ok(), true);
    return response.json();
  };
  const current = await fetchModel();
  const historical = await fetchModel('2026-09-13.5');
  const card = id => page.locator(`.business-card[data-node-id="${id}"]`);
  const heading = name => page.getByRole('heading', { level: 1, name, exact: true });
  const params = href => new URLSearchParams(new URL(href, base).hash.slice(1));
  const nameOf = (model, id) => model.nodes.find(node => node.id === id).fields.name;
  const children = (model, id) => model.relations.filter(relation => ['contains', 'presents'].includes(relation.type) && relation.source_id === id).map(relation => model.nodes.find(node => node.id === relation.target_id));
  const waitMap = async (model, universe) => {
    await heading(universe.fields.name).waitFor();
    const ids = children(model, universe.id).map(node => node.id).sort();
    if (!ids.length) return;
    await page.waitForFunction(expected => JSON.stringify([...document.querySelectorAll('.business-card')].map(node => node.dataset.nodeId).sort()) === JSON.stringify(expected), ids);
    await page.waitForFunction(() => {
      const viewport = document.querySelector('.react-flow__viewport');
      const signature = viewport?.getAttribute('style') + JSON.stringify([...document.querySelectorAll('.business-card')].map(card => {
        const { x, y, width, height } = card.getBoundingClientRect();
        return [x, y, width, height];
      }));
      if (window.__universeStable?.signature !== signature) {
        window.__universeStable = { signature, since: performance.now() };
        return false;
      }
      return performance.now() - window.__universeStable.since > 180;
    });
  };
  const visit = async (model, universe, pinned = true) => {
    await page.goto(base + '/#' + new URLSearchParams({ node: universe.id, view: 'map', ...(pinned ? { version: model.version } : {}) }));
    await waitMap(model, universe);
  };
  const capture = async name => {
    await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
    await page.screenshot({ path: fileURLToPath(new URL(name + '.png', output)), fullPage: true });
  };

  for (const model of [current, historical]) {
    const universes = model.nodes.filter(node => node.group_role === 'urbanism_level' && node.level_ref === 'universe');
    assert.ok(universes.length > 0);
    for (const universe of universes) {
      await visit(model, universe, model !== current);
      for (const domain of children(model, universe.id)) {
        const expected = domain.kind === 'domain' ? children(model, domain.id).filter(node => node.kind === 'capability') : [];
        const links = card(domain.id).locator('a.capacity-link');
        assert.deepEqual(await links.allTextContents(), expected.map(node => node.fields.name), `${model.version} / ${domain.id} : exact published capacities`);
        for (let index = 0; index < expected.length; index++) {
          const href = params(await links.nth(index).getAttribute('href'));
          assert.equal(href.get('node'), expected[index].id);
          assert.equal(href.get('view'), 'sheet');
          assert.equal(href.get('version'), model.version);
          assert.equal(href.has('scope'), false);
        }
        if (domain.kind === 'group' && domain.group_role !== 'urbanism_level') {
          const references = children(model, domain.id).filter(node => node.kind === 'reference');
          const referenceLinks = card(domain.id).locator('a.reference-link');
          assert.deepEqual(await referenceLinks.allTextContents(), references.map(node => node.fields.name));
          for (let index = 0; index < references.length; index++) {
            const href = params(await referenceLinks.nth(index).getAttribute('href'));
            assert.equal(href.get('node'), references[index].id);
            assert.equal(href.get('view'), 'sheet');
            assert.equal(href.get('version'), model.version);
            assert.equal(href.has('scope'), false);
          }
        }
      }
      if (!children(model, universe.id).length) {
        assert.equal(await page.locator('a.capacity-link').count(), 0);
        await page.getByText('Aucun élément publié dans ce périmètre.', { exact: true }).waitFor();
      }
    }
    checks.push(`${model.version} : chaque domaine montre exactement ses capacités publiées ; les groupes de présentation et univers vides restent distincts.`);
  }

  const supply = current.nodes.find(node => node.id === 'universe-supply');
  await visit(current, supply, false);
  const references = children(current, 'business-references').filter(node => node.kind === 'reference');
  assert.ok(references.length > 0, 'Business References présente des référentiels publiés.');
  const referenceList = card('business-references').getByRole('list', { name: 'Référentiels de Business References' });
  await card('business-references').screenshot({ path: fileURLToPath(new URL('supply-business-references.png', output)) });
  await referenceList.getByRole('link').first().focus();
  await page.getByRole('tooltip').waitFor();
  assert.ok((await page.getByRole('tooltip').innerText()).includes(references[0].fields.name));
  await page.keyboard.press('Escape');
  await page.getByRole('tooltip').waitFor({ state: 'hidden' });
  await page.keyboard.press('Enter');
  await heading(references[0].fields.name).waitFor();
  await page.getByTestId('business-sheet').waitFor();
  assert.equal(params(page.url()).get('version'), current.version);
  await page.goBack();
  await waitMap(current, supply);
  await referenceList.getByRole('link').last().click();
  await heading(references.at(-1).fields.name).waitFor();
  await page.getByTestId('business-sheet').waitFor();
  assert.equal(params(page.url()).get('version'), current.version);
  await page.goBack();
  await waitMap(current, supply);
  checks.push(`Business References dans Supply : ${references.length} référentiels exacts, aperçu, clic/Entrée vers leur fiche et retour à la carte.`);
  const protection = card('D01').getByRole('link', { name: nameOf(current, 'D02.b'), exact: true });
  const reservation = card('D01').getByRole('link', { name: nameOf(current, 'D02.c'), exact: true });
  await protection.hover();
  await page.getByRole('tooltip').waitFor();
  assert.ok((await page.getByRole('tooltip').innerText()).includes(nameOf(current, 'D02.b')));
  await page.keyboard.press('Escape');
  await page.getByRole('tooltip').waitFor({ state: 'hidden' });
  await reservation.click();
  await heading(nameOf(current, 'D02.c')).waitFor();
  await page.getByTestId('business-sheet').waitFor();
  assert.equal(params(page.url()).get('node'), 'D02.c');
  assert.equal(params(page.url()).get('view'), 'sheet');
  assert.equal(params(page.url()).get('version'), current.version);
  await page.goBack();
  await waitMap(current, supply);
  // The restored card can appear beneath the old mouse position; start keyboard navigation without its hover preview.
  await page.mouse.move(10, 10);
  await page.getByRole('tooltip').waitFor({ state: 'hidden' });
  await protection.focus();
  await page.getByRole('tooltip').waitFor();
  await page.keyboard.press('Tab');
  assert.equal(await reservation.evaluate(link => document.activeElement === link), true);
  await page.keyboard.press('Enter');
  await heading(nameOf(current, 'D02.c')).waitFor();
  await page.getByTestId('business-sheet').waitFor();
  await page.goBack();
  await waitMap(current, supply);
  await protection.focus();
  await page.keyboard.press('Control+k');
  await page.waitForFunction(() => document.activeElement?.id === 'fa-search');
  checks.push('D02.b/c dans D01 : aperçu au survol/focus, Échap, clic direct sans sélection du domaine, retour navigateur et Tab/Entrée.');
  checks.push('Ctrl+K depuis une capacité conserve l’accès à la recherche globale.');

  await visit(historical, historical.nodes.find(node => node.id === supply.id));
  await card('D03').getByRole('link', { name: nameOf(historical, 'D02.e'), exact: true }).click();
  await heading(nameOf(historical, 'D02.e')).waitFor();
  assert.equal(params(page.url()).get('view'), 'sheet');
  assert.equal(params(page.url()).get('version'), historical.version);
  await page.reload();
  await heading(nameOf(historical, 'D02.e')).waitFor();
  assert.equal(params(page.url()).get('version'), historical.version);
  checks.push('v003 : D02.e ouvre sa fiche depuis D03 et conserve la publication après rechargement.');

  for (const viewport of [{ width: 1440, height: 1000 }, { width: 390, height: 844 }]) {
    if (viewport.width < 600) {
      await page.close();
      page = await browser.newPage({ viewport, isMobile: true, hasTouch: true, reducedMotion: 'reduce' });
      page.setDefaultTimeout(30000);
      page.on('pageerror', error => errors.push(error.message));
    } else await page.setViewportSize(viewport);
    await visit(current, supply, false);
    const geometry = await page.locator('.business-card').evaluateAll(cards => cards.map(card => {
      const box = card.getBoundingClientRect();
      return { id: card.dataset.nodeId, links: [...card.querySelectorAll('a.card-child-link')].map(link => {
        const rect = link.getBoundingClientRect();
        return { text: link.textContent, contained: rect.left >= box.left - 1 && rect.right <= box.right + 1 && rect.top >= box.top - 1 && rect.bottom <= box.bottom + 1,
          unclipped: link.scrollHeight <= link.clientHeight + 1, renderedFontSize: Number.parseFloat(getComputedStyle(link).fontSize) * box.width / card.offsetWidth };
      }) };
    }));
    for (const domain of geometry) for (const link of domain.links) {
      assert.equal(link.contained, true, `${viewport.width}px / ${domain.id} / ${link.text} outside card`);
      assert.equal(link.unclipped, true, `${viewport.width}px / ${domain.id} / ${link.text} clipped`);
    }
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), true);
    measurements.push({ viewport, cards: geometry });
    if (viewport.width < 600) {
      await page.locator('.graph-canvas').evaluate(canvas => canvas.scrollIntoView({ block: 'start', behavior: 'instant' }));
      await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
      const before = await page.evaluate(() => scrollY);
      const touch = await page.context().newCDPSession(page);
      await touch.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: 195, y: 700 }] });
      for (let y = 650; y >= 350; y -= 50) {
        await touch.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x: 195, y }] });
        await new Promise(resolve => setTimeout(resolve, 50));
      }
      await touch.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] });
      await page.waitForFunction(start => scrollY > start + 100, before);
      await touch.detach();
      // A full-page mobile capture temporarily changes viewport metrics; take it after the gesture.
      await capture('supply-' + viewport.width);
      const last = page.locator('.card-child-list a.reference-link').last();
      const target = params(await last.getAttribute('href')).get('node');
      await last.click();
      await heading(nameOf(current, target)).waitFor();
      await page.getByTestId('business-sheet').waitFor();
    } else await capture('supply-' + viewport.width);
  }
  checks.push('Desktop et mobile tactile : capacités et référentiels sans troncature ni débordement, balayage du canvas défile la page et dernier référentiel accessible.');
  assert.deepEqual(errors, []);
  const report = { checkedAt: new Date().toISOString(), publication: current.version, checks, measurements, errors };
  await writeFile(new URL('browser-checks.json', output), JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify({ checks, errors }, null, 2));
} catch (error) {
  if (page) await page.screenshot({ path: fileURLToPath(new URL('failure.png', output)), fullPage: true }).catch(() => {});
  throw error;
} finally { await browser.close(); }

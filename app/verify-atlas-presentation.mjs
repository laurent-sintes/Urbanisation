import { createRequire } from 'node:module';
import { mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = process.env.ATLAS_URL || 'http://127.0.0.1:8765';
const output = new URL('../audits/2026-09-19-atlas-U450/browser/', import.meta.url);
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const errors = [], checks = [];
let activePage;
try {
  const page = await browser.newPage({ viewport: { width: 1500, height: 1050 }, reducedMotion: 'reduce' });
  activePage = page;
  page.setDefaultTimeout(12000);
  page.on('pageerror', error => errors.push(error.message));
  const status = await (await page.request.get(base + '/api/status')).json();
  assert.equal(status.appName, 'FLOW Atlas'); assert.equal(status.space, 'release');
  const model = await (await page.request.get(base + '/api/model')).json();
  const guide = await (await page.request.get(base + '/api/modeling-guide?version=' + model.version)).json();
  assert.equal(guide.status, 'available');
  const goto = async hash => { await page.goto(base + '/#' + hash); await page.locator('#page-title').waitFor(); };
  const clean = async () => {
    assert.equal(await page.locator('.status-badge, .lifecycle-badge, .source-dialog, .validation-summary, .detail-reservations, .source-link').count(), 0);
    assert.equal(await page.getByText('Publier ne vaut pas valider', { exact: true }).count(), 0);
    const internalLinks = await page.locator('a[href]').evaluateAll(items => items.filter(item => item.origin === location.origin && /backlog|connaissance\/|source=/.test(item.getAttribute('href'))).map(item => ({text:item.textContent,href:item.getAttribute('href')})));
    assert.deepEqual(internalLinks, [], page.url());
  };
  await goto('view=principles');
  await page.locator('.guide-lesson').waitFor();
  assert.equal(await page.locator('h1').innerText(), 'Comprendre le méta modèle');
  assert.equal(await page.locator('.guide-topics > button').count(), 6);
  for (const button of await page.locator('.guide-topics > button').all()) {
    await button.click();
    await page.locator('.guide-reveal').click();
    assert.ok((await page.locator('.guide-answer').innerText()).trim());
    await page.locator('.guide-contribute > summary').click();
    await clean();
  }
  checks.push('Six repères du méta modèle accessibles, explications et frontières présentes, sources internes masquées.');
  await page.screenshot({ path: fileURLToPath(new URL('meta-model.png', output)), fullPage: true });
  await page.getByRole('button', { name: 'Glossaire métier', exact: true }).click();
  await page.locator('[data-glossary="model"]').waitFor();
  assert.equal(await page.locator('.glossary-index li').count(), model.glossary.terms.length - guide.guide.glossary.model_term_ids.length);
  assert.ok((await page.locator('.glossary-term h2').innerText()).trim());
  const longest = [...model.glossary.terms].filter(t => !guide.guide.glossary.model_term_ids.includes(t.id)).sort((a,b) => JSON.stringify(b).length - JSON.stringify(a).length)[0];
  await goto('view=glossary&term=' + longest.id);
  await page.locator('#term-' + longest.id).waitFor();
  const list = page.locator('.glossary-index ul'), detail = page.locator('.glossary-term');
  const detailBox = await detail.boundingBox();
  await list.hover(); await page.mouse.wheel(0, 500);
  await page.waitForFunction(() => document.querySelector('.glossary-index ul').scrollTop > 0);
  assert.equal(await detail.evaluate(el => el.scrollTop), 0);
  assert.equal((await detail.boundingBox()).y, detailBox.y);
  await detail.hover(); await page.mouse.wheel(0, 500);
  await page.waitForFunction(() => document.querySelector('.glossary-term').scrollTop > 0);
  await page.locator('.glossary-index li a').last().click();
  await page.waitForFunction(() => document.querySelector('.glossary-term').scrollTop === 0);
  await page.getByRole('textbox', { name: 'Rechercher dans le glossaire' }).fill('introuvable-xyz');
  assert.equal(await page.locator('.glossary-index li').count(), 0);
  await page.getByRole('textbox', { name: 'Rechercher dans le glossaire' }).fill('');
  await clean();
  checks.push('Glossaire métier : sélection initiale, recherche, défilements indépendants immédiats, retour en haut au changement de terme.');
  await page.getByRole('button', { name: 'Glossaire du méta modèle', exact: true }).click();
  await page.locator('[data-glossary="meta"]').waitFor();
  assert.equal(await page.locator('.glossary-index li').count(), guide.guide.glossary.terms.length + guide.guide.glossary.model_term_ids.length);
  await goto('view=glossary&term=TER001');
  await page.locator('[data-glossary="meta"] #term-TER001').waitFor();
  await goto('view=glossary&glossary=meta&term=MOD006');
  await page.locator('#term-MOD006').waitFor();
  await clean();
  await page.screenshot({ path: fileURLToPath(new URL('meta-glossary.png', output)), fullPage: true });
  checks.push('Deux glossaires distincts ; ancien lien TER001 dirigé vers le méta modèle ; MOD006 et ses exemples accessibles.');
  for (const id of ['D03', 'D03.n', 'BHV001']) {
    await goto('view=sheet&node=' + id + '&source=connaissance/01-contributions-utilisateur.md&anchor=u450');
    await page.locator('.business-sheet').waitFor(); await clean();
    assert.doesNotMatch(await page.locator('.business-sheet').innerText(), /\bU\d+\b|Le nom et la composition sont adoptés|U445 adopte/);
  }
  await goto('view=relations&node=D03');
  await page.locator('.dependencies-pane').waitFor(); await clean();
  checks.push('Fiches domaine, capacité, comportement et vue Relations sans statuts de validation ni accès aux sources internes, y compris ancien lien source.');
  const expectedRefs = {'Product Reference':'lucide-package','Party / Role':'lucide-users','Catalog':'lucide-book-open','Agreement':'lucide-file-signature','Fulfillment Network':'lucide-network','Service Catalog':'lucide-clipboard-list'};
  for (const ref of model.nodes.filter(n => n.kind === 'reference')) {
    const relation = model.relations.find(r => r.type === 'contains' && r.source_id === ref.id && model.nodes.find(n => n.id === r.target_id)?.kind === 'capability');
    if (!relation) continue;
    await goto('view=sheet&node=' + relation.target_id);
    await page.locator('.business-sheet').waitFor();
    const icons = page.locator(`[data-reference-icon="${ref.fields.name}"] svg`);
    assert.ok(await icons.count() > 0, ref.fields.name);
    assert.ok((await icons.first().getAttribute('class')).includes(expectedRefs[ref.fields.name]), ref.fields.name);
  }
  checks.push('Capacités des six référentiels : pictogrammes métier spécifiques fondés sur leur parent explicite.');
  await page.setViewportSize({ width: 390, height: 844 });
  await goto('view=glossary&glossary=meta&term=MOD006');
  await page.locator('#term-MOD006').waitFor();
  assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
  assert.equal(Math.round((await page.locator('.glossary-index').boundingBox()).height), 240);
  await page.screenshot({ path: fileURLToPath(new URL('mobile-glossary.png', output)), fullPage: true });
  checks.push('Mobile 390 px : aucun débordement horizontal, index borné et définition séparée.');
  // Future published fields only in this browser fixture; no live backlog read or fallback.
  const fixture = structuredClone(model);
  const types = { policy_strategy:'sliders-horizontal', process_variant:'route', intervention_mechanism:'settings-2', business_scope:'scan-line', decision_dimension:'compass', business_effect:'arrow-left-right', planning_practice:'calendar-check' };
  const behaviors = fixture.nodes.filter(n => n.kind === 'behavior').slice(0, 7);
  Object.keys(types).forEach((type, index) => behaviors[index].fields.nature = type);
  await page.route('**/api/model?*', route => route.fulfill({ json: fixture }));
  await page.route('**/api/model', route => route.fulfill({ json: fixture }));
  await page.setViewportSize({ width: 1500, height: 1050 });
  await page.reload();
  await page.locator('#term-MOD006').waitFor();
  for (const behavior of behaviors) {
    await goto('view=sheet&node=' + behavior.id);
    await page.locator('.business-sheet').waitFor();
    const icons = page.locator(`[data-behavior-type="${behavior.fields.nature}"] svg`);
    assert.ok(await icons.count() > 0);
    assert.ok((await icons.first().getAttribute('class')).includes('lucide-' + types[behavior.fields.nature]));
  }
  checks.push('Fixture de publication isolée : les sept formes de comportements utilisent sept pictogrammes distincts.');
  assert.deepEqual(errors, []);
  const result = { version: model.version, guide: guide.guide.version, checks, errors };
  await writeFile(new URL('verification.json', output), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
} catch (error) {
  console.error(JSON.stringify({errors, url:activePage?.url(), text:activePage ? (await activePage.locator('body').innerText()).slice(-1800) : ''}));
  throw error;
} finally { await browser.close(); }

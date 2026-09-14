import { createRequire } from 'node:module';
import { mkdir, writeFile } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = process.env.ATLAS_URL || 'http://127.0.0.1:8765';
const output = new URL('./.runtime/qa-glossary/', import.meta.url);
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const errors = [], checks = [];
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
  page.setDefaultTimeout(10000);
  page.on('pageerror', e => errors.push(e.message));
  const raw = await (await page.request.get(base + '/api/model')).json();
  await page.goto(base + '/#version=2026-09-13.5&view=glossary');
  await page.getByRole('heading', { name: 'Glossaire non publié dans cette version' }).waitFor();
  checks.push('La publication réelle v003 ne reçoit aucun terme du backlog.');
  await page.screenshot({ path: fileURLToPath(new URL('publication-v003.png', output)), fullPage: true });
  if (raw.glossary?.terms.length) {
    await page.goto(base + '/#view=glossary');
    await page.getByRole('textbox', { name: 'Rechercher dans le glossaire' }).waitFor();
    assert.equal(await page.locator('.glossary-index li').count(), raw.glossary.terms.length);
    const unit = raw.glossary.terms.find(term => term.id === 'TER059');
    if (unit) {
      await page.getByRole('textbox', { name: 'Rechercher dans le glossaire' }).fill('Product Unit');
      await page.locator('.glossary-index').getByRole('link', { name: 'Product Unit', exact: true }).hover();
      await page.getByRole('tooltip').waitFor();
      assert.ok((await page.getByRole('tooltip').innerText()).includes(unit.short_description));
      await page.locator('.glossary-index').getByRole('link', { name: 'Product Unit', exact: true }).click();
      await page.getByRole('heading', { level: 2, name: 'Product Unit', exact: true }).waitFor();
      await page.screenshot({ path: fileURLToPath(new URL('published-product-unit.png', output)) });
      await page.locator('.glossary-term').getByRole('link', { name: 'Serial Number', exact: true }).click();
      await page.getByRole('heading', { level: 2, name: 'Serial Number', exact: true }).waitFor();
      assert.ok(page.url().includes('version=' + raw.version));
    }
    checks.push(`La publication réelle ${raw.version} affiche ses ${raw.glossary.terms.length} termes, leurs infobulles et liens.`);
  }
  await page.goto(base + '/#node=D01.f&view=sheet');
  const parent = page.locator('.detail-parent a.model-reference').first();
  await parent.hover();
  await page.getByRole('tooltip').waitFor();
  assert.ok((await page.getByRole('tooltip').textContent()).includes('Inventory Management'));
  const pinned = await parent.getAttribute('href');
  assert.ok(pinned.includes('version=' + raw.version));
  await page.keyboard.press('Escape');
  await page.getByRole('tooltip').waitFor({ state: 'hidden' });
  await parent.focus();
  await page.getByRole('tooltip').waitFor();
  await parent.press('Enter');
  await page.getByRole('heading', { level: 1, name: 'Inventory Management', exact: true }).waitFor();
  checks.push('Lien de fiche réel : survol, focus, Échap, Entrée et publication conservée.');

  // Future vocabulary is exercised through a browser-only fixture, never a local release.
  const fixture = structuredClone(raw);
  fixture.glossary = { terms: [
    { id: 'QA_PRODUCT', name: 'Product', short_description: 'Référence commune d’un produit, déclinable en variantes.', definition: 'Donnée de test : un produit possède des [unités physiques](glossary:QA_UNIT#definition).', source_refs: [], review: { state: 'proposed', note: 'Donnée de test, non publiée.' } },
    { id: 'QA_UNIT', name: 'Product Unit', short_description: 'Exemplaire physique individuel d’un produit, avec son identité propre.', definition: 'Donnée de test : consulter [Inventory Tracking](model:D01.f#definition).', source_refs: [], review: { state: 'proposed' } },
  ] };
  fixture.nodes.find(n => n.id === 'D01.f').fields.definition = 'Donnée de test : suivre les [unités physiques](glossary:QA_UNIT#definition). La [notion absente](glossary:QA_MISSING) reste signalée. <script>test</script>';
  await page.route('**/api/model*', async route => route.fulfill({ json: fixture }));
  await page.goto(base + '/#node=D01.f&view=sheet');
  const inline = page.locator('.business-copy').getByRole('link', { name: 'unités physiques' });
  await inline.hover();
  const tooltip = page.getByRole('tooltip');
  await tooltip.waitFor();
  assert.ok((await tooltip.innerText()).includes(fixture.glossary.terms[1].short_description));
  await tooltip.hover();
  assert.equal(await tooltip.isVisible(), true);
  assert.equal(await page.locator('.unresolved-reference').count(), 1);
  assert.ok((await page.locator('.business-sheet').innerText()).includes('<script>test</script>'));
  await inline.click();
  await page.getByRole('heading', { level: 1, name: 'Glossaire', exact: true }).waitFor();
  await page.getByRole('heading', { level: 2, name: 'Product Unit', exact: true }).waitFor();
  assert.ok(page.url().includes('term=QA_UNIT'));
  assert.ok(page.url().includes('section=definition'));
  assert.ok(page.url().includes('version=' + raw.version));
  await page.waitForFunction(() => document.activeElement?.id === 'term-QA_UNIT-definition');
  await page.reload();
  await page.getByRole('heading', { level: 2, name: 'Product Unit', exact: true }).waitFor();
  const reverse = page.locator('.glossary-term').getByRole('link', { name: 'Inventory Tracking' });
  await reverse.click();
  await page.waitForFunction(() => document.activeElement?.id === 'field-D01.f-definition');
  checks.push('Fixture : lien lexical, ancre après rechargement, retour vers une fiche, référence absente et texte sûr.');
  await page.getByRole('button', { name: 'Glossaire', exact: true }).click();
  await page.getByRole('textbox', { name: 'Rechercher dans le glossaire' }).fill('individuel');
  assert.equal(await page.locator('.glossary-index li').count(), 1);
  await page.locator('.glossary-index').getByRole('link', { name: 'Product Unit', exact: true }).click();
  await page.locator('.glossary-index').getByRole('link', { name: 'Product', exact: true }).hover();
  await page.getByRole('tooltip').waitFor();
  await page.screenshot({ path: fileURLToPath(new URL('fixture-desktop.png', output)), fullPage: true });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.locator('.glossary-index').getByRole('link', { name: 'Product', exact: true }).click();
  await page.locator('.glossary-term').getByRole('link', { name: 'unités physiques' }).focus();
  await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
  await page.getByRole('tooltip').waitFor();
  const box = await page.getByRole('tooltip').boundingBox();
  assert.ok(box.x >= 0 && box.x + box.width <= 391 && box.y >= 0 && box.y + box.height <= 845);
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
  await page.screenshot({ path: fileURLToPath(new URL('fixture-mobile.png', output)) });
  checks.push('Fixture : recherche par définition, mobile sans débordement et infobulle dans le viewport.');
  assert.deepEqual(errors, []);
  await writeFile(new URL('browser-checks.json', output), JSON.stringify({ publication: raw.version, checks, errors, fixture_is_published: false }, null, 2));
  console.log(JSON.stringify({ checks, errors }, null, 2));
} finally { await browser.close(); }

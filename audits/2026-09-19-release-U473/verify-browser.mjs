// Recette en lecture seule contre la publication réellement servie.
import { createRequire } from 'node:module';
import { writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
const require = createRequire(import.meta.url);
const { chromium } = require('C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const version = '2026-09-19.6', checks = [], errors = [], base = 'http://127.0.0.1:8765';
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
  page.setDefaultTimeout(12000);
  page.on('pageerror', error => errors.push(error.message));
  const go = async hash => {
    await page.goto(`${base}/#${hash}`);
    await page.locator('#page-title').waitFor();
  };
  await go('node=universe-supply&view=map');
  await page.locator('.capabilities-canvas').waitFor();
  assert.equal(await page.locator('#page-title').innerText(), 'Supply Chain Orchestration');
  assert.equal(await page.locator('[data-tree-id="universe-case"]').count(), 0);
  assert.equal(await page.getByRole('button', { name: 'Informations métier', exact: true }).count(), 0);
  const overviewLink = page.locator('.capabilities-canvas a.model-reference[href*="node=D04.j"]').first();
  await overviewLink.hover();
  await page.locator('.tooltip-behaviors li').first().waitFor();
  await page.keyboard.press('Escape');
  await page.screenshot({ path: fileURLToPath(new URL('v013-base.png', import.meta.url)) });
  checks.push('Publication courante : Supply seul univers ; aperçu des comportements au survol.');

  await go(`version=${version}&node=universe-supply&view=sheet`);
  await page.locator('.business-sheet').waitFor();
  assert.match(await page.locator('[id="field-universe-supply-definition"]').innerText(), /Décider quels produits fournir/);
  const supplyTerm = page.locator('.business-sheet a[href*="term=TER084"]').first();
  await supplyTerm.hover();
  await page.getByRole('tooltip').waitFor();
  assert.match(await page.getByRole('tooltip').innerText(), /Chaîne d’approvisionnement/);
  await page.keyboard.press('Escape');
  assert.match(await page.locator('[id="field-universe-supply-scope"]').innerText(), /sources de vérité/);
  const headerBefore = await page.locator('.workspace-header').boundingBox();
  await page.locator('.workspace-content').evaluate(element => { element.scrollTop = element.scrollHeight; });
  const headerAfter = await page.locator('.workspace-header').boundingBox();
  assert.equal(headerBefore.y, headerAfter.y);
  checks.push('Fiche Supply : entrée concrète, projections externes, lien glossaire et infobulle ; bandeau fixe.');

  await page.getByRole('tab', { name: 'Marché & choix', exact: true }).click();
  await page.locator('.market-source a').first().waitFor();
  assert.equal(await page.locator('.market-source a').count(), 3);
  checks.push('Univers : trois références marché publiées (CSCMP, Microsoft, Oracle).');
  await go(`version=${version}&node=BHV006&view=market`);
  await page.locator('[id="field-BHV006-market_comparisons"] .market-source a').first().waitFor();
  assert.equal(await page.locator('.market-source a').count(), 2);
  checks.push('Fiche enrichie BHV006 : deux sources distinctes accessibles.');

  await go(`version=${version}&node=D04.j&view=sheet`);
  await page.locator('[id="field-D04.j-definition"]').waitFor();
  assert.match(await page.locator('.business-sheet').innerText(), /Exemples concrets/);
  assert.equal(await page.locator('.sheet-information-list,.information-page,.status-badge,.lifecycle-badge,.source-link').count(), 0);
  checks.push('Purchase Order : exemples préservés ; catalogue information et qualifications internes masqués.');
  await go(`version=${version}&view=glossary&glossary=model&term=TER084`);
  await page.locator('[data-glossary="model"] #term-TER084').waitFor();
  assert.match(await page.locator('#term-TER084').innerText(), /Chaîne d’approvisionnement/);
  assert.equal(await page.locator('#term-TER067').count(), 0);
  await go(`version=${version}&view=glossary&glossary=meta&term=MOD012`);
  await page.locator('[data-glossary="meta"] #term-MOD012').waitFor();
  await go(`version=${version}&view=principles`);
  await page.locator('.guide-lesson').waitFor();
  assert.equal(await page.locator('.guide-topics > button').count(), 6);
  checks.push('Deux glossaires et guide du méta modèle disponibles ; TER067 retiré du courant.');

  await go('version=2026-09-19.5&node=universe-case&view=sheet');
  await page.locator('[id="field-universe-case-definition"]').waitFor();
  assert.equal(await page.locator('#page-title').innerText(), 'Business Services');
  checks.push('Historique v012 : Business Services reste consultable dans son snapshot.');
  await page.setViewportSize({ width: 390, height: 844 });
  await go(`version=${version}&node=universe-supply&view=sheet`);
  await page.locator('[id="field-universe-supply-definition"]').waitFor();
  assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
  const reading = await page.locator('.workspace-content').boundingBox();
  assert.ok(reading.height >= 120);
  await page.screenshot({ path: fileURLToPath(new URL('v013-mobile.png', import.meta.url)) });
  checks.push('Fiche Supply sur mobile : contenu disponible, sans débordement horizontal.');
  assert.deepEqual(errors, []);
  const result = { version, checks, errors };
  await writeFile(new URL('browser-verification.json', import.meta.url), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
} finally { await browser.close(); }

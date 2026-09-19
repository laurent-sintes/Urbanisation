// Headless, isolated browser fixture using the real immutable publication and guide loader.
// No listener is started and no publication or production server is modified.
import { createRequire } from 'node:module';
import { execFileSync } from 'node:child_process';
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { resolve, extname, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
import { loadPublication } from '../scripts/load-publication.mjs';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root = fileURLToPath(new URL('../', import.meta.url));
const dist = resolve(root, 'app/dist');
const output = resolve(root, 'audits/2026-09-18-modeling-guide/browser');
const python = process.env.ATLAS_PYTHON || resolve(process.env.USERPROFILE, '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe');
const current = (await loadPublication()).raw;
const old = (await loadPublication({ version: '2026-09-13.5' })).raw;
const loadGuide = version => JSON.parse(execFileSync(python, ['-X', 'utf8', '-c',
  "import json,sys;sys.path.insert(0,'app');from modeling_guide import load_modeling_guide;print(json.dumps(load_modeling_guide(version=sys.argv[1]),ensure_ascii=True))", version,
], { cwd: root, encoding: 'utf8', windowsHide: true, maxBuffer: 16 * 1024 * 1024 }));
const guideResponse = loadGuide(current.version);
const unavailable = loadGuide(old.version);
assert.equal(guideResponse.status, 'available');
assert.equal(unavailable.status, 'unavailable');
const guide = guideResponse.guide;
assert.equal(guide.lessons.length, 6);
const first = guide.lessons[0];
const ids = new Set(current.nodes.map(node => node.id));
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const errors = [], checks = [], requests = [];
let holdGuide;
let injectMissingLink = false;

try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1100 }, reducedMotion: 'reduce' });
  page.setDefaultTimeout(10000);
  page.on('pageerror', error => errors.push(error.message));
  await page.route('**/*', async route => {
    const url = new URL(route.request().url());
    requests.push(url.pathname + url.search);
    if (url.origin !== 'http://atlas.test') return route.abort();
    if (url.pathname === '/api/releases') return route.fulfill({ json: {
      current_version: current.version, versions: [current, old].map(model => ({ version: model.version, revision: model.revision })),
    } });
    if (url.pathname === '/api/model') {
      assert.ok([current.version, old.version].includes(url.searchParams.get('version')), 'Model reads must be pinned.');
      return route.fulfill({ json: url.searchParams.get('version') === old.version ? old : current });
    }
    if (url.pathname === '/api/modeling-guide') {
      const version = url.searchParams.get('version');
      assert.ok([current.version, old.version].includes(version), 'Guide reads must be pinned.');
      const response = structuredClone(version === old.version ? unavailable : guideResponse);
      if (injectMissingLink && response.guide) response.guide.lessons[0].model_links.push({ id: 'QA_NOT_IN_PUBLICATION', label: 'Référence absente de cette publication' });
      const held = holdGuide?.version === version ? holdGuide : null;
      if (held) {
        holdGuide = null;
        held.entered();
        await held.wait;
        // An aborted request may no longer be fulfillable after a version switch.
        try { await route.fulfill({ json: response }); } catch { /* Abort is expected. */ }
        held.completed();
        return;
      }
      return route.fulfill({ json: response });
    }
    if (url.pathname.startsWith('/api/')) return route.fulfill({ status: 404, json: { error: 'Unexpected fixture endpoint' } });
    const path = resolve(dist, '.' + (url.pathname === '/' ? '/index.html' : decodeURIComponent(url.pathname)));
    if (!path.startsWith(dist + sep)) return route.abort();
    try {
      return await route.fulfill({ body: await readFile(path), contentType: ({ '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.png': 'image/png', '.svg': 'image/svg+xml', '.webmanifest': 'application/manifest+json' })[extname(path)] || 'application/octet-stream' });
    } catch { return route.fulfill({ status: 404, body: 'Not found' }); }
  });

  const visit = async params => page.goto('http://atlas.test/#' + new URLSearchParams({ version: current.version, ...params }));
  const nav = page.getByRole('navigation', { name: 'Choisir un principe' });
  const currentLesson = lesson => page.getByRole('heading', { name: lesson.title, exact: true });
  const settle = () => page.evaluate(() => new Promise(done => requestAnimationFrame(() => requestAnimationFrame(done))));

  await visit({ view: 'sheet', node: 'D03.a' });
  await page.getByTestId('business-sheet').waitFor();
  await page.getByRole('button', { name: 'Les clés du modèle', exact: true }).click();
  await currentLesson(first).waitFor();
  assert.equal(await nav.getByRole('button').count(), 6);
  assert.equal(new URL(page.url()).hash.includes('view=principles'), true);
  assert.equal(await page.getByRole('heading', { level: 1, name: 'Les clés du modèle', exact: true }).count(), 1);
  checks.push('Entrée depuis la fiche : six clés, vue dédiée et publication conservée.');

  const business = await page.locator('.guide-business').innerText();
  const realizations = new Set();
  for (const label of ['Brique dédiée', 'Mutualisation', 'Services distribués']) {
    const button = page.getByRole('button', { name: label, exact: true });
    await button.click();
    assert.equal(await button.getAttribute('aria-pressed'), 'true');
    assert.equal(await page.locator('.guide-business').innerText(), business);
    realizations.add(await page.locator('.guide-realizations').innerText());
  }
  assert.equal(realizations.size, 3);
  await page.screenshot({ path: resolve(output, 'desktop-business-solution.png'), fullPage: true });
  checks.push('Trois réalisations techniques différentes ; responsabilités métier inchangées.');

  for (let i = 0; i < guide.lessons.length; i++) {
    const lesson = guide.lessons[i];
    await nav.getByRole('button').nth(i).click();
    await currentLesson(lesson).waitFor();
    assert.equal(await nav.getByRole('button').nth(i).getAttribute('aria-pressed'), 'true');
    assert.ok(page.url().includes('principle=' + lesson.id));
    assert.equal(await page.locator('.guide-choices button').count(), 2);
    const feedback = page.locator('.guide-answer');
    assert.equal(await feedback.innerText(), '', 'Another principle must not retain the previous answer.');
    for (let choice = 0; choice < 2; choice++) {
      await page.locator('.guide-choices button').nth(choice).click();
      assert.equal(await page.locator('.guide-choices button').nth(choice).getAttribute('aria-pressed'), 'true');
      assert.ok((await feedback.innerText()).includes(lesson.choices[choice].feedback));
    }
    const summary = page.locator('summary').filter({ hasText: /^Pour contribuer/ });
    await summary.click();
    const contributor = summary.locator('..');
    assert.ok((await contributor.innerText()).includes(lesson.contributor.criterion));
    assert.ok((await contributor.innerText()).includes(lesson.contributor.boundary));
    assert.ok((await contributor.innerText()).includes(lesson.contributor.scope));
    const sourceSummary = page.locator('summary').filter({ hasText: /^Sources et portée/ });
    await sourceSummary.click();
    const sources = sourceSummary.locator('..');
    for (const id of lesson.contributor.source_refs) {
      const source = guide.sources.find(item => item.id === id);
      assert.ok(source);
      assert.ok((await sources.innerText()).includes(source.excerpt));
      assert.ok((await sources.innerText()).includes(source.scope));
    }
    for (const link of await page.locator('.guide-model-links a').all()) {
      const href = await link.getAttribute('href');
      const params = new URLSearchParams(new URL(href, page.url()).hash.slice(1));
      assert.equal(params.get('version'), current.version);
      assert.ok(ids.has(params.get('node')));
    }
  }
  checks.push('Six sujets : chaque choix a son explication, approfondissement et extraits de sources figés. Tous les liens restent dans le snapshot affiché.');

  await visit({ view: 'principles', principle: first.id });
  await currentLesson(first).waitFor();
  await page.getByRole('button', { name: 'Voir directement l’explication', exact: true }).click();
  assert.ok((await page.locator('.guide-answer').innerText()).includes(first.explanation));
  checks.push('L’explication est accessible directement, sans réponse obligatoire.');

  const availableLesson = guide.lessons.find(lesson => lesson.model_links.some(link => ids.has(link.id)));
  assert.ok(availableLesson, 'The guide should include at least one actual publication link.');
  await visit({ view: 'principles', principle: availableLesson.id });
  await currentLesson(availableLesson).waitFor();
  await page.locator('summary').filter({ hasText: /^Pour contribuer/ }).click();
  const modelLink = page.locator('.guide-model-links a').first();
  await modelLink.click();
  await page.getByTestId('business-sheet').waitFor();
  assert.ok(page.url().includes('version=' + current.version));
  await page.goBack();
  await currentLesson(availableLesson).waitFor();
  checks.push('Lien vers une fiche puis retour navigateur : principe et version retrouvés.');

  injectMissingLink = true;
  await visit({ view: 'principles', principle: first.id });
  await page.reload();
  await currentLesson(first).waitFor();
  assert.equal(await page.getByRole('link', { name: 'Référence absente de cette publication', exact: true }).count(), 0);
  injectMissingLink = false;
  checks.push('Une référence absente du snapshot n’est jamais transformée en lien ni cherchée dans le backlog.');

  await nav.getByRole('button').nth(1).focus();
  await page.keyboard.press('Enter');
  await currentLesson(guide.lessons[1]).waitFor();
  await page.locator('.guide-choices button').first().focus();
  await page.keyboard.press('Space');
  assert.ok((await page.locator('.guide-answer').innerText()).includes(guide.lessons[1].choices[0].feedback));
  const contributorSummary = page.locator('summary').filter({ hasText: /^Pour contribuer/ });
  await contributorSummary.focus();
  await page.keyboard.press('Space');
  assert.equal(await contributorSummary.locator('..').getAttribute('open'), '');
  checks.push('Clavier : sélection d’une clé, réponse et ouverture de l’approfondissement.');

  for (const width of [390, 320]) {
    await page.setViewportSize({ width, height: 844 });
    for (const lesson of guide.lessons) {
      await visit({ view: 'principles', principle: lesson.id });
      await currentLesson(lesson).waitFor();
      await page.getByRole('button', { name: 'Voir directement l’explication', exact: true }).click();
      await page.locator('summary').filter({ hasText: /^Pour contribuer/ }).click();
      await page.locator('summary').filter({ hasText: /^Sources et portée/ }).click();
      await settle();
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `Horizontal overflow at ${width}px: ${lesson.id}`);
    }
    await page.screenshot({ path: resolve(output, `mobile-${width}-sources.png`), fullPage: true, style: '.topbar { visibility: hidden !important; }' });
    await visit({ view: 'principles', principle: first.id });
    await currentLesson(first).waitFor();
    await page.getByRole('button', { name: 'Services distribués', exact: true }).click();
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.screenshot({ path: resolve(output, `mobile-${width}.png`) });
    await page.locator('.guide-technical-scene').screenshot({ path: resolve(output, `mobile-${width}-business-solution.png`), style: '.topbar { visibility: hidden !important; }' });
  }
  checks.push('Mobile 390 px et 320 px : les six clés, explications et sources ne débordent pas horizontalement.');

  await page.setViewportSize({ width: 1440, height: 1100 });
  await visit({ version: old.version, view: 'principles', principle: first.id });
  await page.getByText(unavailable.message, { exact: true }).waitFor();
  assert.equal(await nav.count(), 0);
  assert.equal(await currentLesson(first).count(), 0);
  await page.screenshot({ path: resolve(output, 'historical-unavailable.png'), fullPage: true });
  checks.push('Publication historique sans association : guide explicitement indisponible, aucun repli courant ou backlog.');

  let release, entered, completed;
  const waiting = new Promise(done => { release = done; });
  const requested = new Promise(done => { entered = done; });
  const finished = new Promise(done => { completed = done; });
  holdGuide = { version: current.version, wait: waiting, entered, completed };
  await visit({ version: current.version, view: 'principles', principle: first.id });
  await requested;
  await visit({ version: old.version, view: 'principles', principle: first.id });
  await page.getByText(unavailable.message, { exact: true }).waitFor();
  release();
  await finished;
  await settle();
  assert.equal(await nav.count(), 0);
  assert.equal(await page.getByText(unavailable.message, { exact: true }).isVisible(), true);
  checks.push('Changement de version pendant une réponse lente : la réponse précédente ne remplace pas le guide historique.');

  await visit({ version: '', view: 'principles', principle: first.id });
  await currentLesson(first).waitFor();
  assert.ok(requests.includes('/api/modeling-guide?version=' + current.version));
  assert.ok(!requests.some(url => url.includes('backlog') || url.startsWith('/api/source')));
  assert.deepEqual(errors, []);
  const result = { status: 'passed', publication: current.version, guide: guide.version, checks, errors, fixture_only: true };
  await writeFile(resolve(output, 'checks.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
} finally { await browser.close(); }

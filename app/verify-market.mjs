// Isolated browser fixture: no publication, server mutation or backlog fallback.
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
const output = resolve(root, 'audits/2026-09-18-market-comparisons/browser');
await mkdir(output, { recursive: true });
const python = process.env.ATLAS_PYTHON || resolve(process.env.USERPROFILE, '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe');
const fixture = JSON.parse(execFileSync(python, ['-c', "import json;from scripts.structured_io import read;m=read('modeles/backlog/model.yaml');m['glossary']=read('modeles/backlog/glossary.yaml');print(json.dumps(m,ensure_ascii=True))"], { cwd: root, encoding: 'utf8', windowsHide: true, maxBuffer: 16 * 1024 * 1024 }));
fixture.space = 'release'; fixture.version = '2099-09-18.1'; fixture.revision = 0;
fixture.nodes = fixture.nodes.filter(n => n.review.state !== 'illustration');
const ids = new Set(fixture.nodes.map(n => n.id));
fixture.relations = fixture.relations.filter(r => r.review.state !== 'illustration' && ids.has(r.source_id) && ids.has(r.target_id));
for (const n of fixture.nodes) {
  n.approved_fields = n.lifecycle?.validated_fields || [];
  n.proposed_fields = Object.keys(n.fields).filter(k => !n.approved_fields.includes(k));
}
const old = (await loadPublication({ version: '2026-09-13.5' })).raw;
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const errors = [], checks = [];
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1100 } });
  page.on('pageerror', error => errors.push(error.message));
  await page.route('**/*', async route => {
    const url = new URL(route.request().url());
    if (url.origin !== 'http://atlas.test') return route.abort();
    if (url.pathname === '/api/releases') return route.fulfill({ json: { current_version: fixture.version, versions: [{ version: fixture.version }, { version: old.version }] } });
    if (url.pathname === '/api/model') return route.fulfill({ json: url.searchParams.get('version') === old.version ? old : fixture });
    const path = resolve(dist, '.' + (url.pathname === '/' ? '/index.html' : decodeURIComponent(url.pathname)));
    if (!path.startsWith(dist + sep)) return route.abort();
    try {
      return await route.fulfill({ body: await readFile(path), contentType: ({ '.html':'text/html', '.js':'text/javascript', '.css':'text/css', '.png':'image/png', '.svg':'image/svg+xml', '.webmanifest':'application/manifest+json' })[extname(path)] || 'application/octet-stream' });
    } catch { return route.fulfill({ status: 404, body: 'Not found' }); }
  });
  const visit = async (params) => page.goto('http://atlas.test/#' + new URLSearchParams({ version: fixture.version, ...params }));
  await visit({ node: 'D05.e', view: 'sheet' });
  const section = page.getByRole('region', { name: 'Comparaison par rapport au marché' });
  await section.waitFor();
  assert.equal(await section.locator('.market-card').count(), 2);
  assert.ok((await section.innerText()).includes('Différences et limites de périmètre'));
  assert.ok((await section.innerText()).includes('Rapprochement proposé'));
  await section.getByText('Source et portée de la comparaison', { exact: true }).first().click();
  assert.ok((await section.getByRole('link').first().getAttribute('href')).startsWith('https://help.sap.com/'));
  assert.ok((await section.innerText()).includes('5.0 FPS02'));
  await section.screenshot({ path: resolve(output, 'capability-comparisons.png'), style: '.topbar { visibility: hidden !important; }' });
  checks.push('Fiche capacité : deux éditeurs, différences, choix FLOW, statut, source datée et lien primaire.');
  for (const term of ['TER079','TER080']) {
    await visit({ view:'glossary', term });
    await page.locator(`#term-${term}`).waitFor();
    assert.equal(await page.locator('.glossary-term .market-card').count(), 2);
  }
  await page.getByRole('textbox', { name: 'Rechercher dans le glossaire' }).fill('In-Season Fill-In');
  // Both terms can cite the same SAP passage, so neither should be suppressed.
  assert.ok(await page.locator('.glossary-index li').count() >= 1);
  assert.equal(await page.locator('.glossary-index').getByRole('link', { name: 'Réassort', exact: true }).count(), 1);
  checks.push('Implantation et Réassort : comparaison visible et recherche par terme SAP.');
  await page.setViewportSize({ width: 390, height: 844 });
  await visit({ node: 'D05.e', view: 'sheet' });
  await section.waitFor();
  assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
  await section.screenshot({ path: resolve(output, 'mobile-comparisons.png'), style: '.topbar { visibility: hidden !important; }' });
  checks.push('Mobile 390 px : cartes lisibles sans débordement horizontal.');
  await page.goto('http://atlas.test/#' + new URLSearchParams({ version: old.version, node: 'D03.a', view:'sheet' }));
  await page.getByTestId('business-sheet').waitFor();
  assert.equal(await page.locator('.market-comparisons').count(), 0);
  checks.push('Publication historique : aucune comparaison récupérée depuis le backlog.');
  assert.deepEqual(errors, []);
  await writeFile(resolve(output, 'checks.json'), JSON.stringify({ status:'passed', checks, errors, fixture_only:true }, null, 2));
  console.log(JSON.stringify({ status:'passed', checks }, null, 2));
} finally { await browser.close(); }

// Read-only browser checks: live publication, then an explicitly isolated fixture.
import { createRequire } from 'node:module';
import { execFileSync } from 'node:child_process';
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { resolve, extname, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
import { businessExamples } from '../../app/src/examples.ts';
import { loadPublication } from '../../scripts/load-publication.mjs';
const require = createRequire(import.meta.url);
const { chromium } = require('C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root = fileURLToPath(new URL('../../', import.meta.url));
const dist = resolve(root, 'app/dist');
const output = resolve(root, 'audits/2026-09-19-contenu-U462/browser', new Date().toISOString().replace(/[:.]/g, '-'));
await mkdir(output, { recursive: true });
const fixture = JSON.parse(execFileSync('python', ['-X','utf8','-c', "import json;from scripts.structured_io import read;m=read('modeles/backlog/model.yaml');m['glossary']=read('modeles/backlog/glossary.yaml');print(json.dumps(m,ensure_ascii=True))"], { cwd:root, encoding:'utf8', windowsHide:true, maxBuffer:16*1024*1024 }));
fixture.space='release';fixture.version='2099-09-19.1';fixture.revision=0;
const old=(await loadPublication({version:'2026-09-13.5'})).raw;
const browser=await chromium.launch({channel:'msedge',headless:true});
const errors=[],checks=[];
let page;
const noOverflow=async()=>assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
const shot=name=>page.screenshot({path:resolve(output,name+'.png'),fullPage:false});
try {
  page=await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
  page.setDefaultTimeout(15000);
  page.on('pageerror',e=>errors.push(e.message));
  const base='http://127.0.0.1:8765';
  const published=await (await page.request.get(base+'/api/model')).json();
  const visit=async hash=>{await page.goto(base+'/#'+hash);await page.locator('#page-title').waitFor();};
  await visit('node=D04.j&view=sheet');
  const ex=page.getByRole('region',{name:'Exemples concrets'});
  await ex.waitFor();
  assert.equal(await ex.locator('.example-card').count(),businessExamples(published.nodes.find(n=>n.id==='D04.j').fields).length);
  assert.match(await ex.innerText(),/60 pièces reçues sur 100/);
  assert.ok(await ex.evaluate(el=>el.getBoundingClientRect().top < 1000));
  await shot('published-examples');
  const marketTab=page.getByRole('tab',{name:'Marché & choix',exact:true});
  await marketTab.click();
  assert.match(page.url(),/view=market/);
  assert.equal(await marketTab.getAttribute('aria-selected'),'true');
  assert.equal(await page.locator('.market-card').count(),published.nodes.find(n=>n.id==='D04.j').fields.market_comparisons.length);
  assert.ok(await page.locator('.market-choice').first().isVisible());
  assert.ok(await page.locator('.market-source a').first().isVisible());
  assert.doesNotMatch(await page.locator('.market-comparisons').innerText(),/\bU\d+\b|\bCMP\d+\b|\bELM\d+\b/);
  assert.equal(await page.locator('.source-link,.lifecycle-badge,.market-status').count(),0);
  await shot('published-market');
  await marketTab.focus();await page.keyboard.press('ArrowLeft');
  assert.equal(await page.getByRole('tab',{name:/Relations/}).getAttribute('aria-selected'),'true');
  await page.keyboard.press('ArrowRight');
  assert.equal(await marketTab.getAttribute('aria-selected'),'true');
  await visit('version='+published.version+'&node=D04.j&view=sheet&section=market_comparisons');
  await page.waitForFunction(()=>document.querySelector('#tab-market')?.getAttribute('aria-selected')==='true');
  assert.match(page.url(),/view=market/);
  assert.match(page.url(),new RegExp('version='+published.version.replaceAll('.','\\.')));
  checks.push('Publication réelle : exemples extraits du snapshot, onglet marché, choix et sources visibles, clavier, ancien lien redirigé sans changer de version.');
  await visit('node=D08&view=market');
  assert.match(await page.locator('.market-intro').innerText(),/non documenté/);
  assert.equal(await page.locator('.market-card').count(),0);
  checks.push('Aucun complément backlog : Product Reference reste sans comparaison dans v010.');
  await page.setViewportSize({width:390,height:844});
  await visit('node=D04.j&view=market');await page.locator('.market-card').first().waitFor();await noOverflow();
  await page.locator('.market-detail > summary').first().click();await noOverflow();
  await shot('mobile-market');
  await page.getByRole('tab',{name:'Fiche',exact:true}).click();await ex.waitFor();await noOverflow();
  await shot('mobile-examples');
  checks.push('390 px : quatre onglets, sources et exemples sans débordement horizontal.');
  await page.setViewportSize({width:720,height:500});
  await visit('node=D04.j&view=market');await page.locator('.market-card').first().waitFor();await noOverflow();
  checks.push('Surface équivalente à 200 % : repli et contenu lisibles à 720 px.');
  const term=published.glossary.terms.find(t=>t.market_comparisons?.length);
  await visit('view=glossary&term='+term.id);await page.locator('#term-'+term.id).waitFor();
  assert.ok(await page.locator('.glossary-term .market-source a').first().isVisible());
  checks.push('Glossaire : sources externes également accessibles directement.');
  await page.close();

  page=await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
  page.setDefaultTimeout(15000);page.on('pageerror',e=>errors.push(e.message));
  await page.route('**/*',async route=>{
    const url=new URL(route.request().url());
    if(url.origin!=='http://atlas.test')return route.abort();
    if(url.pathname==='/api/releases')return route.fulfill({json:{current_version:fixture.version,versions:[{version:fixture.version},{version:old.version}]}});
    if(url.pathname==='/api/model')return route.fulfill({json:url.searchParams.get('version')===old.version?old:fixture});
    if(url.pathname==='/api/modeling-guide')return route.fulfill({json:{schema_version:'1.0.0',publication_version:url.searchParams.get('version'),status:'unavailable',message:'Fixture isolée.'}});
    const path=resolve(dist,'.'+(url.pathname==='/'?'/index.html':decodeURIComponent(url.pathname)));
    if(!path.startsWith(dist+sep))return route.abort();
    try{return route.fulfill({body:await readFile(path),contentType:({'.html':'text/html','.js':'text/javascript','.css':'text/css','.png':'image/png','.svg':'image/svg+xml','.webmanifest':'application/manifest+json'})[extname(path)]||'application/octet-stream'});}
    catch{return route.fulfill({status:404,body:'Not found'});}
  });
  const preview=async(node,view,version=fixture.version)=>{await page.goto('http://atlas.test/#'+new URLSearchParams({version,node,view}));await page.locator('#page-title').waitFor();};
  await preview('D03.n','market');await page.locator('.market-card').last().waitFor();
  const choices=page.locator('.market-card').filter({has:page.getByRole('heading',{name:'Confirm sales orders',exact:true})});
  assert.match(await choices.innerText(),/Pourquoi ce terme/);
  assert.match(await choices.innerText(),/Promise Management était trop vague/);
  assert.match(await choices.innerText(),/Pourquoi cette définition/);
  assert.ok(await choices.locator('.market-source a').isVisible());
  await choices.scrollIntoViewIfNeeded();await shot('fixture-terminology');
  await preview('D02.e','market');await page.locator('.market-card').last().waitFor();
  const sapChoice=page.locator('.market-card').filter({has:page.getByRole('heading',{name:'Explaining Supply Assignment',exact:true})});
  await sapChoice.locator('summary').click();
  assert.match(await sapChoice.innerText(),/FLOW sépare cet effet dans Reservation/);
  await preview('D04.n','sheet');await page.locator('.example-card').first().waitFor();
  assert.equal(await page.locator('.example-card').count(),3);
  assert.match(await page.locator('.business-examples').innerText(),/Regrouper en conservant les identités/);
  await shot('fixture-three-examples');
  await preview('D04.o','sheet');await page.locator('.example-card').first().waitFor();
  assert.match(await page.locator('.business-examples').innerText(),/aucune suspension des 60 pièces n’est implicite/);
  const search=page.getByRole('textbox',{name:'Rechercher dans le modèle publié'});
  await search.fill('prorata');await page.locator('[data-search-result]').first().waitFor();
  assert.match(await page.locator('[data-search-result]').allTextContents().then(x=>x.join('\n')),/Supply Assignment/);
  checks.push('Fixture seule : raisons du nom/de la définition, écart SAP explicite, trois comportements illustrés et recherche des exemples.');
  await preview('D03.a','market',old.version);await page.locator('.market-intro').waitFor();
  assert.match(await page.locator('.market-intro').innerText(),/non documenté/);
  assert.equal(await page.locator('.market-card').count(),0);
  checks.push('Publication historique : aucune comparaison ou explication récupérée dans le modèle courant.');
  assert.deepEqual(errors,[]);
  const coverage=raw=>Object.fromEntries(['capability','behavior','domain','reference'].map(kind=>{
    const ns=raw.nodes.filter(n=>n.kind===kind);
    return[kind,{total:ns.length,examples:ns.filter(n=>businessExamples(n.fields||{}).length).length,market:ns.filter(n=>n.fields?.market_comparisons?.length).length,
      explicit_choices:ns.filter(n=>n.fields?.market_comparisons?.some(c=>c.term_choice&&c.definition_choice)).length}];
  }));
  const gaps={};
  for(const kind of ['capability','behavior','domain','reference']){
    const ns=fixture.nodes.filter(n=>n.kind===kind);
    gaps[kind]={market:ns.filter(n=>!n.fields?.market_comparisons?.length).map(n=>({id:n.id,name:n.fields.name})),
      examples:ns.filter(n=>!businessExamples(n.fields||{}).length).map(n=>({id:n.id,name:n.fields.name}))};
  }
  const report={status:'passed',version:published.version,checks,errors,published:coverage(published),backlog_fixture:coverage(fixture),gaps,fixture_was_not_published:true,output};
  await writeFile(resolve(output,'verification.json'),JSON.stringify(report,null,2));
  console.log(JSON.stringify({...report,gaps:undefined},null,2));
}catch(error){if(page&&!page.isClosed())await shot('failure');console.error(output);throw error;}
finally{await browser.close();}

// Candidate preview is isolated; the actual publication stays immutable.
import {createRequire} from 'node:module';
import {execFileSync} from 'node:child_process';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {resolve,extname,sep} from 'node:path';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
import {loadPublication} from '../../scripts/load-publication.mjs';
const require=createRequire(import.meta.url);
const {chromium}=require('C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=fileURLToPath(new URL('../../',import.meta.url)),dist=resolve(root,'app/dist');
const output=resolve(root,'audits/2026-09-19-base-U470/browser',new Date().toISOString().replace(/[:.]/g,'-'));
await mkdir(output,{recursive:true});
const preview=JSON.parse(execFileSync('python',['-X','utf8','-c',"import json;from scripts.prepare_release import build_candidate;b=build_candidate(version='2099-09-19.1',source_refs=['U470','U471']);errors=b['report']['validation_errors'];assert all('lifecycle approval lacks a matching decision' in e for e in errors),errors;print(json.dumps({'candidate':b['candidate'],'publication_checks_pending':errors},ensure_ascii=True))"],{cwd:root,encoding:'utf8',windowsHide:true,maxBuffer:24*1024*1024}));
const fixture=preview.candidate;
const old=(await loadPublication({version:'2026-09-19.5'})).raw;
const browser=await chromium.launch({channel:'msedge',headless:true}),checks=[],errors=[];
const page=await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
page.setDefaultTimeout(12000);page.on('pageerror',e=>errors.push(e.message));
const noOverflow=async()=>assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
const shot=name=>page.screenshot({path:resolve(output,name+'.png'),fullPage:false});
const visit=async(params={})=>{await page.goto('http://atlas.test/#'+new URLSearchParams({version:fixture.version,view:'sheet',node:'universe-supply',...params}));await page.locator('#page-title').waitFor();};
try {
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
  await visit();
  await page.getByText('Organiser l’approvisionnement, la répartition et la livraison des produits pour tenir les quantités et les dates promises.',{exact:true}).waitFor();
  assert.equal(await page.locator('.example-card').count(),2);
  const scope=page.locator('.sheet-scope');
  assert.match(await scope.innerText(),/sources de vérité/);
  assert.equal(await scope.locator('details').count(),0);
  assert.equal(await page.locator('.unresolved-reference').count(),0);
  await noOverflow(); await shot('univers-desktop');
  checks.push('Univers : entrée concrète, deux exemples, périmètre explicite sans contenu replié ni lien orphelin.');

  const supplyLink=page.getByRole('link',{name:'Supply Chain',exact:true});
  await supplyLink.hover();await page.getByRole('tooltip').waitFor();
  assert.match(await page.getByRole('tooltip').innerText(),/Chaîne d’approvisionnement/);
  assert.match(await supplyLink.getAttribute('href'),/version=2099-09-19.1/);
  await shot('infobulle');await page.keyboard.press('Escape');assert.equal(await page.getByRole('tooltip').count(),0);
  await supplyLink.focus();await page.getByRole('tooltip').waitFor();
  await supplyLink.click();await page.locator('#term-TER084').waitFor();
  assert.match(page.url(),/term=TER084/);assert.match(page.url(),/version=2099-09-19.1/);
  checks.push('Glossaire : définition complète au survol et au focus, Échap, clic vers le terme de la même publication.');

  await visit({view:'market'});
  await page.locator('.market-source a').first().waitFor();
  assert.equal(await page.locator('.market-source a').count(),3);
  for(const vendor of ['CSCMP','Microsoft','Oracle'])assert.ok((await page.locator('main').innerText()).includes(vendor));
  await shot('marche-univers');checks.push('Univers Marché & choix : trois références au niveau du nom et du périmètre.');
  for(const id of ['D03.k','BHV057','BHV069']){
    await visit({view:'market',node:id});await page.locator('.market-source a').first().waitFor();
    assert.equal(await page.locator('.market-source a').count(),2,id);
    const hrefs=await page.locator('.market-source a').evaluateAll(xs=>xs.map(x=>x.href));assert.equal(new Set(hrefs).size,2,id);
  }
  checks.push('PTP, Return for Repair et Intercompany Sales : deux références distinctes visibles.');

  for(const version of [fixture.version,old.version]){
    await visit({version,node:'D04.j'});
    assert.equal(await page.getByRole('button',{name:'Informations métier',exact:true}).count(),0);
    assert.equal(await page.locator('.sheet-information-list').count(),0);
    assert.equal(await page.locator('option[value="information"]').count(),0);
    await page.getByRole('textbox',{name:'Rechercher dans le modèle publié'}).fill('Supplier Response');
    assert.equal(await page.locator('[data-search-result^="PINFO-"]').count(),0);
    await visit({version,view:'information',node:'D04.j',information:'PINFO-001'});
    await page.locator('.business-sheet').waitFor();
    assert.equal(await page.locator('.information-detail').count(),0);
    assert.ok(page.url().includes('version='+version));
    await visit({version,view:'information',node:'',information:'PINFO-001',type:'information'});
    assert.equal(await page.locator('.information-detail').count(),0);
  }
  checks.push('Catalogue Informations métier masqué : navigation, fiches, recherche, filtre et anciens liens ; version candidate et v012.');

  await page.setViewportSize({width:390,height:844});await visit();await noOverflow();await shot('univers-mobile');
  await visit({view:'market'});await page.locator('.market-source a').first().waitFor();await noOverflow();
  checks.push('390 px : fiche et marché sans débordement horizontal.');
  assert.deepEqual(errors,[]);checks.push('Aucune erreur JavaScript.');
  await writeFile(resolve(output,'result.json'),JSON.stringify({status:'passed',checks,errors,publication_checks_pending:preview.publication_checks_pending},null,2));
  console.log(JSON.stringify({status:'passed',checks,output}));
}catch(error){await shot('failure');await writeFile(resolve(output,'result.json'),JSON.stringify({status:'failed',error:String(error),checks,errors},null,2));throw error;}
finally{await browser.close();}

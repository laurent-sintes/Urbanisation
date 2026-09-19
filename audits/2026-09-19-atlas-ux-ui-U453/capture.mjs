import { createRequire } from 'node:module';
import { writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
const require = createRequire(import.meta.url);
const { chromium } = require('C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = 'http://127.0.0.1:8765';
const browser = await chromium.launch({channel:'msedge',headless:true});
const findings={capturedAt:new Date().toISOString(), viewport:{width:1440,height:900}, pages:[], searches:[], errors:[]};
try {
 const page=await browser.newPage({viewport:findings.viewport,reducedMotion:'reduce'});
 page.on('pageerror',e=>findings.errors.push(e.message));
 const raw=await (await page.request.get(base+'/api/model')).json();
 findings.version=raw.version;
 if(raw.version!=='2026-09-19.3') throw new Error('Publication différente : '+raw.version);
 async function capture(name,hash,wait='.page-heading') {
  await page.goto(base+'/'+hash); await page.locator(wait).first().waitFor();
  await page.waitForTimeout(600);
  await page.screenshot({path:fileURLToPath(new URL(name+'.png',import.meta.url)),fullPage:true});
  const data=await page.evaluate(()=>{
   const rect=el=>{const r=el.getBoundingClientRect();return {x:Math.round(r.x),y:Math.round(r.y),width:Math.round(r.width),height:Math.round(r.height)}};
   const css=el=>{const c=getComputedStyle(el);return {color:c.color,background:c.backgroundColor,font:c.fontSize,weight:c.fontWeight}};
   return {url:location.href,title:document.querySelector('#page-title')?.textContent,bodyHeight:document.documentElement.scrollHeight,bodyWidth:document.documentElement.scrollWidth,headings:[...document.querySelectorAll('main h1,main h2,main h3')].map(el=>({text:el.textContent,...rect(el)})),mainText:document.querySelector('main')?.innerText,controls:[...document.querySelectorAll('button,select,input')].filter(el=>el.getBoundingClientRect().width>0).map(el=>({name:el.getAttribute('aria-label')||el.textContent?.slice(0,90),...rect(el)})),styles:['.page-heading h1','.page-heading p','.business-card h3','.business-card p','.section-kicker','.detail-muted','.tree-label','.model-reference','.dependency-legend'].map(sel=>{const el=document.querySelector(sel);return el?{selector:sel,...css(el)}:null}).filter(Boolean)};
  });
  findings.pages.push({name,...data});
 }
 await capture('01-accueil','#view=map&scope=@root');
 await capture('02-univers','#node=universe-supply&view=map&scope=universe-supply');
 await capture('03-achat','#view=sheet&node=D04.j','.business-sheet');
 await capture('04-produit','#view=sheet&node=D08','.business-sheet');
 await capture('05-relations-achat','#view=relations&node=D04.j','.dependencies-pane');
 await capture('06-relations-globales','#view=relations','.dependencies-pane');
 await page.getByRole('button',{name:'Comprendre le méta modèle',exact:true}).click();
 await capture('07-meta',new URL(page.url()).hash,'.guide-lesson');
 await page.getByRole('button',{name:'Glossaire métier',exact:true}).click();
 await capture('08-glossaire',new URL(page.url()).hash,'.glossary-index');
 await page.goto(base+'/#view=map&scope=@root');
 for(const query of ['achat','commande fournisseur','bon de commande','purchase order','réserver','réservation','stock','projection','external','proposé']){
  await page.locator('#fa-search').fill(query);
  await page.waitForTimeout(150);
  findings.searches.push({query,results:await page.locator('[data-search-result]').evaluateAll(els=>els.map(el=>({id:el.dataset.searchResult,text:el.innerText})))});
 }
 await page.locator('#fa-search').fill('');
 await page.keyboard.press('Control+k');
 findings.ctrlKSearchFocus=await page.locator('#fa-search').evaluate(el=>document.activeElement===el);
 await page.setViewportSize({width:390,height:844});
 await capture('09-mobile-achat','#view=sheet&node=D04.j','.business-sheet');
 await page.setViewportSize({width:1280,height:720});
 await capture('10-petit-ecran','#view=sheet&node=D04.j','.business-sheet');
 await writeFile(new URL('browser-observations.json',import.meta.url),JSON.stringify(findings,null,2));
 console.log(JSON.stringify({version:findings.version,pages:findings.pages.map(p=>({name:p.name,height:p.bodyHeight,width:p.bodyWidth,headings:p.headings.filter(h=>['Périmètre','Comportements 3','Comparaison par rapport au marché','Rattachement et frontières'].includes(h.text))})),searches:findings.searches.map(s=>({query:s.query,count:s.results.length,first:s.results.slice(0,4).map(x=>x.id)})),ctrlKSearchFocus:findings.ctrlKSearchFocus,errors:findings.errors},null,2));
} finally {await browser.close();}

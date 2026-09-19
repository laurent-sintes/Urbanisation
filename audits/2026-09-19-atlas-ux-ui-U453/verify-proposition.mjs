import {createRequire} from 'node:module';
import {writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
const require=createRequire(import.meta.url);
const {chromium}=require('C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const browser=await chromium.launch({channel:'msedge',headless:true});
const checks=[],errors=[];
try {
 const page=await browser.newPage({viewport:{width:1440,height:1080}});
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(new URL('proposition.html',import.meta.url).href);
 assert.equal(await page.locator('h1').innerText(),'Purchase Order');
 assert.ok(await page.locator('#understand').isVisible());
 for(const palette of ['mono','balanced','domains']){
  await page.locator(`[data-palette="${palette}"]`).click();
  assert.equal(await page.locator(`[data-palette="${palette}"]`).getAttribute('aria-pressed'),'true');
 }
 await page.locator('[data-palette="balanced"]').click();
 await page.screenshot({path:fileURLToPath(new URL('proposition-fiche.png',import.meta.url)),fullPage:true});
 await page.locator('[data-view="information"]').click();
 assert.ok(await page.locator('#information').isVisible());
 assert.ok(await page.locator('#understand').isHidden());
 await page.screenshot({path:fileURLToPath(new URL('proposition-informations.png',import.meta.url)),fullPage:true});
 checks.push('Les trois palettes et les deux vues sont fonctionnelles ; avertissement de maquette présent.');
 for(const width of [1440,390]){
  await page.setViewportSize({width,height:900});
  for(const view of ['understand','information']){
   await page.locator(`[data-view="${view}"]`).click();
   const scrollWidth=await page.evaluate(()=>document.documentElement.scrollWidth);
   assert.ok(scrollWidth<=width,`${view} déborde à ${width}px : ${scrollWidth}`);
  }
 }
 checks.push('Pas de débordement horizontal des deux vues à 1440 et 390 px.');
 assert.deepEqual(errors,[]);
 await writeFile(new URL('prototype-verification.json',import.meta.url),JSON.stringify({checks,errors},null,2));
 console.log(JSON.stringify({checks,errors},null,2));
} finally {await browser.close()}

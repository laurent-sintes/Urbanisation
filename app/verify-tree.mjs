import { createRequire } from 'node:module';
import { mkdir } from 'node:fs/promises';
import assert from 'node:assert/strict';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.ATLAS_PLAYWRIGHT_PATH || 'C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base = process.env.ATLAS_URL || 'http://127.0.0.1:8765';
const output = path.join(path.dirname(fileURLToPath(import.meta.url)), '.runtime', 'qa-tree');
await mkdir(output, {recursive:true});
const browser = await chromium.launch({channel:'msedge',headless:true});
try {
  const page = await browser.newPage({viewport:{width:1366,height:900}}), errors=[];
  page.on('pageerror', e => errors.push(e.message));
  const item = id => page.locator(`[role="treeitem"][data-tree-id="${id}"]`);
  const title = text => page.getByRole('heading',{name:text,exact:true,level:1});
  await page.goto(base+'/#node=D02.b');
  await title('Supply Protection').waitFor();
  assert.equal(await page.locator('#fa-recent').count(),0);
  assert.equal(await page.locator('[data-go="atlas"]').count(),0);
  assert.equal(await item('process').count(),1);
  assert.equal(await item('D01').getAttribute('aria-expanded'),'true');
  assert.equal(await item('D02.b').getAttribute('aria-selected'),'true');
  assert.equal(await item('D01').locator('[data-tree-id="D02.b"]').count(),1);
  // Expanding a branch preserves the current page; selection opens it.
  await page.locator('[data-tree-toggle="D03"]').click();
  assert.equal(await item('D03').getAttribute('aria-expanded'),'true');
  await title('Supply Protection').waitFor();
  await item('D02.e').focus(); await page.keyboard.press('Enter');
  await title('Supply Assignment').waitFor();
  assert.equal(await item('D03').locator('[data-tree-id="D02.e"]').count(),1);
  assert.equal(await item('D02.e').evaluate(el=>el===document.activeElement),true);
  await page.keyboard.press('ArrowLeft');
  assert.equal(await item('D03').evaluate(el=>el===document.activeElement),true);
  await page.keyboard.press('ArrowLeft');
  assert.equal(await item('D03').getAttribute('aria-expanded'),'false');
  await page.keyboard.press('ArrowRight'); await page.keyboard.press('ArrowRight');
  assert.equal(await page.evaluate(()=>document.activeElement.dataset.treeId),'D03.a');
  await page.keyboard.press('Home'); assert.equal(await page.evaluate(()=>document.activeElement.dataset.treeId),'transactional');
  await page.keyboard.press('End'); assert.equal(await page.evaluate(()=>document.activeElement.dataset.treeId),'process');
  // Persistent expansion survives reload and search reveals the selected ancestors.
  await page.locator('[data-tree-toggle="business-references"]').click();
  await page.reload(); await title('Supply Assignment').waitFor();
  assert.equal(await item('business-references').getAttribute('aria-expanded'),'true');
  await page.locator('#fa-search').fill('D01.g');
  await page.keyboard.press('ArrowDown');
  assert.equal(await page.evaluate(()=>document.activeElement.dataset.go),'D01.g');
  await page.keyboard.press('Enter'); await title('Record Inventory Movements').waitFor();
  assert.equal(await title('Record Inventory Movements').evaluate(el=>el===document.activeElement),true);
  assert.equal(await item('D01.g').getAttribute('aria-selected'),'true');
  assert.equal(await page.locator('.fa-detail-hero').count(),0);
  assert.equal(await page.locator('[data-view="links"]').count(),0);
  const readingWidth=await page.locator('.fa-business').evaluate(el=>el.getBoundingClientRect().width);
  assert.ok(readingWidth>600, `Reading width ${readingWidth}`);
  await page.screenshot({path:path.join(output,'central-sheet.png')});
  // Proofs start closed, maintain adopted-field scope and restore source trigger.
  assert.equal(await page.locator('#fa-provenance').getAttribute('open'),null);
  await page.locator('[data-proof]').click();
  assert.match(await page.locator('#fa-provenance').innerText(),/Portée validée : Libellé/);
  const source=page.locator('.fa-source button').filter({hasText:/^U129$/});
  await source.click();
  await page.locator('#fa-source-dialog').getByRole('heading',{name:'U129',exact:true}).waitFor();
  await page.keyboard.press('Escape');
  assert.equal(await source.evaluate(el=>el===document.activeElement),true);
  await page.locator('#fa-back').click();
  await title('Record Inventory Movements').waitFor();
  await page.locator('#fa-back').click();
  await page.locator('#fa-results-area').waitFor();
  assert.equal(await page.locator('#fa-search').inputValue(),'D01.g');
  await page.locator('#fa-search').fill('inventaire');
  assert.equal(await page.locator('.fa-result').count(),0);
  assert.doesNotMatch(await page.locator('#fa-results-area').innerText(),/exemple « affectation »|« inventaire »/);
  assert.doesNotMatch(await page.locator('#fa-type').innerText(),/Composants SI|Flux SI/);
  assert.doesNotMatch(await page.locator('#fa-status').innerText(),/Hypothèses|Non traités/);
  // Old navigation roots redirect to the published root.
  for(const node of ['atlas']) { await page.goto(base+'/#node='+node); await title('Urbanisation').waitFor(); }
  // Real capacity pages and the whole domain map at desktop and narrow widths.
  await page.goto(base+'/#node=D01'); await title('Inventory Management').waitFor();
  await page.screenshot({path:path.join(output,'domain.png')});
  await page.locator('#fa-rail-resize').focus(); await page.keyboard.press('End');
  assert.equal(await page.locator('#fa-rail').evaluate(el=>el.getBoundingClientRect().width),420);
  await page.keyboard.press('Home');
  assert.equal(await page.locator('#fa-rail').evaluate(el=>el.getBoundingClientRect().width),240);
  await page.keyboard.press('ArrowRight'); await page.keyboard.press('ArrowRight'); await page.keyboard.press('ArrowRight');
  const measure=[];
  for(const width of [1920,1366,1024,980,390,320]) {
    await page.setViewportSize({width,height:844});
    await page.goto(base+'/#node=D01.g'); await title('Record Inventory Movements').waitFor();
    const metrics=await page.evaluate(()=>({width:innerWidth,overflow:document.documentElement.scrollWidth>innerWidth,definition:[...document.querySelectorAll('.fa-business h2')].find(el=>el.textContent==='Définition').getBoundingClientRect().top,readingWidth:document.querySelector('.fa-business').getBoundingClientRect().width}));
    assert.equal(metrics.overflow,false); assert.ok(metrics.definition<844,JSON.stringify(metrics)); measure.push(metrics);
    if([1366,390].includes(width)) await page.screenshot({path:path.join(output,`sheet-${width}.png`)});
    if(width<=1000) {
      await page.locator('#fa-tree-open').click();
      assert.equal(await page.locator('#fa-main').evaluate(el=>el.inert),true);
      await page.locator('#fa-tree-close').focus(); await page.keyboard.press('Shift+Tab');
      assert.equal(await page.evaluate(()=>document.activeElement.dataset.treeId),'D01.g');
      await page.keyboard.press('Tab'); assert.equal(await page.evaluate(()=>document.activeElement.id),'fa-tree-close');
      if(width===390) await page.screenshot({path:path.join(output,'drawer-390.png')});
      await page.keyboard.press('Escape'); assert.equal(await page.evaluate(()=>document.activeElement.id),'fa-tree-open');
      await page.locator('#fa-tree-open').click(); await item('D01.d').focus(); await page.keyboard.press('Enter');
      await title('Stocktaking').waitFor(); assert.equal(await page.locator('#fa-main').evaluate(el=>el.inert),false);
      assert.equal(await title('Stocktaking').evaluate(el=>el===document.activeElement),true);
    }
  }
  // Synthetic deeper hierarchy and transverse relation: HTTP fixture only.
  const api=await (await page.request.get(base+'/api/model')).json(), fixture=structuredClone(api);
  const cap=fixture.nodes.find(node=>node.id==='D03.b');
  for(let depth=1;depth<=4;depth++) {
    fixture.nodes.push({id:'TEST-L'+depth,kind:'group',group_role:'urbanism_level',level_ref:'TEST-LEVEL-'+depth,layer:'transactional',fields:{name:'Niveau de test '+depth},review:{state:'proposed'},source_refs:[]});
    fixture.relations.push({id:'TEST-R'+depth,type:'contains',source_id:depth===1?'D03':'TEST-L'+(depth-1),target_id:'TEST-L'+depth,review:{state:'proposed'},source_refs:[]});
  }
  fixture.relations.find(edge=>edge.type==='contains'&&edge.target_id===cap.id).source_id='TEST-L4';
  fixture.nodes.push({id:'TEST-OBJ',kind:'object',layer:'transactional',fields:{name:'Objet de test'},review:{state:'proposed'},source_refs:[]});
  fixture.relations.push({id:'TEST-LINK',type:'relates-to',source_id:cap.id,target_id:'TEST-OBJ',fields:{label:'utilise'},review:{state:'proposed'},source_refs:[]});
  await page.route('**/api/model',route=>route.fulfill({json:fixture}));
  await page.setViewportSize({width:1366,height:900}); await page.goto(base+'/#node=D03.b'); await page.reload();
  await item('TEST-L4').waitFor();
  assert.equal(await item('D03.b').getAttribute('aria-level'),'8');
  assert.match(await page.locator('[id="tree-label-TEST-L4"]').innerText(),/Niveau d’urbanisme/);
  assert.equal(await item('TEST-OBJ').count(),0);
  await page.locator('[data-view="links"]').click(); await page.locator('[data-go="TEST-OBJ"]').click();
  await title('Objet de test').waitFor();
  assert.equal(await item('TEST-OBJ').count(),0);
  assert.deepEqual(errors,[]);
  console.log(JSON.stringify({checks:'tree/keyboard/search/expansion/proofs/history/resize/mobile/depth/transverse-relations',measure,errors,output}));
} finally { await browser.close(); }

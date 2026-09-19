import {createRequire} from 'node:module';
import {writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
const require=createRequire(import.meta.url);
const {chromium}=require('C:/Users/laure/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const browser=await chromium.launch({channel:'msedge',headless:true});
const observations=[];
try {
 const page=await browser.newPage({viewport:{width:1440,height:900},reducedMotion:'reduce'});
 for(const [name,hash] of [['achat','#view=sheet&node=D04.j'],['agreement','#view=sheet&node=D11'],['meta','#view=principles'],['relations-domaines','#view=relations&level=domain&depth=0'],['glossaire','#view=glossary']]){
  await page.goto('http://127.0.0.1:8765/'+hash); await page.locator('#page-title').waitFor();await page.waitForTimeout(500);
  const data=await page.evaluate(()=>{
   const rgb=v=>v.match(/[\d.]+/g)?.map(Number)||[0,0,0,0];
   const blend=(a,b)=>[0,1,2].map(i=>a[i]*(a[3]??1)+b[i]*(1-(a[3]??1)));
   const bg=el=>{const chain=[];for(let e=el;e;e=e.parentElement)chain.unshift(e);return chain.reduce((b,e)=>blend(rgb(getComputedStyle(e).backgroundColor),b),[255,255,255]);};
   const lum=c=>c.map(v=>{v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4}).reduce((sum,v,i)=>sum+v*[.2126,.7152,.0722][i],0);
   const results=[];
   for(const el of document.querySelectorAll('main *,aside *,header *')){
    if(![...el.childNodes].some(n=>n.nodeType===Node.TEXT_NODE&&n.textContent.trim())) continue;
    const r=el.getBoundingClientRect(); const c=getComputedStyle(el);if(!r.width||!r.height||c.visibility==='hidden'||c.display==='none')continue;
    const b=bg(el),f=blend(rgb(c.color),b),l1=lum(f),l2=lum(b),ratio=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);
    let complex=false;for(let e=el;e;e=e.parentElement){const s=getComputedStyle(e);if(s.backgroundImage!=='none'||Number(s.opacity)!==1)complex=true;}
    results.push({text:el.textContent.trim().slice(0,100),class:el.className,fg:c.color,bg:b.map(Math.round),ratio:Number(ratio.toFixed(3)),font:parseFloat(c.fontSize),weight:c.fontWeight,complexBackground:complex});
   }
   const simple=results.filter(x=>!x.complexBackground);
   return {minimumSimpleContrast:Math.min(...simple.map(x=>x.ratio)),lowContrast:simple.filter(x=>x.ratio<((x.font>=24||(Number(x.weight)>=700&&x.font>=18.667))?3:4.5)),smallText:simple.filter(x=>x.font<12).slice(0,20),bodyWidth:document.documentElement.scrollWidth,bodyHeight:document.documentElement.scrollHeight,mastership:document.querySelector('[id$="-mastership"]')?.textContent,guideTopics:[...document.querySelectorAll('.guide-topics button')].map(e=>e.textContent),skipLinks:[...document.querySelectorAll('a')].filter(e=>/aller|skip/i.test(e.textContent)).map(e=>e.textContent)};
  });
  observations.push({name,...data});
  await page.screenshot({path:fileURLToPath(new URL('detail-'+name+'.png',import.meta.url)),fullPage:false});
 }
 // Check the repaired split-panel glossary mechanics; this is not a usability study.
 const list=page.locator('.glossary-index ul');
 const listInfo=await list.evaluate(el=>({height:el.clientHeight,scroll:el.scrollHeight}));
 await list.evaluate(el=>el.scrollTop=el.scrollHeight);
 const entries=page.locator('.glossary-index li a');
 if(await entries.count())await entries.last().click();
 const glossary=await page.evaluate(()=>({selected:document.querySelector('.glossary-index [aria-current]')?.textContent,term:document.querySelector('.glossary-term h2')?.textContent,panes:[...document.querySelectorAll('.glossary-page *')].filter(e=>e.scrollHeight>e.clientHeight+10&&['auto','scroll'].includes(getComputedStyle(e).overflowY)).map(e=>({class:e.className,scrollTop:e.scrollTop}))}));
 await writeFile(new URL('accessibility-observations.json',import.meta.url),JSON.stringify({method:'CSS text/background pairs; excludes ancestors with images or opacity. No full WCAG conformance claim; canvas, focus, hover and all responsive states are not exhaustively tested.',observations,glossary:{listInfo,...glossary}},null,2));
 console.log(JSON.stringify({observations:observations.map(o=>({name:o.name,min:o.minimumSimpleContrast,lowCount:o.lowContrast.length,examples:o.lowContrast.slice(0,3),mastership:o.mastership,guideTopics:o.guideTopics})),glossary:{listInfo,...glossary}},null,2));
} finally {await browser.close()}

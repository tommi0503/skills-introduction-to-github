import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {root,serve,launch} from './runtime.mjs';
const manifest=JSON.parse(await fs.readFile(path.join(root,'review/slide-manifest.json'),'utf8'));
const select=process.argv.find(x=>x.startsWith('--concept='))?.split('=')[1];
const ids=manifest.concepts.filter(c=>!select||select.includes(c.id)).map(c=>c.id);
const server=await serve(),browser=await launch(),results=[];
await fs.mkdir(path.join(root,'previews'),{recursive:true});
try{
 await Promise.all(ids.map(async id=>{
  const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  for(const mode of ['design','wireframe']){
   const dir=path.join(root,'concepts',id,'previews',mode);await fs.mkdir(dir,{recursive:true});
   for(let i=1;i<=12;i++){
    const n=String(i).padStart(2,'0');await page.goto(server.url+`/concepts/${id}/${mode}/${n}.html`,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);
    const qa=await page.evaluate(()=>{
     const slide=document.querySelector('.slide'),b=slide.getBoundingClientRect(),issues=[],overlaps=[],labels=[];
     const rect=x=>({x:Math.round(x.x*100)/100,y:Math.round(x.y*100)/100,width:Math.round(x.width*100)/100,height:Math.round(x.height*100)/100});
     const bookend=['01','12'].includes(slide.dataset.slide),section=slide.querySelector('.section-label');
     if(!document.fonts.check('20px Pretendard'))issues.push('Pretendard not loaded');
     if(b.width!==1280||b.height!==720)issues.push('Canvas dimensions');
     if(bookend&&slide.querySelector('.section-label,.slide-header,.page-number,.slide-footer'))issues.push('Bookend has section/footer');
     if(!bookend&&!section)issues.push('Missing body section label');
     const text=[];const walker=document.createTreeWalker(slide,NodeFilter.SHOW_TEXT);let node;
     while(node=walker.nextNode()){if(!node.textContent.trim())continue;const el=node.parentElement;if(['STYLE','SCRIPT'].includes(el.tagName)||el.closest('[aria-hidden="true"]')&&el.closest('svg'))continue;const st=getComputedStyle(el);if(st.display==='none'||st.visibility==='hidden')continue;const r=document.createRange();r.selectNodeContents(node);for(const t of r.getClientRects()){if(!t.width||!t.height)continue;const label=node.textContent.trim().slice(0,48);if(t.left<b.left-2||t.right>b.right+2||t.top<b.top-2||t.bottom>b.bottom+2)issues.push('Text outside canvas: '+label);text.push({x:t.x,y:t.y,w:t.width,h:t.height,label,el})}const font=parseFloat(st.fontSize),line=parseFloat(st.lineHeight);if(font%2)issues.push('Odd font size '+font+': '+node.textContent.trim().slice(0,20));if(Number.isFinite(line)&&Math.abs(line/2-Math.round(line/2))>.01)issues.push('Odd line height '+line+': '+node.textContent.trim().slice(0,20))}
     for(let a=0;a<text.length;a++)for(let d=a+1;d<text.length;d++){const x=text[a],y=text[d];if(x.el===y.el||x.el.contains(y.el)||y.el.contains(x.el))continue;const iw=Math.min(x.x+x.w,y.x+y.w)-Math.max(x.x,y.x),ih=Math.min(x.y+x.h,y.y+y.h)-Math.max(x.y,y.y);if(iw>8&&ih>6&&iw*ih>120)overlaps.push([x.label,y.label])}
     const placeholders=[...slide.querySelectorAll('.placeholder')].map(p=>{const color=getComputedStyle(p).backgroundColor;if(color!=='rgb(229, 229, 229)')issues.push('Image placeholder not solid gray');return rect(p.getBoundingClientRect())});
     return{issues:[...new Set(issues)],possibleTextOverlaps:overlaps,section:section?rect(section.getBoundingClientRect()):null,heading:slide.querySelector('.heading')?rect(slide.querySelector('.heading').getBoundingClientRect()):null,placeholderCount:placeholders.length,placeholderArea:Math.round(placeholders.reduce((n,p)=>n+p.width*p.height,0)),placeholders,textRuns:text.length};
    });
    const file=path.join(dir,n+'.png');await page.screenshot({path:file});const sha256=crypto.createHash('sha256').update(await fs.readFile(file)).digest('hex');results.push({concept:id,mode,page:n,...qa,sha256});
   }
   await fs.mkdir(path.join(root,'concepts',id,'pdfs'),{recursive:true});await page.goto(server.url+`/concepts/${id}/${mode}/print.html`,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);await page.pdf({path:path.join(root,'concepts',id,'pdfs',mode+'.pdf'),width:'1280px',height:'720px',printBackground:true,preferCSSPageSize:true});
  }
  const coords=results.filter(r=>r.concept===id&&r.mode==='design'&&r.section).map(r=>[r.section.x,r.section.y].join(','));if(new Set(coords).size!==1)errors.push('Section coordinates differ: '+coords.join(' / '));
  const css=await fs.readFile(path.join(root,'concepts',id,'style.css'),'utf8');const odd=[...css.matchAll(/(-?\d*\.?\d+)px\b/g)].map(m=>Number(m[1])).filter(n=>n%2!==0);if(odd.length)errors.push('Odd CSS px: '+[...new Set(odd)].join(','));
  await fs.writeFile(path.join(root,'review',id+'-render.json'),JSON.stringify({concept:id,errors,pages:results.filter(r=>r.concept===id)},null,2));console.log(id.toUpperCase()+': rendered 24 HTML slides + 2 PDFs; '+results.filter(r=>r.concept===id).reduce((n,r)=>n+r.issues.length,0)+' layout issues, '+errors.length+' source errors.');await page.close();
 }));
 const page=await browser.newPage({viewport:{width:1600,height:1100},deviceScaleFactor:1});await page.goto(server.url+'/index.html',{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);await page.waitForFunction(()=>[...document.querySelectorAll('iframe')].every(f=>f.classList.contains('ready')));await page.screenshot({path:path.join(root,'previews/review-home.png'),fullPage:true});await page.goto(server.url+'/index.html#view=final&page=06&mode=design&layout=compare',{waitUntil:'networkidle'});await page.waitForFunction(()=>[...document.querySelectorAll('iframe')].every(f=>f.classList.contains('ready')));await page.screenshot({path:path.join(root,'previews/review-compare.png'),fullPage:true});await page.goto(server.url+'/docs/planning.html',{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);await fs.mkdir(path.join(root,'pdfs'),{recursive:true});await page.pdf({path:path.join(root,'pdfs/planning.pdf'),format:'A4',printBackground:true,preferCSSPageSize:true});await page.close();
 const hashes={};for(const file of ['shared/base.css','shared/content.js',...ids.flatMap(id=>[`concepts/${id}/deck.js`,`concepts/${id}/style.css`])])hashes[file]=crypto.createHash('sha256').update(await fs.readFile(path.join(root,file))).digest('hex');await fs.writeFile(path.join(root,'review/render-sources.json'),JSON.stringify(hashes,null,2));
}finally{await browser.close();await server.close()}
console.log('Render complete. Inspect review/*-render.json before delivery.');

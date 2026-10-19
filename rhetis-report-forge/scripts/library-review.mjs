import {chromium} from 'playwright-core';
import fs from 'node:fs/promises';
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage']});
const page=await browser.newPage({viewport:{width:1280,height:720}});
const fontData=(await fs.readFile('public/fonts/PretendardVariable.woff2')).toString('base64');
const modes=process.argv.slice(2).length?process.argv.slice(2):['light','dark'];const tasks=[],results=[];
for(const mode of modes){
 await page.goto(`http://localhost:5173/outputs/${mode}.html`);await page.evaluate(()=>document.fonts.ready);
 const sheet=await page.evaluate(()=>({styles:document.querySelector('style').textContent,fixtures:[...document.querySelectorAll('article')].map((a,i)=>({label:a.querySelector('h2').textContent,html:a.querySelector('.slide').outerHTML,index:i+1}))}));
 await fs.mkdir(`renders/library-${mode}`,{recursive:true});
 for(const f of sheet.fixtures){
  if(process.env.LIB_FILTER&&!process.env.LIB_FILTER.split(',').some(k=>f.label.startsWith(k+' /')))continue;
  const min=(f.label.match(/min (\d+)x(\d+)/)||[]).slice(1).map(Number),sizes=[['full',12,6],...(min.length&&!(min[0]===12&&min[1]===6)?[['min',...min]]:[])];
  for(const [scale,cols,rows] of sizes)tasks.push({...f,mode,scale,cols,rows,styles:sheet.styles});
 }
}
let cursor=0;
await Promise.all(Array.from({length:4},async()=>{
 const capture=await browser.newPage({viewport:{width:1280,height:720}});
 while(cursor<tasks.length){const t=tasks[cursor++];
  await capture.setContent(`<html><head><meta charset="UTF-8"><style>@font-face{font-family:Pretendard;src:url('data:font/woff2;base64,${fontData}');font-weight:100 900}body{margin:0}</style><style>${t.styles}</style></head><body>${t.html}</body></html>`);
  await capture.evaluate(({scale,cols,rows})=>{const body=document.querySelector('.body');if(scale==='min'&&body){body.firstElementChild.style.gridColumn=`1 / span ${cols}`;body.firstElementChild.style.gridRow=`1 / span ${rows}`;}},t);
  await capture.evaluate(()=>document.fonts.ready);
  if(t.scale==='full')await capture.locator('.slide').screenshot({path:`renders/library-${t.mode}/${String(t.index).padStart(3,'0')}.png`});
  const audit=await capture.evaluate(()=>{
   const issues=[],contrastIssues=[],root=document.querySelector('.slide'),bounds=root.getBoundingClientRect(),walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
   const rgba=s=>{let n=s.match(/[\d.]+/g)?.map(Number)||[0,0,0];if(s.startsWith('color(srgb'))n=n.map((v,i)=>i<3?v*255:v);return [n[0],n[1],n[2],n[3]??1]};
   const lum=c=>c.slice(0,3).map(v=>v/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((n,v,i)=>n+v*[.2126,.7152,.0722][i],0);
   while(walker.nextNode()){
    const n=walker.currentNode;if(!n.textContent.trim())continue;const el=n.parentElement,s=getComputedStyle(el);if(s.display==='none'||!el.getClientRects().length)continue;
    const range=document.createRange();range.selectNode(n);const r=range.getBoundingClientRect(),nearest=el.closest('[data-el]')||root,b=nearest.getBoundingClientRect();
    if(r.width&&r.height&&(r.left<bounds.left-1||r.right>bounds.right+1||r.top<bounds.top-1||r.bottom>bounds.bottom+1||r.left<b.left-2||r.right>b.right+2||r.top<b.top-2||r.bottom>b.bottom+2))issues.push({text:n.textContent.slice(0,70),root:nearest.dataset.el,rect:[r.x,r.y,r.width,r.height],boundary:[b.x,b.y,b.width,b.height]});
    const backgrounds=[];let e=el;while(e){const c=rgba(getComputedStyle(e).backgroundColor);backgrounds.push(c);if(c[3]>.999)break;e=e.parentElement;}let bg=[255,255,255];for(const c of backgrounds.reverse())bg=bg.map((v,i)=>v*(1-c[3])+c[i]*c[3]);const fg=rgba(s.color);const L1=lum(fg),L2=lum(bg),ratio=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05),threshold=parseFloat(s.fontSize)>=28?3:4.5;if(ratio<threshold-.02)contrastIssues.push({text:n.textContent.slice(0,50),ratio:+ratio.toFixed(2),threshold,fg:s.color,bg});
   }
   return {issues,contrastIssues,size:[bounds.width,bounds.height],font:document.fonts.check('400 20px Pretendard')};
  });results.push({mode:t.mode,label:t.label,scale:t.scale,cols:t.cols,rows:t.rows,...audit});
 }
 await capture.close();
}));
results.sort((a,b)=>a.mode.localeCompare(b.mode)||a.label.localeCompare(b.label)||a.scale.localeCompare(b.scale));
await fs.writeFile(process.env.LIB_FILTER?'review/library-audit-targeted.json':'review/library-audit.json',JSON.stringify(results,null,2));
console.log('cases',results.length,'overflow',results.reduce((n,r)=>n+r.issues.length,0),'contrast',results.reduce((n,r)=>n+r.contrastIssues.length,0));await browser.close();

// Lead-author browser audit. It does not change collection or review sources.
const {chromium}=require('playwright');
const fs=require('fs');const path=require('path');
const http=require('http');
const ROOT=path.resolve(__dirname,'..');
const names=process.argv.slice(2).length?process.argv.slice(2):['chalkline','undertow','cutplane','skylight','arrowtab','blockweave'];
(async()=>{
const server=http.createServer((req,res)=>{const f=path.resolve(ROOT,'.'+decodeURIComponent(req.url.split('?')[0]));if(!f.startsWith(ROOT+'/')){res.writeHead(403);res.end();return;}fs.readFile(f,(e,data)=>{if(e){res.writeHead(404);res.end();return;}const types={'.html':'text/html; charset=utf-8','.css':'text/css','.woff2':'font/woff2','.png':'image/png','.woff':'font/woff'};res.setHeader('Content-Type',types[path.extname(f)]||'application/octet-stream');res.end(data)});});
await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin='http://127.0.0.1:'+server.address().port;
const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
let report=[];
for(const name of names){
 const entry={collection:name,modes:[]};
 for(const mode of ['light','dark']){
  const file=path.join(ROOT,'reviews',name+'-review','library',mode+'.html');if(!fs.existsSync(file)){entry.modes.push({mode,error:'sheet missing'});continue;}
  const page=await browser.newPage({viewport:{width:1360,height:900}});let fails=[];
  page.on('requestfailed',r=>fails.push({url:r.url(),error:r.failure()?.errorText}));
  await page.goto(origin+'/reviews/'+name+'-review/library/'+mode+'.html');await page.evaluate(()=>document.fonts.ready);
  const sourceReport=await page.evaluate(()=>{
   const out=[];
   function walkRules(rules){for(const rule of rules){if(rule.selectorText)out.push({selector:rule.selectorText,css:rule.style.cssText});else if(rule.cssRules)walkRules(rule.cssRules);}}
   for(const sheet of document.styleSheets){try{walkRules(sheet.cssRules)}catch{}}
   return {fonts:[...document.fonts].map(f=>({family:f.family,status:f.status})),rules:out};
  });
  const contrast=await page.evaluate(()=>{
   const canvas=document.createElement('canvas');canvas.width=canvas.height=1;const ctx=canvas.getContext('2d',{willReadFrequently:true});const cache=new Map();
   function rgba(s){if(cache.has(s))return cache.get(s);ctx.clearRect(0,0,1,1);ctx.fillStyle=s;ctx.fillRect(0,0,1,1);const v=[...ctx.getImageData(0,0,1,1).data];v[3]/=255;cache.set(s,v);return v;}
   function blend(f,b){return [f[0]*f[3]+b[0]*(1-f[3]),f[1]*f[3]+b[1]*(1-f[3]),f[2]*f[3]+b[2]*(1-f[3]),1];}
   function lum(c){return c.slice(0,3).map(x=>{x/=255;return x<=.04045?x/12.92:((x+.055)/1.055)**2.4}).reduce((n,v,i)=>n+v*[.2126,.7152,.0722][i],0);}
   const out=[];
   for(const article of document.querySelectorAll('article')){const title=article.querySelector('h2')?.textContent||'',slide=article.querySelector('.slide');if(!slide)continue;let walk=document.createTreeWalker(slide,NodeFilter.SHOW_TEXT);for(let t;t=walk.nextNode();){if(!t.textContent.trim())continue;const el=t.parentElement,cs=getComputedStyle(el);let r=document.createRange();r.selectNodeContents(t);if(![...r.getClientRects()].some(x=>x.width&&x.height)||cs.visibility==='hidden'||el.closest('[data-icon]'))continue;let ancestors=[];for(let a=el;a;a=a.parentElement)ancestors.unshift(a);const rr=[...r.getClientRects()].find(x=>x.width&&x.height),px=(rr.left+rr.right)/2,py=(rr.top+rr.bottom)/2;let bg=[255,255,255,1],gradient=false;for(const a of ancestors){const ar=a.getBoundingClientRect();if(px<ar.left||px>ar.right||py<ar.top||py>ar.bottom)continue;const s=getComputedStyle(a);bg=blend(rgba(s.backgroundColor),bg);if(s.backgroundImage!=='none')gradient=true;}const fg=blend(rgba(cs.color),bg),l1=lum(fg),l2=lum(bg),ratio=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05),size=parseFloat(cs.fontSize),min=size>=28?3:4.5;if(ratio+.05<min)out.push({title,text:t.textContent.trim().slice(0,70),className:el.className,fontSize:size,ratio:+ratio.toFixed(2),minimum:min,gradientUncertain:gradient,color:cs.color,background:bg});}}
   return out;
  });
  const stress=await page.evaluate(()=>{
   let all=[];
   const fontSize=e=>parseFloat(getComputedStyle(e).fontSize);
   function inspect(root,slot){
    const issues=[];const text=[];
    const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
    for(let t;t=walker.nextNode();){
     if(!t.textContent.trim())continue;let el=t.parentElement;
     if(!el||el.closest('[data-icon]'))continue;
     const st=getComputedStyle(el);if(st.visibility==='hidden'||st.display==='none')continue;
     const range=document.createRange();range.selectNodeContents(t);
     const rects=[...range.getClientRects()].filter(r=>r.width>0&&r.height>0);
     for(const r of rects){
      let clipped=false;
      for(let anc=el;anc&&anc!==root.parentElement;anc=anc.parentElement){let cs=getComputedStyle(anc),ar=anc.getBoundingClientRect();if((cs.overflowX==='hidden'||cs.overflowX==='clip')&&(r.left<ar.left-1||r.right>ar.right+1))clipped=true;if((cs.overflowY==='hidden'||cs.overflowY==='clip')&&(r.top<ar.top-1||r.bottom>ar.bottom+1))clipped=true;}
      if(r.left<slot.left-2||r.right>slot.right+2||r.top<slot.top-2||r.bottom>slot.bottom+2||clipped)issues.push({type:'text-overflow',text:t.textContent.trim().slice(0,90),tag:el.tagName,cls:el.className,slot:{w:slot.width,h:slot.height},rect:{x:r.left-slot.left,y:r.top-slot.top,w:r.width,h:r.height},clipped});
      text.push({el,rect:r,value:t.textContent.trim()});
     }
    }
    for(let i=0;i<text.length;i++)for(let j=i+1;j<text.length;j++){
     const a=text[i],b=text[j];if(a.el===b.el||a.el.contains(b.el)||b.el.contains(a.el))continue;
     const w=Math.min(a.rect.right,b.rect.right)-Math.max(a.rect.left,b.rect.left),h=Math.min(a.rect.bottom,b.rect.bottom)-Math.max(a.rect.top,b.rect.top);
     if(w>2&&h>2&&w*h>Math.min(a.rect.width*a.rect.height,b.rect.width*b.rect.height)*.15)issues.push({type:'text-overlap',a:a.value.slice(0,50),b:b.value.slice(0,50)});
    }
    return issues;
   }
   for(const article of document.querySelectorAll('article')){
    const title=article.querySelector('h2')?.textContent||'';
    if(title.startsWith('foundation'))continue;
    const body=article.querySelector('.slide>.page>.body');if(!body||!body.firstElementChild){all.push({title,error:'missing body root'});continue;}
    const root=body.firstElementChild;
    let sizes=[[12,6]];
    const min=title.split('min ')[1]||'';
    for(const m of min.matchAll(/(\d+)x(\d+)/g)){let c=+m[1],r=+m[2];sizes.push([c,r],[Math.ceil((c+12)/2),Math.ceil((r+6)/2)]);}
    sizes=[...new Map(sizes.map(x=>[x.join('x'),x])).values()];
    const orig=root.getAttribute('style');
    for(const [c,r] of sizes){root.style.gridColumn=`1 / span ${c}`;root.style.gridRow=`1 / span ${r}`;void root.offsetWidth;const br=body.getBoundingClientRect(),bs=getComputedStyle(body),scale=br.width/body.clientWidth;const cols=bs.gridTemplateColumns.split(' ').map(parseFloat),rows=bs.gridTemplateRows.split(' ').map(parseFloat);const w=(cols.slice(0,c).reduce((a,b)=>a+b,0)+parseFloat(bs.columnGap||0)*(c-1))*scale,h=(rows.slice(0,r).reduce((a,b)=>a+b,0)+parseFloat(bs.rowGap||0)*(r-1))*scale;const slot={left:br.left,top:br.top,right:br.left+w,bottom:br.top+h,width:w,height:h};const issues=inspect(root,slot);all.push({title,size:`${c}x${r}`,issues});}
    if(orig===null)root.removeAttribute('style');else root.setAttribute('style',orig);
   }
   return all;
  });
  const summary={mode,requestFailures:fails,fonts:sourceReport.fonts.filter(f=>f.status==='loaded'),contrast,cases:stress.length,issueCases:stress.filter(s=>s.error||s.issues.length),issueCount:stress.reduce((n,s)=>n+(s.issues?.length||0),0)};
  entry.modes.push(summary);await page.close();
 }
 report.push(entry);fs.mkdirSync(path.join(ROOT,'checks/lead-review'),{recursive:true});fs.writeFileSync(path.join(ROOT,'checks/lead-review')+'/'+name+'-audit.json',JSON.stringify(entry,null,2));console.log(name,entry.modes.map(m=>({mode:m.mode,cases:m.cases,issues:m.issueCount,error:m.error})));
}
await browser.close();server.close();fs.writeFileSync(path.join(ROOT,'checks/integration-browser-audit.json'),JSON.stringify(report,null,2));
})().catch(e=>{console.error(e);process.exit(1)});

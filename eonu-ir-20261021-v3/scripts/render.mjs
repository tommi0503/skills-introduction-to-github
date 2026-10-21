import fs from 'node:fs/promises';
import path from 'node:path';
import http from 'node:http';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const require=createRequire(import.meta.url);
const {chromium}=require('playwright');
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const mime={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.woff2':'font/woff2','.json':'application/json'};
const server=http.createServer(async(req,res)=>{try{const url=new URL(req.url,'http://localhost');const name=path.resolve(root,'.'+decodeURIComponent(url.pathname==='/'?'/index.html':url.pathname));if(!name.startsWith(root+path.sep)){res.writeHead(403);res.end();return;}const data=await fs.readFile(name);res.setHeader('Content-Type',mime[path.extname(name)]||'application/octet-stream');res.end(data);}catch{res.writeHead(404);res.end('Not found');}});
await new Promise(r=>server.listen(0,'127.0.0.1',r));
const origin=`http://127.0.0.1:${server.address().port}`;
await fs.mkdir(path.join(root,'previews'),{recursive:true});await fs.mkdir(path.join(root,'review'),{recursive:true});
const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
const page=await browser.newPage({viewport:{width:1280,height:800},deviceScaleFactor:1});
const errors=[],requests=[];page.on('pageerror',e=>errors.push(e.message));page.on('requestfailed',r=>requests.push(r.url()));
const docsOnly=process.argv.includes('--docs-only');
const report={canvas:[1280,720],variants:docsOnly?[]:['wireframe','design'],slidesPerVariant:12,pages:[],errors,failedRequests:requests};
try{
 for(const theme of report.variants){
  await fs.mkdir(path.join(root,'previews',theme),{recursive:true});
  for(let i=1;i<=12;i++){
   const id=String(i).padStart(2,'0');
   await page.goto(`${origin}/${theme}/${id}.html`,{waitUntil:'networkidle'});
   await page.evaluate(()=>document.fonts.ready);
   const findings=await page.locator('.slide').evaluate(slide=>{
    const r=slide.getBoundingClientRect(),head=slide.querySelector('.heading')?.getBoundingClientRect(),label=slide.querySelector('.section-label')?.getBoundingClientRect(),body=slide.querySelector('.slide-body').getBoundingClientRect(),bookend=slide.classList.contains('bookend');
    const issues=[];
    for(const el of slide.querySelectorAll('.slide-body *')){
     if(el.closest('svg')||['svg','path'].includes(el.tagName.toLowerCase()))continue;
     const b=el.getBoundingClientRect();
     if(b.width&&b.height&&(b.left<body.left-2||b.right>body.right+2||b.top<body.top-2||b.bottom>body.bottom+2))issues.push({type:'body-boundary',tag:el.tagName,class:el.className,text:el.textContent.slice(0,50),box:[b.x-r.x,b.y-r.y,b.width,b.height]});
     if(el.scrollWidth>el.clientWidth+2&&el.clientWidth>0&&getComputedStyle(el).display!=='inline'&&!el.classList.contains('story'))issues.push({type:'horizontal-overflow',class:el.className,text:el.textContent.slice(0,50),scroll:el.scrollWidth,width:el.clientWidth});
    }
    const placeholders=[...slide.querySelectorAll('.placeholder')].map(el=>getComputedStyle(el).backgroundColor);
    for(const el of slide.querySelectorAll('.icon-badge')){const st=getComputedStyle(el);if(st.display!=='flex'||st.alignItems!=='center'||st.justifyContent!=='center')issues.push({type:'icon-badge-alignment',class:el.className});}
    for(const el of slide.querySelectorAll('*')){
     if(el.closest('svg'))continue;
     for(const node of el.childNodes){
      if(node.nodeType!==Node.TEXT_NODE||!node.textContent.trim())continue;
      const range=document.createRange();range.selectNodeContents(node);
      for(const rect of range.getClientRects()){
       let parent=el;
       while(parent&&parent!==slide){
        const st=getComputedStyle(parent),pr=parent.getBoundingClientRect();
        if(['hidden','clip'].includes(st.overflowY)&&rect.bottom>pr.bottom+1)issues.push({type:'clipped-text',class:parent.className,text:node.textContent.slice(0,60)});
        parent=parent.parentElement;
       }
      }
     }
    }
    const fontSizes=[...new Set([...slide.querySelectorAll('*')].filter(e=>!e.closest('svg')).map(e=>parseFloat(getComputedStyle(e).fontSize)))];
    const fontFamilies=[...new Set([...slide.querySelectorAll('*')].map(e=>getComputedStyle(e).fontFamily))];
    const lineHeights=[...new Set([...slide.querySelectorAll('*')].filter(e=>!e.closest('svg')).map(e=>getComputedStyle(e).lineHeight).filter(v=>v!=='normal').map(parseFloat))];
    const imageArea=[...slide.querySelectorAll('.placeholder')].reduce((sum,e)=>{const b=e.getBoundingClientRect();return sum+b.width*b.height},0);
    return {size:[r.width,r.height],bookend,heading:head?[head.x-r.x,head.y-r.y]:null,section:label?[label.x-r.x,label.y-r.y]:null,bookendHasRunningHeader:bookend&&!!slide.querySelector('.slide-header,.section-label,.page-number'),fontLoaded:document.fonts.check('20px Pretendard'),fontSizes,lineHeights,fontFamilies,imageArea,imageAreaPercent:Math.round(imageArea/(1280*720)*10000)/100,placeholders,svgCount:slide.querySelectorAll('svg').length,rasterImages:slide.querySelectorAll('img,image').length,issues};
   });
   const file=path.join(root,'previews',theme,`${id}.png`);await page.locator('.slide').screenshot({path:file});
   const sha=createHash('sha256').update(await fs.readFile(file)).digest('hex');
   report.pages.push({theme,id,...findings,pngSha256:sha});
  }
  await page.goto(`${origin}/${theme}/print.html`,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);
  await page.pdf({path:path.join(root,'previews',`eonu-${theme}.pdf`),preferCSSPageSize:true,printBackground:true,displayHeaderFooter:false});
 }
 await page.goto(`${origin}/docs/planning.html`,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);
 await page.pdf({path:path.join(root,'previews','eonu-planning.pdf'),format:'A4',preferCSSPageSize:true,printBackground:true});
 const sourceFiles=['src/components.js','src/slides.js','src/slides.css','src/viewer.js','src/viewer.css','index.html'];
 report.sourceHashes=Object.fromEntries(await Promise.all(sourceFiles.map(async f=>[f,createHash('sha256').update(await fs.readFile(path.join(root,f))).digest('hex')])));
 const cssTokens=await fs.readFile(path.join(root,'src/slides.css'),'utf8');
 report.offGridPxTokens=[...cssTokens.matchAll(/(-?\d*\.?\d+)px/g)].map(m=>Number(m[1])).filter(n=>n%2!==0);
 report.status=report.pages.every(p=>p.size[0]===1280&&p.size[1]===720&&(p.bookend?!p.bookendHasRunningHeader:p.heading[0]===64&&p.heading[1]===96&&p.section[0]===64)&&p.fontLoaded&&p.rasterImages===0&&p.placeholders.every(c=>c==='rgb(229, 229, 229)')&&p.fontSizes.every(n=>n%2===0)&&p.lineHeights.every(n=>n%2===0)&&p.issues.length===0)&&report.offGridPxTokens.length===0&&errors.length===0&&requests.length===0?'passed':'needs-review';
 if(!docsOnly)await fs.writeFile(path.join(root,'review','render-audit.json'),JSON.stringify(report,null,2)+'\n');
 console.log(JSON.stringify({status:report.status,pages:report.pages.length,issues:report.pages.filter(p=>p.issues.length).map(p=>({theme:p.theme,id:p.id,issues:p.issues})),errors,requests},null,2));
 if(report.status!=='passed')throw new Error('Render audit requires review; see review/render-audit.json');
}finally{await browser.close();await new Promise(r=>server.close(r));}

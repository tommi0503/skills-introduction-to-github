import {chromium} from 'playwright-core';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';

// Check every integer grid size admitted by any declared minimum, through 12x6.
// The check reads generated light/dark sheets and writes only the JSON report.
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage']});
const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
const font=(await readFile('node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2')).toString('base64');
const sheetSnapshot=Object.fromEntries(await Promise.all(['light','dark'].map(async mode=>[mode,await readFile(mode+'.html','utf8')])));
const report={generatedAt:new Date().toISOString(),method:'Every integer column/row size from each declared minimum to 12x6; 3px layout tolerance; >=12px outside-slot or >5px own-box overflow classified serious. Text overlap uses individual rendered line rectangles, >6px in each axis.',sheets:{},modes:[],summary:{}};
try{
for(const mode of ['light','dark']){
 const html=sheetSnapshot[mode];report.sheets[mode]=createHash('sha256').update(html).digest('hex');
 await page.setContent(html);
 await page.addStyleTag({content:`@font-face{font-family:'Pretendard Variable';font-style:normal;font-weight:45 920;src:url(data:font/woff2;base64,${font})}body{padding:0;display:block}article{display:none}article.active{display:block}article.active h2{display:none}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}`});
 await page.evaluate(async()=>{await document.fonts.load('400 20px "Pretendard Variable"','고객 성장 전략');await document.fonts.load('700 44px "Pretendard Variable"','고객 성장 전략');await document.fonts.ready});
 const fixtures=await page.evaluate(()=>{
  const records=[];const bounds=r=>({left:r.left,top:r.top,right:r.right,bottom:r.bottom,width:r.width,height:r.height});
  const outside=(q,r)=>Math.max(r.left-q.left,r.top-q.top,q.right-r.right,q.bottom-r.bottom,0);
  for(const article of document.querySelectorAll('article')){
   article.classList.add('active');
   const label=article.querySelector('h2').textContent,slide=article.querySelector('.slide'),root=slide.querySelector('.body')?.firstElementChild;
   if(!root){records.push({label,foundation:true,cases:[],status:'cover; fixed full slide'});article.classList.remove('active');continue}
   const minimums=[...label.matchAll(/(\d+)x(\d+)/g)].map(m=>[+m[1],+m[2]]),sizes=new Set();
   for(const [minC,minR]of minimums.length?minimums:[[12,6]])for(let c=minC;c<=12;c++)for(let r=minR;r<=6;r++)sizes.add(`${c}x${r}`);
   const cases=[];const previous=root.getAttribute('style');
   for(const size of sizes){
    const [columns,rows]=size.split('x').map(Number);root.style.gridColumn=`1 / span ${columns}`;root.style.gridRow=`1 / span ${rows}`;
    const rootBox=root.getBoundingClientRect(),slideBox=slide.getBoundingClientRect(),issues=[],texts=[];
    const all=[root,...root.querySelectorAll('*')];
    for(const element of all){
     if(element.children.length||!element.textContent.trim())continue;
     const cs=getComputedStyle(element),box=element.getBoundingClientRect();if(cs.display==='none'||cs.visibility==='hidden'||!box.width)continue;
     const range=document.createRange();range.selectNodeContents(element);const lineBoxes=[...range.getClientRects()].filter(r=>r.width&&r.height),union=range.getBoundingClientRect();
     const lineYs=new Set(lineBoxes.map(r=>Math.round(r.top)));
     if(element.matches('.fig,.bar > b,.pt > b')&&/^[₩+−\-]?[\d,.%]+(?:억|만|원|점|명|회|%)?$/.test(element.textContent.trim())&&lineYs.size>1)issues.push({kind:'numeric-wrap',severity:'serious',text:element.textContent,lines:lineYs.size,elementClass:element.className});
     const delta=outside(union,rootBox),canvasDelta=outside(union,slideBox),ownDx=Math.max(union.width-box.width,0),ownDy=Math.max(union.height-box.height,0);
     if(delta>3)issues.push({kind:'outside-slot',severity:delta>=12?'serious':'minor',text:element.textContent.slice(0,110),overflow:Math.round(delta*10)/10,elementClass:element.className});
     if(canvasDelta>3)issues.push({kind:'outside-slide',severity:'serious',text:element.textContent.slice(0,110),overflow:Math.round(canvasDelta*10)/10});
     if(ownDx>5||ownDy>5)issues.push({kind:'own-text-box',severity:'serious',text:element.textContent.slice(0,110),box:[Math.round(box.width),Math.round(box.height)],textBox:[Math.round(union.width),Math.round(union.height)]});
     texts.push({element,text:element.textContent.slice(0,100),rects:lineBoxes.map(bounds)});
    }
    for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){
     const a=texts[i],b=texts[j];if(a.element.contains(b.element)||b.element.contains(a.element))continue;
     let overlap=null;for(const x of a.rects)for(const y of b.rects){const w=Math.min(x.right,y.right)-Math.max(x.left,y.left),h=Math.min(x.bottom,y.bottom)-Math.max(x.top,y.top);if(w>6&&h>6)overlap={width:Math.round(w),height:Math.round(h)}}
     if(overlap)issues.push({kind:'text-overlap',severity:'serious',a:a.text,b:b.text,...overlap});
    }
    cases.push({size,slot:[Math.round(rootBox.width),Math.round(rootBox.height)],issues});
   }
   if(previous==null)root.removeAttribute('style');else root.setAttribute('style',previous);
   records.push({label,minimums,cases});article.classList.remove('active');
  }
  return records;
 });
 const cases=fixtures.flatMap(f=>f.cases),issues=cases.flatMap(c=>c.issues),summary={fixtures:fixtures.length,cases:cases.length,casesWithIssues:cases.filter(c=>c.issues.length).length,casesWithSeriousIssues:cases.filter(c=>c.issues.some(i=>i.severity==='serious')).length,issues:issues.length,seriousIssues:issues.filter(i=>i.severity==='serious').length};
 report.modes.push({mode,summary,fixtures});console.log(mode,JSON.stringify(summary));
 for(const fixture of fixtures){const bad=fixture.cases.filter(c=>c.issues.some(i=>i.severity==='serious'));if(bad.length)console.log(JSON.stringify({mode,label:fixture.label,affectedSizes:bad.map(c=>c.size),first:bad[0]}))}
}
report.summary={fixtures:report.modes.reduce((n,m)=>n+m.summary.fixtures,0),cases:report.modes.reduce((n,m)=>n+m.summary.cases,0),seriousIssues:report.modes.reduce((n,m)=>n+m.summary.seriousIssues,0)};
report.status=report.summary.seriousIssues?'needs-review':'passed';
await writeFile('review/library-min-check.json',JSON.stringify(report,null,2));
}finally{await browser.close()}

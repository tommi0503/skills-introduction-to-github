/** Independent Rhetis composition pipeline. Source React is read only through browser DOM.
 * node scripts/assemble-library.mjs --refresh --audit
 * Subsequent runs without --refresh always rebuild from provenance JSON and reread library CSS.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import {chromium} from 'playwright-core';
const cwd=process.cwd(), args=new Set(process.argv.slice(2));
const base='http://localhost:5173', kit='report-forge';
const dataPath=path.join(cwd,'src/assembly-data.json');
const escape=s=>String(s??'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const clean=s=>String(s??'').replace(/\s+/g,' ').trim();
const norm=s=>clean(s).replace(/[\s\[\]·:：_\-]/g,'').toLowerCase();
const launch=()=>chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
if(args.has('--refresh') || !(await fs.stat(dataPath).catch(()=>false))){
 const browser=await launch(),page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
 await page.goto(base); await page.waitForFunction(()=>window.__DECKS__?.length>=7);
 const decks=await page.evaluate(()=>window.__DECKS__), slides=[];
 for(const deck of decks) for(const slide of deck.slides){
  await page.goto(`${base}/?deck=${deck.id}&slide=${slide.id}`);await page.evaluate(()=>document.fonts.ready);
  const raw=await page.evaluate(()=>{
   const root=document.querySelector('.slide'), rr=root.getBoundingClientRect();
   const bounds=e=>{const r=e.getBoundingClientRect();return {x:+(r.x-rr.x).toFixed(2),y:+(r.y-rr.y).toFixed(2),w:+r.width.toFixed(2),h:+r.height.toFixed(2)}};
   const appearance=e=>{const s=getComputedStyle(e);return {font:s.fontFamily,size:parseFloat(s.fontSize),weight:s.fontWeight,color:s.color,background:s.backgroundColor,lineHeight:s.lineHeight,letterSpacing:s.letterSpacing,align:s.textAlign}};
   const texts=[...root.querySelectorAll('[data-ui="text"],[data-ui="chip"],svg text')].filter(e=>!e.closest('table')).map((e,i)=>({ref:`t${i}`,text:e.textContent.trim(),ui:e.getAttribute('data-ui')||'svg-text',...bounds(e),style:appearance(e)})).filter(t=>t.text);
   const boxes=[...root.querySelectorAll('[data-ui="box"]')].map((e,i)=>({ref:`b${i}`,...bounds(e),style:appearance(e)}));
   const seats=[...root.querySelectorAll('.seat,[data-ui="placeholder"]')].map((e,i)=>({ref:`seat${i}`,...bounds(e)}));
   const tables=[...root.querySelectorAll('table')].map((e,i)=>({ref:`table${i}`,...bounds(e),rows:[...e.rows].map((r,j)=>[...r.cells].map((c,k)=>({ref:`table${i}-r${j}-c${k}`,text:c.textContent.trim(),header:c.tagName==='TH',rowSpan:c.rowSpan,colSpan:c.colSpan,...bounds(c),style:appearance(c)})))}));
   const svgs=[...root.querySelectorAll('svg')].filter(e=>!e.hasAttribute('data-ui')).map((e,i)=>({ref:`svg${i}`,...bounds(e),hasPolyline:!!e.querySelector('polyline'),hasPath:!!e.querySelector('path'),hasRects:e.querySelectorAll('rect').length,polylines:[...e.querySelectorAll('polyline')].map(p=>p.getAttribute('points')),rects:[...e.querySelectorAll('rect')].map(p=>Object.fromEntries(['x','y','width','height','fill'].map(a=>[a,p.getAttribute(a)]))),lines:[...e.querySelectorAll('line')].map(p=>Object.fromEntries(['x1','x2','y1','y2'].map(a=>[a,Number(p.getAttribute(a))]))),texts:[...e.querySelectorAll('text')].map(t=>({text:t.textContent.trim(),...bounds(t),xLocal:parseFloat(t.getAttribute('x')||'0'),yLocal:parseFloat(t.getAttribute('y')||'0'),anchor:t.getAttribute('text-anchor')}))}));
   return {page:appearance(root),texts,boxes,seats,tables,svgs};
  });
  slides.push({deck:deck.id,id:slide.id,declaredTitle:slide.title,deckTitle:deck.title,source:{url:`/?deck=${deck.id}&slide=${slide.id}`,reference:`public/reference/${deck.id}/slide_${slide.id}.png`},...raw});
 }
 await browser.close(); await fs.writeFile(dataPath,JSON.stringify({schema:'rhetis.slide-assembly-provenance/1',kit,canvas:[1280,720],extractedAt:new Date().toISOString(),method:'Actual browser DOM extraction; all text/bounds/computed styles, native table cells, seat positions and SVG chart text. No source React or reference raster used by assembly renderer.',slides},null,2));
 console.log(`Extracted ${slides.length} slides`);
}
const data=JSON.parse(await fs.readFile(dataPath,'utf8'));
const accents={'053':'#384ba4','054':'#e43240','056':'#344778','057':'#497b31','058':'#e43240','060':'#247946','061':'#2584cd'};
const surfaces={'053':'#f2f2f2','054':'#f6f7f9','056':'#f7f8fc','057':'#ffffff','058':'#fffafa','060':'#fafafa','061':'#f1f2f8'};
const refSpan=t=>`<span data-source-ref="${escape(t.ref)}">${escape(t.text)}</span>`;
const p=(cls,items)=>items.length?`<p class="${cls}">${items.map((t,i)=>(i?(cls==='note'&&t.text.length<65&&items[i-1].text.length<65?' · ':'<br>'):'')+refSpan(t)).join('')}</p>`:'';
const place=(x=1,w=12,y=1,h=6)=>`grid-column:${x} / span ${w}; grid-row:${y} / span ${h}`;
const root=(folder,cls,body,layout,extra='')=>`<div class="${cls}" data-el="${kit}-${folder}" style="${layout};${extra}">${body}</div>`;
function numeric(t){return /^[-+]?\d[\d,.]*(?:\s*(?:%|억|만|원|명|건|개|점|배|일|시간|개월|년|조|천|P|p|%p|원\s*이상))*$/.test(clean(t.text));}
function findTitle(s){
 const ts=s.texts.filter(t=>t.ui!=='svg-text'&&t.text.length>1&&!numeric(t));
 let exact=ts.find(t=>norm(t.text)===norm(s.declaredTitle));
 if(exact)return exact;
 const contained=ts.filter(t=>norm(t.text).includes(norm(s.declaredTitle))&&norm(s.declaredTitle).length>3).sort((a,b)=>b.style.size-a.style.size)[0];
 if(contained)return contained;
 const candidates=ts.filter(t=>t.style.size>=28&&!/MIRI\s?COMPANY|BUSINESS PROJECT|REPORT|템플릿 모음집/i.test(t.text));
 return candidates.sort((a,b)=>((b.y<350?1:0)*100+b.style.size)-((a.y<350?1:0)*100+a.style.size))[0]||ts[0];
}
function groupTexts(s,ts){
 const panels=s.boxes.filter(b=>b.w>140&&b.h>75&&b.w*b.h<720000&&b.y>95&&b.y<660);
 const map=new Map(),unassigned=[];
 for(const t of ts){
  const within=panels.filter(b=>t.x>=b.x-5&&t.x+t.w<=b.x+b.w+8&&t.y>=b.y-5&&t.y+t.h<=b.y+b.h+8).sort((a,b)=>a.w*a.h-b.w*b.h);
  if(within.length){const b=within[0];if(!map.has(b.ref))map.set(b.ref,{rect:b,items:[]});map.get(b.ref).items.push(t);}else unassigned.push(t);
 }
 let groups=[...map.values()];
 // Leftover text joins the nearest authored panel when the original placement is close.
 for(const t of unassigned){
  const nearby=groups.filter(g=>!g.key).map(g=>{const b=g.rect,cx=Math.abs(t.x+t.w/2-b.x-b.w/2),overlap=Math.max(0,Math.min(t.x+t.w,b.x+b.w)-Math.max(t.x,b.x)),edgeX=Math.max(b.x-t.x-t.w,t.x-b.x-b.w,0),edgeY=Math.max(b.y-t.y-t.h,t.y-b.y-b.h,0),aligned=overlap>=Math.min(t.w,b.w)*.65&&cx<Math.min(t.w,b.w)*.45,above=t.y+t.h<=b.y+12;return {g,d:Math.hypot(edgeX,edgeY)+cx*(aligned?.15:.65),acceptable:(aligned&&above&&edgeY<210)||(edgeY<90&&edgeX<25&&cx<180)};}).filter(v=>v.acceptable).sort((a,b)=>a.d-b.d)[0];
  if(nearby){nearby.g.items.push(t);}else{
   const col=Math.min(2,Math.max(0,Math.floor((t.x+t.w/2)/427))),row=t.y<390?0:1,key=`area-${col}-${row}`;
   let g=groups.find(g=>g.key===key);if(!g){g={key,rect:{x:col*427,y:140+row*270,w:427,h:270},items:[]};groups.push(g);}g.items.push(t);
  }
 }
 groups=groups.filter(g=>g.items.length).map(g=>({...g,items:g.items.sort((a,b)=>a.y-b.y||a.x-b.x)}));
 while(groups.length>6){
  let min=Infinity,pair=[0,1];for(let i=0;i<groups.length;i++)for(let j=i+1;j<groups.length;j++){const d=Math.hypot(groups[i].rect.x-groups[j].rect.x,groups[i].rect.y-groups[j].rect.y);if(d<min){min=d;pair=[i,j]}}
  const [i,j]=pair;groups[i].items.push(...groups[j].items);groups.splice(j,1);
 }
 return groups.sort((a,b)=>Math.abs(a.rect.y-b.rect.y)>80?a.rect.y-b.rect.y:a.rect.x-b.rect.x);
}
function authoredText(cls,items,size){return items.length?`<p class="${cls}" style="font-size:var(--type-${size});line-height:1.35">${items.map((t,i)=>(i?(cls==='note'&&t.text.length<65&&items[i-1].text.length<65?' · ':'<br>'):'')+refSpan(t)).join('')}</p>`:'';}
function card(g,layout,idx=0){
 const items=g.items,figure=(g.forceCard?[]:items).filter(t=>numeric(t)&&t.style.size>=28).sort((a,b)=>b.style.size-a.style.size)[0];
 const headings=items.filter(t=>t!==figure&&!numeric(t)&&t.text.length<110&&!/^[^\p{L}\p{N}]+$/u.test(t.text)).sort((a,b)=>b.style.size-a.style.size||a.y-b.y),head=headings[0]||items.find(t=>t!==figure);
 const rest=items.filter(t=>t!==head&&t!==figure);
 if(figure&&/^\d+(?:\.\d+)?%$/.test(figure.text)&&!rest.length)return root('chart-donut','donut',p('fig',[figure])+p('name',head?[head]:[]),layout,`--v:${parseFloat(figure.text)};--pad:18px;`);const folder=figure?'metric':'card',cls=figure?'stat':'card';
 const spanRows=Number(layout.match(/grid-row:\d+ \/ span (\d+)/)?.[1]||6),pad=g.forceCard?8:spanRows>=3?20:12;return root(folder,cls,`<div class="parts">${figure?p('fig',[figure]):''}${head?authoredText('name',[head],head.text.length>30?18:22):''}${authoredText('note',rest,16)}</div>`,layout,`--pad:${pad}px;--gap-sm:8px;--body-line:1.3;`);
}
function list(g,layout){const items=g.items;return root('list','list divided',items.map(t=>`<div class="item">${p('name',[t])}</div>`).join(''),layout,'--gap:8px;--gap-sm:6px;--body-line:1.4;');}
function flow(groups,layout,kind){
 const step=kind==='steps'?'step':'stop',cls=kind==='steps'?'steps':'track',folder=kind;
 return root(folder,cls,groups.map((g,i)=>{const first=g.items[0],rest=g.items.slice(1);return `<div class="${step}">${kind==='steps'?`<span class="mark">${i+1}</span>`:''}${p(kind==='steps'?'name':'kick',[first])}${p(kind==='steps'?'note':'name',kind==='steps'?rest:rest.slice(0,1))}${p('note',kind==='steps'?[]:rest.slice(1))}</div>`}).join(''),layout,'--gap:18px;--pad:18px;--body-line:1.35;');
}
function tableMarkup(table,layout){return root('table','tablebox',`<table class="table"><thead>${table.rows.slice(0,1).map(row=>`<tr>${row.map(c=>`<th${c.colSpan>1?` colspan="${c.colSpan}"`:''}>${refSpan(c)}</th>`).join('')}</tr>`).join('')}</thead><tbody>${table.rows.slice(1).map(row=>`<tr>${row.map(c=>`<td${numeric(c)?' class="num"':''}${c.colSpan>1?` colspan="${c.colSpan}"`:''}>${refSpan(c)}</td>`).join('')}</tr>`).join('')}</tbody></table>`,layout,'--gap-sm:7px;--body-line:1.3;');}
function inferSvgSeries(svg,ts){
 const raw=svg.texts||[];const numericLabels=raw.filter(t=>/^\d[\d,.]*$/.test(t.text));
 const axis=numericLabels.filter(t=>t.anchor==='end'||t.xLocal<30).sort((a,b)=>parseFloat(a.text.replaceAll(',',''))-parseFloat(b.text.replaceAll(',','')));
 const longest=(svg.polylines||[]).map(p=>p.trim().split(/\s+/).map(pair=>pair.split(',').map(Number))).sort((a,b)=>b.length-a.length)[0];
 if(longest?.length>=3&&axis.length>=2){
  const lo=axis[0],hi=axis[axis.length-1],low=parseFloat(lo.text.replaceAll(',','')),high=parseFloat(hi.text.replaceAll(',',''));
  const grids=(svg.lines||[]).filter(l=>l.y1===l.y2&&Math.abs(l.x2-l.x1)>150);
  const nearY=y=>grids.sort((a,b)=>Math.abs(a.y1-y)-Math.abs(b.y1-y))[0]?.y1??y;
  const bottom=nearY(lo.yLocal),top=nearY(hi.yLocal);if(bottom===top)return null;
  const labels=ts.filter(t=>t.x>svg.x+40&&t.x<svg.x+svg.w&&t.y>svg.y+svg.h-45&&t.y<svg.y+svg.h+45&&!numeric(t));
  return {kind:'chart-line',derived:true,svg,values:longest.map(([x,y],i)=>{const value=Math.round((low+(bottom-y)/(bottom-top)*(high-low))*10)/10;const label=labels.sort((a,b)=>Math.abs(a.x+a.w/2-(svg.x+x))-Math.abs(b.x+b.w/2-(svg.x+x)))[0];return {source:{ref:`${svg.ref}-point${i}`,text:String(value),provenance:{svg:svg.ref,point:[x,y],axis:{bottom,top,low,high},method:'linear numeric axis interpolation from original SVG geometry'}},value,label}})};
 }
 if(svg.hasRects>=2&&numericLabels.length>=2){
  const sorted=[...numericLabels].sort((a,b)=>parseFloat(a.text.replaceAll(',',''))-parseFloat(b.text.replaceAll(',',''))),lo=sorted[0],hi=sorted[sorted.length-1];
  const max=parseFloat(hi.text.replaceAll(',','')),scale=hi.xLocal-lo.xLocal;if(scale<=0)return null;
  const values=(svg.rects||[]).filter(r=>+r.width>20&&+r.height>5&&+r.height<100).map((r,i)=>{const value=Math.round(+r.width/scale*max*10)/10;return {source:{ref:`${svg.ref}-rect${i}`,text:String(value),provenance:{svg:svg.ref,rect:r,method:'original SVG rect width divided by labeled x-axis range'}},value,label:undefined}});
  if(values.length>=2)return {kind:'chart-bar',derived:true,svg,values};
 }
 return null;
}
function chartFromSource(s,ts){
 for(const svg of s.svgs.filter(v=>v.w>220&&v.h>120&&(v.hasRects>1||(v.polylines||[]).some(p=>p.trim().split(/\s+/).length>=4)))){
  const nums=ts.filter(t=>t.x>=(t.ui==='svg-text'?svg.x+30:svg.x-30)&&t.x<=svg.x+svg.w-10&&t.y>=svg.y-30&&t.y<=svg.y+svg.h&&numeric(t)&&t.text.length<10);
  if((svg.hasRects>1&&nums.length&&Math.max(...nums.map(t=>t.y))-Math.min(...nums.map(t=>t.y))<8)||nums.length<2||nums.length>30){const inferred=inferSvgSeries(svg,ts);if(inferred)return inferred;continue;}
  let values=nums.filter(t=>!/^20\d\d$/.test(t.text)&&parseFloat(t.text.replaceAll(',',''))>=0);values=values.filter(v=>values.filter(t=>Math.abs(t.x-v.x)<2).length<3);const clusters=[];for(const v of values){let col=clusters.find(c=>Math.abs(c[0].x-v.x)<12);if(!col){col=[];clusters.push(col);}col.push(v);}if(clusters.length>=3&&clusters.filter(c=>c.length>=2).length>=3)values=clusters.map(c=>c[0]);const runs=[[]];for(const v of values){const last=runs[runs.length-1];if(last.length&&v.x<last[last.length-1].x-35)runs.push([v]);else last.push(v);}if(runs.length>1)values=runs.sort((a,b)=>b.length-a.length)[0];if(values.length>12)values=values.slice(0,12);
  if(values.length<2)continue;
  const labels=ts.filter(t=>!numeric(t)&&t.text.length<20&&t.x>=svg.x-70&&t.x<=svg.x+svg.w+50&&t.y>=svg.y+svg.h-100&&t.y<=svg.y+svg.h+60&&(/^(?:\d{1,2}월(?:\s*\d주)?|\d주차|Week\s*\d+|20\d{2})$/.test(clean(t.text))||t.y>=svg.y+svg.h-20));const assignedLabels=new Set();
  return {kind:svg.hasPolyline?'chart-line':'chart-bar',values:values.map((v,i)=>{const label=labels.filter(t=>!assignedLabels.has(t.ref)).sort((a,b)=>Math.abs(a.x+a.w/2-v.x-v.w/2)-Math.abs(b.x+b.w/2-v.x-v.w/2))[0];const use=label&&Math.abs(label.x+label.w/2-v.x-v.w/2)<45?label:null;if(use)assignedLabels.add(use.ref);return {source:v,value:parseFloat(v.text.replaceAll(',','')),label:use}}),svg};
 }
 const shares=ts.filter(t=>/^\d+(?:\.\d+)?\s*%$/.test(clean(t.text))&&parseFloat(t.text)<=100);if(shares.length>=2&&shares.length<=6&&/비중|분포|점유|종합 평가|주요 이슈 현황/.test(s.declaredTitle)){const used=new Set();return {kind:'chart-donut',values:shares.map(v=>{const label=ts.filter(t=>!numeric(t)&&t.text.length<16&&!used.has(t.ref)).sort((a,b)=>Math.hypot(a.x-v.x,a.y-v.y)-Math.hypot(b.x-v.x,b.y-v.y))[0];if(label)used.add(label.ref);return {source:v,value:parseFloat(v.text),label}})};}return null;
}
function chartMarkup(chart,layout){if(chart.kind==='chart-donut')return root('chart-donut','donuts',chart.values.map(v=>`<div class="donut" data-el="report-forge-chart-donut" style="--v:${v.value}"><p class="fig">${refSpan(v.source)}</p><p class="name">${v.label?refSpan(v.label):''}</p></div>`).join(''),layout,'--gap:24px;--pad:16px;');const line=chart.kind==='chart-line';return root(chart.kind,line?'lines':'bars',chart.values.map(v=>`<div class="${line?'pt':('bar'+(chart.values.indexOf(v)===chart.values.length-1?' on':''))}" style="--v:${v.value}"><b>${refSpan(v.source)}</b><span>${v.label?refSpan(v.label):''}</span></div>`).join(''),layout,`--max:${Math.max(...chart.values.map(v=>v.value))*1.15};--pad:18px;`);}
function agenda(s,ts,layout){
 let groups=groupTexts(s,ts);if(groups.length<2)return null;
 return root('agenda','agenda',groups.map((g,i)=>{const first=g.items.find(t=>!numeric(t))||g.items[0],rest=g.items.filter(t=>t!==first);return `<div class="entry${i===0?' on':''}"><span class="mark">${String(i+1).padStart(2,'0')}</span>${p('name',[first])}${p('note',rest)}</div>`}).join(''),layout,'--pad:12px;--gap:16px;--gap-sm:4px;--body-line:1.3;');
}
function diagramMarkup(kind,groups,layout,title){
 const members=groups.map(g=>{const head=g.items.filter(t=>!numeric(t)&&t.text.length<80).sort((a,b)=>b.style.size-a.style.size)[0]||g.items[0];return {head,rest:g.items.filter(t=>t!==head)}});
 if(kind==='person')return root('person','people',members.map((m,i)=>`<div class="person" data-el="report-forge-person"><div class="seat avatar" data-ph="${i+1}"></div>${p('name',m.head?[m.head]:[])}${p('note',m.rest)}</div>`).join(''),layout,'--pad:16px;--gap:20px;--gap-sm:10px;--body-line:1.4;');
 if(kind==='hierarchy')return root('hierarchy','org',`<div class="root">${escape(title)}</div>`+members.map(m=>`<div class="branch"><div class="node">${refSpan(m.head)}</div>${m.rest.map(t=>`<div class="leaf">${refSpan(t)}</div>`).join('')}</div>`).join(''),layout,'--gap:16px;--gap-sm:8px;--pad:14px;--body-line:1.4;');
 if(kind==='matrix'){
  const cells=Array.from({length:4},(_,i)=>members[i]||{head:null,rest:[]});if(members.length>4)cells[3].rest.push(...members.slice(4).flatMap(m=>[m.head,...m.rest]));
  return root('matrix','matrix',`<div class="axis-x"><span></span><span></span></div><div class="axis-y"><span></span><span></span></div>`+cells.map((m,i)=>`<div class="cell${i===0?' on':''}">${p('name',m.head?[m.head]:[])}${p('note',m.rest)}</div>`).join(''),layout,'--gap:12px;--gap-sm:8px;--pad:18px;--body-line:1.4;');
 }
 const child=kind==='cycle'?'node':'spoke';return root(kind,kind,`<div class="core">${escape(title)}</div>`+members.map((m,i)=>`<div class="${child}">${kind==='hub'?`<span class="mark">${i+1}</span>`:''}${p('name',m.head?[m.head]:[])}${p('note',m.rest)}</div>`).join(''),layout,'--gap:12px;--gap-sm:8px;--pad:16px;--body-line:1.35;');
}
function spatialGroups(s,ts,kind){
 const numericAnchors=ts.filter(t=>/^(?:0[1-9]|[1-9])(?:\s|$)/.test(t.text)&&t.style.size>=18);
 const dateAnchors=ts.filter(t=>/^(?:\d{1,2}월|MON|TUE|WED|THU|FRI|SAT|SUN|20\d\d[.\-/]\d\d(?:[.\-/]\d\d)?)$/.test(clean(t.text)));
 let anchors=kind==='agenda'?numericAnchors:dateAnchors;
 if(anchors.length<2||anchors.length>(kind==='agenda'?12:8)){
  const heads=ts.filter(t=>t.style.size>=22&&t.text.length<60&&!numeric(t));
  anchors=heads.length>=2&&heads.length<=6?heads:[];
 }
 if(!anchors.length)return groupTexts(s,ts);
 const groups=anchors.map(a=>({rect:{x:a.x,y:a.y,w:180,h:350},items:[a],anchor:a}));
 for(const t of ts.filter(t=>!anchors.includes(t))){
  const g=groups.map(g=>({g,d:(kind==='agenda'?(t.x>=g.anchor.x-5&&t.x<g.anchor.x+250?Math.abs(t.x-g.anchor.x)*.1:Math.abs(t.x-g.anchor.x)+250):Math.abs(t.x-g.anchor.x))+Math.abs(t.y-g.anchor.y)*.08})).sort((a,b)=>a.d-b.d)[0].g;g.items.push(t);
 }
 return groups.map(g=>({...g,items:[g.anchor,...g.items.filter(t=>t!==g.anchor).sort((a,b)=>a.y-b.y||a.x-b.x)]})).sort((a,b)=>Math.abs(a.rect.y-b.rect.y)>70?a.rect.y-b.rect.y:a.rect.x-b.rect.x);
}
function authoredAgenda(g,index,layout){
 const first=g.items.find(t=>!numeric(t))||g.items[0],anchor=g.items.find(t=>/^0?[1-9]$/.test(t.text))||(/^(?:0[1-9]|[1-9])\s/.test(first.text)?first:null),mark=anchor?.text.match(/^(?:0[1-9]|[1-9])/)[0]||String(index+1).padStart(2,'0');
 const heading={...first,text:first.text.replace(/^(?:0[1-9]|[1-9])\s+/,'')},rest=g.items.filter(t=>t!==first&&t!==anchor);
 return root('agenda','agenda',`<div class="entry on"><span class="mark">${anchor?refSpan({...anchor,text:mark}):mark}</span>${authoredText('name',[heading],heading.text.length>30?18:22)}${authoredText('note',rest,16)}</div>`,layout,'--pad:16px;--gap:12px;--gap-sm:6px;--body-line:1.35;');
}
// Page authorship preserves source relationships when geometry alone is ambiguous.
function authoredSemantic(s){
 const key=s.deck+'/'+s.id, refs=new Set(), G=n=>s.texts.find(t=>t.ref==='t'+n), R=n=>{const t=G(n);if(!t)return '';refs.add(t.ref);return refSpan(t).replace('<span ', '<span style="position:static;display:inline;width:auto;max-width:none;font:inherit;line-height:inherit" ')}, A=(cls,ids,size=16)=>`<p class="${cls}" style="display:block;font-size:var(--type-${size});line-height:1.35">${ids.map(R).join('<br>')}</p>`, M=(ids)=>{ids.forEach(n=>refs.add('t'+n));return ids.reduceRight((a,n)=>`<span data-source-ref="t${n}">${a}</span>`,escape(G(ids[0]).text))},
 C=(name,notes,layout,size=22)=>root('card','card',`<div class="parts">${A('name',[name],size)}${A('note',notes,16)}</div>`,layout,'--pad:20px;--gap-sm:8px;'),
 T=(headers,rows,layout=place(),size=16,caption='')=>root('table','tablebox',`<table class="table" style="font-size:var(--type-${size});line-height:1.35">${caption?`<caption style="text-align:left;margin-bottom:10px;font-size:var(--type-18)">${caption}</caption>`:''}<thead><tr>${headers.map((v,i)=>`<th${i===0&&headers.length>10?' style="width:140px"':''}>${v}</th>`).join('')}</tr></thead><tbody>${rows.map(row=>`<tr>${row.map(v=>typeof v==='object'?`<td colspan="${v.span}">${v.html}</td>`:`<td>${v}</td>`).join('')}</tr>`).join('')}</tbody></table>`,layout,'--gap-sm:8px;'),
 steps=(rows,layout=place())=>root('steps','steps',rows.map((r,i)=>`<div class="step"><span class="mark">${r.mark?R(r.mark):i+1}</span>${A('name',[r.name],22)}${A('note',r.note,16)}</div>`).join(''),layout,'--pad:18px;--gap:20px;--gap-sm:10px;'),
 seriesLegend=(ids,colors,layout)=>root('legend','legend',ids.map((n,i)=>`<span class="key" style="--accent:${colors[i]==='var(--accent)'?accents[s.deck]:colors[i]};font-size:var(--type-14)">${R(n)}</span>`).join(''),layout,'--gap:24px;'),
 legend=(ids,layout,label='')=>root('legend','legend',`${label?`<span class="key tone-1">${label}</span>`:''}${ids.map(n=>`<span class="key tone-2" style="font-size:var(--type-14)">${R(n)}</span>`).join('')}`,layout,'--gap:14px;'),
 line=(values,labels,layout,max)=>root('chart-line','lines',values.map((v,i)=>`<div class="pt" style="--v:${typeof v==='number'?parseFloat(G(v).text.replaceAll(',','')):v.value}"><b>${typeof v==='number'?R(v):v.html}</b><span>${R(labels[i])}</span></div>`).join(''),layout,`--max:${max};--pad:16px;`),
 bars=(values,labels,layout,max)=>root('chart-bar','bars',values.map((v,i)=>`<div class="bar${i%2?' on':''}" style="--v:${v.value};${i%2?'':'--accent:var(--line)'}"><b>${v.html}</b><span style="${i%2?'':'width:calc(200% + 18px);left:0;max-width:none'}">${i%2?'':R(labels[i/2])}</span></div>`).join(''),layout,`--max:${max};--pad:16px;`),
 metric=(name,fig,notes,layout)=>root('metric','stat',`<div class="parts">${A('fig',[fig],44)}${A('name',[name],22)}${A('note',notes,16)}</div>`,layout,'--pad:18px;--gap-sm:10px;'),
 result=(html,lead=[])=>({html,refs:[...refs],lead:lead.map(n=>'t'+n)}),
 gantt=(months,rows,layout=place(),caption='')=>T(['',...months.map(R)],rows.map(row=>[R(row.name),{span:months.length,html:`<div style="height:${row.bars.length>1?72:48}px;position:relative">${row.bars.map((b,i)=>`<span style="position:absolute;left:${b.start*100}%;width:${b.width*100}%;top:${i*34}px;min-height:30px;display:flex;align-items:center;justify-content:center;background:var(--accent);color:var(--accent-ink);padding:4px 6px;font-size:var(--type-12);line-height:1.2;border-radius:4px">${R(b.note)}</span>`).join('')}</div>`}]),layout,14,caption),
 matrix=(cells,axes,layout=place())=>root('matrix','matrix',`<div class="axis-x"><span>${axes.x[0]}</span><span>${axes.x[1]}</span></div><div class="axis-y"><span>${axes.y[0]}</span><span>${axes.y[1]}</span></div>${cells.map((html,i)=>`<div class="cell${i===0?' on':''}" style="position:relative;padding:16px;gap:8px">${html}</div>`).join('')}`,layout,'--gap:16px;--gap-sm:10px;'),
 pointMatrix=(points,axes,layout)=>{const cells=[[],[],[],[]];for(const pt of points){const col=pt.x>=.5?1:0,row=pt.y>=.5?1:0,lx=(pt.x-col*.5)*200,ly=(pt.y-row*.5)*200;cells[row*2+col].push(`<span style="position:absolute;left:${lx}%;top:${ly}%;transform:translate(-50%,-50%);display:block;width:12px;height:12px;border-radius:50%;background:var(--accent)"></span><p class="name" style="position:absolute;left:clamp(90px,${lx}%,calc(100% - 90px));top:calc(${ly}% + 12px);transform:translateX(-50%);width:180px;text-align:center;font-size:var(--type-14);line-height:1.25">${R(pt.ref)}</p>`)}return matrix(cells.map(c=>c.join('')),axes,layout)};
 if(key==='058/12')return result(steps([{name:5,note:[6,7,14]},{name:8,note:[9,10,15]},{name:11,note:[12,13,16]}]),[3]);
 if(key==='058/14')return result(root('cycle','cycle',`<div class="core" style="width:30%;left:35%;height:30%;top:35%;padding:14px;--ink-2:var(--accent-ink)">${A('name',[4],22)}${A('note',[5],16)}</div>${[[6,7],[8,9],[12,13],[10,11]].map(([n,d])=>`<div class="node" style="padding:8px;gap:4px">${A('name',[n],22)}${A('note',[d],16)}</div>`).join('')}`,place(),'--pad:12px;--gap-sm:4px;'));
 if(key==='058/15'){refs.add('t25');s.semanticInterpretation='Week8 source t25 explicitly reads 1만 달성; numeric value = 10000.';return result(line([10,11,12,13,14,15,16,{value:10000,html:R(25)}],[17,18,19,20,21,22,23,24],place(1,12,1,4),11000)+C(5,[6],place(1,6,5,2))+C(7,[8],place(7,6,5,2)),[9]);}
 if(key==='058/16')return result(T(['',... [4,5,6,7].map(R)],[[8,13,14,15,16],[9,17,18,19,20],[10,21,22,23,24],[11,25,26,27,28]].map(row=>row.map(R)).concat([[R(12),{span:4,html:R(29)}]]),place(),18));
 if(key==='058/17'){
  const panel=(title,pairs,desc,x)=>root('card','card',`${A('name',[title],22)}<div class="donuts" data-el="report-forge-chart-donut" style="height:230px;gap:10px">${pairs.map(([name,val])=>`<div class="donut" data-el="report-forge-chart-donut" style="--v:${parseFloat(G(val).text)}"><p class="fig">${R(val)}</p>${A('name',[name],name===20?16:18)}</div>`).join('')}</div>${A('note',[desc],16)}`,place(x,6,1,6),'--pad:18px;--gap-sm:16px;');
  return result(panel(4,[[8,7],[9,6],[10,5]],11,1)+panel(12,[[17,14],[18,15],[19,13],[20,16]],21,7));}
 if(key==='058/18')return result(gantt(Array.from({length:12},(_,i)=>i+4),[{name:16,bars:[{note:16,start:.01646,width:.30106}]},{name:17,bars:[{note:17,start:.26718,width:.21878}]},{name:18,bars:[{note:18,start:.38045,width:.24588}]},{name:19,bars:[{note:19,start:.50823,width:.23136}]},{name:20,bars:[{note:20,start:.50823,width:.4637}]}],place(1,12,1,5))+root('callout','callout',A('name',[21],18)+A('note',[22],16),place(1,12,6,1),'--pad:12px;--gap-sm:8px;'));
 if(key==='054/04'){
  const vals=[11,12,13,14,15,16,17,18].map(n=>({value:parseFloat(G(n).text),html:R(n)}));
  const lines=`<div class="group" style="${place(7,6,1,3)};position:relative">${line([19,20,21,22],[27,28,29,30],'position:absolute;inset:0',110)}${line([23,24,25,26],[27,28,29,30],'position:absolute;inset:0;--accent:var(--tone-2)',110)}</div>`;
  return result(bars(vals,[27,28,29,30],place(1,6,1,3),65)+lines+seriesLegend([31,32],['var(--surface-2)','var(--accent)'],place(1,6,4,1))+seriesLegend([33,34],['var(--accent)','var(--tone-2)'],place(7,6,4,1))+[35,37,39].map((n,i)=>C(n,[n+1],place(i*4+1,4,5,2),18)).join('')+`<div class="group" style="${place(7,6,4,1)};align-self:end;font-size:var(--type-12)">고객축: ${[5,6,7,8,9,10].map(R).join(' · ')}</div>`,[4]);}
 if(key==='054/06')return result(T([4,5,6,7].map(R),[[8,9,10,11,12,13],[14,15,16,17,18,19],[20,21,22,23,24,25]].map(([a,b,c,d,e,f])=>[R(a),R(b),`${R(c)}<br><small>${R(d)} ↔ ${R(e)}</small>`,R(f)]),place(),16));
 if(key==='054/20')return result(pointMatrix([{ref:5,x:.821,y:.1815},{ref:6,x:.535,y:.305},{ref:7,x:.798,y:.538},{ref:8,x:.498,y:.808}],{x:[R(13),`${R(12)} · ${R(14)}`],y:[`${R(9)} · ${R(10)}`,R(11)]},place(1,6,1,6))+[15,17,19,21].map((n,i)=>C(n,[n+1],place(7+(i%2)*3,3,1+Math.floor(i/2)*3,3),18)).join(''),[4]);
 if(key==='056/02')return result([[2,3,4,5],[6,7,8,9],[10,11,12,13]].map(([word,num,title,note],i)=>root('agenda','agenda',`<div class="entry on"><span class="mark" style="display:flex;flex-direction:column;font-size:var(--type-18)">${R(word)} ${R(num)}</span>${A('name',[title],22)}${A('note',[note],16)}</div>`,place(i*4+1,4,1,6),'--pad:20px;--gap-sm:10px;')).join(''),[1]);
 if(key==='056/13')return result([[5,6,7,8,9,10,11],[12,13,14,15,16,17,18],[19,20,21,22,23,24,25],[26,27,28,29,30,31,32]].map(([name,val,goal,gv,base,bv,note],i)=>root('metric','stat',`<div class="parts">${A('fig',[val],44)}${A('name',[name],22)}<p class="note" style="font-size:var(--type-16);line-height:1.5">${R(goal)}: <strong>${R(gv)}</strong><br>${R(base)}: ${R(bv)}<br>${R(note)}</p></div>`,place(1+i*3,3,1,6),'--pad:20px;--gap-sm:14px;')).join(''));
 if(key==='056/14')return result(matrix([[5,13,14],[6,15,16],[7,17,18],[8,19,20]].map(([name,alias,note])=>`<p class="name" style="font-size:var(--type-22)">${M([name,alias])}</p>${A('note',[note],16)}`),{x:['',`${R(11)} ${R(10)}`],y:[`${R(9)} ${R(12)}`,'']}));
 if(key==='056/17')return result(steps([{mark:5,name:6,note:[7,8]},{mark:9,name:10,note:[11,12]},{mark:13,name:14,note:[15,16]},{mark:17,name:18,note:[19,20]}]));
 if(key==='056/18'){
  const embed=(whole,part)=>{refs.add('t'+whole);refs.add('t'+part);return `<span data-source-ref="t${whole}">${escape(G(whole).text).replace(escape(G(part).text),`<span data-source-ref="t${part}">${escape(G(part).text)}</span>`)}</span>`};
  return result(metric(5,6,[],place(1,3,1,2))+C(7,[8,9,10],place(1,3,3,4),18)+T(['번호','항목','금액 · 비중','활용 계획'],[[21,22,23,24,11,12],[25,26,27,28,13,14],[29,30,31,32,15,16],[33,34,35,36,17,18],[37,38,39,40,19,20]].map(([num,name,amount,note,alias,av])=>[R(num),M([name,alias]),embed(amount,av),R(note)]),place(4,9,1,6),14));}
 if(key==='056/19')return result(T([5,6,7].map(R),[[8,9,10],[11,12,13],[14,15,16],[17,18,19]].map(row=>row.map(R)),place(1,8,1,6),22)+`<div class="stack" style="${place(9,4,1,6)}">${root('pill','pill',A('name',[20],18),'','--pad:12px;')}${metric(21,22,[],'')}${metric(23,24,[],'')}</div>`);
 if(key==='057/02')return result([[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23]].map(([mark,name,note],i)=>root('agenda','agenda',`<div class="entry on"><span class="mark">${R(mark)}</span>${A('name',[name],22)}${A('note',[note],16)}</div>`,place(1+i%2*6,6,1+Math.floor(i/2)*2,2),'--pad:16px;--gap-sm:6px;')).join(''));
 if(key==='057/04')return result(C(7,[9,11,13,15],place(1,5,1,4))+line([21,23,25,27],[22,24,26,28],place(6,7,1,4),90)+legend([16,17,18,19,20],place(6,7,5,1),'세로축')+root('callout','callout',A('name',[29],22)+A('note',[31,33],16),place(1,12,6,1),'--pad:12px;--gap-sm:8px;'));
 if(key==='057/09')return result(gantt([10,11,12,13,14,15],[{name:16,bars:[{note:22,start:.0107,width:.155}]},{name:17,bars:[{note:23,start:.1667,width:.1944}]},{name:18,bars:[{note:24,start:.1667,width:.1944},{note:25,start:.3707,width:.2724}]},{name:19,bars:[{note:26,start:.3707,width:.3333}]},{name:20,bars:[{note:27,start:.4316,width:.1282},{note:28,start:.6635,width:.1282}]},{name:21,bars:[{note:29,start:.75,width:.2222}]}]));
 if(key==='060/06'){
  refs.add('t19');s.semanticInterpretation='Six original SVG bar heights [88,132,176,220,264,308] on 0–80 axis baseline352 yield20/30,40/50,60/70 for3 categories and2 periods.';
  const values=[20,30,40,50,60,70].map((value,i)=>({value,html:`<span style="position:static;font:inherit" data-source-ref="svg3-rect${i}">${value}</span>`}));
  return result(`<div class="stack" style="${place(1,4,1,6)}">${metric(4,5,[],'')}${metric(6,7,[],'')}${metric(8,9,[],'')}</div>`+bars(values,[16,17,18],place(5,8,1,4),80)+root('legend','legend',`<span class="key" style="--accent:var(--surface-2)" data-source-ref="t19">4월 5주차</span><span class="key" data-source-ref="t19">5월 1주차</span>`,place(5,8,5,1),'--gap:28px;')+legend([11,12,13,14,15],place(5,8,6,1),'세로축'),[10]);}
 if(key==='060/07')return result(root('chart-donut','donuts',[[4,19,5,20],[6,13,7,14],[8,15,9,16],[10,17,11,18]].map(([name,alias,val,av])=>`<div class="donut" data-el="report-forge-chart-donut" style="--v:${parseFloat(G(val).text)}"><p class="fig">${M([val,av])}</p><p class="name" style="font-size:var(--type-22)">${M([name,alias])}</p></div>`).join(''),place(1,12,1,5),'--gap:20px;--pad:18px;')+legend([21],place(1,12,6,1)),[12]);
 if(key==='060/14')return result(matrix([[4,8,9,10],[5,11,12,13],[6,14,15,16],[7,17,18,19]].map(([letter,title,sub,note])=>`${A('fig',[letter],36)}${A('name',[title],22)}${A('name',[sub],18)}${A('note',[note],14)}`),{x:['',''],y:['','']}));
 if(key==='060/18'){
  s.semanticInterpretation='Original SVG widths scaled by labeled x-axis0–50 yield self/competitor pairs40/30 and48/35; source category labels both read키워드.';
  const names=['자사','경쟁사'];const panel=(label,values,y)=>root('card','card',`${A('name',[label],22)}${root('chart-bar','bars h',values.map((v,i)=>`<div class="bar${i===0?' on':''}" style="--v:${v};${i===1?'--accent:var(--line)':''}"><b data-source-ref="svg0-rect${(y===1?0:2)+i}">${v}</b><span>${names[i]}</span></div>`).join(''),'height:70px;min-height:70px;flex:0 0 70px;--max:50;--gap-lg:4px;--gap:4px;--gap-sm:4px;')}`,place(1,12,y,2),'--pad:14px;--gap-sm:10px;');
  return result(panel(10,[40,30],1)+panel(11,[48,35],3)+legend([12,4,5,6,7,8,9],place(1,12,5,1))+root('callout','callout',A('note',[13],16),place(1,12,6,1),'--pad:14px;'));
 }
 if(key==='060/20')return result(T([5,6,7].map(R),[[8,9,10],[11,12,13],[14,15,16],[17,18,19]].map(row=>row.map(R)),place(1,4,1,4),16,R(4))+root('callout','callout',A('note',[28],16),place(1,4,5,2),'--pad:16px;')+pointMatrix([{ref:24,x:.205,y:.195},{ref:25,x:.8775,y:.315},{ref:26,x:.48,y:.655},{ref:27,x:.1975,y:.87}],{x:[R(22),R(23)],y:[R(20),R(21)]},place(5,8,1,6)));
 if(key==='060/23')return result(steps([{name:4,note:[5]},{name:6,note:[7]},{name:8,note:[9]},{name:10,note:[11]}]));
 if(key==='060/25')return result(gantt([5,6,7,8,9],[{name:10,bars:[{note:11,start:0,width:.3005}]},{name:12,bars:[{note:13,start:.19896,width:.201}]},{name:14,bars:[{note:15,start:.19896,width:.40207}]},{name:16,bars:[{note:17,start:.601,width:.20725}]},{name:18,bars:[{note:19,start:.4,width:.6}]}],place(),R(4)));
 return null;
}

function authoredCharts(s){
 const get=ref=>s.texts.find(t=>t.ref===ref),use=ids=>ids.map(get),stat=(name,figure,note)=>root('metric','stat',`<div class="parts">${authoredText('fig',use([figure]),s.deck==='056'?44:52)}${authoredText('name',use([name]),22)}${note?authoredText('note',use([note]),16):''}</div>`,'','--gap-sm:6px;--body-line:1.35;');
 if(s.deck==='056'&&s.id==='04'){
  const actual=['t11','t14','t17','t20','t23','t26'],target=['t12','t15','t18','t21','t24','t27'],labels=['t13','t16','t19','t22','t25','t28'],axis=['t7','t8','t9','t10'];
  const chart={kind:'chart-line',values:actual.map((ref,i)=>({source:get(ref),value:parseFloat(get(ref).text),label:get(labels[i])}))};
  const chartHtml=chartMarkup(chart,place(1,8,1,4));
  const stats=`<div class="stack" style="${place(9,4,1,6)}">${stat('t30','t32','t31')}${stat('t33','t35','t34')}${stat('t36','t38','t37')}</div>`;
  const table=`<table class="table" style="font-size:var(--type-14);line-height:1.3"><caption style="text-align:left;font-size:var(--type-14);padding-bottom:8px">기준 눈금: ${use(axis).map(refSpan).join(' · ')}</caption><thead><tr><th></th>${use(labels).map(t=>`<th>${refSpan(t)}</th>`).join('')}</tr></thead><tbody><tr><th>${refSpan(get('t5'))}</th>${use(actual).map(t=>`<td class="num">${refSpan(t)}</td>`).join('')}</tr><tr><th>${refSpan(get('t6'))}</th>${use(target).map(t=>`<td class="num">${refSpan(t)}</td>`).join('')}</tr></tbody></table>`;
  return {html:chartHtml+stats+root('table','tablebox',table,place(1,8,5,2),'--gap-sm:4px;'),refs:Array.from({length:34},(_,i)=>'t'+(i+5)),lead:['t29']};
 }
 if(s.deck==='060'&&s.id==='08'){
  const values=['t15','t17','t19','t21','t23','t25'],labels=['t16','t18','t20','t22','t24','t26'],axis=['t9','t10','t11','t12','t13','t14'];
  const chart={kind:'chart-line',values:values.map((ref,i)=>({source:get(ref),value:parseFloat(get(ref).text.replaceAll(',','')),label:get(labels[i])}))};
  const stats=`<div class="stack" style="${place(1,4,1,6)}">${stat('t4','t5')}${stat('t6','t7')}</div>`;
  const legend=root('legend','legend',`<span class="key tone-1" style="font-size:var(--type-14)">세로축 눈금</span>${use(axis).map(t=>`<span class="key tone-2" style="font-size:var(--type-14)">${refSpan(t)}</span>`).join('')}`,place(5,8,6,1),'--gap:12px;');
  return {html:stats+chartMarkup(chart,place(5,8,1,5))+legend,refs:['t4','t5','t6','t7',...axis,...values,...labels],lead:[]};
 }
 return null;
}
function authoredHierarchy(s){
 const get=ref=>s.texts.find(t=>t.ref===ref),refs=[];
 const use=(cls,ids,size)=>{refs.push(...ids);return authoredText(cls,ids.map(get).filter(Boolean),size)};
 if(s.deck==='056'&&s.id==='12'){
  const head=`<div class="root" style="left:20%;width:60%;flex-direction:column;gap:4px;--ink-2:var(--accent-ink)">${use('name',['t5'],22)}${use('note',['t6'],16)}</div>`;
  const branches=[['t7','t8','t9'],['t10','t11','t12'],['t13','t14','t15'],['t16','t17','t18']].map(([name,...leaves])=>`<div class="branch"><div class="node">${use('name',[name],22)}</div>${leaves.map(ref=>`<div class="leaf">${use('note',[ref],16)}</div>`).join('')}</div>`).join('');
  return {html:root('hierarchy','org',head+branches,place(),'--gap:20px;--gap-sm:12px;--pad:16px;--body-line:1.35;'),refs};
 }
 if(s.deck==='058'&&s.id==='19'){
  const head=`<div class="root">${use('name',['t5'],22)}</div>`;
  const teams=[{name:'t6',people:[['t8','t9','t10'],['t11','t12','t13'],['t14','t15','t16']]},{name:'t7',people:[['t17','t18','t19'],['t20','t21','t22'],['t23','t24','t25']]}];
  const branches=teams.map(team=>`<div class="branch"><div class="node">${use('name',[team.name],22)}</div>${team.people.map(([name,role,note])=>`<div class="leaf" style="display:grid;grid-template-columns:1fr 1.2fr 2.8fr;align-items:center;gap:10px;text-align:left">${use('name',[name],22)}${use('note',[role],16)}${use('note',[note],16)}</div>`).join('')}</div>`).join('');
  return {html:root('hierarchy','org',head+branches,place(),'--gap:24px;--gap-sm:10px;--pad:16px;--body-line:1.35;'),refs};
 }
 return null;
}
function inferredTable(ts){
 const rows=[];for(const t of [...ts].sort((a,b)=>a.y-b.y||a.x-b.x)){let row=rows.find(r=>Math.abs(r.y-t.y)<16);if(!row){row={y:t.y,items:[]};rows.push(row);}row.items.push(t);}
 const maxCols=Math.max(...rows.map(r=>r.items.length));if(maxCols<3||rows.length>13)return null;
 return {rows:rows.map(r=>r.items.sort((a,b)=>a.x-b.x).map((t,i)=>({...t,colSpan:r.items.length===1?maxCols:1}))),inferred:true};
}
const compositions=[];
function compose(s,index){
 const candidate=findTitle(s);const title=candidate&&(norm(candidate.text)===norm(s.declaredTitle)||/목차|contents/i.test(s.declaredTitle)&&/목차|contents/i.test(candidate.text))?candidate:null;const represented=new Set();if(title)represented.add(title.ref);
 const possibleCover=s.texts.filter(t=>t.ui!=='svg-text'&&t.style.size>=58&&!numeric(t)&&t.text.length>1);
 const cover=possibleCover.length>0&&s.texts.length<17&&!s.tables.length&&!/목차|contents/i.test(s.declaredTitle);
 const meta=s.texts.filter(t=>t!==title&&t.style.size<=28&&((t.y<95&&!(numeric(t)&&t.style.size>=18))||(t.y<190&&t.w<350&&t.style.size<25&&/^[A-Za-z][A-Za-z &.]+$/.test(t.text))||t.x>1200||(t.y>=650&&t.text.length<12)));
 const smallMarkers=s.texts.filter(t=>/^[•·▪]$/.test(t.text));smallMarkers.forEach(t=>represented.add(t.ref));
 const footer=meta.filter(t=>t.y>=650),kicker=meta.filter(t=>t.y<650);
 meta.forEach(t=>represented.add(t.ref));
 let body=s.texts.filter(t=>!represented.has(t.ref)),html='',elements=[];const lead=body.filter(t=>t.ui!=='svg-text'&&t.y<210&&t.w>300&&t.text.length>12&&!s.boxes.some(b=>b.y>120&&b.h>70&&b.w<1200&&t.x>=b.x-2&&t.x+t.w<=b.x+b.w+8&&t.y>=b.y&&t.y+t.h<=b.y+b.h+8));lead.forEach(t=>represented.add(t.ref));body=body.filter(t=>!lead.includes(t));
 const style=`--accent:${accents[s.deck]||'#384ba4'};--tone-1:${accents[s.deck]||'#384ba4'};--page:${surfaces[s.deck]||'#f5f5f4'};--margin-x:52px;--margin-y:36px;--gap:18px;--gap-sm:10px;--body-line:1.45;`;
 if(cover){
  const titles=possibleCover.length?possibleCover:[candidate].filter(Boolean);if(title&&!titles.includes(title))represented.delete(title.ref);titles.forEach(t=>represented.add(t.ref));
  const rest=[...lead,...body.filter(t=>!represented.has(t.ref))];rest.forEach(t=>represented.add(t.ref));
  html=`<section class="slide cover overrides" id="${s.deck}-${s.id}" data-origin="${s.deck}/${s.id}" style="${style}"><div class="page">${footer.length?`<div class="meta">${footer.map(refSpan).join(' · ')}</div>`:''}<div class="lockup at-left" style="max-width:72%">${p('kicker',kicker)}<h1 class="title" style="font-size:var(--type-64)">${titles.map(refSpan).join('<br>')}</h1>${p('lead',rest)}</div>${s.seats.length?'<div class="seat back" data-ph="1" style="width:28%;height:74%;justify-self:end;align-self:center"></div>':'<div class="deco"></div>'}</div></section>`;
  elements=['foundation.cover'];
 }else{
  let slots=[];const explicitChart=authoredSemantic(s)||authoredCharts(s);if(explicitChart){slots.push({type:'authored-chart',html:explicitChart.html});explicitChart.refs.forEach(ref=>represented.add(ref));for(let i=lead.length-1;i>=0;i--)if(explicitChart.refs.includes(lead[i].ref))lead.splice(i,1);body=body.filter(t=>!explicitChart.refs.includes(t.ref));for(const item of body){if(!lead.includes(item))lead.push(item);represented.add(item.ref);}body=[];for(const ref of explicitChart.lead||[]){const item=s.texts.find(t=>t.ref===ref);if(item&&!lead.includes(item))lead.push(item);}}const explicitHierarchy=authoredHierarchy(s);if(explicitHierarchy){slots.push({type:'hierarchy',html:explicitHierarchy.html});explicitHierarchy.refs.forEach(ref=>represented.add(ref));body=body.filter(t=>!explicitHierarchy.refs.includes(t.ref));}
  const tables=[...s.tables];if(!tables.length&&/테이블|요약 테이블|実行|実績|실행 과제 및 관리 지표|KPI 관리 체계|지표별 KPI|예산 및 리소스/.test(s.declaredTitle)){const inferred=inferredTable(body.filter(t=>t.y>=180));if(inferred){tables.push(inferred);const refs=new Set(inferred.rows.flat().map(t=>t.ref));body=body.filter(t=>!refs.has(t.ref));}}
  if(tables.length){tables.forEach(t=>{slots.push({type:'table',data:t});t.rows.flat().forEach(c=>represented.add(c.ref))});}
  const chart=(tables.length||explicitChart||explicitHierarchy)?null:chartFromSource(s,body);
  if(chart){s.derivedChart=chart.derived?chart.values.map(v=>({ref:v.source.ref,value:v.value,provenance:v.source.provenance})):undefined;
   const consumed=new Set(chart.values.flatMap(v=>[v.source.ref,v.label?.ref]).filter(Boolean));
   body=body.filter(t=>!consumed.has(t.ref));consumed.forEach(ref=>represented.add(ref));slots.push({type:chart.kind,data:chart});
  }
  if(chart){const subheads=body.filter(t=>t.y<250&&t.style.size>=20&&t.w>500);lead.push(...subheads);body=body.filter(t=>!subheads.includes(t));}let groups=chart&&body.length?[{rect:{x:0,y:500,w:1280,h:180},items:body,forceCard:true}]:groupTexts(s,body);const canAgenda=/목차|contents|CONTENTS/.test(s.declaredTitle)&&groups.length<=6&&!slots.length;
  const canTimeline=/연혁|로드맵|일정|타임라인/.test(s.declaredTitle)&&groups.length>=2&&groups.length<=6&&!slots.length;
  const canSteps=/프로세스|추진 단계|실행 단계|진행 과정|추진 체계/.test(s.declaredTitle)&&groups.length>=2&&groups.length<=6&&!slots.length;
  const diagram=slots.length?null:/SWOT|매트릭스|포지셔닝/.test(s.declaredTitle)?'matrix':/사이클|선순환|순환/.test(s.declaredTitle)?'cycle':/연관 키워드|허브/.test(s.declaredTitle)?'hub':/조직 체계|인력 구성도/.test(s.declaredTitle)?'hierarchy':s.seats.length&&/팀 소개/.test(s.declaredTitle)?'person':null;if(diagram==='matrix'){const anchors=body.filter(t=>/^[SWOT]$/.test(t.text));if(anchors.length===4){const side=body.filter(t=>t.x<Math.min(...anchors.map(a=>a.x))-50);lead.push(...side);body=body.filter(t=>!side.includes(t));groups=anchors.map(a=>({rect:{x:a.x,y:a.y,w:350,h:240},items:[]}));for(const t of body){const g=groups.map(g=>({g,d:Math.abs(t.x-g.rect.x)+Math.abs(t.y-g.rect.y)*1.4})).sort((a,b)=>a.d-b.d)[0].g;g.items.push(t);}}else{groups=Array.from({length:4},(_,i)=>({rect:{x:i%2*640,y:Math.floor(i/2)*280+180,w:640,h:280},items:[]}));for(const t of body){const col=t.x+t.w/2<640?0:1,row=t.y<410?0:1;groups[row*2+col].items.push(t);}}}if(diagram&&!(diagram==='hierarchy'&&(body.reduce((n,t)=>n+t.text.length,0)>200||groups.length>4))&&groups.length>=(['cycle','hub'].includes(diagram)?3:2)&&groups.length<=6){slots=[{type:diagram,groups}];body.forEach(t=>represented.add(t.ref));}
  else if(canAgenda){groups=spatialGroups(s,body,'agenda');slots=groups.map(g=>({type:'agenda-group',data:g}));body.forEach(t=>represented.add(t.ref));}
  else if(canTimeline||canSteps){groups=spatialGroups(s,body,'timeline');slots=[{type:canSteps?'steps':'timeline',groups}];body.forEach(t=>represented.add(t.ref));}
  else{for(const g of groups){slots.push({type:'card',data:g});g.items.forEach(t=>represented.add(t.ref));}if(!explicitChart&&!explicitHierarchy&&s.seats.length&&body.length<14&&groups.length<=3){for(const seat of s.seats.filter(p=>p.w*p.h>30000).slice(0,3))slots.unshift({type:'image-frame',data:seat});}}
  // Every body source text is kept even if grouping is empty, including small chart labels.
  const n=Math.max(1,slots.length);let cols=n===1?1:n===2?2:n===3?3:n===4?2:3;
  if(slots.some(sl=>sl.type==='table'))cols=1;
  if(n<=3&&slots.every(sl=>sl.type==='card')){const rects=slots.map(sl=>sl.data.rect);if(Math.max(...rects.map(r=>r.y))-Math.min(...rects.map(r=>r.y))>160&&Math.max(...rects.map(r=>r.x))-Math.min(...rects.map(r=>r.x))<120)cols=1;}const rows=Math.ceil(n/cols);const nativeTable=tables.length===1?tables[0]:null;
  const markup=slots.map((slot,i)=>{
   let w=12/cols,x=1+(i%cols)*w,h=6/rows,y=1+Math.floor(i/cols)*h;if(nativeTable){if(slot.type==='table'){x=1;w=12;y=1;h=5;}else{x=1;w=12;y=6;h=1;}}
   if(chart&&n>1){if(slot.type==='chart-line'||slot.type==='chart-bar'||slot.type==='chart-donut'){x=1;w=12;y=1;h=4;}else{x=1;w=12;y=5;h=2;}}const layout=place(x,w,y,h);elements.push(slot.type);
   if(slot.html)return slot.html;if(slot.type==='image-frame')return root('image-frame','frame',`<div class="seat" data-ph="${i+1}" data-source-seat="${slot.data.ref}"></div>`,layout);
   if(slot.type==='table')return tableMarkup(slot.data,layout);if(nativeTable){const items=slots.filter(sl=>sl.type==='card').flatMap(sl=>sl.data.items);if(slots.findIndex(sl=>sl.type==='card')!==i)return '';return root('callout','callout',`<p style="font-size:var(--type-14);line-height:1.3">${items.map(refSpan).join(' · ')}</p>`,layout,'--pad:10px;--body-line:1.35;');}
   if(slot.type==='chart-line'||slot.type==='chart-bar'||slot.type==='chart-donut')return chartMarkup(slot.data,layout);
   if(['matrix','cycle','hub','hierarchy','person'].includes(slot.type))return diagramMarkup(slot.type,slot.groups,layout,s.declaredTitle);if(slot.type==='steps'||slot.type==='timeline')return flow(slot.groups,layout,slot.type);
   // Pure bullet sequences are represented by the collection's list element.
   const g=slot.data;if(slot.type==='agenda-group')return authoredAgenda(g,i,layout);if(g.items.length>=2&&g.items.length<=3&&g.items.every(t=>t.style.size<=20&&t.text.length<50)){elements[elements.length-1]='list';return list(g,layout);}
   if(g.items.some(t=>numeric(t)&&t.style.size>=28))elements[elements.length-1]='metric';
   return card(g,layout,i);
  }).join('');
  const tableRefs=s.tables.flatMap(t=>t.rows.flat().map(c=>c.ref));
  html=`<section class="slide overrides" id="${s.deck}-${s.id}" data-origin="${s.deck}/${s.id}" style="${style}"><div class="page"><header class="head">${kicker.length?`<p class="kicker">${kicker.map(refSpan).join(' · ')}</p>`:''}<h1 class="title" style="font-size:var(--type-36)">${title?refSpan(title):escape(s.declaredTitle)}</h1>${lead.length?`<p class="lead" style="font-size:var(--type-18);line-height:1.35">${lead.map(refSpan).join(' · ')}</p>`:''}</header><div class="body">${markup}</div>${footer.length?`<div class="meta" style="font-size:var(--type-12);line-height:1.2">${footer.map(refSpan).join(' · ')}</div>`:''}</div></section>`;
 }
 const expected=[...s.texts.map(t=>t.ref),...s.tables.flatMap(t=>t.rows.flat().map(c=>c.ref))];
 const actual=new Set([...html.matchAll(/data-source-ref="([^"]+)"/g)].map(m=>m[1]));
 const omitted=expected.filter(r=>!actual.has(r)&&!smallMarkers.some(t=>t.ref===r));
 compositions.push({deck:s.deck,id:s.id,title:s.declaredTitle,origin:s.source,layout:cover?'cover':'foundation-12x6',elements:[...new Set([...html.matchAll(/data-el="report-forge-([^"]+)"/g)].map(m=>m[1]))],sourceTextCount:expected.length,representedTextCount:actual.size,omittedSourceRefs:omitted,seatCount:s.seats.length,svgCount:s.svgs.length,derivedChart:s.derivedChart,semanticInterpretation:s.semanticInterpretation});
 return html;
}
const slidesHtml=data.slides.map(compose).join('\n');
let css='';for(const file of ['kit/css/tokens.css','foundation/foundation.css',...(await fs.readdir('collection/report-forge/elements')).sort().map(d=>`elements/${d}/element.css`)])css+=`\n/* Collection source: ${file} */\n`+await fs.readFile(path.join('collection/report-forge',file),'utf8');
const steps=JSON.parse(await fs.readFile('contract/type-steps.json','utf8'));
const types=`.slide{${steps.map(n=>`--type-${n}:${n}px`).join(';')}}`;
const font=await fs.readFile('public/fonts/PretendardVariable.woff2');
const html=`<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Report Forge — Rhetis library assembly, 112 slides</title><style>@font-face{font-family:Pretendard;src:url(data:font/woff2;base64,${font.toString('base64')}) format('woff2');font-weight:100 900;font-display:swap}*{box-sizing:border-box}body{margin:0;background:#dfe2e8}.navigation{font:14px Pretendard,sans-serif;padding:18px 32px;background:white;display:flex;gap:18px}.gallery{display:flex;flex-direction:column;align-items:center;gap:24px;padding:24px}.slide[hidden]{display:none!important}${types}${css}\n/* Only page-authored placement and numeric type/layout adjustments follow. No element CSS is rewritten. */\n@media print{body{background:white}.navigation{display:none}.gallery{padding:0;gap:0}.slide{break-after:page;break-inside:avoid}@page{size:1280px 720px;margin:0}}</style></head><body><nav class="navigation"><b>Rhetis · REPORT FORGE</b><span>원문과 수치를 보존한 라이브러리 재조립본 · 112 slides</span><a href="assembled.html">전체</a>${Object.keys(accents).map(d=>`<a href="?deck=${d}">${d}</a>`).join('')}</nav><main class="gallery">${slidesHtml}</main><script>window.__ASSEMBLY__=${JSON.stringify(compositions)};function filter(){const p=new URLSearchParams(location.search),hash=location.hash.slice(1);const deck=p.get('deck'),slide=p.get('slide');const only=!!slide||!!hash;document.querySelector('.navigation').hidden=only;document.querySelector('.gallery').style.cssText=only?'padding:0;gap:0;align-items:flex-start':'';document.querySelectorAll('section.slide').forEach(el=>{let [d,s]=el.dataset.origin.split('/');el.hidden=hash?el.id!==hash:!!((deck&&d!==deck)||(slide&&s!==slide));})}filter();addEventListener('hashchange',filter);window.renderAssembly=(deck,slide)=>{history.replaceState({},'',location.pathname+'?deck='+deck+'&slide='+slide);filter()};</script></body></html>`;
await fs.mkdir('outputs',{recursive:true});await fs.writeFile('outputs/assembled.html',html);
await fs.writeFile('review/assembly-manifest.json',JSON.stringify({schema:'rhetis.slide-assembly-manifest/1',count:compositions.length,kit,sourceData:'src/assembly-data.json',renderer:'outputs/assembled.html',independentOfReact:true,compositions},null,2));
console.log(`Assembled ${compositions.length} slides; ${compositions.filter(c=>c.omittedSourceRefs.length).length} with unrepresented source text references.`);
if(args.has('--audit')){
 const browser=await launch(),page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1}),audit=[];
 await page.route('**/@vite/client',route=>route.fulfill({status:200,contentType:'application/javascript',body:''}));await fs.mkdir('renders/assembled',{recursive:true});await page.goto(`${base}/outputs/assembled.html?deck=${compositions[0].deck}&slide=${compositions[0].id}`);await page.evaluate(()=>document.fonts.ready);
 for(const s of compositions){
  await page.evaluate(({deck,id})=>window.renderAssembly(deck,id),s);await page.evaluate(()=>new Promise(requestAnimationFrame));
  const a=await page.evaluate(()=>{
   const slide=[...document.querySelectorAll('section.slide')].find(s=>!s.hidden),r=slide.getBoundingClientRect(),issues=[];
   for(const el of slide.querySelectorAll('[data-source-ref],[data-el]')){const b=el.getBoundingClientRect(),st=getComputedStyle(el);if(st.display==='none'||!b.width||!b.height){if(el.hasAttribute('data-source-ref'))issues.push({type:'hidden-text',ref:el.dataset.sourceRef,text:el.textContent.slice(0,70)});continue;}if(b.left<r.left-.6||b.top<r.top-.6||b.right>r.right+.6||b.bottom>r.bottom+.6)issues.push({type:'outside-slide',ref:el.dataset.sourceRef,text:el.textContent.slice(0,70),rect:[b.x,b.y,b.width,b.height]});if(el.hasAttribute('data-el')&&el.scrollHeight>el.clientHeight+3)issues.push({type:'element-overflow',el:el.dataset.el,overflow:el.scrollHeight-el.clientHeight});}
   return {size:[r.width,r.height],fonts:document.fonts.check('400 20px Pretendard'),issues,sourceRefs:[...slide.querySelectorAll('[data-source-ref]')].map(e=>e.dataset.sourceRef)};
  });
  await fs.mkdir(`renders/assembled/${s.deck}`,{recursive:true});await page.locator('section.slide:not([hidden])').screenshot({path:`renders/assembled/${s.deck}/${s.id}.png`});audit.push({deck:s.deck,id:s.id,...a});
 }
 await fs.writeFile('review/audit-assembly.json',JSON.stringify(audit,null,2));await browser.close();console.log(`Audited ${audit.length} slides; ${audit.filter(a=>a.issues.length).length} have findings.`);
}

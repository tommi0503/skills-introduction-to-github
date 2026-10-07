// Inspect final browser geometry and the actual faces used for Korean and Latin glyphs.
export async function auditPage(page){return page.evaluate(async()=>{
 const article=document.querySelector('[data-page]'),paper=article?.querySelector('[data-paper]');
 if(!article||!paper)throw Error('Missing page canvas');
 const a=article.getBoundingClientRect(),p=paper.getBoundingClientRect(),ps=getComputedStyle(paper),scale=p.width/parseFloat(ps.width),issues=[],fontChecks=[];
 const ctx=document.createElement('canvas').getContext('2d');
 const add=(el,issue,details={},allowClip=false)=>issues.push({issue,elementId:el.dataset.elementId,kind:el.dataset.elementKind,text:(el.textContent??'').trim().slice(0,150),expectedClip:allowClip&&!!el.dataset.clipReason,clipReason:allowClip?el.dataset.clipReason:undefined,...details});
 if(a.width!==1280||a.height!==720)issues.push({issue:'Incorrect page canvas',size:[a.width,a.height]});
 if(Math.abs(scale-p.height/parseFloat(ps.height))>0.0001)issues.push({issue:'Nonuniform source scale'});
 if(article.querySelector('img,svg image'))issues.push({issue:'Raster reference embedded in UI'});
 for(const el of paper.querySelectorAll('.element')){
  const s=getComputedStyle(el),b=el.getBoundingClientRect();
  if(s.backgroundImage!=='none'&&/url\(/.test(s.backgroundImage))add(el,'Raster background embedded in UI');
  if(el.dataset.elementKind==='image'&&s.backgroundColor!=='rgb(229, 229, 229)')add(el,'Placeholder must be light gray');
  if(![b.x,b.y,b.width,b.height].every(Number.isFinite))add(el,'Invalid element geometry');
  if(el.dataset.elementKind!=='text')continue;
  const text=(el.textContent??'').trim();if(!text)continue;
  const weight=Number(s.fontWeight),style=s.fontStyle,family=s.fontFamily;
  const glyphs=[text.match(/[가-힣]/)?.[0],text.match(/[A-Za-z0-9]/)?.[0],text.match(/[\u3400-\u9fff]/)?.[0]].filter(Boolean);if(!glyphs.length)glyphs.push(text[0]);
  for(const glyph of new Set(glyphs)){
   const faces=await document.fonts.load(`${style} ${weight} ${s.fontSize} ${family}`,glyph);
   const loaded=faces.filter(f=>f.status==='loaded');
   const covers=f=>{const w=f.weight.split(' ').map(Number);return w.length===2?weight>=w[0]&&weight<=w[1]:weight===w[0]};
   const record={family,weight,style,glyph,loadedFaces:loaded.map(f=>({family:f.family,weight:f.weight,style:f.style}))};fontChecks.push(record);
   if(!loaded.length||!loaded.some(covers)||!loaded.some(f=>f.style===style))add(el,'Requested font face/weight/style not loaded',record);
  }
  const range=document.createRange();range.selectNodeContents(el);const r=range.getBoundingClientRect();
  ctx.font=`${style} ${weight} ${s.fontSize} ${family}`;ctx.letterSpacing=s.letterSpacing==='normal'?'0px':s.letterSpacing;
  const m=ctx.measureText(text.split('\n').at(-1));
  const paintedBottom=r.bottom-(m.fontBoundingBoxDescent-m.actualBoundingBoxDescent)*scale;
  if(r.width>b.width+2*scale)add(el,'text wider than element',{excess:(r.width-b.width)/scale});
  if(paintedBottom>b.bottom+2*scale)add(el,'text taller than element',{excess:(paintedBottom-b.bottom)/scale});
  if(r.left<p.left-2*scale||r.right>p.right+2*scale||r.top<p.top-2*scale||paintedBottom>p.bottom+2*scale)add(el,'text outside paper',{range:[r.left,r.top,r.width,r.height]},true);
  if(el.dataset.chip==='true'){
   const label=el.querySelector('[data-chip-label]'),l=label.getBoundingClientRect(),line=text.split('\n').sort((a,b)=>b.length-a.length)[0],metrics=ctx.measureText(line);
   const x=l.x+l.width/2+(metrics.actualBoundingBoxRight-metrics.actualBoundingBoxLeft-metrics.width)/2*scale-(b.x+b.width/2);
   const y=l.y+l.height/2+(metrics.fontBoundingBoxAscent-metrics.fontBoundingBoxDescent+metrics.actualBoundingBoxDescent-metrics.actualBoundingBoxAscent)/2*scale-(b.y+b.height/2);
   if(Math.abs(x)>1.2||Math.abs(y)>1.2)add(el,'chip ink not centered',{offset:[x,y]});
   if(l.width>b.width+scale||l.height>b.height+scale)add(el,'chip label exceeds bounds');
  }
 }
 for(const path of paper.querySelectorAll('svg path'))if(/NaN|Infinity|undefined/.test(path.getAttribute('d')??''))issues.push({issue:'Invalid vector coordinates'});
 return{size:[a.width,a.height],uniformScale:true,issues,fontChecks,chipCount:paper.querySelectorAll('[data-chip]').length,placeholderCount:paper.querySelectorAll('.element-image').length,replacementCount:paper.querySelectorAll('[data-replacement]').length};
});}

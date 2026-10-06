export async function auditSlide(page) {
 return page.evaluate(async () => {
  const article=document.querySelector('article[data-slide]');
  if(!article)throw Error('Slide article missing');
  await document.fonts.ready;
  const issues=[],fontChecks=[];
  const bounds=article.getBoundingClientRect();
  const issue=(element,kind,details={})=>{
   const owner=element.closest?.('.element')??element;
   const allowed=owner.dataset.allowClip==='true'&&['text outside slide','text exceeds element bounds','text clipped by ancestor horizontally','text clipped by ancestor vertically'].includes(kind);
   issues.push({issue:kind,index:Number(owner.dataset.elementIndex??-1),kind:owner.dataset.elementKind,
    text:(element.textContent??'').trim().slice(0,180),expectedClip:allowed,clipReason:owner.dataset.clipReason,...details});
  };
  if(bounds.width!==1280||bounds.height!==720)issue(article,'canvas dimensions',{size:[bounds.width,bounds.height]});
  if(getComputedStyle(article).transform!=='none')issue(article,'canvas transformed');
  if(article.querySelectorAll('img,svg image').length)issue(article,'embedded image inside UI slide');
  const seenFonts=new Set();
  const labels=[...article.querySelectorAll('.element-text,.element-chip,.data-table td,.bar-label,.bar-value,.donut>div')];
  for(const element of labels){
   const style=getComputedStyle(element);
   const text=(element.textContent??'').trim();
   if(!text)continue;
   const key=[style.fontFamily,style.fontWeight,style.fontStyle].join('|');
   if(!seenFonts.has(key)){
    seenFonts.add(key);
    const fonts=await document.fonts.load(style.fontStyle+' '+style.fontWeight+' '+style.fontSize+' '+style.fontFamily,text.slice(0,120));
    const first=style.fontFamily.split(',')[0].trim().replace(/^["']|["']$/g,'');
    const generic=['serif','sans-serif','monospace','system-ui','cursive','fantasy'];
    const matching=fonts.filter(face=>face.family.replace(/^["']|["']$/g,'').toLowerCase()===first.toLowerCase()&&face.status==='loaded'&&face.style===style.fontStyle);
    const weight=Number(style.fontWeight);
    const supported=matching.some(face=>{
     const range=face.weight.split(/\s+/).map(Number);
     return range.length===1?range[0]===weight:range[0]<=weight&&weight<=range[1];
    });
    const record={family:first,weight,style:style.fontStyle,loaded:matching.length>0,
     actualWeights:matching.map(f=>f.weight),supportedWeight:supported,systemGeneric:generic.includes(first)};
    fontChecks.push(record);
    if(!record.systemGeneric&&!record.loaded)issue(element,'font family not loaded',record);
    else if(!record.systemGeneric&&!record.supportedWeight)issue(element,'requested font weight unavailable',record);
   }
  }
  await document.fonts.ready;
  await new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
  const canvas=document.createElement('canvas'),context=canvas.getContext('2d');
  for(const element of labels){
   if(!(element.textContent??'').trim())continue;
   const owner=element.closest('.element')??element;
   const style=getComputedStyle(element);
   const b=element.getBoundingClientRect();
   const range=document.createRange();range.selectNodeContents(element);
   let r=range.getBoundingClientRect();
   const matrix=new DOMMatrix(getComputedStyle(owner).transform==='none'?undefined:getComputedStyle(owner).transform);
   if(Math.abs(matrix.b)<0.0001&&Math.abs(matrix.c)<0.0001){
    const walker=document.createTreeWalker(element,NodeFilter.SHOW_TEXT);
    let node,minX=Infinity,minY=Infinity,maxX=-Infinity,maxY=-Infinity;
    const measureCache=new Map();
    while((node=walker.nextNode())){
     const textStyle=getComputedStyle(node.parentElement);
     const font=textStyle.fontStyle+' '+textStyle.fontWeight+' '+textStyle.fontSize+' '+textStyle.fontFamily;
     context.font=font;context.letterSpacing=textStyle.letterSpacing==='normal'?'0px':textStyle.letterSpacing;
     let offset=0;
     for(const character of node.textContent){
      const end=offset+character.length;
      if(!/\s/u.test(character)){
       const glyphRange=document.createRange();glyphRange.setStart(node,offset);glyphRange.setEnd(node,end);
       const rectangle=glyphRange.getBoundingClientRect();
       const key=font+'|'+textStyle.letterSpacing+'|'+character;
       let m=measureCache.get(key);if(!m){m=context.measureText(character);measureCache.set(key,m)}
       const sy=Math.abs(matrix.d)||1,sx=Math.abs(matrix.a)||1;
       const baseline=rectangle.y+(rectangle.height-(m.fontBoundingBoxAscent+m.fontBoundingBoxDescent)*sy)/2+m.fontBoundingBoxAscent*sy;
       minX=Math.min(minX,rectangle.x-m.actualBoundingBoxLeft*sx);
       maxX=Math.max(maxX,rectangle.x+m.actualBoundingBoxRight*sx);
       minY=Math.min(minY,baseline-m.actualBoundingBoxAscent*sy);
       maxY=Math.max(maxY,baseline+m.actualBoundingBoxDescent*sy);
      }
      offset=end;
     }
    }
    if(Number.isFinite(minX))r={x:minX,y:minY,left:minX,top:minY,right:maxX,bottom:maxY,width:maxX-minX,height:maxY-minY};
   }
   if(r.left<bounds.left-2||r.top<bounds.top-2||r.right>bounds.right+2||r.bottom>bounds.bottom+2)
    issue(element,'text outside slide',{range:[r.x,r.y,r.width,r.height]});
   if(r.width>b.width+3||r.height>b.height+3)
    issue(element,'text exceeds element bounds',{range:[r.width,r.height],box:[b.width,b.height]});
   let ancestor=element.parentElement;
   while(ancestor&&ancestor!==article){
    const s=getComputedStyle(ancestor),a=ancestor.getBoundingClientRect();
    if(['hidden','clip'].includes(s.overflowX)&&((r.left<a.left-2)||(r.right>a.right+2)))
     issue(element,'text clipped by ancestor horizontally');
    if(['hidden','clip'].includes(s.overflowY)&&((r.top<a.top-2)||(r.bottom>a.bottom+2)))
     issue(element,'text clipped by ancestor vertically');
    ancestor=ancestor.parentElement;
   }
   if(element.classList.contains('element-chip')){
    const label=element.querySelector('[data-chip-label]'),l=label.getBoundingClientRect();
    if(style.justifyContent!=='center'||style.alignItems!=='center')issue(element,'chip label not centered');
    context.font=style.fontStyle+' '+style.fontWeight+' '+style.fontSize+' '+style.fontFamily;
    context.letterSpacing=style.letterSpacing==='normal'?'0px':style.letterSpacing;
    const metrics=context.measureText(element.textContent??'');
    const dx=(metrics.actualBoundingBoxRight-metrics.actualBoundingBoxLeft-metrics.width)/2;
    const dy=(metrics.fontBoundingBoxAscent-metrics.fontBoundingBoxDescent+metrics.actualBoundingBoxDescent-metrics.actualBoundingBoxAscent)/2;
    const x=l.x+l.width/2+dx-(b.x+b.width/2),y=l.y+l.height/2+dy-(b.y+b.height/2);
    if(Math.abs(x)>1.2||Math.abs(y)>1.2)issue(element,'chip ink not centered',{offset:[x,y]});
    if(l.width>b.width+1||l.height>b.height+1)issue(element,'chip label exceeds bounds');
   }
  }
  for(const element of article.querySelectorAll('.element-image')){
   if(getComputedStyle(element).backgroundColor!=='rgb(229, 229, 229)')issue(element,'placeholder is not light gray');
  }
  for(const element of [article,...article.querySelectorAll('*')]){
   const background=getComputedStyle(element).backgroundImage;
   if(/url\(/i.test(background))issue(element,'image background embedded');
   if(/gradient\(/i.test(background)&&!element.classList.contains('donut'))issue(element,'graphic gradient background not replaced');
  }
  return {size:[bounds.width,bounds.height],issues,fontChecks,
   chipCount:article.querySelectorAll('.element-chip').length,
   placeholderCount:article.querySelectorAll('.element-image').length};
 });
}


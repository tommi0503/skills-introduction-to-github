// Browser-backed checks shared by capture and production verification.
export async function auditSlide(page) {
 return await page.evaluate(async()=>{
  const article=document.querySelector('.slide-canvas');if(!article)throw Error('No slide')
  const slide=article.getBoundingClientRect(),ctx=document.createElement('canvas').getContext('2d')
  const findings=[],fontUsage=[]
  // Browser ranges include font ascent/descent space without painted glyphs.
  // Use each text node's loaded font metrics to distinguish that space from clipping.
  const paintedBounds=el=>{
   const walker=document.createTreeWalker(el,NodeFilter.SHOW_TEXT),boxes=[]
   for(let node=walker.nextNode();node;node=walker.nextNode()){
    if(!node.textContent.trim())continue
    const style=getComputedStyle(node.parentElement),range=document.createRange();range.selectNodeContents(node)
    ctx.font=`${style.fontStyle} ${style.fontWeight} ${style.fontSize} ${style.fontFamily}`
    const rects=[...range.getClientRects()].filter(rect=>rect.width&&rect.height)
    const lines=node.textContent.split('\n').filter(line=>line.trim())
    for(const [index,rect] of rects.entries()){
     const m=ctx.measureText(lines.length===rects.length?lines[index]:node.textContent),fontHeight=m.fontBoundingBoxAscent+m.fontBoundingBoxDescent
     const leading=(rect.height-fontHeight)/2
     boxes.push({left:rect.left,right:rect.right,top:rect.top+leading+m.fontBoundingBoxAscent-m.actualBoundingBoxAscent,bottom:rect.bottom-leading-m.fontBoundingBoxDescent+m.actualBoundingBoxDescent})
    }
   }
   return boxes.length?{left:Math.min(...boxes.map(b=>b.left)),right:Math.max(...boxes.map(b=>b.right)),top:Math.min(...boxes.map(b=>b.top)),bottom:Math.max(...boxes.map(b=>b.bottom))}:null
  }
  const record=(el,issue,details={})=>{const b=el.getBoundingClientRect();findings.push({text:el.textContent.slice(0,160),issue,elementBounds:[b.x-slide.x,b.y-slide.y,b.width,b.height],expectedClip:el.dataset.allowClip==='true',clipReason:el.dataset.clipReason,...details})}
  for(const el of article.querySelectorAll('.element-text,.element-text>span,.element-chip,.data-table td,.element-graphic text,.bar-label,.bar-value,.donut>div')){
   const b=el.getBoundingClientRect(),s=getComputedStyle(el),range=document.createRange();range.selectNodeContents(el);const r=range.getBoundingClientRect()
   const family=s.fontFamily.split(',')[0].trim().replace(/^["']|["']$/g,'')
   const glyphs=el.textContent.trim();if(!glyphs)continue
   const loaded=await document.fonts.load(`${s.fontStyle} ${s.fontWeight} ${s.fontSize} "${family}"`,glyphs)
   fontUsage.push({family,weight:s.fontWeight,style:s.fontStyle,loadedFaces:loaded.filter(f=>f.status==='loaded').length,actualFaces:[...new Set(loaded.filter(f=>f.status==='loaded').map(f=>f.weight+' '+f.style))],text:glyphs.slice(0,12)})
   if(!loaded.length&&!['Arial','Times New Roman','sans-serif','serif'].includes(family))record(el,'font family not loaded',{family,weight:s.fontWeight})
   const wanted=Number(s.fontWeight)||400
   const weightAvailable=loaded.some(f=>{const weights=f.weight==='normal'?[400]:f.weight==='bold'?[700]:f.weight.split(/\s+/).map(Number);return weights.length===2?wanted>=weights[0]&&wanted<=weights[1]:weights.includes(wanted)})
   if(loaded.length&&!weightAvailable)record(el,'font weight not loaded',{family,requestedWeight:s.fontWeight,actualWeights:loaded.map(f=>f.weight)})
   if(loaded.length&&s.fontStyle!=='normal'&&!loaded.some(f=>f.style===s.fontStyle))record(el,'font style not loaded',{family,requestedStyle:s.fontStyle,actualStyles:loaded.map(f=>f.style)})
   const ink=el.namespaceURI==='http://www.w3.org/2000/svg'?b:paintedBounds(el)||r
   if(ink.right>slide.right+1||ink.bottom>slide.bottom+1||ink.left<slide.left-1||ink.top<slide.top-1)record(el,'text outside slide',{bounds:{x:ink.left-slide.left,y:ink.top-slide.top,w:ink.right-ink.left,h:ink.bottom-ink.top},rangeBounds:{x:r.x-slide.x,y:r.y-slide.y,w:r.width,h:r.height}})
   if(el.classList.contains('element-text')){
    if(r.width>b.width+3)record(el,'text wider than box',{excess:r.width-b.width})
    if(ink.bottom>b.bottom+3||ink.top<b.top-3)record(el,'text taller than box',{excess:Math.max(ink.bottom-b.bottom,b.top-ink.top)})
   }
   for(let parent=el.parentElement;parent&&parent!==article;parent=parent.parentElement){
    const ps=getComputedStyle(parent),p=parent.getBoundingClientRect()
    if((ps.overflowX==='hidden'||ps.overflowX==='clip')&&(r.left<p.left-1||r.right>p.right+1))record(el,'text clipped by parent horizontally')
    if((ps.overflowY==='hidden'||ps.overflowY==='clip')&&(ink.top<p.top-1||ink.bottom>p.bottom+1))record(el,'text clipped by parent vertically')
   }
   if((el.classList.contains('element-chip')||el.matches('.donut>div'))&&s.justifyContent==='center'){
    const l=el.querySelector('[data-chip-label]').getBoundingClientRect()
    ctx.font=`${s.fontStyle} ${s.fontWeight} ${s.fontSize} ${s.fontFamily}`;ctx.letterSpacing=s.letterSpacing;ctx.wordSpacing=s.wordSpacing
    const m=ctx.measureText(glyphs)
    const dx=(m.actualBoundingBoxRight-m.actualBoundingBoxLeft-m.width)/2
    const dy=(m.fontBoundingBoxAscent-m.fontBoundingBoxDescent+m.actualBoundingBoxDescent-m.actualBoundingBoxAscent)/2
    const matrix=new DOMMatrix(s.transform==='none'?undefined:s.transform)
    const x=l.x+l.width/2+matrix.a*dx+matrix.c*dy-(b.x+b.width/2),y=l.y+l.height/2+matrix.b*dx+matrix.d*dy-(b.y+b.height/2)
    if(Math.abs(x)>1.2||Math.abs(y)>1.2)record(el,'chip ink not centered',{offset:[x,y]})
    if(l.width>b.width+1||l.height>b.height+1)record(el,'chip label exceeds bounds')
   }
  }
  const dedup=[...new Map(fontUsage.map(f=>[`${f.family}/${f.weight}/${f.style}`,f])).values()]
  await document.fonts.ready
  await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))
  const forbidden=article.querySelectorAll('svg image,svg foreignObject,svg script')
  if(forbidden.length)throw Error('Vector scenes must contain actual vectors; embedded raster content is forbidden')
  for(const el of article.querySelectorAll('.element-graphic'))if(!el.querySelector('svg'))throw Error('Missing vector scene')
  const ids=[...article.querySelectorAll('svg [id]')].map(el=>el.id)
  if(new Set(ids).size!==ids.length)throw Error('Duplicate SVG definition IDs')
  for(const path of article.querySelectorAll('.element-graphic path[d]')){
   if(!path.getAttribute('d').trim())continue
   const box=path.getBBox(),view=path.ownerSVGElement.viewBox.baseVal,max=Math.max(view.width,view.height)
   if(max&&(box.width>max*10||box.height>max*10))record(path,'SVG path geometry exceeds scene by more than 10x',{graphic:path.closest('.element-graphic').dataset.graphicName,svgBounds:[box.x,box.y,box.width,box.height],sceneViewBox:[view.x,view.y,view.width,view.height]})
  }
  for(const el of article.querySelectorAll('svg path,svg line,svg polyline')){
   if(el.closest('defs'))continue
   const stroke=getComputedStyle(el).stroke,match=stroke.match(/url\(["']?[^#)]*#([^"')]+)["']?\)/)
   if(!match)continue
   const paint=document.getElementById(match[1])
   if(!paint||!['linearGradient','radialGradient'].includes(paint.tagName)||paint.getAttribute('gradientUnits')==='userSpaceOnUse')continue
   const box=el.getBBox()
   if(!box.width||!box.height)record(el,'gradient stroke has empty object bounding box',{gradientId:match[1],svgBounds:[box.x,box.y,box.width,box.height]})
  }
  return {findings,fontUsage:dedup,canvas:[slide.width,slide.height],placeholderRule:[...article.querySelectorAll('.element-image')].every(el=>getComputedStyle(el).backgroundColor==='rgb(229, 229, 229)'),embeddedImages:article.querySelectorAll('img').length,vectorScenes:article.querySelectorAll('.element-graphic').length,fontStatus:document.fonts.status}
 })
}

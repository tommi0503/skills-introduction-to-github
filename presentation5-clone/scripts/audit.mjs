// Browser-backed checks shared by capture and production verification.
export async function auditSlide(page) {
 return await page.evaluate(async()=>{
  const article=document.querySelector('.slide-canvas');if(!article)throw Error('No slide')
  const slide=article.getBoundingClientRect(),ctx=document.createElement('canvas').getContext('2d')
  const findings=[],fontUsage=[]
  const record=(el,issue,details={})=>{const b=el.getBoundingClientRect();findings.push({text:el.textContent.slice(0,160),issue,elementBounds:[b.x-slide.x,b.y-slide.y,b.width,b.height],expectedClip:el.dataset.allowClip==='true',clipReason:el.dataset.clipReason,...details})}
  for(const el of article.querySelectorAll('.element-text,.element-text>span,.element-chip,.data-table td')){
   const b=el.getBoundingClientRect(),s=getComputedStyle(el),range=document.createRange();range.selectNodeContents(el);const r=range.getBoundingClientRect()
   const family=s.fontFamily.split(',')[0].trim().replace(/^["']|["']$/g,'')
   const glyphs=el.textContent.trim();if(!glyphs)continue
   const loaded=await document.fonts.load(`${s.fontStyle} ${s.fontWeight} ${s.fontSize} "${family}"`,glyphs)
   fontUsage.push({family,weight:s.fontWeight,loadedFaces:loaded.filter(f=>f.status==='loaded').length,actualFaces:[...new Set(loaded.filter(f=>f.status==='loaded').map(f=>f.weight+' '+f.style))],text:glyphs.slice(0,12)})
   if(!loaded.length&&!['Arial','Times New Roman','sans-serif','serif'].includes(family))record(el,'font family not loaded',{family,weight:s.fontWeight})
   const wanted=Number(s.fontWeight)||400
   const weightAvailable=loaded.some(f=>{const weights=f.weight==='normal'?[400]:f.weight==='bold'?[700]:f.weight.split(/\s+/).map(Number);return weights.length===2?wanted>=weights[0]&&wanted<=weights[1]:weights.includes(wanted)})
   if(loaded.length&&!weightAvailable)record(el,'font weight not loaded',{family,requestedWeight:s.fontWeight,actualWeights:loaded.map(f=>f.weight)})
   if(loaded.length&&s.fontStyle!=='normal'&&!loaded.some(f=>f.style===s.fontStyle))record(el,'font style not loaded',{family,requestedStyle:s.fontStyle,actualStyles:loaded.map(f=>f.style)})
   if(r.right>slide.right+1||r.bottom>slide.bottom+1||r.left<slide.left-1||r.top<slide.top-1)record(el,'text outside slide',{bounds:{x:r.x,y:r.y,w:r.width,h:r.height}})
   if(el.classList.contains('element-text')){
    if(r.width>b.width+3)record(el,'text wider than box',{excess:r.width-b.width})
    if(r.height>b.height+3)record(el,'text taller than box',{excess:r.height-b.height})
   }
   for(let parent=el.parentElement;parent&&parent!==article;parent=parent.parentElement){
    const ps=getComputedStyle(parent),p=parent.getBoundingClientRect()
    if((ps.overflowX==='hidden'||ps.overflowX==='clip')&&(r.left<p.left-1||r.right>p.right+1))record(el,'text clipped by parent horizontally')
    if((ps.overflowY==='hidden'||ps.overflowY==='clip')&&(r.top<p.top-1||r.bottom>p.bottom+1))record(el,'text clipped by parent vertically')
   }
   if(el.classList.contains('element-chip')&&s.justifyContent==='center'){
    const l=el.querySelector('[data-chip-label]').getBoundingClientRect()
    ctx.font=`${s.fontStyle} ${s.fontWeight} ${s.fontSize} ${s.fontFamily}`;ctx.letterSpacing=s.letterSpacing
    const m=ctx.measureText(glyphs)
    const dx=(m.actualBoundingBoxRight-m.actualBoundingBoxLeft-m.width)/2
    const dy=(m.fontBoundingBoxAscent-m.fontBoundingBoxDescent+m.actualBoundingBoxDescent-m.actualBoundingBoxAscent)/2
    const matrix=new DOMMatrix(s.transform==='none'?undefined:s.transform)
    const x=l.x+l.width/2+matrix.a*dx+matrix.c*dy-(b.x+b.width/2),y=l.y+l.height/2+matrix.b*dx+matrix.d*dy-(b.y+b.height/2)
    if(Math.abs(x)>1.2||Math.abs(y)>1.2)record(el,'chip ink not centered',{offset:[x,y]})
    if(l.width>b.width+1||l.height>b.height+1)record(el,'chip label exceeds bounds')
   }
  }
  const dedup=[...new Map(fontUsage.map(f=>[`${f.family}/${f.weight}`,f])).values()]
  await document.fonts.ready
  await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))
  return {findings,fontUsage:dedup,canvas:[slide.width,slide.height],placeholderRule:[...article.querySelectorAll('.element-image')].every(el=>getComputedStyle(el).backgroundColor==='rgb(229, 229, 229)'),embeddedImages:article.querySelectorAll('img').length,fontStatus:document.fonts.status}
 })
}

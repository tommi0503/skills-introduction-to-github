import * as Icons from 'lucide-react'
import type { CSSProperties, ComponentType } from 'react'
import {useId,useEffect,useState} from 'react'
import type { Element, Slide, Deck } from './model'

const colorAt = (e:Element,i:number) => e.colors?.[i % e.colors.length] ?? e.fill ?? '#3478f6'
const fontAliases:Record<string,string>={'Roboto':'Roboto Variable','Josefin Sans':'Josefin Sans Variable','Open Sans':'Open Sans Variable','Raleway':'Raleway Variable','Inter':'Inter Variable','Manrope':'Manrope Variable','DM Sans':'DM Sans Variable','Archivo':'Archivo Variable','Playfair Display':'Playfair Display Variable','Pretendard':'Pretendard Variable','Bodoni Moda':'Bodoni Moda Variable','Pixelify Sans':'Pixelify Sans Variable','Roboto Condensed':'Roboto Condensed Variable','Noto Sans KR':'Noto Sans KR','Noto Serif KR':'Noto Serif KR'}
for(const name of ['Figtree','Geist','Instrument Sans','Montserrat','Onest','Outfit','Plus Jakarta Sans','Sora','Space Grotesk','Urbanist'])fontAliases[name]=name+' Variable'
const resolveFont=(font:string)=>font.split(',').map(part=>{const name=part.trim().replace(/^["']|["']$/g,'');return fontAliases[name]?`"${fontAliases[name]}"`:part}).join(',')
function Bars({element:e}:{element:Element}) {
  const values=e.values??[],max=e.max??Math.max(...values,1)
  return <div className={`chart ${e.vertical?'horizontal':'vertical'}`}>
    {values.map((v,i)=><div className="bar-item" key={i}>
      {e.showValues!==false&&<span className="bar-value" style={{color:e.color,fontSize:e.valueSize??24}}>{v}{e.text??'%'}</span>}
      <div className="bar" style={{background:colorAt(e,i),[e.vertical?'width':'height']:`${v/max*78}%`}} />
      <span className="bar-label" style={{color:e.color,fontSize:e.labelSize??16}}>{e.labels?.[i]}</span>
    </div>)}
  </div>
}
function Donut({element:e}:{element:Element}) {
  const values=e.values??[75,25],sum=values.reduce((a,b)=>a+b,0)
  let position=0
  const segments=values.map((v,i)=>{const start=position;position+=v/sum*100;return `${colorAt(e,i)} ${start}% ${position}%`})
  return <div className="donut" style={{background:`conic-gradient(${segments.join(',')})`}}><div style={{background:e.border??'#fff',color:e.color}}>{e.text}</div></div>
}
function VectorPath({element:e}:{element:Element}) {
 const markerId=useId().replace(/:/g,'')
 const points=e.points??[]
 if(points.length<2)return null
 let d=`M ${points[0].x} ${points[0].y}`
 if(e.curved){
  for(let i=1;i<points.length;i++){
   const a=points[i-1],b=points[i],previous=points[i-2]??a,next=points[i+1]??b
   // Shared Catmull–Rom tangents keep adjacent segments smooth instead of
   // forcing a horizontal tangent (and a visible step) at every sample.
   const c1={x:a.x+(b.x-previous.x)/6,y:a.y+(b.y-previous.y)/6}
   const c2={x:b.x-(next.x-a.x)/6,y:b.y-(next.y-a.y)/6}
   d+=` C ${c1.x} ${c1.y}, ${c2.x} ${c2.y}, ${b.x} ${b.y}`
  }
 }else d+=points.slice(1).map(p=>` L ${p.x} ${p.y}`).join('')
 if(e.closed)d+=' Z'
 const stroke=e.color??'#222'
 return <svg width="100%" height="100%" viewBox="0 0 100 100" preserveAspectRatio="none" style={{overflow:'visible'}} aria-hidden="true">
  {e.arrow&&<defs><marker id={markerId} markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke={stroke} strokeWidth="1.5"/></marker></defs>}
  <path d={d} fill={e.fill??'none'} stroke={stroke} strokeWidth={e.strokeWidth??2} vectorEffect="non-scaling-stroke" strokeDasharray={e.dashPattern??(e.dashed?'5 4':undefined)} strokeLinecap={e.lineCap} markerEnd={e.arrow?`url(#${markerId})`:undefined}/>
 </svg>
}
// Center the painted glyphs, including fonts whose baseline metrics are asymmetric.
function ChipLabel({element:e}:{element:Element}) {
 const [shift,setShift]=useState({x:0,y:0})
 useEffect(()=>{let active=true;document.fonts.ready.then(()=>{
  if(!active)return
  const context=document.createElement('canvas').getContext('2d')!
  context.font=`${e.fontStyle??'normal'} ${e.weight??500} ${e.size??32}px ${resolveFont(e.font??'Pretendard')}`
  context.letterSpacing=`${e.letterSpacing??0}px`
  const m=context.measureText(e.text??'')
  const y=(m.actualBoundingBoxAscent-m.actualBoundingBoxDescent-m.fontBoundingBoxAscent+m.fontBoundingBoxDescent)/2
  const x=e.align==='left'||e.align==='right'?0:(m.width-m.actualBoundingBoxRight+m.actualBoundingBoxLeft)/2
  setShift({x,y})
 });return()=>{active=false}},[e.text,e.size,e.weight,e.font,e.fontStyle,e.align,e.letterSpacing])
 return <span data-chip-label data-optical-x={shift.x} data-optical-y={shift.y} style={{transform:`translate(${shift.x}px,${shift.y}px)`}}>{e.text}</span>
}
function ElementView({element:e,sourceAspect}:{element:Element;sourceAspect?:number}) {
  const style:CSSProperties={left:`${e.x}%`,top:`${e.y}%`,width:`${e.w}%`,height:`${e.h}%`,color:e.color??'#171717',fontSize:e.size??32,fontWeight:e.weight??400,fontStyle:e.fontStyle,fontFamily:resolveFont(e.font??'Inter, Pretendard, sans-serif'),textAlign:e.align??'left',lineHeight:e.lineHeight??1.12,letterSpacing:e.letterSpacing??0,opacity:e.opacity??1,borderRadius:e.radius??0,clipPath:e.clipPath,WebkitTextStroke:e.textStroke}
  let content
  // Only reference elements such as stickers rotate; the 1280×720 stage stays flat.
  if(e.kind!=='text'&&e.rotate){style.transform=`rotate(${e.rotate}deg)`;style.transformOrigin='center'}
  if(e.kind==='text') {
    const stretch=(e.scaleX??1)*(sourceAspect?(16/9)/sourceAspect:1)
    style.width=`${e.w/stretch}%`;style.transform=`rotate(${e.rotate??0}deg) scaleX(${stretch})`;style.transformOrigin='top left'
    if(e.nowrap)style.whiteSpace='pre'
    content=e.runs?e.runs.map((run,i)=><span key={i} style={{color:run.color,fontWeight:run.weight,fontStyle:run.fontStyle,fontFamily:run.font?resolveFont(run.font):undefined}}>{run.text}</span>):e.text
  }
  if(e.kind==='text'&&e.valign) {style.display='flex';style.flexDirection='column';style.justifyContent=e.valign==='middle'?'center':e.valign==='bottom'?'flex-end':'flex-start'}
  if(e.kind==='chip') {style.background=e.fill;style.border=e.border;style.display='flex';style.alignItems='center';style.justifyContent=e.align==='left'?'flex-start':e.align==='right'?'flex-end':'center';style.padding=e.padding??0;style.lineHeight=e.lineHeight??1;style.whiteSpace='pre';content=<ChipLabel element={e}/>}
  if(e.kind==='box') {style.background=e.fill;style.border=e.border;style.boxShadow=e.shadow}
  if(e.kind==='image') {style.background='#e5e5e5';style.border=e.border;content=<span className="sr-only">{e.text??'Image placeholder'}</span>}
  if(e.kind==='line') {if(e.vertical)style.width=e.strokeWidth??1;else style.height=e.strokeWidth??1;style.background=e.color??'#bbb'}
  if(e.kind==='icon') {
    const Icon=(Icons as unknown as Record<string,ComponentType<{size?:number;strokeWidth?:number}>>)[e.icon??'Circle']??Icons.Circle
    content=<Icon size={Math.min(e.w*12.8,e.h*7.2)} strokeWidth={e.strokeWidth??1.5} />
  }
  if(e.kind==='bars') content=<Bars element={e}/>
  if(e.kind==='donut') content=<Donut element={e}/>
  if(e.kind==='table') content=<table className="data-table"><tbody>{e.rows?.map((row,i)=><tr key={i}>{row.map((cell,j)=><td key={j} style={{borderColor:e.border??'#ddd',background:i===0?e.fill:undefined}}>{cell}</td>)}</tr>)}</tbody></table>
  if(e.kind==='path')content=<VectorPath element={e}/>
  return <div className={`element element-${e.kind}`} style={style} data-allow-clip={e.allowClip?'true':undefined} data-clip-reason={e.clipReason} role={e.kind==='image'?'img':undefined} aria-label={e.kind==='image'?(e.text??'Image placeholder'):undefined}>{content}</div>
}
export function sourceVisibility(deck:Deck,index:number) {
 const r=deck.referenceRegions[index]
 if(!r)return {x:0,y:0,w:100,h:100}
 const left=Math.max(0,-r.x/r.w*100),top=Math.max(0,-r.y/r.h*100)
 const right=Math.min(100,(100-r.x)/r.w*100),bottom=Math.min(100,(100-r.y)/r.h*100)
 return {x:left,y:top,w:Math.max(0,right-left),h:Math.max(0,bottom-top)}
}
export function SlideCanvas({slide,visible}:{slide:Slide;visible?:{x:number;y:number;w:number;h:number}}) {
 const clip=visible?`inset(${visible.y}% ${100-visible.x-visible.w}% ${100-visible.y-visible.h}% ${visible.x}%)`:undefined
  return <article className="slide-canvas" data-slide={slide.id} style={{background:slide.background}} aria-label={slide.title}>
    <div style={{position:'absolute',inset:0,clipPath:clip}}>{slide.elements.map((element,i)=><ElementView element={element} sourceAspect={slide.sourceAspect} key={i}/>)}</div>
  </article>
}
export function ReferenceBoard({deck}:{deck:Deck}) {
 const size=deck.referenceSize??{width:1024,height:768}
 return <section className="reference-board" data-reference-board={deck.id} style={{width:size.width,height:size.height,background:deck.referenceBackground??'#ddd',position:'relative',overflow:'hidden'}}>
  {deck.slides.map((slide,i)=>{
   const r=deck.referenceRegions[i]
   return <div key={slide.id} style={{position:'absolute',left:r.x/100*size.width,top:r.y/100*size.height,width:1280,height:720,transform:`scale(${r.w/100*size.width/1280},${r.h/100*size.height/720})`,transformOrigin:'top left'}}><SlideCanvas slide={slide}/></div>
  })}
 </section>
}
export function ScaledReferenceBoard({deck,width=560}:{deck:Deck;width?:number}) {
 const size=deck.referenceSize??{width:1024,height:768},scale=width/size.width
 return <div style={{width,height:size.height*scale,overflow:'hidden'}}><div style={{transform:`scale(${scale})`,transformOrigin:'top left'}}><ReferenceBoard deck={deck}/></div></div>
}
export function ScaledSlide({slide,width=480,visible}:{slide:Slide;width?:number;visible?:{x:number;y:number;w:number;h:number}}) {
  return <div style={{width,height:width*9/16,overflow:'hidden'}}><div style={{transform:`scale(${width/1280})`,transformOrigin:'top left'}}><SlideCanvas slide={slide} visible={visible}/></div></div>
}

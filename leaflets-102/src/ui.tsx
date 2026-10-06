import * as Icons from 'lucide-react'
import {useEffect,useState,type CSSProperties,type ComponentType} from 'react'
import type {Element,Panel,Side} from './model'
import {resolveFont} from './fonts'
function Chip({element:e}:{element:Element}){
 const ctx=document.createElement('canvas').getContext('2d')!
 ctx.font=`${e.fontStyle??'normal'} ${e.weight??600} ${e.size??18}px ${resolveFont(e.font)}`;ctx.letterSpacing=`${e.letterSpacing??0}px`
 const line=(e.text??'').split('\n').sort((a,b)=>b.length-a.length)[0],m=ctx.measureText(line)
 const x=(m.width-m.actualBoundingBoxRight+m.actualBoundingBoxLeft)/2,y=(m.actualBoundingBoxAscent-m.actualBoundingBoxDescent-m.fontBoundingBoxAscent+m.fontBoundingBoxDescent)/2
 return <span data-chip-label style={{transform:`translate(${x}px,${y}px)`}}>{e.text}</span>
}
function ElementView({element:e}:{element:Element}){
 const style:CSSProperties={position:'absolute',left:e.x,top:e.y,width:e.w,height:e.h,color:e.color??'#111',fontFamily:resolveFont(e.font),fontWeight:e.weight??400,fontStyle:e.fontStyle,fontSize:e.size??16,lineHeight:e.lineHeight??1.25,letterSpacing:e.letterSpacing??0,textAlign:e.align??'left',borderRadius:e.radius??0,border:e.border,opacity:e.opacity??1,whiteSpace:'pre-wrap',WebkitTextStroke:e.textStroke,paintOrder:'stroke fill',transform:e.rotate?`rotate(${e.rotate}deg)`:undefined,transformOrigin:'top left'}
 let child
 if(e.kind==='box')style.background=e.fill
 if(e.kind==='image'){style.background='#e5e5e5';child=<span className="sr-only">이미지 영역</span>}
 if(e.kind==='text'){
  child=e.text
  if(e.chip){style.background=e.fill;style.display='flex';style.alignItems='center';style.justifyContent=e.align==='left'?'flex-start':e.align==='right'?'flex-end':'center';style.whiteSpace='pre';style.lineHeight=e.lineHeight??1;child=<Chip element={e}/>}
 }
 if(e.kind==='donut'){let at=0;const total=(e.values??[]).reduce((a,b)=>a+b,0)||1;const segments=(e.values??[]).map((v,i)=>{const start=at;at+=v/total*100;return `${e.colors?.[i]??'#168dc1'} ${start}% ${at}%`});style.background=`conic-gradient(${segments.join(',')})`;style.borderRadius='50%';style.display='flex';style.alignItems='center';style.justifyContent='center';child=<div style={{width:`${(e.hole??.7)*100}%`,height:`${(e.hole??.7)*100}%`,borderRadius:'50%',background:e.fill??'#fff'}}/>}
 if(e.kind==='icon'){const Icon=(Icons as unknown as Record<string,ComponentType<{size:number;strokeWidth:number}>>)[e.icon??'Circle']??Icons.Circle;style.display='flex';style.alignItems='center';style.justifyContent='center';child=<Icon size={Math.min(e.w,e.h)} strokeWidth={e.strokeWidth??1.5}/>}
 if(e.kind==='path'){child=<svg width="100%" height="100%" viewBox={`0 0 ${e.w} ${e.h}`} preserveAspectRatio="none" style={{overflow:'visible'}}><path d={e.d??((e.points??[]).map(([x,y],i)=>`${i?'L':'M'}${x} ${y}`).join(' ')+(e.closed?' Z':''))} fill={e.fill??'none'} stroke={e.color??'#111'} strokeWidth={e.strokeWidth??1}/></svg>}
 return <div className={`element element-${e.kind}`} style={style} data-element-id={e.id} data-chip={e.chip?'true':undefined} data-replacement={e.replacement?'true':undefined}>{child}</div>
}
export function PageCanvas({page}:{page:Panel|Side}){
 const [ready,setReady]=useState(false),[paint,setPaint]=useState(0)
 useEffect(()=>{
  let active=true;setReady(false)
  const glyphs=new Map<string,string>()
  for(const e of page.elements.filter(e=>e.kind==='text')){
   const font=`${e.fontStyle??'normal'} ${e.weight??400} ${e.size??16}px ${resolveFont(e.font)}`
   glyphs.set(font,(glyphs.get(font)??'')+(e.text??''))
  }
  Promise.all([...glyphs].map(([font,text])=>document.fonts.load(font,text))).then(()=>document.fonts.ready).then(()=>{
   if(active){setPaint(n=>n+1);setReady(true)}
  })
  return()=>{active=false}
 },[page])
 const scale=1,left=0,top=0
 return <article className="page-canvas" data-page={page.id} data-fonts-ready={ready?'true':'false'} aria-label={'title' in page?page.title:page.id}><div className="paper" data-paper style={{position:'absolute',left,top,width:1280,height:910,transform:`scale(${scale})`,transformOrigin:'top left',overflow:'hidden'}} key={paint}>{page.elements.map((e,i)=><ElementView element={e} key={i}/>)}</div></article>
}
export function Thumbnail({page,width=360}:{page:Panel|Side;width?:number}){return <div style={{width,height:width*910/1280,overflow:'hidden'}}><div style={{transform:`scale(${width/1280})`,transformOrigin:'top left'}}><PageCanvas page={page}/></div></div>}

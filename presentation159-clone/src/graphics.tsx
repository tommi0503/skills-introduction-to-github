import {useId} from 'react'
import type {ReactNode} from 'react'
import type {Element,GraphicOptions,SvgShape} from './model'

// All graphics are DOM/SVG geometry or procedural SVG filters, never reference bitmaps.
const number=(value:unknown,fallback:number)=>typeof value==='number'?value:fallback
const string=(value:unknown,fallback:string)=>typeof value==='string'?value:fallback
function seedRandom(seed:number){let state=seed>>>0;return()=>{state=(Math.imul(state,1664525)+1013904223)>>>0;return state/4294967296}}
function halftone(w:number,h:number,o:GraphicOptions):ReactNode {
 const spacing=o.spacing??20,color=o.color??'#bdea89',variant=o.variant??'corner'
 const nodes=[]
 for(let row=0,y=spacing/2;y<h;y+=spacing,row++)for(let x=spacing/2+(row%2)*spacing/2;x<w;x+=spacing){
  const nx=x/w,ny=y/h
  const strength=variant==='uniform'?1:variant==='band'?Math.sin(Math.PI*ny):variant==='wave'?(1+Math.cos(nx*4+ny*3))/2:Math.max(0,1-Math.hypot((1-nx)*1.05,(ny-.5)*1.5))
  const r=spacing*.46*Math.pow(strength,.85)
  if(r>.55)nodes.push(<circle key={`${row}-${x}`} cx={x} cy={y} r={r} fill={color}/>)
 }
 return nodes
}
function waves(w:number,h:number,o:GraphicOptions):ReactNode {
 const spacing=o.spacing??14,color=o.color??'#f36c23',amplitude=number(o.amplitude,spacing*.34),period=number(o.period,spacing*2.1)
 const paths=[]
 for(let y=-spacing;y<h+spacing;y+=spacing){let d='';for(let x=-spacing;x<w+spacing;x+=3)d+=`${d?' L':'M'}${x},${y+Math.sin(x/period*Math.PI*2)*amplitude}`;paths.push(<path key={y} d={d} fill="none" stroke={color} strokeWidth={o.stroke??2.2}/>)}
 return paths
}
function contours(w:number,h:number,o:GraphicOptions):ReactNode {
 const paths=[],spacing=o.spacing??22,variant=o.variant??'waves'
 for(let i=-8;i<Math.ceil(h/spacing)+8;i++){
  const y=i*spacing
  const d=variant==='diagonal'?`M -50 ${y+h*.2} C ${w*.22} ${y-h*.12} ${w*.42} ${y+h*.28} ${w*.63} ${y} S ${w*.89} ${y-h*.24} ${w+70} ${y+h*.04}`:`M -50 ${y} C ${w*.25} ${y+h*.28} ${w*.3} ${y-h*.28} ${w*.52} ${y} S ${w*.8} ${y+h*.22} ${w+50} ${y-h*.06}`
  paths.push(<path key={i} d={d} fill="none" stroke={o.color??'#b6bdac'} strokeWidth={o.stroke??1.1}/>)}
 return paths
}
function wireframe(w:number,h:number,o:GraphicOptions):ReactNode {
 const color=o.color??'#fff',stroke=o.stroke??1.2,paths=[]
 const cx=w*.52,cy=h*.53,rx=w*.48,ry=h*.45
 for(let i=-8;i<=8;i++){const t=i/9,scale=Math.sqrt(1-t*t);paths.push(<ellipse key={`h${i}`} cx={cx} cy={cy+t*ry} rx={rx*scale} ry={ry*.16*scale} fill="none" stroke={color} strokeWidth={stroke}/>)}
 for(let i=-7;i<=7;i++){const t=i/8;paths.push(<ellipse key={`v${i}`} cx={cx} cy={cy} rx={Math.max(1,Math.abs(t)*rx)} ry={ry} fill="none" stroke={color} strokeWidth={stroke} transform={`rotate(${t*24} ${cx} ${cy})`}/>)}
 return paths
}
function tornPaper(w:number,h:number,o:GraphicOptions):ReactNode {
 const random=seedRandom(o.seed??17),step=o.spacing??12,points=[]
 for(let x=0;x<=w;x+=step)points.push(`${x},${random()*8}`)
 for(let y=0;y<=h;y+=step)points.push(`${w-random()*8},${y}`)
 for(let x=w;x>=0;x-=step)points.push(`${x},${h-random()*8}`)
 for(let y=h;y>=0;y-=step)points.push(`${random()*8},${y}`)
 return <polygon points={points.join(' ')} fill={o.color??'#fff'} stroke={o.accent??'none'} strokeWidth={o.stroke??1}/>
}
function botanical(w:number,h:number,o:GraphicOptions):ReactNode {
 const color=o.color??'#f2f4ec',stroke=o.stroke??2.5
 return <g fill="none" stroke={color} strokeWidth={stroke} strokeLinecap="round">
  <path d={`M ${w*.44} ${h} Q ${w*.55} ${h*.58} ${w*.43} ${h*.08}`}/>
  {Array.from({length:7},(_,i)=>{const y=h*(.18+i*.1),side=i%2?-1:1,x=w*.46;return <path key={i} d={`M ${x} ${y+h*.09} Q ${x+side*w*.4} ${y+h*.03} ${x+side*w*.37} ${y-h*.12} Q ${x+side*w*.08} ${y-h*.16} ${x} ${y+h*.09} M ${x} ${y+h*.09} L ${x+side*w*.31} ${y-h*.09}`}/>})}
 </g>
}
function Shape({shape:s,kind,prefix}:{shape:SvgShape;kind:string;prefix:string}){
 const rewrite=(value?:string)=>value?.replace(/url\(#([^)]*)\)/g,`url(#${prefix}-$1)`)
 const props={...s,fill:rewrite(s.fill)??'none',stroke:rewrite(s.stroke)}
 if(kind==='path')return <path {...props}/>
 if(kind==='circle')return <circle {...props}/>
 if(kind==='rect')return <rect {...props}/>
 return <line {...props}/>
}
export function SvgGraphic({element:e}:{element:Element}){
 const prefix='graphic-'+useId().replace(/[^a-zA-Z0-9-]/g,''),o=e.graphicOptions??{},w=e.w*16,h=e.h*9
 let content:ReactNode=null,defs:ReactNode=null
 const name=e.graphic??'custom',color=o.color??'#222'
 if(name==='custom'){
  defs=o.gradients?.map(g=>g.type==='radial'?<radialGradient id={`${prefix}-${g.id}`} key={g.id} cx={g.cx} cy={g.cy} r={g.r}>{g.stops.map((s,i)=><stop key={i} offset={s.offset} stopColor={s.color} stopOpacity={s.opacity??1}/>)}</radialGradient>:<linearGradient id={`${prefix}-${g.id}`} key={g.id} x1={g.x1} y1={g.y1} x2={g.x2} y2={g.y2}>{g.stops.map((s,i)=><stop key={i} offset={s.offset} stopColor={s.color} stopOpacity={s.opacity??1}/>)}</linearGradient>)
  content=<>{o.paths?.map((s,i)=><Shape key={`p${i}`} shape={s} kind="path" prefix={prefix}/>)}{o.circles?.map((s,i)=><Shape key={`c${i}`} shape={s} kind="circle" prefix={prefix}/>)}{o.rects?.map((s,i)=><Shape key={`r${i}`} shape={s} kind="rect" prefix={prefix}/>)}{o.lines?.map((s,i)=><Shape key={`l${i}`} shape={s} kind="line" prefix={prefix}/>)}</>
 }else if(name==='halftone')content=halftone(w,h,o)
 else if(name==='wavy-circle'){defs=<clipPath id={`${prefix}-clip`}><ellipse cx={w/2} cy={h/2} rx={w/2} ry={h/2}/></clipPath>;content=<g clipPath={`url(#${prefix}-clip)`}>{waves(w,h,o)}</g>}
 else if(name==='contour-lines')content=contours(w,h,o)
 else if(name==='wireframe')content=wireframe(w,h,o)
 else if(name==='torn-paper')content=tornPaper(w,h,o)
 else if(name==='botanical')content=botanical(w,h,o)
 else if(name==='marble'){
  const fallback=['#183d32','#80a158','#d2e797','#f1f5c1','#526f45','#aec778','#e4ebaf','#658f63','#285c4c','#c5da88','#ebefc9','#698968']
  const palette=Array.isArray(o.palette)&&o.palette.every(value=>typeof value==='string'&&/^#[0-9a-f]{6}$/i.test(value))?o.palette as string[]:fallback
  const channel=(offset:number)=>palette.map(value=>parseInt(value.slice(offset,offset+2),16)/255).join(' ')
  defs=<filter id={`${prefix}-marble`} x="0" y="0" width="100%" height="100%" colorInterpolationFilters="sRGB">
   <feTurbulence type="fractalNoise" baseFrequency={string(o.frequency,'0.009 0.016')} numOctaves="3" seed={o.seed??50} result="field"/>
   <feTurbulence type="fractalNoise" baseFrequency="0.015 0.023" numOctaves="2" seed={(o.seed??50)+19} result="warp"/>
   <feDisplacementMap in="field" in2="warp" scale={number(o.displacement,190)} xChannelSelector="R" yChannelSelector="G" result="flow"/>
   <feColorMatrix in="flow" type="saturate" values="0"/>
   <feComponentTransfer><feFuncR type="table" tableValues={channel(1)}/><feFuncG type="table" tableValues={channel(3)}/><feFuncB type="table" tableValues={channel(5)}/><feFuncA type="table" tableValues="1 1"/></feComponentTransfer>
  </filter>
  content=<rect width={w} height={h} fill={color} filter={`url(#${prefix}-marble)`}/>
 }
 else if(name==='grain'){
  const rgb=/^#[0-9a-f]{6}$/i.test(color)?[1,3,5].map(i=>parseInt(color.slice(i,i+2),16)/255):[1,1,1]
  defs=<filter id={`${prefix}-grain`} x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency={string(o.frequency,'0.72')} numOctaves="3" seed={o.seed??7}/><feColorMatrix type="matrix" values={`0 0 0 0 ${rgb[0]} 0 0 0 0 ${rgb[1]} 0 0 0 0 ${rgb[2]} 1 0 0 0 0`}/></filter>
  content=<rect width={w} height={h} filter={`url(#${prefix}-grain)`}/>
 }else if(name==='grid'){
  const spacing=o.spacing??40;defs=<pattern id={`${prefix}-grid`} width={spacing} height={spacing} patternUnits="userSpaceOnUse"><path d={`M ${spacing} 0 H 0 V ${spacing}`} fill="none" stroke={color} strokeWidth={o.stroke??1}/></pattern>;content=<rect width={w} height={h} fill={`url(#${prefix}-grid)`}/>
 }else if(name==='paperclip'){
  content=<g transform={`scale(${w/100} ${h/100})`} fill="none" stroke={color} strokeWidth={o.stroke??4} strokeLinecap="round"><path d="M 28 69 L 28 29 Q 28 8 48 8 Q 68 8 68 29 V 76 Q 68 92 53 92 Q 38 92 38 76 V 30 Q 38 21 47 21 Q 56 21 56 30 V 72"/></g>
 }else if(name==='scribble-star'){
  content=<g transform={`scale(${w/100} ${h/100})`} fill="none" stroke={color} strokeWidth={o.stroke??3} strokeLinecap="round" strokeLinejoin="round"><path d="M48 5 L60 35 L94 23 L70 52 L91 80 L58 70 L37 97 L36 63 L5 52 L34 38 Z M51 9 L58 34 L88 25 L68 50 L87 75 L58 68 L39 90"/></g>
 }else if(name==='scribble-candy'){
  content=<g transform={`scale(${w/160} ${h/90})`} stroke={color} strokeWidth={o.stroke??2.5} fill="none" strokeLinejoin="round"><path d="M42 20 Q75 6 118 22 L124 68 Q86 86 41 67 Z M43 24 L7 8 L20 43 L3 76 L43 64 M120 23 L155 8 L141 43 L157 77 L123 66 M63 17 L69 75 M86 15 L94 77 M107 18 L115 72"/></g>
 }
 return <svg width="100%" height="100%" viewBox={o.viewBox??`0 0 ${w} ${h}`} preserveAspectRatio="none" aria-hidden="true" data-svg-graphic={name} style={{display:'block',overflow:'visible'}}><defs>{defs}</defs>{o.background&&<rect width={w} height={h} fill={o.background}/>} {content}</svg>
}

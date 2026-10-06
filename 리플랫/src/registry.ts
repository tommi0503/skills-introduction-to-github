import manifest from '../public/reference/manifest.json'
import type {Brochure,Element,Region,SidePatch} from './model'
const modules=import.meta.glob<{default:Record<string,SidePatch>}>('./data/patch-*.ts',{eager:true})
const patches=Object.assign({},...Object.values(modules).map(m=>m.default)) as Record<string,SidePatch>
const baselines=import.meta.glob<{default:{elements:Element[]}}>('./data/baseline/*.json',{eager:true})
const inside=(e:Element,r:Region)=>e.x+e.w/2>=r.x&&e.x+e.w/2<=r.x+r.w&&e.y+e.h/2>=r.y&&e.y+e.h/2<=r.y+r.h
export const brochures:Brochure[]=manifest.map(original=>{
 const sides=original.sides.map(s=>{
  const key=`${original.id}/${s.id}`,patch=patches[key]??{},base=baselines[`./data/baseline/${original.id}-${s.id}.json`]?.default.elements??[]
  const shapeBase=base.filter(e=>e.kind!=='text'&&!patch.clearShapes&&!patch.removeShapes?.some(r=>inside(e,r)))
  const texts=base.filter(e=>e.kind==='text'&&!patch.images?.some(r=>r.dropText!==false&&inside(e,r))&&!patch.removeText?.some(r=>inside(e,r))).map(e=>({...e,font:patch.defaultFont??e.font,weight:patch.defaultWeight??e.weight,...patch.textStyles?.filter(r=>inside(e,r)).reduce((a,{x,y,w,h,...rest})=>({...a,...rest}),{}),...patch.textEdits?.[e.id??'']}))
  const images=(patch.images??[]).map(r=>({kind:'image' as const,...r,fill:'#e5e5e5'}))
  const decoration=(patch.elements??[]).filter(e=>e.kind==='box'||e.kind==='path')
  const foreground=(patch.elements??[]).filter(e=>e.kind!=='box'&&e.kind!=='path')
  return {id:s.id,size:s.size as [number,number],reference:s.reference,elements:[{kind:'box' as const,x:0,y:0,w:s.size[0],h:s.size[1],fill:patch.background??'#fff'},...images.filter(e=>e.layer==='background'),...shapeBase,...decoration,...images.filter(e=>e.layer!=='background'),...patch.underTextElements??[],...texts,...foreground],notes:patch.notes??[]}
 })
 const panels=sides.flatMap(s=>Array.from({length:3},(_,i)=>{
  const left=Math.round(s.size[0]*i/3),right=Math.round(s.size[0]*(i+1)/3)
  return {id:`${s.id}-p${i+1}`,title:`${original.title} · ${s.id==='s01'?'앞면':'뒷면'} ${i+1}`,sideId:s.id,index:i,crop:{x:left,y:0,w:right-left,h:s.size[1]},size:[right-left,s.size[1]] as [number,number],reference:s.reference,elements:s.elements.filter(e=>e.x<right&&e.x+e.w>left).map(e=>({...e,x:e.x-left}))}
 }))
 return {id:original.id,title:original.title,sides,panels}
})

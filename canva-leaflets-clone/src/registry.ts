import manifest from '../public/reference/manifest.json'
import type {Brochure,BrochureDraft,Element} from './model'
import {groupA} from './data/group-a'
import {groupB} from './data/group-b'
import {groupC} from './data/group-c'
import {groupD} from './data/group-d'
import {groupE} from './data/group-e'
import {groupF} from './data/group-f'
const drafts:BrochureDraft[]=[...groupA,...groupB,...groupC,...groupD,...groupE,...groupF]
function panelElements(elements:Element[],x:number,w:number,h:number):Element[]{
 return elements.filter(e=>e.x+e.w>x&&e.x<x+w&&e.y+e.h>0&&e.y<h).map(e=>({...e,x:e.x-x,foldClip:e.x<x||e.x+e.w>x+w,clipReason:e.clipReason??((e.x<x||e.x+e.w>x+w)?'Shared original element is cropped at the native fold boundary':undefined)}))
}
export const brochures:Brochure[]=manifest.map(item=>{
 const draft=drafts.find(d=>d.id===item.id)
 const sides=item.sides.map(s=>{
  const data=draft?.sides.find(d=>d.id===s.id)
  return {id:s.id,size:s.size as [number,number],reference:s.reference,elements:data?.elements??[],notes:data?.notes??['Implementation pending']}
 })
 const panels=sides.flatMap(side=>{
  const [w,h]=side.size;const edges=Array.from({length:item.foldCount+1},(_,i)=>Math.round(w*i/item.foldCount))
  return Array.from({length:item.foldCount},(_,i)=>i).map(index=>{const x=edges[index],width=edges[index+1]-x;return{id:`${side.id}-p${index+1}`,title:`${side.id==='s01'?'앞면':'뒷면'} ${index+1}번째 접지면`,sideId:side.id,index,crop:{x,y:0,w:width,h},size:[width,h] as [number,number],reference:side.reference,elements:panelElements(side.elements,x,width,h),notes:side.notes}})
 })
 return {id:item.id,title:item.title,designId:item.designId,sides,panels}
})
export const missingImplementations=manifest.flatMap(item=>item.sides.filter(s=>!drafts.find(d=>d.id===item.id)?.sides.find(d=>d.id===s.id)?.elements.length).map(s=>`${item.id}/${s.id}`))

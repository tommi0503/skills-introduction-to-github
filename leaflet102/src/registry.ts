import type {Side} from './model'
import manifest from './data/manifest.json'
const groups=import.meta.glob<{pages:Side[]}>('./data/group-*.ts',{eager:true})
export const pages=Object.values(groups).flatMap(g=>g.pages??[]).map(p=>({...p,size:[1280,910] as [number,number]})).sort((a,b)=>a.id.localeCompare(b.id))
export const pageTitle=(id:string)=>manifest.find(r=>r.filename===`${id}.png`)?.title??id
export const decks=Array.from({length:51},(_,i)=>({id:String(i+1).padStart(2,'0'),title:pageTitle(String(i*2+1).padStart(3,'0')),pages:pages.filter(p=>Number(p.id)===i*2+1||Number(p.id)===i*2+2)}))

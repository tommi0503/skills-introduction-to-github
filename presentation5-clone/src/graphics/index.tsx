import a from './group-a'
import ax from './group-a-extra'
import b from './group-b'
import bx from './group-b-extra'
import c from './group-c'
import cx from './group-c-extra'
import type {GraphicProps,GraphicScenes} from './types'

const sceneEntries=[a,ax,b,bx,c,cx].flatMap(group=>Object.entries(group))
if(new Set(sceneEntries.map(([name])=>name)).size!==sceneEntries.length)throw new Error('Duplicate vector scene registry name')
export const graphicScenes:GraphicScenes=Object.fromEntries(sceneEntries)
export function Graphic({name,...props}:GraphicProps&{name:string}) {
 const Scene=graphicScenes[name]
 if(!Scene)throw new Error(`Unregistered vector scene: ${name}`)
 return <Scene {...props}/>
}
declare global {interface Window {__presentationGraphics:string[]}}
window.__presentationGraphics=Object.keys(graphicScenes)

import React,{type CSSProperties,type ReactNode} from 'react';
import type {RectProps} from './ui';
// Page-author adapter: the same source content is assembled into contract roots.
// Geometry belongs to the page; type and component structure come from the collection.
const step=(n:number)=>n<=32?Math.max(8,Math.round(n/2)*2):Math.min(128,Math.round(n/4)*4);
export function LibraryText({rect,typo,children,size}:{rect:CSSProperties,typo:CSSProperties,children:ReactNode,size:number}){
 const layoutKeys=['display','alignItems','justifyContent','padding','paddingTop','paddingRight','paddingBottom','paddingLeft','whiteSpace','flexDirection','gap','wordBreak','overflowWrap','textWrap'];
 const layout=Object.fromEntries(Object.entries(typo).filter(([k])=>layoutKeys.includes(k)));
 const metric=size>=42&&typeof children==='string'&&/^[\d+−-]/.test(children),root=metric?'stat':'card',el=metric?'metric':'card';
 const vars={...rect,'--rebuild-size':`var(--type-${step(size)})`,'--rebuild-zoom':size/step(size),'--rebuild-font':typo.fontFamily,'--rebuild-weight':typo.fontWeight,'--rebuild-line':typo.lineHeight,'--rebuild-track':typeof typo.letterSpacing==='number'?`${typo.letterSpacing}px`:typo.letterSpacing,'--rebuild-color':typo.color,textAlign:typo.textAlign,...Object.fromEntries(Object.entries(typo).filter(([k])=>![...layoutKeys,'fontSize','fontFamily','fontWeight','lineHeight','letterSpacing','color','textAlign'].includes(k)))} as CSSProperties;
 return <div className={`${root} quiet overrides`} data-el={`studio-spectrum-${el}`} style={vars}><div className="parts"><div className={metric?'fig':'name'} style={{width:'100%',height:'100%',...layout}} data-text="true">{children}</div></div></div>
}
export function LibraryFrame(p:RectProps&{radius?:number|string}){return <div className="frame overrides" data-el="studio-spectrum-image-frame" style={{position:'absolute',left:p.x??0,top:p.y??0,width:p.w,height:p.h,borderRadius:p.radius??0,...p.style}}><div className="seat" data-ph="" data-placeholder="true"/></div>}

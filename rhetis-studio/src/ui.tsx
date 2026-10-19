import {LibraryText,LibraryFrame} from './library';
import React, {useRef,useLayoutEffect,type CSSProperties,type ReactNode} from 'react';
import * as Icons from 'lucide-react';
export type RectProps={x?:number,y?:number,w?:number|string,h?:number|string,style?:CSSProperties,children?:ReactNode};
const rebuilding=new URLSearchParams(location.search).get('mode')==='assembled';
const rect=({x=0,y=0,w,h}:RectProps):CSSProperties=>({position:'absolute',left:x,top:y,width:w,height:h});
function Optical({children}:{children:ReactNode}){const ref=useRef<HTMLSpanElement>(null);useLayoutEffect(()=>{let active=true;document.fonts.ready.then(()=>{if(!active||!ref.current)return;const el=ref.current,s=getComputedStyle(el),ctx=document.createElement('canvas').getContext('2d')!;ctx.font=`${s.fontStyle} ${s.fontWeight} ${s.fontSize} ${s.fontFamily}`;ctx.letterSpacing=s.letterSpacing;const m=ctx.measureText(el.textContent||'');const dx=(m.actualBoundingBoxRight-m.actualBoundingBoxLeft-m.width)/2;const dy=(m.fontBoundingBoxAscent-m.fontBoundingBoxDescent+m.actualBoundingBoxDescent-m.actualBoundingBoxAscent)/2;el.style.transform=`translate(${-dx}px,${-dy}px)`;});return()=>{active=false}},[children]);return <span ref={ref} data-chip-label="true" style={{display:'block',flex:'none'}}>{children}</span>}
export function T(p:RectProps & {size?:number,weight?:number|string,color?:string,font?:string,align?:CSSProperties['textAlign'],lineHeight?:number|string,spacing?:number|string,className?:string,chip?:boolean}){
 const {size=20,weight=400,color='#222',font='Pretendard',align='left',lineHeight=1.35,spacing=0,children,style,className=''}=p;
 const centered=!!(p.chip||(style?.display==='flex'&&style?.alignItems==='center'&&style?.justifyContent==='center'&&typeof children==='string'&&!children.includes('\n')));
 const content=centered?<Optical>{children}</Optical>:children;
 if(rebuilding)return <LibraryText rect={rect(p)} typo={{fontSize:size,fontWeight:weight,fontFamily:font,color,textAlign:align,lineHeight,letterSpacing:spacing,whiteSpace:'pre-wrap',...style}} size={size}>{content}</LibraryText>;
 return <div data-text="true" data-chip={centered?'true':undefined} className={'text '+className} style={{...rect(p),fontSize:size,fontWeight:weight,fontFamily:font,color,textAlign:align,lineHeight,letterSpacing:spacing,whiteSpace:'pre-wrap',...style}}>{content}</div>
}
export function Box(p:RectProps & {fill?:string,stroke?:string,radius?:number|string,className?:string}) {return <div className={p.className} style={{...rect(p),background:p.fill??'transparent',border:p.stroke?`1px solid ${p.stroke}`:undefined,borderRadius:p.radius??0,...p.style}}>{p.children}</div>}
export function PH(p:RectProps & {radius?:number|string}) {if(rebuilding)return <LibraryFrame {...p}/>;return <div data-placeholder="true" aria-label="Image placeholder" style={{...rect(p),background:'#e5e5e5',borderRadius:p.radius??0,...p.style}}/>}
export function Line(p:RectProps & {color?:string,width?:number}) {return <div style={{...rect(p),width:p.w===0?(p.width??1):(p.w??1),height:p.h===0?(p.width??1):(p.h??(p.width??1)),background:p.color??'#ccc',...p.style}}/>}
export function Icon({name,x=0,y=0,size=24,color='#222',strokeWidth=1.5,style}: {name:string,x?:number,y?:number,size?:number,color?:string,strokeWidth?:number,style?:CSSProperties}){const Comp=(Icons as any)[name]??Icons.Circle;return <Comp aria-hidden style={{position:'absolute',left:x,top:y,...style}} width={size} height={size} color={color} strokeWidth={strokeWidth}/>}

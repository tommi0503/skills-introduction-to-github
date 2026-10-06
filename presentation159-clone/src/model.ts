export type Kind = 'text' | 'box' | 'image' | 'icon' | 'line' | 'bars' | 'donut' | 'table' | 'path' | 'chip' | 'graphic'
export interface SvgShape {
 d?:string; x?:number; y?:number; width?:number; height?:number; rx?:number; ry?:number;
 cx?:number; cy?:number; r?:number; x1?:number; y1?:number; x2?:number; y2?:number;
 fill?:string; stroke?:string; strokeWidth?:number; opacity?:number; transform?:string;
 strokeLinecap?:'round'|'butt'|'square'; strokeLinejoin?:'round'|'miter'|'bevel'; strokeDasharray?:string;
}
export interface SvgGradient {
 id:string; type?:'linear'|'radial'; x1?:string; y1?:string; x2?:string; y2?:string;
 cx?:string; cy?:string; r?:string; stops:{offset:number|string;color:string;opacity?:number}[];
}
export interface GraphicOptions {
 color?:string; accent?:string; background?:string; spacing?:number; stroke?:number;
 seed?:number; variant?:string; viewBox?:string; direction?:string; density?:number;
 paths?:SvgShape[]; circles?:SvgShape[]; rects?:SvgShape[]; lines?:SvgShape[]; gradients?:SvgGradient[];
 [key:string]:unknown;
}
export interface TextRun { text:string; color?:string; weight?:number; font?:string; fontStyle?:'normal'|'italic' }
export interface Point { x:number; y:number }
export interface Element {
  kind: Kind; x: number; y: number; w: number; h: number;
  text?: string; size?: number; color?: string; fill?: string; weight?: number;
  font?: string; fontStyle?:'normal'|'italic'; fontVariantNumeric?:'lining-nums'; align?: 'left' | 'center' | 'right' | 'justify'; lineHeight?: number;
  radius?: number|string; border?: string; opacity?: number; icon?: string;
  values?: number[]; labels?: string[]; colors?: string[]; rows?: string[][];
  vertical?: boolean; letterSpacing?: number; strokeWidth?: number;
  textStroke?:string; rotate?:number; scaleX?: number; nowrap?: boolean; runs?: TextRun[];
  points?: Point[]; curved?: boolean; closed?: boolean; cyclic?:boolean; dashed?: boolean; arrow?: boolean;
  labelSize?:number; valueSize?:number; showValues?:boolean; max?:number;
  clipPath?:string; valign?:'top'|'middle'|'bottom'; padding?:number; shadow?:string; allowClip?:boolean; clipReason?:string;
  mask?:string; filter?:string; blendMode?:'normal'|'multiply'|'screen'|'overlay'|'soft-light'|'hard-light';
  graphic?:string; graphicOptions?:GraphicOptions;
}
export interface Slide { id: string; title: string; background: string; elements: Element[]; sourceAspect?:number }
export interface Region { x: number; y: number; w: number; h: number }
export interface Deck { id: string; title: string; slides: Slide[]; columns?: number; referenceRegions: Region[]; referenceSize?:{width:number;height:number}; referenceBackground?:string; references?:string[] }
export const text = (x:number,y:number,w:number,h:number,value:string,size=32,extra:Partial<Element>={}):Element => ({kind:'text',x,y,w,h,text:value,size,...extra})
export const box = (x:number,y:number,w:number,h:number,fill:string,extra:Partial<Element>={}):Element => ({kind:'box',x,y,w,h,fill,...extra})
export const image = (x:number,y:number,w:number,h:number,label='Image',extra:Partial<Element>={}):Element => ({kind:'image',x,y,w,h,text:label,...extra})
export const icon = (x:number,y:number,w:number,h:number,name:string,color='#222',extra:Partial<Element>={}):Element => ({kind:'icon',x,y,w,h,icon:name,color,...extra})
export const line = (x:number,y:number,w:number,color='#bbb',extra:Partial<Element>={}):Element => ({kind:'line',x,y,w,h:0,color,...extra})
export const bars = (x:number,y:number,w:number,h:number,values:number[],labels:string[],extra:Partial<Element>={}):Element => ({kind:'bars',x,y,w,h,values,labels,...extra})
export const donut = (x:number,y:number,w:number,h:number,values:number[],extra:Partial<Element>={}):Element => ({kind:'donut',x,y,w,h,values,...extra})
export const table = (x:number,y:number,w:number,h:number,rows:string[][],extra:Partial<Element>={}):Element => ({kind:'table',x,y,w,h,rows,...extra})
export const footer = (label:string,color='#666'):Element[] => [text(4,94,75,3,label,11,{color}),text(91,94,5,3,'↗',14,{color,align:'right'})]
export const richText = (x:number,y:number,w:number,h:number,runs:TextRun[],size=32,extra:Partial<Element>={}):Element => ({kind:'text',x,y,w,h,runs,size,...extra})
export const path = (x:number,y:number,w:number,h:number,points:Point[],extra:Partial<Element>={}):Element => ({kind:'path',x,y,w,h,points,...extra})

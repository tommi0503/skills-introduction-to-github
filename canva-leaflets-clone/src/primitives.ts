import type {Element} from './model'
// All coordinates are native source pixels. One uniform transform fits each page.
export const T=(x:number,y:number,w:number,h:number,text:string,size:number,extra:Partial<Element>={}):Element=>({kind:'text',x,y,w,h,text,size,font:'Pretendard',weight:400,lineHeight:1.25,...extra})
export const B=(x:number,y:number,w:number,h:number,fill:string,extra:Partial<Element>={}):Element=>({kind:'box',x,y,w,h,fill,...extra})
export const I=(x:number,y:number,w:number,h:number,extra:Partial<Element>={}):Element=>({kind:'image',x,y,w,h,fill:'#e5e5e5',...extra})
export const C=(x:number,y:number,w:number,h:number,text:string,size:number,fill:string,extra:Partial<Element>={}):Element=>T(x,y,w,h,text,size,{chip:true,fill,align:'center',lineHeight:1,radius:18,weight:600,...extra})
export const L=(x:number,y:number,w:number,h:number,color:string):Element=>B(x,y,w,h,color)
export const IC=(x:number,y:number,w:number,h:number,icon:string,color='#111',extra:Partial<Element>={}):Element=>({kind:'icon',x,y,w,h,icon,color,strokeWidth:1.5,...extra})
export const P=(points:number[][],color:string,strokeWidth=1,fill?:string):Element=>{const xs=points.map(p=>p[0]),ys=points.map(p=>p[1]),x=Math.min(...xs),y=Math.min(...ys);return {kind:'path',x,y,w:Math.max(...xs)-x||1,h:Math.max(...ys)-y||1,points:points.map(p=>[p[0]-x,p[1]-y]),color,strokeWidth,fill,closed:!!fill}}

export const DN=(x:number,y:number,w:number,h:number,values:number[],colors:string[],hole=.7):Element=>({kind:'donut',x,y,w,h,values,colors,hole})
// Local SVG coordinates permit simple curved borders without raster artwork.
export const VP=(x:number,y:number,w:number,h:number,d:string,extra:Partial<Element>={}):Element=>({kind:'path',x,y,w,h,d,color:'#111',strokeWidth:1,...extra})

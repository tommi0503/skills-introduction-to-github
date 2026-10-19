// Shared 1280×720 scene model. All slide data remain editable, without raster UI.
export const T=(x,y,w,h,text,size=24,extra={})=>({kind:'text',x,y,w,h,text,size,weight:400,font:'Pretendard',color:'#222',lineHeight:1.35,...extra});
export const B=(x,y,w,h,fill='#fff',extra={})=>({kind:'box',x,y,w,h,fill,...extra});
export const P=(x,y,w,h,extra={})=>({kind:'placeholder',x,y,w,h,fill:'#e6e6e6',...extra});
export const L=(x,y,w,h=0,color='#222',strokeWidth=1,extra={})=>({kind:'line',x,y,w,h,color,strokeWidth,...extra});
export const C=(x,y,w,h,text,size=20,fill='#fff',extra={})=>({kind:'chip',x,y,w,h,text,size,fill,font:'Pretendard',weight:600,color:'#222',align:'center',lineHeight:1,radius:999,...extra});
export const I=(x,y,w,h,icon='Circle',color='#222',extra={})=>({kind:'icon',x,y,w,h,icon,color,strokeWidth:1.6,...extra});
export const V=(x,y,w,h,svg,extra={})=>({kind:'svg',x,y,w,h,svg,...extra});
export const S=(id,title,background,elements)=>({id,title,background,elements});
export const D=(id,title,slides)=>({id,title,slides});

// Declarative scene primitives. Coordinates are native 1280 × 720 pixels.
export const text=(x,y,w,h,value,size=20,color='#222',weight=400,extra={})=>({kind:'text',x,y,w,h,text:value,size,color,weight,...extra});
export const rect=(x,y,w,h,fill='#f2f3f5',extra={})=>({kind:'rect',x,y,w,h,fill,...extra});
export const ellipse=(x,y,w,h,fill='#e9edf3',extra={})=>({kind:'ellipse',x,y,w,h,fill,...extra});
export const line=(x,y,w,h,color='#ccd1d8',width=1,extra={})=>({kind:'line',x,y,w,h,color,width,...extra});
export const path=(x,y,w,h,d,fill='none',stroke='#222',extra={})=>({kind:'path',x,y,w,h,d,fill,stroke,...extra});
export const icon=(x,y,w,h,name='circle',color='#555',extra={})=>({kind:'icon',x,y,w,h,name,color,...extra});
export const placeholder=(x,y,w,h,extra={})=>({kind:'placeholder',x,y,w,h,fill:'#eeeeef',...extra});
export const group=(x,y,w,h,children,extra={})=>({kind:'group',x,y,w,h,children,...extra});
export const slide=(id,nodes,extra={})=>({id,nodes,bg:'#fff',...extra});
export const card=(x,y,w,h,title,note,extra={})=>group(x,y,w,h,[rect(0,0,w,h,extra.fill||'#f4f5f7',{radius:extra.radius||0}),text(20,18,w-40,36,title,extra.size||22,extra.color||'#222',700),text(20,60,w-40,h-74,note,extra.noteSize||16,extra.noteColor||'#555',400,{lineHeight:1.55})],{element:'card',...extra});

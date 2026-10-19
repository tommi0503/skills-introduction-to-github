// Each slide is serializable data. Coordinates always refer to the 1280×720 canvas.
export const t=(x,y,w,h,text,size=20,color='#222',weight=400,extra={})=>({type:'text',x,y,w,h,text,size,color,weight,...extra});
export const r=(x,y,w,h,fill='#fff',extra={})=>({type:'rect',x,y,w,h,fill,...extra});
export const line=(x,y,w,h,color='#bbb',stroke=1,extra={})=>({type:'line',x,y,w,h,color,stroke,...extra});
export const ph=(x,y,w,h,extra={})=>({type:'placeholder',x,y,w,h,...extra});
export const icon=(x,y,w,h,name='Lightbulb',color='#197c79',extra={})=>({type:'icon',x,y,w,h,name,color,...extra});
export const svg=(x,y,w,h,content,extra={})=>({type:'svg',x,y,w,h,content,...extra});
export const chip=(x,y,w,h,text,fill='#197c79',color='#fff',size=16,extra={})=>({type:'chip',x,y,w,h,text,fill,color,size,...extra});
export const circle=(x,y,d,fill,extra={})=>r(x,y,d,d,fill,{radius:999,...extra});
export function bars(x,y,w,h,values,labels=[],colors=['#197c79'],max=100){const gap=18,bw=(w-gap*(values.length-1))/values.length;return values.flatMap((v,i)=>[r(x+i*(bw+gap),y+h-h*v/max,bw,h*v/max,colors[i%colors.length]),t(x+i*(bw+gap)-10,y+h+8,bw+20,24,labels[i]??'',12,'#555',400,{align:'center'}),t(x+i*(bw+gap)-10,y+h-h*v/max-27,bw+20,25,String(v),14,colors[i%colors.length],700,{align:'center'})]);}
export function donut(x,y,d,value,color='#197c79',bg='#ddd',label=''){return [svg(x,y,d,d,`<circle cx="50" cy="50" r="39" fill="none" stroke="${bg}" stroke-width="15"/><circle cx="50" cy="50" r="39" fill="none" stroke="${color}" stroke-width="15" stroke-dasharray="${value*2.4504} 245.04" transform="rotate(-90 50 50)"/>`,{viewBox:'0 0 100 100'}),t(x,y+d*.31,d,d*.28,`${value}%`,d*.18,color,700,{align:'center'}),t(x,y+d*.6,d,d*.2,label,12,color,400,{align:'center'})];}
export function table(x,y,w,h,rows,{header='#197c79',headInk='#fff',fill='#fff',ink='#333',lineColor='#ccc',size=15,widths}={}){const rh=h/rows.length;return rows.flatMap((row,i)=>{let cursor=x;return row.flatMap((cell,j)=>{const cw=w*(widths?.[j]??1/row.length);const nodes=[r(cursor,y+i*rh,cw,rh,i===0?header:fill,{stroke:lineColor,strokeWidth:1}),t(cursor+7,y+i*rh+3,cw-14,rh-6,String(cell),size,i===0?headInk:ink,i===0?700:400,{align:'center',valign:'middle'})];cursor+=cw;return nodes;});});}

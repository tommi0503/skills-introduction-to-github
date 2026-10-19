// Presentation data is independent of DOM output. Every coordinate uses the 1280x720 canvas.
export const T=(x,y,w,h,text,size=24,color='#17202b',weight=400,opts={})=>({type:'text',x,y,w,h,text,size,color,weight,...opts});
export const R=(x,y,w,h,fill='#fff',radius=0,stroke='none',sw=1,opts={})=>({type:'rect',x,y,w,h,fill,radius,stroke,sw,...opts});
export const C=(x,y,d,fill='#fff',stroke='none',sw=1,opts={})=>R(x,y,d,d,fill,d/2,stroke,sw,opts);
export const L=(x1,y1,x2,y2,color='#ccc',width=1,opts={})=>({type:'line',x:x1,y:y1,w:x2-x1,h:y2-y1,color,width,...opts});
export const PH=(x,y,w,h,radius=0,opts={})=>({type:'placeholder',x,y,w,h,radius,...opts});
export const S=(x,y,w,h,svg,opts={})=>({type:'svg',x,y,w,h,svg,...opts});
export const I=(x,y,size,name,color='#1c3f5b',opts={})=>({type:'icon',x,y,w:size,h:size,name,color,...opts});
export const P=(x,y,w,h,text,fill='#315b96',color='#fff',size=16,opts={})=>({type:'pill',x,y,w,h,text,fill,color,size,radius:h/2,weight:600,...opts});
export const paragraph='핵심 목표와 실행 계획을 명확하게 정리합니다. 주요 성과와 추진 과제를 점검하고 지속 가능한 성장을 위한 방향을 제시합니다.';
export function bullets(x,y,w,lines,size=16,color='#263a4c',gap=32){return lines.map((t,i)=>T(x,y+i*gap,w,gap,'•  '+t,size,color));}
export const slide=(id,title,elements,background='#fff',opts={})=>({id,title,elements:elements.flat(Infinity).filter(Boolean),background,...opts});

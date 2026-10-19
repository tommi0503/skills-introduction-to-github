export function skyline(x,y,w,h,light=false,id='city'){
const white=light?'#465f7e':'#fff',blue=light?'#465f7e':'#7db9ef';let paths='',defs='',ct=0;
function tower(a,b,ww,hh,color,step=11,slant=0,peaked=false,sw=3.2){const num=ct++,key=`${id}-${num}`;defs+=`<linearGradient id="${key}" gradientUnits="userSpaceOnUse" x1="0" y1="${b}" x2="0" y2="${b+hh}"><stop offset="0" stop-color="${color}"/><stop offset=".18" stop-color="${color}"/><stop offset="1" stop-color="${color}" stop-opacity="0"/></linearGradient>`;for(let q=0;q<=ww;q+=step){let top=b+(peaked?-40*(1-Math.abs(q/ww*2-1)):slant*q/ww);paths+=`<path d="M${a+q} ${top}V${b+hh}" stroke="url(#${key})" stroke-width="${sw}"/>`}}
function horiz(a,b,ww,hh,step=12,sw=4){for(let q=0;q<=hh;q+=step)paths+=`<path d="M${a} ${b+q}h${ww}" stroke="${white}" stroke-width="${sw}"/>`}
let vb='0 0 770 345';
if(light){
vb='0 0 290 100';tower(5,91,14,8,white,3.7,0,false,.8);tower(20,59,13,40,white,3.5,0,false,1);tower(59,48,14,51,white,4,0,false,.9);tower(75,19,30,30,white,4,-10,false,1.4);tower(75,48,30,51,white,4,0,false,.9);tower(119,1,40,58,white,4,0,false,1);tower(119,58,32,41,white,4,0,true,.9);tower(168,48,39,51,white,4,0,false,.9);tower(210,8,16,91,white,3.5,0,false,.9);tower(234,19,20,22,white,4,0,false,.9);tower(234,35,20,50,white,4,0,false,.9);tower(251,8,17,41,white,3.5,0,false,.9);tower(271,19,10,31,white,3.5,0,false,.9);
}else if(id==='thanks'){
horiz(11,250,38,89,15,4);tower(92,204,34,130,white,10);tower(93,297,40,37,blue,8,0,false,5);tower(136,235,30,99,white,10);tower(175,175,114,159,white,12);tower(215,89,76,87,blue,12,-28,false,6);tower(327,0,76,181,white,8);tower(365,195,68,139,blue,11,0,true);horiz(280,270,51,66,5,1.5);paths+=`<path d="M337 270v66M343 270v66" stroke="${white}" stroke-width="3"/>`;
}else if(id==='contents'||id==='sidebar'){
vb='0 0 400 325';tower(38,0,70,167,white,7,0,false,2.5);tower(138,60,70,105,blue,10,22,false,5);tower(138,164,102,150,white,11,0,false,2.6);tower(11,184,60,130,blue,10,0,true,3);tower(250,219,24,93,white,8,0,false,2.6);tower(285,192,28,119,white,8,0,false,3);tower(280,278,30,37,blue,7,0,false,4);horiz(351,235,34,81,13,4);horiz(101,256,45,60,5,1.6);paths+=`<path d="M91 256v60M97 256v60" stroke="${white}" stroke-width="2"/>`;
}else{
horiz(11,255,38,89,15,4);tower(57,303,40,41,blue,8,0,false,5);tower(93,208,34,125,white,10);tower(138,238,30,95,white,10);tower(177,178,114,155,white,12);tower(225,93,76,85,blue,12,-28,false,6);tower(331,0,76,181,white,8);tower(331,201,68,137,blue,11,0,true);tower(447,176,98,157,white,11);tower(551,60,44,270,white,8);tower(607,76,44,60,blue,9);tower(621,140,38,196,white,8);tower(665,88,23,150,white,8);tower(681,60,24,150,white,8);tower(706,88,10,140,white,8);tower(670,238,69,95,white,10);horiz(282,278,51,66,5,1.5);paths+=`<path d="M339 278v66M345 278v66" stroke="${white}" stroke-width="3"/>`;horiz(557,289,38,47,9,2);
}
return {type:'svg',x,y,w,h,svg:`<svg viewBox="${vb}" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"><defs>${defs}</defs>${paths}</svg>`}
}
export function richBanner(x,y,w,h,t,accent='#7db9ef'){
const ranges=['매출 XX억 원 돌파 목표 경쟁 심화 속에서 통합 역량 확보가 관건','매출 XX억 원 돌파 목표','맞춤 솔루션 개발과 파트너십 확대로 고객 기반 확장','추천 기능과 실시간 대시보드 개발로 플랫폼 경쟁력 확보','목표 달성을 위한 협업 체계를 구축','주요 전략 과제를 분기별로 단계화','목표 달성 가능성','타겟 고객 확보와 파트너십 체결에 집중','효율적인 의사결정 구조를 확립','인건비 · 개발 · 마케팅 중심으로 총 XX억 원을 효율적으로 배분','4단계 프로세스로 전략 실행 성과를 체계적으로 관리','주요 리스크를 사전에 식별하고 각각의 대응 방안 마련','매출 150억 원 달성 및 시장 Top 3 진입 가능'];
if(w===856)t=t.replace('체계적으로 실행','체계적\n으로 실행');if(w===900)t=t.replace('검증','\n검증');
const escape=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');let lines=t.split('\n'),hlight=ranges.find(r=>t.includes(r)),index=hlight?t.indexOf(hlight):-1;let passed=0;
let text=lines.map((line,i)=>{let parts='';for(let j=0;j<line.length;){let hi=index>=0&&passed+j>=index&&passed+j<index+hlight.length,k=j+1;while(k<line.length&&(index>=0&&passed+k>=index&&passed+k<index+hlight.length)===hi)k++;parts+=`<tspan fill="${hi?accent:'#fff'}" font-weight="${hi?700:400}">${escape(line.slice(j,k))}</tspan>`;j=k}passed+=line.length+1;return `<text x="${w/2}" y="${h/2+(i-(lines.length-1)/2)*28}" dominant-baseline="central" text-anchor="middle" font-family="Pretendard" font-size="21" letter-spacing="-.25">${parts}</text>`}).join('');return {type:'svg',x,y,w,h,svg:`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}">${text}</svg>`}
}

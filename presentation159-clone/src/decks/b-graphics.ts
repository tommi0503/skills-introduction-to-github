import type {Element, SvgShape} from '../model'
import {B,G} from '../primitives'

// Original-sized SVG geometry is kept separate from the slide's content data.
const full=(paths:SvgShape[],extra:Partial<Element>={})=>G(0,0,1600,900,'custom',{viewBox:'0 0 1600 900',paths},extra)
const randomSeries=(seed:number)=>{let value=seed>>>0;return()=>{value=(Math.imul(value,1664525)+1013904223)>>>0;return value/4294967296}}
const ribbon=(d:string,color:string,width:number):SvgShape=>({d,fill:'none',stroke:color,strokeWidth:width,strokeLinecap:'round',strokeLinejoin:'round'})
export function marketingGraphics(variant=1):Element[]{
 const d=variant===1?'M -70 335 C 175 290 110 645 275 645 C 470 650 350 455 370 240 C 386 35 652 17 711 155 C 797 365 624 478 711 751 C 761 924 1011 870 1001 572 C 1012 277 1170 212 1279 386 C 1367 544 1448 592 1662 589':'M -90 292 C 160 275 102 473 280 477 C 472 481 542 343 523 167 C 505 -26 713 -68 789 93 C 882 289 727 387 801 590 C 880 805 1102 671 1138 450 C 1173 216 1434 154 1514 349 C 1592 539 1441 727 1562 937'
 const random=randomSeries(210+variant),flecks=Array.from({length:2200},()=>({cx:random()*1600,cy:random()*900,r:.5+random()*1.8,fill:'#fffff8',opacity:.45+random()*.55}))
 return [B(0,0,1600,900,'#fffff8'),full([ribbon(d,'#edf0eb',168)]),G(0,0,1600,900,'custom',{viewBox:'0 0 1600 900',circles:flecks})]
}
export const aldenaireMark=()=>G(656,88,58,33,'custom',{viewBox:'0 0 58 33',paths:[ribbon('M 8 26 L 21 5','#517d5c',13),ribbon('M 28 26 L 41 5','#44758a',13)],circles:[{cx:51,cy:26,r:6,fill:'#292e29'}]})
export const thynkMark=()=>G(86,57,50,51,'custom',{viewBox:'0 0 50 51',paths:[{d:'M 28 3 C 11 3 3 11 3 25 L 3 37 L 11 37 L 11 24 C 11 15 19 11 28 11Z M 48 16 L 26 16 L 26 24 L 40 24 L 40 33 C 40 41 33 45 24 45 L 3 45 L 3 51 L 27 51 C 40 51 48 43 48 32Z',fill:'#3262f8'}]})
export const paperGrain=()=>G(0,0,1600,900,'grain',{color:'#6b635b',seed:24,frequency:'0.8'},{opacity:.018})
export const burgundy='linear-gradient(120deg,#620d22 0%,#29060d 26%,#000000 47%,#26060d 65%,#680d24 100%)'
export const burgundyPill='linear-gradient(90deg,#580e22 0%,#24080f 45%,#000000 100%)'
export const wavyMark=(x:number,y:number,d:number,color='#242423')=>G(x,y,d,d,'wavy-circle',{color,spacing:d/18,stroke:d/48,amplitude:d/58,period:d/5.7})
export const shareMark=()=>G(1345,642,115,107,'custom',{viewBox:'0 0 110 110',paths:[ribbon('M 28 55 L 72 23 M 28 55 L 72 88','#ffffff',7)],circles:[{cx:28,cy:55,r:14,fill:'#fff'},{cx:72,cy:23,r:14,fill:'#fff'},{cx:72,cy:88,r:14,fill:'#fff'}]})
export function brandGraphics(variant:number):Element[]{
 if(variant===2)return [B(0,0,1600,900,'#d06bc4'),full([ribbon('M -30 -70 C 10 80 -36 244 23 349 C 79 449 187 310 296 328 C 432 351 437 600 565 662 C 695 724 874 574 1044 645 C 1195 707 1188 842 1345 850 C 1482 858 1520 875 1670 900','#dc90d2',104)])]
 if(variant===3)return [B(0,0,1600,900,'#f8eee4'),full([{d:'M 350 0 L 498 0 C 540 25 567 95 585 121 C 602 151 613 116 622 68 C 630 30 642 8 651 0 L 842 0 C 875 25 908 90 932 131 C 958 170 974 147 978 117 C 990 10 1105 14 1117 18 C 1254 28 1431 135 1600 301 L 1600 466 C 1561 481 1541 494 1505 467 C 1437 415 1341 298 1254 249 C 1129 191 1145 218 1173 352 C 1194 459 1111 540 1024 465 C 949 415 864 268 796 230 C 726 174 730 283 749 332 C 777 445 715 508 616 464 C 555 422 508 324 468 270 C 416 211 322 133 289 107 C 254 80 304 18 350 0 Z',fill:'#f3d9df'}])]
 if(variant===7)return [B(0,0,1600,900,'#f8eee4'),full([{d:'M 45 0 L 296 0 C 325 36 350 89 369 105 C 388 127 387 54 407 31 C 420 17 433 9 447 0 L 645 0 C 760 45 877 126 938 193 L 940 350 C 803 307 703 224 649 210 C 537 154 568 291 587 332 C 608 397 568 434 518 441 C 457 446 413 426 388 401 C 337 346 236 207 196 188 C 108 143 165 292 174 341 C 187 413 142 460 92 447 C 43 433 13 421 0 407 L 0 87 C 19 108 30 54 45 0 Z',fill:'#f3d9df'}])]
 return [B(0,0,1600,900,'#f8eee4'),full([ribbon('M 768 -70 C 810 101 936 118 1091 53 C 1261 -20 1352 21 1334 192 C 1316 364 1333 435 1514 385 C 1610 359 1660 365 1690 414','#f3d9df',88),ribbon('M -90 707 C 101 639 255 603 365 692 C 455 765 380 944 440 995','#f3d9df',88)])]
}
export function brandSwirl():Element{
 const d='M 205 500 C 40 466 -45 284 23 142 C 64 51 153 -4 236 0 C 306 1 367 43 375 125 C 384 198 329 257 251 286 C 315 226 330 150 285 110 C 218 51 127 85 91 163 C 45 269 80 417 205 500 Z'
 return G(605,217,499,480,'custom',{viewBox:'0 0 500 500',paths:[{d,fill:'#5e6d47'},{d,fill:'#5e6d47',transform:'rotate(180 250 250)'}]})
}
export function notebookGraphics():Element[]{
 const lines:SvgShape[]=Array.from({length:7},(_,i)=>({d:`M 131 ${260+i*79} Q 460 ${257+i*79} 790 ${260+i*79} T 1449 ${260+i*79}`,fill:'none',stroke:'#c9d7dc',strokeWidth:2}))
 const corners:SvgShape[]=[{d:'M 1350 0 C 1308 64 1480 66 1470 147 C 1465 193 1535 251 1600 246 L 1600 0 Z',fill:'#101b59'},{d:'M 1600 0 L 1600 138 C 1525 164 1489 116 1500 72 C 1516 14 1431 39 1430 0Z',fill:'#a9bed5'},{d:'M 0 552 C 103 550 36 655 144 666 C 214 674 234 806 191 900 L 0 900Z',fill:'#aabed5'},{d:'M 0 688 C 93 681 56 766 150 798 C 208 818 126 887 148 900 L 0 900Z',fill:'#111a54'}]
 return [B(0,0,1600,900,'repeating-linear-gradient(90deg,rgba(136,174,204,.23) 0px,rgba(136,174,204,.23) 40px,transparent 40px,transparent 80px),repeating-linear-gradient(0deg,rgba(146,181,208,.2) 0px,rgba(146,181,208,.2) 54px,transparent 54px,transparent 98px),#e9f0f1'),G(0,0,1600,900,'grain',{color:'#83a9c8',seed:31,frequency:'0.88'},{opacity:.13}),G(0,0,1600,900,'grain',{color:'#ffffff',seed:311,frequency:'0.45 0.9'},{opacity:.42}),G(0,0,1600,900,'grid',{color:'#91a7bd',spacing:2,stroke:.3},{opacity:.15}),full(corners),G(145,171,1340,630,'torn-paper',{color:'#111647',seed:84,spacing:11}),G(120,139,1330,625,'torn-paper',{color:'#ffffff',seed:31,spacing:9}),full(lines),G(353,12,196,188,'custom',{viewBox:'0 0 200 200',paths:[{d:'M 65 96 L 62 57 C 24 35 58 1 105 4 C 145 6 153 42 114 57 L 117 94',fill:'none',stroke:'#131942',strokeWidth:4,strokeLinecap:'round'},{d:'M 24 99 L 156 91 L 196 183 L 4 194 Z',fill:'#151943'}]}),G(177,193,130,141,'scribble-star',{color:'#182158',stroke:2.7}),G(177,193,130,141,'custom',{viewBox:'0 0 100 100',paths:hatchPolygons([[[48,5],[60,35],[94,23],[70,52],[91,80],[58,70],[37,97],[36,63],[5,52],[34,38]]],31)}),G(1200,620,216,126,'scribble-candy',{color:'#182158',stroke:2.7},{rotate:-24}),G(1200,620,216,126,'custom',{viewBox:'0 0 160 90',paths:hatchPolygons([[[42,20],[69,9],[99,15],[118,22],[124,68],[96,84],[65,80],[41,67]],[[43,24],[7,8],[20,43],[3,76],[43,64]],[[120,23],[155,8],[141,43],[157,77],[123,66]]],311)},{rotate:-24})]
}
export const rimGraphics=()=>[B(0,0,1600,900,'radial-gradient(ellipse at 65% 91%,rgba(26,133,58,.62) 0%,transparent 50%),radial-gradient(ellipse at 11% 72%,rgba(19,111,86,.48) 0%,transparent 55%),linear-gradient(113deg,#082b15 0%,#082b1b 100%)'),G(0,0,1600,900,'grain',{color:'#4ca650',seed:32,frequency:'0.8'},{opacity:.2})]
export function workflowGraphics():Element[]{
 const d='M -300 -200 C 400 -400 1060 -250 1300 -50 C 1500 120 1390 320 1060 480 C 820 690 530 760 330 620 C 150 470 -180 40 -300 -200 Z'
 return [B(0,0,1600,900,'radial-gradient(ellipse at 100% 0%,#0021a7 0%,#005fa7 35%,transparent 62%),radial-gradient(ellipse at 0% 100%,#00c270 0%,#006d03 36%,transparent 65%),linear-gradient(130deg,#002600 0%,#008440 45%,#00a7bd 80%,#00a7bd 100%)'),full([ribbon('M 1300 -100 C 1500 120 1390 320 1060 480 C 820 690 530 760 330 620','#0018b7',170)],{filter:'blur(38px)'}),full([{d,fill:'#000604'}],{filter:'blur(42px)'})]
}
export const workflowMark=()=>G(1380,769,45,44,'custom',{viewBox:'0 0 45 44',paths:[{d:'M 12 1 L 24 8 L 24 21 L 12 28 L 0 21 L 0 8Z M 33 1 L 45 8 L 45 21 L 33 28 L 21 21 L 21 8Z M 23 16 L 35 23 L 35 36 L 23 43 L 11 36 L 11 23Z',fill:'#5fe150'},{d:'M 12 14 L 12 28 M 0 8 L 12 14 L 24 8 M 33 14 L 33 28 M 21 8 L 33 14 L 45 8 M 23 29 L 23 43 M 11 23 L 23 29 L 35 23',stroke:'#0d4835',strokeWidth:1.2}]})
export function annualGraphics(variant=1):Element[]{
 if(variant===1)return [B(0,0,1600,900,'#fff'),G(162,44,1276,856,'grid',{color:'#eeeeee',spacing:116,stroke:1.5}),B(0,623,925,277,'radial-gradient(ellipse at 29% 88%,rgba(245,115,84,.76) 0%,rgba(242,137,135,.31) 30%,transparent 56%),radial-gradient(ellipse at 66% 43%,rgba(241,122,73,.77) 0%,rgba(236,138,145,.31) 27%,transparent 54%)'),G(0,622,925,278,'grain',{color:'#e67157',seed:37,frequency:'0.9'},{opacity:.08,mask:'linear-gradient(0deg,#000000,transparent)'})]
 return [B(0,0,1600,900,'#fff'),B(782,58,800,789,'radial-gradient(ellipse at 40% 26%,rgba(221,149,211,.48) 0%,transparent 32%),radial-gradient(ellipse at 25% 43%,rgba(244,175,80,.79) 0%,transparent 38%),radial-gradient(ellipse at 75% 27%,rgba(245,199,117,.77) 0%,transparent 38%),radial-gradient(ellipse at 50% 66%,rgba(221,154,213,.5) 0%,transparent 24%),radial-gradient(ellipse at 74% 79%,rgba(243,174,81,.75) 0%,transparent 35%)',{mask:'radial-gradient(ellipse at 49% 48%,#000 35%,transparent 72%)'}),G(796,75,776,754,'grain',{color:'#ecc276',seed:3710,frequency:'0.9'},{opacity:.08,mask:'radial-gradient(ellipse,#000 20%,transparent 69%)'})]
}
export const annualFlower=()=>G(86,725,88,88,'custom',{viewBox:'0 0 88 88',paths:Array.from({length:10},(_,i)=>({d:'M 44 43 L 44 9',stroke:'#ed6c4e',strokeWidth:11,strokeLinecap:'round',transform:`rotate(${i*36} 44 44)`}))})

export function traitMark(x:number,y:number,name:string):Element {
 const color='#a0c028'
 if(name==='Flower')return G(x,y,32,32,'custom',{viewBox:'0 0 32 32',paths:Array.from({length:8},(_,i)=>({d:'M 16 16 C 12 13 12 3 16 2 C 20 3 20 13 16 16Z',fill:color,transform:`rotate(${i*45} 16 16)`}))})
 if(name==='Sparkles')return G(x,y,32,32,'custom',{viewBox:'0 0 32 32',paths:[{d:'M16 1 C18 12 20 14 31 16 C20 18 18 20 16 31 C14 20 12 18 1 16 C12 14 14 12 16 1Z',fill:color}]})
 if(name==='Asterisk')return G(x,y,32,32,'custom',{viewBox:'0 0 32 32',paths:Array.from({length:8},(_,i)=>({d:'M16 2 L16 30',stroke:color,strokeWidth:2.3,transform:`rotate(${i*22.5} 16 16)`}))})
 return G(x,y,32,32,'custom',{viewBox:'0 0 32 32',rects:[{x:1,y:7,width:7,height:8,fill:color},{x:13,y:7,width:7,height:8,fill:color},{x:25,y:7,width:7,height:8,fill:color},{x:7,y:16,width:7,height:8,fill:color},{x:19,y:16,width:7,height:8,fill:color}]})
}

function hatchPolygons(polygons:number[][][],seed:number):SvgShape[]{
 const random=randomSeries(seed),paths:SvgShape[]=[]
 const inside=(x:number,y:number,points:number[][])=>{let yes=false;for(let i=0,j=points.length-1;i<points.length;j=i++){const a=points[i],b=points[j];if((a[1]>y)!==(b[1]>y)&&x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0])yes=!yes}return yes}
 for(const polygon of polygons){
  const maxX=Math.max(...polygon.map(point=>point[0])),maxY=Math.max(...polygon.map(point=>point[1]))
  for(let y=1;y<maxY;y+=4)for(let x=1;x<maxX;x+=3.4){
   const startX=x+random()*2,startY=y+random()*2
   if(!inside(startX,startY,polygon))continue
   let length=1;while(length<13&&inside(startX+length*.28,startY-length,polygon))length++
   paths.push({d:`M ${startX.toFixed(1)} ${startY.toFixed(1)} L ${(startX+length*.28).toFixed(1)} ${(startY-length).toFixed(1)}`,stroke:'#182158',strokeWidth:.7+random()*.7,opacity:.72+random()*.28,strokeLinecap:'round'})
  }
 }
 return paths
}

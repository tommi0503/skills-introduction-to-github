import {useId} from 'react'
import {Image,Lightbulb} from 'lucide-react'
import type {GraphicScenes,GraphicProps} from './types'
import {WorldLand,worldLandPath} from './world-land'
import {germanyStates} from './germany-states'

// Every scene uses local SVG definitions: individual slides are independent DOM trees.
function Sphere({variant='2-0'}:GraphicProps){
 const id=useId().replace(/:/g,'');const [preview,index]=variant.split('-').map(Number);const v=index+(preview===3?9:0);
 const paint=(name:string)=>`url(#${id}-${name})`;
 const white=paint('white'),blue=paint('blue'),gold=paint('gold'),cream=paint('cream'),gray=paint('gray'),brown=paint('brown');
 const dome=(fill:string)=> <path d="M35 250A215 215 0 0 1 465 250A215 215 0 0 1 35 250Z" fill={fill}/>;
 const cut=(mode:number)=> {const originalBlue=mode===0||v===4;const outer=originalBlue?blue:gray,middle=originalBlue?gold:cream,inner=originalBlue?cream:gold,core=originalBlue?white:blue;return <>
  {dome(white)}
  <path d={mode===1?'M102 311Q83 140 198 37Q302 5 338 152L322 274Z':'M120 282Q124 80 250 25Q365 74 405 232L283 324Z'} fill={outer}/>
  <path d={mode===1?'M135 299Q139 131 225 70Q297 48 321 170L306 274Z':'M156 285Q153 126 251 61Q346 109 365 245L283 315Z'} fill={middle}/>
  <path d={mode===1?'M170 286Q168 164 246 122Q291 102 302 190L291 271Z':'M190 287Q190 160 251 110Q316 148 328 255L282 307Z'} fill={inner}/>
  <path d={mode===1?'M205 278Q195 203 260 166Q295 156 290 225L280 270Z':'M221 292Q220 207 254 166Q292 195 297 270L280 299Z'} fill={core}/>
  <path d="M120 282Q213 324 412 232Q472 248 439 291Q316 376 120 325Z" fill={outer}/>
  <path d="M154 285Q241 317 382 243Q422 254 402 282Q285 345 154 314Z" fill={middle}/>
  <path d="M190 287Q254 315 345 257Q373 270 350 289Q282 324 190 308Z" fill={inner}/>
  <path d="M221 292Q265 306 307 273Q332 289 303 300Q258 315 221 303Z" fill={core}/>
  <path d="M120 325Q294 392 439 291Q441 435 299 470Q160 449 120 325Z" fill={white}/>
 </>};
 const quarters=(separate=true)=> <>
  <path d="M246 25Q67 37 26 236Q99 282 207 270L244 247Z" fill={blue}/><path d="M246 25L244 247L207 270L216 96Z" fill="#294c5f"/>
  <path d="M266 25Q449 36 475 234Q394 275 258 267L266 25Z" fill={gold}/>
  <path d={`M26 ${separate?273:253}Q97 251 213 285L245 306Q235 403 245 476Q58 452 26 ${separate?273:253}Z`} fill={gray}/>
  <path d="M213 285L245 306Q235 403 245 476Q218 469 213 443Z" fill="#aaa"/>
  <path d={`M264 ${separate?289:271}Q380 291 475 ${separate?272:253}Q446 458 268 477Q246 397 264 ${separate?289:271}Z`} fill={cream}/>
  {separate&&<><ellipse cx="130" cy="277" rx="104" ry="23" fill="#777"/><ellipse cx="369" cy="276" rx="106" ry="24" fill="#947834"/></>}
 </>;
 const exploded=(diagonal=false,reverse=false,alternate=false)=> <g transform={diagonal?`rotate(${reverse?32:-35} 250 250)`:undefined}>
  <path d="M73 79Q244-31 427 80L73 79Z" fill={alternate?blue:white}/><ellipse cx="250" cy="80" rx="177" ry="23" fill={alternate?'#284a5e':'#777'}/>
  <path d="M48 126Q243 88 450 124L470 212Q241 229 28 211Z" fill={alternate?gold:cream}/><ellipse cx="250" cy="212" rx="220" ry="18" fill="#998043"/>
  <path d="M28 250Q240 243 470 250Q462 300 439 344Q236 356 54 343Z" fill={alternate?cream:gold}/>
  <path d="M68 383Q250 409 431 382Q374 478 250 480Q123 477 68 383Z" fill={alternate?white:blue}/><ellipse cx="250" cy="383" rx="180" ry="23" fill={alternate?'#dedede':'#284a5e'} stroke="#f8f8f8" strokeWidth="3"/>
 </g>;
 const orbital=(mode:number)=> <>
  {dome(white)}
  <path d={mode===0?'M263 21Q93 28 41 181Q-23 367 177 461Q259 493 328 458Q123 378 138 193Q146 54 263 21Z':'M209 26Q54 65 34 233Q15 400 191 468Q296 499 398 435Q163 479 127 317Q87 134 209 26Z'} fill={blue}/>
  <path d="M207 27Q106 79 141 269Q168 417 324 459Q209 437 185 254Q169 91 207 27Z" fill="#294c5f"/>
  <path d={mode===0?'M284 47Q399 111 438 263Q422 359 339 404L238 392Q370 279 350 166Q336 81 284 47Z':'M336 49Q424 115 464 258Q443 379 325 425L237 382Q384 268 382 143Q379 86 336 49Z'} fill={gold}/>
  <path d="M337 53Q385 73 382 143Q381 290 237 382L249 405Q410 279 407 139Q401 87 337 53Z" fill="#a08332"/>
  <path d="M131 121Q275 25 381 112L379 158Q236 98 142 161Z" fill={cream}/>
  <path d="M140 145Q268 81 381 133L379 158Q236 98 142 161Z" fill="#b4a05b"/>
 </>;
 const eggCut=()=> <>
  {dome(white)}<path d="M246 26Q355 38 415 137L85 137Q159 39 246 26Z" fill={brown}/>
  <path d="M85 137L415 137Q440 191 450 221L50 221Q58 174 85 137Z" fill={gray}/>
  <path d="M50 221L450 221Q454 267 447 302L52 302Q43 258 50 221Z" fill={cream}/>
  <path d="M52 302L447 302Q438 366 402 394L99 394Q67 355 52 302Z" fill={gold}/>
  <path d="M99 394L402 394Q340 460 250 475Q162 447 99 394Z" fill={blue}/>
  <path d="M250 25Q95 132 118 312Q141 428 250 475Q38 468 35 250Q41 39 250 25Z" fill={white}/>
  <path d="M250 25Q405 132 382 312Q359 428 250 475Q462 468 465 250Q459 39 250 25Z" fill={white}/>
  <path d="M250 26L250 475" stroke="#ffffff" opacity=".3" strokeWidth="2"/>
 </>;
 let art;
 if(v===0)art=exploded();
 else if(v===1)art=quarters();
 else if(v===2)art=cut(0);
 else if(v===4)art=<>{dome(white)}<path d="M95 285C95 145 155 25 250 25C345 25 405 145 405 285Q250 311 95 285Z" fill={blue}/><path d="M131 284C131 172 184 74 250 74C316 74 369 172 369 284Q250 303 131 284Z" fill={gold}/><path d="M166 283C166 205 204 123 250 123C296 123 334 205 334 283Q250 297 166 283Z" fill={cream}/><path d="M203 282C203 236 226 179 250 179C274 179 297 236 297 282Q250 290 203 282Z" fill={white}/></>;
 else if(v===3)art=<g transform="rotate(9 250 250)">{dome(white)}<path d="M63 71Q227 123 438 71L466 163Q255 218 36 163Z" fill={blue}/><path d="M36 163Q255 218 466 163L451 269Q251 326 53 269Z" fill={gold}/><path d="M53 269Q251 326 451 269L398 390Q243 434 103 390Z" fill={cream}/></g>;
 else if(v===5)art=<>{dome(white)}<path d="M97 93Q137 25 250 25Q363 25 403 93L394 111Q363 64 324 67Q306 76 300 105Q300 166 250 169Q200 166 200 105Q194 76 176 67Q137 64 106 111Z" fill={blue}/><path d="M61 184Q25 268 59 357Q114 455 214 475Q177 432 164 406Q157 395 176 377Q203 355 193 329Q186 305 155 307Q126 311 97 284Q61 254 61 184Z" fill={gold}/><path d="M439 184Q475 268 441 357Q386 455 286 475Q323 432 336 406Q343 395 324 377Q297 355 307 329Q314 305 345 307Q374 311 403 284Q439 254 439 184Z" fill={gold}/><Image x={235} y={91} width={30} height={30} color="#fff" strokeWidth={1.6}/><Image x={109} y={329} width={30} height={30} color="#fff" strokeWidth={1.6}/><Image x={360} y={329} width={30} height={30} color="#fff" strokeWidth={1.6}/></>;
 else if(v===6)art=<g transform="rotate(-31 250 250)"><path d="M99 21Q244-35 402 27L432 66Q257 100 69 63Z" fill={blue}/><path d="M62 112Q250 65 439 112L455 158Q250 203 44 158Z" fill={gold}/><path d="M34 204Q250 165 467 204L474 250Q250 288 27 250Z" fill={cream}/><path d="M28 300Q250 277 473 300L455 345Q250 377 46 345Z" fill={white}/><path d="M62 391Q250 380 437 391L405 432Q250 466 94 432Z" fill={gray}/><path d="M118 468Q250 450 382 468Q328 510 250 512Q171 510 118 468Z" fill={brown}/></g>;
 else if(v===7)art=exploded(true,true,true);
 else if(v===8)art=eggCut();
 else if(v===9)art=<>{dome(white)}<path d="M227 22Q36 45 31 239Q21 437 226 477Q125 336 133 204Q137 85 227 22Z" fill={gold}/><path d="M227 22Q157 120 174 302Q185 426 226 477L253 463Q198 338 187 206Q178 92 253 35Z" fill="#9d7f31"/><path d="M244 50Q381 19 445 201L418 232Q364 90 255 90Z" fill={blue}/><path d="M207 295Q352 268 457 210Q468 385 290 455Q239 448 207 295Z" fill={cream}/><path d="M207 295Q352 268 457 210L454 244Q337 301 214 322Z" fill="#b5a16e"/></>;
 else if(v===10)art=cut(1);
 else if(v===11)art=<g transform="rotate(22 250 250)"><path d="M99 21Q244-35 402 27L432 66Q257 100 69 63Z" fill={brown}/><path d="M62 112Q250 65 439 112L455 158Q250 203 44 158Z" fill={brown}/><path d="M34 204Q250 165 467 204L474 250Q250 288 27 250Z" fill={white}/><path d="M28 300Q250 277 473 300L455 345Q250 377 46 345Z" fill={cream}/><path d="M62 391Q250 380 437 391L405 432Q250 466 94 432Z" fill={gold}/><path d="M118 468Q250 450 382 468Q328 510 250 512Q171 510 118 468Z" fill={blue}/></g>;
 else if(v===12)art=quarters(false);
 else if(v===13)art=orbital(1);
 else if(v===14)art=exploded(true,true,true);
 else if(v===15)art=<>{dome(gray)}<path d="M250 25A215 215 0 0 1 250 475Q178 250 250 25Z" fill={white}/><path d="M250 71Q418 85 425 250Q413 419 250 428Q198 252 250 71Z" fill={cream}/><path d="M250 142Q345 145 352 250Q344 351 250 358Q221 252 250 142Z" fill={gold}/><ellipse cx="251" cy="252" rx="20" ry="28" fill={blue}/><path d="M250 25Q178 250 250 475" fill="none" stroke="#777" strokeWidth="4"/></>;
 else if(v===16)art=<>{dome(white)}<path d="M227 22Q36 45 31 239Q21 437 226 477Q125 336 133 204Q137 85 227 22Z" fill={gray}/><path d="M244 50Q381 19 445 201L418 232Q364 90 255 90Z" fill={cream}/><path d="M244 96Q357 80 416 225L217 318Z" fill={blue}/><path d="M207 295Q352 268 457 210Q468 385 290 455Q239 448 207 295Z" fill={gold}/><path d="M207 295Q352 268 457 210L454 244Q337 301 214 322Z" fill="#b39b5e"/></>;
 else art=<>{dome(gray)}<path d="M250 25Q96 34 38 241Q39 420 250 475Q83 239 250 25Z" fill={blue}/><path d="M250 25Q86 245 250 475L282 475Q198 226 282 27Z" fill={gold}/><path d="M282 27Q373 52 375 250Q367 410 282 475L250 475L250 25Z" fill={cream}/><ellipse cx="250" cy="251" rx="213" ry="31" fill="#fff"/><path d="M38 251Q246 306 463 251" fill="none" stroke="#bababa" strokeWidth="9" opacity=".6"/></>;
 return <svg width="100%" height="100%" viewBox={(["28 24 442 456","26 25 449 452","35 25 430 450","35 25 430 450","35 25 430 450","35 25 430 450","9 -5 481 535","9 5 481 490","35 25 430 450","31 22 437 455","35 25 430 450","9 -5 481 535","26 25 449 451","34 26 430 450","9 5 481 490","35 25 430 450","35 25 430 450","35 25 430 450"])[v]} aria-hidden="true"><defs>
  {[['white','#fff','#f1f1f1','#dcdcdc'],['blue','#678a9f','#486b83','#254a60'],['gold','#d4be80','#c3a85d','#a28536'],['cream','#f1e6cf','#e0d3b3','#c6b58e'],['gray','#eee','#d7d7d7','#a4a4a4'],['brown','#b39d92','#937e74','#73615a']].map(([name,a,b,c])=><radialGradient key={name} id={`${id}-${name}`} cx="36%" cy="26%" r="80%"><stop offset="0" stopColor={a}/><stop offset=".6" stopColor={b}/><stop offset="1" stopColor={c}/></radialGradient>)}
 </defs>{art}</svg>
}

type SphereDecoration={ring?:[number,number,number];plane?:[number,number,number];wave?:[number,number];dots?:[number,number];arrow?:[number,number];blob:number};
// Original-specific placements measured against each native sheet cell, in 1600×900 coordinates.
const sphereDecorations:SphereDecoration[]=[
 {ring:[1270,24,30],plane:[1503,405,0],wave:[449,802],blob:0},
 {ring:[1250,150,30],plane:[15,180,0],blob:1},
 {ring:[460,665,30],arrow:[1350,60],blob:2},
 {ring:[0,535,30],plane:[1200,55,0],wave:[865,780],blob:3},
 {ring:[1340,805,30],dots:[300,160],arrow:[1350,-30],blob:4},
 {ring:[1280,93,30],plane:[90,204,0],blob:5},
 {ring:[1250,200,30],dots:[380,65],blob:6},
 {blob:7},
 {ring:[110,105,30],blob:8},
 {ring:[0,535,30],plane:[1200,55,0],wave:[865,780],blob:3},
 {ring:[120,0,30],dots:[1440,210],blob:9},
 {ring:[1510,640,30],plane:[1280,80,0],blob:10},
 {ring:[0,535,30],plane:[1200,55,0],wave:[865,780],blob:3},
 {ring:[1280,93,30],plane:[90,204,0],blob:5},
 {ring:[1340,805,30],dots:[300,160],arrow:[1350,-30],blob:4},
 {plane:[330,240,0],dots:[1340,690],blob:11},
 {ring:[1500,650,30],dots:[1360,55],blob:12},
 {ring:[0,535,30],plane:[1200,55,0],wave:[865,780],blob:3},
];
function SphereBackground({variant='2-0'}:GraphicProps){const [pre,index]=variant.split('-').map(Number);const spec=sphereDecorations[index+(pre===3?9:0)];const id=useId().replace(/:/g,'');const soft=['M0 12C145-18 160 141 346 111C494 88 537 210 471 321C345 397 140 461 0 605Z','M0 687C215 520 289 553 431 726C609 936 274 936 0 900Z','M828 0C938 54 1044 365 1282 311C1488 261 1432 76 1600 155L1600 0Z','M0 27C210 63 233 304 470 217C671 142 867-5 960 0Z','M0 0C10 135 83 224 225 177C311 148 383 156 439 321C420 447 193 556 0 655Z','M1122 900C1056 653 1113 439 1321 440C1425 439 1493 363 1600 420L1600 900Z','M0 657C103 550 360 431 497 559C712 846 456 900 0 900Z','M0 0H1600V900H0Z','M1034 0C1079 181 1160 309 1318 264C1447 231 1550 271 1600 377L1600 0Z','M0 0C45 211 237 265 373 327C541 405 517 591 223 525C133 471 32 410 0 485Z','M0 0C223-10 304 54 495 178C670 231 728 223 867 0Z','M0 526C193 439 278 715 548 705C713 712 458 900 0 900Z','M963 0C1088 94 1188 380 1447 294C1543 267 1567 311 1600 363L1600 0Z'];
 return <svg width="100%" height="100%" viewBox="0 0 1600 900" aria-hidden="true"><defs><radialGradient id={id}><stop offset="0" stopColor="#fff"/><stop offset=".78" stopColor="#fff"/><stop offset="1" stopColor={spec.blob===7?'#eee':'#fafafa'}/></radialGradient></defs><rect width="1600" height="900" fill={`url(#${id})`}/><path d={soft[spec.blob]} fill={spec.blob===7?'#fff':'#f5f5f5'} opacity=".75"/>
 {spec.blob!==7&&<path d={spec.blob===0?'M1220 0C1068 205 1270 292 1484 186L1600 89V0Z':spec.blob===1?'M828 900C687 736 950 580 1184 754C1394 953 1224 923 828 900Z':spec.blob===5?'M1083 900C1050 682 1209 479 1467 587L1600 721V900Z':'M0 800C188 636 361 721 422 900H0Z'} fill="#f7f4e8" opacity=".48"/>}
 {spec.ring&&<g transform={`translate(${spec.ring[0]} ${spec.ring[1]}) rotate(${spec.ring[2]})`} stroke="#333" strokeWidth="3" fill="none">{Array.from({length:11},(_,n)=><ellipse key={n} cx={n%4*37} cy={Math.floor(n/4)*42} rx={n%3?4:5} ry={n%3?14:11}/>)}</g>}
 {spec.plane&&(variant==='2-1'?<g transform="translate(0 175)" fill="none" stroke="#333" strokeWidth="3"><path d="M42 17Q-40-24-9 33Q33 61 24 27Q17 8 42 17"/><path d="M70 6L240 85L109 101L96 65L70 6M70 6L138 75L240 85M96 65L138 75L109 101"/></g>:<g transform={`translate(${spec.plane[0]} ${spec.plane[1]}) rotate(${spec.plane[2]})`} fill="none" stroke="#333" strokeWidth="3"><path d="M75 0Q120 30 91 55Q51 77 55 35Q89 18 96 59"/><path d="M96 59L8 46L38 88L63 78L48 132L111 66L96 59M8 46L63 78L111 66M38 88L63 78M48 132L63 78"/></g>)}
 {spec.wave&&<g transform={`translate(${spec.wave[0]} ${spec.wave[1]})`} fill="none" stroke="#333" strokeWidth="3"><path d="M0 9Q108-29 160 37Q215 115 282 112M31 31Q121-10 158 56Q181 105 227 110M62 51Q118 19 167 105"/></g>}
 {variant==='2-6'&&<g color="#b9b9b9" opacity=".4"><Lightbulb x={350} y={60} width={40} height={40} strokeWidth={1.5}/><Lightbulb x={396} y={100} width={32} height={32} strokeWidth={1.5}/></g>}{variant==='3-1'&&<g transform="translate(1440 150) rotate(25)" fill="none" stroke="#333" strokeWidth="3">{Array.from({length:4},(_,i)=><path key={i} d={`M${i*17} 0V78M-10 ${i*21+5}H65`}/>)}</g>}{spec.dots&&variant!=='2-6'&&variant!=='3-1'&&<g transform={`translate(${spec.dots[0]} ${spec.dots[1]})`} fill="#333">{Array.from({length:9},(_,i)=><circle key={i} cx={i%3*20} cy={Math.floor(i/3)*20} r="2.2"/>)}</g>}
 {spec.arrow&&<path transform={`translate(${spec.arrow[0]} ${spec.arrow[1]})`} d="M0 0Q99 79 1 114Q-31 139 40 169M0 0Q57 36 100 30M0 0Q9 49-25 68" fill="none" stroke="#333" strokeWidth="3"/>}
 </svg>}
function FilledLeaf({colors=['#fff']}:GraphicProps){return <svg width="100%" height="100%" viewBox="0 0 100 100" aria-hidden="true"><path d="M83 10Q23-2 19 44Q16 76 46 81Q75 85 83 10Z" fill={colors[0]}/><path d="M21 92Q40 56 69 30" fill="none" stroke={colors[0]} strokeWidth="7" strokeLinecap="round"/></svg>}
function Radiation({colors=['#006675']}:GraphicProps){return <svg width="100%" height="100%" viewBox="0 0 300 300" aria-hidden="true"><g fill="none" stroke={colors[0]} strokeWidth="3"><circle cx="150" cy="150" r="131"/><circle cx="150" cy="150" r="25"/>{[0,120,240].map(a=><path key={a} transform={`rotate(${a} 150 150)`} d="M123 105L88 45A122 122 0 0 1 212 45L177 105A52 52 0 0 0 123 105Z"/>)}</g></svg>}
function EcoMap({colors=['#999'],variant}:GraphicProps){return <WorldLand fill={colors[0]} stroke={variant==='outline'?colors[1]??'#666':undefined} strokeWidth={variant==='outline'?1:0}/>}
function EcoGlobe({colors=['#006675','#fff'],variant}:GraphicProps){const id=useId().replace(/:/g,'');return <svg width="100%" height="100%" viewBox="0 0 500 500" aria-hidden="true"><defs><clipPath id={`${id}-clip`}><circle cx="250" cy="250" r="238"/></clipPath><radialGradient id={`${id}-shade`} cx="36%" cy="28%" r="80%"><stop offset="0" stopColor={colors[0]}/><stop offset="1" stopColor={colors[2]??'#004550'}/></radialGradient></defs><circle cx="250" cy="250" r="238" fill={`url(#${id}-shade)`}/><g clipPath={`url(#${id}-clip)`}><path d={worldLandPath} transform={variant==='asia'?'translate(-410 48) scale(1.1 .96)':'translate(-165 52) scale(.94 .96)'} fill={colors[1]??'#fff'}/></g></svg>}
function Germany({colors=['#f69b06','#c64132','#d5d5d5']}:GraphicProps){const red=['DE-TH','DE-SN','DE-BB'];const gray=['DE-MV','DE-SH','DE-HB','DE-HE','DE-ST','DE-BE'];return <svg width="100%" height="100%" viewBox="0 0 640 500" aria-hidden="true"><g transform="scale(1.73 1)">{germanyStates.map(state=><path key={state.id} d={state.path} fill={red.includes(state.id)?colors[1]:gray.includes(state.id)?colors[2]:colors[0]} stroke="#fff" strokeWidth="2" strokeLinejoin="round"/>)}</g></svg>}
function LegalContours({variant}:GraphicProps){return <svg width="100%" height="100%" viewBox="0 0 1600 900" aria-hidden="true"><g fill="none" stroke={variant==='dark'?'#b5b390':'#d4c9a6'} strokeWidth="1" opacity={variant==='dark'?.05:.17}>{Array.from({length:165},(_,i)=>{const pts=Array.from({length:81},(_,j)=>{const y=j*12,x=i*11+35*Math.sin(y/95+i/15)+65*Math.sin(y/190-i/14);return `${j?'L':'M'}${x.toFixed(2)},${y}`}).join('');return <path key={i} d={pts}/>})}</g></svg>}
function MaxxBackground({variant='poster'}:GraphicProps){const id=useId().replace(/:/g,'');const palettes:Record<string,string[]>={cover:['#302d2c','#221f20'],coverblue:['#1554a7','#0665fa'],contents:['#32312e','#41403d'],'section:1':['#0066ff','#1451a4'],'section:2':['#b3a05a','#ffe36e'],'section:3':['#8165f3','#5845a5'],'section:4':['#b9f38a','#80a761'],'section:5':['#aeaeac','#fcfcfa'],online:['#454542','#262624'],welcome:['#cce0ff','#c7d9f2'],about:['#d4ccb2','#a7a38f'],primary2:['#fffbe9','#d7d0b4'],primary3:['#d0e5ff','#93a1b5'],web:['#b2b2b2','#fff'],post:['#aaa','#eee'],logo:['#b1b1b1','#e2e2e2'],imagery:['#aaa','#fff'],imagery2:['#aaa','#e0e0e0'],colors:['#aaa','#c3c3c3'],photo:['#eeeeec','#fff'],letter:['#b0b0b0','#d9d9d9'],primary:['#aaa','#c8c8c8'],clear:['#fafafa','#fff'],primarycolors:['#f8f8f8','#e7e7e7']};const tones=palettes[variant]??['#fff','#b5b5b3'];const reverse=['web','post','logo','imagery','imagery2','primary3','letter','primary','colors','primary2'].includes(variant);return <svg width="100%" height="100%" viewBox="0 0 1600 900" aria-hidden="true"><defs><linearGradient id={`${id}-linear`} x1="0" y1="0" x2="1" y2=".55"><stop offset="0" stopColor={tones[0]}/><stop offset=".74" stopColor={tones[1]}/><stop offset="1" stopColor={tones[1]}/></linearGradient><radialGradient id={`${id}-spot`} cx={reverse?'88%':'12%'} cy={variant==='web2'?'25%':'85%'} r="60%"><stop offset="0" stopColor={variant==='primary2'?'#fffce9':'#fff'} stopOpacity={variant.startsWith('section')||['cover','coverblue','contents','online'].includes(variant)?0:.86}/><stop offset="1" stopColor="#fff" stopOpacity="0"/></radialGradient></defs><rect width="1600" height="900" fill={`url(#${id}-linear)`}/><rect width="1600" height="900" fill={`url(#${id}-spot)`}/></svg>}
function BrandBag(){const id=useId().replace(/:/g,'');return <svg width="100%" height="100%" viewBox="0 0 480 490" aria-hidden="true"><defs><linearGradient id={id} x1="0" x2="1"><stop stopColor="#0869ff"/><stop offset=".77" stopColor="#0062ff"/><stop offset="1" stopColor="#0348b7"/></linearGradient></defs><path d="M173 171Q175 23 240 20Q305 19 309 172" fill="none" stroke="#004db9" strokeWidth="19"/><path d="M176 169Q179 24 241 20Q302 20 306 169" fill="none" stroke="#0b69fa" strokeWidth="8"/><path d="M33 174H461V485H40Z" fill="#000" opacity=".08"/><path d="M15 165H450V480H15Z" fill={`url(#${id})`}/><path d="M450 165L464 176V470L450 480Z" fill="#0041b0"/><path d="M15 165H450" stroke="#3083ff" strokeWidth="2"/></svg>}
function EcoBulb({colors=['#569ca2','#84b4b9']}:GraphicProps){return <svg width="100%" height="100%" viewBox="0 0 420 650" aria-hidden="true"><path d="M115 20C15 28 53 76 160 61C236 47 266 76 135 101C21 125 50 160 179 147C301 131 322 168 143 189C13 203 37 245 180 230C301 217 287 262 143 279C52 290 72 327 202 316C321 305 294 348 157 363C60 374 61 410 204 400C298 395 297 436 263 484L249 541H146L133 483C76 462 52 432 71 390C27 370 22 342 58 317C3 293 25 262 58 244C10 207 35 178 55 159C17 129 30 101 55 84C5 45 47 14 115 20Z" fill={colors[0]} opacity=".65"/><path d="M97 40Q233-1 222 47Q184 66 89 75M84 111Q314 56 260 107Q229 135 81 154M86 191Q324 133 269 188Q212 220 87 233M115 285Q303 234 269 283Q221 311 107 326M127 375Q289 342 267 389Q223 416 137 424" stroke={colors[1]} strokeWidth="28" fill="none" strokeLinecap="round"/><path d="M146 537H248L242 576H153Z" fill={colors[0]}/>{Array.from({length:7},(_,i)=><path key={i} d={`M147 ${540+i*7}H247`} stroke={colors[1]} strokeWidth="3"/>)}<path d="M170 590H225L214 612H181Z" fill={colors[0]}/></svg>}
function EcoLeaves(){const id=useId().replace(/:/g,'');return <svg width="100%" height="100%" viewBox="0 0 1600 696" aria-hidden="true"><defs><linearGradient id={id} x2=".7" y2="1"><stop stopColor="#43978c"/><stop offset="1" stopColor="#005e65"/></linearGradient></defs><rect width="1600" height="696" fill={`url(#${id})`}/>{Array.from({length:100},(_,i)=>{const x=i%14*125+(i%3)*17-35,y=Math.floor(i/14)*112-40,a=(i*73)%360;return <g key={i} transform={`translate(${x} ${y}) rotate(${a})`} opacity={.08+(i%4)*.022}><path d="M0-55Q82-38 47 35Q12 68 0 55Q-53 45-48-2Q-46-38 0-55Z" fill="#b8d9bb"/><path d="M0-47V48M0-27L29-9M0-6L-32-17M0 17L22 29" stroke="#246761" fill="none" strokeWidth="3"/></g>})}</svg>}
function EcoDroplets(){return <svg width="100%" height="100%" viewBox="0 0 1600 900" aria-hidden="true"><g fill="#95b3b0" opacity=".08">{Array.from({length:120},(_,i)=>{const x=150+i%16*86+(i%3)*17,y=65+Math.floor(i/16)*107,d=4+i%5*3;return <path key={i} d={`M${x} ${y-d}Q${x+d*2} ${y+d} ${x+d} ${y+d*2}Q${x} ${y+d*3} ${x-d} ${y+d*2}Q${x-d*2} ${y+d} ${x} ${y-d}Z`}/>})}</g></svg>}

const scenes:GraphicScenes={'c-brand-bag':BrandBag,'c-eco-bulb':EcoBulb,'c-eco-leaves':EcoLeaves,'c-eco-droplet-pattern':EcoDroplets,'c-sphere':Sphere,'c-sphere-background':SphereBackground,'c-leaf':FilledLeaf,'c-radiation':Radiation,'c-eco-map':EcoMap,'c-eco-globe':EcoGlobe,'c-germany':Germany,'c-legal-contours':LegalContours,'c-maxx-background':MaxxBackground}
export default scenes

import {T,B,P,L,C,I,V,S,D} from '../primitives.mjs';
const bg='#0a0a0a', white='#ffffff', lime='#bdd022';
const tx=(x,y,w,h,text,size=18,color=white,extra={})=>T(x,y,w,h,text,size===20?19:size,{font:'Roboto Condensed',color,lineHeight:1.38,...extra,...(size===20?{lineHeight:(extra.lineHeight||1.38)*20/19}:{})});
const head=(x,y,w,text)=>tx(x,y,w,70,text,26,lime,{font:'Pretendard',weight:800,lineHeight:1.2,letterSpacing:-0.45});
const box=(x,y,w,h,light=false,radius=16)=>B(x,y,w,h,light?white:bg,{radius,border:light?undefined:white,borderWidth:1.2});
const dots=()=>[[1152,103],[1191,103],[1152,138],[1191,138],[1191,173]].map(([x,y])=>B(x-8,y-8,16,16,bg,{border:lime,borderWidth:3,radius:99}));
const header=()=>[T(80,90,1000,115,'Enter a title here',80,{font:'Pretendard',color:white,weight:800,lineHeight:1.2,letterSpacing:-1.9}),L(80,232,1120,0,white,1.2),...dots()];
const slide=(n,title,elements)=>S(`slide_${String(n).padStart(2,'0')}`,title,bg,elements);
const body='Et haru quidem rerum facilis est et elit expedita distinctio. Nam libero eiusmod tempore, cum soluta nobis est eligendi optio cumque nihil.';
const body4='Et haru quidem rerum\nfacilis est et elit expedita\ndistinctio. Nam libero\neiusmo tempore, cum\nsoluta nobis est eligendi\noptio cumque nihil.';
const bullets='•  Ut enim ad minim veniam officia consectetur adipiscing.\n•  Duis aute irure dolor in reprehender dictum lorem vitae.\n•  Nam libero tempore cum soluta no viverra et elit at.';
const cover=(closing=false)=>[
 tx(80,66,400,30,'YOUR ORGANIZATION',18,white,{weight:300,letterSpacing:1.7}),tx(920,65,280,35,'Presenter: Your Name',20,white,{weight:300,align:'right'}),
 T(80,179,650,45,closing?'ADD A SUBTITLE HERE':'Building Stronger Communities',26,{color:lime,weight:700,letterSpacing:2.5}),
 T(80,232,660,200,closing?'ENTER A\nTITLE HERE':'IMPACT REPORT\n2050',80,{font:'Pretendard',weight:800,color:white,lineHeight:1.1,letterSpacing:-1.6}),
 P(765,398,435,240,{radius:14}),B(1140,418,15,16,'#e6e6e6',{border:lime,borderWidth:3,radius:99}),B(1166,418,16,16,lime,{radius:99}),
 ...(closing?[tx(80,519,610,125,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eu justo\nvitae quam sodales semper quis nec risus. Donec euismod blandit massa\neu fermentum. Cras eu varius turpis. Nam id interdum magna, at lacinia\ntortor. Donec rhoncus libero eu cursus aliquam. Aliquam suscipit et nulla\nvel imperdiet. Donec ac bibendum ipsum.',20,white,{font:'Roboto Condensed',lineHeight:1.15})]:[tx(80,592,650,60,'Summit Office Complex | 123 Anywhere St., Suite 100, Any City, ST 12345\n@youraccounthere | visit@here.com | yoursitehere.com | +1 (123) 456-7890',18,white,{weight:300})])
];
const slides=[];
slides.push(slide(1,'Impact Report 2050',cover()));
slides.push(slide(2,'Agenda',[
 ...header().map((n,i)=>i===0?{...n,y:103}:n),box(80,291,1120,348,true,18),
 ...Array.from({length:6},(_,i)=>{const x=i<3?130:722,y=336+(i%3)*103;return [C(x,y,50,50,String(i+1).padStart(2,'0'),23,white,{font:'Roboto Condensed',weight:800,color:bg,border:bg,borderWidth:4,radius:99}),head(x+85,y+5,410,'Enter your content here')]}).flat()
]));
slides.push(slide(3,'Four subpoints',[
 ...header(),...Array.from({length:4},(_,i)=>{const x=80+i*286.7,light=i%2===0;return [box(x,321,260,318,light,13),head(x+30,364,210,`Subpoint 0${i+1}`),tx(x+30,462,215,160,body4,20,light?bg:white,{weight:300,lineHeight:1.25})]}).flat()
]));
slides.push(slide(4,'Image and narrative',[
 ...header(),P(80,319,284,320,{radius:20}),box(378,319,822,320,true,18),head(403,343,690,'Please enter a title for the\nsection and image here'),
 tx(403,460,770,90,'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentum voluptatu\ndeleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non pro,\nsimilique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.',20,bg,{weight:300,lineHeight:1.25}),
 tx(403,560,770,60,'Et haru quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est\neligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus',20,bg,{weight:300,lineHeight:1.25})
]));
slides.push(slide(5,'Keypoints',[
 ...header(),box(80,317,369,322,true),box(456,317,744,322),head(110,349,300,'Keypoint 01'),head(486,349,680,'Keypoint 02'),
 tx(110,444,311,60,'Et haru quidem rerum facilis est et elit\nexpedita distinctio.',20,bg,{weight:300,lineHeight:1.25}),
 tx(110,525,320,80,'•  Ut enim ad minim veniam officia\n•  Duis aute irure dolor in reprehender\n•  Nam libero tempore cum soluta no',18,bg,{weight:800,lineHeight:1.4}),
 tx(486,444,684,80,'Aenean luctus accumsan sapien et molestie. Sed urna magna, dignissim accumsan\nneque id, maximus sagittis enim. Proin arcu purus, pharetra et facilisis vitae, accumsa\nvitae elit. Vestibulum eu tortor efficitur, accumsan augue.',20,white,{weight:300,lineHeight:1.25}),
 tx(486,551,686,60,'Aenean luctus accumsan sapien et molestie. Sed urna magna, dignissim accumsan\nneque id, maximus sagittis enim.',20,lime,{weight:800,lineHeight:1.25})
]));
slides.push(slide(6,'Category subtopics',[
 ...header(),tx(80,318,900,48,'Enter a category title here',26,white,{weight:800}),
 ...Array.from({length:3},(_,i)=>{const x=80+i*375.5;return [box(x,381,368,258),head(x+30,414,316,`Subtopic 0${i+1}`),tx(x+30,500,320,120,'Et haru quidem rerum facilis est et elit\nexpedita distinctio. Nam libero eiusmo\ntempore, cum soluta nobis est eligendi\noptio cumque nihil.',20,white,{weight:300,lineHeight:1.25})]}).flat()
]));
slides.push(slide(7,'Context matrix',[
 ...header(),...[[84,361,1],[84,506,2],[512,361,3],[512,506,4]].flatMap(([x,y,n])=>[box(x,y,416,128,false,10),head(x+34,y+30,340,`Context 0${n}`),tx(x+34,y+74,355,38,'Et haru quidem rerum facilis est et elit nucus.',20,white,{weight:300})]),
 box(941,361,254,273,false,13),head(969,386,210,'Context 05'),tx(969,434,207,185,'Et haru quidem rerum\nfacilis est et elit. Quisque\neu justo vitae quam\nsodales semper quis nec\nrisus. Donec euismod\nblandit massa eu nucus\nfermentum dolor sit.',20,white,{weight:300,lineHeight:1.25})
]));
slides.push(slide(8,'Section narrative',[
 ...header(),box(80,319,1120,320,true,18),head(114,363,1000,'Please enter a title for the section here'),
 tx(114,423,1056,108,'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatu deleniti atque corrupti quos dolores et\nquas molestias excepturi sint occaecati cupiditate non pro, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et\ndolorum fuga. Et haru quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque\nnihil impedit quo minus id quod maxime placeat facere possimus.',20,bg,{weight:300,lineHeight:1.25}),
 tx(114,548,1056,60,'Cras eu varius turpis. Nam id interdum magna, at lacinia tortor. Donec rhoncus libero eu cursus aliquam. Aliquam suscipit et nulla vel\nimperdiet. Donec ac bibendum ipsum. Suspendisse suscipit lacus vitae lacus aliquam porttitor.',20,bg,{weight:300,lineHeight:1.25})
]));
slides.push(slide(9,'Main points',[
 ...header(),...[80,648].flatMap((x,i)=>{const col=i?white:bg;return [box(x,319,552,320,!i),head(x+41,363,470,`Main Point 0${i+1}`),tx(x+41,423,478,88,'At vero eos et accusamus et iusto odio dignissimos ducimus\nqui blanditiis praesentum voluptatu deleniti atque corrupti\nquos dolores et quas molestias excepturi sint occaecati',20,col,{weight:300,lineHeight:1.25}),tx(x+41,524,480,90,bullets,18,col,{weight:800,lineHeight:1.4})]})
]));
slides.push(slide(10,'Comparison',[
 ...header(),box(628,319,572,325,true),head(80,352,490,'Comparison 01'),head(684,352,470,'Comparison 02'),
 ...[80,684].flatMap((x,i)=>[421,539].flatMap(y=>[I(x,y-3,36,36,'CircleCheck',lime,{strokeWidth:1.7}),tx(x+62,y-8,430,95,'At vero eos et accusamus et iusto odio dignissimos nucus\nducimus qui blanditiis praesentum voluptatu deleniti\natque corrupti quos dolores et quas suscipit lacus.',20,i?bg:white,{weight:300,lineHeight:1.25})])),
 C(591,454,74,74,'VS',26,lime,{color:bg,font:'Pretendard',weight:900,radius:99})
]));
slides.push(slide(11,'Image cards',[
 ...header(),...Array.from({length:4},(_,i)=>{const x=80+i*282.3,light=i%2===1;return [box(x,317,273,322,light,14),head(x+31,345,220,`Image 0${i+1}`),tx(x+31,391,223,90,'Quisque eu justo vitae\nquam sodales semper quis\nnec risus. Donec euismod.',20,light?bg:white,{lineHeight:1.2}),P(x+31,499,213,109,{radius:6})]}).flat()
]));
slides.push(slide(12,'Image with subpoints',[
 ...header(),P(80,319,284,320,{radius:20}),head(405,329,440,'Subpoint 01'),head(405,497,440,'Subpoint 02'),
 ...[378,546].map(y=>tx(405,y,438,94,'Quisque eu justo vitae quam sodales semper quis nec\nrisus. Donec euismod. Cras eu varius turpis. Nam id\ninterdum magna, at lacinia tortor. Donec rhoncus.',20,white,{lineHeight:1.15})),
 box(876,319,324,320,false,24),head(905,346,270,'Subpoint 03'),tx(905,394,270,133,'Quisque eu justo vitae quam\nsodales semper quis nec risus.\nDonec euismod. Cras eu varius\nturpis. Nam id interdum magna,\nat lacinia tortor. Donec rhoncus.',20,white,{lineHeight:1.15}),
 tx(905,533,270,75,'Lorem ipsum dolor sit amet, elit\nconsectetur adipiscing elit nucus\nQuisque eu justo vitae quam.',20,white,{lineHeight:1.15})
]));
slides.push(slide(13,'Process',[
 ...header(),...Array.from({length:4},(_,i)=>{const x=80+i*282.5;return [box(x,317,274,315,true,14),head(x+25,350,230,`Process 0${i+1}`),tx(x+25,400,231,105,'Et haru quidem rerum facili\nest et expedita distinctio.\nNam libero tempore soluta\nnobis est eligendi optio isal.',20,bg,{weight:300,lineHeight:1.25}),tx(x+25,520,231,64,'•  Ut enim ad minim veniam\n•  Duis aute irure dolor in',20,bg,{weight:800,lineHeight:1.25}),B(x+105.5,600,64,64,lime,{radius:99}),...(i<3?[V(x+119,620,38,25,'<svg viewBox="0 0 38 25" xmlns="http://www.w3.org/2000/svg"><path d="m1 3 8 10-8 10m12-20 8 10-8 10m12-20 8 10-8 10" fill="none" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>')]:[B(x+117.5,612,40,40,lime,{radius:99,border:white,borderWidth:8})])]}).flat()
]));
slides.push(slide(14,'Closing',cover(true)));
export default D('030','Black Modern Community Impact Report',slides);

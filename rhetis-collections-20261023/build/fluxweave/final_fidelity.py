from pathlib import Path
O=Path('/workspace/output/fluxweave');W=Path('/workspace/work/fluxweave')
def add(p,s):
 f=O/p;f.write_text(f.read_text()+'\n'+s+'\n')
p=O/'elements/table/element.css';s=p.read_text().replace('.tablebox[data-el="fluxweave-table"]:has(th:nth-child(2):last-child)','.tablebox[data-el="fluxweave-table"]:has(th:nth-child(2):last-child):not(:has(th:empty))');p.write_text(s)
p=O/'foundation/foundation.css';s=p.read_text().replace(':has(.at-left:not(:has(.kicker)))',':has(.lockup.at-left)');p.write_text(s)
p=O/'kit/css/tokens.css';s=p.read_text().replace("--font-display:'Montserrat','Pretendard Variable'","--font-display:'Pretendard Variable'");p.write_text(s)
add('foundation/foundation.css','''
.slide.cover .at-top-left .title,.slide.cover .at-bottom-left .title{font-size:var(--type-92);}
.slide.cover .at-left .title>.icon{position:absolute;left:calc(var(--margin-x)*4.9);top:calc(var(--margin-y)*1.15);margin:0;}
.slide .rail>.deco{inset:auto 0 0;height:220px;width:212px;transform:none;}
.slide .page:has(.body>.steps .mark>small)>.seat.back{inset:auto;left:0;top:430px;width:740px;height:290px;aspect-ratio:auto;opacity:.23;z-index:-1;}
''')
add('elements/card/element.css','''
.card[data-el="fluxweave-card"]:has(>.parts>.kick:last-child):not(:has(>.parts>.fig))>.parts>.kick{display:block;}
''')
add('elements/hub/element.css','''
@container(min-width:800px) and (min-height:350px){
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke:not(:nth-child(4)):not(:nth-child(7))::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:var(--n-4);}
}
''')
add('elements/timeline/element.css','''
@container(min-width:400px) and (min-height:650px){
.track.col[data-el="fluxweave-timeline"]>.stop{padding-top:calc(var(--gap-lg)*1.5 - var(--gap) - var(--gap-sm)*.2);}
}
''')
add('elements/steps/element.css','''
.steps[data-el="fluxweave-steps"]:has(.mark>small)>.step:nth-child(3){background:var(--a1-8);}
''')
# The source fills beneath the same line data. Segment fill follows the line point anchors.
add('elements/card/element.css','''
.card[data-el="fluxweave-card"]>.parts>.lines>.pt:not(:first-child)::after{display:block;content:"";left:anchor(var(--fluxweave-prev) center);right:anchor(var(--fluxweave-self) center);top:calc(anchor(var(--fluxweave-prev) bottom) - 100cqh);bottom:calc(var(--gap-lg)*1.8);background:color-mix(in srgb,var(--a2) 28%,var(--n-1));clip-path:polygon(0 100cqh,100% calc(100% - var(--v)/var(--max)*100cqh),100% 100%,0 100%);z-index:-2;}
''')
p=W/'waves.py';s=p.read_text().replace('  else:\n   d=f', '''  elif kind==4:
   d=f'M -30 {150*t:.2f} C 40 {30+150*t:.2f}, 105 {100+50*t:.2f}, 170 190 C 190 {205-45*t:.2f}, 220 {180-30*t:.2f}, 250 {175-50*t:.2f}'
   vb='0 0 212 220'
  else:
   d=f''');p.write_text(s)
p=W/'reassemble.py';s=p.read_text().replace("'<span class=\"logo\"></span><div class=\"deco\">'+wave_svg(1)","'<span class=\"logo\"></span><div class=\"deco\">'+wave_svg(4)")
s=s.replace("v=f'<section class=\"slide\">{rail}<div class=\"page\">{head}","v=f'<section class=\"slide\">{rail}<div class=\"page\">'+('<div class=\"seat back\" data-ph=\"1\"></div>' if n==17 else '')+f'{head}")
# Explicit editorial line breaks retained from the originals.
notes={8:'사업 성장에 발맞춰 전문 인력과 조직 체계를 지속적으로<br>확대하며, 고객과 함께 더 큰 성장을 만들어가고 있습니다.',9:'기업의 다양한 과제를 이해하고 전략 수립부터 실행과<br>운영까지, 필요한 솔루션을 유기적으로 연결해 제공합니다.',10:'기업의 업무 환경과 목표에 최적화된 솔루션을 통해<br>업무 효율을 높이고 안정적인 비즈니스 성장을 지원합니다.',11:'사업 전략 중심으로 시작해 컨설팅 영역을 확대하며<br>프로젝트 수행 규모를 지속적으로 키워가고 있습니다.',12:'기업 환경에 따라 필요한 제품과 서비스를<br>유연하게 구성할 수 있습니다.',13:'축적된 경험과 전문성, 안정적인 운영 역량을 바탕으로<br>고객의 지속적인 성장과 비즈니스 가치를 만들어갑니다.',14:'다양한 고객과 프로젝트를 함께하며 지속적인 파트너십과<br>성과를 만들어가고 있습니다.',15:'지속적인 기술 개발과 품질 혁신을 통해<br>기업의 전문성과 신뢰도를 높여가고 있습니다.',16:'각 분야의 전문 파트너와 긴밀하게 협력하며 더 넓은 비즈니스 가치와<br>새로운 성장 기회를 만들어갑니다.',17:'사업 기반을 강화하고 시장과 사업 영역을 단계적으로<br>확장해 지속 가능한 성장 체계를 구축합니다.'}
s=s.replace('# The review style',f'for _n,_desc in {notes!r}.items():\n slides[_n]=(slides[_n][0],_desc,slides[_n][2])\n\n# The review style');p.write_text(s)
print('final source repairs')

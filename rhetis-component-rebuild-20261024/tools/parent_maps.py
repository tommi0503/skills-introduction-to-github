from pathlib import Path
import json,sys,re
sys.path.insert(0,'/workspace/work/tools')
from render_review import browser,serve_url,load
from playwright.sync_api import sync_playwright
BASE=Path('/workspace/work/rebuild-20261024');OLD=Path('/workspace/work/deliverables')
# Every source component is identified by a DOM selector, never by a library fixture selector.
SPECS={
'afterglow':{
'01':[(None,'furniture','.slide>div:nth-of-type(1)','표지의 두 줄 메시지, 46px/가벼운 행과 굵은 행'),('prose','variant:.lead','.slide>h2','28px 두 줄 도입 문단'),('prose','variant:.quiet','.slide>p.bodycopy','16px 네 줄 부연')],
'02':[(None,'furniture','.slide>div:nth-of-type(1)','54px 영문 섹션 표제와 32px 국문 부제'),('agenda','base','.slide>div[style*="border-radius:50%"]','160px 테두리 원 다섯 개, 210px 간격, 큰 영문명/100px 가는 괘선/작은 국문명')],
'03':[(None,'unexpressible','.slide>div:nth-of-type(1)','176px SUITE 영문 구분 표제'),(None,'furniture','.slide>div:nth-of-type(2)','32px 한글 구분 부제'),('prose','same-as:01','.slide>div:nth-of-type(4)>p','작은 두 줄 부연'),('list','variant:.check','.slide>div:nth-of-type(4)>ul','16px 소제목 세 줄'),(None,'unexpressible','.slide>div:last-of-type','오른쪽 아래 원형 다음 이동 버튼')],
'04':[('headline','base','.eyebrow,.heading','21px kick + 32px 강조 두 줄, 행간1.35, 자간-.25px'),('list','base','.bullet','27px 원형 화살표 아이콘 + 18px 이름/16px 긴 note'),('image-frame','base','.ph','493px 높이의 둥근 회색 그림 자리')],
'05':[('headline','same-as:04','.eyebrow,.heading','반복 섹션 머리'),('card','base','.service-cards','280×376 흰 미디어 패널 네 개, 14px 간격, 260×212 그림/23px 검정 순번/18px 이름/14px 설명')],
'06':[('headline','same-as:04','.eyebrow,.heading','반복 섹션 머리'),('list','same-as:04','.bullet','원형 화살표와 이름/본문'),('chart-area','base','.slide>svg','가는 강조선과 지름7px 점 여섯 개, 단일 면적 채움'),(None,'unexpressible','.slide>div:last-of-type','140px 증가 수치와 38px 단위')],
'07':[('headline','same-as:04','.eyebrow,.heading','반복 섹션 머리'),('image-frame','same-as:04','.ph','둥근 중앙 복잡 일러스트 자리'),('tag','base','.process h3','16px 문자 높이의 강조 사각 하이라이트 네 개'),('prose','variant:.quiet','.process p','14px 네 줄 부연 네 개'),(None,'unexpressible','.process.toprow','위쪽 두 항목의 아래 1px 가로 괘선')],
'08':[('headline','same-as:04','.eyebrow,.heading','반복 섹션 머리'),('prose','base','.content>p.bodycopy','정상 자간 Freesentation 시각16.92px, 24.75px 행간, 5줄'),('steps','base','.how-cards','140px 흰 가로카드 세 개의 수직 시퀀스, 왼쪽82px 아이콘/오른쪽 이름과 3줄 note, 사이33px 원+하향 쉐브론')],
'09':[('headline','variant:.center','.slide>h1','가운데 두 줄 강조 제목'),('prose','variant:.lead','.slide>p','가운데 두 줄 도입 문단'),('prose','variant:.quiet','.slide>div:last-of-type','13px 연락처/문의 세부문단')]
},
'confluence':{
'01':[(None,'furniture','.slide>div:last-of-type','오른쪽 표지 lockup: 작은 영문/47px 부제/128px 제목/16px 설명/8px 부연'),(None,'furniture','.ph','표지 그림 자리와 우상단 작은 로고')],
'02':[(None,'furniture','.slide>.ph,.slide>h1,.slide>.caps,.slide>.rule','중앙 표제와 영문 작은 부제, 양옆 선, 그림 자리'),('agenda','base','.slide>.card','346×175 visible panel 여섯 개, 3열2행, 원형53px 순번이 상단23px 겹침, 32px 이름/괘선/13px 부연')],
'03':[(None,'furniture','.slide>.ph,.slide>div:nth-of-type(2),.slide>.rule','왼쪽 페이지 장치: 작은 그림/60px 2행 제목/9px 영문/13px 부연/수직 괘선'),(None,'unexpressible','.slide>.card:nth-of-type(4)','좌측220×98 강조 제목 패널을 품은 766×115 label/value 띠'),('card','base','.slide>.card:nth-of-type(n+5)','242×433 필드 카드 세 개, 220×68 상단강조띠, 20px 작은 필드/52px 값(두 줄 날짜24px), 점선/20px·15px 세부값')],
'04':[('hub','base','.rule,.icon,.goal,.slide>div[style*="width:367px"],.ph','1080×568 중심-주변 관계: 367px 원+17px 흰 ring/60px 제목, 4개76px 아이콘+40px 이름+14px note, 가로세로 중심선')]
}}
WHY={
('afterglow','03','176px SUITE 영문 구분 표제'):'원본176px는 허용된 최대 type128을 넘는다. 고정 glyph 배율로 타입 계약을 우회하지 않는다.',
('afterglow','03','오른쪽 아래 원형 다음 이동 버튼'):'독립 navigation/action 버튼 계약이 없고 callout은 결론 문장용이다.',
('afterglow','06','140px 증가 수치와 38px 단위'):'원본140px 수치가 허용 type128 상한을 넘고 단위는 분리 절대배치된다.',
('afterglow','07','위쪽 두 항목의 아래 1px 가로 괘선'):'소속 멤버와 무관한 독립 괘선 계약이 없다. prose나 tag의 형제 위치 조건으로 그리지 않는다.',
('confluence','03','좌측220×98 강조 제목 패널을 품은 766×115 label/value 띠'):'다른 제목 패널과 값 영역을 담는 label/value 컨테이너가 없다. pill은 한 줄 capsule이며 card base는 세로 필드 카드다.'}
MEASURE=r'''(selector)=>{
let els=[...document.querySelectorAll(selector)];if(!els.length)return null;
let rs=els.map(e=>e.getBoundingClientRect());let x=Math.min(...rs.map(r=>r.x)),y=Math.min(...rs.map(r=>r.y)),z=Math.max(...rs.map(r=>r.right)),b=Math.max(...rs.map(r=>r.bottom));
return {bbox:[x,y,z-x,b-y].map(v=>+v.toFixed(2)),metrics:els.map(e=>{let s=getComputedStyle(e),r=e.getBoundingClientRect();return {tag:e.tagName,class:e.getAttribute('class'),text:e.textContent.trim().slice(0,500),box:[r.x,r.y,r.width,r.height],font:s.fontFamily,size:s.fontSize,weight:s.fontWeight,line:s.lineHeight,tracking:s.letterSpacing,padding:s.padding,gap:s.gap,border:s.border,borderRadius:s.borderRadius,fill:s.background,color:s.color}})}
}'''
with sync_playwright() as pw:
 b=browser(pw)
 for name,pages in SPECS.items():
  instances=[];measurements={}
  for pp,spec in pages.items():
   f=OLD/name/'review/replica'/('slide_'+pp+'.html');page=b.new_page(viewport={'width':1280,'height':720});load(page,f);measurements[pp]=[]
   instances.append({'page':pp,'bbox':[0,0,1280,720],'leaf':None,'use':'background','design':'전체 페이지 면과 테두리/페이지 바깥 바탕. 색은 roles가 지정한 자리만 사용한다.'})
   if name=='afterglow':
    m=page.evaluate(MEASURE,'.top');instances.append({'page':pp,'bbox':m['bbox'],'leaf':None,'use':'furniture','design':'상단 세 칸 페이지 장치: 왼쪽 덱 이름/가운데 섹션/오른쪽 회사명','replica_selector':'.top','source_metrics':m['metrics']})
    if page.locator('.rule').count():
     m=page.evaluate(MEASURE,'.rule');instances.append({'page':pp,'bbox':m['bbox'],'leaf':None,'use':'furniture','design':'페이지를 두 영역으로 가르는 전폭 1px 기준선','replica_selector':'.rule','source_metrics':m['metrics']})
   for leaf,use,sel,desc in spec:
    m=page.evaluate(MEASURE,sel)
    if m is None:raise ValueError((name,pp,sel))
    entry={'page':pp,'bbox':m['bbox'],'leaf':leaf,'use':use,'design':desc,'replica_selector':sel,'source_metrics':m['metrics']}
    if use=='unexpressible':entry['why']=WHY[(name,pp,desc)];entry['proposed_markup']='<section class="'+('action-button' if '버튼' in desc else 'field-band' if name=='confluence' else 'extended-type' if 'px' in desc else 'rule-block')+'">…</section>'
    if leaf:entry['fixture']='replica-'+pp
    instances.append(entry);measurements[pp].append(m)
   if name=='afterglow' and pp=='06':
    entry={'page':pp,'bbox':[1044,252,161,375],'leaf':None,'use':'unexpressible','design':'면적 플롯 위 검정 상향 화살표 세 개','why':'chart.area 구조에 데이터와 무관한 장식 화살표 멤버가 없고 source의 그래프 위에 겹친다.','proposed_markup':'<div class="trend-arrows"><i></i><i></i><i></i></div>'};instances.append(entry)
   page.close()
  roles=({'페이지 내부 바탕':'--page','본문':'--ink','상단 강조/하단 glow/화살표/영역선':'--a1','강조 면 위 글자':'--a1-on','흰 카드/그림 위 반대 면':'--n-9','흰 카드 위 글자':'--page','그림 자리':'--n-3','바깥 회색':'--n-5','가는 규칙선':'--n-6'} if name=='afterglow' else {'cyan 강조 채움':'--a1','blue 강조 채움':'--a2','대조 글자':'--a1-on / --a2-on','흰 패널/중앙 ring':'--page','기본 글자':'--ink','보조 설명':'--n-7','가는 선':'--n-3','옅은 위 바탕':'--a1-1-soft','옅은 아래 바탕':'--a2-1-soft'})
  r=BASE/name/'review';(r/'map.json').write_text(json.dumps({'collection':name,'roles':roles,'instances':instances},ensure_ascii=False,indent=2));(BASE/name/'build').mkdir(exist_ok=True);(BASE/name/'build/source-measurements.json').write_text(json.dumps(measurements,ensure_ascii=False,indent=2))
  gaps=[x for x in instances if x['use']=='unexpressible'];(r/'GAPS.md').write_text('# Unexpressible\n\n'+'\n\n'.join(f'## {x["page"]} · {x["design"]}\n\n{x["why"]}\n\n```html\n{x["proposed_markup"]}\n```'for x in gaps)+'\n')
  print(name,len(instances),'instances',len(gaps),'gaps')
 b.close()

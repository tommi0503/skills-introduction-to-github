from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
import json,hashlib,copy
B=Path('/workspace/work/rebuild/toggle-grid/build');old=B/'map-foundation.json';m=json.loads(old.read_text());a=copy.deepcopy(m['instances']);src=json.loads((B/'source-toggle-furniture.json').read_text());dom=json.loads((B/'source-dom.json').read_text())
brand='<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 8-3 6q-2 5 2 3l6-8m1 0-3 6q-2 5 2 3l7-10m0 1-3 6q-2 5 2 3l4-8"/><circle cx="7" cy="4" r="1.5" fill="currentColor" stroke="none"/></svg>'
# One real cover lockup replaces three incorrectly typed top/title/top fragments.
a=[i for i in a if not(i['page']=='01'and i['use']=='furniture'and i.get('source',{}).get('selector')in['.slide > span.badge','.slide > h1','.slide > p'])]
a.append({'page':'01','bbox':[35,56,472.171875,145],'leaf':None,'use':'furniture','foundation_slot':'lockup','cover':True,'title_font':52,'source_font_size':52,'surface_role':'transparent','foreground_role':'--ink','reassembly_markup':'<p class="kicker">11 CREATIVE SLIDES</p><h1 class="title">BRAND STRATEGY</h1><p class="lead">Presentation Template</p>','design':'52/850 Pretendard 제목,18/700 검정 capsule kicker,29/350 무면 부제를 가진 단일 cover lockup. 원본 좌표35/56부터145높이; 배지 바깥 직사각 면 없음.','source':{'file':'replica/slide_01.html','selectors':['.slide > span.badge','.slide > h1','.slide > p'],'measurements':src['01']},'source_texts':dom['01']['texts']})
for i in a:
 p=i['page'];slot=i.get('foundation_slot');data=src.get(p,{})
 if p=='02'and slot=='lockup':
  i['bbox']=data['coverTitle']['bbox'];i['title_font']=122;i['source_font_size']=122;i['design']='실제 Pretendard Variable122/900 제목. DOM block135y/134.1875h와 textRange129y/145h를 구별하여 원문 line-height1.1 유지.'
 if p=='02'and slot=='top':
  i['reassembly_markup']='<span class="deck">Presentation</span><span class="sec">（2090）</span><b class="label">'+brand+' YOUR COMPANY</b>';i['design']='45px 높이의 위아래 가는 괘선,42px 좌우 inset,15/400 일반 필드2개와15/700 company/icon. pill 없음.'
 if p=='02'and slot=='foot':
  i['reassembly_markup']='<span class="deck">Presentation Template</span><span class="src">PHONE : 010 000 0000<br>MAIL : KIMMIRI@MIRIDIH.COM</span>';i['design']='116px footer:왼쪽30/300 제목(59,644),오른쪽13/300 연락처(1001.61,640),줄간22.1. 서로 독립된 deck/src 의미 필드.'
 if p=='02'and i.get('graphic')=='hairline':i['role']='--n-5';i['design']='source02 y419의1px 괘선; transparent로 잘못 분류했던 source border-top을 실제 중립5 선으로 복원.'
 if slot=='head'and'header'in data:
  b=data['headerBadge'];h=data['header'];i['foundation_tokens']={'--toggle-grid-head-label-x':str(b['bbox'][0]/h['bbox'][2]*100)+'%','--toggle-grid-head-label-y':str(b['bbox'][1]/h['bbox'][3]*100)+'%','--toggle-grid-head-label-w':str(b['bbox'][2]/h['bbox'][2]*100)+'%','--toggle-grid-head-label-pad':b['style']['padding'].split()[-1],'--toggle-grid-head-label-size':'var(--type-'+str(round(float(b['style']['size'][:-2])))+')'};i['design']+='; 원본 header title(132,34),badge좌표/폭/폰트는 선언된 foundation_tokens,14/300 설명 right56/top32. 실제Oswald는허용NotoSans75%로 대체하며 exact font gap 별도.'
 if p=='05'and slot=='head'and'<h1'not in i.get('reassembly_markup',''):
  i['reassembly_markup']=i['reassembly_markup'].replace('\n','<br>');i['design']='Source whyexplain standalone paragraph,16/300/24.5; source explicit two-line break retained with br, transparent face.'
 if slot=='foot'and'footBrand'in data:
  i['reassembly_markup']='<span class="no">'+escape(data['footNo']['text'])+'</span><span class="deck">'+brand+' YOUR COMPANY</span>';i['design']='57px numbered footer,14/300 page number at28px inset;13/300 company with22x20 source brand vector,38px extra right margin. 무근거 bold700 제거.'
 if slot=='rail'and'railTitle'in data:i['design']+='; label140y, title180y, 본문442y(425+원본17 margin)의 실제 DOM 좌표. Source Oswald79/700→허용 Noto Sans native75%;본문17/300/27.5 보존.'
# Simple switch is a page graphic, preserved as text-free geometry.
a.append({'page':'02','bbox':[88,284,111,43],'leaf':None,'use':'furniture','foundation_slot':'deco','design':'111x43 단순 스위치 장식. ink capsule와36x37 accent 타원,상3/우4 inset. 텍스트/요소 없음.','source_svg':'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 111 43"><rect width="111" height="43" rx="21.5" fill="var(--ink)"/><ellipse cx="89" cy="21.5" rx="18" ry="18.5" fill="var(--a1)"/></svg>'})
# Exact unsupported family is stated; the supported fallback does not pretend to be Oswald.
for p,data in src.items():
 if p=='native_width_probe':continue
 key='headerTitle'if'headerTitle'in data else'railTitle'if'railTitle'in data else None
 if key:
  n=data[key];title=BeautifulSoup(n['html'],'html.parser').find('h1').decode_contents();a.append({'page':p,'bbox':n['bbox'],'leaf':None,'use':'unexpressible','design':'79px/700 Oswald 장치 제목의 정확한 글꼴 윤곽','why':'원본 실제CDP는 Oswald-Bold를 사용하지만 README 허용글꼴표에는 Oswald가 없다. 컬렉션은 허용 Noto Sans의 native wdth75%/700을 사용하며 정확한 Oswald 글리프 높이·윤곽까지 동일하다고 주장하지 않는다. font alias나 transform으로 우회하지 않는다.','proposed_markup':'<h1 class="title" data-contract-proposal="foundation.allowed-fonts@2" data-font-family="Oswald" data-font-weight="700">'+title+'</h1>','source_font_family':'Oswald','fallback_font_family':'Noto Sans','fallback_native_width':'75%','source_actual_fonts':n['actual_fonts']})
proposal={'collection':'toggle-grid','base_map_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'notes':['Do not edit shared map_foundation.py while Filament author owns its branch. Replace this collections map-foundation instances only after root review.','reassemble.py must forward declared foundation_tokens into apparatus style, without page-specific CSS.','All permitted foundation classes are existing contract names. Exact unsupported Oswald is listed separately; body Do Hyeon remains unchanged.'],'new_font':{'family':'Noto Sans','native_axes':{'wght':[100,400,900],'wdth':[62.5,100,100]},'used_width':'75%','asset':'review/assets/fonts/NotoSansWidth.ttf','font_token':'--toggle-grid-header-font'},'native_width_probe':src['native_width_probe'],'instances':a};(B/'foundation-toggle-proposal.json').write_text(json.dumps(proposal,ensure_ascii=False,indent=2));print('proposal',len(a),'instances',sum(i['use']=='unexpressible'for i in a),'gaps')

"""Inventory immutable replica furniture and residual coverage. Never reads old library CSS."""
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
from reassemble import palette
import json,re
R=Path('/workspace/work/rebuild');NAMES=['tide-tab','cutfield','filament','portico','toggle-grid','lamella','rulemark']
def union(bs):
 x=min(b[0] for b in bs);y=min(b[1] for b in bs);return [round(x,2),round(y,2),round(max(b[0]+b[2] for b in bs)-x,2),round(max(b[1]+b[3] for b in bs)-y,2)]
def inside(b,a):
 x=b[0]+b[2]/2;y=b[1]+b[3]/2
 return a[0]-1<=x<=a[0]+a[2]+1 and a[1]-1<=y<=a[1]+a[3]+1

def contains_box(a,b):
 return a[0]-1<=b[0] and a[1]-1<=b[1] and a[0]+a[2]+1>=b[0]+b[2] and a[1]+a[3]+1>=b[1]+b[3]

def parts(ts):return '<br>'.join(escape(t['text']) for t in ts)
def mapone(name):
 D=R/name/'build';src=json.loads((D/'source-dom.json').read_text());others=sum([json.loads(f.read_text())['instances'] for f in D.glob('map-*.json') if f.name!='map-foundation.json'],[]);out=[]
 def paint(c,foreground=False):
  nums=re.findall(r'[\d.]+',str(c));
  if c.startswith('rgba') and len(nums)>3 and float(nums[3])==0:return 'transparent'
  if len(nums)<3:return '--ink' if foreground else '--page'
  rgb=tuple(round(float(x))for x in nums[:3]);pal=palette(name);keys=['--page','--ink','--a1','--a2','--n-1','--n-2','--n-3','--n-4','--n-5','--n-6','--n-7','--n-8','--n-9','--a1-1-soft','--a1-2-soft','--a1-3-soft','--a1-9']
  opts=[]
  for k in keys:
   h=pal.get(k,'')
   if re.fullmatch('#[a-fA-F0-9]{6}',h):r=tuple(int(h[j:j+2],16)for j in(1,3,5));opts.append((sum((a-b)**2 for a,b in zip(rgb,r)),keys.index(k),k))
  key=min(opts)[2]
  if foreground and key in ['--a1','--a2'] and name=='portico':key+='-7'
  return key
 def add(page,bbox,use,design,slot=None,markup=None,why=None,**kw):
  a=dict(page=page,bbox=bbox,leaf=None,use=use,design=design)
  if slot:a['foundation_slot']=slot
  if markup:a['reassembly_markup']=markup
  if why:a.update(why=why,proposed_markup=kw.pop('proposed_markup','<div class="apparatus" data-contract-proposal="foundation.page@2"><div class="title">원문</div></div>'))
  a.update(kw);out.append(a);return a
 for page,v in src.items():
  basebg=v['background']['background'];dark='rgb(10, 48, 51)' in basebg and 'rgb(10, 48, 51)'==v['background']['color']
  # HTML source .slide has color ink even on dark scenes; background decides scene context.
  bgrole=paint(basebg);bgrole='--a1-9' if name=='cutfield' and 'rgb(10, 48, 51)' in basebg else ('--page'if bgrole=='transparent'else bgrole)
  add(page,[0,0,1280,720],'background','페이지 전체 바탕; 장면 면은 foundation 소유. '+basebg,role=bgrole,context='on' if bgrole in['--a1-9','--ink','--a1'] else 'base',foreground_role='--page' if bgrole=='--a1-9' else paint(v['background']['color'],True))
  mapped=[i for i in others if i['page']==page];ts=v['texts']
  def owned(b):return any(inside(b,i['bbox']) for i in mapped)
  def node_ts(node):return [t for t in ts if t['selector']==node['selector'] or t['selector'].startswith(node['selector']+' > ')]
  def furn(node,slot,markup=None,design=None,bbox=None):
   nt=node_ts(node);b=bbox or (union([t['bbox']for t in nt])if node['tag'].lower()=='svg'and nt else node['bbox'])
   if node['tag'].lower()=='svg'and nt and markup and escape(node['text'])in markup:markup=markup.replace(escape(node['text']),parts(nt))
   measured_size=float((nt[0]['style']['size']if node['tag'].lower()=='svg'and nt else node['style']['size'])[:-2])
   right_aligned=bool(len(nt)>1 and max(t['bbox'][0]+t['bbox'][2]for t in nt)-min(t['bbox'][0]+t['bbox'][2]for t in nt)<2)
   return add(page,b,'furniture',design or f"{slot}: source {node['classes'] or node['tag']} apparatus",slot,markup or escape(node['text']),source={'selector':node['selector'],'file':'replica/slide_'+page+'.html','measurements':node['style']},source_texts=nt,text_align=('right'if 'text-align:right'in node['html'] or right_aligned else 'left'),surface_role=paint(node['style']['background']),foreground_role=paint(node['style']['color'],True),source_font_size=measured_size)
  def h1(node,slot='head',cover=False):
   nt=node_ts(node)
   if not nt:return
   # Do not take a title already mapped inside a body element or unsupported component.
   nt=[t for t in nt if not owned(t['bbox'])]
   if not nt:return
   b=union([t['bbox'] for t in nt]);maxfont=max(float(t['style']['size'][:-2]) for t in nt)
   if maxfont>130:
    add(page,b,'unexpressible','원본 대형 표제 '+str(round(maxfont,2))+'px',why='공유 타입의 최댓값은128이며 원본의 대형 표제를 같은 크기로 담을 수 없다. 타입 확장이나 SVG 텍스트로 계약을 우회하지 않는다.',proposed_markup='<div class="lockup display-xl" data-contract-proposal="foundation.page@2"><h1 class="title">'+parts(nt)+'</h1></div>',source_texts=nt,text_align=('right'if 'text-align:right'in node['html'] else 'left'),surface_role=paint(node['style']['background']),foreground_role=paint(node['style']['color'],True),source_font_size=float(node['style']['size'][:-2]));return
   f=furn(node,'lockup' if cover else slot,'<h1 class="title">'+parts(nt)+'</h1>',bbox=b);f.update(title_font=min(128,maxfont),cover=cover)
   if node['tag'].lower()=='svg':
    fills=re.findall(r'fill:(#[a-fA-F0-9]{6})',node['html'])
    if fills:
     h=fills[0];f['foreground_role']=paint('rgb('+','.join(str(int(h[j:j+2],16))for j in(1,3,5))+')',True)
  for node in v['nodes']:
   c=set((node['classes'] or '').split());nt=node_ts(node);b=node['bbox'];text=node['text'];tag=node['tag'].lower()
   if name=='tide-tab':
    if 'side'in c:
     soup=BeautifulSoup(node['html'],'html.parser');title=soup.select_one('h1');en=soup.select_one('.en');sub=soup.select_one('.sub')
     titlehtml=''.join('<b>'+escape(t.get_text())+'</b>' if 'blue'in(t.get('class')or[]) else escape(t.get_text()) for t in title.find_all('span'))
     titlehtml=titlehtml.replace('</b>','</b>')
     # Source uses block cyan/blue spans: preserve explicit line breaks.
     spans=title.find_all('span');titlehtml='<br>'.join(('<b>'+escape(t.get_text())+'</b>') if 'blue'in(t.get('class')or[]) else escape(t.get_text()) for t in spans)
     furn(node,'rail','<h1 class="title">'+titlehtml+'</h1><span class="label">'+escape(en.get_text())+'</span><p class="lead">'+str(sub.decode_contents())+'</p>')
    elif tag=='h1' and 'title'in c:
     soup=BeautifulSoup(node['html'],'html.parser');sp=soup.find_all('span');f=furn(node,'head','<h1 class="title">'+''.join('<b>'+escape(x.get_text())+'</b>' if 'blue'in(x.get('class')or[]) else escape(x.get_text()) for x in sp)+'</h1>');f['title_font']=64
    elif 'en'in c:furn(node,'top','<span class="sec">'+escape(text)+'</span>')
   elif name=='cutfield':
    if 'logo'in c:furn(node,'top','<span class="deck"><span class="seat logo"></span>'+escape(text)+'</span>')
    elif 'topline'in c:furn(node,'top','<span class="sec">'+escape(text)+'</span>')
    elif tag=='svg' and nt and max(float(t['style']['size'][:-2]) for t in nt)>=70:h1(node,cover=page=='01')
    elif page=='01' and text and not any(owned(t['bbox']) for t in nt):furn(node,'foot' if b[1]>600 else 'head','<span class="deck">'+escape(text)+'</span>')
    elif page=='14' and text and b[1]>500 and not owned(b):furn(node,'foot','<span class="deck">'+escape(text)+'</span>')
   elif name=='filament':
    if 'seal'in c:
     add(page,b,'unexpressible','회전한 타원 경로의 COMPANY PROFILE 순환 글자 인장',why='foundation에는 곡선 텍스트/인장 슬롯이 없고 tag/headline은 직선 텍스트다. 텍스트를 SVG 그래픽으로 바꾸어 우회하지 않는다.',proposed_markup='<div class="seal" data-contract-proposal="foundation.page@2"><span class="text">'+escape(text)+'</span></div>');continue
    if 'conf'in c or 'footer'in c or (text and 'small'in c):
     f=furn(node,'rail' if 'conf'in c or b[2]<50 else 'foot','<span class="deck">'+escape(text)+'</span>')
     rotation=re.search(r'transform:\s*rotate\(([-\d.]+)deg\)',node['html'])
     if rotation:f['rotation_degrees']=float(rotation.group(1))
    elif 'eng'in c and not owned(b):
     if 'writing-mode:vertical-rl'in node['html']:
      f=furn(node,'rail','<h1 class="title">'+escape(text)+'</h1>');f['title_font']=98
     else:h1(node,cover=page=='01')
    elif text and not any(owned(t['bbox']) for t in nt) and (page=='01' or page=='02' and b[1]<100 or page=='03' and b[1]<200):furn(node,'top' if b[1]<70 else 'head','<span class="kicker">'+escape(text)+'</span>')
   elif name=='portico':
    if 'titleband'in c:
     soup=BeautifulSoup(node['html'],'html.parser');h=soup.select_one('h1');f=furn(node,'head','<h1 class="title">'+escape(h.get_text())+'</h1>');f['title_font']=54
     star=soup.select_one('svg.star')
     if star:
      st=dict(re.findall(r'(left|top|width|height):([\d.]+)px',star.get('style','')));sb=[float(st.get('left',0))+b[0],float(st.get('top',0))+b[1],float(st.get('width',40)),float(st.get('height',40))]
      add(page,sb,'furniture','주 표제 오른쪽 위 6개 점의 방사형 별 장식','deco',source_svg=str(star),foreground_device=True,foreground_role='--a1-7')
    elif 'rail'in c:
     texts=[t['text'] for t in nt];furn(node,'rail',''.join('<span class="'+('sec' if i==0 else 'deck')+'">'+escape(t)+'</span>' for i,t in enumerate(texts)))
    elif tag=='footer':
     soup=BeautifulSoup(node['html'],'html.parser');ps=soup.select('footer>p');last=soup.select_one('footer>b')
     furn(node,'foot',''.join('<span class="idx"><span class="deck">'+x.decode_contents()+'</span></span>'for x in ps)+'<span class="label">'+escape(last.get_text())+'</span>')
    elif 'main'in c:
     soup=BeautifulSoup(node['html'],'html.parser');f=furn(node,'lockup','<p class="kicker">'+escape(soup.h2.get_text())+'</p><h1 class="title">'+escape(soup.h1.get_text())+'</h1><p class="lead">'+ '<br>'.join(p.decode_contents() for p in soup.find_all('p'))+'</p>');f.update(cover=True,title_font=128)
   elif name=='toggle-grid':
    if 'header'in c:
     soup=BeautifulSoup(node['html'],'html.parser');h=soup.h1;k=soup.select_one('.badge');lead=soup.select_one('small');f=furn(node,'head','<h1 class="title">'+escape(h.get_text())+'</h1>'+('<p class="kicker">'+escape(k.get_text())+'</p>' if k else '')+('<p class="lead">'+escape(lead.get_text())+'</p>' if lead else ''));f['title_font']=79
    elif 'side'in c:
     soup=BeautifulSoup(node['html'],'html.parser');furn(node,'rail','<span class="label">'+escape(soup.select_one('.badge').get_text())+'</span><h1 class="title">'+soup.h1.decode_contents()+'</h1><p class="lead">'+soup.p.decode_contents()+'</p>')
    elif 'footer'in c or 'bottom'in c:
     furn(node,'foot','<span class="no">'+escape(nt[0]['text'])+'</span><span class="deck">'+'<br>'.join(escape(t['text']) for t in nt[1:])+'</span>')
    elif 'topline'in c:furn(node,'top',''.join('<span class="'+k+'">'+escape(t['text'])+'</span>' for k,t in zip(['deck','sec','label'],nt)))
    elif page in ['01','02'] and tag=='h1':h1(node,cover=True)
    elif page=='01' and text:furn(node,'top','<span class="label">'+escape(text)+'</span>')
    elif 'whyexplain'in c:furn(node,'head','<p class="lead">'+escape(text)+'</p>')
   elif name=='lamella':
    if 'measured-title'in c or page=='20' and 'ink'in c and b[1]<211 and b[0]<1000:
     # Grouped below; don't reproduce defective per-line width fitting.
     continue
    if text and not any(owned(t['bbox']) for t in nt):
     if b[1]>=650 and len(text)<60:furn(node,'foot','<span class="'+('no' if text.isdigit() else 'sec')+'">'+escape(text)+'</span>')
     elif b[1]<70 and float(node['style']['size'][:-2])<20:furn(node,'top','<span class="sec">'+escape(text)+'</span>')
     elif page=='01' and b[1]<180:furn(node,'top','<span class="sec">'+escape(text)+'</span>')
     elif b[0]<52 and b[1]<660 and float(node['style']['size'][:-2])<20:
      furn(node,'head','<p class="lead">'+escape(text)+'</p>',design='주 표제에 딸린 페이지 설명; 독립 본문 요소가 아닌 head.lead')
    if page=='01' and 'measured-title'in c:pass
   elif name=='rulemark':
    if 'head'in c:
     soup=BeautifulSoup(node['html'],'html.parser');brand=soup.select_one('.brand');chips=soup.select('.chip');furn(node,'top','<span class="deck"><span class="logo"><i></i></span>'+escape(brand.get_text())+'</span><div class="idx">'+''.join('<span class="label'+(' on' if 'on'in k.get('class',[]) else '')+'">'+escape(k.get_text())+'</span>' for k in chips)+'</div>')
    elif tag=='h1' and 'title'in c:h1(node)
    elif 'foot'in c:furn(node,'foot',''.join('<span class="'+k+'">'+escape(t.get_text())+'</span>' for k,t in zip(['deck','src','no'],BeautifulSoup(node['html'],'html.parser').select('footer>span'))))
    elif page=='01' and b==[180,224,920,220]:
     soup=BeautifulSoup(node['html'],'html.parser');ds=soup.select('div.at>div');f=furn(node,'lockup','<h1 class="title">'+escape(ds[0].get_text())+'<br><b>'+escape(ds[1].get_text())+'</b></h1>');f.update(cover=True,title_font=88)
  if name=='lamella':
   titleNodes=[n for n in v['nodes'] if 'measured-title'in(n['classes']or'').split() or page=='20' and 'ink'in(n['classes']or'').split() and n['bbox'][1]<211 and n['bbox'][0]<1000]
   if titleNodes:
    titletexts=sum([node_ts(n) for n in titleNodes],[]);bbox=union([n['bbox'] for n in titleNodes])
    if page=='01':
     bbox=union([bbox]+[t['bbox']for t in ts if inside(t['bbox'],bbox)])
     add(page,bbox,'unexpressible','오른쪽 아래 고정된 브랜드 표제와 설명',why='cover의 허용 anchor에는 at-bottom-right가 없다. 반대 의미의 at-bottom-left 또는 일반 요소로 바꾸어 숨기지 않는다.',proposed_markup='<div class="lockup at-bottom-right" data-contract-proposal="foundation.page@2"><h1 class="title">MIRIMedi AI</h1><p class="lead">The New Vision of Radiology</p></div>')
    else:
     f=add(page,bbox,'furniture','44px 보통 굵기 다행 주 표제의 의미 구조. 일부 행의 비정상적인 폭 맞춤 효과는 별도 unexpressible 항목으로 기록한다.','head','<h1 class="title">'+parts(titletexts)+'</h1>',title_font=44,source_texts=titletexts,foreground_role=paint(titletexts[0]['style']['color'],True))
     fitted=[n for n in titleNodes if float(n['style']['size'][:-2])>60]
     if fitted:
      measurements=[{'text':n['text'],'bbox':n['bbox'],'font_size':n['style']['size'],'tracking':n['style']['tracking'],'line_height':n['style']['line']}for n in fitted]
      add(page,union([n['bbox']for n in fitted]),'unexpressible','주 표제의 행별 폭 맞춤: 실제 글자 크기 60px 초과와 큰 음수 자간이 결합된 행',why='고정 replica에는 행마다 서로 다른 font-size·line-height·큰 음수 tracking으로 폭을 맞춘 결과가 있다. foundation의 단일 title 타이포 계약으로는 이 독립 행 효과를 표현할 수 없다. 조립본의 표제는 보통 크기 44px 의미 구조를 유지하므로 해당 행은 replica와 다르다.',proposed_markup='<h1 class="title"><span class="run" data-contract-proposal="foundation.title-runs@1" data-font-ratio="source-size / title-box" data-track-ratio="source-tracking / source-size">'+escape(' / '.join(n['text']for n in fitted))+'</span></h1>',source_measurements=measurements)
  # Text-free global decorative vectors only. Never copy chart art or text as a backdrop.
  # A source-wide image placeholder is itself a page surface. Keeping only the
  # white HTML slide behind it would erase the source's inverse furniture.
  for node in v['nodes']:
   bb=node['bbox'];cc=set((node['classes']or'').split())
   if not node['text'] and ('seat'in cc or 'ph'in cc) and abs(bb[0])<1 and abs(bb[1])<1 and bb[2]>=1279 and bb[3]>=719:
    add(page,[0,0,1280,720],'background','고정 replica의 페이지 전체 사진 placeholder 면. 사진 자체는 이식하지 않고 연한 회색 자리만 보존한다.',role='--n-2',region=True,source={'selector':node['selector'],'file':'replica/slide_'+page+'.html','measurements':node['style']})
   # Independent full-bleed flat section fills are page furniture, not cards.
   # Require a text-free literal source surface and a page-edge boundary.
   elif not node['text'] and 'background:'in node['html'] and ((bb[2]>=1279 and bb[3]>=200 and abs(bb[0])<1)or(bb[3]>=719 and bb[2]>=64 and(abs(bb[0])<1 or abs(bb[0]+bb[2]-1280)<1))) and 'rgba(0, 0, 0, 0)'not in node['style']['background'] and not any(contains_box(a['bbox'],bb)for a in mapped if a.get('leaf')):
    if not(name=='cutfield'and page=='03'):
     add(page,bb,'background','페이지 가장자리까지 닿는 독립 단색 구획 면; 내부 데이터/멤버 도형은 포함하지 않는다.',role=paint(node['style']['background']),region=True,source={'selector':node['selector'],'file':'replica/slide_'+page+'.html','measurements':node['style']})
  # Descendant planes also include backgrounds defined in replica.css rather
  # than inline styles. Measurements are read-only browser captures of replica.
  planes=D/'source-planes.json'
  if planes.exists():
   for plane in json.loads(planes.read_text()).get(page,[]):
    bb=plane['bbox']
    if name=='cutfield' and page=='03':continue
    if any(a['page']==page and a['use']=='background' and all(abs(x-y)<1 for x,y in zip(a['bbox'],bb)) for a in out):continue
    if any(contains_box(a['bbox'],bb) for a in mapped if a.get('leaf')):continue
    add(page,bb,'background','중첩 DOM까지 읽어 확인한 독립 단색 페이지 구획 면. 내용 요소와 별개인 foundation 배경이다.',role=paint(plane['background']),region=True,source={'file':'replica/slide_'+page+'.html','measurements':plane})
  if name=='portico':
   vec=json.loads((D/'source-vector-dom.json').read_text())
   for g in vec.get(page,[]):
    if g.get('apparatus') in ['rail','FOOTER'] and g.get('classes')=='star':
     add(page,[round(x,4) for x in g['bbox']],'furniture','측면 레일 또는 하단 연락처 띠의 작은 방사형 점 장식','deco',source_svg=g['html'],foreground_device=True,foreground_role=paint(g['parts'][0]['fill'],True))
  for node in v['nodes']:
   c=set((node['classes'] or '').split());b=node['bbox'];tag=node['tag'].lower()
   # Tiny, text-free diagonal cuts at independent page-plane boundaries. A cut
   # inside a mapped member or unsupported panel remains that component's own.
   corner=False
   if name=='cutfield'and tag=='svg'and not node['text']and b[2]<=80 and b[3]<=80 and not owned(b):
    svg=BeautifulSoup(node['html'],'xml');paths=svg.find_all('path')
    corner=len(paths)==1 and not re.search(r'[CcQqAaSsTt]',paths[0].get('d',''))and paths[0].get('fill','none')!='none'
   if tag=='svg' and not node['text'] and (corner or ('decoration'in c and name=='lamella') or 'ribbon'in c or name=='filament' and b[2]<=60 and b[3]<=60 or name=='cutfield' and b[1]<80 and b[2]<=70):
    add(page,b,'furniture','텍스트 없는 페이지 장식 벡터. 연결선/차트/본문 도형은 포함하지 않는다.','deco',source_svg=str(BeautifulSoup((Path('/workspace/work/delivery')/name/'review/replica'/('slide_'+page+'.html')).read_text(),'html.parser').select_one('svg.'+('decoration'if name=='lamella'else'ribbon'))) if name=='lamella' or 'ribbon'in c else node['html'],source={'selector':node['selector']})
   elif name=='rulemark' and 'arr'in c:
    add(page,b,'furniture','독립 원형 방향 표시. 연결된 멤버를 가지지 않는 페이지 읽기 방향 장치.','deco',graphic='circle-chevron-down' if 'down'in c else 'circle-chevron-right',role='--page' if 'white'in c else '--ink')
  for node in v['nodes']:
   bb=node['bbox'];cc=set((node['classes']or'').split())
   if not node['text'] and ((bb[2]<=2 and bb[3]>=300)or(bb[3]<=2 and bb[2]>=600)) and not any(inside(bb,a['bbox'])for a in mapped):
    add(page,bb,'furniture','페이지 구획의 얇은 독립 괘선','deco',graphic='hairline',role=paint(node['style']['background']))
  if name=='cutfield' and page=='03':add(page,[640,0,640,720],'background','오른쪽 절반의 진한 청록 면; 왼쪽 세 카드와 별개인 페이지 구획',role='--a1-9',foreground_role='--page',region=True)
  if name=='tide-tab':add(page,[0,712,1280,8],'furniture','아래쪽8px 청록/파랑 절반 띠','deco',graphic='split-rule')
  if name=='toggle-grid':
   if page not in ['01','02']:add(page,[0,0,68,663],'furniture','왼쪽68px 회색 페이지 여백/레일 바탕','deco',graphic='gutter')
   if page=='01':add(page,[0,206,1280,514],'unexpressible','기울어진 여러 페이지 미리보기 몽타주',why='복수 페이지를 담고 원근/회전을 적용한 장면 장치다. 요소 계약이나 foundation의 단일 seat로 동일한 편집 구조를 담지 못한다.',proposed_markup='<div class="page-montage" data-contract-proposal="foundation.page@2"><div class="page-preview"></div><div class="page-preview"></div></div>')
   if page=='12':add(page,[469,-186,772,772],'furniture','hub와 표 뒤의 페이지 크기 점선 동심원3개; 연결선이 아닌 페이지 배경 장식','deco',graphic='dotted-circles',diameters=[772,580,306],center=[855,200])
 # A source-measured apparatus transfer is data, not a page-dependent CSS patch.
 proposal=D/'foundation-toggle-proposal.json'
 if name=='toggle-grid'and proposal.exists():
  proposed=json.loads(proposal.read_text())['instances']
  out=[a for a in proposed if not(a.get('use')=='furniture'and any(o.get('use')=='furniture'and o['page']==a['page']and o['bbox']==a['bbox']for o in others))]
 (D/'map-foundation.json').write_text(json.dumps({'collection':name,'group':'foundation','instances':out},ensure_ascii=False,indent=2));print(name,len(out))
if __name__=='__main__':
 for n in NAMES:mapone(n)

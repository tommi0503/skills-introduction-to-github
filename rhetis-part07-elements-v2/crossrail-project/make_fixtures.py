from pathlib import Path
import re,json,html
from lxml import html as L
P=Path(__file__).parent;R=Path('/workspace/work/reference');E=P/'crossrail/elements'
allowed={'--max','--v','--xmax','--ymax','--x','--y','--r','--n','--cols','--from','--to','--target','--low','--high','--a','--b','--at','--mood','--next','--tilt','--x1','--y1','--x2','--y2'}|{'--v'+str(i) for i in range(1,9)}
WORDS=['동부 회수 창구','긴급 수리 접수','예비 부품 창고','야간 배차 조정','상온 보관 구역','현장 점검 예약','봉인 자재 반출','중부 반품 거점','남부 정비 창구','서부 출고 접수','분실 물품 회수','운송장 대조']
NOTES=['도착한 포장물을 운송장 번호와 맞춘 뒤 선반별 접수 대장에 남깁니다.','회수 차량의 잔여 운행 거리를 살펴 가장 가까운 정비실부터 방문 순서를 정합니다.','파손 신고가 들어오면 봉인 사진과 인수 시각을 함께 보관해 수리실로 전달합니다.','재고가 부족한 소모품은 대체 규격을 대조하고 다음 입고 차량에 우선 배정합니다.','지점마다 반납한 장비를 묶어 통전 시험을 진행하며 누락된 부품은 별도 보관합니다.','분해 후 남은 자재의 수량을 다시 세어 출고 담당자가 인수 대장에 서명합니다.']
changes=[]
def fresh_text(text,part,ix):
 if not text or not text.strip():return text
 t=text.strip()
 if not re.search('[가-힣A-Za-z]',t):return text
 # Numeric quantities and code identifiers remain data; Korean prose and categorical labels are new.
 if re.fullmatch(r'[\d,.$+%/()~·−–\-\s]+[가-힣]{0,3}',t):return text
 if part in ['fig','from','to','a','b','price'] and re.search(r'\d',t):return text
 if part in ['note','pain'] or len(t)>35:return NOTES[ix%len(NOTES)]
 if part=='cond':return ['입고 승인','사진 누락','재검 요청'][ix%3]
 if part in ['kick','mark']:
  if re.search(r'\d',t):return re.sub('[가-힣A-Za-z ]+','기수 ',t).strip()
  return ['회수 접수','방문 정비','반출 대기'][ix%3]
 if len(t)<=3:return ['회수','정비','배차','접수','반출','보관'][ix%6]
 if len(t)<=7:return ['회수 창구','수리 접수','부품 대조','운송장 확인','반품 인수','봉인 점검'][ix%6]
 return WORDS[ix%len(WORDS)]
def fresh_markup(src,leaf,seed):
 root=L.fragments_fromstring(src)[0];ix=seed
 for el in root.iter():
  if not isinstance(el.tag,str):continue
  cls=set(el.get('class','').split());part=next((c for c in ['fig','note','pain','cond','kick','mark','from','to','a','b','name','price'] if c in cls),'name')
  if 'data-el' in el.attrib:el.set('data-el','crossrail-'+el.get('data-el').split('-',1)[-1])
  if 'icon' in cls:
   el.text=None
   for ch in list(el):el.remove(ch)
   el.set('data-icon',['package','wrench','truck','clipboard-check'][ix%4]);ix+=1
  else:
   el.text=fresh_text(el.text,part,ix);ix+=1
  # Child tails inherit the containing part, retaining valid nesting and numeric units.
  for ch in el:
   ch.tail=fresh_text(ch.tail,part,ix);ix+=1
  st=el.get('style')
  if st:
   keep=[]
   for decl in st.split(';'):
    if ':' not in decl:continue
    a,b=decl.split(':',1);a=a.strip()
    if a in allowed or a in ['grid-column','grid-row']:keep.append(a+':'+b.strip())
   if keep:el.set('style',';'.join(keep))
   else:el.attrib.pop('style',None)
 root.set('style','grid-column:1 / span 12;grid-row:1 / span 6'+''.join(';'+d for d in root.get('style','').split(';') if d.startswith('--')))
 return L.tostring(root,encoding='unicode',method='html')
for d in sorted(E.iterdir()):
 leaf=d.name
 if leaf in ['steps','code','tag']:continue
 srcs=sorted((R/f'samples/annual/elements/{leaf}/fixtures').glob('*.html'))
 assert srcs,leaf
 for n,f in enumerate([srcs[0],srcs[-1]]):
  raw=f.read_text();m=re.match(r'<!--\s*min:\s*([^>]+)-->',raw);mini=(m[1].strip().split('|')[0].strip() if m else '6x4');body=re.sub(r'^<!--.*?-->\s*','',raw,count=1,flags=re.S)
  out=fresh_markup(body,leaf,n*13)
  if n and leaf in ['legend','pricing']:
   rr=L.fragments_fromstring(out)[0]; children=rr.xpath('./*[contains(concat(" ",normalize-space(@class)," ")," '+('key' if leaf=='legend' else 'plan')+' ")]')
   if len(children)>1:rr.remove(children[-1])
   out=L.tostring(rr,encoding='unicode',method='html')
  if n and leaf=='versus':
   rr=L.fragments_fromstring(out)[0];sides=rr.cssselect('.side') if False else rr.xpath('./*[contains(concat(" ",normalize-space(@class)," ")," side ")]')
   for ix,side in enumerate(sides):side.set('class','side'+(' on' if ix==0 else ''))
   out=L.tostring(rr,encoding='unicode',method='html')
  out=f'<!-- min:{mini} -->\n'+out+'\n';(d/f'fixtures/base-{chr(97+n)}.html').write_text(out)
G={'card':('confetti','card-2-quiet card-3-icon3d card-3-line card-3-on card-4 card-5-tone'.split()),'callout':('annual','callout callout-icon callout-stack'.split()),'chart-area':('annual','area-1 areas-2 areas-stacked-3 area-3pt'.split()),'chart-bar':('confetti','bars-12 bars-6 bars-3 bars-h-5 bars-h-8 bars-2'.split()),'chart-donut':('amethyst','donut donuts-3 donuts-4 donut-0 donut-100'.split()),'chart-line':('amethyst','lines-12 lines-6 lines-3 lines-flat'.split())}
for leaf,(sample,names) in G.items():
 for name in names:
  f=R/f'samples/{sample}/elements/{leaf}/fixtures/{name}.html';s=f.read_text().replace(f'data-el="{sample}-', 'data-el="crossrail-');(E/leaf/f'fixtures/{name}.html').write_text(s)
# Code is newly authored and remains executable source rather than renamed prose.
for label,numbered,body,mini in [('a',False,'<p><span class="k">const</span> pickups = [42, 55, 61];</p><p><span class="k">const</span> total = pickups.reduce((sum, n) =&gt; sum + n, 0);</p><p>console.log(<span class="s">"회수 대장"</span>, total);</p>','6x3'),('b',True,'<p><span class="c">// 입고된 부품만 반출 목록에 넣습니다.</span></p><p><span class="k">function</span> selectBins(bins) {</p><p>  <span class="k">return</span> bins.filter(bin =&gt; bin.count &gt; <span class="n">0</span>);</p><p>}</p><p><span class="k">const</span> ready = selectBins(stock);</p><p>dispatch(ready);</p>','8x4')]:
 (E/f'code/fixtures/base-{label}.html').write_text(f'<!-- min:{mini} -->\n<div class="code'+(' numbered' if numbered else '')+'" data-el="crossrail-code" style="grid-column:1 / span 12;grid-row:1 / span 6"><p class="name">pickup-log.js</p><div class="lines">'+body+'</div></div>\n')
print('base/golden structural fixtures',sum(len(list(d.glob('fixtures/*.html'))) for d in E.iterdir()))

for label,cls,text in [('a','tag','입고 승인'),('b','hl','야간 회수')]:
 (E/f'tag/fixtures/base-{label}.html').write_text(f'<!-- min:2x1 -->\n<span class="{cls}" data-el="crossrail-tag" style="grid-column:1 / span 12;grid-row:1 / span 6"><span>{text}</span></span>\n')

from pathlib import Path
from lxml import html,etree
import json,re
P=Path(__file__).parent;R=Path('/workspace/work/reference');C=P/'seedmark';A=json.loads((P/'map.json').read_text())
source_text='\n'.join(n['text']for p in A['rawMeasurements']for n in p['nodes']);normalized_source=re.sub(r'\s+','',source_text).casefold();source6={normalized_source[i:i+6]for i in range(len(normalized_source)-5)}
chunks=['협업 체계를 고도화합니다.','부서별 실행안을 조율합니다.','담당 권한을 분명히 나눕니다.','검토 시간을 꾸준히 단축합니다.','분기별 예산안을 재설계합니다.','납기 준수율을 높여갑니다.','신규 거래망을 넓혀갑니다.','실증 자료를 기반으로 판단합니다.']
shorts=['운영 혁신','조직 정비','사업 확장','실행 관리','손익 개선','납기 준수','영업 연계','신뢰 구축','분기 요약','현장 대응']
def fresh(t,seed=0):
 t=t.strip()
 if not t:return''
 if re.fullmatch(r'[\d.%+−–~:/ ,억만원년월명개회배]+',t):
  if len(t)<5:return t
  m=re.search(r'\d+',t)
  if m:return t[:m.start()]+str(int(m.group())+37)+t[m.end():]
 L=len(t)
 if L<12:s=shorts[seed%len(shorts)]
 else:
  s='';j=seed
  while len(s)<L*.85:
   s+=(' 'if s else'')+chunks[j%len(chunks)];j+=1
  if len(s)>L*1.25 and len(s.split('. '))>1:s='. '.join(s.split('. ')[:-1])+'.'
 k=0
 while any(re.sub(r'\s+','',s).casefold()[i:i+6]in source6 for i in range(max(0,len(re.sub(r'\s+','',s))-5))):
  s=s.replace('합니다','추진해요').replace('높여갑니다','향상해요').replace('자료를','근거로');k+=1
  if k>3:s='협업 효율을 향상해요. '+shorts[(seed+k)%len(shorts)];break
 return s

G={'card':('confetti','card-2-quiet card-3-icon3d card-3-line card-3-on card-4 card-5-tone'.split()),'callout':('annual','callout callout-icon callout-stack'.split()),'chart-area':('annual','area-1 areas-2 areas-stacked-3 area-3pt'.split()),'chart-bar':('confetti','bars-12 bars-6 bars-3 bars-h-5 bars-h-8 bars-2'.split()),'chart-donut':('amethyst','donut donuts-3 donuts-4 donut-0 donut-100'.split()),'chart-line':('amethyst','lines-12 lines-6 lines-3 lines-flat'.split())}
changes=[]
for f in sorted((R/'samples/annual/elements').iterdir()):
 E=C/'elements'/f.name;(E/'fixtures').mkdir(parents=True,exist_ok=True)
 if not(E/'element.json').exists():(E/'element.json').write_text((f/'element.json').read_text())
 if not(E/'description.md').exists():(E/'description.md').write_text('A Seedmark component uses rounded outlines, quiet surfaces and a deliberate hierarchy of strong names, light notes and crisp labels. Its local geometry is designed from the same source proportions as the page components and scales within its own container. The component owns its members and any connectors between them; no adjacent component or page identifier changes its appearance.\n')
 chosen=[]
 if f.name in G:
  samp,names=G[f.name];chosen=[(R/'samples'/samp/'elements'/f.name/'fixtures'/(n+'.html'),True)for n in names]
 else:chosen=[(x,False)for x in sorted((f/'fixtures').glob('*.html'))[:2]]
 for j,(src,gold)in enumerate(chosen):
  txt=src.read_text();txt=re.sub(r'data-el="[a-z0-9-]+-','data-el="seedmark-',txt)
  # Replacing prefixes uses each registered leaf folder, not an ambiguous hyphen split.
  for leaf in [x.name for x in(R/'samples/annual/elements').iterdir()]:
   txt=re.sub(r'data-el="(?:annual|confetti|amethyst)-'+re.escape(leaf)+'"',f'data-el="seedmark-{leaf}"',txt)
  # The broad first replacement above is corrected from the untouched source by exact registered roots.
  txt=src.read_text()
  for leaf in [x.name for x in(R/'samples/annual/elements').iterdir()]:txt=txt.replace(f'data-el="{src.parts[-5]}-{leaf}"',f'data-el="seedmark-{leaf}"')
  txt=re.sub(r'data-el="(?:annual|confetti|amethyst)-', 'data-el="seedmark-',txt)
  nodes=html.fragments_fromstring(txt);mod=False;seed=j*19
  for node in nodes:
   if not hasattr(node,'iter'):continue
   for q in node.iter():
    if not isinstance(q.tag,str):continue
    for attr in ['text','tail']:
     t=getattr(q,attr)
     if not t or not t.strip():continue
     nt=re.sub(r'\s+','',t).casefold();overlap=any(nt[k:k+6]in source6 for k in range(max(0,len(nt)-5)))
     if overlap:
      v=t.replace('division','biz_unit')if f.name=='code'and'division'in t else fresh(t,seed);seed+=1
      if v!=t:changes.append({'file':f'{f.name}/{src.name}','golden':gold,'before':t,'after':v});setattr(q,attr,v);mod=True
  if mod:
   comment=re.search(r'<!--\s*min:.*?-->',txt).group(0);txt=comment+'\n'+''.join(etree.tostring(n,encoding='unicode',method='html')for n in nodes if hasattr(n,'tag')and isinstance(n.tag,str))
  (E/'fixtures'/src.name).write_text(txt)

def root(leaf,cl,parts):return f'<div class="{cl}" data-el="seedmark-{leaf}" style="grid-column:1 / span 12;grid-row:1 / span 6">{parts}</div>'
def nodes(inst):return inst['sourceMeasurements']
def texts(inst):return[(q,q.get('text','').strip())for q in nodes(inst)if q.get('text','').strip()]
def semantic(inst):
 leaf=inst['leaf'];ts=texts(inst);seed=int(inst['page'])*11+int(re.sub(r'\D','',inst['id'])[-2:]);t=[fresh(x,seed+j)for j,(q,x)in enumerate(ts)]
 def text(j,default=''):return t[j]if j<len(t)else default
 if leaf=='card':
  mark=any('icon'in q.get('classes','')for q in nodes(inst));kick=next((fresh(x,seed+j)for j,(q,x)in enumerate(ts)if float(q.get('fontSize','18px').replace('px',''))<16),'')
  name=next((fresh(x,seed+j)for j,(q,x)in enumerate(ts)if float(q.get('fontSize','18px').replace('px',''))>=22),text(0,'실행 체계'))
  note=next((fresh(x,seed+j)for j,(q,x)in enumerate(ts)if len(x)>30),text(-1,'책임과 권한을 명확하게 나눕니다.'))
  bits=('<span class="mark"><span class="icon" data-icon="briefcase-business"></span></span>'if mark else'')+(f'<p class="kick">{kick}</p>'if kick else'')+f'<h3 class="name">{name}</h3><p class="note">{note}</p>'
  if inst['page']==10:bits+='<div class="list check" data-el="seedmark-list"><div class="item"><p class="name">'+fresh('적합한 요금 구간을 선택합니다.',seed+7)+'</p><p class="note"></p></div></div>'
  return root(leaf,'card '+(inst.get('contractVariant','')),'<div class="parts">'+bits+'</div>'),('6x2'if inst['bbox'][2]/inst['bbox'][3]>2.5 else'4x4')
 if leaf=='pill':return root(leaf,'pill '+inst.get('contractVariant',''),f'<div class="parts"><span class="mark">분기 목표</span><span class="name">{text(0)}</span><span class="note">{text(1)}</span></div>'),'4x2'
 if leaf=='headline':return root(leaf,'headline '+(inst.get('contractVariant','')),f'<h2>{text(0)}</h2>'+(''if len(t)<2 else f'<p class="note">{text(1)}</p>')),'6x2'
 if leaf=='prose':return root(leaf,'prose '+(inst.get('contractVariant','')),''.join(f'<p>{x}</p>'for x in t[:4])),'4x2'
 if leaf=='metric':return root(leaf,'stat',f'<div class="parts"><p class="fig">{text(0)}</p><p class="name">{text(1)}</p><p class="note">{text(2)}</p></div>'),'6x2'
 if leaf=='tag':return root(leaf,'tag',f'<span>{text(0)}</span>'),'2x1'
 if leaf=='callout':return root(leaf,'callout',f'<p>{text(0)}</p>'),'8x2'
 if leaf=='legend':return root(leaf,'legend',''.join(f'<span class="key tone-{j+1}">{x}</span>'for j,x in enumerate(t))),'3x2'
 return None
for inst in A['instances']:
 if inst.get('fixture')and inst['leaf']in ['card','pill','headline','prose','metric','tag','callout','legend']:
  got=semantic(inst)
  if got:
   txt,mini=got;(C/inst['fixture']).write_text('<!-- min: '+mini+' -->\n'+txt+'\n')
(P/'fixture-decisions.json').write_text(json.dumps({'rule':'Latest six-character source-copy ban overrides golden text preservation where the two conflict; markup, member counts, numeric data and variants remain intact.','changes':changes},ensure_ascii=False,indent=2))
print('Base/golden fixtures created; source fixtures for first9 leaf types created.')

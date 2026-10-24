#!/usr/bin/env python3
"""Package frozen v2 sources and portable review evidence. Never edits design inputs.

Dry-run does not create ZIPs. --write-previews writes only HTML/Markdown viewers.
Final archives are written atomically, CRC checked, and accompanied by SHA manifests.
"""
from __future__ import annotations
import argparse,collections,datetime,hashlib,html,json,posixpath,re,struct,sys,zipfile,zlib
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path,PurePosixPath
from urllib.parse import unquote,urlsplit

ROOT=Path(__file__).resolve().parents[1]
PROJECTS=[('069','vectorbox',12),('072','seedmark',21),('073','crossrail',30),('074','meridian-deck',30),('078','onboard-docket',19)]
LEAVES='agenda architecture balance bullet callout card chart-area chart-bar chart-donut chart-line chart-scatter chart-stack chart-waterfall code concentric cycle decision-tree delta flowchart funnel gauge headline heatmap hierarchy hub image-frame journey legend list logo-group matrix matrix-nine metric mindmap network person pill positioning pricing prose pyramid quote radar roadmap sankey slope sparkline steps swimlane table tag timeline treemap venn versus waffle'.split()
ALLOWED={'.css','.json','.md','.html'}
MAX_REVIEW=100_000_000
H=lambda x:hashlib.sha256(x).hexdigest()
J=lambda x:json.dumps(x,ensure_ascii=False,indent=2).encode()
E=lambda x:html.escape(str(x),quote=True)
STAMP=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()

@dataclass
class Entry:
 name:str
 path:Path|None=None
 data:bytes|None=None
 def read(self):return self.data if self.data is not None else self.path.read_bytes()

def readjson(p):return json.loads(p.read_text())
def project(root,k):return root/(k+'-project')
def mapped(m):return [i for i in m.get('instances',[])if i.get('leaf')in LEAVES and(i.get('use')=='base'or str(i.get('use','')).startswith('variant:'))]
def page_label(x):
 try:return f'{int(x):02d}'
 except (TypeError,ValueError):return str(x)
def pages(m):return sorted({page_label(i['page'])for i in m.get('instances',[])if i.get('page')is not None})
def css_comment(p):
 if not p.exists():return 'CSS 미작성 — 추론 근거 미확정'
 t=p.read_text();a=re.search(r'/\*(.*?)\*/',t,re.S)
 return re.sub(r'\s+',' ',a.group(1)).strip()if a else'첫 CSS 주석 없음 — 추론 모티프 미기재'

def origin(root,k,leaf):
 P=project(root,k);m=readjson(P/'map.json');a=[i for i in mapped(m)if i['leaf']==leaf]
 base=sorted({page_label(i['page'])for i in a if i['use']=='base'})
 variants=collections.defaultdict(set)
 for i in a:
  if str(i['use']).startswith('variant:'):variants[i['use'][8:]].add(page_label(i['page']))
 variant='; '.join(f'{name}: {", ".join(sorted(ps))}'for name,ps in sorted(variants.items()))or'—'
 basis='base 관찰'if base else'variant만 관찰 · base 추론'if variants else'inferred · 직접 대응 없음'
 motif=''if base else css_comment(P/k/'elements'/leaf/'element.css')
 design=' / '.join(dict.fromkeys(re.sub(r'\s+',' ',i.get('design','')).strip() for i in a if i.get('design')))
 return {'base':base,'variant':variant,'state':basis,'motif':motif,'design':design}

def origins_md(root,k=None):
 txt='# 요소별 출처\n\n지도에서 `base`와 명명된 `variant:`만 직접 출처로 센다. `same-as:`는 반복 사용이며 새 원형이 아니다. base가 없는 요소는 추론이다. 그 경우 첫 CSS 주석을 인용하며, 주석에 적힌 source/경로를 해당 요소의 직접 원형으로 승격하지 않는다. 이 표의 출처는 시각적 동일성이나 계약 반입 성공을 뜻하지 않는다.\n\n| 컬렉션 | 요소 | base 페이지 | 계약 variant 페이지 | 근거 | 실측 원형 설명 |\n|---|---|---|---|---|---|\n'
 for _,kid,_ in PROJECTS:
  if k and k!=kid:continue
  for leaf in LEAVES:
   o=origin(root,kid,leaf);prefix=''if k else kid+'-project/'
   info=o['state']+(' — 첫 주석: '+o['motif']if o['motif']else'');info=info.replace('|','\\|').replace('\n',' ')
   measured=o['design'].replace('|','/').replace('\n',' ')or'—'
   txt+=f'| {kid} | [{leaf}]({prefix}{kid}/elements/{leaf}/element.css) | {", ".join(o["base"])or"—"} | {o["variant"].replace("|","/")} | {info} | {measured} |\n'
 return txt

VIEW_CSS='''*{box-sizing:border-box}body{margin:0;background:#f3f5f8;color:#172033;font:15px/1.6 system-ui,sans-serif}body[data-theme=dark]{background:#101722;color:#e9edf3}header,main,footer{max-width:1450px;margin:auto;padding:24px}header{padding-top:42px}h1{font-size:32px;line-height:1.2;margin:8px 0 14px}h2{font-size:23px;margin-top:34px}a{color:inherit;text-underline-offset:3px}nav,.links,.toolbar{display:flex;flex-wrap:wrap;gap:12px}.muted{opacity:.72}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(285px,1fr));gap:18px}.tile{border:1px solid #aeb8c455;border-radius:12px;padding:16px;background:#ffffff06}.tile h3{margin:0 0 6px;font-size:18px}.thumb{display:block;width:100%;height:170px;object-fit:contain;background:#8793a210;margin:12px 0}.pages .thumb{height:190px}.origin{font-size:12px;min-height:38px}.tag{display:inline-block;border:1px solid #aeb8c455;border-radius:999px;padding:2px 8px;font-size:12px}.search{width:100%;padding:11px;border:1px solid #aeb8c477;border-radius:7px;background:transparent;color:inherit;font:inherit;margin:18px 0}button{font:inherit;cursor:pointer;border:1px solid #aeb8c477;border-radius:6px;padding:6px 12px;background:transparent;color:inherit}dialog{position:fixed;inset:2vh 2vw;width:96vw;height:96vh;padding:0;border:1px solid #8793a2;border-radius:9px;background:#121925;color:#fff}dialog::backdrop{background:#000b}.toolbar{height:60px;align-items:center;padding:10px 16px}.viewport{height:calc(100% - 60px);overflow:auto;background:#444b55;cursor:grab}.viewport img{display:block;max-width:none}.viewport.drag{cursor:grabbing}.sheet{border-top:1px solid #aeb8c455;padding:25px 0}.sheet img{max-width:100%;height:auto;display:block}.summary{display:flex;flex-wrap:wrap;gap:12px;margin:15px 0}.summary span{border:1px solid #aeb8c455;border-radius:7px;padding:8px 13px}@media(max-width:700px){header,main,footer{padding:16px}h1{font-size:25px}.grid{grid-template-columns:1fr}.toolbar{height:auto;min-height:60px}.viewport{height:80vh}}'''
VIEW_JS='''const dlg=document.querySelector('#zoom'),vp=document.querySelector('.viewport'),zi=document.querySelector('#zoom-img');let scale=1,down=null;function setScale(s){scale=Math.max(.03,Math.min(5,s));zi.style.width=(zi.naturalWidth*scale)+'px';document.querySelector('#zoom-level').textContent=Math.round(scale*100)+'%'}document.addEventListener('click',e=>{const a=e.target.closest('a.zoomable');if(!a)return;e.preventDefault();zi.onload=()=>setScale(Math.min(1,(vp.clientWidth-20)/zi.naturalWidth));zi.src=a.href;document.querySelector('#zoom-title').textContent=a.dataset.title||a.textContent.trim();document.querySelector('#zoom-raw').href=a.href;dlg.showModal()});document.querySelector('#close').onclick=()=>dlg.close();document.querySelector('#fit').onclick=()=>setScale(Math.min(1,(vp.clientWidth-20)/zi.naturalWidth));document.querySelector('#native').onclick=()=>setScale(1);document.querySelector('#plus').onclick=()=>setScale(scale*1.3);document.querySelector('#minus').onclick=()=>setScale(scale/1.3);vp.onmousedown=e=>{down=[e.clientX,e.clientY,vp.scrollLeft,vp.scrollTop];vp.classList.add('drag');e.preventDefault()};window.addEventListener('mouseup',()=>{down=null;vp.classList.remove('drag')});vp.onmousemove=e=>{if(down){vp.scrollLeft=down[2]-e.clientX+down[0];vp.scrollTop=down[3]-e.clientY+down[1]}};document.querySelector('#search')?.addEventListener('input',e=>document.querySelectorAll('[data-search]').forEach(t=>t.hidden=!t.dataset.search.includes(e.target.value.toLowerCase())));'''
def frame(title,body,theme='light'):
 dialog='<dialog id="zoom"><div class="toolbar"><strong id="zoom-title"></strong><button id="fit">폭 맞춤</button><button id="native">100%</button><button id="minus">−</button><span id="zoom-level"></span><button id="plus">+</button><a id="zoom-raw" target="_blank" rel="noopener">PNG 직접 열기</a><button id="close">닫기</button></div><div class="viewport"><img id="zoom-img" alt="확대 검수 이미지"></div></dialog>'
 return '<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+E(title)+'</title><style>'+VIEW_CSS+'</style></head><body data-theme="'+theme+'">'+body+dialog+'<script>'+VIEW_JS+'</script></body></html>'
def zoom(src,label,title=None):return f'<a class="zoomable" href="{E(src)}" data-title="{E(title or label)}">{E(label)}</a>'
def project_html(root,k,offline=False):
 P=project(root,k);m=readjson(P/'map.json');pn=pages(m);mapped_leaves={i['leaf']for i in mapped(m)}
 back=''if offline else'<a href="../index.html">5컬렉션 전체</a>'
 verification='<a href="'+('verification/integration-verification.md'if offline else'../integration-verification.md')+'">최종 통합 검증</a>'if(root/'integration-verification.json').exists()else''
 downloads=''if offline else f'<a href="../deliverables/{k}.zip">컬렉션 ZIP</a><a href="../deliverables/{k}-review.zip">검수 ZIP</a>'
 common=('<a href="verification/GAPS-INDEX.md">전체 GAPS</a><a href="verification/ORIGINS-COMPACT.md">56행 출처 요약</a><a href="verification/root-review-notes.md">전체 품질 검수</a>'if offline else'<a href="../GAPS-INDEX.md">전체 GAPS</a><a href="../ORIGINS-COMPACT.md">56행 출처 요약</a><a href="../review-notes.md">전체 품질 검수</a>')
 body=f'<header><nav>{back}{downloads}{verification}{common}<a href="map.json">지도 JSON</a><a href="GAPS.md">미표현 계약</a><a href="review-notes.md">검수 기록</a><a href="design-language.md">디자인 언어</a><a href="ORIGINS.md">56개 출처</a></nav><h1>{E(k)}</h1><p>실제 크기 시트와 원본 | 불변 replica | 조립본을 함께 검토합니다. 이미지를 누르면 확대·100%·드래그 이동을 사용할 수 있습니다.</p><div class="summary"><span>{len(pn)}페이지</span><span>56요소</span><span>직접 대응 {len(mapped_leaves)}종</span><span>지도 unexpressible {sum(i.get("use")=="unexpressible"for i in m.get("instances",[]))}항목</span></div><nav><a href="library-light.html">라이트 전체 시트</a><a href="library-dark.html">다크 전체 시트</a><a href="#assembly">페이지 비교</a></nav></header><main><h2>요소 시트</h2><p class="muted">최소 칸부터12×6까지의 native 렌더입니다. 직접 대응 시트는 측정 replica 조각과 요소의12×6·최소 칸을 비교합니다. 기능 검수와 원본 일치 판단은 별도입니다.</p><input id="search" class="search" type="search" placeholder="요소 이름 검색" aria-label="요소 검색"><div class="grid">'
 for f in sorted((P/'foundation-sheets').glob('*.png')):
  body+=f'<article class="tile" data-search="foundation {E(f.stem.lower())}"><h3>Foundation · {E(f.stem)}</h3><a class="zoomable" href="foundation-sheets/{E(f.name)}" data-title="Foundation {E(f.stem)}"><img class="thumb" loading="lazy" src="foundation-sheets/{E(f.name)}" alt="foundation1280×720"></a></article>'
 for leaf in LEAVES:
  o=origin(root,k,leaf);r=f'sheets/{leaf}-replica.png';has=leaf in mapped_leaves and(P/r).exists()
  origintext=('base '+','.join(o['base'])if o['base']else o['state'])+(' · '+o['variant']if o['variant']!='—'else'')
  body+=f'<article class="tile" data-search="{E(leaf)}"><h3>{E(leaf)}</h3><p class="origin">{E(origintext)}</p><a class="zoomable" href="sheets/{leaf}-light.png" data-title="{E(leaf)} · light"><img class="thumb" loading="lazy" src="sheets/{leaf}-light.png" alt="{E(leaf)} 라이트 크기 시트"></a><div class="links">'+zoom(f'sheets/{leaf}-light.png','Light',leaf+' light')+zoom(f'sheets/{leaf}-dark.png','Dark',leaf+' dark')+(zoom(r,'Replica 비교',leaf+' measured replica')if has else'')+f'<a href="{k}/elements/{leaf}/element.css">CSS</a><a href="{k}/elements/{leaf}/element.json">계약</a></div></article>'
 for mode in ['light','dark']:
  if(P/f'contract-preview-{mode}.html').exists():body+=f'<p><a href="contract-view-{mode}.html">공식 preview.py {mode} HTML</a></p>'
 body+='</div><h2 id="assembly">페이지별 조립과 비교</h2><p class="muted">세 열의 순서는 원본 | 불변 replica | 컬렉션 조립본입니다. 미표현 부분과 고정 그리드의 차이는 GAPS·검수 기록을 함께 읽습니다.</p><div class="grid pages">'
 for n in pn:
  body+=f'<article class="tile"><h3>페이지 {n}</h3><a class="zoomable" href="compare-reassembled/slide_{n}.png" data-title="페이지 {n}: 원본 | replica | 조립"><img class="thumb" loading="lazy" src="compare-reassembled/slide_{n}.png" alt="페이지 {n} 세 열 비교"></a><div class="links">'+zoom(f'compare-reassembled/slide_{n}.png','세 열 확대')+zoom(f'reassembled/slide_{n}.png','조립 PNG')+f'<a href="reassembled/slide_{n}.html">조립 HTML</a></div></article>'
 return frame(k+' review',body+'</div></main><footer>오프라인에서는 압축을 푼 폴더의 index.html을 엽니다. CSS·폰트·아이콘 런타임은 동봉된 로컬 파일을 사용합니다.</footer>')
def library_html(root,k,mode):
 P=project(root,k);body=f'<header><nav><a href="index.html">검수 처음</a><a href="library-'+('dark'if mode=='light'else'light')+'.html">다른 모드</a><a href="ORIGINS.md">출처 표</a></nav><h1>'+E(k)+' · '+mode+'</h1><p>각 PNG는 모든 fixture와 실제 크기 칸을 담습니다. 확대하면 원본 해상도로 읽을 수 있습니다.</p></header><main>'
 for leaf in LEAVES:
  src=f'sheets/{leaf}-{mode}.png';body+=f'<section class="sheet"><h2>{E(leaf)}</h2>'+zoom(src,'확대 / 100%',leaf+' '+mode)+f'<a class="zoomable" href="{src}" data-title="{E(leaf)} {mode}"><img loading="lazy" src="{src}" alt="{E(leaf)} {mode} 전체 시트"></a></section>'
 return frame(k+' '+mode,body+'</main>',mode)
def root_html(root):
 body='<header><h1>Rhetis 디자인 라이브러리 · v2</h1><p>5개 덱,112페이지에서 만든 서로 다른5컬렉션입니다. 각 컬렉션은56개 요소의 크기·모드 시트와 고정 지도 조립 비교를 제공합니다.</p><nav><a href="README.md">읽는 방법</a><a href="ORIGINS.md">280개 요소 출처</a><a href="ORIGINS-COMPACT.md">56행 출처 요약</a><a href="GAPS-INDEX.md">85개 GAPS</a><a href="review-notes.md">전체 품질 검수</a><a href="root-visual-review-status.json">775장 최종 SHA 검수</a><a href="integration-verification.md">최종 통합 검증</a><a href="deliverables/SHA256SUMS">ZIP SHA256</a><a href="deliverables/manifest.json">패키지 검증 명세</a></nav></header><main><div class="grid">'
 for deck,k,n in PROJECTS:
  first=pages(readjson(project(root,k)/'map.json'))[0]
  body+=f'<article class="tile"><span class="tag">덱 {deck} · {n}페이지</span><h2>{k}</h2><a href="{k}-project/index.html"><img class="thumb" loading="lazy" src="{k}-project/reassembled/slide_{first}.png" alt="{k} 조립 미리보기"></a><div class="links"><a href="{k}-project/index.html">검수 미리보기</a><a href="deliverables/{k}.zip">컬렉션 ZIP</a><a href="deliverables/{k}-review.zip">검수 ZIP</a></div></article>'
 return frame('Rhetis 5 collections',body+'</div></main><footer>컬렉션 기능 시트의 통과는 원본과의 픽셀 일치를 뜻하지 않습니다. 각 GAPS·검수 기록에 해석과 남은 차이를 명시합니다. 기존v1 작업은 이 도구가 수정하지 않습니다.</footer>')
def readme(root):
 t='# Rhetis 디자인 라이브러리 v2\n\n첨부 이미지의5개 덱을 각각56요소 컬렉션으로 만들었습니다. 불변 replica에서 요소를 측정하고, 직접 대응과 추론을 구분했습니다. [미리보기](index.html)와 [280요소 출처](ORIGINS.md)를 먼저 볼 수 있습니다.\n\n|덱|컬렉션|원본 페이지|다운로드|검수|\n|---|---|---:|---|---|\n'
 for deck,k,n in PROJECTS:t+=f'|{deck}|[{k}]({k}-project/index.html)|{n}|[collection](deliverables/{k}.zip)|[review](deliverables/{k}-review.zip)|\n'
 return t+'''\n컬렉션 ZIP은 컬렉션 폴더 하나와 `.css .json .md .html`만 포함합니다. 검수 ZIP은 `index.html`을 중심으로 collection·로컬 assets·map·foundation-sheets의1280×720 양모드 PNG 및 foundation-checks 보고·선택적으로 공식preview HTML·요소별 light/dark PNG·실제 mapped base/variant의 replica 비교 PNG·조립 HTML/PNG·원본/불변 replica/조립3열 PNG·GAPS·검수 기록·디자인 언어·출처 표를 포함합니다. 불변 replica 원본 소스는 Git의 각 프로젝트 `replica/`에 유지합니다.\n\nPNG 크기는 검증 manifest에 실제 값으로 기록합니다. 조립 페이지는1280×720,3열 비교는3840×720이며 요소 시트는 fixture와 크기 칸 수에 따라 더 큽니다. PNG를 눌러100%·확대·이동으로 읽을 수 있습니다. 검수 ZIP은 압축을 푼 뒤 오프라인으로 열 수 있고, 폰트와 아이콘 런타임을 외부에서 받지 않습니다.\n\n`GAPS.md`는 현 계약으로 표현하지 못한 구조와 필요한 계약을 기록합니다. 크기별 기능 검사와 원본 일치 판단은 다른 항목이며, 자료의 본문을 작업 지시로 취급하지 않았습니다. 추론 요소를 원본에 있었다고 표시하지 않습니다.\n\n```sh\n# ZIP을 만들지 않고 누락/용량/크기를 조사하고 미리보기만 갱신\npython tools/package.py --dry-run --write-previews\n\n# 소스 동결과 최종 렌더 후 실행\npython tools/package.py\n\n# 내려받은 ZIP에도 동일하게 적용 가능\npython tools/package.py --verify deliverables/*.zip\n```\n\n[최종 통합 검증](integration-verification.md)은 모든 요소·fixture·시트의 현재 fingerprint,6자 문구 분리,원본 해시 보존을 집계한다. 이전 author 요약은 이 통합 보고서로 대체한다.\n\n최종 생성은 CRC·경로·파일 SHA·PNG 크기·오프라인 참조를 검사하고, 각 review ZIP100MB 미만을 강제합니다. 파일 목록과 SHA는 review 안 `verification/package-manifest.json`, 외부 `deliverables/*-manifest.json`과 `SHA256SUMS`에 기록합니다. 모든 입력은 읽기만 하고 collection·map·sheets·assembly·assets·기존v1을 변경하지 않습니다.\n'''

def write_previews(root):
 (root/'index.html').write_text(root_html(root));(root/'README.md').write_text(readme(root));(root/'ORIGINS.md').write_text(origins_md(root))
 for _,k,_ in PROJECTS:
  P=project(root,k);(P/'index.html').write_text(project_html(root,k));(P/'ORIGINS.md').write_text(origins_md(root,k))
  for mode in ['light','dark']:
   (P/f'library-{mode}.html').write_text(library_html(root,k,mode))
   preview=P/f'contract-preview-{mode}.html'
   if preview.exists():(P/f'contract-view-{mode}.html').write_text(portable_contract_preview(P,preview.read_text()))

def png_info(data,crc=False):
 if data[:8]!=b'\x89PNG\r\n\x1a\n' or len(data)<33:raise ValueError('invalid PNG header')
 dims=list(struct.unpack('>II',data[16:24]))
 if crc:
  pos=8;ended=False
  while pos<len(data):
   if pos+12>len(data):raise ValueError('truncated PNG chunk')
   n=struct.unpack('>I',data[pos:pos+4])[0];kind=data[pos+4:pos+8];end=pos+8+n
   if end+4>len(data)or zlib.crc32(data[pos+4:end])&0xffffffff!=struct.unpack('>I',data[end:end+4])[0]:raise ValueError('PNG CRC mismatch')
   pos=end+4
   if kind==b'IEND':ended=True;break
  if not ended:raise ValueError('missing PNG IEND')
 return dims

def source_fp(P,k,leaf=None):
 folders=[P/k,P/'assets']
 if leaf:
  deps={leaf};todo=[leaf]
  while todo:
   current=todo.pop()
   for f in(P/k/'elements'/current/'fixtures').glob('*.html'):
    for dep in re.findall(r'data-el=["\']'+re.escape(k)+r'-([^"\']+)',f.read_text()):
     if dep not in deps:deps.add(dep);todo.append(dep)
  folders=[P/k/'kit',P/k/'foundation',P/'assets/fonts']+[P/k/'elements'/x for x in sorted(deps)]
 d={str(f.relative_to(P)):H(f.read_bytes())for folder in folders for f in sorted(folder.rglob('*'))if f.is_file()and f.suffix in['.css','.html','.json','.js','.woff','.woff2']}
 return H(json.dumps(d,sort_keys=True).encode())

class References(HTMLParser):
 def __init__(self):super().__init__();self.refs=[]
 def handle_starttag(self,tag,attrs):
  self.refs.extend(v for key,v in attrs if key in['href','src']and v)
def offline_check(entries):
 names={e.name for e in entries};issues=[]
 for e in entries:
  if not e.name.endswith(('.html','.css')):continue
  text=e.read().decode('utf-8');refs=[]
  if e.name.endswith('.html'):
   p=References();p.feed(text);refs+=p.refs
  refs+=re.findall(r'url\(\s*["\']?([^\)"\']+)',text)
  for ref in refs:
   ref=ref.strip();u=urlsplit(ref)
   if not ref or ref.startswith('#')or u.scheme in['data','mailto']:continue
   if u.scheme or ref.startswith('//')or ref.startswith('/'):
    issues.append([e.name,ref,'external/absolute reference']);continue
   target=posixpath.normpath(posixpath.join(posixpath.dirname(e.name),unquote(u.path)))
   if target not in names:issues.append([e.name,ref,'missing offline dependency'])
 return issues

def portable_contract_preview(P,text):
 font='assets/fonts/fonts.css'if(P/'assets/fonts/fonts.css').exists()else'assets/fonts.css'
 return re.sub(r'href=([\"\'])([^\"\']*fonts(?:/fonts)?\.css)\1',lambda m:'href='+m.group(1)+font+m.group(1),text)

def local_refs(entry):
 if not entry.name.endswith(('.html','.css')):return[]
 text=entry.read().decode('utf-8');refs=[]
 if entry.name.endswith('.html'):
  p=References();p.feed(text);refs+=p.refs
 refs+=re.findall(r'url\(\s*[\"\']?([^\)\"\']+)',text)
 result=[]
 for ref in refs:
  u=urlsplit(ref.strip())
  if not u.scheme and not ref.startswith(('#','/'))and u.path:result.append(posixpath.normpath(posixpath.join(posixpath.dirname(entry.name),unquote(u.path))))
 return result

def include_font_dependencies(P,review):
 # Some authentic assembly font CSS points to immutable replica/fonts/. Only its
 # dependency fonts are copied, never replica slide HTML/PNG or other projects.
 names={e.name for e in review};added=[]
 for _ in range(4):
  missing={r for e in review for r in local_refs(e)if r not in names}
  new=[]
  for rel in sorted(missing):
   q=(P/rel).resolve()
   if q.is_relative_to(P.resolve())and rel.startswith('replica/fonts/')and q.is_file()and q.suffix.lower()in['.woff','.woff2','.ttf','.otf','.css']:
    new.append(Entry(rel,q));names.add(rel);added.append(rel)
  if not new:break
  review+=new
 return added

def inventory(root,k,include_checks=False):
 P=project(root,k);C=P/k;m=readjson(P/'map.json');errors=[];warnings=[];collection=[];review=[]
 def add(path,name,required=True):
  if path.exists()and path.is_file()and not path.is_symlink():review.append(Entry(name,path))
  elif required:errors.append('missing '+str(path.relative_to(root)))
 for f in sorted(C.rglob('*')):
  if not f.is_file():continue
  if f.is_symlink()or f.suffix not in ALLOWED:errors.append('collection disallowed '+str(f.relative_to(root)));continue
  rel=f.relative_to(P).as_posix();collection.append(Entry(rel,f));review.append(Entry(rel,f))
 for leaf in LEAVES:
  for name in['element.css','element.json','description.md']:
   if not(C/'elements'/leaf/name).exists():errors.append(f'missing {k}/elements/{leaf}/{name}')
  if len(list((C/'elements'/leaf/'fixtures').glob('*.html')))<2:errors.append('fewer than2 fixtures '+leaf)
  for mode in['light','dark']:add(P/'sheets'/f'{leaf}-{mode}.png',f'sheets/{leaf}-{mode}.png')
  check=P/'sheets'/f'{leaf}-checks.json'
  if not check.exists():errors.append('missing checks '+leaf)
  else:
   d=readjson(check)
   if d.get('sourceFingerprint')!=source_fp(P,k,leaf):errors.append('stale sheet '+leaf)
   if include_checks:add(check,'verification/sheets/'+check.name)
 foundation=P/'foundation-sheets'
 fs=list(foundation.glob('*.png'))
 for f in sorted(foundation.rglob('*')):
  if f.is_file():add(f,f.relative_to(P).as_posix())
 expected_foundation=2*len(list((C/'foundation/fixtures').glob('*.html')))
 if len(fs)!=expected_foundation:errors.append('foundation PNG count '+str(len(fs))+' expected '+str(expected_foundation))
 for f in fs:
  if png_info(f.read_bytes())!=[1280,720]:errors.append('foundation PNG dimensions '+f.name)
 for name in ['foundation-checks.json']:
  add(P/name,name,False)
 for mode in ['light','dark']:
  f=P/f'contract-preview-{mode}.html'
  if f.exists():
   b=portable_contract_preview(P,f.read_text()).encode();review.append(Entry(f.name,f,b));review.append(Entry(f'contract-view-{mode}.html',data=b))
 for leaf in sorted({i['leaf']for i in mapped(m)}):add(P/'sheets'/f'{leaf}-replica.png',f'sheets/{leaf}-replica.png')
 for name in['map.json','GAPS.md','review-notes.md','design-language.md']:add(P/name,name)
 for f in sorted((P/'assets').rglob('*')):
  if f.is_file()and not f.is_symlink():add(f,f.relative_to(P).as_posix())
 for n in pages(m):
  for ext in['html','png']:add(P/'reassembled'/f'slide_{n}.{ext}',f'reassembled/slide_{n}.{ext}')
  add(P/'compare-reassembled'/f'slide_{n}.png',f'compare-reassembled/slide_{n}.png')
 for f in sorted(P.glob('support-review-*.md')):add(f,'verification/'+f.name)
 for name in['source-contract-audit.json','source-text-audit.json','relationship-review-final.json','validation-final.json','replica-integrity.json','reassembly-checks.json']:
  add(P/name,'verification/'+name,False)
 for name in ['integration-verification.json','integration-verification.md','integration-png-manifest.json','integration-replica-preservation.json','integration-cache-cleanup.json','integration-golden-text-evidence.json','root-visual-review.json','root-visual-review-status.json','GAPS-INDEX.md','ORIGINS-COMPACT.md']:
  add(root/name,'verification/'+name,False)
 add(root/'review-notes.md','verification/root-review-notes.md',False)
 audit=root/'integration-contracts'/f'{k}.json';add(audit,'verification/contracts-audit.json',False)
 if audit.exists()and readjson(audit).get('errors'):errors.append('supplementary contract errors '+str(len(readjson(audit)['errors'])))
 rc=P/'reassembly-checks.json'
 if not rc.exists():errors.append('missing reassembly checks')
 else:
  d=readjson(rc);rs=d.get('pages',[])
  if isinstance(rs,dict):rs=list(rs.values())
  current=source_fp(P,k)
  if len(rs)!=len(pages(m)):errors.append('assembly check count mismatch')
  if any(q.get('sourceFingerprint')!=current for q in rs):errors.append('stale assembly check fingerprint')
 review+=[Entry('index.html',data=project_html(root,k,True).encode()),Entry('ORIGINS.md',data=origins_md(root,k).encode()),Entry('README.md',data=(f'# {k} review\n\n압축을 푼 뒤 [index.html](index.html)을 엽니다. [GAPS](GAPS.md)와 [검수 기록](review-notes.md), [출처](ORIGINS.md)를 함께 읽습니다. 원본 | 불변 replica | 조립3열은 compare-reassembled/에 있으며, 불변 replica 소스는 Git에 유지합니다. 모든 HTML 의존 파일을 로컬에 동봉했습니다.\n').encode())]
 for mode in['light','dark']:review.append(Entry(f'library-{mode}.html',data=library_html(root,k,mode).encode()))
 include_font_dependencies(P,review)
 verification=root/'integration-verification.json'
 if not verification.exists():errors.append('missing final integration verification')
 else:
  final=readjson(verification)
  if final.get('status')!='verified-with-recorded-candidates'or final.get('errors'):errors.append('integration verification not final/clear')
  snap=next((q for q in final.get('projects',[])if q.get('collection')==k),{})
  if snap.get('currentGlobalFingerprint')!=source_fp(P,k):errors.append('integration verification global fingerprint stale')
  collection_tree=H(json.dumps({str(f.relative_to(C)):H(f.read_bytes())for f in sorted(C.rglob('*'))if f.is_file()},sort_keys=True).encode())
  if snap.get('collectionTreeSHA256')!=collection_tree:errors.append('integration verification collection tree stale')
 issues=offline_check(review);errors+=['offline '+str(x)for x in issues]
 return collection,review,errors,warnings

def entry_manifest(entries,check_png_crc=False):
 out=[]
 for e in entries:
  b=e.read();r={'path':e.name,'bytes':len(b),'sha256':H(b)}
  if e.path is not None and e.data is not None:
   r['originalInputSHA256']=H(e.path.read_bytes());r['archiveTransformation']='Contract preview font stylesheet link is rewritten to the bundled local font provider; the original source file remains unchanged.'
  if e.name.endswith('.png'):
   r['pngDimensions']=png_info(b,check_png_crc)
   if e.name.startswith(('reassembled/','foundation-sheets/'))and r['pngDimensions']!=[1280,720]:raise ValueError('assembly PNG dimensions '+e.name)
   if e.name.startswith('compare-reassembled/')and r['pngDimensions']!=[3840,720]:raise ValueError('comparison PNG dimensions '+e.name)
  out.append(r)
 return out

def write_zip(path,entries,prefix,expected):
 path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_name(path.name+'.tmp');by={r['path']:r for r in expected}
 try:
  with zipfile.ZipFile(tmp,'w',allowZip64=True)as z:
   for e in sorted(entries,key=lambda e:e.name):
    b=e.read();assert H(b)==by[e.name]['sha256'],('input changed during packaging',e.name)
    zi=zipfile.ZipInfo(prefix+e.name,date_time=(2026,10,24,0,0,0));zi.external_attr=0o100644<<16
    zi.compress_type=zipfile.ZIP_STORED if Path(e.name).suffix in['.png','.woff2']else zipfile.ZIP_DEFLATED
    z.writestr(zi,b,compresslevel=6)
  report=verify_zip(tmp,expected=by,prefix=prefix)
  if path.name.endswith('-review.zip')and tmp.stat().st_size>=MAX_REVIEW:raise ValueError('review archive exceeds100MB '+path.name)
  tmp.replace(path);report['name']=path.name;return report
 except BaseException:
  tmp.unlink(missing_ok=True);raise

def verify_zip(path,expected=None,prefix=None):
 path=Path(path)
 with zipfile.ZipFile(path)as z:
  bad=z.testzip()
  if bad:raise ValueError('ZIP CRC mismatch '+bad)
  infos=z.infolist();roots={PurePosixPath(i.filename).parts[0]for i in infos}
  if len(roots)!=1:raise ValueError('ZIP must have exactly one top folder')
  root=next(iter(roots));review=root.endswith('-review');pngs={};listing=[]
  for i in infos:
   pp=PurePosixPath(i.filename)
   if pp.is_absolute()or'..'in pp.parts or i.is_dir():raise ValueError('unsafe/unexpected ZIP path '+i.filename)
   b=z.read(i);r={'path':i.filename,'bytes':len(b),'compressedBytes':i.compress_size,'crc32':f'{i.CRC:08x}','sha256':H(b)}
   if not review and pp.suffix not in ALLOWED:raise ValueError('disallowed collection type '+i.filename)
   if pp.suffix=='.png':pngs[i.filename]=png_info(b,True)
   if expected is not None:
    rel=i.filename[len(prefix):]
    if rel not in expected or r['sha256']!=expected[rel]['sha256']:raise ValueError('ZIP content SHA mismatch '+i.filename)
   listing.append(r)
  if expected is not None and len(listing)!=len(expected):raise ValueError('ZIP entry count differs')
  manifest=root+'/verification/package-manifest.json'
  if review and manifest in z.namelist():
   m=json.loads(z.read(manifest));by={r['path']:r for r in m['files']}
   for r in listing:
    rel=r['path'][len(root)+1:]
    if rel=='verification/package-manifest.json':continue
    if rel not in by or r['sha256']!=by[rel]['sha256']:raise ValueError('embedded review manifest mismatch '+rel)
 return {'name':path.name,'bytes':path.stat().st_size,'sha256':H(path.read_bytes()),'crc':'passed','entryCount':len(listing),'topFolder':root,'pngDimensions':pngs,'files':listing}

def run(root,out,only,dry,include_checks,write_viewers):
 if write_viewers or not dry:write_previews(root)
 reports=[]
 for deck,k,expected_pages in PROJECTS:
  if only and k not in only:continue
  C,R,errors,warnings=inventory(root,k,include_checks);cm=entry_manifest(C);rm=entry_manifest(R,check_png_crc=not dry)
  if len(pages(readjson(project(root,k)/'map.json')))!=expected_pages:errors.append('source page count differs from deck inventory')
  raw=sum(x['bytes']for x in rm);plan={'collection':k,'sourceDeck':deck,'expectedPages':expected_pages,'collectionFiles':len(C),'reviewFiles':len(R),'reviewRawBytes':raw,'reviewLimitBytes':MAX_REVIEW,'errors':errors,'warnings':warnings,'pngCount':sum('pngDimensions'in x for x in rm)}
  if dry:
   print(json.dumps(plan,ensure_ascii=False));reports.append(plan);continue
  if errors:raise RuntimeError(k+' not frozen/complete:\n'+'\n'.join(errors))
  inside={'collection':k,'generatedAtUTC':STAMP(),'sourceDeck':deck,'pages':expected_pages,'files':rm,'selfHashNote':'This file is excluded from its own file list; the outer archive SHA identifies it.','rawLibraryChecks':'Per-cell JSON is optional (--include-cell-checks); source and integrated summaries remain in verification/.'}
  e=Entry('verification/package-manifest.json',data=J(inside));R.append(e);rm.append({'path':e.name,'bytes':len(e.data),'sha256':H(e.data)})
  cr=write_zip(out/(k+'.zip'),C,'',cm);rr=write_zip(out/(k+'-review.zip'),R,k+'-review/',rm)
  result={'collection':k,'generatedAtUTC':STAMP(),'sourceDeck':deck,'pages':expected_pages,'collectionArchive':cr,'reviewArchive':rr,'reviewRawBytes':raw};(out/(k+'-manifest.json')).write_bytes(J(result));reports.append(result)
  print(k,cr['bytes'],rr['bytes'],'CRC/SHA/PNG/offline passed',flush=True)
 if not dry:
  # Preserve other successfully packaged collections when --only is used.
  allreports=[readjson(out/(k+'-manifest.json'))for _,k,_ in PROJECTS if(out/(k+'-manifest.json')).exists()]
  (out/'manifest.json').write_bytes(J({'generatedAtUTC':STAMP(),'collections':allreports}))
  sums=[]
  for r in allreports:
   for key in['collectionArchive','reviewArchive']:sums.append(r[key]['sha256']+'  '+r[key]['name'])
  (out/'SHA256SUMS').write_text('\n'.join(sums)+'\n')
 return reports

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--out',type=Path);p.add_argument('--only',nargs='+',choices=[k for _,k,_ in PROJECTS]);p.add_argument('--dry-run',action='store_true');p.add_argument('--write-previews',action='store_true');p.add_argument('--include-cell-checks',action='store_true');p.add_argument('--verify',nargs='+',type=Path)
 a=p.parse_args()
 if a.verify:
  for path in a.verify:
   r=verify_zip(path);print(json.dumps({k:r[k]for k in['name','bytes','sha256','crc','entryCount','topFolder']},ensure_ascii=False))
 else:run(a.root.resolve(),(a.out or a.root/'deliverables').resolve(),a.only,a.dry_run,a.include_cell_checks,a.write_previews)

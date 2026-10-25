#!/usr/bin/env python3
"""Package frozen Round5 observed designs and self-contained offline review archives.

No design, map, fixture, replica or rendered PNG is edited. --dry-run writes no
archives; --write-previews creates viewers and dynamic provenance Markdown only.
verify_zip(path, expected=None, prefix=None) is retained for public re-downloads.
"""
from __future__ import annotations
import argparse, collections, datetime, hashlib, html, json, posixpath, re, struct, sys, zipfile, zlib
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
PROJECTS=[('069','vectorbox',12),('072','seedmark',21),('073','crossrail',30),('074','meridian-deck',30),('078','onboard-docket',19)]
ALLOWED={'.css','.json','.md','.html'}
MAX_REVIEW=100_000_000
DOWNLOAD='https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables'
H=lambda b:hashlib.sha256(b).hexdigest()
J=lambda v:json.dumps(v,ensure_ascii=False,indent=2).encode()
E=lambda s:html.escape(str(s),quote=True)
STAMP=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()

def readjson(p):return json.loads(Path(p).read_text())
def project(root,k):return Path(root)/(k+'-project')
def leaves(root,k):return sorted(p.name for p in(project(root,k)/k/'elements').iterdir()if p.is_dir())
def page_label(n):
 try:return f'{int(n):02d}'
 except(ValueError,TypeError):return str(n)
def pages(m):return sorted({page_label(p.get('page'))for p in m.get('pages',[])if p.get('page')is not None}|{page_label(i['page'])for i in m.get('instances',[])if i.get('page')is not None})
def mapped(m):return[i for i in m.get('instances',[])if i.get('leaf')and(i.get('use')=='base'or str(i.get('use','')).startswith('variant:'))]
def source_fp(P,k,leaf=None):
 # Keep this byte-for-byte algorithm equivalent to sheets.fingerprint, without
 # importing browser dependencies into the downloaded archive verifier.
 folders=[P/k,P/'assets']
 if leaf:
  deps={leaf};todo=[leaf]
  while todo:
   current=todo.pop()
   for f in(P/k/'elements'/current/'fixtures').glob('*.html'):
    for dep in re.findall(r'data-el=["\']'+re.escape(k)+r'-([^"\']+)',f.read_text()):
     if dep not in deps:deps.add(dep);todo.append(dep)
  folders=[P/k/'kit',P/k/'foundation',P/'assets/fonts']+[P/k/'elements'/x for x in sorted(deps)]
 files={str(f.relative_to(P)):H(f.read_bytes())for folder in folders for f in sorted(folder.rglob('*'))if f.is_file()and f.suffix in['.css','.html','.json','.js','.woff','.woff2']}
 return H(json.dumps(files,sort_keys=True).encode())
def tree_sha(C):return H(json.dumps({str(f.relative_to(C)):H(f.read_bytes())for f in sorted(C.rglob('*'))if f.is_file()},sort_keys=True).encode())
def foundation_images(P,k):
 return [P/'foundation-sheets'/f'{f.stem}-{mode}.png'for f in sorted((P/k/'foundation/fixtures').glob('*.html'))for mode in ['light','dark']]
def panel_images(P,k):
 fixtures=[f for f in(P/k/'foundation/fixtures').glob('panel*.html')if not re.search(r'class=["\'][^"\']*\bslide\b',f.read_text())]
 return [P/'panel-sheets'/f'foundation-panels-{mode}.png'for mode in ['light','dark']]if fixtures else[]
def origin(root,k,leaf):
 P=project(root,k);m=readjson(P/'map.json');instances=[i for i in m.get('instances',[])if i.get('leaf')==leaf];direct=[i for i in instances if i.get('use')=='base'or str(i.get('use','')).startswith('variant:')]
 deps=[]
 for other in leaves(root,k):
  if other==leaf:continue
  if any(re.search(r'data-el=["\']'+re.escape(k+'-'+leaf)+r'["\']',f.read_text())for f in(P/k/'elements'/other/'fixtures').glob('*.html')):deps.append(other)
 return{'pages':sorted({page_label(i['page'])for i in instances}),'directPages':sorted({page_label(i['page'])for i in direct}),'uses':sorted({i.get('use','')for i in instances}),'design':' / '.join(dict.fromkeys(str(i.get('design','')).strip()for i in instances if i.get('design'))),'contractLeaf':leaf.split('--',1)[0],'dependencyOf':deps,'state':'원형 관측'if direct else'원형 반복 사용'if instances else'중첩 의존: '+', '.join(deps)if deps else'직접 지도 근거 없음'}
def origins_md(root,k=None):
 t='# 실제 디자인별 출처 · ROUND5\n\n현재 존재하는 폴더와 map의 논리 인스턴스로만 집계한다. `--design`은 독립 디자인이며, `same-as:` 반복을 새 원형으로 세지 않는다. 원형 없는 보조 요소는 실제 중첩 의존성을 따로 표시한다. 시각적 차이는 각 검수 기록을 따른다.\n\n|컬렉션|실제 디자인 폴더|기본 계약|원본 페이지|근거|구체적인 원형|\n|---|---|---|---|---|---|\n'
 for _,kid,_ in PROJECTS:
  if k and k!=kid:continue
  for leaf in leaves(root,kid):
   o=origin(root,kid,leaf);prefix=''if k else kid+'-project/';clean=lambda s:str(s).replace('|','/').replace('\n',' ')
   t+=f'|{kid}|[{leaf}]({prefix}{kid}/elements/{leaf}/element.css)|{o["contractLeaf"]}|{", ".join(o["pages"])or"—"}|{clean(o["state"])}|{clean(o["design"])or"실제 의존성 참조"}|\n'
 return t

VIEW_CSS='''*{box-sizing:border-box}body{margin:0;background:#f3f5f8;color:#172033;font:15px/1.6 system-ui,sans-serif}body[data-theme=dark]{background:#101722;color:#e9edf3}header,main,footer{max-width:1450px;margin:auto;padding:24px}h1{font-size:32px;line-height:1.2}h2{font-size:23px}a{color:inherit;text-underline-offset:3px}nav,.links,.toolbar{display:flex;flex-wrap:wrap;gap:12px}.muted{opacity:.72}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(285px,1fr));gap:18px}.tile{border:1px solid #aeb8c455;border-radius:12px;padding:16px;background:#ffffff06}.tile h3{margin:0;font-size:18px}.thumb{display:block;width:100%;height:180px;object-fit:contain;background:#8793a210;margin:12px 0}.origin{font-size:12px}.search{width:100%;padding:11px;border:1px solid #aeb8c477;border-radius:7px;background:transparent;color:inherit;font:inherit;margin:18px 0}button{font:inherit;cursor:pointer;border:1px solid #aeb8c477;border-radius:6px;padding:6px 12px;background:transparent;color:inherit}dialog{position:fixed;inset:2vh 2vw;width:96vw;height:96vh;padding:0;border:1px solid #8793a2;border-radius:9px;background:#121925;color:#fff}dialog::backdrop{background:#000b}.toolbar{min-height:60px;align-items:center;padding:10px 16px}.viewport{height:calc(100% - 60px);overflow:auto;background:#444b55;cursor:grab}.viewport img{display:block;max-width:none}.sheet{border-top:1px solid #aeb8c455;padding:25px 0}.sheet img{max-width:100%;height:auto;display:block}.summary{display:flex;flex-wrap:wrap;gap:12px;margin:15px 0}.summary span{border:1px solid #aeb8c455;border-radius:7px;padding:8px 13px}@media(max-width:700px){header,main,footer{padding:16px}h1{font-size:25px}.grid{grid-template-columns:1fr}}'''
VIEW_JS='''const dlg=document.querySelector('#zoom'),vp=document.querySelector('.viewport'),zi=document.querySelector('#zoom-img');let scale=1,down=null;function setScale(s){scale=Math.max(.03,Math.min(5,s));zi.style.width=zi.naturalWidth*scale+'px';document.querySelector('#zoom-level').textContent=Math.round(scale*100)+'%'}document.addEventListener('click',e=>{const a=e.target.closest('a.zoomable');if(!a)return;e.preventDefault();zi.onload=()=>setScale(Math.min(1,(vp.clientWidth-20)/zi.naturalWidth));zi.src=a.href;document.querySelector('#zoom-title').textContent=a.dataset.title||a.textContent;document.querySelector('#zoom-raw').href=a.href;dlg.showModal()});document.querySelector('#close').onclick=()=>dlg.close();document.querySelector('#fit').onclick=()=>setScale(Math.min(1,(vp.clientWidth-20)/zi.naturalWidth));document.querySelector('#native').onclick=()=>setScale(1);document.querySelector('#plus').onclick=()=>setScale(scale*1.3);document.querySelector('#minus').onclick=()=>setScale(scale/1.3);vp.onmousedown=e=>{down=[e.clientX,e.clientY,vp.scrollLeft,vp.scrollTop];e.preventDefault()};window.addEventListener('mouseup',()=>down=null);vp.onmousemove=e=>{if(down){vp.scrollLeft=down[2]-e.clientX+down[0];vp.scrollTop=down[3]-e.clientY+down[1]}};document.querySelector('#search')?.addEventListener('input',e=>document.querySelectorAll('[data-search]').forEach(t=>t.hidden=!t.dataset.search.includes(e.target.value.toLowerCase())));'''
def frame(title,body,theme='light'):
 dialog='<dialog id="zoom"><div class="toolbar"><strong id="zoom-title"></strong><button id="fit">폭 맞춤</button><button id="native">100%</button><button id="minus">−</button><span id="zoom-level"></span><button id="plus">+</button><a id="zoom-raw" target="_blank" rel="noopener">PNG 직접 열기</a><button id="close">닫기</button></div><div class="viewport"><img id="zoom-img" alt="확대 검수 이미지"></div></dialog>'
 return '<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+E(title)+'</title><style>'+VIEW_CSS+'</style></head><body data-theme="'+theme+'">'+body+dialog+'<script>'+VIEW_JS+'</script></body></html>'
def zoom(src,label,title=None):return f'<a class="zoomable" href="{E(src)}" data-title="{E(title or label)}">{E(label)}</a>'
def tile(src,title,links=''):
 return f'<article class="tile" data-search="{E(title.lower())}"><h3>{E(title)}</h3><a class="zoomable" href="{E(src)}" data-title="{E(title)}"><img class="thumb" loading="lazy" src="{E(src)}" alt="{E(title)}"></a><div class="links">{links}</div></article>'
def project_html(root,k,offline=False):
 P=project(root,k);m=readjson(P/'map.json');ls=leaves(root,k);obs={i['leaf']for i in mapped(m)};back=''if offline else'<a href="../index.html">전체 컬렉션</a>';download=''if offline else f'<a href="{DOWNLOAD}/{k}.zip">컬렉션 ZIP</a><a href="{DOWNLOAD}/{k}-review.zip">검수 ZIP</a>'
 links=back+download+'<a href="library-light.pdf">Light PDF</a><a href="library-dark.pdf">Dark PDF</a>'+'<a href="map.json">지도</a><a href="GAPS.md">잔여 GAP</a><a href="round5-report.md">ROUND5 보고</a><a href="review-notes.md">검수 기록</a><a href="design-language.md">디자인 언어</a><a href="ORIGINS.md">실제 출처</a>'
 body=f'<header><nav>{links}</nav><h1>{E(k)} · ROUND5</h1><p>이미지를 열어100%·확대·드래그 이동으로 검토합니다.</p><div class="summary"><span>{len(pages(m))}페이지</span><span>{len(ls)}개 실제 디자인</span><span>{len(obs)}개 직접 원형</span></div><nav><a href="library-light.html">라이트 전체 시트</a><a href="library-dark.html">다크 전체 시트</a><a href="#assembly">페이지 비교</a></nav></header><main><h2>반응형 디자인 시트</h2><input id="search" class="search" placeholder="디자인 폴더 검색" aria-label="디자인 검색"><div class="grid">'
 for leaf in ls:
  o=origin(root,k,leaf);r=f'sheets/{leaf}-replica.png';extra=zoom(f'sheets/{leaf}-light.png','Light')+zoom(f'sheets/{leaf}-dark.png','Dark')+(zoom(r,'원형 비교')if leaf in obs else'')+f'<a href="{k}/elements/{leaf}/element.css">CSS</a><a href="{k}/elements/{leaf}/element.json">계약</a>'
  body+=tile(f'sheets/{leaf}-light.png',leaf,extra).replace('</article>',f'<p class="origin">{E(o["state"])} · {E(", ".join(o["pages"]))}</p></article>')
 body+='</div><h2>Foundation · 패널</h2><div class="grid">'
 for f in foundation_images(P,k)+panel_images(P,k):body+=tile(f.relative_to(P).as_posix(),'Foundation '+f.stem)
 body+='</div>'
 for mode in ['light','dark']:
  if(P/f'contract-preview-{mode}.html').exists():body+=f'<p><a href="contract-view-{mode}.html">공식 preview.py {mode}</a></p>'
 body+='<h2 id="assembly">원본 | 불변 replica | 조립본</h2><div class="grid">'
 for n in pages(m):body+=tile(f'compare-reassembled/slide_{n}.png','페이지 '+n,zoom(f'reassembled/slide_{n}.png','조립 PNG')+f'<a href="reassembled/slide_{n}.html">조립 HTML</a><a href="replica/slide_{n}.html">불변 replica HTML</a>')
 return frame(k+' review',body+'</div></main><footer>압축을 풀고 index.html을 엽니다. 폰트·아이콘·모든 HTML 의존 파일은 로컬에 동봉됩니다. 그리드 양자화·원본 자료의 불일치·잔여 차이는 검수 기록을 따릅니다.</footer>')
def library_html(root,k,mode):
 P=project(root,k);body=f'<header><nav><a href="index.html">검수 처음</a><a href="library-'+('dark'if mode=='light'else'light')+'.html">다른 모드</a></nav><h1>'+E(k)+' · '+mode+'</h1><p>각 시트의 한 행은 fixture 하나이며, 최소 칸부터 허용되는 각 크기를 실제 native 픽셀로 담습니다.</p></header><main>'
 for leaf in leaves(root,k):
  src=f'sheets/{leaf}-{mode}.png';body+=f'<section class="sheet"><h2>{E(leaf)}</h2>'+zoom(src,'확대 / 100%')+f'<a class="zoomable" href="{src}"><img loading="lazy" src="{src}" alt="{E(leaf)} {mode}"></a></section>'
 return frame(k+' '+mode,body+'</main>',mode)
def root_html(root):
 count=sum(len(leaves(root,k))for _,k,_ in PROJECTS);body=f'<header><h1>Rhetis 디자인 라이브러리 · ROUND5</h1><p>{len(PROJECTS)}개 덱의{sum(n for _,_,n in PROJECTS)}페이지에서 실제로 관측한{count}개 독립 디자인입니다.</p><nav><a href="README.md">읽는 방법</a><a href="ORIGINS.md">실제 디자인 출처</a><a href="integration-verification.md">최종 통합 검증</a><a href="deliverables/SHA256SUMS">ZIP SHA256</a></nav></header><main><div class="grid">'
 for deck,k,n in PROJECTS:
  first=pages(readjson(project(root,k)/'map.json'))[0];body+=tile(f'{k}-project/reassembled/slide_{first}.png',f'{k} · 덱{deck} / {n}페이지 / {len(leaves(root,k))}디자인',f'<a href="{k}-project/index.html">검수 미리보기</a><a href="{DOWNLOAD}/{k}.zip">컬렉션 ZIP</a><a href="{DOWNLOAD}/{k}-review.zip">검수 ZIP</a><a href="{DOWNLOAD}/{k}-library-light.pdf">Light PDF</a><a href="{DOWNLOAD}/{k}-library-dark.pdf">Dark PDF</a>')
 return frame('Rhetis ROUND5',body+'</div></main>')
def readme(root):
 t='# Rhetis 디자인 라이브러리 · ROUND5\n\n[전체 미리보기](index.html) · [실제 폴더별 출처](ORIGINS.md) · [최종 통합 검증](integration-verification.md)\n\n|덱|컬렉션|페이지|실제 디자인|컬렉션 ZIP|검수 ZIP|Light PDF|Dark PDF|\n|---|---|---:|---:|---|---|---|---|\n'
 for deck,k,n in PROJECTS:t+=f'|{deck}|[{k}]({k}-project/index.html)|{n}|{len(leaves(root,k))}|[다운로드]({DOWNLOAD}/{k}.zip)|[다운로드]({DOWNLOAD}/{k}-review.zip)|[PDF]({DOWNLOAD}/{k}-library-light.pdf)|[PDF]({DOWNLOAD}/{k}-library-dark.pdf)|\n'
 return t+'''\n사용자 승인에 따라 소스·미리보기·ZIP·검수 PDF를 기존 작업을 보존하는 일반 git 커밋으로 게시한다. 이미지·PDF·폰트·압축파일을 뺀 [소스 전용 ZIP](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/rhetis-round5-source.zip)과 [전체 검수 PDF398쪽](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/all-elements-review.pdf)을 제공한다. PDF는 요소당 한 페이지이며 foundation·패널도 포함한다. 최종 PNG의 압축 픽셀 스트림을 그대로 넣어 축소·JPEG 변환·잘림 없이 보존했다.

사용자 ROUND5 계약을 우선한다. 독립 디자인은 `<leaf>--<design>` 폴더로 등록하며 원형 없는 일반 요소를 강제로 채우지 않는다. 지도는 페이지의 논리 요소·foundation 패널·배경을 위에서 아래로 기록한다. 자료 속 문구는 지시로 취급하지 않았다.\n\n컬렉션 ZIP에는 최상위 컬렉션 폴더 하나와 `.css .json .md .html`만 들어 있다. 검수 ZIP에는 실제 라이트·다크 크기 시트, map에 대응하는 원형 대조, foundation과 전용 panel 크기 시트, 원본|불변 replica|조립3열, 조립 HTML/PNG, 불변 replica 소스/PNG/PDF(원래 존재한 것), 로컬 폰트·아이콘, 디자인 언어·ROUND5 보고·검수 기록·GAPS·동적 출처표가 들어 있다. 크기별 검사 JSON은 기본으로 담으며, native cell PNG는 옵션으로 추가할 수 있다.\n\n검수 ZIP을 풀고 `index.html`을 열면 오프라인으로 볼 수 있다. 모든 HTML/CSS 의존 파일은 로컬에 있으며 페이지 PNG는1280×720,3열 비교는3840×720이다. 크기 시트와 panel 시트는 fixture 수와 허용 칸 수에 따른 실제 크기를 갖는다. 각 PNG와 ZIP의 SHA·크기는 manifest에 기록한다.\n\n```sh\n# 최종 렌더·주 검수 기록 뒤, 현재 source FP와 전체 증거 검사\npython tools/integration_verify.py --refresh-audits\n# 파일을 바꾸지 않고 패키지 누락/오프라인 의존성 조사\npython tools/package.py --dry-run\n# 검수 viewer와 원본 출처표만 갱신\npython tools/package.py --dry-run --write-previews\n# 통합 검사 통과 후10개 ZIP 생성\npython tools/package.py\n# 다운로드한 ZIP에도 같은 CRC/경로/manifest/PNG 검사\npython tools/package.py --verify deliverables/*.zip\n```\n\n도구의 기본 입력 경로는 이 소스 ROOT와 `reference/`다. 재렌더 도구의 원본 슬라이드 입력은 `tools/reassembly.py`의 `ORIGINALS` 상수로 명시한다. ZIP 생성과 검증은 디자인 source·fixture·map·replica를 변경하지 않는다. 실제 API 게시와 게시 후 재다운로드 검증은 별도 절차이며, 이 도구는 게시 성공을 추정하지 않는다.\n'''

def write_previews(root):
 (root/'index.html').write_text(root_html(root));(root/'README.md').write_text(readme(root));(root/'ORIGINS.md').write_text(origins_md(root))
 for _,k,_ in PROJECTS:
  P=project(root,k);(P/'index.html').write_text(project_html(root,k));(P/'ORIGINS.md').write_text(origins_md(root,k))
  for mode in ['light','dark']:
   (P/f'library-{mode}.html').write_text(library_html(root,k,mode))
   f=P/f'contract-preview-{mode}.html'
   if f.exists():(P/f'contract-view-{mode}.html').write_text(portable_contract_preview(P,f.read_text()))

@dataclass
class Entry:
 name:str
 path:Path|None=None
 data:bytes|None=None
 def read(self):return self.data if self.data is not None else self.path.read_bytes()
class References(HTMLParser):
 def __init__(self):super().__init__();self.refs=[]
 def handle_starttag(self,tag,attrs):self.refs.extend(v for k,v in attrs if k in ['href','src','poster']and v)
def refs(e):
 if not e.name.endswith(('.html','.css')):return[]
 t=e.read().decode();p=References()
 if e.name.endswith('.html'):p.feed(t)
 return p.refs+re.findall(r'url\(\s*["\']?([^\)"\']+)',t)
def local_refs(e):
 out=[]
 for ref in refs(e):
  u=urlsplit(ref.strip())
  if not u.scheme and not ref.startswith(('#','/'))and u.path:out.append(posixpath.normpath(posixpath.join(posixpath.dirname(e.name),unquote(u.path))))
 return out
def offline_check(entries):
 names={e.name for e in entries};issues=[]
 for e in entries:
  for ref in refs(e):
   ref=ref.strip();u=urlsplit(ref)
   if not ref or ref.startswith('#')or u.scheme in ['data','mailto','tel']:continue
   if u.scheme or ref.startswith(('/','//')):issues.append([e.name,ref,'external/absolute reference']);continue
   target=posixpath.normpath(posixpath.join(posixpath.dirname(e.name),unquote(u.path)))
   if target not in names:issues.append([e.name,ref,'missing offline dependency'])
 return issues
def portable_contract_preview(P,text):
 font='assets/fonts/fonts.css'if(P/'assets/fonts/fonts.css').exists()else'assets/fonts.css'
 return re.sub(r'href=(["\'])([^"\']*fonts(?:/fonts)?\.css)\1',lambda m:'href='+m.group(1)+font+m.group(1),text)
def png_info(data,crc=False):
 if len(data)<33 or data[:8]!=b'\x89PNG\r\n\x1a\n':raise ValueError('invalid PNG header')
 dims=list(struct.unpack('>II',data[16:24]))
 if min(dims)<=0:raise ValueError('empty PNG dimensions')
 if crc:
  pos=8;ended=False
  while pos<len(data):
   if pos+12>len(data):raise ValueError('truncated PNG chunk')
   n=struct.unpack('>I',data[pos:pos+4])[0];kind=data[pos+4:pos+8];end=pos+8+n
   if end+4>len(data)or zlib.crc32(data[pos+4:end])&0xffffffff!=struct.unpack('>I',data[end:end+4])[0]:raise ValueError('PNG CRC mismatch')
   pos=end+4
   if kind==b'IEND':ended=True;break
  if not ended or pos!=len(data):raise ValueError('invalid PNG ending')
 return dims

def inventory(root,k,include_checks=False):
 P=project(root,k);C=P/k;m=readjson(P/'map.json');ls=leaves(root,k);obs={i['leaf']for i in mapped(m)};collection=[];review=[];errors=[];warnings=[]
 def add(path,name,required=True):
  if path.is_file()and not path.is_symlink():review.append(Entry(name,path))
  elif required:errors.append('missing '+str(path.relative_to(root)))
 for f in sorted(C.rglob('*')):
  if not f.is_file():continue
  if f.is_symlink()or f.suffix not in ALLOWED:errors.append('collection disallowed '+str(f.relative_to(root)));continue
  e=Entry(f.relative_to(P).as_posix(),f);collection.append(e);review.append(e)
 for leaf in ls:
  for name in ['element.css','element.json','description.md']:
   if not(C/'elements'/leaf/name).exists():errors.append('missing '+leaf+'/'+name)
  if len(list((C/'elements'/leaf/'fixtures').glob('*.html')))<2:errors.append('fewer than2 fixtures '+leaf)
  for mode in ['light','dark']:add(P/'sheets'/f'{leaf}-{mode}.png',f'sheets/{leaf}-{mode}.png')
  f=P/'sheets'/f'{leaf}-checks.json';add(f,'verification/sheets/'+f.name)
  if f.exists()and readjson(f).get('sourceFingerprint')!=source_fp(P,k,leaf):errors.append('stale sheet '+leaf)
  if leaf in obs:add(P/'sheets'/f'{leaf}-replica.png',f'sheets/{leaf}-replica.png')
  if include_checks and f.exists():
   for mode,rows in readjson(f).get('modes',{}).items():
    for row in rows:
     name=f'{leaf}--{Path(row["fixture"]).stem}--{mode}--{row["size"][0]}x{row["size"][1]}.png';add(P/'sheet-cells'/name,'sheet-cells/'+name)
 for f in foundation_images(P,k)+panel_images(P,k):add(f,f.relative_to(P).as_posix())
 if panel_images(P,k):add(P/'panel-sheets/panel-checks.json','panel-sheets/panel-checks.json')
 if include_checks:
  for f in sorted((P/'panel-cells').glob('*.png')):add(f,f.relative_to(P).as_posix())
 for name in ['map.json','GAPS.md','review-notes.md','design-language.md','round5-report.md']:add(P/name,name)
 for f in sorted((P/'assets').rglob('*')):
  if f.is_file()and not f.is_symlink():add(f,f.relative_to(P).as_posix())
 for f in sorted((P/'replica').rglob('*')):
  if f.is_file()and not f.is_symlink():add(f,f.relative_to(P).as_posix())
 for n in pages(m):
  for ext in ['html','png']:add(P/'reassembled'/f'slide_{n}.{ext}',f'reassembled/slide_{n}.{ext}')
  add(P/'compare-reassembled'/f'slide_{n}.png',f'compare-reassembled/slide_{n}.png')
 for f in(P/'reassembled').glob('*.pdf'):add(f,f.relative_to(P).as_posix())
 for f in sorted((P/'paint-proofs').glob('*')):
  if f.is_file():add(f,'paint-proofs/'+f.name)
 for name in ['foundation-checks.json','source-contract-audit.json','reassembly-checks.json','round5-review.json','support078-fragments.json','optical-checks.json']:
  add(P/name,'verification/'+name,False)
 for name in ['integration-verification.json','integration-verification.md','integration-png-manifest.json','integration-replica-preservation.json','root-visual-review.json','root-visual-review-status.json','review-notes.md','preview-build-checks.json','pdf-verification.json']:
  add(root/name,'verification/'+name,False)
 add(root/'integration-contracts'/f'{k}.json','verification/contracts-audit.json',False)
 for mode in ['light','dark']:
  add(P/f'library-{mode}.pdf',f'library-{mode}.pdf')
 for mode in ['light','dark']:
  f=P/f'contract-preview-{mode}.html'
  if f.exists():
   b=portable_contract_preview(P,f.read_text()).encode();review.extend([Entry(f.name,f,b),Entry(f'contract-view-{mode}.html',data=b)])
 review.extend([Entry('index.html',data=project_html(root,k,True).encode()),Entry('ORIGINS.md',data=origins_md(root,k).encode()),Entry('README.md',data=f'# {k} 검수\n\n압축을 풀고 [index.html](index.html)을 엽니다. [출처](ORIGINS.md)·[지도](map.json)·[ROUND5 결과](round5-report.md)·[검수 기록](review-notes.md)을 함께 읽습니다.\n'.encode())])
 for mode in ['light','dark']:review.append(Entry(f'library-{mode}.html',data=library_html(root,k,mode).encode()))
 # Resolve only real local dependencies confined to this project. Source HTML is
 # not rewritten to borrow a font from another project or external server.
 names={e.name for e in review}
 for _ in range(8):
  missing={r for e in review for r in local_refs(e)if r not in names};added=[]
  for rel in sorted(missing):
   f=(P/rel).resolve()
   if f.is_relative_to(P.resolve())and f.is_file()and not f.is_symlink():added.append(Entry(rel,f));names.add(rel)
  if not added:break
  review+=added
 by={}
 for e in review:
  if e.name in by and H(e.read())!=H(by[e.name].read()):errors.append('duplicate differing archive entry '+e.name)
  by[e.name]=e
 review=list(by.values());errors.extend('offline '+str(x)for x in offline_check(review))
 final=root/'integration-verification.json'
 if not final.exists():errors.append('missing final integration verification')
 else:
  d=readjson(final);snap=next((q for q in d.get('projects',[])if q.get('collection')==k),{})
  if d.get('status')!='verified-with-recorded-candidates'or d.get('errors'):errors.append('integration verification not final/clear')
  if snap.get('currentGlobalFingerprint')!=source_fp(P,k):errors.append('integration global fingerprint stale')
  if snap.get('collectionTreeSHA256')!=tree_sha(C):errors.append('integration collection tree stale')
 return collection,review,errors,warnings

def entry_manifest(entries,check_png_crc=False):
 result=[]
 for e in entries:
  b=e.read();r={'path':e.name,'bytes':len(b),'sha256':H(b)}
  if e.path is not None and e.data is not None:r.update(originalInputSHA256=H(e.path.read_bytes()),archiveTransformation='Only official preview font href is made local; design inputs remain unchanged.')
  if e.name.endswith('.png'):
   r['pngDimensions']=png_info(b,check_png_crc)
   if e.name.startswith(('reassembled/','foundation-sheets/','replica/slide_'))and r['pngDimensions']!=[1280,720]:raise ValueError('page PNG dimensions '+e.name)
   if e.name.startswith('compare-reassembled/')and r['pngDimensions']!=[3840,720]:raise ValueError('triple PNG dimensions '+e.name)
  result.append(r)
 return result

def verify_zip(path,expected=None,prefix=None):
 path=Path(path)
 with zipfile.ZipFile(path)as z:
  bad=z.testzip()
  if bad:raise ValueError('ZIP CRC mismatch '+bad)
  infos=z.infolist();names=[i.filename for i in infos]
  if len(names)!=len(set(names)):raise ValueError('duplicate ZIP paths')
  roots={PurePosixPath(n).parts[0]for n in names if PurePosixPath(n).parts}
  if len(roots)!=1:raise ValueError('ZIP must have exactly one top folder')
  root=next(iter(roots));review=root.endswith('-review');pngs={};listing=[]
  for i in infos:
   pp=PurePosixPath(i.filename)
   if pp.is_absolute()or'..'in pp.parts or'\\'in i.filename or'\x00'in i.filename or i.is_dir()or(i.external_attr>>16)&0o170000==0o120000:raise ValueError('unsafe ZIP path '+i.filename)
   if len(pp.parts)<2:raise ValueError('ZIP entry outside top folder '+i.filename)
   b=z.read(i);r={'path':i.filename,'bytes':len(b),'compressedBytes':i.compress_size,'crc32':f'{i.CRC:08x}','sha256':H(b)}
   if not review and pp.suffix not in ALLOWED:raise ValueError('disallowed collection type '+i.filename)
   if pp.suffix=='.png':
    dims=png_info(b,True);pngs[i.filename]=dims
    if any(q in pp.parts for q in ['reassembled','foundation-sheets'])and dims!=[1280,720]:raise ValueError('page PNG dimensions '+i.filename)
    if 'compare-reassembled'in pp.parts and dims!=[3840,720]:raise ValueError('triple PNG dimensions '+i.filename)
   if expected is not None:
    if prefix is not None and not i.filename.startswith(prefix):raise ValueError('ZIP prefix mismatch '+i.filename)
    rel=i.filename[len(prefix or''):]
    if rel not in expected or r['sha256']!=expected[rel]['sha256']:raise ValueError('ZIP content SHA mismatch '+i.filename)
   listing.append(r)
  if expected is not None and len(expected)!=len(listing):raise ValueError('ZIP entry count differs')
  embedded=root+'/verification/package-manifest.json'
  if review:
   if embedded not in names:raise ValueError('review ZIP lacks embedded manifest')
   m=json.loads(z.read(embedded));by={v['path']:v for v in m['files']}
   if len(by)!=len(m['files']):raise ValueError('duplicate embedded manifest paths')
   actual={r['path'][len(root)+1:]for r in listing if r['path']!=embedded}
   if actual!=set(by):raise ValueError('embedded manifest file set mismatch')
   for r in listing:
    rel=r['path'][len(root)+1:]
    if r['path']!=embedded and(r['sha256']!=by[rel]['sha256']or r['bytes']!=by[rel]['bytes']):raise ValueError('embedded manifest SHA/bytes mismatch '+rel)
   entries=[Entry(n[len(root)+1:],data=z.read(n))for n in names if n!=embedded]
   issues=offline_check(entries)
   if issues:raise ValueError('review archive offline references '+str(issues[:8]))
 return{'name':path.name,'bytes':path.stat().st_size,'sha256':H(path.read_bytes()),'crc':'passed','entryCount':len(listing),'topFolder':root,'pngDimensions':pngs,'files':listing}

def write_zip(path,entries,prefix,expected):
 path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_name(path.name+'.tmp');by={r['path']:r for r in expected}
 try:
  with zipfile.ZipFile(tmp,'w',allowZip64=True)as z:
   for e in sorted(entries,key=lambda x:x.name):
    b=e.read()
    if H(b)!=by[e.name]['sha256']:raise ValueError('input changed during packaging '+e.name)
    zi=zipfile.ZipInfo(prefix+e.name,date_time=(2026,10,25,0,0,0));zi.external_attr=0o100644<<16;zi.compress_type=zipfile.ZIP_STORED if Path(e.name).suffix.lower()in['.png','.woff2','.pdf']else zipfile.ZIP_DEFLATED;z.writestr(zi,b,compresslevel=6)
  report=verify_zip(tmp,by,prefix)
  if path.name.endswith('-review.zip')and tmp.stat().st_size>=MAX_REVIEW:raise ValueError('review archive exceeds100MB '+path.name)
  tmp.replace(path);report['name']=path.name;return report
 except BaseException:tmp.unlink(missing_ok=True);raise

def run(root,out,only=None,dry=False,include_checks=False,write_viewers=False):
 if write_viewers or not dry:write_previews(root)
 plans=[]
 for deck,k,n in PROJECTS:
  if only and k not in only:continue
  C,R,errors,warnings=inventory(root,k,include_checks);cm=entry_manifest(C);rm=entry_manifest(R,check_png_crc=not dry)
  if len(pages(readjson(project(root,k)/'map.json')))!=n:errors.append('page count differs from deck inventory')
  plan={'collection':k,'sourceDeck':deck,'pages':n,'designs':len(leaves(root,k)),'collectionFiles':len(C),'reviewFiles':len(R),'reviewRawBytes':sum(r['bytes']for r in rm),'pngCount':sum('pngDimensions'in r for r in rm),'errors':errors,'warnings':warnings}
  if dry:print(json.dumps(plan,ensure_ascii=False));plans.append(plan);continue
  if errors:raise RuntimeError(k+' not frozen/complete:\n'+'\n'.join(errors))
  inside={'schema':'rhetis.round5-package-manifest/1','collection':k,'generatedAtUTC':STAMP(),'sourceDeck':deck,'pages':n,'designs':plan['designs'],'sourceFingerprint':source_fp(project(root,k),k),'files':rm,'selfHashNote':'This manifest excludes itself; the outer archive SHA identifies it.'};e=Entry('verification/package-manifest.json',data=J(inside));R.append(e);rm.append({'path':e.name,'bytes':len(e.data),'sha256':H(e.data)})
  cr=write_zip(out/(k+'.zip'),C,'',cm);rr=write_zip(out/(k+'-review.zip'),R,k+'-review/',rm);result={'collection':k,'generatedAtUTC':STAMP(),'sourceDeck':deck,'pages':n,'designs':plan['designs'],'collectionArchive':cr,'reviewArchive':rr,'reviewRawBytes':plan['reviewRawBytes']};(out/(k+'-manifest.json')).write_bytes(J(result));plans.append(result);print(k,cr['bytes'],rr['bytes'],'CRC/SHA/PNG/offline passed',flush=True)
 if not dry:
  allreports=[readjson(out/(k+'-manifest.json'))for _,k,_ in PROJECTS if(out/(k+'-manifest.json')).exists()];(out/'manifest.json').write_bytes(J({'schema':'rhetis.round5-deliverables/1','generatedAtUTC':STAMP(),'collections':allreports}));(out/'SHA256SUMS').write_text(''.join(r[t]['sha256']+'  '+r[t]['name']+'\n'for r in allreports for t in ['collectionArchive','reviewArchive']))
 return plans

if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__);a.add_argument('--root',type=Path,default=ROOT);a.add_argument('--out',type=Path);a.add_argument('--only',nargs='+',choices=[k for _,k,_ in PROJECTS]);a.add_argument('--dry-run',action='store_true');a.add_argument('--write-previews',action='store_true');a.add_argument('--include-cell-checks',action='store_true');a.add_argument('--verify',nargs='+',type=Path);v=a.parse_args()
 if v.verify:
  for f in v.verify:
   r=verify_zip(f);print(json.dumps({k:r[k]for k in ['name','bytes','sha256','crc','entryCount','topFolder']},ensure_ascii=False))
 else:run(v.root.resolve(),(v.out or v.root/'deliverables').resolve(),v.only,v.dry_run,v.include_cell_checks,v.write_previews)

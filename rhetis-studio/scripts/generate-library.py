"""Author the standalone Studio Spectrum Rhetis collection from contract data.
No sample stylesheet or reference bitmap is embedded in this collection.
"""
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / 'collections' / 'studio-spectrum'
KIT = 'studio-spectrum'
TAX = json.loads((BASE / 'contract/taxonomy.json').read_text())

def write(path, text):
    p=OUT/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text.strip()+'\n',encoding='utf-8')
def js(path,obj): write(path,json.dumps(obj,ensure_ascii=False,indent=2))
js(Path('kit/kit.json'),dict(schema='rhetis.kit/2',id=KIT,label='Studio Spectrum',tokens='css/tokens.css',description='description.md',extensions={}))
write(Path('kit/description.md'),'''Studio Spectrum is an editorial presentation language distilled from the ten supplied business and portfolio references. Quiet white space, flat surfaces, fine horizontal rules and crisp near-square corners give information a composed rhythm. Navy carries the default emphasis; muted red, fresh lime and soft green offer distinct narrative tones. Large confident figures sit beside compact explanatory text. Color is applied in deliberate areas rather than decoration. Dark mode uses a deep blue paper, lifted slate surfaces and brighter restrained accents, with an independently tuned contrast hierarchy.''')
colors={
'--page':'#ffffff','--surface':'#f5f6f7','--surface-2':'#e9edf1','--ink':'#17202e','--ink-2':'#343e4b','--mute':'#58616d','--line':'#c8cdd4','--accent':'#304577','--accent-ink':'#ffffff','--accent-soft':'#eef1fa','--tone-1':'#304577','--tone-1-ink':'#ffffff','--tone-2':'#a63d41','--tone-2-ink':'#ffffff','--tone-3':'#d8fa8a','--tone-3-ink':'#223017','--tone-4':'#c2e6bf','--tone-4-ink':'#163b26','--tone-5':'#f4e6b6','--tone-5-ink':'#493b1b','--good':'#236240','--warn':'#805b18','--bad':'#a12e3b'}
dark={'--page':'#111a2b','--surface':'#1c2840','--surface-2':'#2b3850','--ink':'#f6f7fa','--ink-2':'#d4dce8','--mute':'#adb9cc','--line':'#526079','--accent':'#a8bbf2','--accent-ink':'#14213b','--accent-soft':'#253656','--tone-1':'#a8bbf2','--tone-1-ink':'#14213b','--tone-2':'#efadb0','--tone-2-ink':'#4b1b24','--tone-3':'#d8fa8a','--tone-3-ink':'#223017','--tone-4':'#b3d9ba','--tone-4-ink':'#163b26','--tone-5':'#eddaa1','--tone-5-ink':'#493b1b','--good':'#a7d9b7','--warn':'#eed69a','--bad':'#f1afb7'}
other={'--font-display':'"Pretendard", sans-serif','--font-body':'"Pretendard", sans-serif','--weight-display':'700','--weight-body':'400','--tracking-display':'-0.045em','--radius':'4px','--radius-sm':'2px','--stroke':'1px','--text-min':'12px','--margin-x':'64px','--margin-y':'48px','--gap':'24px','--gap-sm':'12px','--gap-lg':'40px','--pad':'28px','--furn-edge':'24px','--top-h':'28px','--foot-h':'28px','--furn-gap':'24px','--rail-w':'56px','--rail-gap':'32px','--title-weight':'700','--title-line':'1.12','--title-track':'-0.045em','--lead-weight':'400','--lead-line':'1.45','--lead-track':'-0.018em','--figure-weight':'600','--figure-line':'1.05','--figure-track':'-0.045em','--name-weight':'600','--name-line':'1.3','--name-track':'-0.025em','--body-weight':'400','--body-line':'1.55','--body-track':'-0.012em','--label-weight':'600','--label-line':'1.2','--label-track':'-0.005em','--label-track-latin':'0.065em'}
write(Path('kit/css/tokens.css'), '.slide {\n'+''.join(f'  {k}: {v};\n' for k,v in {**colors,**other}.items())+'}\n.slide.dark {\n'+''.join(f'  {k}: {v};\n' for k,v in dark.items())+'}')
js(Path('foundation/foundation.json'),dict(schema='rhetis.design-library-foundation-source/1',kit=KIT,registrations={},tokenDefaults={}))
write(Path('foundation/description.md'),'''A 1280 by 720 editorial canvas with a twelve-column, six-row content grid. A small category line, a strong title and a restrained lead align on a consistent left edge. Thin running rules and compact page furniture recall the supplied portfolio and business references. The cover uses an oversized left-aligned lockup with a simple geometric quadrant, never a screenshot. Numbered neutral seats clearly reserve photographs, logos or illustrations without simulating their content.''')
write(Path('foundation/foundation.css'),'''
.slide, .slide * { box-sizing: border-box; }
.slide { position:relative; width:1280px; height:720px; overflow:hidden; background:var(--page); color:var(--ink); font-family:var(--font-body); font-size:var(--type-20); font-weight:var(--body-weight); line-height:var(--body-line); letter-spacing:var(--body-track); word-break:keep-all; overflow-wrap:anywhere; -webkit-font-smoothing:antialiased; }
.slide :is(h1,h2,h3,h4,p,blockquote,ul,ol) { margin:0; }
.slide > .page { position:absolute; inset:var(--margin-y) var(--margin-x); display:flex; flex-direction:column; gap:var(--gap-lg); }
.slide:has(> .top) > .page { top:calc(var(--furn-edge) + var(--top-h) + var(--furn-gap)); }
.slide:has(> .foot) > .page { bottom:calc(var(--furn-edge) + var(--foot-h) + var(--furn-gap)); }
.slide:has(> .rail) > .page { left:calc(var(--rail-w) + var(--rail-gap)); }
.slide .head { display:flex; flex-direction:column; gap:var(--gap-sm); flex:none; }
.slide .head.center { align-items:center; text-align:center; }
.slide .kicker { color:var(--accent); font-size:var(--type-14); font-weight:var(--label-weight); line-height:var(--label-line); letter-spacing:var(--label-track-latin); }
.slide .title { font-family:var(--font-display); font-size:var(--type-48); font-weight:var(--title-weight); line-height:var(--title-line); letter-spacing:var(--title-track); }
.slide .lead { font-size:var(--type-20); font-weight:var(--lead-weight); line-height:var(--lead-line); letter-spacing:var(--lead-track); color:var(--ink-2); }
.slide .body { flex:1; min-height:0; display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); grid-template-rows:repeat(6,minmax(0,1fr)); gap:var(--gap); }
.slide :is(.body,.group,.stack,.split) > * { min-width:0; min-height:0; }
.slide .group { display:flex; gap:var(--gap); }
.slide .group > * { flex:1 1 0; }
.slide .group.col { flex-direction:column; }
.slide .group.two { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); }
.slide .group.three { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); }
.slide .stack { display:flex; flex-direction:column; gap:var(--gap-sm); }
.slide .split { display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:var(--gap); }
.slide .split.wide-left { grid-template-columns:minmax(0,7fr) minmax(0,5fr); }
.slide .icon { display:inline-flex; width:1em; height:1em; flex:none; align-items:center; justify-content:center; }
.slide .icon svg { width:100%; height:100%; display:block; }
.slide > :is(.top,.foot,.rail) { position:absolute; color:var(--mute); font-size:var(--type-12); font-weight:var(--label-weight); letter-spacing:var(--label-track); line-height:var(--label-line); }
.slide > :is(.top,.foot) { left:var(--margin-x); right:var(--margin-x); display:flex; align-items:center; gap:var(--gap); }
.slide > .top { top:var(--furn-edge); height:var(--top-h); border-bottom:var(--stroke) solid var(--line); }
.slide > .foot { bottom:var(--furn-edge); height:var(--foot-h); border-top:var(--stroke) solid var(--line); }
.slide > :is(.top,.foot) > :is(.sec,.src) { margin-left:auto; }
.slide > .foot > .no { color:var(--ink); font-variant-numeric:tabular-nums; }
.slide > .rail { inset:0 auto 0 0; width:var(--rail-w); border-right:var(--stroke) solid var(--line); display:flex; flex-direction:column; align-items:center; justify-content:center; gap:var(--gap); }
.slide > .rail > .on { color:var(--accent); }
.slide > .rail > .label { writing-mode:vertical-rl; }
.slide.cover > .page { display:grid; grid-template:1fr/1fr; }
.slide.cover .page > * { grid-area:1/1; min-width:0; }
.slide.cover .lockup { z-index:2; align-self:center; justify-self:start; display:flex; flex-direction:column; gap:var(--gap); max-width:74%; }
.slide.cover .lockup.at-center { justify-self:center; text-align:center; align-items:center; }
.slide.cover .lockup.at-top-left { align-self:start; }
.slide.cover .lockup.at-bottom-left { align-self:end; }
.slide.cover .lockup .title { font-size:var(--type-92); }
.slide.cover .lockup .lead { max-width:36em; }
.slide.cover .meta { z-index:2; align-self:end; font-size:var(--type-14); color:var(--mute); }
.slide.cover:has(.at-bottom-left) .meta { align-self:start; }
.slide.cover .deco { width:440px; height:440px; border-radius:50% 0 0 0; border:var(--stroke) solid var(--line); background:radial-gradient(ellipse at 82% 24%,var(--tone-4) 0,var(--accent-soft) 46%,var(--page) 88%); justify-self:end; align-self:end; }
.slide .seat { display:flex; align-items:center; justify-content:center; min-width:0; min-height:0; background:var(--surface-2); color:var(--mute); border-radius:var(--radius-sm); overflow:hidden; }
.slide .seat[data-ph]::after { content:attr(data-ph); font-size:var(--type-14); font-weight:var(--label-weight); line-height:var(--label-line); }
.slide .body > .seat { width:100%; height:100%; }
.slide .seat.avatar { aspect-ratio:1; border-radius:50%; }
.slide .seat.portrait { aspect-ratio:4/5; }
.slide .seat.logo { aspect-ratio:3/1; }
.slide .seat.back { position:absolute; inset:0; z-index:0; }
''')
write(Path('foundation/fixtures/seat.html'),'''<!-- min: 12x6 -->
<section class="slide"><div class="top"><span class="deck">STUDIO SPECTRUM</span><span class="sec">2026 성과 보고</span></div><div class="page"><header class="head"><p class="kicker">BUSINESS REVIEW</p><h1 class="title">성장의 근거를 명확하게</h1><p class="lead">데이터와 실행 계획을 한 화면의 질서로 연결합니다.</p></header><div class="body"><div class="seat" data-ph="1" style="grid-column:1 / span 7; grid-row:1 / span 6"></div><div class="seat portrait" data-ph="2" style="grid-column:9 / span 4; grid-row:1 / span 6"></div></div></div><div class="foot"><span class="deck">기획전략팀</span><span class="src">2026년 3분기 내부 집계</span><span class="no">03</span></div></section>''')
write(Path('foundation/fixtures/cover.html'),'''<!-- min: 12x6 -->
<section class="slide cover"><div class="page"><div class="lockup at-left"><p class="kicker">2026 · STRATEGY &amp; PERFORMANCE</p><h1 class="title">다음 성장을<br>설계합니다.</h1><p class="lead">성과의 기록에서 실행의 방향으로, 더 분명한 비즈니스 이야기.</p></div><div class="deco"></div><p class="meta">STUDIO SPECTRUM · 전략기획팀 · 2026.10</p></div></section>''')

CSS={}
DESC={}
FIX={}
ROOTS={c['category'].split('.')[-1]:c['roots'] for c in TAX['contracts']}
CONTRACT={c['category'].split('.')[-1]:c['id'] for c in TAX['contracts']}
def root(folder, cls=None, content='', attrs=''):
    cls=cls or ROOTS[folder][0]
    return f'<div class="{cls}" data-el="{KIT}-{folder}" {attrs}>{content}</div>'
def fixture(folder,name,body,minimum='6x3 | 3x6'):
    # Single fixture root occupies its seat, with chart custom values preserved.
    body=re.sub(r'(<\w+\b[^>]*)(>)',lambda m:m[1]+' style="grid-column:1 / span 12; grid-row:1 / span 6"'+m[2] if 'style=' not in m[1] else m[1].replace('style="','style="grid-column:1 / span 12; grid-row:1 / span 6; ',1)+m[2],body,count=1)
    FIX.setdefault(folder,[]).append((name, '<!-- min: '+minimum+' -->\n'+body))
def define(folder,desc,css): DESC[folder]=desc; CSS[folder]=css

def parts(kick='성장 지표',fig='150',unit='억',name='고객과 함께 만드는 성과',note='핵심 고객의 사용 경험을 개선하고, 지속 가능한 매출 기반을 넓혔습니다.',mark='↗'):
    return '<div class="parts">'+(f'<span class="kick">{kick}</span>' if kick else '')+(f'<span class="mark">{mark}</span>' if mark else '')+(f'<p class="fig">{fig}<small>{unit}</small></p>' if fig else '')+f'<h3 class="name">{name}</h3><p class="note">{note}</p></div>'

define('card','Flat editorial panels use a narrow accent rule, generous internal air and a large figure. Tone variants preserve the same crisp hierarchy.', '''
@R { display:flex; background:var(--surface); border-radius:var(--radius); border-top:2px solid var(--accent); padding:var(--pad); }
@R > .parts { display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); width:100%; }
@R > .parts > .mark { align-self:flex-end; color:var(--accent); font-size:var(--type-30); }
@R > .parts > .fig { margin-top:auto; font-size:var(--type-80); }
@R.on { background:var(--accent); color:var(--accent-ink); }
@R.on :is(.kick,.note,.mark) { color:var(--accent-ink); }
@R.quiet { background:var(--page); border-top-color:var(--line); }
@R.line { background:var(--page); border:var(--stroke) solid var(--line); }
@R.tone-1 { background:var(--tone-1); color:var(--tone-1-ink); }
@R.tone-2 { background:var(--tone-2); color:var(--tone-2-ink); }
@R.tone-3 { background:var(--tone-3); color:var(--tone-3-ink); }
@R.tone-4 { background:var(--tone-4); color:var(--tone-4-ink); }
@R.tone-5 { background:var(--tone-5); color:var(--tone-5-ink); }
@R:is(.tone-1,.tone-2,.tone-3,.tone-4,.tone-5) :is(.kick,.note,.mark) { color:inherit; }
@container (max-width:560px) { @R > .parts > .fig { font-size:var(--type-52); } @R > .parts > .name { font-size:var(--type-22); } }
@container (max-height:220px) { @R > .parts { gap:calc(var(--gap-sm)/2); } @R > .parts > .fig { font-size:var(--type-40); } @R > .parts > .mark { display:none; } }
''')
for v in ['', 'on','quiet','line']+[f'tone-{i}' for i in range(1,6)]: fixture('card',v or 'default',root('card','card '+v,parts()))

define('pill','A precise one-line capsule aligns the icon, title and supporting note on their optical centre. A fine outline and accent-filled variant express emphasis without shadows.','''
@R { display:flex; align-items:center; justify-content:center; }
@R > .parts { display:flex; align-items:center; justify-content:center; gap:var(--gap-sm); background:var(--accent-soft); color:var(--accent); border:var(--stroke) solid var(--accent-soft); border-radius:999px; padding:var(--gap-sm) var(--pad); max-width:100%; }
@R > .parts > .name { font-size:var(--type-22); }
@R > .parts > .note { font-size:var(--type-16); color:inherit; }
@R > .parts > .mark { font-size:var(--type-24); line-height:var(--label-line); }
@R.on > .parts { background:var(--accent); color:var(--accent-ink); }
@R.quiet > .parts { background:var(--surface); color:var(--ink-2); }
@R.line > .parts { background:var(--page); border-color:var(--line); color:var(--ink); }
@container (max-width:560px) { @R > .parts > .name { font-size:var(--type-18); } @R > .parts > .note { font-size:var(--type-14); } }
@container (max-width:340px) { @R > .parts > .note { display:none; } }
''')
for v in ['', 'on','quiet','line']: fixture('pill',v or 'default',root('pill','pill '+v,'<div class="parts"><span class="mark">✓</span><span class="name">분기 목표 달성</span><span class="note">전년 대비 24% 성장</span></div>'))

define('callout','A concise concluding sentence rests on a soft panel with a fine leading rule. Its strongest phrase uses a deliberate accent emphasis.','''
@R { display:flex; align-items:center; justify-content:center; gap:var(--gap); padding:var(--pad); background:var(--accent-soft); border-left:2px solid var(--accent); border-radius:var(--radius-sm); }
@R > p { max-width:34em; font-size:var(--type-32); line-height:var(--lead-line); letter-spacing:var(--lead-track); }
@R > p b { color:var(--accent); font-weight:var(--name-weight); }
@R > .icon { font-size:var(--type-40); color:var(--accent); }
@container (max-width:600px) { @R > p { font-size:var(--type-24); } @R > .icon { font-size:var(--type-28); } }
@container (max-width:360px) { @R > p { font-size:var(--type-20); } }
''')
fixture('callout','conclusion',root('callout',content='<p>성장의 다음 단계는 <b>고객 경험의 일관성</b>에서 시작합니다.</p>'))
fixture('callout','with-icon',root('callout',content='<span class="icon">↗</span><p>핵심 고객의 재구매율을 높여 <b>지속 가능한 매출 구조</b>를 만듭니다.</p>'))

define('tag','Compact editorial labels and inline marker highlights borrow the references’ restrained chip language. Text is centred with balanced horizontal breathing room.','''
@R { container-type:normal; width:max-content; max-width:100%; }
@R.tag { display:flex; align-items:center; justify-content:center; align-self:center; justify-self:center; background:var(--accent-soft); color:var(--accent); border:var(--stroke) solid var(--line); border-radius:999px; padding:calc(var(--gap-sm)/2) var(--gap-sm); font-size:var(--type-16); font-weight:var(--label-weight); line-height:var(--label-line); }
@R.hl { align-self:center; justify-self:center; background:var(--tone-3); color:var(--tone-3-ink); padding:calc(var(--gap-sm)/3) calc(var(--gap-sm)/2); font-size:var(--type-28); line-height:var(--lead-line); font-weight:var(--name-weight); }
@container (max-width:460px) { @R.tag { font-size:var(--type-14); } @R.hl { font-size:var(--type-20); } }
''')
fixture('tag','label',root('tag','tag','검증된 고객 인사이트'))
fixture('tag','highlight',root('tag','hl','전략의 중심은 고객입니다'))

def items(n=3):
    texts=[('고객 경험을 일관되게 설계합니다','핵심 여정을 분석하고 접점마다 같은 품질을 제공합니다.'),('성과를 데이터로 설명합니다','채널별 지표를 연결해 개선의 우선순위를 정합니다.'),('실행 가능한 변화에 집중합니다','작은 실험을 반복하고 검증된 방법을 확장합니다.'),('부서 간 실행 기준을 맞춥니다','담당과 일정을 명확하게 공유합니다.'),('고객의 목소리를 수집합니다','정성적인 피드백을 지표와 함께 해석합니다.'),('다음 분기 과제를 정리합니다','배운 내용을 기록하고 실행 계획에 반영합니다.'),('좋은 경험을 확산합니다','팀별 사례를 공유하고 공통 기준을 고도화합니다.'),('정기적으로 전략을 점검합니다','환경 변화에 맞춰 가설과 목표를 조정합니다.')]
    return ''.join(f'<div class="item"><p class="name">{a}</p><p class="note">{b}</p></div>' for a,b in texts[:n])
define('list','An open list uses small geometric markers and clear title-to-note spacing. Numbered, checked and ruled versions share the same editorial rhythm.','''
@R { display:flex; flex-direction:column; justify-content:center; gap:var(--gap); counter-reset:entry; padding:var(--gap-sm) 0; }
@R > .item { position:relative; padding-left:var(--gap-lg); counter-increment:entry; }
@R > .item::before { content:""; position:absolute; left:0; top:calc(var(--gap-sm)*.8); width:7px; height:7px; border-radius:50%; background:var(--accent); }
@R.check > .item::before { content:"✓"; width:auto; height:auto; background:none; color:var(--accent); top:0; font-size:var(--type-22); font-weight:var(--label-weight); }
@R.num > .item::before { content:counter(entry,decimal-leading-zero); width:auto; height:auto; border-radius:0; background:none; color:var(--accent); top:0; font-size:var(--type-20); font-weight:var(--label-weight); }
@R.divided > .item { padding-top:var(--gap-sm); border-top:var(--stroke) solid var(--line); }
@R.divided > .item::before { top:calc(var(--gap-sm)*1.8); }
@R > .item > .note { margin-top:calc(var(--gap-sm)/2); }
@R:has(> .item:nth-child(5)) { gap:var(--gap-sm); }
@R:has(> .item:nth-child(5)) > .item > .name { font-size:var(--type-20); }
@R:has(> .item:nth-child(5)) > .item > .note { font-size:var(--type-16); }
@R:has(> .item:nth-child(8)) > .item > .name { font-size:var(--type-18); }
@R:has(> .item:nth-child(8)) > .item > .note { font-size:var(--type-14); }
@container (max-height:460px) { @R:has(> .item:nth-child(8)) > .item > .note { display:none; } }
@container (max-width:420px) { @R > .item > .name { font-size:var(--type-18); } @R:has(> .item:nth-child(5)) > .item > .note { display:none; } }
@container (max-height:300px) { @R > .item > .name { font-size:var(--type-18); } @R > .item > .note { font-size:var(--type-14); } }
@container (max-height:180px) { @R > .item > .note { display:none; } }
''')
for v,n in [('',3),('check',4),('num',5),('divided',3),('check divided',8)]: fixture('list',(v or 'default').replace(' ','-')+f'-{n}',root('list','list '+v,items(n)),'6x4 | 4x6')

define('quote','An editorial quotation uses a large opening mark, a clear voice and a quiet author line. The avatar remains a neutral numbered seat.','''
@R { display:flex; flex-direction:column; justify-content:center; gap:var(--gap-lg); padding:var(--pad); border-top:var(--stroke) solid var(--line); }
@R > blockquote { position:relative; padding-top:var(--gap-lg); font-size:var(--type-36); line-height:var(--lead-line); font-weight:var(--lead-weight); letter-spacing:var(--lead-track); }
@R > blockquote::before { content:"“"; position:absolute; top:calc(var(--gap-sm)*-2); left:0; color:var(--accent); font-size:var(--type-80); font-weight:var(--title-weight); line-height:var(--figure-line); }
@R.big > blockquote { font-size:var(--type-48); }
@R > .by { display:grid; grid-template-columns:auto 1fr; gap:calc(var(--gap-sm)/2) var(--gap-sm); align-items:center; }
@R > .by > .seat { width:56px; grid-row:span 2; }
@R > .by > .name { align-self:end; font-size:var(--type-18); }
@R > .by > .note { align-self:start; font-size:var(--type-14); }
@container (max-width:600px) { @R > blockquote, @R.big > blockquote { font-size:var(--type-26); } }
@container (max-height:250px) { @R > blockquote, @R.big > blockquote { font-size:var(--type-22); } @R > .by > .seat { width:40px; } }
''')
for v in ['', 'big']: fixture('quote',v or 'default',root('quote','quote '+v,'<blockquote>복잡한 의사결정이 명확해졌습니다.<br>우리 팀이 같은 방향을 바라보게 된 변화입니다.</blockquote><div class="by"><div class="seat avatar" data-ph="1"></div><p class="name">김지은 · 사업전략 리드</p><p class="note">에버그린 파트너스, 2026년 고객 인터뷰</p></div>'))

define('metric','Open figures sit on the page without a card surface. Large tabular values, compact labels and fine dividers echo the KPI pages of the supplied decks.','''
@R.stat { display:flex; align-items:center; padding:var(--gap); }
@R.stat > .parts { display:flex; flex-direction:column; gap:var(--gap-sm); width:100%; }
@R.stat .fig { font-size:var(--type-92); color:var(--accent); }
@R.stats { display:flex; align-items:stretch; gap:var(--gap); }
@R.stats > .stat { flex:1; min-width:0; }
@R.stats > .stat + .stat { border-left:var(--stroke) solid var(--line); }
@container (max-width:620px) { @R.stat .fig { font-size:var(--type-56); } @R.stat .name { font-size:var(--type-20); } }
@container (max-width:340px) { @R.stat .fig { font-size:var(--type-40); } @R.stat .note { font-size:var(--type-14); } }
@container (max-height:180px) { @R.stat .fig { font-size:var(--type-36); } @R.stat .note { display:none; } }
''')
fixture('metric','single',root('metric','stat',parts(kick='',fig='150',unit='억',name='분기 누적 매출',mark='')))
for n in [2,3,6]: fixture('metric',f'row-{n}',root('metric','stats',''.join(root('metric','stat',parts(kick='',fig=str(25+i*13),unit='%',name=['신규 고객 증가','고객 유지율 개선','운영 비용 절감'][i%3],note='전년 동기 대비 개선되었습니다.',mark='')) for i in range(n))),'12x3 | 8x6')

define('delta','A quiet before value leads through a fine drawn arrow to a stronger after value. The pair is centred and reads as one measured change.','''
@R { display:flex; align-items:center; justify-content:center; gap:var(--gap-lg); font-size:var(--type-64); font-weight:var(--figure-weight); line-height:var(--figure-line); letter-spacing:var(--figure-track); }
@R > .from { color:var(--mute); }
@R > .to { color:var(--accent); display:flex; align-items:center; gap:var(--gap-lg); }
@R > .to::before { content:"→"; font-size:var(--type-40); font-weight:var(--body-weight); }
@container (max-width:650px) { @R > :is(.from,.to) { font-size:var(--type-40); } @R > .to { gap:var(--gap); } }
@container (max-width:380px) { @R > :is(.from,.to) { font-size:var(--type-28); } @R > .to::before { font-size:var(--type-24); } }
''')
fixture('delta','revenue',root('delta',content='<span class="from">12.1억</span><span class="to">15.6억</span>'))
fixture('delta','conversion',root('delta',content='<span class="from">3.8%</span><span class="to">5.2%</span>'))

define('chart-bar','Fine baseline rules support flat bars with values above and category labels below. Navy emphasis and muted tone alternatives keep quantitative comparison direct.','''
@R { display:flex; align-items:stretch; justify-content:space-around; gap:var(--gap); padding:var(--gap-lg) var(--gap) var(--gap); }
@R > .bar { position:relative; flex:1; min-width:0; border-bottom:var(--stroke) solid var(--line); display:flex; flex-direction:column; align-items:center; justify-content:flex-end; padding-bottom:var(--gap-lg); }
@R > .bar::before { content:""; position:absolute; width:64%; height:calc((100% - var(--gap-lg)*2)*var(--v)/var(--max)); bottom:var(--gap-lg); background:var(--accent-soft); }
@R > .bar.on::before, @R > .bar.tone-1::before { background:var(--tone-1); }
@R > .bar.tone-2::before { background:var(--tone-2); }
@R > .bar.tone-3::before { background:var(--tone-3); }
@R > .bar.tone-4::before { background:var(--tone-4); }
@R > .bar.tone-5::before { background:var(--tone-5); }
@R > .bar > b { position:absolute; bottom:calc(var(--gap-lg) + (100% - var(--gap-lg)*2)*var(--v)/var(--max)); padding-bottom:var(--gap-sm); font-size:var(--type-24); font-weight:var(--figure-weight); line-height:var(--figure-line); white-space:nowrap; }
@R > .bar > span { position:absolute; bottom:calc(var(--gap-sm)/2); font-size:var(--type-16); color:var(--mute); line-height:var(--label-line); text-align:center; }
@R.h { flex-direction:column; padding:var(--gap); }
@R.h > .bar { border-bottom:none; padding:0; min-height:var(--gap-lg); align-items:flex-start; justify-content:center; }
@R.h > .bar::before { left:calc(var(--gap-lg)*3); bottom:20%; height:60%; width:calc((100% - var(--gap-lg)*5)*var(--v)/var(--max)); }
@R.h > .bar > span { position:relative; bottom:auto; max-width:calc(var(--gap-lg)*2.5); text-align:left; }
@R.h > .bar > b { bottom:auto; left:calc(var(--gap-lg)*3.2 + (100% - var(--gap-lg)*5)*var(--v)/var(--max)); padding:0; }
@container (max-width:600px) { @R > .bar > b { font-size:var(--type-18); } @R > .bar > span { font-size:var(--type-14); } }
@container (max-width:360px) { @R > .bar > b { font-size:var(--type-14); } @R > .bar > span { font-size:var(--type-12); } }
''')
for variant,n in [('',4),('h',5),('',8)]:
    body=''.join(f'<div class="bar tone-{i%5+1}" style="--v:{v}"><b>{v}억</b><span>{i+1}분기</span></div>' for i,v in enumerate([42,58,74,92,85,67,80,95][:n]))
    fixture('chart-bar',f'{variant or "vertical"}-{n}',root('chart-bar','bars '+variant,body,'style="--max:100"'),'8x4 | 6x6')

define('chart-line','A restrained navy line connects measured point values above a fine baseline. Compact date labels and open plotting space keep the growth story legible.','''
@R { display:grid; grid-auto-flow:column; grid-auto-columns:minmax(0,1fr); grid-template-rows:minmax(0,1fr) auto; padding:var(--gap-lg) var(--gap) var(--gap); position:relative; isolation:isolate; anchor-scope:all; }
@R > .pt { display:contents; }
@R > .pt > b { position:relative; grid-row:1; align-self:end; height:calc((100% - var(--gap-lg))*var(--v)/var(--max)); display:flex; justify-content:center; align-items:flex-start; anchor-name:var(--studio-spectrum-self); font-size:var(--type-22); font-weight:var(--figure-weight); line-height:var(--figure-line); color:var(--accent); }
@R > .pt > b::after { content:""; position:absolute; top:calc(var(--gap-sm)*2); width:8px; height:8px; border-radius:50%; background:var(--accent); border:var(--stroke) solid var(--page); }
@R > .pt > span { grid-row:2; border-top:var(--stroke) solid var(--line); padding-top:var(--gap-sm); font-size:var(--type-16); color:var(--mute); text-align:center; }
@R > .pt::before, @R > .pt::after { content:""; position:absolute; left:anchor(var(--studio-spectrum-prev) center); right:anchor(var(--studio-spectrum-self) center); pointer-events:none; z-index:-1; }
@R > .pt::before { top:calc(anchor(var(--studio-spectrum-prev) top) + var(--gap-sm)*2 + 3px); bottom:calc(anchor(var(--studio-spectrum-self) top) - var(--gap-sm)*2 - 5px); background:linear-gradient(to top right, var(--page) calc(50% - 1px), var(--accent) 50%, var(--page) calc(50% + 1px)); }
@R > .pt::after { top:calc(anchor(var(--studio-spectrum-self) top) + var(--gap-sm)*2 + 3px); bottom:calc(anchor(var(--studio-spectrum-prev) top) - var(--gap-sm)*2 - 5px); background:linear-gradient(to bottom right, var(--page) calc(50% - 1px), var(--accent) 50%, var(--page) calc(50% + 1px)); }
@R > .pt:first-child::before, @R > .pt:first-child::after { content:none; }
@container (max-width:600px) { @R > .pt > b { font-size:var(--type-16); } @R > .pt > span { font-size:var(--type-12); } }
'''+''.join(f'@R > .pt:nth-child({i}) {{ --studio-spectrum-self:--spectrum-point-{i}; --studio-spectrum-prev:--spectrum-point-{max(1,i-1)}; }}\n' for i in range(1,13)))
for n,vals in [(4,[18,43,39,82]),(6,[18,29,25,54,72,92])]: fixture('chart-line',f'trend-{n}',root('chart-line','lines',''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b><span>{i+1}월</span></div>' for i,v in enumerate(vals)),'style="--max:100"'),'8x4 | 6x6')

define('chart-donut','A clean single-share ring places its figure at the centre and its label beneath. The contrasting remainder stays quiet and structural.','''
@R.donut { position:relative; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:var(--gap-sm); min-height:0; padding:var(--gap); }
@R.donut::before { content:""; position:absolute; width:min(74%,340px); aspect-ratio:1; border-radius:50%; background:conic-gradient(var(--accent) calc(var(--v)*1%),var(--surface-2) 0);  }
@R.donut::after { content:""; position:absolute; width:min(54%,248px); aspect-ratio:1; border-radius:50%; background:var(--page); }
@R.donut > .fig { z-index:1; font-size:var(--type-64); color:var(--accent); }
@R.donut > .name { z-index:1; font-size:var(--type-18); text-align:center; max-width:60%; }
@R.donuts { display:flex; gap:var(--gap); }
@R.donuts > .donut { flex:1; min-width:0; }
@container (max-width:420px) { @R.donut > .fig { font-size:var(--type-40); } @R.donut > .name { font-size:var(--type-14); } }
@container (max-width:250px) { @R.donut > .fig { font-size:var(--type-28); } @R.donut > .name { font-size:var(--type-12); } }
''')
fixture('chart-donut','single',root('chart-donut','donut','<p class="fig">65<small>%</small></p><p class="name">온라인 매출 비중</p>','style="--v:65"'),'4x4 | 6x3')
for n in [2,3,4]: fixture('chart-donut',f'row-{n}',root('chart-donut','donuts',''.join(root('chart-donut','donut',f'<p class="fig">{v}<small>%</small></p><p class="name">{name}</p>',f'style="--v:{v}"') for v,name in [(65,'온라인 매출'),(35,'오프라인 매출'),(48,'신규 고객'),(72,'고객 만족도')][:n])),'12x4 | 8x6')

define('gauge','A flat progress track pairs its title with a right-aligned numerical value. The filled width directly follows the supplied percentage.','''
@R { display:grid; grid-template-columns:1fr auto; grid-template-rows:auto 10px; align-content:center; gap:var(--gap-sm) var(--gap); }
@R::before, @R::after { content:""; grid-column:1/-1; grid-row:2; border-radius:999px; }
@R::before { background:var(--surface-2); }
@R::after { width:calc(var(--v)*1%); background:var(--accent); }
@R > .name { grid-column:1; grid-row:1; font-size:var(--type-24); }
@R > .fig { grid-column:2; grid-row:1; font-size:var(--type-30); color:var(--accent); }
@container (max-width:550px) { @R > .name { font-size:var(--type-18); } @R > .fig { font-size:var(--type-22); } }
@container (max-width:320px) { @R > .name { font-size:var(--type-14); } @R > .fig { font-size:var(--type-18); } }
''')
for v,name in [(90,'브랜드 개편 프로젝트'),(67,'신규 캠페인 제작 및 운영')]: fixture('gauge',f'progress-{v}',root('gauge','meter',f'<p class="name">{name}</p><p class="fig">{v}%</p>',f'style="--v:{v}"'),'6x2 | 3x3')

define('table','An open ruled table favours generous cell padding, quiet row rules and a single highlighted decision column. Numerical values use tabular alignment.','''
@R { display:flex; align-items:center; }
@R > .table { border-collapse:collapse; width:100%; table-layout:fixed; color:var(--ink); font-family:var(--font-body); font-size:var(--type-18); line-height:var(--body-line); }
@R :is(th,td) { padding:var(--gap-sm) var(--gap); text-align:left; border-bottom:var(--stroke) solid var(--line); overflow-wrap:anywhere; }
@R th { border-top:var(--stroke) solid var(--ink); color:var(--ink-2); font-size:var(--type-16); font-weight:var(--label-weight); }
@R .num { text-align:right; font-variant-numeric:tabular-nums; }
@R .pick { background:var(--accent-soft); color:var(--accent); font-weight:var(--name-weight); }
@container (max-width:700px) { @R > .table { font-size:var(--type-14); } @R th { font-size:var(--type-14); } @R :is(th,td) { padding:var(--gap-sm); } }
@container (max-height:260px) { @R :is(th,td) { padding:calc(var(--gap-sm)/2) var(--gap-sm); } }
''')
for n in [3,5]:
    rows=''.join(f'<tr><td>{name}</td><td class="num">{40+i*11}억</td><td class="num pick">{52+i*12}억</td><td class="num">{112+i*4}%</td></tr>' for i,name in enumerate(['온라인 사업','파트너 사업','기업 솔루션','신규 시장 개발','브랜드 캠페인'][:n]))
    fixture('table',f'performance-{n}',root('table','tablebox','<table class="table"><thead><tr><th>사업 부문</th><th class="num">전년 실적</th><th class="num pick">올해 실적</th><th class="num">달성률</th></tr></thead><tbody>'+rows+'</tbody></table>'),'8x4 | 6x6')

define('legend','Small square keys and calm labels organise chart categories in one centred row. Each key uses the same tone tokens as the data elements.','''
@R { display:flex; flex-wrap:wrap; align-content:center; align-items:center; justify-content:center; gap:var(--gap) var(--gap-lg); }
@R > .key { display:flex; align-items:center; gap:var(--gap-sm); color:var(--ink-2); font-size:var(--type-18); }
@R > .key::before { content:""; width:12px; height:12px; background:var(--tone-1); }
@R > .key.tone-2::before { background:var(--tone-2); }
@R > .key.tone-3::before { background:var(--tone-3); }
@R > .key.tone-4::before { background:var(--tone-4); }
@R > .key.tone-5::before { background:var(--tone-5); }
@container (max-width:500px) { @R > .key { font-size:var(--type-14); } }
''')
for n in [3,5]: fixture('legend',f'keys-{n}',root('legend','legend',''.join(f'<span class="key tone-{i+1}">{name}</span>' for i,name in enumerate(['온라인 사업','오프라인 사업','파트너 채널','기업 고객','신규 사업'][:n]))),'6x2 | 3x4')

def seq(n,member='step',date=False):
    names=['목표 정의','고객 이해','전략 수립','실행 검증','성과 확장','지속 개선','다음 단계','새로운 도약']
    return ''.join(f'<div class="{member}{" on" if date and i==1 else ""}">'+(f'<p class="kick">2026.{i+1:02}</p>' if date else f'<span class="mark">{i+1:02}</span>')+f'<p class="name">{names[i]}</p><p class="note">고객의 요구를 확인하고 실행 기준을 구체화합니다.</p></div>' for i in range(n))
define('steps','Numbered circles and fine connectors establish a calm left-to-right sequence. In the vertical version, the rule moves to the margin while titles retain their alignment.','''
@R { display:flex; align-items:center; gap:var(--gap); }
@R > .step { position:relative; flex:1; align-self:stretch; display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); padding-top:var(--gap); min-width:0; }
@R > .step > .mark { width:48px; height:48px; display:flex; align-items:center; justify-content:center; border:var(--stroke) solid var(--line); border-radius:50%; background:var(--page); color:var(--accent); font-size:var(--type-18); font-weight:var(--label-weight); z-index:1; }
@R > .step:not(:last-child)::before { content:""; position:absolute; left:48px; right:calc(var(--gap)*-1); top:calc(50% - var(--gap-lg)*1.15); height:var(--stroke); background:var(--line); }
@R.col { flex-direction:column; align-items:stretch; gap:var(--gap-sm); }
@R.col > .step { display:grid; grid-template-columns:48px 1fr; gap:calc(var(--gap-sm)/2) var(--gap); padding:0; align-content:center; }
@R.col > .step > .mark { grid-row:span 2; }
@R.col > .step:not(:last-child)::before { left:24px; right:auto; top:50%; bottom:calc(var(--gap)*-1); width:var(--stroke); height:auto; }
@container (max-width:650px) { @R > .step > .name { font-size:var(--type-20); } @R > .step > .note { font-size:var(--type-14); } }
@container (max-height:240px) { @R > .step > .note { display:none; } }
''')
for v,n in [('',3),('',5),('col',4)]: fixture('steps',f'{v or "row"}-{n}',root('steps','steps '+v,seq(n)),'8x4 | 6x6' if not v else '4x6')

define('timeline','A fine track and small circular stops pair dates with milestone titles. A filled active stop marks the present without breaking the quiet structure.','''
@R { display:flex; align-items:center; gap:var(--gap); }
@R > .stop { position:relative; flex:1; min-width:0; padding-top:var(--gap-lg); border-top:var(--stroke) solid var(--line); }
@R > .stop::before { content:""; position:absolute; left:0; top:-5px; width:9px; height:9px; background:var(--page); border:var(--stroke) solid var(--accent); border-radius:50%; }
@R > .stop.on::before { background:var(--accent); }
@R > .stop > .kick { margin-bottom:var(--gap-sm); }
@R > .stop > .note { margin-top:var(--gap-sm); }
@R.alt > .stop:nth-child(even) { transform:translateY(-40%); }
@R.col { flex-direction:column; align-items:stretch; gap:0; }
@R.col > .stop { padding:var(--gap-sm) var(--gap-lg); border-top:none; border-left:var(--stroke) solid var(--line); }
@R.col > .stop::before { top:var(--gap); left:-5px; }
@container (max-height:450px) { @R.col > .stop { padding:calc(var(--gap-sm)/2) var(--gap-lg); } @R.col > .stop > .note { display:none; } @R.col > .stop > .name { font-size:var(--type-20); } @R.col > .stop > .kick { font-size:var(--type-12); } }
@container (max-width:700px) { @R > .stop > .name { font-size:var(--type-20); } @R > .stop > .note { font-size:var(--type-14); } }
@container (max-height:260px) { @R > .stop > .note { display:none; } }
''')
for v,n in [('',4),('alt',3),('col',5)]: fixture('timeline',f'{v or "row"}-{n}',root('timeline','track '+v,seq(n,'stop',True)),'8x4 | 6x6')

# The circular relationship families use the same geometric placement vocabulary.
def radial(folder,member,n):
    labels=['고객 이해','전략 설계','실행 관리','성과 분석','경험 개선','가치 확장']
    return root(folder,content='<div class="core">지속 가능한 성장</div>'+''.join(f'<div class="{member}">'+(f'<span class="mark">{i+1:02}</span><p class="name">{labels[i]}</p><p class="note">연결된 실행으로 가치를 높입니다.</p>' if folder=='hub' else labels[i])+'</div>' for i in range(n)))
for folder,member in [('cycle','node'),('hub','spoke')]:
    css='''
@R { position:relative; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); grid-template-rows:repeat(3,minmax(0,1fr)); gap:var(--gap); padding:var(--gap); }
@R > .core { grid-column:2; grid-row:2; display:flex; align-items:center; justify-content:center; text-align:center; border-radius:50%; border:var(--stroke) solid var(--accent); color:var(--accent); background:var(--accent-soft); padding:var(--gap-sm); font-size:var(--type-24); font-weight:var(--name-weight); z-index:2; }
@R > .MEMBER { position:relative; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; gap:calc(var(--gap-sm)/2); background:var(--surface); border:var(--stroke) solid var(--line); border-radius:var(--radius); padding:var(--gap-sm); font-size:var(--type-22); z-index:1; }
@R > .MEMBER:nth-child(2) { grid-area:1/2; }
@R > .MEMBER:nth-child(3) { grid-area:1/3; }
@R > .MEMBER:nth-child(4) { grid-area:3/3; }
@R > .MEMBER:nth-child(5) { grid-area:3/2; }
@R > .MEMBER:nth-child(6) { grid-area:3/1; }
@R > .MEMBER:nth-child(7) { grid-area:1/1; }
@R > .MEMBER > .mark { font-size:var(--type-14); color:var(--accent); }
@R > .MEMBER > .name { font-size:var(--type-20); }
@R > .MEMBER > .note { font-size:var(--type-14); }
@container (max-width:650px) { @R > .core { font-size:var(--type-18); } @R > .MEMBER, @R > .MEMBER > .name { font-size:var(--type-16); } @R > .MEMBER > .note { font-size:var(--type-12); } }
@container (max-width:420px) { @R > .MEMBER > .note { display:none; } }
'''.replace('MEMBER',member)
    if folder=='cycle': css+='''
@R::before { content:""; position:absolute; inset:17% 19%; border:var(--stroke) solid var(--line); border-radius:50%; }
@R > .node::after { content:"→"; position:absolute; right:calc(var(--gap)*-1); color:var(--accent); font-size:var(--type-24); }
@R > .node:nth-child(n+5)::after { content:"←"; right:auto; left:calc(var(--gap)*-1); }
'''
    else: css+='''
@R::before { content:""; position:absolute; top:17%; bottom:17%; left:50%; width:var(--stroke); background:var(--line); }
@R::after { content:""; position:absolute; inset:17% 17%; background:linear-gradient(to bottom right,var(--page) calc(50% - 1px),var(--line) 50%,var(--page) calc(50% + 1px)); }
'''
    css += """
@R > .core { position:absolute; grid-area:auto; left:38%; top:37%; width:24%; height:26%; }
@R > .MEMBER:nth-child(n) { position:absolute; grid-area:auto; width:26%; height:26%; }
@R > .MEMBER:nth-child(2) { left:37%; top:0; }
@R > .MEMBER:nth-child(3) { left:74%; top:37%; }
@R > .MEMBER:nth-child(4) { left:37%; top:74%; }
@R > .MEMBER:nth-child(5) { left:0; top:37%; }
@R:has(> .MEMBER:nth-child(4):last-child) > .MEMBER:nth-child(3) { left:68%; top:70%; }
@R:has(> .MEMBER:nth-child(4):last-child) > .MEMBER:nth-child(4) { left:6%; top:70%; }
@R:has(> .MEMBER:nth-child(6):last-child) > .MEMBER:nth-child(3) { left:74%; top:24%; }
@R:has(> .MEMBER:nth-child(6):last-child) > .MEMBER:nth-child(4) { left:61%; top:74%; }
@R:has(> .MEMBER:nth-child(6):last-child) > .MEMBER:nth-child(5) { left:13%; top:74%; }
@R:has(> .MEMBER:nth-child(6):last-child) > .MEMBER:nth-child(6) { left:0; top:24%; }
@R:has(> .MEMBER:nth-child(7):last-child) > .MEMBER:nth-child(2) { left:16%; top:0; }
@R:has(> .MEMBER:nth-child(7):last-child) > .MEMBER:nth-child(3) { left:58%; top:0; }
@R:has(> .MEMBER:nth-child(7):last-child) > .MEMBER:nth-child(4) { left:74%; top:37%; }
@R:has(> .MEMBER:nth-child(7):last-child) > .MEMBER:nth-child(5) { left:58%; top:74%; }
@R:has(> .MEMBER:nth-child(7):last-child) > .MEMBER:nth-child(6) { left:16%; top:74%; }
@R:has(> .MEMBER:nth-child(7):last-child) > .MEMBER:nth-child(7) { left:0; top:37%; }
""".replace('MEMBER',member)
    if folder=='hub':
        css += """
@R { padding:0; }
@R::before, @R::after { content:none; }
@R > .spoke::before { content:""; position:absolute; left:50%; top:50%; width:hypot(calc((50 - var(--studio-spectrum-x))*1cqw),calc((50 - var(--studio-spectrum-y))*1cqh)); height:var(--stroke); background:var(--line); transform-origin:0 0; transform:rotate(atan2(calc((50 - var(--studio-spectrum-y))*1cqh),calc((50 - var(--studio-spectrum-x))*1cqw))); z-index:-2; }
@R > .spoke::after { content:""; position:absolute; inset:0; background:var(--surface); border-radius:var(--radius); z-index:-1; }
"""
        positions={3:[(50,13),(81,83),(19,83)],4:[(50,13),(87,50),(50,87),(13,50)],5:[(50,13),(87,37),(74,87),(26,87),(13,37)],6:[(29,13),(71,13),(87,50),(71,87),(29,87),(13,50)]}
        for total,points in positions.items():
            for number,(x,y) in enumerate(points,2):
                css+=f'@R:has(> .spoke:nth-child({total+1}):last-child) > .spoke:nth-child({number}) {{ --studio-spectrum-x:{x}; --studio-spectrum-y:{y}; }}\n'
    define(folder,'Radial relationships combine a quiet central statement, precise surrounding panels and hairline connections. The centre retains visual priority as member count changes.',css)
    for n in [3,4,5,6]:fixture(folder,f'nodes-{n}',radial(folder,member,n),'8x6 | 12x5')

define('funnel','Wide flat stages descend toward a focused outcome. Each supplied percentage determines the stage width while centred names and values maintain clear comparison.','''
@R { display:flex; flex-direction:column; justify-content:center; align-items:center; gap:var(--gap-sm); padding:var(--gap); }
@R > .stage { display:flex; justify-content:space-between; align-items:center; gap:var(--gap-sm); min-width:24%; width:calc(var(--v)*1%); flex:1; max-height:calc(var(--gap-lg)*2); padding:var(--gap-sm) var(--pad); background:var(--accent-soft); border:var(--stroke) solid var(--line); border-radius:var(--radius-sm); }
@R > .stage:last-child { background:var(--accent); color:var(--accent-ink); }
@R > .stage > .fig { font-size:var(--type-28); }
@R > .stage > .name { font-size:var(--type-22); }
@container (max-width:650px) { @R > .stage > .name { font-size:var(--type-18); } @R > .stage > .fig { font-size:var(--type-22); } }
@container (max-width:420px) { @R > .stage > .name { font-size:var(--type-14); } @R > .stage > .fig { font-size:var(--type-18); } }
''')
for n in [3,4,6]: fixture('funnel',f'stages-{n}',root('funnel',content=''.join(f'<div class="stage" style="--v:{100-i*10}"><span class="name">{name}</span><span class="fig">{100-i*13}%</span></div>' for i,name in enumerate(['유입','탐색','관심','상담','전환','재구매'][:n]))),'8x4 | 6x6')

define('pyramid','A compact stepped pyramid uses increasingly broad editorial bands. Labels and notes sit within each level without pictorial decoration.','''
@R { display:flex; flex-direction:column; align-items:center; justify-content:center; gap:calc(var(--gap-sm)/2); padding:var(--gap); }
@R > .level { width:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:calc(var(--gap-sm)/2); flex:1; max-height:calc(var(--gap-lg)*2.5); background:var(--surface); border-bottom:var(--stroke) solid var(--line); padding:var(--gap-sm) var(--pad); text-align:center; }
@R > .level:nth-child(1) { width:38%; background:var(--accent); color:var(--accent-ink); }
@R > .level:nth-child(1) > .note { color:var(--accent-ink); }
@R > .level:nth-child(2) { width:54%; background:var(--accent-soft); }
@R > .level:nth-child(3) { width:70%; }
@R > .level:nth-child(4) { width:86%; }
@R > .level > .name { font-size:var(--type-22); }
@R > .level > .note { font-size:var(--type-16); }
@container (max-width:650px) { @R > .level > .name { font-size:var(--type-18); } @R > .level > .note { font-size:var(--type-14); } }
@container (max-height:300px) { @R > .level > .note { display:none; } }
''')
for n in [3,4,5]: fixture('pyramid',f'levels-{n}',root('pyramid',content=''.join(f'<div class="level"><p class="name">{name}</p><p class="note">공유된 실행 기준으로 성장을 만듭니다.</p></div>' for name in ['고객 가치','핵심 전략','실행 체계','협업 구조','데이터 기반'][:n])),'8x5 | 6x6')

define('matrix','An open two-by-two field uses hairline quadrant borders and concise axis labels. A soft navy quadrant identifies the recommended focus.','''
@R { position:relative; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:repeat(2,minmax(0,1fr)); gap:var(--gap-sm); padding:var(--gap-lg); }
@R > .cell { padding:var(--pad); background:var(--surface); display:flex; align-items:center; justify-content:center; text-align:center; font-size:var(--type-28); font-weight:var(--name-weight); border:var(--stroke) solid var(--line); }
@R > .cell.on { background:var(--accent-soft); color:var(--accent); border-color:var(--accent); }
@R > .axis-x { position:absolute; bottom:0; left:var(--gap-lg); right:var(--gap-lg); display:flex; justify-content:space-between; font-size:var(--type-14); color:var(--mute); }
@R > .axis-y { position:absolute; top:var(--gap-lg); bottom:var(--gap-lg); left:0; display:flex; flex-direction:column; justify-content:space-between; font-size:var(--type-14); color:var(--mute); }
@container (max-width:650px) { @R > .cell { font-size:var(--type-22); } }
@container (max-width:420px) { @R > .cell { font-size:var(--type-16); } }
''')
for i in [0,3]: fixture('matrix',f'priority-{i+1}',root('matrix',content='<div class="axis-x"><span>낮은 실행 난이도</span><span>높은 실행 난이도</span></div><div class="axis-y"><span>높은 효과</span><span>낮은 효과</span></div>'+''.join(f'<div class="cell{" on" if j==i else ""}">{name}</div>' for j,name in enumerate(['즉시 실행','전략 과제','운영 개선','선택적 검토']))),'8x5 | 6x6')

define('venn','Fine circular sets overlap with a deliberately quiet centre. Restrained fills and centred set labels express shared value without gradients.','''
@R { position:relative; display:flex; align-items:center; justify-content:center; padding:var(--gap-lg); }
@R > .set { width:44%; aspect-ratio:1; max-height:90%; border-radius:50%; border:var(--stroke) solid var(--accent); background:var(--accent-soft); display:flex; align-items:center; justify-content:center; padding:var(--gap); margin:0 calc(var(--gap-lg)*-.5); }
@R > .set.on { background:var(--tone-4); color:var(--tone-4-ink); }
@R > .set > .name { font-size:var(--type-28); text-align:center; }
@R > .core { position:absolute; left:40%; right:40%; text-align:center; font-size:var(--type-20); font-weight:var(--name-weight); color:var(--accent); background:var(--page); border:var(--stroke) solid var(--line); border-radius:var(--radius); padding:var(--gap-sm); z-index:2; }
@container (max-width:650px) { @R > .set > .name { font-size:var(--type-20); } @R > .core { font-size:var(--type-16); } }
@container (max-width:420px) { @R > .set > .name { font-size:var(--type-14); } @R > .core { font-size:var(--type-12); } }
''')
for n in [2,3]:fixture('venn',f'sets-{n}',root('venn',content=''.join(f'<div class="set{" on" if i==1 else ""}"><p class="name">{name}</p></div>' for i,name in enumerate(['고객 경험','비즈니스 가치','실행 역량'][:n]))+'<div class="core">지속 성장</div>'),'8x5 | 6x6')

define('hierarchy','A clear root label anchors a row of ruled branches. Small branch panels and open leaf labels make organisational ownership easy to scan.','''
@R { position:relative; display:grid; grid-auto-columns:minmax(0,1fr); grid-auto-flow:column; grid-template-rows:auto 1fr; gap:var(--gap-lg) var(--gap); padding:var(--gap); }
@R { grid-template-columns:repeat(4,minmax(0,1fr)); }
@R:has(> .branch:nth-child(3):last-child) { grid-template-columns:repeat(2,minmax(0,1fr)); }
@R:has(> .branch:nth-child(4):last-child) { grid-template-columns:repeat(3,minmax(0,1fr)); }
@R > .root { grid-column:1/-1; justify-self:center; background:var(--accent); color:var(--accent-ink); padding:var(--gap-sm) var(--gap-lg); border-radius:var(--radius-sm); font-size:var(--type-28); font-weight:var(--name-weight); }
@R > .root { position:relative; }
@R > .root::after { content:""; position:absolute; top:100%; left:50%; width:var(--stroke); height:var(--gap-lg); background:var(--line); }
@R > .branch { grid-row:2; display:flex; flex-direction:column; align-items:stretch; gap:var(--gap-sm); border-top:var(--stroke) solid var(--line); padding-top:var(--gap); position:relative; }
@R > .branch::before { content:""; position:absolute; top:calc(var(--gap-lg)*-1); height:var(--gap-lg); width:var(--stroke); background:var(--line); left:50%; }
@R > .branch > .node { background:var(--accent-soft); color:var(--accent); padding:var(--gap-sm); text-align:center; font-size:var(--type-22); font-weight:var(--name-weight); }
@R > .branch > .leaf { border-bottom:var(--stroke) solid var(--line); padding:var(--gap-sm); text-align:center; font-size:var(--type-18); }
@container (max-width:650px) { @R > .root { font-size:var(--type-22); } @R > .branch > .node { font-size:var(--type-18); } @R > .branch > .leaf { font-size:var(--type-14); } }
''')
for n in [2,3,4]:fixture('hierarchy',f'branches-{n}',root('hierarchy','org','<div class="root">성장전략 본부</div>'+''.join(f'<div class="branch"><div class="node">{name}</div><div class="leaf">기획 및 운영</div><div class="leaf">분석 및 개선</div></div>' for name in ['고객전략팀','브랜드팀','제품성장팀','파트너팀'][:n])),'8x5 | 6x6')

define('flowchart','A modular flow uses crisp outlined nodes, a softened start and end, and a diamond decision. Fine directional arrows connect only the explicitly marked edges.','''
@R { display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); grid-template-rows:repeat(5,minmax(0,1fr)); gap:var(--gap); padding:var(--gap); }
@R > .node { position:relative; display:flex; align-items:center; justify-content:center; text-align:center; padding:var(--gap-sm); border:var(--stroke) solid var(--line); border-radius:var(--radius-sm); background:var(--surface); font-size:var(--type-20); font-weight:var(--name-weight); }
@R > .node.start, @R > .node.end { border-radius:999px; background:var(--accent); color:var(--accent-ink); border-color:var(--accent); }
@R > .node.ask { background:var(--accent-soft); color:var(--accent); border-color:var(--accent); }
@R > .node.to-r::after { content:"→"; position:absolute; left:100%; width:var(--gap); text-align:center; color:var(--accent); }
@R > .node.to-l::after { content:"←"; position:absolute; right:100%; width:var(--gap); text-align:center; color:var(--accent); }
@R > .node.to-d::before { content:"↓"; position:absolute; top:100%; height:var(--gap); color:var(--accent); }
@R > .node.to-u::before { content:"↑"; position:absolute; bottom:100%; height:var(--gap); color:var(--accent); }
@container (max-width:700px) { @R > .node { font-size:var(--type-16); } }
@container (max-width:450px) { @R > .node { font-size:var(--type-12); } }
''')
fixture('flowchart','linear',root('flowchart',content='<div class="node start to-r" style="grid-column:1;grid-row:3">목표 수립</div><div class="node to-r" style="grid-column:2;grid-row:3">고객 분석</div><div class="node ask to-r" style="grid-column:3;grid-row:3">가설 검증</div><div class="node to-r" style="grid-column:4;grid-row:3">전략 실행</div><div class="node end" style="grid-column:5;grid-row:3">성과 확인</div>'),'10x4 | 8x6')
fixture('flowchart','decision',root('flowchart',content='<div class="node start to-d" style="grid-column:3;grid-row:1">고객 요청</div><div class="node ask to-r to-d" style="grid-column:3;grid-row:2">기준 충족?</div><div class="node to-d" style="grid-column:4;grid-row:2">보완 요청</div><div class="node to-d" style="grid-column:3;grid-row:3">검토 승인</div><div class="node end" style="grid-column:3;grid-row:4">처리 완료</div>'),'8x6')

define('architecture','Horizontal system layers use a narrow title rail and centred chips. A restrained rule, rather than a heavy enclosure, separates each layer.','''
@R { display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); }
@R > .layer { display:flex; align-items:center; justify-content:flex-start; flex-wrap:wrap; gap:var(--gap-sm); padding:var(--gap); background:var(--surface); border-left:2px solid var(--accent); border-bottom:var(--stroke) solid var(--line); }
@R > .layer > .name { flex:0 0 22%; font-size:var(--type-22); }
@R > .layer > .chip { display:flex; align-items:center; justify-content:center; text-align:center; padding:var(--gap-sm) var(--gap); background:var(--page); border:var(--stroke) solid var(--line); border-radius:var(--radius-sm); font-size:var(--type-16); line-height:var(--label-line); }
@container (max-width:700px) { @R > .layer { padding:var(--gap-sm); } @R > .layer > .name { font-size:var(--type-18); flex-basis:100%; } @R > .layer > .chip { font-size:var(--type-14); padding:calc(var(--gap-sm)/2) var(--gap-sm); } }
@container (max-height:300px) { @R > .layer { padding:var(--gap-sm); } @R > .layer > .chip { padding:calc(var(--gap-sm)/2) var(--gap-sm); } }
''')
for n in [3,5]:fixture('architecture',f'layers-{n}',root('architecture','arch',''.join(f'<div class="layer"><p class="name">{name}</p><span class="chip">{a}</span><span class="chip">{b}</span><span class="chip">공통 운영 기준</span></div>' for name,a,b in [('경험 계층','고객 포털','브랜드 웹사이트'),('서비스 계층','고객 관리','프로젝트 관리'),('데이터 계층','분석 저장소','실시간 지표'),('연결 계층','파트너 API','이벤트 허브'),('운영 계층','권한 관리','품질 모니터링')][:n])),'8x5 | 6x6')

define('versus','Two open editorial columns contrast current and future approaches. A compact central versus mark separates them while a soft accent field signals the chosen side.','''
@R { display:grid; grid-template-columns:minmax(0,1fr) auto minmax(0,1fr); align-items:stretch; gap:var(--gap); }
@R > .side { padding:var(--pad); border-top:var(--stroke) solid var(--line); background:var(--surface); display:flex; flex-direction:column; justify-content:center; gap:var(--gap); }
@R > .side.on { background:var(--accent-soft); border-top-color:var(--accent); }
@R > .side > .name { font-size:var(--type-32); }
@R > .side > .list { flex:1; min-height:0; }
@R > .vs { align-self:center; font-size:var(--type-18); font-weight:var(--label-weight); color:var(--mute); }
@container (max-width:700px) { @R > .side > .name { font-size:var(--type-24); } }
@container (max-width:450px) { @R > .side > .name { font-size:var(--type-18); } }
''')
for n in [2,3]:fixture('versus',f'comparison-{n}',root('versus',content='<div class="side"><p class="name">기존 운영 방식</p>'+root('list','list',items(n))+'</div><b class="vs">VS</b><div class="side on"><p class="name">통합 성장 전략</p>'+root('list','list check',items(n))+'</div>'),'10x5 | 8x6')

define('pricing','Pricing plans use open rules and clear price hierarchy, with a softly highlighted recommended plan. Feature lists inherit the same checked editorial rhythm.','''
@R.plans { display:flex; align-items:stretch; gap:var(--gap); }
@R.plans > .plan { flex:1; min-width:0; }
@R.plan { display:flex; flex-direction:column; justify-content:center; gap:var(--gap); padding:var(--pad); background:var(--surface); border-top:2px solid var(--line); border-radius:var(--radius); }
@R.plan.on { background:var(--accent-soft); border-top-color:var(--accent); }
@R.plan > .name { font-size:var(--type-26); }
@R.plan > .price { display:flex; align-items:baseline; gap:var(--gap-sm); }
@R.plan > .price > .fig { font-size:var(--type-64); color:var(--accent); }
@R.plan > .price > small { font-size:var(--type-16); color:var(--mute); }
@R.plan > .list { flex:1; }
@R.plan > .list .name { font-size:var(--type-18); }
@R.plan > .list .note { font-size:var(--type-14); }
@R.plan > .tag { align-self:flex-start; }
@container (max-width:430px) { @R.plan > .price > .fig { font-size:var(--type-40); } @R.plan > .name { font-size:var(--type-22); } @R.plan > .list .name { font-size:var(--type-16); } @R.plan > .list .note { display:none; } }
@container (max-height:300px) { @R.plan > .list .note { display:none; } }
''')
def plan(i): return root('pricing','plan'+(' on' if i==1 else ''),f'<p class="name">{["스타터","비즈니스","엔터프라이즈","파트너"][i]}</p><div class="price"><span class="fig">{[29,59,99,149][i]}만</span><small>원 / 월</small></div>'+root('list','list check',items(2))+(root('tag','tag','가장 많이 선택한 플랜') if i==1 else ''))
fixture('pricing','single',plan(1),'4x6 | 6x5')
for n in [2,3,4]:fixture('pricing',f'plans-{n}',root('pricing','plans',''.join(plan(i) for i in range(n))),'12x6')

define('person','A neutral portrait seat leads a concise name and role. Groups maintain equal portrait proportions and aligned editorial captions.','''
@R.people { display:flex; align-items:stretch; gap:var(--gap); }
@R.people > .person { flex:1; min-width:0; }
@R.person { display:flex; flex-direction:column; align-items:flex-start; justify-content:center; gap:var(--gap-sm); }
@R.person > .seat { width:100%; max-height:68%; flex:1; }
@R.person > .seat.avatar { width:min(100%,240px); flex:none; align-self:center; }
@R.person > .name { font-size:var(--type-26); }
@R.person > .note { font-size:var(--type-18); }
@R.person > .list { flex:1; }
@container (max-width:400px) { @R.person > .name { font-size:var(--type-20); } @R.person > .note { font-size:var(--type-14); } }
@container (max-width:220px) { @R.person > .name { font-size:var(--type-16); } @R.person > .note { font-size:var(--type-12); } }
''')
def person(i,avatar=False):return root('person','person',f'<div class="seat {"avatar" if avatar else "portrait"}" data-ph="{i+1}"></div><p class="name">{["김지은","박서준","이민지","정도윤","최하린","윤서진"][i]}</p><p class="note">{["사업전략 리드","고객경험 디자이너","데이터 분석가","브랜드 매니저","프로젝트 매니저","파트너십 리드"][i]}</p>')
fixture('person','single-portrait',person(0),'4x6')
fixture('person','single-avatar',person(1,True),'4x5')
for n in [3,5,6]:fixture('person',f'people-{n}',root('person','people',''.join(person(i) for i in range(n))),'12x6')

define('logo-group','Equal neutral logo seats form a measured horizontal strip, separated by ample air and a quiet running rule. Denser groups wrap into a regular grid.','''
@R { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); align-content:center; gap:var(--gap-lg); padding:var(--pad); border-top:var(--stroke) solid var(--line); border-bottom:var(--stroke) solid var(--line); }
@R:has(> :nth-child(7)) { grid-template-columns:repeat(4,minmax(0,1fr)); }
@R > .seat.logo { width:100%; aspect-ratio:3/1; background:var(--surface); }
@container (max-width:650px) { @R > .seat.logo { aspect-ratio:2/1; } }
''')
for n in [3,6,12]:fixture('logo-group',f'logos-{n}',root('logo-group','logos',''.join(f'<div class="seat logo" data-ph="{i+1}"></div>' for i in range(n))),'8x4 | 6x6')

define('image-frame','A fine crisp frame and generous neutral seat reserve a photograph or screen without reproducing its bitmap. The quiet border matches the collection’s editorial rules.','''
@R { display:flex; padding:var(--gap-sm); border:var(--stroke) solid var(--line); background:var(--page); border-radius:var(--radius-sm); }
@R > .seat { width:100%; height:100%; background:var(--surface-2); }
@container (max-width:400px) { @R > .seat { border-radius:var(--radius-sm); } }
''')
fixture('image-frame','landscape',root('image-frame','frame','<div class="seat" data-ph="1"></div>'),'6x3 | 4x6')
fixture('image-frame','portrait',root('image-frame','frame','<div class="seat portrait" data-ph="2"></div>'),'4x6 | 6x3')

define('agenda','A ruled editorial contents list pairs a small two-digit index with a strong title and quiet note. The active entry gains a restrained accent field.','''
@R { display:flex; flex-direction:column; justify-content:center; }
@R > .entry { display:grid; grid-template-columns:var(--gap-lg) minmax(0,1fr) minmax(0,1fr); gap:var(--gap); align-items:center; border-top:var(--stroke) solid var(--line); padding:var(--gap) var(--gap-sm); }
@R > .entry:last-child { border-bottom:var(--stroke) solid var(--line); }
@R:has(> .entry:nth-child(8)) > .entry { padding:var(--gap-sm); }
@R:has(> .entry:nth-child(8)) > .entry > .name { font-size:var(--type-20); }
@R:has(> .entry:nth-child(8)) > .entry > .note { font-size:var(--type-14); }
@R > .entry.on { background:var(--accent-soft); color:var(--accent); }
@R > .entry > .mark { font-size:var(--type-16); color:var(--mute); font-weight:var(--label-weight); }
@R > .entry > .name { font-size:var(--type-26); }
@R > .entry > .note { font-size:var(--type-16); }
@container (max-width:700px) { @R > .entry > .name { font-size:var(--type-20); } @R > .entry > .note { font-size:var(--type-14); } }
@container (max-width:400px) { @R > .entry > .note { display:none; } }
@container (max-height:420px) { @R > .entry { padding:var(--gap-sm); } @R > .entry > .name { font-size:var(--type-20); } }
''')
for n in [3,5,8]:fixture('agenda',f'entries-{n}',root('agenda',content=''.join(f'<div class="entry{" on" if i==1 else ""}"><span class="mark">{i+1:02}</span><p class="name">{name}</p><p class="note">성과의 배경과 다음 실행 방향</p></div>' for i,name in enumerate(['시장과 고객','핵심 성과','성장의 기회','전략적 우선순위','실행 로드맵','협업 및 자원','측정 기준','다음 단계'][:n]))),'8x5 | 6x6')

# Scope every rule directly to its contract root. No style reaches another element.
for folder,css in CSS.items():
    selectors=', '.join(f'.{r}[data-el="{KIT}-{folder}"]' for r in ROOTS[folder])
    r=f':is({selectors})'
    common=f'''
{r} {{ container-type:size; min-width:0; min-height:0; }}
{r} :is(.name,.fig,.note,.kick) {{ margin:0; }}
{r} .name {{ font-size:var(--type-26); font-weight:var(--name-weight); line-height:var(--name-line); letter-spacing:var(--name-track); }}
{r} .fig {{ font-family:var(--font-display); font-weight:var(--figure-weight); line-height:var(--figure-line); letter-spacing:var(--figure-track); font-variant-numeric:tabular-nums; }}
{r} .fig small {{ font-size:var(--type-22); font-weight:var(--body-weight); color:inherit; margin-left:calc(var(--gap-sm)/3); }}
{r} .note {{ color:var(--ink-2); font-size:var(--type-18); font-weight:var(--body-weight); line-height:var(--body-line); letter-spacing:var(--body-track); }}
{r} .kick {{ color:var(--mute); font-size:var(--type-14); font-weight:var(--label-weight); line-height:var(--label-line); letter-spacing:var(--label-track); }}
'''
    # The generic typography declarations only address contract-defined parts.
    allowed={'card':{'name','fig','note','kick'},'pill':{'name','note'},'callout':set(),'tag':set(),'list':{'name','note'},'quote':{'name','note'},'metric':{'name','fig','note'},'delta':set(),'chart-bar':set(),'chart-line':set(),'chart-donut':{'name','fig'},'gauge':{'name','fig'},'table':set(),'legend':set(),'steps':{'name','note'},'timeline':{'name','note','kick'},'cycle':set(),'hub':{'name','note'},'funnel':{'name','fig'},'pyramid':{'name','note'},'matrix':set(),'venn':{'name'},'hierarchy':set(),'flowchart':set(),'architecture':{'name'},'versus':{'name'},'pricing':{'name','fig'},'person':{'name','note'},'logo-group':set(),'image-frame':set(),'agenda':{'name','note'}}[folder]
    # Remove generated rules for parts that the contract does not define.
    commonlines=common.splitlines()
    common=f'{r} {{ container-type:size; min-width:0; min-height:0; }}\n'
    for part in ['name','fig','note','kick']:
        if part in allowed:
            common += next(line for line in commonlines if f' .{part} {{' in line)+'\n'
    if 'fig' in allowed: common += next(line for line in commonlines if ' .fig small {' in line)+'\n'
    # A reset is legal for each actual part; existing foundation also resets common prose tags.
    if allowed:common+=f'{r} :is('+','.join('.'+p for p in sorted(allowed))+') { margin:0; }\n'
    if folder=='versus': common=common.replace(f'{r} .name',f'{r} > .side > .name')
    write(Path(f'elements/{folder}/element.css'),common+css.replace('@R',r))
    js(Path(f'elements/{folder}/element.json'),dict(schema='rhetis.design-library-element-source/1',contract=CONTRACT[folder],registrations={},tokenDefaults={}))
    write(Path(f'elements/{folder}/description.md'),DESC[folder])
    for name,body in FIX[folder]:write(Path(f'elements/{folder}/fixtures/{name}.html'),body)
assert len(CSS)==31, len(CSS)
print(f'Created {len(CSS)} elements and {sum(len(v) for v in FIX.values())} element fixtures')

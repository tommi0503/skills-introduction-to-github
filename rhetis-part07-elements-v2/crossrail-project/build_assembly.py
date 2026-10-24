from pathlib import Path
import json,re,copy,html,math
from lxml import html as LH
P=Path(__file__).parent;M=json.loads((P/'map.json').read_text()); E=P/'crossrail/elements';new=[]
# Each contents column is its own honest counted list root.
for o in M['instances']:
 if o['id']=='p02-contents':
  for k,x in enumerate([464,806]):
   a=copy.deepcopy(o);a['id']+='-'+str(k+1);a['bbox']=[x,343,290,312];a['fixture']='elements/agenda/fixtures/replica-02'+('' if k==0 else '-2')+'.html';a['sourceMeasurements']=[r for r in o['sourceMeasurements'] if r['bbox'][0]>=x-2 and r['bbox'][0]<x+300];a['use']='base' if k==0 else 'same-as:2';new.append(a)
   labels=['반입 물량','봉인 확인','운송장 대조','수리 창구','야간 배차','선반 배정','예비 부품','출고 예약','차량 회수','창고 정산']
   body=''.join('<div class="entry"><b class="mark">'+f'{k*5+i+1:02}'+'</b><p class="name">'+labels[k*5+i]+'</p></div>' for i in range(5))
   (P/'crossrail'/a['fixture']).write_text('<!-- min:4x5 -->\n<div class="agenda" data-el="crossrail-agenda" style="grid-column:1 / span 12;grid-row:1 / span 6">'+body+'</div>\n')
 else:new.append(o)
M['instances']=new
for o in new:
 for r in o.get('sourceMeasurements',[]):r['owner']=o['id']
(P/'map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
# External source style supplies palette values only. No source geometry is stored here.
(P/'assets/source-palette.css').write_text('''.slide{--page:#ffffff;--ink:#1e385d;--n-1:#f1f2f5;--n-2:#e9eaec;--n-3:#d4d6df;--n-4:#d4d8e2;--n-5:#aeb6c8;--n-6:#969fb7;--n-7:#666b78;--n-8:#555555;--n-9:#1e385d;--a1:#1e385d;--a1-on:#ffffff;--a1-1-soft:#f1f2f5;--a1-2-soft:#e2e6ef;--a1-3-soft:#d4d8e2;--a1-4-soft:#969fb7;--a1-6:#65719a;--a1-7:#1e385d;--a1-8:#65719a;--a2:#65719a;--a2-on:#ffffff;--a2-2-soft:#e4e6ee;--a2-7:#65719a;--a3:#969fb7;--a3-on:#1e385d;--a3-2-soft:#eceef2;--a3-7:#65719a;--a4:#d4d8e2;--a4-on:#1e385d;--a4-2-soft:#f1f2f5;--a4-7:#65719a;--good:#1e385d;--warn:#65719a;--bad:#65719a}\n''')
# Source colors deliberately deepen very light secondary copy while keeping the same palette roles.
# Only contract roots, foundation classes and grid placements appear in the assembly.
A=P/'reassembled';A.mkdir(exist_ok=True)
titles=['입고 현장을 연결하는','차례','정비 거점 소개','접수 창구 현황','정비 운영 원칙','접수 기준 체계','회수 거점 연결','회수 단계별 점검','반입 실적 요약','입고 처리 흐름','창구별 담당 업무','회수 업무 안내','현장 정비 절차','물류 연결 흐름','예비 장비 현황','설비 상세 사양','거점별 정비 판단','정비 역량 점검','배차 전후 비교','창고 운영 지표','정비 결과 요약','반입 건수 흐름','회수 창구 비교','거점별 반입 비율','회수 일정 점검','창구별 배차 일정','주간 회수 예약','거점 확장 이력','거점 배치 분석','방문 정비 예약']
links='<link rel="stylesheet" href="../assets/fonts/fonts.css"><link rel="stylesheet" href="../crossrail/kit/css/tokens.css"><link rel="stylesheet" href="../crossrail/foundation/foundation.css">'+''.join(f'<link rel="stylesheet" href="../crossrail/elements/{d.name}/element.css">' for d in sorted(E.iterdir()))+'<link rel="stylesheet" href="../assets/v2-defaults.css"><link rel="stylesheet" href="../assets/source-palette.css">'
types=json.load(open('/workspace/work/reference/contract/type-steps.json'));defs={}
for f in (P/'crossrail').rglob('*.json'):
 try:defs.update(json.loads(f.read_text()).get('tokenDefaults',{}))
 except:pass
(P/'assets/v2-defaults.css').write_text('.slide{'+''.join(f'--type-{n}:{n}px;' for n in types)+''.join(k+':'+str(v)+';' for k,v in defs.items())+'}\n')
report=[]
for page in range(1,31):
 instances=[o for o in new if o['page']==page and o.get('fixture')];body=[];placements=[]
 if page in [1,25]:
  cover='<section class="slide cover"><div class="page"><div class="lockup '+('at-top-left' if page==1 else 'at-left')+'"><p class="kicker">DEPOT OPERATIONS</p><h1 class="title">'+html.escape(titles[page-1])+'<br><b>반입 점검 보고</b></h1><p class="lead">서원 정비 거점 · 운영지원실</p></div><p class="meta">DEPOT TEAM</p><div class="deco"></div></div></section>';doc=cover
 else:
  leftpanel=page==2
  # Standard page body follows foundation: x95,y263,w1090,h393.
  # Sidebar contents use the same 12x6 grid inside its foundation-reserved right region.
  X,Y,W,H=(95,263,1090,393)
  if leftpanel:X,Y,W,H=462.33,344,722.67,312
  for o in instances:
   f=P/'crossrail'/o['fixture'];node=LH.fromstring(f.read_text());x,y,w,h=o['bbox'];cw=(W+12)/12;rh=(H+12)/6
   col=max(1,min(12,round((x-X)/cw)+1));row=max(1,min(6,round((y-Y)/rh)+1));cols=max(1,min(13-col,round((w+12)/cw)));rows=max(1,min(7-row,round((h+12)/rh)))
   # Field-only data attributes remain intact; page geometry is only integral grid placement.
   st=node.get('style','');extra=';'.join(a for a in st.split(';') if a.strip().startswith('--'));node.set('style',f'grid-column:{col} / span {cols};grid-row:{row} / span {rows}'+(';'+extra if extra else ''))
   body.append(LH.tostring(node,encoding='unicode'));placements.append({'id':o['id'],'sourceBBox':o['bbox'],'grid':[col,row,cols,rows]})
  doc='<section class="slide"><div class="page">'+('<div class="rail on"></div>' if leftpanel else '')+'<header class="head"><p class="kicker">DEPOT OPERATIONS</p><h1 class="title">'+html.escape(titles[page-1])+'</h1><span class="no">'+f'{page:02}'+'</span></header><div class="body">'+''.join(body)+'</div></div></section>'
  if page==30:report.append({'page':30,'limitation':'The reference has a left accent lockup and right contact table. The fresh foundation sidebar keeps one reusable geometry; the exact 552px left field needs a separately contracted split-cover layout.'})
 (A/f'slide_{page:02}.html').write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=1280"><title>Crossrail assembly '+f'{page:02}'+'</title>'+links+'</head><body>'+doc+'<script src="../assets/lucide.min.js"></script><script src="../assets/icons.js"></script></body></html>\n')
 report.append({'page':page,'placements':placements,'gaps':[o['id'] for o in new if o['page']==page and o['use']=='unexpressible']})
(P/'assembly-placement.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
# All newly discovered failures stay visible in the map and gap ledger.
gaps=[o for o in new if o['use']=='unexpressible'];lines=['# Crossrail contract gaps','', 'No missing source feature is imitated by unrelated markup, hidden chart values, source-index selectors or private page geometry.','']
for g in gaps:lines+=['## '+g['id'],f'Source page {g["page"]}, bbox `{g["bbox"]}`. Proposed contract `{g["leaf"]}`.',g['why'],'Required markup: a named part or explicit variant carrying this visual meaning (e.g. `.headline.quiet` for a pale ruled heading strip, `.pie > .seg` for a multipart share chart); the supplied contract cannot encode it.','']
lines+=['## Foundation layout quantization','The 12×6 body grid approximates source coordinates. Source05 has tall independent panels starting beside the page heading; source04/05 have right-hand accent fields, and source30 has a wide left lockup. The supplied normal header plus body and single sidebar base do not express all these independent layout geometries. They remain layout differences, without per-page numeric geometry variables.','']
(P/'GAPS.md').write_text('\n'.join(lines)+'\n')
print('assembly',30,'source fixtures',len(instances),'map',len(new),'gaps',len(gaps))

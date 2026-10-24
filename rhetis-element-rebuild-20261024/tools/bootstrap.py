from pathlib import Path
import json,shutil
ROOT=Path('/workspace/work/rebuild');REF=Path('/workspace/work/reference')
PROFILES={
 'tide-tab':dict(page='#ffffff',ink='#111111',display='Pretendard Variable',weight=900,radius=21,small=16,mx=94,my=74,gap=20,pad=32,line=1.3,track='-0.04em',roles={'청록 강조':'--a1','파랑 강조':'--a2','흰 패널':'--page','연한 페이지 면':'--a1-1-soft','보조문':'--n-7','가느다란 구분선':'--n-3'},accents=['#44cde5','#3858e1','#569dc1','#756fbb']),
 'cutfield':dict(page='#ffffff',ink='#0a3033',display='Pretendard Variable',weight=400,radius=0,small=0,mx=44,my=76,gap=20,pad=28,line=1.45,track='-0.025em',roles={'민트 강조':'--a1','라임 강조':'--a2','진한 청록 면':'--a1-9','본문':'--ink','흰 면':'--page','회색 띠':'--n-3'},accents=['#29caa3','#a9d828','#f0adb3','#638d91']),
 'filament':dict(page='#f5f6e9',ink='#a43527',display='Pretendard Variable',weight=250,radius=12,small=0,mx=64,my=52,gap=20,pad=20,line=1.4,track='-0.045em',roles={'붉은 면':'--a1','붉은 본문':'--a1-8','크림 바탕':'--page','반전 문구':'--a1-on','사진 자리':'--n-2'},accents=['#a43527','#767744','#b58061','#8d675e']),
 'portico':dict(page='#fffcf1',ink='#20201d',display='Montserrat',weight=800,radius=0,small=0,mx=74,my=54,gap=24,pad=24,line=1.45,track='-0.025em',roles={'짙은 남색 면':'--a1','모래색 머리띠':'--a2-2-soft','차분한 금빛':'--a2','가는 칸선':'--n-4','크림 바탕':'--page','기본 글자':'--ink'},accents=['#244859','#938a61','#6d877f','#bb9877']),
 'toggle-grid':dict(page='#f0f0ee',ink='#141414',display='Do Hyeon',weight=400,radius=999,small=0,mx=68,my=60,gap=22,pad=24,line=1.48,track='-0.02em',roles={'검정 띠':'--ink','주황 강조':'--a1','회색 상자':'--n-2','가는 검정선':'--ink','바탕':'--page'},accents=['#ff6d1e','#646d79','#9b795e','#a1a16c']),
 'lamella':dict(page='#efefef',ink='#101010',display='Pretendard Variable',weight=400,radius=32,small=0,mx=49,my=44,gap=20,pad=20,line=1.45,track='-0.025em',roles={'파랑 주 강조':'--a1','라벤더 면':'--a1-3-soft','연보라 면':'--a1-2-soft','보라 보조 시리즈':'--a2','가는 세로선':'--n-5','회색 페이지':'--page'},accents=['#5c6dbe','#6953b9','#7c99b1','#9d7fb3']),
 'rulemark':dict(page='#f6f6f6',ink='#000000',display='Pretendard Variable',weight=750,radius=0,small=0,mx=66,my=50,gap=24,pad=28,line=1.5,track='-0.015em',roles={'검정 면':'--ink','흰 카드':'--page','연회색 상자':'--n-1','중간 회색 막대':'--n-5','가는 선':'--n-4','기본 글자':'--ink'},accents=['#222222','#777777','#555555','#999999'])
}
for name,p in PROFILES.items():
 C=ROOT/name/name;R=ROOT/name/'review';A=R/'assets';(A/'fonts').mkdir(parents=True,exist_ok=True)
 vals={'--page':p['page'],'--ink':p['ink'],'--font-display':repr(p['display']),'--font-body':"'Pretendard Variable'",'--weight-display':str(p['weight']),'--weight-body':'400','--tracking-display':p['track'],'--radius':f"{p['radius']}px",'--radius-sm':f"{p['small']}px",'--stroke':'1px','--text-min':'12px','--margin-x':f"{p['mx']}px",'--margin-y':f"{p['my']}px",'--gap':f"{p['gap']}px",'--gap-sm':'8px','--gap-lg':f"{p['gap']*2}px",'--pad':f"{p['pad']}px",'--furn-edge':f"{p['mx']}px",'--top-h':'52px','--foot-h':'32px','--furn-gap':'24px','--rail-w':'68px','--rail-gap':'24px'}
 for role,weight,line,tracking in [('title',p['weight'],1.12,p['track']),('lead',400,p['line'],p['track']),('figure',700,1.05,'-0.035em'),('name',650,1.3,p['track']),('body',400,p['line'],p['track']),('label',600,1.2,'-0.01em')]:vals.update({f'--{role}-weight':str(weight),f'--{role}-line':str(line),f'--{role}-track':tracking})
 vals['--label-track-latin']='0.05em'
 C.joinpath('kit/css/tokens.css').write_text('.slide {\n'+''.join(f'  {k}: {v};\n' for k,v in vals.items())+'}\n.slide.dark { --page: #182027; --ink: #f6f6f6; }\n')
 C.joinpath('kit/kit.json').write_text(json.dumps({'schema':'rhetis.kit/2','id':name,'label':name,'tokens':'css/tokens.css','description':'description.md','extensions':{f'--{name}-code-font':{'type':'font','default':"'Nanum Gothic Coding'",'label':'Code typeface'}}},ensure_ascii=False,indent=2))
 C.joinpath('kit/description.md').write_text(f"A collection rebuilt from measured, immutable {name} replica instances. Component proportions, edge treatments, text hierarchy and connector construction are recorded in the review map. Colours are supplied exclusively by palette roles; this kit contains no fixed accent colours.\n")
 css='''/* Foundation furniture and a regular 12 by 6 element grid. No element selectors. */
.slide{box-sizing:border-box;position:relative;width:1280px;height:720px;isolation:isolate;background:var(--page);color:var(--ink);font-family:var(--font-body);font-weight:var(--body-weight);font-size:var(--type-18);line-height:var(--body-line);letter-spacing:var(--body-track)}
.slide *,.slide *::before,.slide *::after{box-sizing:border-box}
.slide .page{position:relative;width:100%;height:100%;padding:var(--margin-y) var(--margin-x);display:flex;flex-direction:column;gap:var(--furn-gap)}
.slide .body{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));grid-template-rows:repeat(6,minmax(0,1fr));gap:var(--gap);flex:1;min-width:0;min-height:0;container-type:size}
.slide .body>*{min-width:0;min-height:0}
.slide .group{display:flex;gap:var(--gap);min-width:0;min-height:0}
.slide .group>*{flex:1;min-width:0;min-height:0}
.slide .group.col,.slide .stack{display:flex;flex-direction:column;gap:var(--gap);min-width:0;min-height:0}
.slide .stack>*{flex:1;min-width:0;min-height:0}
.slide .group.two{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}
.slide .group.three{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}
.slide .split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:var(--gap-lg);min-width:0;min-height:0}
.slide .split.wide-left{grid-template-columns:minmax(0,2fr) minmax(0,1fr)}
.slide .head{position:relative;flex:none;color:var(--ink)}
.slide .head.center{text-align:center}
.slide .head .kicker,.slide .lockup .kicker{margin:0 0 var(--gap-sm);font-size:var(--type-14);font-weight:var(--label-weight);letter-spacing:var(--label-track);line-height:var(--label-line)}
.slide .head .title{margin:0;font-family:var(--font-display);font-size:var(--type-48);font-weight:var(--title-weight);line-height:var(--title-line);letter-spacing:var(--title-track)}
.slide .head .lead,.slide .lockup .lead{margin:var(--gap-sm) 0 0;font-size:var(--type-16);font-weight:var(--lead-weight);line-height:var(--lead-line);letter-spacing:var(--lead-track)}
.slide .top,.slide .foot{position:absolute;left:var(--furn-edge);right:var(--furn-edge);display:flex;align-items:center;justify-content:space-between;font-size:var(--type-12);font-weight:var(--label-weight);line-height:var(--label-line);letter-spacing:var(--label-track)}
.slide .top{top:var(--furn-gap);height:var(--top-h)}
.slide .foot{bottom:var(--furn-gap);height:var(--foot-h)}
.slide .rail{position:absolute;top:0;bottom:0;right:0;width:var(--rail-w);border-left:var(--stroke) solid var(--n-4);writing-mode:vertical-rl;padding:var(--furn-gap);font-size:var(--type-12);letter-spacing:var(--label-track)}
.slide .seat{display:grid;place-items:center;min-width:0;min-height:0;background:var(--n-2);color:var(--n-7);font:var(--label-weight) var(--type-18)/var(--label-line) var(--font-body)}
.slide .seat:empty::after{content:attr(data-ph)}
.slide .seat.avatar{aspect-ratio:1;border-radius:50%}
.slide .seat.logo,.slide .seat.portrait{aspect-ratio:1}
.slide .seat.back{position:absolute;inset:0;z-index:-1}
.slide .icon{display:inline-block;flex:none;width:28px;height:28px}
.slide.cover .page{display:block}
.slide .lockup{position:absolute;max-width:85%}
.slide .lockup .title{margin:0;font-family:var(--font-display);font-size:var(--type-96);font-weight:var(--title-weight);line-height:var(--title-line);letter-spacing:var(--title-track)}
.slide .at-center{left:50%;top:50%;transform:translate(-50%,-50%);text-align:center}
.slide .at-left{left:var(--margin-x);top:50%;transform:translateY(-50%)}
.slide .at-top-left{left:var(--margin-x);top:var(--margin-y)}
.slide .at-bottom-left{left:var(--margin-x);bottom:calc(var(--margin-y) + var(--furn-gap))}
.slide .meta{position:absolute;right:var(--margin-x);bottom:var(--margin-y);font-size:var(--type-14);line-height:var(--body-line);letter-spacing:var(--body-track);margin:0}
'''
 C.joinpath('foundation/foundation.css').write_text(css)
 C.joinpath('foundation/foundation.json').write_text(json.dumps({'schema':'rhetis.design-library-foundation-source/1','kit':name,'registrations':{},'tokenDefaults':{}},indent=2))
 C.joinpath('foundation/description.md').write_text('The foundation owns page furniture and an explicit, regular twelve-column, six-row element grid. Element appearance and all member connectors remain exclusively within their respective elements. Unsupported source furniture is recorded in the map instead of reproduced through page-specific selectors.\n')
 C.joinpath('foundation/fixtures/seat.html').write_text('<!-- min: 3x3 -->\n<div class="seat" data-ph="1" style="grid-column:1 / span 12; grid-row:1 / span 6"></div>\n')
 C.joinpath('foundation/fixtures/cover.html').write_text('<section class="slide cover"><div class="page"><div class="lockup at-left"><p class="kicker">기업 운영 전략</p><h1 class="title">성장의 기준</h1><p class="lead">현장에서 검증한 실행 계획을 함께 살펴봅니다.</p></div><p class="meta">분기 경영 브리핑</p></div></section>\n')
 families={'pretendard/PretendardVariable.woff2':('PV.woff2','Pretendard Variable','100 900'),'montserrat/Montserrat.woff2':('Montserrat.woff2','Montserrat','100 900'),'do-hyeon/DoHyeon-Regular.woff2':('DoHyeon.woff2','Do Hyeon','400'),'nanum-gothic-coding/NanumGothicCoding-Regular.woff2':('Mono.woff2','Nanum Gothic Coding','400')}
 fcss=[]
 for rel,(filename,family,weight) in families.items():
  src=REF/'fonts/artifacts'/rel
  if src.exists():shutil.copy(src,A/'fonts'/filename);fcss.append(f"@font-face{{font-family:'{family}';src:url('{filename}');font-weight:{weight};font-style:normal}}")
 (A/'fonts/fonts.css').write_text('\n'.join(fcss))
 # Canonical colours for size sheets; the original source skin remains separate.
 shutil.copy(REF/'contract/palette.json',A/'palette.json')
 (R/'review-notes.md').write_text('# 컬렉션 재제작 검수 기록\n\n기존 replica는 수정하지 않았다. map.json의 수치와 구조에서 요소를 새로 작성한다. 크기별 시트는 README 기준 팔레트로 그리며, replica 조각의 원래 색과 팔레트 색의 차이는 디자인의 고정 색으로 옮기지 않는다. 지원하지 않는 구조는 GAPS.md에만 정리한다.\n')
(ROOT/'profiles.json').write_text(json.dumps(PROFILES,ensure_ascii=False,indent=2));print('fresh kits/foundations/profiles prepared')

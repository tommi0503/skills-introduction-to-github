"""Source-derived commercial comparison leaves. Root-owned; no legacy CSS."""
from pathlib import Path
from html import escape
import json,sys
R=Path('/workspace/work/rebuild');NAMES=list(json.loads((R/'profiles.json').read_text()))
SOURCE={
'tide-tab':('05/06','779×261 floating panels with21px corners and235×52 attached labels;271px rimmed core and light supporting faces'),
'cutfield':('05/10/11','28px lower-right chamfer on268px fields,54px light figures,18px names and16px open paragraphs'),
'filament':('07','178×121 fine-outline services with12px corners,25px/300 upper names and17px/700 lower notes'),
'portico':('08/11','orthogonal sand heading strips over ruled definitions;21px titles,16px notes and1px neutral4 separators'),
'toggle-grid':('06/09/12','40px circular marks,44px capsules,exposed1px ink rules and one accent beside quiet gray fields'),
'lamella':('03/06/13','217×30 leaf caps with opposite upper-right/lower-left corners,19px inset and1px vertical rail'),
'rulemark':('05/13','straight1px black rules,square367×373 evidence fields,40px/750 figures and18px detail')}

def root(n,leaf,cls):return '.'+cls+'[data-el="'+n+'-'+leaf+'"]'
def feature_list(n,items):return '<ul class="list check" data-el="'+n+'-list">'+''.join('<li class="item"><span class="name">'+escape(t)+'</span></li>'for t in items)+'</ul>'
def save(n,leaf,css,contract,fixtures):
 d=R/n/n/'elements'/leaf;pages,design=SOURCE[n]
 (d/'element.css').write_text('/* Absent '+leaf+'; inferred from replica'+pages+': '+design+'.\n   No mapped source instance or previous element stylesheet is reused. */\n'+css+'\n')
 (d/'element.json').write_text(json.dumps({'schema':'rhetis.design-library-element-source/1','contract':contract,'registrations':{},'tokenDefaults':{}},indent=2))
 (d/'description.md').write_text('This contract is absent from the frozen replica. Its material derives from replica'+pages+': '+design+'. Equal members own their layouts; the comparison or pricing enclosure never controls a neighbouring element. Nested feature lists retain their own data-el and stylesheet. Source shapes and type hierarchy remain distinct from the comparison data, which is new Korean business content. Long names, list rows and highlighted members are verified at fixture-specific minima.\n')
 for f,m,html in fixtures:(d/'fixtures'/(f+'.html')).write_text('<!-- min: '+m+' -->\n'+html+'\n')

def material(n,selectors,vs=False):
 p=selectors;v='--'+n+'-commercial-';s=''
 # Every material comes from the named source dimensions, not only a colour change.
 if n=='tide-tab':s+=f'{p}{{border-radius:0 var(--radius) var(--radius) var(--radius);background:var(--n-1);box-shadow:0 calc(var(--gap-sm)*.6) var(--gap-sm) color-mix(in srgb,var(--a2-1-muted) 40%,transparent)}}\n'
 elif n=='cutfield':s+=f'{p}{{--cutfield-commercial-face:var(--n-2);position:relative;isolation:isolate;padding-bottom:calc(var(--pad)*1.6);background:transparent}}{p}::before{{content:"";position:absolute;z-index:-1;inset:0;background:var(--cutfield-commercial-face);clip-path:polygon(0 0,100% 0,100% calc(100% - min(calc(var(--gap)*1.4),10.447761194cqw)),calc(100% - min(calc(var(--gap)*1.4),10.447761194cqw)) 100%,0 100%)}}\n'
 elif n=='filament':s+=f'{p}{{border:var(--stroke) solid var(--a1-8);border-radius:var(--radius);background:var(--page)}}\n'
 elif n=='portico':s+=f'{p}{{border-top:var(--stroke) solid var(--n-4);border-bottom:var(--stroke) solid var(--n-4);background:var(--page)}}\n'
 elif n=='toggle-grid':s+=f'{p}{{border:var(--stroke) solid var(--ink);border-radius:0;background:var(--n-2)}}\n'
 elif n=='lamella':s+=f'{p}{{border-left:var(--stroke) solid var(--n-5);padding-left:calc(var(--pad)*.95);background:transparent}}\n'
 elif n=='rulemark':s+=f'{p}{{border-top:var(--stroke) solid var(--ink);border-bottom:var(--stroke) solid var(--ink);background:var(--n-1)}}\n'
 return s

def pricing(n):
 s=root(n,'pricing','plans');p=root(n,'pricing','plan');sel=f':is({p},{s}>.plan)'; cap={'tide-tab':52,'cutfield':56,'filament':48,'portico':48,'toggle-grid':64,'lamella':32,'rulemark':40}[n];namecap={'filament':24,'lamella':20,'rulemark':20,'portico':24}.get(n,30)
 css=f'''{s}{{--{n}-pricing-count:1;container-type:size;display:flex;flex-wrap:wrap;align-items:stretch;align-content:stretch;gap:var(--gap);width:100%;height:100%;min-width:0;min-height:0;padding:var(--gap-sm)}}
{sel}{{container-type:size;position:relative;isolation:isolate;display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:auto auto minmax(0,1fr);align-content:start;row-gap:var(--gap-sm);width:100%;height:100%;min-width:0;min-height:0;padding:var(--pad);color:var(--ink);font-family:var(--font-body)}}
{s}>.plan{{flex:1 1 calc((100% - (var(--{n}-pricing-count) - 1)*var(--gap))/var(--{n}-pricing-count));width:auto;height:auto}}
{sel}>.name{{margin:0;min-width:0;font-size:clamp(var(--type-16),8cqw,var(--type-{namecap}));font-weight:var(--name-weight);line-height:var(--name-line);letter-spacing:var(--name-track);word-break:keep-all;overflow-wrap:anywhere;text-wrap:balance}}
{sel}>.price{{display:flex;align-items:baseline;flex-wrap:wrap;column-gap:var(--gap-sm);margin:0;min-width:0}}
{sel}>.price>.fig{{min-width:0;font-size:clamp(var(--type-24),18cqw,var(--type-{cap}));font-weight:var(--figure-weight);line-height:var(--figure-line);letter-spacing:var(--figure-track);white-space:nowrap}}
{sel}>.price>small{{font-size:var(--type-12);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track)}}
{sel}>.list{{margin:0;min-height:0;min-width:0;width:100%;height:100%}}
{sel}>.tag{{position:absolute;right:var(--gap-sm);top:var(--gap-sm);display:grid;place-items:center;height:var(--type-24);white-space:nowrap;width:calc(var(--type-12)*6.5);max-width:calc(100% - var(--gap-sm)*2)}}
{p}:has(>.tag),{s}:has(>.plan>.tag)>.plan{{padding-top:calc(var(--pad) + var(--type-24))}}
'''
 if n in ['cutfield','toggle-grid','rulemark']:
  css+=f'@container(min-height:400px){{{sel}>.list{{height:min(100%,55cqh);align-self:center}}}}\n'
 for count in range(2,9):css+=f'{s}:has(>.plan:nth-child({count}):last-child){{--{n}-pricing-count:{count}}}\n'
 css+=material(n,s+'>.plan' if n=='tide-tab' else sel)
 if n in ['portico','lamella']:
  rad='0'if n=='portico'else'0 var(--radius) 0 var(--radius)'
  css+=f'{sel}>.name{{background:var(--n-3);color:var(--ink);padding:var(--gap-sm);border-radius:{rad}}}\n'
 css+=f'{sel}.on{{background:'+('transparent;--cutfield-commercial-face:var(--a1)'if n=='cutfield'else'var(--a1)')+';color:var(--a1-on);border-color:var(--a1)}\n'
 if n=='lamella':css+=f'{sel}.on{{background:var(--a1-1-soft);color:var(--ink)}}{sel}.on>.name{{background:var(--a1);color:var(--a1-on)}}\n'
 if n=='tide-tab':css+=f'{sel}>.name{{width:max-content;max-width:100%;background:var(--a1-2-soft);padding:var(--gap-sm) var(--gap);border-radius:var(--radius-sm)}}{sel}.on{{background:transparent;color:var(--ink)}}{s}>.plan.on{{background:var(--n-1)}}{sel}.on>.name{{background:var(--a1);color:var(--a1-on)}}\n'
 if n=='tide-tab':css+=f'{p},{p}.on{{background:transparent;box-shadow:none}}{p}::before{{content:"";position:absolute;z-index:-1;inset:var(--gap-sm) var(--gap-sm) calc(var(--gap-sm)*2);border-radius:0 var(--radius) var(--radius) var(--radius);background:var(--n-1);box-shadow:0 calc(var(--gap-sm)*.6) var(--gap-sm) color-mix(in srgb,var(--a2-1-muted) 40%,transparent)}}\n'
 if n=='rulemark':css+=f'{sel}.on{{background:var(--ink);color:var(--page);border-color:var(--ink)}}\n'
 css+=f'@container(max-width:480px){{{s}>.plan{{flex-basis:100%}}}}\n@container(max-height:250px){{{sel}{{padding:var(--gap-sm)}}{sel}>.name{{font-size:var(--type-16)}}{sel}>.price>.fig{{font-size:var(--type-24)}}}}\n'
 def plan(title,amount,features,on=False,tag=None,standalone=False):
  h='<article class="plan'+(' on'if on else'')+'"'+(' data-el="'+n+'-pricing" style="grid-column:1 / span 12; grid-row:1 / span 6"'if standalone else'')+'><h3 class="name">'+escape(title)+'</h3><div class="price"><b class="fig">'+amount+'</b><small>만원 / 월</small></div>'+feature_list(n,features)
  if tag:h+='<span class="tag" data-el="'+n+'-tag">'+tag+'</span>'
  return h+'</article>'
 def plans(items):return '<div class="plans" data-el="'+n+'-pricing" style="grid-column:1 / span 12; grid-row:1 / span 6">'+''.join(items)+'</div>'
 fs=[('plan-single','2x3',plan('현장 지원형','19',['자료 보관','월간 점검','담당자 상담'],standalone=True)),('plans-two','6x3 | 3x6',plans([plan('기본 운영','29',['정기 보고','예약 관리','문서 공유']),plan('협업 확장','59',['팀별 권한','공동 편집','현황 알림'],True,'권장 구성')])),('plans-three-long','6x4',plans([plan('소규모 사업장 시작형','39',['현장 자료 수집','담당자별 업무 배정','분기 운영 현황 정리']),plan('여러 지점 공동 운영형','79',['부서 간 문서 검토','예약 요청 통합 관리','고객 문의 우선 처리'],True),plan('전사 확장 및 연계형','129',['외부 시스템 자료 연계','본사와 현장 공동 점검','관리자별 접근 범위 설정'])]))]
 save(n,'pricing',css,'pricing.plans@1',fs)

def versus(n):
 s=root(n,'versus','versus');p=s+'>.side'
 css=f'''{s}{{container-type:size;position:relative;display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:stretch;gap:var(--gap-sm);width:100%;height:100%;min-width:0;min-height:0;padding:var(--gap-sm)}}
{p}{{container-type:size;display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:auto minmax(0,1fr);gap:var(--gap-sm);min-width:0;min-height:0;padding:var(--pad);color:var(--ink);font-family:var(--font-body)}}
{p}>.name{{margin:0;min-width:0;font-size:clamp(var(--type-16),9cqw,var(--type-30));font-weight:var(--name-weight);line-height:var(--name-line);letter-spacing:var(--name-track);word-break:keep-all;overflow-wrap:anywhere;text-wrap:balance}}
{p}>.list{{min-width:0;min-height:0;width:100%;height:100%;margin:0}}
{s}>.vs{{align-self:center;display:grid;place-items:center;width:var(--type-48);aspect-ratio:1;margin:0;color:var(--ink);font-family:var(--font-display);font-size:var(--type-20);font-weight:var(--figure-weight);line-height:var(--figure-line);letter-spacing:var(--label-track)}}
'''
 if n in ['cutfield','toggle-grid','rulemark']:
  css+=f'@container(min-height:400px){{{p}>.list{{height:min(100%,55cqh);align-self:center}}}}\n'
 css+=material(n,p,True)
 if n=='tide-tab':css+=f'{s}>.vs{{border:calc(var(--stroke)*2) solid var(--a1);border-radius:50%;background:var(--n-1)}}\n'
 elif n=='cutfield':css+=f'{s}>.vs{{clip-path:polygon(0 0,100% 0,100% 75%,75% 100%,0 100%);background:var(--a1-2-soft);color:var(--a1-9)}}\n'
 elif n=='filament':css+=f'{s}>.vs{{color:var(--a1-8);font-weight:var(--name-weight);border-top:var(--stroke) solid currentColor;border-bottom:var(--stroke) solid currentColor}}\n'
 elif n=='portico':css+=f'{p}>.name{{padding-bottom:var(--gap-sm);border-bottom:var(--stroke) solid var(--n-4)}}{s}>.vs{{background:var(--n-3)}}\n'
 elif n=='toggle-grid':css+=f'{s}>.vs{{border-radius:999px;background:var(--ink);color:var(--page);font-family:var(--font-body)}}\n'
 elif n=='lamella':css+=f'{p}>.name{{padding:var(--gap-sm);background:var(--a1-2-soft);border-radius:0 var(--radius) 0 var(--radius)}}{s}>.vs{{background:var(--a1-2-soft);border-radius:0 var(--radius-sm) 0 var(--radius-sm);font-family:var(--font-body)}}\n'
 elif n=='rulemark':css+=f'{s}>.vs{{border:calc(var(--stroke)*2) solid var(--ink);border-radius:50%;background:var(--page)}}\n'
 css+=f'{p}.on{{background:'+('transparent;--cutfield-commercial-face:var(--a1)'if n=='cutfield'else'var(--a1)')+';color:var(--a1-on);border-color:var(--a1)}\n'
 if n=='lamella':css+=f'{p}.on{{background:var(--a1-1-soft);color:var(--ink)}}{p}.on>.name{{background:var(--a1);color:var(--a1-on)}}\n'
 if n=='tide-tab':css+=f'{p}>.name{{width:max-content;max-width:100%;padding:var(--gap-sm);background:var(--a1-2-soft);border-radius:var(--radius-sm)}}{p}.on{{background:var(--n-1);color:var(--ink)}}{p}.on>.name{{background:var(--a1);color:var(--a1-on)}}\n'
 if n=='rulemark':css+=f'{p}.on{{background:var(--ink);color:var(--page);border-color:var(--ink)}}\n'
 css+=f'@container(max-width:480px){{{s}>.side{{padding:var(--gap-sm)}}{s}>.vs{{width:var(--type-24);font-size:var(--type-12)}}}}\n'
 def pair(names,items):return '<div class="versus" data-el="'+n+'-versus" style="grid-column:1 / span 12; grid-row:1 / span 6"><section class="side"><h3 class="name">'+names[0]+'</h3>'+feature_list(n,items[0])+'</section><b class="vs">VS</b><section class="side on"><h3 class="name">'+names[1]+'</h3>'+feature_list(n,items[1])+'</section></div>'
 fs=[('pair-three','4x3',pair(['개별 접수','통합 접수'],[['담당자 확인','자료 재입력','회신 대기'],['공동 현황판','자료 자동 연계','처리 내역 공유']])),('pair-four-long','4x3',pair(['지점별로 나뉜 수기 관리','본사와 현장이 연결된 공동 관리'],[['문의 내용을 담당자가 따로 기록','변경 사항을 문서로 다시 전달','월말에 실적 자료를 취합','문제 원인을 부서별로 확인'],['같은 화면에서 접수 상태를 확인','승인된 내용을 관계자에게 알림','운영 지표를 주 단위로 점검','점검 결과와 후속 조치를 함께 기록']]))]
 save(n,'versus',css,'versus.pair@1',fs)

if __name__=='__main__':
 for n in sys.argv[1:]or NAMES:pricing(n);versus(n)

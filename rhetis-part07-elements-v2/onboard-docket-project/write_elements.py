"""Fresh element sources, measured from replica units. Run one named leaf at a time."""
from pathlib import Path
import json,sys,re,html
P=Path(__file__).resolve().parent;K=P/'onboard-docket';kid=K.name;REF=Path('/workspace/work/reference')
contracts=json.loads((P/'contract-folders.json').read_text());ids={v:k for k,v in contracts.items()}
def write(leaf,root,css,description,fixtures):
 f=K/'elements'/leaf;f.mkdir(parents=True,exist_ok=True)
 (f/'element.json').write_text(json.dumps({'schema':'rhetis.design-library-element-source/1','contract':ids[leaf],'registrations':{},'tokenDefaults':{}},indent=2))
 (f/'element.css').write_text(css.replace('ROOT',f'.{root}[data-el="{kid}-{leaf}"]'))
 (f/'description.md').write_text(description+'\n');fd=f/'fixtures';fd.mkdir(exist_ok=True)
 for name,minimum,markup in fixtures:
  markup=markup.replace('DATA',f'data-el="{kid}-{leaf}" style="grid-column:1 / span 12;grid-row:1 / span 6"')
  def merge_styles(m):
   tag=m.group(0);styles=re.findall(r' style="([^"]*)"',tag)
   return re.sub(r' style="[^"]*"','',tag)[:-1]+' style="'+';'.join(styles)+'">' if len(styles)>1 else tag
  markup=re.sub(r'<[^>]+>',merge_styles,markup)
  (fd/(name+'.html')).write_text(f'<!-- min: {minimum} -->\n'+markup+'\n')

def steps(col=False,n=4,long=False):
 labels=['검토 범위 확정','현장 의견 수집','실행 항목 승인','후속 성과 확인','운영 위험 분석','품질 지표 공유']
 notes=['지난 분기 접수된 장애 사례를 유형별로 분류하고 담당 부서의 개선 의견을 취합합니다.','현장 인터뷰에서 확인한 불편을 우선순위로 묶어 이번 배포 범위에 반영합니다.','예산 검토와 담당자 합의를 거쳐 승인된 항목부터 순차적으로 운영에 적용합니다.','배포 후 수집한 지표와 상담 이력을 대조해 다음 분기 보완 과제를 선정합니다.']
 items=[]
 for i in range(n):
  mark=('검토 '+str(i+1)) if col else '<span class="icon" data-icon="'+['handshake','lightbulb','chart-column','rocket','shield','check'][i%6]+'"></span>'
  note=notes[i%4] if col else ['접수 채널별 장애를 나누고<br>반복 문의의 원인을 확인해<br>우선 개선할 항목을 정한 뒤<br>담당 조직과 범위를 맞춥니다.','현장 상담의 이력을 살피고<br>검토할 요청을 함께 묶어<br>이번 분기의 승인 조건을<br>운영 책임자와 협의합니다.','이관 근거와 예산을 대조해<br>승인된 항목부터 적용한 뒤<br>예외 요청의 처리 사유를<br>담당 조직에 공유합니다.','운영 지표와 조치 결과를<br>접수 기록과 다시 대조해<br>후속 점검의 담당자를 정하고<br>다음 배포의 범위를 정합니다.'][i%4]
  items.append(f'<div class="step"><div class="mark">{mark}</div><p class="name">{labels[i%6]+(" 및 승인 책임자 지정" if long and i==1 else "")}</p><p class="note">{note}</p></div>')
 return '<div class="steps'+(' col' if col else '')+'" DATA>'+''.join(items)+'</div>'

CSS_STEPS='''/* Replica15:196px circular fields,70px line icons,16×50px arrows and centred copy.
Replica10:122px descending rows with234px mark blocks and20×10px notches. */
ROOT{container-type:size;container-name:od-steps;position:relative;display:grid;grid-template-columns:repeat(60,minmax(0,1fr));grid-auto-rows:minmax(0,1fr);column-gap:0;row-gap:var(--gap-sm);padding:0;min-width:0;min-height:0;color:var(--ink);--od-count:4}
ROOT:has(>.step:nth-child(3):last-child){--od-count:3}ROOT:has(>.step:nth-child(5):last-child){--od-count:5}ROOT:has(>.step:nth-child(6):last-child){--od-count:6}ROOT:has(>.step:nth-child(2):last-child){--od-count:2}
ROOT>.step{position:relative;display:flex;align-items:center;flex-direction:column;grid-column:span calc(60 / var(--od-count));padding-inline:calc(var(--gap-sm)/2);min-width:0;min-height:0;text-align:center}
ROOT>.step>.mark{flex:none;inline-size:min(100%,53.735cqh,196px);aspect-ratio:1;border-radius:50%;background:var(--a1-1-soft);color:var(--a1);display:flex;align-items:center;justify-content:center}
ROOT>.step>.mark>.icon{width:36%;height:41%;display:inline-flex}
ROOT>.step>.mark>.icon>svg{width:100%;height:100%}
ROOT>.step>.name{margin:min(var(--gap-sm),3.8356cqh) 0 0;font-size:clamp(var(--type-16),min(1.913cqw,5.754cqh),var(--type-22));line-height:var(--body-line);font-weight:var(--name-weight);letter-spacing:var(--name-track);max-width:100%;overflow-wrap:anywhere}
ROOT>.step>.note{margin:min(calc(var(--gap-sm)*.8857),3.397cqh) 0 0;font-size:clamp(var(--type-12),min(1.548cqw,4.658cqh),var(--type-18));font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);color:var(--n-7);overflow-wrap:anywhere;max-width:100%}
ROOT>.step:not(:last-child)::after{content:"";position:absolute;right:0;top:calc(min(53.735cqh,196px)/2 - min(13.7cqh,50px)/2);width:min(1.5cqw,16px);height:min(13.7cqh,50px);background:var(--a1-2-soft);clip-path:polygon(0 0,100% 50%,0 100%)}
ROOT.col{grid-template-columns:1fr;grid-template-rows:repeat(var(--od-count),minmax(0,1fr));gap:calc(var(--gap)*1.15);padding:0;inline-size:min(100%,1043px);justify-self:center}
ROOT.col>.step{display:grid;grid-template-columns:22.5% minmax(0,1fr);grid-template-rows:minmax(0,1fr) minmax(0,1.7fr);column-gap:var(--pad);grid-column:1;padding:0;background:var(--n-1);text-align:left}
ROOT.col>.step>.mark{grid-column:1;grid-row:1 / 3;width:100%;height:100%;aspect-ratio:auto;border-radius:0;background:var(--a1);color:var(--a1-on);font-size:clamp(var(--type-14),calc(2.5886cqw),var(--type-28));font-weight:var(--onboard-docket-value-weight);line-height:var(--figure-line)}
ROOT.col>.step:nth-child(2)>.mark{background:var(--a2-7);color:var(--page)}ROOT.col>.step:nth-child(3)>.mark{background:var(--n-9);color:var(--page)}
ROOT.col>.step>.name{grid-column:2;grid-row:1;align-self:end;margin:0;padding-right:var(--pad);font-size:clamp(var(--type-14),calc(1.8217cqw),var(--type-20));font-weight:var(--onboard-docket-emphasis-weight)}
ROOT.col>.step>.note{font-size:clamp(var(--type-12),calc(1.534cqw),var(--type-18));line-height:var(--onboard-docket-steps-note-line);grid-column:2;grid-row:2;align-self:start;margin:calc(var(--gap-sm)/3) 0 0;padding-right:var(--pad)}
ROOT.col>.step:not(:last-child)::after{left:calc(11.25% - min(1.8cqw,20px)/2);right:auto;top:100%;width:min(1.8cqw,20px);height:min(2.4cqh,10px);background:var(--a1);clip-path:polygon(0 0,100% 0,50% 100%)}
ROOT.col>.step:nth-child(2)::after{background:var(--a2-7)}
ROOT:has(>.step:nth-child(5):last-child):not(.col)>.step>.name,ROOT:has(>.step:nth-child(6):last-child):not(.col)>.step>.name{font-size:var(--type-16);min-block-size:calc(var(--type-16)*var(--body-line)*2)}ROOT:has(>.step:nth-child(5):last-child):not(.col)>.step>.note,ROOT:has(>.step:nth-child(6):last-child):not(.col)>.step>.note{font-size:var(--type-14);line-height:var(--onboard-docket-statement-line)}
@container od-steps (max-width:900px){ROOT:has(>.step:nth-child(5):last-child):not(.col)>.step>.note,ROOT:has(>.step:nth-child(6):last-child):not(.col)>.step>.note{display:none}}
@container od-steps (max-height:280px){ROOT>.step>.mark{width:min(100%,38cqh,130px)}ROOT>.step>.name{margin-top:calc(var(--gap-sm)/2);font-size:var(--type-16)}ROOT>.step>.note{font-size:var(--type-12);line-height:var(--label-line);margin-top:calc(var(--gap-sm)/3)}ROOT>.step:not(:last-child)::after{top:calc(min(38cqh,130px)/2 - min(10cqh,30px)/2);height:min(10cqh,30px)}ROOT.col>.step{grid-template-rows:1fr}ROOT.col>.step>.mark{width:100%;grid-row:1}ROOT.col>.step>.name{grid-row:1;align-self:center;margin:0}ROOT.col>.step>.note{display:none}ROOT.col>.step:not(:last-child)::after{top:100%;height:8px}}
@container od-steps (max-width:560px){ROOT:not(.col)>.step{grid-column:span 60;flex-direction:row;justify-content:flex-start;gap:var(--gap-sm)}ROOT:has(>.step:nth-child(5):last-child)>.step,ROOT:has(>.step:nth-child(6):last-child)>.step{--od-rows:3}ROOT>.step>.mark{width:min(20cqh,calc((100cqh - (var(--od-count) - 1)*var(--gap-sm)) / var(--od-count)),64px)}ROOT>.step>.name{font-size:var(--type-14);line-height:var(--label-line);margin:0}ROOT>.step>.note{display:none}ROOT:not(.col)>.step:not(:last-child)::after{left:calc(min(20cqh,(100cqh - (var(--od-count) - 1)*var(--gap-sm)) / var(--od-count),64px)/2 + 3px);right:auto;top:100%;width:8px;height:12px;clip-path:polygon(0 0,100% 0,50% 100%)}ROOT.col>.step{column-gap:var(--gap-sm)}ROOT.col>.step>.mark{width:100%;font-size:var(--type-14)}ROOT.col>.step>.name{font-size:var(--type-14);padding-right:calc(var(--pad)/2)}}
'''

if __name__=='__main__':
 leaf=sys.argv[1]
 if leaf=='steps':
  write('steps','steps',CSS_STEPS,'Four pale circular illustration fields connect with slim triangular arrows. Names and supporting copy sit beneath each field. The downward col variant uses solid rectangular mark blocks with a narrow notch connecting each complete row.',[('replica-15','6x3',steps()),('replica-10','6x3',steps(True,3)),('sequence-six-long','6x6',steps(False,6,True))])
  f=K/'elements/steps/element.json';j=json.loads(f.read_text());j['tokenDefaults']['--onboard-docket-steps-note-line']='1.8';f.write_text(json.dumps(j,indent=2))
 else:raise SystemExit('not yet authored: '+leaf)

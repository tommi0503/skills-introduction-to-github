from pathlib import Path
import re,json
P=Path(__file__).parent;C=P/'meridian-deck'
for f in [P/'replica/slide_13.html',P/'reassembled/slide_13.html',C/'foundation/fixtures/source-composition-13.html']:
 s=f.read_text();s=s.replace('목표 달성을 위한 구체적 전략적 방향','목표 달성을 위한 두번째 전략적 방향',1);pos=s.rfind('참여형 캠페인 운영');s=s[:pos]+s[pos:].replace('참여형 캠페인 운영','브랜드 협업형 콘텐츠 패키지 개발',1).replace('목표 달성을 위한 구체적 전략적 방향','목표 달성을 위한 세번째 전략적 방향',1);f.write_text(s)
def app(n,t):
 f=C/'elements'/n/'element.css';f.write_text(f.read_text()+'\n/* Final direct source comparison. */\n'+t+'\n')
c='[data-el="meridian-deck-card"]';s='.slide.src '+c
app('card',s+'.card.line:has(.kick) .name{border-bottom:0}'+s+'.card.quiet:not(.tone-2):has(.kick):not(:has(.note:not(:empty))):not(:has(.mark))::after{content:"";position:absolute;left:calc(100% - 1px);top:50%;width:46px;height:2px;background:var(--n-7);clip-path:none;translate:0;transform:none}'+s+'.card.quiet:not(.tone-2):has(.kick):not(:has(.note:not(:empty))):not(:has(.mark))::before{content:"";position:absolute;left:calc(100% + 36px);top:calc(50% - 3px);width:8px;height:8px;background:none;border:0;border-top:2px solid var(--n-7);border-right:2px solid var(--n-7);border-radius:0;rotate:45deg;translate:0;transform:none}'+s+'.card.on.tone-1:not(:has(.mark,.fig,.kick))::after{clip-path:path("M0 0L8 4L0 8L0 6L5 4L0 2Z M0 195L8 199L0 203L0 201L5 199L0 197Z")}')
a='.slide.src .split.wide-left>.group>[data-el="meridian-deck-chart-area"]'
css=a+' .pt{box-shadow:none}'+a+' .pt>b{position:relative}'+a+' .pt>b::after{content:"";position:absolute;left:calc(50% - 3px);top:calc(150% - 3px);width:6px;height:6px;background:var(--a1);border-radius:50%}'
for n in range(2,13):css+=a+f' .pt:nth-child({n} of .pt)::before'+'{left:calc(anchor(--meridian-area-'+str(n-1)+' center) - .5px);right:calc(anchor(--meridian-area-'+str(n)+' center) - .5px)}'
app('chart-area',css)
f=C/'elements/hub/element.json';j=json.loads(f.read_text());j['tokenDefaults']['--meridian-deck-photo-ink']='var(--ink)';f.write_text(json.dumps(j,ensure_ascii=False,indent=2))
h='[data-el="meridian-deck-hub"]:has(>.core>.seat.avatar):has(>.spoke:nth-child(4 of .spoke):last-child)'
app('hub',h+'>.core>.name,'+h+'>.core>.note{color:var(--meridian-deck-photo-ink)}')
f=P/'assets/source-palette.css';f.write_text(f.read_text()+'\n.slide.src{--meridian-deck-photo-ink:var(--page)}\n')
# Current standalone source runtime supplies element defaults; preserve that runtime without touching root tooling.
f=P/'assets/source-defaults.css';f.write_text(f.read_text()+'\n.slide{--meridian-deck-photo-ink:var(--ink)}\n')
print('Source text, open connectors, round points and photo text role restored')

from pathlib import Path
p=Path(__file__).parent/'build_collection.py';s=p.read_text();mark='# Emit CSS with roots specific'
x='''# Final responsive repairs from minimum-slot audits.
foundation=foundation.replace('.slide .stack>*{min-height:0}', '.slide .stack>*{min-height:0;flex:1 1 0}.slide .stack>.seat{flex:none;width:var(--type-80);height:var(--type-80);align-self:center}')
write(Path('foundation/foundation.css'),foundation)
S['chart-donut']+='@.donuts{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,var(--type-128)),1fr));gap:var(--gap-sm)}@.donut{padding:var(--gap-sm)}@.donut::before{width:min(68cqw,68cqh);top:40%}@.donut::after,@.donuts>.donut::after{width:min(60cqw,60cqh);top:40%}@.donut>.fig{position:absolute;left:50%;top:40%;translate:-50% -50%;max-width:none;white-space:nowrap}@.donut>.name{position:absolute;top:calc(40% + min(30cqw,30cqh) + var(--gap-sm)/2);left:0;right:0;max-width:none;width:100%;padding:0 var(--gap-sm)}@.donuts>.donut>.fig{font-size:var(--type-24)}@.donuts>.donut>.fig small{font-size:var(--type-14)}@.donuts>.donut>.name{font-size:var(--type-14)}'
S['hub']+='@{overflow:clip}@>.spoke::before{content:none}@::before{content:"";position:absolute;left:16%;right:16%;top:16%;bottom:16%;border:var(--stroke) solid var(--a1-2-soft);z-index:-1;clip-path:polygon(0 0,50% 48%,100% 0,52% 50%,100% 100%,50% 52%,0 100%,48% 50%)}'
S['list']+='@container (max-height:500px){@>.item{padding-bottom:calc(var(--gap-sm)/2)}@>.item>.name{font-size:var(--type-20)}@>.item>.note{font-size:var(--type-16)}}'
S['logo-group']+='@:has(>.seat:nth-child(6)){grid-template-rows:repeat(2,minmax(0,1fr))}@>.seat.logo{height:100%;width:auto;max-width:100%;justify-self:center}'
S['person']+='@.person>.seat{width:auto;height:min(32cqh,32cqw);max-height:none;flex:none}@.person>.list{width:100%;flex:none}@.person .list .name{font-size:var(--type-18)}@.person .list .note{font-size:var(--type-14)}'
S['tag']+='@{container-type:normal;min-width:max-content;height:auto;white-space:nowrap}'
S['venn']+='@:has(>.set:nth-child(3))>.set{width:min(35cqw,55cqh)}@:has(>.set:nth-child(3))>.set:nth-child(3){width:min(35cqw,55cqh);top:35%}'
\n'''
p.write_text(s.replace(mark,x+mark))
# Use source-deck filled headers on normal content cards, with the compact horizontal source row for short stacks.
p=Path(__file__).parent/'build_reassembled.py';s=p.read_text();s=s.replace("variant='line'","variant=''")
# Give the step cards their source staircase by legal element placement on 12x6 grid.
start=s.index("P[17]=")
end=s.index("P[18]=",start)
s=s[:start]+'''P[17]=(head('05. 추진 계획','차년도는 콘텐츠 소비 중심 성장 구조 강화 및','커뮤니티 활성화 기 확대에 주력'),''.join(pos(card(n,'<br>'.join(ls),variant='quiet'),i*3+1,4-i,3,i+2) for i,(n,ls) in enumerate(plan))+pos(el('legend','legend','<span class="key tone-1">상반기</span><span class="key tone-2">하반기</span>'),1,6,12,1))
'''+s[end:]
# Source markup stays contract compliant; lightweight icon hydration supplies Lucide-like SVGs for the standalone review.
s=s.replace("print('reassembled',len(P))",'''from build_replica import icon
mapping={'clapperboard':'video','handshake':'bag','user':'user','user-round-check':'user','shopping-bag':'bag','chart-no-axes-combined':'chart','presentation':'chart'}
icons={name:icon(value).replace('<svg ','<svg width="100%" height="100%" ') for name,value in mapping.items()}
runtime='<script>const icons='+json.dumps(icons)+';document.querySelectorAll("[data-icon]").forEach(e=>{e.innerHTML=icons[e.dataset.icon]||""});</script>'
for f in O.glob('*.html'):f.write_text(f.read_text().replace('</body>',runtime+'</body>'))
print('reassembled',len(P))''')
p.write_text(s)

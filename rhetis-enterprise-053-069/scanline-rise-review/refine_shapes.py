from pathlib import Path
p=Path(__file__).parent/'build_collection.py';s=p.read_text();mark='# Emit CSS with roots specific'
x='''# Source-deck panel grammar, circular geometry and code-face refinements.
S['card']+='@.card:not(.line):not(.quiet):not(.on):not(:has(.fig))::before{height:52%;background:var(--a1)}@.card:not(.line):not(.quiet):not(.on):not(:has(.fig))>.parts{height:100%;display:grid;grid-template-rows:minmax(0,1fr) auto minmax(0,1fr);gap:var(--gap-sm)}@.card:not(.line):not(.quiet):not(.on):not(:has(.fig)) .mark{grid-row:1;align-self:end;justify-self:center;background:var(--page);color:var(--a1-7)}@.card:not(.line):not(.quiet):not(.on):not(:has(.fig)) .name{grid-row:2;text-align:center;color:var(--a1-on)}@.card:not(.line):not(.quiet):not(.on):not(:has(.fig)) .note{grid-row:3;align-self:start;padding-top:var(--gap-sm)}@.card:not(.line):not(.quiet):not(.on):not(:has(.fig)) .kick{grid-row:1;align-self:start;color:var(--a1-on)}'
S['cycle']+='@::before{width:min(68cqw,68cqh);height:auto;aspect-ratio:1}@>.core{width:min(28cqw,28cqh);height:auto;aspect-ratio:1}@>.node{width:min(24cqw,24cqh);height:auto;aspect-ratio:1;left:calc(50% + cos(var(--scanline-rise-angle))*min(34cqw,34cqh));top:calc(50% + sin(var(--scanline-rise-angle))*min(34cqw,34cqh))}'
S['hub']+='@>.core{width:min(24cqw,28cqh);height:auto;aspect-ratio:1;align-self:center;justify-self:center}'
S['chart-donut']+='@.donut::before{inset:auto;left:50%;top:50%;translate:-50% -50%;width:min(84cqw,84cqh);height:auto;aspect-ratio:1}@.donut::after,@.donuts>.donut::after{width:min(70cqw,70cqh)}@.donut>.fig{max-width:60%;font-size:var(--type-52)}@.donut>.name{max-width:48%}@.donuts>.donut>.fig{font-size:var(--type-32)}@.donuts>.donut>.name{font-size:var(--type-16)}'
S['concentric']+='@>.ring{width:min(90cqw,90cqh);height:auto;aspect-ratio:1;bottom:5%;top:auto}@>.ring:nth-child(2){width:min(64cqw,64cqh);height:auto;top:auto}@>.ring:nth-child(3){width:min(38cqw,38cqh);height:auto;top:auto}@>.ring:nth-child(4){width:min(20cqw,20cqh);height:auto;top:auto}'
S['code']=S['code'].replace('font-family:var(--font-body)','font-family:var(--scanline-rise-code-font)')
k=json.loads((C/'kit/kit.json').read_text());k['extensions']['--scanline-rise-code-font']='font';write(Path('kit/kit.json'),js(k))
tokens['--scanline-rise-code-font']="'Nanum Gothic Coding'"
write(Path('kit/css/tokens.css'),'.slide{'+''.join(f'{k}:{v};' for k,v in tokens.items())+'}\\n.slide.dark{--page:#101820;--ink:#f5f8fc;}')
\n'''
p.write_text(s.replace(mark,x+mark))

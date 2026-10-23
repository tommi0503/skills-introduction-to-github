from pathlib import Path
import re,json,html
p=Path(__file__).parent;c=p/'crossrail'
f=c/'kit/css/tokens.css';f.write_text(f.read_text()+"\n.slide{--crossrail-font-label:'Pretendard Variable';--crossrail-title-stack-line:1.25}\n")
f=c/'kit/kit.json';d=json.loads(f.read_text());d['extensions'].update({'--crossrail-font-label':'font','--crossrail-title-stack-line':'number'});f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
f=c/'foundation/foundation.css';f.write_text(f.read_text()+'''\n.slide:not(.cover) .kicker{font-family:var(--crossrail-font-label);letter-spacing:0;padding-left:1px}.slide:not(.cover) .no{font-family:var(--crossrail-font-label);font-size:var(--type-18);letter-spacing:0;right:calc(var(--gap-sm)*-1)}.slide:not(.cover):has(.head>.title>br) .head>.title{margin-top:-1px;line-height:var(--crossrail-title-stack-line)}.slide:not(.cover):has(.head>.title>br) .page::after{content:"";position:absolute;left:calc(var(--margin-x)*-1);right:calc(var(--margin-x)*-1);bottom:0;border-top:1px solid var(--n-3)}\n''')
f=c/'elements/chart-donut/element.css';f.write_text(f.read_text()+'\n[data-el="crossrail-chart-donut"].donut{width:100%;height:100%;aspect-ratio:auto}[data-el="crossrail-chart-donut"].donuts>.donut{width:auto}\n')
f=c/'elements/legend/element.css';f.write_text(f.read_text()+'\n[data-el="crossrail-legend"]:has(.key>b){align-items:stretch}\n')
s='[data-el="crossrail-card"].quiet:has(.fig):not(:has(.mark,.kick))';f=c/'elements/card/element.css';f.write_text(f.read_text()+f'\n{s} .parts{{grid-template-rows:41px 1fr}}{s} .fig{{font-size:var(--type-40)}}\n')
s='[data-el="crossrail-versus"]:has(.side>.pill)';f=c/'elements/versus/element.css';f.write_text(f.read_text()+f'\n{s} .vs::before{{content:"";position:absolute;left:calc(var(--gap)*-1);top:calc(var(--gap-sm)*5/6);width:52px;height:46px;background:var(--a1-6);clip-path:polygon(0 20%,68% 20%,68% 0,100% 50%,68% 100%,68% 80%,0 80%)}}\n')
f=p/'reassembled/slide_19.html';s=f.read_text().replace('<div class="vs"><span class="icon" data-icon="move-right"></span></div>','<div class="vs"></div>');f.write_text(s)
# Correct the independent replicas at their source, never by loading library CSS.
f=p/'replica/replica.css';s=f.read_text();s="@font-face{font-family:'Pretendard Variable';src:url('../assets/fonts/artifacts/pretendard/PretendardVariable.woff2');font-weight:100 900;font-style:normal}"+s;f.write_text(s)
for f in sorted((p/'replica').glob('slide_*.html')):
 n=int(f.stem.split('_')[1]);s=f.read_text()
 def fix(m):
  st,t=m.groups();plain=html.unescape(re.sub('<[^>]+>','',t)).strip();fs=re.search(r'font-size:(\d+)px',st);tp=re.search(r'top:(-?[\d.]+)px',st)
  if not fs:return m[0]
  v=int(fs[1]);y=float(tp[1]) if tp else 0
  if v==28:
   st=st.replace('font-size:28px','font-size:26px');st+='letter-spacing:-0.8px;'
  elif v==44:st=st.replace('font-size:44px','font-size:40px')
  elif v==20:st=st.replace('font-size:20px','font-size:18px')
  if v==64:
   st=re.sub(r'letter-spacing:[^;]+;?','',st)+'letter-spacing:-1.472px;'
   if y==122:st=st.replace('top:122px','top:121px')
  if v==18 and re.search('[가-힣]',plain):st=st.replace('line-height:1.34','line-height:1.22')+'letter-spacing:-0.8px;'
  if y in [98,99] and plain and not re.search('[가-힣]',plain):
   st+="font-family:'Pretendard Variable';letter-spacing:0;"
   if plain.isdigit():st=re.sub('left:115[57]px','left:1147px',st)
  if n==10:
   if y==263:st=st.replace('top:263px','top:261px')
   if y==500:st=st.replace('top:500px','top:498px').replace('left:103px','left:104px')
   if y==566:st=st.replace('top:566px','top:565px').replace('letter-spacing:-0.8px','letter-spacing:-0.9px')
  return '<div style="'+st+'">'+t+'</div>'
 s=re.sub(r'<div style="([^"]*)">(.*?)</div>',fix,s);f.write_text(s)
print('shared headers and all 30 independent replica typography sources corrected')

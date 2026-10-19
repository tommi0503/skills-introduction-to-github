"""Reassemble scene data with the Rhetis collection's semantic components.
Page-authored .overrides retains source composition; the collection itself is unchanged.
"""
from pathlib import Path
import json,html,re
R=Path(__file__).resolve().parents[1]; C=R/'library/rhetis-report'; data=json.loads((R/'review/scenes.json').read_text());svgs=json.loads((R/'review/svg-scenes.json').read_text());steps=json.loads((R/'contract/type-steps.json').read_text())
esc=lambda s:html.escape(str(s),quote=True)
css='\n'.join(p.read_text() for p in [C/'kit/css/tokens.css',C/'foundation/foundation.css',*sorted(C.glob('elements/*/element.css'))]);css+='\n.slide{'+''.join(f'--type-{n}:{n}px;'for n in steps)+'}'
adapter='''
body{margin:0;background:#dfe2df}.slide{--font-body:"Pretendard Variable";--font-display:"Pretendard Variable"}.sheet-label{margin:20px 0 8px;font:14px Arial;color:#364039}.slide{margin:0;break-after:page;page-break-after:always}.slide>.page{inset:0;display:block}.slide .page>.head{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);border:0;padding:0;gap:0}.slide .body{position:absolute;inset:0;gap:0}.slide .body>.overrides{position:relative;width:100%;height:100%;grid-column:1 / span 12;grid-row:1 / span 6}.overrides>[data-el]{min-width:0;min-height:0;margin:0;box-shadow:none}.overrides>.stat{display:block;border:0;padding:0;background:none}.overrides .stat .fig,.overrides .stat .name,.overrides .stat .note{display:block!important}.overrides>.stat>.parts{display:block;margin:0;padding:0;width:100%;height:100%}.overrides .stat .name,.overrides .stat .fig,.overrides .stat .note{font:inherit;letter-spacing:inherit;line-height:inherit;color:inherit;white-space:pre-wrap;overflow-wrap:normal;word-break:normal}.overrides>.card{padding:0}.overrides>.pill{padding:0;min-height:0}.overrides>.pill>.parts{display:flex;align-items:center;justify-content:center;width:100%;height:100%;gap:0}.overrides>.pill .name{font:inherit;line-height:inherit;letter-spacing:inherit;color:inherit;white-space:pre}.overrides>.frame{display:block;padding:0;margin:0;min-width:0;min-height:0}.overrides>.frame>.seat{height:100%;width:100%;border-radius:inherit}.overrides>.tag{padding:0;display:flex;justify-content:center;align-items:center;border:0;background:none;min-height:0}.overrides>.tag svg{width:100%;height:100%}.overrides>.deco{position:absolute}.overrides>.tablebox{padding:0;border:0;overflow:visible;border-radius:0}.overrides .table{width:100%;height:100%;border-collapse:collapse;font:inherit}.overrides .table td,.overrides .table th{font:inherit;padding:12px;border:0;border-bottom:1px solid var(--line);color:inherit}.overrides .table th{background:var(--surface);text-align:inherit}.overrides>.donut{aspect-ratio:auto}.overrides>.donut .fig{font:inherit;color:inherit}.overrides>.bars{padding:0;gap:6%;border:0}.overrides>.bars .bar b,.overrides>.bars .bar span{font-size:var(--type-16)}.overrides>.deco svg{overflow:visible}
@page{size:1280px 720px;margin:0}@media print{body{background:white}.sheet-label{display:none}.slide{margin:0}}
'''
links='<link rel="stylesheet" href="public/fonts/assembly-fonts.css">';pages=[];mapping=[]
for d in data:
 for s in d['slides']:
  key=d['id']+'-'+s['id'];els=[]
  for i,e in enumerate(s['elements']):
   kind=e['kind'];text=e.get('text','');font=e.get('font','Inter, Pretendard, sans-serif').replace('Inter','Inter Variable').replace('Pretendard','Pretendard Variable');sz=min(steps,key=lambda n:abs(n-e.get('size',32)))
   style=f"position:absolute;left:{e['x']}%;top:{e['y']}%;width:{e['w']}%;height:{e['h']}%;font-family:{esc(font)};font-size:var(--type-{sz});font-weight:{e.get('weight',400)};font-style:{e.get('fontStyle','normal')};text-align:{e.get('align','left')};line-height:{e.get('lineHeight',1.12)};letter-spacing:{e.get('letterSpacing',0)}px;word-spacing:{e.get('wordSpacing',0)}px;--ink:{esc(e.get('color','#171717'))};color:var(--ink);opacity:{e.get('opacity',1)};border-radius:{str(e.get('radius',0))+('px' if isinstance(e.get('radius',0),(int,float)) else '')};"
   if e.get('clipPath'):style+=f"clip-path:{e['clipPath']};"
   if e.get('rotate'):style+=f"transform:rotate({e['rotate']}deg);transform-origin:top left;"
   content=esc(text)
   if e.get('runs'):content=''.join(f'<span style="color:{esc(r.get("color",e.get("color","inherit")))};font-weight:{r.get("weight",e.get("weight",400))}">{esc(r["text"])}</span>'for r in e['runs'])
   root='';contract=''
   if kind=='text':
    contract='metric';role='fig'if e.get('size',0)>=44 else'name'if e.get('weight',400)>=600 else'note';style+='background:none;';
    if e.get('scaleX'):
     scale=e['scaleX'];style+=f"width:{e['w']/scale}%;transform:scaleX({scale});transform-origin:top left;"
    innerstyle='height:100%;display:flex!important;flex-direction:column;justify-content:'+({"middle":"center","bottom":"flex-end"}.get(e.get("valign"),"flex-start"))+';' if e.get("valign") else ""
    root=f'<div class="stat" data-el="rhetis-report-metric" style="{style}"><div class="parts"><div class="{role}" style="{innerstyle}">{content}</div></div></div>'
   elif kind=='chip':
    contract='pill';style+=f"--surface:{esc(e.get('fill','transparent'))};background:var(--surface);border:{esc(e.get('border','none'))};";root=f'<div class="pill" data-el="rhetis-report-pill" style="{style}"><div class="parts"><span class="name">{content}</span></div></div>'
   elif kind=='box':
    contract='card';style+=f"--surface:{esc(e.get('fill','transparent'))};background:var(--surface);border:{esc(e.get('border','none'))};"
    if e.get('shadow'):style+=f"box-shadow:{esc(e['shadow'])};"
    root=f'<div class="card" data-el="rhetis-report-card" style="{style}"><div class="parts"></div></div>'
   elif kind=='image':
    contract='image-frame';style+=f"--surface-2:#e5e5e5;border:{esc(e.get('border','none'))};";root=f'<div class="frame" data-el="rhetis-report-image-frame" style="{style}"><div class="seat" data-ph="" role="img" aria-label="{esc(text or "Image placeholder")}"></div></div>'
   elif kind in ['icon','path']:
    svg=svgs.get(key,[])[i]if i<len(svgs.get(key,[]))else'';svg=svg or'';svg=re.sub(r'url\(#([^)]*)\)',lambda m:f'url(#{key}-{i}-{m[1]})',svg);svg=re.sub(r'id="([^"]*)"',lambda m:f'id="{key}-{i}-{m[1]}"',svg)
    if kind=='icon':contract='tag';root=f'<span class="tag" data-el="rhetis-report-tag" style="{style}">{svg}</span>'
    else:contract='foundation.deco';root=f'<div class="deco" style="{style}">{svg}</div>'
   elif kind=='line':
    contract='foundation.deco';style+=f"background:var(--ink);{'width'if e.get('vertical')else'height'}:{e.get('strokeWidth',1)}px;";root=f'<div class="deco" style="{style}"></div>'
   elif kind=='donut':
    contract='chart-donut';vs=e.get('values',[75,25]);v=vs[0]/sum(vs)*100;style+=f"--v:{v};--surface:{esc(e.get('border','#fff'))};";root=f'<div class="donut" data-el="rhetis-report-chart-donut" style="{style}"><div class="fig">{content}</div><div class="name"></div></div>'
   elif kind=='bars':
    contract='chart-bar';vs=e.get('values',[]);style+=f"--max:{e.get('max',max(vs,default=100))};";bars=''.join(f'<div class="bar tone-{j%5+1}" style="--v:{v}"><b>{v}{esc(text)}</b><span>{esc(e.get("labels",[])[j]if j<len(e.get("labels",[]))else"")}</span></div>'for j,v in enumerate(vs));root=f'<div class="bars{ " h"if e.get("vertical")else""}" data-el="rhetis-report-chart-bar" style="{style}">{bars}</div>'
   elif kind=='table':
    contract='table';rows=e.get('rows',[]);style+=f"--line:{esc(e.get('border','#ddd'))};--surface:{esc(e.get('fill','transparent'))};";head=''.join('<th>'+esc(c)+'</th>'for c in rows[0])if rows else'';body=''.join('<tr>'+''.join('<td>'+esc(c)+'</td>'for c in row)+'</tr>'for row in rows[1:]);root=f'<div class="tablebox" data-el="rhetis-report-table" style="{style}"><table class="table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'
   els.append(root);mapping.append({'slide':key,'sourceElement':i,'kind':kind,'contract':contract,'typeStep':sz if kind in ['text','chip']else None})
  pages.append(f'<p class="sheet-label">{esc(d["title"])} · {s["id"]}</p><section class="slide" data-assembly="{key}" style="--page:{s["background"]}"><div class="page"><header class="head"><h1 class="title">{esc(s["title"])}</h1></header><div class="body"><div class="overrides" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join(els)+'</div></div></div></section>')
(R/'assembly.html').write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Rhetis Report · Collection assembly</title>'+links+'<style>'+css+adapter+'</style></head><body>'+''.join(pages)+'</body></html>');(R/'review/assembly-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2));print('Assembled',len(pages),'slides',len(mapping),'components')

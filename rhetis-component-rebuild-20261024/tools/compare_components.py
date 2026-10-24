"""One replica | 12x6 | minimum comparison sheet per mapped element.
The rendering host supplies the source palette; collection CSS remains palette-independent.
"""
from pathlib import Path
import argparse,json,re,math,io,sys
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(Path(__file__).resolve().parent))
from size_review import paths,assets,document,wrapper,MIN_RE,MEASURE,LABEL,browser,serve_url,BASE,OLD,source_hash

def compare(name,only=None):
 w,c,r=paths(name);assets(name);(r/'sheets').mkdir(exist_ok=True);(r/'probes').mkdir(exist_ok=True);data=json.loads((r/'map.json').read_text());by={}
 for x in data['instances']:
  if x.get('leaf') and x['use']not in ['unexpressible','furniture','background'] and (not only or x['leaf']in only):by.setdefault(x['leaf'],[]).append(x)
 report=[];before=source_hash(c)
 with sync_playwright() as pw:
  b=browser(pw)
  for leaf,instances in sorted(by.items()):
   rows=[];seen=set()
   for inst in sorted(instances,key=lambda z:(z['use']!='base',z['page'])):
    family=inst['use'] if inst['use'].startswith('variant:') else 'base'
    # One source base and every explicitly mapped semantic variant. Repeats remain in map.json.
    if family in seen:continue
    seen.add(family);stem=Path(inst.get('fixture','replica-'+inst['page'])).stem
    fix=c/'elements'/leaf/'fixtures'/(stem+'.html')
    if not fix.exists():raise ValueError(f'{name}/{leaf} missing mapped fixture {fix}')
    content=fix.read_text();m=MIN_RE.match(content);mins=[tuple(map(int,a))for a in re.findall(r'(\d+)x(\d+)',m.group(1) if m else '')]
    if not mins:raise ValueError('Missing minimum: '+str(fix))
    source=OLD/name/'review/replica'/('slide-'+inst['page']+'.png'if name=='diecut'else'slide_'+inst['page']+'.png')
    box=inst['bbox'];source_im=Image.open(source).convert('RGB').crop((max(0,math.floor(box[0])),max(0,math.floor(box[1])),min(1280,math.ceil(box[0]+box[2])),min(720,math.ceil(box[1]+box[3]))))
    probe=r/'probes'/(leaf+'-source-palette.html');probe.write_text(document(c,wrapper(content,12,6,'light'),host=True,title=name+' '+leaf+' source comparison'))
    page=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1);page.goto(serve_url(probe),wait_until='load');page.evaluate('document.fonts.ready');pieces=[('replica '+inst['page']+' / '+inst['use'],source_im)]
    for co,ro in [(12,6),mins[0]]:
     page.evaluate('([co,ro])=>{let e=document.querySelector(".slide>.page>.body").firstElementChild;e.style.gridColumn="1 / span "+co;e.style.gridRow="1 / span "+ro}',[co,ro]);page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');a=page.evaluate(MEASURE,[co,ro]);z=a['slotRect'];x=max(0,math.floor(z['x'])-6);y=max(0,math.floor(z['y'])-6);ww=min(1280-x,math.ceil(z['width'])+12);hh=min(720-y,math.ceil(z['height'])+12);shot=page.screenshot(clip={'x':x,'y':y,'width':ww,'height':hh},animations='disabled');pieces.append((str(co)+'x'+str(ro)+(' MIN'if(co,ro)==mins[0]else''),Image.open(io.BytesIO(shot)).convert('RGB')))
    page.close();rw=250+sum(im.width for _,im in pieces)+32;rh=max(im.height for _,im in pieces)+60;row=Image.new('RGB',(rw,rh),'#e8e8ec');draw=ImageDraw.Draw(row);draw.text((8,10),stem,font=LABEL,fill='#111');draw.text((8,40),'bbox '+','.join(str(round(x,1))for x in box),font=LABEL,fill='#111');x=250
    for label,im in pieces:draw.text((x,8),label,font=LABEL,fill='#111');row.paste(im,(x,40));x+=im.width+16
    rows.append(row);report.append({'leaf':leaf,'page':inst['page'],'use':inst['use'],'bbox':box,'fixture':stem,'min':list(mins[0])})
   if not rows:continue
   out=Image.new('RGB',(max(z.width for z in rows),sum(z.height for z in rows)+40),'#e8e8ec');draw=ImageDraw.Draw(out);draw.text((10,10),name+' / '+leaf+' / source palette',font=LABEL,fill='#111');y=40
   for z in rows:out.paste(z,(0,y));y+=z.height
   out.save(r/'sheets'/(leaf+'-replica.png'),compress_level=3);print(name,leaf,'comparison',len(rows),'rows',flush=True)
  b.close()
 (r/'replica-comparison-audit.json').write_text(json.dumps({'sourceSHA256':before,'sourceUnchanged':before==source_hash(c),'rows':report,'palette':'source-palette.json; reference size sheets remain on the library palette'},ensure_ascii=False,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('name');p.add_argument('--only');a=p.parse_args();compare(a.name,set(a.only.split(','))if a.only else None)

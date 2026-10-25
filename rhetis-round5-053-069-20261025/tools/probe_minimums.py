"""Probe overly conservative full-slide minima without changing rendering CSS.
Only12x6 fixtures are candidates. A proposed smaller minimum must pass all
listed grid sizes that dominate it, in both themes, with >=10px visible text.
The normal sheet engine performs the full paint/contrast/chip check afterwards.
"""
import asyncio,json,re,time,hashlib,argparse
from pathlib import Path
from playwright.async_api import async_playwright
from element_sheets import ROOT,SIZES,PALETTE,load_css,fixture,AUDIT
async def main(apply=False):
 targets=[]
 for c in json.loads((ROOT/'collections.json').read_text()):
  cid=c['id']
  for f in sorted((ROOT/cid/'elements').glob('*/fixtures/*.html')):
   if re.search(r'<!--\s*min:\s*12x6\s*-->',f.read_text()):targets.append((cid,f))
 records=[]
 async with async_playwright()as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);page=await b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  csses={cid:load_css(ROOT/cid)for cid,_ in targets}
  for cid,f in targets:
   before=hashlib.sha256(f.read_bytes()).hexdigest();raw=f.read_text();states=[]
   for mode in ['light','dark']:
    palette='.slide{'+''.join(k+':'+v+';'for k,v in PALETTE[mode].items())+'}'
    articles=''.join(f'<article data-fixture="{f.stem}" data-size="{c}x{r}"><section class="slide"><div class="page"><div class="body">{fixture(raw,c,r)}</div></div></section></article>'for c,r in SIZES)
    doc='<html><meta charset="utf-8"><link rel="stylesheet" href="../fonts/fonts.css"><style>'+csses[cid]+palette+'html,body{margin:0;width:1280px}article{height:728px;width:1280px}.icon{outline:1px dashed currentColor;outline-offset:-1px;border-radius:50%}</style><body>'+articles
    w=ROOT/'.sheet-work'/'minimum-probe.html';w.write_text(doc);await page.goto('http://127.0.0.1:8767/.sheet-work/minimum-probe.html?n='+str(time.time_ns()),wait_until='load');await page.evaluate('document.fonts.ready');a=await page.evaluate(AUDIT)
    for s in a['states']:
     s['minFont']=min((t['fontSize']for t in s.pop('text')),default=100);s['fontErrors']=a['fontErrors'];s['mode']=mode;s['clean']=not(s['overflow']or s['textOverlap']or s['hiddenNameFig']or a['fontErrors'])and s['minFont']>=9.98;states.append(s)
   candidates=[]
   for c,r in SIZES:
    relevant=[s for s in states if int(s['size'].split('x')[0])>=c and int(s['size'].split('x')[1])>=r]
    if all(s['clean']for s in relevant):candidates.append((c,r))
   choice=min(candidates,key=lambda t:(t[0]*t[1],t[0],t[1]))if candidates else(12,6)
   changed=False
   if apply and choice!=(12,6):
    assert hashlib.sha256(f.read_bytes()).hexdigest()==before,'Fixture changed during probe'
    f.write_text(re.sub(r'<!--\s*min:\s*12x6\s*-->',f'<!-- min: {choice[0]}x{choice[1]} -->',raw,count=1));changed=True
   records.append({'path':str(f.relative_to(ROOT)),'beforeSha256':before,'afterSha256':hashlib.sha256(f.read_bytes()).hexdigest(),'previous':'12x6','proposed':str(choice[0])+'x'+str(choice[1]),'applied':changed,'states':states})
   print(cid,f.parent.parent.name,f.stem,'12x6 ->',choice,flush=True)
  await b.close()
 (ROOT/'minimum-probe.json').write_text(json.dumps({'createdUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'policy':'Both-mode geometric/text probe; full final sheet audit remains mandatory. Minimum chosen from the nine requested sizes.','fixtures':records},ensure_ascii=False,indent=2))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--apply',action='store_true');asyncio.run(main(a.parse_args().apply))

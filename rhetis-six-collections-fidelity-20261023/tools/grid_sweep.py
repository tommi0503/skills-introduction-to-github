"""Review every declared minimum through 12x6 using the generated preview sheets.
No screenshots are changed. Diagnostics retain representative details and all case counts.
"""
from render_review import *
import argparse

def sweep(root,name,out,only=None):
 root=Path(root).resolve();collection=root/'collection'/name
 def fingerprint():
  h=hashlib.sha256()
  for path in sorted(p for p in collection.rglob('*') if p.is_file()):h.update(str(path.relative_to(collection)).encode());h.update(path.read_bytes())
  return h.hexdigest()
 before=fingerprint()
 spec=importlib.util.spec_from_file_location('rhetis_preview',REF/'tools'/'preview.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 steps=json.loads((REF/'contract/type-steps.json').read_text());palette=json.loads((REF/'contract/palette.json').read_text())
 for mode in ['light','dark']:
  (root/'review'/'library'/f'parent-{mode}-audit.html').write_text(module.sheet(collection,steps,palette,dark=mode=='dark',fonts_href='../assets/fonts/fonts.css'))
 allcases=[];stats={'cases':0,'clippedCases':0,'overflowCases':0,'contrastCases':0,'fontFailures':0,'hiddenEssentialCases':0,'zeroElementRootCases':0};bad=[]
 with sync_playwright() as p:
  b=browser(p);ctx=b.new_context(viewport={'width':1280,'height':720},device_scale_factor=1);source=ctx.new_page();probe=ctx.new_page()
  for mode in ['light','dark']:
   path=root/'review'/'library'/f'parent-{mode}-audit.html';load(source,path);load(probe,path)
   probe.add_style_tag(content='body{display:block;margin:0;padding:0;width:1280px;height:720px;overflow:hidden}body>.slide{width:1280px;height:720px;transform:none;position:relative}')
   fixtures=source.locator('body>article').evaluate_all('''(xs)=>xs.map(e=>({title:e.querySelector('h2').textContent,html:e.querySelector('.frame>.slide').outerHTML}))''')
   for f in fixtures:
    folder=f['title'].split(' / ')[0]
    if folder=='foundation' or (only and folder not in only):continue
    mins=[(int(c),int(r))for c,r in re.findall(r'(\d+)x(\d+)',f['title'])] or [(12,6)]
    cases=[(c,r)for c in range(1,13)for r in range(1,7)if any(c>=mc and r>=mr for mc,mr in mins)]
    probe.evaluate('(html)=>document.body.innerHTML=html',f['html']);probe.evaluate('document.fonts.ready')
    for c,r in cases:
     probe.evaluate('''([c,r])=>{let el=document.querySelector('.slide>.page>.body')?.firstElementChild;if(el){el.style.gridColumn='1 / span '+c;el.style.gridRow='1 / span '+r}}''',[c,r])
     a=probe.evaluate(AUDIT_JS);stats['cases']+=1
     row={'mode':mode,'fixture':f['title'],'slot':f'{c}x{r}','clipped':len(a['clipped']),'overflow':len(a['overflow']),'contrast':len(a['contrast']),'hiddenEssential':len(a['hiddenEssential']),'zeroElementRoots':len(a.get('zeroElementRoots',[]))}
     allcases.append(row)
     for key,flag in [('clippedCases',a['clipped']),('overflowCases',a['overflow']),('contrastCases',a['contrast']),('hiddenEssentialCases',a['hiddenEssential']),('zeroElementRootCases',a.get('zeroElementRoots',[]))]:
      if flag:stats[key]+=1
     stats['fontFailures']+=len(a['failedFonts'])
     if a['clipped'] or a['contrast'] or a['hiddenEssential'] or a.get('zeroElementRoots'):
      bad.append({**row,'clippedDetails':a['clipped'][:5],'contrastDetails':a['contrast'][:5],'hiddenEssentialDetails':a['hiddenEssential'][:5],'zeroElementRootDetails':a.get('zeroElementRoots',[])[:5]})
    print(name,mode,folder,f['title'].split(' / ')[1],len(cases),flush=True)
  b.close()
 result={'collection':name,'folders':sorted(only) if only else 'all','sourceSHA256':before,'sourceUnchanged':before==fingerprint(),'summary':stats,'cases':allcases,'issues':bad,'scope':'Every column/row count that dominates at least one declared minimum; no minimums were reduced by the reviewer. Raw overflow includes intentional connectors and externally positioned labels and requires visual review.'}
 Path(out).write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(stats),flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--root',required=True);a.add_argument('--name',required=True);a.add_argument('--out',required=True);a.add_argument('--only');x=a.parse_args();sweep(x.root,x.name,x.out,set(x.only.split(',')) if x.only else None)

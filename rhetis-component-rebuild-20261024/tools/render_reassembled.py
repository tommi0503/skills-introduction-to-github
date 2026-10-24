"""1280x720 render and original | frozen replica | new contract assembly triples."""
from pathlib import Path
import sys,json,re,hashlib,argparse
from PIL import Image
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(Path(__file__).parent))
from size_review import browser,serve_url,source_hash,BASE,OLD,AUDIT_JS
INV=json.loads(Path('/workspace/work/inventory.json').read_text());IDS=dict(nocturne='006',inflexion='011',diecut='012',afterglow='015',dockside='016',confluence='020')
def run(n):
 c=BASE/n/'collection'/n;review=BASE/n/'review';folder=review/'reassembled';compare=review/'compare-reassembled';compare.mkdir(exist_ok=True);out=[]
 with sync_playwright() as pw:
  b=browser(pw)
  for f in sorted(folder.glob('*.html')):
   if not re.search(r'\d\d$',f.stem):continue
   pp=re.search(r'(\d\d)$',f.stem)[1];p=b.new_page(viewport={'width':1280,'height':720});p.goto(serve_url(f),wait_until='load');p.evaluate('document.fonts.ready');p.add_script_tag(path='/workspace/work/tools/icons-runtime.js');p.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');a=p.evaluate(AUDIT_JS);png=f.with_suffix('.png');p.screenshot(path=str(png),clip={'x':0,'y':0,'width':1280,'height':720},animations='disabled');a['file']=f.name;a['htmlSHA256']=hashlib.sha256(f.read_bytes()).hexdigest();out.append(a);p.close()
   orig=next(x for x in INV if x['deck'].startswith(IDS[n]) and re.search(r'(\d+)\.png$',x['file'])[1].zfill(2)==pp)
   op=Path('/workspace')/orig['path'];rp=OLD/n/'review/replica'/('slide-'+pp+'.png'if n=='diecut'else'slide_'+pp+'.png');im=Image.new('RGB',(3840,720))
   for i,path in enumerate([op,rp,png]):im.paste(Image.open(path).convert('RGB'),(i*1280,0))
   im.save(compare/(f.stem+'.png'),compress_level=3)
  b.close()
 (review/'reassembled-audit.json').write_text(json.dumps({'collection':n,'sourceSHA256':source_hash(c),'pages':out},ensure_ascii=False,indent=2));print(n,len(out),'pages',sum(len(x['clipped'])for x in out),'clip',sum(len(x['failedFonts'])for x in out),'fontErrors',flush=True)
if __name__=='__main__':
 for n in sys.argv[1:]:run(n)

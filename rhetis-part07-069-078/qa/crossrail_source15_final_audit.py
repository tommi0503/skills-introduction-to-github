"""Narrow final source-only photo-rule follow-up; does not redate broad audits."""
import hashlib, importlib.util, io, json
from PIL import Image
from playwright.sync_api import sync_playwright
from audit_css import BASE, REFERENCE
from clipping_audit import CHECK

root = BASE / 'crossrail-project/crossrail'
def files():
    return {str(f.relative_to(root)): hashlib.sha256(f.read_bytes()).hexdigest()
            for f in sorted(root.rglob('*')) if f.is_file()}
def tree_sha(snapshot):
    return hashlib.sha256(json.dumps(snapshot,sort_keys=True,separators=(',',':')).encode()).hexdigest()
spec = importlib.util.spec_from_file_location('pv', REFERENCE/'tools/preview.py')
pv = importlib.util.module_from_spec(spec); spec.loader.exec_module(pv)
start = files()
result = {'scope': 'Single foundation photo-line top offset; source15 and image-circle minimum/full only.',
          'collectionSourceTreeSha256': tree_sha(start), 'fixtures': [],
          'limitations': 'Earlier broad reports retain their previous source snapshots. No global visual identity claim.'}
probe = '''e=>{const s=getComputedStyle(e,'::before'),d=document.createElement('div');
for(let k of ['position','top','left','right','bottom','width','height','transform','translate','boxSizing'])d.style[k]=s[k];
d.style.margin='0';d.style.padding='0';d.style.border='0';e.appendChild(d);let r=d.getBoundingClientRect();
const out={x:r.x,y:r.y,width:r.width,height:r.height,background:s.backgroundColor};d.remove();return out}'''
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1280,'height':720})
    page.goto('http://127.0.0.1:8765/crossrail-project/reassembled/slide_15.html',wait_until='networkidle')
    page.evaluate('document.fonts.ready')
    line=page.locator('.body').evaluate(probe)
    centers=page.locator('.body>.frame>.seat.avatar').evaluate_all('es=>es.map(e=>{let r=e.getBoundingClientRect();return [r.x+r.width/2,r.y+r.height/2]})')
    raw=page.screenshot(path=str(BASE/'qa/crossrail-source15-final.png'))
    im=Image.open(io.BytesIO(raw)).convert('RGB')
    result['source15']={'line':line,'photoCenters':centers,'pngSize':list(im.size),
                        'linePixel10x354':list(im.getpixel((10,354))),
                        'fontStatus':page.evaluate('document.fonts.status'),
                        'ruleAligned':abs(line['y']-354)<.6 and all(abs(c[1]-(line['y']+.5))<1 for c in centers)}
    for dark in [False,True]:
        markup=pv.sheet(root,json.loads((REFERENCE/'contract/type-steps.json').read_text()),json.loads((REFERENCE/'contract/palette.json').read_text()),dark=dark,fonts_href='/crossrail-project/assets/fonts/fonts.css')
        page.set_content(markup,wait_until='networkidle');page.evaluate('document.fonts.ready')
        a=page.locator('article').filter(has=page.locator('h2',has_text='image-frame / image-circle')).first
        page.locator('article').evaluate_all("es=>es.forEach(e=>e.style.display='none')")
        a.evaluate("a=>a.style.display='block'")
        for size in [[4,3],[12,6]]:
            a.evaluate('''(a,size)=>{let f=a.querySelector('.frame');f.style.width='1280px';f.style.height='720px';f.querySelector('.slide').style.transform='none';for(let e of a.querySelector('.body').children){e.style.gridColumn='1 / span '+size[0];e.style.gridRow='1 / span '+size[1]}}''',size)
            geometry=a.evaluate((BASE/'qa/functional.js').read_text())
            screenshot=f'crossrail-photo-rule-{"dark" if dark else "light"}-{size[0]}x{size[1]}.png'
            a.locator('.slide').screenshot(path=str(BASE/'qa'/screenshot))
            result['fixtures'].append({'mode':'dark' if dark else 'light','size':size,
                                       'sheetSha256':hashlib.sha256(markup.encode()).hexdigest(),
                                       'geometry':geometry,'textClips':a.evaluate(CHECK),'screenshot':screenshot})
    browser.close()
result['sourceUnchanged']=start==files()
result['passed']=result['sourceUnchanged'] and result['source15']['ruleAligned'] and all(not c['textClips'] and not any(c['geometry'][k] for k in ['stack','donut','balance','bullet','seats','graphics','polygonText']) for c in result['fixtures'])
(BASE/'qa/crossrail-source15-final-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(result['collectionSourceTreeSha256'],result['source15'], 'passed',result['passed'])

import asyncio,json,re,math
from pathlib import Path
from PIL import Image,ImageDraw
import fitz
from playwright.async_api import async_playwright
W=Path('/workspace/output/fluxweave-review');D=Path('/workspace/work/deck/miricanvas_기업_selected/002_1leen_파랑_미니멀_기업소개서_기획서');TMP=Path('/workspace/work/fluxweave/render');TMP.mkdir(exist_ok=True)
async def main():
 checks=[]
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for f in sorted((W/'reassembled').glob('slide_*.html')):
   await page.goto('http://127.0.0.1:8762/reassembled/'+f.name);await page.evaluate('document.fonts.ready');await page.screenshot(path=str(f.with_suffix('.png')))
   checks.append({'kind':'reassembled','page':f.name,'font':await page.evaluate("document.fonts.check('16px \"Pretendard Variable\"')"),'size':await page.locator('.slide').bounding_box(),'overflow':await page.evaluate('''()=>{let s=document.querySelector('.slide').getBoundingClientRect();return [...document.querySelectorAll('[data-el]')].filter(e=>{let r=e.getBoundingClientRect();return r.right>s.right+1||r.bottom>s.bottom+1||r.left<s.left-1||r.top<s.top-1}).map(e=>e.dataset.el)}''')})
   im=Image.new('RGB',(2560,720),'white');im.paste(Image.open(D/f.with_suffix('.png').name),(0,0));im.paste(Image.open(f.with_suffix('.png')),(1280,0));im.save(W/'compare-reassembled'/f.with_suffix('.png').name)
  doc=fitz.open()
  for f in sorted((W/'reassembled').glob('slide_*.png')):
   pg=doc.new_page(width=960,height=540);pg.insert_image(pg.rect,filename=str(f))
  doc.save(W/'reassembled'/'reassembled.pdf',garbage=4,deflate=True,deflate_images=True);doc.close()
  for mode in ['light','dark']:
   await page.goto('http://127.0.0.1:8762/library/'+mode+'.html');await page.evaluate('document.fonts.ready')
   await page.add_style_tag(content='body{display:block;padding:0;background:white}article{display:none}article.active{display:block}article>h2{display:none}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}')
   entries=await page.locator('article>h2').all_text_contents(); doc=fitz.open();groups={}
   for i,title in enumerate(entries):
    await page.evaluate('''i=>{document.querySelectorAll('article').forEach((e,j)=>e.classList.toggle('active',i===j))}''',i)
    fn=TMP/f'{mode}-{i:03}.png';await page.screenshot(path=str(fn));elem=title.split('/')[0].strip();groups.setdefault(elem,[]).append((title,fn));pg=doc.new_page(width=960,height=540);pg.insert_image(pg.rect,filename=str(fn))
   doc.save(W/'library'/f'library-{mode}.pdf',garbage=4,deflate=True,deflate_images=True);doc.close()
   for elem,items in groups.items():
    # Full-size element sheet with multiple fixture panels; source slides remain 1280x720.
    im=Image.new('RGB',(1280,math.ceil(len(items)/2)*390),'#e8e8ec');dr=ImageDraw.Draw(im)
    for i,(title,fn) in enumerate(items):
     x=(i%2)*640;y=(i//2)*390;thumb=Image.open(fn).resize((640,360));im.paste(thumb,(x,y+30));dr.text((x+10,y+8),title[:70],fill='#333')
    d=W/'library'/elem;d.mkdir(exist_ok=True);im.save(d/(mode+'.png'))
   print(mode,len(entries),'fixtures',len(groups),'sheets',flush=True)
  await b.close()
 (W/'render-checks.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False))
asyncio.run(main())

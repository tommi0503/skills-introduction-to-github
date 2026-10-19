from pathlib import Path
import subprocess,json,hashlib,io
from PIL import Image
import fitz
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'build/library';out.mkdir(parents=True,exist_ok=True)
fontcss=subprocess.check_output(['node','--input-type=module','-e',"import {fontCSS} from './src/renderer.mjs';process.stdout.write(fontCSS)"],cwd=ROOT,text=True).replace('../../../assets/','../../assets/')
for mode in ['light','dark']:
 args=['python',str(ROOT/'tools/preview.py'),str(ROOT/'collection/blueprint-06'),str(ROOT/'contract/type-steps.json'),'--out',str(out/(mode+'.html'))]
 if mode=='dark':args.append('--dark')
 subprocess.run(args,check=True,capture_output=True)
 p=out/(mode+'.html');p.write_text(p.read_text().replace('</head>','<style>'+fontcss+'</style></head>'))
 doc=fitz.open()
 for png in sorted((ROOT/'review/library-render-final').glob('*-full-'+mode+'.png')):
  pg=doc.new_page(width=1280,height=720);raw=io.BytesIO();Image.open(png).convert('RGB').save(raw,format='JPEG',quality=95);pg.insert_image(pg.rect,stream=raw.getvalue())
 doc.save(ROOT/'pdfs'/('library-'+mode+'.pdf'),garbage=4,deflate=True);print(mode,len(doc),'library PDF pages');doc.close()

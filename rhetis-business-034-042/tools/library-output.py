from pathlib import Path
import subprocess,shutil,json,hashlib
import fitz
ROOT=Path(__file__).resolve().parents[1];C=ROOT/'collection/business-spectrum'
def main():
 out=ROOT/'build/library';out.mkdir(parents=True,exist_ok=True)
 for mode in ['light','dark']:
  args=['python',str(ROOT/'tools/preview.py'),str(C),str(ROOT/'contract/type-steps.json'),'--out',str(out/(mode+'.html'))]
  if mode=='dark':args.append('--dark')
  subprocess.run(args,check=True)
  css=subprocess.check_output(['node','--input-type=module','-e',"import {fontCSS} from './src/renderer.mjs';process.stdout.write(fontCSS)"],cwd=ROOT,text=True).replace('../../../assets/','../../assets/')
  p=out/(mode+'.html');p.write_text(p.read_text().replace('</head>','<style>'+css+'</style></head>'))
 source=C/'previews' if (C/'previews').exists() else ROOT/'renders/library'
 if source.exists():
  for mode in ['light','dark']:
   if (source/mode).resolve()!=(ROOT/'renders/library'/mode).resolve():shutil.copytree(source/mode,ROOT/'renders/library'/mode,dirs_exist_ok=True)
   if not (source/f'library-{mode}.pdf').exists():continue
   srcpdf=fitz.open(source/f'library-{mode}.pdf');doc=fitz.open()
   for idx in range(len(srcpdf)):
    pg=doc.new_page(width=1280,height=720);pg.show_pdf_page(pg.rect,srcpdf,idx)
   doc.save(ROOT/'pdfs'/f'library-{mode}.pdf');doc.close();srcpdf.close()
  for name in ['automatic.json','automatic-final.json','source-hashes.json']:
   if(source/name).exists():shutil.copy2(source/name,ROOT/'review'/('library-'+name))
 print('Library sheets, full/min PNGs, PDF and audit records exported')
if __name__=='__main__':main()

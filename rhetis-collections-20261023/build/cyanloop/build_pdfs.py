from pathlib import Path
import fitz,re
R=Path('/workspace/output/cyanloop-review');W=Path('/workspace/work/cyanloop')
tasks=[]
for mode in ['light','dark']:
 count=(R/'library'/f'{mode}.html').read_text().count('<article>');tasks.append((R/'library'/f'library-{mode}.pdf',[W/f'{mode}-{i:03}.png' for i in range(count)]))
for fold in ['replica','reassembled']:tasks.append((R/fold/f'{fold}.pdf',sorted((R/fold).glob('slide_*.png'))))
for target,images in tasks:
 d=fitz.open()
 for im in images:
  assert im.exists(),im
  p=d.new_page(width=960,height=540);p.insert_image(p.rect,filename=str(im))
 tmp=target.with_suffix('.tmp.pdf');d.save(tmp,garbage=4,deflate=True,deflate_images=True);d.close();tmp.replace(target)
 print(target.name,len(images),round(target.stat().st_size/1024/1024,2),'MiB')

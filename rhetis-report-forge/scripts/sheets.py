from PIL import Image,ImageDraw
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
P=Path(__file__).resolve().parent.parent
for mode in ['replica','assembled']:
 files=sorted((P/'renders'/mode).glob('*/*.png'));out=P/'sheets'/mode;out.mkdir(parents=True,exist_ok=True)
 pdf=canvas.Canvas(str(P/'pdfs'/f'{mode}-sheets.pdf'),pagesize=(960,540))
 overview=Image.new('RGB',(1280,((len(files)+3)//4)*204+50),'#e8eaf0');draw=ImageDraw.Draw(overview);draw.text((18,15),f'REPORT FORGE / {mode.upper()} / {len(files)} SLIDES',fill='#1b2437')
 for n in range(0,len(files),4):
  sheet=Image.new('RGB',(1280,720),'#e8eaf0');sd=ImageDraw.Draw(sheet)
  for k,p in enumerate(files[n:n+4]):
   im=Image.open(p).convert('RGB');x=24+(k%2)*640;y=(k//2)*360
   sd.text((x,y+4),f'{p.parent.name} / {p.stem}',fill='#263149');sheet.paste(im.resize((592,333),Image.Resampling.LANCZOS),(x,y+22))
   i=n+k;ox=12+(i%4)*320;oy=50+(i//4)*204;draw.text((ox,oy),f'{p.parent.name} / {p.stem}',fill='#263149');overview.paste(im.resize((304,171),Image.Resampling.LANCZOS),(ox,oy+19))
  target=out/f'sheet-{n//4+1:02}.png';sheet.save(target);pdf.drawImage(ImageReader(sheet),0,0,width=960,height=540);pdf.showPage()
 pdf.save();overview.save(P/'outputs'/f'{mode}-overview.jpg',quality=90)
 print(mode,len(files),len(list(out.glob('*.png'))),'sheets')

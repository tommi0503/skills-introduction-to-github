from pathlib import Path
from PIL import Image,ImageDraw
import sys,json
id,round,mode=sys.argv[1:]; root=Path('.')
for f in sorted((root/f'renders/{round}/{mode}').glob(f'{id}-*.png')):
 orig=Image.open(root/'public/reference'/id/(f.stem[4:]+'.png')).convert('RGB'); result=Image.open(f).convert('RGB')
 out=Image.new('RGB',(2560,760),'#243440');out.paste(orig,(0,40));out.paste(result,(1280,40));d=ImageDraw.Draw(out);d.text((16,12),'ORIGINAL  '+id+'/'+f.stem[4:],fill='white');d.text((1296,12),f'{mode.upper()}  ROUND {round}',fill='white')
 out.save(root/f'comparisons/{round}/{mode}'/(f.stem+'.jpg'),quality=92)

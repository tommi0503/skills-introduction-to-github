from PIL import Image,ImageDraw
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
id,round=sys.argv[1:3]
src=Image.open(root/'public/reference'/f'{id}.png').convert('RGB')
assert src.width==1280 and src.height in (909,910)
# A 909px recovered reference is padded by one bottom pixel; never stretched.
original=Image.new('RGB',(1280,910),'#eef0f3');original.paste(src,(0,0))
result=Image.open(root/'renders'/round/f'{id}.png').convert('RGB')
pair=Image.new('RGB',(2560,948),'#fff');pair.paste(original,(0,38));pair.paste(result,(1280,38))
d=ImageDraw.Draw(pair);d.text((18,10),f'{id}  REFERENCE (native size)',fill='#222');d.text((1298,10),f'{id}  IMPLEMENTED UI  /  round {round}',fill='#222')
pair.save(root/'comparisons'/f'round-{round}'/f'{id}.jpg',quality=94)

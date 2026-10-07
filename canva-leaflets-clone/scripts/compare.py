"""Create individual original/browser pairs; source photos are only in comparisons."""
import json,sys
from pathlib import Path
from PIL import Image,ImageDraw,ImageOps
root=Path(__file__).resolve().parents[1]
brochure,round_name=sys.argv[1:3]
meta=json.loads((root/f'comparisons/{round_name}/{brochure}.json').read_text())
for page in meta['panels']+meta['sides']:
    source=Image.open(root/page['reference']).convert('RGB')
    if page.get('crop'):
        c=page['crop'];source=source.crop((c['x'],c['y'],c['x']+c['w'],c['y']+c['h']))
    rendered=Image.open(root/page['file']).convert('RGB');assert rendered.size==(1280,720)
    if page.get('crop'):
        w,h=page['size'];factor=min(1280/w,720/h);x=(1280-w*factor)/2;y=(720-h*factor)/2
        rendered=rendered.crop((round(x),round(y),round(x+w*factor),round(y+h*factor)))
        area_w=round(w/h*720);pair_w=area_w*2+24
    else:area_w=1280;pair_w=2584
    pair=Image.new('RGB',(pair_w,752),'#f0f1f3');draw=ImageDraw.Draw(pair)
    draw.text((8,8),f'{brochure}/{page["id"]} ORIGINAL',fill='#222');draw.text((area_w+24,8),'IMPLEMENTATION '+round_name,fill='#222')
    for offset,image in [(0,source),(area_w+24,rendered)]:
        fitted=ImageOps.contain(image,(area_w,720));pair.paste(fitted,(offset+(area_w-fitted.width)//2,28+(720-fitted.height)//2))
    pair.save(root/f'comparisons/{round_name}/{brochure}-{page["id"]}.jpg',quality=95)

import json,pathlib,sys
from PIL import Image,ImageDraw,ImageOps
root=pathlib.Path(__file__).resolve().parents[1]
id,round_name=sys.argv[1:3];meta=json.loads((root/'comparisons'/round_name/f'{id}.json').read_text())
sheet=Image.new('RGB',(1800,1260),'#edf0f4');draw=ImageDraw.Draw(sheet)
for i,p in enumerate(meta['panels']):
    source=Image.open(p['reference']).convert('RGB');c=p['crop'];source=source.crop((c['x'],0,c['x']+c['w'],c['h']))
    render=Image.open(p['file']).convert('RGB');assert render.size==(1280,720)
    factor=min(1280/p['size'][0],720/p['size'][1]);left=(1280-p['size'][0]*factor)/2;top=(720-p['size'][1]*factor)/2
    paper=render.crop((round(left),round(top),round(left+p['size'][0]*factor),round(top+p['size'][1]*factor)))
    a=ImageOps.contain(source,(342,720));b=ImageOps.contain(paper,(342,720));pair=Image.new('RGB',(704,750),'#edf0f4');d=ImageDraw.Draw(pair)
    d.text((8,8),f'{id}/{p["id"]} | ORIGINAL',fill='#111');d.text((360,8),'IMPLEMENTATION '+round_name,fill='#111');pair.paste(a,((342-a.width)//2,28));pair.paste(b,(360+(342-b.width)//2,28))
    pair.save(root/'comparisons'/round_name/f'{id}-{p["id"]}.jpg',quality=94)
    thumb=pair.resize((586,624),Image.Resampling.LANCZOS);x=i%3*600;y=i//3*630;sheet.paste(thumb,(x,y));draw.text((x+5,y+625),p['id'],fill='#111')
sheet.save(root/'comparisons'/round_name/f'{id}-contact.jpg',quality=94)
for p in meta['sides']:
    source=Image.open(p['reference']).convert('RGB');render=Image.open(p['file']).convert('RGB')
    source=ImageOps.contain(source,(1280,720));reference=Image.new('RGB',(1280,720),'#eef0f3');reference.paste(source,((1280-source.width)//2,(720-source.height)//2))
    pair=Image.new('RGB',(2584,750),'#eef0f3');d=ImageDraw.Draw(pair);d.text((8,8),id+'/'+p['id']+' ORIGINAL',fill='#111');d.text((1300,8),'IMPLEMENTATION '+round_name,fill='#111');pair.paste(reference,(0,28));pair.paste(render,(1304,28));pair.save(root/'comparisons'/round_name/f'{id}-{p["id"]}.jpg',quality=94)

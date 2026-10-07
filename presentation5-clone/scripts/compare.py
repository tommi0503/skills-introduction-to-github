import json,pathlib,sys
from PIL import Image,ImageDraw,ImageOps
root=pathlib.Path(__file__).resolve().parents[1]
id=sys.argv[1];round=sys.argv[2]
meta=json.loads((root/'comparisons'/round/f'{id}.json').read_text())
render_sheet=Image.new('RGB',(1600,((len(meta['slides'])+3)//4)*260),'#e9ecf0');draw=ImageDraw.Draw(render_sheet)
pair_sheet=Image.new('RGB',(1600,((len(meta['slides'])+1)//2)*260),'#e9ecf0');pd=ImageDraw.Draw(pair_sheet)
for n,s in enumerate(meta['slides']):
 source=ImageOps.pad(Image.open(s['reference']).convert('RGB'),(1280,720),method=Image.Resampling.LANCZOS,color='#fff',centering=(.5,.5))
 render=Image.open(s['file']).convert('RGB');assert render.size==(1280,720)
 pair=Image.new('RGB',(2584,756),'#e9ecf0');d=ImageDraw.Draw(pair)
 # Keep the visual evidence deterministic across capture rounds. The round,
 # hashes and production provenance remain in the accompanying deck JSON.
 d.text((8,10),f'{id}/{s["id"]} ORIGINAL',fill='#111');d.text((1304,10),'IMPLEMENTATION',fill='#111')
 pair.paste(source,(0,30));pair.paste(render,(1304,30));pair.save(root/'comparisons'/round/f'{id}-{s["id"]}.jpg',quality=94)
 thumb=render.resize((390,219),Image.Resampling.LANCZOS);x=n%4*400;y=n//4*260
 render_sheet.paste(thumb,(x,y+28));draw.text((x+4,y+7),s['id'],fill='#222')
 pair_thumb=pair.resize((790,231),Image.Resampling.LANCZOS);x=n%2*800;y=n//2*260
 pair_sheet.paste(pair_thumb,(x,y+28));pd.text((x+4,y+7),f'{id}/{s["id"]}',fill='#222')
render_sheet.save(root/'renders'/round/f'{id}-contact.jpg',quality=94)
pair_sheet.save(root/'comparisons'/round/f'{id}-contact.jpg',quality=94)

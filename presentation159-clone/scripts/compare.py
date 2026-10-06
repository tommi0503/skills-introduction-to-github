import json,pathlib,sys
from PIL import Image,ImageDraw
root=pathlib.Path(__file__).resolve().parents[1]
deck,round=sys.argv[1:3]
meta=json.loads((root/'comparisons'/round/f'{deck}.json').read_text())
for slide in meta['slides']:
    source=Image.open(root/slide['reference']).convert('RGB')
    assert source.size==(1600,900)
    source=source.resize((1280,720),Image.Resampling.LANCZOS)
    render=Image.open(root/slide['file']).convert('RGB')
    assert render.size==(1280,720)
    pair=Image.new('RGB',(2584,756),'#e9ecf0')
    draw=ImageDraw.Draw(pair)
    draw.text((8,9),f'{deck}/{slide["id"]} ORIGINAL',fill='#111')
    draw.text((1304,9),f'IMPLEMENTATION {round}',fill='#111')
    pair.paste(source,(0,30));pair.paste(render,(1304,30))
    pair.save(root/'comparisons'/round/f'{deck}-{slide["id"]}.jpg',quality=95)


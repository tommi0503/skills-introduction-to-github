import json
from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[1]
a=json.loads((root/'review/assignment-c.json').read_text())
# Manually inspected slide edges, excluding outer contact-sheet shadows/gutters.
g={
(110,2):[(37,96,358,201),(406,96,358,201),(775,96,358,201),(37,321,358,201),(406,321,358,201),(775,321,358,201),(37,542,268,151),(313,542,268,151),(590,542,268,151),(865,542,268,151)],
(110,3):[(37,96,358,201),(406,96,358,201),(775,96,358,201),(37,321,358,201),(406,321,358,201),(775,321,358,201),(37,542,268,151),(313,542,268,151),(590,542,268,151),(865,542,268,151)],
(112,1):[(x,y,379,214) for y in [62,312,562] for x in [79,495,911]],
(112,2):[(x,y,414,233) for y in [88,340,593] for x in [46,478,910]],
(112,3):[(x,y,414,233) for y in [88,340,593] for x in [46,478,910]],
(112,4):[(x,y,606,341) for y in [102,470] for x in [68,700]],
(119,2):[(x,y,353,199) for y in [75,290,505] for x in [35,408,782]],
(119,3):[(x,y,353,199) for y in [75,290,505] for x in [35,408,782]],
(127,3):[(98,117,376,212),(497,117,376,212),(896,117,376,212),(98,351,376,212),(497,351,376,212)],
(127,4):[(x,y,376,212) for y in [117,351,585] for x in [98,497,896]],
(127,5):[(x,y,376,212) for y in [117,351,585] for x in [98,497,896]],
(127,6):[(x,y,533,300) for y in [140,475] for x in [123,690]],
(127,7):[(x,y,376,212) for y in [117,351,585] for x in [98,497,896]],
(143,2):[(71,287,601,338),(699,287,599,338)],
(143,3):[(x,y,398,224) for y in [103,345,587] for x in [71,487,900]],
(143,4):[(x,y,398,224) for y in [103,345,587] for x in [71,487,900]],
(145,2):[(x,y,351,197) for y in [-45,172,390,607] for x in [40,410,779]],
(145,3):[(x,y,351,197) for y in [40,258,476,694] for x in [40,410,779]],
(145,4):[(x,y,351,197) for y in [40,258,476,694] for x in [40,410,779]],
(151,2):[(x,y,380,214) for y in [99,349,599] for x in [79,493,909]],
(151,3):[(79,99,380,214),(493,99,380,214)],
(151,4):[(x,y,380,214) for y in [99,349,599] for x in [79,493,909]],
(152,2):[(x,y,337,190) for y in [85,295,505] for x in [58,416,775]],
(152,3):[(157,150,856,482)],
(152,5):[(x,y,444,250) for y in [125,406] for x in [360,835]],
(152,6):[(x,y,222,125) for y in [44,186,328,470,612] for x in [177,416,656,895]],
(152,7):[(x,y,435,245) for y in [133,403] for x in [138,597]],
(152,8):[(x,y,330,186) for y in [192,403] for x in [65,420,775]],
(160,2):[(x,y,359,202) for y in [66,290,513] for x in [32,406,780]],
(162,2):[(99,56,579,326),(688,56,383,215),(99,392,284,160),(393,392,284,160),(688,282,383,215),(99,563,284,160),(393,563,284,160),(688,509,383,215)],
(165,1):[(x,y,359,202) for y in [126,355,585] for x in [119,506,892]],
(165,10):[(x,y,436,245) for y in [133,403] for x in [138,597]],
(167,2):[(x,y,282,159) for y in [26,200,374,548] for x in [15,314,613,912]],
(174,2):[(x,y,359,202) for y in [67,290,513] for x in [32,405,780]],
(174,4):[(x,y,359,202) for y in [67,290,513] for x in [32,405,780]],
(180,4):[(64,247,508,286),(598,247,508,286)],
(194,3):[(x,y,489,275) for y in [103,403] for x in [86,595]],
}
decks={}
for s in a:
 id=f'p{s["id"]:03d}';im=Image.open(s['sheet']).convert('RGB');decks.setdefault(id,dict(id=id,originalDeck=s['id'],title=s['title'],sourceSize=[1280,720],slides=[]));out=root/'public/reference'/id;out.mkdir(parents=True,exist_ok=True)
 for i,(x,y,w,h) in enumerate(g[(s['id'],s['preview'])],1):
  sid=f's{s["preview"]:02d}-{i:02d}'; tile=Image.new('RGB',(w,h),'white');left=max(x,0);top=max(y,0);right=min(x+w,im.width);bottom=min(y+h,im.height);tile.paste(im.crop((left,top,right,bottom)),(left-x,top-y));tile.save(out/f'{sid}.jpg',quality=98,subsampling=0)
  item=dict(id=sid,reference=f'/reference/{id}/{sid}.jpg',originalPath='sheets/'+Path(s['sheet']).name,sheetSize=[im.width,im.height],crop=[x,y,w,h],nativeSize=[w,h])
  if x<0 or y<0 or x+w>im.width or y+h>im.height:item.update(incomplete=True,visibleCrop=[left,top,right-left,bottom-top],reconstruction='Missing outer region completed from the same deck style; native reference pixels are preserved with white padding.')
  decks[id]['slides'].append(item)
(root/'public/reference/groups').mkdir(parents=True,exist_ok=True)
(root/'public/reference/groups/c.json').write_text(json.dumps(list(decks.values()),indent=2))
print({k:len(v['slides']) for k,v in decks.items()});print('TOTAL',sum(len(v['slides']) for v in decks.values()))

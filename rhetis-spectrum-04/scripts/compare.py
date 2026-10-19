from pathlib import Path
from PIL import Image,ImageDraw
import sys
root=Path(__file__).resolve().parent.parent
deck=sys.argv[1];round=sys.argv[2] if len(sys.argv)>2 else 'final';mode=sys.argv[3] if len(sys.argv)>3 else 'direct'
refs=Path('/workspace/work/rhetis/images/miricanvas_selected_references')
folder=next(refs.glob(deck+'*'));out=root/'comparisons'/mode/round;out.mkdir(parents=True,exist_ok=True)
for f in sorted(folder.glob('*.png')):
 result=root/'renders'/mode/round/(deck+'-'+f.name)
 if not result.exists():continue
 sheet=Image.new('RGB',(2560,752),'#ddd');sheet.paste(Image.open(f).convert('RGB'),(0,32));sheet.paste(Image.open(result).convert('RGB'),(1280,32));d=ImageDraw.Draw(sheet);d.text((12,9),'REFERENCE '+deck+'/'+f.stem,fill='black');d.text((1292,9),'IMPLEMENTATION '+mode,fill='black');sheet.save(out/(deck+'-'+f.stem+'.jpg'),quality=92)
print(out)

"""Create inspectable original / previous delivery / revised delivery comparisons."""
import pathlib
from PIL import Image, ImageDraw
root=pathlib.Path(__file__).resolve().parents[1]
prior=pathlib.Path('/workspace/leaflet-prior/unfolded')
out=pathlib.Path('/workspace/shared/downloads');out.mkdir(parents=True,exist_ok=True)
cases=[('l07','s01'),('l11','s02'),('l17','s02'),('l21','s01'),('l39','s01'),('l52','s01'),('l62','s01'),('l68','s02')]
for batch in range(2):
    sheet=Image.new('RGB',(1952,1632),'#f1f2f4');draw=ImageDraw.Draw(sheet)
    for col,title in enumerate(['ORIGINAL REFERENCE','PREVIOUS DELIVERY','REVISED DELIVERY']):draw.text((col*648+12,12),title,fill='#20242a')
    for row,(brochure,side) in enumerate(cases[batch*4:batch*4+4]):
        y=40+row*396;draw.text((12,y),f'{brochure} / {side}',fill='#20242a')
        source=Image.open(root/'public/reference'/brochure/(side+'.webp')).convert('RGB')
        reference=Image.new('RGB',(1280,720),'#eef0f3');scale=min(1280/source.width,720/source.height)
        resized=source.resize((round(source.width*scale),round(source.height*scale)),Image.Resampling.LANCZOS)
        reference.paste(resized,((1280-resized.width)//2,(720-resized.height)//2))
        previous=Image.open(prior/brochure/(side+'.png')).convert('RGB')
        revised=Image.open(root/'renders/final'/(brochure+'-'+side+'.png')).convert('RGB')
        for col,image in enumerate([reference,previous,revised]):sheet.paste(image.resize((640,360),Image.Resampling.LANCZOS),(col*648+8,y+22))
    sheet.save(out/f'leaflet-before-after-{batch+1}.jpg',quality=95)

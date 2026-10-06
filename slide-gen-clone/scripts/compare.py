import sys,json,pathlib
from PIL import Image,ImageDraw,ImageOps
root=pathlib.Path(__file__).resolve().parents[1]
key=sys.argv[1]
round_name=sys.argv[2] if len(sys.argv)>2 else 'final'
metadata=json.loads((root/'comparisons'/f'{key}.json').read_text())
reference=Image.open(root/'public/reference'/f'{key}.jpg').convert('RGB')
regions=metadata['referenceRegions']
size=(640,360)
sheet=Image.new('RGB',(1304,len(metadata['slides'])*390),'#dfe2e6')
draw=ImageDraw.Draw(sheet)
for i,slide in enumerate(metadata['slides']):
    region=regions[i]
    x,y,w,h=[region[k]/100 for k in ('x','y','w','h')]
    left,top,right,bottom=round(x*reference.width),round(y*reference.height),round((x+w)*reference.width),round((y+h)*reference.height)
    crop=Image.new('RGB',(right-left,bottom-top),'#dfe2e6')
    visible=(max(left,0),max(top,0),min(right,reference.width),min(bottom,reference.height))
    if visible[2]>visible[0] and visible[3]>visible[1]:
        crop.paste(reference.crop(visible),(visible[0]-left,visible[1]-top))
    rendered=Image.open(slide['file']).convert('RGB')
    row_y=i*390
    draw.text((8,row_y+6),f'{key}/{slide["id"]} ORIGINAL (gray outside original = unavailable)',fill='black')
    draw.text((656,row_y+6),f'REVISED: {round_name} (image placeholders intentional)',fill='black')
    sheet.paste(crop.resize(size),(8,row_y+25))
    sheet.paste(rendered.resize(size),(656,row_y+25))
    sheet.crop((0,row_y,1304,row_y+390)).save(root/'comparisons'/round_name/f'{key}-{slide["id"]}.jpg',quality=95)
sheet.save(root/'comparisons'/f'{key}.jpg',quality=94)
sheet.save(root/'comparisons'/round_name/f'{key}.jpg',quality=94)
board=Image.open(metadata['boardFile']).convert('RGB').resize(reference.size)
board_sheet=Image.new('RGB',(reference.width*2+24,reference.height+32),'#dfe2e6')
board_draw=ImageDraw.Draw(board_sheet)
board_draw.text((8,7),f'{key} ORIGINAL BOARD',fill='black')
board_draw.text((reference.width+16,7),f'{key} REVISED BOARD: {round_name}',fill='black')
board_sheet.paste(reference,(8,28));board_sheet.paste(board,(reference.width+16,28))
board_sheet.save(root/'comparisons'/round_name/f'{key}-board.jpg',quality=95)

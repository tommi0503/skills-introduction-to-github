"""Summarize the final browser captures and independently check native crops."""
import json,pathlib
from PIL import Image
root=pathlib.Path(__file__).resolve().parents[1]
manifest=json.loads((root/'public/reference/manifest.json').read_text())
fonts={};outliers=[];count=0
for deck in manifest:
 meta=json.loads((root/'comparisons/final'/f'{deck["id"]}.json').read_text())
 for slide in meta['slides']:
  for font in slide['fontUsage']:
   key=(font['family'],font['weight'])
   item=fonts.setdefault(key,{'family':font['family'],'weight':font['weight'],'actualFaces':set(),'examples':[],
    'loaded':True,'supported':True,'syntheticFontsAllowed':False})
   item['actualFaces'].update(font['actualFaces']);item['loaded']&=font['loadedFaces']>0
   if len(item['examples'])<4:item['examples'].append(f'{deck["id"]}/{slide["id"]}')
  assert not any(f.get('issue') in ['font not loaded','requested font weight/style unavailable'] for f in slide['findings'])
 for slide in deck['slides']:
  capture=next(x for x in meta['slides'] if x['id']==slide['id']);p=pathlib.Path(capture['reference'])
  with Image.open(p) as im:
   assert list(im.size)==slide['nativeSize'],f'Native crop mismatch {deck["id"]}/{slide["id"]}'
   if abs(im.width/im.height-16/9)>.04:outliers.append({'deck':deck['id'],'slide':slide['id'],'nativeSize':list(im.size)})
  count+=1
for item in fonts.values():item['actualFaces']=sorted(item['actualFaces']);assert item['loaded'] and item['actualFaces']
(root/'review/font-request-precheck.json').write_text(json.dumps(list(fonts.values()),ensure_ascii=False,indent=2)+'\n')
assert count==1057 and len(outliers)==1 and outliers[0]['deck']=='p105' and outliers[0]['slide']=='s03-25'
outliers[0]['reason']='원본의 세로형 Timeline 단일 페이지; 1280×720에 비율을 보존하여 중앙 배치'
(root/'review/reference-crop-check.json').write_text(json.dumps({'slides':count,'allNativeSizesMatch':True,'aspectOutliers':outliers},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'nativeCrops':count,'portraitExceptions':len(outliers),'actualFontFamilyWeightCombinations':len(fonts),'allFontsLoaded':True}))

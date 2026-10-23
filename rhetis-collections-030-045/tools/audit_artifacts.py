"""Check that comparisons/PDFs actually contain the final page renders."""
from pathlib import Path
from PIL import Image,ImageChops
from pypdf import PdfReader
import json, hashlib
BASE=Path(__file__).resolve().parents[1]
NAMES={'030':'chalkline','031':'undertow','033':'cutplane','038':'skylight','043':'arrowtab','045':'blockweave'}
def audit():
 report=[]
 for code,name in NAMES.items():
  original=sorted((BASE/'originals'/code).glob('*.png'))
  rv=BASE/'reviews'/(name+'-review');row={'collection':name,'comparisons':[],'pdfs':[],'errors':[]}
  for kind in ['replica','reassembled']:
   renders=sorted((rv/kind).glob('*.png'));comp=sorted((rv/('compare-'+kind)).glob('*.png'));pdf=rv/kind/(kind+'.pdf')
   if len(renders)!=len(original) or len(comp)!=len(original):row['errors'].append(kind+': incomplete pages');continue
   for src,out,compare in zip(original,renders,comp):
    with Image.open(compare) as ci,Image.open(src) as si,Image.open(out) as oi:
     a=ci.convert('RGB');s=si.convert('RGB');o=oi.convert('RGB');left=ImageChops.difference(a.crop((0,0,1280,720)),s).getbbox() is None;right=ImageChops.difference(a.crop((1280,0,2560,720)),o).getbbox() is None
     record={'kind':kind,'page':out.name,'comparison':compare.name,'left_matches_original':left,'right_matches_final_render':right};row['comparisons'].append(record)
     if not left or not right:row['errors'].append(kind+': stale/different comparison '+compare.name)
   if pdf.exists():
    count=len(PdfReader(str(pdf)).pages);newer=pdf.stat().st_mtime>=max(p.stat().st_mtime for p in renders)-1
    row['pdfs'].append({'file':kind+'/'+pdf.name,'pages':count,'expected':len(original),'newer_than_final_renders':newer})
    if count!=len(original) or not newer:row['errors'].append(kind+': stale/wrong page PDF')
   else:row['errors'].append('missing '+str(pdf))
  for mode in ['light','dark']:
   pdf=rv/'library'/('library-'+mode+'.pdf')
   if pdf.exists():row['pdfs'].append({'file':'library/'+pdf.name,'pages':len(PdfReader(str(pdf)).pages)})
   else:row['errors'].append('missing library PDF '+mode)
  report.append(row)
 (BASE/'checks/integration-artifacts-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
 for r in report:print(r['collection'],len(r['comparisons']),'comparisons',r['errors'])
 return report
if __name__=='__main__':audit()

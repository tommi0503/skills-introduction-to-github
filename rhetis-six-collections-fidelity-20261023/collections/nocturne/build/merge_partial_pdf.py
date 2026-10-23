from pathlib import Path
import json,re,hashlib,fitz
B=Path(__file__).resolve().parent.parent;R=B/'review';L=R/'library'
old=json.loads((B/'build/audit-library-before-dots.json').read_text());new=json.loads((R/'audit-library.json').read_text());merged=[x for x in old if x['folder'] not in {'headline','callout'}]+new
assert len(merged)==708
(R/'audit-library.json').write_text(json.dumps(merged,ensure_ascii=False,indent=2))
titles=re.findall(r'<article><h2>(.*?)</h2>',(L/'light.html').read_text());folders=[re.sub('<[^>]+>','',s).split(' / ')[0]for s in titles];indices=[i for i,f in enumerate(folders) if f in {'headline','callout'}];assert len(indices)==13
report=[]
for mode in ['light','dark']:
 base=fitz.open(L/f'library-{mode}.pdf');part=fitz.open(L/f'partial-update-{mode}.pdf');assert len(base)==len(titles)==176;assert len(part)==len(indices)==13
 out=fitz.open();partidx={idx:j for j,idx in enumerate(indices)}
 for i in range(len(base)):
  src=part if i in partidx else base;j=partidx.get(i,i);out.insert_pdf(src,from_page=j,to_page=j)
 temp=B/f'build/library-{mode}-final.pdf';out.save(temp,deflate=True);out.close()
 result=fitz.open(temp)
 for idx,j in partidx.items():
  assert result[idx].get_pixmap(matrix=fitz.Matrix(.25,.25)).digest==part[j].get_pixmap(matrix=fitz.Matrix(.25,.25)).digest
 result.close();base.close();part.close();temp.replace(L/f'library-{mode}.pdf');(L/f'partial-update-{mode}.pdf').unlink();report.append({'mode':mode,'pages':176,'replaced_pages_1based':[x+1 for x in indices],'replacement_raster_hashes_match':True})
(R/'pdf-final-checks.json').write_text(json.dumps(report,indent=2));print(report)

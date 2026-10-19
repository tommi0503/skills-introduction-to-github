from pathlib import Path
import hashlib,json,datetime
P=Path(__file__).resolve().parent.parent
records={}
sets={
 'assembled':['scripts/assemble-library.mjs','src/assembly-data.json','contract/type-steps.json','public/fonts/PretendardVariable.woff2',*[str(p.relative_to(P)) for p in sorted((P/'collection/report-forge').rglob('*.css'))]],
 'library':['scripts/library-review.mjs','contract/type-steps.json',*[str(p.relative_to(P)) for p in sorted((P/'collection/report-forge').rglob('*')) if p.is_file()]],
}
for name,files in sets.items():
 inputs={f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in files}
 htmls=['outputs/assembled.html'] if name=='assembled' else ['outputs/light.html','outputs/dark.html']
 renders=list((P/'renders/assembled').glob('*/*.png')) if name=='assembled' else [*list((P/'renders/library-light').glob('*.png')),*list((P/'renders/library-dark').glob('*.png'))]
 html={f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in htmls}
 css_in_html=all((P/f).read_text().strip() in (P/'outputs/assembled.html').read_text() for f in files if f.endswith('.css')) if name=='assembled' else True
 newestinput=max((P/f).stat().st_mtime for f in files if not f.startswith('scripts/'))
 oldesthtml=min((P/f).stat().st_mtime for f in htmls)
 oldestpng=min(f.stat().st_mtime for f in renders)
 assert css_in_html and newestinput<=oldesthtml<=oldestpng,(name,'stale rendering inputs')
 assert (P/files[0]).stat().st_mtime <= (oldesthtml if name=='assembled' else oldestpng),(name,'script newer than render')
 records[name]={'inputs':inputs,'html':html,'renderCount':len(renders),'latestCSSIncluded':css_in_html,'inputsWrittenBeforeHTMLAndPNG':True}
(P/'review/final-render-inputs.json').write_text(json.dumps({'recordedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sets':records},indent=2)+'\n')
print({k:v['renderCount'] for k,v in records.items()})

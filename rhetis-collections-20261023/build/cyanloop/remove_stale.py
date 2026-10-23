from pathlib import Path
import re,fitz
C=Path('/workspace/output/cyanloop');R=Path('/workspace/output/cyanloop-review');W=Path('/workspace/work/cyanloop')
p=C/'elements/callout/fixtures/source-07-2.html'
assert p.exists()
a=re.findall(r'<article><h2>(.*?)</h2>',(R/'library/light.html').read_text());indices=[i for i,t in enumerate(a) if t.startswith('callout / source-07-2 ')];assert len(indices)==1;idx=indices[0]
p.unlink()
for mode in ['light','dark']:
 for i in range(idx+1,len(a)):(W/f'{mode}-{i:03}.png').replace(W/f'{mode}-{i-1:03}.png')
 f=R/'library'/f'library-{mode}.pdf';d=fitz.open(f);assert len(d)==len(a);d.delete_page(idx);temp=f.with_suffix('.tmp.pdf');d.save(temp,garbage=4,deflate=True,deflate_images=True);d.close();temp.replace(f)
s=(W/'render_final.py').read_text().replace("selected={'pricing','matrix'}", "selected={'callout'}");(W/'render_callout_final.py').write_text(s)
p=W/'source_fixtures.py';s=p.read_text();s=s.replace("ns=runpy.run_path(str(p));P=ns['P']", "for stale in C.glob('elements/*/fixtures/source-*.html'):stale.unlink()\nns=runpy.run_path(str(p));P=ns['P']");p.write_text(s)
print('removed stale duplicate at',idx)

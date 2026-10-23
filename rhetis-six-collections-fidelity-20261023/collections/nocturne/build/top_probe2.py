exec(open('/workspace/work/deliverables/nocturne/build/measure_pages.py').read().split('B=')[0])
B=Path('/workspace/work/deliverables/nocturne');
with sync_playwright() as p:
 b=rr.browser(p);pg=b.new_page(viewport={'width':1280,'height':720});rr.load(pg,B/'review/reassembled/slide_23.html');print(pg.evaluate('''()=>[...document.querySelectorAll('.top,.top *')].map(e=>({el:e.outerHTML,color:getComputedStyle(e).color,opacity:getComputedStyle(e).opacity,visibility:getComputedStyle(e).visibility,z:getComputedStyle(e).zIndex}))'''));pg.evaluate(rr.AUDIT_JS);pg.screenshot(path=str(B/'build/probe-top-after-audit.png'));b.close()

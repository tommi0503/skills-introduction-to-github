"""Inspect actual text runs for cross-component overlap in final browser pages."""
import asyncio, functools, json, threading
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


CHECK = r'''() => {
 const runs=[], issues=[], nodes=document.querySelectorAll('[data-kind="text"],[data-kind="pill"]');
 for(const el of nodes){
   const walker=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);
   let text;
   while(text=walker.nextNode()){
     if(!text.textContent.trim())continue;
     const range=document.createRange();range.selectNodeContents(text);
     for(const r of range.getClientRects()){
       if(r.width<1||r.height<1)continue;
       runs.push({node:el.dataset.node,text:text.textContent,rect:[r.left,r.top,r.right,r.bottom]});
     }
   }
 }
 for(let i=0;i<runs.length;i++)for(let j=i+1;j<runs.length;j++){
   const a=runs[i],b=runs[j];if(a.node===b.node)continue;
   const [al,at,ar,ab]=a.rect,[bl,bt,br,bb]=b.rect;
   const w=Math.min(ar,br)-Math.max(al,bl),h=Math.min(ab,bb)-Math.max(at,bt);
   if(w>3&&h>4&&w*h>Math.min((ar-al)*(ab-at),(br-bl)*(bb-bt))*.28)
     issues.push({type:'text-overlap',a:a.node,b:b.node,aText:a.text,bText:b.text,intersection:[w,h]});
 }
 return {issues,textNodes:nodes.length,fontFaces:Array.from(document.fonts).filter(f=>f.status==='loaded').map(f=>({family:f.family,weight:f.weight}))};
}'''


async def main():
    server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])
        page = await browser.new_page(viewport={'width': 1280, 'height': 720})
        for mode in ['replica', 'assembly']:
            for f in sorted((ROOT / 'build' / mode).glob('*/slide_*.html')):
                await page.goto(f'http://127.0.0.1:{server.server_port}/' + str(f.relative_to(ROOT)))
                await page.wait_for_selector('body[data-ready="true"]')
                result = await page.evaluate(CHECK)
                results.append({'mode': mode, 'deck': f.parent.name, 'slide': f.stem, **result})
        await browser.close()
    server.shutdown()
    report = {'pages': results, 'findings': sum(len(r['issues']) for r in results)}
    (ROOT / 'review/text-overlap-audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps({'pages': len(results), 'findings': report['findings']}))


if __name__ == '__main__':
    asyncio.run(main())

"""Print every official fixture at full resolution using the actual host fonts."""
import asyncio, functools, json, threading
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import fitz
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


async def main():
    server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    report = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])
        page = await browser.new_page(viewport={'width': 1280, 'height': 720})
        for mode in ['light', 'dark']:
            await page.goto(f'http://127.0.0.1:{server.server_port}/build/library/{mode}.html')
            await page.add_style_tag(content='''
              @page{size:1280px 720px;margin:0}
              html,body{margin:0;padding:0;display:block;background:white}
              article{margin:0;width:1280px;height:720px;break-after:page;overflow:hidden}
              article:last-child{break-after:auto}
              h2{display:none}
              article>.frame{width:1280px;height:720px;border-radius:0;overflow:hidden}
              article>.frame>.slide{transform:none;width:1280px;height:720px}
              *{print-color-adjust:exact;-webkit-print-color-adjust:exact}
            ''')
            await page.evaluate('document.fonts.ready')
            expected = await page.locator('article').count()
            raw = await page.pdf(width='1280px', height='720px', print_background=True, prefer_css_page_size=True)
            src = fitz.open(stream=raw, filetype='pdf')
            doc = fitz.open()
            for i in range(len(src)):
                pg = doc.new_page(width=1280, height=720)
                pg.show_pdf_page(pg.rect, src, i)
            if len(doc) != expected:
                raise RuntimeError(f'{mode}: unexpected PDF pages {len(doc)} != {expected}')
            dest = ROOT / 'pdfs' / f'library-{mode}.pdf'
            doc.save(dest)
            report.append({'mode': mode, 'pages': len(doc), 'size': [1280, 720]})
            doc.close()
            src.close()
        await browser.close()
    server.shutdown()
    (ROOT / 'review/library-pdf-verification.json').write_text(json.dumps(report, indent=2))
    print(json.dumps(report))


if __name__ == '__main__':
    asyncio.run(main())

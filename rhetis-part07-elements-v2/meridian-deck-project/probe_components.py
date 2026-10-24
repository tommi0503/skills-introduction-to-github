from pathlib import Path
import importlib.util,json
from playwright.sync_api import sync_playwright
P=Path(__file__).parent
s=importlib.util.spec_from_file_location('ss','/workspace/work/rhetis-elements-v2/tools/sheets.py');ss=importlib.util.module_from_spec(s);s.loader.exec_module(ss)
css=ss.style(P,'meridian-deck');f=P/'sheet-runtime/probe.html';fixture=(P/'meridian-deck/elements/card/fixtures/replica-16.html').read_text()
f.write_text('<html><meta charset="utf-8"><link rel="stylesheet" href="../assets/fonts/fonts.css"><style>html,body{margin:0}'+css+'</style><body><section class="slide"><div class="page"><div class="body">'+fixture+'</div></div></section></body></html>')
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);p=b.new_page(viewport={'width':1280,'height':720});p.goto('http://127.0.0.1:8875/meridian-deck-project/sheet-runtime/probe.html');p.evaluate('document.fonts.ready');print(p.locator('[data-el="meridian-deck-card"]').first.evaluate('e=>[e,...e.querySelectorAll(".parts,.name,.note")].map(x=>{let s=getComputedStyle(x),r=x.getBoundingClientRect();return [x.className,[r.x,r.y,r.width,r.height],s.top,s.bottom,s.position,s.width,s.height]})'));b.close()

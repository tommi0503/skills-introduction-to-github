from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,json,time
R=Path('/workspace/work/rebuild');icons=set()
for f in R.glob('*/review/reassembled/*.html'):icons.update(re.findall(r'data-icon="([^"]+)',f.read_text()))
def get(n):
 for attempt in range(3):
  try:
   svg=urlopen('https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/'+n+'.svg',timeout=20).read().decode();break
  except Exception:
   if attempt==2:raise
   time.sleep(attempt+1)
 s=BeautifulSoup(svg,'xml');root=s.svg
 assert root and not s.find(['script','foreignObject','image'])
 root.attrs.pop('class',None);root['aria-hidden']='true';root['width']='100%';root['height']='100%';return n,str(root)
cache=R/'lucide-icons.json';data=json.loads(cache.read_text())if cache.exists()else{}
with ThreadPoolExecutor(max_workers=3)as ex:data.update(dict(ex.map(get,sorted(icons-set(data)))))
(R/'lucide-icons.json').write_text(json.dumps(data))
js='const icons='+json.dumps(data)+';document.querySelectorAll("[data-icon]").forEach(e=>{const s=icons[e.dataset.icon];if(s)e.innerHTML=s});'
for d in R.iterdir():
 if (d/'review/assets').exists():(d/'review/assets/lucide.js').write_text(js)
print(len(data),'official SVG icons stored; no CSS or per-page rules')

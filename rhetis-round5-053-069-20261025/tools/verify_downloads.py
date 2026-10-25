"""Independently download and verify the published ZIP bytes."""
import argparse,concurrent.futures,hashlib,io,json,posixpath,subprocess,time,zipfile
from collections import Counter
from pathlib import Path
from PIL import Image
from lxml import html
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--commit',required=True);p.add_argument('--destination',default='/tmp/rhetis-elements-published-downloads');a=p.parse_args();target=Path(a.destination);target.mkdir(parents=True,exist_ok=True)
 artifacts=json.loads((ROOT/'artifacts.json').read_text());base='https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/'+a.commit+'/'+ROOT.name+'/'
 def download(item):
  out=target/item['name'];url=item.get('url',base+item['name']);subprocess.run(['curl','--fail','--location','--silent','--show-error','--retry','2',url,'--output',str(out)],check=True)
  assert hashlib.sha256(out.read_bytes()).hexdigest()==item['sha256'],(out.name,'SHA mismatch')
  assert out.stat().st_size==item['bytes'],(out.name,'byte-count mismatch')
  return item,out,url
 with concurrent.futures.ThreadPoolExecutor(max_workers=3)as pool:downloads=list(pool.map(download,artifacts))
 rows=[]
 for item,out,url in downloads:
  dims=Counter();pngs=0;links=0
  with zipfile.ZipFile(out)as z:
   assert z.testzip()is None,(out.name,'CRC');names=set(z.namelist())
   if not out.name.endswith('-review.zip'):
    assert {n.split('/')[0]for n in names}=={out.stem}
    assert all(Path(n).suffix in ['.css','.json','.md','.html']for n in names)
   for name in names:
    assert not name.startswith('/')and'..'not in Path(name).parts
    if name.endswith('.png'):
     with Image.open(io.BytesIO(z.read(name)))as im:
      dims[f'{im.width}x{im.height}']+=1;pngs+=1
      if name.startswith('reassembled/'):assert im.size==(1280,720),(out.name,name,im.size)
      if name.startswith('compare-reassembled/'):assert im.size==(3840,720),(out.name,name,im.size)
      im.verify()
    if name.startswith('reassembled/')and name.endswith('.html'):
     for link in html.fromstring(z.read(name)).xpath('//link/@href|//script/@src'):
      if link.startswith(('http:','https:','data:')):continue
      resolved=posixpath.normpath(posixpath.join(posixpath.dirname(name),link.split('?')[0]));assert resolved in names,(out.name,name,link);links+=1
  rows.append({'name':out.name,'url':url,'bytes':item['bytes'],'sha256':item['sha256'],'crc':'pass','pngs':pngs,'dimensions':dict(dims),'portableReassembledDependenciesChecked':links});print(out.name,'CRC/SHA/PNG/relative dependencies PASS',flush=True)
 report={'commit':a.commit,'downloadedUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'method':'Actual HTTPS downloads from an immutable GitHub commit; SHA-256, byte count, ZIP CRC, intake root/extensions, PNG headers/CRC and review HTML CSS/font/script closure.','files':rows}
 (ROOT/'download-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('Downloaded and verified',len(rows),'ZIPs',sum(r['pngs']for r in rows),'PNGs')
if __name__=='__main__':main()

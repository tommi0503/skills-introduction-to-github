"""Prepare readable root-review overviews and remember their exact PNG provenance."""
from pathlib import Path
import sys,json,hashlib,time
from PIL import Image
from sheets import ROOT
Image.MAX_IMAGE_PIXELS=None
k=sys.argv[1];p=ROOT/(k+'-project');out=Path('/tmp/rhetis-root-view')/k;out.mkdir(parents=True,exist_ok=True)
mf=out/'manifest.json';manifest=json.loads(mf.read_text()) if mf.exists() else {}
for leaf in sys.argv[2:]:
 ims=[]
 for mo in ['light','dark']:
  f=p/'sheets'/(leaf+'-'+mo+'.png');raw=f.read_bytes();manifest[str(f.relative_to(ROOT))]=hashlib.sha256(raw).hexdigest()
  im=Image.open(f).convert('RGB');im.thumbnail((1700,1250));ims.append(im)
 result=Image.new('RGB',(max(i.width for i in ims),sum(i.height for i in ims)));y=0
 for im in ims:result.paste(im,(0,y));y+=im.height
 result.save(out/(leaf+'.png'))
mf.write_text(json.dumps(manifest,indent=2));print(out)

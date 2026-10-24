"""Rebuild the standard contract previews with portable font links and input hashes."""
import hashlib,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inputs(cid):
 C=ROOT/cid
 paths=[ROOT/'tools/preview.py',ROOT/'tools/make_previews.py',ROOT/'contract/palette.json',ROOT/'contract/type-steps.json',ROOT/'fonts/fonts.css']
 paths +=sorted(p for p in C.rglob('*')if p.is_file()and p.suffix in ['.css','.json','.html'])
 return{str(p.relative_to(ROOT)):sha(p)for p in paths}
def main():
 for item in json.loads((ROOT/'collections.json').read_text()):
  cid=item['id'];R=ROOT/(cid+'-review');before=inputs(cid);outputs={}
  for mode in ['light','dark']:
   out=R/('preview-'+mode+'.html');cmd=['python',str(ROOT/'tools/preview.py'),str(ROOT/cid),str(ROOT/'contract/type-steps.json'),'--out',str(out),'--fonts',str(ROOT/'fonts/fonts.css')]
   if mode=='dark':cmd.append('--dark')
   subprocess.run(cmd,check=True,stdout=subprocess.DEVNULL)
   text=out.read_text();text=re.sub(r'href="file:[^"]*fonts/fonts\.css"','href="../fonts/fonts.css"',text);out.write_text(text)
   assert 'file:'not in text,'Nonportable preview URI';outputs[out.name]=sha(out)
  assert before==inputs(cid),'Preview inputs changed during build'
  (R/'preview-audit.json').write_text(json.dumps({'inputs':before,'outputs':outputs},ensure_ascii=False,indent=2))
  print(cid,'previews current',flush=True)
if __name__=='__main__':main()

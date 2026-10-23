"""Catch rules that Chromium silently drops, including invalid nested :has()."""
from pathlib import Path
import argparse,json,sys
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(Path(__file__).parent))
from render_review import browser

def headers(css):
 buf='';quote=None;escape=False;comment=False;i=0
 while i<len(css):
  c=css[i];n=css[i:i+2]
  if comment:
   if n=='*/':comment=False;i+=2;continue
   i+=1;continue
  if quote:
   buf+=c
   if escape:escape=False
   elif c=='\\':escape=True
   elif c==quote:quote=None
   i+=1;continue
  if n=='/*':comment=True;i+=2;continue
  if c in ['"',"'"]:quote=c;buf+=c
  elif c=='{':
   h=buf.strip();buf=''
   if h:yield h
  elif c in ['}',';']:buf=''
  else:buf+=c
  i+=1

def main():
 a=argparse.ArgumentParser();a.add_argument('collection');a.add_argument('--out',required=True);arg=a.parse_args()
 root=Path(arg.collection);items=[]
 for p in sorted(root.rglob('*.css')):
  for h in headers(p.read_text()):
   if not h.startswith('@'):items.append({'file':str(p.relative_to(root)),'selector':h})
 with sync_playwright() as p:
  b=browser(p);page=b.new_page();valid=page.evaluate('(sels)=>sels.map(s=>{try{let sheet=new CSSStyleSheet();sheet.insertRule(s+"{--syntax-audit:1}");return sheet.cssRules.length===1}catch(e){return false}})',[x['selector'] for x in items]);b.close()
 failures=[x for x,v in zip(items,valid) if not v]
 result={'collection':root.name,'selectors':len(items),'invalidSelectors':failures};Path(arg.out).write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()

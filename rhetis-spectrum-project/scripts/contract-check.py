from pathlib import Path
from html.parser import HTMLParser
import json,re
root=Path('collection/rhetis-spectrum'); tax=json.loads(Path('contract/taxonomy.json').read_text()); shared=json.loads(Path('contract/kit-tokens.json').read_text())['tokens']; steps=set(json.loads(Path('contract/type-steps.json').read_text()));issues=[]; counts={}
class Fragment(HTMLParser):
 def __init__(self): super().__init__();self.depth=0;self.roots=0;self.classes=[];self.roots_data=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if self.depth==0:self.roots+=1;self.roots_data.append(a)
  if 'class' in a:self.classes.extend(a['class'].split())
  if tag not in ['br','hr','img','input','meta','link','wbr']:self.depth+=1
 def handle_endtag(self,tag):self.depth-=1
kit=json.loads((root/'kit/kit.json').read_text());assert kit['schema']=='rhetis.kit/2' and kit['id']==root.name
css=(root/'kit'/kit['tokens']).read_text();blocks=re.findall(r'\.slide(?:\.dark)?\s*\{([^}]+)',css)
for key,kind in shared.items():
 if not re.search(re.escape(key)+r'\s*:',blocks[0]):issues.append('missing token '+key)
 if kind=='color' and (len(blocks)<2 or not re.search(re.escape(key)+r'\s*:',blocks[1])):issues.append('missing dark token '+key)
for c in tax['contracts']:
 folder=c['category'].split('.')[-1];d=root/'elements'/folder;meta=json.loads((d/'element.json').read_text());assert meta['schema']=='rhetis.design-library-element-source/1' and meta['contract']==c['id'];content=(d/'element.css').read_text();fs=sorted((d/'fixtures').glob('*.html'));counts[folder]=len(fs)
 if len(fs)<2:issues.append(folder+' needs 2 fixtures')
 if '@container' not in content:issues.append(folder+' missing container rules')
 if re.search(r'@(import|font-face|keyframes|property)\b|url\(',content):issues.append(folder+' forbidden at-rule/resource')
 if re.search(r'#[a-fA-F0-9]{3,8}\b|(?:rgb|hsl)a?\(',content):issues.append(folder+' color literal')
 if re.search(r'font-size\s*:\s*(?!var\(--type-)[^;]+',content):issues.append(folder+' font size not type token')
 for n in re.findall(r'--type-(\d+)',content):
  if int(n) not in steps:issues.append(folder+' invalid type step '+n)
 if re.search(r'font-weight\s*:\s*\d',content):issues.append(folder+' literal weight')
 for f in fs:
  txt=f.read_text();p=Fragment();p.feed(re.sub(r'<!--.*?-->','',txt,flags=re.S))
  if p.roots!=1:issues.append(str(f)+' root count '+str(p.roots))
  if not re.match(r'<!-- min: [^>]+ -->\n',txt):issues.append(str(f)+' missing min declaration')
  if not re.search(r'data-el="'+root.name+'-'+folder+'"',txt):issues.append(str(f)+' missing data-el')
report={'status':'passed' if not issues else 'failed','collection':root.name,'elements':len(counts),'elementFixtures':sum(counts.values()),'fixtureCounts':counts,'issues':issues};Path('review/contract-check.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));assert not issues

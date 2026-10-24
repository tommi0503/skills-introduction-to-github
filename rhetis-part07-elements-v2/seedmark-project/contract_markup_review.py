"""Current-v2 contract corrections; no source replica is ever modified."""
from pathlib import Path
from lxml import html,etree
import re
P=Path(__file__).parent

def normalize_markup(s):
 root=html.fragment_fromstring(s,create_parent='audit-fragment')
 for e in list(root.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," list ")]')):
  items=e.xpath('./*[contains(concat(" ",normalize-space(@class)," ")," item ")]')
  par=e.getparent();classes=(par.get('class','')if par is not None else'').split()
  if len(items)==1 and ('parts'in classes or'person'in classes):
   item=items[0];name=item.xpath('./*[contains(concat(" ",normalize-space(@class)," ")," name ")]')[0]
   t=''.join(name.itertext()).strip();note=etree.Element('p',{'class':'note'})
   icon=etree.SubElement(note,'span',{'class':'icon','data-icon':'check'if'check'in e.get('class','').split()else'dot'});icon.tail=t
   more=item.xpath('./*[contains(concat(" ",normalize-space(@class)," ")," note ")]')
   if more and ''.join(more[0].itertext()).strip():icon.tail+=' '+''.join(more[0].itertext()).strip()
   par.replace(e,note);continue
  if 'plan'in classes and 'check'not in e.get('class','').split():e.set('class',e.get('class','')+' check')
  if e.tag=='ul':
   new=etree.Element('div',{'class':e.get('class'),'data-el':'seedmark-list'})
   for li in e:
    item=etree.SubElement(new,'div',{'class':'item'});name=etree.SubElement(item,'p',{'class':'name'});name.text=''.join(li.itertext()).strip();etree.SubElement(item,'p',{'class':'note'})
   par.replace(e,new)
 for tag in root.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," tag ")]'):
  if tag.get('data-el')is None:tag.set('data-el','seedmark-tag')
 for grid in root.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," grid9 ")]'):
  for cl,labels in [('axis-x',['작음','중간','큼']),('axis-y',['낮음','보통','높음'])]:
   if not grid.xpath('./*[contains(concat(" ",normalize-space(@class)," ")," '+cl+' ")]'):
    a=etree.Element('div',{'class':cl})
    for t in labels:etree.SubElement(a,'span').text=t
    grid.insert(0,a)
 for e in root.xpath('.//*[@style]'):
  styles=[]
  for decl in e.get('style').split(';'):
   if not decl.strip():continue
   k=decl.partition(':')[0].strip()
   if k in ['justify-content','gap','font-size','line-height']:continue
   styles.append(decl.strip())
  if styles:e.set('style',';'.join(styles))
  else:e.attrib.pop('style',None)
 return ''.join(html.tostring(e,encoding='unicode',method='html')for e in root)

def fix_collection():
 for f in(P/'seedmark').glob('**/fixtures/*.html'):
  golden={'card':{'card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone'},'callout':{'callout','callout-icon','callout-stack'},'chart-area':{'area-1','areas-2','areas-stacked-3','area-3pt'},'chart-bar':{'bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2'},'chart-donut':{'donut','donuts-3','donuts-4','donut-0','donut-100'},'chart-line':{'lines-12','lines-6','lines-3','lines-flat'}}
  if f.stem in golden.get(f.parent.parent.name,set()):continue
  s=f.read_text();comment=re.match(r'\s*<!--.*?-->\s*',s,re.S);head=comment.group(0)if comment else'';body=s[len(head):];updated=head+normalize_markup(body)+'\n'
  # Only files whose semantics or forbidden markup actually need repair are rewritten.
  need=bool(re.search(r'<ul\b[^>]*class="list|<(?:span|div)\b[^>]*class="tag"(?![^>]*data-el)|justify-content:|gap:var|font-size:var|line-height:1\.8',body))
  e=html.fragment_fromstring(body,create_parent='audit-fragment')
  for q in e.xpath('.//*[@data-el="seedmark-list"]'):
   if len(q.xpath('./*[contains(concat(" ",normalize-space(@class)," ")," item ")]'))==1:need=True
  if 'grid9'in body and 'axis-x'not in body:need=True
  if f.parent.parent.name=='pricing'and 'list check'not in body:need=True
  first=next(q for q in e if isinstance(q.tag,str))
  sty=first.get('style','')
  if not re.search(r'grid-column\s*:\s*1\s*/\s*span\s*12',sty)or not re.search(r'grid-row\s*:\s*1\s*/\s*span\s*6',sty):need=True
  if need:
   wrap=html.fragment_fromstring(updated,create_parent='audit-fragment')
   first=next(e for e in wrap if isinstance(e.tag,str));sty=first.get('style','');sty=re.sub(r'grid-column\s*:[^;]+','grid-column:1 / span 12',sty);sty=re.sub(r'grid-row\s*:[^;]+','grid-row:1 / span 6',sty);first.set('style',sty)
   body=''.join(html.tostring(e,encoding='unicode',method='html')for e in wrap if isinstance(e.tag,str));f.write_text(head+body+'\n')
if __name__=='__main__':fix_collection()

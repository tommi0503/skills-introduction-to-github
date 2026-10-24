from pathlib import Path
from lxml import html
import json,re
P=Path(__file__).parent;K=P/'vectorbox'
p=P/'write_elements_v2.py';s=p.read_text();start=s.index("common='''");end=s.index("\nstyles={}",start);part=s[start:end]
for cls in ['name','note','kick','fig']:
 part=part.replace('R .'+cls+'{','R :where(.'+cls+'){').replace('R .'+cls+' small{','R :where(.'+cls+') small{')
s=s[:start]+part+s[end:]
s=s.replace('R.on{background:var(--a1);color:var(--a1-on)}R.on b{color:inherit}','')
s=s.replace('R.on{background:var(--a1);color:var(--a1-on)}R.quiet{background:none;color:var(--n-8);border-color:var(--n-3)}R.line{background:none}','')
p.write_text(s)
p=P/'write_more_v2.py';s=p.read_text();s=s.replace('padding:var(--gap-sm) var(--gap-sm) calc(2*var(--gap))','padding:calc(var(--gap-sm)/2) var(--gap-sm) var(--gap)')
s=s.replace('bottom:var(--gap-sm);height:16px','bottom:calc(var(--gap-sm)/2);height:8px')
s=s.replace('font-size:clamp(var(--type-16),4cqw,var(--type-26))','font-size:clamp(var(--type-14),min(4cqw,60cqh),var(--type-26))')
s=s.replace('font-size:clamp(var(--type-24),7cqw,var(--type-48))','font-size:clamp(var(--type-20),min(7cqw,70cqh),var(--type-48))')
# Own names do not override a nested independent list's parts.
a=s.index("S['pricing']=");b=s.index("S['code']=",a);q=s[a:b];q=q.replace('R .name{','R.plan>.name,R>.plan>.name{').replace('R.on .name,R .plan.on .name','R.on>.name,R>.plan.on>.name');s=s[:a]+q+s[b:]
a=s.index("S['matrix']=");b=s.index("S['venn']=",a);q=s[a:b];q=q.replace('R .name{','R>.cell>.name{').replace('R .note{','R>.cell>.note{').replace('R>.cell.on .note','R>.cell.on>.note').replace('background:var(--a1);color:var(--a1-on);border-color:var(--a1)','background:var(--a1-1-soft);color:var(--ink);border-color:var(--a1)');s=s[:a]+q+s[b:]
p.write_text(s)
for leaf in ['matrix','pricing','versus']:
 for f in (K/'elements'/leaf/'fixtures').glob('base-*.html'):
  text=f.read_text();root=html.fragment_fromstring(text,create_parent='fragment')
  for ul in root.xpath('.//ul[contains(concat(" ",@class," ")," list ")]'):
   ul.tag='div';ul.set('data-el','vectorbox-list')
   if leaf=='pricing':ul.set('class','list check')
   for li in list(ul):
    li.tag='div';li.set('class','item');t=li.text_content();li.clear();li.set('class','item');name=html.Element('b',{'class':'name'});name.text=t;li.append(name)
  for tag in root.xpath('.//*[contains(concat(" ",@class," ")," tag ")]'):
   tag.set('data-el','vectorbox-tag');tag.set('class','tag');plan=tag.getparent();name=plan.xpath('.//*[contains(concat(" ",@class," ")," name ")]')[0];plan.remove(tag);name.append(tag)
  f.write_text('<!-- min: '+re.search(r'min:\s*([\dx]+)',text)[1]+' -->\n'+''.join(html.tostring(x,encoding='unicode') for x in root if isinstance(x.tag,str)))
for f in (K/'elements/tag/fixtures').glob('base-*.html'):
 s=f.read_text();s=re.sub('class="tag (?:on|quiet|line)"','class="tag"',s).replace('class="tag hl"','class="hl"');f.write_text(s)
f=K/'elements/matrix-nine/fixtures/base-short.html';s=f.read_text();s=s.replace('\n</div>','\n<div class="axis-x"><span>미착수</span><span>검증 중</span><span>완료</span></div><div class="axis-y"><span>본부</span><span>권역</span><span>매장</span></div>\n</div>');f.write_text(s)
f=K/'kit/kit.json';d=json.loads(f.read_text());d['tokens']='tokens.css';d['description']='description.md';d['extensions']={k:{'font-weight':'weight','line-height':'number','letter-spacing':'tracking'}.get(v,v) for k,v in d['extensions'].items()};f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (P/'review-notes.md').open('a') as f:f.write('\n보조 note 해석: taxonomy는 멤버 수와 root/부품 이름을 명시하지만 requiredParts로 보조 note를 별도 강제하지 않는다. 원본에 번호·제목만 있는 목차와 이름만 있는 목록은 보조 note를 생략한다. 원문에 없는 설명을 만들어 조립본에 넣지 않았다. 중첩 list와 tag는 독립 data-el 및 정식 item/name 마크업으로 분리했다. hl은 tag 변형이 아닌 독립 계약 root로 작성했다.\n')
print('Own project contract corrections complete')

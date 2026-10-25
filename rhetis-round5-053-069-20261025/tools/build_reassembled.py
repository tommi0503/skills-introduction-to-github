"""Assemble the frozen map through contract markup and the collection grid only.

There is deliberately no page CSS. Positions are a deterministic projection of
the measured source boxes onto the foundation's twelve by six grid. All deltas,
unrepresentable objects, and nested-element suppressions remain inspectable.
"""
import argparse, copy, html as H, json, re
from pathlib import Path
from lxml import html,etree

ROOT=Path(__file__).resolve().parents[1]
FURN=set('head center kicker title lead icon top rail foot idx deck sec src no label on seat avatar portrait logo back lockup at-center at-left at-bottom-left at-top-left meta deco'.split())

def cls(e,name):return name in e.get('class','').split()
def find(t,name):return next((e for e in t.iter() if cls(e,name)),None)
def text(e):return ''.join(e.itertext()).strip() if e is not None else ''
def inner(e):return H.escape(e.text or '')+''.join(html.tostring(x,encoding='unicode') for x in e) if e is not None else ''
def safe_inline(e):
    if e is None:return ''
    e=copy.deepcopy(e)
    for n in list(e.iter()):
        if n.tag in ('script','style'):n.drop_tree();continue
        if n.tag=='svg':n.drop_tree();continue
        for a in list(n.attrib):
            if a not in ('class','data-ph','data-icon'):del n.attrib[a]
        if 'class' in n.attrib:
            keep=[('sec'if c=='accent'else c) for c in n.get('class').split() if c in FURN or c=='accent']
            if keep:n.set('class',' '.join(keep))
            else:del n.attrib['class']
    return html.tostring(e,encoding='unicode',with_tail=False)

def inline_content(e):
    s=safe_inline(e)
    if not s:return ''
    n=html.fragment_fromstring(s)
    # Foundation text parts require phrasing content; a nested div closes p.meta in HTML.
    for child in n.iterdescendants():
        if child.tag in ('div','p','section'):child.tag='span'
    return inner(n)

def tag(name,classes,content):return f'<{name} class="{classes}">{content}</{name}>'
def p(classes,content):return tag('p',classes,content)

def numeric_style(e):
    return {k.strip():v.strip() for k,v in re.findall(r'([\w-]+)\s*:\s*([^;]+)',e.get('style',''))}

def furniture_svg(shapes):
    return '<svg class="deco" viewBox="0 0 1280 720" aria-hidden="true">'+''.join(shapes)+'</svg>'

def scan_decoration(t):
    shapes=[]
    for e in t.iter():
        if not cls(e,'scan'):continue
        props=numeric_style(e)
        def val(k,default=0):
            v=props.get(k,str(default)).removesuffix('px')
            try:return float(v)
            except ValueError:return default
        w=val('width');h=val('height');x=val('left',1280-val('right')-w);y=val('top',720-val('bottom')-h)
        poly=re.search(r'polygon\((.*?)\)',props.get('clip-path',''))
        if poly:
            pts=[]
            for pair in poly[1].split(','):
                a,b=pair.strip().split();a=float(a.removesuffix('%'));b=float(b.removesuffix('%'));pts.append(f'{x+a*w/100:.3f},{y+b*h/100:.3f}')
            shapes.append('<polygon points="'+' '.join(pts)+'" fill="var(--n-2)"/>')
        else:shapes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="var(--n-2)"/>')
    if find(t,'ribbon') is not None:
        shapes.append('<defs><linearGradient id="footer-ribbon"><stop stop-color="var(--a1-7)"/><stop offset="1" stop-color="var(--a1-2)"/></linearGradient></defs><polygon points="0,646 44.8,694.1 57.6,701.5 1280,701.5 1280,720 0,720" fill="url(#footer-ribbon)"/>')
    return furniture_svg(shapes)

def cinder_decoration(t):
    shapes=[]
    for e in t.iter():
        props=numeric_style(e)
        if 'border-radius' not in props or '999' not in props['border-radius'] or 'height'not in props:continue
        if not props['height'].endswith('px'):continue
        try:x=float(props.get('left','0px')[:-2]);y=float(props.get('top','0px')[:-2]);w=float(props.get('width','0px')[:-2]);h=float(props['height'][:-2])
        except ValueError:continue
        if h<290 or w>150:continue
        color='--a1-7' if props.get('background')=='#fe3810'else('--n-2'if cls(e,'seat')else'--n-7')
        shapes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w/2}" fill="var({color})"/>')
    return furniture_svg(shapes)

def furniture(cid,nn,t,instances):
    """Only named foundation parts. Source SVG is permitted for page decoration."""
    cover=any(x.get('source',{}).get('cover') for x in instances if x['use']=='furniture')
    out=[];slide='slide'+(' cover' if cover else '')
    if not cover and any(x.get('source',{}).get('emphasis')for x in instances if x['use']=='background'):slide+=' on'
    if cid in ('current-fold','halo-field'):
        original=find(t,'slide')
        if original is not None and cls(original,'on'):slide+=' on'
        names=('rail','lockup','meta','top') if cover else ('rail','top','head','foot')
        for name in names:
            e=find(t,name)
            if e is not None:
                markup=safe_inline(e)
                if cid=='current-fold':
                    placements=[x.get('source',{}).get('placement')for x in instances if x.get('use')=='furniture']
                    if name=='head':
                        variant=next((v for v in placements if v in ('at-right','quiet')),None)
                        if variant:markup=markup.replace('class="head"','class="head '+variant+'"',1)
                    elif name=='rail'and 'right'in placements:markup=markup.replace('class="rail"','class="rail right"',1)
                out.append(markup)
        if cover:
            page_node=find(t,'page')
            if page_node is not None:
                for e in page_node:
                    if cls(e,'lead'):out.append(safe_inline(e))
        d=find(t,'deco')
        if d is not None:
            if d.tag=='svg':
                d=copy.deepcopy(d)
                for a in list(d.attrib):
                    if a not in ('viewbox','viewBox','class'):del d.attrib[a]
                s=html.tostring(d,encoding='unicode',with_tail=False).replace('viewbox=','viewBox=')
                out.append(s)
            else:out.append('<div class="deco"></div>')
    elif cid=='rise-block':
        logo=find(t,'logo')
        if cover:
            out.append(tag('div','top',p('deck',H.escape(text(logo)))))
            out.append(tag('div','lockup at-left',p('kicker',H.escape(text(find(t,'sub'))))+tag('h1','title',H.escape(text(next(iter(t.xpath('//h1')),None))))))
            labels=[]
            contact=find(t,'contact')
            if contact is not None:
                for row in contact:labels.append(tag('span','label',inline_content(row)))
            shapes=[];mosaic=find(t,'mosaic')
            if mosaic is not None:
                for e in mosaic:
                    s=numeric_style(e);numbers={k:float(s.get(k,'0px').removesuffix('px'))for k in ['left','top','width','height']}
                    fill='--a1-7'if s.get('background')=='#1731e3'else('--page'if s.get('background')=='#ffffff'else'--n-2')
                    shapes.append(f'<rect x="{numbers["left"]+654}" y="{numbers["top"]}" width="{numbers["width"]}" height="{numbers["height"]}" fill="var({fill})"/>')
            out.extend([tag('div','meta',''.join(labels)),furniture_svg(shapes)])
        else:
            top=find(t,'top');b=next(iter(top.xpath('./b')),None);h=next(iter(top.xpath('./h1')),None)
            out.append(tag('div','top',tag('span','idx',H.escape(text(b)))+tag('span','label',H.escape(text(h)))+tag('span','deck',H.escape(text(logo)))))
            heading=find(t,'heading');v=inline_content(heading).replace('<em>','<b>').replace('</em>','</b>')
            out.append(tag('header','head',tag('h1','title',v)))
    elif cid=='corner-signal':
        if cover:
            out.append(tag('div','top',p('deck','MIRI COMPANY')))
            out.append(tag('div','lockup at-top-left',tag('h1','title','MIRICOMPANY<br><b>IR DECK.</b>')+p('lead','빠른 투자 유치를 위한 핵심 문서')))
            out.append(p('meta','경영 기획팀 | 김미리 팀장<br>Contact us | miri@miricompany.com'))
            # The picture is an image-frame instance, if present in the map.
            if not any(x.get('leaf')=='image-frame' for x in instances):out.append('<div class="seat back" data-ph=""></div>')
        else:
            heads=[x for x in instances if x['use']=='furniture' and '상단' in x.get('design','')]
            title=next((x for x in heads if x['bbox'][3]>48),heads[0] if heads else None)
            lead=next((x for x in heads if x is not title),None)
            titletext=H.escape(title.get('text','')) if title else ''
            actual_h1=next(iter(t.xpath('//main/h1')),None)
            if actual_h1 is not None:titletext=inline_content(actual_h1)
            # Recover split-color tspans as semantic emphasis, rather than a color literal.
            svgtexts=t.xpath('//svg/text')
            if svgtexts:
                target=next((e for e in svgtexts if abs(float(e.get('font-size','0'))-56)<1),None)
                if target is not None:
                    parts=[]
                    if target.text:parts.append(H.escape(target.text))
                    for c in target:
                        s=H.escape(text(c));parts.append('<b>'+s+'</b>' if c.get('fill') and c.get('fill') not in ('#343434','#000','#000000') else s)
                        if c.tail:parts.append(H.escape(c.tail))
                    titletext='<span class="label">'+''.join(parts)+'</span>'
            out.append(tag('header','head',tag('h1','title',titletext)+(p('lead',H.escape(lead.get('text','')).replace('\n','<br>'))if lead else'')))
            feet=[x for x in instances if x['use']=='furniture' and '하단' in x.get('design','')]
            actual_footer=find(t,'footer')
            if actual_footer is not None:
                out.append(tag('div','foot',''.join(tag('span','deck' if i==0 else 'no',H.escape(text(e)))for i,e in enumerate(actual_footer))))
            elif feet:out.append(tag('div','foot',''.join(tag('span','deck' if i==0 else 'no',H.escape(x.get('text','')))for i,x in enumerate(feet))))
            outlines=[]
            for poly in t.xpath('//svg/polygon[@fill="none"]'):
                outlines.append('<polygon points="'+H.escape(poly.get('points',''))+'" fill="none" stroke="var(--n-3)" stroke-width="1"/>')
            if outlines:out.append(furniture_svg(outlines))
            for signature in instances:
                if signature.get('source',{}).get('furniturePart')=='brand-signature':
                    out.append(tag('div','top',tag('span','deck','MIRI COMPANY')))
    elif cid=='anchor-frame':
        out.append(tag('div','lockup at-left',p('kicker',inline_content(find(t,'kicker')))+tag('h1','title',inline_content(find(t,'headline')).replace('<strong>','<b>').replace('</strong>','</b>'))+p('lead',inline_content(find(t,'lead')))))
        out.append(p('meta',inline_content(find(t,'meta'))))
        out.append('<div class="deco"></div>')
    elif cid=='scanline-rise':
        brand=find(t,'brand');out.append(tag('div','top',inline_content(brand)))
        if cover:
            # The sole cover has a large two-line text block and contact metadata.
            body=next(iter(t.xpath('//body')),t)
            texts=[e for e in body.iter() if 'font-size:84px' in e.get('style','')]
            if texts:
                e=copy.deepcopy(texts[0]);lead=next(iter(e.xpath('./p')),None);leadvalue=inline_content(lead)
                if lead is not None:e.remove(lead)
                bits=[H.escape(text(c)) for c in e]
                titlevalue=('<b>'+bits[0]+'</b><br>'+bits[1]) if len(bits)>1 else H.escape(text(e))
                out.append(tag('div','lockup at-left',tag('h1','title',titlevalue)+p('lead',leadvalue)))
            lines=[]
            for e in body.iter():
                if 'top:524px' in e.get('style',''):
                    for x,icon_name in zip(e,('mail','phone','map-pin')):
                        label=x.xpath('./b');label=label[0]if label else None
                        value=H.escape(label.tail or '').strip()if label is not None else H.escape(text(x))
                        lines.append(p('label','<span class="icon" data-icon="'+icon_name+'"></span><b>'+H.escape(text(label))+'</b><span>'+value+'</span>'))
                    break
            out.append(tag('div','meta',''.join(lines)))
        else:
            h=find(t,'heading');value=inline_content(h)
            value=re.sub(r'<span>(.*?)</span>',r'<b>\1</b><br>',value,count=1,flags=re.S)
            section=text(find(t,'section'))
            source_title=find(t,'title')
            if h is not None or source_title is not None:
                if h is None:
                    value=inline_content(source_title)
                    section=text(find(t,'chip'))
                out.append(tag('header','head',(p('kicker',H.escape(section))if section else'')+tag('h1','title',value)))
            else:
                title=next((e for e in t.iter() if numeric_style(e).get('font-size')=='76px'),None)
                lead=next((e for e in t.iter() if numeric_style(e).get('top')=='256px'),None)
                out.append(tag('header','head center',tag('h1','title',inline_content(title))+p('lead',inline_content(lead))))
        out.append(scan_decoration(t))
    elif cid=='cinder-pulse':
        if cover:
            # Legitimate cover lockup placements encode three source furniture designs.
            texts=[e for e in t.iter() if cls(e,'text')]
            def with_size(n):return next((e for e in texts if f'font-size:{n}px' in e.get('style','')),None)
            size=88 if nn=='20'else 72;title=with_size(size);lead=with_size(40 if nn=='20'else 20)
            value=inline_content(title)
            # .accent is source-only; the source emphasized span becomes b.
            if title is not None:
                raw=inner(title);raw=re.sub(r'<span[^>]*class="accent"[^>]*>(.*?)</span>',r'<b>\1</b>',raw,flags=re.S)
                value=re.sub(r'\sstyle="[^"]*"','',raw)
            kicker='PART 1' if nn=='03' else 'MIRI Company'
            place='at-center'if nn=='20'else('at-top-left'if nn=='03'else'at-left')
            out.append(tag('div','lockup '+place,p('kicker',kicker)+tag('h1','title',value)+p('lead',inline_content(lead))))
            if nn=='03':
                # The source arrow belongs to the cover furniture, never a card connector.
                out[-1]=out[-1].removesuffix('</div>')+'<span class="icon" data-icon="arrow-down-right"></span></div>'
            meta=with_size(16)
            if meta is not None:out.append(p('meta',inline_content(meta)))
            out.append(cinder_decoration(t))
        elif nn=='02':
            fs=[x for x in instances if x['use']=='furniture' and x['bbox'][0]<400 and x.get('text')]
            out.append(tag('div','top',tag('h1','title',H.escape(fs[0].get('text',''))if fs else'')+p('kicker',H.escape(fs[1].get('text','')).replace('\n','<br>')if len(fs)>1 else'')))
            out.append(cinder_decoration(t))
        else:
            panel=next((x for x in instances if x['use']=='furniture' and x.get('source',{}).get('parts')),None)
            if panel is not None:
                ps=panel['source']['parts'];rail=panel['bbox'][2]<500
                def value(item):
                    e=html.fragment_fromstring('<div>'+item['html']+'</div>')
                    # Accent PART text uses the named foundation section part.
                    for n in e.iter():
                        if cls(n,'accent'):n.set('class','sec')
                    return inline_content(e)
                out.append(tag('div'if rail else'header','rail'if rail else'head',p('kicker',value(ps[0]))+tag('h1','title',value(ps[1])if len(ps)>1 else'')+(p('lead',value(ps[2]))if len(ps)>2 else'')))
    for item in instances:
        if item['instance_id'].endswith('-arrow-furniture'):
            x,y,w,h=item['bbox'];n=item['source']['numbers'];scale=n['arrowBox']/n['viewBox'];off=(w-n['arrowBox'])/2
            out.append('<svg class="deco navigation" viewBox="0 0 1280 720" aria-hidden="true"><g transform="translate('+str(x)+' '+str(y)+')"><circle cx="'+str(w/2)+'" cy="'+str(h/2)+'" r="'+str(w/2)+'" fill="var(--a1)"/><path transform="translate('+str(off)+' '+str(off)+') scale('+str(scale)+')" d="'+n['path']+'" fill="none" stroke="var(--a1-on)" stroke-width="'+str(n['stroke'])+'"/></g></svg>')
    photos=[x for x in instances if x.get('source',{}).get('furniturePart')=='photo-background']
    if photos:
        shapes=[]
        for item in photos:
            x,y,w,h=item['bbox'];rx=w/2 if'cap'in item.get('source',{}).get('seatClass','').split() else 0;shapes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="var(--n-2)"/>')
        out.append('<svg class="deco furniture" viewBox="0 0 1280 720" aria-hidden="true">'+''.join(shapes)+'</svg>')
    # Footer text that crosses an image placeholder uses the readable neutral
    # foreground role. This is a reusable furniture state, not a page selector.
    if photos:
        for i,fragment in enumerate(out):
            if 'class="foot"'not in fragment:continue
            node=html.fragment_fromstring(fragment)
            for part in node:
                label=text(part)
                measured=next((x for x in instances if x.get('use')=='furniture'and str(x.get('text','')).strip()==label),None)
                if measured:
                    x,y,w,h=measured['bbox'];cx=x+w/2;cy=y+h/2
                    if any(p['bbox'][0]<=cx<=p['bbox'][0]+p['bbox'][2]and p['bbox'][1]<=cy<=p['bbox'][1]+p['bbox'][3]for p in photos):part.set('class',part.get('class','')+' over-photo')
            out[i]=html.tostring(node,encoding='unicode')
    return slide,cover,''.join(out)

def project(bb,field,gap):
    x,y,w,h=bb;fx,fy,fw,fh=field
    cw=(fw-11*gap)/12;rh=(fh-5*gap)/6
    # Select the nearest grid lines, retaining geometry independent of CSS/fixture min.
    a=max(0,min(11,round((x-fx)/(cw+gap))));b=max(a+1,min(12,round((x+w-fx+gap)/(cw+gap))))
    c=max(0,min(5,round((y-fy)/(rh+gap))));d=max(c+1,min(6,round((y+h-fy+gap)/(rh+gap))))
    result=[fx+a*(cw+gap),fy+c*(rh+gap),(b-a)*(cw+gap)-gap,(d-c)*(rh+gap)-gap]
    return(a+1,b-a,c+1,d-c),result

def sanitize_markup(markup,cid):
    nodes=html.fragments_fromstring(markup)
    root=next(e for e in nodes if not isinstance(e,str))
    for e in root.iter():
        if e.tag in ('script','style'):raise ValueError('active source markup')
        if e.tag=='svg':raise ValueError('element maps must contain empty Lucide icon spans')
        for a in list(e.attrib):
            if a.startswith('on')or a in ('id','width','height'):del e.attrib[a]
        if e.get('style'):
            props=[]
            for pair in e.get('style').split(';'):
                if ':'not in pair:continue
                k,v=pair.split(':',1);k=k.strip();v=v.strip()
                if k.startswith('--')and re.fullmatch(r'[-+\d. %]+',v):props.append(k+':'+v)
            if props:e.set('style',';'.join(props))
            else:e.attrib.pop('style',None)
    return root

def dense_position(bb,field):
    x,y,w,h=bb;fx,fy,fw,fh=field
    a=max(0,min(119,round((x-fx)/fw*120)));b=max(a+1,min(120,round((x+w-fx)/fw*120)))
    c=max(0,min(59,round((y-fy)/fh*60)));d=max(c+1,min(60,round((y+h-fy)/fh*60)))
    return f'grid-column:{a+1} / span {b-a};grid-row:{c+1} / span {d-c}'

def panel_markup(panel,instances,cid,fresh=False):
    classes=panel.get('classes',[]);classes=classes.split()if isinstance(classes,str)else list(classes)
    if 'panel'not in classes:classes.insert(0,'panel')
    node=html.Element('div',{'class':' '.join(classes),'data-slot':panel.get('id')or panel.get('instance_id')or 'source-panel'})
    field=panel['bbox'];numbers=panel.get('sourceNumbers',{});bar=panel.get('bar')or{}
    if any(bar.values()):
        bb=numbers.get('barBBox')or[field[0],field[1],field[2],min(50,field[3]*.18)]
        b=etree.SubElement(node,'div',{'class':'bar','style':dense_position(bb,field)})
        if bar.get('kick')or bar.get('kicker'):etree.SubElement(b,'span',{'class':'kick'}).text='이력'if fresh else str(bar.get('kick')or bar.get('kicker'))
        if bar.get('name'):etree.SubElement(b,'b',{'class':'name'}).text=('회수 현황'if len(str(bar['name']).replace(' ',''))<=7 else'거점별 출고 이력과 빈 용기 회수량 비교')if fresh else str(bar['name'])
        if bar.get('note'):etree.SubElement(b,'span',{'class':'note'}).text='단위: 건 / 회'if fresh else str(bar['note'])
    content=etree.SubElement(node,'div',{'class':'panel-body'})
    ids=panel.get('children',panel.get('childrenIDs',[]));lookup={x['instance_id']:x for x in instances}
    for key in ids:
        if key not in lookup:raise ValueError('Missing panel child '+cid+' '+str(key))
        inst=lookup[key]
        if not inst.get('markup'):continue
        markup=inst['markup']
        if fresh:
            folder=ROOT/cid/'elements'/inst['leaf']/'fixtures';fixture=folder/(str(inst.get('fixture',''))+'.html')
            if not fixture.exists():fixture=next(iter(sorted(folder.glob('*.html'))),None)
            if fixture:markup=re.sub(r'<!--.*?-->','',fixture.read_text(),flags=re.S)
        child=sanitize_markup(markup,cid);other=child.get('style','');child.set('style',dense_position(inst['bbox'],field)+(';'+other if other else''));content.append(child)
    seatbox=panel.get('imageBBox')or numbers.get('imageBBox')
    if seatbox:
        etree.SubElement(content,'div',{'class':'seat logo','data-ph':'1'if fresh else panel.get('imageLabel','1'),'style':dense_position(seatbox,field)})
    if panel.get('caption'):
        bb=panel.get('captionBBox')or[field[0]+field[2]*.05,field[1]+field[3]*.9,field[2]*.9,field[3]*.05]
        etree.SubElement(node,'p',{'class':'caption','style':dense_position(bb,field)}).text='* 출고 이력과 용기 회수 기록을 함께 점검한 결과입니다.'if fresh else panel['caption']
    return node

def main(args):
    configs=json.loads((ROOT/'foundation-geometry.json').read_text());report=[]
    for item in json.loads((ROOT/'collections.json').read_text()):
        cid=item['id']
        if args.collections and cid not in args.collections:continue
        R=ROOT/(cid+'-review');m=json.loads((R/'map.json').read_text())
        additions=ROOT/'round5/furniture-additions.json'
        if additions.exists():
            for photo in json.loads(additions.read_text()).get(cid,[]):
                bb=photo['bbox'];owners=[x for x in m['instances']if x['page']==photo['page']and x.get('leaf')and x['use']!='unexpressible']
                owned=any(bb[0]>=x['bbox'][0]-2 and bb[1]>=x['bbox'][1]-2 and bb[0]+bb[2]<=x['bbox'][0]+x['bbox'][2]+2 and bb[1]+bb[3]<=x['bbox'][1]+x['bbox'][3]+2 for x in owners)
                if not owned and not any(x['instance_id']==photo['instance_id']for x in m['instances']):m['instances'].append(photo)
        out=R/'reassembled';out.mkdir(exist_ok=True)
        css=[]
        for rel in ['kit/css/tokens.css','foundation/foundation.css']+['elements/'+p.name+'/element.css'for p in sorted((ROOT/cid/'elements').iterdir())if p.is_dir()]:
            css.append(f'<link rel="stylesheet" href="../../{cid}/{rel}">')
        defaults={};registrations={}
        for f in [ROOT/cid/'foundation/foundation.json',*sorted((ROOT/cid/'elements').glob('*/element.json'))]:
            data=json.loads(f.read_text());defaults.update(data.get('tokenDefaults',{}));registrations.update(data.get('registrations',{}))
        # Deterministically regenerate shared contract runtime on every build.
        runtime=ROOT/'runtime.css'
        ts=json.loads((ROOT/'contract/type-steps.json').read_text());ts=ts['steps']if isinstance(ts,dict)and'steps'in ts else ts
        if isinstance(ts,dict):ts=ts.get('values',list(ts))
        palette=json.loads((ROOT/'contract/palette.json').read_text())
        runtime.write_text('html,body{margin:0;padding:0;width:1280px;height:720px}\n.slide{'+''.join(f'--type-{n}:{n}px;'for n in ts)+'--radius-lg:var(--radius);}\n.slide{'+''.join(k+':'+v+';'for k,v in palette['light'].items())+'}\n.slide.dark{'+''.join(k+':'+v+';'for k,v in palette['dark'].items())+'}\n')
        defaultsfile=ROOT/cid/'runtime-defaults.css'
        # Runtime defaults are outside the collection package; element.json is canonical.
        defaultsfile=R/'runtime-defaults.css';defaultsfile.write_text('\n'.join(registrations[k]for k in sorted(registrations))+'\n.slide{'+''.join(k+':'+str(defaults[k])+';'for k in sorted(defaults))+'}')
        frozen=ROOT/'reference/frozen'/(cid+'-review')/'replica'
        source_folder=frozen if frozen.exists()else Path(item['replica'])
        for source in sorted(source_folder.glob('*.html')):
            nn=re.search(r'(\d+)\.html$',source.name)[1];instances=[x for x in m['instances']if x['page']==nn];t=html.fromstring(source.read_text())
            slide,cover,furn=furniture(cid,nn,t,instances);field=configs[cid]['body'];gap=16
            tokens=(ROOT/cid/'kit/css/tokens.css').read_text();mg=re.search(r'--gap-sm:\s*([\d.]+)px',tokens)
            if mg:gap=float(mg[1])
            if cid=='cinder-pulse':
                if 'class="top"'in furn:field=[588,57,635,607]
                elif 'class="rail"'in furn:field=[437,70,772,580]
                else:field=[71,203,1138,447]
            parts=[];boxes=[];rail_parts=[]
            panels=[x for x in m.get('panels',[])if x['page']==nn]
            panel_children={key for p in panels for key in p.get('children',p.get('childrenIDs',[]))}
            for panel in panels:
                node=panel_markup(panel,instances,cid)
                slots,actual=project(panel['bbox'],field,gap);a,b,c,d=slots
                node.set('style',f'grid-column:{a} / span {b};grid-row:{c} / span {d}')
                parts.append(html.tostring(node,encoding='unicode'));boxes.append({'instance':panel.get('id',panel.get('instance_id','panel')),'leaf':'foundation.panel','source':panel['bbox'],'grid':slots,'projected':actual})
            for inst in instances:
                if inst['instance_id']in panel_children:continue
                if inst.get('source',{}).get('furniturePart')=='seat':
                    slots,actual=project(inst['bbox'],field,gap);a,b,c,d=slots
                    parts.append(f'<div class="seat {inst["source"].get("seatClass","")}" data-ph="1" style="grid-column:{a} / span {b};grid-row:{c} / span {d}"></div>');continue
                if not inst.get('leaf')or inst.get('inline')or inst.get('contained_by')or inst['use']in('unexpressible','furniture','background'):continue
                if not inst.get('markup'):raise ValueError('Missing map markup: '+inst['instance_id'])
                node=sanitize_markup(inst['markup'],cid)
                in_rail=inst.get('source',{}).get('placementField')=='rail'
                slots,actual=project(inst['bbox'],[34,34,355,652] if in_rail else field,gap);a,b,c,d=slots
                value=node.get('style','');node.set('style',f'grid-column:{a} / span {b};grid-row:{c} / span {d}'+(';'+value if value else''))
                (rail_parts if in_rail else parts).append(html.tostring(node,encoding='unicode',with_tail=False));boxes.append({'instance':inst['instance_id'],'leaf':inst['leaf'],'source':inst['bbox'],'grid':slots,'projected':actual,'delta':[round(actual[i]-inst['bbox'][i],3)for i in range(4)]})
            if rail_parts:
                furniture_root=html.fragment_fromstring('<div>'+furn+'</div>');rail_node=next(iter(furniture_root.xpath('./div[contains(concat(" ",normalize-space(@class)," ")," rail ")]')),None)
                if rail_node is None:raise ValueError('Source requests absent foundation rail')
                rail_node.append(html.fragment_fromstring('<div class="group">'+''.join(rail_parts)+'</div>'))
                furn=inner(furniture_root)
            # Covers with observed image frames still use the canonical body grid.
            body='<div class="body">'+''.join(parts)+'</div>'if parts or not cover else''
            doc='<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="../../fonts/fonts.css"><link rel="stylesheet" href="../../runtime.css">'+''.join(css)+'<link rel="stylesheet" href="../runtime-defaults.css"><body><section class="'+slide+'"><div class="page">'+furn+body+'</div></section><script src="../../assets/lucide.js"></script><script src="../../assets/icons.js"></script></body></html>'
            (out/('slide_'+nn+'.html')).write_text(doc)
            report.append({'collection':cid,'page':nn,'source':str(source),'boxes':boxes,'unexpressible':[x['instance_id']for x in instances if x['use']=='unexpressible']})
    (ROOT/'reassembly-projection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print('Assembled',len(report),'pages')

if __name__=='__main__':
    p0=argparse.ArgumentParser();p0.add_argument('collections',nargs='*');main(p0.parse_args())

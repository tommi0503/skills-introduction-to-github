from pathlib import Path
from lxml import html,etree
R=Path('/workspace/output/nightchamfer-review/replica')
def read(n):return html.fromstring((R/f'slide_{n:02}.html').read_text())
def write(n,d):(R/f'slide_{n:02}.html').write_text('<!doctype html>'+html.tostring(d,encoding='unicode'))
def sty(e,**kw):
 s=dict(x.split(':',1)for x in e.get('style','').split(';')if ':'in x);s.update({k.replace('_','-'):str(v)for k,v in kw.items()});e.set('style',';'.join(k+':'+v for k,v in s.items()))
def box(sec,txt,style,cls='box'):
 e=html.fragment_fromstring(f'<div class="{cls}" style="{style}">{txt}</div>');sec.append(e);return e
for n in range(1,19):
 d=read(n)
 for e in d.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," ph ")]'):e.text='';[e.remove(ch)for ch in list(e)]
 write(n,d)
d=read(1);h=d.xpath('//h1')[0];sty(h,font_size='108px',position='relative',z_index='4');write(1,d)
d=read(2)
for e in d.xpath('//div[contains(@style,"top:129px")]'):sty(e,top='113px')
write(2,d)
d=read(5);sec=d.xpath('//section')[0];plot=d.xpath('//div[contains(@class,"barplot")]')[0];sty(plot,background='none')
plot.insert(0,html.fragment_fromstring('<svg viewBox="0 0 457 196" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%;z-index:-1"><path d="M0 0.5H457M0 65.5H457M0 130.5H457M0 195.5H457" stroke="#777" fill="none" stroke-width="1"/></svg>'));sty(plot,isolation='isolate')
for e in d.xpath('//div[contains(@class,"chip")]'):sty(e,border_radius='12px')
write(5,d)
d=read(6)
for b in d.xpath('//div[contains(@style,"top:102px")]/b'):
 par=b.getparent();par.text=b.text
 for ch in list(b):par.append(ch)
 par.remove(b)
for b in d.xpath('//b[contains(text(),"AI")]'):b.attrib.pop('class',None)
write(6,d)
d=read(7)
for e in d.xpath('//div[contains(@class,"chip")]'):
 tx=''.join(e.itertext())
 if tx=='AI 미사용 고객':sty(e,background='linear-gradient(90deg,#777 0%,#777 50%,#444 50%,#444 100%)',font_weight='500')
 elif tx=='AI 사용 고객':sty(e,background='#3982FB',font_weight='500')
for e in d.xpath('//div[contains(@style,"border-left")]'):sty(e,border_left='1px dotted #888')
write(7,d)
d=read(8);sec=d.xpath('//section')[0]
for x in [429,813]:box(sec,'',f'left:{x}px;top:426px;width:26px;border-top:2px dotted #888')
write(8,d)
d=read(9);sec=d.xpath('//section')[0]
for e in d.xpath('//div[contains(@class,"chip")]'):
 if '기존 플랜' in ''.join(e.itertext()):sty(e,background='linear-gradient(90deg,#2874E6,#173B88)')
for x in [835,982]:box(sec,'',f'left:{x}px;top:522px;width:21px;border-top:1px dotted #aaa')
write(9,d)
d=read(10);sec=d.xpath('//section')[0]
for e in list(sec):
 if e.tag in ['div'] and e.get('class')!='brand':sec.remove(e)
for i,(x,y,w,h,label,fill,ty,k,tx)in enumerate([(229,260,214,72,'4단계','#242D34',275,'외부 확장','레퍼런스와 입소문을 지렛대로 신규, 기업 고객까지 확대'),(174,325,324,106,'3단계','#525E6A',368,'조직 표준화','팀을 넘어 회사 표준 도구로 정착시켜 객단가 상승'),(125,393,422,136,'2단계','#8395A9',461,'팀 확산','한 명의 사용 경험이 팀 전체로 번지는 협업 기반 자연 확산'),(84,466,504,156,'1단계','#A8C0DA',553,'내부 침투','기존 유저에게 무료로 노출해 진입 비용 최소화')]):
 box(sec,'',f'left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:50%;background:linear-gradient(#000,{fill});z-index:{5-i}')
 box(sec,f'<b>{label}</b>',f'left:{x}px;top:{ty}px;width:{w}px;font-size:20px;line-height:1.3;text-align:center;z-index:8')
 x1=x+w+(15 if i==3 else 24);box(sec,'',f'left:{x1}px;top:{ty+14}px;width:{634-x1}px;border-top:2px dotted #888')
 box(sec,f'<b>{k}</b> |　{tx}',f'left:670px;top:{ty}px;width:535px;font-size:20px;line-height:1.3;color:#ccc;z-index:8')
write(10,d)
d=read(11)
for e in d.xpath('//div[contains(@class,"chip")]'):sty(e,border_radius='999px',font_weight='400')
for e in d.xpath('//div[contains(@style,"border-left")]'):sty(e,border_left='1px dotted #888')
write(11,d)
d=read(12)
for e in d.xpath('//div[contains(@style,"width:237px")]'):sty(e,width='250px',font_size='20px',line_height='1.45')
for e in d.xpath('//div[contains(@style,"top:495px")]'):
 e.text='기존 고객을 대상으로 회의록·';[e.remove(ch)for ch in list(e)];e.append(html.fragment_fromstring('<span><br>문서 요약 기능을 우선 공개합<br>니다.</span>'))
write(12,d)
d=read(13);sec=d.xpath('//section')[0];plot=d.xpath('//div[contains(@class,"barplot")]')[0];sty(plot,background='none',height='240px')
for e,v in zip(plot.xpath('./div[contains(@class,"bar")]'),[72,240]):sty(e,height=f'{v}px')
sec.append(html.fragment_fromstring('<svg viewBox="0 0 182 194" style="position:absolute;left:722px;top:244px;width:182px;height:194px"><defs><linearGradient id="rise" x2="0" y2="1"><stop stop-color="#3982fb"/><stop offset="1" stop-color="#102845" stop-opacity=".2"/></linearGradient></defs><path d="M0 194C63 181 107 131 108 48H88L132 0 176 48H147C137 133 84 184 0 194Z" fill="url(#rise)"/></svg>'))
write(13,d)
d=read(15)
for e in d.xpath('//div[contains(@style,"top:74px")]'):sty(e,top='61px')
write(15,d)
d=read(16);sec=d.xpath('//section')[0]
rail=d.xpath('//div[contains(@style,"left:79px")]')[0];sty(rail,top='313px')
for e in list(rail):rail.remove(e)
for j,tx in enumerate(['AI 정확도','AI 비용','데이터 보안']):box(rail,f'<b>{tx}</b>',f'left:0;top:{37+j*102}px;width:168px;font-size:22px;text-align:center;line-height:1.3')
for j in [1,2]:box(rail,'',f'left:30px;top:{j*102+2}px;width:108px;border-top:1px dotted #777')
for panel in d.xpath('//div[contains(@style,"width:446px")]'):
 for ch in list(panel):panel.remove(ch)
 right='757px'in panel.get('style','');sty(panel,border_color='#3468a4' if right else '#65676a')
 box(panel,'대응 방안' if right else '위험 요인','left:145px;top:34px;width:155px;height:49px;border:1px solid '+('#3468a4' if right else '#555')+';border-radius:999px;background:none;font-size:22px;display:flex;align-items:center;justify-content:center','chip gray')
 lines=['출처 표기·검증 단계·사용자 피드백 루프로 보완','사용량 과금·경량 모델 병행으로 마진 확보','데이터 격리·미학습 정책·보안 인증으로 신뢰 확보']if right else['부정확한 답변(환각)으로 인한 신뢰 저하 우려','LLM 호출 비용이 수익성을 압박할 가능성 존재','업무 데이터의 외부 유출에 대한 고객 우려']
 for j,tx in enumerate(lines):
  box(panel,tx,f'left:31px;top:{120+j*102}px;width:385px;font-size:18px;text-align:center;color:#ccc;line-height:1.35')
  if j<2:box(panel,'',f'left:31px;top:{184+j*102}px;width:385px;border-top:1px dotted #777')
write(16,d)
d=read(17)
for e in d.xpath('//div[contains(@class,"arrow")]'):
 if 'rotate' in e.get('style',''):sty(e,transform='none',background='linear-gradient(90deg,#008fee,transparent)',clip_path='polygon(0 50%,14.6% 0,14.6% 28%,100% 28%,100% 72%,14.6% 72%,14.6% 100%)')
 else:sty(e,background='linear-gradient(90deg,transparent,#c4d9e9)',clip_path='polygon(0 28%,85.4% 28%,85.4% 0,100% 50%,85.4% 100%,85.4% 72%,0 72%)')
write(17,d)
p=R/'replica.css';p.write_text(p.read_text()+'''\nsection:not(.cover){background:#000;isolation:isolate}section:not(.cover)::after{content:"";position:absolute;inset:0;z-index:10;pointer-events:none;mix-blend-mode:screen;background:radial-gradient(ellipse 140% 28% at 50% 105%,#4082f0 0%,#143263 48%,#07111e 72%,transparent 100%)}.ph{z-index:11}.cover>.ph{z-index:0}.cover>.box{position:absolute;z-index:3}.cover h1{position:relative;z-index:4}.cover h1.lift{display:inline-block;width:max-content;background-image:linear-gradient(90deg,#fff 0%,#fff 30%,#3982dd 100%)}.cover b.lift{display:inline-block}.dotted{border-top:1px dotted #888}.arrow:not(.right){clip-path:polygon(50% 0,100% 50%,77% 50%,76% 62%,78% 77%,84% 100%,16% 100%,22% 77%,24% 62%,23% 50%,0 50%)}.arrow.down{clip-path:polygon(50% 0,100% 50%,77% 50%,76% 62%,78% 77%,84% 100%,16% 100%,22% 77%,24% 62%,23% 50%,0 50%)}\n''')

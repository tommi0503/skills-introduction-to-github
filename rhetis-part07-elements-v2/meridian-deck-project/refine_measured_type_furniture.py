from pathlib import Path
P=Path(__file__).parent;E=P/'meridian-deck/elements'
def add(l,s):
 p=E/l/'element.css';p.write_text(p.read_text()+'\n'+s+'\n')
add('headline','''.headline[data-el="meridian-deck-headline"].big.center>.kick{font-size:clamp(var(--type-20),min(7cqw,32cqh),var(--type-56))}.headline[data-el="meridian-deck-headline"].big.center>h2{font-size:clamp(var(--type-28),min(9cqw,40cqh),var(--type-68))}.headline[data-el="meridian-deck-headline"].big.on>h2{font-size:clamp(var(--type-28),min(6cqw,30cqh),var(--type-36));font-weight:var(--label-weight)}.headline[data-el="meridian-deck-headline"]:not(.big):not(.center)>h2:has(>b:nth-of-type(2))>b{color:var(--n-7)}''')
add('person','''.person[data-el="meridian-deck-person"]:has(>.seat.portrait){grid-template-rows:minmax(0,calc(100% - var(--type-14)*2.4 - var(--type-10)*1.6 - var(--gap-sm)*2)) auto minmax(0,1fr)}.person[data-el="meridian-deck-person"]:has(>.seat.portrait)>.name{padding-top:0;font-size:var(--type-14);font-weight:var(--name-weight)}.person[data-el="meridian-deck-person"]:has(>.seat.portrait)>.note{font-size:var(--type-10)}''')
add('prose','''.prose[data-el="meridian-deck-prose"]:has(>p>b:only-child)>p{font-size:var(--type-16)}.prose[data-el="meridian-deck-prose"]>p>b:only-child{font-size:var(--type-18);font-weight:var(--title-weight)}''')
p=P/'meridian-deck/foundation/foundation.css'
p.write_text(p.read_text()+'''
/* Quiet hemisphere cover furniture; .on is the accent-medallion closing variant. */
.slide .deco:not(.on){left:50.23%;right:auto;top:58.89%;width:59.38%;height:69.44%;border-radius:999px}
.slide .deco:not(.on)>.label{left:-13.03%;top:14.6%;width:13.42%;height:20.4%}
.slide .deco:not(.on)>.label:nth-child(2){left:30.53%;top:-37.6%;width:6.97%;height:10.6%}
.slide .deco:not(.on)>.label:nth-child(3){left:63.16%;right:auto;top:-15.8%;width:8.29%;height:12.6%}
.slide .deco.on>.label{background:var(--a1);color:var(--a1-on);border:2px solid var(--page)}
''')
p=P/'assemble.py';s=p.read_text();s=s.replace('<div class="deco"><span class="label">','<div class="deco'+"'+(' on' if pg==30 else '')+'"+'"><span class="label">');p.write_text(s)

from pathlib import Path
p=Path('/workspace/work/cyanloop/replicas.py');s=p.read_text()
insert='''
def logo(x,y):
 return f'<svg style="position:absolute;left:{x}px;top:{y}px" width="39" height="40" viewBox="0 0 40 40" fill="white"><circle cx="20" cy="7" r="6"/><circle cx="8" cy="19" r="6"/><circle cx="32" cy="19" r="6"/><circle cx="20" cy="31" r="6"/><path d="M8 19Q20 31 32 19L28 29 20 35 12 29Z"/></svg>'
def special(n):
 defs='<defs><linearGradient id="teal" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#00eee2"/><stop offset="1" stop-color="#001134"/></linearGradient><linearGradient id="reverse"><stop stop-color="#001134"/><stop offset="1" stop-color="#00eee2"/></linearGradient><linearGradient id="blue"><stop stop-color="#001134"/><stop offset="1" stop-color="#0753d6"/></linearGradient><linearGradient id="mix" x1="1" y1="0" x2="0" y2="1"><stop stop-color="#00a9ee"/><stop offset="1" stop-color="#0753d6"/></linearGradient><linearGradient id="vert" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#00bbb8"/><stop offset="1" stop-color="#001134"/></linearGradient></defs>'
 if n==1:
  paths='<path d="M1192 0V461" stroke="url(#vert)" stroke-width="81"/><path d="M857 461A167.5 167.5 0 0 1 1192 461" stroke="url(#teal)" stroke-width="83"/><circle cx="857" cy="461" r="41.5" fill="#00eee2"/><path d="M1192 461A172 172 0 0 1 1034 633" stroke="url(#mix)" stroke-width="83"/><circle cx="1192" cy="461" r="41.5" fill="#00a9ee"/><path d="M0 633H1034" stroke="url(#blue)" stroke-width="83"/><circle cx="1034" cy="633" r="41.5" fill="#0753d6"/>'
 elif n==2:
  paths='<path d="M801 247A139 139 0 1 1 1065 160" stroke="url(#teal)" stroke-width="70"/><circle cx="801" cy="247" r="35" fill="#00eee2"/><path d="M1065 160A139 139 0 1 1 1340 115" stroke="url(#blue)" stroke-width="70"/><circle cx="1065" cy="160" r="35" fill="#0753d6"/>'
 elif n==3:
  paths='<path d="M655 123A160 160 0 0 1 882 278" stroke="url(#reverse)" stroke-width="78"/><circle cx="882" cy="278" r="39" fill="#00eee2"/><path d="M882 297A161 161 0 0 0 1204 297" stroke="url(#reverse)" stroke-width="78"/><circle cx="1204" cy="297" r="39" fill="#2bd4c8"/><path d="M95 480A140 140 0 0 0 375 480" stroke="url(#blue)" stroke-width="78"/><circle cx="95" cy="480" r="39" fill="#0753d6"/>'
 else:
  paths='<path d="M808 82A125 125 0 0 0 1058 82" stroke="url(#reverse)" stroke-width="78"/><circle cx="1058" cy="82" r="39" fill="#2bd4c8"/><path d="M1056 296C1018 410 1098 490 1211 494" stroke="url(#reverse)" stroke-width="78"/><circle cx="1211" cy="494" r="39" fill="#00eee2"/><path d="M985 720A150 150 0 0 1 1285 720" stroke="url(#blue)" stroke-width="80"/>'
 return '<svg style="position:absolute;left:0;top:0" width="1280" height="720" viewBox="0 0 1280 720" fill="none">'+defs+paths+'</svg>'
'''
s=s.replace("titles=['HRD Learning Solution'",insert+"\ntitles=['HRD Learning Solution'")
s=s.replace("s+=loop(756,203,512,'#00eee2',180)+loop(756,203,512,cyan,0)+box(1151,0,81,450,'transparent',radius=0,extra='background:linear-gradient(#00bbb8,transparent)')","s+=special(1)")
s=s.replace("s+=box(0,591,1036,83,'transparent',radius=0,extra='background:linear-gradient(90deg,transparent,#0753d6)')+tx(62,612,'● MIRI HRD',30,'white',700)","s+=logo(61,614)+tx(115,615,'MIRI HRD',30,'white',700)")
s=s.replace("s+=loop(700,-10,450,'#00eee2',-30)+loop(980,-180,450,blue,160)","s+=special(2)")
s=s.replace("s+=loop(522,15,440,'#00eee2',180)+loop(870,105,440,teal)+loop(0,370,400,blue)","s+=special(3)")
s=s.replace("s+=loop(738,-122,438,teal)+loop(962,117,355,'#00eee2',70)+loop(950,470,400,blue,180)","s+=special(18)")
s=s.replace("tx(1029,624,'● MIRI HRD',25,'white',700)","logo(1027,620)+tx(1073,624,'MIRI HRD',25,'white',700)")
p.write_text(s)

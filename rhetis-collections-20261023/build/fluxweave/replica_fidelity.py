from pathlib import Path
p=Path('/workspace/work/fluxweave/replicas.py');s=p.read_text();a=s.index('def wave(');b=s.index('def base(',a)
s=s[:a]+'''from waves import wave_svg
def wave(x=0,y=350,w=1280,h=370,flip=False):
 kind=1
 if x==-240:kind=2;x=0;y=0;w=520;h=440
 elif x==250:kind=3;x=0;y=0;w=1280;h=340
 elif x==-70:kind=4;x=0;y=500;w=212;h=220
 z=wave_svg(kind).replace('var(--a2-4-soft)','#42bdec').replace('var(--a1-4-soft)','#c287ee')
 return '<div class="wave" style="left:'+str(x)+'px;top:'+str(y)+'px;width:'+str(w)+'px;height:'+str(h)+'px;'+('transform:scaleX(-1);' if flip else '')+'">'+z+'</div>'
'''+s[b:]
a=s.index('def chart(');b=s.index('pages={}',a)
s=s[:a]+'''def chart(x,y,w,h,vals,line=None,title=''):
 maxi=100 if '컨설팅' in title else 200;unit='건' if maxi==100 else '명';ticks=5 if maxi==100 else 4;b='';pts=[];plotx=82;ploty=105;plotw=315;ploth=192;base=ploty+ploth
 grid=''.join(f'<path d="M{plotx} {ploty+j*ploth/ticks}H{plotx+plotw}" stroke="#ddd"/><text x="{plotx-6}" y="{ploty+j*ploth/ticks+4}" text-anchor="end" fill="#333" font-size="12">{round(maxi*(1-j/ticks))}{unit}</text>' for j in range(ticks+1))
 if line:
  pts=[(plotx+(i+.5)*plotw/len(vals),base-v/maxi*ploth) for i,v in enumerate(line)]
  b+='<polygon points="'+str(pts[0][0])+','+str(base)+' '+' '.join(f'{a},{z}' for a,z in pts)+' '+str(pts[-1][0])+','+str(base)+'" fill="#099ef3" opacity=".28"/>'
 for i,v in enumerate(vals):
  bx=plotx+(i+.17)*plotw/len(vals);bw=plotw/len(vals)*.66;by=base-v/maxi*ploth
  b+=f'<rect x="{bx}" y="{by}" width="{bw}" height="{base-by}" rx="11" fill="#a13cff"/><text x="{bx+bw/2}" y="{by+19}" text-anchor="middle" fill="white" font-size="14">{v}{unit}</text><text x="{bx+bw/2}" y="{base+19}" text-anchor="middle" fill="#333" font-size="12">{2080+i}</text>'
 if line:
  b+='<polyline points="'+' '.join(f'{a},{z}' for a,z in pts)+'" fill="none" stroke="#099ef3" stroke-width="2"/>'
  b+=''.join(f'<circle cx="{a}" cy="{z}" r="3" fill="#099ef3"/><text x="{a}" y="{z-12}" text-anchor="middle" fill="#099ef3" font-size="14">{v}{unit}</text>' for (a,z),v in zip(pts,line))
 labels=['프로젝트 수','재계약률'] if maxi==100 else ['임직원 수','고객사 수']
 b+=f'<rect x="159" y="340" width="11" height="11" rx="2" fill="#a13cff"/><text x="173" y="350" fill="#333" font-size="11">{labels[0]}</text><circle cx="237" cy="345" r="5" fill="#099ef3"/><text x="245" y="350" fill="#333" font-size="11">{labels[1]}</text>'
 return at(x,y,w,h,'<h2 style="margin:0 0 14px">'+title+'</h2><svg width="100%" height="100%" viewBox="0 0 '+str(w)+' '+str(h)+'" style="position:absolute;inset:0;font:15px Pretendard Variable">'+grid+b+'</svg>','panel')
'''+s[b:]
# Own custom icon span initially inherited white on white-circle fields; assign explicit icon role.
s=s.replace("(R/'replica.css').write_text(css)",'''css+=' .wave>svg{width:100%;height:100%;display:block}.rail .wave{left:0!important;top:500px!important;width:212px!important;height:220px!important;transform:none!important}.circle[style*="background:white"] .icon{color:#a13cff}.circle .icon svg{display:block}.panel[style*="background:#099ef3"] .icon{color:white}.panel .icon svg{display:block}.slide .data-table th{border-radius:12px 12px 0 0}.panel[style*="opacity"] .icon{color:inherit}'
pages[4]=pages[4].replace('text-align:right;margin-top:18px','text-align:right;margin-top:18px;margin-right:292px')
pages[7]=pages[7].replace('>누적 프로젝트</span>','><span style="display:inline-block;width:24px;height:24px;vertical-align:middle;margin-right:8px">'+icon('briefcase').replace('class="icon"','class="icon" style="width:24px;height:24px;color:#999;margin:0"')+'</span>누적 프로젝트</span>').replace('>누적 고객사</span>','><span style="display:inline-block;width:24px;height:24px;vertical-align:middle;margin-right:8px">'+icon('user').replace('class="icon"','class="icon" style="width:24px;height:24px;color:#999;margin:0"')+'</span>누적 고객사</span>')
pages[10]=pages[10].replace('<th>핵심 효과</th>','<th style="width:35%">핵심 효과</th>')
pages[11]=pages[11].replace('class="icon"','class="icon" style="color:#099ef3"').replace('background:#099ef3;color:white;','background:#099ef3;color:white;').replace('color:#099ef3"><svg','color:#099ef3"><svg')
pages[11]=pages[11].replace('background:#099ef3;color:white;text-align:center;padding:38px 16px;">'+icon('puzzle').replace('class="icon"','class="icon" style="color:#099ef3"'),'background:#099ef3;color:white;text-align:center;padding:38px 16px;">'+icon('puzzle').replace('class="icon"','class="icon" style="color:white"'))
pages[12]=pages[12].replace('<th>구분</th>','<th style="width:25%">구분</th>').replace('<th>제품·서비스</th>','<th style="width:25%">제품·서비스</th>').replace('<th>주요 특징</th>','<th style="width:31%">주요 특징</th>').replace('<th>추천 대상</th>','<th style="width:19%">추천 대상</th>')
for _name in ['MIRI Basic','MIRI Pro','MIRI Enterprise','MIRI Consulting','MIRI Care']:
 pages[12]=pages[12].replace('<td>'+_name+'</td>','<td><svg style="width:16px;height:16px;vertical-align:middle;margin-right:4px" viewBox="0 0 24 24"><rect x="1" y="1" width="22" height="22" rx="3" fill="'+('#099ef3' if _name=='MIRI Care' else '#a13cff')+'"/><path d="m6 12 4 4 8-9" fill="none" stroke="white" stroke-width="3"/></svg>'+_name+'</td>')
pages[14]=pages[14].replace('<th>항목</th>','<th style="width:21.2%;background:#d1d2d3;color:#363636">항목</th>').replace('<th>프로젝트 A</th>','<th style="background:#a13cff">프로젝트 A</th>').replace('<th>프로젝트 B</th>','<th style="background:#7d1dcc">프로젝트 B</th>')
# Keep shapes translucent, while labels stay above every overlapping set.
for _word in ['VISION','MISSION','STRATEGY']:
 pages[6]=pages[6].replace('background:'+({'VISION':'#a13cff','MISSION':'#363636','STRATEGY':'#099ef3'}[_word])+';opacity:.92','background:'+({'VISION':'rgba(161,60,255,.92)','MISSION':'rgba(54,54,54,.92)','STRATEGY':'rgba(9,158,243,.92)'}[_word]))
pages[6]=pages[6].replace('<div style="position:absolute;left:0;right:0;top:','<div style="position:absolute;z-index:5;left:0;right:0;top:')
for _i,_ic in enumerate(['puzzle','edit','user']):
 _needle=f'background:{["#099ef3","#a13cff","#7d1dcc"][_i]};color:white;padding:22px 18px;">'
 pages[17]=pages[17].replace(_needle,_needle+'<div style="position:absolute;right:18px;top:18px;width:32px;height:32px">'+icon(_ic).replace('class="icon"','class="icon" style="width:32px;height:32px;color:white;margin:0"')+'</div>')
pages[17]=ph(212,433,740,287,1).replace('background:#e7e7e7','background:rgba(220,220,220,.18)')+pages[17]
pages[18]=pages[18].replace('YOU ↗','YOU<span style="position:absolute;left:390px;top:92px"><svg width="60" height="60" viewBox="0 0 40 40"><path d="M4 36 36 4M13 4h23v23" fill="none" stroke="#363636" stroke-width="4"/></svg></span>')
css+=' .panel[style*="background:#e7e7e7"]>span{display:none}'
(R/'replica.css').write_text(css)''')
p.write_text(s)

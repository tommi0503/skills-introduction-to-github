from pathlib import Path
P=Path(__file__).parent
exec((P/'write_replica_fixtures.py').read_text().split('# Cards:')[0])
save('agenda',2,root('agenda','agenda',''.join('<div class="entry"><span class="mark">'+f'{j+1:02}'+'</span><b class="name">'+fresh(S[2][i]['text'][3:])+'</b><p class="note">'+txt(2,i+1)+'</p></div>' for j,i in enumerate(range(8,25,2)))),'12x5')
save('callout',28,root('callout','callout','<p>'+txt(28,57)+'</p>'),'12x2')
save('delta',20,group([root('delta','delta','<div class="from">'+txt(20,i)+'</div><div class="to">'+txt(20,i+2)+'</div>') for i in [12,19,26]],'stack'),'8x5')
save('delta',28,root('delta','delta','<div class="from">'+txt(28,20)+'</div><div class="to">'+txt(28,22)+'</div>'),'2x4')
def spoke(name,note,mark=''):
 return '<div class="spoke">'+('<span class="mark">'+mark+'</span>' if mark else '')+'<b class="name">'+name+'</b><div class="note">'+note+'</div></div>'
save('hub',10,root('hub','hub','<div class="core">'+photo(1,'avatar')+'<b class="name"></b></div>'+''.join(spoke(txt(10,i),txt(10,i+1),icon(ic)) for i,ic in zip([14,20,26],['folder-open','pencil','graduation-cap']))),'12x6')
save('hub',18,root('hub','hub','<div class="core">'+photo(1,'avatar')+'<b class="name">'+txt(18,9)+'</b><p class="note">'+txt(18,10)+'</p></div>'+''.join(spoke(txt(18,k),paragraphs([txt(18,i) for i in ids])) for k,ids in [(21,[16,17,18,19]),(32,[27,28,29,30]),(43,[38,39,40,41]),(54,[49,50,51,52])])),'12x6')
save('image-frame',27,group([root('image-frame','frame',photo(i+1)) for i in range(3)]),'12x3')
save('person',4,root('person','person',photo(1,'portrait')+'<b class="name">'+txt(4,10)+'</b><p class="note">'+txt(4,11)+'</p>'),'4x6')
save('person',29,root('person','people',''.join('<div class="person">'+photo(j+1)+'<b class="name">'+txt(29,i+1)+'</b><div class="note"><span>'+txt(29,i+3)+'</span></div></div>' for j,i in enumerate([10,14,18,22]))),'12x6')
head=['']+[txt(19,i) for i in [22,23,24]]
body='<table class="table"><thead><tr>'+''.join('<th>'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr><td>'+txt(19,i)+'</td>'+''.join('<td>'+txt(19,i+j)+'</td>' for j in [2,4,6])+'</tr>' for i in [26,34,42,50,58,66])+'</tbody></table>'
save('table',19,root('table','tablebox',body),'6x6')
ht=S[21][8]['html'];tm=re.search(r'<table\b.*?</table>',ht,re.S)
if tm:
 t=tm.group();t=re.sub(r' style="[^"]*"','',t);t=re.sub(r' class="[^"]*"','',t);t=t.replace('<table','<table class="table"',1)
 t=re.sub(r'>([^<>]+)<',lambda m:'>'+fresh(m.group(1))+'<' if m.group(1).strip() else m.group(),t)
 save('table',21,root('table','tablebox',t),'12x5')
else:print('NO table21')
save('legend',11,root('legend','legend','<span class="key tone-2">'+txt(11,23)+'</span><span class="key tone-1">'+txt(11,25)+'</span>'),'3x1')
save('legend',26,root('legend','legend',''.join('<span class="key tone-'+str(j+1)+'">'+txt(26,i)+'</span>' for j,i in enumerate([10,16,22,28]))),'12x1')
save('chart-donut',26,root('chart-donut','donuts',''.join('<div class="donut" style="--v:'+str(v)+'"><b class="fig">'+str(v)+'<small>%</small></b><p class="name"></p></div>' for v in [80,70,75,91])),'12x3')
print('9 mapped structure specimens complete')

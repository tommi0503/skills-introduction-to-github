from pathlib import Path
P=Path(__file__).parent
exec((P/'write_replica_fixtures.py').read_text().split('# Cards:')[0])
save('headline',12,group([root('headline','headline','<h2>'+txt(12,i)+'</h2>') for i in [16,18,20,22]]),'12x1')
save('prose',12,group([root('prose','prose quiet','<p>'+txt(12,i)+'</p>') for i in [17,19,21,23]]),'12x2')
save('hierarchy',15,root('hierarchy','org','<div class="root">'+txt(15,13)+'</div>'+''.join('<div class="branch"><div class="node"><b>'+txt(15,i)+'</b><span>'+txt(15,i+1)+'</span></div>'+''.join('<div class="leaf"><b>'+txt(15,j)+'</b><span>'+txt(15,j+1)+'</span></div>' for j in ids)+'</div>' for i,ids in [(15,[20,23,26]),(29,[34,37,40])])),'12x6')
save('hierarchy',28,root('hierarchy','org','<div class="root">'+txt(28,36)+'</div>'+''.join('<div class="branch"><div class="node">'+txt(28,i)+'</div></div>' for i in [51,53,55])),'3x3')
save('positioning',25,root('positioning','posmap','<div class="axis-x"><span></span><span>'+html.escape(S[25][18]['text'])+'</span></div><div class="axis-y"><span>'+html.escape(S[25][15]['text'])+'</span><span>'+html.escape(S[25][14]['text'])+'</span></div>'+''.join('<div class="mark'+(' on' if j==0 else '')+'" style="--x:'+str(x)+';--y:'+str(y)+'"><b class="name">'+txt(25,i)+'</b></div>' for j,(i,x,y) in enumerate([(35,87,93),(37,54,78),(39,75,62),(41,46,48)]))),'7x5')
save('timeline',23,root('timeline','track alt',''.join('<div class="stop"><div class="kick">'+txt(23,i+1)+'<span>'+txt(23,i+2)+'</span></div><b class="name">'+txt(23,i+3)+'</b><div class="note"><b>'+txt(23,i+6)+'</b>'+txt(23,i+7)+'</div></div>' for i in [8,16,24,32,40])),'12x6')
notes=[]
notes.append(lst(bullets(28,18))+root('delta','delta','<span class="from">'+txt(28,20)+'</span><span class="to">'+txt(28,22)+'</span>'))
notes.append(lst(bullets(28,26))+pill(txt(28,28))+pill(txt(28,30)))
notes.append(lst(bullets(28,34))+root('hierarchy','org','<div class="root">'+txt(28,36)+'</div>'+''.join('<div class="branch"><div class="node">'+txt(28,i)+'</div></div>' for i in [51,53,55])))
notes.append(lst(bullets(28,40))+pill(txt(28,42),'on')+pill(txt(28,44),'on'))
save('steps',28,root('steps','steps',''.join('<div class="step"><b class="mark"></b><b class="name">'+txt(28,i)+'</b><div class="note">'+note+'</div></div>' for i,note in zip([16,24,32,38],notes))),'12x6')
print('connected source fixtures complete')

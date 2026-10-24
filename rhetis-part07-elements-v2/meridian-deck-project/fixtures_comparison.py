from pathlib import Path
P=Path(__file__).parent
exec((P/'write_replica_fixtures.py').read_text().split('# Cards:')[0])
# The reference owns row categories and project columns as a comparison table.
rows=[]
rows.append('<tr><td>'+txt(17,10)+'</td>'+''.join('<td>'+txt(17,i)+'</td>' for i in [19,32,45])+'</tr>')
rows.append('<tr><td>'+txt(17,12)+'</td>'+''.join('<td>'+lst(bullets(17,i))+'</td>' for i in [21,34,47])+'</tr>')
vals=[[20,35,61],[25,65,80],[30,36,69]]
plots=[]
for vs in vals:plots.append(root('chart-line','lines',''.join('<div class="pt" style="--v:'+str(v)+'"><b></b><span>'+str(j+2)+'Q</span></div>' for j,v in enumerate(vs)),'--max:'+str(max(vs)*1.25)))
rows.append('<tr><td>'+txt(17,14)+'</td>'+''.join('<td>'+x+'</td>' for x in plots)+'</tr>')
body='<table class="table"><thead><tr><th></th>'+''.join('<th>'+txt(17,i)+'</th>' for i in [18,31,44])+'</tr></thead><tbody>'+''.join(rows)+'</tbody></table>'
save('table',17,root('table','tablebox',body),'12x5')
print('source17 comparison table specimen complete')

from pathlib import Path
import re
C=Path('/workspace/output/cyanloop')
def root(n):
 import json
 m=json.loads((C/'elements'/n/'element.json').read_text());tax=json.load(open('/workspace/work/reference/contract/taxonomy.json'));rs=next(x['roots'] for x in tax['contracts'] if x['id']==m['contract']);return ':is('+','.join('.'+r+f'[data-el="cyanloop-{n}"]' for r in rs)+')'
def app(n,t):p=C/'elements'/n/'element.css';p.write_text(p.read_text()+'\n'+t.replace('$',root(n))+'\n')
for p in (C/'elements').glob('*/element.css'):
 s=p.read_text().replace('color:var(--a1);','color:var(--a1-7);').replace('color:var(--a2);','color:var(--a2-7);').replace('color:var(--a3);','color:var(--a3-7);')
 s=s.replace('font-size:var(--type-24);font-weight:var(--name-weight)','font-size:var(--type-20);font-weight:var(--name-weight)').replace('font-size:var(--type-18);font-weight:var(--body-weight)','font-size:var(--type-16);font-weight:var(--body-weight)')
 # Padding and gaps are part of the shared 12/24 spacing ladder.
 p.write_text(s)
app('card','$.on .mark{background:var(--page);color:var(--a1-7);}')
app('radar','''$ .axis{width:min(30cqw,30cqh);} $ .series{inset:auto;left:50%;top:50%;width:min(60cqw,60cqh);height:min(60cqw,60cqh);transform:translate(-50%,-50%);} $::before{inset:auto;left:50%;top:50%;width:min(64cqw,64cqh);height:min(64cqw,64cqh);transform:translate(-50%,-50%);}
''')
app('heatmap','''$.calendar .row{flex:1;min-height:0;} $.calendar .cell{width:auto;max-width:100%;height:100%;min-height:0;aspect-ratio:1;justify-self:center;} $.calendar .heads{flex:0;font-size:var(--type-12);}''')
app('steps','''$.col{gap:var(--gap-sm);} $.col .step{padding:var(--gap-sm);column-gap:var(--gap-sm);row-gap:calc(var(--gap-sm) / 2);grid-template-columns:48px 1fr;} $.col .mark{width:48px;height:48px;font-size:var(--type-28);} $.col .name{font-size:var(--type-18);} $.col .note{font-size:var(--type-14);} @container(max-height:400px){$.col .name{font-size:var(--type-16);} $.col .note{font-size:var(--type-12);}}''')
app('timeline','''$.col{gap:var(--gap-sm);} $.col .stop{padding:var(--gap-sm) var(--pad);gap:calc(var(--gap-sm) / 2);} $.col .name{font-size:var(--type-18);} $.col .note{font-size:var(--type-14);} $.col .kick{font-size:var(--type-12);} @container(max-height:400px){$.col .name{font-size:var(--type-16);} $.col .note{font-size:var(--type-12);}}''')
app('architecture','''$ {padding:var(--gap-sm);gap:var(--gap-sm);} $ .layer{padding:calc(var(--gap-sm) / 2) var(--gap-sm);gap:var(--gap-sm);} $ .chip{padding:calc(var(--gap-sm) / 2) var(--gap-sm);font-size:var(--type-16);} $ .name{font-size:var(--type-18);} @container(max-height:320px){$ .name{font-size:var(--type-16);} $ .chip{font-size:var(--type-12);}}''')
app('bullet','''$.bullet{padding:var(--gap-sm);gap:calc(var(--gap-sm) / 2);} $ .fig{font-size:var(--type-28);} $ .name{font-size:var(--type-18);} $ .note{font-size:var(--type-14);} $.bullet::after{height:var(--gap-sm);} $.bullet::before{height:var(--gap);bottom:var(--gap-sm);} @container(max-height:140px){$ .note{display:none;} $ .name{font-size:var(--type-16);} $ .fig{font-size:var(--type-24);}}''')
app('gauge','''$ {padding:var(--gap-sm);gap:calc(var(--gap-sm) / 2);} $::after{height:var(--gap-sm);} $ .fig{font-size:var(--type-28);} $ .name{font-size:var(--type-18);} @container(max-height:140px){$ .name{font-size:var(--type-16);} $ .fig{font-size:var(--type-24);}}''')
app('delta','''$ {font-size:var(--type-40);} @container(max-height:130px){$ {font-size:var(--type-28);}}''')
app('headline','''$ {padding:var(--gap-sm);gap:var(--gap-sm);} @container(max-height:160px){$ h2,$.big h2{font-size:var(--type-32);} $ .note{font-size:var(--type-14);} $ .kick{display:none;}} @container(max-height:100px){$ h2,$.big h2{font-size:var(--type-24);} $ .note{display:none;}}''')
app('funnel','''$ .stage{padding:calc(var(--gap-sm) / 2) var(--gap-sm);} $ .name{font-size:var(--type-18);} $ .fig{font-size:var(--type-28);} @container(max-height:350px){$ .name{font-size:var(--type-16);} $ .fig{font-size:var(--type-22);}}''')
app('hierarchy','''$ {gap:var(--gap) var(--gap-sm);padding:var(--gap-sm);} $ .root{padding:var(--gap-sm);font-size:var(--type-22);} $ .node{padding:var(--gap-sm);font-size:var(--type-18);} $ .leaf{font-size:var(--type-16);padding:calc(var(--gap-sm) / 2);} @container(max-height:350px){$ .root{font-size:var(--type-18);} $ .node{font-size:var(--type-14);} $ .leaf{font-size:var(--type-12);} $ .branch{gap:calc(var(--gap-sm) / 2);}}''')
app('journey','''$ {padding:var(--gap-sm);} $ .stage{padding:var(--gap-sm);padding-top:var(--gap-lg);} $ .name{font-size:var(--type-18);} $ .note{font-size:var(--type-14);} @container(max-height:320px){$ .name{font-size:var(--type-16);} $ .note,$ .pain{font-size:var(--type-12);}}''')
app('list','''$ {gap:var(--gap-sm);} $ .item{gap:calc(var(--gap-sm) / 2);} $ .name{font-size:var(--type-18);} $ .note{font-size:var(--type-16);} @container(max-height:280px){$ .name{font-size:var(--type-16);} $ .note{font-size:var(--type-12);} $ .item{gap:0;}}''')
app('metric','''$.stats{gap:var(--gap-sm);} $.stats>.stat,$.stat:not(.stats){padding:var(--gap-sm);} $ .parts{gap:var(--gap-sm);} $ .fig{font-size:var(--type-64);} @container(max-height:230px){$ .parts{gap:calc(var(--gap-sm) / 2);} $ .fig{font-size:var(--type-36);} $ .name{font-size:var(--type-16);} $ .note{font-size:var(--type-12);}} @container(max-height:110px){$ .parts{gap:0;} $ .fig{font-size:var(--type-28);} $ .name{font-size:var(--type-14);} $ .note{display:none;}}''')
app('mindmap','''$ {gap:var(--gap-sm);padding:var(--gap-sm);} $ .branch{gap:calc(var(--gap-sm) / 2);padding:calc(var(--gap-sm) / 2);} $ .name{font-size:var(--type-18);} $ .leaf{font-size:var(--type-14);padding:calc(var(--gap-sm) / 2);} @container(max-height:400px){$ .name{font-size:var(--type-16);} $ .leaf{font-size:var(--type-12);}}''')
app('prose','''$.cols{column-fill:balance;} $.cols p{break-inside:auto;} @container(max-height:350px){$ p{font-size:var(--type-18);} $.lead p{font-size:var(--type-22);}}''')
app('sankey','''$ {gap:var(--gap);padding:var(--gap-sm);} $ .branch{padding:calc(var(--gap-sm) / 2) var(--gap-sm);} $ .name{font-size:var(--type-18);} $ .fig{font-size:var(--type-28);} @container(max-height:350px){$ .name{font-size:var(--type-14);} $ .fig{font-size:var(--type-22);}}''')
app('slope','''$ {gap:var(--gap-sm);padding:var(--gap-sm);} $ .heads{font-size:var(--type-14);} $ .pair .name{font-size:var(--type-16);} $ .pair b{font-size:var(--type-20);} @container(max-height:350px){$ .pair .name{font-size:var(--type-12);} $ .pair b{font-size:var(--type-16);}}''')
app('sparkline','''$ {height:64px;padding:calc(var(--gap-sm) / 2);} @container(max-height:200px){$ {height:40px;}}''')
app('table','''$ :is(th,td){padding:calc(var(--gap-sm) / 2);} @container(max-height:230px){$ .table{font-size:var(--type-12);}}''')
app('waffle','''$ {padding:var(--gap-sm);gap:var(--gap-sm);} $ .units{min-height:0;max-height:60%;gap:calc(var(--gap-sm) / 2);} $ .u{aspect-ratio:auto;min-height:0;} $ .fig{font-size:var(--type-36);} $ .name{font-size:var(--type-18);} @container(max-height:250px){$ .fig{font-size:var(--type-28);} $ .name{font-size:var(--type-14);} $ .units{height:45%;}}''')
# Tag fixture's running text is an enclosing prose item, and needs at least two body rows.
for p in (C/'elements/tag/fixtures').glob('*.html'):p.write_text(re.sub(r'<!-- min:.*?-->','<!-- min: 6x2 -->',p.read_text()))
# This is our declared usability floor rather than the sample collection's floor.
mins={'flowchart':{'flowchart-col':'5x5'},'matrix':{'swot':'8x5'},'steps':{'steps-col-4':'6x5'},'timeline':{'track-col-4':'6x5'},'heatmap':{'calendar-12':'8x5'},'prose':{'prose-cols':'9x4'},'sparkline':{'spark-in-stat':'6x3'}}
for name,fs in mins.items():
 for stem,minval in fs.items():
  p=C/'elements'/name/'fixtures'/(stem+'.html');p.write_text(re.sub(r'<!-- min:.*?-->',f'<!-- min: {minval} -->',p.read_text()))
# Meaningful Korean fixture copy for source placeholders, while canonical examples remain untouched.
for name in ['quote','tag']:
 for p in (C/'elements'/name/'fixtures').glob('*.html'):p.write_text(p.read_text().replace('TEXT HERE','김미리 교육원장'))

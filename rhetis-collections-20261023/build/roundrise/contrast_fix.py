from pathlib import Path
B=Path('/workspace/output/roundrise')
fixes={
'pill':'.pill[data-el="roundrise-pill"].on .mark{color:var(--a1-on)}',
'matrix':'.matrix[data-el="roundrise-matrix"]>.cell.on :is(.name,.note,.kick,.list){color:var(--a1-on)}',
'matrix-nine':'.grid9[data-el="roundrise-matrix-nine"]>.cell.on :is(.name,.note,.kick){color:var(--a1-on)}',
'pyramid':'.pyramid[data-el="roundrise-pyramid"]>.level:first-child :is(.name,.note){color:var(--a1-on)}',
'code':'.code[data-el="roundrise-code"] .s{color:var(--a3-7)}',
}
for k,s in fixes.items():
 p=B/f'elements/{k}/element.css';p.write_text(p.read_text()+s)
# Code has its own shared font token; its source lines remain monospaced.
import json
p=B/'kit/kit.json';j=json.loads(p.read_text());j['extensions']['--roundrise-font-code']='font';p.write_text(json.dumps(j,indent=2))
p=B/'kit/css/tokens.css';p.write_text(p.read_text()+"\n.slide{--roundrise-font-code:'Nanum Gothic Coding';}\n")
p=B/'elements/code/element.css';p.write_text(p.read_text()+'.code[data-el="roundrise-code"]>.lines{font-family:var(--roundrise-font-code)}')
for k,root in [('flowchart','flowchart'),('swimlane','swimlane')]:
 p=B/f'elements/{k}/element.css';p.write_text(p.read_text()+f'''.{root}[data-el="roundrise-{k}"]>.node.to-l:after{{content:'';position:absolute;left:calc(var(--gap-lg)*-1);right:auto;top:calc(50% - 4px);width:var(--gap-lg);height:8px;background:var(--a1);clip-path:polygon(100% 40%,20% 40%,20% 0,0 50%,20% 100%,20% 60%,100% 60%);}}.{root}[data-el="roundrise-{k}"]>.node.to-u:before{{content:'';position:absolute;top:calc(var(--gap-lg)*-1);bottom:auto;left:calc(50% - 4px);height:var(--gap-lg);width:8px;background:var(--a1);clip-path:polygon(40% 100%,60% 100%,60% 20%,100% 20%,50% 0,0 20%,40% 20%);}}''')

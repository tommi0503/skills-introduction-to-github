from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1];C=B/'collection/afterglow'
replace={'font-weight': {'300': 'var(--figure-weight)', '400': 'var(--weight-body)', '700': 'var(--title-weight)', '800': 'var(--afterglow-emphasis-weight)'}, 'line-height': {'1': 'var(--figure-line)', '1.2': 'var(--label-line)', '1.5': 'var(--body-line)', '1.65': 'var(--afterglow-contact-line)', '24px': 'var(--afterglow-copy-line)'}, 'letter-spacing': {'-.02em': 'var(--lead-track)', '.36px': 'var(--afterglow-section-track)', '-.8px': 'var(--afterglow-contents-track)', '-.5px': 'var(--afterglow-heading-track)', '0': 'var(--label-track-latin)'}}
for f in (C/'elements').glob('*/element.css'):
 t=f.read_text()
 for prop,vals in replace.items():
  for val,token in vals.items():t=re.sub(r'(?<![-\w])'+prop+r'\s*:\s*'+re.escape(val)+r'\s*(?=[;}])',prop+':'+token,t)
 f.write_text(t)
f=C/'kit/css/tokens.css';t=f.read_text().split('\n/* MEASURED TOKENS */')[0];f.write_text(t+'\n/* MEASURED TOKENS */\n.slide{--afterglow-emphasis-weight:800;--afterglow-contact-line:1.65;--afterglow-copy-line:1.4627659574;--afterglow-copy-track:0em;--afterglow-font-copy:Freesentation;--afterglow-section-track:.36px;--afterglow-contents-track:-.8px;--afterglow-heading-track:-.5px;}\n')
f=C/'kit/kit.json';j=json.loads(f.read_text());j['extensions'].update({'--afterglow-emphasis-weight': 'weight', '--afterglow-contact-line': 'number', '--afterglow-copy-line': 'number', '--afterglow-section-track': 'tracking', '--afterglow-contents-track': 'tracking', '--afterglow-heading-track': 'tracking', '--afterglow-copy-track': 'tracking', '--afterglow-font-copy': 'font'});f.write_text(json.dumps(j,ensure_ascii=False,indent=2))

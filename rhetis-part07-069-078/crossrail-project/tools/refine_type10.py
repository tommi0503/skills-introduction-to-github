from pathlib import Path
p=Path(__file__).parent;c=p/'crossrail'
f=c/'kit/css/tokens.css';f.write_text(f.read_text()+"\n.slide{--font-display:'Noto Sans KR';--font-body:'Noto Sans KR';--title-track:-0.015em;--body-track:-0.6px;--body-line:1.22;--label-line:1.34}\n")
f=c/'foundation/foundation.css';f.write_text(f.read_text()+'\n.slide:not(.cover) .kicker{line-height:var(--label-line)}.slide:not(.cover) .no{right:calc(var(--gap-sm)*-11/6)}\n')
f=c/'elements/headline/element.css';f.write_text(f.read_text()+'\n[data-el="crossrail-headline"]:not(.big) h2{font-size:var(--type-26);line-height:var(--name-line)}\n')
f=c/'elements/steps/element.css';s='[data-el="crossrail-steps"]:has(.name>.icon):not(.col)';f.write_text(f.read_text()+f'\n{s} .name{{font-size:var(--type-26)}}{s} .note{{margin-top:calc(var(--gap) - 1px);letter-spacing:calc(var(--body-track)*1.5)}}\n')
# Independent replicas load the same measured source font, including its actual weight range.
f=p/'replica/replica.css';s=f.read_text();s=s.replace("@font-face{font-family:'Pretendard Variable';src:url('../assets/fonts/artifacts/pretendard/PretendardVariable.woff2');font-weight:100 900;font-style:normal}","@font-face{font-family:'Noto Sans KR';src:url('../assets/fonts/artifacts/noto-sans-kr/NotoSansKR.woff2');font-weight:100 900;font-style:normal}")
s=s.replace("font-family:'Pretendard Variable',sans-serif","font-family:'Noto Sans KR',sans-serif");f.write_text(s)

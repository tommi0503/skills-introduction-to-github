from pathlib import Path
import json
B=Path(__file__).resolve().parent.parent;C=B/'anchor-frame';R=B/'anchor-frame-review'
styles=(C/'kit/css/tokens.css').read_text()+(C/'foundation/foundation.css').read_text()+''.join(p.read_text() for p in (C/'elements').glob('*/element.css'))
steps=json.load(open('/workspace/work/ref/contract/type-steps.json'));palette=json.load(open('/workspace/work/ref/contract/palette.json'))
styles+=' .slide{'+''.join(f'--type-{n}:{n}px;' for n in steps)+''.join(f'{k}:{v};' for k,v in palette['light'].items())+'}'
styles+=' .slide{--page:#ffffff;--ink:#000000;--n-1:#ededed;--n-7:#808080;--a1:#2861e3;--a1-7:#2861e3;--a1-on:#ffffff;--a1-3-muted:#8ca8e2;}'
markup='''<section class="slide"><div class="page"><div class="body"><div class="headline" data-el="anchor-frame-headline" style="grid-column:1 / span 8;grid-row:1 / span 1"><h2>BUSINESS PROPOSAL</h2></div><div class="headline big" data-el="anchor-frame-headline" style="grid-column:1 / span 9;grid-row:2 / span 3"><h2><b>비즈니스 프로젝트 제안</b>프레젠테이션</h2></div><div class="prose" data-el="anchor-frame-prose" style="grid-column:1 / span 8;grid-row:4 / span 1"><p>고객의 문제를 해결하는 전략과 실행 방안을 체계적으로 제안합니다.</p></div><div class="prose quiet" data-el="anchor-frame-prose" style="grid-column:1 / span 4;grid-row:6 / span 1"><p>MIRI COMPANY<br>email@email.com</p></div><div class="frame" data-el="anchor-frame-image-frame" style="grid-column:10 / span 3;grid-row:1 / span 5"><div class="seat" data-ph="1"></div></div><div class="frame" data-el="anchor-frame-image-frame" style="grid-column:9 / span 4;grid-row:5 / span 2"><div class="seat" data-ph="2"></div></div></div></div></section>'''
(R/'reassembled').mkdir(exist_ok=True)
(R/'reassembled/slide_01.html').write_text('<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="../../fonts/fonts.css"><style>body{margin:0}'+styles+'</style>'+markup)

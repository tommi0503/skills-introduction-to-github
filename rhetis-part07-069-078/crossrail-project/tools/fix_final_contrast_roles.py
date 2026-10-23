from pathlib import Path
P=Path(__file__).parent;E=P/'crossrail/elements'
# Change text/surface palette roles only. Source geometry and all fixtures stay frozen.
f=P/'crossrail/foundation/foundation.css';s=f.read_text();s=s.replace('color:var(--n-5);letter-spacing:var(--body-track)','color:var(--n-7);letter-spacing:var(--body-track)');s+='\n.slide:not(.cover) .head>.kicker{color:var(--n-7)}.slide.cover .lockup.at-top-left>.kicker,.slide.cover .lockup.at-left>.kicker{color:var(--n-1)}\n';f.write_text(s)
for el in ['hub','legend','pill']:
 f=E/el/'element.css';s=f.read_text().replace('color:var(--n-5)','color:var(--n-7)');f.write_text(s)
f=E/'card/element.css';s=f.read_text();s=s.replace('color:var(--n-3);margin-inline','color:var(--n-7);margin-inline').replace(' .fig{color:var(--n-5)}',' .fig{color:var(--n-7)}');f.write_text(s)
f=E/'headline/element.css';f.write_text(f.read_text()+'\n[data-el="crossrail-headline"].on .note{color:var(--a1-on)}\n')
f=E/'roadmap/element.css';s=f.read_text().replace('background:var(--n-5);color:var(--page)','background:var(--n-7);color:var(--page)');f.write_text(s)
f=E/'table/element.css';s=f.read_text().replace('th:first-child{color:var(--warn)!important}','th:first-child{color:var(--bad)!important}');f.write_text(s)
# External source palette maps those roles back to the original source's deliberately subdued text.
f=P/'assets/source-palette.css';f.write_text(f.read_text()+'''\n/* Source-only palette-role remapping. This provider contains no geometry or type rules. */
.slide:not(.cover) .head>.kicker{--n-7:var(--n-5)}
.slide.cover .lockup>.kicker{--n-1:var(--a1-5)}
.slide [data-el="crossrail-card"].quiet .kick{--n-7:var(--n-3)}
.slide [data-el="crossrail-card"].quiet.on:first-child .fig{--n-7:var(--n-5)}
.slide [data-el="crossrail-hub"] .core small{--n-7:var(--n-5)}
.slide [data-el="crossrail-legend"] .key>b{--n-7:var(--n-5)}
.slide [data-el="crossrail-pill"] .name{--n-7:var(--n-5)}
.slide [data-el="crossrail-roadmap"] .bar{--n-7:var(--n-5)}
.slide [data-el="crossrail-table"] th:first-child{--bad:var(--warn)}
''')
f=P/'review-notes.md';f.write_text(f.read_text()+'''\n## 마지막 대비 역할 보정\n\n최소 칸의 실제 대비 검사에서 발견한 kicker·quiet kick·hub 보조어·legend 비중·pill 이름의 옅은 text 역할은 n7로 높였다. on headline의 note는 a1-on을 상속하며, roadmap의 일반 막대 면과 달력 일요일도 기준 팔레트에서 읽히는 역할로 교정했다. 원본의 의도적인 낮은 대비는 외부 source-palette에서 색 변수의 역할만 다시 매핑하여 보존하며 기하·폰트·fixture는 바꾸지 않았다. 주석형 막대 축은 별도 sibling이 그린 진한 패널 위에 겹쳐 있으므로 조상 배경만 보는 대비 탐지의1:1 후보와 실제 화면을 구분한다.\n''')

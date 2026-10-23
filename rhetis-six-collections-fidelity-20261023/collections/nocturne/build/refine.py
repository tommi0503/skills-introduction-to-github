from pathlib import Path
import re,json
C=Path('/workspace/work/deliverables/nocturne/collection/nocturne')
required={'card':{'card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone'},'callout':{'callout','callout-icon','callout-stack'},'chart-area':{'area-1','areas-2','areas-stacked-3','area-3pt'},'chart-bar':{'bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2'},'chart-donut':{'donut','donuts-3','donuts-4','donut-0','donut-100'},'chart-line':{'lines-12','lines-6','lines-3','lines-flat'}}
for name,names in required.items():
 for p in (C/'elements'/name/'fixtures').glob('*.html'):
  if p.stem not in names:p.unlink()
for p in C.glob('elements/*/fixtures/*.html'):
 if p.parent.parent.name in required:continue
 s=p.read_text();minimum='10x5' if p.parent.parent.name in ['decision-tree','mindmap','matrix-nine','network','roadmap','swimlane','radar','balance'] else '8x4'
 s=re.sub(r'<!-- min: [^>]+ -->',f'<!-- min: {minimum} -->',s,count=1);p.write_text(s)
# Full boxes are content-sized in vertical fixture stacks; otherwise cards can collapse to a text baseline.
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'.slide .stack{justify-content:center}.slide .stack>.seat{flex:1;align-self:center;max-height:70%;width:auto}.slide .stack>[data-el]{flex:1;min-height:64px}\n')
def patch(name,css):
 p=C/'elements'/name/'element.css';p.write_text(p.read_text()+css.replace('R',f'[data-el="nocturne-{name}"]')+'\n')
patch('chart-line','''R .pt::before{background:linear-gradient(to top right,transparent calc(50% - 1px),var(--a1) calc(50% - 1px),var(--a1) calc(50% + 1px),transparent calc(50% + 1px))}R .pt::after{background:linear-gradient(to bottom right,transparent calc(50% - 1px),var(--a1) calc(50% - 1px),var(--a1) calc(50% + 1px),transparent calc(50% + 1px))}''')
patch('chart-donut','''R.donuts{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(150px,100%),1fr));grid-auto-rows:minmax(0,1fr)}R.donut::before{width:min(85cqw,calc(100cqh - var(--type-100)))}R.donut .fig{position:absolute;left:50%;top:calc(var(--gap-sm) + min(85cqw,calc(100cqh - var(--type-100)))/2);transform:translate(-50%,-50%);margin:0;white-space:nowrap}R.donut .name{min-height:0;margin-top:auto;margin-bottom:0;max-width:100%;font-size:var(--type-22)}@container(max-height:200px){R.donut::before{width:min(85cqw,calc(100cqh - var(--type-60)))}R.donut .fig{top:calc(var(--gap-sm) + min(85cqw,calc(100cqh - var(--type-60)))/2);font-size:var(--type-28)}R.donut .name{font-size:var(--type-14)}}''')
# Protect fig/name in minimal readable inline allocations.
patch('delta','''@container(max-width:400px){R .from,R .to{font-size:var(--type-24)}}''')
patch('cycle','''R::after{content:'';position:absolute;right:18%;top:42%;width:12px;height:12px;border-right:2px solid var(--n-4);border-bottom:2px solid var(--n-4);transform:rotate(45deg)}''')
# Record exact-fixture exceptions and intentional minimums.
r=C.parents[1]/'review/review-notes.md'
r.write_text(r.read_text()+'''\n## 컬렉션 1차 검수 및 수정\n- 56개 요소를 독립 CSS로 작성. 예시에서는 구조·데이터 fixture만 재사용했으며 디자인 CSS는 복사하지 않았다.\n- 지정 모범 fixture의 원래 배치·래퍼 및 아이콘 문자는 동일 마크업·데이터 우선 규칙에 따라 보존했다. 따라서 모범 fixture의 일부는 일반 fixture의 12×6 배치 규칙과 다르다.\n- 그 밖의 복합 요소는 여러 멤버가 하나의 최소 칸을 공유하므로 8×4 또는 복잡도에 따라 10×5를 최소로 선언했다.\n- 첫 라이트 시트에서 작은 4도넛 fixture의 수치 줄바꿈을 발견해 자동 2열 배열과 고정 중앙 수치 배치를 적용. 라인 차트 배경의 불필요한 불투명 사각형을 제거.\n- 사진 placeholder의 명암 변화는 원본과 다르며 사용자 placeholder 지시에 따른 차이다.\n''')
print('Refined source')

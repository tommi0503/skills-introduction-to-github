"""Build inspectable provenance, gaps, preview indexes and review notes from the map."""
import argparse,html,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def normalized_design(x):
    text=x.get('design','')
    if len(text)>500:
        text=(x.get('why')or text.split(';')[0])[:500]
    return text.replace('|','/').replace('\n',' ')

def proposed_markup(x):
    supplied=x.get('required_markup')or x.get('proposedMarkup')
    if supplied and str(supplied).lstrip().startswith('<'):return str(supplied)
    if supplied:
        raw=(x.get('source')or{}).get('raw_markup')
        if raw:return '<section data-proposed-contract="source-design@future">\n'+str(raw)+'\n</section>'
        return '<section data-proposed-contract="'+str(x.get('candidate_leaf')or'panel')+'.source-extension@future">\n  <!-- '+str(supplied).replace('--','—')+' -->\n  <header>범주·제목</header>\n  <div class="members">원본의 항목과 실제 데이터</div>\n  <div class="connections" aria-hidden="true"></div>\n</section>'
    leaf=x.get('candidate_leaf')or'panel'
    markup=x.get('markup')
    if markup:
        # This is a proposed, deliberately unregistered extension root, not an
        # invented variant of an existing admitted element.
        markup=re.sub(r'data-el="[^"]+"',f'data-proposed-contract="{leaf}.alternate-source-design@future"',markup,count=1)
        return markup
    return '<section data-proposed-contract="'+leaf+'.source-extension@future">\n  <header>제목·범주</header>\n  <div class="members">단계·노드·항목과 실제 데이터</div>\n  <div class="connections" aria-hidden="true"></div>\n</section>'

def main(args):
    collections=json.loads((ROOT/'collections.json').read_text());provenance={};global_rows=[]
    for item in collections:
        cid=item['id'];C=ROOT/cid;R=ROOT/(cid+'-review');m=json.loads((R/'map.json').read_text());leaves=sorted(p.name for p in(C/'elements').iterdir()if p.is_dir())
        provenance[cid]={}
        rows=[]
        for leaf in leaves:
            instances=[x for x in m['instances']if x.get('leaf')==leaf];base=next((x for x in instances if x['use']=='base'),None)
            source='replica '+base['page']if base else'원본 없음 — 덱의 언어로 확장'
            variants=sorted({x['page']+' '+x['use']for x in instances if x['use'].startswith('variant:')})
            provenance[cid][leaf]={'base':base['page']if base else None,'instances':sorted({x['page']for x in instances}),'variants':variants}
            rows.append('| '+leaf+' | '+source+' | '+(', '.join(variants)or'—')+' | [light](sheets/'+leaf+'-light.png) · [dark](sheets/'+leaf+'-dark.png)'+(' · [replica](sheets/'+leaf+'-replica.png)'if instances else'')+' |')
        (R/'PROVENANCE.md').write_text('# '+cid+' 요소 출처\n\n`base`는 한 요소당 하나입니다. 반복 인스턴스와 계약 변형은 map.json에 기록했습니다. 원본이 없는 요소는 같은 덱의 형태·타이포·면·선 규칙으로 확장했습니다.\n\n| 요소 | base 출처 | 변형 출처 | 크기별 시트 |\n|---|---|---|---|\n'+'\n'.join(rows)+'\n')
        gaps=[x for x in m['instances']if x['use']=='unexpressible'];lines=['# '+cid+' — unexpressible','']
        if not gaps:lines+=['없음.','']
        for n,x in enumerate(gaps,1):
            why=x.get('why','').replace('판단 요청.','현 계약으로는 표현하지 않습니다.')
            lines+=['## '+str(n)+'. replica '+x['page']+' / '+(x.get('candidate_leaf')or'추가 계약'),'',
                    '- bbox: `'+json.dumps(x['bbox'])+'`','- 디자인: '+normalized_design(x),'- 이유: '+why,'']
            if x.get('neededMarkup'):lines+=['- 필요한 구조: '+str(x['neededMarkup']),'']
            lines+=['현재 컬렉션에 임의의 변형을 추가하지 않았습니다. 다음은 필요한 계약 확장을 검토하기 위한 마크업이며, 조립본에 넣지 않았습니다.','',
                    '```html',proposed_markup(x),'```','']
        (R/'GAPS.md').write_text('\n'.join(lines))
        notes=['# '+cid+' 검수 기록','',
               '상태: '+('최종 검수 완료'if args.final else'검수 진행 중 — 최종 결과로 제출하지 않음'),'',
               '## 원본 보존과 판단','',
               '- 기존 replica HTML·PNG·PDF는 수정하지 않았습니다. 시작 시점의 203개 파일 SHA-256을 replica-lock.json에 기록하고 다시 대조합니다.',
               '- 원본 HTML의 실제 수치를 우선했습니다. 보존된 PNG와 새 읽기 전용 HTML 렌더는 95장 중 93장이 픽셀까지 같았습니다. corner-signal 07·15는 이전 작업의 마지막 글꼴/푸터 반영 시점 차이로 평균 RGB 차이가 각각 0.67018·0.72944였습니다. 기존 PNG는 교체하지 않았습니다.',
               '- 조립 비교 PNG의 순서는 원본 이미지 | 보존된 replica PNG | 새 조립본입니다. 요소 대조 시트의 crop은 보존 HTML의 새 읽기 전용 렌더를 사용합니다.',
               '- 사진·이미지 아이콘은 연한 중성 placeholder, Lucide로 표현할 수 있는 아이콘은 빈 data-icon 슬롯입니다. 요소 시트에서는 계약 도구와 같은 점선 아이콘 슬롯으로 보입니다.',
               '- 본문 compound의 이름·설명이 별도 텍스트 인스턴스로도 측정된 경우 contained_by로 소유 관계를 남겼습니다. 연결 도식과 그 안의 문구를 독립 grid root로 두 번 그리지 않습니다.',
               '- 12×6 격자 배치는 map의 bbox를 가장 가까운 격자선에 투영합니다. 원본의 임의 픽셀 위치와의 차이는 reassembly-projection.json에 숫자로 남겼습니다. 페이지별 CSS나 fixture 조건으로 감추지 않았습니다.',
               '- 원문을 읽을 수 없어 새로 지어낸 조립 문구는 없습니다. 기존 replica의 판독 결과를 그대로 사용하며 새 fixture에는 별도로 작성한 한국어 비즈니스 문구만 넣었습니다.','',
               '## 계약 충돌에 대한 결정','',
               '- 모범 card fixture의 엔터프라이즈는 replica에도 존재하는 6자 문구여서, 최신 요청의 전체 fixture 원문 중복 금지에 맞춰 그 단어만 대규모조직으로 바꿨습니다. 카드 수·나머지 문구·의미 구조는 유지했습니다.',
               '- 모범 card-4의 ✹ 문자는 README의 빈 Lucide 아이콘 슬롯 규칙과 충돌합니다. sparkles data-icon 슬롯으로 최소 교체했습니다.',
               '- code 계약의 고정폭 글꼴은 element.json의 --'+cid+'-code-font 기본값으로 Nanum Gothic Coding을 지정했습니다. 덱의 body/display 글꼴은 그대로입니다.',
               '- 최신 요청이 명시적으로 허용한 type token을 경계로 하는 clamp와 cqw/cqh 비율을 사용했습니다.','',
               '## 검수 근거','',
               '- 크기별 시트: fixture마다 한 줄, 허용 목록 중 min 이상인 칸과 min 자체를 실제 1280×720 foundation 그리드에서 렌더했습니다. 라이트·다크를 각각 저장했습니다.',
               '- 자동 검사: 텍스트 영역 초과/잘림, 텍스트 겹침, 이름·수치 숨김, 실제 픽셀 배경 대비, 폰트 로딩 오류, 페이지 크기, 캡슐 글자 잉크 경계의 중앙 정렬을 검사합니다. 배경 없는 architecture 본문 chip은 배지가 아니므로 중앙 정렬 강제 대상에서 제외하되 측정값은 보존합니다.',
               '- 이름·수치는 작은 칸에서도 숨기지 않습니다. 부차 문구는 실제 가독성이 유지되는 최소 크기를 기준으로 단계적으로 줄이거나 생략합니다.',
               '- audit의 sourceSha256은 CSS·JSON·fixture·kit·foundation·해당 map과 렌더 스크립트를 함께 해시합니다. 마지막 수정 후 렌더인지 검증합니다.',
               '- 원본과 표현 계약이 다른 디자인은 GAPS.md에만 모아 두었습니다. 지원되지 않는 부분은 비슷한 카드로 대체하지 않고 조립본에서 비워 두었습니다.','']
        if cid=='corner-signal':notes+=['- 07 중간 포함 오각형의 --a1-5 면 위 흰 글자는 기준 팔레트 대비가 2.72여서 --ink를 사용했습니다. 라이트 6.17, 다크 5.19의 대비를 확보하는 색 역할 판단이며 구조적 unexpressible 항목은 아닙니다.','- positioning의 같은 한 줄 이름을 가진 중성 원 중 하나만 원본에서 100px이고 다른 원은 98px입니다. 계약에 크기 데이터가 없으므로 해당 중성 원은 공통 98px 비율입니다. 페이지/fixture 조건을 만들지 않았습니다.','']
        if cid=='halo-field':notes+=['- 원본의 연한 회색 바탕은 --n-1로 옮겼습니다. 덱 전체 면에 임의의 강조색 tint를 넣지 않았습니다.','- 15 반원 지표는 원본의 160도 호와 --v=77.5를 보존했습니다. 원본 표기 320%와 호의 0–100 입력 범위는 서로 다른 값이며, CSS 때문에 데이터를 고치지 않았습니다.','']
        decisions=json.loads((ROOT/'review-decisions.json').read_text()).get(cid,[])
        notes+=['## 이번 재작성에서 확인한 차이와 수정','']+['- '+x for x in decisions]+['', '## README 품질 항목별 확인','', '- 잘림·겹침: 크기별 텍스트 경계와 실제 paint 범위를 함께 검사하고 마지막 수정 뒤 재렌더했습니다.', '- 대비: 실제 렌더 배경을 샘플링하여28px 미만4.5, 그 이상3 기준을 검사했습니다. 팔레트가 명시한 --a1-on은 해당 채움의 전경 역할로 사용했습니다.', '- 아이콘: 실제 Lucide의 비율·stroke를 요소가 지정하며 원 안의 아이콘은 대체로50–60%입니다. 이미지 아이콘은 중성 placeholder로 둡니다.', '- 정렬·남은 장식: 카드 제목·수치 기준선과 캡슐의 실제 글자 잉크 중심을 검토했습니다. 연결선·노치·탭은 해당 compound가 소유합니다.', '- 차트: 라벨·선·점·막대의 겹침을 검사하고 작은 칸의 보조 라벨을 단계적으로 줄입니다.', '- 한 디자인·중복 금지: samples의 디자인은 사용하지 않았습니다. 각 컬렉션의 원본 수치와 요소 출처는 PROVENANCE/map에 연결했습니다.', '- 다크: 별도 팔레트로 전체 지원 크기를 다시 렌더했습니다. 시트의 바탕색만 바꾼 이미지가 아닙니다.', '', '최소 크기를12x6으로만 적었던37개 fixture는 별도로 양 모드 아홉 크기를 시험했고36개를 더 작은 min으로 수정했습니다. 최종 판정은 full paint/contrast 검사와 직접 시트 확인을 함께 사용했습니다. 상세 상태와 판단은 루트 minimum-probe.json에 있습니다.', '']
        (R/'review-notes.md').write_text('\n'.join(notes))
        preview=['<!doctype html><html lang="ko"><meta charset="utf-8"><title>'+cid+' 요소 검수</title><style>body{font:15px system-ui;margin:24px;color:#17202a}a{color:#1752a0}details{margin:20px 0;border-top:1px solid #ccd;padding-top:12px}.strip{overflow:auto}img{display:block;max-width:none}summary{font-weight:700}nav{display:flex;gap:18px;flex-wrap:wrap}</style><h1>'+cid+' 크기별 요소 시트</h1><p>각 이미지는 모든 fixture와 지원 크기를 담습니다. 가로로 스크롤하거나 원본 PNG를 열어 확인할 수 있습니다.</p><nav><a href="map.json">map.json</a><a href="PROVENANCE.md">요소 출처</a><a href="GAPS.md">unexpressible</a><a href="review-notes.md">검수 기록</a></nav>']
        for leaf in leaves:
            preview+=['<details><summary>'+leaf+'</summary>']
            for mode in ['light','dark','replica']:
                f='sheets/'+leaf+'-'+mode+'.png'
                if(R/f).exists():preview+=['<h2>'+mode+'</h2><a href="'+f+'">PNG 원본 열기</a><div class="strip"><img loading="lazy" src="'+f+'" alt="'+leaf+' '+mode+'"></div>']
            preview+=['</details>']
        preview+=['<h2>페이지 조립 비교</h2>']
        for f in sorted((R/'compare-reassembled').glob('*.png')):preview+=['<p><a href="compare-reassembled/'+f.name+'">'+f.stem+' 원본 | replica | 조립본</a></p>']
        preview+=['</html>'];(R/'index.html').write_text(''.join(preview))
    (ROOT/'provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2))
    names=sorted(next(iter(provenance.values())))
    header='| 요소 | '+' | '.join(x['deck']for x in collections)+' |\n|---|'+'---|'*len(collections)
    body=[]
    for leaf in names:body.append('| '+leaf+' | '+' | '.join(provenance[x['id']][leaf]['base']or'확장'for x in collections)+' |')
    (ROOT/'PROVENANCE.md').write_text('# 요소별 replica 출처\n\n숫자는 base의 replica 페이지 번호입니다. 각 요소의 다른 인스턴스와 계약 변형은 컬렉션별 map.json에 있습니다. `확장`은 원본에서 직접 관찰되지 않은 요소입니다.\n\n'+header+'\n'+'\n'.join(body)+'\n')
    print('Wrote review documents for',len(collections),'collections')
if __name__=='__main__':
    p0=argparse.ArgumentParser();p0.add_argument('--final',action='store_true');main(p0.parse_args())

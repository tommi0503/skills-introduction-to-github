"""Copy scoped QA evidence and merge review notes; never edit render inputs."""
from pathlib import Path
import argparse, datetime, hashlib, json, re, shutil
from audit_css import BASE, COLLECTIONS

START='<!-- BEGIN FINAL QUALITY REVIEW -->'
END='<!-- END FINAL QUALITY REVIEW -->'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def snapshot(root):
    return {str(p.relative_to(root)):sha(p) for p in sorted(root.rglob('*')) if p.is_file()}
def tree(files):return hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def escape(s):return str(s).replace('|','\\|').replace('\n','<br>')
def freshness(info):
    values=[]
    for k,v in info.items():
        if k.startswith('matchesCurrent'):
            values.extend(v.values() if isinstance(v,dict) else [v])
    return 'current' if values and all(values) else 'historical' if values else 'unversioned'
def report_summary(name,d):
    if name.endswith('-audit.json') and isinstance(d,dict) and 'summary' in d:
        s=d['summary'];return f"오류{s.get('error',0)}, 경고{s.get('warning',0)}, 불완전{s.get('incomplete',0)}"
    if 'code-font' in name and isinstance(d,list):
        return '실로드·등폭 통과' if d and all(r.get('fontStatus') and r.get('monospaced') for r in d) else '원시 보고서 확인'
    if isinstance(d,dict) and 'clippedTextRuns' in d:return f"실제 text clip {d['clippedTextRuns']} (검사 당시 범위)"
    if isinstance(d,dict) and all(m in d for m in ['light','dark']) and 'candidates' in d['light']:
        return '대비 후보 light '+str(len(d['light']['candidates']))+' / dark '+str(len(d['dark']['candidates']))
    if isinstance(d,dict) and 'counts' in d and 'testedTypes' in d:return '기능 원시 후보 '+', '.join(f'{k}={v}' for k,v in d['counts'].items())
    if isinstance(d,dict) and d.get('passed') is True:return '해당 최종 후속 범위 통과'
    if isinstance(d,dict) and d.get('sourceUnchanged') is True:return '검사 중 소스 불변 확인; 상세 범위 참조'
    return '원시 결과·검사 범위 참조'

parser=argparse.ArgumentParser();parser.add_argument('collections',nargs='*');args=parser.parse_args()
manifest=json.loads((BASE/'qa/final-source-manifest.json').read_text())
generated=datetime.datetime.now(datetime.timezone.utc).isoformat()
for kid in args.collections or COLLECTIONS:
    project=BASE/(kid+'-project');collection=project/kid
    before=snapshot(collection);info=manifest['collections'][kid]
    if tree(before)!=info['sourceTreeSha256']:raise SystemExit(f'{kid}: manifest does not match frozen source')
    out=project/'quality';out.mkdir(exist_ok=True)
    reports=out/'reports';reports.mkdir(exist_ok=True)
    history=out/'history';history.mkdir(exist_ok=True)
    evidence=out/'evidence';evidence.mkdir(exist_ok=True)
    rows=[];copied=[]
    for source in sorted((BASE/'qa').glob(kid+'-*')):
        if source.suffix not in ['.json','.md']:continue
        suffix=source.stem[len(kid)+1:]
        auditinfo=info['audits'].get(suffix,{})
        state=freshness(auditinfo)
        if source.suffix=='.md':state='historical'
        dest=(history if state=='historical' else reports)/source.name
        shutil.copy2(source,dest);copied.append(str(dest.relative_to(out)))
        data=json.loads(source.read_text()) if source.suffix=='.json' else {}
        label={'current':'현재 소스와 해시 일치','historical':'과거 스냅샷','unversioned':'개별 해시 미기재·원시 실행 증거'}[state]
        summary=report_summary(source.name,data) if source.suffix=='.json' else '과거 진단 요약; 최종 통과 판정에 단독 사용하지 않음'
        rows.append(f'| [{source.name}]({dest.relative_to(out)}) | {label} | {escape(summary)} |')
    scope={'status':'Technical checks and per-page fidelity review are separate; no pixel identity claim.',
           'generatedAtUtc':generated,'collection':kid,'sourceTreeSha256':tree(before),
           'collectionSnapshot':info,'auditToolSha256':manifest['auditToolSha256']}
    (out/'source-manifest.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2)+'\n')
    shutil.copy2(BASE/'qa/FINAL-QA-STATUS.md',out/'integration-audit-history.md')
    if kid=='meridian-deck':shutil.copy2(BASE/'qa/meridian-tail-review.md',out/'meridian-tail-review.md')
    names={
      'seedmark':['072-pill-stack.png','072-bubble-5.png'],
      'crossrail':['crossrail-bars-annotated-light.png','crossrail-bars-annotated-dark.png','crossrail-pyramid5-min.png','073-logos-6.png','crossrail-source15-final.png']+[p.name for p in (BASE/'qa').glob('crossrail-photo-rule-*.png')],
      'onboard-docket':['078-agenda-3.png','078-three-icon-circles-source.png']}.get(kid,[])
    for name in names:
        p=BASE/'qa'/name
        if p.exists():shutil.copy2(p,evidence/name)
    primary=project/'fidelity/primary-review.json'
    review=json.loads(primary.read_text())
    shutil.copy2(primary,out/'primary-review.json')
    page_rows=[]
    for page,r in sorted(review['pages'].items()):
        page_rows.append(f"| {page} | 검토 기록 있음 ({escape(r.get('status',''))}) | {escape(r.get('notes',''))} |")
    page_table='| 페이지 | 검토 상태 | 최종 개별 대조 메모·남은 차이 |\n|---|---|---|\n'+'\n'.join(page_rows)
    primary_md='# 최종 개별 페이지 대조 기록\n\n원본·replica·조립본의 주 에이전트 개별 대조 메모를 그대로 옮겼다. `accepted`는 해당 검토 기록의 상태이며 원본과 100% 픽셀 동일하다는 뜻이 아니다. 비교 PNG 해시와 검토 시각은 `primary-review.json`에 보존했다.\n\n'+page_table+'\n'
    (out/'primary-review.md').write_text(primary_md)
    intro=f'''# {kid} 검수 보고서

생성 시각: {generated}  
최종 컬렉션 SHA-256: `{tree(before)}`

정적 계약, 실제 글꼴 로딩·코드 등폭 측정, 대비, 실제 overflow clipping, 선택한 의미·그래픽 검사에서 확인한 통과와 원본 시각 동일성은 별개다. 이 결과는 원본과 100% 동일하다는 판정이 아니다. 요소·크기·모드·예외의 구체적인 검사 범위는 각 JSON과 아래 스냅샷 상태를 따른다.

사진·복잡한 일러스트·래스터 아이콘·기기 화면 등은 요청대로 연한 회색 placeholder로 대체했다. 단순 도형·표·차트는 구현했고 가능한 선화 아이콘은 Lucide로 대체했다. 이 허용 대체와 별개로, 원본 글꼴을 식별할 수 없어 선택한 실제 로드 글꼴의 획·폭·행간, 일부 줄바꿈·미세 좌표·테두리 차이가 남는다. 페이지별 차이는 [개별 대조 메모](primary-review.md)에서 확인할 수 있다.

`현재 소스와 해시 일치`는 해당 보고서의 검사 입력과 현재 입력이 같다는 뜻이다. `과거 스냅샷`은 수정 전 보고서이며 현재 통과로 바꿔 표시하지 않았다. 소스 전용 최종 변경은 해당 구성의 별도 후속 보고서로 검증했다. 개별 해시가 없는 font/CSS 지원 등의 원시 실행 증거도 최신 소스 전체의 포괄 통과로 확대하지 않는다. gradient·polygon·sibling 배경·의도된 crop/접근성 숨김 등의 자동 후보는 원시 값을 유지하고 실화면 판단을 별도 기록했다.

[소스와 보고서 해시·스코프](source-manifest.json), [누적 감사 경과](integration-audit-history.md), [주 검수 원본 메모](primary-review.json)를 함께 보존했다. 누적 경과에는 수정 전 결과가 포함되므로 최종 상태는 해시와 후속 범위를 확인해야 한다. 정적 경고는 데이터 기하 등 검토용 후보이며 오류와 구별한다.

| 보고서 | 스냅샷 상태 | 실제 기록 요약 |
|---|---|---|
'''
    old_readme=(out/'README.md').read_text() if (out/'README.md').exists() else ''
    raw_marker='<!-- RAW CANDIDATE SCOPE -->'
    raw_tail='\n\n'+(raw_marker+old_readme.split(raw_marker,1)[1]) if raw_marker in old_readme else ''
    (out/'README.md').write_text(intro+'\n'.join(rows)+'\n'+raw_tail)
    section=f'''{START}
## 최종 독립 QA와 개별 페이지 검수 차이

최종 컬렉션 해시: `{tree(before)}`. 검사 통과는 보고서에 명시한 정적 계약·폰트·대비·잘림·기능 범위에 대한 결과이며 원본과 100% 동일하다는 뜻이 아니다. 이전 본문의 해시와 수치는 해당 시점의 기록이다. 최신/과거 스냅샷과 마지막 변경의 좁은 후속 검사 범위는 `quality/source-manifest.json` 및 `quality/README.md`에 구분했다.

요청된 사진·복잡한 그림·래스터 아이콘 등의 회색 placeholder와 Lucide 대체는 허용한 차이다. 실제 로드한 대체 글꼴의 획·폭·행간, 줄바꿈·미세 배치·테두리 등 남은 차이는 허용 미디어 대체와 구별해 아래에 적었다. `accepted`는 개별 검토 기록의 상태이며 픽셀 동일을 뜻하지 않는다. 원시 비교 이미지 해시·검토 시각은 `quality/primary-review.json`에 있다.

{page_table}
{END}
'''
    notes=project/'review-notes.md';text=notes.read_text()
    if START in text:text=re.sub(re.escape(START)+'.*?'+re.escape(END),lambda _:section.rstrip(),text,flags=re.S)
    else:text=text.rstrip()+'\n\n'+section
    notes.write_text(text.rstrip()+'\n')
    after=snapshot(collection)
    if before!=after:raise SystemExit(f'{kid}: frozen collection unexpectedly changed while copying quality reports')
    inventory={str(p.relative_to(out)):sha(p) for p in sorted(out.rglob('*')) if p.is_file() and p.name!='file-inventory.json'}
    (out/'file-inventory.json').write_text(json.dumps({'collection':kid,'generatedAtUtc':generated,'sourceUnchanged':True,'files':inventory},ensure_ascii=False,indent=2)+'\n')
    print(kid, 'files',len(inventory)+1,'pageNotes',len(page_rows),'sourceUnchanged',True,flush=True)

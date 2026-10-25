"""Package text sources only; never include media, fonts or nested archives."""
from pathlib import Path
from collections import Counter
import hashlib,json,shutil,zipfile

ROOT=Path('/workspace/work/round5-delivery-20261025')
OUT=Path('/workspace/work/round5-source-only-20261025')
NAME='rhetis-round5-006-020-source'
ALLOWED={'.html','.css','.js','.json','.md','.py','.txt'}

def sha(data):return hashlib.sha256(data).hexdigest()
def main():
    stage=OUT/NAME;stage.mkdir(parents=True,exist_ok=False)
    included=[];excluded=Counter()
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file():continue
        if p.suffix.lower()not in ALLOWED:
            excluded[p.suffix.lower()]+=1;continue
        data=p.read_bytes();data.decode('utf-8');assert b'\0'not in data,p
        rel=p.relative_to(ROOT);target=stage/rel
        target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    overrides=OUT/'latest-documents.json'
    if overrides.exists():
        for rel,content in json.loads(overrides.read_text()).items():
            target=stage/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(content)
    (stage/'PUBLISHED-README.md').write_text((stage/'README.md').read_text())
    (stage/'README.md').write_text('''# Rhetis Round5 · 6개 컬렉션 소스 전용 ZIP

최종 컬렉션6개와 검수 페이지·도구의 텍스트 소스를 모았다. 이미지·PDF·폰트 등 바이너리, 기존 ZIP과 실행 로그는 포함하지 않는다.

- `collections/`: 최종135개 요소, 키트 토큰, foundation, fixture 소스
- `reviews/<collection>/replica/`: 보존된 replica HTML·CSS
- `reviews/<collection>/reassembled/`: 조립본 HTML·CSS
- `reviews/<collection>/library/`: 실제 소스로 동작하는 라이트·다크 시트 HTML
- `tools/`, `build/`: 생성·검수 도구와 작업 기록
- `REPORT.md`, `element-origins.md`, 검수 JSON: 디자인 출처·차이·검증 기록

이미지와 폰트 파일을 제외했으므로 PNG를 참조하는 `preview.html`에서는 미리보기 이미지가 표시되지 않는다. 소스 기반 시트 HTML의 원래 글꼴을 재현하려면 `reviews/<collection>/assets/fonts/fonts.css`가 참조하는 폰트 파일을 별도로 준비해야 한다. 최종 컬렉션 소스는 `collections/`이며 `build/`에는 과거 생성 스크립트도 보존되어 있다.

게시된 PDF는 `element-review-pdfs/README.md`의 GitHub 다운로드 링크로 별도 제공한다. `SOURCE-MANIFEST.json`에서 이 ZIP의 전체 소스 목록·해시를 확인할 수 있다. 기존 제출물과 replica는 수정하지 않았다.
''')
    shutil.copy2(Path(__file__),stage/'tools/pack_source_only.py')
    for p in sorted(stage.rglob('*')):
        if p.is_file():
            data=p.read_bytes();data.decode('utf-8');assert b'\0'not in data
            included.append({'file':str(p.relative_to(stage)),'bytes':len(data),'sha256':sha(data)})
    assert len(list((stage/'collections').glob('*/elements/*/element.json')))==135
    assert len(list((stage/'collections').glob('*/kit/kit.json')))==6
    manifest={'format':'text-source-only','collections':6,'elements':135,'allowedExtensions':sorted(ALLOWED),'sourceFiles':len(included),'excludedFilesByExtension':dict(excluded),'embeddedBinaryMedia':False,'files':included}
    (stage/'SOURCE-MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    archive=OUT/(NAME+'.zip')
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
        for p in sorted(stage.rglob('*')):
            if p.is_file():z.write(p,str(Path(NAME)/p.relative_to(stage)))
    with zipfile.ZipFile(archive)as z:
        assert z.testzip()is None
        assert {x.split('/')[0]for x in z.namelist()}=={NAME}
        for p in z.namelist():
            assert Path(p).suffix.lower()in ALLOWED,p
            data=z.read(p);data.decode('utf-8');assert b'\0'not in data,p
    result={'file':archive.name,'bytes':archive.stat().st_size,'sha256':sha(archive.read_bytes()),'zipCRC':'pass','allFilesUTF8':True,'entries':len(included)+1,'collections':6,'elements':135,'excludedFilesByExtension':dict(excluded)}
    (OUT/'source-zip-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='excludedFilesByExtension'},ensure_ascii=False),flush=True)
if __name__=='__main__':main()

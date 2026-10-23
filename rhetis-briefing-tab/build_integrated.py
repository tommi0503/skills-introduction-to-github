"""Bundle the collection, replica/reassembled code, assets and review PDFs."""
from pathlib import Path
import hashlib,json,zipfile
SOURCE=Path(__file__).resolve().parent;REPO=SOURCE.parent
TARGET=REPO/'briefing-tab-complete.zip';PREFIX='briefing-tab-complete'
EXCLUDED={'__pycache__','release-staging','downloaded-github'}
sha=lambda data:hashlib.sha256(data).hexdigest()
files=[]
for p in sorted(SOURCE.rglob('*')):
 rel=p.relative_to(SOURCE)
 if not p.is_file() or any(part in EXCLUDED for part in rel.parts):continue
 if p.name in {'.gitignore','integrated-archive-verification.json'} or p.name.startswith(('chip-page-','temp-')):continue
 files.append((p,'rhetis-briefing-tab/'+str(rel)))
for name in ['briefing-tab-elements-light.pdf','briefing-tab-elements-dark.pdf','briefing-tab-compare-replica.pdf','briefing-tab-compare-reassembled.pdf','briefing-tab-preview.png']:
 p=REPO/name;assert p.is_file();files.append((p,name))
assert len(list((SOURCE/'briefing-tab/elements').glob('*/element.css')))==56
assert len(list((SOURCE/'briefing-tab-review/replica').glob('slide_*.html')))==11
assert len(list((SOURCE/'briefing-tab-review/reassembled').glob('slide_*.html')))==11
readme='''# Briefing Tab 통합 패키지

이 ZIP 하나에 컬렉션 전체 코드, 원본 재현본(replica) 코드, 라이브러리 재조립본 코드, 글꼴·아이콘 런타임, 원본 이미지, 검수 자료와 재생성 도구를 함께 담았습니다. 입력은 덱1개, 슬라이드11장(20–30번)입니다.

- `rhetis-briefing-tab/briefing-tab/`: 56개 요소·148개 요소 fixture, 키트 토큰과 foundation을 포함한 반입용 컬렉션 전체 소스.
- `rhetis-briefing-tab/briefing-tab-review/replica/`: HTML/CSS 소스, 페이지별 PNG, replica.pdf.
- `rhetis-briefing-tab/briefing-tab-review/reassembled/`: 컬렉션으로 재조립한 HTML/CSS 소스, 페이지별 PNG, reassembled.pdf.
- `rhetis-briefing-tab/briefing-tab-review/library/`: 라이트·다크 HTML, 요소별 PNG와 fixture별 벡터 PDF.
- `rhetis-briefing-tab/briefing-tab-review/compare-replica/`, `compare-reassembled/`: 원본과 카피를 나란히 놓은 PNG.
- 루트의 `briefing-tab-elements-*.pdf`: 요소별 검수 시트, 각각57페이지.
- 루트의 `briefing-tab-compare-*.pdf`: 원본·카피 비교 시트, 각각11페이지.
- `rhetis-briefing-tab/README.md`: 실행·재생성 방법. `design-language.md`, `review-notes.md`는 검수 폴더 안에 있습니다.
- `manifest.json`: ZIP 내 파일 목록, 크기와 SHA-256. manifest 자신은 목록에서 제외합니다.

## 미리보기

압축을 푼 뒤 터미널에서 다음을 실행합니다.

```sh
cd rhetis-briefing-tab
python -m http.server 8765 --bind 127.0.0.1 --directory .
```

브라우저에서 `http://127.0.0.1:8765/briefing-tab-review/index.html`을 엽니다. 외부 CDN 없이 동봉된 글꼴과 아이콘 런타임을 사용합니다.

각 ZIP의 내용은 이미 펼친 상태로 통합했으므로 기존 컬렉션 ZIP과 검수 ZIP을 중복으로 넣지 않았습니다. 기존 별도 ZIP의 계약과 폴더 구조는 변경하지 않았습니다.
'''
manifest={'package':'briefing-tab-complete','decks':1,'slides':11,'elements':56,'element_fixtures':148,'replica_html':11,'reassembled_html':11,'files':[]}
with zipfile.ZipFile(TARGET,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p,rel in files:
  data=p.read_bytes();z.writestr(f'{PREFIX}/{rel}',data)
  manifest['files'].append({'path':rel,'bytes':len(data),'sha256':sha(data)})
 data=readme.encode();z.writestr(f'{PREFIX}/README.md',data);manifest['files'].append({'path':'README.md','bytes':len(data),'sha256':sha(data)})
 z.writestr(f'{PREFIX}/manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
with zipfile.ZipFile(TARGET) as z:
 assert z.testzip() is None
 assert sorted({p.split('/')[0] for p in z.namelist()})==[PREFIX]
 for record in manifest['files']:
  data=z.read(f'{PREFIX}/{record["path"]}');assert len(data)==record['bytes'] and sha(data)==record['sha256']
 report={'archive':TARGET.name,'bytes':TARGET.stat().st_size,'sha256':sha(TARGET.read_bytes()),'entries':len(z.namelist()),'single_top_level':PREFIX,'zip_crc':'pass','all_file_hashes_match':True,'elements':56,'replica_html':11,'reassembled_html':11}
(SOURCE/'integrated-archive-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,indent=2))

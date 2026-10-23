# Briefing Tab · Rhetis collection from deck 078

업로드된 덱1개(슬라이드20–30,11장)에서 만든 독립 컬렉션입니다. 컬렉션56요소, 요소fixture148개, foundation fixture3개, 필수모범fixture28개를 포함합니다.

`briefing-tab/`은 반입용 HTML/CSS 원본입니다. `briefing-tab-review/`는 원본·replica·재조립·라이트/다크 요소시트와 검수기록입니다. 루트의 `briefing-tab.zip`, `briefing-tab-review.zip`, `briefing-tab-preview.png`는 같은 최종 소스에서 생성했습니다.

원본과 차이가 컸던 초기 재조립은 제출본에서 교체했습니다. 최종 조립은 복합차트·다중구간도넛/파이·사람비율을 기존 계약 요소와 실제 수치 데이터로 복원했고, 11장 비교PNG를 각각 검수했습니다. 25번 플롯은 원본414px에 대해413.891px입니다. 일부 폰트·아이콘·라벨위치의 미세차이와 원본style의 낮은대비는 review-notes.md에 기록했습니다.

## 미리보기

이 디렉터리에서 `python -m http.server 8765 --bind 127.0.0.1 --directory .`를 실행한 뒤 `http://127.0.0.1:8765/briefing-tab-review/index.html`을 엽니다. 프레젠테이션 본문은 모두1280×720입니다. 비교PNG는2560×720이며 요소별시트PNG는1328px폭의세로시트입니다.

## 다시 빌드하기

Python3.12+, Chromium, 그리고 requirements.txt의 Python 패키지가 필요합니다. Playwright는 기본 `/usr/bin/chromium`을 사용합니다. 먼저 위 HTTP 서버를 실행합니다.

```sh
python validate_contract.py
python scope_audit.py
python build_sheets.py
python browser_audit.py
python chip_audit.py
python render_all.py
python package_release.py
```

`package_release.py`는 `release-staging/`에 두ZIP,해시검증JSON,미리보기PNG를만듭니다. `render_all.py`는 최종조립HTML을 읽어 렌더하며 페이지를 오래된 초안으로 재생성하지 않습니다. 소스HTML이 최종조립의 기준입니다.

`reference/`에는 원본계약과 preview.py, 모범fixture 및 폴더계약 매핑용JSON만 둡니다. 샘플컬렉션의디자인CSS는복사하지않았습니다. 글꼴과Lucide런타임은검수폴더에들어있어렌더에외부CDN이필요없습니다.

## 검증의 범위

기본팔레트의라이트/다크6776크기조합,폰트,텍스트범위,겹침/잘림/계산색대비를검사했습니다. 캡슐/원형라벨19개는실제렌더픽셀의글자중심도검사했습니다.원본style의낮은대비는복제충실도를위해유지하며별도기록합니다.실제Rhetis intake는참조팩에없으므로실제반입성공을주장하지않습니다.

필수 card-4의✹4개와callout2개의원본배치는일반규칙과충돌하나사용자가명시한동일마크업·데이터보존을우선했습니다.새fixture는빈Lucide슬롯을사용합니다.

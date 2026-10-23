# Rhetis collections 030–045

첨부 이미지 ZIP의 6개 덱, 원본 90장을 각각 독립 컬렉션으로 제작한 소스와 검수 산출물입니다. [비교 미리보기](index.html), [90장 목록](inventory.md), [최종 파일 검사](verification.json)를 함께 제공합니다.

요소별 시트를 모은 [검수 PDF 모음](element-sheet-pdfs/README.md)과 [6개 컬렉션 통합 PDF](element-sheet-pdfs/all-collections-element-sheets.pdf)를 제공합니다. 컬렉션별 114페이지(라이트 57장 + 다크 57장), 통합 684페이지이며 요소별 북마크가 있습니다.

원본·카피본 비교 시트의 [검수 PDF 모음](comparison-pdfs/README.md)도 제공합니다. [원본 | replica 90쪽](comparison-pdfs/original-vs-replica.pdf), [원본 | 조립본 90쪽](comparison-pdfs/original-vs-reassembled.pdf), [전체 통합 180쪽](comparison-pdfs/all-slide-comparisons.pdf)에 덱·페이지별 북마크를 넣었습니다.

[전체 컬렉션·복제본 코드 통합 ZIP 다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/rhetis-collections-030-045-all-source.zip) — 6개 컬렉션과 모든 fixture, replica·조립본 180장의 코드, 실행용 폰트, 계약, 도구, 슬라이드별 PNG·미리보기를 포함합니다. 검수 PDF·원본·요소시트·비교 PNG는 아래 별도 검수자료로 제공합니다. 압축을 푼 폴더에서 아래 미리보기 실행 명령을 사용할 수 있습니다.

| 덱 | 컬렉션 / 소스 | 원본 페이지 | 요소 fixture | 다운로드 |
|---|---|---:|---:|---|
| 030 | [chalkline](collections/chalkline/) | 2 | 171 | [collection](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/chalkline.zip) · [review](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/chalkline-review.zip) |
| 031 | [undertow](collections/undertow/) | 13 | 174 | [collection](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/undertow.zip) · [review](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/undertow-review.zip) |
| 033 | [cutplane](collections/cutplane/) | 15 | 171 | [collection](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/cutplane.zip) · [review](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/cutplane-review.zip) |
| 038 | [skylight](collections/skylight/) | 21 | 175 | [collection](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/skylight.zip) · [review](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/skylight-review.zip) |
| 043 | [arrowtab](collections/arrowtab/) | 20 | 180 | [collection](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/arrowtab.zip) · [review](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/arrowtab-review.zip) |
| 045 | [blockweave](collections/blockweave/) | 19 | 183 | [collection](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/blockweave.zip) · [review](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/blockweave-review.zip) |

각 컬렉션은 kit, foundation, 계약 요소 56종을 포함합니다. `collections/<name>/`과 컬렉션 ZIP 안에는 계약이 허용한 CSS/JSON/MD/HTML만 있습니다. 사진·복잡한 일러스트·이미지 아이콘·기기 화면은 연회색 placeholder입니다. 원본 전체 이미지를 페이지 배경으로 쓰지 않았습니다.

## 검수 산출물

`reviews/<name>-review/`에는 replica/재조립 HTML·CSS와 1280×720 PNG·PDF, 원본과 나란히 놓은 2560×720 비교 PNG, 라이트·다크 라이브러리 HTML, 56종 각각의 양 모드 시트 PNG, 전체 라이브러리 PDF가 있습니다. `design-language.md`, `review-notes.md`, `automatic-checks.json`은 해석·수정·검사 근거를 기록합니다.

원본 폰트 메타데이터가 없어 제공 글꼴 중 형태가 가까운 실제 폰트를 로드했습니다. 판독 불가로 보완한 문구와 원본의 차이는 덱별 노트에 구분했습니다. 재조립은 foundation의 12×6 그리드와 계약 요소로 구성했습니다. 원본의 비율과 배치를 맞추기 위해 의미가 있는 조합과 요소 변형을 사용하고, 차이가 남는 부분은 검수 기록에 구체적으로 적었습니다. 라이브러리 색은 디자인에 고정하지 않고 Rhetis의 팔레트 자리를 사용합니다.

## 미리보기 실행

이 폴더에서 다음 명령을 실행하고 `http://127.0.0.1:8000/`을 엽니다. 외부 서비스·네트워크 폰트 없이 로컬 파일로 그립니다.

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

표준 라이브러리 시트 빌드는 다음과 같습니다.

```sh
python tools/preview.py collections/chalkline contract/type-steps.json --out light.html
python tools/preview.py collections/chalkline contract/type-steps.json --dark --out dark.html
```

제공 preview.py의 전역 `.frame`과 `small` 규칙이 계약의 이미지 프레임·숫자 단위에 영향을 주어, 이 저장본에서는 시트 wrapper/header만 선택하도록 범위를 좁혔습니다. 모범 fixture의 마크업·데이터는 namespace 외 그대로이며, 최소 칸 주석은 실제 수용 크기입니다. 모범 callout의 원본 배치는 구체적인 동일 마크업 요구를 우선하여 보존했습니다. 모범 card-4의 `✹` 문자도 같은 이유로 보존하며 추가 아이콘은 빈 Lucide slot으로 작성했습니다.

## 검증 재실행

Python Pillow·pypdf, Node playwright·pngjs와 Chromium을 사용합니다. `CHROMIUM_PATH`로 브라우저 실행 경로를 바꿀 수 있습니다.

```sh
python tools/audit_collections.py
node tools/audit_css.cjs
node tools/audit_browser.cjs
node tools/audit_pages.cjs
node tools/audit_chip_glyphs.cjs
node tools/audit_foundation.cjs
python tools/audit_artifacts.py
python tools/check_reassembly_css.py
```

정적 계약 검사, 명시된 최소/중간/12×6의 실제 브라우저 검사, 폰트·1280×720·텍스트 경계·chip 정렬 검사, 소스 재렌더와 저장 PNG의 픽셀 비교, 비교 PNG 양쪽의 원본/최종 렌더 일치, PDF 페이지 수·수정 시점, 전체 PNG 크기와 ZIP CRC/SHA-256을 확인했습니다. CSS 색 대비 자동 후보는 실제 도형/가상요소 바탕을 눈으로 확인해 구분하며 근거를 체크 기록에 남깁니다. Rhetis 본 저장소 내부의 intake 실행은 이 레퍼런스 팩에 포함되지 않습니다.

원본 90장은 `originals/`에, 제공 계약은 `contract/`에 보존했습니다. 샘플 컬렉션의 디자인 CSS는 이 소스에 포함하지 않았습니다. 게시 후 ZIP을 실제로 다시 내려받아 검증한 결과는 `download-verification.json`에 추가됩니다.

# Rhetis Enterprise 053–069

7개 덱을 각각 컬렉션으로 제작했습니다. 총 원본 95장, 컬렉션 요소 392개입니다.

| 덱 | 컬렉션 | 페이지 | 컬렉션 ZIP | 검수 ZIP |
|---|---|---:|---|---|
|053|[rise-block](rise-block/)|2|[다운로드](downloads/rise-block.zip)|[다운로드](downloads/rise-block-review.zip)|
|054|[cinder-pulse](cinder-pulse/)|20|[다운로드](downloads/cinder-pulse.zip)|[다운로드](downloads/cinder-pulse-review.zip)|
|055|[current-fold](current-fold/)|18|[다운로드](downloads/current-fold.zip)|[다운로드](downloads/current-fold-review.zip)|
|056|[scanline-rise](scanline-rise/)|18|[다운로드](downloads/scanline-rise.zip)|[다운로드](downloads/scanline-rise-review.zip)|
|058|[halo-field](halo-field/)|15|[다운로드](downloads/halo-field.zip)|[다운로드](downloads/halo-field-review.zip)|
|067|[corner-signal](corner-signal/)|21|[다운로드](downloads/corner-signal.zip)|[다운로드](downloads/corner-signal-review.zip)|
|069|[anchor-frame](anchor-frame/)|1|[다운로드](downloads/anchor-frame.zip)|[다운로드](downloads/anchor-frame-review.zip)|

[미리보기](index.html) · [미리보기 이미지](preview.png) · [전체 이미지 목록과 계약 대응](inventory.md) · [최종 파일 검증](final-verification.json) · [내려받기 검증](downloads/github-download-verification.json)

컬렉션 ZIP에는 최상위 컬렉션 폴더 하나와 계약에서 허용한 파일 형식만 있습니다. 검수 ZIP의 루트에는 replica, compare-replica, library, reassembled, compare-reassembled, 디자인 언어와 검수 기록이 있으며, runtime 폴더에 실제 글꼴과 컬렉션 CSS를 함께 넣어 압축을 푼 뒤 독립적으로 열 수 있습니다. 최신 Chromium에서 여세요. CSS anchor 기반 선/면 차트는 해당 브라우저 기능이 필요합니다.

검수 ZIP의 PNG는 페이지·요소 시트 1280×720, 비교 PNG 2560×720입니다. 전체 library PDF에는 fixture 또는 요소별 전체 시트가 들어 있으며 컬렉션별 페이지 수는 검증 JSON에 기록했습니다.

## 확인 범위와 남은 차이

각 원본은 독립 HTML/CSS replica로 만들고 실제 브라우저에서 페이지별로 비교했습니다. 사진·복잡한 그림·기기 화면은 회색 placeholder입니다. 조립본은 foundation 및 계약 요소를 12×6 grid에 배치했습니다. 원본과 완전한 픽셀 일치를 달성했다고 주장하지 않습니다. 일부 콤보차트 시리즈, 복잡한 리본/원형 관계, 세부 타일 위치와 페이지 문구의 축약 등 차이는 각 `<collection>-review/review-notes.md`에 기록했습니다.

053은 오류 보정 과정에서 요청한 비교·수정 횟수 상한을 초과했습니다. 모든 컬렉션이 요청의 모든 품질 조건을 충족했다고 단정하지 않으며, 자동검사는 구조·렌더링·배치 검사의 범위를 의미합니다. 실제 Rhetis intake 실행 환경은 제공되지 않아 정식 반입은 검증하지 못했습니다.

필수 card-4 fixture의 ✹ 문자는 문자 아이콘 금지 규칙과 충돌하지만 필수 fixture 원문 보존을 우선했습니다.

## 소스 사용

리포지토리의 각 컬렉션 폴더가 CSS/JSON/HTML 원본입니다. `tools/preview.py`와 `contract/`는 제공된 레퍼런스 팩의 원본입니다. `fonts/`는 제공된 실제 글꼴입니다. 다음 명령으로 시트를 생성할 수 있습니다.

```sh
python tools/preview.py rise-block contract/type-steps.json --out light.html
python tools/preview.py rise-block contract/type-steps.json --dark --out dark.html
python tools/contract_audit.py
```

브라우저가 file URL을 차단하면 이 폴더만 127.0.0.1 로컬 서버로 제공해 열 수 있습니다. GitHub에서 HTML은 소스 뷰로 열리므로 실제 미리보기는 내려받아 로컬 브라우저로 여세요. 기존 저장소 작업을 보존하고 force push를 사용하지 않았습니다.

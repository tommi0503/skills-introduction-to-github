# Rhetis 기업 덱 요소 컬렉션

7개 덱의 디자인 언어를 서로 다른 컬렉션으로 옮긴 소스와 검수 자료입니다. [이미지 미리보기](PREVIEW.md)와 [시각 탐색 화면](index.html)에서 요소 시트와 총95페이지의 조립 비교로 이동할 수 있습니다. 정적 미리보기 HTML도 소스와 함께 저장합니다.

최종 검수 결과와 산출물 해시는 각각 [verification.json](verification.json), [artifacts.json](artifacts.json)을 기준으로 확인하세요. 이 문서는 검수 성공이나 배포 완료를 대신 선언하지 않습니다. 패키징 전에는 해당 파일 또는 ZIP 링크가 아직 없을 수 있습니다.

최종 확인: 392개 요소 · 1,093개 fixture · 11,000개 크기/테마 상태 · 조립95장 · PNG1,152개. ZIP14개를 GitHub에서 실제로 다시 다운로드해 SHA-256·CRC·PNG 크기와 조립 HTML 의존성 경로를 검사했습니다. [다운로드 검증 기록](download-verification.json). 계약 미지원103개와 격자 투영 차이는 [전체 목록](UNEXPRESSIBLE.md)과 각 검수 기록에 남깁니다.

## 컬렉션과 다운로드

| 덱 | 컬렉션 소스 | 페이지 | 다운로드 | 검수 자료 |
|---|---|---:|---|---|
| 053 | [rise-block](rise-block/) | 2 | [rise-block.zip](rise-block.zip) · [review ZIP](rise-block-review.zip) | [시트](rise-block-review/index.html) · [출처](rise-block-review/PROVENANCE.md) · [GAPS](rise-block-review/GAPS.md) |
| 054 | [cinder-pulse](cinder-pulse/) | 20 | [cinder-pulse.zip](cinder-pulse.zip) · [review ZIP](cinder-pulse-review.zip) | [시트](cinder-pulse-review/index.html) · [출처](cinder-pulse-review/PROVENANCE.md) · [GAPS](cinder-pulse-review/GAPS.md) |
| 055 | [current-fold](current-fold/) | 18 | [current-fold.zip](current-fold.zip) · [review ZIP](current-fold-review.zip) | [시트](current-fold-review/index.html) · [출처](current-fold-review/PROVENANCE.md) · [GAPS](current-fold-review/GAPS.md) |
| 056 | [scanline-rise](scanline-rise/) | 18 | [scanline-rise.zip](scanline-rise.zip) · [review ZIP](scanline-rise-review.zip) | [시트](scanline-rise-review/index.html) · [출처](scanline-rise-review/PROVENANCE.md) · [GAPS](scanline-rise-review/GAPS.md) |
| 058 | [halo-field](halo-field/) | 15 | [halo-field.zip](halo-field.zip) · [review ZIP](halo-field-review.zip) | [시트](halo-field-review/index.html) · [출처](halo-field-review/PROVENANCE.md) · [GAPS](halo-field-review/GAPS.md) |
| 067 | [corner-signal](corner-signal/) | 21 | [corner-signal.zip](corner-signal.zip) · [review ZIP](corner-signal-review.zip) | [시트](corner-signal-review/index.html) · [출처](corner-signal-review/PROVENANCE.md) · [GAPS](corner-signal-review/GAPS.md) |
| 069 | [anchor-frame](anchor-frame/) | 1 | [anchor-frame.zip](anchor-frame.zip) · [review ZIP](anchor-frame-review.zip) | [시트](anchor-frame-review/index.html) · [출처](anchor-frame-review/PROVENANCE.md) · [GAPS](anchor-frame-review/GAPS.md) |

## 출처와 적용 범위

계약의56개 요소 폴더를 컬렉션마다 갖추는 구조입니다. 이것이56개 요소 모두 원본에 등장했다는 뜻은 아닙니다. [전체 출처 표](PROVENANCE.md) · [unexpressible 전체 목록](UNEXPRESSIBLE.md) 및 각 컬렉션의 PROVENANCE에서 직접 관찰한 요소와 디자인 언어로 새로 설계한 **확장** 요소를 구별합니다. [provenance.json](provenance.json)과 각 review/map.json에는 인스턴스별 bbox, 원본 수치, 계약 마크업, base·변형·같은 형태의 관계가 기록됩니다.

입력 replica는 동결한 비교 기준이며 이번 요소 재작성 과정에서 바꾸지 않습니다. 요소 CSS는 원본 HTML·SVG의 실제 좌표, 크기, 선, 타이포와 멤버 구조에서 새로 작성했습니다. fixture의 예시 문구는 새 물류업무 내용이며, 정량 형태를 결정하는 수치와 필수 모범 fixture는 그 목적에 맞춰 보존합니다. 원본 문구와 새 fixture 문구를 동일 데이터라고 해석하지 마세요.

기존 계약 마크업으로 표현할 수 없는 원본 형태는 각 GAPS에 이유와 필요한 구조를 기록하고 **조립본에서 빈칸으로 둡니다**. 임의 변형이나 다른 요소로 바꿔 채우지 않습니다. 사진·복잡한 이미지의 연한 회색 placeholder와 계약 미지원 빈칸은 서로 다른 처리입니다.

조립본은 foundation의 `.slide > .page > .body` 12×6 그리드에 계약 요소를 배치합니다. 원본 bbox를 가까운 격자 칸으로 투영하므로 원본의 자유 좌표와 위치·폭·높이가 달라질 수 있습니다. 요소의 원본 크기 비교와 격자 조립 결과는 별도로 확인해야 합니다. [격자 투영 기록](reassembly-projection.json), [조립 검사](reassembled-audit.json), 개별 비교 PNG를 함께 보세요.

## 로컬 열기와 재현

이 README가 있는 디렉터리에서 서버를 실행합니다. HTML을 파일로 직접 열기보다 같은 서버에서 열어 상대 CSS·폰트 경로를 유지하세요.

```bash
python -m http.server 8766 --bind 127.0.0.1
```

브라우저에서 http://127.0.0.1:8766/index.html 을 엽니다. 재생성 도구는 Python과 Playwright, Chromium을 사용합니다. `pip install -r requirements.txt`로 의존성을 설치하고 `/usr/bin/chromium`을 준비한 뒤 별도 터미널에서 아래 명령을 실행합니다. 재생성은 해당 HTML·PNG·감사 자료를 갱신합니다.

```bash
# 구조 및 fixture 문구 검사
python tools/static_audit.py
python tools/check_fixture_text.py

# 예: 한 컬렉션의 전체 요소 시트, 또는 특정 요소
python tools/element_sheets.py current-fold --skip-current
python tools/element_sheets.py current-fold --leaf table --skip-current

# 계약 요소와 foundation으로 조립하고 실제 브라우저에서 렌더
python tools/build_reassembled.py
python tools/render_reassembled.py

# 현재 소스와 렌더 계보 검사; 통과 조건을 만족하면 패키징
python tools/package_release.py --verify-only
python tools/package_release.py
```

전체 요소 시트 재생성은7개 ID를 `element_sheets.py`의 위치 인자로 전달합니다. 원본 고정 자료는 `reference/`, 계약과 참고자료는 `contract/` 및 `reference-contract/`, 실행 도구는 `tools/`에 있습니다. 각 review의 `audits/`는 최소 칸과 지원 크기, 라이트·다크 모드의 검사 기록이며, 자동 검사와 실제 화면 검수의 범위를 각 검수 문서에서 확인할 수 있습니다.

# Rhetis 기업 덱 컬렉션 — Round 5

기존 replica와 Round 4 결과는 보존하고, 실제 replica에 등장한 디자인만 독립 요소로 다시 작성했습니다. 최신 Round 5 완화 규칙을 적용합니다. 이 작업에서는 git 명령을 실행하지 않습니다. GitHub 게시에는 연결 도구와 HTTP API를 사용하며, 결과는 `publication.json`과 재다운로드 검사로 확인합니다.

[시각 탐색](index.html) · [대표 비교](PREVIEW.md) · [전체 변경 보고](round5/summary.json) · [이전 gap 재분류](round5/gap-reclassification.json)

| 덱 | 컬렉션·소스 | 페이지 | 컬렉션 ZIP | 검수 ZIP | 출처·검수 |
|---|---|---:|---|---|---|
| 053 | [rise-block](rise-block/) | 2 | [다운로드](rise-block.zip) | [다운로드](rise-block-review.zip) | [폴더 ← replica](rise-block-review/PROVENANCE.md) · [검수](rise-block-review/review-notes.md) |
| 054 | [cinder-pulse](cinder-pulse/) | 20 | [다운로드](cinder-pulse.zip) | [다운로드](cinder-pulse-review.zip) | [폴더 ← replica](cinder-pulse-review/PROVENANCE.md) · [검수](cinder-pulse-review/review-notes.md) |
| 055 | [current-fold](current-fold/) | 18 | [다운로드](current-fold.zip) | [다운로드](current-fold-review.zip) | [폴더 ← replica](current-fold-review/PROVENANCE.md) · [검수](current-fold-review/review-notes.md) |
| 056 | [scanline-rise](scanline-rise/) | 18 | [다운로드](scanline-rise.zip) | [다운로드](scanline-rise-review.zip) | [폴더 ← replica](scanline-rise-review/PROVENANCE.md) · [검수](scanline-rise-review/review-notes.md) |
| 058 | [halo-field](halo-field/) | 15 | [다운로드](halo-field.zip) | [다운로드](halo-field-review.zip) | [폴더 ← replica](halo-field-review/PROVENANCE.md) · [검수](halo-field-review/review-notes.md) |
| 067 | [corner-signal](corner-signal/) | 21 | [다운로드](corner-signal.zip) | [다운로드](corner-signal-review.zip) | [폴더 ← replica](corner-signal-review/PROVENANCE.md) · [검수](corner-signal-review/review-notes.md) |
| 069 | [anchor-frame](anchor-frame/) | 1 | [다운로드](anchor-frame.zip) | [다운로드](anchor-frame-review.zip) | [폴더 ← replica](anchor-frame-review/PROVENANCE.md) · [검수](anchor-frame-review/review-notes.md) |

관찰 디자인141종, fixture373개(요소347개·foundation26개), 검증용 조립95페이지입니다. 최종3448개 크기/모드 상태에 자동 검사 문제가 없고, 시트435장과 삼단 비교95장을 주 에이전트가 개별 열람했습니다. 남은 unexpressible은0건입니다. 마지막 렌더의 검사 결과·PNG 크기·해시는 `verification.json`, ZIP CRC와 해시는 `artifacts.json` 및 `SHA256SUMS`를 기준으로 확인합니다. 검증 결과는 실제 마지막 파일의 SHA-256과 연결됩니다.

각 요소의 fixture 행마다 최소 칸 이상인 모든 지정 크기를 실제 1280×720 브라우저에서 렌더하고 요소 칸을 잘랐습니다. 라이트·다크 시트와 replica | 12×6 | min 대조 시트를 제공합니다. 부모의 실제 이미지 열람은 `primary-visual-review.json`에 해당 PNG SHA-256과 함께 기록합니다.

조립본은 foundation의12×6 그리드에 배치하므로 원본 자유 좌표와 차이가 있습니다. 패널 내부는 source bbox 비율을 보존하는120×60 그리드입니다. 원본 색은 공통 팔레트의 역할로 바뀌며 사진·3D·이미지 아이콘은 중성 placeholder로 유지합니다. 원본과 완전히 같은 페이지라고 주장하지 않습니다.

원본 문구는 조립 검증 페이지에서만 사용합니다. fixture는 새 한국어 업무 내용이며 6자 이상 원문 중복을 자동 검사합니다. 소스 replica203개와 제공 폰트32개를 SHA-256으로 보존합니다.

로컬 열기:

```bash
python -m http.server 8767 --bind 127.0.0.1
```

브라우저에서 http://127.0.0.1:8767/index.html 을 엽니다. 재현에는 requirements.txt, Playwright, /usr/bin/chromium이 필요합니다.

```bash
python tools/static_audit.py
python tools/check_fixture_text.py --out fixture-text-audit.json
python tools/element_sheets.py current-fold --skip-current
python tools/element_sheets.py halo-field --leaf foundation-panels --skip-current
python tools/build_reassembled.py
python tools/render_reassembled.py
python tools/audit_furniture.py
python tools/make_previews.py
python tools/package_release.py
```

`tools/merge_maps.py`와 이전 Round4 보정 스크립트는 이번 지도에 실행하지 않습니다. 이전 증거는 `round5/round4-evidence/`에 따로 보존합니다.

루트에 남은 Round4 검수 JSON과 `round5/round4-evidence/`는 이력입니다. 최종 판단에는 `static-audit.json`, `fixture-text-audit.json`, `furniture-audit.json`, `round5/cross-audit.json`, `verification.json`, `primary-visual-review.json` 및 각 컬렉션의 `audits/`를 사용합니다.


[전체 요소 PDF 검수 시트 — 7개 컬렉션](pdfs/README.md)

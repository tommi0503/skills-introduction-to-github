# Rhetis: 6개 덱, 6개 독립 컬렉션

88개 원본 슬라이드를 바탕으로 만든 컬렉션입니다. 원본 충실도 지적 후 일반 카드로 대체했던 도표와 임의로 바뀐 색·형태·제목 크기를 다시 제작했습니다. 기존 저장소의 작업은 보존하고 이 폴더에만 결과를 추가했습니다.

[미리보기 HTML](preview.html) · [미리보기 이미지](preview.png) · [전체 이미지 목록과 페이지 유형](image-inventory.md) · [재작업 기준](fidelity-revision.md) · [검증 결과](delivery-validation.json)

| 원본 덱 | 컬렉션 | 페이지 | 반입용 ZIP | 검수 ZIP | 소스 |
|---|---|---:|---|---|---|
| 006 타운홀 | nocturne | 6 | [다운로드](nocturne.zip) | [다운로드](nocturne-review.zip) | [열기](collections/nocturne/) |
| 011 IR | inflexion | 20 | [다운로드](inflexion.zip) | [다운로드](inflexion-review.zip) | [열기](collections/inflexion/) |
| 012 협동로봇 | diecut | 19 | [다운로드](diecut.zip) | [다운로드](diecut-review.zip) | [열기](collections/diecut/) |
| 015 서비스 | afterglow | 9 | [다운로드](afterglow.zip) | [다운로드](afterglow-review.zip) | [열기](collections/afterglow/) |
| 016 피칭 | dockside | 30 | [다운로드](dockside.zip) | [다운로드](dockside-review.zip) | [열기](collections/dockside/) |
| 020 산학협력 | confluence | 4 | [다운로드](confluence.zip) | [다운로드](confluence-review.zip) | [열기](collections/confluence/) |

각 컬렉션은 kit, foundation, 계약 요소 56개를 포함합니다. 검수 ZIP에는 독립 실행 가능한 replica·재조립 HTML, 페이지 PNG/PDF, 원본과 나란히 비교 PNG, 요소 폴더별 라이트·다크 PNG와 전체 시트 HTML/PDF, 디자인 언어 및 검수 기록을 넣었습니다. 원본 비교 이미지의 두 패널은 각각 1280×720입니다. 전체 시트 PNG는 fixture 수에 따라 세로 길이가 다릅니다.

## 확인 방법

이 폴더에서 `python -m http.server 8000`을 실행하고 `http://localhost:8000/preview.html`을 엽니다. 페이지 비교의 실제 크기 버튼으로 1280×720 화면을 확인할 수 있습니다. HTML은 로컬 폰트를 로드하므로 ZIP을 풀고 폴더 구조를 유지해야 합니다.

```sh
python reference/tools/preview.py collections/nocturne/collection/nocturne reference/contract/type-steps.json --out light.html
python reference/tools/preview.py collections/nocturne/collection/nocturne reference/contract/type-steps.json --dark --out dark.html
python tools/check_contract.py collections/nocturne/collection/nocturne
python tools/render_review.py library --root collections/nocturne --name nocturne
```

렌더 도구는 Python, Pillow, PyMuPDF, Playwright와 Chromium을 사용합니다. `tools/check_contract.py`는 제공된 README와 예시의 구조를 비교하는 자체 검사이며 정식 Rhetis intake는 첨부 자료에 포함되지 않았습니다. `reference/samples/`는 계약 검사에 필요한 메타데이터·fixture만 포함하며 디자인 CSS는 포함하지 않습니다. `collections/*/build/`는 제작 과정 기록이며, 최종 HTML·CSS와 재렌더 기준은 `collection/`, `review/`, 공통 `tools/`입니다.

## 남는 차이와 판단

사진, 3D, 이미지 아이콘, 기기 화면은 사용자 지시에 따라 연한 회색 placeholder로 처리했습니다. 원본 폰트 파일이 없는 경우 실제 로드한 허용 글꼴 중 형태가 가까운 Pretendard·SUITE·Montserrat 등을 사용하고 크기·자간·줄바꿈을 조정했습니다. 판독 불가 문구와 도형 해석은 각 `review/review-notes.md`에 기록했습니다. 따라서 픽셀 단위 100% 동일함을 주장하지 않습니다.

원본에서 대비가 낮은 부분은 비교 화면에서 원래 색을 보존했습니다. 라이브러리는 역할 토큰과 기준 팔레트로 검수했습니다. DOM 대비 검사는 그라디언트의 최악 색상과 투명 글자, 의사 요소 채움 때문에 오탐이 있으므로 경고를 삭제하지 않고 실제 색상·화면 검토 결과와 함께 남겼습니다. raw overflow 역시 외부 연결선·라벨을 포함하며 실제 글자 잘림 검사와 구분됩니다. 원본 대비 픽셀 100% 일치와 라이브러리 사용 가능성은 별도로 기록했습니다. 재작업 이전 audit 파일은 경과 기록이고 최종 검사는 `audit-parent-*-final.json`, `delivery-validation.json` 및 최종 PNG/PDF를 기준으로 봅니다.

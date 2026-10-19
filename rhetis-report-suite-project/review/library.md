# Rhetis Report Suite 컬렉션 검수

## 범위와 계약

첨부 `rhetis-kit-reference.zip`의 README.md 전체를 먼저 읽고, taxonomy 2026-10-18.1과 4개 계약 JSON을 기준으로 작성했다. `atlas`와 `miri`는 파일 형식·root 클래스·fixture 사용 방식만 참고했다. 해당 예시의 디자인이나 CSS를 복제하지 않았다.

- 컬렉션: `collection/rhetis-report-suite/`
- 공유 토큰: 63개. 색상 토큰은 light/dark 각각 정의.
- foundation: 1280×720, 12열×6행, seat와 cover fixture.
- 요소: 계약의 31개 전부. 각 요소의 설명, source JSON, CSS, 2개 이상의 fixture.
- fixture: foundation 2개 + 요소 77개 = 총 79개.
- 기본·강조·quiet·line·5개 tone 카드, 최소/최대 멤버 수, 세로/가로 프로세스, 교대 timeline, 다중 요금제·팀 구성을 포함한다.
- 요소 CSS는 해당 `data-el` root 내부에만 적용하며 외부 이미지·폰트·URL·애니메이션을 사용하지 않는다. 글자 크기는 허용된 `--type-N`으로만 선언한다.

## 참고 이미지의 해석

005의 얇은 검정 테두리·하늘색 보고서 프레임·연노랑 강조, 006의 정돈된 정보 위계와 선 중심의 편집, 007의 stone/beige 계열과 여백, 008의 sage 모듈, 009의 cobalt/lime 강조를 공통 보고서 언어로 연결했다. 컬렉션의 주 강조색은 cobalt, 결론과 선택 영역은 연노랑이며, 하늘색·sage·beige·lime을 보조 tone으로 쓴다. 다크 모드는 charcoal 표면, 밝은 청보라 강조와 별도의 파스텔 tone 잉크로 구성했다.

직접 등장하지 않는 cycle·hub·architecture·pricing 등도 같은 선 두께, 제한된 모서리 곡률, 정렬, 수치 위계로 설계했다. 사진이나 복잡한 삽화를 새로 만들지 않고, 계약의 번호가 있는 단색 seat로 자리만 확보했다. fixture의 한국어 문구는 원본 복원 문구가 아니라 요소의 실제 사용성을 검증하기 위해 작성한 업무 예문이다.

## 실제 브라우저 검수

Chromium + Playwright로 79개 fixture를 각자의 선언된 최소 칸과 전체 12×6 칸에 렌더했다. light/dark 두 모드를 확인했다. cover는 전체 크기만 검사하므로 최종 PNG는 314장이다. 모든 PNG의 실제 IHDR 크기는 1280×720이다. 각 요소의 개별 PNG를 열어 숫자, 줄바꿈, 제목과 설명 간격, chip·pill 중앙 정렬, 다크 표면 대비, 연결선과 화살표를 확인했다. 연락처 시트만으로 검수를 끝내지 않았다.

전체 시각 비교·수정은 3회 수행하고, 마지막에 대비 수정이 있었던 agenda만 집중 재캡처했다. 마지막 CSS를 모든 fixture에 다시 적용한 자동 검증도 수행했다.

| 최종 검사 | 결과 |
|---|---:|
| 계약·정적 검사 오류 | 0 |
| 실제 브라우저 검증 사례 | 314 |
| 칸 밖으로 나간 요소·가로 글자 초과 | 0 |
| 실제 글리프 경계 기준 텍스트 겹침 | 0 |
| 텍스트 대비 미달 | 0 |
| 페이지 크기 오류 | 0 |
| 기본 한국어 폰트 준비 실패 | 0 |

대비 검사는 실제 계산된 글자색과 조상 표면의 알파 합성 결과를 비교했다. 28px 미만은 4.5:1, 28px 이상은 3:1을 기준으로 했다. 텍스트 겹침은 폰트의 여분 ascender/descender 공간을 실제 글리프 영역과 구분했다. 큰 숫자의 line box만 겹치는 경우가 실제 글자 충돌로 오인되지 않도록 Canvas의 글리프 측정을 함께 썼다.

## 발견 후 수정한 사항

1. 중첩 list의 size containment 때문에 pricing과 versus 안에서 제목·목록이 겹쳤다. 중첩 list는 내용 높이를 계산하도록 수정했다.
2. 8항목 목록의 전체 높이와 4항목 numbered 목록의 최소 칸 초과를 멤버 수에 따른 간격·서체 단계로 수정했다.
3. 세로 timeline의 최소 칸을 4×6으로 명시하고 연결선을 각 milestone에 정확히 정렬했다. 교대형은 같은 축의 위·아래에 내용을 실제로 나누었다.
4. 다크 pyramid·matrix·venn의 연한 tone 표면에는 별도 어두운 잉크를 사용했다. 다크 agenda 선택 행의 숫자·화살표도 연노랑용 잉크로 수정했다.
5. 세 원 venn의 중앙 label이 core에 가리지 않도록 위로 분리했다.
6. 한국어 단어 중간의 부자연스러운 줄바꿈을 keep-all로 완화했다.
7. line chart의 선이 실제 Chromium에서 이어지는 것을 확대 확인했다. 복수 차트의 anchor 이름 충돌을 막기 위해 `anchor-scope: all`을 쓴다.

## 판단과 제한

다섯 덱의 색과 편집 관습이 서로 달라, 하나의 컬렉션으로 쓸 때에는 cobalt·연노랑을 공통 축으로 삼고 sage·beige를 보조 tone으로 통합했다. 31개 계약을 모두 채우는 과정에서 원본에 없는 요소는 시각 언어를 확장한 설계 판단이다. 픽셀 복원 슬라이드와 컬렉션 fixture는 서로 다른 목적의 산출물이다.

독립 컬렉션은 외부 리소스를 금지한 계약을 따르므로 `@font-face`를 포함하지 않는다. 검수 환경에 실제 설치된 `Noto Sans CJK KR`의 regular/bold를 사용했고, font stack은 공유 토큰에만 둔다. collection의 차트 선 연결은 CSS anchor positioning을 지원하는 최신 Chromium을 기준으로 검증했다.

## 재생성

프로젝트 루트에서 다음 명령으로 계약 형식의 light/dark 시트를 다시 생성할 수 있다.

```sh
python tools/preview.py collection/rhetis-report-suite contract/type-steps.json --out collection/rhetis-report-suite/preview-light.html
python tools/preview.py collection/rhetis-report-suite contract/type-steps.json --dark --out collection/rhetis-report-suite/preview-dark.html
```

작성·검수 중간 자료는 `/workspace/work/library-renders/`에 있으며, 최종 결과는 `audit.json`, `summary.json`, `static-validation.json`과 개별 PNG 314장이다. 최종 컬렉션 ZIP은 `rhetis-report-suite/` 하나만 최상위에 포함하고 압축 자체 검사를 통과했다.

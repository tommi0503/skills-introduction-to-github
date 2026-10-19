# Rhetis Spectrum 라이브러리 검수

완성 범위는 `collection/rhetis-spectrum/`의 키트, foundation, 요소 31종이다. 요소 fixture 90개와 foundation fixture 2개, 총 92개를 작성했다. 이 폴더에는 HTML·CSS·JSON·영문 설명만 들어 있으며 원본 이미지, 폰트 파일, 외부 리소스는 넣지 않았다.

## 참고 이미지에서 읽어낸 디자인 언어

- 077: 크림색 문서의 얇은 남색 테두리와 정돈된 정보 패널, 수치 중심의 위계.
- 078: 파란 구조색, 분명한 단계 구분, 작은 원형 강조점과 연결선.
- 079: 주황 강조색, 직각 프레임, 간결한 회색 구획, 절제된 여백.
- 080: 연노랑 종이 탭, 가는 회색 선, 숫자 라벨, 차분한 문서 구성.
- 084: 깊은 네이비 바탕, 선명한 파란 정보 위계, 정교한 표와 비교 패널.

이 언어를 흰 문서 바탕·청회색 얇은 선·작게 둥근 직각 프레임·coral 실행 강조·paper-yellow 라벨·deep-blue 구조색으로 통합했다. 참고 이미지에 없는 요소도 같은 원리로 직접 설계했다. atlas/miri의 디자인 CSS를 복제하지 않았으며 계약 구조와 fixture 형식만 확인했다.

## 구현과 판단

공유 토큰 전체를 정의했고 색은 라이트·다크 각각 설계했다. 작은 coral 글자의 대비를 확보하기 위해 `--accent-text` 확장 토큰을 추가하고 `kit.json`의 `extensions`에 `color`로 선언했다. 기본 강조 면은 밝은 coral을 유지한다. 의도한 텍스트/표면 토큰 조합의 대비 최솟값은 **5.21:1**이며 산식 결과는 `library-palette-contrast.json`에 있다.

모든 요소 CSS 선택자는 해당 요소의 `data-el="rhetis-spectrum-…"` 범위 안에 있다. 글자 크기는 계약의 `--type-N`, 색·폰트·굵기·행간·자간·간격은 토큰을 사용한다. 각 요소에 `@container` 단계를 두었다. fixture의 최소 칸은 모두 단일 크기로 선언했으며 12×6 전체 크기와 그 최소 크기를 모두 렌더했다. 작은 칸에서 `fig`와 `name`은 유지한다.

선 차트는 실제 데이터 점의 위치를 CSS anchor positioning으로 연결하며 상승·하강 구간을 모두 지원한다. 숫자와 월 라벨은 실제 텍스트이다. cycle/hub의 멤버 3·4·5·6개, funnel 3~6단계, pyramid 3~5단계, hierarchy 2~4분기, architecture 2~5레이어의 변형을 각각 포함했다. 리스트 번호, 단계 화살표, 조직도 연결선은 CSS가 그린다. pricing/versus의 중첩 리스트도 독립적인 `data-el`을 갖는다.

## 브라우저 검수

공식 명령 두 개로 `light.html`, `dark.html`을 생성했다.

```sh
python tools/preview.py collection/rhetis-spectrum contract/type-steps.json --out light.html
python tools/preview.py collection/rhetis-spectrum contract/type-steps.json --dark --out dark.html
```

Chromium에서 실제 로컬 Pretendard 400·600·700 및 Gmarket Sans 700 폰트를 로드해 **364개 뷰**를 렌더했다. foundation 2개는 각 모드 전체 크기만, 요소 90개는 각 모드의 전체/최소 크기로 확인했다. 모든 PNG는 정확히 **1280×720**이다. PNG는 `renders/library/{light,dark}/{full,minimum}/`에 있으며 최종 파일 SHA-256은 `library-automatic.json`에 기록했다.

검수는 초기 렌더, 구조 수정, 최종 시각·대비 확인의 세 단계로 진행했다. 개별 요소의 라이트/다크 최소 칸을 모두 시각적으로 확인했고, foundation·선 차트·태그·다항목 목록·수정된 다크 강조 요소는 1280×720 개별 렌더를 열어 재확인했다. `renders/library/inspection/`의 보조 시트는 해당 개별 PNG에서 생성했다.

발견하고 고친 사항:

1. 선 차트의 퍼센트 margin이 너비를 기준으로 동작하던 문제를 제거하고, 데이터에 따라 높이가 정해지는 anchor 위치로 변경했다. 상승·하강 선이 각 점에 연결되는 것을 개별 이미지로 확인했다.
2. inline 태그의 size containment 때문에 글자가 세로로 흘렀던 문제를 수정했다. 태그는 intrinsic width와 실제 글자 중앙을 유지한다.
3. 8항목 번호 목록이 위아래로 넘쳤던 문제를 항목 수에 따른 간격/타입 단계로 수정했다.
4. 다크 모드에서 노랑 강조 면 위의 pale-blue/white 글자가 약했던 delta·highlight·Venn의 전경색을 수정했다. callout의 핵심 구절도 전용 노랑 면/짙은 글자 조합으로 정리했다.
5. matrix의 세로 축에 붙었던 180도 회전을 제거해 한글이 거꾸로 보이지 않도록 했다.
6. 6개 metric의 수치와 이름 행 높이를 맞췄고 막대의 tone 1~5가 실제로 각기 다른 면색을 갖도록 확인했다.

최종 자동 결과: **텍스트의 root 영역 초과 0건, 폰트 로딩 실패 0건, 페이지 크기 불일치 0건**. 마지막으로 바뀐 7개 요소는 렌더와 파일 해시를 다시 갱신했다. 소스 계약 검사도 **31요소/90 element fixtures 통과**했다. 이 검사는 제공된 계약의 휴대용 검사이며 Rhetis 서버 importer의 정식 admission을 실행한 결과라고 주장하지 않는다.

## 해석이 갈린 부분과 한계

서로 다른 다섯 덱은 모서리·바탕색·강조색이 다르므로, 하나의 컬렉션에서는 청회색 선과 직각 문서 구조를 공통으로 두고 coral/yellow/blue를 역할별 강조로 분리했다. 사진·3D·화면·로고의 실제 모양은 그리지 않고 계약의 회색 seat로 남겼다. 작은 참고 이미지에서 읽을 수 없는 문구를 library fixture에 옮기지 않았으며, fixture 내용은 읽을 수 있는 한국어 비즈니스 문장으로 새로 작성했다.

선 차트의 순수 CSS 연결은 CSS anchor positioning을 지원하는 현대 Chromium을 기준으로 검수했다. 컬렉션 소스에는 외부 폰트/이미지 경로가 없으며 최종 호스트가 실제 폰트를 공급해야 한다.

## 통합 검수 후 inline 계약 수리

주 에이전트 통합 검수에서 `.hl`이 큰 면 패널처럼 렌더되는 문제를 확인했다. `.hl`만 실제 inline 표시, intrinsic width, 20px 타입 단계, 상하 padding 0, 좌우 토큰 padding 4px, baseline 정렬 및 줄별 box decoration으로 수정했다. `.tag`와 다른 요소는 변경하지 않았다. 두 tag fixture의 light/dark 전체·최소 8뷰를 다시 렌더하고 공식 light/dark 시트와 소스·PNG 해시를 갱신했다. 최종 자동 결과는 계속 364뷰·0 findings다.

# Studio Spectrum 컬렉션 검수 기록

## 결과

31개 계약 요소, 요소 fixture 95개, foundation fixture 2개를 제작했다. 모든 요소는 최소 2개 fixture를 가지며 카드의 9개 표면 변형, pill의 4개 변형, 관계도 3~6개 멤버, 표·리스트·목차의 밀도 차이를 포함한다.

Chromium에서 라이트/다크의 모든 fixture를 실제 렌더했다. 12×6 기본 배치와 fixture 첫 줄에 선언한 최소 칸의 모든 OR 조합을 합해 554개 배치를 검사했다. 글자 DOM Range와 요소 경계를 비교한 영역 초과는 0개다. PNG 554개는 모두 1280×720이다. 페이지별 원본 크기 렌더를 확보하고 각 요소 패밀리의 실제 이미지와 좁은 칸의 대표 사례를 개별 시각 검토했다.

1504개 텍스트에 대해 실제 계산된 전경·배경색으로 대비를 검사했다. 미달은 0개, 관찰된 최저 대비는 5.56:1이다. 28px 미만은 4.5:1, 그 이상은 3:1 기준을 적용했다. 복잡한 사진·일러스트·로고는 회색 numbered seat로 남겼다. 외부 이미지나 원본 슬라이드 전체를 요소에 포함하지 않았다.

## 디자인 해석

첨부 README를 끝까지 읽고 계약·공유 토큰·클래스 구조를 확인했다. atlas/miri는 폴더·schema·fixture 형식만 확인했으며 디자인 CSS를 복사하지 않았다. 참고 10개 덱의 공통 언어로 편집형 여백, 얇은 rule, 작은 kicker, 선명한 타이포 위계, 평면적인 데이터 표현을 추출했다. 기본 navy에 red, lime, green, pale yellow의 tone을 구성했다. 작은 모서리와 그림자 없는 표면을 공통 기준으로 삼았다. 표지의 작은 radial-gradient는 03/04 덱의 부드러운 색 영역을 토큰만으로 표현한다.

원본들의 serif, condensed sans, 일반 sans가 서로 다르므로 컬렉션은 한국어 실제 문장을 위한 Pretendard로 통일했다. 원본별 글꼴 재현은 별도 복제 슬라이드에서 다루고, 라이브러리 fixture는 그 언어를 확장하는 한국어 비즈니스 예문으로 새로 작성했다. fixture의 수치와 인물은 디자인을 검증하기 위한 예시다. 읽히지 않는 글자를 선으로 흉내 내지 않았다.

## 발견한 문제와 수정

- 도넛의 가운데가 뚫리지 않던 마스크를 제거하고 토큰색의 내부 원으로 구성했다.
- 선 차트의 CSS anchor 연결 위치와 기울기 방향을 실측해 수정했다.
- cycle/hub의 3~6개 멤버를 균형 있게 배치하고 hub의 spoke를 기하식으로 연결했다.
- 8개 리스트·목차, 5개 아키텍처 레이어의 좁은 칸에서 글자 단계와 간격을 낮췄다. 정말 좁은 리스트에서는 note를 숨기며 name과 figure는 유지한다.
- tag의 size containment로 발생한 세로 글자 문제를 intrinsic width로 수정하고 pill/chip의 시각적 중앙을 확인했다.
- table의 브라우저 기본 검정색을 명시적인 --ink로 바꾸어 다크 모드 대비 문제를 해결했다.
- foundation portrait seat의 aspect-ratio가 그리드 밖으로 넘치던 문제를 실제 칸의 width/height로 고정했다.
- 다크는 page/surface/ink와 각 accent의 대비 관계를 별도로 정했다. 단순 색 반전은 사용하지 않았다.

브라우저 검수 초기의 about:blank 문서에서 외부 폰트를 부르는 방식은 CORS로 실패했다. 이를 동일 localhost origin에서 문서를 여는 방식으로 수정하고, 전체 554개 PNG와 대비 검사를 실제 Pretendard 폰트로 다시 생성했다. 최종 결과는 이 재생성본이다.

## 계약 확인과 재현

kit 및 foundation schema, 31개 contract ID, 영어 description, data-el 접두사, fixture의 첫 줄 min 주석과 grid 배치를 확인했다. CSS에서 색 리터럴·외부 리소스·@import·@font-face·크기 px 글꼴·숫자 굵기를 사용하지 않았다. 폰트 이름은 kit token에만 둔다. 브라우저 검수 시에만 별도로 실제 Pretendard variable WOFF2를 주입하고 라이트/다크 모두 fontLoaded=true를 확인했으며 컬렉션 CSS에는 외부 font loader를 넣지 않았다.

제공된 tools/preview.py의 표준 명령으로 preview-light.html과 preview-dark.html을 재생성했다. 실제 Rhetis intake 서버는 이 환경에 포함되지 않으므로 반입 검증을 실행했다고 주장하지 않는다. 상세 배치별 결과와 최종 소스 SHA-256은 library-qa.json에 기록했다.

원본 시트: contact/03, 04, 09, 10, 11, 13, 19, 22, 24, 32. 로컬 브라우저 산출물: /workspace/work/library-review/{light,dark,light-min,dark-min}/. 이 문서는 라이브러리 컬렉션의 검수 범위이며, 107개 복제 슬라이드의 원본/결과 차이 검수는 별도 기록을 따른다.

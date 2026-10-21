# EONU v2 HTML 뷰어 연동 검수

- 검수일: 2026-10-21 (Asia/Seoul)
- 대상: `eonu-ir-20261021-v2`, 실제 슬라이드 12장 × 와이어프레임/시안
- 결과: 182개 기능·규격 검사 통과. 개별 HTML 24개와 인쇄용 HTML 2개 확인.
- 자동 증빙: `viewer-check.json`
- 직접 열람한 UI 캡처: `viewer-desktop.png`, `viewer-mobile.png`
- 재검수: Playwright와 `/usr/bin/chromium`이 있는 환경에서 `node review/verify-viewer.cjs`

## 이번 수정

표지와 마지막 장처럼 섹션명이 비어 있으면 하단 뷰어의 빈 섹션 라벨과 세로 구분선을 함께 숨기도록 수정했다. 본문 페이지는 섹션 라벨과 구분선을 유지한다. 슬라이드 본문 소스는 수정하지 않았다.

## 검수 결과

1. 01/12장 양쪽 스타일의 슬라이드 내부에는 섹션 라벨이 없고, 뷰어의 빈 라벨·구분선도 숨겨진다.
2. 02~11장에서는 현재 한글 섹션명이 정상 표시된다.
3. 24개 페이지 모두 1280×720 캔버스이며, 현재 모드 버튼의 선택 상태와 개별 HTML 링크가 일치한다.
4. 좌우/Home/End 키, 페이지 선택, 첫·끝 버튼 비활성, 모드 전환, 그리드 선택, 대본 토글/Escape가 작동한다.
5. 현재 페이지의 대본은 슬라이드 데이터와 일치한다. 전체 보기에는 실제 HTML로 렌더링한 12개 미리보기가 있다.
6. 독립 HTML 24개에서 해당 장이 하나씩 보이고 로컬 Pretendard가 로드된다. 인쇄용 HTML은 각각 12장이다.
7. 390px 모바일에서 뷰어·그리드·독립 HTML에 가로 넘침이 없다. 16:9 비율을 유지한다.
8. 기획 검토 메뉴를 클릭해 새 탭을 열고 문서 제목을 확인했다. 기획 HTML과 양쪽 PDF는 모두 HTTP 200이며 PDF 시그니처가 올바르다.
9. 검사 중 브라우저 페이지 오류 및 실패한 리소스 요청은 없었다.

## CSS 규격과 글꼴

`src/viewer.css`의 `px` 단위 값 139개를 검사했다. 모두 짝수 정수이며 홀수·소수 선언은 없다. 뷰어 및 버튼·선택 입력·미리보기 캡션의 글꼴 선언은 Pretendard이고, 실제 로딩도 확인했다. 임의 창 크기에 맞춘 비례 축소에서는 런타임의 표시 영역에 소수 픽셀이 생길 수 있다. 이는 종횡비를 보존하기 위한 렌더링 값이며 고정 CSS 규격과 구분한다.

## 시각 확인 범위

데스크톱 표지에서 뷰어 메뉴·캔버스·페이지 탐색이 겹치지 않는다. 표지의 하단에는 모드명만 남고 빈 세로 구분선은 보이지 않는다. 모바일에서 상단 스타일 전환과 하단 페이지 이동이 개별적으로 조작 가능하다. 캡처는 CSS 전환 애니메이션을 완료시킨 상태로 저장했다. 슬라이드 전체의 내용·시각 검수는 별도 렌더 검수 범위다.

## 환경 제약

이번 실행에서 `file://`을 다시 시도했고 관리형 Chromium의 `ERR_BLOCKED_BY_ADMINISTRATOR` 차단을 확인했다. 따라서 실제 기능 검사는 localhost HTTP에서 수행했다. 환경 정책을 바꾸거나 우회하지 않았다. 구조는 상대 경로 HTML/CSS·classic JavaScript·로컬 폰트만 사용하며 fetch·CDN·ES module·서버 API 의존성이 없다. 이 환경에서 file:// 직접 실행이 검증됐다고 주장하지 않는다.

Chromium 실행 및 localhost 검사에는 `exec_command`의 `sandbox_permissions: with_additional_permissions`, `additional_permissions.network.enabled: true`가 필요하다. 기본 sandbox에서는 Chromium 내부 소켓 생성이 차단된다.

## 도착 링크

| 파일 | HTTP | 검사 시 byte 수 |
|---|---:|---:|
| `docs/planning.html` | 200 | 52,414 |
| `previews/eonu-design.pdf` | 200 | 1,466,035 |
| `previews/eonu-wireframe.pdf` | 200 | 1,426,072 |

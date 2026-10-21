# EONU HTML 뷰어 연동 검수

- 검수일: 2026-10-21 (Asia/Seoul)
- 대상: 최신 실제 슬라이드 데이터 12장 × 와이어프레임/시안 2종
- 결과: 브라우저 기능 검사 118개 통과. 생성한 개별 HTML 24개와 인쇄용 HTML 2개를 확인했다.
- 자동 증빙: `viewer-check.json`
- 눈으로 확인한 화면: `viewer-desktop.png`, `viewer-mobile.png`

## 확인한 기능

1. 첫 실행은 시안 01장이고 이전 버튼은 비활성화된다.
2. 12장 전체를 두 가지 모드에서 렌더링하며 실제 캔버스는 1280 × 720이다.
3. 좌우 키, Home/End, 페이지 선택, 이전/다음 버튼의 경계 처리가 작동한다.
4. 스타일을 전환해도 현재 페이지가 유지되고 해시 주소가 갱신된다.
5. 전체 보기에는 12장의 실제 HTML 축소 미리보기가 나타나며 선택한 장으로 이동한다.
6. 발표 대본은 현재 슬라이드의 대본과 일치한다. Escape로 대본과 그리드를 닫는다.
7. 개별 HTML, 현재 모드의 PDF, 현재 모드의 인쇄용 HTML, 기획 검토 문서로 연결한다.
8. 개별 HTML 24개에서 해당 페이지가 하나씩 표시되고 로컬 Pretendard가 로드된다.
9. 각 인쇄용 HTML에는 순서대로 12장이 있다.
10. 폭 390px의 모바일에서 뷰어/그리드/개별 HTML의 가로 넘침이 없다.
11. 검사 중 브라우저 JavaScript 오류와 실패한 리소스 요청은 없었다.

## 시각 확인

데스크톱에서는 상단의 스타일/검토 메뉴, 중앙 16:9 슬라이드, 하단 페이지 이동이 분리되어 보이며 서로 겹치지 않는다. 시안의 연보라 포인트와 중립 배경을 뷰어에서도 이어 갔다. 모바일은 16:9 비율을 유지한 축소 화면으로 보이며, 상단 스타일 전환과 하단 이동 버튼은 별도로 조작할 수 있다. 자세한 본문 검토는 큰 화면이나 PDF가 적합하다. 개별 슬라이드 내부의 시각·본문 검수는 별도 렌더 검수에서 다룬다.

## 실행 환경과 오프라인 구조

이 관리형 Chromium은 `file://` 탐색을 `ERR_BLOCKED_BY_ADMINISTRATOR`로 차단하므로 실제 브라우저 검사는 localhost HTTP에서 실행했다. 환경 정책을 변경하거나 우회하지 않았다. HTML은 상대 경로의 CSS·classic JavaScript·로컬 폰트만 사용하며 fetch, CDN, ES module, 서버 API에 의존하지 않는다. 따라서 일반 브라우저에서는 압축 해제 후 `index.html`을 열 수 있는 정적 구조다. 이 환경에서 file:// 직접 실행을 검증했다고 주장하지 않는다.

Chromium 실행과 localhost 검사는 `exec_command`의 `sandbox_permissions: with_additional_permissions`, `additional_permissions.network.enabled: true`가 필요했다. 기본 sandbox에서는 Chromium 내부 소켓 생성이 `setsockopt: Operation not permitted`로 차단되었다.

재검수는 Playwright와 `/usr/bin/chromium`이 설치된 환경에서 `node review/verify-viewer.cjs`로 수행한다. 이 스크립트는 임시 localhost 서버를 열고 검사 후 닫으며, 결과 JSON과 두 장의 뷰어 캡처를 갱신한다.

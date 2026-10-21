# EONU v3 HTML 뷰어 검수

2026-10-21. `review/verify-viewer.cjs`로 최종 소스에서 182개 검사를 통과했습니다. 상세 결과와 검사 시점 소스 해시는 `viewer-check.json`에 있습니다.

- 시안/와이어프레임 24개 화면, 각 1280×720.
- 좌우/Home/End 키, 페이지 선택, 스타일 전환과 현재 페이지 유지.
- 전체 보기 12개 실제 HTML 미리보기와 클릭 이동.
- 발표 대본 일치, 열기/닫기, Escape.
- 표지·마지막 장의 슬라이드 섹션 타이틀 및 뷰어의 빈 섹션 라벨·구분선 없음.
- 본문 2–11장에는 현재 섹션 표시.
- 개별 HTML 24개, 12장씩의 인쇄용 HTML, PDF 링크.
- 기획 문서 팝업과 PDF의 실제 HTTP 200 및 PDF 시그니처.
- 390px 모바일 뷰어·그리드·개별 페이지에 가로 넘침 없음.
- 로컬 Pretendard 로딩, 뷰어 CSS 고정 px 값 139개 전부 짝수 정수.
- 브라우저 페이지 오류와 실패한 리소스 요청 없음.

실제 캡처는 `viewer-desktop.png`, `viewer-mobile.png`입니다. UI 전환 애니메이션이 끝난 화면으로 저장했습니다.

관리형 Chromium의 정책으로 `file://` 직접 접근은 `ERR_BLOCKED_BY_ADMINISTRATOR`로 차단됐습니다. 실제 기능 검수는 localhost HTTP에서 수행했으며 직접 파일 열기가 이 환경에서 검증됐다고 주장하지 않습니다. 배포 폴더는 상대 경로 HTML/CSS, classic JavaScript, 로컬 폰트를 사용하고 외부 API·fetch·CDN·ES module 실행에 의존하지 않습니다.

`scripts/verify-delivery.py`에서 검수 당시 뷰어 해시와 최종 파일의 일치를 다시 확인합니다.

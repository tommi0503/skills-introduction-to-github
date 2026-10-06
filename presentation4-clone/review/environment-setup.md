# 클라우드 환경 설정

cloud-environment-onboarding:setup 스킬을 적용했다. 기존 체크아웃을 사용했고 별도 worktree를 만들지 않았다. 기존 프로젝트의 소스나 설정을 수정하지 않았다.

Node v24.19.0, npm 11.9.0, Python 3.12, /usr/bin/chromium 및 Pillow를 확인했다. npm ci --cache /workspace/.npm-cache --no-audit --no-fund가 성공했고 production 빌드와 실제 Chromium 렌더·검사가 성공했다. npm 기본 캐시는 이 환경에서 쓰기 권한이 없으므로 /workspace/.npm-cache를 사용한다. 개발 서버 5297 포트의 HTTP 응답과 갤러리/덱/비교/슬라이드 브라우저 동작을 확인했다.

테스트한 설치·시작 절차를 클라우드 설정 초안에 저장했다. API 응답 status=saved, requires_publish=true이다. 초안 저장은 설정 적용·발행·재시작을 의미하지 않는다. 활성화하려면 환경 설정에서 내용을 검토·저장한 뒤 Publish해야 한다. 저장소 목록, 네트워크 정책, 비밀 값은 변경하지 않았다. 새 작업의 자동 복원은 별도로 검증하지 않았다.

원본 CSV는 내용과 BOM을 유지하고 Git의 공백 검사에 맞춰 줄 끝만 LF로 정규화했다. 렌더 소스에는 변화가 없다.

# 다음 작업 지침

기존 /workspace/skills-introduction-to-github 체크아웃의 presentation5-clone을 사용한다. 사용자가 요청하지 않은 Git worktree를 만들지 않는다. 다른 프로젝트를 보존하고 slides-clone을 확인하지 않는다.

README.md, review/inventory.md, review/integrated.md, public/reference/manifest.json 및 review/group-*.md를 읽는다. 두 ZIP의117개 참고시트47개덱을1057개 독립1280×720페이지로 나눈다. 시트 UI를 결과로 만들지 않는다. 원본시트는 비교용이고 결과화면 배경으로 사용하지 않는다. 복잡한이미지영역은#e5e5e5 placeholder로 둔다. 단순도형·표·차트·텍스트·Lucide아이콘은실제로구현한다.

기본경로는프로젝트폴더이다. npm ci --cache /workspace/.npm-cache --no-audit --no-fund, npm run build로 준비한다. npm run dev -- --host 127.0.0.1 --port 5298 --strictPort로 시작한다. 실제 로컬폰트와 굵기를 로드하고 작은참고의 글자크기/간격/leading/줄바꿈을 주의한다. chip은실제글자경계로시각적중앙을보정한다. 판독불가문구는 정상문구로대체하고페이지별기록한다. OCR오인식이나문자실루엣contour를최종결과로두지않는다.

수정후 실제브라우저로 해당페이지를 렌더하고 원본과나란히개별검토한다. 마지막변경후 npm run build, npm run render -- --round=final --production, npm run verify, npm run package 순으로전체검증한다. 데이터/렌더러/PNG해시로최종소스와결과일치를확인한다. GitHub push는 기존HTTPS프록시인증을사용하며강제push하지않는다. 모든ZIP을실제GitHub에서다시다운로드해SHA-256,CRC,전체1057개PNG크기를검증한다. 실제실행근거가있을때만테스트/업로드/다운로드성공을보고한다.

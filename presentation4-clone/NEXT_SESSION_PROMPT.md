# 다음 작업 지침

기존 `/workspace/skills-introduction-to-github/presentation4-clone` 체크아웃을 사용한다. 각 클라우드 작업은 이미 격리되어 있으므로 사용자가 요청하지 않은 Git worktree를 만들지 않는다. 기존 다른 프로젝트를 보존하고 `slides-clone`을 확인하지 않는다.

`README.md`, `review/inventory.md`, `public/reference/manifest.json`, `review/group-*.md`, `review/integrated.md`를 읽는다. 기본 작업 경로는 프로젝트 폴더이며 `npm ci --cache /workspace/.npm-cache`, `npm run build`로 준비한다. `npm run dev -- --host 127.0.0.1 --port 5297 --strictPort`로 시작한다.

43개 덱 77장은 동일한 1280×720이다. 원본 1600×900의 비율을 유지하고, 공통 모델·렌더러·팩토리를 유지한다. 복잡한 이미지 영역은 #e5e5e5 placeholder로 두며 원본 이미지는 비교용으로만 사용한다. 읽기 어려운 문구는 정상 문구로 대체하고 기록한다. 실제 폰트 파일과 굵기를 로드한다. chip은 글자 경계로 시각적 중앙을 보정한다.

수정 후 반드시 실제 브라우저로 해당 슬라이드를 렌더하고 원본과 나란히 개별 검토한다. 최종 캡처는 `npm run build` 후 `npm run render -- --round=final --production`; `node scripts/verify.mjs`로 데이터/렌더러/PNG 해시, 글자 경계와 폰트, chip 정렬을 확인한다. 전체 변경이 끝나면 `python3 scripts/package.py`로 ZIP과 미리보기를 갱신한다. 테스트 통과와 업로드/다운로드 검증은 실제 실행 근거가 있을 때만 보고한다.

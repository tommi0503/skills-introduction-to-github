# 빌드와 미리보기

`index.html`은 페이지 선택형 비교 미리보기입니다. 압축을 풀고 폴더를 HTTP 정적 서버로 제공하면 됩니다. `assets/fonts/`에 실제 사용 글꼴을 동봉했습니다.

수정이 모두 통합된 소스는 `build_replica.py`, `build_collection.py`, `build_reassembled.py`입니다. 제공받은 레퍼런스 ZIP을 `/workspace/work/ref`, 원본 이미지를 `/workspace/work/deck`에 풀어 둔 환경에서 실행했습니다. `render.py replica`, `render_library.py`, `render.py reassembled` 순서로 Chromium 렌더를 생성합니다. 상위 프로젝트를 `127.0.0.1:8765`로 제공하는 정적 서버를 사용합니다. `refine*.py`는 검수 과정의 기록용 일회성 변환 파일이며 완성된 build 소스에 다시 적용하지 않습니다.

컬렉션 폴더에는 허용 확장자의 소스만 포함됩니다. review의 PNG/PDF/폰트/검수 JSON/Python 파일은 컬렉션 반입 파일이 아닙니다.

# 검수 소스 재현

페이지 소스는 replica/와 reassembled/의 HTML이며 fonts/를 상대경로로 참조합니다. reassembled/collection.css는 컬렉션의 tokens·foundation·요소 CSS와 JSON 등록 기본값을 합친 파일입니다. 추가 페이지 CSS는 없습니다. library/light.html·dark.html도 상대경로로 폰트를 로드합니다.

도구는 제작 환경의 경로를 기록한 실행 소스입니다. 다른 환경에서 실행하려면 Python/Node 파일의 `/workspace/work/deliverables/skylight`, `/workspace/work/deliverables/skylight-review`, `/workspace/work/agents/038`, reference와 원본 deck 경로를 해당 로컬 위치로 바꾸십시오. Rhetis reference pack, Python(Pillow, PyMuPDF), Node Playwright와 Chromium이 필요합니다.

review 폴더를 `python -m http.server 8138 --bind 127.0.0.1`로 서비스한 뒤 render/check 스크립트를 실행합니다. 원본 PNG 자체는 review에 복제하지 않았으며 비교 PNG의 왼쪽에 포함됩니다. 1280×720의 replica/reassembled HTML은 브라우저에서도 직접 열 수 있습니다.

순서: replica.py → render-replica.js → reassemble.py → build-library.py → render-library.js → contact-library.py → render-reassembled.js → check-pages.js/check-chips.js/stress-library.js → notes.py. 원본/조립 비교와 PDF 묶음은 PNG를 Pillow로 연결했습니다.

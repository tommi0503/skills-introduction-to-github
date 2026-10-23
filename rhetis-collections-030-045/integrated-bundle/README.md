# 전체 컬렉션·복제본 코드 통합 ZIP

[통합 소스 ZIP 다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-collections-030-045/downloads/rhetis-collections-030-045-all-source.zip)

컬렉션6개(요소336종과 모든fixture), replica90장과 라이브러리 조립본90장의 모든코드, 실행용폰트, 계약, 빌드도구, 네이티브슬라이드PNG180장과 미리보기를 포함합니다. 최상위폴더는 `rhetis-collections-030-045/` 하나입니다.

압축을 푼폴더에서 `python3 -m http.server 8000 --bind 127.0.0.1`을 실행하고 `http://127.0.0.1:8000/`을 엽니다. 컬렉션은 `collections/`, 복제본 코드는 `reviews/<name>-review/replica/`, 조립본은 같은경로의 `reassembled/`입니다.

검수PDF·원본PNG·비교PNG·요소시트PNG는 앞서 제공한 검수자료에 있습니다. 통합소스ZIP의 비교미리보기는 게시된 이미지로 연결됩니다. 네이티브HTML과 라이브러리HTML은 포함된 로컬폰트로 실행됩니다.

`verification.json`은 전체 ZIP의 SHA-256·CRC·구조검사 결과입니다. ZIP 내부 `bundle-manifest.json`은 모든 포함파일의 크기·SHA-256을 담았습니다. 중복개별ZIP·게시영수증·Python캐시와 대용량 검수미디어는 소스ZIP에서 제외했습니다.

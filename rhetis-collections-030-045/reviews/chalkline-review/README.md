# Chalkline review

030 교육 자료 안내 덱의 두 페이지에서 추출한 컬렉션입니다.

- `inventory.md`: 전체 원본 목록/페이지 유형/관찰 계약
- `replica/`: 1280×720 HTML/CSS, PNG 2장, 2p PDF
- `compare-replica/`: 원본 | replica 2560×720 PNG
- `library/light.html`, `dark.html`: 제공 preview.py로 생성한 전체 시트
- `library/<element>/light.png`, `dark.png`: 해당 요소의 모든 fixture를 담은 시트(56종 + foundation)
- `library/fixtures-light/`, `fixtures-dark/`: 각 fixture의 원본 해상도 브라우저 캡처(각173장)
- `library/library-light.pdf`, `library-dark.pdf`: 전체173페이지 PDF
- `reassembled/`: 컬렉션 foundation/요소만 사용하는 HTML, PNG 2장, 2p PDF
- `compare-reassembled/`: 원본 | 재조립 2560×720 PNG
- `design-language.md`, `review-notes.md`: 설계/차이/결정/검수 기록
- `automatic-checks.json`: browser stress·대비·폰트·PNG/PDF·SHA-256 기록

HTML은 상대 폰트 경로를 사용합니다. 이 폴더에서 `python -m http.server 8000`을 실행하고 http://127.0.0.1:8000/replica/slide_14.html 등을 여세요. 페이지 HTML 자체가 완전한 소스이며 실행 JavaScript와 원본 슬라이드 배경 이미지가 필요하지 않습니다. library 시트의 아이콘 자리는 reference preview.py 규칙대로 점선 원으로 나타납니다. 실제 Rhetis가 지정 Lucide 아이콘을 채우는 자리입니다.

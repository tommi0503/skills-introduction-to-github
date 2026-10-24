# Replica 요소 단위 재제작

기존 7개 컬렉션과 동결 replica를 보존한 별도 결과다. 컬렉션마다56요소, 총392요소를 새 CSS로 작성했다. source base/계약 변형은 replica HTML의 실측에서 출발하고 나머지는 각 덱의 문법에서 추론했다.

**원본과100% 동일한 조립본은 아니다.** 계약에서 표현할 수 없는 장치·변형·멤버 수는 `GAPS-INDEX.md`와 각 review/GAPS.md에 이유·bbox·제안 마크업을 기록했다. 그 부분은 조립 비교에서 비어 있다.

| 덱 | 컬렉션 ZIP | 검수 ZIP | 소스 | 미리보기 |
|---|---|---|---|---|
| 020 tide-tab | [tide-tab.zip](dist/tide-tab.zip) | [tide-tab-review.zip](dist/tide-tab-review.zip) | [컬렉션](collections/tide-tab) | [요소·페이지](reviews/tide-tab/index.html) |
| 022 cutfield | [cutfield.zip](dist/cutfield.zip) | [cutfield-review.zip](dist/cutfield-review.zip) | [컬렉션](collections/cutfield) | [요소·페이지](reviews/cutfield/index.html) |
| 024 filament | [filament.zip](dist/filament.zip) | [filament-review.zip](dist/filament-review.zip) | [컬렉션](collections/filament) | [요소·페이지](reviews/filament/index.html) |
| 026 portico | [portico.zip](dist/portico.zip) | [portico-review.zip](dist/portico-review.zip) | [컬렉션](collections/portico) | [요소·페이지](reviews/portico/index.html) |
| 027 toggle-grid | [toggle-grid.zip](dist/toggle-grid.zip) | [toggle-grid-review.zip](dist/toggle-grid-review.zip) | [컬렉션](collections/toggle-grid) | [요소·페이지](reviews/toggle-grid/index.html) |
| 028 lamella | [lamella.zip](dist/lamella.zip) | [lamella-review.zip](dist/lamella-review.zip) | [컬렉션](collections/lamella) | [요소·페이지](reviews/lamella/index.html) |
| 030 rulemark | [rulemark.zip](dist/rulemark.zip) | [rulemark-review.zip](dist/rulemark-review.zip) | [컬렉션](collections/rulemark) | [요소·페이지](reviews/rulemark/index.html) |

[요소별 출처:56개 요소×7컬렉션](ORIGINS.md) · [unexpressible 전체 목록](GAPS-INDEX.md) · [SHA-256](dist/SHA256SUMS) · [PNG 크기](dist/png-dimensions.json) · [검수 미리보기](index.html)

## 검사와 보존

- `dist/release-manifest.json`:14ZIP의 SHA-256/CRC,파일 목록과PNG 크기.
- `reviews/<collection>/validation/release-audit.json`:계약56개·모범fixture·최종의존성·min크기검수·font/raster·87페이지검사를 연결한 배포 검사.
- `root-final-review.json`:주 담당자가 직접 연 최종 요소 시트와 페이지 비교PNG의 해시.
- `replica-freeze.json`:이전 replica192파일의 고정 해시. 이번 ZIP은 replica를 다시 만들거나 포함하지 않는다. 이전 저장소 경로에서 보존한다.
- `reviews/*/html`, `reassembled`, `assets`:검수 HTML과글꼴·아이콘 자산. 내려받아HTTP서버로 열면 렌더할 수 있다.
- `tools`:측정·지도·시트·검사·패키징 도구. 원본 작업 환경의 `/workspace/work/reference`, `/workspace/work/delivery`, `/workspace/work/rebuild` 경로를 사용한다. 재실행 시 같은 구조로 준비하거나 도구의 ROOT 경로를 변경한다. bootstrap/foundation 생성기는 최초 골격 기록으로, 최종 요소 CSS에 다시 실행하지 않는다.
- 같은6자 문구 검사에서 계약 모범fixture의 한 일반문장과 충돌한 최소 문구 변경 등 예외는 required-fixture 감사에 명시한다.

## 원격 재다운로드 검증

ZIP을 포함한 커밋 `b839af3bba34a69a2a7de57c30819a0954ac67ea`에서14개파일을실제로다시내려받아HTTP200·SHA-256·CRC·파일목록일치를확인했다. [검증기록](publication-verification.json). ZIP은동일바이트이므로검사한PNG크기와컬렉션최상위폴더/확장자제약도그대로보존된다. 기존브랜치에일반push로만추가했다.

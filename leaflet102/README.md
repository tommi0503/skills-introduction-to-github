# 리플렛 UI 소스 · 102개 화면

이미지 파일을 제외한 독립 React 프로젝트입니다. 51개 양면 리플렛을 공통 컴포넌트와 화면 데이터로 구성하며, 모든 페이지는 1280×910으로 표시합니다. 사진과 복잡한 그림은 CSS 단색 placeholder이므로 외부 이미지 없이 실행됩니다.

```sh
npm ci
npm run dev
npm run build
```

`#/page/001`부터 `#/page/102`까지 개별 화면을 볼 수 있습니다. 첫 화면에는 모든 리플렛의 컴포넌트 미리보기가 표시됩니다. 폰트는 npm 의존성으로 설치하여 로컬에서 로드합니다.

## 배포용 정리

출처 목록의 외부 이미지 주소는 제거했고, 지정된 서비스의 UI 표기는 중립적인 예시 이름과 `www.example.com`으로 변경했습니다. 이미지·비교 이미지·기존 ZIP·설치 의존성·빌드 산출물은 이 배포용 폴더와 ZIP에서 제외합니다. 원본 비교 이미지 없이도 UI를 실행할 수 있습니다.

`src/data/group-*.ts`에는 102개 화면의 데이터가, `src/ui.tsx`에는 공통 텍스트·도형·칩·아이콘·placeholder 렌더러가 있습니다. 화면별 제목은 외부 주소를 제거한 `src/data/manifest.json`에서 관리합니다.

## 검수 및 ZIP 재생성

```sh
npm run render
npm run verify
npm run package
```

렌더 검수에는 `/usr/bin/chromium`이 필요합니다. 첫 두 명령은 로컬 PNG와 페이지별 자동 검사 기록을 생성하며, 배포 ZIP에는 생성된 이미지가 포함되지 않습니다. 원본 이미지가 없는 구성에 맞춰 렌더 스크립트의 이미지 비교 단계는 제거했습니다.

소스 ZIP은 `deliverables/leaflet102-source.zip`입니다. 최종 정리 검수 기록은 `review/source-export-verification.json`에 있습니다. 문서의 DOM `canvas`와 글자 크기 측정용 HTML 태그는 브라우저 기능 명칭입니다.

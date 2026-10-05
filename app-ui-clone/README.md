# App UI Clone

React + Tailwind CSS v4 + lucide-react로 레퍼런스 이미지 26장(약 85개 화면)을 재현한 프로젝트입니다.

## 실행

```bash
cd app-ui-clone
npm install
npm run dev          # http://localhost:5173
```

- `#/` — 전체 갤러리
- `#/compare/NN` — 레퍼런스 이미지와 구현을 나란히 비교
- `#/NN` — 해당 쇼케이스만 1:1 크기로 렌더

## 구조

```
src/
  ui/                     공용 UI 라이브러리 (앱에 종속되지 않는 프리미티브)
    core/                 Stage, Placed, Scaled, cn, ShowcaseDefinition
    device/               PhoneFrame, StatusBar, DynamicIsland, HomeIndicator, 상태바 글리프
    media/                ImagePlaceholder, Avatar
    controls/             IconButton, Button, ChipGroup, SearchField, SegmentedControl, Toggle
    navigation/           TabBar(renderItem 주입), IconLabelTab
  showcases/
    registry.ts           import.meta.glob 자동 등록 (새 쇼케이스 추가 시 수정 불필요)
    sNN/                  레퍼런스 이미지 1장 = 쇼케이스 1개
      index.tsx           Stage 구성 (배경 + 기기 배치)
      screens/            화면 단위 컴포넌트
      components/         앱 전용 재사용 컴포넌트
      data.ts             콘텐츠(텍스트·목록) — 컴포넌트는 데이터를 map 해서 렌더
      theme.ts            색상/폰트 토큰
    shared-naver/         19–22 (네이버페이) 공용 컴포넌트
    shared-canvas/        07–09 공용 헬퍼
public/reference/         원본 레퍼런스 이미지
scripts/                  screenshot.mjs + compare.py (시각 비교 도구)
```

### 설계 원칙 (SOLID)
- **SRP**: 위치(`Placed`), 기기 외형(`PhoneFrame`), 화면 내용(screens), 콘텐츠(data)를 분리.
- **OCP**: `TabBar`의 `renderItem`, `className` 주입, 테마 props로 수정 없이 확장
  (예: 14번 세 가지 컬러 테마가 하나의 `MoodHomeScreen` 템플릿을 공유).
- **ISP**: 컴포넌트는 필요한 최소 props만 받음.
- **DIP**: 갤러리는 `ShowcaseDefinition` 계약에만 의존하고, 구체 쇼케이스는 glob으로 주입.

### 이미지 처리 규칙
사진·일러스트·로고·지도·3D 렌더 등 UI나 lucide로 표현할 수 없는 영역은 모두
`ImagePlaceholder`(연한 회색 단색)로 처리했습니다. 흰 텍스트가 위에 올라가는 사진 영역만
가독성을 위해 조금 더 진한 회색 단색 톤을 사용합니다.

## 시각 검증

```bash
node scripts/screenshot.mjs 05                    # shots/05-side.png, 05-blend.png
node scripts/screenshot.mjs 05 --crop x,y,w,h     # 영역 확대 비교 shots/05-crop.png
```

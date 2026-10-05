# App2 Clone

20개 앱 레퍼런스(약 80화면)를 React + Tailwind CSS v4 + lucide-react로 재현한 프로젝트입니다.
`app-ui-clone`의 뼈대(UI 라이브러리·설정·스크립트)만 복사했고, 기존 디자인은 포함하지 않습니다.

## 실행
```bash
cd app2-clone && npm install && npm run dev
```
- `#/` 갤러리, `#/compare/NN` 레퍼런스(추출본)와 비교, `#/NN` 보드 단독 렌더

## 규칙
- 모든 화면은 `SCREEN` = 390×844 (radius 44), 기울기 없이 `ScreenBoard`(padding 40, gap 40)에 나란히 배치
- 사진·지도·로고·일러스트·lucide 미지원 아이콘 → `ImagePlaceholder` (단색)
- 콘텐츠는 앱별 `data.ts`, 화면은 `screens/`, 앱 전용 부품은 `components/`

## 구조
```
src/ui/                 공용 라이브러리 (board/ScreenBoard·AppScreen·geometry, device/StatusBar·HighlightChip …)
src/apps/aNN/           레퍼런스 1장 = 앱 1개 (import.meta.glob 자동 등록)
public/reference/       원본 레퍼런스
public/flat/            레퍼런스에서 화면을 잘라 390×844로 맞춘 비교본 (scripts/extract.py)
scripts/                extract.py, screenshot.mjs, compare.py
```

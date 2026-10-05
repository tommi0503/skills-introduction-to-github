# Web Clone

13개 실제 웹사이트를 React + Tailwind CSS v4 + lucide-react로 재현한 프로젝트입니다.

| id | 사이트 | id | 사이트 |
|---|---|---|---|
| 01 | cartesia.ai | 08 | calendly.com |
| 02 | aside.com | 09 | cosmos.so |
| 03 | harvey.ai | 10 | giga.ai |
| 04 | cloudflare.com | 11 | useorigin.com |
| 05 | monologue.to | 13 | retool.com |
| 06 | x.ai | 14 | gitbook.com |
| 07 | mobbin.com (공개 랜딩) | 12 | ada.cx — 봇 차단으로 캡처 불가 |

## 실행
```bash
cd web-clone && npm install && npm run dev
```
- `#/` 갤러리, `#/compare/NN` 원본 캡처와 비교, `#/NN` 단독 렌더

## 규칙
- 모든 렌더는 `FRAME` = 1440×4500 (데스크톱 1440폭, 페이지 상단 4500px), `PageFrame`으로 고정
- 사진·영상·일러스트·로고·그래픽 배경·lucide 미지원 아이콘 → `ImagePlaceholder` (단색)
- 사이트별 `data.ts`(콘텐츠) · `theme.ts`(토큰) · `sections/` · `components/`

## 원본 캡처
`node scripts/capture.mjs [NN]` — 실제 브라우저로 1440폭 캡처
- `public/reference/NN.png` 전체 페이지, `public/flat/NN.png` 상단 4500px(비교 기준)
- `reference-dom/NN.json` 요소별 텍스트·폰트·크기·색·좌표

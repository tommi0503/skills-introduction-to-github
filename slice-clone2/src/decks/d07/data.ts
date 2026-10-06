import { t } from './theme'

/** Decoration: drawn circles/rings, organic bits as placeholders. */
export type Deco =
  | { k: 'circle'; cx: number; cy: number; r: number; c: string }
  | { k: 'ring'; cx: number; cy: number; r: number; b: number; c: string }
  | { k: 'blob'; x: number; y: number; w: number; h: number; r?: string }

export const cover = {
  kicker: 'CUTE & SIMPLE',
  title: ['귀엽고 활용도 높은', '프레젠테이션'],
  site: 'MIRICANVAS.COM',
  deco: [
    { k: 'circle', cx: 22, cy: 44, r: 125, c: t.orange },
    { k: 'circle', cx: 218, cy: 38, r: 136, c: t.orange },
    { k: 'circle', cx: 1045, cy: 700, r: 131, c: t.yellow },
    { k: 'circle', cx: 1255, cy: 660, r: 112, c: t.yellow },
    { k: 'blob', x: 1087, y: 506, w: 82, h: 82, r: '50%' },
    { k: 'blob', x: 171, y: 553, w: 92, h: 108, r: '50% 0 50% 50%' },
    { k: 'blob', x: 985, y: 79, w: 87, h: 87, r: '0 0 80px 0' },
  ] as Deco[],
}

export const toc = {
  page: '02',
  title: '목차',
  items: ['강조해서 보여주는 문장', '강조 키워드', '상하로 나뉜 텍스트', '3번 보여주는 사진과 텍스트', '흐름을 보여주는 인포그래픽', '깔끔하게 정리된 표'].map((text, i) => ({ n: `0${i + 1}`, text })),
  deco: [
    { k: 'blob', x: 125, y: 115, w: 98, h: 96, r: '0 0 0 90px' },
    { k: 'ring', cx: 1107, cy: 12, r: 60, b: 26, c: t.yellow },
  ] as Deco[],
}

export const highlight = {
  page: '03',
  kicker: 'HIGHLIGHT',
  title: ['강조해서', '보여주는', '문장'],
  body: ['해당 페이지는 사진과 짧은 텍스트를', '적기 좋은 페이지입니다.', '여기에는 보여주고 싶은 핵심 문장을', '간결하게 적어주세요.'],
  deco: [
    { k: 'blob', x: 1003, y: 129, w: 120, h: 118, r: '0 0 110px 0' },
    { k: 'blob', x: 301, y: 473, w: 172, h: 173, r: '50%' },
    { k: 'ring', cx: 1136, cy: 631, r: 35, b: 12, c: '#f9a8c9' },
  ] as Deco[],
}

export const keywords = {
  page: '04',
  kicker: 'KEYWORD',
  title: '강조 키워드',
  items: [220, 499, 779, 1060].map((cx, i) => ({ cx, name: `키워드 0${i + 1}`, desc: ['여기에 키워드에 대한', '설명을 입력해 보세요.'] })),
  shapes: ['50%', '42%', '30%', '50% 50% 50% 50% / 40% 40% 60% 60%'],
  deco: [
    { k: 'blob', x: 120, y: 71, w: 136, h: 67, r: '60px 60px 0 0' },
    { k: 'ring', cx: 1069, cy: 172, r: 27, b: 13, c: t.green },
  ] as Deco[],
}

export const twoCol = {
  page: '05',
  kicker: '2-COLUMN',
  title: ['상하로', '나뉜', '텍스트'],
  blocks: [
    { cy: 114, head: '소제목', lines: ['많은 내용을 깔끔하게 정리하기 좋은 페이지입니다.', '본문의 내용을 요약한, 간결한 제목을 입력해 보세요.', '제목은 페이지 내용을 모두 아우를 수 있는', '소제목이면 좋습니다.', '문장형보다 명사구로 끝내는 게 더욱 깔끔해요.'] },
    { cy: 421, head: '소제목', lines: ['해당 키워드에 관한 소개, 설명을 입력해 보세요.', '소개할 내용이 여러 개라면 단추형 목록이나', '번호를 활용해 정리해 보세요.', '구체적인 예시나 수치 등을 활용한다면', '신뢰도를 높일 수 있어요.'] },
  ],
  deco: [
    { k: 'blob', x: 149, y: 503, w: 83, h: 83, r: '50%' },
    { k: 'blob', x: 332, y: 604, w: 101, h: 52, r: '60px 60px 0 0' },
  ] as Deco[],
}

export const photos = {
  page: '06',
  kicker: 'IMAGE & TEXT',
  title: '사진과 텍스트',
  items: [
    { cx: 294, desc: ['해당 페이지는 사진을 넣고 설명', '텍스트를 기입할 수 있는 페이지입니다.', '자유롭게 사진을 넣어보세요.'] },
    { cx: 641, desc: ['넣고 싶은 사진을 프레임으로', '끌어오면 자동으로 프레임 사이즈에', '맞게 삽입됩니다.'] },
    { cx: 987, desc: ['좌측 요소 탭에서', '원하는 주제의 사진을 검색해', '자유롭게 사용해보세요.'] },
  ].map((it) => ({ ...it, head: '소제목' })),
  deco: [{ k: 'blob', x: 98, y: 82, w: 85, h: 43, r: '0 0 60px 60px' }] as Deco[],
}

export const process = {
  page: '07',
  kicker: 'PROCESS',
  title: ['흐름을 보여주는', '인포그래픽'],
  steps: [
    { cx: 220, cy: 217, dot: 421, head: '첫 번째', desc: ['해당 페이지는 로드맵,', '단계, 과정 등의 흐름을', '나타내는 페이지입니다.'] },
    { cx: 499, cy: 158, dot: 341, head: '두 번째', desc: ['또한 과정, 변천사를', '한눈에 설명하기 좋은', '페이지입니다.'] },
    { cx: 780, cy: 158, dot: 341, head: '세 번째', desc: ['다음 단계로 넘어갈 수', '있었던 이유에 대해', '입력해 보세요.'] },
    { cx: 1060, cy: 217, dot: 421, head: '마지막', desc: ['마지막 단계에선 도착', '지점에 대한 구체적인', '내용을 입력해 주세요.'] },
  ],
  deco: [
    { k: 'blob', x: 98, y: -20, w: 50, h: 121, r: '25px' },
    { k: 'blob', x: 1047, y: 54, w: 65, h: 36, r: '0 0 40px 40px' },
  ] as Deco[],
}

export const table = {
  page: '08',
  kicker: 'TABLE',
  title: ['깔끔하게', '정리된 표'],
  cols: ['A', 'B', 'C', 'D'],
  rows: [0, 1, 2].map(() => ['텍스트', '텍스트', '텍스트', '텍스트']),
  caption: ['표에 대한 부가적인 설명을 간략하게 적어주세요.', '표에 대한 부가적인 설명을 간략하게 적어주세요.'],
  deco: [
    { k: 'circle', cx: 870, cy: 0, r: 95, c: t.yellow },
    { k: 'circle', cx: 1035, cy: 0, r: 100, c: t.yellow },
    { k: 'circle', cx: 1200, cy: 0, r: 100, c: t.yellow },
    { k: 'circle', cx: 141, cy: 682, r: 112, c: t.orange },
    { k: 'circle', cx: 305, cy: 682, r: 104, c: t.orange },
    { k: 'circle', cx: -10, cy: 720, r: 100, c: t.orange },
    { k: 'ring', cx: 113, cy: 137, r: 20, b: 9, c: t.sage },
    { k: 'blob', x: 422, y: 47, w: 70, h: 69, r: '70px 0 0 0' },
    { k: 'blob', x: 492, y: 562, w: 59, h: 59, r: '50%' },
  ] as Deco[],
}

export const closing = {
  kicker: 'THANK YOU',
  title: ['시청해 주셔서', '감사합니다'],
  deco: [
    { k: 'circle', cx: 149, cy: 30, r: 185, c: t.orange },
    { k: 'circle', cx: -20, cy: 0, r: 160, c: t.orange },
    { k: 'circle', cx: 979, cy: 712, r: 125, c: t.yellow },
    { k: 'circle', cx: 1200, cy: 690, r: 115, c: t.yellow },
    { k: 'blob', x: 1042, y: 0, w: 122, h: 124, r: '0 0 120px 0' },
    { k: 'blob', x: 108, y: 486, w: 141, h: 141, r: '50% 0 50% 50%' },
  ] as Deco[],
}

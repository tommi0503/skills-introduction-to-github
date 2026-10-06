import { t } from './theme'

/** Decorative bits: simple dots / crosses are drawn, organic shapes are placeholders. */
export type Deco =
  | { k: 'dot'; x: number; y: number; d: number; c: string }
  | { k: 'x'; x: number; y: number; s: number; c: string }
  | { k: 'ring'; x: number; y: number; d: number; c: string; b: number }
  | { k: 'shape'; x: number; y: number; w: number; h: number; r?: string }

export const cover = {
  kicker: '미리 초등학교 수업 자료',
  title: ['학교 수업', '프레젠테이션'],
  author: '김미리 선생님',
  deco: [
    { k: 'ring', x: 600, y: -100, d: 190, c: t.sky, b: 26 },
    { k: 'dot', x: 304, y: 203, d: 28, c: t.peach },
    { k: 'dot', x: 986, y: 218, d: 28, c: t.mint },
    { k: 'x', x: 192, y: 356, s: 46, c: t.mint },
    { k: 'shape', x: 66, y: 408, w: 84, h: 82, r: '50%' },
    { k: 'shape', x: 92, y: 527, w: 175, h: 175, r: '50%' },
    { k: 'shape', x: 1092, y: 412, w: 132, h: 80, r: '0 0 80px 80px' },
    { k: 'shape', x: 760, y: 552, w: 135, h: 138, r: '10px' },
    { k: 'shape', x: 1003, y: 638, w: 162, h: 76, r: '0 0 40px 40px' },
    { k: 'ring', x: 474, y: 660, d: 150, c: '#ddeee4', b: 22 },
  ] as Deco[],
}

export const toc = {
  title: '오늘의 수업은?',
  items: ['01', '02', '03', '04', '05', '06'].map((n) => ({ n, text: '목차를 입력해 주세요.' })),
  deco: [
    { k: 'ring', x: -80, y: 254, d: 150, c: t.sky, b: 26 },
    { k: 'x', x: 70, y: 400, s: 44, c: t.lemon },
    { k: 'dot', x: 1168, y: 499, d: 28, c: t.peach },
    { k: 'shape', x: 1169, y: 557, w: 111, h: 163, r: '14px 14px 0 0' },
  ] as Deco[],
}

export const praise = {
  title: '친구를 칭찬합니다.',
  cards: ['김미리', '유미리', '강미리'].map((name) => ({ quote: `"${name}를 칭찬합니다"`, desc: ['칭찬하는 친구에 관한 간단한 설명과', '상황을 입력해 보세요.'] })),
  note: '페이지 내 인물 사진은 샘플이미지 입니다.',
  deco: [
    { k: 'ring', x: -50, y: 160, d: 110, c: t.sky, b: 20 },
    { k: 'ring', x: 1232, y: 588, d: 110, c: t.sky, b: 20 },
  ] as Deco[],
}

const desc2 = ['해당 키워드에 관한 소개, 설명을 간단하게 입력해 보세요. 다른 키', '워드에선 볼 수 없는 특징을 입력하면 구분이 더욱 명확해집니다.']
export const compare = {
  title: '2가지 상황 비교하기',
  cards: [0, 1].map(() => ({ topic: '이곳에 주제를 입력하세요', desc: desc2 })),
  deco: [
    { k: 'shape', x: 56, y: 246, w: 76, h: 78, r: '50%' },
    { k: 'shape', x: 12, y: 377, w: 62, h: 72, r: '0 60px 60px 0' },
    { k: 'dot', x: 76, y: 533, d: 20, c: t.blue },
    { k: 'shape', x: 1152, y: 248, w: 72, h: 110, r: '8px' },
    { k: 'shape', x: 1180, y: 397, w: 68, h: 68, r: '8px' },
    { k: 'dot', x: 1176, y: 545, d: 22, c: t.mint },
  ] as Deco[],
}

export const four = {
  title: '4가지 상황 알아보기',
  items: ['첫번째', '두번째', '세번째', '네번째'].map((w, i) => ({ n: `0${i + 1}.`, label: `${w} 상황`, desc: ['해당 키워드에 관한 소개, 설명을', '간단하게 입력해 보세요.'] })),
  deco: [
    { k: 'shape', x: 68, y: 237, w: 90, h: 90, r: '50%' },
    { k: 'shape', x: 1100, y: 268, w: 98, h: 110, r: '8px' },
    { k: 'shape', x: 74, y: 512, w: 92, h: 100, r: '8px' },
    { k: 'shape', x: 1110, y: 517, w: 95, h: 100, r: '0 100px 100px 0' },
  ] as Deco[],
}

export const points = {
  title: '주요 포인트 알아보기',
  rows: [
    '해당 키워드에 관한 소개, 설명을 입력해 보세요.',
    '소개할 내용이 여러개라면 단추형 목록이나 번호를 활용해 정리해 보세요.',
    '구체적인 예시나 수치 등을 활용한다면 신뢰도를 높일 수 있어요.',
    '다른 키워드에선 볼 수 없는 특징을 입력하면 구분이 더욱 명확해집니다.',
    '혹은 다른 키워드와 비교했을 때 해당 키워드만의 장점을 입력해도 좋아요.',
  ].map((text) => ({ key: '키워드 입력', text })),
  deco: [
    { k: 'shape', x: 0, y: 232, w: 42, h: 80, r: '0 50% 50% 0' },
    { k: 'shape', x: 1228, y: 444, w: 52, h: 90, r: '50% 0 0 50%' },
    { k: 'shape', x: 1114, y: 556, w: 130, h: 132, r: '50%' },
  ] as Deco[],
}

export const core = {
  title: '핵심 내용 알아보기',
  cols: (['microscope', 'checklist', 'book', 'monitor'] as const).map((icon) => ({ key: '키워드 입력', icon, desc: ['해당 키워드에 관한 설명을 간', '단하게 입력해 보세요.'] })),
  result: '이곳에 최종 결과에 대한 내용을 입력해 주세요',
  deco: [
    { k: 'ring', x: -86, y: 266, d: 150, c: t.sky, b: 22 },
    { k: 'x', x: 22, y: 422, s: 44, c: t.sky },
    { k: 'ring', x: 1228, y: 266, d: 150, c: t.sky, b: 22 },
    { k: 'x', x: 1212, y: 422, s: 44, c: t.sky },
  ] as Deco[],
}

export const summary = {
  title: '수업 내용 요약하기',
  rows: [
    { text: '이곳에 오늘 수업 내용을 요약해 보세요.', c: '#8fd0f0' },
    { text: '소개할 내용이 여러개라면 단추형 목록이나 번호를 활용해 정리해 보세요.', c: '#f6d968' },
    { text: '구체적인 예시나 수치 등을 활용한다면 신뢰도를 높일 수 있어요.', c: '#ff9f80' },
    { text: '다른 키워드에선 볼 수 없는 특징을 입력하면 구분이 더욱 명확해집니다.', c: '#94d6ae' },
  ],
  deco: [
    { k: 'shape', x: 68, y: 226, w: 80, h: 84, r: '50%' },
    { k: 'dot', x: 1186, y: 264, d: 18, c: t.peach },
    { k: 'shape', x: 1144, y: 310, w: 76, h: 110, r: '8px' },
    { k: 'shape', x: 64, y: 405, w: 82, h: 102, r: '8px' },
    { k: 'dot', x: 70, y: 517, d: 16, c: '#f6d968' },
    { k: 'shape', x: 1144, y: 514, w: 74, h: 100, r: '60px 0 60px 0' },
  ] as Deco[],
}

export const closing = {
  title: ['다음 수업', '시간에 만나요!'],
  question: '다음 수업 시간에는?',
  pill: '다음 수업 시간에 배우게될 수업 내용을 알려주세요',
  deco: [
    { k: 'ring', x: 590, y: -120, d: 200, c: t.sky, b: 22 },
    { k: 'dot', x: 304, y: 216, d: 28, c: t.peach },
    { k: 'dot', x: 986, y: 216, d: 28, c: t.mint },
    { k: 'x', x: 198, y: 346, s: 46, c: t.mint },
    { k: 'shape', x: 66, y: 400, w: 84, h: 84, r: '50%' },
    { k: 'shape', x: 88, y: 528, w: 160, h: 160, r: '50%' },
    { k: 'shape', x: 1092, y: 413, w: 132, h: 78, r: '0 0 80px 80px' },
    { k: 'shape', x: 880, y: 594, w: 130, h: 116, r: '10px' },
    { k: 'shape', x: 1065, y: 637, w: 160, h: 83, r: '0 0 40px 40px' },
    { k: 'ring', x: 440, y: 650, d: 160, c: '#ddeee4', b: 22 },
  ] as Deco[],
}

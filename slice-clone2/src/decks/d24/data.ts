export const cover = { kicker: '몽글몽글한 느낌의', title: '프레젠테이션', sub: '소속과 이름을 입력해주세요' }
export const toc = {
  title: 'CONTENTS',
  groups: ['01', '02', '03', '04'].map((no) => ({ no, lines: ['01', '02', '03'].map((n) => `${n}. 목차 내용을 입력해주세요.`) })),
}
export const agenda = ['01', '02', '03'].map((n) => `${n}. 목차를 입력해주세요`)
const desc22 = '내용을 입력해주세요.\n폰트는 나눔스퀘어라운드 Regular,\n크기는 22입니다.'
export const photos = { items: [0, 1, 2].map(() => ({ title: '제목을 입력해주세요', text: desc22 })) }
export const cards = { items: [0, 1, 2].map(() => ({ title: '제목을 입력해주세요', text: '내용을 입력해주세요.\n폰트는 나눔스퀘어라운드\nRegular, 크기는 24입니다.' })) }
export const features = {
  title: '제목을\n입력해주세요', sub: '이 텍스트 박스에 현재 페이지와 관련된 내용을\n간략하게 입력해주세요.',
  items: [0, 1, 2].map(() => ({ title: '제목을 입력해주세요', text: '키워드 및 페이지에 대한 부연 설명을 입력해주세요.\n폰트는 나눔스퀘어라운드 Regular, 크기는 24입니다.' })),
}
export const flow = {
  keyword: '키워드를\n입력해주세요', center: '중요 키워드를\n입력해주세요',
  quote: '키워드 또는 페이지에 대한 부가 설명을 입력해주세요.\n폰트는 나눔스퀘어라운드 Regular, 크기는 24입니다.',
}
export const bars = {
  series: [[20, 30], [40, 50], [60, 70], [30, 35]] as [number, number][],
  legend: ['타이틀 01', '타이틀 02'],
  notes: ['01', '02'].map((no) => ({ no, title: '차트에 대한 키워드를 입력해주세요', text: '차트에 대한 부연 설명을 입력해주세요.\n폰트는 나눔스퀘어라운드 Regular, 크기는 22입니다.' })),
}
export const donuts = {
  items: [50, 75, 25].map((v) => ({ v, label: '키워드를\n입력해주세요' })),
  text: '그래프에 대한 내용을 입력해주세요.\n폰트는 나눔스퀘어라운드 Regular,\n크기는 22입니다.',
}
export const points = {
  items: ['01', '02'].map((n) => ({ title: `${n}. 핵심 내용을 입력해주세요`, text: '키워드 및 페이지에 대한 부연 설명을 입력해주세요.\n폰트는 나눔스퀘어라운드 Regular, 크기는 24입니다.\n두줄에서 세줄 정도 입력해주세요.' })),
}
export const table = {
  cols: ['표 제목 01', '표 제목 02', '표 제목 03', '표 제목 04'],
  rows: ['표 제목 01', '표 제목 02', '표 제목 03', '표 제목 04'],
  cell: '내용을 입력해주세요', strong: '강조 내용을 입력해주세요',
  highlights: [[1, 1], [3, 2]] as [number, number][],
}
export type MapPill = { x: number; y: number; w: number; kind: 'lav' | 'peach' | 'blue' | 'orange' }
export const mindmap = {
  center: '핵심 키워드를\n입력해주세요', keyword: '키워드를 입력해주세요', leaf: '내용을 입력해주세요',
  pills: [
    { x: 89, y: 156, w: 243, kind: 'lav' }, { x: 292, y: 216, w: 245, kind: 'lav' }, { x: 156, y: 302, w: 247, kind: 'blue' },
    { x: 122, y: 456, w: 243, kind: 'peach' }, { x: 221, y: 545, w: 246, kind: 'orange' }, { x: 95, y: 623, w: 243, kind: 'peach' },
    { x: 966, y: 173, w: 244, kind: 'peach' }, { x: 840, y: 262, w: 265, kind: 'orange' }, { x: 927, y: 355, w: 245, kind: 'peach' },
    { x: 818, y: 498, w: 245, kind: 'blue' }, { x: 968, y: 574, w: 245, kind: 'lav' }, { x: 832, y: 635, w: 245, kind: 'lav' },
  ] as MapPill[],
}
export const thanks = { title: 'THANK YOU', sub: '발표를 들어주셔서 감사합니다 :)' }

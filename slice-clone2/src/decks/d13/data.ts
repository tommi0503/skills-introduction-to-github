import type { Tone } from './theme'

export const total = '13'
export const cover = {
  brand: 'MIRICOMPANY', year: '2090', month: '04',
  title: ['다양한 레이아웃의', '심플한 프레젠테이션'],
  sub: 'SIMPLE LAYOUT PRESENTATION',
  org: '미리컴퍼니', name: '김미리 팀장', tel: '010-0000-0000', mail: 'miridih@company.com',
}
const cycle: Tone[] = ['pink', 'green', 'pink', 'green', 'pink', 'green']
export const toc = { title: '목차 안내', items: cycle.map((c, i) => ({ c, chapter: `CHAPTER 0${i + 1}`, title: '타이틀을 넣어주세요', bullets: ['이곳에 세부 내용을 넣어주세요.', '이곳에 세부 내용을 넣어주세요.'] })) }
export const chapter = { title: 'Chapter 01', lines: ['본문 사이사이에 들어가는 소제목 페이지입니다.', '해당 챕터에 대한 설명을 간략히 적어주세요.'] }
const sub = '이곳은 부제목 자리입니다.'
const kw3: Tone[] = ['pink', 'blue', 'green']
export const threeCol = {
  title: '3단 구성 페이지', sub,
  items: kw3.map((c, i) => ({ c, key: `KEYWORD 0${i + 1}`, bullets: [['해당 키워드에 대한 소개와 설명', '을 입력하세요.'], ['소개할 내용이 여러개라면 단추', '형 목록이나 번호를 활용해 정리', '하세요.']] })),
}
export const threeRow = {
  title: '3단 구성 페이지', sub,
  items: kw3.map((c, i) => ({ c, key: `KEYWORD 0${i + 1}`, bullets: ['해당 키워드에 대한 소개와 설명을 입력하세요.', '소개할 내용이 여러개라면 단추형 목록이나 번호를 활용해 정리하세요.'] })),
}
const desc2 = ['해당 사진과 관련된 내용을 간략히 정리해 보세요.', '해당 페이지에서 전달하고자 하는 내용을 정리하기에 좋습니다.']
export const mainImage = { title: '메인 이미지와 텍스트', sub, desc: desc2, key: 'KEYWORD 01', keyText: '해당 키워드에 대한 소개와 설명을 입력하세요.' }
const kdesc = ['해당 키워드에 대한', '소개와 설명을 입력하세요.']
export const twoImages = {
  title: '2개의 이미지와 텍스트', sub: ['이곳은', '부제목 자리입니다.'],
  desc: ['해당 사진과 관련된 내용을', '간략히 정리해 보세요.', '해당 페이지에서 전달하고자 하는', '내용을 정리하기에 좋습니다.'],
  items: (['pink', 'green'] as Tone[]).map((c, i) => ({ c, key: `KEYWORD 0${i + 1}`, desc: kdesc })),
}
export const threeImages = { title: '3개의 이미지와 텍스트', sub, desc: desc2, items: kw3.map((c, i) => ({ c, key: `KEYWORD 0${i + 1}`, desc: kdesc })) }
export const bars = {
  title: '막대그래프와 텍스트', sub,
  desc: ['해당 그래프 관련된 내용을 간략히 정리해 보세요.', '해당 페이지에서 전달하고자 하는 내용을 정리하기에', '좋습니다.'],
  data: [{ label: '항목 01', v: 20 }, { label: '항목 02', v: 40 }, { label: '항목 03', v: 60 }],
  ticks: [0, 20, 40, 60],
  bullets: ['이곳에 해당 그래프에 대한 내용을 적어주세요.', '이곳에 해당 그래프에 대한 내용을 적어주세요.', '이곳에 해당 그래프에 대한 내용을 적어주세요.'],
}
export const donut = {
  title: ['원그래프와', '텍스트'], sub,
  desc: ['해당 그래프 관련된 내용을 간략히 정리해 보세요.', '해당 페이지에서 전달하고자 하는 내용을', '정리하기에 좋습니다.'],
  segs: [{ label: '항목 01', v: 20, c: 'pink' as Tone }, { label: '항목 02', v: 40, c: 'blue' as Tone }, { label: '항목 03', v: 60, c: 'green' as Tone }],
  bullets: ['이곳에 해당 그래프에 대한 내용을 적어주세요.', '이곳에 해당 그래프에 대한 내용을 적어주세요.'],
}
const kw5: Tone[] = ['pink', 'blue', 'green', 'blue', 'pink']
export const iconsGrid = {
  title: '아이콘과 키워드', sub,
  desc: '키워드 리스트에 대한 설명을 적어주세요. 관련된 이야기를 간략하게 표현해 내용을 정리하기에 좋습니다.',
  items: (['handshake', 'doc', 'puzzle', 'map', 'globe'] as const).map((icon, i) => ({ icon, c: kw5[i], key: `KEYWORD 0${i + 1}`, desc: ['키워드에 대한', '소개와 설명을', '입력하세요.'] })),
}
export const iconsList = {
  title: ['아이콘과', '키워드'], sub,
  desc: ['여러개의 나열된 키워드 리스트에 대한 설명을', '적어주세요. 리스트에 관련된 이야기를 간략하', '게 표현해 내용을 정리하기에 좋습니다.'],
  items: (['search', 'board', 'pie', 'trend', 'target'] as const).map((icon, i) => ({ icon, c: kw5[i], key: `KEYWORD 0${i + 1}`, text: '해당 키워드에 대한 소개와 설명을 입력하세요.' })),
}
export const process = {
  title: '프로세스와 텍스트', sub, note: '이곳에는 아래 흐름도에 대한 핵심 내용을 간략하게 적어주세요.',
  items: (['cog', 'pencil', 'atom', 'globe'] as const).map((icon, i) => ({ icon, key: `KEYWORD 0${i + 1}`, desc: ['키워드에 대한 소개와', '설명을 입력하세요.'] })),
}

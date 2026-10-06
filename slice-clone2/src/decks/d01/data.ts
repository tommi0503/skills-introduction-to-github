export const cover = { title: '피피티 템플릿', titleTail: '입니당', sub: '여기에 이름을 적어주세용' }
export const toc = {
  title: ['목차', '라구용'] as const,
  items: ['첫번째', '두번째', '세번째', '네번째'].map((k) => ({ label: k, text: `${k} 목차를 적으면 돼용` })),
}
export const team = {
  title: ['팀원', '들을소개합니당'] as const,
  members: Array.from({ length: 4 }, () => ({ name: '조원이름', role: '역할과 간단한 소개' })),
}
export const topic = { kicker: '발표주제는요...', title: '난 왜 이렇게 귀여운가', sub: '나의 귀여움과 매력에 대한 고찰' }
export const keywords = {
  title: '핵심 키워드는',
  items: [1, 2, 3].map((n) => ({ word: `키워드${n}`, desc: ['키워드에 대한', '설명을 적어주세요!'] })),
  circled: 1,
}
export const charts = {
  title: '그래프도 필요해용',
  pie: { value: 65, labels: ['35%', '65%'], caption: '얘는 원그래프' },
  bars: { heights: [290, 235, 160, 73], emphasis: '강조!', note: '수치', caption: '얘는 막대그래프' },
}
export const photos = { title: '사진도 넣고 싶어용', caption: ['사진에 대한 설명', '이건 우수우수 사진입니다'], bubble: ['사진에 대한', '설명이지용'] }
export const longText = {
  title: '글도 많이 쓸래용',
  bubble: ['사진에 대한', '설명이지용'],
  heading: '긴 글을 쓰고 싶어요',
  body: '이 페이지엔 긴 설명을 적으시면 됩니다. 폰트는 홍차왕자 소년R입니다. 폰트 사이즈는 40입니다. 자간은 0, 행간은 20입니다. 장평은 100%입니다. 취향에 맞게 조정해서 사용해 보세요! 이 페이지엔 긴 설명을 적으시면 됩니다. 폰트는 홍차왕자 소년R입니다. 폰트 사이즈는 40입니다. 자간은 0, 행간은 20입니다. 장평은 100%입니다.',
}
export const closing = { kicker: '마지막으로', lines: ['발표를 들어주셔서', '감사합니다'] }

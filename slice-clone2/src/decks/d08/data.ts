export const brand = 'MIRI BRAND'
export const bubble = ['MIRI', 'BRAND']

export const cover = { script: '귀엽고 심플한', title: '프레젠테이션', sideL: 'CUTE & SIMPLE', sideR: 'PRESENTATION' }

export const contents = {
  page: '01',
  title: 'CONTENTS',
  items: [
    ['목차의 제목을 입력해 주세요.'],
    ['유기적인 구성으로 발표의', '흐름을 표현하기 좋습니다.'],
    ['핵심 내용이 포함되는,', '간결한 제목을 입력해 보세요.'],
    ['청자가 궁금해 할법한 순서대로', '내용을 구성해요.'],
    ['발표의 내용을 한번에파악할 수', '있도록 요약해 보세요.'],
    ['목차만 보고도 말하는 바를', '알 수 있도록 정리해 보세요.'],
  ],
}

export const quote = {
  page: '02',
  title: [['강조해서', '보여주는'], ['문장']] as const,
  body: { plain: '해당 페이지는 사진과 짧은 텍스트를 적기 좋은 페이지입니다.', strong: '여기에는 보여주고 싶은 핵심 문장을 간', tail: '결하게 적어주세요.' },
}

export const keywords = {
  page: '03',
  title: '강조 키워드',
  items: [1, 2, 3, 4].map((n) => ({ name: `키워드${n}`, desc: ['여기에 키워드에', '대한 설명을', '입력해 보세요.'] })),
}

const para = ['많은 내용을 깔끔하게 정리하기 좋은', '페이지입니다. 본문의 내용을 요약한, 간결한', '제목을 입력해 보세요. 페이지 내용을 모두', '아우를 수 있는 소제목이면 좋습니다.']
export const twoRow = { page: '04', title: ['상하로', '나뉜', '텍스트'], blocks: [{ head: '소제목', body: para }, { head: '소제목', body: para }] }

export const photos = {
  page: '05',
  title: '3번 보여주는 사진과 텍스트',
  items: [0, 1, 2].map(() => ({ head: '소제목', desc: ['해당 페이지는 사진을 넣고 설명을', '기입할 수 있는 페이지입니다.', '자유롭게 사진을 넣어보세요.'] })),
}

export const steps = {
  page: '06',
  title: '흐름을 보여주는 인포그래픽',
  items: [
    { head: '첫 번째', desc: ['해당 페이지는 로드맵,', '단계, 과정 등의 흐름을', '나타내는 페이지입니다.'] },
    { head: '두 번째', desc: ['또한 과정, 변천사를', '한눈에 설명하기 좋은', '페이지입니다.'] },
    { head: '세 번째', desc: ['다음 단계로 넘어갈 수', '있었던 이유에 대해', '입력해 보세요.'] },
    { head: '마지막', desc: ['마지막 단계에선', '도착지점에 대한 구체적인', '내용을 입력해 주세요.'] },
  ],
}

export const table = {
  page: '07',
  title: '깔끔하게 정리된 표',
  sub: '깔끔하게 표로 내용을 정리하기 좋은 페이지 입니다.',
  cols: ['A', 'B', 'C', 'D'],
  rows: [['텍스트', '텍스트', '텍스트', '텍스트'], ['', '', '', ''], ['', '', '', '']],
}

export const closing = { page: 'FIN', kicker: '시청해 주서서 감사합니다.', title: 'Thank you' }

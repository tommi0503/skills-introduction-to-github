export const frame = { left: 'Business', right: 'Presentation', tab: '|  MIRI STUDY  |' }

export const cover = {
  title: ['심플하고 깔끔한', '프레젠테이션'],
  keyword: 'Keyword',
  keywordText: '교육 아이콘과 이미지가 있는 템플릿',
}

export const contents = {
  page: '0',
  title: 'CONTENTS',
  items: [
    { label: ['긴글이 있는', '텍스트 레이아웃'], icon: 'landmark' },
    { label: ['2단 이미지', '레이아웃'], icon: 'library' },
    { label: ['3가지 비교', '레이아웃'], icon: 'bookmark' },
    { label: ['4개 키워드', '레이아웃'], icon: 'inbox' },
    { label: ['프로세스가', '있는 레이아웃'], icon: 'search' },
  ] as const,
}

export const chapter = {
  page: '0',
  pill: 'Chapter 1',
  title: ['타이틀을', '입력해주세요.'],
  rows: ['첫번째', '두번째', '세번째'].map((lead, i) => ({ letter: 'ABC'[i], lead: `${lead},`, text: ' 세부 타이틀을 입력해주세요.' })),
}

export const longText = {
  page: '1',
  title: ['긴글이 있는', '텍스트 레이아웃'],
  body: [
    '해당 페이지는 많은 분량 텍스트를 입력할 때 쓰기 좋은 페이지입니다. 중요한 내용이나 길게',
    '의견을 보여주어야 할 경우 해당 페이지를 활용해보세요. 가독성의 핵심은 얼마나 내용을 간',
    '결하게 전달하는가 입니다. 쉽게 읽을 수 있고, 눈에 잘띄는 것이 중요해요.',
  ],
  circles: (['bookmark', 'edit', 'tablet'] as const).map((icon, i) => ({ letter: 'ABC'[i], icon, title: '핵심 키워드', desc: ['주제에 대한 세부내용을', '간략하게 입력해주세요.'], filled: i !== 1 })),
}

export const twoImages = {
  page: '2',
  title: '2단 이미지 레이아웃',
  items: ['A', 'B'].map((letter) => ({
    letter,
    title: ['핵심 키워드를', '입력해주세요.'],
    body: ['주제에 대한 세부내용을 간략하게', '입력해주세요. 페이지 이미지에서', '말하고자하는 내용을 알려주세요.', '주제에 대한 세부내용을 간략하게', '입력해주세요.'],
  })),
}

export const compare = {
  page: '3',
  title: '3가지 비교 레이아웃',
  rows: (['contact', 'music', 'laptop'] as const).map((icon) => ({ icon, key: '핵심키워드', before: '세부 내용을 입력해주세요.', after: '세부 내용을 입력해주세요.' })),
  labels: ['Before', 'After'],
}

export const keywords = {
  page: '4',
  title: '4개 키워드 레이아웃',
  items: ['A', 'B', 'C', 'D'].map((letter) => ({ letter, title: '키워드를 입력해주세요.', bullets: ['- 세부키워드를 입력해주세요.', '- 세부키워드를 입력해주세요.'] })),
}

export const process = {
  page: '4',
  title: ['프로세스가', '있는 레이아웃'],
  steps: [
    { letter: 'A', cy: 226, title: '키워드를 입력해주세요.', desc: ['주제에 대한 세부내용을 간략하게 입력해주세요.'] },
    { letter: 'B', cy: 336, title: '키워드를 입력해주세요.', desc: ['주제에 대한 세부내용을 간략하게 입력해주세요.'] },
    { letter: 'C', cy: 446, title: '키워드를 입력해주세요.', desc: ['주제에 대한 세부내용을 간략하게 입력해주세요.'] },
    { letter: 'D', cy: 584, title: '키워드를 입력해주세요.', desc: ['주제에 대한 세부내용을 간략하게 입력해주세요. 강조하고 싶은', '부분은 볼드체 또는 큰 사이즈로 표현해보세요. 구체적인 예시나', '아이콘을 활용해 설명하셔도 좋습니다.'] },
  ],
}

export const closing = {
  title: '감사합니다',
  sub: '마지막 페이지의 인사 또는 핵심주제에 대한 요약 내용을 입력해주세요.',
  org: '미리스터디',
  contact: ['Tel. 070.1234.5678', 'E-Mail. miri@miristudy.com'],
}

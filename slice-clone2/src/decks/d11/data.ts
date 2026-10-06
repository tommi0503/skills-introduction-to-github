export const cover = {
  title: ['Business', 'Presentation'],
  sub: '다양하게 쓰이는 기본 보고서 양식',
  contacts: [['Manager.', 'Kim Miri'], ['E.', 'miri@miricompany.com'], ['T.', '000-1234-5678'], ['W.', 'www.yoursite.com']] as const,
}

export const contents = {
  title: 'CONTENTS',
  intro: ['프레젠테이션 주제에 대한 구체적인 설명을 작성해주세요.', '주요 키워드와 궁극적 목적 문장을 기재해주세요.'],
  items: ['긴 글이 있는 레이아웃', '두가지 이미지 레이아웃', '네가지 키워드 레이아웃', '세가지 키워드 레이아웃', '프로세스 레이아웃', '요약이 있는 레이아웃'],
}

export const longText = {
  kicker: 'About Us',
  title: '긴 글이 있는 레이아웃',
  body: [
    '해당 페이지는 많은 분량 텍스트를 입력할 때 쓰기 좋은 페이지입니다. 중요한 내용이',
    '나 길게 의견을 보여주어야 할 경우 해당 페이지를 활용해보세요. 가독성의 핵심은 얼',
    '마나 내용을 간결하게 전달하는가 입니다. 쉽게 읽을 수 있고, 눈에 잘띄는 것이 중요',
    '해요. 프레젠테이션의 전체적인 톤앤매너와 맞는 폰트와 색상 등을 활용해주세요. 해',
    '당 페이지는 많은 분량 텍스트를 입력할 때 쓰기 좋은 페이지입니다.',
  ],
  keys: [{ k: 'Keyword 1', text: '세부키워드를 입력해주세요.' }, { k: 'Keyword 2', text: '세부키워드를 입력해주세요.' }],
}

export const twoImages = {
  kicker: 'Overview',
  title: '두가지 이미지 레이아웃',
  cards: [1, 2].map((n) => ({
    k: `Keyword ${n}`,
    head: '핵심 키워드를 입력해주세요.',
    body: ['키워드와 이미지에 대한 내용을 입력해주세요. 키워드에 대한', '내용을 입력해주세요. 키워드와 이미지에 대한 내용을 입력해주세요.'],
  })),
}

export const fourKeys = {
  kicker: 'Overview',
  title: '네가지 키워드 레이아웃',
  items: [1, 2, 3, 4].map((n) => ({ k: `Keyword ${n}`, head: '키워드를 입력해주세요.', body: ['키워드에 대한 세부 내용을 입력해주세요.', '핵심 키워드를 아이콘으로 표현해보세요.'] })),
}

export const threeKeys = {
  kicker: 'Project',
  title: '세가지 키워드 레이아웃',
  items: [1, 2, 3].map((n) => ({ k: `Keyword ${n}`, head: '핵심 키워드를 입력해주세요.', body: ['핵심 키워드에 대한 세부내용을 입력해주세요.', '주제와 핵심 키워드에 대한 설명글을 간략하게', '기재해주세요. 텍스트를 입력해주세요.'] })),
}

export const process = {
  kicker: 'Process',
  title: '프로세스 레이아웃',
  body: ['프레젠테이션 주제에 대한 구체적인 설명을 작성해주세요.', '주요 키워드와 궁극적 목적 문장을 기재해주세요.'],
  steps: ['첫번째', '두번째', '세번째', '네번째', '다섯번째'].map((n, i) => ({ step: `Step ${i + 1}`, head: `${n} 키워드`, sub: '· 세부 내용을 입력해주세요.' })),
}

export const summary = {
  kicker: 'Strategy',
  title: '요약이 있는 페이지',
  rows: [
    '프레젠테이션 전체 내용을 요약하고 결론을 제시해 보세요.',
    '핵심 내용을 정리하여 중요한 포인트를 다시 확인할 수 있도록 해요.',
    '중요한 개념이나 메시지는 반복해서 전달하세요.',
    '프레젠테이션을 통해 독자가 얻은 새로운 정보를 강조해 마무리하세요.',
    '주제에 대한 설명을 간략하게 입력해주세요.',
  ].map((text, i) => ({ k: `Keyword ${i + 1}`, text })),
}

export const thanks = {
  sub: '다양하게 쓰이는 기본 보고서 양식',
  title: 'Thank You!',
  body: ['프레젠테이션 주제에 대한 구체적인 설명을 작성해주세요.', '주요 키워드와 궁극적 목적 문장을 기재해주세요.'],
  contact: 'Contact Us.',
  cols: [['Manager.', 'Kim Miri'], ['Tel.', '000-1234-5678'], ['E-Mail.', 'miri@miricompany.com']] as const,
}

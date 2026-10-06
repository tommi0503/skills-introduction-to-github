export const band = 'SIMPLE BUSINESS PRESENTATION'

export const cover = {
  title: ['심플하고 깔끔한', '비즈니스 프레젠테이션'],
  info: ['미리컴퍼니 기획팀', '김미리 대리', '010-1234-5678', 'kim@miricompany.com'],
  site: 'MIRICOMPANY.COM',
}

export const contents = { title: 'CONTENTS', items: [1, 2, 3, 4, 5, 6].map((n) => ({ n: `0${n}`, title: '해당 제목을 입력해 주세요', sub: '목차에 대한 설명을 간략하게 입력하세요' })) }

const kdesc = ['이곳에 해당 내용을 텍스트로 간략하게', '입력해 주세요. 관련 내용을 넣어 주세요.', '간결하고 명확하게 입력해 주세요.']
export const keywords = { n: '01', title: '프로젝트 포인트 키워드', items: (['idea', 'docs', 'present'] as const).map((icon, i) => ({ icon, name: `KEYWORD ${i + 1}`, desc: kdesc })) }

export const photoText = {
  n: '02', title: '사진과 텍스트 레이아웃',
  kicker: 'KEY POINTS', lead: '강조하고 싶은 내용을 입력해 주세요',
  body: [
    '해당 페이지는 많은 분략 텍스트를 입력할 때 쓰기 좋은 페이지입니다. 5줄 이상의 텍스',
    '트를 넣어야 할 때 이 페이지를 활용해 보세요.',
    '중요한 내용이나 길게 의견을 보여주어야 할 경우 해당 페이지를 활용해 보세요. 가독성',
    '의 핵심은 얼마나 내용을 간결하게 전달하는가 입니다. 쉽게 읽을 수 있고, 눈에 잘띄는',
    '것이 중요해요. 프레젠테이션의 전체적인 톤앤매너와 맞는 폰트와 색상 등을 활용해 주',
    '세요. 구체적인 예시나 수치 등을 활용하면 좋습니다.',
    '해당 페이지는 많은 분량 텍스트를 입력할 때 쓰기 좋은 페이지입니다. 관련 내용을 입력',
    '해 주세요. 해당페이지는 많은 분량의 텍스트를 입력할 때 쓰기 좋은 페이지입니다.',
    '5줄 이상의 텍스트를 넣어야 할 때 이 페이지를 활용해 보세요. 중요한 내용이나 길게 의',
    '견을 보여주어야 할 경우 해당 페이지를 활용해 보세요.',
  ],
}

export const fourText = {
  n: '03', title: '4단 텍스트 레이아웃',
  items: ['첫', '두', '세', '네'].map((w, i) => ({ kicker: `POINT. 0${i + 1}`, title: `${w} 번째 키워드 입력`, desc: '이곳에 해당 내용을 간략하게 입력해 주세요. 관련 내용을 입력해 주세요.' })),
}

export const chapter = {
  kicker: 'CHAPTER.', n: '02', title: '컨텐츠 제목을 입력해 주세요',
  items: ['1. 강조하고 싶은 포인트 내용을 입력해 주세요', '2. 이곳에 핵심 내용을 간결하고 명확하게 입력해 주세요.', '3. 이곳에 해당 내용을 텍스트로 간략하게 입력해 주세요. 관련 내용을 넣어 주세요.'],
}

const b1 = [['이곳에 상세설명을 작성해 주', '세요.'], ['해당 연혁에 대해 넣어 주세요.'], ['관련 내용을 입력하세요.']]
const b2 = [['연혁에 대해 설명해 주세요.'], ['관련 내용을 입력하세요.'], ['해당하는 내용을 간결하고 명', '확하게 설명해 주세요.']]
export const flow = {
  n: '04', title: '흐름을 보여주는 인포그래픽',
  steps: [b1, b2, b2, b1].map((bullets, i) => ({ kicker: `STEP.0${i + 1}`, title: `${['첫', '두', '세', '네'][i]} 번째 키워드 입력`, bullets })),
  note: '이곳에 관련 내용을 텍스트로 간략하게 입력해 주세요. 강조하고 싶은 내용을 입력하세요.',
}

export const photos = { n: '05', title: '4개의 사진과 텍스트', items: [1, 2, 3, 4].map((n) => ({ n: `0${n}`, name: `KEYWORD ${n}`, desc: ['이곳에 해당 내용을 간략하게 입력', '해 주세요. 내용을 입력해 주세요.'] })) }

export const list = {
  n: '06', title: '5단 목록형 레이아웃',
  rows: [1, 2, 3, 4, 5].map((n) => ({ n: `0${n}`, text: '이곳에 관련 내용을 간략하게 입력해 주세요.' })),
  aside: ['이곳에 부제목격의 텍스트를 입력', '해 주세요. 해당 페이지를 요약하는', '내용도 좋아요.'],
}

const ba = [1, 2, 3, 4].map((n) => `${n}. 이곳에 관련 내용을 간략하게 입력해 주세요.`)
export const compare = { n: '07', title: '문제점과 해결 방안', cols: [{ head: 'BEFORE', items: ba }, { head: 'AFTER', items: ba }] }

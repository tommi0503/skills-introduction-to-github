export const cover = { bubble: '신나는~', title: ['퀴즈', '게임'], memo: 'MEMO.', memoText: 'MT에서 하기 좋은 퀴즈게임 모음.zip' }
export const rules = { title: '게 임 방 법', rows: [['01.', '우리팀만의 구호를 정한다'], ['02.', '정답을 알면 구호를 외친다'], ['03.', '틀리면 -10점 맞히면 +20점']] }
export const ready = { kicker: '그럼 지금부터 시작합니다.', title: '눈 크게 뜨고 보세요!' }
export const countdown = [
  { n: '3', art: { x: 174, y: 232, w: 386, h: 361 } },
  { n: '2', art: { x: 158, y: 224, w: 430, h: 370 } },
  { n: '1', art: { x: 163, y: 241, w: 435, h: 332 } },
]
const q1 = 'Q. 다음 사진 속 사물의 이름은?'
const q2 = 'Q. 사회자는 오늘 아침밥을 먹고 왔다?'
const q3 = 'Q. 오늘 사회자가 가장 많이 말한 단어는?'
const q4 = 'Q. 다음 목소리의 주인공을 맞춰보세요.'
export const quizzes = {
  photo: { q: q1, tag: '사물이름 퀴즈', answer: '트래픽콘' },
  ox: { q: q2, tag: 'OX 퀴즈' },
  word: { q: q3, tag: '단답 퀴즈', hints: [['힌트1:', '여러 번 강조함'], ['힌트2:', '게임 직전에도 말함']], answer: '행 복' },
  sound: { q: q4, tag: '사운드 퀴즈', answer: '김 미 리' },
}
export const answerLabel = '정답:'
export const ending = { pill: '오늘의 게임은 끝~', title: ['우리 팀이 1등인 것', '같다면 함성!'] }
export const prize = { kicker: '오늘의 1등 팀 상품', title: ['치킨 반반세트', '기프티콘!'] }

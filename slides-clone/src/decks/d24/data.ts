export interface Question { q: string; lines: string[]; x: number; y: number; accent: 'blue' | 'yellow'; img: { x: number; y: number; w: number; h: number; round?: boolean } }
export const heading = { num: '05', plain: '상담교사의', accent: '고민과 질문들' }
export const questions: Question[] = [
  { q: 'Q1', lines: ['상담도 행정업무도', '모두 잘 해내고 싶어요.'], x: 136, y: 253, accent: 'blue', img: { x: 53, y: 59, w: 131, h: 96 } },
  { q: 'Q2', lines: ['깊이 있는 상담을', '할 시간이 없었어요.'], x: 394, y: 277, accent: 'yellow', img: { x: 46, y: 35, w: 139, h: 107 } },
  { q: 'Q3', lines: ['변화가 보이지 않을 때', '해결 방법?'], x: 650, y: 253, accent: 'blue', img: { x: 59, y: 43, w: 115, h: 115, round: true } },
  { q: 'Q4', lines: ['감정적으로 소진된', '느낌이 들 때는?'], x: 907, y: 277, accent: 'yellow', img: { x: 40, y: 48, w: 157, h: 99 } },
]
export const footer = '고민 끝에 내린 결론이나 답안이 있다면 이야기를 들려주세요.'

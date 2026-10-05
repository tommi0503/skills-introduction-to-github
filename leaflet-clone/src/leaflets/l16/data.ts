import { Clock, DoorClosed, type LucideIcon } from 'lucide-react'

export const about = {
  eyebrow: 'ABOUT',
  title: '공연을 소개합니다',
  lead: '깊어가는 가을밤,',
  sub: '현악의 울림으로 계절의 정취를 전합니다.',
  paragraphs: [
    [
      "이번 정기연주회는 '세레나데'를 주제로 엘가와 드보르자크의",
      '현을 위한 세레나데를 한 무대에 올립니다. 비발디의 ‘가을’과',
      '피아졸라의 리베르탄고까지, 고전과 현대를 넘나드는 프로그램',
      '으로 가을의 낭만을 담았습니다.',
    ],
    [
      '연주회의 문턱을 낮추고 싶은 마음으로, 곡마다 지휘자의 짧은',
      '해설을 곁들입니다. 클래식이 처음인 분도 편안하게 즐기실 수',
      '있습니다.',
    ],
  ],
}

export interface Piece {
  composer: string
  title: string
  note?: string
}

export interface ProgramPart {
  title: string
  /** Top of the part block (panel y). */
  y: number
  pieces: Piece[]
}

export const program = {
  eyebrow: 'PROGRAM',
  title: '프로그램',
  parts: [
    {
      title: '1부',
      y: 188,
      pieces: [
        { composer: 'W. A. 모차르트', title: "오페라 '피가로의 결혼' 서곡 K.492" },
        { composer: 'E. 엘가', title: '현을 위한 세레나데 E단조 Op.20' },
        { composer: 'A. 비발디', title: "'사계' 중 가을 F장조 RV 293", note: '* 바이올린 서도윤' },
      ],
    },
    {
      title: '2부',
      y: 641,
      pieces: [
        { composer: 'J. 브람스', title: '헝가리 무곡 제5번 G단조' },
        { composer: 'A. 드보르자크', title: '현악 세레나데 E장조 Op.22 중', note: '* 첼로 민하늘' },
        { composer: 'A. 피아졸라', title: '리베르탄고 (현악 오케스트라 편곡)' },
      ],
    },
  ] satisfies ProgramPart[],
  intermission: { label: 'INTERMISSION', length: '15분', y: 537 },
}

export interface GuideItem {
  title: string
  lines: string[]
  /** lucide icon, or null when the pictogram is artwork (placeholder). */
  icon: LucideIcon | null
  iconShape?: 'figure' | 'pin'
}

export const guide = {
  eyebrow: 'GUIDE',
  title: '관람 안내',
  items: [
    { title: '관람 연령', lines: ['8세 이상(초등학생 이상) 입장 가능'], icon: null, iconShape: 'figure' },
    { title: '공연 시간', lines: ['약 90분(인터미션 15분 포함)'], icon: Clock },
    { title: '입장 안내', lines: ['공연 시작 30분 전부터 입장', '시작 후에는 곡 사이에만 입장 가능합니다'], icon: DoorClosed },
    { title: '주차 안내', lines: ['아트센터 지하주차장 3시간 무료', '(로비 무인정산기에서 등록)'], icon: null, iconShape: 'pin' },
  ] satisfies GuideItem[],
  next: {
    title: '다음 공연',
    headline: '제13회 정기연주회 <겨울, 첫눈의 왈츠>',
    detail: '2080. 12. 19(토) 오후 7시 30분 | 아트센터',
    note: '* 사전 예약 시 20% 얼리버드 할인',
  },
  contactTitle: '문의',
  contacts: [
    { label: '공연 문의', value: '02-1234-5678', extra: '평일 10:00-17:00' },
    { label: '단체 관람', value: 'dream@canvakorea.co.kr' },
  ],
}

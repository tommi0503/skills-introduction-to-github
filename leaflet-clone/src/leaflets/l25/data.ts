import { CalendarDays, Laptop, Phone, Smartphone, type LucideIcon } from 'lucide-react'
import type { FooterText } from '../shared-2425/components/ContactFooter'

export interface ProgramItem {
  label: string
  desc: string[]
}

export interface ProgramGroup {
  title: string
  items: ProgramItem[]
}

export const programGroups: ProgramGroup[] = [
  {
    title: '어린이 배움 특강',
    items: [
      { label: '그림책 탐험', desc: ['이야기를 읽고 질문하며 생각을 자유롭', '게 나눠요.'] },
      { label: '창의 체험', desc: ['관찰·놀이·만들기 활동으로 새로운 아', '이디어를 표현해요.'] },
    ],
  },
  {
    title: '방학 독서 프로젝트',
    items: [
      { label: '함께 읽기', desc: ['주요 장면을 살펴보고 인상 깊은 내용', '을 이야기해요.'] },
      { label: '생각 나누기', desc: ['질문 카드, 북토크, 짧은 글쓰기로 감상', '을 표현해요.'] },
    ],
  },
  {
    title: '함께하는 평생학습',
    items: [
      { label: '생활 속 배움', desc: ['일상에 바로 활용할 수 있는 유익한 지', '식과 정보를 익혀요.'] },
      { label: '함께 성장', desc: ['참여자들과 의견과 경험을 나누며 새로', '운 관점을 발견해요.'] },
    ],
  },
]

/** What sits at the right of an application step. */
export type StepAside = { kind: 'pill'; text: string } | { kind: 'art'; label: string } | { kind: 'qr'; text: string }

export interface ApplyStep {
  icon: LucideIcon
  title: string
  lines: string[]
  aside: StepAside
}

export const howToApply = {
  title: '신청방법안내',
  steps: [
    { icon: CalendarDays, title: '신청 기간', lines: ['6. 30.(월) 09:00 ~'], aside: { kind: 'pill', text: '선착순 마감' } },
    { icon: Laptop, title: '신청 방법', lines: ['도서관 홈페이지 온라인 신청', '프로그램 〉 수강신청 메뉴'], aside: { kind: 'art', label: 'apple on books' } },
    { icon: Phone, title: '문의', lines: ['02-1234-5678', '(평일 09:00~18:00)'], aside: { kind: 'art', label: 'books' } },
    { icon: Smartphone, title: '신청 바로가기', lines: ['QR코드를 스캔하여', '신청 페이지로 이동하세요.'], aside: { kind: 'qr', text: 'QR코드' } },
  ] satisfies ApplyStep[],
  notice: {
    title: '유의사항',
    items: ['모든 프로그램은 선착순으로 마감됩니다.', '프로그램 일정 및 내용은 도서관 사정에 따라 변경될 수 있습니다.', '자세한 내용은 도서관 홈페이지를 참고 바랍니다.'],
  },
}

export const cover = {
  arc: '오늘보다 더 나은 내일',
  title: ['평생 학습', '프로그램 안내'],
  slogan: '배우는 즐거움, 함께 성장하는 우리',
  center: 'LIFELONG LEARNING CENTER',
  url: 'www.umchungjoeun.kr',
}

export const footer: FooterText[] = [
  { text: '02-1234-5678', x: 55 },
  { text: 'dream@canvakorea.co.kr', x: 203 },
]

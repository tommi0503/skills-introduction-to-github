import type { TitledEntry } from '../shared-3233/components/TitledEntries'

export const brand = { name: '휴텍 미디어', latin: 'HuTech Media' }

export const cover = {
  headline: ['기술을 넘어', '가치를,', '내일의 비즈니스', '를 엽니다'],
  sub: ['휴텍 미디어가 제공하는', '차세대 맞춤형 IT 솔루션'],
}

export interface ContactRow {
  label: string
  value: string
}

export const contact = {
  title: '연락처',
  rows: [
    { label: '주소', value: '서울특별시 다정구 상상로 77 희망빌딩 1층\n00031' },
    { label: '대표 번호', value: '02-1234-5678' },
    { label: '이메일', value: 'dream@canvakorea.co.kr' },
  ] satisfies ContactRow[],
}

export const website = {
  title: '웹사이트',
  url: 'http://www.umchungjoeun.kr',
  qrLabel: 'QR코드\n입력',
  qrCaption: '바로가기 QR코드',
}

export const copyright = 'Copyright © 기업명 All rights reserved.'

export const about = {
  title: 'ABOUT US',
  subtitle: '미래를 향한 우리의 움직임',
  philosophy: {
    title: '기업 이념',
    entries: [
      { title: 'Mission', body: '기술을 통해 고객의 비즈니스 효율을 극대화하고 지속 가\n능한 성장을 돕습니다.' },
      { title: 'Vision 2030', body: '글로벌 시장을 선도하는 혁신 기술의 표준이 되겠습니다.' },
    ] satisfies TitledEntry[],
  },
  milestones: {
    title: '주요 성과',
    rows: [
      { year: '2024', text: '누적 고객사 [100개사] 돌파 및 시리즈 A 투자 유치' },
      { year: '2025', text: '[OO 기술 인증] 획득 및 산업통상자원부 장관상\n수상' },
      { year: '2026', text: '매출액 [200%] 성장 및 글로벌 해외 법인 설립' },
    ],
  },
}

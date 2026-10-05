import { festival, type LabeledValue } from '../shared-1718/data'

export interface ProgramDetail {
  title: string
  description: string
  bullets: string[]
}

export interface ScheduleItem {
  time: string
  label: string
}

export const greeting = {
  title: '초대의 글',
  /** Printed line breaks (justified block). */
  lines: [
    '도서관 책 축제는 지역 주민이 함께 만들어가는',
    '작은 축제입니다. 크지 않아도, 책과 사람 사이',
    '의 거리를 조금 더 가깝게 만드는 하루가 되기를',
    '바라는 마음으로 준비했습니다. 올 가을, 도서관',
    '앞 광장에서 만나요.',
  ],
}

export const schedule = {
  title: '프로그램 타임테이블',
  items: [
    { time: '10:00', label: '개막식 및 북마켓 오픈' },
    { time: '11:00', label: '어린이 그림책 놀이터' },
    { time: '13:00', label: '작가와의 만남' },
    { time: '15:00', label: '낭독 공연' },
    { time: '16:00', label: '시민 참여 북토크' },
    { time: '16:30', label: '경품 추첨 및 마무리 인사' },
  ] as ScheduleItem[],
}

export const programs = {
  title: '주요 프로그램 안내',
  /** Two columns, one per inner panel. */
  columns: [
    [
      {
        title: '개막식 및 북마켓',
        description: '축제 개막식과 함께, 독립출판물부터 특별 큐레이션 도서까지 다양하게 만날수 있는 북마켓이 펼쳐집니다.',
        bullets: ['장소 및 일시: 도서관 앞 광장 부스존  10:00 – 17:00', '대상: 전 연령'],
      },
      {
        title: '어린이 그림책 놀이터',
        description: '그림책 낭독과 함께 색칠, 만들기 등 간단한 놀이 활동이 이어져 아이들이 책과 친해질 수 있도록 구성했습니다.',
        bullets: ['장소 및 일시: 광장 내 어린이 체험존  11:00 – 12:30', '대상: 유아 및 초등 저학년 (보호자 동반)'],
      },
      {
        title: '작가와의 만남',
        description: '이해영 작가님의 목소리를 가까이에서 들어보는 시간입니다. 실내 프로그램으로 진행되는 만큼 좌석이 한정되어 있어 사전 신청을 권해드립니다.',
        bullets: ['장소 및 일시: 도서관 다목적홀 13:00 – 14:00', '대상: 성인 및 청소년 독자'],
      },
    ],
    [
      {
        title: '낭독 공연',
        description: '잔잔한 음악과 함께 어우러지는 낭독 무대로, 가을 오후 광장에 앉아 편안하게 즐기실 수 있는 프로그램입니다.',
        bullets: ['장소 및 일시: 광장 중앙 무대  15:00  15:40', '대상: 전 연령'],
      },
      {
        title: '시민 참여 북토크',
        description: '참가자들이 자유롭게 자신이 좋아하는 책을 소개하고 이야기 나누는 열린 토크 자리입니다.',
        bullets: ['장소 및 일시: 도서관 세미나실  16:00 – 16:30', '대상: 성인 및 청소년'],
      },
      {
        title: '경품 추첨 및 마무리 인사',
        description: '도서관과 지역 서점이 함께 준비한 소정의 경품을 추첨을 통해 전달해 드리며, 다음 축제를 기약하는 인사로 하루를 마무리합니다.',
        bullets: ['장소 및 일시: 광장 중앙 무대  16:30  17:00', '대상: 전체 참가자'],
      },
    ],
  ] as ProgramDetail[][],
}

export const participation = {
  title: '참가 안내',
  /** Printed line breaks. */
  lines: [
    '사전 신청은 다정구 도서관 홈페이지 또는 현장 접수처에서 가능합니다. 대부분의 프로그램은 현장',
    '참여도 환영하지만, 저자와의 만남 등 일부 인기 프로그램은 선착순으로 마감될 수 있으니 사전에 신',
    '청해 주세요.',
  ],
  contacts: [
    { label: '웹사이트', value: festival.website },
    { label: '전화문의', value: festival.phoneDashes },
  ] as LabeledValue[],
  qr: { label: 'QR코드', caption: '사전신청 페이지' },
}

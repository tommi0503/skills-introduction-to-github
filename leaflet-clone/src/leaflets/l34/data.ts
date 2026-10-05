export const greeting = {
  title: '인사말',
  paragraphs: [
    '안녕하세요, 라라나의원입니다.\n라라나의원은 지역 주민 여러분의 평생 건강 파트너가\n되고자 정확한 진단과 따뜻한 진료를 약속드립니다.',
    '작은 증상도 편하게 상담하세요. 가족을 진료하는\n마음으로 함께하겠습니다.',
  ],
}

export interface Doctor {
  name: string
  credentials: string[]
}

export const doctors = {
  title: '의료진 소개',
  list: [
    { name: '원장 김라라', credentials: ['내과 전문의', '대학교병원 내과 전공의 수료'] },
    { name: '원장 이태훈', credentials: ['가정의학과 전문의', '검진의학회 정회원'] },
    { name: '원장 김철수', credentials: ['내과 전문의', '대학교병원 내과 전공의 수료'] },
  ] satisfies Doctor[],
}

export interface DirectionItem {
  label: string
  value: string
}

export const directions = {
  title: '오시는 길',
  items: [
    { label: '주소', value: '서울특별시 다정구 상상로 77 희망빌딩 1층 00031' },
    { label: '지하철', value: '서울역 3번 출구 도보 3분' },
    { label: '버스', value: '라라나 정류장 하차 (140, 402, 3412-1)' },
    { label: '주차', value: '건물 지하주차장 1시간 무료' },
  ] satisfies DirectionItem[],
}

export interface HoursRow {
  day: string
  time: string
}

export const hours = {
  title: '진료 시간',
  rows: [
    { day: '평  일', time: '09:00 – 18:30' },
    { day: '토요일', time: '09:00 – 13:00' },
    { day: '점심 시간', time: '13:00 – 14:00' },
  ] satisfies HoursRow[],
  note: '* 일요일 및 공휴일은 휴진입니다.',
}

export const departments = ['내과', '가정의학과', '건강검진']

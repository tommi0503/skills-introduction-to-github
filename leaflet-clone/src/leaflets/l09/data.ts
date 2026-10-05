export interface Program {
  title: string
  desc: string[]
  schedule: string
}

export const programPanel = {
  heading: '체험 프로그램',
  items: [
    {
      title: '전통 미술 체험 워크샵',
      desc: ['전통적인 미술 기법을 배우고,', '다양한 재료를 활용하여 자신만의', '작품을 창작해봅니다'],
      schedule: '운영 시간: 수 오후 3시',
    },
    {
      title: '전통 미술 소개 가이드투어',
      desc: ['가이드와 함께 미술 기념 공원을', '돌아봅니다'],
      schedule: '운영 시간: 금 오후 3시',
    },
    {
      title: '명상과 다도 체험',
      desc: ['전문 명상가에게서 명상의 기본과', '다도를 배우며 마음의 평화를', '찾아봅니다'],
      schedule: '운영 시간: 토 오후 3시',
    },
  ] satisfies Program[],
}

export const visitPanel = {
  directions: { heading: '찾아오시는 길', address: '경상북도 안동시 풍천면 갈전리 2303', note: ': 자차 이용 시, 공용 주차장 이용 가능합니다' },
  hours: { heading: '운영 시간', lines: ['화~일 10:00-18:00 개관', '매 달 둘째주 화요일 휴무'] },
  contact: '방문 문의: 03-987-1533',
}

export const coverPanel = {
  lead: '과거로의 여행,',
  heading: '역사를 만나다',
  org: ['풍천문화재단', '한국역사기념공원 가이드'],
}

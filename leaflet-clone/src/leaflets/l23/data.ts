import type { BlobShape } from '../shared-2223/components/Blob'

export interface Program {
  id: string
  tag: string
  title: string
  photo: string
  /** Body copy, one entry per printed line (justified). */
  lines: string[]
}

export const programPanel = {
  heading: '체험 프로그램',
  programs: [
    {
      id: 'farm',
      tag: '농사 체험',
      title: '제철 농산물 수확',
      photo: 'children harvesting vegetables',
      lines: ['호미를 들고 부드러운', '흙을 파내며 영양 가득', '한 제철 농산물을 수확', '해 봅니다.'],
    },
    {
      id: 'taste',
      tag: '미각 체험',
      title: '건강한 시골 밥상',
      photo: 'bowls of country food',
      lines: ['직접 수확한 제철 재료', '로 차려낸 뷔페식 시골', '밥상으로 든든하게 배', '를 채웁니다.'],
    },
    {
      id: 'craft',
      tag: '공예 체험',
      title: '생태 공예 체험',
      photo: 'girl crafting with leaves',
      lines: ['산책길에 주운 나뭇잎,', '돌멩이, 나뭇가지 등을', '활용해 다양한 작품을', '만들어 볼 수 있습니다.'],
    },
  ] satisfies Program[],
  checklistHeading: '체험 갈때 준비물을 꼭 챙겨요!',
  checklist: ['편안한 옷과 운동화를 준비해요.', '챙이 넓은 모자와 선크림을 챙겨요.', '시원한 물과 개인 물병을 챙겨요.'],
}

export interface TimeSlot {
  time: string
  title: string
  details: string[]
}

export const schedulePanel = {
  heading: '체험 프로그램 시간표',
  slots: [
    { time: '09:00', title: '등록 및 오리엔테이션', details: ['참가자 확인, 전체 일정 안내 및', '안전 교육'] },
    { time: '10:00', title: '1부 체험 활동', details: ['메인 프로그램 진행 (이론 및 실습)', '농작물 수확 및 동물 먹이주기'] },
    { time: '12:00', title: '점심 식사 및 휴식', details: ['건강한 시골 밥상 점심식사'] },
    { time: '13:00', title: '2부 체험 활동', details: ['그룹별 심화 활동 또는', '전통 먹거리 및 생태 공예 체험'] },
    { time: '15:00', title: '티타임 및 중간 휴식', details: ['다과 제공 및 재정비 시간'] },
    { time: '15:30', title: '결과물 공유 및 리뷰', details: ['조별 발표, 체험 소감 나누기'] },
    { time: '16:30', title: '마무리 및 해산', details: ['수료증 및 기념품 배부'] },
  ] satisfies TimeSlot[],
}

export interface Faq {
  q: string
  a: string[]
}

export const faqPanel = {
  heading: '자주 묻는 질문',
  faqs: [
    {
      q: '비가 와도 체험이 진행되나요?',
      a: ['소나기나 가벼운 비가 내릴 경우 우비', '를 착용하고 운치 있게 진행합니다. 다', '만, 야외 활동이 불가능할 정도의 폭우', '가 내릴 경우 실내 대체 프로그램으로', '전환됩니다.'],
    },
    {
      q: '유아나 어르신도 참여할 수 있나요?',
      a: ['네, 누구나 즐기실 수 있습니다. 만 4', '세 이상 아이들에게 가장 추천하며,', '36개월 미만 유아는 무료로 입장 가', '능합니다. (단, 유아에게는 체험 물품', '및 식사가 별도 제공되지 않습니다.)'],
    },
    {
      q: '점심 식사는 어떻게 제공되나요?',
      a: ['마을 어르신들이 직접 기른 제철 농산', '물로 정성껏 차려낸 뷔페식 시골 밥상', '이 기본 제공됩니다. 개인적인 알레르', '기나 유아용 간식이 필요하신 경우 개', '인적으로 챙겨오셔도 좋습니다.'],
    },
  ] satisfies Faq[],
  art: [
    { id: 'tomato', x: 195, y: 862, width: 255, height: 160, radius: '46% 54% 40% 40% / 50% 50% 40% 40%', label: 'pink tomato' },
    { id: 'leaf', x: 380, y: 748, width: 60, height: 185, radius: '50%', rotate: 20, label: 'leaf' },
    { id: 'berry1', x: 50, y: 890, width: 52, height: 58, label: 'blue berry' },
    { id: 'berry2', x: 118, y: 857, width: 48, height: 52, label: 'blue berry' },
    { id: 'berry3', x: 103, y: 930, width: 50, height: 48, label: 'blue berry' },
  ] satisfies BlobShape[],
}

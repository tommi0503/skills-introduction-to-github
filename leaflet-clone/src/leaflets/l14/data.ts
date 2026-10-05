import type { InfoEntry } from '../shared-1314/components/InfoBlock'

export const intro = {
  headline: ['국내 최대 규모', '유아용품 박람회를', '놓치지 마세요!'],
  body: [
    '2030 국제 유아용품 중소기업 박람회는 전 세',
    '계 유아용품 제조업체 및 유통업체들이 참여하',
    '여 새로운 제품을 소개하고 비즈니스 네트워킹',
    '을 하는 행사입니다.',
  ],
  facts: ['1천 평 규모의 행사장', '총 450개 업체 참여', '식료품, 이동, 침구 등 다양한 산업군'],
}

export interface ListSection {
  title: string
  items: InfoEntry[]
}

export const booths: ListSection = {
  title: '부스 소개',
  items: [
    { title: '유아 의류 코너', lines: ['최신 유아 의류 및 패션 아이템을 전시하고', '판매합니다.'] },
    { title: '유아 장난감 코너', lines: ['안전하고 창의적인 유아 장난감을 체험하고', '구매할 수 있습니다.'] },
    { title: '유아 식품 및 영양 코너', lines: ['건강한 유아 식품 및 영양 제품을 소개합니', '다.'] },
  ],
}

export const programs: ListSection = {
  title: '프로그램',
  items: [
    { title: '산업 동향 세미나', lines: ['유아용품 산업에 대한 최신 동향 및 전문', '가 강연'] },
    { title: 'C&D 네트워킹 파티', lines: ['국제적인 유아용품 기업과의 네트워킹', '기회'] },
    { title: '상품 발표', lines: ['새로운 제품 발표 및 시연'] },
    { title: '유아용품 디자인 공모전', lines: ['참가업체들의 디자인 작품 전시 및 시상식'] },
  ],
}

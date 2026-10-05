/** Content shared by the two 강풍호 크루즈 leaflet designs (04, 05). */

export interface FareRow {
  /** Cruise type; a string[] means forced line breaks. */
  type: string[]
  adult: string
  youth: string
  child: string
}

export const cruise = {
  title: ['강풍호', '크루즈'],
  subtitle: '시티투어',
  english: ['STRONG WIND', 'CRUISE CITY TOUR'],
  tagline: '물에서 보는 도시 이야기',
  guide: {
    heading: '이용 안내',
    steps: ['온라인 사전 예약', '선착장 매표소에서 승선신고서 작성', '신분증 지참 필수', '티켓 수령 후 탑승'],
  },
  fares: {
    heading: '운항 요금',
    columns: { type: '크루즈 타입', adult: '대인', youth: '청소년', child: '소인' },
    rows: [
      { type: ['한강', '일몰 투어'], adult: '16,000원', youth: '14,000원', child: '11,000원' },
      { type: ['디너 앤', '샴페인'], adult: '179,000원', youth: '-', child: '-' },
      { type: ['선상 파티'], adult: '57,000원', youth: '-', child: '-' },
    ] as FareRow[],
  },
  directions: {
    heading: '선착장 오시는 길',
    pier: '선착장',
    address: '서울 용산구 용산동7가 60-19',
    transit: ['지하철 강풍역 3번출구 도보 7분', '버스 강풍역 1번출구 앞 정차: 7613, 6623, 262'],
  },
  qrCaption: ['크루즈 시티투어', '운항코스 확인'],
  contact: {
    heading: '예약 문의',
    lines: ['03-987-1533', '@dreamcanvakorea', 'www.umchungjoeun.kr'],
  },
}

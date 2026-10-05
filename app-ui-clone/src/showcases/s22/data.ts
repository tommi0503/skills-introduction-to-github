export interface CompanyResult {
  name: string
  bizNo: string
  address: string
}

export const companyQuery = '삼성'

export const companyResults: CompanyResult[] = [
  { name: '삼성전자(주)', bizNo: '1248100998', address: '경기 수원시 영통구 삼성로 129' },
  { name: '삼성디스플레이(주)', bizNo: '1428145237', address: '경기 용인시 기흥구 삼성로 1' },
  { name: '삼성SDI(주)', bizNo: '1248131282', address: '경기 용인시 기흥구 공세로 150-20' },
  { name: '삼성전기(주)', bizNo: '1248100979', address: '경기 수원시 영통구 매영로 150' },
  { name: '삼성에스디에스(주)', bizNo: '1108128774', address: '서울 송파구 올림픽로35길 125' },
  { name: '삼성중공업(주)', bizNo: '1208152780', address: '경기 성남시 분당구 판교로227번길 23' },
]

export interface WheelColumn {
  /** Visible items, top to bottom; the selected one sits on the 3rd row. */
  items: (string | null)[]
  /** Left edge of the column's text (logical px). */
  x: number
}

/** Visible rows of the date wheel (index 2 is the highlighted row). */
export const joinDateWheel: WheelColumn[] = [
  { x: 80.5, items: ['2023년', '2024년', '2025년', null, null] },
  { x: 178.5, items: ['4월', '5월', '6월', '7월', '8월'] },
  { x: 251.7, items: ['16일', '17일', '18일', '19일', '20일'] },
]

export const healthInsurance = { options: ['직장의료보험', '지역의료보험'], selected: 0 }
export const housing = { options: ['자가', '전세', '월세', '기타'], selected: 0 }

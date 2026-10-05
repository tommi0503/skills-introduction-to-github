import type { InfoEntry } from '../shared-1314/components/InfoBlock'

export interface ContactRow {
  label: string
  value: string
}

export interface StripeSpec {
  y: number
  height: number
  width: number
}

export const participation = {
  stripes: [
    { y: 48, height: 86, width: 184 },
    { y: 134, height: 85, width: 270 },
  ] satisfies StripeSpec[],
  title: '참가 안내',
  apply: {
    title: '참가 신청',
    lines: ['웹사이트에서 박람회 참가', '등록 양식을 제출해주세요.'],
  },
  contactTitle: '문의',
  contacts: [
    { label: '웹사이트', value: 'www.umchungjoeun.kr' },
    { label: '이메일', value: 'dream@canvakorea.co.kr' },
    { label: '전화', value: '03-987-1533' },
  ] satisfies ContactRow[],
}

export const directions = {
  title: '찾아오시는 길',
  routes: [
    { title: '주소', lines: ['서울 강남구 삼성로 7 명보빌딩 13층'] },
    { title: '버스 이용 시', lines: ['137번 삼성로 정류장 하차'] },
    { title: '지하철 이용 시', lines: ['삼성역 하차 후 도보 10분'] },
  ] satisfies InfoEntry[],
  credits: [
    { title: '주관', lines: ['중소기업 진흥청'] },
    { title: '후원', lines: ['공동육아협의회, 유아포스코,', '밝은미래만들기'] },
  ] satisfies InfoEntry[],
}

export const cover = {
  year: '2030',
  titleLines: ['유아용품', '박람회'],
  details: ['4.10(월) ~ 5.30(목)', '강남 대박람회장 A동'],
}

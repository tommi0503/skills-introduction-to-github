import { Globe, MessageSquareMore, Phone, Pill, Syringe, ConciergeBell, type LucideIcon } from 'lucide-react'

export interface CareService {
  /** lucide glyph, or null when the artwork (stomach, lungs) has no lucide equivalent. */
  icon: LucideIcon | null
  title: string
  detail: string
}

export const care = {
  title: '진료 안내',
  services: [
    { icon: Pill, title: '내과 일반 진료', detail: '감기, 몸살, 소화불량, 복통, 두통' },
    { icon: null, title: '소화기 클리닉', detail: '위·대장 내시경, 역류성 식도염' },
    { icon: null, title: '호흡기 클리닉', detail: '천식, 알레르기 비염, 만성 기침' },
    { icon: Syringe, title: '예방접종', detail: '독감, 폐렴구균, 대상포진, A/B형 간염' },
  ] satisfies CareService[],
  symptomsTitle: '이런 증상이 있다면 방문하세요',
  symptoms: ['감기 기운이 일주일 이상 지속될 때', '속쓰림·소화불량이 반복될 때', '혈압·혈당 수치가 걱정될 때', '혈압·혈당 수치가 걱정될 때'],
}

export interface ProgramRow {
  program: string
  target: string
  main: string
  sub?: string
}

export const checkup = {
  title: '건강검진 프로그램',
  subtitle: '국가건강검진 지정기관',
  headers: { program: '프로그램', target: '대상', main: '주요 항목' },
  rows: [
    { program: '국가일반검진', target: '만 20세 이상', main: '혈액·소변검사,\n흉부 X-ray' },
    { program: '기본 종합검진', target: '성인 누구나', main: '심전도', sub: '일반검진 + 초음파' },
    { program: '정밀 종합검진', target: '40세 이상 권장', main: '내시경', sub: '기본검진 + 위·대장' },
    { program: '채용검진', target: '취업 예정자', main: '당일 결과지 발급 가능' },
  ] satisfies ProgramRow[],
  stepsTitle: '검진 절차',
  steps: ['전화 또는 챗봇 예약', '검진 전 8시간 금식', '검진 진행 (약 1시간)', '결과 상담 (7일 이내)'],
}

export interface ReserveMethod {
  label: string
  value: string
  icon: LucideIcon
}

export interface Faq {
  q: string
  a: string
}

export const guide = {
  title: '이용 안내',
  reserveTitle: '진료 예약 방법',
  methods: [
    { label: '전화 예약', value: '02-1234-5678', icon: Phone },
    { label: '챗봇 예약', value: '@dreamcanvakorea', icon: MessageSquareMore },
    { label: '지도 앱 예약', value: '라라나의원 검색', icon: Globe },
    { label: '당일 접수', value: '방문 진료 가능', icon: ConciergeBell },
  ] satisfies ReserveMethod[],
  notice: {
    title: '처음 방문하시나요?',
    body: '신분증을 지참해 주세요!\n국가검진 대상자는 검진 안내문을 준비하시면 접수\n가 빨라집니다.',
  },
  faqTitle: '자주 묻는 질문',
  faqs: [
    { q: '주차는 어떻게 하나요?', a: '건물 지하주차장 이용 시 1시간 무료입니다.' },
    { q: '검진 결과는 언제 나오나요?', a: '기본검진 3일, 종합검진 7일 이내 안내드립니다.' },
    { q: '실비보험 서류 발급 되나요?', a: '진단서 · 진료확인서 · 영수증 즉시 발급 가능합니다.' },
  ] satisfies Faq[],
}

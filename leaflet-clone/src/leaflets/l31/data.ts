import type { Artwork } from '../shared-3031/components/ArtworkLayer'
import type { RichLine } from '../shared-3031/components/RichLines'

const r = (text: string): RichLine => ({ text })
const b = (text: string): RichLine => ({ text, strong: true })

/** Panel 1 — programme introduction. */
export const intro = {
  title: ['지역 성장', '지원사업'],
  paragraphs: [
    [r('지역 내 기업과 소상공인의 성장 기반'), r('마련을 위해 맞춤형 지원 프로그램을 운영합니다.')],
    [b('전문 컨설팅을 통해 안정적인 성장과'), b('지속 가능한 발전을 돕습니다.')],
    [r('본 사업은 성장 가능성을 가진 기업 및'), r('소상공인을 대상으로 필요한 자원과'), r('전문 서비스를 제공하여 경쟁력 강화와'), r('안정적인 사업 운영을 지원합니다.')],
    [r('참여자의 상황에 맞춘 단계별 지원을 통해'), b('새로운 기회를 발굴하고'), b('지속 가능한 성장을 만들어갑니다.')],
  ],
  figure: {
    label: 'two colleagues at desk illustration',
    x: 22,
    y: 662,
    w: 436,
    h: 356,
    clipPath:
      'polygon(168px 58px, 218px 38px, 268px 62px, 300px 20px, 348px 0, 398px 28px, 400px 100px, 436px 140px, 430px 356px, 0 356px, 0 218px, 88px 218px, 98px 170px, 150px 128px)',
  } satisfies Artwork,
}

/** Panel 2 — main services heading. */
export const services = {
  title: ['주요 사업', '지원 내용'],
  lead: [r('[Customized Support Program]'), r('전문적인 컨설팅부터 역량 강화 교육,'), b('실질적인 성장을 위한 서비스를 운영합니다.')],
}

export interface ServiceItem {
  key: string
  heading: string[]
  bullets: string[]
}

/** Service grid spanning panels 2–3 (sheet coordinates). */
export const serviceGrid = {
  card: { x: 516, y: 389, w: 887, h: 566 },
  columns: [560, 1005],
  rows: [439, 610, 780],
  circle: 125,
  textOffset: { x: 151, y: 10 },
  items: [
    { key: 'consult', heading: ['전문가 상담 및', '성장 전략'], bullets: ['사업 운영 문제 해결 지원', '분야별 전문가 상담 제공'] },
    { key: 'promo', heading: ['홍보 콘텐츠 제작 및', '온라인 홍보'], bullets: ['브랜드 및 홍보 콘텐츠 제작', '온라인 마케팅 전략 지원'] },
    { key: 'skill', heading: ['실무 역량', '강화 프로그램'], bullets: ['디지털 활용 교육', '콘텐츠 제작 실습'] },
    { key: 'network', heading: ['교류 및 협력', '기회 제공'], bullets: ['참여자 네트워킹', '그룹 활동'] },
    { key: 'execute', heading: ['실행 및', '운영 지원'], bullets: ['사업 실행 계획 수립', '제품 및 서비스 개선 지원'] },
    { key: 'mentor', heading: ['멘토링', '프로그램'], bullets: ['1:1 멘토링', '분야별 상담'] },
  ] satisfies ServiceItem[],
}

/** Panel 3 — application steps. */
export const procedure = {
  title: ['지원 절차'],
  steps: [
    { no: '01', label: '사업 신청' },
    { no: '02', label: '심사 및 선정' },
    { no: '03', label: '프로그램 참여' },
    { no: '04', label: '결과 관리' },
  ],
}

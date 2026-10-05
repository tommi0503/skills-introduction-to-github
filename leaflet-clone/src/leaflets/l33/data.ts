import type { TitledEntry } from '../shared-3233/components/TitledEntries'

export interface ServiceSection {
  title: string
  body?: string
  entries?: TitledEntry[]
}

export interface ServiceContent {
  iconBox: { width: number; height: number }
  /** Left content inset of the panel (px). */
  inset: number
  label: string
  headline: string
  sections: ServiceSection[]
}

export const services: ServiceContent[] = [
  {
    iconBox: { width: 161, height: 179 },
    inset: 47,
    label: 'SERVICE 01',
    headline: '비즈니스의 속도를 바꾸는\n핵심 솔루션',
    sections: [
      {
        title: '올인원 데이터 관리 시스템',
        body: '분산되어 있던 기업의 데이터를 하나의 플랫폼에서 실시\n간으로 통합하고 분석하세요. 중소기업부터 대기업까지\n모두 적용 가능한 유연한 아키텍처로 설계되었습니다.',
      },
      {
        title: '핵심 장점',
        entries: [
          { title: '비용 절감', body: '기술을 통해 고객의 비즈니스 효율을 극대화하고 지속 가\n능한 성장을 돕습니다.' },
          { title: '보안 강화', body: '글로벌 시장을 선도하는 혁신 기술의 표준이 되겠습니다.' },
          { title: '간편한 도입', body: '별도의 장비 설치 없이 웹 로그인만으로 즉시 시작' },
        ],
      },
    ],
  },
  {
    iconBox: { width: 168, height: 160 },
    inset: 41,
    label: 'SERVICE 02',
    headline: '경쟁사와 차별화되는 우리만의\n기술력',
    sections: [
      {
        title: '인공지능(AI) 기반 예측 고도화 서비스',
        body: '과거 데이터 학습에 머무르는 기존 시스템과 다릅니다. 휴\n텍 미디어의 AI 솔루션은 실시간 시장 트렌드와 내부 데이\n터를 결합해 가장 정확한 미래 수요를 예측합니다.',
      },
      {
        title: '차별화 포인트',
        entries: [
          { title: '정확도 [98%]', body: '독자적으로 개발한 AI 예측 알고리즘 탑재' },
          { title: '맞춤형 커스텀', body: '귀사의 비즈니스 도메인에 딱 맞춘 대시보드 UI 제공' },
        ],
      },
    ],
  },
]

export const partners = {
  title: 'PARTNERS',
  subtitle: '신뢰로 검증된 비즈니스 파트너',
  lead: '수많은 선두 기업들이 이미 휴텍 미디어와\n함께하고 있습니다.',
  caseStudy: {
    title: '성공 사례',
    body: '[OO 유통 기업] 도입 사례: 재고 관리 솔루션 도입 후, 과\n잉 재고 문제를 [35%] 해결하여 연간 [O억 원]의 비용을\n절감했습니다.',
  },
  logos: { title: '파트너사', count: 9, columns: 3 },
  callout: '지금 바로 비즈니스 파트너가 되어보세요.\n귀사의 지속 가능한 성장을 위해 휴텍 미디어가\n가장 든든한 동반자가 되어 드리겠습니다.\n(도입 및 제휴 문의: 02-1234-5678)',
}

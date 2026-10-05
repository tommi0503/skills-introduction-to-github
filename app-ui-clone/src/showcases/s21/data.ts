export const amountOptions = ['30만원', '50만원', '70만원', '100만원']

export const cardInfo = { issuer: '우리카드', name: '카드의 정석 WOWRI' }

export const alertQuestion = '얼마를 써야 혜택을 받나요?'
export const amountPlaceholder = '만원 단위로 입력해주세요.'

export const doneTitle = ['알림 설정 완료!', '실적 확인을 위해 알려드릴게요']

export const doneNotes = [
  '카드 실적을 확인할 수 있도록 알려드려요.',
  '카드 실적은 카드조회 화면에서 확인할 수 있어요. 알림을\n설정한 경우에는 다음달부터 안내해드려요.',
  '카드사 별로 실적으로 인정되지 않는 결제 내역이 있을 수\n있어요. 정확한 기준은 카드사에서 확인해 주세요.',
]

export interface CardCharge {
  card: string
  amount: string
  badge?: string
}

export interface BillingDay {
  date: string
  total: string
  charges: CardCharge[]
}

export interface BillingMonth {
  month: string
  total: string
  /** Green when the month is still upcoming, grey for past statements. */
  tone: 'accent' | 'muted'
  days: BillingDay[]
}

export const upcomingBilling: BillingMonth[] = [
  {
    month: '3월',
    total: '총 610,618원',
    tone: 'accent',
    days: [
      {
        date: '3월 14일 (금)',
        total: '610,618원',
        charges: [
          { card: '신한카드', amount: '262,235원' },
          { card: 'KB국민카드', amount: '205,074원' },
          { card: '우리카드', amount: '143,309원' },
        ],
      },
    ],
  },
  {
    month: '2월',
    total: '총 168,295원',
    tone: 'accent',
    days: [{ date: '2월 25일 (화)', total: '168,295원', charges: [{ card: '비씨카드', amount: '168,295원', badge: '확정' }] }],
  },
]

export const pastBilling: BillingMonth[] = [
  {
    month: '2월',
    total: '총 2,956,280원',
    tone: 'muted',
    days: [{ date: '2월 14일 (금)', total: '2,956,280원', charges: [] }],
  },
]

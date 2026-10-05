export interface StoreRow {
  name: string
  method: string
  description?: string
  /** Logo placeholder size (logical px). */
  logo: { width: number; height: number }
}

export const storeChips = ['전체', '편의점', 'F&B', '마트/생활', '주유']

export const stores: StoreRow[] = [
  { name: 'CU', method: '네이버페이 QR코드 스캔', logo: { width: 52, height: 32 } },
  { name: 'GS25', method: '네이버페이 QR코드 스캔', logo: { width: 59, height: 19 } },
  {
    name: '7-ELEVEN',
    method: '네이버페이 QR코드 스캔',
    description: 'QR코드 스캔 가능한 계산기에서만 결제 가\n능. 일부 특수 매장 결제불가',
    logo: { width: 47, height: 46 },
  },
  { name: '이마트24', method: '네이버페이 QR코드 스캔', logo: { width: 67, height: 14 } },
  { name: '맘스터치', method: '네이버페이 QR코드 스캔', logo: { width: 56, height: 29 } },
  { name: '다이소', method: '바코드/QR결제 > 스캔', description: '일부 매장 결제불가\n(매장 사정에 따라 다를 수 있음)', logo: { width: 64, height: 16 } },
]

export interface InfoParagraph {
  text: string
  tone: 'strong' | 'accent' | 'body'
  /** Extra space above (logical px). */
  gap?: number
}

export const quickPayInfo: InfoParagraph[] = [
  { tone: 'strong', text: '바로결제를 사용하면 비밀번호나 생체 인증 단계 없이\n더 빠르고 간편하게 결제하실 수 있습니다.' },
  {
    tone: 'accent',
    gap: 10.8,
    text: '네이버페이의 부정거래방지시스템(FDS)이 상시 모니터링\n중이며 바로결제를 ON으로 설정했더라도 추가 확인이 필요\n한 경우 비밀번호 또는 생체 인증, ARS 본인 확인이 요청될\n수 있습니다.',
  },
  { tone: 'body', gap: 10.8, text: '바로결제 동작 환경\n· 현장결제: 네이버페이 앱, 네이버 앱' },
  { tone: 'body', gap: 10.3, text: '바로결제를 사용하기 전에 기기의 잠금을 설정해주세요.' },
  {
    tone: 'body',
    gap: 10.3,
    text: '휴대전화 분실이나 도난 시 네이버페이 결제도용센터\n(1588-3816)로 빠르게 신고 부탁드립니다.\n분실이나 도난 통지 전 제3자가 바로결제를 이용하여 발생\n하는 손해는 네이버페이에서 책임지지 않습니다.',
  },
]

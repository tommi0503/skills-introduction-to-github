import {
  Car,
  CircleUserRound,
  House,
  MapPin,
  MessageCircleMore,
  FileText,
  UserRound,
  Warehouse,
  type LucideIcon,
} from 'lucide-react'

export interface Category {
  key: string
  icon: LucideIcon
  label: string
}

export const homeHeader = { town: '반포동' }

export const categories: Category[] = [
  { key: 'job', icon: CircleUserRound, label: '알바' },
  { key: 'estate', icon: Warehouse, label: '부동산' },
  { key: 'car', icon: Car, label: '중고차' },
]

export interface Listing {
  key: string
  /** Leading emoji (rendered as a placeholder glyph). */
  emoji?: boolean
  title: string
  meta: string
  price: string
  comments?: number
  likes?: number
  menu?: boolean
}

export const listings: Listing[] = [
  { key: 'apt', title: '반포미도아파트 33평 10층', meta: '반포동 · 3일 전', price: '월세 6억/70만원', comments: 4, likes: 21, menu: true },
  { key: 'iphone', title: '아이폰13 128GB 화이트 (박스, 케이블 포함)', meta: '역삼1동 · 45분 전', price: '390,000원', likes: 3, menu: true },
  {
    key: 'kodak',
    emoji: true,
    title: '코닥 일회용 플래쉬 카메라 펀 세이버 27 (27컷 촬영가능)',
    meta: '동작구 흑석동 · 끌올 1개월 전',
    price: '20,000원',
    comments: 3,
    likes: 9,
  },
  { key: 'tumbler', title: '대용량 텀블러(42oz/1250ml)', meta: '논현2동 · 2분 전', price: '5,000원', menu: true },
  { key: 'next', title: '', meta: '', price: '', menu: true },
]

export const writeLabel = '글쓰기'

export interface Tab {
  key: string
  icon: LucideIcon
  label: string
}

export const tabs: Tab[] = [
  { key: 'home', icon: House, label: '홈' },
  { key: 'life', icon: FileText, label: '동네생활' },
  { key: 'map', icon: MapPin, label: '동네지도' },
  { key: 'chat', icon: MessageCircleMore, label: '채팅' },
  { key: 'my', icon: UserRound, label: '나의 당근' },
]

export const seller = { name: '청포도', town: '동작구 흑석동', temp: '43.3°C', tempLevel: 0.42, tempLabel: '매너온도' }

export const article = {
  title: '코닥 일회용 플래쉬 카메라 펀 세이버 27 (27컷 촬영가능)',
  category: '취미/게임/음반',
  meta: '끌올 1개월 전',
  /** Paragraph lines; `emoji` count appended as placeholder glyphs. */
  body: [
    { text: '새 상품입니다.' },
    { text: '선물받았는데 이미 집에 필름카메라가 있어서 팔아요,,', emoji: 2 },
    { text: '3000원 할인가로 팔아요!' },
  ],
  placeLabel: '거래 희망 장소',
  place: '중앙대 중문',
  price: '20,000원',
  priceNote: '가격 제안 불가',
  cta: '채팅하기',
}

export const chat = {
  partner: '청포도',
  temp: '43.3°C',
  response: '보통 10분 이내 응답',
  product: { status: '판매중', title: '코닥 일회용 플래쉬 카메라 펀 세이버 27 (27컷 촬영가능)', price: '20,000원', note: '(가격제안불가)' },
  actions: [
    { key: 'date', label: '3/21 (금) 오후 6:20' },
    { key: 'pay', label: '당근페이' },
    { key: 'add', label: '물품추가' },
  ],
  input: '메시지 보내기',
}

export type ChatItem =
  | { kind: 'in'; key: string; text: string; time: string; avatar?: boolean }
  | { kind: 'out'; key: string; text: string; time: string }
  | { kind: 'notice'; key: string; label: string; text: string; link: string }
  | { kind: 'appointment'; key: string; title: string; lines: string[]; action: string; time: string }
  | { kind: 'system'; key: string; text: string; link: string }
  | { kind: 'sticker'; key: string; status: string; time: string }

export const messages: ChatItem[] = [
  { kind: 'in', key: 'm0', text: '안녕드리고 할게요~', time: '오후 9:42' },
  { kind: 'out', key: 'm1', text: '네 개찰구쪽으로 가겠습니다~', time: '오후 9:43' },
  { kind: 'in', key: 'm2', text: '네~ 내일뵐게요!', time: '오후 9:43', avatar: true },
  {
    kind: 'notice',
    key: 'n1',
    label: '안내',
    text: '당근당근v님과 거래 예약을 했어요. 당근페이로 채팅방에서 바로 송금할 수 있어요.',
    link: '송금하기',
  },
  {
    kind: 'appointment',
    key: 'a1',
    title: '약속을 만들었어요.',
    lines: ['날짜: 3월 21일 (금)', '시간: 오후 6:20'],
    action: '약속 보기',
    time: '오후 9:44',
  },
  { kind: 'system', key: 's1', text: '약속 시간 전 알림을 받아보세요.', link: '알림 설정' },
  { kind: 'sticker', key: 'st', status: '전송됨', time: '오후 9:44' },
]

export const sales = {
  title: '나의 판매내역',
  write: '글쓰기',
  tabs: ['판매중 2', '거래완료', '숨김'],
  filter: '홍보가능만 보기',
  actions: ['끌어올리기', '홍보하기'],
  items: [
    { key: 'xm5', title: '소니 WH-1000XM5 헤드폰', meta: '반포동 · 51분 전', price: '450,000원' },
    { key: 'ch710', title: '소니 WH-CH710N 블랙 블루투스 헤드폰', meta: '반포동 · 51분 전', price: '400,000원' },
  ] satisfies Listing[],
}

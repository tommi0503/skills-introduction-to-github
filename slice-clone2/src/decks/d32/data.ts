export const cover = { season: '2080 F/W', brand: 'MIRIGOLF', script: 'Catalog', lines: ['새로운 시즌,', '더 완벽한 라운딩을 준비하세요.'], logo: 'MIRI', side: ['Play Beyond Limits', "This season's collection is designed for greater distance, precision control, and an effortless swing.", 'Elevate your performance on the course to the next level.'] }
export const contents = {
  blurb: { title: 'Play Beyond Limits', lines: ["This season's collection is designed for greater distance,", 'precision control, and an effortless swing. Elevate your', 'performance on the course to the next level.'] },
  cols: [
    { no: '01', title: '시즌 컬렉션', items: [['시즌컨셉', 'Season Concept'], ['핵심 포인트', 'Collection Features'], ['제품 카테고리', 'Product Categories']] },
    { no: '02', title: '제품 라인업', items: [['베스트셀러', 'Best Sellers'], ['제품 라인업', 'Product Lineup'], ['제품 상세', 'Product Detail'], ['필드 스타일링', 'Golf Styling'], ['골프 액세서리', 'Accessories']] },
    { no: '03', title: '구매 가이드', items: [['클럽 선택가이드', 'Club Buying Guide'], ['시즌 프로모션', 'Special Promotion'], ['매장 및 문의', 'Store & Contact']] },
  ],
  page: '00P',
}
export const concept = { words: ['Play', 'Beyond', 'Limits'], lead: '한계를 넘어, 최고의 플레이를 경험하다.', body: ['이번 시즌 컬렉션은 더 긴 비거리, 더 정교한 컨트롤,', '그리고 더 가벼운 스윙을 위해 설계되었습니다.', '필드 위에서 당신의 퍼포먼스를 한 단계 끌어올려 보세요.'] }
export const lookbook = { lines: ['새로운 시즌, 필드 위에서', '==가장 돋보이는 스타일==을 만나보세요.'] }
export const features = {
  lead: ['한층 향상된', '==퍼포먼스==와 완성도 높은', '==플레이==를 경험해 보세요'],
  body: ['이번 시즌 컬렉션은 **비거리,**', '**안정성, 경량화, 프리미엄 소재**를', '중심으로 설계되었습니다.'],
  points: [
    { kr: ['비거리 향상을', '위한 설계'], en: 'Longer Distance' },
    { kr: ['정교한 컨트롤과', '일관된 방향성'], en: 'Precision Control' },
    { kr: ['가벼운 무게로', '편안한 스윙'], en: 'Lightweight Design' },
    { kr: ['프리미엄 소재를 적용한', '높은 내구성과 타구감'], en: 'Premium Materials' },
  ],
}
export const categories = {
  lead: ['드라이버부터 액세서리까지,', '필드를 완성하는 ==다양한 골프 아이템==을 한눈에 만나보세요.'],
  items: [['Driver', '드라이버', '긴 비거리와 안정적인 티샷'], ['Iron', '아이언', '정확한 거리와 방향성'], ['Putter', '퍼터', '안정적인 퍼팅 밸런스'], ['Golf Ball', '골프공', '플레이 스타일에 맞는 성능'], ['Apparel', '골프웨어', '기능성과 스타일을 동시에'], ['Accessories', '골프 액세서리', '라운드를 완성하는 필수 아이템']] as const,
}
export const section = { cap: 'P', rest: 'roduct LineUp', items: [['베스트셀러', 'Best Sellers'], ['제품 라인업', 'Product Lineup'], ['제품 상세', 'Product Detail'], ['필드 스타일링', 'Golf Styling'], ['골프 액세서리', 'Accessories']] as const, page: '00P' }
export const best = {
  lead: '많은 골퍼들에게 사랑받는 ==대표 인기 제품==을 소개합니다.',
  items: [
    { en: 'PRO X Driver', kr: '프로 X 드라이버', price: '₩689,000', points: ['카본 복합 소재 헤드 적용', '높은 관용성으로 안정적인 방향성', '로프트 각도 조절 가능'] },
    { en: 'Elite Iron Set', kr: '엘리트 아이언 세트', price: '1,290,000', points: ['단조 페이스로 부드러운 타구감', '최적의 무게 중심 설계', '미스샷에도 안정적인 비거리'] },
    { en: 'Premium Golf Bag', kr: '프리미엄 골프백', price: '249,000', points: ['경량 설계로 편안한 휴대성', '클럽과 액세서리를 위한 넉넉한 수납공간', '생활 방수 소재와 견고한 프레임 적용'] },
  ],
}
export const lineup = {
  title: ['PRO X', 'Series'],
  body: ['드라이버부터 퍼터까지 하나의 퍼포먼스', '컨셉으로 완성한 골프 클럽 시리즈입니다.', '일관된 스윙 감각과 안정적인 플레이를', '경험해 보세요.'],
  head: ['No.', '제품명', '추천 플레이', '주요 특징', '가격'],
  rows: [
    ['PRO X Driver', '티샷', ['최대 비거리와', '높은 관용성'], '₩689,000'],
    ['PRO X Fairway Wood', '롱게임', ['안정적인 탄도와', '긴 비거리'], '₩429,000'],
    ['PRO X Hybrid', '중·장거리', ['쉬운 볼 컨택과', '높은 정확도'], '₩359,000'],
    ['PRO X Iron Set', '아이언 샷', ['정교한 컨트롤과', '부드러운 타구감'], '₩1,290,000'],
    ['PRO X Wedge', '쇼트게임', ['뛰어난 스핀과', '거리 조절'], '₩199,000'],
    ['PRO X Putter', '퍼팅', ['안정적인', '스트로크와 방향성'], '₩329,000'],
  ] as const,
}
export const detail = {
  name: '==PRO X== Driver', kr: '프로 엑스 드라이버', priceLabel: '소비자가', price: '₩689,000',
  card: { lead: ['더 멀리,', '더 정확하게.'], body: ['비거리와 방향성을 모두 고려한 설계로', '안정적인 티샷을 완성하는 프리미엄 퍼포먼스', '드라이버입니다.'] },
  key: ['Key Features', '핵심 특징'], spec: ['Product', 'Specification', '제품 사양'],
  features: [
    ['Carbon Crown Design', '가벼운 카본 크라운을 적용하여 헤드 무게를 최적화하고스윙 스피드를 향상시킵니다.'],
    ['High Rebound Face', '고반발 페이스 설계로 볼 스피드를 높여 더 긴 비거리를 제공합니다.'],
    ['Optimized Weight Balance', '최적의 무게 중심 설계로 미스샷에도 안정적인 탄도와 일관된 방향성을 유지합니다.'],
  ] as const,
  specs: [['헤드 크기', '460cc'], ['로프트', '9° / 10.5°'], ['라이각', '58.5°'], ['샤프트', 'Graphite'], ['플렉스', 'R / SR / S'], ['총 중량', '약 305g'], ['권장 대상', '초급 ~ 상급']] as const,
}
export const styling = {
  title: ['WOMEN\'S', 'LOOK'], body: ['기능성과 스타일을 모두 갖춘 아이템으로', '라운드마다 완성도 높은 골프 스타일을', '연출해 보세요.'],
  list: [['01', 'Performance Polo Shirt  ₩89,000'], ['02', 'Pleated Golf Skirt  ₩129,000'], ['03', 'Classic Logo Cap  ₩39,000'], ['04', "Women's Golf Glove  ₩29,000"], ['05', 'Air Motion Golf Shoes  ₩229,000'], ['06', 'Premium Stand Bag  ₩249,000']] as const,
  outfit: 'FW SIGNITURE Black & White Outfit', outfitYear: '2080 ',
  outfitBody: ["This season's collection is designed for greater distance, precision control, and an effortless swing.", 'Elevate your performance on the course to the next level.'],
  labels: [['01', 520, 194], ['02', 520, 314], ['03', 520, 466], ['04', 677, 194], ['05', 682, 415], ['06', 862, 194]] as const,
}
export const accessories = {
  lead: ['필드에서의 편안함과 완성도 높은 플레이를 위한', '==필수 액세서리==를 만나보세요.'],
  tall: { en: 'Premium Stand Bag', kr: '프리미엄 스탠드백', price: '₩249,000' },
  top: [{ en: 'Classic Logo Cap', kr: '클래식 로고 캡', price: '₩39,000' }, { en: 'Tour Golf Glove', kr: '투어 골프 장갑', price: '₩29,000' }],
  bottom: [{ en: 'Performance Golf Balls', kr: '포먼스 골프공', price: '₩59,000' }, { en: 'Magnetic Ball Marker', kr: '마그네틱 볼 마커', price: '₩19,000' }, { en: 'Utility Pouch', kr: '유틸리티 파우치', price: '₩49,000' }],
}
export const promo = {
  title: ['Season ', 'Event'], sub: '신제품 출시 기념 특별 시즌 이벤트', periodLabel: '이벤트 기간', period: '2080년 3월 1일(월) - 4월 30일(금)',
  items: [['전 품목', '최대 30% 할인'], ['금액 상관없이', '무료배송'], ['기간 내', '멤버십 추가 적립']] as const,
}
export const contact = {
  oval: 'CONTACT', lines: ['가까운 매장에 방문하여', '==원하는 제품을 직접 체험==해 보고', '전문 상담을 통해 ==나에게 맞는==', '==골프 스타일==을 찾아보세요'],
  label: 'SHOWROOM', info: ['미리시 미리구 미리로 00 1F, 미리골프', '평일 10:30–20:00 / 주말·공휴일 11:00–19:00', 'TEL. 00-0000-0000'],
}

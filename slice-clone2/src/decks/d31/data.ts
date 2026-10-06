export const cover = {
  title: ['SEASON NEW', 'COLLECTION'], year: '2080', tagline: 'Play Beyond Limits',
  bottom: '새로운 시즌, **더 완벽한 라운딩**을 준비하세요.', right: ['가을 라운딩을 위한', '골프 시즌 신상 카탈로그'],
}
export const contents = {
  title: 'CONTENTS', kr: '목차', side: ['SEASON NEW ', 'COLLECTION'],
  groups: [
    { no: '01', en: 'COLLECTION', kr: '시즌 컬렉션', cy: 262, items: [['01 시즌 컨셉', 'SEASON CONCEPT'], ['02 핵심 포인트', 'COLLECTION FEATURES'], ['03 제품 카테고리', 'PRODUCT CATEGORIES']] },
    { no: '02', en: 'PRODUCT LINEUP', kr: '제품 라인업', cy: 391, items: [['04 베스트셀러', 'BEST SELLERS'], ['05 제품 라인업', 'PRODUCT LINEUP'], ['06 제품 상세', 'PRODUCT DETAIL'], ['07 필드 스타일링', 'GOLF STYLING'], ['08 골프 액세서리', 'ACCESSORIES COLLECTION']] },
    { no: '03', en: 'BUYING GUIDE', kr: '구매 가이드', cy: 575, items: [['09 클럽 선택 가이드', 'CLUB BUYING GUIDE'], ['10 시즌 프로모션', 'SPECIAL PROMOTION'], ['11 매장 및 문의', 'STORE & CONTACT']] },
  ],
}
export const concept = {
  title: '시즌 컨셉', caption: '2080 F/W SEASON CONCEPT', big: ['PLAY', 'BEYOND', 'LIMITS'],
  lead: '__한계를 넘어__ 최고의 플레이를 경험하다',
  body: ['이번 시즌 컬렉션은 더 긴 비거리, 더 정교한 컨트롤,', '그리고 더 가벼운 스윙을 위해 설계되었습니다.', '필드 위에서 당신의 퍼포먼스를 한 단계 끌어올려 보세요.'],
}
export const lookbook = { title: '시즌 룩북', caption: 'SEASON LOOKBOOK', lines: ['새로운 시즌 필드 위에서', '가장 돋보이는 스타일을 만나보세요.'] }
export const features = {
  title: '이번 시즌 핵심 포인트', caption: 'COLLECTION FEATURES',
  lead: ['한층 향상된 **퍼포먼스**와', '완성도 높은 **플레이**를 경험해 보세요.'],
  body: ['이번 시즌 컬렉션은 비거리, 안정성, 경량화,', '프리미엄소재를 중심으로 설계되었습니다.'],
  items: [
    { en: ['LONGER', 'DISTANCE'], kr: ['비거리 향상을', '위한 설계'] },
    { en: ['PRECISION', 'CONTROL'], kr: ['정교한 컨트롤과', '일관된 방향성'] },
    { en: ['LIGHTWEIGHT', 'DESIGN'], kr: ['가벼운 무게로', '편안한 스윙'] },
    { en: ['PREMIUM', 'MATERIALS'], kr: ['프리미엄 소재를 적용한', '높은 내구성과 타구감'] },
  ],
}
export const categories = {
  title: '제품 카테고리', caption: 'PRODUCT CATEGORIES',
  lead: '**드라이버부터 액세서리까지,** 필드를 완성하는 다양한 골프 아이템을 한눈에 만나보세요.',
  items: [
    ['DRIVER', '드라이버', '긴 비거리와 안정적인 티샷'], ['PUTTER', '퍼터', '안정적인 퍼팅 밸런스'], ['IRON', '아이언', '정확한 거리와 방향성'],
    ['GOLF BALL', '골프공', '플레이 스타일에 맞는 성능'], ['APPAREL', '골프웨어', '기능성과 스타일을 동시에'], ['ACCESSORIES', '골프 액세서리', '라운드를 완성하는 필수 아이템'],
  ] as const,
}
export const section = { kicker: ['SEASON NEW ', 'COLLECTION'], no: '02', title: ['PRODUCT', 'LINEUP', '제품 라인업'] }
export const best = {
  title: '베스트셀러', caption: 'BEST SELLERS',
  lead: '많은 골퍼들에게 사랑받는 **대표 인기 제품**을 소개합니다.',
  items: [
    { name: 'PRO X DRIVER | 프로 X 드라이버', price: '₩689,000', sub: '더 멀리, 더 정확한 티샷을 위한 드라이버', points: ['카본 복합 소재 헤드 적용', '높은 관용성으로 안정적인 방향성', '로프트 각도 조절 가능'] },
    { name: 'ELITE IRON SET | 엘리트 아이언 세트', price: '₩1,290,000', sub: '정교한 샷과 안정적인 컨트롤을 위한 아이언 세트', points: ['단조 페이스로 부드러운 타구감', '최적의 무게 중심 설계', '미스샷에도 안정적인 비거리'] },
    { name: 'PREMIUM GOLF BAG | 프리미엄 골프백', price: '₩249,000', sub: '가벼운 무게와 넉넉한 수납공간', points: ['경량 설계로 편안한 휴대성', '클럽과 액세서리를 위한 넉넉한 수납공간', '생활 방수 소재와 견고한 프레임 적용'] },
  ],
}
export const lineup = {
  title: '제품 라인업', caption: 'PRODUCT LINEUP',
  intro: ['드라이버부터 퍼터까지 하나의 퍼포먼스 컨셉으로 완성한 골프 클럽 시리즈입니다.', '일관된 스윙 감각과 안정적인 플레이를 경험해 보세요.'],
  head: ['제품명', '추천 플레이', '주요 특징', '가격'],
  rows: [
    ['PRO X Driver', '티샷', '최대 비거리와 높은 관용성', '₩689,000'],
    ['PRO X Fairway Wood', '롱게임', '안정적인 탄도와 긴 비거리', '₩429,000'],
    ['PRO X Hybrid', '중·장거리', '쉬운 볼 컨택과 높은 정확도', '₩359,000'],
    ['PRO X Iron Set', '아이언 샷', '정교한 컨트롤과 부드러운 타구감', '₩1,290,000'],
    ['PRO X Wedge', '쇼트게임', '뛰어난 스핀과 거리 조절', '₩199,000'],
    ['PRO X Putter', '퍼팅', '안정적인 스트로크와 방향성', '₩329,000'],
  ] as const,
}
export const detail = {
  title: '제품 상세', caption: 'PRODUCT DETAIL',
  name: ['PRO X DRIVER', '프로 엑스 드라이버'], price: '₩689,000',
  lead: '더 멀리, 더 정확하게.', body: ['비거리와 방향성을 모두 고려한 설계로 안정적인 티샷을', '완성하는 프리미엄 퍼포먼스 드라이버입니다.'],
  features: [
    ['CARBON CROWN DESIGN', '가벼운 카본 크라운을 적용하여 헤드 무게를', '최적화하고 스윙 스피드를 향상시킵니다.'],
    ['HIGH REBOUND FACE', '고반발 페이스 설계로 볼 스피드를', '높여 더 긴 비거리를 제공합니다.'],
    ['OPTIMIZED WEIGHT BALANCE', '최적의 무게 중심 설계로 미스샷에도 안정적인', '탄도와 일관된 방향성을 유지합니다.'],
  ] as const,
  specs: [['항목', '사양'], ['모델명', 'PRO X Driver'], ['헤드 크기', '460cc'], ['로프트', '9° / 10.5°'], ['라이각', '58.5°'], ['샤프트', 'Graphite'], ['플렉스', 'R / SR / S'], ['총중량', '약 305g'], ['권장 대상', '초급 ~ 상급']] as const,
}
export const styling = {
  title: '골프 스타일링', caption: 'GOLF STYLING',
  body: ['기능성과 스타일을 모두 갖춘 아이템으로 라운드마다', '완성도 높은 골프 스타일을 연출해 보세요.'],
  point: ['세련된 디자인과 퍼포먼스를', '모두 만족시키는 스타일'],
  list: ['1.  PREMIUM STAND BAG ₩249,000', '2. CLASSIC LOGO CAP ₩39,000', '3. AIR MOTION GOLF SHOES ₩229,000', '4. PERFORMANCE POLO SHIRT ₩89,000', '5. PLEATED GOLF SKIRT ₩129,000', '6. WOMEN\'S GOLF GLOVE ₩29,000'],
  badges: [[542, 135], [908, 143], [288, 477], [786, 328], [812, 540], [970, 606]] as const,
}
export const accessories = {
  title: '액세서리 컬렉션', caption: 'ACCESSORIES COLLECTION',
  lead: '필드에서의 **편안함과 완성도 높은 플레이**를 위한 필수 액세서리를 만나보세요.',
  small: [
    { name: '유틸리티 파우치', price: '₩49,000', desc: ['골프공과 티, 거리측정기 등', '작은 용품을 깔끔하게 정리할 수 있는', '다용도 파우치입니다.'], en: 'UTILITY POUCH' },
    { name: '투어 골프 장갑', price: '₩29,000', desc: ['부드러운 착용감과 안정적인 그립력을', '제공하여 정교한 스윙을 돕는', '골프 장갑입니다.'], en: 'TOUR GOLF GLOVE' },
    { name: '클래식 로고 캡', price: '₩39,000', desc: ['깔끔한 실루엣과 편안한 착용감으로', '필드와 일상에서 활용하기 좋은', '골프 모자입니다.'], en: 'CLASSIC LOGO CAP' },
  ],
  wide: [
    { name: '퍼포먼스 골프공 / 12구', price: '₩59,000', desc: ['안정적인 비거리와 섬세한 스핀 컨트롤을', '균형 있게 구현한 3피스 골프공입니다.'], en: 'PERFORMANCE GOLF BALLS' },
    { name: '마그네틱 볼 마커', price: '₩19,000', desc: ['모자나 벨트에 간편하게 부착해 필요할 때', '빠르게 사용할 수 있는 볼 마커입니다.'], en: 'MAGNETIC BALL MARKER' },
  ],
  tall: { name: '프리미엄 스탠드백', price: '₩249,000', desc: ['가벼운 무게와 넉넉한 수납공간으로', '이동과 플레이를 더욱 편리하게', '만들어주는 골프백입니다.'], en: 'PREMIUM STAND BAG' },
}
export const promo = {
  title: '스페셜 프로모션', caption: 'SPECIAL PROMOTION',
  kicker: '**SEASON** EVENT', lines: ['신제품 출시 기념', '**특별 시즌 이벤트**'], date: '2080. 3.1 - 4.30',
  pct: '30', upTo: 'UP TO', perks: ['전 품목 최대 30% 할인', '30만원 이상 구매 시 골프공 증정', '무료배송 | 멤버십 추가 적립'],
}
export const contact = {
  title: '매장 및 문의', body: ['가까운 매장에서 제품을 직접 체험하고', '전문 상담을 통해 나에게 맞는 골프 스타일을 찾아보세요.'],
  side: '2080 SEASON NEW COLLECTION',
  rows: [
    { label: 'SHOWROOM', cy: 505, values: [['미리시 미리구 미리로 00', 503], ['평일 10:30–20:00', 530], ['주말·공휴일 11:00–19:00', 556]] },
    { label: 'CONTACT', cy: 575, values: [['TEL. 00-0000-0000', 595], ['E-MAIL. kimmiri@miridih.com', 621], ['WEB. www.mirigolf.com', 647]] },
  ],
}

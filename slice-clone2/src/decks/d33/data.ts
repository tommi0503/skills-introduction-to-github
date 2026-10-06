export const season = '2080 F/W Season'
export const cover = { title: '2080 Golf Catalog', sub: 'F/W 골프시즌 신상 카탈로그' }
export const contents = {
  title: 'Contents', tag: '목차',
  cols: [
    { no: '01', en: 'COLLECTION', kr: '시즌 컬렉션', items: ['시즌 컨셉', '컬렉션 핵심 포인트', '제품 카테고리'] },
    { no: '02', en: 'PRODUCT LINEUP', kr: '제품 라인업', items: ['베스트셀러', '제품 라인업', '제품 상세', '필드 스타일링', '골프 액세서리'] },
    { no: '03', en: 'BUYING GUIDE', kr: '구매 가이드', items: ['클럽 선택 가이드', '시즌 프로모션', '매장 및 문의'] },
  ],
}
export const concept = {
  tag: '2080 F/W Season Concept', title: ['Play Beyond', 'Limits'], lead: '한계를 넘어, 최고의 플레이를 경험하다',
  body: ['이번 시즌 컬렉션은 더 긴 비거리, 더 정교한 컨트롤,', '그리고 더 가벼운 스윙을 위해 설계되었습니다.', '필드 위에서 당신의 퍼포먼스를 한 단계 끌어올려 보세요.'],
  tags: ['Sporty', 'Wearable'],
}
export const lookbook = { title: ['Season', 'Lookbook'] as const, sub: '2080 F/W 시즌 룩북', body: ['새로운 시즌, 필드 위에서', '가장 돋보이는 스타일을 만나보세요.'] }
export const features = {
  title: 'Collection Features', sub: '이번 시즌 핵심 포인트',
  body: ['이번 시즌 컬렉션은 비거리, 안정성, 경량화, 프리미엄 소재를 중심으로 설계되었습니다.', '한층 향상된 퍼포먼스와 완성도 높은 플레이를 경험해 보세요.'],
  items: [
    { en: 'Longer Distance', kr: ['비거리 향상을 위한 설계'] },
    { en: 'Precision Control', kr: ['정교한 컨트롤과 일관된 방향성'] },
    { en: 'Lightweight Design', kr: ['가벼운 무게로 편안한 스윙'] },
    { en: 'Premium Materials', kr: ['프리미엄 소재를 적용한 높은', '내구성과 타구감'] },
  ],
}
export const categories = {
  title: ['Product', 'Categories'] as const, sub: '제품 카테고리', body: ['드라이버부터 액세서리까지, 필드를 완성하는', '다양한 골프 아이템을 한눈에 만나보세요.'],
  items: [['Driver', '드라이버', '긴 비거리와 안정적인 티샷'], ['Iron', '아이언', '정확한 거리와 방향성'], ['Putter', '퍼터', '안정적인 퍼팅 밸런스'], ['Golf Ball', '골프공', '플레이 스타일에 맞는 성능'], ['Apparel', '골프웨어', '기능성과 스타일을 동시에'], ['Accessories', '액세서리', '라운드를 완성하는 필수 아이템']] as const,
}
export const section = {
  no: '02', title: 'Procuct Lineup', sub: '제품 라인업',
  items: [['07', 'Product Lineup', '제품 라인업'], ['08', 'Best Sellers', '베스트셀러'], ['09', 'Product Detail', '제품 상세'], ['10', 'Golf Styling', '필드 스타일링'], ['11', 'Accessories Collection', '골프 액세서리']] as const,
}
export const best = {
  title: ['Best', 'Sellers'] as const, sub: '베스트셀러', body: ['많은 골퍼들에게 사랑받는', '대표 인기 제품을 소개합니다.'],
  items: [
    { name: 'PRO X Driver | 프로 X 드라이버', desc: ['더 멀리, 더 정확한 티샷을 위한 드라이버'], price: '₩689,000', points: [['카본 복합 소재 헤드 적용'], ['높은 관용성으로', '안정적인 방향성'], ['로프트 각도 조절 가능']] },
    { name: 'Elite Iron Set | 엘리트 아이언 세트', desc: ['정교한 샷과 안정적인 컨트롤을 위한', '아이언 세트'], price: '₩1,290,000', points: [['단조 페이스로', '부드러운 타구감'], ['최적의 무게 중심 설계'], ['미스샷에도 안정적인 비거리']] },
    { name: 'Premium Golf Bag | 프리미엄 골프백', desc: ['가벼운 무게와 넉넉한 수납공간'], price: '₩249,000', points: [['경량 설계로 편안한 휴대성'], ['클럽과 액세서리를 위한', '넉넉한 수납공간'], ['생활 방수 소재와', '견고한 프레임 적용']] },
  ],
}
export const lineup = {
  title: ['Product', 'Lineup'] as const, sub: '제품 라인업', head: 'PRO X SERIES',
  body: ['드라이버부터 퍼터까지 하나의 퍼포먼스', '컨셉으로 완성한 골프 클럽 시리즈입니다.', '일관된 스윙 감각과 안정적인 플레이를', '경험해 보세요.'],
  cols: ['제품명', '추천 플레이', '주요 특징', '가격'],
  rows: [
    [['PRO X Driver'], '티샷', '최대 비거리와 높은 관용성', '₩689,000'],
    [['PRO X Fairway', 'Wood'], '롱게임', '안정적인 탄도와 긴 비거리', '₩429,000'],
    [['PRO X Hybrid'], '중·장거리', '쉬운 볼 컨택과 높은 정확도', '₩359,000'],
    [['PRO X Iron Set'], '아이언 샷', '정교한 컨트롤과 부드러운 타구감', '₩1,290,000'],
    [['PRO X Wedge'], '쇼트게임', '뛰어난 스핀과 거리 조절', '₩199,000'],
    [['PRO X Putter'], '퍼팅', '안정적인 스트로크와 방향성', '₩329,000'],
  ] as const,
}
export const detail = {
  title: ['Product', 'Detail'] as const, sub: '제품 상세', band: 'PRO X DRIVER | 프로 엑스 드라이버',
  body: ['더 멀리, 더 정확하게. 비거리와 방향성을 모두 고려한 설계로', '안정적인 티샷을 완성하는 프리미엄 퍼포먼스 드라이버입니다.'],
  priceLabel: 'PRICE | 소비자가', price: '₩689,000', key: 'KEY FEATURES | 핵심 특징',
  features: [
    ['Carbon Crown Design', '가벼운 카본 크라운을 적용하여', '헤드 무게를 최적화하고', '스윙 스피드를 향상시킵니다.'],
    ['High Rebound Face', '고반발 페이스 설계로', '볼 스피드를 높여', '더 긴 비거리를 제공합니다.'],
    ['Optimized Weight Balance', '최적의 무게 중심 설계로', '미스샷에도 안정적인 탄도와', '일관된 방향성을 유지합니다.'],
  ] as const,
  specs: [[['모델명', 'PRO X Driver'], ['헤드 크기', '460cc'], ['로프트', '9° / 10.5°'], ['라이각', '58.5°']], [['샤프트', 'Graphite'], ['플렉스', 'R / SR / S'], ['총중량', '약 305g'], ['권장 대상', '초급 ~ 상급']]] as const,
}
export const styling = {
  title: ['Golf', 'Styling'] as const, sub: '골프 스타일링', body: ['기능성과 스타일을 모두 갖춘 아이템으로 라운드마다', '완성도 높은 골프 스타일을 연출해 보세요.'],
  point: { head: 'Styling Point', lines: ['세련된 디자인과 퍼포먼스를', '모두 만족시키는 스타일'] },
  tip: { head: 'Styling Tip', lines: ['- 상·하의는 톤을 맞춰 깔끔하게 연출하기', '- 모자와 벨트 컬러를 통일해 완성도 높이기', '- 계절에 맞는 기능성 소재 선택하기'] },
  items: [['01', '상의', ['Performance', 'Polo Shirt'], '₩89,000'], ['02', '하의', ['Pleated', 'Golf Skirt'], '₩129,000'], ['03', '모자', ['Classic', 'Logo Cap'], '₩39,000'], ['04', '장갑', ["Women's", 'Golf Glove'], '₩29,000'], ['05', '골프화', ['Air Motion', 'Golf Shoes'], '₩229,000'], ['06', '골프백', ['Premium', 'Stand Bag'], '₩249,000']] as const,
}
export const accessories = {
  title: ['Accessories', 'Collection'] as const, sub: '액세서리 컬렉션', body: ['필드에서의 편안함과 완성도 높은 플레이를 위한', '필수 액세서리를 만나보세요.'],
  items: [
    ['01', ['Premium Stand Bag', '| 프리미엄 스탠드백'], ['가벼운 무게와 넉넉한 수납공간', '으로 이동과 플레이를 더욱 편리', '하게 만들어주는 골프백입니다.'], '₩249,000'],
    ['02', ['Classic Logo Cap', '| 클래식 로고 캡'], ['깔끔한 실루엣과 편안한 착용감', '으로 필드와 일상에서 활용하기', '좋은 골프 모자입니다.'], '₩39,000'],
    ['03', ['Tour Golf Glove', '| 투어 골프 장갑'], ['부드러운 착용감과 안정적인', '그립력을 제공하여 정교한', '스윙을 돕는 골프 장갑입니다.'], '₩29,000'],
    ['04', ['Classic Golf Balls', '| 클래식 골프공'], ['안정적인 비거리와 섬세한', '스핀 컨트롤을 균형 있게 구현한', '3피스 골프공입니다.'], '₩59,000 / 12구'],
    ['05', ['Magnetic Marker', '| 마그네틱 볼 마커'], ['모자나 벨트에 간편하게 부착해', '필요할 때 빠르게 사용할 수 있는', '볼 마커입니다.'], '₩19,000'],
    ['6', ['Utility Pouch', '| 유틸리티 파우치'], ['골프공과 티, 거리측정기 등', '작은 용품을 깔끔하게 정리할 수', '있는 다용도 파우치입니다.'], '₩49,000'],
  ] as const,
}
export const promo = {
  title: ['Special', 'Promotion'] as const, sub: '스페셜 프로모션', event: ['SEASON EVENT', '신제품 출시 기념 특별 시즌 이벤트'],
  kicker: '전 품목 최대', pct: '30', unit: ['%', '할인'], perks: ['30만원 이상 구매 시 골프공 증정', '전 품목 무료배송', '멤버십 추가 적립'], period: '2080.03.01 - 2080.04.30',
}

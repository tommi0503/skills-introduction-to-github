const desc = '이곳에 타이틀에 관한 간략한 설명을 적어주세요. 사용된 폰트는 에스코어 드림 3입니다.'
export const cover = { title: ['2039', 'INVESTMENT', 'PROPOSALS'], sub: '비즈골프클럽 투자제안서' }
export const overview = {
  title: '사업개요', en: 'Business Overview',
  wide: [['대지위치', '주소를 입력해주세요. 이곳을 더블클릭하여 내용을 수정할 수 있습니다. 폰트는 에스코어 드림 3 입니다.'], ['용도', '용도를 입력해주세요. 이곳을 더블클릭하여 내용을 수정할 수 있습니다. 폰트는 에스코어 드림 3 입니다.']],
  pairs: [['대지면적', '000,000㎡', '건축면적', '000.00㎡'], ['전용면적', '00,000㎡', '건폐율', '00% 이하'], ['공용면적', '00,000㎡', '용적율', '00% 이하'], ['필지구성', '총000필지', '높이', '00 m (예정)']],
}
const chDesc = '해당 챕터에 대한 간단한 설명을 2-3줄 내외로 써주세요.\n사용된 폰트는 에스코어 드림 3 입니다.'
export const contents = {
  title: 'Contents', sub: '비즈골프클럽 투자제안서',
  items: ['사업개요', '시장분석', '마케팅 전략', '예산안과 기대효과'].map((name, i) => ({ no: `0${i + 1}.`, name, desc: chDesc })),
}
export const market = {
  title: '시장분석', en: 'Market Analysis', desc,
  charts: [
    { max: 150, step: 50, values: [105, 107, 122, 122, 125], legend: '필드 인구이용변화' },
    { max: 200, step: 50, values: [60, 94, 127, 136, 165], legend: '스크린 인구이용변화' },
    { max: 300, step: 100, values: [135, 170, 205, 220, 250], legend: '골프 인구 증가 추세' },
  ],
  years: ['2039', '2040', '2041', '2042', '2043'],
  unit: '(만명)',
  note: '현재 골프 인구 증가 추세 대비 스크린 골프 인구 증가세로 국내 골프 경험 인구 2039년 대비 약 2배 증가',
}
const item = '해당 항목과 관련 있는 내용을\n이곳에 간략하게 입력해주세\n요. 내용은 다섯줄정도 입력해\n주세요. 이 폰트는 에스코어 드\n림 3 입니다.'
export const marketing = {
  title: '마케팅 전략', en: 'Marketing Strategy', desc,
  steps: ['주요 고객\n분석', '회원제\n모집', '직원\n교육', '홍보\n전략'].map((label) => ({ label, text: item })),
}
export const values = {
  title: '핵심가치', en: 'Core Values',
  items: [
    { title: '01_최상의 라운딩 GOLF ZONE', text: '골프를 통해 자연과 조화로운 레저문화를 선도하는\n비즈골프에서 최상의 라운딩을 경험하실 수 있습니다.' },
    { title: '02_회원전용공간 VIP LOUNGE', text: 'VIP LOUNGE 가 제공하는 고품격 서비스는\n고객의 삶을 풍요롭고, 여유롭게 만들어 드립니다.' },
    { title: '03_골프와 문화가 공존하는 EVENT HALL', text: '월별, 주별 다채로운 테마 이벤트가 펼쳐지는 곳입니다.\n(골프 클리닉,문화강연,고객초청 등)' },
  ],
}
export const finance = {
  title: '재무현황', en: 'Financial Status', desc, sub: '대차대조표', unit: '(단위 : 천원)',
  head: ['과목', '금액'],
  assets: { group: '자산', rows: [['유동자산', '2,959'], ['투자와 기타자산', '18,221'], ['고정자산', '14,000'], ['무형자산', '12,131'], ['기타', '']], total: ['자산총계', '47,311'] },
  debts: [
    { group: '부채', rows: [['유동부채', '1,931'], ['고정부채', '3,400'], ['기타', '']] },
    { group: '자본', rows: [['자본금', '3,813'], ['이익잉여금', '17,321'], ['기타', '']] },
  ],
  debtTotal: ['부채,자본총계', '26,465'],
}
export const income = {
  title: '추정 손익계산서', en: 'Estimated Income Statement', desc, unit: '(단위 : 백만원)',
  bars: [['매출액', 10000, 8000], ['매출원가', 8000, 7200], ['매출총이익', 2000, 800], ['판매관리비', 1200, 900]] as [string, number, number][],
  ticks: [10000, 8000, 6000, 4000, 2000, 0],
  years: ['2039', '2040'],
  rows: [['매출액', '10,000', '8,000'], ['매출원가', '8,000', '7,200'], ['매출총이익', '2,000', '800'], ['판매관리비', '1,200', '900'], ['영업이익(손실)', '800', '(100)'], ['영업외수익', '40', '30'], ['영업외비용', '200', '180'], ['당기순이익', '500', '250']],
}
const cell = '해당 항목과 관련 있는 내용을\n이곳에 간략하게 입력해주세요.'
export const club = {
  title: ['BIZ LAKESIDE', 'GOLF CLUB'], lead: '골프를 통해 자연과 조화로운\n레저문화를 선도하는 기업',
  body: '이곳에 서브 텍스트를 입력해 주세요.\n컨텐츠에 맞는 내용을 써주세요.\n회사의 비전에 관한 내용을\n요약하여 정리해 주시면 좋습니다.',
  cells: [{ title: '최상의 라운딩', text: cell }, { title: 'VIP LOUNGE', text: cell }, { title: 'EVENT HALL', text: cell }],
}
export const budget = {
  title: '예산안과 기대효과', en: 'Budget& Benefit', caption: '※ 사업별 예산 그래프',
  donuts: [60, 50, 70, 70], legend: ['항목1', '항목2'],
  money: '000,000,000',
}
const pdesc = '해당 항목과 관련 있는 내용을 이곳에\n간략하게 입력해주세요. 내용은 다섯\n줄정도 입력해주세요. 이 폰트는 에스\n코어 드림 3 입니다.'
export const partners = {
  title: '제휴현황', en: 'Partnership', desc,
  items: ['미리건설 - 부동산 개발', '비즈모아 - 멤버쉽 관리', '비즈투어 - 골프여행/레저', 'Oz golf - 골프용품 런칭'].map((name) => ({ name, text: pdesc })),
}
export const thanks = { title: 'Thank you.', company: '(주)비즈골프클럽', address: '서울 구로구 디지털로12길 12 미리빌딩 305호', copy: '©MIRIDIH ALL RIGHTS RESERVED.' }

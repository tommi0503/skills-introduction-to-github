import type { LucideIcon } from 'lucide-react'
import { Heart, LayoutGrid, Menu, Store, UserRound } from 'lucide-react'

export const homeTabs = [
  { key: 'deal', label: '1만원특가', accent: true },
  { key: 'trend', label: '트렌드', active: true },
  { key: 'rank', label: '랭킹' },
  { key: 'brand', label: '브랜드' },
  { key: 'beauty', label: '뷰티' },
  { key: 'life', label: '라이프' },
]

export const promo = { title: '쇼핑몰 1만원 특가', sub: '최대 98% 할인 + 30% 쿠폰', cta: '쿠폰받기' }
export const hero = {
  tag: '내가 좋아할 만한 스토어',
  title: '미리 준비하는 겨울 코디\n미쏘 24시간 특가',
  sub: '최대 67% 할인 + 15% 쿠폰',
  page: 5,
  total: 27,
}
export const shortcuts = [
  { key: 'first', label: '첫구매혜택' },
  { key: '24h', label: '24H특가' },
  { key: 'big', label: '빅사이즈', dot: true },
  { key: 'beauty', label: '이미용가전' },
  { key: 'express', label: '직진배송' },
]

export interface NavTab {
  key: string
  label: string
  icon?: LucideIcon
  dot?: boolean
}
export const navTabs: NavTab[] = [
  { key: 'home', label: '홈' },
  { key: 'store', label: '스토어', icon: Store },
  { key: 'category', label: '카테고리', icon: Menu },
  { key: 'like', label: '찜', icon: Heart },
  { key: 'my', label: '마이페이지', icon: UserRound, dot: true },
]

export const suggested = ['스웨이드자켓', '트위드자켓', '원피스', '셔츠', '오프숄더']
export const brands = ['토리든', '에이딕트', '스킨푸드', '웨이크메이크', '힌스']
export const ages = ['전체', '10대', '20대 초반', '20대 중반', '20대 후반', '30대']
export const activeAge = '20대 중반'

export type Trend = 'up' | 'down' | 'same'
export const rising: { rank: number; keyword: string; trend: Trend }[] = [
  { rank: 1, keyword: '스웨이드치마', trend: 'up' },
  { rank: 2, keyword: '스킨푸드 패드', trend: 'down' },
  { rank: 3, keyword: '토리든', trend: 'same' },
  { rank: 4, keyword: '웨이크메이크', trend: 'up' },
  { rank: 5, keyword: '블러셔', trend: 'up' },
  { rank: 6, keyword: '스킨푸드마스크', trend: 'down' },
]

export interface Tag {
  label: string
  tone: 'pink' | 'grey'
}
export interface Product {
  key: string
  store: string
  crown?: boolean
  ad?: boolean
  name: string
  discount?: string
  price: string
  liked?: boolean
  express?: boolean
  tags?: Tag[]
  colors?: string[]
  moreColors?: number
  meta?: string
}

export const recent: Product[] = [
  { key: 'r1', store: '리언스', name: '업민 시스루 매쉬 티셔츠 긴팔', price: '38,000', tags: [{ label: '최저가도전', tone: 'pink' }] },
  { key: 'r2', store: '리얼코코', name: '네로우 셔링 나시 티셔츠', discount: '32%', price: '26,400', liked: true, tags: [{ label: '무료배송', tone: 'grey' }] },
  { key: 'r3', store: '리언스', name: '원숄더 시스루 피임 니트', price: '34,000', liked: true, tags: [{ label: '최저가도전', tone: 'pink' }] },
  { key: 'r4', store: '진이어', name: '럭키비키 니트', discount: '50%', price: '19,800' },
]

export const results: Product[] = [
  {
    key: 'p1', store: '데일리쥬', crown: true, ad: true, name: '로가튼 언발 오프숄더 맨투맨', discount: '20%', price: '25,600',
    tags: [{ label: '첫구매쿠폰', tone: 'pink' }, { label: '무료배송', tone: 'grey' }],
    colors: ['#111', '#4b6b3c', '#a3a3a3', '#f4f4f4'], meta: '1.6천 명 보는중',
  },
  {
    key: 'p2', store: '데일리쥬', crown: true, name: '[단독] [8천장판매/MADE] 수피마 오프숄더', discount: '74%', price: '8,520', express: true,
    tags: [{ label: '첫구매가', tone: 'pink' }, { label: '무료배송', tone: 'grey' }],
    colors: ['#111', '#1f3a8a', '#2f4bb0', '#4b5a3c', '#8fb6f0'], moreColors: 1, meta: '★ 4.8(1,698) · 1.5만 명 보는중',
  },
]

export const similar: Product[] = [
  { key: 's1', store: '보블리에', name: '쿨 나일론 랩 리본 롱 스커트', price: '36,000', tags: [{ label: '무료배송', tone: 'grey' }] },
  { key: 's2', store: '에이퍼플', crown: true, name: '랩 스커드 튤립 허리 밴딩', discount: '20%', price: '25,200', tags: [{ label: '첫구매쿠폰', tone: 'pink' }, { label: '무료배송', tone: 'grey' }] },
  { key: 's3', store: '스위트글램', name: '클린 큐빅 롱 스커드', discount: '8%', price: '92,300', tags: [{ label: '첫구매쿠폰', tone: 'pink' }, { label: '무료배송', tone: 'grey' }] },
]

export const resultsHeader = { query: '오프숄더 맨투맨', count: '3,131', sort: '직잭추천순', filters: ['직진배송', '빠른출발', '색상', '카테고리', '가격'], dropdown: ['색상', '카테고리', '가격'] }
export const banner = { title: '이 배너가 보인다면\n인기 상품 100원', sub: '첫 구매 혜택!' }
export const gridIcon = LayoutGrid

/** Content for 나무섬 전망대 (07). */
import type { CSSProperties } from 'react'

export interface Fee {
  label: string
  price: string
}

export interface ArtBox {
  label: string
  style: CSSProperties
}

export const admission = {
  heading: '입장료',
  fees: [
    { label: '유아', price: '3000원' },
    { label: '청소년', price: '6000원' },
    { label: '성인', price: '1,2000원' },
  ] satisfies Fee[],
  note: '(전화 및 온라인 사전 예약시 2000원 할인)',
}

export const greeting = {
  heading: '인사말',
  paragraphs: [
    ['나무섬 전망대에 오신 여러분 환영합니다.', '높은 곳에서 자연의 아름다움과', '섬의 풍경을 만끽해 보세요!'],
    ['감사합니다.'],
    ['나무섬 전망대'],
  ],
}

export const directions = {
  heading: '오시는 길',
  mapLabels: [
    { lines: ['나무섬 전망대'], x: 150, y: 260 },
    { lines: ['나무섬역', '2번출구'], x: 76, y: 349 },
  ],
  address: '강원도 강릉시 주문진읍 해안로 2733-9',
  transit: ['지하철 나무섬역 2번 출구 앞', '무료 셔틀버스 운영'],
}

export const reservation = {
  heading: '예약 문의',
  contacts: ['03-987-1533', 'www.umchungjoeun.kr'],
  note: ['10인 이상 방문의 경우, 사전 예약 필수!', '전화 또는 웹사이트로 예약 부탁드립니다.'],
}

export const cover = {
  tagline: '하늘과 땅을 한 눈에',
  /** Vertical title columns, read right column first (나무섬 · 전망대). */
  columns: { light: ['전', '망', '대'], dark: ['나', '무', '섬'] },
  hours: ['매주 월요일 정기휴관', '10:00 - 17:00', '(입장마감 16:00)'],
  art: [
    { label: 'island illustration', style: { left: 42, top: 290, width: 438, height: 412, clipPath: 'polygon(4% 36%, 22% 32%, 50% 14%, 72% 2%, 100% 0, 100% 100%, 60% 96%, 26% 86%, 8% 70%, 1% 50%)' } },
    { label: 'cloud', style: { left: 416, top: 50, width: 64, height: 44, borderRadius: '22px 0 0 22px' } },
    { label: 'cloud', style: { left: 170, top: 180, width: 70, height: 36, borderRadius: 18 } },
    { label: 'cloud', style: { left: 368, top: 232, width: 70, height: 36, borderRadius: 18 } },
    { label: 'cloud', style: { left: 40, top: 338, width: 86, height: 42, borderRadius: 21 } },
  ] satisfies ArtBox[],
}

export const trees: ArtBox = {
  label: 'trees and pond illustration',
  style: {
    left: 0,
    top: 738,
    width: 480,
    height: 280,
    clipPath: 'polygon(0 30%, 20% 26%, 38% 18%, 58% 2%, 100% 0, 100% 100%, 0 100%)',
  },
}

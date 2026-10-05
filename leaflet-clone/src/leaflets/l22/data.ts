import type { BlobShape } from '../shared-2223/components/Blob'

export interface InfoRow {
  label: string
  lines: string[]
}

export const introPanel = {
  heading: ['초록빛 자연 속으로', '떠나볼까요?'],
  art: [
    { id: 'photo', x: 55, y: 198, width: 366, height: 372, label: 'children harvesting radish (circular photo)' },
    { id: 'squiggle', x: 50, y: 230, width: 142, height: 46, radius: '24px', rotate: -6, label: 'orange squiggle' },
    { id: 'pink', x: 330, y: 456, width: 92, height: 72, radius: '48% 52% 40% 60%', rotate: -12, label: 'pink blob' },
  ] satisfies BlobShape[],
  rows: [
    { label: '체험 일시', lines: ['2046년 7월 20일 ~ 8월 14일'] },
    { label: '체험 장소', lines: ['행복 농촌 체험 마을'] },
    { label: '참가 인원', lines: ['회차당 선착순 40명'] },
    { label: '참가비', lines: ['성인 : 1인당 35,000원', '어린이 : 1인당 25,000원'] },
    { label: '참가 혜택', lines: ['제철 재료로 만든 식사 제공', '직접 수확한 농산물 제공', '체험 프로그램 재료비 포함'] },
  ] satisfies InfoRow[],
}

export interface ApplyStep {
  lines: string[]
}

export interface ContactLine {
  label: string
  value: string
}

export const applyPanel = {
  heading: '신청 방법',
  qrCta: '체험 신청하러 가기',
  steps: [
    { lines: ['QR코드 스캔 또는 홈페이지 접속'] },
    { lines: ['참가 신청서 작성 및 제출'] },
    { lines: ['참가비 입금', '(00은행 123-4567-8901)'] },
    { lines: ['예약 확정 문자 수신'] },
  ] satisfies ApplyStep[],
  periodHeading: '신청 기간',
  period: '2046.6.4(월) 오전 10시 ~ 7.4(금) 오후 6시',
  contactHeading: '문의처',
  contacts: [
    { label: '대표전화', value: '02-1234-5678' },
    { label: '상담시간', value: '평일 오전 10시 ~ 오후 6시' },
    { label: 'SNS', value: '@dreamcanvakorea' },
  ] satisfies ContactLine[],
}

export const coverPanel = {
  kicker: '2046 행복 농촌 체험 마을',
  title: '농촌체험',
  subtitle: '프로그램',
  dates: '2046. 7. 20 ~ 8. 14',
  art: [
    { id: 'pepper', x: 300, y: 385, width: 175, height: 300, radius: '50% 42% 36% 50% / 34% 34% 50% 50%', label: 'green pepper' },
    { id: 'stem', x: 340, y: 325, width: 50, height: 105, radius: '40% 60% 30% 40%', rotate: 18, label: 'pepper stem' },
    { id: 'photo', x: 50, y: 422, width: 392, height: 435, label: 'children holding radishes (circular photo)' },
    { id: 'berry1', x: 120, y: 383, width: 60, height: 60, label: 'blue berry' },
    { id: 'berry2', x: 25, y: 428, width: 55, height: 60, label: 'blue berry' },
    { id: 'berry3', x: 90, y: 483, width: 52, height: 58, label: 'blue berry' },
    { id: 'leaf', x: 48, y: 667, width: 112, height: 212, radius: '50% 50% 40% 60% / 60% 60% 40% 40%', rotate: -18, label: 'leaf' },
    { id: 'tomato', x: 303, y: 740, width: 172, height: 158, radius: '50% 50% 45% 45%', label: 'pink tomato' },
  ] satisfies BlobShape[],
}

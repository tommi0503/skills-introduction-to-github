import type { DisplayLineSpec } from '../shared-1718/components/DisplayLine'
import { festival, type LabeledValue } from '../shared-1718/data'

export interface TimetableEntry {
  title: string
  lines: string[]
}

export const invitation = {
  arcTagline: festival.arcTagline,
  message: [['도서관에서 보내는', '특별한 하루,'], ['책과 사람이 만나는', '즐거운 축제에 초대합니다.']],
  footer: [{ label: '일시', value: festival.date }] as LabeledValue[],
}

export const timetable = {
  title: '프로그램 타임테이블 및 위치',
  entries: [
    { title: '개막식 및 북마켓 오픈', lines: ['10:00 - 17:00 도서관 앞 광장 부스존', '대상: 전 연령'] },
    { title: '어린이 그림책 놀이터', lines: ['11:00 - 12:30 광장 내 어린이 체험존', '대상: 유아 및 초등 저학년 (보호자 동반)'] },
    { title: '작가와의 만남', lines: ['13:00 - 14:00 도서관 다목적홀 (실내)', '대상: 성인 및 청소년 독자'] },
    { title: '낭독 공연', lines: ['15:00 – 15:40 광장 중앙 무대', '대상: 전 연령'] },
    { title: '시민 참여 북토크', lines: ['16:00 - 16:30 도서관 세미나실 (실내)', '대상: 성인 및 청소년'] },
    { title: '경품 추첨 및 마무리 인사', lines: ['16:30 – 17:00 광장 중앙 무대', '대상: 전체 참가자'] },
  ] as TimetableEntry[],
  website: festival.website,
}

export const cover = {
  title: [
    { text: festival.name[0], x: 103, y: 60, size: 119, scaleY: 1.29 },
    { text: festival.name[1], x: 74, y: 202, size: 137, scaleY: 1.03 },
    { text: festival.name[2], x: 77, y: 328, size: 131, scaleY: 1.1 },
  ] as DisplayLineSpec[],
  tagline: festival.tagline,
  date: festival.date,
  footer: [
    { label: '장소', value: festival.place },
    { label: '문의', value: festival.phoneDots },
  ] as LabeledValue[],
}

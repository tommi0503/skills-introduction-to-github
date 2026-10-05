import { CalendarDays, Laptop, Phone, Smartphone, type LucideIcon } from 'lucide-react'
import type { TableColumn, TableRow } from './components/NavyTable'
import type { PillInfo } from './components/InfoPillList'
import type { FooterText } from '../shared-2425/components/ContactFooter'

export interface TableSection {
  title: string
  columns: TableColumn[]
  rows: TableRow[]
}

export const childClass: TableSection = {
  title: '어린이 배움 특강',
  columns: [
    { key: 'who', header: '대상', width: 66 },
    { key: 'name', header: '프로그램명', width: 99 },
    { key: 'desc', header: '수업 내용', width: 230 },
  ],
  rows: [
    { who: ['유아', '6~7세'], name: ['그림책 속 자연', '탐험대'], desc: ['그림책을 읽고 나뭇잎, 동물, 계절을', '주제로 놀이와 만들기를 진행합니다.'] },
    { who: ['초등', '1~2학년'], name: ['말랑말랑 이야기', '공작소'], desc: ['짧은 이야기를 만들고 등장인물', '카드와 미니북으로 표현합니다.'] },
    { who: ['초등', '1~3학년'], name: ['생활 속 과학', '발견단'], desc: ['빛, 소리, 공기 등 주변에서 만나는', '과학 원리를 간단한 실험으로 배웁니다.'] },
  ],
}

export const digitalClass: TableSection = {
  title: '창의/디지털 특강',
  columns: [
    { key: 'who', header: '대상', width: 71 },
    { key: 'name', header: '프로그램명', width: 123 },
    { key: 'desc', header: '수업 내용', width: 206 },
  ],
  rows: [
    { who: ['초등', '3~4학년'], name: ['나만의 동네 지도', '만들기'], desc: ['우리 동네의 장소와 이야기를', '관찰하고', '일러스트 지도로 완성합니다.'] },
    { who: ['초등', '4~6학년'], name: ['어린이 콘텐츠', '스튜디오'], desc: ['사진 구성, 제목 만들기,', '카드뉴스 기초를 배우며', '디지털 콘텐츠를 제작합니다.'] },
  ],
}

export const readingProject: TableSection = {
  title: '방학 독서 프로젝트',
  columns: [
    { key: 'item', header: '항목', width: 120 },
    { key: 'detail', header: '내용', width: 289 },
  ],
  rows: [
    { item: ['대상'], detail: ['초등 3~5학년'] },
    { item: ['프로그램명'], detail: ['한 권을 깊이 읽는 여름'] },
    { item: ['주요 활동'], detail: ['함께 읽기, 질문 카드 만들기, 북토크'] },
    { item: ['운영 방식'], detail: ['3회 연속 참여형 수업'] },
    { item: ['준비물'], detail: ['필기도구, 개인 물병'] },
  ],
}

export const academy = {
  title: { accent: '그림책 마음 여행', rest: ' 아카데미' },
  intro: ['그림책을 함께 읽고 이야기 속 감정과 생각을', '자유롭게 나누는 참여형 독서 프로그램입니다.'],
  facts: [
    { label: '대상', value: '초등 1~3학년' },
    { label: '일정', value: '7.23.(수)~8.13.(수)' },
    { label: '시간', value: '10:30~12:00' },
    { label: '장소', value: '도서관 프로그램실' },
  ] satisfies PillInfo[],
  apply: {
    title: '홈페이지 온라인 신청 · 선착순 접수',
    note: '프로그램 일정 및 내용은 도서관 사정에 따라 변경될 수 있습니다.',
    contact: '문의 : 02-1234-5678 / 평일 09:00~18:00',
  },
}

export interface OperationItem {
  icon: LucideIcon
  title: string
  detail: string
}

export const operations: OperationItem[] = [
  { icon: CalendarDays, title: '운영 기간', detail: '7.25.(금) ~ 8.16.(토) / 프로그램별 일정 상이' },
  { icon: Laptop, title: '운영 장소', detail: '도서관 프로그램실 / 강좌별 세부 장소 별도 안내' },
  { icon: Phone, title: '접수 일정', detail: '모집 시작 후 선착순 마감 / 조기 마감될 수 있음' },
  { icon: Smartphone, title: '문의', detail: '02-1234-5678 / 평일 09:00~18:00' },
]

export const common = {
  title: '공통 안내',
  items: [
    { label: '운영대상', value: '유아 6~7세, 초등학생' },
    { label: '운영장소', value: '우리동네 도서관 프로그램실' },
    { label: '접수방법', value: '홈페이지 온라인 신청' },
    { label: '웹사이트', value: 'http://www.umchungjoeun.kr' },
    { label: '이메일', value: 'dream@canvakorea.co.kr' },
    { label: '신청방식', value: '프로그램별 선착순 접수' },
    { label: '문의', value: '02-1234-5678' },
  ] satisfies PillInfo[],
}

export const footer: FooterText[] = [
  { text: '02-1234-5678', x: 52 },
  { text: 'dream@canvakorea.co.kr', x: 196 },
]

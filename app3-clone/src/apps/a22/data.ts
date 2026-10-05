import type { WheelColumn } from './components/WheelPicker'

const range = (from: number, to: number, pad = false) =>
  Array.from({ length: to - from + 1 }, (_, i) => String(from + i).padStart(pad ? 2 : 1, '0'))

export interface DayCard {
  weekday: string
  day: number
}

export const workout = {
  title: ['5-Min Bodyweight Burn:', 'Your Second Strength', 'Class'],
  coach: 'With Alex Piccirilli',
  sheetTitle: 'Select a Date & Time',
  sheetBody: "We'll send reminders before your workout so you can prepare.",
  days: [
    { weekday: 'Wed', day: 15 },
    { weekday: 'Thu', day: 16 },
    { weekday: 'Fri', day: 17 },
    { weekday: 'Sat', day: 18 },
    { weekday: 'Sun', day: 19 },
  ] as DayCard[],
  selectedDay: 1,
  picker: [
    { items: range(1, 12), selected: 7, x: 123 },
    { items: ['58', '59', ...range(0, 59, true)], selected: 2, x: 190 },
    { items: ['AM', 'PM'], selected: 0, x: 255 },
  ] as WheelColumn[],
  cancel: 'Cancel',
  confirm: 'Confirm',
}

export interface ClockLabel {
  hour: number
  text: string
  suffix?: string
}

export const sleep = {
  cancel: 'Cancel',
  add: 'Add',
  title: ['Set Your', 'First Schedule'],
  daysTitle: 'Days Active',
  days: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
  bedTitle: 'Bedtime and Wake Up',
  bedtime: { label: 'BEDTIME', value: '10:00 PM', hour: 22 },
  wakeup: { label: 'WAKE UP', value: '6:30 AM', hour: 6.5 },
  labels: [
    { hour: 0, text: '12', suffix: 'AM' },
    { hour: 2, text: '2' },
    { hour: 4, text: '4' },
    { hour: 6, text: '6', suffix: 'AM' },
    { hour: 8, text: '8' },
    { hour: 10, text: '10' },
    { hour: 12, text: '12', suffix: 'PM' },
    { hour: 14, text: '2' },
    { hour: 16, text: '4' },
    { hour: 18, text: '6', suffix: 'PM' },
    { hour: 20, text: '8' },
    { hour: 22, text: '10' },
  ] as ClockLabel[],
}

export const live = {
  title: 'Live Video',
  cancel: 'Cancel',
  rows: ['Test live', 'Start time'],
  note: 'Your scheduled live video will appear on your profile.',
  sheetTitle: 'Start time',
  sheetBody: ['Choose a time between 3 months from today and', '1 hour from now.'],
  picker: [
    {
      items: ['Sat Aug 19', 'Sun Aug 20', 'Mon Aug 21', 'Tue Aug 22', 'Wed Aug 23', 'Today', 'Fri Aug 25', 'Sat Aug 26', 'Sun Aug 27', 'Mon Aug 28'],
      selected: 5,
      x: 175,
      align: 'right',
    },
    { items: range(2, 11), selected: 5, x: 207 },
    { items: ['35', '40', '45', '50', '55', '00', '05', '10', '15', '20'], selected: 5, x: 264 },
    { items: ['AM', 'PM'], selected: 1, x: 322 },
  ] as WheelColumn[],
  done: 'Done',
}

import type { KeyboardLayout, KeyRow, KeySpec } from './components/Keyboard'
import type { WheelColumn } from './components/WheelPicker'

/* ---------- keyboards ---------- */
const letters = (s: string, upper: boolean): KeySpec[] => [...s].map((c) => ({ label: upper ? c.toUpperCase() : c, w: 32 }))

function letterRows(upper: boolean): KeyRow[] {
  const mid = letters('zxcvbnm', upper)
  mid[0] = { ...mid[0], gap: 13 }
  return [
    { left: 6, keys: letters('qwertyuiop', upper) },
    { left: 25, keys: letters('asdfghjkl', upper) },
    { left: 6, keys: [{ icon: upper ? 'shiftOn' : 'shift', w: 44 }, ...mid, { icon: 'delete', w: 45, gap: 13 }] },
  ]
}

const KB_GEOMETRY = { rowTop: [24, 78, 131, 185], keyHeight: 42, gap: 6 }

export const keyboards: Record<'upper' | 'lower', KeyboardLayout> = {
  upper: {
    ...KB_GEOMETRY,
    bottomLeft: 'globe',
    rows: [
      ...letterRows(true),
      {
        left: 6,
        keys: [
          { label: '123', w: 42, small: true },
          { icon: 'emoji', w: 41 },
          { label: '', w: 184, gap: 7 },
          { icon: 'return', w: 89, gap: 7 },
        ],
      },
    ],
  },
  lower: {
    ...KB_GEOMETRY,
    bottomLeft: 'emoji',
    rows: [
      ...letterRows(false),
      {
        left: 6,
        keys: [
          { label: '123', w: 89, small: true },
          { label: '', w: 184, gap: 7 },
          { icon: 'return', w: 89, gap: 7 },
        ],
      },
    ],
  },
}

/* ---------- month grids ---------- */
export interface DayCell {
  day: number
  muted?: boolean
  tone?: 'blue' | 'rose'
  ring?: boolean
  dot?: boolean
  selected?: boolean
  thumb?: boolean
  /** Number of activity glyphs under the date (a24 screen 3). */
  marks?: number
}

function grid(start: number, prevLen: number, len: number, rows: number): DayCell[] {
  const cells: DayCell[] = []
  for (let i = 0; i < rows * 7; i++) {
    const n = i - start + 1
    if (n < 1) cells.push({ day: prevLen + n, muted: true })
    else if (n > len) cells.push({ day: n - len, muted: true })
    else cells.push({ day: n })
  }
  return cells
}

const patch = (cells: DayCell[], day: number, extra: Partial<DayCell>) =>
  cells.map((c) => (!c.muted && c.day === day ? { ...c, ...extra } : c))

let julyA = grid(2, 30, 31, 5)
julyA = patch(julyA, 15, { tone: 'blue', dot: true })
julyA = patch(julyA, 16, { tone: 'blue', dot: true })
julyA = patch(julyA, 17, { tone: 'blue', dot: true, ring: true })

export const trackScreen = {
  month: 'JULY 2026',
  weekdays: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
  cells: julyA,
  suggestionsTitle: 'Often tracked for breakfast',
  suggestions: ['Silken Tofu Overnight Oats with Dates and Pears', 'Avocado Toast with...', 'Greek'],
  placeholder: 'What do you want to track?',
}

let julyB = grid(2, 30, 31, 6)
julyB = patch(julyB, 1, { selected: true })
julyB = patch(julyB, 2, { thumb: true })

export const linkScreen = {
  name: 'Sam',
  month: 'July',
  year: "'26",
  weekdays: ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
  weekendFrom: 5,
  cells: julyB,
  placeholder: 'Paste a link',
}

let may = grid(5, 30, 31, 6).slice(0, 36).map((c) => (c.muted ? { ...c, day: 0 } : { ...c, marks: 2 }))
may = patch(may, 11, { tone: 'rose', marks: 4 })
may = patch(may, 12, { selected: true })

export const taskScreen = {
  time: '1:00 – 1:15 PM (15 min)',
  title: 'Submit portfolio',
  date: 'Tue, May 12, 2026',
  relative: 'Tomorrow',
  section: 'Time',
  month: 'May',
  year: '2026',
  today: 'Today',
  weekdays: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
  cells: may,
}

export const eventScreen = {
  title: 'Event',
  heading: 'Coffee with Sam',
  picker: [
    {
      items: ['Wed Jul 1', 'Thu Jul 2', 'Today', 'Fri Jul 3', 'Sat Jul 4', 'Sun Jul 5', 'Mon Jul 6', 'Tue Jul 7', 'Wed Jul 8', 'Thu Jul 9'],
      selected: 5,
      x: 164,
      align: 'right',
    },
    { items: ['9', '10', '11', '12', '1', '2', '3', '4', '5', '6'], selected: 5, x: 214 },
    { items: ['55', '56', '57', '58', '59', '00', '01', '02', '03', '04'], selected: 5, x: 270 },
    { items: ['AM', 'PM'], selected: 1, x: 324 },
  ] as WheelColumn[],
  rows: [
    { label: 'Start', info: true, value: 'Sun, Jul 5 at 2:00 PM' },
    { label: 'End', info: false, value: '4:00 PM' },
  ],
}

export interface FormRow {
  label: string
  value?: string
  muted?: boolean
  action?: string
}

let june = grid(1, 31, 30, 2)
june = june.map((c) => (c.muted ? { ...c, day: 0 } : c))

export const meetingScreen = {
  streak: 3,
  month: 'Jun 2026',
  weekdays: ['S', 'M', 'T', 'W', 'T', 'F', 'S'],
  cells: june,
  sheetTitle: 'Meeting',
  rows: [
    { label: 'Starts', value: 'Jun 26, 2026' },
    { label: 'Repeat', value: 'None', muted: true },
    { label: 'Dress code', value: 'Business casual' },
    { label: 'Closet items to include', action: 'Add' },
  ] as FormRow[],
  notes: 'Notes...',
  cta: 'Create new event',
}

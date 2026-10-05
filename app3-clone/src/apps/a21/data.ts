export const statusTime = '10:27'

export interface Account {
  initial: string
  name: string
  email: string
  enabled: boolean
}

export const accounts: Account[] = [{ initial: 'M', name: 'Mobbin Design2', email: 'mobbin.cms2@gmail.com', enabled: true }]

export const onboarding = {
  title: 'Select Google Accounts',
  addAccount: 'Add another account',
  cta: 'Get started',
}

export const gmailIntro = {
  title: 'Gmail on your calendar',
  body: ['Reservations for flights, restaurants, etc,', 'automatically added from email.'],
  note: 'You can change this in settings.',
  cta: 'Got it',
}

export const gmailDialog = {
  title: 'Events from Gmail',
  body: 'Events from Gmail will be added automatically for the account mobbin.cms2@gmail.com. You can change this in Settings.',
  action: 'OK',
}

export const splash = { text: 'Setting up your calendar...' }

export type ScheduleItem =
  | { kind: 'today'; weekday: string; day: number; text: string }
  | { kind: 'range'; label: string }
  | { kind: 'month'; label: string; tone: 'june' | 'july' }

export const schedule = {
  month: 'May',
  items: [
    { kind: 'today', weekday: 'TUE', day: 25, text: 'Nothing planned. Tap to create.' },
    { kind: 'range', label: 'MAY 30 – JUNE 5' },
    { kind: 'month', label: 'June', tone: 'june' },
    { kind: 'range', label: 'JUNE 6 – 12' },
    { kind: 'range', label: 'JUNE 13 – 19' },
    { kind: 'range', label: 'JUNE 20 – 26' },
    { kind: 'range', label: 'JUNE 27 – JULY 3' },
    { kind: 'month', label: 'July', tone: 'july' },
    { kind: 'range', label: 'JULY 4 – 10' },
    { kind: 'range', label: 'JULY 11 – 17' },
    { kind: 'range', label: 'JULY 18 – 24' },
  ] satisfies ScheduleItem[] as ScheduleItem[],
}

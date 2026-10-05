/** Content for the Origin clone — positions/metrics follow reference-dom/11.json. */
export interface NavLink {
  label: string
  /** Shows a "+" icon (menu trigger). */
  menu?: boolean
}
export interface Box {
  x: number
  y: number
  w: number
  h: number
}
export interface AdviceCard {
  eyebrow: string
  title: string
  body: string
}
export interface Feature {
  title: string
  body: string
  /** Mockup image box (relative to the card). */
  mediaH: number
  /** Title top relative to card top. */
  titleTop: number
}
export interface Notification {
  text: string
  strong?: string
  time: string
}

export const nav = {
  links: [
    { label: 'Products', menu: true },
    { label: 'For Employers' },
    { label: 'Resources' },
  ] satisfies NavLink[],
  login: 'Log In',
  cta: 'Get Started',
}

export const hero = {
  promo: { was: '$99', now: '$1 for 1 Year', badge: 'Limited time' },
  titleLines: [
    [{ t: 'Meet your ' }, { t: 'proactive', em: true }],
    [{ t: 'AI Financial Advisor.' }],
  ],
  body: 'Track all of your finances while Origin proactively finds new ways to save you money.',
  cta: 'Get Started',
  phone: { x: 405, y: 610, w: 630, h: 1301 } satisfies Box,
  found: ['We found 14 actions that', 'can save you $3,457'],
  card: {
    eyebrow: 'Tax strategy',
    title: 'Save $2,200 on childcare.',
    body: 'Put $7,500 of your childcare spending through a dependent care FSA and keep about $2,200 more per year.',
  } satisfies AdviceCard,
}

export const think = {
  title: [
    [{ t: 'You shouldn’t have to ' }, { t: 'think', em: true }],
    [{ t: 'about your money.' }],
  ],
  body: "We'll tell you what to do next and why it matters, right when it counts.",
  awards: [
    { x: 332, w: 195 },
    { x: 551, w: 176 },
    { x: 751, w: 163 },
    { x: 938, w: 170 },
  ],
}

export const logos = {
  caption: 'Loved by these companies',
  items: [
    { x: 158, y: 1838, w: 96, h: 30 },
    { x: 306, y: 1842, w: 60, h: 21 },
    { x: 418, y: 1837, w: 134, h: 31 },
    { x: 604, y: 1842, w: 86, h: 21 },
    { x: 742, y: 1841, w: 132, h: 24 },
    { x: 926, y: 1836, w: 100, h: 34 },
    { x: 1078, y: 1843, w: 65, h: 19 },
    { x: 1195, y: 1837, w: 88, h: 32 },
  ] satisfies Box[],
}

export const track = {
  title: [[{ t: 'Track', em: true }, { t: ' your entire' }], [{ t: 'financial life.' }]],
  cta: 'More about spending',
}

export const features: Feature[] = [
  { title: 'Stay on budget', body: 'Build a personalized budget in seconds, and know exactly how much you can spend.', mediaH: 373, titleTop: 445 },
  { title: 'Manage your subscriptions', body: 'Find recurring payments and cancel subscriptions you don’t need.', mediaH: 324, titleTop: 466 },
  { title: 'Invest with intention', body: 'Track your portfolio and monitor performance in one place.', mediaH: 273, titleTop: 466 },
  { title: 'Maximize your savings', body: "Earn more on your savings when you move it to Origin's high-yield cash account.", mediaH: 270, titleTop: 466 },
]

export const advice = {
  title: [[{ t: 'Receive', em: true }, { t: ' always-on' }], [{ t: 'financial advice.' }]],
  notification: {
    text: "You're paying $60,000 in investment fund fees you don't have to.",
    strong: 'See advice',
    time: '1m ago',
  } satisfies Notification,
}

export const analyze = {
  title: [[{ t: 'We analyze' }], [{ t: 'everything', em: true }]],
  body: 'We connect every piece of your finances to understand what matters most.',
}

export const chat = {
  title: 'Need help?',
  body: 'The team typically replies in a few minutes.',
}

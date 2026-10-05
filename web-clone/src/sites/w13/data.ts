/** Content for the Retool clone — metrics follow reference-dom/13.json. */
export interface Box {
  x: number
  y: number
  w: number
  h: number
}

export const banner = { badge: 'Public Beta: Retool CLI', link: 'Learn more' }

export const nav = {
  brand: 'Retool',
  links: [
    { label: 'Solution', menu: true },
    { label: 'Audience', menu: true },
    { label: 'Resources', menu: true },
    { label: 'Use cases' },
    { label: 'Pricing' },
  ],
  signIn: 'Sign in',
  demo: 'Book a demo',
  cta: 'Start for free',
}

export const hero = {
  title: 'Secure your vibe-coded apps',
  badge: 'New',
  tagline: 'Explore the new Retool app builder for free',
  prompt: { before: 'Build a simple KPI dashboard that pulls revenue and churn metrics from', mention: 'Snowflake', after: 'and refreshes daily.' },
  starter: 'Starter prompts',
  chips: [
    { label: 'Import code', icons: 3, x: 488, w: 180 },
    { label: 'Build with AI agents', icons: 5, x: 677, w: 259 },
  ],
  film: { lead: "See what's new.", cta: 'Watch the film' },
}

export const logos = {
  cols: [57, 397, 737, 1077],
  rows: [936, 1016],
  w: 292,
  h: 48,
  /** Rendered logo footprint inside each 292x48 cell. */
  marks: [
    [140, 22], [90, 26], [104, 40], [132, 36],
    [62, 26], [90, 22], [116, 28], [100, 30],
  ] as [number, number][],
  plus: [363, 703, 1043],
}

export const gallery = {
  title: 'Apps that mean business',
  rows: [
    { y: 1227, start: -170 },
    { y: 1422, start: -263 },
  ],
  tile: { w: 283, h: 177, step: 301 },
  cta: 'View app gallery',
}

export const feature = {
  title: 'Ship safely, with governance built in',
  body: 'Deploy with auth, access controls, and audit logging already in place. Fast to production, without sacrificing security.',
  link: 'Learn about security and governance',
  panels: [1800, 2584, 3368, 4152],
}

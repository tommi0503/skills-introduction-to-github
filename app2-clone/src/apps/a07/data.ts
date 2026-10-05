export type BotShape = 'triangle' | 'group' | 'pill' | 'circle' | 'square' | 'drop'

export interface ChatThread {
  id: string
  title: string
  tag?: string
  time: string
  preview?: string
  shape: BotShape
  online?: boolean
}

export const onboarding = {
  heading: 'Meet Your First Bot',
  botName: 'Inbox Triage',
  botBlurb: 'Sorts email, drafts replies, surfaces what’s urgent',
  pages: 5,
  activePage: 2,
  primary: 'Start Chat',
  secondary: 'Create My Own',
}

export const me = { initials: 'SL' }

export const threads: ChatThread[] = [
  {
    id: 'slmob',
    title: 'SLMob',
    tag: 'Meal prepping',
    time: '10:51 PM',
    preview: 'Told them: every Sunday 8:41, menu plus shopping list.',
    shape: 'triangle',
    online: true,
  },
  { id: 'group', title: 'UX Research, Design, Chief of Staff', time: '10:46 PM', shape: 'group' },
  {
    id: 'ux',
    title: 'UX Research Bot',
    tag: 'Challenges in onboarding',
    time: '10:45 PM',
    preview: 'What’s the first thing you want me on? A study, a recap…',
    shape: 'pill',
  },
  {
    id: 'design',
    title: 'Design',
    tag: 'Proposes UI fixes',
    time: '7:13 PM',
    preview: 'Yes. Drop the screenshot (or a few, if that helps).',
    shape: 'circle',
  },
  {
    id: 'inbox',
    title: 'Inbox Triage',
    time: '6:47 PM',
    preview: 'Sent to alexsmith.mobbin@gmail.com. Subject line: weekly…',
    shape: 'square',
  },
  {
    id: 'cos',
    title: 'Chief of Staff',
    time: '6:39 PM',
    preview: 'Nothing on on-call, travel, family, or Today’s calendar.',
    shape: 'drop',
    online: true,
  },
]

export interface ChatOption {
  key: string
  label: string
}

export const conversation = {
  bot: 'SLMob',
  messages: [
    'Bowls rotated through peanut sauce, chili-lime, and sesame slaw so they don’t get repetitive midweek. Dinners: Japanese curry Mon and Thu, garlic salmon Tue and Fri (cook those fresh, 15 min — fish doesn’t keep), chicken noodle stir-fry Wednesday.',
    'Sunday order: rice cooker on first (4 cups), chicken thighs in the oven at 200°C, broccoli and carrots on a second tray, curry on the stove with S&B roux, oat jars and cucumber slaw while that simmers. Then box it. Full quantities, timing, and the shopping list are in the file.',
  ],
  file: { name: 'week-meal-prep', ext: '.md', size: '3.1 KB' },
  question: 'Want me to tweak this, or is this the shape of week you wanted?',
  options: [
    { key: 'A', label: 'This works' },
    { key: 'B', label: 'Vegetarian' },
    { key: 'C', label: 'No seafood' },
    { key: 'D', label: 'Cooking for two' },
    { key: 'E', label: 'Shorter Sunday cook' },
  ] satisfies ChatOption[],
  placeholder: 'Ask SLMob',
}

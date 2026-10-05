import type { SyntaxToken } from './theme'

export interface NavLink {
  label: string
  dropdown?: boolean
}

export const nav: NavLink[] = [
  { label: 'Products', dropdown: true },
  { label: 'Solutions', dropdown: true },
  { label: 'Developer', dropdown: true },
  { label: 'Company', dropdown: true },
  { label: 'Pricing' },
  { label: 'News' },
]

export const navActions = { secondary: 'Contact Sales', primary: 'Try for free' }

export const hero = {
  badge: 'New',
  announcement: 'Meet Grok 4.7',
  announcementSub: 'Our new model',
  lines: ['Frontier AI models', 'for everything you'],
  underlined: 'build',
  tail: '.',
  sub: "Reasoning, code, voice, images, and video. Trained on the world's largest supercluster.",
  primary: 'Get API Access',
  secondary: 'View Documentation',
}

export interface Bubble {
  text: string
  from: 'user' | 'bot'
  top: number
  width: number
  /** Extra right padding to reproduce the captured line break. */
  padRight?: number
}

/** Chat card conversation (positions relative to the card's top edge). */
export const chatBubbles: Bubble[] = [
  { text: 'Why is the sky blue?', from: 'user', top: -15, width: 127 },
  { text: 'Shorter blue wavelengths scatter more off air molecules than longer red ones.', from: 'bot', top: 28, width: 297, padRight: 40 },
  { text: 'How do black holes form?', from: 'user', top: 88, width: 154 },
  { text: 'A massive star exhausts its fuel and gravity collapses the core into a singularity.', from: 'bot', top: 131, width: 297, padRight: 16 },
  { text: 'What causes aurora borealis?', from: 'user', top: 191, width: 170 },
]

export const botCard = {
  prompt: 'month-end is friday, close out the card for me?',
  reply: "i'll match every charge to a receipt and file\nthe report. anything that doesn't line up, i ask instead of guessing.",
  routineLabel: 'Created routine',
  routineName: 'Month-end close',
  thinking: 'Thinking',
}

export const productCards = { chat: 'Chat', build: 'Build', bot: 'Bot', imagine: 'Imagine', voice: 'Voice', explore: 'Explore' }

export const developers = {
  eyebrow: 'For developers',
  title: ['One API.', 'Every modality.'],
  body: 'Text, code, voice, images, and video — all through a single unified API. Start building in seconds.',
  primary: 'Get API Key',
  secondary: 'Read Docs',
  stats: [
    { value: '1M+', label: 'API calls per day' },
    { value: '<200ms', label: 'Median latency' },
    { value: '5+', label: 'Model families' },
  ],
  tabs: ['Python', 'TypeScript', 'TypeScript (OpenAI SDK)', 'cURL'],
}

export type CodeLine = [string, SyntaxToken][]

export const pythonSample: CodeLine[] = [
  [['import', 'kw'], [' os', 'id']],
  [['from', 'kw'], [' xai_sdk ', 'id'], ['import', 'kw'], [' Client', 'id']],
  [['from', 'kw'], [' xai_sdk.chat ', 'id'], ['import', 'kw'], [' user', 'id']],
  [['client ', 'id'], ['=', 'kw'], [' Client(', 'id']],
  [['    ', 'id'], ['api_key', 'arg'], ['=', 'kw'], ['os.getenv(', 'id'], ['"XAI_API_KEY"', 'str'], [')', 'id']],
  [[')', 'id']],
  [['chat ', 'id'], ['=', 'kw'], [' client.chat.create(', 'id'], ['model', 'arg'], ['=', 'kw'], ['"grok-4.7"', 'str'], [')', 'id']],
  [['chat.append(user(', 'id'], ['"Explain quantum computing"', 'str'], ['))', 'id']],
  [['response ', 'id'], ['=', 'kw'], [' chat.sample()', 'id']],
  [['print', 'fn'], ['(response.content)', 'id']],
]

export const stats = [
  { value: '400M+', label: 'queries processed daily', logo: false },
  { value: '200K', label: 'GPUs in', logo: true },
  { value: '122', label: 'days to build Colossus', logo: false },
]

export interface NewsItem {
  category?: string
  date: string
  title: string
}

export const news = {
  title: 'Latest news',
  all: 'All posts',
  items: [
    { category: 'Product', date: 'Sep 21, 2026', title: 'Introducing Grok 4.7' },
    { category: 'Product', date: 'Sep 28, 2026', title: 'Team Bots: shared AI teammates that learn as they work' },
    { category: 'Product', date: 'Sep 22, 2026', title: 'How SpaceXAI is using Grok Bot to scale customer support' },
    { date: 'Sep 18, 2026', title: 'Introducing Grok Voice Transcribe 2.0' },
  ] as NewsItem[],
}

export interface Plan {
  title: string
  body: string
  features: string[]
  cta: string
  variant: 'solid' | 'outline'
}

export const getStarted = {
  title: 'Choose how to get started',
  plans: [
    {
      title: 'Build on your own',
      body: 'Launch your AI-powered product with:',
      features: [
        'Access to all Grok models',
        'Usage-based pricing',
        'Automatically increasing rate limits',
        'Comprehensive documentation and guides',
      ],
      cta: 'Start Building',
      variant: 'solid',
    },
    {
      title: 'Get extra support',
      body: 'Custom rate limits and hands-on support for your team.',
      features: [
        'Dedicated onboarding support',
        'Custom rate limits',
        'Billing via monthly invoices',
        'Single sign-on and audit logging',
        'Data residency options',
      ],
      cta: 'Contact Sales',
      variant: 'outline',
    },
  ] as Plan[],
}

export interface FooterGroup {
  title: string
  links: string[]
}

/** Footer columns; each column stacks one or more groups. */
export const footerColumns: FooterGroup[][] = [
  [
    { title: 'Products', links: ['Chat', 'Build', 'Imagine', 'Voice', 'Bot', 'Grokipedia'] },
    { title: 'Download', links: ['grok.com', 'iOS', 'Android', 'Grok on X'] },
  ],
  [
    { title: 'Solutions', links: ['Business', 'Government', 'Customer Support', 'Legal', 'Security', 'Use Cases'] },
    { title: 'Grok Bot', links: ['Overview', 'Marketplace', 'Guides', 'Use Cases', 'Changelog'] },
  ],
  [
    { title: 'Developers', links: ['API Overview', 'Pricing', 'Models', 'Console', 'Changelog', 'Docs', 'Status'] },
    { title: 'Enterprise', links: ['Contact Sales', 'FAQs', 'BAA', 'DPA'] },
  ],
  [
    { title: 'Company', links: ['About', 'Colossus', 'Careers', 'News', 'Contact'] },
    { title: 'Trust', links: ['Safety', 'Security', 'Privacy Portal', 'Subprocessors', 'Help Center'] },
  ],
  [
    { title: 'Legal', links: ['Terms', 'Enterprise Terms', 'Privacy', 'Cookies', 'AUP', 'Brand', 'Privacy choices'] },
    { title: 'Social', links: ['@SpaceXAI', '@grok', 'Discord'] },
  ],
]

export const footerMeta = { copyright: '© 2026 SpaceXAI LLC', builtWith: 'Built with Grok' }

export const cookie = {
  text: 'Essential cookies keep the site working and stay on. Optional cookies help with performance and advertising — accept, reject, or manage them. Learn more in our',
  links: ['Cookie Policy', 'Privacy Policy', 'Terms of Service'],
  settings: 'Cookies Settings',
  reject: 'Reject All',
  accept: 'Accept All Cookies',
}

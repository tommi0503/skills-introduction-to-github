import type { LucideIcon } from 'lucide-react'
import {
  BookOpen,
  Brush,
  CloudDownload,
  Code,
  Gauge,
  Hand,
  Layers,
  Lightbulb,
  ListChecks,
  LockKeyhole,
  Logs,
  Monitor,
  MonitorUp,
  Shapes,
  Shield,
  ShieldCheck,
  ShieldOff,
  ShieldUser,
  Sparkles,
  TableProperties,
  Zap,
  HandHelping,
} from 'lucide-react'

export interface Rect {
  x: number
  y: number
  w: number
  h: number
}

/* ---------- Header ---------- */
export const nav = {
  logo: { w: 127, h: 25 },
  links: [
    { label: 'Product', menu: true },
    { label: 'Solutions', menu: true },
    { label: 'Resources', menu: true },
    { label: 'Pricing', menu: false },
  ],
  login: 'Login',
  secondary: 'Start for free',
  primary: 'Talk to us',
}

/* ---------- Hero ---------- */
export const hero = {
  badge: { tag: 'New', label: 'GitBook MCP Server' },
  title: [
    [{ text: 'The docs platform that flags' }],
    [{ text: 'outdated content. ' }, { text: 'Then fixes it.', accent: true }],
  ] as Array<Array<{ text: string; accent?: boolean }>>,
  subtitle: 'GitBook keeps docs accurate, for both people and AI',
  primary: 'Start for free',
  github: 'Sign up with GitHub',
}

/** Customer logo strip (absolute page coordinates of the logos visible in the frozen marquee; edges fade out). */
export const logoStrip: Rect[] = [
  { x: 244, y: 490, w: 75, h: 33 },
  { x: 421, y: 492, w: 120, h: 29 },
  { x: 645, y: 488, w: 72, h: 37 },
  { x: 803, y: 499, w: 156, h: 15 },
  { x: 1027, y: 491, w: 108, h: 30 },
  { x: 1244, y: 495, w: 75, h: 23 },
]

/* ---------- Product demo ---------- */
export const demoTabs = ['Ask your docs', 'AI insights', 'Embed and connect', 'Proactive updates']

export const docsApp = {
  search: 'Search…',
  keys: ['Ctrl', 'K'],
  ask: 'Ask',
  signIn: 'Sign in',
  tabs: [
    { label: 'Product', icon: Shapes, active: true },
    { label: 'API', icon: Code },
    { label: 'Help center', icon: HandHelping },
    { label: 'Changelog', icon: ListChecks },
  ] as Array<{ label: string; icon: LucideIcon; active?: boolean }>,
  sidebar: [
    {
      title: 'Getting started',
      items: [
        { label: 'Welcome', icon: Hand, active: true },
        { label: 'Quickstart', icon: Zap },
        { label: 'Concepts', icon: Lightbulb },
        { label: 'System performance', icon: Gauge },
        { label: 'Optimizing for workloads', icon: Sparkles },
        { label: 'Kernel tuning', icon: Logs },
      ],
    },
    {
      title: 'Security',
      items: [
        { label: 'Overview', icon: BookOpen },
        { label: 'Security best practices', icon: ShieldCheck },
        { label: 'System hardening', icon: TableProperties },
        { label: 'Updates and patching', icon: CloudDownload },
        { label: 'Audit and logging', icon: ListChecks },
        { label: 'Vulnerability management', icon: ShieldOff },
      ],
    },
    {
      title: 'customization',
      items: [
        { label: 'Theme customization', icon: Brush },
        { label: 'Custom domain', icon: Monitor },
      ],
    },
  ] as Array<{ title: string; items: Array<{ label: string; icon: LucideIcon; active?: boolean }> }>,
  eyebrow: 'Getting started',
  title: 'Welcome to Acme',
  intro: 'Acme is an open-source, distributed operating system incubated and operated by the OpenHQ Foundation.',
  cards: [
    { title: 'Quickstart', text: 'Get up and running fast with Acme.' },
    { title: 'Security', text: 'Monitor and optimize your system.' },
    { title: 'Quickstart', text: 'Get up and running fast with Acme' },
    { title: 'Security', text: 'Monitor and optimize your system.' },
  ],
}

export const assistant = {
  title: 'GitBook Assistant',
  question: 'How do I get started with Acme?',
  answer: [
    { text: 'To get started with Acme, start by ' },
    { text: 'creating an account', link: true },
    { text: ' and invite your team.' },
  ] as Array<{ text: string; link?: boolean }>,
  input: 'How do I get started with Acme?',
  context: 'Based on your context',
  send: 'Send',
  cta: 'GitBook Assistant',
}

/* ---------- Get started with AI ---------- */
export const getStarted = {
  title: 'Get started with AI',
  agents: ['Claude', 'ChatGPT', 'Cursor'],
  setup: 'Set up GitBook with your agent',
  copy: 'Copy prompt',
}

/* ---------- Split features ---------- */
export interface SplitFeature {
  badge?: { label: string; value: string }
  title: string
  text: string
  /** Media rectangle relative to the section box. */
  mediaSide: 'left' | 'right'
}

export const splits: SplitFeature[] = [
  {
    badge: { label: 'Agent traffic tracker', value: '56.003%' },
    title: 'Agents turn small docs errors into big problems',
    text: 'When your product changes, your docs don’t automatically update with it. GitBook spots what’s drifted and queues it for review before the wrong answer appears everywhere.',
    mediaSide: 'right',
  },
  {
    title: 'Readable to an agent isn’t the same as useful to a user',
    text: 'Most docs tools focus on making your docs readable by agents. That’s the easy part. GitBook makes sure what they find is reliable. So when a human or agent follows the instructions, they get the right answer.',
    mediaSide: 'left',
  },
]

/* ---------- System ---------- */
export const system = {
  title: ['A system built to keep docs', 'accurate, not just create them.'],
  cards: [
    {
      icon: null,
      title: 'Collaborate on docs like code',
      text: 'Sync your repo, then branch, review, and merge documentation like a PR.',
      chip: 'Git Sync',
    },
    {
      icon: Layers,
      title: 'Proactively detect stale content',
      text: 'Scans your docs for content that no longer matches your product and flags it for review.',
      chip: 'GitBook Agent',
    },
    {
      icon: Sparkles,
      title: 'Turn docs into answers',
      text: 'Users can ask your docs directly through the AI Assistant and get personalized support.',
      chip: 'AI Assistant',
    },
    {
      icon: Lightbulb,
      title: 'Know what to fix before users tell you',
      text: 'Tracks where users (both human and agent) get stuck and shows you which content to fix first.',
      chip: 'Insights',
    },
  ] as Array<{ icon: LucideIcon | null; title: string; text: string; chip: string }>,
}

/* ---------- Testimonial ---------- */
export const testimonial = {
  quote:
    '“After we started using GitBook, life became completely different. Here at bunq, our goal is to make life easy — and we don\'t only want that for our users, but for ourselves too. GitBook did exactly that for us. It made writing our public API documentation so much easier.”',
  author: 'Emily Durães',
  role: 'Product Owner - Public API',
  company: 'bunq',
  cta: 'View the docs',
}

/* ---------- Enterprise ---------- */
export const enterprise = {
  title: 'Enterprise-grade docs that stay accurate at scale',
  text: ['SOC 2, ISO 27001, SAML SSO, access controls, white-glove migration.', 'Built for teams that need security, control and collaboration.'],
  cta: 'Get a demo',
  left: [
    {
      icon: MonitorUp,
      title: 'Migration and support',
      text: 'White-glove migration, 1:1 support & training, and custom integrations ensure you get up, running and ready to scale fast.',
    },
    {
      icon: ShieldUser,
      title: 'Access control',
      text: 'Tiered role and permissions settings let you precisely choose who can view and edit your content.',
    },
  ],
  right: [
    {
      icon: Shield,
      title: 'Security and compliance',
      text: 'We are SOC 2, ISO 27001 and GDPR compliant, with SAML-based SSO to meet your security and data requirements.',
    },
    {
      icon: LockKeyhole,
      title: 'Auth-protected content',
      text: 'With authenticated access, only your chosen customers, team members or authorized users can view your docs.',
    },
  ],
}

export const overlays = {
  cookie: 'We use cookies to personalize content, run ads, and analyze traffic.',
  okay: 'Okay',
  ask: 'Ask',
}

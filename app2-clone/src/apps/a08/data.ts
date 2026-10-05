import {
  Book,
  Building2,
  CircleDot,
  File,
  GitPullRequest,
  House,
  Inbox,
  LaptopMinimal,
  MessagesSquare,
  Bot,
  SquareKanban,
  Star,
  Telescope,
  type LucideIcon,
} from 'lucide-react'

/* ---------- sign-in ---------- */
export const signIn = {
  primary: { label: 'Sign in to GitHub.com', caption: 'Use your account to sign in to GitHub.com' },
  secondary: { label: 'Sign in with GitHub Enterprise', caption: 'Requires server version 3.10.0 or higher' },
  legal: { before: 'By signing in you accept our ', terms: 'Terms of use', middle: ' and ', privacy: 'Privacy policy', after: '.' },
}

/* ---------- tabs ---------- */
export interface NavTab {
  key: string
  label: string
  icon: LucideIcon
  filled?: boolean
}
export const navTabs: NavTab[] = [
  { key: 'home', label: 'Home', icon: House, filled: true },
  { key: 'inbox', label: 'Inbox', icon: Inbox },
  { key: 'explore', label: 'Explore', icon: Telescope },
  { key: 'copilot', label: 'Copilot', icon: Bot },
]

/* ---------- home ---------- */
export interface WorkItem {
  key: string
  label: string
  icon: LucideIcon
  color: string
  filled?: boolean
}
export const myWork: WorkItem[] = [
  { key: 'issues', label: 'Issues', icon: CircleDot, color: '#4f9f5b' },
  { key: 'prs', label: 'Pull Requests', icon: GitPullRequest, color: '#4b8cf0' },
  { key: 'discussions', label: 'Discussions', icon: MessagesSquare, color: '#9a6ae0' },
  { key: 'projects', label: 'Projects', icon: SquareKanban, color: '#6f7680' },
  { key: 'repos', label: 'Top Repositories', icon: Book, color: '#363a40' },
  { key: 'orgs', label: 'Organizations', icon: Building2, color: '#d2722e' },
  { key: 'starred', label: 'Starred', icon: Star, color: '#dfbd4a', filled: true },
]

export interface RepoRef {
  owner: string
  name: string
}
export const favorites: RepoRef[] = [
  { owner: 'SLMobbin', name: 'padel-score-counter' },
  { owner: 'SLMobbin', name: 'snake-game' },
]

/* ---------- issue ---------- */
export const issue = {
  owner: 'SLMobbin',
  repo: 'padel-score-counter',
  number: 2,
  title: 'Add dynamic scoring',
  state: 'Closed',
  progress: '1 of 1',
  author: 'SLMobbin',
  meta: ' · 4d · edited',
  role: 'Owner',
  bodyHeading: 'Acceptance Criteria',
  criteria: [
    'Scoreboard reflects padel rules accurately.',
    'UI is intuitive, responsive, and visually polished.',
    'Reset/new match controls work reliably.',
    'All new logic is covered by tests.',
  ],
  subIssues: [{ title: 'Build dynamic scoreboard UI', number: 6 }],
  timeline: [
    { actor: 'SLMobbin', text: ' added milestone v1.0' },
    { actor: 'SLMobbin', text: ' self-assigned this' },
  ],
}

/* ---------- diff ---------- */
export type DiffKind = 'hunk' | 'del' | 'add' | 'ctx'
/** A code token: `t` text, optional style role. */
export interface Token {
  t: string
  role?: 'heading' | 'link' | 'mark' | 'icon'
}
export interface DiffLine {
  kind: DiffKind
  no?: number
  tokens: Token[]
  expandable?: boolean
}

const ctx = (no: number, ...tokens: Token[]): DiffLine => ({ kind: 'ctx', no, tokens })
const del = (no: number, ...tokens: Token[]): DiffLine => ({ kind: 'del', no, tokens })
const add = (no: number, ...tokens: Token[]): DiffLine => ({ kind: 'add', no, tokens })

export const diff = {
  title: 'Files Changed',
  additions: '+172',
  deletions: '-17',
  file: 'README.md',
  lines: [
    { kind: 'hunk', tokens: [{ t: '@@ -1,4 +1,4 @@' }] },
    del(1, { t: '# ' }, { t: 'Score Counter', role: 'heading' }, { t: ' Boilerplate', role: 'mark' }),
    add(1, { t: '# ' }, { t: 'Padel ', role: 'mark' }, { t: 'Score Counter', role: 'heading' }),
    ctx(2),
    ctx(3, { t: '[![License: MIT](' }, { t: 'https://img.shields.io/badge/License-MIT-yellow.svg', role: 'link' }),
    ctx(4, { t: '![Database: PostgreSQL](' }, { t: 'https://img.shields.io/badge/Database-PostgreSQL', role: 'link' }),
    { kind: 'hunk', expandable: true, tokens: [{ t: '@@ -7,15 +7,14 @@' }] },
    ctx(7, { t: '![Style: CSS](' }, { t: 'https://img.shields.io/badge/Style-CSS', role: 'link' }),
    ctx(8, { t: '![Framework: Express](' }, { t: 'https://img.shields.io/badge/Express', role: 'link' }),
    ctx(9),
    del(10, { t: 'A ' }, { t: 'reusable starter kit', role: 'mark' }, { t: ' for ' }, { t: 'building score-tracking apps', role: 'mark' }),
    add(10, { t: 'A ' }, { t: 'dedicated web app', role: 'mark' }, { t: ' for tracking ' }, { t: 'padel matches', role: 'mark' }),
    ctx(11),
    ctx(12, { t: '## ', role: 'heading' }, { t: '🚀', role: 'icon' }, { t: ' Features', role: 'heading' }),
    del(13, { t: '- Simple point entry with intuitive controls' }),
    del(14, { t: '- Real-time score updates' }),
    del(15, { t: '- Match history tracking' }),
    del(16, { t: '- Modular scoring logic (easy to adapt for other sports)' }),
    del(17, { t: '- Clean UI components ready for customization' }),
    del(18),
    add(13, { t: '- Padel scoring logic → Points → Games → Sets' }),
    add(14, { t: '- Real-time updates → Scoreboard refreshes instantly' }),
    add(15, { t: '- Match history → Track completed matches with stats' }),
    add(16, { t: '- Reset & new match → Start fresh with one tap' }),
    add(17, { t: '- Clean UI → Responsive scoreboard with player names' }),
    ctx(18),
    ctx(19, { t: '## ', role: 'heading' }, { t: 'Tech Stack', role: 'heading' }),
    ctx(20, { t: 'This project uses the following technologies:' }),
  ] as DiffLine[],
}

/* ---------- copilot ---------- */
export interface SessionStep {
  key: string
  label: string
  icon?: LucideIcon
  state?: 'active' | 'working'
  trailing?: 'chevron' | 'duration'
  duration?: string
}
export const copilot = {
  title: 'Planning dark theme implementation',
  repo: 'SLMobbin/padel-score-counter',
  meta: 'Created just now · 1 session',
  prompt: 'Create a plan for dark theme implementation',
  steps: [
    { key: 'plan', label: 'Planning dark theme implementation', state: 'active', trailing: 'duration', duration: '28s' },
    { key: 'clone', label: 'Clone repository SLMobbin/padel-score-counter', icon: LaptopMinimal },
    { key: 'view', label: 'View padel-score-counter', icon: File, trailing: 'chevron' },
    { key: 'public', label: 'View public', icon: File },
    { key: 'src', label: 'View src', icon: File },
    { key: 'working', label: 'Working...', state: 'working' },
  ] as SessionStep[],
  placeholder: 'Follow up',
}

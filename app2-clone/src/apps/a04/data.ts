import { Building2, Mail, UserKey, type LucideIcon } from 'lucide-react'

/** A sign-in provider row. Brand marks are placeholders; generic ones use a lucide icon. */
export interface Provider {
  key: string
  label: string
  /** lucide glyph; when absent a brand-mark placeholder is rendered. */
  icon?: LucideIcon
}

export const providers: Provider[] = [
  { key: 'google', label: 'Google' },
  { key: 'apple', label: 'Apple' },
  { key: 'microsoft', label: 'Microsoft' },
  { key: 'passkey', label: 'Passkey', icon: UserKey },
  { key: 'sso', label: 'SSO', icon: Building2 },
  { key: 'email', label: 'Email', icon: Mail },
]

/** Inline rich-text run: plain or link-styled. */
export interface TextRun {
  text: string
  kind?: 'plain' | 'link' | 'underline'
}

export const welcome = {
  title: 'Welcome to Notion Mail',
  subtitle: 'Continue with a Notion account',
  cta: 'Get started',
  legal: [
    { text: 'By clicking "Get started" above, you acknowledge that you have read and understood, and agree to the ' },
    { text: 'Notion Mail Terms', kind: 'link' },
    { text: ' and ' },
    { text: 'Privacy Policy', kind: 'link' },
    { text: ' as applicable to your use of Notion Mail' },
  ] satisfies TextRun[],
}

export const sheet = {
  host: 'notion.so',
  title: 'Add an account',
  subtitle: ['Use an existing account,', 'or sign up with a new email'],
}

export const emailForm = {
  label: 'Email',
  placeholder: 'Enter your email address...',
  hint: 'Use an organization email to easily collaborate with teammates',
  cta: 'Continue',
  legal: [
    { text: 'By continuing, you acknowledge that you understand and agree to the ' },
    { text: 'Terms & Conditions', kind: 'underline' },
    { text: ' and ' },
    { text: 'Privacy Policy', kind: 'underline' },
  ] satisfies TextRun[],
}

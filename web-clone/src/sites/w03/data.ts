export interface NavItem {
  label: string
  hasMenu?: boolean
}

export interface AudienceCard {
  title: string
  body: string
  cta: string
  tone: string
}

export interface FeatureTab {
  label: string
  active?: boolean
}

import { theme } from './theme'

export const announcement = {
  text: 'We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence',
  cta: 'Learn more',
}

export const brand = 'Harvey'

export const navItems: NavItem[] = [
  { label: 'Platform', hasMenu: true },
  { label: 'Solutions', hasMenu: true },
  { label: 'Customers' },
  { label: 'Security' },
  { label: 'Resources', hasMenu: true },
  { label: 'Company', hasMenu: true },
]

export const navActions = { login: 'Login', demo: 'Request a Demo' }

export const hero = {
  title: ['Build a Frontier', 'Legal Organization'],
  body: "The world's top law firms and in-house legal teams trust Harvey with their highest-stakes work.",
  cta: 'Request a Demo',
}

export const logoCloud = {
  title: '3,000+ Legal Organizations Build on Harvey',
}

export const platform = {
  title: 'One Platform for Legal Work',
  body: 'Firms and legal departments do their best work with Harvey. Run everything your team and practice needs on one collaborative platform.',
  cards: [
    {
      title: 'For Law Firms',
      body: 'Run every client matter securely on one platform, with your lawyers and agents working from the same context.',
      cta: 'Explore Harvey for Law Firms',
      tone: theme.tone.cardGreen,
    },
    {
      title: 'For In-House',
      body: 'Manage your contracts intelligently, optimize external counsel relationships and hand the repetitive work to agents.',
      cta: 'Explore Harvey for In-House Teams',
      tone: theme.tone.cardBrown,
    },
  ] satisfies AudienceCard[],
}

export const launch = {
  badge: 'New',
  title: 'Introducing Harvey II',
  body: 'The most powerful Harvey yet. Smarter agents can now deliver more complex work in exactly the way you like it.',
  cta: 'Request a Demo',
}

export const innovation = {
  title: 'Product Innovation for the Best Legal Minds',
  tabs: [{ label: 'Agents', active: true }, { label: 'Spaces' }] satisfies FeatureTab[],
}

import { CheckCheck, CreditCard, FileText, Pizza, ReceiptText, Search, Tag, User, type LucideIcon } from 'lucide-react'

/* ---------- Screen 1 · onboarding ---------- */
export interface BrandTile {
  key: string
  /** Flat tone standing in for the brand artwork. */
  tone: string
}

export const onboarding = {
  title: ['Split your purchase', 'anywhere VISA is accepted'],
  merchant: 'Late night delivery',
  price: '$60',
  installmentsLabel: '4 payments of',
  installment: '$16',
  primary: 'Create an account',
  secondary: 'Sign in',
  legal: [
    'Apply today with no hard credit check',
    'VISA is a trademark owned by Visa International',
    'Service Association and used under license.',
  ],
  legalLink: 'Read more about our terms here',
  /** Tiles on the wheel, index 0 sits on top (centre). */
  wheel: [
    { key: 'left2', tone: '#e5e7eb' },
    { key: 'amazon', tone: '#e5e7eb' },
    { key: 'doordash', tone: '#e5e7eb' },
    { key: 'walmart', tone: '#e5e7eb' },
    { key: 'right2', tone: '#e5e7eb' },
  ] satisfies BrandTile[],
}

/* ---------- Screen 2 · home ---------- */
export interface Chip {
  key: string
  label: string
  icon: LucideIcon
}
export interface Brand {
  key: string
  label: string
}
export interface PromoCard {
  key: string
  title: string[]
  cta: string
}
export interface NavItem {
  key: string
  label: string
  icon: LucideIcon
}

export const home = {
  greeting: 'Hi there,',
  spendingLabel: 'Spending power',
  spendingValue: '$1,000.00',
  notice: {
    badge: '2',
    title: 'Treat yourself to a bigger buy',
    body: ['Pay a little more upfront to unlock up to', '$1,500.00 in Estimated Spending Power.'],
    link: 'Learn more',
  },
  search: 'Search or enter URL',
  chips: [
    { key: 'pay2', label: 'Pay in 2', icon: CheckCheck },
    { key: 'bills', label: 'Bills', icon: FileText },
    { key: 'food', label: 'Food & Beverage', icon: Pizza },
  ] satisfies Chip[],
  disclosure: 'Affiliate disclosure',
  brandsTitle: 'Shop top brands',
  viewAll: 'View all',
  brands: [
    { key: 'amazon', label: 'Amazon' },
    { key: 'chewy', label: 'Chewy' },
    { key: 'stubhub', label: 'StubHub' },
    { key: 'tmobile', label: 'T-Mobile' },
    { key: 'pandora', label: 'Pandora' },
  ] satisfies Brand[],
  promos: [
    { key: 'nift', title: ['Grab a $30', 'thank-you gift', 'for using Zip'], cta: 'Claim with Nift' },
    { key: 'samsung', title: ['Samsung', 'Galaxy', 'for $25'], cta: 'Shop now' },
  ] satisfies PromoCard[],
  nav: [
    { key: 'online', label: 'Online', icon: Search },
    { key: 'instore', label: 'In-Store', icon: CreditCard },
    { key: 'deals', label: 'Deals', icon: Tag },
    { key: 'payments', label: 'Payments', icon: ReceiptText },
    { key: 'account', label: 'Account', icon: User },
  ] satisfies NavItem[],
  activeNav: 'online',
}

/* ---------- Screen 3 · search results ---------- */
export interface SearchResult {
  key: string
  title: string
  subtitle: string
  ad?: boolean
}

export const results = {
  query: 'Best Buy',
  cancel: 'Cancel',
  items: [
    { key: 'bobs', title: "Bob's Discount Furniture", subtitle: "Bob's Discount Furniture", ad: true },
    { key: 'bbgift', title: 'Best Buy Gift Card', subtitle: 'zip.thegiftcardshop.com' },
    { key: 'bbmember', title: 'Best Buy Membership', subtitle: 'bestbuy.com' },
    { key: 'bestbuy', title: 'Best Buy', subtitle: 'bestbuy.com' },
    { key: 'costco', title: 'Costco', subtitle: 'costco.com' },
    { key: 'goat', title: 'GOAT', subtitle: 'goat.com' },
  ] satisfies SearchResult[],
  showFewer: 'Show fewer results',
  featuredTitle: 'Featured results',
  featured: ['bobs', 'amazon', 'b', 'ikea', 'lg'],
  google: { title: 'Google search', subtitle: 'Best Buy' },
  virtualCard: { title: 'Add amount to virtual card', body: ['Pay in other apps with your', 'online virtual card.'] },
}

/* ---------- Screen 4 · spending power ---------- */
export interface CardRow {
  key: string
  title: string
  sup?: string
  amount: string
  chevron?: boolean
}

export const spending = {
  estimateLabel: 'Estimated spending power',
  currency: '$',
  amount: '1000.00',
  payLabel: 'Pay in up to 2 or 4',
  payValue: '$1,000.00',
  cards: [
    { key: 'virtual', title: 'Online virtual card', sup: '¹', amount: 'Card amount: $0.00' },
    { key: 'instore', title: 'In-store', amount: 'Card amount: $0.00', chevron: true },
  ] satisfies CardRow[],
  upsell: {
    lead: 'You may be approved to spend up to',
    amount: '$1,500.00',
    sup: '²',
    mid: ' with a ',
    link: 'larger first installment',
  },
  levelUp: {
    title: 'All set to start!',
    body: 'Fully pay off 5 orders on-time to level up your spending power.',
    link: 'Learn more',
    steps: ['1', '2', '3', '4', '5'],
    cta: 'Pay with Zip to start',
  },
  about: {
    title: 'ABOUT SPENDING POWER',
    body:
      '² Displayed estimated spending power is for representative purposes only. Your Estimated Spending Power is a point-in-time estimate of how much you may be able to spend, is not guaranteed, and is impacted by a number of factors.',
  },
}

export interface Category {
  key: string
  label: string
}
export interface OfferCard {
  key: string
  store: string
  cashBack: string
  description: string
  code: string
}
export interface StoreTile {
  key: string
}
export interface NavItem {
  key: string
  label: string
}
export interface SocialProvider {
  key: string
  label: string
}

export const searchPlaceholder = 'Try searching Expedia'
export const homeTabs = [
  { key: 'today', label: 'Today' },
  { key: 'foryou', label: 'For you', badge: 'New' },
]
export const categories: Category[] = [
  { key: 'hot', label: 'Hot Deals' },
  { key: 'stores', label: 'All Stores' },
  { key: 'travel', label: 'Travel' },
  { key: 'exp', label: 'Experiences' },
  { key: 'school', label: 'School' },
]
export const promo = {
  badge: 'ONLINE & IN STORES',
  title: ['Limited-time offer:', 'Triple Cash Back'],
  cta: 'See All Stores',
}
export const offers: OfferCard[] = [
  {
    key: 'saks',
    store: 'Saks Fifth Avenue',
    cashBack: '2% Cash Back',
    description: 'Earn a $50 - $900 gift card with your purchase.',
    code: 'AUGGC',
  },
  { key: 'bg', store: '', cashBack: '', description: '', code: '' },
]
export const tripleSection = { title: 'Triple Cash Back stores', action: 'See All' }
export const storeTiles: StoreTile[] = [
  { key: 'tripadvisor' },
  { key: 'sams' },
  { key: 'gap' },
]
export const storeTilesNextRow: StoreTile[] = [
  { key: 'r1' },
  { key: 'r2' },
  { key: 'r3' },
]
export const navItems: NavItem[] = [
  { key: 'home', label: 'Home' },
  { key: 'explore', label: 'Explore' },
  { key: 'rewards', label: 'Rewards' },
  { key: 'instore', label: 'In-Store' },
  { key: 'account', label: 'Account' },
]

export const signup = {
  title: ["Let's get you signed up", 'and shopping'],
  skip: 'Skip',
  emailPlaceholder: 'Email',
  passwordPlaceholder: 'Password (8+ characters)',
  cta: 'Join Now',
  or: 'or',
  haveAccount: 'Already have an account?',
  signIn: 'Sign In',
  refer: 'Did someone refer you?',
}
export const socialProviders: SocialProvider[] = [
  { key: 'apple', label: 'Continue with Apple' },
  { key: 'facebook', label: 'Continue with Facebook' },
  { key: 'google', label: 'Continue with Google' },
]
export const filledForm = {
  email: 'alexsmith.mobbin@gmail.com',
  passwordLength: 19,
  strengthLabel: 'Password Strength:',
  strength: 'Very Strong',
}

import { Heart, MessageSquare, Search, CircleUserRound, Umbrella, Waves, TreePalm, type LucideIcon } from 'lucide-react'

/* ---------- Screen 1 · stays explore ---------- */
export interface Category {
  key: string
  label: string
  /** null → brand/illustrative glyph lucide can't express (placeholder). */
  icon: LucideIcon | null
}
export interface Listing {
  id: string
  place: string
  rating: string
  lines: string[]
  price: string
  unit: string
  dots: number
}
export interface ExploreTab {
  key: string
  label: string
  icon: LucideIcon | null
}

export const explore = {
  searchTitle: 'Where to?',
  searchSub: 'Anywhere · Any week · Add guests',
  categories: [
    { key: 'omg', label: 'OMG!', icon: null },
    { key: 'beach', label: 'Beach', icon: Umbrella },
    { key: 'pools', label: 'Amazing pools', icon: Waves },
    { key: 'islands', label: 'Islands', icon: TreePalm },
    { key: 'arctic', label: 'Arctic', icon: null },
  ] satisfies Category[],
  activeCategory: 'omg',
  listings: [
    {
      id: 'abiansemal',
      place: 'Abiansemal, Indonesia',
      rating: '4.87',
      lines: ['1,669 kilometers', 'Jul 2 – 7'],
      price: '$360',
      unit: 'night',
      dots: 5,
    },
    {
      id: 'ubud',
      place: 'Ubud, Indonesia',
      rating: '4.93',
      lines: ['1,672 kilometers', 'Jul 8 \u2013 13'],
      price: '$214',
      unit: 'night',
      dots: 5,
    },
  ] satisfies Listing[],
  mapLabel: 'Map',
  tabs: [
    { key: 'explore', label: 'Explore', icon: Search },
    { key: 'wishlists', label: 'Wishlists', icon: Heart },
    { key: 'trips', label: 'Trips', icon: null },
    { key: 'inbox', label: 'Inbox', icon: MessageSquare },
    { key: 'profile', label: 'Profile', icon: CircleUserRound },
  ] satisfies ExploreTab[],
  activeTab: 'explore',
}

/* ---------- Screen 2 · streak premium paywall ---------- */
export interface StreakPlan {
  key: string
  name: string
  price: string
  /** Lines under the name; `strong` lines are dark, the rest muted. */
  lines: { text: string; strong?: boolean }[]
  strike?: string
  badge?: string
  height: number
  /** Top inset of the card content. */
  padTop: number
}

export const streak = {
  title: 'Gentler Streak Premium',
  /** Pre-broken lines, as laid out in the app. */
  description: [
    'Streak, Workout Suggestions, Health Summary,',
    'Mirror Tracking, Add Workout with RPE,',
    'Statuses, Overview Charts, Sneak-Peek,',
    'Insights, Profile Customization.',
  ],
  plans: [
    {
      key: 'yearly',
      name: 'Yearly',
      price: '$24.99/year',
      strike: '$49.99/year',
      badge: 'For You 50% OFF',
      lines: [{ text: 'Includes' }, { text: 'Family Sharing' }],
      height: 119,
      padTop: 22,
    },
    { key: 'monthly', name: 'Monthly', price: '$7.99/month', lines: [], height: 105, padTop: 25 },
    {
      key: 'lifetime',
      name: 'Lifetime',
      price: '$139.99',
      lines: [{ text: 'Pay Once, Use Forever', strong: true }, { text: 'Includes Family Sharing' }],
      height: 109,
      padTop: 15,
    },
  ] satisfies StreakPlan[],
  selected: 'yearly',
  restore: 'Restore Purchase',
  summaryStrike: '$49.99',
  summary: '$24.99/year (50% OFF)',
  cta: 'Continue',
  ctaSub: 'Cancel Anytime',
  back: 'Back',
}

/* ---------- Screen 3 · nutrition premium trial ---------- */
export interface Feature {
  title: string
  text: string
}
export interface TrialPlan {
  key: string
  name: string
  price: string
  unit: string
  strike?: string
  billed: string
  badge?: string
}

export const trial = {
  title: ['Say hello to', 'your best self.'],
  subtitle: 'Members are up to 65% more likely to reach their goals with Premium.',
  features: [
    { title: 'Barcode Scan:', text: 'Skip the search and\nlog faster' },
    { title: 'Custom Macro Tracking:', text: 'Find your balance\nof carbs, protein & fat' },
    { title: 'Zero Ads:', text: 'Track and reach your goals,\ndistraction-free' },
  ] satisfies Feature[],
  selectTitle: 'Select a plan for your free trial.',
  plans: [
    {
      key: 'yearly',
      name: 'YEARLY',
      price: '$68.98',
      unit: '/YR',
      strike: '$179.76',
      billed: 'Billed yearly after free trial.',
      badge: '62% SAVINGS',
    },
    { key: 'monthly', name: 'MONTHLY', price: '$14.98', unit: '/MO', billed: 'Billed monthly after free trial.' },
  ] satisfies TrialPlan[],
  selected: 'yearly',
  note: 'Change plans or cancel anytime.',
  cta: 'Start 1-Month Free Trial',
  /** Food photo cut-outs scattered over the top-right corner. */
  photos: [
    { x: 228, y: -8, w: 64, h: 58, r: '45%' },
    { x: 336, y: -6, w: 62, h: 42, r: '0 0 0 40px' },
    { x: 296, y: 48, w: 72, h: 56, r: '40%' },
    { x: 276, y: 82, w: 90, h: 64, r: '45%' },
    { x: 356, y: 150, w: 40, h: 84, r: '20px 0 0 20px' },
  ],
}

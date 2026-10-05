export interface Listing {
  kind: string
  title: string[]
  rating: string
  reviews: string
  badge: string
}

export interface TripField {
  label: string
  value: string
  action: string
}

export interface PayOption {
  key: string
  title: string
  description: string
  link?: string
}

export const booking = {
  title: 'Request to book',
  listing: {
    kind: 'Room in rental unit',
    title: ['Centre place Graslin -', 'Private room La Cambronne'],
    rating: '4.95',
    reviews: '(22)',
    badge: 'Superhost',
  } satisfies Listing,
  tripTitle: 'Your trip',
  trip: [
    { label: 'Dates', value: 'Aug 1 – 2', action: 'Edit' },
    { label: 'Guests', value: '1 guest', action: 'Edit' },
  ] satisfies TripField[],
  payTitle: 'Choose how to pay',
  payOptions: [
    { key: 'full', title: 'Pay in full', description: "Pay the total ($93.05) now and you're all set." },
    {
      key: 'part',
      title: 'Pay part now, part later',
      description: '$50.49 due today,\u00a0 $42.56 on Jul 17, 2023. No extra fees.',
      link: 'More info',
    },
  ] satisfies PayOption[],
  selectedPay: 'full',
}

export interface CartItem {
  qty: number
  name: string
  price: string
}

export interface ActionRow {
  key: 'gift' | 'promo'
  title: string
  subtitle: string
  accent?: boolean
}

export interface FeeRow {
  label: string
  value: string
  info?: boolean
  accent?: boolean
  total?: boolean
}

export const checkout = {
  title: 'Checkout',
  itemsTitle: 'Your items',
  seeMenu: 'See menu',
  items: [{ qty: 1, name: 'Regular Oreo McFlurry', price: '$5.69' }] satisfies CartItem[],
  addItems: 'Add items',
  actions: [
    { key: 'gift', title: 'Make it a gift', subtitle: 'Add recipient info and a message' },
    { key: 'promo', title: 'Promotion applied', subtitle: '$25 off', accent: true },
  ] satisfies ActionRow[],
  upsell: 'Add $9.31 to save with Uber One',
  fees: [
    { label: 'Subtotal', value: '$5.69' },
    { label: 'Promotion', value: '-$5.69', accent: true },
    { label: 'Delivery Fee', value: '$2.49', info: true },
    { label: 'Taxes & Other Fees', value: '$3.40', info: true },
    { label: 'Total', value: '$5.89', total: true },
  ] satisfies FeeRow[],
  cta: 'Next · $5.89',
}

import {
  Bike,
  CircleCheck,
  Coffee,
  ConciergeBell,
  Donut,
  Flame,
  IceCreamCone,
  Leaf,
  Receipt,
  RefreshCcw,
  Soup,
  type LucideIcon,
} from 'lucide-react'

export const brand = 'TheKitchen~'

export interface QuickAction {
  key: string
  label: string
  icon?: LucideIcon
  glyph?: string
  filled?: boolean
}

export const quickActions: QuickAction[] = [
  { key: 'repeat', label: 'Repeat last order', icon: RefreshCcw },
  { key: 'help', label: 'Help me choose', glyph: '?' },
  { key: 'surprise', label: 'Surprise me', icon: ConciergeBell, filled: true },
]

export interface Tag {
  key: string
  label?: string
  icon: LucideIcon
  color: string
  /** Icon drawn inside a filled circle (e.g. donut badge). */
  badge?: boolean
}

export const categories: Tag[] = [
  { key: 'vegan', label: 'Vegan', icon: Leaf, color: '#3fae2a' },
  { key: 'coffee', label: 'Coffee', icon: Coffee, color: '#e8771d' },
  { key: 'donuts', label: 'Donuts', icon: Donut, color: '#ec1f4f', badge: true },
  { key: 'ice', label: 'Ice cream', icon: IceCreamCone, color: '#f59a1b' },
]

export interface Dish {
  key: string
  name: string[]
  price: string
}

export const recommended: Dish[] = [
  { key: 'quinoa', name: ['TheKitchen~', 'Quinoa'], price: '$20' },
  { key: 'asparagus', name: ['TheKitchen~', 'Asparagus'], price: '$18' },
]

export const cartCount = 2

export interface Nutrient {
  value: string
  label: string
}

export interface ProductVariant {
  name: string
  weight: string
  tags: Tag[]
  nutritionTitle: string
  nutrients: Nutrient[]
  ingredients: string[]
  storage: string[]
  quantity: number
  price: string
  cartCount: number
}

const productTags: Tag[] = [
  { key: 'vegan', label: 'Vegan', icon: Leaf, color: '#3fae2a' },
  { key: 'cal', label: 'Few Calories', icon: Flame, color: '#f2711c' },
]

const nutrients: Nutrient[] = [
  { value: '198', label: 'kcal' },
  { value: '13.1', label: 'proteins' },
  { value: '13.4', label: 'fats' },
  { value: '5.8', label: 'carbohydrates' },
]

export const quinoa: ProductVariant = {
  name: 'TheKitchen~ Quinoa',
  weight: '~240 g',
  tags: productTags,
  nutritionTitle: 'Nutritional value per 100 g',
  nutrients,
  ingredients: ['Quinoa, fresh peaches, shelled peas, onion', 'pieces, pistachios, chickpeas, lettuce and', 'avocado.'],
  storage: ['No more than a day, at temperature from +2°C', 'to +6°C.'],
  quantity: 1,
  price: '$20',
  cartCount: 1,
}

export const quinoaCompact: ProductVariant = {
  ...quinoa,
  weight: '240 g',
  ingredients: ['Quinoa, fresh peaches, shelled peas, onion pieces,', 'pistachios, chickpeas, lettuce and avocado.'],
  storage: ['No more than 5 days, at temperature from +2°C', 'to +6°C.'],
  cartCount: 2,
}

export interface DeliveryStep {
  key: string
  icon: LucideIcon
  done: boolean
}

export const delivery = {
  title: 'Estimated delivery time is 6:18 PM',
  subtitle: 'Your order is already on its way to you!',
  steps: [
    { key: 'order', icon: Receipt, done: true },
    { key: 'cook', icon: Soup, done: true },
    { key: 'ride', icon: Bike, done: true },
    { key: 'arrived', icon: CircleCheck, done: false },
  ] as DeliveryStep[],
  courier: { name: 'Sheri Turner Jr.', role: 'Courier' },
}

export interface CartLine {
  key: string
  name: string
  price: string
}

export const cart = {
  lines: [
    { key: 'quinoa', name: 'TheKitchen~ Quinoa', price: '$20' },
    { key: 'bread', name: 'Garlic Bread', price: '$8' },
    { key: 'asparagus', name: 'TheKitchen~ Asparagus', price: '$18' },
  ] as CartLine[],
  code: 'KITCHEN6',
  promo: 'Promocode Confirmed',
  summary: [
    { label: 'Subtotal', value: '$46.00' },
    { label: 'Discount', value: '- $6.00' },
  ],
  total: { label: 'Total', value: '$40.00' },
  cta: 'Checkout',
}

export const quiz = { title: 'Question 1/8', progress: 1 / 8 }

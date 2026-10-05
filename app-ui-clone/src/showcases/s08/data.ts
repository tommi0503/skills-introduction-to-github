import { Heart, Home, MessageCircleMore, CirclePlus, Search, type LucideIcon } from 'lucide-react'

export interface Product {
  id: string
  tag: string
  title: string[]
  price: string
  /** Image height in pt (cards in the masonry grid differ). */
  imageHeight: number
  /** Total card height in pt. */
  height: number
}

export const homeCategories = ['All', 'Vintage', 'Home', 'Tech', 'Art']

export const featured = {
  eyebrow: 'FEATURED COLLECTION',
  title: ['Mid-Century', 'Finds'],
  cta: 'EXPLORE',
}

export const homeProducts: Product[][] = [
  [{ id: 'camera', tag: 'VINTAGE · BERLIN', title: ['Olympus OM-1 35mm', 'Film Camera'], price: '$185', imageHeight: 207, height: 311 }],
  [{ id: 'mug', tag: 'HANDMADE · LISBON', title: ['Speckled Ceramic', 'Coffee Mug'], price: '$32', imageHeight: 166, height: 270 }],
]

export const listing = {
  tag: 'VINTAGE · COPENHAGEN',
  title: '1970s Danish Teak Sideboard',
  price: '$340',
  pickup: 'Local Pickup Only',
  photos: 2,
  specs: [
    { label: 'CONDITION', value: ['Excellent,', 'restored'] },
    { label: 'DIMENSIONS', value: ['120 x 45 x 70 cm'] },
  ],
  seller: { name: "Hazel's Attic", rating: '4.9', sales: '212 sales' },
  actions: { secondary: 'Contact', primary: 'Make Offer' },
}

export const searchQuery = 'Vintage Furniture'
export const searchFilters = ['Price', 'Distance', 'Condition', 'Style']
export const resultCount = '128 RESULTS FOUND'

export const searchProducts: Product[][] = [
  [
    { id: 'canvas', tag: 'ART · BERLIN', title: ['Modernist Abstract', 'Canvas'], price: '$450', imageHeight: 183, height: 286 },
    { id: 'candles', tag: 'VINTAGE · LONDON', title: ['Brass Taper Candle', 'Holders'], price: '$95', imageHeight: 233.5, height: 334 },
  ],
  [
    { id: 'lamp', tag: 'VINTAGE · BROOKLYN', title: ['1920s Brass Table', 'Lamp'], price: '$210', imageHeight: 166.6, height: 269 },
    { id: 'satchel', tag: 'ARTISANAL · FLORENCE', title: ['Leather Satchel'], price: '$145', imageHeight: 200.5, height: 292 },
  ],
]

export interface NavItem {
  key: string
  icon: LucideIcon
}

export const tabs: NavItem[] = [
  { key: 'home', icon: Home },
  { key: 'search', icon: Search },
  { key: 'sell', icon: CirclePlus },
  { key: 'inbox', icon: MessageCircleMore },
  { key: 'saved', icon: Heart },
]

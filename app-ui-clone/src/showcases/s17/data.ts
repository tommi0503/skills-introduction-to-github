import { Award, House, Star, Tag, UserRound, type LucideIcon } from 'lucide-react'

export const museumScreen = {
  venue: 'Art & History Museum',
  headline: { line1: 'Discover the', faded: 'Power', rest: 'of Art' },
  subtitle: 'Explore inspiring art and creative expressions.',
  actions: [
    { key: 'member', label: 'MEMBER', variant: 'outline' as const },
    { key: 'book', label: 'Book Now', variant: 'solid' as const },
  ],
}

export interface Artwork {
  key: string
  title: string
  artist: string
  medium: string
  price: string
}

export const galleryScreen = {
  greeting: 'Welcome to',
  title: 'Arts Gallery',
  search: 'Search Gallery',
  forYou: 'For You',
  categories: 'Categories',
  artworks: [
    { key: 'blue', title: 'Stillness in Blue', artist: 'Elena Varga', medium: 'Watercolor on paper', price: '$6,400' },
    { key: 'salvo', title: 'Salvo', artist: 'La cattedrale,2001', medium: 'Oil on paper laid on canvas', price: '$30,200' },
  ] satisfies Artwork[],
  nav: [
    { key: 'home', icon: House },
    { key: 'tags', icon: Tag },
    { key: 'profile', icon: UserRound },
  ] satisfies { key: string; icon: LucideIcon }[],
  activeNav: 'home',
}

export const artworkScreen = {
  name: ['Aurora', 'Vellmont'],
  meta: 'Female • May 27, 2021',
  price: '$5,000-$7,500',
  features: [
    { key: 'unique', icon: Star, label: 'One-of-a-kind artwork' },
    { key: 'cert', icon: Award, label: 'Includes Certificate of Authenticity' },
  ] satisfies { key: string; icon: LucideIcon; label: string }[],
  specs: ['Oil, acrylic and pastel on canvas', '48 × 36 × 1.5 in | 122 × 92 cm'],
  cta: 'Make an Offer',
}

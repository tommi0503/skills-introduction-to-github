import { AtSign, Camera, Music2, SquareUser, TvMinimalPlay, X, type LucideIcon } from 'lucide-react'

export const brand = { name: 'blastup', time: '13:13' }

export const hero = {
  badge: 'GROW WITH EASE',
  title: 'Supercharge your growth with 100% real Instagram likes',
  body: 'Struggling to stand out? Discover why thousands of Social Media users call Blastup their ‘secret’ for supercharging their growth. 100% hassle-free.',
}

export const pricingTeaser = {
  title: 'High quality likes for celebrity Instagrammers',
  plans: [
    { amount: '50', discount: '5% OFF' },
    { amount: '100', discount: '5% OFF' },
    { amount: '250', discount: '7% OFF' },
  ],
}

export const growHero = {
  badge: 'GROW WITH EASE',
  title: 'The easiest way to grow on Instagram & TikTok',
}

export interface Network {
  key: string
  icon: LucideIcon
}

/** Brand glyphs aren't in lucide, so the closest generic icons stand in. */
export const networks: Network[] = [
  { key: 'instagram', icon: Camera },
  { key: 'tiktok', icon: Music2 },
  { key: 'youtube', icon: TvMinimalPlay },
  { key: 'x', icon: X },
  { key: 'linkedin', icon: SquareUser },
  { key: 'threads', icon: AtSign },
]

export const picker = {
  title: 'What we’re growing today?',
  active: 'instagram',
  discounts: ['5% OFF', '5% OFF', '7% OFF'],
}

export const why = {
  badge: 'WHY USING BLASTUP',
  title: 'Why is Blastup the Best Instagram & TikTok growth service?',
  body: 'We provide you with the highest-quality followers, likes, and views. Guaranteed.',
}

export interface Feature {
  tag: string
  title: string
  body: string
  color: string
}

export const features: Feature[] = [
  {
    tag: 'GROWTH',
    title: 'Boost Growth',
    body: 'Growing on social isn’t as easy as it used to be. We’ll supercharge your growth without guesswork.',
    color: '#ff74cb',
  },
  {
    tag: 'SAFE',
    title: 'Stay Safe',
    body: 'Real engagement only.',
    color: '#3b7df0',
  },
]

export const faq = {
  badge: 'WE’RE HERE TO HELP',
  title: 'Common questions about buying Blastup likes',
  items: [
    {
      question: 'Why should I choose Blastup?',
      answer: [
        'One reason is that we’re repeatedly chosen as the #1 Instagram likes service in polls of the app’s power users, who praise our high-quality real likes, our reasonable prices, our immediate delivery, and the powerful results we deliver.',
        'If you’re looking for another reason, though, we’re one of the only high-end providers you can find that lets you split our packages between multiple posts and delivers free Instagram video views with every likes package.',
      ],
      open: true,
    },
    { question: 'What’s the point of buying likes?', answer: [], open: false },
  ],
}

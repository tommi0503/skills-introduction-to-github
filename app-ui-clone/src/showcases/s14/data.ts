import { BookOpenText, Bubbles, House, Settings, type LucideIcon } from 'lucide-react'

export const categories = ['Moments', 'Emotional', 'Motivation', 'Headache']
export const activeCategory = 'Emotional'

/** Waveform as a compact pattern: T = tall bar, s = short bar. */
export const waveformPattern = 'TsTssTssTTsTssTssTTsTssTssTTsTssTssT'

export interface Track {
  title: string
  description: string
  /** Explicit line break used on the card (data-driven, not CSS luck). */
  descriptionLines: string[]
  artLabel: string
}

export const tracks: Track[] = [
  {
    title: 'Midnight Echo',
    description: 'Lose yourself in dreamy midnight sounds.',
    descriptionLines: ['Lose yourself in dreamy', 'midnight sounds.'],
    artLabel: 'Silhouette portrait on teal',
  },
  {
    title: 'Better Sleep',
    description: 'Relax your body, quiet your thoughts.',
    descriptionLines: ['Relax your body, quiet', 'your thoughts.'],
    artLabel: 'Portrait looking up on lilac',
  },
]

/** Cards peeking in from the right edge of each row. */
export const peekTracks: Track[] = [
  {
    title: 'Positive Vibes',
    description: 'Refresh and uplift your mood.',
    descriptionLines: ['Refresh and', 'uplift your mood.'],
    artLabel: 'Album art',
  },
  {
    title: 'Stress Relief',
    description: 'Breathe and release tension.',
    descriptionLines: ['Breathe and release', 'tension.'],
    artLabel: 'Album art',
  },
]

export interface LatestRelease {
  eyebrow: string
  titleLines: string[]
  coverLabel: string
}

export const latestReleases = {
  neon: { eyebrow: 'Latest', titleLines: ['Neon', 'Dreams'], coverLabel: 'Neon portrait cover' },
  crimson: { eyebrow: 'Latest', titleLines: ['Crimson', 'Pulse'], coverLabel: 'Red sunglasses portrait cover' },
} satisfies Record<string, LatestRelease>

export interface NavEntry {
  key: string
  icon?: LucideIcon
  /** Brand orb rendered as an image placeholder. */
  orb?: boolean
  accent?: boolean
}

export const navEntries: NavEntry[] = [
  { key: 'home', icon: House },
  { key: 'moods', icon: Bubbles },
  { key: 'orb', orb: true },
  { key: 'library', icon: BookOpenText, accent: true },
  { key: 'settings', icon: Settings, accent: true },
]

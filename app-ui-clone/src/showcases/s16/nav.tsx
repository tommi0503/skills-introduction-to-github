import { Bell, House, User } from 'lucide-react'
import type { NavEntry } from './components/BottomNav'
import { CompassGlyph } from './components/CompassGlyph'

/** Bottom navigation entries shared by the Location and Discover screens. */
export const navItems: NavEntry[] = [
  {
    key: 'home',
    label: 'Home',
    glyph: (active) => <House size={21} strokeWidth={1.7} fill={active ? 'currentColor' : 'none'} />,
  },
  {
    key: 'discover',
    label: 'Discover',
    glyph: (active) => <CompassGlyph size={19} filled={active} />,
  },
  { key: 'action', center: true },
  { key: 'alerts', label: 'Alerts', icon: Bell },
  { key: 'profile', label: 'Profile', icon: User },
]

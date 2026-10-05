import { BookUser, Plane, Users } from 'lucide-react'
import type { TabItem } from '../../ui'

export const navTabs: TabItem[] = [
  { key: 'flights', icon: Plane, label: 'My Flights' },
  { key: 'friends', icon: Users, label: 'Friends' },
  { key: 'passport', icon: BookUser, label: 'Passport' },
]
